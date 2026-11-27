# Paczka AI P42 (Fala 2 · 2C) — Tabela modeli postaci oraz interfejs, zadania i przedmioty RPG Canto X (część 4/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P42_2c_modele_i_rpg_ui_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P42_2c_modele_i_rpg_ui_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tryb RPG [floor-b1] — rpg-loc-quest-floor-b1-b
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-quest-floor-b1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

1. [RPG [Q-1010] — opis] 뿌이보고 마음에 드는 에스컬레이터를 고르라고 했다. 뿌이가 고른 에스컬레이터를 정의내리자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1010].description
   limit: do 120 znaków
   EN: We let Pwie pick whichever escalator they liked. Now to define the escalator they chose.
   PL: Kazaliśmy Pwie wybrać schody ruchome, które mu się spodobają. Określmy, czym jest wybrane przez niego.
2. [RPG [Q-1010] — krok 1 — cel zadania 1] 에스컬레이터 고르기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1010].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Choose an Escalator
   PL: Wybieramy schody ruchome
3. [RPG [Q-1011] — tytuł] 지하 2층 에스컬레이터로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1011].title
   limit: do 40 znaków
   EN: Head to B2F's Escalator
   PL: Udaj się do schodów na poziom -2
4. [RPG [Q-1011] — opis] 지하 2층 에스컬레이터를 타고 내려가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1011].description
   limit: do 120 znaków
   EN: Let's take B2F's escalator down.
   PL: Wjedźmy schodami ruchomymi w dół, na poziom -2.
5. [RPG [Q-1011] — krok 1 — cel zadania 1] 지하 2층 에스컬레이터로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1011].steps[#0].goalDescription1
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b1] — rpg-loc-quest-floor-b1
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-quest-floor-b1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

6. [RPG [Q-1000] — krok 1 — cel zadania 1] 지하 1층 식품관 진입
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1000].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to B1F - Food Hall
   PL: Wejście na poziom -1: Salon Spożywczy
7. [RPG [Q-1000] — krok 2 — cel zadania 1] 식품관 진입대화
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1000].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Discuss the Food Hall
   PL: Rozmowa przy wejściu do Salonu Spożywczego
8. [RPG [Q-1001] — tytuł] 지하 2층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1001].title
   limit: do 40 znaków
   EN: Head to B2F
   PL: Udaj się na poziom -2
9. [RPG [Q-1001] — opis] 부셰가 요리해 준 황금고치를 얻었다. 이제 지하 2층으로 내려갈 방법을 찾아봐야 한다. 지나왔던 복도의 아래쪽에 있던 길로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1001].description
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Boucher cooked us a "dish" called the Golden Cocoon. Now, to find our way down to B2F.\n\nLet's check the path down from the corridor we walked through.
   PL: Boucher przygotował dla nas „danie” zwane Złotym Kokonem. Teraz trzeba znaleźć drogę na poziom -2. Sprawdźmy przejście w dolnej części korytarza, którym szliśmy.
10. [RPG [Q-1001] — krok 1 — cel zadania 1] 지하 2층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head down to B2F
   PL: Udaj się na poziom -2
11. [RPG [Q-1002] — tytuł] 내려가는 에스컬레이터를 찾아보기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1002].title
   limit: do 50 znaków
   EN: Look for a Descending Escalator
   PL: Poszukaj schodów ruchomych w dół
12. [RPG [Q-1002] — opis] 에스컬레이터로 가득 찬 곳으로 왔다. 에스컬레이터들을 조사해서 지하 2층으로 향하는 에스컬레이터가 무엇인지 찾아보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1002].description
   limit: do 210 znaków
   EN: We found ourselves in a room full of escalators that lead who knows where. We should investigate these escalators and find the one that can bring us down to B2F.
   PL: Trafiliśmy do miejsca wypełnionego schodami ruchomymi prowadzącymi, nie wiadomo dokąd. Zbadajmy je i znajdźmy te, które zawiodą nas na poziom -2.
13. [RPG [Q-1002] — krok 1 — cel zadania 1] 에스컬레이터 조사하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1002].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Investigate the escalators
   PL: Zbadaj schody ruchome
14. [RPG [Q-1003] — tytuł] 푸드코트로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1003].title
   limit: do 40 znaków
   EN: Head to the Food Court
   PL: Udaj się do Strefy Gastronomicznej
15. [RPG [Q-1003] — opis] 지하 1층으로 내려왔다. 지하의 풍경은 지상에 있던 매장들과는 사뭇 달라 보인다. 고치를 찾기 위해서는 푸드코트라는 곳으로 가보는 게 좋을 것 같다. 바닥에 달팽이 껍질이 그려진 곳으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1003].description
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Made our way down to B1F. It certainly has a different feel from the upper floors...\nWe should probably head to this place they call the "Food Court" if we want to find the Golden Cocoon. Let's look for the drawing of a snail shell on the ground.
   PL: Zeszliśmy na poziom -1. Podziemia wyglądają zupełnie inaczej niż sklepy na wyższych piętrach. Żeby znaleźć kokon, dobrze będzie udać się do miejsca zwanego Strefą Gastronomiczną. Poszukajmy miejsca z narysowaną muszlą ślimaka na podłodze.
16. [RPG [Q-1003] — krok 1 — cel zadania 1] 푸드코트로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1003].steps[#0].goalDescription1
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [RPG [Q-1004] — tytuł] 수셰프 쫓아가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1004].title
   limit: do 40 znaków
   EN: Pursue the Sous Chef!
   PL: Pogoń za Sous Chef
18. [RPG [Q-1004] — opis] 수셰프라는 자를 만났다. 그자는 황금고치를 부셰라는 자의 창고에서 보았다고 했다. 도망친 수셰프를 쫓아가서 황금고치에 대한 정보를 더 얻어내자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1004].description
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Met someone called "Sous Chef." We were told that she'd seen the Golden Cocoon in someone called Boucher's storeroom.\nLet's chase after Sous Chef and find out more about the Golden Cocoon.
   PL: Poznaliśmy kogoś zwanego „Sous Chef”. Podobno widziała Złoty Kokon w magazynie kogoś o imieniu Boucher. Pędźmy za uciekającą Sous Chef i wyciągnijmy od niej więcej informacji o Złotym Kokonie.
19. [RPG [Q-1004] — krok 1 — cel zadania 1] 수셰프 쫓아가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1004].steps[#0].goalDescription1
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [RPG [Q-1005] — tytuł] 부셰에게 가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1005].title
   limit: do 40 znaków
   EN: Visit Boucher
   PL: Odwiedź Bouchera
21. [RPG [Q-1005] — opis] 수셰프로부터 지하 1층의 플로어 매니저, 부셰라는 자에 대해 알아냈다. 부셰에게 가서 황금고치를 얻을 수 있는 방법에 대해 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1005].description
   limit: do 200 znaków
   EN: Sous Chef told us about Boucher, the B1F Floor Manager. Let's find Boucher and ask if there's any way we could convince him to give us the Golden Cocoon.
   PL: Od Sous Chef dowiedzieliśmy się o Boucherze, Kierowniku Piętra poziomu -1. Odwiedźmy go i zapytajmy, jak można zdobyć Złoty Kokon.
22. [RPG [Q-1005] — krok 1 — cel zadania 1] 부셰에게 가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1005].steps[#0].goalDescription1
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [RPG [Q-1006] — tytuł] 피식자의 사유를 가져오기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1006].title
   limit: do 60 znaków
   EN: Bring Back the Ruminations of the Prey
   PL: Przynieś Rozmyślania Ofiary
24. [RPG [Q-1006] — opis] 부셰가 가지고 있는 황금고치를 얻기 위해서는 피식자의 사유라고 불리는 고기를 가져와야 한다. 신선정육코너의 어딘가에 매달려있는 피식자의 사유를 얻어온 후 부셰에게 건네주자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1006].description
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Boucher said he's willing to part with his Golden Cocoon... but only for this cut of meat called "Ruminations of the Prey," which can be found hanging somewhere inside the Fresh Meat Section.\n\nWe should find that cut of meat and hand it over to Boucher.
   PL: Boucher odda swój Złoty Kokon… ale tylko w zamian za kawał mięsa zwany „Rozmyślaniami Ofiary”, wiszący gdzieś w Stoisku ze Świeżym Mięsem. Znajdźmy ten kawał i przekażmy go Boucherowi.
25. [RPG [Q-1006] — krok 1 — cel zadania 1] 피식자의 사유를 가져오기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1006].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Bring back the Ruminations of the Prey
   PL: Przynieś Rozmyślania Ofiary
26. [RPG [Q-1008] — tytuł] 에스컬레이터실로 복귀
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1008].title
   limit: do 50 znaków
   EN: Return to the Hall of Escalators
   PL: Powrót do Hali Schodów Ruchomych
27. [RPG [Q-1008] — krok 1 — cel zadania 1] 에스컬레이터실 복귀
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1008].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Return to the room of escalators
   PL: Wróć do Hali Schodów Ruchomych
28. [RPG [Q-1009] — tytuł] 에스컬레이터를 정의 내리기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1009].title
   limit: do 40 znaków
   EN: Define the Escalator
   PL: Określ schody ruchome
29. [RPG [Q-1009] — opis] 잔느의 말에 의하면 아래로 내려가는 에스컬레이터를 찾는 것이 아니라 에스컬레이터를 정의 내려야 하는 것 같다. 사다리, 혹은 언덕이나 신발. 이 중에 어떤 것으로 정의 내리라고 뫼르소에게 말해볼까?
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1009].description
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: According to Jeanne's cryptic hints, we shouldn't look for an escalator that leads downstairs... but define one instead. Meursault gave me three options—a ladder, a hill, or a shoe.\n\nWhich of these should I tell Meursault to define the escalator as?
   PL: Według zagadkowych wskazówek Jeanne nie powinniśmy szukać schodów ruchomych prowadzących w dół… lecz określić, czym są. Drabina, wzgórze albo but. Którą z tych opcji mam kazać Meursaultowi wybrać?
30. [RPG [Q-1009] — krok 1 — cel zadania 1] 에스컬레이터를 사다리, 언덕, 신발 중에 하나로 정의내리기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1009].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Define the escalator: a ladder, a hill, or a shoe?
   PL: Określ schody ruchome jako drabinę, wzgórze albo but
31. [RPG [Q-1010] — tytuł] 에스컬레이터 작동 시키기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1010].title
   limit: do 40 znaków
   EN: Activate the Escalator
   PL: Uruchom schody ruchome
32. [RPG [Q-1011] — tytuł] 에스컬레이터로 내려가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1.json :: dataList[key=Q-1011].title
   limit: do 40 znaków
   EN: Take the Escalator Down
   PL: Zjedź schodami ruchomymi

## Tryb RPG [floor-b1] — rpg-loc-swarm-mob-floor-b1-a
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

33. [RPG [swarm_baggar] — nazwa wyświetlana] 가죽 지갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_baggar].displayName
   limit: do 40 znaków
   EN: Leather Wallet
   PL: Skórzany Portfel
34. [RPG [swarm_collecter_type_e] — nazwa wyświetlana] 눈 시식담당자
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_collecter_type_e].displayName
   limit: do 40 znaków
   EN: Eye Taste Tester
   PL: Degustator Ok
35. [RPG [swarm_collecter_type_m] — nazwa wyświetlana] 입 시식담당자
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_collecter_type_m].displayName
   limit: do 40 znaków
   EN: Mouth Taste Tester
   PL: Degustator Ust
36. [RPG [swarm_collector_type_n] — nazwa wyświetlana] 코 시식담당자
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_collector_type_n].displayName
   limit: do 40 znaków
   EN: Nose Taste Tester
   PL: Degustator Nosu
37. [RPG [swarm_denim_baggar] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_denim_baggar].displayName
   limit: do 40 znaków
   EN: Denim Wallet
   PL: Portfel z Denimu
38. [RPG [swarm_resident] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_resident].displayName
   limit: do 40 znaków
   EN: Thirsty Kaki
   PL: Spragniony Le Kaki
39. [RPG [swarm_resident_b] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json :: dataList[key=swarm_resident_b].displayName
   limit: do 40 znaków
   EN: Hungry Kaki
   PL: Głodny Le Kaki

## Tryb RPG [floor-b1] — rpg-loc-swarm-mob-floor-b1-b
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

40. [RPG [swarm_baggar] — nazwa wyświetlana] 가죽 지갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_baggar].displayName
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [RPG [swarm_collecter_type_e] — nazwa wyświetlana] 눈 시식담당자
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_collecter_type_e].displayName
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [RPG [swarm_collecter_type_m] — nazwa wyświetlana] 입 시식담당자
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_collecter_type_m].displayName
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [RPG [swarm_collector_type_n] — nazwa wyświetlana] 코 시식담당자
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_collector_type_n].displayName
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [RPG [swarm_denim_baggar] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_denim_baggar].displayName
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [RPG [swarm_horizontal_hide] — nazwa wyświetlana] 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_horizontal_hide].displayName
   limit: do 40 znaków
   EN: Crawling Leather
   PL: Pełzająca Skóra
46. [RPG [swarm_resident] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_resident].displayName
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [RPG [swarm_resident_b] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_resident_b].displayName
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [RPG [swarm_resident_b_fisher] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_resident_b_fisher].displayName
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [RPG [swarm_resident_fisher] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json :: dataList[key=swarm_resident_fisher].displayName
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b2] — rpg-loc-location-floor-b2-b
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-location-floor-b2-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

50. [RPG [220100] — tekst] 방적장
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=220100].text
   limit: do 120 znaków
   EN: Spinning Mill
   PL: Przędzalnia
51. [RPG [220200] — tekst] 타래둥지
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=220200].text
   limit: do 120 znaków
   EN: Skein Nest
   PL: Gniazdo Przędzy
52. [RPG [220300] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=220300].text
   limit: do 120 znaków
   EN: Corridor
   PL: Korytarz
53. [RPG [220400] — tekst] 염색실
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=220400].text
   limit: do 120 znaków
   EN: Dyehouse
   PL: Farbiarnia
54. [RPG [220500] — tekst] 염료 눈물 창고
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=220500].text
   limit: do 120 znaków
   EN: Dye-tear Storage
   PL: Magazyn Łez Barwniczych
55. [RPG [221400] — tekst] 숨겨진 에스컬레이터실
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=221400].text
   limit: do 120 znaków
   EN: Secret Escalator Hall
   PL: Ukryta Hala Schodów Ruchomych
56. [RPG [221500] — tekst] 타래둥지 복도
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=221500].text
   limit: do 120 znaków
   EN: Skein Nest Corridor
   PL: Korytarz Gniazda Przędzy
57. [RPG [221600] — tekst] 염료 눈물 창고 복도
   źródło: RPGSystem/rpg-loc-location-floor-b2-b.json :: dataList[key=221600].text
   limit: do 120 znaków
   EN: Dye-tear Storage Corridor
   PL: Korytarz Magazynu Łez Barwniczych

## Tryb RPG [floor-b2] — rpg-loc-location-floor-b2
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-location-floor-b2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

58. [RPG [220100] — tekst] 방적장
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=220100].text
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [RPG [220200] — tekst] 타래둥지
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=220200].text
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [RPG [220300] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=220300].text
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [RPG [220400] — tekst] 염색실
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=220400].text
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [RPG [220500] — tekst] 염료 눈물 창고
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=220500].text
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [RPG [221400] — tekst] 숨겨진 에스컬레이터실
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=221400].text
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [RPG [221500] — tekst] 타래둥지 복도
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=221500].text
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [RPG [221600] — tekst] 염료 눈물 창고 복도
   źródło: RPGSystem/rpg-loc-location-floor-b2.json :: dataList[key=221600].text
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b2] — rpg-loc-npc-floor-b2-a-enemy
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

66. [RPG [N202031] — nazwa wyświetlana] 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N202031].displayName
   limit: do 40 znaków
   EN: Red Needlekin
   PL: Czerwona Igiełka
67. [RPG [N202031Alt] — nazwa wyświetlana] 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N202031Alt].displayName
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [RPG [N202032] — nazwa wyświetlana] 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N202032].displayName
   limit: do 40 znaków
   EN: Green Needlekin
   PL: Zielona Igiełka
69. [RPG [N112001] — nazwa wyświetlana] 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N112001].displayName
   limit: do 40 znaków
   EN: Macerating Yellow Tears
   PL: Rozmiękające Żółte Łzy
70. [RPG [N112002] — nazwa wyświetlana] 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N112002].displayName
   limit: do 40 znaków
   EN: Festering Red Tears
   PL: Ropiejące Czerwone Łzy
71. [RPG [N112003] — nazwa wyświetlana] 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N112003].displayName
   limit: do 40 znaków
   EN: Overflowing Blue Tears
   PL: Przepełnione Niebieskie Łzy
72. [RPG [N202034] — nazwa wyświetlana] 검은 실
   źródło: RPGSystem/rpg-loc-npc-floor-b2-a-enemy.json :: dataList[key=N202034].displayName
   limit: do 40 znaków
   EN: Blackthread
   PL: Czarna Nić

## Tryb RPG [floor-b2] — rpg-loc-npc-floor-b2-b-enemy
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

73. [RPG [N202202] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202202].displayName
   limit: do 40 znaków
   EN: Le Noir Priest
   PL: Kapłan Le Noir
74. [RPG [N202203] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202203].displayName
   limit: do 40 znaków
   EN: Le Noir Sales Associate
   PL: Pracownik Le Noir
75. [RPG [N202204] — nazwa wyświetlana] 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202204].displayName
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [RPG [N202206] — nazwa wyświetlana] 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202206].displayName
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [RPG [N202207] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202207].displayName
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [RPG [N202208] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202208].displayName
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [RPG [N202214] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202214].displayName
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [RPG [N202215] — nazwa wyświetlana] 르누아르 메종 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202215].displayName
   limit: do 50 znaków
   EN: Maison du Noir Sales Associate
   PL: Pracownik Maison du Noir
81. [RPG [N202216] — nazwa wyświetlana] 르누아르 신발관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202216].displayName
   limit: do 60 znaków
   EN: Le Noir Footwear Hall Sales Associate
   PL: Pracownik Salonu Obuwia Le Noir
82. [RPG [N202217] — nazwa wyświetlana] 르누아르 컨템포러리 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202217].displayName
   limit: do 60 znaków
   EN: Le Noir Contemporary Hall Sales Associate
   PL: Pracownik Salonu Contempora Le Noir
83. [RPG [N202211] — nazwa wyświetlana] 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202211].displayName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [RPG [N202212] — nazwa wyświetlana] 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202212].displayName
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [RPG [N202213] — nazwa wyświetlana] 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202213].displayName
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [RPG [N202290] — nazwa wyświetlana] 지하 2층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202290].displayName
   limit: do 40 znaków
   EN: B2F Floor Manager
   PL: Kierownik Piętra -2
87. [RPG [N202291] — nazwa wyświetlana] 위선의 붉은 실타래
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202291].displayName
   limit: do 40 znaków
   EN: Red Thread of Hypocrisy
   PL: Czerwona Przędza Obłudy
88. [RPG [N202292] — nazwa wyświetlana] 기만의 하얀 실타래
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202292].displayName
   limit: do 40 znaków
   EN: White Thread of Deception
   PL: Biała Przędza Oszustwa
89. [RPG [N202293] — nazwa wyświetlana] 방임의 푸른 실타래
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202293].displayName
   limit: do 40 znaków
   EN: Blue Thread of Neglect
   PL: Niebieska Przędza Zaniedbania
90. [RPG [N202294] — nazwa wyświetlana] 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202294].displayName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [RPG [N202295] — nazwa wyświetlana] 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202295].displayName
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [RPG [N202296] — nazwa wyświetlana] 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202296].displayName
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [RPG [N202271] — nazwa wyświetlana] 사나워진 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202271].displayName
   limit: do 40 znaków
   EN: Ferocious Le Noir Priest
   PL: Rozwścieczony Kapłan Le Noir
94. [RPG [N202272] — nazwa wyświetlana] 사나워진 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202272].displayName
   limit: do 40 znaków
   EN: Ferocious Le Noir Associate
   PL: Rozwścieczony Pracownik Le Noir
95. [RPG [N202273] — nazwa wyświetlana] 사나워진 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202273].displayName
   limit: do 40 znaków
   EN: Ferocious Red Needlekin
   PL: Rozwścieczona Czerwona Igiełka
96. [RPG [N202274] — nazwa wyświetlana] 사나워진 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202274].displayName
   limit: do 40 znaków
   EN: Ferocious Green Needlekin
   PL: Rozwścieczona Zielona Igiełka
97. [RPG [N202280] — nazwa wyświetlana] 사나워진 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202280].displayName
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [RPG [N202281] — nazwa wyświetlana] 사나워진 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202281].displayName
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [RPG [N202275] — nazwa wyświetlana] 사나워진 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202275].displayName
   limit: do 50 znaków
   EN: Ferocious Macerating Yellow Tears
   PL: Rozwścieczone Rozmiękające Żółte Łzy
100. [RPG [N202276] — nazwa wyświetlana] 사나워진 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202276].displayName
   limit: do 50 znaków
   EN: Ferocious Festering Red Tears
   PL: Rozwścieczone Ropiejące Czerwone Łzy
101. [RPG [N202277] — nazwa wyświetlana] 사나워진 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202277].displayName
   limit: do 50 znaków
   EN: Ferocious Overflowing Blue Tears
   PL: Rozwścieczone Przepełnione Niebieskie Łzy
102. [RPG [N202278] — nazwa wyświetlana] 사나워진 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202278].displayName
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [RPG [N202279] — nazwa wyświetlana] 사나워진 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json :: dataList[key=N202279].displayName
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b2] — rpg-loc-npc-floor-b2-b
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-npc-floor-b2-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

104. [RPG [N202104] — nazwa wyświetlana] 줄 선 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202104].displayName
   limit: do 40 znaków
   EN: Queueing Red Needlekin
   PL: Czerwona Igiełka w Kolejce
105. [RPG [N202105] — nazwa wyświetlana] 줄 선 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202105].displayName
   limit: do 40 znaków
   EN: Queueing Green Needlekin
   PL: Zielona Igiełka w Kolejce
106. [RPG [N202105B] — nazwa wyświetlana] 줄 선 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202105B].displayName
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [RPG [N202105C] — nazwa wyświetlana] 줄 선 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202105C].displayName
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [RPG [N202107] — nazwa wyświetlana] 르누아르 경비원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202107].displayName
   limit: do 40 znaków
   EN: Le Noir Guard
   PL: Strażnik Le Noir
109. [RPG [N202108] — nazwa wyświetlana] 르누아르 메종
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202108].displayName
   limit: do 40 znaków
   EN: Maison du Noir
   PL: Maison du Noir
110. [RPG [N202109] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202109].displayName
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [RPG [N202101] — nazwa wyświetlana] 팔레트
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202101].displayName
   limit: do 40 znaków
   EN: Palette
   PL: Paleta
112. [RPG [N202102] — nazwa wyświetlana] 퍼티
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202102].displayName
   limit: do 40 znaków
   EN: Putty
   PL: Putty
113. [RPG [N2021022] — nazwa wyświetlana] 퍼티
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N2021022].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [RPG [N202110] — nazwa wyświetlana] 르누아르 경비원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202110].displayName
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [RPG [N202103] — nazwa wyświetlana] 지하 2층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202103].displayName
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [RPG [N202121] — nazwa wyświetlana] 바느질의 왕
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202121].displayName
   limit: do 40 znaków
   EN: King of Needleworks
   PL: Król Szycia
117. [RPG [N202111] — nazwa wyświetlana] 르누아르 경비원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202111].displayName
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [RPG [N202118] — nazwa wyświetlana] 르누아르 경비원
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202118].displayName
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [RPG [N202112] — nazwa wyświetlana] 줄 선 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202112].displayName
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [RPG [N202113] — nazwa wyświetlana] 줄 선 초록 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202113].displayName
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [RPG [N202114] — nazwa wyświetlana] 일하는 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202114].displayName
   limit: do 40 znaków
   EN: Laboring Needlekin
   PL: Pracująca Igiełka
122. [RPG [N202115] — nazwa wyświetlana] 일하는 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202115].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [RPG [N202116] — nazwa wyświetlana] 일하는 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202116].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [RPG [N202102S] — nazwa wyświetlana] 퍼티
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202102S].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [RPG [N202117] — nazwa wyświetlana] 네이키드
   źródło: RPGSystem/rpg-loc-npc-floor-b2-b.json :: dataList[key=N202117].displayName
   limit: do 40 znaków
   EN: Naked
   PL: Naked

## Tryb RPG [floor-b2] — rpg-loc-npc-floor-b2
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-npc-floor-b2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

126. [RPG [N202001] — nazwa wyświetlana] 크로머 언니
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202001].displayName
   limit: do 40 znaków
   EN: Kromer's Sister
   PL: Siostra Kromer
127. [RPG [N202002] — nazwa wyświetlana] 지하 2층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202002].displayName
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [RPG [N202003] — nazwa wyświetlana] 빨간 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202003].displayName
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [RPG [N202004] — nazwa wyświetlana] 대기 중인 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202004].displayName
   limit: do 40 znaków
   EN: Queued Needlekin
   PL: Igiełka w Kolejce
130. [RPG [N202005] — nazwa wyświetlana] 대기 중인 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202005].displayName
   limit: do 40 znaków
   EN: Queued Noir
   PL: Le Noir w Kolejce
131. [RPG [N202028] — nazwa wyświetlana] 대기 중인 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202028].displayName
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [RPG [N202029] — nazwa wyświetlana] 대기 중인 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202029].displayName
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [RPG [N202030] — nazwa wyświetlana] 대기 중인 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202030].displayName
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [RPG [N202006] — nazwa wyświetlana] 네이키드
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202006].displayName
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [RPG [N202015] — nazwa wyświetlana] 팔레트
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202015].displayName
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [RPG [N202021] — nazwa wyświetlana] 바느질의 왕
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202021].displayName
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [RPG [N202022] — nazwa wyświetlana] 퍼티
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202022].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [RPG [N202025] — nazwa wyświetlana] 일하는 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202025].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [RPG [N202026] — nazwa wyświetlana] 일하는 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202026].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [RPG [N202027] — nazwa wyświetlana] 일하는 바늘이
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202027].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [RPG [N202035] — nazwa wyświetlana] 빛을 잃은 황금고치
   źródło: RPGSystem/rpg-loc-npc-floor-b2.json :: dataList[key=N202035].displayName
   limit: do 40 znaków
   EN: Tarnished Golden Cocoon
   PL: Zmatowiały Złoty Kokon

## Tryb RPG [floor-b2] — rpg-loc-quest-floor-b2-b
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-quest-floor-b2-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

142. [RPG [Q-2001] — tytuł] 지하 2층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2001].title
   limit: do 40 znaków
   EN: Explore B2F
   PL: Rozejrzyj się na poziomie -2
143. [RPG [Q-2001] — opis] 지하 2층으로 도착했다. 황금염료를 기다리는 빽빽한 줄이 보인다. 지난번 우리와 거래를 하였던 네이키드라는 자에게 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2001].description
   limit: do 190 znaków
   EN: We've arrived on B2F. A tightly packed line of customers is waiting for Golden Dye. Let's speak with Naked, the one we traded with before last time.
   PL: Dotarliśmy na poziom -2. Widać ciasną kolejkę czekającą na Złoty Barwnik. Zagadajmy Nakeda, który handlował z nami ostatnio.
144. [RPG [Q-2001] — krok 1 — cel zadania 1] 네이키드에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to Naked
   PL: Zagadaj Nakeda
145. [RPG [Q-2002] — tytuł] 네이키드에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2002].title
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [RPG [Q-2002] — opis] 지하 2층으로 도착했다. 황금염료를 기다리는 빽빽한 줄이 보인다. 지난번 우리와 거래를 하였던 네이키드라는 자에게 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2002].description
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [RPG [Q-2002] — krok 1 — cel zadania 1] 네이키드에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2002].steps[#0].goalDescription1
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [RPG [Q-2002] — krok 2 — cel zadania 1] 덤벼드는 르누아르 무리 격퇴
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2002].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Fight off the Le Noir assault
   PL: Odepchnij nacierających Le Noir
149. [RPG [Q-2002] — krok 3 — cel zadania 1] 전투 뒤 상황 정리
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2002].steps[#2].goalDescription1
   limit: do 120 znaków
   EN: Get your bearings after the battle
   PL: Ogarnij sytuację po walce
150. [RPG [Q-2003] — tytuł] 염색실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2003].title
   limit: do 40 znaków
   EN: Head to the Dyehouse
   PL: Udaj się do Farbiarni
151. [RPG [Q-2003] — opis] 르누아르들이 덤벼오기 시작했다. 일단은 지하로 더 내려갈 방법을 찾아야 한다. 염색실의 팔레트에게 내려가는 길을 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2003].description
   limit: do 190 znaków
   EN: The Noirs have started coming after us. For now, we need to find a way farther underground. Let's ask Palette in the Dyehouse how to get down.
   PL: Le Noir ruszyły na nas. Na razie trzeba znaleźć drogę jeszcze głębiej w podziemia. Zapytajmy Paletę w Farbiarni, jak zejść na dół.
152. [RPG [Q-2003] — krok 1 — cel zadania 1] 염색실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2003].steps[#0].goalDescription1
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [RPG [Q-2004] — tytuł] 염색실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2004].title
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [RPG [Q-2004] — opis] 르누아르들이 덤벼오기 시작했다. 일단은 지하로 더 내려갈 방법을 찾아야 한다. 염색실의 팔레트에게 내려가는 길을 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2004].description
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [RPG [Q-2004] — krok 1 — cel zadania 1] 염색실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2004].steps[#0].goalDescription1
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [RPG [Q-2004A] — tytuł] 타래둥지로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2004A].title
   limit: do 40 znaków
   EN: Head to the Skein Nest
   PL: Udaj się do Gniazda Przędzy
157. [RPG [Q-2004A] — opis] 팔레트는 지하 2층 플로어 매니저가 가지고 있는 알록달록한 실타래를 원하는 것 같다. 팔레트의 부탁을 들어주기 위해 타래둥지로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2004A].description
   limit: do 180 znaków
   EN: Palette appears to need the Colorful Skein held by the B2F's Floor Manager. Let's head to the Skein Nest to carry out Palette's request.
   PL: Paleta chyba chce Kolorową Przędzę trzymaną przez Kierownika Piętra -2. Aby spełnić prośbę Palety, udamy się do Gniazda Przędzy.
158. [RPG [Q-2004A] — krok 1 — cel zadania 1] 타래둥지로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2004A].steps[#0].goalDescription1
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [RPG [Q-2005] — tytuł] 르누아르들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2005].title
   limit: do 40 znaków
   EN: Kill the Noirs
   PL: Zabij Le Noir
160. [RPG [Q-2005] — krok 1 — cel zadania 1] 르누아르들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2005].steps[#0].goalDescription1
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [RPG [Q-2006] — tytuł] 르누아르들을 처치하기 2
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2006].title
   limit: do 40 znaków
   EN: Kill the Noirs (2)
   PL: Zabij Le Noir (2)
162. [RPG [Q-2006] — opis] 계속해서 르누아르들이 길을 막고 있다. 이들을 처치하면서 계속 나아가자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2006].description
   limit: do 120 znaków
   EN: More Noirs stand in the way. We should clear them out and press onward.
   PL: Kolejni Le Noir zagradzają drogę. Rozprawiajmy się z nimi i idźmy dalej.
163. [RPG [Q-2006] — krok 1 — cel zadania 1] 르누아르들을 계속 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2006].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Keep clearing out the Noirs
   PL: Zabijaj Le Noir dalej
164. [RPG [Q-2007] — tytuł] 타래둥지로 계속 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2007].title
   limit: do 50 znaków
   EN: Press onward to the Skein Nest
   PL: Idź dalej do Gniazda Przędzy
165. [RPG [Q-2007] — opis] 길을 막고 있던 르누아르들을 모두 처치했다. 이제 타래둥지로 도달하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2007].description
   limit: do 120 znaków
   EN: The Noirs blocking the way have been dealt with. Let's make for the Skein Nest.
   PL: Le Noir zagradzające drogę są rozprawione. Teraz dotrzyjmy do Gniazda Przędzy.
166. [RPG [Q-2007] — krok 1 — cel zadania 1] 타래둥지로 계속 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2007].steps[#0].goalDescription1
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [RPG [Q-2008] — tytuł] 지하 2층 플로어 매니저에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2008].title
   limit: do 40 znaków
   EN: Talk to B2F's Floor Manager
   PL: Zagadaj Kierownika Piętra -2
168. [RPG [Q-2008] — opis] 타래둥지에 도착했다. 지하 2층 플로어 매니저에게 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2008].description
   limit: do 120 znaków
   EN: We've arrived at the Skein Nest. Let's speak with B2F's Floor Manager.
   PL: Dotarliśmy do Gniazda Przędzy. Zagadajmy Kierownika Piętra -2.
169. [RPG [Q-2008] — krok 1 — cel zadania 1] 지하 2층 플로어 매니저에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2008].steps[#0].goalDescription1
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [RPG [Q-2008] — krok 2 — cel zadania 1] 지하 2층 플로어 매니저 처치
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2008].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Kill the B2F Floor Manager
   PL: Zabij Kierownika Piętra -2
171. [RPG [Q-2008] — krok 3 — cel zadania 1] 알록달록한 실타래 획득
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2008].steps[#2].goalDescription1
   limit: do 120 znaków
   EN: Obtained Colorful Skein
   PL: Zdobądź Kolorową Przędzę
172. [RPG [Q-2009] — tytuł] 팔레트에게 실타래를 전달하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2009].title
   limit: do 40 znaków
   EN: Bring the Skein to Palette
   PL: Przekaż Przędzę Palecie
173. [RPG [Q-2009] — opis] 지하 2층 플로어 매니저로부터 알록달록한 실타래를 얻었다. 이제 염색실로 돌아가서 팔레트에게 알록달록한 실타래를 건네주자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2009].description
   limit: do 180 znaków
   EN: Palette appears to need the Colorful Skein held by the B2F's Floor Manager. Let's head to the Skein Nest to carry out Palette's request.
   PL: Zdobyliśmy od Kierownika Piętra -2 Kolorową Przędzę. Teraz wróćmy do Farbiarni i przekażmy ją Palecie.
174. [RPG [Q-2009] — krok 1 — cel zadania 1] 팔레트에게 실타래를 전달하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2009].steps[#0].goalDescription1
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [RPG [Q-2010] — tytuł] 지하 3층 에스컬레이터로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010].title
   limit: do 40 znaków
   EN: Head to B3F's Escalator
   PL: Udaj się do schodów na poziom -3
176. [RPG [Q-2010] — opis] 팔레트가 약속을 지켰다. 우리에게 지하 3층으로 내려가는 에스컬레이터의 위치를 알려주었다. 지하 3층으로 향하는 에스컬레이터로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010].description
   limit: do 150 znaków
   EN: Palette kept her word and told us where to find the escalator to B3F. Let's head there and continue downward.
   PL: Paleta dotrzymała słowa i zdradziła położenie schodów ruchomych na poziom -3. Udamy się do nich i zejdziemy niżej.
177. [RPG [Q-2010] — krok 1 — cel zadania 1] 지하 3층 에스컬레이터로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010].steps[#0].goalDescription1
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [RPG [Q-2010A] — tytuł] 지하 3층으로 내려가기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010A].title
   limit: do 40 znaków
   EN: Head down to B3F
   PL: Zejdź na poziom -3
179. [RPG [Q-2010A] — opis] 지하 3층으로 향하는 에스컬레이터에 도착했다. 지하 3층으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010A].description
   limit: do 120 znaków
   EN: We've reached the escalator. Let's take it down to B3F.
   PL: Dotarliśmy do schodów ruchomych na poziom -3. Zejdźmy nim na dół.
180. [RPG [Q-2010A] — krok 1 — cel zadania 1] 지하 3층으로 내려가기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010A].steps[#0].goalDescription1
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [RPG [Q-2010A] — krok 2 — cel zadania 1] 지하 3층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2-b.json :: dataList[key=Q-2010A].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Explore 3F
   PL: Rozejrzyj się na poziomie -3

## Tryb RPG [floor-b2] — rpg-loc-quest-floor-b2
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-quest-floor-b2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

182. [RPG [Q-2000] — tytuł] 지하 2층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2000].title
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [RPG [Q-2000] — opis] 지하 2층으로 도착했다. 앞으로 계속 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2000].description
   limit: do 120 znaków
   EN: We've reached B2F. Let's keep moving.
   PL: Dotarliśmy na poziom -2. Idźmy dalej.
184. [RPG [Q-2000] — krok 1 — cel zadania 1] 지하 2층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2000].steps[#0].goalDescription1
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [RPG [Q-2001] — tytuł] 타래둥지로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2001].title
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [RPG [Q-2001] — opis] 지하 2층으로 내려왔다. 크로머의 언니로부터 타래둥지라는 곳에 대한 이야기를 들었다. 왼쪽으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2001].description
   limit: do 150 znaków
   EN: We've made it down to B2F. Kromer's older sister mentioned a place called the Skein Nest. Let's head to the left.
   PL: Zeszliśmy na poziom -2. Siostra Kromer opowiedziała nam o miejscu zwanym Gniazdem Przędzy. Udamy się na lewo.
187. [RPG [Q-2001] — krok 1 — cel zadania 1] 왼쪽에 있는 타래둥지로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the Skein Nest to the Left
   PL: Udaj się do Gniazda Przędzy po lewej
188. [RPG [Q-2002] — tytuł] 화장실 밖으로 나가보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2002].title
   limit: do 40 znaków
   EN: Leave the Restroom
   PL: Wyjdź z toalety
189. [RPG [Q-2002] — opis] 타래둥지로 향했지만 정체불명의 거대한 괴물이 쫓아와 우리를 죽였다. 우리가 갖고 다니는 황금고치 때문인 것 같았다. 일단 화장실을 나와 방법을 찾아보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2002].description
   limit: do 270 znaków
   EN: We tried to reach the Skein Nest, but a massive monster chased us down and killed us. It seemed to be after the Golden Cocoon we're carrying. For now, let's leave the Restroom and figure out another way through.
   PL: Chcieliśmy dotrzeć do Gniazda Przędzy, ale ogromny, nieznany potwór dopadł nas i zabił. Chyba polował na niesiony przez nas Złoty Kokon. Na razie wyjdźmy z toalety i poszukajmy innego sposobu.
190. [RPG [Q-2002] — krok 1 — cel zadania 1] 화장실 밖으로 나가보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2002].steps[#0].goalDescription1
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [RPG [Q-2003] — tytuł] 타래둥지로 향하기 2
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2003].title
   limit: do 40 znaków
   EN: Head to the Skein Nest (2)
   PL: Udaj się do Gniazda Przędzy (2)
192. [RPG [Q-2003] — opis] 다행히도 괴물은 잠깐 자리를 비운 것 같다. 이 틈을 타서 다시 한 번 타래둥지로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2003].description
   limit: do 160 znaków
   EN: Looks like the monster has stepped away for the moment. Let's use this chance to make another run for the Skein Nest.
   PL: Na szczęście potwór chyba na chwilę gdzieś odszedł. Skorzystajmy z okazji i spróbujmy ponownie dotrzeć do Gniazda Przędzy.
193. [RPG [Q-2003] — krok 1 — cel zadania 1] 타래둥지로 다시 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2003].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head Back to the Skein Nest
   PL: Udaj się ponownie do Gniazda Przędzy
194. [RPG [Q-2004] — tytuł] 지하 2층의 플로어 매니저와 대화하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2004].title
   limit: do 40 znaków
   EN: Talk to B2F's Floor Manager
   PL: Rozmawiaj z Kierownikiem Piętra -2
195. [RPG [Q-2004] — opis] 타래둥지로 무사히 향했다. 지하 2층의 플로어 매니저가 보인다. 그자에게 황금고치로부터 황금 실타래를 만들 수 있는지를 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2004].description
   limit: do 180 znaków
   EN: We made it safely to the Skein Nest. B2F's Floor Manager is here. Let's ask whether the Golden Cocoon can be spun into Golden Thread.
   PL: Bez przeszkód dotarliśmy do Gniazda Przędzy. Kierownik Piętra -2 jest na miejscu. Zapytajmy, czy potrafi uprząść Złotą Przędzę ze Złotego Kokonu.
196. [RPG [Q-2004] — krok 1 — cel zadania 1] 지하 2층의 플로어 매니저에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2004].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to the B2F's Floor Manager
   PL: Zagadaj Kierownika Piętra -2
197. [RPG [Q-2005] — tytuł] 염색실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2005].title
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [RPG [Q-2005] — opis] 플로어 매니저는 황금 실타래를 만들기 위해서는 황금염료가 필요하다고 했다. 염색실의 팔레트라는 자에게 황금염료를 받아올 수 있는 것 같다. 염색실로 가보자. 염색실은 복도로 나간 후 위쪽으로 향하면 될 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2005].description
   limit: do 270 znaków
   EN: The Floor Manager says Golden Dye is needed to make Golden Thread. Someone named Palette in the Dyehouse should be able to help. We should leave through the corridor, then head upward to find the Dyehouse.
   PL: Kierownik Piętra powiedział, że do uprzędzenia Złotej Przędzy potrzeba Złotego Barwnika. Podobno można go dostać od Palety z Farbiarni. Udamy się do Farbiarni. Po wyjściu na korytarz trzeba iść w górę.
199. [RPG [Q-2005] — krok 1 — cel zadania 1] 염색실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2005].steps[#0].goalDescription1
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [RPG [Q-2006] — opis] 일하는 고객들의 대화를 엿들어 소문을 수집하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2006].description
   limit: do 120 znaków
   EN: Let's eavesdrop on the customers at work and gather information.
   PL: Podsłuchajmy rozmowy pracujących klientów i zbierzmy plotki.
201. [RPG [Q-2006] — krok 1 — cel zadania 1] 일하는 고객의 대화 엿듣기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2006].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Ask a Working Customer
   PL: Podsłuchaj pracującego klienta
202. [RPG [Q-2006] — krok 2 — cel zadania 1] 일하는 고객에게 물어보기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2006].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Ask a Working Customer
   PL: Wypytaj pracującego klienta
203. [RPG [Q-2007] — tytuł] 네이키드를 찾아 협상하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2007].title
   limit: do 40 znaków
   EN: Find Naked and Negotiate
   PL: Znajdź Nakeda i negocjuj
204. [RPG [Q-2007] — opis] 황금염료를 구하기 위해서는 말도 안 되는 순서를 기다려야 한다. 르누아르의 네이키드라는 자가 가장 빠른 순번을 가졌다고 한다. 네이키드를 찾아 황금염료를 매입할 수 있는지 협상을 해보도록 하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2007].description
   limit: do 230 znaków
   EN: The wait for Golden Dye is absurdly long. Apparently, a Noir named Naked has the earliest place in line. Let's find Naked and see if we can negotiate for his place in the queue.
   PL: Kolejka po Złoty Barwnik jest absurdalnie długa. Podobno najwcześniejsze miejsce zajmuje Le Noir o imieniu Naked. Znajdźmy Nakeda i spróbujmy wynegocjować jego miejsce.
205. [RPG [Q-2007] — krok 1 — cel zadania 1] 네이키드를 찾아 협상하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2007].steps[#0].goalDescription1
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [RPG [Q-2008] — krok 1 — cel zadania 1] 대기 중인 르누아르에게 묻기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2008].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Ask the Queued Noir
   PL: Wypytaj Le Noir z kolejki
207. [RPG [Q-2009] — tytuł] 팔레트에게 랭콜로르 염료를 얻을 수 있냐고 부탁하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2009].title
   limit: do 50 znaków
   EN: Ask Palette for L'Incolore Dye
   PL: Zapytaj Paletę o Barwnik L'Incolore
208. [RPG [Q-2009] — opis] 네이키드는 순순히 황금염료를 넘기지 않으려는 모양이다. 대신에 랭콜로르라는 염료를 가지고 온다면 황금염료와 바꿔준다고 한다. 팔레트에게 돌아가 랭콜로르를 얻을 수 있는지 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2009].description
   limit: do 220 znaków
   EN: Naked has no intention of giving up the Golden Dye for free. He'll trade it for a dye called L'Incolore instead. Let's return to Palette and ask if she can make some.
   PL: Naked nie zamierza oddać Złotego Barwnika za darmo. W zamian zażądał barwnika o nazwie L'Incolore. Wróćmy do Palety i zapytajmy, czy może go zrobić.
209. [RPG [Q-2009] — krok 1 — cel zadania 1] 팔레트에게 랭콜로르 염료를 얻을 수 있냐고 부탁하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2009].steps[#0].goalDescription1
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [RPG [Q-2010] — tytuł] 염색창고에서 눈물 터뜨리기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2010].title
   limit: do 50 znaków
   EN: Burst the Tears at the Dye Storage
   PL: Rozbij Łzy w Magazynie Barwników
211. [RPG [Q-2010] — opis] 다행히도 팔레트는 랭콜로르를 바로 만들어줄 수 있다고 한다. 대신에 눈물을 색깔별로 터뜨려 달라고 한다. 눈물들은 오른쪽에 있는 염색창고에서부터 얻을 수 있는 것 같다. 노란 염료, 빨간 염료, 파란 염료를 각각 2개씩 모아서 팔레트에게 가져가자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2010].description
   limit: do 330 znaków
   EN: Luckily, Palette says she can make L'Incolore right away. In exchange, she wants us to burst Tears of different colors. They can apparently be found in the Dye Storage to the right. Collect 2 Yellow, 2 Red, and 2 Blue Dye, then bring them back to Palette.
   PL: Na szczęście Paleta może zrobić L'Incolore od razu. W zamian prosi o rozbicie Łz o różnych barwach. Podobno można je zdobyć w Magazynie Barwników po prawej. Zbierzmy po 2 Żółte, 2 Czerwone i 2 Niebieskie Łzy i przynieśmy je Palecie.
212. [RPG [Q-2010] — krok 1 — cel zadania 1] 노란색 염료 모으기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2010].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Collect the Yellow Dye
   PL: Zbierz żółty Barwnik
213. [RPG [Q-2010] — krok 1 — cel zadania 2] 빨간색 염료 모으기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2010].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Collect the Red Dye
   PL: Zbierz czerwony Barwnik
214. [RPG [Q-2010] — krok 1 — cel zadania 3] 파란색 염료 모으기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2010].steps[#0].goalDescription3
   limit: do 120 znaków
   EN: Collect the Blue Dye
   PL: Zbierz niebieski Barwnik
215. [RPG [Q-2010] — krok 2 — cel zadania 1] 팔레트에게 염료들을 전달하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2010].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Bring the Dyes to Palette
   PL: Przekaż Barwniki Palecie
216. [RPG [Q-2011] — tytuł] 네이키드에게 가서 황금염료를 받아오기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2011].title
   limit: do 50 znaków
   EN: Trade with Naked for Golden Dye
   PL: Odwiedź Nakeda po Złoty Barwnik
217. [RPG [Q-2011] — opis] 팔레트로부터 랭콜로르 염료를 얻었다. 내 눈에는 어떤 색도 보이지 않지만… 일단 네이키드에게 가져가서 황금염료와 교환할 수 있을지를 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2011].description
   limit: do 180 znaków
   EN: Palette gave us L'Incolore. I can't see any color in it at all, but... let's bring it to Naked and see if he'll trade us the Golden Dye.
   PL: Dostaliśmy od Palety barwnik L'Incolore. Nie widzę w nim żadnego koloru, ale… zanieśmy go Nakedowi i zapytajmy, czy wymieni go na Złoty Barwnik.
218. [RPG [Q-2011] — krok 1 — cel zadania 1] 네이키드에게 가서 황금염료와 랭콜로르를 교환하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2011].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Trade L'Incolore for Golden Dye with Naked
   PL: Wymień L'Incolore na Złoty Barwnik u Nakeda
219. [RPG [Q-2012] — opis] 팔레트에게서 황금염료를 받아 오자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2012].description
   limit: do 120 znaków
   EN: We should collect the Golden Dye from Palette.
   PL: Odbierzmy Złoty Barwnik od Palety.
220. [RPG [Q-2012] — krok 1 — cel zadania 1] 팔레트에게서 황금염료 받기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2012].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Collect the Golden Dye from Palette
   PL: Odbierz Złoty Barwnik od Palety
221. [RPG [Q-2013] — tytuł] 지하 2층 플로어 매니저에게 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2013].title
   limit: do 50 znaków
   EN: Return to the B2F Floor Manager
   PL: Udaj się do Kierownika Piętra -2
222. [RPG [Q-2013] — opis] 오티스의 활약으로 네이키드는 황금염료를 우리에게 내주었다. 이제 이걸 가지고 지하 2층의 플로어 매니저에게 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2013].description
   limit: do 180 znaków
   EN: Thanks to Outis's eloquent requisition effort, Naked finally agreed to hand over the Golden Dye. Let's take it to the B2F Floor Manager.
   PL: Dzięki staraniom Outis Naked w końcu oddał nam Złoty Barwnik. Zanieśmy go Kierownikowi Piętra -2.
223. [RPG [Q-2013] — krok 1 — cel zadania 1] 지하 2층 플로어 매니저에게 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2013].steps[#0].goalDescription1
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [RPG [Q-2014] — tytuł] 복도의 침입자를 막아내기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2014].title
   limit: do 40 znaków
   EN: Hold off the Intruders
   PL: Odepchnij intruzów z korytarza
225. [RPG [Q-2014] — opis] 황금고치로부터 실을 짜내고 있는 중, 복도에서부터 무언가 오는 소리가 들렸다. 황금 실타래를 탐내는 자일 것 같다. 황금 실타래가 무사히 짜여질 때까지 복도 입구에서 몰려오는 것들을 막아내야 한다.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2014].description
   limit: do 300 znaków
   EN: While we were waiting for the Golden Cocoon to be spun into thread, we heard the sound of someone approaching from the corridor. They are probably after the Golden Skein. Hold the corridor entrance until the spinning is complete.
   PL: W trakcie uprzędania Złotego Kokonu w Przędzę z korytarza dobiegło kroki. Chyba ktoś pożąda Złotej Przędzy. Blokujmy wejście na korytarz, aż uprzędzenie dobiegnie końca.
226. [RPG [Q-2014] — krok 1 — cel zadania 1] 복도의 침입자를 막아내기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2014].steps[#0].goalDescription1
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [RPG [Q-2015] — tytuł] 완성된 황금 실타래 받기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2015].title
   limit: do 50 znaków
   EN: Collect the Completed Golden Skein
   PL: Odbierz gotową Złotą Przędzę
228. [RPG [Q-2015] — opis] 정체불명의 괴물을 물리쳤다. 다시 지하 2층의 플로어 매니저에게 돌아가 황금 실타래를 받아가자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2015].description
   limit: do 140 znaków
   EN: The unknown creature is down. Let's return to the B2F Floor Manager and collect the finished Golden Skein.
   PL: Nieznany potwór pada. Wróćmy do Kierownika Piętra -2 i odbierzmy skończoną Złotą Przędzę.
229. [RPG [Q-2015] — krok 1 — cel zadania 1] 지하 2층의 플로어 매니저에게 돌아가 완성된 황금 실타래 받기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2015].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Collect the Finished Golden Skein from the B2F Floor Manager
   PL: Wróć do Kierownika Piętra -2 po gotową Złotą Przędzę
230. [RPG [Q-2016A] — tytuł] 지하 2층을 떠나기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2016A].title
   limit: do 40 znaków
   EN: Leave B2F
   PL: Opuść poziom -2
231. [RPG [Q-2016A] — opis] 무사히 짜여진 황금 실타래를 받을 수 있었다. 지하 2층에서의 할 일은 끝난 것 같다. 지하 2층을 벗어나자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2016A].description
   limit: do 120 znaków
   EN: We have the finished Golden Skein. Looks like we're done here. Time to leave B2F.
   PL: Mamy gotową Złotą Przędzę. Wygląda na to, że na poziomie -2 skończyliśmy. Opuśćmy go.
232. [RPG [Q-2016A] — krok 1 — cel zadania 1] 지하 2층을 떠나기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2016A].steps[#0].goalDescription1
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [RPG [Q-2017] — tytuł] 3층으로 올라가기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2017].title
   limit: do 40 znaków
   EN: Head to 3F
   PL: Wspinaj się na 3. piętro
234. [RPG [Q-2017] — opis] 이제 3층으로 올라가서 황금 실타래를 이용해 황금원단을 지을 수 있는지 알아보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2017].description
   limit: do 120 znaków
   EN: Time to head up to 3F and see if the Golden Skein can be woven into Golden Fabric.
   PL: Czas wjechać na 3. piętro i przekonać się, czy ze Złotej Przędzy można utkać Złotą Tkaninę.
235. [RPG [Q-2017] — krok 1 — cel zadania 1] 3층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-b2.json :: dataList[key=Q-2017].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Take the Escalator to 3F
   PL: Wjedź schodami ruchomymi na 3. piętro

## Tryb RPG [floor-b2] — rpg-loc-swarm-mob-floor-b2-a
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

236. [RPG [swarm_green_needle] — nazwa wyświetlana] 초록 바늘이
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json :: dataList[key=swarm_green_needle].displayName
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [RPG [swarm_pus_blue] — nazwa wyświetlana] 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json :: dataList[key=swarm_pus_blue].displayName
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [RPG [swarm_pus_red] — nazwa wyświetlana] 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json :: dataList[key=swarm_pus_red].displayName
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [RPG [swarm_pus_yellow] — nazwa wyświetlana] 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json :: dataList[key=swarm_pus_yellow].displayName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [RPG [swarm_red_needle] — nazwa wyświetlana] 빨간 바늘이
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json :: dataList[key=swarm_red_needle].displayName
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b2] — rpg-loc-swarm-mob-floor-b2-b
- obszar/warstwa: `floor-b2` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

241. [RPG [swarm_green_needle] — nazwa wyświetlana] 초록 바늘이
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_green_needle].displayName
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [RPG [swarm_lanoir_fanatic] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_lanoir_fanatic].displayName
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [RPG [swarm_lanoir_guard] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_lanoir_guard].displayName
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [RPG [swarm_pus_blue] — nazwa wyświetlana] 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_pus_blue].displayName
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [RPG [swarm_pus_red] — nazwa wyświetlana] 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_pus_red].displayName
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [RPG [swarm_pus_yellow] — nazwa wyświetlana] 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_pus_yellow].displayName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [RPG [swarm_red_needle] — nazwa wyświetlana] 빨간 바늘이
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json :: dataList[key=swarm_red_needle].displayName
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b3] — rpg-loc-location-floor-b3
- obszar/warstwa: `floor-b3` · plik gry: `RPGSystem/rpg-loc-location-floor-b3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

248. [RPG [230200] — tekst] 건조장
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230200].text
   limit: do 120 znaków
   EN: Drying Room
   PL: Suszarnia
249. [RPG [230400] — tekst] 가죽실
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230400].text
   limit: do 120 znaków
   EN: Leather Room
   PL: Skórzarnia
250. [RPG [230500] — tekst] 건조장 복도
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230500].text
   limit: do 120 znaków
   EN: Drying Room Corridor
   PL: Korytarz Suszarni
251. [RPG [230600] — tekst] 건조장
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230600].text
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [RPG [230700] — tekst] 태닝실 복도
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230700].text
   limit: do 120 znaków
   EN: Tannery Corridor
   PL: Korytarz Garbarni
253. [RPG [230800] — tekst] 태닝실
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230800].text
   limit: do 120 znaków
   EN: Tannery
   PL: Garbarnia
254. [RPG [230900] — tekst] 절삭실 복도
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=230900].text
   limit: do 120 znaków
   EN: Cutting Room Corridor
   PL: Korytarz Pracowni Krojenia
255. [RPG [231000] — tekst] 절삭실
   źródło: RPGSystem/rpg-loc-location-floor-b3.json :: dataList[key=231000].text
   limit: do 120 znaków
   EN: Cutting Room
   PL: Pracownia Krojenia

## Tryb RPG [floor-b3] — rpg-loc-npc-floor-b3-b-enemy
- obszar/warstwa: `floor-b3` · plik gry: `RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

256. [RPG [N203006] — nazwa wyświetlana] 길들여진 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203006].displayName
   limit: do 40 znaków
   EN: Tamed Leather
   PL: Oswojona Skóra
257. [RPG [N203008] — nazwa wyświetlana] 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203008].displayName
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [RPG [N203010] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203010].displayName
   limit: do 40 znaków
   EN: Leather Glove
   PL: Skórzana Rękawica
259. [RPG [N203014] — nazwa wyświetlana] 검은 실
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203014].displayName
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [RPG [N203101] — nazwa wyświetlana] 유기된 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203101].displayName
   limit: do 40 znaków
   EN: Abandoned Leather
   PL: Porzucona Skóra
261. [RPG [N203102] — nazwa wyświetlana] 사나워진 유기된 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203102].displayName
   limit: do 40 znaków
   EN: Ferocious Abandoned Leather
   PL: Rozwścieczona Porzucona Skóra
262. [RPG [N203103] — nazwa wyświetlana] 황금가죽 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203103].displayName
   limit: do 40 znaków
   EN: Golden Hide Glove
   PL: Rękawica ze Złotej Skóry
263. [RPG [N203104] — nazwa wyświetlana] 가죽아비
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203104].displayName
   limit: do 40 znaków
   EN: Leatherfather
   PL: Skórzany Ojciec
264. [RPG [N203105] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203105].displayName
   limit: do 50 znaków
   EN: Le Rouge Sales Associate [Sunshone]
   PL: Pracownik Le Rouge [Napromieniony]
265. [RPG [N203106] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203106].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [RPG [N203107] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203107].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [RPG [N203108] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203108].displayName
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [RPG [N203109] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203109].displayName
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [RPG [N203110] — nazwa wyświetlana] 바늘꽂이 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203110].displayName
   limit: do 40 znaków
   EN: Pincushion Glove
   PL: Rękawica z Poduszką na Szpilki
270. [RPG [N203111] — nazwa wyświetlana] 짓물러버린 노란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203111].displayName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [RPG [N203112] — nazwa wyświetlana] 곪아버린 붉은 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203112].displayName
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [RPG [N203113] — nazwa wyświetlana] 넘쳐버린 파란 눈물
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203113].displayName
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [RPG [N203114] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203114].displayName
   limit: do 40 znaków
   EN: Mobile-Go-Spin
   PL: Wirująca Karuzela
274. [RPG [N203115] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203115].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [RPG [N203116] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203116].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [RPG [N203117] — nazwa wyświetlana] 뭉쳐 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203117].displayName
   limit: do 40 znaków
   EN: Clumped Crawling Leather
   PL: Zbrylona Pełzająca Skóra
277. [RPG [N203118] — nazwa wyświetlana] 바늘꽂이
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203118].displayName
   limit: do 40 znaków
   EN: Pincushion
   PL: Poduszka na Szpilki
278. [RPG [N203119] — nazwa wyświetlana] 무두질된 죄수
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203119].displayName
   limit: do 40 znaków
   EN: Tanned Prisoner
   PL: Wygarbowany Więzień
279. [RPG [N203120] — nazwa wyświetlana] 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203120].displayName
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [RPG [N203121] — nazwa wyświetlana] 길들여진 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json :: dataList[key=N203121].displayName
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b3] — rpg-loc-npc-floor-b3-b
- obszar/warstwa: `floor-b3` · plik gry: `RPGSystem/rpg-loc-npc-floor-b3-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

281. [RPG [N203001] — nazwa wyświetlana] 가죽 전시장
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203001].displayName
   limit: do 40 znaków
   EN: Leather Exhibition Hall
   PL: Galeria Skór
282. [RPG [N203003] — nazwa wyświetlana] 가죽 후처리장
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203003].displayName
   limit: do 40 znaków
   EN: Leather Treatment Facility
   PL: Zakład Obróbki Skór
283. [RPG [N203004] — nazwa wyświetlana] 테너
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203004].displayName
   limit: do 40 znaków
   EN: Tanner
   PL: Garbarz
284. [RPG [N203005] — nazwa wyświetlana] 키우는 자
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203005].displayName
   limit: do 40 znaków
   EN: Nurturer
   PL: Hodowca
285. [RPG [N203007] — nazwa wyświetlana] 통제자
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203007].displayName
   limit: do 40 znaków
   EN: Overseer
   PL: Nadzorca
286. [RPG [N203017] — nazwa wyświetlana] 통제자
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203017].displayName
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [RPG [N203013] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203013].displayName
   limit: do 40 znaków
   EN: Buffet
   PL: Bufet
288. [RPG [N203015] — nazwa wyświetlana] 절삭 기계
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203015].displayName
   limit: do 40 znaków
   EN: Cutting Machine
   PL: Maszyna Krojąca
289. [RPG [N201030] — nazwa wyświetlana] 고치
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N201030].displayName
   limit: do 40 znaków
   EN: Cocoon
   PL: Kokon
290. [RPG [N203018] — nazwa wyświetlana] 긁어내는 자
   źródło: RPGSystem/rpg-loc-npc-floor-b3-b.json :: dataList[key=N203018].displayName
   limit: do 40 znaków
   EN: Scraper
   PL: Zdrapywacz

## Tryb RPG [floor-b3] — rpg-loc-quest-floor-b3-b
- obszar/warstwa: `floor-b3` · plik gry: `RPGSystem/rpg-loc-quest-floor-b3-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

291. [RPG [Q-3000] — tytuł] 가죽을 가져오기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].title
   limit: do 40 znaków
   EN: Fetch the Hide
   PL: Przynieś Skóry
292. [RPG [Q-3000] — opis] 통제자가 황금 수의를 지어주는 대가로 가죽 여덟 장을 요구했다.\n백화점 위아래로 흩어진 것들을 모아 오자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].description
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Overseer requested 8 pieces of hide in return for making the Golden Shroud. We need to gather the hides scattered across the Grand Magasin.
   PL: Nadzorca uszyje Złoty Całun w zamian za osiem skór.\nZbierzmy te rozrzucone po całym domu handlowym.
293. [RPG [Q-3000] — krok 1 — cel zadania 1] 지하 2층의 가죽 세 장
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: B2F: 3 Hide Pieces
   PL: Poziom -2: trzy skóry
294. [RPG [Q-3000] — krok 1 — cel zadania 2] 지하 1층의 가죽
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: B1F: Hide Piece
   PL: Poziom -1: jedna skóra
295. [RPG [Q-3000] — krok 1 — cel zadania 3] 1층의 가죽
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].steps[#0].goalDescription3
   limit: do 120 znaków
   EN: 1F: Hide Piece
   PL: 1. piętro: jedna skóra
296. [RPG [Q-3000] — krok 1 — cel zadania 4] 2층의 가죽
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].steps[#0].goalDescription4
   limit: do 120 znaków
   EN: 2F: Hide Piece
   PL: 2. piętro: jedna skóra
297. [RPG [Q-3000] — krok 1 — cel zadania 5] 3층의 가죽
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].steps[#0].goalDescription5
   limit: do 120 znaków
   EN: 3F: Hide Piece
   PL: 3. piętro: jedna skóra
298. [RPG [Q-3000] — krok 1 — cel zadania 6] 4층의 가죽
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3000].steps[#0].goalDescription6
   limit: do 120 znaków
   EN: 4F: Hide Piece
   PL: 4. piętro: jedna skóra
299. [RPG [Q-3010] — tytuł] 황금가죽들을 모아오기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].title
   limit: do 50 znaków
   EN: Collect the Pieces of Golden Hide
   PL: Zbierz kawałki Złotej Skóry
300. [RPG [Q-3010] — opis] 지하 3층에서 통제자를 만났다. 통제자는 황금가죽으로 옷을 만들기 위해선 우리가 지나왔던 길에서부터 황금가죽을 모아와야 한다고 한다. 그자는 황금가죽의 위치를 우리에게 이야기해 주었다. 황금가죽을 모으러 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].description
   limit: do 350 znaków
   EN: We encountered the Overseer on B3F. The Overseer said that in order to make clothing from the Golden Hide, we need to collect the pieces from all the location we've visited so far. The exact locations were given to us. Now we need to go fetch the Golden Hide for the Overseer.
   PL: Spotkaliśmy Nadzorcę na poziomie -3. Powiedział, że żeby uszyć ubranie ze Złotej Skóry, musimy zebrać kawałki ze wszystkich miejsc, które minęliśmy po drodze. Wskazał nam ich położenie. Ruszajmy po Złotą Skórę.
301. [RPG [Q-3010] — krok 1 — cel zadania 1] 팔레트의 황금송진을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Collect Palette's Golden Resin
   PL: Zdobądź Złotą Żywicę od Palety
302. [RPG [Q-3010] — krok 1 — cel zadania 2] 지하 2층 플로어 매니저의 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Collect B2F Floor Manager's Golden Hide
   PL: Zdobądź Złotą Skórę Kierownika Piętra -2
303. [RPG [Q-3010] — krok 1 — cel zadania 3] 바느질의 왕의 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription3
   limit: do 120 znaków
   EN: Collect the King of Needlework's Golden Hide
   PL: Zdobądź Złotą Skórę Króla Szycia
304. [RPG [Q-3010] — krok 1 — cel zadania 4] 수셰프의 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription4
   limit: do 120 znaków
   EN: Collect Sous Chef's Golden Hide
   PL: Zdobądź Złotą Skórę Sous Chef
305. [RPG [Q-3010] — krok 1 — cel zadania 5] 1층 시체더미로부터 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription5
   limit: do 120 znaków
   EN: Collect the Golden Hide from 1F's corpse pile
   PL: Zdobądź Złotą Skórę ze stosu zwłok na 1. piętrze
306. [RPG [Q-3010] — krok 1 — cel zadania 6] 4층 벽에서부터 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription6
   limit: do 120 znaków
   EN: Collect the Golden Hide from the wall on 4F
   PL: Zdobądź Złotą Skórę ze ściany na 4. piętrze
307. [RPG [Q-3010] — krok 1 — cel zadania 7] 르루주 브랜드 디렉터의 시체로부터 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription7
   limit: do 120 znaków
   EN: Collect the Golden Hide from the Rouge Brand Director's corpse
   PL: Zdobądź Złotą Skórę ze zwłok Dyrektora Marki Le Rouge
308. [RPG [Q-3010] — krok 1 — cel zadania 8] 3층 플로어 매니저로부터 황금가죽을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3010].steps[#0].goalDescription8
   limit: do 120 znaków
   EN: Collect the Golden Hide from 3F's Floor Manager
   PL: Zdobądź Złotą Skórę Kierownika 3. Piętra
309. [RPG [Q-3011] — tytuł] 가죽을 가져오기 — 지하 1층
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011].title
   limit: do 40 znaków
   EN: Gather the Hide - B1F
   PL: Przynieś Skóry — poziom -1
310. [RPG [Q-3011] — opis] 통제자가 요구한 가죽 여덟 장 중 지하 1층 몫.\n푸드코트의 수셰프에게서 뜯어내자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011].description
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the eight pieces of hide demanded by the Overseer can be found on B1F. It has to be flayed off the Sous Chef.
   PL: Nadzorca zażądał ośmiu skór; ta pochodzi z poziomu -1.\nOderwij ją od Sous Chef ze Strefy Gastronomicznej.
311. [RPG [Q-3011] — krok 1 — cel zadania 1] 지하 1층 푸드코트로
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: To B1F Food Court
   PL: Do Strefy Gastronomicznej poziomu -1
312. [RPG [Q-3011] — krok 1 — cel zadania 2] 수셰프의 황금가죽 (4/8) 확보
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Sous Chef's Golden Hide (4/8)
   PL: Złota Skóra Sous Chef (4/8) zdobyta
313. [RPG [Q-3012] — tytuł] 가죽을 가져오기 — 1층
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3012].title
   limit: do 40 znaków
   EN: Gather the Hide - 1F
   PL: Przynieś Skóry — 1. piętro
314. [RPG [Q-3012] — opis] 통제자가 요구한 가죽 여덟 장 중 1층 몫.\n시체더미를 뒤져 찾아내자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3012].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the eight pieces of hide demanded by the Overseer can be found on 1F. It should be somewhere in the corpse pile.
   PL: Nadzorca zażądał ośmiu skór; ta pochodzi z 1. piętra.\nPrzeszukajmy stos zwłok.
315. [RPG [Q-3012] — krok 1 — cel zadania 1] 시체더미 사이의 황금가죽을 줍기 (5/8)
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3012].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Find the Golden Hide hidden in the corpse pile (5/8)
   PL: Podnieś Złotą Skórę ukrytą w stosie zwłok (5/8)
316. [RPG [Q-3012] — krok 1 — cel zadania 2] 시체더미 사이의 황금가죽 (5/8) 확보
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3012].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Corpse Pile's Golden Hide (5/8)
   PL: Złota Skóra ze stosu zwłok (5/8) zdobyta
317. [RPG [Q-3013] — tytuł] 가죽을 가져오기 — 2층
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3013].title
   limit: do 40 znaków
   EN: Gather the Hide - 2F
   PL: Przynieś Skóry — 2. piętro
318. [RPG [Q-3013] — opis] 통제자가 요구한 가죽 여덟 장 중 2층 몫.\n브랜드 디렉터에게서 뜯어내자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3013].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the eight pieces of hide demanded by the Overseer can be found on 2F. It has to be flayed off the Brand Director.
   PL: Nadzorca zażądał ośmiu skór; ta pochodzi z 2. piętra.\nOderwij ją od Dyrektora Marki.
319. [RPG [Q-3013] — krok 1 — cel zadania 1] 르루주 브랜드 디렉터의 황금가죽을 줍기 (7/8)
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3013].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Take the Brand Director's Golden Hide (7/8)
   PL: Podnieś Złotą Skórę Dyrektora Marki Le Rouge (7/8)
320. [RPG [Q-3013] — krok 1 — cel zadania 2] 르루주 브랜드 디렉터의 황금가죽 (7/8) 확보
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3013].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Brand Director's Golden Hide (7/8)
   PL: Złota Skóra Dyrektora Marki Le Rouge (7/8) zdobyta
321. [RPG [Q-3014] — tytuł] 가죽을 가져오기 — 3층
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3014].title
   limit: do 40 znaków
   EN: Gather the Hide - 3F
   PL: Przynieś Skóry — 3. piętro
322. [RPG [Q-3014] — opis] 통제자가 요구한 가죽 여덟 장 중 3층 몫.\n3층 플로어 매니저에게서 뜯어내자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3014].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the eight pieces of hide demanded by the Overseer can be found on 3F. It has to be flayed off the Floor Manager.
   PL: Nadzorca zażądał ośmiu skór; ta pochodzi z 3. piętra.\nOderwij ją od Kierownika 3. Piętra.
323. [RPG [Q-3014] — krok 1 — cel zadania 1] 3층 플로어 매니저의 방으로
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3014].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: To the 3F Floor Manager's Room
   PL: Do pokoju Kierownika 3. Piętra
324. [RPG [Q-3014] — krok 1 — cel zadania 2] 3층 플로어 매니저의 황금가죽 (8/8) 확보
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3014].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: 3F Floor Manager's Golden Hide (8/8)
   PL: Złota Skóra Kierownika 3. Piętra (8/8) zdobyta
325. [RPG [Q-3015] — tytuł] 가죽을 가져오기 — 4층
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3015].title
   limit: do 40 znaków
   EN: Gather the Hide - 4F
   PL: Przynieś Skóry — 4. piętro
326. [RPG [Q-3015] — opis] 통제자가 요구한 가죽 여덟 장 중 4층 몫.\n해체파가 남긴 시멘트 더미를 헤집자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3015].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the eight pieces of hide demanded by the Overseer can be found on 4F. We should search through the concrete rubble left behind by the Deconstructionists.
   PL: Nadzorca zażądał ośmiu skór; ta pochodzi z 4. piętra.\nPrzeszukajmy hałdę cementu pozostawioną przez Deconstructorów.
327. [RPG [Q-3015] — krok 1 — cel zadania 1] 벽 틈새의 황금가죽을 줍기 (6/8)
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3015].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Pick up the Golden Hide stuffed inside the crack in the wall (6/8)
   PL: Podnieś Złotą Skórę wciśniętą w szczelinę ściany (6/8)
328. [RPG [Q-3015] — krok 1 — cel zadania 2] 벽 틈새의 황금가죽 (6/8) 확보
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3015].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Obtained Golden Hide from the crack in the wall (6/8)
   PL: Złota Skóra ze szczeliny ściany (6/8) zdobyta
329. [RPG [Q-3006] — tytuł] 통제자에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3006].title
   limit: do 40 znaków
   EN: Return to the Overseer
   PL: Wróć do Nadzorcy
330. [RPG [Q-3006] — opis] 마침내 황금가죽 여덟 장을 전부 모았다. 지하 3층의 통제자에게 돌아가서 모아온 가죽들을 넘기고 뿌이의 황금가죽 옷을 만들자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3006].description
   limit: do 240 znaków
   EN: We've finally procured all eight pieces of the Golden Hide. Let's return to the Overseer on B3F and hand over what we've collected so he can craft Pwie an outfit out of the Golden Hide.
   PL: Wreszcie zebraliśmy wszystkie osiem skór. Wróćmy do Nadzorcy na poziomie -3, przekażmy mu je i pozwólmy uszyć Pwie ubranie ze Złotej Skóry.
331. [RPG [Q-3006] — krok 1 — cel zadania 1] 통제자에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3006].steps[#0].goalDescription1
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [RPG [Q-3003] — tytuł] 태닝실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003].title
   limit: do 40 znaków
   EN: Head to the Tannery
   PL: Udaj się do Garbarni
333. [RPG [Q-3003] — opis] 황금가죽 8장들을 다 모아왔다. 맞춤형 옷을 짓기 위해서는 몇 가지의 공정이 필요하고 제일 먼저 치수를 재야 한다고 한다. 치수를 재기 위해 태닝실에 있는 테너라는 자에게 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003].description
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We've brought all eight pieces of the Golden Hide, but our journey didn't end there. To make bespoke garment, said the Overseer, Pwie should first head to the Tannery and get their size measured.\nLet's head to the Tannery and meet the... Tanner.
   PL: Zgromadziliśmy wszystkie 8 kawałków Złotej Skóry. Ale to nie koniec: żeby uszyć szyte na miarę ubranie, najpierw trzeba wziąć wymiary. Udamy się do Garbarni i spotkamy się z osobą zwaną Garbarzem, by zmierzyć Pwie.
334. [RPG [Q-3003] — krok 1 — cel zadania 1] 태닝실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003].steps[#0].goalDescription1
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [RPG [Q-3003] — krok 2 — cel zadania 1] 패턴 준비가 끝날 때까지 몰려오는 적들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003].steps[#1].goalDescription1
   limit: do 130 znaków
   EN: Hold the position against the onslaught of enemies until the patterning process is completed.
   PL: Odpieraj nawałę wrogów, aż przygotowanie wykrojów się skończy
336. [RPG [Q-3003] — krok 3 — cel zadania 1] 테너에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003].steps[#2].goalDescription1
   limit: do 120 znaków
   EN: Talk to the Tanner
   PL: Zagadaj Garbarza
337. [RPG [Q-3004] — tytuł] 절삭실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3004].title
   limit: do 40 znaków
   EN: Head to the Cutting Room
   PL: Udaj się do Pracowni Krojenia
338. [RPG [Q-3004] — opis] 뿌이의 치수를 재고 패턴 준비가 모두 끝났다. 이제는 절삭과 봉제 작업이 남아있다고 한다. 절삭실로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3004].description
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pwie's size has been measured, and patterns have been patterned. Now, it's time for cutting and sewing.\n\nLet's head to the Cutting Room.
   PL: Wymiary Pwie zostały zmierzone, a wykroje przygotowane. Zostały krojenie i szycie. Udamy się do Pracowni Krojenia.
339. [RPG [Q-3004] — krok 1 — cel zadania 1] 절삭실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3004].steps[#0].goalDescription1
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [RPG [Q-3004] — krok 2 — cel zadania 1] 절삭 공정이 끝날 때까지 몰려오는 적들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3004].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Hold the position against the onslaught of enemies until the cutting process is completed.
   PL: Odpieraj nawałę wrogów, aż proces krojenia się skończy
341. [RPG [Q-3004] — krok 3 — cel zadania 1] 절삭 기계 확인하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3004].steps[#2].goalDescription1
   limit: do 120 znaków
   EN: Check the cutting machine
   PL: Sprawdź Maszynę Krojącą
342. [RPG [Q-3007] — tytuł] 봉제 마치기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3007].title
   limit: do 40 znaków
   EN: Finish the Sewing Process
   PL: Zakończ szycie
343. [RPG [Q-3007] — opis] 절삭 작업이 끝났다. 이제 키우는 자로부터 봉제를 맡기면 황금 가죽 옷은 완성이 될 것이다.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3007].description
   limit: do 150 znaków
   EN: The cutting is complete. Once the Nurturer handles the stitching, the Golden Hide garment should be finished.
   PL: Krojenie się skończyło. Gdy Hodowca przejmie szycie, ubranie ze Złotej Skóry będzie gotowe.
344. [RPG [Q-3007] — krok 1 — cel zadania 1] 키우는 자에게 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3007].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the Nurturer
   PL: Udaj się do Hodowcy
345. [RPG [Q-3007] — krok 2 — cel zadania 1] 키우는 자가 봉제 작업을 끝마칠 때까지 몰려오는 적들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3007].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Hold off the incoming enemies until the Nurturer finishes stitching
   PL: Odpieraj nadciągających wrogów, aż Hodowca skończy szyć
346. [RPG [Q-3001] — tytuł] 통제자에게 완성된 황금 수의를 받기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3001].title
   limit: do 60 znaków
   EN: Receive the Golden Shroud from the Overseer
   PL: Odbierz Złoty Całun od Nadzorcy
347. [RPG [Q-3001] — opis] 공정은 다 끝난 것 같다. 통제자에게 완성된 옷을 받자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3001].description
   limit: do 130 znaków
   EN: Looks like the whole process is complete. We should collect the finished garment from the Overseer.
   PL: Chyba cały proces się zakończył. Odbierzmy gotowe ubranie od Nadzorcy.
348. [RPG [Q-3001] — krok 1 — cel zadania 1] 통제자에게 완성된 황금 수의를 받기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3001].steps[#0].goalDescription1
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [RPG [Q-3005] — tytuł] 통제자 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3005].title
   limit: do 40 znaków
   EN: Kill the Overseer
   PL: Zabij Nadzorcę
350. [RPG [Q-3005] — opis] 통제자가 황금가죽 옷을 완성시켜주었지만 넘겨주기에는 아까웠는지 우리를 공격하기 시작했다. 통제자를 처치하고 완성된 황금가죽 옷을 가져가자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3005].description
   limit: do 230 znaków
   EN: The Overseer finished the Golden Hide garment, but apparently couldn't bear to hand it over and turned on us instead. We should defeat the Overseer and claim the finished garment.
   PL: Nadzorca uszył ubranie ze Złotej Skóry, ale żal mu było go oddać, więc zaatakował nas. Pokonajmy Nadzorcę i zabierzmy gotowe ubranie.
351. [RPG [Q-3005] — krok 1 — cel zadania 1] 통제자 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3005].steps[#0].goalDescription1
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [RPG [Q-3002] — tytuł] 5층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3002].title
   limit: do 40 znaków
   EN: Head to 5F
   PL: Udaj się na 5. piętro
353. [RPG [Q-3002] — opis] 통제자가 완성해준 황금가죽 옷을 뿌이가 입었다. 하지만 꼬물이를 먹어치워버린 뿌이의 기분은 그다지 좋지 않아 보인다. 이제 5층으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3002].description
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Overseer completed the Golden Hide, allowing Pwie to don clothing made from it. Pwie, however, doesn't seem glad at all after devouring Wriggley.\n... It's time to head to 5F.
   PL: Pwie przywdział ubranie uszyte przez Nadzorcę ze Złotej Skóry. Ale Pwie, który pożarł Wriggleya, widać, nie ma dobrego humoru. Czas udać się na 5. piętro.
354. [RPG [Q-3002] — krok 1 — cel zadania 1] 5층에 도달하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3002].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Reach 5F
   PL: Dotrzyj na 5. piętro
355. [RPG [Q-3003A] — tytuł] 태닝실 공정
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003A].title
   limit: do 40 znaków
   EN: The Process at the Tannery
   PL: Proces w Garbarni
356. [RPG [Q-3003A] — krok 1 — cel zadania 1] 태닝실 공정을 끝까지 지킨다
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003A].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: See the tanning process through to completion
   PL: Przyglądamy się procesowi w Garbarni do końca
357. [RPG [Q-3003B] — tytuł] 절삭실 공정
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003B].title
   limit: do 50 znaków
   EN: The Process at the Cutting Room
   PL: Proces w Pracowni Krojenia
358. [RPG [Q-3003B] — krok 1 — cel zadania 1] 절삭실 공정을 끝까지 지킨다
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003B].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: See the cutting process through to completion
   PL: Przyglądamy się procesowi krojenia do końca
359. [RPG [Q-3003C] — tytuł] 바깥 광장 공정
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003C].title
   limit: do 50 znaków
   EN: The Process at the Outdoor Plaza
   PL: Proces na Placu na Zewnątrz
360. [RPG [Q-3003C] — krok 1 — cel zadania 1] 바깥 광장 공정을 끝까지 지킨다
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3003C].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: See the process at the Outdoor Plaza through to completion
   PL: Przyglądamy się procesowi na Placu na Zewnątrz do końca
361. [RPG [Q-3011R] — tytuł] 수셰프와 재협상하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011R].title
   limit: do 50 znaków
   EN: Negotiate with Sous Chef again
   PL: Negocjuj z Sous Chef ponownie
362. [RPG [Q-3011R] — opis] 팔을 내주는 거래는 대가가 너무 컸다. 지하 1층 푸드코트의 수셰프에게 돌아가 다른 대가로 황금가죽을 협상하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011R].description
   limit: do 170 znaków
   EN: The consequence of giving up the arm was too dire. Let's return to Sous Chef on B1F's Food Court and offer her another trade.
   PL: Cena oddania ramienia była za wysoka. Wróćmy do Sous Chef ze Strefy Gastronomicznej na poziomie -1 i zaoferujmy jej inną zapłatę za Złotą Skórę.
363. [RPG [Q-3011R] — krok 1 — cel zadania 1] 수셰프와 재협상하기
   źródło: RPGSystem/rpg-loc-quest-floor-b3-b.json :: dataList[key=Q-3011R].steps[#0].goalDescription1
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b3] — rpg-loc-swarm-mob-floor-b3-b
- obszar/warstwa: `floor-b3` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

364. [RPG [swarm_b_3_leather_ghost] — nazwa wyświetlana] 길들여진 가죽
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b_3_leather_ghost].displayName
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [RPG [swarm_horizontal_hide_b3] — nazwa wyświetlana] 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_horizontal_hide_b3].displayName
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [RPG [swarm_leather_mutt_b3] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_leather_mutt_b3].displayName
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [RPG [swarm_b3_larouge_1st] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b3_larouge_1st].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [RPG [swarm_b3_larouge_2nd] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b3_larouge_2nd].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [RPG [swarm_b3_larouge_3rd] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b3_larouge_3rd].displayName
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [RPG [swarm_b3_golden_mutt] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b3_golden_mutt].displayName
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [RPG [swarm_b3_needle] — nazwa wyświetlana] 바늘꽂이
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b3_needle].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [RPG [swarm_b3_overhide] — nazwa wyświetlana] 뭉쳐 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json :: dataList[key=swarm_b3_overhide].displayName
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [inne] — rpg-loc-npc-route-a-warden
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-npc-route-a-warden.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

373. [RPG [N999999] — nazwa wyświetlana] 간수
   źródło: RPGSystem/rpg-loc-npc-route-a-warden.json :: dataList[key=N999999].displayName
   limit: do 40 znaków
   EN: The Warden
   PL: Strażnik

## Tryb RPG [inne] — rpg-loc-npc-route-b-warden
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-npc-route-b-warden.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

374. [RPG [N999999] — nazwa wyświetlana] 간수
   źródło: RPGSystem/rpg-loc-npc-route-b-warden.json :: dataList[key=N999999].displayName
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [RPG [N999998] — nazwa wyświetlana] 간수
   źródło: RPGSystem/rpg-loc-npc-route-b-warden.json :: dataList[key=N999998].displayName
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [inne] — rpg-loc-npc-route-b
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-npc-route-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

376. [RPG [N400041] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N400041].displayName
   limit: do 40 znaków
   EN: Pwie
   PL: Pwie
377. [RPG [N400042] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N400042].displayName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [RPG [N400043] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N400043].displayName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [RPG [N999101] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N999101].displayName
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [RPG [N999102] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N999102].displayName
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [RPG [N999103] — nazwa wyświetlana] 르누아르 메종
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N999103].displayName
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [RPG [N999104] — nazwa wyświetlana] 르누아르 메종 점원
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N999104].displayName
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [RPG [N999105] — nazwa wyświetlana] 르누아르 컨템포러리 점원
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N999105].displayName
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [RPG [N999106] — nazwa wyświetlana] 르누아르 신발관 점원
   źródło: RPGSystem/rpg-loc-npc-route-b.json :: dataList[key=N999106].displayName
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [inne] — rpg-loc-npc-route-c-warden
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-npc-route-c-warden.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

385. [RPG [N999999] — nazwa wyświetlana] 간수
   źródło: RPGSystem/rpg-loc-npc-route-c-warden.json :: dataList[key=N999999].displayName
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [inne] — rpg-loc-player-route-a
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-player-route-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

386. [RPG [1] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=1].displayName
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang
387. [RPG [2] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=2].displayName
   limit: do 40 znaków
   EN: Faust
   PL: Faust
388. [RPG [3] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=3].displayName
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
389. [RPG [4] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=4].displayName
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
390. [RPG [5] — nazwa wyświetlana] 뫼르소
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=5].displayName
   limit: do 40 znaków
   EN: Meursault
   PL: Meursault
391. [RPG [6] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=6].displayName
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu
392. [RPG [7] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=7].displayName
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
393. [RPG [8] — nazwa wyświetlana] 이스마엘
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=8].displayName
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael
394. [RPG [9] — nazwa wyświetlana] 로쟈
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=9].displayName
   limit: do 40 znaków
   EN: Rodion
   PL: Rodion
395. [RPG [10] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=10].displayName
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair
396. [RPG [11] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=11].displayName
   limit: do 40 znaków
   EN: Outis
   PL: Outis
397. [RPG [12] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=12].displayName
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor
398. [RPG [13] — nazwa wyświetlana] 단테
   źródło: RPGSystem/rpg-loc-player-route-a.json :: dataList[key=13].displayName
   limit: do 40 znaków
   EN: Dante
   PL: Dante

## Tryb RPG [inne] — rpg-loc-player-route-b
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-player-route-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

399. [RPG [1] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=1].displayName
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [RPG [2] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=2].displayName
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [RPG [3] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=3].displayName
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [RPG [4] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=4].displayName
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [RPG [5] — nazwa wyświetlana] 뫼르소
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=5].displayName
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [RPG [6] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=6].displayName
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [RPG [7] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=7].displayName
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [RPG [8] — nazwa wyświetlana] 이스마엘
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=8].displayName
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [RPG [9] — nazwa wyświetlana] 로쟈
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=9].displayName
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [RPG [10] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=10].displayName
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [RPG [11] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=11].displayName
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [RPG [12] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=12].displayName
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [RPG [13] — nazwa wyświetlana] 단테
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=13].displayName
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [RPG [400041] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=400041].displayName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [RPG [400042] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=400042].displayName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [RPG [400043] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-player-route-b.json :: dataList[key=400043].displayName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [inne] — rpg-loc-player-route-c
- obszar/warstwa: `inne` · plik gry: `RPGSystem/rpg-loc-player-route-c.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

415. [RPG [1] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=1].displayName
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [RPG [2] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=2].displayName
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [RPG [3] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=3].displayName
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [RPG [4] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=4].displayName
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [RPG [5] — nazwa wyświetlana] 뫼르소
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=5].displayName
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [RPG [6] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=6].displayName
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [RPG [7] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=7].displayName
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [RPG [8] — nazwa wyświetlana] 이스마엘
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=8].displayName
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [RPG [9] — nazwa wyświetlana] 로쟈
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=9].displayName
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [RPG [10] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=10].displayName
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [RPG [11] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=11].displayName
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [RPG [12] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=12].displayName
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [RPG [13] — nazwa wyświetlana] 단테
   źródło: RPGSystem/rpg-loc-player-route-c.json :: dataList[key=13].displayName
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
