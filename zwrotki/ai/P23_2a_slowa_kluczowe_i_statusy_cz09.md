# Paczka AI P23 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 9/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P23_2a_slowa_kluczowe_i_statusy_cz09.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P23_2a_slowa_kluczowe_i_statusy_cz09.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs-a1c10p3
- plik gry: `Bufs-a1c10p3.json`

1. [Status [JeanneManager] — nazwa] 앙가즈망(engagement)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneManager].name
   kontekst: identyfikator statusu w tekstach: `[JeanneManager]`
   limit: do 40 znaków
   EN: Engagement
   PL: Engagement
2. [Status [JeanneManager] — opis] - <color=#ff6000><mark color=#ff000040><b><u>자신의 코인 앞면 확률 100% 고정</color></mark></b></u>\n- 자신과 합을 진행하거나 자신을 공격하는 <color=#ff6000><mark color=#ff000040><b><u>대상의 스킬 더하기 코인 뒷면 확률 100% 고정</color></mark></b></u>\n· 빼기 코인이면, 앞면 코인 확률 100% 고정\n- 포착 스킬 장착 또는 흐트러짐 시 효과 해제
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneManager].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - <color=#ff6000><mark color=#ff000040><b><u>This unit has 100% chance to flip Heads</color></mark></b></u>\n- Targets Clashing with or attacking this unit have <color=#ff6000><mark color=#ff000040><b><u>100% chance to flip Tails for Plus Coins</color></mark></b></u>\n · The said units' Minus Coins have 100% chance to flip Heads\n- Remove this effect upon equipping the "Focusing" Skill, or if this unit becomes Staggered
   PL: - <color=#ff6000><mark color=#ff000040><b><u>Szanse na Awers własnych Monet zamrożone na 100%</u></b></mark></color>\n- Cele prowadzące z nim Starcie lub atakujące go mają <color=#ff6000><mark color=#ff000040><b><u>Monety Plus o zamrożonych szansach na Rewers wynoszących 100%</u></b></mark></color>\n· Monety Minus tych jednostek mają 100% szans na Awers\n- Efekt znika po wyposażeniu Umiejętności „Skupienie” lub gdy jednostka zostanie oszołomiona
3. [Status [JeanneManager] — tekst klimatyczny] 나는 백화점을 세웠어. 그리고 지금은 런웨이 위의 모델이자, 무대 위의 배우지.\n\n마 퓌스, 당신은… 시네마겠지?
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneManager].flavor
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I designed the department store. And now, I'm a model on its runway, an actress on its stage.\n\nAnd you, ma puce... you'd be the cinéma itself, wouldn't you?
   PL: Zaprojektowałam Grand Magasin. A teraz jestem modelą na jego wybiegu i aktorką na jego scenie.\n\nA ty, ma puce... tobą będzie samo kino, nieprawdaż?
4. [Status [JeannePartner] — nazwa] 에트르 뿌르 오트뤼(être-pour-autrui)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePartner].name
   kontekst: identyfikator statusu w tekstach: `[JeannePartner]`
   limit: do 40 znaków
   EN: Être-pour-autrui
   PL: Être-pour-autrui
5. [Status [JeannePartner] — opis] - 이 효과 획득 시 대상의 모든 부정적인 효과 제거\n- 정신력을 45로 고정\n· 빼기 코인을 사용하는 인격일 경우, 정신력을 -30으로 고정\n- 흐트러짐 상태가 되지 않음\n- 잔느의 페이즈 변경 시 제거
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePartner].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Targets that gain this effect lose all negative effects\n- Fix SP to 45\n · For Minus Coin Identities, fix SP to -30\n- Cannot be Staggered\n- Remove this effect when Jeanne enters a new phase
   PL: - Przy zdobyciu tego efektu cel traci wszystkie negatywne efekty\n- Zamraża Poczytalność na 45\n· Dla Tożsamości używających Monet Minus zamraża Poczytalność na -30\n- Nie może ulec Oszołomieniu\n- Znika, gdy Jeanne zmienia fazę
6. [Status [JeannePartner] — tekst klimatyczny] 당신은 내게 어떻게 보여지고 있을 것 같아?\n당신이 보는 자기 자신과 내가 보는 당신은 전혀 다를 거야.\n마 퓌스, 당신은 내 안에서 못 박혔어.
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePartner].flavor
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: How do you suppose you look to me? The self you see and the you I see must be entirely different.\nMa puce... you've already been nailed into place within me.
   PL: Jak sądzisz, jak wyglądasz w moich oczach?\nTy, którego widzisz siebie, a ty, którego widzę ja, będą zupełnie różne.\nMa puce... jesteś już przybity gwoździem we mnie.
7. [Status [JeannePartnerTwo] — nazwa] 에트르 뿌르 수아(être-pour-soi)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePartnerTwo].name
   kontekst: identyfikator statusu w tekstach: `[JeannePartnerTwo]`
   limit: do 40 znaków
   EN: Être-pour-soi
   PL: Être-pour-soi
8. [Status [JeannePartnerTwo] — opis] - 정신력을 45로 고정\n- 피해를 받지 않음\n- 잔느의 페이즈 변경 시 제거
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePartnerTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Fix SP to 45\n- Does not take damage\n- Remove this effect when Jeanne enters a new phase
   PL: - Zamraża Poczytalność na 45\n- Nie otrzymuje obrażeń\n- Znika, gdy Jeanne zmienia fazę
9. [Status [JeannePartnerTwo] — tekst klimatyczny] 의식을 가진다는 건 무서운 일이야. 어딘가 구멍이 생겨버릴 수밖에 없거든.\n\n채워줄래, 마 퓌스?
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePartnerTwo].flavor
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Consciousness is a frightening thing, you know. Somewhere within it, a hollow is bound to open.\n\nWill you fill it for me, ma puce?
   PL: Posiadanie świadomości to przerażająca rzecz. Gdzieś w niej nieuchronnie otwiera się dziura.\n\nWypełnisz ją dla mnie, ma puce?
10. [Status [JeannePathos] — nazwa] 파토스 - 데지르 데트르(désir d'être)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePathos].name
   kontekst: identyfikator statusu w tekstach: `[JeannePathos]`
   limit: do 40 znaków
   EN: Pathos - Désir d'être
   PL: Pathos - Désir d'être
11. [Status [JeannePathos] — opis] - 최댓값: 100\n- 합 승리시 3 증가\n- 합 패배시 5 증가\n- 합 횟수만큼 증가\n- 턴 종료시 최댓값이면, 페이즈를 변경함
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePathos].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- On Clash Win, gain 3 Stacks\n- On Clash Lose, gain 5 Stacks\n- Gain Stack equal to Clash count\n- Turn End: At max Stack, enter a new phase
   PL: - Maks. ładunków: 100\n- Po wygranym Starciu zyskuje 3 ładunków\n- Po przegranej w Starciu zyskuje 5 ładunków\n- Zyskuje ładunki w liczbie Stareć\n- Na koniec tury przy Maks. ładunków zmienia fazę
12. [Status [JeannePathos] — tekst klimatyczny] 열정과 정열. 붉은 파토스로 난 붉게 피어나고 싶었어.
   źródło: Bufs-a1c10p3.json :: dataList[id=JeannePathos].flavor
   limit: do 140 znaków
   EN: I wanted to bloom red... with all that red passion, all that fervor, all that pathos burning within me.
   PL: Pasja i namiętność. Chciałam rozkwitnąć czerwono — w tym czerwonym patosie.
13. [Status [JeanneLogos] — nazwa] 로고스 - 망끄 데트르(manque d'être)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneLogos].name
   kontekst: identyfikator statusu w tekstach: `[JeanneLogos]`
   limit: do 40 znaków
   EN: Logos - Manque d'être
   PL: Logos - Manque d'être
14. [Status [JeanneLogos] — opis] - 최댓값: 100\n- 합 승리시 5 증가\n- 합 횟수만큼 증가\n- 수치 10당 공격 레벨 +1\n- 수치 20당 합 위력 +1
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneLogos].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- On Clash Win, gain 5 Stacks\n- Gain Stack equal to Clash count\n- Offense Level +1 for every 10 Stacks\n- Clash Power +1 for every 20 Stacks
   PL: - Maks. ładunków: 100\n- Po wygranym Starciu zyskuje 5 ładunków\n- Zyskuje ładunki w liczbie odbytych Stareć\n- Poziom Ataku +1 za każde 10 ładunków\n- Moc Starcia +1 za każde 20 ładunków
15. [Status [JeanneLogos] — tekst klimatyczny] 당신에게는 무언가 결여되어 있어. 나도 그렇지. 그러니까 서로 채워줄 수 있어.
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneLogos].flavor
   limit: do 120 znaków
   EN: There's something missing in you—in me, too. We can fill each other.
   PL: Czemuś w tobie czegoś brakuje. We mnie także. Dlatego możemy się nawzajem wypełnić.
16. [Status [JeanneCheat] — nazwa] 데제스푸아르(désespoir)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneCheat].name
   kontekst: identyfikator statusu w tekstach: `[JeanneCheat]`
   limit: do 40 znaków
   EN: Désespoir
   PL: Désespoir
17. [Status [JeanneCheat] — opis] - 코인 뒷면 확률 100%로 고정 (빼기 코인일 경우, 앞면으로 고정)\n- 턴 종료시 1 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneCheat].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This unit has 100% chance to flip Tails (for Minus Coins, Heads)\n- Turn End: Lose 1 Stack
   PL: - Szanse na Rewers Monet zamrożone na 100% (dla Monet Minus — na Awers)\n- Na koniec tury traci 1 ładunek
18. [Status [JeanneCheat] — tekst klimatyczny] …마 퓌스, 도피할 거야? 판단으로부터, 이 빛으로부터…
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneCheat].flavor
   limit: do 120 znaków
   EN: ... Ma puce, are you running away? From judgment, from this light...?
   PL: ...Ma puce, uciekasz? Od sądu, od tego światła...?
19. [Status [JeanneBlueprint] — nazwa] 델레스망(délaissement)
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneBlueprint].name
   kontekst: identyfikator statusu w tekstach: `[JeanneBlueprint]`
   limit: do 40 znaków
   EN: Délaissement
   PL: Délaissement
20. [Status [JeanneBlueprint] — opis] - 최댓값: 5\n- 수치당 합 위력 +1\n- 수치당 스킬로 받는 피해량 +10%\n- 턴 시작시 4이상이면, 아래 효과 적용\n· 모든 흐트러짐 선 제거\n· 흐트러짐 시 흐트러짐 상태 해제\n· 슬롯 가중치 +1
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneBlueprint].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Clash Power +1 for every Stack\n- Take +10% damage from Skills for every Stack\n- Turn Start: At 4+ Stacks, apply the following effects:\n · Remove all Stagger Thresholds\n · When Staggered, recover from Stagger\n · Slot Weight +1
   PL: - Maks. ładunków: 5\n- Moc Starcia +1 za każdy ładunek\n- Otrzymuje obrażenia +10% od Umiejętności za każdy ładunek\n- Na początku tury przy 4 lub więcej ładunkach stosowane są następujące efekty:\n· Usunięcie wszystkich Progów Oszołomienia\n· Po Oszołomieniu wychodzi z Oszołomienia\n· Waga Slotu +1
21. [Status [JeanneBlueprint] — tekst klimatyczny] 그 무엇도 보장해 주지 않는 절망적 자유 속에서도, 시지프 백화점 안에서만큼은 설계와 시선에 따라 재단되고, 유지되는 축복을 누릴 수 있다.
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneBlueprint].flavor
   limit: do 250 znaków
   EN: Amid the freedom of despair that promises nothing, Grand Magasin Sisyphe alone offers a blessing: to be cut to measure by design and gaze, and in doing so, be given certainty and continuity.
   PL: Nawet w rozpaczliwej wolności, która niczego nie gwarantuje, wewnątrz Grand Magasin Sisyphe można cieszyć się błogosławieństwem bycia skrojonym wedle projektu i spojrzenia — i utrwalonym.
22. [Status [BoneNail] — nazwa] 라브젝트(l'abject)
   źródło: Bufs-a1c10p3.json :: dataList[id=BoneNail].name
   kontekst: identyfikator statusu w tekstach: `[BoneNail]`
   limit: do 40 znaków
   EN: L'Abject
   PL: L'Abject
23. [Status [BoneNail] — opis] - 최댓값 : 5\n- 수치 1당, 속도 1 감소\n- 수치 1당, 출혈로 받는 피해 +20% (소수점 버림)\n- 기본 공격 스킬 사용 시, 수치만큼 자신의 출혈 횟수 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=BoneNail].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Lose 1 Speed for every Stack\n- Take +20% damage from Bleed for every Stack (rounded down)\n- On Base Attack Skill Use, gain Bleed Count equal to Stack
   PL: - Maks. ładunków: 5\n- Traci 1 Szybkości za każdy ładunek\n- Otrzymuje +20% obrażeń od Krwawienia za każdy ładunek (zaokr. w dół)\n- Przy użyciu Umiejętności ataku podstawowego zyskuje Licznik Krwawienia równy ładunkom
24. [Status [BoneNail] — tekst klimatyczny] 내던져진 부속기관. 뷔페가 밀어내고, 뱉어내고, 쏟아냈다.\n\n자신의 몸에서 나왔으나, 밖으로 나온 이상 자신의 것이 아니다. 그러나 설령 상대에게 박히게 되더라도, 그것은 상대의 것이 아니다.
   źródło: Bufs-a1c10p3.json :: dataList[id=BoneNail].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A cast-off appendage. Buffet pushed it out, spat it forth, spilled it from within.\n\nThough it came from one's own body, once cast outside, it ceased to belong to the self. And even should it be inserted into another, it would never belong to that body either.
   PL: Odrzucona przydatka. Buffet ją wypchnął, wypluł, wylał z siebie.\n\nChoć przyszła z własnego ciała, skoro znalazła się na zewnątrz, przestała być swoją. A nawet gdyby przybić ją w czyimś ciele, nie stanie się jego.
25. [Status [BuffetDream] — nazwa] 뿌이의 기억
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDream]`
   limit: do 40 znaków
   EN: Pwie's Memories
   PL: Wspomnienia Pwie
26. [Status [BuffetDream] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- For every Stack,\n · Base Offense Level -5\n · Base Defense Level -5\n · Clash Power -1\n- Turn Start: Heal (8 x Stack) SP
   PL: - Maks. ładunków: 5\n- Za każdy ładunek Podstawowy Poziom Ataku -5, Podstawowy Poziom Obrony -5, Moc Starcia -1\n- Na początku tury odzyskuje Poczytalność (8 x ładunki)
27. [Status [BuffetDream1] — nazwa] 뿌이의 기억
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream1].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDream1]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Status [BuffetDream1] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Status [BuffetDream1] — tekst klimatyczny] 신발… 기뻤어…
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream1].flavor
   limit: do 120 znaków
   EN: The shoes... made me really happy...
   PL: Buty... ucieszyły mnie...
30. [Status [BuffetDream2] — nazwa] 뿌이의 기억
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream2].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDream2]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Status [BuffetDream2] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream2].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Status [BuffetDream2] — tekst klimatyczny] 눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream2].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Dziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
33. [Status [BuffetDream3] — nazwa] 뿌이의 기억
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream3].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDream3]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Status [BuffetDream3] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream3].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Status [BuffetDream3] — tekst klimatyczny] 같이 모험했어… 재밌었어…\n\n눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream3].flavor
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We went on an adventure... It was fun...\n\nThanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Bawiliśmy się w przygodę... było fajnie...\n\nDziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
36. [Status [BuffetDream4] — nazwa] 뿌이의 기억
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream4].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDream4]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Status [BuffetDream4] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream4].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Status [BuffetDream4] — tekst klimatyczny] 배고팠어… 아프게 하고 싶지 않았어… 괴로웠어…\n\n같이 모험했어… 재밌었어…\n\n눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream4].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I was hungry... I didn't want to hurt anybody... It hurt so much...\n\nWe went on an adventure... It was fun...\n\nThanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Byłem głodny... nie chciałem nikogo ranić... bolało...\n\nBawiliśmy się w przygodę... było fajnie...\n\nDziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
39. [Status [BuffetDream5] — nazwa] 뿌이의 기억
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream5].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDream5]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Status [BuffetDream5] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream5].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Status [BuffetDream5] — tekst klimatyczny] 멈출 수 없었어… 보고 싶었어… 계속 혼자여서… 같이 가고 싶었어…\n\n배고팠어… 아프게 하고 싶지 않았어… 괴로웠어…\n\n같이 모험했어… 재밌었어…\n\n눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDream5].flavor
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I couldn't stop... I missed you... I was all alone, so... I wanted to come with you...\n\nI was hungry... I didn't want to hurt anybody... It hurt so much...\n\nWe went on an adventure... It was fun...\n\nThanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Nie mogłem przestać... tęskniłem... ciągle byłem sam... chciałem iść z tobą...\n\nByłem głodny... nie chciałem nikogo ranić... bolało...\n\nBawiliśmy się w przygodę... było fajnie...\n\nDziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
42. [Status [BuffetDreamEnd] — nazwa] 나는… ‘뿌이’
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDreamEnd].name
   kontekst: identyfikator statusu w tekstach: `[BuffetDreamEnd]`
   limit: do 40 znaków
   EN: I... am "Pwie".
   PL: Jestem... „Pwie”
43. [Status [BuffetDreamEnd] — opis] - 기본 공격 레벨 -30\n- 기본 방어 레벨 -30\n- 받는 피해량 +100%
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDreamEnd].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -30\n- Base Defense Level -30\n- Take +100% damage
   PL: - Podstawowy Poziom Ataku -30\n- Podstawowy Poziom Obrony -30\n- Otrzymuje obrażenia +100%
44. [Status [BuffetDreamEnd] — tekst klimatyczny] 날 뿌이라 기억해줘.\n고마워.
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetDreamEnd].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Remember me as "Pwie," okay?\nThank you... for everything.
   PL: Zapamiętaj mnie jako „Pwie”.\nDziękuję... za wszystko.
45. [Status [BuffetRevival] — nazwa] 붉은 신의 목소리
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetRevival].name
   kontekst: identyfikator statusu w tekstach: `[BuffetRevival]`
   limit: do 40 znaków
   EN: Voice of the Crimson God
   PL: Głos Czerwonego Boga
46. [Status [BuffetRevival] — opis] - 최댓값 : 3\n- 사망하지 않음\n- 턴 종료 시 1 감소\n- 이 효과 소멸 시 본래의 모습(르루주 고위 스태프)으로 돌아가며, 붉은 신의 뜯긴 살점 상태에서 남아있던 체력 10당, 정신력 5 회복. 맥동 횟수 2 얻음\n· 얻은 맥동 횟수가 10 이상이면, 맥동 횟수를 모두 소모하고 소모한 수치 5당, 다음 턴에 폭주[르 데지르] 1 얻음
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetRevival].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Cannot be defeated\n- Turn End: Lose 1 Stack\n- When this effect expires,\n · Return to "Le Rouge Senior Staff" form\n · Heal 5 SP for every 10 HP that remained while this unit was in "Ripped Flesh of the Crimson God" form; gain +2 Pulsation Count\n · If this unit gained 10+ Pulsation Count, consume all Pulsation Count; then, gain 1 Uncontrollable Rampage [Le Désir] next turn for every 5 Stacks consumed
   PL: - Maks. ładunków: 3\n- Nie ginie\n- Na koniec tury traci 1 ładunek\n- Gdy ten efekt znika, wraca do pierwotnej postaci (starszy personel Le Rouge); za każde 10 HP, jakie pozostało mu w stanie Rozdartego Mięsa Czerwonego Boga, odzyskuje 5 Poczytalności; zyskuje 2 Licznika Pulsowania\n· Jeżeli zdobyte Liczniki Pulsowania wynoszą 10 lub więcej, zużywa je wszystkie i za każde 5 zużytych zyskuje w następnej turze 1 Niepowstrzymanej Furii [Le Désir]
47. [Status [BuffetRevival] — tekst klimatyczny] 살고 또 살아라.\n\n경험한다는 것은, 산다는 것은.\n\n의식이 현재가 아닌 미래에 가 있는 것.\n기대하기 때문에 경험하고 싶은 것. 경험하고 싶기 때문에 살려는 것.
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetRevival].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Live, and live again.\n\nTo experience, to live, is for the mind to dwell not in the present, but already in the future.\n\nBecause one looks forward to what is yet to come, one longs to experience. And because one longs to experience, one chooses to go on living.
   PL: Żyj i żyj dalej.\n\nDoświadczanie, życie — polega na tym, że świadomość przebywa nie w teraźniejszości, lecz już w przyszłości.\nBo czemu człowiek oczekuje — dlatego chce doświadczać; a bo chce doświadczać — dlatego chce żyć.
48. [Status [BuffetRouge] — nazwa] 폭주[르 데지르]
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetRouge].name
   kontekst: identyfikator statusu w tekstach: `[BuffetRouge]`
   limit: do 50 znaków
   EN: Uncontrollable Rampage [Le Désir]
   PL: Niepowstrzymana Furia [Le Désir]
49. [Status [BuffetRouge] — opis] - 최댓값 : 3\n- 속도 최솟값 +1, 최댓값 +1\n- 출혈로 받는 피해량 -50%\n- 출혈 피해로 사망하지 않음\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetRouge].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Min & Max Speed +1\n- Take -50% damage from Bleed\n- Cannot be defeated by Bleed damage\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 3\n- Min. Szybkość +1, Maks. Szybkość +1\n- Otrzymuje -50% obrażeń od Krwawienia\n- Nie ginie od obrażeń Krwawienia\n- Na koniec tury traci 1 ładunek
50. [Status [BuffetRouge] — tekst klimatyczny] 절대 만족할 수 없다. 내 욕망이 아님에도, 내 것이라 착각하고 있기 때문에.\n\n이건 당신으로 인한, 당신으로부터 터져 나오는 욕망.
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetRouge].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I can never be satisfied.\n\nEven though the desire is not truly mine, I mistake it for something that belongs to me.\n\nThis is a desire born of you—a desire that bursts forth from you, because of you.
   PL: Nigdy nie nasycę się dosyć.\n\nChoć ta żądza nie jest naprawdę moją, biorę ją za własną.\n\nTo żądza zrodzona z ciebie — żądza wybuchająca z ciebie, przez ciebie.
51. [Status [BuffetScruple] — nazwa] 뿌이와의 경험
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetScruple].name
   kontekst: identyfikator statusu w tekstach: `[BuffetScruple]`
   limit: do 40 znaków
   EN: Shared with Pwie
   PL: Doświadczenie z Pwie
52. [Status [BuffetScruple] — opis] - 속도 최솟값 +3, 최댓값 +3\n- 턴 시작 시 정신력 15 회복\n- 붉은 신[완숙]에게 받는 최종 피해량 -75%
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetScruple].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Turn Start: Heal 15 SP\n- Take -75% final damage from The Crimson God [Adulthood]
   PL: - Min. i Maks. Szybkość +3\n- Na początku tury +15 Poczytalności\n- Otrzymuje -75% obrażeń końcowych od Czerwonego Boga [Dojrzałość]
53. [Status [BuffetScruple] — tekst klimatyczny] 분명 우리는 뿌이와 함께했다.\n\n망설임이, 그런 느낌이 떠오른다.
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetScruple].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We shared an experience with Pwie. Together. That much is certain.\n\nHesitation begins to surface.
   PL: Na pewno dzieliliśmy doświadczenie z Pwie. Wspólnie. Na pewno.\n\nNarasta wahanie.
54. [Status [BuffetResolve] — nazwa] 결단
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetResolve].name
   kontekst: identyfikator statusu w tekstach: `[BuffetResolve]`
   limit: do 40 znaków
   EN: Decision
   PL: Decyzja
55. [Status [BuffetResolve] — opis] - 최댓값 : 1\n- 붉은 신[완숙]에게 가하는 피해량 +30%\n- 턴 시작 시 정신력 15 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetResolve].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Deal +30% damage to The Crimson God [Adulthood]\n- Turn Start: Heal 15 SP
   PL: - Maks. ładunków: 1\n- Zadaje Czerwonemu Bogowi [Dojrzałość] obrażenia +30%\n- Na początku tury odzyskuje 15 Poczytalności
56. [Status [BuffetResolve] — tekst klimatyczny] ‘관리자로서 선택해야만 하겠지.’\n‘그렇습니다.’\n‘…….’\n‘…….’\n‘…결정했어.’
   źródło: Bufs-a1c10p3.json :: dataList[id=BuffetResolve].flavor
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "As Manager... I have to choose, don't I?"\n\n"Correct, Manager."\n\n"......."\n\n"......."\n\n"... I've made my decision."
   PL: „Jako Kierownik... muszę wybrać, prawda?”\n„Zupełnie tak, Kierowniku.”\n„.......”\n„.......”\n„... podjąłem decyzję.”
57. [Status [MeursaultBuffetEnd] — nazwa] 못 박는 자
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffetEnd].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBuffetEnd]`
   limit: do 40 znaków
   EN: He Who Nails
   PL: Ten, Który Przybija
58. [Status [MeursaultBuffetEnd] — opis] - 속도 최솟값 +3, 최댓값 +3\n- 최종 위력 +3\n- 이번 전투에서 자신의 스킬 사용 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 2회)\n- 퇴각 불가능
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffetEnd].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Final Power +3\n- On Skill Use, gain 2 additional E.G.O Resource for the said Skill's Affinity (2 times per turn)\n- Cannot Retreat
   PL: - Min. Szybkość +3, Maks. Szybkość +3\n- Moc Końcowa +3\n- W tej walce przy użyciu Umiejętności dodatkowo zyskuje 2 Zasoby E.G.O Grzechu tej Umiejętności (2 razy na turę)\n- Nie może się wycofać
59. [Status [GrandBuffet_LowMorale] — nazwa] 르 데지르(le désir)
   źródło: Bufs-a1c10p3.json :: dataList[id=GrandBuffet_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[GrandBuffet_LowMorale]`
   limit: do 40 znaków
   EN: Le Désir
   PL: Le Désir
60. [Status [GrandBuffet_LowMorale] — opis] - 사기 저하\n- 공격 레벨 3 증가\n- 방어 레벨 3 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=GrandBuffet_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level +3\n- Defense Level +3
   PL: - Niskie Morale\n- Poziom Ataku +3\n- Poziom Obrony +3
61. [Status [GrandBuffet_Panic] — nazwa] 르 데지르(le désir)
   źródło: Bufs-a1c10p3.json :: dataList[id=GrandBuffet_Panic].name
   kontekst: identyfikator statusu w tekstach: `[GrandBuffet_Panic]`
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Status [GrandBuffet_Panic] — opis] - 패닉\n- 공격 레벨 5 증가\n- 방어 레벨 5 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=GrandBuffet_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level +5\n- Defense Level +5
   PL: - Panika\n- Poziom Ataku +5\n- Poziom Obrony +5
63. [Status [LaRougeSuperior_LowMorale] — nazwa] 좀 더 가죽 밖으로!
   źródło: Bufs-a1c10p3.json :: dataList[id=LaRougeSuperior_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LaRougeSuperior_LowMorale]`
   limit: do 40 znaków
   EN: Farther Past the Hide!
   PL: Skóra Jeszcze Dalej na Zewnątrz!
64. [Status [LaRougeSuperior_LowMorale] — opis] - 사기 저하\n- 방어 레벨 2 감소\n- 공격 레벨 2 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=LaRougeSuperior_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Defense Level -2\n- Offense Level +2
   PL: - Niskie Morale\n- Poziom Obrony -2\n- Poziom Ataku +2
65. [Status [LaRougeSuperior_Panic] — nazwa] 좀 더 가죽 밖으로!
   źródło: Bufs-a1c10p3.json :: dataList[id=LaRougeSuperior_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LaRougeSuperior_Panic]`
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Status [LaRougeSuperior_Panic] — opis] - 패닉\n- 방어 레벨 5 감소\n- 공격 레벨 3 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=LaRougeSuperior_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Defense Level -5\n- Offense Level +3
   PL: - Panika\n- Poziom Obrony -5\n- Poziom Ataku +3
67. [Status [Jeanne_LowMorale] — nazwa] 라 노제(la nausée)
   źródło: Bufs-a1c10p3.json :: dataList[id=Jeanne_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Jeanne_LowMorale]`
   limit: do 40 znaków
   EN: La Nausée
   PL: La Nausée
68. [Status [Jeanne_LowMorale] — opis] - 사기 저하\n- 가하는 피해량 -10%
   źródło: Bufs-a1c10p3.json :: dataList[id=Jeanne_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal -10% damage
   PL: - Niskie Morale\n- Zadaje obrażenia -10%
69. [Status [Jeanne_Panic] — nazwa] 라 노제(la nausée)
   źródło: Bufs-a1c10p3.json :: dataList[id=Jeanne_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Jeanne_Panic]`
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Status [Jeanne_Panic] — opis] - 패닉\n- 기본 위력 -1\n가하는 피해량 -10%
   źródło: Bufs-a1c10p3.json :: dataList[id=Jeanne_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Base Power -1\n- Deal -10% damage
   PL: - Panika\n- Moc Bazowa -1\nZadaje obrażenia -10%

## Statusy i efekty bojowe — Bufs-a1c5p1
- plik gry: `Bufs-a1c5p1.json`

71. [Status [AaCePaBa] — nazwa] 강박
   źródło: Bufs-a1c5p1.json :: dataList[id=AaCePaBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCePaBa]`
   limit: do 40 znaków
   EN: Compulsion
   PL: Kompulsja
72. [Status [AaCePaBa] — opis] 정신력 -25상태로 전투 시작. 턴 시작 시 정신력이 0 미만일 때 공격 위력 증가 3을 얻음.
   źródło: Bufs-a1c5p1.json :: dataList[id=AaCePaBa].desc
   limit: do 120 znaków
   EN: Starts encounter with -25 SP. At less than 0 SP at Turn Start, gain 3 Attack Power Up.
   PL: Rozpoczyna walkę z Poczytalnością -25. Na początku tury przy Poczytalności poniżej 0 zyskuje 3 Wzrostu Mocy Ataku.
73. [Status [AaCePaBa] — podsumowanie] 정신력이 0 미만일 때 공격 위력 증가 3을 얻음
   źródło: Bufs-a1c5p1.json :: dataList[id=AaCePaBa].summary
   limit: do 120 znaków
   EN: At less than 0 SP, gain 3 Attack Power Up
   PL: Na początku tury przy Poczytalności poniżej 0 zyskuje 3 Wzrostu Mocy Ataku

## Statusy i efekty bojowe — Bufs-a1c5p2
- plik gry: `Bufs-a1c5p2.json`

74. [Status [AaCePbBa] — nazwa] 창백한 소음
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBa]`
   limit: do 40 znaków
   EN: Pallid Noise
   PL: Blady Szum
75. [Status [AaCePbBa] — opis] 정신력 감소 효율 +2.\n이 버프를 가지고 있을 때, 정신력이 -45이하라면 다음 턴에 소음 공황을 얻는다.\n턴 종료시 1 감소
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBa].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: SP Loss Efficiency +2\nIf at less than or equal to -45 SP and inflicted with this buff, gain Noise Panic next turn.\nTurn End: Reduce this effect by 1
   PL: Wydajność utraty Poczytalności +2.\nPosiadając ten efekt, przy Poczytalności -45 lub niższej zyskuje w następnej turze Panikę Szumu.\nNa koniec tury traci 1 ładunek
76. [Status [AaCePbBa] — podsumowanie] 정신력 감소 효율 +2
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBa].summary
   limit: do 120 znaków
   EN: SP Loss Efficiency +2
   PL: Wydajność utraty Poczytalności +2
77. [Status [AaCePbBb] — nazwa] 소음 공황
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBb].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBb]`
   limit: do 40 znaków
   EN: Noise Panic
   PL: Panika Szumu
78. [Status [AaCePbBb] — opis] 자신이 사용하는 모든 코인이 뒷면이 나옴.\n다음 턴에 사라짐
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBb].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every Coin this unit flips lands on tails.\nExpires next turn
   PL: Wszystkie Monety tej jednostki zawsze wypadają jako Rewers.\nZnika w następnej turze
79. [Status [AaCePbBb] — podsumowanie] 모든 코인이 뒷면이 나옴
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBb].summary
   limit: do 120 znaków
   EN: Every Coin lands on tails
   PL: Wszystkie Monety wypadają jako Rewers
80. [Status [AaCePbBc] — nazwa] 불순
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBc].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBc]`
   limit: do 40 znaków
   EN: Impurity
   PL: Nieczystość
81. [Status [AaCePbBc] — opis] - 사기 저하\n- 취약 1을 얻음. 합 패배시 대상의 정신력 -2
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBc].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile. If this unit loses a clash, the target loses 2 SP
   PL: - Niskie Morale\n- Zyskuje 1 Wrażliwości. Po przegranej w Starciu cel traci 2 Poczytalności
82. [Status [AaCePbBc] — podsumowanie] 합 패배시 대상의 정신력 -2
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBc].summary
   limit: do 120 znaków
   EN: Target loses 2 SP if this unit loses the clash
   PL: Po przegranej w Starciu cel traci 2 Poczytalności
83. [Status [AaCePbBd] — nazwa] 불순
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBd].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBd]`
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Status [AaCePbBd] — opis] - 패닉\n- 취약 2를 얻음. 합 패배시 대상의 정신력 -5
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBd].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Fragile. If this unit loses a clash, the target loses 5 SP
   PL: - Panika\n- Zyskuje 2 Wrażliwości. Po przegranej w Starciu cel traci 5 Poczytalności
85. [Status [AaCePbBd] — podsumowanie] 합 패배시 대상의 정신력 -5
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBd].summary
   limit: do 120 znaków
   EN: Target loses 5 SP if this unit loses the clash
   PL: Po przegranej w Starciu cel traci 5 Poczytalności
86. [Status [AaCePbBi] — nazwa] 형님의 시험
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBi].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBi]`
   limit: do 40 znaków
   EN: Test of the Big Brother
   PL: Test Starszego Brata
87. [Status [AaCePbBi] — opis] 턴 종료 시 1 감소\n이 효과가 있는 동안 스킬 피해, 진동 폭발로 인한 흐트러짐 손상을 3배로 받음.\n이 효과가 사라질 때 흐트러짐 상태가 아닌 경우, 다음 턴 시작 시 피해량 증가 5를 얻음
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBi].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Lose 1 Stack\n- While this effect is active, triple the damage taken from Skills and the amount of Stagger Threshold raised from Tremor Burst\n- If this unit is not Staggered when this effect expires, gain 5 Damage Up at the next Turn Start
   PL: Na koniec tury traci 1 ładunek\nDopóki aktywny jest ten efekt, obrażenia od Umiejętności oraz obniżenie Progu Oszołomienia z Wyładowania Wstrząsu są potrajane.\nJeżeli przy znikaniu tego efektu jednostka nie jest oszołomiona, na początku następnej tury zyskuje 5 Wzrostu Obrażeń
88. [Status [AaCePbBe] — nazwa] 앙갚음
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBe].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBe]`
   limit: do 40 znaków
   EN: Vengeance
   PL: Zemsta
89. [Status [AaCePbBe] — opis] - 사기 저하\n- 턴 시작 시 공격 위력 증가 1, 방어 레벨 감소 3을 얻고, 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음. (최대 체력의 3%당 피해량 증가 1을 얻음)
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBe].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Attack Power Up and 3 Defense Level Down. Gain Damage Up based on the amount of damage taken last turn (1 Damage Up for every 3% of Max HP lost)
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrostu Mocy Ataku i 3 Spadku Poziomu Obrony, a Wzrost Obrażeń zależnie od obrażeń otrzymanych w poprzedniej turze (1 Wzrost Obrażeń za każde 3% Maks. HP utraconego)
90. [Status [AaCePbBe] — podsumowanie] 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음.
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBe].summary
   limit: do 120 znaków
   EN: Gain Damage Up based on total damage taken last turn.
   PL: Zyskuje Wzrost Obrażeń zależnie od łącznych obrażeń otrzymanych w poprzedniej turze.
91. [Status [AaCePbBf] — nazwa] 앙갚음
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBf].name
   kontekst: identyfikator statusu w tekstach: `[AaCePbBf]`
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Status [AaCePbBf] — opis] - 패닉\n- 턴 시작 시 공격 위력 증가 2, 방어 레벨 감소 6을 얻고, 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음. (최대 체력의 3%당 피해량 증가 1을 얻음)
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBf].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Attack Power Up and 6 Defense Level Down. Gain Damage Up based on the amount of damage taken last turn\n(1 Damage Up for every 3% of Max HP lost)
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 6 Spadku Poziomu Obrony, a Wzrost Obrażeń zależnie od obrażeń otrzymanych w poprzedniej turze\n(1 Wzrost Obrażeń za każde 3% Maks. HP utraconego)
93. [Status [AaCePbBf] — podsumowanie] 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음.
   źródło: Bufs-a1c5p2.json :: dataList[id=AaCePbBf].summary
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs-a1c5p3
- plik gry: `Bufs-a1c5p3.json`

94. [Status [AaCePcBa] — nazwa] 표식
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBa]`
   limit: do 40 znaków
   EN: Marked
   PL: Oznaczony
95. [Status [AaCePcBa] — opis] 우선 공격 지정 대상이 됨.\n피격시 얻는 모든 화상 위력, 화상 횟수의 2배를 추가로 얻음
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBa].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Will be primarily targeted.\nWhen hit, gain additional Burn Potency and Burn Count equal to 2 times the amount gained.
   PL: Staje się głównym celem ataków.\nPrzy trafieniu zyskuje dodatkowo podwójną ilość Siły Podpalenia i Licznika Podpalenia
96. [Status [AaCePcBb] — nazwa] 형광등 파편
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBb].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBb]`
   limit: do 40 znaków
   EN: Fluorescence Shard
   PL: Odłamek Świetlówki
97. [Status [AaCePcBb] — opis] 턴 시작 시 호흡 3 얻음, 호흡 횟수 2 증가
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBb].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 3 Poise and +2 Poise Count
   PL: Na początku tury zyskuje 3 Oddechu i Licznik Oddechu +2
98. [Status [AaCePcBc] — nazwa] 맹목
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBc].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBc]`
   limit: do 40 znaków
   EN: Blind Obsession
   PL: Zaślepiona Obsesja
99. [Status [AaCePcBc] — opis] 수치가 3이 되면 흐트러짐 상태가 됨.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBc].desc
   limit: do 120 znaków
   EN: At 3+ value, this unit becomes staggered.
   PL: Przy wartości 3 lub większej jednostka zostaje oszołomiona.
100. [Status [AaCePcBg] — nazwa] 유충
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBg].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBg]`
   limit: do 40 znaków
   EN: Larva
   PL: Larwa
101. [Status [AaCePcBg] — opis] 턴 종료 시 현재 체력이 가장 높은 아군에게 유충이 옮겨감.\n턴 시작 시 수치만큼 정신력 피해를 얻음.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBg].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Move Larva to the ally with the highest HP.\nTurn Start: Lose SP equal to the value of Larva on self.
   PL: Na koniec tury Larwa przenosi się na sojusznika z najwyższym HP.\nNa początku tury traci Poczytalność równą wartości Larwy.
102. [Status [AaCePcBh] — nazwa] 녹색 점액
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBh].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBh]`
   limit: do 40 znaków
   EN: Green Slime
   PL: Zielony Śluz
103. [Status [AaCePcBh] — opis] 감소할 때마다, 다음 턴에 녹색 점액을 생성함.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBh].desc
   limit: do 120 znaków
   EN: Generates Green Slime next turn every time this value shrinks
   PL: Za każdym razem, gdy wartość maleje, w następnej turze tworzy Zielony Śluz.
104. [Status [AaCePcBi] — nazwa] 거친 호흡
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBi].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBi]`
   limit: do 40 znaków
   EN: Uneven Breathing
   PL: Nierówny Oddech
105. [Status [AaCePcBi] — opis] 턴 종료 시 호흡을 5 잃음.\n가하는 피해량 +50%, 받는 피해량 +50%
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBi].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 5 Poise.\nDeal +50% damage and receive +50% damage
   PL: Na koniec tury traci 5 Oddechu.\nZadaje obrażenia +50% i otrzymuje +50%.
106. [Status [AaCePcBi] — podsumowanie] 가하는 피해량 +50%, 받는 피해량 +50%
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBi].summary
   limit: do 120 znaków
   EN: Deal +50% damage and receive +50% damage
   PL: Zadaje +50% obrażeń i otrzymuje +50% obrażeń
107. [Status [AaCePcBj] — nazwa] 사냥감의 징표
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBj].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBj]`
   limit: do 40 znaków
   EN: Prey Mark
   PL: Piętno Zdobyczy
108. [Status [AaCePcBj] — opis] 모든 피쿼드 선원의 타겟이 됨\n피쿼드 선원에게 받는 피해 50% 증가
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBj].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All Pequod crew targets this unit\nTake +50% damage from Pequod crew
   PL: Wszyscy członkowie załogi Pequoda celują w tę jednostkę\nOtrzymuje +50% obrażeń od członków załogi Pequoda
109. [Status [AaCePcBj] — podsumowanie] 피쿼드 선원에게 받는 피해 50% 증가
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBj].summary
   limit: do 120 znaków
   EN: Take +50% damage from Pequod crew
   PL: Otrzymuje +50% obrażeń od członków załogi Pequoda
110. [Status [AaCePcBk] — nazwa] 결박
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBk].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBk]`
   limit: do 40 znaków
   EN: Tangle
   PL: Splecenie
111. [Status [AaCePcBk] — opis] 포획 과 같은 대상에게 부여되면, 대상이 흐트러짐 상태가 됨
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBk].desc
   limit: do 120 znaków
   EN: If inflicted against a target with Capture, Stagger target
   PL: Jeśli nadany na cel posiadający Pojmanie, cel popada w stan Oszołomienia
112. [Status [AaCePcBk] — podsumowanie] 조건 만족 시 대상이 흐트러짐 상태가 됨
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBk].summary
   limit: do 120 znaków
   EN: Stagger target under certain conditions
   PL: Przy spełnieniu warunków cel popada w stan Oszołomienia
113. [Status [AaCePcBl] — nazwa] 포획
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBl].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBl]`
   limit: do 40 znaków
   EN: Capture
   PL: Pojmanie
114. [Status [AaCePcBl] — opis] 결박 과 같은 대상에게 부여되면, 대상이 흐트러짐 상태가 됨
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBl].desc
   limit: do 120 znaków
   EN: If inflicted against a target with Tangle, Stagger target
   PL: Jeśli nadany na cel posiadający Splecenie, cel popada w stan Oszołomienia
115. [Status [AaCePcBl] — podsumowanie] 조건 만족 시 대상이 흐트러짐 상태가 됨
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBl].summary
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Status [AaCePcBn] — nazwa] 거역할 수 없는 명령
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBn].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBn]`
   limit: do 40 znaków
   EN: Undefiable Command
   PL: Rozkaz Bez Dyskusji
117. [Status [AaCePcBn] — opis] 스킬 사용 시 체력이 현재 체력의 10%만큼 감소. 스킬 최종 위력 +1,\n적중 시 에이해브의 정신력 8 회복, 자신과 에이해브에게 호흡 2 부여
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBn].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose 10% of current HP when using a Skill. Skill Final Power +1\nOn Hit, Ahab heals 8 SP; apply 2 Poise to self and Ahab
   PL: Przy użyciu Umiejętności traci 10% obecnego HP; Moc Końcowa +1,\nPrzy trafieniu Ahab odzyskuje 8 Poczytalności, a jednostka i Ahab otrzymują 2 Oddechu
118. [Status [AaCePcBn] — podsumowanie] 스킬 사용 시 체력 감소, 최종 위력 +1.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBn].summary
   limit: do 120 znaków
   EN: Lose HP when using a Skill; Final Power +1
   PL: Przy użyciu Umiejętności traci HP; Moc Końcowa +1.
119. [Status [AaCePcBo] — nazwa] 핍의 자아
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBo].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBo]`
   limit: do 40 znaków
   EN: Pip's Ego
   PL: Ego Pipa
120. [Status [AaCePcBo] — opis] 턴 시작 시 수치 1당 정신력 3 회복.\n회피 실패 시, 죄책감의 무게 스킬 사용 시 감소.\n턴 종료 시 수치가 0이면 흐트러짐 상태가 됨.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBo].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Heal 3 SP per value.\nDecreases when using Weight of Guilt after failing Evade.\nTurn End: If at 0, get Staggered.
   PL: Na początku tury odzyskuje 3 Poczytalności za wartość.\nMaleje przy nieudanym Uniku i użyciu „Ciężaru Poczucia Winy”.\nNa koniec tury przy 0 — Oszołomienie.
121. [Status [AaCePcBo] — podsumowanie] 수치에 비례하여 정신력 회복. 회피 실패 시, 특정 스킬 사용 시 감소.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBo].summary
   limit: do 120 znaków
   EN: Heal SP by value. Reduce value when failing Evade or after using certain Skills.
   PL: Odzyskuje Poczytalność zależnie od wartości. Maleje przy nieudanym Uniku oraz przy użyciu pewnej Umiejętności.
122. [Status [AaCePcBp] — nazwa] 스타벅의 자아
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBp].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBp]`
   limit: do 40 znaków
   EN: Starbuck's Ego
   PL: Ego Starbucka
123. [Status [AaCePcBp] — opis] 턴 시작 시 수치 5당 보호 1 얻음.\n사냥감의 징표 가 있는 대상과의 합 패배 시 합에서 파괴된 코인 수만큼 감소.\n턴 종료 시 수치가 0이면 흐트러짐 상태가 됨.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBp].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Gain 1 Protection for every 5 value.\nDecreases for every Coin destroyed in Clash against targets with Prey Mark.\nTurn End: If at 0, get Staggered.
   PL: Na początku tury zyskuje 1 Ochrony za każde 5 wartości.\nMaleje o liczbę Monet zniszczonych w Starciu z celem posiadającym „Piętno Zdobyczy”.\nNa koniec tury przy wartości 0 jednostka zostaje oszołomiona.
124. [Status [AaCePcBp] — podsumowanie] 수치에 비례하여 보호 얻음. 특정 대상과의 합 패배 시 감소.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBp].summary
   limit: do 120 znaków
   EN: Gain Protection by value. Reduce value when losing Clash against certain targets.
   PL: Zyskuje Ochronę zależnie od wartości. Maleje po przegranej w Starciu z pewnymi celami.
125. [Status [AaCePcBq] — nazwa] 퀴케그의 자아
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBq].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBq]`
   limit: do 40 znaków
   EN: Queequeg's Ego
   PL: Ego Queequeg
126. [Status [AaCePcBq] — opis] 턴 종료 시 보호막이 남아있으면 수치 증가\n턴 종료 시 보호막이 없거나 탈색된 참회 스킬 사용시 감소.\n턴 종료 시 수치가 0이면 흐트러짐 상태가 됨.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBq].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Gain value if Shielded\nTurn End: Lose value when without Shield or when using Bleached Atonement.\nTurn End: At 0, get Staggered.
   PL: Na koniec tury, gdy jest Tarcza, wartość rośnie\nNa koniec tury maleje bez Tarczy lub przy użyciu „Wybielonej Pokuty”.\nNa koniec tury przy 0 — Oszołomienie.
127. [Status [AaCePcBq] — podsumowanie] 턴 종료 시 보호막 유무에 따라 수치 증가 또는 감소.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBq].summary
   limit: do 120 znaków
   EN: Turn End: Depending on whether this unit is Shielded or not, lose or gain value.
   PL: Na koniec tury wartość rośnie lub maleje zależnie od obecności Tarczy.
128. [Status [AaCePcBe] — nazwa] 하얀 공황
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBe].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBe]`
   limit: do 40 znaków
   EN: Pallid Panic
   PL: Blada Panika
129. [Status [AaCePcBe] — opis] 정신력 감소 효율 +2
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBe].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Status [AaCePcBf] — nazwa] 하얀 공황
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBf].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBf]`
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Status [AaCePcBf] — opis] 턴 종료 시 속박 2를 얻음.\n자신이 사용하는 모든 코인이 뒷면이 나옴.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBf].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 2 Bind at Turn End.\nEvery Coin this unit flips lands on tails.
   PL: Na koniec tury zyskuje 2 Spętania.\nWszystkie Monety tej jednostki zawsze wypadają jako Rewers.
132. [Status [AaCePcBr] — nazwa] 원호 방어 보호막
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBr].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBr]`
   limit: do 40 znaków
   EN: Assist Barrier
   PL: Tarcza Obrony Wsparcia
133. [Status [AaCePcBr] — opis] 피격 시 피해만큼 수치 감소.\n턴 종료 시 사라지지 않음.\n에이헤브가 1페이즈일 때, 턴 종료 시 수치가 0이 되면 다음 턴에 흐트러짐 상태가 됨.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBr].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduce value by the amount of damage taken.\nDoes not expire at the end of the turn.\nTurn End: If this value becomes 0 during Ahab's 1st phase, get Staggered next turn.
   PL: Wartość maleje o wielkość otrzymanych obrażeń.\nNie znika na koniec tury.\nGdy Ahab znajduje się w 1. fazie, jeśli wartość osiągnie 0 na koniec tury, w następnej turze popada w stan Oszołomienia.
134. [Status [AaCePcBs] — nazwa] 원호 방어
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBs].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBs]`
   limit: do 40 znaków
   EN: Assist Defense
   PL: Obrona Wsparcia
135. [Status [AaCePcBs] — opis] 에이해브를 공격하는 스킬의 타겟팅이 자신의 슬롯으로 이동됨.\n이 효과를 가진 캐릭터의 슬롯 가중치가 무제한으로 증가함.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBs].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pull skills targeting Ahab to this unit's slot.\nThe unit with this effect has unlimited Slot Weight.
   PL: Umiejętności atakujące Ahaba przenoszą celowanie na slot tej jednostki.\nWaga Slotu jednostki z tym efektem rośnie bez limitu.
136. [Status [AaCePcBt] — nazwa] 원호 공격
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBt].name
   kontekst: identyfikator statusu w tekstach: `[AaCePcBt]`
   limit: do 40 znaków
   EN: Assist Attack
   PL: Atak Wsparcia
137. [Status [AaCePcBt] — opis] 에이해브의 공격 스킬 종료 시 에이해브가 공격한 대상을 1회 일방 공격함.\n이 때 사용하는 스킬은 '명령을 받들어...' 스킬과 동일한 코인 값, 코인 효과, 공격 레벨을 가짐.
   źródło: Bufs-a1c5p3.json :: dataList[id=AaCePcBt].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After Ahab's attack, commence unopposed attack against the same target Ahab attacked.\nThe Skill used in this action has the same Offense Level, Coin values and effects as this unit's 'I Follow Orders...' Skill.
   PL: Po zakończeniu Umiejętności ataku Ahaba jednostka wykonuje 1 Atak Jednostronny na cel, którego Ahab zaatakował.\nUmiejętność użyta w ten sposób ma takie same wartości i efekty Monet oraz Poziom Ataku jak Umiejętność „Z rozkazu...” tej jednostki.

## Statusy i efekty bojowe — Bufs-a1c6p1
- plik gry: `Bufs-a1c6p1.json`

138. [Status [CleanUp_LowMorale] — nazwa] 정리 강박
   źródło: Bufs-a1c6p1.json :: dataList[id=CleanUp_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[CleanUp_LowMorale]`
   limit: do 40 znaków
   EN: Organization Compulsion
   PL: Przymus Organizowania
139. [Status [CleanUp_LowMorale] — opis] - 사기 저하\n- 합 패배 시 정신력 5 감소. 피격 시 다음 턴에 신속 1 얻음 (최대 2)
   źródło: Bufs-a1c6p1.json :: dataList[id=CleanUp_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Lose 5 SP on Clash Lose. Gain 1 Haste next turn when hit (max 2)
   PL: - Niskie Morale\n- Przegrana w Starciu: traci 5 Poczytalności. Przy trafieniu: 1 Pośpiechu w następnej turze (maks. 2)
140. [Status [CleanUp_LowMorale] — podsumowanie] 합 패배 시 정신력 5 감소. 피격 시 다음 턴에 신속 1 얻음
   źródło: Bufs-a1c6p1.json :: dataList[id=CleanUp_LowMorale].summary
   limit: do 120 znaków
   EN: Lose 5 SP on Clash Lose. Gain 1 Haste next turn when hit
   PL: Po przegranej w Starciu traci 5 Poczytalności. Przy trafieniu zyskuje w następnej turze 1 Pośpiechu
141. [Status [CleanUp_Panic] — nazwa] 정리 강박
   źródło: Bufs-a1c6p1.json :: dataList[id=CleanUp_Panic].name
   kontekst: identyfikator statusu w tekstach: `[CleanUp_Panic]`
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Status [CleanUp_Panic] — opis] - 패닉\n- 취약 2 얻음. 피격 시 다음 턴에 신속 1 얻음 (최대 3)
   źródło: Bufs-a1c6p1.json :: dataList[id=CleanUp_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Fragile. Gain 1 Haste next turn when hit (max 3)
   PL: - Panika\n- Zyskuje 2 Wrażliwości. Przy trafieniu zyskuje w następnej turze 1 Pośpiechu (maks. 3)
143. [Status [CleanUp_Panic] — podsumowanie] 취약 2 얻음. 피격 시 다음 턴에 신속 1 얻음
   źródło: Bufs-a1c6p1.json :: dataList[id=CleanUp_Panic].summary
   limit: do 120 znaków
   EN: Gain 3 Fragile. Gain 1 Haste next turn when hit
   PL: Zyskuje 2 Wrażliwości. Przy trafieniu zyskuje w następnej turze 1 Pośpiechu
144. [Status [Acclamation_LowMorale] — nazwa] 저택의 메아리
   źródło: Bufs-a1c6p1.json :: dataList[id=Acclamation_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Acclamation_LowMorale]`
   limit: do 40 znaków
   EN: Echoes of the Manor
   PL: Echa Rezydencji
145. [Status [Acclamation_LowMorale] — opis] - 사기 저하\n- 자신의 합 위력 -1. 앞면 적중 시 피해량 +10%
   źródło: Bufs-a1c6p1.json :: dataList[id=Acclamation_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1 on self. Deal +10% damage on Heads Hit
   PL: - Niskie Morale\n- Moc Starcia -1. Przy trafieniu Awersami zadaje +10% obrażeń
146. [Status [Acclamation_LowMorale] — podsumowanie] 자신의 합 위력 -1. 앞면 적중 시 피해량 +10%
   źródło: Bufs-a1c6p1.json :: dataList[id=Acclamation_LowMorale].summary
   limit: do 120 znaków
   EN: Clash Power -1 on self. Deal +10% damage on Heads Hit
   PL: Moc Starcia -1. Przy trafieniu Awersami zadaje +10% obrażeń
147. [Status [Acclamation_Panic] — nazwa] 저택의 메아리
   źródło: Bufs-a1c6p1.json :: dataList[id=Acclamation_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Acclamation_Panic]`
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Status [Acclamation_Panic] — opis] - 패닉\n- 자신의 합 위력 -2. 피해량 증가 1 얻음
   źródło: Bufs-a1c6p1.json :: dataList[id=Acclamation_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Power -2 on self. Gain 1 Damage Up
   PL: - Panika\n- Moc Starcia -2. Zyskuje 1 Wzrost Obrażeń
149. [Status [Acclamation_Panic] — podsumowanie] 자신의 합 위력 -2. 피해량 증가 1 얻음
   źródło: Bufs-a1c6p1.json :: dataList[id=Acclamation_Panic].summary
   limit: do 120 znaków
   EN: Clash Power -2 on self. Gain 1 Damage Up
   PL: Moc Starcia -2. Zyskuje 1 Wzrost Obrażeń
150. [Status [Unstable_LowMorale] — nazwa] 분열
   źródło: Bufs-a1c6p1.json :: dataList[id=Unstable_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Unstable_LowMorale]`
   limit: do 40 znaków
   EN: Splitting
   PL: Wewnętrzny Rozłam
151. [Status [Unstable_LowMorale] — opis] - 사기 저하\n- 합 진행 시 매 합마다 자신의 체력 2 피해, 턴 시작 시 공격 레벨 증가 1 얻음.
   źródło: Bufs-a1c6p1.json :: dataList[id=Unstable_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Lose 2 HP on self with every Clash. Gain 1 Offense Level Up at Turn Start.
   PL: - Niskie Morale\n- W każdym Starciu traci 2 HP. Na początek tury zyskuje 1 Wzrost Poziomu Ataku.
152. [Status [Unstable_LowMorale] — podsumowanie] 합마다 자신의 체력 2 피해
   źródło: Bufs-a1c6p1.json :: dataList[id=Unstable_LowMorale].summary
   limit: do 120 znaków
   EN: Lose 2 HP on self with every Clash
   PL: Traci 2 HP w każdym Starciu
153. [Status [Unstable_Panic] — nazwa] 분열
   źródło: Bufs-a1c6p1.json :: dataList[id=Unstable_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Unstable_Panic]`
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Status [Unstable_Panic] — opis] - 패닉\n- 합 진행 시 매 합마다 자신의 체력 3 피해, 턴 시작 시 공격 레벨 증가 2 얻음.
   źródło: Bufs-a1c6p1.json :: dataList[id=Unstable_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Lose 3 HP on self with every Clash. Gain 2 Offense Level Up at Turn Start.
   PL: - Panika\n- W każdym Starciu traci 3 HP. Na początek tury zyskuje 2 Wzrosty Poziomu Ataku.
155. [Status [Unstable_Panic] — podsumowanie] 합마다 자신의 체력 3 피해
   źródło: Bufs-a1c6p1.json :: dataList[id=Unstable_Panic].summary
   limit: do 120 znaków
   EN: Lose 3 HP on self with every Clash
   PL: Traci 3 HP w każdym Starciu
156. [Status [AaCfPaBa] — nazwa] 상실
   źródło: Bufs-a1c6p1.json :: dataList[id=AaCfPaBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPaBa]`
   limit: do 40 znaków
   EN: Bereavement
   PL: Żałoba
157. [Status [AaCfPaBa] — opis] 턴 종료 시 정신력이 -15 이상이면, 정신력 10 감소.\n피격 시 정신력 2 감소, 다음 턴에 공격 레벨 증가 1 얻음.(턴 당 3회)\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.
   źródło: Bufs-a1c6p1.json :: dataList[id=AaCfPaBa].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: at -15 or higher SP, lose 10 SP.\nWhen hit, lose 2 SP and gain 1 Offense Level Up next turn. (3 times per turn)\nTurn Start: at less than 0 SP, gain 3 Attack Power Up.
   PL: Na koniec tury przy Poczytalności -15 lub więcej traci 10 Poczytalności.\nPrzy trafieniu: -2 Poczytalności, 1 Wzrost Poziomu Ataku w następnej turze (3 na turę)\nNa początek tury przy Poczytalności poniżej 0: 3 Wzrosty Mocy Ataku.
158. [Status [AaCfPaBa] — podsumowanie] 피격 시 정신력 2 감소, 다음 턴에 공격 레벨 증가 1 얻음.\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.
   źródło: Bufs-a1c6p1.json :: dataList[id=AaCfPaBa].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit, lose SP and gain 1 Offense Level Up next turn.\nTurn Start: at less than 0 SP, gain 3 Attack Power Up.
   PL: Przy trafieniu: -2 Poczytalności, 1 Wzrost Poziomu Ataku w następnej turze.\nNa początek tury przy Poczytalności poniżej 0: 3 Wzrosty Mocy Ataku.

## Statusy i efekty bojowe — Bufs-a1c6p2
- plik gry: `Bufs-a1c6p2.json`

159. [Status [Vengeance_LowMorale] — nazwa] 복수
   źródło: Bufs-a1c6p2.json :: dataList[id=Vengeance_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Vengeance_LowMorale]`
   limit: do 40 znaków
   EN: Revenge
   PL: Zemsta
160. [Status [Vengeance_LowMorale] — opis] - 사기 저하\n- 방어 레벨 감소 3, 피해량 증가 3 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=Vengeance_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 3 Defense Level Down and 3 Damage Up
   PL: - Niskie Morale\n- Zyskuje 3 Spadki Poziomu Obrony i 3 Wzrosty Obrażeń
161. [Status [Vengeance_LowMorale] — podsumowanie] 방어 레벨 감소 3, 피해량 증가 3 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=Vengeance_LowMorale].summary
   limit: do 120 znaków
   EN: Gain 3 Defense Level Down and 3 Damage Up
   PL: Zyskuje 3 Spadki Poziomu Obrony i 3 Wzrosty Obrażeń
162. [Status [Vengeance_Panic] — nazwa] 복수
   źródło: Bufs-a1c6p2.json :: dataList[id=Vengeance_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Vengeance_Panic]`
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Status [Vengeance_Panic] — opis] - 패닉\n- 방어 레벨 감소 6, 피해량 증가 5 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=Vengeance_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 6 Defense Level Down and 5 Damage Up
   PL: - Panika\n- Zyskuje 6 Spadków Poziomu Obrony i 5 Wzrostów Obrażeń
164. [Status [Vengeance_Panic] — podsumowanie] 방어 레벨 감소 6, 피해량 증가 5 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=Vengeance_Panic].summary
   limit: do 120 znaków
   EN: Gain 6 Defense Level Down and 5 Damage Up
   PL: Zyskuje 6 Spadków Poziomu Obrony i 5 Wzrostów Obrażeń
165. [Status [AaCfPbBe] — nazwa] 사냥감 표시
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBe].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBe]`
   limit: do 40 znaków
   EN: Marked Prey
   PL: Oznaczona Zdobycz
166. [Status [AaCfPbBe] — opis] - 이번 턴동안 피해 받지 않고 공격 종료시, 열등감 1 부여 이후 소멸\n- 최대 1
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBe].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit does not take damage during this turn, inflict 1 Inferiority Complex at Attack End then expires\n- Max Stack: 1
   PL: - Przez tę turę nie otrzymuje obrażeń, a po zakończeniu ataku nakłada 1 Kompleksu Niższości, po czym znika\n- Maks. 1
167. [Status [AaCfPbBf] — nazwa] 열등감
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBf].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBf]`
   limit: do 40 znaków
   EN: Inferiority Complex
   PL: Kompleks Niższości
168. [Status [AaCfPbBf] — opis] - 피격시마다 받는 체력 피해량의 (20% * {0})만큼 피해를 입음.\n- 최대 5
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBf].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Every time this unit is hit, take ((20% of HP damage taken) * {0}) damage\n- Max Value: 5
   PL: - Za każdym razem, gdy zostanie trafiony, otrzymuje obrażenia równe (20% otrzymanych obrażeń HP) * {0}\n- Maks. 5
169. [Status [AaCfPbBf] — podsumowanie] 받는 체력 피해량의 (20% * {0})만큼 피해를 입음.
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBf].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take ((20% of HP damage taken) * {0}) damage
   PL: Otrzymuje obrażenia równe (20% otrzymanych obrażeń HP) * {0}.
170. [Status [AaCfPbBa] — nazwa] 폭발하는 우울
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBa]`
   limit: do 40 znaków
   EN: Explosive Gloom
   PL: Wybuchowa Posępność
171. [Status [AaCfPbBa] — opis] - 우울 속성 내성 +0.3\n- 그 외 속성 내성 -0.5\n- 피격 시 대상에게 정신력 피해 3, 자신은 침잠 횟수를 1 얻고, 다음 턴에 공격 레벨 증가 1 얻음 (턴 당 최대 9회 발동)
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBa].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gloom Affinity Resistance +0.3\n- Other Affinity Resistance -0.5\n- When hit: inflict 3 SP damage on the attacker, gain 1 Sinking Count, and gain 1 Offense Level Up next turn (9 times per turn)
   PL: - Odporność na Posępność +0,3\n- Pozostałe odporności -0,5\n- Przy trafieniu zadaje atakującemu 3 obrażeń Poczytalności, zyskuje 1 Licznik Zatonięcia i 1 Wzrostu Poziomu Ataku na następną turę (maks. 9 razy na turę)
172. [Status [AaCfPbBa] — podsumowanie] 우울 속성에만 취약해짐.\n피격 시 정신력 피해 3, 자신은 침잠 횟수를 1 얻고, 다음 턴에 공격 레벨 증가 1 얻음.
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBa].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Resistance to Gloom(and only Gloom) becomes Fatal.\nWhen hit: Inflict 3 SP damage on the attacker, gain 1 Sinking Count, and gain 1 Offense Level Up next turn.
   PL: Odporność na Posępność (i wyłącznie na Posępność) staje się śmiertelna.\nPrzy trafieniu zadaje atakującemu 3 obrażeń Poczytalności, zyskuje 1 Licznika Zatonięcia i w następnej turze 1 Wzrost Poziomu Ataku.
173. [Status [AaCfPbBb] — nazwa] 폭발하는 질투
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBb].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBb]`
   limit: do 40 znaków
   EN: Explosive Envy
   PL: Wybuchowa Zawiść
174. [Status [AaCfPbBb] — opis] - 질투 속성 내성 +0.3\n- 그 외 속성 내성 -0.5\n- 피격 시 대상에게 공격 레벨 증가 1, 출혈 2, 출혈 횟수 2 부여, 다음 턴에 방어 레벨 감소 1 얻음 (턴 당 최대 9회 발동)
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBb].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Envy Affinity Resistance +0.3\n- Other Affinity Resistance -0.5\n- When hit: apply 1 Offense Level Up, inflict 2 Bleed, and 2 Bleed Count on attacker, and gain 1 Defense Level Down next turn (9 times per turn)
   PL: - Odporność na Zawiść +0,3\n- Pozostałe odporności -0,5\n- Przy trafieniu nakłada na atakującego 1 Wzrost Poziomu Ataku, 2 Siły Krwawienia i 2 Liczniki Krwawienia, a w następnej turze zyskuje 1 Spadek Poziomu Obrony (maks. 9 razy na turę)
175. [Status [AaCfPbBb] — podsumowanie] 질투 속성에만 취약해짐.\n피격 시 공격 레벨 증가 1, 출혈 2, 출혈 횟수 2 부여, 다음 턴에 방어 레벨 감소 1 얻음.
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBb].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Resistance to Envy(and only Envy) becomes Fatal\nWhen hit: apply 1 Offense Level Up, 2 Bleed, and 2 Bleed Count on target, and gain 1 Defense Level Down next turn
   PL: Odporność na Zazdrość (i tylko na Zazdrość) staje się śmiertelna\nPrzy trafieniu nakłada na atakującego Wzrost Poziomu Ataku 1, Krwawienie 2 i Licznik Krwawienia 2, a w następnej turze 1 Spadek Poziomu Obrony
176. [Status [AaCfPbBc] — nazwa] 폭발하는 분노
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBc].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBc]`
   limit: do 40 znaków
   EN: Explosive Wrath
   PL: Wybuchowy Gniew
177. [Status [AaCfPbBc] — opis] - 분노 속성 내성 +0.3\n- 그 외 속성 내성 -0.5\n- 피격 시 다음 턴에 공격 레벨 증가 1, 방어 레벨 감소 1 얻음 (턴 당 최대 9회 발동)
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBc].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Wrath Affinity Resistance +0.3\n- Other Affinity Resistance -0.5\n- When hit: Gain 1 Offense Level Up and 1 Defense Level Down next turn (9 times per turn)
   PL: - Odporność na Gniew +0,3\n- Pozostałe odporności -0,5\n- Przy trafieniu w następnej turze zyskuje 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony (maks. 9 razy na turę)
178. [Status [AaCfPbBc] — podsumowanie] 분노 속성에만 취약해짐.\n피격 시 다음 턴에 공격 레벨 증가 1, 방어 레벨 감소 1 얻음.
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBc].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Resistance to Wrath(and only Wrath) becomes Fatal.\nWhen hit, gain 1 Offense Level Up and 1 Defense Level Down.
   PL: Odporność na Gniew (i wyłącznie na Gniew) staje się śmiertelna.\nPrzy trafieniu: 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony w następnej turze.
179. [Status [AaCfPbBd] — nazwa] 깊은 상실
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBd].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBd]`
   limit: do 40 znaków
   EN: Deep Bereavement
   PL: Głęboka Żałoba
180. [Status [AaCfPbBd] — opis] 턴 시작 시 속도 5 감소, 방어 레벨 감소 5 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBd].desc
   limit: do 120 znaków
   EN: Turn Start: Lose 5 Speed and gain 5 Defense Level Down
   PL: Na początku tury traci 5 Szybkości i zyskuje 5 Spadek Poziomu Obrony
181. [Status [AaCfPbBg] — nazwa] 흐트러진 그림
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBg].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBg]`
   limit: do 40 znaków
   EN: Misshapen Painting
   PL: Zniekształcony Obraz
182. [Status [AaCfPbBg] — opis] - 사기저하\n- 공격 위력 증가 1, 취약 1 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBg].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Attack Power Up & 1 Fragile
   PL: - Niskie Morale\n- Zyskuje 1 Wzrost Mocy Ataku i 1 Wrażliwości
183. [Status [AaCfPbBh] — nazwa] 흐트러진 그림
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBh].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBh]`
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Status [AaCfPbBh] — opis] - 패닉\n- 더하기 코인 강화 1, 취약 3 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBh].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Plus Coin Boost & 3 Fragile
   PL: - Panika\n- Zyskuje 1 Wzmocnienie Monet Plus i 3 Wrażliwości
185. [Status [AaCfPbBi] — nazwa] 증오
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBi].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBi]`
   limit: do 40 znaków
   EN: Hatred
   PL: Nienawiść
186. [Status [AaCfPbBi] — opis] - 사기저하\n- 합 승리 시 다음 턴에 공격 레벨 증가를 1 얻음. (턴 당 최대 3)\n합 패배 시 방어 레벨 증가를 1 얻음. (턴 당 최대 3)
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBi].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Win: Gain 1 Offense Level Up next turn. (max 3 per turn)\nClash Lose: Gain 1 Defense Level Up. (max 3 per turn)
   PL: - Niskie Morale\n- Wygrana w Starciu: 1 Wzrost Poziomu Ataku w następnej turze (maks. 3 na turę)\nPrzegrana w Starciu: 1 Wzrost Poziomu Obrony (maks. 3 na turę)
187. [Status [AaCfPbBj] — nazwa] 증오
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBj].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPbBj]`
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Status [AaCfPbBj] — opis] - 패닉\n- 합 승리 시 이번 턴과 다음 턴에 공격 레벨 증가를 1 얻음. (턴 당 최대 3)\n합 패배 시 방어 레벨 증가를 1 얻음. (턴 당 최대 3)\n턴 종료 시 다음 턴에 신속을 2 얻음
   źródło: Bufs-a1c6p2.json :: dataList[id=AaCfPbBj].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Win: Gain 1 Offense Level Up this turn and next turn. (max 3 per turn)\nClash Lose: Gain 1 Defense Level Up. (max 3 per turn)\nTurn End: Gain 2 Haste next turn
   PL: - Panika\n- Wygrana w Starciu: zyskuje 1 Wzrost Poziomu Ataku w tej i następnej turze (maks. 3 na turę)\nPrzegrana w Starciu: zyskuje 1 Wzrost Poziomu Obrony (maks. 3 na turę)\nNa koniec tury zyskuje w następnej turze 2 Pośpiechu

## Statusy i efekty bojowe — Bufs-a1c6p3
- plik gry: `Bufs-a1c6p3.json`

189. [Status [AaCfPcBe] — nazwa] 깊은 상실
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBe].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBe]`
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Status [AaCfPcBe] — opis] 공격 종료 시 정신력 5 피해 입힘.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBe].desc
   limit: do 120 znaków
   EN: Inflict 5 SP damage at Attack End.
   PL: Po zakończeniu ataku zadaje 5 obrażeń Poczytalności.
191. [Status [AaCfPcBf] — nazwa] 해방되지 못한 서글픔
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBf].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBf]`
   limit: do 40 znaków
   EN: Fettered Woe
   PL: Skuty Żal
192. [Status [AaCfPcBf] — opis] 특정 조건에서 턴 종료시 3이상이면, 다음 턴에 모든 부위가 흐트러짐 상태가 됨.\n사슬 부위에 취약을 3 얻고 소멸함.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBf].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Under a certain condition, and at 3+ Value at Turn End, all Parts become Staggered next turn.\nExpires after applying 3 Fragile to the Chain Part
   PL: - Przy określonym warunku, przy wartości 3+ na koniec tury, wszystkie części przechodzą w Oszołomienie w następnej turze.\nNakłada 3 Wrażliwości na część Łańcucha i znika
193. [Status [AaCfPcBg] — nazwa] 분노의 대상
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBg].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBg]`
   limit: do 40 znaków
   EN: Subject of Wrath
   PL: Cel Gniewu
194. [Status [AaCfPcBg] — opis] 마음이 찢겨진 히스클리프의 공격에 우선 지정 당함.\n죽음을 맞이할 때, 다른 인격에게 부여가 됨.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBg].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Becomes a priority attack target for Heathcliff The Heartbroken.\nWhen this unit is killed, this effect moves to a different Identity.
   PL: Staje się głównym celem ataków Heathcliffa ze Złamanym Sercem.\nGdy ginie, efekt przenosi się na inną Tożsamość.
195. [Status [AaCfPcBb] — nazwa] 버틀러의 표식
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBb].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBb]`
   limit: do 40 znaków
   EN: Butler's Mark
   PL: Znak Kamerdynera
196. [Status [AaCfPcBb] — opis] 특정 공격 스킬의 가중치 증가에 사용됨
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBb].desc
   limit: do 120 znaków
   EN: Used to raise Atk Weight of certain Attack Skills
   PL: Służy do zwiększania Wagi Ataku określonych Umiejętności ataku
197. [Status [AaCfPcBc] — nazwa] 포박술
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBc].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBc]`
   limit: do 40 znaków
   EN: Binding Technique
   PL: Technika Spętań
198. [Status [AaCfPcBc] — opis] - 최대 3\n- 턴 종료시 1 증가\n- 턴 종료 시 다음 턴에 속박을 수치만큼 얻음.\n- 턴 종료 시 수치가 3이면, 이번 전투 동안 흐트러짐 상태가 됨.\n소멸하지 않음.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBc].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max 3\n- Turn End: increases by 1\n- Turn End: gain Bind equal to the Value of this effect.\n- Turn End: if at 3 Value, become Staggered for the rest of the Encounter.\nDoes not expire.
   PL: - Maks. 3\n- Na koniec tury rośnie o 1\n- Na koniec tury zyskuje w następnej turze Spętanie równe wartości.\n- Na koniec tury, przy wartości 3, popada w stan Oszołomienia na resztę walki.\nNie znika.
199. [Status [AaCfPcBc] — podsumowanie] 다음 턴에 속박을 수치만큼 얻음.\n수치가 3이면, 이번 전투 동안 흐트러짐 상태가 됨.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBc].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Bind equal to the Value next turn.\nIf at 3 Value, become Staggered for the rest of the Encounter.
   PL: W następnej turze zyskuje Spętań w liczbie wartości.\nPrzy wartości 3 przechodzi w stan Oszołomienia na resztę walki.
200. [Status [AaCfPcBa] — nazwa] 각오
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBa]`
   limit: do 40 znaków
   EN: Determination
   PL: Postanowienie
201. [Status [AaCfPcBa] — opis] 피격 시 다음 턴에 공격 레벨 증가 1 얻음.(턴 당 3회)\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.\n자신이 고정 편성되어야 하는 전투에서 자신의 퇴각 관련 기능이 작동하지 않음.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBa].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When attacked, gain 1 Offense Level Up next turn. (3 times per turn)\n- Turn Start: If at less than 0 SP, gain 3 Attack Power Up.\nThis unit's Retreat abilities do not activate for the duration of this Encounter.
   PL: Przy trafieniu zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury, przy Poczytalności poniżej 0, zyskuje 3 Wzrosty Mocy Ataku.\nW walkach, w których ta jednostka musi zostać obowiązkowo rozmieszczona, jej funkcje wycofania nie działają.
202. [Status [AaCfPcBa] — podsumowanie] 피격 시 공격 레벨 증가 1 얻음.\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBa].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit, gain 1 Offense Level Up next turn.\nTurn Start: at less than 0 SP, gain 3 Attack Power Up.
   PL: Przy trafieniu zyskuje 1 Wzrost Poziomu Ataku.\nNa początek tury, przy Poczytalności poniżej 0, zyskuje 3 Wzrosty Mocy Ataku.
203. [Status [AaCfPcBh] — nazwa] 고통스러운 분노
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBh].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBh]`
   limit: do 40 znaków
   EN: Excruciating Rage
   PL: Rozdzierający Gniew
204. [Status [AaCfPcBh] — opis] 공격자에게 폭발하는 분노가 있으면 받는 피해 +100%
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBh].desc
   limit: do 120 znaków
   EN: If the attacker has Explosive Wrath, take +100% damage
   PL: Jeżeli atakujący posiada Wybuchowy Gniew, otrzymuje +100% obrażeń
205. [Status [AaCfPcBm] — nazwa] 고통의 벼락
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBm].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBm]`
   limit: do 40 znaków
   EN: Lightning of Suffering
   PL: Grom Cierpienia
206. [Status [AaCfPcBm] — opis] - 합 승리 시 대상에게 찢어지는 마음을 부여하고, 대상에게 체력 피해를 7 준다.\n- 합 패배 또는 일방 공격 종료 시 찢어지는 마음을 얻고, 체력 피해를 7 받는다.\n- 스킬 종료 시 1 감소
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBm].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Win: Inflict Breaking Heart and deal 7 HP damage.\n- Clash Lose or After Unopposed Attack: Gain Breaking Heart and take 7 HP damage.\n- Reduced by 1 at Skill End
   PL: - Po wygranym Starciu nakłada na cel Rwające Serce i zadaje 7 obrażeń HP.\n- Po przegranej w Starciu lub po Ataku Jednostronnym zyskuje Rwające Serce i otrzymuje 7 obrażeń HP.\n- Na koniec Umiejętności maleje o 1
207. [Status [AaCfPcBn] — nazwa] 찢어지는 마음
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBn].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBn]`
   limit: do 40 znaków
   EN: Breaking Heart
   PL: Rwające Serce
208. [Status [AaCfPcBn] — opis] - (수치 X 0.2)만큼 모든 죄악 속성 내성 증가\n- 수치가 3이 되면 흐트러짐 상태가 된다.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Every Sin Affinity Resistance is increased by (Value x 0.2)\n- At 3 Value, become Staggered.
   PL: - Zwiększa odporność na wszystkie Grzechy o (wartość x 0,2)\n- Przy wartości 3 przechodzi w stan Oszołomienia.
209. [Status [AaCfPcBp] — nazwa] 다가갈 용기
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBp].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBp]`
   limit: do 40 znaków
   EN: Courage to Approach
   PL: Odwaga, by się Zbliżyć
210. [Status [AaCfPcBp] — opis] - 턴 종료시 정신력 10 회복\n- 매 턴마다 공격 위력 증가 3, 보호 5 얻음\n- 피격 시 정신력 5 회복. 다음 턴에 공격 레벨 증가 1 얻음.(턴 당 3회)\n- 턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.\n- 이번 전투동안 생존한 아군이 자신을 제외하여 1명 이상 있을 때, 히스클리프의 체력이 1 미만으로 감소하지 않는다.\n이번 전투동안 자신의 퇴각 관련 기능이 작동하지 않음.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBp].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Heal 10 SP\n- Gain 3 Attack Power Up and 5 Protection every turn\n- When attacked, heal 5 SP. Gain 1 Offense Level Up next turn. (3 times per turn)\n- Turn Start: If at less than 0 SP, gain 3 Attack Power Up.\n- As long as there are 1 or more other surviving ally in this Encounter, Heathcliff's HP does not drop below 1.\nThis unit's Retreat abilities do not activate for the duration of this Encounter.
   PL: - Na koniec tury odzyskuje 10 Poczytalności\n- Co turę zyskuje 3 Wzrostu Mocy Ataku i 5 Ochrony\n- Przy trafieniu odzyskuje 5 Poczytalności. W następnej turze zyskuje 1 Wzrost Poziomu Ataku. (3 razy na turę)\n- Na początku tury, jeżeli Poczytalność jest niższa od 0, zyskuje 3 Wzrostu Mocy Ataku.\n- Dopóki w tej walce żyje co najmniej 1 sojusznik poza Heathcliffem, HP Heathcliffa nie spada poniżej 1.\nW tej walce funkcje wycofania tej jednostki nie działają.
211. [Status [AaCfPcBo] — nazwa] 각오
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBo].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBo]`
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Status [AaCfPcBo] — opis] 턴 종료 시 정신력 회복 10. 피격 시 다음 턴에 공격 레벨 증가 1 얻음.(턴 당 3회)\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.\n이번 전투동안 생존한 아군이 자신을 제외하여 1명 이상 있을 때, 히스클리프의 체력이 1 미만으로 감소하지 않는다.\n이번 전투동안 퇴각 관련 기능이 작동하지 않음.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBo].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Heal 10 SP. When attacked, heal 5 SP. Gain 1 Offense Level Up next turn. (3 times per turn)\n- Turn Start: If at less than 0 SP, gain 3 Attack Power Up.\n- As long as there are 1 or more other surviving allies in this Encounter, Heathcliff's HP does not drop below 1.\nThis unit's Retreat abilities do not activate for the duration of this Encounter.
   PL: Na koniec tury odzyskuje 10 Poczytalności. Przy trafieniu zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury, przy Poczytalności poniżej 0, zyskuje 3 Wzrosty Mocy Ataku.\nDopóki w tej walce przeżywa co najmniej 1 sojusznik poza nim samym, HP Heathcliffa nie spada poniżej 1.\nW tej walce funkcje wycofania nie działają.
213. [Status [AaCfPcBo] — podsumowanie] 턴 종료 시 정신력 회복 10.\n피격 시 공격 레벨 증가 1 얻음.\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBo].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: heal 10 SP. \nWhen hit, gain 1 Offense Level Up.\nTurn Start: at less than 0 SP, gain 3 Attack Power Up.
   PL: Na koniec tury odzyskuje 10 Poczytalności.\nPrzy trafieniu: 1 Wzrost Poziomu Ataku.\nNa początek tury przy Poczytalności ujemnej: 3 Wzrosty Mocy Ataku.
214. [Status [AaCfPcBq] — nazwa] 찢긴 마음
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBq].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBq]`
   limit: do 40 znaków
   EN: Broken Heart
   PL: Złamane Serce
215. [Status [AaCfPcBq] — opis] - 최대 속도 값 +2\n- 매 턴마다 피해량 증가, 취약 3 얻음\n- 메인 공격 대상이 히스클리프면 공격 스킬의 최종 위력 +2\n- 히스클리프에게 합 패배 시 다음 턴에 속박 3, 피해량 감소 3 얻음
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBq].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Speed +2\n- Gain 3 Damage Up and 3 Fragile every turn\n- If the main target is Heathcliff, the Attack Skill gains Final Power +2\n- Clash Lose against Heathcliff: gain 3 Bind and 3 Damage Down next turn
   PL: - Maks. Szybkość +2\n- Co turę zyskuje 3 Wzrostu Obrażeń i 3 Wrażliwości\n- Jeżeli głównym celem jest Heathcliff, Umiejętność ataku zyskuje Moc Końcowa +2\n- Po przegranej w Starciu z Heathcliffem w następnej turze zyskuje 3 Spętań i 3 Spadku Obrażeń
216. [Status [AaCfPcBr] — nazwa] 고통 속에서...비참하게 깨어나기를!
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBr].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBr]`
   limit: do 40 znaków
   EN: May She... Wake in Torment!
   PL: Niech się... Przebudzi w Męce!
217. [Status [AaCfPcBr] — opis] 고통의 벼락이 부여된 대상과 합 진행 시 합 위력 -6
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBr].desc
   limit: do 120 znaków
   EN: Clash Power -6 in a Clash against targets with Lightning of Suffering
   PL: Moc Starcia -6 w Starciu z celami posiadającymi Grom Cierpienia
218. [Status [AaCfPcBi] — nazwa] 고열기전
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBi].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBi]`
   limit: do 40 znaków
   EN: Superthermogenesis
   PL: Nadtermogeneza
219. [Status [AaCfPcBi] — opis] 턴 종료 시 수치에 비례하여 고정 피해를 받고 효과 소멸
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBi].desc
   limit: do 120 znaków
   EN: Turn End: Take fixed damage based on Stack and lose this effect
   PL: Na koniec tury otrzymuje obrażenia stałe zależne od wartości i traci efekt
220. [Status [AaCfPcBs] — nazwa] 방해하지마
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBs].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBs]`
   limit: do 40 znaków
   EN: Away With You
   PL: Nie Przeszkadzaj
221. [Status [AaCfPcBs] — opis] 남은 보호막 수치 : {0}
   źródło: Bufs-a1c6p3.json :: dataList[id=AaCfPcBs].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Remaining Shield Value : {0}
   PL: Pozostała wartość Tarczy: {0}
222. [Status [RageResonance] — nazwa] 움켜쥔 분노
   źródło: Bufs-a1c6p3.json :: dataList[id=RageResonance].name
   kontekst: identyfikator statusu w tekstach: `[RageResonance]`
   limit: do 40 znaków
   EN: Seized Wrath
   PL: Uchwycony Gniew
223. [Status [RageResonance] — opis] 턴 종료 시, 다음 턴에 공격 레벨 증가를 {0} 얻음 (매 턴마다 효과 강화됨)
   źródło: Bufs-a1c6p3.json :: dataList[id=RageResonance].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: gain {0} Offense Level Up next turn (effect intensifies with each turn)
   PL: Na koniec tury zyskuje w następnej turze {0} Wzrostu Poziomu Ataku (efekt nasila się z każdą turą)

## Statusy i efekty bojowe — Bufs-a1c7p1
- plik gry: `Bufs-a1c7p1.json`

224. [Status [BloodScissor] — nazwa] 핏빛 가위날
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissor].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissor]`
   limit: do 40 znaków
   EN: Blood-tinged Scissorblades
   PL: Zakrwawione Ostrza Nożyc
225. [Status [BloodScissor] — opis] - 최댓값 : 10\n- 핏빛 가위날 1단계\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissor].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Blood-tinged Scissorblades\n- Used for special skills
   PL: - Maks. wartości: 10\n- Krwawe Ostrza Nożyc 1. stopnia\n- Służy Umiejętnościom specjalnym
226. [Status [BloodScissorTwo] — nazwa] 핏빛 가위날 II
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissorTwo].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissorTwo]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades II
   PL: Zakrwawione Ostrza Nożyc II
227. [Status [BloodScissorTwo] — opis] - 최댓값 : 20\n- 핏빛 가위날 2단계\n- 턴 시작시 수치 5당 공격 레벨 증가 1, 방어 레벨 감소 1 얻음\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissorTwo].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Blood-tinged Scissorblades\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Down for every 5 Stack\n- Used for certain Skills
   PL: - Maks. wartości: 20\n- Krwawe Ostrza Nożyc 2. stopnia\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony za każde 5 wartości\n- Służy Umiejętnościom specjalnym
228. [Status [BloodScissorThree] — nazwa] 핏빛 가위날 III
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissorThree].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissorThree]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades III
   PL: Zakrwawione Ostrza Nożyc III
229. [Status [BloodScissorThree] — opis] - 최댓값 : 30\n- 핏빛 가위날 3단계\n- 턴 시작시 수치 5당 공격 레벨 증가 2, 방어 레벨 감소 1 얻음\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissorThree].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Blood-tinged Scissorblades\n- Turn Start: gain 2 Offense Level Up and 1 Defense Level Down for every 5 Stack\n- Used for certain Skills
   PL: - Maks. wartości: 30\n- Krwawe Ostrza Nożyc 3. stopnia\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku i 1 Spadek Poziomu Obrony za każde 5 wartości\n- Służy Umiejętnościom specjalnym
230. [Status [BloodDinner] — nazwa] 혈찬
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodDinner].name
   kontekst: identyfikator statusu w tekstach: `[BloodDinner]`
   limit: do 40 znaków
   EN: Bloodfeast
   PL: Krwawa Uczta
231. [Status [BloodDinner] — opis] - 최댓값 : 999\n- 해당 장소에서 발생한 출혈 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함\n- 아군 중 같은 턴에 혈찬을 소모하는 상위 권속이 있으면, 해당 캐릭터가 혈찬을 소모할 때까지 혈찬을 소모할 수 없음
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodDinner].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 999\n- Stores all Bleed damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters\n- Among allies, if there is a higher Kindred who also consumes Bloodfeast in the same turn, this unit cannot consume Bloodfeast until that ally consumes it first.
   PL: - Maks. wartości: 999\n- Przechowuje obrażenia Krwawienia zadane w tym miejscu\n- Resetuje się przy zmianie miejsca walki\n- Wartość jest współdzielona przez wszystkie postacie\n- Jeżeli wśród sojuszników jest wyższy Pokrewny, który w tej samej turze zużywa Krwawą Ucztę, ta jednostka nie może jej zużyć, dopóki nie zrobi tego tamten sojusznik
232. [Status [BloodDinner_Accumulation] — nazwa] 누적 소모 혈찬
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodDinner_Accumulation].name
   kontekst: identyfikator statusu w tekstach: `[BloodDinner_Accumulation]`
   limit: do 40 znaków
   EN: Bloodfeast Consumed
   PL: Skonsumowana Krwawa Uczta
233. [Status [BloodDinner_Accumulation] — opis] - 최댓값 : 999\n- 이번 전투 동안 누적 소모한 혈찬 : {0}
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodDinner_Accumulation].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Value: 999\n- Total Bloodfeast consumed in this Encounter: {0}
   PL: - Maks. wartości: 999\n- Skumulowana zużyta Krwawa Uczta w tej walce: {0}
234. [Status [FamineBlood_LowMorale] — nazwa] 굶주림
   źródło: Bufs-a1c7p1.json :: dataList[id=FamineBlood_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[FamineBlood_LowMorale]`
   limit: do 40 znaków
   EN: Hunger
   PL: Głód
235. [Status [FamineBlood_LowMorale] — opis] - 사기 저하\n턴 시작 시, 속박 1, 공격 위력 증가 2 얻음. 턴 종료 시, 정신력 5 피해
   źródło: Bufs-a1c7p1.json :: dataList[id=FamineBlood_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: gain 1 Bind and 3 Attack Power Up. Turn End: take 5 SP damage
   PL: - Niskie Morale\nNa początek tury: 1 Spętania i 2 Wzrosty Mocy Ataku. Na koniec tury 5 obrażeń Poczytalności
236. [Status [FamineBlood_Panic] — nazwa] 굶주림
   źródło: Bufs-a1c7p1.json :: dataList[id=FamineBlood_Panic].name
   kontekst: identyfikator statusu w tekstach: `[FamineBlood_Panic]`
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Status [FamineBlood_Panic] — opis] - 패닉\n턴 시작 시, 속박 2, 공격 위력 증가 4 얻음.
   źródło: Bufs-a1c7p1.json :: dataList[id=FamineBlood_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: Gain 2 Bind and 4 Attack Power Up.
   PL: - Panika\nNa początku tury zyskuje 2 Spętań i 4 Wzrostu Mocy Ataku.
238. [Status [DuelDeclaration_Camille] — nazwa] 결투 선포 - 까미유
   źródło: Bufs-a1c7p1.json :: dataList[id=DuelDeclaration_Camille].name
   kontekst: identyfikator statusu w tekstach: `[DuelDeclaration_Camille]`
   limit: do 40 znaków
   EN: Declared Duel - Camille
   PL: Wyzwanie na Pojedynek - Camille
239. [Status [DuelDeclaration_Camille] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1\n공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회)\n부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸.\n다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: Bufs-a1c7p1.json :: dataList[id=DuelDeclaration_Camille].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit with the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. \n- Replaced when another unit inflicts Declared Duel on the same target.
   PL: W Starciu między jednostką, która nałożyła Wyzwanie na Pojedynek, a jednostką z tym efektem wyzywająca ma Moc Starcia +1.\nPrzy trafieniu w następnej turze zyskuje 1 Pośpiechu. (maks. 4 razy na turę)\nEfekt znika, gdy wyzywająca jednostka nałoży go na inny cel.\nZastępowany, gdy inna postać nałoży Wyzwanie na Pojedynek.
240. [Status [RecklessDuel] — nazwa] 무모한 결투
   źródło: Bufs-a1c7p1.json :: dataList[id=RecklessDuel].name
   kontekst: identyfikator statusu w tekstach: `[RecklessDuel]`
   limit: do 40 znaków
   EN: Foolhardy Duel
   PL: Nieostrożny Pojedynek
241. [Status [RecklessDuel] — opis] 턴 종료시 전투 중 전체 체력의 잃어버린 체력 10%당 다음 턴에 합 위력 증가를 얻음. (최대 5)\n턴 종료시 전투 중 전체 체력의 잃어버린 체력 10%당 다음 턴에 속박을 얻음. (최대 5)
   źródło: Bufs-a1c7p1.json :: dataList[id=RecklessDuel].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: gain 1 Clash Power Up next turn for every 10% of the missing HP. (max 5)\nTurn End: gain 1 Bind next turn for every 10% of the missing HP. (max 5)
   PL: Na koniec tury zyskuje 1 Wzrost Mocy Starcia na następną turę za każde 10% brakującego HP. (maks. 5)\nNa koniec tury zyskuje 1 Spętanie na następną turę za każde 10% brakującego HP. (maks. 5)
242. [Status [ConcentratedAttack] — nazwa] 집중 공격
   źródło: Bufs-a1c7p1.json :: dataList[id=ConcentratedAttack].name
   kontekst: identyfikator statusu w tekstach: `[ConcentratedAttack]`
   limit: do 40 znaków
   EN: Focused Attack
   PL: Atak Skupiony
243. [Status [ConcentratedAttack] — opis] 특정 슬롯에 사용됨
   źródło: Bufs-a1c7p1.json :: dataList[id=ConcentratedAttack].desc
   limit: do 120 znaków
   EN: Used on certain Slots
   PL: Używane na określonych slotach
244. [Status [TrulyWeak] — nazwa] 약자
   źródło: Bufs-a1c7p1.json :: dataList[id=TrulyWeak].name
   kontekst: identyfikator statusu w tekstach: `[TrulyWeak]`
   limit: do 40 znaków
   EN: The Weak
   PL: Słabeusz
245. [Status [TrulyWeak] — opis] - 가하는 피해량 -10%\n- 턴 종료시 수치 1 감소
   źródło: Bufs-a1c7p1.json :: dataList[id=TrulyWeak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal -10% damage\n- Turn End: Reduce Value by 1
   PL: - Zadaje -10% obrażeń\n- Na koniec tury wartość maleje o 1
246. [Status [RealPaperBear] — nazwa] 진짜 곰
   źródło: Bufs-a1c7p1.json :: dataList[id=RealPaperBear].name
   kontekst: identyfikator statusu w tekstach: `[RealPaperBear]`
   limit: do 40 znaków
   EN: An Actual Bear
   PL: Prawdziwy Niedźwiedź
247. [Status [RealPaperBear] — opis] - 사람까지 잡아먹는 무시무시한 곰
   źródło: Bufs-a1c7p1.json :: dataList[id=RealPaperBear].desc
   limit: do 120 znaków
   EN: - It eats people. How fearsome!
   PL: - Zjada ludzi. Jak przerażające!
248. [Status [BloodScissorScars] — nazwa] 깊게 베인 상처
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissorScars].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissorScars]`
   limit: do 40 znaków
   EN: Deep Laceration
   PL: Głębokie Rozcięcie
249. [Status [BloodScissorScars] — opis] 합 패배 시, 출혈 횟수가 3 증가하고, 자신의 출혈이 발동됨. 이후  출혈 횟수 1 감소.\n- 턴 종료 시 제거
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodScissorScars].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Lose: gain +3 Bleed Count and trigger Bleed on self. Then, lose 1 Bleed Count.\n- Expires at Turn End
   PL: Po przegranej w Starciu Licznik Krwawienia rośnie o 3 i wywołuje Krwawienie. Następnie Licznik Krwawienia maleje o 1.\n- Znika na koniec tury
250. [Status [LineCutting] — nazwa] 재봉 대상
   źródło: Bufs-a1c7p1.json :: dataList[id=LineCutting].name
   kontekst: identyfikator statusu w tekstach: `[LineCutting]`
   limit: do 40 znaków
   EN: Sewing Target
   PL: Cel Szycia
251. [Status [LineCutting] — opis] - ???의 우선 공격 대상이 됨.\n- 턴 종료 시 제거
   źródło: Bufs-a1c7p1.json :: dataList[id=LineCutting].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Prioritized by ???.\n- Expires at Turn End
   PL: - Staje się głównym celem ataków ???.\n- Znika na koniec tury
252. [Status [StarvingBarberOne] — nazwa] 노쇠
   źródło: Bufs-a1c7p1.json :: dataList[id=StarvingBarberOne].name
   kontekst: identyfikator statusu w tekstach: `[StarvingBarberOne]`
   limit: do 40 znaków
   EN: Withered
   PL: Zwiędnięcie
253. [Status [StarvingBarberOne] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: Bufs-a1c7p1.json :: dataList[id=StarvingBarberOne].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Starved for blood for a long, long time.\n- Lose 15 Base Offense Level\n- Lose 15 Base Defense Level
   PL: - Przez długi, długi czas nie mógł wypić krwi.\n- Podstawowy Poziom Ataku -15\n- Podstawowy Poziom Obrony -15
254. [Status [StarvingBarberTwo] — nazwa] 노쇠
   źródło: Bufs-a1c7p1.json :: dataList[id=StarvingBarberTwo].name
   kontekst: identyfikator statusu w tekstach: `[StarvingBarberTwo]`
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Status [StarvingBarberTwo] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 25 감소\n- 기본 방어 레벨 25 감소
   źródło: Bufs-a1c7p1.json :: dataList[id=StarvingBarberTwo].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Starved for blood for a long, long time.\n- Lose 25 Base Offense Level\n- Lose 25 Base Defense Level
   PL: - Przez długi, długi czas nie mógł wypić krwi.\n- Podstawowy Poziom Ataku -25\n- Podstawowy Poziom Obrony -25
256. [Status [BloodShooting] — nazwa] 블러드슈팅!!
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodShooting].name
   kontekst: identyfikator statusu w tekstach: `[BloodShooting]`
   limit: do 40 znaków
   EN: Blood-shooting!!
   PL: Krwawy Wystrzał!!
257. [Status [BloodShooting] — opis] 사망 시\n- 혈찬 30 증가\n- 가장 수량이 적은 E.G.O 자원 2 증가\n- 다음 턴에 자신과 같은 팀의 캐릭터의 모든 물리 내성이 0.1 증가. 이 효과는 중첩됨. (최대 5)
   źródło: Bufs-a1c7p1.json :: dataList[id=BloodShooting].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Death:\n- Bloodfeast +30\n- gain 2 E.G.O resource for the least-owned E.G.O resource\n- Next turn: all allies gain 0.1 to all Phys. Resistances. This effect can stack. (max 5)
   PL: Po śmierci\n- Krwawa Uczta +30\n- Zyskuje 2 Zasoby E.G.O najmniej posiadanego Grzechu\n- W następnej turze wszystkie odporności fizyczne postaci z jego drużyny rosną o 0,1. Ten efekt się kumuluje. (maks. 5)
258. [Status [RighteousFeeling] — nazwa] 정의로운 기분이라네!!
   źródło: Bufs-a1c7p1.json :: dataList[id=RighteousFeeling].name
   kontekst: identyfikator statusu w tekstach: `[RighteousFeeling]`
   limit: do 40 znaków
   EN: HOW RIGHTEOUS!!
   PL: Jak to Sprawiedliwie!!
259. [Status [RighteousFeeling] — opis] - 매 턴 종료 시, 다음 턴에 신속 1, 공격 레벨 증가 3, 방어 레벨 감소 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: Bufs-a1c7p1.json :: dataList[id=RighteousFeeling].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At every Turn End: gain 1 Haste, 3 Offense Level Up, and 3 Defense Level Down next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Na koniec każdej tury zyskuje w następnej turze 1 Pośpiech, 3 Wzrostu Poziomu Ataku i 3 Spadek Poziomu Obrony\n- Za każde 3 zsumowane tury zyskuje +2 Wzrostu Poziomu Ataku (maks. 6)\n- Po wygranym Starciu odzyskuje 3 Poczytalności\n- Przy zabiciu wroga w następnej turze zyskuje 1 Wzrost Mocy Starcia (1 raz na turę)
260. [Status [DuelDeclarationMeursault] — nazwa] 결투 선포 - 뫼르소
   źródło: Bufs-a1c7p1.json :: dataList[id=DuelDeclarationMeursault].name
   kontekst: identyfikator statusu w tekstach: `[DuelDeclarationMeursault]`
   limit: do 40 znaków
   EN: Declared Duel - Meursault
   PL: Wyzwanie na Pojedynek - Meursault
261. [Status [DuelDeclarationMeursault] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1\n공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회)\n부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸.\n다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: Bufs-a1c7p1.json :: dataList[id=DuelDeclarationMeursault].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Status [ConcentratedAttackMeursault] — nazwa] 집중 공격 - 뫼르소
   źródło: Bufs-a1c7p1.json :: dataList[id=ConcentratedAttackMeursault].name
   kontekst: identyfikator statusu w tekstach: `[ConcentratedAttackMeursault]`
   limit: do 40 znaków
   EN: Focused Attack - Meursault
   PL: Atak Skupiony - Meursault
263. [Status [ConcentratedAttackMeursault] — opis] <집중 전투 전용>\n집중 공격을 부여한 캐릭터가 대상 슬롯의 집중 공격 수치에 따라 다음 효과를 얻음\n1스택: 합 위력 +1\n2스택: 기본 위력 + 1\n3스택: 기본 위력 + 1, 코인 위력 + 1\n- 부여한 캐릭터가 한 턴 동안 집중 공격이 부여된 슬롯에 공격을 성공하지 못하면, 소멸.
   źródło: Bufs-a1c7p1.json :: dataList[id=ConcentratedAttackMeursault].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: <Focused Encounters Only>\nThe unit that inflicted this Focused Attack gains the following effects based on the target Slot's Focused Attack Stack.\n  · 1x Stack: Gain Clash Power +1\n  · 2x Stack: Gain Base Power +1\n  · 3x Stack: Gain Base Power +1 and Coin Power +1\n- Expires if, for a turn, the unit that inflicted it fails to hit the Slot inflicted with their Focused Attack.
   PL: <Tylko walki skupione>\nJednostka, która nadała Atak Skupiony, zyskuje następujące efekty zależnie od liczby stosów Ataku Skupionego na slotu celu\n1 stos: Moc Starcia +1\n2 stosy: Moc Bazowa +1\n3 stosy: Moc Bazowa +1, Moc Monet +1\n- Znika, jeśli nadająca jednostka nie przeprowadzi w tej turze udanego ataku na slot z nadanym Atakiem Skupionym.
264. [Status [Duello_LowMorale] — nazwa] 1:1 전력
   źródło: Bufs-a1c7p1.json :: dataList[id=Duello_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Duello_LowMorale]`
   limit: do 40 znaków
   EN: Duel Specialist
   PL: Specjalista od Pojedynków
265. [Status [Duello_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 증가 2 얻음. 합 패배 시 방어 레벨 감소 1얻음 (턴 당 최대 3). 속도 최솟값 -1
   źródło: Bufs-a1c7p1.json :: dataList[id=Duello_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Offense Level Up. On Clash Lose, gain 1 Defense Level Down(max 3 per turn). Min. Speed -1
   PL: - Niskie Morale\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku. Po przegranej w Starciu zyskuje 1 Spadek Poziomu Obrony (maks. 3 na turę). Min. Szybkość -1
266. [Status [Duello_Panic] — nazwa] 1:1 전력
   źródło: Bufs-a1c7p1.json :: dataList[id=Duello_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Duello_Panic]`
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Status [Duello_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 레벨 증가 4 얻음. 합 패배 시 방어 레벨 감소 2얻음 (턴 당 최대 6). 속도 최솟값 -1
   źródło: Bufs-a1c7p1.json :: dataList[id=Duello_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 4 Offense Level Up. On Clash Lose, gain 2 Defense Level Down(max 6 per turn). Min. Speed -1
   PL: - Panika\n- Na początku tury zyskuje 4 Wzrostu Poziomu Ataku. Po przegranej w Starciu zyskuje 2 Spadku Poziomu Obrony (maks. 6 na turę). Min. Szybkość -1
268. [Status [RighteousFeelingSancho] — nazwa] 피눈물을 머금고, 내가 책임지겠다.
   źródło: Bufs-a1c7p1.json :: dataList[id=RighteousFeelingSancho].name
   kontekst: identyfikator statusu w tekstach: `[RighteousFeelingSancho]`
   limit: do 70 znaków
   EN: I will take responsibility, through my bloody tears.
   PL: Zapłakawszy krwawymi łzami, wezmę to na siebie.
269. [Status [RighteousFeelingSancho] — opis] - 경혈을 얻을 때마다, 경혈을 1 추가로 얻음. (턴 당 최대 5회)\n- 매 턴 종료 시, 다음 턴에 신속 2, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: Bufs-a1c7p1.json :: dataList[id=RighteousFeelingSancho].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 additional Hardblood every time this unit gains Hardblood. (5 times per turn)\n- At every Turn End: gain 2 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Za każde zdobycie Twardej Krwi zyskuje dodatkowo 1 Twardej Krwi. (maks. 5 razy na turę)\n- Na koniec każdej tury zyskuje w następnej turze 2 Pośpiechu i 3 Wzrostu Poziomu Ataku\n- Za każde 3 zsumowane tury zyskuje dodatkowo 2 Wzrostu Poziomu Ataku (maks. 6)\n- Po wygranym Starciu odzyskuje 3 Poczytalności\n- Przy zabiciu wroga w następnej turze zyskuje 1 Wzrost Mocy Starcia (1 raz na turę)
270. [Status [UnfinishedDreamSancho] — nazwa] 물보다 진한 피에서 벗어나지 못하여,
   źródło: Bufs-a1c7p1.json :: dataList[id=UnfinishedDreamSancho].name
   kontekst: identyfikator statusu w tekstach: `[UnfinishedDreamSancho]`
   limit: do 90 znaków
   EN: In which is recounted the thralldom to blood thicker than water.
   PL: Niezdolny do oswobodzenia z krwi gęstszej niż woda,
271. [Status [UnfinishedDreamSancho] — opis] - 경혈을 얻을 때마다, 경혈을 2 추가로 얻음. (턴 당 최대 5회)\n- 매 턴 종료 시, 다음 턴에 신속 2, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: Bufs-a1c7p1.json :: dataList[id=UnfinishedDreamSancho].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 2 additional Hardblood every time this unit gains Hardblood. (5 times per turn)\n- At every Turn End: gain 2 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 2 Clash Power Up next turn (once per turn)
   PL: - Za każdym razem, gdy zyskuje Twardą Krew, zyskuje dodatkowo 2 Twardą Krew (maks. 5 razy na turę)\n- Na koniec tury w następnej turze zyskuje 2 Pośpiechu i 3 Wzrosty Poziomu Ataku\n- Za każde 3 skumulowane tury zyskuje dodatkowe 2 Wzrosty Poziomu Ataku (maks. 6)\n- Wygrana w Starciu: odzyskuje 3 Poczytalności\n- Za zabicie wroga zyskuje 1 Wzrost Mocy Starcia w następnej turze (raz na turę)
272. [Status [FragmentOfHopeSancho] — nazwa] 고통 받은 가족들을 위해 피의 만찬을 열고,
   źródło: Bufs-a1c7p1.json :: dataList[id=FragmentOfHopeSancho].name
   kontekst: identyfikator statusu w tekstach: `[FragmentOfHopeSancho]`
   limit: do 90 znaków
   EN: Which treats the banquet of blood for the Family's suffering.
   PL: W którym urządza się ucztę krwi dla cierpiącej Rodziny,
273. [Status [FragmentOfHopeSancho] — opis] 수치만큼 합 위력 증가\n가하는 피해량 +10%
   źródło: Bufs-a1c7p1.json :: dataList[id=FragmentOfHopeSancho].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power Up equal to Stack\nDeal +10% damage
   PL: Zyskuje Wzrost Mocy Starcia w liczbie wartości\nZadaje obrażenia +10%
274. [Status [FragmentOfHopeTwoSancho] — nazwa] 자식을 등진 어버이를 처단하여 모든 죄악감을 짊어진 어느 혈귀에 대하여
   źródło: Bufs-a1c7p1.json :: dataList[id=FragmentOfHopeTwoSancho].name
   kontekst: identyfikator statusu w tekstach: `[FragmentOfHopeTwoSancho]`
   limit: do 130 znaków
   EN: Of how a lone Bloodfiend came to bear the guilt of slaying the Father who forsook his Children.
   PL: O pewnym Krwiożercy, który po zabiciu rodzica wziął całą winę na siebie,
275. [Status [FragmentOfHopeTwoSancho] — opis] - 수치당 합 위력 +4\n- 전투 시작 시 자신과 아군에게 보호막 부여\n- 가하는 피해량 +20%\n- 적중시마다 고정 피해 1 입힘
   źródło: Bufs-a1c7p1.json :: dataList[id=FragmentOfHopeTwoSancho].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power +4 for every value\n- Apply Shield to self and all allies at Combat Start\n- Deal +20% damage\n- On Hit, deal 1 fixed damage as well
   PL: - Moc Starcia +4 za każdą wartość\n- Na początku walki nakłada Tarczę na siebie i wszystkich sojuszników\n- Zadaje obrażenia +20%\n- Przy trafieniu zadaje dodatkowo 1 obrażeń stałych

## Statusy i efekty bojowe — Bufs-a1c7p2
- plik gry: `Bufs-a1c7p2.json`

276. [Status [BloodyHand] — nazwa] 피로 물든 손
   źródło: Bufs-a1c7p2.json :: dataList[id=BloodyHand].name
   kontekst: identyfikator statusu w tekstach: `[BloodyHand]`
   limit: do 40 znaków
   EN: Bloodied Hand
   PL: Zakrwawiona Dłoń
277. [Status [BloodyHand] — opis] - 최댓값: 10\n- 기본값 : 0\n- 수치가 10이면, 자신의 스킬 적중시 파열 1 추가로 부여
   źródło: Bufs-a1c7p2.json :: dataList[id=BloodyHand].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Base Value: 0\n- At 10 Stack: inflict +1 additional Rupture On Hit with this unit's Skill
   PL: - Maks. wartości: 10\n- Wartość bazowa: 0\n- Przy 10 stosach Umiejętności tej jednostki nakładają przy trafieniu dodatkowe 1 Rozdarcia
278. [Status [BloomingThorns] — nazwa] 피어나는 가시
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns].name
   kontekst: identyfikator statusu w tekstach: `[BloomingThorns]`
   limit: do 40 znaków
   EN: Blooming Thorn
   PL: Kwitnące Ciernie
279. [Status [BloomingThorns] — opis] - 최댓값 : 10\n- 스킬로 피해를 받을 때, 공격자에게 스택의 절반만큼 출혈을 부여하고 1 감소 (올림하여 처리)
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- When taking damage from Skills, inflict Bleed equal to half of this effect's Stack against the Attacker (rounded up)
   PL: - Maks. wartości: 10\n- Gdy otrzymuje obrażenia od Umiejętności, nakłada na atakującego Krwawienie równe połowie stosów (zaokrąglone w górę)
280. [Status [BloomingThorns] — podsumowanie] 공격자에게 스택 절반만큼 출혈 부여
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns].summary
   limit: do 120 znaków
   EN: Inflict Bleed equal to Stack against the Attacker
   PL: Nakłada na atakującego Krwawienie równe stosom
281. [Status [BloomingThorns_2nd] — nazwa] 피를 엮은 가시
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns_2nd].name
   kontekst: identyfikator statusu w tekstach: `[BloomingThorns_2nd]`
   limit: do 40 znaków
   EN: Bloodwoven Thorn
   PL: Krwawo Utkany Cierń
282. [Status [BloomingThorns_2nd] — opis] - 피어나는 가시를 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 10\n- 턴 시작 시, 수치 3당 공격 레벨 증가 1 얻음 (최대 3)\n- 스킬로 피해를 받을 때, 공격자에게 스택만큼 출혈을 부여하고 1 감소 (올림하여 처리)\n- 스킬 효과로 적중 시 출혈, 출혈 횟수의 부여량 +1\n- 아군(자신 제외)에게 스킬 코인 효과로 공격 레벨 증가 또는 방어 레벨 증가를 부여할 때, 다음 턴에 합 위력 증가 1을 추가로 부여\n- 혈찬을 소모하는 스킬의 코인 위력 +1
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns_2nd].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Blooming Thorn gain this effect instead\n- Max Value: 10\n- Turn Start: gain 1 Offense Level Up per 3 Stack (max 3)\n- When taking damage from Skills, inflict Bleed equal to this effect's Stack against the Attacker, then lose 1 Stack (rounded up)\n- On Hit, inflict +1 more Bleed and Bleed Count with this unit's Skill effects\n- When applying Offense Level Up or Defense Level Up to another ally with Skill Coin effects, apply 1 Clash Power Up next turn as well\n- All Skills that consume Bloodfeast gain Coin Power +1
   PL: - Efekty zdobywające Kwitnący Cierń zdobywają zamiast tego ten efekt\n- Maks. wartości: 10\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 3 stosy (maks. 3)\n- Gdy otrzymuje obrażenia od Umiejętności, nakłada na atakującego Krwawienie równe stosom i traci 1 stos (zaokrąglone w górę)\n- Umiejętności tej jednostki nakładają przy trafieniu o 1 więcej Siły Krwawienia i Licznika Krwawienia\n- Gdy sojusznik (poza sobą) nakłada Monetą Umiejętności Wzrost Poziomu Ataku lub Wzrost Poziomu Obrony, nakłada dodatkowo 1 Wzrost Mocy Starcia na następną turę\n- Umiejętności zużywające Krwawą Ucztę zyskują Moc Monety +1
283. [Status [BloomingThorns_2nd] — podsumowanie] 공격자에게 스택만큼 출혈 부여\n출혈, 출혈 횟수 부여량 +1\n아군일 경우 합 위력 증가 1 부여\n혈찬 소모 스킬일 경우 코인 위력 +1
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns_2nd].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict Bleed on the Attacker equal to Stack\nInflict +1 more Bleed Potency & Count\nApply 1 Clash Power Up to allies\nIf the Skill consumes Bloodfeast, Coin Power +1
   PL: Nakłada na atakującego Krwawienie równe stosom\nNakłada o 1 więcej Siły Krwawienia i Licznika Krwawienia\nSojusznikom nakłada 1 Wzrost Mocy Starcia\nJeżeli Umiejętność zużywa Krwawą Ucztę, Moc Monety +1
284. [Status [BloomingThorns_3rd] — nazwa] 피로 빚은 가시
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns_3rd].name
   kontekst: identyfikator statusu w tekstach: `[BloomingThorns_3rd]`
   limit: do 40 znaków
   EN: Bloodmolded Thorn
   PL: Ulepiony z Krwi Cierń
285. [Status [BloomingThorns_3rd] — opis] - 피어나는 가시를 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 10\n- 턴 시작 시, 수치 2당 공격 레벨 증가 1 얻음 (최대 5)\n- 스킬로 피해를 받을 때, 공격자에게 스택만큼 출혈을 부여하고 1 감소 (올림하여 처리)\n- 스킬 효과로 적중 시 출혈, 출혈 횟수의 부여량 +2\n- 아군(자신 제외)에게 스킬 코인 효과로 공격 레벨 증가 또는 방어 레벨 증가를 부여할 때, 다음 턴에 합 위력 증가 2를 추가로 부여\n- 혈찬을 소모하는 스킬의 코인 위력 +2, 피해량 +50%\n- '퍼레이드는 영원히 반복될거야' 스킬 사용 시, 체력을 회복하는 대신 그 수치만큼 정신력을 회복
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns_3rd].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Blooming Thorn gain this effect instead\n- Max Value: 10\n- Turn Start: gain 1 Offense Level Up per 2 Stack (max 3)\n- When taking damage from Skills, inflict Bleed equal to this effect's Stack against the Attacker, then lose 1 Stack (rounded up)\n- On Hit, inflict +2 more Bleed and Bleed Count with this unit's Skill effects\n- When applying Offense Level Up or Defense Level Up to another ally with Skill Coin effects, apply 2 Clash Power Up next turn as well\n- All Skills that consume Bloodfeast gain Coin Power +1\n- When using 'The Parade Repeats for Eternity' Skill, instead of healing HP, heal the same value as SP
   PL: - Efekty zdobywające Kwitnący Cierń zdobywają zamiast tego ten efekt\n- Maks. wartości: 10\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 2 stosy (maks. 5)\n- Gdy otrzymuje obrażenia od Umiejętności, nakłada na atakującego Krwawienie równe stosom i traci 1 stos (zaokrąglone w górę)\n- Umiejętności tej jednostki nakładają przy trafieniu o 2 więcej Siły Krwawienia i Licznika Krwawienia\n- Gdy sojusznik (poza sobą) nakłada Monetą Umiejętności Wzrost Poziomu Ataku lub Wzrost Poziomu Obrony, nakłada dodatkowo 2 Wzrostu Mocy Starcia na następną turę\n- Umiejętności zużywające Krwawą Ucztę zyskują Moc Monety +2 i zadają +50% obrażeń\n- Przy użyciu Umiejętności „Parada powtarza się wiecznie” zamiast leczyć HP, leczy tę samą liczbę Poczytalności
286. [Status [BloomingThorns_3rd] — podsumowanie] 공격자에게 스택만큼 출혈 부여\n출혈, 출혈 횟수 부여량 +2\n아군일 경우 합 위력 증가 2 부여\n혈찬 소모 스킬일 경우 코인 위력 +2, 피해량 +50%
   źródło: Bufs-a1c7p2.json :: dataList[id=BloomingThorns_3rd].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict Bleed on the Attacker equal to Stack\nInflict +2 more Bleed Potency & Count\nApply 2 Clash Power Up to allies\nIf the Skill consumes Bloodfeast, Coin Power +2 and deal +50% damage
   PL: Nakłada na atakującego Krwawienie równe stosom\nNakłada o 2 więcej Siły Krwawienia i Licznika Krwawienia\nSojusznikom nakłada 2 Wzrostu Mocy Starcia\nJeżeli Umiejętność zużywa Krwawą Ucztę, Moc Monety +2 i +50% obrażeń
287. [Status [FestivalFever] — nazwa] 축제의 열기
   źródło: Bufs-a1c7p2.json :: dataList[id=FestivalFever].name
   kontekst: identyfikator statusu w tekstach: `[FestivalFever]`
   limit: do 40 znaków
   EN: Festive Fever
   PL: Gorączka Święta
288. [Status [FestivalFever] — opis] - 최댓값 : 10\n- 턴 시작 시, 수치 3당 공격 레벨 증가 1 얻음 (최대 3)\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p2.json :: dataList[id=FestivalFever].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Turn Start: gain 1 Offense Level Up per 3 Stack (max 3)\n- Used for special skills
   PL: - Maks.: 10\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 3 stosy (maks. 3)\n- Służy Umiejętnościom specjalnym
289. [Status [IncompleteParade] — nazwa] 불완전한 퍼레이드
   źródło: Bufs-a1c7p2.json :: dataList[id=IncompleteParade].name
   kontekst: identyfikator statusu w tekstach: `[IncompleteParade]`
   limit: do 40 znaków
   EN: Imperfect Parade
   PL: Niedoskonała Parada
290. [Status [IncompleteParade] — opis] - 최댓값 : 50\n- 피주머니 사망 시, 2 얻음\n- 혈귀 사망 시, 3 얻음\n- 턴 시작 시, 누적 소모한 수치 5당 취약 1 얻음\n- 누적 소모량 : {0}
   źródło: Bufs-a1c7p2.json :: dataList[id=IncompleteParade].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Value: 50\n- Gain 2 when a Bloodbag dies\n- Gain 3 when a Bloodfiend dies\n- Turn Start: gain 1 Fragile every time this unit consumes 5 cumulative Stack\n- Total Stack consumed: {0}
   PL: - Maks. wartości: 50\n- Zyskuje 2, gdy ginie Worek Krwi\n- Zyskuje 3, gdy ginie Krwiożerca\n- Na początku tury za każde skumulowane zużycie 5 wartości zyskuje 1 Wrażliwości\n- Skumulowane zużycie: {0}
291. [Status [FamineBloodDolci_LowMorale] — nazwa] 허무의 굴레
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodDolci_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[FamineBloodDolci_LowMorale]`
   limit: do 40 znaków
   EN: Bridle of Nihility
   PL: Ogłowie Nicości
292. [Status [FamineBloodDolci_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 위력 증가 1, 방어 레벨 감소 3을 얻음\n- 턴 종료 시, 정신력 5 피해
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodDolci_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: gain 1 Attack Power Up and 3 Defense Level Down\n- Turn End: take 5 SP damage
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Mocy Ataku i 3 Spadek Poziomu Obrony\n- Na koniec tury otrzymuje 5 obrażeń Poczytalności
293. [Status [FamineBloodDolci_LowMorale] — podsumowanie] 공격 위력 증가 1, 방어 레벨 감소 3 얻음
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodDolci_LowMorale].summary
   limit: do 120 znaków
   EN: Gain 1 Attack Power Up & 3 Defense Level Down
   PL: Zyskuje 1 Wzrost Mocy Ataku i 3 Spadek Poziomu Obrony
294. [Status [FamineBloodDolci_Panic] — nazwa] 허무의 굴레
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodDolci_Panic].name
   kontekst: identyfikator statusu w tekstach: `[FamineBloodDolci_Panic]`
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Status [FamineBloodDolci_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 위력 증가 2, 방어 레벨 감소 6을 얻음\n- 턴 종료 시, 정신력 10 회복
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodDolci_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: gain 2 Attack Power Up and 6 Defense Level Down\n- Turn End: heal 10 SP
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 6 Spadek Poziomu Obrony\n- Na koniec tury +10 Poczytalności
296. [Status [FamineBloodDolci_Panic] — podsumowanie] 공격 위력 증가 2, 방어 레벨 감소 6 얻음
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodDolci_Panic].summary
   limit: do 120 znaków
   EN: Gain 2 Attack Power Up & 6 Defense Level Down
   PL: Zyskuje 2 Wzrostu Mocy Ataku i 6 Spadek Poziomu Obrony
297. [Status [StarvingDolcineaOne] — nazwa] 노쇠
   źródło: Bufs-a1c7p2.json :: dataList[id=StarvingDolcineaOne].name
   kontekst: identyfikator statusu w tekstach: `[StarvingDolcineaOne]`
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Status [StarvingDolcineaOne] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 35 감소\n- 기본 방어 레벨 35 감소
   źródło: Bufs-a1c7p2.json :: dataList[id=StarvingDolcineaOne].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Starved for blood for a long, long time.\n- Lose 35 Base Offense Level\n- Lose 35 Base Defense Level
   PL: - Przez długi, długi czas nie mogła wypić krwi.\n- Podstawowy Poziom Ataku -35\n- Podstawowy Poziom Obrony -35
299. [Status [StarvingDolcineaServant] — nazwa] 노쇠
   źródło: Bufs-a1c7p2.json :: dataList[id=StarvingDolcineaServant].name
   kontekst: identyfikator statusu w tekstach: `[StarvingDolcineaServant]`
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Status [StarvingDolcineaServant] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: Bufs-a1c7p2.json :: dataList[id=StarvingDolcineaServant].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Status [ThornyFall_LowMorale] — nazwa] 가시
   źródło: Bufs-a1c7p2.json :: dataList[id=ThornyFall_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ThornyFall_LowMorale]`
   limit: do 40 znaków
   EN: Thorns
   PL: Ciernie
302. [Status [ThornyFall_LowMorale] — opis] 합 승리 시, 피해량 증가 1 얻음
   źródło: Bufs-a1c7p2.json :: dataList[id=ThornyFall_LowMorale].desc
   limit: do 120 znaków
   EN: Clash Win: gain 1 Damage Up
   PL: Po wygranym Starciu zyskuje 1 Wzrost Obrażeń
303. [Status [ThornyFall_LowMorale] — podsumowanie] 합 승리 시, 피해량 증가 1 얻음
   źródło: Bufs-a1c7p2.json :: dataList[id=ThornyFall_LowMorale].summary
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Status [ThornyFall_Panic] — nazwa] 가시
   źródło: Bufs-a1c7p2.json :: dataList[id=ThornyFall_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ThornyFall_Panic]`
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Status [ThornyFall_Panic] — opis] 합 승리 시, 피해량 증가 1 얻음\n턴 종료 시, 다음 턴에 합 위력 증가 2 얻음.
   źródło: Bufs-a1c7p2.json :: dataList[id=ThornyFall_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Win: gain 1 Damage Up\nTurn End: gain 2 Clash Power Up next turn
   PL: Po wygranym Starciu zyskuje 1 Wzrost Obrażeń\nNa koniec tury zyskuje 2 Wzrostu Mocy Starcia w następnej turze.
306. [Status [ThornyFall_Panic] — podsumowanie] 합 승리 시, 피해량 증가 1 얻음
   źródło: Bufs-a1c7p2.json :: dataList[id=ThornyFall_Panic].summary
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Status [HonorableDuel_Don] — nazwa] 명예로운 결투
   źródło: Bufs-a1c7p2.json :: dataList[id=HonorableDuel_Don].name
   kontekst: identyfikator statusu w tekstach: `[HonorableDuel_Don]`
   limit: do 40 znaków
   EN: Honorable Duel
   PL: Honorowy Pojedynek
308. [Status [HonorableDuel_Don] — opis] 기억 속 모험담\n능력치가 대폭 증가함
   źródło: Bufs-a1c7p2.json :: dataList[id=HonorableDuel_Don].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Reminisced Tale of Adventures\nBecome immensely powerful
   PL: Przygodowa opowieść z pamięci\nStatystyki rosną drastycznie
309. [Status [HonorableDuel_Knight] — nazwa] 명예로운 결투
   źródło: Bufs-a1c7p2.json :: dataList[id=HonorableDuel_Knight].name
   kontekst: identyfikator statusu w tekstach: `[HonorableDuel_Knight]`
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Status [HonorableDuel_Knight] — opis] 기억 속 모험담
   źródło: Bufs-a1c7p2.json :: dataList[id=HonorableDuel_Knight].desc
   limit: do 120 znaków
   EN: Reminisced Tales of Adventure
   PL: Przygodowe opowieści z pamięci
311. [Status [StarvingPriestOne] — nazwa] 노쇠
   źródło: Bufs-a1c7p2.json :: dataList[id=StarvingPriestOne].name
   kontekst: identyfikator statusu w tekstach: `[StarvingPriestOne]`
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Status [StarvingPriestOne] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: Bufs-a1c7p2.json :: dataList[id=StarvingPriestOne].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Status [FamineBloodPriestServant_LowMorale] — nazwa] 굶주림
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodPriestServant_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[FamineBloodPriestServant_LowMorale]`
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Status [FamineBloodPriestServant_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 합 위력 증가 1, 방어 레벨 감소 3을 얻음\n- 턴 종료 시, 정신력 5 피해
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodPriestServant_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: gain 1 Clash Power Up and 3 Defense Level Down\n- Turn End: take 5 SP damage
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Mocy Starcia i 3 Spadek Poziomu Obrony\n- Na koniec tury 5 obrażeń Poczytalności
315. [Status [FamineBloodPriestServant_Panic] — nazwa] 굶주림
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodPriestServant_Panic].name
   kontekst: identyfikator statusu w tekstach: `[FamineBloodPriestServant_Panic]`
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Status [FamineBloodPriestServant_Panic] — opis] - 패닉\n- 턴 시작 시, 합 위력 증가 2, 방어 레벨 감소 6을 얻음\n- 턴 종료 시, 정신력 10 회복
   źródło: Bufs-a1c7p2.json :: dataList[id=FamineBloodPriestServant_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: gain 2 Clash Power Up and 6 Defense Level Down\n- Turn End: heal 10 SP
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Starcia i 6 Spadek Poziomu Obrony\n- Na koniec tury +10 Poczytalności
317. [Status [UnstoppableFunny] — nazwa] 멈출 수 없는 환희
   źródło: Bufs-a1c7p2.json :: dataList[id=UnstoppableFunny].name
   kontekst: identyfikator statusu w tekstach: `[UnstoppableFunny]`
   limit: do 40 znaków
   EN: Unstoppable Bliss
   PL: Niepowstrzymana Rozkosz
318. [Status [UnstoppableFunny] — opis] 사망 시\n- 가장 수량이 적은 E.G.O 자원 3종 각각 1씩 증가\n- 적 하나의 출혈 횟수 3 증가 (자신을 처치한 대상을 우선으로 함)\n- 축제의 열기가 5 이상인 모든 아군이 다음 턴에 신속 1 얻음\n- 축제의 열기가 없는 모든 아군이 다음 턴에 합 위력 증가 1 얻음
   źródło: Bufs-a1c7p2.json :: dataList[id=UnstoppableFunny].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Death:\n- Gain 1 E.G.O resource for 3 least-owned E.G.O resources\n- Inflict +3 Bleed Count against an enemy (prioritizes the unit that killed this unit)\n- All allies at 5+ Festive Fever gain 1 Haste next turn\n- All allies without Festive Fever gain 1 Clash Power Up
   PL: Po śmierci\n- Zyskuje po 1 Zasobie E.G.O dla 3 najmniej posiadanych Zasobów E.G.O\n- Nakłada +3 Licznika Krwawienia na wroga (priorytet: jednostka, która ją zabiła)\n- Wszyscy sojusznicy z 5 lub więcej Gorączki Świętej zyskują w następnej turze 1 Pośpiech\n- Wszyscy sojusznicy bez Gorączki Świętej zyskują 1 Wzrost Mocy Starcia
319. [Status [UnstoppableFunny] — podsumowanie] E.G.O 자원 3종 하나씩 획득\n출혈 횟수 3 증가
   źródło: Bufs-a1c7p2.json :: dataList[id=UnstoppableFunny].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 1 of each 3 E.G.O resources\nInflict +3 Bleed Count
   PL: Zyskuje po 1 z 3 Zasobów E.G.O\nNakłada +3 Licznika Krwawienia

## Statusy i efekty bojowe — Bufs-a1c7p3
- plik gry: `Bufs-a1c7p3.json`

320. [Status [BloodyHand_2nd] — nazwa] 피로 물든 손 II
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodyHand_2nd].name
   kontekst: identyfikator statusu w tekstach: `[BloodyHand_2nd]`
   limit: do 40 znaków
   EN: Bloodied Hand II
   PL: Zakrwawiona Dłoń II
321. [Status [BloodyHand_2nd] — opis] - 피로 물든 손을 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 20\n- 기본값 : 10\n- 수치 6당 공격 레벨 1 증가
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodyHand_2nd].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Bloodied Hand gain this effect instead\n- Max Value: 20\n- Base Value: 10\n- Gain 1 Offense Level for every 6 Stack
   PL: - Efekty zdobywające Krwawą Dłoń zdobywają zamiast tego ten efekt\n- Maks. wartości: 20\n- Wartość bazowa: 10\n- Zyskuje 1 Poziomu Ataku za każde 6 stosów
322. [Status [BloodyHand_3rd] — nazwa] 피로 물든 손 III
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodyHand_3rd].name
   kontekst: identyfikator statusu w tekstach: `[BloodyHand_3rd]`
   limit: do 40 znaków
   EN: Bloodied Hand III
   PL: Zakrwawiona Dłoń III
323. [Status [BloodyHand_3rd] — opis] - 피로 물든 손을 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 30\n- 기본값 : 20\n- 공격 위력 1 증가\n- 수치가 30이면, 자신의 스킬 적중시 파열 2, 파열 횟수 1 추가로 부여\n- 수치가 30이면, 자신의 스킬 적중시 자신과 공격 대상에게 서로 출혈 3 부여
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodyHand_3rd].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Bloodied Hand gain this effect instead\n- Max Value: 30\n- Base Value: 20\n- Gain 1 Attack Power\n- At 30 Stack: On Hit with this unit's Skill, inflict additional 2 Rupture and +1 Rupture Count\n- At 30 Stack: On Hit with this unit's Skill, inflict 3 Bleed both on self and against the target
   PL: - Efekty zdobywające Krwawą Dłoń zdobywają zamiast tego ten efekt\n- Maks. wartości: 30\n- Wartość bazowa: 20\n- Zyskuje 1 Mocy Ataku\n- Przy 30 stosach Umiejętności tej jednostki nakładają przy trafieniu dodatkowe 2 Rozdarcia i +1 Licznika Rozdarcia\n- Przy 30 stosach Umiejętności tej jednostki nakładają przy trafieniu po 3 Siły Krwawienia na sobie i na celu
324. [Status [WornHeart] — nazwa] 닳아버린 마음
   źródło: Bufs-a1c7p3.json :: dataList[id=WornHeart].name
   kontekst: identyfikator statusu w tekstach: `[WornHeart]`
   limit: do 40 znaków
   EN: Ailing Heart
   PL: Zmęczone Serce
325. [Status [WornHeart] — opis] - 최대 10 스택\n- 처음부터 3을 가지고 전투 시작.\n- 턴 시작시, 수치 1당 방어 레벨 감소 1 얻음\n- 턴 시작시, 수치 2당 공격 레벨 증가 1 얻음\n- 턴 시작시, 수치가 10이면 취약 3 얻고 정신력 5 감소\n- 수치가 10이면, 자신의 공격 적중시 피해량의 40%만큼 부위와 본체 체력 회복하고 피로 물든 손을 2 얻음
   źródło: Bufs-a1c7p3.json :: dataList[id=WornHeart].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Enters Encounter with 3 Stack\n- Turn Start: gain 1 Defense Level Down for every Stack\n- Turn Start: gain 1 Offense Level Up for every 2 Stack\n- Turn Start: at 10 Stack, gain 3 Fragile and lose 5 SP\n- At 10 Stack: On Hit, heal 40% of the damage dealt to this unit's Part and Core, and gain 2 Bloodied Hand
   PL: - Maks. 10 stosów\n- Rozpoczyna walkę z 3 stosami\n- Na początku tury zyskuje 1 Spadek Poziomu Obrony za każdy stos\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 2 stosy\n- Na początku tury przy 10 stosach zyskuje 3 Wrażliwości i traci 5 Poczytalności\n- Przy 10 stosach, gdy jego atak trafia, leczy 40% zadanych obrażeń części i korpusu oraz zyskuje 2 Krwawej Dłoni
326. [Status [StarvingPriestTwo] — nazwa] 노쇠
   źródło: Bufs-a1c7p3.json :: dataList[id=StarvingPriestTwo].name
   kontekst: identyfikator statusu w tekstach: `[StarvingPriestTwo]`
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Status [StarvingPriestTwo] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 25 감소\n- 기본 방어 레벨 25 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=StarvingPriestTwo].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Status [Guilt_LowMorale] — nazwa] 죄책감
   źródło: Bufs-a1c7p3.json :: dataList[id=Guilt_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Guilt_LowMorale]`
   limit: do 40 znaków
   EN: Guilt
   PL: Poczucie Winy
329. [Status [Guilt_LowMorale] — opis] 턴 종료 시 다음 턴에 취약, 정신력 회복 효율 감소 1 얻음
   źródło: Bufs-a1c7p3.json :: dataList[id=Guilt_LowMorale].desc
   limit: do 120 znaków
   EN: Turn End: gain 1 Fragility and SP Heal Efficiency Down
   PL: Na koniec tury w następnej turze zyskuje 1 Wrażliwości i Spadek Wydajności Leczenia Poczytalności
330. [Status [Guilt_Panic] — nazwa] 죄책감
   źródło: Bufs-a1c7p3.json :: dataList[id=Guilt_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Guilt_Panic]`
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Status [Guilt_Panic] — opis] 턴 종료 시 다음 턴에 취약, 정신력 회복 효율 감소 2 얻음
   źródło: Bufs-a1c7p3.json :: dataList[id=Guilt_Panic].desc
   limit: do 120 znaków
   EN: Turn End: gain 2 Fragility and 1 SP Heal Efficiency Down
   PL: Na koniec tury w następnej turze zyskuje 2 Wrażliwości i Spadek Wydajności Leczenia Poczytalności
332. [Status [MentalIncreaseDown] — nazwa] 정신력 회복 효율 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=MentalIncreaseDown].name
   kontekst: identyfikator statusu w tekstach: `[MentalIncreaseDown]`
   limit: do 40 znaków
   EN: SP Heal Efficiency Down
   PL: Słabsze Leczenie Poczytalności
333. [Status [MentalIncreaseDown] — opis] 정신력 회복 효율이 스택만큼 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=MentalIncreaseDown].desc
   limit: do 120 znaków
   EN: SP Heal Efficiency decreases by the effect's Stack
   PL: Efektywność leczenia Poczytalności maleje o liczbę stosów
334. [Status [AffectionTeddy] — nazwa] 애착
   źródło: Bufs-a1c7p3.json :: dataList[id=AffectionTeddy].name
   kontekst: identyfikator statusu w tekstach: `[AffectionTeddy]`
   limit: do 40 znaków
   EN: Attachment
   PL: Przywiązanie
335. [Status [AffectionTeddy] — opis] - 최댓값 : 9\n- 공격자가 이 효과를 보유한 대상을 공격할 때, 수치만큼 합 위력 증가\n- 턴 종료 시, 1 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=AffectionTeddy].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 9\n- When the Attacker attacks the target with this effect, the Attacker gains Clash Power equal to the Stack\n- Turn End: reduce by 1
   PL: - Maks. wartości: 9\n- Gdy atakujący atakuje cel z tym efektem, zyskuje Moc Starcia równą liczbie stosów\n- Na koniec tury maleje o 1
336. [Status [FaintMemory] — nazwa] 아련한 기억
   źródło: Bufs-a1c7p3.json :: dataList[id=FaintMemory].name
   kontekst: identyfikator statusu w tekstach: `[FaintMemory]`
   limit: do 40 znaków
   EN: Faint Memories
   PL: Zamglone Wspomnienia
337. [Status [FaintMemory] — opis] - 기본값 : 10\n- 턴 시작 시, 수치만큼 방어 레벨 증가를 얻음\n- 합 패배 시, 1 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=FaintMemory].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Value: 10\n- Turn Start: gain Defense Level Up equal to the Stack\n- Clash Lose: reduce by 1
   PL: - Wartość bazowa: 10\n- Na początku tury zyskuje Wzrost Poziomu Obrony równy liczbie stosów\n- Po przegranej w Starciu maleje o 1
338. [Status [CursePackage] — nazwa] 저주 꾸러미
   źródło: Bufs-a1c7p3.json :: dataList[id=CursePackage].name
   kontekst: identyfikator statusu w tekstach: `[CursePackage]`
   limit: do 40 znaków
   EN: Box of Curses
   PL: Pakunek Klątw
339. [Status [CursePackage] — opis] - 최댓값 : 1\n- 턴 종료시, 공격 위력 감소 1, 수비 위력 감소 1, 공격 레벨 감소 2, 방어 레벨 감소 2를 얻고 수치 1 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=CursePackage].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Turn End: gain 1 Attack Power Down, 1 Defense Power Down, 2 Offense Level Down, 2 Defense Level Down, and reduce the Stack of this effect by 1
   PL: - Maks. wartości: 1\n- Na koniec tury zyskuje 1 Spadek Mocy Ataku, 1 Spadek Mocy Obrony, 2 Spadku Poziomu Ataku i 2 Spadek Poziomu Obrony, a wartość maleje o 1
340. [Status [TinyCarmilla] — nazwa] 작은 카르밀라
   źródło: Bufs-a1c7p3.json :: dataList[id=TinyCarmilla].name
   kontekst: identyfikator statusu w tekstach: `[TinyCarmilla]`
   limit: do 40 znaków
   EN: Little Carmilla
   PL: Mała Carmilla
341. [Status [TinyCarmilla] — opis] - 최댓값 3\n- 작은 카르밀라를 얻을 때마다 출혈을 2 얻음\n- 턴 종료시, 출혈 횟수 2 증가\n- 턴 종료시, 3이면 대상의 최대 체력 15%만큼 고정 피해를 입히고 모든 적들의 최대 체력의 5% 회복 이후 제거됨
   źródło: Bufs-a1c7p3.json :: dataList[id=TinyCarmilla].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 2 Bleed every time this unit gains Little Carmilla\n- Turn End: gain +2 Bleed Count\n- Turn End: at 3 Stack, take fixed damage equal to 15% of this unit's max HP, heal HP equal to 5% of each enemy's max HP, then this effect expires
   PL: - Maks. 3 stosów\n- Za każde zdobycie Małej Carmilli zyskuje 2 Krwawienia\n- Na koniec tury zyskuje +2 Licznika Krwawienia\n- Na koniec tury przy 3 stosach otrzymuje obrażenia stałe równe 15% Maks. HP i leczy HP równe 5% Maks. HP wszystkich wrogów, po czym efekt znika
342. [Status [OneDropNutrition] — nazwa] 한 방울의 양분
   źródło: Bufs-a1c7p3.json :: dataList[id=OneDropNutrition].name
   kontekst: identyfikator statusu w tekstach: `[OneDropNutrition]`
   limit: do 40 znaków
   EN: A Drop of Nourishment
   PL: Kropla Pożywienia
343. [Status [OneDropNutrition] — opis] - 최댓값: 10\n- 자신의 공격으로 체력 회복할 때, 회복한 최대 체력의 비율 10%당, 1 증가\n- 회복한 체력 비율: {0}
   źródło: Bufs-a1c7p3.json :: dataList[id=OneDropNutrition].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Stack: 10\n- Gain 1 Stack every time this unit heals 10% of its max HP with its HP-healing Attacks\n- HP healed: {0}%
   PL: - Maks.: 10\n- Rośnie o 1 za każde odzyskanie 10% Maks. HP własnym atakiem leczącym HP\n- Odzyskane HP: {0}%
344. [Status [ThornNoose] — nazwa] 가시 올가미
   źródło: Bufs-a1c7p3.json :: dataList[id=ThornNoose].name
   kontekst: identyfikator statusu w tekstach: `[ThornNoose]`
   limit: do 40 znaków
   EN: Barbed Lasso
   PL: Kolczaste Lasso
345. [Status [ThornNoose] — opis] - 최댓값: 3\n- 턴 종료 시 파열 2, 파열 횟수 2 증가\n- 턴 종료 시 수치가 1 이상이면, 다음 턴에 속도가 1로 고정됨.\n- 턴 종료 시 수치가 2가 되면, 20의 탐식 피해를 입음.\n- 턴 종료 시 수치가 3이 되면, 다음 턴에 강제 흐트러짐 상태가 됨.  버프 제거 및 연결된 가시 올가미 제거됨.\n- 턴 시작 시 1 증가
   źródło: Bufs-a1c7p3.json :: dataList[id=ThornNoose].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: gain 2 Rupture and +2 Rupture Count\n- Turn End: at 1+ Stack, fix this unit's Speed to 1.\n- Turn End: at 2 Stack, take 20 Gluttony damage.\n- Turn End: at 3 Stack, become forcibly Staggered next turn. This effect and the connected Barbed Lasso both expire.\n- Gain 1 at Turn Start
   PL: - Maks. 3 stosów\n- Na koniec tury zyskuje 2 Siły Rozdarcia i 2 Licznika Rozdarcia\n- Na koniec tury przy 1+ stosach Szybkość w następnej turze wynosi 1.\n- Na koniec tury przy 2 stosach otrzymuje 20 obrażeń Obżarstwa.\n- Na koniec tury przy 3 stosach przechodzi w wymuszone Oszołomienie w następnej turze; efekt i połączone Kolczaste Lasso znikają.\n- Na początku tury rośnie o 1
346. [Status [SwirlingBlood] — nazwa] 일렁임【혈귀】
   źródło: Bufs-a1c7p3.json :: dataList[id=SwirlingBlood].name
   kontekst: identyfikator statusu w tekstach: `[SwirlingBlood]`
   limit: do 40 znaków
   EN: Shimmering【Bloodfiend】
   PL: Drgający【Krwiopijca】
347. [Status [SwirlingBlood] — opis] - 이 버프가 있을 때, 피해를 입으면 대상의 공격 종료 시 출혈 5를 부여함.\n- 이 버프가 있는 동안 보호막 체력은 턴 종료 시 사라지지 않음\n- 조건 만족 시, 소멸 및 패턴 변경전까지 취약을 3 얻음
   źródło: Bufs-a1c7p3.json :: dataList[id=SwirlingBlood].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - While this effect is active: when this unit takes damage, the Attacker gains 5 Bleed at Attack End.\n- While this effect is active: the Shield HP does not expire at Turn End\n- When conditions are met, gain 3 Fragile until this effect expires and this unit gains a new pattern
   PL: - Dopóki ten efekt jest aktywny: gdy otrzymuje obrażenia, atakujący zyskuje 5 Krwawienia po zakończeniu ataku.\n- Dopóki ten efekt jest aktywny: HP Tarczy nie znika na koniec tury\n- Po spełnieniu warunków zyskuje 3 Wrażliwości aż do zniknięcia efektu i zmiany wzorca
348. [Status [BloodArmor] — nazwa] 경혈
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodArmor].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmor]`
   limit: do 40 znaków
   EN: Hardblood
   PL: Skondensowana Krew
349. [Status [BloodArmor] — opis] - 최댓값: 10\n- 경혈 1단계\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodArmor].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Hardblood\n- Used for special Skills
   PL: - Maks. wartości: 10\n- Twarda Krew 1. stopnia\n- Służy specjalnym Umiejętnościom
350. [Status [BloodArmor_2nd] — nazwa] 경혈 II
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodArmor_2nd].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmor_2nd]`
   limit: do 40 znaków
   EN: Hardblood II
   PL: Skondensowana Krew II
351. [Status [BloodArmor_2nd] — opis] - 최댓값: 20\n- 경혈 2단계\n- 턴 시작시 수치 6당 공격 레벨 1, 방어 레벨 1 증가\n- 속도 최솟값, 최댓값 1 증가\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodArmor_2nd].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Hardblood\n- Turn Start: gain 1 Offense Level and Defense Level for every 6 Stack\n- Raise Min & Max Speed values by 1\n- Used for special Skills
   PL: - Maks. wartości: 20\n- Twarda Krew 2. stopnia\n- Na początku tury zyskuje 1 Poziomu Ataku i 1 Poziomu Obrony za każde 6 wartości\n- Podnosi Min. i Maks. Szybkość o 1\n- Służy specjalnym Umiejętnościom
352. [Status [BloodArmor_3rd] — nazwa] 경혈 III
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodArmor_3rd].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmor_3rd]`
   limit: do 40 znaków
   EN: Hardblood III
   PL: Skondensowana Krew III
353. [Status [BloodArmor_3rd] — opis] - 최댓값: 30\n- 경혈 3단계\n- 턴 시작시 수치 6당 공격 레벨 2, 방어 레벨 2 증가\n- 속도 최솟값, 최댓값 2 증가\n- 특수 스킬에 사용됨
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodArmor_3rd].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Hardblood\n- Turn Start: gain 2 Offense Level and Defense Level for every 6 Stack\n- Raise Min & Max Speed values by 2\n- Used for special Skills
   PL: - Maks. wartości: 30\n- Twarda Krew 3. stopnia\n- Na początku tury zyskuje 2 Poziomu Ataku i 2 Poziomu Obrony za każde 6 wartości\n- Podnosi Min. i Maks. Szybkość o 2\n- Służy specjalnym Umiejętnościom
354. [Status [Dreamy] — nazwa] 꿈결속 망설임
   źródło: Bufs-a1c7p3.json :: dataList[id=Dreamy].name
   kontekst: identyfikator statusu w tekstach: `[Dreamy]`
   limit: do 40 znaków
   EN: Dreamy Hesitation
   PL: Senne Wahanie
355. [Status [Dreamy] — opis] - 기본 공격 레벨 35 감소\n- 기본 방어 레벨 35 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=Dreamy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 35 Base Offense Level\n- Lose 35 Base Defense Level
   PL: - Podstawowy Poziom Ataku -35\n- Podstawowy Poziom Obrony -35
356. [Status [BloodringUp_LowMorale] — nazwa] 피올림
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodringUp_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BloodringUp_LowMorale]`
   limit: do 40 znaków
   EN: Resanguination
   PL: Nakrwawienie
357. [Status [BloodringUp_LowMorale] — opis] - 사기 저하\n출혈이 없는 대상이면, 합 위력 -1, 적중시 대상의 출혈 위력만큼 체력 회복
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodringUp_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nIf the target does not have Bleed, Clash Power -1; On Hit, heal HP equal to Bleed Potency on the target
   PL: - Niskie Morale\nJeśli cel nie posiada Krwawienia, Moc Starcia -1; przy trafieniu odzyskuje HP równe Mocy Krwawienia celu
358. [Status [BloodringUp_Panic] — nazwa] 피올림
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodringUp_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BloodringUp_Panic]`
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Status [BloodringUp_Panic] — opis] - 패닉\n출혈이 있는 대상이면, 합 위력 +2, 출혈이 없는 대상이면, 합 위력 -2, 적중시 대상의 출혈 위력만큼 체력 회복
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodringUp_Panic].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nIf the target has Bleed, Clash Power +2; if the target does not have Bleed, Clash Power -2; On Hit, heal HP equal to Bleed Potency on the target
   PL: - Panika\nJeśli cel posiada Krwawienie, Moc Starcia +2; jeśli cel nie posiada Krwawienia, Moc Starcia -2; przy trafieniu odzyskuje HP równe Mocy Krwawienia celu
360. [Status [BloodDinner_Common_Accumulation] — nazwa] 공용 누적 소모 혈찬
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodDinner_Common_Accumulation].name
   kontekst: identyfikator statusu w tekstach: `[BloodDinner_Common_Accumulation]`
   limit: do 40 znaków
   EN: Bloodfeast Consumed (shared)
   PL: Krwawa Uczta (wspólna)
361. [Status [BloodDinner_Common_Accumulation] — opis] 이번 전투 동안 누적 소모한 혈찬
   źródło: Bufs-a1c7p3.json :: dataList[id=BloodDinner_Common_Accumulation].desc
   limit: do 120 znaków
   EN: Total Bloodfeast consumed in this Encounter
   PL: Łączna liczba Krwawej Uczty skonsumowanej w tej walce
362. [Status [ThirstyRose] — nazwa] 목마른 장미
   źródło: Bufs-a1c7p3.json :: dataList[id=ThirstyRose].name
   kontekst: identyfikator statusu w tekstach: `[ThirstyRose]`
   limit: do 40 znaków
   EN: Polydipsic Rose
   PL: Spragniona Róża
363. [Status [ThirstyRose] — opis] - 최댓값: 5\n- 턴 종료 시 자신의 출혈 위력이 10이상일 때, 자신의 최대 체력 1%만큼 색욕 피해를 입음. (최대 30)\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=ThirstyRose].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 5\n- Turn End: at 10+ Bleed Potency, take Lust damage equal to 1% of this unit's max HP. (max 30)\n- Turn End: reduced by 1
   PL: - Maks. wartości: 5\n- Na koniec tury, jeżeli Siła Krwawienia wynosi 10 lub więcej, otrzymuje obrażenia Żądzy równe 1% Maks. HP. (maks. 30)\n- Na koniec tury maleje o 1
364. [Status [RoseWedge] — nazwa] 장미 쐐기
   źródło: Bufs-a1c7p3.json :: dataList[id=RoseWedge].name
   kontekst: identyfikator statusu w tekstach: `[RoseWedge]`
   limit: do 40 znaków
   EN: Rose Wedge
   PL: Klin Róży
365. [Status [RoseWedge] — opis] - 위력 최댓값 : 10\n- 횟수 최댓값 : 4\n- 출혈 피해를 10 받을 때마다, 위력 1 증가.\n- 피격시 자신에게 스킬 효과로 출혈, 특수 출혈이 부여될 때마다 출혈 2를 얻고, 공격자에게 출혈 1을 부여함. (턴 당 최대 5회)\n· 이 효과의 위력이 10이면, 위 효과 발동 시 추가로 출혈 횟수가 1 증가함.\n- 턴 종료 시 횟수 1 감소\n- 전투 종료 시 위력 10 또는 횟수 1이면, 버프가 소멸하고 (위력 x 10)만큼 색욕 피해를 받음.\n- 부여 대상이 사망하거나 버프 소멸 시 (위력 x 10)만큼 혈찬 증가, 부여 대상의 모든 아군 유닛에게 (위력 x 2)만큼 색욕 피해를 입힘 (최소 1)
   źródło: Bufs-a1c7p3.json :: dataList[id=RoseWedge].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 10\n- Max Count: 4\n- Gain 1 Potency every time this unit takes 10 Bleed damage\n- When gaining Bleed or 'Unique Bleed' from getting hit, gain 2 Bleed and inflict 1 Bleed against the Attacker. (5 times per turn)\n· At 10 Potency, gain +1 Bleed Count as well when triggering the above effect.\n- Turn End: lose 1 Count\n- Combat End: at 10 Potency or 1 Count, this effect expires, and this unit takes (Potency x 10) Lust damage.\n- If the unit inflicted with this effect dies, or when this effect expires: increase Bloodfeast by (Potency x 10), and deal (Potency x 2) Lust damage against all of its allies (min 1)
   PL: - Maks. Siły: 10\n- Maks. Licznika: 4\n- Zyskuje 1 Siły za każde otrzymanie 10 obrażeń Krwawienia\n- Przy otrzymaniu od trafienia Krwawienia lub Specjalnego Krwawienia z efektu Umiejętności zyskuje 2 Krwawienia i nakłada 1 Krwawienie na atakującego. (maks. 5 razy na turę)\n· Przy 10 Siły, podczas wywołania powyższego efektu, zyskuje dodatkowo +1 Licznika Krwawienia.\n- Na koniec tury traci 1 Licznika\n- Po zakończeniu walki, przy 10 Siły lub 1 Liczniku, efekt znika, a jednostka otrzymuje (Siła x 10) obrażeń Żądzy.\n- Przy śmierci jednostki z tym efektem lub zniknięciu efektu: Krwawa Uczta rośnie o (Siła x 10), a wszyscy sojusznicy jednostki otrzymują (Siła x 2) obrażeń Żądzy (min. 1)
366. [Status [FerrisWheel] — nazwa] 돌고도는 관람차
   źródło: Bufs-a1c7p3.json :: dataList[id=FerrisWheel].name
   kontekst: identyfikator statusu w tekstach: `[FerrisWheel]`
   limit: do 40 znaków
   EN: The Endless Wheel
   PL: Wieczny Diabelski Młyn
367. [Status [FerrisWheel] — opis] 곤돌라가 처치될 때마다 1 감소.\n이 수치가 0이고, 다음 턴에 생성될 유닛이 없으면 다음 페이즈로 넘어감.
   źródło: Bufs-a1c7p3.json :: dataList[id=FerrisWheel].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduced by 1 every time a Gondola is defeated.\nIf this value is at 0, and if there are no units to be spawned next turn, move on to the next phase.
   PL: Maleje o 1 za każdą pokonaną Gondolę.\nJeżeli wartość wynosi 0, a w następnej turze nie pojawi się żadna jednostka, następuje przejście do następnej fazy.
368. [Status [StarvingDonqui] — nazwa] 굶주림과 노쇠
   źródło: Bufs-a1c7p3.json :: dataList[id=StarvingDonqui].name
   kontekst: identyfikator statusu w tekstach: `[StarvingDonqui]`
   limit: do 40 znaków
   EN: Starved and Withered
   PL: Wygłodniały i Zwiędnięty
369. [Status [StarvingDonqui] — opis] - 기본 공격 레벨 10 감소\n- 기본 방어 레벨 10 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=StarvingDonqui].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 10 Base Offense Level\n- Lose 10 Base Defense Level
   PL: - Podstawowy Poziom Ataku -10\n- Podstawowy Poziom Obrony -10
370. [Status [RegainedStrength] — nazwa] 다시 도는 피의 충동
   źródło: Bufs-a1c7p3.json :: dataList[id=RegainedStrength].name
   kontekst: identyfikator statusu w tekstach: `[RegainedStrength]`
   limit: do 40 znaków
   EN: Returning Bloodlust
   PL: Powracający Popęd Krwi
371. [Status [RegainedStrength] — opis] - 최댓값: 10\n- 다시 도는 피의 충동 1단계
   źródło: Bufs-a1c7p3.json :: dataList[id=RegainedStrength].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Returning Bloodlust
   PL: - Maks. wartości: 10\n- Powracający Popęd Krwi 1. stopnia
372. [Status [RegainedStrength_2nd] — nazwa] 다시 도는 피의 충동 II
   źródło: Bufs-a1c7p3.json :: dataList[id=RegainedStrength_2nd].name
   kontekst: identyfikator statusu w tekstach: `[RegainedStrength_2nd]`
   limit: do 40 znaków
   EN: Returning Bloodlust II
   PL: Powracający Popęd Krwi II
373. [Status [RegainedStrength_2nd] — opis] - 최대 20\n- 다시 도는 피의 충동 2단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 다시 도는 피의 충동을 소모하는 스킬의 합 위력 +1, 해당 스킬에서 부여하는 출혈, 파열의 위력과 횟수 +1
   źródło: Bufs-a1c7p3.json :: dataList[id=RegainedStrength_2nd].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Returning Bloodlust\n- Turn Start: gain 1 Offense Level up and 1 Defense Level Up for every 5 Value\n- Clash Power +1 to Skills that consume Returning Bloodlust; inflict +1 more of Potency and Count for Bleed and Rupture inflicted by the said Skill
   PL: - Maks. 20\n- Powracający Popęd Krwi 2. stopnia\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 5 wartości\n- Umiejętności zużywające Powracający Popęd Krwi zyskują Moc Starcia +1 i nakładają o 1 więcej Siły i Licznika Krwawienia oraz Rozdarcia
374. [Status [RegainedStrength_3rd] — nazwa] 다시 도는 피의 충동 III
   źródło: Bufs-a1c7p3.json :: dataList[id=RegainedStrength_3rd].name
   kontekst: identyfikator statusu w tekstach: `[RegainedStrength_3rd]`
   limit: do 40 znaków
   EN: Returning Bloodlust III
   PL: Powracający Popęd Krwi III
375. [Status [RegainedStrength_3rd] — opis] - 최대 30\n- 다시 도는 피의 충동 3단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 2, 방어 레벨 증가 1 얻음\n- 다시 도는 피의 충동을 소모하는 스킬의 코인 위력 +1, 해당 스킬에서 부여하는 출혈, 파열의 위력과 횟수 +1
   źródło: Bufs-a1c7p3.json :: dataList[id=RegainedStrength_3rd].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Returning Bloodlust\n- Turn Start: gain 2 Offense Level up and 1 Defense Level Up for every 5 Value\n- Coin Power +1 to Skills that consume Returning Bloodlust; inflict +1 more of Potency and Count for Bleed and Rupture inflicted by the said Skill
   PL: - Maks. 30\n- Powracający Popęd Krwi 3. stopnia\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 5 wartości\n- Umiejętności zużywające Powracający Popęd Krwi zyskują Moc Monety +1 i nakładają o 1 więcej Siły i Licznika Krwawienia oraz Rozdarcia
376. [Status [WeightOfResponsibility_LowMorale] — nazwa] 내 꿈을 버리고 이제는...
   źródło: Bufs-a1c7p3.json :: dataList[id=WeightOfResponsibility_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[WeightOfResponsibility_LowMorale]`
   limit: do 40 znaków
   EN: Time to abandon my dream...
   PL: Pora porzucić mój sen...
377. [Status [WeightOfResponsibility_LowMorale] — opis] - 사기 저하\n- 공격 위력 증가 2, 취약  1 얻음, 속도 최댓값 2 증가\n- 체력 회복량 30% 증가\n- 턴 종료 시 턴 시작 시보다 다시 도는 피의 충동의 수치가 낮으면 다음 턴에 공격 레벨 증가 2, 방어 레벨 감소 2 얻음.
   źródło: Bufs-a1c7p3.json :: dataList[id=WeightOfResponsibility_LowMorale].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 2 Attack Power Up and 1 Fragile; raise max Speed value by 2\n- Heal +30% more HP when healing\n- Turn End: if the current Returning Bloodlust is lower than its value at Turn Start, gain 2 Offense Level Up and 2 Defense Level Down
   PL: - Niskie Morale\n- Zyskuje 2 Wzrostu Mocy Ataku i 1 Wrażliwości; Maks. Szybkość +2\n- Leczenie HP +30%\n- Na koniec tury, jeżeli wartość Powracającego Popędu Krwi jest niższa niż na początku tury, w następnej turze zyskuje 2 Wzrostu Poziomu Ataku i 2 Spadek Poziomu Obrony.
378. [Status [WeightOfResponsibility_Panic] — nazwa] 어버이로써 가족을 위해....
   źródło: Bufs-a1c7p3.json :: dataList[id=WeightOfResponsibility_Panic].name
   kontekst: identyfikator statusu w tekstach: `[WeightOfResponsibility_Panic]`
   limit: do 60 znaków
   EN: ... for my Family, as their Father...
   PL: ... Dla mojej Rodziny, jako jej Ojciec...
379. [Status [WeightOfResponsibility_Panic] — opis] - 패닉\n- 공격 위력 증가 2, 신속 2, 취약 2 얻음\n- 체력 회복량 50% 증가\n- 턴 종료 시 턴 시작 시보다 다시 도는 피의 충동의 수치가 낮으면 다음 턴에 공격 레벨 증가 3, 방어 레벨 감소 5 얻음
   źródło: Bufs-a1c7p3.json :: dataList[id=WeightOfResponsibility_Panic].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Attack Power Up, 2 Haste, and 2 Fragile\n- Heal +50% more HP when healing\n- Turn End: if the current Returning Bloodlust is lower than its value at Turn Start, gain 3 Offense Level Up and 5 Defense Level Down
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Ataku, 2 Pośpiechu i 2 Wrażliwości\n- Leczenie HP +50%\n- Na koniec tury, jeżeli wartość Powracającego Popędu Krwi jest niższa niż na początku tury, w następnej turze zyskuje 3 Wzrostu Poziomu Ataku i 5 Spadek Poziomu Obrony.
380. [Status [Precarious] — nazwa] 무책임한 꿈
   źródło: Bufs-a1c7p3.json :: dataList[id=Precarious].name
   kontekst: identyfikator statusu w tekstach: `[Precarious]`
   limit: do 40 znaków
   EN: Irresponsible Dream
   PL: Nieodpowiedzialny Sen
381. [Status [Precarious] — opis] 돈키호테에게 피격 시 처치됨.
   źródło: Bufs-a1c7p3.json :: dataList[id=Precarious].desc
   limit: do 120 znaków
   EN: Killed when hit by Don Quixote.
   PL: Ginie przy trafieniu przez Don Quixote.
382. [Status [Penetration] — nazwa] 굳어가는 피
   źródło: Bufs-a1c7p3.json :: dataList[id=Penetration].name
   kontekst: identyfikator statusu w tekstach: `[Penetration]`
   limit: do 40 znaków
   EN: Congealing Blood
   PL: Zastygająca Krew
383. [Status [Penetration] — opis] 2턴동안 행동이 불가능하며, 아군을 꿰뚫은 창 유닛이 생성됨.
   źródło: Bufs-a1c7p3.json :: dataList[id=Penetration].desc
   limit: do 120 znaków
   EN: Cannot act for 2 turns; spawns an Impaling Spear unit over the ally.
   PL: Przez 2 tury nie może działać; nad sojusznikiem pojawia się jednostka Przebijającej Włóczni.
384. [Status [DecreamentalDefense] — nazwa] 심각한 부상
   źródło: Bufs-a1c7p3.json :: dataList[id=DecreamentalDefense].name
   kontekst: identyfikator statusu w tekstach: `[DecreamentalDefense]`
   limit: do 40 znaków
   EN: Crippling Injury
   PL: Wyniszczająca Rana
385. [Status [DecreamentalDefense] — opis] - 이전 전투의 부상이 아직 회복되지 않았다.\n- 최대 체력 대폭 감소\n- 턴 시작시, 누적된 턴 1 당 방어 레벨 감소 1 추가로 얻음 (최대 15)
   źródło: Bufs-a1c7p3.json :: dataList[id=DecreamentalDefense].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Yet to recover from the wounds gained in the previous battle.\n- Massively reduce max HP\n- Turn Start: gain 1 Defense Level Down for every cumulative turn (max 15)
   PL: - Rany z poprzedniej walki jeszcze się nie zagoiły.\n- Maks. HP drastycznie maleje\n- Na początku tury zyskuje dodatkowo 1 Spadek Poziomu Obrony za każdą zsumowaną turę (maks. 15)
386. [Status [UnfinishedDream] — nazwa] 물보다 진한 피에서 벗어나,
   źródło: Bufs-a1c7p3.json :: dataList[id=UnfinishedDream].name
   kontekst: identyfikator statusu w tekstach: `[UnfinishedDream]`
   limit: do 90 znaków
   EN: IN WHICH IS RECOUNTED THE LIBERATION FROM BLOOD THICKER THAN WATER
   PL: Oswobodzenie z krwi gęstszej niż woda,
387. [Status [UnfinishedDream] — opis] - 매 턴 종료 시, 다음 턴에 신속 1, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: Bufs-a1c7p3.json :: dataList[id=UnfinishedDream].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At every Turn End: gain 1 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Na koniec tury w następnej turze zyskuje 1 Pośpiechu i 3 Wzrosty Poziomu Ataku\n- Za każde 3 skumulowane tury zyskuje dodatkowe 2 Wzrosty Poziomu Ataku (maks. 6)\n- Wygrana w Starciu: odzyskuje 3 Poczytalności\n- Za zabicie wroga zyskuje 1 Wzrost Mocy Starcia w następnej turze (raz na turę)
388. [Status [SanchoMind_LowMorale] — nazwa] 깨어나는 살육의 고양감
   źródło: Bufs-a1c7p3.json :: dataList[id=SanchoMind_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[SanchoMind_LowMorale]`
   limit: do 40 znaków
   EN: Reawakening Joy Of Carnage
   PL: Przebudzająca się Radość Rzezi
389. [Status [SanchoMind_LowMorale] — opis] - 사기 저하\n매 턴 시작 시, 공격 레벨 증가 2 얻음. 정신력 효율 +2
   źródło: Bufs-a1c7p3.json :: dataList[id=SanchoMind_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nGain 2 Attack Power Up at every Turn Start; +2 SP Efficiency
   PL: - Niskie Morale\nZyskuje 2 Wzrostu Poziomu Ataku na początku każdej tury; +2 Efektywności Poczytalności
390. [Status [SanchoMind_Panic] — nazwa] 깨어나는 살육의 고양감
   źródło: Bufs-a1c7p3.json :: dataList[id=SanchoMind_Panic].name
   kontekst: identyfikator statusu w tekstach: `[SanchoMind_Panic]`
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Status [SanchoMind_Panic] — opis] - 패닉\n턴 시작 시, 방어 레벨 증가 6 얻음. 다음 턴에 공격 레벨 증가 3 얻음
   źródło: Bufs-a1c7p3.json :: dataList[id=SanchoMind_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: gain 6 Defense Level Up. Gain 3 Offense Level Up next turn
   PL: - Panika\nNa początku tury zyskuje 6 Wzrostu Poziomu Obrony. W następnej turze zyskuje 3 Wzrostu Poziomu Ataku
392. [Status [FragmentOfHope] — nazwa] 버스에서 동료들과 함께 여러 모험을 겪었으며,
   źródło: Bufs-a1c7p3.json :: dataList[id=FragmentOfHope].name
   kontekst: identyfikator statusu w tekstach: `[FragmentOfHope]`
   limit: do 80 znaków
   EN: WHICH TREATS THE BUS, THE COMPANIONS, AND THE ADVENTURES
   PL: W którym mowa o autobusie, towarzyszach i przygodach,
393. [Status [FragmentOfHope] — opis] 수치만큼 합 위력 증가
   źródło: Bufs-a1c7p3.json :: dataList[id=FragmentOfHope].desc
   limit: do 120 znaków
   EN: Gain Clash Power equal to the value
   PL: Zyskuje Moc Starcia równą wartości
394. [Status [FragmentOfHopeTwo] — nazwa] 꿈을 끝내지 않을 산초이자 우리의 돈키호테에 대하여
   źródło: Bufs-a1c7p3.json :: dataList[id=FragmentOfHopeTwo].name
   kontekst: identyfikator statusu w tekstach: `[FragmentOfHopeTwo]`
   limit: do 80 znaków
   EN: OF HOW SANCHO, OUR DON QUIXOTE, REFUSED TO END THE DREAM
   PL: O tym, jak Sancho, nasza Don Quixote, odmówiła zakończenia snu
395. [Status [FragmentOfHopeTwo] — opis] 수치당 합 위력 +4\n전투 시작 시 자신과 아군에게 보호막 부여
   źródło: Bufs-a1c7p3.json :: dataList[id=FragmentOfHopeTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +4 for every value\nApply Shield to self and all allies at Combat Start
   PL: Moc Starcia +4 za każdą wartość\nNa początku walki nakłada Tarczę na siebie i wszystkich sojuszników
396. [Status [ConfinementOfGoldenBranch] — nazwa] 황금가지의 강제 조율
   źródło: Bufs-a1c7p3.json :: dataList[id=ConfinementOfGoldenBranch].name
   kontekst: identyfikator statusu w tekstach: `[ConfinementOfGoldenBranch]`
   limit: do 60 znaków
   EN: The Golden Bough's Forced Arbitration
   PL: Przymusowy Arbitraż Złotej Gałęzi
397. [Status [ConfinementOfGoldenBranch] — opis] - 기본 공격 레벨 30 감소\n- 기본 방어 레벨 30 감소
   źródło: Bufs-a1c7p3.json :: dataList[id=ConfinementOfGoldenBranch].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 30 Base Offense Level\n- Lose 30 Base Defense Level
   PL: - Podstawowy Poziom Ataku -30\n- Podstawowy Poziom Obrony -30

## Statusy i efekty bojowe — Bufs-a1c8p1
- plik gry: `Bufs-a1c8p1.json`

398. [Status [TheDrifter_LowMorale] — nazwa] 박도
   źródło: Bufs-a1c8p1.json :: dataList[id=TheDrifter_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[TheDrifter_LowMorale]`
   limit: do 40 znaków
   EN: Podao
   PL: Podao
399. [Status [TheDrifter_LowMorale] — opis] - 사기저하\n- 일방 공격에 의한 받는 피해량 +10%, 반격으로 주는 피해량 +30%
   źródło: Bufs-a1c8p1.json :: dataList[id=TheDrifter_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +10% damage from Unopposed Attacks; deal +30% damage with Counterattacks
   PL: - Niskie Morale\n- Otrzymuje +10% obrażeń od Ataków Jednostronnych; zadaje +30% obrażeń Kontrą
400. [Status [TheDrifter_Panic] — nazwa] 박도
   źródło: Bufs-a1c8p1.json :: dataList[id=TheDrifter_Panic].name
   kontekst: identyfikator statusu w tekstach: `[TheDrifter_Panic]`
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Status [TheDrifter_Panic] — opis] - 패닉\n- 일방 공격에 의한 받는 피해량 +20%, 반격으로 주는 피해량 +50%
   źródło: Bufs-a1c8p1.json :: dataList[id=TheDrifter_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Take +20% damage from Unopposed Attacks; deal +50% damage with Counterattacks
   PL: - Panika\n- Otrzymuje +20% obrażeń od Ataków Jednostronnych; zadaje +50% obrażeń Kontrą
402. [Status [SipOfAlcohol] — nazwa] 한 모금
   źródło: Bufs-a1c8p1.json :: dataList[id=SipOfAlcohol].name
   kontekst: identyfikator statusu w tekstach: `[SipOfAlcohol]`
   limit: do 40 znaków
   EN: Swig
   PL: Łyczek
403. [Status [SipOfAlcohol] — opis] - 최대값: 5\n- 턴 종료 시 수치가 3 이상이면, 전체 체력의 3%만큼 회복 (본체, 부위)\n- 턴 종료 시 수치가 5라면, 다음 턴에 공격 위력 증가 3, 취약 2 얻음
   źródło: Bufs-a1c8p1.json :: dataList[id=SipOfAlcohol].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack :5\n- Turn End: at 3 Stack, heal 3% HP (Core, Part)\n- Turn End: at 5 Stack, gain 3 Attack Power Up and 2 Fragile next turn
   PL: - Maks. stosów: 5\n- Na koniec tury przy 3+ stosach leczy 3% HP (korpus, części)\n- Na koniec tury przy 5 stosach zyskuje w następnej turze 3 Wzrostu Mocy Ataku i 2 Wrażliwości

## Statusy i efekty bojowe — Bufs-a1c8p2
- plik gry: `Bufs-a1c8p2.json`

404. [Status [ExaminationOfQiu] — nazwa] 일말의 기대
   źródło: Bufs-a1c8p2.json :: dataList[id=ExaminationOfQiu].name
   kontekst: identyfikator statusu w tekstach: `[ExaminationOfQiu]`
   limit: do 40 znaków
   EN: A Sliver of Anticipation
   PL: Iskra Oczekiwania
405. [Status [ExaminationOfQiu] — opis] 전력으로 싸우고 있지 않다.\n- 기본 공격 레벨 35 감소, 기본 방어 레벨 35 감소\n- 대상에게 일방 공격 시 피해량 +30%
   źródło: Bufs-a1c8p2.json :: dataList[id=ExaminationOfQiu].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: He's not giving it his all.\n- Lose 35 Base Offense Level, Lose 35 Base Defense Level\n- Deal +30% damage with Unopposed Attacks
   PL: Nie walczy z pełną siłą.\n- Podstawowy Poziom Ataku -35, Podstawowy Poziom Obrony -35\n- Zadaje +30% obrażeń Atakami Jednostronnymi
406. [Status [BurstStop] — nazwa] 주살【물동】
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstStop].name
   kontekst: identyfikator statusu w tekstach: `[BurstStop]`
   limit: do 40 znaków
   EN: Deathrite 【Halt】
   PL: Obrzęd Śmierci 【Halt】
407. [Status [BurstStop] — opis] 기본값: 4\n- 주살\n- 속박이 3 이상 있는 상태에서 파열이 발동될 때, 1 감소.\n- 수치 감소 시 10만큼 흐트러짐 손상\n- 수치가 0이 될 때, 파열 위력만큼 흐트러짐 손상. 소멸함\n- ※ 이 효과는 갱신되지 않음.
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstStop].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 4\n- Deathrite\n- When getting Rupture triggered while this unit has 3+ Bind, lose 1 Stack\n- When losing Stacks, raise this unit's Stagger Threshold by 10\n- At 0 Stack, raise this unit's Stagger Threshold by Rupture Potency on self, then expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 4\n- Obrzęd Śmierci\n- Gdy wywołane zostaje Rozdarcie, a jednostka ma 3 lub więcej Spętań, maleje o 1.\n- Przy utracie wartości podnosi Próg Oszołomienia o 10\n- Przy wartości 0 podnosi Próg Oszołomienia o Siłę Rozdarcia, po czym znika\n- ※ Ten efekt nie odnawia się.
408. [Status [BurstSuppress] — nazwa] 주살【철주】
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstSuppress].name
   kontekst: identyfikator statusu w tekstach: `[BurstSuppress]`
   limit: do 40 znaków
   EN: Deathrite 【Impede】
   PL: Obrzęd Śmierci 【Impede】
409. [Status [BurstSuppress] — opis] 기본값: 10\n- 주살\n- 다른 주살이 조건에 의해 감소할 때, 수치 1 감소. (턴 당 최대 4)\n- 수치가 0이 될 때, 다음 턴동안 공격 레벨 감소 6 얻음. 소멸함\n- ※ 이 효과는 갱신되지 않음.
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstSuppress].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 10\n- Deathrite\n- When this unit loses other Deathrites' Stacks due to their conditions, lose 1 Stack (max 4 per turn)\n- At 0 Stack, gain 6 Offense Level Down for the next turn, then expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 10\n- Obrzęd Śmierci\n- Gdy inne Obrzędy Śmierci tracą stosy przez swoje warunki, ten maleje o 1. (maks. 4 na turę)\n- Przy wartości 0 zyskuje 6 Spadku Poziomu Ataku na następną turę, po czym znika\n- ※ Ten efekt nie odnawia się.
410. [Status [BurstWave] — nazwa] 주살【즉감】
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstWave].name
   kontekst: identyfikator statusu w tekstach: `[BurstWave]`
   limit: do 40 znaków
   EN: Deathrite 【Wane】
   PL: Obrzęd Śmierci 【Wane】
411. [Status [BurstWave] — opis] 기본값: 10\n- 주살\n부여자에 의해 파열이 발동될 때, 1 감소.\n- 해당 효과를 제외한 자신이 가지고 있는 주살 중 무작위 1개의 수치가 1 감소함.\n- 수치가 0이 될 때, 소멸함\n- ※ 이 효과는 갱신되지 않음.
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstWave].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 10\n- Deathrite\nWhen the unit that inflicted this effect triggers Rupture, lose 1 Stack\n- Also lose 1 Stack of a random Deathrite on self, except for this Deathrite\n- At 0 Stack, expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 10\n- Obrzęd Śmierci\nGdy jednostka, która nałożyła ten efekt, wywołuje Rozdarcie, maleje o 1.\n- Dodatkowo o 1 maleje wartość losowego Obrzędu Śmierci na tej jednostce (poza tym Obrzędem)\n- Przy wartości 0 znika\n- ※ Ten efekt nie odnawia się.
412. [Status [Teaching] — nazwa] 문답
   źródło: Bufs-a1c8p2.json :: dataList[id=Teaching].name
   kontekst: identyfikator statusu w tekstach: `[Teaching]`
   limit: do 40 znaków
   EN: Dialogues
   PL: Dialogi
413. [Status [Teaching] — opis] 최댓값: 3\n- 턴 종료시, 정신력 5 회복\n- 전투 중 체력이 0이 될 때 체력을 최대 체력만큼 회복함 (수치만큼 발동)\n- 발동 횟수: {0}
   źródło: Bufs-a1c8p2.json :: dataList[id=Teaching].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Max Stack: 3\n- Turn End: heal 5 SP\n- When HP drops to 0 during the Encounter, heal up to max HP (activates as many times as this unit has Stacks)\n- Activated: {0} time(s)
   PL: Maks.: 3\n- Na koniec tury odzyskuje 5 Poczytalności\n- Gdy w trakcie walki HP spadnie do 0, odzyskuje HP do Maks. HP (wywoływane tyle razy, ile wynosi wartość)\n- Liczba wywołań: {0}
414. [Status [BurstWeakness] — nazwa] 주살【약화】
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstWeakness].name
   kontekst: identyfikator statusu w tekstach: `[BurstWeakness]`
   limit: do 40 znaków
   EN: Deathrite 【Enfeeble】
   PL: Obrzęd Śmierci 【Enfeeble】
415. [Status [BurstWeakness] — opis] 기본값: 5\n- 주살\n- 대상의 속도가 빠르고, 속도 차이가 5 이상일 때, 피격 시 파열이 발동될 때, 1 감소.\n- 수치 감소 시 다음 턴에 방어 레벨 감소 1 을 얻음 (턴 당 최대 1)\n- 수치가 0이 될 때, 다음 턴 방어 레벨 감소 3, 속박 1을 얻고 소멸\n- ※ 이 효과는 갱신되지 않음.
   źródło: Bufs-a1c8p2.json :: dataList[id=BurstWeakness].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 5\n- Deathrite\n- If the target's Speed is faster than this unit's, and if the Speed difference 5 or greater: when getting Rupture triggered, lose 1 Stack\n- When losing Stacks, gain 1 Defense Level Down next turn (once per turn)\n- At 0 Stack, gain 3 Defense Level Down and 1 Bind next turn, then expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 5\n- Obrzęd Śmierci\n- Jeżeli Szybkość celu jest większa, a różnica Szybkości wynosi 5 lub więcej: gdy przy trafieniu wywołane zostaje Rozdarcie, maleje o 1.\n- Przy utracie wartości zyskuje 1 Spadek Poziomu Obrony na następną turę (1 raz na turę)\n- Przy wartości 0 zyskuje 3 Spadek Poziomu Obrony i 1 Spętanie na następną turę, po czym znika\n- ※ Ten efekt nie odnawia się.
416. [Status [Qiu_LowMorale] — nazwa] 가치우
   źródło: Bufs-a1c8p2.json :: dataList[id=Qiu_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Qiu_LowMorale]`
   limit: do 40 znaków
   EN: Jia Qiu
   PL: Jia Qiu
417. [Status [Qiu_LowMorale] — opis] - 사기저하\n- 홍루를 제외한 대상에게 가하는 피해량 +10%
   źródło: Bufs-a1c8p2.json :: dataList[id=Qiu_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal +10% damage against targets that aren't Hong Lu
   PL: - Niskie Morale\n- Zadaje +10% obrażeń celom innym niż Hong Lu
418. [Status [Qiu_Panic] — nazwa] 가치우
   źródło: Bufs-a1c8p2.json :: dataList[id=Qiu_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Qiu_Panic]`
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Status [Qiu_Panic] — opis] - 패닉\n- 홍루를 제외한 대상에게 가하는 피해량 +20%
   źródło: Bufs-a1c8p2.json :: dataList[id=Qiu_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal +20% damage against targets that aren't Hong Lu
   PL: - Panika\n- Zadaje +20% obrażeń celom innym niż Hong Lu
420. [Status [QiuAndHonglu] — nazwa] 나의 진짜 마음…
   źródło: Bufs-a1c8p2.json :: dataList[id=QiuAndHonglu].name
   kontekst: identyfikator statusu w tekstach: `[QiuAndHonglu]`
   limit: do 40 znaków
   EN: My True Heart...
   PL: Moje prawdziwe serce…
421. [Status [QiuAndHonglu] — opis] - 홍루의 모든 스킬의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)
   źródło: Bufs-a1c8p2.json :: dataList[id=QiuAndHonglu].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Skills gain +1 Final Power\n- On Clash Win, 1 ally(including this unit) with the least SP heals 5 SP\n- When an ally dies, remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)
   PL: - Wszystkie Umiejętności Hong Lu zyskują Moc Końcowa +1\n- Po wygranym Starciu 1 sojusznik (w tym ta jednostka) o najniższej Poczytalności odzyskuje +5 Poczytalności\n- Gdy ginie sojusznik, pozostali na koniec tury zyskują 1 Wzrost Mocy Ataku na następną turę (raz/turę)
422. [Status [ProtectStance] — nazwa] 보호 태세
   źródło: Bufs-a1c8p2.json :: dataList[id=ProtectStance].name
   kontekst: identyfikator statusu w tekstach: `[ProtectStance]`
   limit: do 40 znaków
   EN: Protective Stance
   PL: Postawa Ochronna
423. [Status [ProtectStance] — opis] 최댓값 : 2\n이 효과는 합산되지 않고, 갱신됨\n턴 종료 시 1 감소\n이 효과를 얻으면 다음 턴에 아래 효과 적용\n- 보호 2 얻음\n- 자신의 각 슬롯 도발치 5 증가
   źródło: Bufs-a1c8p2.json :: dataList[id=ProtectStance].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 2\nThis effect does not compound in potency; stacking it only extends its duration\nReduced by 1 at Turn End\nWhen a unit gains this effect, gain the following effects next turn:\n- Gain 2 Protection\n- Gain 5 Aggro to each of this unit's Slots
   PL: Maks. stosów: 2\nTen efekt się nie sumuje — odnawia się\nNa koniec tury maleje o 1\nPo zdobyciu tego efektu w następnej turze:\n- Zyskuje 2 Ochrony\n- Prowokacja każdego slotu tej jednostki rośnie o 5
424. [Status [ZiluDebuff] — nazwa] 살기 억제
   źródło: Bufs-a1c8p2.json :: dataList[id=ZiluDebuff].name
   kontekst: identyfikator statusu w tekstach: `[ZiluDebuff]`
   limit: do 40 znaków
   EN: Bloodthirst Suppressed
   PL: Ukrócona Krwiożerczość
425. [Status [ZiluDebuff] — opis] - 기본 공격 레벨 20 감소, 기본 방어 레벨 20 감소
   źródło: Bufs-a1c8p2.json :: dataList[id=ZiluDebuff].desc
   limit: do 120 znaków
   EN: - Lose 20 Base Offense Level, Lose 20 Base Defense Level
   PL: - Podstawowy Poziom Ataku -20, Podstawowy Poziom Obrony -20
426. [Status [WitheredWood_LowMorale] — nazwa] 고목화
   źródło: Bufs-a1c8p2.json :: dataList[id=WitheredWood_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[WitheredWood_LowMorale]`
   limit: do 40 znaków
   EN: Eldtree Mutation
   PL: Mutacja Prastarego Drzewa
427. [Status [WitheredWood_LowMorale] — opis] - 사기 저하\n- 피해량 증가 1, 취약 1, 파열 취약 1 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=WitheredWood_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Damage Up, 1 Fragile, and 1 Rupture Fragility
   PL: - Niskie Morale\n- Zyskuje 1 Wzrost Obrażeń, 1 Wrażliwości i 1 Wrażliwość na Rozdarcie
428. [Status [WitheredWood_Panic] — nazwa] 고목화
   źródło: Bufs-a1c8p2.json :: dataList[id=WitheredWood_Panic].name
   kontekst: identyfikator statusu w tekstach: `[WitheredWood_Panic]`
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Status [WitheredWood_Panic] — opis] - 패닉\n- 피해량 증가 2, 취약 2, 파열 취약 2 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=WitheredWood_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Damage Up, 2 Fragile, and 2 Rupture Fragility
   PL: - Panika\n- Zyskuje 2 Wzrostu Obrażeń, 2 Wrażliwości i 2 Wrażliwość na Rozdarcie
430. [Status [EvilHeart_LowMorale] — nazwa] 사심
   źródło: Bufs-a1c8p2.json :: dataList[id=EvilHeart_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[EvilHeart_LowMorale]`
   limit: do 40 znaków
   EN: Heart of Evil
   PL: Serce Zła
431. [Status [EvilHeart_LowMorale] — opis] - 사기 저하\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 피해량 증가 2, 취약 1 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=EvilHeart_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +2\nTurn Start: gain 2 Damage Up and 1 Fragile
   PL: - Niskie Morale\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +2\nNa początku tury zyskuje 2 Wzrostu Obrażeń i 1 Wrażliwości
432. [Status [EvilHeart_Panic] — nazwa] 사심
   źródło: Bufs-a1c8p2.json :: dataList[id=EvilHeart_Panic].name
   kontekst: identyfikator statusu w tekstach: `[EvilHeart_Panic]`
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Status [EvilHeart_Panic] — opis] - 패닉\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 피해량 증가 3, 취약 2 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=EvilHeart_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +3\nTurn Start: gain 3 Damage Up and 2 Fragile
   PL: - Panika\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +3\nNa początku tury zyskuje 3 Wzrostu Obrażeń i 2 Wrażliwości
434. [Status [DeepEvilHeart_LowMorale] — nazwa] 짙은 사심
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepEvilHeart_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DeepEvilHeart_LowMorale]`
   limit: do 40 znaków
   EN: Heart of Oppressive Evil
   PL: Głębokie Serce Zła
435. [Status [DeepEvilHeart_LowMorale] — opis] - 사기 저하\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 피해량 증가 3, 취약 1 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepEvilHeart_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +2\nTurn Start: gain 3 Damage Up and 1 Fragile
   PL: - Niskie Morale\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +2\nNa początku tury zyskuje 3 Wzrostu Obrażeń i 1 Wrażliwości
436. [Status [DeepEvilHeart_Panic] — nazwa] 짙은 사심
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepEvilHeart_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DeepEvilHeart_Panic]`
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Status [DeepEvilHeart_Panic] — opis] - 패닉\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 피해량 증가 4, 취약 2 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepEvilHeart_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +3\nTurn Start: gain 4 Damage Up and 2 Fragile
   PL: - Panika\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +3\nNa początku tury zyskuje 4 Wzrostu Obrażeń i 2 Wrażliwości
438. [Status [OminousTalisman] — nazwa] 불길한 부적
   źródło: Bufs-a1c8p2.json :: dataList[id=OminousTalisman].name
   kontekst: identyfikator statusu w tekstach: `[OminousTalisman]`
   limit: do 40 znaków
   EN: Omen Talisman
   PL: Złowieszczy Talizman
439. [Status [OminousTalisman] — opis] - 기본값 : 10\n- 수치가 0이 될 때, 파열 위력만큼 탐식 속성 피해와 정신력 피해를 받고 소멸 (정신력 피해 최대 20)\n- 불길한 부적이 감소할 때 감소한 수치만큼 파열 위력을 얻고 그 수치의 절반만큼 파열 횟수가 증가 (소수점 버림)\n※ 이 효과는 갱신되지 않음
   źródło: Bufs-a1c8p2.json :: dataList[id=OminousTalisman].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- When dropping to 0 Stack: take Gluttony damage and SP damage equal to Rupture Potency on self, then expires (max SP damage: 20)\n- When losing Omen Talismans, gain Rupture Potency equal to the number of Omen Talismans lost; then, gain half of Rupture Potency lost as Rupture Count (rounded down)\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: - Wartość bazowa: 10\n- Przy spadku do 0 stosów otrzymuje obrażenia Obżarstwa i obrażenia Poczytalności równe Sile Rozdarcia, po czym znika (maks. obrażeń Poczytalności: 20)\n- Gdy Złowieszczy Talizman maleje, zyskuje Siłę Rozdarcia równą utraconej liczbie, a Licznik Rozdarcia rośnie o połowę tej liczby (zaokrąglone w dół)\n※ Ten efekt nie odnawia się
440. [Status [RepressedMurderousIntendTwo] — nazwa] 눌린 살기
   źródło: Bufs-a1c8p2.json :: dataList[id=RepressedMurderousIntendTwo].name
   kontekst: identyfikator statusu w tekstach: `[RepressedMurderousIntendTwo]`
   limit: do 40 znaków
   EN: Concealed Bloodthirst
   PL: Skryta Krwiożerczość
441. [Status [RepressedMurderousIntendTwo] — opis] 기본 공격 레벨 5 감소\n기본 방어 레벨 5 감소
   źródło: Bufs-a1c8p2.json :: dataList[id=RepressedMurderousIntendTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose 5 Base Offense Level\nLose 5 Base Defense Level
   PL: Podstawowy Poziom Ataku -5\nPodstawowy Poziom Obrony -5
442. [Status [UncontrolledChargeAxe_LowMorale] — nazwa] 충전 회로 역류
   źródło: Bufs-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[UncontrolledChargeAxe_LowMorale]`
   limit: do 50 znaków
   EN: Charge Circuitry Countercurrent
   PL: Wsteczny Prąd Obwodu Ładowania
443. [Status [UncontrolledChargeAxe_LowMorale] — opis] - 사기 저하\n파열을 보유한 대상과 합 진행 시, 충전 횟수 3, 취약 1 얻음 (턴 당 2회)
   źródło: Bufs-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Rupture, gain +3 Charge Count and 1 Fragile (2 times per turn)
   PL: - Niskie Morale\nW Starciu z celami posiadającymi Rozdarcie zyskuje +3 Liczby Ładunków i 1 Wrażliwości (2 razy na turę)
444. [Status [UncontrolledChargeAxe_Panic] — nazwa] 충전 회로 역류
   źródło: Bufs-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_Panic].name
   kontekst: identyfikator statusu w tekstach: `[UncontrolledChargeAxe_Panic]`
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Status [UncontrolledChargeAxe_Panic] — opis] - 패닉\n파열을 보유한 대상과 합 진행 시, 충전 횟수 5, 피해량 증가 1, 취약 2 얻음 (턴 당 2회)
   źródło: Bufs-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nWhen Clashing against targets with Rupture, gain +5 Charge Count, 1 Damage Up, and 2 Fragile (2 times per turn)
   PL: - Panika\nW Starciu z celami posiadającymi Rozdarcie zyskuje +5 Liczby Ładunków, 1 Wzrost Obrażeń i 2 Wrażliwości (2 razy na turę)
446. [Status [MadFeather] — nazwa] 눈알 깃
   źródło: Bufs-a1c8p2.json :: dataList[id=MadFeather].name
   kontekst: identyfikator statusu w tekstach: `[MadFeather]`
   limit: do 40 znaków
   EN: Eyeball Pinion
   PL: Pióro z Gałką Oczową
447. [Status [MadFeather] — opis] - 최대값 : 10\n- 턴 종료시, (수치/2)만큼 파열 횟수, 출혈 횟수 얻음 (소수점 버림)\n- 턴 종료시, 수치 1 감소
   źródło: Bufs-a1c8p2.json :: dataList[id=MadFeather].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Turn End: gain (Stack / 2) Rupture Count and Bleed Count (rounded down)\n- Turn End: lose 1 Stack
   PL: - Maks. stosów: 10\n- Na koniec tury zyskuje (stosy/2) Licznika Rozdarcia i Licznika Krwawienia (zaokrąglone w dół)\n- Na koniec tury traci 1 stos
448. [Status [MadFeather_LowMorale] — nazwa] 양날깃
   źródło: Bufs-a1c8p2.json :: dataList[id=MadFeather_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[MadFeather_LowMorale]`
   limit: do 40 znaków
   EN: Double-edged Feather
   PL: Dwukrawędziowe Pióro
449. [Status [MadFeather_LowMorale] — opis] - 사기 저하\n턴 시작시 취약 1, 체력 회복 증가 1 얻음. 자신의 공격 적중시 파열 1, 출혈 1 부여
   źródło: Bufs-a1c8p2.json :: dataList[id=MadFeather_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: gain 1 Fragile and 1 HP Healing Boost. On Hit, inflict 1 Rupture and 1 Bleed
   PL: - Niskie Morale\nNa początku tury zyskuje 1 Wrażliwości i 1 Wzrost Leczenia HP. Przy trafieniu nakłada 1 Rozdarcie i 1 Krwawienie
450. [Status [MadFeather_Panic] — nazwa] 양날깃
   źródło: Bufs-a1c8p2.json :: dataList[id=MadFeather_Panic].name
   kontekst: identyfikator statusu w tekstach: `[MadFeather_Panic]`
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Status [MadFeather_Panic] — opis] - 패닉\n턴 시작시 취약 2, 체력 회복 증가 2 얻음. 자신의 공격 적중시 파열 1, 출혈 1 부여
   źródło: Bufs-a1c8p2.json :: dataList[id=MadFeather_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: -Panic\nTurn Start: gain 2 Fragile and 2 HP Healing Boost. On Hit, inflict 1 Rupture and 1 Bleed
   PL: - Panika\nNa początku tury zyskuje 2 Wrażliwości i 2 Wzrost Leczenia HP. Przy trafieniu nakłada 1 Rozdarcie i 1 Krwawienie
452. [Status [JarMaster_LowMorale] — nazwa] 돌격 지시
   źródło: Bufs-a1c8p2.json :: dataList[id=JarMaster_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[JarMaster_LowMorale]`
   limit: do 40 znaków
   EN: Charge Order
   PL: Rozkaz Szturmu
453. [Status [JarMaster_LowMorale] — opis] - 사기 저하\n턴 시작시 취약 1을 얻고, 모든 아군에게 피해량 증가 1 부여
   źródło: Bufs-a1c8p2.json :: dataList[id=JarMaster_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: gain 1 Fragile and apply 1 Damage Up to all allies
   PL: - Niskie Morale\nNa początku tury zyskuje 1 Wrażliwości i nakłada 1 Wzrost Obrażeń na wszystkich sojuszników
454. [Status [JarMaster_Panic] — nazwa] 돌격 지시
   źródło: Bufs-a1c8p2.json :: dataList[id=JarMaster_Panic].name
   kontekst: identyfikator statusu w tekstach: `[JarMaster_Panic]`
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Status [JarMaster_Panic] — opis] - 패닉\n턴 시작시 취약 2를 얻고, 모든 아군에게 피해량 증가 2 부여
   źródło: Bufs-a1c8p2.json :: dataList[id=JarMaster_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: gain 2 Fragile and apply 2 Damage Up to all allies
   PL: - Panika\nNa początku tury zyskuje 2 Wrażliwości i nakłada 2 Wzrostu Obrażeń na wszystkich sojuszników
456. [Status [DeepAngry_LowMorale] — nazwa] 울분
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepAngry_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DeepAngry_LowMorale]`
   limit: do 40 znaków
   EN: Angst
   PL: Udręka
457. [Status [DeepAngry_LowMorale] — opis] - 사기 저하\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 피해량 증가 2, 취약 1 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepAngry_LowMorale].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Status [DeepAngry_Panic] — nazwa] 울분
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepAngry_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DeepAngry_Panic]`
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Status [DeepAngry_Panic] — opis] - 패닉\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 피해량 증가 3, 취약 2 얻음
   źródło: Bufs-a1c8p2.json :: dataList[id=DeepAngry_Panic].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Status [TakeBreath_LowMorale] — nazwa] 숨 돌리기
   źródło: Bufs-a1c8p2.json :: dataList[id=TakeBreath_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[TakeBreath_LowMorale]`
   limit: do 40 znaków
   EN: Catching Breath
   PL: Wyrównanie Oddechu
461. [Status [TakeBreath_LowMorale] — opis] - 사기 저하\n턴 시작시 방어 레벨 증가 2를 얻고 호흡 위력 2 감소
   źródło: Bufs-a1c8p2.json :: dataList[id=TakeBreath_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: gain 2 Defense Level Up and lose 2 Poise Potency
   PL: - Niskie Morale\nNa początku tury zyskuje 2 Wzrostu Poziomu Obrony i traci 2 Siły Oddechu
462. [Status [TakeBreath_Panic] — nazwa] 숨 돌리기
   źródło: Bufs-a1c8p2.json :: dataList[id=TakeBreath_Panic].name
   kontekst: identyfikator statusu w tekstach: `[TakeBreath_Panic]`
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Status [TakeBreath_Panic] — opis] - 패닉\n턴 시작시 방어 레벨 증가 5를 얻고 호흡 위력 5 감소
   źródło: Bufs-a1c8p2.json :: dataList[id=TakeBreath_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: gain 5 Defense Level Up and lose 5 Poise Potency
   PL: - Panika\nNa początku tury zyskuje 5 Wzrostu Poziomu Obrony i traci 5 Siły Oddechu

## Statusy i efekty bojowe — Bufs-a1c8p3
- plik gry: `Bufs-a1c8p3.json`

464. [Status [Bothersome] — nazwa] 절참 [切斬]
   źródło: Bufs-a1c8p3.json :: dataList[id=Bothersome].name
   kontekst: identyfikator statusu w tekstach: `[Bothersome]`
   limit: do 40 znaków
   EN: Severing Slash [切斬]
   PL: Rozcinające Cięcie [切斬]
465. [Status [Bothersome] — opis] - 대상의 참격 내성을 약점(1.5)으로 취급함 (대상의 참격 내성이 1.5 이상인 경우에는 적용되지 않음)\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c8p3.json :: dataList[id=Bothersome].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The target's Slash Resistance counts as 'Weak'(1.5). (does not activate against targets with 1.5 or higher Slash Resistance)\n- Expires at Turn End
   PL: - Odporność na Cięcie celu liczy się jako Słaba (1,5). (nie działa na cele z odpornością na Cięcie 1,5 lub wyższą)\n- Na koniec tury znika
466. [Status [VibrationIgnition] — nazwa] 진동 - 작열
   źródło: Bufs-a1c8p3.json :: dataList[id=VibrationIgnition].name
   kontekst: identyfikator statusu w tekstach: `[VibrationIgnition]`
   limit: do 40 znaków
   EN: Tremor - Scorch
   PL: Wstrząs - Żar
467. [Status [VibrationIgnition] — opis] - 진동 폭발 시 (진동 위력과 화상 위력의 합/2)만큼 분노 피해를 입고 화상 횟수 1 감소\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs-a1c8p3.json :: dataList[id=VibrationIgnition].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Wrath Damage equal to (sum of Tremor Potency and Burn Potency / 2), and lose 1 Burn Count\n- When hit by Skills that trigger Tremor Burst, raise this unit's Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wyładowaniu Wstrząsu otrzymuje obrażenia Gniewu równe (suma Siły Wstrząsu i Siły Podpalenia / 2) i traci 1 Licznika Podpalenia\n- Przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu podnosi Próg Oszołomienia o Siłę tego efektu\n- Po zakończeniu tury traci 1 Licznika\n(Działa tak samo jak zwykły Wstrząs wobec efektów zwiększających lub zmniejszających Siłę i Licznik Wstrząsu)
468. [Status [BulletPropellant] — nazwa] 호표탄
   źródło: Bufs-a1c8p3.json :: dataList[id=BulletPropellant].name
   kontekst: identyfikator statusu w tekstach: `[BulletPropellant]`
   limit: do 40 znaków
   EN: Tigermark Round
   PL: Pocisk Tygrysiego Znaku
469. [Status [BulletPropellant] — opis] - 특수 탄환\n- 특정 스킬 사용 시 소모\n- 최댓값 : 6
   źródło: Bufs-a1c8p3.json :: dataList[id=BulletPropellant].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Spent by certain Skills\n- Max Stack: 6
   PL: - Specjalna amunicja\n- Zużywana przy użyciu określonych Umiejętności\n- Maks. stosów: 6
470. [Status [BulletPropellantSpecial] — nazwa] 맹호표탄
   źródło: Bufs-a1c8p3.json :: dataList[id=BulletPropellantSpecial].name
   kontekst: identyfikator statusu w tekstach: `[BulletPropellantSpecial]`
   limit: do 40 znaków
   EN: Savage Tigermark Round
   PL: Dziki Pocisk Tygrysiego Znaku
471. [Status [BulletPropellantSpecial] — opis] - 특수 탄환\n- 특정 스킬 사용 시 소모 (호표탄의 효과가 적용됨)\n- 장착한 탄환과 남은 탄환이 이 효과의 위력과 횟수로 표기됨\n· 위력 최댓값 (장착한 탄환) : 6\n- 이 탄환을 소모한 코인의 피해량이 30%만큼 증가하고, 부여하는 화상 위력, 화상 횟수의 부여값이 2배로 증가\n- 장착한 탄환과 남은 탄환을 전부 소모하면 호표탄으로 변경
   źródło: Bufs-a1c8p3.json :: dataList[id=BulletPropellantSpecial].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Spent by certain Skills (actives the same way as Tigermark Round does)\n- The Potency and the Count of this effect are "Loaded Ammo" and "Remaining Ammo", respectively\n· Max Potency (Loaded Ammo): 6\n- Coins that spent this Ammo deal +30% damage, and inflict double the normal amount of Burn Potency and Count\n- When all Loaded Ammo and Remaining Ammo are spent, converts back to Tigermark Round
   PL: - Specjalna amunicja\n- Zużywana przy użyciu określonych Umiejętności (działa jak Pocisk Znaku Tygrysa)\n- Siła i Licznik tego efektu oznaczają „Załadowaną Amunicję” i „Pozostałą Amunicję”\n· Maks. Siły (Załadowana Amunicja): 6\n- Monety, które zużyły tę amunicję, zadają +30% obrażeń i nakładają dwukrotnie więcej Siły i Licznika Podpalenia\n- Po zużyciu całej Załadowanej i Pozostałej Amunicji zmienia się z powrotem w Pocisk Znaku Tygrysa
472. [Status [Prey] — nazwa] 사냥감
   źródło: Bufs-a1c8p3.json :: dataList[id=Prey].name
   kontekst: identyfikator statusu w tekstach: `[Prey]`
   limit: do 40 znaków
   EN: Prey
   PL: Zdobycz
473. [Status [Prey] — opis] - 적과 합 진행 시, 합 위력 - 5\n- 전투 시작 시,\n· 공격 스킬을 장착하였다면 공격 스킬로 뇌횡에게 가하는 피해량이 50%만큼 감소\n· 수비 스킬을 장착하였다면 뇌횡에게 받는 피해량이 75%만큼 감소\n- 이 효과를 보유한 상태에서 뇌횡과 합하여 승리 시, 제일 적게 보유한 E.G.O 자원 3개 획득\n- 턴 종료 시 사라지고, 자신의 정신력 10 회복
   źródło: Bufs-a1c8p3.json :: dataList[id=Prey].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash with an enemy, Clash Power -5\n- Combat Start:\n· If this unit equipped an Attack Skill, deal -50% damage against Lei Heng using Attack Skills\n· If this unit equipped a Defense Skill, take -75% damage from Lei Heng\n- If this unit wins a Clash against Lei Heng while under this effect, gain 3 of the least-owned E.G.O Resources\n- Expires at Turn End; this unit heals 10 SP
   PL: - W Starciu z wrogiem Moc Starcia -5\n- Na początku walki,\n· Jeżeli wyposażono Umiejętność ataku, zadaje o 50% mniej obrażeń Lei Hengowi Umiejętnościami ataku\n· Jeżeli wyposażono Umiejętność obrony, otrzymuje o 75% mniej obrażeń od Lei Henga\n- Jeżeli wygrywa Starcie z Lei Hengiem, mając ten efekt, zyskuje 3 najmniej posiadanych Zasobów E.G.O\n- Znika na koniec tury, a jednostka odzyskuje 10 Poczytalności
474. [Status [Complacency] — nazwa] 오버히트
   źródło: Bufs-a1c8p3.json :: dataList[id=Complacency].name
   kontekst: identyfikator statusu w tekstach: `[Complacency]`
   limit: do 40 znaków
   EN: Overheat
   PL: Przegrzanie
475. [Status [Complacency] — opis] - 최댓값 : 5\n- 턴 시작 시, 수치만큼 합 위력 감소, 취약 얻음\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c8p3.json :: dataList[id=Complacency].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: gain Clash Power Down and Fragile equal to the Stack\n- Expires at Turn End
   PL: - Maks. stosów: 5\n- Na początku tury zyskuje Spadek Mocy Starcia i Wrażliwości równy liczbie stosów\n- Na koniec tury znika
476. [Status [BattleSense] — nazwa] 저력 [底力]
   źródło: Bufs-a1c8p3.json :: dataList[id=BattleSense].name
   kontekst: identyfikator statusu w tekstach: `[BattleSense]`
   limit: do 40 znaków
   EN: Inner Strength [底力]
   PL: Siła Skryta [底力]
477. [Status [BattleSense] — opis] - 최댓값 : 25\n- 특정 스킬 사용 시 소모하며, 해당 턴 종료 시 소모한 수치만큼 정신력을 회복\n- 합을 진행할 때마다 1 증가 (스킬당 최대 5). 합 패배 시, 해당 합에서 얻은 스택을 잃음\n- 일방 공격으로 적중 시 2 증가 (스킬당 최대 10)\n- 누적 소모한 수치에 비례하여 턴 종료 시 다음 턴에 신속 얻음 (수치 25당 신속 1, 최대 2)\n- 특정 패턴 시, 버프가 변경됨\n\n- 누적 소모량 : {0}
   źródło: Bufs-a1c8p3.json :: dataList[id=BattleSense].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Stack: 25\n- Consumed by certain Skills; at Turn End, heal SP equal to the Stack consumed by the end of the turn\n- Gain 1 Stack with every Clash (max 5 per Skill). On Clash Lose, lose the Stacks gained from the said Clash\n- Gain 2 Stack when hitting with an Unopposed Attack (max 10 per Skill)\n- Turn End: next turn, gain Haste based on the total Stack consumed this turn (1 Haste per 25 Stack; max 2)\n- Gains a different buff when using a specific pattern\n\n- Total Stacks Consumed: {0}
   PL: - Maks.: 25\n- Zużywana przez określone Umiejętności; na koniec tury odzyskuje Poczytalność równą wartości zużytej do końca tury\n- Rośnie o 1 w każdym Starciu (maks. 5 na Umiejętność). Po przegranej w Starciu traci stosy zyskane w tym Starciu\n- Przy trafieniu Atakiem Niekwestionowanym rośnie o 2 (maks. 10 na Umiejętność)\n- Zależnie od skumulowanej zużytej wartości zyskuje na koniec tury w następnej turze Pośpiech (1 Pośpiechu za każde 25 wartości, maks. 2)\n- Przy określonym wzorcu Wzmocnienie się zmienia\n\n- Skumulowane zużycie: {0}
478. [Status [RestoredBattleSense] — nazwa] 극력 [極力]
   źródło: Bufs-a1c8p3.json :: dataList[id=RestoredBattleSense].name
   kontekst: identyfikator statusu w tekstach: `[RestoredBattleSense]`
   limit: do 40 znaków
   EN: Extreme Strength [極力]
   PL: Siła Skrajna [極力]
479. [Status [RestoredBattleSense] — opis] - 최댓값 : 50\n- 저력으로 취급함. 특정 스킬 사용 시 소모하며, 해당 턴 종료 시 소모한 수치만큼 정신력을 회복\n- 합을 진행할 때마다 2 증가 (스킬당 최대 10). 합 패배 시, 해당 합에서 얻은 스택을 잃음\n- 일방 공격으로 적중 시 3 증가 (스킬당 최대 15)\n- 누적 소모한 수치에 비례하여 턴 종료 시 다음 턴에 신속 얻음 (수치 25당 신속 1, 최대 5)\n\n- 누적 소모량 : {0}
   źródło: Bufs-a1c8p3.json :: dataList[id=RestoredBattleSense].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Stack: 50\n- Counts as "Inner Strength". Consumed by certain Skills; at Turn End, heal SP equal to the Stack consumed by the end of the turn.\n- Gain 2 Stack with every Clash (max 10 per Skill). On Clash Lose, lose the Stacks gained from the said Clash\n- Gain 3 Stack when hitting with an Unopposed Attack (max 15 per Skill)\n- Turn End: next turn, gain Haste based on the total Stack consumed this turn (1 Haste per 25 Stack, max 5)\n\n- Total Stacks Consumed: {0}
   PL: - Maks.: 50\n- Traktowana jako 'Siła Skryta'. Zużywana przez określone Umiejętności; na koniec tury odzyskuje Poczytalność równą wartości zużytej do końca tury\n- Rośnie o 2 w każdym Starciu (maks. 10 na Umiejętność). Po przegranej w Starciu traci stosy zyskane w tym Starciu\n- Przy trafieniu Atakiem Niekwestionowanym rośnie o 3 (maks. 15 na Umiejętność)\n- Zależnie od skumulowanej zużytej wartości zyskuje na koniec tury w następnej turze Pośpiech (1 Pośpiechu za każde 25 wartości, maks. 5)\n\n- Skumulowane zużycie: {0}
480. [Status [Irritation] — nazwa] 천퇴성[天退星]
   źródło: Bufs-a1c8p3.json :: dataList[id=Irritation].name
   kontekst: identyfikator statusu w tekstach: `[Irritation]`
   limit: do 40 znaków
   EN: Tiantui Star [天退星]
   PL: Gwiazda Tianhui [天退星]
481. [Status [Irritation] — opis] - 턴 시작 시, 잃은 체력 20%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 3)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +2\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 20%)\n- '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경\n- 특정 패턴 시, 이 버프가 신(心) - 천퇴성[天退星]으로 변경
   źródło: Bufs-a1c8p3.json :: dataList[id=Irritation].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Damage Up and 1 Power Up for every 20% missing HP on self (max 3 each)\n- Inflict +2 more Tremor Potency with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 20%)\n- Convert the final Coin of 'Triple Slash - Blast' to an Unbreakable Coin\n- This buff changes into Shin (心) - Tiantui Star [天退星] when using a specific pattern
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy za każde 20% brakującego HP (każdy maks. 3)\n- Umiejętności nakładają na wrogów o 2 więcej Siły Wstrząsu\n- Jeżeli Szybkość tej jednostki jest o 3 lub więcej większa od Szybkości celu, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 20%)\n- Ostatnia Moneta „Potrójnego Cięcia - Wybuch” staje się Niezniszczalną Monetą\n- Przy określonym wzorcu ten buff zmienia się w Shin (心) - Gwiazdę Tiantui [天退星]
482. [Status [HugeIrritation] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: Bufs-a1c8p3.json :: dataList[id=HugeIrritation].name
   kontekst: identyfikator statusu w tekstach: `[HugeIrritation]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Shin (心) - Gwiazda Tiantui [天退星]
483. [Status [HugeIrritation] — opis] - 턴 시작 시, 잃은 체력 15%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 5)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +3, 진동 횟수 증가량 +1\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 20%)\n- '이연참-폭', '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: Bufs-a1c8p3.json :: dataList[id=HugeIrritation].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Damage Up and 1 Power Up for every 15% missing HP on self (max 5 each)\n- Inflict +3 more Tremor Potency and +1 more Tremor Count with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 20%)\n- Convert the final Coins of 'Double Slash - Blast' and 'Triple Slash - Blast' to Unbreakable Coins
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy za każde 15% brakującego HP (każdy maks. 5)\n- Umiejętności nakładają na wrogów o 3 więcej Siły Wstrząsu i +1 Licznika Wstrząsu\n- Jeżeli Szybkość tej jednostki jest o 3 lub więcej większa od Szybkości celu, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 20%)\n- Ostatnie Monety „Podwójnego Cięcia - Wybuch” i „Potrójnego Cięcia - Wybuch” stają się Niezniszczalnymi Monetami
484. [Status [ReloadKeepAmmo] — nazwa] 재장전 - 잔탄 유지
   źródło: Bufs-a1c8p3.json :: dataList[id=ReloadKeepAmmo].name
   kontekst: identyfikator statusu w tekstach: `[ReloadKeepAmmo]`
   limit: do 40 znaków
   EN: Reload - Tactical
   PL: Przeładowanie - Taktyczne
485. [Status [ReloadKeepAmmo] — opis] - 탄환을 획득 가능한 최대 수치만큼 다시 얻음 (단, 보유한 탄환을 버리지 않음)
   źródło: Bufs-a1c8p3.json :: dataList[id=ReloadKeepAmmo].desc
   limit: do 120 znaków
   EN: - Restore this unit's Ammo to its maximum capacity (does not discard any remaining Ammo)
   PL: - Odzyskuje amunicję do Maks. wartości (bez wyrzucania posiadanej amunicji)
486. [Status [BeastEyes_LowMorale] — nazwa] 맹수의 본능 - 사기저하
   źródło: Bufs-a1c8p3.json :: dataList[id=BeastEyes_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BeastEyes_LowMorale]`
   limit: do 50 znaków
   EN: Beastly Instinct - Low Morale
   PL: Instynkt Bestii - Niskie Morale
487. [Status [BeastEyes_LowMorale] — opis] - 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이/2)%만큼 증가 (최대 10%)\n- 턴 시작 시, 최종 위력 증가 1, 피해량 증가 1, 취약 1 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=BeastEyes_LowMorale].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals +(HP percentage difference / 2)% damage to targets with higher HP percentages that this unit's (max 10%)\n- Turn Start: gain 1 Final Power Up, 1 Damage Up, and 1 Fragile
   PL: - Zadaje +(różnica procentowa HP / 2)% obrażeń celom o wyższym procentowym HP niż własne (maks. 10%)\n- Na początku tury zyskuje 1 Wzrost Mocy Końcowej, 1 Wzrost Obrażeń i 1 Wrażliwości
488. [Status [BeastEyes_Panic] — nazwa] 맹수의 본능 - 패닉
   źródło: Bufs-a1c8p3.json :: dataList[id=BeastEyes_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BeastEyes_Panic]`
   limit: do 40 znaków
   EN: Beastly Instinct - Panic
   PL: Instynkt Bestii - Panika
489. [Status [BeastEyes_Panic] — opis] - 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이)%만큼 증가 (최대 25%)\n- 턴 시작 시, 코인 위력 증가 1, 피해량 증가 2, 취약 2 얻음\n- 다음 턴 시작 시, 자신의 잃은 체력 비율 수치만큼 정신력 회복 (최대 25)
   źródło: Bufs-a1c8p3.json :: dataList[id=BeastEyes_Panic].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals +(HP percentage difference)% damage to targets with higher HP percentages that this unit's (max 25%)\n- Turn Start: gain 1 Coin Power Up, 2 Damage Up, and 2 Fragile\n- Next Turn Start: heal SP equal to this unit's missing HP percentage (max 25)
   PL: - Zadaje +(różnica procentowa HP)% obrażeń celom o wyższym procentowym HP niż własne (maks. 25%)\n- Na początku tury zyskuje 1 Wzrost Mocy Monety, 2 Wzrostu Obrażeń i 2 Wrażliwości\n- Na początku następnej tury odzyskuje Poczytalność równą procentowi brakującego HP (maks. 25)
490. [Status [DisengageCombat] — nazwa] 전투 이탈
   źródło: Bufs-a1c8p3.json :: dataList[id=DisengageCombat].name
   kontekst: identyfikator statusu w tekstach: `[DisengageCombat]`
   limit: do 40 znaków
   EN: Escape Battle
   PL: Wycofanie z Walki
491. [Status [DisengageCombat] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)
   źródło: Bufs-a1c8p3.json :: dataList[id=DisengageCombat].desc
   limit: do 150 znaków
   EN: - Turn End: recover from Stagger and escape from the Encounter (excluding forced Staggers; does not count as death)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)
492. [Status [Chesed_Mercy] — nazwa] 헤세드의 자비
   źródło: Bufs-a1c8p3.json :: dataList[id=Chesed_Mercy].name
   kontekst: identyfikator statusu w tekstach: `[Chesed_Mercy]`
   limit: do 40 znaków
   EN: Chesed's Mercy
   PL: Miłosierdzie Cheseda
493. [Status [Chesed_Mercy] — opis] - 모든 캐릭터의 공격 레벨, 방어 레벨이 평균으로 조정됨\n- 아군 인격은 헤세드 효과가 적용된 후 공격 레벨 3, 방어 레벨 6을 추가로 얻음\n- [최초 개방 효과] 헤세드의 자비가 이번 전투 동안 지속됨
   źródło: Bufs-a1c8p3.json :: dataList[id=Chesed_Mercy].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Averages the Offense Level and Defense Level of all units\n- After the Chesed effect activates, allied Identities gain 3 Offense Levels and 6 Defense Levels\n- [First-time Unleashing Effect]: "Chesed's Mercy" lasts for the duration of this Encounter
   PL: - Poziom Ataku i Poziom Obrony wszystkich postaci są wyrównane do średniej\n- Po aktywacji efektu Cheseda sojusznicze Tożsamości zyskują dodatkowo 3 Poziomy Ataku i 6 Poziomów Obrony\n- [Efekt Pierwszego Uwolnienia] „Miłosierdzie Cheseda” trwa przez resztę walki
494. [Status [Ryoshu_Attackup] — nazwa] 난도질당한 기억
   źródło: Bufs-a1c8p3.json :: dataList[id=Ryoshu_Attackup].name
   kontekst: identyfikator statusu w tekstach: `[Ryoshu_Attackup]`
   limit: do 40 znaków
   EN: Mutilated Memory
   PL: Pocięta Pamięć
495. [Status [Ryoshu_Attackup] — opis] [료슈 특수 효과]\n- 이번 전투에서 뇌횡에게 입히는 피해량 +(현재 턴 수 x 2.5)% (최대 30%)
   źródło: Bufs-a1c8p3.json :: dataList[id=Ryoshu_Attackup].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Ryōshū Exclusive Effect]\n- Deal +(Current Turn Count x 2.5)% damage against Lei Heng in this Encounter (max 30%)
   PL: [Efekt specjalny Ryōshū]\n- W tej walce zadaje Lei Hengowi +(liczba tur x 2,5)% obrażeń (maks. 30%)
496. [Status [Honglu_EGOResourceup] — nazwa] 나의 마음과 생각...
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_EGOResourceup].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_EGOResourceup]`
   limit: do 40 znaków
   EN: My Heart, My Own Thoughts...
   PL: Moje serce i myśli...
497. [Status [Honglu_EGOResourceup] — opis] [홍루 특수 효과]\n- 이번 전투에서 자신의 스킬 공격 종료 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 1회)
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_EGOResourceup].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Hong Lu Exclusive Effect]\n- For this Encounter: after using a Skill Attack, gain 2 additional E.G.O resources of the Skill's Affinity (once per turn)
   PL: [Efekt specjalny Hong Lu]\n- W tej walce po zakończeniu ataku Umiejętnością zyskuje dodatkowo 2 Zasoby E.G.O Grzechu tej Umiejętności (1 raz na turę)
498. [Status [BudgetBulletPropellant] — nazwa] 추진탄
   źródło: Bufs-a1c8p3.json :: dataList[id=BudgetBulletPropellant].name
   kontekst: identyfikator statusu w tekstach: `[BudgetBulletPropellant]`
   limit: do 40 znaków
   EN: Propellant Ammo
   PL: Amunicja Napędowa
499. [Status [BudgetBulletPropellant] — opis] - 특수 탄환\n- 특정 스킬 사용 시 소모\n- 최댓값 : 4
   źródło: Bufs-a1c8p3.json :: dataList[id=BudgetBulletPropellant].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Spent by certain Skills\n- Max Stack: 4
   PL: - Specjalna amunicja\n- Zużywana przy użyciu określonych Umiejętności\n- Maks. stosów: 4
500. [Status [NEgoFleshSpatula_LowMorale] — nazwa] 살점 주걱
   źródło: Bufs-a1c8p3.json :: dataList[id=NEgoFleshSpatula_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[NEgoFleshSpatula_LowMorale]`
   limit: do 40 znaków
   EN: Flesh Scoop
   PL: Łopatka do Mięsa
501. [Status [NEgoFleshSpatula_LowMorale] — opis] - 사기 저하\n- 턴 시작시 출혈 5 획득, 공격 위력 증가 1 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=NEgoFleshSpatula_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 5 Bleed and 1 Attack Power Up
   PL: - Niskie Morale\n- Na początku tury zyskuje 5 Krwawienia i 1 Wzrost Mocy Ataku
502. [Status [NEgoFleshSpatula_Panic] — nazwa] 살점 주걱
   źródło: Bufs-a1c8p3.json :: dataList[id=NEgoFleshSpatula_Panic].name
   kontekst: identyfikator statusu w tekstach: `[NEgoFleshSpatula_Panic]`
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Status [NEgoFleshSpatula_Panic] — opis] - 패닉\n- 턴 시작시 출혈 10 획득, 공격 위력 증가 2 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=NEgoFleshSpatula_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 10 Bleed and 2 Attack Power Up
   PL: - Panika\n- Na początku tury zyskuje 10 Krwawienia i 2 Wzrostu Mocy Ataku
504. [Status [LeRegole_LowMorale] — nazwa] 규율
   źródło: Bufs-a1c8p3.json :: dataList[id=LeRegole_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LeRegole_LowMorale]`
   limit: do 40 znaków
   EN: Le Regole
   PL: Le Regole
505. [Status [LeRegole_LowMorale] — opis] - 사기 저하\n- 전 턴에 진동을 2 이상 부여 했다면, 나태 피해량 증가 1 획득,\n- 전 턴에 화상을 2 이상 부여 했다면, 분노 피해량 증가 1 획득,\n- 아무것도 부여하지 못했으면, 방어 레벨 감소 2 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=LeRegole_LowMorale].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If this unit inflicted 2+ Tremor last turn, gain 1 Sloth DMG Up\n- If this unit inflicted 2+ Burn last turn, gain 1 Wrath DMG Up\n- If this unit failed to inflict anything, gain 2 Defense Level Down
   PL: - Niskie Morale\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Wstrząsu, zyskuje 1 Wzrost Obrażeń Lenistwa,\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Podpalenia, zyskuje 1 Wzrost Obrażeń Gniewu,\n- Jeżeli nie nałożyła niczego, zyskuje 2 Spadek Poziomu Obrony
506. [Status [LeRegole_Panic] — nazwa] 규율
   źródło: Bufs-a1c8p3.json :: dataList[id=LeRegole_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LeRegole_Panic]`
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Status [LeRegole_Panic] — opis] - 패닉\n- 전 턴에 진동을 2 이상 부여 했다면, 나태 피해량 증가 2 획득,\n- 전 턴에 화상을 2 이상 부여 했다면, 분노 피해량 증가 2 획득,\n- 아무것도 부여하지 못했으면, 방어 레벨 감소 3 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=LeRegole_Panic].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If this unit inflicted 2+ Tremor last turn, gain 2 Sloth DMG Up\n- If this unit inflicted 2+ Burn last turn, gain 2 Wrath DMG Up\n- If this unit failed to inflict anything, gain 3 Defense Level Down
   PL: - Panika\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Wstrząsu, zyskuje 2 Wzrostu Obrażeń Lenistwa,\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Podpalenia, zyskuje 2 Wzrostu Obrażeń Gniewu,\n- Jeżeli nie nałożyła niczego, zyskuje 3 Spadek Poziomu Obrony
508. [Status [GazeReplica] — nazwa] 시선
   źródło: Bufs-a1c8p3.json :: dataList[id=GazeReplica].name
   kontekst: identyfikator statusu w tekstach: `[GazeReplica]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
509. [Status [GazeReplica] — opis] - 최대치 : 7\n- 수치 1당 가환에게 받는 피해량과 가하는 피해량 모두 +10%\n- 수치가 7이 되면 경멸로 변경됨
   źródło: Bufs-a1c8p3.json :: dataList[id=GazeReplica].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 7\n- Take and deal +10% damage from and against Jia Huan\n- At 7 Stack, converts to Contempt
   PL: - Maks. stosów: 7\n- Za każdy stos otrzymuje i zadaje +10% obrażeń od i wobec Jia Huana\n- Przy 7 stosach zamienia się w Pogardę
510. [Status [ContemptReplica] — nazwa] 경멸
   źródło: Bufs-a1c8p3.json :: dataList[id=ContemptReplica].name
   kontekst: identyfikator statusu w tekstach: `[ContemptReplica]`
   limit: do 40 znaków
   EN: Contempt
   PL: Pogarda
511. [Status [ContemptReplica] — opis] - 최대치 : 1\n- 가환에게 받는 피해량과 가하는 피해량 -50%\n- 경멸이 있는 대상은 시선을 얻을 수 없음\n- 턴 종료시 소멸
   źródło: Bufs-a1c8p3.json :: dataList[id=ContemptReplica].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take and deal -50% damage from and against Jia Huan\n- Targets with Contempt cannot gain Gaze\n- Expires at Turn End
   PL: - Maks. stosów: 1\n- Otrzymuje i zadaje -50% obrażeń od i wobec Jia Huana\n- Cele z Pogardą nie mogą zdobyć Spojrzenia\n- Znika na koniec tury
512. [Status [GraspReplica] — nazwa] 손아귀
   źródło: Bufs-a1c8p3.json :: dataList[id=GraspReplica].name
   kontekst: identyfikator statusu w tekstach: `[GraspReplica]`
   limit: do 40 znaków
   EN: Grasp
   PL: Uchwyt
513. [Status [GraspReplica] — opis] - 최대치 : 4\n- 턴 종료시 다음 턴에 속박 10 얻음\n- 턴 종료시 수치 1 감소
   źródło: Bufs-a1c8p3.json :: dataList[id=GraspReplica].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn End: gain 10 Bind next turn\n- Turn End: lose 1 Stack
   PL: - Maks. stosów: 4\n- Na koniec tury zyskuje 10 Spętań w następnej turze\n- Na koniec tury traci 1 stos
514. [Status [EgoErodeReplica] — nazwa] E.G.O 침식 - N사
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeReplica].name
   kontekst: identyfikator statusu w tekstach: `[EgoErodeReplica]`
   limit: do 40 znaków
   EN: E.G.O Corrosion - N Corp.
   PL: Korozja E.G.O - Korporacja N
515. [Status [EgoErodeReplica] — opis] - 최대치 : 10\n- 턴 시작시마다 아래 효과 적용\n· 수치만큼 정신력 감소\n· 수치 3당 공격 위력 증가 1 얻음\n- 수치가 최대치면 턴 종료시 최대 체력의 5%만큼 피해
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeReplica].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- The following effects activate at every Turn Start:\n· Lose SP by the effect's Stack\n· Gain 1 Attack Power Up for every 3 Stack\n- At Max Stack, take 5% HP damage at Turn End
   PL: - Maks. stosów: 10\n- Na początku każdej tury:\n· Traci Poczytalność równą liczbie stosów\n· Zyskuje 1 Wzrost Mocy Ataku za każde 3 stosy\n- Przy Maks. stosach otrzymuje na koniec tury 5% Maks. HP obrażeń
516. [Status [BoseProjektilReplica] — nazwa] 찢어진 추억
   źródło: Bufs-a1c8p3.json :: dataList[id=BoseProjektilReplica].name
   kontekst: identyfikator statusu w tekstach: `[BoseProjektilReplica]`
   limit: do 40 znaków
   EN: Torn Memory
   PL: Naderwane Wspomnienie
517. [Status [BoseProjektilReplica] — opis] 최대치: 7
   źródło: Bufs-a1c8p3.json :: dataList[id=BoseProjektilReplica].desc
   limit: do 120 znaków
   EN: Max Stack: 7
   PL: Maks. stosów: 7
518. [Status [EgoErodeContempt_LowMorale] — nazwa] 여린 금으로 주조한 마음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeContempt_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[EgoErodeContempt_LowMorale]`
   limit: do 40 znaków
   EN: Soft Goldcasted Heart
   PL: Serce z Miękkiego Złota
519. [Status [EgoErodeContempt_LowMorale] — opis] - 사기 저하\n- 턴 시작시 공격 위력 증가 1, 취약 1 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeContempt_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Attack Power Up and 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Mocy Ataku i 1 Wrażliwości
520. [Status [EgoErodeContempt_Panic] — nazwa] 여린 금으로 주조한 마음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeContempt_Panic].name
   kontekst: identyfikator statusu w tekstach: `[EgoErodeContempt_Panic]`
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Status [EgoErodeContempt_Panic] — opis] - 패닉\n- 턴 시작시 공격 위력 증가 2, 취약 2 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeContempt_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Attack Power Up and 2 Fragile
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 2 Wrażliwości
522. [Status [EgoErodeMemory_LowMorale] — nazwa] 새 시대로 향하는 마음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeMemory_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[EgoErodeMemory_LowMorale]`
   limit: do 40 znaków
   EN: Heart Toward the New Era
   PL: Serce Ku Nowej Erze
523. [Status [EgoErodeMemory_LowMorale] — opis] - 사기 저하\n- 공격 적중시 자신의 정신력 3 소모, 침잠 2 부여
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeMemory_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- On Hit, consume 3 SP on self to inflict 2 Sinking
   PL: - Niskie Morale\n- Przy trafieniu traci 3 Poczytalności i nakłada 2 Zatonięcia
524. [Status [EgoErodeMemory_Panic] — nazwa] 새 시대로 향하는 마음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeMemory_Panic].name
   kontekst: identyfikator statusu w tekstach: `[EgoErodeMemory_Panic]`
   (powtórzenie elementu 522 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Status [EgoErodeMemory_Panic] — opis] - 패닉\n- 공격 적중시 침잠 3 부여, 침잠 1 얻음
   źródło: Bufs-a1c8p3.json :: dataList[id=EgoErodeMemory_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- On Hit, inflict 3 Sinking and gain 1 Sinking
   PL: - Panika\n- Przy trafieniu nakłada 3 Zatonięcia i zyskuje 1 Zatonięcie
526. [Status [PileObedient] — nazwa] 쌓이는 순종
   źródło: Bufs-a1c8p3.json :: dataList[id=PileObedient].name
   kontekst: identyfikator statusu w tekstach: `[PileObedient]`
   limit: do 40 znaków
   EN: Heaping Obedience
   PL: Narastające Uposłuszeństwo
527. [Status [PileObedient] — opis] - 턴 종료 시 수치가 3이면, 다음 턴에 이 효과가 공허한 순종으로 변경됨
   źródło: Bufs-a1c8p3.json :: dataList[id=PileObedient].desc
   limit: do 120 znaków
   EN: - Turn End: at 3 Stack, convert this effect to Hollow Obedience next turn
   PL: - Na koniec tury przy 3 stosach efekt zamienia się w następną turę w Puste Uposłuszeństwo
528. [Status [Obedient] — nazwa] 공허한 순종
   źródło: Bufs-a1c8p3.json :: dataList[id=Obedient].name
   kontekst: identyfikator statusu w tekstach: `[Obedient]`
   limit: do 40 znaków
   EN: Hollow Obedience
   PL: Puste Uposłuszeństwo
529. [Status [Obedient] — opis] - 가모와 합 진행 시 합 위력 -2\n- 이 캐릭터의 정신력이 45가 되거나 수치가 0이 되면 해제됨\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c8p3.json :: dataList[id=Obedient].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power -2 in Clashes against Jia Mu\n- Expires when this unit's SP reaches 45, or when the Stack drops to 0\n- Turn End: lose 1 Stack
   PL: - W Starciu z Jia Mu Moc Starcia -2\n- Znika, gdy Poczytalność tej postaci osiągnie 45 lub wartość spadnie do 0\n- Na koniec tury maleje o 1
530. [Status [ExpensiveJade] — nazwa] 보옥요람
   źródło: Bufs-a1c8p3.json :: dataList[id=ExpensiveJade].name
   kontekst: identyfikator statusu w tekstach: `[ExpensiveJade]`
   limit: do 40 znaków
   EN: Precious Jade's Cradle
   PL: Kołyska Jadeitu
531. [Status [ExpensiveJade] — opis] - 버프, 체력, 정신력이 갱신되지 않는 행동 불가능 상태가 되고, 이 캐릭터와 연결된 보옥이 생성됨
   źródło: Bufs-a1c8p3.json :: dataList[id=ExpensiveJade].desc
   limit: do 170 znaków
   EN: - Enter an 'Immobilized' state where this unit's buffs, HP, and SP cannot be changed. Forms a Precious Jade connected to this unit
   PL: - Przechodzi w stan „Unieruchomienia”, w którym buffy, HP i Poczytalność nie mogą się zmieniać. Tworzy Jadeit połączony z tą postacią
532. [Status [FamilyTreasure] — nazwa] 폭발유희
   źródło: Bufs-a1c8p3.json :: dataList[id=FamilyTreasure].name
   kontekst: identyfikator statusu w tekstach: `[FamilyTreasure]`
   limit: do 40 znaków
   EN: Explosive Amusement
   PL: Wybuchowa Zabawa
533. [Status [FamilyTreasure] — opis] - 턴 종료 시\n· 기본 값 : 1\n· 이 유닛과 연결된 캐릭터의 체력이 최대 체력의 25%만큼 회복, 정신력 20 감소\n· 수치 1 증가\n· 수치가 3이면, 자폭 스킬을 사용함. 이 캐릭터가 자폭으로 사망한 경우, 갇혀있던 캐릭터에게 다음 턴에 공허한 순종 3을 부여함
   źródło: Bufs-a1c8p3.json :: dataList[id=FamilyTreasure].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Turn End:\n· Base Stack: 1\n· The unit connected to this unit heals 25% HP and loses 20 SP\n· Gain 1 Stack\n· At 3 Stack, use a self-detonation Skill. If this unit is killed by self-detonation, inflict the caged character with 3 Hollow Obedience next turn
   PL: - Na koniec tury\n· Wartość bazowa: 1\n· Postać połączona z tą jednostką leczy 25% HP i traci 20 Poczytalności\n· Wartość rośnie o 1\n· Przy wartości 3 używa Umiejętności samozniszczenia. Jeżeli ta jednostka ginie od samozniszczenia, nakłada na uwięzioną postać 3 Pustego Uposłuszeństwa w następnej turze
534. [Status [OutpouringAnger] — nazwa] 발악
   źródło: Bufs-a1c8p3.json :: dataList[id=OutpouringAnger].name
   kontekst: identyfikator statusu w tekstach: `[OutpouringAnger]`
   limit: do 40 znaków
   EN: Rampage
   PL: Ostatnie Zrywy
535. [Status [OutpouringAnger] — opis] - ‘너희는 그 눈의 힘과 특별함을 아직도 한참을 모르고 있구나’ 스킬의 메인 공격 대상이 홍루면, 해당 스킬의 모든 코인이 스킬 효과를 무시하고 파괴 불가 코인이 됨
   źródło: Bufs-a1c8p3.json :: dataList[id=OutpouringAnger].desc
   limit: do 250 znaków
   EN: - If the 'You do not know the fathoms of the eye's powers, its special nature' Skill's main target is Hong Lu, ignore all Skill effects and convert all Coins on that Skill to Unbreakable Coins
   PL: - Jeżeli głównym celem Umiejętności „Jeszcze nie pojmujesz, jak głęboka jest moc tego oka i jego szczególna natura” jest Hong Lu, wszystkie Monety tej Umiejętności ignorują efekty Umiejętności i stają się Niezniszczalnymi Monetami
536. [Status [Honglu_Xi] — nazwa] 기쁨
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Xi].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Xi]`
   limit: do 40 znaków
   EN: Happiness
   PL: Radość
537. [Status [Honglu_Xi] — opis] - 홍루의 합 위력 +1\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 페이즈에서 1회 보옥 상태가 되지 않음. 보옥 상태로 만드는 스킬과 합 진행 시 합 위력 +5, 해당 스킬과 합에서 승리한 경우, 보옥 상태가 되지 않고 자신의 흐트러짐 해제, 가모의 정신력 10 감소, 가모에게 취약 2 부여\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Xi].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Clash Power +1\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Nullfies the effect that turns this unit into a Precious Jade once. When clashing against Skills that turns this unit into a Precious Jade, Clash Power +5; if this unit wins that Clash, this unit does not become a Precious Jade, recovers from Stagger, reduces Jia Mu's SP by 10, and inflicts 2 Fragile against Jia Mu\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Starcia Hong Lua +1\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\n- Jednorazowo unieważnia przemianę w Jadeit; w Starciu z Umiejętnością przemieniającą w Jadeit Moc Starcia +5; po wygranej nie następuje przemiana, oszołomienie zostaje wyleczone, Poczytalność Jia Mu maleje o 10, a Jia Mu otrzymuje 2 Wrażliwości\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
538. [Status [Honglu_Le] — nazwa] 기쁨, 즐거움
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Le].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Le]`
   limit: do 40 znaków
   EN: Happiness, Joy
   PL: Radość, Rozkosz
539. [Status [Honglu_Le] — opis] - 홍루의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Le].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +1\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +1\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
540. [Status [Honglu_Ai] — nazwa] 기쁨, 즐거움, 슬픔
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Ai].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Ai]`
   limit: do 40 znaków
   EN: Happiness, Joy, Sorrow
   PL: Radość, Rozkosz, Smutek
541. [Status [Honglu_Ai] — opis] - 홍루의 최종 위력 +3\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Ai].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +3\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +3\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury 1 Wzrost Mocy Ataku w następnej turze (raz na turę)\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
542. [Status [Honglu_Nu] — nazwa] 기쁨, 즐거움, 슬픔, 분노
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Nu].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Nu]`
   limit: do 50 znaków
   EN: Happiness, Joy, Sorrow, Wrath
   PL: Radość, Rozkosz, Smutek, Gniew
543. [Status [Honglu_Nu] — opis] - 홍루의 최종 위력 +5\n- 매 턴 시작 시 모든 아군의 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 전투에서 누적으로 잃은 체력 비율의 30%만큼 피해량 증가 (최대 100%)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Nu].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +5\n- Allies heal 5 SP at every Turn Start (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Increases damage dealt by 30% of the total HP percentage this unit has cumulatively lost during this Encounter (max 100%)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +5\n- Na początku każdej tury wszyscy sojusznicy regenerują 5 Poczytalności (łącznie z tą jednostką)\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury 1 Wzrost Mocy Ataku w następnej turze (raz na turę)\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\n- Zadawane obrażenia rosną o 30% łącznie utraconego procentu HP w tej walce (maks. 100%)\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
544. [Status [SupremeEternalLife] — nazwa] 지고한 불사
   źródło: Bufs-a1c8p3.json :: dataList[id=SupremeEternalLife].name
   kontekst: identyfikator statusu w tekstach: `[SupremeEternalLife]`
   limit: do 40 znaków
   EN: Sublime Immortality
   PL: Wzniosła Nieśmiertelność
545. [Status [SupremeEternalLife] — opis] - 턴 시작 시 가모의 본체와 모든 부위에 각 최대 체력의 5%만큼 보호막 부여
   źródło: Bufs-a1c8p3.json :: dataList[id=SupremeEternalLife].desc
   limit: do 120 znaków
   EN: - Turn Start: Jia Mu's Core and every Part gain 5% of each of their max HP as Shield
   PL: - Na początku tury nakłada korpusowi i wszystkim częściom Jia Mu Tarczę równą 5% Maks. HP każdego z nich
546. [Status [ImperfectEternalLife] — nazwa] 불완전한 불사
   źródło: Bufs-a1c8p3.json :: dataList[id=ImperfectEternalLife].name
   kontekst: identyfikator statusu w tekstach: `[ImperfectEternalLife]`
   limit: do 40 znaków
   EN: Imperfect Immortality
   PL: Niedoskonała Nieśmiertelność
547. [Status [ImperfectEternalLife] — opis] - 가모의 특정 스킬에 피격 시 흡수 당함\n- 이 효과가 가모에게 부여된 경우, 수치당 취약 1 얻고, 수치가 5면, 흐트러짐 상태가 됨
   źródło: Bufs-a1c8p3.json :: dataList[id=ImperfectEternalLife].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Absorbed when struck by certain Skills of Jia Mu\n- If this effect was inflicted against Jia Mu, gain 1 Fragile per Stack; at 5 Stack, become Staggered
   PL: - Jest absorbowany przy trafieniu określonymi Umiejętnościami Jia Mu\n- Jeżeli ten efekt nałożono na Jia Mu, zyskuje 1 Wrażliwości za każdy stos; przy 5 stosach przechodzi w stan Oszołomienia
548. [Status [GoldenBoughSync] — nazwa] 부감응
   źródło: Bufs-a1c8p3.json :: dataList[id=GoldenBoughSync].name
   kontekst: identyfikator statusu w tekstach: `[GoldenBoughSync]`
   limit: do 40 znaków
   EN: Malattunement
   PL: Zdegradowane Dostrojenie
549. [Status [GoldenBoughSync] — opis] - 기본 공격 레벨 +2, 기본 방어 레벨 +2
   źródło: Bufs-a1c8p3.json :: dataList[id=GoldenBoughSync].desc
   limit: do 120 znaków
   EN: - Base Offense Level +2, Base Defense Level +2
   PL: - Podstawowy Poziom Ataku +2, Podstawowy Poziom Obrony +2
550. [Status [GoldenBoughSyncDistorted] — nazwa] 괴력난신
   źródło: Bufs-a1c8p3.json :: dataList[id=GoldenBoughSyncDistorted].name
   kontekst: identyfikator statusu w tekstach: `[GoldenBoughSyncDistorted]`
   limit: do 60 znaków
   EN: Supernatural, Strength, Chaos, and Spirits
   PL: Demoniczna Siła i Chaotyczne Duchy
551. [Status [GoldenBoughSyncDistorted] — opis] - 기본 공격 레벨 +4, 기본 방어 레벨 +4
   źródło: Bufs-a1c8p3.json :: dataList[id=GoldenBoughSyncDistorted].desc
   limit: do 120 znaków
   EN: - Base Offense Level +4, Base Defense Level +4
   PL: - Podstawowy Poziom Ataku +4, Podstawowy Poziom Obrony +4
552. [Status [LastingHongwonWill_LowMorale] — nazwa] 계승된 홍원의 뜻
   źródło: Bufs-a1c8p3.json :: dataList[id=LastingHongwonWill_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LastingHongwonWill_LowMorale]`
   limit: do 40 znaków
   EN: Inherited Will of Hongyuan
   PL: Odziedziczona Wola Hongyuan
553. [Status [LastingHongwonWill_LowMorale] — opis] - 사기저하\n- 공격 위력 증가 2, 속박 1 얻음\n- 홍루에게 몸통 부위가 합 패배 시 다음 턴에 몸통 부위가 피해량 증가 1, 취약 1 얻음 (턴 당 1회)
   źródło: Bufs-a1c8p3.json :: dataList[id=LastingHongwonWill_LowMorale].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 2 Attack Power Up and 1 Bind\n- When the Body Part loses a Clash against Hong Lu: the Body Part gains 1 Damage Up and 1 Fragile next turn (once per turn)
   PL: - Niskie Morale\n- Zyskuje 2 Wzrostu Mocy Ataku i 1 Spętanie\n- Gdy część Tułowia przegra Starcie z Hong Lu, część Tułowia zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości w następnej turze (1 raz na turę)
554. [Status [LastingHongwonWill_Panic] — nazwa] 계승된 홍원의 뜻
   źródło: Bufs-a1c8p3.json :: dataList[id=LastingHongwonWill_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LastingHongwonWill_Panic]`
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Status [LastingHongwonWill_Panic] — opis] - 패닉\n- 공격 위력 증가 2, 속박 2 얻음\n- 홍루에게 몸통 부위가 합 패배 시 다음 턴에 몸통 부위가 피해량 증가 2, 취약 2 얻음 (턴 당 1회)
   źródło: Bufs-a1c8p3.json :: dataList[id=LastingHongwonWill_Panic].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Attack Power Up and 2 Bind\n- When the Body Part loses a Clash against Hong Lu: the Body Part gains 2 Damage Up and 2 Fragile next turn (once per turn)
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Ataku i 2 Spętań\n- Gdy część Tułowia przegra Starcie z Hong Lu, część Tułowia zyskuje 2 Wzrostu Obrażeń i 2 Wrażliwości w następnej turze (1 raz na turę)
556. [Status [LongLastingHongwonWill_LowMorale] — nazwa] 유구히 계승될 홍원의 뜻
   źródło: Bufs-a1c8p3.json :: dataList[id=LongLastingHongwonWill_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LongLastingHongwonWill_LowMorale]`
   limit: do 60 znaków
   EN: Infinitely Bequeathing Will of Hongyuan
   PL: Wiecznie Przekazywana Wola Hongyuan
557. [Status [LongLastingHongwonWill_LowMorale] — opis] - 사기저하\n- 공격 위력 증가 2, 취약 1 얻음\n- 자신이 생성한 유닛이 방어 레벨 감소 3 얻음\n- 가하는 피해량 20% 증가. 가마 부위의 체력이 0이면, 대신 가하는 피해량 10% 감소
   źródło: Bufs-a1c8p3.json :: dataList[id=LongLastingHongwonWill_LowMorale].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 2 Attack Power Up and 1 Fragile\n- Units generated by this unit gain 3 Defense Level Down\n- Deal +20% damage. If the Palanquin Part's HP drops to 0, deal -10% damage instead
   PL: - Niskie Morale\n- Zyskuje 2 Wzrostu Mocy Ataku i 1 Wrażliwości\n- Jednostki wytworzone przez tę jednostkę zyskują 3 Spadek Poziomu Obrony\n- Zadaje +20% obrażeń. Jeżeli HP części Lektyki spadnie do 0, zamiast tego zadaje -10% obrażeń
558. [Status [LongLastingHongwonWill_Panic] — nazwa] 유구히 계승될 홍원의 뜻
   źródło: Bufs-a1c8p3.json :: dataList[id=LongLastingHongwonWill_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LongLastingHongwonWill_Panic]`
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Status [LongLastingHongwonWill_Panic] — opis] - 패닉\n- 공격 위력 증가 2, 취약 2 얻음\n- 자신이 생성한 유닛이 방어 레벨 감소 6 얻음\n- 가하는 피해량 30% 증가. 가마 부위의 체력이 0이면, 대신 가하는 피해량 15% 감소
   źródło: Bufs-a1c8p3.json :: dataList[id=LongLastingHongwonWill_Panic].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Attack Power Up and 2 Fragile\n- Units generated by this unit gain 6 Defense Level Down\n- Deal +30% damage. If the Palanquin Part's HP drops to 0, deal -15% damage instead
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Ataku i 2 Wrażliwości\n- Jednostki wytworzone przez tę jednostkę zyskują 6 Spadek Poziomu Obrony\n- Zadaje +30% obrażeń. Jeżeli HP części Lektyki spadnie do 0, zamiast tego zadaje -15% obrażeń
560. [Status [YisangParryGubo] — nazwa] 책임감
   źródło: Bufs-a1c8p3.json :: dataList[id=YisangParryGubo].name
   kontekst: identyfikator statusu w tekstach: `[YisangParryGubo]`
   limit: do 40 znaków
   EN: Responsibility
   PL: Poczucie Obowiązku
561. [Status [YisangParryGubo] — opis] 구보와 합을 진행할 때, 합 위력 +2
   źródło: Bufs-a1c8p3.json :: dataList[id=YisangParryGubo].desc
   limit: do 120 znaków
   EN: In Clashes against Gubo, Clash Power +2
   PL: W Starciach z Gubo Moc Starcia +2
562. [Status [HongluParryGahwan] — nazwa] 마주하려는 의지
   źródło: Bufs-a1c8p3.json :: dataList[id=HongluParryGahwan].name
   kontekst: identyfikator statusu w tekstach: `[HongluParryGahwan]`
   limit: do 40 znaków
   EN: The Will to Confront
   PL: Wola Konfrontacji
563. [Status [HongluParryGahwan] — opis] 가환과 합을 진행할 때, 합 위력 +2
   źródło: Bufs-a1c8p3.json :: dataList[id=HongluParryGahwan].desc
   limit: do 120 znaków
   EN: In Clashes against Jia Huan, Clash Power +2
   PL: W Starciach przeciwko Jia Huan: Moc Starcia +2
564. [Status [GahwanEgoContempt] — nazwa] 불안정 E.G.O 감응 - 경멸
   źródło: Bufs-a1c8p3.json :: dataList[id=GahwanEgoContempt].name
   kontekst: identyfikator statusu w tekstach: `[GahwanEgoContempt]`
   limit: do 50 znaków
   EN: Volatile E.G.O Attunement - Contempt
   PL: Niestabilne Dostrojenie E.G.O - Pogarda
565. [Status [GahwanEgoContempt] — opis] - N사에서 추출한 E.G.O 장비. 적성에는 맞으나 경험은 적어 아직 사용에 익숙하지 않다.\n- 최대값 : 5\n- 공격 레벨, 방어 레벨 -7\n- 합 승리 시 수치 1 증가\n- 수치 1 당 공격 레벨 1 감소, 방어 레벨 1 증가\n- 수치가 최대치면, 다음 턴에 보호 2를 얻고 수치 0으로 초기화
   źródło: Bufs-a1c8p3.json :: dataList[id=GahwanEgoContempt].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - E.G.O Gear extracted by N Corp. While the user meets the aptitude requirements, the lack of experience may cause issues.\n- Max Stack: 5\n- Offense Level, Defense Level -7\n- On Clash Win, gain 1 Stack\n- Lose 1 Offense Level and gain 1 Defense Level for every Stack\n- At Max Stack: next turn, gain 2 Protection and reset the Stack to 0
   PL: - E.G.O wyekstrahowane przez Korporację N. Użytkownik spełnia wymogi predyspozycji, ale brak doświadczenia może sprawiać trudności.\n- Maks. stosów: 5\n- Poziom Ataku i Poziom Obrony -7\n- Po wygranym Starciu zyskuje 1 stos\n- Traci 1 Poziom Ataku i zyskuje 1 Poziom Obrony za każdy stos\n- Przy Maks. stosach zyskuje w następnej turze 2 Ochrony i resetuje liczbę stosów do 0
566. [Status [GuboEgoShooter] — nazwa] 불안정 E.G.O 감응 - 흉탄
   źródło: Bufs-a1c8p3.json :: dataList[id=GuboEgoShooter].name
   kontekst: identyfikator statusu w tekstach: `[GuboEgoShooter]`
   limit: do 60 znaków
   EN: Volatile E.G.O Attunement - Fell Bullet
   PL: Niestabilne Dostrojenie E.G.O - Zabójczy Pocisk
567. [Status [GuboEgoShooter] — opis] - N사에서 추출한 E.G.O 장비. 적성에는 맞으나 경험은 적어 아직 사용에 익숙하지 않다.\n- 최대값 : 5\n- 공격 레벨, 방어 레벨  -2\n- 합 패배 시 수치 1 증가\n- 수치 1 당 공격 레벨 1 증가, 방어 레벨 1 감소\n- 수치가 최대치면, 다음 턴에 피해량 증가 2를 얻고 수치 0으로 초기화
   źródło: Bufs-a1c8p3.json :: dataList[id=GuboEgoShooter].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - E.G.O Gear extracted by N Corp. While the user meets the aptitude requirements, the lack of experience may cause issues.\n- Max Stack: 5\n- Offense Level, Defense Level -2\n- On Clash Lose, gain 1 Stack\n- Gain 1 Offense Level and lose 1 Defense Level for every Stack\n- At Max Stack: next turn, gain 2 Damage Up and reset the Stack to 0
   PL: - E.G.O wyekstrahowane przez Korporację N. Użytkownik spełnia wymogi predyspozycji, ale brak doświadczenia może sprawiać trudności.\n- Maks. stosów: 5\n- Poziom Ataku i Poziom Obrony -2\n- Po przegranej w Starciu zyskuje 1 stos\n- Zyskuje 1 Poziom Ataku i traci 1 Poziom Obrony za każdy stos\n- Przy Maks. stosach zyskuje w następnej turze 2 Wzrost Obrażeń i resetuje liczbę stosów do 0
568. [Status [FellBulletMarkReplica] — nazwa] 징표
   źródło: Bufs-a1c8p3.json :: dataList[id=FellBulletMarkReplica].name
   kontekst: identyfikator statusu w tekstach: `[FellBulletMarkReplica]`
   limit: do 40 znaków
   EN: Stigmatized
   PL: Napiętnowany
569. [Status [FellBulletMarkReplica] — opis] - 구보의 표적이 됨\n- 턴 종료시 제거됨
   źródło: Bufs-a1c8p3.json :: dataList[id=FellBulletMarkReplica].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Tageted by Gubo\n- Expires at Turn End
   PL: - Staje się celem Gubo\n- Znika na koniec tury
570. [Status [Honglu_Xi_Mirror] — nazwa] 기쁨
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Xi_Mirror].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Xi_Mirror]`
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Status [Honglu_Xi_Mirror] — opis] - 합 위력 +1\n- 이번 페이즈에서 1회 보옥 상태가 되지 않음. 보옥 상태로 만드는 스킬과 합 진행 시 합 위력 +5, 해당 스킬과 합에서 승리한 경우, 보옥 상태가 되지 않고 자신의 흐트러짐 해제, 가모의 정신력 10 감소, 가모에게 취약 2 부여\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Xi_Mirror].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power +1\n- Nullfies the effect that turns this unit into a Precious Jade once. When clashing against Skills that turns this unit into a Precious Jade, Clash Power +5; if this unit wins that Clash, this unit does not become a Precious Jade, recovers from Stagger, reduces Jia Mu's SP by 10, and inflicts 2 Fragile against Jia Mu\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Starcia +1\n- Raz w tej fazie nie staje się Jadeitem. W Starciu z Umiejętnościami zamieniającymi w Jadeit Moc Starcia +5; przy wygranej w takim Starciu nie staje się Jadeitem, dochodzi do siebie z Oszołomienia, Poczytalność Jia Mu spada o 10, a Jia Mu otrzymuje 2 Wrażliwości\nWygrana w Starciu z Jia Mu: zyskuje po 1 zasobu E.G.O losowych atrybutów spośród 3 najmniej posiadanych, łącznie 3 zasoby
572. [Status [Honglu_Le_Mirror] — nazwa] 기쁨, 즐거움
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Le_Mirror].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Le_Mirror]`
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Status [Honglu_Le_Mirror] — opis] - 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Le_Mirror].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +1\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa +1\n- Po wygranej w Starciu 1 sojusznik z najniższą Poczytalnością (wliczając siebie) odzyskuje 5 Poczytalności\nWygrana w Starciu z Jia Mu: zyskuje po 1 zasobu E.G.O losowych atrybutów spośród 3 najmniej posiadanych, łącznie 3 zasoby
574. [Status [Honglu_Ai_Mirror] — nazwa] 기쁨, 즐거움, 슬픔
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Ai_Mirror].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Ai_Mirror]`
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Status [Honglu_Ai_Mirror] — opis] - 최종 위력 +3\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Ai_Mirror].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +3\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa +3\n- Po wygranej w Starciu 1 sojusznik z najniższą Poczytalnością (wliczając siebie) odzyskuje 5 Poczytalności\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury w następnej turze 1 Wzrost Mocy Ataku (raz na turę)\nWygrana w Starciu z Jia Mu: zyskuje po 1 zasobu E.G.O losowych atrybutów spośród 3 najmniej posiadanych, łącznie 3 zasoby
576. [Status [Honglu_Nu_Mirror] — nazwa] 기쁨, 즐거움, 슬픔, 분노
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Nu_Mirror].name
   kontekst: identyfikator statusu w tekstach: `[Honglu_Nu_Mirror]`
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Status [Honglu_Nu_Mirror] — opis] - 최종 위력 +5\n- 매 턴 시작 시 모든 아군의 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 누적으로 잃은 체력 비율의 30%만큼 피해량 증가 (최대 100%)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs-a1c8p3.json :: dataList[id=Honglu_Nu_Mirror].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +5\n- Allies heal 5 SP at every Turn Start (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- Increases damage dealt by 30% of the total HP percentage this unit has cumulatively lost during this Encounter (max 100%)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa +5\n- Na początek każdej tury wszyscy sojusznicy (wliczając siebie) odzyskują 5 Poczytalności\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury w następnej turze 1 Wzrost Mocy Ataku (raz na turę)\n- Zadawane obrażenia rosną o 30% skumulowanego procentu utraconego HP w tej walce (maks. 100%)\nWygrana w Starciu z Jia Mu: zyskuje po 1 zasobu E.G.O losowych atrybutów spośród 3 najmniej posiadanych, łącznie 3 zasoby

## Statusy i efekty bojowe — Bufs-a1c9114
- plik gry: `Bufs-a1c9114.json`

578. [Status [A1c971a] — nazwa] 끓어오르는 분노
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971a].name
   kontekst: identyfikator statusu w tekstach: `[A1c971a]`
   limit: do 40 znaków
   EN: Boiling Wrath
   PL: Wrzący Gniew
579. [Status [A1c971a] — opis] 매 턴 시작 시, 턴 수만큼 화상을 얻음.
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971a].desc
   limit: do 120 znaków
   EN: Every Turn Start: gain Burn equal to Turn Count
   PL: Na początku każdej tury zyskuje Podpalenie równe liczbie tur.
580. [Status [A1c971b] — nazwa] 퍼져나가는 우울
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971b].name
   kontekst: identyfikator statusu w tekstach: `[A1c971b]`
   limit: do 40 znaków
   EN: Propagating Gloom
   PL: Rozprzestrzeniająca się Posępność
581. [Status [A1c971b] — opis] 턴 종료 시, 수치가 1이라면 체력이 가장 적은 적에게 자신의 현재 체력만큼 피해를 입히고 사망함\n턴 종료 시, 1 감소
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971b].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: at 1 Stack, inflict damage equal to this unit's current HP against the enemy with the least HP, then die\nReduced by 1 at Turn End
   PL: Na koniec tury, jeżeli wartość wynosi 1, zadaje wrogowi z najmniejszym HP obrażenia równe swojemu obecnemu HP i ginie\nNa koniec tury maleje o 1
582. [Status [A1c971c] — nazwa] 계속되는 탐식
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971c].name
   kontekst: identyfikator statusu w tekstach: `[A1c971c]`
   limit: do 40 znaków
   EN: Perpetuating Gluttony
   PL: Nieustanne Obżarstwo
583. [Status [A1c971c] — opis] 턴 시작 시, 진행된 턴 수 2당 체력 회복량 증가 1 얻음 (최대 5)\n턴 시작 시, 회복한 체력량 10당 피해량 증가 1, 합 위력 증가 1 얻음 (최대 5)\n\n회복한 체력량: {0}
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971c].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Turn Start: gain 1 HP heal boost every 2 turns (max 5)\nTurn Start: gain 1 Damage Up and 1 Clash Power Up for every 10 HP healed (max 5)\n\nHP Healed: {0}
   PL: Na początku tury zyskuje 1 Wzrost Leczenia HP za każde 2 tury (maks. 5)\nNa początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy Starcia za każde 10 wyleczonych HP (maks. 5)\n\nWyleczone HP: {0}
584. [Status [A1c971d] — nazwa] 뱉어내는 호흡
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971d].name
   kontekst: identyfikator statusu w tekstach: `[A1c971d]`
   limit: do 40 znaków
   EN: Gasping Breath
   PL: Dyszący Oddech
585. [Status [A1c971d] — opis] 호흡을 얻을 때, 호흡 추가 3 얻음 혹은 호흡 횟수 추가 2 증가
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971d].desc
   limit: do 120 znaków
   EN: When gaining Poise, gain 3 additional Poise or +2 additional Poise Count
   PL: Przy zdobyciu Oddechu zyskuje dodatkowo 3 Oddechu lub +2 Licznika Oddechu
586. [Status [A1c971e] — nazwa] 상처속의 상처
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971e].name
   kontekst: identyfikator statusu w tekstach: `[A1c971e]`
   limit: do 40 znaków
   EN: Wounded Wound
   PL: Rana w Ranę
587. [Status [A1c971e] — opis] 적중시, 출혈 추가 2 부여 혹은 출혈 횟수 추가 1 증가
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971e].desc
   limit: do 120 znaków
   EN: On Hit, inflict 2 additional Bleed or +1 additional Bleed Count
   PL: Przy trafieniu nakłada 2 dodatkowe Krwawienia lub zwiększa Licznik Krwawienia o +1
588. [Status [A1c971f] — nazwa] 게으른 나태
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971f].name
   kontekst: identyfikator statusu w tekstach: `[A1c971f]`
   limit: do 40 znaków
   EN: Lazy Sloth
   PL: Leniwe Lenistwo
589. [Status [A1c971f] — opis] 턴 종료 시 1 감소.\n0이 되면, EX클리어 실패.
   źródło: Bufs-a1c9114.json :: dataList[id=A1c971f].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduced by 1 at Turn End.\nFails Extra Condition at 0
   PL: Na koniec tury maleje o 1.\nPrzy 0 — niepowodzenie Warunku Dodatkowego.

## Statusy i efekty bojowe — Bufs-a1c9116
- plik gry: `Bufs-a1c9116.json`

590. [Status [BurstAgility] — nazwa] 주살【신속】
   źródło: Bufs-a1c9116.json :: dataList[id=BurstAgility].name
   kontekst: identyfikator statusu w tekstach: `[BurstAgility]`
   limit: do 40 znaków
   EN: Deathrite【Haste】
   PL: Obrzęd Śmierci 【Haste】
591. [Status [BurstAgility] — opis] - 기본값 : 3\n- 속도가 10 이상인 대상에게 공격 스킬로 피격되어 파열이 발동될 때 1 감소, 자신의 파열 횟수 1 증가\n- 수치가 0이 될 때, (파열 위력) 만큼 탐식 속성 피해를 받고 소멸\n※ 이 효과는 갱신되지 않음
   źródło: Bufs-a1c9116.json :: dataList[id=BurstAgility].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- When getting Rupture triggered by getting hit by an Attack Skill from a target with 10+ Speed, lose 1 Stack and gain +1 Rupture Count\n- At 0 Stack, take Gluttony damage equal to Rupture Potency on self; then, this effect expires\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: - Wartość bazowa: 3\n- Gdy Rozdarcie zostanie wywołane przez trafienie Umiejętnością ataku celu o Szybkości 10 lub więcej, maleje o 1, a Licznik Rozdarcia rośnie o 1\n- Przy wartości 0 otrzymuje obrażenia Obżarstwa równe Mocy Rozdarcia i znika\n※ Ten efekt nie odświeża się
592. [Status [BurstAgility] — podsumowanie] 조건 만족시, 탐식 추가 피해 입힘
   źródło: Bufs-a1c9116.json :: dataList[id=BurstAgility].summary
   limit: do 120 znaków
   EN: If conditions are met: inflict Gluttony bonus damage
   PL: Po spełnieniu warunków otrzymuje dodatkowe obrażenia Obżarstwa
593. [Status [LegStrength] — nazwa] 각력【묘】
   źródło: Bufs-a1c9116.json :: dataList[id=LegStrength].name
   kontekst: identyfikator statusu w tekstach: `[LegStrength]`
   limit: do 40 znaków
   EN: Strider【Mao】
   PL: Biegacz【Mao】
594. [Status [LegStrength] — opis] 최댓값: 3\n턴 종료 시 다음 턴에 신속을 5 얻음\n턴 종료 시 1 감소
   źródło: Bufs-a1c9116.json :: dataList[id=LegStrength].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nTurn End: gain 5 Haste next turn\nReduced by 1 at Turn End
   PL: Maks. stosów: 3\nNa koniec tury zyskuje 5 Pośpiechu w następnej turze\nNa koniec tury maleje o 1
595. [Status [LegStrength] — podsumowanie] 조건 만족시, 탐식 추가 피해 입힘
   źródło: Bufs-a1c9116.json :: dataList[id=LegStrength].summary
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Status [DarkBeast_LowMorale] — nazwa] 암수
   źródło: Bufs-a1c9116.json :: dataList[id=DarkBeast_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DarkBeast_LowMorale]`
   limit: do 40 znaków
   EN: Deception
   PL: Podstęp
597. [Status [DarkBeast_LowMorale] — opis] - 사기 저하\n- 자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, 대상에게 피해량 +10%
   źródło: Bufs-a1c9116.json :: dataList[id=DarkBeast_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If this unit's Speed is faster than the target's or when using an Unopposed Attack, deal +10% damage against the target
   PL: - Niskie Morale\n- Jeżeli Szybkość tej jednostki jest większa niż celu lub przy Ataku Jednostronnym, zadaje +10% obrażeń celowi
598. [Status [DarkBeast_Panic] — nazwa] 암수
   źródło: Bufs-a1c9116.json :: dataList[id=DarkBeast_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DarkBeast_Panic]`
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Status [DarkBeast_Panic] — opis] - 패닉\n- 자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, 대상에게 피해량 +20%, 자신의 속도가 대상보다 빠르면, 받는 피해량 -20%
   źródło: Bufs-a1c9116.json :: dataList[id=DarkBeast_Panic].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- If this unit's Speed is faster than the target's or when using an Unopposed Attack, deal +20% damage against the target; if this unit's Speed is faster than the target's, take -20% damage
   PL: - Panika\n- Jeżeli Szybkość tej jednostki jest większa niż celu lub przy Ataku Jednostronnym, zadaje +20% obrażeń celowi; jeżeli Szybkość jest większa, otrzymuje -20% obrażeń
600. [Status [RepressedMurderousIntend] — nazwa] 억눌린 살기
   źródło: Bufs-a1c9116.json :: dataList[id=RepressedMurderousIntend].name
   kontekst: identyfikator statusu w tekstach: `[RepressedMurderousIntend]`
   limit: do 40 znaków
   EN: Repressed Bloodthirst
   PL: Stłumiona Krwiożerczość
601. [Status [RepressedMurderousIntend] — opis] 기본 공격 레벨 -10, 기본 방어 레벨 -10
   źródło: Bufs-a1c9116.json :: dataList[id=RepressedMurderousIntend].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -10\nBase Defense Level -10
   PL: Podstawowy Poziom Ataku -10, Podstawowy Poziom Obrony -10
602. [Status [WeighedMurderousIntend] — nazwa] 짓눌린 살기
   źródło: Bufs-a1c9116.json :: dataList[id=WeighedMurderousIntend].name
   kontekst: identyfikator statusu w tekstach: `[WeighedMurderousIntend]`
   limit: do 40 znaków
   EN: Crushed Bloodthirst
   PL: Rozgnieciona Krwiożerczość
603. [Status [WeighedMurderousIntend] — opis] 기본 공격 레벨 -25, 기본 방어 레벨 -25
   źródło: Bufs-a1c9116.json :: dataList[id=WeighedMurderousIntend].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -25\nBase Defense Level -25
   PL: Podstawowy Poziom Ataku -25, Podstawowy Poziom Obrony -25
604. [Status [MiddleFingerBook] — nazwa] 중지의 복수 대상
   źródło: Bufs-a1c9116.json :: dataList[id=MiddleFingerBook].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerBook]`
   limit: do 40 znaków
   EN: The Middle's Vendetta Mark
   PL: Cel Zemsty Środkowego
605. [Status [MiddleFingerBook] — opis] 최댓값 : 10\n중지 소속에게 공격당할 때, 받는 피해량 +3% (최대 30%)
   źródło: Bufs-a1c9116.json :: dataList[id=MiddleFingerBook].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 10\nWhen attacked by The Middle, take +3% damage per Stack (max 30%)
   PL: Maks. stosów: 10\nPrzy ataku przez Środkowy otrzymuje +3% obrażeń za każdy stos (maks. 30%)
606. [Status [Persistent] — nazwa] 끈질김
   źródło: Bufs-a1c9116.json :: dataList[id=Persistent].name
   kontekst: identyfikator statusu w tekstach: `[Persistent]`
   limit: do 40 znaków
   EN: Persistence
   PL: Wytrwałość
607. [Status [Persistent] — opis] 최댓값 : 4\n체력이 0이 되는 피해를 받으면, 80% 확률로 해당 피해를 받지 않고, 체력을 60 회복, 흐트러짐 해제하고 이 버프 소멸\n\n아래 상황에서는 사망 방지 및 회복 효과가 발동하지 않음\n- 피격 시 코인 피해량이 자신의 최대 체력을 초과\n- 체력 회복 감소 효과를 보유\n턴 종료시 수치 1 감소
   źródło: Bufs-a1c9116.json :: dataList[id=Persistent].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 4\nWhen taking lethal damage, 80% chance to not take that damage, heal 60 HP, recover from Stagger, and lose this effect\n\nThe above effects do not activate under the following conditions:\n- When the Coin damage taken exceeds this unit's max HP\n- When this unit has the HP Healing Down effect\nReduced by 1 at Turn End
   PL: Maks. stosów: 4\nGdy otrzymuje obrażenia redukujące HP do 0, z 80% szansą nie otrzymuje ich, leczy 60 HP, wychodzi z Oszołomienia i traci ten buff\n\nPoniższe efekty nie działają w następujących sytuacjach:\n- Gdy obrażenia Monety przy trafieniu przekraczają Maks. HP\n- Gdy posiada efekt obniżenia Leczenia HP\nNa koniec tury traci 1 stos
608. [Status [BackstreetsNight_LowMorale] — nazwa] 뒷골목의 밤
   źródło: Bufs-a1c9116.json :: dataList[id=BackstreetsNight_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BackstreetsNight_LowMorale]`
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL: Noc w Zaułkach
609. [Status [BackstreetsNight_LowMorale] — opis] - 사기 저하\n- 턴 시작시 공격 위력 증가 1, 체력 회복 증가 1, 취약 1을 얻음
   źródło: Bufs-a1c9116.json :: dataList[id=BackstreetsNight_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: gain 1 Attack Power Up, 1 HP Healing Boost, and 1 Fragile
   PL: - Niskie Morale\n- Na początek tury zyskuje 1 Wzrost Mocy Ataku, 1 Wzrost Leczenia HP i 1 Wrażliwości
610. [Status [BackstreetsNight_Panic] — nazwa] 뒷골목의 밤
   źródło: Bufs-a1c9116.json :: dataList[id=BackstreetsNight_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BackstreetsNight_Panic]`
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Status [BackstreetsNight_Panic] — opis] - 패닉\n- 턴 시작시 공격 위력 증가 2, 체력 회복 증가 2, 취약 1을 얻음
   źródło: Bufs-a1c9116.json :: dataList[id=BackstreetsNight_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: gain 2 Attack Power Up, 2 HP Healing Boost, and 1 Fragile
   PL: - Panika\n- Na początek tury zyskuje 2 Wzrosty Mocy Ataku, 2 Wzrosty Leczenia HP i 1 Wrażliwości
612. [Status [SweeperA] — nazwa] 제 1파
   źródło: Bufs-a1c9116.json :: dataList[id=SweeperA].name
   kontekst: identyfikator statusu w tekstach: `[SweeperA]`
   limit: do 40 znaków
   EN: The First Wave
   PL: Pierwsza Fala
613. [Status [SweeperA] — opis] {0}턴 후 제 1파 종료
   źródło: Bufs-a1c9116.json :: dataList[id=SweeperA].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The first wave ends after {0} turn(s)
   PL: Pierwsza fala kończy się po {0} turach
614. [Status [SweeperB] — nazwa] 제 2파
   źródło: Bufs-a1c9116.json :: dataList[id=SweeperB].name
   kontekst: identyfikator statusu w tekstach: `[SweeperB]`
   limit: do 40 znaków
   EN: The Second Wave
   PL: Druga Fala
615. [Status [SweeperB] — opis] {0}턴 후 제 2파 종료
   źródło: Bufs-a1c9116.json :: dataList[id=SweeperB].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The second wave ends after {0} turn(s)
   PL: Druga fala kończy się po {0} turach
616. [Status [SweeperC] — nazwa] 제 3파
   źródło: Bufs-a1c9116.json :: dataList[id=SweeperC].name
   kontekst: identyfikator statusu w tekstach: `[SweeperC]`
   limit: do 40 znaków
   EN: The Third Wave
   PL: Trzecia Fala
617. [Status [SweeperC] — opis] {0}턴 후 제 3파 종료
   źródło: Bufs-a1c9116.json :: dataList[id=SweeperC].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The third wave ends after {0} turn(s)
   PL: Trzecia fala kończy się po {0} turach

## Statusy i efekty bojowe — Bufs-a1c951
- plik gry: `Bufs-a1c951.json`

618. [Status [AaCeSeBa] — nazwa] 호!호!호!
   źródło: Bufs-a1c951.json :: dataList[id=AaCeSeBa].name
   kontekst: identyfikator statusu w tekstach: `[AaCeSeBa]`
   limit: do 40 znaków
   EN: HO! HO! HO!
   PL: HO! HO! HO!
619. [Status [AaCeSeBa] — opis] 턴 종료 시 {1}만큼 다음 턴에 자신의 호흡 횟수를 증가.\n충전 횟수가 0이되면, 제거됨.
   źródło: Bufs-a1c951.json :: dataList[id=AaCeSeBa].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, \n
   EN: Turn End: Gain {1} Poise Count next turn.\nExpires at 0 Charge Count.
   PL: Na koniec tury Licznik Oddechu w następnej turze rośnie o {1}.\nZnika przy 0 Licznika Ładowania.
620. [Status [AaCeSeBb] — nazwa] 선물로 만들어주마
   źródło: Bufs-a1c951.json :: dataList[id=AaCeSeBb].name
   kontekst: identyfikator statusu w tekstach: `[AaCeSeBb]`
   limit: do 40 znaków
   EN: I'll Gift-wrap You
   PL: Zapakuję Cię na Prezent
621. [Status [AaCeSeBb] — opis] 매 턴마다 호흡 3을 얻음.\n턴 종료시 피해를 입힌 공격 스킬당 정신력 3 회복
   źródło: Bufs-a1c951.json :: dataList[id=AaCeSeBb].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 3 Poise every turn.\nTurn End: Heal 3 SP for every Attack Skill that dealt damage
   PL: Zyskuje 3 Oddechu co turę.\nNa koniec tury odzyskuje 3 Poczytalności za każdą Umiejętność ataku, która zadała obrażenia

## Statusy i efekty bojowe — Bufs-a1c971
- plik gry: `Bufs-a1c971.json`

622. [Status [Bloodthirst] — nazwa] 피갈망
   źródło: Bufs-a1c971.json :: dataList[id=Bloodthirst].name
   kontekst: identyfikator statusu w tekstach: `[Bloodthirst]`
   limit: do 40 znaków
   EN: Yearning for Blood
   PL: Tęsknota za Krwią
623. [Status [Bloodthirst] — opis] - 기본 공격 레벨 35 감소\n- 기본 방어 레벨 35 감소
   źródło: Bufs-a1c971.json :: dataList[id=Bloodthirst].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -35\n- Base Defense Level -35
   PL: - Podstawowy Poziom Ataku -35\n- Podstawowy Poziom Obrony -35
624. [Status [ObservedPerson] — nazwa] 피관찰자
   źródło: Bufs-a1c971.json :: dataList[id=ObservedPerson].name
   kontekst: identyfikator statusu w tekstach: `[ObservedPerson]`
   limit: do 40 znaków
   EN: Subject of Observation
   PL: Obiekt Obserwacji
625. [Status [ObservedPerson] — opis] - 최대 30\n- 턴 시작 시, 3 증가 (획득한 다음 턴부터 적용)\n- 뒤틀린 호엔하임에게 공격 스킬 효과로 피해를 받거나 입힐 때마다 1 증가\n- (수치 x 4)%만큼 적에게 받는 피해량 증가\n- (수치 x 2)%만큼 가하는 피해량이 증가하는 대신 적중 시 입힌 피해량의 (수치 / 2)%만큼 체력 피해를 입음 (이 효과로 흐트러지지 않음)
   źródło: Bufs-a1c971.json :: dataList[id=ObservedPerson].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn Start: gain 3 Stack (starting from the turn after this unit gained this effect)\n- Gain 1 Stack every time this unit takes or deals damage with an Attack Skill effect against Distorted Hohenheim\n- Take +(Stack x 4)% damage from enemies\n- Deal +(Stack x 2)% damage, but On Hit, take (Stack / 2)% of the damage dealt as HP damage (cannot be Staggered from this effect)
   PL: - Maks. 30\n- Na początku tury rośnie o 3 (od tury po zdobyciu)\n- Rośnie o 1 za każde otrzymanie lub zadanie obrażeń efektem Umiejętności ataku wobec Wykrzywionego Hohenheima\n- Otrzymuje +(stosy x 4)% obrażeń od wrogów\n- Zadaje +(stosy x 2)% obrażeń, ale przy trafieniu otrzymuje (stosy / 2)% zadanych obrażeń jako obrażenia HP (nie powoduje Oszołomienia)
626. [Status [BloodthirstHard] — nazwa] 피갈망
   źródło: Bufs-a1c971.json :: dataList[id=BloodthirstHard].name
   kontekst: identyfikator statusu w tekstach: `[BloodthirstHard]`
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Status [BloodthirstHard] — opis] - 기본 공격 레벨 25 감소\n- 기본 방어 레벨 25 감소
   źródło: Bufs-a1c971.json :: dataList[id=BloodthirstHard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -25\n- Base Defense Level -25
   PL: - Podstawowy Poziom Ataku -25\n- Podstawowy Poziom Obrony -25

## Statusy i efekty bojowe — Bufs-a1c9p1
- plik gry: `Bufs-a1c9p1.json`

628. [Status [MuscleContraction] — nazwa] 근섬유의 기계적 수축과 이완
   źródło: Bufs-a1c9p1.json :: dataList[id=MuscleContraction].name
   kontekst: identyfikator statusu w tekstach: `[MuscleContraction]`
   limit: do 40 znaków
   EN: Automated Myofiber Activity
   PL: Automatyczna Praca Włókien Mięśniowych
629. [Status [MuscleContraction] — opis] 최댓값: 2\n수치 당 피해량 +15%\n수치가 2일경우, 전투 시작 시 자신이 사용하는 공격 스킬의 모든 코인이 파괴 불가 코인으로 변경됨.\n공격 종료 시 버프 소멸
   źródło: Bufs-a1c9p1.json :: dataList[id=MuscleContraction].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Deal +15% damage per Stack\n- Combat Start: At 2 Stacks, convert all Coins of this unit's Attack Skills into Unbreakable Coins.\n- Attack End: Lose this effect
   PL: - Maks. 2 stosów\n- Zadaje +15% obrażeń za każdy stos\n- Na początku walki przy 2 stosach wszystkie Monety Umiejętności ataku tej jednostki stają się Niezniszczalnymi Monetami.\n- Po zakończeniu ataku traci efekt
630. [Status [DuelEdge] — nazwa] 결투 고조
   źródło: Bufs-a1c9p1.json :: dataList[id=DuelEdge].name
   kontekst: identyfikator statusu w tekstach: `[DuelEdge]`
   limit: do 40 znaków
   EN: The Duel Escalates
   PL: Eskalacja Pojedynku
631. [Status [DuelEdge] — opis] - 최댓값: 20\n- '엄지 제자 - 루치오'와 합을 진행할 시 '엄지 제자 - 루치오'의 스킬 위력과 피해량 증가\n- 매 턴마다 '엄지 제자 - 루치오'와 합을 하지 않으면 턴 종료 시 소멸
   źródło: Bufs-a1c9p1.json :: dataList[id=DuelEdge].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- 'The Thumb Apprentice - Lucio' gains Skill Power and deals more damage with every Clash with this unit\n- Expires at Turn End if this unit did not Clash with 'The Thumb Apprentice - Lucio' this turn
   PL: - Maks. wartości: 20\n- W Starciu z „Uczniem Kciuka - Lucio” Umiejętności tego wroga zyskują Siłę i zadają więcej obrażeń\n- Znika na koniec tury, jeżeli w tej turze nie odbyło się Starcie z „Uczniem Kciuka - Lucio"
632. [Status [HostageCharon] — nazwa] 인질극
   źródło: Bufs-a1c9p1.json :: dataList[id=HostageCharon].name
   kontekst: identyfikator statusu w tekstach: `[HostageCharon]`
   limit: do 40 znaków
   EN: Hostage Situation
   PL: Wzięcie Zakładnika
633. [Status [HostageCharon] — opis] - '엄지 제자 - 루치오'와 합을 진행할 시 합 위력 -1\n- '엄지 제자 - 루치오'에게 가하는 피해량 -20%
   źródło: Bufs-a1c9p1.json :: dataList[id=HostageCharon].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Clashing with 'The Thumb Apprentice - Lucio', Clash Power -1\n- Deal -20% damage to 'The Thumb Apprentice - Lucio'
   PL: - W Starciu z „Uczniem Kciuka - Lucio” Moc Starcia -1\n- Zadaje -20% obrażeń „Uczniowi Kciuka - Lucio"
634. [Status [SeveredTendon] — nazwa] 힘줄 절단
   źródło: Bufs-a1c9p1.json :: dataList[id=SeveredTendon].name
   kontekst: identyfikator statusu w tekstach: `[SeveredTendon]`
   limit: do 40 znaków
   EN: Severed Tendon
   PL: Przecięte Ścięgno
