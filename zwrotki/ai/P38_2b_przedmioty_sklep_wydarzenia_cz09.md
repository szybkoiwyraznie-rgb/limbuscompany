# Paczka AI P38 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 9/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P38_2b_przedmioty_sklep_wydarzenia_cz09.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P38_2b_przedmioty_sklep_wydarzenia_cz09.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Przedmioty, sklep i profil gracza: UserBanner
- plik gry: `UserBanner.json`

1. [Przedmioty, sklep i profil gracza [27] — opis] 시즌 3 본 보야지 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=27].desc
   limit: do 150 znaków
   EN: Obtained by clearing the Terminus of Line 3 with 100 Turns or less Total Turns before Season 3: Bon Voyage ends
   PL: Zdobyto za ukończenie stacji końcowej Linii 3 z limitem 100 tur łącznych przed końcem Sezonu 3: Bon Voyage
2. [Przedmioty, sklep i profil gracza [28] — nazwa] 육참골단
   źródło: UserBanner.json :: dataList[id=28].name
   limit: do 50 znaków
   EN: Yield My Flesh to Claim Their Bones
   PL: Oddam Ciało, by Złamać Ich Kości
3. [Przedmioty, sklep i profil gracza [28] — opis] 육참골단 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=28].desc
   limit: do 120 znaków
   EN: Obtained from the 'Yield My Flesh to Claim Their Bones' event
   PL: Zdobyto z wydarzenia „Oddam Ciało, by Złamać Ich Kości”
4. [Przedmioty, sklep i profil gracza [29] — nazwa] 육참골단 - 특별 배너
   źródło: UserBanner.json :: dataList[id=29].name
   limit: do 70 znaków
   EN: Yield My Flesh to Claim Their Bones - Special Banner
   PL: Oddam Ciało, by Złamać Ich Kości — Specjalny Banner
5. [Przedmioty, sklep i profil gracza [29] — opis] 육참골단 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=29].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Przedmioty, sklep i profil gracza [30] — nazwa] 림버스 컴퍼니 1주년 기념 배너
   źródło: UserBanner.json :: dataList[id=30].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Limbus Company\n1st Anniversary Banner
   PL: Banner Pamiątkowy 1. Rocznicy Limbus Company
7. [Przedmioty, sklep i profil gracza [30] — opis] 1주년 기념 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=30].desc
   limit: do 120 znaków
   EN: Obtained from the 1st Anniversary event
   PL: Zdobyto z wydarzenia 1. Rocznicy
8. [Przedmioty, sklep i profil gracza [31] — nazwa] 시즌 4 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=31].name
   limit: do 40 znaków
   EN: Season 4 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 4
9. [Przedmioty, sklep i profil gracza [31] — opis] 시즌 4 클리어 올 캐시 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=31].desc
   limit: do 120 znaków
   EN: Obtained at Season 4 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 4: Clear All Cathy
10. [Przedmioty, sklep i profil gracza [32] — nazwa] 시즌 4 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=32].name
   limit: do 40 znaków
   EN: Season 4 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 4
11. [Przedmioty, sklep i profil gracza [32] — opis] 시즌 4 클리어 올 캐시 림버스 패스 보상 120레벨에 획득
   źródło: UserBanner.json :: dataList[id=32].desc
   limit: do 120 znaków
   EN: Obtained at Season 4 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 4: Clear All Cathy
12. [Przedmioty, sklep i profil gracza [33] — nazwa] 시즌 4 림버스 패키지 특별 배너
   źródło: UserBanner.json :: dataList[id=33].name
   limit: do 60 znaków
   EN: Season 4 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 4
13. [Przedmioty, sklep i profil gracza [33] — opis] 시즌 4 클리어 올 캐시 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=33].desc
   limit: do 120 znaków
   EN: Obtained from Season 4 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 4
14. [Przedmioty, sklep i profil gracza [34] — nazwa] 시즌 4 림버스 패키지 특별 배너 II
   źródło: UserBanner.json :: dataList[id=34].name
   limit: do 60 znaków
   EN: Season 4 Limbus Package Special Banner II
   PL: Specjalny Banner Pakietu Limbus Sezonu 4 II
15. [Przedmioty, sklep i profil gracza [34] — opis] 시즌 4 클리어 올 캐시 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=34].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Przedmioty, sklep i profil gracza [35] — nazwa] 라이브러리 오브 루이나
   źródło: UserBanner.json :: dataList[id=35].name
   limit: do 40 znaków
   EN: Library of Ruina
   PL: Library of Ruina
17. [Przedmioty, sklep i profil gracza [35] — opis] 라이브러리 오브 루이나 구매 특전 쿠폰 등록 시 획득
   źródło: UserBanner.json :: dataList[id=35].desc
   limit: do 120 znaków
   EN: Obtained from entering Library of Ruina special bonus coupon code
   PL: Zdobyto po wpisaniu kodu kuponu specjalnego bonusu Library of Ruina
18. [Przedmioty, sklep i profil gracza [36] — nazwa] 새벽 사무소
   źródło: UserBanner.json :: dataList[id=36].name
   limit: do 40 znaków
   EN: Dawn Office
   PL: Biuro Świtu
19. [Przedmioty, sklep i profil gracza [36] — opis] 제3회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=36].desc
   limit: do 120 znaków
   EN: Obtained from the 3rd Walpurgis Night Event
   PL: Zdobyto z wydarzenia 3. Nocy Walpurgii
20. [Przedmioty, sklep i profil gracza [37] — nazwa] 시간살인시간
   źródło: UserBanner.json :: dataList[id=37].name
   limit: do 40 znaków
   EN: Timekilling Time
   PL: Czas Zabijania Czasu
21. [Przedmioty, sklep i profil gracza [37] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=37].desc
   limit: do 120 znaków
   EN: Obtained from the Timekilling Time event
   PL: Zdobyto z wydarzenia Czas Zabijania Czasu
22. [Przedmioty, sklep i profil gracza [38] — nazwa] 시간살인시간 - 특별 배너
   źródło: UserBanner.json :: dataList[id=38].name
   limit: do 50 znaków
   EN: Timekilling Time - Special Banner
   PL: Czas Zabijania Czasu — Specjalny Banner
23. [Przedmioty, sklep i profil gracza [38] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=38].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Przedmioty, sklep i profil gracza [39] — nazwa] 거울굴절철도 4호선 기념 배너
   źródło: UserBanner.json :: dataList[id=39].name
   limit: do 50 znaków
   EN: Refraction Railway Line 4 Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 4
25. [Przedmioty, sklep i profil gracza [39] — opis] 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=39].desc
   limit: do 120 znaków
   EN: Obtained by clearing Section #4 of Refraction Railway Line 4
   PL: Zdobyto za ukończenie Odcinka 4 Kolei Załamania — Linia 4
26. [Przedmioty, sklep i profil gracza [40] — nazwa] 거울굴절철도 4호선 특별 기념 배너
   źródło: UserBanner.json :: dataList[id=40].name
   limit: do 60 znaków
   EN: Special Refraction Railway Line 4 Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 4
27. [Przedmioty, sklep i profil gracza [40] — opis] 시즌 4 클리어 올 캐시 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=40].desc
   limit: do 150 znaków
   EN: Obtained by clearing Section #4 of Line 4 with 100 Turns or fewer Total Turns before Season 4: Clear All Cathy ends
   PL: Zdobyto za ukończenie Odcinka 4 Linii 4 z limitem 100 tur łącznych przed końcem Sezonu 4: Clear All Cathy
28. [Przedmioty, sklep i profil gracza [41] — nazwa] 워프특급 살인사건
   źródło: UserBanner.json :: dataList[id=41].name
   limit: do 40 znaków
   EN: Murder on the WARP Express
   PL: Morderstwo w Ekspresie WARP
29. [Przedmioty, sklep i profil gracza [41] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=41].desc
   limit: do 120 znaków
   EN: Obtained from the Murder on the WARP Express event
   PL: Zdobyto z wydarzenia Morderstwo w Ekspresie WARP
30. [Przedmioty, sklep i profil gracza [42] — nazwa] 워프특급 살인사건 - 특별 배너
   źródło: UserBanner.json :: dataList[id=42].name
   limit: do 60 znaków
   EN: Murder on the WARP Express - Special Banner
   PL: Morderstwo w Ekspresie WARP — Specjalny Banner
31. [Przedmioty, sklep i profil gracza [42] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=42].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Przedmioty, sklep i profil gracza [43] — nazwa] 자색 정오
   źródło: UserBanner.json :: dataList[id=43].name
   limit: do 40 znaków
   EN: Noon of Violet
   PL: Fioletowe Południe
33. [Przedmioty, sklep i profil gracza [43] — opis] 제4회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=43].desc
   limit: do 120 znaków
   EN: Obtained from the 4th Walpurgis Night event
   PL: Zdobyto z wydarzenia 4. Nocy Walpurgii
34. [Przedmioty, sklep i profil gracza [48] — nazwa] 마침표 사무소
   źródło: UserBanner.json :: dataList[id=48].name
   limit: do 40 znaków
   EN: Full-Stop Office
   PL: Biuro Kropki
35. [Przedmioty, sklep i profil gracza [48] — opis] 제5회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=48].desc
   limit: do 120 znaków
   EN: Obtained from the 5th Walpurgis Night event
   PL: Zdobyto z wydarzenia 5. Nocy Walpurgii
36. [Przedmioty, sklep i profil gracza [49] — nazwa] LCB 정기검진
   źródło: UserBanner.json :: dataList[id=49].name
   limit: do 40 znaków
   EN: LCB Regular Check-up
   PL: Okresowe Badania LCB
37. [Przedmioty, sklep i profil gracza [49] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=49].desc
   limit: do 120 znaków
   EN: Obtained from the LCB Regular Check-up event
   PL: Zdobyto z wydarzenia Okresowe Badania LCB
38. [Przedmioty, sklep i profil gracza [50] — nazwa] LCB 정기검진 - 특별 배너
   źródło: UserBanner.json :: dataList[id=50].name
   limit: do 60 znaków
   EN: LCB Regular Check-up - Special Banner
   PL: Okresowe Badania LCB — Specjalny Banner
39. [Przedmioty, sklep i profil gracza [50] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=50].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Przedmioty, sklep i profil gracza [51] — nazwa] 거울굴절철도 5호선 기념 배너
   źródło: UserBanner.json :: dataList[id=51].name
   limit: do 50 znaków
   EN: Refraction Railway Line 5 Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 5
41. [Przedmioty, sklep i profil gracza [51] — opis] 거울굴절철도 5호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=51].desc
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 5
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 5
42. [Przedmioty, sklep i profil gracza [52] — nazwa] 거울굴절철도 5호선 특별 기념 배너
   źródło: UserBanner.json :: dataList[id=52].name
   limit: do 60 znaków
   EN: Special Refraction Railway Line 5 Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 5
43. [Przedmioty, sklep i profil gracza [52] — opis] 시즌 5 오블리비언 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 5호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=52].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 5 with 100 or fewer Total Turns before Season 5: Oblivion ends.
   PL: Zdobyto za ukończenie Linii 5 z limitem 100 tur łącznych przed końcem Sezonu 5: Oblivion
44. [Przedmioty, sklep i profil gracza [53] — nazwa] 림버스 컴퍼니 2주년 기념 배너
   źródło: UserBanner.json :: dataList[id=53].name
   limit: do 60 znaków
   EN: Limbus Company 2nd Anniversary Banner
   PL: Banner Pamiątkowy 2. Rocznicy Limbus Company
45. [Przedmioty, sklep i profil gracza [53] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=53].desc
   limit: do 120 znaków
   EN: Obtained from the 2nd Anniversary event
   PL: Zdobyto z wydarzenia 2. Rocznicy
46. [Przedmioty, sklep i profil gracza [54] — nazwa] 림버스 컴퍼니 2주년 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=54].name
   limit: do 70 znaków
   EN: Limbus Company 2nd Anniversary Special Banner
   PL: Specjalny Banner Pamiątkowy 2. Rocznicy Limbus Company
47. [Przedmioty, sklep i profil gracza [54] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=54].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Przedmioty, sklep i profil gracza [55] — nazwa] 시즌 5 꿈결의 거울 기념 배너
   źródło: UserBanner.json :: dataList[id=55].name
   limit: do 80 znaków
   EN: Season 5: Mirror of the Dreaming Commemorative Banner
   PL: Banner Pamiątkowy Sezonu 5: Lustro Snu
49. [Przedmioty, sklep i profil gracza [55] — opis] 꿈결의 거울 업적 보상으로 획득\n\n※ 「시즌 5 거울 던전 - 꿈결의 거울」을 5층 이상 클리어한 횟수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=55].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of the Dreaming Achievements Rewards\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 5 Mirror Dungeon - Mirror of the Dreaming」.
   PL: Zdobyto jako nagroda osiągnięć Lustra Snu\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 5 — Lustro Snu”.
50. [Przedmioty, sklep i profil gracza [56] — nazwa] 시즌 5 꿈결의 거울 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=56].name
   limit: do 90 znaków
   EN: Season 5: Mirror of the Dreaming Special Commemorative Banner
   PL: Specjalny Banner Pamiątkowy Sezonu 5: Lustro Snu
51. [Przedmioty, sklep i profil gracza [56] — opis] 꿈결의 거울 업적 보상으로 획득\n\n※ 「시즌 5 거울 던전 - 꿈결의 거울」을 5층 이상 클리어한 횟수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=56].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Przedmioty, sklep i profil gracza [57] — nazwa] 심야청소
   źródło: UserBanner.json :: dataList[id=57].name
   limit: do 40 znaków
   EN: Nocturnal Sweeping
   PL: Nocne Sprzątanie
53. [Przedmioty, sklep i profil gracza [57] — opis] 심야청소 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=57].desc
   limit: do 120 znaków
   EN: Obtained from the 'Nocturnal Sweeping' event
   PL: Zdobyto z wydarzenia Nocne Sprzątanie
54. [Przedmioty, sklep i profil gracza [58] — nazwa] 심야청소 - 특별 배너
   źródło: UserBanner.json :: dataList[id=58].name
   limit: do 50 znaków
   EN: Nocturnal Sweeping - Special Banner
   PL: Nocne Sprzątanie — Specjalny Banner
55. [Przedmioty, sklep i profil gracza [58] — opis] 심야청소 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=58].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Przedmioty, sklep i profil gracza [59] — nazwa] 시즌 5 꿈결의 거울 업적 특별 배너
   źródło: UserBanner.json :: dataList[id=59].name
   limit: do 80 znaków
   EN: Season 5: Mirror of the Dreaming Special Achievement Banner
   PL: Specjalny Banner Osiągnięć Sezonu 5: Lustro Snu
57. [Przedmioty, sklep i profil gracza [59] — opis] 꿈결의 거울 모든 업적 달성 보상으로 획득\n\n해당 아이템 수령 시 시즌 5 꿈결의 거울 기념 배너, 기념 특별 배너 아이템이 업적 특별 배너의 디자인으로 변경됩니다.\n\n※ 「시즌 5 거울 던전 - 꿈결의 거울」을 5층 이상 클리어한 횟수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=59].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of the Dreaming by completing all Achievements\n\nObtaining this item will update the designs of the following with the Special Achievement Banner look: Season 5: Mirror of the Dreaming Commemorative Banner & Special Commemorative Banner\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 5 Mirror Dungeon - Mirror of the Dreaming」.
   PL: Zdobyto za osiągnięcie wszystkich Osiągnięć Lustra Snu\n\nPo otrzymaniu tego przedmiotu Banner Pamiątkowy Sezonu 5: Lustro Snu oraz Specjalny Banner Pamiątkowy zmienią wygląd na Specjalny Banner Osiągnięć.\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 5 — Lustro Snu”.
58. [Przedmioty, sklep i profil gracza [66] — nazwa] 시즌 6 영생의 거울 기념 배너
   źródło: UserBanner.json :: dataList[id=66].name
   limit: do 70 znaków
   EN: Season 6: Mirror of Immortality Commemorative Banner
   PL: Banner Pamiątkowy Sezonu 6: Lustro Nieśmiertelności
59. [Przedmioty, sklep i profil gracza [66] — opis] 영생의 거울 업적 보상으로 획득\n\n※ 「시즌 6 거울 던전 - 영생의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=66].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of Immortality Achievements Rewards\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 6 Mirror Dungeon - Mirror of Immortality」, and the highest Floor you've reached.
   PL: Zdobyto jako nagroda osiągnięć Lustra Nieśmiertelności\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 6 — Lustro Nieśmiertelności” oraz najwyższe osiągnięte piętro.
60. [Przedmioty, sklep i profil gracza [67] — nazwa] 시즌 6 영생의 거울 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=67].name
   limit: do 80 znaków
   EN: Season 6: Mirror of Immortality Special Commemorative Banner
   PL: Specjalny Banner Pamiątkowy Sezonu 6: Lustro Nieśmiertelności
61. [Przedmioty, sklep i profil gracza [67] — opis] 영생의 거울 업적 보상으로 획득\n\n※ 「시즌 6 거울 던전 - 영생의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=67].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Przedmioty, sklep i profil gracza [68] — nazwa] 시즌 6 영생의 거울 업적 특별 배너
   źródło: UserBanner.json :: dataList[id=68].name
   limit: do 80 znaków
   EN: Season 6: Mirror of Immortality Special Achievement Banner
   PL: Specjalny Banner Osiągnięć Sezonu 6: Lustro Nieśmiertelności
63. [Przedmioty, sklep i profil gracza [68] — opis] 영생의 거울 모든 업적 달성 보상으로 획득\n\n해당 아이템 수령 시 시즌 6 영생의 거울 기념 배너, 기념 특별 배너 아이템이 업적 특별 배너의 디자인으로 변경됩니다.\n\n※ 「시즌 6 거울 던전 - 영생의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=68].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of Immortality by completing all Achievements\n\nObtaining this item will update the designs of the following with the Special Achievement Banner look: Season 6: Mirror Immortality Commemorative Banner & Special Commemorative Banner\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 6 Mirror Dungeon - Mirror Immortality」.
   PL: Zdobyto za osiągnięcie wszystkich Osiągnięć Lustra Nieśmiertelności\n\nPo otrzymaniu tego przedmiotu Banner Pamiątkowy Sezonu 6: Lustro Nieśmiertelności oraz Specjalny Banner Pamiątkowy zmienią wygląd na Specjalny Banner Osiągnięć.\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 6 — Lustro Nieśmiertelności” oraz najwyższe osiągnięte piętro.
64. [Przedmioty, sklep i profil gracza [44] — nazwa] 시즌 5 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=44].name
   limit: do 40 znaków
   EN: Season 5 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 5
65. [Przedmioty, sklep i profil gracza [44] — opis] 시즌 5 오블리비언 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=44].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 5: Oblivion
66. [Przedmioty, sklep i profil gracza [45] — nazwa] 시즌 5 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=45].name
   limit: do 40 znaków
   EN: Season 5 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 5
67. [Przedmioty, sklep i profil gracza [45] — opis] 시즌 5 오블리비언 림버스 패스 보상 120레벨에 획득
   źródło: UserBanner.json :: dataList[id=45].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 5: Oblivion
68. [Przedmioty, sklep i profil gracza [46] — nazwa] 시즌 5 림버스 패키지 특별 배너
   źródło: UserBanner.json :: dataList[id=46].name
   limit: do 60 znaków
   EN: Season 5 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 5
69. [Przedmioty, sklep i profil gracza [46] — opis] 시즌 5 오블리비언 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=46].desc
   limit: do 120 znaków
   EN: Obtained from Season 5 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 5
70. [Przedmioty, sklep i profil gracza [47] — nazwa] 시즌 5 림버스 패키지 특별 배너 II
   źródło: UserBanner.json :: dataList[id=47].name
   limit: do 60 znaków
   EN: Season 5 Limbus Package Special Banner II
   PL: Specjalny Banner Pakietu Limbus Sezonu 5 II
71. [Przedmioty, sklep i profil gracza [47] — opis] 시즌 5 오블리비언 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=47].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Przedmioty, sklep i profil gracza [60] — nazwa] 시즌 6 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=60].name
   limit: do 40 znaków
   EN: Season 6 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 6
73. [Przedmioty, sklep i profil gracza [60] — opis] 시즌 6 장화인 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=60].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 6: Zàng Huā Yín
74. [Przedmioty, sklep i profil gracza [61] — nazwa] 시즌 6 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=61].name
   limit: do 40 znaków
   EN: Season 6 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 6
75. [Przedmioty, sklep i profil gracza [61] — opis] 시즌 6 장화인 림버스 패스 보상 120레벨에 획득
   źródło: UserBanner.json :: dataList[id=61].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 6: Zàng Huā Yín
76. [Przedmioty, sklep i profil gracza [62] — nazwa] 시즌 6 림버스 패키지 특별 배너
   źródło: UserBanner.json :: dataList[id=62].name
   limit: do 60 znaków
   EN: Season 6 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 6
77. [Przedmioty, sklep i profil gracza [62] — opis] 시즌 6 장화인 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=62].desc
   limit: do 120 znaków
   EN: Obtained from Season 6 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 6
78. [Przedmioty, sklep i profil gracza [63] — nazwa] 마법소녀
   źródło: UserBanner.json :: dataList[id=63].name
   limit: do 40 znaków
   EN: Magical Girl
   PL: Czarodziejska Panienka
79. [Przedmioty, sklep i profil gracza [63] — opis] 제6회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=63].desc
   limit: do 120 znaków
   EN: Obtained from the 6th Walpurgis Night event
   PL: Zdobyto z wydarzenia 6. Nocy Walpurgii
80. [Przedmioty, sklep i profil gracza [64] — nazwa] 절차탁춘
   źródło: UserBanner.json :: dataList[id=64].name
   limit: do 40 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
81. [Przedmioty, sklep i profil gracza [64] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=64].desc
   limit: do 120 znaków
   EN: Obtained from the 'Spring Cultivation' event
   PL: Zdobyto z wydarzenia Wiosenny Szlif
82. [Przedmioty, sklep i profil gracza [65] — nazwa] 절차탁춘 - 특별 배너
   źródło: UserBanner.json :: dataList[id=65].name
   limit: do 50 znaków
   EN: Spring Cultivation - Special Banner
   PL: Wiosenny Szlif — Specjalny Banner
83. [Przedmioty, sklep i profil gracza [65] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=65].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Przedmioty, sklep i profil gracza [69] — nazwa] 선의의 순례
   źródło: UserBanner.json :: dataList[id=69].name
   limit: do 40 znaków
   EN: Pilgrimage of Compassion
   PL: Pielgrzymka Współczucia
85. [Przedmioty, sklep i profil gracza [69] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=69].desc
   limit: do 120 znaków
   EN: Obtained from the Pilgrimage of Compassion event
   PL: Zdobyto z wydarzenia Pielgrzymka Współczucia
86. [Przedmioty, sklep i profil gracza [70] — nazwa] 선의의 순례 - 특별 배너
   źródło: UserBanner.json :: dataList[id=70].name
   limit: do 60 znaków
   EN: Pilgrimage of Compassion - Special Banner
   PL: Pielgrzymka Współczucia — Specjalny Banner
87. [Przedmioty, sklep i profil gracza [70] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=70].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Przedmioty, sklep i profil gracza [71] — nazwa] 어느 도서관의 일반적인 초대
   źródło: UserBanner.json :: dataList[id=71].name
   limit: do 60 znaków
   EN: A Certain Library's General Invitation
   PL: Zwykłe Zaproszenie z Pewnej Biblioteki
89. [Przedmioty, sklep i profil gracza [71] — opis] 제7회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=71].desc
   limit: do 120 znaków
   EN: Obtained from the 7th Walpurgis Night event
   PL: Zdobyto z wydarzenia 7. Nocy Walpurgii
90. [Przedmioty, sklep i profil gracza [72] — nazwa] 거울굴절철도 1호선 BokGak 특별 기념 배너
   źródło: UserBanner.json :: dataList[id=72].name
   limit: do 70 znaków
   EN: Special Refraction Railway Line 1 BokGak Banner
   PL: Specjalny Banner BokGak Kolei Załamania — Linia 1
91. [Przedmioty, sklep i profil gracza [72] — opis] 누적 턴 수 120턴 이하로 거울굴절철도 1호선 BokGak 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=72].desc
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 1 BokGak under 120 total turns
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 1 BokGak w limicie 120 tur łącznych
92. [Przedmioty, sklep i profil gracza [73] — nazwa] 시즌 7 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=73].name
   limit: do 40 znaków
   EN: Season 7 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 7
93. [Przedmioty, sklep i profil gracza [73] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=73].desc
   limit: do 120 znaków
   EN: Obtained at Season 7 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 7
94. [Przedmioty, sklep i profil gracza [74] — nazwa] 시즌 7 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=74].name
   limit: do 40 znaków
   EN: Season 7 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 7
95. [Przedmioty, sklep i profil gracza [74] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 림버스 패스 보상 120레벨에 획득
   źródło: UserBanner.json :: dataList[id=74].desc
   limit: do 120 znaków
   EN: Obtained at Season 7 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 7
96. [Przedmioty, sklep i profil gracza [75] — nazwa] 시즌 7 림버스 패키지 특별 배너
   źródło: UserBanner.json :: dataList[id=75].name
   limit: do 60 znaków
   EN: Season 7 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 7
97. [Przedmioty, sklep i profil gracza [75] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=75].desc
   limit: do 120 znaków
   EN: Obtained from Season 7 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 7
98. [Przedmioty, sklep i profil gracza [76] — nazwa] 림버스 컴퍼니 3주년 기념 배너
   źródło: UserBanner.json :: dataList[id=76].name
   limit: do 60 znaków
   EN: Limbus Company 3rd Anniversary Banner
   PL: Banner Pamiątkowy 3. Rocznicy Limbus Company
99. [Przedmioty, sklep i profil gracza [76] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=76].desc
   limit: do 120 znaków
   EN: Obtained from the 3rd Anniversary event
   PL: Zdobyto z wydarzenia 3. Rocznicy
100. [Przedmioty, sklep i profil gracza [77] — nazwa] 림버스 컴퍼니 3주년 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=77].name
   limit: do 70 znaków
   EN: Limbus Company 3rd Anniversary Special Banner
   PL: Specjalny Banner Pamiątkowy 3. Rocznicy Limbus Company
101. [Przedmioty, sklep i profil gracza [77] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=77].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Przedmioty, sklep i profil gracza [78] — nazwa] 호박색 어스름
   źródło: UserBanner.json :: dataList[id=78].name
   limit: do 40 znaków
   EN: The Dusk of Amber
   PL: Bursztynowy Zmierzch
103. [Przedmioty, sklep i profil gracza [78] — opis] 제8회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=78].desc
   limit: do 120 znaków
   EN: Obtained from the 8th Walpurgis Night event
   PL: Zdobyto z wydarzenia 8. Nocy Walpurgii
104. [Przedmioty, sklep i profil gracza [79] — nazwa] 시즌 7 이름과 거미의 거울 기념 배너
   źródło: UserBanner.json :: dataList[id=79].name
   limit: do 80 znaków
   EN: Season 7: Mirror of Names and Spiders Commemorative Banner
   PL: Banner Pamiątkowy Sezonu 7: Lustro Imion i Pająków
105. [Przedmioty, sklep i profil gracza [79] — opis] 이름과 거미의 거울 업적 보상으로 획득\n\n※ 「시즌 7 거울 던전 - 이름과 거미의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=79].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of Names and Spiders Achievements Rewards\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 7 Mirror Dungeon - Mirror of Names and Spiders」, and the highest Floor you've reached.
   PL: Zdobyto jako nagroda osiągnięć Lustra Imion i Pająków\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 7 — Lustro Imion i Pająków” oraz najwyższe osiągnięte piętro.
106. [Przedmioty, sklep i profil gracza [80] — nazwa] 시즌 7 이름과 거미의 거울 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=80].name
   limit: do 90 znaków
   EN: Season 7: Mirror of Names and Spiders Special Commemorative Banner
   PL: Specjalny Banner Pamiątkowy Sezonu 7: Lustro Imion i Pająków
107. [Przedmioty, sklep i profil gracza [80] — opis] 이름과 거미의 거울 업적 보상으로 획득\n\n※ 「시즌 7 거울 던전 - 이름과 거미의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=80].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Przedmioty, sklep i profil gracza [81] — nazwa] 시즌 7 이름과 거미의 거울 업적 특별 배너
   źródło: UserBanner.json :: dataList[id=81].name
   limit: do 90 znaków
   EN: Season 7: Mirror of Names and Spiders Special Achievement Banner
   PL: Specjalny Banner Osiągnięć Sezonu 7: Lustro Imion i Pająków
109. [Przedmioty, sklep i profil gracza [81] — opis] 이름과 거미의 거울 모든 업적 달성 보상으로 획득\n\n해당 아이템 수령 시 시즌 7 이름과 거미의 거울 기념 배너, 기념 특별 배너 아이템이 업적 특별 배너의 디자인으로 변경됩니다.\n\n※ 「시즌 7 거울 던전 - 이름과 거미의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=81].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of Names and Spiders by completing all Achievements\n\nObtaining this item will update the designs of the following with the Special Achievement Banner look: Season 7: Mirror of Names and Spiders Commemorative Banner & Special Commemorative Banner\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 7 Mirror Dungeon - Mirror of Names and Spiders」.
   PL: Zdobyto za osiągnięcie wszystkich Osiągnięć Lustra Imion i Pająków\n\nPo otrzymaniu tego przedmiotu Banner Pamiątkowy Sezonu 7: Lustro Imion i Pająków oraz Specjalny Banner Pamiątkowy zmienią wygląd na Specjalny Banner Osiągnięć.\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 7 — Lustro Imion i Pająków” oraz najwyższe osiągnięte piętro.
110. [Przedmioty, sklep i profil gracza [82] — nazwa] 타래 엮기
   źródło: UserBanner.json :: dataList[id=82].name
   limit: do 40 znaków
   EN: Twining Threads
   PL: Splatanie Pasm
111. [Przedmioty, sklep i profil gracza [82] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=82].desc
   limit: do 120 znaków
   EN: Obtained from the Twining Threads event
   PL: Zdobyto z wydarzenia Splatanie Pasm
112. [Przedmioty, sklep i profil gracza [83] — nazwa] 타래 엮기 - 특별 배너
   źródło: UserBanner.json :: dataList[id=83].name
   limit: do 50 znaków
   EN: Twining Threads - Special Banner
   PL: Splatanie Pasm — Specjalny Banner
113. [Przedmioty, sklep i profil gracza [83] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=83].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Przedmioty, sklep i profil gracza [84] — nazwa] 거울굴절철도 6호선 기념 배너
   źródło: UserBanner.json :: dataList[id=84].name
   limit: do 50 znaków
   EN: Refraction Railway Line 6 Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 6
115. [Przedmioty, sklep i profil gracza [84] — opis] 거울굴절철도 6호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=84].desc
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 6
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 6
116. [Przedmioty, sklep i profil gracza [85] — nazwa] 거울굴절철도 6호선 특별 기념 배너
   źródło: UserBanner.json :: dataList[id=85].name
   limit: do 60 znaków
   EN: Special Refraction Railway Line 6 Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 6
117. [Przedmioty, sklep i profil gracza [85] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 기간 내에 누적 턴 수 111턴 이하로 거울굴절철도 6호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=85].desc
   limit: do 140 znaków
   EN: Obtained by clearing Line 6 with 111 or fewer Total Turns before Season 7: Kumo no Ito · otI on akA ends.
   PL: Zdobyto za ukończenie Linii 6 z limitem 111 tur łącznych przed końcem Sezonu 7: Kumo no Ito · otI on akA
118. [Przedmioty, sklep i profil gracza [86] — nazwa] 경험기억
   źródło: UserBanner.json :: dataList[id=86].name
   limit: do 40 znaków
   EN: Mnestic Experience
   PL: Pamięć Doświadczenia
119. [Przedmioty, sklep i profil gracza [86] — opis] 경험기억 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=86].desc
   limit: do 120 znaków
   EN: Obtained from the Mnestic Experience event
   PL: Zdobyto z wydarzenia Pamięć Doświadczenia
120. [Przedmioty, sklep i profil gracza [87] — nazwa] 경험기억 - 특별 배너
   źródło: UserBanner.json :: dataList[id=87].name
   limit: do 50 znaków
   EN: Mnestic Experience - Special Banner
   PL: Pamięć Doświadczenia — Specjalny Banner
121. [Przedmioty, sklep i profil gracza [87] — opis] 경험기억 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=87].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Przedmioty, sklep i profil gracza [88] — nazwa] 새벽녘의 해결사
   źródło: UserBanner.json :: dataList[id=88].name
   limit: do 40 znaków
   EN: The Fixer at Dawnbreak
   PL: Fikser o Świcie
123. [Przedmioty, sklep i profil gracza [88] — opis] 제9회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=88].desc
   limit: do 120 znaków
   EN: Obtained from the 9th Walpurgis Night event
   PL: Zdobyto z wydarzenia 9. Nocy Walpurgii
124. [Przedmioty, sklep i profil gracza [89] — nazwa] 거울굴절철도 2호선 BokGak 특별 기념 배너
   źródło: UserBanner.json :: dataList[id=89].name
   limit: do 70 znaków
   EN: Special Refraction Railway Line 2 BokGak Banner
   PL: Specjalny Banner BokGak Kolei Załamania — Linia 2
125. [Przedmioty, sklep i profil gracza [89] — opis] 순환 횟수 5 이상, 누적 턴 수 150턴 이하로 거울굴절철도 2호선 BokGak 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=89].desc
   limit: do 140 znaków
   EN: Obtained by clearing Refraction Railway Line 2 BokGak with 5 or more Cycles and 150 or fewer Total Turns
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 2 BokGak z liczbą Cykli 5 lub więcej i limitem 150 tur łącznych
126. [Przedmioty, sklep i profil gracza [90] — nazwa] 시즌 8 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=90].name
   limit: do 40 znaków
   EN: Season 8 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 8
127. [Przedmioty, sklep i profil gracza [90] — opis] 시즌 8 푼크툼 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=90].desc
   limit: do 120 znaków
   EN: Obtained at Season 8 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 8
128. [Przedmioty, sklep i profil gracza [91] — nazwa] 시즌 8 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=91].name
   limit: do 40 znaków
   EN: Season 8 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 8
129. [Przedmioty, sklep i profil gracza [91] — opis] 시즌 8 푼크툼 림버스 패스 보상 120레벨에 획득
   źródło: UserBanner.json :: dataList[id=91].desc
   limit: do 120 znaków
   EN: Obtained at Season 8 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 8
130. [Przedmioty, sklep i profil gracza [92] — nazwa] 시즌 8 림버스 패키지 특별 배너
   źródło: UserBanner.json :: dataList[id=92].name
   limit: do 60 znaków
   EN: Season 8 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 8
131. [Przedmioty, sklep i profil gracza [92] — opis] 시즌 8 푼크툼 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=92].desc
   limit: do 120 znaków
   EN: Obtained from Season 8 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 8
132. [Przedmioty, sklep i profil gracza [93] — nazwa] 삽시호
   źródło: UserBanner.json :: dataList[id=93].name
   limit: do 40 znaków
   EN: Chachihu
   PL: Chachihu
133. [Przedmioty, sklep i profil gracza [93] — opis] 사영전투][투전영사 - 삽시호 Normal 난이도 24턴 이하로 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=93].desc
   limit: do 130 znaków
   EN: Obtained by clearing Reflectrial][lairtcelfeR - Chachihu on Normal Difficulty with 24 or fewer Turns
   PL: Zdobyto za ukończenie Reflectrial][lairtcelfeR — Chachihu na poziomie trudności Normal w limicie 24 tur
134. [Przedmioty, sklep i profil gracza [94] — nazwa] 시즌 8 시지프의 거울 기념 배너
   źródło: UserBanner.json :: dataList[id=94].name
   limit: do 70 znaków
   EN: Season 8: Mirror of Sisyphe Commemorative Banner
   PL: Banner Pamiątkowy Sezonu 8: Lustro Sisyphe
135. [Przedmioty, sklep i profil gracza [94] — opis] 시지프의 거울 업적 보상으로 획득\n\n※ 「시즌 8 거울 던전 - 시지프의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=94].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of Sisyphe Achievements Rewards\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 8 Mirror Dungeon - Mirror of Sisyphe」, and the highest Floor you've reached.
   PL: Zdobyto jako nagroda osiągnięć Lustra Sisyphe\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 8 — Lustro Sisyphe” oraz najwyższe osiągnięte piętro.
136. [Przedmioty, sklep i profil gracza [95] — nazwa] 시즌 8 시지프의 거울 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=95].name
   limit: do 80 znaków
   EN: Season 8: Mirror of Sisyphe Special Commemorative Banner
   PL: Specjalny Banner Pamiątkowy Sezonu 8: Lustro Sisyphe
137. [Przedmioty, sklep i profil gracza [95] — opis] 시지프의 거울 업적 보상으로 획득\n\n※ 「시즌 8 거울 던전 - 시지프의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=95].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Przedmioty, sklep i profil gracza [96] — nazwa] 시즌 8 시지프의 거울 업적 특별 배너
   źródło: UserBanner.json :: dataList[id=96].name
   limit: do 80 znaków
   EN: Season 8: Mirror of Sisyphe Special Achievement Banner
   PL: Specjalny Banner Osiągnięć Sezonu 8: Lustro Sisyphe
139. [Przedmioty, sklep i profil gracza [96] — opis] 시지프의 거울 모든 업적 달성 보상으로 획득\n\n해당 아이템 수령 시 시즌 8 시지프의 거울 기념 배너, 기념 특별 배너 아이템이 업적 특별 배너의 디자인으로 변경됩니다.\n\n※ 「시즌 8 거울 던전 - 시지프의 거울」을 5층 이상 클리어한 횟수와 도달한 최대 층수가 배너에 표시됩니다.
   źródło: UserBanner.json :: dataList[id=96].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained from the Mirror of Sisyphe by completing all Achievements\n\nObtaining this item will update the designs of the following with the Special Achievement Banner look: Season 8: Mirror of Sisyphe Commemorative Banner & Special Commemorative Banner\n\n※ This banner displays the number of times you've completed Floor 5 or higher in the 「Season 8 Mirror Dungeon - Mirror of Sisyphe」.
   PL: Zdobyto za osiągnięcie wszystkich Osiągnięć Lustra Sisyphe\n\nPo otrzymaniu tego przedmiotu Banner Pamiątkowy Sezonu 8: Lustro Sisyphe oraz Specjalny Banner Pamiątkowy zmienią wygląd na Specjalny Banner Osiągnięć.\n\n※ Banner wyświetla liczbę ukończeń od 5. Piętra wzwyż w „Lustrzanym Lochu Sezonu 8 — Lustro Sisyphe” oraz najwyższe osiągnięte piętro.
140. [Przedmioty, sklep i profil gracza [97] — nazwa] 쐐기 사무소
   źródło: UserBanner.json :: dataList[id=97].name
   limit: do 40 znaków
   EN: Wedge Office
   PL: Biuro Klinów
141. [Przedmioty, sklep i profil gracza [97] — opis] 제10회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=97].desc
   limit: do 120 znaków
   EN: Obtained from the 10th Walpurgis Night event
   PL: Zdobyto z wydarzenia 10. Nocy Walpurgii
142. [Przedmioty, sklep i profil gracza [98] — nazwa] 도상구축 Beta 기념 배너
   źródło: UserBanner.json :: dataList[id=98].name
   limit: do 50 znaków
   EN: Schemacraft Beta Celebratory Banner
   PL: Banner Świętowania Konstrukcji Schematów Beta
143. [Przedmioty, sklep i profil gracza [98] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserBanner.json :: dataList[id=98].desc
   limit: do 120 znaków
   EN: Obtained from the Schemacraft Beta Pass Reward
   PL: Zdobyto z nagrody przepustki Konstrukcji Schematów Beta
144. [Przedmioty, sklep i profil gracza [99] — nazwa] 도상구축 Beta 기념 특별 배너
   źródło: UserBanner.json :: dataList[id=99].name
   limit: do 60 znaków
   EN: Schemacraft Beta Celebratory Special Banner
   PL: Specjalny Banner Świętowania Konstrukcji Schematów Beta
145. [Przedmioty, sklep i profil gracza [99] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserBanner.json :: dataList[id=99].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-EGOBg-a1c10p1
- plik gry: `UserTicket-EGOBg-a1c10p1.json`

146. [Przedmioty, sklep i profil gracza [80] — nazwa] ???
   źródło: UserTicket-EGOBg-a1c10p1.json :: dataList[id=80].name
   limit: do 40 znaków
   EN: ???
   PL: ???
147. [Przedmioty, sklep i profil gracza [80] — opis] 시즌 8 푼크툼 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg-a1c10p1.json :: dataList[id=80].desc
   limit: do 120 znaków
   EN: Obtained at Season 8 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie darmowych nagród Sezonu 8
148. [Przedmioty, sklep i profil gracza [81] — nazwa] ???
   źródło: UserTicket-EGOBg-a1c10p1.json :: dataList[id=81].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Przedmioty, sklep i profil gracza [81] — opis] 시즌 8 푼크툼 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg-a1c10p1.json :: dataList[id=81].desc
   limit: do 120 znaków
   EN: Obtained at Season 8 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 8
150. [Przedmioty, sklep i profil gracza [82] — nazwa] ???
   źródło: UserTicket-EGOBg-a1c10p1.json :: dataList[id=82].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Przedmioty, sklep i profil gracza [82] — opis] 시즌 8 푼크툼 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg-a1c10p1.json :: dataList[id=82].desc
   limit: do 120 znaków
   EN: Obtained at Season 8 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie darmowych nagród Sezonu 8

## Przedmioty, sklep i profil gracza: UserTicket-EGOBg-a1c10p3
- plik gry: `UserTicket-EGOBg-a1c10p3.json`

152. [Przedmioty, sklep i profil gracza [80] — nazwa] N사 광장
   źródło: UserTicket-EGOBg-a1c10p3.json :: dataList[id=80].name
   limit: do 40 znaków
   EN: N Corp. Plaza
   PL: Plac Korporacji N
153. [Przedmioty, sklep i profil gracza [80] — opis] 시즌 8 푼크툼 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg-a1c10p3.json :: dataList[id=80].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Przedmioty, sklep i profil gracza [81] — nazwa] 자살 자판기
   źródło: UserTicket-EGOBg-a1c10p3.json :: dataList[id=81].name
   limit: do 40 znaków
   EN: Suicide Vending Machine
   PL: Samobójczy Automat
155. [Przedmioty, sklep i profil gracza [81] — opis] 시즌 8 푼크툼 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg-a1c10p3.json :: dataList[id=81].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Przedmioty, sklep i profil gracza [82] — nazwa] 시지프 백화점
   źródło: UserTicket-EGOBg-a1c10p3.json :: dataList[id=82].name
   limit: do 40 znaków
   EN: Grand Magasin Sisyphe
   PL: Grand Magasin Sisyphe
157. [Przedmioty, sklep i profil gracza [82] — opis] 시즌 8 푼크툼 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg-a1c10p3.json :: dataList[id=82].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-EGOBg-a1c7p3
- plik gry: `UserTicket-EGOBg-a1c7p3.json`

158. [Przedmioty, sklep i profil gracza [38] — nazwa — tylko EN w danych gry] La Manchaland of Nightmares
   źródło: UserTicket-EGOBg-a1c7p3.json :: dataList[id=38].name
   limit: do 40 znaków
   EN: La Manchaland of Nightmares
   PL: La Manchaland Koszmarów
159. [Przedmioty, sklep i profil gracza [38] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 70
   źródło: UserTicket-EGOBg-a1c7p3.json :: dataList[id=38].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie Darmowej Przepustki Sezonu 5
160. [Przedmioty, sklep i profil gracza [39] — nazwa — tylko EN w danych gry] A Lighthouse in the Ruins (the Cradle)
   źródło: UserTicket-EGOBg-a1c7p3.json :: dataList[id=39].name
   limit: do 60 znaków
   EN: A Lighthouse in the Ruins (the Cradle)
   PL: Latarnia w Ruinach (Kołyska)
161. [Przedmioty, sklep i profil gracza [39] — opis — tylko EN w danych gry] Obtained at Season 5 Limbus Pass Level 90
   źródło: UserTicket-EGOBg-a1c7p3.json :: dataList[id=39].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 5
162. [Przedmioty, sklep i profil gracza [40] — nazwa — tylko EN w danych gry] La Manchaland of Dreams
   źródło: UserTicket-EGOBg-a1c7p3.json :: dataList[id=40].name
   limit: do 40 znaków
   EN: La Manchaland of Dreams
   PL: La Manchaland Snów
163. [Przedmioty, sklep i profil gracza [40] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 110
   źródło: UserTicket-EGOBg-a1c7p3.json :: dataList[id=40].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie Darmowej Przepustki Sezonu 5

## Przedmioty, sklep i profil gracza: UserTicket-EGOBg-a1c8p1
- plik gry: `UserTicket-EGOBg-a1c8p1.json`

164. [Przedmioty, sklep i profil gracza [52] — nazwa — tylko EN w danych gry] Daguanyuan
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=52].name
   limit: do 40 znaków
   EN: Daguanyuan
   PL: Daguanyuan
165. [Przedmioty, sklep i profil gracza [52] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 70
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=52].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie Darmowej Przepustki Sezonu 6
166. [Przedmioty, sklep i profil gracza [53] — nazwa — tylko EN w danych gry] Kong Family Laboratory
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=53].name
   limit: do 40 znaków
   EN: Kong Family Laboratory
   PL: Laboratorium Rodziny Kong
167. [Przedmioty, sklep i profil gracza [53] — opis — tylko EN w danych gry] Obtained at Season 6 Limbus Pass Level 90
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=53].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 6
168. [Przedmioty, sklep i profil gracza [54] — nazwa — tylko EN w danych gry] Greeting Path to Tiekan Temple
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=54].name
   limit: do 50 znaków
   EN: Greeting Path to Tiekan Temple
   PL: Droga Powitań do Świątyni Tiekan
169. [Przedmioty, sklep i profil gracza [54] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 110
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=54].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie Darmowej Przepustki Sezonu 6
170. [Przedmioty, sklep i profil gracza [55] — nazwa — tylko EN w danych gry] L Corp. Central Command Team
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=55].name
   limit: do 40 znaków
   EN: L Corp. Central Command Team
   PL: Zespół Dowodzenia Centralnego L Corp.
171. [Przedmioty, sklep i profil gracza [55] — opis — tylko EN w danych gry] Obtained from the 6th Walpurgis Night event
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=55].desc
   limit: do 120 znaków
   EN: Obtained from the 6th Walpurgis Night event
   PL: Zdobyto z wydarzenia 6. Nocy Walpurgii
172. [Przedmioty, sklep i profil gracza [56] — nazwa — tylko EN w danych gry] Spring Cultivation
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=56].name
   limit: do 40 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
173. [Przedmioty, sklep i profil gracza [56] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=56].desc
   limit: do 120 znaków
   EN: Obtained from the 'Spring Cultivation' event
   PL: Zdobyto z wydarzenia „Wiosenny Szlif”
174. [Przedmioty, sklep i profil gracza [57] — nazwa — tylko EN w danych gry] Spring Cultivation - Special Ticket
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=57].name
   limit: do 50 znaków
   EN: Spring Cultivation - Special Ticket
   PL: Wiosenny Szlif — Specjalny Bilet
175. [Przedmioty, sklep i profil gracza [57] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=57].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Przedmioty, sklep i profil gracza [60] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=60].name
   limit: do 40 znaków
   EN: Pilgrimage of Compassion
   PL: Pielgrzymka Współczucia
177. [Przedmioty, sklep i profil gracza [60] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=60].desc
   limit: do 120 znaków
   EN: Obtained from the Pilgrimage of Compassion event
   PL: Zdobyto z wydarzenia Pielgrzymki Współczucia
178. [Przedmioty, sklep i profil gracza [61] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion - Special Ticket
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=61].name
   limit: do 60 znaków
   EN: Pilgrimage of Compassion - Special Ticket
   PL: Pielgrzymka Współczucia — Specjalny Bilet
179. [Przedmioty, sklep i profil gracza [61] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserTicket-EGOBg-a1c8p1.json :: dataList[id=61].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-EGOBg-a1c9p1
- plik gry: `UserTicket-EGOBg-a1c9p1.json`

180. [Przedmioty, sklep i profil gracza [64] — nazwa] 습격
   źródło: UserTicket-EGOBg-a1c9p1.json :: dataList[id=64].name
   limit: do 40 znaków
   EN: The Raid
   PL: Napad
181. [Przedmioty, sklep i profil gracza [64] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg-a1c9p1.json :: dataList[id=64].desc
   limit: do 120 znaków
   EN: Obtained at Season 7 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie darmowych nagród Sezonu 7
182. [Przedmioty, sklep i profil gracza [65] — nazwa] 거미집
   źródło: UserTicket-EGOBg-a1c9p1.json :: dataList[id=65].name
   limit: do 40 znaków
   EN: The House of Spiders
   PL: Dom Pająków
183. [Przedmioty, sklep i profil gracza [65] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg-a1c9p1.json :: dataList[id=65].desc
   limit: do 120 znaków
   EN: Obtained at Season 7 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 7
184. [Przedmioty, sklep i profil gracza [66] — nazwa] 밤하늘 영사기 아래
   źródło: UserTicket-EGOBg-a1c9p1.json :: dataList[id=66].name
   limit: do 50 znaków
   EN: Under the Projected Night Sky
   PL: Pod Rzutowanym Nocnym Niebem
185. [Przedmioty, sklep i profil gracza [66] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg-a1c9p1.json :: dataList[id=66].desc
   limit: do 120 znaków
   EN: Obtained at Season 7 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie darmowych nagród Sezonu 7

## Przedmioty, sklep i profil gracza: UserTicket-EGOBg
- plik gry: `UserTicket-EGOBg.json`

186. [Przedmioty, sklep i profil gracza [-1] — nazwa] 림버스 컴퍼니
   źródło: UserTicket-EGOBg.json :: dataList[id=-1].name
   limit: do 40 znaków
   EN: Limbus Company
   PL: Limbus Company
187. [Przedmioty, sklep i profil gracza [-1] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=-1].desc
   limit: do 120 znaków
   EN: Base
   PL: Domyślny
188. [Przedmioty, sklep i profil gracza [1] — nazwa] 죄악 : 분노
   źródło: UserTicket-EGOBg.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Sin: Wrath
   PL: Grzech: Gniew
189. [Przedmioty, sklep i profil gracza [1] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Przedmioty, sklep i profil gracza [2] — nazwa] 죄악 : 색욕
   źródło: UserTicket-EGOBg.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Sin: Lust
   PL: Grzech: Żądza
191. [Przedmioty, sklep i profil gracza [2] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=2].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Przedmioty, sklep i profil gracza [3] — nazwa] 죄악 : 나태
   źródło: UserTicket-EGOBg.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Sin: Sloth
   PL: Grzech: Lenistwo
193. [Przedmioty, sklep i profil gracza [3] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=3].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Przedmioty, sklep i profil gracza [4] — nazwa] 죄악 : 탐식
   źródło: UserTicket-EGOBg.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Sin: Gluttony
   PL: Grzech: Obżarstwo
195. [Przedmioty, sklep i profil gracza [4] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=4].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Przedmioty, sklep i profil gracza [5] — nazwa] 죄악 : 우울
   źródło: UserTicket-EGOBg.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Sin: Gloom
   PL: Grzech: Smutek
197. [Przedmioty, sklep i profil gracza [5] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=5].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Przedmioty, sklep i profil gracza [6] — nazwa] 죄악 : 오만
   źródło: UserTicket-EGOBg.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Sin: Pride
   PL: Grzech: Pycha
199. [Przedmioty, sklep i profil gracza [6] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=6].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Przedmioty, sklep i profil gracza [7] — nazwa] 죄악 : 질투
   źródło: UserTicket-EGOBg.json :: dataList[id=7].name
   limit: do 40 znaków
   EN: Sin: Envy
   PL: Grzech: Zazdrość
201. [Przedmioty, sklep i profil gracza [7] — opis] 기본
   źródło: UserTicket-EGOBg.json :: dataList[id=7].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Przedmioty, sklep i profil gracza [8] — nazwa] K사의 눈물
   źródło: UserTicket-EGOBg.json :: dataList[id=8].name
   limit: do 40 znaków
   EN: Tears of K Corp.
   PL: Łzy K Corp.
203. [Przedmioty, sklep i profil gracza [8] — opis] 시즌 2 레미니센스 무료 보상 40레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=8].desc
   limit: do 120 znaków
   EN: Obtained at Season 2 Free Pass Level 40
   PL: Zdobyto na 40. Poziomie darmowych nagród Sezonu 2: Reminiscence
204. [Przedmioty, sklep i profil gracza [9] — nazwa] 비 오는 날
   źródło: UserTicket-EGOBg.json :: dataList[id=9].name
   limit: do 40 znaków
   EN: Rainy Day
   PL: Deszczowy Dzień
205. [Przedmioty, sklep i profil gracza [9] — opis] 시즌 2 레미니센스 림버스 패스 보상 45레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=9].desc
   limit: do 120 znaków
   EN: Obtained at Season 2 Limbus Pass Level 45
   PL: Zdobyto na 45. Poziomie Limbus Pass Sezonu 2: Reminiscence
206. [Przedmioty, sklep i profil gracza [10] — nazwa] 동백
   źródło: UserTicket-EGOBg.json :: dataList[id=10].name
   limit: do 40 znaków
   EN: Dongbaek
   PL: Dongbaek
207. [Przedmioty, sklep i profil gracza [10] — opis] 시즌 2 레미니센스 무료 보상 55레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=10].desc
   limit: do 120 znaków
   EN: Obtained at Season 2 Free Pass Level 55
   PL: Zdobyto na 55. Poziomie darmowych nagród Sezonu 2: Reminiscence
208. [Przedmioty, sklep i profil gracza [11] — nazwa] 우.미.다
   źródło: UserTicket-EGOBg.json :: dataList[id=11].name
   limit: do 40 znaków
   EN: S.E.A
   PL: M.O.R.Z.E.
209. [Przedmioty, sklep i profil gracza [11] — opis] 우.미.다 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=11].desc
   limit: do 120 znaków
   EN: Obtained from the S.E.A event
   PL: Zdobyto z wydarzenia M.O.R.Z.E.
210. [Przedmioty, sklep i profil gracza [12] — nazwa] 2호선
   źródło: UserTicket-EGOBg.json :: dataList[id=12].name
   limit: do 40 znaków
   EN: Line 2
   PL: Linia 2
211. [Przedmioty, sklep i profil gracza [12] — opis] 순환 횟수 5 이상으로 2호선 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=12].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycle Counts
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej
212. [Przedmioty, sklep i profil gracza [13] — nazwa] 2호선 : 뫼비우스
   źródło: UserTicket-EGOBg.json :: dataList[id=13].name
   limit: do 40 znaków
   EN: Line 2 : Möbius
   PL: Linia 2 : Möbius
213. [Przedmioty, sklep i profil gracza [13] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 200턴 이하로 2호선 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=13].desc
   limit: do 160 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycle Counts and 200 or less Total Turns before Season 2: Reminiscence ends
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej i limitem 200 tur łącznych przed końcem Sezonu 2: Reminiscence
214. [Przedmioty, sklep i profil gracza [14] — nazwa] 2호선 : 뫼비우스 II
   źródło: UserTicket-EGOBg.json :: dataList[id=14].name
   limit: do 40 znaków
   EN: Line 2 : Möbius II
   PL: Linia 2 : Möbius II
215. [Przedmioty, sklep i profil gracza [14] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 150턴 이하로 거울굴절철도 2호선 클리어 시 획득 (단, 23/09/15 20:15 (KST) 이후에 새롭게 시작한 기록을 기준으로 함)
   źródło: UserTicket-EGOBg.json :: dataList[id=14].desc
   limit: do 240 znaków
   EN: Obtained by clearing Refraction Railway Line 2 with 5 or more Cycle Counts and under 150 Total Turns before Season 2: Reminiscence ends (Must be a record made after 2023.09.15 20:15(KST))
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 2 z liczbą Cykli 5 lub więcej i limitem 150 tur łącznych przed końcem Sezonu 2: Reminiscence (dotyczy rekordów rozpoczętych po 23/09/15 20:15 (KST))
216. [Przedmioty, sklep i profil gracza [15] — nazwa] 항구 컨테이너
   źródło: UserTicket-EGOBg.json :: dataList[id=15].name
   limit: do 40 znaków
   EN: Shipping Container
   PL: Kontener Portowy
217. [Przedmioty, sklep i profil gracza [15] — opis] 시즌 3 본 보야지 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=15].desc
   limit: do 120 znaków
   EN: Obtained at Season 3 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie darmowych nagród Sezonu 3: Bon Voyage
218. [Przedmioty, sklep i profil gracza [16] — nazwa] 폭풍우 속 선상
   źródło: UserTicket-EGOBg.json :: dataList[id=16].name
   limit: do 40 znaków
   EN: Amidst the Storm
   PL: Pośród Sztormu
219. [Przedmioty, sklep i profil gracza [16] — opis] 시즌 3 본 보야지 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=16].desc
   limit: do 120 znaków
   EN: Obtained at Season 3 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 3: Bon Voyage
220. [Przedmioty, sklep i profil gracza [17] — nazwa] 피쿼드타운
   źródło: UserTicket-EGOBg.json :: dataList[id=17].name
   limit: do 40 znaków
   EN: Pequod Town
   PL: Pequod Town
221. [Przedmioty, sklep i profil gracza [17] — opis] 시즌 3 본 보야지 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=17].desc
   limit: do 120 znaków
   EN: Obtained at Season 3 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie darmowych nagród Sezonu 3: Bon Voyage
222. [Przedmioty, sklep i profil gracza [18] — nazwa] 메리 크리스마스
   źródło: UserTicket-EGOBg.json :: dataList[id=18].name
   limit: do 40 znaków
   EN: Merry Christmas
   PL: Wesołych Świąt
223. [Przedmioty, sklep i profil gracza [18] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=18].desc
   limit: do 120 znaków
   EN: Obtained from the Miracle in District 20 event
   PL: Zdobyto z wydarzenia Cud w Dystrykcie 20
224. [Przedmioty, sklep i profil gracza [19] — nazwa] 메리 크리스마스 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=19].name
   limit: do 50 znaków
   EN: Merry Christmas - Special Ticket
   PL: Wesołych Świąt — Specjalny Bilet
225. [Przedmioty, sklep i profil gracza [19] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=19].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Przedmioty, sklep i profil gracza [20] — nazwa] 로보토미 지휘팀
   źródło: UserTicket-EGOBg.json :: dataList[id=20].name
   limit: do 40 znaków
   EN: L Corp. Control Team
   PL: Zespół Kontroli L Corp.
227. [Przedmioty, sklep i profil gracza [20] — opis] 제2회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=20].desc
   limit: do 120 znaków
   EN: Obtained from the 2nd Walpurgis Night event
   PL: Zdobyto z wydarzenia 2. Nocy Walpurgii
228. [Przedmioty, sklep i profil gracza [21] — nazwa] 3호선
   źródło: UserTicket-EGOBg.json :: dataList[id=21].name
   limit: do 40 znaków
   EN: Line 3
   PL: Linia 3
229. [Przedmioty, sklep i profil gracza [21] — opis] 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=21].desc
   limit: do 120 znaków
   EN: Obtained by clearing the Terminus of Refraction Railway Line 3
   PL: Zdobyto za ukończenie stacji końcowej Kolei Załamania — Linia 3
230. [Przedmioty, sklep i profil gracza [22] — nazwa] 3호선 : MirrorClock OrangeRoad
   źródło: UserTicket-EGOBg.json :: dataList[id=22].name
   limit: do 50 znaków
   EN: Line 3 : MirrorClock OrangeRoad
   PL: Linia 3 : MirrorClock OrangeRoad
231. [Przedmioty, sklep i profil gracza [22] — opis] 시즌 3 본 보야지 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=22].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Przedmioty, sklep i profil gracza [23] — nazwa] 육참골단
   źródło: UserTicket-EGOBg.json :: dataList[id=23].name
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Przedmioty, sklep i profil gracza [23] — opis] 육참골단 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=23].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Przedmioty, sklep i profil gracza [24] — nazwa] 육참골단 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=24].name
   limit: do 70 znaków
   EN: Yield My Flesh to Claim Their Bones - Special Ticket
   PL: Oddam Ciało, by Złamać Ich Kości — Specjalny Bilet
235. [Przedmioty, sklep i profil gracza [24] — opis] 육참골단 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=24].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Przedmioty, sklep i profil gracza [25] — nazwa] 1st Birthday
   źródło: UserTicket-EGOBg.json :: dataList[id=25].name
   limit: do 40 znaków
   EN: 1st Birthday
   PL: 1st Birthday
237. [Przedmioty, sklep i profil gracza [25] — opis] 1주년 기념 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=25].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Przedmioty, sklep i profil gracza [26] — nazwa] 폭풍의 언덕
   źródło: UserTicket-EGOBg.json :: dataList[id=26].name
   limit: do 40 znaków
   EN: Wuthering Heights
   PL: Wuthering Heights
239. [Przedmioty, sklep i profil gracza [26] — opis] 시즌 4 클리어 올 캐시 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=26].desc
   limit: do 120 znaków
   EN: Obtained at Season 4 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie darmowych nagród Sezonu 4: Clear All Cathy
240. [Przedmioty, sklep i profil gracza [27] — nazwa] 지하 실험실
   źródło: UserTicket-EGOBg.json :: dataList[id=27].name
   limit: do 40 znaków
   EN: Subterranean Laboratory
   PL: Podziemne Laboratorium
241. [Przedmioty, sklep i profil gracza [27] — opis] 시즌 4 클리어 올 캐시 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=27].desc
   limit: do 120 znaków
   EN: Obtained at Season 4 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 4: Clear All Cathy
242. [Przedmioty, sklep i profil gracza [28] — nazwa] 누군가 두드리는 유리창
   źródło: UserTicket-EGOBg.json :: dataList[id=28].name
   limit: do 40 znaków
   EN: Knocking on the Window
   PL: Ktoś Puka w Szybę
243. [Przedmioty, sklep i profil gracza [28] — opis] 시즌 4 클리어 올 캐시 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=28].desc
   limit: do 120 znaków
   EN: Obtained at Season 4 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie darmowych nagród Sezonu 4: Clear All Cathy
244. [Przedmioty, sklep i profil gracza [29] — nazwa] 라이브러리 오브 루이나
   źródło: UserTicket-EGOBg.json :: dataList[id=29].name
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Przedmioty, sklep i profil gracza [29] — opis] 라이브러리 오브 루이나 구매 특전 쿠폰 등록 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=29].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Przedmioty, sklep i profil gracza [30] — nazwa] 새벽 사무소
   źródło: UserTicket-EGOBg.json :: dataList[id=30].name
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Przedmioty, sklep i profil gracza [30] — opis] 제3회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=30].desc
   limit: do 120 znaków
   EN: Obtained from the 3rd Walpurgis Night event
   PL: Zdobyto z wydarzenia 3. Nocy Walpurgii
248. [Przedmioty, sklep i profil gracza [31] — nazwa] 시간살인시간
   źródło: UserTicket-EGOBg.json :: dataList[id=31].name
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Przedmioty, sklep i profil gracza [31] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=31].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Przedmioty, sklep i profil gracza [32] — nazwa] 시간살인시간 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=32].name
   limit: do 50 znaków
   EN: Timekilling Time - Special Ticket
   PL: Czas Zabijania Czasu — Specjalny Bilet
251. [Przedmioty, sklep i profil gracza [32] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=32].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Przedmioty, sklep i profil gracza [33] — nazwa] 4호선
   źródło: UserTicket-EGOBg.json :: dataList[id=33].name
   limit: do 40 znaków
   EN: Line 4
   PL: Linia 4
253. [Przedmioty, sklep i profil gracza [33] — opis] 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=33].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Przedmioty, sklep i profil gracza [34] — nazwa] 4호선 : Masquerade
   źródło: UserTicket-EGOBg.json :: dataList[id=34].name
   limit: do 40 znaków
   EN: Line 4 : Masquerade
   PL: Linia 4 : Masquerade
255. [Przedmioty, sklep i profil gracza [34] — opis] 시즌 4 클리어 올 캐시 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=34].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Przedmioty, sklep i profil gracza [35] — nazwa] 워프특급 살인사건
   źródło: UserTicket-EGOBg.json :: dataList[id=35].name
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Przedmioty, sklep i profil gracza [35] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=35].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Przedmioty, sklep i profil gracza [36] — nazwa] 워프특급 살인사건 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=36].name
   limit: do 60 znaków
   EN: Murder on the WARP Express - Special Ticket
   PL: Morderstwo w Ekspresie WARP — Specjalny Bilet
259. [Przedmioty, sklep i profil gracza [36] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=36].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Przedmioty, sklep i profil gracza [37] — nazwa] 로보토미 교육팀
   źródło: UserTicket-EGOBg.json :: dataList[id=37].name
   limit: do 40 znaków
   EN: L Corp. Training Team
   PL: Zespół Szkoleniowy L Corp.
261. [Przedmioty, sklep i profil gracza [37] — opis] 제4회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=37].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Przedmioty, sklep i profil gracza [41] — nazwa] 마침표 사무소
   źródło: UserTicket-EGOBg.json :: dataList[id=41].name
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Przedmioty, sklep i profil gracza [41] — opis] 제5회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=41].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Przedmioty, sklep i profil gracza [42] — nazwa] LCB 정기검진
   źródło: UserTicket-EGOBg.json :: dataList[id=42].name
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Przedmioty, sklep i profil gracza [42] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=42].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Przedmioty, sklep i profil gracza [43] — nazwa] LCB 정기검진 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=43].name
   limit: do 60 znaków
   EN: LCB Regular Check-up - Special Ticket
   PL: Okresowe Badania LCB — Specjalny Bilet
267. [Przedmioty, sklep i profil gracza [43] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=43].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Przedmioty, sklep i profil gracza [44] — nazwa] 5호선
   źródło: UserTicket-EGOBg.json :: dataList[id=44].name
   limit: do 40 znaków
   EN: Line 5
   PL: Linia 5
269. [Przedmioty, sklep i profil gracza [44] — opis] 거울굴절철도 5호선 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=44].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Przedmioty, sklep i profil gracza [45] — nazwa] 5호선 : Merry Go Round
   źródło: UserTicket-EGOBg.json :: dataList[id=45].name
   limit: do 40 znaków
   EN: Line 5: Merry Go Round
   PL: Linia 5: Merry Go Round
271. [Przedmioty, sklep i profil gracza [45] — opis] 시즌 5 오블리비언 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 5호선 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=45].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Przedmioty, sklep i profil gracza [48] — nazwa] 2nd Anniversary
   źródło: UserTicket-EGOBg.json :: dataList[id=48].name
   limit: do 40 znaków
   EN: 2nd Anniversary
   PL: 2nd Anniversary
273. [Przedmioty, sklep i profil gracza [48] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=48].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Przedmioty, sklep i profil gracza [49] — nazwa] 2nd Anniversary (Special)
   źródło: UserTicket-EGOBg.json :: dataList[id=49].name
   limit: do 40 znaków
   EN: 2nd Anniversary (Special)
   PL: 2nd Anniversary (Special)
275. [Przedmioty, sklep i profil gracza [49] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=49].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Przedmioty, sklep i profil gracza [46] — nazwa] 꿈결의 거울
   źródło: UserTicket-EGOBg.json :: dataList[id=46].name
   limit: do 40 znaków
   EN: Mirror of the Dreaming
   PL: Lustro Snu
277. [Przedmioty, sklep i profil gracza [46] — opis] 꿈결의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=46].desc
   limit: do 120 znaków
   EN: Obtained as a Mirror of the Dreaming Achievement Reward
   PL: Zdobyto jako nagroda osiągnięć Lustra Snu
278. [Przedmioty, sklep i profil gracza [47] — nazwa] 꿈결의 거울 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=47].name
   limit: do 60 znaków
   EN: Mirror of the Dreaming - Special Ticket
   PL: Lustro Snu — Specjalny Bilet
279. [Przedmioty, sklep i profil gracza [47] — opis] 꿈결의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=47].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Przedmioty, sklep i profil gracza [50] — nazwa] 심야청소
   źródło: UserTicket-EGOBg.json :: dataList[id=50].name
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Przedmioty, sklep i profil gracza [50] — opis] 심야청소 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=50].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Przedmioty, sklep i profil gracza [51] — nazwa] 심야청소 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=51].name
   limit: do 50 znaków
   EN: Nocturnal Sweeping - Special Ticket
   PL: Nocne Sprzątanie — Specjalny Bilet
283. [Przedmioty, sklep i profil gracza [51] — opis] 심야청소 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=51].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Przedmioty, sklep i profil gracza [58] — nazwa] 영생의 거울
   źródło: UserTicket-EGOBg.json :: dataList[id=58].name
   limit: do 40 znaków
   EN: Mirror of Immortality
   PL: Lustro Nieśmiertelności
285. [Przedmioty, sklep i profil gracza [58] — opis] 영생의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=58].desc
   limit: do 120 znaków
   EN: Obtained as a Mirror of Immortality Achievement Reward
   PL: Zdobyto jako nagroda osiągnięć Lustra Nieśmiertelności
286. [Przedmioty, sklep i profil gracza [59] — nazwa] 영생의 거울 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=59].name
   limit: do 60 znaków
   EN: Mirror of Immortality - Special Ticket
   PL: Lustro Nieśmiertelności — Specjalny Bilet
287. [Przedmioty, sklep i profil gracza [59] — opis] 영생의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=59].desc
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Przedmioty, sklep i profil gracza [38] — nazwa] 악몽의 라만차랜드
   źródło: UserTicket-EGOBg.json :: dataList[id=38].name
   limit: do 40 znaków
   EN: La Manchaland of Nightmares
   PL: La Manchaland Koszmarów
289. [Przedmioty, sklep i profil gracza [38] — opis] 시즌 5 오블리비언 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=38].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie darmowych nagród Sezonu 5: Oblivion
290. [Przedmioty, sklep i profil gracza [39] — nazwa] 유적 어딘가의 등대 (요람)
   źródło: UserTicket-EGOBg.json :: dataList[id=39].name
   limit: do 60 znaków
   EN: A Lighthouse in the Ruins (the Cradle)
   PL: Latarnia w Ruinach (Kołyska)
291. [Przedmioty, sklep i profil gracza [39] — opis] 시즌 5 오블리비언 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=39].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 5: Oblivion
292. [Przedmioty, sklep i profil gracza [40] — nazwa] 꿈의 라만차랜드
   źródło: UserTicket-EGOBg.json :: dataList[id=40].name
   limit: do 40 znaków
   EN: La Manchaland of Dreams
   PL: La Manchaland Snów
293. [Przedmioty, sklep i profil gracza [40] — opis] 시즌 5 오블리비언 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=40].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie darmowych nagród Sezonu 5: Oblivion
294. [Przedmioty, sklep i profil gracza [52] — nazwa] 대관원
   źródło: UserTicket-EGOBg.json :: dataList[id=52].name
   limit: do 40 znaków
   EN: Daguanyuan
   PL: Daguanyuan
295. [Przedmioty, sklep i profil gracza [52] — opis] 시즌 6 장화인 무료 보상 70레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=52].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Free Pass Level 70
   PL: Zdobyto na 70. Poziomie darmowych nagród Sezonu 6: Zàng Huā Yín
296. [Przedmioty, sklep i profil gracza [53] — nazwa] 공가의 연구소
   źródło: UserTicket-EGOBg.json :: dataList[id=53].name
   limit: do 40 znaków
   EN: Kong Family Laboratory
   PL: Laboratorium Rodziny Kong
297. [Przedmioty, sklep i profil gracza [53] — opis] 시즌 6 장화인 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=53].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Limbus Pass Level 90
   PL: Zdobyto na 90. Poziomie Limbus Pass Sezonu 6: Zàng Huā Yín
298. [Przedmioty, sklep i profil gracza [54] — nazwa] 철함사로 문안인사 가는 길
   źródło: UserTicket-EGOBg.json :: dataList[id=54].name
   limit: do 50 znaków
   EN: Greeting Path to Tiekan Temple
   PL: Droga Powitań do Świątyni Tiekan
299. [Przedmioty, sklep i profil gracza [54] — opis] 시즌 6 장화인 무료 보상 110레벨에 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=54].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Free Pass Level 110
   PL: Zdobyto na 110. Poziomie darmowych nagród Sezonu 6: Zàng Huā Yín
300. [Przedmioty, sklep i profil gracza [55] — nazwa] 로보토미 중앙본부팀
   źródło: UserTicket-EGOBg.json :: dataList[id=55].name
   limit: do 40 znaków
   EN: L Corp. Central Command Team
   PL: Zespół Dowodzenia Centralnego L Corp.
301. [Przedmioty, sklep i profil gracza [55] — opis] 제6회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=55].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Przedmioty, sklep i profil gracza [56] — nazwa] 절차탁춘
   źródło: UserTicket-EGOBg.json :: dataList[id=56].name
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Przedmioty, sklep i profil gracza [56] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=56].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Przedmioty, sklep i profil gracza [57] — nazwa] 절차탁춘 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=57].name
   limit: do 50 znaków
   EN: Spring Cultivation - Special Ticket
   PL: Wiosenny Szlif — Specjalny Bilet
305. [Przedmioty, sklep i profil gracza [57] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=57].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Przedmioty, sklep i profil gracza [60] — nazwa] 선의의 순례
   źródło: UserTicket-EGOBg.json :: dataList[id=60].name
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Przedmioty, sklep i profil gracza [60] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=60].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Przedmioty, sklep i profil gracza [61] — nazwa] 선의의 순례 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=61].name
   limit: do 60 znaków
   EN: Pilgrimage of Compassion - Special Ticket
   PL: Pielgrzymka Współczucia — Specjalny Bilet
309. [Przedmioty, sklep i profil gracza [61] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=61].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Przedmioty, sklep i profil gracza [62] — nazwa] 어느 도서관의 일반적인 초대
   źródło: UserTicket-EGOBg.json :: dataList[id=62].name
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Przedmioty, sklep i profil gracza [62] — opis] 제7회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=62].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Przedmioty, sklep i profil gracza [63] — nazwa] 1호선 BokGak : Madness
   źródło: UserTicket-EGOBg.json :: dataList[id=63].name
   limit: do 40 znaków
   EN: Line 1 BokGak : Madness
   PL: Linia 1 BokGak : Madness
313. [Przedmioty, sklep i profil gracza [63] — opis] 거울굴절철도 1호선 BokGak 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=63].desc
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 1 BokGak
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 1 BokGak
314. [Przedmioty, sklep i profil gracza [67] — nazwa] 3rd Anniversary
   źródło: UserTicket-EGOBg.json :: dataList[id=67].name
   limit: do 40 znaków
   EN: 3rd Anniversary
   PL: 3rd Anniversary
315. [Przedmioty, sklep i profil gracza [67] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=67].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Przedmioty, sklep i profil gracza [68] — nazwa] 3rd Anniversary (Special)
   źródło: UserTicket-EGOBg.json :: dataList[id=68].name
   limit: do 40 znaków
   EN: 3rd Anniversary (Special)
   PL: 3rd Anniversary (Special)
317. [Przedmioty, sklep i profil gracza [68] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=68].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Przedmioty, sklep i profil gracza [69] — nazwa] 로보토미 복지팀
   źródło: UserTicket-EGOBg.json :: dataList[id=69].name
   limit: do 40 znaków
   EN: L Corp. Welfare Team
   PL: Zespół Dobrobytu L Corp.
319. [Przedmioty, sklep i profil gracza [69] — opis] 제8회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=69].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Przedmioty, sklep i profil gracza [70] — nazwa] 이름과 거미의 거울
   źródło: UserTicket-EGOBg.json :: dataList[id=70].name
   limit: do 40 znaków
   EN: Mirror of Names and Spiders
   PL: Lustro Imion i Pająków
321. [Przedmioty, sklep i profil gracza [70] — opis] 이름과 거미의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=70].desc
   limit: do 120 znaków
   EN: Obtained as a Mirror of Names and Spiders Achievement Reward
   PL: Zdobyto jako nagroda osiągnięć Lustra Imion i Pająków
322. [Przedmioty, sklep i profil gracza [71] — nazwa] 이름과 거미의 거울 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=71].name
   limit: do 60 znaków
   EN: Mirror of Names and Spiders - Special Ticket
   PL: Lustro Imion i Pająków — Specjalny Bilet
323. [Przedmioty, sklep i profil gracza [71] — opis] 이름과 거미의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=71].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Przedmioty, sklep i profil gracza [72] — nazwa] 타래 엮기
   źródło: UserTicket-EGOBg.json :: dataList[id=72].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Przedmioty, sklep i profil gracza [72] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=72].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Przedmioty, sklep i profil gracza [73] — nazwa] 타래 엮기 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=73].name
   limit: do 50 znaków
   EN: Twining Threads - Special Ticket
   PL: Splatanie Pasm — Specjalny Bilet
327. [Przedmioty, sklep i profil gracza [73] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=73].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Przedmioty, sklep i profil gracza [74] — nazwa] 6호선
   źródło: UserTicket-EGOBg.json :: dataList[id=74].name
   limit: do 40 znaków
   EN: Line 6
   PL: Linia 6
329. [Przedmioty, sklep i profil gracza [74] — opis] 거울굴절철도 6호선 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=74].desc
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Przedmioty, sklep i profil gracza [75] — nazwa] 6호선 : Maru no Uchi no Sanzu no Kawa
   źródło: UserTicket-EGOBg.json :: dataList[id=75].name
   limit: do 60 znaków
   EN: Line 6: Maru no Uchi no Sanzu no Kawa
   PL: Linia 6: Maru no Uchi no Sanzu no Kawa
331. [Przedmioty, sklep i profil gracza [75] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 기간 내에 누적 턴 수 111턴 이하로 거울굴절철도 6호선 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=75].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Przedmioty, sklep i profil gracza [76] — nazwa] 경험기억
   źródło: UserTicket-EGOBg.json :: dataList[id=76].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Przedmioty, sklep i profil gracza [76] — opis] 경험기억 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=76].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Przedmioty, sklep i profil gracza [77] — nazwa] 경험기억 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=77].name
   limit: do 50 znaków
   EN: Mnestic Experience - Special Ticket
   PL: Pamięć Doświadczenia — Specjalny Bilet
335. [Przedmioty, sklep i profil gracza [77] — opis] 경험기억 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=77].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Przedmioty, sklep i profil gracza [78] — nazwa] 새벽녘의 해결사
   źródło: UserTicket-EGOBg.json :: dataList[id=78].name
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Przedmioty, sklep i profil gracza [78] — opis] 제9회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=78].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Przedmioty, sklep i profil gracza [79] — nazwa] 2호선 BokGak : Möbius
   źródło: UserTicket-EGOBg.json :: dataList[id=79].name
   limit: do 40 znaków
   EN: Line 2 BokGak : Möbius
   PL: Linia 2 BokGak : Möbius
339. [Przedmioty, sklep i profil gracza [79] — opis] 거울굴절철도 2호선 BokGak 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=79].desc
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 2 BokGak
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 2 BokGak
340. [Przedmioty, sklep i profil gracza [83] — nazwa] 삽시호
   źródło: UserTicket-EGOBg.json :: dataList[id=83].name
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Przedmioty, sklep i profil gracza [83] — opis] 사영전투][투전영사 - 삽시호 Hard 난이도 클리어 시 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=83].desc
   limit: do 120 znaków
   EN: Obtained by clearing Reflectrial][lairtcelfeR - Chachihu on Hard Difficulty
   PL: Zdobyto za ukończenie Reflectrial][lairtcelfeR — Chachihu na poziomie trudności Hard
342. [Przedmioty, sklep i profil gracza [84] — nazwa] 시지프의 거울
   źródło: UserTicket-EGOBg.json :: dataList[id=84].name
   limit: do 40 znaków
   EN: Mirror of Sisyphe
   PL: Lustro Sisyphe
343. [Przedmioty, sklep i profil gracza [84] — opis] 시지프의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=84].desc
   limit: do 120 znaków
   EN: Obtained as a Mirror of Sisyphe Achievement Reward
   PL: Zdobyto jako nagroda osiągnięć Lustra Sisyphe
344. [Przedmioty, sklep i profil gracza [85] — nazwa] 시지프의 거울 - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=85].name
   limit: do 50 znaków
   EN: Mirror of Sisyphe - Special Ticket
   PL: Lustro Sisyphe — Specjalny Bilet
345. [Przedmioty, sklep i profil gracza [85] — opis] 시지프의 거울 업적 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=85].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Przedmioty, sklep i profil gracza [86] — nazwa] 쐐기 사무소
   źródło: UserTicket-EGOBg.json :: dataList[id=86].name
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Przedmioty, sklep i profil gracza [86] — opis] 제10회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=86].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Przedmioty, sklep i profil gracza [87] — nazwa] 도상구축 Beta
   źródło: UserTicket-EGOBg.json :: dataList[id=87].name
   limit: do 40 znaków
   EN: Schemacraft Beta
   PL: Konstrukcja Schematów Beta
349. [Przedmioty, sklep i profil gracza [87] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=87].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Przedmioty, sklep i profil gracza [88] — nazwa] 도상구축 Beta - 특별 티켓
   źródło: UserTicket-EGOBg.json :: dataList[id=88].name
   limit: do 50 znaków
   EN: Schemacraft Beta - Special Banner
   PL: Konstrukcja Schematów Beta — Specjalny Bilet
351. [Przedmioty, sklep i profil gracza [88] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserTicket-EGOBg.json :: dataList[id=88].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-L-a1c10p1
- plik gry: `UserTicket-L-a1c10p1.json`

352. [Przedmioty, sklep i profil gracza [80] — nazwa] ???
   źródło: UserTicket-L-a1c10p1.json :: dataList[id=80].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Przedmioty, sklep i profil gracza [80] — opis] 시즌 8 푼크툼 무료 보상 70레벨에 획득
   źródło: UserTicket-L-a1c10p1.json :: dataList[id=80].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Przedmioty, sklep i profil gracza [81] — nazwa] ???
   źródło: UserTicket-L-a1c10p1.json :: dataList[id=81].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Przedmioty, sklep i profil gracza [81] — opis] 시즌 8 푼크툼 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L-a1c10p1.json :: dataList[id=81].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Przedmioty, sklep i profil gracza [82] — nazwa] ???
   źródło: UserTicket-L-a1c10p1.json :: dataList[id=82].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Przedmioty, sklep i profil gracza [82] — opis] 시즌 8 푼크툼 무료 보상 110레벨에 획득
   źródło: UserTicket-L-a1c10p1.json :: dataList[id=82].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-L-a1c10p3
- plik gry: `UserTicket-L-a1c10p3.json`

358. [Przedmioty, sklep i profil gracza [80] — nazwa] N사 광장
   źródło: UserTicket-L-a1c10p3.json :: dataList[id=80].name
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Przedmioty, sklep i profil gracza [80] — opis] 시즌 8 푼크툼 무료 보상 70레벨에 획득
   źródło: UserTicket-L-a1c10p3.json :: dataList[id=80].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Przedmioty, sklep i profil gracza [81] — nazwa] 자살 자판기
   źródło: UserTicket-L-a1c10p3.json :: dataList[id=81].name
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Przedmioty, sklep i profil gracza [81] — opis] 시즌 8 푼크툼 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L-a1c10p3.json :: dataList[id=81].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Przedmioty, sklep i profil gracza [82] — nazwa] 시지프 백화점
   źródło: UserTicket-L-a1c10p3.json :: dataList[id=82].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Przedmioty, sklep i profil gracza [82] — opis] 시즌 8 푼크툼 무료 보상 110레벨에 획득
   źródło: UserTicket-L-a1c10p3.json :: dataList[id=82].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-L-a1c7p3
- plik gry: `UserTicket-L-a1c7p3.json`

364. [Przedmioty, sklep i profil gracza [38] — nazwa — tylko EN w danych gry] La Manchaland of Nightmares
   źródło: UserTicket-L-a1c7p3.json :: dataList[id=38].name
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Przedmioty, sklep i profil gracza [38] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 70
   źródło: UserTicket-L-a1c7p3.json :: dataList[id=38].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Przedmioty, sklep i profil gracza [39] — nazwa — tylko EN w danych gry] A Lighthouse in the Ruins (the Cradle)
   źródło: UserTicket-L-a1c7p3.json :: dataList[id=39].name
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Przedmioty, sklep i profil gracza [39] — opis — tylko EN w danych gry] Obtained at Season 5 Limbus Pass Level 90
   źródło: UserTicket-L-a1c7p3.json :: dataList[id=39].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Przedmioty, sklep i profil gracza [40] — nazwa — tylko EN w danych gry] La Manchaland of Dreams
   źródło: UserTicket-L-a1c7p3.json :: dataList[id=40].name
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Przedmioty, sklep i profil gracza [40] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 110
   źródło: UserTicket-L-a1c7p3.json :: dataList[id=40].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-L-a1c8p1
- plik gry: `UserTicket-L-a1c8p1.json`

370. [Przedmioty, sklep i profil gracza [52] — nazwa — tylko EN w danych gry] Daguanyuan
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=52].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Przedmioty, sklep i profil gracza [52] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 70
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=52].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Przedmioty, sklep i profil gracza [53] — nazwa — tylko EN w danych gry] Kong Family Laboratory
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=53].name
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Przedmioty, sklep i profil gracza [53] — opis — tylko EN w danych gry] Obtained at Season 6 Limbus Pass Level 90
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=53].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Przedmioty, sklep i profil gracza [54] — nazwa — tylko EN w danych gry] Greeting Path to Tiekan Temple
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=54].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Przedmioty, sklep i profil gracza [54] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 110
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=54].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Przedmioty, sklep i profil gracza [55] — nazwa — tylko EN w danych gry] L Corp. Central Command Team
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=55].name
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Przedmioty, sklep i profil gracza [55] — opis — tylko EN w danych gry] Obtained from the 6th Walpurgis Night event
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=55].desc
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Przedmioty, sklep i profil gracza [56] — nazwa — tylko EN w danych gry] Spring Cultivation
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=56].name
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Przedmioty, sklep i profil gracza [56] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=56].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Przedmioty, sklep i profil gracza [57] — nazwa — tylko EN w danych gry] Spring Cultivation - Special Ticket
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=57].name
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Przedmioty, sklep i profil gracza [57] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=57].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Przedmioty, sklep i profil gracza [60] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=60].name
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Przedmioty, sklep i profil gracza [60] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=60].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Przedmioty, sklep i profil gracza [61] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion - Special Ticket
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=61].name
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Przedmioty, sklep i profil gracza [61] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserTicket-L-a1c8p1.json :: dataList[id=61].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-L-a1c9p1
- plik gry: `UserTicket-L-a1c9p1.json`

386. [Przedmioty, sklep i profil gracza [64] — nazwa] 습격
   źródło: UserTicket-L-a1c9p1.json :: dataList[id=64].name
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Przedmioty, sklep i profil gracza [64] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 70레벨에 획득
   źródło: UserTicket-L-a1c9p1.json :: dataList[id=64].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Przedmioty, sklep i profil gracza [65] — nazwa] 거미집
   źródło: UserTicket-L-a1c9p1.json :: dataList[id=65].name
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Przedmioty, sklep i profil gracza [65] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L-a1c9p1.json :: dataList[id=65].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Przedmioty, sklep i profil gracza [66] — nazwa] 밤하늘 영사기 아래
   źródło: UserTicket-L-a1c9p1.json :: dataList[id=66].name
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Przedmioty, sklep i profil gracza [66] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 110레벨에 획득
   źródło: UserTicket-L-a1c9p1.json :: dataList[id=66].desc
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-L
- plik gry: `UserTicket-L.json`

392. [Przedmioty, sklep i profil gracza [-1] — nazwa] 림버스 컴퍼니
   źródło: UserTicket-L.json :: dataList[id=-1].name
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Przedmioty, sklep i profil gracza [-1] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=-1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Przedmioty, sklep i profil gracza [1] — nazwa] 죄악 : 분노
   źródło: UserTicket-L.json :: dataList[id=1].name
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Przedmioty, sklep i profil gracza [1] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Przedmioty, sklep i profil gracza [2] — nazwa] 죄악 : 색욕
   źródło: UserTicket-L.json :: dataList[id=2].name
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Przedmioty, sklep i profil gracza [2] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=2].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Przedmioty, sklep i profil gracza [3] — nazwa] 죄악 : 나태
   źródło: UserTicket-L.json :: dataList[id=3].name
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Przedmioty, sklep i profil gracza [3] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=3].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Przedmioty, sklep i profil gracza [4] — nazwa] 죄악 : 탐식
   źródło: UserTicket-L.json :: dataList[id=4].name
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Przedmioty, sklep i profil gracza [4] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=4].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Przedmioty, sklep i profil gracza [5] — nazwa] 죄악 : 우울
   źródło: UserTicket-L.json :: dataList[id=5].name
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Przedmioty, sklep i profil gracza [5] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=5].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Przedmioty, sklep i profil gracza [6] — nazwa] 죄악 : 오만
   źródło: UserTicket-L.json :: dataList[id=6].name
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Przedmioty, sklep i profil gracza [6] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=6].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Przedmioty, sklep i profil gracza [7] — nazwa] 죄악 : 질투
   źródło: UserTicket-L.json :: dataList[id=7].name
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Przedmioty, sklep i profil gracza [7] — opis] 기본
   źródło: UserTicket-L.json :: dataList[id=7].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Przedmioty, sklep i profil gracza [8] — nazwa] K사의 눈물
   źródło: UserTicket-L.json :: dataList[id=8].name
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Przedmioty, sklep i profil gracza [8] — opis] 시즌 2 레미니센스 무료 보상 40레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=8].desc
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Przedmioty, sklep i profil gracza [9] — nazwa] 비 오는 날
   źródło: UserTicket-L.json :: dataList[id=9].name
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Przedmioty, sklep i profil gracza [9] — opis] 시즌 2 레미니센스 림버스 패스 보상 45레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=9].desc
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Przedmioty, sklep i profil gracza [10] — nazwa] 동백
   źródło: UserTicket-L.json :: dataList[id=10].name
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Przedmioty, sklep i profil gracza [10] — opis] 시즌 2 레미니센스 무료 보상 55레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=10].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Przedmioty, sklep i profil gracza [11] — nazwa] 우.미.다
   źródło: UserTicket-L.json :: dataList[id=11].name
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Przedmioty, sklep i profil gracza [11] — opis] 우.미.다 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=11].desc
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Przedmioty, sklep i profil gracza [12] — nazwa] 2호선
   źródło: UserTicket-L.json :: dataList[id=12].name
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Przedmioty, sklep i profil gracza [12] — opis] 순환 횟수 5 이상으로 2호선 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=12].desc
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Przedmioty, sklep i profil gracza [13] — nazwa] 2호선 : 뫼비우스
   źródło: UserTicket-L.json :: dataList[id=13].name
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Przedmioty, sklep i profil gracza [13] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 200턴 이하로 2호선 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=13].desc
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Przedmioty, sklep i profil gracza [14] — nazwa] 2호선 : 뫼비우스 II
   źródło: UserTicket-L.json :: dataList[id=14].name
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Przedmioty, sklep i profil gracza [14] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 150턴 이하로 거울굴절철도 2호선 클리어 시 획득 (단, 23/09/15 20:15 (KST) 이후에 새롭게 시작한 기록을 기준으로 함)
   źródło: UserTicket-L.json :: dataList[id=14].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Przedmioty, sklep i profil gracza [15] — nazwa] 항구 컨테이너
   źródło: UserTicket-L.json :: dataList[id=15].name
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Przedmioty, sklep i profil gracza [15] — opis] 시즌 3 본 보야지 무료 보상 70레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=15].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Przedmioty, sklep i profil gracza [16] — nazwa] 폭풍우 속 선상
   źródło: UserTicket-L.json :: dataList[id=16].name
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Przedmioty, sklep i profil gracza [16] — opis] 시즌 3 본 보야지 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=16].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Przedmioty, sklep i profil gracza [17] — nazwa] 피쿼드타운
   źródło: UserTicket-L.json :: dataList[id=17].name
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Przedmioty, sklep i profil gracza [17] — opis] 시즌 3 본 보야지 무료 보상 110레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=17].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Przedmioty, sklep i profil gracza [18] — nazwa] 메리 크리스마스
   źródło: UserTicket-L.json :: dataList[id=18].name
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Przedmioty, sklep i profil gracza [18] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=18].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Przedmioty, sklep i profil gracza [19] — nazwa] 메리 크리스마스 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=19].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Przedmioty, sklep i profil gracza [19] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=19].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Przedmioty, sklep i profil gracza [20] — nazwa] 로보토미 지휘팀
   źródło: UserTicket-L.json :: dataList[id=20].name
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Przedmioty, sklep i profil gracza [20] — opis] 제2회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=20].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Przedmioty, sklep i profil gracza [21] — nazwa] 3호선
   źródło: UserTicket-L.json :: dataList[id=21].name
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Przedmioty, sklep i profil gracza [21] — opis] 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=21].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Przedmioty, sklep i profil gracza [22] — nazwa] 3호선 : MirrorClock OrangeRoad
   źródło: UserTicket-L.json :: dataList[id=22].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Przedmioty, sklep i profil gracza [22] — opis] 시즌 3 본 보야지 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=22].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Przedmioty, sklep i profil gracza [23] — nazwa] 육참골단
   źródło: UserTicket-L.json :: dataList[id=23].name
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Przedmioty, sklep i profil gracza [23] — opis] 육참골단 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=23].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Przedmioty, sklep i profil gracza [24] — nazwa] 육참골단 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=24].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Przedmioty, sklep i profil gracza [24] — opis] 육참골단 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=24].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Przedmioty, sklep i profil gracza [25] — nazwa] 1st Birthday
   źródło: UserTicket-L.json :: dataList[id=25].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Przedmioty, sklep i profil gracza [25] — opis] 1주년 기념 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=25].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Przedmioty, sklep i profil gracza [26] — nazwa] 폭풍의 언덕
   źródło: UserTicket-L.json :: dataList[id=26].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Przedmioty, sklep i profil gracza [26] — opis] 시즌 4 클리어 올 캐시 무료 보상 70레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=26].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Przedmioty, sklep i profil gracza [27] — nazwa] 지하 실험실
   źródło: UserTicket-L.json :: dataList[id=27].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Przedmioty, sklep i profil gracza [27] — opis] 시즌 4 클리어 올 캐시 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=27].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Przedmioty, sklep i profil gracza [28] — nazwa] 누군가 두드리는 유리창
   źródło: UserTicket-L.json :: dataList[id=28].name
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Przedmioty, sklep i profil gracza [28] — opis] 시즌 4 클리어 올 캐시 무료 보상 110레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=28].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Przedmioty, sklep i profil gracza [29] — nazwa] 라이브러리 오브 루이나
   źródło: UserTicket-L.json :: dataList[id=29].name
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Przedmioty, sklep i profil gracza [29] — opis] 라이브러리 오브 루이나 구매 특전 쿠폰 등록 시 획득
   źródło: UserTicket-L.json :: dataList[id=29].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Przedmioty, sklep i profil gracza [30] — nazwa] 새벽 사무소
   źródło: UserTicket-L.json :: dataList[id=30].name
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Przedmioty, sklep i profil gracza [30] — opis] 제3회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=30].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Przedmioty, sklep i profil gracza [31] — nazwa] 시간살인시간
   źródło: UserTicket-L.json :: dataList[id=31].name
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Przedmioty, sklep i profil gracza [31] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=31].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Przedmioty, sklep i profil gracza [32] — nazwa] 시간살인시간 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=32].name
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Przedmioty, sklep i profil gracza [32] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=32].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Przedmioty, sklep i profil gracza [33] — nazwa] 4호선
   źródło: UserTicket-L.json :: dataList[id=33].name
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Przedmioty, sklep i profil gracza [33] — opis] 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=33].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Przedmioty, sklep i profil gracza [34] — nazwa] 4호선 : Masquerade
   źródło: UserTicket-L.json :: dataList[id=34].name
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Przedmioty, sklep i profil gracza [34] — opis] 시즌 4 클리어 올 캐시 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=34].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Przedmioty, sklep i profil gracza [35] — nazwa] 워프특급 살인사건
   źródło: UserTicket-L.json :: dataList[id=35].name
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Przedmioty, sklep i profil gracza [35] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=35].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Przedmioty, sklep i profil gracza [36] — nazwa] 워프특급 살인사건 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=36].name
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Przedmioty, sklep i profil gracza [36] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=36].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Przedmioty, sklep i profil gracza [37] — nazwa] 로보토미 교육팀
   źródło: UserTicket-L.json :: dataList[id=37].name
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Przedmioty, sklep i profil gracza [37] — opis] 제4회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=37].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Przedmioty, sklep i profil gracza [41] — nazwa] 마침표 사무소
   źródło: UserTicket-L.json :: dataList[id=41].name
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Przedmioty, sklep i profil gracza [41] — opis] 제5회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=41].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Przedmioty, sklep i profil gracza [42] — nazwa] LCB 정기검진
   źródło: UserTicket-L.json :: dataList[id=42].name
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Przedmioty, sklep i profil gracza [42] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=42].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Przedmioty, sklep i profil gracza [43] — nazwa] LCB 정기검진 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=43].name
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Przedmioty, sklep i profil gracza [43] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=43].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Przedmioty, sklep i profil gracza [44] — nazwa] 5호선
   źródło: UserTicket-L.json :: dataList[id=44].name
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Przedmioty, sklep i profil gracza [44] — opis] 거울굴절철도 5호선 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=44].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Przedmioty, sklep i profil gracza [45] — nazwa] 5호선 : Merry Go Round
   źródło: UserTicket-L.json :: dataList[id=45].name
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Przedmioty, sklep i profil gracza [45] — opis] 시즌 5 오블리비언 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 5호선 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=45].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Przedmioty, sklep i profil gracza [48] — nazwa] 2nd Anniversary
   źródło: UserTicket-L.json :: dataList[id=48].name
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Przedmioty, sklep i profil gracza [48] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=48].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Przedmioty, sklep i profil gracza [49] — nazwa] 2nd Anniversary (Special)
   źródło: UserTicket-L.json :: dataList[id=49].name
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Przedmioty, sklep i profil gracza [49] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=49].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Przedmioty, sklep i profil gracza [46] — nazwa] 꿈결의 거울
   źródło: UserTicket-L.json :: dataList[id=46].name
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Przedmioty, sklep i profil gracza [46] — opis] 꿈결의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=46].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Przedmioty, sklep i profil gracza [47] — nazwa] 꿈결의 거울 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=47].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Przedmioty, sklep i profil gracza [47] — opis] 꿈결의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=47].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Przedmioty, sklep i profil gracza [50] — nazwa] 심야청소
   źródło: UserTicket-L.json :: dataList[id=50].name
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Przedmioty, sklep i profil gracza [50] — opis] 심야청소 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=50].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Przedmioty, sklep i profil gracza [51] — nazwa] 심야청소 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=51].name
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Przedmioty, sklep i profil gracza [51] — opis] 심야청소 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=51].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Przedmioty, sklep i profil gracza [58] — nazwa] 영생의 거울
   źródło: UserTicket-L.json :: dataList[id=58].name
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Przedmioty, sklep i profil gracza [58] — opis] 영생의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=58].desc
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Przedmioty, sklep i profil gracza [59] — nazwa] 영생의 거울 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=59].name
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Przedmioty, sklep i profil gracza [59] — opis] 영생의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=59].desc
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Przedmioty, sklep i profil gracza [38] — nazwa] 악몽의 라만차랜드
   źródło: UserTicket-L.json :: dataList[id=38].name
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Przedmioty, sklep i profil gracza [38] — opis] 시즌 5 오블리비언 무료 보상 70레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=38].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Przedmioty, sklep i profil gracza [39] — nazwa] 유적 어딘가의 등대 (요람)
   źródło: UserTicket-L.json :: dataList[id=39].name
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Przedmioty, sklep i profil gracza [39] — opis] 시즌 5 오블리비언 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=39].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Przedmioty, sklep i profil gracza [40] — nazwa] 꿈의 라만차랜드
   źródło: UserTicket-L.json :: dataList[id=40].name
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Przedmioty, sklep i profil gracza [40] — opis] 시즌 5 오블리비언 무료 보상 110레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=40].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Przedmioty, sklep i profil gracza [52] — nazwa] 대관원
   źródło: UserTicket-L.json :: dataList[id=52].name
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Przedmioty, sklep i profil gracza [52] — opis] 시즌 6 장화인 무료 보상 70레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=52].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Przedmioty, sklep i profil gracza [53] — nazwa] 공가의 연구소
   źródło: UserTicket-L.json :: dataList[id=53].name
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Przedmioty, sklep i profil gracza [53] — opis] 시즌 6 장화인 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=53].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Przedmioty, sklep i profil gracza [54] — nazwa] 철함사로 문안인사 가는 길
   źródło: UserTicket-L.json :: dataList[id=54].name
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Przedmioty, sklep i profil gracza [54] — opis] 시즌 6 장화인 무료 보상 110레벨에 획득
   źródło: UserTicket-L.json :: dataList[id=54].desc
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Przedmioty, sklep i profil gracza [55] — nazwa] 로보토미 중앙본부팀
   źródło: UserTicket-L.json :: dataList[id=55].name
   (powtórzenie elementu 300 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Przedmioty, sklep i profil gracza [55] — opis] 제6회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=55].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Przedmioty, sklep i profil gracza [56] — nazwa] 절차탁춘
   źródło: UserTicket-L.json :: dataList[id=56].name
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Przedmioty, sklep i profil gracza [56] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=56].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Przedmioty, sklep i profil gracza [57] — nazwa] 절차탁춘 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=57].name
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Przedmioty, sklep i profil gracza [57] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=57].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Przedmioty, sklep i profil gracza [60] — nazwa] 선의의 순례
   źródło: UserTicket-L.json :: dataList[id=60].name
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Przedmioty, sklep i profil gracza [60] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=60].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Przedmioty, sklep i profil gracza [61] — nazwa] 선의의 순례 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=61].name
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Przedmioty, sklep i profil gracza [61] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=61].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Przedmioty, sklep i profil gracza [62] — nazwa] 어느 도서관의 일반적인 초대
   źródło: UserTicket-L.json :: dataList[id=62].name
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Przedmioty, sklep i profil gracza [62] — opis] 제7회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=62].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Przedmioty, sklep i profil gracza [63] — nazwa] 1호선 BokGak : Madness
   źródło: UserTicket-L.json :: dataList[id=63].name
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Przedmioty, sklep i profil gracza [63] — opis] 거울굴절철도 1호선 BokGak 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=63].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Przedmioty, sklep i profil gracza [67] — nazwa] 3rd Anniversary
   źródło: UserTicket-L.json :: dataList[id=67].name
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Przedmioty, sklep i profil gracza [67] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=67].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Przedmioty, sklep i profil gracza [68] — nazwa] 3rd Anniversary (Special)
   źródło: UserTicket-L.json :: dataList[id=68].name
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Przedmioty, sklep i profil gracza [68] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=68].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Przedmioty, sklep i profil gracza [69] — nazwa] 로보토미 복지팀
   źródło: UserTicket-L.json :: dataList[id=69].name
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Przedmioty, sklep i profil gracza [69] — opis] 제8회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=69].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Przedmioty, sklep i profil gracza [70] — nazwa] 이름과 거미의 거울
   źródło: UserTicket-L.json :: dataList[id=70].name
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Przedmioty, sklep i profil gracza [70] — opis] 이름과 거미의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=70].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Przedmioty, sklep i profil gracza [71] — nazwa] 이름과 거미의 거울 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=71].name
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Przedmioty, sklep i profil gracza [71] — opis] 이름과 거미의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=71].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Przedmioty, sklep i profil gracza [72] — nazwa] 타래 엮기
   źródło: UserTicket-L.json :: dataList[id=72].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Przedmioty, sklep i profil gracza [72] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=72].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Przedmioty, sklep i profil gracza [73] — nazwa] 타래 엮기 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=73].name
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Przedmioty, sklep i profil gracza [73] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=73].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Przedmioty, sklep i profil gracza [74] — nazwa] 6호선
   źródło: UserTicket-L.json :: dataList[id=74].name
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Przedmioty, sklep i profil gracza [74] — opis] 거울굴절철도 6호선 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=74].desc
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Przedmioty, sklep i profil gracza [75] — nazwa] 6호선 : Maru no Uchi no Sanzu no Kawa
   źródło: UserTicket-L.json :: dataList[id=75].name
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Przedmioty, sklep i profil gracza [75] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 기간 내에 누적 턴 수 111턴 이하로 거울굴절철도 6호선 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=75].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Przedmioty, sklep i profil gracza [76] — nazwa] 경험기억
   źródło: UserTicket-L.json :: dataList[id=76].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Przedmioty, sklep i profil gracza [76] — opis] 경험기억 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=76].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Przedmioty, sklep i profil gracza [77] — nazwa] 경험기억 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=77].name
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Przedmioty, sklep i profil gracza [77] — opis] 경험기억 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=77].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Przedmioty, sklep i profil gracza [78] — nazwa] 새벽녘의 해결사
   źródło: UserTicket-L.json :: dataList[id=78].name
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Przedmioty, sklep i profil gracza [78] — opis] 제9회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=78].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Przedmioty, sklep i profil gracza [79] — nazwa] 2호선 BokGak : Möbius
   źródło: UserTicket-L.json :: dataList[id=79].name
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Przedmioty, sklep i profil gracza [79] — opis] 거울굴절철도 2호선 BokGak 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=79].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Przedmioty, sklep i profil gracza [83] — nazwa] 삽시호
   źródło: UserTicket-L.json :: dataList[id=83].name
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Przedmioty, sklep i profil gracza [83] — opis] 사영전투][투전영사 - 삽시호 Hard 난이도 클리어 시 획득
   źródło: UserTicket-L.json :: dataList[id=83].desc
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Przedmioty, sklep i profil gracza [84] — nazwa] 시지프의 거울
   źródło: UserTicket-L.json :: dataList[id=84].name
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Przedmioty, sklep i profil gracza [84] — opis] 시지프의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=84].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Przedmioty, sklep i profil gracza [85] — nazwa] 시지프의 거울 - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=85].name
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Przedmioty, sklep i profil gracza [85] — opis] 시지프의 거울 업적 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=85].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Przedmioty, sklep i profil gracza [86] — nazwa] 쐐기 사무소
   źródło: UserTicket-L.json :: dataList[id=86].name
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Przedmioty, sklep i profil gracza [86] — opis] 제10회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-L.json :: dataList[id=86].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Przedmioty, sklep i profil gracza [87] — nazwa] 도상구축 Beta
   źródło: UserTicket-L.json :: dataList[id=87].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Przedmioty, sklep i profil gracza [87] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=87].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Przedmioty, sklep i profil gracza [88] — nazwa] 도상구축 Beta - 특별 티켓
   źródło: UserTicket-L.json :: dataList[id=88].name
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Przedmioty, sklep i profil gracza [88] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserTicket-L.json :: dataList[id=88].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-R-a1c10p1
- plik gry: `UserTicket-R-a1c10p1.json`

558. [Przedmioty, sklep i profil gracza [80] — nazwa] ???
   źródło: UserTicket-R-a1c10p1.json :: dataList[id=80].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Przedmioty, sklep i profil gracza [80] — opis] 시즌 8 푼크툼 무료 보상 70레벨에 획득
   źródło: UserTicket-R-a1c10p1.json :: dataList[id=80].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Przedmioty, sklep i profil gracza [81] — nazwa] ???
   źródło: UserTicket-R-a1c10p1.json :: dataList[id=81].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Przedmioty, sklep i profil gracza [81] — opis] 시즌 8 푼크툼 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R-a1c10p1.json :: dataList[id=81].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Przedmioty, sklep i profil gracza [82] — nazwa] ???
   źródło: UserTicket-R-a1c10p1.json :: dataList[id=82].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Przedmioty, sklep i profil gracza [82] — opis] 시즌 8 푼크툼 무료 보상 110레벨에 획득
   źródło: UserTicket-R-a1c10p1.json :: dataList[id=82].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-R-a1c10p3
- plik gry: `UserTicket-R-a1c10p3.json`

564. [Przedmioty, sklep i profil gracza [80] — nazwa] N사 광장
   źródło: UserTicket-R-a1c10p3.json :: dataList[id=80].name
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Przedmioty, sklep i profil gracza [80] — opis] 시즌 8 푼크툼 무료 보상 70레벨에 획득
   źródło: UserTicket-R-a1c10p3.json :: dataList[id=80].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Przedmioty, sklep i profil gracza [81] — nazwa] 자살 자판기
   źródło: UserTicket-R-a1c10p3.json :: dataList[id=81].name
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Przedmioty, sklep i profil gracza [81] — opis] 시즌 8 푼크툼 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R-a1c10p3.json :: dataList[id=81].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Przedmioty, sklep i profil gracza [82] — nazwa] 시지프 백화점
   źródło: UserTicket-R-a1c10p3.json :: dataList[id=82].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Przedmioty, sklep i profil gracza [82] — opis] 시즌 8 푼크툼 무료 보상 110레벨에 획득
   źródło: UserTicket-R-a1c10p3.json :: dataList[id=82].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-R-a1c7p3
- plik gry: `UserTicket-R-a1c7p3.json`

570. [Przedmioty, sklep i profil gracza [38] — nazwa — tylko EN w danych gry] La Manchaland of Nightmares
   źródło: UserTicket-R-a1c7p3.json :: dataList[id=38].name
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Przedmioty, sklep i profil gracza [38] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 70
   źródło: UserTicket-R-a1c7p3.json :: dataList[id=38].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Przedmioty, sklep i profil gracza [39] — nazwa — tylko EN w danych gry] A Lighthouse in the Ruins (the Cradle)
   źródło: UserTicket-R-a1c7p3.json :: dataList[id=39].name
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Przedmioty, sklep i profil gracza [39] — opis — tylko EN w danych gry] Obtained at Season 5 Limbus Pass Level 90
   źródło: UserTicket-R-a1c7p3.json :: dataList[id=39].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Przedmioty, sklep i profil gracza [40] — nazwa — tylko EN w danych gry] La Manchaland of Dreams
   źródło: UserTicket-R-a1c7p3.json :: dataList[id=40].name
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Przedmioty, sklep i profil gracza [40] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 110
   źródło: UserTicket-R-a1c7p3.json :: dataList[id=40].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-R-a1c8p1
- plik gry: `UserTicket-R-a1c8p1.json`

576. [Przedmioty, sklep i profil gracza [52] — nazwa — tylko EN w danych gry] Daguanyuan
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=52].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Przedmioty, sklep i profil gracza [52] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 70
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=52].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Przedmioty, sklep i profil gracza [53] — nazwa — tylko EN w danych gry] Kong Family Laboratory
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=53].name
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Przedmioty, sklep i profil gracza [53] — opis — tylko EN w danych gry] Obtained at Season 6 Limbus Pass Level 90
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=53].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Przedmioty, sklep i profil gracza [54] — nazwa — tylko EN w danych gry] Greeting Path to Tiekan Temple
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=54].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Przedmioty, sklep i profil gracza [54] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 110
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=54].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Przedmioty, sklep i profil gracza [55] — nazwa — tylko EN w danych gry] L Corp. Central Command Team
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=55].name
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Przedmioty, sklep i profil gracza [55] — opis — tylko EN w danych gry] Obtained from the 6th Walpurgis Night event
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=55].desc
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Przedmioty, sklep i profil gracza [56] — nazwa — tylko EN w danych gry] Spring Cultivation
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=56].name
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Przedmioty, sklep i profil gracza [56] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=56].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Przedmioty, sklep i profil gracza [57] — nazwa — tylko EN w danych gry] Spring Cultivation - Special Ticket
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=57].name
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Przedmioty, sklep i profil gracza [57] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=57].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Przedmioty, sklep i profil gracza [60] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=60].name
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Przedmioty, sklep i profil gracza [60] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=60].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Przedmioty, sklep i profil gracza [61] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion - Special Ticket
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=61].name
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Przedmioty, sklep i profil gracza [61] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserTicket-R-a1c8p1.json :: dataList[id=61].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-R-a1c9p1
- plik gry: `UserTicket-R-a1c9p1.json`

592. [Przedmioty, sklep i profil gracza [64] — nazwa] 습격
   źródło: UserTicket-R-a1c9p1.json :: dataList[id=64].name
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Przedmioty, sklep i profil gracza [64] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 70레벨에 획득
   źródło: UserTicket-R-a1c9p1.json :: dataList[id=64].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Przedmioty, sklep i profil gracza [65] — nazwa] 거미집
   źródło: UserTicket-R-a1c9p1.json :: dataList[id=65].name
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Przedmioty, sklep i profil gracza [65] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R-a1c9p1.json :: dataList[id=65].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Przedmioty, sklep i profil gracza [66] — nazwa] 밤하늘 영사기 아래
   źródło: UserTicket-R-a1c9p1.json :: dataList[id=66].name
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Przedmioty, sklep i profil gracza [66] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 무료 보상 110레벨에 획득
   źródło: UserTicket-R-a1c9p1.json :: dataList[id=66].desc
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserTicket-R
- plik gry: `UserTicket-R.json`

598. [Przedmioty, sklep i profil gracza [-1] — nazwa] 림버스 컴퍼니
   źródło: UserTicket-R.json :: dataList[id=-1].name
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Przedmioty, sklep i profil gracza [-1] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=-1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Przedmioty, sklep i profil gracza [1] — nazwa] 죄악 : 분노
   źródło: UserTicket-R.json :: dataList[id=1].name
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Przedmioty, sklep i profil gracza [1] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Przedmioty, sklep i profil gracza [2] — nazwa] 죄악 : 색욕
   źródło: UserTicket-R.json :: dataList[id=2].name
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Przedmioty, sklep i profil gracza [2] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=2].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Przedmioty, sklep i profil gracza [3] — nazwa] 죄악 : 나태
   źródło: UserTicket-R.json :: dataList[id=3].name
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Przedmioty, sklep i profil gracza [3] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=3].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Przedmioty, sklep i profil gracza [4] — nazwa] 죄악 : 탐식
   źródło: UserTicket-R.json :: dataList[id=4].name
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Przedmioty, sklep i profil gracza [4] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=4].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Przedmioty, sklep i profil gracza [5] — nazwa] 죄악 : 우울
   źródło: UserTicket-R.json :: dataList[id=5].name
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Przedmioty, sklep i profil gracza [5] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=5].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Przedmioty, sklep i profil gracza [6] — nazwa] 죄악 : 오만
   źródło: UserTicket-R.json :: dataList[id=6].name
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Przedmioty, sklep i profil gracza [6] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=6].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Przedmioty, sklep i profil gracza [7] — nazwa] 죄악 : 질투
   źródło: UserTicket-R.json :: dataList[id=7].name
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Przedmioty, sklep i profil gracza [7] — opis] 기본
   źródło: UserTicket-R.json :: dataList[id=7].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Przedmioty, sklep i profil gracza [8] — nazwa] K사의 눈물
   źródło: UserTicket-R.json :: dataList[id=8].name
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Przedmioty, sklep i profil gracza [8] — opis] 시즌 2 레미니센스 무료 보상 40레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=8].desc
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Przedmioty, sklep i profil gracza [9] — nazwa] 비 오는 날
   źródło: UserTicket-R.json :: dataList[id=9].name
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Przedmioty, sklep i profil gracza [9] — opis] 시즌 2 레미니센스 림버스 패스 보상 45레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=9].desc
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Przedmioty, sklep i profil gracza [10] — nazwa] 동백
   źródło: UserTicket-R.json :: dataList[id=10].name
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Przedmioty, sklep i profil gracza [10] — opis] 시즌 2 레미니센스 무료 보상 55레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=10].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Przedmioty, sklep i profil gracza [11] — nazwa] 우.미.다
   źródło: UserTicket-R.json :: dataList[id=11].name
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Przedmioty, sklep i profil gracza [11] — opis] 우.미.다 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=11].desc
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Przedmioty, sklep i profil gracza [12] — nazwa] 2호선
   źródło: UserTicket-R.json :: dataList[id=12].name
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Przedmioty, sklep i profil gracza [12] — opis] 순환 횟수 5 이상으로 2호선 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=12].desc
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Przedmioty, sklep i profil gracza [13] — nazwa] 2호선 : 뫼비우스
   źródło: UserTicket-R.json :: dataList[id=13].name
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Przedmioty, sklep i profil gracza [13] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 200턴 이하로 2호선 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=13].desc
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Przedmioty, sklep i profil gracza [14] — nazwa] 2호선 : 뫼비우스 II
   źródło: UserTicket-R.json :: dataList[id=14].name
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Przedmioty, sklep i profil gracza [14] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 150턴 이하로 거울굴절철도 2호선 클리어 시 획득 (단, 23/09/15 20:15 (KST) 이후에 새롭게 시작한 기록을 기준으로 함)
   źródło: UserTicket-R.json :: dataList[id=14].desc
   limit: do 240 znaków
   EN: Obtained by clearing Refraction Railway Line 2 with 5 or more Cycle Count and under 150 Total Turns before Season 2: Reminiscence ends (Must be a record made after 2023.09.15 20:15(KST))
   PL: Zdobyto za ukończenie Kolei Załamania — Linia 2 z liczbą Cykli 5 lub więcej i limitem 150 tur łącznych przed końcem Sezonu 2: Reminiscence (dotyczy rekordów rozpoczętych po 23/09/15 20:15 (KST))
628. [Przedmioty, sklep i profil gracza [15] — nazwa] 항구 컨테이너
   źródło: UserTicket-R.json :: dataList[id=15].name
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Przedmioty, sklep i profil gracza [15] — opis] 시즌 3 본 보야지 무료 보상 70레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=15].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Przedmioty, sklep i profil gracza [16] — nazwa] 폭풍우 속 선상
   źródło: UserTicket-R.json :: dataList[id=16].name
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Przedmioty, sklep i profil gracza [16] — opis] 시즌 3 본 보야지 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=16].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Przedmioty, sklep i profil gracza [17] — nazwa] 피쿼드타운
   źródło: UserTicket-R.json :: dataList[id=17].name
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Przedmioty, sklep i profil gracza [17] — opis] 시즌 3 본 보야지 무료 보상 110레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=17].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Przedmioty, sklep i profil gracza [18] — nazwa] 메리 크리스마스
   źródło: UserTicket-R.json :: dataList[id=18].name
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Przedmioty, sklep i profil gracza [18] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=18].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Przedmioty, sklep i profil gracza [19] — nazwa] 메리 크리스마스 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=19].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Przedmioty, sklep i profil gracza [19] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=19].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Przedmioty, sklep i profil gracza [20] — nazwa] 로보토미 지휘팀
   źródło: UserTicket-R.json :: dataList[id=20].name
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Przedmioty, sklep i profil gracza [20] — opis] 제2회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=20].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Przedmioty, sklep i profil gracza [21] — nazwa] 3호선
   źródło: UserTicket-R.json :: dataList[id=21].name
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Przedmioty, sklep i profil gracza [21] — opis] 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=21].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Przedmioty, sklep i profil gracza [22] — nazwa] 3호선 : MirrorClock OrangeRoad
   źródło: UserTicket-R.json :: dataList[id=22].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Przedmioty, sklep i profil gracza [22] — opis] 시즌 3 본 보야지 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=22].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Przedmioty, sklep i profil gracza [23] — nazwa] 육참골단
   źródło: UserTicket-R.json :: dataList[id=23].name
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Przedmioty, sklep i profil gracza [23] — opis] 육참골단 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=23].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Przedmioty, sklep i profil gracza [24] — nazwa] 육참골단 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=24].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Przedmioty, sklep i profil gracza [24] — opis] 육참골단 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=24].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Przedmioty, sklep i profil gracza [25] — nazwa] 1st Birthday
   źródło: UserTicket-R.json :: dataList[id=25].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Przedmioty, sklep i profil gracza [25] — opis] 1주년 기념 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=25].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Przedmioty, sklep i profil gracza [26] — nazwa] 폭풍의 언덕
   źródło: UserTicket-R.json :: dataList[id=26].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Przedmioty, sklep i profil gracza [26] — opis] 시즌 4 클리어 올 캐시 무료 보상 70레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=26].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Przedmioty, sklep i profil gracza [27] — nazwa] 지하 실험실
   źródło: UserTicket-R.json :: dataList[id=27].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Przedmioty, sklep i profil gracza [27] — opis] 시즌 4 클리어 올 캐시 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=27].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Przedmioty, sklep i profil gracza [28] — nazwa] 누군가 두드리는 유리창
   źródło: UserTicket-R.json :: dataList[id=28].name
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Przedmioty, sklep i profil gracza [28] — opis] 시즌 4 클리어 올 캐시 무료 보상 110레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=28].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Przedmioty, sklep i profil gracza [29] — nazwa] 라이브러리 오브 루이나
   źródło: UserTicket-R.json :: dataList[id=29].name
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Przedmioty, sklep i profil gracza [29] — opis] 라이브러리 오브 루이나 구매 특전 쿠폰 등록 시 획득
   źródło: UserTicket-R.json :: dataList[id=29].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Przedmioty, sklep i profil gracza [30] — nazwa] 새벽 사무소
   źródło: UserTicket-R.json :: dataList[id=30].name
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Przedmioty, sklep i profil gracza [30] — opis] 제3회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=30].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Przedmioty, sklep i profil gracza [31] — nazwa] 시간살인시간
   źródło: UserTicket-R.json :: dataList[id=31].name
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Przedmioty, sklep i profil gracza [31] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=31].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Przedmioty, sklep i profil gracza [32] — nazwa] 시간살인시간 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=32].name
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Przedmioty, sklep i profil gracza [32] — opis] 시간살인시간 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=32].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Przedmioty, sklep i profil gracza [33] — nazwa] 4호선
   źródło: UserTicket-R.json :: dataList[id=33].name
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Przedmioty, sklep i profil gracza [33] — opis] 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=33].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Przedmioty, sklep i profil gracza [34] — nazwa] 4호선 : Masquerade
   źródło: UserTicket-R.json :: dataList[id=34].name
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Przedmioty, sklep i profil gracza [34] — opis] 시즌 4 클리어 올 캐시 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=34].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Przedmioty, sklep i profil gracza [35] — nazwa] 워프특급 살인사건
   źródło: UserTicket-R.json :: dataList[id=35].name
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Przedmioty, sklep i profil gracza [35] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=35].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Przedmioty, sklep i profil gracza [36] — nazwa] 워프특급 살인사건 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=36].name
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Przedmioty, sklep i profil gracza [36] — opis] 워프특급 살인사건 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=36].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Przedmioty, sklep i profil gracza [37] — nazwa] 로보토미 교육팀
   źródło: UserTicket-R.json :: dataList[id=37].name
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Przedmioty, sklep i profil gracza [37] — opis] 제4회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=37].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Przedmioty, sklep i profil gracza [41] — nazwa] 마침표 사무소
   źródło: UserTicket-R.json :: dataList[id=41].name
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Przedmioty, sklep i profil gracza [41] — opis] 제5회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=41].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Przedmioty, sklep i profil gracza [42] — nazwa] LCB 정기검진
   źródło: UserTicket-R.json :: dataList[id=42].name
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Przedmioty, sklep i profil gracza [42] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=42].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Przedmioty, sklep i profil gracza [43] — nazwa] LCB 정기검진 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=43].name
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Przedmioty, sklep i profil gracza [43] — opis] LCB 정기검진 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=43].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Przedmioty, sklep i profil gracza [44] — nazwa] 5호선
   źródło: UserTicket-R.json :: dataList[id=44].name
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Przedmioty, sklep i profil gracza [44] — opis] 거울굴절철도 5호선 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=44].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Przedmioty, sklep i profil gracza [45] — nazwa] 5호선 : Merry Go Round
   źródło: UserTicket-R.json :: dataList[id=45].name
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Przedmioty, sklep i profil gracza [45] — opis] 시즌 5 오블리비언 기간 내에 누적 턴 수 100턴 이하로 거울굴절철도 5호선 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=45].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Przedmioty, sklep i profil gracza [48] — nazwa] 2nd Anniversary
   źródło: UserTicket-R.json :: dataList[id=48].name
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Przedmioty, sklep i profil gracza [48] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=48].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Przedmioty, sklep i profil gracza [49] — nazwa] 2nd Anniversary (Special)
   źródło: UserTicket-R.json :: dataList[id=49].name
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Przedmioty, sklep i profil gracza [49] — opis] 2주년 기념 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=49].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Przedmioty, sklep i profil gracza [46] — nazwa] 꿈결의 거울
   źródło: UserTicket-R.json :: dataList[id=46].name
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Przedmioty, sklep i profil gracza [46] — opis] 꿈결의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=46].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Przedmioty, sklep i profil gracza [47] — nazwa] 꿈결의 거울 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=47].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Przedmioty, sklep i profil gracza [47] — opis] 꿈결의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=47].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Przedmioty, sklep i profil gracza [50] — nazwa] 심야청소
   źródło: UserTicket-R.json :: dataList[id=50].name
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Przedmioty, sklep i profil gracza [50] — opis] 심야청소 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=50].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Przedmioty, sklep i profil gracza [51] — nazwa] 심야청소 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=51].name
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Przedmioty, sklep i profil gracza [51] — opis] 심야청소 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=51].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Przedmioty, sklep i profil gracza [58] — nazwa] 영생의 거울
   źródło: UserTicket-R.json :: dataList[id=58].name
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Przedmioty, sklep i profil gracza [58] — opis] 영생의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=58].desc
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Przedmioty, sklep i profil gracza [59] — nazwa] 영생의 거울 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=59].name
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Przedmioty, sklep i profil gracza [59] — opis] 영생의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=59].desc
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Przedmioty, sklep i profil gracza [38] — nazwa] 악몽의 라만차랜드
   źródło: UserTicket-R.json :: dataList[id=38].name
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Przedmioty, sklep i profil gracza [38] — opis] 시즌 5 오블리비언 무료 보상 70레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=38].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Przedmioty, sklep i profil gracza [39] — nazwa] 유적 어딘가의 등대 (요람)
   źródło: UserTicket-R.json :: dataList[id=39].name
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Przedmioty, sklep i profil gracza [39] — opis] 시즌 5 오블리비언 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=39].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Przedmioty, sklep i profil gracza [40] — nazwa] 꿈의 라만차랜드
   źródło: UserTicket-R.json :: dataList[id=40].name
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Przedmioty, sklep i profil gracza [40] — opis] 시즌 5 오블리비언 무료 보상 110레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=40].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Przedmioty, sklep i profil gracza [52] — nazwa] 대관원
   źródło: UserTicket-R.json :: dataList[id=52].name
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Przedmioty, sklep i profil gracza [52] — opis] 시즌 6 장화인 무료 보상 70레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=52].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Przedmioty, sklep i profil gracza [53] — nazwa] 공가의 연구소
   źródło: UserTicket-R.json :: dataList[id=53].name
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Przedmioty, sklep i profil gracza [53] — opis] 시즌 6 장화인 림버스 패스 보상 90레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=53].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Przedmioty, sklep i profil gracza [54] — nazwa] 철함사로 문안인사 가는 길
   źródło: UserTicket-R.json :: dataList[id=54].name
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Przedmioty, sklep i profil gracza [54] — opis] 시즌 6 장화인 무료 보상 110레벨에 획득
   źródło: UserTicket-R.json :: dataList[id=54].desc
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Przedmioty, sklep i profil gracza [55] — nazwa] 로보토미 중앙본부팀
   źródło: UserTicket-R.json :: dataList[id=55].name
   (powtórzenie elementu 300 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Przedmioty, sklep i profil gracza [55] — opis] 제6회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=55].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Przedmioty, sklep i profil gracza [56] — nazwa] 절차탁춘
   źródło: UserTicket-R.json :: dataList[id=56].name
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Przedmioty, sklep i profil gracza [56] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=56].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Przedmioty, sklep i profil gracza [57] — nazwa] 절차탁춘 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=57].name
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Przedmioty, sklep i profil gracza [57] — opis] 절차탁춘 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=57].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Przedmioty, sklep i profil gracza [60] — nazwa] 선의의 순례
   źródło: UserTicket-R.json :: dataList[id=60].name
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Przedmioty, sklep i profil gracza [60] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=60].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Przedmioty, sklep i profil gracza [61] — nazwa] 선의의 순례 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=61].name
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Przedmioty, sklep i profil gracza [61] — opis] 선의의 순례 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=61].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Przedmioty, sklep i profil gracza [62] — nazwa] 어느 도서관의 일반적인 초대
   źródło: UserTicket-R.json :: dataList[id=62].name
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Przedmioty, sklep i profil gracza [62] — opis] 제7회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=62].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Przedmioty, sklep i profil gracza [63] — nazwa] 1호선 BokGak : Madness
   źródło: UserTicket-R.json :: dataList[id=63].name
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Przedmioty, sklep i profil gracza [63] — opis] 거울굴절철도 1호선 BokGak 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=63].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Przedmioty, sklep i profil gracza [67] — nazwa] 3rd Anniversary
   źródło: UserTicket-R.json :: dataList[id=67].name
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Przedmioty, sklep i profil gracza [67] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=67].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Przedmioty, sklep i profil gracza [68] — nazwa] 3rd Anniversary (Special)
   źródło: UserTicket-R.json :: dataList[id=68].name
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Przedmioty, sklep i profil gracza [68] — opis] 3주년 기념 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=68].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Przedmioty, sklep i profil gracza [69] — nazwa] 로보토미 복지팀
   źródło: UserTicket-R.json :: dataList[id=69].name
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Przedmioty, sklep i profil gracza [69] — opis] 제8회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=69].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Przedmioty, sklep i profil gracza [70] — nazwa] 이름과 거미의 거울
   źródło: UserTicket-R.json :: dataList[id=70].name
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Przedmioty, sklep i profil gracza [70] — opis] 이름과 거미의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=70].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Przedmioty, sklep i profil gracza [71] — nazwa] 이름과 거미의 거울 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=71].name
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Przedmioty, sklep i profil gracza [71] — opis] 이름과 거미의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=71].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Przedmioty, sklep i profil gracza [72] — nazwa] 타래 엮기
   źródło: UserTicket-R.json :: dataList[id=72].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Przedmioty, sklep i profil gracza [72] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=72].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Przedmioty, sklep i profil gracza [73] — nazwa] 타래 엮기 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=73].name
   (powtórzenie elementu 326 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Przedmioty, sklep i profil gracza [73] — opis] 타래 엮기 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=73].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Przedmioty, sklep i profil gracza [74] — nazwa] 6호선
   źródło: UserTicket-R.json :: dataList[id=74].name
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Przedmioty, sklep i profil gracza [74] — opis] 거울굴절철도 6호선 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=74].desc
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Przedmioty, sklep i profil gracza [75] — nazwa] 6호선 : Maru no Uchi no Sanzu no Kawa
   źródło: UserTicket-R.json :: dataList[id=75].name
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Przedmioty, sklep i profil gracza [75] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 기간 내에 누적 턴 수 111턴 이하로 거울굴절철도 6호선 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=75].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Przedmioty, sklep i profil gracza [76] — nazwa] 경험기억
   źródło: UserTicket-R.json :: dataList[id=76].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Przedmioty, sklep i profil gracza [76] — opis] 경험기억 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=76].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Przedmioty, sklep i profil gracza [77] — nazwa] 경험기억 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=77].name
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Przedmioty, sklep i profil gracza [77] — opis] 경험기억 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=77].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Przedmioty, sklep i profil gracza [78] — nazwa] 새벽녘의 해결사
   źródło: UserTicket-R.json :: dataList[id=78].name
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Przedmioty, sklep i profil gracza [78] — opis] 제9회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=78].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Przedmioty, sklep i profil gracza [79] — nazwa] 2호선 BokGak : Möbius
   źródło: UserTicket-R.json :: dataList[id=79].name
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Przedmioty, sklep i profil gracza [79] — opis] 거울굴절철도 2호선 BokGak 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=79].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Przedmioty, sklep i profil gracza [83] — nazwa] 삽시호
   źródło: UserTicket-R.json :: dataList[id=83].name
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Przedmioty, sklep i profil gracza [83] — opis] 사영전투][투전영사 - 삽시호 Hard 난이도 클리어 시 획득
   źródło: UserTicket-R.json :: dataList[id=83].desc
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Przedmioty, sklep i profil gracza [84] — nazwa] 시지프의 거울
   źródło: UserTicket-R.json :: dataList[id=84].name
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Przedmioty, sklep i profil gracza [84] — opis] 시지프의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=84].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Przedmioty, sklep i profil gracza [85] — nazwa] 시지프의 거울 - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=85].name
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Przedmioty, sklep i profil gracza [85] — opis] 시지프의 거울 업적 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=85].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Przedmioty, sklep i profil gracza [86] — nazwa] 쐐기 사무소
   źródło: UserTicket-R.json :: dataList[id=86].name
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Przedmioty, sklep i profil gracza [86] — opis] 제10회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserTicket-R.json :: dataList[id=86].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Przedmioty, sklep i profil gracza [87] — nazwa] 도상구축 Beta
   źródło: UserTicket-R.json :: dataList[id=87].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Przedmioty, sklep i profil gracza [87] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=87].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Przedmioty, sklep i profil gracza [88] — nazwa] 도상구축 Beta - 특별 티켓
   źródło: UserTicket-R.json :: dataList[id=88].name
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Przedmioty, sklep i profil gracza [88] — opis] 도상구축 Beta 패스 보상으로 획득
   źródło: UserTicket-R.json :: dataList[id=88].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: reward-popup-text-ProjectGS
- plik gry: `reward-popup-text-ProjectGS.json`

764. [Przedmioty, sklep i profil gracza [UNIT_LEVEL_UPGRADE] — warunek wzrostu poczytalności] {0}의 레벨 {1} 증가
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=UNIT_LEVEL_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} gained {1} Level(s)
   PL: Poziom {0} rośnie o {1}
765. [Przedmioty, sklep i profil gracza [UNIT_LEVEL_UPGRADE] — warunek spadku poczytalności] {0}의 레벨 {1} 감소
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=UNIT_LEVEL_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} lost {1} Level(s)
   PL: Poziom {0} spada o {1}
766. [Przedmioty, sklep i profil gracza [MAX_HP_ADD_UPGRADE] — warunek wzrostu poczytalności] {0}의 최대 체력 {1} 증가
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=MAX_HP_ADD_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} gained {1} max HP
   PL: Maks. PZ {0} rośnie o {1}
767. [Przedmioty, sklep i profil gracza [MAX_HP_ADD_UPGRADE] — warunek spadku poczytalności] {0}의 최대 체력 {1} 감소
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=MAX_HP_ADD_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} lost {1} max HP
   PL: Maks. PZ {0} spada o {1}
768. [Przedmioty, sklep i profil gracza [ATK_UPGRADE] — warunek wzrostu poczytalności] {0}의 공격 레벨 {1} 증가
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} gained {1} Offense Level(s)
   PL: Poziom Ataku {0} rośnie o {1}
769. [Przedmioty, sklep i profil gracza [ATK_UPGRADE] — warunek spadku poczytalności] {0}의 공격 레벨 {1} 감소
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} lost {1} Offense Level(s)
   PL: Poziom Ataku {0} spada o {1}
770. [Przedmioty, sklep i profil gracza [DEF_UPGRADE] — warunek wzrostu poczytalności] {0}의 방어 레벨 {1} 증가
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=DEF_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} gained {1} Defense Level(s)
   PL: Poziom Obrony {0} rośnie o {1}
771. [Przedmioty, sklep i profil gracza [DEF_UPGRADE] — warunek spadku poczytalności] {0}의 방어 레벨 {1} 감소
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=DEF_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} lost {1} Defense Level(s)
   PL: Poziom Obrony {0} spada o {1}
772. [Przedmioty, sklep i profil gracza [SPEED_RANGE_UPGRADE] — warunek wzrostu poczytalności] {0}의 속도 최솟값, 최댓값 {1} 증가
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=SPEED_RANGE_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Min & Max Speed +{1}
   PL: Min. i Maks. Szybkość {0} rosną o {1}
773. [Przedmioty, sklep i profil gracza [SPEED_RANGE_UPGRADE] — warunek spadku poczytalności] {0}의 속도 최솟값, 최댓값 {1} 감소
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=SPEED_RANGE_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Min & Max Speed -{1}
   PL: Min. i Maks. Szybkość {0} spadają o {1}
774. [Przedmioty, sklep i profil gracza [ATK_SLASH_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 참격 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_SLASH_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Slash Resist.: {1}
   PL: Odporność na Cięcie {0}: {1}
775. [Przedmioty, sklep i profil gracza [ATK_SLASH_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 참격 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_SLASH_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Slash Resist.: +{1}
   PL: Odporność na Cięcie {0}: +{1}
776. [Przedmioty, sklep i profil gracza [ATK_PENETRATE_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 관통 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_PENETRATE_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Pierce Resist.: {1}
   PL: Odporność na Kłucie {0}: {1}
777. [Przedmioty, sklep i profil gracza [ATK_PENETRATE_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 관통 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_PENETRATE_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Pierce Resist.: +{1}
   PL: Odporność na Kłucie {0}: +{1}
778. [Przedmioty, sklep i profil gracza [ATK_HIT_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 타격 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_HIT_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Blunt Resist.: {1}
   PL: Odporność na Uderzenie {0}: {1}
779. [Przedmioty, sklep i profil gracza [ATK_HIT_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 타격 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATK_HIT_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Blunt Resist.: +{1}
   PL: Odporność na Uderzenie {0}: +{1}
780. [Przedmioty, sklep i profil gracza [ATTRIBUTE_CRIMSON_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 분노 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_CRIMSON_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Wrath Resist.: {1}
   PL: Odporność na Gniew {0}: {1}
781. [Przedmioty, sklep i profil gracza [ATTRIBUTE_CRIMSON_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 분노 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_CRIMSON_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Wrath Resist.: +{1}
   PL: Odporność na Gniew {0}: +{1}
782. [Przedmioty, sklep i profil gracza [ATTRIBUTE_SCARLET_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 색욕 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_SCARLET_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Lust Resist.: {1}
   PL: Odporność na Żądzę {0}: {1}
783. [Przedmioty, sklep i profil gracza [ATTRIBUTE_SCARLET_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 색욕 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_SCARLET_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Lust Resist.: +{1}
   PL: Odporność na Żądzę {0}: +{1}
784. [Przedmioty, sklep i profil gracza [ATTRIBUTE_AMBER_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 나태 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_AMBER_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Sloth Resist.: {1}
   PL: Odporność na Lenistwo {0}: {1}
785. [Przedmioty, sklep i profil gracza [ATTRIBUTE_AMBER_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 나태 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_AMBER_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Sloth Resist.: +{1}
   PL: Odporność na Lenistwo {0}: +{1}
786. [Przedmioty, sklep i profil gracza [ATTRIBUTE_SHAMROCK_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 탐식 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_SHAMROCK_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Gluttony Resist.: {1}
   PL: Odporność na Obżarstwo {0}: {1}
787. [Przedmioty, sklep i profil gracza [ATTRIBUTE_SHAMROCK_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 탐식 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_SHAMROCK_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Gluttony Resist.: +{1}
   PL: Odporność na Obżarstwo {0}: +{1}
788. [Przedmioty, sklep i profil gracza [ATTRIBUTE_AZURE_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 우울 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_AZURE_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Gloom Resist.: {1}
   PL: Odporność na Smutek {0}: {1}
789. [Przedmioty, sklep i profil gracza [ATTRIBUTE_AZURE_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 우울 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_AZURE_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Gloom Resist.: +{1}
   PL: Odporność na Smutek {0}: +{1}
790. [Przedmioty, sklep i profil gracza [ATTRIBUTE_INDIGO_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 오만 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_INDIGO_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Pride Resist.: {1}
   PL: Odporność na Pychę {0}: {1}
791. [Przedmioty, sklep i profil gracza [ATTRIBUTE_INDIGO_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 오만 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_INDIGO_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Pride Resist.: +{1}
   PL: Odporność na Pychę {0}: +{1}
792. [Przedmioty, sklep i profil gracza [ATTRIBUTE_VIOLET_RESIST_UPGRADE] — warunek wzrostu poczytalności] {0}의 질투 내성 {1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_VIOLET_RESIST_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Envy Resist.: {1}
   PL: Odporność na Zazdrość {0}: {1}
793. [Przedmioty, sklep i profil gracza [ATTRIBUTE_VIOLET_RESIST_UPGRADE] — warunek spadku poczytalności] {0}의 질투 내성 +{1}
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ATTRIBUTE_VIOLET_RESIST_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s Envy Resist.: +{1}
   PL: Odporność na Zazdrość {0}: +{1}
794. [Przedmioty, sklep i profil gracza [ACQUIRE_SKILL] — warunek wzrostu poczytalności] {0}(이/가) [{1}] 스킬 습득
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ACQUIRE_SKILL].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} learned [{1}] Skill
   PL: {0} zdobywa [{1}] Umiejętność
795. [Przedmioty, sklep i profil gracza [ACQUIRE_SKILL] — warunek spadku poczytalności] {0}(이/가) [{1}] 스킬 상실
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ACQUIRE_SKILL].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} forgot [{1}] Skill
   PL: {0} traci [{1}] Umiejętność
796. [Przedmioty, sklep i profil gracza [SKILL_UPGRADE] — warunek wzrostu poczytalności] {0}의 [{1}] 스킬 강화
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=SKILL_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s [{1}] Skill improved!
   PL: [{1}] Umiejętność {0} wzmocniona!
797. [Przedmioty, sklep i profil gracza [SKILL_UPGRADE] — warunek spadku poczytalności] {0}의 [{1}] 스킬 약화
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=SKILL_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} weakened their [{1}] Skill
   PL: [{1}] Umiejętność {0} osłabiona
798. [Przedmioty, sklep i profil gracza [ACQUIRE_PASSIVE] — warunek wzrostu poczytalności] {0}(이/가) [{1}] 패시브 습득
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ACQUIRE_PASSIVE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} learned [{1}] Passive
   PL: {0} zdobywa [{1}] Pasywkę
799. [Przedmioty, sklep i profil gracza [ACQUIRE_PASSIVE] — warunek spadku poczytalności] {0}(이/가) [{1}] 패시브 상실
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=ACQUIRE_PASSIVE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} forgot [{1}] Passive
   PL: {0} traci [{1}] Pasywkę
800. [Przedmioty, sklep i profil gracza [PASSIVE_UPGRADE] — warunek wzrostu poczytalności] {0}의 [{1}] 패시브 강화
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=PASSIVE_UPGRADE].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}'s [{1}] Passive improved!
   PL: [{1}] Pasywka {0} wzmocniona!
801. [Przedmioty, sklep i profil gracza [PASSIVE_UPGRADE] — warunek spadku poczytalności] {0}의 [{1}] 패시브 약화
   źródło: reward-popup-text-ProjectGS.json :: dataList[id=PASSIVE_UPGRADE].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} weakened their [{1}] Passive
   PL: [{1}] Pasywka {0} osłabiona
