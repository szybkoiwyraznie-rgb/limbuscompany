# Paczka AI P40 (Fala 2 · 2C) — Tabela modeli postaci oraz interfejs, zadania i przedmioty RPG Canto X (część 2/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P40_2c_modele_i_rpg_ui_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P40_2c_modele_i_rpg_ui_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tryb RPG [common] — rpg-loc-item-common-a1c10p1
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-item-common-a1c10p1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

1. [RPG [I104002] — opis] 행복한 옷장이 내어준 옷. 등굽은 조명에게 입혀 주자.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I104002].description
   limit: do 120 znaków
   EN: An outfit given by the Happy Closet. Let's hand it over to the Arc Floor Lamp.
   PL: Ubranie podarowane przez Szczęśliwą Szafę. Przekaż je Łukowej Lampie Podłogowej.
2. [RPG [I104003] — nazwa wyświetlana] 종이 조각
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I104003].displayName
   limit: do 40 znaków
   EN: Scrap of Paper
   PL: Kawałek Papieru
3. [RPG [I104003] — opis] 행복한 옷장의 잔해에서부터 발견한 종이 조각. '행복'이라고 적혀 있다. 구조적으로는 어떤 역할도 하지 않았지만, 행복한 옷장이 존재할 수 있도록 도와주었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I104003].description
   limit: do 250 znaków
   EN: A scrap of paper recovered from the remains of the Happy Closet. The word "Happiness" is written upon it. It served no structural purpose, yet it helped the Happy Closet to continue to exist.
   PL: Kawałek papieru znaleziony w szczątkach Szczęśliwej Szafy. Widnieje na nim słowo „szczęście”. Strukturalnie nie pełnił żadnej roli, ale pozwalał Szczęśliwej Szafie trwać przy istnieniu.
4. [RPG [I1201] — nazwa wyświetlana] 테이프
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1201].displayName
   limit: do 40 znaków
   EN: Audiotape
   PL: Taśma Dźwiękowa
5. [RPG [I1201] — opis] 붉은 신이 이전에 읊어주던 옛 목소리가 반복된다. 르루주들이 듣던 목소리. 신실한 누군가는 더 깊은 이야기를 들을 수도 있었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1201].description
   limit: do 220 znaków
   EN: The Crimson God's old Voice plays again, repeating what it once recited. It is the Voice the Rouges once heard. Those of stronger faith could hear a more profound story.
   PL: Odtwarza się dawny Głos, który kiedyś wyrecytował Szkarłatny Bóg. To głos, którego słuchali Le Rouge. Ci bardziej wierni mogli usłyszeć głębszą opowieść.
6. [RPG [I1206] — nazwa wyświetlana] 날이 잘 든 재봉 가위
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1206].displayName
   limit: do 50 znaków
   EN: Well-sharpened Sewing Scissors
   PL: Ostrokrajne Nożyczki Krawieckie
7. [RPG [I1206] — opis] 가위는 대극의 결합으로 존재를 가른다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1206].description
   limit: do 120 znaków
   EN: Scissors divide existence through the joining of opposites.
   PL: Nożyczki dzielą istnienie przez połączenie przeciwieństw.
8. [RPG [I1207] — nazwa wyświetlana] 르누아르의 감정평가서
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1207].displayName
   limit: do 50 znaków
   EN: Le Noir Authenticity Certificate
   PL: Świadectwo Autentyczności Le Noir
9. [RPG [I1207] — opis] 본 고객은 르누아르의 훌륭한 고객으로서 브랜드의 가치 보존에 힘써주었음.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1207].description
   limit: do 160 znaków
   EN: This customer has proven to be an exemplary patron of Le Noir and has contributed to the preservation of the brand's value.
   PL: Niniejszy klient udowodnił, że jest wzorowym klientem Le Noir i przyczynił się do zachowania wartości marki.
10. [RPG [I1208] — nazwa wyświetlana] 검고 붉은 실
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1208].displayName
   limit: do 40 znaków
   EN: Black-and-Red Thread
   PL: Czarno-Czerwona Nić
11. [RPG [I1208] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +1\n\n상징계 <color=#fe4b48>공격 속도</color> +10%\n\n상징계 <color=#F8C200>이동 속도</color> +5%\n\n상징계에서 르누아르 점원[햇살], 르루주 점원[햇살] 계열 적에게 받는 <color=#fe4b48>피해량</color> -1, 가하는 <color=#fe4b48>피해량</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1208].statText
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#fe4b48>, <color=#F8C200>, \n
   EN: Symbolic <color=#00ff9c>HP</color> +1\n\n<color=#fe4b48>Attack Speed</color> +10% in the Symbolic\n\n<color=#F8C200>Movement Speed</color> +5% in the Symbolic\n\nAgainst Le Noir Sales Associate [Sunshone] and Le Rouge Sales Associate [Sunshone]-type enemies in the Symbolic:\n- <color=#fe4b48>Damage</color> Taken -1\n- <color=#fe4b48>Damage</color> Dealt +1
   PL: Symboliczne <color=#00ff9c>HP</color> +1\n\n<color=#fe4b48>Szybkość Ataku</color> +10% w Symbolicznym\n\n<color=#F8C200>Szybkość Ruchu</color> +5% w Symbolicznym\n\nPrzeciwko wrogom typu Pracownik Le Noir [Sunshone] i Pracownik Le Rouge [Sunshone] w Symbolicznym:\n- otrzymywane <color=#fe4b48>Obrażenia</color> -1, zadawane <color=#fe4b48>Obrażenia</color> +1
12. [RPG [I1208] — opis] 균열에서 빛이 새어 나와 백화점의 모든 사람들에게 닿았을 때, 백화점의 사람들은 점차 바뀌어갔다. 그들이 추구하는 가치의 모습으로, 그들이 추종하는 브랜드가 좇는 가치의 모습으로. 그 변화 속에서 이성을 잃으면, 마네킹이라고 불릴 뿐, 본질은 다를 바가 없다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1208].description
   limit: do 470 znaków
   EN: When light spilled through the cracks and touched everyone, the people in the department store began to change. They took the shape of the values they pursued, the shape of the values pursued by the brands they followed. Those who lost their reason in the transformation came to be called Mannequins. In essence, however, they were no different from the rest of us.
   PL: Gdy światło przeciekło przez pęknięcia i dosięgnęło wszystkich, ludzie w Grand Magasin zaczęli się zmieniać. Przybierali kształt wartości, których się trzymali, kształt wartości, za którymi podążały brandy, które wyznawali. Ci, którzy stracili w tej przemianie rozum, zaczęli być nazywani Manekinami. W istocie jednak nie różnili się od reszty z nas.
13. [RPG [I990001] — nazwa wyświetlana] 못
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990001].displayName
   limit: do 40 znaków
   EN: Nail
   PL: Gwóźdź
14. [RPG [I990001] — statystyki przedmiotu] 상징계에서 <color=#F8C200>약점 공격</color> 시 <color=#fe4b48>피해량</color> +1\n- 약점 공격 : 적의 후방에서 공격 시 발동 (일부 적 제외)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990001].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, <color=#F8C200>Weakpoint Attack</color> <color=#fe4b48>Damage</color> Dealt +1\nWeakpoint Attack: Triggers when attacking an enemy from behind (excluding certain enemies)
   PL: W Symbolicznym <color=#F8C200>Atak na Słaby Punkt</color> zadaje <color=#fe4b48>Obrażenia</color> +1\n- Atak na Słaby Punkt: uruchamia się przy ataku od tyłu wroga (z wyłączeniem części wrogów)
15. [RPG [I990001] — opis] 못. 못은 대상을 고정시킨다. 망치 없이는 박히지 못한다. 하지만 망치가 없어도, 못에 몸을 던지는 자들은 제멋대로 못 박힌다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990001].description
   limit: do 230 znaków
   EN: A nail. Nails fix their targets in place. Without a hammer, they cannot be driven in. Yet those who throw themselves upon a nail will pin themselves down, hammer or no hammer.
   PL: Gwóźdź. Gwóździe mocują cele w miejscu. Bez młotka nie da się go wbić. Ale nawet bez młotka ci, którzy rzucają się na gwóźdź, wbijają się sami.
16. [RPG [I990006] — nazwa wyświetlana] 무뎌진 재봉 가위
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990006].displayName
   limit: do 40 znaków
   EN: Dull Sewing Scissors
   PL: Ztępione Nożyczki Krawieckie
17. [RPG [I990006] — opis] 수선사는 중립이어야 하지 않냐고요? 르누아르가 원단을 좋아하고 르루주는 가죽을 좋아하는데 과연 수선사는 누구를 더 필요로 하고 누구에게 가위를 더 건네주려 하겠나요?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990006].description
   limit: do 310 znaków
   EN: You ask whether the Alterationist ought to remain neutral? The Noirs favor fabric, while the Rouges prefer hide. Think about it: which brand, then, needs the Alterationist more... and to whom will she be more willing to give her scissors?
   PL: Pytasz, czy krawcowa powinna pozostawać neutralna? Le Noir kochają tkaniny, a Le Rouge skóry. Zastanów się: której brandy krawcowa bardziej potrzebuje... i komu chętniej podaruje nożyczki?
18. [RPG [I990101] — nazwa wyświetlana] 르누아르의 컨템포러리 가디건
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990101].displayName
   limit: do 50 znaków
   EN: Le Noir Contemporary Cardigan
   PL: Kardigan Contempora Le Noir
19. [RPG [I990101] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990101].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>
   EN: Symbolic <color=#00ff9c>HP</color> +2
   PL: Symboliczne <color=#00ff9c>HP</color> +2
20. [RPG [I990101] — opis] 당신은 백화점 벽에 균열이 처음 생겼을 때를, 기억하시나요?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990101].description
   limit: do 120 znaków
   EN: Do you remember the first crack that appeared in the walls of the Grand Magasin?
   PL: Pamiętasz, kiedy na ścianach Grand Magasin pierwszy raz pojawiło się pęknięcie?
21. [RPG [I990102] — nazwa wyświetlana] 르누아르의 컨템포러리 모자
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990102].displayName
   limit: do 40 znaków
   EN: Le Noir Contemporary Hat
   PL: Kapelusz Contempora Le Noir
22. [RPG [I990102] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990102].statText
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [RPG [I990102] — opis] 백화점은, 보존되어야 합니다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990102].description
   limit: do 120 znaków
   EN: The Grand Magasin must be eternally preserved.
   PL: Grand Magasin musi być zachowany na wieczność.
24. [RPG [I990103] — nazwa wyświetlana] 르누아르의 컨템포러리 신사 모자
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990103].displayName
   limit: do 50 znaków
   EN: Le Noir Contemporary Gentleman Hat
   PL: Kapelusz Gentlemena Contempora Le Noir
25. [RPG [I990103] — statystyki przedmiotu] 상징계에서 아무 조작도 하지 않으면 5초마다 상징계 <color=#00ff9c>체력</color> 1 <color=#00ff9c>회복</color> (최대 3회)\n- 샘터에서 휴식 시 재충전
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990103].statText
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: If no player inputs are made, <color=#00ff9c>heals</color> 1 Symbolic <color=#00ff9c>HP</color> every 5 seconds (3 times)\n- Rest at the Fount to recharge
   PL: Jeśli przez 5 sekund nie wykonasz żadnej akcji, <color=#00ff9c>leczy</color> 1 Symboliczne <color=#00ff9c>HP</color> (maks. 3 razy)\n- Odpoczynek przy Źródle ładuje ponownie
26. [RPG [I990103] — opis] 균열은 더 커지고 더 많이 생겨났다. 어째서?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990103].description
   limit: do 120 znaków
   EN: The cracks spread wider, multiplying. Why?
   PL: Pęknięcia robiły się coraz większe i coraz liczniejsze. Dlaczego?
27. [RPG [I990104] — nazwa wyświetlana] 르루주의 SPA 후드 집업
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990104].displayName
   limit: do 50 znaków
   EN: Le Rouge Casualwear Zip-up Hoodie
   PL: Hoodie SPA z Zamkiem Le Rouge
28. [RPG [I990104] — statystyki przedmiotu] 상징계 공격 <color=#fe4b48>피해량</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990104].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: <color=#fe4b48>Damage</color> Dealt +1 in the Symbolic
   PL: <color=#fe4b48>Obrażenia</color> zadawane +1 w Symbolicznym
29. [RPG [I990104] — opis] 우리의 신은 어디로 갔는가…
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990104].description
   limit: do 120 znaków
   EN: Where has our God gone?
   PL: Dokąd odszedł nasz Bóg…
30. [RPG [I990105] — nazwa wyświetlana] 르루주의 SPA 치마
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990105].displayName
   limit: do 40 znaków
   EN: Le Rouge Casualwear Skirt
   PL: Spódnica SPA Le Rouge
31. [RPG [I990105] — statystyki przedmiotu] 상징계 <color=#F8C200>이동 속도</color> +5%\n\n상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990105].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: <color=#F8C200>Movement Speed</color> +5% in the Symbolic\n\nSymbolic <color=#00ff9c>HP</color> +1
   PL: <color=#F8C200>Szybkość Ruchu</color> +5% w Symbolicznym\n\nSymboliczne <color=#00ff9c>HP</color> +1
32. [RPG [I990105] — opis] 붉은 신의 목소리가, 더는 들리지 않아…
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990105].description
   limit: do 120 znaków
   EN: I can no longer hear the Crimson God's Voice...
   PL: Głosu Szkarłatnego Boga już nie słyszę…
33. [RPG [I990106] — nazwa wyświetlana] 르루주의 컨템포러리 지퍼
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990106].displayName
   limit: do 40 znaków
   EN: Le Rouge Contemporary Zipper
   PL: Zamek Contempora Le Rouge
34. [RPG [I990106] — statystyki przedmiotu] 상징계에서 <color=#F8C200>달리기</color> 해금\n- 달리기 시 <color=#F8C200>이동 속도</color> +30%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990106].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: Unlocks <color=#F8C200>Sprint</color> in the Symbolic\n- Sprint: <color=#F8C200>Movement Speed</color> +30%
   PL: Odblokowuje <color=#F8C200>Bieg</color> w Symbolicznym\n- Bieg: <color=#F8C200>Szybkość Ruchu</color> +30%
35. [RPG [I990106] — opis] 르루주는 생명과 그 맥동에 가치를 두고 의미를 부여한다. 그리고 경험을 기대한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990106].description
   limit: do 140 znaków
   EN: The Rouges find value and meaning in life and every pulse of it. They wait in anticipation for experience.
   PL: Le Rouge nadają wartość i znaczenie życiu i każdemu jego tętnu. I czekają na doświadczenie.
36. [RPG [I990107] — nazwa wyświetlana] 르루주의 컨템포러리 양말
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990107].displayName
   limit: do 40 znaków
   EN: Le Rouge Contemporary Socks
   PL: Skarpety Contempora Le Rouge
37. [RPG [I990107] — statystyki przedmiotu] 그림자계 전투 진입 시 모든 적에게 <color=#F8C200>출혈</color> 위력 2, <color=#F8C200>출혈</color> 횟수 2 부여\n\n상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990107].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: Upon entering battle in the Shadowed, inflicts 2 <color=#F8C200>Bleed</color> Potency and +2 <color=#F8C200>Bleed</color> Count on all enemies\n\nSymbolic <color=#00ff9c>HP</color> +1
   PL: Po wejściu do walki w Zacienionym nakłada wszystkim wrogom 2 <color=#F8C200>Moc Krwawienia</color> i +2 <color=#F8C200>Liczba Krwawienia</color>\n\nSymboliczne <color=#00ff9c>HP</color> +1
38. [RPG [I990107] — opis] 붉은색은 피와 살점 그리고 가죽.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990107].description
   limit: do 120 znaków
   EN: Red is blood, flesh, and hide.
   PL: Czerwień to krew, mięso i skóra.
39. [RPG [I990108] — nazwa wyświetlana] 43cm의 커다랗고 날카로운 못
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990108].displayName
   limit: do 40 znaków
   EN: Huge Sharp Needle (43cm)
   PL: Ogromny Ostry Gwóźdź (43 cm)
40. [RPG [I990108] — opis] 따뜻한 목소리를 듣고 마네킹이 되어버린 존재들. 그 마네킹 중에서도 목소리에 더 깊이 안겼던 것은, 한 발짝 더 나아간다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990108].description
   limit: do 200 znaków
   EN: Those who heard the Voice of warmth turned into Mannequins. Of those, the ones held deepest in the Voice's embrace are able to take one step farther.
   PL: Istoty, które usłyszały ciepły Głos, zamieniły się w Manekiny. A z tych Manekinów te najgłębiej wtulone w Głos czynią krok dalej.
41. [RPG [I990110] — nazwa wyświetlana] 에너지 음료
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990110].displayName
   limit: do 40 znaków
   EN: Energy Drink
   PL: Napój Energetyczny
42. [RPG [I990110] — statystyki przedmiotu] 상징계에서 공격이 적중한 이후 5초 동안 공격하지 않으면, 다음 상징계 공격의 <color=#fe4b48>피해량</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990110].statText
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: In the Symbolic, if 5 seconds have elapsed without attacking after landing a hit on the enemy, <color=#fe4b48>Damage</color> Dealt +3 on the next attack
   PL: W Symbolicznym, jeśli po trafieniu wroga przez 5 sekund nie atakujesz, następny atak w Symbolicznym zadaje <color=#fe4b48>Obrażenia</color> +3
43. [RPG [I990110] — opis] 시지프 백화점에서는 음식을 열량과 생존을 위해 먹지 않는다. 오로지 허기진 마음을 채우기 위해 섭취한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990110].description
   limit: do 180 znaków
   EN: At Grand Magasin Sisyphe, food is not consumed for energy or survival. It is taken for one purpose alone: to sate the hunger of the heart.
   PL: W Grand Magasin Sisyphe nie je się dla kalorii ani przetrwania. Spożywa się wyłącznie po to, by ukoić głód serca.
44. [RPG [I990303] — nazwa wyświetlana] 수선실에서 파는 천
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990303].displayName
   limit: do 50 znaków
   EN: Fabric from the Alteration Shop
   PL: Tkanina z Warsztatu Poprawek
45. [RPG [I990303] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990303].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>
   EN: Symbolic <color=#00ff9c>HP</color> +1
   PL: Symboliczne <color=#00ff9c>HP</color> +1
46. [RPG [I990303] — opis] 르루주, 르누아르도 아닌 나는 중립적인 가치를 추구해. 어느 브랜드든 원단을 원한다면, 기꺼이 거래할 거야.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990303].description
   limit: do 180 znaków
   EN: I belong to neither Le Rouge nor Le Noir. Mine is a neutral value. Whichever brand comes seeking fabric, I will gladly trade with them.
   PL: Nie należę ani do Le Rouge, ani do Le Noir. Moja wartość jest neutralna. Którekolwiek z brandy zapragnie tkaniny — chętnie się wymienię.
47. [RPG [I990304] — nazwa wyświetlana] 르루주 부티크 선글라스
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990304].displayName
   limit: do 40 znaków
   EN: Boutique du Rouge Sunglasses
   PL: Okulary Słoneczne Boutique du Rouge
48. [RPG [I990304] — statystyki przedmiotu] 상징계에서 <color=#F8C200>약점 공격</color> 시 <color=#fe4b48>피해량</color> +1\n\n상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990304].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, <color=#00ff9c>, \n
   EN: In the Symbolic, <color=#F8C200>Weakpoint Attack</color> <color=#fe4b48>Damage</color> Dealt +1\n\nSymbolic <color=#00ff9c>HP</color> +1
   PL: W Symbolicznym <color=#F8C200>Atak na Słaby Punkt</color> zadaje <color=#fe4b48>Obrażenia</color> +1\n\nSymboliczne <color=#00ff9c>HP</color> +1
49. [RPG [I990304] — opis] 눈이 부셔서 선글라스를 껴요. 그리고 햇살을 다시 쳐다봐요. 선글라스는 햇빛을 보지 않기 위해 쓰는 것이 아니라 더 잘 보려고 쓰는 거니까요.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990304].description
   limit: do 210 znaków
   EN: You put on sunglasses because the light is too bright. Then you look back into the sun. Sunglasses are not worn to avoid the sunlight, but to see it more clearly.
   PL: Okulary przeciwsłoneczne zakłada się, bo światło oślepia. A potem patrzy się w słońce. Okularów nie nosi się po to, by nie widzieć słońca, lecz po to, by widzieć je lepiej.
50. [RPG [I990305] — nazwa wyświetlana] 르루주 부티크 티셔츠
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990305].displayName
   limit: do 40 znaków
   EN: Boutique du Rouge T-Shirt
   PL: T-Shirt Boutique du Rouge
51. [RPG [I990305] — statystyki przedmiotu] 상징계 공격 적중 시 5초 동안 <color=#F8C200>이동 속도</color> +5%\n\n상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990305].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, <color=#F8C200>Movement Speed</color> +5% upon landing an attack\n\nSymbolic <color=#00ff9c>HP</color> +1
   PL: W Symbolicznym po trafieniu atakiem przez 5 sekund <color=#F8C200>Szybkość Ruchu</color> +5%\n\nSymboliczne <color=#00ff9c>HP</color> +1
52. [RPG [I990305] — opis] 우리의 신이 침묵하고 균열이 더 벌어졌을 때… 누군가는 다시 목소리를 들었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990305].description
   limit: do 120 znaków
   EN: When our God fell silent and the cracks yawned wider... some of us heard the Voice again.
   PL: Gdy nasz Bóg zamilkł, a pęknięcia rozstąpiły się szerzej… ktoś znów usłyszał Głos.
53. [RPG [I990306] — nazwa wyświetlana] 르루주 부티크 데님
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990306].displayName
   limit: do 40 znaków
   EN: Boutique du Rouge Denim
   PL: Denim Boutique du Rouge
54. [RPG [I990306] — statystyki przedmiotu] 상징계 공격의 <color=#fe4b48>공격 속도</color> +10%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990306].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: <color=#fe4b48>Attack Speed</color> +10% in the Symbolic
   PL: <color=#fe4b48>Szybkość Ataku</color> +10% w Symbolicznym
55. [RPG [I990306] — opis] 르루주는 슬림 핏을 추구한답니다. 몸의 라인을 드러내는 것이야말로 패션의 가치니까요.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990306].description
   limit: do 140 znaków
   EN: The Rouges favor a slim fit. What greater worth can fashion hold than laying bare the body's own lines?
   PL: Le Rouge preferują kroje slim fit. Bo nic nie niesie wartości mody tak, jak odsłanianie linii ciała.
56. [RPG [I990307] — nazwa wyświetlana] 르누아르 메종 넥타이
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990307].displayName
   limit: do 40 znaków
   EN: Maison du Noir Necktie
   PL: Krawat Maison du Noir
57. [RPG [I990307] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990307].statText
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [RPG [I990307] — opis] 르누아르의 옷은 고객님의 몸을 가려, 체형을 보완해줍니다. 몸을 가려주는 것이야말로 패션의 가치입니다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990307].description
   limit: do 210 znaków
   EN: What we offer—exquisite garments designed by the Noirs—conceals the customer's body and corrects the silhouette beneath. Fashion's worth lies in what it covers.
   PL: Ubrania Le Noir zakrywają ciało klienta i korygują sylwetkę. Zakrywanie ciała to właśnie wartość mody.
59. [RPG [I990308] — nazwa wyświetlana] 르누아르 메종 슬랙스
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990308].displayName
   limit: do 40 znaków
   EN: Maison du Noir Slacks
   PL: Slacks Maison du Noir
60. [RPG [I990308] — statystyki przedmiotu] 상징계에서 피격 시 <color=#F8C200>무적</color> 시간 +0.05초
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990308].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, <color=#F8C200>Invul. Frame</color> +0.05 seconds when hit
   PL: W Symbolicznym przy trafieniu <color=#F8C200>Klatka Niewrażliwości</color> +0.05 s
61. [RPG [I990308] — opis] 르누아르든 르루주든… 누군가의 목소리를 듣더니 미쳐가는 놈들이 생기더군.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990308].description
   limit: do 120 znaków
   EN: This strange voice seems to drive whoever listens to it mad, be it a Noir or a Rouge.
   PL: Le Noir czy Le Rouge… ten dziwny głos doprowadza do szaleństwa każdego, kto go usłyszy.
62. [RPG [I990309] — nazwa wyświetlana] 르누아르 메종 셔츠
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990309].displayName
   limit: do 40 znaków
   EN: Maison du Noir Shirt
   PL: Koszula Maison du Noir
63. [RPG [I990309] — statystyki przedmiotu] 그림자계 전투 진입 시 모든 적에게 <color=#F8C200>진동</color> 위력 2, <color=#F8C200>진동</color> 횟수 2 부여\n\n그림자계 전투에서 아군 피격 시 <color=#F8C200>충전</color> 횟수 2 증가 (턴당 5회)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990309].statText
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: Upon entering battle in the Shadowed, inflicts 2 <color=#F8C200>Tremor</color> Potency and +2 <color=#F8C200>Tremor</color> Count on all enemies\n\nDuring battle in the Shadowed: When an ally takes a hit, the ally gains +2 <color=#F8C200>Charge</color> Count (5 times per turn)
   PL: Po wejściu do walki w Zacienionym nakłada wszystkim wrogom 2 <color=#F8C200>Moc Wstrząsu</color> i +2 <color=#F8C200>Licznik Wstrząsu</color>\n\nW walce w Zacienionym, gdy sojusznik zostanie trafiony, otrzymuje +2 <color=#F8C200>Liczba Ładowań</color> (5 razy na turę)
64. [RPG [I990309] — opis] 백화점에는 마네킹이 가득하다. 균열에서 빛이 새어 들기 전에는, 모두가 두 팔과 두 다리를 가진 모습으로, 그 모습에 걸맞는 옷을 지었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990309].description
   limit: do 230 znaków
   EN: The Grand Magasin is filled with Mannequins. Before the sunlight began leaking through the cracks, they all had two arms and two legs, and garments were made to fit that shape.
   PL: Grand Magasin zapełnione jest Manekinami. Zanim światło zaczęło przeciekać przez pęknięcia, wszyscy mieli dwie ręce i dwie nogi, a ubrania szyto na ten kształt.
65. [RPG [I990310] — nazwa wyświetlana] 새장
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990310].displayName
   limit: do 40 znaków
   EN: Birdcage
   PL: Klatka dla Ptaków
66. [RPG [I990310] — statystyki przedmiotu] 상징계에서 피격 시 20% 확률로 받는 <color=#fe4b48>피해량</color> 20% 감소 (소수점 버림)\n\n그림자계 전투 진입 시 모든 수감자의 <color=#F8C200>충전</color> 횟수 4 증가
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990310].statText
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#F8C200>, \n
   EN: In the Symbolic, 20% chance of <color=#fe4b48>Damage</color> Taken -20% when hit (rounded down)\n\nUpon entering battle in the Shadowed, all Sinners gain +4 <color=#F8C200>Charge</color> Count
   PL: W Symbolicznym przy trafieniu 20% szans na otrzymywane <color=#fe4b48>Obrażenia</color> -20% (zaokrąglone w dół)\n\nPo wejściu do walki w Zacienionym wszyscy Grzesznicy otrzymują +4 <color=#F8C200>Liczba Ładowań</color>
67. [RPG [I990310] — opis] 새장이 있어야만 자유가 생긴다아아아. 새장이 없는 곳에는 자유라는 의미도 존재할 수 없다아아…
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990310].description
   limit: do 120 znaków
   EN: Cages bring freedom into beeeeeeing. Without cages, freedom is meaninglessssss
   PL: Właśnie dzięki klatce rodzi sięeee wolność. Tam, gdzie nie ma klatek, nie może istnieć nawet pojęcie wolnośccci…
68. [RPG [I990312] — nazwa wyświetlana] 황금못
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990312].displayName
   limit: do 40 znaków
   EN: Golden Nail
   PL: Złoty Gwóźdź
69. [RPG [I990312] — opis] 가장 고귀한 문명의 재료로 가장 원초적인 척추뼈를 감싸 만들어진 황금못. 이 바늘은 가장 낮은 것에서 가장 높은 것까지, 그 어떤 경계라도 뚫는다. 그리고 찢는다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990312].description
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: By sheathing the vertebrae, the primordial, in civilization's most exalted material, this Golden Nail was created.\nThis needle pierces every boundary, from the lowest to the highest. Then it tears.
   PL: Złoty Gwóźdź opleciony najszlachetniejszym materiałem cywilizacji wokół najprymitywniejszej kości kręgosłupa. Ta igła przebija każdą granicę — od najniższych po najwyższe. I rozdziera.
70. [RPG [I990401] — nazwa wyświetlana] 르누아르 메리 제인
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990401].displayName
   limit: do 40 znaków
   EN: Le Noir Mary Janes
   PL: Balerinki Mary Jane Le Noir
71. [RPG [I990401] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990401].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>
   EN: Symbolic <color=#00ff9c>HP</color> +3
   PL: Symboliczne <color=#00ff9c>HP</color> +3
72. [RPG [I990401] — opis] 시지프 백화점에서 이름은 옅어진다. 남는 건 제품과 브랜드의 이름뿐이다. 그래서, 더욱 옷을 껴입어야 한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990401].description
   limit: do 180 znaków
   EN: Names fade inside Grand Magasin Sisyphe. Only the names of products and brands remain. That is why one must dress in ever more layers.
   PL: W Grand Magasin Sisyphe imiona bledną. Zostają tylko nazwy produktów i brandy. Dlatego trzeba ubierać się w coraz więcej warstw.
73. [RPG [I990402] — nazwa wyświetlana] 르누아르 죠퍼 부츠
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990402].displayName
   limit: do 40 znaków
   EN: Le Noir Jodhpur Boots
   PL: Buty Jodhpur Le Noir
74. [RPG [I990402] — statystyki przedmiotu] 상징계 공격의 <color=#F8C200>경직</color> 시간 +0.1초\n\n상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990402].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: <color=#F8C200>Hitstun</color> +0.1 seconds for attacks in the Symbolic\n\nSymbolic <color=#00ff9c>HP</color> +2
   PL: <color=#F8C200>Hitstun</color> +0.1 s dla ataków w Symbolicznym\n\nSymboliczne <color=#00ff9c>HP</color> +2
75. [RPG [I990402] — opis] 고정해주세요. 조여 주세요. 불안정한 나에게 형태를 주세요. 제 자유를 바치겠어요.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990402].description
   limit: do 130 znaków
   EN: Fix me in place. Draw me tight. Bestow form on this unstable body. I offer up my freedom to you.
   PL: Unieruchom mnie. Cisnę mnie mocniej. Daj kształt mojemu niestabilnemu ciału. Ofiaruję ci moją wolność.
76. [RPG [I990403] — nazwa wyświetlana] 르누아르 보수적인 라스트
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990403].displayName
   limit: do 40 znaków
   EN: Le Noir Classic Last
   PL: Klasyczny Ostatni Le Noir
77. [RPG [I990403] — statystyki przedmiotu] 상징계에서 사망에 이르는 <color=#fe4b48>피해</color>를 받으면 <color=#00ff9c>체력 1로 생존</color> (최대 1회)\n- 샘터에서 휴식 시 재충전\n- 즉사 등 일부 피해 제외
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990403].statText
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, upon taking <color=#fe4b48>Damage</color> that would result in death, <color=#00ff9c>survive with 1 HP</color> (once)\n- Rest at the Fount to recharge\n- Excluding certain damages such as Instant Death
   PL: W Symbolicznym, gdy otrzymasz <color=#fe4b48>Obrażenia</color> grożące śmiercią, <color=#00ff9c>przeżywasz z 1 HP</color> (raz)\n- Odpoczynek przy Źródle ładuje ponownie\n- Nie dotyczy części obrażeń, np. natychmiastowej śmierci
78. [RPG [I990403] — opis] 세계는 변하면 안 된다. 세계는 그렇게 그 자리에 있어줘야 한다. 영원히.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990403].description
   limit: do 120 znaków
   EN: The world must not change. It must remain exactly where it is. Forever.
   PL: Świat nie może się zmieniać. Świat musi pozostać dokładnie tam, gdzie jest. Na zawsze.
79. [RPG [I990404] — nazwa wyświetlana] 르루주 발레 플랫
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990404].displayName
   limit: do 40 znaków
   EN: Le Rouge Ballet Flats
   PL: Balerinki Le Rouge
80. [RPG [I990404] — statystyki przedmiotu] 상징계에서 적 처치 시 5초 동안 <color=#F8C200>이동 속도</color> +30%\n\n상징계 <color=#00ff9c>체력</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990404].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, <color=#F8C200>Movement Speed</color> +30% upon killing an enemy\n\nSymbolic <color=#00ff9c>HP</color> +3
   PL: W Symbolicznym po zabiciu wroga przez 5 sekund <color=#F8C200>Szybkość Ruchu</color> +30%\n\nSymboliczne <color=#00ff9c>HP</color> +3
81. [RPG [I990404] — opis] 여러 옷이 있지만 그중 가장 중요한 옷은 신발이야. 신발은 가장 첫 번째로 세상과 맞닿는 옷이니까.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990404].description
   limit: do 140 znaków
   EN: Many kinds of clothing exist, but shoes matter most. They are the first garments that touch the world.
   PL: Ubrań jest wiele, ale najważniejsze z nich to buty. Bo to buty jako pierwsze stykają się ze światem.
82. [RPG [I990405] — nazwa wyświetlana] 르루주 첼시 부츠
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990405].displayName
   limit: do 40 znaków
   EN: Le Rouge Chelsea Boots
   PL: Buty Chelsea Le Rouge
83. [RPG [I990405] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Avant</color> 해금\n- 마지막 공격 뒤 공격 버튼을 한 번 더 누르면 <color=#F8C200>Avant</color> 발동\n- Avant 발동 시 전방을 넓게 쓸어 공격하고 맞은 적을 <color=#F8C200>넉백</color>시킴\n- <color=#F8C200>Garde</color> 중 발동 시 Garde 단계에 비례해 <color=#F8C200>공격 범위</color>와 <color=#F8C200>넉백 거리</color> 증가
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990405].statText
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: Unlocks <color=#F8C200>Avant</color> in the Symbolic\n- Avant: Press the Attack button once more after the last Attack to activate <color=#F8C200>Avant</color>\n- Upon activating Avant, performs a wide front sweep to <color=#F8C200>Knockback</color> enemies hit\n- When activated during <color=#F8C200>Garde</color>, <color=#F8C200>Attack Range</color> and <color=#F8C200>Knockback Distance</color> increase based on Garde level
   PL: Odblokowuje <color=#F8C200>Avant</color> w Symbolicznym\n- Avant: naciśnij przycisk ataku jeszcze raz po ostatnim ataku, aby uruchomić <color=#F8C200>Avant</color>\n- Uruchomienie Avant wykonuje szerokie cięcie z przodu i <color=#F8C200>Odrzuca</color> trafionych wrogów\n- Uruchomione podczas <color=#F8C200>Garde</color> zwiększa <color=#F8C200>Zasięg Ataku</color> i <color=#F8C200>Zasięg Odrzutu</color> proporcjonalnie do poziomu Garde
84. [RPG [I990405] — opis] 신발은 숨을 쉬어야 해. 르누아르의 신발처럼 마냥 닫혀있기만 하면 안 된다고. 신발이 유연해서 숨을 쉴 수 있어줘야 내가 이 땅에 서 있을 수 있는 거지. 그러지 않고서는 그저 분리된 채 얹어질 뿐이라고.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990405].description
   limit: do 320 znaków
   EN: Shoes need to breathe. The Noirs have it wrong—footwear shouldn't be sealed shut. They need to stay supple and let the feet breathe. Only then can you truly stand upon the earth. Otherwise, you're merely laid upon it, cut off from the ground below.
   PL: Buty muszą oddychać. Nie mogą być zasyfione jak buty Le Noir. Muszą pozostać elastyczne i pozwalać stopom oddychać. Dopiero wtedy naprawdę stoisz na ziemi. Inaczej zostajesz na niej tylko odłożony, odcięty od tego, co pod spodem.
85. [RPG [I990406] — nazwa wyświetlana] 리클라이너
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990406].displayName
   limit: do 40 znaków
   EN: Recliner
   PL: Fotel
86. [RPG [I990406] — statystyki przedmiotu] 상징계에서 <color=#fe4b48>피해</color>를 받지 않은 시점부터 15초마다 상징계 <color=#00ff9c>체력</color> 1 <color=#00ff9c>회복</color> (최대 4)\n- 샘터에서 휴식 시 재충전
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990406].statText
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#00ff9c>, \n
   EN: <color=#00ff9c>Heals</color> 1 Symbolic <color=#00ff9c>HP</color> every 15 seconds since last taking <color=#fe4b48>Damage</color> (max 4)\n- Rest at the Fount to recharge
   PL: <color=#00ff9c>Leczy</color> 1 Symboliczne <color=#00ff9c>HP</color> co 15 sekund od ostatniego otrzymania <color=#fe4b48>Obrażeń</color> (maks. 4)\n- Odpoczynek przy Źródle ładuje ponownie
87. [RPG [I990406] — opis] 가구는 의식주 중 어디에 속한다고 생각해? 안에서 거주하는 것일까? 아니면 옷처럼 입는 것일까?\n둘 다 아니야. 가구는 옷과 집을 이어주는 다리인 거지.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990406].description
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Food, clothing, shelter. Where does furniture belong? Is it something we dwell in, or something we wear like clothing?\nOh, neither. Furniture is the bridge between clothing and shelter.
   PL: Meble — do którego z trzech należą? Do tego, w czym się mieszka? A może do tego, co się nosi jak ubranie?\nAni jedno, ani drugie. Meble są mostem łączącym ubranie i mieszkanie.
88. [RPG [I990407] — nazwa wyświetlana] 매트리스
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990407].displayName
   limit: do 40 znaków
   EN: Mattress
   PL: Materac
89. [RPG [I990407] — statystyki przedmiotu] 상징계에서 이동하지 않는 동안 피격 시 받는 <color=#fe4b48>피해량</color> -1 (받는 피해량 최소 1)\n\n상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990407].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, <color=#fe4b48>Damage</color> Taken -1 when hit while standing still (min 1)\n\nSymbolic <color=#00ff9c>HP</color> +2
   PL: W Symbolicznym przy trafieniu w bezruchu otrzymywane <color=#fe4b48>Obrażenia</color> -1 (minimalnie 1)\n\nSymboliczne <color=#00ff9c>HP</color> +2
90. [RPG [I990407] — opis] 시지프 백화점에서 생각을 멈추고 싶었던 고객들과 점원들은 가구가 되었다. 어느 날부터 균열은 더 커져갔고 그 틈에서 강렬한 햇살이 새어 들어 속삭일 때, 가구들은 강제로 깨어나 움직여야만 했다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990407].description
   limit: do 330 znaków
   EN: Customers and employees who wished to stop thinking became furnishings in Grand Magasin Sisyphe. Then the cracks began to widen, and when the fierce sunlight spilled through and whispered to them, the furnishings were torn from sleep and forced to move.
   PL: Klienci i pracownicy Grand Magasin Sisyphe, którzy zapragnęli przestać myśleć, stali się meblami. Pewnego dnia pęknięcia zaczęły rosnąć, a przez ich szczeliny zaczęło sączyć się intensywne światło, które do nich szeptało — meble musiały się wybudzić i zacząć się ruszać.
91. [RPG [I990408] — nazwa wyświetlana] 원목 테이블
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990408].displayName
   limit: do 40 znaków
   EN: Solid Wood Table
   PL: Stół z Litego Drewna
92. [RPG [I990408] — statystyki przedmiotu] 상징계 공격 적중 시 15% 확률로 <color=#F8C200>추가 공격</color> 발동 (경직 0.2초)\n- 맞은 적 기준 십자 5칸에 3만큼 <color=#fe4b48>피해</color> 입힘\n- 주위 1칸에 뫼르소를 감지한 적 1명당 발동 확률 +10%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990408].statText
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, 15% chance to trigger an <color=#F8C200>Extra Attack</color> upon landing an attack (0.2 seconds Hitstun)\n- Deals 3 <color=#fe4b48>Damage</color> to the 5 tiles in a cross centered on the enemy hit\n- Trigger Chance +10% for each enemy within 1 tile that has detected Meursault
   PL: W Symbolicznym 15% szans na uruchomienie <color=#F8C200>Dodatkowego Ataku</color> po trafieniu atakiem (0.2 s Hitstun)\n- Zadaje 3 <color=#fe4b48>Obrażenia</color> na 5 polach w krzyżu wyśrodkowanych na trafionym wrogu\n- Szansa uruchomienia +10% za każdego wroga w promieniu 1 pola, który wykrył Meursaulta
93. [RPG [I990408] — opis] 왜 의자에 앉아 테이블 위에 음식을 두고 먹냐고 르루주 나부랭이가 묻더군. 바닥에서 먹지 않고 굳이 이런 절차를 거치는 건, 당연히 더 맛있게 먹기 위해서지. 인내하며 힘들게 얻은 것일수록 달며 가치가 있으니까. 그러니 더 불편한 테이블과 의자에서 먹을수록 문명화되었다고 할 수 있지 않겠어?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990408].description
   limit: do 440 znaków
   EN: A Rouge wretch once asked why we sit at a table to eat. Why go to such trouble instead of eating off the floor? Well, the ceremony makes food taste better. What is won through hardship and patience is sweeter, and therefore more valuable. By that logic, the more uncomfortable the table and chair, the more civilized the diner. Wouldn't you agree?
   PL: Któryś z Le Rouge zapytał mnie kiedyś, czemu siedzimy przy stole, żeby jeść. Czemu przechodzimy przez taki ceremoniał zamiast jeść z podłogi? Bo ceremonia sprawia, że jedzenie smakuje lepiej. To, co zdobyte cierpliwością i trudem, jest słodsze — a więc cenniejsze. Skoro tak, im niewygodniejsze stół i krzesło, tym bardziej ucywilizowany biesiadnik. Nieprawdaż?
94. [RPG [I990409] — nazwa wyświetlana] 혓바닥
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990409].displayName
   limit: do 40 znaków
   EN: Tongue
   PL: Język
95. [RPG [I990409] — opis] 행복한 옷장이 맛을 느끼도록 해주던 기관
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990409].description
   limit: do 120 znaków
   EN: The organ that once allowed the Happy Closet to taste.
   PL: Narząd, który kiedyś pozwalał Szczęśliwej Szafie smakować.
96. [RPG [I990410] — nazwa wyświetlana] 뼈 다발
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990410].displayName
   limit: do 40 znaków
   EN: Bundle of Bones
   PL: Wiązka Kości
97. [RPG [I990410] — opis] 행복한 옷장이 스스로를 지탱하도록 해주던 뼈들
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990410].description
   limit: do 120 znaków
   EN: The bones that once allowed the Happy Closet to support itself.
   PL: Kości, które kiedyś pozwalały Szczęśliwej Szafie utrzymać się na nogach.
98. [RPG [I990411] — nazwa wyświetlana] 정강이
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990411].displayName
   limit: do 40 znaków
   EN: Shank
   PL: Goleń
99. [RPG [I990411] — opis] 행복한 옷장이 걸음을 옮기도록 도와주던 물건
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990411].description
   limit: do 120 znaków
   EN: The object that once allowed the Happy Closet to walk.
   PL: Przedmiot, który kiedyś pomagał Szczęśliwej Szafie stawiać kroki.
100. [RPG [I990412] — nazwa wyświetlana] 뒤엉킨 창자
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990412].displayName
   limit: do 40 znaków
   EN: Tangled Entrails
   PL: Splecione Trzewia
101. [RPG [I990412] — opis] 행복한 옷장이 음식을 소화시키도록 해주었던 장기
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990412].description
   limit: do 120 znaków
   EN: The organ that once allowed the Happy Closet to digest food.
   PL: Narząd, który kiedyś pozwalał Szczęśliwej Szafie trawić jedzenie.
102. [RPG [I990413] — nazwa wyświetlana] 눈 한 알
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990413].displayName
   limit: do 40 znaków
   EN: An Eyeball
   PL: Gałka Oczowa
103. [RPG [I990413] — opis] 행복한 옷장이 세상의 아름다움을 볼 수 있게 해주었던 기관
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990413].description
   limit: do 120 znaków
   EN: The organ that once allowed the Happy Closet to behold the beauty of the world.
   PL: Narząd, który kiedyś pozwalał Szczęśliwej Szafie oglądać piękno świata.
104. [RPG [I990414] — nazwa wyświetlana] 눈 두 알
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990414].displayName
   limit: do 40 znaków
   EN: Two Eyeballs
   PL: Dwie Gałki Oczowe
105. [RPG [I990414] — opis] 행복한 옷장이 세상의 추악함을 볼 수 있게 해주었던 기관
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990414].description
   limit: do 120 znaków
   EN: The organs that once allowed the Happy Closet to behold the ugliness of the world.
   PL: Narządy, które kiedyś pozwalały Szczęśliwej Szafie oglądać brzydotę świata.
106. [RPG [I990415] — nazwa wyświetlana] 얼굴 피부
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990415].displayName
   limit: do 40 znaków
   EN: Facial Skin
   PL: Skóra Twarzy
107. [RPG [I990415] — opis] 행복한 옷장이 제 감정을 표정으로 드러내도록 해주었던 것
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990415].description
   limit: do 120 znaków
   EN: That which once allowed the Happy Closet to reveal its feelings through expression.
   PL: To, co kiedyś pozwalało Szczęśliwej Szafie wyrażać uczucia przez mimikę.
108. [RPG [I990416] — nazwa wyświetlana] 핏줄 그물
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990416].displayName
   limit: do 40 znaków
   EN: Blood Vessel Mesh
   PL: Siatka Naczyń Krwionośnych
109. [RPG [I990416] — opis] 행복한 옷장의 기관과 뼈와 물건과 장기들이 서로 맞물려 작동하도록 도와주던 장치
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990416].description
   limit: do 150 znaków
   EN: The mechanism that once allowed the Happy Closet's organs, bones, items, and entrails to come and function together.
   PL: Mechanizm, który kiedyś pomagał narządom, kościom, przedmiotom i trzewiom Szczęśliwej Szafy współpracować ze sobą.
110. [RPG [I990801] — nazwa wyświetlana] 탄산 음료
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990801].displayName
   limit: do 40 znaków
   EN: Soda Pop
   PL: Gazowany Napój
111. [RPG [I990801] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color>이 5 이하가 되면 상징계 <color=#00ff9c>체력</color> 5 <color=#00ff9c>회복</color> (최대 1회)\n- 샘터에서 휴식 시 재충전
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990801].statText
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: If Symbolic <color=#00ff9c>HP</color> drops to 5 or lower, <color=#00ff9c>heals</color> 5 Symbolic <color=#00ff9c>HP</color> (once)\n- Rest at the Fount to recharge
   PL: Gdy Symboliczne <color=#00ff9c>HP</color> spadnie do 5 lub niżej, <color=#00ff9c>leczy</color> 5 Symbolicznych <color=#00ff9c>HP</color> (raz)\n- Odpoczynek przy Źródle ładuje ponownie
112. [RPG [I990801] — opis] 명품관에서 습격이 발생했다! 르누아르가 차지하고 있던 명품관을 르루주가 급습하여 잔치를 벌이고 있다!
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990801].description
   limit: do 150 znaków
   EN: The Luxury Hall is under attack! The Rouges have stormed the Hall held by the Noirs and have now begun a feast!
   PL: Salon Prestiżu został zaatakowany! Le Rouge szturmem wzięły Salon okupowany przez Le Noir i urządza ucztę!
113. [RPG [I990802] — nazwa wyświetlana] 빨대
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990802].displayName
   limit: do 40 znaków
   EN: Straw
   PL: Słomka
114. [RPG [I990802] — statystyki przedmiotu] 상징계 공격 적중 시 10% 확률로 상징계 <color=#00ff9c>체력</color> 1 <color=#00ff9c>회복</color>\n\n상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990802].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: In the Symbolic, 10% chance to <color=#00ff9c>heal</color> 1 Symbolic <color=#00ff9c>HP</color> upon landing an attack\n\nSymbolic <color=#00ff9c>HP</color> +2
   PL: W Symbolicznym 10% szans na <color=#00ff9c>uleczenie</color> 1 Symbolicznego <color=#00ff9c>HP</color> po trafieniu atakiem\n\nSymboliczne <color=#00ff9c>HP</color> +2
115. [RPG [I990802] — opis] 섭취하기 위해서는 여기에서 저기로 가는 통로가 필요하다. 섭취는 대상으로부터 나에게 무언가를 끌어오는 것이고 그렇기에 쾌감이 따라온다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990802].description
   limit: do 190 znaków
   EN: Consumption requires a passage from there to here. To consume is to draw something out of another and into oneself. That is why pleasure follows.
   PL: Spożycie wymaga przejścia stamtąd tutaj. Spożywać to znaczy wyciągać coś z celu do siebie — i dlatego płynie za tym przyjemność.
116. [RPG [I990803] — nazwa wyświetlana] 거예요
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990803].displayName
   limit: do 40 znaków
   EN: "You Hear?"
   PL: Wiesz?!
117. [RPG [I990803] — statystyki przedmiotu] 상징계 공격 적중 시 30% 확률로 <color=#F8C200>추가 공격</color> 발동\n- 맞은 적 주위 4칸 이내의 무작위 적 1명에게 3만큼 <color=#fe4b48>피해</color> 입힘
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990803].statText
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, 30% chance to trigger an <color=#F8C200>Extra Attack</color> upon landing an attack\n- Deals 3 <color=#fe4b48>Damage</color> to 1 random enemy within 4 tiles of the enemy hit
   PL: W Symbolicznym 30% szans na uruchomienie <color=#F8C200>Dodatkowego Ataku</color> po trafieniu atakiem\n- Zadaje 3 <color=#fe4b48>Obrażenia</color> 1 losowemu wrogowi w promieniu 4 pól od trafionego wroga
118. [RPG [I990803] — opis] 푸드코트에서 만들어지는 것은 맛있는 요리이지만 그건 식사가 아니게 된다. 요리의 문제가 아닌 어디에서 먹냐는 구조의 문제이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990803].description
   limit: do 240 znaków
   EN: What the Food Court produces may be a scrumptious dish, yet it ceases to be a meal. The fault lies not with the cooking, but with where it is eaten. It is a conundrum of the structure.
   PL: To, co produkuje Strefa Gastronomiczna, może być pyszną potrawą, ale przestaje być posiłkiem. Wina nie leży w gotowaniu, lecz w tym, gdzie się je. To zagadka samej struktury.
119. [RPG [I990804] — nazwa wyświetlana] 접이식 우산
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990804].displayName
   limit: do 40 znaków
   EN: Folding Umbrella
   PL: Zwijany Parasol
120. [RPG [I990804] — statystyki przedmiotu] 상징계에서 제거 가능한 투사체에 공격 적중 시 해당 <color=#F8C200>투사체 제거</color>\n\n상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990804].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, upon landing an attack on a destructible projectile, <color=#F8C200>destroys the projectile</color>\n\nSymbolic <color=#00ff9c>HP</color> +2
   PL: W Symbolicznym trafienie atakiem w zniszczalny pocisk <color=#F8C200>usuwa pocisk</color>\n\nSymboliczne <color=#00ff9c>HP</color> +2
121. [RPG [I990804] — opis] 르카키의 주력 상품. 패션을 만들어내기 힘겨워하는 르카키에게 우산은 몇 안 되는 창작물이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990804].description
   limit: do 170 znaków
   EN: Le Kaki's flagship product. For a brand struggling to create fashion, the umbrella is no more than one of its few true creations.
   PL: Flagowy produkt Le Kaki. Dla brandy z trudem tworzącej modę parasol jest jednym z nielicznych prawdziwych stworzeń.
122. [RPG [I990805] — nazwa wyświetlana] 티슈 한 장
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990805].displayName
   limit: do 40 znaków
   EN: A Piece of Tissue Paper
   PL: Chusteczka
123. [RPG [I990805] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990805].statText
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [RPG [I990805] — opis] 얇은 티슈 한 장으로 무엇을 할 수 있을지 모르겠지만 어딘가엔 티슈 한 장만으로도 샘터 뒤처리를 할 수 있는 자가 있다고 한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990805].description
   limit: do 240 znaków
   EN: It is hard to imagine what one could accomplish with a single piece of tissue paper. Somewhere, however, someone is said to be able to finish their business in the restroom with just one.
   PL: Trudno wyobrazić sobie, co można zrobić z jedną cienką chusteczką. Podobno gdzieś na świecie ktoś potrafi załatwić swoje sprawy w toalecie zaledwie jedną.
125. [RPG [I990806] — nazwa wyświetlana] 단추
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990806].displayName
   limit: do 40 znaków
   EN: Button
   PL: Guzik
126. [RPG [I990806] — statystyki przedmiotu] 상징계에서 「거예요」 <color=#F8C200>추가 공격</color> 발동 시 투사체 +1\n\n그림자계 전투에서 적 처치 시 처치한 아군의 <color=#00ff9c>체력</color> 15, 정신력 10 <color=#00ff9c>회복</color>
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990806].statText
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, upon triggering "You Hear?" <color=#F8C200>Extra Attack</color>, number of projectile +1\n\nDuring battle in the Shadowed, <color=#00ff9c>heals</color> 15 Symbolic <color=#00ff9c>HP</color> and 10 SP for the ally that killed an enemy
   PL: W Symbolicznym uruchomienie <color=#F8C200>Dodatkowego Ataku</color> „Wiesz?!” daje +1 pocisk\n\nW walce w Zacienionym, gdy sojusznik zabije wroga, <color=#00ff9c>leczy</color> go za 15 Symbolicznych <color=#00ff9c>HP</color> i 10 SP
127. [RPG [I990806] — opis] 이방인들이 절 죽이려고 한다는 거예요. 대화로 해결할 수 있었는데도 죽이려고 한다는 거예요!
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990806].description
   limit: do 160 znaków
   EN: The strangers are trying to kill me, you hear?! We could've settled this by talking, but they want me dead, you hear?!
   PL: Ci cudzoziemcy próbują mnie zabić, wiesz?! Można było to załatwić rozmową, a oni chcą mnie zabić, wiesz?!
128. [RPG [I990901] — nazwa wyświetlana] 바늘겨레
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990901].displayName
   limit: do 40 znaków
   EN: Pincushion
   PL: Poduszka na Szpilki
129. [RPG [I990901] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990901].statText
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [RPG [I990901] — opis] 봉제를 하기 위해서는 바늘이 필요해. 그리고 바늘은 못과 다를 게 없어. 봉제는 고정시키기 위한 것이고, 바늘은 그걸 위해 쓰이는 건데, 못도 같은 역할을 하니까.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990901].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To sew, we need a needle.\nAnd what are needles but another name for nails? Sewing is a form of affixation, and that's what needles are used for... Just like nails.
   PL: Żeby szyć, potrzebna jest igła.\nA igły to w gruncie rzeczy inne imię gwóździ. Szycie jest formą mocowania — i do tego służą igły. Zupełnie jak gwóździe.
131. [RPG [I990902] — nazwa wyświetlana] 바늘이 못
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990902].displayName
   limit: do 40 znaków
   EN: Needlekin's Nail
   PL: Gwóźdź Iglika
132. [RPG [I990902] — statystyki przedmiotu] 상징계 공격의 경직 시간 +0.2초\n\n상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990902].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: Hitstun +0.2 seconds for Attacks in the Symbolic\n\nSymbolic <color=#00ff9c>HP</color> +1
   PL: Hitstun +0.2 s dla ataków w Symbolicznym\n\nSymboliczne <color=#00ff9c>HP</color> +1
133. [RPG [I990902] — opis] 바늘이들이 섬기는 왕이 있다. 왕은 미식을 원하며 끊임없이 찌르기를 원한다. 찔러봄으로써 대상의 탄성과 괴성을 통해 그 가치를 짐작해볼 수 있기 때문이다. 바늘이들은 왕을 따라 찌르고 거기에서 새어나오는 즙을 조용히 핥아먹는다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990902].description
   limit: do 360 znaków
   EN: Needlekins serve a king. The king is a gourmet, and he demands that his subjects stab endlessly. Stabbing is a barometer that measures worth through the delicacy's moans of delight and screeches of pain. Needlekins stab as their king commands, and quietly lap up the secretions.
   PL: Iglikowie służą królowi. Król jest smakoszem i nieustannie żąda pchnięć. Pchnięcie pozwala ocenić wartość delikwenta po jego jękach zachwytu i wrzaskach bólu. Iglikowie pchają zgodnie z rozkazem króla i cicho wyliżują wyciekające soki.
134. [RPG [I990904] — nazwa wyświetlana] 혀클리너
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990904].displayName
   limit: do 40 znaków
   EN: Tongue Scraper
   PL: Skrobak do Języka
135. [RPG [I990904] — statystyki przedmiotu] 상징계에서 적 처치 시 다음 공격의 <color=#fe4b48>피해량</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990904].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: In the Symbolic, upon killing an enemy, <color=#fe4b48>Damage</color> Dealt +2 on the next attack
   PL: W Symbolicznym po zabiciu wroga <color=#fe4b48>Obrażenia</color> zadawane +2 przy następnym ataku
136. [RPG [I990904] — opis] 옷을 입기 전에 먼저 씻어야지. 제대로 씻으려면 이렇게 박박 긁어내야 해.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990904].description
   limit: do 150 znaków
   EN: Gotta clean myself before getting dressed. Don't be scared to be a little rough—you gotta scrub the crevices <i>hard</i>.
   PL: Zanim się ubierzesz, najpierw się umyj. A żeby się porządnie umyć, trzeba tak wyskrobać jak należy.
137. [RPG [I990905] — nazwa wyświetlana] 네이키드의 골무
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990905].displayName
   limit: do 40 znaków
   EN: Naked's Thimble
   PL: Naparstek Nakeda
138. [RPG [I990905] — statystyki przedmiotu] 상징계에서 피격 시 받는 <color=#fe4b48>피해량</color> -2 (쿨타임 10초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990905].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: In the Symbolic, <color=#fe4b48>Damage</color> Taken -2 when hit (10 seconds cooldown)
   PL: W Symbolicznym przy trafieniu otrzymywane <color=#fe4b48>Obrażenia</color> -2 (odnowienie 10 s)
139. [RPG [I990905] — opis] 이 멍청한 바늘들은 미쳐버린 게 분명해. 마음에 안 든다 싶으면 뭐든 찌르고 보거든. 찌르고, 또 찌르고, 그러다 무언가 나오면 맛을 보고. 골무가 있어서 다행이지. 골무도 없이 여길 돌아다녔다간, 제법 곤란했을 테니.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990905].description
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: These stupid needles must all be insane. Stab stab stab—that's all they know. They see something they don't like? <i>Stab!</i> That's what they do. And when something oozes out, they lick it up.\nGlad I've got a thimble with me... I would've been in quite a pickle had I been caught down here without it.
   PL: Te głupie igły na pewno oszalały. Coś im się nie podoba? Kłują. Kłują i kłują, a jak coś wypłynie, to degustują. Na szczęście mam naparstek. Gdybym kręcił się tu bez niego, byłoby niezła Kitka.
140. [RPG [I990906] — nazwa wyświetlana] 팔레트
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990906].displayName
   limit: do 40 znaków
   EN: Palette
   PL: Paleta
141. [RPG [I990906] — statystyki przedmiotu] 상징계에서 피격 시 뫼르소 주위 1칸에 <color=#F8C200>붉은 염색 타일</color> 생성\n- 타일 위의 적에게 2초마다 1만큼 <color=#fe4b48>피해</color> 입힘
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990906].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: When hit in the Symbolic, creates <color=#F8C200>Red-Dyed Tiles</color> within 1 tile of Meursault.\n- Enemies standing on these tiles take 1 <color=#fe4b48>Damage</color> every 2 seconds
   PL: W Symbolicznym przy trafieniu tworzy <color=#F8C200>Czerwone Barwione Kafelki</color> w promieniu 1 pola od Meursaulta.\n- Wrogowie stojący na tych kafelkach otrzymują 1 <color=#fe4b48>Obrażenie</color> co 2 sekundy
142. [RPG [I990906] — opis] 여러 가지의 염료가 올려져 있는 판이다. 이 판 위에서 기본 염료들을 섞어 원하는 색을 만든다. 원하는 것을 만들기 위해서는 적절한 양의 배합과 속도가 중요하다. 그렇게 뒤섞인 고름의 냄새는 알록달록하다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990906].description
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A board on which dyes of many kinds are placed.\n\nBasic colors are mixed upon it to create the desired shade. The right proportions and speed are essential to make what is wanted.\n\nThe smell of all that mingled pus is quite colorful.
   PL: Deska, na której leżą barwniki różnych rodzajów.\n\nNa niej miesza się barwniki bazowe, by uzyskać pożądany odcień. Odpowiednia proporcja i tempo są niezbędne, by stworzyć to, czego się pragnie.\n\nZapach zmieszanej ropy jest barwny.
143. [RPG [I990907] — nazwa wyświetlana] 긴 붓
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990907].displayName
   limit: do 40 znaków
   EN: Long Brush
   PL: Długi Pędzel
144. [RPG [I990907] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Garde</color> 적중 시 맞은 적 뒤 1칸까지 공격이 이어짐
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990907].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, landing <color=#F8C200>Garde</color> on an enemy extends the attack 1 tile behind the enemy hit
   PL: W Symbolicznym trafienie <color=#F8C200>Garde</color> przedłuża atak o 1 pole za trafionym wrogiem
145. [RPG [I990907] — opis] 눈물을 섞기 위해선 긴 붓이 필요하다. 붓이 짧으면 눈물이 팔에 빠지고 그대로 빨려 들어가기도 한다. 눈물에 잠기게 되면 색이 빠지기 전까진 하염없이 울게 된다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990907].description
   limit: do 290 znaków
   EN: A long brush is needed to mix tears. Use a brush too short, and the arms might sink into them and be sucked under. One must be wary that they are not submerged in tears, for they will cry and cry until the colors leach out.
   PL: Do mieszania łez potrzebny jest długi pędzel. Krótki pędzel sprawi, że łzy zaleją ramiona, które zostaną wciągnięte pod powierzchnię. Zanurzony w łzach będzie płakał bez końca, dopóki nie straci koloru.
146. [RPG [I990908] — nazwa wyświetlana] 큰 붓
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990908].displayName
   limit: do 40 znaków
   EN: Large Brush
   PL: Duży Pędzel
147. [RPG [I990908] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Garde</color> 해금\n- 일정 시간 동안 공격 버튼을 누른 후 떼면 피해량이 높은 <color=#F8C200>Garde</color>로 발동\n- Garde 충전 시간: 2초\n- Garde 피해량: 상징계 공격의 <color=#fe4b48>피해량</color> +1\n- Garde 중 <color=#F8C200>이동 속도</color> 50%로 감소
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990908].statText
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: Unlocks <color=#F8C200>Garde</color> in the Symbolic\n- Hold the Attack button for a set duration, then release to perform a high-damage <color=#F8C200>Garde</color>\n- Garde Charge Time: 2 seconds\n- Garde Damage: Attack <color=#fe4b48>Damage</color> +1 in the Symbolic\n- <color=#F8C200>Movement Speed</color> is reduced to 50% during Garde
   PL: Odblokowuje <color=#F8C200>Garde</color> w Symbolicznym\n- Przytrzymaj przycisk ataku przez określony czas, a po zwolnieniu wykonasz wysokobrażeniowy <color=#F8C200>Garde</color>\n- Czas ładowania Garde: 2 s\n- Obrażenia Garde: <color=#fe4b48>Obrażenia</color> ataku +1 w Symbolicznym\n- Podczas Garde <color=#F8C200>Szybkość Ruchu</color> spada do 50%
148. [RPG [I990908] — opis] 여러 색의 눈물을 칠하기 위해서는 큰 붓이 필요하다. 붓이 충분히 크지 않으면 붓질을 여러 번 해야 한다. 하지만 붓질은 최소한으로 끝내는 게 좋다. 붓질을 할 때마다 눈물이 튀어 그 냄새가 몸에 배기 때문에 또 눈물을 쏟게 되니까. 울지도 아픔도 느끼지 못하게 된 누군가를 위해 나는 아직도 계속해서 붓질을 하고 있다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990908].description
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One needs a large brush to paint a diverse spectrum of colors. Smaller brushes naturally lend themselves to more brushstrokes, but one must keep the number of strokes to a minimum. Each daub of the brush leaves tear droplets on me, and with them, its scent.\n\nThe scent makes me cry, but I keep painting. I paint for the one who has forgotten tears and pain.
   PL: Do malowania łzami różnych barw potrzebny jest duży pędzel. Małe pędzle wymagają wielu pociągnięć, a pociągnięć trzeba ograniczać do minimum. Każdy pociągnięcie zostawia na mnie kropelki łez — i ich zapach.\n\nZapach każe mi płakać, ale ja nadal maluję. Maluję dla tej, która zapomniała łez i bólu.
149. [RPG [I990909] — nazwa wyświetlana] 티슈 두 장
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990909].displayName
   limit: do 40 znaków
   EN: Two Tissue Papers
   PL: Dwie Chusteczki
150. [RPG [I990909] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990909].statText
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [RPG [I990909] — opis] 이 층에서 티슈가 사용되는 이유는 두 가지다. 뚫리기 위해서, 혹은 눈물을 머금기 위해서. 티슈는 얇아 뚫리기가 쉬우면서도 구멍이 많아 많은 고름을 머금을 수 있기 때문이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990909].description
   limit: do 240 znaków
   EN: Tissue paper serves two purposes on this floor: to be pierced, or to soak up tears. It is thin enough to puncture easily, yet full of enough tiny holes to soak up a great deal of pus.
   PL: Na tym piętrze chusteczki służą dwóm celom: żeby je przetknąć, albo żeby nasączyć je łzami. Chusteczka jest na tyle cienka, że łatwo ją przetknąć, a jednocześnie ma tyle dziurek, że może nasiąknąć mnóstwem ropy.
152. [RPG [I990910] — nazwa wyświetlana] 주스
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990910].displayName
   limit: do 40 znaków
   EN: Juice
   PL: Sok
153. [RPG [I990910] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Garde</color> 중 <color=#F8C200>이동 속도</color> 감소량을 25%로 변경\n\n상징계 <color=#00ff9c>체력</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990910].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, changes the <color=#F8C200>Movement Speed</color> reduction during <color=#F8C200>Garde</color> to 25%\n\nSymbolic <color=#00ff9c>HP</color> +1
   PL: W Symbolicznym zmienia redukcję <color=#F8C200>Szybkości Ruchu</color> podczas <color=#F8C200>Garde</color> na 25%\n\nSymboliczne <color=#00ff9c>HP</color> +1
154. [RPG [I990910] — opis] 찌르면 나오는 것은 전부 주스다. 마시면 된다. 차오른 눈물을 찔러 터뜨려 마시는 것이다. 아니면 누군가를 찔러 고름 같은 눈물을 흘리게 할 수도. 맛은 슬픔의 맛을 따라간다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990910].description
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Anything that comes out when pierced is juice. Drink it. Poke and pop the bubble of tears and drink what bursts forth. Or pierce someone else and make them weep pus.\nThe flavor follows the taste of sorrow.
   PL: Wszystko, co wypływa przy pchnięciu, to sok. Wystarczy pić. Nakłuwa i wybuchający balon łez pije się tym samym. Można też nakłuć kogoś innego i zmusić go do łez podobnych do ropy.\nSmak podąża za smutkiem.
155. [RPG [I990911] — nazwa wyświetlana] 바느질의 왕의 칫솔
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990911].displayName
   limit: do 60 znaków
   EN: Toothbrush of the King of Needleworks
   PL: Szczoteczka do Zębów Króla Szycia
156. [RPG [I990911] — statystyki przedmiotu] 상징계에서 뫼르소를 추격 중인 적에게 1초마다 <color=#F8C200>추가 공격</color> 발동\n- 5칸 이내의 추격 중인 적 중 무작위 1명에게 2만큼 <color=#fe4b48>피해</color> 입힘\n- 순찰·도주 중인 적 제외\n- <color=#F8C200>달리기</color> 중에는 발동하지 않음
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990911].statText
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, triggers an <color=#F8C200>Extra Attack</color> every 1 second against enemies pursuing Meursault\n- Deals 2 <color=#fe4b48>Damage</color> to 1 random pursuing enemy within 5 tiles\n- Does not target enemies that are patrolling or fleeing\n- Does not trigger while <color=#F8C200>Sprinting</color>
   PL: W Symbolicznym co 1 sekundę uruchamia <color=#F8C200>Dodatkowy Atak</color> na wrogów ścigających Meursaulta\n- Zadaje 2 <color=#fe4b48>Obrażenia</color> 1 losowemu ścigającemu wrogowi w promieniu 5 pól\n- Nie celuje we wrogów patrolujących ani uciekających\n- Nie uruchamia się podczas <color=#F8C200>Biegu</color>
157. [RPG [I990911] — opis] 칫솔에 가느다란 못들이 촘촘히 박혀 있다. 이 못은 살을 쓸어내며 박힌 것들을 긁고 뚫어내 안에 든 것을 줄줄 새어 나오게 한다. 그리고 왕은 그것을 맛본다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990911].description
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A toothbrush whose head is a forest of spindly nails.\n\nThe nails grate the skin, ripping and breaking through what is embedded. This drains the subdermal fluid.\n\nThen, it is brought to the king for tasting.
   PL: Szczoteczka, której główka jest gajem kruchych gwóździ.\n\nGwoździe ścierają skórę, rozdzierając i przebijając to, co pod nią, aż zawartość wypływa strumieniem.\n\nA potem podawane są królowi do degustacji.
158. [RPG [I992701] — nazwa wyświetlana] 정오의 푸른색
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992701].displayName
   limit: do 40 znaków
   EN: Noonday Blue
   PL: Błękit Południa
159. [RPG [I992701] — opis] 정오에 해가 가장 높이 뜬다. 가장 높이 뜨는 해는 가장 짧은 그림자를 만든다. 그림자가 너무 짧아져서 보이지 않게 되었을 때의 햇빛은 푸른색이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992701].description
   limit: do 200 znaków
   EN: At noon, the sun reaches its highest point. The higher the sun, the shorter the shadow. When the shadow has shrunk beyond sight, the sunlight is blue.
   PL: W południe słońce sięga najwyższego punktu. Im wyższe słońce, tym krótszy cień. Gdy cień kurczy się ponad granicą widoczności, światło słoneczne jest błękitne.
160. [RPG [I992702] — nazwa wyświetlana] 피식자의 사유
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992702].displayName
   limit: do 40 znaków
   EN: Ruminations of the Prey
   PL: Rozmyślania Ofiary
161. [RPG [I992702] — opis] 이 요리를 통해 온전히 먹혀본 적 있는 자의 경험을 겪을 수 있다. 그 맛을 보면 먹혀버렸기 때문에 죽는다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992702].description
   limit: do 170 znaków
   EN: This dish grants the complete experience of being eaten. Tasting it brings death, for the taster has become consumed as prey.
   PL: Ta potrawa pozwala przeżyć pełne doświadczenie bycia zjedzonym. Skosztowanie jej oznacza śmierć, bo degustator stał się skonsumowaną ofiarą.
162. [RPG [I992704] — nazwa wyświetlana] 황금고치
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992704].displayName
   limit: do 40 znaków
   EN: Golden Cocoon
   PL: Złoty Kokon
163. [RPG [I992704] — statystyki przedmiotu] 상징계에서 <color=#F8C200>랜턴</color> 해금\n- 랜턴 버튼(F 키)을 누르면 바라보는 방향을 비추는 <color=#F8C200>랜턴</color>을 켜고 끔
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992704].statText
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: Unlocks <color=#F8C200>Lantern</color> in the Symbolic\n- Press the Lantern button (F on keyboard) to toggle the <color=#F8C200>Lantern</color> that illuminates the direction the character is facing
   PL: Odblokowuje <color=#F8C200>Lampę</color> w Symbolicznym\n- Naciśnij przycisk lampy (F na klawiaturze), aby włączyć lub wyłączyć <color=#F8C200>Lampę</color> oświetlającą kierunek, w którym patrzy postać
164. [RPG [I992704] — opis] 누군가를 부르듯이 고치가 울부짖는다. 지금은 사라진 과거에서부터 아이는 해변까지 떠밀려 왔으며, 푸드코트까지 흘러와 지금 이렇게 요리가 되었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992704].description
   limit: do 210 znaków
   EN: The cocoon cries as if calling out to someone. Carried from a past now gone, the child washed ashore, drifted as far as the Food Court... and has now become a dish.
   PL: Kokon jęczy, jakby kogoś wołał. Prz niesione z przeszłości, która już nie istnieje, dziecko wybiło się na brzeg, przepłynęło aż do Strefy Gastronomicznej... i stało się potrawą.
165. [RPG [I990934] — nazwa wyświetlana] 더러운 앞치마
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990934].displayName
   limit: do 40 znaków
   EN: Dirty Apron
   PL: Brudny Fartuch
166. [RPG [I990934] — statystyki przedmiotu] 상징계에서 적 체력 바가 표시되는 체력 상한을 100%로 변경\n- 보유 시 첫 타격부터 체력 바가 표시됨
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990934].statText
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In the Symbolic, changes the HP threshold for displaying enemy HP bars to 100%\n- While owned, enemy HP bars are displayed from the first hit onward
   PL: W Symbolicznym zmienia próg HP wyświetlania pasków HP wrogów na 100%\n- Przy posiadaniu pasek HP wroga wyświetla się od pierwszego trafienia
167. [RPG [I990934] — opis] 보이지 않는 것에겐 색을 덮어 윤곽을 잡는다. 그렇게 수많은 것들에게 색을 뿌려 윤곽을 헤아리다 보면 자신의 몸도 얼룩지게 된다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990934].description
   limit: do 220 znaków
   EN: What is invisible must be coated in color until its outline emerges. Splash enough unseen things with color, and one realizes that one's own body has become stained.
   PL: To, co niewidzialne, trzeba pokryć kolorem, aż zarysuje się kontur. Kiedy chlapiesz kolorem na mnóstwo niewidzialnych rzeczy, zauważasz, że twoje własne ciało też się poplamiło.
168. [RPG [I992806] — nazwa wyświetlana] 깊은 바다 염료
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992806].displayName
   limit: do 40 znaków
   EN: Deep-sea Dye
   PL: Barwnik Głębin
169. [RPG [I992806] — opis] 가끔 아주 깊은 곳에서부터 끌어 올려진 채, 부풀어 오르는 눈물이 있다. 지독한 썩은내와 자글거리는 검은 얼룩을 휘젓고 정제하다 보면… 눈물은 더없이 투명한 색을 되찾는다. 깊은 바다의 염료는 그러한 옛 것의 눈물로 만들어진다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992806].description
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is a tear that, once every long while, is dredged up bloated from the deepest depths. After a long, grueling process of stirring through the rancid stench and the smudging black... the tear regains its original clarity.\n\nThe Deep-sea Dye is made from the tears of such olden beings.
   PL: Podobno raz na jakiś czas z najgłębszych głębin wydobywa się rozdęta łza. Po męczącym procesie mieszania przez zgniły smród i plamiącą czerń... łza odzyskuje bezkresną przejrzystość.\n\nBarwnik Głębin powstaje z łez takich dawnych istot.
170. [RPG [I992807] — nazwa wyświetlana] 황금염료
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992807].displayName
   limit: do 40 znaków
   EN: Golden Dye
   PL: Złoty Barwnik
171. [RPG [I992807] — opis] 황금송진에서부터 나온 즙을 고름에 섞는다. 황금의 의미와 가치는 드높아서 어떤 염료라도 황금빛으로 바꾼다. 그 즙을 구하기가 어려울 뿐.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992807].description
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mix the secretion from the Golden Resin with the pus.\n\nEach ounce of the golden is densely saturated with meaning and worth, enough to turn any dye just as aureate. The hard part is getting the secretion.
   PL: Zmieszaj wydzielinę ze Złotej Żywicy z ropą.\n\nKażda kropla złota jest gęsto nasycona znaczeniem i wartością — na tyle, by nadać aureatę każdemu barwnikowi. Trudno tylko zdobyć tę wydzielinę.
172. [RPG [I992808] — nazwa wyświetlana] 황금 실타래
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992808].displayName
   limit: do 40 znaków
   EN: Golden Skein
   PL: Złoty Motek
173. [RPG [I992808] — opis] 실을 운반하기 위해 실을 감는다. 실은 만들어질 때도, 옮겨질 때도 돌고 돌아야 한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I992808].description
   limit: do 130 znaków
   EN: Woven threads wound for transport. Spin, spin, spin... In every step of its life, the thread spins.
   PL: Nici nawinięte na transport. Kręć, kręć, kręć... W każdym etapie swojego życia nić się kręci.
174. [RPG [I993002] — nazwa wyświetlana] 노란 눈물
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I993002].displayName
   limit: do 40 znaków
   EN: Yellow Tears
   PL: Żółte Łzy
175. [RPG [I993002] — opis] 노란 고름과도 같은 눈물이 차오른다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I993002].description
   limit: do 120 znaków
   EN: Tears well like yellow pus.
   PL: Wypełniają się łzy podobne do żółtej ropy.
176. [RPG [I993003] — nazwa wyświetlana] 빨간 눈물
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I993003].displayName
   limit: do 40 znaków
   EN: Red Tears
   PL: Czerwone Łzy
177. [RPG [I993003] — opis] 차오른 붉은 눈물은 고름이 터지듯 터져나온다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I993003].description
   limit: do 120 znaków
   EN: The red, swollen tears burst like a pus-filled abscess.
   PL: Napęczniałe czerwone łzy pękają niczym ropny absces.
178. [RPG [I993004] — nazwa wyświetlana] 파란 눈물
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I993004].displayName
   limit: do 40 znaków
   EN: Blue Tears
   PL: Błękitne Łzy
179. [RPG [I993004] — opis] 푸른 염료는 고름 냄새가 난다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I993004].description
   limit: do 120 znaków
   EN: The blue dye smells of pus.
   PL: Błękitny barwnik pachnie ropą.
180. [RPG [I990925] — nazwa wyświetlana] 나무 톱밥
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990925].displayName
   limit: do 40 znaków
   EN: Sawdust
   PL: Trociny
181. [RPG [I990925] — statystyki przedmiotu] 상징계 공격의 <color=#F8C200>경직</color> 시간 +0.2초
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990925].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: <color=#F8C200>Hitstun</color> +0.2 seconds for Attacks in the Symbolic
   PL: <color=#F8C200>Hitstun</color> +0.2 s dla ataków w Symbolicznym
182. [RPG [I990925] — opis] 어둠 속에서 의미 있는 부스러기를 찾는 것엔 어떤 의미가 있을까. 부스러기에서 의미있는 것을 찾아내는 것인지, 아니면 찾다 보니 의미를 부여하게 되는 것인지.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990925].description
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Why does one stumble in the dark for the crumbs of meaning?\nDoes one find meaning inherent in the crumbs, or does the search itself imbue them with one?
   PL: Czy szukanie w ciemności znaczących okruchów ma jakiś sens? Czy odnajduje się w okruchach coś znaczącego, czy raczej szukanie samo w sobie nadaje im sens?
183. [RPG [I990924] — nazwa wyświetlana] 하늘색 염료
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990924].displayName
   limit: do 40 znaków
   EN: Sky-blue Dye
   PL: Barwnik Błękitu Nieba
184. [RPG [I990924] — statystyki przedmiotu] 그림자계 전투에서 승리 시 상징계 <color=#00ff9c>체력</color>을 최대 체력의 10%만큼 <color=#00ff9c>회복</color>
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990924].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: During battle in the Shadowed:\nAfter winning an Encounter, <color=#00ff9c>heal</color> 10% Symbolic <color=#00ff9c>HP</color>
   PL: W walce w Zacienionym:\nPo wygranej potyczce <color=#00ff9c>leczy</color> 10% Symbolicznych <color=#00ff9c>HP</color>
185. [RPG [I990924] — opis] 시지프 백화점에선 하늘을 볼 수 없을 텐데, 이 염료를 하늘색이라고 부르는 거 웃기지 않아? 진짜 하늘은 시간에 따라, 날씨에 따라, 혹은 마음에 따라 색이 다른데 말이야.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990924].description
   limit: do 340 znaków
   EN: Isn't it funny that the people of the Grand Magasin Sisyphe call this dye "sky-blue" when none of them can see the sky in here? Besides, there's no such thing as "sky-color"—the real sky changes color with the time of day, the weather, or... the observer's heart.
   PL: Nie wydaje ci się śmieszne, że ludzie Grand Magasin Sisyphe nazywają ten barwnik „błękitem nieba”, choć żaden z nich nie widział tu nieba? Poza tym „kolor nieba” nie istnieje — prawdziwe niebo zmienia barwę z porą dnia, pogodą, a czasem... sercem patrzącego.
186. [RPG [I990923] — nazwa wyświetlana] 실
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990923].displayName
   limit: do 40 znaków
   EN: Thread
   PL: Nić
187. [RPG [I990923] — statystyki przedmiotu] 상징계에서 공격 적중 시 5초 동안 대상의 <color=#F8C200>이동 속도</color> 10% 감소, 가하는 <color=#fe4b48>피해량</color> 2 감소 (쿨타임 15초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990923].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, for 5 seconds upon landing an attack:\n- Target's <color=#F8C200>Movement Speed</color> -10%\n- Target's <color=#fe4b48>Damage</color> Dealt -2 \n\n(15 second cooldown)
   PL: W Symbolicznym po trafieniu atakiem przez 5 sekund:\n- <color=#F8C200>Szybkość Ruchu</color> celu -10%\n- zadawane przez cel <color=#fe4b48>Obrażenia</color> -2\n\n(odnowienie 15 s)
188. [RPG [I990923] — opis] 뫼르소를 얇게 뽑아서 꼬아낸 실. 익숙한 색상이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990923].description
   limit: do 120 znaków
   EN: A thread twined from thinly sliced Meursault. Its color is quite familiar.
   PL: Nić skręcona z cienko pokrojonego Meursaulta. Kolor dość znajomy.
189. [RPG [I990922] — nazwa wyświetlana] 파하하
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990922].displayName
   limit: do 40 znaków
   EN: "Bwahahaha!"
   PL: Bwahahaha!
190. [RPG [I990922] — statystyki przedmiotu] 그림자계 전투에서 시지프 소속 적에게 아군이 가하는 <color=#fe4b48>피해량</color> +5%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990922].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, \n
   EN: During battle in the Shadowed:\nAllies deal +5% <color=#fe4b48>damage</color> against Sisyphe enemies
   PL: W walce w Zacienionym:\nSojusznicy zadają +5% <color=#fe4b48>obrażeń</color> wrogom Sisyphe
191. [RPG [I990922] — opis] 시지프 백화점의 벽은 뭐로 되어 있다고 생각해?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990922].description
   limit: do 120 znaków
   EN: What do you think the walls of the Grand Magasin Sisyphe are made of?
   PL: Z czego — jak myślisz — zbudowane są ściany Grand Magasin Sisyphe?
192. [RPG [I990815] — nazwa wyświetlana] 음식 찌꺼기
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990815].displayName
   limit: do 40 znaków
   EN: Food Scraps
   PL: Resztki Jedzenia
193. [RPG [I990815] — statystyki przedmiotu] 그림자계 전투에서 턴 시작 시 <color=#00ff9c>체력</color>이 50% 미만인 아군이 <color=#00ff9c>체력 회복 증가</color> 1을 얻음 (전투당 4회)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990815].statText
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: During battle in the Shadowed:\nTurn Start: Ally that has lower than 50% <color=#00ff9c>HP</color> gains 1 <color=#00ff9c>HP Healing</color> Boost (4 times per Encounter)
   PL: W walce w Zacienionym:\nPoczątek tury: sojusznik z poniżej 50% <color=#00ff9c>HP</color> otrzymuje 1 <color=#00ff9c>Wzmocnienie Leczenia HP</color> (4 razy na potyczkę)
194. [RPG [I990815] — opis] 찌꺼기를 구분하는 경계가 뭔지 아나? 음식을 한 입만 먹고 버려도 그것은 찌꺼기가 되고 누군가는 그 찌꺼기를 희귀한 재료로 여기며 맛있게 먹기도 하지. 그래서 찌꺼기가 무엇으로 구분되느냐가 푸드코트에선 아주 중요한 문제인데… 지금은 르누아르가 아니면 전부 찌꺼기인 상황이지.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990815].description
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you know where food ends and scraps begin?\n\nTake one bite and throw the rest away, and it becomes refuse. But to some, that waste becomes a wonderfully rare ingredient, devoured with delight. What I mean is, what counts as scraps is an incredibly important issue in the Food Court... and right now, anything that isn't Noir is considered scraps.
   PL: Wiesz, gdzie kończy się jedzenie, a zaczynają resztki?\n\nZjesz jeden kęs, a resztę wyrzucisz — i to już jest śmiecice. Ale dla niektórych ten odpad jest cudownie rzadkim składnikiem, pochłanianym z rozkoszą. Chodzi mi o to, że to, co liczy się jako resztki, jest w Strefie Gastronomicznej kwestią szalenie ważną... a obecnie wszystko, co nie jest Le Noir, uważane jest za resztki.
195. [RPG [I990814] — nazwa wyświetlana] 지도 조각
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990814].displayName
   limit: do 40 znaków
   EN: Map Fragment
   PL: Fragment Mapy
196. [RPG [I990814] — statystyki przedmiotu] 그림자계 전투 진입 시 1턴 동안 <color=#F8C200>E.G.O 자원 획득량 +</color> 1을 얻음
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990814].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: Upon entering battle in the Shadowed, gain 1 <color=#F8C200>E.G.O Resource Amp</color> for 1 turn
   PL: Po wejściu do walki w Zacienionym otrzymuje na 1 turę 1 <color=#F8C200>Wzmocnienie Zysku Zasobów E.G.O</color>
197. [RPG [I990814] — opis] 명품관까지 급습할 수 있는 층의 통로가 그려진 지도. 허나 이미 사용되어 알아볼 수 없다. 시지프 시스템은 여러 겹으로 중첩되어 있으며 이러한 다층 구조로 인해 많은 고객들이 잠들어 있다. 다층 구조를 분석할 수 있는 아주 극소수의 인원만이 만든 이 지도는 천문학적인 가치를 지닌다. 르루주는 이것을 손에 넣었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990814].description
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A map outlining a direct inroad into the Luxury Hall, but it is now used and illegible. Sisyphe System is, as a whole, a superposition of layers upon layers, which is precisely what permits it to house an implausible number of customers.\nCreated by the few minds able to analyze the many-tiered structure, this map is of astronomical worth.\n\nAnd it fell into the Rouges' hand.
   PL: Mapa rysująca bezpośrednią drogę wtargnięcia do Salonu Prestiżu, choć jest już zużyta i nieczytelna. System Sisyphe to, w całości, nakładanie się warstw na warstwy — i właśnie ta wielowarstwowa struktura pozwala pomieścić nieprawdopodobną liczbę klientów.\nOpracowana przez garstkę umysłów zdolnych analizować wielopoziomową strukturę, mapa ta ma astronomiczną wartość.\n\nI wpadła w ręce Le Rouge.
198. [RPG [I990320] — nazwa wyświetlana] 황금원단
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990320].displayName
   limit: do 40 znaków
   EN: Golden Fabric
   PL: Złota Tkanina
199. [RPG [I990320] — opis] 가장 가치 있고 의미 있는 소재로 만들어진 옷은, 과연 그 재료만큼 고귀할까.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990320].description
   limit: do 170 znaków
   EN: If a garment is made from the most worthy and meaningful material of all... does that make the garment as exalted as the material?
   PL: Jeśli ubranie uszyto z najcenniejszego i najbardziej znaczącego materiału ze wszystkich... czy czyni to ubranie tak szlachetnym jak materiał?
200. [RPG [I990008] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990008].displayName
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang
201. [RPG [I990008] — statystyki przedmiotu] 상징계 <color=#F8C200>이동 속도</color> +10%\n\n상징계에서 공격 적중 시 5초 동안 대상의 가하는 <color=#fe4b48>피해량</color> 1 감소 (쿨타임 10초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990008].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: <color=#F8C200>Movement Speed</color> +10% in the Symbolic\n\nIn the Symbolic, upon landing an attack, target's <color=#fe4b48>Damage</color> Dealt -1 for 5 seconds (10 seconds cooldown)
   PL: <color=#F8C200>Szybkość Ruchu</color> +10% w Symbolicznym\n\nW Symbolicznym po trafieniu atakiem zadawane przez cel <color=#fe4b48>Obrażenia</color> -1 przez 5 sekund (odnowienie 10 s)
202. [RPG [I990008] — opis] 날개의 상징. 자유로워진다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990008].description
   limit: do 120 znaków
   EN: Symbol of Wings. To become free.
   PL: Symbol Skrzydeł. Staje się wolny.
203. [RPG [I990009] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990009].displayName
   limit: do 40 znaków
   EN: Faust
   PL: Faust
204. [RPG [I990009] — statystyki przedmiotu] 상징계에서 <color=#F8C200>약점 공격</color> 시 <color=#fe4b48>피해량</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990009].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, <color=#F8C200>Weakpoint Attack</color> <color=#fe4b48>Damage</color> Dealt +2
   PL: W Symbolicznym <color=#F8C200>Atak na Słaby Punkt</color> zadaje <color=#fe4b48>Obrażenia</color> +2
205. [RPG [I990009] — opis] 지식의 상징. 영리해진다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990009].description
   limit: do 120 znaków
   EN: Symbol of Knowledge. To become clever.
   PL: Symbol Wiedzy. Staje się bystry.
206. [RPG [I990010] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990010].displayName
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
207. [RPG [I990010] — statystyki przedmiotu] 상징계에서 적 처치 시 상징계 <color=#00ff9c>체력</color>을 최대 체력의 5%만큼 <color=#00ff9c>회복</color> (쿨타임 10초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990010].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>
   EN: In the Symbolic, <color=#00ff9c>heals</color> 5% Symbolic <color=#00ff9c>HP</color> upon killing an enemy (10 seconds cooldown)
   PL: W Symbolicznym <color=#00ff9c>leczy</color> 5% Symbolicznych <color=#00ff9c>HP</color> po zabiciu wroga (odnowienie 10 s)
208. [RPG [I990010] — opis] 행동의 상징. 건강해진다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990010].description
   limit: do 120 znaków
   EN: Symbol of Action. To become vigorous.
   PL: Symbol Czynu. Staje się żywotny.
209. [RPG [I990011] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990011].displayName
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
210. [RPG [I990011] — statystyki przedmiotu] 상징계에서 공격 적중 시 20% 확률로 대상에게 <color=#F8C200>취약 표식</color> 1 부여\n(<color=#F8C200>취약 표식</color>: 받는 <color=#fe4b48>피해량</color> +10%)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990011].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, 20% chance to inflict 1 <color=#F8C200>Fragile Mark</color> upon landing an attack\n(<color=#F8C200>Fragile Mark</color>: <color=#fe4b48>Damage</color> Taken +10%)
   PL: W Symbolicznym 20% szans na nałożenie 1 <color=#F8C200>Znaku Kruchości</color> po trafieniu atakiem\n(<color=#F8C200>Znak Kruchości</color>: otrzymywane <color=#fe4b48>Obrażenia</color> +10%)
211. [RPG [I990011] — opis] 애증의 상징. <s>끊어낸다.</s>엮는다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990011].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: Symbol of Affection and Resentment. To <s>sever</s> twine.
   PL: Symbol Przywiązania i Urazy. <s>Odcina.</s>Splata.
212. [RPG [I990012] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990012].displayName
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu
213. [RPG [I990012] — statystyki przedmiotu] 그림자계 전투에 뫼르소의 공격으로 진입하면 전장의 모든 아군 <color=#F8C200>정신력 5~10 회복</color>
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990012].statText
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: Upon entering battle in the Shadowed via Meursault's Attack, all allies on the field <color=#F8C200>heal 5~10 SP</color>
   PL: Po wejściu do walki w Zacienionym atakiem Meursaulta wszyscy sojusznicy na polu <color=#F8C200>leczy 5~10 SP</color>
214. [RPG [I990012] — opis] 통찰의 상징. 지켜본다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990012].description
   limit: do 120 znaków
   EN: Symbol of Insight. To watch.
   PL: Symbol Wglądu. Przygląda się.
215. [RPG [I990013] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990013].displayName
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
216. [RPG [I990013] — statystyki przedmiotu] 상징계 <color=#F8C200>이동 속도</color> +10%\n\n상징계에서 적 처치 시 20초 동안 공격 <color=#fe4b48>피해량</color> +2 (쿨타임 30초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990013].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: <color=#F8C200>Movement Speed</color> +10% in the Symbolic\n\nIn the Symbolic, Attack <color=#fe4b48>Damage</color> Dealt +2 for 20 seconds upon killing an enemy (30 seconds cooldown)
   PL: <color=#F8C200>Szybkość Ruchu</color> +10% w Symbolicznym\n\nW Symbolicznym po zabiciu wroga <color=#fe4b48>Obrażenia</color> ataku +2 przez 20 sekund (odnowienie 30 s)
217. [RPG [I990013] — opis] 폭풍의 상징. !@#!$ 기억한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990013].description
   limit: do 120 znaków
   EN: Symbol of the Storm. To remember !@#!$.
   PL: Symbol Burzy. Pamięta !@#!$.
218. [RPG [I990014] — nazwa wyświetlana] 이스마엘
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990014].displayName
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael
219. [RPG [I990014] — statystyki przedmiotu] 상징계에서 공격 적중 시 10초 동안 대상의 <color=#F8C200>이동 속도</color> 20% 감소 (쿨타임 13초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990014].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, upon landing an attack, reduce target's <color=#F8C200>Movement Speed</color> by 20% for 10 seconds (13 seconds cooldown)
   PL: W Symbolicznym po trafieniu atakiem <color=#F8C200>Szybkość Ruchu</color> celu -20% przez 10 sekund (odnowienie 13 s)
220. [RPG [I990014] — opis] 모험의 상징. 항해한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990014].description
   limit: do 120 znaków
   EN: Symbol of Adventure. To set sail.
   PL: Symbol Przygody. Żegluje.
221. [RPG [I990015] — nazwa wyświetlana] 로쟈
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990015].displayName
   limit: do 40 znaków
   EN: Rodion
   PL: Rodion
222. [RPG [I990015] — statystyki przedmiotu] 상징계에서 대상의 <color=#00ff9c>체력</color>이 50% 이상이면, 공격 <color=#fe4b48>피해량</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990015].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#fe4b48>
   EN: If target has 50%+ Symbolic <color=#00ff9c>HP</color>, Attack <color=#fe4b48>Damage</color> Dealt +1
   PL: Jeśli cel ma 50% lub więcej Symbolicznych <color=#00ff9c>HP</color>, atak zadaje <color=#fe4b48>Obrażenia</color> +1
223. [RPG [I990015] — opis] 영웅의 상징. 기다린다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990015].description
   limit: do 120 znaków
   EN: Symbol of the Hero. To await.
   PL: Symbol Bohatera. Czeka.
224. [RPG [I990016] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990016].displayName
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair
225. [RPG [I990016] — statystyki przedmiotu] 상징계에서 앞쪽의 적에게 가하는 <color=#fe4b48>피해량</color> +2\n\n상징계에서 뒤쪽의 적에게서 받는 <color=#fe4b48>피해량</color> -2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990016].statText
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, \n
   EN: In the Symbolic:\n- <color=#fe4b48>Damage</color> Dealt +2 against enemies in the front\n- <color=#fe4b48>Damage</color> Taken -2 from enemies behind
   PL: W Symbolicznym:\n- <color=#fe4b48>Obrażenia</color> zadawane +2 wrogom z przodu\n- otrzymywane <color=#fe4b48>Obrażenia</color> -2 od wrogów z tyłu
226. [RPG [I990016] — opis] 각성의 상징. 깨어난다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990016].description
   limit: do 120 znaków
   EN: Symbol of Awakening. To awaken.
   PL: Symbol Przebudzenia. Wybudza się.
227. [RPG [I990017] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990017].displayName
   limit: do 40 znaków
   EN: Outis
   PL: Outis
228. [RPG [I990017] — statystyki przedmiotu] 상징계에서 대상의 <color=#00ff9c>체력</color>이 50% 미만이면, 공격<color=#fe4b48>피해량</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990017].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#fe4b48>
   EN: If the target has lower than 50% Symbolic <color=#00ff9c>HP</color>, <color=#fe4b48>Damage</color> Dealt +1
   PL: Jeśli cel ma poniżej 50% Symbolicznych <color=#00ff9c>HP</color>, atak zadaje <color=#fe4b48>Obrażenia</color> +1
229. [RPG [I990017] — opis] 계략의 상징. 헤매인다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990017].description
   limit: do 120 znaków
   EN: Symbol of Guile. To wander.
   PL: Symbol Fortelu. Błądzi.
230. [RPG [I990018] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990018].displayName
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor
231. [RPG [I990018] — statystyki przedmiotu] 상징계 체력이 25% 미만이면 상징계 <color=#00ff9c>체력</color>을 15 <color=#00ff9c>회복</color>하고, 10초 동안 받는 <color=#fe4b48>피해량</color> 20% 감소 (쿨타임 19초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990018].statText
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#fe4b48>
   EN: At lower than 25% Symbolic HP, <color=#00ff9c>heals</color> 15 Symbolic <color=#00ff9c>HP</color> and <color=#fe4b48>Damage</color> Taken -20% for the next 10 seconds (19 seconds cooldown)
   PL: Poniżej 25% Symbolicznych HP: <color=#00ff9c>leczy</color> 15 Symbolicznych <color=#00ff9c>HP</color> i otrzymuje <color=#fe4b48>Obrażenia</color> -20% przez następne 10 sekund (odnowienie 19 s)
232. [RPG [I990018] — opis] 변신의 상징. 섭취한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990018].description
   limit: do 120 znaków
   EN: Symbol of Metamorphosis. To consume.
   PL: Symbol Metamorfozy. Spożywa.
233. [RPG [I990432] — nazwa wyświetlana] 전등 줄
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990432].displayName
   limit: do 40 znaków
   EN: Lamp Pull Cord
   PL: Sznurek Lampy
234. [RPG [I990432] — statystyki przedmiotu] 상징계에서 3초 동안 이동하지 않은 뒤 공격 시 그 공격의 <color=#fe4b48>피해량</color> +2 (쿨타임 10초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990432].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: If player did not move for 3 seconds in the Symbolic, <color=#fe4b48>Damage</color> Dealt +2 for the next attack (10 seconds cooldown)
   PL: Jeśli przez 3 sekundy w Symbolicznym gracz się nie ruszał, następny atak zadaje <color=#fe4b48>Obrażenia</color> +2 (odnowienie 10 s)
235. [RPG [I990432] — opis] 줄을 당기면 전등이 켜진다. 줄을 다시 당기면 전등이 꺼진다. 줄에 묶여있기 때문이다. 이것이 줄과 못이 가지는 공통점이자 차이점이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990432].description
   limit: do 230 znaków
   EN: Pull the cord, and the light turns on. Pull it again, and the light goes dark. The lamp is bound to the cord. This is what cords and nails share... and what sets them apart.
   PL: Pociągnij sznurek — i lampa się zapala. Pociągnij znowu — lampa gaśnie. Bo lampa jest przywiązana do sznurka. To jest to, co łączy sznurek z gwoździem... i to, co je różni.
236. [RPG [I990117] — nazwa wyświetlana] 철 지난 르루주 옷
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990117].displayName
   limit: do 40 znaków
   EN: Out-of-style Rouge Clothing
   PL: Przestarzałe Ubranie Le Rouge
237. [RPG [I990117] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +4
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990117].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>
   EN: Symbolic <color=#00ff9c>HP</color> +4
   PL: Symboliczne <color=#00ff9c>HP</color> +4
238. [RPG [I990117] — opis] 벽돌 속에 박혀있는 시즌이 지나버린 못. 한때는 트렌드에 맞는 못이었겠지만 지금 이 못은 촌스럽다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990117].description
   limit: do 150 znaków
   EN: A nail from a bygone season, driven into brick. It may once have been on trend, but now it is merely out-of-style.
   PL: Gwóźdź z minionej pory, wbity w cegłę. Kiedyś może pasował do trendów, ale dziś jest po prostu kiczowaty.
239. [RPG [I990321] — nazwa wyświetlana] 낡은 녹음기
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990321].displayName
   limit: do 40 znaków
   EN: Old Recorder
   PL: Stary Dyktafon
240. [RPG [I990321] — statystyki przedmiotu] 그림자계 전투 진입 시 전장의 모든 아군 <color=#F8C200>정신력 4 회복</color>
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990321].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: Upon entering battle in the Shadowed, all allies on the field <color=#F8C200>heal 4 SP</color>
   PL: Po wejściu do walki w Zacienionym wszyscy sojusznicy na polu <color=#F8C200>leczy 4 SP</color>
241. [RPG [I990321] — opis] 녹음기에서는 기록된 목소리가 흘러나온다. 흘러나오지만 목소리는 갇혀 있다. 목소리조차 못 박을 수 있다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990321].description
   limit: do 150 znaków
   EN: A recorded Voice flows from the machine. It flows, yet remains imprisoned. Even a Voice can be nailed in place.
   PL: Z dyktafonu płynie nagrany Głos. Płynie, a jednak pozostaje uwięziony. Nawet Głos można przygwoździć.
242. [RPG [I990322] — nazwa wyświetlana] 죽은 새
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990322].displayName
   limit: do 40 znaków
   EN: Dead Bird
   PL: Martwy Ptak
243. [RPG [I990322] — statystyki przedmiotu] 상징계에서 <color=#F8C200>약점 공격</color> 시 <color=#fe4b48>피해량</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990322].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, <color=#F8C200>Weakpoint Attack</color> <color=#fe4b48>Damage</color> Dealt +1
   PL: W Symbolicznym <color=#F8C200>Atak na Słaby Punkt</color> zadaje <color=#fe4b48>Obrażenia</color> +1
244. [RPG [I990322] — opis] 일생 동안 나팔에 대고 지저귀던 새는, 어느 날 머리에 나팔을 처박고 지저귀다 죽었다. 그다음에 온 새로운 새는 새장에 갇혀 지저귀게 되었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990322].description
   limit: do 220 znaków
   EN: A bird spent its entire life singing into a horn. One day, it thrust its head into the horn and sang until it died. The next bird was made to sing from inside a cage.
   PL: Ptak, który przez całe życie gwizdał w trąbę, pewnego dnia wpił głowę w trąbę i gwizdał aż do śmierci. Następny ptak musiał już gwizdać z klatki.
245. [RPG [I990323] — nazwa wyświetlana] 양말
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990323].displayName
   limit: do 40 znaków
   EN: Socks
   PL: Skarpety
246. [RPG [I990323] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +4
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990323].statText
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [RPG [I990323] — opis] 신발을 신을 때 양말을 신어야 하는 건 이상해. 이미 발을 보호하려고 신발을 신었는데, 다시 신발과 발 사이에 뭔가를 씌우는 거잖아.\n아니, 그렇기엔 양말에는 품위가 있지. 신발은 발이 아파서 찾는 본능의 영역이지만, 양말은 쾌적함을 위해 찾는 문명의 영역이거든.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990323].description
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's strange that shoes require socks. We wear shoes to protect our feet, yet we place another layer between the foot and the shoe to protect them both?\nOr... perhaps that excess is what gives socks their dignity. Shoes belong to instinct—we <i>need</i> shoes because our feet hurt without them, while socks fall within the realm of civilization because we <i>want</i> the comfort.
   PL: Dziwne jest to, że buty wymagają skarpet. Buty zakładamy, żeby chronić stopy, a potem wkładamy jeszcze jedną warstwę między stopę a but?\nNie... może właśnie ta nadwyżka daje skarpetom ich godność. Buty należą do sfery instynktu — <i>potrzebujemy</i> ich, bo bez nich stopy bolą, podczas gdy skarpety należą do sfery cywilizacji, bo <i>chcemy</i> komfortu.
248. [RPG [I102023] — nazwa wyświetlana] 브랜드 디렉터의 유품
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I102023].displayName
   limit: do 40 znaków
   EN: Brand Director's Effects
   PL: Pamiątki Dyrektorki Marki
249. [RPG [I102023] — statystyki przedmiotu] 상징계에서 피격 시 10% 확률로 공격자에게 3 <color=#fe4b48>피해</color>
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I102023].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: When hit in the Symbolic, 10% chance to return 3 <color=#fe4b48>Damage</color> against the attacker
   PL: W Symbolicznym przy trafieniu 10% szans na odniesienie 3 <color=#fe4b48>Obrażeń</color> przez atakującego
250. [RPG [I102023] — opis] 르루주의 브랜드 디렉터. 르루주라는 브랜드가 지녀야 할 의미와 방향성 그 모든 것은 브랜드 디렉터의 지시 아래 정해진다. 브랜드 디렉터는 누구보다 붉은 신의 목소리를 잘 들어왔다. 그리고 기특하게도 붉은 신의 목소리가 사라졌을 때마저 목소리를 들려줄 새로운 존재를 빚어내려 했다. 사실 붉은 신의 부재는 숨기고자 했다면 얼마든지 숨길 수 있던 사실이었는데도.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I102023].description
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Le Rouge's Brand Director.\n\nEvery meaning and direction of the brand was decided under her command. No one heard the Crimson God's Voice more clearly than she did. Admirably, even after that Voice vanished, the Brand Director sought to fashion a new being through which the Voice might be heard again. The Crimson God's absence could have remained hidden had she wished it so, but she chose not to.
   PL: Dyrektorka Marki Le Rouge.\n\nCałe znaczenie i kierunek, jakie miała mieć branda Le Rouge, określane były pod jej komendą. Nikt nie słyszał Głosu Szkarłatnego Boga wyraźniej niż ona. Podziw godna — nawet po tym, jak Głos zniknął, starała się ulepić nową istotę, przez którą Głos mógłby znów zabrzmieć. Nieobecność Szkarłatnego Boga mogła pozostać ukryta, gdyby tego zechciała — lecz nie zechciała.
251. [RPG [I990919] — nazwa wyświetlana] 반복
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990919].displayName
   limit: do 40 znaków
   EN: Repetition
   PL: Powtarzanie
252. [RPG [I990919] — statystyki przedmiotu] 상징계에서 <color=#F8C200>자동 공격</color> 토글(T 키)을 켜면 바라보는 방향의 적을 감지해 <color=#F8C200>기본 공격을 자동 반복</color>\n- 감지 범위: 앞 4칸 × 좌우 1칸\n- 이동·가드 등 다른 행동이 우선하고, 끝나면 다시 진행\n- 공격 후 이동 후딜 제거(토글과 무관하게 상시 발동)\n- 층 이동·그림자계 전투 진입 시 토글 해제
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990919].statText
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: Unlocks <color=#F8C200>Auto-attack</color> in the Symbolic.\n\nPress the Auto-attack (T on keyboard) button to toggle ON/OFF. Detects enemies based on character orientation and <color=#F8C200>automatically uses the Basic Attack</color>\n- Detection Range: 4 tiles ahead, 1 tile each left & right\n- Prioritizes other actions such as Move or Block; resumes Auto-attack when other actions are completed\n- Removes post-attack movement delay regardless of toggling\n- Automatically toggled OFF when:\n  - Moving between floors\n  - Entering a battle in the Shadowed
   PL: Odblokowuje <color=#F8C200>Atak Automatyczny</color> w Symbolicznym.\n\nNaciśnij przycisk ataku automatycznego (T na klawiaturze), aby go włączyć lub wyłączyć. Wykrywa wrogów zależnie od orientacji postaci i <color=#F8C200>automatycznie wykonuje Atak Podstawowy</color>\n- Zasięg wykrywania: 4 pola z przodu, po 1 polu w lewo i w prawo\n- Priorytet mają inne akcje, jak Ruch czy Blok; atak automatyczny wznawia się po ich zakończeniu\n- Usuwa opóźnienie ruchu po ataku niezależnie od przełącznika\n- Wyłącza się automatycznie przy:\n  - zmianie piętra\n  - wejściu do walki w Zacienionym
253. [RPG [I990919] — opis] 자동으로 반복한다. 그저 수행한다. 이 반복이 당신에게 부디 편리하기를.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I990919].description
   limit: do 130 znaków
   EN: Repeat automatically. Simply execute. May this repetition, at least, prove convenient to you.
   PL: Powtarza automatycznie. Po prostu wykonuje. Niech to powtarzanie okaże się ci choć trochę wygodne.
254. [RPG [I1209] — nazwa wyświetlana] 벼린 재봉 가위
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1209].displayName
   limit: do 40 znaków
   EN: Tempered Sewing Scissors
   PL: Zahartowane Nożyczki Krawieckie
255. [RPG [I1209] — statystyki przedmiotu] 상징계 공격 적중 시 30% 확률로 1만큼 <color=#fe4b48>피해</color> 입히는 <color=#F8C200>가위 추가 공격</color> 발동 (경직 0.3초)\n\n그림자계 전투 진입 시 해당 효과로 피격 당한 횟수만큼 모든 적의 <color=#F8C200>출혈</color> 횟수 증가 (최대 5)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1209].statText
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#F8C200>, \n
   EN: In the Symbolic, 30% chance to trigger <color=#F8C200>Scissors-snip Extra Attack</color> dealing 1 <color=#fe4b48>Damage</color> upon landing an attack (0.3 seconds Hitstun)\n\nUpon entering battle in the Shadowed, inflicts on all enemies <color=#F8C200>Bleed</color> Count equal to the number of times they were struck by this effect (max 5)
   PL: W Symbolicznym 30% szans na uruchomienie <color=#F8C200>Dodatkowego Ataku Nożycami</color> zadającego 1 <color=#fe4b48>Obrażenie</color> po trafieniu atakiem (0.3 s Hitstun)\n\nPo wejściu do walki w Zacienionym nakłada wszystkim wrogom <color=#F8C200>Liczba Krwawienia</color> równą liczbie trafień tym efektem (maks. 5)
256. [RPG [I1209] — opis] 수선사는 원단을 자르고 패턴대로 붙이죠. 요즘 부쩍 가위질 소리가 커졌어요. 르누아르 쪽에서 엄청난 양의 발주가 온 모양이에요. 뭔가 큰 싸움이라도 나려나?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I1209].description
   limit: do 280 znaków
   EN: The Alterationist cuts fabric, then joins it again according to the pattern. The snipping has grown much louder of late—the Noirs must have placed an enormous order. Perhaps a major conflict is about to break out?
   PL: Krawcowa tnie tkaninę, a potem skleja ją według wzoru. Ostatnio dźwięk cięcia głośniejszy — Le Noir musiały złożyć ogromne zamówienie. Może szykuje się jakiś wielki konflikt?

## Tryb RPG [common] — rpg-loc-item-common-a1c10p2
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-item-common-a1c10p2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

257. [RPG [I104004] — nazwa wyświetlana] 붉은 색의 루비 심장
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104004].displayName
   limit: do 40 znaków
   EN: Red Ruby Heart
   PL: Czerwone Rubinowe Serce
258. [RPG [I104004] — opis] 행복한 옷장의 계속 존재하고 싶다는 마음이 담겨있던 그릇
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104004].description
   limit: do 120 znaków
   EN: The vessel that once held the Happy Closet's wish to go on existing.
   PL: Naczynie, w którym mieszkało pragnienie Szczęśliwej Szafy, by trwać przy istnieniu.
259. [RPG [I104005] — nazwa wyświetlana] 분홍 꽃잎을 휘날리던 환상체의 알
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104005].displayName
   limit: do 70 znaków
   EN: The Egg of an Abnormality that Scattered Pink Petals
   PL: Jajo Abnormalności Rozsiejącej Różowe Płatki
260. [RPG [I104005] — statystyki przedmiotu] 상징계에서 적에게 <color=#F8C200>기본 공격</color> 적중 시 대상에게 <color=#F8C200>꽃잎 표식</color> 부여\n- <color=#F8C200>표식</color>을 가진 적이 없을 때만 부여\n- <color=#F8C200>꽃잎 표식</color> 유지 시간: 10초\n- 꽃잎 표식 쿨타임: 10초 (표식을 부여한 순간부터)\n- 꽃잎 표식이 부여된 대상에게 뫼르소의 <color=#F8C200>기본 공격</color>으로 가하는 <color=#fe4b48>피해량</color> +1\n- 해당 표식이 부여된 대상 사망 시 그 대상 3x3 범위에 5만큼 <color=#fe4b48>피해</color> 입힘
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104005].statText
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, when landing a hit using <color=#F8C200>Basic Attack</color> on the enemy, inflict <color=#F8C200>Petal Mark</color>\n- This effect is inflicted only when the enemy does not have this <color=#F8C200>Mark</color>\n- <color=#F8C200>Petal Mark</color> lasts for 10 seconds\n- Petal Mark cooldown: 10 seconds (counts from the moment the mark is inflicted)\n- Meursault's <color=#F8C200>Basic Attack</color> deals +1 <color=#fe4b48>Damage</color> against targets inflicted with Petal Mark\n- When a target that has this mark is defeated, deal 5 <color=#fe4b48>damage</color> on 3 x 3 tiles centered on the target
   PL: W Symbolicznym trafienie <color=#F8C200>Atakiem Podstawowym</color> wroga nakłada na niego <color=#F8C200>Znak Płatków</color>\n- Nakładany tylko, gdy wróg nie ma tego <color=#F8C200>Znaku</color>\n- <color=#F8C200>Znak Płatków</color> utrzymuje się 10 sekund\n- Odnowienie Znaku Płatków: 10 s (liczone od chwili nałożenia)\n- <color=#fe4b48>Obrażenia</color> <color=#F8C200>Ataku Podstawowego</color> Meursaulta wobec celów z Znakiem Płatków +1\n- Po śmierci celu ze znakiem zadaje 5 <color=#fe4b48>Obrażeń</color> w obszarze 3 x 3 wyśrodkowanym na celu
261. [RPG [I104005] — opis] 백화점의 고객과 점원들은 이미 저마다의 뒤틀림이 진행되었다. 그리고 뒤틀림의 끝은 환상체이기에, 이곳에 환상체가 없는 것은 오히려 이상한 일이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104005].description
   limit: do 280 znaków
   EN: Every customer and employee in the department store is already undergoing their own Distortion. Since the terminus of Distortion is an Abnormality, the true abnormality would be if no Abnormalities had appeared here.
   PL: Klienci i pracownicy Grand Magasin są już na różnych etapach Wypaczenia. A końcem Wypaczenia jest Abnormalność — więc tym, co naprawdę nienormalne, byłoby to, gdyby w tym miejscu nie pojawiła się żadna Abnormalność.
262. [RPG [I104006] — nazwa wyświetlana] 황금 단추
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104006].displayName
   limit: do 40 znaków
   EN: Golden Button
   PL: Złoty Guzik
263. [RPG [I104006] — opis] 황금송진으로 빚어낸 단추.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104006].description
   limit: do 120 znaków
   EN: A button fashioned from Golden Resin.
   PL: Guzik uformowany ze Złotej Żywicy.
264. [RPG [I104007] — nazwa wyświetlana] 황금 이빨
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104007].displayName
   limit: do 40 znaków
   EN: Golden Tooth
   PL: Złoty Ząb
265. [RPG [I104007] — opis] 황금가죽으로 꿰맨 이빨
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104007].description
   limit: do 120 znaków
   EN: A tooth stitched together with Golden Hide.
   PL: Ząb zszyty Złotą Skórą.
266. [RPG [I104008] — nazwa wyświetlana] 황금 머리카락
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104008].displayName
   limit: do 40 znaków
   EN: Golden Hair
   PL: Złote Włosy
267. [RPG [I104008] — opis] 황금가닥으로 뽑아낸 머리카락
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I104008].description
   limit: do 120 znaków
   EN: Hair drawn out into strands of gold.
   PL: Włosy wyciągnięte w pasma złota.
268. [RPG [I990311] — nazwa wyświetlana] 붉은 못
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990311].displayName
   limit: do 40 znaków
   EN: Red Nail
   PL: Czerwony Gwóźdź
269. [RPG [I990311] — opis] 목소리를 절실히 기다렸던 점원의 척추뼈. 못은 고정하기 위한 것. 뼈는 살을 고정한다. 뼈는 못. 못은 바늘과 같이 관통한다. 이 척추뼈는 좋은 못이자 바늘이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990311].description
   limit: do 300 znaków
   EN: The vertebra of an employee who waited desperately for the Voice. A nail exists to hold things fast. Bone holds flesh in place. Bone is a nail. A nail pierces like a needle. This vertebra is not only a quality nail but also a needle.
   PL: Kręg pracownika, który gorączkowo wyczekiwał Głosu. Gwóźdź istnieje po to, by unieruchamiać. Kość unieruchamia ciało. Kość jest gwoździem. Gwóźdź przebija jak igła. Ten kręg to dobry gwóźdź i zarazem igła.
270. [RPG [I990313] — nazwa wyświetlana] 믿음
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990313].displayName
   limit: do 40 znaków
   EN: Faith
   PL: Wiara
271. [RPG [I990313] — statystyki przedmiotu] 상징계에서 사망에 이르는 <color=#fe4b48>피해</color>를 받으면 10% 확률로 <color=#00ff9c>체력</color> 1로 생존\n- 즉사 등 일부 피해 제외\n\n상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990313].statText
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, upon taking <color=#fe4b48>Damage</color> that would result in death, 10% chance to survive with 1 <color=#00ff9c>HP</color>\n- Excluding certain damages such as Instant Death\n\nSymbolic <color=#00ff9c>HP</color> +2
   PL: W Symbolicznym, gdy otrzymasz <color=#fe4b48>Obrażenia</color> grożące śmiercią, 10% szans na <color=#00ff9c>przeżycie z 1 HP</color>\n- Nie dotyczy części obrażeń, np. natychmiastowej śmierci\n\nSymboliczne <color=#00ff9c>HP</color> +2
272. [RPG [I990313] — opis] 믿음은 바라는 것들의 실상이요 보이지 않는 것들의 증거니
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990313].description
   limit: do 120 znaków
   EN: "Now faith is the substance of things hoped for, the evidence of things not seen."
   PL: „Wiara to podstawy tego, czego się oczekuje, i dowód rzeczy niewidzialnych”
273. [RPG [I990417] — nazwa wyświetlana] 분홍색 메리 제인
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990417].displayName
   limit: do 40 znaków
   EN: Pink Mary Janes
   PL: Różowe Balerinki Mary Jane
274. [RPG [I990417] — statystyki przedmiotu] 그림자계 전투에서 뿌이의 맥동 위력 +1\n- 속도 최솟값 +3, 최댓값 +3\n- '붉은 못' 코인 +1 (추가 코인 적중 시 <color=#F8C200>꽃잎 투사체</color> 발사)\n- '힘내' 사용 시 맥동 위력 2당 가중치 +1 (최대 2)\n- '내 손 잡아' 해금 (아군이 흐트러지면 자동 사용해 <color=#F8C200>흐트러짐 해제</color> 및 <color=#00ff9c>체력</color> <color=#00ff9c>회복</color>, 턴당 2회)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990417].statText
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: Pwie's Pulsation Potency +1 during battle in the Shadowed\n- Min & Max Speed +3\n- "Crimson Nail" Coin +1 (On Hit using additional Coins, fire <color=#F8C200>Petal Projectiles</color>)\n- Upon using the "Perk Up" Skill, gain +1 Atk Weight for every 2 Pulsation Potency (max 2)\n- Unlock the "Grab My Hand" Skill (used automatically when an ally is Staggered to <color=#F8C200>recover them from Stagger</color> and <color=#00ff9c>heal</color> their <color=#00ff9c>HP</color>; 2 times per turn)
   PL: W walce w Zacienionym Moc Pulsacji Pwie +1\n- Minimalna i maksymalna Szybkość +3\n- Moneta „Szkarłatny Gwóźdź” +1 (trafienie dodatkowymi monetami wystrzeliwuje <color=#F8C200>Pociski Płatków</color>)\n- Użycie „Ożyw się”: +1 Waga Ataku za każde 2 Moc Pulsacji (maks. 2)\n- Odblokowuje „Złap Mą Rękę” (używane automatycznie, gdy sojusznik zostanie Ogłuszony, aby <color=#F8C200>zdjąć Ogłuszenie</color> i <color=#00ff9c>leczyć</color> jego <color=#00ff9c>HP</color>; 2 razy na turę)
275. [RPG [I990417] — opis] 누구든 집으로 돌아오게 해주는 신발. 걸을 때마다 흩날리는 잔향에는 그리움이 묻어있다. 이 신발을 신으면 집에서 가장 먼 곳으로 떠나고 싶어진다. 집을 그리워할수록 집에 가까워지기 마련이니.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990417].description
   limit: do 320 znaków
   EN: Shoes that bring anyone home. The faint aroma scattered by each footfall is steeped in longing, for whoever wears them begins to yearn for the farthest place from home. After all, the more one longs for home, the closer to home one inevitably draws.
   PL: Buty, które zawsze prowadzą każdego z powrotem do domu. W resztkach aromatu rozwiewanych przy każdym kroku tkwi tęsknota. Kto je wkłada, chce wyruszyć jak najdalej od domu. W końcu im mocniej tęsknimy za domem, tym bliżej domu się zbliżamy.
276. [RPG [I991012] — nazwa wyświetlana] 황금 수의
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991012].displayName
   limit: do 40 znaków
   EN: Golden Shroud
   PL: Złoty Całun
277. [RPG [I991012] — statystyki przedmiotu] 상징계에서 뿌이의 이동 경로에 <color=#F8C200>르 보미스망 (Le Vomissement)</color> 생성\n- 뿌이 주위 1칸 또는 <color=#F8C200>르 보미스망 (Le Vomissement)</color> 위의 적에게 2초마다 4만큼 <color=#fe4b48>피해</color> 입힘\n- <color=#fe4b48>피해</color> 입힌 적에게 <color=#F8C200>황금계시</color> 부여\n- <color=#F8C200>황금계시</color>가 있는 적 사망 시 주위 1칸에 4만큼 <color=#fe4b48>피해</color> 입힘 (경직 0.1초)\n\n그림자계 전투에서 뿌이의 맥동 위력 +1\n- 방어 레벨 +10\n- 턴 종료 시 흐트러짐 상태이면 해제하고 최대 <color=#00ff9c>체력</color>의 50% <color=#00ff9c>회복</color> (전투당 1회)\n- '붉은 못'(2번째 코인)·'저리가'·'붉은못 세례' 적중 시 <color=#F8C200>황금계시</color> 1 부여\n- '붉은못 세례' 사용 시 맥동 위력 5 이상이면 가중치 +2, 코인 위력 +(맥동 위력 - 3)\n- '아프지마' 적중 시 대상 최대 <color=#00ff9c>체력</color>의 (맥동 위력 x 2)%만큼 추가 <color=#00ff9c>회복</color>, 정신력 (맥동 위력 x 3) 추가 회복\n- '내 손 잡아' 적중 시 다음 턴에 대상 최대 <color=#00ff9c>체력</color>의 50%만큼 보호막 부여
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991012].statText
   limit: do 1200 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, <color=#00ff9c>, \n
   EN: In the Symbolic, Pwie leaves <color=#F8C200>Le Vomissement</color> in their tracks\n- Enemies 1 tile within Pwie and enemies on top of <color=#F8C200>Le Vomissement</color> take 4 <color=#fe4b48>Damage</color> every 2 seconds\n- Inflicts <color=#F8C200>Golden Revelation</color> on all enemies who took <color=#fe4b48>Damage</color> from this effect\n- When enemies that have <color=#F8C200>Golden Revelation</color> dies, they deal 4 <color=#fe4b48>Damage</color> within 1 tile around them (0.1 seconds Hitstun)\n\nDuring battle in the Shadowed:\n- Pwie gains 1 Pulsation Potency\n- Defense Level +10\n- Turn End: If Pwie is Staggered, recover from Stagger and <color=#00ff9c>heal</color> 50% <color=#00ff9c>HP</color> (once per Encounter)\n- On Hit using "Crimson Nail (2nd Coin)", "Go Away", or "Baptism of Crimson Nails", inflict 1 <color=#F8C200>Golden Revelation</color>\n- On "Baptism of Crimson Nails" use, at 5+ Pulsation Potency, gain +2 Atk Weight and Coin Power +(Pulsation Potency - 3)\n- Upon using "Don't Get Hurty", additionally <color=#00ff9c>heal</color> (Pulsation Potency x 2)% <color=#00ff9c>HP</color> and (Pulsation Potency x 3) SP\n- On Hit using "Grab My Hand", apply Shield equal to 50% of target's max <color=#00ff9c>HP</color> next turn
   PL: W Symbolicznym Pwie zostawia na swojej drodze <color=#F8C200>Le Vomissement</color>\n- Wrogowie w promieniu 1 pola od Pwie i wrogowie na <color=#F8C200>Le Vomissement</color> otrzymują 4 <color=#fe4b48>Obrażenia</color> co 2 sekundy\n- Wrogom poszkodowanym przez ten efekt nakłada <color=#F8C200>Złote Objawienie</color>\n- Śmierć wroga z <color=#F8C200>Złotym Objawieniem</color> zadaje 4 <color=#fe4b48>Obrażenia</color> w promieniu 1 pola (0.1 s Hitstun)\n\nW walce w Zacienionym Moc Pulsacji Pwie +1\n- Poziom Obrony +10\n- Koniec tury: jeśli Pwie jest Ogłuszone, zdejmuje Ogłuszenie i <color=#00ff9c>leczy</color> 50% maksymalnego <color=#00ff9c>HP</color> (raz na potyczkę)\n- Trafienie „Szkarłatnym Gwoździem (2. moneta)”, „Odejdź” lub „Chrzestem Szkarłatnych Gwoździ” nakłada 1 <color=#F8C200>Złote Objawienie</color>\n- Użycie „Chrzest Szkarłatnych Gwoździ” przy Mocy Pulsacji 5+: Waga Ataku +2 i Moc Monety +(Moc Pulsacji - 3)\n- Trafienie „Nie Bolej”: dodatkowo <color=#00ff9c>leczy</color> (Moc Pulsacji x 2)% <color=#00ff9c>HP</color> i (Moc Pulsacji x 3) SP\n- Trafienie „Złap Mą Rękę”: następnej tury nakłada celowi Tarczę równą 50% jego maksymalnego <color=#00ff9c>HP</color>
278. [RPG [I991012] — opis] 황금가죽에서 털을 보존한 시어링 케이프. 이 외투는 밖에서 오는 것을 막아 준다. 그리고 안에서 피어나는것을 촉진한다. 이 옷을 걸침으로써 아이의 유년기는 끝을 맞이한다. 기대받는 것과 부흥해야 하는 것을 알게 되고 그에 따라 행해야 한다. 세계에 대한 질문은 이제 허락되지 않는다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991012].description
   limit: do 450 znaków
   EN: A shearling cape that preserves the fur of the Golden Hide. This garment keeps what comes from outside at bay, while hastening what blooms within. Once the child dons it, childhood reaches its end. The child learns what others expect and what must be restored, and is compelled to act accordingly. It is no longer permitted to be curious about the world.
   PL: Szeroki płaszcz z futrem, zachowujący sierść Złotej Skóry. To okrycie broni przed tym, co z zewnątrz, i przyśpiesza to, co rozkwita wewnątrz. Narzucenie go oznacza koniec dzieciństwa. Dziecko poznaje, czego się od niego oczekuje i co musi wskrzesić, i w konsekwencji musi tak postępować. Pytanie o świat nie jest już dozwolone.
279. [RPG [I991013] — nazwa wyświetlana] 생가죽 다발
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991013].displayName
   limit: do 40 znaków
   EN: Bundle of Rawhide
   PL: Wiązka Surowej Skóry
280. [RPG [I991013] — opis] 뼈에서 살을 발라내듯 살 위에서 가죽을 벗겨낸다. 그리고 가죽에 붙어있는 털들을 녹여서 원피만을 남겨야 한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991013].description
   limit: do 190 znaków
   EN: As flesh is stripped from bone, hide is peeled from flesh. Then the hair clinging to it must be dissolved away until only the raw skin remains.
   PL: Tak jak z kości zdejmuje się mięso, tak z ciała obdziera się skórę. A potem sierść przywierającą do skóry trzeba rozpuścić tak, by została sama surowa skóra.
281. [RPG [I991014] — nazwa wyświetlana] 무두질한 가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991014].displayName
   limit: do 40 znaków
   EN: Tanned Hide
   PL: Garbowana Skóra
282. [RPG [I991014] — opis] 가죽은 탄색으로 태너리에서 탄닌질로 태닝된다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991014].description
   limit: do 120 znaków
   EN: Hide takes on the color of tan as tannins transform it inside the Tannery.
   PL: Skóra przybiera barwę brunatną, gdy garbniki przekształcają ją w Garbarni.
283. [RPG [I991015] — nazwa wyświetlana] 부드러워진 가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991015].displayName
   limit: do 40 znaków
   EN: Supple Hide
   PL: Zmiękczona Skóra
284. [RPG [I991015] — opis] 가죽은 고기가 식물이 되어가는 과정이다. 살점들은 녹아내려 가고 그 속을 나뭇가지들이 채운다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991015].description
   limit: do 160 znaków
   EN: Hide is the process by which meat becomes plant. The flesh dissolves, and branches of wood fill the hollows left behind.
   PL: Skóra to proces, w którym mięso staje się rośliną. Mięso się rozpuszcza, a puste w środku miejsca wypełniają gałązki.
285. [RPG [I991016] — nazwa wyświetlana] 수선 도구
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991016].displayName
   limit: do 40 znaków
   EN: Alteration Tools
   PL: Narzędzia Krawieckie
286. [RPG [I991016] — statystyki przedmiotu] 상징계에서 뿌이의 <color=#F8C200>통제자 투사체</color> 해금\n- 5칸 이내의 무작위 적에게 발사 (쿨타임 2.5초)\n- 적중 시 주위 1칸에 3만큼 <color=#fe4b48>피해</color> 입힘 (경직 0.1초)\n\n그림자계 전투에서 뿌이의 '내가 끝내줄게…' 해금\n- 공격 스킬로 적을 처치하지 못하면 그 적에게 사용 (턴당 1회)\n- 대상의 잃은 <color=#00ff9c>체력</color> 1%당 <color=#fe4b48>피해량</color> +0.5% (최대 30%)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991016].statText
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, <color=#00ff9c>, \n
   EN: In the Symbolic, unlock <color=#F8C200>Overseer Projectiles</color>\n- Fired to a random enemy within 5 tiles (2.5 seconds cooldown)\n- On hitting the target, deals 3 <color=#fe4b48>Damage</color> within 1 tile (0.1 seconds Hitstun)\n\nIn Shadowed Battles, unlock "I'll End It for You..." for Pwie\n- If an enemy is not killed by an Attack Skill, use it on that enemy (once per turn)\n- Deal +0.5% <color=#fe4b48>damage</color> for every 1% missing <color=#00ff9c>HP</color> on target (max 30%)
   PL: W Symbolicznym odblokowuje <color=#F8C200>Pocisk Nadzorcy</color> Pwie\n- Wystrzeliwuje w losowego wroga w promieniu 5 pól (odnowienie 2.5 s)\n- Trafienie zadaje 3 <color=#fe4b48>Obrażenia</color> w promieniu 1 pola (0.1 s Hitstun)\n\nW walce w Zacienionym odblokowuje dla Pwie „Ja to Skończę…”\n- Jeśli umiejętność ataku nie zabije wroga, używa jej na tym wrogu (raz na turę)\n- +0.5% <color=#fe4b48>obrażeń</color> za każdy 1% brakującego <color=#00ff9c>HP</color> celu (maks. 30%)
287. [RPG [I991016] — opis] 르루주들이 가죽을 원하는 이유는 간단하지. 가죽은 고갈이야. 원단은 과잉이고. 고기를 먹고 나서 남은 것을 두르는 거지 더 이상 먹을 게 없어지면 어떡하지는 신경 쓰지 않아. 지금 먹고 지금 두르는 거야. 르루주는 고갈을 숭배하니까. 가죽을 좋아해서 고갈을 향하는 게 아니야. 고갈을 향하다 보니 가죽을 두른 거지.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991016].description
   limit: do 460 znaków
   EN: The reason the Rouges desire hide is simple. Hide is depletion; fabric is excess. They eat the meat, then wear what remains, never wondering what happens when nothing is left to eat. Consume now. Wear now. The Rouges worship depletion. They do not walk toward depletion because they love hide. They came to wear hide because depletion was always its destination.
   PL: Powód, dla którego Le Rouge pragną skóry, jest prosty. Skóra to wyczerpanie. Tkanina to nadmiar. Je się mięso, a potem narzuca się to, co z niego zostało — nie obchodzi ich, co będzie, gdy nie będzie już czego jeść. Je się teraz i ubiera się teraz. Le Rouge otaczają kultem wyczerpanie. Nie zwracają się ku wyczerpaniu, bo kochają skórę. Zwróciły się ku wyczerpaniu — a po drodze narzuciły skórę.
288. [RPG [I991022] — nazwa wyświetlana] 황금가죽 원단
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991022].displayName
   limit: do 40 znaków
   EN: Golden Hide Fabric
   PL: Tkanina ze Złotej Skóry
289. [RPG [I991022] — opis] 그렇다면 황금가죽은 가죽 속에 미세한 황금다발들이 가죽의 구조 사이에 빽빽하게 채워진 가죽이라 할 수 있다. 균열을 메웠던 황금가죽은 진정 누군가의 피부이자 고기였고. 무두질을 거쳐진 황금가죽은 황금가지에 걸맞게 나무적 속성을 가지게 되었다. 하지만 황금가지가 식물이라 단정 지어진 적이 있던가?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991022].description
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Golden Hide, then, could be described as a hide whose very structure is densely packed with minute bundles of gold. The Hide that once filled the cracks truly had been someone's skin and flesh. And once it was tanned, it came to take on arboreal properties befitting the Golden Bough.\n\nBut was the Golden Bough ever truly established to be a plant?
   PL: Złotą Skórę można zatem opisać jako skórę, której struktura jest gęsto wypełniona drobnymi paczkami złota. Skóra, która zapełniała pęknięcia, naprawdę była czyjąś skórą i mięsem. A po garbowaniu Złota Skóra nabrała drzewnych właściwości przystających do Złotej Gałęzi.\nAle czy kiedykolwiek ustalono, że Złota Gałąź jest rośliną?
290. [RPG [I992705] — nazwa wyświetlana] 유체
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I992705].displayName
   limit: do 40 znaków
   EN: Larva
   PL: Larwa
291. [RPG [I992705] — opis] 백화점이 세워지기 전 옛 존재가 기적처럼 살아남아 자식을 남겼고, 그렇게 살아남은 자손은 해변에 떠밀려 와 새 시대의 재료가 된다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I992705].description
   limit: do 260 znaków
   EN: Before the department store was built, a being of eld survived as if by miracle and left behind an offspring. That surviving descendant was beached on the Shore, there to become material for a new age.
   PL: Zanim wzniesiono Grand Magasin, dawna istota cudem przeżyła i pozostawiła po sobie potomka. Ten potomek został wyrzucony na brzeg, by stać się materiałem nowej epoki.
292. [RPG [I990926] — nazwa wyświetlana] 알록달록한 실타래
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990926].displayName
   limit: do 40 znaków
   EN: Colorful Skein
   PL: Kolorowy Motek
293. [RPG [I990423] — nazwa wyświetlana] 조명
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990423].displayName
   limit: do 40 znaków
   EN: The Lights
   PL: Lampy
294. [RPG [I990423] — statystyki przedmiotu] 상징계에서 이동하지 않는 동안 피격 시 받는 <color=#fe4b48>피해량</color> -2 (받는 <color=#fe4b48>피해량</color> 최소 1)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990423].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: In the Symbolic, <color=#fe4b48>Damage</color> Taken -2 when hit while standing still (min 1 <color=#fe4b48>Damage</color> taken)
   PL: W Symbolicznym przy trafieniu w bezruchu otrzymywane <color=#fe4b48>Obrażenia</color> -2 (minimalnie 1 <color=#fe4b48>Obrażenie</color>)
295. [RPG [I990423] — opis] 태양이 내는 빛이 부러워 조명이 되었다. 하지만 조명은 태양보다 사람 곁에 있어야 한다. 태양은 너무 눈부시고 뜨겁기에 조명처럼 곁에 둘 수가 없다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990423].description
   limit: do 210 znaków
   EN: Envious of the sun's radiance, it became a lamp. Yet a lamp must stay closer to people than the sun, because the sun is too dazzling and hot to keep at one's side.
   PL: Z zazdrości o blask słońca stała się lampą. Ale lampa musi być bliżej ludzi niż słońce — słońce jest zbyt oślepiające i zbyt gorące, by trzymać je przy sobie.
296. [RPG [I990808] — nazwa wyświetlana] 구수한 거예요
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990808].displayName
   limit: do 40 znaków
   EN: It's Toasty, You Hear?
   PL: To Swojski Smak, Słyszysz?
297. [RPG [I990808] — statystyki przedmiotu] 상징계에서 적 처치 시 상징계 <color=#00ff9c>체력</color> 3 <color=#00ff9c>회복</color> (쿨타임 4초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990808].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>
   EN: In the Symbolic, <color=#00ff9c>heals</color> 3 Symbolic <color=#00ff9c>HP</color> upon killing an enemy (4 seconds cooldown)
   PL: W Symbolicznym po zabiciu wroga <color=#00ff9c>leczy</color> 3 Symboliczne <color=#00ff9c>HP</color> (odnowienie 4 s)
298. [RPG [I990808] — opis] 구수함은 맛이 아닌 냄새예요. 냄새와 맛은 다르지만 서로 붙어있어요. 언젠간 냄새만으로 된 요리를 만들 거예요. 그러면 여기 있는 모두를 먹일 수 있는 거예요!
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990808].description
   limit: do 330 znaków
   EN: Toasty is an aroma, not a flavor, you hear? Aroma and taste are different, but they cling together, you hear? Someday, I'll cook a dish made only of aroma, you hear?  Then everyone here can have their fill without worrying about food running out, you hear?
   PL: Swojskość to aromat, nie smak, słyszysz? Aromat i smak to co innego, ale trzymają się razem, słyszysz? Kiedyś ugotuję potrawę z samego aromatu, słyszysz? I wtedy nakarmię do syta wszystkich tu obecnych, słyszysz?
299. [RPG [I990807] — nazwa wyświetlana] 감칠맛인 거예요
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990807].displayName
   limit: do 40 znaków
   EN: It's Savory, You Hear?
   PL: To Umami, Słyszysz?
300. [RPG [I990807] — statystyki przedmiotu] 상징계 공격의 <color=#fe4b48>공격 속도</color> +15%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990807].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>
   EN: <color=#fe4b48>Attack Speed</color> +15% in the Symbolic
   PL: <color=#fe4b48>Szybkość Ataku</color> +15% w Symbolicznym
301. [RPG [I990807] — opis] 감칠맛은 입맛을 돋우는 맛이에요. 입맛이 돋우어지면 다음 음식이 먹고 싶게 해요. 다음 음식을 먹고 싶어지는 건 다음에 다가올 맛을 기대하는 거예요. 그러니까 감칠맛은 기대의 맛인 거예요!
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990807].description
   limit: do 310 znaków
   EN: Savory flavor really brings up the appetite, you hear? Once you feel that appetite, you start craving the next dish, you hear? Craving the next dish means looking forward to the next flavor, you hear? So, savory means anticipation, you hear?
   PL: Umami pobudza apetyt, słyszysz? A gdy apetyt rośnie, chce się kolejnego jedzenia, słyszysz? Chęć na kolejne jedzenie to oczekiwanie kolejnego smaku, słyszysz? Czyli umami to smak oczekiwania, słyszysz?
302. [RPG [I990113] — nazwa wyświetlana] 르루주의 SPA 숄더백
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990113].displayName
   limit: do 50 znaków
   EN: Le Rouge Casualwear Shoulder Bag
   PL: Torba Przez Ramię SPA Le Rouge
303. [RPG [I990113] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990113].statText
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [RPG [I990113] — opis] 균열에 채워진 황금가죽을 먹어본 적 있나요? 그 가죽으로 맛을 낸 옷은… 정말 잊을 수 없죠.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990113].description
   limit: do 190 znaków
   EN: Have you ever tasted the Golden Hide packed into the cracks? Oh, clothes seasoned with that hide... now that is a flavor one can never forget.
   PL: Gustowałeś kiedyś w Złotej Skórze wcisniętej w pęknięcia? Ubrania doprawione tą skórą… naprawdę trudno zapomnieć.
305. [RPG [I990114] — nazwa wyświetlana] 르루주의 SPA 후드티
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990114].displayName
   limit: do 40 znaków
   EN: Le Rouge Casualwear Hoodie
   PL: Hoodie SPA Le Rouge
306. [RPG [I990114] — statystyki przedmiotu] 상징계 공격 <color=#fe4b48>피해량</color> +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990114].statText
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [RPG [I990114] — opis] 황금가죽을 뜯어먹다가, 균열이 더 커질 때도 있어요. 그럴 때는 이 황금가죽을 멋대로 통제하려던 르누아르 놈들을 그 균열 안에 쑤셔 메꾸면… 되는 거죠.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990114].description
   limit: do 270 znaków
   EN: Sometimes, gnawing away at the Golden Hide makes the crack wider. When that happens, you catch these nasty Noirs who tried to control the Hide. Stuff them into the gap, plug it up... And voilà, problem solved.
   PL: Czasem, gdy obgryza się Złotą Skórę, pęknięcie robi się większe. Wtedy łapie się te paskudne Le Noir, które próbowały zawładnąć Skórą, wpierdala je w szczelinę i zatyka… i już, problem z głowy.
308. [RPG [I990115] — nazwa wyświetlana] 르루주의 컨템포러리 캡 모자
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990115].displayName
   limit: do 40 znaków
   EN: Le Rouge Contemporary Cap
   PL: Czapka z Daszkiem Contempora Le Rouge
309. [RPG [I990115] — statystyki przedmiotu] 상징계에서 <color=#F8C200>회피</color> 해금\n- <color=#F8C200>회피 버튼(Z 키)</color>을 누르면 이동 방향(정지 중이면 바라보는 방향)으로 1칸 <color=#F8C200>회피</color> (쿨타임 0.5초)\n- <color=#F8C200>회피</color> 중 0.2초 동안 <color=#F8C200>무적</color>, 공격 중에도 발동 가능
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990115].statText
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: In the Symbolic, unlocks <color=#F8C200>Evade</color>\n- Press the <color=#F8C200>Evade button (Z on keyboard)</color> to <color=#F8C200>Evade</color> 1 tile in the direction of movement, or the direction currently faced while stationary (0.5 seconds cooldown)\n- <color=#F8C200>Evade</color> triggers <color=#F8C200>Invul. Frame</color> for 0.2 seconds and can also be activated during attacks
   PL: W Symbolicznym odblokowuje <color=#F8C200>Unik</color>\n- Naciśnij <color=#F8C200>przycisk uniku (Z na klawiaturze)</color>, aby wykonać <color=#F8C200>Unik</color> o 1 pole w kierunku ruchu (lub w kierunku patrzenia w bezruchu) (odnowienie 0.5 s)\n- Podczas <color=#F8C200>Uniku</color> przez 0.2 s zyskuje <color=#F8C200>Niewrażliwość</color>; możliwe również podczas ataku
310. [RPG [I990115] — opis] 누군가는 생각했다. 백화점이 세워지기 전, 이 자리에는 무엇이 있었을까? 허나 그 생각은 곧 모자에 담겨 가라앉았다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990115].description
   limit: do 190 znaków
   EN: Someone once wondered, "What stood here before the Grand Magasin was built?" The thought was soon placed inside a cap, where it sank out of sight.
   PL: Ktoś kiedyś się zastanowił: co stało na tym miejscu, zanim wzniesiono Grand Magasin? Lecz ta myśl wkrótce utonęła w czapce, w którą ją schowano.
311. [RPG [I990116] — nazwa wyświetlana] 르루주의 컨템포러리 장갑
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990116].displayName
   limit: do 40 znaków
   EN: Le Rouge Contemporary Gloves
   PL: Rękawiczki Contempora Le Rouge
312. [RPG [I990116] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990116].statText
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [RPG [I990116] — opis] 황금가죽은 먹을 수도 있고 두를 수도 있습니다. 가죽은 살결 그 자체이니, 말 그대로 살아 숨 쉬고 있죠. 우리의 피부와 다를 게 없이.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990116].description
   limit: do 200 znaków
   EN: The Golden Hide may be consumed or worn. Hide is flesh itself; it quite literally lives and breathes. It is no different from the skin of our own bodies.
   PL: Złotą Skórę można jeść, można nosić. Skóra to samo ciało — dosłownie żyje i oddycha. Nie różni się od skóry naszych ciał.
314. [RPG [I990111] — nazwa wyświetlana] 르누아르의 컨템포러리 장목 양말
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990111].displayName
   limit: do 50 znaków
   EN: Le Noir Contemporary Long Socks
   PL: Długie Skarpety Contempora Le Noir
315. [RPG [I990111] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Garde</color> 2단계 해금\n- 2단계 <color=#F8C200>Garde</color> 시간: 2.5초\n- 2단계 <color=#F8C200>Garde</color> <color=#fe4b48>피해량</color>: 상징계 공격의 <color=#fe4b48>피해량</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990111].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: Unlocks Level 2 <color=#F8C200>Garde</color> in the Symbolic\n- <color=#F8C200>Garde</color> Time: 2.5 seconds\n- <color=#F8C200>Garde</color> <color=#fe4b48>Damage</color>: Attack <color=#fe4b48>Damage</color> +2 in the Symbolic
   PL: Odblokowuje <color=#F8C200>Garde</color> 2. poziomu w Symbolicznym\n- Czas <color=#F8C200>Garde</color> 2. poziomu: 2.5 s\n- <color=#fe4b48>Obrażenia</color> <color=#F8C200>Garde</color> 2. poziomu: <color=#fe4b48>Obrażenia</color> ataku w Symbolicznym +2
316. [RPG [I990111] — opis] 오오 균열이 메워진다. 오오 황금빛으로 균열이 메워진다. 저건 황금의 송진…
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990111].description
   limit: do 120 znaków
   EN: Oh, the crack is closing. Sealing the breach is the gold—the Resin of Gold.
   PL: O, pęknięcie się zasklepia. O, zasklepia się złotym blaskiem. To Złota Żywica…
317. [RPG [I990112] — nazwa wyświetlana] 르누아르의 컨템포러리 넥타이 핀
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990112].displayName
   limit: do 40 znaków
   EN: Le Noir Contemporary Tiepin
   PL: Spinka do Krawata Contempora Le Noir
318. [RPG [I990112] — statystyki przedmiotu] 상징계에서 <color=#F8C200>저스트 가드</color> 해금\n- 발동 조건: <color=#F8C200>가드</color> 버튼을 누른 뒤 0.3초 안에 <color=#F8C200>가드</color> 방향으로 <color=#F8C200>가드</color> 시 받는 <color=#fe4b48>피해량</color>이 0이 됨
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990112].statText
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: Unlocks <color=#F8C200>Perfect Block</color> in the Symbolic\n- Trigger Condition: Within 0.3 seconds of pressing the <color=#F8C200>Block</color> button, <color=#F8C200>Blocking</color> in the <color=#F8C200>Block</color> direction reduces incoming <color=#fe4b48>Damage</color> to 0
   PL: Odblokowuje <color=#F8C200>Perfekcyjny Blok</color> w Symbolicznym\n- Warunek: jeśli w ciągu 0.3 s od naciśnięcia przycisku <color=#F8C200>Bloku</color> <color=#F8C200>Blokujesz</color> w kierunku <color=#F8C200>Bloku</color>, otrzymywane <color=#fe4b48>Obrażenia</color> spadają do 0
319. [RPG [I990112] — opis] 황금송진을 지킨다. 그리고 황금송진은 백화점의 붕괴를 막아준다. 단순한 인과다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990112].description
   limit: do 170 znaków
   EN: Protect the Golden Resin. The Golden Resin, in turn, keeps the Grand Magasin from collapsing. A simple chain of cause and effect.
   PL: Strzeże Złotej Żywicy. A Złota Żywica chroni Grand Magasin przed zawaleniem. Prosty związek przyczyny i skutku.
320. [RPG [I990418] — nazwa wyświetlana] 르누아르 신발관 윙팁 구두
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990418].displayName
   limit: do 50 znaków
   EN: Le Noir Footwear Hall Wingtip Shoes
   PL: Buty Wingtip z Salonu Obuwia Le Noir
321. [RPG [I990418] — statystyki przedmiotu] 상징계에서 2단계 이상 <color=#F8C200>Garde</color> 시 3칸 <color=#F8C200>돌진</color>\n- 경로에 장애물이 있으면 그 앞에서 멈춤
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990418].statText
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: In the Symbolic, using Level 2 or higher <color=#F8C200>Garde</color> triggers <color=#F8C200>Dash</color> 3 tiles forward\n- Stops early if an obstacle blocks the path
   PL: W Symbolicznym <color=#F8C200>Garde</color> 2. poziomu lub wyższego uruchamia <color=#F8C200>Szarżę</color> o 3 pola\n- Zatrzymuje się przed przeszkodą, jeśli stoi na drodze
322. [RPG [I990418] — opis] 구두는 착용자를 완벽히 보호해야 한다. 흔들림 없이 꼿꼿하게 대지에 설 수 있도록 받쳐줘야 한다. 세상은 위험하기에 불안정한 곳에서 안정을 찾아줄 최후의 보루가 구두다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990418].description
   limit: do 250 znaków
   EN: A shoe must protect its wearer without fault. It must hold them upright upon the earth, steady and unshaken. The world is dangerous; on unstable ground, the shoe is the final bastion of stability.
   PL: Buty muszą doskonale chronić noszącego. Muszą podtrzymywać go na ziemi, pewnie i bez chwiania. Świat jest niebezpieczny — na niestabilnym gruncie buty są ostatnim bastionem stabilności.
323. [RPG [I990419] — nazwa wyświetlana] 르누아르 신발관 구두약
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990419].displayName
   limit: do 50 znaków
   EN: Le Noir Footwear Hall Shoe Polish
   PL: Pasta do Butów z Salonu Obuwia Le Noir
324. [RPG [I990419] — statystyki przedmiotu] 상징계 <color=#F8C200>Garde</color> 속도 +25%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990419].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: Symbolic <color=#F8C200>Garde</color> Speed +25%
   PL: <color=#F8C200>Szybkość Garde</color> +25% w Symbolicznym
325. [RPG [I990419] — opis] 취급 안내: 르누아르의 구두는 돌로 만들어집니다. 돌로 만든 구두는 단단해서 부서지지 않습니다. 하지만 스크래치가 많이 나기에 구두약으로 가려줘야 합니다. 스크래치가 많은 구두는 낡아 보이고 낡아 보이는 구두는 내구성이 약해 보여지기에, 부서질 수 있습니다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990419].description
   limit: do 370 znaków
   EN: Care Instructions: Noir shoes are made of stone. Stone shoes are hard and do not break. However, they scratch easily, so you must conceal marks with polish. Heavily scratched shoes look old; old-looking shoes appear structurally fragile, and structurally fragile-looking shoes may break.
   PL: Instrukcja: buty Le Noir wykonane są z kamienia. Kamienne buty są twarde i nie łamią się. Łatwo jednak porysować ich powierzchnię, dlatego trzeba ją maskować pastą. Obute porysowane buty wyglądają na stare, stare buty wyglądają na kruche, a kruche buty mogą się złamać.
326. [RPG [I990811] — nazwa wyświetlana] 떡밥
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990811].displayName
   limit: do 40 znaków
   EN: Paste Bait
   PL: Zanęta
327. [RPG [I990811] — statystyki przedmiotu] 상징계 <color=#00ff9c>체력</color> +4\n\n상징계에서 2단계 <color=#F8C200>Garde</color>가 <color=#F8C200>콤보 2타 공격</color>으로 발동\n- 동작·효과 모두 <color=#F8C200>콤보 2타 공격</color>으로 적용
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990811].statText
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#F8C200>, \n
   EN: Symbolic <color=#00ff9c>HP</color> +4\n\nIn the Symbolic, activates Level 2 <color=#F8C200>Garde</color> as <color=#F8C200>Attack Chain 2</color>\n- All motions and effects are applied as <color=#F8C200>Attack Chain 2</color>
   PL: Symboliczne <color=#00ff9c>HP</color> +4\n\nW Symbolicznym <color=#F8C200>Garde</color> 2. poziomu uruchamia <color=#F8C200>Atak Kombo 2</color>\n- Ruch i efekty stosowane jak przy <color=#F8C200>Ataku Kombo 2</color>
328. [RPG [I990811] — opis] 떠밀려 오기까지 숨이 붙어 있던 유체들은 떡밥의 냄새를 맡고 해변까지 기어오르려 했지만 끝내 해변에서 익어버렸다. 이곳은 물 밖이기 때문에 아쿠아리움의 시대는 끝났고 이제는 백화점의 시대를 지새우고 있다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990811].description
   limit: do 370 znaków
   EN: The larvae that survived long enough to wash ashore caught the scent of chum. They tried to crawl onto the Shore, only to be cooked in the heat of the open air. This is a world outside the waters. The Age of the Aquarium is over, and the Age of the Department Store must now be endured.
   PL: Larwy, które przeżyły drogę aż na brzeg, poczuły zapach zanęty i próbowały czołgać się na brzeg — lecz ugotowały się w powietrzu. To świat spoza wody. Era Akwarium się skończyła; teraz trwa era Grand Magasin i trzeba ją przetrwać.
329. [RPG [I990812] — nazwa wyświetlana] 해변의 검은 물
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990812].displayName
   limit: do 40 znaków
   EN: Black Water of the Shore
   PL: Czarna Woda Brzegu
330. [RPG [I990812] — statystyki przedmiotu] 상징계에서 뿌이의 <color=#F8C200>검은 물 투사체</color> 해금\n- 5칸 이내의 가장 가까운 적에게 발사 (쿨타임 2.5초)\n- 적중한 적은 3초 동안 총 2만큼 <color=#fe4b48>피해</color>를 받음\n\n그림자계 전투에서 뿌이의 맥동 위력 +1\n- '힘내' 사용 후 폭주 상태이고 맥동 횟수가 10 이상이면, 10 소모하고 대상에게 <color=#F8C200>기본 위력 증가</color> 1 부여\n- '아프지마' 사용 시 맥동 위력 3 이상이면 가중치 +2, 적중 시 스킬 위력만큼 정신력 회복\n- '붉은못 세례' 해금 (적 3명 공격)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990812].statText
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, unlocks Pwie's <color=#F8C200>Blackwater Projectile</color>\n- Fires at the nearest enemy within 5 tiles (2.5 seconds cooldown)\n- On hit, deals a total of 2 <color=#fe4b48>Damage</color> over 3 seconds\n\nIn Shadowed Battle, Pwie's Pulsation Potency +1\n- After using "Perk Up", if in Uncontrollable Rampage and at 10+ Pulsation Count, consume 10 Pulsation Count to apply 1 <color=#F8C200>Base Power Up</color> on the target\n- When using "Don't Get Hurty" and at 3+ Pulsation Potency, gain Atk Weight +2; On Hit, heal SP equal to Skill Power\n- Unlocks "Baptism of Crimson Nails" (attacks 3 enemies)
   PL: W Symbolicznym odblokowuje <color=#F8C200>Pocisk Czarnej Wody</color> Pwie\n- Wystrzeliwuje w najbliższego wroga w promieniu 5 pól (odnowienie 2.5 s)\n- Trafiony wróg otrzymuje łącznie 2 <color=#fe4b48>Obrażenia</color> w ciągu 3 sekund\n\nW walce w Zacienionym Moc Pulsacji Pwie +1\n- Po użyciu „Ożyw się”, jeśli Pwie jest w Niepowstrzymanym Szale i ma Licznik Pulsacji 10+, zużywa 10 Licznika Pulsacji i nakłada na cel 1 <color=#F8C200>Zwiększenie Mocy Podstawowej</color>\n- Użycie „Nie Bolej” przy Mocy Pulsacji 3+: Waga Ataku +2; przy trafieniu leczy SP równy Mocy Umiejętności\n- Odblokowuje „Chrzest Szkarłatnych Gwoździ” (atakuje 3 wrogów)
331. [RPG [I990812] — opis] 너무 많은 것을 태어나게 해버렸다. 그렇기에 그것의 죄는 무겁다. 많은 것을 태어나게 해버린 것은 그만큼을 죽인 것과 같다. 그래서 검은 실에서 헤엄치던 옛 존재는 가장 낮은 곳에서 조용히 알을 품으며 죄를 늘려갔다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990812].description
   limit: do 350 znaków
   EN: It brought far too many things into being, and thus, grave is its sin. To give birth to so much is no different from killing just as much. And so the thing of eld that once swam through the Blackthread quietly brooded over its eggs at the lowest depths, propagating its sins.
   PL: Narodziła zbyt wiele. Dlatego jej grzech jest ciężki. Zrodzenie tyleż znaczy tyle, co zabicie tyleż. A więc dawna istota, która niegdyś pływała w Czarnej Nici, cichutko wysiadywała jaja na samym dnie, powiększając grzechy.
332. [RPG [I991019] — nazwa wyświetlana] 탄닌
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991019].displayName
   limit: do 40 znaków
   EN: Tannin
   PL: Garbnik
333. [RPG [I991019] — statystyki przedmiotu] 상징계 <color=#F8C200>Garde</color>의 <color=#fe4b48>피해량</color> +3
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991019].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, <color=#F8C200>Garde</color> <color=#fe4b48>Damage</color> Dealt +3
   PL: W Symbolicznym <color=#fe4b48>Obrażenia</color> <color=#F8C200>Garde</color> +3
334. [RPG [I991019] — opis] 백화점 가장 밑에서는 냄새나고 잔혹한 가죽공정이 이뤄진다. 가죽은 생명의 흔적을 덮어쓰는 것. 하지만 가죽 그 자체로는 부패할 뿐. 무두질을 거쳐 가죽은 생전의 온기가 아닌 섬유질의 뭉치가 되어 다른 무언가가 된다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991019].description
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the very bottom of the department store, foul-smelling, brutal leatherwork takes place.\n\nHide is what remains after the traces of life have been stripped away. Left as it is, however, it does nothing but rot. Only through tanning does it cease to be something that still carries the warmth of the living, becoming instead a dense mass of fibers... something else entirely.
   PL: Na samym dole Grand Magasin odbywa się śmierdząca, brutalna praca nad skórami.\nSkóra to to, co zostaje po zatarto ślady życia. Ale pozostawiona sobie — nic poza gniciem. Dopiero garbowanie odbiera jej ciepło żywej istoty: staje się zbitek włókien i zmienia się w coś innego.
335. [RPG [I991020] — nazwa wyświetlana] 크롬염
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991020].displayName
   limit: do 40 znaków
   EN: Chromium Salt
   PL: Sól Chromowa
336. [RPG [I991020] — statystyki przedmiotu] 상징계 <color=#F8C200>Garde</color>의 <color=#F8C200>돌진</color> 속도 +30%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991020].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, <color=#F8C200>Garde</color> <color=#F8C200>Dash</color> Speed +30%
   PL: W Symbolicznym <color=#F8C200>Szybkość Szarży</color> <color=#F8C200>Garde</color> +30%
337. [RPG [I991020] — opis] 가죽을 가공하기 위해서 빠른 방법과 느린 방법이 있다. 빠른 무두질을 위해 크롬에 가죽을 담가 무두질을 진행했을 때 가죽은 자연상태에서 연이 없던 금속을 속에 스미게 하고 굳어간다. 빠르지만 빠르게 시간을 당겨온 만큼 오래가지 못한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991020].description
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are fast ways and slow ways to process hides. In chrome tanning, the hide is steeped in chromium to hasten the process, drawing into itself a metal it would never have encountered in nature as it hardens.\n\nIt is fast, but having dragged time forward to gain that speed, it does not endure for long.
   PL: Do obróbki skór są metody szybkie i powolne. Przy garbowaniu chromowym skórę zanurza się w chromie, by przyśpieszyć proces — wsiąka w nią metal, jakiego nigdy nie spotkałaby w naturze, i twardnieje.\nTo szybkie, ale skoro przyspieszono czas, szybko przemija.
338. [RPG [I991021] — nazwa wyświetlana] 오일
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991021].displayName
   limit: do 40 znaków
   EN: Oil
   PL: Olej
339. [RPG [I991021] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Garde</color> 중 <color=#F8C200>가드</color> 효과 적용\n\n상징계 <color=#00ff9c>체력</color> +4
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991021].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, applies the <color=#F8C200>Block</color> effect during <color=#F8C200>Garde</color>\n\nSymbolic <color=#00ff9c>HP</color> +4
   PL: W Symbolicznym podczas <color=#F8C200>Garde</color> działa efekt <color=#F8C200>Bloku</color>\n\nSymboliczne <color=#00ff9c>HP</color> +4
340. [RPG [I991021] — opis] 가죽을 식물성 성분에 절여 천천히 무두질한다. 인내와 시간이 필요한 만큼 이 긴 공정을 지샌 가죽은 더 오랜 시간을 견딜 수 있다. 가죽은 무엇보다 육식적이지만 이렇게 만들어진 가죽은 베지탠 가죽이라 불린다. 육식 속에 채식을 넣어 완성시킨다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991021].description
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The hide is steeped in plant-based tanning agents and cured slowly. It demands patience and time, but leather that endures such a lengthy process can, in turn, endure for far longer. Hide is, above all else, carnivorous in origin. And yet leather made this way is called veg-tan leather. It is finished by putting the vegetable into the carnivorous.
   PL: Skórę zanurza się w roślinnych środkach garbnikowych i powoli garbuje. Wymaga cierpliwości i czasu, ale skóra, która przetrwała taki długi proces, wytrzymuje znacznie dłużej. Skóra z natury jest drapieżna — lecz skóra wytworzona tą metodą nazywana jest skórą wegetariańską. Drapieżność dopełnia się roślinnością.
341. [RPG [I990316] — nazwa wyświetlana] 르루주 부티크 귀걸이
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990316].displayName
   limit: do 40 znaków
   EN: Boutique du Rouge Earrings
   PL: Kolczyki Boutique du Rouge
342. [RPG [I990316] — statystyki przedmiotu] 상징계 공격의 <color=#fe4b48>공격 속도</color> +10%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990316].statText
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [RPG [I990316] — opis] 튀는 소리, 따뜻한 피, 육즙이 흐르는 고기, 기대되는 맛과 경험들.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990316].description
   limit: do 140 znaków
   EN: A sharp sizzle. Warm blood. Meat running with juice. Anticipation of flavors and experiences yet to come.
   PL: Skwierczenie, ciepła krew, mięso pełne soków, oczekiwane smaki i doświadczenia.
344. [RPG [I990420] — nazwa wyświetlana] 르루주 신발관 샌들
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990420].displayName
   limit: do 50 znaków
   EN: Le Rouge Footwear Hall Sandals
   PL: Sandały z Salonu Obuwia Le Rouge
345. [RPG [I990420] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Avant</color> 발동 시 그 공격의 <color=#fe4b48>피해량</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990420].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, <color=#F8C200>Avant</color> <color=#fe4b48>Damage</color> Dealt +2
   PL: W Symbolicznym uruchomienie <color=#F8C200>Avant</color> zadaje <color=#fe4b48>Obrażenia</color> +2
346. [RPG [I990420] — opis] 발이 많으면 신발을 많이 신을 수 있으니 좋은 거 아닌가? 언제부터 다리가 적은 게 신발관의 명예가 된 건지 이해할 수가 없어. 예전에는 다리가 많을수록 좋았는데, 말세는 말세인가 보다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990420].description
   limit: do 300 znaków
   EN: More feet mean more shoes to wear. Isn't that a good thing? Since when has having fewer legs become a mark of honor in the Footwear Hall? In the old days, the more legs one had, the better it was. Seriously, what's the world coming to?
   PL: Im więcej nóg, tym więcej butów można nosić — to chyba dobrze, nie? Od kiedy mało nóg stało się zaszczytem Salonu Obuwia? Kiedyś więcej nóg znaczyło lepiej. Koniec świata to koniec świata, widocznie.
347. [RPG [I990421] — nazwa wyświetlana] 르루주 신발관 운동화 끈
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990421].displayName
   limit: do 50 znaków
   EN: Le Rouge Footwear Hole Shoelaces
   PL: Sznurówki do Sneakerów z Salonu Obuwia Le Rouge
348. [RPG [I990421] — statystyki przedmiotu] 상징계에서 <color=#F8C200>회피</color> 횟수 +1
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990421].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, successive <color=#F8C200>Evade</color> Use +1
   PL: W Symbolicznym liczba kolejnych <color=#F8C200>Uników</color> +1
349. [RPG [I990421] — opis] 끈은 신발의 입을 다물어 혀를 가려준다. 또한 입을 단단히 꿰매어 풀리지 않게 조여준다. 그렇게 꼭꼭 조여지면 말은 못 할지언정 내 발의 모양이 드러난다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990421].description
   limit: do 310 znaków
   EN: Laces close the shoe's mouth and hide its tongue. They stitch the mouth shut and pull it tight so that it cannot come undone. Bound so firmly, the shoe may be unable to speak... But this allows for the shape of one's foot to be laid bare.
   PL: Sznurówki zamykają butowi usta i chowają jego język. Szyją usta na gęsto i zaciskają, by się nie rozwiązały. Tak ciasno związany but może nie umieć mówić... ale dzięki temu obnaża się kształt stopy.
350. [RPG [I990426] — nazwa wyświetlana] 르루주 가방관 버클
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990426].displayName
   limit: do 50 znaków
   EN: Le Rouge Handbags Hall Buckle
   PL: Klamra z Salonu Torebek Le Rouge
351. [RPG [I990426] — statystyki przedmiotu] 상징계에서 <color=#F8C200>콤보 2타 공격</color> 적중 시 상징계 <color=#00ff9c>체력</color> 1 <color=#00ff9c>회복</color>
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990426].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>
   EN: In the Symbolic, landing <color=#F8C200>Attack Chain 2</color> <color=#00ff9c>heals</color> 1 <color=#00ff9c>HP</color>
   PL: W Symbolicznym trafienie <color=#F8C200>Atakiem Kombo 2</color> <color=#00ff9c>leczy</color> 1 Symboliczne <color=#00ff9c>HP</color>
352. [RPG [I990426] — opis] 가죽 조각들 사이에 끼어든 이질적인 쇳조각. 버클은 가죽만으로는 할 수 없는 기능을 위해 존재한다. 가죽은 살이고, 버클은 뼈다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990426].description
   limit: do 190 znaków
   EN: An alien shard of metal wedged between pieces of hide. The buckle exists to perform what hide alone cannot. Hide is flesh. The buckle is bone.
   PL: Obca blaszka wciśnięta między kawałki skóry. Klamra istnieje po to, by spełniać to, czego sama skóra nie potrafi. Skóra jest ciałem, a klamra kością.
353. [RPG [I990424] — nazwa wyświetlana] 르루주 가방관 토트백
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990424].displayName
   limit: do 50 znaków
   EN: Le Rouge Handbags Hall Tote Bag
   PL: Torba Tote z Salonu Torebek Le Rouge
354. [RPG [I990424] — statystyki przedmiotu] 상징계에서 <color=#F8C200>패링</color> 성공 시 3칸 이내의 가장 가까운 적에게 2만큼 <color=#fe4b48>피해</color> 입히는 <color=#F8C200>유도 투사체</color> 1개 발사
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990424].statText
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, upon a successful <color=#F8C200>Parry</color>, fires 1 <color=#F8C200>Homing Projectile</color> at the nearest enemy within 3 tiles, dealing 2 <color=#fe4b48>Damage</color>
   PL: W Symbolicznym udany <color=#F8C200>Parry</color> wystrzeliwuje 1 <color=#F8C200>Pocisk Naprowadzający</color> w najbliższego wroga w promieniu 3 pól, zadający 2 <color=#fe4b48>Obrażenia</color>
355. [RPG [I990424] — opis] 이 토트백 안에는 무엇이든 넉넉히 담을 수 있다. 가죽으로 만든 가방은 담긴 물건만큼 늘어난다. 하지만 가죽은 늘어나지 않는다. 가죽은 부드러워지기만 한다. 늘어나는 것처럼 보일 뿐이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990424].description
   limit: do 270 znaków
   EN: This tote has plenty of room and can hold anything without issue. Bags made of hide may seem stretched to match the size of whatever is inside, but the hide does not truly stretch. It merely grows more pliant.
   PL: Do tej torby tote zmieści się wszystko, co trzeba. Torebki ze skóry rozciągają się na tyle, ile niesie. Ale skóra się nie rozciąga. Skóra tylko mięknie. Wydaje się, że się rozciąga.
356. [RPG [I990425] — nazwa wyświetlana] 르루주 가방관 숄더백
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990425].displayName
   limit: do 50 znaków
   EN: Le Rouge Handbags Hall Shoulder Bag
   PL: Torba Przez Ramię z Salonu Torebek Le Rouge
357. [RPG [I990425] — statystyki przedmiotu] 상징계에서 <color=#F8C200>패링</color> 성공 시 <color=#F8C200>패링</color>한 대상에게 가하는 <color=#fe4b48>피해량</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990425].statText
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, upon a successful <color=#F8C200>Parry</color>, <color=#fe4b48>Damage</color> Dealt +2 against the target whose attack is <color=#F8C200>Parried</color>
   PL: W Symbolicznym udany <color=#F8C200>Parry</color> zadaje <color=#fe4b48>Obrażenia</color> +2 celowi, którego atak został <color=#F8C200>sparowany</color>
358. [RPG [I990425] — opis] 르루주가 붉은 신을 빚기로 결심했을 때 수많은 가방이 동원됐다. 가방을 해체하여 얻은 가죽은 요람의 일부가 될 수 있었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990425].description
   limit: do 230 znaków
   EN: When the Rouges resolved to fashion the Crimson God, countless bags were requisitioned. The hide stripped from their dismantled bodies had the honor of becoming part of the Cradle.
   PL: Kiedy Le Rouge postanowiły ulepić Szkarłatnego Boga, zarekwirowano niezliczone torby. Skóra zdjęta z ich rozebranych ciał miała zaszczyt stać się częścią Kołyski.
359. [RPG [I990427] — nazwa wyświetlana] 르누아르 가방관 클러치백
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990427].displayName
   limit: do 50 znaków
   EN: Le Noir Handbags Hall Clutch Bag
   PL: Kopertówka z Salonu Torebek Le Noir
360. [RPG [I990427] — statystyki przedmiotu] 상징계에서 근접 공격을 <color=#F8C200>가드</color>하면 공격자에게 3만큼 <color=#fe4b48>피해</color> 입힘
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990427].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, <color=#F8C200>Blocking</color> a melee attack deals 3 <color=#fe4b48>Damage</color> to the attacker
   PL: W Symbolicznym <color=#F8C200>Zablokowanie</color> ataku wręcz zadaje atakującemu 3 <color=#fe4b48>Obrażenia</color>
361. [RPG [I990427] — opis] 백화점 안의 재료로 신을 만든다 해도, 그 거인은 백화점의 규칙을 벗어날 순 없을 거다. 다른 신들과 같은 권능을 지니려면 적어도 이 백화점에서, 백화점의 재료로 태어나선 안 되었지.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990427].description
   limit: do 360 znaków
   EN: Countless materials may be dedicated to the creation of a god, but the resulting Giant will never be able to escape the Grand Magasin's laws. To wield authority equal to that of other gods, it should never have been born here. Not as just another material for the department store.
   PL: Nawet gdyby ulepić boga z materiałów wewnątrz Grand Magasin, ten Gigant nie wymknie się z jego praw. Aby dzierżyć władzę równą innym bogom, nie powinien był się tu w ogóle narodzić — nie jako kolejny materiał Grand Magasin.
362. [RPG [I990428] — nazwa wyświetlana] 르누아르 가방관 백팩
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990428].displayName
   limit: do 50 znaków
   EN: Le Noir Handbags Hall Backpack
   PL: Plecak z Salonu Torebek Le Noir
363. [RPG [I990428] — statystyki przedmiotu] 상징계에서 <color=#F8C200>저스트 가드</color> 성공 시 뫼르소 주위 1칸에 2만큼 <color=#fe4b48>피해</color> 입히는 <color=#F8C200>추가 공격</color> 발동 (경직 0.1초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990428].statText
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, upon a successful <color=#F8C200>Perfect Block</color>, triggers an <color=#F8C200>Extra Attack</color> that deals 2 <color=#fe4b48>Damage</color> within 1 tile of Meursault (0.1 seconds Hitstun)
   PL: W Symbolicznym udany <color=#F8C200>Perfekcyjny Blok</color> uruchamia <color=#F8C200>Dodatkowy Atak</color> zadający 2 <color=#fe4b48>Obrażenia</color> w promieniu 1 pola od Meursaulta (0.1 s Hitstun)
364. [RPG [I990428] — opis] 그래도 막아야겠지. 어린 신이어도, 신은 신일 테니. 그것은 르루주들이 황금송진을 더 갉아먹도록 할 것이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990428].description
   limit: do 220 znaków
   EN: Even so, it <i>must</i> be stopped. A fledgling god is still a god. Allow that thing to exist, and it will only drive the Rouges to gnaw away and devour still more Golden Resin.
   PL: Mimo wszystko trzeba to powstrzymać. Bóg, choćby mały, jest bogiem. Pozwolić tej rzeczy istnieć — to tylko zmusić Le Rouge, by obgryzały i pożerały jeszcze więcej Złotej Żywicy.
365. [RPG [I990429] — nazwa wyświetlana] 르누아르 가방관 가방끈
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990429].displayName
   limit: do 50 znaków
   EN: Le Noir Handbags Hall Bag Strap
   PL: Pasek do Torby z Salonu Torebek Le Noir
366. [RPG [I990429] — statystyki przedmiotu] 상징계에서 <color=#F8C200>저스트 가드</color> 성공 시 뫼르소 주위 1칸의 적을 1칸 넉백
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990429].statText
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, upon a successful <color=#F8C200>Perfect Block</color>, knocks back enemies within 1 tile of Meursault by 1 tile
   PL: W Symbolicznym udany <color=#F8C200>Perfekcyjny Blok</color> <color=#F8C200>Odrzuca</color> wrogów w promieniu 1 pola od Meursaulta o 1 pole
367. [RPG [I990429] — opis] 르누아르 브랜드 매니저가 직접 층을 이동할 수 없는 상황이라 빠르게 갈 수 있는 점원들만 명품관으로 보냈다던데. 명품관의 상황이 무사히 수습되었을지나 모르겠군.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990429].description
   limit: do 290 znaków
   EN: They say the Noirs' Brand Manager could not presently move between floors in person, so only the nearest available employees were sent to the Luxury Hall. I wonder whether we managed to bring the situation there under control.
   PL: Podobno Dyrektor Marki Le Noir nie może teraz osobiście przemieszczać się między piętrami, więc do Salonu Prestiżu wysłano tylko tych sprzedawców, którzy mogli dotrzeć najszybciej. Nie wiadomo, czy udało się tam opanować sytuację.
368. [RPG [I990912] — nazwa wyświetlana] 매염제
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990912].displayName
   limit: do 40 znaków
   EN: Mordant
   PL: Zaprawa
369. [RPG [I990912] — statystyki przedmiotu] 상징계에서 <color=#F8C200>달리기</color> 중 지나간 칸에 3초 동안 유지되는 <color=#F8C200>고름 타일</color> 생성\n- 타일 위의 적은 이동 속도 -30%\n\n상징계 <color=#00ff9c>체력</color> +4
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990912].statText
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, <color=#F8C200>Sprinting</color> leaves behind <color=#F8C200>Pus Tiles</color> that last for 3 seconds\n- Enemies standing on these tiles have Movement Speed -30%\n\nSymbolic <color=#00ff9c>HP</color> +4
   PL: W Symbolicznym <color=#F8C200>Bieg</color> zostawia za sobą <color=#F8C200>Kafle Ropy</color> utrzymujące się 3 sekundy\n- Wrogowie stojący na kafelkach tracą 30% Szybkości Ruchu\n\nSymboliczne <color=#00ff9c>HP</color> +4
370. [RPG [I990912] — opis] 한 명은 눈물을 너무나 많이 머금었고 한 명은 단 한 방울의 눈물도 머금지 않고 있다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990912].description
   limit: do 120 znaków
   EN: One carries enough tears to burst; the other, not a drop.
   PL: Jedna nasiąka łzami aż do pęknięcia; druga nie nosi ani kropli.
371. [RPG [I990913] — nazwa wyświetlana] 염재
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990913].displayName
   limit: do 40 znaków
   EN: Dyestuff
   PL: Surowiec Barwiący
372. [RPG [I990913] — statystyki przedmiotu] 상징계에서 <color=#F8C200>콤보 2타 공격</color> 적중 시 <color=#F8C200>추가 공격</color> 발동 (경직 1초)\n- 맞은 적 주위 3칸의 무작위 적 1명에게 4만큼 <color=#fe4b48>피해</color> 입힘\n- 그 <color=#F8C200>추가 공격</color>에 맞은 적 주위 1칸의 무작위 적 1명에게 (80 - 발동 횟수 x 20)% 확률로 다시 발동\n- 연속 발동 가능 (최대 5회, 최소 발동 확률 10%)\n\n상징계 <color=#F8C200>콤보 2타 공격</color>의 사거리 +1칸
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990913].statText
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, landing <color=#F8C200>Attack Chain 2</color> triggers an <color=#F8C200>Extra Attack</color> (1 second Hitstun)\n- Deals 4 <color=#fe4b48>Damage</color> to 1 random enemy within 3 tiles of the enemy hit\n- After triggering the <color=#F8C200>Extra Attack</color>, (80 - trigger count x 20)% chance to trigger again on 1 random enemy within 1 tile of the target hit\n- Can be chained (max 5 times; 10% minimum trigger chance)\n\nIn the Symbolic, <color=#F8C200>Attack Chain 2</color> range +1 tile
   PL: W Symbolicznym trafienie <color=#F8C200>Atakiem Kombo 2</color> uruchamia <color=#F8C200>Dodatkowy Atak</color> (1 s Hitstun)\n- Zadaje 4 <color=#fe4b48>Obrażenia</color> 1 losowemu wrogowi w promieniu 3 pól od trafionego wroga\n- Po <color=#F8C200>Dodatkowym Ataku</color> (80 - liczba wywołań x 20)% szans na ponowne wywołanie na 1 losowym wrogu w promieniu 1 pola od trafionego celu\n- Można łączyć (maks. 5 razy; minimalna szansa wywołania 10%)\n\nW Symbolicznym zasięg <color=#F8C200>Ataku Kombo 2</color> +1 pole
373. [RPG [I990913] — opis] 균열이 생기고 목소리가 새어든 날, 둘은 각각 다른 것을 빌었다. 한 명은 아프지 않기를, 다른 한 명은 슬프지 않기를. 아프지 않게 된 것은 눈물에 젖어도 괜찮아진다. 눈물은 아픔에서 오는 게 아니기에.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990913].description
   limit: do 350 znaków
   EN: On the day cracks formed on the walls, on the day the Voice leached in, the siblings each made a different wish. One wished to never hurt again. The other wished to never be sad again. The one freed from hurt can now be soaked in tears, for it is not pain that draws tears.
   PL: Tego dnia, gdy na murach powstały pęknięcia i wsiąkł w nie Głos, rodzeństwo pomodliło się o co innego. Jedno — by nigdy więcej nie boleć. Drugie — by nigdy więcej nie smutnieć. To, które przestało boleć, może już nasiąkać łzami. Bo łzy nie płyną z bólu.
374. [RPG [I990915] — nazwa wyświetlana] 바늘못
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990915].displayName
   limit: do 40 znaków
   EN: Naildle
   PL: Gwoździk
375. [RPG [I990915] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Avant</color> 공격의 <color=#F8C200>콤보 3타 공격</color> 해금\n- <color=#F8C200>콤보 3타 공격</color> 발동 시 상징계 공격의 <color=#fe4b48>피해량</color> +2, 경직 시간 +0.1초, <color=#00ff9c>체력</color> 1 <color=#00ff9c>회복</color>\n- 그 공격으로 적 처치 시 적이 시체가 되지 않고 5칸 넉백\n- 넉백 중 충돌 시 즉시 그 적 주위 1칸에 2만큼 <color=#fe4b48>피해</color> 입히고 터지면서 시체가 됨\n- 넉백 중 충돌하지 않으면 넉백 종료 위치에서 2만큼 <color=#fe4b48>피해</color> 입히고 터지면서 시체가 됨
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990915].statText
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, <color=#00ff9c>, \n
   EN: In the Symbolic, unlocks <color=#F8C200>Attack Chain 3</color> for <color=#F8C200>Avant</color>\n\n- Upon triggering <color=#F8C200>Attack Chain 3</color>, Symbolic <color=#fe4b48>Damage</color> Dealt +2, Hitstun +0.1s, and <color=#00ff9c>heals</color> 1 <color=#00ff9c>HP</color>\n- Enemies defeated by this attack are knocked back 5 tiles instead of becoming corpses on the spot\n- If the enemy collides during knockback, it immediately explodes, dealing 2 <color=#fe4b48>Damage</color> within 1 tile, then becomes a corpse\n- If no collision occurs, it explodes at the end of the knockback, dealing 2 <color=#fe4b48>Damage</color> within 1 tile, then becomes a corpse
   PL: W Symbolicznym odblokowuje <color=#F8C200>Atak Kombo 3</color> dla <color=#F8C200>Avant</color>\n- Uruchomienie <color=#F8C200>Ataku Kombo 3</color>: <color=#fe4b48>Obrażenia</color> ataku w Symbolicznym +2, Hitstun +0.1 s, <color=#00ff9c>leczy</color> 1 <color=#00ff9c>HP</color>\n- Wróg zabity tym atakiem nie zostaje trupem na miejscu, lecz zostaje odrzucony o 5 pól\n- Przy kolizji podczas odrzutu natychmiast wybucha, zadając 2 <color=#fe4b48>Obrażenia</color> w promieniu 1 pola wokół wroga, i staje się trupem\n- Bez kolizji wybucha w miejscu końca odrzutu, zadając 2 <color=#fe4b48>Obrażenia</color> w promieniu 1 pola, i staje się trupem
376. [RPG [I990915] — opis] 지하 2층의 플로어 매니저는 오랫동안 실을 짜왔다. 백화점이 생기기로 마음먹어진 날부터 옷이 필요했고 실이 필요했다. 실을 오래 뽑고 뽑기 위해 적합한 모습으로 변해갔고 그 의지는 의식 없는 마네킹이 되지 않도록 이자를 지켜주었다. 그 결과 셋으로 분열되었지만 사실은 하나다. 이미 다들 분열되어 있는 건 매한가지다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990915].description
   limit: do 360 znaków
   EN: Over time, the Floor Manager's form warped into a shape suited to the endless turning of the spinning wheel. That same will protected her from becoming a mindless Mannequin, splitting her into three parts. The three are, in fact, one. We, too, are all but wholes of parts ourselves.
   PL: Kierownik Piętra -2 przez lata przędła nić. Od dnia, w którym postanowiono, że powstanie Grand Magasin, potrzebne były ubrania i nić. By prząść ją coraz dłużej, przybrała odpowiedni kształt, a ta wola ochroniła ją przed bezwiednym Manekinem — rozdzieliła ją na trzy części. Te trzy są w istocie jednością. I my jesteśmy zaledwie całościami z części.
377. [RPG [I990916] — nazwa wyświetlana] 물레
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990916].displayName
   limit: do 40 znaków
   EN: Spinning Wheel
   PL: Kołowrotek
378. [RPG [I990916] — statystyki przedmiotu] 상징계에서 뿌이의 <color=#F8C200>바늘 투사체</color> 해금\n- 10칸 이내의 가장 먼 적에게 3만큼 <color=#fe4b48>피해</color> 입히는 투사체 발사 (쿨타임 3초, 경직 0.5초)\n- 적중 시 (100/해당 효과 발동 횟수)% 확률로 주위의 적으로 번짐.\n\n그림자계 전투에서 뿌이의 맥동 위력 +1\n- '저리가' 사용 시 맥동 위력 2당 가중치 +1 (최대 2)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990916].statText
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: Unlocks <color=#F8C200>Needle Projectile</color> in the Symbolic\n- Fires a projectile dealing 3 <color=#fe4b48>Damage</color> against the farthest enemy within 10 tiles (cooldown 3 seconds, 0.5 seconds Hitstun)\n- When the projectile hits, fires another Projectile against a nearby enemy with a (100 / number of times the effect triggers)% chance\n\nDuring battle in the Shadowed, Pwie gains 1 Pulsation Potency\n- On "Go Away" Skill Use, Atk Weight +1 for every 2 Pulsation Potency (max 2)
   PL: W Symbolicznym odblokowuje <color=#F8C200>Pocisk Igły</color> Pwie\n- Wystrzeliwuje pocisk zadający 3 <color=#fe4b48>Obrażenia</color> najdalszemu wrogowi w promieniu 10 pól (odnowienie 3 s, 0.5 s Hitstun)\n- Przy trafieniu (100 / liczba wywołań tego efektu)% szans na wystrzelenie kolejnego pocisku w pobliskiego wroga\n\nW walce w Zacienionym Moc Pulsacji Pwie +1\n- Użycie „Odejdź”: +1 Waga Ataku za każde 2 Moc Pulsacji (maks. 2)
379. [RPG [I990916] — opis] 실을 짜기 위해 물레를 돌린다. 너무 오랫동안 실을 짜와서 인과조차 뒤틀리고 있다. 물레를 돌리기 위해 실을 짜는 것인지, 실을 짜기 위해 물레를 돌리는 것인지 알 수 없다. 이 층에선 무엇 때문인지 중요하지 않다. 실이 짜여졌고 그 실을 누군가 받아갈 수 있는 것만으로도 플로어 매니저는 그 역할을 다한 것이다. 그래서 플로어 매니저가 죽어도 물레는 돌아간다. 실이 나오고 실이 꿰매지기 위해, 이곳에서 저곳으로 통하기 위해 못을 기다리고 있는 것이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990916].description
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n
   EN: They turn the wheel to spin the thread.\n\nThey have done so for so long that causality itself has warped into itself. Does one spin thread to turn the wheel, or turn the wheel to spin thread? The question has become unanswerable, but it does not matter. On this floor, the "why" is of little significance. The Floor Manager's role begins and ends with a singular function: to spin thread and give it to its recipient. Thus, the spinning wheel does not stop even when the spinners die. The thread waits here for the arrival of the nail, to tether the here to the there.
   PL: Kołowrotek kręci się, by prząść nić.\nPrzą tak długo, że skręca się już sama przyczynowość. Nie wiadomo, czy nić przędzie się dla kołowrotka, czy kołowrotek kręci się dla nici. Na tym piętrze „dlaczego” nie ma znaczenia. Rola Kierownika Piętra zaczyna się i kończy jednej funkcji: prząść nić i oddać ją czekającemu. Dlatego kołowrotek kręci się nawet po śmierci prządek. Nić powstaje i czeka, aż ktoś ją przeszyje — czeka na gwóźdź, który połączy tutaj z tamtąd.
380. [RPG [I990422] — nazwa wyświetlana] 유리 의자
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990422].displayName
   limit: do 40 znaków
   EN: Glass Chair
   PL: Szklany Fotel
381. [RPG [I990422] — statystyki przedmiotu] 상징계에서 「원목 테이블」 <color=#F8C200>추가 공격</color>의 범위 +1칸 (상하좌우)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990422].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, 「Solid Wood Table」<color=#F8C200>Extra Attack</color> range +1 tile (both vertical and horizontal)
   PL: W Symbolicznym zasięg <color=#F8C200>Dodatkowego Ataku</color> 「Stółu z Litego Drewna」 +1 pole (pion i poziom)
382. [RPG [I990422] — opis] 앉자마자 부서지는 의자. 그래서 비싸다. 깨어질 것을 알기에.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990422].description
   limit: do 150 znaków
   EN: A chair that shatters the moment one sits. That is why it is expensive. One purchases it knowing it will break.
   PL: Krzesło, które rozpada się w chwili, gdy się na nim usiądzie. Dlatego jest drogie. Kupuje się je wiedząc, że się roztrzaska.
383. [RPG [I990809] — nazwa wyświetlana] 낚시대
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990809].displayName
   limit: do 40 znaków
   EN: Fishing Rod
   PL: Wędka
384. [RPG [I990809] — statystyki przedmiotu] 상징계 공격 적중 시 30% 확률로 3만큼 <color=#fe4b48>피해</color> 입히는 <color=#F8C200>검은 물 추가 공격</color> 발동 (경직 1초)\n- 맞은 적 주위 3칸의 무작위 적 1명에게 <color=#F8C200>검은 물 추가 공격</color>이 이어서 발동 (최대 3회)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990809].statText
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#F8C200>, \n
   EN: In the Symbolic, 30% chance to trigger <color=#F8C200>Blackwater Extra Attack</color>, dealing 3 <color=#fe4b48>Damage</color> upon landing an attack (1 second Hitstun)\n- Triggers <color=#F8C200>Blackwater Extra Attack</color> on 1 random enemy within 3 tiles of the enemy hit (3 times max)
   PL: W Symbolicznym trafienie atakiem daje 30% szans na uruchomienie <color=#F8C200>Dodatkowego Ataku Czarną Wodą</color> zadającego 3 <color=#fe4b48>Obrażenia</color> (1 s Hitstun)\n- <color=#F8C200>Dodatkowy Atak Czarną Wodą</color> przechodzi na 1 losowego wroga w promieniu 3 pól od trafionego wroga (maks. 3 razy)
385. [RPG [I990809] — opis] 해변에는 옛것이 떠밀려 온다. 떠밀려 오는 것들은 백화점의 것이 아닌 것들이다. 그건 이전 시대의 것들이며 이미 망가져 있고 망가질 예정이다. 이제 이곳은 다른 누군가의 설계로 지어진 백화점이기 때문이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990809].description
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Things of eld are beached upon the Shore. They are not of the Grand Magasin, but remnants of the previous age, broken and fated to break further.\nFor this place is now a department store built from another's design.
   PL: Na brzeg wyrzuca to, co dawne. To, co wyrzucone, nie jest rzeczą Grand Magasin — to pozostałości poprzedniej epoki, już nadłamane i skazane na dalsze łamanie.\nBo to miejsce jest teraz Grand Magasin zbudowanym według cudzego projektu.
386. [RPG [I990317] — nazwa wyświetlana] 르루주 부티크 목걸이
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990317].displayName
   limit: do 40 znaków
   EN: Boutique du Rouge Necklace
   PL: Naszyjnik Boutique du Rouge
387. [RPG [I990317] — statystyki przedmiotu] 상징계에서 <color=#F8C200>회피</color> 시 20% 확률로 <color=#F8C200>벼락 추가 공격</color> 발동 (경직 0.5초)\n- 3칸 이내의 무작위 적 1명에게 2만큼 <color=#fe4b48>피해</color> 입힘\n\n상징계 <color=#00ff9c>체력</color> +2
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990317].statText
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, <color=#00ff9c>, \n
   EN: In the Symbolic, upon <color=#F8C200>Evading</color>, 20% chance to trigger a <color=#F8C200>Lightning Strike Extra Attack</color> (0.5 seconds Hitstun)\n- Lightning Strike deals 2 <color=#fe4b48>Damage</color> to 1 random enemy within 3 tiles\n\nSymbolic <color=#00ff9c>HP</color> +2
   PL: W Symbolicznym <color=#F8C200>Unik</color> daje 20% szans na uruchomienie <color=#F8C200>Dodatkowego Ataku Pioruna</color> (0.5 s Hitstun)\n- Piorun zadaje 2 <color=#fe4b48>Obrażenia</color> 1 losowemu wrogowi w promieniu 3 pól\n\nSymboliczne <color=#00ff9c>HP</color> +2
388. [RPG [I990317] — opis] 붉은 신의 붉은 목소리가 들리지 않는다면, 들리도록 만든다. 르루주의 숙원이자 숙업.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990317].description
   limit: do 200 znaków
   EN: If the Crimson God's crimson Voice can no longer be heard, then <i>make</i> it heard. This is the cherished wish of the Rouges... and their appointed labor.
   PL: Jeśli nie słychać szkarłatnego Głosu Szkarłatnego Boga, trzeba sprawić, by znów zabrzmiał. Dawne pragnienie Le Rouge… i ich wyznaczona robota.
389. [RPG [I990318] — nazwa wyświetlana] 르누아르 메종 탑 햇
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990318].displayName
   limit: do 40 znaków
   EN: Maison du Noir Top Hat
   PL: Cylinder Maison du Noir
390. [RPG [I990318] — statystyki przedmiotu] 상징계 <color=#F8C200>콤보 2타 공격</color>의 사거리 +1칸
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990318].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>
   EN: In the Symbolic, <color=#F8C200>Attack Chain 2</color> range +1 tile
   PL: W Symbolicznym zasięg <color=#F8C200>Ataku Kombo 2</color> +1 pole
391. [RPG [I990318] — opis] 쌓아 올리고, 가리고, 감추고, 보호하고, 유지하는 견고한 르누아르의 미덕.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990318].description
   limit: do 140 znaków
   EN: To build up. To cover. To conceal. To protect. To preserve. Such are the steadfast virtues of Le Noir.
   PL: Nagromadzić. Okryć. Ukryć. Chronić. Zachować. Takie są niewzruszone cnoty Le Noir.
392. [RPG [I990810] — nazwa wyświetlana] 뜰채
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990810].displayName
   limit: do 40 znaków
   EN: Scoop Net
   PL: Podbierak
393. [RPG [I990810] — statystyki przedmiotu] 상징계에서 적 처치 시 20% 확률로 적 위치에 <color=#F8C200>검은 유체</color> 생성 (동시 1개까지)\n- <color=#F8C200>검은 유체</color>는 10칸 이내의 가장 가까운 적에게 기어감\n- 적에게 닿거나 3초 안에 닿지 못하면 그 자리에서 폭발\n- 폭발 시 주위 1칸에 5만큼 <color=#fe4b48>피해</color> 입힘
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990810].statText
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, upon killing an enemy, 20% chance to generate <color=#F8C200>Black Larva</color>\n- <color=#F8C200>Black Larva</color> crawls to the nearest enemy within 10 tiles\n- When it touches an enemy, or if it fails to touch an enemy within 3 seconds, detonates on the spot\n- Upon detonation, deal 5 <color=#fe4b48>Damage</color> within 1 tile
   PL: W Symbolicznym po zabiciu wroga 20% szans na wygenerowanie <color=#F8C200>Czarnej Larwy</color> (maks. 1 naraz)\n- <color=#F8C200>Czarna Larwa</color> czołga się do najbliższego wroga w promieniu 10 pól\n- Gdy dotknie wroga albo nie dotknie go w ciągu 3 sekund, wybucha na miejscu\n- Wybuch zadaje 5 <color=#fe4b48>Obrażeń</color> w promieniu 1 pola
394. [RPG [I990810] — opis] 아쿠아리움에는 다양한 물고기들이 살았으며 여러 종류의 수족관이 있었다. 다양한 환경으로 구현된 그곳에는 저마다의 비늘과 물과 어항들이 누비어 있었다. 그중 검은 실로 이루어진 물은 가장 낮은 곳에서 흘렀으며, 그곳에 조용히 잠을 자던 물고기가 있었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990810].description
   limit: do 310 znaków
   EN: The Aquarium once held countless fish and tanks of every kind. Scales, waters, and glass enclosures threaded through environments of every variety. Lowest of all flowed water woven from Blackthread, and within it slept a fish in silence.
   PL: W Akwarium żyły przeróżne ryby, a zbiorników było bez liku. W miejscach urzeczywistnionych w najróżniejszych środowiskach krążyły łuski, wody i akwaria. Woda utkana z Czarnej Nici płynęła najniżej, a w niej cicho spała pewna ryba.
395. [RPG [I991018] — nazwa wyświetlana] 공허를 담은 눈
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991018].displayName
   limit: do 40 znaków
   EN: Voidbearing Eye
   PL: Oko Niosące Pustkę
396. [RPG [I991018] — statystyki przedmiotu] 상징계에서 뿌이의 <color=#F8C200>통제자 투사체</color> 강화\n- 적중 시 주위 2칸에 3만큼 <color=#fe4b48>피해</color>를 한 번 더 입힘 (경직 0.1초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991018].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, enhance Pwie's <color=#F8C200>Overseer Projectile</color>\n- Upon landing the projectile, deals 3 <color=#fe4b48>Damage</color> within 2 tiles (0.1 seconds Hitstun)
   PL: W Symbolicznym wzmacnia <color=#F8C200>Pocisk Nadzorcy</color> Pwie\n- Po trafieniu pocisk zadaje 3 <color=#fe4b48>Obrażenia</color> w promieniu 2 pól (0.1 s Hitstun)
397. [RPG [I991018] — opis] 아쿠아리움에서 백화점으로 바뀔 때 아쿠아리움의 잔재는 소멸했어야 했다. 하지만 그렇지 않고 남아서 아쿠아리움에서의 때를 추억하는 존재가 남아 있다는 것은 결함이 없다 믿어왔던 시지프 시스템이 해결해야 할 문제다. 어떤 이유에서 고객이 되지 못하고 남겨진 물고기는 백화점이 몇 번이고 리셋되더라도 고객이 되지 못한다. 이 결점을 고치려면 시지프 시스템적으로 이 물고기를 담당하고 있는 죄인을 죽여야 한다. 하지만 시지프 시스템은 처벌장치이자 자원채취기이자 N사의 도덕성이기 때문에 시지프 시스템 수감자를 강제로 죽이지 못하게 되어있다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991018].description
   limit: do 940 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Aquarium transformed into the Grand Magasin, every remnant of the Aquarium should have disappeared with it. Yet something remained—something that still remembers its time there. For the Sisyphe System, which had long been believed to be flawless, this is a defect that must be resolved.\n\nFor whatever reason, the fish that was left behind without ever becoming a customer will remain a fish, no matter how many times the Grand Magasin resets.\n\nTo correct this flaw within the Sisyphe System, the convict responsible for that fish would have to die.\n\nBut the Sisyphe System is at once a punishment device, a resource-harvesting apparatus, and an embodiment of N Corp.'s morality. By design, it cannot forcibly kill one of its own prisoners.
   PL: Gdy Akwarium przeobraziło się w Grand Magasin, wszelkie pozostałości Akwarium powinny były zniknąć. Ale coś zostało — istota, która do dziś wspomina czasy w Akwarium. Dla Systemu Sisyphe, który od zawsze uchodził za nieskazitelny, to wada wymagająca rozwiązania.\nRyba, która z jakiegoś powodu nie stała się klientem i została w tyle, nie stanie się klientem, choćby Grand Magasin resetowało się bez końca.\nBy naprawić tę wadę w Systemie Sisyphe, skazaniec odpowiedzialny za tę rybę musiałby umrzeć.\nAle System Sisyphe to zarazem urząd karzący, maszyna pozyskująca zasoby i moralność N Corp. — z założenia nie może zmusić swego więźnia do śmierci.
398. [RPG [I990918] — nazwa wyświetlana] 바느질의 왕의 실꾸리
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990918].displayName
   limit: do 50 znaków
   EN: Clew of the King of Needleworks
   PL: Kłębek Króla Szycia
399. [RPG [I990918] — statystyki przedmiotu] 상징계에서 뿌이의 <color=#F8C200>바늘 투사체</color> 강화\n- 날아가는 경로의 적을 관통하며 2만큼 <color=#fe4b48>피해</color> 입힘\n\n그림자계 전투에서 뿌이의 '힘내' 강화\n- 적중 시 <color=#F8C200>합 위력 증가</color> 대신 <color=#F8C200>기본 위력 증가</color> 1 부여\n- 적중 시 부여하는 <color=#F8C200>공격 레벨 증가</color>를 다음 턴에도 부여
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990918].statText
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, enhance Pwie's <color=#F8C200>Needle Projectile</color>\n- Punches through enemies in its trajectory, dealing 2 <color=#fe4b48>Damage</color>\n\nDuring battle in the Shadowed, enhance Pwie's "Perk Up" Skill\n- On Hit, instead of applying <color=#F8C200>Clash Power Up</color>, apply 1 <color=#F8C200>Base Power Up</color>\n- Applies <color=#F8C200>Offense Level Up</color> applied On Hit next turn as well
   PL: W Symbolicznym wzmacnia <color=#F8C200>Pocisk Igły</color> Pwie\n- Przebija wrogów na swojej drodze, zadając 2 <color=#fe4b48>Obrażenia</color>\n\nW walce w Zacienionym wzmacnia umiejętność Pwie „Ożyw się”\n- Trafienie: zamiast <color=#F8C200>Zwiększenia Mocy Starcia</color> nakłada 1 <color=#F8C200>Zwiększenie Mocy Podstawowej</color>\n- Nakładane trafieniem <color=#F8C200>Zwiększenie Poziomu Ataku</color> utrzymuje się także w następnej turze
400. [RPG [I990918] — opis] 맛이… 그렇게 중요해? 꼬무리가 맛있을지, 아닐지 모르잖아. 그런데도 꼬무리를 먹고 싶어한다는 건…이미 먹어본 적이 있다는 거야? 하지만… 맛이라는 건 매번 변하는 거잖아. 왜 같은 맛이 날 거라고 생각하는 거야…? 그리고 이상해… 꼬무리는 여기 있어… 먹힌 적도 없어.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990918].description
   limit: do 390 znaków
   EN: Is taste... that important? You don't know if Wriggley's gonna be tasty or not. If you wanna eat Wriggley anyway... have you eaten Wriggley before? But... taste is changing all the time. Why do you think Wriggley'll taste the same again? And... Wriggley's right here. No one's eaten Wriggley. Weird...
   PL: Czy smak… aż tak się liczy? Nie wiadomo, czy Wriggley będzie smaczny, czy nie. A mimo to chcesz zjeść Wriggleya… czyżbyś już kiedyś go jadł? Ale… smak się wciąż zmienia. Skąd pewność, że Wriggley znowu tak samo posmakuje…? I coś dziwnego… Wriggley jest tu… nikt go jeszcze nie zjadł.
401. [RPG [I990813] — nazwa wyświetlana] 깨끗한 앞치마
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990813].displayName
   limit: do 40 znaków
   EN: Clean Apron
   PL: Czysty Fartuch
402. [RPG [I990813] — statystyki przedmiotu] 상징계에서 뿌이의 <color=#F8C200>검은 물 투사체</color> 강화\n- 적중 지점 주위 1칸에 <color=#F8C200>검은 물 타일</color> 생성 (5초 유지)\n- 타일 위의 적은 2초마다 2만큼 <color=#fe4b48>피해</color>를 받고 이동 속도 20% 감소\n\n그림자계 전투에서 뿌이의 '붉은못 세례' 강화\n- 사용 시 대상의 <color=#F8C200>출혈</color> 4당 기본 위력 +1 (최대 2)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990813].statText
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, enhance Pwie's <color=#F8C200>Blackwater Projectile</color>\n- Generate <color=#F8C200>Blackwater Tile</color> within 1 tile of the landing point (duration: 5 seconds)\n- Enemies on top of affected tiles:\n  - Take 2 <color=#fe4b48>Damage</color> every 2 seconds \n  - Movement Speed -20%\n\nDuring battle in the Shadowed, enhance Pwie's "Baptism of Crimson Nails" Skill\n- On Use, Base Power +1 for every 4 <color=#F8C200>Bleed</color> on target (max 2)
   PL: W Symbolicznym wzmacnia <color=#F8C200>Pocisk Czarnej Wody</color> Pwie\n- W miejscu trafienia tworzy <color=#F8C200>Kafel Czarnej Wody</color> w promieniu 1 pola (utrzymuje się 5 s)\n- Wrogowie na kafelku otrzymują co 2 sekundy 2 <color=#fe4b48>Obrażenia</color> i tracą 20% Szybkości Ruchu\n\nW walce w Zacienionym wzmacnia umiejętność Pwie „Chrzest Szkarłatnych Gwoździ”\n- Przy użyciu: +1 Moc Podstawowa za każde 4 <color=#F8C200>Krwawienia</color> na celu (maks. 2)
403. [RPG [I990813] — opis] …모르겠어. 처음 만났을 때… 너도 뫼르소와 단테를, 나를 죽이려고 했잖아. 원하는 게 있어. 그러려면 어쩔 수 없는 거잖아. 약해서… 약하기까지 해서 죽는 거야. 기분 나빠. 너도 똑같았는데, 왜… 이런 감정이 느껴져? 왜 내가 이런 죄책감을… 가져야만 해…?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990813].description
   limit: do 430 znaków
   EN: ... I don't understand. You tried to kill Meursault, Dante, and me when we first met. I need something from you... but you won't give it, so there's really no other way, right? You die because... because you're evil... And weak, too. So why do I feel so awful? You did the same thing—Why... why am I the only one left to feel this guilt?
   PL: …Nie wiem. Gdyśmy się poznali… i ty próbowałeś zabić Meursaulta, Dante i mnie. Masz swoje pragnienia. Więc nie da się inaczej, prawda? Giniesz, bo… bo jesteś zły. I słaby. Dlaczego więc czuję się tak źle? Ty zrobiłeś to samo — czemu… czemu to ja muszę nosić tę winę…?
404. [RPG [I990315] — nazwa wyświetlana] 담요
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990315].displayName
   limit: do 40 znaków
   EN: Blanket
   PL: Koc
405. [RPG [I990315] — statystyki przedmiotu] 상징계에서 <color=#F8C200>가드</color> 중 피격 시 받는 <color=#fe4b48>피해량</color> 20% 감소
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990315].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: In the Symbolic, <color=#fe4b48>Damage</color> Taken -20% when hit while <color=#F8C200>Blocking</color>
   PL: W Symbolicznym przy trafieniu podczas <color=#F8C200>Bloku</color> otrzymywane <color=#fe4b48>Obrażenia</color> -20%
406. [RPG [I990315] — opis] 누군가는 새장 안에서 단잠을 청한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990315].description
   limit: do 120 znaków
   EN: Some seek a peaceful sleep inside the birdcage.
   PL: Niektórzy proszą o głęboki sen wewnątrz klatki.
407. [RPG [I990914] — nazwa wyświetlana] 연골
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990914].displayName
   limit: do 40 znaków
   EN: Cartilage
   PL: Chrząstka
408. [RPG [I990914] — statystyki przedmiotu] 상징계에서 <color=#F8C200>Garde</color> 3단계 해금\n- 3단계 <color=#F8C200>Garde</color> 시간: 3초\n- 3단계 <color=#F8C200>Garde</color> <color=#fe4b48>피해량</color>: 상징계 공격의 <color=#fe4b48>피해량</color> +3\n\n상징계 <color=#F8C200>Garde</color>의 <color=#F8C200>돌진</color> 거리 +2칸
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990914].statText
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: Unlocks Level 3 <color=#F8C200>Garde</color> in the Symbolic\n- <color=#F8C200>Garde</color> Time: 3 seconds\n- <color=#F8C200>Garde</color> <color=#fe4b48>Damage</color>: Attack <color=#fe4b48>Damage</color> +3 in the Symbolic\n\nIn the Symbolic, <color=#F8C200>Garde</color> <color=#F8C200>Dash</color> distance +2 tiles
   PL: Odblokowuje <color=#F8C200>Garde</color> 3. poziomu w Symbolicznym\n- Czas <color=#F8C200>Garde</color> 3. poziomu: 3 s\n- <color=#fe4b48>Obrażenia</color> <color=#F8C200>Garde</color> 3. poziomu: <color=#fe4b48>Obrażenia</color> ataku w Symbolicznym +3\n\nW Symbolicznym dystans <color=#F8C200>Szarży</color> <color=#F8C200>Garde</color> +2 pola
409. [RPG [I990914] — opis] 슬프지 않게 된 것은 눈물을 모른다. 건조하게 삐걱대고 날카로워진다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990914].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Those who are freed from sadness forget tears.\nThey become dry, rigid, and cutting.
   PL: Ci, których nie dotknie smutek, nie znają łez.\nStają się wysuszeni, sztywni i raniący.
410. [RPG [I991017] — nazwa wyświetlana] 그을음
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991017].displayName
   limit: do 40 znaków
   EN: Soot
   PL: Sadza
411. [RPG [I991017] — statystyki przedmiotu] 상징계에서 3단계 <color=#F8C200>Garde</color>가 <color=#F8C200>콤보 3타 공격</color>으로 발동\n- 동작·효과 모두 <color=#F8C200>콤보 3타 공격</color>으로 적용\n- 「떡밥」 보유 시 동작은 <color=#F8C200>콤보 3타 공격</color>으로 적용\n- 이때 효과는 <color=#F8C200>콤보 2타 공격</color>과 <color=#F8C200>콤보 3타 공격</color>이 중첩되어 적용
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991017].statText
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, \n
   EN: In the Symbolic, activates Level 3 <color=#F8C200>Garde</color> as <color=#F8C200>Attack Chain 3</color>\n- All motions and effects are applied as <color=#F8C200>Attack Chain 3</color>\n- When player has 「Paste Bait」, motion is applied as <color=#F8C200>Attack Chain 3</color>\n- When this effect activates, triggers both <color=#F8C200>Attack Chain 2</color> effect and <color=#F8C200>Attack Chain 3</color> effect
   PL: W Symbolicznym <color=#F8C200>Garde</color> 3. poziomu uruchamia <color=#F8C200>Atak Kombo 3</color>\n- Ruch i efekty stosowane jak przy <color=#F8C200>Ataku Kombo 3</color>\n- Przy posiadaniu 「Zanęty」 ruch stosowany jest jak przy <color=#F8C200>Ataku Kombo 3</color>\n- Wtedy efekty nakładają się jak przy <color=#F8C200>Ataku Kombo 2</color> i <color=#F8C200>Ataku Kombo 3</color>
412. [RPG [I991017] — opis] 백화점에 속하지 않는 존재가 남긴 그을음. 시지프 시스템은 매번 시대에 따라 그 모습을 바꿔왔다. 시지프 백화점은 시지프 시스템을 다루는 거인 중 설계자이자 재단사가 생각한, 상징계로 구현해내기 가장 편하고 적합한 모습이다. 이 자리의 담당자에 따라 시지프 시스템은 백화점에서 아쿠아리움, 주유소, 동굴, 산맥 등으로 바뀐다. 백화점이든 동굴이든 형태가 중요하지 않다. 시지프 시스템은 그 안에서 어떻게든 낙차를 만들어내는 구조를 만들어내기 때문에 거인은 이 구조를 상상해 낼 수만 있는 시선을 가지고 있으면 된다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991017].description
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Soot left behind by something that does not belong to the department store.\n\nThe Sisyphe System has changed its form time and again with each passing age. Grand Magasin Sisyphe is simply the form one of its Giants—namely the Architect, who was also an Alterationist—deemed the most convenient and suitable for realization within the Symbolic.\n\nDepending on who is assigned to this position, the Sisyphe System may take the form of a department store, an aquarium, a gas station, a cave, a mountain range, or something else entirely.\n\nWhether it is a department store or a cave is beside the point. Whatever shape it takes, the Sisyphe System will always construct some means of creating a "drop", or fluctuations, within itself. All the Giant needs is a perspective capable of imagining such a structure.
   PL: Sadza pozostawiona przez istotę, która nie należy do Grand Magasin.\nSystem Sisyphe z epoki na epokę zmieniał swoje oblicze. Grand Magasin Sisyphe to po prostu forma, którą jeden z jego Gigantów — Architekt, a zarazem Krawiec — uznał za najwygodniejszą i najodpowiedniejszą do urzeczywistnienia w Symbolicznym.\nW zależności od tego, kto piastuje tę funkcję, System Sisyphe zmienia się w Grand Magasin, Akwarium, stację benzynową, jaskinię, pasmo górskie albo w coś zupełnie innego.\nCzy to Grand Magasin, czy jaskinia — forma nie ma znaczenia. System Sisyphe zawsze wybuduje w sobie strukturę, która z jakiś powodów tworzy spadek (przepaść wysokości). Gigant potrzebuje tylko spojrzenia, zdolnego wyobrazić sobie taką strukturę.
413. [RPG [I990917] — nazwa wyświetlana] 바느질의 왕의 시침핀
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990917].displayName
   limit: do 60 znaków
   EN: Straight Pin of the King of Needleworks
   PL: Szpilka Króla Szycia
414. [RPG [I990917] — statystyki przedmiotu] 상징계에서 <color=#F8C200>콤보 2타 공격</color> 적중 시 그 대상에게 <color=#F8C200>바느질의 왕 표식</color> 부여\n- <color=#F8C200>표식</color>을 가진 대상이 없을 때만 부여\n- 바느질의 왕 표식 유지 시간: 5초\n- 해당 표식이 부여된 대상의 이동 속도 -30%\n- 해당 표식이 부여된 대상 사망 시 주위 3칸에 3만큼 <color=#fe4b48>피해</color> 입힘 (경직 0.1초)\n- 유지 시간 종료 시 표식 해제 후 5만큼 <color=#fe4b48>피해</color> 입힘\n- 해당 피해로 사망 시 주위 1칸에 3만큼 <color=#fe4b48>피해</color> 입힘 (경직 0.1초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990917].statText
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: In the Symbolic, upon landing <color=#F8C200>Attack Chain 2</color>, inflict <color=#F8C200>Mark of the King of Needleworks</color>\n- Inflicts this effect only when there are no targets that have this <color=#F8C200>Mark</color>\n- Mark of the King of Needleworks duration: 5 seconds\n- Affected target Movement Speed -30%\n- When the affected target is killed, deals 3 <color=#fe4b48>Damage</color> within 3 tiles (0.1 seconds Hitstun)\n- After the effect duration expires, removes the Mark and deals 5 <color=#fe4b48>Damage</color>\n- If that Damage kills the affected target, deals 3 <color=#fe4b48>Damage</color> within 1 tile (0.1 seconds Hitstun)
   PL: W Symbolicznym trafienie <color=#F8C200>Atakiem Kombo 2</color> nakłada na cel <color=#F8C200>Znak Króla Szycia</color>\n- Nakładany tylko, gdy nie ma celu z tym <color=#F8C200>Znakiem</color>\n- <color=#F8C200>Znak Króla Szycia</color> utrzymuje się 5 sekund\n- Szybkość Ruchu celowi ze znakiem -30%\n- Po śmierci celu ze znakiem zadaje 3 <color=#fe4b48>Obrażenia</color> w promieniu 3 pól (0.1 s Hitstun)\n- Po wygaśnięciu znak znika i zadaje 5 <color=#fe4b48>Obrażeń</color>\n- Jeśli te Obrażenia zabiją cel, zadaje 3 <color=#fe4b48>Obrażenia</color> w promieniu 1 pola (0.1 s Hitstun)
415. [RPG [I990917] — opis] 실과 바늘. 지하 2층은 이 두 개념의 필요로 인해 구축되었다. 실은 바늘을 통과하고 싶어하고 바늘은 무엇이든 통과되려 한다.\n본질을 다루려면 자신도 본질에 가까워져야 한다. 그래서 지하로 내려갈수록 존재의 해상도는 옅어지고 결국엔 점으로 환원된다. 실과 바늘은 옷의 본질에 가깝지만 본질은 아니다. 그리하여 실을 다루는 재단사의 존재가 분해되는 것은 필연적이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990917].description
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thread and needle. B2F was built from the need for these two concepts.\n\nThread seeks to penetrate the needle, while the needle longs to be penetrated. To handle the essence, one must draw close to the essence oneself; therefore, the deeper one descends to the basement, the clarity of existence blurs and segments until it is reduced to a collection of bits.\nThough the concept of thread and needle does, indeed, approach the essence of clothing closely, it is not the same as the essence. The dissolving of the Alterationist, who handles thread, is an inevitable fate.
   PL: Nić i igła. Poziom -2 zbudowany jest z potrzeby tych dwóch pojęć.\nNić chce przeniknąć igłę, a igła pragnie być przeniknięta. By władać istotą, trzeba samemu zbliżyć się do istoty; dlatego im głębiej schodzi się do podziemia, tym jaśniejsza staje się gęstość istnienia, aż składa się w punkt.\nNić i igła zbliżają się do istoty ubrania, ale istotą nie są. Rozpad istoty Krawca, który włada nićmi, jest nieuchronny.
416. [RPG [I102024] — nazwa wyświetlana] 어떤 르누아르의 기록
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I102024].displayName
   limit: do 40 znaków
   EN: A Noir's Note
   PL: Zapiski Le Noir
417. [RPG [I102024] — statystyki przedmiotu] 상징계에서 <color=#F8C200>가드</color> 시 다음 공격의 <color=#fe4b48>피해량</color> +2 (쿨타임 5초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I102024].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: After <color=#F8C200>Blocking</color> in the Symbolic, <color=#fe4b48>Damage</color> Dealt +2 on the next attack (5 seconds cooldown)
   PL: Po <color=#F8C200>Bloku</color> w Symbolicznym <color=#fe4b48>Obrażenia</color> następnego ataku +2 (odnowienie 5 s)
418. [RPG [I102024] — opis] 습격해온 르루주들 사이에서 나는 르루주의 브랜드 디렉터를 보았다. 그자는 알을 품에 안고 있었다. 나는 느꼈다. 그 알에서 옅게, 퍼지고 있는 신의 체온을. 아, 그자가 무엇을 위해 우리를 다 죽인 건지 알 것 같기도…
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I102024].description
   limit: do 300 znaków
   EN: "I saw the Rouges' Brand Director among the raiders. She held an egg against her chest. I could feel it—the faint, godly warmth that spread from within it.  Ah... I think I may understand what she slaughtered us all to accomplish..."
   PL: Wśród napastników Le Rouge zobaczyłem Dyrektorkę Marki Le Rouge. Niosła jajo przy piersi. Czułem. Jak z jego wnętrza rozlewa się delikatne, boże ciepło. Ach... chyba zaczynam rozumieć, dla czego pozabijała nas wszystkich…
419. [RPG [I990319] — nazwa wyświetlana] 꽃가위
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990319].displayName
   limit: do 40 znaków
   EN: Blossom Scissors
   PL: Nożyczki Kwiatowe
420. [RPG [I990319] — statystyki przedmiotu] 상징계 공격 적중 시 30% 확률로 5만큼 <color=#fe4b48>피해</color> 입히는 <color=#F8C200>꽃가위 추가 공격</color> 발동 (경직 0.3초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990319].statText
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#F8C200>
   EN: In the Symbolic, 30% chance to trigger <color=#F8C200>Blossom Scissors-snip Extra Attack</color> dealing 5 <color=#fe4b48>Damage</color> upon landing an attack (0.3 seconds Hitstun)
   PL: W Symbolicznym trafienie atakiem daje 30% szans na uruchomienie <color=#F8C200>Dodatkowego Ataku Nożyczek Kwiatowych</color> zadającego 5 <color=#fe4b48>Obrażeń</color> (0.3 s Hitstun)
421. [RPG [I990319] — opis] 너희가 가는 곳 그 어디든 꽃길이 되도록 이 꽃가위로 자박자박 잘라내어줄게.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990319].description
   limit: do 150 znaków
   EN: Wherever you go, I will <i>snip-snip</i> with these blossom shears until the path beneath you blooms with fallen blossoms.
   PL: Wszędzie, gdzie pójdziecie, podetnę tymi nożyczkami kwiatowymi, krok po kroku, aż pod twoimi stopami rozkwitną kwiaty.
422. [RPG [I991004] — nazwa wyświetlana] 팔레트의 황금송진
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991004].displayName
   limit: do 40 znaków
   EN: Palette's Golden Resin
   PL: Złota Żywica z Palety
423. [RPG [I991004] — opis] 황금가죽에는 힘이 있다. 마네킹으로 전락해도 이상하지 않을 마음이 의식을 가질 수 있도록, 온전한 뒤틀림이 될 수 있도록 도와준다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991004].description
   limit: do 250 znaków
   EN: The Golden Hide is an object of power. Minds may teeter on the brink of descent into a Mannequin, yet the Golden Hide gives them consciousness, guiding them to become a complete Distortion.
   PL: W Złotej Skórze drzemie siła. Umysłom chwiejącym się na krawędzi Manekina ona daje świadomość, prowadząc ku pełnemu Wypaczeniu.
424. [RPG [I991005] — nazwa wyświetlana] 지하 2층 플로어 매니저의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991005].displayName
   limit: do 50 znaków
   EN: B2F Floor Manager's Golden Hide
   PL: Złota Skóra Kierownika Piętra -2
425. [RPG [I991005] — opis] 끝에 닿은 뒤틀림은 자신만이 이해할 수 있는 언어를 갖는다. 이 언어로는 타인과 소통할 수 없다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991005].description
   limit: do 190 znaków
   EN: A Distortion that has reached the terminus acquires a language only it can understand. It cannot communicate with others with such a language.
   PL: Wypaczenie, które doszło do końca, ma język, który rozumie tylko ono samo. Takim językiem nie da się porozumiewać z innymi.
426. [RPG [I991006] — nazwa wyświetlana] 바느질의 왕의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991006].displayName
   limit: do 60 znaków
   EN: Golden Hide of the King of Needleworks
   PL: Złota Skóra Króla Szycia
427. [RPG [I991006] — opis] 오랜 시간이 지났음에도 그것은 마네킹이 되지 않고, 지성 있는 뒤틀림으로 남았다. 이는 모두 황금가죽의 덕분이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991006].description
   limit: do 170 znaków
   EN: Though ages passed, it did not devolve into a Mannequin; instead, aided by the Golden Hide, it remained a sapient Distortion.
   PL: Choć minęły wieki, nie zeszedł do poziomu Manekina; dzięki Złotej Skórze pozostał rozumnym Wypaczeniem.
428. [RPG [I991007] — nazwa wyświetlana] 수셰프의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991007].displayName
   limit: do 40 znaków
   EN: Sous Chef's Golden Hide
   PL: Złota Skóra Sous Chefa
429. [RPG [I991007] — opis] 황금가죽에서 새어나오는 빛은 어째서 마네킹들이 지성을 유지할 수 있도록 돕는가. 오히려 마네킹처럼 지성 없는 뒤틀림이 되도록 도와야 하는 것이 아닌가?
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991007].description
   limit: do 220 znaków
   EN: Why does the light, bleeding out of the Golden Hide, act as an anchor to the Mannequins' sapience? Should it not instead hasten their descent into mindless Distortions?
   PL: Czemu światło, które sączy się ze Złotej Skóry, pomaga Manekinom utrzymać rozum? Czy nie powinno raczej przyśpieszać ich zejścia ku bezrozumnym Wypaczeniom?
430. [RPG [I991008] — nazwa wyświetlana] 시체더미 사이의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991008].displayName
   limit: do 50 znaków
   EN: Golden Hide from the Corpse Pile
   PL: Złota Skóra ze Stosu Zwłok
431. [RPG [I991008] — opis] 황금빛은 모든 뒤틀림이 끝에 닿기를 원하지만, 동시에 원치 않는다. 빛 안에 있는 것은 하나가 아니며, 그중 하나의 마음조차 하나가 아니기에.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991008].description
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Paradoxically, the golden light wishes for all Distortions to reach their terminus, and at the same time, it does not.\nWhat dwells within the light is more than a single entity, and neither is the heart inside one of them.
   PL: Złoty blask pragnie, by każde Wypaczenie doszło do końca, a zarazem nie pragnie tego.\nBo w świetle mieszka więcej niż jedna istota, a i serce jednej z nich nie jest jedno.
432. [RPG [I991009] — nazwa wyświetlana] 르루주 브랜드 디렉터의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991009].displayName
   limit: do 60 znaków
   EN: Le Rouge Brand Director's Golden Hide
   PL: Złota Skóra Dyrektorki Marki Le Rouge
433. [RPG [I991009] — opis] 뒤틀림은 지성을 가지고, 다양한 방식으로 타자와 소통할 수 있다. 빛이 그들의 지성을 종말로 인도하지 않는 아이러니는, 어쩌면 빛이 지닌 인간성을 의미하는 것일지도 모른다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991009].description
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Distortions can remain sapient and convey their wills to others through various avenues of communication.\nThat the light does not obliterate their wisdom is an irony, and may betray a glimpse of the humanity still dwelling within it.
   PL: Wypaczenia zachowują rozum i mogą porozumiewać się z innymi na przeróżne sposoby.\nTo, że światło nie prowadzi ich mądrości ku zagładzie, jest ironią — może zdradzającą resztki człowieczeństwa, które jeszcze w nim mieszka.
434. [RPG [I991010] — nazwa wyświetlana] 3층 플로어 매니저의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991010].displayName
   limit: do 50 znaków
   EN: 3F Floor Manager's Golden Hide
   PL: Złota Skóra Kierownika Piętra 3
435. [RPG [I991010] — opis] 황금가죽을 지닌 고객은 빛과의 대화를 통해 더욱 강력한 힘을 얻고, 백화점 내에서의 영향력 또한 넓혀갈 수 있었다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991010].description
   limit: do 250 znaków
   EN: Through dialogue with the light, customers who carried a piece of the Golden Hide gained powers beyond those of others, which allowed them to expand their influence throughout the Grand Magasin.
   PL: Przez dialog ze światłem klienci niosący kawałek Złotej Skóry zdobywali potężniejsze moce i rozszerzali swoje wpływy wewnątrz Grand Magasin.
436. [RPG [I991011] — nazwa wyświetlana] 벽 틈새의 황금가죽
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991011].displayName
   limit: do 60 znaków
   EN: Golden Hide from the Crack in the Wall
   PL: Złota Skóra ze Szczeliny w Murze
437. [RPG [I991011] — opis] 르네앙이 바라는 것은 단순히 백화점의 붕괴가 아니다. 그들은 어떤 방해도 없이, 빛이 온전히 이곳에 임하기를 바란다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I991011].description
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Le Néant's purpose goes beyond the deconstruction of this department store.\nThey desire the full, unhindered embrace of the light.
   PL: Celem Le Néant nie jest samo rozczłonkowanie tego Grand Magasin.\nOni pragną pełnego, nieograniczonego objęcia światła.
438. [RPG [I990501] — nazwa wyświetlana] 복종
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990501].displayName
   limit: do 40 znaków
   EN: Obedience
   PL: Posłuszeństwo
439. [RPG [I990501] — statystyki przedmiotu] 그림자계 전투에서 <color=#00ff9c>체력</color>이 50% 이하인 인격이 적 스킬에 맞기 직전 잃은 <color=#00ff9c>체력</color>의 20%만큼 보호막 얻음\n- 인격별 전투당 1회\n- 이 보호막은 턴이 끝나도 사라지지 않음
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990501].statText
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, \n
   EN: During battle in the Shadowed, immediately before an Identity that has 50% or lower <color=#00ff9c>HP</color> is hit by an enemy Skill, the said Identity gains Shield equal to 20% of its missing <color=#00ff9c>HP</color>\n- Once per Identity per Encounter\n- This Shield does not expire after the turn ends
   PL: W walce w Zacienionym, zanim Tożsamość o <color=#00ff9c>HP</color> 50% lub niżej zostanie trafiona umiejętnością wroga, zyskuje Tarczę równą 20% brakującego <color=#00ff9c>HP</color>\n- Raz na Tożsamość na potyczkę\n- Ta Tarcza nie znika z końcem tury
440. [RPG [I990501] — opis] 시지프 시스템은 수감자들에게서 경험을 효율적이고 비폭력적으로 추출해 내기 위한 장치이다. 시지프 시스템 안에서 다양한 경험을 하고 그 경험의 다채로움이 경험 반죽의 기본적인 재료가 된다. 경험은 변화의 감지이고, 정지와 이동의 연속이다. 르누아르는 정지를 담당한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990501].description
   limit: do 450 znaków
   EN: The Sisyphe System is an apparatus built to extract experience from prisoners efficiently and without violence. Within it, prisoners undergo a multitude of experiences, and the variety becomes the base ingredient of Experience Dough. Experience is the perception of change: an unbroken alternation between stillness and motion. Le Noir governs stillness.
   PL: System Sisyphe to urząd zbudowany, by wydajnie i bez przemocy pozyskiwać od więźniów doświadczenia. Więźniowie przeżywają w nim mnóstwo doświadczeń, a ich różnorodność staje się podstawowym składnikiem Ciasta Doświadczeń. Doświadczenie to spostrzeżenie zmiany: nieustanne następstwo bezruchu i ruchu. Le Noir sprawuje władzę nad bezruchem.
441. [RPG [I990004] — nazwa wyświetlana] 박동
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990004].displayName
   limit: do 40 znaków
   EN: Pulsation
   PL: Pulsacja
442. [RPG [I990004] — statystyki przedmiotu] 상징계에서 <color=#F8C200>패링</color> 해금\n- 적의 공격 직전 0.2초 안에 뫼르소의 공격 적중 시 적의 공격 취소 (일부 공격 제외)\n\n상징계에서 <color=#F8C200>가드</color> 해금\n- <color=#F8C200>가드</color> 버튼(C키)을 누르는 동안 뫼르소가 <color=#F8C200>가드</color> 자세를 유지함\n- <color=#F8C200>가드</color> 중 <color=#F8C200>가드</color>한 방향에서 들어오는 공격으로 받는 <color=#fe4b48>피해량</color> -30%\n\n상징계에서 <color=#F8C200>Avant</color> 공격의 <color=#F8C200>콤보 2타 공격</color> 해금\n- Avant 발동 후 <color=#F8C200>연속 입력</color>시 콤보 2타 공격 발동\n- <color=#F8C200>콤보 2타 공격</color> 발동 시 상징계 공격의 <color=#fe4b48>피해량</color> +2, <color=#F8C200>경직</color> 시간 +0.1초
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990004].statText
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: Unlocks <color=#F8C200>Parry</color> in the Symbolic\n- Parry: While controlling Meursault, hit the enemy 0.2 seconds before its attack to cancel the attack (excluding certain attacks)\n\nUnlocks <color=#F8C200>Block</color> in the Symbolic\n- Block: Press and hold <color=#F8C200>Block</color> (C on keyboard) to maintain Meursault's <color=#F8C200>Block</color> stance\n- While <color=#F8C200>Blocking</color>, <color=#fe4b48>Damage</color> Taken -30% from the <color=#fe4b48>Blocked</color> direction\n\nUnlocks <color=#F8C200>Attack Chain 2</color> for <color=#F8C200>Avant</color> Attack in the Symbolic\n- After activating Avant, <color=#F8C200>repeat the attack</color> to activate Attack Chain 2\n- <color=#F8C200>Attack Chain 2</color>: <color=#fe4b48>Damage</color> Dealt +2 and <color=#F8C200>Hitstun</color> +0.1 seconds against the enemy
   PL: Odblokowuje <color=#F8C200>Parry</color> w Symbolicznym\n- Parry: traf wroga atakiem w ciągu 0.2 s przed jego atakiem, aby anulować jego atak (nie dotyczy części ataków)\n\nOdblokowuje <color=#F8C200>Blok</color> w Symbolicznym\n- Blok: przytrzymaj przycisk <color=#F8C200>Bloku</color> (C na klawiaturze), aby Meursault utrzymywał postawę <color=#F8C200>Bloku</color>\n- Podczas <color=#F8C200>Bloku</color> otrzymywane <color=#fe4b48>Obrażenia</color> -30% z kierunku, w który <color=#F8C200>Blokujesz</color>\n\nOdblokowuje <color=#F8C200>Atak Kombo 2</color> dla ataku <color=#F8C200>Avant</color> w Symbolicznym\n- Po uruchomieniu Avant <color=#F8C200>ponowne naciśnięcie ataku</color> uruchamia Atak Kombo 2\n- Uruchomienie <color=#F8C200>Ataku Kombo 2</color>: <color=#fe4b48>Obrażenia</color> +2 i <color=#F8C200>Hitstun</color> +0.1 s dla wroga
443. [RPG [I990004] — opis] 지금을 경험한다고들 말하지만, 경험이란 다가올 것을 기대하고 그 기대를 확인하는 일. 그렇다면 경험은 언제나 미래에 있을 테죠.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990004].description
   limit: do 220 znaków
   EN: People speak of experiencing the present. Yet if experience is the act of anticipating what is to come and seeing it realized, then it must always lie in the future.
   PL: Mówi się o przeżywaniu teraźniejszości. Ale jeśli doświadczenie to oczekiwanie tego, co ma nadejść, i sprawdzenie tego oczekiwania, to doświadczenie zawsze tkwi w przyszłości.
444. [RPG [I990002] — nazwa wyświetlana] 망치
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990002].displayName
   limit: do 40 znaków
   EN: Hammer
   PL: Młotek
445. [RPG [I990002] — statystyki przedmiotu] 상징계 공격 <color=#fe4b48>피해량</color> +1\n그림자계 전투에서 <color=#F8C200>속박</color>이 부여된 적에게 가하는 <color=#fe4b48>피해량</color> +10%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990002].statText
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#F8C200>, \n
   EN: <color=#fe4b48>Damage</color> Dealt +1 in the Symbolic\nDuring battle in the Shadowed, deal +10% <color=#fe4b48>damage</color> against enemies that have <color=#F8C200>Bind</color>
   PL: <color=#fe4b48>Obrażenia</color> zadawane +1 w Symbolicznym\nW walce w Zacienionym +10% <color=#fe4b48>obrażeń</color> wobec wrogów z <color=#F8C200>Spętaniem</color>
446. [RPG [I990002] — opis] 망치. 망치는 못이 제 기능을 하게 한다. 하지만 망치는 그 홀로도, 대상을 파괴하는 것으로 기능한다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990002].description
   limit: do 170 znaków
   EN: A hammer. It allows a nail to fulfill its purpose. Yet even alone, a hammer serves just as well as an instrument of destruction.
   PL: Młotek. Pozwala gwoździowi spełnić jego przeznaczenie. A jednak i sam w sobie młotek spełnia się doskonale — jako narzędzie zniszczenia.
447. [RPG [I990431] — nazwa wyświetlana] 빛구두
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990431].displayName
   limit: do 40 znaków
   EN: Luminous Shoes
   PL: Świecące Buty
448. [RPG [I990431] — statystyki przedmiotu] 상징계에서 <color=#F8C200>회피</color> 시 다음 공격의 <color=#fe4b48>피해량</color> +3 (쿨타임 10초)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990431].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>
   EN: After <color=#F8C200>Evading</color> in the Symbolic, <color=#fe4b48>Damage</color> Dealt +3 on the next attack (10 seconds cooldown)
   PL: Po <color=#F8C200>Uniku</color> w Symbolicznym <color=#fe4b48>Obrażenia</color> następnego ataku +3 (odnowienie 10 s)
449. [RPG [I990431] — opis] 힘들어… 굉장히 많아… 너무 많으면 재미가 없어질지 몰라… 너무 많은 면이 빛나면… 그 빛남이 특별하지 않을지 몰라…
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990431].description
   limit: do 190 znaków
   EN: This is too hard... There are so many... Too many will make it less fun... Too many shiny surfaces... won't make the shine special anymore...
   PL: To trudne… jest ich tak dużo… za dużo może odbić radość… za dużo lśniących powierzchni… może sprawić, że lśnienie przestanie być wyjątkowe…
450. [RPG (RPGSystem/rpg-loc-item-common-a1c10p2.json) — nazwa wyświetlana] 알록달록한 실타래
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990926#2].displayName
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [RPG (RPGSystem/rpg-loc-item-common-a1c10p2.json) — opis] 활발한 붉은색도, 엄중한 검정색도, 떠도는 녹갈색도 바늘 가는 곳을 따라갈 수 밖에 없다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p2.json :: dataList[key=I990926#2].description
   limit: do 140 znaków
   EN: Vibrant red, austere black, drifting khaki... all colors are bound to follow wherever the needle leads.
   PL: Żywa czerwień, poważna czerń, unosząca się khaki brunatność — wszystkie barwy nie mają innego wyboru, jak iść tam, gdzie prowadzi igła.

## Tryb RPG [common] — rpg-loc-item-common-a1c10p3
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-item-common-a1c10p3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

452. [RPG [I990931] — nazwa wyświetlana] 목도리
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990931].displayName
   limit: do 40 znaków
   EN: Scarf
   PL: Szal
453. [RPG [I990931] — statystyki przedmiotu] 상징계 공격 <color=#fe4b48>피해량</color> +350\n상징계에서 <color=#00ff9c>체력</color>이 1 미만으로 감소하지 않음
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990931].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, <color=#00ff9c>, \n
   EN: In the Symbolic, <color=#fe4b48>Damage</color> Dealt +350\nIn the Symbolic, <color=#00ff9c>HP</color> does not drop below 1
   PL: <color=#fe4b48>Obrażenia</color> ataku w Symbolicznym +350\nW Symbolicznym <color=#00ff9c>HP</color> nie spada poniżej 1
454. [RPG [I990931] — opis] 데미안과 닮은 푸른 여인이 건내준 목도리. 지니고 있으면 모든것으로부터 보호 받는 느낌이 든다.\n실패에 대한 연민일지, 과정에 대한 응원일지 모르겠으나 바다와 같은 따듯함이 느껴진다.\n바다는 수심을 알수없어 섬뜩하면서도, 모든것을 품어줄것만 같다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990931].description
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A scarf given by the woman in blue who bears a resemblance to Demian. Carrying it brings the strange sensation of being sheltered from all things.\n\nWhether it is pity for failure or encouragement for the road still ahead, there is a warmth to it like the sea.\n\nThe sea is frightening for how little one can know of its depths... and yet it feels as though it might take everything into its embrace.
   PL: Szal podarowany przez kobietę w błękicie przypominającą Demiana. Noszenie go daje dziwne poczucie, że chroni przed wszystkim.\nNiewiadomo, czy to litość nad porażką, czy wsparcie na dalszą drogę — czuje się ciepło podobne do morza.\nMorze straszy niedostępnością głębin, a jednak wydaje się, że mogłoby objąć wszystko.
455. [RPG [I990430] — nazwa wyświetlana] 해진 브로치
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990430].displayName
   limit: do 40 znaków
   EN: Frayed Brooch
   PL: Wytarta Broszka
456. [RPG [I990430] — statystyki przedmiotu] 그림자계 전투에서 적의 가중치 공격 대상이 된 아군에게 피격 직전 최대 <color=#00ff9c>체력</color>의 15%만큼 보호막 부여\n- 전투당 2회\n\n그림자계 전투에서 아군이나 적이 사망하면 다음 턴에 모든 적에게 <color=#F8C200>속박</color> 2 부여\n- 턴당 1회
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990430].statText
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#F8C200>, \n
   EN: During battle in the Shadowed, when an ally is targeted by an enemy's multi-Atk Weight attack, apply Shield equal to 15% of their max <color=#00ff9c>HP</color> immediately before they are hit\n- 2 times per Encounter\n\nDuring battle in the Shadowed, when an ally or enemy dies, inflict 2 <color=#F8C200>Bind</color> on all enemies next turn\n- Once per turn
   PL: W walce w Zacienionym, gdy sojusznik zostanie wybrany jako cel ataku wroga z Wagą Ataku, tuż przed trafieniem nakłada mu Tarczę równą 15% jego maksymalnego <color=#00ff9c>HP</color>\n- 2 razy na potyczkę\n\nW walce w Zacienionym, gdy zginie sojusznik albo wróg, następnej tury nakłada wszystkim wrogom 2 <color=#F8C200>Spętanie</color>\n- Raz na turę
457. [RPG [I990430] — opis] 다른 누구와 다를 바 없이 1층에서 이방인으로 들어와 고객이 되고 긴 세월 끝에 플로어 매니저가 된 존재가 만들어낸 것. 세월을, 시대를 견디고 견뎌 끝내 견뎌낼 수 있게 된 자의 잔재다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990430].description
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Like any other stranger, he entered through 1F, became a customer, and, after a long time, endured enough to rise to Floor Manager. This is an object created by that entity.\n\nHe endured the passage of time and the Age until endurance itself became second nature.
   PL: Jak każdy obcy wszedł przez 1. piętro, stał się klientem i po długim czasie przetrwał tyle, by wspiąć się na Kierownika Piętra. To rzecz stworzona przez tę istotę.\nPrzetrwał upływ czasu i epokę — aż przetrwanie stało się jego naturą.
458. [RPG [I990502] — nazwa wyświetlana] 권위
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990502].displayName
   limit: do 40 znaków
   EN: Authority
   PL: Autorytet
459. [RPG [I990502] — statystyki przedmiotu] 그림자계 전투에서 자신보다 속도가 높은 대상과 합 시작 시 대상에게 다음 턴에 <color=#F8C200>속박</color> 1 부여\n- 턴당 1회\n\n그림자계 전투에서 자신보다 속도가 낮은 대상에게 가하는 <color=#fe4b48>피해량</color> +10%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990502].statText
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#fe4b48>, \n
   EN: During battle in the Shadowed, on Clash Start against target with faster Speed than this unit, inflict 1 <color=#F8C200>Bind</color> on that target next turn\n- Once per turn\n\nDuring battle in the Shadowed, deal +10% <color=#fe4b48>Damage</color> to targets with slower Speed than this unit
   PL: W walce w Zacienionym, na początku Starcia z celem o wyższej Szybkości, nakłada na niego następnnej tury 1 <color=#F8C200>Spętanie</color>\n- Raz na turę\n\nW walce w Zacienionym +10% <color=#fe4b48>Obrażeń</color> wobec celów o niższej Szybkości
460. [RPG [I990502] — opis] 자신에게 부여된 역할, 업무가 있었다. 그 업무가 매뉴얼화되어 있고 정형화되어 있고 시지프 타워에 출근해 같은 말들을 되뇌고 방송을 한다. 여느 직장인처럼 퇴근을 기다리지만, 그에게 신념이 있었다. 시지프 시스템은 진정으로 N사와 도시를 위해 유지되어야 하는 것이라고. 못 박을 자이자 망치를 담당하는 자로서 그 신념의 심지는 단단했다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990502].description
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: He had a role assigned to him. A job.\n\nThe work was standardized, codified into manuals. He would report to Sisyphe Tower, repeat the same lines, and make the same broadcasts day after day.\n\nLike any other employee, he would count down the minutes until the end of his shift.\n\nYet there was one conviction he held firmly: that the Sisyphe System had to exist and be maintained, for the sake of N Corp. and the City as a whole.\n\nAs One Who Nails, and the one entrusted with the hammer, that conviction had taken root in him deeply.
   PL: Miał wyznaczoną rolę. Pracę.\nTa praca była zmanualizowana i uformowana: chodził do Wieży Sisyphe, powtarzał te same słowa i nadawał te same audycje.\nJak każdy pracownik czekał na koniec zmiany.\nA jednak trzymał się jednego przekonania: że System Sisyphe musi istnieć i być utrzymywany — dla N Corp. i dla miasta jako całości.\nJako Ten, Kto Przybija, i ten, komu powierzono młot, to przekonanie trwało w nim głęboko.
461. [RPG [I990503] — nazwa wyświetlana] 섭취
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990503].displayName
   limit: do 40 znaków
   EN: Consumption
   PL: Spożycie
462. [RPG [I990503] — statystyki przedmiotu] 그림자계 전투에서 합 승리 시 (스킬의 최종 위력 x 1.5)만큼 자신의 <color=#00ff9c>체력 회복</color> (인격별 턴당 1회)\n- E.G.O 스킬이면 1.5 대신 1로 적용 (소수점 버림)\n- 이 <color=#00ff9c>회복</color>이 발동한 인격은 다음 턴에 <color=#fe4b48>피해량</color> 증가 1을 얻음 (인격별 턴당 1회)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990503].statText
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#fe4b48>, \n
   EN: During battle in the Shadowed, on Clash Win, heal (Skill Final Power x 1.5) <color=#00ff9c>HP</color> (once per turn per Identity)\n- For E.G.O Skills, x1 instead of x1.5 (rounded down)\n- Identities <color=#00ff9c>healed</color> by this effect gain 1 <color=#fe4b48>Damage</color> Up next turn (once per turn per Identity)
   PL: W walce w Zacienionym wygrana w Starciu <color=#00ff9c>leczy</color> o (Moc Końcowa Umiejętności x 1.5) <color=#00ff9c>HP</color> (raz na turę na Tożsamość)\n- Dla Umiejętności E.G.O stosuje się x1 zamiast x1.5 (zaokrąglone w dół)\n- Tożsamość wyleczona tym efektem zyskuje w następnej turze 1 <color=#fe4b48>Zwiększenie Obrażeń</color> (raz na turę na Tożsamość)
463. [RPG [I990503] — opis] 먹어도 먹어도 배고프다. 정도의 차이일 뿐 모두가 그렇다. 지금은 배불러도 다시 배고파진다. 이 아이에게는 그 간격이 비정상적으로 빠를 뿐. 허기지도록 태어났고 계속 먹기를 기대받는 신으로 못 박힌 채 태어났다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990503].description
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eat and eat, but the hunger will always return. Everyone is the same; the difference is only how long it takes. Even a full stomach will empty again.\n\nFor this child, that interval is simply unnaturally short, because they were born to hunger, born with the expectation that they would go on devouring.\n\nThey were nailed fast into the role of a god who must never cease to feed.
   PL: Jeść i jeść — a głód zawsze wraca. Wszyscy są tacy sami; różni się tylko tempo. Nawet pełny brzuch znów opróżni się.\nU tego dziecka ta przerwa jest po prostu nienaturalnie krótsza: narodziło się z głodu, narodziło się z oczekiwaniem, że będzie nieustannie pożerać.\nNarodziło się przybite do roli boga, który nigdy nie może przestać się karmić.
464. [RPG [I990003] — nazwa wyświetlana] 밧줄
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990003].displayName
   limit: do 40 znaków
   EN: Rope
   PL: Lina
465. [RPG [I990003] — opis] 밧줄. 밧줄은 못과는 다른 방식으로 대상을 고정한다. 박는 것과 묶는 것에는 많은 차이가 있으니.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990003].description
   limit: do 220 znaków
   EN: A rope. It fixes its target in place by means unlike a nail. There is, after all, a world of difference between driving something through and binding something fast.
   PL: Lina. Lina unieruchamia cel w inny sposób niż gwóźdź. Między wbijaniem a wiązaniem jest przepaść różnic.
466. [RPG [I990005] — nazwa wyświetlana] 정지
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990005].displayName
   limit: do 40 znaków
   EN: Stillness
   PL: Bezruch
467. [RPG [I990005] — statystyki przedmiotu] 상징계에서 3단계 <color=#F8C200>Garde 충전 시간</color> 이 1단계 Garde 시간과 같아짐\n- 충전 완료 시 <color=#F8C200>Garde</color>가 항상 <color=#F8C200>3단계</color>로 발동\n\n상징계 <color=#F8C200>콤보 2타 공격</color>의 범위가 좌우 1칸씩 증가\n- 증가한 좌우 범위는 사거리 증가 효과의 영향을 받지 않음\n\n상징계 전투에서 간수가 특정 장소로 소환시킬 때,\n- 해당 장소에서 떨어지는 촛대에 피해를 입혀 부술 수 있게 됨 (촛대를 부술 경우, 1씩 <color=#00ff9c>체력 회복</color>)\n- 해당 상징계 전투에서 간수에게 받는 <color=#fe4b48>피해량</color> -25%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990005].statText
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, <color=#fe4b48>, \n
   EN: In the Symbolic, <color=#F8C200>Level 3 Garde's charge time</color> is reduced to match Level 1 Garde\n- Once fully charged, <color=#F8C200>Garde</color> always activates as <color=#F8C200>Level 3</color>\n\nIn the Symbolic, <color=#F8C200>Attack Chain 2</color> gains +1 tile of width on both the left and right sides\n- The added side range is not affected by range-increasing effects\n\nDuring battle in the Symbolic, when the Warden summons the player to a certain area,\n- The player can destroy the candles falling upon that area (destroying a candle <color=#00ff9c></color>heals 1 <color=#00ff9c>HP</color>)\n- <color=#fe4b48>Damage</color> Taken from the Warden -25% in the said Symbolic battle
   PL: W Symbolicznym <color=#F8C200>czas ładowania Garde 3. poziomu</color> skraca się do czasu Garde 1. poziomu\n- Po naładowaniu <color=#F8C200>Garde</color> uruchamia się zawsze jako <color=#F8C200>3. poziom</color>\n\nW Symbolicznym <color=#F8C200>Atak Kombo 2</color> zyskuje +1 pole szerokości w lewo i w prawo\n- Dodany zakres boczny nie podlega efektom zwiększania zasięgu\n\nW walce w Symbolicznym, gdy Strażnik przywoła gracza w określone miejsce,\n- gracz może niszczyć spadające na to miejsce świece (zburzenie świecy <color=#00ff9c>leczy</color> o 1 <color=#00ff9c>HP</color>)\n- <color=#fe4b48>Obrażenia</color> otrzymywane od Strażnika w tej walce -25%
468. [RPG [I990005] — opis] 한없이 느려질 뿐 완전한 정지란 없다. 그것은 관념으로조차 그려낼 수 없다. 그게 인간의 구조다.\n간수의 권능은 그것을 실체화한다. 정지하라.\n'아니, 그렇지 않다. 나는 그렇지 않다는 말이 안에서 터져 나오려 한다.'\n그는 정지한 것을 부수고 저항할 것이다. 그런 느낌이 솟구쳤기 때문이다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990005].description
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One may slow infinitely close to perfect stillness, but that is an unreachable state. It cannot even be pictured as an idea. Such is the architecture of the human being.\n\nThe Warden's power makes that impossibility real—"Be still."\n\n"No, that isn't me. I refuse to be still." These words strain to burst from within against the judgment.\n\nHe will break what has been stilled. He will rebel.\nBecause that sensation has already begun to rise.
   PL: Można zwalniać bez końca, ale doskonały bezruch nie istnieje. Tego nie da się wyobrazić nawet jako pojęcie. Taka jest budowa człowieka.\nWładza Strażnika urzeczywistnia tę niemożliwość: „Bezruch”.\n„Nie, to nie ja. Nie zgadzam się na bezruch” — te słowa rwą się z wnętrza na przekór wyrokowi.\nZłame to, co zamarło. Zbuntuje się.\nBo to odczucie już zaczęło w nim kipieć.
469. [RPG [I990935] — nazwa wyświetlana] 세월에 깎여나간 부채
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990935].displayName
   limit: do 40 znaków
   EN: Timeworn Fan
   PL: Wachlarz Wycierany Czasem
470. [RPG [I990935] — statystyki przedmiotu] 그림자계 전투에서 시지프 소속 인격이 적에게 가하는 <color=#fe4b48>피해량</color> +10%
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990935].statText
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fe4b48>, </color>, \n
   EN: During battle in the Shadowed:\n"Sisyphe" Identities deal +10% <color=#fe4b48>damage</color> against enemies
   PL: W walce w Zacienionym:\nTożsamości „Sisyphe” zadają +10% <color=#fe4b48>obrażeń</color> wrogom
471. [RPG [I990935] — opis] 이 자는 백화점의 풍화와 함께 세월을 견디며 흉터들을 천으로 꿰어 나갔다. 이것은 그 시간을 견뎌내다 무너진 자를 쓰러뜨렸다는 증표.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990935].description
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This one weathered the time alongside the department store itself, stitching scar after scar together with cloth.\n\nThis is proof of victory against the one who endured the weight of time and ultimately broke beneath it.
   PL: Ten przechodził przez czasy wraz z samym Grand Magasin, zszywając blizny tkaniną.\nTo dowód zwycięstwa nad tym, co przetrwało ciężar czasu i ostatecznie pod nim runęło.
472. [RPG [I990936] — nazwa wyświetlana] 붉게 물든 꽃신
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990936].displayName
   limit: do 40 znaków
   EN: Crimson-stained Flower Shoes
   PL: Szkarłatne Kwiatowe Pantofelki
473. [RPG [I990936] — statystyki przedmiotu] 그림자계 전투에서 턴 시작 시 흐트러짐 상태인 인격 중 체력 비율이 가장 낮은 1명의 <color=#F8C200>흐트러짐 해제</color>. 해당 인격의 최대 체력의 20%만큼 <color=#00ff9c>체력 회복</color>. 르루주 소속인 경우, 회복 대신 <color=#fe4b48>공격 위력 증가</color> 2 부여 (전투당 최대 2회 발동)
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990936].statText
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, <color=#00ff9c>, <color=#fe4b48>, \n
   EN: During battle in the Shadowed,\n- Turn Start: 1 unit with the lowest HP among Staggered Identities <color=#F8C200>recovers from Stagger</color>; then, the said ally <color=#00ff9c>heals</color> 20% <color=#00ff9c>HP</color>\n- If the said unit is a "Le Rouge" Identity, gain 2 <color=#fe4b48>Attack Power Up</color> instead of HP healing effect\n- 2 times per Encounter
   PL: W walce w Zacienionym, na początku tury, 1 Tożsamość w Ogłuszeniu z najniższym HP <color=#F8C200>zdejmuje Ogłuszenie</color>. Następnie <color=#00ff9c>leczy</color> ją o 20% jej maksymalnego HP. Jeśli to Tożsamość „Le Rouge”, zamiast leczenia zyskuje 2 <color=#fe4b48>Zwiększenie Mocy Ataku</color> (maks. 2 razy na potyczkę)
474. [RPG [I990936] — opis] 봄의 잔향이 맴돌던 꽃신은 비체에 덮여 더 이상 이전의 꽃신이 아니게 된 것만 같다. 하지만 그 끈적임 속에서 은은한 봄바람을 내는 신발은 뿌이와 같이 걸었던 날들의 잔향을 남기고 있다.
   źródło: RPGSystem/rpg-loc-item-common-a1c10p3.json :: dataList[key=I990936].description
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The flower shoes that once carried the lingering scent of spring are now smothered in phlegmatic discharge, scarcely resembling what they once were.\n\nAnd yet, from somewhere buried beneath that viscous filth rise the subtle traces of a spring breeze...\n\nA faint aroma that brings to mind the days spent walking beside Pwie.
   PL: Kwiatowe pantofelki, niegdyś przesycone aromatem wiosny, pokrył śluz — wyglądają tak, jakby nie były już tymi pantofelkami.\nA jednak spod tej lepkiej plamy wyłania się delikatny powiew wiosny...\nSubtelny aromat, który przywodzi na myśl dni chodzenia u boku Pwie.

## Tryb RPG [common] — rpg-loc-npc-common-a1c10p1
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-npc-common-a1c10p1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

475. [RPG [N101001] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-common-a1c10p1.json :: dataList[key=N101001].displayName
   limit: do 40 znaków
   EN: ???
   PL: ???

## Tryb RPG [common] — rpg-loc-npc-common-a1c10p2
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-npc-common-a1c10p2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

476. [RPG [N990899] — nazwa wyświetlana] 검은 유체
   źródło: RPGSystem/rpg-loc-npc-common-a1c10p2.json :: dataList[key=N990899].displayName
   limit: do 40 znaków
   EN: Black Larva
   PL: Czarna Larwa

## Tryb RPG [common] — rpg-loc-npc-common-warden-boss-a1c10p2
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

477. [RPG [N999997] — nazwa wyświetlana] 간수
   źródło: RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p2.json :: dataList[key=N999997].displayName
   limit: do 40 znaków
   EN: The Warden
   PL: Strażnik
478. [RPG [N999996] — nazwa wyświetlana] 촛대
   źródło: RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p2.json :: dataList[key=N999996].displayName
   limit: do 40 znaków
   EN: Candle
   PL: Świeca

## Tryb RPG [common] — rpg-loc-npc-common-warden-boss-a1c10p3
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

479. [RPG [N999995] — nazwa wyświetlana] 촛대(광증)
   źródło: RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p3.json :: dataList[key=N999995].displayName
   limit: do 40 znaków
   EN: Candle (Madness)
   PL: Świeca (Obłęd)
480. [RPG [N999994] — nazwa wyświetlana] 촛대(노랑)
   źródło: RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p3.json :: dataList[key=N999994].displayName
   limit: do 40 znaków
   EN: Candle (Yellow)
   PL: Świeca (Żółta)
481. [RPG [N999997C] — nazwa wyświetlana] 간수
   źródło: RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p3.json :: dataList[key=N999997C].displayName
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [common] — rpg-loc-ui-common-a1c10p1
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-ui-common-a1c10p1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

482. [RPG [ReturnToMainUiScene] — tekst] 유리창으로 이동하시겠습니까?\n<color=#ff0000>유리창 복귀 시 현재 탐색 진도가 저장되지 않을 수 있습니다.</color>\n\n※ 탐색 진도는 퀘스트 완료 / 층 이동 / 구역 이동 시 자동으로 저장됩니다.\n유리창으로 이동하기 전, 현재 저장 상태를 확인해주세요.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ReturnToMainUiScene].text
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: Return to the Window?\n<color=#ff0000>Recent progress may be lost.</color>\n\n※ The game saves at the following points: Quest finished / Floor or Area transition.\nPlease verify your last savepoint before exiting to the Window.
   PL: Wrócić do Okna?\n<color=#ff0000>Po powrocie do Okna obecny postęp eksploracji może nie zostać zapisany.</color>\n\n※ Postęp eksploracji zapisuje się automatycznie przy ukończeniu zadania / zmianie piętra / zmianie strefy.\nPrzed powrotem do Okna sprawdź stan zapisu.
483. [RPG [AskToMoveFloor] — tekst] {0}층으로 이동하시겠습니까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=AskToMoveFloor].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Move to Floor {0}?
   PL: Przenieść się na piętro {0}?
484. [RPG [MoveFloorUiDesc] — tekst] 어느 층으로 이동할까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=MoveFloorUiDesc].text
   limit: do 120 znaków
   EN: Which Floor should we go to?
   PL: Na które piętro się przenieść?
485. [RPG [FloorMoveUnboughtConfirmDesc] — tekst] 현재 층에서 아직 구매하지 않은\n아이템이 남아 있습니다.\n다른 층으로 이동하시겠습니까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=FloorMoveUnboughtConfirmDesc].text
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You haven't yet purchased all available items from this floor.\nMove on to a different floor anyway?
   PL: Na tym piętrze wciąż są\nniekupione przedmioty.\nPrzenieść się na inne piętro?
486. [RPG [FloorMoveUnboughtDontShowAgain] — tekst] 팝업 다시 보지 않기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=FloorMoveUnboughtDontShowAgain].text
   limit: do 120 znaków
   EN: Don't show this message again
   PL: Nie pokazuj ponownie tego okna
487. [RPG [DialogueSkipConfirmDesc] — tekst] 스토리를 스킵하시겠습니까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=DialogueSkipConfirmDesc].text
   limit: do 120 znaków
   EN: Skip this story scene?
   PL: Pominąć scenę fabularną?
488. [RPG [DialogueSkipDontShowAgain] — tekst] 팝업 다시 보지 않기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=DialogueSkipDontShowAgain].text
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [RPG [AccumulatedExp] — tekst] 현재 누적 소모 눈알
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=AccumulatedExp].text
   limit: do 120 znaków
   EN: Eyeball Expenditure Tally
   PL: Łącznie wydane Gałki Oczowe
490. [RPG [RemainExpToNextLevel] — tekst] 다음 등급까지
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RemainExpToNextLevel].text
   limit: do 120 znaków
   EN: To Next Tier
   PL: Do następnego poziomu
491. [RPG [ItemFilterAll] — tekst] 전체
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterAll].text
   limit: do 120 znaków
   EN: All
   PL: Wszystko
492. [RPG [ItemFilterKeyItem] — tekst] 퀘스트
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterKeyItem].text
   limit: do 120 znaków
   EN: Quest
   PL: Zadanie
493. [RPG [ItemFilterSurvival] — tekst] 생존
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterSurvival].text
   limit: do 120 znaków
   EN: Survivability
   PL: Przetrwanie
494. [RPG [ItemFilterBasicAttack] — tekst] 기본 공격
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterBasicAttack].text
   limit: do 120 znaków
   EN: Basic Attack
   PL: Atak Podstawowy
495. [RPG [ItemFilterAdditionalAttack] — tekst] 추가 공격
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterAdditionalAttack].text
   limit: do 120 znaków
   EN: Extra Attack
   PL: Dodatkowy Atak
496. [RPG [ItemFilterPrisonerEffect] — tekst] 수감자 효과
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterPrisonerEffect].text
   limit: do 120 znaków
   EN: Sinner Effects
   PL: Efekty Grzeszników
497. [RPG [ItemFilterEtc] — tekst] 기타
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ItemFilterEtc].text
   limit: do 120 znaków
   EN: Other
   PL: Inne
498. [RPG [Item_QuestMark] — tekst] 중요 아이템
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Item_QuestMark].text
   limit: do 120 znaków
   EN: Key Item
   PL: Kluczowy Przedmiot
499. [RPG [Item_Suffix_Disabled] — tekst] {0} (비활성화됨)
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Item_Suffix_Disabled].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} (inactive)
   PL: {0} (nieaktywne)
500. [RPG [rpg_quest_tag_dialogue] — tekst] 대화
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=rpg_quest_tag_dialogue].text
   limit: do 120 znaków
   EN: Dialogue
   PL: Rozmowa
501. [RPG [rpg_quest_tag_battle] — tekst] 전투
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=rpg_quest_tag_battle].text
   limit: do 120 znaków
   EN: Battle
   PL: Walka
502. [RPG [rpg_quest_tag_hunt] — tekst] 사냥
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=rpg_quest_tag_hunt].text
   limit: do 120 znaków
   EN: Eliminate
   PL: Polowanie
503. [RPG [rpg_quest_tag_gather] — tekst] 수집
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=rpg_quest_tag_gather].text
   limit: do 120 znaków
   EN: Gather
   PL: Kolekcja
504. [RPG [rpg_quest_tag_shop] — tekst] 상점
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=rpg_quest_tag_shop].text
   limit: do 120 znaków
   EN: Shop
   PL: Sklep
505. [RPG [rpg_quest_tag_move] — tekst] 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=rpg_quest_tag_move].text
   limit: do 120 znaków
   EN: Travel
   PL: Przejdź
506. [RPG [Common_Ok] — tekst] 확인
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Common_Ok].text
   limit: do 120 znaków
   EN: Confirm
   PL: Potwierdź
507. [RPG [Quest_Tag_Progress] — tekst] 진행도
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Quest_Tag_Progress].text
   limit: do 120 znaków
   EN: Progress
   PL: Postęp
508. [RPG [Quest_Tag_Reward] — tekst] 보상
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Quest_Tag_Reward].text
   limit: do 120 znaków
   EN: Reward
   PL: Nagrody
509. [RPG [Shop_Title] — tekst] 상점
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Title].text
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [RPG [Shop_Category_All] — tekst] 전체
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Category_All].text
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [RPG [Shop_Category_Artifact] — tekst] 아티팩트
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Category_Artifact].text
   limit: do 120 znaków
   EN: Artifacts
   PL: Artefakty
512. [RPG [Shop_Category_Etc] — tekst] 기타
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Category_Etc].text
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [RPG [Shop_Button_Buy] — tekst] 구매
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Button_Buy].text
   limit: do 120 znaków
   EN: Purchase
   PL: Kup
514. [RPG [Shop_SelectedItem_None] — tekst] 구매하실 아이템을 선택해 주세요.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_SelectedItem_None].text
   limit: do 120 znaków
   EN: Select items to purchase.
   PL: Wybierz przedmioty do kupienia.
515. [RPG [Shop_Item_Stock] — tekst] 잔여
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Item_Stock].text
   limit: do 120 znaków
   EN: Stock
   PL: Pozostało
516. [RPG [Shop_Item_Owned] — tekst] 보유 중
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Item_Owned].text
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
517. [RPG [Shop_Item_NotForSale] — tekst] 구매 불가
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Item_NotForSale].text
   limit: do 120 znaków
   EN: Cannot Purchase
   PL: Zakup niemożliwy
518. [RPG [Shop_Empty_Item_List] — tekst] 표시할 상품이 없습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Shop_Empty_Item_List].text
   limit: do 120 znaków
   EN: No items to display.
   PL: Brak towarów do wyświetlenia.
519. [RPG [Log_ItemAcquired] — tekst] 아이템 획득: {0} x{1}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_ItemAcquired].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Item Obtained: {0} x{1}
   PL: Zdobyto przedmiot: {0} x{1}
520. [RPG [Log_ItemAcquiredKeyItem] — tekst] 아이템 획득: <color=#{2}>{0} x{1}</color>
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_ItemAcquiredKeyItem].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#{2}>, </color>, {2}, {0}, {1}
   EN: Item Obtained: <color=#{2}>{0} x{1}</color>
   PL: Zdobyto przedmiot: <color=#{2}>{0} x{1}</color>
521. [RPG [Log_CurrencyEarned] — tekst] 눈알 {0}개 획득
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_CurrencyEarned].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obtained: {0} eyeballs
   PL: Zdobyto {0} Gałek Oczowych
522. [RPG [Log_Purchased] — tekst] 구매: {0} x{1} ({2} 소모)
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_Purchased].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Purchased: {0} x{1} ({2} spent)
   PL: Kupno: {0} x{1} (wydano {2})
523. [RPG [Log_PurchasedKeyItem] — tekst] 구매: <color=#{3}>{0} x{1}</color> ({2} 소모)
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_PurchasedKeyItem].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#{3}>, </color>, {3}, {0}, {1}, {2}
   EN: Purchased: <color=#{3}>{0} x{1}</color> ({2} spent)
   PL: Kupno: <color=#{3}>{0} x{1}</color> (wydano {2})
524. [RPG [Log_NpcInteracted] — tekst] 대화를 끝냈다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_NpcInteracted].text
   limit: do 120 znaków
   EN: Ended the conversation.
   PL: Zakończono rozmowę.
525. [RPG [Log_ProjectileRemoved] — tekst] 투사체 제거: {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_ProjectileRemoved].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Projectile Removed: {0}
   PL: Usunięto pocisk: {0}
526. [RPG [Log_ChoiceSelected] — tekst] 선택: {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_ChoiceSelected].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Choice Made: {0}
   PL: Wybór: {0}
527. [RPG [Log_QuestAcquired] — tekst] <color=#{1}>퀘스트 발생: {0}</color>
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_QuestAcquired].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#{1}>, </color>, {1}, {0}
   EN: <color=#{1}>Began Quest: {0}</color>
   PL: <color=#{1}>Zaczęto zadanie: {0}</color>
528. [RPG [Log_QuestCompleted] — tekst] 퀘스트 완료: {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_QuestCompleted].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Quest Completed: {0}
   PL: Ukończono zadanie: {0}
529. [RPG [Log_QuestGoalProgress] — tekst] 목표 진행: {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_QuestGoalProgress].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Quest Progress: {0}
   PL: Postęp zadania: {0}
530. [RPG [Log_BattleResultSync] — tekst] 전투 결과 반영({0}): HP {1}/{2}, MP {3}/{4}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_BattleResultSync].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, {4}
   EN: Battle Outcome Reflected: ({0}): HP {1}/{2}, MP{3}/{4}
   PL: Odzwierciedlenie wyniku walki ({0}): HP {1}/{2}, MP {3}/{4}
531. [RPG [Log_BattleDefeatHp] — tekst] 전투 패배: HP {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_BattleDefeatHp].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Battle Lost: HP {0}
   PL: Przegrana walka: HP {0}
532. [RPG [Log_CheatVitals] — tekst] 치트: {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_CheatVitals].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cheat: {0}
   PL: Cheat: {0}
533. [RPG [Log_EventEffectVitals] — tekst] 이벤트 효과: {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_EventEffectVitals].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Event Effect :{0}
   PL: Efekt zdarzenia: {0}
534. [RPG [Log_RecruitFullRecover] — tekst] 동료 영입({0}): HP/정신력 전체 회복
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_RecruitFullRecover].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ally Gained ({0}): Fully Heal HP/SP
   PL: Nowy sojusznik ({0}): pełne wyleczenie HP/SP
535. [RPG [Log_VitalsNoChange] — tekst] 변화 없음
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_VitalsNoChange].text
   limit: do 120 znaków
   EN: No Changes
   PL: Bez zmian
536. [RPG [Log_NpcDefeated] — tekst] {0} 처치
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_NpcDefeated].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defeated {0}
   PL: Pokonano: {0}
537. [RPG [Log_PlayerDead] — tekst] 플레이어 사망
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_PlayerDead].text
   limit: do 120 znaków
   EN: Player Dead
   PL: Gracz poległ
538. [RPG [Log_BattleEntered] — tekst] 전투 진입
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_BattleEntered].text
   limit: do 120 znaków
   EN: Commence Battle
   PL: Rozpoczyna się walka
539. [RPG [Log_BattleWin] — tekst] 전투 승리
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_BattleWin].text
   limit: do 120 znaków
   EN: Battle Won
   PL: Zwycięstwo w walce
540. [RPG [Log_BattleLose] — tekst] 전투 패배
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_BattleLose].text
   limit: do 120 znaków
   EN: Battle Lost
   PL: Porażka w walce
541. [RPG [Log_RestSpotHealed] — tekst] 체력이 전체 회복되었습니다
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_RestSpotHealed].text
   limit: do 120 znaków
   EN: HP fully healed
   PL: HP zostało całkowicie wyleczone
542. [RPG [Log_EscapeBlocked] — tekst] 지금은 이곳을 벗어날 수 없다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_EscapeBlocked].text
   limit: do 120 znaków
   EN: Can't leave this room at the moment.
   PL: W tej chwili nie da się stąd wyjść.
543. [RPG [Log_WardenAppeared] — tekst] 서늘한 불길함이 서서히 조여온다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_WardenAppeared].text
   limit: do 120 znaków
   EN: A sense of unsettling omen creeps in.
   PL: Chłodna złowrogość powoli się zaciska.
544. [RPG [Log_SuicideBlocked] — tekst] 이것으로는 도피할 수 없는 것 같다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Log_SuicideBlocked].text
   limit: do 120 znaków
   EN: This cannot be the way out.
   PL: Najwyraźniej tą drogą nie da się uciec.
545. [RPG [ProgressPopup_Title] — tekst] 시지프 백화점
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ProgressPopup_Title].text
   limit: do 120 znaków
   EN: Grand Magasin Sisyphe
   PL: Grand Magasin Sisyphe
546. [RPG [ProgressPopup_Suicide] — tekst] 샘터로\n돌아가기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ProgressPopup_Suicide].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Return\nto Fount
   PL: Powrót\ndo Źródła
547. [RPG [ProgressPopup_EnemyAttackIndication] — tekst] 적 공격 예고 표시
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ProgressPopup_EnemyAttackIndication].text
   limit: do 120 znaków
   EN: Show precise enemy attack range
   PL: Pokaż zapowiedź ataku wroga
548. [RPG [ProgressPopup_MyAttackIndication] — tekst] 내 공격 범위 표시
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ProgressPopup_MyAttackIndication].text
   limit: do 120 znaków
   EN: Show precise ally attack range
   PL: Pokaż zakres mojego ataku
549. [RPG [ProgressPopup_Restore] — tekst] 세이브 복원
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=ProgressPopup_Restore].text
   limit: do 120 znaków
   EN: Restore Savepoint
   PL: Przywróć zapis
550. [RPG [RestorePopup_Title] — tekst] 세이브 복원
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_Title].text
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [RPG [RestorePopup_Checking] — tekst] 확인 중…
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_Checking].text
   limit: do 120 znaków
   EN: Checking...
   PL: Sprawdzanie…
552. [RPG [RestorePopup_FoundNoQuest] — tekst] 복원할 수 있는 자동 저장 지점이 있습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_FoundNoQuest].text
   limit: do 120 znaków
   EN: Restorable Autosave found.
   PL: Znaleziono punkt automatycznego zapisu do przywrócenia.
553. [RPG [RestoreCompare_ColCurrent] — tekst] 마지막 저장
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestoreCompare_ColCurrent].text
   limit: do 120 znaków
   EN: Last Savepoint
   PL: Ostatni zapis
554. [RPG [RestoreCompare_ColBackup] — tekst] 복원
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestoreCompare_ColBackup].text
   limit: do 120 znaków
   EN: Restore
   PL: Przywróć
555. [RPG [RestoreCompare_NoQuest] — tekst] 없음
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestoreCompare_NoQuest].text
   limit: do 120 znaków
   EN: None
   PL: Brak
556. [RPG [RestoreCompare_Unknown] — tekst] 확인 불가
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestoreCompare_Unknown].text
   limit: do 120 znaków
   EN: Not Found
   PL: Nie znaleziono
557. [RPG [RestoreCompare_SavedAt] — tekst] 저장한 시간 : {0}
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestoreCompare_SavedAt].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Saved At: {0}
   PL: Czas zapisu: {0}
558. [RPG [RestorePopup_None] — tekst] 되돌릴 수 있는 자동 저장 지점이 없습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_None].text
   limit: do 120 znaków
   EN: No restorable Autosave found.
   PL: Brak punktów automatycznego zapisu do przywrócenia.
559. [RPG [RestorePopup_LoadFailed] — tekst] 자동 저장 정보를 확인할 수 없습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_LoadFailed].text
   limit: do 120 znaków
   EN: Cannot verify autosave information.
   PL: Nie można sprawdzić informacji o automatycznym zapisie.
560. [RPG [RestorePopup_Confirm] — tekst] 이 지점 이후의 진행은 사라집니다. 되돌릴 수 없습니다.\n세이브를 복원하시겠습니까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_Confirm].text
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Any progress you've made since that savepoint will be deleted. This process is irreversible. Restore save anyway?
   PL: Cały postęp po tym punkcie przepadnie. Nie da się go cofnąć.\nPrzywrócić zapis?
561. [RPG [RestorePopup_Running] — tekst] 복원 중입니다…
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_Running].text
   limit: do 120 znaków
   EN: Restoring...
   PL: Przywracanie…
562. [RPG [RestorePopup_NeedRestart] — tekst] 복원되었습니다. 지금부터의 진행은 저장되지 않으니 게임을 다시 시작해 주세요.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_NeedRestart].text
   limit: do 120 znaków
   EN: Restored. Any progress made after this point will not be saved. Please restart the game.
   PL: Przywrócono. Postęp od tej chwili nie zostanie zapisany. Uruchom grę ponownie.
563. [RPG [RestorePopup_Close] — tekst] 닫기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=RestorePopup_Close].text
   limit: do 120 znaków
   EN: Close
   PL: Zamknij
564. [RPG [Inventory_Empty] — tekst] 보유 중인 아이템이 없습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Inventory_Empty].text
   limit: do 120 znaków
   EN: No items in inventory.
   PL: Nie masz żadnych przedmiotów.
565. [RPG [Inventory_NotSelected] — tekst] 선택된 아이템이 없습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Inventory_NotSelected].text
   limit: do 120 znaków
   EN: No items selected.
   PL: Nie wybrano przedmiotów.
566. [RPG [LogPopup_Title] — tekst] 전체 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=LogPopup_Title].text
   limit: do 120 znaków
   EN: Log History
   PL: Pełny dziennik
567. [RPG [LogPopup_Tab_Story] — tekst] 스토리 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=LogPopup_Tab_Story].text
   limit: do 120 znaków
   EN: Story Logs
   PL: Dziennik fabuły
568. [RPG [LogPopup_Tab_System] — tekst] 시스템 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=LogPopup_Tab_System].text
   limit: do 120 znaków
   EN: System Logs
   PL: Dziennik systemu
569. [RPG [Setting_Tab_Sisyphus] — tekst] 시지프
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Tab_Sisyphus].text
   limit: do 120 znaków
   EN: Sisyphe
   PL: Sisyphe
570. [RPG [Setting_Sisyphus_UiSetting] — tekst] UI 설정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_UiSetting].text
   limit: do 120 znaków
   EN: UI Settings
   PL: Ustawienia UI
571. [RPG [Setting_Sisyphus_KeyManual] — tekst] 단축키 매뉴얼
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_KeyManual].text
   limit: do 120 znaków
   EN: Keyboard shortcuts guide
   PL: Przewodnik po skrótach klawiszowych
572. [RPG [Setting_Sisyphus_CensorDeadscene] — tekst] 데드씬 검열
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_CensorDeadscene].text
   limit: do 120 znaków
   EN: Censor death scenes
   PL: Cenzura scen śmierci
573. [RPG [Setting_Sisyphus_LightMode] — tekst] 라이트 모드
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_LightMode].text
   limit: do 120 znaków
   EN: Lighting Mode
   PL: Tryb oświetlenia
574. [RPG [Setting_Sisyphus_Brightness] — tekst] 밝기 조정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Brightness].text
   limit: do 120 znaków
   EN: Adjust Brightness
   PL: Regulacja jasności
575. [RPG [Setting_Sisyphus_BrightnessCeiling] — tekst] 밝기 상한
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_BrightnessCeiling].text
   limit: do 120 znaków
   EN: Limit Peak Brightness
   PL: Limit jasności
576. [RPG [Setting_Sisyphus_MoveAssist] — tekst] 이동 방향 보정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MoveAssist].text
   limit: do 120 znaków
   EN: Directional Movement Correction
   PL: Korekta kierunku ruchu
577. [RPG [Setting_Sisyphus_RunStartDelay] — tekst] 달리기 제한 시간
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_RunStartDelay].text
   limit: do 120 znaków
   EN: Auto-Sprint Timer
   PL: Limit czasu biegu
