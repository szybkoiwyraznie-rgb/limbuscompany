# Paczka AI P25 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 11/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P25_2a_slowa_kluczowe_i_statusy_cz11.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P25_2a_slowa_kluczowe_i_statusy_cz11.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs-mowe
- plik gry: `Bufs-mowe.json`

1. [Status [BloodPocket_LowMorale] — opis] 턴 시작 시 취약, 피해량 증가 1 얻음
   źródło: Bufs-mowe.json :: dataList[id=BloodPocket_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Fragile and Damage Up
   PL: Na początku tury zyskuje 1 Wrażliwości i 1 Wzrost Obrażeń
2. [Status [BloodPocket_Panic] — nazwa] 흡혈 갈망
   źródło: Bufs-mowe.json :: dataList[id=BloodPocket_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BloodPocket_Panic]`
   limit: do 40 znaków
   EN: Bloodthirst
   PL: Krwiożerczość
3. [Status [BloodPocket_Panic] — opis] 턴 시작시 취약, 피해량 증가 2 얻음
   źródło: Bufs-mowe.json :: dataList[id=BloodPocket_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Fragile and Damage Up
   PL: Na początku tury zyskuje 2 Wrażliwości i 2 Wzrostu Obrażeń
4. [Status [HardenedBlood] — nazwa] 경화 혈액
   źródło: Bufs-mowe.json :: dataList[id=HardenedBlood].name
   kontekst: identyfikator statusu w tekstach: `[HardenedBlood]`
   limit: do 40 znaków
   EN: Coagulated Blood
   PL: Skrzepnięta Krew
5. [Status [HardenedBlood] — opis] 수치만큼 자신의 공격 레벨과 방어 레벨이 증가 (최대 5)
   źródło: Bufs-mowe.json :: dataList[id=HardenedBlood].desc
   limit: do 120 znaków
   EN: Gain Offense Level and Defense Level equal to the value (max 5)
   PL: Zyskuje Poziom Ataku i Poziom Obrony równy wartości (maks. 5)

## Statusy i efekty bojowe — Bufs-night-clean-up-re
- plik gry: `Bufs-night-clean-up-re.json`

6. [Status [RepressedMurderousIntendHard] — nazwa] 억눌린 살기
   źródło: Bufs-night-clean-up-re.json :: dataList[id=RepressedMurderousIntendHard].name
   kontekst: identyfikator statusu w tekstach: `[RepressedMurderousIntendHard]`
   limit: do 40 znaków
   EN: Repressed Bloodthirst
   PL: Stłumiona Krwiożerczość
7. [Status [RepressedMurderousIntendHard] — opis] 기본 공격 레벨 -5, 기본 방어 레벨 -5
   źródło: Bufs-night-clean-up-re.json :: dataList[id=RepressedMurderousIntendHard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -5\nBase Defense Level -5
   PL: Podstawowy Poziom Ataku -5\nPodstawowy Poziom Obrony -5
8. [Status [WeighedMurderousIntendHard] — nazwa] 짓눌린 살기
   źródło: Bufs-night-clean-up-re.json :: dataList[id=WeighedMurderousIntendHard].name
   kontekst: identyfikator statusu w tekstach: `[WeighedMurderousIntendHard]`
   limit: do 40 znaków
   EN: Crushed Bloodthirst
   PL: Rozgnieciona Krwiożerczość
9. [Status [WeighedMurderousIntendHard] — opis] 기본 공격 레벨 -15, 기본 방어 레벨 -15
   źródło: Bufs-night-clean-up-re.json :: dataList[id=WeighedMurderousIntendHard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -15\nBase Defense Level -15
   PL: Podstawowy Poziom Ataku -15\nPodstawowy Poziom Obrony -15

## Statusy i efekty bojowe — Bufs-pilgrimage
- plik gry: `Bufs-pilgrimage.json`

10. [Status [NetherseaBrand] — nazwa] 명흔
   źródło: Bufs-pilgrimage.json :: dataList[id=NetherseaBrand].name
   kontekst: identyfikator statusu w tekstach: `[NetherseaBrand]`
   limit: do 40 znaków
   EN: Nethersea Brand
   PL: Piętno Głębin
11. [Status [NetherseaBrand] — opis] 턴이 지날 때마다 명흔의 영향 범위가 수감자 진영으로 확산\n- 1단계 : 시테러 진영\n- 2단계 : 전방 수감자 2명\n- 3단계 : 전방 수감자 5명\n- 4단계 : 모든 수감자
   źródło: Bufs-pilgrimage.json :: dataList[id=NetherseaBrand].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nethersea Brand expands toward the Sinners with each passing turn.\n- Stage 1 : Sea Terror territory\n- Stage 2 : 2 frontmost Sinners\n- Stage 3 : 5 frontmost Sinners\n- Stage 4 : All Sinners
   PL: Z każdą turą wpływy Piętna Głębin rozszerzają się na Grzeszników.\n- 1. stopień: terytorium Sea Terror\n- 2. stopień: 2 Grzeszników z przodu\n- 3. stopień: 5 Grzeszników z przodu\n- 4. stopień: wszyscy Grzesznicy
12. [Status [NetherseaBrand] — podsumowanie] 턴이 지날 때마다 명흔 확산
   źródło: Bufs-pilgrimage.json :: dataList[id=NetherseaBrand].summary
   limit: do 120 znaków
   EN: The Nethersea Brand expands with each turn
   PL: Piętno Głębin rozszerza się z każdą turą
13. [Status [NetherseaBrandUnit] — nazwa] 명흔
   źródło: Bufs-pilgrimage.json :: dataList[id=NetherseaBrandUnit].name
   kontekst: identyfikator statusu w tekstach: `[NetherseaBrandUnit]`
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Status [NetherseaBrandUnit] — opis] - 명흔 위의 수감자가 턴 종료 시 최대 체력의 5%만큼 고정 피해를 입고 신경 손상 3 얻음\n- 명흔 위의 시테러가 수감자에게 가하는 신경 손상이 크게 증가\n- 턴이 지날 때마다 명흔의 영향 범위가 수감자 진영으로 확산\n· 1단계 : 시테러 진영\n· 2단계 : 제일 앞에 있는 수감자 2명까지 적용\n· 3단계 : 제일 앞에 있는 수감자 5명까지 적용\n· 4단계 : 모든 수감자에게 적용
   źródło: Bufs-pilgrimage.json :: dataList[id=NetherseaBrandUnit].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Sinners on top of Nethersea Brand: at Turn End, take fixed damage equal to 5% HP and gain 3 Nervous Impairment\n- Greatly increases the Nervous Impairment Stack Sea Terrors on top of Nethersea Brand inflict against Sinners\n- Nethersea Brand's influence expands toward Sinner territory with each passing turn\n· Stage 1 : Sea Terror territory\n· Stage 2 : Affects 2 frontmost Sinners\n· Stage 3 : Affects 5 frontmost Sinners\n· Stage 4 : Affects all Sinners
   PL: - Grzesznicy na Piętnie Głębin na koniec tury otrzymują obrażenia stałe równe 5% HP i zyskują 3 Uszkodzenia Nerwów\n- Sea Terror na Piętnie Głębin znacznie zwiększa nakładane na Grzeszników Uszkodzenia Nerwów\n- Z każdą turą wpływy Piętna Głębin rozszerzają się na Grzeszników\n· 1. stopień: terytorium Sea Terror\n· 2. stopień: 2 Grzeszników z przodu\n· 3. stopień: 5 Grzeszników z przodu\n· 4. stopień: wszyscy Grzesznicy
15. [Status [NetherseaBrandUnit] — podsumowanie] 명흔 위의 아군이 고정 피해와 신경 손상 얻음.\n명흔 위의 적이 아군에게 가하는 신경 손상 크게 증가
   źródło: Bufs-pilgrimage.json :: dataList[id=NetherseaBrandUnit].summary
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Allies on top of Nethersea Brand takes fixed damage and gain Nervous Impairment.\nGreatly increase the amount of Nervous Impairment inflicted against allies by enemies on top of Nethersea Brand
   PL: Sojusznicy na Piętnie Głębin otrzymują obrażenia stałe i zyskują Uszkodzenia Nerwów.\nWrogowie na Piętnie Głębin znacznie zwiększają nakładane na sojuszników Uszkodzenia Nerwów
16. [Status [SeaTerrorCell] — nazwa] 시테러 동화
   źródło: Bufs-pilgrimage.json :: dataList[id=SeaTerrorCell].name
   kontekst: identyfikator statusu w tekstach: `[SeaTerrorCell]`
   limit: do 40 znaków
   EN: Sea Terror Assimilation
   PL: Asymilacja Sea Terror
17. [Status [SeaTerrorCell] — opis] - 최댓값 : 5\n- 턴 시작 시 수치 1 증가\n- 수치 1 당 공격 레벨 감소 1, 방어 레벨 감소 1 얻음\n- 턴 종료시 아군 수감자의 버프 수치가 5면 전장 이탈.\n- 아군 수감자가 버프 보유시, 수비 스킬을 장착하고 전투를 시작하면, 턴 종료시 전장 이탈
   źródło: Bufs-pilgrimage.json :: dataList[id=SeaTerrorCell].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack : 5\n- Gain 1 Stack at Turn Start\n- Gain 1 Offense Level Down and 1 Defense Level Down per Stack\n- Turn End: if an allied Sinner has 5 Stacks of this effect, it Escapes Battlefield.\n- When an allied Sinner has a Defense Skill equipped while it has this effect, they Escape Battlefield at Combat Start
   PL: - Maks. stosów: 5\n- Na początku tury rośnie o 1\n- Zyskuje 1 Spadek Poziomu Ataku i 1 Spadek Poziomu Obrony za każdy stos\n- Na koniec tury, jeżeli sojuszniczy Grzesznik ma 5 stosów, opuszcza pole bitwy.\n- Jeżeli sojuszniczy Grzesznik ma ten efekt i rozpoczął walkę z wyposażoną Umiejętnością obrony, opuszcza pole bitwy na koniec tury
18. [Status [SeaTerrorCell] — podsumowanie] 수치에 비례하여 공격 레벨 감소, 방어 레벨 감소 얻음
   źródło: Bufs-pilgrimage.json :: dataList[id=SeaTerrorCell].summary
   limit: do 120 znaków
   EN: Gains Offense Level Down and Defense Level Down based on the Stack
   PL: Zyskuje Spadek Poziomu Ataku i Spadek Poziomu Obrony zależnie od stosów
19. [Status [NervousImpairment] — nazwa] 신경 손상
   źródło: Bufs-pilgrimage.json :: dataList[id=NervousImpairment].name
   kontekst: identyfikator statusu w tekstach: `[NervousImpairment]`
   limit: do 40 znaków
   EN: Nervous Impairment
   PL: Uszkodzenie Nerwów
20. [Status [NervousImpairment] — opis] - 최댓값 : 30\n- 수치가 30이면, 흐트러진 다음 최대 체력의 25%만큼 고정 피해를 입고 이 효과 제거
   źródło: Bufs-pilgrimage.json :: dataList[id=NervousImpairment].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack : 30\n- At 30 Stack, become Staggered; then, take fixed damage equal to 25% of this unit's max HP, and remove this effect
   PL: - Maks. stosów: 30\n- Przy 30 stosach zostaje oszołomiony, a następnie otrzymuje obrażenia stałe równe 25% HP i traci ten efekt
21. [Status [NervousImpairment] — podsumowanie] 흐트러지고 큰 체력 피해를 입음
   źródło: Bufs-pilgrimage.json :: dataList[id=NervousImpairment].summary
   limit: do 120 znaków
   EN: Become Staggered and take significant HP damage
   PL: Zostaje oszołomiony i otrzymuje znaczne obrażenia HP
22. [Status [WaitingforCommandMod] — nazwa] 명령 대기
   źródło: Bufs-pilgrimage.json :: dataList[id=WaitingforCommandMod].name
   kontekst: identyfikator statusu w tekstach: `[WaitingforCommandMod]`
   limit: do 40 znaków
   EN: Standby State
   PL: Stan Oczekiwania
23. [Status [WaitingforCommandMod] — opis] - 명령 대기 상태에서는 피해를 입기 전까지 공격 스킬을 사용하지 않음
   źródło: Bufs-pilgrimage.json :: dataList[id=WaitingforCommandMod].desc
   limit: do 120 znaków
   EN: - When in Standby State, this unit does not use Attack Skills until it takes damage
   PL: - W stanie Oczekiwania jednostka nie używa Umiejętności ataku, dopóki nie otrzyma obrażeń
24. [Status [WaitingforCommandMod] — podsumowanie] 명령 대기 상태에서는 피해를 입기 전까지 공격 스킬을 사용하지 않음
   źródło: Bufs-pilgrimage.json :: dataList[id=WaitingforCommandMod].summary
   limit: do 120 znaków
   EN: When in Standby State, this unit does not use Attack Skills until it takes damage
   PL: W stanie Oczekiwania jednostka nie używa Umiejętności ataku, dopóki nie otrzyma obrażeń
25. [Status [ParticipationMod] — nazwa] 참전
   źródło: Bufs-pilgrimage.json :: dataList[id=ParticipationMod].name
   kontekst: identyfikator statusu w tekstach: `[ParticipationMod]`
   limit: do 40 znaków
   EN: Combat-Ready State
   PL: Stan Bojowy
26. [Status [ParticipationMod] — opis] - 피해를 받아 공격 스킬을 사용하는 상태로 돌입\n- 참전 상태에서 턴 시작 시,\n· 모든 적에게 신경 손상 3 부여\n· 속도 최솟값, 최댓값 3 증가\n· 잃은 체력 10%당 공격 레벨 증가 1 얻음 (최대 8)\n- 참전 상태에서 턴 종료 시, 최대 체력의 10%만큼 고정 체력 피해를 입음
   źródło: Bufs-pilgrimage.json :: dataList[id=ParticipationMod].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - After taking damage, this unit has begun to use its Attack Skills.\n- Turn Start while in Combat-Ready State:\n· Inflict 3 Nervous Impairment to all enemies\n· Min & Max Speed +3\n· Gain 1 Offense Level Up for every 10% missing HP (max 8)\n- Turn End while in Combat-Ready State: take fixed damage equal to 10% HP
   PL: - Po otrzymaniu obrażeń jednostka przystępuje do używania Umiejętności ataku.\n- Na początku tury w stanie Bojowym:\n· Nakłada 3 Uszkodzenia Nerwów wszystkim wrogom\n· Min. i Maks. Szybkość +3\n· Zyskuje 1 Wzrost Poziomu Ataku za każde 10% brakującego HP (maks. 8)\n- Na koniec tury w stanie Bojowym otrzymuje obrażenia stałe równe 10% HP
27. [Status [ParticipationMod] — podsumowanie] 피해를 받아 공격 스킬을 사용하는 상태로 돌입
   źródło: Bufs-pilgrimage.json :: dataList[id=ParticipationMod].summary
   limit: do 120 znaków
   EN: After taking damage, this unit begins to use its Attack Skills
   PL: Po otrzymaniu obrażeń jednostka przystępuje do używania Umiejętności ataku
28. [Status [AbyssalVitality] — nazwa] 깊은 바다의 생명력
   źródło: Bufs-pilgrimage.json :: dataList[id=AbyssalVitality].name
   kontekst: identyfikator statusu w tekstach: `[AbyssalVitality]`
   limit: do 40 znaków
   EN: Abyssal Vitality
   PL: Witalność Otchłani
29. [Status [AbyssalVitality] — opis] - 최댓값 : 100\n- 특정 스킬 사용 시 소모됨\n- 소모될 때마다 그 수치만큼 자신의 정신력 회복
   źródło: Bufs-pilgrimage.json :: dataList[id=AbyssalVitality].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack : 100\n- Consumed when using certain Skills\n- Every time this effect is consumed, Heal SP on self by the amount consumed
   PL: - Maks. stosów: 100\n- Zużywana przy użyciu określonych Umiejętności\n- Za każdym razem, gdy jest zużywana, odzyskuje Poczytalność równą zużytej liczbie
30. [Status [AbyssalVitality] — podsumowanie] 특정 스킬 사용 시 소모\n- 소모될 때마다 정신력 회복
   źródło: Bufs-pilgrimage.json :: dataList[id=AbyssalVitality].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Consumed when using certain Skills\n- Every time this effect is consumed, Heal SP
   PL: Zużywana przy użyciu określonych Umiejętności\n- Za każdym zużyciem odzyskuje Poczytalność
31. [Status [IndelibleGoodwill] — nazwa] 지워지지 않을 선의
   źródło: Bufs-pilgrimage.json :: dataList[id=IndelibleGoodwill].name
   kontekst: identyfikator statusu w tekstach: `[IndelibleGoodwill]`
   limit: do 40 znaków
   EN: Indelible Compassion
   PL: Niewymazywalne Współczucie
32. [Status [IndelibleGoodwill] — opis] - 턴 종료 시 보호막이 사라지지 않음 (피해, 효과로 사라지는 경우는 제외)\n- 보호막이 피격을 받아 파괴되면, 흐트러지고 다음 턴까지 취약 5 얻음\n- 흐트러짐 손상으로 흐트러지면, 다음 턴까지 취약 5 얻음\n- 이 버프 효과로 얻는 취약은 중첩되지 않음\n- 보호막 수치는 중첩 가능하며, 이 효과가 적용 중인 경우에는 보호막의 수치가 보호막 적용 대상의 최대 체력 50%를 넘을 수 없음\n- 이 효과는 보호막 관리 효과로 취급됨 (다른 보호막 관리 효과 적용 시, 교체됨)
   źródło: Bufs-pilgrimage.json :: dataList[id=IndelibleGoodwill].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This unit does not lose Shield at Turn End (unless removed by damage or certain effects)\n- When the Shield breaks due to getting hit, become Staggered and gain 5 Fragile until next turn\n- When becoming Staggered due to raised Stagger threshold, gain 5 Fragile until next turn\n- Fragile gained due to this buff's effects do not stack\n- Shield HP can stack, however; when this effect is active, the shield HP cannot be more than 50% of the Shielded unit's max HP\n- This effect counts as a 'Shield Management' effect. (replaced when gaining a different Shield Management effect)
   PL: - Na koniec tury Tarcza nie znika (chyba że zniknęła od obrażeń lub efektów)\n- Gdy Tarcza pęknie od trafienia, zostaje oszołomiona i zyskuje 5 Wrażliwości do następnej tury\n- Gdy zostaje oszołomiona przez podniesiony Próg Oszołomienia, zyskuje 5 Wrażliwości do następnej tury\n- Wrażliwości zdobyte dzięki temu buffowi się nie kumulują\n- HP Tarczy może się kumulować; podczas tego efektu HP Tarczy nie może przekraczać 50% Maks. HP chronionej jednostki\n- Ten efekt liczy się jako „Zarządzanie Tarczą” (zastępowany przy zdobyciu innego efektu Zarządzania Tarczą)
33. [Status [IndelibleGoodwill] — podsumowanie] 턴 종료 시 보호막이 사라지지 않음\n보호막이 파괴되면 크게 약해짐
   źródło: Bufs-pilgrimage.json :: dataList[id=IndelibleGoodwill].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Does not lose Shield at Turn End\nWhen the Shield breaks, become very fragile
   PL: Na koniec tury Tarcza nie znika\nGdy Tarcza pęknie, jednostka staje się bardzo podatna
34. [Status [ColdAirDOQ] — nazwa] 냉기
   źródło: Bufs-pilgrimage.json :: dataList[id=ColdAirDOQ].name
   kontekst: identyfikator statusu w tekstach: `[ColdAirDOQ]`
   limit: do 40 znaków
   EN: Cold
   PL: Chłód
35. [Status [ColdAirDOQ] — opis] - 최댓값 : 3\n- 냉기 1당, 속도 1 감소\n- 스킬 종료 시 수치가 3이면, 우울 피해 20과 정신력 피해 20을 받고, 이번 턴과 다음 턴에 빙결 1 얻음 모든 효과 발동 후 냉기 소멸\n- 턴 종료 시 이번 턴에 마지막 기사를 공격하지 않았으면, 소멸
   źródło: Bufs-pilgrimage.json :: dataList[id=ColdAirDOQ].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Lose 1 Speed for every Cold Stack\n- If this unit has 3 Stacks after Skill End: take 20 Gloom damage and 20 SP damage; then, gain 1 Frozen this turn and next turn.\n- Cold Stack expires after all effects are activated\n- Turn End: if this unit did not attack The Last Knight, expires
   PL: - Maks. stosów: 3\n- Traci 1 Szybkości za każdy stos Chłodu\n- Jeżeli na koniec Umiejętności ma 3 stosy: otrzymuje 20 obrażeń Posępności i 20 obrażeń Poczytalności, a w tej i następnej turze zyskuje 1 Zamarznięcia\n- Chłód znika po wywołaniu wszystkich efektów\n- Na koniec tury znika, jeżeli w tej turze nie zaatakował Ostatniego Rycerza
36. [Status [FreezingDOQ] — nazwa] 빙결
   źródło: Bufs-pilgrimage.json :: dataList[id=FreezingDOQ].name
   kontekst: identyfikator statusu w tekstach: `[FreezingDOQ]`
   limit: do 40 znaków
   EN: Frozen
   PL: Zamarznięcie
37. [Status [FreezingDOQ] — opis] - 특수 냉기\n- 이번 턴동안 행동할 수 없음\n- 체력이 1이 될 시 일부 스킬 발동을 무효화함
   źródło: Bufs-pilgrimage.json :: dataList[id=FreezingDOQ].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Cold\n- Cannot act for this turn\n- Certain Skill activations become nullified at 1 HP
   PL: - Specjalny Chłód\n- Nie może działać w tej turze\n- Przy HP 1 wybrane aktywacje Umiejętności są unieważniane
38. [Status [BloodborneDOQ] — nazwa] 기사의 피와 뼈
   źródło: Bufs-pilgrimage.json :: dataList[id=BloodborneDOQ].name
   kontekst: identyfikator statusu w tekstach: `[BloodborneDOQ]`
   limit: do 40 znaków
   EN: The Knight's Corpus
   PL: Ciało Rycerza
39. [Status [BloodborneDOQ] — opis] 받는 피해량 +80%
   źródło: Bufs-pilgrimage.json :: dataList[id=BloodborneDOQ].desc
   limit: do 120 znaków
   EN: Take +80% damage
   PL: Otrzymuje +80% obrażeń
40. [Status [WeakenDOQ] — nazwa] 재난과 시련
   źródło: Bufs-pilgrimage.json :: dataList[id=WeakenDOQ].name
   kontekst: identyfikator statusu w tekstach: `[WeakenDOQ]`
   limit: do 40 znaków
   EN: Misery and Calamity
   PL: Nędza i Klęska
41. [Status [WeakenDOQ] — opis] - 공격 레벨 ?? 감소\n- 방어 레벨 ?? 감소
   źródło: Bufs-pilgrimage.json :: dataList[id=WeakenDOQ].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -??\n- Defense Level -??
   PL: - Poziom Ataku -??\n- Poziom Obrony -??
42. [Status [DOQ_LowMorale] — nazwa] 군체 의식
   źródło: Bufs-pilgrimage.json :: dataList[id=DOQ_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DOQ_LowMorale]`
   limit: do 40 znaków
   EN: Hive Mind
   PL: Świadomość Roju
43. [Status [DOQ_LowMorale] — opis] 모든 내성이 보통 상태가 됨
   źródło: Bufs-pilgrimage.json :: dataList[id=DOQ_LowMorale].desc
   limit: do 120 znaków
   EN: All Resistances change to 'Normal'
   PL: Wszystkie odporności zmieniają się na Zwykłą
44. [Status [DOQ_LowMorale] — podsumowanie] 모든 내성이 보통 상태가 됨
   źródło: Bufs-pilgrimage.json :: dataList[id=DOQ_LowMorale].summary
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Status [DOQ_Panic] — nazwa] 군체 의식
   źródło: Bufs-pilgrimage.json :: dataList[id=DOQ_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DOQ_Panic]`
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Status [DOQ_Panic] — opis] 모든 내성이 보통 상태가 됨\n스킬로 받는 화상, 출혈, 진동, 파열의 위력을 2배로 받음
   źródło: Bufs-pilgrimage.json :: dataList[id=DOQ_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All Resistances change to 'Normal'\nDouble the amount of Burn, Bleed, Tremor, and Rupture Potency gained due to Skill effects
   PL: Wszystkie odporności zmieniają się na Zwykłą\nPodwaja Siłę Podpalenia, Krwawienia, Wstrząsu i Rozdarcia otrzymywaną przez Umiejętności
47. [Status [DOQ_Panic] — podsumowanie] 모든 내성이 보통 상태가 됨\n스킬로 받는 화상, 출혈, 진동, 파열의 위력을 2배로 받음
   źródło: Bufs-pilgrimage.json :: dataList[id=DOQ_Panic].summary
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Status [CallOfSea_LowMorale] — nazwa] 동족의 부름
   źródło: Bufs-pilgrimage.json :: dataList[id=CallOfSea_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[CallOfSea_LowMorale]`
   limit: do 40 znaków
   EN: Call of the Bloodkin
   PL: Wołanie Pokrewnych
49. [Status [CallOfSea_LowMorale] — opis] 턴 종료시 자신의 체력을 최대 체력의 3% 소모하여 자신을 포함한 모든 아군에게 다음 턴에 공격 위력 증가 1, 취약 1 부여
   źródło: Bufs-pilgrimage.json :: dataList[id=CallOfSea_LowMorale].desc
   limit: do 150 znaków
   EN: Turn End: consume 3% HP to apply 1 Attack Power Up and 1 Fragile to all allies, including this unit, next turn
   PL: Na koniec tury zużywa 3% HP, by nakładać na wszystkich sojuszników, łącznie z sobą, 1 Wzrost Mocy Ataku i 1 Wrażliwości w następnej turze
50. [Status [CallOfSea_LowMorale] — podsumowanie] 체력을 소모하여 아군에게 공격 위력 증가, 취약 부여
   źródło: Bufs-pilgrimage.json :: dataList[id=CallOfSea_LowMorale].summary
   limit: do 120 znaków
   EN: Consume HP to apply Attack Power Up and Fragile to allies
   PL: Zużywa HP, by nakładać na sojuszników Wzrost Mocy Ataku i Wrażliwość
51. [Status [CallOfSea_Panic] — nazwa] 동족의 부름
   źródło: Bufs-pilgrimage.json :: dataList[id=CallOfSea_Panic].name
   kontekst: identyfikator statusu w tekstach: `[CallOfSea_Panic]`
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Status [CallOfSea_Panic] — opis] 턴 종료시 자신의 체력을 최대 체력의 5% 소모하여 취약 1을 얻고 자신을 포함한 모든 아군에게 다음 턴에 공격 위력 증가 1, 취약 1 부여
   źródło: Bufs-pilgrimage.json :: dataList[id=CallOfSea_Panic].desc
   limit: do 170 znaków
   EN: Turn End: consume 5% HP and gain 1 Fragile to apply 1 Attack Power Up and 1 Fragile to all allies, including this unit, next turn
   PL: Na koniec tury zużywa 5% HP i zyskuje 1 Wrażliwości, by nakładać na wszystkich sojuszników, łącznie z sobą, 1 Wzrost Mocy Ataku i 1 Wrażliwości w następnej turze
53. [Status [CallOfSea_Panic] — podsumowanie] 체력을 소모하여 아군에게 공격 위력 증가, 취약 부여
   źródło: Bufs-pilgrimage.json :: dataList[id=CallOfSea_Panic].summary
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Status [BitOfEmotion] — nazwa] 감정 공유
   źródło: Bufs-pilgrimage.json :: dataList[id=BitOfEmotion].name
   kontekst: identyfikator statusu w tekstach: `[BitOfEmotion]`
   limit: do 40 znaków
   EN: Emotional Connection
   PL: Więź Emocjonalna
55. [Status [BitOfEmotion] — opis] - 적에게 공격 적중 시, (50/스킬의 코인 수)% 확률로 사용한 스킬 속성의 E.G.O 자원 1개 얻음\n- 아군의 스킬 공격 종료 시 적이 사망했다면, 가장 적게 보유한 무작위 E.G.O 자원 2개 얻음\n- 이번 전투에서 다음 E.G.O 스킬 사용 시, 소모한 자원을 종류 별로 1개씩 획득 (오버클록 시, 2개씩 획득)\n· 영작오 홍루\n· 명령 : 용해 파우스트\n· 눈부시지 않은 영광 그레고르\n· 파도의 만가 이스마엘
   źródło: Bufs-pilgrimage.json :: dataList[id=BitOfEmotion].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Hit against enemies: (50 / # of Coins)% chance to gain 1 E.G.O resource corresponding to the used Skill's Affinity\n- When an enemy dies after an allied unit's Skill attack ends, gain 2 least-owned E.G.O Resources\n- In an Encounter, gain 1 E.G.O resource of each Affinity consumed when using the following E.G.O Skills (2 of each when using Overclocked Skills)\n· To Remain Oneself Hong Lu\n· Command : Meltdown Faust\n· Unbrilliant Glory Gregor\n· Tidal Elegy Ishmael
   PL: - Przy trafieniu wrogów: (50 / liczba Monet Umiejętności)% szans na 1 Zasób E.G.O Grzechu użytej Umiejętności\n- Gdy po zakończeniu ataku Umiejętnością sojusznika ginie wrog, zyskuje 2 najmniej posiadanych Zasobów E.G.O\n- W tej walce przy użyciu następujących Umiejętności E.G.O odzyskuje po 1 Zasobie E.G.O każdego zużytego Grzechu (2 sztuki przy Przeciążeniu)\n· Pozostać Sobą Hong Lu\n· Rozkaz : Roztopienie Faust\n· Nieolśniewająca Chwała Gregor\n· Elegia Fal Ishmael
56. [Status [BitOfEmotion] — podsumowanie] 공격이 적중하거나 적 사망 시, E.G.O 자원 얻음\n특정 E.G.O 스킬 사용 시, E.G.O 자원 얻음
   źródło: Bufs-pilgrimage.json :: dataList[id=BitOfEmotion].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Hit, or on enemyt death, gain E.G.O Resources\nWhen using certain E.G.O Skills, gain E.G.O Resources
   PL: Przy trafieniu lub śmierci wroga zyskuje Zasoby E.G.O\nPrzy użyciu określonych Umiejętności E.G.O zyskuje Zasoby E.G.O
57. [Status [WildernessSurvivalModule] — nazwa] 조력자 - 야외 생존 유닛
   źródło: Bufs-pilgrimage.json :: dataList[id=WildernessSurvivalModule].name
   kontekst: identyfikator statusu w tekstach: `[WildernessSurvivalModule]`
   limit: do 60 znaków
   EN: Little Handy - Wilderness Survival Module
   PL: Little Handy - Moduł Przetrwania w Terenie
58. [Status [WildernessSurvivalModule] — opis] - 최대 체력이 20% 증가하고 스킬, 패시브, 버프 효과로 회복하는 체력 회복량이 40%만큼 증가
   źródło: Bufs-pilgrimage.json :: dataList[id=WildernessSurvivalModule].desc
   limit: do 120 znaków
   EN: - Max HP +20%. Heal +40% more from Skills, Passives, and buff effects
   PL: - Maks. HP +20%. Leczy +40% więcej przez Umiejętności, pasywne i efekty buffów
59. [Status [WildernessSurvivalModule] — podsumowanie] 최대 체력과 체력 회복량이 증가
   źródło: Bufs-pilgrimage.json :: dataList[id=WildernessSurvivalModule].summary
   limit: do 120 znaków
   EN: Gain max HP and heal more
   PL: Zwiększa Maks. HP i ilość leczenia
60. [Status [HousekeepingAssistantModule] — nazwa] 조력자 - 가사 보조 모듈
   źródło: Bufs-pilgrimage.json :: dataList[id=HousekeepingAssistantModule].name
   kontekst: identyfikator statusu w tekstach: `[HousekeepingAssistantModule]`
   limit: do 60 znaków
   EN: Little Handy - Housekeeping Assistant Module
   PL: Little Handy - Moduł Pomocy Gospodarczej
61. [Status [HousekeepingAssistantModule] — opis] - 성도의 손 사용 시, 다음 턴에 1회 추가로 발동\n- 턴 시작 시, 이번 전투 동안 성도의 손으로 명흔을 제거한 횟수만큼 공격 레벨 증가, 방어 레벨 증가 얻음 (각각 최대 4)
   źródło: Bufs-pilgrimage.json :: dataList[id=HousekeepingAssistantModule].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When activating the Hand of the Saint, it activates again once next turn\n- Turn Start: gain Offense Level Up and Defense Level Up equal to the number of times Nethersea Brand was removed by using the Hand of the Saint during this Encounter (max 4 each)
   PL: - Przy aktywacji Ręki Świętego aktywuje się ponownie raz w następnej turze\n- Na początku tury zyskuje Wzrost Poziomu Ataku i Wzrost Poziomu Obrony równy liczbie usunięć Piętna Głębin przez Rękę Świętego w tej walce (każdy maks. 4)
62. [Status [HousekeepingAssistantModule] — podsumowanie] 성도의 손 사용 시, 다음 턴에 1회 추가 발동\n명흔 제거한 횟수만큼 공격 레벨 증가, 방어 레벨 증가 얻음
   źródło: Bufs-pilgrimage.json :: dataList[id=HousekeepingAssistantModule].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When activating the Hand of the Saint, it activates again once next turn\nTurn Start: gain Offense Level Up and Defense Level Up equal to the number of times Nethersea Brand was removed
   PL: Przy aktywacji Ręki Świętego aktywuje się ponownie raz w następnej turze\nZyskuje Wzrost Poziomu Ataku i Wzrost Poziomu Obrony równy liczbie usunięć Piętna Głębin
63. [Status [IncrementalMotionFirmware] — nazwa] 조력자 - 운동 증량 펌웨어
   źródło: Bufs-pilgrimage.json :: dataList[id=IncrementalMotionFirmware].name
   kontekst: identyfikator statusu w tekstach: `[IncrementalMotionFirmware]`
   limit: do 60 znaków
   EN: Little Handy - Incremental Motion Firmware
   PL: Little Handy - Firmware Przyrostowego Ruchu
64. [Status [IncrementalMotionFirmware] — opis] - 모든 아군의 제일 앞에 있는 흐트러짐 선을 하나 제거\n- 흐트러질 경우, 1회에 한하여 다음 턴 시작 시 흐트러짐 상태에서 즉시 해제
   źródło: Bufs-pilgrimage.json :: dataList[id=IncrementalMotionFirmware].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Remove 1 highest Stagger threshold from every allied unit\n- When Staggered, immediately recover from Stagger at the start of the next turn (once)
   PL: - Usuwa 1 najwyższy Próg Oszołomienia z każdej jednostki sojusznika\n- Przy Oszołomieniu natychmiast wychodzi z Oszołomienia na początku następnej tury (1 raz)
65. [Status [IncrementalMotionFirmware] — podsumowanie] 흐트러짐 선 하나 제거\n흐트러질 시, 다음 턴에 흐트러짐 상태에서 즉시 해제
   źródło: Bufs-pilgrimage.json :: dataList[id=IncrementalMotionFirmware].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Remove one Stagger Threshold\nWhen Staggered, immediately recover next turn
   PL: Usuwa jeden Próg Oszołomienia\nPrzy Oszołomieniu natychmiast wychodzi z Oszołomienia w następnej turze
66. [Status [MiniDecontaminationKit] — nazwa] 조력자 - 얼룩 제거 세트
   źródło: Bufs-pilgrimage.json :: dataList[id=MiniDecontaminationKit].name
   kontekst: identyfikator statusu w tekstach: `[MiniDecontaminationKit]`
   limit: do 60 znaków
   EN: Little Handy - Mini Decontamination Kit
   PL: Little Handy - Mini Zestaw Odkażający
67. [Status [MiniDecontaminationKit] — opis] - 명흔이 아군에게 더 이상 피해를 입히지 않고 신경 손상을 부여하지 않음
   źródło: Bufs-pilgrimage.json :: dataList[id=MiniDecontaminationKit].desc
   limit: do 120 znaków
   EN: - Nethersea Brand no longer inflicts Nervous Impairment or deals damage to allies
   PL: - Piętno Głębin nie zadaje już sojusznikom obrażeń ani nie nakłada Uszkodzeń Nerwów
68. [Status [MiniDecontaminationKit] — podsumowanie] 명흔이 아군에게 더 이상 피해를 입히지 않고 신경 손상을 부여하지 않음
   źródło: Bufs-pilgrimage.json :: dataList[id=MiniDecontaminationKit].summary
   limit: do 120 znaków
   EN: Nethersea Brand no longer inflicts Nervous Impairment or deals damage to allies
   PL: Piętno Głębin nie zadaje już sojusznikom obrażeń ani nie nakłada Uszkodzeń Nerwów
69. [Status [ExternalUpgradeModule] — nazwa] 조력자 - 외장 강화 장치
   źródło: Bufs-pilgrimage.json :: dataList[id=ExternalUpgradeModule].name
   kontekst: identyfikator statusu w tekstach: `[ExternalUpgradeModule]`
   limit: do 60 znaków
   EN: Little Handy - External Upgrade Module
   PL: Little Handy - Moduł Zewnętrznych Ulepszeń
70. [Status [ExternalUpgradeModule] — opis] - 효과 획득 이후 3턴 동안 턴 시작 시 위력 증가 2, 피해량 증가 2 얻음 (대기 해제된 인격은 대기 해제된 턴부터 적용)
   źródło: Bufs-pilgrimage.json :: dataList[id=ExternalUpgradeModule].desc
   limit: do 210 znaków
   EN: - For 3 turns after gaining this effect: gain 2 Power Up and 2 Damage Up at the start of each turn (Substituting units earn it in the turn they Substitute in)
   PL: - Przez 3 tury po zdobyciu tego efektu zyskuje na początku każdej tury 2 Wzrost Mocy i 2 Wzrost Obrażeń (jednostki wchodzące z Rezerwy zyskują od tury wejścia)
71. [Status [ExternalUpgradeModule] — podsumowanie] 효과 획득 후 3턴 동안 위력 증가, 피해량 증가 얻음
   źródło: Bufs-pilgrimage.json :: dataList[id=ExternalUpgradeModule].summary
   limit: do 120 znaków
   EN: For 3 turns after gaining this effect: gain Power Up and Damage Up
   PL: Przez 3 tury po zdobyciu efektu zyskuje Wzrost Mocy i Wzrost Obrażeń
72. [Status [DesireToSave_LowMorale] — nazwa] 선의의 마음
   źródło: Bufs-pilgrimage.json :: dataList[id=DesireToSave_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DesireToSave_LowMorale]`
   limit: do 40 znaków
   EN: Heart of Compassion
   PL: Serce Współczucia
73. [Status [DesireToSave_LowMorale] — opis] - 가하는 피해량이 (대상이 보유한 신경 손상/2)%만큼 증가 (최대 15%)\n턴 시작 시, 피해량 증가 1, 취약 2 얻음
   źródło: Bufs-pilgrimage.json :: dataList[id=DesireToSave_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +(Nervous Impairment on target / 2)% damage (max 15%)\n- Turn Start: gain 1 Damage Up and 2 Fragile
   PL: - Zadaje +(Uszkodzenia Nerwów celu / 2)% obrażeń (maks. 15%)\nNa początku tury zyskuje 1 Wzrost Obrażeń i 2 Wrażliwości
74. [Status [DesireToSave_LowMorale] — podsumowanie] 대상의 신경 손상에 비례하여 피해량 증가
   źródło: Bufs-pilgrimage.json :: dataList[id=DesireToSave_LowMorale].summary
   limit: do 120 znaków
   EN: Deal more damage based on Nervous Impairment on target
   PL: Zadaje więcej obrażeń zależnie od Uszkodzeń Nerwów celu
75. [Status [DesireToSave_Panic] — nazwa] 선의의 마음
   źródło: Bufs-pilgrimage.json :: dataList[id=DesireToSave_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DesireToSave_Panic]`
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Status [DesireToSave_Panic] — opis] - 가하는 피해량이 (대상이 보유한 신경 손상)%만큼 증가 (최대 30%)\n- 턴 시작 시, 피해량 증가 2, 취약 3 얻음
   źródło: Bufs-pilgrimage.json :: dataList[id=DesireToSave_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +(Nervous Impairment on target)% damage (max 30%)\n- Turn Start: gain 2 Damage Up and 3 Fragile
   PL: - Zadaje +(Uszkodzenia Nerwów celu)% obrażeń (maks. 30%)\n- Na początku tury zyskuje 2 Wzrostu Obrażeń i 3 Wrażliwości
77. [Status [DesireToSave_Panic] — podsumowanie] 대상의 신경 손상에 비례하여 피해량 증가
   źródło: Bufs-pilgrimage.json :: dataList[id=DesireToSave_Panic].summary
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs-schema
- plik gry: `Bufs-schema.json`

78. [Status [BlackCloudBladeEnemy] — nazwa] 흑운도
   źródło: Bufs-schema.json :: dataList[id=BlackCloudBladeEnemy].name
   kontekst: identyfikator statusu w tekstach: `[BlackCloudBladeEnemy]`
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL: Ostrze Czarnej Chmury
79. [Status [BlackCloudBladeEnemy] — opis] - 최댓값 : 1\n- 참격 위력 1 증가\n- 참격 스킬로 공격 적중시 출혈 1 부여
   źródło: Bufs-schema.json :: dataList[id=BlackCloudBladeEnemy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Slash Power +1\n- On Hit using Slash Skills, inflict 1 Bleed
   PL: - Maks. stosów: 1\n- Siła Cięcia +1\n- Przy trafieniu Umiejętnościami Cięcia nakłada 1 Krwawienie
80. [Status [EngageToBattleEnemy] — nazwa] 임전
   źródło: Bufs-schema.json :: dataList[id=EngageToBattleEnemy].name
   kontekst: identyfikator statusu w tekstach: `[EngageToBattleEnemy]`
   limit: do 40 znaków
   EN: Battle Ready
   PL: Gotowość Bojowa
81. [Status [EngageToBattleEnemy] — opis] - 최댓값 : 1\n- 자신의 스킬, 코인 효과로 출혈 위력, 횟수를 부여할 때 부여하는 값 +1\n- 이번 전투 동안 참격 위력 증가 1, 참격 피해량 증가 3 얻음
   źródło: Bufs-schema.json :: dataList[id=EngageToBattleEnemy].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Bleed Potency and Count inflicted using this unit's Skill or Coin effects: +1\n- Gain 1 Slash Power Up and 3 Slash DMG Up for the duration of this Encounter
   PL: - Maks. stosów: 1\n- Siła i Licznik Krwawienia nakładane efektami Umiejętności lub Monet: +1\n- Na czas tej walki zyskuje 1 Wzrost Mocy Cięcia i 3 Wzrost Obrażeń Cięcia
82. [Status [SharpSensibility] — nazwa] 칼질의 재미
   źródło: Bufs-schema.json :: dataList[id=SharpSensibility].name
   kontekst: identyfikator statusu w tekstach: `[SharpSensibility]`
   limit: do 40 znaków
   EN: Delightful Swordbutchery
   PL: Rozkosz Rzeźbienia Ostrzem
83. [Status [SharpSensibility] — opis] - 최댓값 : 100\n- 스킬 슬롯에 ‘발도 자세’가 장착된 상태에서 자신의 스킬 코인 적중 시, 10 얻음 (스킬당 1회)\n- 특정 스킬에서 소모됨
   źródło: Bufs-schema.json :: dataList[id=SharpSensibility].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- On Hit using Skill Coins while "Battō Shisei" is equipped on Skill Slot, gain 10 Stacks (once per Skill)\n- Consumed by certain Skills
   PL: - Maks. stosów: 100\n- Przy trafieniu Monetami Umiejętności, gdy „Battō Shisei” jest wyposażone w slot, zyskuje 10 stosów (1 raz na Umiejętność)\n- Zużywana przez określone Umiejętności
84. [Status [SharpSensibility] — tekst klimatyczny] ‘검에 집중하고 검을 뽑고 누군가가 쓰러지고. 이렇게 삶과 죽음이 교차하는 검 놀이가 제일 재밌단 말이지.’
   źródło: Bufs-schema.json :: dataList[id=SharpSensibility].flavor
   limit: do 330 znaków
   EN: 'The mind settles on the hilt grasped within my palms, then the blade leaps outta its sheath. Blink, and somebody's already hittin' the floor. Swords go <i>clang</i>, and crossroads of life and death flash before our eyes... There ain't no better game than that.'
   PL: „Umysł skupia się na trzonie w dłoni, ostrze wyskakuje z pochwy. Mgnienie oka — i ktoś już leży na deskach. Miecze brzęczą, a przed oczami przebiega granica życia i śmierci... Nie ma lepszej zabawy.”
85. [Status [InkwashShadow_LowMorale] — nazwa] 안하무인
   źródło: Bufs-schema.json :: dataList[id=InkwashShadow_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[InkwashShadow_LowMorale]`
   limit: do 40 znaków
   EN: Overbearing Hubris
   PL: Bezczelna Pycha
86. [Status [InkwashShadow_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 피해량 증가 1, 취약 1을 얻음
   źródło: Bufs-schema.json :: dataList[id=InkwashShadow_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Damage Up and 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości
87. [Status [InkwashShadow_Panic] — nazwa] 안하무인
   źródło: Bufs-schema.json :: dataList[id=InkwashShadow_Panic].name
   kontekst: identyfikator statusu w tekstach: `[InkwashShadow_Panic]`
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Status [InkwashShadow_Panic] — opis] - 패닉\n- 턴 시작 시 피해량 증가 2, 취약 2를 얻음
   źródło: Bufs-schema.json :: dataList[id=InkwashShadow_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Damage Up and 2 Fragile
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Obrażeń i 2 Wrażliwości
89. [Status [ElectricPolePower] — nazwa] 고압 방전
   źródło: Bufs-schema.json :: dataList[id=ElectricPolePower].name
   kontekst: identyfikator statusu w tekstach: `[ElectricPolePower]`
   limit: do 40 znaków
   EN: High-voltage Discharge
   PL: Wysokonapięciowe Wyładowanie
90. [Status [ElectricPolePower] — opis] - 최댓값 : 10\n- 진동 폭발 피격 시 5 감소 (스킬당 1회)\n- 나태 속성 스킬 피격 시 1 감소 (스킬당 1회)\n- 나태 속성이 아닌 스킬에 받는 피해량 -100%\n- 흐트러짐 상태가 되지 않음
   źródło: Bufs-schema.json :: dataList[id=ElectricPolePower].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- When hit by Tremor Burst, lose 5 Stacks (once per Skill)\n- When hit by Sloth Skills, lose 1 Stack (once per Skill)\n- Take -100% damage from non-Sloth Skills\n- Cannot become Staggered
   PL: - Maks. stosów: 10\n- Przy trafieniu Wyładowaniem Wstrząsu traci 5 stosów (raz na Umiejętność)\n- Przy trafieniu Umiejętnościami Lenistwa traci 1 stos (raz na Umiejętność)\n- Otrzymuje -100% obrażeń od Umiejętności poza Lenistwem\n- Nie może zostać oszołomiony
91. [Status [SweeperSchema] — nazwa] 청소 시간
   źródło: Bufs-schema.json :: dataList[id=SweeperSchema].name
   kontekst: identyfikator statusu w tekstach: `[SweeperSchema]`
   limit: do 40 znaków
   EN: Time to <i>Sweep</i>
   PL: Czas na Sprzątanie
92. [Status [SweeperSchema] — opis] {0}턴 후 청소 종료
   źródło: Bufs-schema.json :: dataList[id=SweeperSchema].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The Sweeping ends after {0} turn(s)
   PL: Sprzątanie kończy się po {0} turach

## Statusy i efekty bojowe — Bufs-tkt-re
- plik gry: `Bufs-tkt-re.json`

93. [Status [AccumulatedPastSinner] — nazwa] 축적된 과거
   źródło: Bufs-tkt-re.json :: dataList[id=AccumulatedPastSinner].name
   kontekst: identyfikator statusu w tekstach: `[AccumulatedPastSinner]`
   limit: do 40 znaków
   EN: Accumulated Past
   PL: Zakumulowana Przeszłość
94. [Status [AccumulatedPastSinner] — opis] - 최대값 : 12\n- 턴 시작시 수치 3 당, 합 위력 증가 1, 공격 레벨 증가 1 얻음
   źródło: Bufs-tkt-re.json :: dataList[id=AccumulatedPastSinner].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 12\n- Turn Start: gain 1 Clash Power Up and 1 Offense Level Up for every 3 Stack
   PL: - Maks. stosów: 12\n- Na początku tury zyskuje 1 Wzrost Mocy Starcia i 1 Wzrost Poziomu Ataku za każde 3 stosy
95. [Status [OutisNoHat] — nazwa] 강력 징수 집행
   źródło: Bufs-tkt-re.json :: dataList[id=OutisNoHat].name
   kontekst: identyfikator statusu w tekstach: `[OutisNoHat]`
   limit: do 40 znaków
   EN: Violent Collections
   PL: Gwałtowne Windykacje
96. [Status [OutisNoHat] — opis] - 자신에게 신속이 있을 때, 자신의 기본 스킬로 얻는 자신의 진동 횟수 +1\n- 자신의 속도가 대상보다 빠르면, 피해량 (대상과의 속도 차이 x 3)% (최대 15%)
   źródło: Bufs-tkt-re.json :: dataList[id=OutisNoHat].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit has Haste, gain +1 more Tremor Count from its Base Skills\n- If this unit's Speed is faster than the target's, deal +(Speed difference x 3)% damage (max 15%)
   PL: - Jeżeli ma Pośpiech, podstawowe Umiejętności zyskują +1 więcej Licznika Wstrząsu\n- Jeżeli Szybkość jest większa niż celu, zadaje +(różnica Szybkości x 3)% obrażeń (maks. 15%)

## Statusy i efekty bojowe — Bufs-tkt
- plik gry: `Bufs-tkt.json`

97. [Status [FusionVibration] — nazwa] 진폭 얽힘
   źródło: Bufs-tkt.json :: dataList[id=FusionVibration].name
   kontekst: identyfikator statusu w tekstach: `[FusionVibration]`
   limit: do 40 znaków
   EN: Amplitude Entanglement
   PL: Splątanie Amplitudy
98. [Status [FusionVibration] — opis] - 얽힘시키는 진동 효과와 대상의 진동 계열을 진동 - 중첩으로 합침.\n- 얽힘 시 기존 진동의 위력, 횟수가 유지됨.\n- 진동 - 중첩에 진폭 변환 발동 시 변환시키려는 진동 효과가 얽힘으로 적용됨.\n- 턴 종료시, 진동으로 변환됨
   źródło: Bufs-tkt.json :: dataList[id=FusionVibration].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Fuses the effects of the Tremor type added by Amplitude Entanglement and the Tremor type currently on target together under Tremor - Superposition.\n- Potency and Count values do not change over Entanglement.\n- When triggering Amplitude Conversion on Tremor - Superposition, it activates as Amplitude Entanglement instead.\n- Turn End: converted into base Tremor.
   PL: - Scala efekt Wstrząsu dodawany przez Splątanie Amplitudy z typem Wstrząsu na celu w Wstrząs - Superpozycja.\n- Podczas Splątania Siła i Licznik obecnego Wstrząsu zostają zachowane.\n- Przy wywołaniu Konwersji Amplitudy na Wstrząsie - Superpozycji efekt Wstrząsu zadziała jako Splątanie Amplitudy.\n- Na koniec tury zamienia się w zwykły Wstrząs
99. [Status [VibrationNesting] — nazwa] 진동 - 중첩
   źródło: Bufs-tkt.json :: dataList[id=VibrationNesting].name
   kontekst: identyfikator statusu w tekstach: `[VibrationNesting]`
   limit: do 40 znaków
   EN: Tremor - Superposition
   PL: Wstrząs - Superpozycja
100. [Status [VibrationNesting] — opis] - 진폭 얽힘을 통해 얻을 수 얻을 수 있음.\n- 진폭 변환시 진동 - 중첩에 해당 특수 진동이 추가됨.
   źródło: Bufs-tkt.json :: dataList[id=VibrationNesting].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gained through Amplitude Entanglement\n- When triggering Amplitude Conversion, add the effects of the resulting Tremor type to the list of active Tremor effects under Tremor - Superposition.
   PL: - Zdobywany przez Splątanie Amplitudy\n- Przy wywołaniu Konwersji Amplitudy do listy aktywnych efektów Wstrząsu w Wstrząsie - Superpozycji dołącza wynikowy Specjalny Wstrząs
101. [Status [VibrationDistribution] — nazwa] 진동 - 분배
   źródło: Bufs-tkt.json :: dataList[id=VibrationDistribution].name
   kontekst: identyfikator statusu w tekstach: `[VibrationDistribution]`
   limit: do 40 znaków
   EN: Tremor - Distribution
   PL: Wstrząs - Dystrybucja
102. [Status [VibrationDistribution] — opis] - 턴 종료 시 (아군 전체의 진동 횟수의 합 / 살아있는 아군 수)만큼 다음 턴에 공격 레벨 증가를 얻음 (최대 5)\n- {1}턴 동안 진동 폭발 스킬로 피격 시, {0}만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs-tkt.json :: dataList[id=VibrationDistribution].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: - Turn End: Gain ((sum of all allies' Tremor Count) / (# of surviving allies)) Offense Level Up next turn (max 5)\n- For {1} turns, when hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by {0}\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Na koniec tury zyskuje w następnej turze Wzrost Poziomu Ataku w ilości (suma Liczników Wstrząsu wszystkich sojuszników / liczba żyjących sojuszników) (maks. 5)\n- Przez {1} tur przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}\n- Na koniec tury Licznik maleje o 1\n- (Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Wstrząsu)
103. [Status [TcorpSpecialInvestigator] — nazwa] T사 특별 수사관 배지
   źródło: Bufs-tkt.json :: dataList[id=TcorpSpecialInvestigator].name
   kontekst: identyfikator statusu w tekstach: `[TcorpSpecialInvestigator]`
   limit: do 50 znaków
   EN: T Corp. Special Investigator Badge
   PL: Odznaka Specjalnego Śledczego Korporacji T
104. [Status [TcorpSpecialInvestigator] — opis] - 체력이 0이 될 때, 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투당 1회 발동)\n- 버프 효과 발동 시 다음 턴부터 5턴 동안 턴 시작 시 공격 위력 증가 2 얻음.
   źródło: Bufs-tkt.json :: dataList[id=TcorpSpecialInvestigator].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: -When this unit takes lethal damage, their HP does not drop below 1, instantly heals 80% of their max HP, and recovers from Stagger. (Once per Encounter)\n- When this buff effect activates, starting next turn, this unit gains 2 Attack Power Up at every Turn Start for 5 turns.
   PL: - Przy śmiertelnych obrażeniach HP nie spada poniżej 1, natychmiast leczy 80% Maks. HP i wychodzi z Oszołomienia (1 raz na walkę)\n- Po wywołaniu tego efektu, od następnej tury, zyskuje 2 Wzrostu Mocy Ataku na początku każdej tury przez 5 tur.
105. [Status [VibrationChain] — nazwa] 진동 - 사슬
   źródło: Bufs-tkt.json :: dataList[id=VibrationChain].name
   kontekst: identyfikator statusu w tekstach: `[VibrationChain]`
   limit: do 40 znaków
   EN: Tremor - Chain
   PL: Wstrząs - Łańcuch
106. [Status [VibrationChain] — opis] - 진동 위력 10 당 합 위력 1 감소 (최대 3)\n- {1}턴 동안 진동 폭발 스킬로 피격 시 {0}만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs-tkt.json :: dataList[id=VibrationChain].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: - Lose 1 Clash Power for every 10 Tremor Potency on self (max 3)\n- For {1} Turns: When Hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by {0}.\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Moc Starcia maleje o 1 za każde 10 Mocy Wstrząsu (maks. 3)\n- Przez {1} tur przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}\n- Na koniec tury Licznik maleje o 1\n- (Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Wstrząsu)
107. [Status [VibrationChain] — podsumowanie] 진동 위력 10 당 합 위력 1 감소\n{0}만큼 흐트러짐 손상
   źródło: Bufs-tkt.json :: dataList[id=VibrationChain].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Lose 1 Clash Power for every 10 Tremor Potency on self\nRaise Stagger Threshold by {0}
   PL: Moc Starcia maleje o 1 za każde 10 Mocy Wstrząsu\nPróg Oszołomienia rośnie o {0}
108. [Status [TimeRentalTwo] — nazwa] T사의 시간 대여
   źródło: Bufs-tkt.json :: dataList[id=TimeRentalTwo].name
   kontekst: identyfikator statusu w tekstach: `[TimeRentalTwo]`
   limit: do 40 znaków
   EN: T Corp. Borrowed Time
   PL: Pożyczony Czas Korporacji T
109. [Status [TimeRentalTwo] — opis] 턴 종료시\n-다음 턴에 신속, 합 위력 증가, 취약 {1} 만큼 얻음.\n- 횟수가 1이면, 턴 종료시 효과를 대신하여 다음 턴에 속박 {0} 얻음\n- 위력 1 증가, 횟수 1 감소\n- 가지고 있는 신속보다 속박이 많을 경우 시간 대여 해제, 흐트러짐 상태가 됨.
   źródło: Bufs-tkt.json :: dataList[id=TimeRentalTwo].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: Turn End:\n- Gain {1} Haste, Clash Power Up, and Fragile next turn.\n- At 1 Count, gain {0} Bind next turn instead.\n- Gain 1 Stack and lose 1 Count\n- If this unit has more Bind than it has Haste, the Borrowed Time effect expires and this unit gets Staggered.
   PL: Na koniec tury\n- W następnej turze zyskuje {1} Pośpiechu, Wzrostu Mocy Starcia i Wrażliwości.\n- Przy 1 Liczniku zamiast powyższego efektu zyskuje w następnej turze {0} Spętań\n- Zyskuje 1 Siły i traci 1 Licznika\n- Jeżeli ma więcej Spętań niż Pośpiechu, efekt Pożyczonego Czasu znika, a jednostka zostaje oszołomiona.
110. [Status [TimeAccumulation] — nazwa] 시간 누진
   źródło: Bufs-tkt.json :: dataList[id=TimeAccumulation].name
   kontekst: identyfikator statusu w tekstach: `[TimeAccumulation]`
   limit: do 40 znaków
   EN: Time Delay
   PL: Opóźnienie Czasu
111. [Status [TimeAccumulation] — opis] 이 효과가 있는 동안 피해를 받지 않고 저장함.\n턴 종료 시 1 감소\n턴 종료 시 수치가 1이면, 저장한 피해의 2배만큼 나태 피해를 주고 효과 제거\n이 효과가 존재할 때, 추가로 얻거나 갱신되지 않음
   źródło: Bufs-tkt.json :: dataList[id=TimeAccumulation].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As long as this effect is active, damage dealt against this unit is stored and not taken.\nTurn End: reduce value by 1\nTurn End: If there is only 1 value left of this effect, the effect expires after dealing (2 x stored damage) Sloth damage to this unit\nWhen this effect is active, its value cannot be gained or be refreshed.
   PL: Dopóki ten efekt jest aktywny, otrzymywane obrażenia są magazynowane i nie są przyjmowane.\nNa koniec tury maleje o 1\nNa koniec tury, jeżeli zostaje tylko 1 wartość, efekt znika po zadaniu (2 x zmagazynowane obrażenia) obrażeń Lenistwa\nPodczas istnienia tego efektu jego wartość nie może zostać zdobyta ani odnowiona
112. [Status [ParryingResultDown] — nazwa] 합 위력 감소
   źródło: Bufs-tkt.json :: dataList[id=ParryingResultDown].name
   kontekst: identyfikator statusu w tekstach: `[ParryingResultDown]`
   limit: do 40 znaków
   EN: Clash Power Down
   PL: Spadek Mocy Starcia
113. [Status [ParryingResultDown] — opis] 합 진행 시, 합 위력이 수치만큼 감소
   źródło: Bufs-tkt.json :: dataList[id=ParryingResultDown].desc
   limit: do 120 znaków
   EN: In a Clash, lose Clash Power equal to the value
   PL: W Starciu traci Moc Starcia równą wartości
114. [Status [ParryingResultUp] — nazwa] 합 위력 증가
   źródło: Bufs-tkt.json :: dataList[id=ParryingResultUp].name
   kontekst: identyfikator statusu w tekstach: `[ParryingResultUp]`
   limit: do 40 znaków
   EN: Clash Power Up
   PL: Wzrost Mocy Starcia
115. [Status [ParryingResultUp] — opis] 합 진행 시, 합 위력이 수치만큼 증가
   źródło: Bufs-tkt.json :: dataList[id=ParryingResultUp].desc
   limit: do 120 znaków
   EN: In a Clash, gain Clash Power equal to the value
   PL: W Starciu zyskuje Moc Starcia równą wartości
116. [Status [ParryingResultUp] — podsumowanie] 합 진행 시, 합 위력이 수치만큼 증가
   źródło: Bufs-tkt.json :: dataList[id=ParryingResultUp].summary
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Status [LimitedTime] — nazwa] 빼앗은 시간
   źródło: Bufs-tkt.json :: dataList[id=LimitedTime].name
   kontekst: identyfikator statusu w tekstach: `[LimitedTime]`
   limit: do 40 znaków
   EN: Stolen Time
   PL: Skradziony Czas
118. [Status [LimitedTime] — opis] - 턴 시작 시 수치가 200 이상이면, ({0} - 200)/50만큼 공격 레벨 증가, 방어 레벨 증가를 얻음.\n- 턴 시작 시 수치가 200 미만이면, (200 - {0})/50 만큼 공격 레벨 감소, 방어 레벨 감소를 얻음.
   źródło: Bufs-tkt.json :: dataList[id=LimitedTime].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Turn Start: At 200+ value, gain ({0}- 200)/50 Offense Level Up & Defense Level Up.\n- Turn Start: At less than 200 value, gain (200 - {0})/50 Offense Level Down & Defense Level Down.
   PL: - Na początek tury przy wartości 200 lub więcej zyskuje ({0} - 200)/50 Wzrostów Poziomu Ataku i Wzrostów Poziomu Obrony.\n- Na początek tury przy wartości poniżej 200 zyskuje (200 - {0})/50 Spadków Poziomu Ataku i Spadków Poziomu Obrony.
119. [Status [OwnTime] — nazwa] 분담 시간
   źródło: Bufs-tkt.json :: dataList[id=OwnTime].name
   kontekst: identyfikator statusu w tekstach: `[OwnTime]`
   limit: do 40 znaków
   EN: Shared Time
   PL: Współdzielony Czas
120. [Status [OwnTime] — opis] - 턴 시작 시 수치가 40 이상이면, ({0} - 40)/10 만큼 공격 레벨 증가, 방어 레벨 증가를 얻음.\n- 턴 시작 시 수치가 40 미만이면, (40 - {0})/10 만큼 공격 레벨 감소, 방어 레벨 감소를 얻음.
   źródło: Bufs-tkt.json :: dataList[id=OwnTime].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Turn Start: At 40+ value, gain ({0}- 40)/10 Offense Level Up & Defense Level Up.\n- Turn Start: At less than 40 value, gain (40 - {0})/10 Offense Level Down & Defense Level Down.
   PL: - Na początek tury przy wartości 40+: zyskuje ({0} - 40)/10 Wzrostów Poziomu Ataku i Wzrostów Poziomu Obrony.\n- Przy wartości poniżej 40: zyskuje (40 - {0})/10 Spadków Poziomu Ataku i Spadków Poziomu Obrony.
121. [Status [EquitableDistribution] — nazwa] 시간 공동 분담 지출
   źródło: Bufs-tkt.json :: dataList[id=EquitableDistribution].name
   kontekst: identyfikator statusu w tekstach: `[EquitableDistribution]`
   limit: do 40 znaków
   EN: Joint Time Expenditure
   PL: Wspólny Wydatek Czasu
122. [Status [EquitableDistribution] — opis] 분담 시간이 소모될 때, 모든 뇌가 공정하게 시간을 지출함.
   źródło: Bufs-tkt.json :: dataList[id=EquitableDistribution].desc
   limit: do 120 znaków
   EN: When spending Shared Time, the Brains spend an equal amount of time across the board.
   PL: Gdy Współdzielony Czas jest wydawany, Mózgi wydawają go uczciwie, po równo.
123. [Status [UnfairDistribution] — nazwa] 내부 분열
   źródło: Bufs-tkt.json :: dataList[id=UnfairDistribution].name
   kontekst: identyfikator statusu w tekstach: `[UnfairDistribution]`
   limit: do 40 znaków
   EN: Infighting
   PL: Konflikt Wewnętrzny
124. [Status [UnfairDistribution] — opis] 분담 시간이 소모될 때 각 뇌가 내키는대로 시간을 지출함.\n턴 시작 시 남은 시간이 동일하지 않은 부위의 수만큼 모든 부위가 보호를 잃음.
   źródło: Bufs-tkt.json :: dataList[id=UnfairDistribution].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When spending Shared Time, the Brains no longer spend an equal amount of time across the board.\nTurn Start: all parts lose Protection equal to the number of Parts with different remaining Time values.
   PL: Gdy Współdzielony Czas jest wydawany, każdy Mózg wydaje go wedle własnego uznania.\nNa początku tury wszystkie części tracą Ochronę równą liczbie części o różnej pozostałej wartości Czasu.
125. [Status [TimeAcceleration] — nazwa] 시간 가속
   źródło: Bufs-tkt.json :: dataList[id=TimeAcceleration].name
   kontekst: identyfikator statusu w tekstach: `[TimeAcceleration]`
   limit: do 40 znaków
   EN: Time Acceleration
   PL: Przyspieszenie Czasu
126. [Status [TimeAcceleration] — opis] - 자신의 속도 5 증가\n- 자신의 스킬이 강화됨.\n- 취약 1을 얻고, 진동 폭발, 스킬, 코인 효과로 받는 흐트러짐 손상이 50% 증가함.
   źródło: Bufs-tkt.json :: dataList[id=TimeAcceleration].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 5 Speed\n- Enhances this unit's Skills.\n- Gain 1 Fragile; when Tremor Burst, Skill or Coin effect raises this unit's Stagger Threshold, it raises it by +50% more.
   PL: - Zyskuje 5 Szybkości\n- Wzmacnia Umiejętności tej jednostki.\n- Zyskuje 1 Wrażliwości; podniesienie Progu Oszołomienia przez Wyładowanie Wstrząsu, Umiejętności lub efekty Monet rośnie o 50%
127. [Status [Yurodivy_LowMorale] — nazwa] 어긋난 단결
   źródło: Bufs-tkt.json :: dataList[id=Yurodivy_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Yurodivy_LowMorale]`
   limit: do 40 znaków
   EN: Broken Unity
   PL: Rozbita Jedność
128. [Status [Yurodivy_LowMorale] — opis] - 사기 저하\n취약 1 얻음. 피격시, 자신의 진동 횟수 1 증가. (최대 3회)
   źródło: Bufs-tkt.json :: dataList[id=Yurodivy_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nGain 1 Fragile. Gain 1 Tremor Count when hit. (3 times max)
   PL: - Niskie Morale\nZyskuje 1 Wrażliwości. Przy trafieniu zyskuje 1 Licznika Wstrząsu. (maks. 3 razy)
129. [Status [Yurodivy_Panic] — nazwa] 어긋난 단결
   źródło: Bufs-tkt.json :: dataList[id=Yurodivy_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Yurodivy_Panic]`
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Status [Yurodivy_Panic] — opis] - 패닉\n취약 2 얻음. 피격 시, 자신의 진동 횟수 2 증가. (최대 3회)
   źródło: Bufs-tkt.json :: dataList[id=Yurodivy_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nGain 2 Fragile. Gain 2 Tremor Count when hit. (3 times max)
   PL: - Panika\nZyskuje 2 Wrażliwości. Przy trafieniu zyskuje 2 Licznika Wstrząsu. (maks. 3 razy)
131. [Status [TimeKillerWatch] — nazwa] 시간 구제 대상
   źródło: Bufs-tkt.json :: dataList[id=TimeKillerWatch].name
   kontekst: identyfikator statusu w tekstach: `[TimeKillerWatch]`
   limit: do 40 znaków
   EN: Time Relief Entitlement
   PL: Cel Ratowania Czasu
132. [Status [TimeKillerWatch] — opis] 시간 가속 상태동안 시간 살인마의 공격 대상이 됨.
   źródło: Bufs-tkt.json :: dataList[id=TimeKillerWatch].desc
   limit: do 120 znaków
   EN: Targeted by the Time Ripper while Time Acceleration is active.
   PL: Podczas Przyspieszenia Czasu staje się celem ataków Zabójcy Czasu.
133. [Status [UltraPrecisionTimeAcceleration] — nazwa] 초정밀 시간 가속
   źródło: Bufs-tkt.json :: dataList[id=UltraPrecisionTimeAcceleration].name
   kontekst: identyfikator statusu w tekstach: `[UltraPrecisionTimeAcceleration]`
   limit: do 50 znaków
   EN: Microprecision Time Acceleration
   PL: Mikroprecyzyjne Przyspieszenie Czasu
134. [Status [UltraPrecisionTimeAcceleration] — opis] 수치만큼 자신의 속도 최저 기본값과 최고 기본값이 증가\n진동 위력, 횟수를 부여하거나, 진동 폭발 효과를 보유한 스킬의 기본 위력 +(수치), 적에게 가하는 피해량 +(수치 X 10)%, 적에게 진동 폭발로 가하는 흐트러짐 손상 (수치 X 10)% 증가 (E.G.O 스킬 포함)\n턴 종료 시 1 감소\n수치가 1이면, 0이 되지 않고 스테이지동안 유지됨
   źródło: Bufs-tkt.json :: dataList[id=UltraPrecisionTimeAcceleration].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This unit gains base Min and Max Speed by Stack\nSkills that inflict Tremor Potency, Count, or trigger Tremor Burst: gain Base Power +(Stack), deal +(Stack x 10)% damage against enemies, and when raising Stagger Thresholds via Tremor Burst, increase the amount raised by (Stack x 10)% (including E.G.O Skills)\nReduced by 1 at Turn End\nAt 1 Stack, the Stack does not drop below 0, and is maintained through the Encounter.
   PL: Zyskuje bazowe Min. i Maks. Szybkość równe stosom\nUmiejętności nakładające Siłę lub Licznik Wstrząsu albo wywołujące Wyładowanie Wstrząsu zyskują Moc Bazową +(stosy), zadają +(stosy x 10)% obrażeń wrogom, a podniesienie Progu Oszołomienia przez Wyładowanie Wstrząsu rośnie o (stosy x 10)% (w tym Umiejętności E.G.O)\nNa koniec tury maleje o 1\nPrzy 1 stosie wartość nie spada do 0 i utrzymuje się przez całą walkę

## Statusy i efekty bojowe — Bufs-twth
- plik gry: `Bufs-twth.json`

135. [Status [BearClawWound] — nazwa] 찢긴 색채 [루주]
   źródło: Bufs-twth.json :: dataList[id=BearClawWound].name
   kontekst: identyfikator statusu w tekstach: `[BearClawWound]`
   limit: do 40 znaków
   EN: Mauled Color [Rouge]
   PL: Rwana Barwa [Rouge]
136. [Status [BearClawWound] — opis] - 최댓값 : 9\n- 피격 시 수치 3당, 출혈 위력 1 얻음 (턴당 1회)\n- 턴 종료 시 다음 턴에 수치 4당 방어 레벨 감소 1 얻음 (최대 2)\n- 턴 종료 시 1 감소
   źródło: Bufs-twth.json :: dataList[id=BearClawWound].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- When hit, gain 1 Bleed Potency for every 3 Stack (once per turn)\n- Turn End: Gain 1 Defense Level Down next turn for every 4 Stack (max 2)\n- Turn End: Lose 1 Stack
   PL: - Maks. stosów: 9\n- Przy trafieniu zyskuje 1 Siły Krwawienia za każde 3 stosy (1 raz na turę)\n- Na koniec tury zyskuje 1 Spadek Poziomu Obrony w następnej turze za każde 4 stosy (maks. 2)\n- Na koniec tury maleje o 1
137. [Status [BearClawWound] — tekst klimatyczny] ‘약지의 물감은 강화 문신과 재료가 같다는 말이 있죠. 한 번 새겨지면 색이 쉽게 빠지지 않고 지워지지 않으니까.’
   źródło: Bufs-twth.json :: dataList[id=BearClawWound].flavor
   limit: do 240 znaków
   EN: 'Some say that the Ring's paint is made from the same base material as Augmentation Tattoos—they are both nigh-indelible pigments that take considerable effort to erase, let alone bleach.'
   PL: „Mówią, że farby Serdecznego mają tę samą bazę co wzmocnione tatuaże — raz utrwalone, kolor prawie nie schodzi i nie da się go zatrzeć.”
138. [Status [EagleClawWound] — nazwa] 찢긴 색채 [블뢰]
   źródło: Bufs-twth.json :: dataList[id=EagleClawWound].name
   kontekst: identyfikator statusu w tekstach: `[EagleClawWound]`
   limit: do 40 znaków
   EN: Mauled Color [Bleu]
   PL: Rwana Barwa [Bleu]
139. [Status [EagleClawWound] — opis] - 최댓값 : 9\n- 피격 시 수치 3당, 침잠 위력 1 얻음 (턴당 1회)\n- 턴 종료 시 수치가 5 이상이면, 정신력 5 감소\n- 턴 종료 시 1 감소
   źródło: Bufs-twth.json :: dataList[id=EagleClawWound].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- When hit, gain 1 Sinking Potency for every 3 Stack (once per turn)\n- Turn End: At 5+ Stack, lose 5 SP\n- Turn End: Lose 1 Stack
   PL: - Maks. stosów: 9\n- Przy trafieniu zyskuje 1 Siły Zatonięcia za każde 3 stosy (1 raz na turę)\n- Na koniec tury przy 5+ stosach traci 5 Poczytalności\n- Na koniec tury maleje o 1
140. [Status [EagleClawWound] — tekst klimatyczny] ‘중지의 문신이 스스로 새겨 넣어 강화하는 것이라면, 약지의 문신은 대상에게 강제로 새겨 약화시키는 것일까?’
   źródło: Bufs-twth.json :: dataList[id=EagleClawWound].flavor
   limit: do 200 znaków
   EN: 'If the Middle uses their tattoos for self-augmentation, does that make the Ring's tattoos more brands that, when forcibly applied, weaken their enemies?'
   PL: „Jeżeli Środkowy tuszuje się sam dla wzmocnienia, to tatuaże Serdecznego to raczej piętna, które nakłada się na wrogów, by ich osłabić?”
141. [Status [BoldBrushstrokes] — nazwa] 과감한 터치
   źródło: Bufs-twth.json :: dataList[id=BoldBrushstrokes].name
   kontekst: identyfikator statusu w tekstach: `[BoldBrushstrokes]`
   limit: do 40 znaków
   EN: Touche Hardie
   PL: Touche Hardie
142. [Status [BoldBrushstrokes] — opis] - 이 효과가 있는 동안 출혈과 침잠으로 인한 체력 피해와 정신력 피해를 2배로 받음\n- 턴 종료 시 1 감소\n- 최댓값 : 1
   źródło: Bufs-twth.json :: dataList[id=BoldBrushstrokes].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - While this unit has this effect, double the amount of HP and SP damage this unit takes from Bleed and Sinking\n- Turn End: Lose 1 Stack\n- Max Stack: 1
   PL: - Dopóki posiada ten efekt, podwaja obrażenia HP i Poczytalności otrzymywane od Krwawienia i Zatonięcia\n- Na koniec tury maleje o 1\n- Maks. stosów: 1
143. [Status [BoldBrushstrokes] — tekst klimatyczny] “늑대의 발톱과 스라소니의 발톱, 그리고 잘 보이지 않는 여러 거북이의 발톱으로 디테일을 챙기다니… 과감하군요.”
   źródło: Bufs-twth.json :: dataList[id=BoldBrushstrokes].flavor
   limit: do 160 znaków
   EN: "Wolven claws, lynx claws... and even those of turtles, so minuscule yet intricately arranged... What a bold expression."
   PL: „Pazury wilka, pazury rysia... i nawet żółwi, tak maleńkie, a tak mistycznie ułożone... Jak odważny wyraz.”
144. [Status [IntenseColors] — nazwa] 강렬한 색채
   źródło: Bufs-twth.json :: dataList[id=IntenseColors].name
   kontekst: identyfikator statusu w tekstach: `[IntenseColors]`
   limit: do 40 znaków
   EN: Palette Vibrante
   PL: Palette Vibrante
145. [Status [IntenseColors] — opis] - 약지 소속에게 받는 피해량 +(수치x5)%\n· 대상이 약지 야수파 소속이면 효과가 강화되어, 대신 피해량 +(수치x10)%\n- 전투 시작 시 (수치+1)만큼 출혈, 침잠 얻고 출혈 횟수, 침잠 횟수 증가\n- 전투 종료 시 이 효과가 소멸되고 찢긴 색채 [루주], 찢긴 색채 [블뢰] 수치가 절반으로 감소 (소수점 버림)\n- 최댓값 : 4
   źródło: Bufs-twth.json :: dataList[id=IntenseColors].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +(Stack x 5)% damage from The Ring-faction units\n· If the attacker is in The Ring School of Fauvism faction, take +(Stack x 10)% damage instead\n- Combat Start: Gain (Stack +1) Bleed, Sinking, Bleed Count, and Sinking Count\n- Combat End: This effect expires. Halve Mauled Color [Rouge] and Mauled Color [Bleu] Stacks on this unit (rounded down)\n- Max Stack: 4
   PL: - Otrzymuje +(stosy x 5)% obrażeń od Stronnictwa Serdecznego\n· Jeżeli atakujący należy do Szkoły Fowizmu Stronnictwa Serdecznego, zamiast tego +(stosy x 10)%\n- Na początku walki zyskuje (stosy +1) Krwawienia i Zatonięcia oraz ich Liczniki\n- Po zakończeniu walki ten efekt znika, a stosy Rwanej Barwy [Rouge] i Rwanej Barwy [Bleu] są zmniejszane o połowę (zaokrąglone w dół)\n- Maks. stosów: 4
146. [Status [FaubismWolfMask] — nazwa] 야수파 - 마스크 드 루
   źródło: Bufs-twth.json :: dataList[id=FaubismWolfMask].name
   kontekst: identyfikator statusu w tekstach: `[FaubismWolfMask]`
   limit: do 40 znaków
   EN: Le Fauvisme - Masque de Loup
   PL: Le Fauvisme - Masque de Loup
147. [Status [FaubismWolfMask] — opis] - 속도 최솟값, 최댓값 +1\n- 스킬로 부여하는 출혈, 침잠 위력 부여량 +1\n- 적중 전 대상에게 침잠이 없으면, 대상의 침잠 횟수 2 증가 (턴당 수감자별 1회)\n- 피격 직전 대상에게 출혈이 없으면, 대상의 출혈 횟수 2 증가 (턴당 수감자별 1회)
   źródło: Bufs-twth.json :: dataList[id=FaubismWolfMask].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Inflict +1 more Bleed and Sinking Potency with Skills\n- Before hitting, if target does not have Sinking, inflict +2 Sinking Count (once per Sinner per turn)\n- Before Getting Hit, if target does not have Bleed, inflict +2 Bleed Count (once per Sinner per turn)
   PL: - Min. i Maks. Szybkość +1\n- Umiejętności nakładają +1 więcej Siły Krwawienia i Zatonięcia\n- Przed trafieniem, jeżeli cel nie ma Zatonięcia, zyskuje +2 Licznika Zatonięcia (1 raz na Grzesznika na turę)\n- Przed otrzymaniem trafienia, jeżeli cel nie ma Krwawienia, zyskuje +2 Licznika Krwawienia (1 raz na Grzesznika na turę)
148. [Status [FaubismWolfMask] — tekst klimatyczny] “흑수, R사 혹은 다른 짐승을 이용한 무언가들과 야수파가 무엇이 다른가 싶을 수 있죠.”\n\n“흑수가 짐승을 몸에 박아 넣은 것이라면, 야수파는 덧씌워 입는 작품으로 표현해내는 것.”
   źródło: Bufs-twth.json :: dataList[id=FaubismWolfMask].flavor
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "One might ask: What even distinguishes les Fauves from factions such as Heishous, R Corp. Packs, and more that incorporate beasts into their identities?"\n\n"A reasonable query, of that there is no doubt; to that I say we are distinguished by the transcendence of beastliness into artistic costumery, while the Heishous have mindlessly jammed it into their anatomies, disregarding their aesthetic qualities."
   PL: „Można pytać: co odróżnia les Fauves od frakcji takich jak Heishou, stada Korporacji R i innych, które wplatają bestie w swoją tożsamość?”\n\n„Słuszne pytanie; odpowiem tak: my przemieniamy dzikość w dzieło sztuki nakładane na siebie, podczas gdy Heishou bezmyślnie wpisują je we własne ciała, nie dbając o walory estetyczne.”
149. [Status [FaubismWolfMaskBlooded] — nazwa] 야수파 - 마스크 드 루 앙상글랑테
   źródło: Bufs-twth.json :: dataList[id=FaubismWolfMaskBlooded].name
   kontekst: identyfikator statusu w tekstach: `[FaubismWolfMaskBlooded]`
   limit: do 60 znaków
   EN: Le Fauvisme - Masque de Loup Ensanglanté
   PL: Le Fauvisme - Masque de Loup Ensanglanté
150. [Status [FaubismWolfMaskBlooded] — opis] - 피해량 +20%, 모든 코인이 파괴 불가 코인으로 변경됨\n- 속도 최솟값, 최댓값 +1\n- 스킬로 부여하는 다음 부정적인 효과의 부여량 +1\n· 출혈 위력과 횟수\n· 침잠 위력과 횟수\n- 적중 전 대상에게 침잠이 없으면, 대상의 침잠 횟수 2 증가 (턴당 수감자별 3회)\n- 피격 직전 대상에게 출혈이 없으면, 대상의 출혈 횟수 2 증가 (턴당 수감자별 3회)
   źródło: Bufs-twth.json :: dataList[id=FaubismWolfMaskBlooded].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage; convert all Coins into Unbreakable Coins\n- Min & Max Speed +1\n- Inflict +1 more of the following negative effects with Skills\n· Bleed Potency and Count\n· Sinking Potency and Count\n- Before hitting, if target does not have Sinking, inflict +2 Sinking Count (3 times per Sinner per turn)\n- Before Getting Hit, if target does not have Bleed, inflict +2 Bleed Count (3 times per Sinner per turn)
   PL: - Zadaje +20% obrażeń; wszystkie Monety stają się Niezniszczalnymi Monetami\n- Min. i Maks. Szybkość +1\n- Umiejętności nakładają +1 więcej następujących negatywnych efektów\n· Siła i Licznik Krwawienia\n· Siła i Licznik Zatonięcia\n- Przed trafieniem, jeżeli cel nie ma Zatonięcia, zyskuje +2 Licznika Zatonięcia (3 razy na Grzesznika na turę)\n- Przed otrzymaniem trafienia, jeżeli cel nie ma Krwawienia, zyskuje +2 Licznika Krwawienia (3 razy na Grzesznika na turę)
151. [Status [FaubismWolfMaskBlooded] — tekst klimatyczny] 단순히 짐승 탈을 머리에 쓴다고 해서 야성이 일깨워지고 전투력이 상승하는 것은 아니다.\n탈 안에는 야수파의 물감으로 칠해진 수많은 바늘이 있어, 탈을 뒤집어쓰는 것만으로도 바늘들이 몸속으로 물감을 주입한다.\n\n약지의 물감. 결국 모든 약지는 물감을 사용할 수밖에 없다.
   źródło: Bufs-twth.json :: dataList[id=FaubismWolfMaskBlooded].flavor
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One does not simply awaken the power of one's inner ferity by donning a beastly mask.\nThe interior of each headgear worn by these artists is lined with a mat of needles dipped in the Fauvist paint, which is injected into the body upon equipment. \n\nThus is the paint of the Ring—and these artists, regardless of their School, are all bound to use it.
   PL: Samo założenie maski bestii nie budzi wewnętrznej dzikości.\nWnętrze każdego nakrycia głowy tych artystów wyścieła matowina igieł zanurzonych w farbie Le Fauvisme, która wstrzykuje się do ciała przy złożeniu.\n\nTak jest z farbą Stronnictwa Serdecznego — a ci artyści, niezależnie od Szkoły, wszyscy muszą jej używać.
152. [Status [PanicChangeLock] — nazwa] 패닉 변경 불가
   źródło: Bufs-twth.json :: dataList[id=PanicChangeLock].name
   kontekst: identyfikator statusu w tekstach: `[PanicChangeLock]`
   limit: do 40 znaków
   EN: Fixed Panic
   PL: Zablokowana Panika
153. [Status [PanicChangeLock] — opis] - 패닉 유형을 변경하는 버프 획득 시, 패닉 유형이 변경되지 않는 대신 정신력이 없는 대상에게 부여되는 효과가 부여됨
   źródło: Bufs-twth.json :: dataList[id=PanicChangeLock].desc
   limit: do 240 znaków
   EN: This unit's Panic Type does not change when inflicted with an effect that changes Panic Types. Instead, this unit is inflicted with an effect that is inflicted against Non-SP Units.
   PL: - Przy zdobyciu efektu zmieniającego typ Paniki typ nie ulega zmianie; zamiast tego nakładany jest efekt stosowany wobec jednostek bez Poczytalności
154. [Status [Fauvism_Lowmorale] — nazwa] 떨어지는 영감
   źródło: Bufs-twth.json :: dataList[id=Fauvism_Lowmorale].name
   kontekst: identyfikator statusu w tekstach: `[Fauvism_Lowmorale]`
   limit: do 40 znaków
   EN: Faltering Inspiration
   PL: Wygasająca Inspiracja
155. [Status [Fauvism_Lowmorale] — opis] - 사기 저하\n- 자신이 공격하는 대상에게 찢긴 색채가 있으면, 피해량 10% 증가\n- 취약 1 얻음
   źródło: Bufs-twth.json :: dataList[id=Fauvism_Lowmorale].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If target this unit attacks has Mauled Color, deal +10% damage\n- Gain 1 Fragile
   PL: - Niskie Morale\n- Jeżeli cel ataku ma Rwaną Barwę, zadaje +10% obrażeń\n- Zyskuje 1 Wrażliwości
156. [Status [Fauvism_Panic] — nazwa] 떨어지는 영감
   źródło: Bufs-twth.json :: dataList[id=Fauvism_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Fauvism_Panic]`
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Status [Fauvism_Panic] — opis] - 패닉\n- 자신이 공격하는 대상에게 찢긴 색채가 있으면, 피해량 20% 증가\n- 취약 2 얻음
   źródło: Bufs-twth.json :: dataList[id=Fauvism_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- If target this unit attacks has Mauled Color, deal +20% damage\n- Gain 2 Fragile
   PL: - Panika\n- Jeżeli cel ataku ma Rwaną Barwę, zadaje +20% obrażeń\n- Zyskuje 2 Wrażliwości
158. [Status [FauvismDocent_Lowmorale] — nazwa] 충동적인 채색
   źródło: Bufs-twth.json :: dataList[id=FauvismDocent_Lowmorale].name
   kontekst: identyfikator statusu w tekstach: `[FauvismDocent_Lowmorale]`
   limit: do 40 znaków
   EN: Coloriage Impulsif
   PL: Coloriage Impulsif
159. [Status [FauvismDocent_Lowmorale] — opis] - 사기 저하\n- 자신이 공격하는 대상이 보유한 부정적인 효과 1개당, 피해량 +2.5% (최대 15%)\n- 취약 1 얻음
   źródło: Bufs-twth.json :: dataList[id=FauvismDocent_Lowmorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal +2.5% damage for every type of negative effect on target this unit attacks (max 15%)\n- Gain 1 Fragile
   PL: - Niskie Morale\n- Zadaje +2,5% obrażeń za każdy rodzaj negatywnego efektu na atakowanym celu (maks. 15%)\n- Zyskuje 1 Wrażliwości
160. [Status [FauvismDocent_Panic] — nazwa] 충동적인 채색
   źródło: Bufs-twth.json :: dataList[id=FauvismDocent_Panic].name
   kontekst: identyfikator statusu w tekstach: `[FauvismDocent_Panic]`
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Status [FauvismDocent_Panic] — opis] - 패닉\n- 자신이 공격하는 대상이 보유한 부정적인 효과 1개당, 피해량 +5% (최대 30%)\n- 취약 2 얻음
   źródło: Bufs-twth.json :: dataList[id=FauvismDocent_Panic].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal +5% damage for every type of negative effect on target this unit attacks (max 30%)\n- Gain 2 Fragile
   PL: - Panika\n- Zadaje +5% obrażeń za każdy rodzaj negatywnego efektu na atakowanym celu (maks. 30%)\n- Zyskuje 2 Wrażliwości
162. [Status [IndexPrescriptEnemy_0] — nazwa] 지령[쪽지] I
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_0].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptEnemy_0]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] I
   PL: Nakaz [Kartka] I
163. [Status [IndexPrescriptEnemy_0] — opis] 수감자를 공격하여 적중한다.\n\n- 턴 시작 시 지령의 가호가 0~2일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_0].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Sinner.\n\n- Turn Start: At 0~2 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Atakuje Grzesznika i trafia.\n\n- Na początku tury zdobywany przy Łasce Nakazu 0–2\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
164. [Status [IndexPrescriptEnemy_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_0].flavor
   limit: do 220 znaków
   EN: The Prescripts are delivered by many means, their medium determined with finality akin to divine prophecy. Those who receive them hold no power over how they arrive.
   PL: Nakazy przekazywane są na rozmaite sposoby. Forma, w jakiej dotrą do adresata, zostaje wybrana jednokierunkowo, niczym wyrocznia — bez jego wpływu.
165. [Status [IndexPrescriptEnemy_1] — nazwa] 지령[쪽지] II
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_1].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptEnemy_1]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] II
   PL: Nakaz [Kartka] II
166. [Status [IndexPrescriptEnemy_1] — opis] 지령 대상을 공격하여 적중한다.\n\n- 턴 시작 시 지령의 가호가 3~5일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target.\n\n- Turn Start: At 3~5 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Atakuje Cel Nakazu i trafia.\n\n- Na początku tury zdobywany przy Łasce Nakazu 3–5\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
167. [Status [IndexPrescriptEnemy_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_1].flavor
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Status [IndexPrescriptEnemy_2] — nazwa] 지령[쪽지] III
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_2].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptEnemy_2]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] III
   PL: Nakaz [Kartka] III
169. [Status [IndexPrescriptEnemy_2] — opis] 자신을 포함한 아군이 무작위 수감자를 흐트러뜨리거나 처치한다.\n\n- 턴 시작 시 지령의 가호가 6~8일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stagger or eliminate a random Sinner, either by you or your ally.\n\n- Turn Start: At 6~8 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Ty lub sojusznik oszołomiasz albo zabijasz losowego Grzesznika.\n\n- Na początku tury, przy 6–8 Łaskach Nakazu\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
170. [Status [IndexPrescriptEnemy_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_2].flavor
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Status [IndexPrescriptEnemy_3] — nazwa] 지령[쪽지] IV
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_3].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptEnemy_3]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] IV
   PL: Nakaz [Kartka] IV
172. [Status [IndexPrescriptEnemy_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 지령의 가호가 9일 때 얻음
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: At 9 Grace of the Prescript, gain this effect
   PL: Zabija wszystkich wrogów, zanim nadejdzie kolejny Nakaz.\n\n- Na początku tury, przy 9 Łaskach Nakazu
173. [Status [IndexPrescriptEnemy_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-twth.json :: dataList[id=IndexPrescriptEnemy_3].flavor
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Status [KarmaOfIndexEnemy] — nazwa] 카르마
   źródło: Bufs-twth.json :: dataList[id=KarmaOfIndexEnemy].name
   kontekst: identyfikator statusu w tekstach: `[KarmaOfIndexEnemy]`
   limit: do 40 znaków
   EN: Karmic Consequence
   PL: Karma
175. [Status [KarmaOfIndexEnemy] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 최대 100
   źródło: Bufs-twth.json :: dataList[id=KarmaOfIndexEnemy].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stacks\n· Gain 1 Fragile for every 20 Stacks\n- Max Stack: 100
   PL: - Na początku tury:\n· 1 Spadek Poziomu Obrony za każde 10 stosów\n· 1 Wrażliwość za każde 20 stosów\n- Maks. stosów: 100
176. [Status [KarmaOfIndexEnemy] — tekst klimatyczny] 지령을 받고, 수행한다. 그것은 하나의 업이 되어, 돌고 돌아 축적되기 마련.
   źródło: Bufs-twth.json :: dataList[id=KarmaOfIndexEnemy].flavor
   limit: do 200 znaków
   EN: Receive the Prescript and undertake it. Its execution is etched as karma, drawn into a ceaseless cycle that circles back to the hand of its executor.
   PL: Przyjmuje Nakaz i wypełnia go. Wypełnienie staje się karmą, która — krążąc bez końca — nawarstwia się znowu.
177. [Status [ResentmentSpiderDaughterTwo] — nazwa] <s>중지</s> - 원한
   źródło: Bufs-twth.json :: dataList[id=ResentmentSpiderDaughterTwo].name
   kontekst: identyfikator statusu w tekstach: `[ResentmentSpiderDaughterTwo]`
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Middle</s> - Grudge
   PL: <s>Środkowy</s> - Uraza
178. [Status [ResentmentSpiderDaughterTwo] — opis] - 최댓값: 10\n- 특정 스킬 사용시 감소\n- 수치당 공격 레벨 +1, 방어 레벨 -2, 반격 스킬의 피해량 +5%\n- 최댓값일 시, 받는 피해량 +20%
   źródło: Bufs-twth.json :: dataList[id=ResentmentSpiderDaughterTwo].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced when using certain Skills\n- For every Stack, Offense Level +1, Defense Level -2, and Counter Skills deal +5% damage\n- At max Stack, take +20% damage
   PL: - Maks. stosów: 10\n- Zmniejszana przy użyciu określonych Umiejętności\n- Za każdy stos: Poziom Ataku +1, Poziom Obrony -2, Obrażenia Umiejętności Kontratakujących +5%\n- Przy maks. stosach otrzymuje +20% obrażeń
179. [Status [ReinforcedTattooSpiderDaughterTwo] — nazwa] <s>중지식</s> 강화문신
   źródło: Bufs-twth.json :: dataList[id=ReinforcedTattooSpiderDaughterTwo].name
   kontekst: identyfikator statusu w tekstach: `[ReinforcedTattooSpiderDaughterTwo]`
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Middle Styled</s> Augmentation Tattoos
   PL: <s>Styl Środkowego</s> - Wzmacniane Tatuaże
180. [Status [ReinforcedTattooSpiderDaughterTwo] — opis] - 최댓값: 3\n- 타격, 질투 속성의 피해량 +10%
   źródło: Bufs-twth.json :: dataList[id=ReinforcedTattooSpiderDaughterTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Deal +10% Blunt and Envy damage
   PL: - Maks. stosów: 3\n- Zadaje +10% obrażeń atakami Uderzenia i Zazdrości
181. [Status [HeatingWireOnSpiderTwo] — nazwa] 열선 ON
   źródło: Bufs-twth.json :: dataList[id=HeatingWireOnSpiderTwo].name
   kontekst: identyfikator statusu w tekstach: `[HeatingWireOnSpiderTwo]`
   limit: do 40 znaków
   EN: Thermal Blades ON
   PL: Ostrza Termiczne - ON
182. [Status [HeatingWireOnSpiderTwo] — opis] 열선 스킬의 코인 적중시 출혈 위력 및 횟수 부여량 만큼 화상 위력 및 횟수 추가 부여
   źródło: Bufs-twth.json :: dataList[id=HeatingWireOnSpiderTwo].desc
   limit: do 170 znaków
   EN: On Hit with Thermal Blade Skill Coins: Additionally inflict Burn Potency and Count equal to Bleed Potency and Count inflicted
   PL: Przy trafieniu monetą Umiejętności Ostrzy Termicznych dodatkowo nadaje Podpalenie (Moc i Licznik) w wysokości nadawanego Krwawienia (Moc i Licznik)

## Statusy i efekty bojowe — Bufs-walpu10
- plik gry: `Bufs-walpu10.json`

183. [Status [Emulation] — nazwa] 본받는 자세
   źródło: Bufs-walpu10.json :: dataList[id=Emulation].name
   kontekst: identyfikator statusu w tekstach: `[Emulation]`
   limit: do 40 znaków
   EN: Learning by Example
   PL: Naśladowanie Przykładu
184. [Status [Emulation] — opis] 최댓값: 30\n다음 조건에 따라서 수치가 상승\n- 자신이 합 승리 시 수치 2, 기본 공격 스킬 적중 시 수치 1, 공격 종료시 적이 사망했으면, 수치 3 얻음.\n- 자신을 제외한 아군이 기본 공격 스킬로 합 승리 시 수치 2 얻음.\n· 자신과 같은 소속사인 자신을 제외한 아군이 기본 공격 스킬로 합 승리 시 대신 수치 4 얻음.\n\n수치에 따라 다음 효과를 누적하여 적용.\n- 수치 1당, 기본 공격 스킬의 피해량 +1% (최대 30%)\n- 10 이상 : 기본 공격 스킬의 합 위력 +1.\n- 20 이상 : 기본 공격 스킬의 코인 위력 +1.
   źródło: Bufs-walpu10.json :: dataList[id=Emulation].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 30\nGain Stacks based on the following conditions:\n- On Clash Win, gain 2 Stacks; On Hit using Base Attack Skills, gain 1 Stack; At Attack End, if the enemy was defeated, gain 3 Stacks\n- On Clash Win using Base Attack Skills by other allies, gain 2 Stacks\n · On Clash Win using Base Attack Skills by other allies in the same faction as this unit, gain 4 Stacks instead\n\nGain the following effects cumulatively based on Stacks:\n- Base Attack Skills deal +1% damage for every Stack (max 30%)\n- 10+: Base Attack Skills Clash Power +1\n- 20+: Base Attack Skills Coin Power +1
   PL: Maks. stosów: 30\nZyskuje stosy według następujących warunków:\n- Po wygranym Starciu: +2 stosy; przy trafieniu monetą podstawowej Umiejętności ataku: +1 stos; jeśli po zakończeniu ataku wrog ginie: +3 stosy\n- Po wygranym Starciu podstawową Umiejętnością ataku przez sojusznika (poza tą jednostką): +2 stosy\n · Jeśli podstawową Umiejętnością ataku wygra sojusznik tej samej frakcji (poza tą jednostką): zamiast tego +4 stosy\n\nWedług liczby stosów działają kumulatywnie następujące efekty:\n- Za każdy stos podstawowe Umiejętności ataku zadają +1% obrażeń (maks. 30%)\n- Od 10 stosów: Moc Starcia podstawowych Umiejętności ataku +1\n- Od 20 stosów: Moc Monet podstawowych Umiejętności ataku +1
185. [Status [Emulation] — podsumowanie] 특정 조건에 따라 수치 증가\n수치에 따라 피해량, 합 위력, 코인 위력 증가
   źródło: Bufs-walpu10.json :: dataList[id=Emulation].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Stacks based on certain conditions\nDeal more damage, gain Clash Power, gain Coin Power based on Stacks
   PL: Zyskuje stosy pod pewnymi warunkami\nWedług stosów: większe obrażenia, Moc Starcia i Moc Monet
186. [Status [CursedBlessing] — nazwa] 절망의 시험
   źródło: Bufs-walpu10.json :: dataList[id=CursedBlessing].name
   kontekst: identyfikator statusu w tekstach: `[CursedBlessing]`
   limit: do 40 znaków
   EN: A Test of Despair
   PL: Próba Rozpaczy
187. [Status [CursedBlessing] — opis] - 모든 슬롯의 도발치 20 증가\n- 공격 스킬 사용 시 정신력 20 감소\n- 사망 시 자신을 제외한 모든 아군 정신력 20 감소
   źródło: Bufs-walpu10.json :: dataList[id=CursedBlessing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All Slots gain +20 Aggro\n- On Attack Skill Use, lose 20 SP\n- On Death, all other allies lose 20 SP
   PL: - Prowokacja slotów +20\n- Umiejętność ataku: traci 20 Poczytalności\n- Po śmierci pozostali sojusznicy tracą 20 Poczytalności
188. [Status [BeyondDespair] — nazwa] 절망을 넘어선 자
   źródło: Bufs-walpu10.json :: dataList[id=BeyondDespair].name
   kontekst: identyfikator statusu w tekstach: `[BeyondDespair]`
   limit: do 40 znaków
   EN: The One Beyond Despair
   PL: Ten, Który Przekroczył Rozpacz
189. [Status [BeyondDespair] — opis] - 턴 시작 시 보호 2, 공격 위력 증가 1 얻음\n- 수비 스킬 사용 시 수비 위력 증가 3 얻음 (턴당 1회)\n- 합 승리 시 정신력 5 회복 (턴당 2회)\n· 정신력이 최대치이면, 자신이 보유한 해제 가능한 부정적인 효과 1개 제거\n- 기본 스킬 종료 시 해당 스킬이 각 적에게 가한 피해량 10%만큼 오만 피해\n\n- 체력이 0이 되는 피해를 받으면, 해당 턴 피해를 받지 않음 (전투당 1회)\n· 위 효과가 발동한 다음 턴에 체력을 모두 회복하고, 전투 종료 시까지 자신의 보호 수치 1당, 가하는 피해량 +10% (최대 80%)
   źródło: Bufs-walpu10.json :: dataList[id=BeyondDespair].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 2 Protection and 1 Attack Power Up\n- On Defense Skill Use, gain 3 Defense Power Up (once per turn)\n- On Clash Win, heal 5 SP (2 times per turn)\n · At max SP, remove 1 removable negative effect applied to self\n- At Base Skill End, deal Pride damage equal to 10% of damage the said Skill dealt to each enemy\n\n- When this unit takes damage that brings its HP down to 0, it does not take damage for the turn (once per Encounter)\n · After the above effect activates, heal all HP next turn; then, deal +10% damage for every Protection on self until Combat End (max 80%)
   PL: - Na początku tury zyskuje 2 Ochrony i 1 Wzrost Mocy Ataku\n- Przy użyciu Umiejętności obrony zyskuje 3 Wzrosty Mocy Obrony (1 na turę)\n- Po wygranym Starciu odzyskuje 5 Poczytalności (2 na turę)\n · Przy maks. Poczytalności usuwa 1 usuwalny negatywny efekt nakładony na siebie\n- Po zakończeniu podstawowej Umiejętności zadaje każdemu wrogowi obrażenia Pychą równe 10% obrażeń zadanych przez nią\n\n- Gdy otrzymuje obrażenia obniżające jego HP do 0, nie przyjmuje ich w tej turze (1 na spotkanie)\n · W następnej turze po wywołaniu tego efektu w pełni leczy HP, a do końca walki zadaje +10% obrażeń za każdą Ochronę na sobie (maks. 80%)
190. [Status [EmbeddedSpearhead] — nazwa] 박힌 창날
   źródło: Bufs-walpu10.json :: dataList[id=EmbeddedSpearhead].name
   kontekst: identyfikator statusu w tekstach: `[EmbeddedSpearhead]`
   limit: do 40 znaków
   EN: Embedded Spearhead
   PL: Wbite Ostrze Włóczni
191. [Status [EmbeddedSpearhead] — opis] - 최댓값: 1\n- 이 효과를 부여한 대상 이외의 대상에게 관통 기본 공격 스킬로 크리티컬 피격 시, 받는 피해량 +15%\n- '연' 효과가 있는 스킬로 피격 시, 받는 피해량 + 20% 추가\n- 피격한 스킬 종료 후 소멸
   źródło: Bufs-walpu10.json :: dataList[id=EmbeddedSpearhead].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- On Crit using Pierce Base Attack Skills by targets other than the target that inflicted this effect, take +15% damage\n- When hit by Skills that have the "Joint Combo" effect, take an additional +20% damage\n- At Skill End of the Skill that hit, expires
   PL: - Maks. stosów: 1\n- Gdy krytycznie trafi ją podstawowa Umiejętność ataku Przebicia od celu innego niż ten, który nałożył ten efekt, otrzymuje +15% obrażeń\n- Przy trafieniu Umiejętnością z efektem „Łączenia” otrzymuje dodatkowo +20% obrażeń\n- Znika po zakończeniu Umiejętności, która trafiła
192. [Status [WalpuTenWedgeOffice] — nazwa] 쐐기 사무소
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenWedgeOffice].name
   kontekst: identyfikator statusu w tekstach: `[WalpuTenWedgeOffice]`
   limit: do 40 znaków
   EN: Wedge Office
   PL: Biuro Klinów
193. [Status [WalpuTenWedgeOffice] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 증가\n- 수치가 3이면, 턴 시작 시 관통 피해량 증가 1 얻음\n- 턴 시작 시 자신을 제외하고 ‘쐐기 사무소’를 보유한 아군이 모두 사망했으면 소멸
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenWedgeOffice].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack\n- Turn Start: At 3 Stacks, gain 1 Pierce DMG Up\n- Turn Start: If all other allies that have "Wedge Office" are defeated, this effect expires
   PL: - Maks. stosów: 3\n- Poziom Ataku +1 za każdy stos\n- Od 3 stosów: na początku tury zyskuje 1 Wzrost Obrażeń Przebicia\n- Na początku tury, jeśli wszyscy inni sojusznicy z „Biurem Klina” nie żyją, efekt znika
194. [Status [WalpuTenComboWedge] — nazwa] 승기
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenComboWedge].name
   kontekst: identyfikator statusu w tekstach: `[WalpuTenComboWedge]`
   limit: do 40 znaków
   EN: Momentum
   PL: Przewaga
195. [Status [WalpuTenComboWedge] — opis] - 최댓값 : 30\n- 특정 스킬에서 소모\n- 턴당 최대 20까지 얻을 수 있음
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenComboWedge].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Consumed by certain Skills\n- Can gain up to 20 Stacks per turn
   PL: - Maks. stosów: 30\n- Zużywana przez określone Umiejętności\n- Można zyskać do 20 stosów na turę
196. [Status [WalpuTenBattleFieldKnow] — nazwa] 전장 파악
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenBattleFieldKnow].name
   kontekst: identyfikator statusu w tekstach: `[WalpuTenBattleFieldKnow]`
   limit: do 40 znaków
   EN: Field Analysis
   PL: Ocena Pola Walki
197. [Status [WalpuTenBattleFieldKnow] — opis] - 최대값: 4\n- 이 효과를 얻을 때, 자신의 호흡 횟수 2 증가\n- 턴 종료 시 (수치 x 2)만큼 자신의 호흡 횟수 증가\n- 이 효과 수치에 따라 스킬이 아래 효과 얻음\n· 1 ~ : 적에게 가하는 피해량 +(수치 x 2.5)%\n· 2 ~ : 합 진행 시 2합당, 합 위력 +1 (최대 2)\n· 3 ~ : 코인 위력 +1, 마지막 코인이 파괴 불가 코인이 됨\n· 4 ~ : 공격 종료 시까지 공격 대상의 관통 내성 +0.1
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenBattleFieldKnow].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Gain +2 Poise Count when gaining this effect\n- Turn End: Gain +(Stack x 2) Poise Count\n- Skills gain the following effects based on Stack:\n · 1+: Deal +(Stack x 2.5)% damage against enemies\n · 2+: In a Clash, Clash Power +1 for every 2 Clashes (max 2)\n · 3+: Coin Power +1, the final Coin becomes Unbreakable Coin\n · 4+: Target's Pierce Resist. +0.1 until Attack End
   PL: - Maks. stosów: 4\n- Przy uzyskaniu tego efektu zyskuje +2 Licznika Oddechu\n- Na koniec tury zyskuje +(stosy x 2) Licznika Oddechu\n- Według liczby stosów Umiejętności zyskują:\n · Od 1: +(stosy x 2,5)% obrażeń zadanych wrogom\n · Od 2: podczas Starcia Moc Starcia +1 za każde 2 Starcia (maks. 2)\n · Od 3: Moc Monet +1, a ostatnia moneta staje się monetą niezniszczalną\n · Od 4: do końca ataku Odporność celu na Przebicie +0,1
198. [Status [WalpuTenWedgeMarkSilver] — nazwa] 은색 표식[쐐기]
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenWedgeMarkSilver].name
   kontekst: identyfikator statusu w tekstach: `[WalpuTenWedgeMarkSilver]`
   limit: do 40 znaków
   EN: Silver Mark [Wedge]
   PL: Srebrne Oznaczenie [Klin]
199. [Status [WalpuTenWedgeMarkSilver] — opis] - 최댓값 : 5\n- 턴 종료 시 자신의 진동 횟수 1 증가\n- 턴 시작 시 전장에 적 진영에 쐐기 사무소 소속이 없으면, 이 효과 소멸
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenWedgeMarkSilver].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn End: Gain +1 Tremor Count\n- Turn Start: If there are no "Wedge Office" enemies on the field, this effect expires
   PL: - Maks. stosów: 5\n- Na koniec tury zyskuje +1 Licznika Wstrząsu\n- Na początku tury, jeśli na polu nie ma wrogów z „Biura Klina”, efekt znika
200. [Status [WalpuTenWedgeMarkGold] — nazwa] 금색 표식[쐐기]
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenWedgeMarkGold].name
   kontekst: identyfikator statusu w tekstach: `[WalpuTenWedgeMarkGold]`
   limit: do 40 znaków
   EN: Golden Mark [Wedge]
   PL: Złote Oznaczenie [Klin]
201. [Status [WalpuTenWedgeMarkGold] — opis] - 최댓값 : 5\n- 턴 종료 시 자신의 진동 횟수 1 증가\n- 턴 시작 시 전장에 적 진영에 쐐기 사무소 소속이 없으면, 이 효과 소멸
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenWedgeMarkGold].desc
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Status [DawnOfficeStigmaSOne] — nazwa] 새벽불
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSOne].name
   kontekst: identyfikator statusu w tekstach: `[DawnOfficeStigmaSOne]`
   limit: do 40 znaków
   EN: Light of Daybreak
   PL: Płomień Świtu
203. [Status [DawnOfficeStigmaSOne] — opis] - 최댓값 : 30\n- 턴 시작 시 수치 5당 화상을 1 얻음\n- 턴 시작 시 수치 10당 자신의 화상 횟수 1 증가\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSOne].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn Start: Gain 1 Burn for every 5 Stacks\n- Turn Start: Gain +1 Burn Count for every 10 Stacks\n- At 10+ Stacks, inflict +1 more Burn Potency using Base Skills against the enemy\n- At 20+ Stacks, inflict +1 more Burn Count using Base Skills against the enemy
   PL: - Maks. stosów: 30\n- Na początku tury zyskuje 1 Podpalenie za każde 5 stosów\n- Na początku tury zyskuje +1 Licznika Podpalenia za każde 10 stosów\n- Od 10 stosów podstawowe Umiejętności nadają wrogom +1 więcej Mocy Podpalenia\n- Od 20 stosów podstawowe Umiejętności nadają wrogom +1 więcej Licznika Podpalenia
204. [Status [DawnOfficeStigmaSOne] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSOne].flavor
   limit: do 120 znaków
   EN: The first flare of dawn is not a fire that scorches, but one that casts its glow on people.
   PL: Płomień, który rozświetla świt, nie jest ogniem, co pali, lecz ogniem, co oświetla ludzi.
205. [Status [DawnOfficeStigmaSTwo] — nazwa] 새벽불
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSTwo].name
   kontekst: identyfikator statusu w tekstach: `[DawnOfficeStigmaSTwo]`
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Status [DawnOfficeStigmaSTwo] — opis] - 최댓값 : 30\n- 턴 시작 시 수치 5당 화상을 1 얻음\n- 턴 시작 시 수치 10당 자신의 화상 횟수 1 증가\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSTwo].desc
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Status [DawnOfficeStigmaSTwo] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSTwo].flavor
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Status [DawnOfficeStigmaSThree] — nazwa] 새벽불
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSThree].name
   kontekst: identyfikator statusu w tekstach: `[DawnOfficeStigmaSThree]`
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Status [DawnOfficeStigmaSThree] — opis] - 최댓값 : 30\n- 턴 시작 시 수치 5당 화상을 1 얻음\n- 턴 시작 시 수치 10당 자신의 화상 횟수 1 증가\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSThree].desc
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Status [DawnOfficeStigmaSThree] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaSThree].flavor
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Status [DawnOfficeStigmaYOne] — nazwa] 불꽃나비의 관
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYOne].name
   kontekst: identyfikator statusu w tekstach: `[DawnOfficeStigmaYOne]`
   limit: do 40 znaków
   EN: Fire Butterfly Coffin
   PL: Trumna Ognistych Motyli
212. [Status [DawnOfficeStigmaYOne] — opis] - 최댓값 : 30\n- 기본 스킬 적중시 3 얻음\n· 새벽 사무소 - 선배 패시브로 사용하는 스킬 1이면, 1 추가로 얻음\n· 대상에게 화상이 있으면, 1 추가로 얻음\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYOne].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- On Hit using Base Skills, gain 3 Stacks\n · If the said Skill is Skill 1 used via the "Dawn Office - Seonbae" Passive, gain 1 more Stack\n · If target has Burn, gain 1 more Stack\n- Turn End: At more than 20 Stacks, gain (excess Stack / 2) Burn next turn (rounded down)\n · At 30 Stacks, gain 5 Burn and +2 Burn Count instead
   PL: - Maks. stosów: 30\n- Przy trafieniu podstawową Umiejętnością zyskuje 3 stosy\n · Jeśli to Umiejętność 1 użyta przez pasyw „Biuro Świtu - Seonbae”, dodatkowo +1 stos\n · Jeśli cel ma Podpalenie, dodatkowo +1 stos\n- Na koniec tury, powyżej 20 stosów, w następnej turze otrzymuje Podpalenie równe połowie nadwyżki (zaokrąglone w dół)\n · Przy 30 stosach zamiast tego otrzymuje 5 Podpalenia i +2 Licznika Podpalenia
213. [Status [DawnOfficeStigmaYOne] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n\n“필립, 너에겐 아직 이른 무기지만, 특성을 미리 공부하는 것도 괜찮겠네..”\n“관 속에 있는 여러 칼날 덕에 여러 명을 상대할 때 편해. 보통은 혼자 수행하기 어려운 의뢰도 맡을 수 있고.”
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYOne].flavor
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heated to a smoldering temperature within the coffin are butterflies, the kaleidoscope spilling forth to melt and tear the target apart.\n\n"This type of weapon is still too premature for you to wield, Philip, but it shouldn't hurt to at least learn how it works."\n\n"All those blades inside the coffin make it much easier to deal with multiple opponents at once. That way, you can even take on jobs that would normally be too much for a single Fixer to handle."
   PL: Rozgrzane do żaru w trumnie motyle wylatują rojem i topią, rozrywając cel.\n\n“Philipie, to broń jeszcze zbyt wczesna dla ciebie, ale poznanie jej działania z wyprzedzeniem niczego nie zaszkodzi.”\n“Dzięki ostrzom ukrytym w trumnie łatwiej radzę sobie z wieloma przeciwnikami naraz. Mogę nawet przyjmować zlecenia, z którymi pojedynczy Fixer zwykle sobie nie poradzi.”
214. [Status [DawnOfficeStigmaYTwo] — nazwa] 불꽃나비의 관
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYTwo].name
   kontekst: identyfikator statusu w tekstach: `[DawnOfficeStigmaYTwo]`
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Status [DawnOfficeStigmaYTwo] — opis] - 최댓값 : 30\n- 기본 스킬 적중시 3 얻음\n· 새벽 사무소 - 선배 패시브로 사용하는 스킬 1이면, 1 추가로 얻음\n· 대상에게 화상이 있으면, 1 추가로 얻음\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYTwo].desc
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Status [DawnOfficeStigmaYTwo] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n\n“필립, 너에겐 아직 이른 무기지만, 특성을 미리 공부하는 것도 괜찮겠네..”\n“관 속에 있는 여러 칼날 덕에 여러 명을 상대할 때 편해. 보통은 혼자 수행하기 어려운 의뢰도 맡을 수 있고.”
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYTwo].flavor
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Status [DawnOfficeStigmaYThree] — nazwa] 불꽃나비의 관
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYThree].name
   kontekst: identyfikator statusu w tekstach: `[DawnOfficeStigmaYThree]`
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Status [DawnOfficeStigmaYThree] — opis] - 최댓값 : 30\n- 기본 스킬 적중시 3 얻음\n· 새벽 사무소 - 선배 패시브로 사용하는 스킬 1이면, 1 추가로 얻음\n· 대상에게 화상이 있으면, 1 추가로 얻음\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYThree].desc
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Status [DawnOfficeStigmaYThree] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n\n“필립, 너에겐 아직 이른 무기지만, 특성을 미리 공부하는 것도 괜찮겠네..”\n“관 속에 있는 여러 칼날 덕에 여러 명을 상대할 때 편해. 보통은 혼자 수행하기 어려운 의뢰도 맡을 수 있고.”
   źródło: Bufs-walpu10.json :: dataList[id=DawnOfficeStigmaYThree].flavor
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Status [LoneFixer] — nazwa] 고독한 해결사
   źródło: Bufs-walpu10.json :: dataList[id=LoneFixer].name
   kontekst: identyfikator statusu w tekstach: `[LoneFixer]`
   limit: do 40 znaków
   EN: The Lone Fixer
   PL: Samotny Fixer
221. [Status [LoneFixer] — opis] - 최종 위력 +3\n- 공격 레벨 +3\n- 방어 레벨 +3
   źródło: Bufs-walpu10.json :: dataList[id=LoneFixer].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +3\n- Offense Level +3\n- Defense Level +3
   PL: - Moc Końcowa +3\n- Poziom Ataku +3\n- Poziom Obrony +3
222. [Status [PhilipReady] — nazwa] 타오르는 일격 준비
   źródło: Bufs-walpu10.json :: dataList[id=PhilipReady].name
   kontekst: identyfikator statusu w tekstach: `[PhilipReady]`
   limit: do 40 znaków
   EN: Readying Blazing Strike
   PL: Przygotowanie Płonącego Ciosu
223. [Status [PhilipReady] — opis] {0}턴 후에 타오르는 일격 사용
   źródło: Bufs-walpu10.json :: dataList[id=PhilipReady].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Use "Blazing Strike" after {0} turns
   PL: Po {0} turach używa „Płonącego Ciosu”
224. [Status [PhilipShield] — nazwa] 깃털 방패
   źródło: Bufs-walpu10.json :: dataList[id=PhilipShield].name
   kontekst: identyfikator statusu w tekstach: `[PhilipShield]`
   limit: do 40 znaków
   EN: Feather Shield
   PL: Tarcza z Piór
225. [Status [PhilipShield] — opis] - 피격 시 공격자에게 화상 2 부여\n- 공격으로 받는 피해 5% 감소
   źródło: Bufs-walpu10.json :: dataList[id=PhilipShield].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When hit, inflict 2 Burn on the attacker\n- Take -5% damage from Attack Skills
   PL: - Przy trafieniu nadaje atakującemu 2 Podpalenia\n- Otrzymuje -5% obrażeń od ataków
226. [Status [PhilipSword] — nazwa] 이글거리는 검
   źródło: Bufs-walpu10.json :: dataList[id=PhilipSword].name
   kontekst: identyfikator statusu w tekstach: `[PhilipSword]`
   limit: do 40 znaków
   EN: Searing Sword
   PL: Kipiący Miecz
227. [Status [PhilipSword] — opis] 공격 적중시 대상에게 화상 2 부여
   źródło: Bufs-walpu10.json :: dataList[id=PhilipSword].desc
   limit: do 120 znaków
   EN: On Hit, inflict 2 Burn
   PL: Przy trafieniu nadaje celowi 2 Podpalenia
228. [Status [PhilipPower] — nazwa] 슬픔과 함께 일어설 수 있는 길
   źródło: Bufs-walpu10.json :: dataList[id=PhilipPower].name
   kontekst: identyfikator statusu w tekstach: `[PhilipPower]`
   limit: do 60 znaków
   EN: Getting Back on One's Feet Amid Sadness
   PL: Droga Powstania w Smutku
229. [Status [PhilipPower] — opis] - 자신의 스킬 종료 후 정신력 5 회복\n- 진동을 보유한 적에게 가하는 피해량 +20%\n- 턴 시작시 흐트러짐 상태면, 흐트러짐을 해제하고 해당 턴 동안 자신의 모든 내성을 1.5로 고정함
   źródło: Bufs-walpu10.json :: dataList[id=PhilipPower].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At Skill End, heal 5 SP\n- Deal +20% damage to enemies that have Tremor\n- Turn Start: When Staggered, recover from Stagger; then, all Resist. on self are fixed to 1.5 for the turn
   PL: - Po zakończeniu Umiejętności odzyskuje 5 Poczytalności\n- Zadaje +20% obrażeń wrogom z Wstrząsem\n- Na początku tury, jeśli jest oszołomiony, wychodzi z Oszołomienia, a wszystkie jego Odporności są przez tę turę ustalone na 1,5
230. [Status [PhilipPower] — tekst klimatyczny] ‘그 누구보다 슬퍼하고 있는 나를 위해서…’
   źródło: Bufs-walpu10.json :: dataList[id=PhilipPower].flavor
   limit: do 120 znaków
   EN: 'For me, who's feeling sadder than anyone...'
   PL: ‚…dla mnie, który smuci się bardziej niż ktokolwiek inny…’
231. [Status [PhilipWax] — nazwa] 불확실한 슬픔의 감정
   źródło: Bufs-walpu10.json :: dataList[id=PhilipWax].name
   kontekst: identyfikator statusu w tekstach: `[PhilipWax]`
   limit: do 40 znaków
   EN: Emotion of Uncertain Sorrow
   PL: Emocja Niepewnego Smutku
232. [Status [PhilipWax] — opis] - 최댓값 : 5\n- 수치 1당 화상 위력 최댓값 +10\n· 이 효과 감소 및 소멸 시, 초과되는 화상 위력은 소멸함\n- 수치 1당 화상 발동으로 받는 피해 +10%\n- 화상 발동 시 1 감소
   źródło: Bufs-walpu10.json :: dataList[id=PhilipWax].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Burn Potency Cap +10 for every Stack\n · When this effect expires or is reduced, the surplus Burn Potency expires\n- Take +10% damage from Burn activation for every Stack\n- When Burn activates, lose 1 Stack
   PL: - Maks. stosów: 5\n- Za każdy stos Maks. Moc Podpalenia +10\n · Gdy efekt maleje lub znika, nadwyżka Mocy Podpalenia znika\n- Za każdy stos otrzymuje +10% obrażeń przy aktywacji Podpalenia\n- Przy aktywacji Podpalenia traci 1 stos
233. [Status [PatronLibrarianofHistorysPage] — nazwa] 지정 사서 [역사의 층]
   źródło: Bufs-walpu10.json :: dataList[id=PatronLibrarianofHistorysPage].name
   kontekst: identyfikator statusu w tekstach: `[PatronLibrarianofHistorysPage]`
   limit: do 50 znaków
   EN: Patron Librarian [Floor of History]
   PL: Wyznaczony Bibliotekarz [Piętro Historii]
234. [Status [PatronLibrarianofHistorysPage] — opis] - 해당 캐릭터의 슬롯 +1, 1스킬 수량 -1, 3스킬 수량 +1\n- 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동을 부여할 때, 부여값 +1(특수 상태이상 포함)\n- 자신이 스킬로 호흡, 충전(특수 충전)을 얻을 때, 부여값 +1\n- 관통 속성 스킬 사용시 피해량 +30%\n- 스킬 적중시 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 +1 (스킬당 2회)
   źródło: Bufs-walpu10.json :: dataList[id=PatronLibrarianofHistorysPage].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1, lose 1 use of Skill 1, gain 1 use of Skill 3\n- Increase the amount of Burn, Bleed, Rupture, Sinking, or Tremor inflicted using Skills by +1 (including Unique Status Effects)\n- Increase the amount of Poise or Charge (including Unique Charge) gained from Skills by +1\n- Pierce Skills deal +30% damage On Use\n- On Hit using Skills, gain 1 random least-owned E.G.O resource (2 times per Skill)
   PL: - Sloty tej postaci: +1; liczba Umiejętności 1: -1; liczba Umiejętności 3: +1\n- Gdy Umiejętnościami nadaje Podpalenie, Krwawienie, Rozdarcie, Zatonięcie lub Wstrząs, wartość nadania +1 (również szczególne stany)\n- Gdy Umiejętnościami zyskuje Oddech lub Ładowanie (również szczególne ładowanie), wartość +1\n- Umiejętności Przebicia zadają +30% obrażeń przy użyciu\n- Przy trafieniu Umiejętnością zyskuje +1 losowego zasobu E.G.O, którego ma najmniej (2 na Umiejętność)
235. [Status [EmotionLevelZero] — nazwa] 감정 0단계
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelZero].name
   kontekst: identyfikator statusu w tekstach: `[EmotionLevelZero]`
   limit: do 40 znaków
   EN: Emotion Level 0
   PL: Poziom Emocji 0
236. [Status [EmotionLevelZero] — opis] - 최댓값 : 30\n- 화상 효과로 받는 피해량 -75% (소수점 버림)\n- 모든 아군의 감정 단계 수치가 9가 될 때까지 9 초과로 증가하지 않음\n- 합 승리 시, 코인 앞면 적중 시, 적 처치 시 3 증가\n- 합 패배, 코인 뒷면 적중 시, 아군 사망 시 1 증가\n- 턴 종료시 모든 아군의 감정 단계 수치가 9면, 1 추가로 얻고 감정 단계 증가
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelZero].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Take -75% damage from Burn effects (rounded down)\n- Does not increase beyond 9 Stacks until all allies are at 9 Emotion Level Stacks\n- Gain 3 Stacks On Clash Win, On Heads Hit, and On Kill\n- Gain 1 Stack On Clash Lose, On Tails Hit, and on Ally Death\n- Turn End: If all allies are at 9 Emotion Level Stacks, gain 1 more Stack and increase Emotion Level stage
   PL: - Maks. stosów: 30\n- Otrzymuje -75% obrażeń od efektów Podpalenia (zaokrąglone w dół)\n- Nie rośnie powyżej 9 stosów, dopóki wszyscy sojusznicy nie osiągną 9 stosów Poziomu Emocji\n- +3 stosy po wygranym Starciu, trafieniu awersem monety i zabiciu wroga\n- +1 stos po przegranej w Starciu, trafieniu rewersem monety i śmierci sojusznika\n- Na koniec tury, jeśli wszyscy sojusznicy mają 9 stosów Poziomu Emocji, zyskuje +1 stos i przechodzi do kolejnego etapu emocji
237. [Status [EmotionLevelOne] — nazwa] 감정 1단계
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelOne].name
   kontekst: identyfikator statusu w tekstach: `[EmotionLevelOne]`
   limit: do 40 znaków
   EN: Emotion Level 1
   PL: Poziom Emocji 1
238. [Status [EmotionLevelOne] — opis] - 최댓값 : 30\n- 최종 위력 +1\n- 화상 효과로 받는 피해량 -75% (소수점 버림)\n- 모든 아군의 감정 단계 수치가 19가 될 때까지 19 초과로 증가하지 않음\n- 합 승리 시, 코인 앞면 적중 시, 적 처치 시 3 증가\n- 합 패배, 코인 뒷면 적중 시, 아군 사망 시 1 증가\n- 턴 종료시 모든 아군의 감정 단계 수치가 19면, 1 추가로 얻고 감정 단계 증가\n\n[지정 사서 전용 효과]\n- 재 : 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelOne].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Final Power +1\n- Take -75% damage from Burn effects (rounded down)\n- Does not increase beyond 19 Stacks until all allies are at 19 Emotion Level Stacks\n- Gain 3 Stacks On Clash Win, On Heads Hit, and On Kill\n- Gain 1 Stack On Clash Lose, On Tails Hit, and on Ally Death\n- Turn End: If all allies are at 19 Emotion Level Stacks, gain 1 more Stack and increase Emotion Level stage\n\n[Patron Librarian Exclusive Effect]\n- Ashes: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)
   PL: - Maks. stosów: 30\n- Moc Końcowa +1\n- Otrzymuje -75% obrażeń od efektów Podpalenia (zaokrąglone w dół)\n- Nie rośnie powyżej 19 stosów, dopóki wszyscy sojusznicy nie osiągną 19 stosów Poziomu Emocji\n- +3 stosy po wygranym Starciu, trafieniu awersem monety i zabiciu wroga\n- +1 stos po przegranej w Starciu, trafieniu rewersem monety i śmierci sojusznika\n- Na koniec tury, jeśli wszyscy sojusznicy mają 19 stosów Poziomu Emocji, zyskuje +1 stos i przechodzi do kolejnego etapu emocji\n\n[Efekt wyznaczonego Bibliotekarza]\n- Popiół: przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)
239. [Status [EmotionLevelTwo] — nazwa] 감정 2단계
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelTwo].name
   kontekst: identyfikator statusu w tekstach: `[EmotionLevelTwo]`
   limit: do 40 znaków
   EN: Emotion Level 2
   PL: Poziom Emocji 2
240. [Status [EmotionLevelTwo] — opis] - 최댓값 : 30\n- 최종 위력 +2\n- 화상 효과로 받는 피해량 -75% (소수점 버림)\n- 모든 아군의 감정 단계 수치가 29가 될 때까지 29 초과로 증가하지 않음\n- 합 승리 시, 코인 앞면 적중 시, 적 처치 시 3 증가\n- 합 패배, 코인 뒷면 적중 시, 아군 사망 시 1 증가\n- 턴 종료시 모든 아군의 감정 단계 수치가 29면, 1 추가로 얻고 감정 단계 증가\n\n[지정 사서 전용 효과]\n- 재 : 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)\n- 그리웠던 옛날의 포옹 : 합 승리 시 20% 확률로 대상에게 진동 폭발. 동일한 대상과 합을 할수록 확률이 증가함 (1합당 2%, 최대 50%)
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelTwo].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Final Power +2\n- Take -75% damage from Burn effects (rounded down)\n- Does not increase beyond 29 Stacks until all allies are at 29 Emotion Level Stacks\n- Gain 3 Stacks On Clash Win, On Heads Hit, and On Kill\n- Gain 1 Stack On Clash Lose, On Tails Hit, and on Ally Death\n- Turn End: If all allies are at 29 Emotion Level Stacks, gain 1 more Stack and increase Emotion Level stage\n\n[Patron Librarian Exclusive Effect]\n- Ashes: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)\n- Nostalgic Embrace of the Old Days: On Clash Win, 20% chance to trigger Tremor Burst on target; chance increases with every Clash against the same target (2% for every Clash, max 50%)
   PL: - Maks. stosów: 30\n- Moc Końcowa +2\n- Otrzymuje -75% obrażeń od efektów Podpalenia (zaokrąglone w dół)\n- Nie rośnie powyżej 29 stosów, dopóki wszyscy sojusznicy nie osiągną 29 stosów Poziomu Emocji\n- +3 stosy po wygranym Starciu, trafieniu awersem monety i zabiciu wroga\n- +1 stos po przegranej w Starciu, trafieniu rewersem monety i śmierci sojusznika\n- Na koniec tury, jeśli wszyscy sojusznicy mają 29 stosów Poziomu Emocji, zyskuje +1 stos i przechodzi do kolejnego etapu emocji\n\n[Efekt wyznaczonego Bibliotekarza]\n- Popiół: przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)\n- Tęskny Uścisk Dawnych Dni: po wygranym Starciu 20% szans na wywołanie Wybuchu Wstrząsu u celu; szansa rośnie z każdym Starciem z tym samym celem (2% na Starcie, maks. 50%)
241. [Status [EmotionLevelThree] — nazwa] 감정 3단계
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelThree].name
   kontekst: identyfikator statusu w tekstach: `[EmotionLevelThree]`
   limit: do 40 znaków
   EN: Emotion Level 3
   PL: Poziom Emocji 3
242. [Status [EmotionLevelThree] — opis] - 최댓값 : 30\n- 최종 위력 +3\n- 화상 효과로 받는 피해량 -75% (소수점 버림)\n\n[지정 사서 전용 효과]\n- 재 : 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)\n- 그리웠던 옛날의 포옹 : 합 승리 시 20% 확률로 대상에게 진동 폭발. 동일한 대상과 합을 할수록 확률이 증가함 (1합당 2%, 최대 50%)\n- 식탐 : 자신의 공격 대상이 이번 턴에 피해를 받았다면, 적중 시 피해량이 1-3 증가하고, 체력을 2-5 회복함
   źródło: Bufs-walpu10.json :: dataList[id=EmotionLevelThree].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Final Power +3\n- Take -75% damage from Burn effects (rounded down)\n\n[Patron Librarian Exclusive Effect]\n- Ashes: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)\n- Nostalgic Embrace of the Old Days: On Clash Win, 20% chance to trigger Tremor Burst on target; chance increases with every Clash against the same target (2% for every Clash, max 50%)\n- Gluttony: If this unit's attack target has taken damage this turn, deal 1-3 additional damage On Hit and heal 2-5 HP
   PL: - Maks. stosów: 30\n- Moc Końcowa +3\n- Otrzymuje -75% obrażeń od efektów Podpalenia (zaokrąglone w dół)\n\n[Efekt wyznaczonego Bibliotekarza]\n- Popiół: przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)\n- Tęskny Uścisk Dawnych Dni: po wygranym Starciu 20% szans na wywołanie Wybuchu Wstrząsu u celu; szansa rośnie z każdym Starciem z tym samym celem (2% na Starcie, maks. 50%)\n- Łakomstwo: jeśli cel ataku tej jednostki otrzymał w tej turze obrażenia, przy trafieniu zadaje 1–3 dodatkowych obrażeń i odzyskuje 2–5 HP
243. [Status [WalpuTenHard] — nazwa] 어려움 난이도
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenHard].name
   kontekst: identyfikator statusu w tekstach: `[WalpuTenHard]`
   limit: do 40 znaków
   EN: Hard Difficulty
   PL: Poziom Trudności: Trudny
244. [Status [WalpuTenHard] — opis] - 최대 체력 50% 증가\n- 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제\n- 공격 레벨 +3\n- 화상, 출혈, 진동, 파열, 침잠의 위력이 최대 30까지 누적되고 횟수는 최대 10까지 누적됨\n- 출혈, 진동, 파열, 침잠으로 받는 피해량 -30%
   źródło: Bufs-walpu10.json :: dataList[id=WalpuTenHard].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +50%\n- Remove the first Stagger Threshold\n- Offense Level +3\n- Max Potency cap for Burn, Bleed, Tremor, Rupture, Sinking: 30\n- Max Count cap for Burn, Bleed, Tremor, Rupture, Sinking: 10\n- Take -30% damage from Bleed, Tremor, Rupture, Sinking
   PL: - Maks. HP +50%\n- Usuwa pierwszy Próg Oszołomienia\n- Poziom Ataku +3\n- Maks. Mocy Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia: 30\n- Maks. Liczników Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia: 10\n- Otrzymuje -30% obrażeń od Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia
245. [Status [HistoryAshes] — nazwa] 도서관의 책장 - 재
   źródło: Bufs-walpu10.json :: dataList[id=HistoryAshes].name
   kontekst: identyfikator statusu w tekstach: `[HistoryAshes]`
   limit: do 40 znaków
   EN: Pages of the Library - Ashes
   PL: Karta Biblioteki - Popiół
246. [Status [HistoryAshes] — opis] 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)
   źródło: Bufs-walpu10.json :: dataList[id=HistoryAshes].desc
   limit: do 200 znaków
   EN: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)
   PL: Przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)
247. [Status [HistoryAshes] — tekst klimatyczny] “까맣게 타버린 몸은 그 아이의 부서진 희망, 그럼에도 여전히 타오르는 촛불은 애정을 갈구하는 집착이라고 볼 수 있습니다.”
   źródło: Bufs-walpu10.json :: dataList[id=HistoryAshes].flavor
   limit: do 170 znaków
   EN: "The charred body represents the child's crumbled hope, while the ever-blazing flame represents the obsession for affection."
   PL: “Zwęglone ciało wyobraża rozpadłe nadzieje dziecka, a wiecznie płonący płomień — obsesję pragnącą czułości.”
248. [Status [HistoryNostalgicEmbraceOfTheOldDays] — nazwa] 도서관의 책장 - 그리웠던 옛날의 포옹
   źródło: Bufs-walpu10.json :: dataList[id=HistoryNostalgicEmbraceOfTheOldDays].name
   kontekst: identyfikator statusu w tekstach: `[HistoryNostalgicEmbraceOfTheOldDays]`
   limit: do 80 znaków
   EN: Pages of the Library - Nostalgic Embrace of the Old Days
   PL: Karta Biblioteki - Tęskny Uścisk Dawnych Dni
249. [Status [HistoryNostalgicEmbraceOfTheOldDays] — opis] 합 승리 시 20% 확률로 대상에게 진동 폭발. 동일한 대상과 합을 할수록 확률이 증가함 (1합당 2%, 최대 50%)
   źródło: Bufs-walpu10.json :: dataList[id=HistoryNostalgicEmbraceOfTheOldDays].desc
   limit: do 190 znaków
   EN: On Clash Win, 20% chance to trigger Tremor Burst on target; chance increases with every Clash against the same target (2% for every Clash, max 50%)
   PL: Po wygranym Starciu 20% szans na wywołanie Wybuchu Wstrząsu u celu; szansa rośnie z każdym Starciem z tym samym celem (2% na Starcie, maks. 50%)
250. [Status [HistoryNostalgicEmbraceOfTheOldDays] — tekst klimatyczny] 테디가 누군가를 꽉 껴안고 있었죠. 테디는 포옹을 매우 좋아했거든요. 그런데 조금 이상했어요.
   źródło: Bufs-walpu10.json :: dataList[id=HistoryNostalgicEmbraceOfTheOldDays].flavor
   limit: do 120 znaków
   EN: Teddy was hugging someone tightly. Teddy loved hugs. But something was odd.
   PL: Teddy mocno przytulał kogoś. Teddy bardzo lubił przytulanie. Ale coś było w tym dziwnego.
251. [Status [HistoryGluttony] — nazwa] 도서관의 책장 - 식탐
   źródło: Bufs-walpu10.json :: dataList[id=HistoryGluttony].name
   kontekst: identyfikator statusu w tekstach: `[HistoryGluttony]`
   limit: do 50 znaków
   EN: Pages of the Library - Gluttony
   PL: Karta Biblioteki - Łakomstwo
252. [Status [HistoryGluttony] — opis] 자신의 공격 대상이 이번 턴에 피해를 받았다면, 적중 시 피해량이 1-3 증가하고, 체력을 2-5 회복함
   źródło: Bufs-walpu10.json :: dataList[id=HistoryGluttony].desc
   limit: do 140 znaków
   EN: If this unit's attack target has taken damage this turn, deal 1-3 additional damage On Hit and heal 2-5 HP
   PL: Jeśli cel ataku otrzymał w tej turze obrażenia, przy trafieniu zadaje 1–3 obrażeń dodatkowych i leczy 2–5 HP
253. [Status [HistoryGluttony] — tekst klimatyczny] 요정들은 단지 고기를 좋아하는 괴물이었고, '보호하는' 행위는 고기의 신선도가 떨어지는 걸 방지하기 위해서였다.
   źródło: Bufs-walpu10.json :: dataList[id=HistoryGluttony].flavor
   limit: do 150 znaków
   EN: The fairies were no more than carnivorous monsters, and their "protection" was their method to keep the meat fresh.
   PL: Wróżki były jedynie mięsożernymi potworami, a ich „ochrona” służyła utrzymaniu świeżości mięsa.
254. [Status [DawnOffice_LowMorale] — nazwa] 새벽 사무소
   źródło: Bufs-walpu10.json :: dataList[id=DawnOffice_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DawnOffice_LowMorale]`
   limit: do 40 znaków
   EN: Dawn Office
   PL: Biuro Świtu
255. [Status [DawnOffice_LowMorale] — opis] - 사기 저하\n- 화상이 있는 적에게 가하는 피해량 -5%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +5%
   źródło: Bufs-walpu10.json :: dataList[id=DawnOffice_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal -5% damage to enemies that have Burn\n- +5% to Stagger Threshold raised against enemies that have Tremor
   PL: - Spadek Moralu\n- Zadaje -5% obrażeń wrogom z Podpaleniem\n- +5% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
256. [Status [DawnOffice_Panic] — nazwa] 새벽 사무소
   źródło: Bufs-walpu10.json :: dataList[id=DawnOffice_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DawnOffice_Panic]`
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Status [DawnOffice_Panic] — opis] - 패닉\n- 화상이 있는 적에게 가하는 피해량 -10%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +10%
   źródło: Bufs-walpu10.json :: dataList[id=DawnOffice_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal -10% damage to enemies that have Burn\n- +10% to Stagger Threshold raised against enemies that have Tremor
   PL: - Panika\n- Zadaje -10% obrażeń wrogom z Podpaleniem\n- +10% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
258. [Status [WedgeOffice_LowMorale] — nazwa] 쐐기 사무소
   źródło: Bufs-walpu10.json :: dataList[id=WedgeOffice_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[WedgeOffice_LowMorale]`
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Status [WedgeOffice_LowMorale] — opis] - 사기 저하\n- 크리티컬 피해량 -5%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +5%
   źródło: Bufs-walpu10.json :: dataList[id=WedgeOffice_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal -5% damage on Critical hit\n- +5% to Stagger Threshold raised against enemies that have Tremor
   PL: - Spadek Moralu\n- Zadaje -5% obrażeń krytycznych\n- +5% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
260. [Status [WedgeOffice_Panic] — nazwa] 쐐기 사무소
   źródło: Bufs-walpu10.json :: dataList[id=WedgeOffice_Panic].name
   kontekst: identyfikator statusu w tekstach: `[WedgeOffice_Panic]`
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Status [WedgeOffice_Panic] — opis] - 패닉\n- 크리티컬 피해량 -10%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +10%
   źródło: Bufs-walpu10.json :: dataList[id=WedgeOffice_Panic].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal -10% damage on Critical Hit\n- +10% to Stagger Threshold raised against enemies that have Tremor
   PL: - Panika\n- Zadaje -10% obrażeń krytycznych\n- +10% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
262. [Status [WaxWing_LowMorale] — nazwa] 밀랍날개
   źródło: Bufs-walpu10.json :: dataList[id=WaxWing_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[WaxWing_LowMorale]`
   limit: do 40 znaków
   EN: Waxen Pinion
   PL: Woskowe Skrzydło
263. [Status [WaxWing_LowMorale] — opis] - 사기 저하\n- 취약 1 얻음\n- 화상이 있는 적에게 가하는 피해량 +10%
   źródło: Bufs-walpu10.json :: dataList[id=WaxWing_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile\n- Deal +10% damage to enemies that have Burn
   PL: - Spadek Moralu\n- Zyskuje 1 Wrażliwość\n- Zadaje +10% obrażeń wrogom z Podpaleniem
264. [Status [WaxWing_Panic] — nazwa] 밀랍날개
   źródło: Bufs-walpu10.json :: dataList[id=WaxWing_Panic].name
   kontekst: identyfikator statusu w tekstach: `[WaxWing_Panic]`
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Status [WaxWing_Panic] — opis] - 패닉\n- 취약 1 얻음\n- 화상이 있는 적에게 가하는 피해량 +25%
   źródło: Bufs-walpu10.json :: dataList[id=WaxWing_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile\n- Deal +25% damage to enemies that have Burn
   PL: - Panika\n- Zyskuje 1 Wrażliwość\n- Zadaje +25% obrażeń wrogom z Podpaleniem

## Statusy i efekty bojowe — Bufs-walpu4
- plik gry: `Bufs-walpu4.json`

266. [Status [RedEyeFirst] — nazwa] 적안
   źródło: Bufs-walpu4.json :: dataList[id=RedEyeFirst].name
   kontekst: identyfikator statusu w tekstach: `[RedEyeFirst]`
   limit: do 40 znaków
   EN: Red Eyes
   PL: Czerwone Oko
267. [Status [RedEyeFirst] — opis] - 기본 스킬 코인 효과의 출혈 부여 값 +1\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 적안\n· 2단계 (8~15) : 적안 - 경계\n· 3단계 (16~20) : 적안 - 포식\n- 버프를 강화하면 기본 스킬 코인 효과의 출혈 부여량이 강화 단계만큼 증가 (최대 3)
   źródło: Bufs-walpu4.json :: dataList[id=RedEyeFirst].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skill Coin effects inflict +1 more Bleed\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Red Eyes\n· Stage 2 (8~15) : Red Eyes - Alert\n· Stage 3 (16~20) : Red Eyes - Devouring\n- The amount of additional bleed inflicted by the first line of this buff is equal to the buff enhancement Stage (max 3)
   PL: - Podstawowe monety Umiejętności ataku nadają +1 więcej Krwawienia\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Czerwone Oko\n · Etap 2 (8–15): Czerwone Oko - Czujność\n · Etap 3 (16–20): Czerwone Oko - Pożeranie\n- Pierwsza linia tego wzmocnienia nadaje dodatkowe Krwawienie równe etapowi wzmocnienia (maks. 3)
268. [Status [RedEyeSecond] — nazwa] 적안 - 경계
   źródło: Bufs-walpu4.json :: dataList[id=RedEyeSecond].name
   kontekst: identyfikator statusu w tekstach: `[RedEyeSecond]`
   limit: do 40 znaków
   EN: Red Eyes - Alert
   PL: Czerwone Oko - Czujność
269. [Status [RedEyeSecond] — opis] - 기본 스킬 코인 효과의 출혈 부여 값 +2\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 적안\n· 2단계 (8~15) : 적안 - 경계\n· 3단계 (16~20) : 적안 - 포식\n- 버프를 강화하면 기본 스킬 코인 효과의 출혈 부여량이 강화 단계만큼 증가 (최대 3)
   źródło: Bufs-walpu4.json :: dataList[id=RedEyeSecond].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skill Coin effects inflict +2 more Bleed\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Red Eyes\n· Stage 2 (8~15) : Red Eyes - Alert\n· Stage 3 (16~20) : Red Eyes - Devouring\n- The amount of additional bleed inflicted by the first line of this buff is equal to the buff enhancement Stage (max 3)
   PL: - Podstawowe monety Umiejętności ataku nadają +2 więcej Krwawienia\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Czerwone Oko\n · Etap 2 (8–15): Czerwone Oko - Czujność\n · Etap 3 (16–20): Czerwone Oko - Pożeranie\n- Pierwsza linia tego wzmocnienia nadaje dodatkowe Krwawienie równe etapowi wzmocnienia (maks. 3)
270. [Status [RedEyeThird] — nazwa] 적안 - 포식
   źródło: Bufs-walpu4.json :: dataList[id=RedEyeThird].name
   kontekst: identyfikator statusu w tekstach: `[RedEyeThird]`
   limit: do 40 znaków
   EN: Red Eyes - Devouring
   PL: Czerwone Oko - Pożeranie
271. [Status [RedEyeThird] — opis] - 기본 스킬 코인 효과의 출혈 부여 값 +3\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 적안\n· 2단계 (8~15) : 적안 - 경계\n· 3단계 (16~20) : 적안 - 포식\n- 버프를 강화하면 기본 스킬 코인 효과의 출혈 부여량이 강화 단계만큼 증가 (최대 3)
   źródło: Bufs-walpu4.json :: dataList[id=RedEyeThird].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skill Coin effects inflict +3 more Bleed\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Red Eyes\n· Stage 2 (8~15) : Red Eyes - Alert\n· Stage 3 (16~20) : Red Eyes - Devouring\n- The amount of additional bleed inflicted by the first line of this buff is equal to the buff enhancement Stage (max 3)
   PL: - Podstawowe monety Umiejętności ataku nadają +3 więcej Krwawienia\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Czerwone Oko\n · Etap 2 (8–15): Czerwone Oko - Czujność\n · Etap 3 (16–20): Czerwone Oko - Pożeranie\n- Pierwsza linia tego wzmocnienia nadaje dodatkowe Krwawienie równe etapowi wzmocnienia (maks. 3)
272. [Status [PenanceFirst] — nazwa] 참회
   źródło: Bufs-walpu4.json :: dataList[id=PenanceFirst].name
   kontekst: identyfikator statusu w tekstach: `[PenanceFirst]`
   limit: do 40 znaków
   EN: Penitence
   PL: Skrucha
273. [Status [PenanceFirst] — opis] - 참회를 얻는 기본 스킬 코인 적중 시, 2만큼 정신력 회복\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 턴 시작 시, 최대 체력의 (참회)%만큼 보호막을 얻음\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 참회\n· 2단계 (8~15) : 참회 - 경계\n· 3단계 (16~20) : 참회 - 고해\n- 버프를 강화하면 참회를 얻는 기본 스킬 코인 적중 시, (강화 단계 x 2)만큼 정신력 회복.
   źródło: Bufs-walpu4.json :: dataList[id=PenanceFirst].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 2 SP On Hit with Base Skill Coins that gain Penitence\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Turn Start: gain (Penitence)% of max HP as Shield\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Penitence\n· Stage 2 (8~15) : Penitence - Periphery\n· Stage 3 (16~20) : Penitence - Confession\n- The amount of SP healed by the first line of this buff is based on the enhancement Stage (enhancement Stage x 2)
   PL: - Zyskuje 2 Poczytalności przy trafieniu monetą podstawowej Umiejętności ataku dającej Skruchę\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Na początku tury zyskuje Tarczę równą (Skrucha)% Maks. HP\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Skrucha\n · Etap 2 (8–15): Skrucha - Czujność\n · Etap 3 (16–20): Skrucha - Wyznanie\n- Pierwsza linia tego wzmocnienia leczy Poczytalność według etapu wzmocnienia (etap x 2)
274. [Status [PenanceSecond] — nazwa] 참회 - 경계
   źródło: Bufs-walpu4.json :: dataList[id=PenanceSecond].name
   kontekst: identyfikator statusu w tekstach: `[PenanceSecond]`
   limit: do 40 znaków
   EN: Penitence - Periphery
   PL: Skrucha - Czujność
275. [Status [PenanceSecond] — opis] - 참회를 얻는 기본 스킬 코인 적중 시, 4만큼 정신력 회복\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 턴 시작 시, 최대 체력의 (참회)%만큼 보호막을 얻음\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 참회\n· 2단계 (8~15) : 참회 - 경계\n· 3단계 (16~20) : 참회 - 고해\n- 버프를 강화하면 참회를 얻는 기본 스킬 코인 적중 시, (강화 단계 x 2)만큼 정신력 회복.
   źródło: Bufs-walpu4.json :: dataList[id=PenanceSecond].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 4 SP On Hit with Base Skill Coins that gain Penitence\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Turn Start: gain (Penitence)% of max HP as Shield\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Penitence\n· Stage 2 (8~15) : Penitence - Periphery\n· Stage 3 (16~20) : Penitence - Confession\n- The amount of SP healed by the first line of this buff is based on the enhancement Stage (enhancement Stage x 2)
   PL: - Zyskuje 4 Poczytalności przy trafieniu monetą podstawowej Umiejętności ataku dającej Skruchę\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Na początku tury zyskuje Tarczę równą (Skrucha)% Maks. HP\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Skrucha\n · Etap 2 (8–15): Skrucha - Czujność\n · Etap 3 (16–20): Skrucha - Wyznanie\n- Pierwsza linia tego wzmocnienia leczy Poczytalność według etapu wzmocnienia (etap x 2)
276. [Status [PenanceThird] — nazwa] 참회 - 고해
   źródło: Bufs-walpu4.json :: dataList[id=PenanceThird].name
   kontekst: identyfikator statusu w tekstach: `[PenanceThird]`
   limit: do 40 znaków
   EN: Penitence - Confession
   PL: Skrucha - Wyznanie
277. [Status [PenanceThird] — opis] - 참회를 얻는 기본 스킬 코인 적중 시, 6만큼 정신력 회복\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 턴 시작 시, 최대 체력의 (참회)%만큼 보호막을 얻음\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 참회\n· 2단계 (8~15) : 참회 - 경계\n· 3단계 (16~20) : 참회 - 고해\n- 버프를 강화하면 참회를 얻는 기본 스킬 코인 적중 시, (강화 단계 x 2)만큼 정신력 회복.
   źródło: Bufs-walpu4.json :: dataList[id=PenanceThird].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 6 SP On Hit with Base Skill Coins that gain Penitence\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Turn Start: gain (Penitence)% of max HP as Shield\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Penitence\n· Stage 2 (8~15) : Penitence - Periphery\n· Stage 3 (16~20) : Penitence - Confession\n- The amount of SP healed by the first line of this buff is based on the enhancement Stage (enhancement Stage x 2)
   PL: - Zyskuje 6 Poczytalności przy trafieniu monetą podstawowej Umiejętności ataku dającej Skruchę\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Na początku tury zyskuje Tarczę równą (Skrucha)% Maks. HP\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Skrucha\n · Etap 2 (8–15): Skrucha - Czujność\n · Etap 3 (16–20): Skrucha - Wyznanie\n- Pierwsza linia tego wzmocnienia leczy Poczytalność według etapu wzmocnienia (etap x 2)
278. [Status [Emptiness] — nazwa] 하얗게 태워버렸군
   źródło: Bufs-walpu4.json :: dataList[id=Emptiness].name
   kontekst: identyfikator statusu w tekstach: `[Emptiness]`
   limit: do 40 znaków
   EN: Only Ashes Remain
   PL: Ostały się Tylko Popioły
279. [Status [Emptiness] — opis] - 적안과 참회를 보유할 수 없음\n- 기본 스킬 효과로 적안 획득 시, 자신과 현재 체력 비율이 가장 낮은 아군의 체력을 자신의 최대 체력의 (적안 획득량)%만큼 회복 (턴 당 2회)\n- 기본 스킬 효과로 참회 획득 시, 자신과 현재 정신력이 가장 낮은 아군의 정신력을 (참회 획득량/2)만큼 회복 (턴 당 2회)\n- 턴 종료 시 효과 소멸됨
   źródło: Bufs-walpu4.json :: dataList[id=Emptiness].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Cannot maintain Red Eyes & Penitence\n- When gaining Red Eyes with Base Skill effects, heal self and 1 ally with the lowest HP percentage by (Red Eyes gained)% of this unit's max HP (2 times per turn)\n- When gaining Penitence with Base Skill effects, heal self and 1 ally with the least SP by ((Penitence gained)/2) SP (2 times per turn)\n- Turn End: this effect expires
   PL: - Nie może posiadać Czerwonego Oka ani Skruchy\n- Gdy efektem podstawowej Umiejętności zyskuje Czerwone Oko, leczy siebie i sojusznika z najniższym procentem HP o (uzyskane Czerwone Oko)% własnego Maks. HP (2 na turę)\n- Gdy efektem podstawowej Umiejętności zyskuje Skruchę, leczy siebie i sojusznika z najniższą Poczytalnością o (uzyskana Skrucha/2) Poczytalności (2 na turę)\n- Na koniec tury efekt znika
280. [Status [SinkingWhite] — nazwa] 나비
   źródło: Bufs-walpu4.json :: dataList[id=SinkingWhite].name
   kontekst: identyfikator statusu w tekstach: `[SinkingWhite]`
   limit: do 40 znaków
   EN: Butterfly
   PL: Motyl
281. [Status [SinkingWhite] — opis] - 특수 침잠\n- 기본값 : 0, 최댓값 : 15\n- 피격 시 공격자의 정신력을 {2}만큼 회복.\n- 피격 시 정신력이 0 미만이면, {3}만큼 우울 피해를 받음.\n- 턴 종료 시 이 효과의 죽은나비 0으로 초기화, 이 효과의 산나비(위력)만큼 침잠 부여 후 산나비가 죽은나비(횟수)로 변환.\n- 산나비와 죽은나비가 모두 0이 되면 효과가 제거됨.
   źródło: Bufs-walpu4.json :: dataList[id=SinkingWhite].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: {2}, {3}, \n
   EN: - Unique Sinking\n- Base Value: 0, Max Value: 15\n- When hit, the attacker heals {2} SP.\n- When hit, and if this unit's SP is at less than 0, take {3} Gloom damage.\n- Turn End: Reset The Departed of this effect to 0; gain Sinking equal to The Living(Potency) and convert The Living into The Departed(Count).\n- This effect expires when both The Living and The Departed reach 0.
   PL: - Szczególne Zatonięcie\n- Wartość bazowa: 0, maks.: 15\n- Przy trafieniu atakujący odzyskuje {2} Poczytalności.\n- Przy trafieniu, jeśli Poczytalność jest niższa od 0, otrzymuje {3} obrażeń Posępności.\n- Na koniec tury Martwe Motyle tego efektu resetują się do 0, po czym zyskuje Zatonięcie równe Żywym Motylom (Mocy), a Żywe Motyle stają się Martwymi Motylami (Licznik).\n- Efekt znika, gdy Żywe i Martwe Motyle osiągną 0.
282. [Status [SinkingBlack] — nazwa] 구버전 효과
   źródło: Bufs-walpu4.json :: dataList[id=SinkingBlack].name
   kontekst: identyfikator statusu w tekstach: `[SinkingBlack]`
   limit: do 40 znaków
   EN: !!!OUDATED EFFECT!!!
   PL: Efekt Starej Wersji
283. [Status [BulletLament] — nazwa] 산나비·죽은나비
   źródło: Bufs-walpu4.json :: dataList[id=BulletLament].name
   kontekst: identyfikator statusu w tekstach: `[BulletLament]`
   limit: do 40 znaków
   EN: The Living & The Departed
   PL: Żywe i Martwe Motyle
284. [Status [BulletLament] — opis] - 특수 탄환\n- 위력 + 횟수의 최댓값 : 20\n- 특정 스킬 사용 시 소모.\n- 소모 시 이 효과의 산나비(위력)와 죽은나비(횟수)를 무작위로 소모.\n- 소모 시 수치가 부족한 경우, 공격이 취소됨.
   źródło: Bufs-walpu4.json :: dataList[id=BulletLament].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Potency + Count = Max 20\n- Consumed for certain Skills.\n- When consumed, randomly selected between The Living(Potency) or The Departed(Count).\n- Some attacks cancel if lacking Ammo.
   PL: - Szczególna amunicja\n- Suma Mocy i Licznika: maks. 20\n- Zużywana przez określone Umiejętności.\n- Przy zużyciu losowo zużywa Żywe Motyle (Moc) albo Martwe Motyle (Licznik).\n- Gdy wartości są niewystarczające, atak zostaje anulowany.
285. [Status [TrainTeamCaptain] — nazwa] 교육팀 팀장
   źródło: Bufs-walpu4.json :: dataList[id=TrainTeamCaptain].name
   kontekst: identyfikator statusu w tekstach: `[TrainTeamCaptain]`
   limit: do 40 znaków
   EN: Training Team Captain
   PL: Kapitan Zespołu Szkoleniowego
286. [Status [TrainTeamCaptain] — opis] 해당 캐릭터의 슬롯 +1\n1스킬 수량 -1, 3스킬 수량 +1\n턴 시작 시 정신력 15 회복\n자신이 스킬로 화상, 출혈, 파열, 침잠, 진동을 부여할 때, 부여값 +1(특수 상태이상 포함)\n자신이 스킬로 호흡, 충전(특수 충전)을 얻을 때, 부여값 +1\n적 처치시 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1
   źródło: Bufs-walpu4.json :: dataList[id=TrainTeamCaptain].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Slot +1\nModify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\nTurn Start: heal 15 SP\nIncrease the amount of Burn, Bleed, Rupture, Sinking, or Tremor inflicted by +1 (including 'Unique Status Effects')\nIncrease the amount of Poise or Charge(including 'Unique Charge') gained by +1\nOn Kill, Gain +2 E.G.O resource to the Affinity of the Skill that defeated the enemy; gain +1 E.G.O resource to rest of the Affinities
   PL: Sloty tej postaci: +1\nLiczba Umiejętności 1: -1, liczba Umiejętności 3: +1\nNa początku tury odzyskuje 15 Poczytalności\nGdy Umiejętnościami nadaje Podpalenie, Krwawienie, Rozdarcie, Zatonięcie lub Wstrząs, wartość nadania +1 (również szczególne stany)\nGdy Umiejętnościami zyskuje Oddech lub Ładowanie (również szczególne ładowanie), wartość +1\nPrzy zabiciu wroga: +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu
287. [Status [VioletUnderstand] — nazwa] 이해
   źródło: Bufs-walpu4.json :: dataList[id=VioletUnderstand].name
   kontekst: identyfikator statusu w tekstach: `[VioletUnderstand]`
   limit: do 40 znaków
   EN: Understanding
   PL: Zrozumienie
288. [Status [VioletUnderstand] — opis] 스택당 가하는 피해량 +5%\n스택당 받는 피해량 + 5%\n(최댓값 : 5)
   źródło: Bufs-walpu4.json :: dataList[id=VioletUnderstand].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +5% damage per Stack\n- Take +5% damage per Stack\n(max value : 5)
   PL: Za każdy stos zadaje +5% obrażeń\nZa każdy stos otrzymuje +5% obrażeń\n(maks. 5)
289. [Status [MentalCrack] — nazwa] 정신 균열
   źródło: Bufs-walpu4.json :: dataList[id=MentalCrack].name
   kontekst: identyfikator statusu w tekstach: `[MentalCrack]`
   limit: do 40 znaków
   EN: Mental Fracture
   PL: Pęknięcie Umysłu
290. [Status [MentalCrack] — opis] 스택당 정신력 감소 효율 +1 (최대 5)\n5스택에 도달하면 스택이 소멸하고 정신력 10 피해\n턴 당 스택 1 감소
   źródło: Bufs-walpu4.json :: dataList[id=MentalCrack].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: SP Loss Efficiency +1 per Stack (max 5)\nExpires when it reaches 5 Stack, and take 10 SP damage\nLose 1 Stack per turn
   PL: Wydajność Spadku Poczytalności +1 za stos (maks. 5)\nPo 5 stosach stosy znikają, a jednostka traci 10 Poczytalności\nCo turę traci 1 stos
291. [Status [ImpendingCollapse] — nazwa] 붕괴 임박
   źródło: Bufs-walpu4.json :: dataList[id=ImpendingCollapse].name
   kontekst: identyfikator statusu w tekstach: `[ImpendingCollapse]`
   limit: do 40 znaków
   EN: Imminent Decay
   PL: Nieuchronny Upadek
292. [Status [ImpendingCollapse] — opis] 턴 종료 시 스택 1 감소\n턴 시작 시 스택이 1 이하면, 특수 스킬을 사용함
   źródło: Bufs-walpu4.json :: dataList[id=ImpendingCollapse].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 1 Stack\nTurn Start: At 1- Stack, use a special Skill
   PL: Na koniec tury traci 1 stos\nNa początku tury, przy 1 stosie lub mniej, używa specjalnej Umiejętności
293. [Status [ReloadLament] — nazwa] 재장전
   źródło: Bufs-walpu4.json :: dataList[id=ReloadLament].name
   kontekst: identyfikator statusu w tekstach: `[ReloadLament]`
   limit: do 40 znaków
   EN: Reload
   PL: Przeładowanie
294. [Status [ReloadLament] — opis] - 정신력을 ((30 - 보유한 산나비·죽은나비)/2)만큼 소모. (소수점 버림)\n- 보유한 산나비·죽은나비를 0으로 만들고, 산나비·죽은나비를 합하여 최댓값만큼 '죽어가는나비를본다.' 패시브의 확률에 따라 얻음.\n- 재장전 시 산나비와 죽은나비를 최소 1씩 얻음.
   źródło: Bufs-walpu4.json :: dataList[id=ReloadLament].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Consume (30 - (The Living + The Departed))/2 SP. (rounded down)\n- Reset both The Living and The Departed values on self to 0, and gain the max value of their sum based on the probabilities listed in the Passive 'ISeeTheDyingButterfly.'\n- On Reload, gain at least 1 of The Living and The Departed.
   PL: - Zużywa ((30 - posiadane Żywe i Martwe Motyle)/2) Poczytalności (zaokrąglone w dół)\n- Zeruje posiadane Żywe i Martwe Motyle, a ich sumę przywraca do maksimum według szans z pasywu „Widzę Umierające Motyle”.\n- Przy Przeładowaniu zyskuje co najmniej 1 Żywe i 1 Martwego Motyla.

## Statusy i efekty bojowe — Bufs-walpu5
- plik gry: `Bufs-walpu5.json`

295. [Status [Smoke] — nazwa] 연기
   źródło: Bufs-walpu5.json :: dataList[id=Smoke].name
   kontekst: identyfikator statusu w tekstach: `[Smoke]`
   limit: do 40 znaków
   EN: Smoke
   PL: Dym
296. [Status [Smoke] — opis] - 위력 최댓값: 10\n- 횟수 최댓값: 5\n- 수치가 9 이상이면, 최종 위력 +1\n- 수치당 받는 피해량 +5%\n- 턴 종료 시 횟수 1 감소
   źródło: Bufs-walpu5.json :: dataList[id=Smoke].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 10\n- Max Count: 5\n- At 9+ Potency, Final Power +1\n- Take +5% damage for every Potency\n- Lose 1 Count at Turn End
   PL: - Maks. Mocy: 10\n- Maks. Licznika: 5\n- Od 9 Mocy: Moc Końcowa +1\n- Otrzymuje +5% obrażeń za każdą Moc\n- Na koniec tury traci 1 Licznik
297. [Status [Church_LowMorale] — nazwa] 교단
   źródło: Bufs-walpu5.json :: dataList[id=Church_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Church_LowMorale]`
   limit: do 40 znaków
   EN: The Church
   PL: Zakon
298. [Status [Church_LowMorale] — opis] - 사기저하\n- 전투 중 연기 혹은 연기 횟수를 얻을 때, 추가로 1 얻음.\n- 턴 시작 시 취약 3, 피해량 증가 2, 수비 위력 증가 1 얻음
   źródło: Bufs-walpu5.json :: dataList[id=Church_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 additional Smoke or Smoke Count when gaining them\n- Turn Start: gain 3 Fragility, 2 Damage Up, and 1 Defense Power Up
   PL: - Spadek Moralu\n- Gdy podczas walki zyskuje Dym lub Licznik Dymu, zyskuje dodatkowo 1\n- Na początku tury zyskuje 3 Wrażliwości, 2 Wzrosty Obrażeń i 1 Wzrost Mocy Obrony
299. [Status [Church_Panic] — nazwa] 교단
   źródło: Bufs-walpu5.json :: dataList[id=Church_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Church_Panic]`
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Status [Church_Panic] — opis] - 패닉\n- 전투 중 연기 혹은 연기 횟수를 얻을 때, 추가로 2 얻음.\n- 턴 시작 시 취약 3, 피해량 증가 4, 수비 위력 증가 2 얻음
   źródło: Bufs-walpu5.json :: dataList[id=Church_Panic].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 additional Smoke or Smoke Count when gaining them\n- Turn Start: gain 3 Fragility, 4 Damage Up, and 2 Defense Power Up
   PL: - Panika\n- Gdy podczas walki zyskuje Dym lub Licznik Dymu, zyskuje dodatkowo 2\n- Na początku tury zyskuje 3 Wrażliwości, 4 Wzrosty Obrażeń i 2 Wzrosty Mocy Obrony
301. [Status [MeatGearForce] — nazwa] 고기 톱니:강제
   źródło: Bufs-walpu5.json :: dataList[id=MeatGearForce].name
   kontekst: identyfikator statusu w tekstach: `[MeatGearForce]`
   limit: do 40 znaków
   EN: Meat Gear: Coercion
   PL: Mięsna Zębatka: Przymus
302. [Status [MeatGearForce] — opis] - 체력이 1이 되더라도 전투 중에 죽지않음.\n- 턴 종료시 체력이 1 이라면, 사망함.
   źródło: Bufs-walpu5.json :: dataList[id=MeatGearForce].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - HP does not drop below 1 HP during the Combat Phase.\n- This unit dies if it has 1 HP at Turn End.
   PL: - Nie umiera podczas walki, nawet gdy HP spadnie do 1.\n- Jeśli na koniec tury ma 1 HP, umiera.
303. [Status [AllSetForShooting] — nazwa] 사격 준비 만전
   źródło: Bufs-walpu5.json :: dataList[id=AllSetForShooting].name
   kontekst: identyfikator statusu w tekstach: `[AllSetForShooting]`
   limit: do 40 znaków
   EN: Ready to Fire
   PL: Pełna Gotowość do Strzału
304. [Status [AllSetForShooting] — opis] - 스킬 슬롯 수 +1\n- 스킬 3 수량 +1, 대신 스킬 1 수량 -1\n- 사용하는 기본 공격 스킬에서 탄환을 소모하는 수만큼 피해량 +10%\n- 사용하는 공격 스킬에서 탄환을 얻는 스킬은 현재 보유한 마탄만큼 피해량 +10% (가장 높은 피해량 증가가 반영됨)\n- 스킬로 적 처치 시 자신을 포함하여 정신력이 가장 낮은 아군 2명 정신력 25 회복, 적을 처치한 스킬 속성의 E.G.O 자원 +2, 나머지 속성의 E.G.O 자원 +1
   źródło: Bufs-walpu5.json :: dataList[id=AllSetForShooting].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Modify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\n- Deal +10% damage for every Ammo the Base Attack Skill spends\n- Attack Skills that gain Ammo deal +10% damage for every Magic Bullet (applies whichever that has the highest damage gain)\n- On Kill with a Skill: heal 25 SP for 2 allies(including self) with the least SP; +2 E.G.O resources for the Affinity of the Skill that defeated the target; +1 E.G.O resource for all other Affinities
   PL: - Liczba slotów Umiejętności +1\n- Liczba Umiejętności 3: +1, w zamian liczba Umiejętności 1: -1\n- Zadaje +10% obrażeń za każdą Amunicję zużytą przez użytą podstawową Umiejętność ataku\n- Podstawowe Umiejętności ataku, które zyskują Amunicję, zadają +10% obrażeń za każdą Magiczną Amunicję (liczy się wariant dający najwyższy wzrost obrażeń)\n- Przy zabiciu wroga Umiejętnością leczy 25 Poczytalności u 2 sojuszników (w tym siebie) z najniższą Poczytalnością; +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu

## Statusy i efekty bojowe — Bufs-walpu6
- plik gry: `Bufs-walpu6.json`

305. [Status [ColdBlackTear] — nazwa] 차갑고 검은 눈물
   źródło: Bufs-walpu6.json :: dataList[id=ColdBlackTear].name
   kontekst: identyfikator statusu w tekstach: `[ColdBlackTear]`
   limit: do 40 znaków
   EN: Cold, Black Tears
   PL: Zimne, Czarne Łzy
306. [Status [ColdBlackTear] — opis] - 최댓값: 5\n- 턴 시작시 합 위력 감소 1 얻음\n- 이 효과가 있는 상태로 피격 시 정신력이 (스택 x 2)만큼 감소함 (턴 당 1회, 적중한 코인이 파괴되었다면 발동 하지 않음)\n- 이 효과가 증오의 여왕에 의해 감소되었다면, 정신력 5 회복\n- 이 효과로 감소하는 정신력은 -40 이하로 내려가지 않음
   źródło: Bufs-walpu6.json :: dataList[id=ColdBlackTear].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: gain 1 Clash Power Down\n- If this unit is hit while it has this effect, lose (Stack x 2) SP (once per turn; does not activate when hit by a Cracked Coin)\n- If Queen of Hatred reduced this effect, heal 5 SP\n- This effect cannot reduce this unit's SP below -40
   PL: - Maks. stosów: 5\n- Na początku tury zyskuje 1 Spadek Mocy Starcia\n- Przy trafieniu z tym efektem traci (stosy x 2) Poczytalności (1 na turę; nie działa, gdy trafiła pęknięta moneta)\n- Jeśli efekt zmniejszyła Królowa Nienawiści, odzyskuje 5 Poczytalności\n- Ten efekt nie może obniżyć Poczytalności poniżej -40
307. [Status [HelplessTear] — nazwa] 무력한 눈물
   źródło: Bufs-walpu6.json :: dataList[id=HelplessTear].name
   kontekst: identyfikator statusu w tekstach: `[HelplessTear]`
   limit: do 40 znaków
   EN: Helpless Tears
   PL: Bezsilne Łzy
308. [Status [HelplessTear] — opis] - 최댓값: 1\n- 공격 레벨 증가 3\n- 방어 레벨 감소 6\n- 모든 스킬의 가중치가 1 늘어남\n- 모든 스킬이 파괴 불가 코인이 됨\n- 침잠 위력 및 횟수 부여량 1 증가
   źródło: Bufs-walpu6.json :: dataList[id=HelplessTear].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Gain 3 Offense Levels\n- Lose 6 Defense Levels\n- All Skills gain +1 Atk Weight\n- All Skills become Unbreakable Coins\n- Inflict +1 more Sinking Potency and Count
   PL: - Maks. stosów: 1\n- Poziom Ataku +3\n- Poziom Obrony -6\n- Waga ataku wszystkich Umiejętności +1\n- Wszystkie monety Umiejętności stają się monetami niezniszczalnymi\n- Nadaje +1 więcej Mocy i Licznika Zatonięcia
309. [Status [WornOutKnight] — nazwa] 닳디 닳은 기사
   źródło: Bufs-walpu6.json :: dataList[id=WornOutKnight].name
   kontekst: identyfikator statusu w tekstach: `[WornOutKnight]`
   limit: do 40 znaków
   EN: Weathered Knight
   PL: Zwietczały Rycerz
310. [Status [WornOutKnight] — opis] 이번 턴 동안 받는 피해량 +100%
   źródło: Bufs-walpu6.json :: dataList[id=WornOutKnight].desc
   limit: do 120 znaków
   EN: Take +100% damage this turn
   PL: Otrzymuje +100% obrażeń w tej turze
311. [Status [WornOutKnight] — tekst klimatyczny] <color=#2e72b9>다른 이를 구함으로써 스스로를 구하고 싶었던 기사는, 이제 절망의 기사라는 불명예로 불리운 채, 다른 이들과 마찬가지로 사람들의 기억 속에서 사라져갔다.</color>
   źródło: Bufs-walpu6.json :: dataList[id=WornOutKnight].flavor
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#2e72b9>, </color>
   EN: <color=#2e72b9>The knight who wanted to redeem herself by saving others was now dishonorably called the Knight of Despair; forgotten from the people's memory, just like the others.</color>
   PL: <color=#2e72b9>Rycerz, który chciał ocalić samego siebie, ratując innych, nosi dziś niechlubny przydomek Rycerza Rozpaczy i — jak wszyscy inni — znika z pamięci ludzi.</color>
312. [Status [SignOfDespair] — nazwa] 절망의 가호
   źródło: Bufs-walpu6.json :: dataList[id=SignOfDespair].name
   kontekst: identyfikator statusu w tekstach: `[SignOfDespair]`
   limit: do 40 znaków
   EN: Blessing of Despair
   PL: Błogosławieństwo Rozpaczy
313. [Status [SignOfDespair] — opis] 공격 종료 시 차갑고 검은 눈물이 없는 대상이 있을 경우, 다음 턴에 해제됨\n\n합 위력 증가 1, 피해량 증가 1 얻음\n차갑고 검은 눈물 부여량 1 증가
   źródło: Bufs-walpu6.json :: dataList[id=SignOfDespair].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack End: If there are targets without Cold, Black Tears, removes this effect next turn\n\nGain 1 Clash Power Up and 1 Damage Up\nInflict +1 more Cold, Black Tears
   PL: Po zakończeniu ataku, jeśli istnieją cele bez Zimnych, Czarnych Łez, efekt zostanie zdjęty w następnej turze\n\nZyskuje 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń\nNadaje +1 więcej Zimnych, Czarnych Łez
314. [Status [CollapsedPride] — nazwa] 무너져 내린 긍지
   źródło: Bufs-walpu6.json :: dataList[id=CollapsedPride].name
   kontekst: identyfikator statusu w tekstach: `[CollapsedPride]`
   limit: do 40 znaków
   EN: Crumbled Pride
   PL: Pokruszona Duma
315. [Status [CollapsedPride] — opis] 닳디 닳은 기사 패시브에서 사용됨
   źródło: Bufs-walpu6.json :: dataList[id=CollapsedPride].desc
   limit: do 120 znaków
   EN: Used for "Weathered Knight" Passive
   PL: Używana przez pasyw „Zwietczały Rycerz”
316. [Status [CollapsedPride] — tekst klimatyczny] <color=#2e72b9>남은 건 닳디 닳은 기사라는 볼품없는 긍지 하나뿐이다.</color>
   źródło: Bufs-walpu6.json :: dataList[id=CollapsedPride].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#2e72b9>, </color>
   EN: <color=#2e72b9>All that remains is the hollow pride of a weathered knight.</color>
   PL: <color=#2e72b9>Ostała się jedynie pokruszona duma zwietczałego rycerza.</color>
317. [Status [FailedToAssistQueen] — nazwa] 내가… 무슨 쓸모…야?
   źródło: Bufs-walpu6.json :: dataList[id=FailedToAssistQueen].name
   kontekst: identyfikator statusu w tekstach: `[FailedToAssistQueen]`
   limit: do 40 znaków
   EN: What use... am I...?
   PL: Do czego ja... jeszcze... służę...?
318. [Status [FailedToAssistQueen] — opis] - 최댓값: 1\n- 공격 레벨 감소 3\n- 방어 레벨 감소 3
   źródło: Bufs-walpu6.json :: dataList[id=FailedToAssistQueen].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Lose 3 Offense Levels\n- Lose 3 Defense Levels
   PL: - Maks. stosów: 1\n- Poziom Ataku -3\n- Poziom Obrony -3
319. [Status [UsedTooMuchPower] — nazwa] 힘을 너무 많이 썼나봐
   źródło: Bufs-walpu6.json :: dataList[id=UsedTooMuchPower].name
   kontekst: identyfikator statusu w tekstach: `[UsedTooMuchPower]`
   limit: do 40 znaków
   EN: I used too much power
   PL: Chyba użyłam zbyt dużej mocy
320. [Status [UsedTooMuchPower] — opis] - 최댓값: 1\n- 턴 종료 시 전투에서 이탈함
   źródło: Bufs-walpu6.json :: dataList[id=UsedTooMuchPower].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: escapes from the Encounter
   PL: - Maks. stosów: 1\n- Na koniec tury opuszcza walkę
321. [Status [UsedTooMuchPower] — tekst klimatyczny] <color=#ff3d8f>힘이 다해 움직일 수 없다</color>
   źródło: Bufs-walpu6.json :: dataList[id=UsedTooMuchPower].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff3d8f>, </color>
   EN: <color=#ff3d8f>Exhausted and unable to move.</color>
   PL: <color=#ff3d8f>Siła wyczerpana — nie może się ruszać.</color>
322. [Status [ChasingArcana] — nazwa] 영창 - 아르카나 슬레이브
   źródło: Bufs-walpu6.json :: dataList[id=ChasingArcana].name
   kontekst: identyfikator statusu w tekstach: `[ChasingArcana]`
   limit: do 40 znaków
   EN: Chanting - Arcana Slave
   PL: Inkantacja - Arcana Slave
323. [Status [ChasingArcana] — opis] - 최댓값: 3\n- 턴 시작 시 1 증가\n- 스택이 3이 되면, 다음 턴에 속도 20을 얻고 아르카나 슬레이브를 사용함
   źródło: Bufs-walpu6.json :: dataList[id=ChasingArcana].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 1 at Turn Start\n- At 3 Stack, gains 20 Speed and uses ARCANA SLAVE next turn
   PL: - Maks. stosów: 3\n- +1 na początku tury\n- Przy 3 stosach w następnej turze zyskuje 20 Szybkości i używa ARCANA SLAVE
324. [Status [PowerOfLoveAndJustice] — nazwa] 사랑/정의
   źródło: Bufs-walpu6.json :: dataList[id=PowerOfLoveAndJustice].name
   kontekst: identyfikator statusu w tekstach: `[PowerOfLoveAndJustice]`
   limit: do 40 znaków
   EN: Love/Justice
   PL: Miłość/Sprawiedliwość
325. [Status [PowerOfLoveAndJustice] — opis] - 위력 당 파열 위력 부여량 1 증가
   źródło: Bufs-walpu6.json :: dataList[id=PowerOfLoveAndJustice].desc
   limit: do 120 znaków
   EN: - For every Stack, inflict +1 more Rupture Potency
   PL: - Za każdą Moc nadaje +1 więcej Mocy Rozdarcia
326. [Status [CentralCommandTeamCaptain] — nazwa] 중앙본부팀 팀장
   źródło: Bufs-walpu6.json :: dataList[id=CentralCommandTeamCaptain].name
   kontekst: identyfikator statusu w tekstach: `[CentralCommandTeamCaptain]`
   limit: do 40 znaków
   EN: Central Command Team Captain
   PL: Kapitan Zespołu Dowodzenia Centrali
327. [Status [CentralCommandTeamCaptain] — opis] - 해당 캐릭터의 슬롯 +1, 1스킬 수량 -1, 3스킬 수량 +1\n- 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동 위력을 부여할 때, 부여값 +1 (특수 상태이상 포함)\n- 자신이 스킬로 호흡 위력, 충전 횟수(특수 충전 포함)를 얻을 때, 획득값 +1\n- 패닉 및 침식 상태를 무시하고, 다음 턴에 정신력 0이 됨 (전투 당 1회)\n- 공격 가중치가 2 이상인 기본 스킬의 피해량 +30%\n- 적 처치시 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1
   źródło: Bufs-walpu6.json :: dataList[id=CentralCommandTeamCaptain].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Modify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\n- Increase the amount of Burn, Bleed, Rupture, Sinking, or Tremor Potency inflicted with Skills by +1 (including 'Unique Status Effects')\n- Increase the amount of Poise Potency or Charge Count(including 'Unique Charge') gained from Skills by +1\n- Instead of Panicking or Corroding, reset SP to 0 next turn (once per Encounter)\n- Base Attack Skills with 2+ Atk Weight deal +30% damage\n- On Kill, Gain +2 E.G.O resource to the Affinity of the Skill that defeated the enemy; gain +1 E.G.O resource to rest of the Affinities
   PL: - Sloty tej postaci: +1; liczba Umiejętności 1: -1; liczba Umiejętności 3: +1\n- Gdy Umiejętnościami nadaje Moc Podpalenia, Krwawienia, Rozdarcia, Zatonięcia lub Wstrząsu, wartość nadania +1 (również szczególne stany)\n- Gdy Umiejętnościami zyskuje Moc Oddechu lub Licznik Ładowania (również szczególne ładowanie), wartość +1\n- Ignoruje Panikę i Korozję, a w następnej turze Poczytalność spada do 0 (1 na walkę)\n- Podstawowe Umiejętności ataku o Wadze 2+ zadają +30% obrażeń\n- Przy zabiciu wroga: +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu
328. [Status [BestWelfareTeamMember] — nazwa] 복지팀 우수 직원
   źródło: Bufs-walpu6.json :: dataList[id=BestWelfareTeamMember].name
   kontekst: identyfikator statusu w tekstach: `[BestWelfareTeamMember]`
   limit: do 40 znaków
   EN: Welfare Team Model Employee
   PL: Wzorowy Pracownik Zespołu Dobrobytu
329. [Status [BestWelfareTeamMember] — opis] - 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동 위력을 부여할 때, 부여값 +1 (특수 상태이상 포함)\n- 패닉 및 침식 상태를 무시하고, 다음 턴에 정신력 0이 됨 (전투 당 1회)\n- 이 효과를 받는 게 로보토미 E.G.O::눈물로 벼려낸 검 로쟈라면, 매 턴 시작시 관통 피해량 증가 1 얻음
   źródło: Bufs-walpu6.json :: dataList[id=BestWelfareTeamMember].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When inflicting Burn, Bleed, Rupture, Sinking, and Tremor Potency with this unit's Skills, inflict +1 more of each (including 'Unique Status Effects')\n- Instead of Panicking or Corroding, reset this unit's SP to 0 next turn (once per Encounter)\n- If this effect is applied to Lobotomy E.G.O::The Sword Sharpened with Tears Rodion, gain 1 Pierce DMG Up at every Turn Start
   PL: - Gdy Umiejętnościami nadaje Moc Podpalenia, Krwawienia, Rozdarcia, Zatonięcia lub Wstrząsu, wartość nadania +1 (również szczególne stany)\n- Ignoruje Panikę i Korozję, a w następnej turze Poczytalność spada do 0 (1 na walkę)\n- Jeśli ten efekt działa na Lobotomy E.G.O::Miecz Ostrzony Łzami Rodion, na początku każdej tury zyskuje 1 Wzrost Obrażeń Przebicia
330. [Status [ChasingArcanahard] — nazwa] 영창 - 아르카나 슬레이브
   źródło: Bufs-walpu6.json :: dataList[id=ChasingArcanahard].name
   kontekst: identyfikator statusu w tekstach: `[ChasingArcanahard]`
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Status [ChasingArcanahard] — opis] - 최댓값: 3\n- 턴 시작 시 1 증가\n- 스택이 3이 되면, 다음 턴에 속박을 20 얻고 아르카나 슬레이브를 사용함
   źródło: Bufs-walpu6.json :: dataList[id=ChasingArcanahard].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 1 at Turn Start\n- At 3 Stack: next turn, gain 20 Bind and use ARCANA SLAVE
   PL: - Maks. stosów: 3\n- +1 na początku tury\n- Przy 3 stosach w następnej turze zyskuje 20 Spętań i używa ARCANA SLAVE
332. [Status [HystericGauge] — nazwa] 히스테리
   źródło: Bufs-walpu6.json :: dataList[id=HystericGauge].name
   kontekst: identyfikator statusu w tekstach: `[HystericGauge]`
   limit: do 40 znaków
   EN: Hysteria
   PL: Histeria
333. [Status [HystericGauge] — opis] - 기본값: 0\n- 최댓값: 3\n- 턴 종료 시\n· 정신력이 0 이상이면, 1 감소\n· 정신력이 0 미만이면, 1 증가
   źródło: Bufs-walpu6.json :: dataList[id=HystericGauge].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 0\n- Max Stack: 3\n- At Turn End...\n· At 0 or higher SP, lose 1 Stack\n· At less than 0 SP, gain 1 Stack
   PL: - Wartość bazowa: 0\n- Maks.: 3\n- Na koniec tury:\n· przy Poczytalności 0 lub wyższej traci 1 stos\n· przy Poczytalności niższej od 0 zyskuje 1 stos
334. [Status [MagicalGirlAppear] — nazwa] 마법소녀 등장!
   źródło: Bufs-walpu6.json :: dataList[id=MagicalGirlAppear].name
   kontekst: identyfikator statusu w tekstach: `[MagicalGirlAppear]`
   limit: do 40 znaków
   EN: Here Comes Magical Girl!
   PL: Pojawia się Czarodziejka!
335. [Status [MagicalGirlAppear] — opis] - 이번 턴에 사용하는 기본 공격 스킬이 더하기 코인 스킬로 변경됨\n\n- 자신의 사랑/증오당 기본 공격 스킬의 피해량 +3% (최대 15%)
   źródło: Bufs-walpu6.json :: dataList[id=MagicalGirlAppear].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For this turn, this unit uses Plus Coin Base Attack Skills\n\n- Base Attack Skills deal +3% damage for every Love/Hate on self (max 15%)
   PL: - W tej turze podstawowe Umiejętności ataku stają się Umiejętnościami z monetami plus\n\n- Za każdą Miłość/Nienawiść podstawowe Umiejętności ataku zadają +3% obrażeń (maks. 15%)
336. [Status [NoVillain] — nazwa] 역변-리버스드
   źródło: Bufs-walpu6.json :: dataList[id=NoVillain].name
   kontekst: identyfikator statusu w tekstach: `[NoVillain]`
   limit: do 50 znaków
   EN: Regressive Transformation - Reversed
   PL: Transformacja Wsteczna - Odwrócona
337. [Status [NoVillain] — opis] - 이번 턴에 사용하는 기본 공격 스킬이 빼기 코인 스킬로 변경됨
   źródło: Bufs-walpu6.json :: dataList[id=NoVillain].desc
   limit: do 120 znaków
   EN: - For this turn, this unit uses Minus Coin Base Attack Skills
   PL: - W tej turze podstawowe Umiejętności ataku stają się Umiejętnościami z monetami minus
338. [Status [VillainMark] — nazwa] 악당 표식
   źródło: Bufs-walpu6.json :: dataList[id=VillainMark].name
   kontekst: identyfikator statusu w tekstach: `[VillainMark]`
   limit: do 40 znaków
   EN: Mark of Villainy
   PL: Znak Złoczyńcy
339. [Status [VillainMark] — opis] - 돈키호테의 공격에 받는 피해량 +10%\n\n- 턴마다 가장 먼저 부여 받은 대상에게만 부여됨
   źródło: Bufs-walpu6.json :: dataList[id=VillainMark].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Don Quixote\n\n- Applies only to the first target to receive the effect in each turn
   PL: - Otrzymuje +10% obrażeń od ataków Don Kichota\n\n- W każdej turze nakładany tylko na pierwszego celu, który go otrzymał
340. [Status [ArcanaQueenOfHate] — nazwa] 매지컬 아르카나
   źródło: Bufs-walpu6.json :: dataList[id=ArcanaQueenOfHate].name
   kontekst: identyfikator statusu w tekstach: `[ArcanaQueenOfHate]`
   limit: do 40 znaków
   EN: Magical Arcana
   PL: Magiczna Arcana
341. [Status [ArcanaQueenOfHate] — opis] - 최댓값: 3\n- 자신의 기본 공격 스킬의  피해량 +(수치 X 5)%\n- 턴 종료 시 수치가 3이고 정신력이 -25이상이면, 정신력이 -25가 됨
   źródło: Bufs-walpu6.json :: dataList[id=ArcanaQueenOfHate].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Base Attack Skills deal +(Stack x 5)% damage\n- Turn End: At 3 Stack and with -25 or higher SP, change SP to -25
   PL: - Maks. stosów: 3\n- Podstawowe ataki zadają +(stosy x 5)% obrażeń\n- Na koniec tury, przy 3 stosach i Poczytalności -25 lub wyższej, Poczytalność zmienia się na -25
342. [Status [ThePowerOfLoveAndHate] — nazwa] 사랑/증오
   źródło: Bufs-walpu6.json :: dataList[id=ThePowerOfLoveAndHate].name
   kontekst: identyfikator statusu w tekstach: `[ThePowerOfLoveAndHate]`
   limit: do 40 znaków
   EN: Love/Hate
   PL: Miłość/Nienawiść
343. [Status [ThePowerOfLoveAndHate] — opis] - 횟수 최댓값: 20\n- 특수 충전\n- 소모 시 특정 스킬의 능력이 상승함. 횟수를 최대 20까지 얻을 수 있음. 턴 종료 시 횟수 1 감소\n(충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs-walpu6.json :: dataList[id=ThePowerOfLoveAndHate].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: - Max Count: 20\n- Unique Charge\n- Resource used by certain skills for additional effects. Its Count can go up to 20. Count lowers by 1 at the end of each turn.\n(Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency/Count)\n\n<color=#1aece7>Total Count consumed: {2}</color>
   PL: - Maks. Licznika: 20\n- Szczególne Ładowanie\n- Zużywane przez określone Umiejętności dla efektów dodatkowych. Licznik może osiągnąć 20. Na koniec tury Licznik maleje o 1\n(Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Ładowania)\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
344. [Status [MagicalGirlResponse] — nazwa] 마법소녀의 영창
   źródło: Bufs-walpu6.json :: dataList[id=MagicalGirlResponse].name
   kontekst: identyfikator statusu w tekstach: `[MagicalGirlResponse]`
   limit: do 40 znaków
   EN: Magical Girl's Chant
   PL: Inkantacja Czarodziejki
345. [Status [MagicalGirlResponse] — opis] - 최댓값: 2\n- 이 효과를 얻으면, 공격 위력 증가 1, 피해량 증가 1 얻음\n- 자신의 충전 횟수를 증가하거나 충전 횟수를 소모하는 공격 스킬의 최종 위력 +1, 피해량 +10%\n- 턴 종료 시 1 감소
   źródło: Bufs-walpu6.json :: dataList[id=MagicalGirlResponse].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- When gaining this effect, gain 1 Attack Power Up and 1 Damage Up\n- This unit's Attack Skills that gain or consume Charge Count gain Final Power +1 and deal +10% damage\n- Reduced by 1 at Turn End
   PL: - Maks. stosów: 2\n- Przy uzyskaniu tego efektu zyskuje 1 Wzrost Mocy Ataku i 1 Wzrost Obrażeń\n- Podstawowe Umiejętności ataku, które zyskują lub zużywają Licznik Ładowania, zyskują Moc Końcową +1 i zadają +10% obrażeń\n- Na koniec tury maleje o 1
346. [Status [BlessingAlly] — nazwa] 가호
   źródło: Bufs-walpu6.json :: dataList[id=BlessingAlly].name
   kontekst: identyfikator statusu w tekstach: `[BlessingAlly]`
   limit: do 40 znaków
   EN: Blessing
   PL: Błogosławieństwo
347. [Status [BlessingAlly] — opis] - 턴 시작 시 정신력 8당, 지키는 검 1 얻음 (최대 5)\n- 합 종료 시, 대상에게 침잠 2 부여 (턴당 1회)\n- 피격 시, 공격한 대상에게 침잠 2 부여 (턴당 1회)\n- 정신력 20당, 이 버프 효과로 부여하는 침잠 위력 부여값 +1 (최대 2)\n- 사용하는 기본 스킬이 더하기 코인 스킬로 변경됨
   źródło: Bufs-walpu6.json :: dataList[id=BlessingAlly].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Protecting Sword for every 8 SP (max 5)\n- When Clash ends, inflict 2 Sinking (once per turn)\n- When hit, inflict 2 Sinking on the attacker (once per turn)\n- For every 20 SP, inflict +1 more Sinking Potency with above effects (max 2)\n- Replace this unit's Base Skills with Plus Coin Skills
   PL: - Na początku tury zyskuje 1 Miecz Obrońcy za każde 8 Poczytalności (maks. 5)\n- Po zakończeniu Starcia nadaje celowi 2 Zatonięcia (1 na turę)\n- Przy trafieniu nadaje atakującemu 2 Zatonięcia (1 na turę)\n- Za każde 20 Poczytalności Zatonięcie nadawane tym błogosławieństwem zyskuje +1 więcej Mocy (maks. 2)\n- Podstawowe Umiejętności stają się Umiejętnościami z monetami plus
348. [Status [ProtectiveSword] — nazwa] 지키는 검
   źródło: Bufs-walpu6.json :: dataList[id=ProtectiveSword].name
   kontekst: identyfikator statusu w tekstach: `[ProtectiveSword]`
   limit: do 40 znaków
   EN: Protecting Sword
   PL: Miecz Obrońcy
349. [Status [ProtectiveSword] — opis] - 턴 시작 시, 수치 1당 방어 레벨 증가 1 얻음 (최대 5)\n- 턴 시작 시, 조작 패널에서 가장 왼쪽의 스킬 슬롯 도발치가 (수치 x 3)만큼 증가 (최대 15)\n- 최댓값 : 5\n- 턴 종료 시, 사라짐
   źródło: Bufs-walpu6.json :: dataList[id=ProtectiveSword].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Defense Level Up for every Stack (max 5)\n- Turn Start: +(Stack x 3) Aggro to the leftmost Skill Slot on the Dashboard (max 15)\n- Max Stack: 5\n- Expires at Turn End
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Obrony za każdy stos (maks. 5)\n- Na początku tury Wartość Prowokacji skrajnie lewego slotu Umiejętności w panelu rośnie o (stosy x 3) (maks. 15)\n- Maks. stosów: 5\n- Znika na koniec tury
350. [Status [DespairAlly] — nazwa] 절망
   źródło: Bufs-walpu6.json :: dataList[id=DespairAlly].name
   kontekst: identyfikator statusu w tekstach: `[DespairAlly]`
   limit: do 40 znaków
   EN: Despair
   PL: Rozpacz
351. [Status [DespairAlly] — opis] - 턴 시작 시, 정신력 -8당 꿰뚫는 검 1 얻음 (최대 5)\n- 합 종료 시, 대상의 침잠 횟수 1 증가 (턴당 1회)\n- 기본 공격 스킬의 첫 번째 코인 적중 시, 대상의 침잠 횟수 1 증가 (턴당 1회)\n- 정신력 -20당, 이 버프 효과로 부여하는 침잠 횟수의 부여값 +1 (최대 2)\n- 사용하는 기본 스킬이 빼기 코인 스킬로 변경됨
   źródło: Bufs-walpu6.json :: dataList[id=DespairAlly].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Piercing Sword for every -8 SP (max 5)\n- When Clash ends, inflict +1 Sinking Count (once per turn)\n- On Hit with the first Coin of a Base Attack Skill, inflict +1 Sinking Count (once per turn)\n- For every -20 SP, inflict +1 more Sinking Count with above effects (max 2)\n- Replace this unit's Base Skills with Minus Coin Skills
   PL: - Na początku tury zyskuje 1 Miecz Przebijający za każde -8 Poczytalności (maks. 5)\n- Po zakończeniu Starcia Licznik Zatonięcia celu +1 (1 na turę)\n- Przy trafieniu pierwszą monetą podstawowej Umiejętności ataku Licznik Zatonięcia celu +1 (1 na turę)\n- Za każde -20 Poczytalności Licznik Zatonięcia nadawany tym błogosławieństwem zyskuje +1 więcej (maks. 2)\n- Podstawowe Umiejętności stają się Umiejętnościami z monetami minus
352. [Status [PenetratingSword] — nazwa] 꿰뚫는 검
   źródło: Bufs-walpu6.json :: dataList[id=PenetratingSword].name
   kontekst: identyfikator statusu w tekstach: `[PenetratingSword]`
   limit: do 40 znaków
   EN: Piercing Sword
   PL: Miecz Przebijający
353. [Status [PenetratingSword] — opis] - 턴 시작 시, 수치 1당 공격 레벨 증가 1 얻음 (최대 5)\n- 턴 시작 시, 모든 스킬 슬롯의 도발치가 (수치 x 0.15)만큼 감소 (최대 0.75)\n- 최댓값 : 5\n- 턴 종료 시, 사라짐
   źródło: Bufs-walpu6.json :: dataList[id=PenetratingSword].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Offense Level Up for every Stack (max 5)\n- Turn Start: -(Stack x 0.15) Aggro to all Skill Slots on the Dashboard (max 0.75)\n- Max Stack: 5\n- Expires at Turn End
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każdy stos (maks. 5)\n- Na początku tury Wartość Prowokacji wszystkich slotów Umiejętności w panelu maleje o (stosy x 0,15) (maks. 0,75)\n- Maks. stosów: 5\n- Znika na koniec tury
354. [Status [SwordCutwithTear] — nazwa] 눈물 벼리기
   źródło: Bufs-walpu6.json :: dataList[id=SwordCutwithTear].name
   kontekst: identyfikator statusu w tekstach: `[SwordCutwithTear]`
   limit: do 40 znaków
   EN: Tear-sharpened
   PL: Ostrzone Łzami
355. [Status [SwordCutwithTear] — opis] - 턴 시작 시, 깊은 눈물 5 얻음\n· 수치가 3이면, 깊은 눈물 5 추가로 얻음\n- 턴 종료 시, (수치 x 15)만큼 정신력 감소\n- 기본 공격 스킬의 피해량이 (수치 x 10)%만큼 증가 (최대 30%)\n- 가호 상태면, 턴 시작 시 수치만큼 합 위력 증가 얻음\n- 절망 상태면, 턴 시작 시 수치만큼 관통 위력 증가 얻음\n- 최댓값 : 3
   źródło: Bufs-walpu6.json :: dataList[id=SwordCutwithTear].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 5 Deep Tears\n· At 3 Stack, gain additional 5 Deep Tears\n- Turn End: lose (Stack x 15) SP\n- Base Attack Skills deal +(Stack x 10)% damage (max 30%)\n- If this unit has Blessing, gain Clash Power Up by the effect's Stack at Turn Start\n- If this unit has Despair, gain Pierce Power Up by the effect's Stack at Turn Start\n- Max Stack: 3
   PL: - Na początku tury zyskuje 5 Głębokich Łez\n · Przy 3 stosach dodatkowo 5 Głębokich Łez\n- Na koniec tury traci (stosy x 15) Poczytalności\n- Podstawowe Umiejętności ataku zadają +(stosy x 10)% obrażeń (maks. 30%)\n- W stanie Błogosławieństwa na początku tury zyskuje tyle Wzrostów Mocy Starcia, ile wynosi stos tego efektu\n- W stanie Rozpaczy na początku tury zyskuje tyle Wzrostów Mocy Przebicia, ile wynosi stos tego efektu\n- Maks. stosów: 3
356. [Status [BlackTearsAlly] — nazwa] 깊은 눈물
   źródło: Bufs-walpu6.json :: dataList[id=BlackTearsAlly].name
   kontekst: identyfikator statusu w tekstach: `[BlackTearsAlly]`
   limit: do 40 znaków
   EN: Deep Tears
   PL: Głębokie Łzy
357. [Status [BlackTearsAlly] — opis] - 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 최댓값 : 20
   źródło: Bufs-walpu6.json :: dataList[id=BlackTearsAlly].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Charge (fixed Potency)\n- Resource used by certain skills for additional effects\n- Max Stack: 20
   PL: - Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Maks.: 20
358. [Status [KnightBless] — nazwa] 가호
   źródło: Bufs-walpu6.json :: dataList[id=KnightBless].name
   kontekst: identyfikator statusu w tekstach: `[KnightBless]`
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Status [KnightBless] — opis] - 턴 시작 시 보호 2 얻음\n- 1을 초과하는 물리 내성이 1로 조정됨 (흐트러짐 상태 제외)
   źródło: Bufs-walpu6.json :: dataList[id=KnightBless].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 2 Protection\n- Adjust any Attack Type Resistances exceeding 1 to 1 (unless Staggered)
   PL: - Na początku tury zyskuje 2 Ochrony\n- Wszystkie Odporności fizyczne powyżej 1 są korygowane do 1 (poza stanem Oszołomienia)
360. [Status [TraumaShield] — nazwa] 트라우마 방지장
   źródło: Bufs-walpu6.json :: dataList[id=TraumaShield].name
   kontekst: identyfikator statusu w tekstach: `[TraumaShield]`
   limit: do 40 znaków
   EN: Trauma Shield
   PL: Osłona Przed Traumą
361. [Status [TraumaShield] — opis] - 적에게 받는 정신력 피해 80% 감소\n- 침잠 피해 80% 감소\n- 턴 종료시 수치 1 감소
   źródło: Bufs-walpu6.json :: dataList[id=TraumaShield].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Reduce SP damage from enemies by 80%\n- Reduce Sinking damage taken by 80%\n- Reduced by 1 at Turn End
   PL: - Otrzymuje -80% obrażeń Poczytalności od wrogów\n- Otrzymuje -80% obrażeń od Zatonięcia\n- Na koniec tury maleje o 1

## Statusy i efekty bojowe — Bufs-walpu8
- plik gry: `Bufs-walpu8.json`

362. [Status [DesperadoBuff] — nazwa] 데스페라도
   źródło: Bufs-walpu8.json :: dataList[id=DesperadoBuff].name
   kontekst: identyfikator statusu w tekstach: `[DesperadoBuff]`
   limit: do 40 znaków
   EN: Desperado
   PL: Desperado
363. [Status [DesperadoBuff] — opis] - 최댓값: 2\n- 수치 1당, 기본 공격 스킬의 합 위력 +1, 기본 위력 +1\n- 수치가 2면, 기본 공격 스킬의 더하기 코인 위력 +1, 빼기 코인 위력 -1\n- 턴 종료 시 효과 소멸
   źródło: Bufs-walpu8.json :: dataList[id=DesperadoBuff].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- For every Stack, Base Attack Skill Clash Power +1, Base Power +1\n- At 2 Stack, Base Attack Skill Plus Coin Power +1, Minus Coin Power -1\n- Expires at Turn End
   PL: - Maks. stosów: 2\n- Za każdy stos Moc Starcia podstawowych Umiejętności ataku +1, Moc bazowa +1\n- Przy 2 stosach monety plus podstawowych Umiejętności ataku zyskują +1 Mocy, a monety minus -1 Mocy\n- Znika na koniec tury
364. [Status [TensionUp] — nazwa] 텐션 업
   źródło: Bufs-walpu8.json :: dataList[id=TensionUp].name
   kontekst: identyfikator statusu w tekstach: `[TensionUp]`
   limit: do 40 znaków
   EN: Hyped-up
   PL: Rozkręcony
365. [Status [TensionUp] — opis] - 최댓값: 3\n- 수치 1당, 분노, 색욕 속성 스킬로 가하는 피해량 +5%\n- 피격 시 (5 x 수치)만큼 흐트러짐 피해 입음\n- 턴 종료 시 효과 소멸
   źródło: Bufs-walpu8.json :: dataList[id=TensionUp].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- For every Stack, deal +5% damage with Wrath and Lust Skills\n- When hit, raise this unit's Stagger Threshold by (5 x Stack)\n- Expires at Turn End
   PL: - Maks. stosów: 3\n- Za każdy stos zadaje +5% obrażeń Umiejętnościami Gniewu i Żądzy\n- Przy trafieniu otrzymuje (5 x stosy) obrażeń Oszołomienia\n- Znika na koniec tury
366. [Status [PinkPetals] — nazwa] 분홍 꽃잎
   źródło: Bufs-walpu8.json :: dataList[id=PinkPetals].name
   kontekst: identyfikator statusu w tekstach: `[PinkPetals]`
   limit: do 40 znaków
   EN: Pink Petals
   PL: Różowe Płatki
367. [Status [PinkPetals] — opis] - 최댓값: 30\n- 수치 1당, 우울 속성 스킬로 피격 시 받는 피해량 +1% (최대 15%)\n- 수치 10당, 피격 시 침잠 횟수 1 증가 (턴당 2회)\n- 진동 폭발 시 (침잠 위력과 분홍 꽃잎 수치의 합/5)만큼 우울 피해\n- 턴 종료 시 1 감소
   źródło: Bufs-walpu8.json :: dataList[id=PinkPetals].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- For every Stack, take +1% damage when hit by Gloom Skills (max 15%)\n- For every 10 Stack, gain +1 Sinking Count when hit (2 times per turn)\n- When Tremor Burst is triggered on this unit, take ((Sinking Potency + Pink Petals) / 5) Gloom damage\n- Turn End: Lose 1 Stack
   PL: - Maks. stosów: 30\n- Za każdy stos otrzymuje +1% obrażeń przy trafieniu Umiejętnościami Posępności (maks. 15%)\n- Za każde 10 stosów zyskuje +1 Licznika Zatonięcia przy trafieniu (2 na turę)\n- Po wywołaniu Wybuchu Wstrząsu otrzymuje (Moc Zatonięcia + Różowe Płatki)/5 obrażeń Posępnością\n- Na koniec tury maleje o 1
368. [Status [QueenBeepheromone] — nazwa] 페로몬
   źródło: Bufs-walpu8.json :: dataList[id=QueenBeepheromone].name
   kontekst: identyfikator statusu w tekstach: `[QueenBeepheromone]`
   limit: do 40 znaków
   EN: Pheromone
   PL: Feromon
369. [Status [QueenBeepheromone] — opis] - 도발치 10 증가\n- 피격 시 대상에게 화상 3 부여
   źródło: Bufs-walpu8.json :: dataList[id=QueenBeepheromone].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +10 Aggro\n- When hit, inflict 3 Burn on target
   PL: - Wartość Prowokacji +10\n- Przy trafieniu nadaje celowi 3 Podpalenia
370. [Status [QueenBeeMark] — nazwa] 페로몬 표식
   źródło: Bufs-walpu8.json :: dataList[id=QueenBeeMark].name
   kontekst: identyfikator statusu w tekstach: `[QueenBeeMark]`
   limit: do 40 znaków
   EN: Pheromone Mark
   PL: Znak Feromonów
371. [Status [QueenBeeMark] — opis] - 자신의 화상 수치 3당, 피격시 받는 피해량 +1% (최대 20%)\n- 턴 종료 시 효과 소멸
   źródło: Bufs-walpu8.json :: dataList[id=QueenBeeMark].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 3 Burn on self, take +1% damage when hit (max 20%)\n- Expires at Turn End
   PL: - Za każde 3 Podpalenia na sobie otrzymuje +1% obrażeń przy trafieniu (maks. 20%)\n- Znika na koniec tury
372. [Status [RunHallway] — nazwa] 무리 이동 준비
   źródło: Bufs-walpu8.json :: dataList[id=RunHallway].name
   kontekst: identyfikator statusu w tekstach: `[RunHallway]`
   limit: do 40 znaków
   EN: Preparing Herd Migration
   PL: Przygotowanie do Wędrówki Stada
373. [Status [RunHallway] — opis] - 최댓값: 3\n- 전투 시작 시 1 감소\n- 0이 되면, 턴 시작 시 '무리 이동' 스킬 사용
   źródło: Bufs-walpu8.json :: dataList[id=RunHallway].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Combat Start: Lose 1 Stack\n- At 0 Stack, use 'Herd Migration' at Turn Start
   PL: - Maks. stosów: 3\n- Na początku walki traci 1 stos\n- Przy 0 stosach używa na początku tury Umiejętności „Wędrówka Stada”
374. [Status [NextHallway] — nazwa] 무리 이주
   źródło: Bufs-walpu8.json :: dataList[id=NextHallway].name
   kontekst: identyfikator statusu w tekstach: `[NextHallway]`
   limit: do 40 znaków
   EN: Herd Relocation
   PL: Wędrówka Stada
375. [Status [NextHallway] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함\n(강제 흐트러짐 제외, 사망으로 처리되지 않음)\n- 연속 전투 인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동
   źródło: Bufs-walpu8.json :: dataList[id=NextHallway].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: recover from Stagger and escape from the Encounter\n(excluding forced Stagger; does not count as death)\n- In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order
   PL: - Na koniec tury wychodzi z Oszołomienia i opuszcza walkę\n(poza wymuszonym Oszołomieniem; nie liczy się jako śmierć)\n- W walkach łańcuchowych przy odwrocie przekazuje liczbę swoich slotów jednostce zastępującej, po czym przenosi się na koniec kolejki jednostek rezerwowych
376. [Status [PumpkinJelly] — nazwa] 오렌지맛 뀽뀽이
   źródło: Bufs-walpu8.json :: dataList[id=PumpkinJelly].name
   kontekst: identyfikator statusu w tekstach: `[PumpkinJelly]`
   limit: do 40 znaków
   EN: BongBong Orange
   PL: Pomarańczowy BongBong
377. [Status [PumpkinJelly] — opis] - 최댓값: 1\n턴 시작 시 현재 체력이 최대 체력의 60% 미만이면, 최대 체력의 30% 만큼 체력 회복하고 버프 소멸
   źródło: Bufs-walpu8.json :: dataList[id=PumpkinJelly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\nTurn Start: At less than 60% HP, heal 30% HP and lose this effect
   PL: - Maks. stosów: 1\nNa początku tury, przy HP poniżej 60% maks., leczy 30% Maks. HP, a błogosławieństwo znika
378. [Status [BestWelfareTeamCaptain] — nazwa] 복지팀 팀장
   źródło: Bufs-walpu8.json :: dataList[id=BestWelfareTeamCaptain].name
   kontekst: identyfikator statusu w tekstach: `[BestWelfareTeamCaptain]`
   limit: do 40 znaków
   EN: Welfare Team Captain
   PL: Kapitan Zespołu Dobrobytu
379. [Status [BestWelfareTeamCaptain] — opis] - 해당 캐릭터의 슬롯 +1, 1스킬 수량 -1, 3스킬 수량 +1\n- 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동 위력을 부여할 때, 부여값 +2  (특수 상태이상 포함)\n- 탄환을 얻음 또는 소모하는 기본 스킬의 피해량 + 30%\n- 탄환을 얻음 또는 소모하는 기본 스킬 사용 시 자신을 포함하여, 정신력이 가장 낮은 아군 1명 정신력 10 회복\n- 적 처치시 다음 효과 발동\n· 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1\n· 다음 턴에 해당 적이 보유했던 화상, 출혈, 파열, 침잠, 진동의 위력과 횟수를 각각 모든 적에게 무작위로 부여. (최소 1)
   źródło: Bufs-walpu8.json :: dataList[id=BestWelfareTeamCaptain].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n  - Modify Skill pool: Gain 1 copy of Skill 3, but lose 1 copy of Skill 1\n- Increase the amount of Burn, Bleed, Rupture, Sinking, or Tremor Potency inflicted with Skills by +2 (including 'Unique Status Effects')\n- Base Skills that gain or spend Ammo deal +30% damage\n- On Use with Base Skills that gain or spend Ammo, heal 10 SP for 1 ally with the lowest SP (including this unit)\n- On Kill, activate the following:\n· E.G.O Resource +2 to the Affinity that killed the enemy; E.G.O Resource +1 to all Affinities\n· Next turn, inflict the remaining Burn, Bleed, Rupture, Sinking, and Tremor Potency and Count on the said enemy randomly between all enemies (min 1)
   PL: - Sloty tej postaci: +1; liczba Umiejętności 1: -1; liczba Umiejętności 3: +1\n- Gdy Umiejętnościami nadaje Moc Podpalenia, Krwawienia, Rozdarcia, Zatonięcia lub Wstrząsu, wartość nadania +2 (również szczególne stany)\n- Podstawowe Umiejętności, które zyskują lub zużywają Amunicję, zadają +30% obrażeń\n- Przy użyciu takich podstawowych Umiejętności leczy 10 Poczytalności u 1 sojusznika z najniższą Poczytalnością (wliczając siebie)\n- Przy zabiciu wroga:\n· +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu\n· W następnej turze losowo rozdziela pozostałą wrogu Moc i Licznik Podpalenia, Krwawienia, Rozdarcia, Zatonięcia i Wstrząsu między wszystkich wrogów (min. 1)

## Statusy i efekty bojowe — Bufs-x1p1c1
- plik gry: `Bufs-x1p1c1.json`

380. [Status [LeakedOutSauce] — nazwa] 새어나온 양념장
   źródło: Bufs-x1p1c1.json :: dataList[id=LeakedOutSauce].name
   kontekst: identyfikator statusu w tekstach: `[LeakedOutSauce]`
   limit: do 40 znaków
   EN: Leaking Marinade
   PL: Wyciekająca Marynata
381. [Status [LeakedOutSauce] — opis] - 턴 종료 시 수치 2당, 다음 턴에 신속 1 얻음 (최대 10)\n- 턴 종료 시 소멸
   źródło: Bufs-x1p1c1.json :: dataList[id=LeakedOutSauce].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Gain 1 Haste next turn for every 2 Stack (max 10)\n- Expires at Turn End
   PL: - Na koniec tury: 1 Pośpiech w następnej turze za każde 2 stosy (maks. 10)\n- Znika na koniec tury
382. [Status [DeliciousSauce] — nazwa] 황금 비법 소스
   źródło: Bufs-x1p1c1.json :: dataList[id=DeliciousSauce].name
   kontekst: identyfikator statusu w tekstach: `[DeliciousSauce]`
   limit: do 40 znaków
   EN: Golden Recipe Sauce
   PL: Złoty Sekretny Sos
383. [Status [DeliciousSauce] — opis] - 합 위력 +2
   źródło: Bufs-x1p1c1.json :: dataList[id=DeliciousSauce].desc
   limit: do 120 znaków
   EN: - Clash Power +2
   PL: - Moc Starcia +2
384. [Status [Yummy_Lowmorale] — nazwa] 맛있어짐
   źródło: Bufs-x1p1c1.json :: dataList[id=Yummy_Lowmorale].name
   kontekst: identyfikator statusu w tekstach: `[Yummy_Lowmorale]`
   limit: do 40 znaków
   EN: Yummers
   PL: Coraz Smaczniejsze
385. [Status [Yummy_Lowmorale] — opis] - 사기 저하\n- 턴 시작시 취약 1 얻음
   źródło: Bufs-x1p1c1.json :: dataList[id=Yummy_Lowmorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile
   PL: - Spadek Moralu\n- Na początku tury zyskuje 1 Wrażliwość
386. [Status [Yummy_Lowmorale] — podsumowanie] 취약 얻음
   źródło: Bufs-x1p1c1.json :: dataList[id=Yummy_Lowmorale].summary
   limit: do 120 znaków
   EN: Gain Fragile
   PL: Zyskuje Wrażliwość
387. [Status [Yummy_Panic] — nazwa] 맛있어짐
   źródło: Bufs-x1p1c1.json :: dataList[id=Yummy_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Yummy_Panic]`
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Status [Yummy_Panic] — opis] - 패닉\n- 턴 시작시 취약 2 얻음
   źródło: Bufs-x1p1c1.json :: dataList[id=Yummy_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Fragile
   PL: - Panika\n- Na początku tury zyskuje 2 Wrażliwości
389. [Status [Yummy_Panic] — podsumowanie] 취약 얻음
   źródło: Bufs-x1p1c1.json :: dataList[id=Yummy_Panic].summary
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs-ycgd
- plik gry: `Bufs-ycgd.json`

390. [Status [Grudge] — nazwa] 맺혀가는 응어리
   źródło: Bufs-ycgd.json :: dataList[id=Grudge].name
   kontekst: identyfikator statusu w tekstach: `[Grudge]`
   limit: do 40 znaków
   EN: Growing Resentment
   PL: Narastający Żal
391. [Status [Grudge] — opis] 버프가 있을 때, 받은 피해량만큼 수치를 얻음. 턴 종료 시 소멸됨
   źródło: Bufs-ycgd.json :: dataList[id=Grudge].desc
   limit: do 140 znaków
   EN: When this unit has a relevant buff: gain Growing Resentment equal to damage taken. Expires at Turn End
   PL: Mając odpowiednie błogosławieństwo, zyskuje wartość równą otrzymanym obrażeniom. Znika na koniec tury
392. [Status [AaCePbBg] — nazwa] 원한
   źródło: Bufs-ycgd.json :: dataList[id=AaCePbBg].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBg]`
   limit: do 40 znaków
   EN: Resentment
   PL: Uraza
393. [Status [AaCePbBg] — opis] 턴 시작 시 피해량 증가 2, 방어 레벨 감소 3을 얻음
   źródło: Bufs-ycgd.json :: dataList[id=AaCePbBg].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Damage Up and 3 Defense Level Down
   PL: Na początku tury zyskuje 2 Wzrosty Obrażeń i 3 Spadki Poziomu Obrony
394. [Status [AaCePbBh] — nazwa] 원한
   źródło: Bufs-ycgd.json :: dataList[id=AaCePbBh].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBh]`
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Status [AaCePbBh] — opis] 턴 시작 시 공격 위력 증가 1, 방어 레벨 감소 5를 얻음
   źródło: Bufs-ycgd.json :: dataList[id=AaCePbBh].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Attack Power Up and 5 Defense Level Down
   PL: Na początku tury zyskuje 1 Wzrost Mocy Ataku i 5 Spadków Poziomu Obrony

## Statusy i efekty bojowe — Bufs
- plik gry: `Bufs.json`

396. [Status [Enhancement] — nazwa] 공격 위력 증가
   źródło: Bufs.json :: dataList[id=Enhancement].name
   kontekst: identyfikator statusu w tekstach: `[Enhancement]`
   limit: do 40 znaków
   EN: Attack Power Up
   PL: Wzrost Mocy Ataku
397. [Status [Enhancement] — opis] 이번 턴 동안 공격 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=Enhancement].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Attack Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności ataku +{0}
398. [Status [Enhancement] — podsumowanie] 공격 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=Enhancement].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ATK Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności ataku +{0}
399. [Status [Agility] — nazwa] 신속
   źródło: Bufs.json :: dataList[id=Agility].name
   kontekst: identyfikator statusu w tekstach: `[Agility]`
   limit: do 40 znaków
   EN: Haste
   PL: Pośpiech
400. [Status [Agility] — opis] 이번 턴 동안 속도 +{0}
   źródło: Bufs.json :: dataList[id=Agility].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Speed +{0} for this turn.
   PL: W tej turze Szybkość +{0}
401. [Status [Agility] — podsumowanie] 속도 +{0}
   źródło: Bufs.json :: dataList[id=Agility].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: SPD +{0}
   PL: Szybkość +{0}
402. [Status [Endurance] — nazwa] 수비 위력 증가
   źródło: Bufs.json :: dataList[id=Endurance].name
   kontekst: identyfikator statusu w tekstach: `[Endurance]`
   limit: do 40 znaków
   EN: Defense Power Up
   PL: Wzrost Mocy Obrony
403. [Status [Endurance] — opis] 이번 턴 동안 수비 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=Endurance].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności obrony +{0}
404. [Status [Endurance] — podsumowanie] 수비 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=Endurance].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: DEF Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności obrony +{0}
405. [Status [Reduction] — nazwa] 공격 위력 감소
   źródło: Bufs.json :: dataList[id=Reduction].name
   kontekst: identyfikator statusu w tekstach: `[Reduction]`
   limit: do 40 znaków
   EN: Attack Power Down
   PL: Spadek Mocy Ataku
406. [Status [Reduction] — opis] 이번 턴 동안 공격 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=Reduction].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Attack Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności ataku -{0}
407. [Status [Reduction] — podsumowanie] 공격 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=Reduction].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ATK Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności ataku -{0}
408. [Status [Binding] — nazwa] 속박
   źródło: Bufs.json :: dataList[id=Binding].name
   kontekst: identyfikator statusu w tekstach: `[Binding]`
   limit: do 40 znaków
   EN: Bind
   PL: Spętanie
409. [Status [Binding] — opis] 이번 턴 동안 속도 -{0}
   źródło: Bufs.json :: dataList[id=Binding].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Speed -{0} for this turn.
   PL: W tej turze Szybkość -{0}
410. [Status [Binding] — podsumowanie] 속도 -{0}
   źródło: Bufs.json :: dataList[id=Binding].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: SPD -{0}
   PL: Szybkość -{0}
411. [Status [Vulnerable] — nazwa] 취약
   źródło: Bufs.json :: dataList[id=Vulnerable].name
   kontekst: identyfikator statusu w tekstach: `[Vulnerable]`
   limit: do 40 znaków
   EN: Fragile
   PL: Wrażliwość
412. [Status [Vulnerable] — opis] 이번 턴 동안 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=Vulnerable].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage this turn. (Max 100%)
   PL: Otrzymuje +{0}0% obrażeń w tej turze (maks. 100%)
413. [Status [Vulnerable] — podsumowanie] 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=Vulnerable].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0}0% Damage Taken
   PL: Otrzymuje +{0}0% obrażeń
414. [Status [Taunt] — nazwa] 도발
   źródło: Bufs.json :: dataList[id=Taunt].name
   kontekst: identyfikator statusu w tekstach: `[Taunt]`
   limit: do 40 znaków
   EN: Taunt
   PL: Prowokacja
415. [Status [ElectricShock] — nazwa] 감전
   źródło: Bufs.json :: dataList[id=ElectricShock].name
   kontekst: identyfikator statusu w tekstach: `[ElectricShock]`
   limit: do 40 znaków
   EN: Shock
   PL: Porażenie
416. [Status [ElectricShock] — opis] 이번 턴동안 받는 피해가 {0}만큼 고정으로 증가
   źródło: Bufs.json :: dataList[id=ElectricShock].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take {0} more damage this turn.
   PL: Otrzymuje {0} więcej obrażeń w tej turze
417. [Status [Target] — nazwa] 표적
   źródło: Bufs.json :: dataList[id=Target].name
   kontekst: identyfikator statusu w tekstach: `[Target]`
   limit: do 40 znaków
   EN: Marked
   PL: Oznaczony
418. [Status [Target] — opis] [날카로운 칼] 패시브를 가지고 있는 캐릭터의 공격 대상이 됨
   źródło: Bufs.json :: dataList[id=Target].desc
   limit: do 120 znaków
   EN: Targeted by the character with the Passive [Sharp Edge].
   PL: Staje się celem postaci posiadającej pasyw [Ostre Ostrze]
419. [Status [SelfHarm_LowMorale] — nazwa] 자해
   źródło: Bufs.json :: dataList[id=SelfHarm_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[SelfHarm_LowMorale]`
   limit: do 40 znaków
   EN: Compulsion
   PL: Samookaleczenie
420. [Status [SelfHarm_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 신속 2, 취약 2를 얻음
   źródło: Bufs.json :: dataList[id=SelfHarm_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Haste and 2 Fragile
   PL: - Niskie Morale\n- Na początek tury zyskuje 2 Pośpiechu i 2 Wrażliwości
421. [Status [SelfHarm_Panic] — nazwa] 자해
   źródło: Bufs.json :: dataList[id=SelfHarm_Panic].name
   kontekst: identyfikator statusu w tekstach: `[SelfHarm_Panic]`
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Status [SelfHarm_Panic] — opis] - 패닉\n- 턴 시작 시 자신의 체력 -10
   źródło: Bufs.json :: dataList[id=SelfHarm_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Lose 10 HP
   PL: - Panika\n- Na początku tury traci 10 HP
423. [Status [Blame_LowMorale] — nazwa] 비난
   źródło: Bufs.json :: dataList[id=Blame_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Blame_LowMorale]`
   limit: do 40 znaków
   EN: Outlash
   PL: Pogarda
424. [Status [Blame_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 공격 위력 증가 2, 취약 2를 얻음
   źródło: Bufs.json :: dataList[id=Blame_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Attack Power Up and 2 Fragile
   PL: - Niskie Morale\n- Na początek tury zyskuje 2 Wzrosty Mocy Ataku i 2 Wrażliwości
425. [Status [Blame_Panic] — nazwa] 비난
   źródło: Bufs.json :: dataList[id=Blame_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Blame_Panic]`
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Status [Blame_Panic] — opis] - 패닉\n- 턴 시작 시 무작위 아군의 정신력 -20
   źródło: Bufs.json :: dataList[id=Blame_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: A random ally loses 20 SP
   PL: - Panika\n- Na początku tury losowy sojusznik traci 20 Poczytalności
427. [Status [EgoErode] — nazwa] E.G.O침식
   źródło: Bufs.json :: dataList[id=EgoErode].name
   kontekst: identyfikator statusu w tekstach: `[EgoErode]`
   limit: do 40 znaków
   EN: E.G.O Corrosion
   PL: Korozja E.G.O
428. [Status [EgoErode] — opis] 이번 턴 동안 명령 불가. E.G.O 침식 스킬만 사용 가능.
   źródło: Bufs.json :: dataList[id=EgoErode].desc
   limit: do 120 znaków
   EN: Won’t listen to orders and will only use Corrosion Skills.
   PL: Nie wykonuje rozkazów. Może używać wyłącznie Umiejętności Korozji E.G.O.
429. [Status [EgoErode] — podsumowanie] 명령 불가. E.G.O 침식 스킬 사용
   źródło: Bufs.json :: dataList[id=EgoErode].summary
   limit: do 120 znaków
   EN: Out of control; uses Corrosion Skills
   PL: Nie wykonuje rozkazów; używa Umiejętności Korozji E.G.O
430. [Status [Charge] — nazwa] 충전
   źródło: Bufs.json :: dataList[id=Charge].name
   kontekst: identyfikator statusu w tekstach: `[Charge]`
   limit: do 40 znaków
   EN: Charge
   PL: Ładowanie
431. [Status [Charge] — opis] 소모 시 특정 스킬의 능력이 상승함. 횟수를 최대 20까지 얻을 수 있음. 턴 종료 시 횟수 1 감소.\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs.json :: dataList[id=Charge].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: Resource used by certain skills for additional effects. Its Count can go up to 20. Count lowers by 1 at the end of each turn.\n\n<color=#1aece7>Total Count consumed: {2}</color>
   PL: Zużywane przez określone Umiejętności dla efektów dodatkowych. Licznik może osiągnąć 20. Na koniec każdej tury Licznik maleje o 1.\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
432. [Status [Charge] — podsumowanie] 특정 스킬 사용 시 증가 또는 소모
   źródło: Bufs.json :: dataList[id=Charge].summary
   limit: do 120 znaków
   EN: Specific Skill Resource
   PL: Zyskiwany lub zużywany przy użyciu określonych Umiejętności
433. [Status [DamageOverTime] — nazwa] 지속 피해
   źródło: Bufs.json :: dataList[id=DamageOverTime].name
   kontekst: identyfikator statusu w tekstach: `[DamageOverTime]`
   limit: do 40 znaków
   EN: Ongoing Damage
   PL: Obrażenia Ciągłe
434. [Status [DamageOverTime] — opis] 턴 시작 시 {0} 만큼 고정 체력 피해를 입음
   źródło: Bufs.json :: dataList[id=DamageOverTime].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn Start: Take {0} fixed HP damage.
   PL: Na początek tury otrzymuje obrażenia stałe w wysokości {0}
435. [Status [DamageOverTime] — podsumowanie] 고정 체력 피해 -{0}
   źródło: Bufs.json :: dataList[id=DamageOverTime].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} fixed HP damage
   PL: Obrażenia stałe -{0}
436. [Status [ResultEnhancement] — nazwa] 위력 증가
   źródło: Bufs.json :: dataList[id=ResultEnhancement].name
   kontekst: identyfikator statusu w tekstach: `[ResultEnhancement]`
   limit: do 40 znaków
   EN: Power Up
   PL: Wzrost Mocy
437. [Status [ResultEnhancement] — opis] 이번 턴 동안 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=ResultEnhancement].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności +{0}
438. [Status [ResultEnhancement] — podsumowanie] 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=ResultEnhancement].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności +{0}
439. [Status [Protection] — nazwa] 보호
   źródło: Bufs.json :: dataList[id=Protection].name
   kontekst: identyfikator statusu w tekstach: `[Protection]`
   limit: do 40 znaków
   EN: Protection
   PL: Ochrona
440. [Status [Protection] — opis] 이번 턴 동안 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=Protection].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage this turn. (Max 100%)
   PL: Otrzymuje -{0}0% obrażeń w tej turze (maks. 100%)
441. [Status [Protection] — podsumowanie] 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=Protection].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: -{0}0% Damage Taken
   PL: Otrzymuje -{0}0% obrażeń
442. [Status [AttackDmgUp] — nazwa] 피해량 증가
   źródło: Bufs.json :: dataList[id=AttackDmgUp].name
   kontekst: identyfikator statusu w tekstach: `[AttackDmgUp]`
   limit: do 40 znaków
   EN: Damage Up
   PL: Wzrost Obrażeń
443. [Status [AttackDmgUp] — opis] 이번 턴 동안 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AttackDmgUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami w tej turze (maks. 100%)
444. [Status [AttackDmgUp] — podsumowanie] 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=AttackDmgUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0}0% Damage Dealt
   PL: Zadawane Obrażenia +{0}0%
445. [Status [DefenseUp] — nazwa] 방어 레벨 증가
   źródło: Bufs.json :: dataList[id=DefenseUp].name
   kontekst: identyfikator statusu w tekstach: `[DefenseUp]`
   limit: do 40 znaków
   EN: Defense Level Up
   PL: Wzrost Poziomu Obrony
446. [Status [DefenseUp] — opis] 이번 턴 동안 방어 레벨 +{0}
   źródło: Bufs.json :: dataList[id=DefenseUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level +{0} for this turn.
   PL: W tej turze Poziom Obrony +{0}
447. [Status [DefenseUp] — podsumowanie] 방어 레벨 +{0}
   źródło: Bufs.json :: dataList[id=DefenseUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level +{0}
   PL: Poziom Obrony +{0}
448. [Status [PlusCoinValueUp] — nazwa] 더하기 코인 강화
   źródło: Bufs.json :: dataList[id=PlusCoinValueUp].name
   kontekst: identyfikator statusu w tekstach: `[PlusCoinValueUp]`
   limit: do 40 znaków
   EN: Plus Coin Boost
   PL: Wzmocnienie Monet Plus
449. [Status [PlusCoinValueUp] — opis] 이번 턴 동안 더하기 코인 위력 +{0}
   źródło: Bufs.json :: dataList[id=PlusCoinValueUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Plus Coin Power +{0} for this turn.
   PL: W tej turze Moc Monet Plus +{0}
450. [Status [PlusCoinValueUp] — podsumowanie] 더하기 코인 위력 +{0}
   źródło: Bufs.json :: dataList[id=PlusCoinValueUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Plus Coin Power +{0}
   PL: Moc Monet Plus +{0}
451. [Status [MinusCoinValueUp] — nazwa] 빼기 코인 강화
   źródło: Bufs.json :: dataList[id=MinusCoinValueUp].name
   kontekst: identyfikator statusu w tekstach: `[MinusCoinValueUp]`
   limit: do 40 znaków
   EN: Minus Coin Boost
   PL: Wzmocnienie Monet Minus
452. [Status [MinusCoinValueUp] — opis] 이번 턴 동안 빼기 코인 위력 +{0}
   źródło: Bufs.json :: dataList[id=MinusCoinValueUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Minus Coin Power +{0} for this turn.
   PL: W tej turze Moc Monet Minus +{0}
453. [Status [MinusCoinValueUp] — podsumowanie] 빼기 코인 위력 +{0}
   źródło: Bufs.json :: dataList[id=MinusCoinValueUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Minus Coin Power +{0}
   PL: Moc Monet Minus +{0}
454. [Status [TimesCoinValueUp] — nazwa] 곱하기 코인 강화
   źródło: Bufs.json :: dataList[id=TimesCoinValueUp].name
   kontekst: identyfikator statusu w tekstach: `[TimesCoinValueUp]`
   limit: do 40 znaków
   EN: Multiply Coin Boost
   PL: Wzmocnienie Monet Mnożenia
455. [Status [TimesCoinValueUp] — opis] 이번 턴 동안 곱하기 코인 위력 +{0}
   źródło: Bufs.json :: dataList[id=TimesCoinValueUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Multiply Coin Power +{0} for this turn.
   PL: W tej turze Moc Monet Mnożenia +{0}
456. [Status [TimesCoinValueUp] — podsumowanie] 곱하기 코인 위력 +{0}
   źródło: Bufs.json :: dataList[id=TimesCoinValueUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Multiply Coin Power +{0}
   PL: Moc Monet Mnożenia +{0}
457. [Status [Disarming] — nazwa] 수비 위력 감소
   źródło: Bufs.json :: dataList[id=Disarming].name
   kontekst: identyfikator statusu w tekstach: `[Disarming]`
   limit: do 40 znaków
   EN: Defense Power Down
   PL: Spadek Mocy Obrony
458. [Status [Disarming] — opis] 이번 턴 동안 수비 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=Disarming].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności obrony -{0}
459. [Status [Disarming] — podsumowanie] 수비 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=Disarming].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: DEF Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności obrony -{0}
460. [Status [ResultReduction] — nazwa] 위력 감소
   źródło: Bufs.json :: dataList[id=ResultReduction].name
   kontekst: identyfikator statusu w tekstach: `[ResultReduction]`
   limit: do 40 znaków
   EN: Power Down
   PL: Spadek Mocy
461. [Status [ResultReduction] — opis] 이번 턴 동안 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=ResultReduction].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności -{0}
462. [Status [ResultReduction] — podsumowanie] 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=ResultReduction].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności -{0}
463. [Status [AttackDmgDown] — nazwa] 피해량 감소
   źródło: Bufs.json :: dataList[id=AttackDmgDown].name
   kontekst: identyfikator statusu w tekstach: `[AttackDmgDown]`
   limit: do 40 znaków
   EN: Damage Down
   PL: Spadek Obrażeń
464. [Status [AttackDmgDown] — opis] 이번 턴 동안 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AttackDmgDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami w tej turze (maks. 100%)
465. [Status [AttackDmgDown] — podsumowanie] 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=AttackDmgDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: -{0}0% Damage Dealt
   PL: Zadawane Obrażenia -{0}0%
466. [Status [DefenseDown] — nazwa] 방어 레벨 감소
   źródło: Bufs.json :: dataList[id=DefenseDown].name
   kontekst: identyfikator statusu w tekstach: `[DefenseDown]`
   limit: do 40 znaków
   EN: Defense Level Down
   PL: Spadek Poziomu Obrony
467. [Status [DefenseDown] — opis] 이번 턴 동안 방어 레벨 -{0}
   źródło: Bufs.json :: dataList[id=DefenseDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level -{0} for this turn.
   PL: W tej turze Poziom Obrony -{0}
468. [Status [DefenseDown] — podsumowanie] 방어 레벨 -{0}
   źródło: Bufs.json :: dataList[id=DefenseDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level -{0}
   PL: Poziom Obrony -{0}
469. [Status [Paralysis] — nazwa] 마비
   źródło: Bufs.json :: dataList[id=Paralysis].name
   kontekst: identyfikator statusu w tekstach: `[Paralysis]`
   limit: do 40 znaków
   EN: Paralyze
   PL: Paraliż
470. [Status [Paralysis] — opis] 이번 턴 동안 코인 {0}개의 값을 0으로 고정
   źródło: Bufs.json :: dataList[id=Paralysis].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Fix the Power of {0} Coin(s) to 0 for this turn.
   PL: W tej turze wartość {0} monet jest ustalona na 0
471. [Status [Paralysis] — podsumowanie] {0}개의 코인 값 0
   źródło: Bufs.json :: dataList[id=Paralysis].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Coin(s) have 0 Power
   PL: Wartość {0} monet: 0
472. [Status [PlusCoinValueDown] — nazwa] 더하기 코인 약화
   źródło: Bufs.json :: dataList[id=PlusCoinValueDown].name
   kontekst: identyfikator statusu w tekstach: `[PlusCoinValueDown]`
   limit: do 40 znaków
   EN: Plus Coin Drop
   PL: Osłabienie Monet Plus
473. [Status [PlusCoinValueDown] — opis] 이번 턴 동안 더하기 코인 위력 -{0}
   źródło: Bufs.json :: dataList[id=PlusCoinValueDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Plus Coin Power -{0} for this turn.
   PL: W tej turze Moc Monet Plus -{0}
474. [Status [PlusCoinValueDown] — podsumowanie] 더하기 코인 위력 -{0}
   źródło: Bufs.json :: dataList[id=PlusCoinValueDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Plus Coin Power -{0}
   PL: Moc Monet Plus -{0}
475. [Status [MinusCoinValueDown] — nazwa] 빼기 코인 약화
   źródło: Bufs.json :: dataList[id=MinusCoinValueDown].name
   kontekst: identyfikator statusu w tekstach: `[MinusCoinValueDown]`
   limit: do 40 znaków
   EN: Minus Coin Drop
   PL: Osłabienie Monet Minus
476. [Status [MinusCoinValueDown] — opis] 이번 턴 동안 빼기 코인 위력 -{0}
   źródło: Bufs.json :: dataList[id=MinusCoinValueDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Minus Coin Power -{0} for this turn.
   PL: W tej turze Moc Monet Minus -{0}
477. [Status [MinusCoinValueDown] — podsumowanie] 빼기 코인 위력 -{0}
   źródło: Bufs.json :: dataList[id=MinusCoinValueDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Minus Coin Power -{0}
   PL: Moc Monet Minus -{0}
478. [Status [TimesCoinValueDown] — nazwa] 곱하기 코인 약화
   źródło: Bufs.json :: dataList[id=TimesCoinValueDown].name
   kontekst: identyfikator statusu w tekstach: `[TimesCoinValueDown]`
   limit: do 40 znaków
   EN: Multiply Coin Drop
   PL: Osłabienie Monet Mnożenia
479. [Status [TimesCoinValueDown] — opis] 이번 턴 동안 곱하기 코인 위력 -{0}
   źródło: Bufs.json :: dataList[id=TimesCoinValueDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Multiply Coin Power -{0} for this turn.
   PL: W tej turze Moc Monet Mnożenia -{0}
480. [Status [TimesCoinValueDown] — podsumowanie] 곱하기 코인 위력 -{0}
   źródło: Bufs.json :: dataList[id=TimesCoinValueDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Multiply Coin Power -{0}
   PL: Moc Monet Mnożenia -{0}
481. [Status [BeingGolden] — nazwa] 황금빛
   źródło: Bufs.json :: dataList[id=BeingGolden].name
   kontekst: identyfikator statusu w tekstach: `[BeingGolden]`
   limit: do 40 znaków
   EN: Golden Sheen
   PL: Złoty Blask
482. [Status [BeingGolden] — opis] 턴 시작 시 수치당 10만큼 체력 회복
   źródło: Bufs.json :: dataList[id=BeingGolden].desc
   limit: do 120 znaków
   EN: Turn Start: Heal 10 HP per Count.
   PL: Na początku tury leczy 10 HP za każdą wartość
483. [Status [BeingGolden] — podsumowanie] 체력 회복
   źródło: Bufs.json :: dataList[id=BeingGolden].summary
   limit: do 120 znaków
   EN: HP Recovery
   PL: Odzyskiwanie HP
484. [Status [MoonLight] — nazwa] 달빛
   źródło: Bufs.json :: dataList[id=MoonLight].name
   kontekst: identyfikator statusu w tekstach: `[MoonLight]`
   limit: do 40 znaków
   EN: Moonlight
   PL: Światło Księżyca
485. [Status [MoonLight] — opis] 특정 스킬 사용 시 달빛을 소모하여 추가 효과가 발동함
   źródło: Bufs.json :: dataList[id=MoonLight].desc
   limit: do 120 znaków
   EN: Resource used by certain skills for additional effects.
   PL: Zasób zużywany przez określone Umiejętności dla dodatkowych efektów.
486. [Status [MoonLight] — podsumowanie] 추가 효과 발동
   źródło: Bufs.json :: dataList[id=MoonLight].summary
   limit: do 120 znaków
   EN: For additional effects
   PL: Dla efektów dodatkowych
487. [Status [Daunted_LowMorale] — nazwa] 위축 (사기저하)
   źródło: Bufs.json :: dataList[id=Daunted_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Daunted_LowMorale]`
   limit: do 40 znaków
   EN: Atrophied (Low Morale)
   PL: Osłabnięcie (Niskie Morale)
488. [Status [Daunted_LowMorale] — opis] 턴 시작 시 공격 위력 감소 2를 얻음
   źródło: Bufs.json :: dataList[id=Daunted_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Attack Power Down.
   PL: Na początek tury zyskuje 2 Spadki Mocy Ataku
489. [Status [Daunted_LowMorale] — podsumowanie] 공격 위력 감소 2 얻음
   źródło: Bufs.json :: dataList[id=Daunted_LowMorale].summary
   limit: do 120 znaków
   EN: Gain 2 Attack Power Down
   PL: Zyskuje 2 Spadki Mocy Ataku
490. [Status [Daunted_Panic] — nazwa] 위축
   źródło: Bufs.json :: dataList[id=Daunted_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Daunted_Panic]`
   limit: do 40 znaków
   EN: Atrophied
   PL: Osłabnięcie
491. [Status [Daunted_Panic] — opis] - 패닉\n- 턴 시작 시 공격 위력 감소 4를 얻음
   źródło: Bufs.json :: dataList[id=Daunted_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 4 Attack Power Down
   PL: - Panika\n- Na początek tury zyskuje 4 Spadki Mocy Ataku
492. [Status [Daunted_Panic] — podsumowanie] 공격 위력 감소 4 얻음
   źródło: Bufs.json :: dataList[id=Daunted_Panic].summary
   limit: do 120 znaków
   EN: Gain 4 Attack Power Down
   PL: Zyskuje 4 Spadki Mocy Ataku
493. [Status [Overwhelm_LowMorale] — nazwa] 압도 (사기저하)
   źródło: Bufs.json :: dataList[id=Overwhelm_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Overwhelm_LowMorale]`
   limit: do 40 znaków
   EN: Overwhelmed (Low Morale)
   PL: Przytłoczenie (Niskie Morale)
494. [Status [Overwhelm_LowMorale] — opis] 턴 시작 시 공격 위력 감소 2를 얻음
   źródło: Bufs.json :: dataList[id=Overwhelm_LowMorale].desc
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Status [Overwhelm_LowMorale] — podsumowanie] 공격 위력 감소 2 얻음
   źródło: Bufs.json :: dataList[id=Overwhelm_LowMorale].summary
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Status [Overwhelm_Panic] — nazwa] 압도
   źródło: Bufs.json :: dataList[id=Overwhelm_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Overwhelm_Panic]`
   limit: do 40 znaków
   EN: Overwhelmed
   PL: Przytłoczenie
497. [Status [Overwhelm_Panic] — opis] - 패닉\n- 이번 턴 동안 행동하지 않음
   źródło: Bufs.json :: dataList[id=Overwhelm_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Does not act for this turn
   PL: - Panika\n- Nie działa w tej turze
498. [Status [Overwhelm_Panic] — podsumowanie] 행동하지 않음
   źródło: Bufs.json :: dataList[id=Overwhelm_Panic].summary
   limit: do 120 znaków
   EN: Inactive
   PL: Nieaktywny
499. [Status [Anger_LowMorale] — nazwa] 분함
   źródło: Bufs.json :: dataList[id=Anger_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Anger_LowMorale]`
   limit: do 40 znaków
   EN: Agitated
   PL: Pobudzenie
500. [Status [Anger_LowMorale] — opis] - 사기저하\n- 턴 시작 시  피해량 증가 1, 취약 2를 얻음
   źródło: Bufs.json :: dataList[id=Anger_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Attack Power Up and 2 Fragile
   PL: - Niskie Morale\n- Na początek tury zyskuje 1 Wzrost Obrażeń i 2 Wrażliwości
501. [Status [Anger_LowMorale] — podsumowanie] 피해량 증가 1, 취약 2 얻음
   źródło: Bufs.json :: dataList[id=Anger_LowMorale].summary
   limit: do 120 znaków
   EN: Gain 1 Damage Up and 2 Fragile
   PL: Zyskuje 1 Wzrost Obrażeń i 2 Wrażliwości
502. [Status [Anger_Panic] — nazwa] 분함
   źródło: Bufs.json :: dataList[id=Anger_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Anger_Panic]`
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Status [Anger_Panic] — opis] - 패닉\n- 턴 시작 시  피해량 증가 2, 취약5를 얻음
   źródło: Bufs.json :: dataList[id=Anger_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Damage Up and 5 Fragile
   PL: - Panika\n- Na początek tury zyskuje 2 Wzrosty Obrażeń i 5 Wrażliwości
504. [Status [Anger_Panic] — podsumowanie] 피해량 증가 2, 취약 5 얻음
   źródło: Bufs.json :: dataList[id=Anger_Panic].summary
   limit: do 120 znaków
   EN: Gain 2 Damage Up and 5 Fragile
   PL: Zyskuje 2 Wzrosty Obrażeń i 5 Wrażliwości
505. [Status [Run_LowMorale] — nazwa] 도주
   źródło: Bufs.json :: dataList[id=Run_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Run_LowMorale]`
   limit: do 40 znaków
   EN: Running
   PL: Ucieczka
506. [Status [Run_LowMorale] — opis] 행동하지 않음. 피격 시, 해당 스킬 종료 후 사망
   źródło: Bufs.json :: dataList[id=Run_LowMorale].desc
   limit: do 120 znaków
   EN: Does not act. When hit, this unit is defeated after the skill ends.
   PL: Nie działa. Przy trafieniu ginie po zakończeniu Umiejętności.
507. [Status [Run_LowMorale] — podsumowanie] 행동하지 않음
   źródło: Bufs.json :: dataList[id=Run_LowMorale].summary
   limit: do 120 znaków
   EN: Inactive & Fleeing
   PL: Nieaktywny i ucieka
508. [Status [Nail] — nazwa] N사의 못
   źródło: Bufs.json :: dataList[id=Nail].name
   kontekst: identyfikator statusu w tekstach: `[Nail]`
   limit: do 40 znaków
   EN: N Corp’s Nails
   PL: Gwóźdź Korporacji N
509. [Status [Nail] — opis] 턴 시작 시 출혈 1을 얻고, 출혈 횟수가 {0} 증가. 턴 종료 시 수치가 1 감소
   źródło: Bufs.json :: dataList[id=Nail].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Turn Start: Gain 1 Bleed and increase the Bleed Count by {0}.\nTurn End: Reduce this effect by 1.
   PL: Na początek tury zyskuje Krwawienie 1, a Licznik Krwawienia rośnie o {0}. Na koniec tury wartość maleje o 1
510. [Status [Nail] — podsumowanie] 출혈 1 얻음. 출혈 횟수 {0} 증가
   źródło: Bufs.json :: dataList[id=Nail].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain 1 Bleed and add +{0} Bleed Count
   PL: Zyskuje Krwawienie 1. Licznik Krwawienia rośnie o {0}
511. [Status [Inactible] — nazwa] 행동 불가
   źródło: Bufs.json :: dataList[id=Inactible].name
   kontekst: identyfikator statusu w tekstach: `[Inactible]`
   limit: do 40 znaków
   EN: Immobilized
   PL: Unieruchomienie
512. [Status [Inactible] — opis] 이번 턴 동안 행동하지 않음
   źródło: Bufs.json :: dataList[id=Inactible].desc
   limit: do 120 znaków
   EN: Does not act for this turn.
   PL: Nie podejmuje działań w tej turze
513. [Status [Inactible] — podsumowanie] 행동하지 않음
   źródło: Bufs.json :: dataList[id=Inactible].summary
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Status [Combustion] — nazwa] 화상
   źródło: Bufs.json :: dataList[id=Combustion].name
   kontekst: identyfikator statusu w tekstach: `[Combustion]`
   limit: do 40 znaków
   EN: Burn
   PL: Podpalenie
515. [Status [Combustion] — opis] {1}턴 동안 턴 종료 시 {0}만큼 고정 체력 피해를 입음
   źródło: Bufs.json :: dataList[id=Combustion].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Turn End: Take {0} fixed damage. Lasts {1} turn(s).
   PL: Przez {1} tur na koniec tury otrzymuje obrażenia stałe w wysokości {0}
516. [Status [Combustion] — podsumowanie] 고정 체력 피해 -{0}
   źródło: Bufs.json :: dataList[id=Combustion].summary
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Status [Laceration] — nazwa] 출혈
   źródło: Bufs.json :: dataList[id=Laceration].name
   kontekst: identyfikator statusu w tekstach: `[Laceration]`
   limit: do 40 znaków
   EN: Bleed
   PL: Krwawienie
518. [Status [Laceration] — opis] {1}번 공격 스킬의 코인 판정 시 {0}만큼 고정 체력 피해를 받음
   źródło: Bufs.json :: dataList[id=Laceration].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: The next {1} time(s) this unit tosses an attack skill Coin, take {0} fixed damage.
   PL: Przez następne {1} rzuty Monety Umiejętności ataku otrzymuje obrażenia stałe w wysokości {0}
519. [Status [Laceration] — podsumowanie] 고정 체력 피해 -{0}
   źródło: Bufs.json :: dataList[id=Laceration].summary
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Status [Vibration] — nazwa] 진동
   źródło: Bufs.json :: dataList[id=Vibration].name
   kontekst: identyfikator statusu w tekstach: `[Vibration]`
   limit: do 40 znaków
   EN: Tremor
   PL: Wstrząs
521. [Status [Vibration] — opis] {1}턴 동안 진동 폭발 스킬로 피격 시 {0}만큼 흐트러짐 손상
   źródło: Bufs.json :: dataList[id=Vibration].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: When hit by attacks that trigger Tremor Burst, raise the Stagger Threshold by {0}. Lasts {1} turn(s).
   PL: Przez {1} tur przy trafieniu atakami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}
522. [Status [Vibration] — podsumowanie] {0}만큼 흐트러짐 손상
   źródło: Bufs.json :: dataList[id=Vibration].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Raise Stagger Threshold by {0}
   PL: Próg Oszołomienia rośnie o {0}
523. [Status [Burst] — nazwa] 파열
   źródło: Bufs.json :: dataList[id=Burst].name
   kontekst: identyfikator statusu w tekstach: `[Burst]`
   limit: do 40 znaków
   EN: Rupture
   PL: Rozdarcie
524. [Status [Burst] — opis] {1}번 피격 시 {0}만큼 고정 체력 피해를 받음
   źródło: Bufs.json :: dataList[id=Burst].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: The next {1} time(s) the unit is hit, take {0} fixed damage.
   PL: Przez następne {1} trafienia otrzymuje obrażenia stałe w wysokości {0}
525. [Status [Burst] — podsumowanie] 고정 체력 피해 -{0}
   źródło: Bufs.json :: dataList[id=Burst].summary
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Status [Sinking] — nazwa] 침잠
   źródło: Bufs.json :: dataList[id=Sinking].name
   kontekst: identyfikator statusu w tekstach: `[Sinking]`
   limit: do 40 znaków
   EN: Sinking
   PL: Zatonięcie
527. [Status [Sinking] — opis] {1}번 피격 시 {0}만큼 고정 정신력 피해를 받음. (정신력이 없는 대상에게는 우울 속성 피해로 적용됨)
   źródło: Bufs.json :: dataList[id=Sinking].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: The next {1} time(s) the unit is hit, take {0} fixed SP damage. (Non-SP Units take Gloom damage.)
   PL: Przez następne {1} trafienia: {0} stałych obrażeń Poczytalności. (Bez Poczytalności: obrażenia Posępności)
528. [Status [Sinking] — podsumowanie] 침잠 피해 -{0}
   źródło: Bufs.json :: dataList[id=Sinking].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Sinking DMG
   PL: Obrażenia Zatonięcia -{0}
529. [Status [Breath] — nazwa] 호흡
   źródło: Bufs.json :: dataList[id=Breath].name
   kontekst: identyfikator statusu w tekstach: `[Breath]`
   limit: do 40 znaków
   EN: Poise
   PL: Oddech
530. [Status [Breath] — opis] {1}회 적중 시 크리티컬 확률 {0}x5%만큼 증가
   źródło: Bufs.json :: dataList[id=Breath].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Boost critical hit chance by {0}x5% for the next {1} hit(s).
   PL: Przez następne {1} trafienia szansa trafienia krytycznego rośnie o {0}x5%
531. [Status [Breath] — podsumowanie] 크리티컬 확률 {0}x5%
   źródło: Bufs.json :: dataList[id=Breath].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}x5% crit chance
   PL: Szansa trafienia krytycznego {0}x5%
532. [Status [BloodPocket] — nazwa] 피주머니
   źródło: Bufs.json :: dataList[id=BloodPocket].name
   kontekst: identyfikator statusu w tekstach: `[BloodPocket]`
   limit: do 40 znaków
   EN: Blood Sac
   PL: Sakiewka Krwi
533. [Status [BloodPocket] — opis] 특정 수치에 강력한 공격을 사용
   źródło: Bufs.json :: dataList[id=BloodPocket].desc
   limit: do 120 znaków
   EN: Use a powerful attack at a certain Count.
   PL: Używa potężnego ataku przy określonej wartości
534. [Status [BloodPocket] — podsumowanie] 강력한 공격 사용
   źródło: Bufs.json :: dataList[id=BloodPocket].summary
   limit: do 120 znaków
   EN: Readies a powerful attack
   PL: Przygotowuje potężny atak
535. [Status [WaterPocket] — nazwa] 물주머니
   źródło: Bufs.json :: dataList[id=WaterPocket].name
   kontekst: identyfikator statusu w tekstach: `[WaterPocket]`
   limit: do 40 znaków
   EN: Fluid Sac
   PL: Sakiewka Wody
536. [Status [WaterPocket] — opis] {0}x20만큼 체력을 회복
   źródło: Bufs.json :: dataList[id=WaterPocket].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Heals {0} x 20 HP.
   PL: Odzyskuje {0} x 20 HP
537. [Status [WaterPocket] — podsumowanie] 체력 회복량 증가
   źródło: Bufs.json :: dataList[id=WaterPocket].summary
   limit: do 120 znaków
   EN: HP heal boost
   PL: Wzrost Leczenia HP
538. [Status [DogThunder] — nazwa] 번개
   źródło: Bufs.json :: dataList[id=DogThunder].name
   kontekst: identyfikator statusu w tekstach: `[DogThunder]`
   limit: do 40 znaków
   EN: Lightning
   PL: Piorun
539. [Status [DogThunder] — opis] 특정 수치에 자신을 강화
   źródło: Bufs.json :: dataList[id=DogThunder].desc
   limit: do 120 znaków
   EN: Powers up at a certain Count.
   PL: Wzmacnia się przy określonej wartości
540. [Status [DogThunder] — podsumowanie] 자신 강화
   źródło: Bufs.json :: dataList[id=DogThunder].summary
   limit: do 120 znaków
   EN: Strengthens self
   PL: Wzmacnia się
541. [Status [Run_Panic] — nazwa] 압도
   źródło: Bufs.json :: dataList[id=Run_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Run_Panic]`
   limit: do 40 znaków
   EN: Oppression
   PL: Przytłoczenie
542. [Status [Run_Panic] — opis] 이번 턴 동안 행동 불가. 피격 시 공격자의 스킬이 종료된 후 도주함.
   źródło: Bufs.json :: dataList[id=Run_Panic].desc
   limit: do 120 znaków
   EN: Does not act. When hit, this unit is defeated after the skill ends.
   PL: Nie może działać w tej turze. Przy trafieniu ucieka po zakończeniu Umiejętności atakującego.
543. [Status [Run_Panic] — podsumowanie] 행동하지 않음
   źródło: Bufs.json :: dataList[id=Run_Panic].summary
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Status [Operation] — nazwa] 시술
   źródło: Bufs.json :: dataList[id=Operation].name
   kontekst: identyfikator statusu w tekstach: `[Operation]`
   limit: do 40 znaków
   EN: Surgery
   PL: Zabieg
545. [Status [Operation] — opis] 이 수치가 5가 되면 사망함\n최대 체력이 수치에 비례하여 20%씩 감소 \n가하는 피해량이 수치에 비례하여 20%씩 증가\n신속 {0}을 얻음
   źródło: Bufs.json :: dataList[id=Operation].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Die when Count reaches 5.\nReduce Max HP by 20% per Count ({0}).\nDeal +20% damage per Count ({0}).\nTurn Start: Gain {0} Haste.
   PL: Umiera, gdy wartość osiągnie 5\nMaks. HP maleje o 20% za każdą wartość\nZadawane obrażenia rosną o 20% za każdą wartość\nZyskuje {0} Pośpiechu
546. [Status [Operation] — podsumowanie] 시술 5가 되면 사망
   źródło: Bufs.json :: dataList[id=Operation].summary
   limit: do 120 znaków
   EN: Dies at 5 Count
   PL: Umiera przy wartości 5
547. [Status [Emergency_Operation] — nazwa] 긴급 시술
   źródło: Bufs.json :: dataList[id=Emergency_Operation].name
   kontekst: identyfikator statusu w tekstach: `[Emergency_Operation]`
   limit: do 40 znaków
   EN: Makeshift Surgery
   PL: Zabieg Polowy
548. [Status [Emergency_Operation] — opis] 자신의 '긴급 시술' 수에 비례하여 최대 체력이 25%, 위력이 1만큼 증가함.\nn매 턴마다 '긴급 시술'을 1 얻음\n'긴급 시술'이 5가 될 경우, 사망함
   źródło: Bufs.json :: dataList[id=Emergency_Operation].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Boost Max HP by 25% and skill Power by 1 per this effect’s Count.\nEach turn, increase this effect’s Count by 1.\nDie when Count reaches 5.
   PL: Maks. HP rośnie o 25%, a Moc Umiejętności o 1, proporcjonalnie do liczby własnych „Zabiegów Polowych”.\nCo turę zyskuje 1 „Zabiegu Polowego”\nGdy „Zabieg Polowy” osiągnie 5, umiera
549. [Status [Emergency_Operation] — podsumowanie] 긴급 시술 5가 되면 사망
   źródło: Bufs.json :: dataList[id=Emergency_Operation].summary
   limit: do 120 znaków
   EN: Dies at 5 Count
   PL: Umiera, gdy Zabieg Polowy osiągnie 5
550. [Status [BabayagaTimeLimit] — nazwa] 다가오는 바바야가
   źródło: Bufs.json :: dataList[id=BabayagaTimeLimit].name
   kontekst: identyfikator statusu w tekstach: `[BabayagaTimeLimit]`
   limit: do 40 znaków
   EN: Baba Yaga’s Coming!
   PL: Nadchodząca Baba Jaga
551. [Status [BabayagaTimeLimit] — opis] 바바야가가 당신에게 다가오고 있습니다. 달아나지 못하면 죽음을 맞이합니다.
   źródło: Bufs.json :: dataList[id=BabayagaTimeLimit].desc
   limit: do 120 znaków
   EN: Baba Yaga is closing in. Clear the way or face certain death.
   PL: Baba Jaga się do ciebie zbliża. Jeśli nie uciekniesz, czeka cię śmierć.
552. [Status [BabayagaTimeLimit] — podsumowanie] 바바야가가 다가옵니다
   źródło: Bufs.json :: dataList[id=BabayagaTimeLimit].summary
   limit: do 120 znaków
   EN: Baba Yaga approaches!
   PL: Nadchodzi Baba Jaga
553. [Status [PinkRibbon_Ishmael] — nazwa] 분홍 리본
   źródło: Bufs.json :: dataList[id=PinkRibbon_Ishmael].name
   kontekst: identyfikator statusu w tekstach: `[PinkRibbon_Ishmael]`
   limit: do 40 znaków
   EN: Pink Ribbons
   PL: Różowa Wstążka
554. [Status [PinkRibbon_Ishmael] — opis] 한 턴동안 공격 스킬의 코인을 사용할 때마다 수치 증가\n턴 종료 시 수치만큼 속박을 얻은 뒤 효과 소멸
   źródło: Bufs.json :: dataList[id=PinkRibbon_Ishmael].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Count by 1 whenever the unit tosses an attack skill Coin.\nTurn End: Gain Bind by the Count, then remove this effect.
   PL: W ciągu tury wartość rośnie przy każdym rzucie Monety Umiejętności ataku\nNa koniec tury zyskuje Spętanie równe wartości, po czym efekt znika
555. [Status [PinkRibbon_Ishmael] — podsumowanie] 속박 +{0}
   źródło: Bufs.json :: dataList[id=PinkRibbon_Ishmael].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain {0} Bind
   PL: Spętanie +{0}
556. [Status [Muckworm] — nazwa] 구더기
   źródło: Bufs.json :: dataList[id=Muckworm].name
   kontekst: identyfikator statusu w tekstach: `[Muckworm]`
   limit: do 40 znaków
   EN: Maggots
   PL: Czerwie
557. [Status [Muckworm] — opis] 턴 종료 시 수치만큼 탐식 피해를 받고, 출혈 횟수가 1 증가한 뒤 수치 1 감소
   źródło: Bufs.json :: dataList[id=Muckworm].desc
   limit: do 120 znaków
   EN: Turn End: Take Gluttony damage by the Count, then lower it by 1; Bleed Count +1.
   PL: Na koniec tury otrzymuje tyle obrażeń Obżarstwem, ile wynosi Licznik; Licznik Krwawienia +1, a wartość maleje o 1
558. [Status [Muckworm] — podsumowanie] 수치만큼 탐식 피해. 출혈 횟수 1 증가
   źródło: Bufs.json :: dataList[id=Muckworm].summary
   limit: do 120 znaków
   EN: Gluttony damage; Bleed Count +1
   PL: Obrażenia Obżarstwa równe wartości. Licznik Krwawienia +1
559. [Status [AttackUp] — nazwa] 공격 레벨 증가
   źródło: Bufs.json :: dataList[id=AttackUp].name
   kontekst: identyfikator statusu w tekstach: `[AttackUp]`
   limit: do 40 znaków
   EN: Offense Level Up
   PL: Wzrost Poziomu Ataku
560. [Status [AttackUp] — opis] 이번 턴 동안 공격 레벨 +{0}
   źródło: Bufs.json :: dataList[id=AttackUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level +{0} for this turn.
   PL: W tej turze Poziom Ataku +{0}
561. [Status [AttackUp] — podsumowanie] 공격 레벨 +{0}
   źródło: Bufs.json :: dataList[id=AttackUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level +{0}
   PL: Poziom Ataku +{0}
562. [Status [AttackDown] — nazwa] 공격 레벨 감소
   źródło: Bufs.json :: dataList[id=AttackDown].name
   kontekst: identyfikator statusu w tekstach: `[AttackDown]`
   limit: do 40 znaków
   EN: Offense Level Down
   PL: Spadek Poziomu Ataku
563. [Status [AttackDown] — opis] 이번 턴 동안 공격 레벨 -{0}
   źródło: Bufs.json :: dataList[id=AttackDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level -{0} for this turn.
   PL: W tej turze Poziom Ataku -{0}
564. [Status [AttackDown] — podsumowanie] 공격 레벨 -{0}
   źródło: Bufs.json :: dataList[id=AttackDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level -{0}
   PL: Poziom Ataku -{0}
565. [Status [Liu_Meursault_Guard_Buff] — nazwa] 태산
   źródło: Bufs.json :: dataList[id=Liu_Meursault_Guard_Buff].name
   kontekst: identyfikator statusu w tekstach: `[Liu_Meursault_Guard_Buff]`
   limit: do 40 znaków
   EN: Great Mountain
   PL: Wielka Góra
566. [Status [Liu_Meursault_Guard_Buff] — opis] 피격 시 화상 횟수 1 증가
   źródło: Bufs.json :: dataList[id=Liu_Meursault_Guard_Buff].desc
   limit: do 120 znaków
   EN: When attacked, inflict +1 Burn Count on the attacker.
   PL: Przy trafieniu Licznik Podpalenia atakującego rośnie o 1
567. [Status [Liu_Meursault_Guard_Buff] — podsumowanie] 화상 횟수 1 증가
   źródło: Bufs.json :: dataList[id=Liu_Meursault_Guard_Buff].summary
   limit: do 120 znaków
   EN: Attacker Burn Count +1
   PL: Licznik Podpalenia atakującego +1
568. [Status [SlashResistUp] — nazwa] 참격 내성 강화
   źródło: Bufs.json :: dataList[id=SlashResistUp].name
   kontekst: identyfikator statusu w tekstach: `[SlashResistUp]`
   limit: do 40 znaków
   EN: Slash Resist Up
   PL: Wzmocnienie Odporności na Cięcie
569. [Status [SlashResistUp] — opis] 대상의 참격 내성을 {0:F1} 감소
   źródło: Bufs.json :: dataList[id=SlashResistUp].desc
   limit: do 120 znaków
   EN: Reduce Slash Resistance by {0:F1}
   PL: Zmniejsza Odporność celu na Cięcie o {0:F1}
570. [Status [PenetrateResistUp] — nazwa] 관통 내성 강화
   źródło: Bufs.json :: dataList[id=PenetrateResistUp].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateResistUp]`
   limit: do 40 znaków
   EN: Pierce Resist Up
   PL: Wzmocnienie Odporności na Przebicie
571. [Status [PenetrateResistUp] — opis] 대상의 관통 내성을 {0:F1} 감소
   źródło: Bufs.json :: dataList[id=PenetrateResistUp].desc
   limit: do 120 znaków
   EN: Reduce Pierce Resistance by {0:F1}
   PL: Zmniejsza Odporność celu na Przebicie o {0:F1}
572. [Status [HitResistUp] — nazwa] 타격 내성 강화
   źródło: Bufs.json :: dataList[id=HitResistUp].name
   kontekst: identyfikator statusu w tekstach: `[HitResistUp]`
   limit: do 40 znaków
   EN: Blunt Resist Up
   PL: Wzmocnienie Odporności na Uderzenie
573. [Status [HitResistUp] — opis] 대상의 타격 내성을 {0:F1} 감소
   źródło: Bufs.json :: dataList[id=HitResistUp].desc
   limit: do 120 znaków
   EN: Reduce Blunt Resistance by {0:F1}
   PL: Zmniejsza Odporność celu na Uderzenie o {0:F1}
574. [Status [SlashDamageUp] — nazwa] 참격 피해량 증가
   źródło: Bufs.json :: dataList[id=SlashDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[SlashDamageUp]`
   limit: do 40 znaków
   EN: Slash DMG Up
   PL: Wzrost Obrażeń Cięcia
575. [Status [SlashDamageUp] — opis] 이번 턴 동안 참격 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=SlashDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Slash skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Cięcia w tej turze (maks. 100%)
576. [Status [SlashDamageUp] — podsumowanie] 참격 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=SlashDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash damage +{0}0%
   PL: Obrażenia Cięcia +{0}0%
577. [Status [PenetrateDamageUp] — nazwa] 관통 피해량 증가
   źródło: Bufs.json :: dataList[id=PenetrateDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateDamageUp]`
   limit: do 40 znaków
   EN: Pierce DMG Up
   PL: Wzrost Obrażeń Przebicia
578. [Status [PenetrateDamageUp] — opis] 이번 턴 동안 관통 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=PenetrateDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Pierce skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Przebicia w tej turze (maks. 100%)
579. [Status [PenetrateDamageUp] — podsumowanie] 관통 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=PenetrateDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce damage +{0}0%
   PL: Obrażenia Przebicia +{0}0%
580. [Status [HitDamageUp] — nazwa] 타격 피해량 증가
   źródło: Bufs.json :: dataList[id=HitDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[HitDamageUp]`
   limit: do 40 znaków
   EN: Blunt DMG Up
   PL: Wzrost Obrażeń Uderzenia
581. [Status [HitDamageUp] — opis] 이번 턴 동안 타격 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=HitDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Blunt skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Uderzenia w tej turze (maks. 100%)
582. [Status [HitDamageUp] — podsumowanie] 타격 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=HitDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt damage +{0}0%
   PL: Obrażenia Uderzenia +{0}0%
583. [Status [SlashResistDown] — nazwa] 참격 내성 약화
   źródło: Bufs.json :: dataList[id=SlashResistDown].name
   kontekst: identyfikator statusu w tekstach: `[SlashResistDown]`
   limit: do 40 znaków
   EN: Slash Resist Down
   PL: Osłabienie Odporności na Cięcie
584. [Status [SlashResistDown] — opis] 대상의 참격 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=SlashResistDown].desc
   limit: do 120 znaków
   EN: Increase Slash Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Cięcie o {0:F1}
585. [Status [PenetrateResistDown] — nazwa] 관통 내성 약화
   źródło: Bufs.json :: dataList[id=PenetrateResistDown].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateResistDown]`
   limit: do 40 znaków
   EN: Pierce Resist Down
   PL: Osłabienie Odporności na Przebicie
586. [Status [PenetrateResistDown] — opis] 대상의 관통 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=PenetrateResistDown].desc
   limit: do 120 znaków
   EN: Increase Pierce Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Przebicie o {0:F1}
587. [Status [HitResistDown] — nazwa] 타격 내성 약화
   źródło: Bufs.json :: dataList[id=HitResistDown].name
   kontekst: identyfikator statusu w tekstach: `[HitResistDown]`
   limit: do 40 znaków
   EN: Blunt Resist Down
   PL: Osłabienie Odporności na Uderzenie
588. [Status [HitResistDown] — opis] 대상의 타격 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=HitResistDown].desc
   limit: do 120 znaków
   EN: Increase Blunt Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Uderzenie o {0:F1}
589. [Status [SlashDamageDown] — nazwa] 참격 피해량 감소
   źródło: Bufs.json :: dataList[id=SlashDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[SlashDamageDown]`
   limit: do 40 znaków
   EN: Slash DMG Down
   PL: Spadek Obrażeń Cięcia
590. [Status [SlashDamageDown] — opis] 이번 턴 동안 참격 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=SlashDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Slash skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Cięcia w tej turze (maks. 100%)
591. [Status [SlashDamageDown] — podsumowanie] 참격 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=SlashDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash damage -{0}0%
   PL: Obrażenia Cięcia -{0}0%
592. [Status [PenetrateDamageDown] — nazwa] 관통 피해량 감소
   źródło: Bufs.json :: dataList[id=PenetrateDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateDamageDown]`
   limit: do 40 znaków
   EN: Pierce DMG Down
   PL: Spadek Obrażeń Przebicia
593. [Status [PenetrateDamageDown] — opis] 이번 턴 동안 관통 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=PenetrateDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Pierce skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Przebicia w tej turze (maks. 100%)
594. [Status [PenetrateDamageDown] — podsumowanie] 관통 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=PenetrateDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce damage -{0}0%
   PL: Obrażenia Przebicia -{0}0%
595. [Status [HitDamageDown] — nazwa] 타격 피해량 감소
   źródło: Bufs.json :: dataList[id=HitDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[HitDamageDown]`
   limit: do 40 znaków
   EN: Blunt DMG Down
   PL: Spadek Obrażeń Uderzenia
596. [Status [HitDamageDown] — opis] 이번 턴 동안 타격 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=HitDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Blunt skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Uderzenia w tej turze (maks. 100%)
597. [Status [HitDamageDown] — podsumowanie] 타격 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=HitDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt damage -{0}0%
   PL: Obrażenia Uderzenia -{0}0%
598. [Status [CrimsonResistDown] — nazwa] 분노 내성 약화
   źródło: Bufs.json :: dataList[id=CrimsonResistDown].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonResistDown]`
   limit: do 40 znaków
   EN: Wrath Resist Down
   PL: Osłabienie Odporności na Gniew
599. [Status [CrimsonResistDown] — opis] 대상의 분노 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=CrimsonResistDown].desc
   limit: do 120 znaków
   EN: Increase Wrath Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Gniew o {0:F1}
600. [Status [ScarletResistDown] — nazwa] 색욕 내성 약화
   źródło: Bufs.json :: dataList[id=ScarletResistDown].name
   kontekst: identyfikator statusu w tekstach: `[ScarletResistDown]`
   limit: do 40 znaków
   EN: Lust Resist Down
   PL: Osłabienie Odporności na Żądzę
601. [Status [ScarletResistDown] — opis] 대상의 색욕 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=ScarletResistDown].desc
   limit: do 120 znaków
   EN: Increase Lust Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Żądzę o {0:F1}
602. [Status [AmberResistDown] — nazwa] 나태 내성 약화
   źródło: Bufs.json :: dataList[id=AmberResistDown].name
   kontekst: identyfikator statusu w tekstach: `[AmberResistDown]`
   limit: do 40 znaków
   EN: Sloth Resist Down
   PL: Osłabienie Odporności na Lenistwo
603. [Status [AmberResistDown] — opis] 대상의 나태 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=AmberResistDown].desc
   limit: do 120 znaków
   EN: Increase Sloth Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Lenistwo o {0:F1}
604. [Status [ShamrockResistDown] — nazwa] 탐식 내성 약화
   źródło: Bufs.json :: dataList[id=ShamrockResistDown].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockResistDown]`
   limit: do 40 znaków
   EN: Gluttony Resist Down
   PL: Osłabienie Odporności na Obżarstwo
605. [Status [ShamrockResistDown] — opis] 대상의 탐식 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=ShamrockResistDown].desc
   limit: do 120 znaków
   EN: Increase Gluttony Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Obżarstwo o {0:F1}
606. [Status [AzureResistDown] — nazwa] 우울 내성 약화
   źródło: Bufs.json :: dataList[id=AzureResistDown].name
   kontekst: identyfikator statusu w tekstach: `[AzureResistDown]`
   limit: do 40 znaków
   EN: Gloom Resist Down
   PL: Osłabienie Odporności na Posępność
607. [Status [AzureResistDown] — opis] 대상의 우울 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=AzureResistDown].desc
   limit: do 120 znaków
   EN: Increase Gloom Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Posępność o {0:F1}
608. [Status [IndigoResistDown] — nazwa] 오만 내성 약화
   źródło: Bufs.json :: dataList[id=IndigoResistDown].name
   kontekst: identyfikator statusu w tekstach: `[IndigoResistDown]`
   limit: do 40 znaków
   EN: Pride Resist Down
   PL: Osłabienie Odporności na Pychę
609. [Status [IndigoResistDown] — opis] 대상의 오만 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=IndigoResistDown].desc
   limit: do 120 znaków
   EN: Increase Pride Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Pychę o {0:F1}
