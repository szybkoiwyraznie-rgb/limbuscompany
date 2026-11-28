# Paczka AI P39 (Fala 2 · 2C) — Tabela modeli postaci oraz interfejs, zadania i przedmioty RPG Canto X (część 1/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P39_2c_modele_i_rpg_ui_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P39_2c_modele_i_rpg_ui_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tabela modeli postaci: ScenarioModelCodes-AutoCreated
- plik gry: `ScenarioModelCodes-AutoCreated.json`
- Uwaga: imiona używane w scenach fabularnych pokrywają się częściowo z `sceny.zip/mowcy-i-miejsca.md`; zachowaj identyczną pisownię imion i przydomków.

1. [Tabela modeli postaci [이상] — nazwa] 이상
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상].name
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang
2. [Tabela modeli postaci [이상] — przydomek / oznaczenie] 1번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상].nickName
   limit: do 40 znaków
   EN: Sinner #1
   PL: Grzesznik nr 1
3. [Tabela modeli postaci [파우스트] — nazwa] 파우스트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트].name
   limit: do 40 znaków
   EN: Faust
   PL: Faust
4. [Tabela modeli postaci [파우스트] — przydomek / oznaczenie] 2번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트].nickName
   limit: do 40 znaków
   EN: Sinner #2
   PL: Grzesznik nr 2
5. [Tabela modeli postaci [돈키호테] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테].name
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
6. [Tabela modeli postaci [돈키호테] — przydomek / oznaczenie] 3번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테].nickName
   limit: do 40 znaków
   EN: Sinner #3
   PL: Grzesznik nr 3
7. [Tabela modeli postaci [료슈] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈].name
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
8. [Tabela modeli postaci [료슈] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈].nickName
   limit: do 40 znaków
   EN: Sinner #4
   PL: Grzesznik nr 4
9. [Tabela modeli postaci [뫼르소] — nazwa] 뫼르소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소].name
   limit: do 40 znaków
   EN: Meursault
   PL: Meursault
10. [Tabela modeli postaci [뫼르소] — przydomek / oznaczenie] 5번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소].nickName
   limit: do 40 znaków
   EN: Sinner #5
   PL: Grzesznik nr 5
11. [Tabela modeli postaci [홍루] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루].name
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu
12. [Tabela modeli postaci [홍루] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루].nickName
   limit: do 40 znaków
   EN: Sinner #6
   PL: Grzesznik nr 6
13. [Tabela modeli postaci [히스클리프] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프].name
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
14. [Tabela modeli postaci [히스클리프] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프].nickName
   limit: do 40 znaków
   EN: Sinner #7
   PL: Grzesznik nr 7
15. [Tabela modeli postaci [이스마엘] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘].name
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael
16. [Tabela modeli postaci [이스마엘] — przydomek / oznaczenie] 8번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘].nickName
   limit: do 40 znaków
   EN: Sinner #8
   PL: Grzesznik nr 8
17. [Tabela modeli postaci [로쟈] — nazwa] 로쟈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈].name
   limit: do 40 znaków
   EN: Rodion
   PL: Rodion
18. [Tabela modeli postaci [로쟈] — przydomek / oznaczenie] 9번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈].nickName
   limit: do 40 znaków
   EN: Sinner #9
   PL: Grzesznik nr 9
19. [Tabela modeli postaci [싱클레어] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어].name
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair
20. [Tabela modeli postaci [싱클레어] — przydomek / oznaczenie] 11번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어].nickName
   limit: do 40 znaków
   EN: Sinner #11
   PL: Grzesznik nr 11
21. [Tabela modeli postaci [오티스] — nazwa] 오티스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스].name
   limit: do 40 znaków
   EN: Outis
   PL: Outis
22. [Tabela modeli postaci [오티스] — przydomek / oznaczenie] 12번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스].nickName
   limit: do 40 znaków
   EN: Sinner #12
   PL: Grzesznik nr 12
23. [Tabela modeli postaci [그레고르] — nazwa] 그레고르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르].name
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor
24. [Tabela modeli postaci [그레고르] — przydomek / oznaczenie] 13번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르].nickName
   limit: do 40 znaków
   EN: Sinner #13
   PL: Grzesznik nr 13
25. [Tabela modeli postaci [아야] — nazwa] 아야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아야].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Aya
26. [Tabela modeli postaci [유리] — nazwa] 유리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유리].name
   limit: do 40 znaków
   EN: Yuri
   PL: Yuri
27. [Tabela modeli postaci [홉킨스] — nazwa] 홉킨스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홉킨스].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Hopkins
28. [Tabela modeli postaci [G사 직원] — nazwa] G사 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=G사 직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik G Corp.
29. [Tabela modeli postaci [G사 직원] — przydomek / oznaczenie] G사 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=G사 직원].nickName
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Tabela modeli postaci [독백] — nazwa] 독백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=독백].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Monolog
31. [Tabela modeli postaci [베르길리우스] — nazwa] 베르길리우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스].name
   limit: do 40 znaków
   EN: Vergilius
   PL: Vergilius
32. [Tabela modeli postaci [베르길리우스] — przydomek / oznaczenie] 길잡이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스].nickName
   limit: do 40 znaków
   EN: Guide
   PL: Przewodnik
33. [Tabela modeli postaci [베르길리우스2] — nazwa] 베르길리우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스2].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Tabela modeli postaci [베르길리우스2] — przydomek / oznaczenie] 길잡이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스2].nickName
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Tabela modeli postaci [베르길리우스3] — nazwa] 베르길리우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스3].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Tabela modeli postaci [베르길리우스3] — przydomek / oznaczenie] 길잡이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스3].nickName
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Tabela modeli postaci [눈이붉은자] — nazwa] 눈이 붉은 자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=눈이붉은자].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ten o Czerwonych Oczach
38. [Tabela modeli postaci [눈이붉은자] — przydomek / oznaczenie] 눈이 붉은 자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=눈이붉은자].nickName
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Tabela modeli postaci [카론] — nazwa] 카론
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카론].name
   limit: do 40 znaków
   EN: Charon
   PL: Charon
40. [Tabela modeli postaci [카론] — przydomek / oznaczenie] 운전수
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카론].nickName
   limit: do 40 znaków
   EN: Bus Driver
   PL: Kierowca
41. [Tabela modeli postaci [단테] — nazwa] 단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테].name
   limit: do 40 znaków
   EN: Dante
   PL: Dante
42. [Tabela modeli postaci [단테] — przydomek / oznaczenie] 관리자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테].nickName
   limit: do 40 znaków
   EN: Manager
   PL: Zarządca
43. [Tabela modeli postaci [단테1] — nazwa] 단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테1].name
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Tabela modeli postaci [단테1] — przydomek / oznaczenie] 관리자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테1].nickName
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Tabela modeli postaci [단테2] — nazwa] 단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테2].name
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Tabela modeli postaci [단테2] — przydomek / oznaczenie] 관리자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테2].nickName
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Tabela modeli postaci [4구 불량배 1] — nazwa] 4구 불량배 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4구 불량배 1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Chuligan 1 z Dystryktu 4
48. [Tabela modeli postaci [4구 불량배 1] — przydomek / oznaczenie] 4구 불량배 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4구 불량배 1].nickName
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Tabela modeli postaci [4구 불량배 2] — nazwa] 4구 불량배 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4구 불량배 2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Chuligan 2 z Dystryktu 4
50. [Tabela modeli postaci [4구 불량배 2] — przydomek / oznaczenie] 4구 불량배 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4구 불량배 2].nickName
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Tabela modeli postaci [4구 불량배 3] — nazwa] 4구 불량배 3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4구 불량배 3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Chuligan 3 z Dystryktu 4
52. [Tabela modeli postaci [4구 불량배 3] — przydomek / oznaczenie] 4구 불량배 3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4구 불량배 3].nickName
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Tabela modeli postaci [석상머리] — nazwa] 석상머리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=석상머리].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kamienna Głowa
54. [Tabela modeli postaci [석상머리] — przydomek / oznaczenie] 로보토미 지부 생존자?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=석상머리].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ocalały z Oddziału L Corp.?
55. [Tabela modeli postaci [G사부장] — nazwa] G사부장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=G사부장].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dyrektor G Corp.
56. [Tabela modeli postaci [G사부장] — przydomek / oznaczenie] G사부장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=G사부장].nickName
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Tabela modeli postaci [화난패잔병] — nazwa] 화난패잔병
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=화난패잔병].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wściekły Rozbityk
58. [Tabela modeli postaci [화난패잔병] — przydomek / oznaczenie] 화난패잔병
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=화난패잔병].nickName
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Tabela modeli postaci [의아한패잔병] — nazwa] 의아한패잔병
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=의아한패잔병].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zdumiony Rozbityk
60. [Tabela modeli postaci [의아한패잔병] — przydomek / oznaczenie] 의아한패잔병
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=의아한패잔병].nickName
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Tabela modeli postaci [쓰러진아야] — nazwa] 쓰러진아야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쓰러진아야].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Powalona Aya
62. [Tabela modeli postaci [쓰러진아야] — przydomek / oznaczenie] 8급 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쓰러진아야].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Fikser 8. Klasy
63. [Tabela modeli postaci [백설공주그림자] — nazwa] 백설공주그림자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=백설공주그림자].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Cień Królewny Śnieżki
64. [Tabela modeli postaci [카지노경호원대장] — nazwa] 카지노경호원대장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카지노경호원대장].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Szef Ochrony Kasyna
65. [Tabela modeli postaci [카지노경호원대장] — przydomek / oznaczenie] 경호원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카지노경호원대장].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ochroniarz
66. [Tabela modeli postaci [각잡힌카지노경호원] — nazwa] 각잡힌카지노경호원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각잡힌카지노경호원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pewny Siebie Ochroniarz Kasyna
67. [Tabela modeli postaci [각잡힌카지노경호원] — przydomek / oznaczenie] 경호원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각잡힌카지노경호원].nickName
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Tabela modeli postaci [세보이고싶었던콩콩파조직원] — nazwa] 세보이고싶었던콩콩파조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=세보이고싶었던콩콩파조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Kongkong Chcący Być Seboyem
69. [Tabela modeli postaci [세보이고싶었던콩콩파조직원] — przydomek / oznaczenie] 콩콩이파
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=세보이고싶었던콩콩파조직원].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Gang Kongkongi
70. [Tabela modeli postaci [콩을싫어하는콩콩파조직원] — nazwa] 콩을싫어하는콩콩파조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=콩을싫어하는콩콩파조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Gang Kongkong Nielubujący Fasoli
71. [Tabela modeli postaci [콩을싫어하는콩콩파조직원] — przydomek / oznaczenie] 콩콩이파
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=콩을싫어하는콩콩파조직원].nickName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Tabela modeli postaci [콩콩이파보스] — nazwa] 콩콩이파보스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=콩콩이파보스].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Boss Gang Kongkongi
73. [Tabela modeli postaci [콩콩이파보스] — przydomek / oznaczenie] 콩콩이파
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=콩콩이파보스].nickName
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Tabela modeli postaci [에피] — nazwa] 에피
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에피].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Effie
75. [Tabela modeli postaci [위협적인철공회조직원] — nazwa] 위협적인철공회조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=위협적인철공회조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Groźny Członek Związku Ślusarski
76. [Tabela modeli postaci [위협적인철공회조직원] — przydomek / oznaczenie] 철공회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=위협적인철공회조직원].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Związek Ślusarski
77. [Tabela modeli postaci [몸푸는철공회조직원] — nazwa] 몸푸는철공회조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=몸푸는철공회조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Rozgrzewający Członek Związku Ślusarski
78. [Tabela modeli postaci [몸푸는철공회조직원] — przydomek / oznaczenie] 철공회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=몸푸는철공회조직원].nickName
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Tabela modeli postaci [철공회보스] — nazwa] 철공회보스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=철공회보스].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Boss Związku Ślusarski
80. [Tabela modeli postaci [철공회보스] — przydomek / oznaczenie] 철공회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=철공회보스].nickName
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Tabela modeli postaci [흥겨운마리아치조직원] — nazwa] 흥겨운마리아치조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흥겨운마리아치조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wesoły Członek Gangu Mariachi
82. [Tabela modeli postaci [흥겨운마리아치조직원] — przydomek / oznaczenie] 마리아치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흥겨운마리아치조직원].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mariachi
83. [Tabela modeli postaci [경쾌한마리아치조직원] — nazwa] 경쾌한마리아치조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=경쾌한마리아치조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Skoczny Członek Gangu Mariachi
84. [Tabela modeli postaci [경쾌한마리아치조직원] — przydomek / oznaczenie] 마리아치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=경쾌한마리아치조직원].nickName
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Tabela modeli postaci [아이드] — nazwa] 아이드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아이드].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ayed
86. [Tabela modeli postaci [아이드] — przydomek / oznaczenie] 마리아치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아이드].nickName
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Tabela modeli postaci [너맞아볼래매우] — nazwa] 너맞아볼래매우
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=너맞아볼래매우].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Chcesz Przymierzyć Cios? Bardzo!
88. [Tabela modeli postaci [너맞아볼래매우] — przydomek / oznaczenie] 당신은 강해졌나요
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=너맞아볼래매우].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Czy Stałeś Się Silniejszy?
89. [Tabela modeli postaci [노예] — nazwa] 노예
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=노예].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Niewolnik
90. [Tabela modeli postaci [노예] — przydomek / oznaczenie] 볼모가 된 빚쟁이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=노예].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dłużnik jako Zakładnik
91. [Tabela modeli postaci [모제스] — nazwa] 모제스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스].name
   limit: do 40 znaków
   EN: Moses
   PL: Moses
92. [Tabela modeli postaci [모제스] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스].nickName
   limit: do 40 znaków
   EN: LCD
   PL: LCD
93. [Tabela modeli postaci [에즈라] — nazwa] 에즈라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에즈라].name
   limit: do 40 znaków
   EN: Ezra
   PL: Ezra
94. [Tabela modeli postaci [에즈라] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에즈라].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Tabela modeli postaci [소드] — nazwa] 소드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소드].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Saude
96. [Tabela modeli postaci [소냐] — nazwa] 소냐
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소냐].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Sonya
97. [Tabela modeli postaci [전당포주인] — nazwa] 전당포주인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=전당포주인].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Właściciel Lombardu
98. [Tabela modeli postaci [전당포주인] — przydomek / oznaczenie] 10구
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=전당포주인].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dystrykt 10
99. [Tabela modeli postaci [촌스러운말투의콩콩파조직원] — nazwa] 촌스러운말투의콩콩파조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=촌스러운말투의콩콩파조직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Kongkong Mówiący Gwarą
100. [Tabela modeli postaci [촌스러운말투의콩콩파조직원] — przydomek / oznaczenie] 콩콩파
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=촌스러운말투의콩콩파조직원].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Gang Kongkong
101. [Tabela modeli postaci [크로머] — nazwa] 크로머
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크로머].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kromer
102. [Tabela modeli postaci [크로머] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크로머].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Nagel und Hammer
103. [Tabela modeli postaci [귀도] — nazwa] 귀도
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=귀도].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Guido
104. [Tabela modeli postaci [귀도] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=귀도].nickName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Tabela modeli postaci [N사심문관1] — nazwa] N사심문관1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사심문관1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Śledczy N Corp. 1
106. [Tabela modeli postaci [N사심문관1] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사심문관1].nickName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Tabela modeli postaci [N사심문관2] — nazwa] N사심문관2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사심문관2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Śledczy N Corp. 2
108. [Tabela modeli postaci [N사심문관2] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사심문관2].nickName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Tabela modeli postaci [N사심문관3] — nazwa] N사심문관3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사심문관3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Śledczy N Corp. 3
110. [Tabela modeli postaci [N사심문관3] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사심문관3].nickName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Tabela modeli postaci [지크프리트] — nazwa] 지크프리트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=지크프리트].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Siegfried
112. [Tabela modeli postaci [지크프리트] — przydomek / oznaczenie] 1급 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=지크프리트].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Fikser 1. Klasy
113. [Tabela modeli postaci [검문소경비] — nazwa] 검문소경비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검문소경비].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Straż Punktu Kontrolnego
114. [Tabela modeli postaci [검문소경비] — przydomek / oznaczenie] K사 검문소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검문소경비].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Punkt Kontrolny K Corp.
115. [Tabela modeli postaci [침식직원1] — nazwa] 침식직원1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=침식직원1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik w Erozji 1
116. [Tabela modeli postaci [침식직원1] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=침식직원1].nickName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Tabela modeli postaci [침식직원2] — nazwa] 침식직원2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=침식직원2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik w Erozji 2
118. [Tabela modeli postaci [침식직원2] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=침식직원2].nickName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Tabela modeli postaci [제복소드] — nazwa] 제복소드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=제복소드].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Saude w Mundurze
120. [Tabela modeli postaci [제복에피] — nazwa] 제복에피
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=제복에피].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Effie w Mundurze
121. [Tabela modeli postaci [학생크로머] — nazwa] 학생크로머
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=학생크로머].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kromer Uczennica
122. [Tabela modeli postaci [학생크로머] — przydomek / oznaczenie] 학급생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=학생크로머].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Uczeń Klasy
123. [Tabela modeli postaci [데미안] — nazwa] 데미안
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=데미안].name
   limit: do 40 znaków
   EN: Demian
   PL: Demian
124. [Tabela modeli postaci [학생데미안] — nazwa] 데미안
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=학생데미안].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Demian
125. [Tabela modeli postaci [늑대] — nazwa] 늑대
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=늑대].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wilk
126. [Tabela modeli postaci [늑대] — przydomek / oznaczenie] 늑대
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=늑대].nickName
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Tabela modeli postaci [표범] — nazwa] 표범
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=표범].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Leopard
128. [Tabela modeli postaci [표범] — przydomek / oznaczenie] 표범
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=표범].nickName
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Tabela modeli postaci [사자] — nazwa] 사자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사자].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Lew
130. [Tabela modeli postaci [사자] — przydomek / oznaczenie] 사자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사자].nickName
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Tabela modeli postaci [프롤로그단테] — nazwa] 프롤로그단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=프롤로그단테].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dante (Prolog)
132. [Tabela modeli postaci [프롤로그단테] — przydomek / oznaczenie] 프롤로그단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=프롤로그단테].nickName
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Tabela modeli postaci [프롤로그단테2] — nazwa] 프롤로그단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=프롤로그단테2].name
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Tabela modeli postaci [프롤로그단테2] — przydomek / oznaczenie] 프롤로그단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=프롤로그단테2].nickName
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Tabela modeli postaci [프롤로그파우스트] — nazwa] 프롤로그파우스트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=프롤로그파우스트].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Faust (Prolog)
136. [Tabela modeli postaci [프롤로그파우스트] — przydomek / oznaczenie] 프롤로그파우스트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=프롤로그파우스트].nickName
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Tabela modeli postaci [???] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=???].name
   limit: do 40 znaków
   EN: ???
   PL: ???
138. [Tabela modeli postaci [???] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=???].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Tabela modeli postaci [헤르만] — nazwa] 헤르만
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=헤르만].name
   limit: do 40 znaków
   EN: Hermann
   PL: Hermann
140. [Tabela modeli postaci [헤르만] — przydomek / oznaczenie] 헤르만
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=헤르만].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Hermann
141. [Tabela modeli postaci [피묻은귀도] — nazwa] 귀도
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피묻은귀도].name
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Tabela modeli postaci [다친소드] — nazwa] 소드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친소드].name
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Tabela modeli postaci [변신크로머] — nazwa] 크로머
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=변신크로머].name
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Tabela modeli postaci [애프터팀상사] — nazwa] 애프터팀상사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=애프터팀상사].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Firma Afterteam
145. [Tabela modeli postaci [애프터팀상사] — przydomek / oznaczenie] LCCA
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=애프터팀상사].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: LCCA
146. [Tabela modeli postaci [구보] — nazwa] 구보
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=구보].name
   limit: do 40 znaków
   EN: Gubo
   PL: Gubo
147. [Tabela modeli postaci [가환] — nazwa] 가환
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가환].name
   limit: do 40 znaków
   EN: Jia Huan
   PL: Jia Huan
148. [Tabela modeli postaci [그레고르요리사] — nazwa] 그레고르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르요리사].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Tabela modeli postaci [그레고르요리사] — przydomek / oznaczenie] 13번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르요리사].nickName
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Tabela modeli postaci [뫼르소요리사] — nazwa] 뫼르소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소요리사].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Tabela modeli postaci [뫼르소요리사] — przydomek / oznaczenie] 5번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소요리사].nickName
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Tabela modeli postaci [오티스요리사] — nazwa] 오티스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스요리사].name
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Tabela modeli postaci [오티스요리사] — przydomek / oznaczenie] 12번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스요리사].nickName
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Tabela modeli postaci [료슈요리사] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈요리사].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Tabela modeli postaci [료슈요리사] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈요리사].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Tabela modeli postaci [삼조] — nazwa] 삼조
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=삼조].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Samjo
157. [Tabela modeli postaci [보살치킨] — nazwa] 보살치킨
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=보살치킨].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kurczak Bosala
158. [Tabela modeli postaci [은봉치킨] — nazwa] 은봉치킨
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=은봉치킨].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kurczak Eunbonga
159. [Tabela modeli postaci [히스클리프요리사] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프요리사].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Tabela modeli postaci [히스클리프요리사] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프요리사].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Tabela modeli postaci [뒤틀린닭1] — nazwa] 뒤틀린닭1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린닭1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczony Kurczak 1
162. [Tabela modeli postaci [뒤틀린닭1] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린닭1].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczona Istota
163. [Tabela modeli postaci [뒤틀린닭2] — nazwa] 뒤틀린닭2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린닭2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczony Kurczak 2
164. [Tabela modeli postaci [뒤틀린닭2] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린닭2].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Tabela modeli postaci [뒤틀린손님1] — nazwa] 뒤틀린손님1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린손님1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczony Gość 1
166. [Tabela modeli postaci [뒤틀린손님1] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린손님1].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Tabela modeli postaci [뒤틀린손님2] — nazwa] 뒤틀린손님2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린손님2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczony Gość 2
168. [Tabela modeli postaci [뒤틀린손님2] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린손님2].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Tabela modeli postaci [뒤틀린주인] — nazwa] 뒤틀린주인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczony Gospodarz
170. [Tabela modeli postaci [뒤틀린주인] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Tabela modeli postaci [그렉료슈] — nazwa] 그레고르 & 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그렉료슈].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Gregor i Ryōshū
172. [Tabela modeli postaci [뒤틀린주인카운트1] — nazwa] 카운트1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인카운트1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Lada 1
173. [Tabela modeli postaci [뒤틀린주인카운트1] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인카운트1].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Tabela modeli postaci [뒤틀린주인카운트2] — nazwa] 카운트2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인카운트2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Lada 2
175. [Tabela modeli postaci [뒤틀린주인카운트2] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인카운트2].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Tabela modeli postaci [뒤틀린주인카운트3] — nazwa] 카운트3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인카운트3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Lada 3
177. [Tabela modeli postaci [뒤틀린주인카운트3] — przydomek / oznaczenie] 뒤틀린 것
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린주인카운트3].nickName
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Tabela modeli postaci [알폰소] — nazwa] 알폰소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알폰소].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Alfonso
179. [Tabela modeli postaci [동백] — nazwa] 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dongbaek
180. [Tabela modeli postaci [동랑] — nazwa] 동랑
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동랑].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dongrang
181. [Tabela modeli postaci [마리르] — nazwa] 마리르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마리르].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Marille
182. [Tabela modeli postaci [니코] — nazwa] 니코
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=니코].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Niko
183. [Tabela modeli postaci [란] — nazwa] 란
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=란].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ran
184. [Tabela modeli postaci [K사드론들] — nazwa] K사 드론들
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사드론들].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Drony K Corp.
185. [Tabela modeli postaci [기술해방연합기계] — nazwa] 기술해방연합 기계
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기술해방연합기계].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Maszyna Sojuszu Wyzwolenia Technologii
186. [Tabela modeli postaci [장미스패너1] — nazwa] 장미 스패너 공방 직원 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=장미스패너1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Warsztatu Rose Spanner 1
187. [Tabela modeli postaci [장미스패너2] — nazwa] 장미 스패너 공방 직원 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=장미스패너2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Warsztatu Rose Spanner 2
188. [Tabela modeli postaci [K사앰플기계] — nazwa] K사 앰플 도우미
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사앰플기계].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pomocnik K Corp. z Ampułkami
189. [Tabela modeli postaci [해킹당한K사앰플기계] — nazwa] K사 앰플 도우미
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=해킹당한K사앰플기계].name
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Tabela modeli postaci [슈렌느] — nazwa] 슈렌느
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=슈렌느].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Szurenne
191. [Tabela modeli postaci [K사3등급전투원] — nazwa] K사 3등급 적출직 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사3등급전투원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Ekstrakcji 3. Klasy K Corp.
192. [Tabela modeli postaci [K사연구원1] — nazwa] 다급한 K사 연구원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사연구원1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zdesperowany Badacz K Corp.
193. [Tabela modeli postaci [K사연구원2] — nazwa] 죽어가는 K사 연구원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사연구원2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Umierający Badacz K Corp.
194. [Tabela modeli postaci [K사연구원3] — nazwa] K사 연구원2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사연구원3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Badacz K Corp. 2
195. [Tabela modeli postaci [기술해방연합1] — nazwa] 기술해방연합원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기술해방연합1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Sojuszu Wyzwolenia Technologii
196. [Tabela modeli postaci [각성기술해방연합1] — nazwa] EGO 각성한 기술해방연합원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각성기술해방연합1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Sojuszu Wyzwolenia z E.G.O
197. [Tabela modeli postaci [동백여우각성] — nazwa] 각성한 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백여우각성].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Przebudzona Dongbaek
198. [Tabela modeli postaci [동백에고각성중] — nazwa] 흐드러지고 있는 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백에고각성중].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wiądząca Dongbaek
199. [Tabela modeli postaci [동백에고각성] — nazwa] 흐드러진 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백에고각성].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zwiędła Dongbaek
200. [Tabela modeli postaci [과거동백] — nazwa] 기억 속 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거동백].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wspomniana Dongbaek
201. [Tabela modeli postaci [영지] — nazwa] 기억 속 영지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=영지].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wspomniana Young-ji
202. [Tabela modeli postaci [과거구보] — nazwa] 기억 속 구보
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거구보].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wspomniany Gubo
203. [Tabela modeli postaci [과거동랑] — nazwa] 동랑
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거동랑].name
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Tabela modeli postaci [되살아난해방연합] — nazwa] 되살아난? 해방연합
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=되살아난해방연합].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Odrodzony? Sojusz Wyzwolenia
205. [Tabela modeli postaci [T사기술청1] — nazwa] T사 기술청 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사기술청1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Biura Technicznego T Corp.
206. [Tabela modeli postaci [각성동랑] — nazwa] 각성하는 동랑
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각성동랑].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Przebudzający się Dongrang
207. [Tabela modeli postaci [뒤틀린동랑] — nazwa] 뒤틀리는 동랑
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린동랑].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wypaczający się Dongrang
208. [Tabela modeli postaci [뒤틀린다친동랑] — nazwa] 뒤틀리는 동랑
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린다친동랑].name
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Tabela modeli postaci [다친에고동랑] — nazwa] 다친 에고 동랑
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친에고동랑].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ranny Dongrang z E.G.O
210. [Tabela modeli postaci [도망치던시민] — nazwa] 도망치던 시민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=도망치던시민].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Uciekający Obywatel
211. [Tabela modeli postaci [파우스트와삼조] — nazwa] 파우스트와 삼조
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트와삼조].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Faust i Samjo
212. [Tabela modeli postaci [검문소경비2] — nazwa] 2등급 적출직 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검문소경비2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik 2. Klasy Ekstrakcji
213. [Tabela modeli postaci [검문소경비2] — przydomek / oznaczenie] K사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검문소경비2].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: K Corp.
214. [Tabela modeli postaci [기술해방연합기계2] — nazwa] 기술해방연합기계2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기술해방연합기계2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Maszyna Sojuszu Wyzwolenia Technologii 2
215. [Tabela modeli postaci [T사기술청2] — nazwa] T사 기술청 직원2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사기술청2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Biura Technicznego T Corp. 2
216. [Tabela modeli postaci [변신T사기술청] — nazwa] T사 기술청 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=변신T사기술청].name
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Tabela modeli postaci [K사안내방송] — nazwa] 안내방송
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사안내방송].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Komunikat
218. [Tabela modeli postaci [옷벗은삼조] — nazwa] 삼조
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옷벗은삼조].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Tabela modeli postaci [동백여우각성_먼지] — nazwa] 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백여우각성_먼지].name
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Tabela modeli postaci [동백에고각성중_먼지] — nazwa] 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백에고각성중_먼지].name
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Tabela modeli postaci [동백에고각성중_다침] — nazwa] 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백에고각성중_다침].name
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Tabela modeli postaci [상이] — nazwa] 상이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=상이].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ranny
223. [Tabela modeli postaci [과거이상] — nazwa] 이상
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거이상].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Yi Sang
224. [Tabela modeli postaci [동백에고각성중_찔림] — nazwa] 동백
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=동백에고각성중_찔림].name
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Tabela modeli postaci [K사임원진1] — nazwa] K사 임원진 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사임원진1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kadra Zarządzająca K Corp. 1
226. [Tabela modeli postaci [K사임원진2] — nazwa] K사 임원진 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=K사임원진2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kadra Zarządzająca K Corp. 2
227. [Tabela modeli postaci [미카] — nazwa] 미카
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=미카].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mika
228. [Tabela modeli postaci [올가] — nazwa] 올가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=올가].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Olga
229. [Tabela modeli postaci [올가잠수복] — nazwa] 올가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=올가잠수복].name
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Tabela modeli postaci [무기레인] — nazwa] 레인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=무기레인].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Rain
231. [Tabela modeli postaci [레인] — nazwa] 레인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=레인].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Tabela modeli postaci [크랩게라디오] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크랩게라디오].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: ???
233. [Tabela modeli postaci [크랩게] — nazwa] 크랲게
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크랩게].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Krab
234. [Tabela modeli postaci [올가헬멧] — nazwa] 올가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=올가헬멧].name
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Tabela modeli postaci [쌍갈고리파조직원1] — nazwa] 쌍갈고리파 조직원 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쌍갈고리파조직원1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Gangu Podwójnych Haków 1
236. [Tabela modeli postaci [쌍갈고리파조직원2] — nazwa] 쌍갈고리파 조직원 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쌍갈고리파조직원2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Gangu Podwójnych Haków 2
237. [Tabela modeli postaci [쌍갈고리파조직원3] — nazwa] 쌍갈고리파 조직원 3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쌍갈고리파조직원3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Gangu Podwójnych Haków 3
238. [Tabela modeli postaci [쌍갈고리파조직원4] — nazwa] 쌍갈고리파 조직원 4
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쌍갈고리파조직원4].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Gangu Podwójnych Haków 4
239. [Tabela modeli postaci [쌍갈고리파조직원5] — nazwa] 쌍갈고리파 조직원 5
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쌍갈고리파조직원5].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Gangu Podwójnych Haków 5
240. [Tabela modeli postaci [클럽손님] — nazwa] 클럽 손님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=클럽손님].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Gość Klubu
241. [Tabela modeli postaci [파일럿] — nazwa] 파일럿
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파일럿].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pilot
242. [Tabela modeli postaci [스미] — nazwa] 스미
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스미].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Sumi
243. [Tabela modeli postaci [다친스미] — nazwa] 다친 스미
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친스미].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ranna Sumi
244. [Tabela modeli postaci [작은형님그림자] — nazwa] 작은형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은형님그림자].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Starszy Brat
245. [Tabela modeli postaci [작은형님] — nazwa] 작은형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은형님].name
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Tabela modeli postaci [작은형님안경] — nazwa] 작은형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은형님안경].name
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Tabela modeli postaci [작은형님발광] — nazwa] 작은형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은형님발광].name
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Tabela modeli postaci [작은형님다침] — nazwa] 작은형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은형님다침].name
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Tabela modeli postaci [작은형님책] — nazwa] 작은형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은형님책].name
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Tabela modeli postaci [쪽빛노인] — nazwa] 쪽빛노인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쪽빛노인].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Starzec w Indygo
251. [Tabela modeli postaci [쪽빛노인] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쪽빛노인].nickName
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Tabela modeli postaci [쪽빛노인후드] — nazwa] 쪽빛노인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쪽빛노인후드].name
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Tabela modeli postaci [쪽빛노인후드] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쪽빛노인후드].nickName
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Tabela modeli postaci [쪽빛노인무기] — nazwa] 쪽빛노인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쪽빛노인무기].name
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Tabela modeli postaci [쪽빛노인무기] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쪽빛노인무기].nickName
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Tabela modeli postaci [LCCB직원백화1] — nazwa] LCCB 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCCB직원백화1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik LCCB
257. [Tabela modeli postaci [LCCB직원백화2] — nazwa] LCCB 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCCB직원백화2].name
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Tabela modeli postaci [림] — nazwa] 림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=림].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Lim
259. [Tabela modeli postaci [작은아우] — nazwa] 작은 아우
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작은아우].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Młodszy Brat
260. [Tabela modeli postaci [다친이스마엘] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친이스마엘].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Tabela modeli postaci [다친이스마엘] — przydomek / oznaczenie] 8번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친이스마엘].nickName
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Tabela modeli postaci [다친파우스트] — nazwa] 파우스트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친파우스트].name
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Tabela modeli postaci [다친파우스트] — przydomek / oznaczenie] 2번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친파우스트].nickName
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Tabela modeli postaci [에이해브] — nazwa] 에이해브
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브].name
   limit: do 40 znaków
   EN: Ahab
   PL: Ahab
265. [Tabela modeli postaci [에이해브] — przydomek / oznaczenie] 피쿼드타운 선장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브].nickName
   limit: do 40 znaków
   EN: Captain of the Pequod Town
   PL: Kapitan Pequod Town
266. [Tabela modeli postaci [에이해브다침] — nazwa] 에이해브
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브다침].name
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Tabela modeli postaci [에이해브다침] — przydomek / oznaczenie] 피쿼드타운 선장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브다침].nickName
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Tabela modeli postaci [에이해브과거] — nazwa] 에이해브
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브과거].name
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Tabela modeli postaci [에이해브과거] — przydomek / oznaczenie] 피쿼드호 선장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브과거].nickName
   limit: do 40 znaków
   EN: Captain of the Pequod
   PL: Kapitan Pequod
270. [Tabela modeli postaci [핍과거] — nazwa] 핍
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=핍과거].name
   limit: do 40 znaków
   EN: Pip
   PL: Pip
271. [Tabela modeli postaci [핍과거] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=핍과거].nickName
   limit: do 40 znaków
   EN: The Pequod
   PL: Pequod
272. [Tabela modeli postaci [퀴케그] — nazwa] 퀴케그
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그].name
   limit: do 40 znaków
   EN: Queequeg
   PL: Queequeg
273. [Tabela modeli postaci [퀴케그] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그].nickName
   limit: do 40 znaków
   EN: Pequod Town
   PL: Pequod Town
274. [Tabela modeli postaci [퀴케그과거] — nazwa] 퀴케그
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그과거].name
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Tabela modeli postaci [퀴케그과거] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그과거].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Tabela modeli postaci [스타벅] — nazwa] 스타벅
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스타벅].name
   limit: do 40 znaków
   EN: Starbuck
   PL: Starbuck
277. [Tabela modeli postaci [스타벅] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스타벅].nickName
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Tabela modeli postaci [스타벅과거] — nazwa] 스타벅
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스타벅과거].name
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Tabela modeli postaci [스타벅과거] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스타벅과거].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Tabela modeli postaci [핍] — nazwa] 핍
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=핍].name
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Tabela modeli postaci [핍] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=핍].nickName
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Tabela modeli postaci [퀴케그가면] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그가면].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Tabela modeli postaci [퀴케그가면] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그가면].nickName
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Tabela modeli postaci [스텁] — nazwa] 스텁
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스텁].name
   limit: do 40 znaków
   EN: Stubb
   PL: Stubb
285. [Tabela modeli postaci [스텁] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스텁].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Tabela modeli postaci [피쿼드호주민1] — nazwa] 피쿼드호주민1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피쿼드호주민1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mieszkaniec Pequod 1
287. [Tabela modeli postaci [피쿼드호주민1] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피쿼드호주민1].nickName
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Tabela modeli postaci [피쿼드호주민2] — nazwa] 피쿼드호주민2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피쿼드호주민2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mieszkaniec Pequod 2
289. [Tabela modeli postaci [피쿼드호주민2] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피쿼드호주민2].nickName
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Tabela modeli postaci [이스마엘과거] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘과거].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Tabela modeli postaci [이스마엘과거] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘과거].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Tabela modeli postaci [에이해브그림자] — nazwa] 에이해브
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브그림자].name
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Tabela modeli postaci [에이해브그림자] — przydomek / oznaczenie] 피쿼드타운 선장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에이해브그림자].nickName
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Tabela modeli postaci [이스마엘과거2] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘과거2].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Tabela modeli postaci [퀴케그녹음] — nazwa] 퀴케그
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그녹음].name
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Tabela modeli postaci [퀴케그녹음] — przydomek / oznaczenie] 피쿼드타운
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그녹음].nickName
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Tabela modeli postaci [스텁그림자] — nazwa] 스텁
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스텁그림자].name
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Tabela modeli postaci [스텁그림자] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스텁그림자].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Tabela modeli postaci [퀴케그그림자] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그그림자].name
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Tabela modeli postaci [퀴케그그림자] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴케그그림자].nickName
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Tabela modeli postaci [도미노] — nazwa] 도미노
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=도미노].name
   limit: do 40 znaków
   EN: Domino
   PL: Domino
302. [Tabela modeli postaci [도미노] — przydomek / oznaczenie] 구름마을
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=도미노].nickName
   limit: do 40 znaków
   EN: Cloud Town
   PL: Miasteczko w Chmurach
303. [Tabela modeli postaci [도도루] — nazwa] 도도루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=도도루].name
   limit: do 40 znaków
   EN: Dodoru
   PL: Dodoru
304. [Tabela modeli postaci [도도루] — przydomek / oznaczenie] 선물 공장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=도도루].nickName
   limit: do 40 znaków
   EN: Gift Factory
   PL: Fabryka Prezentów
305. [Tabela modeli postaci [화난도도루] — nazwa] 도도루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=화난도도루].name
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Tabela modeli postaci [화난도도루] — przydomek / oznaczenie] 선물 공장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=화난도도루].nickName
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Tabela modeli postaci [크레용] — nazwa] 크레용
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크레용].name
   limit: do 40 znaków
   EN: Crayon
   PL: Crayon
308. [Tabela modeli postaci [크레용] — przydomek / oznaczenie] 구름마을
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크레용].nickName
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Tabela modeli postaci [산타타] — nazwa] 산타타
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산타타].name
   limit: do 40 znaków
   EN: Santata
   PL: Santata
310. [Tabela modeli postaci [산타타] — przydomek / oznaczenie] 선물 공장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산타타].nickName
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Tabela modeli postaci [빨간노움] — nazwa] 빨간 노움
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=빨간노움].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Czerwony Nome
312. [Tabela modeli postaci [빨간노움] — przydomek / oznaczenie] 선물 공장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=빨간노움].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Fabryka Prezentów
313. [Tabela modeli postaci [초록노움] — nazwa] 초록 노움
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=초록노움].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zielony Nome
314. [Tabela modeli postaci [초록노움] — przydomek / oznaczenie] 선물 공장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=초록노움].nickName
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Tabela modeli postaci [검은노움] — nazwa] 검은 노움
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검은노움].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Czarny Nome
316. [Tabela modeli postaci [검은노움] — przydomek / oznaczenie] 선물 공장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검은노움].nickName
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Tabela modeli postaci [일등 항해사] — nazwa] 일등 항해사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=일등 항해사].name
   limit: do 40 znaków
   EN: First Mate
   PL: Pierwszy Oficer
318. [Tabela modeli postaci [일등 항해사] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=일등 항해사].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Tabela modeli postaci [작살잡이] — nazwa] 작살잡이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작살잡이].name
   limit: do 40 znaków
   EN: Harpooneer
   PL: Harpuonista
320. [Tabela modeli postaci [작살잡이] — przydomek / oznaczenie] 피쿼드호
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=작살잡이].nickName
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Tabela modeli postaci [흑운회조직원1] — nazwa] 흑운회 조직원 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑운회조직원1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Związku Czarnego Obłoku 1
322. [Tabela modeli postaci [흑운회조직원2] — nazwa] 흑운회 조직원 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑운회조직원2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Związku Czarnego Obłoku 2
323. [Tabela modeli postaci [검계조직원1] — nazwa] 검계 조직원 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검계조직원1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Ródu Ostrza 1
324. [Tabela modeli postaci [앵두] — nazwa] 앵두
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=앵두].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Aeng-du
325. [Tabela modeli postaci [김삿갓] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kim w Bambusowym Kapeluszu
326. [Tabela modeli postaci [최종김삿갓] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=최종김삿갓].name
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Tabela modeli postaci [쥰] — nazwa] 쥰
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쥰].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Jun
328. [Tabela modeli postaci [시계쥰] — nazwa] 쥰
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시계쥰].name
   (powtórzenie elementu 327 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Tabela modeli postaci [LCA특작팀] — nazwa] LCA 특수작전팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA특작팀].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zespół Operacji Specjalnych LCA
330. [Tabela modeli postaci [카이만] — nazwa] 카이만
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카이만].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Caiman
331. [Tabela modeli postaci [히스클리프꾸밈] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프꾸밈].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Tabela modeli postaci [히스클리프꾸밈] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프꾸밈].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Tabela modeli postaci [히스클리프헝클어짐] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프헝클어짐].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Tabela modeli postaci [히스클리프헝클어짐] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프헝클어짐].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Tabela modeli postaci [어린히스클리프] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린히스클리프].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Tabela modeli postaci [어린히스클리프] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린히스클리프].nickName
   limit: do 40 znaków
   EN: Wuthering Heights
   PL: Wuthering Heights
337. [Tabela modeli postaci [힌들리] — nazwa] 힌들리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=힌들리].name
   limit: do 40 znaków
   EN: Hindley
   PL: Hindley
338. [Tabela modeli postaci [힌들리] — przydomek / oznaczenie] 언쇼 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=힌들리].nickName
   limit: do 40 znaków
   EN: Earnshaw Family
   PL: Rodzina Earnshaw
339. [Tabela modeli postaci [어린힌들리] — nazwa] 힌들리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린힌들리].name
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Tabela modeli postaci [어린힌들리] — przydomek / oznaczenie] 언쇼 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린힌들리].nickName
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Tabela modeli postaci [린튼] — nazwa] 린튼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=린튼].name
   limit: do 40 znaków
   EN: Linton
   PL: Linton
342. [Tabela modeli postaci [린튼] — przydomek / oznaczenie] 에드가 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=린튼].nickName
   limit: do 40 znaków
   EN: Edgar Family
   PL: Rodzina Edgar
343. [Tabela modeli postaci [어린린튼] — nazwa] 린튼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린린튼].name
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Tabela modeli postaci [어린린튼] — przydomek / oznaczenie] 에드가 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린린튼].nickName
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Tabela modeli postaci [캐서린] — nazwa] 캐서린
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=캐서린].name
   limit: do 40 znaków
   EN: Catherine
   PL: Catherine
346. [Tabela modeli postaci [캐서린] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=캐서린].nickName
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Tabela modeli postaci [어린캐서린2] — nazwa] 캐서린
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린캐서린2].name
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Tabela modeli postaci [어린캐서린2] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린캐서린2].nickName
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Tabela modeli postaci [조세핀] — nazwa] 조세핀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=조세핀].name
   limit: do 40 znaków
   EN: Josephine
   PL: Josephine
350. [Tabela modeli postaci [조세핀] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=조세핀].nickName
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Tabela modeli postaci [넬리] — nazwa] 넬리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=넬리].name
   limit: do 40 znaków
   EN: Nelly
   PL: Nelly
352. [Tabela modeli postaci [넬리] — przydomek / oznaczenie] 치프 버틀러
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=넬리].nickName
   limit: do 40 znaków
   EN: Chief Butler
   PL: Główny Kamerdyner
353. [Tabela modeli postaci [데드레빗츠1] — nazwa] 데드레빗츠1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=데드레빗츠1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dead Rabbits 1
354. [Tabela modeli postaci [데드레빗츠2] — nazwa] 데드레빗츠2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=데드레빗츠2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dead Rabbits 2
355. [Tabela modeli postaci [데드레빗츠보스] — nazwa] 데드레빗츠보스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=데드레빗츠보스].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Boss Dead Rabbits
356. [Tabela modeli postaci [린튼버틀러1] — nazwa] 린튼버틀러1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=린튼버틀러1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kamerdyner Linton 1
357. [Tabela modeli postaci [린튼버틀러2] — nazwa] 린튼버틀러2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=린튼버틀러2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Kamerdyner Linton 2
358. [Tabela modeli postaci [T사갱단1] — nazwa] T사갱단1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사갱단1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Gang T Corp. 1
359. [Tabela modeli postaci [T사갱단2] — nazwa] T사갱단2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사갱단2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Gang T Corp. 2
360. [Tabela modeli postaci [T사시민] — nazwa] T사시민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사시민].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Obywatel T Corp.
361. [Tabela modeli postaci [외우피협회F] — nazwa] 외우피협회F
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=외우피협회F].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Stowarzyszenie Weupi F
362. [Tabela modeli postaci [외우피협회F2] — nazwa] 외우피협회F2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=외우피협회F2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Stowarzyszenie Weupi F2
363. [Tabela modeli postaci [외우피협회보스F] — nazwa] 외우피협회보스F
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=외우피협회보스F].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Boss Stowarzyszenia Weupi F
364. [Tabela modeli postaci [홍루SD] — nazwa] 홍루SD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루SD].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Hong Lu SD
365. [Tabela modeli postaci [로쟈SD] — nazwa] 로쟈SD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈SD].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Rodion SD
366. [Tabela modeli postaci [언쇼] — nazwa] 언쇼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=언쇼].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Earnshaw
367. [Tabela modeli postaci [마왕히스클리프1] — nazwa] 마왕히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Erlking Heathcliff
368. [Tabela modeli postaci [어린히스클리프2] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린히스클리프2].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Tabela modeli postaci [어린히스클리프2] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린히스클리프2].nickName
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Tabela modeli postaci [힌들리2] — nazwa] 힌들리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=힌들리2].name
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Tabela modeli postaci [힌들리2] — przydomek / oznaczenie] 언쇼 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=힌들리2].nickName
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Tabela modeli postaci [아세아] — nazwa] 아세아
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아세아].name
   limit: do 40 znaków
   EN: Aseah
   PL: Aseah
373. [Tabela modeli postaci [어린캐서린] — nazwa] 캐서린
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린캐서린].name
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Tabela modeli postaci [어린캐서린] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린캐서린].nickName
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Tabela modeli postaci [힌들리늑대] — nazwa] 힌들리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=힌들리늑대].name
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Tabela modeli postaci [힌들리늑대] — przydomek / oznaczenie] 언쇼 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=힌들리늑대].nickName
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Tabela modeli postaci [히스클리프과거] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프과거].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Tabela modeli postaci [뒤틀린히스클리프] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린히스클리프].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Tabela modeli postaci [마왕캐서린] — nazwa] 모든 캐서린
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕캐서린].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wszystkie Catherine
380. [Tabela modeli postaci [마왕히스클리프2] — nazwa] 마왕 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프2].name
   limit: do 40 znaków
   EN: Erlking Heathcliff
   PL: Erlking Heathcliff
381. [Tabela modeli postaci [마왕히스클리프2] — przydomek / oznaczenie — tylko EN w danych gry] A Distant World
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프2].nickName
   limit: do 40 znaków
   EN: A Distant World
   PL: A Distant World
382. [Tabela modeli postaci [어린린튼2] — nazwa] 린튼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린린튼2].name
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Tabela modeli postaci [어린린튼2] — przydomek / oznaczenie] 에드가 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린린튼2].nickName
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Tabela modeli postaci [린튼2] — nazwa] 린튼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=린튼2].name
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Tabela modeli postaci [린튼2] — przydomek / oznaczenie] 에드가 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=린튼2].nickName
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Tabela modeli postaci [조세핀2] — nazwa] 조세핀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=조세핀2].name
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Tabela modeli postaci [조세핀2] — przydomek / oznaczenie] 워더링하이츠
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=조세핀2].nickName
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Tabela modeli postaci [마왕히스클리프말] — nazwa] 마왕 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프말].name
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Tabela modeli postaci [마왕히스클리프말] — przydomek / oznaczenie — tylko EN w danych gry] A Distant World
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프말].nickName
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Tabela modeli postaci [마왕히스클리프3] — nazwa] 마왕 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프3].name
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Tabela modeli postaci [마왕히스클리프3] — przydomek / oznaczenie — tylko EN w danych gry] A Distant World
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마왕히스클리프3].nickName
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Tabela modeli postaci [다친넬리] — nazwa] 넬리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친넬리].name
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Tabela modeli postaci [다친넬리] — przydomek / oznaczenie] 치프 버틀러
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친넬리].nickName
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Tabela modeli postaci [히스클리프검정] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프검정].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Tabela modeli postaci [히스클리프검정] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프검정].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Tabela modeli postaci [히스클리프다침] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프다침].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Tabela modeli postaci [히스클리프다침] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프다침].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Tabela modeli postaci [N사연구원검은색] — nazwa] 약지 출신 연구원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사연구원검은색].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Badacz z The Ring
399. [Tabela modeli postaci [히스클리프2] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프2].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Tabela modeli postaci [히스클리프2] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프2].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Tabela modeli postaci [탐정홍루] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=탐정홍루].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Tabela modeli postaci [탐정홍루] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=탐정홍루].nickName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Tabela modeli postaci [탐정로쟈] — nazwa] 로쟈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=탐정로쟈].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Tabela modeli postaci [탐정로쟈] — przydomek / oznaczenie] 9번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=탐정로쟈].nickName
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Tabela modeli postaci [탐정료슈] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=탐정료슈].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Tabela modeli postaci [탐정료슈] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=탐정료슈].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Tabela modeli postaci [T사대표] — nazwa] T사 대표
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사대표].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Prezes T Corp.
408. [Tabela modeli postaci [진짜T사대표] — nazwa] T사 대표
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=진짜T사대표].name
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Tabela modeli postaci [범블] — nazwa] 범블
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=범블].name
   limit: do 40 znaków
   EN: Bumble
   PL: Bumble
410. [Tabela modeli postaci [T사4등급] — nazwa] T사4등급
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사4등급].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik T Corp. 4. Klasy
411. [Tabela modeli postaci [T사사무직] — nazwa] T사사무직
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사사무직].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Biurowy T Corp.
412. [Tabela modeli postaci [시간살인마] — nazwa] 시간 살인마
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시간살인마].name
   limit: do 40 znaków
   EN: The Time Ripper
   PL: The Time Ripper
413. [Tabela modeli postaci [시간살인마] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시간살인마].nickName
   limit: do 40 znaków
   EN: Distortion
   PL: Wypaczenie
414. [Tabela modeli postaci [시간살인마변신] — nazwa] 시간 살인마
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시간살인마변신].name
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Tabela modeli postaci [시간살인마변신] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시간살인마변신].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Tabela modeli postaci [유로지비대장] — nazwa] 유로지비 대장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유로지비대장].name
   limit: do 40 znaków
   EN: Yurodiviye Captain
   PL: Yurodiviye Captain
417. [Tabela modeli postaci [유로지비대장] — przydomek / oznaczenie] 20구 유로지비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유로지비대장].nickName
   limit: do 40 znaków
   EN: District 20 Yurodivy
   PL: Dystrykt 20 Yurodivy
418. [Tabela modeli postaci [유로지비멤버1] — nazwa] 유로지비 멤버
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유로지비멤버1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Członek Yurodiviye
419. [Tabela modeli postaci [유로지비멤버2] — nazwa] 유로지비 멤버
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유로지비멤버2].name
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Tabela modeli postaci [시살동생] — nazwa] 동생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시살동생].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Młodsze Rodzeństwo
421. [Tabela modeli postaci [감속더미] — nazwa] 감속더미
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=감속더미].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Manekin Spowalniający
422. [Tabela modeli postaci [돈키T3] — nazwa] 돈키T3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키T3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Don Quixote T3
423. [Tabela modeli postaci [다친유로지비대장] — nazwa] 유로지비 대장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친유로지비대장].name
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Tabela modeli postaci [다친유로지비대장] — przydomek / oznaczenie] 20구 유로지비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친유로지비대장].nickName
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Tabela modeli postaci [마이] — nazwa] 마이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마이].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mai
426. [Tabela modeli postaci [T사2등급] — nazwa] T사2등급
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=T사2등급].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik T Corp. 2. Klasy
427. [Tabela modeli postaci [다친시간살인마변신] — nazwa] 시간 살인마
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친시간살인마변신].name
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Tabela modeli postaci [다친시간살인마변신] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친시간살인마변신].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Tabela modeli postaci [질투죄종] — nazwa] 질투죄종오티스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=질투죄종].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Outis Grzechu Zazdrości
430. [Tabela modeli postaci [열차아이] — nazwa] 호기심 많은 아이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=열차아이].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zaintrygowane Dziecko
431. [Tabela modeli postaci [카세티] — nazwa] 카세티
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카세티].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Casetti
432. [Tabela modeli postaci [카세티혈귀] — nazwa] 카세티
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카세티혈귀].name
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Tabela modeli postaci [북부창] — nazwa] 북부 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=북부창].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Północny Fikser
434. [Tabela modeli postaci [북부대검] — nazwa] 북부 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=북부대검].name
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Tabela modeli postaci [북부대검혈귀] — nazwa] 북부 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=북부대검혈귀].name
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Tabela modeli postaci [W사정리요원] — nazwa] 정리 요원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=W사정리요원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Agent Porządkowy
437. [Tabela modeli postaci [W사정리요원2] — nazwa] 정리 요원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=W사정리요원2].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Tabela modeli postaci [실루엣돈키호테] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=실루엣돈키호테].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Tabela modeli postaci [돈키호테다침] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테다침].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Tabela modeli postaci [돈키호테다침] — przydomek / oznaczenie] 3번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테다침].nickName
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Tabela modeli postaci [말쿠트] — nazwa] 말쿠트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=말쿠트].name
   limit: do 40 znaków
   EN: Malkuth
   PL: Malkuth
442. [Tabela modeli postaci [네짜흐] — nazwa] 네짜흐
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=네짜흐].name
   limit: do 40 znaków
   EN: Netzach
   PL: Netzach
443. [Tabela modeli postaci [호드] — nazwa] 호드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호드].name
   limit: do 40 znaków
   EN: Hod
   PL: Hod
444. [Tabela modeli postaci [체사라] — nazwa] 체사라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=체사라].name
   limit: do 40 znaków
   EN: Cesara
   PL: Cesara
445. [Tabela modeli postaci [체사라] — przydomek / oznaczenie] P사 아카이빙 부서
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=체사라].nickName
   limit: do 40 znaków
   EN: P Corp. Archival Department
   PL: Dział Archiwizacji P Corp.
446. [Tabela modeli postaci [알레시오] — nazwa] 알레시오
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알레시오].name
   limit: do 40 znaków
   EN: Alessio
   PL: Alessio
447. [Tabela modeli postaci [알레시오] — przydomek / oznaczenie] P사 아카이빙 부서
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알레시오].nickName
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Tabela modeli postaci [로메로] — nazwa] 로메로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로메로].name
   limit: do 40 znaków
   EN: Romero
   PL: Romero
449. [Tabela modeli postaci [로메로] — przydomek / oznaczenie] 송곳니 사냥 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로메로].nickName
   limit: do 40 znaków
   EN: Fanghunt Office
   PL: Biuro Fanghunt
450. [Tabela modeli postaci [혈귀사냥꾼] — nazwa] 혈귀 사냥꾼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀사냥꾼].name
   limit: do 40 znaków
   EN: Bloodfiend Hunter
   PL: Łowca Krwiołaków
451. [Tabela modeli postaci [혈귀사냥꾼] — przydomek / oznaczenie] 송곳니 사냥 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀사냥꾼].nickName
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Tabela modeli postaci [까미유카메라] — nazwa] 까미유
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=까미유카메라].name
   limit: do 40 znaków
   EN: Camille
   PL: Camille
453. [Tabela modeli postaci [까미유카메라] — przydomek / oznaczenie] 서부 섕크 협회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=까미유카메라].nickName
   limit: do 40 znaków
   EN: Cinq Assoc. West
   PL: Cinq Assoc. West
454. [Tabela modeli postaci [까미유] — nazwa] 까미유
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=까미유].name
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Tabela modeli postaci [까미유] — przydomek / oznaczenie] 서부 섕크 협회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=까미유].nickName
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Tabela modeli postaci [폴라] — nazwa] 폴라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=폴라].name
   limit: do 40 znaków
   EN: Paula
   PL: Paula
457. [Tabela modeli postaci [폴라] — przydomek / oznaczenie] 서부 츠바이 협회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=폴라].nickName
   limit: do 40 znaków
   EN: Zwei Assoc. West
   PL: Zwei Assoc. West
458. [Tabela modeli postaci [가시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가시춘].name
   limit: do 40 znaków
   EN: Jia Xichun
   PL: Jia Xichun
459. [Tabela modeli postaci [가시춘] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가시춘].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Tabela modeli postaci [웨이] — nazwa] 웨이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=웨이].name
   limit: do 40 znaków
   EN: Wei
   PL: Wei
461. [Tabela modeli postaci [웨이] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=웨이].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Tabela modeli postaci [한울] — nazwa] 한울
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=한울].name
   limit: do 40 znaków
   EN: Han-ul
   PL: Han-ul
463. [Tabela modeli postaci [한울] — przydomek / oznaczenie] 북부 하나 협회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=한울].nickName
   limit: do 40 znaków
   EN: Hana Assoc. North
   PL: Hana Assoc. North
464. [Tabela modeli postaci [휴고] — nazwa] 휴고
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=휴고].name
   limit: do 40 znaków
   EN: Hugo
   PL: Hugo
465. [Tabela modeli postaci [휴고] — przydomek / oznaczenie] 북부 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=휴고].nickName
   limit: do 40 znaków
   EN: Northern Fixer
   PL: Północny Fikser
466. [Tabela modeli postaci [피주머니] — nazwa] 피주머니
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피주머니].name
   limit: do 40 znaków
   EN: Bloodbag
   PL: Sakiewka Krwi
467. [Tabela modeli postaci [피주머니] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피주머니].nickName
   limit: do 40 znaków
   EN: La Manchaland
   PL: La Manchaland
468. [Tabela modeli postaci [불주먹] — nazwa] 감격에 찬 해결사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=불주먹].name
   limit: do 40 znaków
   EN: Delighted Fixer
   PL: Zachwycony Fikser
469. [Tabela modeli postaci [불주먹] — przydomek / oznaczenie] 불주먹 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=불주먹].nickName
   limit: do 40 znaków
   EN: Firefist Office
   PL: Biuro Firefist
470. [Tabela modeli postaci [이발사] — nazwa] 이발사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사].name
   limit: do 40 znaków
   EN: The Barber
   PL: Goliciarz
471. [Tabela modeli postaci [이발사] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Tabela modeli postaci [라만차내레이션] — nazwa] 내레이션
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=라만차내레이션].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Narracja
473. [Tabela modeli postaci [이발사다침] — nazwa] 이발사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사다침].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Tabela modeli postaci [이발사다침] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사다침].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Tabela modeli postaci [이발사부하] — nazwa] 이발사부하
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사부하].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Podwładny Goliciarza
476. [Tabela modeli postaci [이발사부하] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사부하].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Tabela modeli postaci [기사돈키] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사돈키].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Tabela modeli postaci [기사돈키] — przydomek / oznaczenie] 용감한 모험가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사돈키].nickName
   limit: do 40 znaków
   EN: Brave Adventurer
   PL: Odważny Poszukiwacz Przygód
479. [Tabela modeli postaci [기사싱클] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사싱클].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Tabela modeli postaci [기사싱클] — przydomek / oznaczenie] 하얀 달의 기사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사싱클].nickName
   limit: do 40 znaków
   EN: The Knight of the White Moon
   PL: Rycerz Białego Księżyca
481. [Tabela modeli postaci [산손] — nazwa] 산손
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산손].name
   limit: do 40 znaków
   EN: Sansón
   PL: Sansón
482. [Tabela modeli postaci [산손] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산손].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Tabela modeli postaci [기사산손] — nazwa] 산손
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사산손].name
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Tabela modeli postaci [기사산손] — przydomek / oznaczenie] 하얀 달의 기사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사산손].nickName
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Tabela modeli postaci [주민오티스] — nazwa] 오티스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=주민오티스].name
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Tabela modeli postaci [주민오티스] — przydomek / oznaczenie] 지나가는 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=주민오티스].nickName
   limit: do 40 znaków
   EN: Traveling Villager
   PL: Przechodzący Mieszkaniec
487. [Tabela modeli postaci [주민로쟈] — nazwa] 로쟈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=주민로쟈].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Tabela modeli postaci [주민로쟈] — przydomek / oznaczenie] 양떼 목장 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=주민로쟈].nickName
   limit: do 40 znaków
   EN: Shepherd Ranch Villager
   PL: Mieszkaniec Rancza Pasterskiego
489. [Tabela modeli postaci [말레고르] — nazwa] 그레고르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=말레고르].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Tabela modeli postaci [말레고르] — przydomek / oznaczenie] 로시난테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=말레고르].nickName
   limit: do 40 znaków
   EN: Rocinante
   PL: Rocinante
491. [Tabela modeli postaci [곰스클리프] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=곰스클리프].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Tabela modeli postaci [곰스클리프] — przydomek / oznaczenie] 무시무시한 곰
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=곰스클리프].nickName
   limit: do 40 znaków
   EN: Big Scary Bear
   PL: Straszliwy Niedźwiedź
493. [Tabela modeli postaci [달기사실루엣] — nazwa] 하얀 달의 기사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=달기사실루엣].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Rycerz Białego Księżyca
494. [Tabela modeli postaci [돌시네아] — nazwa] 돌시네아
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시네아].name
   limit: do 40 znaków
   EN: Dulcinea
   PL: Dulcynea
495. [Tabela modeli postaci [돌시네아] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시네아].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Tabela modeli postaci [돌시부하1] — nazwa] 돌시부하1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시부하1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Podwładny Dulcynei 1
497. [Tabela modeli postaci [돌시부하1] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시부하1].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Tabela modeli postaci [돌시부하2] — nazwa] 돌시부하2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시부하2].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Podwładny Dulcynei 2
499. [Tabela modeli postaci [돌시부하2] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시부하2].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Tabela modeli postaci [신부] — nazwa] 신부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부].name
   limit: do 40 znaków
   EN: The Priest
   PL: Ksiądz
501. [Tabela modeli postaci [신부] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Tabela modeli postaci [백발가면혈귀실루엣] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=백발가면혈귀실루엣].name
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Tabela modeli postaci [백발가면혈귀실루엣] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=백발가면혈귀실루엣].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Tabela modeli postaci [백발가면혈귀] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=백발가면혈귀].name
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Tabela modeli postaci [백발가면혈귀] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=백발가면혈귀].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Tabela modeli postaci [혈귀료슈] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀료슈].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Tabela modeli postaci [혈귀료슈] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀료슈].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Tabela modeli postaci [혈귀홍루] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀홍루].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Tabela modeli postaci [혈귀홍루] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀홍루].nickName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Tabela modeli postaci [기사싱클2] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사싱클2].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Tabela modeli postaci [기사싱클2] — przydomek / oznaczenie] 하얀 달의 기사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=기사싱클2].nickName
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Tabela modeli postaci [로메로다침] — nazwa] 로메로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로메로다침].name
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Tabela modeli postaci [로메로다침] — przydomek / oznaczenie] 송곳니 사냥 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로메로다침].nickName
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Tabela modeli postaci [신부다침] — nazwa] 신부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부다침].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Tabela modeli postaci [신부다침] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부다침].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Tabela modeli postaci [웨이다침] — nazwa] 웨이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=웨이다침].name
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Tabela modeli postaci [웨이다침] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=웨이다침].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: La Manchaland
518. [Tabela modeli postaci [신부부하] — nazwa] 신부부하
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부부하].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Podwładny Księdza
519. [Tabela modeli postaci [신부부하] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부부하].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Tabela modeli postaci [돌시네아다침] — nazwa] 돌시네아
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시네아다침].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Tabela modeli postaci [돌시네아다침] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시네아다침].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Tabela modeli postaci [맨발돈키호테] — nazwa] 돈키호테?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=맨발돈키호테].name
   limit: do 40 znaków
   EN: Don Quixote?
   PL: Don Quixote?
523. [Tabela modeli postaci [맨발돈키호테] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=맨발돈키호테].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Tabela modeli postaci [돈키호테무표정] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테무표정].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Tabela modeli postaci [돈키호테무표정] — przydomek / oznaczenie] 3번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테무표정].nickName
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Tabela modeli postaci [키호테] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=키호테].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Tabela modeli postaci [키호테] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=키호테].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Tabela modeli postaci [가면키호테] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가면키호테].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Tabela modeli postaci [가면키호테] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가면키호테].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Tabela modeli postaci [산초] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산초].name
   limit: do 40 znaków
   EN: Sancho
   PL: Sancho
531. [Tabela modeli postaci [산초] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산초].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Tabela modeli postaci [옛돈키] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옛돈키].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Tabela modeli postaci [옛돈키] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옛돈키].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Tabela modeli postaci [옛산초] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옛산초].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Tabela modeli postaci [옛산초] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옛산초].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Tabela modeli postaci [산손베르길리우스] — nazwa] 산손
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산손베르길리우스].name
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Tabela modeli postaci [산손베르길리우스] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산손베르길리우스].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Tabela modeli postaci [바리] — nazwa] 바리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=바리].name
   limit: do 40 znaków
   EN: Bari
   PL: Bari
539. [Tabela modeli postaci [바리] — przydomek / oznaczenie] 하얀 달의 기사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=바리].nickName
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Tabela modeli postaci [이발사하편] — nazwa] 이발사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사하편].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Tabela modeli postaci [이발사하편] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사하편].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Tabela modeli postaci [신부하편] — nazwa] 신부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부하편].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Tabela modeli postaci [신부하편] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부하편].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Tabela modeli postaci [돌시네아하편] — nazwa] 돌시네아
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시네아하편].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Tabela modeli postaci [돌시네아하편] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시네아하편].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Tabela modeli postaci [돌시부하3] — nazwa] 돌시부하3
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시부하3].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Podwładny Dulcynei 3
547. [Tabela modeli postaci [돌시부하3] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돌시부하3].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Tabela modeli postaci [마을주민1] — nazwa] 마을 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마을주민1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mieszkaniec Wioski
549. [Tabela modeli postaci [마을주민1] — przydomek / oznaczenie] 양떼 목장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마을주민1].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Ranczo Pasterskie
550. [Tabela modeli postaci [장미침식혈귀] — nazwa] 침식된 혈귀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=장미침식혈귀].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Skaziony Krwiołak
551. [Tabela modeli postaci [장미침식혈귀] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=장미침식혈귀].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Tabela modeli postaci [장미침식까미유] — nazwa] 까미유?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=장미침식까미유].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Camille?
553. [Tabela modeli postaci [장미침식까미유] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=장미침식까미유].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Tabela modeli postaci [산초피묻음] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산초피묻음].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Tabela modeli postaci [산초피묻음] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=산초피묻음].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Tabela modeli postaci [돈키호테피묻음] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테피묻음].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Tabela modeli postaci [돈키호테피묻음] — przydomek / oznaczenie] 3번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테피묻음].nickName
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Tabela modeli postaci [로시난테] — nazwa] 로시난테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로시난테].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Rocinante
559. [Tabela modeli postaci [로시난테] — przydomek / oznaczenie] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로시난테].nickName
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Tabela modeli postaci [돈키호테산초] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테산초].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Tabela modeli postaci [돈키호테산초] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테산초].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Tabela modeli postaci [이발사다침2] — nazwa] 이발사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사다침2].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Tabela modeli postaci [이발사다침2] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이발사다침2].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Tabela modeli postaci [신부다침2] — nazwa] 신부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부다침2].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Tabela modeli postaci [신부다침2] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부다침2].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Tabela modeli postaci [돈키호테산초2] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테산초2].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Tabela modeli postaci [돈키호테산초2] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테산초2].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Tabela modeli postaci [키호테빛] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=키호테빛].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Tabela modeli postaci [키호테빛] — przydomek / oznaczenie] 라만차랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=키호테빛].nickName
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Tabela modeli postaci [옛산초2] — nazwa] 산초
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옛산초2].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Tabela modeli postaci [옛산초2] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=옛산초2].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Tabela modeli postaci [단테3] — nazwa] 단테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테3].name
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Tabela modeli postaci [단테3] — przydomek / oznaczenie] 관리자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=단테3].nickName
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Tabela modeli postaci [호엔하임] — nazwa] 호엔하임
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임].name
   limit: do 40 znaków
   EN: Hohenheim
   PL: Hohenheim
575. [Tabela modeli postaci [호엔하임] — przydomek / oznaczenie] LCE 연구팀 수석
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임].nickName
   limit: do 40 znaków
   EN: LCE Research Team Chief
   PL: Szef Zespołu Badawczego LCE
576. [Tabela modeli postaci [호엔하임과거] — nazwa] 호엔하임
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임과거].name
   (powtórzenie elementu 574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Tabela modeli postaci [호엔하임과거] — przydomek / oznaczenie] L사 지부 지휘팀장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임과거].nickName
   limit: do 50 znaków
   EN: L Corp. Branch Control Team Chief
   PL: Szef Zespołu Kontroli Oddziału L Corp.
578. [Tabela modeli postaci [알리사] — nazwa] 알리사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알리사].name
   limit: do 40 znaków
   EN: Alyssa
   PL: Alyssa
579. [Tabela modeli postaci [알리사] — przydomek / oznaczenie] LCE 연구팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알리사].nickName
   limit: do 40 znaków
   EN: LCE Research Team
   PL: Zespół Badawczy LCE
580. [Tabela modeli postaci [마튼] — nazwa] 마튼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마튼].name
   limit: do 40 znaków
   EN: Marton
   PL: Marton
581. [Tabela modeli postaci [마튼] — przydomek / oznaczenie] LCE 연구팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마튼].nickName
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Tabela modeli postaci [호엔과거동료] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔과거동료].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Tabela modeli postaci [호엔과거동료] — przydomek / oznaczenie] L사 지부 지휘팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔과거동료].nickName
   limit: do 40 znaków
   EN: L Corp. Branch Control Team
   PL: Zespół Kontroli Oddziału L Corp.
584. [Tabela modeli postaci [뒤틀린호엔하임] — nazwa] 뒤틀린 호엔하임
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린호엔하임].name
   limit: do 40 znaków
   EN: Distorted Hohenheim
   PL: Wypaczony Hohenheim
585. [Tabela modeli postaci [뒤틀린호엔하임] — przydomek / oznaczenie] LCE 연구팀 수석?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린호엔하임].nickName
   limit: do 40 znaków
   EN: LCE Research Team Chief?
   PL: Szef Zespołu Badawczego LCE?
586. [Tabela modeli postaci [검열된직원] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검열된직원].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Tabela modeli postaci [검열된직원] — przydomek / oznaczenie] L사 지부 지휘팀?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검열된직원].nickName
   limit: do 40 znaków
   EN: L Corp. Branch Control Team?
   PL: Zespół Kontroli Oddziału L Corp.?
588. [Tabela modeli postaci [검열된호엔과거동료] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검열된호엔과거동료].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Tabela modeli postaci [검열된호엔과거동료] — przydomek / oznaczenie] L사 지부 지휘팀?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검열된호엔과거동료].nickName
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Tabela modeli postaci [호엔하임실루엣] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임실루엣].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Tabela modeli postaci [호엔하임실루엣] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임실루엣].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Tabela modeli postaci [후디히스] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=후디히스].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Tabela modeli postaci [후디히스] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=후디히스].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Tabela modeli postaci [베르길파우] — nazwa] 베르길파우
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길파우].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Vergili-Paul
595. [Tabela modeli postaci [혈귀목소리] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀목소리].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Tabela modeli postaci [혈귀목소리] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=혈귀목소리].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Tabela modeli postaci [호엔과거동료그림자] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔과거동료그림자].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Tabela modeli postaci [호엔과거동료그림자] — przydomek / oznaczenie] L사 지부 지휘팀?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔과거동료그림자].nickName
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Tabela modeli postaci [다친베르길리우스] — nazwa] 베르길리우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친베르길리우스].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Tabela modeli postaci [다친베르길리우스] — przydomek / oznaczenie] 길잡이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친베르길리우스].nickName
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Tabela modeli postaci [뉴파일럿] — nazwa] 파일럿
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴파일럿].name
   limit: do 40 znaków
   EN: Pilot
   PL: Pilot
602. [Tabela modeli postaci [뉴파일럿] — przydomek / oznaczenie] LCCB
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴파일럿].nickName
   limit: do 40 znaków
   EN: LCCB
   PL: LCCB
603. [Tabela modeli postaci [뉴소드] — nazwa] 소드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴소드].name
   limit: do 40 znaków
   EN: Saude
   PL: Saude
604. [Tabela modeli postaci [뉴소드] — przydomek / oznaczenie] LCCB 과장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴소드].nickName
   limit: do 40 znaków
   EN: LCCB Manager
   PL: Kierownik LCCB
605. [Tabela modeli postaci [리카르도다침] — nazwa] 리카르도
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=리카르도다침].name
   limit: do 40 znaków
   EN: Ricardo
   PL: Ricardo
606. [Tabela modeli postaci [리카르도다침] — przydomek / oznaczenie] 중지 작은 형님
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=리카르도다침].nickName
   limit: do 40 znaków
   EN: The Middle's Big Brother
   PL: Starszy Brat z The Middle
607. [Tabela modeli postaci [사이화] — nazwa] 사이화
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사이화].name
   limit: do 40 znaków
   EN: Shi Yihua
   PL: Shi Yihua
608. [Tabela modeli postaci [사이화] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사이화].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Tabela modeli postaci [경도] — nazwa] 경도
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=경도].name
   limit: do 40 znaków
   EN: Qingtao
   PL: Qingtao
610. [Tabela modeli postaci [경도] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=경도].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Tabela modeli postaci [삼삼] — nazwa] 삼삼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=삼삼].name
   limit: do 40 znaków
   EN: Shan San
   PL: Shan San
612. [Tabela modeli postaci [삼삼] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=삼삼].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Tabela modeli postaci [삼삼다침] — nazwa] 삼삼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=삼삼다침].name
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Tabela modeli postaci [삼삼다침] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=삼삼다침].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Tabela modeli postaci [가치우] — nazwa] 가치우
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가치우].name
   limit: do 40 znaków
   EN: Jia Qiu
   PL: Jia Qiu
616. [Tabela modeli postaci [가치우] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가치우].nickName
   limit: do 40 znaków
   EN: Jia Family
   PL: Rodzina Jia
617. [Tabela modeli postaci [자로] — nazwa] 자로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로].name
   limit: do 40 znaków
   EN: Zilu
   PL: Zilu
618. [Tabela modeli postaci [자로] — przydomek / oznaczenie] 흑수-묘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로].nickName
   limit: do 40 znaków
   EN: Heishou Packs - Mao Branch
   PL: Heishou Packs - Gałąź Mao
619. [Tabela modeli postaci [흑수묘] — nazwa] 흑수묘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수묘].name
   limit: do 40 znaków
   EN: Heishou Packs - Mao Branch
   PL: Heishou Packs - Gałąź Mao
620. [Tabela modeli postaci [흑수묘] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수묘].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Tabela modeli postaci [청소부A] — nazwa] 청소부A
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=청소부A].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zbieracz A
622. [Tabela modeli postaci [청소부A] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=청소부A].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Tabela modeli postaci [청소부B] — nazwa] 청소부B
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=청소부B].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zbieracz B
624. [Tabela modeli postaci [청소부B] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=청소부B].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Tabela modeli postaci [청소부C] — nazwa] 청소부C
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=청소부C].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Zbieracz C
626. [Tabela modeli postaci [청소부C] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=청소부C].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Tabela modeli postaci [로쟈싱클] — nazwa] 로쟈 & 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈싱클].name
   limit: do 40 znaków
   EN: Rodion & Sinclair
   PL: Rodion i Sinclair
628. [Tabela modeli postaci [로쟈싱클] — przydomek / oznaczenie] LCB
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈싱클].nickName
   limit: do 40 znaków
   EN: LCB
   PL: LCB
629. [Tabela modeli postaci [자공] — nazwa] 자공
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자공].name
   limit: do 40 znaków
   EN: Zigong
   PL: Zigong
630. [Tabela modeli postaci [이상다침] — nazwa] 이상
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상다침].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Tabela modeli postaci [이상다침] — przydomek / oznaczenie] 1번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상다침].nickName
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Tabela modeli postaci [파우스트다침] — nazwa] 파우스트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트다침].name
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Tabela modeli postaci [파우스트다침] — przydomek / oznaczenie] 2번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트다침].nickName
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Tabela modeli postaci [료슈다침] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈다침].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Tabela modeli postaci [료슈다침] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈다침].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Tabela modeli postaci [뫼르소다침] — nazwa] 뫼르소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소다침].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Tabela modeli postaci [뫼르소다침] — przydomek / oznaczenie] 5번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소다침].nickName
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Tabela modeli postaci [홍루다침] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루다침].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Tabela modeli postaci [홍루다침] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루다침].nickName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Tabela modeli postaci [히스클리프다침2] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프다침2].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Tabela modeli postaci [히스클리프다침2] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프다침2].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Tabela modeli postaci [이스마엘다침] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘다침].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Tabela modeli postaci [이스마엘다침] — przydomek / oznaczenie] 8번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘다침].nickName
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Tabela modeli postaci [로쟈다침] — nazwa] 로쟈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈다침].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Tabela modeli postaci [로쟈다침] — przydomek / oznaczenie] 9번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈다침].nickName
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Tabela modeli postaci [싱클레어다침] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어다침].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Tabela modeli postaci [싱클레어다침] — przydomek / oznaczenie] 11번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어다침].nickName
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Tabela modeli postaci [오티스다침] — nazwa] 오티스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스다침].name
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Tabela modeli postaci [오티스다침] — przydomek / oznaczenie] 12번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스다침].nickName
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Tabela modeli postaci [그레고르다침] — nazwa] 그레고르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르다침].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Tabela modeli postaci [그레고르다침] — przydomek / oznaczenie] 13번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르다침].nickName
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Tabela modeli postaci [베르너] — nazwa] 베르너
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르너].name
   limit: do 40 znaków
   EN: Werner
   PL: Werner
653. [Tabela modeli postaci [베르너] — przydomek / oznaczenie] 중지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르너].nickName
   limit: do 40 znaków
   EN: The Middle
   PL: The Middle
654. [Tabela modeli postaci [베르너다침] — nazwa] 베르너
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르너다침].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Werner
655. [Tabela modeli postaci [베르너다침] — przydomek / oznaczenie] 중지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르너다침].nickName
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Tabela modeli postaci [이스마엘F] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘F].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Tabela modeli postaci [이스마엘F] — przydomek / oznaczenie] 8번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘F].nickName
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Tabela modeli postaci [그레고르F] — nazwa] 그레고르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르F].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Tabela modeli postaci [그레고르F] — przydomek / oznaczenie] 13번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르F].nickName
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Tabela modeli postaci [료슈F] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈F].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Tabela modeli postaci [료슈F] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈F].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Tabela modeli postaci [가모] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모].name
   limit: do 40 znaków
   EN: Jia Mu
   PL: Jia Mu
663. [Tabela modeli postaci [가모] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모].nickName
   limit: do 40 znaków
   EN: The Hierarch of Hongyuan
   PL: Hierarcha Hongyuan
664. [Tabela modeli postaci [어린홍루] — nazwa] 가보옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린홍루].name
   limit: do 40 znaków
   EN: Jia Baoyu
   PL: Jia Baoyu
665. [Tabela modeli postaci [어린홍루] — przydomek / oznaczenie] 가씨 가문의 보석
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린홍루].nickName
   limit: do 40 znaków
   EN: Gem of the Jia Family
   PL: Klejnot Rodziny Jia
666. [Tabela modeli postaci [뇌횡] — nazwa] 뇌횡
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뇌횡].name
   limit: do 40 znaków
   EN: Lei Heng
   PL: Lei Heng
667. [Tabela modeli postaci [뇌횡] — przydomek / oznaczenie] 엄지 카포ⅠⅠⅠⅠ
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뇌횡].nickName
   limit: do 40 znaków
   EN: The Thumb's Capo ⅠⅠⅠⅠ
   PL: CapoⅠⅠⅠⅠ The Thumb
668. [Tabela modeli postaci [어린가환] — nazwa] 가환
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환].name
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Tabela modeli postaci [어린가환] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Tabela modeli postaci [임대옥] — nazwa] 임대옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임대옥].name
   limit: do 40 znaków
   EN: Lin Daiyu
   PL: Lin Daiyu
671. [Tabela modeli postaci [임대옥] — przydomek / oznaczenie] 보차 세가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임대옥].nickName
   limit: do 40 znaków
   EN: Baochai's Clan
   PL: Klan Baochai
672. [Tabela modeli postaci [어린임대옥] — nazwa] 임대옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린임대옥].name
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Tabela modeli postaci [어린임대옥] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린임대옥].nickName
   limit: do 40 znaków
   EN: Kong Family
   PL: Rodzina Kong
674. [Tabela modeli postaci [설보차] — nazwa] 설보차
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설보차].name
   limit: do 40 znaków
   EN: Xue Baochai
   PL: Xue Baochai
675. [Tabela modeli postaci [설보차] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설보차].nickName
   limit: do 40 znaków
   EN: Xue Family
   PL: Rodzina Xue
676. [Tabela modeli postaci [로쟈&히스] — nazwa] 로쟈 & 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈&히스].name
   limit: do 40 znaków
   EN: Rodion&Heathcliff
   PL: Rodion i Heathcliff
677. [Tabela modeli postaci [로쟈&히스] — przydomek / oznaczenie] LCB
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈&히스].nickName
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Tabela modeli postaci [습인] — nazwa] 습인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=습인].name
   limit: do 40 znaków
   EN: Xiren
   PL: Xiren
679. [Tabela modeli postaci [습인] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=습인].nickName
   limit: do 40 znaków
   EN: Daguanyuan
   PL: Daguanyuan
680. [Tabela modeli postaci [습인과거] — nazwa] 습인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=습인과거].name
   (powtórzenie elementu 678 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Tabela modeli postaci [습인과거] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=습인과거].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Tabela modeli postaci [가원춘] — nazwa] 가원춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가원춘].name
   limit: do 40 znaków
   EN: Jia Yuanchun
   PL: Jia Yuanchun
683. [Tabela modeli postaci [가원춘] — przydomek / oznaczenie] Q사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가원춘].nickName
   limit: do 40 znaków
   EN: Q Corp.
   PL: Q Corp.
684. [Tabela modeli postaci [왕부인] — nazwa] 왕부인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕부인].name
   limit: do 40 znaków
   EN: Lady Wang
   PL: Lady Wang
685. [Tabela modeli postaci [왕부인] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕부인].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Tabela modeli postaci [가정] — nazwa] 가정
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가정].name
   limit: do 40 znaków
   EN: Jia Zheng
   PL: Jia Zheng
687. [Tabela modeli postaci [가정] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가정].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Tabela modeli postaci [설반] — nazwa] 설반
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설반].name
   limit: do 40 znaków
   EN: Xue Pan
   PL: Xue Pan
689. [Tabela modeli postaci [설반] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설반].nickName
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Tabela modeli postaci [취수야객] — nazwa] 취수야객
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=취수야객].name
   limit: do 40 znaków
   EN: Night Drifter
   PL: Pijanica Nocny Wędrowiec
691. [Tabela modeli postaci [취수야객] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=취수야객].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Tabela modeli postaci [가마꾼] — nazwa] 가마꾼
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가마꾼].name
   limit: do 40 znaków
   EN: Palanquin Bearer
   PL: Tragarz Palanki
693. [Tabela modeli postaci [가마꾼] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가마꾼].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Tabela modeli postaci [항아리괴물] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=항아리괴물].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Tabela modeli postaci [항아리괴물] — przydomek / oznaczenie] 항아리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=항아리괴물].nickName
   limit: do 40 znaków
   EN: Jar
   PL: Dzban
696. [Tabela modeli postaci [어린가시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가시춘].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Tabela modeli postaci [어린가시춘] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가시춘].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Tabela modeli postaci [하인1] — nazwa] 과묵한 하인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인1].name
   limit: do 40 znaków
   EN: Reticent Servant
   PL: Milczący Służący
699. [Tabela modeli postaci [하인1] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인1].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Tabela modeli postaci [하인2] — nazwa] 반듯한 하인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인2].name
   limit: do 40 znaków
   EN: Refined Servant
   PL: Ogładany Służący
701. [Tabela modeli postaci [하인2] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인2].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Tabela modeli postaci [하인3] — nazwa] 공손한 하인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인3].name
   limit: do 40 znaków
   EN: Polite Servant
   PL: Uprzejmy Służący
703. [Tabela modeli postaci [하인3] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인3].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Tabela modeli postaci [하인4] — nazwa] 무심한 하인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인4].name
   limit: do 40 znaków
   EN: Indifferent Servant
   PL: Obojętny Służący
705. [Tabela modeli postaci [하인4] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인4].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Tabela modeli postaci [괴한] — nazwa] 괴한
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=괴한].name
   limit: do 40 znaków
   EN: Stranger
   PL: Nieznajomy
707. [Tabela modeli postaci [괴한] — przydomek / oznaczenie] 홍원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=괴한].nickName
   limit: do 40 znaków
   EN: Hongyuan
   PL: Hongyuan
708. [Tabela modeli postaci [알란] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알란].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Tabela modeli postaci [알란] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=알란].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Tabela modeli postaci [하나후다] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하나후다].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Tabela modeli postaci [하나후다] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하나후다].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Tabela modeli postaci [흑수들] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수들].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Tabela modeli postaci [흑수들] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수들].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Tabela modeli postaci [흑수계] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수계].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Tabela modeli postaci [흑수계] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수계].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Tabela modeli postaci [흑수계2] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수계2].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Tabela modeli postaci [흑수계2] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수계2].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Tabela modeli postaci [피주머니2] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피주머니2].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Tabela modeli postaci [피주머니2] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=피주머니2].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Tabela modeli postaci [에고가환] — nazwa] 가환
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고가환].name
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Tabela modeli postaci [에고가환] — przydomek / oznaczenie] N사-신구인회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고가환].nickName
   limit: do 60 znaków
   EN: N Corp. New League of Nine Littérateurs
   PL: N Corp. — Nowa Liga Dziewięciu Literatów
722. [Tabela modeli postaci [과거가환] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거가환].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Tabela modeli postaci [과거가환] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거가환].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Tabela modeli postaci [에고구보] — nazwa] 구보
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고구보].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Tabela modeli postaci [에고구보] — przydomek / oznaczenie] N사-신구인회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고구보].nickName
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Tabela modeli postaci [왕대위] — nazwa] 왕대위
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕대위].name
   limit: do 40 znaków
   EN: Wang Dawei
   PL: Wang Dawei
727. [Tabela modeli postaci [왕대위] — przydomek / oznaczenie] 왕씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕대위].nickName
   limit: do 40 znaków
   EN: Wang Family
   PL: Rodzina Wang
728. [Tabela modeli postaci [왕인] — nazwa] 왕인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕인].name
   limit: do 40 znaków
   EN: Wang Ren
   PL: Wang Ren
729. [Tabela modeli postaci [왕인] — przydomek / oznaczenie] 왕씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕인].nickName
   (powtórzenie elementu 727 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Tabela modeli postaci [과거홍루] — nazwa] 가보옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거홍루].name
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Tabela modeli postaci [과거홍루] — przydomek / oznaczenie] 가씨 가문의 보석
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거홍루].nickName
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Tabela modeli postaci [료슈2] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈2].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Tabela modeli postaci [료슈2] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈2].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Tabela modeli postaci [반시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=반시춘].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Tabela modeli postaci [반시춘] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=반시춘].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Tabela modeli postaci [사회자] — nazwa] 사회자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사회자].name
   limit: do 40 znaków
   EN: Host
   PL: Prowadzący
737. [Tabela modeli postaci [사회자] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사회자].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Tabela modeli postaci [과거가모] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거가모].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Tabela modeli postaci [과거가모] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거가모].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Tabela modeli postaci [과거가치우] — nazwa] 가치우
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거가치우].name
   (powtórzenie elementu 615 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Tabela modeli postaci [과거가치우] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거가치우].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Tabela modeli postaci [공우진] — nazwa] 공우진
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공우진].name
   limit: do 40 znaków
   EN: Kong Youjin
   PL: Kong Youjin
743. [Tabela modeli postaci [공우진] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공우진].nickName
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Tabela modeli postaci [공사혜] — nazwa] 공사혜
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공사혜].name
   limit: do 40 znaków
   EN: Kong Sihui
   PL: Kong Sihui
745. [Tabela modeli postaci [공사혜] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공사혜].nickName
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Tabela modeli postaci [공사혜아기] — nazwa] 공사혜
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공사혜아기].name
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Tabela modeli postaci [공사혜아기] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공사혜아기].nickName
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Tabela modeli postaci [조길인] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=조길인].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Tabela modeli postaci [조길인] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=조길인].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Tabela modeli postaci [왕자우] — nazwa] 왕자우
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕자우].name
   limit: do 40 znaków
   EN: Wang Zhao
   PL: Wang Zhao
751. [Tabela modeli postaci [왕자우] — przydomek / oznaczenie] 왕씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕자우].nickName
   (powtórzenie elementu 727 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Tabela modeli postaci [사화정] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사화정].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Tabela modeli postaci [사화정] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사화정].nickName
   limit: do 40 znaków
   EN: Shi Family
   PL: Rodzina Shi
754. [Tabela modeli postaci [사화정다침] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사화정다침].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Tabela modeli postaci [사화정다침] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사화정다침].nickName
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Tabela modeli postaci [사사정] — nazwa] 사사정
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사사정].name
   limit: do 40 znaków
   EN: Shi Sijing
   PL: Shi Sijing
757. [Tabela modeli postaci [사사정] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사사정].nickName
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Tabela modeli postaci [다친사사정] — nazwa] 사사정
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친사사정].name
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Tabela modeli postaci [다친사사정] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친사사정].nickName
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Tabela modeli postaci [대관원사람] — nazwa] 불안해하는 사람
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=대관원사람].name
   limit: do 40 znaków
   EN: Nervous Stranger
   PL: Zaniepokojony Nieznajomy
761. [Tabela modeli postaci [대관원사람] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=대관원사람].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Tabela modeli postaci [죄수] — nazwa] 홍원의 죄수
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=죄수].name
   limit: do 40 znaków
   EN: Prisoner of Hongyuan
   PL: Więzień Hongyuan
763. [Tabela modeli postaci [죄수] — przydomek / oznaczenie] 홍원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=죄수].nickName
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Tabela modeli postaci [죄수과거] — nazwa] 홍원의 죄수
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=죄수과거].name
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Tabela modeli postaci [죄수과거] — przydomek / oznaczenie] 홍원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=죄수과거].nickName
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Tabela modeli postaci [가리온] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가리온].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Tabela modeli postaci [가리온] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가리온].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Tabela modeli postaci [발톱] — nazwa] 발톱
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=발톱].name
   limit: do 40 znaków
   EN: Claw
   PL: Szpon
769. [Tabela modeli postaci [발톱] — przydomek / oznaczenie] 머리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=발톱].nickName
   limit: do 40 znaków
   EN: The Head
   PL: Głowa
770. [Tabela modeli postaci [임대옥다침] — nazwa] 임대옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임대옥다침].name
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Tabela modeli postaci [임대옥다침] — przydomek / oznaczenie] 보차 세가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임대옥다침].nickName
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Tabela modeli postaci [공씨사람1] — nazwa] 반발하는 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공씨사람1].name
   limit: do 40 znaków
   EN: Obstinate Resident
   PL: Oporny Mieszkaniec
773. [Tabela modeli postaci [공씨사람1] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공씨사람1].nickName
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Tabela modeli postaci [공씨사람1다침] — nazwa] 반발하는 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공씨사람1다침].name
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Tabela modeli postaci [공씨사람1다침] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공씨사람1다침].nickName
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Tabela modeli postaci [공씨사람2] — nazwa] 의아해하는 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공씨사람2].name
   limit: do 40 znaków
   EN: Curious Resident
   PL: Zaintrygowany Mieszkaniec
777. [Tabela modeli postaci [공씨사람2] — przydomek / oznaczenie] 공씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=공씨사람2].nickName
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Tabela modeli postaci [어린가환다침] — nazwa] 가환
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환다침].name
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Tabela modeli postaci [어린가환다침] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환다침].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Tabela modeli postaci [어린가환다침2] — nazwa] 가환
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환다침2].name
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Tabela modeli postaci [어린가환다침2] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환다침2].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Tabela modeli postaci [어린가환죽음] — nazwa] 가환
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환죽음].name
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Tabela modeli postaci [어린가환죽음] — przydomek / oznaczenie] 가씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린가환죽음].nickName
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Tabela modeli postaci [H사직원] — nazwa] H사 연구원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=H사직원].name
   limit: do 40 znaków
   EN: H Corp. Researcher
   PL: Badacz H Corp.
785. [Tabela modeli postaci [H사직원] — przydomek / oznaczenie] 홍원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=H사직원].nickName
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Tabela modeli postaci [에고구보총] — nazwa] 구보
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고구보총].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Tabela modeli postaci [에고구보총] — przydomek / oznaczenie] N사-신구인회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고구보총].nickName
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Tabela modeli postaci [왕청산] — nazwa] 왕청산
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕청산].name
   limit: do 40 znaków
   EN: Wang Qingshan
   PL: Wang Qingshan
789. [Tabela modeli postaci [왕청산] — przydomek / oznaczenie] 왕씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕청산].nickName
   (powtórzenie elementu 727 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Tabela modeli postaci [설반다침] — nazwa] 설반
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설반다침].name
   (powtórzenie elementu 688 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Tabela modeli postaci [설반다침] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설반다침].nickName
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Tabela modeli postaci [어린설반] — nazwa] 설반
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린설반].name
   (powtórzenie elementu 688 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Tabela modeli postaci [어린설반] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린설반].nickName
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Tabela modeli postaci [발톱죽임] — nazwa] 발톱
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=발톱죽임].name
   (powtórzenie elementu 768 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Tabela modeli postaci [발톱죽임] — przydomek / oznaczenie] 머리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=발톱죽임].nickName
   (powtórzenie elementu 769 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Tabela modeli postaci [사이화부활] — nazwa] 사이화
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사이화부활].name
   (powtórzenie elementu 607 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Tabela modeli postaci [사이화부활] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사이화부활].nickName
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Tabela modeli postaci [다친가시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친가시춘].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Tabela modeli postaci [다친가시춘] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친가시춘].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Tabela modeli postaci [어린홍루과거홍루] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린홍루과거홍루].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Tabela modeli postaci [어린홍루과거홍루] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린홍루과거홍루].nickName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Tabela modeli postaci [어린홍루홍루] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린홍루홍루].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Tabela modeli postaci [어린홍루홍루] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어린홍루홍루].nickName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Tabela modeli postaci [다친홍루] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친홍루].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Tabela modeli postaci [다친홍루] — przydomek / oznaczenie] 6번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친홍루].nickName
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Tabela modeli postaci [사씨사병1] — nazwa] 사씨 사병 1
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사씨사병1].name
   limit: do 40 znaków
   EN: Shi Family Footsoldier 1
   PL: Żołnierz Rodziny Shi 1
807. [Tabela modeli postaci [사씨사병1] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사씨사병1].nickName
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Tabela modeli postaci [사씨사병2] — nazwa] 사씨 사병 2
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사씨사병2].name
   limit: do 40 znaków
   EN: Shi Family Footsoldier 2
   PL: Żołnierz Rodziny Shi 2
809. [Tabela modeli postaci [사씨사병2] — przydomek / oznaczenie] 사씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=사씨사병2].nickName
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Tabela modeli postaci [설씨사병네임드] — nazwa] 설씨 가문 사병 수장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설씨사병네임드].name
   limit: do 40 znaków
   EN: Xue Family Captain
   PL: Dowódca Żołnierzy Rodziny Xue
811. [Tabela modeli postaci [설씨사병네임드] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설씨사병네임드].nickName
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Tabela modeli postaci [설씨사병1] — nazwa] 설씨 가문 사병
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설씨사병1].name
   limit: do 40 znaków
   EN: Xue Family Footsoldier
   PL: Żołnierz Rodziny Xue
813. [Tabela modeli postaci [설씨사병1] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설씨사병1].nickName
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Tabela modeli postaci [설씨하인] — nazwa] 설씨 가문 하인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설씨하인].name
   limit: do 40 znaków
   EN: Xue Family Servant
   PL: Służący Rodziny Xue
815. [Tabela modeli postaci [설씨하인] — przydomek / oznaczenie] 설씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=설씨하인].nickName
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Tabela modeli postaci [어르신그림자] — nazwa] 어르신들
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신그림자].name
   limit: do 40 znaków
   EN: Elders
   PL: Starusze
817. [Tabela modeli postaci [어르신그림자] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신그림자].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Tabela modeli postaci [어르신1] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신1].name
   limit: do 40 znaków
   EN: Elder
   PL: Staruszek
819. [Tabela modeli postaci [어르신1] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신1].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Tabela modeli postaci [어르신2] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신2].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Tabela modeli postaci [어르신2] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신2].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Tabela modeli postaci [어르신3] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신3].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Tabela modeli postaci [어르신3] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신3].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Tabela modeli postaci [어르신4] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신4].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Tabela modeli postaci [어르신4] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신4].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Tabela modeli postaci [어르신5] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신5].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Tabela modeli postaci [어르신5] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신5].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Tabela modeli postaci [어르신6] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신6].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Tabela modeli postaci [어르신6] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신6].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Tabela modeli postaci [어르신1그림자] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신1그림자].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Tabela modeli postaci [어르신1그림자] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신1그림자].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Tabela modeli postaci [어르신2그림자] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신2그림자].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Tabela modeli postaci [어르신2그림자] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신2그림자].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Tabela modeli postaci [어르신3그림자] — nazwa] 어르신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신3그림자].name
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Tabela modeli postaci [어르신3그림자] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=어르신3그림자].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Tabela modeli postaci [엄지솔다토1] — nazwa] 엄지 조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지솔다토1].name
   limit: do 40 znaków
   EN: The Thumb Henchman
   PL: Pachołek The Thumb
837. [Tabela modeli postaci [엄지솔다토1] — przydomek / oznaczenie] 솔다토ⅠⅠ
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지솔다토1].nickName
   limit: do 40 znaków
   EN: Soldato ⅠⅠ
   PL: SoldatoⅠⅠ
838. [Tabela modeli postaci [엄지솔다토2] — nazwa] 엄지 조직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지솔다토2].name
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Tabela modeli postaci [엄지솔다토2] — przydomek / oznaczenie] 솔다토ⅠⅠⅠ
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지솔다토2].nickName
   limit: do 40 znaków
   EN: Soldato ⅠⅠⅠ
   PL: SoldatoⅠⅠⅠ
840. [Tabela modeli postaci [가모충] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모충].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Tabela modeli postaci [가모충] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모충].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Tabela modeli postaci [가모롱] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모롱].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Tabela modeli postaci [가모롱] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모롱].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Tabela modeli postaci [가모가지] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모가지].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Tabela modeli postaci [가모가지] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모가지].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Tabela modeli postaci [가모괴물] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모괴물].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Tabela modeli postaci [가모괴물] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모괴물].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Tabela modeli postaci [자로피] — nazwa] 자로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로피].name
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Tabela modeli postaci [자로피] — przydomek / oznaczenie] 흑수-묘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로피].nickName
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Tabela modeli postaci [자로피2] — nazwa] 자로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로피2].name
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Tabela modeli postaci [자로피2] — przydomek / oznaczenie] 흑수-묘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로피2].nickName
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Tabela modeli postaci [하인죽음] — nazwa] 괴로워하는 하인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인죽음].name
   limit: do 40 znaków
   EN: Suffering Attendant
   PL: Cierpiący Służący
853. [Tabela modeli postaci [하인죽음] — przydomek / oznaczenie] 대관원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=하인죽음].nickName
   (powtórzenie elementu 679 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Tabela modeli postaci [가모가지꽂음] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모가지꽂음].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Tabela modeli postaci [가모가지꽂음] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모가지꽂음].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Tabela modeli postaci [더어린홍루] — nazwa] 가보옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=더어린홍루].name
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Tabela modeli postaci [더어린홍루] — przydomek / oznaczenie] 가씨 가문의 보석
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=더어린홍루].nickName
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Tabela modeli postaci [다친뇌횡] — nazwa] 뇌횡
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친뇌횡].name
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Tabela modeli postaci [다친뇌횡] — przydomek / oznaczenie] 엄지 카포ⅠⅠⅠⅠ
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친뇌횡].nickName
   (powtórzenie elementu 667 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Tabela modeli postaci [임대옥다침2] — nazwa] 임대옥
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임대옥다침2].name
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Tabela modeli postaci [임대옥다침2] — przydomek / oznaczenie] 보차 세가
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임대옥다침2].nickName
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Tabela modeli postaci [다친가시춘2] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친가시춘2].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Tabela modeli postaci [다친가시춘2] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친가시춘2].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Tabela modeli postaci [가모괴물다침] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모괴물다침].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Tabela modeli postaci [가모괴물다침] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모괴물다침].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Tabela modeli postaci [가모괴물씻김] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모괴물씻김].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Tabela modeli postaci [가모괴물씻김] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모괴물씻김].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Tabela modeli postaci [가모롱다침] — nazwa] 가모
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모롱다침].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Tabela modeli postaci [가모롱다침] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가모롱다침].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Tabela modeli postaci [뇌횡다침2] — nazwa] 뇌횡
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뇌횡다침2].name
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Tabela modeli postaci [뇌횡다침2] — przydomek / oznaczenie] 엄지 카포ⅠⅠⅠⅠ
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뇌횡다침2].nickName
   (powtórzenie elementu 667 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Tabela modeli postaci [티페리트] — nazwa] 티페리트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=티페리트].name
   limit: do 40 znaków
   EN: Tiphereth
   PL: Tiphereth
873. [Tabela modeli postaci [퀴즈시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴즈시춘].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Tabela modeli postaci [퀴즈시춘] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴즈시춘].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Tabela modeli postaci [퀴즈싱클] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴즈싱클].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Tabela modeli postaci [퀴즈싱클] — przydomek / oznaczenie] 11번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퀴즈싱클].nickName
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Tabela modeli postaci [뿅망히스] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뿅망히스].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Tabela modeli postaci [뿅망히스] — przydomek / oznaczenie] 7번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뿅망히스].nickName
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Tabela modeli postaci [폭주웨이] — nazwa] 웨이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=폭주웨이].name
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Tabela modeli postaci [폭주웨이] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=폭주웨이].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Tabela modeli postaci [왕청산2] — nazwa] 왕청산
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕청산2].name
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Tabela modeli postaci [왕청산2] — przydomek / oznaczenie] 왕씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕청산2].nickName
   (powtórzenie elementu 727 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Tabela modeli postaci [자로사복] — nazwa] 자로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로사복].name
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Tabela modeli postaci [자로사복] — przydomek / oznaczenie] 소지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=자로사복].nickName
   limit: do 40 znaków
   EN: The Pinky
   PL: Mały Palec
885. [Tabela modeli postaci [불량시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=불량시춘].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Tabela modeli postaci [불량시춘] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=불량시춘].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Tabela modeli postaci [이상그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상그림자].name
   limit: do 40 znaków
   EN: Anonymous
   PL: Anonim
888. [Tabela modeli postaci [파우스트그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Tabela modeli postaci [돈키호테그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Tabela modeli postaci [료슈그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Tabela modeli postaci [뫼르소그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Tabela modeli postaci [홍루그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Tabela modeli postaci [히스클리프그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Tabela modeli postaci [이스마엘그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Tabela modeli postaci [로쟈그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Tabela modeli postaci [싱클레어그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Tabela modeli postaci [오티스그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Tabela modeli postaci [그레고르그림자] — nazwa] 익명
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르그림자].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Tabela modeli postaci [흑수사] — nazwa] 흑수-사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수사].name
   limit: do 40 znaków
   EN: Heishou Pack - Si Branch
   PL: Heishou Pack - Gałąź Si
900. [Tabela modeli postaci [흑수사] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=흑수사].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Tabela modeli postaci [료슈3] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈3].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Tabela modeli postaci [료슈3] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈3].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Tabela modeli postaci [왕씨아이] — nazwa] 왕씨 아이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕씨아이].name
   limit: do 40 znaków
   EN: Wang Family Child
   PL: Dziecko Rodziny Wang
904. [Tabela modeli postaci [왕씨아이] — przydomek / oznaczenie] 왕씨 가문
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=왕씨아이].nickName
   (powtórzenie elementu 727 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Tabela modeli postaci [쩔쩔이사] — nazwa] 쩔쩔매는 이사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=쩔쩔이사].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Nieporadny Dyrektor
906. [Tabela modeli postaci [굽신이사] — nazwa] 굽신대는 이사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=굽신이사].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Przypodlakiwający Dyrektor
907. [Tabela modeli postaci [웨이다침2] — nazwa] 웨이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=웨이다침2].name
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Tabela modeli postaci [웨이다침2] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=웨이다침2].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Tabela modeli postaci [가주시춘] — nazwa] 가시춘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가주시춘].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Tabela modeli postaci [가주시춘] — przydomek / oznaczenie] 홍원의 가주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=가주시춘].nickName
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Tabela modeli postaci [아미야] — nazwa] 아미야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아미야].name
   limit: do 40 znaków
   EN: Amiya
   PL: Amiya
912. [Tabela modeli postaci [아미야] — przydomek / oznaczenie] 로도스 아일랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아미야].nickName
   limit: do 40 znaków
   EN: Rhodes Island
   PL: Rhodes Island
913. [Tabela modeli postaci [스카디] — nazwa] 스카디
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스카디].name
   limit: do 40 znaków
   EN: Skadi
   PL: Skadi
914. [Tabela modeli postaci [스카디] — przydomek / oznaczenie] 로도스 아일랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=스카디].nickName
   (powtórzenie elementu 912 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Tabela modeli postaci [켈시] — nazwa] 켈시
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=켈시].name
   limit: do 40 znaków
   EN: Kal'tsit
   PL: Kal'tsit
916. [Tabela modeli postaci [켈시] — przydomek / oznaczenie] 로도스 아일랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=켈시].nickName
   (powtórzenie elementu 912 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Tabela modeli postaci [박사] — nazwa] 박사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=박사].name
   limit: do 40 znaków
   EN: Doctor
   PL: Doktor
918. [Tabela modeli postaci [박사] — przydomek / oznaczenie] 로도스 아일랜드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=박사].nickName
   (powtórzenie elementu 912 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Tabela modeli postaci [아이린] — nazwa] 아이린
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아이린].name
   limit: do 40 znaków
   EN: Irene
   PL: Irene
920. [Tabela modeli postaci [아이린] — przydomek / oznaczenie] 재판소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아이린].nickName
   limit: do 40 znaków
   EN: Inquisition
   PL: Inkwizycja
921. [Tabela modeli postaci [메이어스] — nazwa] 메이어스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=메이어스].name
   limit: do 40 znaków
   EN: Mayors
   PL: Mayors
922. [Tabela modeli postaci [메이어스] — przydomek / oznaczenie] 파로 무에르토
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=메이어스].nickName
   limit: do 40 znaków
   EN: Faro Muerto
   PL: Faro Muerto
923. [Tabela modeli postaci [과거메이어스] — nazwa] 메이어스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거메이어스].name
   (powtórzenie elementu 921 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Tabela modeli postaci [과거메이어스] — przydomek / oznaczenie] 에기르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거메이어스].nickName
   limit: do 40 znaków
   EN: Ægir
   PL: Ægir
925. [Tabela modeli postaci [주교메이어스] — nazwa] 메이어스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=주교메이어스].name
   (powtórzenie elementu 921 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Tabela modeli postaci [주교메이어스] — przydomek / oznaczenie] 심해 주교
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=주교메이어스].nickName
   limit: do 40 znaków
   EN: Bishop of the Church
   PL: Biskup Kościoła
927. [Tabela modeli postaci [심해신도] — nazwa] 심해 신도
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=심해신도].name
   limit: do 40 znaków
   EN: Followers of the Deep
   PL: Wyznawcy Głębin
928. [Tabela modeli postaci [심해신도] — przydomek / oznaczenie] 심해 교회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=심해신도].nickName
   limit: do 40 znaków
   EN: Church of the Deep
   PL: Kościół Głębin
929. [Tabela modeli postaci [심해신도2] — nazwa] 심해 신도
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=심해신도2].name
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Tabela modeli postaci [심해신도2] — przydomek / oznaczenie] 심해 교회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=심해신도2].nickName
   (powtórzenie elementu 928 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Tabela modeli postaci [파비우스] — nazwa] 파비우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파비우스].name
   limit: do 40 znaków
   EN: Fabius
   PL: Fabius
932. [Tabela modeli postaci [파비우스] — przydomek / oznaczenie] 심해 교회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파비우스].nickName
   (powtórzenie elementu 928 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Tabela modeli postaci [이베리아주민1] — nazwa] 마을 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이베리아주민1].name
   limit: do 40 znaków
   EN: Villager
   PL: Mieszkaniec Wioski
934. [Tabela modeli postaci [이베리아주민1] — przydomek / oznaczenie] 파로 무에르토
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이베리아주민1].nickName
   (powtórzenie elementu 922 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Tabela modeli postaci [이베리아주민2] — nazwa] 마을 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이베리아주민2].name
   (powtórzenie elementu 933 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Tabela modeli postaci [이베리아주민2] — przydomek / oznaczenie] 파로 무에르토
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이베리아주민2].nickName
   (powtórzenie elementu 922 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Tabela modeli postaci [뒤틀린메이어스] — nazwa] 선망하여 표류하는 메이어스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린메이어스].name
   limit: do 40 znaków
   EN: Mayors, the Yearning Flotsam
   PL: Mayors, Tęskniący Dryf
938. [Tabela modeli postaci [뒤틀린메이어스] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린메이어스].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Tabela modeli postaci [마지막기사] — nazwa] 마지막 기사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마지막기사].name
   limit: do 40 znaków
   EN: The Last Knight
   PL: Ostatni Rycerz
940. [Tabela modeli postaci [마지막기사] — przydomek / oznaczenie] 시본
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=마지막기사].nickName
   limit: do 40 znaków
   EN: Seaborn
   PL: Seaborn
941. [Tabela modeli postaci [시테러] — nazwa] 시테러
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시테러].name
   limit: do 40 znaków
   EN: Sea Terror
   PL: Postrach Mórz
942. [Tabela modeli postaci [시테러] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시테러].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Tabela modeli postaci [시테러들] — nazwa] 시테러
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시테러들].name
   (powtórzenie elementu 941 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Tabela modeli postaci [시테러들] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시테러들].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Tabela modeli postaci [파비우스다침] — nazwa] 파비우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파비우스다침].name
   (powtórzenie elementu 931 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Tabela modeli postaci [파비우스다침] — przydomek / oznaczenie] 심해 교회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파비우스다침].nickName
   (powtórzenie elementu 928 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Tabela modeli postaci [메이어스다침] — nazwa] 메이어스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=메이어스다침].name
   (powtórzenie elementu 921 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Tabela modeli postaci [메이어스다침] — przydomek / oznaczenie] 심해 주교
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=메이어스다침].nickName
   (powtórzenie elementu 926 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Tabela modeli postaci [엄지아비] — nazwa] 발렌치나
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지아비].name
   limit: do 40 znaków
   EN: Valencina
   PL: Valencina
950. [Tabela modeli postaci [엄지아비] — przydomek / oznaczenie] 엄지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지아비].nickName
   limit: do 40 znaków
   EN: The Thumb Nursefather
   PL: Ojciec Zastępczy The Thumb
951. [Tabela modeli postaci [엄지제자] — nazwa] 루치오
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지제자].name
   limit: do 40 znaków
   EN: Lucio
   PL: Lucio
952. [Tabela modeli postaci [엄지제자] — przydomek / oznaczenie] 엄지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지제자].nickName
   limit: do 40 znaków
   EN: The Thumb Apprentice
   PL: Uczeń The Thumb
953. [Tabela modeli postaci [검지아비상] — nazwa] 뤼엔
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비상].name
   limit: do 40 znaków
   EN: Rien
   PL: Rien
954. [Tabela modeli postaci [검지아비상] — przydomek / oznaczenie] 검지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비상].nickName
   limit: do 40 znaków
   EN: The Index Nursefather
   PL: Ojciec Zastępczy The Index
955. [Tabela modeli postaci [중지제자] — nazwa] 키라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=중지제자].name
   limit: do 40 znaków
   EN: Kira
   PL: Kira
956. [Tabela modeli postaci [중지제자] — przydomek / oznaczenie] 중지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=중지제자].nickName
   limit: do 40 znaków
   EN: The Middle Apprentice
   PL: Uczeń The Middle
957. [Tabela modeli postaci [약지아비상] — nazwa] 칼리스토
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아비상].name
   limit: do 40 znaków
   EN: Callisto
   PL: Callisto
958. [Tabela modeli postaci [약지아비상] — przydomek / oznaczenie] 약지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아비상].nickName
   limit: do 40 znaków
   EN: The Ring Nursefather
   PL: Ojciec Zastępczy The Ring
959. [Tabela modeli postaci [약지제자1] — nazwa] 알비나
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지제자1].name
   limit: do 40 znaków
   EN: Albina
   PL: Albina
960. [Tabela modeli postaci [약지제자1] — przydomek / oznaczenie] 약지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지제자1].nickName
   limit: do 40 znaków
   EN: The Ring Apprentice
   PL: Uczeń The Ring
961. [Tabela modeli postaci [약지제자2] — nazwa] 알비나
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지제자2].name
   (powtórzenie elementu 959 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [Tabela modeli postaci [약지제자2] — przydomek / oznaczenie] 약지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지제자2].nickName
   (powtórzenie elementu 960 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Tabela modeli postaci [소지아비] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비].name
   limit: do 40 znaków
   EN: Dihui Star
   PL: Dihui Star
964. [Tabela modeli postaci [소지아비] — przydomek / oznaczenie] 소지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비].nickName
   limit: do 40 znaków
   EN: The Pinky Nursefather
   PL: Ojciec Zastępczy Małego Palca
965. [Tabela modeli postaci [소지아비B1] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비B1].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Tabela modeli postaci [소지아비B1] — przydomek / oznaczenie] 소지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비B1].nickName
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Tabela modeli postaci [소지아비B2] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비B2].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [Tabela modeli postaci [소지아비B2] — przydomek / oznaczenie] 소지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비B2].nickName
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Tabela modeli postaci [소지제자] — nazwa] 렌
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지제자].name
   limit: do 40 znaków
   EN: Ren
   PL: Ren
970. [Tabela modeli postaci [소지제자] — przydomek / oznaczenie] 소지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지제자].nickName
   limit: do 40 znaków
   EN: The Pinky Apprentice
   PL: Uczeń Małego Palca
971. [Tabela modeli postaci [LCE연구원1] — nazwa] 겁에 질린 연구원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCE연구원1].name
   limit: do 40 znaków
   EN: Frightened Researcher
   PL: Przerażony Badacz
972. [Tabela modeli postaci [LCE연구원1] — przydomek / oznaczenie] LCE 사무팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCE연구원1].nickName
   limit: do 40 znaków
   EN: LCE Clerical Team
   PL: Zespół Biurowy LCE
973. [Tabela modeli postaci [LCE연구원2] — nazwa] 도망가는 연구원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCE연구원2].name
   limit: do 40 znaków
   EN: Fleeing Researcher
   PL: Uciekający Badacz
974. [Tabela modeli postaci [LCE연구원2] — przydomek / oznaczenie] LCE 사무팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCE연구원2].nickName
   (powtórzenie elementu 972 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Tabela modeli postaci [9장소드다침] — nazwa] 소드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=9장소드다침].name
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [Tabela modeli postaci [9장소드다침] — przydomek / oznaczenie] LCCB 과장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=9장소드다침].nickName
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Tabela modeli postaci [모제스1] — nazwa] 모제스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스1].name
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [Tabela modeli postaci [모제스1] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스1].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Tabela modeli postaci [모제스2] — nazwa] 모제스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스2].name
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [Tabela modeli postaci [모제스2] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스2].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Tabela modeli postaci [모제스3] — nazwa] 모제스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스3].name
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
982. [Tabela modeli postaci [모제스3] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스3].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Tabela modeli postaci [LCD앵두] — nazwa] 앵두
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCD앵두].name
   limit: do 40 znaków
   EN: Aeng-du
   PL: Aeng-du
984. [Tabela modeli postaci [LCD앵두] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCD앵두].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Tabela modeli postaci [과거료슈2] — nazwa] 요시히데
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거료슈2].name
   limit: do 40 znaków
   EN: Yoshihide
   PL: Yoshihide
986. [Tabela modeli postaci [과거료슈2] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거료슈2].nickName
   limit: do 40 znaków
   EN: The House of Spiders
   PL: Dom Pająków
987. [Tabela modeli postaci [과거료슈3] — nazwa] 요시히데
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거료슈3].name
   (powtórzenie elementu 985 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Tabela modeli postaci [과거료슈3] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거료슈3].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Tabela modeli postaci [료슈딸] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈딸].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Tabela modeli postaci [료슈딸] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈딸].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [Tabela modeli postaci [시체인형1] — nazwa] 시체로 만들어진 인형
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시체인형1].name
   limit: do 40 znaków
   EN: Corpse Manikin
   PL: Manekin ze Zwłok
992. [Tabela modeli postaci [시체인형1] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시체인형1].nickName
   limit: do 40 znaków
   EN: The Ring
   PL: The Ring
993. [Tabela modeli postaci [시체인형2] — nazwa] 시체로 만들어진 인형
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시체인형2].name
   (powtórzenie elementu 991 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [Tabela modeli postaci [시체인형2] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시체인형2].nickName
   (powtórzenie elementu 992 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Tabela modeli postaci [료슈9장] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [Tabela modeli postaci [료슈9장] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Tabela modeli postaci [엄지아비피] — nazwa] 발렌치나
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지아비피].name
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [Tabela modeli postaci [엄지아비피] — przydomek / oznaczenie] 엄지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지아비피].nickName
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Tabela modeli postaci [중지아비] — nazwa] 마티아스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=중지아비].name
   limit: do 40 znaków
   EN: Matthias
   PL: Matthias
1000. [Tabela modeli postaci [중지아비] — przydomek / oznaczenie] 중지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=중지아비].nickName
   limit: do 40 znaków
   EN: The Middle Nursefather
   PL: Ojciec Zastępczy The Middle
1001. [Tabela modeli postaci [약지아비] — nazwa] 칼리스토
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아비].name
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Tabela modeli postaci [약지아비] — przydomek / oznaczenie] 약지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아비].nickName
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1003. [Tabela modeli postaci [검지아비] — nazwa] 뤼엔
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비].name
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Tabela modeli postaci [검지아비] — przydomek / oznaczenie] 검지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비].nickName
   (powtórzenie elementu 954 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Tabela modeli postaci [검지제자] — nazwa] 소라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지제자].name
   limit: do 40 znaków
   EN: Sora
   PL: Sora
1006. [Tabela modeli postaci [검지제자] — przydomek / oznaczenie] 검지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지제자].nickName
   limit: do 40 znaków
   EN: The Index Apprentice
   PL: Uczeń The Index
1007. [Tabela modeli postaci [검지제자2] — nazwa] 소라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지제자2].name
   (powtórzenie elementu 1005 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Tabela modeli postaci [검지제자2] — przydomek / oznaczenie] LCE 연구팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지제자2].nickName
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [Tabela modeli postaci [라비] — nazwa] 라비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=라비].name
   limit: do 40 znaków
   EN: Ravi
   PL: Ravi
1010. [Tabela modeli postaci [라비] — przydomek / oznaczenie] LCE 사무팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=라비].nickName
   (powtórzenie elementu 972 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1011. [Tabela modeli postaci [LCA네임드] — nazwa] 자밀라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA네임드].name
   limit: do 40 znaków
   EN: Jamila
   PL: Jamila
1012. [Tabela modeli postaci [LCA네임드] — przydomek / oznaczenie] LCA 우제트 선봉 1팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA네임드].nickName
   limit: do 40 znaków
   EN: LCA Udjat Vanguard Team 1
   PL: LCA — 1. Zespół Szturmowy Udżat
1013. [Tabela modeli postaci [베스파] — nazwa] 베스파
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베스파].name
   limit: do 40 znaków
   EN: Vespa
   PL: Vespa
1014. [Tabela modeli postaci [베스파] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베스파].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1015. [Tabela modeli postaci [걷는진주] — nazwa] 걷는 진주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=걷는진주].name
   limit: do 40 znaków
   EN: Ambling Pearl
   PL: Krocząca Perła
1016. [Tabela modeli postaci [걷는진주] — przydomek / oznaczenie] 환상체
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=걷는진주].nickName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Abnormalność
1017. [Tabela modeli postaci [소지아비2] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비2].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1018. [Tabela modeli postaci [소지아비2] — przydomek / oznaczenie] 소지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비2].nickName
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Tabela modeli postaci [과거료슈1] — nazwa] 요시히데
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거료슈1].name
   (powtórzenie elementu 985 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Tabela modeli postaci [과거료슈1] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거료슈1].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Tabela modeli postaci [LCA대원벼락] — nazwa] 벼락인간
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA대원벼락].name
   limit: do 40 znaków
   EN: The Human Thunderbolt
   PL: Człowiek-Piorun
1022. [Tabela modeli postaci [LCA대원벼락] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA대원벼락].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Tabela modeli postaci [호엔하임2] — nazwa] 호엔하임
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임2].name
   (powtórzenie elementu 574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [Tabela modeli postaci [호엔하임2] — przydomek / oznaczenie] LCE 연구팀 수석
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임2].nickName
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1025. [Tabela modeli postaci [9장소드다침2] — nazwa] 소드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=9장소드다침2].name
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1026. [Tabela modeli postaci [9장소드다침2] — przydomek / oznaczenie] LCCB 과장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=9장소드다침2].nickName
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Tabela modeli postaci [머금은목화1] — nazwa] 머금은 목화
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=머금은목화1].name
   limit: do 40 znaków
   EN: Drenched Gossypium
   PL: Nasiąknięta Gosypium
1028. [Tabela modeli postaci [머금은목화1] — przydomek / oznaczenie] 환상체
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=머금은목화1].nickName
   limit: do 40 znaków
   EN: Abnormality
   PL: Abnormalność
1029. [Tabela modeli postaci [머금은목화2] — nazwa] 머금은 목화
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=머금은목화2].name
   (powtórzenie elementu 1027 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [Tabela modeli postaci [머금은목화2] — przydomek / oznaczenie] 환상체
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=머금은목화2].nickName
   (powtórzenie elementu 1028 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Tabela modeli postaci [시체인형3] — nazwa] 시체로 만들어진 인형
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시체인형3].name
   (powtórzenie elementu 991 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1032. [Tabela modeli postaci [시체인형3] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시체인형3].nickName
   (powtórzenie elementu 992 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1033. [Tabela modeli postaci [LCD앵두팔다침] — nazwa] 앵두
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCD앵두팔다침].name
   (powtórzenie elementu 983 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1034. [Tabela modeli postaci [LCD앵두팔다침] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCD앵두팔다침].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Tabela modeli postaci [엄지제자다침] — nazwa] 루치오
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지제자다침].name
   (powtórzenie elementu 951 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1036. [Tabela modeli postaci [엄지제자다침] — przydomek / oznaczenie] 엄지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=엄지제자다침].nickName
   (powtórzenie elementu 952 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Tabela modeli postaci [료슈딸연구실] — nazwa] 아라야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈딸연구실].name
   limit: do 40 znaków
   EN: Araya
   PL: Araya
1038. [Tabela modeli postaci [료슈딸연구실] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈딸연구실].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1039. [Tabela modeli postaci [료슈딸2] — nazwa] 아라야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈딸2].name
   (powtórzenie elementu 1037 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1040. [Tabela modeli postaci [료슈딸2] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈딸2].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Tabela modeli postaci [아라야10대] — nazwa] 아라야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야10대].name
   (powtórzenie elementu 1037 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1042. [Tabela modeli postaci [아라야10대] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야10대].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Tabela modeli postaci [아라야20대] — nazwa] 아라야
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야20대].name
   (powtórzenie elementu 1037 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Tabela modeli postaci [아라야20대] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야20대].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1045. [Tabela modeli postaci [아라야정장] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야정장].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1046. [Tabela modeli postaci [아라야정장] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야정장].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1047. [Tabela modeli postaci [소지아비3] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비3].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1048. [Tabela modeli postaci [소지아비3] — przydomek / oznaczenie] 소지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비3].nickName
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Tabela modeli postaci [검지제자3] — nazwa] 소라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지제자3].name
   (powtórzenie elementu 1005 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1050. [Tabela modeli postaci [검지제자3] — przydomek / oznaczenie] 검지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지제자3].nickName
   (powtórzenie elementu 1006 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1051. [Tabela modeli postaci [모제스4] — nazwa] 모제스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스4].name
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1052. [Tabela modeli postaci [모제스4] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=모제스4].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Tabela modeli postaci [중지아비2] — nazwa] 마티아스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=중지아비2].name
   (powtórzenie elementu 999 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1054. [Tabela modeli postaci [중지아비2] — przydomek / oznaczenie] 중지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=중지아비2].nickName
   (powtórzenie elementu 1000 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [Tabela modeli postaci [우제트선봉팀] — nazwa] 우제트 선봉팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=우제트선봉팀].name
   limit: do 40 znaków
   EN: Udjat Vanguard Team
   PL: Zespół Szturmowy Udżat
1056. [Tabela modeli postaci [우제트선봉팀] — przydomek / oznaczenie] LCA 우제트 선봉 1팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=우제트선봉팀].nickName
   (powtórzenie elementu 1012 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1057. [Tabela modeli postaci [우제트선봉팀2] — nazwa] 우제트 선봉팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=우제트선봉팀2].name
   (powtórzenie elementu 1055 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1058. [Tabela modeli postaci [우제트선봉팀2] — przydomek / oznaczenie] LCA 우제트 선봉 1팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=우제트선봉팀2].nickName
   (powtórzenie elementu 1012 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1059. [Tabela modeli postaci [호엔하임공중] — nazwa] 호엔하임
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임공중].name
   (powtórzenie elementu 574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1060. [Tabela modeli postaci [호엔하임공중] — przydomek / oznaczenie] LCE 연구팀 수석
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=호엔하임공중].nickName
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1061. [Tabela modeli postaci [약지제자3] — nazwa] 알비나
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지제자3].name
   (powtórzenie elementu 959 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1062. [Tabela modeli postaci [약지제자3] — przydomek / oznaczenie] 약지 제자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지제자3].nickName
   (powtórzenie elementu 960 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Tabela modeli postaci [각성싱클레어1] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각성싱클레어1].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1064. [Tabela modeli postaci [각성싱클레어1] — przydomek / oznaczenie] 연기전쟁
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각성싱클레어1].nickName
   limit: do 40 znaków
   EN: Smoke War
   PL: Wojna Dymów
1065. [Tabela modeli postaci [각성싱클레어2] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각성싱클레어2].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1066. [Tabela modeli postaci [각성싱클레어2] — przydomek / oznaczenie] 연기전쟁
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=각성싱클레어2].nickName
   (powtórzenie elementu 1064 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1067. [Tabela modeli postaci [검지아비2] — nazwa] 뤼엔
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비2].name
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1068. [Tabela modeli postaci [검지아비2] — przydomek / oznaczenie] 검지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비2].nickName
   (powtórzenie elementu 954 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1069. [Tabela modeli postaci [그레고르왕] — nazwa] UNGEZIEFER KAISER
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르왕].name
   limit: do 40 znaków
   EN: UNGEZIEFER KAISER
   PL: UNGEZIEFER KAISER
1070. [Tabela modeli postaci [그레고르왕] — przydomek / oznaczenie] 구 G사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르왕].nickName
   limit: do 40 znaków
   EN: Old G Corp.
   PL: Stary G Corp.
1071. [Tabela modeli postaci [아라야정장2] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야정장2].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1072. [Tabela modeli postaci [아라야정장2] — przydomek / oznaczenie] 거미집
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야정장2].nickName
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Tabela modeli postaci [그레고르왕그림자] — nazwa] UNGEZIEFER KAISER
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르왕그림자].name
   (powtórzenie elementu 1069 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1074. [Tabela modeli postaci [그레고르왕그림자] — przydomek / oznaczenie] 구 G사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르왕그림자].nickName
   (powtórzenie elementu 1070 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1075. [Tabela modeli postaci [료슈9장다침] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장다침].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1076. [Tabela modeli postaci [료슈9장다침] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장다침].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1077. [Tabela modeli postaci [다친대행자] — nazwa] 대행자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친대행자].name
   limit: do 40 znaków
   EN: Proxy
   PL: Proxy
1078. [Tabela modeli postaci [다친대행자] — przydomek / oznaczenie] 검지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친대행자].nickName
   limit: do 40 znaków
   EN: The Index
   PL: The Index
1079. [Tabela modeli postaci [소지아비얼굴] — nazwa] 지혜성
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비얼굴].name
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1080. [Tabela modeli postaci [소지아비얼굴] — przydomek / oznaczenie] 소지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=소지아비얼굴].nickName
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1081. [Tabela modeli postaci [약지아비2] — nazwa] 칼리스토
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아비2].name
   (powtórzenie elementu 957 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1082. [Tabela modeli postaci [약지아비2] — przydomek / oznaczenie] 약지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아비2].nickName
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1083. [Tabela modeli postaci [검지아비3] — nazwa] 뤼엔
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비3].name
   (powtórzenie elementu 953 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1084. [Tabela modeli postaci [검지아비3] — przydomek / oznaczenie] 검지 아비
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검지아비3].nickName
   (powtórzenie elementu 954 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1085. [Tabela modeli postaci [넬리2] — nazwa] 넬리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=넬리2].name
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1086. [Tabela modeli postaci [넬리2] — przydomek / oznaczenie] N사-신구인회
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=넬리2].nickName
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1087. [Tabela modeli postaci [LCA네임드2] — nazwa] 자밀라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA네임드2].name
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1088. [Tabela modeli postaci [LCA네임드2] — przydomek / oznaczenie] LCA 우제트 선봉 1팀
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=LCA네임드2].nickName
   (powtórzenie elementu 1012 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [Tabela modeli postaci [료슈9장이후담배] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장이후담배].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1090. [Tabela modeli postaci [료슈9장이후담배] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장이후담배].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1091. [Tabela modeli postaci [료슈9장이후노담배] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장이후노담배].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1092. [Tabela modeli postaci [료슈9장이후노담배] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장이후노담배].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1093. [Tabela modeli postaci [료슈9장이후반담배] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장이후반담배].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1094. [Tabela modeli postaci [료슈9장이후반담배] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈9장이후반담배].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [Tabela modeli postaci [뤼엔딸] — nazwa] !@#*%$
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뤼엔딸].name
   limit: do 40 znaków
   EN: !@#*%$
   PL: !@#*%$
1096. [Tabela modeli postaci [뤼엔딸] — przydomek / oznaczenie] 먼 과거
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뤼엔딸].nickName
   limit: do 40 znaków
   EN: Once Upon a Time
   PL: Dawno, Dawno Temu
1097. [Tabela modeli postaci [이상만우] — nazwa] 이상
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상만우].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1098. [Tabela modeli postaci [이상만우] — przydomek / oznaczenie] 1번 수감생 - 반장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이상만우].nickName
   limit: do 50 znaków
   EN: Sinnerling #1 - Class Captain
   PL: Grzeszniczek nr 1 — Przewodniczący
1099. [Tabela modeli postaci [파우스트만우] — nazwa] 파우스트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트만우].name
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1100. [Tabela modeli postaci [파우스트만우] — przydomek / oznaczenie] 2번 수감생 - 반장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파우스트만우].nickName
   limit: do 50 znaków
   EN: Sinnerling #2 - Class Captain
   PL: Grzeszniczek nr 2 — Przewodniczący
1101. [Tabela modeli postaci [돈키호테만우] — nazwa] 돈키호테
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테만우].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1102. [Tabela modeli postaci [돈키호테만우] — przydomek / oznaczenie] 3번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=돈키호테만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #3
   PL: Grzeszniczek nr 3
1103. [Tabela modeli postaci [료슈만우] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈만우].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1104. [Tabela modeli postaci [료슈만우] — przydomek / oznaczenie] 4번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=료슈만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #4
   PL: Grzeszniczek nr 4
1105. [Tabela modeli postaci [뫼르소만우] — nazwa] 뫼르소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소만우].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1106. [Tabela modeli postaci [뫼르소만우] — przydomek / oznaczenie] 5번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #5
   PL: Grzeszniczek nr 5
1107. [Tabela modeli postaci [홍루만우] — nazwa] 홍루
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루만우].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1108. [Tabela modeli postaci [홍루만우] — przydomek / oznaczenie] 6번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=홍루만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #6
   PL: Grzeszniczek nr 6
1109. [Tabela modeli postaci [히스클리프만우] — nazwa] 히스클리프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프만우].name
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1110. [Tabela modeli postaci [히스클리프만우] — przydomek / oznaczenie] 7번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=히스클리프만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #7
   PL: Grzeszniczek nr 7
1111. [Tabela modeli postaci [이스마엘만우] — nazwa] 이스마엘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘만우].name
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1112. [Tabela modeli postaci [이스마엘만우] — przydomek / oznaczenie] 8번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=이스마엘만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #8
   PL: Grzeszniczek nr 8
1113. [Tabela modeli postaci [로쟈만우] — nazwa] 로쟈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈만우].name
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1114. [Tabela modeli postaci [로쟈만우] — przydomek / oznaczenie] 9번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=로쟈만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #9
   PL: Grzeszniczek nr 9
1115. [Tabela modeli postaci [싱클레어만우] — nazwa] 싱클레어
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어만우].name
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1116. [Tabela modeli postaci [싱클레어만우] — przydomek / oznaczenie] 11번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=싱클레어만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #11
   PL: Grzeszniczek nr 11
1117. [Tabela modeli postaci [오티스만우] — nazwa] 오티스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스만우].name
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1118. [Tabela modeli postaci [오티스만우] — przydomek / oznaczenie] 12번 수감생 - 반장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오티스만우].nickName
   limit: do 50 znaków
   EN: Sinnerling #12 - Class Captain
   PL: Grzeszniczek nr 12 — Przewodniczący
1119. [Tabela modeli postaci [그레고르만우] — nazwa] 그레고르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르만우].name
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1120. [Tabela modeli postaci [그레고르만우] — przydomek / oznaczenie] 13번 수감생
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르만우].nickName
   limit: do 40 znaków
   EN: Sinnerling #13
   PL: Grzeszniczek nr 13
1121. [Tabela modeli postaci [베르길리우스만우] — nazwa] 베르길리우스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스만우].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1122. [Tabela modeli postaci [베르길리우스만우] — przydomek / oznaczenie] 붉은수각류
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=베르길리우스만우].nickName
   limit: do 40 znaków
   EN: The Red Theropod
   PL: Czerwony Teropod
1123. [Tabela modeli postaci [유리만우] — nazwa] 유리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유리만우].name
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1124. [Tabela modeli postaci [카론만우] — nazwa] 카론
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카론만우].name
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1125. [Tabela modeli postaci [뉴키라] — nazwa] 키라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴키라].name
   (powtórzenie elementu 955 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1126. [Tabela modeli postaci [뉴키라] — przydomek / oznaczenie] 포로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴키라].nickName
   limit: do 40 znaków
   EN: Prisoner
   PL: Więzień
1127. [Tabela modeli postaci [뉴키라2] — nazwa] 키라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴키라2].name
   (powtórzenie elementu 955 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1128. [Tabela modeli postaci [뉴키라2] — przydomek / oznaczenie] 포로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴키라2].nickName
   (powtórzenie elementu 1126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1129. [Tabela modeli postaci [에밀브누아] — nazwa] 에밀 브누아
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에밀브누아].name
   limit: do 40 znaków
   EN: Émile Benoît
   PL: Émile Benoît
1130. [Tabela modeli postaci [에밀브누아] — przydomek / oznaczenie] 약지 야수파 마에스트로
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에밀브누아].nickName
   limit: do 40 znaków
   EN: The Ring Fauvist Maestro
   PL: Fowista Maestro The Ring
1131. [Tabela modeli postaci [루포] — nazwa] 루포
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=루포].name
   limit: do 40 znaków
   EN: Rufo
   PL: Rufo
1132. [Tabela modeli postaci [루포] — przydomek / oznaczenie] 약지 야수파 도슨트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=루포].nickName
   limit: do 40 znaków
   EN: The Ring Fauvist Docent
   PL: Fowista Docentka The Ring
1133. [Tabela modeli postaci [털루포] — nazwa] 루포
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=털루포].name
   (powtórzenie elementu 1131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1134. [Tabela modeli postaci [털루포] — przydomek / oznaczenie] 약지 야수파 도슨트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=털루포].nickName
   (powtórzenie elementu 1132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1135. [Tabela modeli postaci [약지아이1] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아이1].nickName
   (powtórzenie elementu 992 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1136. [Tabela modeli postaci [약지아이2] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=약지아이2].nickName
   (powtórzenie elementu 992 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1137. [Tabela modeli postaci [야수파1] — nazwa] 야수파 스튜던트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야수파1].name
   limit: do 40 znaków
   EN: Fauvist Student
   PL: Fowistyczny Student
1138. [Tabela modeli postaci [야수파1] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야수파1].nickName
   (powtórzenie elementu 992 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1139. [Tabela modeli postaci [야수파2] — nazwa] 야수파 스튜던트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야수파2].name
   (powtórzenie elementu 1137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1140. [Tabela modeli postaci [야수파2] — przydomek / oznaczenie] 약지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야수파2].nickName
   (powtórzenie elementu 992 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1141. [Tabela modeli postaci [그레고르네부장] — nazwa] 테드
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르네부장].name
   limit: do 40 znaków
   EN: Ted
   PL: Ted
1142. [Tabela modeli postaci [그레고르네부장] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=그레고르네부장].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1143. [Tabela modeli postaci [아라야공백] — nazwa] ■■■
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야공백].name
   limit: do 40 znaków
   EN: ■■■■■
   PL: ■■■
1144. [Tabela modeli postaci [아라야공백] — przydomek / oznaczenie] ■■■
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=아라야공백].nickName
   limit: do 40 znaków
   EN: ■■■ ■■■■■ ■■ ■■■■■■■
   PL: ■■■
1145. [Tabela modeli postaci [앨런] — nazwa] 앨런
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=앨런].name
   limit: do 40 znaków
   EN: Alan
   PL: Alan
1146. [Tabela modeli postaci [앨런] — przydomek / oznaczenie] 웨이페어러 개통 4팀 팀장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=앨런].nickName
   limit: do 50 znaków
   EN: Wayfarer Doorbreach Team 4 Leader
   PL: Dowódca 4. Zespołu Przebijania Drzwi Wayfarer
1147. [Tabela modeli postaci [앨런마스크] — nazwa] 앨런
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=앨런마스크].name
   (powtórzenie elementu 1145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1148. [Tabela modeli postaci [앨런마스크] — przydomek / oznaczenie] 웨이페어러 개통 4팀 팀장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=앨런마스크].nickName
   (powtórzenie elementu 1146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1149. [Tabela modeli postaci [수행자1] — nazwa] 검지 수행자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=수행자1].name
   limit: do 40 znaków
   EN: The Index Proselyte
   PL: Prozelita The Index
1150. [Tabela modeli postaci [수행자1] — przydomek / oznaczenie] 검지
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=수행자1].nickName
   (powtórzenie elementu 1078 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1151. [Tabela modeli postaci [뒤틀린N사엑스트라1] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린N사엑스트라1].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1152. [Tabela modeli postaci [뒤틀린N사엑스트라1] — przydomek / oznaczenie] 14구 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린N사엑스트라1].nickName
   limit: do 40 znaków
   EN: District 14 Resident
   PL: Mieszkaniec Dystryktu 14
1153. [Tabela modeli postaci [빵가게주인] — nazwa] 빵가게 주인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=빵가게주인].name
   limit: do 40 znaków
   EN: Bakery Owner
   PL: Właściciel Piekarni
1154. [Tabela modeli postaci [빵가게주인] — przydomek / oznaczenie] 14구 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=빵가게주인].nickName
   (powtórzenie elementu 1152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1155. [Tabela modeli postaci [뒤틀린검계1] — nazwa] 기억 속 망자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린검계1].name
   limit: do 40 znaków
   EN: The Reminisced Dead
   PL: Wspomniany Zmarły
1156. [Tabela modeli postaci [뒤틀린검계1] — przydomek / oznaczenie] 검계 살수
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린검계1].nickName
   limit: do 40 znaków
   EN: Blade Lineage Salsu
   PL: Salsu Ródu Ostrza
1157. [Tabela modeli postaci [뒤틀린검계2] — nazwa] 기억 속 망자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린검계2].name
   (powtórzenie elementu 1155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1158. [Tabela modeli postaci [뒤틀린검계2] — przydomek / oznaczenie] 검계 살수
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린검계2].nickName
   (powtórzenie elementu 1156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1159. [Tabela modeli postaci [추노꾼1] — nazwa] 추노꾼?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=추노꾼1].name
   limit: do 40 znaków
   EN: Ch'unokkun?
   PL: Ch'unokkun?
1160. [Tabela modeli postaci [추노꾼1] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=추노꾼1].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1161. [Tabela modeli postaci [추노꾼2] — nazwa] 추노꾼?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=추노꾼2].name
   (powtórzenie elementu 1159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1162. [Tabela modeli postaci [추노꾼2] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=추노꾼2].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1163. [Tabela modeli postaci [N사해결사1] — nazwa] 2등급 고정팀 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사해결사1].name
   limit: do 40 znaków
   EN: Class 2 Pinframing Staff
   PL: Pracownik 2. Klasy Pinframing
1164. [Tabela modeli postaci [N사해결사1] — przydomek / oznaczenie] N사 못 부서
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사해결사1].nickName
   limit: do 40 znaków
   EN: N Corp. Service des Clous
   PL: N Corp. Service des Clous
1165. [Tabela modeli postaci [N사해결사2] — nazwa] 2등급 고정팀 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사해결사2].name
   (powtórzenie elementu 1163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1166. [Tabela modeli postaci [N사해결사2] — przydomek / oznaczenie] N사 못 부서
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=N사해결사2].nickName
   (powtórzenie elementu 1164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1167. [Tabela modeli postaci [임경업] — nazwa] 임경업
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업].name
   limit: do 40 znaków
   EN: Im Gyeong-eop
   PL: Im Gyeong-eop
1168. [Tabela modeli postaci [임경업] — przydomek / oznaczenie] S사 절도사 - 살
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업].nickName
   limit: do 50 znaków
   EN: S Corp. Military Commissioner  - Sal
   PL: Komisarz Wojskowy S Corp. — Sal
1169. [Tabela modeli postaci [임경업과거] — nazwa] 임경업
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업과거].name
   (powtórzenie elementu 1167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1170. [Tabela modeli postaci [임경업과거] — przydomek / oznaczenie] S사 절도사 - 살
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업과거].nickName
   (powtórzenie elementu 1168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1171. [Tabela modeli postaci [임경업뒤틀림] — nazwa] 뒤틀린 임경업
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업뒤틀림].name
   limit: do 40 znaków
   EN: Distorted Im Gyeong-eop
   PL: Wypaczony Im Gyeong-eop
1172. [Tabela modeli postaci [임경업뒤틀림] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업뒤틀림].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1173. [Tabela modeli postaci [뉴앵두] — nazwa] 앵두
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴앵두].name
   (powtórzenie elementu 983 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1174. [Tabela modeli postaci [뉴앵두] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴앵두].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1175. [Tabela modeli postaci [뉴김삿갓] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴김삿갓].name
   limit: do 40 znaków
   EN: Bamboo-hatted Kim
   PL: Kim w Bambusowym Kapeluszu
1176. [Tabela modeli postaci [뉴김삿갓] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴김삿갓].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1177. [Tabela modeli postaci [김삿갓과거] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓과거].name
   (powtórzenie elementu 1175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1178. [Tabela modeli postaci [김삿갓과거] — przydomek / oznaczenie] S사 호위무사 - 피
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓과거].nickName
   limit: do 40 znaków
   EN: S Corp. Bodyguard - Pi
   PL: Ochroniarz S Corp. — Pi
1179. [Tabela modeli postaci [한호배] — nazwa] 한호배
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=한호배].name
   limit: do 40 znaków
   EN: Han Ho-bae
   PL: Han Ho-bae
1180. [Tabela modeli postaci [한호배] — przydomek / oznaczenie] S사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=한호배].nickName
   limit: do 40 znaków
   EN: S Corp.
   PL: S Corp.
1181. [Tabela modeli postaci [에즈라먼지] — nazwa] 에즈라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에즈라먼지].name
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1182. [Tabela modeli postaci [에즈라먼지] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에즈라먼지].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1183. [Tabela modeli postaci [임경업과거오라] — nazwa] 임경업
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업과거오라].name
   (powtórzenie elementu 1167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1184. [Tabela modeli postaci [임경업과거오라] — przydomek / oznaczenie] S사 절도사 - 살
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업과거오라].nickName
   (powtórzenie elementu 1168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1185. [Tabela modeli postaci [임경업뒤틀림사라짐] — nazwa] 뒤틀린 임경업
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업뒤틀림사라짐].name
   (powtórzenie elementu 1171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1186. [Tabela modeli postaci [임경업뒤틀림사라짐] — przydomek / oznaczenie] 뒤틀림
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=임경업뒤틀림사라짐].nickName
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1187. [Tabela modeli postaci [김삿갓과거부상] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓과거부상].name
   (powtórzenie elementu 1175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1188. [Tabela modeli postaci [김삿갓과거부상] — przydomek / oznaczenie] S사 호위무사 - 피
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓과거부상].nickName
   (powtórzenie elementu 1178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1189. [Tabela modeli postaci [김삿갓죄수] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓죄수].name
   (powtórzenie elementu 1175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1190. [Tabela modeli postaci [김삿갓죄수] — przydomek / oznaczenie] 낙인 찍힌 자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=김삿갓죄수].nickName
   limit: do 40 znaków
   EN: The Branded
   PL: Naznaczony
1191. [Tabela modeli postaci [뒤틀린N사엑스트라2] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린N사엑스트라2].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1192. [Tabela modeli postaci [뒤틀린N사엑스트라2] — przydomek / oznaczenie] 14구 주민
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뒤틀린N사엑스트라2].nickName
   (powtórzenie elementu 1152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1193. [Tabela modeli postaci [뉴김삿갓안광] — nazwa] 김삿갓
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴김삿갓안광].name
   (powtórzenie elementu 1175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1194. [Tabela modeli postaci [뉴김삿갓안광] — przydomek / oznaczenie] LCD
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴김삿갓안광].nickName
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1195. [Tabela modeli postaci [뉴료슈노담다침] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴료슈노담다침].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1196. [Tabela modeli postaci [뉴료슈노담다침] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴료슈노담다침].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1197. [Tabela modeli postaci [뉴료슈반담다침] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴료슈반담다침].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1198. [Tabela modeli postaci [뉴료슈반담다침] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴료슈반담다침].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1199. [Tabela modeli postaci [뉴료슈담배다침] — nazwa] 료슈
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴료슈담배다침].name
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1200. [Tabela modeli postaci [뉴료슈담배다침] — przydomek / oznaczenie] 4번 수감자
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뉴료슈담배다침].nickName
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1201. [Tabela modeli postaci [푸른여인] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=푸른여인].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1202. [Tabela modeli postaci [푸른여인] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=푸른여인].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1203. [Tabela modeli postaci [크로머언니] — nazwa] 크로머
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크로머언니].name
   limit: do 40 znaków
   EN: Kromer
   PL: Kromer
1204. [Tabela modeli postaci [크로머언니] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크로머언니].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1205. [Tabela modeli postaci [잔느] — nazwa] 잔느
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=잔느].name
   limit: do 40 znaków
   EN: Jeanne
   PL: Jeanne
1206. [Tabela modeli postaci [잔느] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=잔느].nickName
   limit: do 40 znaków
   EN: Giant
   PL: Gigant
1207. [Tabela modeli postaci [1층백화점손님1] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층백화점손님1].name
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1208. [Tabela modeli postaci [1층백화점손님1] — przydomek / oznaczenie] 르카키
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층백화점손님1].nickName
   limit: do 40 znaków
   EN: Le Kaki
   PL: Le Kaki
1209. [Tabela modeli postaci [1층백화점손님2] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층백화점손님2].name
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1210. [Tabela modeli postaci [1층백화점손님2] — przydomek / oznaczenie] 르카키
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층백화점손님2].nickName
   (powtórzenie elementu 1208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1211. [Tabela modeli postaci [1층스파직원] — nazwa] 미모사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층스파직원].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Mimoza
1212. [Tabela modeli postaci [1층스파직원] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층스파직원].nickName
   limit: do 40 znaków
   EN: Le Rouge
   PL: Le Rouge
1213. [Tabela modeli postaci [시지프뉴비] — nazwa] 뒤부아
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시지프뉴비].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Dubois
1214. [Tabela modeli postaci [시지프뉴비] — przydomek / oznaczenie] 르카키
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=시지프뉴비].nickName
   (powtórzenie elementu 1208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1215. [Tabela modeli postaci [1층컨템누아르] — nazwa] 컨템포러리 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층컨템누아르].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Contempora
1216. [Tabela modeli postaci [1층컨템누아르] — przydomek / oznaczenie] 르누아르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층컨템누아르].nickName
   limit: do 40 znaków
   EN: Le Noir
   PL: Le Noir
1217. [Tabela modeli postaci [1층컨템루즈] — nazwa] 컨템포러리 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층컨템루즈].name
   (powtórzenie elementu 1215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1218. [Tabela modeli postaci [1층컨템루즈] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=1층컨템루즈].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1219. [Tabela modeli postaci [맨얼굴크로머언니] — nazwa] 크로머
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=맨얼굴크로머언니].name
   (powtórzenie elementu 1203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1220. [Tabela modeli postaci [맨얼굴크로머언니] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=맨얼굴크로머언니].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1221. [Tabela modeli postaci [2층가드루주] — nazwa] 명품관 문지기
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=2층가드루주].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Strażnik Butiku Premium
1222. [Tabela modeli postaci [2층가드루주] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=2층가드루주].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1223. [Tabela modeli postaci [3층장기루주] — nazwa] 르루주 고위급
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층장기루주].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Wyższy Stopniem Le Rouge
1224. [Tabela modeli postaci [3층장기루주] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층장기루주].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1225. [Tabela modeli postaci [3층하이도메루주] — nazwa] 리나모비블
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메루주].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: L'Inamovible
1226. [Tabela modeli postaci [3층하이도메루주] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메루주].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1227. [Tabela modeli postaci [3층하이도메누아르1] — nazwa] 하이 도메스틱 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메누아르1].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Pracownik Haute Domestic
1228. [Tabela modeli postaci [3층하이도메누아르1] — przydomek / oznaczenie] 르누아르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메누아르1].nickName
   (powtórzenie elementu 1216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1229. [Tabela modeli postaci [3층하이도메누아르2] — nazwa] 하이 도메스틱 직원
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메누아르2].name
   (powtórzenie elementu 1227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1230. [Tabela modeli postaci [3층하이도메누아르2] — przydomek / oznaczenie] 르누아르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메누아르2].nickName
   (powtórzenie elementu 1216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1231. [Tabela modeli postaci [3층가위] — nazwa] 아네트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층가위].name
   limit: do 40 znaków
   EN: Annette
   PL: Annette
1232. [Tabela modeli postaci [3층가위] — przydomek / oznaczenie] 수선실
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층가위].nickName
   limit: do 40 znaków
   EN: Alteration Shop
   PL: Warsztat Poprawek
1233. [Tabela modeli postaci [3층문셔터] — nazwa] 셔터
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층문셔터].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Roleta
1234. [Tabela modeli postaci [3층문셔터] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층문셔터].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1235. [Tabela modeli postaci [3층하이도메루주변신전] — nazwa] 리나모비블
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메루주변신전].name
   limit: do 40 znaków
   EN: L'Inamovible
   PL: L'Inamovible
1236. [Tabela modeli postaci [3층하이도메루주변신전] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메루주변신전].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1237. [Tabela modeli postaci [3층플로어매니저] — nazwa] 3층 플로어 매니저
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층플로어매니저].name
   limit: do 40 znaków
   EN: 3F Floor Manager
   PL: Kierownik 3. Piętra
1238. [Tabela modeli postaci [3층플로어매니저] — przydomek / oznaczenie] 시지프 백화점
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층플로어매니저].nickName
   limit: do 40 znaków
   EN: ???
   PL: ???
1239. [Tabela modeli postaci [4층원레그] — nazwa] 원레그
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4층원레그].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Surowa Noga
1240. [Tabela modeli postaci [4층원레그] — przydomek / oznaczenie] 르누아르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4층원레그].nickName
   (powtórzenie elementu 1216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1241. [Tabela modeli postaci [4층행복옷장] — nazwa] 행복한 옷장
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4층행복옷장].name
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: Szczęśliwa Szafa
1242. [Tabela modeli postaci [4층행복옷장] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=4층행복옷장].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1243. [Tabela modeli postaci [B2층염색실주인] — nazwa] 팔레트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=B2층염색실주인].name
   limit: do 40 znaków
   EN: Palette
   PL: Palette
1244. [Tabela modeli postaci [B2층염색실주인] — przydomek / oznaczenie] 염색실
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=B2층염색실주인].nickName
   limit: do 40 znaków
   EN: Dyehouse
   PL: Farbiarnia
1245. [Tabela modeli postaci [B2층플로어매니저] — nazwa] 지하 2층 플로어 매니저
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=B2층플로어매니저].name
   limit: do 40 znaków
   EN: B2F Floor Manager
   PL: Kierownik Piętra -2
1246. [Tabela modeli postaci [B2층플로어매니저] — przydomek / oznaczenie] 시지프 백화점
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=B2층플로어매니저].nickName
   limit: do 40 znaków
   EN: Grand Magasin Sisyphe
   PL: Grand Magasin Sisyphe
1247. [Tabela modeli postaci [3층하이도메루주번데기] — nazwa] 리나모비블
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메루주번데기].name
   (powtórzenie elementu 1235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1248. [Tabela modeli postaci [3층하이도메루주번데기] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=3층하이도메루주번데기].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1249. [Tabela modeli postaci [퍼티] — nazwa] 퍼티
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퍼티].name
   limit: do 40 znaków
   EN: Putty
   PL: Putty
1250. [Tabela modeli postaci [퍼티] — przydomek / oznaczenie] 염색실
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=퍼티].nickName
   (powtórzenie elementu 1244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1251. [Tabela modeli postaci [검사] — nazwa] 검사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검사].name
   limit: do 40 znaków
   EN: Prosecutor
   PL: Prokurator
1252. [Tabela modeli postaci [검사] — przydomek / oznaczenie] N사 사법부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=검사].nickName
   limit: do 40 znaków
   EN: N Corp. Judiciary
   PL: Sądownictwo N Corp.
1253. [Tabela modeli postaci [뷔페어린이] — nazwa] 뿌이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어린이].name
   limit: do 40 znaków
   EN: Pwie
   PL: Pwie
1254. [Tabela modeli postaci [뷔페어린이] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어린이].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1255. [Tabela modeli postaci [뷔페어린이신발] — nazwa] 뿌이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어린이신발].name
   (powtórzenie elementu 1253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1256. [Tabela modeli postaci [뷔페어린이신발] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어린이신발].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1257. [Tabela modeli postaci [뷔페어린이옷] — nazwa] 뿌이
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어린이옷].name
   (powtórzenie elementu 1253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1258. [Tabela modeli postaci [뷔페어린이옷] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어린이옷].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1259. [Tabela modeli postaci [뷔페어른] — nazwa] 뷔페
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어른].name
   limit: do 40 znaków
   EN: Buffet
   PL: Bufet
1260. [Tabela modeli postaci [뷔페어른] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뷔페어른].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1261. [Tabela modeli postaci [카르멘] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카르멘].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1262. [Tabela modeli postaci [카르멘] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카르멘].nickName
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1263. [Tabela modeli postaci [판사] — nazwa] 판사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=판사].name
   limit: do 40 znaków
   EN: Judge
   PL: Sędzia
1264. [Tabela modeli postaci [판사] — przydomek / oznaczenie] N사 사법부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=판사].nickName
   (powtórzenie elementu 1252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1265. [Tabela modeli postaci [수셰프] — nazwa] 수셰프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=수셰프].name
   limit: do 40 znaków
   EN: Sous Chef
   PL: Sous Chef
1266. [Tabela modeli postaci [수셰프] — przydomek / oznaczenie] 푸드코트
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=수셰프].nickName
   limit: do 40 znaków
   EN: Food Court
   PL: Strefa Gastronomiczna
1267. [Tabela modeli postaci [붉은신] — nazwa] 붉은 신
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=붉은신].name
   limit: do 40 znaków
   EN: The Crimson God
   PL: Szkarłatny Bóg
1268. [Tabela modeli postaci [붉은신] — przydomek / oznaczenie] 르루주
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=붉은신].nickName
   (powtórzenie elementu 1212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1269. [Tabela modeli postaci [뫼르소엄마] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1270. [Tabela modeli postaci [뫼르소엄마] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1271. [Tabela modeli postaci [과거뫼르소] — nazwa] 뫼르소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거뫼르소].name
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1272. [Tabela modeli postaci [과거뫼르소] — przydomek / oznaczenie] N사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거뫼르소].nickName
   limit: do 40 znaków
   EN: N Corp.
   PL: N Corp.
1273. [Tabela modeli postaci [간수] — nazwa] 간수?
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=간수].name
   limit: do 40 znaków
   EN: The Warden?
   PL: Nadzorca?
1274. [Tabela modeli postaci [간수] — przydomek / oznaczenie] 시지프 백화점
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=간수].nickName
   (powtórzenie elementu 1246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1275. [Tabela modeli postaci [신부거인] — nazwa] 신부
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부거인].name
   limit: do 40 znaków
   EN: The Chaplain
   PL: Kapelan
1276. [Tabela modeli postaci [신부거인] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부거인].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1277. [Tabela modeli postaci [과거잔느] — nazwa] 잔느
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거잔느].name
   (powtórzenie elementu 1205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1278. [Tabela modeli postaci [과거잔느] — przydomek / oznaczenie] N사
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=과거잔느].nickName
   (powtórzenie elementu 1272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1279. [Tabela modeli postaci [뫼르소엄마안경] — nazwa] 어머니
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마안경].name
   limit: do 40 znaków
   EN: Mother
   PL: Matka
1280. [Tabela modeli postaci [뫼르소엄마안경] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마안경].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1281. [Tabela modeli postaci [잔느변신] — nazwa] 잔느
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=잔느변신].name
   (powtórzenie elementu 1205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1282. [Tabela modeli postaci [잔느변신] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=잔느변신].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1283. [Tabela modeli postaci [잔느변신2] — nazwa] 잔느
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=잔느변신2].name
   (powtórzenie elementu 1205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1284. [Tabela modeli postaci [잔느변신2] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=잔느변신2].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1285. [Tabela modeli postaci [카르멘진짜] — nazwa] 카르멘
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카르멘진짜].name
   limit: do 40 znaków
   EN: Carmen
   PL: Carmen
1286. [Tabela modeli postaci [카르멘진짜] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=카르멘진짜].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1287. [Tabela modeli postaci [야코프] — nazwa] 야코프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야코프].name
   limit: do 40 znaków
   EN: Jacob
   PL: Jacob
1288. [Tabela modeli postaci [야코프] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야코프].nickName
   limit: do 40 znaków
   EN: Nagel und Hammer
   PL: Nagel und Hammer
1289. [Tabela modeli postaci [신부진짜] — nazwa] 모리스
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부진짜].name
   limit: do 40 znaków
   EN: Maurice
   PL: Maurice
1290. [Tabela modeli postaci [신부진짜] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=신부진짜].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1291. [Tabela modeli postaci [크로머언니진짜] — nazwa] 크로머
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크로머언니진짜].name
   (powtórzenie elementu 1203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1292. [Tabela modeli postaci [크로머언니진짜] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=크로머언니진짜].nickName
   (powtórzenie elementu 1288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1293. [Tabela modeli postaci [르루주브랜드디렉터] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=르루주브랜드디렉터].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1294. [Tabela modeli postaci [르루주브랜드디렉터] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=르루주브랜드디렉터].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1295. [Tabela modeli postaci [르루주브랜드디렉터다침] — nazwa] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=르루주브랜드디렉터다침].name
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1296. [Tabela modeli postaci [르루주브랜드디렉터다침] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=르루주브랜드디렉터다침].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1297. [Tabela modeli postaci [뫼르소엄마아픔] — nazwa] 어머니
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마아픔].name
   (powtórzenie elementu 1279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1298. [Tabela modeli postaci [뫼르소엄마아픔] — przydomek / oznaczenie] 거인
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마아픔].nickName
   (powtórzenie elementu 1206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1299. [Tabela modeli postaci [야코프머리] — nazwa] 야코프
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야코프머리].name
   (powtórzenie elementu 1287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1300. [Tabela modeli postaci [야코프머리] — przydomek / oznaczenie] 못과 망치
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=야코프머리].nickName
   (powtórzenie elementu 1288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1301. [Tabela modeli postaci [뫼르소엄마뒤틀림1] — nazwa] 어머니
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마뒤틀림1].name
   (powtórzenie elementu 1279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1302. [Tabela modeli postaci [뫼르소엄마뒤틀림1] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마뒤틀림1].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1303. [Tabela modeli postaci [뫼르소엄마뒤틀림2] — nazwa] 어머니
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마뒤틀림2].name
   (powtórzenie elementu 1279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1304. [Tabela modeli postaci [뫼르소엄마뒤틀림2] — przydomek / oznaczenie] ???
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=뫼르소엄마뒤틀림2].nickName
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1305. [Tabela modeli postaci [살바도르] — nazwa] 살바도르
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=살바도르].name
   limit: do 40 znaków
   EN: Salvador
   PL: Salvador
1306. [Tabela modeli postaci [살바도르] — przydomek / oznaczenie] 새벽 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=살바도르].nickName
   limit: do 40 znaków
   EN: Dawn Office
   PL: Biuro Świtu
1307. [Tabela modeli postaci [유나] — nazwa] 유나
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유나].name
   limit: do 40 znaków
   EN: Yuna
   PL: Yuna
1308. [Tabela modeli postaci [유나] — przydomek / oznaczenie] 새벽 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=유나].nickName
   (powtórzenie elementu 1306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1309. [Tabela modeli postaci [필립] — nazwa] 필립
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=필립].name
   limit: do 40 znaków
   EN: Philip
   PL: Philip
1310. [Tabela modeli postaci [필립] — przydomek / oznaczenie] 새벽 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=필립].nickName
   (powtórzenie elementu 1306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1311. [Tabela modeli postaci [다친필립] — nazwa] 필립
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친필립].name
   (powtórzenie elementu 1309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1312. [Tabela modeli postaci [다친필립] — przydomek / oznaczenie] 새벽 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=다친필립].nickName
   (powtórzenie elementu 1306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1313. [Tabela modeli postaci [에고필립] — nazwa] 필립
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고필립].name
   (powtórzenie elementu 1309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1314. [Tabela modeli postaci [에고필립] — przydomek / oznaczenie] 새벽 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=에고필립].nickName
   (powtórzenie elementu 1306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1315. [Tabela modeli postaci [오스카] — nazwa] 오스카
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오스카].name
   limit: do 40 znaków
   EN: Oscar
   PL: Oscar
1316. [Tabela modeli postaci [오스카] — przydomek / oznaczenie] 쐐기 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=오스카].nickName
   limit: do 40 znaków
   EN: Wedge Office
   PL: Biuro Klinów
1317. [Tabela modeli postaci [파멜라] — nazwa] 파멜라
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파멜라].name
   limit: do 40 znaków
   EN: Pamela
   PL: Pamela
1318. [Tabela modeli postaci [파멜라] — przydomek / oznaczenie] 쐐기 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파멜라].nickName
   (powtórzenie elementu 1316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1319. [Tabela modeli postaci [파멜리] — nazwa] 파멜리
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파멜리].name
   limit: do 40 znaków
   EN: Pameli
   PL: Pameli
1320. [Tabela modeli postaci [파멜리] — przydomek / oznaczenie] 쐐기 사무소
   źródło: ScenarioModelCodes-AutoCreated.json :: dataList[id=파멜리].nickName
   (powtórzenie elementu 1316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [common] — rpg-loc-item-common-a1c10p1
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-item-common-a1c10p1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

1321. [RPG [I104002] — nazwa wyświetlana] 행복한 옷장의 옷
   źródło: RPGSystem/rpg-loc-item-common-a1c10p1.json :: dataList[key=I104002].displayName
   limit: do 50 znaków
   EN: Clothes from the Happy Closet
   PL: Ubrania ze Szczęśliwej Szafy
