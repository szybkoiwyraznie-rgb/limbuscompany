# Paczka AI P60 (Fala 3 · 3B) — Dary E.G.O (Lustrzane Lochy i fabularne) (część 5/5)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P60_3b_dary_ego_cz05.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P60_3b_dary_ego_cz05.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Dar E.G.O: EGOgift_StoryDungeon
- plik gry: `EGOgift_StoryDungeon.json`

1. [Dar E.G.O [1052] — nazwa] 뜨거운 육즙 다리살
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1052].name
   limit: do 40 znaków
   EN: Hot ‘n Juicy Drumstick
   PL: Gorący i Soczysty Udek
2. [Dar E.G.O [1052] — opis] 스킬로 적에게 [Combustion] 부여 시 [Combustion] 횟수 5 증가.
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1052].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When inflicting [Combustion] with Skills against enemies, inflict +5 [Combustion] Count.
   PL: Nakładając [Combustion] Umiejętnością na wroga, dodaje +5 do Licznika [Combustion].
3. [Dar E.G.O [1052] — opis skrócony] 스킬로 화상 부여 시 화상 횟수 5 증가
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1052].simpleDesc[abilityID=1052].simpleDesc
   limit: do 120 znaków
   EN: When inflicting Burn with skill effects, inflict +5 Burn Count.
   PL: Nakładając Podpalenie Umiejętnością, dodaje +5 do Licznika Podpalenia.
4. [Dar E.G.O [1053] — nazwa] 목이 뻑뻑 가슴살
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1053].name
   limit: do 40 znaków
   EN: Dry-to-the-Bone Breast
   PL: Sucha Do Kości Pierś
5. [Dar E.G.O [1053] — opis] 스킬로 적에게 [Burst] 부여 시 [Burst] 횟수 5 증가.
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1053].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: When inflicting [Burst] with Skills against enemies, inflict +5 [Burst] Count.
   PL: Nakładając [Burst] Umiejętnością na wroga, dodaje +5 do Licznika [Burst].
6. [Dar E.G.O [1053] — opis skrócony] 스킬로 파열 부여 시 파열 횟수 5 증가
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1053].simpleDesc[abilityID=1053].simpleDesc
   limit: do 120 znaków
   EN: When inflicting Rupture with skill effects, inflict +5 Rupture Count.
   PL: Nakładając Rozdarcie Umiejętnością, dodaje +5 do Licznika Rozdarcia.
7. [Dar E.G.O [1054] — nazwa] 탱고 닭양념장
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1054].name
   limit: do 40 znaków
   EN: Tango Marinade
   PL: Marynata Tango
8. [Dar E.G.O [1054] — opis] 대상보다 속도가 높다면, 합 위력 (속도/2)만큼 증가 (최대 3).
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1054].desc
   limit: do 120 znaków
   EN: Allies gain Clash Power by half their Speed against opponents with lower Speed. (max 3)
   PL: Przeciw przeciwnikom o niższej Prędkości sojusznik zyskuje Moc Starcia równą (Prędkość/2) (maks. 3).
9. [Dar E.G.O [1054] — opis skrócony] 합 위력 (속도/2)만큼 증가
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1054].simpleDesc[abilityID=1054].simpleDesc
   limit: do 120 znaków
   EN: Gain +(Speed/2) Clash Power.
   PL: Zyskuje +(Prędkość/2) Mocy Starcia.
10. [Dar E.G.O [1055] — nazwa] 오염된 실과 바늘
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1055].name
   limit: do 40 znaków
   EN: Contaminated Needle & Thread
   PL: Zanieczyszczona Igła i Nitka
11. [Dar E.G.O [1055] — opis] 매 턴마다 처음으로 적에게 피해를 입힌 스킬에 적용.\n\n(피해량/3)만큼 [Laceration] 위력을 부여.
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1055].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Each turn, the first skill to deal damage to an enemy inflicts Bleed by 1/3 of the damage dealt.
   PL: Dotyczy pierwszej Umiejętności, która zada w tej turze obrażenia wrogowi.\n\nNakłada Moc [Laceration] równą (zadanych obrażeń/3).
12. [Dar E.G.O [1055] — opis skrócony] (피해량/3)만큼 출혈 위력을 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1055].simpleDesc[abilityID=1055].simpleDesc
   limit: do 120 znaków
   EN: Inflict (damage dealt/3) Bleed Potency
   PL: Nakłada (zadane obrażenia/3) Siły Krwawienia
13. [Dar E.G.O [1056] — nazwa] 날카로운 실과 바늘
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1056].name
   limit: do 40 znaków
   EN: Sharp Needle & Thread
   PL: Ostra Igła i Nitka
14. [Dar E.G.O [1056] — opis] 매 턴마다 처음으로 적에게 피해를 입힌 스킬의 (피해량/2)만큼 추가 고정 피해를 입힘.
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1056].desc
   limit: do 140 znaków
   EN: Each turn, the first skill to deal damage to an enemy deals bonus fixed damage by half of the damage dealt.
   PL: Za każdą turę pierwsza Umiejętność, która zada wrogowi obrażenia, zadaje dodatkowe obrażenia stałe równe (zadanych obrażeń/2).
15. [Dar E.G.O [1056] — opis skrócony] (피해량/2)만큼 추가 고정 피해를 입힘
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1056].simpleDesc[abilityID=1056].simpleDesc
   limit: do 120 znaków
   EN: Deal (damage dealt/2) bonus fixed damage
   PL: Zadaje dodatkowe obrażenia stałe równe (zadanych obrażeń/2)
16. [Dar E.G.O [2001] — nazwa] 작은 앰플
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2001].name
   limit: do 40 znaków
   EN: Small Ampule
   PL: Mała Ampułka
17. [Dar E.G.O [2001] — opis] 턴 시작 시 체력이 40% 미만인 아군이 있으면 체력을 최대 체력의 100%만큼 회복 (한 층 당 1회 발동)
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2001].desc
   limit: do 120 znaków
   EN: At the start of the turn, allies under 40% HP heal 100% of max HP. (Once per floor)
   PL: Na początku tury: jeżeli któryś sojusznik ma HP poniżej 40%, leczy go do 100% Maks. HP (1 raz na piętro)
18. [Dar E.G.O [2001] — opis skrócony] 조건 충족 체력 100% 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2001].simpleDesc[abilityID=2001].simpleDesc
   limit: do 120 znaków
   EN: Conditional full heal
   PL: Warunkowe leczenie 100% HP
19. [Dar E.G.O [2002] — nazwa] 허물어진 알 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2002].name
   limit: do 40 znaków
   EN: Piece of Crumbled Egg
   PL: Odłamek Rozpadniętego Jaja
20. [Dar E.G.O [2002] — opis] 매 전투의 1턴 시작 시 현재 보유한 E.G.O 자원 중 무작위 속성 1개의 개수 + 2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2002].desc
   limit: do 130 znaków
   EN: On the first turn of each encounter, gain 2 E.G.O resources of a random affinity in possession
   PL: Na początku 1. tury każdej walki: Licznik Zasobu E.G.O losowego posiadanego Grzechu +2
21. [Dar E.G.O [2002] — opis skrócony] 보유한 속성 중 무작위 E.G.O 자원 + 2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2002].simpleDesc[abilityID=2002].simpleDesc
   limit: do 120 znaków
   EN: Gain 2 E.G.O resources for a random affinity owned
   PL: Zyskuje 2 Zasobów E.G.O losowego posiadanego Grzechu
22. [Dar E.G.O [2003] — nazwa] 싸늘한 환상
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2003].name
   limit: do 40 znaków
   EN: Cold Illusion
   PL: Chłodne Złudzenie
23. [Dar E.G.O [2003] — opis] 탐식 속성 스킬의 피해량 + 10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2003].desc
   limit: do 120 znaków
   EN: Gluttony skills deal +10% damage
   PL: Umiejętności Obżarstwa zadają +10% obrażeń
24. [Dar E.G.O [2003] — opis skrócony] 탐식 속성 스킬의 피해량 + 10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2003].simpleDesc[abilityID=2003].simpleDesc
   limit: do 120 znaków
   EN: Gluttony skill damage +10%
   PL: Umiejętności Obżarstwa: +10% obrażeń
25. [Dar E.G.O [2004] — nazwa] 날카로운 환상
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2004].name
   limit: do 40 znaków
   EN: Sharp Illusion
   PL: Ostre Złudzenie
26. [Dar E.G.O [2004] — opis] 오만 속성 스킬의 피해량 + 10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2004].desc
   limit: do 120 znaków
   EN: Pride skills deal +10% damage
   PL: Umiejętności Pychy zadają +10% obrażeń
27. [Dar E.G.O [2004] — opis skrócony] 오만 속성 스킬의 피해량 + 10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2004].simpleDesc[abilityID=2004].simpleDesc
   limit: do 120 znaków
   EN: Pride skill damage +10%
   PL: Umiejętności Pychy: +10% obrażeń
28. [Dar E.G.O [2005] — nazwa] 향긋한 환상
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2005].name
   limit: do 40 znaków
   EN: Fragrant Illusion
   PL: Pachnące Złudzenie
29. [Dar E.G.O [2005] — opis] 나태 속성 스킬의 피해량 + 10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2005].desc
   limit: do 120 znaków
   EN: Sloth skills deal +10% damage
   PL: Umiejętności Lenistwa zadają +10% obrażeń
30. [Dar E.G.O [2005] — opis skrócony] 나태 속성 스킬의 피해량 + 10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2005].simpleDesc[abilityID=2005].simpleDesc
   limit: do 120 znaków
   EN: Sloth skill damage +10%
   PL: Umiejętności Lenistwa: +10% obrażeń
31. [Dar E.G.O [2006] — nazwa] 별의 흔적
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2006].name
   limit: do 40 znaków
   EN: Trace of Stars
   PL: Ślad Gwiazd
32. [Dar E.G.O [2006] — opis] 정신력이 0 미만일 때 우울, 나태 속성 스킬의 최종 위력 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2006].desc
   limit: do 120 znaków
   EN: When below 0 SP, Gloom and Sloth skills have +1 Final Power
   PL: Gdy SP poniżej 0, Umiejętności Posępności i Lenistwa mają +1 do Mocy Końcowej
33. [Dar E.G.O [2006] — opis skrócony] 정신력이 0 미만일 때 우울, 나태 속성 스킬의 최종 위력 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2006].simpleDesc[abilityID=2006].simpleDesc
   limit: do 120 znaków
   EN: Gloom and Sloth skill Final Power +1 when SP is below 0
   PL: Umiejętności Posępności i Lenistwa: +1 do Mocy Końcowej, gdy SP poniżej 0
34. [Dar E.G.O [2007] — nazwa] 알싸한 꽃봉오리
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2007].name
   limit: do 40 znaków
   EN: Pungent Bud
   PL: Korzenny Pąk
35. [Dar E.G.O [2007] — opis] 스킬로 침잠 부여 시 50% 확률로 침잠 위력 1 추가 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2007].desc
   limit: do 120 znaków
   EN: When inflicting Sinking with skill effects, apply 1 more Sinking with a 50% chance
   PL: Nakładając Zatonięcie Umiejętnością, z szansą 50% nakłada dodatkowo 1 Siłę Zatonięcia
36. [Dar E.G.O [2007] — opis skrócony] 스킬로 침잠 부여 시 50% 확률로 침잠 위력 1 추가 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2007].simpleDesc[abilityID=2007].simpleDesc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Dar E.G.O [2008] — nazwa] 뜨거운 눈물
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2008].name
   limit: do 40 znaków
   EN: Hot Tears
   PL: Gorące Łzy
38. [Dar E.G.O [2008] — opis] 분노 속성으로 받는 피해 -10%\n피격 시 다음 턴에 공격 위력 증가 1을 얻음 (수감자 당 턴 당 1회 발동)
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2008].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take -10% Wrath-affinity damage\nWhen hit, gain 1 Attack Power Up next turn (Once per turn per Sinner)
   PL: Otrzymuje -10% obrażeń od Gniewu\nPo otrzymaniu obrażeń następnej tury zyskuje 1 Wzrost Mocy Ataku (wywołuje 1 raz na turę na Grzesznika)
39. [Dar E.G.O [2008] — opis skrócony] 분노 속성으로 받는 피해 감소
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2008].simpleDesc[abilityID=2009].simpleDesc
   limit: do 120 znaków
   EN: Take less Wrath damage
   PL: Otrzymuje mniej obrażeń od Gniewu
40. [Dar E.G.O [2008] — opis skrócony] 피격 시 다음 턴에 공격 위력 증가 1을 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2008].simpleDesc[abilityID=200901].simpleDesc
   limit: do 120 znaków
   EN: When hit, gain 1 Attack Power Up next turn
   PL: Po otrzymaniu obrażeń następnej tury zyskuje 1 Wzrost Mocy Ataku
41. [Dar E.G.O [2009] — nazwa] 식은 눈물
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2009].name
   limit: do 40 znaków
   EN: Cooled Tear
   PL: Wystygłe Łzy
42. [Dar E.G.O [2009] — opis] 피격 시 다음 턴에 보호 1을 얻음 (수감자 당 턴 당 1회 발동)
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2009].desc
   limit: do 120 znaków
   EN: When attacked, gain 1 Protection next turn (Once per turn per Sinner)
   PL: Po otrzymaniu obrażeń następnej tury zyskuje 1 Ochrony (wywołuje 1 raz na turę na Grzesznika)
43. [Dar E.G.O [2009] — opis skrócony] 피격 시 다음 턴에 보호 1을 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2009].simpleDesc[abilityID=2009].simpleDesc
   limit: do 120 znaków
   EN: When hit, gain 1 Protection next turn
   PL: Po otrzymaniu obrażeń następnej tury zyskuje 1 Ochrony
44. [Dar E.G.O [2010] — nazwa] 파편의 기억
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2010].name
   limit: do 40 znaków
   EN: Memories of Fragments
   PL: Pamięć Odłamków
45. [Dar E.G.O [2010] — opis] 오만, 질투 속성 스킬로 합 진행 시 합 위력 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2010].desc
   limit: do 120 znaków
   EN: In a clash, Pride and Envy skills have +1 Clash Power
   PL: Umiejętności Pychy i Zawiści mają +1 do Mocy Starcia w Starciu
46. [Dar E.G.O [2010] — opis skrócony] 오만, 질투 속성 스킬로 합 진행 시 합 위력 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2010].simpleDesc[abilityID=2010].simpleDesc
   limit: do 120 znaków
   EN: Pride and Envy skill Clash Power +1 in a clash
   PL: Umiejętności Pychy i Zawiści: +1 do Mocy Starcia w Starciu
47. [Dar E.G.O [2011] — nazwa] 찢겨진 봄의 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2011].name
   limit: do 40 znaków
   EN: Piece of a Torn Spring
   PL: Odłamek Rozdartej Wiosny
48. [Dar E.G.O [2011] — opis] 오만 속성으로 받는 피해 -10% \n\n<i>"나는 파릇하게 흩날리고 싶었으며, 서걱거리는 마음에 씨앗이 박히는 듯한 일렁임을 느끼곤 했지."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2011].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Take -10% Pride-affinity damage\n\n<i>"I would feel a desire to scatter into the winds in lush blue, sensing the sway of seeds plunging into my scrawling mind."</i>
   PL: Otrzymuje -10% obrażeń od Pychy\n\n<i>„Chciałem rozfrunąć na wiatr w młodej zieleni, czując, jak w drżące serce wbijają się ziarna niczym nasiona w bruzdy.”</i>
49. [Dar E.G.O [2011] — opis skrócony] 오만 속성으로 받는 피해 -10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2011].simpleDesc[abilityID=2011].simpleDesc
   limit: do 120 znaków
   EN: Pride damage taken -10%
   PL: Otrzymuje -10% obrażeń od Pychy
50. [Dar E.G.O [2012] — nazwa] 찢겨진 여름의 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2012].name
   limit: do 40 znaków
   EN: Piece of a Torn Summer
   PL: Odłamek Rozdartego Lata
51. [Dar E.G.O [2012] — opis] 탐식 속성으로 받는 피해 -10%\n\n<i>"날씨의 변덕스러움을 헤아리려 하는 것은 의미가 없다고 생각하였기에. 잔잔해질 날을 기다리며, 고개를 내어다 볼 뿐이었지."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2012].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Take -10% Gluttony-affinity damage\n\n<i>"I saw no meaning in attempting to fathom the caprices of the weather. I would simply wait for things to calm, looking out for the day's arrival."</i>
   PL: Otrzymuje -10% obrażeń od Obżarstwa\n\n<i>„Nie widziałem sensu w zgadywaniu kaprysów pogody. Czekałem po prostu, aż wszystko ucichnie, wypatrując dnia, który ma nadejść.”</i>
52. [Dar E.G.O [2012] — opis skrócony] 탐식 속성으로 받는 피해 -10% \n\n<i>"비스듬히 바라보다 스며들면 그만일 것이라는게, 안일함이었다는 생각을… 이제야 하게 되오."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2012].simpleDesc[abilityID=2012].simpleDesc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Take -10% Gluttony-affinity damage\n\n<i>"Alas, I was careless in my assumption that I could simply observe slantwise as it comes to pass until it has seeped... Realization comes too late."</i>
   PL: Otrzymuje -10% obrażeń od Obżarstwa\n\n<i>„Ależ byłem lekkomyślny, mniemając, że wystarczy patrzeć z ukosa, jak świat mnie przenika, aż wsiąknie… Zrozumienie przychodzi zbyt późno.”</i>
53. [Dar E.G.O [2013] — nazwa] 찢겨진 가을의 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2013].name
   limit: do 40 znaków
   EN: Piece of a Torn Autumn
   PL: Odłamek Rozdartej Jesieni
54. [Dar E.G.O [2013] — opis] 우울 속성으로 받는 피해 -10%\n\n<i>"비스듬히 바라보다 스며들면 그만일 것이라는게, 안일함이었다는 생각을… 이제야 하게 되오."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2013].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Take -10% Gloom-affinity damage\n\n<i>"Alas, I was careless in my assumption that I could simply observe slantwise as it comes to pass until it has seeped... Realization comes too late."</i>
   PL: Otrzymuje -10% obrażeń od Posępności\n\n<i>„Ależ byłem lekkomyślny, mniemając, że wystarczy patrzeć z ukosa, jak świat mnie przenika, aż wsiąknie… Zrozumienie przychodzi zbyt późno.”</i>
55. [Dar E.G.O [2013] — opis skrócony] 우울 속성으로 받는 피해 -10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2013].simpleDesc[abilityID=2013].simpleDesc
   limit: do 120 znaków
   EN: Gloom damage taken -10%
   PL: Otrzymuje -10% obrażeń od Posępności
56. [Dar E.G.O [2014] — nazwa] 찢겨진 겨울의 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2014].name
   limit: do 40 znaków
   EN: Piece of a Torn Winter
   PL: Odłamek Rozdartej Zimy
57. [Dar E.G.O [2014] — opis] 나태 속성으로 받는 피해 -10% \n\n<i>"구인회의 폭발은 모든 것을 산산이 조각내었고, 나의 모든 것 역시 멈추게 만들었소."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2014].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Take -10% Sloth-affinity damage\n\n<i>"The explosion of the League of Nine shattered everything there was, and everything came to a halt for me as well."</i>
   PL: Otrzymuje -10% obrażeń od Lenistwa\n\n<i>„Wybuch Ligi Dziewięciu roztrzaskał wszystko, co było, i wszystko we mnie również stanęło.”</i>
58. [Dar E.G.O [2014] — opis skrócony] 나태 속성으로 받는 피해 -10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2014].simpleDesc[abilityID=2014].simpleDesc
   limit: do 120 znaków
   EN: Sloth damage taken -10%
   PL: Otrzymuje -10% obrażeń od Lenistwa
59. [Dar E.G.O [2015] — nazwa] 부서진 인연의 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2015].name
   limit: do 40 znaków
   EN: Piece of a Broken Bond
   PL: Odłamek Zerwanej Więzi
60. [Dar E.G.O [2015] — opis] 이상의 모든 스킬의 최종 위력 +2.\n아군 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 신속, 공격 위력 증가 1을 얻음(턴 당 1회)\n\n<i>"행적을 돌이켜 보니… 우리 모두가 많은 걸 잃고 있었소."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2015].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Yi Sang's skills gain +2 Final Power\nWhen an ally dies, remaining allies gain 1 Haste and 1 Attack Power Up next turn (Once per turn)\n\n<i>"Taking a backward glance at our trails... all of us have been suffering great losses."</i>
   PL: Umiejętności Yi Sanga mają +2 do Mocy Końcowej.\nPo śmierci sojusznika: pozostali sojusznicy na koniec tury następnej tury zyskują 1 Pośpiechu i 1 Wzrost Mocy Ataku (1 raz na turę)\n\n<i>„Spoglądając wstecz na nasze ślady… wszyscy traciliśmy tak wiele.”</i>
61. [Dar E.G.O [2015] — opis skrócony] 이상의 모든 스킬의 최종 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2015].simpleDesc[abilityID=2015].simpleDesc
   limit: do 120 znaków
   EN: Yi Sang's Skill Final Power +2
   PL: Umiejętności Yi Sanga mają +2 do Mocy Końcowej
62. [Dar E.G.O [2015] — opis skrócony] 아군 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 신속, 공격 위력 증가 1을 얻음 (턴 당 1회)
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2015].simpleDesc[abilityID=201501].simpleDesc
   limit: do 130 znaków
   EN: When an ally dies, remaining allies gain 1 Haste and 1 Attack Power Up next turn (Once per turn)
   PL: Po śmierci sojusznika: pozostali sojusznicy następną turę zyskują 1 Pośpiechu i 1 Wzrost Mocy Ataku (1 raz na turę)
63. [Dar E.G.O [2016] — nazwa] 돌이키는 기억의 조각
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2016].name
   limit: do 40 znaków
   EN: Piece of Reversing Memories
   PL: Odłamek Przywoływanej Pamięci
64. [Dar E.G.O [2016] — opis] 이상의 레벨이 35레벨로 상승.\n이상의 인격 동기화 단계, E.G.O 환상해석 단계가 3단계로 상승\n\n<i>"우리는 야심가도, 탐욕가도 아니며 그저 기술을 사랑했던 아해에 불과했지."</i>
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2016].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <i>, </i>, \n
   EN: Yi Sang's level rises to 35.\nYi Sang's Uptie and Threadspin Tiers rise to Tier 3.\n\n<i>"We were neither highfliers nor greedy vultures; we were merely children who loved technology."</i>
   PL: Poziom Yi Sanga rośnie do 35.\nPoziomy Synchronizacji Yi Sanga i Splotu Nici jego E.G.O rosną do poziomu 3\n\n<i>„Nie byliśmy ani ambitnymi lotrikami, ani chciwymi sępami — byliśmy tylko dziećmi, które pokochały technologię.”</i>
65. [Dar E.G.O [2016] — opis skrócony] 이상의 레벨이 35레벨로 상승.
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2016].simpleDesc[abilityID=2016].simpleDesc
   limit: do 120 znaków
   EN: Yi Sang's level rises to 35.
   PL: Poziom Yi Sanga rośnie do 35.
66. [Dar E.G.O [2016] — opis skrócony] 이상의 인격 동기화 단계, E.G.O 환상해석 단계가 3단계로 상승
   źródło: EGOgift_StoryDungeon.json :: dataList[id=2016].simpleDesc[abilityID=201601].simpleDesc
   limit: do 120 znaków
   EN: Yi Sang's Uptie and Threadspin Tiers rise to Tier 3
   PL: Poziomy Synchronizacji Yi Sanga i Splotu Nici jego E.G.O rosną do poziomu 3

## Dar E.G.O: EGOgift_TwiningThreads
- plik gry: `EGOgift_TwiningThreads.json`

67. [Dar E.G.O [9260] — nazwa] 작품 : 약동
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9260].name
   limit: do 40 znaków
   EN: Artwork: Pulsation
   PL: Dzieło : Pulsowanie
68. [Dar E.G.O [9260] — opis] 한 턴 동안 자신의 기본 스킬로 [Charge] 횟수를 10 이상 소모했으면, 다음 턴에 기본 스킬로 가하는 피해량 +20% (위력 고정인 특수 <noparse>충전</noparse> 제외)\n- 소모한 [Charge]이 특수 충전이면, 다음 턴에 부여하는 [Laceration] 위력과 [Laceration] 횟수 +1
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9260].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Charge], [Laceration]
   znaczenie tagów: [Charge] = 충전 / Charge; [Laceration] = 출혈 / Bleed
   EN: If an ally consumed 10+ [Charge] Count in a single turn with its Base Skills, the said ally deals +20% damage with Base Skills next turn (excluding 'Unique Charge' with fixed Potency)\n- If the [Charge] consumed was 'Unique Charge', inflict +1 more [Laceration] and [Laceration] Count next turn
   PL: Jeżeli w ciągu jednej tury Tożsamość zużyła Podstawowymi Umiejętnościami co najmniej 10 Liczników [Charge], następnej tury jej Podstawowe Umiejętności zadają +20% obrażeń (z wyjątkiem Szczególnego Ładowania o stałej Mocy)\n- Jeżeli zużyte [Charge] było Szczególnym Ładowaniem, następnej tury nakładane [Laceration] zyskują +1 do Mocy i Licznika
69. [Dar E.G.O [9261] — nazwa] 작품 : 야성
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9261].name
   limit: do 40 znaków
   EN: Artwork: Ferity
   PL: Dzieło : Dzikość
70. [Dar E.G.O [9261] — opis] 정신력이 15 이하거나 [Sinking] 위력을 35 이상 보유한 적에게 타격 스킬로 가하는 피해량 +20% (침잠 위력은 부위로 판정)\n- 해당 타격 스킬이 [Laceration] 위력, 횟수, 특수 출혈을 부여하는 스킬 또는 우울 속성 스킬이고 적중했으면, 다음 턴에 [Enhancement] 1 얻음 (턴마다 캐릭터 당 1회)
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9261].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [Laceration], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Deal +20% damage with Blunt Skills against enemies that either have 35+ [Sinking] Potency or are at 15 or lower SP ([Sinking] Potency is calculated per-Part)\n- If the said Blunt Skill is either a Gloom Skill or a Skill that inflicts [Laceration] Potency, Count, or 'Unique Bleed', and hit the target, gain 1 [Enhancement] next turn (once per turn per Identity)
   PL: Umiejętności obuchowe zadają +20% obrażeń wrogom z SP ≤ 15 lub z co najmniej 35 Siły [Sinking] (Siła Zatonięcia liczona per Część)\n- Jeżeli dana Umiejętność obuchowa nakłada Moc, Licznik [Laceration] lub Szczególne Krwawienie albo jest Umiejętnością Posępności, i trafi, następnej tury zyskuje 1 [Enhancement] (1 raz na turę na Tożsamość)
71. [Dar E.G.O [9262] — nazwa] 모든 것의 뼈대
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9262].name
   limit: do 40 znaków
   EN: Universal Skeleton
   PL: Szkielet Wszystkiego
72. [Dar E.G.O [9262] — opis] 약지 소속 인격 공격 종료시 대상에게 무작위 물리 내성 약화 1 부여 (턴당 2회)\n\n약지 소속 인격이 가하는 피해량 +10%
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9262].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Ring-faction Identities: At Attack End, inflict 1 Stack of a random Attack Type Resist Down on target (2 times per turn)\n\nThe Ring-faction Identities deal +10% damage
   PL: Po zakończeniu ataku Tożsamości frakcji Serdecznego nakłada na cel 1 losowe Osłabienie Odporności fizycznej (2 razy na turę)\n\nTożsamości frakcji Serdecznego zadają +10% obrażeń
73. [Dar E.G.O [9263] — nazwa] 수작 : 진화하는 약동
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9263].name
   limit: do 40 znaków
   EN: Artwork: Evolving Pulsation
   PL: Dzieło : Ewoluujące Pulsowanie
74. [Dar E.G.O [9263] — opis] 턴 시작시, 약지 소속 인격이 2인 이상일 때 발동 (출격 인원을 기준으로 함).\n\n약지 신체파 소속 인격의 기본 스킬 적중시 대상에게 [SlashResistDown] 1 부여 (스킬당 1회, 턴당 2회)\n\n약지 소속 인격이 가하는 피해량 +20%\n\n턴 시작시 모든 적들의 [Laceration] 위력의 합이 99 이상이면, 약지 신체파 소속 인격이 [RingFingerPhysical] 1 얻음
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9263].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [SlashResistDown], [Laceration], [RingFingerPhysical]
   znaczenie tagów: [SlashResistDown] = 참격 내성 약화 / Slash Resist Down; [Laceration] = 출혈 / Bleed; [RingFingerPhysical] = 육체미 / Beauty of the Physique
   EN: Turn Start: Activates when there are 2 or more The Ring-faction Identities (only counts Identities on the field)\n\nThe Ring School of Corporism-faction Identities inflict 1 [SlashResistDown] On Hit with Base Skills (once per Skill; 2 times per turn)\n\nThe Ring Identities deal +20% damage\n\nTurn Start: At 99+ total sum of [Laceration] Potency on all enemies, The Ring School of Corporism-faction Identities gain 1 [RingFingerPhysical]
   PL: Wywołuje na początku tury, gdy na polu są co najmniej 2 Tożsamości frakcji Serdecznego (liczą się tylko Tożsamości na polu).\n\nTrafienie Podstawową Umiejętnością Tożsamości frakcji Serdecznego — Szkoły Korporyzmu nakłada na cel 1 [SlashResistDown] (1 raz na Umiejętność, 2 razy na turę)\n\nTożsamości frakcji Serdecznego zadają +20% obrażeń\n\nNa początku tury: gdy suma Sił [Laceration] wszystkich wrogów wynosi 99+, Tożsamości frakcji Serdecznego — Szkoły Korporyzmu zyskują 1 [RingFingerPhysical]
75. [Dar E.G.O [9264] — nazwa] 수작 : 박제된 야성
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9264].name
   limit: do 40 znaków
   EN: Artwork: Taxidermied Ferity
   PL: Dzieło : Wypchana Dzikość
76. [Dar E.G.O [9264] — opis] 턴 시작시, 약지 소속 인격이 2인 이상일 때 발동 (출격 인원을 기준으로 함).\n\n약지 야수파 소속 인격의 기본 스킬 적중시 대상에게 [HitResistDown] 1 부여 (스킬당 1회, 턴당 2회)\n\n약지 소속 인격이 가하는 피해량 +20%\n\n턴 시작시 모든 적들의 [Laceration] 위력의 합이 99 이상이면, 약지 야수파 소속 인격이 [RingFingerFauvism] 1 얻음
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9264].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [HitResistDown], [Laceration], [RingFingerFauvism]
   znaczenie tagów: [HitResistDown] = 타격 내성 약화 / Blunt Resist Down; [Laceration] = 출혈 / Bleed; [RingFingerFauvism] = 야성미 / Charm of the Beastly
   EN: Turn Start: Activates when there are 2 or more The Ring-faction Identities (only counts Identities on the field)\n\nThe Ring School of Fauvism-faction Identities inflict 1 [HitResistDown] On Hit with Base Skills (once per Skill; 2 times per turn)\n\nThe Ring Identities deal +20% damage\n\nTurn Start: At 99+ total sum of [Laceration] Potency on all enemies, The Ring School of Fauvism-faction Identities gain 1 [RingFingerFauvism]
   PL: Wywołuje na początku tury, gdy na polu są co najmniej 2 Tożsamości frakcji Serdecznego (liczą się tylko Tożsamości na polu).\n\nTrafienie Podstawową Umiejętnością Tożsamości frakcji Serdecznego — Szkoły Fowizmu nakłada na cel 1 [HitResistDown] (1 raz na Umiejętność, 2 razy na turę)\n\nTożsamości frakcji Serdecznego zadają +20% obrażeń\n\nNa początku tury: gdy suma Sił [Laceration] wszystkich wrogów wynosi 99+, Tożsamości frakcji Serdecznego — Szkoły Fowizmu zyskują 1 [RingFingerFauvism]
77. [Dar E.G.O [9265] — nazwa] 중지식 너클
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9265].name
   limit: do 50 znaków
   EN: The Middle Styled Knuckle-dusters
   PL: Kastety w Stylu Środkowego
78. [Dar E.G.O [9265] — opis] 적의 타격 내성이 1.5 이하인 경우, 타격 내성 +0.3.
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9265].desc
   limit: do 120 znaków
   EN: If the target has 1.5 or lower Blunt Resistance, Blunt Resistance +0.3
   PL: Jeżeli Odporność obuchowa celu wynosi 1,5 lub mniej, jej Odporność obuchowa +0,3.
79. [Dar E.G.O [9266] — nazwa] 텅 빈 새장
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9266].name
   limit: do 40 znaków
   EN: Unoccupied Birdcage
   PL: Pusta Klatka
80. [Dar E.G.O [9266] — opis] 공격 가중치가 2 이상인 스킬 공격 종료 시, 사용한 스킬 속성의 E.G.O 자원 +(적에게 적중한 횟수 / 2). (소수점 <noparse>버림</noparse>, 스킬당 최대 5)\n\n공격 가중치가 2 이상인 스킬로 크리티컬이 발생했다면, 공격 종료시 제일 적게 보유한 E.G.O 자원 +(크리티컬이 발생한 코인 수). (최대 3)
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9266].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: At Attack End of a Skill that has 2+ Atk Weight, gain +(# of hits on an enemy / 2) E.G.O resource of that Skill's Affinity (rounded down; max 5 per Skill)\n\nOn Crit with a Skill that has 2+ Atk Weight, gain +(# of Coins that hit Critically) E.G.O resource of the least-owned Affinity at Attack End (max 3)
   PL: Na koniec ataku Umiejętnością o Wadze Ataku 2+: +# trafień we wroga / 2 Zasobu E.G.O Grzechu użytej Umiejętności. (zaokrąglenie w dół, maks. 5 na Umiejętność)\n\nPrzy trafieniu krytycznym Umiejętnością o Wadze Ataku 2+: na koniec ataku +# Monet, które trafiły krytycznie, Zasobu E.G.O najmniej posiadanego Grzechu. (maks. 3)
81. [Dar E.G.O [9267] — nazwa] 달궈진 놋쇠
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9267].name
   limit: do 40 znaków
   EN: Searing Brass
   PL: Rozżarzony Mosiądz
82. [Dar E.G.O [9267] — opis] [Combustion] 위력 최댓값 +11\n\n전투 중 가장 처음으로 부여하는 [Combustion] 위력 부여 값 3배로 증가 (전투당 1회)\n\n적이 [Combustion] 발동으로 [Combustion] 피해를 입을 때, [Combustion] 위력만큼 분노 피해\n\n[Combustion] 위력, [Combustion] 횟수 또는 특수 화상을 부여하는 스킬의 피해량 +20%
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9267].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Max [Combustion] Potency +11\n\nTriple the first [Combustion] Potency to be inflicted in the Encounter (once per Encounter)\n\nWhen an enemy takes [Combustion] damage due to [Combustion] activation, deal Wrath damage equal to [Combustion] Potency\n\nSkills that inflict [Combustion] Potency, [Combustion] Count, or 'Unique Burn' deal +20% damage
   PL: Maks. Siła [Combustion] +11\n\nPierwsza nakładana w walce wartość Siły [Combustion] jest 3-krotnie większa (1 raz na walkę)\n\nGdy wróg otrzymuje obrażenia [Combustion] od wywołania [Combustion], zadaje mu obrażenia Gniewu równe Sile [Combustion]\n\nUmiejętności nakładające Siłę, Licznik [Combustion] lub Szczególne Podpalenie zadają +20% obrażeń
83. [Dar E.G.O [19267] — nazwa] 달궈진 놋쇠+
   źródło: EGOgift_TwiningThreads.json :: dataList[id=19267].name
   limit: do 40 znaków
   EN: Searing Brass+
   PL: Rozżarzony Mosiądz+
84. [Dar E.G.O [19267] — opis] [Combustion] 위력 최댓값 <style="upgradeHighlight">+21</style>\n\n전투 중 가장 처음으로 부여하는 [Combustion] 위력 부여 값 3배로 증가 (전투당 1회)\n\n적이 [Combustion] 발동으로 [Combustion] 피해를 입을 때, [Combustion] 위력만큼 분노 피해\n\n[Combustion] 위력, [Combustion] 횟수 또는 특수 화상을 부여하는 스킬의 피해량 <style="upgradeHighlight">+25%</style>
   źródło: EGOgift_TwiningThreads.json :: dataList[id=19267].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Max [Combustion] Potency <style="upgradeHighlight">+21</style>\n\nTriple the first [Combustion] Potency to be inflicted in the Encounter (once per Encounter)\n\nWhen an enemy takes [Combustion] damage from [Combustion] activation, deal Wrath damage equal to [Combustion] Potency\n\nSkills that inflict [Combustion] Potency, [Combustion] Count, or 'Unique Burn' deal <style="upgradeHighlight">+25%</style> damage
   PL: Maks. Siła [Combustion] <style="upgradeHighlight">+21</style>\n\nPierwsza nakładana w walce wartość Siły [Combustion] jest 3-krotnie większa (1 raz na walkę)\n\nGdy wróg otrzymuje obrażenia [Combustion] od wywołania [Combustion], zadaje mu obrażenia Gniewu równe Sile [Combustion]\n\nUmiejętności nakładające Siłę, Licznik [Combustion] lub Szczególne Podpalenie zadają <style="upgradeHighlight">+25%</style> obrażeń
85. [Dar E.G.O [29267] — nazwa] 달궈진 놋쇠++
   źródło: EGOgift_TwiningThreads.json :: dataList[id=29267].name
   limit: do 40 znaków
   EN: Searing Brass++
   PL: Rozżarzony Mosiądz++
86. [Dar E.G.O [29267] — opis] [Combustion] 위력 최댓값 +21\n\n전투 중 가장 처음으로 부여하는 [Combustion] 위력 부여 값 3배로 증가 (전투당 1회)\n\n적이 [Combustion] 발동으로 [Combustion] 피해를 입을 때, ([Combustion] 위력 x <style="upgradeHighlight">1.5</style>)만큼 분노 피해\n\n[Combustion] 위력, [Combustion] 횟수 또는 특수 화상을 부여하는 스킬의 피해량 <style="upgradeHighlight">+30%</style>
   źródło: EGOgift_TwiningThreads.json :: dataList[id=29267].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Max [Combustion] Potency +21\n\nTriple the first [Combustion] Potency to be inflicted in the Encounter (once per Encounter)\n\nWhen an enemy takes [Combustion] damage due to [Combustion] activation, deal Wrath damage equal to ([Combustion] Potency x <style="upgradeHighlight">1.5</style>)\n\nSkills that inflict [Combustion] Potency, [Combustion] Count, or 'Unique Burn' deal <style="upgradeHighlight">+30%</style> damage
   PL: Maks. Siła [Combustion] +21\n\nPierwsza nakładana w walce wartość Siły [Combustion] jest 3-krotnie większa (1 raz na walkę)\n\nGdy wróg otrzymuje obrażenia [Combustion] od wywołania [Combustion], zadaje mu obrażenia Gniewu równe (Siła [Combustion] x <style="upgradeHighlight">1,5</style>)\n\nUmiejętności nakładające Siłę, Licznik [Combustion] lub Szczególne Podpalenie zadają <style="upgradeHighlight">+30%</style> obrażeń
87. [Dar E.G.O [9268] — nazwa] 모든 것의 본능
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9268].name
   limit: do 40 znaków
   EN: Universal Instinct
   PL: Instynkt Wszystkiego
88. [Dar E.G.O [9268] — opis] 턴 종료시, 무작위 약지 소속 인격 ([Laceration]을 보유한 적 수)명에게 다음 턴에 무작위 죄악 속성 <noparse>피해량 증가</noparse> 1 부여 (턴당 인격 별로 최대 1회, 집중 전투일 경우 부위로 판정)\n\n약지 소속 인격이 가하는 피해량 +10%
   źródło: EGOgift_TwiningThreads.json :: dataList[id=9268].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Turn End: Randomly apply 1 Stack of a random Affinity's <noparse>Damage Up</noparse> next turn to (# of enemies with [Laceration]) The Ring-faction Identities (once per Identity per turn; in Focused Encounters, Parts)\n\nThe Ring-faction Identities deal +10% damage
   PL: Na koniec tury: tyle Tożsamości frakcji Serdecznego, ile wrogów posiada [Laceration] (losowo), następnej tury zyskuje 1 Wzrost Obrażeń losowego Grzechu (maks. 1 raz na turę na Tożsamość; w starciu skupionym liczone per Część)\n\nTożsamości frakcji Serdecznego zadają +10% obrażeń

## Dar E.G.O: EGOgift_a1c8p2
- plik gry: `EGOgift_a1c8p2.json`

89. [Dar E.G.O [2061] — nazwa] 동전
   źródło: EGOgift_a1c8p2.json :: dataList[id=2061].name
   limit: do 40 znaków
   EN: Coin
   PL: Monety
90. [Dar E.G.O [2061] — opis] 보유한 동전당 홍루의 가하는 피해량 +0.5%\n\n<i><color=#a16a3b>2차 가주 심사의 진행을 위한 물건. 동전을 모두 잃어버리거나 빼앗긴 후보자는 그 즉시 탈락한다.</color></i>
   źródło: EGOgift_a1c8p2.json :: dataList[id=2061].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#a16a3b>, </color>, </i>, \n
   EN: Hong Lu deals +0.5% damage for every Coin\n\n<i><color=#a16a3b>Artifacts used for the second round of the Family Hierarch Evaluation. Candidates without any remaining coins, either lost or taken by force, will be immediately eliminated.</color></i>
   PL: Hong Lu zadaje +0,5% obrażeń za każdą posiadaną Monetę\n\n<i><color=#a16a3b>Artefakt używany w 2. rundzie Egzaminu na Głowę Rodu. Kandydat, który straci wszystkie Monety — czy przez zgubienie, czy siłą — odpada natychmiast.</color></i>
91. [Dar E.G.O [2061] — opis skrócony] 보유한 동전당 홍루의 가하는 피해량 +0.5%
   źródło: EGOgift_a1c8p2.json :: dataList[id=2061].simpleDesc[abilityID=2061].simpleDesc
   limit: do 120 znaków
   EN: Hong Lu deals +0.5% damage for every Coin
   PL: Hong Lu zadaje +0,5% obrażeń za każdą posiadaną Monetę
92. [Dar E.G.O [2062] — nazwa] 낡은 출입증
   źródło: EGOgift_a1c8p2.json :: dataList[id=2062].name
   limit: do 40 znaków
   EN: Worn Entry Card
   PL: Znoszona Karta Wstępu
93. [Dar E.G.O [2062] — opis] 부서지고 낡은 출입증이다.\n어딘가의 문을 여는 데 쓸 수 있지 않을까?
   źródło: EGOgift_a1c8p2.json :: dataList[id=2062].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A broken and battered entry card.\nMaybe it opens a door somewhere.
   PL: Połamana i znoszona karta wstępu.\nMoże otwiera jakieś drzwi?
94. [Dar E.G.O [2063] — nazwa] 천왕보심단
   źródło: EGOgift_a1c8p2.json :: dataList[id=2063].name
   limit: do 50 znaków
   EN: Heavenly King's Heartmending Pill
   PL: Pigułka Króla Niebios
95. [Dar E.G.O [2063] — opis] 턴 종료 시 정신력이 가장 낮은 아군 1명의 정신력 10 회복.
   źródło: EGOgift_a1c8p2.json :: dataList[id=2063].desc
   limit: do 120 znaków
   EN: Turn End: 1 ally with the least SP heals 10 SP
   PL: Koniec tury: 1 sojusznik z najniższym SP odzyskuje 10 SP.
96. [Dar E.G.O [2063] — opis skrócony] 매 턴 종료 시 정신력이 가장 낮은 아군 1명의 정신력 10 회복
   źródło: EGOgift_a1c8p2.json :: dataList[id=2063].simpleDesc[abilityID=2063].simpleDesc
   limit: do 120 znaków
   EN: Every Turn End: 1 ally with the least SP heals 10 SP at Turn End
   PL: Na koniec każdej tury: 1 sojusznik z najniższym SP odzyskuje 10 SP
97. [Dar E.G.O [2064] — nazwa] 정연환
   źródło: EGOgift_a1c8p2.json :: dataList[id=2064].name
   limit: do 40 znaków
   EN: Tranquil Lotus Bolus
   PL: Granulat Spokojnego Lotosu
98. [Dar E.G.O [2064] — opis] 턴 종료 시 체력 비율이 제일 낮은 아군 1명의 체력을 대상의 최대 체력 5%만큼 회복 (소수점 버림).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2064].desc
   limit: do 120 znaków
   EN: Turn End: heal 5% HP for 1 ally with the least HP percentage (rounded down)
   PL: Koniec tury: 1 sojusznik z najniższym procentem HP odzyskuje HP równe 5% jego Maks. HP (zaokrąglenie w dół).
99. [Dar E.G.O [2064] — opis skrócony] 해당 캐릭터의 최대 체력의 5%만큼 회복
   źródło: EGOgift_a1c8p2.json :: dataList[id=2064].simpleDesc[abilityID=2064].simpleDesc
   limit: do 120 znaków
   EN: Heal the affected unit by 5% HP
   PL: Leczony odzyskuje 5% HP
100. [Dar E.G.O [2065] — nazwa] 혈화환
   źródło: EGOgift_a1c8p2.json :: dataList[id=2065].name
   limit: do 40 znaków
   EN: Sanguine Blossom Bolus
   PL: Granulat Krwawego Kwiatu
101. [Dar E.G.O [2065] — opis] 턴 시작 시 체력이 감소한 아군 중 현재 체력 비율이 가장 낮은 아군 1명의 피해량이 (대상의 잃은 체력 비율/4)%만큼 증가 (소수점 버림).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2065].desc
   limit: do 170 znaków
   EN: Turn Start: among allies who lost HP, 1 ally with the least HP percentage deals +(missing HP percentage / 4)% damage (rounded down)
   PL: Na początku tury: 1 sojusznik z najniższym procentem HP spośród rannych zadaje +(brakujący procent HP / 4)% obrażeń (zaokrąglenie w dół).
102. [Dar E.G.O [2065] — opis skrócony] 피해량이 해당 캐릭터의 (대상의 잃은 체력 비율/4)%만큼 증가
   źródło: EGOgift_a1c8p2.json :: dataList[id=2065].simpleDesc[abilityID=2065].simpleDesc
   limit: do 120 znaków
   EN: The affected unit deals +(missing HP percentage /4)% damage
   PL: Leczony zadaje +(brakujący procent HP / 4)% obrażeń
103. [Dar E.G.O [2066] — nazwa] 강인환
   źródło: EGOgift_a1c8p2.json :: dataList[id=2066].name
   limit: do 40 znaków
   EN: Tenacity Bolus
   PL: Granulat Wytrwałości
104. [Dar E.G.O [2066] — opis] 턴 시작 시 최대 체력이 가장 높은 아군 1명이 (이번 전투 동안 적에게 스킬 공격으로 피해를 받은 횟수)만큼 [DefenseUp] 얻음 (최대 6).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2066].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: 1 ally with the highest max HP gains [DefenseUp] equal to the number of times that unit was hit by the enemies' Skill Attacks (max 6)
   PL: Na początku tury: 1 sojusznik z najwyższym Maks. HP zyskuje tyle [DefenseUp], ile razy w tej walce był trafiony atakami Umiejętności wrogów (maks. 6).
105. [Dar E.G.O [2066] — opis skrócony] 피해를 받은 횟수만큼 방어 레벨 증가 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2066].simpleDesc[abilityID=2066].simpleDesc
   limit: do 120 znaków
   EN: Gain Defense Level Up equal to the number of times this unit was hit
   PL: Zyskuje Wzrost Poziomu Obrony równy liczbie otrzymanych trafień
106. [Dar E.G.O [2067] — nazwa] 거울 속의 꽃
   źródło: EGOgift_a1c8p2.json :: dataList[id=2067].name
   limit: do 40 znaków
   EN: Flower in the Mirror
   PL: Kwiat w Zwierciadle
107. [Dar E.G.O [2067] — opis] 매 턴 시작 시 [Burst]이 없는 모든 적에게 [Burst] 위력 3 부여, [Burst] 횟수 1 증가 (집중 전투일 경우, 모든 부위에 적용).\n\n<i><color=#a16a3b>흐르는 물 지는 꽃 둘 다 무정하여라.</color></i>
   źródło: EGOgift_a1c8p2.json :: dataList[id=2067].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#a16a3b>, </color>, </i>, \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Every Turn Start: inflict 3 [Burst] Potency and +1 [Burst] Count to all enemies without [Burst] (for Focused Encounters, all Parts)\n\n<i><color=#a16a3b>How heartless they are—the flowing stream and the wilting blossom both.</color></i>
   PL: Na początku każdej tury: nakłada 3 Siły [Burst] i +1 do Licznika [Burst] na wszystkich wrogów bez [Burst] (w starciu skupionym na wszystkich Częściach).\n\n<i><color=#a16a3b>Niech płynąca woda i opadający kwiat będą równie bezlitosne.</color></i>
108. [Dar E.G.O [2067] — opis skrócony] 파열이 없는 모든 적, 모든 부위에 파열 위력 3 부여, 파열 횟수 1 증가
   źródło: EGOgift_a1c8p2.json :: dataList[id=2067].simpleDesc[abilityID=2067].simpleDesc
   limit: do 120 znaków
   EN: Inflict 3 Rupture Potency and +1 Rupture Count to all enemies/Parts without Rupture
   PL: Nakłada 3 Siły Rozdarcia i +1 do Licznika Rozdarcia na wszystkich wrogów bez Rozdarcia
109. [Dar E.G.O [2068] — nazwa] 저주 받은 고문서
   źródło: EGOgift_a1c8p2.json :: dataList[id=2068].name
   limit: do 40 znaków
   EN: Accursed Codex
   PL: Przeklęty Dokument
110. [Dar E.G.O [2068] — opis] 스테이지 첫 턴 시작 시 전투에 참여한 모든 인격의 정신력이 5 감소하고, 해당 인격이 3턴 동안 [ShamrockResultUp], [ShamrockDamageUp] 1 얻음.
   źródło: EGOgift_a1c8p2.json :: dataList[id=2068].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [ShamrockResultUp], [ShamrockDamageUp]
   znaczenie tagów: [ShamrockResultUp] = 탐식 위력 증가 / Gluttony Power Up; [ShamrockDamageUp] = 탐식 피해량 증가 / Gluttony DMG Up
   EN: First Turn Start of an Encounter: every Identity on the field loses 5 SP and gains 1 [ShamrockResultUp] and 1 [ShamrockDamageUp] for 3 turns.
   PL: Na początku pierwszej tury walki: wszystkie Tożsamości na polu tracą 5 SP i przez 3 tury zyskują 1 [ShamrockResultUp] i 1 [ShamrockDamageUp].
111. [Dar E.G.O [2068] — opis skrócony] 배치된 인격의 정신력이 5 감소, 해당 인격이 3턴동안 탐식 위력 증가, 탐식 피해량 증가 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2068].simpleDesc[abilityID=2068].simpleDesc
   limit: do 130 znaków
   EN: Deployed units lose 5 SP; affected units gain Gluttony Power Up and Gluttony DMG Up for 3 turns
   PL: Rozstawione Tożsamości tracą 5 SP; dotknięte jednostki zyskują Wzrost Mocy Obżarstwa i Wzrost Obrażeń Obżarstwa na 3 tury
112. [Dar E.G.O [2069] — nazwa] 광기가 깃든 고문서
   źródło: EGOgift_a1c8p2.json :: dataList[id=2069].name
   limit: do 40 znaków
   EN: Madness-inscribed Codex
   PL: Dokument Przesiąknięty Szaleństwem
113. [Dar E.G.O [2069] — opis] 스테이지 첫 턴 시작 시 전투에 참여한 모든 인격의 정신력이 5 감소하고, 해당 인격이 이번 전투 동안 [ShamrockResultUp], [ShamrockDamageUp] 1 얻음.\n합 패배 시 정신력이 5 감소하고 해당 스킬의 마지막 코인이 [SuperCoin]으로 변경됨.(E.G.O 스킬 제외, 인격마다 턴당 1회 발동).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2069].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [ShamrockResultUp], [ShamrockDamageUp], [SuperCoin]
   znaczenie tagów: [ShamrockResultUp] = 탐식 위력 증가 / Gluttony Power Up; [ShamrockDamageUp] = 탐식 피해량 증가 / Gluttony DMG Up; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: First Turn Start of an Encounter: every Identity on the field loses 5 SP and gains 1 [ShamrockResultUp] and 1 [ShamrockDamageUp] for this Encounter.\nOn Clash Lose, lose 5 SP; convert the Skill's final Coin to [SuperCoin]. (except E.G.O Skills; once per turn per Identity)
   PL: Na początku pierwszej tury walki: wszystkie Tożsamości na polu tracą 5 SP i na czas tej walki zyskują 1 [ShamrockResultUp] i 1 [ShamrockDamageUp].\nPo przegranej Starciu: traci 5 SP, a ostatnia Moneta tej Umiejętności staje się [SuperCoin]. (z wyjątkiem Umiejętności E.G.O; 1 raz na turę na Tożsamość).
114. [Dar E.G.O [2069] — opis skrócony] 전투에 배치된 인격의 정신력이 5 감소, 해당 인격이 이번 전투동안 탐식 위력 증가, 탐식 피해량 증가 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2069].simpleDesc[abilityID=2069].simpleDesc
   limit: do 150 znaków
   EN: Combat Deployed units lose 5 SP; affected units gain Gluttony Power Up and Gluttony DMG Up for this Encounter
   PL: Rozstawione w walce Tożsamości tracą 5 SP; dotknięte zyskują Wzrost Mocy Obżarstwa i Wzrost Obrażeń Obżarstwa na czas tej walki
115. [Dar E.G.O [2069] — opis skrócony] 합 패배시 정신력 5 감소. 해당 스킬의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: EGOgift_a1c8p2.json :: dataList[id=2069].simpleDesc[abilityID=20691].simpleDesc
   limit: do 120 znaków
   EN: Lose 5 SP on Clash Lose. Convert the Skill's final Coin to Unbreakable Coin
   PL: Po przegranej Starciu traci 5 SP. Ostatnia Moneta Umiejętności staje się Monetą Niezniszczalną
116. [Dar E.G.O [2070] — nazwa] 물 속의 달
   źródło: EGOgift_a1c8p2.json :: dataList[id=2070].name
   limit: do 40 znaków
   EN: Moon in the Water
   PL: Księżyc w Wodzie
117. [Dar E.G.O [2070] — opis] 파열 위력이 5 이상 부여된 적에게 공격 적중 시 호흡 위력 1을 얻고, 자신의 호흡 횟수 1 증가 (스킬당 최대 3회).\n\n<i><color=#a16a3b>흐르는 물 지는 꽃 둘 다 무정하여라.</color></i>
   źródło: EGOgift_a1c8p2.json :: dataList[id=2070].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#a16a3b>, </color>, </i>, \n
   EN: On Hit against enemies with 5+ Rupture Potency: gain 1 Poise Potency and +1 Poise Count (3 times per Skill)\n\n<i><color=#a16a3b>How heartless they are—the flowing stream and the wilting blossom both.</color></i>
   PL: Przy trafieniu atakiem we wroga z co najmniej 5 Siły Rozdarcia zyskuje 1 Siłę Oddechu i +1 do własnego Licznika Oddechu (maks. 3 razy na Umiejętność).\n\n<i><color=#a16a3b>Niech płynąca woda i opadający kwiat będą równie bezlitosne.</color></i>
118. [Dar E.G.O [2070] — opis skrócony] 파열이 5 이상 부여된 적에게 공격 적중 시 호흡 위력 얻고, 자신의 호흡 횟수 증가
   źródło: EGOgift_a1c8p2.json :: dataList[id=2070].simpleDesc[abilityID=2070].simpleDesc
   limit: do 120 znaków
   EN: On Hit against enemies with 5+ Rupture: gain Poise Potency and Count
   PL: Przy trafieniu atakiem we wroga z co najmniej 5 Rozdarcia zyskuje Siłę Oddechu i Licznik Oddechu
119. [Dar E.G.O [2071] — nazwa] 꽃무덤
   źródło: EGOgift_a1c8p2.json :: dataList[id=2071].name
   limit: do 40 znaków
   EN: Flower Mound
   PL: Kwiatowy Grób
120. [Dar E.G.O [2071] — opis] [Burst]을 부여하는 스킬의 합 위력 +1, 피해량 +10%\n공격 종료 시 [Burst] 위력을 15 이상 보유한 대상이 사망했으면, 대상을 처치한 인격이 다음 턴에 [AttackUp] 2 얻음 (스킬당 최대 3회 발동).\n\n<i><color=#a16a3b>싸늘한 달빛 아래 꽃의 혼을 묻네</color></i>
   źródło: EGOgift_a1c8p2.json :: dataList[id=2071].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#a16a3b>, </color>, </i>, \n, [Burst], [AttackUp]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Skills that inflict [Burst]: Clash Power +1, deal +10% damage\nAttack End: If target with 15+ [Burst] Potency is defeated, the Identity that defeated said target gains 2 [AttackUp] next turn (3 times per Skill)\n\n<i><color=#a16a3b>Beneath the glacial moon I lay the blossom's soul to rest</color></i>
   PL: Umiejętności nakładające [Burst]: +1 do Mocy Starcia, +10% obrażeń\nNa koniec ataku: jeżeli cel z co najmniej 15 Siły [Burst] ginie, Tożsamość, która go pokonała, następnej tury zyskuje 2 [AttackUp] (maks. 3 razy na Umiejętność).\n\n<i><color=#a16a3b>Pod lodowatym blaskiem księżyca grzeję duszę kwiatu</color></i>
121. [Dar E.G.O [2071] — opis skrócony] 파열을 부여하는 스킬의 합 위력 +1, 피해량 +10%
   źródło: EGOgift_a1c8p2.json :: dataList[id=2071].simpleDesc[abilityID=2071].simpleDesc
   limit: do 120 znaków
   EN: Skills that inflict Rupture: Clash Power +1, deal +10% damage
   PL: Umiejętności nakładające Rozdarcie: +1 do Mocy Starcia, +10% obrażeń
122. [Dar E.G.O [2071] — opis skrócony] 파열이 15 이상 부여된 대상이 사망했으면, 다음 턴에 처치한 캐릭터가 공격 레벨 증가 2 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2071].simpleDesc[abilityID=20712].simpleDesc
   limit: do 140 znaków
   EN: If a target with 15+ Rupture is defeated, the unit that defeated it gains 2 Offense Level Up next turn
   PL: Jeżeli cel z co najmniej 15 Rozdarcia ginie, pokonująca go jednostka następnej tury zyskuje 2 Wzrosty Poziomu Ataku
123. [Dar E.G.O [2072] — nazwa] 전격부
   źródło: EGOgift_a1c8p2.json :: dataList[id=2072].name
   limit: do 40 znaków
   EN: Lightning Axe
   PL: Talizman Pioruna
124. [Dar E.G.O [2072] — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음.\n턴 종료 시, [Charge]이 2 이상이면, 다음 턴에 [ParryingResultUp] 1 얻음.\n[Charge] 횟수를 5 이상 소모한 스킬 적중 시 [Burst] 위력 1 부여 (스킬당 3회)
   źródło: EGOgift_a1c8p2.json :: dataList[id=2072].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [ParryingResultUp], [Burst]
   znaczenie tagów: [Charge] = 충전 / Charge; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [Burst] = 파열 / Rupture
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nTurn End: At 2+ [Charge], gain 1 [ParryingResultUp] next turn\nOn Hit with a Skill that consumed 5+ [Charge]: inflict 1 [Burst] Potency (3 times per Skill)
   PL: Za każde zużycie 10 łącznych Liczników [Charge] w tej walce zyskuje 1 [Charge].\nNa koniec tury, przy 2+ [Charge], następnej tury zyskuje 1 [ParryingResultUp].\nPrzy trafieniu Umiejętnością, która zużyła 5+ Liczników [Charge], nakłada 1 Siłę [Burst] (3 razy na Umiejętność)
125. [Dar E.G.O [2072] — opis skrócony] 충전 횟수 10을 소모할 때마다, 충전 1 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2072].simpleDesc[abilityID=2072].simpleDesc
   limit: do 120 znaków
   EN: Gain 1 Charge every time this unit consumes 10 Charge Count
   PL: Za każde zużycie 10 Liczników Ładowania zyskuje 1 Ładowanie
126. [Dar E.G.O [2072] — opis skrócony] 충전이 2 이상이면, 다음 턴에 합 위력 증가 1 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2072].simpleDesc[abilityID=20721].simpleDesc
   limit: do 120 znaków
   EN: At 2+ Charge, gain 1 Clash Power Up next turn
   PL: Przy 2+ Ładowania następnej tury zyskuje 1 Wzrost Mocy Starcia
127. [Dar E.G.O [2072] — opis skrócony] 충전 횟수를 5 이상 소모한 스킬 적중 시 파열 1 부여
   źródło: EGOgift_a1c8p2.json :: dataList[id=2072].simpleDesc[abilityID=20722].simpleDesc
   limit: do 120 znaków
   EN: On Hit with Skills that consumed 5+ Charge Count: inflict 1 Rupture
   PL: Przy trafieniu Umiejętnością, która zużyła 5+ Liczników Ładowania, nakłada 1 Rozdarcie
128. [Dar E.G.O [2073] — nazwa] 심파부
   źródło: EGOgift_a1c8p2.json :: dataList[id=2073].name
   limit: do 40 znaków
   EN: Heartrender Talisman
   PL: Talizman Rozbijający Serca
129. [Dar E.G.O [2073] — opis] 주살 효과가 부여된 적에게 가하는 탐식 속성 스킬의 피해량 +10%.\n전투 시작시 정신력이 -15 이하인 인격이 사용하는 스킬의 마지막 코인이 [SuperCoin]으로 변경됨 (인격마다 턴당 1회, 가장 왼쪽 슬롯에 사용한 스킬부터 적용, E.G.O 스킬 제외).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2073].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Gluttony Skills deal +10% damage against enemies with Deathrite effects\nFor Identities at -15 or less SP at Combat Start: convert the final Coin for their Skills into [SuperCoin] (once per turn per Identity; prioritizes the Skill in the leftmost Skill Slot; except E.G.O Skills)
   PL: Umiejętności Obżarstwa zadają +10% obrażeń wrogom z nałożonym Obrzędem Śmierci.\nNa początku walki: ostatnia Moneta Umiejętności używanej przez Tożsamości z SP ≤ -15 staje się [SuperCoin] (1 raz na turę na Tożsamość; zaczynając od Umiejętności w najbardziej lewym slocie; z wyjątkiem Umiejętności E.G.O).
130. [Dar E.G.O [2073] — opis skrócony] 주살 효과가 부여된 적에게 가하는 탐식 속성 스킬의 피해량 +10%
   źródło: EGOgift_a1c8p2.json :: dataList[id=2073].simpleDesc[abilityID=2073].simpleDesc
   limit: do 120 znaków
   EN: Gluttony Skills deal +10% damage against enemies with Deathrite effects
   PL: Umiejętności Obżarstwa zadają +10% obrażeń wrogom z nałożonym Obrzędem Śmierci
131. [Dar E.G.O [2073] — opis skrócony] 정신력이 -15 이하면, 사용하는 스킬의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: EGOgift_a1c8p2.json :: dataList[id=2073].simpleDesc[abilityID=20731].simpleDesc
   limit: do 120 znaków
   EN: At -15 or less SP: convert the final Coin for their Skills into Unbreakable Coin
   PL: Przy SP ≤ -15: ostatnia Moneta użytej Umiejętności staje się Monetą Niezniszczalną
132. [Dar E.G.O [2074] — nazwa] 절혈도
   źródło: EGOgift_a1c8p2.json :: dataList[id=2074].name
   limit: do 40 znaków
   EN: Bloodsevering Blade
   PL: Ostrze Przecinające Krew
133. [Dar E.G.O [2074] — opis] 체력이 감소한 상태일 때 합 위력 +1.\n해당 인격이 공격 적중 시, 적중한 대상의 ([Laceration] 위력 + [Laceration] 횟수)당 피해량 +1% (최대 20%)
   źródło: EGOgift_a1c8p2.json :: dataList[id=2074].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Clash Power +1 when not at full HP.\nWhen an affected unit hits, deal +1% damage for every ([Laceration] Potency on target + [Laceration] Count on target) (max 20%)
   PL: +1 do Mocy Starcia, gdy HP nie jest pełne.\nPrzy trafieniu Tożsamość zadaje +1% obrażeń za każdą (Siłę [Laceration] celu + Licznik [Laceration] celu) (maks. 20%)
134. [Dar E.G.O [2074] — opis skrócony] 체력이 감소한 상태일 때 합 위력 +1
   źródło: EGOgift_a1c8p2.json :: dataList[id=2074].simpleDesc[abilityID=2074].simpleDesc
   limit: do 120 znaków
   EN: When not at full HP, Clash Power +1
   PL: Gdy HP nie jest pełne: +1 do Mocy Starcia
135. [Dar E.G.O [2074] — opis skrócony] 공격 적중 시 대상의 (출혈 위력 + 출혈 횟수)당 피해량 +1%
   źródło: EGOgift_a1c8p2.json :: dataList[id=2074].simpleDesc[abilityID=20741].simpleDesc
   limit: do 120 znaków
   EN: On Hit, deal +1% damage for every (Bleed Potency on target + Bleed Count on target)
   PL: Przy trafieniu zadaje +1% obrażeń za każdą (Siłę Krwawienia celu + Licznik Krwawienia celu)
136. [Dar E.G.O [2075] — nazwa] 금강환
   źródło: EGOgift_a1c8p2.json :: dataList[id=2075].name
   limit: do 40 znaków
   EN: Jin Gang Bolus
   PL: Granulat Jin Gang
137. [Dar E.G.O [2075] — opis] 전투 중 피해를 입으면, 다음 턴 동안 스킬 최종 위력 +1, 가하는 피해량 +10% (스스로 피해를 받는 경우에도 발동).\n체력이 1이 되는 피해를 받았을 때, 최대 체력의 50%만큼 체력을 회복하고, 이번 전투 동안 해당 인격이 턴 시작 시 [Enhancement] 2 얻음 (전투당 1회).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2075].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: When taking damage, gain Skill Final Power +1 and deal +10% damage (activates for self-damages as well) next turn\nWhen taking damage that brings a unit's HP down to 1, heal 50% HP, and the affected unit gains 2 [Enhancement] at Turn Start for the duration of that Encounter (once per Encounter)
   PL: Po otrzymaniu obrażeń następnej tury zyskuje +1 do Mocy Końcowej Umiejętności i +10% obrażeń (działa również przy obrażeniach własnych).\nGdy otrzymane obrażenia sprowadzą HP do 1, odzyskuje HP równe 50% Maks. HP, a dotknięta Tożsamość zyskuje 2 [Enhancement] na początku tury na czas tej walki (1 raz na walkę).
138. [Dar E.G.O [2075] — opis skrócony] 다음 턴 동안 스킬 최종 위력 +1, 가하는 피해량 +10%
   źródło: EGOgift_a1c8p2.json :: dataList[id=2075].simpleDesc[abilityID=2075].simpleDesc
   limit: do 120 znaków
   EN: Skill Final Power +1, deal +10% damage next turn
   PL: Następnej tury: +1 do Mocy Końcowej Umiejętności, +10% obrażeń
139. [Dar E.G.O [2075] — opis skrócony] 최대 체력의 50%만큼 회복. 이번 전투 동안 공격 위력 증가 2 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2075].simpleDesc[abilityID=20751].simpleDesc
   limit: do 120 znaków
   EN: Heal 50% HP and gain 2 Attack Power Up for this Encounter
   PL: Leczy 50% Maks. HP i na czas tej walki zyskuje 2 Wzrosty Mocy Ataku
140. [Dar E.G.O [2076] — nazwa] 빛바랜 포스터
   źródło: EGOgift_a1c8p2.json :: dataList[id=2076].name
   limit: do 40 znaków
   EN: Faded Poster
   PL: Wyblakły Plakat
141. [Dar E.G.O [2076] — opis] [편성 1번, 8번 전용 효과]\n공격 종료 시 대상이 사망했으면, [Breath] 위력 2 얻고 [Breath] 횟수 2 증가.\n이번 전투 동안 자신의 공격 종료 시 사망한 적 1명당 공격 레벨 +1 (최대 3).
   źródło: EGOgift_a1c8p2.json :: dataList[id=2076].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: [Effects apply only to #1, #8 Deployed Identities]\nAttack End: If the target is defeated, gain 2 [Breath] Potency and +2 [Breath] Count.\nFor this Encounter, each unit gains +1 Offense Level for every 1 enemy that is defeated at the 'Attack End' timing (max 3)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #1, #8]\nNa koniec ataku: jeżeli cel ginie, zyskuje 2 Siły [Breath] i +2 do Licznika [Breath].\nNa czas tej walki: za każdego wroga pokonanego na koniec ataku +1 do Poziomu Ataku (maks. 3).
142. [Dar E.G.O [2076] — opis skrócony] 호흡 위력 2 얻음, 호흡 횟수 2 증가
   źródło: EGOgift_a1c8p2.json :: dataList[id=2076].simpleDesc[abilityID=2076].simpleDesc
   limit: do 120 znaków
   EN: Gain 2 Poise Potency and +2 Poise Count
   PL: Zyskuje 2 Siły Oddechu i +2 do Licznika Oddechu
143. [Dar E.G.O [2076] — opis skrócony] 사망한 적 1명당 공격 레벨 +1
   źródło: EGOgift_a1c8p2.json :: dataList[id=2076].simpleDesc[abilityID=20761].simpleDesc
   limit: do 120 znaków
   EN: Offense Level +1 for every defeated enemy
   PL: +1 do Poziomu Ataku za każdego pokonanego wroga
144. [Dar E.G.O [2077] — nazwa] 깊게 패인 손톱자국
   źródło: EGOgift_a1c8p2.json :: dataList[id=2077].name
   limit: do 40 znaków
   EN: Deep Claw Marks
   PL: Głębokie Ślady Pazurów
145. [Dar E.G.O [2077] — opis] 대기 해제된 아군이 3턴 동안 [ParryingResultUp] 1 얻음.
   źródło: EGOgift_a1c8p2.json :: dataList[id=2077].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain 1 [ParryingResultUp] for 3 turns after Substituting in.
   PL: Sojusznik wchodzący z Rezerwy zyskuje 1 [ParryingResultUp] na 3 tury.
146. [Dar E.G.O [2077] — opis skrócony] 대기 해제 시 합 위력 증가 1 얻음
   źródło: EGOgift_a1c8p2.json :: dataList[id=2077].simpleDesc[abilityID=20771].simpleDesc
   limit: do 120 znaków
   EN: Gain 1 Clash Power Up for 3 turns after Substituting in
   PL: Po wejściu z Rezerwy zyskuje 1 Wzrost Mocy Starcia na 3 tury
147. [Dar E.G.O [2078] — nazwa] 공멸일의 기억
   źródło: EGOgift_a1c8p2.json :: dataList[id=2078].name
   limit: do 60 znaków
   EN: The Memory of Kong Family Annihilation
   PL: Pamięć Dnia Zagłady Rodu Kong
148. [Dar E.G.O [2078] — opis] 홍루의 레벨이 55레벨로 상승\n홍루 인격의 동기화 단계, E.G.O의 환상해석 단계가 4단계로 상승.\n\n<i><color=#a16a3b>' 공멸일을 기억하라.\n공씨 가문은 그 죄가 한없이 무거워 멸문하였다.\n홍원의 계율을 지키지 않은 업, 가련하지도 않고 우스울 뿐이니.\n이렇듯 응보는 반드시 도래한다.'</color></i>
   źródło: EGOgift_a1c8p2.json :: dataList[id=2078].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#a16a3b>, </color>, </i>, \n
   EN: Hong Lu's level rises to 55\nHong Lu's Uptie and Threadspin Tiers rise to Tier 4\n\n<i><color=#a16a3b>'Remember the day ruin came to the Kong family,\nwho have brought this destruction upon themselves through their grave transgressions.\nTo violate the laws of Hongyuan is no tragedy—as such, it warrants no pity, only humiliation and scorn.\nThis site of history stands as a monument to the inevitability of karma.'</color></i>
   PL: Poziom Hong Lu rośnie do 55\nPoziomy Synchronizacji Hong Lua i Splotu Nici jego E.G.O rosną do poziomu 4\n\n<i><color=#a16a3b>„Pamiętajcie dzień zagłady Rodu Kong,\nktóry za winy bezmiernie ciężkie poniósł zagładę domu.\nCzyn złamania praw Hongyuan nie budzi litości — jedynie śmiech.\nTak wiec odwet niechybnie nadejdzie.”</color></i>
149. [Dar E.G.O [2079] — nazwa] 붉은 출입증
   źródło: EGOgift_a1c8p2.json :: dataList[id=2079].name
   limit: do 40 znaków
   EN: Red Entry Card
   PL: Czerwona Karta Wstępu
150. [Dar E.G.O [2079] — opis] 부서지고 낡은 붉은색 출입증이다.\n어딘가의 문을 여는 데 쓸 수 있지 않을까?
   źródło: EGOgift_a1c8p2.json :: dataList[id=2079].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A broken and battered red entry card.\nMaybe it opens a door somewhere.
   PL: Połamana i znoszona czerwona karta wstępu.\nMoże otwiera jakieś drzwi?

## Dar E.G.O: EGOgift_cultivation
- plik gry: `EGOgift_cultivation.json`

151. [Dar E.G.O [9819] — nazwa] 혈염도
   źródło: EGOgift_cultivation.json :: dataList[id=9819].name
   limit: do 40 znaków
   EN: Bloodflame Sword
   PL: Krwawopłomienny Miecz
152. [Dar E.G.O [9819] — opis] 스테이지 첫 턴 시작 시, 자신에게 [Combustion]을 부여하는 기본 공격 스킬을 보유한 인격이 [Combustion] 5를 얻고, 정신력 8 회복\n\n흑수-유 소속 인격이 유지 또는 회복 가능한 최대 체력의 상한선이 49%로 고정되는 대신 받는 피해량과 자신이 받는 회복량이 50% 감소 (E.G.O 기프트로 인한 회복 제외)
   źródło: EGOgift_cultivation.json :: dataList[id=9819].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: First Turn Start of an Encounter: Identities with Base Attack Skills that gain [Combustion] gain 5 [Combustion] and heal 8 SP\n\nFor Heishou Pack - You Branch Identities: HP gets capped to 49% of Max HP. In return, take 50% less damage and receive 50% reduced heal (except healing from E.G.O Gifts)
   PL: Na początku pierwszej tury walki: Tożsamości z Podstawowymi Umiejętnościami ataku nakładającymi [Combustion] zyskują 5 [Combustion] i odzyskują 8 SP\n\nTożsamości frakcji Heishou - Gałąź You mają Maks. HP ograniczone do 49%; w zamian otrzymują o 50% mniej obrażeń i o 50% mniej leczenia (z wyjątkiem leczenia z Darów E.G.O)
153. [Dar E.G.O [9819] — opis skrócony] [Combustion] 얻고, 공격 레벨 증가, 정신력 회복
   źródło: EGOgift_cultivation.json :: dataList[id=9819].simpleDesc[abilityID=9819].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Gain [Combustion], Offense Levels, and heal SP
   PL: Zyskuje [Combustion], Wzrosty Poziomu Ataku i odzyskuje SP
154. [Dar E.G.O [9819] — opis skrócony] 최대 체력의 상한선 고정, 받는 피해량과 회복량 감소
   źródło: EGOgift_cultivation.json :: dataList[id=9819].simpleDesc[abilityID=98191].simpleDesc
   limit: do 120 znaków
   EN: HP gets capped. Take less damage and heal less HP.
   PL: Maks. HP ograniczone. Otrzymuje mniej obrażeń i mniejsze leczenie.
155. [Dar E.G.O [9820] — nazwa] 흑철마갑
   źródło: EGOgift_cultivation.json :: dataList[id=9820].name
   limit: do 40 znaków
   EN: Blackiron Barding
   PL: Czarnożelazna Zbroja
156. [Dar E.G.O [9820] — opis] 턴 시작 시, 방어 레벨이 가장 높은 아군 하나에게 보호막 (방어 레벨/3) 부여 (흑수-오 소속 인격을 우선으로 지정. 보호막 최대 15)\n\n보호막을 보유한 아군이 합 승리시, 적에게 (속도/2)만큼 [Vibration] 위력을 부여하고, 다음 턴에 [Agility] 2, [DefenseUp] 2 얻음(턴 당, 인격 당 1회)
   źródło: EGOgift_cultivation.json :: dataList[id=9820].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [Agility], [DefenseUp]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: apply (Defense Level / 3) Shield to 1 ally with the highest Defense Level (prioritizes Heishou - Wu Identities; max Shield 15)\n\nWhen allies with Shield win a Clash, inflict (Speed / 2) [Vibration] Potency; then, gain 2 [Agility] and 2 [DefenseUp] next turn (once per turn per Identity)
   PL: Na początku tury: nakłada Tarczę (Poziom Obrony/3) na 1 sojusznika z najwyższym Poziomem Obrony (priorytet: Tożsamości frakcji Heishou - Gałąź Wu; maks. Tarcza 15)\n\nGdy sojusznik z Tarczą wygra Starcie, nakłada na wroga (Prędkość/2) Siły [Vibration], a następna tura zyskuje 2 [Agility] i 2 [DefenseUp] (1 raz na turę na Tożsamość)
157. [Dar E.G.O [9820] — opis skrócony] 아군 하나에게 보호막, [Agility] 부여
   źródło: EGOgift_cultivation.json :: dataList[id=9820].simpleDesc[abilityID=9820].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Apply Shield & [Agility] to an ally
   PL: Nakłada Tarczę i [Agility] na sojusznika
158. [Dar E.G.O [9820] — opis skrócony] 속도 비례 진동 위력 부여, 다음 턴에 방어 레벨 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9820].simpleDesc[abilityID=98201].simpleDesc
   limit: do 120 znaków
   EN: Inflict Tremor Potency based on Speed; gain Defense Level next turn
   PL: Nakłada Siłę Wstrząsu proporcjonalną do Prędkości; następna tura zyskuje Poziom Obrony
159. [Dar E.G.O [9821] — nazwa] 마음을 닫는 붉은 천
   źródło: EGOgift_cultivation.json :: dataList[id=9821].name
   limit: do 50 znaków
   EN: Red Cloth that Closes the Heart
   PL: Czerwona Tkanina Zamykająca Serce
160. [Dar E.G.O [9821] — opis] [편성 1번 인격 전용 효과]\n\n다른 아군이 일방공격으로 적에게 적중 시, 다음 턴에 [AttackUp] 1 얻음 (턴 당, 인격 당 1회, 턴 당 최대 6회)\n\n다른 아군이 [RetreatForCommon] 했다면, 다음 턴에 [SlashResultUp] 1, [SlashDamageUp] 1 얻음 (턴 당 최대 1회)\n\n조건을 모두 만족했다면, 다음 턴에 [ResultEnhancement] 1 얻음 (턴 당 최대 1회)
   źródło: EGOgift_cultivation.json :: dataList[id=9821].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [RetreatForCommon], [SlashResultUp], [SlashDamageUp], [ResultEnhancement]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [Effects apply only to #1 Deployed Identity]\n\nWhen other allies use an Unopposed Attack to hit an enemy, gain 1 [AttackUp] next turn (they can activate this only once per turn per Identity; effect itself activates up to 6 times per turn)\n\nWhen other allies [RetreatForCommon], gain 1 [SlashResultUp] and 1 [SlashDamageUp] next turn (once per turn)\n\nWhen all above conditions are met, gain 1 [ResultEnhancement] next turn (once per turn)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #1]\n\nGdy inni sojusznicy trafią wroga Atakiem Jednostronnym, następna tura zyskuje 1 [AttackUp] (każda Tożsamość wywołuje to 1 raz na turę; efekt działa maks. 6 razy na turę)\n\nGdy inni sojusznicy wykonają [RetreatForCommon], następna tura zyskuje 1 [SlashResultUp] i 1 [SlashDamageUp] (maks. 1 raz na turę)\n\nJeżeli wszystkie powyższe warunki są spełnione, następna tura zyskuje 1 [ResultEnhancement] (maks. 1 raz na turę)
161. [Dar E.G.O [9821] — opis skrócony] 다음 턴에 공격 레벨 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9821].simpleDesc[abilityID=9821].simpleDesc
   limit: do 120 znaków
   EN: Gain Offense Level next turn
   PL: Następna tura zyskuje Poziom Ataku
162. [Dar E.G.O [9821] — opis skrócony] 다음 턴에 참격 위력 증가, 참격 피해량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9821].simpleDesc[abilityID=98211].simpleDesc
   limit: do 120 znaków
   EN: Gain Slash Power Up and Slash DMG Up next turn
   PL: Następna tura zyskuje Wzrost Mocy Cięcia i Wzrost Obrażeń Cięcia
163. [Dar E.G.O [9821] — opis skrócony] 다음 턴에 위력 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9821].simpleDesc[abilityID=98212].simpleDesc
   limit: do 120 znaków
   EN: Gain Power Up next turn
   PL: Następna tura zyskuje Wzrost Mocy
164. [Dar E.G.O [9822] — nazwa] 덕목 - 지(智)
   źródło: EGOgift_cultivation.json :: dataList[id=9822].name
   limit: do 40 znaków
   EN: Virtue - Zhi (智)
   PL: Cnota - Zhi (智)
165. [Dar E.G.O [9822] — opis] [편성 6번 인격 전용 효과]\n\n[Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬(E.G.O 스킬 포함)을 사용하여 합 승리 시, 다음 턴에 [DefenseUp] 2 얻음 (턴 당 최대 1회)\n- 가주 후보 소속이면 추가 효과로 다음 턴에 [Agility] 1 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9822].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [DefenseUp], [Agility]
   znaczenie tagów: [Burst] = 파열 / Rupture; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Agility] = 신속 / Haste
   EN: [Effects apply only to #6 Deployed Identity]\n\nWhen using an Attack Skill(including E.G.O Skills) that inflicts [Burst] Potency or [Burst] Count to win a clash, gain 2 [DefenseUp] next turn (once per turn)\n- If this unit is a Family Hierarch Candidate: also gain 1 [Agility] next turn
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #6]\n\nGdy wygra Starcie Umiejętnością ataku (łącznie z Umiejętnościami E.G.O) nakładającą Siłę lub Licznik [Burst], następna tura zyskuje 2 [DefenseUp] (maks. 1 raz na turę)\n- Frakcja Kandydata na Głowę Rodu dodatkowo zyskuje 1 [Agility] następnej tury
166. [Dar E.G.O [9822] — opis skrócony] 방어 레벨 증가, 가주 후보 소속이면 추가 효과로 다음 턴에 [Agility] 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9822].simpleDesc[abilityID=9822].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Gain Defense Level Up. Family Hierarch Candidate Faction gains [Agility] next turn as well
   PL: Zyskuje Wzrost Poziomu Obrony. Frakcja Kandydata na Głowę Rodu również zyskuje [Agility] następnej tury
167. [Dar E.G.O [9823] — nazwa] 덕목 - 용(勇)
   źródło: EGOgift_cultivation.json :: dataList[id=9823].name
   limit: do 40 znaków
   EN: Virtue - Yong (勇)
   PL: Cnota - Yong (勇)
168. [Dar E.G.O [9823] — opis] [편성 6번 인격 전용 효과]\n\n[Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬(E.G.O 스킬 포함)을 사용하여 합 승리 시, 다음 턴에 [AttackUp] 2 얻음 (턴 당 최대 1회)\n- 가주 후보 소속이면 추가 효과로 다음 턴에 [AttackUp] 3 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9823].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [AttackUp]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [Effects apply only to #6 Deployed Identity]\n\nWhen using an Attack Skill(including E.G.O Skills) that inflicts [Burst] Potency or [Burst] Count to win a clash, gain 2 [AttackUp] next turn (once per turn)\n- If this unit is a Family Hierarch Candidate: also gain 3 [AttackUp] next turn
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #6]\n\nGdy wygra Starcie Umiejętnością ataku (łącznie z Umiejętnościami E.G.O) nakładającą Siłę lub Licznik [Burst], następna tura zyskuje 2 [AttackUp] (maks. 1 raz na turę)\n- Frakcja Kandydata na Głowę Rodu dodatkowo zyskuje 3 [AttackUp] następnej tury
169. [Dar E.G.O [9823] — opis skrócony] 공격 레벨 증가, 가주 후보 소속이면 추가 효과로 다음 턴에 [AttackUp] 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9823].simpleDesc[abilityID=9823].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Gain Offense Level Up. Family Hierarch Candidate Faction gains [AttackUp] next turn as well
   PL: Zyskuje Wzrost Poziomu Ataku. Frakcja Kandydata na Głowę Rodu również zyskuje [AttackUp] następnej tury
170. [Dar E.G.O [9824] — nazwa] 덕목 - 인(仁)
   źródło: EGOgift_cultivation.json :: dataList[id=9824].name
   limit: do 40 znaków
   EN: Virtue - Ren (仁)
   PL: Cnota - Ren (仁)
171. [Dar E.G.O [9824] — opis] [편성 6번 인격 전용 효과]\n\n[Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬(E.G.O 스킬 포함)을 사용하여 합 승리 시, 체력 15 회복 (턴 당 최대 1회)\n- 가주 후보 소속이면 추가 효과로 다음 턴에 [Protection] 1 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9824].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Protection]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Protection] = 보호 / Protection
   EN: [Effects apply only to #6 Deployed Identity]\n\nWhen using an Attack Skill(including E.G.O Skills) that inflicts [Burst] Potency or [Burst] Count to win a clash, heal 15 HP (once per turn)\n- If this unit is a Family Hierarch Candidate: also gain 1 [Protection] next turn
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #6]\n\nGdy wygra Starcie Umiejętnością ataku (łącznie z Umiejętnościami E.G.O) nakładającą Siłę lub Licznik [Burst], leczy 15 HP (maks. 1 raz na turę)\n- Frakcja Kandydata na Głowę Rodu dodatkowo zyskuje 1 [Protection] następnej tury
172. [Dar E.G.O [9824] — opis skrócony] 체력 회복, 가주 후보 소속이면 추가 효과로 다음 턴에 [Protection] 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9824].simpleDesc[abilityID=9824].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Heal HP. Family Hierarch Candidate Faction gains [Protection] next turn as well
   PL: Leczy HP. Frakcja Kandydata na Głowę Rodu również zyskuje [Protection] następnej tury
173. [Dar E.G.O [9825] — nazwa] 절차탁마(切磋琢磨)
   źródło: EGOgift_cultivation.json :: dataList[id=9825].name
   limit: do 60 znaków
   EN: Cultivation: Cut, File, Carve, Polish
   PL: Szlifowanie: Tnij, Piłuj, Rzeźb, Poleruj (切磋琢磨)
174. [Dar E.G.O [9825] — opis] [편성 6번 인격 전용 효과]\n\n[Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬(E.G.O 스킬 포함)을 사용하여 합 승리 시, 체력 20 회복하고 다음 턴에 [AttackUp] 3, [DefenseUp] 3 얻음 (턴 당 최대 1회)\n- 가주 후보 소속이면 추가 효과로 자신을 포함한 모든 아군에게 다음 턴에 [Agility] 1, [Protection] 1, [AttackUp] 3 부여
   źródło: EGOgift_cultivation.json :: dataList[id=9825].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [AttackUp], [DefenseUp], [Agility], [Protection]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Agility] = 신속 / Haste; [Protection] = 보호 / Protection
   EN: [Effects apply only to #6 Deployed Identity]\n\nWhen using an Attack Skill(including E.G.O Skills) that inflicts [Burst] Potency or [Burst] Count to win a clash, heal 20 HP, gain 3 [AttackUp], and gain 3 [DefenseUp] next turn (once per turn)\n- If this unit is a Family Hierarch Candidate: apply 1 [Agility], 1 [Protection], and 3 [AttackUp] to all allies, including this unit
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #6]\n\nGdy wygra Starcie Umiejętnością ataku (łącznie z Umiejętnościami E.G.O) nakładającą Siłę lub Licznik [Burst], leczy 20 HP, a następna tura zyskuje 3 [AttackUp] i 3 [DefenseUp] (maks. 1 raz na turę)\n- Frakcja Kandydata na Głowę Rodu dodatkowo nakłada na wszystkich sojuszników, łącznie z tą jednostką, 1 [Agility], 1 [Protection] i 3 [AttackUp] następnej tury
175. [Dar E.G.O [9825] — opis skrócony] 공격 레벨 증가, 방어 레벨 증가, 체력 회복, 가주 후보 소속이면 추가 효과로 자신을 포함한 모든 아군에게 다음 턴에 신속, 보호, 공격 레벨 증가 부여
   źródło: EGOgift_cultivation.json :: dataList[id=9825].simpleDesc[abilityID=9825].simpleDesc
   limit: do 230 znaków
   EN: Gain Offense Level Up, Defense Level Up, and heal HP. If this unit is a Family Hierarch Candidate, apply Haste, Protection, and Offense Level Up to all allies next turn as well
   PL: Zyskuje Wzrost Poziomu Ataku, Wzrost Poziomu Obrony i leczy HP. Frakcja Kandydata na Głowę Rodu dodatkowo nakłada Pośpiech, Ochronę i Wzrost Poziomu Ataku na wszystkich sojuszników następnej tury
176. [Dar E.G.O [9826] — nazwa] 소흥주
   źródło: EGOgift_cultivation.json :: dataList[id=9826].name
   limit: do 40 znaków
   EN: Shaoxing Wine
   PL: Wino Shaoxing
177. [Dar E.G.O [9826] — opis] [편성 2번 인격 전용 효과]\n\n자신의 잃은 체력 1%당 기본 스킬로 가하는 피해량 +1%(최대 10%)
   źródło: EGOgift_cultivation.json :: dataList[id=9826].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Effects apply only to #2 Deployed Identity]\n\nBase Skills deal +1% damage for every 1% missing HP on self (max 10%)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #2]\n\nPodstawowe Umiejętności zadają +1% obrażeń za każde 1% brakującego własnego HP (maks. 10%)
178. [Dar E.G.O [9826] — opis skrócony] 잃은 체력 비례 가하는 피해량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9826].simpleDesc[abilityID=9826].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage based on missing HP
   PL: Zadaje więcej obrażeń zależnie od brakującego HP
179. [Dar E.G.O [19826] — nazwa] 소흥주+
   źródło: EGOgift_cultivation.json :: dataList[id=19826].name
   limit: do 40 znaków
   EN: Shaoxing Wine+
   PL: Wino Shaoxing+
180. [Dar E.G.O [19826] — opis] [편성 2번, <style="upgradeHighlight">4번</style> 인격 전용 효과]\n\n자신의 잃은 체력 1%당 기본 스킬로 가하는 피해량 +1%(최대 10%)
   źródło: EGOgift_cultivation.json :: dataList[id=19826].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n
   EN: [Effects apply only to #2 <style="upgradeHighlight">and #4 Deployed Identities</style>]\n\nBase Skills deal +1% damage for every 1% missing HP on self (max 10%)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #2, <style="upgradeHighlight">#4</style>]\n\nPodstawowe Umiejętności zadają +1% obrażeń za każde 1% brakującego własnego HP (maks. 10%)
181. [Dar E.G.O [19826] — opis skrócony] 잃은 체력 비례 가하는 피해량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=19826].simpleDesc[abilityID=19826].simpleDesc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Dar E.G.O [29826] — nazwa] 소흥주++
   źródło: EGOgift_cultivation.json :: dataList[id=29826].name
   limit: do 40 znaków
   EN: Shaoxing Wine++
   PL: Wino Shaoxing++
183. [Dar E.G.O [29826] — opis] [편성 2번, 4번, <style="upgradeHighlight">6번</style> 인격 전용 효과]\n\n자신의 잃은 체력 1%당 기본 스킬로 가하는 피해량 +1%(최대 10%)
   źródło: EGOgift_cultivation.json :: dataList[id=29826].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n
   EN: [Effects apply only to #2 ,#4, <style="upgradeHighlight">and #6</style> Deployed Identities]\n\nBase Skills deal +1% damage for every 1% missing HP on self (max 10%)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #2, #4, <style="upgradeHighlight">#6</style>]\n\nPodstawowe Umiejętności zadają +1% obrażeń za każde 1% brakującego własnego HP (maks. 10%)
184. [Dar E.G.O [29826] — opis skrócony] 잃은 체력 비례 가하는 피해량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=29826].simpleDesc[abilityID=29826].simpleDesc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Dar E.G.O [9827] — nazwa] 가족의 원망
   źródło: EGOgift_cultivation.json :: dataList[id=9827].name
   limit: do 40 znaków
   EN: The Family's Resentment
   PL: Uraza Rodu
186. [Dar E.G.O [9827] — opis] 스테이지 내 혈찬의 생산량이 2배로 적용됨\n[Laceration] 위력, [Laceration] 횟수 또는 특수 출혈을 부여하는 스킬 공격 종료 시, 입힌 체력 피해량의 30% 만큼 체력 회복. (최대 20)\n- 위 효과로 체력을 회복했을 경우 다음 턴 시작 시 [Enhancement] 1 얻음 (최대 2)\n\n[BloodDinner_Common_Accumulation] 50당, 다음 턴 시작 시 모든 아군의 [AttackUp] 1 얻음 (최대 5)\n라만차랜드 소속의 경우 추가로 자신의 [BloodDinner_Accumulation] 30당, 다음 턴 시작 시 [AttackUp] 1 얻음 (최대 3)
   źródło: EGOgift_cultivation.json :: dataList[id=9827].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Enhancement], [BloodDinner_Common_Accumulation], [AttackUp], [BloodDinner_Accumulation]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Enhancement] = 공격 위력 증가 / Attack Power Up; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [AttackUp] = 공격 레벨 증가 / Offense Level Up; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Double the amount of Bloodfeast generated in the Stage\nSkills that inflict [Laceration] Potency, [Laceration] Count, or 'Unique Bleed': Heal 30% of the HP damage dealt at Attack End (max 20)\n* If a unit healed using the above effect, it gains 1 [Enhancement] at the next Turn Start (max 2)\n\nFor every 50 [BloodDinner_Common_Accumulation], all allies gain 1 [AttackUp] at the next Turn Start (max 5)\nEach La Manchaland unit also gains 1 [AttackUp] for every 30 [BloodDinner_Accumulation] consumed by each unit (max 3)
   PL: Ilość wytwarzanej Krwawej Uczty w walce jest dwukrotnie większa\nUmiejętności nakładające Siłę, Licznik [Laceration] lub Szczególne Krwawienie: na koniec ataku leczy HP równe 30% zadanych obrażeń HP (maks. 20)\n- Jednostka, która leczyła się tym efektem, na początku następnej tury zyskuje 1 [Enhancement] (maks. 2)\n\nZa każde 50 [BloodDinner_Common_Accumulation] wszyscy sojusznicy na początku następnej tury zyskują 1 [AttackUp] (maks. 5)\nJednostki La Manchaland dodatkowo zyskują 1 [AttackUp] za każde 30 własnego [BloodDinner_Accumulation] na początku następnej tury (maks. 3)
187. [Dar E.G.O [9827] — opis skrócony] 혈찬 생산량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9827].simpleDesc[abilityID=9827].simpleDesc
   limit: do 120 znaków
   EN: Generate more Bloodfeast
   PL: Generuje więcej Krwawej Uczty
188. [Dar E.G.O [9827] — opis skrócony] 체력 회복
   źródło: EGOgift_cultivation.json :: dataList[id=9827].simpleDesc[abilityID=98271].simpleDesc
   limit: do 120 znaków
   EN: Heal HP
   PL: Odzyskiwanie HP
189. [Dar E.G.O [9827] — opis skrócony] 공격 레벨 증가 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9827].simpleDesc[abilityID=98272].simpleDesc
   limit: do 120 znaków
   EN: Gain Offense Level Up
   PL: Zyskuje Wzrost Poziomu Ataku
190. [Dar E.G.O [9827] — opis skrócony] 공격 레벨 증가 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9827].simpleDesc[abilityID=98272#2].simpleDesc
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Dar E.G.O [9828] — nazwa] 카포를 위하여
   źródło: EGOgift_cultivation.json :: dataList[id=9828].name
   limit: do 40 znaków
   EN: For the Capo
   PL: Dla Kapo
192. [Dar E.G.O [9828] — opis] [편성 1번 인격 전용 효과]\n[Bullet]을 소모하는 스킬 사용 시 다음 효과 적용\n- 다음 턴에 [Agility] 3 얻음. (턴 당 1회)\n- 적중 시 [VibrationExplosion]. [Vibration] 횟수 1 소모 (턴 당 2회)\n- 합 승리 후 적중시 대상에게 [Combustion]과 [Vibration](특수 화상과 특수 진동을 포함)이 함께 존재할 경우, [Combustion]과 [Vibration]의 위력 합만큼 분노 피해를 입힘. (턴 당 2회)\n\n분노 공명을 4 이상 발동하였다면, 다음 효과 적용\n- 분노 속성 스킬을 사용할 경우, 스킬의 코인 위력 2 증가\n- 적중 시 [Bullet]을 소모하였다면, 피해량 +30%
   źródło: EGOgift_cultivation.json :: dataList[id=9828].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [Agility], [VibrationExplosion], [Vibration], [Combustion]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [Agility] = 신속 / Haste; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn
   EN: [Effects apply only to #1 Deployed Identity]\nWhen using a Skill that spends [Bullet], activate the following:\n- Gain 3 [Agility] next turn (once per turn)\n- On Hit: Trigger [VibrationExplosion] once (and consume 1 [Vibration] Count) (2 times per turn)\n- On Hit after Clash Win: If target has both [Combustion] and [Vibration](including both 'Unique Burn' and 'Unique Tremor'), inflict Wrath damage equal to ([Combustion] + [Vibration]). (2 times per turn)\n\nAt 4+ Wrath Reson., activate the following:\n- Wrath Skills gain Coin Power +2 upon use\n- On Hit, if [Bullet] was spent, deal +30% damage
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #1]\nPrzy użyciu Umiejętności zużywającej [Bullet] działają następujące efekty:\n- Następna tura zyskuje 3 [Agility] (1 raz na turę)\n- Przy trafieniu: wywołuje [VibrationExplosion] i zużywa 1 Licznika [Vibration] (2 razy na turę)\n- Przy trafieniu po wygranym Starciu: jeżeli cel ma jednocześnie [Combustion] i [Vibration] (łącznie ze Szczególnym Podpaleniem i Szczególnym Wstrząsem), zadaje obrażenia Gniewu równe sumie Sił [Combustion] i [Vibration]. (2 razy na turę)\n\nPrzy Rezonansie Gniewu 4+ działają następujące efekty:\n- Umiejętności Gniewu przy użyciu zyskują +2 Moc Monety\n- Przy trafieniu, jeżeli zużyto [Bullet], zadaje +30% obrażeń
193. [Dar E.G.O [9828] — opis skrócony] 신속 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9828].simpleDesc[abilityID=9828].simpleDesc
   limit: do 120 znaków
   EN: Gain Haste
   PL: Zyskuje Pośpiech
194. [Dar E.G.O [9828] — opis skrócony] 진동 폭발
   źródło: EGOgift_cultivation.json :: dataList[id=9828].simpleDesc[abilityID=98281].simpleDesc
   limit: do 120 znaków
   EN: Trigger Tremor Burst
   PL: Wybuch Wstrząsu
195. [Dar E.G.O [9828] — opis skrócony] 분노 피해
   źródło: EGOgift_cultivation.json :: dataList[id=9828].simpleDesc[abilityID=98282].simpleDesc
   limit: do 120 znaków
   EN: Deal Wrath damage
   PL: Obrażenia Gniewu
196. [Dar E.G.O [9828] — opis skrócony] 코인 위력 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9828].simpleDesc[abilityID=98283].simpleDesc
   limit: do 120 znaków
   EN: Gain Coin Power
   PL: Zyskuje Moc Monet
197. [Dar E.G.O [9828] — opis skrócony] 피해량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9828].simpleDesc[abilityID=98284].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
198. [Dar E.G.O [9829] — nazwa] 중지의 규율
   źródło: EGOgift_cultivation.json :: dataList[id=9829].name
   limit: do 40 znaków
   EN: Rules of the Middle
   PL: Zasady Środkowego
199. [Dar E.G.O [9829] — opis] 타격 유형 기본 스킬의 코인 위력 +1, 중지 소속 인격은 효과가 강화되어 코인 위력 +2\n아군 피격 시 다음 턴에 모든 아군이 [AttackUp] 2 얻음 (턴 당 최대 3회)\n\n아래 효과는 전투 내 중지 소속 인격이 3인 이상일 때 추가로 발동.\n전투 시작 시 질투 공명 수 만큼 [Enhancement] 1 얻음, [Protection] 1 얻음 (최대 3)\n중지 소속 인격이 질투 속성 기본 스킬을 사용할 때 [SuperCoin]으로 변경되며, 받는 피해량이 50% 감소,\n이번 턴과 다음 턴에 [HitDamageUp] 2 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9829].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [Enhancement], [Protection], [SuperCoin], [HitDamageUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Protection] = 보호 / Protection; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: Blunt Attack Type Base Skills: Coin Power +1; "The Middle" Identities gain Coin Power +2 instead\nWhen an ally is hit, all allies gain 2 [AttackUp] next turn (3 times per turn)\n\nThe following effects activate when there are 3 or more "The Middle" Identities in the Encounter.\nCombat Start: Gain 1 [Enhancement] and 1 [Protection] for every Envy Reson. (max 3)\nWhen "The Middle" Identity uses an Envy Base Skill, convert its Coins to [SuperCoin]s, they take -50% damage, and gain 2 [HitDamageUp] this turn and next turn
   PL: Podstawowe Umiejętności Obuchu: +1 do Mocy Monety; Tożsamości frakcji Środkowego zyskują zamiast tego +2 do Mocy Monety\nGdy sojusznik zostanie trafiony, wszyscy sojusznicy następną turę zyskują 2 [AttackUp] (maks. 3 razy na turę)\n\nPoniższe efekty działają dodatkowo, gdy w walce są co najmniej 3 Tożsamości frakcji Środkowego.\nPoczątek Walki: za każdą wartość Rezonansu Zawiści zyskuje 1 [Enhancement] i 1 [Protection] (maks. 3)\nGdy Tożsamość frakcji Środkowego użyje Podstawowej Umiejętności Zawiści, jej Monety zamieniają się w [SuperCoin], otrzymuje o 50% mniej obrażeń, a w tej i następnej turze zyskuje 2 [HitDamageUp]
200. [Dar E.G.O [9829] — opis skrócony] 코인 위력 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9829].simpleDesc[abilityID=9829].simpleDesc
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Dar E.G.O [9829] — opis skrócony] 코인 위력 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9829].simpleDesc[abilityID=98291].simpleDesc
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Dar E.G.O [9829] — opis skrócony] 공격 레벨 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9829].simpleDesc[abilityID=98292].simpleDesc
   limit: do 120 znaków
   EN: Gain Offense Level
   PL: Wzrost Poziomu Ataku
203. [Dar E.G.O [9829] — opis skrócony] 공격 위력 증가, 보호 얻음
   źródło: EGOgift_cultivation.json :: dataList[id=9829].simpleDesc[abilityID=98293].simpleDesc
   limit: do 120 znaków
   EN: Gain Attack Power Up & Protection
   PL: Zyskuje Wzrost Mocy Ataku i Ochronę
204. [Dar E.G.O [9829] — opis skrócony] 파괴 불가 코인으로 변경, 받는 피해량 감소, 타격 피해량 증가
   źródło: EGOgift_cultivation.json :: dataList[id=9829].simpleDesc[abilityID=98294].simpleDesc
   limit: do 120 znaków
   EN: Convert Coins to Unbreakable Coins, take less damage, and deal more Blunt damage
   PL: Zamienia Monety w Monety Niezniszczalne, otrzymuje mniej obrażeń i zadaje więcej obrażeń obuchowych
205. [Dar E.G.O [9830] — nazwa] 꼬미의 작은 선물
   źródło: EGOgift_cultivation.json :: dataList[id=9830].name
   limit: do 40 znaków
   EN: Kkomi's Mini-Gift
   PL: Mały Prezent od Kkomiego
206. [Dar E.G.O [9830] — opis] 스테이지 첫 턴 시작시 또는 대기 해제되는 모든 아군에게 [VerEmergencyCandy] 3 부여\n이전 턴에 [VerEmergencyCandy]이 소모되지 않았으면, 턴 시작 시 [VerHunger] 1 부여
   źródło: EGOgift_cultivation.json :: dataList[id=9830].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [VerEmergencyCandy], [VerHunger]
   znaczenie tagów: [VerEmergencyCandy] = 비상용 사탕 / Backup Candy; [VerHunger] = 배고픔 / Hunger
   EN: On the first Turn Start of an Encounter, and on all allies who Substitute in, apply 3 [VerEmergencyCandy]\nIf they did not consume [VerEmergencyCandy] in the previous turn, apply 1 [VerHunger] at Turn Start
   PL: Na pierwszym początku tury walki oraz sojusznikom wchodzącym z Rezerwy nakłada 3 [VerEmergencyCandy]\nJeżeli w poprzedniej turze nie zużyto [VerEmergencyCandy], na początku tury nakłada 1 [VerHunger]
207. [Dar E.G.O [9830] — opis skrócony] 비상용 사탕 부여
   źródło: EGOgift_cultivation.json :: dataList[id=9830].simpleDesc[abilityID=9830].simpleDesc
   limit: do 120 znaków
   EN: Apply Backup Candy
   PL: Nakłada Zapasowy Cukierek
208. [Dar E.G.O [9830] — opis skrócony] 배고픔 부여
   źródło: EGOgift_cultivation.json :: dataList[id=9830].simpleDesc[abilityID=98301].simpleDesc
   limit: do 120 znaków
   EN: Apply Hunger
   PL: Nakłada Głód

## Dar E.G.O: EGOgift_lcbcheckup-re
- plik gry: `EGOgift_lcbcheckup-re.json`

209. [Dar E.G.O [9243] — nazwa] 시험 추출 : 홍염살
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9243].name
   limit: do 40 znaków
   EN: Trial Extraction : A.B.S
   PL: Ekstrakcja : Gwiazda Żarzącego Kwiatu
210. [Dar E.G.O [9243] — opis] [Combustion] 위력, [Combustion] 횟수 또는 특수 화상을 부여하는 공격 스킬의 피해량 +10%\n- 자신의 [Combustion] 횟수를 증가하는 스킬이면, 추가로 합 위력 +1\n- 자신의 잃은 체력 2%당, 추가로 피해량 +1% (최대 15%)
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9243].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +10% damage with Attack Skills that inflict [Combustion] Potency, Count, or 'Unique Burn'\n- If the Skill applies [Combustion] Count on self, Clash Power +1\n- Deal +1% damage for every 2% missing HP on self (max 15%)
   PL: Umiejętności ataku nakładające Siłę, Licznik [Combustion] lub Szczególne Podpalenie zadają +10% obrażeń\n- Jeżeli Umiejętność zwiększa własny Licznik [Combustion], dodatkowo +1 do Mocy Starcia\n- Za każde 2% brakującego własnego HP dodatkowo +1% obrażeń (maks. 15%)
211. [Dar E.G.O [9243] — opis skrócony] 공격 스킬의 피해량 증가[TabExplain], 조건 만족 시 합 위력 증가[TabExplain]
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9243].simpleDesc[abilityID=9243].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Attack Skills deal more damage, gain Clash Power when conditions are met
   PL: Umiejętności ataku zadają więcej obrażeń [TabExplain], przy spełnionych warunkach +1 do Mocy Starcia [TabExplain]
212. [Dar E.G.O [9244] — nazwa] 시험 추출 : 초롱
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9244].name
   limit: do 40 znaków
   EN: Trial Extraction : Lantern
   PL: Ekstrakcja Próbna : Latarnia
213. [Dar E.G.O [9244] — opis] [Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬의 피해량 +10%\n- 자신의 잃은 체력이 20% 이상이면, 추가로 합 위력 +1\n- 자신의 모든 스킬 슬롯의 [Aggro]의 합 1당, 공격 스킬의 피해량 +1% (최대 15%)
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9244].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Aggro]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Aggro] = 도발치 / Aggro
   EN: Deal +10% damage with Attack Skills that inflict [Burst] Potency or Count\n- At 20%+ missing HP on self, Clash Power +1\n- Deal +1% damage with Attack Skills for every 1 (sum of [Aggro] on all Skill Slots on self) (max 15%)
   PL: Umiejętności ataku nakładające Siłę lub Licznik [Burst] zadają +10% obrażeń\n- Przy 20%+ brakującego własnego HP dodatkowo +1 do Mocy Starcia\n- Umiejętności ataku zadają +1% obrażeń za każde 1 (suma [Aggro] na wszystkich slotach Umiejętności) (maks. 15%)
214. [Dar E.G.O [9244] — opis skrócony] 공격 스킬의 피해량 증가[TabExplain], 조건 만족 시 합 위력 증가[TabExplain]
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9244].simpleDesc[abilityID=9244].simpleDesc
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Dar E.G.O [9245] — nazwa] 변형 추출 : AEDD
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9245].name
   limit: do 40 znaków
   EN: Modified Extraction : AEDD
   PL: Ekstrakcja Zmodyfikowana : AEDD
216. [Dar E.G.O [9245] — opis] 이번 턴에 [Charge] 횟수 또는 특수 충전을 초과해서 얻으면, 다음 턴에 초과한 수치 2당, [AttackUp] 1 얻음 (인격별 턴당 최대 2)\n- [Charge] 횟수 또는 특수 충전을 획득하거나 소모하는 기본 스킬을 보유한 인격이면, 인격별 턴당 최대 6까지 얻을 수 있음\n- 자신에게 [HighVoltageExoshell]가 있으면, 추가로 [Charge] 위력 1 얻음 (전투당 1회)
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9245].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [AttackUp], [HighVoltageExoshell]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [HighVoltageExoshell] = 고전압 외피 / High-voltage Exoskeleton
   EN: If this unit gained [Charge] Count or 'Unique Charge' over maximum limit this turn, gain 1 [AttackUp] next turn for every 2 surplus Stack (2 per turn per Identity)\n- Identities with Base Skills that gain or consume [Charge] Count or 'Unique Charge': max 6 per turn per Identity instead\n- If this unit has [HighVoltageExoshell], also gain 1 [Charge] Potency (once per Encounter)
   PL: Jeżeli w tej turze zyskano Liczniki [Charge] lub Szczególne Ładowanie ponad limit, następna tura zyskuje 1 [AttackUp] za każde 2 nadwyżki (maks. 2 na turę na Tożsamość)\n- Tożsamości z Podstawowymi Umiejętnościami zyskującymi lub zużywającymi Liczniki [Charge] albo Szczególne Ładowanie: zamiast tego maks. 6 na turę na Tożsamość\n- Jeżeli jednostka posiada [HighVoltageExoshell], dodatkowo zyskuje 1 Siły [Charge] (1 raz na walkę)
217. [Dar E.G.O [9245] — opis skrócony] 초과한 [Charge] 횟수에 비례하여 [AttackUp] 얻음, 조건 만족 시 [Charge] 위력 얻음
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9245].simpleDesc[abilityID=9245].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [AttackUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Gain [AttackUp] based on surplus [Charge] Count, gain [Charge] when conditions are met
   PL: Zyskuje [AttackUp] zależnie od nadwyżki Liczników [Charge], a przy spełnionych warunkach Siłę [Charge]
218. [Dar E.G.O [9246] — nazwa] 누군가 놓쳐버린 사원증
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9246].name
   limit: do 50 znaków
   EN: Someone's Dropped Employee Card
   PL: Karta Pracownicza Zgubiona przez Kogoś
219. [Dar E.G.O [9246] — opis] 림버스 컴퍼니 소속 인격이면, 아래 효과 적용\n- 턴 시작 시 [ParryingResultUp]를 (전투에 참여한 림버스 컴퍼니 소속 인격 수 / 3)만큼 얻음 (최대 2, 소수점 버림)\n\nLCE 소속 인격이면, 아래 효과 적용\n- (전투에 참여한 E.G.O 장비를 입은 인격 수 X 10)%만큼 가하는 <noparse>피해량 증가</noparse> (최대 30%)\n- 같은 소속 아군 사망 시 모든 종류의 E.G.O 자원을 1개씩 얻고, 이번 전투동안 턴 시작 시 [PlusCoinValueUp] 1, [MinusCoinValueUp] 1 얻음 (전투당 인격별 최대 2회)
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9246].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ParryingResultUp], [PlusCoinValueUp], [MinusCoinValueUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [MinusCoinValueUp] = 빼기 코인 강화 / Minus Coin Boost
   EN: Limbus Company Identities:\n- Turn Start: Gain (# of Limbus Company Identities participating in battle / 3) [ParryingResultUp] (max 2; rounded down)\n\nLCE Identities:\n- Deal +(# of Identities in battle wearing E.G.O Gears x 10)% damage (max 30%)\n- On same-faction Ally Death: Gain 1 E.G.O resource each for all Affinities; gain 1 [PlusCoinValueUp] and 1 [MinusCoinValueUp] at Turn Start for the rest of this Encounter (2 times per Encounter per Identity)
   PL: Tożsamości frakcji Limbus Company:\n- Na początku tury zyskuje (liczba Tożsamości frakcji Limbus Company w walce / 3) [ParryingResultUp] (maks. 2, zaokrąglenie w dół)\n\nTożsamości frakcji LCE:\n- Zadaje +(liczba Tożsamości w walce w Sprzęcie E.G.O x 10)% obrażeń (maks. 30%)\n- Po śmierci sojusznika z tej samej frakcji zyskuje po 1 Zasobie E.G.O każdego Grzechu, a na czas tej walki na początku tury zyskuje 1 [PlusCoinValueUp] i 1 [MinusCoinValueUp] (maks. 2 razy na walkę na Tożsamość)
220. [Dar E.G.O [9246] — opis skrócony] 전투에 참여한 림버스 컴퍼니 소속 인격 수에 비례하여 [ParryingResultUp] 얻음
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9246].simpleDesc[abilityID=9246].simpleDesc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain [ParryingResultUp] based on the number of Limbus Company Identities participating in battle
   PL: Zyskuje [ParryingResultUp] zależnie od liczby Tożsamości frakcji Limbus Company w walce
221. [Dar E.G.O [9246] — opis skrócony] 전투에 참여한 E.G.O 장비를 입은 인격 수에 비례하여 가하는 피해량 증가[TabExplain]
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9246].simpleDesc[abilityID=92461].simpleDesc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal more damage based on the number of Identities wearing E.G.O Gears participating in battle
   PL: Zadaje więcej obrażeń zależnie od liczby Tożsamości w walce w Sprzęcie E.G.O [TabExplain]
222. [Dar E.G.O [9246] — opis skrócony] 같은 소속 아군 사망 시 E.G.O 자원 얻고, 이번 전투동안 턴 시작 시 다음 턴에 [PlusCoinValueUp], [MinusCoinValueUp] 얻음
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9246].simpleDesc[abilityID=92462].simpleDesc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [PlusCoinValueUp], [MinusCoinValueUp]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [MinusCoinValueUp] = 빼기 코인 강화 / Minus Coin Boost
   EN: On same-faction Ally Death: Gain E.G.O resources; gain [PlusCoinValueUp] and [MinusCoinValueUp] at Turn Start for this Encounter, starting from the next turn
   PL: Po śmierci sojusznika z tej samej frakcji zyskuje Zasoby E.G.O; od następnej tury na początku tury zyskuje [PlusCoinValueUp] i [MinusCoinValueUp] na czas tej walki
223. [Dar E.G.O [9248] — nazwa] 생강꽃, 안경 그리고 전해진 편지
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9248].name
   limit: do 60 znaków
   EN: Spicebush, Glasses, and Mailed Letter
   PL: Kwiat Agnotisa, Okulary i Przekazany List
224. [Dar E.G.O [9248] — opis] [편성 1번, 2번, 3번 인격 전용 효과]\n\n[Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬을 사용하여 합 승리 시, 대상 적에게 [Burst] 위력 5, [Burst] 횟수 3 부여 (인격별 턴당 1회)\n\n자신보다 속도가 낮은 적과 합을 진행할 때, 최종 위력 +1, 피해량 +25%\n\n[AttackUp] 버프를 보유한 적과 합하여 승리 시, 다음 턴 동안 자신은 [AttackUp] 3을 얻고 합에서 패배한 적에게는 [AttackDown] 3 부여 (인격별 턴당 최대 3회)\n\n스킬 1, 스킬 2, 스킬 3을 사용할 때마다 아래 효과 발동 (스킬 종류당 1회)\n- 해당 스킬을 사용한 캐릭터는 이번 전투동안 턴 시작 시 [Agility] 1, [SkillPowerUp] 1 얻음 (최대 3회 누적)
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9248].desc
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [AttackUp], [AttackDown], [Agility], [SkillPowerUp]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [Agility] = 신속 / Haste; [SkillPowerUp] = 기본 위력 증가 / Base Power Up
   EN: [Effects apply only to #1, #2, #3 Deployed Identities]\n\nWhen winning a Clash with an Attack Skill that inflicts [Burst] Potency or Count, inflict 5 [Burst] Potency and +3 [Burst] Count against the target (once per turn per Identity)\n\nWhen Clashing against an enemy with a slower Speed, gain Final Power +1 and deal +25% damage\n\nWhen winning a Clash against an enemy with [AttackUp] buff, gain 3 [AttackUp] for the next turn, and inflict 3 [AttackDown] on the enemy that lost the Clash (3 times per turn per Identity)\n\nEvery time Skill 1, Skill 2, or Skill 3 is used, activate the following effect (once per Skill rank):\n- The unit that used said Skill gains 1 [Agility] and 1 [SkillPowerUp] at Turn Start for this Encounter (can stack up to 3 times)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #1, #2, #3]\n\nGdy wygra Starcie Umiejętnością ataku nakładającą Siłę lub Licznik [Burst], nakłada na cel 5 Siły [Burst] i +3 do Licznika [Burst] (1 raz na turę na Tożsamość)\n\nW Starciu z wrogiem o niższej Prędkości zyskuje +1 do Mocy Końcowej i zadaje +25% obrażeń\n\nGdy wygra Starcie z wrogiem posiadającym buff [AttackUp], następna tura zyskuje 3 [AttackUp], a wroga przegrywającego Starcie obdarza 3 [AttackDown] (maks. 3 razy na turę na Tożsamość)\n\nPrzy każdym użyciu Umiejętności 1, 2 lub 3 wywołuje następujący efekt (1 raz na rangę Umiejętności)\n- Jednostka, która użyła danej Umiejętności, na czas tej walki zyskuje na początku tury 1 [Agility] i 1 [SkillPowerUp] (kumuluje do 3 razy)
225. [Dar E.G.O [9248] — opis skrócony] 합 승리 시 대상 적에게 [Burst] 부여
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9248].simpleDesc[abilityID=9248].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: On Clash Win: Inflict [Burst] on target
   PL: Po wygranym Starciu nakłada [Burst] na cel
226. [Dar E.G.O [9248] — opis skrócony] 자신보다 속도가 낮은 적과 합을 진행할 때, 최종 위력 증가[TabExplain], 피해량 증가[TabExplain]
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9248].simpleDesc[abilityID=92481].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: When Clashing against an enemy with a slower Speed, gain Final Power and deal more damage
   PL: W Starciu z wrogiem o niższej Prędkości zyskuje Moc Końcową [TabExplain] i zadaje więcej obrażeń [TabExplain]
227. [Dar E.G.O [9248] — opis skrócony] 조건 만족 시 자신은 [AttackUp] 얻고 적에겐 [AttackDown] 부여
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9248].simpleDesc[abilityID=92482].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [AttackDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Gain [AttackUp] on self and inflict [AttackDown] on the enemy when conditions are met
   PL: Przy spełnionych warunkach zyskuje [AttackUp] na siebie i nakłada [AttackDown] na wroga
228. [Dar E.G.O [9248] — opis skrócony] 조건 만족 시 턴 시작 시 [Agility] , [SkillPowerUp] 얻음
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9248].simpleDesc[abilityID=92483].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [SkillPowerUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [SkillPowerUp] = 기본 위력 증가 / Base Power Up
   EN: Gain [Agility] and [SkillPowerUp] at Turn Start when conditions are met
   PL: Przy spełnionych warunkach na początku tury zyskuje [Agility] i [SkillPowerUp]
229. [Dar E.G.O [9249] — nazwa] 조그맣고 근사한 바이올린
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].name
   limit: do 40 znaków
   EN: A Small, Lovely Violin
   PL: Małe, Cudowne Skrzypce
230. [Dar E.G.O [9249] — opis] [편성 5번, 6번 인격 전용 효과]\n\n스킬로 입힌 피해량의 10%만큼 자신의 체력 회복 (스킬당 최대 회복량 20)\n\n합 승리 시 [AttackUp] 1, [TakeHpHealIncrease] 1 얻음 (인격별 턴당 2회)\n\n스킬 사용 시 [AttackUp] 1, [TakeHpHealIncrease] 1 얻음 (인격별 턴당 2회)\n\n타격 스킬의 피해량 +10%\n\n합에서 승리한 스킬로 가하는 피해량 +(합 횟수 x 6)% (최대 30%)
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [TakeHpHealIncrease]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: [Effects apply only to #5, #6 Deployed Identities]\n\nHeal 10% of the HP damage dealt with a Skill (max 20 per Skill)\n\nOn Clash Win: Gain 1 [AttackUp] and 1 [TakeHpHealIncrease] (2 times per turn per Identity)\n\nOn Skill Use: Gain 1 [AttackUp] and 1 [TakeHpHealIncrease] (2 times per turn per Identity)\n\nDeal +10% damage with Blunt Skills\n\nDeal +(# of Clashes x 6)% damage with the Skill that won the Clash (max 30%)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #5, #6]\n\nLeczy własne HP równe 10% obrażeń zadanych Umiejętnością (maks. 20 leczenia na Umiejętność)\n\nPo wygranym Starciu zyskuje 1 [AttackUp] i 1 [TakeHpHealIncrease] (2 razy na turę na Tożsamość)\n\nPrzy użyciu Umiejętności zyskuje 1 [AttackUp] i 1 [TakeHpHealIncrease] (2 razy na turę na Tożsamość)\n\nUmiejętności obuchowe zadają +10% obrażeń\n\nUmiejętność, która wygrała Starcie, zadaje +(liczba Starć x 6)% obrażeń (maks. 30%)
231. [Dar E.G.O [9249] — opis skrócony] 스킬로 입힌 피해량에 비례하여 자신의 체력 회복
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].simpleDesc[abilityID=9249].simpleDesc
   limit: do 120 znaków
   EN: Heal HP on self based on damage dealt with a Skill
   PL: Leczy własne HP zależnie od obrażeń zadanych Umiejętnością
232. [Dar E.G.O [9249] — opis skrócony] 합 승리 시 [AttackUp], [TakeHpHealIncrease] 얻음
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].simpleDesc[abilityID=92491].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [TakeHpHealIncrease]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: Gain [AttackUp] and [TakeHpHealIncrease] on Clash Win
   PL: Po wygranym Starciu zyskuje [AttackUp] i [TakeHpHealIncrease]
233. [Dar E.G.O [9249] — opis skrócony] 스킬 사용 시 [AttackUp], [TakeHpHealIncrease] 얻음
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].simpleDesc[abilityID=92492].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [TakeHpHealIncrease]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost
   EN: Gain [AttackUp] and [TakeHpHealIncrease] on Skill Use
   PL: Przy użyciu Umiejętności zyskuje [AttackUp] i [TakeHpHealIncrease]
234. [Dar E.G.O [9249] — opis skrócony] 타격 스킬의 피해량 증가[TabExplain]
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].simpleDesc[abilityID=92493].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal more damage with Blunt Skills
   PL: Umiejętności obuchowe zadają więcej obrażeń [TabExplain]
235. [Dar E.G.O [9249] — opis skrócony] 합에서 승리한 스킬로 가하는 피해량 증가[TabExplain]
   źródło: EGOgift_lcbcheckup-re.json :: dataList[id=9249].simpleDesc[abilityID=92494].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal more damage with Skills that won the Clash
   PL: Umiejętności, które wygrały Starcie, zadają więcej obrażeń [TabExplain]

## Dar E.G.O: EGOgift_night-clean-up-re
- plik gry: `EGOgift_night-clean-up-re.json`

236. [Dar E.G.O [9269] — nazwa] 등장 전용 붐박스
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9269].name
   limit: do 50 znaków
   EN: Boombox of Dramatic Entrances
   PL: Boomboks na Efektowne Wejścia
237. [Dar E.G.O [9269] — opis] 타격 속성 스킬로 공격 적중 시, 해당 아군이 입힌 피해량의 5%만큼 체력 회복\n\n반격 스킬 적중 시 정신력 5 회복 (인격별 턴당 2회)
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9269].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Hit using Blunt Skills: Heal 5% of damage dealt by the ally who used the Skill\n\nOn Hit using Counter Skills: Heal 5 SP (2 times per turn per Identity)
   PL: Przy trafieniu atakiem Umiejętnością obuchową leczy HP równe 5% obrażeń zadanych przez tego sojusznika\n\nPrzy trafieniu Umiejętnością Kontry odzyskuje 5 SP (2 razy na turę na Tożsamość)
238. [Dar E.G.O [9269] — opis skrócony] 입힌 피해량에 비례하여 체력 회복
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9269].simpleDesc[abilityID=9269].simpleDesc
   limit: do 120 znaków
   EN: Heal HP proportional to damage dealt
   PL: Leczy HP zależnie od zadanych obrażeń
239. [Dar E.G.O [9269] — opis skrócony] 정신력 회복
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9269].simpleDesc[abilityID=92691].simpleDesc
   limit: do 120 znaków
   EN: Heal SP
   PL: Odzyskiwanie Poczytalności
240. [Dar E.G.O [9270] — nazwa] 작. 형. 등장
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].name
   limit: do 40 znaków
   EN: ENTER: The B.B.
   PL: WEJŚCIE: B.B.
241. [Dar E.G.O [9270] — opis] 아군 피격 시 공격자의 [Laceration] 횟수가 4 증가하고 피격된 아군은 [AttackUp] 3 얻음 (스킬당 1회)\n\n중지 소속 인격이 사용하는 기본 스킬의 기본 위력 +1, 피해량 +(30/코인 수)%\n- 턴 시작 시 중지 소속 인격이 3인 이상이면, 대신 기본 위력 +1, 피해량 +(60/코인 수)%\n- 5인 이상이면, 대신 기본 위력 +2, 피해량 +(90/코인 수)%\n\n타격 속성 스킬로 공격 적중 시, 해당 아군이 입힌 피해량의 10%만큼 체력 회복\n\n반격 스킬 적중 시 정신력 5 회복 (인격별 턴당 2회)\n\n전투 시작 시 반격 스킬을 장착한 아군이 이번 턴에 반격 스킬을 사용하지 못했으면, 턴 종료 시 다음 턴에 [PlusCoinValueUp] 1, [MinusCoinValueDown] 1 얻음
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].desc
   limit: do 1050 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [AttackUp], [PlusCoinValueUp], [MinusCoinValueDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [MinusCoinValueDown] = 빼기 코인 약화 / Minus Coin Drop
   EN: When an ally is hit, apply 3 [AttackUp] on the ally and inflict +4 [Laceration] Count on the attacker (once per Skill)\n\nBase Skills used by The Middle-faction Identities gain Base Power +1 and deal +(30 / # of Coins)% damage\n- Turn Start: If there are 3+ The Middle-faction Identities on the field, gain Base Power +1 and deal +(60 / # of Coins)% damage instead\n- If there are 5+ The Middle-faction Identities on the field, gain Base Power +2 and deal +(90 / # of Coins)% damage instead\n\nOn Hit using Blunt Skills: Heal 10% of damage dealt by the ally who used the Skill\n\nOn Hit using Counter Skills: Heal 5 SP (2 times per turn per Identity)\n\nTurn End: If the ally who equipped a Counter Skill at Combat Start did not get to use a Counter Skill this turn, the said ally gains 1 [PlusCoinValueUp] and 1 [MinusCoinValueDown] next turn
   PL: Gdy sojusznik zostanie trafiony: +4 do Licznika [Laceration] atakującego, a trafiony sojusznik zyskuje 3 [AttackUp] (1 raz na Umiejętność)\n\nPodstawowe Umiejętności Tożsamości frakcji Środkowego zyskują +1 do Mocy Bazowej i zadają +(30 / liczba Monet)% obrażeń\n- Na początku tury, gdy na polu są co najmniej 3 Tożsamości frakcji Środkowego, zamiast tego +1 do Mocy Bazowej i +(60 / liczba Monet)% obrażeń\n- Gdy jest ich 5+, zamiast tego +2 do Mocy Bazowej i +(90 / liczba Monet)% obrażeń\n\nPrzy trafieniu atakiem Umiejętnością obuchową leczy HP równe 10% obrażeń zadanych przez tego sojusznika\n\nPrzy trafieniu Umiejętnością Kontry odzyskuje 5 SP (2 razy na turę na Tożsamość)\n\nNa koniec tury: jeżeli sojusznik, który na Początku Walki miał Umiejętność Kontry, nie użył jej w tej turze, następnej tury zyskuje 1 [PlusCoinValueUp] i 1 [MinusCoinValueDown]
242. [Dar E.G.O [9270] — opis skrócony] 공격자의 [Laceration] 횟수 증가, 피격된 아군의 [AttackUp] 얻음
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].simpleDesc[abilityID=9270].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Attacker gains [Laceration] Count, attacked ally gains [AttackUp]
   PL: +Licznika [Laceration] atakującego; trafiony sojusznik zyskuje [AttackUp]
243. [Dar E.G.O [9270] — opis skrócony] 기본 위력 증가[TabExplain], 피해량 증가[TabExplain]
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].simpleDesc[abilityID=92701].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Gain Base Power and deal more damage
   PL: Zyskuje Moc Bazową [TabExplain] i zadaje więcej obrażeń [TabExplain]
244. [Dar E.G.O [9270] — opis skrócony] 입힌 피해량에 비례하여 체력 회복
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].simpleDesc[abilityID=92702].simpleDesc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Dar E.G.O [9270] — opis skrócony] 정신력 회복
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].simpleDesc[abilityID=92703].simpleDesc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Dar E.G.O [9270] — opis skrócony] 다음 턴에 [PlusCoinValueUp], [MinusCoinValueDown] 얻음
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9270].simpleDesc[abilityID=92704].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PlusCoinValueUp], [MinusCoinValueDown]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [MinusCoinValueDown] = 빼기 코인 약화 / Minus Coin Drop
   EN: Gain [PlusCoinValueUp] and [MinusCoinValueDown] next turn
   PL: Następna tura zyskuje [PlusCoinValueUp] i [MinusCoinValueDown]
247. [Dar E.G.O [9271] — nazwa] 흑수환 - 묘
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9271].name
   limit: do 40 znaków
   EN: Heishou Bolus - Mao
   PL: Heishou - Mao
248. [Dar E.G.O [9271] — opis] 흑수 - 묘 소속 인격이 스테이지에 첫 등장 시 1턴동안 속도 최솟값이 10으로 유지됨 (속도 최솟값이 10 이상이면, 이 효과는 발동하지 않음)\n\n자신에게 [LegStrength]가 있으면, 기본 스킬의 합 위력 +1, 피해량 +10%
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9271].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [LegStrength]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: When a Heishou Pack - Mao Branch Identity enters the Encounter for the first time, cap its min Speed to 10 for a turn (at 10+ min Speed, this effect does not activate)\n\nIf an ally has [LegStrength], the ally's Base Skills gain Clash Power +1 and deal +10% damage
   PL: Gdy Tożsamość frakcji Heishou - Gałąź Mao po raz pierwszy pojawia się w walce, jej minimalna Prędkość jest utrzymywana na 10 przez 1 turę (przy minimalnej Prędkości 10+ ten efekt nie działa)\n\nJeżeli jednostka posiada [LegStrength], jej Podstawowe Umiejętności zyskują +1 do Mocy Starcia i zadają +10% obrażeń
249. [Dar E.G.O [9271] — opis skrócony] 속도 최솟값 유지
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9271].simpleDesc[abilityID=9271].simpleDesc
   limit: do 120 znaków
   EN: Cap minimum Speed value
   PL: Utrzymuje minimalną wartość Prędkości
250. [Dar E.G.O [9271] — opis skrócony] 합 위력 증가[TabExplain], 피해량 증가[TabExplain]
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9271].simpleDesc[abilityID=92711].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Gain Clash Power and deal more damage
   PL: Zyskuje Moc Starcia [TabExplain] i zadaje więcej obrażeń [TabExplain]
251. [Dar E.G.O [9272] — nazwa] 암약
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].name
   limit: do 40 znaków
   EN: Shadowlurking
   PL: Skradanie się w Cieniu
252. [Dar E.G.O [9272] — opis] 흑수 - 묘 소속 인격이 스테이지에 첫 등장 시 3턴동안 속도 최솟값이 10으로 유지됨 (속도 최솟값이 10 이상이면, 이 효과는 발동하지 않음)\n\n자신의 [LegStrength] 수치 1당, 기본 스킬의 합 위력 +1, 피해량 +10%\n\n[BurstAgility] 부여 시 [BurstAgility]이 없는 적 2명에게 추가 부여함 (턴당 1회, 집중 전투에서는 부위로 판정)\n\n자신의 속도가 대상보다 빠를 때, 스킬로 부여하는 [Burst] 혹은 [Burst] 횟수를 대상에게 (속도 차 / 3)만큼 추가 부여 (최대 3)\n\n턴 종료시 흑수 - 묘 소속이면, 다음 턴에 [Agility] 2 얻음\n자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, (속도 차 / 3)만큼 참격 피해량 +10% (최대 30%)\n자신의 속도가 대상보다 빠르면, (속도 차 / 3)당 받는 피해량 -10% (최대 30%)
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].desc
   limit: do 1110 znaków
   tokeny: zachowaj dokładnie: \n, [LegStrength], [BurstAgility], [Burst], [Agility]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】; [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste
   EN: When a Heishou Pack - Mao Branch Identity enters the Encounter for the first time, cap its min Speed to 10 for 3 turns (at 10+ min Speed, this effect does not activate)\n\nBase Skills gain Clash Power +1 and deal +10% damage for every [LegStrength] Stack\n\nWhen inflicting [BurstAgility], also inflict it on 2 enemies that do not have [BurstAgility] (once per turn; in Focused Encounters, Parts)\n\nIf an ally's Speed is faster than its target's, the ally's Skills inflict (Speed difference / 3) more [Burst] or [Burst] Count (max 3)\n\nTurn End: Heishou Pack - Mao Branch allies gain 2 [Agility] next turn\nIf an ally's Speed is faster than its target's, or when an ally uses an Unopposed Attack, the said ally deals +10% Slash damage for every (Speed difference / 3) (max 30%)\nIf an ally's Speed is faster than its target's, take -10% damage for every (Speed difference / 3) (max 30%)
   PL: Gdy Tożsamość frakcji Heishou - Gałąź Mao po raz pierwszy pojawia się w walce, jej minimalna Prędkość jest utrzymywana na 10 przez 3 tury (przy minimalnej Prędkości 10+ ten efekt nie działa)\n\nZa każdą wartość [LegStrength] Podstawowe Umiejętności zyskują +1 do Mocy Starcia i zadają +10% obrażeń\n\nNakładając [BurstAgility], nakłada go dodatkowo na 2 wrogów bez [BurstAgility] (1 raz na turę; w starciach skupionych liczone per Część)\n\nGdy Prędkość jednostki jest większa niż Prędkość celu, jej Umiejętności nakładają dodatkowo (różnica Prędkości / 3) Siły [Burst] lub Licznika [Burst] (maks. 3)\n\nNa koniec tury: sojusznicy frakcji Heishou - Gałąź Mao następną turę zyskują 2 [Agility]\nGdy Prędkość sojusznika jest większa niż Prędkość celu albo gdy używa Ataku Jednostronnego, zadaje +10% obrażeń Cięcia za każdą (różnica Prędkości / 3) (maks. 30%)\nGdy Prędkość sojusznika jest większa niż Prędkość celu, otrzymuje -10% obrażeń za każdą (różnica Prędkości / 3) (maks. 30%)
253. [Dar E.G.O [9272] — opis skrócony] 속도 최솟값 유지
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=9272].simpleDesc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Dar E.G.O [9272] — opis skrócony] 합 위력 증가[TabExplain], 피해량 증가[TabExplain]
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=92721].simpleDesc
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Dar E.G.O [9272] — opis skrócony] [BurstAgility] 추가 부여
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=92722].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstAgility]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: Inflict additional [BurstAgility]
   PL: Nakłada dodatkowo [BurstAgility]
256. [Dar E.G.O [9272] — opis skrócony] 스킬로 부여하는 [Burst] 혹은 [Burst] 횟수 추가 부여
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=92723].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Skills inflict +1 more [Burst] or [Burst] Count
   PL: Umiejętności nakładają dodatkowo [Burst] lub Licznik [Burst]
257. [Dar E.G.O [9272] — opis skrócony] 턴 종료시 다음 턴에 [Agility] 얻음
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=92724].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Turn End: Gain [Agility] next turn
   PL: Na koniec tury następna tura zyskuje [Agility]
258. [Dar E.G.O [9272] — opis skrócony] 참격 피해량 증가[TabExplain]
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=92725].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal more Slash damage
   PL: Zadaje więcej obrażeń Cięcia [TabExplain]
259. [Dar E.G.O [9272] — opis skrócony] 받는 피해량 감소[TabExplain]
   źródło: EGOgift_night-clean-up-re.json :: dataList[id=9272].simpleDesc[abilityID=92726].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Take less damage
   PL: Otrzymuje mniej obrażeń [TabExplain]

## Dar E.G.O: EGOgift_pilgrimage
- plik gry: `EGOgift_pilgrimage.json`

260. [Dar E.G.O [9831] — nazwa] 시테러 연구집
   źródło: EGOgift_pilgrimage.json :: dataList[id=9831].name
   limit: do 40 znaków
   EN: Sea Terror Notes
   PL: Notatki o Morskim Terrorze
261. [Dar E.G.O [9831] — opis] 적에게 입히는 피해량 +10%.\n- 이번 전투 동안 처치한 적 또는 파괴된 부위 하나당 피해량 추가로 +1% (최대 20%만큼 추가로 증가).\n- 같은 부위 중복 파괴하는 경우에도 적용.\n- 등장 적에 시테러가 포함되어 있으면, 위 효과가 조건 없이 최대로 발동됨.
   źródło: EGOgift_pilgrimage.json :: dataList[id=9831].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +10% damage against enemies\nDeal +1% additional damage for every enemy defeated or every Part broken during this Encounter (max +20% additional damage)\nCan activate the above effect by breaking the same Part repeatedly.\nIf there are Sea Terrors among enemies, the above effect activates at maximum potential regardless of the conditions.
   PL: Zadaje +10% obrażeń wrogom\n- +1% dodatkowych obrażeń za każdego pokonanego wroga lub każdą zniszczoną Część w tej walce (dodatkowo maks. +20%).\n- Działa także przy wielokrotnym niszczeniu tej samej Części.\n- Jeżeli wśród wrogów jest Morski Terror, powyższy efekt osiąga maksimum bez spełniania warunków.
262. [Dar E.G.O [9831] — opis skrócony] 입히는 피해량 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9831].simpleDesc[abilityID=9831].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
263. [Dar E.G.O [9832] — nazwa] 황금으로 만든 나침반
   źródło: EGOgift_pilgrimage.json :: dataList[id=9832].name
   limit: do 40 znaków
   EN: Goldforged Compass
   PL: Kompas Kuty ze Złota
264. [Dar E.G.O [9832] — opis] 더하기 코인 스킬 사용 시 정신력 5 회복, 빼기 코인 스킬 사용 시 정신력 5 감소 (이 효과로 정신력이 -40 미만이 되지 않음, 인격 별로 턴당 1회).\n\n턴 시작 시 정신력이 최대거나 -30 이하면, [ResultEnhancement] 증가 1, [Protection] 2 얻음.
   źródło: EGOgift_pilgrimage.json :: dataList[id=9832].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [ResultEnhancement], [Protection]
   znaczenie tagów: [ResultEnhancement] = 위력 증가 / Power Up; [Protection] = 보호 / Protection
   EN: When using a Plus Coin Skill, heal 5 SP; when using a Minus Coin Skill, lose 5 SP (Each unit's SP cannot drop below -40 from this effect; once per turn per Identity)\n\nTurn Start: at max SP, or at -30 or less SP, gain 1 [ResultEnhancement] and 2 [Protection].
   PL: Przy użyciu Umiejętności z Monetą Plus odzyskuje 5 SP, przy użyciu Umiejętności z Monetą Minus traci 5 SP (ten efekt nie obniży SP poniżej -40, 1 raz na turę na Tożsamość).\n\nNa początku tury: przy pełnym SP lub SP ≤ -30 zyskuje 1 [ResultEnhancement] i 2 [Protection].
265. [Dar E.G.O [9832] — opis skrócony] 스킬 사용 시, 코인에 따라 정신력 회복 또는 감소
   źródło: EGOgift_pilgrimage.json :: dataList[id=9832].simpleDesc[abilityID=9832].simpleDesc
   limit: do 120 znaków
   EN: When using a Skill, either heal or lose SP depending on its Coin type
   PL: Przy użyciu Umiejętności odzyskuje lub traci SP zależnie od jej Monet
266. [Dar E.G.O [9832] — opis skrócony] 정신력이 최대 또는 -30 이하면 위력 증가, 보호 얻음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9832].simpleDesc[abilityID=98321].simpleDesc
   limit: do 120 znaków
   EN: At max SP or at less than or equal to -30, gain Power Up and Protection
   PL: Przy pełnym SP lub SP ≤ -30 zyskuje Wzrost Mocy i Ochronę
267. [Dar E.G.O [9833] — nazwa] 은빛 열쇠 모음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9833].name
   limit: do 40 znaków
   EN: Silver Key Bundle
   PL: Komplet Srebrnych Kluczy
268. [Dar E.G.O [9833] — opis] 보스 전투일 경우, 턴 시작 시 제일 적게 보유한 E.G.O 자원 3종 +1.\n\n턴 종료 시 이번 턴에 E.G.O 스킬을 사용했다면, 현재 보유한 가장 적은 E.G.O 자원 +3 (턴당 1회).
   źródło: EGOgift_pilgrimage.json :: dataList[id=9833].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In boss fights, gain 1 E.G.O resource for the 3 least-owned Affinities at the start of the turn.\n\nTurn End: if E.G.O Skill was used this turn, gain 3 E.G.O resource for the least-owned Affinity. (once per turn)
   PL: W walce z bossem na początku tury: +1 do 3 najmniej posiadanych Zasobów E.G.O.\n\nNa koniec tury: jeżeli w tej turze użyto Umiejętności E.G.O, +3 do najmniej posiadanego Zasobu E.G.O (1 raz na turę).
269. [Dar E.G.O [9833] — opis skrócony] 제일 적은 E.G.O 자원 3종 +1
   źródło: EGOgift_pilgrimage.json :: dataList[id=9833].simpleDesc[abilityID=9833].simpleDesc
   limit: do 120 znaków
   EN: E.G.O Resource +1 for the 3 least-owned Affinities
   PL: +1 do 3 najmniej posiadanych Zasobów E.G.O
270. [Dar E.G.O [9833] — opis skrócony] 가장 적은 E.G.O 자원 +3
   źródło: EGOgift_pilgrimage.json :: dataList[id=9833].simpleDesc[abilityID=98331].simpleDesc
   limit: do 120 znaków
   EN: Gain 3 least-owned E.G.O resource
   PL: +3 do najmniej posiadanego Zasobu E.G.O
271. [Dar E.G.O [9834] — nazwa] 말린 시테러
   źródło: EGOgift_pilgrimage.json :: dataList[id=9834].name
   limit: do 40 znaków
   EN: Sea Terror Jerky
   PL: Suszone Mięso Morskiego Terroru
272. [Dar E.G.O [9834] — opis] 턴 시작 시, 모든 적(환상체일 경우, 부위)에게 [DefenseDown] 3 부여.\n- 등장 적에 시테러가 포함되어 있으면 효과가 강화되어, 대신 [DefenseDown] 7 부여.
   źródło: EGOgift_pilgrimage.json :: dataList[id=9834].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseDown]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: inflict 3 [DefenseDown] to all enemies (in Focused Encounters, all Parts)\n- If Sea Terrors are featured among enemies, inflict 7 [DefenseDown] instead.
   PL: Na początku tury: nakłada 3 [DefenseDown] na wszystkich wrogów (lub Partie Anomalii).\n- Jeżeli wśród wrogów jest Morski Terror, efekt jest wzmocniony: zamiast tego nakłada 7 [DefenseDown].
273. [Dar E.G.O [9834] — opis skrócony] 방어 레벨 감소 부여
   źródło: EGOgift_pilgrimage.json :: dataList[id=9834].simpleDesc[abilityID=9834].simpleDesc
   limit: do 120 znaków
   EN: Inflict Defense Level Down
   PL: Nakłada Spadek Poziomu Obrony
274. [Dar E.G.O [9835] — nazwa] 밝게 빛나는 등불
   źródło: EGOgift_pilgrimage.json :: dataList[id=9835].name
   limit: do 40 znaków
   EN: Brilliant Lamplight
   PL: Jaskrawo Świecąca Lampa
275. [Dar E.G.O [9835] — opis] [편성 순서가 제일 빠른 인격에게 효과 적용]\n\n매 턴마다 처음으로 사용한 공격 스킬의 최종 위력 +3.\n사용한 공격 스킬이 E.G.O 스킬이면 효과가 강화되어, 대신 최종 위력 +4, 피해량 +25%.\n\n전투 시작 시 자신에게 [NervousImpairment]이 있다면, 최대 4까지 소모하고 대신 (소모한 수치 x 2)만큼 [Combustion] 얻음.
   źródło: EGOgift_pilgrimage.json :: dataList[id=9835].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [NervousImpairment], [Combustion]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment; [Combustion] = 화상 / Burn
   EN: [Effects apply only to the Identity with the earliest Deployment order]\n\nEvery turn, the first Attack Skill to be used gains Final Power +3\nIf the Attack Skill was an E.G.O Skill, it gains Final Power +4 and deals +25% damage instead.\n\nCombat Start: if this unit has [NervousImpairment] Stacks, consume up to 4 Stacks of it but gain (Stacks consumed x 2) [Combustion].
   PL: [Efekt dla Tożsamości z najwcześniejszą kolejnością Przydziału]\n\nPierwsza użyta w turze Umiejętność ataku zyskuje +3 do Mocy Końcowej.\nJeżeli to Umiejętność E.G.O, efekt jest wzmocniony: zamiast tego +4 do Mocy Końcowej i +25% obrażeń.\n\nPoczątek Walki: jeżeli jednostka posiada [NervousImpairment], zużywa do 4 jego wartości i zamiast tego zyskuje (zużyta wartość x 2) [Combustion].
276. [Dar E.G.O [9835] — opis skrócony] 이번 턴에 처음 사용한 공격 스킬 최종 위력 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9835].simpleDesc[abilityID=9835].simpleDesc
   limit: do 120 znaków
   EN: First Attack Skill used this turn gains Final Power
   PL: Pierwsza użyta w tej turze Umiejętność ataku zyskuje Moc Końcową
277. [Dar E.G.O [9835] — opis skrócony] 이번 턴에 처음 사용한 공격 스킬 최종 위력, 피해량 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9835].simpleDesc[abilityID=98351].simpleDesc
   limit: do 120 znaków
   EN: First Attack Skill used this turn gains Final Power and deals more damage
   PL: Pierwsza użyta w tej turze Umiejętność ataku zyskuje Moc Końcową i zadaje więcej obrażeń
278. [Dar E.G.O [9835] — opis skrócony] 신경 손상이 있으면 소모하고 대신 수치에 비례하여 화상 얻음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9835].simpleDesc[abilityID=98352].simpleDesc
   limit: do 120 znaków
   EN: If this unit has Nervous Impairment, consume it to gain a proportional amount of Burn
   PL: Jeżeli jednostka ma Uszkodzenie Nerwów, zużywa je i zyskuje proporcjonalne Podpalenie
279. [Dar E.G.O [9836] — nazwa] 오래된 악보
   źródło: EGOgift_pilgrimage.json :: dataList[id=9836].name
   limit: do 40 znaków
   EN: Aged Sheet Music
   PL: Zestarzałe Nuty
280. [Dar E.G.O [9836] — opis] E.G.O 스킬을 포함한 공격 스킬로 단일 대상(환상체일 경우, 부위) 공격 적중 시 피해량 +10%.\n[Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 스킬이면 효과가 강화되어, 대신 피해량 +25%.\n\n[파도의 만가 이스마엘 E.G.O 전용 효과]\n이 E.G.O 스킬로 공격하는 대상이 1명일 경우, 마지막 코인의 위력 +4, 피해량 +20%.
   źródło: EGOgift_pilgrimage.json :: dataList[id=9836].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When using an Attack Skill(including E.G.O Skills) against a single target(for Abnormalities, a single Part), deal +10% damage\nIf the Skill inflicts [Sinking] Potency, [Sinking] Count, or 'Unique Sinking', deal +25% damage instead.\n\n[Tidal Elegy Ishmael E.G.O Exclusive Effect]\nIf this E.G.O Skill targets only a single enemy, the final Coin gains +4 Coin Power and deals +20% damage.
   PL: Przy trafieniu atakiem Umiejętnością ataku (łącznie z Umiejętnościami E.G.O) w pojedynczy cel (lub Partię Anomalii) zadaje +10% obrażeń.\nJeżeli Umiejętność nakłada Siłę, Licznik [Sinking] lub Szczególne Zatonięcie, efekt jest wzmocniony: zamiast tego +25% obrażeń.\n\n[Efekt wyłącznie dla E.G.O Ishmaela — Elegia Przypływu]\nJeżeli ta Umiejętność E.G.O celuje w 1 wroga, jej ostatnia Moneta zyskuje +4 Moc Monety i zadaje +20% obrażeń.
281. [Dar E.G.O [9836] — opis skrócony] 공격 가중치 1인 스킬의 공격 적중 시 피해량 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9836].simpleDesc[abilityID=9836].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage On Hit with a 1 Atk Weight Skill
   PL: Przy trafieniu atakiem Umiejętnością o Wadze Ataku 1 zadaje więcej obrażeń
282. [Dar E.G.O [9836] — opis skrócony] 공격 가중치 1인 침잠 부여 스킬의 공격 적중 시 피해량 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9836].simpleDesc[abilityID=98361].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage On Hit with a 1 Atk Weight Skill that inflicts Sinking
   PL: Przy trafieniu Umiejętnością o Wadze Ataku 1 nakładającą Zatonięcie zadaje więcej obrażeń
283. [Dar E.G.O [9836] — opis skrócony] 파도의 만가 이스마엘 E.G.O 효과 강화
   źródło: EGOgift_pilgrimage.json :: dataList[id=9836].simpleDesc[abilityID=98362].simpleDesc
   limit: do 120 znaków
   EN: Empower Tidal Elegy Ishmael E.G.O
   PL: Wzmacnia E.G.O Ishmaela — Elegia Przypływu
284. [Dar E.G.O [9837] — nazwa] 금속 구성체
   źródło: EGOgift_pilgrimage.json :: dataList[id=9837].name
   limit: do 40 znaków
   EN: Metal Construct
   PL: Metalowy Konstrukt
285. [Dar E.G.O [9837] — opis] 턴 시작 시, 모든 아군이 [TakeHpHealIncrease] 2 얻음.\n[Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬을 보유한 인격이면 효과가 강화되어, 대신 [TakeHpHealIncrease] 4 얻음.\n\n[명령 : 용해 파우스트  E.G.O 전용 효과]\n이 E.G.O 스킬의 효과, 패시브로 회복한 체력 회복 수치의 초과량이 보호막으로 전환됨
   źródło: EGOgift_pilgrimage.json :: dataList[id=9837].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [TakeHpHealIncrease], [Burst]
   znaczenie tagów: [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost; [Burst] = 파열 / Rupture
   EN: Turn Start: all allies gain 2 [TakeHpHealIncrease]\nFor Identities with Attack Skills that inflict [Burst] Potency or [Burst] Count: gain 4 [TakeHpHealIncrease] instead\n\n[Command : Meltdown Faust E.G.O Exclusive Effect]\nAny excess HP healing due to this E.G.O Skill or its Passive’s effects is converted to Shield
   PL: Na początku tury: wszyscy sojusznicy zyskują 2 [TakeHpHealIncrease].\nTożsamości z Umiejętnościami ataku nakładającymi Siłę lub Licznik [Burst] zyskują zamiast tego 4 [TakeHpHealIncrease].\n\n[Efekt wyłącznie dla E.G.O Faust — Rozkaz : Roztopienie]\nNadwyżka HP wyleczona efektem lub Pasywką tej Umiejętności E.G.O zamienia się w Tarczę
286. [Dar E.G.O [9837] — opis skrócony] 체력 회복 증가 얻음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9837].simpleDesc[abilityID=9837].simpleDesc
   limit: do 120 znaków
   EN: Gain HP Healing Boost
   PL: Zyskuje Wzrost Leczenia HP
287. [Dar E.G.O [9837] — opis skrócony] 체력 회복 증가 얻음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9837].simpleDesc[abilityID=98371].simpleDesc
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Dar E.G.O [9837] — opis skrócony] 명령 : 용해 파우스트 E.G.O 효과 강화
   źródło: EGOgift_pilgrimage.json :: dataList[id=9837].simpleDesc[abilityID=98372].simpleDesc
   limit: do 120 znaków
   EN: Empower Command : Meltdown Faust E.G.O
   PL: Wzmacnia E.G.O Faust — Rozkaz : Roztopienie
289. [Dar E.G.O [9838] — nazwa] 달을 담은 술잔
   źródło: EGOgift_pilgrimage.json :: dataList[id=9838].name
   limit: do 40 znaków
   EN: Moonmirror Wine Cup
   PL: Kielich z Uwięzionym Księżycem
290. [Dar E.G.O [9838] — opis] 턴 시작 시 모든 아군의 정신력 5 회복. 정신력이 최대일 경우, 대신 초과된 정신력 수치만큼 [Breath] 얻음 (최대 5).\n[Breath] 위력 또는 [Breath] 횟수를 부여하거나 획득하는 공격 스킬 사용 시, [Breath] 횟수 2 얻음 (인격 별로 턴당 1회).\n\n[영작오 홍루 E.G.O 전용 효과]\n- 각성 : 이 E.G.O 스킬을 사용할 때, 정신력을 소모하는 대신 그 수치만큼 회복\n- 침식 : 이 E.G.O 스킬을 사용할 때, 소모하는 정신력 수치 -50%
   źródło: EGOgift_pilgrimage.json :: dataList[id=9838].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Turn Start: all allies heal 5 SP. At max SP, gain [Breath] equal to excess SP healed (max 5)\nWhen using an Attack Skill that applies or gains [Breath] Potency or Count, gain +2 [Breath] Count (once per Identity per turn)\n\n[To Remain Oneself Hong Lu E.G.O Exclusive Effect]\n- Awakening: When using this E.G.O Skill, instead of consuming SP, heal the amount of SP that it would’ve consumed\n- Corrosion: When using this E.G.O Skill, -50% to SP consumed
   PL: Na początku tury: wszyscy sojusznicy odzyskują 5 SP. Przy pełnym SP zamiast tego zyskuje [Breath] równe nadwyżce SP (maks. 5).\nPrzy użyciu Umiejętności ataku nakładającej lub zyskującej Siłę, Licznik [Breath] zyskuje 2 Licznika [Breath] (1 raz na turę na Tożsamość).\n\n[Efekt wyłącznie dla E.G.O Hong Lu — Pozostać Sobą]\n- Przebudzenie: przy użyciu tej Umiejętności E.G.O zamiast zużywać SP odzyskuje SP równe kosztowi\n- Korozja: przy użyciu tej Umiejętności E.G.O zużywane SP -50%
291. [Dar E.G.O [9838] — opis skrócony] 정신력을 회복. 정신력이 최대면, 대신 호흡 얻음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9838].simpleDesc[abilityID=9838].simpleDesc
   limit: do 120 znaków
   EN: Heal SP. At max SP, gain Poise instead
   PL: Odzyskuje SP. Przy pełnym SP zamiast tego zyskuje Oddech
292. [Dar E.G.O [9838] — opis skrócony] 호흡 부여, 획득 스킬 사용 시, 호흡 횟수 얻음
   źródło: EGOgift_pilgrimage.json :: dataList[id=9838].simpleDesc[abilityID=98381].simpleDesc
   limit: do 120 znaków
   EN: When using a Skill that applies or gains Poise, gain Poise Count
   PL: Przy użyciu Umiejętności nakładającej lub zyskującej Oddech zyskuje Licznik Oddechu
293. [Dar E.G.O [9838] — opis skrócony] 영작오 홍루 E.G.O 효과 강화
   źródło: EGOgift_pilgrimage.json :: dataList[id=9838].simpleDesc[abilityID=98382].simpleDesc
   limit: do 120 znaków
   EN: Empower To Remain Oneself Hong Lu E.G.O
   PL: Wzmacnia E.G.O Hong Lu — Pozostać Sobą
294. [Dar E.G.O [9839] — nazwa] 고풍스러운 페이퍼 나이프
   źródło: EGOgift_pilgrimage.json :: dataList[id=9839].name
   limit: do 50 znaków
   EN: Classical-design Letter Opener
   PL: Starodawny Otwieracz do Listów
295. [Dar E.G.O [9839] — opis] 공격 가중치가 2 이상인 스킬의 피해량 +15%.\n[Vibration] 위력, [Vibration] 횟수 또는 특수 진동을 부여하는 스킬이면 효과가 강화되어, 대신 피해량 +(15 + 공격 가중치 x 5)% (최대 50%).\n\n[눈부시지 않은 영광 그레고르 E.G.O 전용 효과]\n- 각성 : E.G.O 스킬의 코인을 재사용할 때마다 피해량 +20% (최대 60%)\n- 침식 : 공격 시작 전, 소모한 [MlynarWaiting] 10당 [AttackDmgUp] 1 얻음 (최대 4)
   źródło: EGOgift_pilgrimage.json :: dataList[id=9839].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [MlynarWaiting], [AttackDmgUp]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [MlynarWaiting] = 칼집 속 사람 / Man in Scabbard; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Skills with 2+ Atk Weight deal +15% damage\nSkills that inflict [Vibration] Potency, [Vibration] Count, or ‘Unique Tremor’ deal +(15 + Atk Weight x 5)% damage instead (max 50%)\n\n[Unbrilliant Glory Gregor E.G.O Exclusive Effect]\nAwakening Skill : Deal +20% damage with every E.G.O Skill Coin Reuse (max 60%)\nCorrosion : Before attacking, gain [AttackDmgUp] for every 10 [MlynarWaiting] consumed (max 4)
   PL: Umiejętności o Wadze Ataku 2+ zadają +15% obrażeń.\nUmiejętności nakładające Siłę, Licznik [Vibration] lub Szczególny Wstrząs zadają zamiast tego +(15 + Waga Ataku x 5)% obrażeń (maks. 50%).\n\n[Efekt wyłącznie dla E.G.O Gregor — Nieoślepiająca Chwała]\n- Przebudzenie: za każde ponowne użycie Monety Umiejętności E.G.O zadaje +20% obrażeń (maks. 60%)\n- Korozja: przed atakiem zyskuje 1 [AttackDmgUp] za każde zużyte 10 [MlynarWaiting] (maks. 4)
296. [Dar E.G.O [9839] — opis skrócony] 공격 가중치 2 이상인 스킬 사용 시, 피해량 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9839].simpleDesc[abilityID=9839].simpleDesc
   limit: do 120 znaków
   EN: When using Skills with 2+ Atk Weight, deal more damage
   PL: Umiejętności o Wadze Ataku 2+ zadają więcej obrażeń
297. [Dar E.G.O [9839] — opis skrócony] 공격 가중치 2 이상인 진동 부여 스킬 사용 시, 피해량 증가
   źródło: EGOgift_pilgrimage.json :: dataList[id=9839].simpleDesc[abilityID=98391].simpleDesc
   limit: do 120 znaków
   EN: When using Tremor-inflicting Skills with 2+ Atk Weight, deal more damage
   PL: Umiejętności nakładające Wstrząs o Wadze Ataku 2+ zadają więcej obrażeń
298. [Dar E.G.O [9839] — opis skrócony] 눈부시지 않은 영광 그레고르 E.G.O 효과 강화
   źródło: EGOgift_pilgrimage.json :: dataList[id=9839].simpleDesc[abilityID=98392].simpleDesc
   limit: do 120 znaków
   EN: Empower Unbrilliant Glory Gregor E.G.O
   PL: Wzmacnia E.G.O Gregor — Nieoślepiająca Chwała

## Dar E.G.O: EGOgift_tktRe
- plik gry: `EGOgift_tktRe.json`

299. [Dar E.G.O [9812] — nazwa] 엇낀 시간
   źródło: EGOgift_tktRe.json :: dataList[id=9812].name
   limit: do 40 znaków
   EN: Interlinked Time
   PL: Przepleciony Czas
300. [Dar E.G.O [9812] — opis] 적에게 [Switch_Vibration] 혹은 [FusionVibration] 시킬 경우, 대상에게 [VibrationExplosion] (인격마다 턴 당 1회)
   źródło: EGOgift_tktRe.json :: dataList[id=9812].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Switch_Vibration], [FusionVibration], [VibrationExplosion]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When triggering [Switch_Vibration] or [FusionVibration], trigger [VibrationExplosion] on target (once per turn per Identity)
   PL: Wywołując [Switch_Vibration] lub [FusionVibration] na wrogu, wywołuje [VibrationExplosion] na celu (1 raz na turę na Tożsamość)
301. [Dar E.G.O [9812] — opis skrócony] 대상에게 진동 폭발
   źródło: EGOgift_tktRe.json :: dataList[id=9812].simpleDesc[abilityID=9812].simpleDesc
   limit: do 120 znaków
   EN: Trigger Tremor Burst on target
   PL: Wywołuje Wyładowanie Wstrząsu na celu
302. [Dar E.G.O [19812] — nazwa] 엇낀 시간+
   źródło: EGOgift_tktRe.json :: dataList[id=19812].name
   limit: do 40 znaków
   EN: Interlinked Time+
   PL: Przepleciony Czas+
303. [Dar E.G.O [19812] — opis] 적에게 [Switch_Vibration] 혹은 [FusionVibration] 시킬 경우, 대상에게 [VibrationExplosion] (인격마다 턴 당 <style="upgradeHighlight">2</style>회)
   źródło: EGOgift_tktRe.json :: dataList[id=19812].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, [Switch_Vibration], [FusionVibration], [VibrationExplosion]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When triggering [Switch_Vibration] or [FusionVibration], trigger [VibrationExplosion] on target (<style="upgradeHighlight">2 times</style> per turn per Identity)
   PL: Wywołując [Switch_Vibration] lub [FusionVibration] na wrogu, wywołuje [VibrationExplosion] na celu (<style="upgradeHighlight">2 razy</style> na turę na Tożsamość)
304. [Dar E.G.O [19812] — opis skrócony] 대상에게 진동 폭발
   źródło: EGOgift_tktRe.json :: dataList[id=19812].simpleDesc[abilityID=19812].simpleDesc
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Dar E.G.O [29812] — nazwa] 엇낀 시간++
   źródło: EGOgift_tktRe.json :: dataList[id=29812].name
   limit: do 40 znaków
   EN: Interlinked Time++
   PL: Przepleciony Czas++
306. [Dar E.G.O [29812] — opis] 적에게 [Switch_Vibration] 혹은 [FusionVibration] 시킬 경우, 대상에게 [VibrationExplosion] (인격마다 턴 당 <style="upgradeHighlight">3</style>회)
   źródło: EGOgift_tktRe.json :: dataList[id=29812].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, [Switch_Vibration], [FusionVibration], [VibrationExplosion]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When triggering [Switch_Vibration] or [FusionVibration], trigger [VibrationExplosion] on target (<style="upgradeHighlight">3</style> times per turn per Identity)
   PL: Wywołując [Switch_Vibration] lub [FusionVibration] na wrogu, wywołuje [VibrationExplosion] na celu (<style="upgradeHighlight">3 razy</style> na turę na Tożsamość)
307. [Dar E.G.O [29812] — opis skrócony] 대상에게 진동 폭발
   źródło: EGOgift_tktRe.json :: dataList[id=29812].simpleDesc[abilityID=29812].simpleDesc
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Dar E.G.O [9813] — nazwa] 긴급 부여형 수사관 배지
   źródło: EGOgift_tktRe.json :: dataList[id=9813].name
   limit: do 40 znaków
   EN: Emergency Investigator Badge
   PL: Awaryjna Odznaka Śledczego
309. [Dar E.G.O [9813] — opis] [편성 순서 3번 인격 전용 효과]\n\n체력이 0이 될 때, 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투마다 인격당 1회 발동, 소수점 올림)\nE.G.O 기프트의 효과 발동 시 다음 턴부터 스테이지동안 턴 시작 시 [Enhancement] 2, [Vulnerable] 1 얻음\nT사 직원이면, [TimeRentalTwoPersonality]를 얻을 때 1 추가로 얻음\nT사 직원이면, 대상에게 [TimeSuspend]가 있으면, 공격 스킬로 가하는 피해량 +10%
   źródło: EGOgift_tktRe.json :: dataList[id=9813].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Vulnerable], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [Effects apply only to #3 Deployed Identity]\n\nWhen this unit takes lethal damage, their HP does not drop below 1, instantly heals 80% of their max HP, and recovers from Stagger. (once per Encounter, rounded up)\nWhen the E.G.O Gift activates, starting next turn, gain 2 [Enhancement] and 1 [Vulnerable] at every Turn Start for this Encounter.\nIf the affected unit is a T Corp. employee, gain 1 additional [TimeRentalTwoPersonality] when gaining a Stack of it.\nIf the affected unit is a T Corp. employee, if the target has [TimeSuspend], deal +10% damage with Attack Skills.
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #3]\n\nGdy HP spadłoby do 0, nie spada poniżej 1 i natychmiast leczy 80% Maks. HP. Dochodzi do siebie z Oszołomienia (wywołuje 1 raz na walkę na Tożsamość, zaokrąglenie w górę)\nPo wywołaniu efektu tego Daru E.G.O od następnej tury do końca walki na początku tury zyskuje 2 [Enhancement] i 1 [Vulnerable]\nJeżeli dotknięta jednostka jest pracownikiem T Corp., przy zdobywaniu [TimeRentalTwoPersonality] zyskuje 1 dodatkowo\nJeżeli dotknięta jednostka jest pracownikiem T Corp. i cel posiada [TimeSuspend], Umiejętności ataku zadają +10% obrażeń
310. [Dar E.G.O [9813] — opis skrócony] 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복
   źródło: EGOgift_tktRe.json :: dataList[id=9813].simpleDesc[abilityID=9813].simpleDesc
   limit: do 120 znaków
   EN: HP does not drop below 1, and instantly heals 80% of max HP
   PL: HP nie spada poniżej 1, a jednostka natychmiast leczy 80% Maks. HP
311. [Dar E.G.O [9813] — opis skrócony] 시간 대여를 얻을 때 추가로 얻음
   źródło: EGOgift_tktRe.json :: dataList[id=9813].simpleDesc[abilityID=98131].simpleDesc
   limit: do 120 znaków
   EN: Gain additional Borrowed Time when gaining it
   PL: Przy zdobywaniu Pożyczonego Czasu zyskuje dodatkowy
312. [Dar E.G.O [9813] — opis skrócony] 시간 유예가 있으면, 피해량 증가
   źródło: EGOgift_tktRe.json :: dataList[id=9813].simpleDesc[abilityID=98132].simpleDesc
   limit: do 120 znaków
   EN: Deals more damage if this unit has Time Moratorium
   PL: Zadaje więcej obrażeń, jeżeli jednostka posiada Moratorium Czasowe
313. [Dar E.G.O [19813] — nazwa] 긴급 부여형 수사관 배지+
   źródło: EGOgift_tktRe.json :: dataList[id=19813].name
   limit: do 50 znaków
   EN: Emergency Investigator Badge+
   PL: Awaryjna Odznaka Śledczego+
314. [Dar E.G.O [19813] — opis] [편성 순서 <style="upgradeHighlight">2번</style>, 3번 인격 전용 효과]\n\n체력이 0이 될 때, 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투마다 인격당 1회 발동, 소수점 올림)\nE.G.O 기프트의 효과 발동 시 다음 턴부터 스테이지동안 턴 시작 시 [Enhancement] 2, [Vulnerable] 1 얻음\nT사 직원이면, [TimeRentalTwoPersonality]를 얻을 때 1 추가로 얻음\nT사 직원이면, 대상에게 [TimeSuspend]가 있으면, 공격 스킬로 가하는 피해량 +<style="upgradeHighlight">12.5</style>%
   źródło: EGOgift_tktRe.json :: dataList[id=19813].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [Enhancement], [Vulnerable], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [Effects apply only to <style="upgradeHighlight">#2 and</style> #3 Deployed Identities]\n\nWhen this unit takes lethal damage, their HP does not drop below 1, instantly heals 80% of their max HP, and recovers from Stagger. (once per Encounter, rounded up)\nWhen the E.G.O Gift activates, starting next turn, gain 2 [Enhancement] and 1 [Vulnerable] at every Turn Start for this Encounter.\nIf the affected unit is a T Corp. employee, gain 1 additional [TimeRentalTwoPersonality] when gaining a Stack of it.\nIf the affected unit is a T Corp. employee, if the target has [TimeSuspend], deal +<style="upgradeHighlight">12.5</style>% damage with Attack Skills.
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach <style="upgradeHighlight">#2</style>, #3]\n\nGdy HP spadłoby do 0, nie spada poniżej 1 i natychmiast leczy 80% Maks. HP. Dochodzi do siebie z Oszołomienia (wywołuje 1 raz na walkę na Tożsamość, zaokrąglenie w górę)\nPo wywołaniu efektu tego Daru E.G.O od następnej tury do końca walki na początku tury zyskuje 2 [Enhancement] i 1 [Vulnerable]\nJeżeli dotknięta jednostka jest pracownikiem T Corp., przy zdobywaniu [TimeRentalTwoPersonality] zyskuje 1 dodatkowo\nJeżeli dotknięta jednostka jest pracownikiem T Corp. i cel posiada [TimeSuspend], Umiejętności ataku zadają +<style="upgradeHighlight">12,5</style>% obrażeń
315. [Dar E.G.O [19813] — opis skrócony] 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복
   źródło: EGOgift_tktRe.json :: dataList[id=19813].simpleDesc[abilityID=19813].simpleDesc
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Dar E.G.O [19813] — opis skrócony] 시간 대여를 얻을 때 추가로 얻음
   źródło: EGOgift_tktRe.json :: dataList[id=19813].simpleDesc[abilityID=198131].simpleDesc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Dar E.G.O [19813] — opis skrócony] 시간 유예가 있으면, 피해량 증가
   źródło: EGOgift_tktRe.json :: dataList[id=19813].simpleDesc[abilityID=198132].simpleDesc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Dar E.G.O [29813] — nazwa] 긴급 부여형 수사관 배지++
   źródło: EGOgift_tktRe.json :: dataList[id=29813].name
   limit: do 50 znaków
   EN: Emergency Investigator Badge++
   PL: Awaryjna Odznaka Śledczego++
319. [Dar E.G.O [29813] — opis] [편성 순서 <style="upgradeHighlight">1번</style>, 2번, 3번 인격 전용 효과]\n\n체력이 0이 될 때, 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투마다 인격당 1회 발동, 소수점 올림)\nE.G.O 기프트의 효과 발동 시 다음 턴부터 스테이지동안 턴 시작 시 <style="upgradeHighlight">[Enhancement] 2 얻음</style>\nT사 직원이면, [TimeRentalTwoPersonality]를 얻을 때 <style="upgradeHighlight">2</style> 추가로 얻음\nT사 직원이면, 대상에게 [TimeSuspend]가 있으면, 공격 스킬로 가하는 피해량 +<style="upgradeHighlight">15</style>%
   źródło: EGOgift_tktRe.json :: dataList[id=29813].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [Enhancement], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [Effects apply only to <style="upgradeHighlight">#1,</style> #2, and #3 Deployed Identities]\n\nWhen this unit takes lethal damage, their HP does not drop below 1, instantly heals 80% of their max HP, and recovers from Stagger. (once per Encounter, rounded up)\nWhen the E.G.O Gift activates, starting next turn, <style="upgradeHighlight">gain 2 [Enhancement]</style> at every Turn Start for this Encounter.\nIf the affected unit is a T Corp. employee, gain <style="upgradeHighlight">2</style> additional [TimeRentalTwoPersonality] when gaining a Stack of it.\nIf the affected unit is a T Corp. employee, if the target has [TimeSuspend], deal +<style="upgradeHighlight">15</style>% damage with Attack Skills.
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach <style="upgradeHighlight">#1</style>, #2, #3]\n\nGdy HP spadłoby do 0, nie spada poniżej 1 i natychmiast leczy 80% Maks. HP. Dochodzi do siebie z Oszołomienia (wywołuje 1 raz na walkę na Tożsamość, zaokrąglenie w górę)\nPo wywołaniu efektu tego Daru E.G.O od następnej tury do końca walki na początku tury <style="upgradeHighlight">zyskuje 2 [Enhancement]</style>\nJeżeli dotknięta jednostka jest pracownikiem T Corp., przy zdobywaniu [TimeRentalTwoPersonality] zyskuje <style="upgradeHighlight">2</style> dodatkowo\nJeżeli dotknięta jednostka jest pracownikiem T Corp. i cel posiada [TimeSuspend], Umiejętności ataku zadają +<style="upgradeHighlight">15</style>% obrażeń
320. [Dar E.G.O [29813] — opis skrócony] 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복
   źródło: EGOgift_tktRe.json :: dataList[id=29813].simpleDesc[abilityID=29813].simpleDesc
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Dar E.G.O [29813] — opis skrócony] 시간 대여를 얻을 때 추가로 얻음
   źródło: EGOgift_tktRe.json :: dataList[id=29813].simpleDesc[abilityID=298131].simpleDesc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Dar E.G.O [29813] — opis skrócony] 시간 유예가 있으면, 피해량 증가
   źródło: EGOgift_tktRe.json :: dataList[id=29813].simpleDesc[abilityID=298132].simpleDesc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Dar E.G.O [9814] — nazwa] 강제 얽힘 시퀀스 장치
   źródło: EGOgift_tktRe.json :: dataList[id=9814].name
   limit: do 50 znaków
   EN: Entanglement Override Sequencer
   PL: Sekwencer Wymuszonego Splątania
324. [Dar E.G.O [9814] — opis] 턴 시작 시 [Vibration] 횟수가 가장 많은 인격 1명의 [Vibration]을 [VibrationDistribution]로 [FusionVibration]
   źródło: EGOgift_tktRe.json :: dataList[id=9814].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Vibration], [VibrationDistribution], [FusionVibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: At Turn Start, for 1 Identity with the most [Vibration] Count, trigger [FusionVibration] to convert their [Vibration] to [VibrationDistribution]
   PL: Na początku tury: u 1 Tożsamości z największym Licznikiem [Vibration] wywołuje [FusionVibration], zamieniając jej [Vibration] na [VibrationDistribution]
325. [Dar E.G.O [9814] — opis skrócony] 진동 - 분배로 진폭 얽힘
   źródło: EGOgift_tktRe.json :: dataList[id=9814].simpleDesc[abilityID=9814].simpleDesc
   limit: do 120 znaków
   EN: Trigger Amplitude Entanglement into Tremor - Distribution
   PL: Wywołuje Splątanie Amplitudy w Wstrząs - Dystrybucja
326. [Dar E.G.O [19814] — nazwa] 강제 얽힘 시퀀스 장치+
   źródło: EGOgift_tktRe.json :: dataList[id=19814].name
   limit: do 50 znaków
   EN: Entanglement Override Sequencer+
   PL: Sekwencer Wymuszonego Splątania+
327. [Dar E.G.O [19814] — opis] 턴 시작 시 [Vibration] 횟수가 가장 많은 인격 <style="upgradeHighlight">2</style>명의 [Vibration]을 [VibrationDistribution]로 [FusionVibration]
   źródło: EGOgift_tktRe.json :: dataList[id=19814].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, [Vibration], [VibrationDistribution], [FusionVibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: At Turn Start, for <style="upgradeHighlight">2 Identities</style> with the most [Vibration] Count, trigger [FusionVibration] to convert their [Vibration] to [VibrationDistribution]
   PL: Na początku tury: u <style="upgradeHighlight">2 Tożsamości</style> z największym Licznikiem [Vibration] wywołuje [FusionVibration], zamieniając ich [Vibration] na [VibrationDistribution]
328. [Dar E.G.O [19814] — opis skrócony] 진동 - 분배로 진폭 얽힘
   źródło: EGOgift_tktRe.json :: dataList[id=19814].simpleDesc[abilityID=19814].simpleDesc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Dar E.G.O [29814] — nazwa] 강제 얽힘 시퀀스 장치++
   źródło: EGOgift_tktRe.json :: dataList[id=29814].name
   limit: do 50 znaków
   EN: Entanglement Override Sequencer++
   PL: Sekwencer Wymuszonego Splątania++
330. [Dar E.G.O [29814] — opis] 턴 시작 시 [Vibration] 횟수가 가장 많은 인격 <style="upgradeHighlight">3</style>명의 [Vibration]을 [VibrationDistribution]로 [FusionVibration]
   źródło: EGOgift_tktRe.json :: dataList[id=29814].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, [Vibration], [VibrationDistribution], [FusionVibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationDistribution] = 진동 - 분배 / Tremor - Distribution; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: At Turn Start, for <style="upgradeHighlight">3 </style>Identities with the most [Vibration] Count, trigger [FusionVibration] to convert their [Vibration] to [VibrationDistribution]
   PL: Na początku tury: u <style="upgradeHighlight">3 </style>Tożsamości z największym Licznikiem [Vibration] wywołuje [FusionVibration], zamieniając ich [Vibration] na [VibrationDistribution]
331. [Dar E.G.O [29814] — opis skrócony] 진동 - 분배로 진폭 얽힘
   źródło: EGOgift_tktRe.json :: dataList[id=29814].simpleDesc[abilityID=29814].simpleDesc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Dar E.G.O [9816] — nazwa] 초정밀 시간 가속 장치
   źródło: EGOgift_tktRe.json :: dataList[id=9816].name
   limit: do 50 znaków
   EN: Microprecision Time Accelerator
   PL: Mikroprecyzyjny Akcelerator Czasu
333. [Dar E.G.O [9816] — opis] [편성 순서 1번 인격 전용 효과]\n\n기본 공격 스킬 중에 [Vibration] 위력, 횟수를 부여하거나, [VibrationExplosion] 효과를 보유한 스킬이 있는 인격에게 적용됨\n스테이지 시작시, [UltraPrecisionTimeAcceleration]을 5 얻음
   źródło: EGOgift_tktRe.json :: dataList[id=9816].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationExplosion], [UltraPrecisionTimeAcceleration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [UltraPrecisionTimeAcceleration] = 초정밀 시간 가속 / Microprecision Time Acceleration
   EN: Effects apply only to #1 Deployed Identity\n\nApplies to Identities with Skills that inflict [Vibration] Potency, Count, or trigger [VibrationExplosion].\nEncounter Start: gain 5 [UltraPrecisionTimeAcceleration]
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #1]\n\nDziała dla Tożsamości z Podstawowymi Umiejętnościami ataku nakładającymi Siłę lub Licznik [Vibration] albo posiadającymi efekt [VibrationExplosion]\nPoczątek walki: zyskuje 5 [UltraPrecisionTimeAcceleration]
334. [Dar E.G.O [9816] — opis skrócony] 초정밀 시간 가속을 5 얻음
   źródło: EGOgift_tktRe.json :: dataList[id=9816].simpleDesc[abilityID=9816].simpleDesc
   limit: do 120 znaków
   EN: Gain 5 Microprecision Time Acceleration
   PL: Zyskuje 5 Mikroprecyzyjnego Przyspieszenia Czasu

## Dar E.G.O: EGOgift_walpu10
- plik gry: `EGOgift_walpu10.json`

335. [Dar E.G.O [9292] — nazwa] 롤모델
   źródło: EGOgift_walpu10.json :: dataList[id=9292].name
   limit: do 40 znaków
   EN: Role Model
   PL: Model do Naśladowania
336. [Dar E.G.O [9292] — opis] 해결사 인격을 2인 이상 편성했을 시, 아군 해결사 중 편성 순서가 가장 느린 1명에게 다음 효과 발동 (대기 인원 미포함)\n- 스테이지 첫 등장 시 [Emulation] 얻음\n\n전장의 아군 해결사 인격 2명당, 턴 시작 시 아군 해결사의 정신력 2 회복\n\n해결사이면서 같은 소속인 인격이 3인 이상이면 다음 효과 적용\n- [Emulation]를 보유한 아군의 기본 공격 스킬의 피해량 +(전장의 해결사 아군 수 x 3)% (최대 15%)\n\n해결사이면서 소속이 서로 다른 인격이 3인 이상이면 다음 효과 적용\n- [Emulation]를 보유한 아군이 기본 공격 스킬 사용 시 [Enhancement] 1 얻음 (턴당 2회)\n- [Emulation]를 보유한 아군이 기본 공격 스킬 적중 시 [Vulnerable] 1 부여 (턴당 2회. 집중 전투면, 부위로 판정)
   źródło: EGOgift_walpu10.json :: dataList[id=9292].desc
   limit: do 1180 znaków
   tokeny: zachowaj dokładnie: \n, [Emulation], [Enhancement], [Vulnerable]
   znaczenie tagów: [Emulation] = 본받는 자세 / Learning by Example; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: If there are 2 or more "Fixer" Identities in the Team Loadout, activate the following effect for 1 "Fixer" ally with the lattermost Deployment Order (excluding Backup units):\n- Upon entering the Encounter for the first time, gain [Emulation]\n\nTurn Start: Allied "Fixer" Identities heal 2 SP for every 2 allied "Fixer" Identities on the field\n\nIf there are 3 or more "Fixer" Identities of the same faction on the field, activate the following effect:\n- Base Attack Skills of allies that have [Emulation] deal +(# of "Fixer" allies on the field x 3)% damage (max 15%)\n\nIf there are 3 or more "Fixer" Identities of different factions on the field, activate the following effect:\n- On Base Attack Skill Use by an ally that has [Emulation], the said ally gains 1 [Enhancement] (2 times per turn)\n- On Hit using a Base Attack Skill by an ally that has [Emulation], inflict 1 [Vulnerable] (2 times per turn; in Focused Encounters, the Part)
   PL: Jeżeli w składzie są co najmniej 2 Tożsamości „Fixerów”, wywołuje następujący efekt dla 1 sojusznika Fixera z najpóźniejszym Przydziałem (nie licząc Rezerwy):\n- Przy pierwszym pojawieniu się w walce zyskuje [Emulation]\n\nNa początku tury: sojusznicy Fixerzy odzyskują 2 SP za każdych 2 Tożsamości Fixerów na polu\n\nJeżeli na polu są co najmniej 3 Tożsamości Fixerów tej samej frakcji, działa następujący efekt:\n- Podstawowe Umiejętności ataku sojuszników z [Emulation] zadają +(liczba sojuszników Fixerów na polu x 3)% obrażeń (maks. 15%)\n\nJeżeli na polu są co najmniej 3 Tożsamości Fixerów różnych frakcji, działa następujący efekt:\n- Gdy sojusznik z [Emulation] użyje Podstawowej Umiejętności ataku, zyskuje 1 [Enhancement] (2 razy na turę)\n- Gdy sojusznik z [Emulation] trafi Podstawową Umiejętnością ataku, nakłada 1 [Vulnerable] (2 razy na turę; w starciach skupionych liczone per Część)
337. [Dar E.G.O [9293] — nazwa] 정성껏 나눈 약재
   źródło: EGOgift_walpu10.json :: dataList[id=9293].name
   limit: do 50 znaków
   EN: Carefully-selected Medicinal Herbs
   PL: Starannie Wybrane Zioła Lecznicze
338. [Dar E.G.O [9293] — opis] [ComboSkill] 효과를 보유한 스킬 또는 아군의 스킬, 패시브 효과로 추가 발동된 공격 스킬 피해량 +10%\n- 위 효과가 발동할 때마다 피해량 +2% 추가 (최대 10%)\n- [ComboSkill] 효과를 보유한 스킬 사용시 [AttackDmgUp] 1 얻음 (인격당 최대 2)\n- 해당 아군이 <noparse>새벽 사무소</noparse> 또는 <noparse>쐐기 사무소</noparse> 소속이면, [Enhancement] 1 얻음 (인격당 최대 2)
   źródło: EGOgift_walpu10.json :: dataList[id=9293].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ComboSkill], [AttackDmgUp], [Enhancement]
   znaczenie tagów: [ComboSkill] = 연 / Joint Combo; [AttackDmgUp] = 피해량 증가 / Damage Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Attack Skills additionally triggered by Skills that have the [ComboSkill] effect or triggered by allies' Skill / Passive effects deal +10% damage\n- Deal an additional +2% damage every time the above effect activates (max 10%)\n- For Skills that have the [ComboSkill] effect, gain 1 [AttackDmgUp] every time the said Skills are used (max 2 per Identity)\n- If the ally is a "<noparse>Dawn Office</noparse>" or "<noparse>Wedge Office</noparse>" Identity, the said ally gains 1 [Enhancement] (max 2 per Identity)
   PL: Umiejętności ataku dodatkowo wywołane przez Umiejętności z efektem [ComboSkill] lub przez efekty Umiejętności/Pasywek sojuszników zadają +10% obrażeń\n- Za każde wywołanie powyższego efektu +2% obrażeń dodatkowo (maks. 10%)\n- Przy użyciu Umiejętności z efektem [ComboSkill] zyskuje 1 [AttackDmgUp] (maks. 2 na Tożsamość)\n- Jeżeli sojusznik należy do frakcji <noparse>Biura Świtu</noparse> lub <noparse>Biura Klinów</noparse>, zyskuje 1 [Enhancement] (maks. 2 na Tożsamość)
339. [Dar E.G.O [9293] — opis skrócony] <noparse>피해량 증가</noparse>, [AttackDmgUp] 얻음. 조건 만족시 [Enhancement] 얻음
   źródło: EGOgift_walpu10.json :: dataList[id=9293].simpleDesc[abilityID=9293].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, [AttackDmgUp], [Enhancement]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: <noparse>Deal more damage</noparse>, gain [AttackDmgUp]. Gain [Enhancement] upon fulfilling conditions
   PL: <noparse>Zadaje więcej obrażeń</noparse>, zyskuje [AttackDmgUp]. Przy spełnionych warunkach zyskuje [Enhancement]
340. [Dar E.G.O [9294] — nazwa] 볼품없는 긍지
   źródło: EGOgift_walpu10.json :: dataList[id=9294].name
   limit: do 40 znaków
   EN: Hollow Pride
   PL: Pusta Duma
341. [Dar E.G.O [9294] — opis] 스테이지 시작 시 무작위 아군 1명에게 [CursedBlessing] 부여\n[CursedBlessing]을 보유한 인격이 생존한 상태로 전투를 6회 승리할 시 해당 E.G.O 기프트가 변경됨 (기사의 긍지)\n{0}
   źródło: EGOgift_walpu10.json :: dataList[id=9294].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: {0}, \n, [CursedBlessing]
   znaczenie tagów: [CursedBlessing] = 절망의 시험 / A Test of Despair
   EN: Encounter Start: Apply [CursedBlessing] to 1 random ally\nThis E.G.O Gift changes into "Pride of the Knight" after 6 Encounter wins in which the Identity that has [CursedBlessing] survives\n{0}
   PL: Początek walki: nakłada [CursedBlessing] na 1 losowego sojusznika\nJeżeli Tożsamość z [CursedBlessing] przeżyje 6 wygranych walk, ten Dar E.G.O się zmienia (Duma Rycerza)\n{0}
342. [Dar E.G.O [9294] — opis skrócony] [CursedBlessing] 부여
   źródło: EGOgift_walpu10.json :: dataList[id=9294].simpleDesc[abilityID=9294].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CursedBlessing]
   znaczenie tagów: [CursedBlessing] = 절망의 시험 / A Test of Despair
   EN: Apply [CursedBlessing]
   PL: Nakłada [CursedBlessing]
343. [Dar E.G.O [9295] — nazwa] 기사의 긍지
   źródło: EGOgift_walpu10.json :: dataList[id=9295].name
   limit: do 40 znaków
   EN: Pride of the Knight
   PL: Duma Rycerza
344. [Dar E.G.O [9295] — opis] [편성 순서 1번 전용 효과]\n모든 흐트러짐 구간 제거. 스테이지 시작 시 [BeyondDespair] 부여.
   źródło: EGOgift_walpu10.json :: dataList[id=9295].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [BeyondDespair]
   znaczenie tagów: [BeyondDespair] = 절망을 넘어선 자 / The One Beyond Despair
   EN: [Effects apply only to #1 Deployed Identity]\nRemove all Stagger thresholds\nEncounter Start: Apply [BeyondDespair]
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #1]\nUsuwa wszystkie Progi Oszołomienia. Początek walki: nakłada [BeyondDespair].
345. [Dar E.G.O [9295] — opis skrócony] [BeyondDespair] 부여
   źródło: EGOgift_walpu10.json :: dataList[id=9295].simpleDesc[abilityID=9295].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeyondDespair]
   znaczenie tagów: [BeyondDespair] = 절망을 넘어선 자 / The One Beyond Despair
   EN: Apply [BeyondDespair]
   PL: Nakłada [BeyondDespair]
346. [Dar E.G.O [9296] — nazwa] 비통이 맺힌 검
   źródło: EGOgift_walpu10.json :: dataList[id=9296].name
   limit: do 40 znaków
   EN: Sword Laced with Grief
   PL: Miecz Przesiąknięty Żałobą
347. [Dar E.G.O [9296] — opis] [Sinking] 위력 또는 횟수, 특수 [Sinking]을 부여하는 관통 속성 기본 스킬의 최종 위력 +1\n\n아군의 스킬 적중 시, 대상의 정신력이 -20 이하면, 대상의 [Sinking] 위력만큼 우울 피해 (스킬당 1회)\n- 관통 스킬이었으면, 대상의 ([Sinking] 횟수 / 2)만큼 추가 고정 피해 (스킬당 1회)\n\n[로보토미 E.G.O::<noparse>눈물로 벼려낸 검</noparse> 로쟈 전용 효과]\n공격 가중치가 1인 [BlackTearsAlly]을 소모하는 기본 스킬로 적에게 마지막 코인 적중 시 최종 피해량의 (소모한 [BlackTearsAlly])%만큼 모든 적에게 오만 피해\n\n[<noparse>눈물로 벼려낸 검</noparse> 홍루 E.G.O 스킬 전용 효과]\nE.G.O 스킬 최종 위력 +1
   źródło: EGOgift_walpu10.json :: dataList[id=9296].desc
   limit: do 940 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Sinking], [BlackTearsAlly]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [BlackTearsAlly] = 깊은 눈물 / Deep Tears
   EN: Pierce Base Skills that inflict [Sinking] Potency, Count, or Unique [Sinking] gain Final Power +1\n\nOn Hit by an ally using a Skill, if target has -20 or lower SP, deal Gloom damage equal to [Sinking] Potency to target (once per Skill)\n- If the said Skill was a Pierce Skill, deal additional fixed damage equal to ([Sinking] Count on target / 2) (once per Skill)\n\n[Lobotomy E.G.O::<noparse>The Sword Sharpened with Tears</noparse> Rodion Exclusive Effect]\nOn Hit against an enemy using the final Coin of a Base Skill that consumes [BlackTearsAlly] and has 1 Atk Weight, deal Pride damage to all enemies equal to ([BlackTearsAlly] Potency consumed)% of final damage\n\n[<noparse>The Sword Sharpened with Tears</noparse> Hong Lu E.G.O Skill Exclusive Effect]\nE.G.O Skill Final Power +1
   PL: Podstawowe Umiejętności Kłucia nakładające Siłę, Licznik lub Szczególne [Sinking] zyskują +1 do Mocy Końcowej\n\nGdy sojusznik trafi Umiejętnością, a cel ma SP ≤ -20, zadaje celowi obrażenia Posępności równe Sile [Sinking] celu (1 raz na Umiejętność)\n- Jeżeli to była Umiejętność Kłucia, zadaje dodatkowe stałe obrażenia równe (Licznik [Sinking] celu / 2) (1 raz na Umiejętność)\n\n[Lobotomy E.G.O::<noparse>The Sword Sharpened with Tears</noparse> — Efekt wyłącznie dla Rodion]\nGdy ostatnia Moneta Podstawowej Umiejętności zużywającej [BlackTearsAlly] i mającej Wagę Ataku 1 trafi wroga, zadaje wszystkim wrogom obrażenia Pychy równe (zużyte [BlackTearsAlly])% obrażeń końcowych\n\n[<noparse>The Sword Sharpened with Tears</noparse> — Efekt wyłącznie dla Umiejętności E.G.O Hong Lu]\nUmiejętność E.G.O zyskuje +1 do Mocy Końcowej
348. [Dar E.G.O [9296] — opis skrócony] 스킬 최종 위력이 증가, 우울 피해, 대상의 정신력이 낮으면 고정 피해
   źródło: EGOgift_walpu10.json :: dataList[id=9296].simpleDesc[abilityID=9296].simpleDesc
   limit: do 120 znaków
   EN: Skills gain Final Power, deal Gloom damage; if target has low SP, deal fixed damage
   PL: Umiejętności zyskują Moc Końcową, zadają obrażenia Posępności; przy niskim SP celu dodatkowe stałe obrażenia
349. [Dar E.G.O [9297] — nazwa] 하얀색 크라바트
   źródło: EGOgift_walpu10.json :: dataList[id=9297].name
   limit: do 40 znaków
   EN: White Cravat
   PL: Biały Krawat
350. [Dar E.G.O [9297] — opis] 턴 시작 시 <noparse>쐐기 사무소</noparse> 소속 인격이 3인 이상일 때 발동 (대기 인원 포함)\n\n[<noparse>쐐기 사무소</noparse> 대표 오티스 전용 효과]\n- 위 조건을 처음 만족한 턴 시작 시 [ComboWedge] 20 얻음\n- '쐐기 대형 전개', '...전원 격돌 준비.', '새벽 뒤 꿰뚫어 오는 쐐기' 사용 시 다음 턴에 [ComboWedgeDawn] 1 얻음 (턴당 2회)\n- '쐐기 대형 전개'를 사용했으면, 다음 턴 시작 시 해당 스킬로 소모한 [ComboWedge]의 절반을 돌려받음 (턴당 1회, 소수점 버림)
   źródło: EGOgift_walpu10.json :: dataList[id=9297].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ComboWedge], [ComboWedgeDawn]
   znaczenie tagów: [ComboWedge] = 승기 / Momentum; [ComboWedgeDawn] = 새벽의 유대 / Dawn's Camaraderie
   EN: Turn Start: Activates when there are 3 or more "<noparse>Wedge Office</noparse>" Identities (counts Backup Identities)\n\n[<noparse>Wedge Office</noparse> Rep Outis Exclusive Effect]\n- Turn Start: If the condition above was met for the first time, gain 20 [ComboWedge]\n- Upon using "Assume Wedge Formation", "... All units, engage for collision.", "The Wedge in the Wake of Dawnbreak", gain 1 [ComboWedgeDawn] next turn (2 times per turn)\n- If "Assume Wedge Formation" was used, regain half of the consumed [ComboWedge] at the next Turn Start (once per turn, rounded down)
   PL: Wywołuje na początku tury, gdy jest co najmniej 3 Tożsamości frakcji <noparse>Biura Klinów</noparse> (licząc Tożsamości w Rezerwie)\n\n[<noparse>Biuro Klinów</noparse> — Efekt wyłącznie dla Rep Outis]\n- Na początku tury, gdy warunek powyżej zostanie spełniony po raz pierwszy, zyskuje 20 [ComboWedge]\n- Przy użyciu „Przyjęcia Szyku Klina”, „...Wszystkie jednostki, gotowość do szarży.” lub „Klin Przebijający za Świtem” następna tura zyskuje 1 [ComboWedgeDawn] (2 razy na turę)\n- Jeżeli użyto „Przyjęcia Szyku Klina”, na początku następnej tury odzyskuje połowę [ComboWedge] zużytego przez tę Umiejętność (1 raz na turę, zaokrąglenie w dół)
351. [Dar E.G.O [9297] — opis skrócony] [ComboWedge] 또는 [ComboWedgeDawn] 얻음
   źródło: EGOgift_walpu10.json :: dataList[id=9297].simpleDesc[abilityID=9297].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ComboWedge], [ComboWedgeDawn]
   znaczenie tagów: [ComboWedge] = 승기 / Momentum; [ComboWedgeDawn] = 새벽의 유대 / Dawn's Camaraderie
   EN: Gain [ComboWedge] or [ComboWedgeDawn]
   PL: Zyskuje [ComboWedge] lub [ComboWedgeDawn]
352. [Dar E.G.O [9298] — nazwa] 검은색 트리코른
   źródło: EGOgift_walpu10.json :: dataList[id=9298].name
   limit: do 40 znaków
   EN: Black Tricorne
   PL: Czarny Tricorne
353. [Dar E.G.O [9298] — opis] 합 진행 시 매 합마다 적에게 [Vibration] 2 부여 (스킬당 3회)\n\n아군의 기본 공격 스킬이 적에게 크리티컬 적중 시, 메인 타겟에게 [Vibration]이 있으면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 1회)\n- 적이 [Switch_Vibration] 상태면, 크리티컬 피해량 +10%\n- 적이 [VibrationNesting] 상태이면, 중첩된 상태 1당, 크리티컬 피해량 +5% 추가 (최대 25%)
   źródło: EGOgift_walpu10.json :: dataList[id=9298].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationExplosion], [Switch_Vibration], [VibrationNesting]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationNesting] = 진동 - 중첩 / Tremor - Superposition
   EN: In a Clash, inflict 2 [Vibration] on the enemy for every Clash (3 times per Skill)\n\nOn Crit by an ally using a Basic Attack Skill against enemies, if the main target has [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (once per Skill)\n- If the enemy is in [Switch_Vibration] state, deal +10% damage on Critical Hit\n- If the enemy is in [VibrationNesting] state, deal an additional +5% damage on Critical Hit for each type of <noparse>superposed</noparse> Unique [Vibration] (max 25%)
   PL: W Starciu: nakłada 2 [Vibration] na wroga za każde Starcie (3 razy na Umiejętność)\n\nGdy Podstawowa Umiejętność ataku sojusznika trafi krytycznie wroga, a główny cel posiada [Vibration], wywołuje [VibrationExplosion] i zmniejsza Licznik [Vibration] celu o 1 (1 raz na Umiejętność)\n- Jeżeli wróg jest w stanie [Switch_Vibration], zadaje +10% obrażeń krytycznych\n- Jeżeli wróg jest w stanie [VibrationNesting], +5% obrażeń krytycznych dodatkowo za każdy <noparse>superponowany</noparse> stan [Vibration] (maks. 25%)
354. [Dar E.G.O [9298] — opis skrócony] 합 진행 시 진동 부여\n조건 만족시 진동 폭발, 스킬 크리티컬 피해량이 증가
   źródło: EGOgift_walpu10.json :: dataList[id=9298].simpleDesc[abilityID=9298].simpleDesc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a Clash, inflict Tremor\nTrigger Tremor Burst when conditions are met, Skills deal more damage on Critical Hit
   PL: W Starciu nakłada Wstrząs\nWywołuje Wyładowanie Wstrząsu przy spełnionych warunkach; Umiejętności zadają więcej obrażeń krytycznych
355. [Dar E.G.O [9299] — nazwa] 신체 적응용 장치
   źródło: EGOgift_walpu10.json :: dataList[id=9299].name
   limit: do 50 znaków
   EN: Backup Body Adaptation Device
   PL: Urządzenie Przystosowujące Ciało Zapasowe
356. [Dar E.G.O [9299] — opis] [VibrationCollapse]를 보유한 적에게 [VibrationExplosion] 시, 각 대상에게 가한 피해량의 (각 대상의 감소된 방어 레벨 수치)%만큼 나태 피해 (최대 15%)
   źródło: EGOgift_walpu10.json :: dataList[id=9299].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [VibrationCollapse], [VibrationExplosion]
   znaczenie tagów: [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When triggering [VibrationExplosion] on enemies that have [VibrationCollapse], deal Sloth damage to each target equal to (each target's Defense Level reduction)% of the damage dealt (max 15%)
   PL: Wywołując [VibrationExplosion] na wrogach posiadających [VibrationCollapse], zadaje każdemu celowi obrażenia Lenistwa równe (procent obniżenia Poziomu Obrony każdego celu)% zadanych mu obrażeń (maks. 15%)
357. [Dar E.G.O [9299] — opis skrócony] 나태 피해
   źródło: EGOgift_walpu10.json :: dataList[id=9299].simpleDesc[abilityID=9299].simpleDesc
   limit: do 120 znaków
   EN: Sloth damage
   PL: Obrażenia Lenistwa
358. [Dar E.G.O [9300] — nazwa] 부러진 창날
   źródło: EGOgift_walpu10.json :: dataList[id=9300].name
   limit: do 40 znaków
   EN: Broken Spearhead
   PL: Złamany Grot
359. [Dar E.G.O [9300] — opis] 관통 기본 공격 스킬로 크리티컬 피해를 입혔으면, 공격 종료 시 대상에게 [EmbeddedSpearhead] 부여 (인격당 턴당 1회. 집중 전투면, 부위로 판정)
   źródło: EGOgift_walpu10.json :: dataList[id=9300].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [EmbeddedSpearhead]
   znaczenie tagów: [EmbeddedSpearhead] = 박힌 창날 / Embedded Spearhead
   EN: On Crit using a Pierce Base Attack Skill, inflict [EmbeddedSpearhead] on target at Attack End (once per turn per Identity; in Focused Encounters, the Parts)
   PL: Przy trafieniu krytycznym Podstawową Umiejętnością ataku Kłucia nakłada na cel [EmbeddedSpearhead] na koniec ataku (1 raz na turę na Tożsamość; w starciach skupionych liczone per Część)
360. [Dar E.G.O [9300] — opis skrócony] [EmbeddedSpearhead] 부여
   źródło: EGOgift_walpu10.json :: dataList[id=9300].simpleDesc[abilityID=9300].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EmbeddedSpearhead]
   znaczenie tagów: [EmbeddedSpearhead] = 박힌 창날 / Embedded Spearhead
   EN: Inflict [EmbeddedSpearhead]
   PL: Nakłada [EmbeddedSpearhead]

## Dar E.G.O: EGOgift_walpu4
- plik gry: `EGOgift_walpu4.json`

361. [Dar E.G.O [9744] — nazwa] 치사랑
   źródło: EGOgift_walpu4.json :: dataList[id=9744].name
   limit: do 40 znaków
   EN: Filial Love
   PL: Synowska Miłość
362. [Dar E.G.O [9744] — opis] 기본 공격 스킬 효과로 [Laceration] 위력 또는 특수 출혈을 적에게 부여할 때마다 대상의 [Laceration] 횟수 2 증가 (모든 인격 합하여 턴 당 3회 발동)\n\n대상의 [Laceration] 횟수당 피해량 +1% (최대 20%)
   źródło: EGOgift_walpu4.json :: dataList[id=9744].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When inflicting [Laceration] Potency or 'Unique Bleed' with Base Attack Skill effects against enemies, inflict +2 [Laceration] Count (3 times per turn for the whole team)\n\nDeal +1% damage for every [Laceration] Count on the target (max 20%)
   PL: Za każde nałożenie Siły [Laceration] lub Szczególnego Krwawienia wrogu efektem Podstawowej Umiejętności ataku zwiększa Licznik [Laceration] celu o 2 (wywołuje 3 razy na turę w sumie dla wszystkich Tożsamości)\n\nZadaje +1% obrażeń za każdy Licznik [Laceration] celu (maks. 20%)
363. [Dar E.G.O [9744] — opis skrócony] 대상의 [Laceration] 횟수 증가, 자신의 피해량 증가
   źródło: EGOgift_walpu4.json :: dataList[id=9744].simpleDesc[abilityID=9744].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Inflict [Laceration] Count and deal more damage
   PL: Zwiększa Licznik [Laceration] celu i zadaje więcej obrażeń
364. [Dar E.G.O [9745] — nazwa] 어긋난 트랜지스터
   źródło: EGOgift_walpu4.json :: dataList[id=9745].name
   limit: do 40 znaków
   EN: Misaligned Transistor
   PL: Przesunięty Tranzystor
365. [Dar E.G.O [9745] — opis] 기본 공격 스킬에서 소모하는 [Charge] 횟수 또는 특수 충전의 절반만큼 추가 소모\n기본 공격 스킬에서 소모한 [Charge] 횟수 또는 특수 충전당 피해량 +2% (최대 20%)
   źródło: EGOgift_walpu4.json :: dataList[id=9745].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Base Attack Skills that consume [Charge] Count or 'Unique Charge' consume 1.5x more\nDeal +2% damage for every [Charge] Count or 'Unique Charge' consumed by Base Attack Skills (max 20%)
   PL: Podstawowe Umiejętności ataku zużywają dodatkowo połowę zużywanych Liczników [Charge] lub Szczególnego Ładowania\nZadaje +2% obrażeń za każdy Licznik [Charge] lub Szczególne Ładowanie zużyte przez Podstawowe Umiejętności ataku (maks. 20%)
366. [Dar E.G.O [9745] — opis skrócony] [Charge] 횟수 또는 특수 충전 추가 소모하여 피해량 증가
   źródło: EGOgift_walpu4.json :: dataList[id=9745].simpleDesc[abilityID=9745].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Consume additional [Charge] Count or 'Unique Charge' to deal more damage
   PL: Zużywa dodatkowe Liczniki [Charge] lub Szczególne Ładowanie, by zadawać więcej obrażeń
367. [Dar E.G.O [9746] — nazwa] 정신 오염 가속 가스
   źródło: EGOgift_walpu4.json :: dataList[id=9746].name
   limit: do 50 znaków
   EN: Mental Corruption Boosting Gas
   PL: Gaz Przyspieszający Zanieczyszczenie Umysłu
368. [Dar E.G.O [9746] — opis] [Sinking] 위력, [Sinking] 횟수 또는 특수 침잠를 부여하는 공격 스킬로 합을 진행한 후 공격 피해를 입힐 경우, 적중시 진행한 합 횟수만큼 [Sinking] 위력 부여 (최대 부여량 3, 턴 당 3회 발동)
   źródło: EGOgift_walpu4.json :: dataList[id=9746].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When engaging in a Clash using an Attack Skill that inflicts [Sinking] Potency, Count, or 'Unique Sinking' , then dealing damage with the said Attack Skill: On Hit, inflict [Sinking] Potency equal to the number of Clashes (max 3; 3 times per turn)
   PL: Gdy po Starciu Umiejętnością ataku nakładającą Siłę, Licznik [Sinking] lub Szczególne Zatonięcie zadaje nią obrażenia, przy trafieniu nakłada Siłę [Sinking] równą liczbie stoczonych Starć (maks. nakład 3, wywołuje 3 razy na turę)
369. [Dar E.G.O [9746] — opis skrócony] 합 횟수만큼 [Sinking] 위력 부여
   źródło: EGOgift_walpu4.json :: dataList[id=9746].simpleDesc[abilityID=9746].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict [Sinking] Potency equal to the number of Clashes
   PL: Nakłada Siłę [Sinking] równą liczbie Starć
370. [Dar E.G.O [9747] — nazwa] 흘러내린 엔케팔린
   źródło: EGOgift_walpu4.json :: dataList[id=9747].name
   limit: do 40 znaków
   EN: Leaked Enkephalin
   PL: Wyciekła Enkefalina
371. [Dar E.G.O [9747] — opis] 적의 [Sinking] 횟수 감소 또는 소모 시 (대상의 [Sinking] 위력)% 확률로 감소 또는 소모 직전 [Sinking] 횟수 1 증가 (턴 당 3회 발동, 최대 100%)\n- (최대 공명 수 x 2)%만큼 기본 확률 증가 (최대 12%)\n- 해당 최대 공명이 우울 또는 질투 공명이면 부여하는 [Sinking] 횟수 +1
   źródło: EGOgift_walpu4.json :: dataList[id=9747].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When the enemy is about to lose or consume [Sinking] Count: ([Sinking] Potency on the target)% chance to inflict +1 [Sinking] Count immediately before the target is about to lose or consume [Sinking] Count (3 times per turn; max 100%)\n- Raise base chance by (highest Reson. x2)% (max 12%)\n- If the said highest Reson. was a Gloom or an Envy Reson.: Inflict +1 more [Sinking] Count
   PL: Gdy wróg ma stracić lub zużyć Liczniki [Sinking]: z szansą (Siła [Sinking] celu)% nakłada +1 Licznika [Sinking] tuż przed utratą lub zużyciem (wywołuje 3 razy na turę, maks. 100%)\n- Podnosi bazową szansę o (najwyższy Rezonans x 2)% (maks. 12%)\n- Jeżeli ten najwyższy Rezonans to Rezonans Posępności lub Zawiści, nakłada +1 Licznika [Sinking]
372. [Dar E.G.O [9747] — opis skrócony] ([Sinking] 위력)% 확률로 감소 또는 소모 직전 [Sinking] 횟수 증가
   źródło: EGOgift_walpu4.json :: dataList[id=9747].simpleDesc[abilityID=9747].simpleDesc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: ([Sinking] Potency)% chance to inflict [Sinking] Count immediately before losing or consuming [Sinking] Count
   PL: Z szansą (Siła [Sinking])% nakłada Licznik [Sinking] tuż przed utratą lub zużyciem [Sinking]
373. [Dar E.G.O [9748] — nazwa] 고초
   źródło: EGOgift_walpu4.json :: dataList[id=9748].name
   limit: do 40 znaków
   EN: Hardship
   PL: Nędza
374. [Dar E.G.O [9748] — opis] 합 승리시, 진행한 합 횟수만큼 정신력 회복 (최대 3)\n정신력이 45이상에서 회복한다면, 합 횟수의 절반만큼 다음 턴에 [AttackUp] 얻음 (최대 3)
   źródło: EGOgift_walpu4.json :: dataList[id=9748].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Clash Win: Heal SP equal to the number of Clashes (max 3)\nIf the affected unit is already at 45+ SP, gain (# of Clashes/2) [AttackUp] next turn (max 3)
   PL: Po wygranym Starciu odzyskuje SP równe liczbie stoczonych Starć (maks. 3)\nJeżeli jednostka odzyskuje SP mając 45+, następna tura zyskuje (liczba Starć/2) [AttackUp] (maks. 3)
375. [Dar E.G.O [9748] — opis skrócony] 합 승리시, 진행한 합 횟수만큼 정신력 회복
   źródło: EGOgift_walpu4.json :: dataList[id=9748].simpleDesc[abilityID=9748].simpleDesc
   limit: do 120 znaków
   EN: On Clash Win, heal SP equal to number of Clashes
   PL: Po wygranym Starciu odzyskuje SP równe liczbie Starć
376. [Dar E.G.O [9749] — nazwa] 가시나무 관
   źródło: EGOgift_walpu4.json :: dataList[id=9749].name
   limit: do 40 znaków
   EN: Crown of Thorns
   PL: Korona z Cierni
377. [Dar E.G.O [9749] — opis] 턴 시작 시 정신력이 가장 낮은 아군 1명의 정신력 8 회복 (패닉 상태, E.G.O 침식 상태 제외)\n해당 캐릭터의 정신력이 최대였으면, 이번 턴동안 합 위력 +1\n이번 턴동안 해당 캐릭터의 [MentalSystemResultIncrease_Typo] +1, [MentalSystemResultDecrease_Typo] -1
   źródło: EGOgift_walpu4.json :: dataList[id=9749].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [MentalSystemResultIncrease_Typo], [MentalSystemResultDecrease_Typo]
   znaczenie tagów: [MentalSystemResultIncrease_Typo] = 정신력 회복 효율 / SP Heal Efficiency; [MentalSystemResultDecrease_Typo] = 정신력 감소 효율 / SP Loss Efficiency
   EN: Turn Start: 1 ally with the least SP heals 8 SP (unless they are in Panic or in E.G.O Corrosion)\nIf the said ally was already at max SP, Clash Power +1 for this turn\nFor this turn: [MentalSystemResultIncrease_Typo] +1, [MentalSystemResultDecrease_Typo] -1
   PL: Na początku tury: 1 sojusznik z najniższym SP odzyskuje 8 SP (z wyjątkiem Paniki i Korozji E.G.O)\nJeżeli jego SP było pełne, +1 do Mocy Starcia w tej turze\nW tej turze: [MentalSystemResultIncrease_Typo] +1, [MentalSystemResultDecrease_Typo] -1
378. [Dar E.G.O [9749] — opis skrócony] 턴 시작 시 정신력이 가장 낮은 아군 1명의 정신력 8 회복
   źródło: EGOgift_walpu4.json :: dataList[id=9749].simpleDesc[abilityID=9749].simpleDesc
   limit: do 120 znaków
   EN: Turn Start: heal 8 SP to 1 ally with the least SP
   PL: Na początku tury: 1 sojusznik z najniższym SP odzyskuje 8 SP
379. [Dar E.G.O [9750] — nazwa] 안식
   źródło: EGOgift_walpu4.json :: dataList[id=9750].name
   limit: do 40 znaków
   EN: Rest
   PL: Odpoczynek
380. [Dar E.G.O [9750] — opis] 기본 공격 스킬에서 자신의 정신력이 감소할 때, 소모량 1 감소\n대상에게 [Sinking]이 있을 경우, 이 공격 스킬에서 코인 앞면이 나온 수에 따라 피해량 +2%씩 증가 (최대 16%)
   źródło: EGOgift_walpu4.json :: dataList[id=9750].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Lose 1 less SP when an ally loses SP due to their own Base Attack Skill effect\nIf the target has [Sinking], deal +2% damage for every Heads Coin this Attack Skill flipped when attacking (max 16%)
   PL: Gdy Podstawowa Umiejętność ataku zmniejsza własne SP, zużywa o 1 mniej\nJeżeli cel posiada [Sinking], zadaje +2% obrażeń za każdą Monetę Awersową wyrzuconą przez tę Umiejętność ataku (maks. 16%)
381. [Dar E.G.O [9750] — opis skrócony] 기본 공격 스킬에서 자신의 정신력이 감소할 때, 소모량 1 감소
   źródło: EGOgift_walpu4.json :: dataList[id=9750].simpleDesc[abilityID=9750].simpleDesc
   limit: do 120 znaków
   EN: Lose 1 less SP when an ally loses SP due to their own Base Attack Skill effect
   PL: Gdy Podstawowa Umiejętność ataku zmniejsza własne SP, zużywa o 1 mniej
382. [Dar E.G.O [9750] — opis skrócony] 대상에게 침잠이 있으면 피해량이 증가
   źródło: EGOgift_walpu4.json :: dataList[id=9750].simpleDesc[abilityID=97501].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage if the target has Sinking
   PL: Zadaje więcej obrażeń, jeżeli cel posiada Zatonięcie

## Dar E.G.O: EGOgift_walpu6
- plik gry: `EGOgift_walpu6.json`

383. [Dar E.G.O [9805] — nazwa] 잿빛 별자리의 가호
   źródło: EGOgift_walpu6.json :: dataList[id=9805].name
   limit: do 50 znaków
   EN: Ashen Constellation's Blessing
   PL: Błogosławieństwo Popielatego Gwiazdozbioru
384. [Dar E.G.O [9805] — opis] [편성 1번 인격 전용 효과]\n\n스테이지 시작 시 [KnightBless] 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9805].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [KnightBless]
   znaczenie tagów: [KnightBless] = 가호 / Blessing
   EN: [Effects apply only to #1 Deployed Identity]\n\nGain [KnightBless] at Encounter Start
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #1]\n\nPoczątek walki: zyskuje [KnightBless]
385. [Dar E.G.O [9805] — opis skrócony] [KnightBless] 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9805].simpleDesc[abilityID=9744].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [KnightBless]
   znaczenie tagów: [KnightBless] = 가호 / Blessing
   EN: Gain [KnightBless]
   PL: Zyskuje [KnightBless]
386. [Dar E.G.O [9806] — nazwa] 선택 받지 못한 자
   źródło: EGOgift_walpu6.json :: dataList[id=9806].name
   limit: do 40 znaków
   EN: The Unchosen
   PL: Ten, Którego Nie Wybrano
387. [Dar E.G.O [9806] — opis] 아군이 피격당할 때마다, 공격자에게 [Sinking] 3 부여\n\n아군 사망 시, 모든 아군이 다음 턴에 [Enhancement] 2 얻음 (턴 당 1회)
   źródło: EGOgift_walpu6.json :: dataList[id=9806].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Whenever an ally takes a hit, inflict 3 [Sinking] on the attacker\n\nWhen an ally is killed, all allies gain 2 [Enhancement] next turn (once per turn)
   PL: Za każdym razem, gdy sojusznik zostanie trafiony, nakłada 3 [Sinking] na atakującego\n\nPo śmierci sojusznika wszyscy sojusznicy następną turę zyskują 2 [Enhancement] (1 raz na turę)
388. [Dar E.G.O [9806] — opis skrócony] [Sinking] 부여
   źródło: EGOgift_walpu6.json :: dataList[id=9806].simpleDesc[abilityID=9806].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict [Sinking]
   PL: Nakłada [Sinking]
389. [Dar E.G.O [9806] — opis skrócony] [Enhancement] 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9806].simpleDesc[abilityID=98061].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Gain [Enhancement]
   PL: Zyskuje [Enhancement]
390. [Dar E.G.O [9807] — nazwa] 눈물로 벼려낸 검
   źródło: EGOgift_walpu6.json :: dataList[id=9807].name
   limit: do 40 znaków
   EN: Sword Sharpened with Tears
   PL: Ostrze Wykute z Łez
391. [Dar E.G.O [9807] — opis] 아군의 스킬 적중 시, 대상의 정신력이 -20 이하면, 대상의 [Sinking] 위력만큼 우울 피해 (스킬 당 1회)\n\n- 관통 스킬이었으면, 대상의 ([Sinking] 횟수 / 2)만큼 추가 고정 피해
   źródło: EGOgift_walpu6.json :: dataList[id=9807].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When an ally hits with a Skill, if target has -20 or less SP, deal Gloom damage equal to [Sinking] on target (once per Skill)\n\n- If it was a Pierce Skill, deal ([Sinking] Count on target / 2) bonus fixed damage
   PL: Gdy sojusznik trafi Umiejętnością, a cel ma SP ≤ -20, zadaje celowi obrażenia Posępności równe Sile [Sinking] celu (1 raz na Umiejętność)\n\n- Jeżeli to była Umiejętność Kłucia, zadaje dodatkowe stałe obrażenia równe (Licznik [Sinking] celu / 2)
392. [Dar E.G.O [9807] — opis skrócony] 추가 피해
   źródło: EGOgift_walpu6.json :: dataList[id=9807].simpleDesc[abilityID=9807].simpleDesc
   limit: do 120 znaków
   EN: Bonus damage
   PL: Dodatkowe obrażenia
393. [Dar E.G.O [9808] — nazwa] 마법소녀의 애정 어린 선물
   źródło: EGOgift_walpu6.json :: dataList[id=9808].name
   limit: do 40 znaków
   EN: Magical Girl's Lovely Gift
   PL: Czuły Dar Magicznej Dziewczynki
394. [Dar E.G.O [9808] — opis] 아군의 [Charge] 횟수 또는 특수 충전을 얻거나 소모하는 스킬 적중시마다, 무작위 아군의 체력 또는 정신력이 무작위로 3 회복됨 (코인 당 1회. 체력 또는 정신력이 최대인 아군 제외)\n\n아군이 패닉 또는 E.G.O 침식 상태에서 회복할 때, 정신력 20 회복
   źródło: EGOgift_walpu6.json :: dataList[id=9808].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When an ally hits with a Skill that gains or consumes [Charge] Count or 'Unique Charge', a random ally's HP or SP heals by 3 (once per Coin; excludes allies with max HP or SP)\n\nWhen an ally recovers from Panic or 'E.G.O Corrosion', heal 20 SP
   PL: Za każdym razem, gdy sojusznik trafi Umiejętnością zyskującą lub zużywającą Liczniki [Charge] albo Szczególne Ładowanie, losowy sojusznik odzyskuje 3 HP lub SP (1 raz na Monetę; z wyjątkiem sojuszników z pełnym HP lub SP)\n\nGdy sojusznik dojdzie do siebie z Paniki lub Korozji E.G.O, odzyskuje 20 SP
395. [Dar E.G.O [9808] — opis skrócony] 체력, 정신력 무작위 회복
   źródło: EGOgift_walpu6.json :: dataList[id=9808].simpleDesc[abilityID=9808].simpleDesc
   limit: do 120 znaków
   EN: Randomly heal HP or SP
   PL: Losowo leczy HP lub SP
396. [Dar E.G.O [9808] — opis skrócony] 정신력 회복
   źródło: EGOgift_walpu6.json :: dataList[id=9808].simpleDesc[abilityID=98081].simpleDesc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Dar E.G.O [9809] — nazwa] 다한 쓸모, 맺힌 증오
   źródło: EGOgift_walpu6.json :: dataList[id=9809].name
   limit: do 40 znaków
   EN: Spent Use, Forming Hate
   PL: Zużyta Pożyteczność, Kapiąca Nienawiść
398. [Dar E.G.O [9809] — opis] 공격 스킬로 [Charge] 횟수를 소모하면, 다음 턴에 (소모한 [Charge] 횟수 / 2) 만큼 [AttackUp] 얻음 (턴 당 최대 10. 특수 충전을 포함)\n\n턴 종료 시 이번 턴에 아군의 정신력이 감소했다면, 해당 아군이 다음 턴에 [Enhancement] 1, [Vulnerable] 1 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9809].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [AttackUp], [Enhancement], [Vulnerable]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: When consuming [Charge] Count with Attack Skills, gain ([Charge] Count consumed / 2) [AttackUp] next turn (10 per turn; including 'Unique Charge')\n\nTurn End: if an ally lost SP this turn, the said ally gains 1 [Enhancement] and 1 [Vulnerable] next turn
   PL: Zużywając Liczniki [Charge] Umiejętnością ataku, następna tura zyskuje (zużyte Liczniki [Charge] / 2) [AttackUp] (maks. 10 na turę; łącznie ze Szczególnym Ładowaniem)\n\nNa koniec tury: jeżeli w tej turze sojusznik stracił SP, dotknięty sojusznik następnej tury zyskuje 1 [Enhancement] i 1 [Vulnerable]
399. [Dar E.G.O [9809] — opis skrócony] [AttackUp] 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9809].simpleDesc[abilityID=9809].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Gain [AttackUp]
   PL: Zyskuje [AttackUp]
400. [Dar E.G.O [9809] — opis skrócony] [AttackUp], [DefenseDown] 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9809].simpleDesc[abilityID=98091].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Gain [AttackUp] and [DefenseDown]
   PL: Zyskuje [AttackUp] i [DefenseDown]
401. [Dar E.G.O [9810] — nazwa] 트라우마 방지장
   źródło: EGOgift_walpu6.json :: dataList[id=9810].name
   limit: do 40 znaków
   EN: Trauma Shield
   PL: Osłona Przed Traumą
402. [Dar E.G.O [9810] — opis] 스테이지 시작 시, 모든 아군이 [TraumaShield] 2 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9810].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TraumaShield]
   znaczenie tagów: [TraumaShield] = 트라우마 방지장 / Trauma Shield
   EN: Encounter Start: all allies gain 2 [TraumaShield]
   PL: Początek walki: wszyscy sojusznicy zyskują 2 [TraumaShield]
403. [Dar E.G.O [9810] — opis skrócony] [TraumaShield] 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9810].simpleDesc[abilityID=9810].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TraumaShield]
   znaczenie tagów: [TraumaShield] = 트라우마 방지장 / Trauma Shield
   EN: Gain [TraumaShield]
   PL: Zyskuje [TraumaShield]
404. [Dar E.G.O [9811] — nazwa] 가치처분
   źródło: EGOgift_walpu6.json :: dataList[id=9811].name
   limit: do 40 znaków
   EN: Value Disposal
   PL: Zbycie Wartości
405. [Dar E.G.O [9811] — opis] 전투 중 아군 사망 시, 모든 E.G.O 자원을 2개씩 얻음\n\n전투 시작 시 이번 턴에 대기해제된 아군이 있으면, 정신력이 가장 낮은 아군 2명의 정신력 10 회복 (턴 당 1회. 패닉 / E.G.O 침식 상태 제외)
   źródło: EGOgift_walpu6.json :: dataList[id=9811].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When an ally dies in an Encounter, gain 2 E.G.O Resources for all Affinities\n\nCombat Start: if there are any allies who Substituted in this turn, heal 10 SP for 2 allies with the least SP (once per turn; unless they are in Panic or in 'E.G.O Corrosion')
   PL: Po śmierci sojusznika w walce zyskuje po 2 Zasobów E.G.O każdego Grzechu\n\nPoczątek Walki: jeżeli w tej turze któryś sojusznik wszedł z Rezerwy, leczy 10 SP 2 sojuszników z najniższym SP (1 raz na turę; z wyjątkiem Paniki i Korozji E.G.O)
406. [Dar E.G.O [9811] — opis skrócony] E.G.O 자원 얻음
   źródło: EGOgift_walpu6.json :: dataList[id=9811].simpleDesc[abilityID=9811].simpleDesc
   limit: do 120 znaków
   EN: Gain E.G.O Resources
   PL: Zyskuje Zasoby E.G.O
407. [Dar E.G.O [9811] — opis skrócony] 정신력 회복
   źródło: EGOgift_walpu6.json :: dataList[id=9811].simpleDesc[abilityID=98111].simpleDesc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Dar E.G.O: EGOgift_walpu8
- plik gry: `EGOgift_walpu8.json`

408. [Dar E.G.O [9233] — nazwa] 노이즈 섞인 무전기
   źródło: EGOgift_walpu8.json :: dataList[id=9233].name
   limit: do 40 znaków
   EN: Staticky Two-way Radio
   PL: Zaszumiona Krótkofalówka
409. [Dar E.G.O [9233] — opis] [Bullet]을 얻거나 소모하는 스킬 사용 시 다음 턴에 [Agility] 1, [AttackUp] 2 얻음 (인격별로 턴당 1회)\n- [Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 스킬이면, 가하는 피해량 +(20/코인 수)%
   źródło: EGOgift_walpu8.json :: dataList[id=9233].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [Agility], [AttackUp], [Sinking]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [Agility] = 신속 / Haste; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Sinking] = 침잠 / Sinking
   EN: On Use with a Skill that gains or spends [Bullet]: Gain 1 [Agility] and 2 [AttackUp] next turn (once per turn per Identity)\n- For Skills that inflict [Sinking] Potency, Count, or 'Unique Sinking', deal +(20 / # of Coins)% damage
   PL: Przy użyciu Umiejętności zyskującej lub zużywającej [Bullet] następna tura zyskuje 1 [Agility] i 2 [AttackUp] (1 raz na turę na Tożsamość)\n- Umiejętności nakładające Siłę, Licznik [Sinking] lub Szczególne Zatonięcie zadają +(20 / liczba Monet)% obrażeń
410. [Dar E.G.O [9233] — opis skrócony] 다음 턴에 [Agility], [AttackUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9233].simpleDesc[abilityID=9233].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [AttackUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Gain [Agility] and [AttackUp] next turn
   PL: Następna tura zyskuje [Agility] i [AttackUp]
411. [Dar E.G.O [9233] — opis skrócony] 가하는 피해량 증가[TabExplain]
   źródło: EGOgift_walpu8.json :: dataList[id=9233].simpleDesc[abilityID=92331].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal more damage
   PL: Zadaje więcej obrażeń [TabExplain]
412. [Dar E.G.O [9234] — nazwa] 부리 모양 목걸이
   źródło: EGOgift_walpu8.json :: dataList[id=9234].name
   limit: do 40 znaków
   EN: Beak-shaped Necklace
   PL: Naszyjnik w Kształcie Dzioba
413. [Dar E.G.O [9234] — opis] [Bullet]을 얻거나 소모하는 스킬 사용 시 다음 턴에 [Agility] 1, [Enhancement] 1 얻음 (인격별로 턴당 1회) \n- [Laceration] 위력, [Laceration] 횟수 또는 특수 출혈을 부여하는 스킬이면, 가하는 피해량 +(20/코인 수)%
   źródło: EGOgift_walpu8.json :: dataList[id=9234].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [Agility], [Enhancement], [Laceration]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [Agility] = 신속 / Haste; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Laceration] = 출혈 / Bleed
   EN: On Use with a Skill that gains or spends [Bullet]: Gain 1 [Agility] and 1 [Enhancement] next turn (once per turn per Identity)\n- For Skills that inflict [Laceration] Potency, Count, or 'Unique Bleed', deal +(20 / # of Coins)% damage
   PL: Przy użyciu Umiejętności zyskującej lub zużywającej [Bullet] następna tura zyskuje 1 [Agility] i 1 [Enhancement] (1 raz na turę na Tożsamość) \n- Umiejętności nakładające Siłę, Licznik [Laceration] lub Szczególne Krwawienie zadają +(20 / liczba Monet)% obrażeń
414. [Dar E.G.O [9234] — opis skrócony] 다음 턴에 [Agility], [Enhancement] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9234].simpleDesc[abilityID=9234].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [Enhancement]
   znaczenie tagów: [Agility] = 신속 / Haste; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Gain [Agility] and [Enhancement] next turn
   PL: Następna tura zyskuje [Agility] i [Enhancement]
415. [Dar E.G.O [9234] — opis skrócony] 가하는 피해량 증가[TabExplain]
   źródło: EGOgift_walpu8.json :: dataList[id=9234].simpleDesc[abilityID=92341].simpleDesc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Dar E.G.O [9235] — nazwa] 데스페라도
   źródło: EGOgift_walpu8.json :: dataList[id=9235].name
   limit: do 40 znaków
   EN: Desperado
   PL: Desperado
417. [Dar E.G.O [9235] — opis] [Bullet]을 얻거나 소모하는 인격이 편성된 수에 따라 기프트 효과 강화 (E.G.O 스킬 제외, 편성 인원 포함)\n\n- 2인 이상\n[Bullet]을 얻거나 소모하는 스킬 사용 시 다음 턴에 [Agility] 2, [AttackUp] 4 얻음 (인격별로 턴당 1회)\n\n- 5인 이상\n[Bullet]을 얻거나 소모하는 인격이 사용하는 스킬의 합 위력 +1, 피해량 +10%\n[Bullet]을 얻거나 소모하는 스킬의 피해량 +(100/코인 수)%\n[Bullet]을 전부 소모했으면, 다음 턴 시작 시 [Bullet] 4 얻음 (인격 별로 전투 당 1회)\n\n- 8인 이상\n턴 시작 시 [Bullet]을 얻거나 소모하는 인격에게 [DesperadoBuff] 1 부여\n• 이전 턴에 [Bullet]을 소모하지 않았으면, [DesperadoBuff] 1 추가 부여\n전투 종료 시 무작위 적 1명에게 (아군이 보유한 모든 [DesperadoBuff]의 합 x 3)만큼 관통 피해를 입힘 (최대 30)\n• 이후, 이 효과를 (편성된 수 - 1)만큼 반복함
   źródło: EGOgift_walpu8.json :: dataList[id=9235].desc
   limit: do 1260 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [Agility], [AttackUp], [DesperadoBuff]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [Agility] = 신속 / Haste; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DesperadoBuff] = 데스페라도 / Desperado
   EN: This E.G.O Gift's effects are enhanced based on the number of Identities in the Team loadout with Attack Skills that gain or spend [Bullet] (except E.G.O Skills; counts all units in the Team)\n\n- At 2+...\nOn Use with a Skill that gains or spends [Bullet]: Gain 2 [Agility] and 4 [AttackUp] next turn (once per Identity per turn)\n\n- At 5+...\nSkills used by Identities that gain or spend [Bullet]: Clash Power +1, deal +10% damage\nSkills that gain or spend [Bullet]: Deal +(100 / # of Coins)% damage\nIf an affected unit is out of [Bullet], gain 4 [Bullet] at the next Turn Start (once per Identity per Encounter)\n\n- At 8+...\nTurn Start: Apply 1 [DesperadoBuff] to Identities that gain or spend [Bullet]\n• If the affected unit did not spend [Bullet] last turn, apply 1 additional [DesperadoBuff]\nCombat End: deal (total sum of [DesperadoBuff] on all allies x 3) Pierce damage to 1 random enemy (max 30)\n• Then, repeat the above effect (number of Identities in the Team that gain or spend [Bullet] - 1) times
   PL: Efekty tego Daru E.G.O są wzmocnione zależnie od liczby Tożsamości w składzie z Umiejętnościami zyskującymi lub zużywającymi [Bullet] (z wyjątkiem Umiejętności E.G.O; liczy wszystkie jednostki składu)\n\n- Przy 2+\nPrzy użyciu Umiejętności zyskującej lub zużywającej [Bullet] następna tura zyskuje 2 [Agility] i 4 [AttackUp] (1 raz na Tożsamość na turę)\n\n- Przy 5+\nUmiejętności używane przez Tożsamości zyskujące lub zużywające [Bullet]: +1 do Mocy Starcia, +10% obrażeń\nUmiejętności zyskujące lub zużywające [Bullet] zadają +(100 / liczba Monet)% obrażeń\nJeżeli dotknięta jednostka zużyła całe [Bullet], na początku następnej tury zyskuje 4 [Bullet] (1 raz na Tożsamość na walkę)\n\n- Przy 8+\nNa początku tury: nakłada 1 [DesperadoBuff] na Tożsamości zyskujące lub zużywające [Bullet]\n• Jeżeli dotknięta jednostka nie zużyła [Bullet] w poprzedniej turze, nakłada dodatkowo 1 [DesperadoBuff]\nNa koniec walki: zadaje (suma wszystkich [DesperadoBuff] sojuszników x 3) obrażeń Kłucia 1 losowemu wrogowi (maks. 30)\n• Następnie powtarza powyższy efekt (liczba Tożsamości w składzie zyskujących lub zużywających [Bullet] - 1) razy
418. [Dar E.G.O [9235] — opis skrócony] 다음 턴에 [Agility], [AttackUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9235].simpleDesc[abilityID=9235].simpleDesc
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Dar E.G.O [9235] — opis skrócony] 합 위력 증가[TabExplain], 피해량 증가[TabExplain]
   źródło: EGOgift_walpu8.json :: dataList[id=9235].simpleDesc[abilityID=92351].simpleDesc
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Dar E.G.O [9235] — opis skrócony] 피해량 증가[TabExplain]
   źródło: EGOgift_walpu8.json :: dataList[id=9235].simpleDesc[abilityID=92352].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal more damage
   PL: Zadaje więcej obrażeń [TabExplain]
421. [Dar E.G.O [9235] — opis skrócony] [Bullet] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9235].simpleDesc[abilityID=92353].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Gain [Bullet]
   PL: Zyskuje [Bullet]
422. [Dar E.G.O [9235] — opis skrócony] [DesperadoBuff] 부여, 조건 만족 시 [DesperadoBuff] 추가 부여
   źródło: EGOgift_walpu8.json :: dataList[id=9235].simpleDesc[abilityID=92354].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DesperadoBuff]
   znaczenie tagów: [DesperadoBuff] = 데스페라도 / Desperado
   EN: Inflict [DesperadoBuff]. Inflict additional [DesperadoBuff] when conditions are met
   PL: Nakłada [DesperadoBuff]. Nakłada dodatkowy [DesperadoBuff] przy spełnionych warunkach
423. [Dar E.G.O [9235] — opis skrócony] 무작위 적 1명에게 관통 피해를 입힘
   źródło: EGOgift_walpu8.json :: dataList[id=9235].simpleDesc[abilityID=92355].simpleDesc
   limit: do 120 znaków
   EN: Deal Pierce damage to 1 random enemy
   PL: Zadaje obrażenia Kłucia 1 losowemu wrogowi
424. [Dar E.G.O [9236] — nazwa] 하모닉스
   źródło: EGOgift_walpu8.json :: dataList[id=9236].name
   limit: do 40 znaków
   EN: Harmonics
   PL: Harmoniki
425. [Dar E.G.O [9236] — opis] 이번 턴에 아군 또는 적 사망 시 모든 캐릭터가 다음 턴에 [Vulnerable] 1 얻음 (웨이브당 1회)\n- 효과를 발동한 다음 턴에 아군이 합 승리 시 모든 아군의 [Vulnerable] 1 감소하고 모든 적에게 [Laceration] 4 부여, [Laceration] 횟수 2 증가 (턴당 1회)
   źródło: EGOgift_walpu8.json :: dataList[id=9236].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [Laceration]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Laceration] = 출혈 / Bleed
   EN: When an ally or an enemy dies in a turn, all units gain 1 [Vulnerable] next turn (once per Wave)\n- On ally Clash Win in the same turn where all units gained [Vulnerable] due to the above effect, all allies lose 1 [Vulnerable] and inflict 4 [Laceration] and +2 [Laceration] Count against all enemies (once per turn)
   PL: Gdy w turze ginie sojusznik lub wróg, wszystkie jednostki następną turę zyskują 1 [Vulnerable] (1 raz na falę)\n- W tej samej turze, w której wszystkie jednostki zyskały [Vulnerable] tym efektem, przy wygranym Starciu sojusznika wszyscy sojusznicy tracą 1 [Vulnerable], a na wszystkich wrogów nakłada 4 [Laceration] i +2 do Licznika [Laceration] (1 raz na turę)
426. [Dar E.G.O [9236] — opis skrócony] 다음 턴에 [Vulnerable] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9236].simpleDesc[abilityID=9236].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Gain [Vulnerable] next turn
   PL: Następna tura zyskuje [Vulnerable]
427. [Dar E.G.O [9236] — opis skrócony] 모든 아군의 [Vulnerable]이 감소하고 모든 적에게 [Laceration] 부여, [Laceration] 횟수 증가
   źródło: EGOgift_walpu8.json :: dataList[id=9236].simpleDesc[abilityID=92361].simpleDesc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [Laceration]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Laceration] = 출혈 / Bleed
   EN: Reduce [Vulnerable] Stack on all allies and inflict [Laceration] and [Laceration] Count against all enemies
   PL: Zmniejsza [Vulnerable] wszystkich sojuszników i nakłada [Laceration] oraz Licznik [Laceration] na wszystkich wrogów
428. [Dar E.G.O [19236] — nazwa] 하모닉스+
   źródło: EGOgift_walpu8.json :: dataList[id=19236].name
   limit: do 40 znaków
   EN: Harmonics+
   PL: Harmoniki+
429. [Dar E.G.O [19236] — opis] 이번 턴에 아군 또는 적 사망 시 모든 캐릭터가 다음 턴에 [Vulnerable] <style="upgradeHighlight">2</style> 얻음 (웨이브당 1회)\n- 효과를 발동한 다음 턴에 아군이 합 승리 시 모든 아군의 [Vulnerable] 1 감소하고 모든 적에게 [Laceration] 4 부여, [Laceration] 횟수 2 증가 (턴당 <style="upgradeHighlight">2</style>회)
   źródło: EGOgift_walpu8.json :: dataList[id=19236].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [Vulnerable], [Laceration]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Laceration] = 출혈 / Bleed
   EN: When an ally or an enemy dies in a turn, all units gain <style="upgradeHighlight">2</style> [Vulnerable] next turn (once per Wave)\n- On ally Clash Win in the same turn where all units gained [Vulnerable] due to the above effect, all allies lose 1 [Vulnerable] and inflict 4 [Laceration] and +2 [Laceration] Count against all enemies (<style="upgradeHighlight">2</style> times per turn)
   PL: Gdy w turze ginie sojusznik lub wróg, wszystkie jednostki następną turę zyskują <style="upgradeHighlight">2</style> [Vulnerable] (1 raz na falę)\n- W tej samej turze, w której wszystkie jednostki zyskały [Vulnerable] tym efektem, przy wygranym Starciu sojusznika wszyscy sojusznicy tracą 1 [Vulnerable], a na wszystkich wrogów nakłada 4 [Laceration] i +2 do Licznika [Laceration] (<style="upgradeHighlight">2</style> razy na turę)
430. [Dar E.G.O [19236] — opis skrócony] 다음 턴에 [Vulnerable] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=19236].simpleDesc[abilityID=19236].simpleDesc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Dar E.G.O [19236] — opis skrócony] 모든 아군의 [Vulnerable]이 감소하고 모든 적에게 [Laceration] 부여, [Laceration] 횟수 증가
   źródło: EGOgift_walpu8.json :: dataList[id=19236].simpleDesc[abilityID=192361].simpleDesc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Dar E.G.O [29236] — nazwa] 하모닉스++
   źródło: EGOgift_walpu8.json :: dataList[id=29236].name
   limit: do 40 znaków
   EN: Harmonics++
   PL: Harmoniki++
433. [Dar E.G.O [29236] — opis] 이번 턴에 아군 또는 적 사망 시 모든 캐릭터가 다음 턴에 [Vulnerable] <style="upgradeHighlight">3</style> 얻음 (웨이브당 1회)\n- 효과를 발동한 다음 턴에 아군이 합 승리 시 모든 아군의 [Vulnerable] 1 감소하고 모든 적에게 [Laceration] 4 부여, [Laceration] 횟수 2 증가 (턴당 <style="upgradeHighlight">3</style>회)
   źródło: EGOgift_walpu8.json :: dataList[id=29236].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [Vulnerable], [Laceration]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Laceration] = 출혈 / Bleed
   EN: When an ally or an enemy dies in a turn, all units gain <style="upgradeHighlight">3</style> [Vulnerable] next turn (once per Wave)\n- On ally Clash Win in the same turn where all units gained [Vulnerable] due to the above effect, all allies lose 1 [Vulnerable] and inflict 4 [Laceration] and +2 [Laceration] Count against all enemies (<style="upgradeHighlight">3</style> times per turn)
   PL: Gdy w turze ginie sojusznik lub wróg, wszystkie jednostki następną turę zyskują <style="upgradeHighlight">3</style> [Vulnerable] (1 raz na falę)\n- W tej samej turze, w której wszystkie jednostki zyskały [Vulnerable] tym efektem, przy wygranym Starciu sojusznika wszyscy sojusznicy tracą 1 [Vulnerable], a na wszystkich wrogów nakłada 4 [Laceration] i +2 do Licznika [Laceration] (<style="upgradeHighlight">3</style> razy na turę)
434. [Dar E.G.O [29236] — opis skrócony] 다음 턴에 [Vulnerable] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=29236].simpleDesc[abilityID=29236].simpleDesc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Dar E.G.O [29236] — opis skrócony] 모든 아군의 [Vulnerable]이 감소하고 모든 적에게 [Laceration] 부여, [Laceration] 횟수 증가
   źródło: EGOgift_walpu8.json :: dataList[id=29236].simpleDesc[abilityID=292361].simpleDesc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Dar E.G.O [9237] — nazwa] 워킹 베이스
   źródło: EGOgift_walpu8.json :: dataList[id=9237].name
   limit: do 40 znaków
   EN: Walking Bass
   PL: Walking Bass
437. [Dar E.G.O [9237] — opis] [편성 3번 인격 전용 효과]\n\n턴 시작 시 [TensionUp] 1 얻음\n\n공격 적중 시, 25% 확률로 자신과 무작위 아군 1명에게 [TensionUp] 1 부여\n- [Laceration] 또는 [Combustion] 위력, 횟수 부여하는 스킬(특수 키워드 포함)이면, 부여 확률이 50%로 변경
   źródło: EGOgift_walpu8.json :: dataList[id=9237].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [TensionUp], [Laceration], [Combustion]
   znaczenie tagów: [TensionUp] = 텐션 업 / Hyped-up; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: [Effects apply only to #3 Deployed Identity]\n\nTurn Start: Gain 1 [TensionUp]\n\nOn Hit, 25% chance to apply 1 [TensionUp] on self and 1 random ally\n- If it was a Skill that inflicts [Laceration] or [Combustion](includes Potency, Count, and Unique variants), raise the chance to 50%
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #3]\n\nNa początku tury zyskuje 1 [TensionUp]\n\nPrzy trafieniu z szansą 25% nakłada 1 [TensionUp] na siebie i 1 losowego sojusznika\n- Jeżeli to Umiejętność nakładająca Siłę lub Licznik [Laceration] albo [Combustion] (łącznie z wariantami Szczególnymi), szansę podnosi do 50%
438. [Dar E.G.O [9237] — opis skrócony] [TensionUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9237].simpleDesc[abilityID=9237].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TensionUp]
   znaczenie tagów: [TensionUp] = 텐션 업 / Hyped-up
   EN: Gain [TensionUp]
   PL: Zyskuje [TensionUp]
439. [Dar E.G.O [9237] — opis skrócony] 자신과 무작위 아군 1명에게 [TensionUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9237].simpleDesc[abilityID=92371].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TensionUp]
   znaczenie tagów: [TensionUp] = 텐션 업 / Hyped-up
   EN: Apply [TensionUp] to self and 1 random ally
   PL: Nakłada [TensionUp] na siebie i 1 losowego sojusznika
440. [Dar E.G.O [19237] — nazwa] 워킹 베이스+
   źródło: EGOgift_walpu8.json :: dataList[id=19237].name
   limit: do 40 znaków
   EN: Walking Bass+
   PL: Walking Bass+
441. [Dar E.G.O [19237] — opis] [편성 3번, <style="upgradeHighlight">4번</style> 인격 전용 효과]\n\n턴 시작 시 [TensionUp] 1 얻음\n\n공격 적중 시, 25% 확률로 자신과 무작위 아군 1명에게 [TensionUp] 1 부여\n- [Laceration] 또는 [Combustion] 위력, 횟수 부여하는 스킬(특수 키워드 포함)이면, 부여 확률이 <style="upgradeHighlight">75</style>%로 변경
   źródło: EGOgift_walpu8.json :: dataList[id=19237].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [TensionUp], [Laceration], [Combustion]
   znaczenie tagów: [TensionUp] = 텐션 업 / Hyped-up; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: [Effects apply only to #3, #<style="upgradeHighlight">4</style> Deployed Identities]\n\nTurn Start: Gain 1 [TensionUp]\n\nOn Hit, 25% chance to apply 1 [TensionUp] on self and 1 random ally\n- If it was a Skill that inflicts [Laceration] or [Combustion](includes Potency, Count, and Unique variants), raise the chance to <style="upgradeHighlight">75</style>%
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #3, <style="upgradeHighlight">#4</style>]\n\nNa początku tury zyskuje 1 [TensionUp]\n\nPrzy trafieniu z szansą 25% nakłada 1 [TensionUp] na siebie i 1 losowego sojusznika\n- Jeżeli to Umiejętność nakładająca Siłę lub Licznik [Laceration] albo [Combustion] (łącznie z wariantami Szczególnymi), szansę podnosi do <style="upgradeHighlight">75</style>%
442. [Dar E.G.O [19237] — opis skrócony] [TensionUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=19237].simpleDesc[abilityID=19237].simpleDesc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Dar E.G.O [19237] — opis skrócony] 자신과 무작위 아군 1명에게 [TensionUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=19237].simpleDesc[abilityID=192371].simpleDesc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Dar E.G.O [29237] — nazwa] 워킹 베이스++
   źródło: EGOgift_walpu8.json :: dataList[id=29237].name
   limit: do 40 znaków
   EN: Walking Bass++
   PL: Walking Bass++
445. [Dar E.G.O [29237] — opis] [편성 3번, 4번 인격 전용 효과]\n\n턴 시작 시 [TensionUp] 1 얻음\n\n공격 적중 시, 25% 확률로 자신과 무작위 아군 <style="upgradeHighlight">2</style>명에게 [TensionUp] 1 부여\n- [Laceration] 또는 [Combustion] 위력, 횟수 부여하는 스킬(특수 키워드 포함)이면, 부여 확률이 <style="upgradeHighlight">100</style>%로 변경
   źródło: EGOgift_walpu8.json :: dataList[id=29237].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [TensionUp], [Laceration], [Combustion]
   znaczenie tagów: [TensionUp] = 텐션 업 / Hyped-up; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: [Effects apply only to #3, #4 Deployed Identities]\n\nTurn Start: Gain 1 [TensionUp]\n\nOn Hit, 25% chance to apply 1 [TensionUp] on self and <style="upgradeHighlight">2</style> random allies\n- If it was a Skill that inflicts [Laceration] or [Combustion](includes Potency, Count, and Unique variants), raise the chance to <style="upgradeHighlight">100</style>%
   PL: [Efekt wyłącznie dla Tożsamości na Przydziałach #3, #4]\n\nNa początku tury zyskuje 1 [TensionUp]\n\nPrzy trafieniu z szansą 25% nakłada 1 [TensionUp] na siebie i <style="upgradeHighlight">2</style> losowych sojuszników\n- Jeżeli to Umiejętność nakładająca Siłę lub Licznik [Laceration] albo [Combustion] (łącznie z wariantami Szczególnymi), szansę podnosi do <style="upgradeHighlight">100</style>%
446. [Dar E.G.O [29237] — opis skrócony] [TensionUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=29237].simpleDesc[abilityID=29237].simpleDesc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Dar E.G.O [29237] — opis skrócony] 자신과 무작위 아군 2명에게 [TensionUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=29237].simpleDesc[abilityID=292371].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TensionUp]
   znaczenie tagów: [TensionUp] = 텐션 업 / Hyped-up
   EN: Apply [TensionUp] to self and 2 random allies
   PL: Nakłada [TensionUp] na siebie i 2 losowych sojuszników
448. [Dar E.G.O [9238] — nazwa] 분홍 꽃잎
   źródło: EGOgift_walpu8.json :: dataList[id=9238].name
   limit: do 40 znaków
   EN: Pink Petals
   PL: Różowe Płatki
449. [Dar E.G.O [9238] — opis] 아군이 [Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 스킬로 적에게 공격 적중 시, [PinkPetals] 1 부여\n- 적의 [Sinking] 위력 5당, [PinkPetals] 1 추가 부여 (최대 4)
   źródło: EGOgift_walpu8.json :: dataList[id=9238].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [PinkPetals]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [PinkPetals] = 분홍 꽃잎 / Pink Petals
   EN: On Hit by an ally with a Skill that inflicts [Sinking] Potency, Count, or 'Unique Sinking', inflict 1 [PinkPetals]\n- Inflict 1 additional [PinkPetals] for every 5 [Sinking] on the enemy (max 4)
   PL: Gdy sojusznik trafi wroga Umiejętnością nakładającą Siłę, Licznik [Sinking] lub Szczególne Zatonięcie, nakłada 1 [PinkPetals]\n- +1 dodatkowego [PinkPetals] za każde 5 Siły [Sinking] wroga (maks. 4)
450. [Dar E.G.O [9238] — opis skrócony] [PinkPetals] 부여
   źródło: EGOgift_walpu8.json :: dataList[id=9238].simpleDesc[abilityID=9238].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PinkPetals]
   znaczenie tagów: [PinkPetals] = 분홍 꽃잎 / Pink Petals
   EN: Inflict [PinkPetals]
   PL: Nakłada [PinkPetals]
451. [Dar E.G.O [9239] — nazwa] 분홍빛 꽃잎다발
   źródło: EGOgift_walpu8.json :: dataList[id=9239].name
   limit: do 40 znaków
   EN: Pink Bouquet
   PL: Różowy Bukiet
452. [Dar E.G.O [9239] — opis] 관통 스킬을 사용하여 적에게 적중 시, 다음 턴에 [Agility] 1, [PenetrateDamageUp] 1 얻음 (인격별 턴당 2회)\n- 해당 스킬로 적 처치 시, 다음 턴에 [Agility] 1, [PenetrateDamageUp] 2 추가로 얻음 (인격별 턴당 1회)\n\n[Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 스킬로 적에게 공격 적중 시, [PinkPetals] 2 부여\n- 적의 [Sinking] 위력 5당, [PinkPetals] 1 추가 부여 (최대 4)\n- 적의 [PinkPetals] 수치가 10 이상이면, 공격 적중 시 [Vibration] 2 부여 (턴당 3회)\n\n턴 종료 시, [Sinking]과 [Vibration] 위력의 합 5 이상 보유한 적(환상체일 경우, 해당 부위)에게 다음 턴에 [Binding] 2, [DefenseDown] 3 부여\n- 대상이 [Sinking]과 [Vibration] 위력의 합이 10 이상이면, 효과가 강화되어 [Binding] 2, [Paralysis] 1, [DefenseDown] 4 부여\n\n턴 종료 시 모든 적에게 [PinkPetals]이 있을 경우, 다음 턴에 모든 아군이 [Enhancement] 1 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9239].desc
   limit: do 1140 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [PenetrateDamageUp], [Sinking], [PinkPetals], [Vibration], [Binding], [DefenseDown], [Paralysis], [Enhancement]
   znaczenie tagów: [Agility] = 신속 / Haste; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [Sinking] = 침잠 / Sinking; [PinkPetals] = 분홍 꽃잎 / Pink Petals; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Paralysis] = 마비 / Paralyze …
   EN: On Hit with a Pierce Skill against an enemy: Gain 1 [Agility] and 1 [PenetrateDamageUp] next turn (2 times per turn per Identity)\n- On enemy Kill with the said Skill: gain 1 additional [Agility] and 2 additional [PenetrateDamageUp] next turn (once per turn per Identity)\n\nOn Hit by an ally with a Skill that inflicts [Sinking] Potency, Count, or 'Unique Sinking', inflict 2 [PinkPetals]\n- Inflict 1 additional [PinkPetals] for every 5 [Sinking] on the enemy (max 4)\n- If the enemy has 10+ [PinkPetals] Stack, inflict 2 [Vibration] On Hit (3 times per turn)\n\nTurn End: Inflict 2 [Binding] and 3 [DefenseDown] next turn against enemies(for Abnormalities, Parts) with 5+ ([Sinking] + [Vibration])\n- If target has 10+ ([Sinking] + [Vibration]), inflict 2 [Binding], 1 [Paralysis], and 4 [DefenseDown] instead\n\nTurn End: If all enemies have remaining [PinkPetals] Stack, all allies gain 1 [Enhancement] next turn
   PL: Przy trafieniu wroga Umiejętnością Kłucia następna tura zyskuje 1 [Agility] i 1 [PenetrateDamageUp] (2 razy na turę na Tożsamość)\n- Jeżeli ta Umiejętność pokona wroga, dodatkowo zyskuje 1 [Agility] i 2 [PenetrateDamageUp] następnej tury (1 raz na turę na Tożsamość)\n\nGdy sojusznik trafi wroga Umiejętnością nakładającą Siłę, Licznik [Sinking] lub Szczególne Zatonięcie, nakłada 2 [PinkPetals]\n- +1 dodatkowego [PinkPetals] za każde 5 Siły [Sinking] wroga (maks. 4)\n- Jeżeli wróg ma 10+ wartości [PinkPetals], przy trafieniu nakłada 2 [Vibration] (3 razy na turę)\n\nNa koniec tury: wrogom (lub Partiom Anomalii) z sumą Sił [Sinking] i [Vibration] wynoszącą 5+ nakłada następnej tury 2 [Binding] i 3 [DefenseDown]\n- Jeżeli suma Sił [Sinking] i [Vibration] celu wynosi 10+, efekt wzmocniony: nakłada 2 [Binding], 1 [Paralysis] i 4 [DefenseDown]\n\nNa koniec tury: jeżeli wszyscy wrogowie mają [PinkPetals], wszyscy sojusznicy następnej tury zyskują 1 [Enhancement]
453. [Dar E.G.O [9239] — opis skrócony] 다음 턴에 [Agility], [PenetrateDamageUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9239].simpleDesc[abilityID=9239].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [PenetrateDamageUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Gain [Agility] and [PenetrateDamageUp] next turn
   PL: Następna tura zyskuje [Agility] i [PenetrateDamageUp]
454. [Dar E.G.O [9239] — opis skrócony] 다음 턴에 [Agility] 1, [PenetrateDamageUp] 2 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9239].simpleDesc[abilityID=92391].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [PenetrateDamageUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Gain 1 [Agility] and 2 [PenetrateDamageUp] next turn
   PL: Następna tura zyskuje 1 [Agility] i 2 [PenetrateDamageUp]
455. [Dar E.G.O [9239] — opis skrócony] [PinkPetals] 부여, 조건 만족 시 [Vibration] 부여
   źródło: EGOgift_walpu8.json :: dataList[id=9239].simpleDesc[abilityID=92392].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PinkPetals], [Vibration]
   znaczenie tagów: [PinkPetals] = 분홍 꽃잎 / Pink Petals; [Vibration] = 진동 / Tremor
   EN: Inflict [PinkPetals]. Inflict [Vibration] when conditions are met
   PL: Nakłada [PinkPetals]. Nakłada [Vibration] przy spełnionych warunkach
456. [Dar E.G.O [9239] — opis skrócony] 다음 턴에 [Binding], [DefenseDown] 부여, 조건 만족 시 [Binding], [Paralysis], [DefenseDown] 부여
   źródło: EGOgift_walpu8.json :: dataList[id=9239].simpleDesc[abilityID=92393].simpleDesc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Binding], [DefenseDown], [Paralysis]
   znaczenie tagów: [Binding] = 속박 / Bind; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Paralysis] = 마비 / Paralyze
   EN: Inflict [Binding] and [DefenseDown] next turn. Inflict [Binding], [Paralysis], and [DefenseDown] when conditions are met
   PL: Nakłada [Binding] i [DefenseDown] następnej tury. Przy spełnionych warunkach nakłada [Binding], [Paralysis] i [DefenseDown]
457. [Dar E.G.O [9239] — opis skrócony] 다음 턴에 모든 아군 [Enhancement] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9239].simpleDesc[abilityID=92394].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: All allies gain [Enhancement] next turn
   PL: Wszyscy sojusznicy następnej tury zyskują [Enhancement]
458. [Dar E.G.O [9240] — nazwa] 로열 젤리 퍼퓸
   źródło: EGOgift_walpu8.json :: dataList[id=9240].name
   limit: do 40 znaków
   EN: Royal Jelly Perfume
   PL: Perfumy z Mleczka Królowej
459. [Dar E.G.O [9240] — opis] [편성 6번 인격 전용 효과]\n\n스테이지 시작 시 [QueenBeepheromone] 얻음\n\n[Combustion]이 있는 적에게 받는 피해량 -15%\n\n턴 종료 시 자신에게 피해를 가장 많이 준 적 1명(집중 전투에서는 부위로 판정)에게 다음 턴에 [QueenBeeMark] 부여\n- 적에게 피해를 받지 않았으면, 무작위 적 1명(집중 전투에서는 부위로 판정)에게 다음 턴에 [QueenBeeMark] 부여
   źródło: EGOgift_walpu8.json :: dataList[id=9240].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [QueenBeepheromone], [Combustion], [QueenBeeMark]
   znaczenie tagów: [QueenBeepheromone] = 페로몬 / Pheromone; [Combustion] = 화상 / Burn; [QueenBeeMark] = 페로몬 표식 / Pheromone Mark
   EN: [Effects apply only to #6 Deployed Identity]\n\nEncounter Start: Gain [QueenBeepheromone]\n\nTake -15% damage from enemies with [Combustion]\n\nTurn End: Inflict [QueenBeeMark] next turn against the enemy(in Focused Encounters, the Part) that dealt the most damage to this unit\n- If allies did not take any damage from enemies, inflict [QueenBeeMark] next turn against 1 random enemy(in Focused Encounters, a Part)
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #6]\n\nPoczątek walki: zyskuje [QueenBeepheromone]\n\nOtrzymuje -15% obrażeń od wrogów z [Combustion]\n\nNa koniec tury: nakłada [QueenBeeMark] następnej tury na 1 wroga (w starciu skupionym liczone per Część), który zadał tej jednostce najwięcej obrażeń\n- Jeżeli sojusznicy nie otrzymali od wrogów żadnych obrażeń, nakłada [QueenBeeMark] następnej tury na 1 losowego wroga (w starciu skupionym liczone per Część)
460. [Dar E.G.O [9240] — opis skrócony] [QueenBeepheromone]을 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9240].simpleDesc[abilityID=9240].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [QueenBeepheromone]
   znaczenie tagów: [QueenBeepheromone] = 페로몬 / Pheromone
   EN: Gain [QueenBeepheromone]
   PL: Zyskuje [QueenBeepheromone]
461. [Dar E.G.O [9240] — opis skrócony] [QueenBeeMark] 부여
   źródło: EGOgift_walpu8.json :: dataList[id=9240].simpleDesc[abilityID=92401].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [QueenBeeMark]
   znaczenie tagów: [QueenBeeMark] = 페로몬 표식 / Pheromone Mark
   EN: Inflict [QueenBeeMark]
   PL: Nakłada [QueenBeeMark]
462. [Dar E.G.O [9241] — nazwa] 아직 따뜻한 커피
   źródło: EGOgift_walpu8.json :: dataList[id=9241].name
   limit: do 40 znaków
   EN: Still-warm Coffee
   PL: Jeszcze Ciepła Kawa
463. [Dar E.G.O [9241] — opis] [편성 1번 인격 전용 효과]\n\n공격 스킬을 사용한 턴 종료 시 정신력 5 회복\n- 이후, 정신력이 최대고 해당 아군이 로보토미 소속 인격이면, 다음 턴에 [PlusCoinValueUp] 1 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9241].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [PlusCoinValueUp]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: [Effects apply only to #1 Deployed Identity]\n\nTurn End after using an Attack Skill: Heal 5 SP\n- Then, if the affected unit is at max HP and is a Lobotomy Corp. Identity, gain 1 [PlusCoinValueUp] next turn
   PL: [Efekt wyłącznie dla Tożsamości na Przydziale #1]\n\nNa koniec tury, w której użyto Umiejętności ataku, odzyskuje 5 SP\n- Następnie, jeżeli SP jest pełne, a dotknięty sojusznik jest Tożsamością frakcji Lobotomii, następna tura zyskuje 1 [PlusCoinValueUp]
464. [Dar E.G.O [9241] — opis skrócony] 정신력 회복, 조건 만족 시 다음 턴에 [PlusCoinValueUp] 얻음
   źródło: EGOgift_walpu8.json :: dataList[id=9241].simpleDesc[abilityID=9241].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PlusCoinValueUp]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: Heal SP; gain [PlusCoinValueUp] next turn if conditions are met
   PL: Odzyskuje SP; przy spełnionych warunkach następna tura zyskuje [PlusCoinValueUp]

## Dar E.G.O: EgoGiftCategory
- plik gry: `EgoGiftCategory.json`

465. [Dar E.G.O [Combustion] — nazwa] 화상
   źródło: EgoGiftCategory.json :: dataList[id=Combustion].name
   limit: do 40 znaków
   EN: Burn
   PL: Podpalenie
466. [Dar E.G.O [Laceration] — nazwa] 출혈
   źródło: EgoGiftCategory.json :: dataList[id=Laceration].name
   limit: do 40 znaków
   EN: Bleed
   PL: Krwawienie
467. [Dar E.G.O [Vibration] — nazwa] 진동
   źródło: EgoGiftCategory.json :: dataList[id=Vibration].name
   limit: do 40 znaków
   EN: Tremor
   PL: Wstrząs
468. [Dar E.G.O [Burst] — nazwa] 파열
   źródło: EgoGiftCategory.json :: dataList[id=Burst].name
   limit: do 40 znaków
   EN: Rupture
   PL: Rozdarcie
469. [Dar E.G.O [Sinking] — nazwa] 침잠
   źródło: EgoGiftCategory.json :: dataList[id=Sinking].name
   limit: do 40 znaków
   EN: Sinking
   PL: Zatonięcie
470. [Dar E.G.O [Breath] — nazwa] 호흡
   źródło: EgoGiftCategory.json :: dataList[id=Breath].name
   limit: do 40 znaków
   EN: Poise
   PL: Oddech
471. [Dar E.G.O [Charge] — nazwa] 충전
   źródło: EgoGiftCategory.json :: dataList[id=Charge].name
   limit: do 40 znaków
   EN: Charge
   PL: Ładowanie
472. [Dar E.G.O [Random] — nazwa] 무작위
   źródło: EgoGiftCategory.json :: dataList[id=Random].name
   limit: do 40 znaków
   EN: Random
   PL: Losowo
473. [Dar E.G.O [Slash] — nazwa] 참격
   źródło: EgoGiftCategory.json :: dataList[id=Slash].name
   limit: do 40 znaków
   EN: Slash
   PL: Cięcie
474. [Dar E.G.O [Penetrate] — nazwa] 관통
   źródło: EgoGiftCategory.json :: dataList[id=Penetrate].name
   limit: do 40 znaków
   EN: Pierce
   PL: Kłucie
475. [Dar E.G.O [Hit] — nazwa] 타격
   źródło: EgoGiftCategory.json :: dataList[id=Hit].name
   limit: do 40 znaków
   EN: Blunt
   PL: Obuch
476. [Dar E.G.O [None] — nazwa] 범용
   źródło: EgoGiftCategory.json :: dataList[id=None].name
   limit: do 40 znaków
   EN: Keywordless
   PL: Uniwersalny

## Dar E.G.O: MirrorDungeonEgoGiftLockedDesc
- plik gry: `MirrorDungeonEgoGiftLockedDesc.json`

477. [Dar E.G.O [9088] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9088].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Shops - 「Fuse E.G.O Gift」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Sklep 「Synteza Daru E.G.O」
478. [Dar E.G.O [9090] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9090].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Dar E.G.O [9092] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9092].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Dar E.G.O [9094] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9094].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Dar E.G.O [9096] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9096].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Dar E.G.O [9098] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9098].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Dar E.G.O [9100] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9100].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Dar E.G.O [9410] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9410].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Dar E.G.O [9416] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9416].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Dar E.G.O [9424] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9424].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Dar E.G.O [9430] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9430].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Dar E.G.O [9434] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9434].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Dar E.G.O [9717] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9717].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Dar E.G.O [9718] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9718].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Dar E.G.O [9728] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9728].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Dar E.G.O [9729] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9729].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Dar E.G.O [9730] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9730].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Dar E.G.O [9731] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9731].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Dar E.G.O [9740] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9740].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Dar E.G.O [9741] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9741].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Dar E.G.O [9742] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9742].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Dar E.G.O [9743] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9743].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Dar E.G.O [9761] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9761].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Dar E.G.O [9764] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9764].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Dar E.G.O [9765] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9765].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Dar E.G.O [9780] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9780].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Dar E.G.O [9783] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9783].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Dar E.G.O [9784] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9784].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Dar E.G.O [9799] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 어떤 철학을 마주하기
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9799].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Confront a certain philosophy
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Stanąć twarzą w twarz z pewną filozofią
506. [Dar E.G.O [9800] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 당신의 운을 시험해 보세요!
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9800].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Test your luck!
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Przetestuj swoje szczęście!
507. [Dar E.G.O [9792] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9792].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Dar E.G.O [9793] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9793].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Dar E.G.O [9825] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9825].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Dar E.G.O [9841] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9841].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Dar E.G.O [9167] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9167].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Dar E.G.O [9171] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9171].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Dar E.G.O [9176] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9176].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Dar E.G.O [9184] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9184].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Dar E.G.O [9158] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9158].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Dar E.G.O [9162] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9162].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Dar E.G.O [9180] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9180].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Dar E.G.O [9157] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9157].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Dar E.G.O [9161] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9161].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Dar E.G.O [9166] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9166].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Dar E.G.O [9170] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9170].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Dar E.G.O [9175] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9175].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Dar E.G.O [9179] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9179].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Dar E.G.O [9183] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9183].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Dar E.G.O [9213] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9213].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Dar E.G.O [9216] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9216].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Dar E.G.O [9224] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9224].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Dar E.G.O [9212] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9212].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Dar E.G.O [9207] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 선택지 「확률과 선택」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9207].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Choice 「Chance & Choice」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Wybór 「Szansa i Wybór」
530. [Dar E.G.O [9227] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 선택지 「귀기 서린 환도」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9227].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Choice 「Baleful Hwando」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Wybór 「Hwando Przesiąknięte Złą Aurą」
531. [Dar E.G.O [9228] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 저주 해제 「귀기 서린 환도」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9228].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Lift Curse from「Baleful Hwando」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Zdjęcie Klątwy z 「Hwando Przesiąknięte Złą Aurą」
532. [Dar E.G.O [9229] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 선택지 「빛바랜 건틀릿」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9229].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Choice 「Tarnished Gauntlet」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Wybór 「Wyblakła Rękawica」
533. [Dar E.G.O [9230] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 저주 해제 「빛바랜 건틀릿」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9230].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Lift Curse from「Tarnished Gauntlet」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Zdjęcie Klątwy z 「Wyblakła Rękawica」
534. [Dar E.G.O [9231] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 선택지 「그날의 기록」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9231].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Choice 「Record Logs of That Day」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Wybór 「Zapisy Tego Dnia」
535. [Dar E.G.O [9232] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 저주 해제 「그날의 기록」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9232].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Lift Curse from 「Record Logs of That Day」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Zdjęcie Klątwy z 「Zapisy Tego Dnia」
536. [Dar E.G.O [9235] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9235].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Dar E.G.O [9239] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9239].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Dar E.G.O [9241] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 선택지 「아직 따뜻한 커피」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9241].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Acquisition Records\n\n<Unlock Conditions>\n- Choice 「Still-warm Coffee」
   PL: Brak historii zdobycia\n\n\n<Warunek odblokowania>\n- Wybór 「Jeszcze Ciepła Kawa」
539. [Dar E.G.O [9248] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9248].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Dar E.G.O [9249] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9249].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Dar E.G.O [9301] — tekst] 획득 기록 없음\n\n\n<획득 조건>\n- 상점 「E.G.O 기프트 합성」
   źródło: MirrorDungeonEgoGiftLockedDesc.json :: dataList[id=9301].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
