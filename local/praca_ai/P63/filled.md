# Paczka AI P63 (Fala 3 · 3B) — Karty E.G.O, umiejętności i pasywki (część 3/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P63_3b_karty_ego_cz03.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P63_3b_karty_ego_cz03.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## E.G.O [20608] Tears of the Tarnished Blood [汚血泣淚] (오혈읍루 [汚血泣淚]) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20608`

1. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] [CantDuel]\n대상 수비 스킬 무시\n이 스킬은 적에게 적중하지 않음\n[EndSkill] [DragonLance] 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060811].levelList[level=3].desc ; dataList[id=2060811].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [EndSkill], [DragonLance]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [EndSkill] = [공격 종료시] / [Attack End]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]
   EN: [CantDuel]\nIgnores the target's Defense Skill\nThis Skill does not hit an enemy\n[EndSkill] Gain [DragonLance]<style="highlight"></style>
   PL: [CantDuel]\nignoruje Umiejętność Obrony celu\nta Umiejętność nie trafia wrogów\n[EndSkill] zyskuje [DragonLance]<style="highlight"></style>
2. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] 이 스킬의 최종 위력만큼 자신이 고정 피해를 받음\n- 이 피해로 흐트러지거나 체력이 1 미만으로 감소하지 않음<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n
   EN: This unit takes fixed damage by this Skill's Final Power\n- This damage does not Stagger or reduce this unit's HP below 1<style="highlight"></style>
   PL: ta jednostka otrzymuje obrażenia stałe równe Mocy Końcowej tej Umiejętności\n- te obrażenia nie Oszołamiają i nie obniżają HP tej jednostki poniżej 1<style="highlight"></style>
3. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 오혈읍루 - 종[終]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].name ; dataList[id=2060812].levelList[level=3].name ; dataList[id=2060812].levelList[level=4].name
   limit: do 60 znaków
   EN: Tears of the Tarnished Blood - The End [終]
   PL: Łzy Splamionej Krwi - Koniec [終]
4. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 응룡
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].abName ; dataList[id=2060812].levelList[level=3].abName ; dataList[id=2060812].levelList[level=4].abName
   limit: do 40 znaków
   EN: Yinglong
   PL: Yinglong
5. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 이 스킬은 E.G.O 자원을 소모하지 않음\n[CantDuel]\n자신의 [DragonLance] 수치당 피해량 +2% (최대 6%)\n자신의 [CondensedBlood] 수치당 피해량 +4% (최대 20%)\n[WhenUse] 메인 타겟의 [Burst]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [CondensedBlood]이 3 이상이면, 공격 가중치 +1, 기본 위력 +1\n[EndSkill] 자신의 [DragonLance], [CondensedBlood] 제거. 이후 사망
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [DragonLance], [CondensedBlood], [WhenUse], [Burst], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]; [CondensedBlood] = 오혈 / Tarnished Blood; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: This Skill does not consume E.G.O Resources\n[CantDuel]\nDeal +2% damage for every [DragonLance] on self (max 6%)\nDeal +4% damage for every [CondensedBlood] on self (max 20%)\n[WhenUse] If main target has 5+ [Burst], Coin Power +1\n[WhenUse] At 3+ [CondensedBlood], Atk Weight +1 and Base Power +1\n[EndSkill] Remove [DragonLance] and [CondensedBlood] from self, then dies
   PL: ta Umiejętność nie zużywa zasobów E.G.O\n[CantDuel]\nzadaje +2% obrażeń za każde [DragonLance] na tej jednostce (maks. 6%)\nzadaje +4% obrażeń za każde [CondensedBlood] na tej jednostce (maks. 20%)\n[WhenUse] przy 5+ [Burst] głównego celu Moc Monety +1\n[WhenUse] przy 3+ [CondensedBlood] Waga Ataku +1, Moc Bazowa +1\n[EndSkill] usuwa [DragonLance] i [CondensedBlood] od tej jednostki, po czym ginie
6. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Burst]
7. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
8. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
9. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
10. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 이 스킬은 E.G.O 자원을 소모하지 않음\n[CantDuel]\n자신의 [DragonLance] 수치당 피해량 <style="highlight">+3% (최대 9%)</style>\n자신의 [CondensedBlood] 수치당 피해량 <style="highlight">+6% (최대 30%)</style>\n<style="highlight">[WhenUse] 메인 타겟의 [Burst] 5당, 코인 위력 +1(최대 2)</style>\n[WhenUse] 자신의 [CondensedBlood]이 3 이상이면, 공격 가중치 +1, 기본 위력 +1\n<style="highlight">- 4 이상이면, 위 효과를 대신하여 공격 가중치 +2 , 기본 위력 +2</style>\n[EndSkill] 자신의 [DragonLance], [CondensedBlood] 제거. 이후 사망
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=3].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [DragonLance], [CondensedBlood], [WhenUse], [Burst], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]; [CondensedBlood] = 오혈 / Tarnished Blood; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: This Skill does not consume E.G.O Resources\n[CantDuel]\nDeal <style="highlight">+3%</style> damage for every [DragonLance] on self (max <style="highlight">9%</style>)\nDeal <style="highlight">+6%</style> damage for every [CondensedBlood] on self (max <style="highlight">30%</style>)\n<style="highlight">[WhenUse] Coin Power +1 for every 5 [Burst] on main target (max 2)</style>\n[WhenUse] At 3+ [CondensedBlood], Atk Weight +1 and Base Power +1\n<style="highlight">- At 4+ [CondensedBlood], Atk Weight +2 and Base Power +2 instead</style>\n[EndSkill] Remove [DragonLance] and [CondensedBlood] from self, then dies
   PL: ta Umiejętność nie zużywa zasobów E.G.O\n[CantDuel]\nzadaje <style="highlight">+3% (maks. 9%)</style> obrażeń za każde [DragonLance] na tej jednostce\nzadaje <style="highlight">+6% (maks. 30%)</style> obrażeń za każde [CondensedBlood] na tej jednostce\n<style="highlight">[WhenUse] Moc Monety +1 za każde 5 [Burst] głównego celu (maks. 2)</style>\n[WhenUse] przy 3+ [CondensedBlood] Waga Ataku +1, Moc Bazowa +1\n<style="highlight">- przy 4+ [CondensedBlood] zamiast tego Waga Ataku +2, Moc Bazowa +2</style>\n[EndSkill] usuwa [DragonLance] i [CondensedBlood] od tej jednostki, po czym ginie
11. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060812].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada +3 Licznika [Burst]<style="highlight"></style>
12. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2060812].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
13. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2060812].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=2060812].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 이 스킬은 E.G.O 자원을 소모하지 않음\n[CantDuel]\n자신의 [DragonLance] 수치당 피해량 +3% (최대 9%)\n자신의 [CondensedBlood] 수치당 피해량 +6% (최대 30%)\n[WhenUse] 메인 타겟의 [Burst] 5당, 코인 위력 +1(최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [CondensedBlood]이 3 이상이면, 공격 가중치 +1, 기본 위력 +1\n- 4 이상이면, 위 효과를 대신하여 공격 가중치 +2 , 기본 위력 +2\n<style="highlight">- 5 이상이면, 위 효과를 대신하여 공격 가중치 +3, 기본 위력 +3</style>\n[EndSkill] 자신의 [DragonLance], [CondensedBlood] 제거. 이후 사망
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060812].levelList[level=4].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [DragonLance], [CondensedBlood], [WhenUse], [Burst], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]; [CondensedBlood] = 오혈 / Tarnished Blood; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: This Skill does not consume E.G.O Resources\n[CantDuel]\nDeal +3% damage for every [DragonLance] on self (max 9%)\nDeal +6% damage for every [CondensedBlood] on self (max 30%)\n[WhenUse] Coin Power +1 for every 5 [Burst] on main target (max <style="highlight">3</style>)\n[WhenUse] At 3+ [CondensedBlood], Atk Weight +1 and Base Power +1\n- At 4+ [CondensedBlood], Atk Weight +2 and Base Power +2 instead\n<style="highlight">- At 5+ [CondensedBlood], Atk Weight +3 and Base Power +3 instead</style>\n[EndSkill] Remove [DragonLance] and [CondensedBlood] from self, then dies
   PL: ta Umiejętność nie zużywa zasobów E.G.O\n[CantDuel]\nzadaje +3% obrażeń za każde [DragonLance] na tej jednostce (maks. 9%)\nzadaje +6% obrażeń za każde [CondensedBlood] na tej jednostce (maks. 30%)\n[WhenUse] Moc Monety +1 za każde 5 [Burst] głównego celu (maks. <style="highlight">3</style>)\n[WhenUse] przy 3+ [CondensedBlood] Waga Ataku +1, Moc Bazowa +1\n- przy 4+ [CondensedBlood] zamiast tego Waga Ataku +2, Moc Bazowa +2\n<style="highlight">- przy 5+ [CondensedBlood] zamiast tego Waga Ataku +3, Moc Bazowa +3</style>\n[EndSkill] usuwa [DragonLance] i [CondensedBlood] od tej jednostki, po czym ginie
16. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 오혈읍루 - 시[始]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].name ; dataList[id=2060821].levelList[level=3].name ; dataList[id=2060821].levelList[level=4].name
   limit: do 60 znaków
   EN: Tears of the Tarnished Blood - Inception [始]
   PL: Łzy Splamionej Krwi - Początek [始]
17. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 응룡
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].abName ; dataList[id=2060821].levelList[level=3].abName ; dataList[id=2060821].levelList[level=4].abName
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 최대 공명 수가 4 이상이면, 공격 가중치 +1\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -8)\n[EndSkill] [DragonLance] 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [EndSkill], [DragonLance]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 4+ highest Reson., Atk Weight +1\n[BeforeAttack] -2 Base Power for every Cracked Coin (max -8)\n[EndSkill] Gain [DragonLance]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n[BeforeAttack] Moc Bazowa -2 za każdą zniszczoną Monetę (maks. -8)\n[EndSkill] zyskuje [DragonLance]
19. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2060821].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
20. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2060821].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2060821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] celu o 2<style="highlight"></style>
21. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2060821].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2060821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2060821].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2060821].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=2060821].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=2060821].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 최대 공명 수가 4 이상이면, 공격 가중치 +1\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -8)\n[EndSkill] [DragonLance] 얻음<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=3].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [EndSkill], [DragonLance]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 4+ highest Reson., Atk Weight +1\n[BeforeAttack] -2 Base Power for every Cracked Coin (max -8)\n[EndSkill] Gain [DragonLance]<style="highlight"></style>
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n[BeforeAttack] Moc Bazowa -2 za każdą zniszczoną Monetę (maks. -8)\n[EndSkill] zyskuje [DragonLance]<style="highlight"></style>
25. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2060821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
26. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2060821].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=2060821].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 최대 공명 수가 4 이상이면, 공격 가중치 +1\n<style="highlight">- 최대 공명 수가 6 이상이면, 위 효과를 대신하여 공격 가중치 +2</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2 (최대 -8)\n[EndSkill] [DragonLance] 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060821].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [EndSkill], [DragonLance]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [DragonLance] = 매화첨[埋花櫼] / Flower-burying Wedge [埋花櫼]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 4+ highest Reson., Atk Weight +1\n<style="highlight">- At 6+ highest Reson., Atk Weight +2 instead</style>\n[BeforeAttack] -2 Base Power for every Cracked Coin (max -8)\n[EndSkill] Gain [DragonLance]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n<style="highlight">- przy najwyższym Rezonansie 6+ zamiast tego Waga Ataku +2</style>\n[BeforeAttack] Moc Bazowa -2 za każdą zniszczoną Monetę (maks. -8)\n[EndSkill] zyskuje [DragonLance]
29. [Pasywka E.G.O — nazwa] 읍루
   źródło: Passive_Ego.json :: dataList[id=2060811].name
   limit: do 40 znaków
   EN: Crying Tears
   PL: Płaczące Łzy
30. [Pasywka E.G.O — opis] 자신의 공격, 반격 스킬 종료 시 대상이 사망했으면\n- 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n- 다음 턴에 자신을 포함한 모든 아군에게 해당 스킬의 물리, 죄악 속성의 피해량 증가를 1 부여 (턴 당 1회)\n- 다음 턴에 모든 적에게 [Reduction] 1 부여 (턴 당 1회)\n\n자신 사망시\n- 다음 턴에 모든 아군에게 [ShamrockDamageUp], [PenetrateDamageUp] 1 부여 (턴 당 1회)\n- 다음 턴에 모든 적에게 [Reduction] 1 부여 (턴 당 1회)
   źródło: Passive_Ego.json :: dataList[id=2060811].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Reduction], [ShamrockDamageUp], [PenetrateDamageUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [Reduction] = 공격 위력 감소 / Attack Power Down; [ShamrockDamageUp] = 탐식 피해량 증가 / Gluttony DMG Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: If the target is defeated after this unit's Attack or Counter Skills:\n- Gain 2 [Agility] next turn (once per turn)\n- To all allies, including this unit: next turn, apply 1 DMG Up to the Damage Type & Affinity of the Skill used to activate this effect (once per turn)\n- Inflict 1 [Reduction] to all enemies next turn (once per turn)\n\nWhen this unit dies:\n- Apply 1 [ShamrockDamageUp] and [PenetrateDamageUp] to all allies next turn (once per turn)\n- Inflict 1 [Reduction] to all enemies next turn (once per turn)
   PL: jeżeli cel ginie po Umiejętności ataku lub kontrataku tej jednostki\n- następnej tury zyskuje 2 [Agility] (1 raz na turę)\n- następnej tury nakłada na wszystkich sojuszników, wliczając tę jednostkę, 1 zwiększenia zadawanych obrażeń dla typu fizycznego i Grzechu tej Umiejętności (1 raz na turę)\n- następnej tury nakłada 1 [Reduction] na wszystkich wrogów (1 raz na turę)\n\nprzy śmierci tej jednostki\n- następnej tury nakłada 1 [ShamrockDamageUp] i 1 [PenetrateDamageUp] na wszystkich sojuszników (1 raz na turę)\n- następnej tury nakłada 1 [Reduction] na wszystkich wrogów (1 raz na turę)

## E.G.O [20609] To Remain Oneself [宁作吾] (영작오 [宁作吾]) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20609`

31. [Karta E.G.O — nazwa] 영작오 [宁作吾]
   źródło: Egos.json :: dataList[id=20609].name
   limit: do 40 znaków
   EN: To Remain Oneself [宁作吾]
   PL: To Remain Oneself [宁作吾]
32. [Karta E.G.O — opis] 홍루 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20609].desc
   limit: do 120 znaków
   EN: Hong Lu’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Hong Lu
33. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 영작오 [宁作吾]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=1].name ; dataList[id=2060911].levelList[level=3].name ; dataList[id=2060911].levelList[level=4].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 링
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=1].abName ; dataList[id=2060911].levelList[level=3].abName ; dataList[id=2060911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Ling
   PL: Ling
35. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음\n[BeforeAttack] [Breath] 위력과 [Breath] 횟수의 합이 5 이상이면, 최종 위력 +1\n[BeforeAttack] [Cianjing]이 있으면, 피해량 +15%\n[BeforeAttack] [SeniorCianjing]이 있으면, 피해량 +27%\n[EndSkill] [Cianjing] 5 얻음\n- [Cianjing] 또는 [SeniorCianjing]이 있으면, 전부 소모하고 [SeniorCianjing] 5 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [BeforeAttack], [Cianjing], [SeniorCianjing], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Gain 2 [Breath]\n[BeforeAttack] At 5+ ([Breath] Potency + [Breath] Count), Final Power +1\n[BeforeAttack] If this unit has [Cianjing], deal +15% damage\n[BeforeAttack] If this unit has [SeniorCianjing], deal +27% damage\n[EndSkill] Gain 5 [Cianjing]\n- If this unit has [Cianjing] or [SeniorCianjing], consume all of it and gain 5 [SeniorCianjing]
   PL: [WhenUse] zyskuje 2 [Breath]\n[BeforeAttack] przy sumie 5+ (Siła [Breath] + Licznik [Breath]) Moc Końcowa +1\n[BeforeAttack] jeżeli ta jednostka ma [Cianjing], zadaje +15% obrażeń\n[BeforeAttack] jeżeli ta jednostka ma [SeniorCianjing], zadaje +27% obrażeń\n[EndSkill] zyskuje 5 [Cianjing]\n- jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], zużywa je wszystkie i zyskuje 5 [SeniorCianjing]
36. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Cianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력/2)% (최대 15%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Cianjing], [Breath]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [Cianjing], deal +([Breath] Potency / 2)% damage on Critical Hit (max 15%)
   PL: jeżeli ta jednostka ma [Cianjing], zadaje +(Siła [Breath] / 2)% obrażeń przy trafieniu krytycznym (maks. 15%)
37. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [SeniorCianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합/2)% (최대 30%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [SeniorCianjing], [Breath]
   znaczenie tagów: [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [SeniorCianjing], deal +(([Breath] Potency + [Breath] Count) / 2)% damage on Critical Hit (max 30%)
   PL: jeżeli ta jednostka ma [SeniorCianjing], zadaje +((Siła [Breath] + Licznik [Breath]) / 2)% obrażeń przy trafieniu krytycznym (maks. 30%)
38. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]
39. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [WhenUse] [Breath] <style="highlight">3</style> 얻음\n[BeforeAttack] [Breath] 위력과 [Breath] 횟수의 합 <style="highlight">5당, 최종 위력 +1 (최대 2)</style>\n[BeforeAttack] [Cianjing]이 있으면, <style="highlight">공격 가중치 +1</style>, 피해량 +15%\n[BeforeAttack] [SeniorCianjing]이 있으면, <style="highlight">공격 가중치 +2</style>, 피해량 +27%\n[EndSkill] [Cianjing] 5 얻음\n- [Cianjing] 또는 [SeniorCianjing]이 있으면, 전부 소모하고 [SeniorCianjing] 5 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=3].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [BeforeAttack], [Cianjing], [SeniorCianjing], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Gain <style="highlight">3</style> [Breath]\n[BeforeAttack] <style="highlight">Final Power +1 for every 5 ([Breath] Potency + [Breath] Count) (max 2)</style>\n[BeforeAttack] If this unit has [Cianjing], gain <style="highlight">+1 Atk Weight</style> and deal +15% damage\n[BeforeAttack] If this unit has [SeniorCianjing], gain <style="highlight">+2 Atk Weight</style> and deal +27% damage\n[EndSkill] Gain 5 [Cianjing]\n- If this unit has [Cianjing] or [SeniorCianjing], consume all of it and gain 5 [SeniorCianjing]
   PL: [WhenUse] zyskuje <style="highlight">3</style> [Breath]\n[BeforeAttack] <style="highlight">Moc Końcowa +1 za każde 5 (Siła [Breath] + Licznik [Breath]) (maks. 2)</style>\n[BeforeAttack] jeżeli ta jednostka ma [Cianjing], <style="highlight">Waga Ataku +1</style>, zadaje +15% obrażeń\n[BeforeAttack] jeżeli ta jednostka ma [SeniorCianjing], <style="highlight">Waga Ataku +2</style>, zadaje +27% obrażeń\n[EndSkill] zyskuje 5 [Cianjing]\n- jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], zużywa je wszystkie i zyskuje 5 [SeniorCianjing]
40. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [Cianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력/2)% (최대 <style="highlight">20%</style>)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Cianjing], [Breath]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [Cianjing], deal +([Breath] Potency / 2)% damage on Critical Hit (max <style="highlight">20</style>%)
   PL: jeżeli ta jednostka ma [Cianjing], zadaje +(Siła [Breath] / 2)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">20%</style>)
41. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [SeniorCianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합/2)% (최대 <style="highlight">40%</style>)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SeniorCianjing], [Breath]
   znaczenie tagów: [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [SeniorCianjing], deal +(([Breath] Potency + [Breath] Count) / 2)% damage on Critical Hit (max <style="highlight">40</style>%)
   PL: jeżeli ta jednostka ma [SeniorCianjing], zadaje +((Siła [Breath] + Licznik [Breath]) / 2)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">40%</style>)
42. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Sinking]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Sinking]
43. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [WhenUse] [Breath] <style="highlight">4</style> 얻음\n[BeforeAttack] [Breath] 위력과 [Breath] 횟수의 합 5당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n<style="highlight">[BeforeAttack] [Cianjing], [SeniorCianjing]이 없으면, 이 스킬에서 소모한 E.G.O 자원과 정신력을 절반만큼 돌려받음 (소수점 <noparse>버림</noparse>. 이 효과는 각성 스킬 사용 시 침식되는 경우에도 적용됨)</style>\n[BeforeAttack] [Cianjing]이 있으면, 공격 가중치 +1, 피해량 <style="highlight">+25%</style>\n[BeforeAttack] [SeniorCianjing]이 있으면, 공격 가중치 +2, 피해량 <style="highlight">+45%</style>\n[EndSkill] [Cianjing] 5 얻음\n- [Cianjing] 또는 [SeniorCianjing]이 있으면, 전부 소모하고 [SeniorCianjing] 5 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=4].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [WhenUse], [Breath], [BeforeAttack], [Cianjing], [SeniorCianjing], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Gain <style="highlight">4</style> [Breath]\n[BeforeAttack] Final Power +1 for every 5 ([Breath] Potency + [Breath] Count) (max <style="highlight">3</style>)\n<style="highlight">[BeforeAttack] If this unit does not have [Cianjing] or [SeniorCianjing], recuperate half of E.G.O resources and SP consumed by this Skill (rounded down; this effect applies to Corrosion Skill as well if it activated due to the "To Corrode" probability when using the Awakening Skill)</style>\n[BeforeAttack] If this unit has [Cianjing], gain +1 Atk Weight and deal +<style="highlight">25</style>% damage\n[BeforeAttack] If this unit has [SeniorCianjing], gain +2 Atk Weight and deal +<style="highlight">45</style>% damage\n[EndSkill] Gain 5 [Cianjing]\n- If this unit has [Cianjing] or [SeniorCianjing], consume all of it and gain 5 [SeniorCianjing]
   PL: [WhenUse] zyskuje <style="highlight">4</style> [Breath]\n[BeforeAttack] Moc Końcowa +1 za każde 5 (Siła [Breath] + Licznik [Breath]) (maks. <style="highlight">3</style>)\n<style="highlight">[BeforeAttack] jeżeli ta jednostka nie ma [Cianjing] ani [SeniorCianjing], odzyskuje połowę zasobów E.G.O i SP zużytych przez tę Umiejętność (zaokrąglone w dół. ten efekt dotyczy także Umiejętności Korozji, jeżeli uruchomiła się przez prawdopodobieństwo „To Corrode” przy użyciu Umiejętności Przebudzenia)</style>\n[BeforeAttack] jeżeli ta jednostka ma [Cianjing], Waga Ataku +1, zadaje <style="highlight">+25%</style> obrażeń\n[BeforeAttack] jeżeli ta jednostka ma [SeniorCianjing], Waga Ataku +2, zadaje <style="highlight">+45%</style> obrażeń\n[EndSkill] zyskuje 5 [Cianjing]\n- jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], zużywa je wszystkie i zyskuje 5 [SeniorCianjing]
44. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Cianjing]이 있으면, 크리티컬 피해량 +(<style="highlight">[Breath] 위력</style>)% (최대 20%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Cianjing], [Breath]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [Cianjing], deal +(<style="highlight">[Breath] Potency</style>)% damage on Critical Hit (max 20%)
   PL: jeżeli ta jednostka ma [Cianjing], zadaje +(<style="highlight">Siła [Breath]</style>)% obrażeń przy trafieniu krytycznym (maks. 20%)
45. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [SeniorCianjing]이 있으면, 크리티컬 피해량 +(<style="highlight">[Breath] 위력과 [Breath] 횟수의 합</style>)% (최대 40%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SeniorCianjing], [Breath]
   znaczenie tagów: [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [SeniorCianjing], deal +(<style="highlight">[Breath] Potency + [Breath] Count</style>)% damage on Critical Hit (max 40%)
   PL: jeżeli ta jednostka ma [SeniorCianjing], zadaje +(<style="highlight">Siła [Breath] + Licznik [Breath]</style>)% obrażeń przy trafieniu krytycznym (maks. 40%)
46. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060911].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Sinking]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Sinking]
47. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 영작오 [宁作吾]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].name ; dataList[id=2060921].levelList[level=3].name ; dataList[id=2060921].levelList[level=4].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 링
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].abName ; dataList[id=2060921].levelList[level=3].abName ; dataList[id=2060921].levelList[level=4].abName
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] [Breath] 2 얻음, [Breath] 횟수 2 증가\n[BeforeAttack] [Cianjing] 또는 [SeniorCianjing]이 있으면, 코인 위력 +1\n[EndSkill] [Cianjing] 5 얻음\n- [Cianjing] 또는 [SeniorCianjing]이 있으면, 전부 소모하고 [SeniorCianjing] 5 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [Breath], [BeforeAttack], [Cianjing], [SeniorCianjing], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count\n[BeforeAttack] If this unit has [Cianjing] or [SeniorCianjing], Coin Power +1\n[EndSkill] Gain 5 [Cianjing]\n- If this unit has [Cianjing] or [SeniorCianjing], consume all of it and gain 5 [SeniorCianjing]
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] zyskuje 2 [Breath] i +2 Licznika [Breath]\n[BeforeAttack] jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], Moc Monety +1\n[EndSkill] zyskuje 5 [Cianjing]\n- jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], zużywa je wszystkie i zyskuje 5 [SeniorCianjing]
50. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
51. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 입힌 피해량의 10%만큼 오만 피해를 줌 (최대 10)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pride damage by 10% of the damage dealt (max 10)
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe 10% zadanych obrażeń (maks. 10)
52. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 입힌 피해량의 15%만큼 오만 피해를 줌 (최대 15)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pride damage by 15% of the damage dealt (max 15)
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe 15% zadanych obrażeń (maks. 15)
54. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 2 — opis] [Cianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력/2)% (최대 20%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Cianjing], [Breath]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [Cianjing], deal +([Breath] Potency / 2)% damage on Critical Hit (max 20%)
   PL: jeżeli ta jednostka ma [Cianjing], zadaje +(Siła [Breath] / 2)% obrażeń przy trafieniu krytycznym (maks. 20%)
56. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 3 — opis] [SeniorCianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합/2)% (최대 40%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [SeniorCianjing], [Breath]
   znaczenie tagów: [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [SeniorCianjing], deal +(([Breath] Potency + [Breath] Count) / 2)% damage on Critical Hit (max 40%)
   PL: jeżeli ta jednostka ma [SeniorCianjing], zadaje +((Siła [Breath] + Licznik [Breath]) / 2)% obrażeń przy trafieniu krytycznym (maks. 40%)
57. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 입힌 피해량의 25%만큼 오만 피해를 줌 (최대 25)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pride damage by 25% of the damage dealt (max 25)
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe 25% zadanych obrażeń (maks. 25)
59. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] [Breath] <style="highlight">3</style> 얻음, [Breath] 횟수 <style="highlight">3</style> 증가\n[BeforeAttack] [Cianjing] 또는 [SeniorCianjing]이 있으면, <style="highlight">공격 가중치 +1, 기본 위력 +1</style>, 코인 위력 +1\n[EndSkill] [Cianjing] 5 얻음\n- [Cianjing] 또는 [SeniorCianjing]이 있으면, 전부 소모하고 [SeniorCianjing] 5 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WhenUse], [Breath], [BeforeAttack], [Cianjing], [SeniorCianjing], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] Gain <style="highlight">3</style> [Breath] and +<style="highlight">3</style> [Breath] Count\n[BeforeAttack] If this unit has [Cianjing] or [SeniorCianjing], <style="highlight">gain +1 Atk Weight, Base Power +1</style>, and Coin Power +1\n[EndSkill] Gain 5 [Cianjing]\n- If this unit has [Cianjing] or [SeniorCianjing], consume all of it and gain 5 [SeniorCianjing]
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] zyskuje <style="highlight">3</style> [Breath] i +<style="highlight">3</style> Licznika [Breath]\n[BeforeAttack] jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], <style="highlight">Waga Ataku +1, Moc Bazowa +1</style>, Moc Monety +1\n[EndSkill] zyskuje 5 [Cianjing]\n- jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], zużywa je wszystkie i zyskuje 5 [SeniorCianjing]
60. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2060921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 입힌 피해량의 10%만큼 오만 피해를 줌 (최대 10)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2060921].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pride damage by 10% of the damage dealt (max 10)<style="highlight"></style>
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe 10% zadanych obrażeń (maks. 10)<style="highlight"></style>
62. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2060921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 입힌 피해량의 15%만큼 오만 피해를 줌 (최대 15)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2060921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pride damage by 15% of the damage dealt (max 15)<style="highlight"></style>
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe 15% zadanych obrażeń (maks. 15)<style="highlight"></style>
64. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2060921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 2 — opis] [Cianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력/2)% (최대 <style="highlight">30%</style>)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Cianjing], [Breath]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [Cianjing], deal +([Breath] Potency / 2)% damage on Critical Hit (max <style="highlight">30</style>%)
   PL: jeżeli ta jednostka ma [Cianjing], zadaje +(Siła [Breath] / 2)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">30%</style>)
66. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 3 — opis] [SeniorCianjing]이 있으면, 크리티컬 피해량 +([Breath] 위력과 [Breath] 횟수의 합/2)% (최대 <style="highlight">60%</style>)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SeniorCianjing], [Breath]
   znaczenie tagów: [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [SeniorCianjing], deal +(([Breath] Potency + [Breath] Count) / 2)% damage on Critical Hit (max <style="highlight">60</style>%)
   PL: jeżeli ta jednostka ma [SeniorCianjing], zadaje +((Siła [Breath] + Licznik [Breath]) / 2)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">60%</style>)
67. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 입힌 피해량의 25%만큼 오만 피해를 줌 (최대 25)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=3].coinlist[#2].coindescs[#4].desc ; dataList[id=2060921].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pride damage by 25% of the damage dealt (max 25)<style="highlight"></style>
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe 25% zadanych obrażeń (maks. 25)<style="highlight"></style>
69. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] [Breath] <style="highlight">4</style> 얻음, [Breath] 횟수 <style="highlight">4</style> 증가\n[BeforeAttack] [Cianjing] 또는 [SeniorCianjing]이 있으면, 공격 가중치 <style="highlight">+2</style>, 기본 위력 <style="highlight">+2</style>, 코인 위력 <style="highlight">+2</style>\n[EndSkill] [Cianjing] 5 얻음\n- [Cianjing] 또는 [SeniorCianjing]이 있으면, 전부 소모하고 [SeniorCianjing] 5 얻음
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WhenUse], [Breath], [BeforeAttack], [Cianjing], [SeniorCianjing], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] Gain <style="highlight">4</style> [Breath] and +<style="highlight">4</style> [Breath] Count\n[BeforeAttack] If this unit has [Cianjing] or [SeniorCianjing], gain +<style="highlight">2</style> Atk Weight, Base Power +<style="highlight">2</style>, and Coin Power +<style="highlight">2</style>\n[EndSkill] Gain 5 [Cianjing]\n- If this unit has [Cianjing] or [SeniorCianjing], consume all of it and gain 5 [SeniorCianjing]
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] zyskuje <style="highlight">4</style> [Breath] i +<style="highlight">4</style> Licznika [Breath]\n[BeforeAttack] jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], Waga Ataku <style="highlight">+2</style>, Moc Bazowa <style="highlight">+2</style>, Moc Monety <style="highlight">+2</style>\n[EndSkill] zyskuje 5 [Cianjing]\n- jeżeli ta jednostka ma [Cianjing] lub [SeniorCianjing], zużywa je wszystkie i zyskuje 5 [SeniorCianjing]
70. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 2 — opis] [Cianjing]이 있으면, 크리티컬 피해량 +(<style="highlight">[Breath] 위력</style>)% (최대 30%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Cianjing], [Breath]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [Cianjing], deal +(<style="highlight">[Breath] Potency</style>)% damage on Critical Hit (max 30%)
   PL: jeżeli ta jednostka ma [Cianjing], zadaje +(<style="highlight">Siła [Breath]</style>)% obrażeń przy trafieniu krytycznym (maks. 30%)
71. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 3 — opis] [SeniorCianjing]이 있으면, 크리티컬 피해량 +(<style="highlight">[Breath] 위력과 [Breath] 횟수의 합</style>)% (최대 60%)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SeniorCianjing], [Breath]
   znaczenie tagów: [SeniorCianjing] = 상급 시엔징 / Higher Thunderer; [Breath] = 호흡 / Poise
   EN: If this unit has [SeniorCianjing], deal +(<style="highlight">[Breath] Potency + [Breath] Count</style>)% damage on Critical Hit (max 60%)
   PL: jeżeli ta jednostka ma [SeniorCianjing], zadaje +(<style="highlight">Siła [Breath] + Licznik [Breath]</style>)% obrażeń przy trafieniu krytycznym (maks. 60%)
72. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Sinking] 2 부여, <style="highlight">[Sinking] 횟수 2 증가</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2060921].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] <style="highlight">and +2 [Sinking] Count</style>
   PL: [OnSucceedAttack] nakłada 2 [Sinking], <style="highlight">+2 Licznika [Sinking]</style>
73. [Pasywka E.G.O — nazwa] 시를 쓰고 술에 취하다
   źródło: Passive_Ego.json :: dataList[id=2060911].name
   limit: do 40 znaków
   EN: So is Writ, an Ode to Wine
   PL: Tak Spisana, Oda do Wina
74. [Pasywka E.G.O — opis] 턴 종료 시, 영작오 홍루 사용 시 소모되는 E.G.O 자원(나태, 우울, 오만) 중 가장 적게 보유한 E.G.O 자원 1개를 얻음\n\n이번 전투에서 [Cianjing], [SeniorCianjing]이 감소 또는 소모된 수치 1당 피해량 +1% (최대 15%)
   źródło: Passive_Ego.json :: dataList[id=2060911].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Cianjing], [SeniorCianjing]
   znaczenie tagów: [Cianjing] = 시엔징 / Thunderer; [SeniorCianjing] = 상급 시엔징 / Higher Thunderer
   EN: Turn End: among the E.G.O resources consumed to use To Remain Oneself Hong Lu(Sloth, Gloom, Pride), gain 1 E.G.O resource of the least-owned Affinity.\n\nDeal +1% damage for every [Cianjing] or [SeniorCianjing] Stack lost or consumed in this Encounter (max 15%)
   PL: Koniec tury: spośród zasobów E.G.O zużywanych przy użyciu To Remain Oneself Hong Lu (Nieczułość, Posępność, Pycha) zyskuje 1 zasób E.G.O najmniej posiadanego Grzechu.\n\nzadaje +1% obrażeń za każde 1 skumulowane zużycie lub utratę [Cianjing] lub [SeniorCianjing] w tej walce (maks. 15%)
75. [Pasywka E.G.O — podsumowanie] 턴 종료 시 E.G.O 자원 얻음\n시엔징, 상급 시엔징 감소 또는 소모 수치만큼 피해량 증가
   źródło: Passive_Ego.json :: dataList[id=2060911].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: gain E.G.O resources\nDeal more damage based on how much Thunderer or Higher Thunderer was lost or consumed
   PL: Koniec tury: zyskuje zasoby E.G.O\nzadaje więcej obrażeń w zależności od skumulowanego zużycia lub utraty Cianjingu lub Wyższego Cianjingu

## E.G.O [20610] Repudiation (거절선포) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20610`

76. [Karta E.G.O — nazwa] 거절선포
   źródło: Egos.json :: dataList[id=20610].name
   limit: do 40 znaków
   EN: Repudiation
   PL: Repudiacja
77. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20610].desc
   limit: do 120 znaków
   EN: Hong Lu’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Hong Lu
78. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 거절선포
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=1].name ; dataList[id=2061011].levelList[level=3].name ; dataList[id=2061011].levelList[level=4].name
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 메트로폴라리스의 주민
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=1].abName ; dataList[id=2061011].levelList[level=3].abName ; dataList[id=2061011].levelList[level=4].abName
   limit: do 40 znaków
   EN: Resident of Metropolaris
   PL: Mieszkaniec Metropolaris
80. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 자신의 [Charge] 횟수 1 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 6까지 소모하고, 자신과 자신을 제외한 무작위 아군 (1 + 소모한 [Charge] 횟수/2)명에게 [ChargeForceField] 5 부여 (최대 5명, 소수점 버림)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [ChargeForceField]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [BeforeAttack] Gain +1 [Charge] Count\n[BeforeAttack] Consume up to 6 [Charge] Count on self; then, apply 5 [ChargeForceField] on self and on (1 + ([Charge] Count consumed / 2)) random other allies (max 5 units; rounded down)
   PL: [BeforeAttack] zyskuje +1 Licznika [Charge]\n[BeforeAttack] zużywa do 6 Licznika [Charge] i nakłada 5 [ChargeForceField] na tę jednostkę oraz na (1 + (zużyty Licznik [Charge] / 2)) losowych innych sojuszników (maks. 5 jednostek, zaokrąglone w dół)
81. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2061011].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2061011].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2
82. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">[WhenUse] 자신의 [Charge] 위력만큼 <noparse>합 위력 증가</noparse> (최대 2)</style>\n[BeforeAttack] 자신의 [Charge] 횟수 <style="highlight">3</style> 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 <style="highlight">8</style>까지 소모하고, 자신과 자신을 제외한 무작위 아군 (1 + 소모한 [Charge] 횟수/2)명에게 [ChargeForceField] 5 부여 (최대 <style="highlight">6</style>명, 소수점 버림)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, <noparse>, </noparse>, </style>, \n, [WhenUse], [Charge], [BeforeAttack], [ChargeForceField]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: <style="highlight">[WhenUse] Gain Clash Power equal to [Charge] Potency on self (max 2)</style>\n[BeforeAttack] Gain +<style="highlight">3</style> [Charge] Count\n[BeforeAttack] Consume up to <style="highlight">8</style> [Charge] Count on self; then, apply 5 [ChargeForceField] on self and on (1 + ([Charge] Count consumed / 2)) random other allies (max <style="highlight">6</style> units; rounded down)
   PL: <style="highlight">[WhenUse] zyskuje Moc Walce równą Siły [Charge] tej jednostki (maks. 2)</style>\n[BeforeAttack] zyskuje <style="highlight">+3</style> Licznika [Charge]\n[BeforeAttack] zużywa do <style="highlight">8</style> Licznika [Charge] i nakłada 5 [ChargeForceField] na tę jednostkę oraz na (1 + (zużyty Licznik [Charge] / 2)) losowych innych sojuszników (maks. <style="highlight">6</style> jednostek, zaokrąglone w dół)
83. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [PhotoElectricity] 1 부여</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhotoElectricity] = 광전 / Photoelectricity
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [PhotoElectricity]</style>
   PL: <style="highlight">[OnSucceedAttack] nakłada 1 [PhotoElectricity]</style>
84. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 위력만큼 <noparse>합 위력 증가</noparse> (최대 <style="highlight">3</style>)\n[BeforeAttack] 자신의 [Charge] 횟수 <style="highlight">5</style> 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 <style="highlight">10</style>까지 소모하고, 자신과 자신을 제외한 무작위 아군 (1 + 소모한 [Charge] 횟수/2)명에게 [ChargeForceField] 5 부여 (최대 <style="highlight">7</style>명, 소수점 버림)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [WhenUse], [Charge], [BeforeAttack], [ChargeForceField]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [WhenUse] Gain Clash Power equal to [Charge] Potency on self (max <style="highlight">3</style>)\n[BeforeAttack] Gain +<style="highlight">5</style> [Charge] Count\n[BeforeAttack] Consume up to <style="highlight">10</style> [Charge] Count on self; then, apply 5 [ChargeForceField] on self and on (1 + ([Charge] Count consumed / 2)) random other allies (max <style="highlight">7</style> units; rounded down)
   PL: [WhenUse] zyskuje Moc Walce równą Siły [Charge] tej jednostki (maks. <style="highlight">3</style>)\n[BeforeAttack] zyskuje <style="highlight">+5</style> Licznika [Charge]\n[BeforeAttack] zużywa do <style="highlight">10</style> Licznika [Charge] i nakłada 5 [ChargeForceField] na tę jednostkę oraz na (1 + (zużyty Licznik [Charge] / 2)) losowych innych sojuszników (maks. <style="highlight">7</style> jednostek, zaokrąglone w dół)
85. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [PhotoElectricity] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061011].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [PhotoElectricity]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [PhotoElectricity]
86. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 거절선포
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].name ; dataList[id=2061021].levelList[level=3].name ; dataList[id=2061021].levelList[level=4].name
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 메트로폴라리스의 주민
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].abName ; dataList[id=2061021].levelList[level=3].abName ; dataList[id=2061021].levelList[level=4].abName
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n보호막을 보유한 대상에게 가하는 피해량 +15%\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -12)\n[BeforeAttack] 자신의 [Charge] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 6까지 소모하고, 자신과 자신을 제외한 무작위 아군 (1 + 소모한 [Charge] 횟수/2)명에게 [ChargeForceField] 7 부여 (최대 5명, 소수점 버림)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge], [ChargeForceField]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [CantIdentify]\nTargets randomly\nDeal +15% damage against targets that have Shield\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -12)\n[BeforeAttack] Gain +3 [Charge] Count\n[BeforeAttack] Consume up to 6 [Charge] Count; then, apply 7 [ChargeForceField] on self and on (1 + ([Charge] Count consumed / 2)) random other allies (max 5 units; rounded down)
   PL: [CantIdentify]\nAtakuje losowy cel\nzadaje +15% obrażeń celom posiadającym Tarczę\n[BeforeAttack] Moc Bazowa -6 za każdą zniszczoną Monetę (maks. -12)\n[BeforeAttack] zyskuje +3 Licznika [Charge]\n[BeforeAttack] zużywa do 6 Licznika [Charge] i nakłada 7 [ChargeForceField] na tę jednostkę oraz na (1 + (zużyty Licznik [Charge] / 2)) losowych innych sojuszników (maks. 5 jednostek, zaokrąglone w dół)
89. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2061021].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2061021].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2061021].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2061021].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2061021].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2061021].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 2 — opis] [OnStartCoin] 자신의 [Charge] 횟수를 최대 10까지 소모하고, 소모한 수치만큼 이 코인의 <noparse>최종 위력 증가</noparse>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2061021].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2061021].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: [OnStartCoin] Consume up to 10 [Charge] Count; then, this Coin gains Final Power equal to Count consumed
   PL: [OnStartCoin] zużywa do 10 Licznika [Charge], po czym ta Moneta zyskuje Moc Końcową równą zużytej wartości
93. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n보호막을 보유한 대상에게 가하는 피해량 +<style="highlight">20</style>%\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -12)\n<style="highlight">[BeforeAttack] 자신의 [Charge] 위력만큼 <noparse>최종 위력 증가</noparse> (최대 2)</style>\n[BeforeAttack] 자신의 [Charge] 횟수 <style="highlight">4</style> 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 <style="highlight">8</style>까지 소모하고, 자신과 자신을 제외한 무작위 아군 (1 + 소모한 [Charge] 횟수/2)명에게 [ChargeForceField] 7 부여 (최대 <style="highlight">6</style>명, 소수점 버림)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=3].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [CantIdentify], [BeforeAttack], [Charge], [ChargeForceField]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [CantIdentify]\nTargets randomly\nDeal +<style="highlight">20</style>% damage against targets that have Shield\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -12)\n<style="highlight">[BeforeAttack] Gain Final Power equal to [Charge] Potency on self (max 2)</style>\n[BeforeAttack] Gain +<style="highlight">4</style> [Charge] Count\n[BeforeAttack] Consume up to <style="highlight">8</style> [Charge] Count on self; then, apply 7 [ChargeForceField] on self and on (1 + ([Charge] Count consumed / 2)) random other allies (max <style="highlight">6</style> units; rounded down)
   PL: [CantIdentify]\nAtakuje losowy cel\nzadaje +<style="highlight">20</style>% obrażeń celom posiadającym Tarczę\n[BeforeAttack] Moc Bazowa -6 za każdą zniszczoną Monetę (maks. -12)\n<style="highlight">[BeforeAttack] zyskuje Moc Końcową równą Siły [Charge] tej jednostki (maks. 2)</style>\n[BeforeAttack] zyskuje <style="highlight">+4</style> Licznika [Charge]\n[BeforeAttack] zużywa do <style="highlight">8</style> Licznika [Charge] i nakłada 7 [ChargeForceField] na tę jednostkę oraz na (1 + (zużyty Licznik [Charge] / 2)) losowych innych sojuszników (maks. <style="highlight">6</style> jednostek, zaokrąglone w dół)
94. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] [PhotoElectricity] 1 부여</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n보호막을 보유한 대상에게 가하는 피해량 +<style="highlight">25</style>%\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -12)\n[BeforeAttack] 자신의 [Charge] 위력만큼 <noparse>최종 위력 증가</noparse> (최대 <style="highlight">3</style>)\n[BeforeAttack] 자신의 [Charge] 횟수 <style="highlight">5</style> 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 최대 <style="highlight">10</style>까지 소모하고, 자신과 자신을 제외한 무작위 아군 (1 + 소모한 [Charge] 횟수/2)명에게 [ChargeForceField] 7 부여 (최대 <style="highlight">7</style>명, 소수점 버림)
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [CantIdentify], [BeforeAttack], [Charge], [ChargeForceField]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [CantIdentify]\nTargets randomly\nDeal +<style="highlight">25</style>% damage against targets that have Shield\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -12)\n[BeforeAttack] Gain Final Power equal to [Charge] Potency on self (max <style="highlight">3</style>)\n[BeforeAttack] Gain +<style="highlight">5</style> [Charge] Count\n[BeforeAttack] Consume up to <style="highlight">10</style> [Charge] Count on self; then, apply 7 [ChargeForceField] on self and on (1 + ([Charge] Count consumed / 2)) random other allies (max <style="highlight">7</style> units; rounded down)
   PL: [CantIdentify]\nAtakuje losowy cel\nzadaje +<style="highlight">25</style>% obrażeń celom posiadającym Tarczę\n[BeforeAttack] Moc Bazowa -6 za każdą zniszczoną Monetę (maks. -12)\n[BeforeAttack] zyskuje Moc Końcową równą Siły [Charge] tej jednostki (maks. <style="highlight">3</style>)\n[BeforeAttack] zyskuje <style="highlight">+5</style> Licznika [Charge]\n[BeforeAttack] zużywa do <style="highlight">10</style> Licznika [Charge] i nakłada 7 [ChargeForceField] na tę jednostkę oraz na (1 + (zużyty Licznik [Charge] / 2)) losowych innych sojuszników (maks. <style="highlight">7</style> jednostek, zaokrąglone w dół)
96. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [PhotoElectricity] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061021].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Pasywka E.G.O — nazwa] 아무도 상처 받지 않는 도시
   źródło: Passive_Ego.json :: dataList[id=2061011].name
   limit: do 60 znaków
   EN: The City Where No One Can Hurt Another
   PL: Miasto, w Którym Nikogo Nie Da się Skrzywdzić
98. [Pasywka E.G.O — opis] [Charge] 횟수 최대치 +5\n\n[Charge] 횟수 또는 특수 [Charge]을 소모하는 스킬 3(E.G.O 스킬 제외)의 피해량 +10%\n\n턴 종료 시 이번 턴에 피격되지 않았으면, 정신력 4 회복\n- 자신이 빼기 코인 기본 공격 스킬을 2개 이상 보유했으면, 대신 정신력 4 감소 (이 효과로 정신력이 -40 미만이 되지 않음)
   źródło: Passive_Ego.json :: dataList[id=2061011].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Max [Charge] Count +5\n\nSkill 3 (except E.G.O Skills) that consume [Charge] Count or Unique [Charge] deals +10% damage\n\nTurn End: If this unit was not hit this turn, heal 4 SP\n- If this unit has 2+ Minus Coin Base Attack Skills, lose 4 SP instead (this effect cannot reduce this unit's SP below -40)
   PL: Maks. Licznik [Charge] +5\n\n3. Umiejętność tej jednostki (poza Umiejętnościami E.G.O) zużywająca Licznik [Charge] lub Szczególne [Charge] zadaje +10% obrażeń\n\nKoniec tury: jeżeli ta jednostka nie była trafiona w tej turze, odzyskuje 4 SP\n- jeżeli ta jednostka ma 2+ Podstawowe Umiejętności Ataku z Monetą Minus, zamiast tego traci 4 SP (nie obniża SP tej jednostki poniżej -40)

## E.G.O [20611] The Sword Sharpened with Tears (눈물로 벼려낸 검) — Hong Lu
- postać: Hong Lu (홍루) · ID E.G.O: `20611`

99. [Karta E.G.O — nazwa] 눈물로 벼려낸 검
   źródło: Egos.json :: dataList[id=20611].name
   limit: do 50 znaków
   EN: The Sword Sharpened with Tears
   PL: Ostrze Wykute z Łez
100. [Karta E.G.O — opis] 홍루의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20611].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 눈물로 벼려낸 검
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=1].name ; dataList[id=2061111].levelList[level=3].name ; dataList[id=2061111].levelList[level=4].name
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 절망의 기사
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=1].abName ; dataList[id=2061111].levelList[level=3].abName ; dataList[id=2061111].levelList[level=4].abName
   limit: do 40 znaków
   EN: The Knight of Despair
   PL: Rycerz Rozpaczy
103. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [CantChangeTarget]\n[SupportAlly]\n자신의 [DespairKnightEGOSword] 1당 피해량 +20%\n[BeforeAttack] 자신의 [DespairKnightEGOMind] 20당 피해량 +1%\n[BeforeAttack] 대상이 적이면, 공격 가중치 +2\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수 6 증가\n[BeforeAttack] 자신의 [DespairKnightEGOMind]가 999면, 전부 소모하여 다음 턴에 [CriticalDamageUp] 1 얻음\n\n[EndSkill] [DespairKnightEGOSword] 1 얻음\n[EndSkill] [DespairKnightEGOMind] 100 얻음\n\n[EndSkill] 대상이 아군이면,\n- [PersonalityBreath] 또는 [PersonalityCharge]이면, [AttackDmgUp] 2 부여\n- [Breath] 위력 5 부여\n- 대상의 [Breath] 횟수 3 증가\n- 대상의 [Charge] 횟수 6 증가\n- 자신의 최대 체력의 20%만큼 보호막을 부여\n- [DespairKnightEGOProtect] 부여
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=1].desc
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [SupportAlly], [DespairKnightEGOSword], [BeforeAttack], [DespairKnightEGOMind], [Breath], [Charge], [CriticalDamageUp], [EndSkill], [PersonalityBreath], [PersonalityCharge], [AttackDmgUp], [DespairKnightEGOProtect]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up …
   EN: [CantChangeTarget]\n[SupportAlly]\nDeal +20% damage for every [DespairKnightEGOSword] on self\n[BeforeAttack] Deal +1% damage for every 20 [DespairKnightEGOMind] on self\n[BeforeAttack] If target is an enemy, Atk Weight +2\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] Gain +6 [Charge] Count\n[BeforeAttack] At 999 [DespairKnightEGOMind], consume all [DespairKnightEGOMind] Stacks to gain 1 [CriticalDamageUp] next turn\n\n[EndSkill] Gain 1 [DespairKnightEGOSword]\n[EndSkill] Gain 100 [DespairKnightEGOMind]\n\n[EndSkill] If target is an ally:\n- If target is a [PersonalityBreath] or a [PersonalityCharge], apply 2 [AttackDmgUp]\n- Apply 5 [Breath] Potency\n- Apply +3 [Breath] Count on target\n- Apply +6 [Charge] Count on target\n- Apply Shield equal to 20% of this unit's max HP\n- Apply [DespairKnightEGOProtect]
   PL: [CantChangeTarget]\n[SupportAlly]\nzadaje +20% obrażeń za każde [DespairKnightEGOSword] na tej jednostce\n[BeforeAttack] zadaje +1% obrażeń za każde 20 [DespairKnightEGOMind] na tej jednostce\n[BeforeAttack] jeżeli celem jest wróg, Waga Ataku +2\n[BeforeAttack] zyskuje +3 Licznika [Breath]\n[BeforeAttack] zyskuje +6 Licznika [Charge]\n[BeforeAttack] przy 999 [DespairKnightEGOMind] zużywa wszystkie Liczniki [DespairKnightEGOMind], by następnej tury zyskać 1 [CriticalDamageUp]\n\n[EndSkill] zyskuje 1 [DespairKnightEGOSword]\n[EndSkill] zyskuje 100 [DespairKnightEGOMind]\n\n[EndSkill] jeżeli celem jest sojusznik:\n- jeżeli to [PersonalityBreath] lub [PersonalityCharge], nakłada 2 [AttackDmgUp]\n- nakłada 5 Siły [Breath]\n- nakłada +3 Licznika [Breath] na cel\n- nakłada +6 Licznika [Charge] na cel\n- nakłada Tarczę równą 20% Maks. HP tej jednostki\n- nakłada [DespairKnightEGOProtect]\n
104. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [CantChangeTarget]\n[SupportAlly]\n자신의 [DespairKnightEGOSword] 1당 피해량 +<style="highlight">30</style>%\n<style="highlight">이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +30% (집중 전투면, 부위로 판정)</style>\n[BeforeAttack] 자신의 [DespairKnightEGOMind] 20당 피해량 +1%\n[BeforeAttack] 대상이 적이면, 공격 가중치 +2\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수 6 증가\n[BeforeAttack] 자신의 [DespairKnightEGOMind]가 999면, 전부 소모하여 다음 턴에 [CriticalDamageUp] 1 얻음\n\n[EndSkill] [DespairKnightEGOSword] 1 얻음\n[EndSkill] [DespairKnightEGOMind] 100 얻음\n\n[EndSkill] 대상이 아군이면,\n- [PersonalityBreath] 또는 [PersonalityCharge]이면, [AttackDmgUp] 2 부여\n- [Breath] 위력 5 부여\n- 대상의 [Breath] 횟수 3 증가\n- 대상의 [Charge] 횟수 6 증가\n- 자신의 최대 체력의 20%만큼 보호막을 부여\n- [DespairKnightEGOProtect] 부여\n<style="highlight">- 자신과 대상의 정신력 15 회복</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=3].desc
   limit: do 1200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantChangeTarget], [SupportAlly], [DespairKnightEGOSword], [BeforeAttack], [DespairKnightEGOMind], [Breath], [Charge], [CriticalDamageUp], [EndSkill], [PersonalityBreath], [PersonalityCharge], [AttackDmgUp], [DespairKnightEGOProtect]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up …
   EN: [CantChangeTarget]\n[SupportAlly]\nDeal +<style="highlight">30</style>% damage for every [DespairKnightEGOSword] on self\n<style="highlight">Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)</style>\n[BeforeAttack] Deal +1% damage for every 20 [DespairKnightEGOMind] on self\n[BeforeAttack] If target is an enemy, Atk Weight +2\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] Gain +6 [Charge] Count\n[BeforeAttack] At 999 [DespairKnightEGOMind], consume all [DespairKnightEGOMind] Stacks to gain 1 [CriticalDamageUp] next turn\n\n[EndSkill] Gain 1 [DespairKnightEGOSword]\n[EndSkill] Gain 100 [DespairKnightEGOMind]\n\n[EndSkill] If target is an ally:\n- If target is a [PersonalityBreath] or a [PersonalityCharge], apply 2 [AttackDmgUp]\n- Apply 5 [Breath] Potency\n- Apply +3 [Breath] Count on target\n- Apply +6 [Charge] Count on target\n- Apply Shield equal to 20% of this unit's max HP\n- Apply [DespairKnightEGOProtect]\n<style="highlight">- Heal 15 SP on target and self</style>
   PL: [CantChangeTarget]\n[SupportAlly]\nzadaje +<style="highlight">30</style>% obrażeń za każde [DespairKnightEGOSword] na tej jednostce\n<style="highlight">zadaje +30% obrażeń za każdego celu ataku o Wadze Ataku niższej niż tej Umiejętności (w walkach skupionych rozpatrywane per Część)</style>\n[BeforeAttack] zadaje +1% obrażeń za każde 20 [DespairKnightEGOMind] na tej jednostce\n[BeforeAttack] jeżeli celem jest wróg, Waga Ataku +2\n[BeforeAttack] zyskuje +3 Licznika [Breath]\n[BeforeAttack] zyskuje +6 Licznika [Charge]\n[BeforeAttack] przy 999 [DespairKnightEGOMind] zużywa wszystkie Liczniki [DespairKnightEGOMind], by następnej tury zyskać 1 [CriticalDamageUp]\n\n[EndSkill] zyskuje 1 [DespairKnightEGOSword]\n[EndSkill] zyskuje 100 [DespairKnightEGOMind]\n\n[EndSkill] jeżeli celem jest sojusznik:\n- jeżeli to [PersonalityBreath] lub [PersonalityCharge], nakłada 2 [AttackDmgUp]\n- nakłada 5 Siły [Breath]\n- nakłada +3 Licznika [Breath] na cel\n- nakłada +6 Licznika [Charge] na cel\n- nakłada Tarczę równą 20% Maks. HP tej jednostki\n- nakłada [DespairKnightEGOProtect]\n<style="highlight">- odzyskuje 15 SP na tej jednostce i celu</style>
107. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2061111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2061111].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [CantChangeTarget]\n[SupportAlly]\n자신의 [DespairKnightEGOSword] 1당 피해량 +<style="highlight">50</style>%\n이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +<style="highlight">50</style>% (집중 전투면, 부위로 판정)\n[BeforeAttack] 자신의 [DespairKnightEGOMind] 20당 피해량 +1%\n[BeforeAttack] 대상이 적이면, 공격 가중치 +2\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수 6 증가\n[BeforeAttack] 자신의 [DespairKnightEGOMind]가 999면, 전부 소모하여 다음 턴에 [CriticalDamageUp] 1 얻음\n\n[EndSkill] [DespairKnightEGOSword] 1 얻음\n[EndSkill] [DespairKnightEGOMind] 100 얻음\n\n[EndSkill] 대상이 아군이면,\n- [PersonalityBreath] 또는 [PersonalityCharge]이면, [AttackDmgUp] 2 부여\n- [Breath] 위력 5 부여\n- 대상의 [Breath] 횟수 3 증가\n- 대상의 [Charge] 횟수 6 증가\n- 자신의 최대 체력의 20%만큼 보호막을 부여\n- [DespairKnightEGOProtect] 부여\n- 자신과 대상의 정신력 15 회복\n<style="highlight">- 대상이 보유한 해제 가능한 부정적인 효과 중 무작위 1개 제거</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=4].desc
   limit: do 1280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantChangeTarget], [SupportAlly], [DespairKnightEGOSword], [BeforeAttack], [DespairKnightEGOMind], [Breath], [Charge], [CriticalDamageUp], [EndSkill], [PersonalityBreath], [PersonalityCharge], [AttackDmgUp], [DespairKnightEGOProtect]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up …
   EN: [CantChangeTarget]\n[SupportAlly]\nDeal +<style="highlight">50</style>% damage for every [DespairKnightEGOSword] on self\nDeal +<style="highlight">50</style>% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[BeforeAttack] Deal +1% damage for every 20 [DespairKnightEGOMind] on self\n[BeforeAttack] If target is an enemy, Atk Weight +2\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] Gain +6 [Charge] Count\n[BeforeAttack] At 999 [DespairKnightEGOMind], consume all [DespairKnightEGOMind] Stacks to gain 1 [CriticalDamageUp] next turn\n\n[EndSkill] Gain 1 [DespairKnightEGOSword]\n[EndSkill] Gain 100 [DespairKnightEGOMind]\n\n[EndSkill] If target is an ally:\n- If target is a [PersonalityBreath] or a [PersonalityCharge], apply 2 [AttackDmgUp]\n- Apply 5 [Breath] Potency\n- Apply +3 [Breath] Count on target\n- Apply +6 [Charge] Count on target\n- Apply Shield equal to 20% of this unit's max HP\n- Apply [DespairKnightEGOProtect]\n- Heal 15 SP on target and self\n<style="highlight">- Remove 1 random removable negative effect applied on target</style>
   PL: [CantChangeTarget]\n[SupportAlly]\nzadaje +<style="highlight">50</style>% obrażeń za każde [DespairKnightEGOSword] na tej jednostce\nzadaje +<style="highlight">50</style>% obrażeń za każdego celu ataku o Wadze Ataku niższej niż tej Umiejętności (w walkach skupionych rozpatrywane per Część)\n[BeforeAttack] zadaje +1% obrażeń za każde 20 [DespairKnightEGOMind] na tej jednostce\n[BeforeAttack] jeżeli celem jest wróg, Waga Ataku +2\n[BeforeAttack] zyskuje +3 Licznika [Breath]\n[BeforeAttack] zyskuje +6 Licznika [Charge]\n[BeforeAttack] przy 999 [DespairKnightEGOMind] zużywa wszystkie Liczniki [DespairKnightEGOMind], by następnej tury zyskać 1 [CriticalDamageUp]\n\n[EndSkill] zyskuje 1 [DespairKnightEGOSword]\n[EndSkill] zyskuje 100 [DespairKnightEGOMind]\n\n[EndSkill] jeżeli celem jest sojusznik:\n- jeżeli to [PersonalityBreath] lub [PersonalityCharge], nakłada 2 [AttackDmgUp]\n- nakłada 5 Siły [Breath]\n- nakłada +3 Licznika [Breath] na cel\n- nakłada +6 Licznika [Charge] na cel\n- nakłada Tarczę równą 20% Maks. HP tej jednostki\n- nakłada [DespairKnightEGOProtect]\n- odzyskuje 15 SP na tej jednostce i celu\n<style="highlight">- usuwa 1 losowy usuwalny negatywny efekt nałożony na cel</style>
110. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">크리티컬 피해량 +30%</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061111].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Deal +30% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +30% obrażeń przy trafieniu krytycznym</style>
111. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 눈물로 벼려낸 검
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=1].name ; dataList[id=2061121].levelList[level=3].name ; dataList[id=2061121].levelList[level=4].name
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 절망의 기사
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=1].abName ; dataList[id=2061121].levelList[level=3].abName ; dataList[id=2061121].levelList[level=4].abName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [DespairKnightEGOSword] 1당 최종 위력 +2\n[BeforeAttack] 자신의 [DespairKnightEGOMind] 10당 피해량 +1%\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수 6 증가\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -3 (최대 9)\n\n[EndSkill] 자신의 ([DespairKnightEGOSword] x 5)만큼 정신력을 회복하고, 효과 소멸\n[EndSkill] 자신의 [DespairKnightEGOMind] 소멸
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [DespairKnightEGOSword], [BeforeAttack], [DespairKnightEGOMind], [Breath], [Charge], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\nFinal Power +2 for every [DespairKnightEGOSword] on self\n[BeforeAttack] Deal +1% damage for every 10 [DespairKnightEGOMind] on self\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] Gain +6 [Charge] Count\n[BeforeAttack] Base Power -3 for every Cracked Coin (max 9)\n\n[EndSkill] Heal SP equal to ([DespairKnightEGOSword] on self x 5); then, [DespairKnightEGOSword] expires\n[EndSkill] [DespairKnightEGOMind] on self expires
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Końcowa +2 za każde [DespairKnightEGOSword] na tej jednostce\n[BeforeAttack] zadaje +1% obrażeń za każde 10 [DespairKnightEGOMind] na tej jednostce\n[BeforeAttack] zyskuje +3 Licznika [Breath]\n[BeforeAttack] zyskuje +6 Licznika [Charge]\n[BeforeAttack] Moc Bazowa -3 za każdą zniszczoną Monetę (maks. 9)\n\n[EndSkill] odzyskuje SP równe ([DespairKnightEGOSword] na tej jednostce x 5), po czym ten efekt wygasa\n[EndSkill] [DespairKnightEGOMind] na tej jednostce wygasa
114. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n자신의 [DespairKnightEGOSword] 1당 최종 위력 +2\n<style="highlight">이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +30% (집중 전투면, 부위로 판정)</style>\n[BeforeAttack] 자신의 [DespairKnightEGOMind] 10당 피해량 +1%\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수 6 증가\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -3 (최대 9)\n\n[EndSkill] 자신의 ([DespairKnightEGOSword] x 5)만큼 정신력을 회복하고, 효과 소멸\n[EndSkill] 자신의 [DespairKnightEGOMind] 소멸
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [DespairKnightEGOSword], [BeforeAttack], [DespairKnightEGOMind], [Breath], [Charge], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\nFinal Power +2 for every [DespairKnightEGOSword] on self\n<style="highlight">Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)</style>\n[BeforeAttack] Deal +1% damage for every 10 [DespairKnightEGOMind] on self\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] Gain +6 [Charge] Count\n[BeforeAttack] Base Power -3 for every Cracked Coin (max 9)\n\n[EndSkill] Heal SP equal to ([DespairKnightEGOSword] on self x 5); then, [DespairKnightEGOSword] expires\n[EndSkill] [DespairKnightEGOMind] on self expires
   PL: [CantIdentify]\nAtakuje losowy cel\nMoc Końcowa +2 za każde [DespairKnightEGOSword] na tej jednostce\n<style="highlight">zadaje +30% obrażeń za każdego celu ataku o Wadze Ataku niższej niż tej Umiejętności (w walkach skupionych rozpatrywane per Część)</style>\n[BeforeAttack] zadaje +1% obrażeń za każde 10 [DespairKnightEGOMind] na tej jednostce\n[BeforeAttack] zyskuje +3 Licznika [Breath]\n[BeforeAttack] zyskuje +6 Licznika [Charge]\n[BeforeAttack] Moc Bazowa -3 za każdą zniszczoną Monetę (maks. 9)\n\n[EndSkill] odzyskuje SP równe ([DespairKnightEGOSword] na tej jednostce x 5), po czym ten efekt wygasa\n[EndSkill] [DespairKnightEGOMind] na tej jednostce wygasa
118. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2061121].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [PenetrateResultUp] 1 얻음 (턴당 1회)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: <style="highlight">[OnSucceedAttack] Gain 1 [PenetrateResultUp] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] następnej tury zyskuje 1 [PenetrateResultUp] (1 raz na turę)</style>
120. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2061121].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [PenetrateDamageUp] 1 얻음 (턴당 1회)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: <style="highlight">[OnSucceedAttack] Gain 1 [PenetrateDamageUp] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] następnej tury zyskuje 1 [PenetrateDamageUp] (1 raz na turę)</style>
122. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2061121].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [IndigoDamageUp] 1 얻음 (턴당 1회)</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [IndigoDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IndigoDamageUp] = 오만 피해량 증가 / Pride DMG Up
   EN: <style="highlight">[OnSucceedAttack] Gain 1 [IndigoDamageUp] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] następnej tury zyskuje 1 [IndigoDamageUp] (1 raz na turę)</style>
124. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">자신의 [DespairKnightEGOMind]가 999면, 최종 위력 +3</style>\n자신의 [DespairKnightEGOSword] 1당 최종 위력 +<style="highlight">3</style>\n이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +<style="highlight">50</style>% (집중 전투면, 부위로 판정)\n<style="highlight">사망 상태인 아군 1명당 피해량 +10%</style>\n[BeforeAttack] 자신의 [DespairKnightEGOMind] 10당 피해량 +1%\n[BeforeAttack] 자신의 [Breath] 횟수 3 증가\n[BeforeAttack] 자신의 [Charge] 횟수 6 증가\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -3 (최대 9)\n\n[EndSkill] 자신의 ([DespairKnightEGOSword] x 5)만큼 정신력을 회복하고, 효과 소멸\n[EndSkill] 자신의 [DespairKnightEGOMind] 소멸
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=4].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [DespairKnightEGOMind], [DespairKnightEGOSword], [BeforeAttack], [Breath], [Charge], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">At 999 [DespairKnightEGOMind], Final Power +3</style>\nFinal Power +<style="highlight">3</style> for every [DespairKnightEGOSword] on self\nDeal +<style="highlight">50</style>% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n<style="highlight">Deal +10% damage for every defeated ally</style>\n[BeforeAttack] Deal +1% damage for every 10 [DespairKnightEGOMind] on self\n[BeforeAttack] Gain +3 [Breath] Count\n[BeforeAttack] Gain +6 [Charge] Count\n[BeforeAttack] Base Power -3 for every Cracked Coin (max 9)\n\n[EndSkill] Heal SP equal to ([DespairKnightEGOSword] on self x 5); then, [DespairKnightEGOSword] expires\n[EndSkill] [DespairKnightEGOMind] on self expires
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">przy 999 [DespairKnightEGOMind] Moc Końcowa +3</style>\nMoc Końcowa +<style="highlight">3</style> za każde [DespairKnightEGOSword] na tej jednostce\nzadaje +<style="highlight">50</style>% obrażeń za każdego celu ataku o Wadze Ataku niższej niż tej Umiejętności (w walkach skupionych rozpatrywane per Część)\n<style="highlight">zadaje +10% obrażeń za każdego pokonanego sojusznika</style>\n[BeforeAttack] zadaje +1% obrażeń za każde 10 [DespairKnightEGOMind] na tej jednostce\n[BeforeAttack] zyskuje +3 Licznika [Breath]\n[BeforeAttack] zyskuje +6 Licznika [Charge]\n[BeforeAttack] Moc Bazowa -3 za każdą zniszczoną Monetę (maks. 9)\n\n[EndSkill] odzyskuje SP równe ([DespairKnightEGOSword] na tej jednostce x 5), po czym ten efekt wygasa\n[EndSkill] [DespairKnightEGOMind] na tej jednostce wygasa
125. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateResultUp] 1 얻음 (턴당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: [OnSucceedAttack] Gain 1 [PenetrateResultUp] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] następnej tury zyskuje 1 [PenetrateResultUp] (1 raz na turę)<style="highlight"></style>
126. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateDamageUp] 1 얻음 (턴당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [OnSucceedAttack] Gain 1 [PenetrateDamageUp] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] następnej tury zyskuje 1 [PenetrateDamageUp] (1 raz na turę)<style="highlight"></style>
127. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">크리티컬 피해량 +30%</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여</style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [PenetrateTakeDamageUp] w następnej turze</style>
129. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [IndigoDamageUp] 1 얻음 (턴당 1회)<style="highlight"></style>
   źródło: Skills_Ego_Personality-06.json :: dataList[id=2061121].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [IndigoDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IndigoDamageUp] = 오만 피해량 증가 / Pride DMG Up
   EN: [OnSucceedAttack] Gain 1 [IndigoDamageUp] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] następnej tury zyskuje 1 [IndigoDamageUp] (1 raz na turę)<style="highlight"></style>
130. [Pasywka E.G.O — nazwa] 절망속에서
   źródło: Passive_Ego.json :: dataList[id=2061111].name
   limit: do 40 znaków
   EN: From the Depths of Despair
   PL: Z Głębin Rozpaczy
131. [Pasywka E.G.O — opis] 자신의 1.5를 초과하는 물리 내성이 1.5로 조정됨 (흐트러짐 상태 제외)\n자신이 흐트러짐 상태면, 받는 피해량 -30% (강제 흐트러짐 포함)\n\n자신의 [DespairKnightEGOMind]가 999면, '눈물로 벼려낸 검' E.G.O 스킬(각성, 침식) 사용 시 E.G.O 자원을 소모하지 않음\n\n자신을 포함한 아군이 받은 피해만큼 [DespairKnightEGOMind] 얻음 (보호막 피해 포함)\n아군 사망시 [DespairKnightEGOSword] 1 얻음 (턴당 1회)\n[DespairKnightEGOProtect]를 보유한 아군 사망 시 [DespairKnightEGOSword] 1 얻음 (턴당 1회)\n\n사망 상태인 아군 2명당 자신의 공격 레벨 +1, 방어 레벨 -1 (최대 5)
   źródło: Passive_Ego.json :: dataList[id=2061111].desc
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: \n, [DespairKnightEGOMind], [DespairKnightEGOSword], [DespairKnightEGOProtect]
   znaczenie tagów: [DespairKnightEGOMind] = 닳아버린 긍지 / Weathered Pride; [DespairKnightEGOSword] = 눈물로 벼려낸 검 / Sword Sharpened with Tears; [DespairKnightEGOProtect] = 기사의 수호 / The Knight's Loyal Protection
   EN: This unit's Attack Type Resist. that are higher than 1.5 are adjusted to 1.5 (except while Staggered)\nIf this unit is Staggered, take -30% damage (including forced Staggers)\n\nAt 999 [DespairKnightEGOMind], does not consume E.G.O resource when using the "The Sword Sharpened with Tears" E.G.O Skill (both Awakening and Corrosion)\n\nGain [DespairKnightEGOMind] equal to damage taken by allies (including this unit; including Shield damage)\nOn Ally Death, gain 1 [DespairKnightEGOSword] (once per turn)\nWhen an ally that has [DespairKnightEGOProtect] is defeated, gain 1 [DespairKnightEGOSword] (once per turn)\n\nOffense Level +1 and Defense Level -1 for every 2 defeated allies (max 5)
   PL: Odporności tej jednostki na typy ataku wyższe niż 1,5 są korygowane do 1,5 (z wyłączeniem stanu Oszołomienia)\njeżeli ta jednostka jest Oszołomiona, otrzymuje -30% obrażeń (w tym wymuszone Oszołomienie)\n\nprzy 999 [DespairKnightEGOMind] użycie Umiejętności E.G.O „The Sword Sharpened with Tears” (zarówno Przebudzenia, jak i Korozji) nie zużywa zasobów E.G.O\n\nzyskuje [DespairKnightEGOMind] równe obrażeniom otrzymanym przez sojuszników, wliczając tę jednostkę (wliczając obrażenia Tarczy)\nprzy śmierci sojusznika zyskuje 1 [DespairKnightEGOSword] (1 raz na turę)\nprzy pokonaniu sojusznika posiadającego [DespairKnightEGOProtect] zyskuje 1 [DespairKnightEGOSword] (1 raz na turę)\n\nPoziom Ataku +1 i Poziom Obrony -1 za każdych 2 pokonanych sojuszników (maks. 5)
132. [Pasywka E.G.O — podsumowanie] 내성 강화, 받는 피해량이 감소.
   źródło: Passive_Ego.json :: dataList[id=2061111].summary
   limit: do 120 znaków
   EN: Strengthen Resist., take less damage
   PL: Wzmocnienie odporności, zmniejszenie otrzymywanych obrażeń.

## E.G.O [20701] Bodysack (시체자루) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20701`

133. [Karta E.G.O — nazwa] 시체자루
   źródło: Egos.json :: dataList[id=20701].name
   limit: do 40 znaków
   EN: Bodysack
   PL: Worek z Zwłok
134. [Karta E.G.O — opis] 히스클리프 기본 EGO 장비
   źródło: Egos.json :: dataList[id=20701].desc
   limit: do 120 znaków
   EN: Heathcliff’s Base E.G.O
   PL: Podstawowe E.G.O Heathcliffa
135. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 시체자루
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=1].name ; dataList[id=2070111].levelList[level=3].name ; dataList[id=2070111].levelList[level=4].name
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 히스클리프
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=1].abName ; dataList[id=2070111].levelList[level=3].abName ; dataList[id=2070111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
137. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Enhancement]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [OnSucceedAttackHead] Gain 1 [Enhancement] next turn
   PL: [OnSucceedAttackHead] następnej tury zyskuje 1 [Enhancement]
138. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 신속 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 2 [Agility] next turn
   PL: [OnSucceedAttackHead] Zyskuje 2 Pośpiechu w następnej turze
139. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Enhancement]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [OnSucceedAttack] Gain 1 [Enhancement] next turn
   PL: [OnSucceedAttack] następnej tury zyskuje 1 [Enhancement]
140. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 신속 3 얻음
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2070111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 3 [Agility] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 3 Pośpiechu
141. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EnemyKill] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills_Ego.json :: dataList[id=2070111].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] Gain 2 [Enhancement] next turn
   PL: [EnemyKill] następnej tury zyskuje 2 [Enhancement]
142. [Pasywka E.G.O — nazwa] 오기
   źródło: Passive_Ego.json :: dataList[id=2070111].name
   limit: do 40 znaków
   EN: Vying Spirit
   PL: Zawziętość
143. [Pasywka E.G.O — opis] 다른 아군이 적을 처치하면 다음 턴 시작 시 공격 위력 증가 1, 신속 1을 얻음 (최대 3)
   źródło: Passive_Ego.json :: dataList[id=2070111].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Agility]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste
   EN: When another ally defeats an enemy, gain 1 [Enhancement] and 1 [Agility] at the next Turn Start (max 3)
   PL: jeżeli inny sojusznik pokonuje wroga, na początku następnej tury zyskuje 1 [Enhancement] i 1 [Agility] (maks. 3)

## E.G.O [20702] Telepole (전봇대) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20702`

144. [Karta E.G.O — nazwa] 전봇대
   źródło: Egos.json :: dataList[id=20702].name
   limit: do 40 znaków
   EN: Telepole
   PL: Telepole
145. [Karta E.G.O — opis] 히스클리프 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20702].desc
   limit: do 120 znaków
   EN: Heathcliff’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Heathcliffa
146. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 전봇대
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=1].name ; dataList[id=2070211].levelList[level=3].name ; dataList[id=2070211].levelList[level=4].name
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 골목파수견
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=1].abName ; dataList[id=2070211].levelList[level=3].abName ; dataList[id=2070211].levelList[level=4].abName
   limit: do 40 znaków
   EN: Alleyway Watchdog
   PL: Pies Stróżujący Zaułków
148. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 충전 횟수 5를 소모하여 스킬 위력 +3
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Spend 5 [Charge] Count to gain +3 Skill Power
   PL: zużywa 5 Licznika [Charge], by zyskać +3 Mocy Umiejętności
149. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 자신의 충전 횟수 3 증가
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Charge]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackTail] Gain +3 [Charge] Count
   PL: [OnSucceedAttackTail] zyskuje +3 Licznika [Charge]
150. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [WhenUse] 질투 공명 수만큼 자신의 충전 횟수 증가\n충전 횟수 5를 소모하여 스킬 위력 +3
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain [Charge] Count by Envy Reson.\nSpend 5 [Charge] Count to gain +3 Skill Power
   PL: [WhenUse] zyskuje Licznika [Charge] równe Rezonansowi Zawiści\nzużywa 5 Licznika [Charge], by zyskać +3 Mocy Umiejętności
151. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 자신의 충전 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070211].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Charge]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackTail] Gain +5 [Charge] Count
   PL: [OnSucceedAttackTail] zyskuje +5 Licznika [Charge]
152. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [WhenUse] 질투 공명 수만큼 자신의 충전 횟수 증가\n충전 횟수 5를 소모할때마다 스킬 위력 +3 (최대 12)
   źródło: Skills_Ego.json :: dataList[id=2070211].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain [Charge] Count by Envy Reson.\nSpend 5 [Charge] Count to gain +3 Skill Power (Max 12)
   PL: [WhenUse] zyskuje Licznik [Charge] równy Rezonansowi Zawiści\nza każde 5 zużytych Licznika [Charge] +3 Mocy Umiejętności (maks. 12)
153. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 전봇대
   źródło: Skills_Ego.json :: dataList[id=2070221].levelList[level=1].name ; dataList[id=2070221].levelList[level=3].name ; dataList[id=2070221].levelList[level=4].name
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 골목파수견
   źródło: Skills_Ego.json :: dataList[id=2070221].levelList[level=1].abName ; dataList[id=2070221].levelList[level=3].abName ; dataList[id=2070221].levelList[level=4].abName
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n충전 횟수 전부 소모하여 스킬 위력 +6
   źródło: Skills_Ego.json :: dataList[id=2070221].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Charge] = 충전 / Charge
   EN: [CantIdentify] Targets randomly\nSpend all [Charge] Count to gain +6 Skill Power
   PL: [CantIdentify]\nAtakuje losowy cel\nzużywa wszystkie Liczniki [Charge], by zyskać +6 Mocy Umiejętności
156. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 3 얻음
   źródło: Skills_Ego.json :: dataList[id=2070221].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070221].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070221].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackHead] Gain 3 [Vulnerable] next turn
   PL: [OnSucceedAttackHead] następnej tury zyskuje 3 [Vulnerable]
157. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse]질투 공명 수만큼 자신의 충전 횟수 증가\n충전 횟수 전부 소모하여 스킬 위력 +10
   źródło: Skills_Ego.json :: dataList[id=2070221].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [CantIdentify] Targets randomly\n[WhenUse] Gain [Charge] Count by Envy Reson.\nSpend all [Charge] Count to gain +10 Skill Power
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] zyskuje Licznika [Charge] równe Rezonansowi Zawiści\nzużywa wszystkie Liczniki [Charge], by zyskać +10 Mocy Umiejętności
158. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse]질투 공명 수만큼 자신의 충전 횟수 증가\n충전 횟수 전부 소모하여 스킬 위력 +15
   źródło: Skills_Ego.json :: dataList[id=2070221].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [CantIdentify] Targets randomly\n[WhenUse] Gain [Charge] Count by Envy Reson.\nSpend all [Charge] Count to gain +15 Skill Power
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] zyskuje Licznika [Charge] równe Rezonansowi Zawiści\nzużywa wszystkie Liczniki [Charge], by zyskać +15 Mocy Umiejętności
159. [Pasywka E.G.O — nazwa] 포효
   źródło: Passive_Ego.json :: dataList[id=2070211].name
   limit: do 40 znaków
   EN: Roar
   PL: Ryk
160. [Pasywka E.G.O — opis] 적 처치 시 해당 턴의 (질투 완전 공명 수/2)만큼 충전 횟수 증가
   źródło: Passive_Ego.json :: dataList[id=2070211].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: On Enemy Kill, gain +(the turn's Envy A-Reson. / 2) [Charge] Count
   PL: przy pokonaniu wroga zyskuje (Absolutnego Rezonansu Zawiści w tej turze / 2) Licznika [Charge]

## E.G.O [20703] AEDD (AEDD) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20703`

161. [Karta E.G.O — nazwa] AEDD
   źródło: Egos.json :: dataList[id=20703].name
   limit: do 40 znaków
   EN: AEDD
   PL: AEDD
162. [Karta E.G.O — opis] 히스클리프의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20703].desc
   limit: do 120 znaków
   EN: Heathcliff’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Heathcliffa
163. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] AEDD
   źródło: Skills_Ego.json :: dataList[id=2070311].levelList[level=1].name ; dataList[id=2070311].levelList[level=3].name
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 충격 지네
   źródło: Skills_Ego.json :: dataList[id=2070311].levelList[level=1].abName ; dataList[id=2070311].levelList[level=3].abName
   limit: do 40 znaków
   EN: Shock Centipede
   PL: Wstrząsowa Stonoga
165. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 자신의 잃은 체력의 10%당 충전 횟수 1 증가 (최대 5)\n다음 턴에 신속 2를 얻음
   źródło: Skills_Ego.json :: dataList[id=2070311].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [Agility]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: [BeforeAttack] Gain +1 [Charge] Count for every 10% of missing HP (Max 5)\nGain 2 [Agility] next turn
   PL: [BeforeAttack] zyskuje +1 Licznika [Charge] za każde 10% brakującego HP (maks. 5)\nzyskuje 2 [Agility] następnej tury
166. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Ego.json :: dataList[id=2070311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis]
   PL: [OnSucceedAttack] Nakłada 3 Paraliżu
167. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신의 잃은 체력의 10%당 충전 횟수 1 증가 (최대 7)\n다음 턴에 신속 2를 얻음
   źródło: Skills_Ego.json :: dataList[id=2070311].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge], [Agility]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: [BeforeAttack] Gain +1 [Charge] Count for every 10% of missing HP (Max 7)\nGain 2 [Agility] next turn
   PL: [BeforeAttack] zyskuje +1 Licznika [Charge] za każde 10% brakującego HP (maks. 7)\nzyskuje 2 [Agility] następnej tury
168. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 3, 우울 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2070311].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] and 1 Gloom Fragility
   PL: [OnSucceedAttack] nakłada 3 [Paralysis] i 1 Kruchości Posępności
169. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] AEDD
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=1].name ; dataList[id=2070321].levelList[level=3].name ; dataList[id=2070321].levelList[level=4].name
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 충격 지네
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=1].abName ; dataList[id=2070321].levelList[level=3].abName ; dataList[id=2070321].levelList[level=4].abName
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 잃은 체력의 10%당 충전 횟수 1 증가 (최대 5)\n다음 턴에 신속 2를 얻음
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain +1 [Charge] Count for every 10% of missing HP (Max 5)\nGain 2 [Agility] next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje +1 Licznika [Charge] za każde 10% brakującego HP (maks. 5)\nzyskuje 2 [Agility] następnej tury
172. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수를 전부 소모하여 피해량의 (소모한 충전 횟수 x 1.5)% 만큼 우울 속성 추가 피해를 줌 (최대 30%)
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Spend all [Charge] Count to deal bonus Gloom damage by ([Charge] Count * 1.5)% of damage dealt (Max 30%)
   PL: [OnSucceedAttack] zużywa wszystkie Liczniki [Charge], zadając dodatkowe obrażenia Posępności równe (zużyty Licznik [Charge] x 1,5)% zadanych obrażeń (maks. 30%)
173. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 공격 종료 시 체력을 최대 체력의 10%만큼 소모하여 자신의 충전 횟수 7 증가
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Charge]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackTail] After the attack, lose 10% of Max HP to gain +7 [Charge] Count
   PL: [OnSucceedAttackTail] na koniec ataku zużywa 10% Maks. HP, zyskując +7 Licznika [Charge]
174. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 잃은 체력의 10%당 충전 횟수 1 증가 (최대 7)\n다음 턴에 신속 2를 얻음
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=3].desc ; dataList[id=2070321].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain +1 [Charge] Count for every 10% of missing HP (Max 7)\nGain 2 [Agility] next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje +1 Licznika [Charge] za każde 10% brakującego HP (maks. 7)\nzyskuje 2 [Agility] następnej tury
175. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수를 전부 소모하여 피해량의 (소모한 충전 횟수 x 2.5)% 만큼 우울 속성 추가 피해를 줌 (최대 50%)
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070321].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Spend all [Charge] Count to deal bonus Gloom damage by ([Charge] Count * 2.5)% of damage dealt (Max 50%)
   PL: [OnSucceedAttack] zużywa wszystkie Liczniki [Charge], zadając dodatkowe obrażenia Posępności równe (zużyty Licznik [Charge] x 2,5)% zadanych obrażeń (maks. 50%)
176. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 공격 종료 시 체력을 최대 체력의 10%만큼 소모하여 자신의 충전 횟수 10 증가
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Charge]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackTail] After the attack, lose 10% of Max HP to gain +10 [Charge] Count
   PL: [OnSucceedAttackTail] na koniec ataku zużywa 10% Maks. HP, zyskując +10 Licznika [Charge]
177. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 충전 횟수 전부 소모
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Charge]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Charge] = 충전 / Charge
   EN: [EndSkill] Spend all [Charge] Count
   PL: [EndSkill] zużywa wszystkie Liczniki [Charge]
178. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EndSkillTail] 체력을 최대 체력의 10%만큼 소모하여 자신의 충전 횟수 10 증가
   źródło: Skills_Ego.json :: dataList[id=2070321].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillTail], [Charge]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]; [Charge] = 충전 / Charge
   EN: [EndSkillTail] Lose HP by 10% of Max HP to gain +10 [Charge] Count
   PL: [EndSkillTail] zużywa 10% Maks. HP, zyskując +10 Licznika [Charge]
179. [Pasywka E.G.O — nazwa] 신경질적인 방전
   źródło: Passive_Ego.json :: dataList[id=2070311].name
   limit: do 40 znaków
   EN: Temperamental Discharge
   PL: Pobudliwe Wyładowanie
180. [Pasywka E.G.O — opis] 피격 시 충전 횟수를 1 소모하여 최대 체력의 2.5%만큼 체력 회복\n피격 시 체력이 40%미만인 경우 충전 횟수가 1 증가한 뒤, 체력 회복 효과가 발동됨 (충전 횟수는 턴 당 최대 10까지 증가 가능)
   źródło: Passive_Ego.json :: dataList[id=2070311].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When hit, consume 1 [Charge] Count to heal 2.5% HP\nAt less than 40% HP, gain +1 [Charge] Count before activating the healing effect (can gain up to 10 [Charge] Count per turn)
   PL: przy trafieniu zużywa 1 Licznika [Charge], by odzyskać 2,5% HP\nprzy trafieniu przy HP niższym niż 40% najpierw zyskuje +1 Licznika [Charge], a następnie uruchamia efekt leczenia (Licznik [Charge] może wzrosnąć maks. o 10 na turę)

## E.G.O [20704] Ya Śūnyatā Tad Rūpam (공즉시색) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20704`

181. [Karta E.G.O — nazwa] 공즉시색
   źródło: Egos.json :: dataList[id=20704].name
   limit: do 40 znaków
   EN: Ya Śūnyatā Tad Rūpam
   PL: Ya Śūnyatā Tad Rūpam
182. [Karta E.G.O — opis] 히스클리프의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20704].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 공즉시색
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=1].name ; dataList[id=2070411].levelList[level=3].name ; dataList[id=2070411].levelList[level=4].name
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 나는 비워내느니
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=1].abName ; dataList[id=2070411].levelList[level=3].abName ; dataList[id=2070411].levelList[level=4].abName
   limit: do 40 znaków
   EN: My Form Empties
   PL: Moja Forma Pusteje
185. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spadku Mocy Ataku
186. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndSkill] 자신을 제외하고 정신력이 가장 낮은 아군 4명의 정신력 12 회복
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 12 SP for 4 other allies with the least SP
   PL: [EndSkill] odzyskuje 12 SP dla 4 innych sojuszników z najniższym SP
187. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 자신의 정신력이 15 이상이면 공격 가중치 +1
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 15+ SP, gain +1 Atk Weight
   PL: [BeforeAttack] przy SP 15+ Waga Ataku +1
188. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 2 부여
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 2 [Reduction] next turn
   PL: [OnSucceedAttack] nakłada 2 [Reduction] następnej tury
189. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [EndSkill] 자신을 제외하고 정신력이 가장 낮은 아군 4명의 정신력 17 회복
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 17 SP for 4 other allies with the least SP
   PL: [EndSkill] odzyskuje 17 SP dla 4 innych sojuszników z najniższym SP
190. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 자신의 정신력이 15 이상이면 공격 가중치 +2
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] At 15+ SP, gain +2 Atk Weight
   PL: [BeforeAttack] przy SP 15+ Waga Ataku +2
191. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 자신을 제외하고 정신력이 가장 낮은 아군 4명의 정신력 25 회복
   źródło: Skills_Ego.json :: dataList[id=2070411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 25 SP for 4 other allies with the least SP
   PL: [EndSkill] odzyskuje 25 SP dla 4 innych sojuszników z najniższym SP
192. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 공즉시색
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=1].name ; dataList[id=2070421].levelList[level=3].name ; dataList[id=2070421].levelList[level=4].name
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 나는 비워내느니
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=1].abName ; dataList[id=2070421].levelList[level=3].abName ; dataList[id=2070421].levelList[level=4].abName
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets randomly
   PL: [CantIdentify]\nAtakuje losowy cel
195. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신을 제외한 아군 1명에게 방어 레벨 감소 3 부여
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070421].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown] to 1 random other ally
   PL: [OnSucceedAttack] nakłada 3 [DefenseDown] na 1 losowego innego sojusznika
196. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 2 얻음.
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2070421].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2070421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn.
   PL: [OnSucceedAttack] następnej tury zyskuje 2 zwiększenia Poziomu Obrony.
197. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 피해량 증가 1 얻음.
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2070421].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2070421].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn.
   PL: [OnSucceedAttack] następnej tury zyskuje 1 zwiększenia zadawanych obrażeń.
198. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 정신력이 -15 이하면, 공격 가중치 +1
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At -15 or lower SP, gain +1 Atk Weight
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy SP -15 lub niższym Waga Ataku +1
199. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttackTail] 자신의 정신력 4 회복
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2070421].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Heal 4 SP on self
   PL: [OnSucceedAttackTail] odzyskuje 4 SP
200. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 정신력이 -15 이하면, 공격 가중치 +2
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At -15 or lower SP, gain +2 Atk Weight
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy SP -15 lub niższym Waga Ataku +2
201. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttackTail] 취약 1 부여
   źródło: Skills_Ego.json :: dataList[id=2070421].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackTail] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttackTail] nakłada 1 [Vulnerable]
202. [Pasywka E.G.O — nazwa] 참선
   źródło: Passive_Ego.json :: dataList[id=2070411].name
   limit: do 40 znaków
   EN: Dhyāna
   PL: Dhyāna
203. [Pasywka E.G.O — opis] 흐트러짐 상태에서 회복될 때, 최대 체력이 인격의 기본 최대 체력의 15%만큼 증가.\n이후 체력을 현재 최대 체력의 15%만큼 회복. 현재 체력이 현재 최대 체력의 30% 미만인 경우, 대신 25%만큼 회복.\n(스테이지당 최대 3회 발동. 스테이지 종료 시 최대 체력 증가가 해제되며, 해제 시점의 체력 비율에 맞게 현재 체력이 조정됨.)
   źródło: Passive_Ego.json :: dataList[id=2070411].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Raise Max HP equal to 15% of this Identity's base Max HP when recovering from Stagger.\nThen, heal 15% of current Max HP. If this unit has less than 30% of its current Max HP, heal 25% of current Max HP instead (3 times per Encounter. At Encounter End, revert to base Max HP. Current HP value will be adjusted to reflect the HP percentage at the time of Encounter End)
   PL: przy dochodzeniu do siebie z Oszołomienia Maks. HP tej jednostki rośnie o 15% bazowych Maks. HP Tożsamości.\nnastępnie odzyskuje 15% aktualnych Maks. HP; przy HP niższym niż 30% aktualnych Maks. HP odzyskuje zamiast tego 25%.\n(uruchamia się maks. 3 razy na walkę. na koniec walki Maks. HP wraca do wartości bazowej, a aktualne HP zostaje dostosowane do procentowego HP z chwili zakończenia walki.)

## E.G.O [20705] Holiday (홀리데이) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20705`

204. [Karta E.G.O — nazwa] 홀리데이
   źródło: Egos.json :: dataList[id=20705].name
   limit: do 40 znaków
   EN: Holiday
   PL: Holiday
205. [Karta E.G.O — opis] 히스클리프의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20705].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 홀리데이
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070511].levelList[level=1].name ; dataList[id=2070511].levelList[level=3].name ; dataList[id=2070511].levelList[level=4].name
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 산돌프
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070511].levelList[level=1].abName ; dataList[id=2070511].levelList[level=3].abName ; dataList[id=2070511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Sandolph
   PL: Sandolph
208. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과의 위력을 2 + (최대 탐식 완전 공명의 수)회 부여 (최대 5)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070511].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070511].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Randomly select one of the following effects: Burn, Bleed, Tremor, Rupture, or Sinking. Then, inflict 1 Potency of the selected effect next turn.\nRepeat the above process (2 + (Highest Glut. A-Reson.)) times. (5 times max)
   PL: [OnSucceedAttackHead] następnej tury nakłada po 1 Siły losowo wybranego z efektów: Podpalenie, Krwawienie, Wstrząs, Rozdarcie lub Zatonięcie (2 + (Absolutnego Rezonansu Obżarstwa)) razy. (maks. 5 razy)
209. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [EnemyKill] 무작위 아군 2명에게 다음 턴에 호흡 횟수 1, 충전 횟수 1, 신속 1, 공격 레벨 증가 1, 방어 레벨 증가 1 중 무작위 1개 효과를 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070511].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Randomly select one of the following effects: 1 Poise Count, 1 Charge Count, 1 Haste, 1 Offense Level Up, or 1 Defense Level Up. Then, apply the selected effect to 2 random allies next turn
   PL: [EnemyKill] następnej tury losowo wybrany z efektów: 1 Licznika Równowagi, 1 Licznika [Charge], 1 Pośpiechu, 1 zwiększenia Poziomu Ataku lub 1 zwiększenia Poziomu Obrony zostaje nałożony na 2 losowych sojuszników
210. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과의 위력을 2 + (최대 탐식 완전 공명의 수)회 부여 (최대 7)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Randomly select one of the following effects: Burn, Bleed, Tremor, Rupture, or Sinking. Then, inflict 1 Potency of the selected effect next turn.\nRepeat the above process (2 + (Highest Glut. A-Reson.)) times. (7 times max)
   PL: [OnSucceedAttack] następnej tury nakłada po 1 Siły losowo wybranego z efektów: Podpalenie, Krwawienie, Wstrząs, Rozdarcie lub Zatonięcie (2 + (Absolutnego Rezonansu Obżarstwa)) razy. (maks. 7 razy)
211. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EnemyKill] 무작위 아군 2명에게 다음 턴에 호흡 횟수 2, 충전 횟수 2, 신속 2, 공격 레벨 증가 2, 방어 레벨 증가 2 중 무작위 1개 효과를 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Randomly select one of the following effects: 2 Poise Count, 2 Charge Count, 2 Haste, 2 Offense Level Up, or 2 Defense Level Up. Then, apply the selected effect to 2 random allies next turn
   PL: [EnemyKill] następnej tury losowo wybrany 1 z efektów: 2 Licznika Równowagi, 2 Licznika [Charge], 2 Pośpiechu, 2 zwiększenia Poziomu Ataku lub 2 zwiększenia Poziomu Obrony zostaje nałożony na 2 losowych sojuszników
212. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 홀리데이
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070521].levelList[level=1].name ; dataList[id=2070521].levelList[level=3].name ; dataList[id=2070521].levelList[level=4].name
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 산돌프
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070521].levelList[level=1].abName ; dataList[id=2070521].levelList[level=3].abName ; dataList[id=2070521].levelList[level=4].abName
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n정신력이 가장 높은 대상 공격\n[BeforeAttack] 대상에게 정신력 10 피해
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070521].levelList[level=1].desc ; dataList[id=2070521].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets the unit with the Most SP\n[BeforeAttack] Target loses 10 SP
   PL: [CantIdentify]\nAtakuje cel z najwyższym SP\n[BeforeAttack] zadaje celowi 10 obrażeń SP
215. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과의 위력을 2 + (최대 탐식 완전 공명의 수)회 부여 (최대 7)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070521].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070521].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n정신력이 가장 높은 대상 공격\n메인 공격 대상의 정신력이 15 이상이면 가중치 +1\n[BeforeAttack] 대상에게 정신력 10 피해
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070521].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets the unit with the Most SP\nIf the main target's SP is higher than 15, Atk Weight +1\n[BeforeAttack] Target loses 10 SP
   PL: [CantIdentify]\nAtakuje cel z najwyższym SP\njeżeli SP głównego celu ataku wynosi 15+, Waga Ataku +1\n[BeforeAttack] zadaje celowi 10 obrażeń SP
217. [Pasywka E.G.O — nazwa] 무한한 증오
   źródło: Passive_Ego.json :: dataList[id=2070511].name
   limit: do 40 znaków
   EN: Infinite Hatred
   PL: Nieskończona Nienawiść
218. [Pasywka E.G.O — opis] 자신에게 상태 이상 또는 부정적인 효과가 있을 때, 메인 공격 대상 또는 자신을 공격하는 대상에게 긍정적인 효과가 있으면, 스킬, 코인 효과로 자신과 적에게 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 +1, 스킬, 코인 효과로 자신이 얻는 호흡, 충전 횟수 +1
   źródło: Passive_Ego.json :: dataList[id=2070511].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [Breath], [Charge]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Breath] = 호흡 / Poise; [Charge] = 충전 / Charge
   EN: When this unit has a status effect or a negative effect, and if the main target or the attacker has a positive effect:\n- Inflict +1 more [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] Potency to self and enemies with Skill effects or Coin effects\n- Gain +1 more [Breath] and [Charge] Count with Skill effects or Coin effects
   PL: gdy ta jednostka ma stan lub negatywny efekt, a główny cel ataku lub atakujący tę jednostkę ma pozytywny efekt:\n- efekty Umiejętności i Monety nakładają +1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia na tę jednostkę i wrogów\n- efekty Umiejętności i Monety dają +1 więcej Licznika [Breath] i [Charge] tej jednostce

## E.G.O [20706] Binds (구속) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20706`

219. [Karta E.G.O — nazwa] 구속
   źródło: Egos.json :: dataList[id=20706].name
   limit: do 40 znaków
   EN: Binds
   PL: Niewola
220. [Karta E.G.O — opis] 히스클리프의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20706].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 구속
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=1].name ; dataList[id=2070611].levelList[level=3].name ; dataList[id=2070611].levelList[level=4].name
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 묶인 왕
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=1].abName ; dataList[id=2070611].levelList[level=3].abName ; dataList[id=2070611].levelList[level=4].abName
   limit: do 40 znaków
   EN: The King in Binds
   PL: Król w Okowach
223. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — opis] [EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소\n[EndSkill] 다음 턴에 [Binding] 20, [ForwardToTheKing] 1, [Enhancement] 1 얻음
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=1].desc ; dataList[id=2070611].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [Binding], [ForwardToTheKing], [Enhancement]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [ForwardToTheKing] = 왕의 앞으로 / Before the King; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndSkill] For 3 turns, lose 10 SP at Turn End\n[EndSkill] Next turn, gain 20 [Binding], 1 [ForwardToTheKing], and 1 [Enhancement]
   PL: [EndSkill] przez 3 tury traci 10 SP na koniec tury\n[EndSkill] następnej tury zyskuje 20 [Binding], 1 [ForwardToTheKing] i 1 [Enhancement]
224. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] Nakłada 4 [Sinking]
225. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] Nakłada 4 [Vibration]
226. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]
227. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]
228. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2070611].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2070611].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2070611].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소\n[EndSkill] 다음 턴에 [Binding] 20, [ForwardToTheBoundKing] 1, [Enhancement] 2 얻음
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070611].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [Binding], [ForwardToTheBoundKing], [Enhancement]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [ForwardToTheBoundKing] = 묶인 왕의 앞으로 / Before the King in Binds; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndSkill] For 3 turns, lose 10 SP at Turn End\n[EndSkill] Next turn, gain 20 [Binding], 1 [ForwardToTheBoundKing], and 2 [Enhancement]
   PL: [EndSkill] przez 3 tury traci 10 SP na koniec tury\n[EndSkill] następnej tury zyskuje 20 [Binding], 1 [ForwardToTheBoundKing] i 2 [Enhancement]
232. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 구속
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].name ; dataList[id=2070621].levelList[level=3].name ; dataList[id=2070621].levelList[level=4].name
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 묶인 왕
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].abName ; dataList[id=2070621].levelList[level=3].abName ; dataList[id=2070621].levelList[level=4].abName
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 다음 턴에 [Binding] 20, [ForwardToTheKing] 1, [Enhancement] 2 얻음\n[EndSkill] 다음 턴에 편성 순으로 자신을 제외한 아군 2명에게 [Binding] 20, [Enhancement] 3 부여\n- (우울 또는 오만 중 높은 공명 수 - 2)만큼 부여 대상 수 증가 (최대 2명)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [Binding], [ForwardToTheKing], [Enhancement]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [ForwardToTheKing] = 왕의 앞으로 / Before the King; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Next turn, gain 20 [Binding], 1 [ForwardToTheKing], and 2 [Enhancement]\n[EndSkill] Next turn, apply 20 [Binding] and 3 [Enhancement] to 2 other allies in the order of Deployment\n- The number of affected allies grows by (highest Gloom or Pride Reson. - 2) (max 2)
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] następnej tury zyskuje 20 [Binding], 1 [ForwardToTheKing] i 2 [Enhancement]\n[EndSkill] następnej tury nakłada 20 [Binding] i 3 [Enhancement] na 2 innych sojuszników według kolejności depozyzu\n- liczba objętych sojuszników rośnie o (wyższego z Rezonansów Posępności lub Pychy - 2) (maks. 2 sojuszników)
235. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070621].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 3 [Binding] następnej tury
236. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2070621].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2070621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2070621].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2070621].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=1].coinlist[#0].coindescs[#3].desc ; dataList[id=2070621].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2070621].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 다음 턴에 [Binding] 20, [ForwardToTheKing] 1, [Enhancement] 2 얻음\n[EndSkill] 다음 턴에 편성 순으로 자신을 제외한 아군 2명에게 [Binding] 20, [Enhancement] 3, <style="highlight">[AzureDamageUp]</style> 1 부여\n- (우울 또는 오만 중 높은 공명 수 - 2)만큼 부여 대상 수 증가 (최대 <style="highlight">3</style>명)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=3].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [Binding], [ForwardToTheKing], [Enhancement], [AzureDamageUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [ForwardToTheKing] = 왕의 앞으로 / Before the King; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AzureDamageUp] = 우울 피해량 증가 / Gloom DMG Up
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Next turn, gain 20 [Binding], 1 [ForwardToTheKing], and 2 [Enhancement]\n[EndSkill] Next turn, apply 20 [Binding], 3 [Enhancement], and 1 <style="highlight">[AzureDamageUp]</style> to 2 other allies in the order of Deployment\n- The number of affected allies grows by (highest Gloom or Pride Reson. - 2) (max <style="highlight">3</style>)
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] następnej tury zyskuje 20 [Binding], 1 [ForwardToTheKing] i 2 [Enhancement]\n[EndSkill] następnej tury nakłada 20 [Binding], 3 [Enhancement] i 1 <style="highlight">[AzureDamageUp]</style> na 2 innych sojuszników według kolejności depozyzu\n- liczba objętych sojuszników rośnie o (wyższego z Rezonansów Posępności lub Pychy - 2) (maks. <style="highlight">3</style> sojuszników)
240. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 다음 턴에 [Binding] 20, [ForwardToTheKing] 1, [Enhancement] 3 얻음\n[EndSkill] 다음 턴에 편성 순으로 자신을 제외한 아군 2명에게 [Binding] 20, [Enhancement] 3, [AzureDamageUp] <style="highlight">2</style> 부여\n- (우울 또는 오만 중 높은 공명 수 - 2)만큼 부여 대상 수 증가 (최대 <style="highlight">4</style>명)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070621].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [Binding], [ForwardToTheKing], [Enhancement], [AzureDamageUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [ForwardToTheKing] = 왕의 앞으로 / Before the King; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AzureDamageUp] = 우울 피해량 증가 / Gloom DMG Up
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Next turn, gain 20 [Binding], 1 [ForwardToTheKing], and 3 [Enhancement]\n[EndSkill] Next turn, apply 20 [Binding], 3 [Enhancement], and <style="highlight">2</style> [AzureDamageUp] to 2 other allies in the order of Deployment\n- The number of affected allies grows by (highest Gloom or Pride Reson. - 2) (max <style="highlight">4</style>)
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] następnej tury zyskuje 20 [Binding], 1 [ForwardToTheKing] i 3 [Enhancement]\n[EndSkill] następnej tury nakłada 20 [Binding], 3 [Enhancement] i <style="highlight">2</style> [AzureDamageUp] na 2 innych sojuszników według kolejności depozyzu\n- liczba objętych sojuszników rośnie o (wyższego z Rezonansów Posępności lub Pychy - 2) (maks. <style="highlight">4</style> sojuszników)
241. [Pasywka E.G.O — nazwa] 구속의 사슬
   źródło: Passive_Ego.json :: dataList[id=2070611].name
   limit: do 40 znaków
   EN: Chains of Binding
   PL: Łańcuchy Uwiązania
242. [Pasywka E.G.O — opis] - 전투 시작 시 자신의 스킬을 포함한 공명 중 가장 높은 공명이 4 이상이 되었다면, 자신과 공명에 포함된 모든 아군에게 [AttackUp] 3, [DefenseUp] 3 부여\n- 해당 공명이 완전 공명이면, 추가 2 부여
   źródło: Passive_Ego.json :: dataList[id=2070611].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: - Combat Start: At 4+ highest Reson. that includes this unit's Skills, apply 3 [AttackUp] and 3 [DefenseUp] to self and all allies who were a part of that Reson.\n- If the said Reson. was an A-Reson., apply 2 additional [AttackUp] and [DefenseUp]
   PL: - Początek walki: przy 4+ najwyższego Rezonansu, w którym uczestniczyły Umiejętności tej jednostki, nakłada 3 [AttackUp] i 3 [DefenseUp] na tę jednostkę i wszystkich sojuszników uczestniczących w tym Rezonansie\n- jeżeli ten Rezonans był Rezonansem Absolutnym, nakłada dodatkowo po 2 [AttackUp] i [DefenseUp]

## E.G.O [20707] Fell Bullet (흉탄) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20707`

243. [Karta E.G.O — nazwa] 흉탄
   źródło: Egos.json :: dataList[id=20707].name
   limit: do 40 znaków
   EN: Fell Bullet
   PL: Mroczny Pocisk
244. [Karta E.G.O — opis] 히스클리프의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20707].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 흉탄
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].name ; dataList[id=2070711].levelList[level=3].name ; dataList[id=2070711].levelList[level=4].name
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 흉탄의 사수
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].abName ; dataList[id=2070711].levelList[level=3].abName ; dataList[id=2070711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Der Fluchschütze
   PL: Der Fluchschütze
247. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] (최대 공명 수 + 1)만큼 [BoseProjektil]을 얻음 (최대 7)\n- 해당 공명이 완전 공명이면 [BoseProjektil]을 (최대 공명 수 + 2)만큼 얻음\n[BeforeAttack] [BoseProjektil]당 [Breath] 1 얻음 (최대 3)\n[EndSkill] [BoseProjektil] 전부 소모
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [BoseProjektil], [Breath], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson. + 1) [BoseProjektil] (max 7)\n- If it was an A-Reson., gain (highest Reson. +2) [BoseProjektil] instead\n[BeforeAttack] Gain 1 [Breath] for every [BoseProjektil] (max 3)\n[EndSkill] Lose every [BoseProjektil]
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans + 1) [BoseProjektil] (maks. 7)\n- jeżeli to był Rezonans Absolutny, zamiast tego zyskuje (najwyższy Rezonans + 2) [BoseProjektil]\n[BeforeAttack] zyskuje 1 [Breath] za każde [BoseProjektil] (maks. 3)\n[EndSkill] zużywa wszystkie [BoseProjektil]
248. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [BoseProjektil]당 크리티컬 피해량 +5% (최대 35%)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +5% Damage on Critical Hit for every [BoseProjektil] (max 35%)
   PL: zadaje +5% obrażeń krytycznych za każde [BoseProjektil] (maks. 35%)
249. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]
250. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=2070711].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=2070711].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict 3 [Sinking]
   PL: [CriticalOnSucceedAttack] nakłada 3 [Sinking]
251. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 2, efekt 4 — opis] [CriticalTargetKill] 자신에게 [Bullet] 효과가 있으면, [Bullet] 1 얻음 (전투 당 2회)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=1].coinlist[#1].coindescs[#3].desc ; dataList[id=2070711].levelList[level=3].coinlist[#1].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalTargetKill], [Bullet]
   znaczenie tagów: [CriticalTargetKill] = [크리티컬 처치 시] / [On Crit Kill]; [Bullet] = 탄환 / Ammo
   EN: [CriticalTargetKill] If this unit has the [Bullet] effect, gain 1 [Bullet] (2 times per Encounter)
   PL: [CriticalTargetKill] jeżeli ta jednostka ma efekt [Bullet], zyskuje 1 [Bullet] (2 razy na walkę)
252. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (최대 공명 수 + 1)만큼 [BoseProjektil]을 얻음 (최대 7)\n- 해당 공명이 완전 공명이면 [BoseProjektil]을 (최대 공명 수 + 2)만큼 얻음\n[BeforeAttack] [BoseProjektil]당 [Breath] 1 얻음 (최대 <style="highlight">4</style>)\n[EndSkill] [BoseProjektil] 전부 소모
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=3].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [BoseProjektil], [Breath], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson. + 1) [BoseProjektil] (max 7)\n- If it was an A-Reson., gain (highest Reson. + 2) [BoseProjektil] instead\n[BeforeAttack] Gain 1 [Breath] for every [BoseProjektil] (max <style="highlight">4</style>)\n[EndSkill] Lose every [BoseProjektil]
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans + 1) [BoseProjektil] (maks. 7)\n- jeżeli to był Rezonans Absolutny, zamiast tego zyskuje (najwyższy Rezonans + 2) [BoseProjektil]\n[BeforeAttack] zyskuje 1 [Breath] za każde [BoseProjektil] (maks. <style="highlight">4</style>)\n[EndSkill] zużywa wszystkie [BoseProjektil]
253. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [BoseProjektil]당 크리티컬 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +<style="highlight">10</style>% Damage on Critical Hit for every [BoseProjektil] (max <style="highlight">70</style>%)
   PL: zadaje +<style="highlight">10</style>% obrażeń krytycznych za każde [BoseProjektil] (maks. <style="highlight">70</style>%)
254. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] Nakłada 4 [Laceration]
255. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (최대 공명 수 + 1)만큼 [BoseProjektil]을 얻음 (최대 7)\n- 해당 공명이 완전 공명이면 [BoseProjektil]을 (최대 공명 수 + 2)만큼 얻음\n[BeforeAttack] [BoseProjektil]당 [Breath] 1 얻음 (최대 <style="highlight">7</style>)\n[BeforeAttack] 자신의 [Breath] 횟수 1 증가\n[EndSkill] [BoseProjektil] 전부 소모
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [BoseProjektil], [Breath], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson. + 1) [BoseProjektil] (max 7)\n- If it was an A-Reson., gain (highest Reson. + 2) [BoseProjektil] instead\n[BeforeAttack] Gain 1 [Breath] for every [BoseProjektil] (max <style="highlight">7</style>)\n[BeforeAttack] Gain +1 [Breath] Count\n[EndSkill] Lose every [BoseProjektil]
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans + 1) [BoseProjektil] (maks. 7)\n- jeżeli to był Rezonans Absolutny, zamiast tego zyskuje (najwyższy Rezonans + 2) [BoseProjektil]\n[BeforeAttack] zyskuje 1 [Breath] za każde [BoseProjektil] (maks. <style="highlight">7</style>)\n[BeforeAttack] zyskuje +1 Licznika [Breath]\n[EndSkill] zużywa wszystkie [BoseProjektil]
256. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [BoseProjektil]당 크리티컬 피해량 +<style="highlight">15</style>% (최대 <style="highlight">105</style>%)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +<style="highlight">15</style>% Damage on Critical Hit for every [BoseProjektil] (max <style="highlight">105</style>%)
   PL: zadaje +<style="highlight">15</style>% obrażeń krytycznych za każde [BoseProjektil] (maks. <style="highlight">105</style>%)
257. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] Nakłada 5 [Laceration]
258. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 4 — opis] [CriticalTargetKill] 자신에게 [Bullet] 효과가 있으면, [Bullet] 1 얻음 (전투 당 3회)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070711].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalTargetKill], [Bullet]
   znaczenie tagów: [CriticalTargetKill] = [크리티컬 처치 시] / [On Crit Kill]; [Bullet] = 탄환 / Ammo
   EN: [CriticalTargetKill] If this unit has the [Bullet] effect, gain 1 [Bullet] (3 times per Encounter)
   PL: [CriticalTargetKill] jeżeli ta jednostka ma efekt [Bullet], zyskuje 1 [Bullet] (3 razy na walkę)
259. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 흉탄
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=1].name ; dataList[id=2070721].levelList[level=3].name ; dataList[id=2070721].levelList[level=4].name
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 흉탄의 사수
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=1].abName ; dataList[id=2070721].levelList[level=3].abName ; dataList[id=2070721].levelList[level=4].abName
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 공명 수 + 1)만큼 [BoseProjektil]을 얻음 (최대 7)\n- 해당 공명이 완전 공명이면 [BoseProjektil]을 (최대 공명 수 + 2) 만큼 얻음\n[BeforeAttack] [BoseProjektil]당 피해량 +2% (최대 14%)\n[BeforeAttack] [BoseProjektil]당 호흡 1 얻음 (최대 3)\n[BeforeAttack] 자신의 [Breath] 5당 피해량 +3% (최대 15%)\n[BeforeAttack] 자신의 [Breath] 5 소모\n[EndSkill] [BoseProjektil] 전부 소모
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [BoseProjektil], [Breath], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (highest Reson. + 1) [BoseProjektil] (max 7)\n- If it was an A-Reson., gain (highest Reson. + 2) [BoseProjektil] instead\n[BeforeAttack] Deal +2% damage for every [BoseProjektil] (max 14%)\n[BeforeAttack] Gain 1 [Breath] for every [BoseProjektil] (max 3)\n[BeforeAttack] Deal +3% damage for every 5 [Breath] on self (max 15%)\n[BeforeAttack] Consume 5 [Breath] on self\n[EndSkill] Lose every [BoseProjektil]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans + 1) [BoseProjektil] (maks. 7)\n- jeżeli to był Rezonans Absolutny, zamiast tego zyskuje (najwyższy Rezonans + 2) [BoseProjektil]\n[BeforeAttack] zadaje +2% obrażeń za każde [BoseProjektil] (maks. 14%)\n[BeforeAttack] zyskuje 1 [Breath] za każde [BoseProjektil] (maks. 3)\n[BeforeAttack] zadaje +3% obrażeń za każde 5 [Breath] na tej jednostce (maks. 15%)\n[BeforeAttack] zużywa 5 [Breath] tej jednostki\n[EndSkill] zużywa wszystkie [BoseProjektil]
262. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2, [Sinking] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and 2 [Sinking]
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i 2 [Sinking]
263. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 공명 수 + 1)만큼 [BoseProjektil]을 얻음 (최대 7)\n- 해당 공명이 완전 공명이면 [BoseProjektil]을 (최대 공명 수 + 2) 만큼 얻음\n<style="highlight">[BeforeAttack] [BoseProjektil]이 3 이상이면, 공격 가중치 1 증가</style>\n[BeforeAttack] [BoseProjektil]당 피해량 +2% (최대 14%)\n[BeforeAttack] [BoseProjektil]당 호흡 1 얻음 (최대 <style="highlight">4</style>)\n[BeforeAttack] 자신의 [Breath] 5당 피해량 +<style="highlight">4</style>% (최대 <style="highlight">20</style>%)\n[BeforeAttack] 자신의 [Breath] 5 소모\n[EndSkill] [BoseProjektil] 전부 소모
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=3].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [BoseProjektil], [Breath], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (highest Reson. + 1) [BoseProjektil] (max 7)\n- If it was an A-Reson., gain (highest Reson. + 2) [BoseProjektil] instead\n<style="highlight">[BeforeAttack] At 3+ [BoseProjektil], gain 1 Atk Weight</style>\n[BeforeAttack] Deal +2% damage for every [BoseProjektil] (max 14%)\n[BeforeAttack] Gain 1 [Breath] for every [BoseProjektil] (max <style="highlight">4</style>)\n[BeforeAttack] Deal +<style="highlight">4</style>% damage for every 5 [Breath] on self (max <style="highlight">20</style>%)\n[BeforeAttack] Consume 5 [Breath] on self\n[EndSkill] Lose every [BoseProjektil]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans + 1) [BoseProjektil] (maks. 7)\n- jeżeli to był Rezonans Absolutny, zamiast tego zyskuje (najwyższy Rezonans + 2) [BoseProjektil]\n<style="highlight">[BeforeAttack] przy 3+ [BoseProjektil] Waga Ataku +1</style>\n[BeforeAttack] zadaje +2% obrażeń za każde [BoseProjektil] (maks. 14%)\n[BeforeAttack] zyskuje 1 [Breath] za każde [BoseProjektil] (maks. <style="highlight">4</style>)\n[BeforeAttack] zadaje +<style="highlight">4</style>% obrażeń za każde 5 [Breath] na tej jednostce (maks. <style="highlight">20</style>%)\n[BeforeAttack] zużywa 5 [Breath] tej jednostki\n[EndSkill] zużywa wszystkie [BoseProjektil]
264. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3, [Sinking] 3 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 3 [Sinking]
265. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 공명 수 + 1)만큼 [BoseProjektil]을 얻음 (최대 7)\n- 해당 공명이 완전 공명이면 [BoseProjektil]을 (최대 공명 수 + 2) 만큼 얻음\n[BeforeAttack] [BoseProjektil] <style="highlight">3당</style> 공격 가중치 1 증가 <style="highlight">(최대 2)</style>\n[BeforeAttack] [BoseProjektil]당 피해량 +<style="highlight">3</style>% (최대 <style="highlight">21</style>%)\n[BeforeAttack] [BoseProjektil]당 호흡 1 얻음 (최대 <style="highlight">7</style>)\n[BeforeAttack] 자신의 [Breath] 5당 피해량 +<style="highlight">5</style>% (최대 <style="highlight">25</style>%)\n[BeforeAttack] 자신의 [Breath] 5 소모\n[EndSkill] [BoseProjektil] 전부 소모
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070721].levelList[level=4].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [BoseProjektil], [Breath], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (highest Reson. + 1) [BoseProjektil] (max 7)\n- If it was an A-Reson., gain (highest Reson. + 2) [BoseProjektil] instead\n[BeforeAttack] Gain 1 Atk Weight for <style="highlight">every 3 [BoseProjektil] (max 2)</style>\n[BeforeAttack] Deal +<style="highlight">3</style>% damage for every [BoseProjektil] (max <style="highlight">21</style>%)\n[BeforeAttack] Gain 1 [Breath] for every [BoseProjektil] (max <style="highlight">7</style>)\n[BeforeAttack] Deal +<style="highlight">5</style>% damage for every 5 [Breath] on self (max <style="highlight">25</style>%)\n[BeforeAttack] Consume 5 [Breath] on self\n[EndSkill] Lose every [BoseProjektil]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans + 1) [BoseProjektil] (maks. 7)\n- jeżeli to był Rezonans Absolutny, zamiast tego zyskuje (najwyższy Rezonans + 2) [BoseProjektil]\n[BeforeAttack] zyskuje 1 Wagi Ataku za każde <style="highlight">3</style> [BoseProjektil] <style="highlight">(maks. 2)</style>\n[BeforeAttack] zadaje +<style="highlight">3</style>% obrażeń za każde [BoseProjektil] (maks. <style="highlight">21</style>%)\n[BeforeAttack] zyskuje 1 [Breath] za każde [BoseProjektil] (maks. <style="highlight">7</style>)\n[BeforeAttack] zadaje +<style="highlight">5</style>% obrażeń za każde 5 [Breath] na tej jednostce (maks. <style="highlight">25</style>%)\n[BeforeAttack] zużywa 5 [Breath] tej jednostki\n[EndSkill] zużywa wszystkie [BoseProjektil]
266. [Pasywka E.G.O — nazwa] 뭉개진 펜던트
   źródło: Passive_Ego.json :: dataList[id=2070711].name
   limit: do 40 znaków
   EN: Crushed Pendant
   PL: Zmiażdżony Wisiorek
267. [Pasywka E.G.O — opis] 전투 시작 시 최대 공명이 3 이상이면, [Breath] 3 얻음.
   źródło: Passive_Ego.json :: dataList[id=2070711].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Combat Start: At 3+ highest Reson., gain 3 [Breath].
   PL: Początek walki: przy najwyższym Rezonansie 3+ zyskuje 3 [Breath].

## E.G.O [20708] Asymmetrical Inertia (쏠린 관성) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20708`

268. [Karta E.G.O — nazwa] 쏠린 관성
   źródło: Egos.json :: dataList[id=20708].name
   limit: do 40 znaków
   EN: Asymmetrical Inertia
   PL: Niesymetryczna Bezwładność
269. [Karta E.G.O — opis] 히스클리프의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20708].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 쏠린 관성
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].name ; dataList[id=2070811].levelList[level=3].name ; dataList[id=2070811].levelList[level=4].name
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 태엽장치시간오뚝이
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].abName ; dataList[id=2070811].levelList[level=3].abName ; dataList[id=2070811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Clockwork-Time-Roly-Poly
   PL: Nakręcany Ważek Czasu
272. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] (최대 공명 수)만큼 자신의 [Vibration] 횟수 증가 (최대 6, 턴 당 최대 20)\n- 해당 공명이 나태 공명이면 자신의 [Vibration]을 [VibrationSpring]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Vibration], [VibrationSpring], [Switch_Vibration]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [VibrationSpring] = 진동 - 태엽감기 / Tremor - Clockwinding; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [BeforeAttack] Gain (highest Reson.) [Vibration] Count (max 6, 20 per turn)\n- If the said Reson. was a Sloth Reson., trigger [Switch_Vibration] on [Vibration] on self into [VibrationSpring]
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans) Licznika [Vibration] (maks. 6, maks. 20 na turę)\n- jeżeli ten Rezonans był Rezonansem Nieczułości, uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationSpring]
273. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2070811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
274. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 2 [Vibration]
275. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] [Vibration] 횟수 2 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2070811].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vibration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackTail] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttackTail] nakłada +2 Licznika [Vibration]
276. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.\n- 진동 폭발 시 이번 턴에 [AmberTakeDamageUp] 1 부여\n- 최대 공명이 나태 완전 공명 4 이상이면, 다음 턴에도 [AmberTakeDamageUp] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [AmberTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When triggering Tremor Burst, inflict 1 [AmberTakeDamageUp] this turn\n- If the highest Reson. was a 4+ Sloth A-Reson., inflict 1 [AmberTakeDamageUp] next turn as well
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]. zmniejsza Licznik [Vibration] celu o 1.\n- przy wyzwoleniu Wstrząsu nakłada 1 [AmberTakeDamageUp] w tej turze\n- jeżeli najwyższy Rezonans był Rezonansem Absolutnym Nieczułości 4+, nakłada 1 [AmberTakeDamageUp] także następnej tury
277. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (<style="highlight">2 +</style> 최대 공명 수)만큼 자신의 [Vibration] 횟수 증가 (최대 <style="highlight">8</style>, 턴 당 최대 20)\n- 해당 공명이 나태 공명이면 자신의 [Vibration]을 [VibrationSpring]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Vibration], [VibrationSpring], [Switch_Vibration]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [VibrationSpring] = 진동 - 태엽감기 / Tremor - Clockwinding; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [BeforeAttack] Gain (<style="highlight">2 +</style> highest Reson.) [Vibration] Count (max <style="highlight">8</style>, 20 per turn)\n- If the said Reson. was a Sloth Reson., trigger [Switch_Vibration] on [Vibration] on self into [VibrationSpring]
   PL: [BeforeAttack] zyskuje (<style="highlight">2 +</style> najwyższy Rezonans) Licznika [Vibration] (maks. <style="highlight">8</style>, maks. 20 na turę)\n- jeżeli ten Rezonans był Rezonansem Nieczułości, uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationSpring]
278. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 4 [Vibration]
   PL: [OnSucceedAttackHead] nakłada 4 [Vibration]
279. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.\n- 진동 폭발 시 이번 턴에 [AmberTakeDamageUp] 1 부여\n- 최대 공명이 <style="highlight">나태 완전 공명</style>이면, 다음 턴에도 [AmberTakeDamageUp] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [AmberTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When triggering Tremor Burst, inflict 1 [AmberTakeDamageUp] this turn\n- If the highest Reson. was a <style="highlight">Sloth A-Reson.</style>, inflict 1 [AmberTakeDamageUp] next turn as well
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]. zmniejsza Licznik [Vibration] celu o 1.\n- przy wyzwoleniu Wstrząsu nakłada 1 [AmberTakeDamageUp] w tej turze\n- jeżeli najwyższy Rezonans był <style="highlight">Rezonansem Absolutnym Nieczułości</style>, nakłada 1 [AmberTakeDamageUp] także następnej tury
280. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (<style="highlight">4 +</style> 최대 공명 수)만큼 자신의 [Vibration] 횟수 증가 (최대 8, 턴 당 최대 20)\n- 해당 공명이 나태 공명이면 자신의 [Vibration]을 [VibrationSpring]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Vibration], [VibrationSpring], [Switch_Vibration]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [VibrationSpring] = 진동 - 태엽감기 / Tremor - Clockwinding; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [BeforeAttack] Gain (<style="highlight">4 +</style> highest Reson.) [Vibration] Count (max 8, 20 per turn)\n- If the said Reson. was a Sloth Reson., trigger [Switch_Vibration] on [Vibration] on self into [VibrationSpring]
   PL: [BeforeAttack] zyskuje (<style="highlight">4 +</style> najwyższy Rezonans) Licznika [Vibration] (maks. 8, maks. 20 na turę)\n- jeżeli ten Rezonans był Rezonansem Nieczułości, uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationSpring]
281. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 5 [Vibration]
   PL: [OnSucceedAttackHead] nakłada 5 [Vibration]
282. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] [Vibration] 횟수 3 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vibration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackTail] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttackTail] nakłada +3 Licznika [Vibration]
283. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.\n- 진동 폭발 시 이번 턴에 [AmberTakeDamageUp] 1 부여\n- 최대 공명이 <style="highlight">나태 공명 3 이상</style>이면, 다음 턴에도 [AmberTakeDamageUp] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070811].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [AmberTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When triggering Tremor Burst, inflict 1 [AmberTakeDamageUp] this turn\n- If the highest Reson. was a <style="highlight">3+ Sloth Reson.</style>, inflict 1 [AmberTakeDamageUp] next turn as well
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]. zmniejsza Licznik [Vibration] celu o 1.\n- przy wyzwoleniu Wstrząsu nakłada 1 [AmberTakeDamageUp] w tej turze\n- jeżeli najwyższy Rezonans był <style="highlight">Rezonansem Nieczułości 3+</style>, nakłada 1 [AmberTakeDamageUp] także następnej tury
284. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 쏠린 관성
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].name ; dataList[id=2070821].levelList[level=3].name ; dataList[id=2070821].levelList[level=4].name
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 태엽장치시간오뚝이
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].abName ; dataList[id=2070821].levelList[level=3].abName ; dataList[id=2070821].levelList[level=4].abName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (2 + 최대 공명 수)만큼 자신의 [Vibration] 횟수 증가 (최대 8, 턴 당 최대 20)\n- 해당 공명이 나태 공명이면 자신의 [Vibration]을 [VibrationSpring]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Vibration], [VibrationSpring], [Switch_Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [VibrationSpring] = 진동 - 태엽감기 / Tremor - Clockwinding; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (2 + highest Reson.) [Vibration] Count (max 8, 20 per turn)\n- If the said Reson. was a Sloth Reson., trigger [Switch_Vibration] on [Vibration] on self into [VibrationSpring]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (2 + najwyższy Rezonans) Licznika [Vibration] (maks. 8, maks. 20 na turę)\n- jeżeli ten Rezonans był Rezonansem Nieczułości, uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationSpring]
287. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070821].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 4 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] [Vibration] 횟수 2 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2070821].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2070821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1.
291. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.\n- 진동 폭발 시 이번 턴에 [AmberTakeDamageUp] 2 부여\n- 최대 공명이 나태 완전 공명 4 이상이면, 다음 턴에도 [AmberTakeDamageUp] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [AmberTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When triggering Tremor Burst, inflict 2 [AmberTakeDamageUp] this turn\n- If the highest Reson. was a 4+ Sloth A-Reson, inflict 2 [AmberTakeDamageUp] next turn as well
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]. zmniejsza Licznik [Vibration] celu o 1.\n- przy wyzwoleniu Wstrząsu nakłada 2 [AmberTakeDamageUp] w tej turze\n- jeżeli najwyższy Rezonans był Rezonansem Absolutnym Nieczułości 4+, nakłada 2 [AmberTakeDamageUp] także następnej tury
292. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (<style="highlight">4 +</style> 최대 공명 수)만큼 자신의 [Vibration] 횟수 증가 (최대 8, 턴 당 최대 20)\n- 해당 공명이 나태 공명이면 자신의 [Vibration]을 [VibrationSpring]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=3].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Vibration], [VibrationSpring], [Switch_Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [VibrationSpring] = 진동 - 태엽감기 / Tremor - Clockwinding; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (<style="highlight">4 +</style> highest Reson.) [Vibration] Count (max 8, 20 per turn)\n- If the said Reson. was a Sloth Reson., trigger [Switch_Vibration] on [Vibration] on self into [VibrationSpring]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (<style="highlight">4 +</style> najwyższy Rezonans) Licznika [Vibration] (maks. 8, maks. 20 na turę)\n- jeżeli ten Rezonans był Rezonansem Nieczułości, uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationSpring]
293. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 5 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] [Vibration] 횟수 3 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.\n- 진동 폭발 시 이번 턴에 [AmberTakeDamageUp] 2 부여\n- 최대 공명이 <style="highlight">나태 완전 공명</style>이면, 다음 턴에도 [AmberTakeDamageUp] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [AmberTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When triggering Tremor Burst, inflict 2 [AmberTakeDamageUp] this turn\n- If the highest Reson. was a <style="highlight">Sloth A-Reson</style>, inflict 2 [AmberTakeDamageUp] next turn as well
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]. zmniejsza Licznik [Vibration] celu o 1.\n- przy wyzwoleniu Wstrząsu nakłada 2 [AmberTakeDamageUp] w tej turze\n- jeżeli najwyższy Rezonans był <style="highlight">Rezonansem Absolutnym Nieczułości</style>, nakłada 2 [AmberTakeDamageUp] także następnej tury
296. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (4 + 최대 공명 수)만큼 자신의 [Vibration] 횟수 증가 (최대 <style="highlight">10</style>, 턴 당 최대 20)\n- 해당 공명이 나태 공명이면 자신의 [Vibration]을 [VibrationSpring]로 [Switch_Vibration]
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Vibration], [VibrationSpring], [Switch_Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [VibrationSpring] = 진동 - 태엽감기 / Tremor - Clockwinding; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (4 + highest Reson.) [Vibration] Count (max <style="highlight">10</style>, 20 per turn)\n- If the said Reson. was a Sloth Reson., trigger [Switch_Vibration] on [Vibration] on self into [VibrationSpring]
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (4 + najwyższy Rezonans) Licznika [Vibration] (maks. <style="highlight">10</style>, maks. 20 na turę)\n- jeżeli ten Rezonans był Rezonansem Nieczułości, uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationSpring]
297. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
298. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 6 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 6 [Vibration]
   PL: [OnSucceedAttackHead] nakłada 6 [Vibration]
299. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] [Vibration] 횟수 4 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Vibration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackTail] Inflict +4 [Vibration] Count
   PL: [OnSucceedAttackTail] nakłada +4 Licznika [Vibration]
300. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소.\n- 진동 폭발 시 이번 턴에 [AmberTakeDamageUp] 2 부여\n- 최대 공명이 <style="highlight">나태 공명 3 이상</style>이면, 다음 턴에도 [AmberTakeDamageUp] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [AmberTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [AmberTakeDamageUp] = 나태 취약 / Sloth Fragility
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When triggering Tremor Burst, inflict 2 [AmberTakeDamageUp] this turn\n- If the highest Reson. was a <style="highlight">3+ Sloth Reson.</style>, inflict 2 [AmberTakeDamageUp] next turn as well
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion]. zmniejsza Licznik [Vibration] celu o 1.\n- przy wyzwoleniu Wstrząsu nakłada 2 [AmberTakeDamageUp] w tej turze\n- jeżeli najwyższy Rezonans był <style="highlight">Rezonansem Nieczułości 3+</style>, nakłada 2 [AmberTakeDamageUp] także następnej tury
301. [Pasywka E.G.O — nazwa] 망가진 종
   źródło: Passive_Ego.json :: dataList[id=2070811].name
   limit: do 40 znaków
   EN: Broken Bell
   PL: Zbity Dzwon
302. [Pasywka E.G.O — opis] 스킬, 코인, 패시브 효과로 [VibrationExplosion]이 발생한 적에게 이번 턴에 [Vulnerable] 1 부여 (적 1명 당 턴 당 1회 발동).\n- 진동 폭발 시 [Vulnerable]을 부여하는 E.G.O 기프트와 중첩하여 발동되지 않음. (해당 기프트가 강화 상태인 경우, 이 효과의 값을 차감한 뒤 부여됨.)
   źródło: Passive_Ego.json :: dataList[id=2070811].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [Vulnerable]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vulnerable] = 취약 / Fragile
   EN: Inflict [Vulnerable] this turn on enemies who were hit by [VibrationExplosion] from Skill, Coin, or Passive effects.\n- Does not stack with E.G.O Gifts that inflict [Vulnerable] upon triggering [VibrationExplosion]. (If the said E.G.O Gifts have been enhanced, subtract this effect's value from the final value before inflicting it.)
   PL: [Vulnerable] nakłada się w tej turze na wrogów, na których [VibrationExplosion] został wyzwolony przez efekty Umiejętności, Monety lub Pasywu.\n(1 raz na turę na wroga)\n- nie kumuluje się z Prezentami E.G.O nakładającymi [Vulnerable] przy wyzwoleniu [VibrationExplosion]. (jeżeli ten Prezent jest w stanie wzmocnionym, jego wartość jest najpierw odejmowana od nakładanej wartości.)
303. [Pasywka E.G.O — podsumowanie] [VibrationExplosion]시 [Vulnerable] 1 부여
   źródło: Passive_Ego.json :: dataList[id=2070811].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [Vulnerable]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vulnerable] = 취약 / Fragile
   EN: Inflict 1 [Vulnerable] upon triggering [VibrationExplosion]
   PL: nakłada 1 [Vulnerable] przy wyzwoleniu [VibrationExplosion]

## E.G.O [20709] Move-in Reg. (입주 신고) — Heathcliff
- postać: Heathcliff (히스클리프) · ID E.G.O: `20709`

304. [Karta E.G.O — nazwa] 입주 신고
   źródło: Egos.json :: dataList[id=20709].name
   limit: do 40 znaków
   EN: Move-in Reg.
   PL: Zgłoszenie Zamieszkowania
305. [Karta E.G.O — opis] 히스클리프 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20709].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 입주 신고
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].name ; dataList[id=2070911].levelList[level=3].name ; dataList[id=2070911].levelList[level=4].name
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] Kqe-1j-23
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].abName ; dataList[id=2070911].levelList[level=3].abName ; dataList[id=2070911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Kqe-1j-23
   PL: Kqe-1j-23
308. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 7)\n- 질투 공명이 4 이상이면, 대신 자신의 [Charge] 횟수 7 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 모두 소모. 소모한 충전 횟수 1당, 피해량 +2% (최대 30%)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 7)\n- At 4+ Envy Reson., gain +7 [Charge] Count instead\n[BeforeAttack] Consume all [Charge] Count on self. Deal +2% damage for every [Charge] Count consumed (max 30%)
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans + 1) Licznika [Charge] (maks. 7)\n- przy Rezonansie Zawiści 4+ zamiast tego zyskuje +7 Licznika [Charge]\n[BeforeAttack] zużywa wszystkie Liczniki [Charge] tej jednostki. zadaje +2% obrażeń za każde 1 zużyty Licznik [Charge] (maks. 30%)
309. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070911].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
310. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2070911].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2070911].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2070911].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [IDMicroChip] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2070911].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2070911].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [IDMicroChip]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IDMicroChip] = 주민등록 마이크로칩 / Resident Reg. Microchip
   EN: [OnSucceedAttack] Inflict 2 [IDMicroChip]
   PL: [OnSucceedAttack] nakłada 2 [IDMicroChip]
313. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1~2 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=2070911].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1~2 [Charge] Count
   PL: [OnSucceedAttack] zyskuje +1~2 Licznika [Charge]
314. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 7)\n- 질투 공명이 4 이상이면, 대신 자신의 [Charge] 횟수 7 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 모두 소모. 소모한 충전 횟수 1당, 피해량 +3% (최대 45%)\n<style="highlight">- [Charge] 횟수를 5 이상 소모했다면, 기본 위력 +1</style>
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Charge]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 7)\n- At 4+ Envy Reson., gain +7 [Charge] Count instead\n[BeforeAttack] Consume all [Charge] Count on self. Deal +3% damage for every [Charge] Count consumed (max 45%)\n<style="highlight">- If this consumed 5+ [Charge] Count, Base Power +1</style>
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans + 1) Licznika [Charge] (maks. 7)\n- przy Rezonansie Zawiści 4+ zamiast tego zyskuje +7 Licznika [Charge]\n[BeforeAttack] zużywa wszystkie Liczniki [Charge] tej jednostki. zadaje +3% obrażeń za każde 1 zużyty Licznik [Charge] (maks. 45%)\n<style="highlight">- przy zużyciu 5+ Licznika [Charge] Moc Bazowa +1</style>
315. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] <style="highlight">메인 타겟의 [Combustion] 6당, 코인 위력 +1 (최대 3)</style>\n[BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 7)\n- 질투 공명이 4 이상이면, 대신 자신의 [Charge] 횟수 7 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 모두 소모. 소모한 충전 횟수 1당, 피해량 +3% (최대 45%)\n- [Charge] 횟수를 5 이상 소모했다면, 기본 위력 +1
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [BeforeAttack], [Charge]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: <style="highlight">Coin Power +1 for every 6 [Combustion] on the main target (max 3)</style>\n[BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 7)\n- At 4+ Envy Reson., gain +7 [Charge] Count instead\n[BeforeAttack] Consume all [Charge] Count on self. Deal +3% damage for every [Charge] Count consumed (max 45%)\n- If this consumed 5+ [Charge] Count, Base Power +1
   PL: <style="highlight">Moc Monety +1 za każde 6 [Combustion] głównego celu (maks. 3)</style>\n[BeforeAttack] zyskuje (najwyższy Rezonans + 1) Licznika [Charge] (maks. 7)\n- przy Rezonansie Zawiści 4+ zamiast tego zyskuje +7 Licznika [Charge]\n[BeforeAttack] zużywa wszystkie Liczniki [Charge] tej jednostki. zadaje +3% obrażeń za każde 1 zużyty Licznik [Charge] (maks. 45%)\n- przy zużyciu 5+ Licznika [Charge] Moc Bazowa +1
316. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
317. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">1~3</style> 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070911].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">1~3</style> [Charge] Count
   PL: [OnSucceedAttack] zyskuje <style="highlight">+1~3</style> Licznika [Charge]
319. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 입주 신고
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].name ; dataList[id=2070921].levelList[level=3].name ; dataList[id=2070921].levelList[level=4].name
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] Kqe-1j-23
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].abName ; dataList[id=2070921].levelList[level=3].abName ; dataList[id=2070921].levelList[level=4].abName
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n체력이 가장 높은 대상 우선 공격\n[BeforeAttack] 자신의 [Charge] 횟수가 10 미만이면, 최대 체력의 10%만큼 피해를 입고 자신의 [Charge] 횟수 10 증가\n(이 효과로 사망하거나 흐트러짐이 발생하지 않음)\n[BeforeAttack] (최대 공명 수 + 1)만큼 자신의 [Charge] 횟수 증가 (최대 8)\n- 질투 공명이 5 이상이면, 대신 자신의 [Charge] 횟수 8 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 모두 소모. 소모한 [Charge] 횟수 1당, 피해량 +3% (최대 50%)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nPrioritizes targets with the most HP\n[BeforeAttack] At less than 10 [Charge] Count, take 10% HP damage and gain +10 [Charge] Count\n(this effect does not kill or Stagger this unit)\n[BeforeAttack] Gain +(highest Reson. + 1) [Charge] Count (max 8)\n- At 5+ Envy Reson., gain +8 [Charge] Count instead\n[BeforeAttack] Consume all [Charge] Count on self. Deal +3% damage for every [Charge] Count consumed (max 50%)
   PL: [CantIdentify]\nPriorytet ataku: cele z najwyższym HP\n[BeforeAttack] przy Liczniku [Charge] niższym niż 10 otrzymuje obrażenia równe 10% Maks. HP i zyskuje +10 Licznika [Charge]\n(ten efekt nie powoduje śmierci ani Oszołomienia)\n[BeforeAttack] zyskuje (najwyższy Rezonans + 1) Licznika [Charge] (maks. 8)\n- przy Rezonansie Zawiści 5+ zamiast tego zyskuje +8 Licznika [Charge]\n[BeforeAttack] zużywa wszystkie Liczniki [Charge] tej jednostki. zadaje +3% obrażeń za każde 1 zużyty Licznik [Charge] (maks. 50%)
322. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2070921].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2070921].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] 대상에게 [IDMicroChip]이 있으면, 피해량 +20%
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2070921].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2070921].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [IDMicroChip]
   znaczenie tagów: [IDMicroChip] = 주민등록 마이크로칩 / Resident Reg. Microchip
   EN: If target has [IDMicroChip], deal +20% damage
   PL: jeżeli cel ma [IDMicroChip], zadaje +20% obrażeń
325. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=2070921].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2070921].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [IDMicroChip] 2 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=2070921].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2070921].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1~2 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#2].coindescs[#3].desc ; dataList[id=2070921].levelList[level=3].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 5 — opis] [EnemyKill] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=1].coinlist[#2].coindescs[#4].desc ; dataList[id=2070921].levelList[level=3].coinlist[#2].coindescs[#4].desc ; dataList[id=2070921].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Charge]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Charge] = 충전 / Charge
   EN: [EnemyKill] Gain +2 [Charge] Count
   PL: [EnemyKill] zyskuje +2 Licznika [Charge]
329. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n체력이 가장 높은 대상 우선 공격\n[BeforeAttack] 자신의 [Charge] 횟수가 10 미만이면, 최대 체력의 10%만큼 피해를 입고 자신의 [Charge] 횟수 10 증가\n(이 효과로 사망하거나 흐트러짐이 발생하지 않음)\n[BeforeAttack] (최대 공명 수 + <style="highlight">2</style>)만큼 자신의 [Charge] 횟수 증가 (최대 8)\n- 질투 공명이 5 이상이면, 대신 자신의 [Charge] 횟수 8 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 모두 소모. 소모한 [Charge] 횟수 1당, 피해량 +3% (최대 <style="highlight">55%</style>)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=3].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nPrioritizes targets with the most HP\n[BeforeAttack] At less than 10 [Charge] Count, take 10% HP damage and gain +10 [Charge] Count\n(this effect does not kill or Stagger this unit)\n[BeforeAttack] Gain +(highest Reson. + <style="highlight">2</style>) [Charge] Count (max 8)\n- At 5+ Envy Reson., gain +8 [Charge] Count instead\n[BeforeAttack] Consume all [Charge] Count on self. Deal +3% damage for every [Charge] Count consumed (max <style="highlight">55</style>%)
   PL: [CantIdentify]\nPriorytet ataku: cele z najwyższym HP\n[BeforeAttack] przy Liczniku [Charge] niższym niż 10 otrzymuje obrażenia równe 10% Maks. HP i zyskuje +10 Licznika [Charge]\n(ten efekt nie powoduje śmierci ani Oszołomienia)\n[BeforeAttack] zyskuje (najwyższy Rezonans + <style="highlight">2</style>) Licznika [Charge] (maks. 8)\n- przy Rezonansie Zawiści 5+ zamiast tego zyskuje +8 Licznika [Charge]\n[BeforeAttack] zużywa wszystkie Liczniki [Charge] tej jednostki. zadaje +3% obrażeń za każde 1 zużyty Licznik [Charge] (maks. <style="highlight">55%</style>)
330. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n체력이 가장 높은 대상 우선 공격\n<style="highlight">메인 타겟의 [Combustion] 6당, 코인 위력 +1 (최대 3)</style>\n[BeforeAttack] 자신의 [Charge] 횟수가 10 미만이면, 최대 체력의 10%만큼 피해를 입고 자신의 [Charge] 횟수 10 증가\n(이 효과로 사망하거나 흐트러짐이 발생하지 않음)\n[BeforeAttack] (최대 공명 수 + <style="highlight">3</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">10</style>)\n- 질투 공명이 5 이상이면, 대신 자신의 [Charge] 횟수 <style="highlight">10</style> 증가\n[BeforeAttack] 자신의 [Charge] 횟수를 모두 소모. 소모한 [Charge] 횟수 1당, 피해량 +3% (최대 <style="highlight">60%</style>)
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=4].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Combustion], [BeforeAttack], [Charge]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge
   EN: [CantIdentify]\nPrioritizes targets with the most HP\n<style="highlight">Coin Power +1 for every 6 [Combustion] on the main target (max 3)</style>\n[BeforeAttack] At less than 10 [Charge] Count, take 10% HP damage and gain +10 [Charge] Count\n(this effect does not kill or Stagger this unit)\n[BeforeAttack] Gain +(highest Reson. + <style="highlight">3</style>) [Charge] Count (max <style="highlight">10</style>)\n- At 5+ Envy Reson., gain +<style="highlight">10</style> [Charge] Count instead\n[BeforeAttack] Consume all [Charge] Count on self. Deal +3% damage for every [Charge] Count consumed (max <style="highlight">60</style>%)
   PL: [CantIdentify]\nPriorytet ataku: cele z najwyższym HP\n<style="highlight">Moc Monety +1 za każde 6 [Combustion] głównego celu (maks. 3)</style>\n[BeforeAttack] przy Liczniku [Charge] niższym niż 10 otrzymuje obrażenia równe 10% Maks. HP i zyskuje +10 Licznika [Charge]\n(ten efekt nie powoduje śmierci ani Oszołomienia)\n[BeforeAttack] zyskuje (najwyższy Rezonans + <style="highlight">3</style>) Licznika [Charge] (maks. <style="highlight">10</style>)\n- przy Rezonansie Zawiści 5+ zamiast tego zyskuje <style="highlight">+10</style> Licznika [Charge]\n[BeforeAttack] zużywa wszystkie Liczniki [Charge] tej jednostki. zadaje +3% obrażeń za każde 1 zużyty Licznik [Charge] (maks. <style="highlight">60</style>%)
331. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">1~3</style> 증가
   źródło: Skills_Ego_Personality-07.json :: dataList[id=2070921].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Pasywka E.G.O — nazwa] 회로 연결
   źródło: Passive_Ego.json :: dataList[id=2070911].name
   limit: do 40 znaków
   EN: Circuit Wiring
   PL: Instalacja Obwodu
335. [Pasywka E.G.O — opis] 자신이 [Combustion] 위력 또는 특수 화상을 부여하는 스킬 또는 질투 속성 스킬을 사용하여 적에게 적중 시, 대상에게 해당 스킬의 코인 수 절반만큼 추가로 [Combustion] 위력 부여\n(소수점 올림, 턴당 3회)
   źródło: Passive_Ego.json :: dataList[id=2070911].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [TabExplain]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On Hit with Skills that apply [Combustion] Potency or 'Unique Burn[TabExplain]', or On Hit with Envy Skills: Inflict additional [Combustion] Potency on target by half of the Skill's total Coins (rounded up; max 3 times per turn)
   PL: przy trafieniu wroga Umiejętnością nakładającą Siłę [Combustion] lub Szczególne Podpalenie[TabExplain] albo Umiejętnością Grzechu Zawiści, nakłada dodatkowo Siłę [Combustion] równą połowie liczby Monet tej Umiejętności na cel\n(zaokrąglone w górę, 3 razy na turę)

## E.G.O [20801] Snagharpoon (작살박이) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20801`

336. [Karta E.G.O — nazwa] 작살박이
   źródło: Egos.json :: dataList[id=20801].name
   limit: do 40 znaków
   EN: Snagharpoon
   PL: Zaczepiony Harpun
337. [Karta E.G.O — opis] 이스마엘 기본 EGO 장비
   źródło: Egos.json :: dataList[id=20801].desc
   limit: do 120 znaków
   EN: Ishmael’s Base E.G.O
   PL: Podstawowe E.G.O Ishmael
338. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 작살박이
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=1].name ; dataList[id=2080111].levelList[level=3].name ; dataList[id=2080111].levelList[level=4].name
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 이스마엘
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=1].abName ; dataList[id=2080111].levelList[level=3].abName ; dataList[id=2080111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael
340. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — opis] 가장 뒤에 있는 대상 공격 (일반 전투 한정)
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=1].desc ; dataList[id=2080111].levelList[level=3].desc ; dataList[id=2080111].levelList[level=4].desc
   limit: do 120 znaków
   EN: Targets the rearmost unit (In regular encounters)
   PL: Atakuje najdalszy cel (tylko w zwykłych walkach)
341. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 4 부여
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 4 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 4 [Binding] następnej tury
342. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 1 [Vibration]
343. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 6 부여
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2080111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 6 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 6 [Binding] następnej tury
344. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
345. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2080111].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Wybuch Wstrząsu
346. [Pasywka E.G.O — nazwa] 강박
   źródło: Passive_Ego.json :: dataList[id=2080111].name
   limit: do 40 znaków
   EN: Compulsion
   PL: Kompulsja
347. [Pasywka E.G.O — opis] 승률이 우세인 합 진행 시 합 위력 +2. 승률이 불리인 합 진행 시 합 위력 -2
   źródło: Passive_Ego.json :: dataList[id=2080111].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a Clash:\n- If win rate is Favored or above, Clash Power +2\n- If win rate is Struggling or below, Clash Power -2
   PL: jeżeli szansa wygranej Walki jest korzystna lub lepsza, Moc Walce +2. jeżeli szansa wygranej Walki jest niekorzystna lub gorsza, Moc Walce -2

## E.G.O [20802] Roseate Desire (분홍욕망) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20802`

348. [Karta E.G.O — nazwa] 분홍욕망
   źródło: Egos.json :: dataList[id=20802].name
   limit: do 40 znaków
   EN: Roseate Desire
   PL: Różowe Pożądanie
349. [Karta E.G.O — opis] 이스마엘 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20802].desc
   limit: do 120 znaków
   EN: Ishmael’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Ishmael
350. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 분홍욕망
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=1].name ; dataList[id=2080211].levelList[level=3].name ; dataList[id=2080211].levelList[level=4].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 분홍신
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=1].abName ; dataList[id=2080211].levelList[level=3].abName ; dataList[id=2080211].levelList[level=4].abName
   limit: do 40 znaków
   EN: Pink Shoes
   PL: Różowe Buty
352. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — opis] 가장 뒤에 있는 대상 공격 (일반 전투 한정)
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=1].desc ; dataList[id=2080211].levelList[level=3].desc ; dataList[id=2080211].levelList[level=4].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 4 부여
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Offense Level Down
   PL: [OnSucceedAttack] nakłada 4 zmniejszenia Poziomu Ataku
354. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 2 부여
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL: [OnSucceedAttack] nakłada 2 [Paralysis]
355. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 7 부여
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 7 Offense Level Down
   PL: [OnSucceedAttack] nakłada 7 zmniejszenia Poziomu Ataku
356. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080211].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 10 부여
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Offense Level Down
   PL: [OnSucceedAttack] nakłada 10 zmniejszenia Poziomu Ataku
358. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080211].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spętania
359. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 분홍욕망
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=1].name ; dataList[id=2080221].levelList[level=3].name ; dataList[id=2080221].levelList[level=4].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 분홍신
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=1].abName ; dataList[id=2080221].levelList[level=3].abName ; dataList[id=2080221].levelList[level=4].abName
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n속도가 가장 빠른 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=1].desc ; dataList[id=2080221].levelList[level=3].desc ; dataList[id=2080221].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets the unit with the fastest Speed
   PL: [CantIdentify]\nAtakuje cel z najwyższą Szybkością
362. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 4 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 353 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 2 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 다음 턴에 속박 4 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 4 [Binding] next turn
   PL: [OnSucceedAttackHead] nakłada 4 [Binding] następnej tury
365. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 7 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 4 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 10 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 5 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 5 [Paralysis]
   PL: [OnSucceedAttack] Nakłada 5 Paraliżu
370. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 속박 5 부여
   źródło: Skills_Ego.json :: dataList[id=2080221].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 5 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 5 [Binding] następnej tury
371. [Pasywka E.G.O — nazwa] 분홍 리본
   źródło: Passive_Ego.json :: dataList[id=2080211].name
   limit: do 40 znaków
   EN: Pink Ribbons
   PL: Różowa Wstążka
372. [Pasywka E.G.O — opis] 합 승리 시 분홍 리본 1 부여
   źródło: Passive_Ego.json :: dataList[id=2080211].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PinkRibbon_Ishmael]
   znaczenie tagów: [PinkRibbon_Ishmael] = 분홍 리본 / Pink Ribbons
   EN: On Clash Win, inflict 1 [PinkRibbon_Ishmael]
   PL: przy wygranej Walce nakłada 1 [PinkRibbon_Ishmael]

## E.G.O [20803] Ardor Blossom Star (홍염살) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20803`

373. [Karta E.G.O — nazwa] 홍염살
   źródło: Egos.json :: dataList[id=20803].name
   limit: do 40 znaków
   EN: Ardor Blossom Star
   PL: Gwiazda Żarzącego Kwiatu
374. [Karta E.G.O — opis] 이스마엘 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20803].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 홍염살
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=1].name ; dataList[id=2080311].levelList[level=3].name ; dataList[id=2080311].levelList[level=4].name
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 홍염나방
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=1].abName ; dataList[id=2080311].levelList[level=3].abName ; dataList[id=2080311].levelList[level=4].abName
   limit: do 40 znaków
   EN: Ardor Blossom Moth
   PL: Ćma Szkarłatnego Płomienia
377. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — opis] 가장 뒤에 있는 대상 공격 (일반 전투 한정)
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=1].desc ; dataList[id=2080311].levelList[level=3].desc ; dataList[id=2080311].levelList[level=4].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] (분노 공명 수/2)만큼 화상 부여
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Inflict [Combustion] by half of Wrath Reson.
   PL: nakłada Podpalenie równe (Rezonansu Gniewu / 2)
379. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 무작위 적 3명에게 화상 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 3 [Combustion] on 3 random enemies
   PL: [OnSucceedAttackHead] nakłada 3 Podpalenia na 3 losowych wrogów
380. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량의 40%만큼 흐트러짐 손상 입힘
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2080311].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Raise Stagger Threshold by 40% of damage dealt
   PL: [OnSucceedAttackHead] podnosi Próg Oszołomienia o wartość 40% zadanych obrażeń
381. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 분노 공명 수만큼 화상 부여
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080311].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] by Wrath Reson.
   PL: [OnSucceedAttack] nakłada Podpalenie równe Rezonansowi Gniewu
382. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 무작위 적 3명에게 화상 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EndSkillHead] 무작위 적 3명에게 화상 5 부여
   źródło: Skills_Ego.json :: dataList[id=2080311].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead], [Combustion]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]; [Combustion] = 화상 / Burn
   EN: [EndSkillHead] Inflict 5 [Combustion] on 3 random enemies
   PL: [EndSkillHead] nakłada 5 Podpalenia na 3 losowych wrogów
384. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 홍염살
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=1].name ; dataList[id=2080321].levelList[level=3].name ; dataList[id=2080321].levelList[level=4].name
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 홍염나방
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=1].abName ; dataList[id=2080321].levelList[level=3].abName ; dataList[id=2080321].levelList[level=4].abName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] 최대 체력의 10%만큼 체력 감소
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=1].desc ; dataList[id=2080321].levelList[level=3].desc ; dataList[id=2080321].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] Lose HP by 10% of Max HP
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] traci HP równe 10% Maks. HP
387. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 모든 캐릭터에게 분노 공명 수만큼 화상 부여
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] by Wrath Reson. on all units
   PL: [OnSucceedAttack] nakłada Podpalenie równe Rezonansowi Gniewu na wszystkich jednostek
388. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 모든 캐릭터에게 (분노 공명 수 *2)만큼 화상 부여
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] by (2x) Wrath Reson. on all units
   PL: [OnSucceedAttack] nakłada Podpalenie równe (Rezonansu Gniewu x 2) na wszystkich jednostek
389. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 60%만큼 흐트러짐 손상 입힘
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080321].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 60% of damage dealt
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o wartość 60% zadanych obrażeń
390. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [EndSkill] 모든 캐릭터에게 (분노 공명 수 *2)만큼 화상 부여
   źródło: Skills_Ego.json :: dataList[id=2080321].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Combustion]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn
   EN: [EndSkill] Inflict [Combustion] by (2 * Wrath Reson.) on all units
   PL: [EndSkill] nakłada Podpalenie równe (Rezonansu Gniewu x 2) na wszystkich jednostek
391. [Pasywka E.G.O — nazwa] 흩날리는 불꽃
   źródło: Passive_Ego.json :: dataList[id=2080311].name
   limit: do 40 znaków
   EN: Shower of Fire
   PL: Sypiący się Ogień
392. [Pasywka E.G.O — opis] [Combustion]이 부여된 적에게 공격 적중 시 무작위 적 3 명에게 화상 1 부여
   źródło: Passive_Ego.json :: dataList[id=2080311].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On hit, if the target has [Combustion], inflict 1 [Combustion] on 3 random enemies
   PL: przy trafieniu, jeżeli cel ma [Combustion], nakłada 1 Podpalenia na 3 losowych wrogów

## E.G.O [20804] Capote (카포테) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20804`

393. [Karta E.G.O — nazwa] 카포테
   źródło: Egos.json :: dataList[id=20804].name
   limit: do 40 znaków
   EN: Capote
   PL: Capote
394. [Karta E.G.O — opis] 이스마엘의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20804].desc
   limit: do 120 znaków
   EN: Ishmael’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Ishmael
395. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — nazwa] 카포테
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=1].name ; dataList[id=2080411].levelList[level=3].name
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — źródło (Anomalia)] 놋쇠 황소
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=1].abName ; dataList[id=2080411].levelList[level=3].abName
   limit: do 40 znaków
   EN: Brazen Bull
   PL: Spiżowy Byk
397. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — opis] [EndSkill] 다음 턴에 모든 아군에게 분노 피해량 증가 1 부여
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=1].desc ; dataList[id=2080411].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Apply 1 Wrath DMG Up to all allies next turn
   PL: [EndSkill] następnej tury nakłada 1 zwiększenia zadawanych obrażeń od Gniewu na wszystkich sojuszników
398. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] Nakłada 3 Podpalenia
399. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 7 피해
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 7 SP damage
   PL: [OnSucceedAttack] zadaje celowi 7 obrażeń SP
400. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL: [OnSucceedAttack] nakłada 4 Podpalenia
401. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 15 피해
   źródło: Skills_Ego.json :: dataList[id=2080411].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 SP damage
   PL: [OnSucceedAttack] zadaje celowi 15 obrażeń SP
402. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — nazwa] 카포테
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=1].name ; dataList[id=2080421].levelList[level=3].name
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — źródło (Anomalia)] 놋쇠 황소
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=1].abName ; dataList[id=2080421].levelList[level=3].abName
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 다음 턴에 모든 캐릭터에게 분노 취약, 분노 피해량 증가 1 부여
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=1].desc ; dataList[id=2080421].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Give 1 Wrath Fragility, and 1 Wrath DMG Up to all units next turn
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] następnej tury nakłada 1 Kruchości Gniewu i zwiększenia obrażeń od Gniewu wszystkim jednostkom
405. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 7 피해
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 2 감소
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce target's [Vibration] Count by 2
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 2
408. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 5 부여
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL: [OnSucceedAttack] nakłada 5 Podpalenia
409. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 15 피해
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. [VibrationExplosion] 시 진동 횟수 2 감소. [VibrationExplosion]로 대상이 흐트러진 경우, 무작위 캐릭터 3명에게 화상 2 부여
   źródło: Skills_Ego.json :: dataList[id=2080421].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 2; if the [VibrationExplosion] Staggered the target, inflict +2 [Combustion] Count on 3 random units
   PL: [OnSucceedAttack] wyzwala [VibrationExplosion], po czym zmniejsza Licznik [Vibration] o 2; jeżeli [VibrationExplosion] Oszołomił cel, nakłada +2 Licznika [Combustion] na 3 losowych jednostek
411. [Pasywka E.G.O — nazwa] 환호 속 숨통 끊기
   źródło: Passive_Ego.json :: dataList[id=2080411].name
   limit: do 40 znaków
   EN: Slaying Amid Cheers
   PL: Duszenie Wśród Owacji
412. [Pasywka E.G.O — opis] 공격하는 대상의 체력이 30% 미만일 때 분노 속성 스킬의 피해량 + 20%
   źródło: Passive_Ego.json :: dataList[id=2080411].desc
   limit: do 120 znaków
   EN: When attacking a target that has less than 30% HP, Wrath Skills deal +20% damage
   PL: przy atakowaniu celu z HP niższym niż 30% Umiejętności Grzechu Gniewu zadają +20% obrażeń

## E.G.O [20805] Blind Obsession (맹목) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20805`

413. [Karta E.G.O — nazwa] 맹목
   źródło: Egos.json :: dataList[id=20805].name
   limit: do 40 znaków
   EN: Blind Obsession
   PL: Zaślepiona Obsesja
414. [Karta E.G.O — opis] 이스마엘의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20805].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 맹목
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=1].name ; dataList[id=2080511].levelList[level=3].name ; dataList[id=2080511].levelList[level=4].name
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 꿈먹는 탁류
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=1].abName ; dataList[id=2080511].levelList[level=3].abName ; dataList[id=2080511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Dream-Devouring Siltcurrent
   PL: Mułowy Prąd Pożerający Sny
417. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 정신력이 가장 낮은 아군 4명의 정신력 15 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 15 SP for 4 allies with the least SP
   PL: [EndSkill] odzyskuje 15 SP dla 4 sojuszników z najniższym SP
418. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 3 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +3 Charge Count
   PL: [OnSucceedAttackHead] zyskuje +3 Licznika [Charge]
419. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 무작위 아군 1명에게 호흡 횟수 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2080511].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Give +1 Poise Count to 1 random ally
   PL: [OnSucceedAttack] nakłada 1 Licznika Równowagi na 1 losowego sojusznika
420. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 정신력이 가장 낮은 아군 4명의 정신력 20 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 20 SP for 4 allies with the least SP
   PL: [EndSkill] odzyskuje 20 SP dla 4 sojuszników z najniższym SP
421. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 4 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +4 Charge Count
   PL: [OnSucceedAttackHead] Zyskuje +4 Licznika Ładowania
422. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [EndSkillHead] 정신력이 가장 높은 아군 4명에게 [PenetrateResultUp] 1, [AttackDmgUp] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead], [PenetrateResultUp], [AttackDmgUp]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [EndSkillHead] Apply 1 [PenetrateResultUp] and 1 [AttackDmgUp] to 4 allies with the highest SP
   PL: [EndSkillHead] nakłada 1 [PenetrateResultUp] i 1 [AttackDmgUp] na 4 sojuszników z najwyższym SP
423. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [EndSkill] 정신력이 가장 낮은 아군 4명의 정신력 25 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 25 SP for 4 allies with the least SP
   PL: [EndSkill] odzyskuje 25 SP dla 4 sojuszników z najniższym SP
424. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 6 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +6 Charge Count
   PL: [OnSucceedAttack] zyskuje +6 Licznika [Charge]
425. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 무작위 아군 1명에게 호흡 횟수 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Give +2 Poise Count to 1 random ally
   PL: [OnSucceedAttack] nakłada 2 Licznika Równowagi na 1 losowego sojusznika
426. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EndSkill] 정신력이 가장 높은 아군 4명에게 [PenetrateResultUp] 2, [AttackDmgUp] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080511].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [PenetrateResultUp], [AttackDmgUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [EndSkill] Apply 2 [PenetrateResultUp] and 2 [AttackDmgUp] to 4 allies with the highest SP
   PL: [EndSkill] nakłada 2 [PenetrateResultUp] i 2 [AttackDmgUp] na 4 sojuszników z najwyższym SP
427. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 맹목
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=1].name ; dataList[id=2080521].levelList[level=3].name ; dataList[id=2080521].levelList[level=4].name
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 꿈먹는 탁류
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=1].abName ; dataList[id=2080521].levelList[level=3].abName ; dataList[id=2080521].levelList[level=4].abName
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=1].desc ; dataList[id=2080521].levelList[level=3].desc ; dataList[id=2080521].levelList[level=4].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 1, 호흡 횟수 1 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Poise and +1 Poise Count
   PL: [OnSucceedAttack] zyskuje 1 Równowagi i +1 Licznika Równowagi
431. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 오만 취약 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Pride Fragility this turn and next turn
   PL: [OnSucceedAttack] nakłada 2 Kruchości Pychy w tej i następnej turze
432. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 자신의 체력을 최대 체력의 3% 만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Heal 3% of Max HP on self
   PL: [OnSucceedAttackTail] odzyskuje HP równe 3% Maks. HP
433. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 호흡 1, 호흡 횟수 1 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 오만 취약 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 4 — opis] [EndSkillTail] 정신력이 가장 낮은 아군 4명에게 이번 턴과 다음 턴에 피해량 증가 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkillTail]
   znaczenie tagów: [EndSkillTail] = [뒷면 공격 종료 시] / [Tails Attack End]
   EN: [EndSkillTail] Apply 2 Damage Up this turn and next turn to 4 allies with the least SP
   PL: [EndSkillTail] nakłada 2 zwiększenia zadawanych obrażeń w tej i następnej turze na 4 sojuszników z najniższym SP
436. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 체력을 최대 체력의 3% 만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 3% of Max HP on self
   PL: [OnSucceedAttack] odzyskuje HP równe 3% Maks. HP
437. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 오만 취약 3 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Pride Fragility this turn and next turn
   PL: [OnSucceedAttack] nakłada 3 Kruchości Pychy w tej i następnej turze
438. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 4 — opis] [EndSkill] 정신력이 가장 낮은 아군 4명에게 이번 턴과 다음 턴에 피해량 증가 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080521].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Apply 2 Damage Up this turn and next turn to 4 allies with the least SP
   PL: [EndSkill] nakłada 2 zwiększenia zadawanych obrażeń w tej i następnej turze na 4 sojuszników z najniższym SP
439. [Pasywka E.G.O — nazwa] 무모한 항해
   źródło: Passive_Ego.json :: dataList[id=2080511].name
   limit: do 40 znaków
   EN: Temeritous Voyage
   PL: Nieustraszona Żegluga
440. [Pasywka E.G.O — opis] 턴 종료 시 자신을 제외한 체력이 가장 낮은 아군 1명에게 침잠 5를 부여하고, 다음 턴에 신속 1, 공격 레벨 증가 3 부여
   źródło: Passive_Ego.json :: dataList[id=2080511].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking], [Agility], [AttackUp]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Agility] = 신속 / Haste; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: At the end of the turn, inflict 5 [Sinking] to 1 other ally with the lowest HP; Apply 1 [Agility] and 3 [AttackUp] next turn
   PL: na koniec tury nakłada 5 Zatonięcia na 1 innego sojusznika z najniższym HP, a następnej tury nakłada 1 [Agility] i 3 [AttackUp]

## E.G.O [20806] Wingbeat (날갯짓) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20806`

441. [Karta E.G.O — nazwa] 날갯짓
   źródło: Egos.json :: dataList[id=20806].name
   limit: do 40 znaków
   EN: Wingbeat
   PL: Uderzenie Skrzydłami
442. [Karta E.G.O — opis] 이스마엘의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20806].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 날갯짓
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].name ; dataList[id=2080611].levelList[level=3].name ; dataList[id=2080611].levelList[level=4].name
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 요정의 축제
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].abName ; dataList[id=2080611].levelList[level=3].abName ; dataList[id=2080611].levelList[level=4].abName
   limit: do 40 znaków
   EN: Fairy Festival
   PL: Święto Wróżek
445. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 체력을 최대 체력의 15%만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 15% of Max HP on self
   PL: [OnSucceedAttack] odzyskuje HP równe 15% Maks. HP
446. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 정신력 1 ~ 2 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2080611].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2080611].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Lose 1~2 SP
   PL: [OnSucceedAttackHead] traci 1~2 SP
447. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 이 코인 재사용 (스킬당 최대 5회)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2080611].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=2080611].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse this Coin (5 times per Skill)
   PL: [OnSucceedAttackHead] używa tej Monety ponownie (maks. 5 razy na Umiejętność)
448. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 체력을 피해량의 4 ~ 8%만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal self by 4~8% of damage dealt
   PL: [OnSucceedAttack] odzyskuje HP równe 4~8% zadanych obrażeń
449. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [ShamrockTakeDamageUp] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].coinlist[#1].coindescs[#3].desc ; dataList[id=2080611].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=2080611].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ShamrockTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ShamrockTakeDamageUp] = 탐식 취약 / Gluttony Fragility
   EN: [OnSucceedAttack] Inflict 1 [ShamrockTakeDamageUp]
   PL: [OnSucceedAttack] nakłada 1 [ShamrockTakeDamageUp]
450. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 2, efekt 5 — opis] [OnSucceedAttack] [Laceration] 1 ~ 3 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=1].coinlist[#1].coindescs[#4].desc ; dataList[id=2080611].levelList[level=3].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1~3 [Laceration]
   PL: [OnSucceedAttack] nakłada 1~3 [Laceration]
451. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] 이 스킬의 효과로 자신의 체력을 초과하여 회복한 경우, 초과한 회복량만큼 체력 비율이 가장 낮은 아군 1명의 체력을 대신 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=3].desc ; dataList[id=2080611].levelList[level=4].desc
   limit: do 170 znaków
   EN: If this Skill's healing exceeds this unit's max HP, redirect the excess healing to 1 ally with the least HP percentage instead
   PL: jeżeli leczenie z efektu tej Umiejętności przekracza Maks. HP tej jednostki, nadwyżkę leczenia kieruje zamiast tego na 1 sojusznika z najniższym procentem HP
452. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 체력을 최대 체력의 <style="highlight">18</style>%만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal <style="highlight">18%</style> of Max HP on self
   PL: [OnSucceedAttack] odzyskuje HP równe <style="highlight">18%</style> Maks. HP
453. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 체력을 피해량의 <style="highlight">6 ~ 10</style>%만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal self by <style="highlight">6~10</style>% of damage dealt
   PL: [OnSucceedAttack] odzyskuje HP równe <style="highlight">6~10</style>% zadanych obrażeń
454. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 체력을 최대 체력의 <style="highlight">20</style>% 만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal <style="highlight">20</style>% of Max HP on self
   PL: [OnSucceedAttack] odzyskuje HP równe <style="highlight">20</style>% Maks. HP
455. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 체력을 피해량의 <style="highlight">8 ~ 12</style>%만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal self by <style="highlight">8~12</style>% of damage dealt
   PL: [OnSucceedAttack] odzyskuje HP równe <style="highlight">8~12</style>% zadanych obrażeń
456. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 5 — opis] [OnSucceedAttack] [Laceration] 1 ~ <style="highlight">4</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080611].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1~<style="highlight">4</style> [Laceration]
   PL: [OnSucceedAttack] nakłada 1~<style="highlight">4</style> [Laceration]
457. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 날갯짓
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=1].name ; dataList[id=2080621].levelList[level=3].name ; dataList[id=2080621].levelList[level=4].name
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 요정의 축제
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=1].abName ; dataList[id=2080621].levelList[level=3].abName ; dataList[id=2080621].levelList[level=4].abName
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n본체 체력이 가장 낮은 대상 공격\n[BeforeAttack] 자신을 제외한 무작위 아군 최대 5명에게 최대 체력의 5%만큼 체력 피해.\n- 아군에게 입힌 피해의 합만큼 자신의 체력 회복.\n- 아군에게 피해를 주었으면, 이번 턴에 [Enhancement] 2, 다음 턴에 [Agility] 2 얻음.\n(턴 당 1회 발동. 입힌 피해에는 보호막 피해 포함. 이 효과로 피해를 받은 아군이 사망할 수 있음.)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Enhancement], [Agility]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste
   EN: [CantIdentify]\nTargets the unit with the least Core HP\n[BeforeAttack] Deal 5% HP damage to at most 5 random other allies\n- Heal HP on self equal to the damage dealt to allies.\n- If this unit dealt damage to an ally, gain 2 [Enhancement] this turn, and gain 2 [Agility] next turn.\n(Once per turn. The 'dealt damage' includes damage dealt to Shield HP. This effect can kill allies.)
   PL: [CantIdentify]\nAtakuje cel z najniższym HP Rdzenia\n[BeforeAttack] zadaje obrażenia HP równe 5% Maks. HP maks. 5 losowym innym sojusznikom.\n- odzyskuje HP równe sumie obrażeń zadanych sojusznikom.\n- jeżeli zadała obrażenia sojusznikom, w tej turze zyskuje 2 [Enhancement], a następnej tury 2 [Agility].\n(uruchamia się 1 raz na turę. zadane obrażenia wliczają obrażenia Tarczy. ten efekt może pokonać sojuszników.)
460. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 자신의 체력을 피해량의 10% 만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Heal self by 10% of damage dealt
   PL: [OnSucceedAttackTail] odzyskuje HP równe 10% zadanych obrażeń
461. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] [Laceration] 1 ~ 4 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Laceration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackTail] Inflict 1~4 [Laceration]
   PL: [OnSucceedAttackTail] nakłada 1~4 [Laceration]
462. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n본체 체력이 가장 낮은 대상 공격\n<style="highlight">[BeforeAttack] (가장 높은 공명 수 -2) 만큼 공격 가중치 증가 (최대 1)</style>\n[BeforeAttack] 자신을 제외한 무작위 아군 최대 5명에게 최대 체력의 5%만큼 체력 피해.\n- 아군에게 입힌 피해의 합만큼 자신의 체력 회복.\n- 아군에게 피해를 주었으면, 이번 턴에 [Enhancement] 2, 다음 턴에 [Agility] 2 얻음.\n(턴 당 1회 발동. 입힌 피해에는 보호막 피해 포함. 이 효과로 피해를 받은 아군이 사망할 수 있음.)\n<style="highlight">[EndSkill] 이 스킬의 효과로 자신의 체력을 초과하여 회복한 경우, (초과한 회복량/자신의 최대 체력) x 10만큼 다음 턴에 [AttackUp]를 얻음. (턴 당 최대 증가량: 3)</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=3].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Enhancement], [Agility], [EndSkill], [AttackUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantIdentify]\nTargets the unit with the least Core HP\n<style="highlight">[BeforeAttack] Gain (# of highest Reson. -2) Atk Weight (max 1)</style>\n[BeforeAttack] Deal 5% HP damage to at most 5 random other allies\n- Heal HP on self equal to the damage dealt to allies.\n- If this unit dealt damage to an ally, gain 2 [Enhancement] this turn, and gain 2 [Agility] next turn.\n(Once per turn. The 'dealt damage' includes damage dealt to Shield HP. This effect can kill allies.)\n<style="highlight">[EndSkill] If this Skill's healing exceeds this unit's max HP, gain (excess heal/max HP) x 10 [AttackUp] next turn. (max 3 per turn)</style>
   PL: [CantIdentify]\nAtakuje cel z najniższym HP Rdzenia\n<style="highlight">[BeforeAttack] zyskuje (najwyższy Rezonans -2) Wagi Ataku (maks. 1)</style>\n[BeforeAttack] zadaje obrażenia HP równe 5% Maks. HP maks. 5 losowym innym sojusznikom.\n- odzyskuje HP równe sumie obrażeń zadanych sojusznikom.\n- jeżeli zadała obrażenia sojusznikom, w tej turze zyskuje 2 [Enhancement], a następnej tury 2 [Agility].\n(uruchamia się 1 raz na turę. zadane obrażenia wliczają obrażenia Tarczy. ten efekt może pokonać sojuszników.)\n<style="highlight">[EndSkill] jeżeli leczenie z efektu tej Umiejętności przekracza Maks. HP tej jednostki, następnej tury zyskuje ((nadwyżka leczenia / Maks. HP tej jednostki) x 10) [AttackUp]. (maks. 3 na turę)</style>
463. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 자신의 체력을 피해량의 <style="highlight">15</style>% 만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Heal self by <style="highlight">15</style>% of damage dealt
   PL: [OnSucceedAttackTail] odzyskuje HP równe <style="highlight">15</style>% zadanych obrażeń
464. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] [Laceration] <style="highlight">2 ~ 5</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Laceration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackTail] Inflict <style="highlight">2~5</style> [Laceration]
   PL: [OnSucceedAttackTail] nakłada <style="highlight">2~5</style> [Laceration]
465. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n본체 체력이 가장 낮은 대상 공격\n[BeforeAttack] (가장 높은 공명 수 -2) 만큼 공격 가중치 증가 (최대 <style="highlight">2</style>)\n[BeforeAttack] 자신을 제외한 무작위 아군 최대 5명에게 최대 체력의 5%만큼 체력 피해.\n- 아군에게 입힌 피해의 합만큼 자신의 체력 회복.\n- 아군에게 피해를 주었으면, 이번 턴에 [Enhancement] 2, 다음 턴에 [Agility] 2 얻음.\n(턴 당 1회 발동. 입힌 피해에는 보호막 피해 포함. 이 효과로 피해를 받은 아군이 사망할 수 있음.)\n[EndSkill] 이 스킬의 효과로 자신의 체력을 초과하여 회복한 경우, (초과한 회복량/자신의 최대 체력) x 10만큼 다음 턴에 [AttackUp]를 얻음. (턴 당 최대 증가량: <style="highlight">6</style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=4].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Enhancement], [Agility], [EndSkill], [AttackUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantIdentify]\nTargets the unit with the least Core HP\n[BeforeAttack] Gain (# of highest Reson. -2) Atk Weight (max <style="highlight">2</style>)\n[BeforeAttack] Deal 5% HP damage to at most 5 random other allies\n- Heal HP on self equal to the damage dealt to allies.\n- If this unit dealt damage to an ally, gain 2 [Enhancement] this turn, and gain 2 [Agility] next turn.\n(Once per turn. The 'dealt damage' includes damage dealt to Shield HP. This effect can kill allies.)\n[EndSkill] If this Skill's healing exceeds this unit's max HP, gain (excess heal/max HP) x 10 [AttackUp] next turn. (max <style="highlight">6</style> per turn)
   PL: [CantIdentify]\nAtakuje cel z najniższym HP Rdzenia\n[BeforeAttack] zyskuje (najwyższy Rezonans -2) Wagi Ataku (maks. <style="highlight">2</style>)\n[BeforeAttack] zadaje obrażenia HP równe 5% Maks. HP maks. 5 losowym innym sojusznikom.\n- odzyskuje HP równe sumie obrażeń zadanych sojusznikom.\n- jeżeli zadała obrażenia sojusznikom, w tej turze zyskuje 2 [Enhancement], a następnej tury 2 [Agility].\n(uruchamia się 1 raz na turę. zadane obrażenia wliczają obrażenia Tarczy. ten efekt może pokonać sojuszników.)\n[EndSkill] jeżeli leczenie z efektu tej Umiejętności przekracza Maks. HP tej jednostki, następnej tury zyskuje ((nadwyżka leczenia / Maks. HP tej jednostki) x 10) [AttackUp]. (maks. <style="highlight">6</style> na turę)
466. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 자신의 체력을 피해량의 <style="highlight">20</style>% 만큼 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Heal self by <style="highlight">20</style>% of damage dealt
   PL: [OnSucceedAttackTail] odzyskuje HP równe <style="highlight">20</style>% zadanych obrażeń
467. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] [Laceration] <style="highlight">3 ~ 6</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [Laceration]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackTail] Inflict <style="highlight">3~6</style> [Laceration]
   PL: [OnSucceedAttackTail] nakłada <style="highlight">3~6</style> [Laceration]
468. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EnemyKill] 다음 턴에 [Enhancement] 1 얻음 (최대 공격 위력 증가량 : 3)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080621].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] Gain 1[Enhancement] next turn (max 3)
   PL: [EnemyKill] następnej tury zyskuje 1 [Enhancement] (maks. 3)
469. [Pasywka E.G.O — nazwa] 식탐
   źródło: Passive_Ego.json :: dataList[id=2080611].name
   limit: do 40 znaków
   EN: Gluttony
   PL: Żarłoczność
470. [Pasywka E.G.O — opis] 스킬 사용 시 메인 타겟이 이번 턴에 체력 피해를 받아 체력이 감소한 상태면, 적중시 자신의 체력이 최대인 경우, 피해량이 5 ~ 10% 증가하고, 자신의 체력이 감소한 상태인 경우, 체력을 2 ~ 5 회복. (턴 당 7회 발동)
   źródło: Passive_Ego.json :: dataList[id=2080611].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If the main target took HP damage this turn and isn't at max HP at Skill Use:\nOn Hit,\n- When this unit is at max HP, deal +5~+10% damage.\n- When this unit isn't at max HP, heal 2~5 HP. \n(7 times per turn)
   PL: przy użyciu Umiejętności jeżeli główny cel otrzymał w tej turze obrażenia HP i ma HP poniżej maksimum:\nprzy trafieniu\n- przy pełnym HP tej jednostki zadaje +5~+10% obrażeń.\n- jeżeli HP tej jednostki nie jest pełne, odzyskuje 2~5 HP.\n(7 razy na turę)
471. [Pasywka E.G.O — podsumowanie] 대상의 체력이 감소했으면, 적중시 피해량 증가 또는 체력 회복
   źródło: Passive_Ego.json :: dataList[id=2080611].summary
   limit: do 120 znaków
   EN: If the target isn't at max HP, deal more damage On Hit or heal HP On Hit
   PL: jeżeli HP celu jest poniżej maksimum, przy trafieniu zadaje więcej obrażeń lub odzyskuje HP

## E.G.O [20807] Bygone Days (지난 날) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20807`

472. [Karta E.G.O — nazwa] 지난 날
   źródło: Egos.json :: dataList[id=20807].name
   limit: do 40 znaków
   EN: Bygone Days
   PL: Dni Przeszłe
473. [Karta E.G.O — opis] 이스마엘의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20807].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 지난 날
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=1].name ; dataList[id=2080711].levelList[level=3].name ; dataList[id=2080711].levelList[level=4].name
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 어느 날의 초상
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=1].abName ; dataList[id=2080711].levelList[level=3].abName ; dataList[id=2080711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Portrait of a Certain Day
   PL: Portret Pewnego Dnia
476. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] 최대 공명이 4 이상이면, 공격 가중치 +1\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 2명이 최대 체력의 (5 + (메인 공격 대상의 [Sinking]과 [Sinking] 횟수의 합) / 3)%만큼 체력 회복 (최대 15% 회복)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [EndSkill], [Sinking]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Sinking] = 침잠 / Sinking
   EN: [BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n[EndSkill] Heal 2 allies with the lowest HP percentages by (5 + ([Sinking] on the main target + [Sinking] Count on the main target)/3)% HP (max 15%)
   PL: [BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n[EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o (5 + (Siła [Sinking] głównego celu ataku + Licznik [Sinking] głównego celu ataku) / 3)% Maks. HP (maks. 15% leczenia)
477. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
478. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Curse] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 1 [Curse]
   PL: [OnSucceedAttack] nakłada 1 [Curse]
479. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [UninvitedGuestPersonality] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [UninvitedGuestPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [UninvitedGuestPersonality] = 초청받지 않은 자 / The Uninvited
   EN: [OnSucceedAttack] Inflict 2 [UninvitedGuestPersonality]
   PL: [OnSucceedAttack] nakłada 2 [UninvitedGuestPersonality]
480. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 최대 공명이 4 이상이면, 공격 가중치 +1\n<style="highlight">- 해당 공명이 우울 공명이면, 공격 가중치 +1</style>\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 2명이 최대 체력의 (<style="highlight">10</style> + (메인 공격 대상의 [Sinking]과 [Sinking] 횟수의 합) / 3)%만큼 체력 회복 (최대 15% 회복)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill], [Sinking]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Sinking] = 침잠 / Sinking
   EN: [BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n<style="highlight">- If the said Reson. was a Gloom Reson., gain +1 Atk Weight</style>\n[EndSkill] Heal 2 allies with the lowest HP percentages by (<style="highlight">10</style> + ([Sinking] on the main target + [Sinking] Count on the main target)/3)% HP (max 15%)
   PL: [BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n<style="highlight">- jeżeli ten Rezonans był Rezonansem Posępności, Waga Ataku +1</style>\n[EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o (<style="highlight">10</style> + (Siła [Sinking] głównego celu ataku + Licznik [Sinking] głównego celu ataku) / 3)% Maks. HP (maks. 15% leczenia)
481. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 2<style="highlight"></style>
482. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Curse] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 1 [Curse]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 1 [Curse]<style="highlight"></style>
483. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 우울 공명 4 이상이면, [AzureTakeDamageUp] 1 부여</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: <style="highlight">[OnSucceedAttack] At 4+ Gloom Reson., inflict 1 [AzureTakeDamageUp]</style>
   PL: <style="highlight">[OnSucceedAttack] przy Rezonansie Posępności 4+ nakłada 1 [AzureTakeDamageUp]</style>
484. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [UninvitedGuestPersonality] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2080711].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [UninvitedGuestPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [UninvitedGuestPersonality] = 초청받지 않은 자 / The Uninvited
   EN: [OnSucceedAttack] Inflict 2 [UninvitedGuestPersonality]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 2 [UninvitedGuestPersonality]<style="highlight"></style>
485. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 최대 공명이 4 이상이면, 공격 가중치 +1\n- 해당 공명이 우울 공명이면, 공격 가중치 +1\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 2명이 최대 체력의 (10 + (메인 공격 대상의 [Sinking]과 [Sinking] 횟수의 합) / 3)%만큼 체력 회복 (최대 <style="highlight">20</style>% 회복)\n<style="highlight">- 최대 공명이 우울 공명 4 이상이면, 회복량이 최대 체력의 10%만큼 증가</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill], [Sinking]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [Sinking] = 침잠 / Sinking
   EN: [BeforeAttack] At 4+ highest Reson., gain +1 Atk Weight\n- If the said Reson. was a Gloom Reson., gain +1 Atk Weight\n[EndSkill] Heal 2 allies with the lowest HP percentages by (10 + ([Sinking] on the main target + [Sinking] Count on the main target)/3)% HP (max <style="highlight">20</style>%)\n<style="highlight">- If the highest Reson. was a 4+ Gloom Reson., heal 10% more of the max HP</style>
   PL: [BeforeAttack] przy najwyższym Rezonansie 4+ Waga Ataku +1\n- jeżeli ten Rezonans był Rezonansem Posępności, Waga Ataku +1\n[EndSkill] leczy 2 sojuszników z najniższym aktualnym procentem HP o (10 + (Siła [Sinking] głównego celu ataku + Licznik [Sinking] głównego celu ataku) / 3)% Maks. HP (maks. <style="highlight">20</style>% leczenia)\n<style="highlight">- jeżeli najwyższy Rezonans był Rezonansem Posępności 4+, leczenie rośnie o 10% Maks. HP</style>
486. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] o <style="highlight">3</style>
487. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Curse] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Curse]
   PL: [OnSucceedAttack] nakłada <style="highlight">2</style> [Curse]
488. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 우울 공명 4 이상이면, [AzureTakeDamageUp] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080711].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] At 4+ Gloom Reson., inflict 1 [AzureTakeDamageUp]<style="highlight"></style>
   PL: [OnSucceedAttack] przy Rezonansie Posępności 4+ nakłada 1 [AzureTakeDamageUp]<style="highlight"></style>
489. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 지난 날
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].name ; dataList[id=2080721].levelList[level=3].name ; dataList[id=2080721].levelList[level=4].name
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 어느 날의 초상
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].abName ; dataList[id=2080721].levelList[level=3].abName ; dataList[id=2080721].levelList[level=4].abName
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n[Sinking]이 가장 많은 대상 우선 공격\n[BeforeAttack] 최대 체력의 10%만큼 체력 감소 (이 효과로 흐트러짐 상태가 되지 않음)\n[EndSkill] 자신을 제외하고 현재 체력 비율이 가장 낮은 아군 3명이 최대 체력의 (5 + (메인 공격 대상의 [Sinking]과 [Sinking] 횟수의 합) / 3)%만큼 체력 회복 (최대 10% 회복)\n- 최대 공명 수가 4 이상이면 , 회복 대상 +1
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Sinking], [BeforeAttack], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nPrioritizes targets that have the most [Sinking]\n[BeforeAttack] Lose HP by 10% of Max HP (does not get Staggered due to this effect)\n[EndSkill] Heal 3 other allies with the lowest HP percentages by (5 + (([Sinking] on the main target + [Sinking] Count on the main target))/3)% HP (max 10%)\n- At 4+ highest Reson., heal 1 additional ally
   PL: [CantIdentify]\nPriorytet ataku: cel z najwyższą wartością [Sinking]\n[BeforeAttack] traci HP równe 10% Maks. HP (ten efekt nie powoduje Oszołomienia)\n[EndSkill] leczy 3 innych sojuszników z najniższym aktualnym procentem HP o (5 + (Siła [Sinking] głównego celu ataku + Licznik [Sinking] głównego celu ataku) / 3)% Maks. HP (maks. 10% leczenia)\n- przy najwyższym Rezonansie 4+ liczba leczonych sojuszników +1
492. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2080721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Curse] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 우울 공명 3 이상이면, [AzureTakeDamageUp] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=2080721].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] At 3+ Gloom Reson., inflict 1 [AzureTakeDamageUp]
   PL: [OnSucceedAttack] przy Rezonansie Posępności 3+ nakłada 1 [AzureTakeDamageUp]
495. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [UninvitedGuestPersonality] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=1].coinlist[#0].coindescs[#3].desc ; dataList[id=2080721].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=2080721].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 479 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n[Sinking]이 가장 많은 대상 우선 공격\n[BeforeAttack] 최대 체력의 10%만큼 체력 감소 (이 효과로 흐트러짐 상태가 되지 않음)\n[EndSkill] 자신을 제외하고 현재 체력 비율이 가장 낮은 아군 3명이 최대 체력의 (<style="highlight">10</style> + (메인 공격 대상의 [Sinking]과 [Sinking] 횟수의 합) / 3)%만큼 체력 회복 (최대 <style="highlight">15</style>% 회복)\n- 최대 공명 수가 4 이상이면 , 회복 대상 +1
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=3].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Sinking], [BeforeAttack], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nPrioritizes targets that have the most [Sinking]\n[BeforeAttack] Lose HP by 10% of Max HP (does not get Staggered due to this effect)\n[EndSkill] Heal 3 other allies with the lowest HP percentages by (<style="highlight">10</style> + ([Sinking] on the main target + [Sinking] Count on the main target)/3)% HP (max <style="highlight">15</style>%)\n- At 4+ highest Reson., heal 1 additional ally
   PL: [CantIdentify]\nPriorytet ataku: cel z najwyższą wartością [Sinking]\n[BeforeAttack] traci HP równe 10% Maks. HP (ten efekt nie powoduje Oszołomienia)\n[EndSkill] leczy 3 innych sojuszników z najniższym aktualnym procentem HP o (<style="highlight">10</style> + (Siła [Sinking] głównego celu ataku + Licznik [Sinking] głównego celu ataku) / 3)% Maks. HP (maks. <style="highlight">15</style>% leczenia)\n- przy najwyższym Rezonansie 4+ liczba leczonych sojuszników +1
497. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Curse] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080721].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 2 [Curse]
   PL: [OnSucceedAttack] nakłada 2 [Curse]
498. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 다음 턴에 [EchoOfMansion] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=2080721].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: [OnSucceedAttack] Inflict 2 [EchoOfMansion] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [EchoOfMansion]
499. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n[Sinking]이 가장 많은 대상 우선 공격\n[BeforeAttack] 최대 체력의 10%만큼 체력 감소 (이 효과로 흐트러짐 상태가 되지 않음)\n[EndSkill] 자신을 제외하고 현재 체력 비율이 가장 낮은 아군 3명이 최대 체력의 (10 + (메인 공격 대상의 [Sinking]과 [Sinking] 횟수의 합) / 3)%만큼 체력 회복 (최대 15% 회복)\n- 최대 공명 수가 4 이상이면 , 회복 대상 +1\n<style="highlight">- 해당 공명이 우울 공명이면, 회복량이 최대 체력의 5%만큼 증가</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [Sinking], [BeforeAttack], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nPrioritizes targets that have the most [Sinking]\n[BeforeAttack] Lose HP by 10% of Max HP (does not get Staggered due to this effect)\n[EndSkill] Heal 3 other allies with the lowest HP percentages by (10 + ([Sinking] on the main target + [Sinking] Count on the main target)/3)% HP (max 15%)\n- At 4+ highest Reson., heal 1 additional ally\n<style="highlight">- If the said Reson. was a Gloom Reson., heal an additional 5% HP</style>
   PL: [CantIdentify]\nPriorytet ataku: cel z najwyższą wartością [Sinking]\n[BeforeAttack] traci HP równe 10% Maks. HP (ten efekt nie powoduje Oszołomienia)\n[EndSkill] leczy 3 innych sojuszników z najniższym aktualnym procentem HP o (10 + (Siła [Sinking] głównego celu ataku + Licznik [Sinking] głównego celu ataku) / 3)% Maks. HP (maks. 15% leczenia)\n- przy najwyższym Rezonansie 4+ liczba leczonych sojuszników +1\n<style="highlight">- jeżeli ten Rezonans był Rezonansem Posępności, leczenie rośnie dodatkowo o 5% Maks. HP</style>
500. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 우울 공명 <style="highlight">3 당</style>, [AzureTakeDamageUp] 1 부여 <style="highlight">(최대 2)</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080721].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] <style="highlight">For every 3</style> Gloom Reson., inflict 1 [AzureTakeDamageUp] <style="highlight">(max 2)</style>
   PL: [OnSucceedAttack] <style="highlight">za każde 3</style> Rezonansu Posępności nakłada 1 [AzureTakeDamageUp] <style="highlight">(maks. 2)</style>
502. [Pasywka E.G.O — nazwa] 불청객 맞이
   źródło: Passive_Ego.json :: dataList[id=2080711].name
   limit: do 40 znaków
   EN: Interloper Reception
   PL: Powitanie Natręta
503. [Pasywka E.G.O — opis] 대상에게 [UninvitedGuestPersonality] 또는 패닉 유형 변경 효과가 있으면, 합 위력 +1.\n해당 대상에게 공격 적중시 정신력이 가장 낮은 아군 1명의 정신력 5 회복. (턴 당 1회)
   źródło: Passive_Ego.json :: dataList[id=2080711].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [UninvitedGuestPersonality]
   znaczenie tagów: [UninvitedGuestPersonality] = 초청받지 않은 자 / The Uninvited
   EN: If the target has [UninvitedGuestPersonality] or any of the Panic Type changing effects, Clash Power +1.\nOn Hit against the said target, heal 1 ally with the least SP for 5 SP. (once per turn)
   PL: jeżeli cel ma [UninvitedGuestPersonality] lub efekt zmiany typu Paniki, Moc Walce +1.\nprzy trafieniu w ten cel odzyskuje 5 SP dla 1 sojusznika z najniższym SP. (1 raz na turę)

## E.G.O [20808] Christmas Nightmare (크리스마스 악몽) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20808`

504. [Karta E.G.O — nazwa] 크리스마스 악몽
   źródło: Egos.json :: dataList[id=20808].name
   limit: do 40 znaków
   EN: Christmas Nightmare
   PL: Bożonarodzeniowy Koszmar
505. [Karta E.G.O — opis] 이스마엘의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20808].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 크리스마스 악몽
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=1].name ; dataList[id=2080811].levelList[level=3].name ; dataList[id=2080811].levelList[level=4].name
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 아늑한 침대
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=1].abName ; dataList[id=2080811].levelList[level=3].abName ; dataList[id=2080811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Cozy Bed
   PL: Przytulne Łóżko
508. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [BeforeAttack] (최대 공명 수 + 5) 만큼 자신의 [Vibration] 횟수 증가 (최대 10)\n[EndSkill] 공격 대상 중 흐트러짐, 사기저하, 패닉 상태인 대상이 있으면, 정신력 10 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Vibration], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson. + 5) [Vibration] Count (max 10)\n[EndSkill] If there are any targets in Staggered, Low Morale, or Panic states, heal 10 SP
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans + 5) Licznika [Vibration] (maks. 10)\n[EndSkill] jeżeli wśród celów ataku są jednostki Oszołomione, z Niskim Moral lub w Panice, odzyskuje 10 SP
509. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 5 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +5 [Vibration] Count
   PL: [OnSucceedAttack] nakłada +5 Licznika [Vibration]
510. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
511. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">대상의 정신력이 0 미만이면, 0 미만의 정신력 1 당 피해량 +1% (최대 45%)</style>\n[BeforeAttack] (최대 공명 수 + 5) 만큼 자신의 [Vibration] 횟수 증가 (최대 10)\n[EndSkill] 공격 대상 중 흐트러짐, 사기저하, 패닉 상태인 대상이 있으면, 정신력 10 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=3].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Vibration], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">If target has less than 0 SP, deal +1% damage for every SP value below 0 (max 45%)</style>\n[BeforeAttack] Gain (highest Reson. + 5) [Vibration] Count (max 10)\n[EndSkill] If there are any targets in Staggered, Low Morale, or Panic states, heal 10 SP
   PL: <style="highlight">jeżeli SP celu jest niższy niż 0, zadaje +1% obrażeń za każdy 1 punktu SP poniżej 0 (maks. 45%)</style>\n[BeforeAttack] zyskuje (najwyższy Rezonans + 5) Licznika [Vibration] (maks. 10)\n[EndSkill] jeżeli wśród celów ataku są jednostki Oszołomione, z Niskim Moral lub w Panice, odzyskuje 10 SP
512. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 5 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2080811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +5 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada +5 Licznika [Vibration]<style="highlight"></style>
513. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [Sinking] 5 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, inflict 5 [Sinking]
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, nakłada 5 [Sinking]
514. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [VibrationExplosion]. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, trigger [VibrationExplosion]; then, reduce the target's [Vibration] Count by 2
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, wyzwala [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 2
515. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2080811].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
516. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 정신력이 0 미만이면, 0 미만의 정신력 1 당 피해량 +1% (최대 45%)\n[BeforeAttack] (최대 공명 수 + 5) 만큼 자신의 [Vibration] 횟수 증가 (최대 10)\n[EndSkill] 공격 대상 중 흐트러짐, 사기저하, 패닉 상태인 대상이 있으면, 정신력 10 회복<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Vibration], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If target has less than 0 SP, deal +1% damage for every SP value below 0 (max 45%)\n[BeforeAttack] Gain (highest Reson. + 5) [Vibration] Count (max 10)\n[EndSkill] If there are any targets in Staggered, Low Morale, or Panic states, heal 10 SP<style="highlight"></style>
   PL: jeżeli SP celu jest niższy niż 0, zadaje +1% obrażeń za każdy 1 punktu SP poniżej 0 (maks. 45%)\n[BeforeAttack] zyskuje (najwyższy Rezonans + 5) Licznika [Vibration] (maks. 10)\n[EndSkill] jeżeli wśród celów ataku są jednostki Oszołomione, z Niskim Moral lub w Panice, odzyskuje 10 SP<style="highlight"></style>
517. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [Sinking] 5 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, inflict 5 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, nakłada 5 [Sinking]<style="highlight"></style>
518. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [VibrationExplosion] <style="highlight">2회.</style> 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080811].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, trigger [VibrationExplosion] <style="highlight">twice</style>; then, reduce the target's [Vibration] Count by 2
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, wyzwala [VibrationExplosion] <style="highlight">2 razy.</style> po czym zmniejsza Licznik [Vibration] celu o 2
519. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 크리스마스 악몽
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=1].name ; dataList[id=2080821].levelList[level=3].name ; dataList[id=2080821].levelList[level=4].name
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 아늑한 침대
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=1].abName ; dataList[id=2080821].levelList[level=3].abName ; dataList[id=2080821].levelList[level=4].abName
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 공명 수 + 5) 만큼 자신의 [Vibration] 횟수 증가 (최대 10)\n[BeforeAttack] 자신의 체력 10 회복
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack], [Vibration]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor
   EN: [CantIdentify]\nTargets randomly\n[BeforeAttack] Gain (highest Reson. + 5) [Vibration] Count (max 10)\n[BeforeAttack] Heal 10 HP
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans + 5) Licznika [Vibration] (maks. 10)\n[BeforeAttack] odzyskuje 10 HP
522. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 5 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2080821].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2080821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2080821].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">메인 공격 대상이 흐트러짐, 사기저하, 패닉 상태면, 기본 위력 +1</style>\n[BeforeAttack] (최대 공명 수 + 5) 만큼 자신의 [Vibration] 횟수 증가 (최대 10)\n[BeforeAttack] 자신의 체력 10 회복\n<style="highlight">[EndSkill] 흐트러짐, 사기저하, 패닉 상태인 적 1명 당 정신력 5 회복</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=3].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Vibration], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">If the main target is in Staggered, Low Morale, or Panic states, Base Power +1</style>\n[BeforeAttack] Gain (highest Reson. + 5) [Vibration] Count (max 10)\n[BeforeAttack] Heal 10 HP\n<style="highlight">[EndSkill] Heal 5 SP for every enemy that is in Staggered, Low Morale, or Panic states</style>
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">jeżeli główny cel ataku jest Oszołomiony, z Niskim Moral lub w Panice, Moc Bazowa +1</style>\n[BeforeAttack] zyskuje (najwyższy Rezonans + 5) Licznika [Vibration] (maks. 10)\n[BeforeAttack] odzyskuje 10 HP\n<style="highlight">[EndSkill] odzyskuje 5 SP za każdego 1 wroga Oszołomionego, z Niskim Moral lub w Panice</style>
526. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [Sinking] 5 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2080821].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, inflict 5 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, nakłada 5 [Sinking] i +2 Licznika [Sinking]
527. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, trigger [VibrationExplosion]; then, reduce the target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, wyzwala [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
528. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=2080821].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n메인 공격 대상이 흐트러짐, 사기저하, 패닉 상태면, 기본 위력 +<style="highlight">2</style>\n[BeforeAttack] (최대 공명 수 + 5) 만큼 자신의 [Vibration] 횟수 증가 (최대 10)\n[BeforeAttack] 자신의 체력 10 회복\n[EndSkill] 흐트러짐, 사기저하, 패닉 상태인 적 1명 당 정신력 5 회복<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [BeforeAttack], [Vibration], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\nIf the main target is in Staggered, Low Morale, or Panic states, Base Power +<style="highlight">2</style>\n[BeforeAttack] Gain (highest Reson. + 5) [Vibration] Count (max 10)\n[BeforeAttack] Heal 10 HP\n[EndSkill] Heal 5 SP for every enemy that is in Staggered, Low Morale, or Panic states<style="highlight"></style>
   PL: [CantIdentify]\nAtakuje losowy cel\njeżeli główny cel ataku jest Oszołomiony, z Niskim Moral lub w Panice, Moc Bazowa +<style="highlight">2</style>\n[BeforeAttack] zyskuje (najwyższy Rezonans + 5) Licznika [Vibration] (maks. 10)\n[BeforeAttack] odzyskuje 10 HP\n[EndSkill] odzyskuje 5 SP za każdego 1 wroga Oszołomionego, z Niskim Moral lub w Panice<style="highlight"></style>
530. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐, 사기저하, 패닉 상태가 아니면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080821].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target isn't in Staggered, Low Morale, or Panic states, trigger [VibrationExplosion]; then, reduce the target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli cel nie jest Oszołomiony, z Niskim Moral ani w Panice, wyzwala [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
533. [Pasywka E.G.O — nazwa] 어둠 속 시선
   źródło: Passive_Ego.json :: dataList[id=2080811].name
   limit: do 40 znaków
   EN: A Gaze in the Shadows
   PL: Spojrzenie w Cieniu
534. [Pasywka E.G.O — opis] 아군이 스킬, 코인 효과로 얻는 [Vibration] 횟수의 값 +1 (턴 당 2회 발동)\n- 아군의 공격 대상이 흐트러짐, 사기저하, 패닉 상태면 대신 +2\n- 동일한 효과를 갖는 E.G.O 기프트와 중첩하여 발동되지 않음.
   źródło: Passive_Ego.json :: dataList[id=2080811].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Allies gain +1 more [Vibration] Count from Skill or Coin effects (2 times per turn)\n- If the ally's target is in Staggered, Low Morale, or Panic states, gain +2 more instead\n- Effect does not stack with E.G.O Gifts of an identical effect.
   PL: sojusznicy zyskują +1 więcej Licznika [Vibration] z efektów Umiejętności lub Monety (2 razy na turę)\n- jeżeli cel ataku sojusznika jest Oszołomiony, z Niskim Moral lub w Panice, zamiast tego +2\n- nie kumuluje się z Prezentem E.G.O o identycznym efekcie.

## E.G.O [20809] Hundred-Footed Death Maggot [蝍蛆殺] (즉저살 [蝍蛆殺]) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20809`

535. [Karta E.G.O — nazwa] 즉저살 [蝍蛆殺]
   źródło: Egos.json :: dataList[id=20809].name
   limit: do 50 znaków
   EN: Hundred-Footed Death Maggot [蝍蛆殺]
   PL: Stuponoga Śmierć Larwy [蝍蛆殺]
536. [Karta E.G.O — opis] 이스마엘의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20809].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 즉저살 [蝍蛆殺]
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=1].name ; dataList[id=2080911].levelList[level=3].name ; dataList[id=2080911].levelList[level=4].name
   (powtórzenie elementu 535 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 지네사도
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=1].abName ; dataList[id=2080911].levelList[level=3].abName ; dataList[id=2080911].levelList[level=4].abName
   limit: do 40 znaków
   EN: Centipede Apostle
   PL: Apostoł Stonogi
539. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 자신과 메인 타겟의 부정적인 효과 수의 합만큼 [CentipedePoison] 부여 (최대 5)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [CentipedePoison]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [EndSkill] Inflict [CentipedePoison] equal to the sum of the types of negative effects on self and the main target (max 5)
   PL: [EndSkill] nakłada [CentipedePoison] równe sumie LICZBY RODZAJÓW negatywnych efektów tej jednostki i głównego celu (maks. 5)
540. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2080911].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2080911].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
542. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 탐식 또는 우울 공명이 4 이상이면, 해당 공명 수만큼 [CentipedePoison]을 부여 (최대 4)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2080911].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CentipedePoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [OnSucceedAttack] At 4+ Gluttony or Gloom Reson., inflict [CentipedePoison] by Reson. (max 4)
   PL: [OnSucceedAttack] przy Rezonansie Obżarstwa lub Posępności 4+ nakłada [CentipedePoison] równe wartości tego Rezonansu (maks. 4)
543. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 자신과 메인 타겟의 부정적인 효과 수의 합만큼 [CentipedePoison] 부여 (최대 <style="highlight">8</style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [CentipedePoison]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [EndSkill] Inflict [CentipedePoison] equal to the sum of the types of negative effects on self and the main target (max <style="highlight">8</style>)
   PL: [EndSkill] nakłada [CentipedePoison] równe sumie LICZBY RODZAJÓW negatywnych efektów tej jednostki i głównego celu (maks. <style="highlight">8</style>)
544. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [EndSkill] 자신과 메인 타겟의 부정적인 효과 수의 합만큼 [CentipedePoison] 부여 (최대 <style="highlight">10</style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [CentipedePoison]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [EndSkill] Inflict [CentipedePoison] equal to the sum of the types of negative effects on self and the main target (max <style="highlight">10</style>)
   PL: [EndSkill] nakłada [CentipedePoison] równe sumie LICZBY RODZAJÓW negatywnych efektów tej jednostki i głównego celu (maks. <style="highlight">10</style>)
545. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
547. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 탐식 또는 우울 공명이 4 이상이면, 해당 공명 수만큼 [CentipedePoison]을 부여 (최대 <style="highlight">5</style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080911].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [CentipedePoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [OnSucceedAttack] At 4+ Gluttony or Gloom Reson., inflict [CentipedePoison] by Reson. (max <style="highlight">5</style>)
   PL: [OnSucceedAttack] przy Rezonansie Obżarstwa lub Posępności 4+ nakłada [CentipedePoison] równe wartości tego Rezonansu (maks. <style="highlight">5</style>)
548. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 즉저살 [蝍蛆殺]
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=1].name ; dataList[id=2080921].levelList[level=3].name ; dataList[id=2080921].levelList[level=4].name
   (powtórzenie elementu 535 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 지네사도
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=1].abName ; dataList[id=2080921].levelList[level=3].abName ; dataList[id=2080921].levelList[level=4].abName
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신과 메인 타겟의 부정적인 효과 수의 합만큼 [CentipedePoison] 부여 (최대 8)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [CentipedePoison]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Inflict [CentipedePoison] equal to the sum of the types of negative effects on self and the main target (max 8)
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] nakłada [CentipedePoison] równe sumie LICZBY RODZAJÓW negatywnych efektów tej jednostki i głównego celu (maks. 8)
551. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2080921].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2080921].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
552. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2080921].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2080921].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 탐식 또는 우울 공명이 4 이상이면, 해당 공명 수만큼 [CentipedePoison]을 부여 (최대 4)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2080921].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신과 메인 타겟의 부정적인 효과 수의 합만큼 [CentipedePoison] 부여 (최대 <style="highlight">10</style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [CentipedePoison]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Inflict [CentipedePoison] equal to the sum of the types of negative effects on self and the main target (max <style="highlight">10</style>)
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] nakłada [CentipedePoison] równe sumie LICZBY RODZAJÓW negatywnych efektów tej jednostki i głównego celu (maks. <style="highlight">10</style>)
555. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신과 메인 타겟의 부정적인 효과 수의 합만큼 [CentipedePoison] 부여 (최대 10<style="highlight"></style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [CentipedePoison]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [CentipedePoison] = 지네 독 / Centipede Venom
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Inflict [CentipedePoison] equal to the sum of the types of negative effects on self and the main target (max 10<style="highlight"></style>)
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] nakłada [CentipedePoison] równe sumie LICZBY RODZAJÓW negatywnych efektów tej jednostki i głównego celu (maks. 10<style="highlight"></style>)
556. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 탐식 또는 우울 공명이 4 이상이면, 해당 공명 수만큼 [CentipedePoison]을 부여 (최대 <style="highlight">5</style>)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2080921].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Pasywka E.G.O — nazwa] 고독반살
   źródło: Passive_Ego.json :: dataList[id=2080911].name
   limit: do 40 znaków
   EN: Reversal Death by Gu Poison
   PL: Śmierć przez Gu-Oswojoną Odwrotnie
558. [Pasywka E.G.O — opis] 자신의 공격 스킬로 [Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여할 때마다, 다음 턴에 [AttackUp] 1 얻음 (최대 2)\n- 완전 공명 수가 3 이상이면, 위 효과를 대신하여, 다음 턴에 [AttackUp] 1 얻음 (최대 3)
   źródło: Passive_Ego.json :: dataList[id=2080911].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [AttackUp]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Whenever this unit inflicts [Sinking] Potency, [Sinking] Count, or 'Unique Sinking' using its Attack Skills, gain 1 [AttackUp] next turn (max 2)\n- At 3+ A-Reson., with the same conditionals, gain 1 [AttackUp] next turn instead (max 3)
   PL: za każdym razem, gdy ta jednostka nakłada Siłę [Sinking], Licznik [Sinking] lub Szczególne Zatonięcie swoimi Umiejętnościami Ataku, następnej tury zyskuje 1 [AttackUp] (maks. 2)\n- przy Rezonansie Absolutnym 3+ przy tym samym warunku zamiast tego zyskuje 1 [AttackUp] (maks. 3)

## E.G.O [20810] Tidal Elegy (파도의 만가) — Ishmael
- postać: Ishmael (이스마엘) · ID E.G.O: `20810`

559. [Karta E.G.O — nazwa] 파도의 만가
   źródło: Egos.json :: dataList[id=20810].name
   limit: do 40 znaków
   EN: Tidal Elegy
   PL: Tidal Elegy
560. [Karta E.G.O — opis] 이스마엘 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20810].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 파도의 만가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].name ; dataList[id=2081011].levelList[level=3].name ; dataList[id=2081011].levelList[level=4].name
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 스카디
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].abName ; dataList[id=2081011].levelList[level=3].abName ; dataList[id=2081011].levelList[level=4].abName
   limit: do 40 znaków
   EN: Skadi
   PL: Skadi
563. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 공격 대상이 1명이면, 코인 위력 +2, 피해량 +100% (집중 전투인 경우, 본체를 기준으로 판정)\n[WhenUse] 메인 타겟의 [Sinking] 4 이상이면, 합 위력 +1\n[BeforeAttack] 메인 타겟의 우울 내성이 1을 초과하면, 초과하는 값 0.1 당 피해량 +2% (최대 10%)\n[BeforeAttack] 우울 공명이 2 이상이면, 우울 공명 1당 피해량 +5% (최대 20%)\n[EndSkill] 공격 대상이 1명 이상 사망했으면, 무작위 적 2명에게 (각 대상의 [Sinking] 위력/2)만큼 우울 피해를 줌. (최대 15. 공격 대상이고, [Sinking] 위력을 많이 보유한 순으로 적용)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [BeforeAttack], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When attacking just a single target(in Focused Encounters, a Core and its connected Parts count as a single target), Coin Power +2 and deal +100% damage\n[WhenUse] If the main target has 4+ [Sinking], Clash Power +1\n[BeforeAttack] If the main target has higher than 1 Gloom Resist., deal +2% damage for every 0.1 excess Resist. (max 10%)\n[BeforeAttack] At 2+ Gloom Reson., deal +5% damage for every Gloom Reson. (max 20%)\n[EndSkill] If 1 or more targets are killed, deal ([Sinking] Potency on each target / 2) Gloom damage against 2 random enemies (max 15; prioritizes targeted enemies with the most [Sinking] Potency)
   PL: jeżeli liczba celów ataku wynosi 1, Moc Monety +2, +100% obrażeń (w walkach skupionych ocenia się względem Rdzenia)\n[WhenUse] jeżeli główny cel ma [Sinking] 4+, Moc Walce +1\n[BeforeAttack] jeżeli Odporność na Posępność głównego celu przekracza 1, zadaje +2% obrażeń za każde 0.1 nadwyżki (maks. 10%)\n[BeforeAttack] przy Rezonansie Posępności 2+ zadaje +5% obrażeń za każdy 1 Rezonansu Posępności (maks. 20%)\n[EndSkill] jeżeli zginął co najmniej 1 cel ataku, zadaje (Siła [Sinking] każdego celu / 2) obrażeń od Posępności 2 losowym wrogom (maks. 15; priorytet celom ataku z najwyższą Siłą [Sinking])
564. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2081011].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2081011].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
567. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2081011].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2081011].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Binding] następnej tury
569. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2081011].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2081011].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 공격 대상 중 흐트러지거나 부위 파괴 또는 사망한 대상이 있으면, 공격 대상이 아닌 무작위 적 1명에게 [Sinking] 2 부여 (턴당 1회, 집중 전투인 경우, 부위를 대상 1명으로 취급)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If there are Staggered, Part broken, or killed units among the targets, inflict 2 [Sinking] against a random non-targeted enemy (once per turn; in Focused Encounters, each Part count as 1 target)
   PL: [OnSucceedAttack] jeżeli wśród celów ataku są jednostki Oszołomione, ze Zniszczoną Częścią lub pokonane, nakłada 2 [Sinking] na 1 losowego wroga, który nie jest celem ataku (1 raz na turę; w walkach skupionych każda Część liczy się jako 1 cel)
571. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 3 — opis] - 공격 대상이 1명이면, 대신 3명에게 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   EN: - If there is just a single target, apply it to 3 targets instead
   PL: - jeżeli celów ataku jest tylko 1, zamiast tego dotyczy 3 celów
572. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 공격 대상이 1명이면, 코인 위력 +2, 피해량 +100% (집중 전투인 경우, 본체를 기준으로 판정)\n[WhenUse] 메인 타겟의 [Sinking] 4 이상이면, 합 위력 +1\n[BeforeAttack] 메인 타겟의 우울 내성이 1을 초과하면, 초과하는 값 0.1 당 피해량 +<style="highlight">3</style>% (최대 <style="highlight">15</style>%)\n[BeforeAttack] 우울 공명이 2 이상이면, 우울 공명 1당 피해량 +<style="highlight">8</style>% (최대 <style="highlight">32</style>%)\n[EndSkill] 공격 대상이 1명 이상 사망했으면, 무작위 적 2명에게 (각 대상의 [Sinking] 위력/2)만큼 우울 피해를 줌. (최대 15. 공격 대상이고, [Sinking] 위력을 많이 보유한 순으로 적용)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [BeforeAttack], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When attacking just a single target(in Focused Encounters, a Core and its connected Parts count as a single target), Coin Power +2 and deal +100% damage\n[WhenUse] If the main target has 4+ [Sinking], Clash Power +1\n[BeforeAttack] If the main target has higher than 1 Gloom Resist., deal +<style="highlight">3</style>% damage for every 0.1 excess Resist. (max <style="highlight">15</style>%)\n[BeforeAttack] At 2+ Gloom Reson., deal +<style="highlight">8</style>% damage for every Gloom Reson. (max <style="highlight">32</style>%)\n[EndSkill] If 1 or more targets are killed, deal ([Sinking] Potency on each target / 2) Gloom damage against 2 random enemies (max 15; prioritizes targeted enemies with the most [Sinking] Potency)
   PL: jeżeli liczba celów ataku wynosi 1, Moc Monety +2, +100% obrażeń (w walkach skupionych ocenia się względem Rdzenia)\n[WhenUse] jeżeli główny cel ma [Sinking] 4+, Moc Walce +1\n[BeforeAttack] jeżeli Odporność na Posępność głównego celu przekracza 1, zadaje +<style="highlight">3</style>% obrażeń za każde 0.1 nadwyżki (maks. <style="highlight">15</style>%)\n[BeforeAttack] przy Rezonansie Posępności 2+ zadaje +<style="highlight">8</style>% obrażeń za każdy 1 Rezonansu Posępności (maks. <style="highlight">32</style>%)\n[EndSkill] jeżeli zginął co najmniej 1 cel ataku, zadaje (Siła [Sinking] każdego celu / 2) obrażeń od Posępności 2 losowym wrogom (maks. 15; priorytet celom ataku z najwyższą Siłą [Sinking])
574. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Vibration]
576. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Binding] next turn<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Binding] następnej tury<style="highlight"></style>
577. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 공격 대상 중 흐트러지거나 부위 파괴 또는 사망한 대상이 있으면, 공격 대상이 아닌 무작위 적 1명에게 [Sinking] 2 부여 (턴당 1회, 집중 전투인 경우, 부위를 대상 1명으로 취급)<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If there are Staggered, Part broken, or killed units among the targets, inflict 2 [Sinking] against a random non-targeted enemy (once per turn; for Focused Encounters, each Part count as 1 target)<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli wśród celów ataku są jednostki Oszołomione, ze Zniszczoną Częścią lub pokonane, nakłada 2 [Sinking] na 1 losowego wroga, który nie jest celem ataku (1 raz na turę; w walkach skupionych każda Część liczy się jako 1 cel)<style="highlight"></style>
578. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] - 공격 대상이 1명이면, 대신 3명에게 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=2081011].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: - When attacking just a single target, apply it to 3 targets instead<style="highlight"></style>
   PL: - jeżeli celów ataku jest tylko 1, zamiast tego dotyczy 3 celów<style="highlight"></style>
579. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=2081011].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 공격 대상이 1명이면, 코인 위력 +2, 피해량 +100% (집중 전투인 경우, 본체를 기준으로 판정)\n[WhenUse] 메인 타겟의 [Sinking] 4 <style="highlight">당 합 위력 +1 (최대 2)</style>\n[BeforeAttack] 메인 타겟의 우울 내성이 1을 초과하면, 초과하는 값 0.1 당 피해량 +<style="highlight">5</style>% (최대 <style="highlight">20</style>%)\n[BeforeAttack] 우울 공명이 2 이상이면, 우울 공명 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">40</style>%)\n[EndSkill] 공격 대상이 1명 이상 사망했으면, 무작위 적 2명에게 (각 대상의 [Sinking] 위력/2)만큼 우울 피해를 줌. (최대 15. 공격 대상이고, [Sinking] 위력을 많이 보유한 순으로 적용)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=4].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [BeforeAttack], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: When attacking just a single target(in Focused Encounters, a Core and its connected Parts count as a single target), Coin Power +2 and deal +100% damage\n[WhenUse] <style="highlight">Clash Power +1 for every 4 [Sinking] on the main target (max 2)</style>\n[BeforeAttack] If the main target has higher than 1 Gloom Resist., deal +<style="highlight">5</style>% damage for every 0.1 excess Resist. (max <style="highlight">20</style>%)\n[BeforeAttack] At 2+ Gloom Reson., deal +<style="highlight">10</style>% damage for every Gloom Reson. (max <style="highlight">40</style>%)\n[EndSkill] If 1 or more targets are killed, deal ([Sinking] Potency on each target / 2) Gloom damage against 2 random enemies (max 15; prioritizes targeted enemies with the most [Sinking] Potency)
   PL: jeżeli liczba celów ataku wynosi 1, Moc Monety +2, +100% obrażeń (w walkach skupionych ocenia się względem Rdzenia)\n[WhenUse] Moc Walce +1 za każde 4 [Sinking] głównego celu <style="highlight">(maks. 2)</style>\n[BeforeAttack] jeżeli Odporność na Posępność głównego celu przekracza 1, zadaje +<style="highlight">5</style>% obrażeń za każde 0.1 nadwyżki (maks. <style="highlight">20</style>%)\n[BeforeAttack] przy Rezonansie Posępności 2+ zadaje +<style="highlight">10</style>% obrażeń za każdy 1 Rezonansu Posępności (maks. <style="highlight">40</style>%)\n[EndSkill] jeżeli zginął co najmniej 1 cel ataku, zadaje (Siła [Sinking] każdego celu / 2) obrażeń od Posępności 2 losowym wrogom (maks. 15; priorytet celom ataku z najwyższą Siłą [Sinking])
581. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
583. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict <style="highlight">2</style> [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada <style="highlight">2</style> [Binding] następnej tury
584. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 공격 대상 중 흐트러지거나 부위 파괴 또는 사망한 대상이 있으면, 공격 대상이 아닌 무작위 적 1명에게 [Sinking] 2 부여 (턴당 1회, 집중 전투인 경우, 부위를 대상 1명으로 취급)<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081011].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If there are Staggered, Part broken, or killed units among the targets, inflict 2 [Sinking] against a random non-targeted enemy (once per turn; in Focused Encounters, each Part count as 1 target)<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli wśród celów ataku są jednostki Oszołomione, ze Zniszczoną Częścią lub pokonane, nakłada 2 [Sinking] na 1 losowego wroga, który nie jest celem ataku (1 raz na turę; w walkach skupionych każda Część liczy się jako 1 cel)<style="highlight"></style>
585. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 파도의 만가
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].name ; dataList[id=2081021].levelList[level=3].name ; dataList[id=2081021].levelList[level=4].name
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 스카디
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].abName ; dataList[id=2081021].levelList[level=3].abName ; dataList[id=2081021].levelList[level=4].abName
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] 메인 타겟의 [Sinking] 5 이상이면 합 위력 +1\n[BeforeAttack] 가장 높은 공명 수 3당 아래 효과 적용\n- 가중치 1 증가 (최대 2)\n- 피해량 +15% (최대 30%)\n[EndSkill] 다음 턴에 무작위 아군 (최대 공명 수)명에게 [HitDamageUp] 1 부여 (본인 포함, 최대 4명, 턴당 1회)
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [Sinking], [BeforeAttack], [EndSkill], [HitDamageUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] If main target has 5+ [Sinking], Clash Power +1\n[BeforeAttack] Gain the following effects for every 3 highest Reson.\n- Gain +1 Atk Weight (max 2)\n- Deal +15% damage (max 30%)\n[EndSkill] Apply 1 [HitDamageUp] next turn to (highest Reson.) random allies (including this unit; max 4 allies; once per turn)
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] jeżeli główny cel ma [Sinking] 5+, Moc Walce +1\n[BeforeAttack] zyskuje poniższe efekty za każde 3 najwyższego Rezonansu\n- Waga Ataku +1 (maks. 2)\n- +15% obrażeń (maks. 30%)\n[EndSkill] następnej tury nakłada 1 [HitDamageUp] na (liczba najwyższego Rezonansu) losowych sojuszników (wliczając tę jednostkę, maks. 4 sojuszników, 1 raz na turę)
588. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2081021].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2081021].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2081021].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=2081021].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=2081021].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=2081021].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] 메인 타겟의 [Sinking] 5 <style="highlight">당 합 위력 +1 (최대 2)</style>\n[BeforeAttack] 가장 높은 공명 수 3당 아래 효과 적용\n- 가중치 1 증가 (최대 2)\n- 피해량 +15% (최대 30%)\n[EndSkill] 다음 턴에 무작위 아군 (최대 공명 수)명에게 [HitDamageUp] 1 부여 (본인 포함, 최대 4명, 턴당 1회)\n<style="highlight">- 해당 공명이 우울 공명이거나 완전 공명이면, [AzureDamageUp] 1 추가 부여</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=3].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WhenUse], [Sinking], [BeforeAttack], [EndSkill], [HitDamageUp], [AzureDamageUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [AzureDamageUp] = 우울 피해량 증가 / Gloom DMG Up
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] <style="highlight">Clash Power +1 for every 5 [Sinking] on the main target (max 2)</style>\n[BeforeAttack] Gain the following effects for every 3 highest Reson.\n- Gain +1 Atk Weight (max 2)\n- Deal +15% damage (max 30%)\n[EndSkill] Apply 1 [HitDamageUp] next turn to (highest Reson.) random allies (including this unit; max 4 allies; once per turn)\n<style="highlight">- If the said Reson. was a Gloom Reson. or an A-Reson., apply 1 [AzureDamageUp] as well</style>
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] Moc Walce +1 za każde 5 [Sinking] głównego celu <style="highlight">(maks. 2)</style>\n[BeforeAttack] zyskuje poniższe efekty za każde 3 najwyższego Rezonansu\n- Waga Ataku +1 (maks. 2)\n- +15% obrażeń (maks. 30%)\n[EndSkill] następnej tury nakłada 1 [HitDamageUp] na (liczba najwyższego Rezonansu) losowych sojuszników (wliczając tę jednostkę, maks. 4 sojuszników, 1 raz na turę)\n<style="highlight">- jeżeli ten Rezonans był Rezonansem Posępności lub Rezonansem Absolutnym, dodatkowo nakłada 1 [AzureDamageUp]</style>
594. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 공격 대상 중 흐트러지거나 부위 파괴 또는 사망한 대상이 있으면, 공격 대상이 아닌 무작위 적 1명에게 다음 턴에 [AzureTakeDamageUp] 1 부여 (턴당 1회, 집중 전투인 경우, 부위를 대상 1명으로 취급)</style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: <style="highlight">[OnSucceedAttack] If there are Staggered, Part broken, or killed units among the targets, inflict 1 [AzureTakeDamageUp] next turn against a random non-targeted enemy (once per turn; for Focused Encounters, each Part counts as 1 target)</style>
   PL: <style="highlight">[OnSucceedAttack] jeżeli wśród celów ataku są jednostki Oszołomione, ze Zniszczoną Częścią lub pokonane, następnej tury nakłada 1 [AzureTakeDamageUp] na 1 losowego wroga, który nie jest celem ataku (1 raz na turę; w walkach skupionych każda Część liczy się jako 1 cel)</style>
595. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=2081021].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[WhenUse] 메인 타겟의 [Sinking] 5 당 합 위력 +1 (최대 <style="highlight">3</style>)\n[BeforeAttack] 가장 높은 공명 수 3당 아래 효과 적용 <style="highlight">(우울 공명이면 공명 요구 값 2로 감소)</style>\n- 가중치 1 증가 (최대 2)\n- 피해량 +15% (최대 30%)\n[EndSkill] 다음 턴에 무작위 아군 (최대 공명 수)명에게 [HitDamageUp] 1 부여 (본인 포함, 최대 4명, 턴당 1회)\n- 해당 공명이 우울 공명이거나 완전 공명이면, [AzureDamageUp] 1 추가 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=4].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [WhenUse], [Sinking], [BeforeAttack], [EndSkill], [HitDamageUp], [AzureDamageUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [AzureDamageUp] = 우울 피해량 증가 / Gloom DMG Up
   EN: [CantIdentify]\nTargets randomly\n[WhenUse] Clash Power +1 for every 5 [Sinking] on the main target (max <style="highlight">3</style>)\n[BeforeAttack] Gain the following effects for every 3 highest Reson. <style="highlight">(if it was a Gloom Reson., for every 2 highest Reson.)</style>\n- Gain +1 Atk Weight (max 2)\n- Deal +15% damage (max 30%)\n[EndSkill] Apply 1 [HitDamageUp] next turn to (highest Reson.) random allies (including this unit; max 4 allies; once per turn)\n- If the said Reson. was a Gloom Reson. or an A-Reson., apply 1 [AzureDamageUp] as well
   PL: [CantIdentify]\nAtakuje losowy cel\n[WhenUse] Moc Walce +1 za każde 5 [Sinking] głównego celu (maks. <style="highlight">3</style>)\n[BeforeAttack] zyskuje poniższe efekty za każde 3 najwyższego Rezonansu <style="highlight">(przy Rezonansie Posępności wymagana wartość Rezonansu zmniejsza się do 2)</style>\n- Waga Ataku +1 (maks. 2)\n- +15% obrażeń (maks. 30%)\n[EndSkill] następnej tury nakłada 1 [HitDamageUp] na (liczba najwyższego Rezonansu) losowych sojuszników (wliczając tę jednostkę, maks. 4 sojuszników, 1 raz na turę)\n- jeżeli ten Rezonans był Rezonansem Posępności lub Rezonansem Absolutnym, dodatkowo nakłada 1 [AzureDamageUp]
597. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 공격 대상 중 흐트러지거나 부위 파괴 또는 사망한 대상이 있으면, 공격 대상이 아닌 무작위 적 1명에게 다음 턴에 [AzureTakeDamageUp] 1 부여 (턴당 1회, 집중 전투인 경우, 부위를 대상 1명으로 취급)<style="highlight"></style>
   źródło: Skills_Ego_Personality-08.json :: dataList[id=2081021].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttack] If there are Staggered, Part broken, or killed units among the targets, inflict 1 [AzureTakeDamageUp] next turn against a random non-targeted enemy (once per turn; for Focused Encounters, each Part counts as 1 target)<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli wśród celów ataku są jednostki Oszołomione, ze Zniszczoną Częścią lub pokonane, następnej tury nakłada 1 [AzureTakeDamageUp] na 1 losowego wroga, który nie jest celem ataku (1 raz na turę; w walkach skupionych każda Część liczy się jako 1 cel)<style="highlight"></style>
600. [Pasywka E.G.O — nazwa] 심해의 춤
   źródło: Passive_Ego.json :: dataList[id=2081011].name
   limit: do 40 znaków
   EN: Abyssal Dance
   PL: Abisalny Taniec
601. [Pasywka E.G.O — opis] - 전투 시작 시 적이 1명만 있으면, 조작 패널에서 가장 왼쪽에 있는 자신의 공격 스킬 합 위력 +1, 합 승리 후 적중시 피해량 +11.5% (E.G.O 스킬 포함)\n- 복귀, 대기 해제한 턴 동안 자신의 속도 최솟값, 최댓값 +1, 합 위력 +1
   źródło: Passive_Ego.json :: dataList[id=2081011].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: if there is just a single enemy, this unit's leftmost Attack Skill on the Dashboard gains Clash Power +1, and deals +11.5% damage on Hit after Clash Win (including E.G.O Skills)\n- For the turns in which this unit Returned or Substituted in: Min & Max Speed +1, Clash Power +1
   PL: - na początku Walki jeżeli jest tylko 1 wróg, skrajna lewa Umiejętność Ataku tej jednostki na Pulpicie zyskuje Moc Walce +1, a przy trafieniu po wygranej Walce zadaje +11.5% obrażeń (wliczając Umiejętności E.G.O)\n- w turach, w których ta jednostka Wróciła na pole lub Zastąpiła inną jednostkę: Min. i Maks. Szybkość +1, Moc Walce +1

## E.G.O [20901] What is Cast (던져지는 것) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20901`

602. [Karta E.G.O — nazwa] 던져지는 것
   źródło: Egos.json :: dataList[id=20901].name
   limit: do 40 znaków
   EN: What is Cast
   PL: To, co Rzucone
603. [Karta E.G.O — opis] 로쟈 기본 EGO 장비
   źródło: Egos.json :: dataList[id=20901].desc
   limit: do 120 znaków
   EN: Rodion’s Base E.G.O
   PL: Podstawowe E.G.O Rodion
604. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 던져지는 것
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=1].name ; dataList[id=2090111].levelList[level=3].name ; dataList[id=2090111].levelList[level=4].name
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 로쟈
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=1].abName ; dataList[id=2090111].levelList[level=3].abName ; dataList[id=2090111].levelList[level=4].abName
   limit: do 40 znaków
   EN: Rodion
   PL: Rodion
606. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 체력이 50%이상이면, 피해량 +10%
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has 50%+ HP, deal +10% damage
   PL: jeżeli cel ma 50%+ HP, zadaje +10% obrażeń
607. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
608. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] 대상의 체력이 50%이상이면, 피해량 +30%
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=3].desc ; dataList[id=2090111].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 50%+ HP, deal +30% damage
   PL: jeżeli cel ma 50%+ HP, zadaje +30% obrażeń
609. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090111].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] Nakłada 4 Krwawienia
610. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 정신력 회복 효율 +2
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 SP Heal Efficiency next turn
   PL: [OnSucceedAttack] następnej tury zyskuje +2 wydajności odzysku SP
611. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 정신력 감소 효율 -2
   źródło: Skills_Ego.json :: dataList[id=2090111].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain -2 SP Loss Efficiency next turn
   PL: [OnSucceedAttack] następnej tury zyskuje -2 wydajności utraty SP
612. [Pasywka E.G.O — nazwa] 단절
   źródło: Passive_Ego.json :: dataList[id=2090111].name
   limit: do 40 znaków
   EN: Severance
   PL: Severance
613. [Pasywka E.G.O — opis] 정신력 회복 효율 +1, 정신력 감소 효율 -1
   źródło: Passive_Ego.json :: dataList[id=2090111].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MentalSystemResultIncrease_Typo], [MentalSystemResultDecrease_Typo]
   znaczenie tagów: [MentalSystemResultIncrease_Typo] = 정신력 회복 효율 / SP Heal Efficiency; [MentalSystemResultDecrease_Typo] = 정신력 감소 효율 / SP Loss Efficiency
   EN: +1 [MentalSystemResultIncrease_Typo], -1 [MentalSystemResultDecrease_Typo]
   PL: +1 [MentalSystemResultIncrease_Typo], -1 [MentalSystemResultDecrease_Typo]

## E.G.O [20902] 4th Match Flame (4번째 성냥불) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20902`

614. [Karta E.G.O — nazwa] 4번째 성냥불
   źródło: Egos.json :: dataList[id=20902].name
   limit: do 40 znaków
   EN: 4th Match Flame
   PL: 4. Płomyk Zapałki
615. [Karta E.G.O — opis] 로쟈 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20902].desc
   limit: do 120 znaków
   EN: Rodion’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Rodion
616. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,5) — nazwa] 4번째 성냥불
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=1].name ; dataList[id=2090211].levelList[level=3].name ; dataList[id=2090211].levelList[level=5].name
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,5) — źródło (Anomalia)] 불타버린 소녀
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=1].abName ; dataList[id=2090211].levelList[level=3].abName ; dataList[id=2090211].levelList[level=5].abName
   limit: do 40 znaków
   EN: Scorched Girl
   PL: Spopielona Dziewczynka
618. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 6 부여
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL: [OnSucceedAttack] nakłada 6 Podpalenia
620. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 분노 취약 3 부여
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Wrath Fragility next turn
   PL: [OnSucceedAttack] następnej tury nakłada 3 Kruchości Gniewu
621. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — opis] <style="highlight">최대 공명 수 1당, 피해량 +5% (최대 30%)\n[EndSkill] 다음 턴에 [CrimsonResultUp] 1, [CrimsonDamageUp] 1 얻음</style>
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=5].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill], [CrimsonResultUp], [CrimsonDamageUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [CrimsonResultUp] = 분노 위력 증가 / Wrath Power Up; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: <style="highlight">Deal +5% damage for every highest Reson. (max 30%)\n[EndSkill] Gain 1 [CrimsonResultUp] and 1 [CrimsonDamageUp] next turn</style>
   PL: <style="highlight">zadaje +5% obrażeń za każdy 1 najwyższego Rezonansu (maks. 30%)\n[EndSkill] następnej tury zyskuje 1 [CrimsonResultUp] i 1 [CrimsonDamageUp]</style>
622. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[SuperCoin]</style>
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: <style="highlight">[SuperCoin]</style>
   PL: <style="highlight">[SuperCoin]</style>
623. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 2 — opis] <style="highlight">[UnBrokenCoinOnSucceedAttack]</style> [Combustion] 6 부여
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[UnBrokenCoinOnSucceedAttack]</style> Inflict 6 [Combustion]
   PL: <style="highlight">[UnBrokenCoinOnSucceedAttack]</style> [Combustion] 6 Podpalenia
624. [E.G.O — Przebudzenie (Awakening) (ulepszenie 5) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [CrimsonTakeDamageUp] 3 부여<style="highlight"></style>
   źródło: Skills_Ego.json :: dataList[id=2090211].levelList[level=5].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [CrimsonTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: [OnSucceedAttack] Inflict 3 [CrimsonTakeDamageUp] next turn<style="highlight"></style>
   PL: [OnSucceedAttack] następnej tury nakłada 3 [CrimsonTakeDamageUp]<style="highlight"></style>
625. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,5) — nazwa] 4번째 성냥불
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=1].name ; dataList[id=2090221].levelList[level=3].name ; dataList[id=2090221].levelList[level=5].name
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,5) — źródło (Anomalia)] 불타버린 소녀
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=1].abName ; dataList[id=2090221].levelList[level=3].abName ; dataList[id=2090221].levelList[level=5].abName
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=1].desc ; dataList[id=2090221].levelList[level=3].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 4 부여
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 6 부여
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 619 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 분노 취약 3 부여
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — opis] [CantIdentify]\n무작위 대상 공격\n<style="highlight">최대 공명 수 1당, 피해량 +5% (최대 30%)\n[DefeatDuel] 기본 위력 -18\n[EndSkill] 다음 턴에 [CrimsonResultUp] 2, [CrimsonDamageUp] 1 얻음</style>
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=5].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [DefeatDuel], [EndSkill], [CrimsonResultUp], [CrimsonDamageUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [CrimsonResultUp] = 분노 위력 증가 / Wrath Power Up; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: [CantIdentify]\nTargets randomly\n<style="highlight">Deal +5% damage for every highest Reson. (max 30%)\n[DefeatDuel] Base Power -18\n[EndSkill] Gain 2 [CrimsonResultUp] and 1 [CrimsonDamageUp] next turn</style>
   PL: [CantIdentify]\nAtakuje losowy cel\n<style="highlight">zadaje +5% obrażeń za każdy 1 najwyższego Rezonansu (maks. 30%)\n[DefeatDuel] Moc Bazowa -18\n[EndSkill] następnej tury zyskuje 2 [CrimsonResultUp] i 1 [CrimsonDamageUp]</style>
632. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 1 — opis] <style="highlight">[SuperCoin]</style>
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=5].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] <style="highlight">10</style> 부여
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">10</style> [Combustion]
   PL: [OnSucceedAttack] [Combustion] <style="highlight">10</style> Podpalenia
634. [E.G.O — Korozja (Corrosion) (ulepszenie 5) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [CrimsonTakeDamageUp] 3 부여<style="highlight"></style>
   źródło: Skills_Ego.json :: dataList[id=2090221].levelList[level=5].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Pasywka E.G.O — nazwa] 불씨
   źródło: Passive_Ego.json :: dataList[id=2090211].name
   limit: do 40 znaków
   EN: Spark of Flame
   PL: Ognik
636. [Pasywka E.G.O — opis] [Combustion]이 부여된 적 처치 시 최대 체력의 (분노 완전 공명 수)% 만큼 체력 회복
   źródło: Passive_Ego.json :: dataList[id=2090211].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: After defeating an enemy that has [Combustion], heal (Wrath A-Reson.)% HP
   PL: po pokonaniu wroga z [Combustion] odzyskuje HP równe (Rezonansowi Absolutnemu Gniewu)% Maks. HP
637. [Pasywka E.G.O — nazwa] 불씨
   źródło: Passive_Ego.json :: dataList[id=2090212].name
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Pasywka E.G.O — opis] <style="highlight">전투 시작 시 분노 완전 공명이 발동했으면, 합 승리 시 메인 타겟에게 [CrimsonTakeDamageUp] 1 부여 (턴당 1회)</style>\n\n[Combustion]이 부여된 적 처치 시 최대 체력의 <style="highlight">(분노 공명 수)</style>% 만큼 체력 회복 <style="highlight">(최대 12%)</style>
   źródło: Passive_Ego.json :: dataList[id=2090212].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CrimsonTakeDamageUp], [Combustion]
   znaczenie tagów: [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [Combustion] = 화상 / Burn
   EN: <style="highlight">Combat Start: If Wrath A-Reson. was activated, inflict 1 [CrimsonTakeDamageUp] on the main target on Clash Win (once per turn)</style>\n\nAfter defeating an enemy that has [Combustion], heal <style="highlight">(Wrath Reson.)</style>% HP <style="highlight">(max 12%)</style>
   PL: <style="highlight">na początku Walki jeżeli został aktywowany Rezonans Absolutny Gniewu, przy wygranej Walce nakłada 1 [CrimsonTakeDamageUp] na główny cel (1 raz na turę)</style>\n\npo pokonaniu wroga z [Combustion] odzyskuje HP równe <style="highlight">(Rezonansowi Gniewu)</style>% Maks. HP <style="highlight">(maks. 12%)</style>
639. [Pasywka E.G.O — podsumowanie] [CrimsonTakeDamageUp] 부여\n조건 만족 시 일정 체력 회복
   źródło: Passive_Ego.json :: dataList[id=2090212].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CrimsonTakeDamageUp]
   znaczenie tagów: [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: Inflict [CrimsonTakeDamageUp]\nHeal HP when conditions are met
   PL: nakłada [CrimsonTakeDamageUp]\nodzyskuje HP po spełnieniu warunków

## E.G.O [20903] Rime Shank (얼음다리) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20903`

640. [Karta E.G.O — nazwa] 얼음다리
   źródło: Egos.json :: dataList[id=20903].name
   limit: do 40 znaków
   EN: Rime Shank
   PL: Rime Shank
641. [Karta E.G.O — opis] 로쟈 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20903].desc
   (powtórzenie elementu 615 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 얼음다리
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=1].name ; dataList[id=2090311].levelList[level=3].name ; dataList[id=2090311].levelList[level=4].name
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 바바야가
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=1].abName ; dataList[id=2090311].levelList[level=3].abName ; dataList[id=2090311].levelList[level=4].abName
   limit: do 40 znaków
   EN: Baba Yaga
   PL: Baba Yaga
644. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 체력이 50%이상이면, 피해량 +10%
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target’s HP is above 50%, deal +10% damage
   PL: jeżeli HP celu wynosi 50% lub więcej, zadaje +10% obrażeń
645. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackHead] Trigger [VibrationExplosion]
   PL: [OnSucceedAttackHead] Wybuch Wstrząsu
646. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Zatonięcia
647. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — opis] 대상의 체력이 50%이상이면, 피해량 +30%
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=3].desc ; dataList[id=2090311].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target’s HP is above 50%, deal +30% damage
   PL: jeżeli HP celu wynosi 50% lub więcej, zadaje +30% obrażeń
648. [E.G.O — Przebudzenie (Awakening) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090311].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Zatonięcia
650. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 5 부여\n[OnSucceedAttack] 침잠 횟수 5 증가
   źródło: Skills_Ego.json :: dataList[id=2090311].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]\n[OnSucceedAttack] Inflict +5 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 5 [Sinking]\n[OnSucceedAttack] nakłada +5 Licznika [Sinking]
651. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 얼음다리
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=1].name ; dataList[id=2090321].levelList[level=3].name ; dataList[id=2090321].levelList[level=4].name
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 바바야가
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=1].abName ; dataList[id=2090321].levelList[level=3].abName ; dataList[id=2090321].levelList[level=4].abName
   (powtórzenie elementu 643 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n체력이 가장 많은 대상 공격\n대상의 체력이 50%이상이면, 피해량 +10%
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets the unit with the most HP\nIf target’s HP is above 50%, +10% Damage
   PL: [CantIdentify]\nAtakuje cel z najwyższym HP\njeżeli HP celu wynosi 50% lub więcej, +10% obrażeń
654. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 4 증가
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +4 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +4 Licznika Zatonięcia
656. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — opis] [CantIdentify]\n체력이 가장 많은 대상 공격\n대상의 체력이 50%이상이면, 피해량 +30%
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=3].desc ; dataList[id=2090321].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nTargets the unit with the most HP\nIf target’s HP is above 50%, +30% Damage
   PL: [CantIdentify]\nAtakuje cel z najwyższym HP\njeżeli HP celu wynosi 50% lub więcej, +30% obrażeń
657. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090321].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 6 증가
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +6 [Sinking] Count
   PL: [OnSucceedAttack] nakłada +6 Licznika [Sinking]
659. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 10 부여\n[OnSucceedAttack] 침잠 횟수 8 증가
   źródło: Skills_Ego.json :: dataList[id=2090321].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 10 [Sinking]\n[OnSucceedAttack] Inflict +8 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 10 [Sinking]\n[OnSucceedAttack] nakłada +8 Licznika [Sinking]
660. [Pasywka E.G.O — nazwa] 추위
   źródło: Passive_Ego.json :: dataList[id=2090311].name
   limit: do 40 znaków
   EN: Coldness
   PL: Zimno
661. [Pasywka E.G.O — opis] [Sinking]이 5 이상 부여된 적에게 공격 적중 시 다음 턴에 속박, 공격 위력 감소 1 부여\n(적 1명 당 최대 3)
   źródło: Passive_Ego.json :: dataList[id=2090311].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [Binding], [Reduction]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: On hit, if the target has 5+ [Sinking], inflict 1 [Binding] and [Reduction] next turn\n(3 times per unit)
   PL: przy trafieniu wroga, na którego nałożono 5+ [Sinking], następnej tury nakłada 1 [Binding] i 1 [Reduction]\n(3 razy na wroga)

## E.G.O [20904] Effervescent Corrosion (들끓는 부식) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20904`

662. [Karta E.G.O — nazwa] 들끓는 부식
   źródło: Egos.json :: dataList[id=20904].name
   limit: do 40 znaków
   EN: Effervescent Corrosion
   PL: Musująca Korozja
663. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20904].desc
   limit: do 120 znaków
   EN: Rodion’s E.G.O Gear
   PL: Wyłączny Sprzęt E.G.O Rodion
664. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 들끓는 부식
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=1].name ; dataList[id=2090411].levelList[level=3].name ; dataList[id=2090411].levelList[level=4].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 걷는 진주
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=1].abName ; dataList[id=2090411].levelList[level=3].abName ; dataList[id=2090411].levelList[level=4].abName
   limit: do 40 znaków
   EN: Ambling Pearl
   PL: Krocząca Perła
666. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Tremor Count
   PL: [OnSucceedAttack] nakłada +3 Licznika Trzęsienia
667. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 속박 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2090411].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2090411].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bind next turn
   PL: [OnSucceedAttackHead] następnej tury nakłada 2 Bind
668. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [BeforeAttack] 메인 공격 대상의 체력이 최대 체력의 50% 이상이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] If main target has 50%+ HP, Atk Weight +1
   PL: [BeforeAttack] jeżeli główny cel ataku ma 50%+ Maks. HP, Waga Ataku +1
669. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3, 진동 횟수 5 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor and +5 Tremor Count
   PL: [OnSucceedAttack] nakłada 3 Trzęsienia i +5 Licznika Trzęsienia
670. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Trigger Tremor Burst
   PL: [OnSucceedAttackHead] Wybuch Wstrząsu
671. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] 메인 공격 대상의 체력이 최대 체력의 50% 이상이면, 공격 가중치 +1, 최대 체력의 75% 이상이면, 추가로 공격 가중치 +1
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] If main target has 50%+ HP, Atk Weight +1;\nIf main target has 75%+ HP, additional Atk Weight +1
   PL: [BeforeAttack] jeżeli główny cel ataku ma 50%+ Maks. HP, Waga Ataku +1;\njeżeli ma 75%+ Maks. HP, dodatkowo Waga Ataku +1
672. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3, 진동 횟수 7 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor and +7 Tremor Count
   PL: [OnSucceedAttack] nakłada 3 Trzęsienia i +7 Licznika Trzęsienia
673. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090411].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL: [OnSucceedAttack] Wybuch Wstrząsu
674. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 들끓는 부식
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=1].name ; dataList[id=2090421].levelList[level=3].name ; dataList[id=2090421].levelList[level=4].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 걷는 진주
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=1].abName ; dataList[id=2090421].levelList[level=3].abName ; dataList[id=2090421].levelList[level=4].abName
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=1].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 자신의 체력 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2090421].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090421].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 30% of damage dealt
   PL: [OnSucceedAttack] odzyskuje HP równe 30% zadanych obrażeń
678. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 메인 공격 대상의 체력이 최대 체력의 50% 이상이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] If main target has 50%+ HP, Atk Weight +1
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] jeżeli główny cel ataku ma 50%+ Maks. HP, Waga Ataku +1
680. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 3 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Defense Level Down
   PL: [OnSucceedAttack] nakłada 3 zmniejszenia Poziomu Obrony
681. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=2090421].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 메인 공격 대상의 체력이 최대 체력의 50% 이상이면, 공격 가중치 +1, 최대 체력의 75% 이상이면, 추가로 공격 가중치 +1
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] If main target has 50%+ HP, Atk Weight +1;\nIf main target has 75%+ HP, additional Atk Weight +1
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] jeżeli główny cel ataku ma 50%+ Maks. HP, Waga Ataku +1;\njeżeli ma 75%+ Maks. HP, dodatkowo Waga Ataku +1
683. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 5 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090421].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Defense Level Down
   PL: [OnSucceedAttack] nakłada 5 zmniejszenia Poziomu Obrony
684. [Pasywka E.G.O — nazwa] 끈적거리는 오물
   źródło: Passive_Ego.json :: dataList[id=2090411].name
   limit: do 40 znaków
   EN: Sticky Filth
   PL: Lepka Brud
685. [Pasywka E.G.O — opis] 관통 속성 스킬로 앞면 적중 시 속박 1 부여 (턴 당 최대 2회)
   źródło: Passive_Ego.json :: dataList[id=2090411].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: On Heads Hit with a Pierce Skill, inflict 1 [Binding] (2 times per turn)
   PL: przy trafieniu Monetą na Wierzch Umiejętnością Kłucia nakłada 1 [Binding] (maks. 2 razy na turę)

## E.G.O [20905] Pursuance (집행) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20905`

686. [Karta E.G.O — nazwa] 집행
   źródło: Egos.json :: dataList[id=20905].name
   limit: do 40 znaków
   EN: Pursuance
   PL: Egzekucja
687. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20905].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 집행
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=1].name ; dataList[id=2090511].levelList[level=3].name ; dataList[id=2090511].levelList[level=4].name
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 하늘 집행관의 보좌
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=1].abName ; dataList[id=2090511].levelList[level=3].abName ; dataList[id=2090511].levelList[level=4].abName
   limit: do 40 znaków
   EN: Heavenly Executor’s Scribe
   PL: Skryba Niebiańskiego Egzekutora
690. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 나태 취약 1 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2090511].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Sloth Fragility next turn
   PL: [OnSucceedAttackHead] następnej tury nakłada 1 Kruchości Nieczułości
691. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndSkill] 자신을 제외하고 현재 체력이 비율이 가장 낮은 아군 2명의 체력을 자신의 최대 체력의 15%만큼 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 2 other allies with the least HP percentage for 15% of this unit's Max HP
   PL: [EndSkill] odzyskuje HP równe 15% Maks. HP tej jednostki dla 2 innych sojuszników z najniższym aktualnym procentem HP
692. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [EndSkill] 자신을 제외하고 현재 체력이 비율이 가장 낮은 아군 2명의 체력을 자신의 최대 체력의 25%만큼 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 2 other allies with the least HP percentage for 25% of this unit's Max HP
   PL: [EndSkill] odzyskuje HP równe 25% Maks. HP tej jednostki dla 2 innych sojuszników z najniższym aktualnym procentem HP
693. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 3 — opis] [EndSkillHead] 대상이 흐트러지거나 사망한 경우, 체력을 회복시킨 캐릭터들에게 자신의 최대 체력의 10%만큼 보호막 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]
   EN: [EndSkillHead] If target is Staggered or defeated, apply 10% of this unit's Max HP as Shield to allies that this unit healed
   PL: [EndSkillHead] jeżeli cel jest Oszołomiony lub pokonany, nakłada Tarczę równą 10% Maks. HP tej jednostki na sojuszników, których ta jednostka leczyła
694. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 나태 취약 1 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Sloth Fragility next turn
   PL: [OnSucceedAttack] następnej tury nakłada 1 Kruchości Nieczułości
695. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndSkill] 자신을 제외하고 현재 체력이 비율이 가장 낮은 아군 2명의 체력을 자신의 최대 체력의 30%만큼 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal 2 other allies with the least HP percentage for 30% of this unit's Max HP
   PL: [EndSkill] odzyskuje HP równe 30% Maks. HP tej jednostki dla 2 innych sojuszników z najniższym aktualnym procentem HP
696. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 3 — opis] [EndSkillHead] 대상이 흐트러지거나 사망한 경우, 체력을 회복시킨 캐릭터들에게 자신의 최대 체력의 15%만큼 보호막 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090511].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [EndSkillHead]
   znaczenie tagów: [EndSkillHead] = [앞면 공격 종료 시] / [Heads Attack End]
   EN: [EndSkillHead] If target is Staggered or defeated, apply 15% of this unit's Max HP as Shield to allies that this unit healed
   PL: [EndSkillHead] jeżeli cel jest Oszołomiony lub pokonany, nakłada Tarczę równą 15% Maks. HP tej jednostki na sojuszników, których ta jednostka leczyła
697. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 집행
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=1].name ; dataList[id=2090521].levelList[level=3].name ; dataList[id=2090521].levelList[level=4].name
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 하늘 집행관의 보좌
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=1].abName ; dataList[id=2090521].levelList[level=3].abName ; dataList[id=2090521].levelList[level=4].abName
   (powtórzenie elementu 689 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=1].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2090521].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090521].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 15 피해
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 체력이 50% 미만이면, 공격 가중치 +1
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 50%- HP, Atk Weight +1
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy HP tej jednostki niższym niż 50%, Waga Ataku +1
703. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 20 피해
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2090521].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 20 SP damage
   PL: [OnSucceedAttack] zadaje celowi 20 obrażeń SP
704. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackTail] 대상이 흐트러지거나 사망한 경우 자신의 정신력 5 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] If target is Staggered or defeated, heal 5 SP on self
   PL: [OnSucceedAttackTail] jeżeli cel jest Oszołomiony lub pokonany, odzyskuje 5 SP
705. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] 자신의 체력이 50% 미만이면, 공격 가중치 +2
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] At 50%- HP, Atk Weight +2
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] przy HP tej jednostki niższym niż 50%, Waga Ataku +2
706. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러지거나 사망한 경우 자신의 정신력 7 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090521].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered or defeated, heal 7 SP on self
   PL: [OnSucceedAttack] jeżeli cel jest Oszołomiony lub pokonany, odzyskuje 7 SP
707. [Pasywka E.G.O — nazwa] 하늘의 선고
   źródło: Passive_Ego.json :: dataList[id=2090511].name
   limit: do 40 znaków
   EN: Sentencing from Above
   PL: Wyrok z Niebios
708. [Pasywka E.G.O — opis] 적이 흐트러짐 상태에 빠질 때마다 아군 중 현재 체력 비율이 가장 낮은 아군 1명이 해당 캐릭터의 최대 체력의 4%만큼 체력을 회복 (턴 당 1회 발동)
   źródło: Passive_Ego.json :: dataList[id=2090511].desc
   limit: do 150 znaków
   EN: Whenever an enemy is Staggered, the ally with the least HP percentage heals 4% of their Max HP. (Once per turn)
   PL: za każdym Oszołomieniem wroga sojusznik z najniższym aktualnym procentem HP odzyskuje HP równe 4% Maks. HP tego sojusznika (1 raz na turę)

## E.G.O [20906] Sanguine Desire (핏빛욕망) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20906`

709. [Karta E.G.O — nazwa] 핏빛욕망
   źródło: Egos.json :: dataList[id=20906].name
   limit: do 40 znaków
   EN: Sanguine Desire
   PL: Krwiste Pożądanie
710. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20906].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 핏빛욕망
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].name ; dataList[id=2090611].levelList[level=3].name ; dataList[id=2090611].levelList[level=4].name
   (powtórzenie elementu 709 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 빨간 구두
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].abName ; dataList[id=2090611].levelList[level=3].abName ; dataList[id=2090611].levelList[level=4].abName
   limit: do 40 znaków
   EN: The Red Shoes
   PL: Czerwone Buty
713. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] 대상의 [Laceration] 2당 코인 위력 +1 (최대 6)\n[StartBattle] 이 스킬의 메인 타겟은 이번 턴 동안 [Laceration] 횟수가 감소하지 않음.\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소.
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [StartBattle], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +1 for every 2 [Laceration] on target (max 6)\n[StartBattle] The main target for this Skill does not lose [Laceration] Count for this turn.\n[EndSkill] For 3 turns, Lose 10 SP at Turn End.
   PL: Moc Monety +1 za każde 2 [Laceration] na celu (maks. 6)\n[StartBattle] główny cel tej Umiejętności nie traci Licznika [Laceration] w tej turze.\n[EndSkill] przez 3 tury traci 10 SP na koniec tury.
714. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력만큼 색욕 속성 피해를 줌.\n- 색욕 공명이 4 이상이면, 1.2배로 계산\n(계산 시 반영되는 [Laceration] 위력은 99를 초과할 수 없음.)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict Lust Affinity damage equal to [Laceration] Potency on target.\n- At 4+ Lust Reson., inflict Lust Affinity damage equal to ([Laceration] Potency on target x 1.2).\n([Laceration] Potency up to only 99 will be used to calculate for this Skill.)
   PL: [OnSucceedAttack] zadaje obrażenia Grzechu Żądzy równe Siły [Laceration] celu.\n- przy Rezonansie Żądzy 4+ zadaje obrażenia równe (Siła [Laceration] celu x 1.2)\n(przy obliczaniu uwzględnia się Siłę [Laceration] tylko do 99)
715. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]에 비례하여 색욕 속성 피해
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].coinlist[#0].coindescs[#0].summary ; dataList[id=2090611].levelList[level=3].coinlist[#0].coindescs[#0].summary ; dataList[id=2090611].levelList[level=4].coinlist[#0].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal Lust Affinity damage based on [Laceration] on target
   PL: [OnSucceedAttack] zadaje obrażenia Grzechu Żądzy proporcjonalne do [Laceration] celu
716. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [EnemyKill] 이 스킬의 피해 또는 코인 효과로 적의 남은 체력을 초과하여 피해를 준 경우, 초과한 피해량을 고정 피해로 적 전체에 나눠서 가함.\n(집중 전투인 경우, 본체의 체력을 기준으로 계산)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=2090611].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2090611].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] If this Skill or its Coin effects dealt damage that exceeds the target's(In Focused Encounters, the Core's) remaining HP, deal the excess damage as fixed damage between all enemies.
   PL: [EnemyKill] jeżeli ta Umiejętność lub jej efekty Monety zadały obrażenia przekraczające pozostałe HP celu, rozdziela nadwyżkę obrażeń jako stałe obrażenia między wszystkich wrogów.\n(w walkach skupionych oblicza się względem HP Rdzenia)
717. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — moneta 1, efekt 2 — podsumowanie] [EnemyKill] 초과 피해를 준 경우, 초과 피해량을 적 전체에 나눠서 가함.
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=1].coinlist[#0].coindescs[#1].summary ; dataList[id=2090611].levelList[level=3].coinlist[#0].coindescs[#1].summary ; dataList[id=2090611].levelList[level=4].coinlist[#0].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Inflict the excess damage between all enemies.
   PL: [EnemyKill] jeżeli zada nadwyżkowe obrażenia, rozdziela je między wszystkich wrogów
718. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] 대상의 [Laceration] 2당 코인 위력 +1 (최대 <style="highlight">9</style>)\n[StartBattle] 이 스킬의 메인 타겟은 이번 턴 동안 [Laceration] 횟수가 감소하지 않음.\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소.
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +1 for every 2 [Laceration] on target (max <style="highlight">9</style>)\n[StartBattle] The main target for this Skill does not lose [Laceration] Count for this turn.\n[EndSkill] For 3 turns, Lose 10 SP at Turn End.
   PL: Moc Monety +1 za każde 2 [Laceration] na celu (maks. <style="highlight">9</style>)\n[StartBattle] główny cel tej Umiejętności nie traci Licznika [Laceration] w tej turze.\n[EndSkill] przez 3 tury traci 10 SP na koniec tury.
719. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <style="highlight">(대상의 [Laceration] 위력 x 1.2)</style>만큼 색욕 속성 피해를 줌.\n- 색욕 공명이 4 이상이면, x<style="highlight">1.5</style>로 계산.\n<style="highlight">- 최대 색욕 완전 공명 수가 4 이상이면, x1.8로 계산.</style>\n(계산 시 반영되는 [Laceration] 위력은 99를 초과할 수 없음.)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict Lust Affinity damage equal to <style="highlight">([Laceration] Potency on target x 1.2)</style>.\n- At 4+ Lust Reson., inflict Lust Affinity damage equal to ([Laceration] Potency on target x <style="highlight">1.5</style>).\n<style="highlight">- At 4+ Lust A-Reson., inflict Lust Affinity damage equal to ([Laceration] Potency on target x 1.8).</style>\n([Laceration] Potency up to only 99 will be used to calculate for this Skill.)
   PL: [OnSucceedAttack] zadaje obrażenia Grzechu Żądzy równe <style="highlight">(Siła [Laceration] celu x 1.2)</style>.\n- przy Rezonansie Żądzy 4+ zadaje obrażenia równe (Siła [Laceration] celu x <style="highlight">1.5</style>)\n<style="highlight">- przy Rezonansie Absolutnym Żądzy 4+ zadaje obrażenia równe (Siła [Laceration] celu x 1.8).</style>\n(przy obliczaniu uwzględnia się Siłę [Laceration] tylko do 99)
720. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] 대상의 [Laceration] 2당 코인 위력 +1 (최대 <style="highlight">13</style>)\n[StartBattle] 이 스킬의 메인 타겟은 이번 턴 동안 [Laceration] 횟수가 감소하지 않음.\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소.
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +1 for every 2 [Laceration] on target (max <style="highlight">13</style>)\n[StartBattle] The main target for this Skill does not lose [Laceration] Count for this turn.\n[EndSkill] For 3 turns, Lose 10 SP at Turn End.
   PL: Moc Monety +1 za każde 2 [Laceration] na celu (maks. <style="highlight">13</style>)\n[StartBattle] główny cel tej Umiejętności nie traci Licznika [Laceration] w tej turze.\n[EndSkill] przez 3 tury traci 10 SP na koniec tury.
721. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (대상의 [Laceration] 위력 x <style="highlight">1.5</style>)만큼 색욕 속성 피해를 줌.\n- 색욕 공명이 4 이상이면, x<style="highlight">1.8</style>로 계산.\n- 최대 색욕 완전 공명 수가 4 이상이면, x<style="highlight">2</style>로 계산.\n(계산 시 반영되는 [Laceration] 위력은 99를 초과할 수 없음.)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090611].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict Lust Affinity damage equal to ([Laceration] Potency on target x <style="highlight">1.5</style>)\n- At 4+ Lust Reson., inflict Lust Affinity damage equal to ([Laceration] Potency on target x <style="highlight">1.8</style>).\n- At 4+ Lust A-Reson., inflict Lust Affinity damage equal to ([Laceration] Potency on target x <style="highlight">2</style>).\n([Laceration] Potency up to only 99 will be used to calculate for this Skill.)
   PL: [OnSucceedAttack] zadaje obrażenia Grzechu Żądzy równe (Siła [Laceration] celu x <style="highlight">1.5</style>)\n- przy Rezonansie Żądzy 4+ zadaje obrażenia równe (Siła [Laceration] celu x <style="highlight">1.8</style>)\n- przy Rezonansie Absolutnym Żądzy 4+ zadaje obrażenia równe (Siła [Laceration] celu x <style="highlight">2</style>)\n(przy obliczaniu uwzględnia się Siłę [Laceration] tylko do 99)
722. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 핏빛욕망
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=1].name ; dataList[id=2090621].levelList[level=3].name ; dataList[id=2090621].levelList[level=4].name
   (powtórzenie elementu 709 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 빨간 구두
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=1].abName ; dataList[id=2090621].levelList[level=3].abName ; dataList[id=2090621].levelList[level=4].abName
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (가장 높은 공명 수 - 2) 만큼 공격 가중치 증가 (최대 2)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=1].desc ; dataList[id=2090621].levelList[level=3].desc ; dataList[id=2090621].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (# of highest Reson. - 2) Atk Weight (max 2)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (liczba najwyższego Rezonansu - 2) Wagi Ataku (maks. 2)
725. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 2 + (색욕 공명 수)만큼 [Laceration] 부여\n(공명 수 비례 최대 [Laceration] 부여량 : 4)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (2 + (Lust Reson.)) [Laceration]\n(Maximum Lust Reson. taken into account : 4)
   PL: [OnSucceedAttack] nakłada (2 + Rezonans Żądzy) [Laceration]\n(maks. 4 [Laceration] proporcjonalnie do Rezonansu)
726. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 2 + 색욕 공명 수만큼 [Laceration] 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=1].coinlist[#0].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (2 + (Lust Reson.)) [Laceration]
   PL: [OnSucceedAttack] nakłada (2 + Rezonans Żądzy) [Laceration]
727. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <style="highlight">3</style> + (색욕 공명 수)만큼 [Laceration] 부여\n(공명 수 비례 최대 [Laceration] 부여량 : <style="highlight">5</style>)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (<style="highlight">3</style> + (Lust Reson.)) [Laceration]\n(Maximum Lust Reson. taken into account : <style="highlight">5</style>)
   PL: [OnSucceedAttack] nakłada (<style="highlight">3</style> + Rezonans Żądzy) [Laceration]\n(maks. <style="highlight">5</style> [Laceration] proporcjonalnie do Rezonansu)
728. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 3 + 색욕 공명 수만큼 [Laceration] 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=3].coinlist[#0].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (3 + (Lust Reson.)) [Laceration]
   PL: [OnSucceedAttack] nakłada (3 + Rezonans Żądzy) [Laceration]
729. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
730. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <style="highlight">4</style> + (색욕 공명 수)만큼 [Laceration] 부여\n(공명 수 비례 최대 [Laceration] 부여량 : <style="highlight">6</style>)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (<style="highlight">4</style> + (Lust Reson.)) [Laceration]\n(Maximum Lust Reson. taken into account : <style="highlight">6</style>)
   PL: [OnSucceedAttack] nakłada (<style="highlight">4</style> + Rezonans Żądzy) [Laceration]\n(maks. <style="highlight">6</style> [Laceration] proporcjonalnie do Rezonansu)
731. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 4 + 색욕 공명 수만큼 [Laceration] 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=4].coinlist[#0].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict (4 + (Lust Reson.)) [Laceration]
   PL: [OnSucceedAttack] nakłada (4 + Rezonans Żądzy) [Laceration]
732. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090621].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">3</style> [Laceration] Count
   PL: [OnSucceedAttack] nakłada +<style="highlight">3</style> Licznika [Laceration]
733. [Pasywka E.G.O — nazwa] 집착
   źródło: Passive_Ego.json :: dataList[id=2090611].name
   limit: do 40 znaków
   EN: Obsession
   PL: Obsesja
734. [Pasywka E.G.O — opis] 자신의 스킬 패널에서 가장 왼쪽에 위치한 스킬의 [Laceration] 위력 부여량이 2배로 증가 (턴 당 1회 적용)
   źródło: Passive_Ego.json :: dataList[id=2090611].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: This unit's leftmost Skill on the Dashboard inflicts double the [Laceration] Potency (once per turn)
   PL: skrajna lewa Umiejętność tej jednostki na Pulpicie nakłada 2 razy większą Siłę [Laceration] (1 raz na turę)
735. [Pasywka E.G.O — podsumowanie] 스킬의 [Laceration] 위력 부여량 2배 증가
   źródło: Passive_Ego.json :: dataList[id=2090611].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: This Skill Inflicts x2 [Laceration] Potency
   PL: ta Umiejętność nakłada 2 razy większą Siłę [Laceration]

## E.G.O [20907] Hex Nail (저주못) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20907`

736. [Karta E.G.O — nazwa] 저주못
   źródło: Egos.json :: dataList[id=20907].name
   limit: do 40 znaków
   EN: Hex Nail
   PL: Gwóźdź Klątwy
737. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20907].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 저주못
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=1].name ; dataList[id=2090711].levelList[level=3].name ; dataList[id=2090711].levelList[level=4].name
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 아파하는 테디
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=1].abName ; dataList[id=2090711].levelList[level=3].abName ; dataList[id=2090711].levelList[level=4].abName
   limit: do 40 znaków
   EN: Hurting Teddy Bear
   PL: Cierpiący Miś
740. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 자신과 현재 체력 비율이 가장 낮은 아군 2명의 체력을 자신의 최대 체력의 12.5%만큼 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal self and 2 other allies with the least HP percentage for 12.5% of this unit's max HP
   PL: [EndSkill] odzyskuje HP równe 12.5% Maks. HP tej jednostki dla siebie i 2 innych sojuszników z najniższym aktualnym procentem HP
741. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
742. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [NailPersonality] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict 2 [NailPersonality]
   PL: [OnSucceedAttackHead] nakłada 2 [NailPersonality]
744. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] [EndSkill] 자신과 현재 체력 비율이 가장 낮은 아군 2명의 체력을 자신의 최대 체력의 12.5%만큼 회복\n<style="highlight">- 회복받는 대상이 보유한 부정적인 효과 종류 2개당 최대 체력의 2.5%만큼 회복량이 증가 (최대 7.5%)</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal self and 2 other allies with the least HP percentage for 12.5% of this unit's max HP\n<style="highlight">- Each heal-receiving unit heals +2.5% more HP for every 2 negative effect on themselves (max 7.5)</style>
   PL: [EndSkill] odzyskuje HP równe 12.5% Maks. HP tej jednostki dla tej jednostki i 2 innych sojuszników z najniższym aktualnym procentem HP\n<style="highlight">- leczenie każdego leczonego celu rośnie o 2.5% HP za każde 2 negatywne efekty, jakie ten cel posiada (maks. 7.5)</style>
745. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Laceration]
746. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 2 [Curse]<style="highlight"></style>
   PL: [OnSucceedAttack] nakłada 2 [Curse]<style="highlight"></style>
747. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [NailPersonality] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict 2 [NailPersonality]<style="highlight"></style>
   PL: [OnSucceedAttackHead] nakłada 2 [NailPersonality]<style="highlight"></style>
748. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [EndSkill] 자신과 현재 체력 비율이 가장 낮은 아군 2명의 체력을 자신의 최대 체력의 <style="highlight">15%</style>만큼 회복\n- 회복받는 대상이 보유한 부정적인 효과 종류 <style="highlight">1</style>개당 최대 체력의 2.5%만큼 회복량이 증가 (최대 <style="highlight">10%</style>)\n<style="highlight">- 이 스킬을 포함하여 질투 공명이 4 이상이면, 회복 대상 수 +1</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal self and 2 other allies with the least HP percentage for <style="highlight">15%</style> of this unit's max HP\n- Each heal-receiving unit heals +2.5% more HP for <style="highlight">every</style> negative effect on themselves (max <style="highlight">10%</style>)\n<style="highlight">- At 4+ Envy Reson. including this Skill, heal 1 additional ally</style>
   PL: [EndSkill] odzyskuje HP równe <style="highlight">15%</style> Maks. HP tej jednostki dla siebie i 2 innych sojuszników z najniższym aktualnym procentem HP\n- leczenie każdego leczonego celu rośnie o 2.5% HP za <style="highlight">każdy 1</style> negatywny efekt, jaki ten cel posiada (maks. <style="highlight">10%</style>)\n<style="highlight">- przy Rezonansie Zawiści 4+ wliczając tę Umiejętność, liczba leczonych sojuszników +1</style>
749. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">4</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Laceration]
750. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Curse]
   PL: [OnSucceedAttack] nakłada <style="highlight">3</style> [Curse]
751. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [NailPersonality] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090711].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict <style="highlight">3</style> [NailPersonality]
   PL: [OnSucceedAttackHead] nakłada <style="highlight">3</style> [NailPersonality]
752. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 저주못
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].name ; dataList[id=2090721].levelList[level=3].name ; dataList[id=2090721].levelList[level=4].name
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 아파하는 테디
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].abName ; dataList[id=2090721].levelList[level=3].abName ; dataList[id=2090721].levelList[level=4].abName
   (powtórzenie elementu 739 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신을 제외하고 현재 체력 비율이 가장 낮은 아군 3명의 체력을 자신의 최대 체력의 15%만큼 회복
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Heal 3 other allies with the least HP percentage for 15% of this unit's max HP
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] odzyskuje HP równe 15% Maks. HP tej jednostki dla 3 innych sojuszników z najniższym aktualnym procentem HP
755. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 741 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 729 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] [NailPersonality] 2 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackTail] Inflict 2 [NailPersonality]
   PL: [OnSucceedAttackTail] nakłada 2 [NailPersonality]
759. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신을 제외하고 현재 체력 비율이 가장 낮은 아군 3명의 체력을 자신의 최대 체력의 15%만큼 회복\n<style="highlight">- 회복받는 대상이 보유한 부정적인 효과 종류 2개당 다음 턴까지 [AttackUp] 1 부여 (최대 2)</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [AttackUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Heal 3 other allies with the least HP percentage for 15% of this unit's max HP\n<style="highlight">- Each heal-receiving unit gains 1 [AttackUp] until next turn for every 2 negative effect on themselves (max 2)</style>
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] odzyskuje HP równe 15% Maks. HP tej jednostki dla 3 innych sojuszników z najniższym aktualnym procentem HP\n<style="highlight">- każdy leczony cel zyskuje 1 [AttackUp] do następnej tury za każde 2 negatywne efekty, jakie ten cel posiada (maks. 2)</style>
760. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 745 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [E.G.O — Korozja (Corrosion) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=2090721].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2<style="highlight"></style>
762. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 746 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] [NailPersonality] 2 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackTail] Inflict 2 [NailPersonality]<style="highlight"></style>
   PL: [OnSucceedAttackTail] nakłada 2 [NailPersonality]<style="highlight"></style>
764. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — opis] [CantIdentify]\n무작위 대상 공격\n[EndSkill] 자신을 제외하고 현재 체력 비율이 가장 낮은 아군 3명의 체력을 자신의 최대 체력의 <style="highlight">20%</style>만큼 회복\n- 회복받는 대상이 보유한 부정적인 효과 종류 <style="highlight">1</style>개당 다음 턴까지 [AttackUp] 1 부여 (최대 <style="highlight">3</style>)\n<style="highlight">- 이 스킬을 포함하여 질투 공명이 4 이상이면, 회복 대상 수 +1</style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantIdentify], [EndSkill], [AttackUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantIdentify]\nTargets randomly\n[EndSkill] Heal 3 other allies with the least HP percentage for <style="highlight">20%</style> of this unit's max HP\n- Each heal-receiving unit gains 1 [AttackUp] until next turn for <style="highlight">every</style> negative effect on themselves (max <style="highlight">3</style>)\n<style="highlight">- At 4+ Envy Reson. including this Skill, heal 1 additional ally</style>
   PL: [CantIdentify]\nAtakuje losowy cel\n[EndSkill] odzyskuje HP równe <style="highlight">20%</style> Maks. HP tej jednostki dla 3 innych sojuszników z najniższym aktualnym procentem HP\n- każdy leczony cel zyskuje 1 [AttackUp] do następnej tury za <style="highlight">każdy 1</style> negatywny efekt, jaki ten cel posiada (maks. <style="highlight">3</style>)\n<style="highlight">- przy Rezonansie Zawiści 4+ wliczając tę Umiejętność, liczba leczonych sojuszników +1</style>
765. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">4</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 750 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [E.G.O — Korozja (Corrosion) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] [NailPersonality] <style="highlight">3</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090721].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackTail] Inflict <style="highlight">3</style> [NailPersonality]
   PL: [OnSucceedAttackTail] nakłada <style="highlight">3</style> [NailPersonality]
768. [Pasywka E.G.O — nazwa] 가슴에 박힌 쇠말뚝
   źródło: Passive_Ego.json :: dataList[id=2090711].name
   limit: do 40 znaków
   EN: Iron Stake against the Heart
   PL: Żelazny Pal wbity w Serce
769. [Pasywka E.G.O — opis] 기본 공격 스킬을 사용하여 적에게 [Laceration] 또는 특수 출혈을 부여할 경우, [DefenseDown] 1 부여 (턴 당 1회)\n- 대상 적이 [Laceration] 또는 특수 출혈을 보유하였다면 [Laceration] 2 추가로 부여 (턴 당 1회)\n\n자신을 포함한 아군이 적에게 스킬로 직접적인 체력 피해를 받은 경우, 대상 적에게 [Curse] 1 부여 (턴 당 2회)
   źródło: Passive_Ego.json :: dataList[id=2090711].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefenseDown], [Curse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Curse] = 저주 / Curse
   EN: When inflicting [Laceration] or 'Unique Bleed' against an enemy with Base Attack Skills, inflict 1 [DefenseDown] (once per turn)\n- If the target has [Laceration] or 'Unique Bleed', inflict additional 2 [Laceration] (once per turn)\n\nIf an ally, including this unit, takes direct HP damage from the enemy, inflict 1 [Curse] against the target enemy (2 times per turn)
   PL: przy nakładaniu [Laceration] lub Szczególnego Krwawienia na wroga Podstawową Umiejętnością Ataku, nakłada 1 [DefenseDown] (1 raz na turę)\n- jeżeli cel ma [Laceration] lub Szczególne Krwawienie, dodatkowo nakłada 2 [Laceration] (1 raz na turę)\n\njeżeli sojusznik, wliczając tę jednostkę, otrzymał bezpośrednie obrażenia HP od wroga, nakłada 1 [Curse] na tego wroga (2 razy na turę)

## E.G.O [20908] Indicant's Trial (지정 재판) — Rodion
- postać: Rodion (로쟈) · ID E.G.O: `20908`

770. [Karta E.G.O — nazwa] 지정 재판
   źródło: Egos.json :: dataList[id=20908].name
   limit: do 40 znaków
   EN: Indicant's Trial
   PL: Proces Wyznaczonego
771. [Karta E.G.O — opis] 로쟈의 전용 EGO 장비
   źródło: Egos.json :: dataList[id=20908].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — nazwa] 지정 재판
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=1].name ; dataList[id=2090811].levelList[level=3].name ; dataList[id=2090811].levelList[level=4].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [E.G.O — Przebudzenie (Awakening) (ulepszenia 1,3,4) — źródło (Anomalia)] 작열공작
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=1].abName ; dataList[id=2090811].levelList[level=3].abName ; dataList[id=2090811].levelList[level=4].abName
   limit: do 40 znaków
   EN: Burning Duchess
   PL: Płonąca Księżna
774. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — opis] [EndSkill] 현재 체력 비율이 가장 낮은 아군 (1 + 최대 공명 수)명의 체력을 최대 체력의 15%만큼 회복 (최대 3명)\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Heal (1 + highest Reson.) allies with the least HP percentages for 15% of their max HP (max 3 allies)\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: [EndSkill] odzyskuje HP równe 15% Maks. HP dla (1 + najwyższy Rezonans) sojuszników z najniższym aktualnym procentem HP (maks. 3 sojuszników)\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
775. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 6 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL: [OnSucceedAttack] [Combustion] 6 Podpalenia
776. [E.G.O — Przebudzenie (Awakening) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 메인 타겟이면, 다음 턴에 [BirdCage] (1 + (분노 공명 수 / 3 ))만큼 부여 (최대 2, 소수점 버림)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BirdCage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BirdCage] = 달궈진 새장 / Searing Birdcage
   EN: [OnSucceedAttack] If this hits the main target, inflict (1 + (Wrath Reson. / 3)) [BirdCage] next turn on main target (max 2; rounded down)
   PL: [OnSucceedAttack] jeżeli to trafienie główne, następnej tury nakłada (1 + (Rezonans Gniewu / 3)) [BirdCage] na główny cel (maks. 2, zaokrąglone w dół)
777. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — opis] <style="highlight">[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 3, 소수점 버림)</style>\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 (1 + 최대 공명 수)명의 체력을 최대 체력의 <style="highlight">18</style>%만큼 회복 (최대 3명)\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">[BeforeAttack] Gain (highest Reson. / 2) Atk Weight (max 3; rounded down)</style>\n[EndSkill] Heal (1 + highest Reson.) allies with the least HP percentage for <style="highlight">18</style>% of their max HP (max 3 allies)\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: <style="highlight">[BeforeAttack] zyskuje (najwyższy Rezonans / 2) Wagi Ataku (maks. 3, zaokrąglone w dół)</style>\n[EndSkill] odzyskuje HP równe <style="highlight">18</style>% Maks. HP dla (1 + najwyższy Rezonans) sojuszników z najniższym aktualnym procentem HP (maks. 3 sojuszników)\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
778. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">8</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">8</style> [Combustion]
   PL: [OnSucceedAttack] [Combustion] <style="highlight">8</style> Podpalenia
779. [E.G.O — Przebudzenie (Awakening) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 메인 타겟이면, 다음 턴에 [BirdCage] (1 + (분노 공명 수 / 3 ))만큼 부여 (최대 <style="highlight">3</style>, 소수점 버림)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BirdCage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BirdCage] = 달궈진 새장 / Searing Birdcage
   EN: [OnSucceedAttack] If this hits the main target, inflict (1 + (Wrath Reson. / 3)) [BirdCage] next turn on main target (max <style="highlight">3</style>; rounded down)
   PL: [OnSucceedAttack] jeżeli to trafienie główne, następnej tury nakłada (1 + (Rezonans Gniewu / 3)) [BirdCage] na główny cel (maks. <style="highlight">3</style>, zaokrąglone w dół)
780. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — opis] [BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 3, 소수점 버림)\n[EndSkill] 현재 체력 비율이 가장 낮은 아군 (1 + 최대 공명 수)명의 체력을 최대 체력의 <style="highlight">20</style>%만큼 회복 (최대 3명)\n[EndSkill] 3턴 동안 턴 종료 시 정신력 10 감소
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [EndSkill]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeAttack] Gain (highest Reson. / 2) Atk Weight (max 3; rounded down)\n[EndSkill] Heal (1 + highest Reson.) allies with the least HP percentage for <style="highlight">20</style>% of their max HP (max 3 allies)\n[EndSkill] For 3 turns, lose 10 SP at Turn End
   PL: [BeforeAttack] zyskuje (najwyższy Rezonans / 2) Wagi Ataku (maks. 3, zaokrąglone w dół)\n[EndSkill] odzyskuje HP równe <style="highlight">20</style>% Maks. HP dla (1 + najwyższy Rezonans) sojuszników z najniższym aktualnym procentem HP (maks. 3 sojuszników)\n[EndSkill] przez 3 tury traci 10 SP na koniec tury
781. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 8 부여<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 8 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] [Combustion] 8 Podpalenia<style="highlight"></style>
782. [E.G.O — Przebudzenie (Awakening) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 메인 타겟이면, 다음 턴에 [BirdCage] (1 + (분노 공명 수 / 3 ))만큼 부여 (최대 3, 소수점 버림)<style="highlight"></style>
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090811].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BirdCage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BirdCage] = 달궈진 새장 / Searing Birdcage
   EN: [OnSucceedAttack] If this hits the main target, inflict (1 + (Wrath Reson. / 3)) [BirdCage] next turn on main target (max 3; rounded down)<style="highlight"></style>
   PL: [OnSucceedAttack] jeżeli to trafienie główne, następnej tury nakłada (1 + (Rezonans Gniewu / 3)) [BirdCage] na główny cel (maks. 3, zaokrąglone w dół)<style="highlight"></style>
783. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — nazwa] 지정 재판
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].name ; dataList[id=2090821].levelList[level=3].name ; dataList[id=2090821].levelList[level=4].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — źródło (Anomalia)] 작열공작
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].abName ; dataList[id=2090821].levelList[level=3].abName ; dataList[id=2090821].levelList[level=4].abName
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — opis] [CantIdentify]\n무작위 대상 공격\n[BeforeAttack] (최대 공명 수 / 2)만큼 공격 가중치 증가 (최대 3, 소수점 버림)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].desc ; dataList[id=2090821].levelList[level=3].desc ; dataList[id=2090821].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [BeforeAttack]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantIdentify]\nTargets Randomly\n[BeforeAttack] Gain (highest Reson. / 2) Atk Weight (max 3; rounded down)
   PL: [CantIdentify]\nAtakuje losowy cel\n[BeforeAttack] zyskuje (najwyższy Rezonans / 2) Wagi Ataku (maks. 3, zaokrąglone w dół)
786. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=2090821].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=2090821].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 6 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 6 [Combustion]
   PL: [UnBrokenCoinOnSucceedAttack] [Combustion] 6 Podpalenia
788. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 메인 타겟이면, [BirdCage] (1 + 분노 공명 수)만큼 부여 (최대 3)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [BirdCage]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BirdCage] = 달궈진 새장 / Searing Birdcage
   EN: [UnBrokenCoinOnSucceedAttack] If this hits the main target, inflict (1 + Wrath Reson.) [BirdCage] on main target (max 3)
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli to trafienie główne, nakłada (1 + Rezonans Gniewu) [BirdCage] na główny cel (maks. 3)
789. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=2090821].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=2090821].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [E.G.O — Korozja (Corrosion) (ulepszenia 1,3) — moneta 2, efekt 2 — opis] 메인 타겟의 [Combustion] 위력당 메인 타겟에게 가하는 피해량 +1% (최대 50%)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=2090821].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +1% damage on main target for every [Combustion] Potency on main target (max 50%)
   PL: zadaje +1% obrażeń głównemu celowi za każde 1 Siły [Combustion] głównego celu (maks. 50%)
791. [E.G.O — Korozja (Corrosion) (ulepszenie 1) — moneta 2, efekt 3 — opis] [EnemyKill] 현재 체력 비율이 가장 낮은 아군 (1 + 최대 공명 수)명에게 [CrimsonResultUp] 1, [CrimsonDamageUp] 1 부여 (최대 4명, 스킬당 1회)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [CrimsonResultUp], [CrimsonDamageUp]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [CrimsonResultUp] = 분노 위력 증가 / Wrath Power Up; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: [EnemyKill] Apply 1 [CrimsonResultUp] and 1 [CrimsonDamageUp] to (1 + highest Reson.) allies with the least HP percentages (max 4 allies; once per Skill)
   PL: [EnemyKill] nakłada 1 [CrimsonResultUp] i 1 [CrimsonDamageUp] na (1 + najwyższy Rezonans) sojuszników z najniższym aktualnym procentem HP (maks. 4 sojuszników, 1 raz na Umiejętność)
792. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] <style="highlight">8</style> 부여
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict <style="highlight">8</style> [Combustion]
   PL: [UnBrokenCoinOnSucceedAttack] [Combustion] <style="highlight">8</style> Podpalenia
793. [E.G.O — Korozja (Corrosion) (ulepszenie 3) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 메인 타겟이면, [BirdCage] (1 + 분노 공명 수)만큼 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_Ego_Personality-09.json :: dataList[id=2090821].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [BirdCage]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BirdCage] = 달궈진 새장 / Searing Birdcage
   EN: [UnBrokenCoinOnSucceedAttack] If this hits the main target, inflict (1 + Wrath Reson.) [BirdCage] on main target (max <style="highlight">4</style>)
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli to trafienie główne, nakłada (1 + Rezonans Gniewu) [BirdCage] na główny cel (maks. <style="highlight">4</style>)
