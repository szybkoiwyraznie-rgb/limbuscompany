# Paczka AI P05 (Fala 1 · 1C) — Tryby gry, nazwy etapów, Lustrzane Lochy, Kolej i Teatr (UI) (część 1/6)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P05_1c_tryby_etapy_lochy_teatr_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P05_1c_tryby_etapy_lochy_teatr_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Notatki Dantego — hasło: StoryTheaterDanteNote
- plik gry: `StoryTheaterDanteNote.json`

1. [Notatki Dantego — hasło [City] — tekst] 도시
   źródło: StoryTheaterDanteNote.json :: dataList[id=City].content
   limit: do 120 znaków
   EN: The City
   PL: Miasto
2. [Notatki Dantego — hasło [Limbuscompany] — tekst] 림버스 컴퍼니
   źródło: StoryTheaterDanteNote.json :: dataList[id=Limbuscompany].content
   limit: do 120 znaków
   EN: Limbus Company
   PL: Limbus Company
3. [Notatki Dantego — hasło [LCB] — tekst] LCB
   źródło: StoryTheaterDanteNote.json :: dataList[id=LCB].content
   limit: do 120 znaków
   EN: The LCB
   PL: LCB
4. [Notatki Dantego — hasło [LCC] — tekst] LCC
   źródło: StoryTheaterDanteNote.json :: dataList[id=LCC].content
   limit: do 120 znaków
   EN: The LCC
   PL: LCC
5. [Notatki Dantego — hasło [Nest] — tekst] 둥지
   źródło: StoryTheaterDanteNote.json :: dataList[id=Nest].content
   limit: do 120 znaków
   EN: The Nests
   PL: Gniazda
6. [Notatki Dantego — hasło [Sinner] — tekst] 수감자
   źródło: StoryTheaterDanteNote.json :: dataList[id=Sinner].content
   limit: do 120 znaków
   EN: Sinners
   PL: Grzesznicy
7. [Notatki Dantego — hasło [Wings] — tekst] 날개
   źródło: StoryTheaterDanteNote.json :: dataList[id=Wings].content
   limit: do 120 znaków
   EN: The Wings
   PL: Skrzydła
8. [Notatki Dantego — hasło [NestK] — tekst] K사
   źródło: StoryTheaterDanteNote.json :: dataList[id=NestK].content
   limit: do 120 znaków
   EN: K Corp.
   PL: K Corp.
9. [Notatki Dantego — hasło [NestN] — tekst] N사
   źródło: StoryTheaterDanteNote.json :: dataList[id=NestN].content
   limit: do 120 znaków
   EN: N Corp.
   PL: N Corp.
10. [Notatki Dantego — hasło [NestL] — tekst] L사
   źródło: StoryTheaterDanteNote.json :: dataList[id=NestL].content
   limit: do 120 znaków
   EN: L Corp.
   PL: L Corp.
11. [Notatki Dantego — hasło [Backstreet] — tekst] 뒷골목
   źródło: StoryTheaterDanteNote.json :: dataList[id=Backstreet].content
   limit: do 120 znaków
   EN: The Backstreets
   PL: Zaułki
12. [Notatki Dantego — hasło [Swordgroup] — tekst] 검계
   źródło: StoryTheaterDanteNote.json :: dataList[id=Swordgroup].content
   limit: do 120 znaków
   EN: The Blade Lineage
   PL: Ród Ostrza
13. [Notatki Dantego — hasło [Kurokumo] — tekst] 흑운회
   źródło: StoryTheaterDanteNote.json :: dataList[id=Kurokumo].content
   limit: do 120 znaków
   EN: The Kurokumo Clan
   PL: Klan Kurokumo
14. [Notatki Dantego — hasło [Personality] — tekst] 인격
   źródło: StoryTheaterDanteNote.json :: dataList[id=Personality].content
   limit: do 120 znaków
   EN: Identities
   PL: Tożsamości
15. [Notatki Dantego — hasło [Ego] — tekst] E.G.O
   źródło: StoryTheaterDanteNote.json :: dataList[id=Ego].content
   limit: do 120 znaków
   EN: E.G.O
   PL: E.G.O
16. [Notatki Dantego — hasło [Tech] — tekst] 도시의 기술
   źródło: StoryTheaterDanteNote.json :: dataList[id=Tech].content
   limit: do 120 znaków
   EN: The City’s Technology
   PL: Technologia Miasta
17. [Notatki Dantego — hasło [Organization] — tekst] 조직
   źródło: StoryTheaterDanteNote.json :: dataList[id=Organization].content
   limit: do 120 znaków
   EN: Syndicates
   PL: Syndykaty
18. [Notatki Dantego — hasło [Fixer] — tekst] 해결사
   źródło: StoryTheaterDanteNote.json :: dataList[id=Fixer].content
   limit: do 120 znaków
   EN: Fixers
   PL: Fikserzy
19. [Notatki Dantego — hasło [Goldenbranch] — tekst] 황금가지
   źródło: StoryTheaterDanteNote.json :: dataList[id=Goldenbranch].content
   limit: do 120 znaków
   EN: The Golden Boughs
   PL: Złote Gałęzie

## Notatki Dantego — hasło: StoryTheaterDanteNote_10
- plik gry: `StoryTheaterDanteNote_10.json`

20. [Notatki Dantego — hasło [Fingers] — tekst] 손가락
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=Fingers].content
   limit: do 120 znaków
   EN: The Fingers
   PL: Palce
21. [Notatki Dantego — hasło [TheRings] — tekst] 약지
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=TheRings].content
   limit: do 120 znaków
   EN: The Ring
   PL: Serdeczny
22. [Notatki Dantego — hasło [TheMiddle] — tekst] 중지
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=TheMiddle].content
   limit: do 120 znaków
   EN: The Middle
   PL: Środkowy
23. [Notatki Dantego — hasło [NestH] — tekst] H사
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=NestH].content
   limit: do 120 znaków
   EN: H Corp.
   PL: H Corp.
24. [Notatki Dantego — hasło [Heishou] — tekst] 흑수
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=Heishou].content
   limit: do 120 znaków
   EN: Heishou Packs
   PL: Watahy Heishou
25. [Notatki Dantego — hasło [Sweeper] — tekst] 청소부
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=Sweeper].content
   limit: do 120 znaków
   EN: Sweepers
   PL: Sprzątacze
26. [Notatki Dantego — hasło [NightBackstreet] — tekst] 뒷골목의 밤
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=NightBackstreet].content
   limit: do 120 znaków
   EN: Night in the Backstreets
   PL: Noc w Zaułkach
27. [Notatki Dantego — hasło [Line5] — tekst] 거울굴절철도 5호선
   źródło: StoryTheaterDanteNote_10.json :: dataList[id=Line5].content
   limit: do 120 znaków
   EN: Refraction Railway Line 5
   PL: Kolej Załamania — Linia 5

## Notatki Dantego — hasło: StoryTheaterDanteNote_11
- plik gry: `StoryTheaterDanteNote_11.json`

28. [Notatki Dantego — hasło [ConceptIncinerator] — tekst] 개념 소각기
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=ConceptIncinerator].content
   limit: do 120 znaków
   EN: Concept Incinerator
   PL: Spopielacz Pojęć
29. [Notatki Dantego — hasło [TheThumb] — tekst] 엄지
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=TheThumb].content
   limit: do 120 znaków
   EN: The Thumb
   PL: Kciuk
30. [Notatki Dantego — hasło [ThePinky] — tekst] 소지
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=ThePinky].content
   limit: do 120 znaków
   EN: The Pinky
   PL: Mały Palec
31. [Notatki Dantego — hasło [Anamnaworm] — tekst] 충
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=Anamnaworm].content
   limit: do 120 znaków
   EN: Anamnaworm
   PL: Anamnoczerw
32. [Notatki Dantego — hasło [NestA] — tekst] A사
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=NestA].content
   limit: do 120 znaków
   EN: A Corp.
   PL: A Corp.
33. [Notatki Dantego — hasło [HouseofSpiders] — tekst] 거미집
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=HouseofSpiders].content
   limit: do 120 znaków
   EN: The House of Spiders
   PL: Dom Pająków
34. [Notatki Dantego — hasło [TheIndex] — tekst] 검지
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=TheIndex].content
   limit: do 120 znaków
   EN: The Index
   PL: Wskazujący
35. [Notatki Dantego — hasło [SmokeWar] — tekst] 연기전쟁
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=SmokeWar].content
   limit: do 120 znaków
   EN: The Smoke War
   PL: Wojna Dymna
36. [Notatki Dantego — hasło [ColorFixer] — tekst] 특색
   źródło: StoryTheaterDanteNote_11.json :: dataList[id=ColorFixer].content
   limit: do 120 znaków
   EN: Color Fixer
   PL: Kolorowi Fikserzy

## Notatki Dantego — hasło: StoryTheaterDanteNote_12
- plik gry: `StoryTheaterDanteNote_12.json`

37. [Notatki Dantego — hasło [TheSigns] — tekst] 표지
   źródło: StoryTheaterDanteNote_12.json :: dataList[id=TheSigns].content
   limit: do 120 znaków
   EN: The Sign
   PL: Znak
38. [Notatki Dantego — hasło [NestWNew] — tekst] 웨이페어러
   źródło: StoryTheaterDanteNote_12.json :: dataList[id=NestWNew].content
   limit: do 120 znaków
   EN: Wayfarer
   PL: Wędrowiec
39. [Notatki Dantego — hasło [Shin] — tekst] 신(心)
   źródło: StoryTheaterDanteNote_12.json :: dataList[id=Shin].content
   limit: do 120 znaków
   EN: Shin (心)
   PL: Shin (心)

## Notatki Dantego — hasło: StoryTheaterDanteNote_13
- plik gry: `StoryTheaterDanteNote_13.json`

40. [Notatki Dantego — hasło [ExpCan] — tekst] 경험 통조림
   źródło: StoryTheaterDanteNote_13.json :: dataList[id=ExpCan].content
   limit: do 120 znaków
   EN: Canned Experience
   PL: Konserwowe Doświadczenie
41. [Notatki Dantego — hasło [EffEGO] — tekst] 개화 E.G.O
   źródło: StoryTheaterDanteNote_13.json :: dataList[id=EffEGO].content
   limit: do 120 znaków
   EN: Effloresced E.G.O
   PL: Rozkwitłe E.G.O

## Notatki Dantego — hasło: StoryTheaterDanteNote_2
- plik gry: `StoryTheaterDanteNote_2.json`

42. [Notatki Dantego — hasło [Association] — tekst] 협회
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=Association].content
   limit: do 120 znaków
   EN: The Associations
   PL: Stowarzyszenia
43. [Notatki Dantego — hasło [ShiAsso] — tekst] 시 협회
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=ShiAsso].content
   limit: do 120 znaków
   EN: Shi Association
   PL: Stowarzyszenie Shi
44. [Notatki Dantego — hasło [LiuAsso] — tekst] 리우 협회
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=LiuAsso].content
   limit: do 120 znaków
   EN: Liu Association
   PL: Stowarzyszenie Liu
45. [Notatki Dantego — hasło [Office] — tekst] 사무소
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=Office].content
   limit: do 120 znaków
   EN: Offices
   PL: Biura
46. [Notatki Dantego — hasło [LobotomyCorp] — tekst] 로보토미 코퍼레이션
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=LobotomyCorp].content
   limit: do 120 znaków
   EN: Lobotomy Corporation
   PL: Lobotomy Corporation
47. [Notatki Dantego — hasło [Enkephalin] — tekst] 엔케팔린
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=Enkephalin].content
   limit: do 120 znaków
   EN: Enkephalin
   PL: Enkefalina
48. [Notatki Dantego — hasło [Abnormality] — tekst] 환상체
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=Abnormality].content
   limit: do 120 znaków
   EN: Abnormalities
   PL: Anomalie
49. [Notatki Dantego — hasło [Cinq] — tekst] 섕크 협회
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=Cinq].content
   limit: do 120 znaków
   EN: Cinq Association
   PL: Stowarzyszenie Cinq
50. [Notatki Dantego — hasło [String] — tekst] 끈
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=String].content
   limit: do 120 znaków
   EN: Thread
   PL: Nić
51. [Notatki Dantego — hasło [Singularity] — tekst] 특이점
   źródło: StoryTheaterDanteNote_2.json :: dataList[id=Singularity].content
   limit: do 120 znaków
   EN: Singularities
   PL: Osobliwości

## Notatki Dantego — hasło: StoryTheaterDanteNote_3
- plik gry: `StoryTheaterDanteNote_3.json`

52. [Notatki Dantego — hasło [NestW] — tekst] W사
   źródło: StoryTheaterDanteNote_3.json :: dataList[id=NestW].content
   limit: do 120 znaków
   EN: W Corp.
   PL: W Corp.
53. [Notatki Dantego — hasło [PersonalitySync] — tekst] 인격 동기화
   źródło: StoryTheaterDanteNote_3.json :: dataList[id=PersonalitySync].content
   limit: do 120 znaków
   EN: Identity Uptying
   PL: Synchronizacja Tożsamości
54. [Notatki Dantego — hasło [AbnormalityInterpret] — tekst] 환상 해석
   źródło: StoryTheaterDanteNote_3.json :: dataList[id=AbnormalityInterpret].content
   limit: do 120 znaków
   EN: Threadspinning
   PL: Splot Nici
55. [Notatki Dantego — hasło [PersonalityUpgrade] — tekst] 인격 강화
   źródło: StoryTheaterDanteNote_3.json :: dataList[id=PersonalityUpgrade].content
   limit: do 120 znaków
   EN: Upgrading Identities
   PL: Ulepszanie Tożsamości
56. [Notatki Dantego — hasło [NestR] — tekst] R사
   źródło: StoryTheaterDanteNote_3.json :: dataList[id=NestR].content
   limit: do 120 znaków
   EN: R Corp.
   PL: R Corp.

## Notatki Dantego — hasło: StoryTheaterDanteNote_4
- plik gry: `StoryTheaterDanteNote_4.json`

57. [Notatki Dantego — hasło [Mepis] — tekst] 메피스토펠레스
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=Mepis].content
   limit: do 120 znaków
   EN: Mephistopheles
   PL: Mefistofeles
58. [Notatki Dantego — hasło [Backdoor] — tekst] 뒷문
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=Backdoor].content
   limit: do 120 znaków
   EN: The Backdoor
   PL: Tylne Drzwi
59. [Notatki Dantego — hasło [MirrorDungeon] — tekst] 거울 던전
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=MirrorDungeon].content
   limit: do 120 znaków
   EN: Mirror Dungeons
   PL: Lustrzane Lochy
60. [Notatki Dantego — hasło [ResourceDungeon] — tekst] 채광 던전
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=ResourceDungeon].content
   limit: do 120 znaków
   EN: Luxcavation Dungeons
   PL: Lochy Wydobywcze
61. [Notatki Dantego — hasło [MirrorSubway] — tekst] 거울굴절철도
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=MirrorSubway].content
   limit: do 120 znaków
   EN: Refraction Railways
   PL: Kolej Załamania
62. [Notatki Dantego — hasło [Line1] — tekst] 거울굴절철도 1호선
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=Line1].content
   limit: do 120 znaków
   EN: Refraction Railway Line 1
   PL: Kolej Załamania — Linia 1
63. [Notatki Dantego — hasło [Line2] — tekst] 거울굴절철도 2호선
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=Line2].content
   limit: do 120 znaków
   EN: Refraction Railway Line 2
   PL: Kolej Załamania — Linia 2
64. [Notatki Dantego — hasło [DieciAsso] — tekst] 디에치 협회
   źródło: StoryTheaterDanteNote_4.json :: dataList[id=DieciAsso].content
   limit: do 120 znaków
   EN: Dieci Association
   PL: Stowarzyszenie Dieci

## Notatki Dantego — hasło: StoryTheaterDanteNote_5
- plik gry: `StoryTheaterDanteNote_5.json`

65. [Notatki Dantego — hasło [MemoryDelete] — tekst] 기억 소거
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=MemoryDelete].content
   limit: do 120 znaków
   EN: Memory Wipe Procedure
   PL: Procedura Wymazania Pamięci
66. [Notatki Dantego — hasło [NestT] — tekst] T사
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=NestT].content
   limit: do 120 znaków
   EN: T Corp.
   PL: T Corp.
67. [Notatki Dantego — hasło [NestU] — tekst] U사
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=NestU].content
   limit: do 120 znaków
   EN: U Corp.
   PL: U Corp.
68. [Notatki Dantego — hasło [Library] — tekst] 도서관
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=Library].content
   limit: do 120 znaków
   EN: The Library
   PL: Biblioteka
69. [Notatki Dantego — hasło [SevenAsso] — tekst] 세븐 협회
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=SevenAsso].content
   limit: do 120 znaków
   EN: Seven Association
   PL: Stowarzyszenie Seven
70. [Notatki Dantego — hasło [DebatyAsso] — tekst] 제뱌찌 협회
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=DebatyAsso].content
   limit: do 120 znaków
   EN: Devyat' Association
   PL: Stowarzyszenie Diewiat'
71. [Notatki Dantego — hasło [Armory] — tekst] 공방
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=Armory].content
   limit: do 120 znaków
   EN: Workshops
   PL: Warsztaty
72. [Notatki Dantego — hasło [Outside] — tekst] 외곽
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=Outside].content
   limit: do 120 znaków
   EN: The Outskirts
   PL: Peryferia
73. [Notatki Dantego — hasło [GreatPond] — tekst] 대호수
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=GreatPond].content
   limit: do 120 znaków
   EN: The Great Lake
   PL: Wielkie Jezioro
74. [Notatki Dantego — hasło [Creature] — tekst] 괴물
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=Creature].content
   limit: do 120 znaków
   EN: Monsters
   PL: Potwory
75. [Notatki Dantego — hasło [Misc] — tekst] 아직 분류가 어려움
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=Misc].content
   limit: do 120 znaków
   EN: Uncategorized
   PL: Niesklasyfikowane
76. [Notatki Dantego — hasło [Walpurgis] — tekst] 발푸르기스의 밤
   źródło: StoryTheaterDanteNote_5.json :: dataList[id=Walpurgis].content
   limit: do 120 znaków
   EN: Walpurgis Night
   PL: Noc Walpurgii

## Notatki Dantego — hasło: StoryTheaterDanteNote_6
- plik gry: `StoryTheaterDanteNote_6.json`

77. [Notatki Dantego — hasło [AbnormalityLevel] — tekst] 위험등급
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=AbnormalityLevel].content
   limit: do 120 znaków
   EN: Risk Levels
   PL: Poziomy Ryzyka
78. [Notatki Dantego — hasło [LCA] — tekst] LCA
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=LCA].content
   limit: do 120 znaków
   EN: The LCA
   PL: LCA
79. [Notatki Dantego — hasło [Distortion] — tekst] 뒤틀림
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=Distortion].content
   limit: do 120 znaków
   EN: Distortions
   PL: Wypaczenia
80. [Notatki Dantego — hasło [Peccatula] — tekst] 죄종
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=Peccatula].content
   limit: do 120 znaków
   EN: Peccatula
   PL: Peccatula
81. [Notatki Dantego — hasło [NestS] — tekst] S사
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=NestS].content
   limit: do 120 znaków
   EN: S Corp.
   PL: S Corp.
82. [Notatki Dantego — hasło [LCD] — tekst] LCD
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=LCD].content
   limit: do 120 znaków
   EN: The LCD
   PL: LCD
83. [Notatki Dantego — hasło [Monolith] — tekst] 모노리스
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=Monolith].content
   limit: do 120 znaków
   EN: Monolith
   PL: Monolit
84. [Notatki Dantego — hasło [PeccatulaLv2] — tekst] 2단계 죄종
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=PeccatulaLv2].content
   limit: do 120 znaków
   EN: Stage 2 Peccatula
   PL: Peccatula 2. stadium
85. [Notatki Dantego — hasło [Line3] — tekst] 거울굴절철도 3호선
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=Line3].content
   limit: do 120 znaków
   EN: Refraction Railway Line 3
   PL: Kolej Załamania — Linia 3
86. [Notatki Dantego — hasło [BattlePower] — tekst] 전투력
   źródło: StoryTheaterDanteNote_6.json :: dataList[id=BattlePower].content
   limit: do 120 znaków
   EN: Combat Capability
   PL: Zdolność Bojowa

## Notatki Dantego — hasło: StoryTheaterDanteNote_7
- plik gry: `StoryTheaterDanteNote_7.json`

87. [Notatki Dantego — hasło [ButlerAssoc] — tekst] 버틀러
   źródło: StoryTheaterDanteNote_7.json :: dataList[id=ButlerAssoc].content
   limit: do 120 znaków
   EN: Butlers
   PL: Kamerdynerzy
88. [Notatki Dantego — hasło [CityDirection] — tekst] 구역 특징
   źródło: StoryTheaterDanteNote_7.json :: dataList[id=CityDirection].content
   limit: do 120 znaków
   EN: Districts
   PL: Dystrykty
89. [Notatki Dantego — hasło [Line4] — tekst] 거울굴절철도 4호선
   źródło: StoryTheaterDanteNote_7.json :: dataList[id=Line4].content
   limit: do 120 znaków
   EN: Refraction Railway Line 4
   PL: Kolej Załamania — Linia 4
90. [Notatki Dantego — hasło [PDA] — tekst] PDA 단말기
   źródło: StoryTheaterDanteNote_7.json :: dataList[id=PDA].content
   limit: do 120 znaków
   EN: PDA Device
   PL: Terminal PDA

## Notatki Dantego — hasło: StoryTheaterDanteNote_8
- plik gry: `StoryTheaterDanteNote_8.json`

91. [Notatki Dantego — hasło [NestP] — tekst] P사
   źródło: StoryTheaterDanteNote_8.json :: dataList[id=NestP].content
   limit: do 120 znaków
   EN: P Corp.
   PL: P Corp.
92. [Notatki Dantego — hasło [ZweiAsso] — tekst] 츠바이 협회
   źródło: StoryTheaterDanteNote_8.json :: dataList[id=ZweiAsso].content
   limit: do 120 znaków
   EN: Zwei Association
   PL: Stowarzyszenie Zwei
93. [Notatki Dantego — hasło [Yurodivy] — tekst] 유로지비
   źródło: StoryTheaterDanteNote_8.json :: dataList[id=Yurodivy].content
   limit: do 120 znaków
   EN: Yurodiviye
   PL: Jurodiwi
94. [Notatki Dantego — hasło [DimensionTrunk] — tekst] 차원가방
   źródło: StoryTheaterDanteNote_8.json :: dataList[id=DimensionTrunk].content
   limit: do 120 znaków
   EN: Dimensional Container
   PL: Torba Wymiarowa
95. [Notatki Dantego — hasło [MirrorWorld] — tekst] 거울세계
   źródło: StoryTheaterDanteNote_8.json :: dataList[id=MirrorWorld].content
   limit: do 120 znaków
   EN: Mirror Worlds
   PL: Światy Lustrzane

## Notatki Dantego — hasło: StoryTheaterDanteNote_9
- plik gry: `StoryTheaterDanteNote_9.json`

96. [Notatki Dantego — hasło [LCE] — tekst] LCE
   źródło: StoryTheaterDanteNote_9.json :: dataList[id=LCE].content
   limit: do 120 znaków
   EN: The LCE
   PL: LCE
97. [Notatki Dantego — hasło [NestX] — tekst] X사
   źródło: StoryTheaterDanteNote_9.json :: dataList[id=NestX].content
   limit: do 120 znaków
   EN: X Corp.
   PL: X Corp.
98. [Notatki Dantego — hasło [NestM] — tekst] M사
   źródło: StoryTheaterDanteNote_9.json :: dataList[id=NestM].content
   limit: do 120 znaków
   EN: M Corp.
   PL: M Corp.
99. [Notatki Dantego — hasło [PeccatulaLv3] — tekst] 3단계 죄종
   źródło: StoryTheaterDanteNote_9.json :: dataList[id=PeccatulaLv3].content
   limit: do 120 znaków
   EN: Stage 3 Peccatula
   PL: Peccatula 3. stadium
100. [Notatki Dantego — hasło [Bloodfiend] — tekst] 혈귀
   źródło: StoryTheaterDanteNote_9.json :: dataList[id=Bloodfiend].content
   limit: do 120 znaków
   EN: Bloodfiends
   PL: Krwiożercy

## Teatr Opowieści: StoryTheaterMain-a1c7p1
- plik gry: `StoryTheaterMain-a1c7p1.json`

101. [Teatr Opowieści [CHAPTER_107] — tytuł — tylko EN w danych gry] The Dream Ending
   źródło: StoryTheaterMain-a1c7p1.json :: dataList[id=CHAPTER_107].title
   limit: do 40 znaków
   EN: The Dream Ending
   PL: Koniec Snu
102. [Teatr Opowieści [CHAPTER_107] — opis — tylko EN w danych gry] With our hearts leaden,\nwe disembark the train.\nIn me is a certain truth hidden,\nforgotten even by whom it concerns.
   źródło: StoryTheaterMain-a1c7p1.json :: dataList[id=CHAPTER_107].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: With our hearts leaden,\nwe disembark the train.\nIn me is a certain truth hidden,\nforgotten even by whom it concerns.
   PL: Z ciężkimi sercami\nwysiadamy z pociągu.\nSkrywam w sobie pewną prawdę,\nzapomnianą nawet przez tę, której dotyczy.

## Teatr Opowieści: StoryTheaterMain
- plik gry: `StoryTheaterMain.json`

103. [Teatr Opowieści [CHAPTER_100] — tytuł] 어두운 숲
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_100].title
   limit: do 40 znaków
   EN: Selva Oscura
   PL: Selva Oscura
104. [Teatr Opowieści [CHAPTER_100] — opis] 나는 검은 숲의 한 가운데에 있었다.\n이유도, 과거도 전부 잊은 채로.\n내게 주어진 것은 시계로 변한 머리와,\n숲을 박차고 튀어나온 버스뿐이었다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_100].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I stood in the middle of a black forest,\nmy reasons and past all lost to me.\nAll I had was a clock that replaced my head,\nand a bus that emerged from the woods.
   PL: Byłem pośrodku czarnego lasu.\nNie pamiętałem ani powodu, ani przeszłości.\nMiałem tylko głowę zmienioną w zegar\ni autobus, który wyrwał się z lasu.
105. [Teatr Opowieści [CHAPTER_101] — tytuł] 속하지 못하는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_101].title
   limit: do 40 znaków
   EN: The Outcast
   PL: Nieprzynależny
106. [Teatr Opowieści [CHAPTER_101] — opis] 나는 관리자가 되어 있었다.\n길잡이는, 나뭇가지를 따오라 말했고.\n나는 그리하겠다 고개를 끄덕였다.\n그것이,\n악몽 속에 피어난 가지일 줄은 모르고.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_101].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I was given the role of Manager.\nMy Guide instructed me to find a branch of gold, to which my head nodded.\nUnknowingly,\nI walked face-first into one of nightmares.
   PL: Zostałem Kierownikiem.\nPrzewodnik kazał mi zdobyć gałąź,\na ja przytaknąłem.\nNie wiedząc,\nże to gałąź, która wyrosła w koszmarze.
107. [Teatr Opowieści [CHAPTER_102] — tytuł] 사랑할 수 없는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_102].title
   limit: do 40 znaków
   EN: The Unloving
   PL: Niekochająca
108. [Teatr Opowieści [CHAPTER_102] — opis] 황금가지는 누군가에게 탈취되었다.\n길잡이는 한숨과 기회를 다시 내밀었다.\n이번에는 성공하고 싶다는 마음과 함께,\n환락과 얼음의 세계 속으로 나아갔다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_102].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Trespassers took the Golden Bough.\nSighing, the Guide offered another chance.\nDetermined to succeed this time,\nwe marched into a world\nof pleasure and ice.
   PL: Ktoś zagarnął Złotą Gałąź.\nPrzewodnik znów podał mi westchnienie i szansę.\nZ nadzieją, że tym razem się uda,\nruszyłem w świat uciech i lodu.
109. [Teatr Opowieści [CHAPTER_103] — tytuł] 마주하지 않는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_103].title
   limit: do 40 znaków
   EN: The Unconfronting
   PL: Unikający
110. [Teatr Opowieści [CHAPTER_103] — opis] 유쾌했지만 차가운 희극은 막을 내렸다.\n그리고 다가올 것은 비극이라는 걸,\n나는 어렴풋하게 예측하고 있었다.\n버스가 덜컹거렸다.\n차창 너머 보인 것은, 고요한 밤이었다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_103].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Curtains close on a blithe yet chilling comedy.\nAfterward, I could vaguely sense\nthat a tragedy lies in wait.\nThe bus rumbled along.\nIn the window, I saw fall a silent night.
   PL: Kurtyna opadła nad wesołą, choć zimną komedią.\nŻe teraz nadejdzie tragedia,\nprzeczuwałem jak przez mgłę.\nAutobus zatrząsł się na wybojach.\nZa szybą widniała cicha noc.
111. [Teatr Opowieści [CHAPTER_104] — tytuł] 변하지 않는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_104].title
   limit: do 40 znaków
   EN: The Unchanging
   PL: Niezmienny
112. [Teatr Opowieści [CHAPTER_104] — opis] 처음으로 의뢰라는 걸 받았다.\n유쾌했던 분위기도 순간일 뿐, K사 둥지 한복판에는 아수라장이 펼쳐진다.\n시간은 어김없이 돌려지고 낮게 내려앉은 누군가의 눈동자가 문득 눈에 띄었다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_104].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We received our first request.\nThe excitement was short-lived as we watched chaos unfold in the middle of K Corp's Nest.\nTime is winded as usual, and a pair of downcast eyes catch my attention.
   PL: Po raz pierwszy otrzymaliśmy prawdziwe zlecenie.\nRadosny nastrój prysł w mgnieniu oka, gdy w samym sercu Gniazda K Corp. rozpętało się piekło.\nCzas jak zwykle zostaje cofnięty, a mój wzrok przykuwają czyjeś spuszczone oczy.
113. [Teatr Opowieści [STORY_10111] — tytuł] 4구 L사 지부 던전
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10111].title
   limit: do 40 znaków
   EN: District 4 Branch Facility
   PL: Dystrykt 4 - loch w filii L Corp.
114. [Teatr Opowieści [STORY_10219] — tytuł] 10구 L사 지부 던전
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10219].title
   limit: do 40 znaków
   EN: District 10 Branch Facility
   PL: Dystrykt 10 - loch w filii L Corp.
115. [Teatr Opowieści [STORY_10322] — tytuł] 11구 L사 지부 던전
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10322].title
   limit: do 40 znaków
   EN: District 11 Branch Facility
   PL: Dystrykt 11 - loch w filii L Corp.
116. [Teatr Opowieści [STORY_10454] — tytuł] 기억 속 자아심도
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10454].title
   limit: do 40 znaków
   EN: Reminisced Fathoms of Ego
   PL: Wspomniana Głębia Ego
117. [Teatr Opowieści [CHAPTER_105] — tytuł] 악으로 규정되는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_105].title
   limit: do 40 znaków
   EN: The Evil Defining
   PL: Naznaczające Zło
118. [Teatr Opowieści [CHAPTER_105] — opis] 좁혀지지 않는 갈등 속에서,\n우리는 호수에 배를 띄웠다.\n정체를 알 수 없는 파도 속으로,\n누군가의 분노가 향했던 곳으로.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_105].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Amidst the conflict that knew no end,\nWe set sail on the Great Lake.\nInto its ineffable Waves,\nInto the flames of a certain wrath.
   PL: Pośród sporu bez końca\nwypłynęliśmy łodzią na Wielkie Jezioro.\nW sam środek niepojętych Fal,\ntam, dokąd wiódł płomień czyjegoś gniewu.
119. [Teatr Opowieści [STORY_10539] — tytuł] 칠흑 속으로
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10539].title
   limit: do 40 znaków
   EN: Into the Dark
   PL: W Kruczą Czerń
120. [Teatr Opowieści [CHAPTER_106] — tytuł] 마음이 어긋나는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_106].title
   limit: do 40 znaków
   EN: The Heartbreaking
   PL: Rozdzierające Serca
121. [Teatr Opowieści [CHAPTER_106] — opis] 색은 점점 바래어져가고,\n세찬 바람과 악천후가 우리를 찾아온다.\n차창 너머로는,\n폭풍이 내려앉은 언덕이 보인다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_106].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The colors are fading,\nand a storm is approaching.\nBeyond the glass windows,\nwe see the wuthering heights.
   PL: Barwy powoli bledną,\na naprzeciw wychodzi nam porywisty wiatr i nawałnica.\nZa szybami autobusu\nmajaczą wichrowe wzgórza.
122. [Teatr Opowieści [STORY_10736] — tytuł] 꿈에 닿으려 했던 위대한 해결사에 대한 이야기
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10736].title
   limit: do 80 znaków
   EN: The Tale of a Great Fixer Who Once Reached for The Dream
   PL: Opowieść o Wielkim Fikserze, Który Sięgnął po Marzenie
123. [Teatr Opowieści [CHAPTER_107] — tytuł] 꿈이 끝나는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_107].title
   limit: do 40 znaków
   EN: The Dream Ending
   PL: Koniec Snu
124. [Teatr Opowieści [CHAPTER_107] — opis] 무거운 마음과 함께,\n우리는 열차에서 내렸다.\n나는 하나의 사실을 숨긴다.\n그 사실의 주인조차 잊은 것을.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_107].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: With our hearts leaden,\nwe disembark the train.\nIn me is a certain truth hidden,\nforgotten even by whom it concerns.
   PL: Z ciężkimi sercami\nwysiadamy z pociągu.\nSkrywam w sobie pewną prawdę,\nzapomnianą nawet przez tę, której dotyczy.
125. [Teatr Opowieści [CHAPTER_108] — tytuł] 바라볼 수밖에 없는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_108].title
   limit: do 40 znaków
   EN: The Surrendered Witnessing
   PL: Skazany na Patrzenie
126. [Teatr Opowieści [CHAPTER_108] — opis] 그의 옥색 눈동자는,\n우리보다 조금 먼 곳을 바라보고 있었다.\n나는, 여직 그 시선의 끝을 알지 못한 채.\n건물들의 숲으로 걸음 한다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_108].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: His watching Jade eye \nsees beyond where our visions lie.\nNot yet knowing where the eye gazes,\nI walk still, into where buildings make mazes.
   PL: Jego nefrytowe oko\nspoglądało nieco dalej niż nasz wzrok.\nWciąż nie wiedząc, dokąd biegnie to spojrzenie,\nwkroczyłem w gęsty las budowli.
127. [Teatr Opowieści [STORY_10820] — tytuł] 가주 심사 2차전
   źródło: StoryTheaterMain.json :: dataList[id=STORY_10820].title
   limit: do 70 znaków
   EN: Second Round of the Family Hierarch Evaluation
   PL: Druga Runda Oceny Głowy Rodu
128. [Teatr Opowieści [CHAPTER_109] — tytuł] 끊어지지 않는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_109].title
   limit: do 40 znaków
   EN: The Unsevering
   PL: Nierozerwalne
129. [Teatr Opowieści [CHAPTER_109] — opis] 기별이 없던 버스 대신 도착한 것은,\n침범당할 리 없던 곳에서의 습격 소식이었다.\n나는 그 혼란 속에,\n가만히 드리운 것을 본다.\n그것은 붉은 실로 짜여진, 거미집이었다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_109].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Instead of the bus that never returned\ncame the news of an attack upon the unassailable.\nCaught within the chaos,\nI quietly behold what is wreathed there:\nA spider's web, woven of red thread.
   PL: Zamiast autobusu, po którym zaginął słuch,\nnadeszła wieść o napaści na miejsce zdawałoby się nietykalne.\nPośród tego zamętu\nw milczeniu patrzę na to, co zawisło nad nami:\npajęczą sieć utkaną z czerwonej nici.
130. [Teatr Opowieści [CHAPTER_110] — tytuł] 바라보아지는
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_110].title
   limit: do 40 znaków
   EN: The Gaze Bearing
   PL: Pod Spojrzeniem
131. [Teatr Opowieści [CHAPTER_110] — opis] 회색빛 사슬이 절그렁거린다.\n옥죄어진 자는 여전히 침묵한다.\n나는 순간 아득함을 느끼며,\n하늘을 올려다 보았다.\n햇살이, 따가웠다.
   źródło: StoryTheaterMain.json :: dataList[id=CHAPTER_110].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heavy do the gray chains rattle,\nbut the bound man holds his silence.\nStruck by a sudden bout of vertigo,\nI turned my gaze toward the sky.\nThe sun was beating down mercilessly.
   PL: Szare łańcuchy szczękają głucho.\nSpętany człowiek wciąż milczy.\nCzując nagły zawrót głowy,\nspojrzałem w niebo.\nSłońce paliło niemiłosiernie.

## Teatr Opowieści: StoryTheaterMirrorWorld
- plik gry: `StoryTheaterMirrorWorld.json`

132. [Teatr Opowieści [MirrorWorld_Name_1] — tekst] 흑운회와 검계의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_1].content
   limit: do 120 znaków
   EN: World of the Kurokumo Clan and Blade Lineage
   PL: Świat Klanu Kurokumo i Rodu Ostrza
133. [Teatr Opowieści [MirrorWorld_Name_2] — tekst] 남부 리우 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_2].content
   limit: do 120 znaków
   EN: World of the Liu Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Liu
134. [Teatr Opowieści [MirrorWorld_Name_3] — tekst] 남부 츠바이 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_3].content
   limit: do 120 znaków
   EN: World of the Zwei Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Zwei
135. [Teatr Opowieści [MirrorWorld_Name_4] — tekst] 남부 시 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_4].content
   limit: do 120 znaków
   EN: World of the Shi Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Shi
136. [Teatr Opowieści [MirrorWorld_Name_5] — tekst] 남부 세븐 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_5].content
   limit: do 120 znaków
   EN: World of the Seven Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Seven
137. [Teatr Opowieści [MirrorWorld_Name_6] — tekst] W사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_6].content
   limit: do 120 znaków
   EN: World of W Corp.
   PL: Świat W Corp.
138. [Teatr Opowieści [MirrorWorld_Name_7] — tekst] R사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_7].content
   limit: do 120 znaków
   EN: World of R Corp.
   PL: Świat R Corp.
139. [Teatr Opowieści [MirrorWorld_Name_8] — tekst] (2장) LCCB의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_8].content
   limit: do 120 znaków
   EN: (Ch. 2) World of the LCCB
   PL: (Rozdz. 2) Świat LCCB
140. [Teatr Opowieści [MirrorWorld_Name_9] — tekst] (1장) 구 L사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_9].content
   limit: do 120 znaków
   EN: (Ch. 1) World of L Corp.
   PL: (Rozdz. 1) Świat dawnej L Corp.
141. [Teatr Opowieści [MirrorWorld_Name_10] — tekst] (1장) 구 G사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_10].content
   limit: do 120 znaków
   EN: (Ch. 1) World of the Former G Corp.
   PL: (Rozdz. 1) Świat dawnej G Corp.
142. [Teatr Opowieści [MirrorWorld_Name_11] — tekst] (2장) J사 뒷골목의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_11].content
   limit: do 120 znaków
   EN: (Ch. 2) World of the J Corp. Backstreets
   PL: (Rozdz. 2) Świat Zaułków J Corp.
143. [Teatr Opowieści [MirrorWorld_Name_12] — tekst] (3장) N사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_12].content
   limit: do 120 znaków
   EN: (Ch. 3) World of N Corp.
   PL: (Rozdz. 3) Świat N Corp.
144. [Teatr Opowieści [MirrorWorld_Name_13] — tekst] 23구 뒷골목의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_13].content
   limit: do 120 znaków
   EN: World of the District 23 Backstreets
   PL: Świat Zaułków Dystryktu 23
145. [Teatr Opowieści [MirrorWorld_Name_14] — tekst] (4장) K사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_14].content
   limit: do 120 znaków
   EN: (Ch. 4) World of K Corp.
   PL: (Rozdz. 4) Świat K Corp.
146. [Teatr Opowieści [MirrorWorld_Name_15] — tekst] 남부 섕크 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_15].content
   limit: do 120 znaków
   EN: World of the Cinq Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Cinq
147. [Teatr Opowieści [MirrorWorld_Name_16] — tekst] 21구 뒷골목의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_16].content
   limit: do 120 znaków
   EN: World of the District 21 Backstreets
   PL: Świat Zaułków Dystryktu 21
148. [Teatr Opowieści [MirrorWorld_Name_17] — tekst] 어금니 사무소의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_17].content
   limit: do 120 znaków
   EN: World of Molar Office
   PL: Świat Biura Trzonowca
149. [Teatr Opowieści [MirrorWorld_Name_18] — tekst] 남부 디에치 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_18].content
   limit: do 120 znaków
   EN: World of the Dieci Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Dieci
150. [Teatr Opowieści [MirrorWorld_Name_19] — tekst] 로보토미 본사의 세계 - 1
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_19].content
   limit: do 120 znaków
   EN: World of Lobotomy Corporation Headquarters - 1
   PL: Świat Centrali Lobotomy Corporation - 1
151. [Teatr Opowieści [MirrorWorld_Name_20] — tekst] 도서관 옛 손님의 세계 - 1
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_20].content
   limit: do 120 znaków
   EN: World of the Former Library Guests - 1
   PL: Świat Dawnych Gości Biblioteki - 1
152. [Teatr Opowieści [MirrorWorld_Name_21] — tekst] (5장) U사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_21].content
   limit: do 120 znaków
   EN: (Ch. 5) World of U Corp.
   PL: (Rozdz. 5) Świat U Corp.
153. [Teatr Opowieści [MirrorWorld_Name_22] — tekst] 남부 외우피 협회의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_22].content
   limit: do 120 znaków
   EN: World of the Öufi Association Southern Branch
   PL: Świat Południowego Oddziału Stowarzyszenia Öufi
154. [Teatr Opowieści [MirrorWorld_Name_23] — tekst] (6장) 워더링하이츠의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_23].content
   limit: do 120 znaków
   EN: (Ch. 6) World of Wuthering Heights
   PL: (Rozdz. 6) Świat Wichrowych Wzgórz
155. [Teatr Opowieści [MirrorWorld_Name_24] — tekst] 약지의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_24].content
   limit: do 120 znaków
   EN: World of the Ring
   PL: Świat Serdecznego
156. [Teatr Opowieści [MirrorWorld_Name_25] — tekst] 20구 뒷골목의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_25].content
   limit: do 120 znaków
   EN: World of the District 20 Backstreets
   PL: Świat Zaułków Dystryktu 20
157. [Teatr Opowieści [MirrorWorld_Name_26] — tekst] T사의 세계
   źródło: StoryTheaterMirrorWorld.json :: dataList[id=MirrorWorld_Name_26].content
   limit: do 120 znaków
   EN: World of T Corp.
   PL: Świat T Corp.

## Teatr Opowieści: StoryTheaterMirrorWorldStoryTitle
- plik gry: `StoryTheaterMirrorWorldStoryTitle.json`

158. [Teatr Opowieści [MirrorWorld_Story_Title_P10102] — tekst] 남부 세븐 협회 6과, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10102].content
   limit: do 120 znaków
   EN: Seven South Section 6: Yi Sang’s Story
   PL: Południowa Sekcja 6 Stowarzyszenia Seven: historia Yi Sanga
159. [Teatr Opowieści [MirrorWorld_Story_Title_P10103] — tekst] 검계 살수, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10103].content
   limit: do 120 znaków
   EN: Blade Lineage Salsu: Yi Sang’s Story
   PL: Salsu Rodu Ostrza: historia Yi Sanga
160. [Teatr Opowieści [MirrorWorld_Story_Title_P10202] — tekst] W사 2등급 정리 요원, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10202].content
   limit: do 120 znaków
   EN: W Corp. L2 Cleanup Agent: Faust’s Story
   PL: Agent porządkowy 2. poziomu W Corp.: historia Faust
161. [Teatr Opowieści [MirrorWorld_Story_Title_P10203] — tekst] 살아남은 로보토미 직원, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10203].content
   limit: do 120 znaków
   EN: Lobotomy Corp. Remnant: Faust’s Story
   PL: Ocalała pracownica Lobotomy Corporation: historia Faust
162. [Teatr Opowieści [MirrorWorld_Story_Title_P10302] — tekst] W사 3등급 정리 요원, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10302].content
   limit: do 120 znaków
   EN: W Corp. L3 Cleanup Agent: Don Quixote’s Story
   PL: Agent porządkowy 3. poziomu W Corp.: historia Don Quixote
163. [Teatr Opowieści [MirrorWorld_Story_Title_P10303] — tekst] 남부 시 협회 5과 부장, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10303].content
   limit: do 120 znaków
   EN: Shi South Section 5 Director: Don Quixote’s Story
   PL: Dyrektor Południowej Sekcji 5 Stowarzyszenia Shi: historia Don Quixote
164. [Teatr Opowieści [MirrorWorld_Story_Title_P10402] — tekst] 남부 세븐 협회 6과, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10402].content
   limit: do 120 znaków
   EN: Seven South Section 6: Ryōshū’s Story
   PL: Południowa Sekcja 6 Stowarzyszenia Seven: historia Ryōshū
165. [Teatr Opowieści [MirrorWorld_Story_Title_P10403] — tekst] 흑운회 와카슈, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10403].content
   limit: do 120 znaków
   EN: Kurokumo Wakashu: Ryōshū’s Story
   PL: Wakashu Klanu Kurokumo: historia Ryōshū
166. [Teatr Opowieści [MirrorWorld_Story_Title_P10502] — tekst] 남부 리우 협회 6과, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10502].content
   limit: do 120 znaków
   EN: Liu South Section 6: Meursault’s Story
   PL: Południowa Sekcja 6 Stowarzyszenia Liu: historia Meursaulta
167. [Teatr Opowieści [MirrorWorld_Story_Title_P10503] — tekst] W사 2등급 정리 요원, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10503].content
   limit: do 120 znaków
   EN: W Corp. L2 Cleanup Agent: Meursault’s Story
   PL: Agent porządkowy 2. poziomu W Corp.: historia Meursaulta
168. [Teatr Opowieści [MirrorWorld_Story_Title_P10602] — tekst] 흑운회 와카슈, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10602].content
   limit: do 120 znaków
   EN: Kurokumo Wakashu: Hong Lu’s Story
   PL: Wakashu Klanu Kurokumo: historia Hong Lu
169. [Teatr Opowieści [MirrorWorld_Story_Title_P10603] — tekst] 콩콩이파 보스, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10603].content
   limit: do 120 znaków
   EN: Tingtang Boss: Hong Lu’s Story
   PL: Szef gangu Tingtang: historia Hong Lu
170. [Teatr Opowieści [MirrorWorld_Story_Title_P10702] — tekst] 남부 시 협회 5과, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10702].content
   limit: do 120 znaków
   EN: Shi South Section 5: Heathcliff’s Story
   PL: Południowa Sekcja 5 Stowarzyszenia Shi: historia Heathcliffa
171. [Teatr Opowieści [MirrorWorld_Story_Title_P10703] — tekst] R사 제 4무리 토끼팀, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10703].content
   limit: do 120 znaków
   EN: R Corp. 4th Pack Rabbit: Heathcliff’s Story
   PL: Zespół Królików 4. Stada R Corp.: historia Heathcliffa
172. [Teatr Opowieści [MirrorWorld_Story_Title_P10802] — tekst] R사 제 4무리 순록팀, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10802].content
   limit: do 120 znaków
   EN: R Corp. 4th Pack Reindeer: Ishmael’s Story
   PL: Zespół Reniferów 4. Stada R Corp.: historia Ishmael
173. [Teatr Opowieści [MirrorWorld_Story_Title_P10803] — tekst] 남부 시 협회 5과, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10803].content
   limit: do 120 znaków
   EN: Shi South Section 5: Ishmael’s Story
   PL: Południowa Sekcja 5 Stowarzyszenia Shi: historia Ishmael
174. [Teatr Opowieści [MirrorWorld_Story_Title_P10804] — tekst] LCCB 대리, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10804].content
   limit: do 120 znaków
   EN: LCCB Assistant Manager: Ishmael’s Story
   PL: Zastępca kierownika LCCB: historia Ishmael
175. [Teatr Opowieści [MirrorWorld_Story_Title_P10902] — tekst] 흑운회 와카슈, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10902].content
   limit: do 120 znaków
   EN: Kurokumo Wakashu: Rodion’s Story
   PL: Wakashu Klanu Kurokumo: historia Rodion
176. [Teatr Opowieści [MirrorWorld_Story_Title_P10903] — tekst] LCCB 대리, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10903].content
   limit: do 120 znaków
   EN: LCCB Assistant Manager: Rodion’s Story
   PL: Zastępca kierownika LCCB: historia Rodion
177. [Teatr Opowieści [MirrorWorld_Story_Title_P11002] — tekst] 검계 살수, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11002].content
   limit: do 120 znaków
   EN: Blade Lineage Salsu: Sinclair’s Story
   PL: Salsu Rodu Ostrza: historia Sinclaira
178. [Teatr Opowieści [MirrorWorld_Story_Title_P11003] — tekst] 남부 츠바이 협회 6과, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11003].content
   limit: do 120 znaków
   EN: Zwei South Section 6: Sinclair’s Story
   PL: Południowa Sekcja 6 Stowarzyszenia Zwei: historia Sinclaira
179. [Teatr Opowieści [MirrorWorld_Story_Title_P11004] — tekst] 마리아치 보스, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11004].content
   limit: do 120 znaków
   EN: Jefe de Los Mariachis: Sinclair’s Story
   PL: Szef Los Mariachis: historia Sinclaira
180. [Teatr Opowieści [MirrorWorld_Story_Title_P11102] — tekst] 검계 살수, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11102].content
   limit: do 120 znaków
   EN: Blade Lineage Salsu: Outis’s Story
   PL: Salsu Rodu Ostrza: historia Outis
181. [Teatr Opowieści [MirrorWorld_Story_Title_P11103] — tekst] G사 부장, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11103].content
   limit: do 120 znaków
   EN: G Corp. Head Manager: Outis’s Story
   PL: Dyrektor G Corp.: historia Outis
182. [Teatr Opowieści [MirrorWorld_Story_Title_P11202] — tekst] 남부 리우 협회 6과, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11202].content
   limit: do 120 znaków
   EN: Liu South Section 6: Gregor’s Story
   PL: Południowa Sekcja 6 Stowarzyszenia Liu: historia Gregora
183. [Teatr Opowieści [MirrorWorld_Story_Title_P11203] — tekst] G사 일등대리, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11203].content
   limit: do 120 znaków
   EN: G Corp. Manager Corporal: Gregor’s Story
   PL: Zastępca kierownika pierwszej klasy G Corp.: historia Gregora
184. [Teatr Opowieści [MirrorWorld_Story_Title_P10504] — tekst] N사 큰 망치, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10504].content
   limit: do 120 znaków
   EN: N Corp. Großhammer: Meursault’s Story
   PL: Wielki Młot N Corp.: historia Meursaulta
185. [Teatr Opowieści [MirrorWorld_Story_Title_P10904] — tekst] N사 중간 망치, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10904].content
   limit: do 120 znaków
   EN: N Corp. Mittelhammer: Rodion’s Story
   PL: Średni Młot N Corp.: historia Rodion
186. [Teatr Opowieści [MirrorWorld_Story_Title_P10204] — tekst] 쥐는 자, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10204].content
   limit: do 120 znaków
   EN: The One Who Grips: Faust’s Story
   PL: Dzierżąca: historia Faust
187. [Teatr Opowieści [MirrorWorld_Story_Title_P10704] — tekst] N사 작은 망치, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10704].content
   limit: do 120 znaków
   EN: N Corp. Kleinhammer: Heathcliff’s Story
   PL: Mały Młot N Corp.: historia Heathcliffa
188. [Teatr Opowieści [MirrorWorld_Story_Title_P11104] — tekst] 남부 세븐 협회 6과 부장, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11104].content
   limit: do 120 znaków
   EN: Seven South Section 6 Director: Outis’s Story
   PL: Dyrektor Południowej Sekcji 6 Stowarzyszenia Seven: historia Outis
189. [Teatr Opowieści [MirrorWorld_Story_Title_P10604] — tekst] 남부 리우 협회 5과, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10604].content
   limit: do 120 znaków
   EN: Liu South Section 5: Hong Lu’s Story
   PL: Południowa Sekcja 5 Stowarzyszenia Liu: historia Hong Lu
190. [Teatr Opowieści [MirrorWorld_Story_Title_P10404] — tekst] 료. 고. 파. 주방장, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10404].content
   limit: do 120 znaków
   EN: R.B. Chef de Cuisine: Ryōshū’s Story
   PL: Szef kuchni R.P.M.: historia Ryōshū
191. [Teatr Opowieści [MirrorWorld_Story_Title_P11204] — tekst] 료. 고. 파. 조수, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11204].content
   limit: do 120 znaków
   EN: R.B. Sous-chef: Gregor’s Story
   PL: Pomoc kuchenna R.P.M.: historia Gregora
192. [Teatr Opowieści [MirrorWorld_Story_Title_P10304] — tekst] N사 중간 망치, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10304].content
   limit: do 120 znaków
   EN: N Corp. Mittelhammer: Don Quixote’s Story
   PL: Średni Młot N Corp.: historia Don Quixote
193. [Teatr Opowieści [MirrorWorld_Story_Title_P11005] — tekst] 쥐어들 자, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11005].content
   limit: do 120 znaków
   EN: The One Who Shall Grip: Sinclair’s Story
   PL: Ten, który będzie dzierżył: historia Sinclaira
194. [Teatr Opowieści [MirrorWorld_Story_Title_P10905] — tekst] 장미스패너 공방 대표, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10905].content
   limit: do 120 znaków
   EN: Rosespanner Workshop Rep: Rodion's Story
   PL: Szefowa Warsztatu Różanego Klucza: historia Rodion
195. [Teatr Opowieści [MirrorWorld_Story_Title_P10505] — tekst] 장미스패너 공방 해결사, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10505].content
   limit: do 120 znaków
   EN: Rosespanner Workshop Fixer: Meursault's Story
   PL: Fikser Warsztatu Różanego Klucza: historia Meursaulta
196. [Teatr Opowieści [MirrorWorld_Story_Title_P10705] — tekst] 로보토미 E.G.O 여우비, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10705].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Sunshower: Heathcliff's Story
   PL: Lobotomy E.G.O::Lisi Deszcz: historia Heathcliffa
197. [Teatr Opowieści [MirrorWorld_Story_Title_P11205] — tekst] 장미스패너 공방 해결사, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11205].content
   limit: do 120 znaków
   EN: Rosespanner Workshop Fixer: Gregor's Story
   PL: Fikser Warsztatu Różanego Klucza: historia Gregora
198. [Teatr Opowieści [MirrorWorld_Story_Title_P10104] — tekst] 개화 E.G.O 동백, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10104].content
   limit: do 120 znaków
   EN: Effloresced E.G.O Spicebush: Yi Sang's Story
   PL: Rozkwitłe E.G.O::Krzew Korzenny: historia Yi Sanga
199. [Teatr Opowieści [MirrorWorld_Story_Title_P10805] — tekst] 로보토미 E.G.O 출렁임, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10805].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Sloshing: Ishmael's Story
   PL: Lobotomy E.G.O::Chlupot: historia Ishmael
200. [Teatr Opowieści [MirrorWorld_Story_Title_P10605] — tekst] K사 3등급 적출직 직원, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10605].content
   limit: do 120 znaków
   EN: K Corp. Class 3 Excision Staff: Hong Lu's Story
   PL: Pracownik wycinania 3. klasy K Corp.: historia Hong Lu
201. [Teatr Opowieści [MirrorWorld_Story_Title_P11006] — tekst] 로보토미 E.G.O 홍적, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11006].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Red Sheet: Sinclair's Story
   PL: Lobotomy E.G.O::Szkarłatny Talizman: historia Sinclaira
202. [Teatr Opowieści [MirrorWorld_Story_Title_P10806] — tekst] 남부 리우 협회 4과, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10806].content
   limit: do 120 znaków
   EN: Liu South Section 4: Ishmael's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Liu: historia Ishmael
203. [Teatr Opowieści [MirrorWorld_Story_Title_P10506] — tekst] R사 제 4무리 코뿔소팀, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10506].content
   limit: do 120 znaków
   EN: R Corp. 4th Pack Rhino: Meursault's Story
   PL: Zespół Nosorożców 4. Stada R Corp.: historia Meursaulta
204. [Teatr Opowieści [MirrorWorld_Story_Title_P10906] — tekst] 남부 츠바이 협회 5과, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10906].content
   limit: do 120 znaków
   EN: Zwei South Section 5: Rodion's Story
   PL: Południowa Sekcja 5 Stowarzyszenia Zwei: historia Rodion
205. [Teatr Opowieści [MirrorWorld_Story_Title_P10305] — tekst] 남부 섕크 협회 5과 부장, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10305].content
   limit: do 120 znaków
   EN: Cinq South Section 5 Director: Don Quixote’s Story
   PL: Dyrektor Południowej Sekcji 5 Stowarzyszenia Cinq: historia Don Quixote
206. [Teatr Opowieści [MirrorWorld_Story_Title_P10807] — tekst] 어금니 보트 센터 해결사, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10807].content
   limit: do 120 znaków
   EN: Molar Boatworks Fixer: Ishmael's Story
   PL: Fikserka Stoczni Trzonowca: historia Ishmael
207. [Teatr Opowieści [MirrorWorld_Story_Title_P11007] — tekst] 어금니 보트 센터 해결사, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11007].content
   limit: do 120 znaków
   EN: Molar Boatworks Fixer: Sinclair's Story
   PL: Fikser Stoczni Trzonowca: historia Sinclaira
208. [Teatr Opowieści [MirrorWorld_Story_Title_P11206] — tekst] 남부 츠바이 협회 4과, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11206].content
   limit: do 120 znaków
   EN: Zwei South Section 4: Gregor’s Story
   PL: Południowa Sekcja 4 Stowarzyszenia Zwei: historia Gregora
209. [Teatr Opowieści [MirrorWorld_Story_Title_P10205] — tekst] 남부 츠바이 협회 4과, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10205].content
   limit: do 120 znaków
   EN: Zwei South Section 4: Faust's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Zwei: historia Faust
210. [Teatr Opowieści [MirrorWorld_Story_Title_P10405] — tekst] W사 3등급 정리 요원, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10405].content
   limit: do 120 znaków
   EN: W Corp. L3 Cleanup Agent: Ryōshū's Story
   PL: Agent porządkowy 3. poziomu W Corp.: historia Ryōshū
211. [Teatr Opowieści [MirrorWorld_Story_Title_P10606] — tekst] W사 2등급 정리 요원, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10606].content
   limit: do 120 znaków
   EN: W Corp. L2 Cleanup Agent: Hong Lu's Story
   PL: Agent porządkowy 2. poziomu W Corp.: historia Hong Lu
212. [Teatr Opowieści [MirrorWorld_Story_Title_P10206] — tekst] 남부 세븐 협회 4과, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10206].content
   limit: do 120 znaków
   EN: Seven South Section 4: Faust's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Seven: historia Faust
213. [Teatr Opowieści [MirrorWorld_Story_Title_P10706] — tekst] 남부 세븐 협회 4과, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10706].content
   limit: do 120 znaków
   EN: Seven South Section 4: Heathcliff’s Story
   PL: Południowa Sekcja 4 Stowarzyszenia Seven: historia Heathcliffa
214. [Teatr Opowieści [MirrorWorld_Story_Title_P10105] — tekst] 어금니 사무소 해결사, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10105].content
   limit: do 120 znaków
   EN: Molar Office Fixer: Yi Sang's Story
   PL: Fikser Biura Trzonowca: historia Yi Sanga
215. [Teatr Opowieści [MirrorWorld_Story_Title_P11105] — tekst] 어금니 사무소 해결사, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11105].content
   limit: do 120 znaków
   EN: Molar Office Fixer: Outis's Story
   PL: Fikserka Biura Trzonowca: historia Outis
216. [Teatr Opowieści [MirrorWorld_Story_Title_P10907] — tekst] 남부 디에치 협회 4과, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10907].content
   limit: do 120 znaków
   EN: Dieci South Section 4: Rodion's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Dieci: historia Rodion
217. [Teatr Opowieści [MirrorWorld_Story_Title_P10207] — tekst] 로보토미 E.G.O 후회, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10207].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Regret: Faust's Story
   PL: Lobotomy E.G.O::Żal: historia Faust
218. [Teatr Opowieści [MirrorWorld_Story_Title_P10607] — tekst] 갈고리 사무소 해결사, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10607].content
   limit: do 120 znaków
   EN: Hook Office Fixer: Hong Lu's Story
   PL: Fikser Biura Haka: historia Hong Lu
219. [Teatr Opowieści [MirrorWorld_Story_Title_P10106] — tekst] W사 3등급 정리 요원, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10106].content
   limit: do 120 znaków
   EN: W Corp. L3 Cleanup Agent: Yi Sang's Story
   PL: Agent porządkowy 3. poziomu W Corp.: historia Yi Sanga
220. [Teatr Opowieści [MirrorWorld_Story_Title_P11207] — tekst] 쌍갈고리 해적단 부선장, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11207].content
   limit: do 120 znaków
   EN: Twinhook Pirates First Mate: Gregor's Story
   PL: Pierwszy oficer Piratów Podwójnego Haka: historia Gregora
221. [Teatr Opowieści [MirrorWorld_Story_Title_P10406] — tekst] LCCB 대리, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10406].content
   limit: do 120 znaków
   EN: LCCB Assistant Manager: Ryōshū’s Story
   PL: Zastępca kierownika LCCB: historia Ryōshū
222. [Teatr Opowieści [MirrorWorld_Story_Title_P10306] — tekst] 중지 작은 아우, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10306].content
   limit: do 120 znaków
   EN: The Middle Little Sister: Don Quixote's Story
   PL: Młodsza Siostra Środkowego: historia Don Quixote
223. [Teatr Opowieści [MirrorWorld_Story_Title_P10507] — tekst] 중지 작은 아우, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10507].content
   limit: do 120 znaków
   EN: The Middle Little Brother: Meursault's Story
   PL: Młodszy Brat Środkowego: historia Meursaulta
224. [Teatr Opowieści [MirrorWorld_Story_Title_P10707] — tekst] 피쿼드호 작살잡이, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10707].content
   limit: do 120 znaków
   EN: The Pequod Harpooneer: Heathcliff's Story
   PL: Harpunnik Pequoda: historia Heathcliffa
225. [Teatr Opowieści [MirrorWorld_Story_Title_P10107] — tekst] 피쿼드호 일등 항해사, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10107].content
   limit: do 120 znaków
   EN: The Pequod First Mate: Yi Sang's Story
   PL: Pierwszy oficer Pequoda: historia Yi Sanga
226. [Teatr Opowieści [MirrorWorld_Story_Title_P11008] — tekst] 남부 섕크 협회 4과 부장, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11008].content
   limit: do 120 znaków
   EN: Cinq South Section 4 Director: Sinclair's Story
   PL: Dyrektor Południowej Sekcji 4 Stowarzyszenia Cinq: historia Sinclaira
227. [Teatr Opowieści [MirrorWorld_Story_Title_P11106] — tekst] 남부 섕크 협회 4과, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11106].content
   limit: do 120 znaków
   EN: Cinq South Section 4: Outis's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Cinq: historia Outis
228. [Teatr Opowieści [MirrorWorld_Story_Title_P11107] — tekst] 로보토미 E.G.O 마탄, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11107].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Magic Bullet Outis's Story
   PL: Lobotomy E.G.O::Magiczny Pocisk: historia Outis
229. [Teatr Opowieści [MirrorWorld_Story_Title_P10307] — tekst] 로보토미 E.G.O 초롱, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10307].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Lantern Don Quixote's Story
   PL: Lobotomy E.G.O::Latarnia: historia Don Quixote
230. [Teatr Opowieści [MirrorWorld_Story_Title_P10608] — tekst] 남부 디에치 협회 4과, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10608].content
   limit: do 120 znaków
   EN: Dieci South Section 4: Hong Lu's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Dieci: historia Hong Lu
231. [Teatr Opowieści [MirrorWorld_Story_Title_P10108] — tekst] 남부 디에치 협회 4과, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10108].content
   limit: do 120 znaków
   EN: Dieci South Section 4: Yi Sang's Story
   PL: Południowa Sekcja 4 Stowarzyszenia Dieci: historia Yi Sanga
232. [Teatr Opowieści [MirrorWorld_Story_Title_P10808] — tekst] 피쿼드호 선장, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10808].content
   limit: do 120 znaków
   EN: The Pequod Captain: Ishmael’s Story
   PL: Kapitan Pequoda: historia Ishmael
233. [Teatr Opowieści [MirrorWorld_Story_Title_P10508] — tekst] 검계 우두머리, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10508].content
   limit: do 120 znaków
   EN: Blade Lineage Mentor: Meursault's Story
   PL: Mentor Rodu Ostrza: historia Meursaulta
234. [Teatr Opowieści [MirrorWorld_Story_Title_P10208] — tekst] 검계 살수, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10208].content
   limit: do 120 znaków
   EN: Blade Lineage Salsu: Faust's Story
   PL: Salsu Rodu Ostrza: historia Faust
235. [Teatr Opowieści [MirrorWorld_Story_Title_P11208] — tekst] 흑운회 부조장, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11208].content
   limit: do 120 znaków
   EN: Kurokumo Clan Captain: Gregor's Story
   PL: Kapitan Klanu Kurokumo: historia Gregora
236. [Teatr Opowieści [MirrorWorld_Story_Title_P10308] — tekst] 검계 살수, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10308].content
   limit: do 120 znaków
   EN: Blade Lineage Salsu: Don Quixote's Story
   PL: Salsu Rodu Ostrza: historia Don Quixote
237. [Teatr Opowieści [MirrorWorld_Story_Title_P10908] — tekst] 남부 리우 협회 4과 부장, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10908].content
   limit: do 120 znaków
   EN: Liu South Section 4 Director: Rodion's Story
   PL: Dyrektor Południowej Sekcji 4 Stowarzyszenia Liu: historia Rodion
238. [Teatr Opowieści [MirrorWorld_Story_Title_P10407] — tekst] 남부 리우 협회 4과, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10407].content
   limit: do 120 znaków
   EN: Liu South Section 4: Ryōshū’s Story
   PL: Południowa Sekcja 4 Stowarzyszenia Liu: historia Ryōshū
239. [Teatr Opowieści [MirrorWorld_Story_Title_P10708] — tekst] 남부 외우피 협회 3과, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10708].content
   limit: do 120 znaków
   EN: Öufi South Section 3: Heathcliff's Story
   PL: Południowa Sekcja 3 Stowarzyszenia Öufi: historia Heathcliffa
240. [Teatr Opowieści [MirrorWorld_Story_Title_P11108] — tekst] 워더링하이츠 치프 버틀러, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11108].content
   limit: do 120 znaków
   EN: Wuthering Heights Chief Butler: Outis's Story
   PL: Główna Kamerdynerka Wichrowych Wzgórz: historia Outis
241. [Teatr Opowieści [MirrorWorld_Story_Title_P10509] — tekst] 데드레빗츠 보스, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10509].content
   limit: do 120 znaków
   EN: Dead Rabbits Boss: Meursault's Story
   PL: Szef Martwych Królików: historia Meursaulta
242. [Teatr Opowieści [MirrorWorld_Story_Title_P11209] — tekst] 에드가 가문 승계자, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11209].content
   limit: do 120 znaków
   EN: Edgar Family Heir: Gregor's Story
   PL: Dziedzic Rodu Edgarów: historia Gregora
243. [Teatr Opowieści [MirrorWorld_Story_Title_P10209] — tekst] 워더링하이츠 버틀러, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10209].content
   limit: do 120 znaków
   EN: Wuthering Heights Butler: Faust's Story
   PL: Kamerdynerka Wichrowych Wzgórz: historia Faust
244. [Teatr Opowieści [MirrorWorld_Story_Title_P10408] — tekst] 에드가 가문 치프 버틀러, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10408].content
   limit: do 120 znaków
   EN: Edgar Family Chief Butler: Ryōshū's Story
   PL: Główna Kamerdynerka Rodu Edgarów: historia Ryōshū
245. [Teatr Opowieści [MirrorWorld_Story_Title_P10809] — tekst] 에드가 가문 버틀러, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10809].content
   limit: do 120 znaków
   EN: Edgar Family Butler: Ishmael's Story
   PL: Kamerdynerka Rodu Edgarów: historia Ishmael
246. [Teatr Opowieści [MirrorWorld_Story_Title_P11009] — tekst] 새벽 사무소 해결사, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11009].content
   limit: do 120 znaków
   EN: Dawn Office Fixer: Sinclair's Story
   PL: Fikser Biura Świtu: historia Sinclaira
247. [Teatr Opowieści [MirrorWorld_Story_Title_P10109] — tekst] 약지 점묘파 스튜던트, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10109].content
   limit: do 120 znaków
   EN: The Ring Pointillist Student: Yi Sang's Story
   PL: Student Pointylizmu Serdecznego: historia Yi Sanga
248. [Teatr Opowieści [MirrorWorld_Story_Title_P11109] — tekst] 약지 점묘파 스튜던트, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11109].content
   limit: do 120 znaków
   EN: The Ring Pointillist Student: Outis's Story
   PL: Studentka Pointylizmu Serdecznego: historia Outis
249. [Teatr Opowieści [MirrorWorld_Story_Title_P10609] — tekst] 20구 유로지비, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10609].content
   limit: do 120 znaków
   EN: District 20 Yurodivy: Hong Lu's Story
   PL: Jurodiwy z Dystryktu 20: historia Hong Lu
250. [Teatr Opowieści [MirrorWorld_Story_Title_P10409] — tekst] 20구 유로지비, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10409].content
   limit: do 120 znaków
   EN: District 20 Yurodivy: Ryōshū's story
   PL: Jurodiwa z Dystryktu 20: historia Ryōshū
251. [Teatr Opowieści [MirrorWorld_Story_Title_P10309] — tekst] T사 3등급 징수직 직원, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10309].content
   limit: do 120 znaków
   EN: T Corp. Class 3 Collection Staff: Don Quixote's Story
   PL: Poborca 3. klasy T Corp.: historia Don Quixote
252. [Teatr Opowieści [MirrorWorld_Story_Title_P10909] — tekst] T사 2등급 징수직 직원, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10909].content
   limit: do 120 znaków
   EN: T Corp. Class 2 Collection Staff: Rodion's Story
   PL: Poborca 2. klasy T Corp.: historia Rodion
253. [Teatr Opowieści [MirrorWorld_Story_Title_P10510] — tekst] 남부 디에치 협회 4과 부장, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10510].content
   limit: do 120 znaków
   EN: Dieci South Section 4 Director: Meursault's Story
   PL: Dyrektor Południowej Sekcji 4 Stowarzyszenia Dieci: historia Meursaulta
254. [Teatr Opowieści [MirrorWorld_Story_Title_P11110] — tekst] W사 3등급 정리 요원 팀장, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11110].content
   limit: do 120 znaków
   EN: W Corp. L3 Cleanup Captain: Outis's Story
   PL: Kapitan porządkowa 3. poziomu W Corp.: historia Outis
255. [Teatr Opowieści [MirrorWorld_Story_Title_P10210] — tekst] 멀티크랙 사무소 대표, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10210].content
   limit: do 120 znaków
   EN: MultiCrack Office Rep: Faust's Story
   PL: Szefowa Biura MultiCrack: historia Faust
256. [Teatr Opowieści [MirrorWorld_Story_Title_P10709] — tekst] 멀티크랙 사무소 해결사, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10709].content
   limit: do 120 znaków
   EN: MultiCrack Office Fixer: Heathcliff's Story
   PL: Fikser Biura MultiCrack: historia Heathcliffa
257. [Teatr Opowieści [MirrorWorld_Story_Title_P10710] — tekst] 와일드헌트, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10710].content
   limit: do 120 znaków
   EN: Wild Hunt: Heathcliff's Story
   PL: Dziki Gon: historia Heathcliffa
258. [Teatr Opowieści [MirrorWorld_Story_Title_P10110] — tekst] 로보토미 E.G.O 엄숙한 애도, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10110].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Solemn Lament Yi Sang's Story
   PL: Lobotomy E.G.O::Uroczysty Lament: historia Yi Sanga
259. [Teatr Opowieści [MirrorWorld_Story_Title_P10410] — tekst] 로보토미 E.G.O 적안・참회, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10410].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Red Eyes & Penitence Ryōshū's Story
   PL: Lobotomy E.G.O::Czerwone Oczy i Pokuta: historia Ryōshū
260. [Teatr Opowieści [MirrorWorld_Story_Title_P10910] — tekst] 북부 제뱌찌 협회 3과, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10910].content
   limit: do 120 znaków
   EN: Devyat' North Section 3: Rodion's Story
   PL: Północna Sekcja 3 Stowarzyszenia Diewiat': historia Rodion
261. [Teatr Opowieści [MirrorWorld_Story_Title_P10810] — tekst] 서부 츠바이 협회 3과, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10810].content
   limit: do 120 znaków
   EN: Zwei West Section 3: Ishmael's Story
   PL: Zachodnia Sekcja 3 Stowarzyszenia Zwei: historia Ishmael
262. [Teatr Opowieści [MirrorWorld_Story_Title_P10511] — tekst] 서부 섕크 협회 3과, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10511].content
   limit: do 120 znaków
   EN: Cinq West Section 3: Meursault’s Story
   PL: Zachodnia Sekcja 3 Stowarzyszenia Cinq: historia Meursaulta
263. [Teatr Opowieści [MirrorWorld_Story_Title_P11010] — tekst] 서부 츠바이 협회 3과, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11010].content
   limit: do 120 znaków
   EN: Zwei West Section 3: Sinclair’s Story
   PL: Zachodnia Sekcja 3 Stowarzyszenia Zwei: historia Sinclaira
264. [Teatr Opowieści [MirrorWorld_Story_Title_P11111] — tekst] 라만차랜드 이발사, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11111].content
   limit: do 120 znaków
   EN: The Barber of La Manchaland: Outis's Story
   PL: Cyruliczka La Manchalandu: historia Outis
265. [Teatr Opowieści [MirrorWorld_Story_Title_P10610] — tekst] 송곳니 사냥 사무소 해결사, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10610].content
   limit: do 120 znaków
   EN: Fanghunt Office Fixer: Hong Lu's Story
   PL: Fikser Biura Łowców Kłów: historia Hong Lu
266. [Teatr Opowieści [MirrorWorld_Story_Title_P11210] — tekst] 라만차랜드 신부, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11210].content
   limit: do 120 znaków
   EN: The Priest of La Manchaland: Gregor's Story
   PL: Ksiądz La Manchalandu: historia Gregora
267. [Teatr Opowieści [MirrorWorld_Story_Title_P10911] — tekst] 라만차랜드 공주, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10911].content
   limit: do 120 znaków
   EN: The Princess of La Manchaland: Rodion's Story
   PL: Księżniczka La Manchalandu: historia Rodion
268. [Teatr Opowieści [MirrorWorld_Story_Title_P11011] — tekst] 북부 제뱌찌 협회 3과, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11011].content
   limit: do 120 znaków
   EN: Devyat' North Section 3: Sinclair's Story
   PL: Północna Sekcja 3 Stowarzyszenia Diewiat': historia Sinclaira
269. [Teatr Opowieści [MirrorWorld_Story_Title_P10310] — tekst] 라만차랜드 실장, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10310].content
   limit: do 120 znaków
   EN: The Manager of La Manchaland: Don Quixote's Story
   PL: Zarządczyni La Manchalandu: historia Don Quixote
270. [Teatr Opowieści [MirrorWorld_Story_Title_P10611] — tekst] 마침표 사무소 대표, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10611].content
   limit: do 120 znaków
   EN: Full-Stop Office Rep: Hong Lu's Story
   PL: Szef Biura Kropki: historia Hong Lu
271. [Teatr Opowieści [MirrorWorld_Story_Title_P10711] — tekst] 마침표 사무소 해결사, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10711].content
   limit: do 120 znaków
   EN: Full-Stop Office Fixer: Heathcliff's Story
   PL: Fikser Biura Kropki: historia Heathcliffa
272. [Teatr Opowieści [MirrorWorld_Story_Title_P10211] — tekst] LCE E.G.O 홍염살, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10211].content
   limit: do 120 znaków
   EN: LCE E.G.O Ardor Blossom Star: Faust's Story
   PL: LCE E.G.O::Gwiazda Żarzącego Kwiatu: historia Faust
273. [Teatr Opowieści [MirrorWorld_Story_Title_P10111] — tekst] LCE E.G.O 초롱, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10111].content
   limit: do 120 znaków
   EN: LCE E.G.O Lantern, Yi Sang's Story
   PL: LCE E.G.O::Latarnia: historia Yi Sanga
274. [Teatr Opowieści [MirrorWorld_Story_Title_P10811] — tekst] 흑운회 부조장, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10811].content
   limit: do 120 znaków
   EN: Kurokumo Clan Captain: Ishmael's Story
   PL: Kapitan Klanu Kurokumo: historia Ishmael
275. [Teatr Opowieści [MirrorWorld_Story_Title_P10712] — tekst] 흑운회 와카슈, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10712].content
   limit: do 120 znaków
   EN: Kurokumo Clan Wakashu: Heathcliff's Story
   PL: Wakashu Klanu Kurokumo: historia Heathcliffa
276. [Teatr Opowieści [MirrorWorld_Story_Title_P10112] — tekst] 남부 리우 협회 3과, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10112].content
   limit: do 120 znaków
   EN: Liu South Section 3: Yi Sang's Story
   PL: Południowa Sekcja 3 Stowarzyszenia Liu: historia Yi Sanga
277. [Teatr Opowieści [MirrorWorld_Story_Title_P10311] — tekst] 동부 섕크 협회 3과, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10311].content
   limit: do 120 znaków
   EN: Cinq East Section 3: Don Quixote’s Story
   PL: Wschodnia Sekcja 3 Stowarzyszenia Cinq: historia Don Quixote
278. [Teatr Opowieści [MirrorWorld_Story_Title_P11211] — tekst] 불주먹 사무소 생존자, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11211].content
   limit: do 120 znaków
   EN: Firefist Office Survivor: Gregor's Story
   PL: Ocalały z Biura Ognistej Pięści: historia Gregora
279. [Teatr Opowieści [MirrorWorld_Story_Title_P11112] — tekst] 흑수 - 묘, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11112].content
   limit: do 120 znaków
   EN: Heishou Pack - Mao Branch: Outis's Story
   PL: Wataha Heishou - Gałąź Mao: historia Outis
280. [Teatr Opowieści [MirrorWorld_Story_Title_P10411] — tekst] 흑수 - 묘, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10411].content
   limit: do 120 znaków
   EN: Heishou Pack - Mao Branch: Ryōshū's Story
   PL: Wataha Heishou - Gałąź Mao: historia Ryōshū
281. [Teatr Opowieści [MirrorWorld_Story_Title_P11012] — tekst] 중지 작은 아우, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11012].content
   limit: do 120 znaków
   EN: The Middle Little Brother: Sinclair's Story
   PL: Młodszy Brat Środkowego: historia Sinclaira
282. [Teatr Opowieści [MirrorWorld_Story_Title_P10612] — tekst] R사 제 4무리 순록팀, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10612].content
   limit: do 120 znaków
   EN: R Corp. 4th Pack Reindeer: Hong Lu's Story
   PL: Zespół Reniferów 4. Stada R Corp.: historia Hong Lu
283. [Teatr Opowieści [MirrorWorld_Story_Title_P11212] — tekst] 흑수 - 사, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11212].content
   limit: do 120 znaków
   EN: Heishou Pack - Si Branch: Gregor's Story
   PL: Wataha Heishou - Gałąź Si: historia Gregora
284. [Teatr Opowieści [MirrorWorld_Story_Title_P10912] — tekst] 흑수 - 사, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10912].content
   limit: do 120 znaków
   EN: Heishou Pack - Si Branch: Rodion's Story
   PL: Wataha Heishou - Gałąź Si: historia Rodion
285. [Teatr Opowieści [MirrorWorld_Story_Title_P10212] — tekst] 흑수 - 묘 필두, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10212].content
   limit: do 120 znaków
   EN: Heishou Pack - Mao Branch Adept: Faust's Story
   PL: Adeptka Watahy Heishou - Gałąź Mao: historia Faust
286. [Teatr Opowieści [MirrorWorld_Story_Title_P10812] — tekst] 가주 후보, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10812].content
   limit: do 120 znaków
   EN: Family Hierarch Candidate: Ishmael's Story
   PL: Kandydatka na Głowę Rodu: historia Ishmael
287. [Teatr Opowieści [MirrorWorld_Story_Title_P10512] — tekst] 동부 엄지 카포IIII, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10512].content
   limit: do 120 znaków
   EN: The Thumb East Capo IIII: Meursault's Story
   PL: Wschodni Capo IIII Kciuka: historia Meursaulta
288. [Teatr Opowieści [MirrorWorld_Story_Title_P11013] — tekst] 동부 엄지 솔다토II, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11013].content
   limit: do 120 znaków
   EN: The Thumb East Soldato II: Sinclair's Story
   PL: Wschodni Soldato II Kciuka: historia Sinclaira
289. [Teatr Opowieści [MirrorWorld_Story_Title_P10113] — tekst] N사 E.G.O 흉탄, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10113].content
   limit: do 120 znaków
   EN: N Corp. E.G.O Fell Bullet: Yi Sang's Story
   PL: N Corp. E.G.O::Złowroga Kula: historia Yi Sanga
290. [Teatr Opowieści [MirrorWorld_Story_Title_P10312] — tekst] 로보토미 E.G.O 사랑과 증오의 이름으로, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10312].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O In the Name of Love and Hate Don Quixote's Story
   PL: Lobotomy E.G.O::W Imię Miłości i Nienawiści: historia Don Quixote
291. [Teatr Opowieści [MirrorWorld_Story_Title_P10913] — tekst] 로보토미 E.G.O 눈물로 벼려낸 검, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10913].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O The Sword Sharpened with Tears Rodion's Story
   PL: Lobotomy E.G.O::Miecz Wyostrzony Łzami: historia Rodion
292. [Teatr Opowieści [MirrorWorld_Story_Title_P11113] — tekst] T사 3등급 강력징수직 직원, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11113].content
   limit: do 120 znaków
   EN: T Corp. Class 3 VDCU Staff: Outis's Story
   PL: Egzekutorka 3. klasy T Corp.: historia Outis
293. [Teatr Opowieści [MirrorWorld_Story_Title_P10613] — tekst] 홍원 군주, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10613].content
   limit: do 120 znaków
   EN: The Lord of Hongyuan: Hong Lu's Story
   PL: Władca Hongyuanu: historia Hong Lu
294. [Teatr Opowieści [MirrorWorld_Story_Title_P10114] — tekst] 흑수 - 오 필두, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10114].content
   limit: do 120 znaków
   EN: Heishou Pack - Wu Branch Adept: Yi Sang's Story
   PL: Adept Watahy Heishou - Gałąź Wu: historia Yi Sanga
295. [Teatr Opowieści [MirrorWorld_Story_Title_P11014] — tekst] 흑수 - 유, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11014].content
   limit: do 120 znaków
   EN: Heishou Pack - You Branch: Sinclair's Story
   PL: Wataha Heishou - Gałąź You: historia Sinclaira
296. [Teatr Opowieści [MirrorWorld_Story_Title_P10412] — tekst] N사 E.G.O 경멸, 경외, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10412].content
   limit: do 120 znaków
   EN: N Corp. E.G.O Contempt, Awe: Ryōshū's Story
   PL: N Corp. E.G.O::Pogarda, Trwoga: historia Ryōshū
297. [Teatr Opowieści [MirrorWorld_Story_Title_P10213] — tekst] 동부 시 협회 3과, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10213].content
   limit: do 120 znaków
   EN: Shi East Section 3: Faust's Story
   PL: Wschodnia Sekcja 3 Stowarzyszenia Shi: historia Faust
298. [Teatr Opowieści [MirrorWorld_Story_Title_P10513] — tekst] 라만차랜드 왕자, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10513].content
   limit: do 120 znaków
   EN: The Prince of La Manchaland: Meursault's Story
   PL: Książę La Manchalandu: historia Meursaulta
299. [Teatr Opowieści [MirrorWorld_Story_Title_P10713] — tekst] W사 4등급 정리 요원 - CCA, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10713].content
   limit: do 120 znaków
   EN: W Corp. L4 Cleanup Agent - CCA: Heathcliff's Story
   PL: Agent porządkowy 4. poziomu W Corp. - CCA: historia Heathcliffa
300. [Teatr Opowieści [MirrorWorld_Story_Title_P10813] — tekst] 정 사무소 대표, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10813].content
   limit: do 120 znaków
   EN: Jeong's Office Rep: Ishmael's Story
   PL: Szefowa Biura Jeonga: historia Ishmael
301. [Teatr Opowieści [MirrorWorld_Story_Title_P11213] — tekst] 밤의 송곳 카피타노, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11213].content
   limit: do 120 znaków
   EN: Night Awls Capitano: Gregor's Story
   PL: Capitano Nocnych Szydeł: historia Gregora
302. [Teatr Opowieści [MirrorWorld_Story_Title_P10313] — tekst] 흑수 - 미, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10313].content
   limit: do 120 znaków
   EN: Heishou Pack - Wei Branch: Don Quixote's Story
   PL: Wataha Heishou - Gałąź Wei: historia Don Quixote
303. [Teatr Opowieści [MirrorWorld_Story_Title_P10714] — tekst] 흑수 - 유 필두, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10714].content
   limit: do 120 znaków
   EN: Heishou Pack - You Branch Adept: Heathcliff's Story
   PL: Adept Watahy Heishou - Gałąź You: historia Heathcliffa
304. [Teatr Opowieści [MirrorWorld_Story_Title_P10413] — tekst] 홍원 방랑무사, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10413].content
   limit: do 120 znaków
   EN: Drifting Blade of Hongyuan: Ryōshū's Story
   PL: Wędrowna Szermierka z Hongyuanu: historia Ryōshū
305. [Teatr Opowieści [MirrorWorld_Story_Title_P10914] — tekst] R사 제 4무리 순록팀, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10914].content
   limit: do 120 znaków
   EN: R Corp. 4th Pack Reindeer: Rodion's Story
   PL: Zespół Reniferów 4. Stada R Corp.: historia Rodion
306. [Teatr Opowieści [MirrorWorld_Story_Title_P10214] — tekst] 검지 수행자:【쪽지】, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10214].content
   limit: do 120 znaków
   EN: The Index Proselyte: 【Paper Slip】: Faust's Story
   PL: Akolitka Wskazującego: 【Karteczka】: historia Faust
307. [Teatr Opowieści [MirrorWorld_Story_Title_P11114] — tekst] LCA 우제트 선봉3팀 팀장, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11114].content
   limit: do 120 znaków
   EN: LCA Udjat Vanguard Team 3 Leader Outis's Story
   PL: Dowódczyni 3. Zespołu Szpicy Udjat LCA: historia Outis
308. [Teatr Opowieści [MirrorWorld_Story_Title_P10314] — tekst] 검지 대행자 - 개화 E.G.O::대행, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10314].content
   limit: do 120 znaków
   EN: The Index Proxy - Effloresced E.G.O::Procuration Don Quixote's Story
   PL: Pełnomocniczka Wskazującego - Rozkwitłe E.G.O::Pełnomocnictwo: historia Don Quixote
309. [Teatr Opowieści [MirrorWorld_Story_Title_P10814] — tekst] 거미집 중지 제자, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10814].content
   limit: do 120 znaków
   EN: The House of Spiders: The Middle Apprentice Ishmael's Story
   PL: Dom Pająków — Uczennica Środkowego: historia Ishmael
310. [Teatr Opowieści [MirrorWorld_Story_Title_P11015] — tekst] 거미집 소지 제자, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11015].content
   limit: do 120 znaków
   EN: The House of Spiders: The Pinky Apprentice Sinclair's Story
   PL: Dom Pająków — Uczeń Małego Palca: historia Sinclaira
311. [Teatr Opowieści [MirrorWorld_Story_Title_P11214] — tekst] 로보토미 E.G.O 램프, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11214].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Lamp: Gregor's Story
   PL: Lobotomy E.G.O::Lampa: historia Gregora
312. [Teatr Opowieści [MirrorWorld_Story_Title_P10115] — tekst] 거미집 검지 아비, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10115].content
   limit: do 120 znaków
   EN: The House of Spiders: The Index Nursefather Yi Sang's Story
   PL: Dom Pająków — Ojciec Wskazującego: historia Yi Sanga
313. [Teatr Opowieści [MirrorWorld_Story_Title_P10414] — tekst] 로보토미 E.G.O 잔향・외로움, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10414].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O Faint Aroma & Solitude: Ryōshū's Story
   PL: Lobotomy E.G.O::Nikła Woń i Samotność: historia Ryōshū
314. [Teatr Opowieści [MirrorWorld_Story_Title_P10514] — tekst] 로보토미 E.G.O 호넷【변조】, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10514].content
   limit: do 120 znaków
   EN: Lobotomy E.G.O::Hornet 【Alteration】 Meursault's Story
   PL: Lobotomy E.G.O::Szerszeń 【Modyfikacja】: historia Meursaulta
315. [Teatr Opowieści [MirrorWorld_Story_Title_P11215] — tekst] LCE E.G.O AEDD, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11215].content
   limit: do 120 znaków
   EN: LCE E.G.O::AEDD Gregor's Story
   PL: LCE E.G.O::AEDD: historia Gregora
316. [Teatr Opowieści [MirrorWorld_Story_Title_P10614] — tekst] 거미집 약지 아비, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10614].content
   limit: do 120 znaków
   EN: The House of Spiders: The Ring Nursefather Hong Lu's Story
   PL: Dom Pająków — Ojciec Serdecznego: historia Hong Lu
317. [Teatr Opowieści [MirrorWorld_Story_Title_P10215] — tekst] 거미집 약지 제자, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10215].content
   limit: do 120 znaków
   EN: The House of Spiders: The Ring Apprentice Faust's Story
   PL: Dom Pająków — Uczennica Serdecznego: historia Faust
318. [Teatr Opowieści [MirrorWorld_Story_Title_P10915] — tekst] 약지 야수파 도슨트, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10915].content
   limit: do 120 znaków
   EN: The Ring Fauvist Docent: Rodion's Story
   PL: Docent Fowizmu Serdecznego: historia Rodion
319. [Teatr Opowieści [MirrorWorld_Story_Title_P10515] — tekst] 약지 야수파 스튜던트, 뫼르소 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10515].content
   limit: do 120 znaków
   EN: The Ring Fauvist Student: Meursault's Story
   PL: Student Fowizmu Serdecznego: historia Meursaulta
320. [Teatr Opowieści [MirrorWorld_Story_Title_P10715] — tekst] 중지 작은 형님, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10715].content
   limit: do 120 znaków
   EN: The Middle Big Brother: Heathcliff's Story
   PL: Starszy Brat Środkowego: historia Heathcliffa
321. [Teatr Opowieści [MirrorWorld_Story_Title_P10415] — tekst] 거미집의 검, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10415].content
   limit: do 120 znaków
   EN: Blade of the House of Spiders: Ryōshū's Story
   PL: Ostrze Domu Pająków: historia Ryōshū
322. [Teatr Opowieści [MirrorWorld_Story_Title_P11115] — tekst] 거미집 중지 아비, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11115].content
   limit: do 120 znaków
   EN: The House of Spiders: The Middle Nursefather Outis's Story
   PL: Dom Pająków — Matka Środkowego: historia Outis
323. [Teatr Opowieści [MirrorWorld_Story_Title_P10815] — tekst] LCD 현장추리팀, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10815].content
   limit: do 120 znaków
   EN: LCD OSIR Team: Ishmael's Story
   PL: Zespół Śledczy LCD: historia Ishmael
324. [Teatr Opowieści [MirrorWorld_Story_Title_P10615] — tekst] S사 추노꾼, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10615].content
   limit: do 120 znaków
   EN: S Corp. Ch'unokkun: Hong Lu's Story
   PL: Łowca Zbiegów S Corp.: historia Hong Lu
325. [Teatr Opowieści [MirrorWorld_Story_Title_P10716] — tekst] 거미집 엄지 제자, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10716].content
   limit: do 120 znaków
   EN: The House of Spiders: The Thumb Apprentice Heathcliff's Story
   PL: Dom Pająków — Uczeń Kciuka: historia Heathcliffa
326. [Teatr Opowieści [MirrorWorld_Story_Title_P10916] — tekst] 거미집 엄지 아비, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10916].content
   limit: do 120 znaków
   EN: The House of Spiders: The Thumb Nursefather Rodion's Story
   PL: Dom Pająków — Matka Kciuka: historia Rodion
327. [Teatr Opowieści [MirrorWorld_Story_Title_P10216] — tekst] 새벽 사무소 해결사, 파우스트 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10216].content
   limit: do 120 znaków
   EN: Dawn Office Fixer: Faust's Story
   PL: Fikserka Biura Świtu: historia Faust
328. [Teatr Opowieści [MirrorWorld_Story_Title_P11216] — tekst] 새벽 사무소 대표, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11216].content
   limit: do 120 znaków
   EN: Dawn Office Rep: Gregor's Story
   PL: Szef Biura Świtu: historia Gregora
329. [Teatr Opowieści [MirrorWorld_Story_Title_P10116] — tekst] LCE E.G.O 차원찢개, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10116].content
   limit: do 120 znaków
   EN: LCE E.G.O::Dimension Shredder, Yi Sang's Story
   PL: LCE E.G.O::Rozpruwacz Wymiarów: historia Yi Sanga
330. [Teatr Opowieści [MirrorWorld_Story_Title_P10616] — tekst] 동부 섕크 협회 3과, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10616].content
   limit: do 120 znaków
   EN: Cinq East Section 3: Hong Lu's Story
   PL: Wschodnia Sekcja 3 Stowarzyszenia Cinq: historia Hong Lu
331. [Teatr Opowieści [MirrorWorld_Story_Title_P10416] — tekst] 오트쿠튀르::르누아르 신발관, 료슈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10416].content
   limit: do 120 znaków
   EN: Haute Couture::Le Noir Footwear Hall Ryōshū's Story
   PL: Haute Couture::Pawilon Obuwia Le Noir: historia Ryōshū
332. [Teatr Opowieści [MirrorWorld_Story_Title_P10816] — tekst] 오트쿠튀르::르루주 부티크, 이스마엘 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10816].content
   limit: do 120 znaków
   EN: Haute Couture::Boutique du Rouge Ishmael's Story
   PL: Haute Couture::Boutique du Rouge: historia Ishmael
333. [Teatr Opowieści [MirrorWorld_Story_Title_P10917] — tekst] 오트쿠튀르::수선실, 로쟈 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10917].content
   limit: do 120 znaków
   EN: Haute Couture::Alteration Shop Rodion's Story
   PL: Haute Couture::Pracownia Poprawek: historia Rodion
334. [Teatr Opowieści [MirrorWorld_Story_Title_P10315] — tekst] 오트쿠튀르::르누아르 브랜드 매니저, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10315].content
   limit: do 120 znaków
   EN: Haute Couture::Le Noir Brand Manager Don Quixote's Story
   PL: Haute Couture::Menedżerka Marki Le Noir: historia Don Quixote
335. [Teatr Opowieści [MirrorWorld_Story_Title_P11016] — tekst] 오트쿠튀르::르루주 붉은 신, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11016].content
   limit: do 120 znaków
   EN: Haute Couture::The Crimson God of Le Rouge Sinclair's Story
   PL: Haute Couture::Szkarłatny Bóg Le Rouge: historia Sinclaira
336. [Teatr Opowieści [MirrorWorld_Story_Title_P10717] — tekst] 오트쿠튀르::르루주 바느질의 왕, 히스클리프 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10717].content
   limit: do 120 znaków
   EN: Haute Couture::Le Rouge King of Needleworks Heathcliff's Story
   PL: Haute Couture::Król Krawiectwa Le Rouge: historia Heathcliffa
337. [Teatr Opowieści [MirrorWorld_Story_Title_P10617] — tekst] 오트쿠튀르::르누아르 3F 방송실, 홍루 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10617].content
   limit: do 120 znaków
   EN: Haute Couture::Le Noir 3F Public Address Room Hong Lu's Story
   PL: Haute Couture::Radiowęzeł 3P Le Noir: historia Hong Lu
338. [Teatr Opowieści [MirrorWorld_Story_Title_P11116] — tekst] 쐐기 사무소 대표, 오티스 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11116].content
   limit: do 120 znaków
   EN: Wedge Office Rep: Outis's Story
   PL: Szefowa Biura Klina: historia Outis
339. [Teatr Opowieści [MirrorWorld_Story_Title_P10316] — tekst] 쐐기 사무소 해결사, 돈키호테 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10316].content
   limit: do 120 znaków
   EN: Wedge Office Fixer: Don Quixote's Story
   PL: Fikserka Biura Klina: historia Don Quixote
340. [Teatr Opowieści [MirrorWorld_Story_Title_P11017] — tekst] 쐐기 사무소 해결사, 싱클레어 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11017].content
   limit: do 120 znaków
   EN: Wedge Office Fixer: Sinclair's Story
   PL: Fikser Biura Klina: historia Sinclaira
341. [Teatr Opowieści [MirrorWorld_Story_Title_P10117] — tekst] 오트쿠튀르::르누아르 B3F 건조장, 이상 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P10117].content
   limit: do 120 znaków
   EN: Haute Couture::Le Noir B3F Drying Room: Yi Sang's Story
   PL: Haute Couture::Suszarnia B3F Le Noir: historia Yi Sanga
342. [Teatr Opowieści [MirrorWorld_Story_Title_P11217] — tekst] 오트쿠튀르::르루주 B2F 타래둥지, 그레고르 이야기
   źródło: StoryTheaterMirrorWorldStoryTitle.json :: dataList[id=MirrorWorld_Story_Title_P11217].content
   limit: do 120 znaków
   EN: Haute Couture::Le Rouge B2F Skein Nest: Gregor's Story
   PL: Haute Couture::Gniazdo Pasm B2F Le Rouge: historia Gregora

## Teatr Opowieści: StoryTheaterOther
- plik gry: `StoryTheaterOther.json`

343. [Teatr Opowieści [STORY_910309] — tytuł] 사장님의 순한맛 심도
   źródło: StoryTheaterOther.json :: dataList[id=STORY_910309].title
   limit: do 50 znaków
   EN: A Restaurateur’s Mild Fathoms
   PL: Łagodna Głębia Szefa Kuchni
344. [Teatr Opowieści [EventTitleText_9010] — tytuł] 단테의 노트
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9010].title
   limit: do 40 znaków
   EN: Dante’s Notes
   PL: Notatki Dantego
345. [Teatr Opowieści [STORY_901001] — tytuł] 단테의 기록
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901001].title
   limit: do 40 znaków
   EN: Dante’s Records
   PL: Zapiski Dantego
346. [Teatr Opowieści [STORY_901002] — tytuł] 버스의 뒷문
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901002].title
   limit: do 40 znaków
   EN: Bus’s Backdoor
   PL: Tylne Drzwi Autobusu
347. [Teatr Opowieści [STORY_901003] — tytuł] 버스 복도 너머
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901003].title
   limit: do 40 znaków
   EN: Beyond the Bus’s Corridor
   PL: Za Korytarzem Autobusu
348. [Teatr Opowieści [EventTitleText_9011] — tytuł] 뒷문의 방들에 대하여
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9011].title
   limit: do 40 znaków
   EN: Rooms Past the Backdoor
   PL: O Pokojach za Tylnymi Drzwiami
349. [Teatr Opowieści [STORY_901004] — tytuł] 뒷문의 방들에 대하여
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901004].title
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Teatr Opowieści [STORY_901005] — tytuł] 제1회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901005].title
   limit: do 40 znaków
   EN: The 1st Walpurgis Night
   PL: 1. Noc Walpurgii
351. [Teatr Opowieści [EventTitleText_9012] — tytuł] 유의미한 변화
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9012].title
   limit: do 40 znaków
   EN: A Notable Change
   PL: Znacząca Zmiana
352. [Teatr Opowieści [STORY_901201] — tytuł] 유의미한 변화
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901201].title
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Teatr Opowieści [EventTitleText_9013] — tytuł] 제2회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9013].title
   limit: do 40 znaków
   EN: The 2nd Walpurgis Night
   PL: 2. Noc Walpurgii
354. [Teatr Opowieści [STORY_901301] — tytuł] 녹빛 여명
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901301].title
   limit: do 40 znaków
   EN: The Dawn of Green
   PL: Zielony Świt
355. [Teatr Opowieści [STORY_901302] — tytuł] 시련
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901302].title
   limit: do 40 znaków
   EN: Ordeal
   PL: Próba
356. [Teatr Opowieści [EventTitleText_9014] — tytuł] 다시, 버스로.
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9014].title
   limit: do 40 znaków
   EN: Back to the Bus.
   PL: Z powrotem do autobusu.
357. [Teatr Opowieści [STORY_901401] — tytuł] 다시, 버스로.
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901401].title
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Teatr Opowieści [STORY_910712] — tytuł] 검귀의 심상
   źródło: StoryTheaterOther.json :: dataList[id=STORY_910712].title
   limit: do 40 znaków
   EN: A Blade Fiend's Fathoms
   PL: Głębia Demona Miecza
359. [Teatr Opowieści [STORY_911512] — tytuł] 검귀의 심상
   źródło: StoryTheaterOther.json :: dataList[id=STORY_911512].title
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Teatr Opowieści [EventTitleText_9015] — tytuł] 위험등급과 일련번호
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9015].title
   limit: do 50 znaków
   EN: Risk Levels & Classifications
   PL: Poziomy Ryzyka i Numery Seryjne
361. [Teatr Opowieści [STORY_901501] — tytuł] 위험등급과 일련번호
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901501].title
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Teatr Opowieści [EventTitleText_9016] — tytuł] 제3회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9016].title
   limit: do 40 znaków
   EN: The 3rd Walpurgis Night
   PL: 3. Noc Walpurgii
363. [Teatr Opowieści [STORY_901601] — tytuł] 다시 찾아온 밤
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901601].title
   limit: do 40 znaków
   EN: The Night Returns
   PL: Powrót Nocy
364. [Teatr Opowieści [STORY_901602] — tytuł] 요정의 축제
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901602].title
   limit: do 40 znaków
   EN: Fairy Festival
   PL: Święto Wróżek
365. [Teatr Opowieści [STORY_910915] — tytuł] 마지막 사건
   źródło: StoryTheaterOther.json :: dataList[id=STORY_910915].title
   limit: do 40 znaków
   EN: The Final Problem
   PL: Ostatnia Zagadka
366. [Teatr Opowieści [STORY_911815] — tytuł] 마지막 사건
   źródło: StoryTheaterOther.json :: dataList[id=STORY_911815].title
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Teatr Opowieści [EventTitleText_9017] — tytuł] 익숙한 알람
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9017].title
   limit: do 40 znaków
   EN: A Familiar Siren
   PL: Znajomy Alarm
368. [Teatr Opowieści [STORY_901701] — tytuł] 익숙한 알람
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901701].title
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Teatr Opowieści [EventTitleText_9018] — tytuł] 제4회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9018].title
   limit: do 40 znaków
   EN: The 4th Walpurgis Night
   PL: 4. Noc Walpurgii
370. [Teatr Opowieści [STORY_901801] — tytuł] 자색 시련
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901801].title
   limit: do 40 znaków
   EN: Ordeal of Violet
   PL: Fioletowa Próba
371. [Teatr Opowieści [STORY_901802] — tytuł] 사랑을 주소서
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901802].title
   limit: do 40 znaków
   EN: Grant Us Love
   PL: Obdarz Nas Miłością
372. [Teatr Opowieści [EventTitleText_9019] — tytuł] 제5회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9019].title
   limit: do 40 znaków
   EN: The 5th Walpurgis Night
   PL: 5. Noc Walpurgii
373. [Teatr Opowieści [STORY_901901] — tytuł] 톱니교단
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901901].title
   limit: do 40 znaków
   EN: The Church of Gears
   PL: Kościół Trybów
374. [Teatr Opowieści [STORY_901902] — tytuł] 밤의 시나리오
   źródło: StoryTheaterOther.json :: dataList[id=STORY_901902].title
   limit: do 40 znaków
   EN: The Night's Scenario
   PL: Scenariusz Nocy
375. [Teatr Opowieści [STORY_911414] — tytuł] 어느 연구원의 심상
   źródło: StoryTheaterOther.json :: dataList[id=STORY_911414].title
   limit: do 40 znaków
   EN: A Researcher's Fathoms
   PL: Głębia Pewnego Badacza
376. [Teatr Opowieści [EventTitleText_9020] — tytuł] 제6회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9020].title
   limit: do 40 znaków
   EN: The 6th Walpurgis Night
   PL: 6. Noc Walpurgii
377. [Teatr Opowieści [STORY_902001] — tytuł] 그래도 밤은 찾아온다
   źródło: StoryTheaterOther.json :: dataList[id=STORY_902001].title
   limit: do 40 znaków
   EN: The Night Comes Still
   PL: A Jednak Nadchodzi Noc
378. [Teatr Opowieści [STORY_902002] — tytuł] 절망의 기사
   źródło: StoryTheaterOther.json :: dataList[id=STORY_902002].title
   limit: do 40 znaków
   EN: The Knight of Despair
   PL: Rycerz Rozpaczy
379. [Teatr Opowieści [STORY_902003] — tytuł] 마법소녀
   źródło: StoryTheaterOther.json :: dataList[id=STORY_902003].title
   limit: do 40 znaków
   EN: Magical Girl
   PL: Czarodziejka
380. [Teatr Opowieści [STORY_912014] — tytuł] 메이어스의 심상
   źródło: StoryTheaterOther.json :: dataList[id=STORY_912014].title
   limit: do 40 znaków
   EN: Mayors's Fathoms
   PL: Głębia Mayors
381. [Teatr Opowieści [EventTitleText_9021] — tytuł] 제8회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9021].title
   limit: do 40 znaków
   EN: The 8th Walpurgis Night
   PL: 8. Noc Walpurgii
382. [Teatr Opowieści [EventTitleText_9022] — tytuł] 제10회 발푸르기스의 밤
   źródło: StoryTheaterOther.json :: dataList[id=EventTitleText_9022].title
   limit: do 40 znaków
   EN: The 10th Walpurgis Night
   PL: 10. Noc Walpurgii
383. [Teatr Opowieści [STORY_912301] — tytuł] 호박색 어스름
   źródło: StoryTheaterOther.json :: dataList[id=STORY_912301].title
   limit: do 40 znaków
   EN: The Dusk of Amber
   PL: Bursztynowy Zmierzch
384. [Teatr Opowieści [STORY_912302] — tytuł] 어느 음료의 생산방식
   źródło: StoryTheaterOther.json :: dataList[id=STORY_912302].title
   limit: do 40 znaków
   EN: How the Drink is Made
   PL: Sposób Produkcji Pewnego Napoju
385. [Teatr Opowieści [STORY_912711] — tytuł] ???의 심상
   źródło: StoryTheaterOther.json :: dataList[id=STORY_912711].title
   limit: do 40 znaków
   EN: ???'s Fathoms
   PL: Głębia ???
386. [Teatr Opowieści [STORY_912901] — tytuł] 역사의 층
   źródło: StoryTheaterOther.json :: dataList[id=STORY_912901].title
   limit: do 40 znaków
   EN: Floor of History
   PL: Piętro Historii
387. [Teatr Opowieści [STORY_912902] — tytuł] 밤의 귀납 추론
   źródło: StoryTheaterOther.json :: dataList[id=STORY_912902].title
   limit: do 50 znaków
   EN: Inductive Reasoning on the Night
   PL: Wnioskowanie Indukcyjne o Nocy

## Teatr Opowieści: StoryTheaterPersonality
- plik gry: `StoryTheaterPersonality.json`

388. [Teatr Opowieści [acheive] — tekst] 획득
   źródło: StoryTheaterPersonality.json :: dataList[id=acheive].content
   limit: do 120 znaków
   EN: Acquisition
   PL: Zdobycie
389. [Teatr Opowieści [dialog01] — tekst] 대화 1
   źródło: StoryTheaterPersonality.json :: dataList[id=dialog01].content
   limit: do 120 znaków
   EN: Chatter #1
   PL: Rozmowa #1
390. [Teatr Opowieści [dialog02] — tekst] 대화 2
   źródło: StoryTheaterPersonality.json :: dataList[id=dialog02].content
   limit: do 120 znaków
   EN: Chatter #2
   PL: Rozmowa #2
391. [Teatr Opowieści [dialog03] — tekst] 대화 3
   źródło: StoryTheaterPersonality.json :: dataList[id=dialog03].content
   limit: do 120 znaków
   EN: Chatter #3
   PL: Rozmowa #3
392. [Teatr Opowieści [sync_dialog01] — tekst] 동기화 후 대화 1
   źródło: StoryTheaterPersonality.json :: dataList[id=sync_dialog01].content
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL: Rozmowa po Synchronizacji #1
393. [Teatr Opowieści [sync_dialog02] — tekst] 동기화 후 대화 2
   źródło: StoryTheaterPersonality.json :: dataList[id=sync_dialog02].content
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL: Rozmowa po Synchronizacji #2
394. [Teatr Opowieści [morning_dialog] — tekst] 아침 로비 대화
   źródło: StoryTheaterPersonality.json :: dataList[id=morning_dialog].content
   limit: do 120 znaków
   EN: Morning Lobby Chat
   PL: Poranna rozmowa w lobby
395. [Teatr Opowieści [lunch_dialog] — tekst] 점심 로비 대화
   źródło: StoryTheaterPersonality.json :: dataList[id=lunch_dialog].content
   limit: do 120 znaków
   EN: Afternoon Lobby Chat
   PL: Popołudniowa rozmowa w lobby
396. [Teatr Opowieści [dinner_dialog] — tekst] 저녁 로비 대화
   źródło: StoryTheaterPersonality.json :: dataList[id=dinner_dialog].content
   limit: do 120 znaków
   EN: Evening Lobby Chat
   PL: Wieczorna rozmowa w lobby
397. [Teatr Opowieści [alone_dialog] — tekst] 방치
   źródło: StoryTheaterPersonality.json :: dataList[id=alone_dialog].content
   limit: do 120 znaków
   EN: Idle
   PL: Bezczynność
398. [Teatr Opowieści [synchronization] — tekst] 동기화 진행
   źródło: StoryTheaterPersonality.json :: dataList[id=synchronization].content
   limit: do 120 znaków
   EN: Uptying
   PL: Synchronizacja
399. [Teatr Opowieści [organization] — tekst] 인격 편성
   źródło: StoryTheaterPersonality.json :: dataList[id=organization].content
   limit: do 120 znaków
   EN: Deployment
   PL: Wystawienie do składu
400. [Teatr Opowieści [success] — tekst] 전투 승리
   źródło: StoryTheaterPersonality.json :: dataList[id=success].content
   limit: do 120 znaków
   EN: Victory Cry
   PL: Zwycięstwo w walce
401. [Teatr Opowieści [ex_success] — tekst] Exclear 전투 승리
   źródło: StoryTheaterPersonality.json :: dataList[id=ex_success].content
   limit: do 120 znaków
   EN: Extra Objectives Met
   PL: Zwycięstwo EX
402. [Teatr Opowieści [failure] — tekst] 전투 패배
   źródło: StoryTheaterPersonality.json :: dataList[id=failure].content
   limit: do 120 znaków
   EN: Defeat Wail
   PL: Porażka w walce
403. [Teatr Opowieści [P10102] — tekst] 남부 세븐 협회 6과, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10102].content
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Teatr Opowieści [P10103] — tekst] 검계 살수, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10103].content
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Teatr Opowieści [seven_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=seven_yisang_analysis].content
   limit: do 620 znaków
   EN: Formerly the youngest chief researcher at the [REDACTED] Wing, this Sinner possesses higher intelligence compared to most others. We estimate that everyday conversation with this Sinner will prove difficult for managers selected by our current screening process. Avoiding communication altogether will pose a risk on its own, however. If the Sinner remains silent for a long time, that means he is currently processing a line of deliberate thought; we recommend waiting patiently for him.
   PL: Dawniej najmłodszy główny badacz w Skrzydle [UTAJNIONO]; odznacza się inteligencją przewyższającą większość pozostałych Grzeszników. Szacujemy, że codzienna rozmowa z tym Grzesznikiem może okazać się trudna dla Kierownika wyłonionego w naszym obecnym procesie rekrutacji. Całkowite unikanie kontaktu niesie jednak własne zagrożenia. Jeśli Grzesznik milczy przez dłuższy czas, oznacza to, że przetwarza w głowie ciąg przemyśleń — zalecamy cierpliwie zaczekać.
406. [Teatr Opowieści [blade_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Teatr Opowieści [P10202] — tekst] W사 2등급 정리 요원, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10202].content
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Teatr Opowieści [P10203] — tekst] 살아남은 로보토미 직원, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10203].content
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Teatr Opowieści [wcorp_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=wcorp_faust_analysis].content
   limit: do 790 znaków
   EN: The Sinner who developed the engine of Mephistopheles, the bus operated by Limbus Company. She claims that there is no one in the City who could rival her library of knowledge and wisdom, and she isn't necessarily wrong. You might find her high and mighty attitude when she allows you to converse with her displeasing, but as seen with how she treats everyone with subtle gestures of arrogance, there is no hope of her parting with it, ever. We recommend simply nodding once and getting over it. Even though she has an unparalleled genius, we can't quite figure out how to use this one. Perhaps you could be the one to find out?
   PL: Grzeszniczka, która skonstruowała silnik Mefistofelesa — autobusu Limbus Company. Sama utrzymuje, że w całym Mieście nie ma nikogo dorównującego jej wiedzą i mądrością, i nie sposób odmówić jej racji. Jej wyniosła postawa podczas rozmów z Kierownikiem może budzić irytację, lecz wobec faktu, iż traktuje z subtelną wyższością absolutnie każdego, nie ma najmniejszych szans na zmianę. Zalecamy po prostu przytaknąć i puścić to mimo uszu. Choć jej geniusz nie ma sobie równych, sami nie wiemy jeszcze, jak z niego właściwie korzystać. Być może odkryje to właśnie Kierownik?
410. [Teatr Opowieści [lcorp_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=lcorp_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Teatr Opowieści [P10302] — tekst] W사 3등급 정리 요원, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10302].content
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Teatr Opowieści [P10303] — tekst] 남부 시 협회 5과 부장, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10303].content
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Teatr Opowieści [wcorp_donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=wcorp_donquixote_analysis].content
   limit: do 690 znaków
   EN: There is no Sinner that can outmatch this one's level of passion if we were to measure it. An avid aficionada of all things Fixer, she adorns herself with a variety of Fixer-related merchandise. They won't affect her performance in combat one way or another, so there is no need for you to restrict her from keeping her decorations. She is deeply immersed in the role of a righteous Fixer (Has such a thing ever existed, really?), hence the exaggerated mannerisms akin to those of an actor. It's advised to play along with her for a smooth mission.
   PL: Gdyby mierzyć wartość Grzeszników samym zapałem, ta Grzeszniczka otrzymałaby najwyższą notę. Jako zapalona kolekcjonerka i wielbicielka wszystkiego, co związane z Fikserami, obwiesza się od stóp do głów pamiątkami z nimi związanymi. Nie wpływa to na jej skuteczność bojową, nie ma więc potrzeby nakładania na nią zakazów. Sama głęboko wczuwa się w rolę „sprawiedliwego Fiksera” (czy ktoś taki w ogóle kiedykolwiek istniał?), przez co zachowuje się przesadnie niczym trzeciorzędna aktorka. Dla sprawnego przebiegu misji najlepiej wtórować jej w tej grze.
414. [Teatr Opowieści [shi_donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=shi_donquixote_analysis].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Teatr Opowieści [P10402] — tekst] 남부 세븐 협회 6과, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10402].content
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Teatr Opowieści [P10403] — tekst] 흑운회 와카슈, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10403].content
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Teatr Opowieści [seven_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=seven_ryoshu_analysis].content
   limit: do 760 znaków
   EN: As they say, every person has their own creed—and it’s only right to respect it as the Executive Manager. But with some creeds, you will have difficulty in even simply pretending to sympathize. You will have noticed that the sinner in question is a silent chain-smoker whose eyes shine with a euphoric gleam only during battle. She believes that senselessly destroying the enemy's heads is an uncultured act and a step backward for art. CAUTION: This sinner's background is one that even our company may have trouble handling; it is advised against making her breed personal resentment towards you.
   PL: Każdy Grzesznik ma własne credo i obowiązkiem Kierownika Wykonawczego jest je szanować — lecz w niektórych przypadkach trudno będzie nawet udawać zrozumienie. Z pewnością zauważyłeś już, że ta Grzeszniczka na co dzień milczy, paląc papierosa za papierosem, a jej oczy rozbłyskują euforią wyłącznie w trakcie walki. Uważa, że bezmyślne roztrzaskiwanie głów wrogów to prostacki akt cofający sztukę w rozwoju. [OSTRZEŻENIE] — za tą Grzeszniczką stoją wpływy, z którymi nawet nasza firma miałaby problem; stanowczo odradzamy ściąganie na siebie jej osobistej urazy.
418. [Teatr Opowieści [kurokumo_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=kurokumo_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Teatr Opowieści [P10502] — tekst] 남부 리우 협회 6과, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10502].content
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Teatr Opowieści [P10503] — tekst] W사 2등급 정리 요원, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10503].content
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Teatr Opowieści [liu_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_meursault_analysis].content
   limit: do 120 znaków
   EN: Wants clear and concise commands, requiring no judgement on his part.
   PL: Wymaga jasnych i krótkich rozkazów — niewymagających żadnego własnego osądu.
422. [Teatr Opowieści [wcorp_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=wcorp_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Teatr Opowieści [P10602] — tekst] 흑운회 와카슈, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10602].content
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Teatr Opowieści [P10603] — tekst] 콩콩이파 보스, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10603].content
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Teatr Opowieści [kurokumo_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=kurokumo_honglu_analysis].content
   limit: do 670 znaków
   EN: A Sinner who had lived an affluent life before becoming our company's asset. As such, he has a certain admiration for a free life; but occasionally, he may make ignorant and unsavory questions in regards to the food cooked by a certain other Sinner or other aspects of the low-lives' lowly culture. This can cause significant irritation for the other sinners. However, it is important to note that no sarcastic undertones are contained in his curiosity-driven inquiries, so it is ill-advised to let them get physical over it.
   PL: Grzesznik, który przed staniem się zasobem naszej firmy żył w pełnym dostatku. Pragnie wolności, lecz niekiedy na widok potraw przyrządzonych przez innych Grzeszników zdradza zupełną nieznajomość kultury niższych warstw i zadaje uwłaczające pytania, doprowadzając towarzyszy do białej gorączki. Nie wynika to jednak ze złośliwości, a ze zwykłej ciekawości — nie dopuszczaj więc, by sięgano z tego powodu po ostrza.
426. [Teatr Opowieści [cong_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=cong_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Teatr Opowieści [P10702] — tekst] 남부 시 협회 5과, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10702].content
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Teatr Opowieści [P10703] — tekst] R사 제 4무리 토끼팀, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10703].content
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Teatr Opowieści [shi_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=shi_heathcliff_analysis].content
   limit: do 750 znaków
   EN: This Sinner prefers to take action rather than wait for logic to dictate his course. His thoughts and feelings are blatantly visible in his demeanor, and he has no intention of hiding them; his brashness may cause headaches (or physical injury leading to a headache) in the process of forming a relationship. Please do note that this is not an indication of serious damage to the Sinner's thought process. If his fit of rage persists, please contact the human resources department. Once you realize that he is the type that tends to be simple-minded, you'll have an easier time handling him.
   PL: Grzesznik przedkładający natychmiastowy czyn nad logiczny namysł. Jego myśli i emocje malują się wprost na twarzy i w słowach, których nawet nie próbuje kryć — toteż budowanie z nim relacji może przyprawić Kierownika o ból głowy (bądź uraz fizyczny skutkujący bólem głowy). Pragniemy zaznaczyć, że nie świadczy to o trwałym uszkodzeniu jego procesów myślowych. Jeśli napad furii nie ustępuje przez dłuższy czas, prosimy o kontakt z działem kadr. Gdy jednak pojmiesz, że to typ prostolinijny i nieskomplikowany, łatwo będzie nad nim zapanować.
430. [Teatr Opowieści [rcorp_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=rcorp_heathcliff_analysis].content
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Teatr Opowieści [P10802] — tekst] R사 제 4무리 순록팀, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10802].content
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Teatr Opowieści [P10803] — tekst] 남부 시 협회 5과, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10803].content
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Teatr Opowieści [P10804] — tekst] LCCB 대리, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10804].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Teatr Opowieści [rcorp_ishmael_analysis] — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=rcorp_ishmael_analysis].content
   limit: do 680 znaków
   EN: You may be disheartened by the defective state of many of your Sinners, but do not worry; this Sinner is one of the few who can carry out most missions without much complaint. She is likely to make reasonable judgements, so it is a good idea to start conversations while looking her way if you're seeking sound advice. However, you mustn't forget: this Sinner has survived an absurd voyage in a far and wide body of water. Her patience may run deep, but once you take a wrong turn with her, it will be a difficult task to regain her trust.
   PL: Możesz czuć przygnębienie na widok licznych ułomności swoich Grzeszników, lecz bez obaw — ta Grzeszniczka należy do nielicznych, którzy wykonują zadania bez zbędnego narzekania. Potrafi podejmować rozsądne decyzje, więc szukając trzeźwej rady, warto zagaić rozmowę, spoglądając w jej stronę. Pamiętaj jednak: przetrwała absurdalny rejs po dalekim, bezmiernym akwenie. Jej cierpliwość jest głęboka, lecz jeśli raz zawiedziesz jej zaufanie, niezwykle trudno będzie je odzyskać.
435. [Teatr Opowieści [shi_ishmael_analysis] — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=shi_ishmael_analysis].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Teatr Opowieści [P10902] — tekst] 흑운회 와카슈, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10902].content
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Teatr Opowieści [P10903] — tekst] LCCB 대리, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10903].content
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Teatr Opowieści [kurokumo_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=kurokumo_rodion_analysis].content
   limit: do 600 znaków
   EN: The unfortunate traits of being Backstreets-born are apparent in this Sinner. She loves money, gambling, and betting—so it is advised to pay close attention to her as the manager. She tends to deflect orders with an unimpressive wink or a silly joke; we recommend taking a stern stance at times to remind her that you are her superior. Her mood may be down at irregular intervals. There is nothing you can do to aid her in that state, so we recommend waiting for it to pass.
   PL: Grzeszniczka, w której aż nazbyt wyraźnie widać nieszczęsne piętno wychowania w Zaułkach. Kocha pieniądze, hazard i zakłady, dlatego wymaga bacznego nadzoru Kierownika. Ma w zwyczaju zbywać polecenia nieudolnym mrugnięciem oka lub głupkowatym żartem — zalecamy niekiedy przyjąć surową postawę, by przypomnieć jej o hierarchii. Nieregularnie popada w przygnębienie; Kierownik nie jest w stanie nic na to poradzić, najwydajniej więc po prostu przeczekać ten stan w ciszy.
439. [Teatr Opowieści [lcb_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=lcb_rodion_analysis].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Teatr Opowieści [P11002] — tekst] 검계 살수, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11002].content
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Teatr Opowieści [P11003] — tekst] 남부 츠바이 협회 6과, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11003].content
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Teatr Opowieści [P11004] — tekst] 마리아치 보스, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11004].content
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Teatr Opowieści [blade_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_sinclair_analysis].content
   limit: do 830 znaków
   EN: Even with the volatile nature of human growth around his age taken into consideration, this Sinner seems to get particularly startled or frown when spoken to. He isn't used to real combat at the moment, meaning that he may struggle to keep himself together at the sight of something as mild as spilt innards at first. As there may be those with violent tendencies among your crew, we recommend taking an approach focused on positive reinforcement with this sinner. He appears to possess a murderous gaze that he himself isn't aware of; this is a hopeful sign that he has the potential to grow into an expert of our company's profession with the right stimuli.
   PL: Nawet biorąc pod uwagę chwiejność właściwą jego wiekowi, ten Grzesznik wyjątkowo łatwo wzdryga się lub krzywi, gdy ktoś się do niego odezwie. Nie nawykł jeszcze do prawdziwej walki, więc początkowo sam widok wnętrzności będzie dla niego ciężką próbą. Ponieważ wśród załogi nie brakuje jednostek skłonnych do przemocy, wobec tego Grzesznika zalecamy metodę marchewki zamiast kija. W jego spojrzeniu czai się nieuświadomiona przezeń żądza krwi — to obiecujący znak, że przy odpowiednich bodźcach wyrośnie na znakomitego specjalistę w branży naszej firmy.
444. [Teatr Opowieści [zwei_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Teatr Opowieści [mariachi_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=mariachi_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Teatr Opowieści [P11102] — tekst] 검계 살수, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11102].content
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Teatr Opowieści [P11103] — tekst] G사 부장, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11103].content
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Teatr Opowieści [blade_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_outis_analysis].content
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Sinner could serve as an excellent advisor depending on your capability. However, she also has a meddlesome tendency, so it is recommended to keep her satisfied with short replies of agreement. She is an expert when it comes to tactics and various pearls of wisdom about life, making her advice all the more valuable for your mission. In addition, she possesses a vast knowledge of workshop technologies; you could trust her with simple repairs of the bus. \nNOTICE: Unlike the other Sinners, accessing records pertaining to the past of this Sinner is not permitted.\nWARNING: Keep an eye on this Sinner and beware that she does not exercise her cunning intellect for purposes other than completing our company's mission.
   PL: Zależnie od kompetencji Kierownika Grzeszniczka ta może stać się znakomitą doradczynią. Ma jednak skłonność do nadmiernego wtrącania się, toteż zalecamy kwitować jej uwagi krótkim przytaknięciem. Jest biegła w taktyce i posiada bogate doświadczenie, warto więc korzystać z jej rad; zna się również świetnie na technologii warsztatowej, dzięki czemu można powierzyć jej drobne naprawy autobusu.\n[UWAGA] — W przeciwieństwie do pozostałych Grzeszników wgląd w akta dotyczące jej przeszłości jest zabroniony.\n[OSTRZEŻENIE] — Dopilnuj, by jej przebiegły umysł nie pracował nad niczym wykraczającym poza misję firmy.
449. [Teatr Opowieści [gcorp_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=gcorp_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Teatr Opowieści [P11202] — tekst] 남부 리우 협회 6과, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11202].content
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Teatr Opowieści [P11203] — tekst] G사 일등대리, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11203].content
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Teatr Opowieści [liu_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_gregor_analysis].content
   limit: do 770 znaków
   EN: This Sinner is relatively easy to handle in terms of personality. However, an upsurge of emotion or a sudden change of environment may cause parts or the whole of his body to transform into insectile (notably akin to a carapace, resembling that of the _________) tissues. If you do not wish to be a rude manager (not that you're obligated to be nice), we recommend keeping your facial expression in check so that your disgust is not visible to him. He sometimes uses cynical language, but he can still be reasoned with, and you can get around him without much difficulty as long as you learn the knack of it.
   PL: Pod względem charakteru z tym Grzesznikiem obcuje się stosunkowo łatwo. Jednak nagły przypływ emocji lub gwałtowna zmiana otoczenia sprawiają, że część — a niekiedy całość — jego ciała przeobraża się w tkankę owadzią (przypominającą pancerz chitynowy zbliżony do ■■■■). Jeśli nie chcesz uchodzić za nieuprzejmego Kierownika (choć nie masz takiego obowiązku), zalecamy starannie panować nad mimiką i nie okazywać obrzydzenia. Posługuje się czasem cynicznym tonem, lecz przy odrobinie wyczucia bez trudu można się z nim porozumieć.
453. [Teatr Opowieści [gcorp_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=gcorp_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Teatr Opowieści [P10504] — tekst] N사 큰 망치, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10504].content
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Teatr Opowieści [ncorp_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=ncorp_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Teatr Opowieści [P10904] — tekst] N사 중간 망치, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10904].content
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Teatr Opowieści [ncorp_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=ncorp_rodion_analysis].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Teatr Opowieści [P10704] — tekst] N사 작은 망치, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10704].content
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Teatr Opowieści [ncorp_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=ncorp_heathcliff_analysis].content
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Teatr Opowieści [P10204] — tekst] 쥐는 자, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10204].content
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Teatr Opowieści [ncorp_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=ncorp_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Teatr Opowieści [P11104] — tekst] 남부 세븐 협회 6과 부장, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11104].content
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Teatr Opowieści [SevenAsso6_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=SevenAsso6_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Teatr Opowieści [P10604] — tekst] 남부 리우 협회 5과, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10604].content
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Teatr Opowieści [LiuAsso5_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=LiuAsso5_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Teatr Opowieści [P10404] — tekst] 료. 고. 파. 주방장, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10404].content
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Teatr Opowieści [23GuCooker_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=23GuCooker_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Teatr Opowieści [P11204] — tekst] 료. 고. 파. 조수, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11204].content
   (powtórzenie elementu 191 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Teatr Opowieści [23GuCooker_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=23GuCooker_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Teatr Opowieści [P11005] — tekst] 쥐어들 자, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11005].content
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Teatr Opowieści [ncorp_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=ncorp_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Teatr Opowieści [P10304] — tekst] N사 중간 망치, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10304].content
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Teatr Opowieści [ncorp_donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=ncorp_donquixote_analysis].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Teatr Opowieści [P10905] — tekst] 장미스패너 공방 대표, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10905].content
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Teatr Opowieści [kcorp_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=kcorp_rodion_analysis].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Teatr Opowieści [P10505] — tekst] 장미스패너 공방 해결사, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10505].content
   (powtórzenie elementu 195 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Teatr Opowieści [kcorp_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=kcorp_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Teatr Opowieści [P10705] — tekst] 로보토미 E.G.O 여우비, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10705].content
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Teatr Opowieści [lego_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_heathcliff_analysis].content
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Teatr Opowieści [P11205] — tekst] 장미스패너 공방 해결사, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11205].content
   (powtórzenie elementu 197 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Teatr Opowieści [kcorp_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=kcorp_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Teatr Opowieści [P10104] — tekst] 개화 E.G.O 동백, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10104].content
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Teatr Opowieści [lego_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Teatr Opowieści [P10805] — tekst] 로보토미 E.G.O 출렁임, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10805].content
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Teatr Opowieści [lego_ishmael_analysis] — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_ishmael_analysis].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Teatr Opowieści [P10605] — tekst] K사 3등급 적출직 직원, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10605].content
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Teatr Opowieści [kcorp_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=kcorp_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Teatr Opowieści [P11006] — tekst] 로보토미 E.G.O 홍적, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11006].content
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Teatr Opowieści [lego_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Teatr Opowieści [P10806] — tekst] 남부 리우 협회 4과, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10806].content
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Teatr Opowieści [liu_ishmael_analysis] — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_ishmael_analysis].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Teatr Opowieści [P10506] — tekst] R사 제 4무리 코뿔소팀, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10506].content
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Teatr Opowieści [rcorp_meursault_profile] — tekst] 뫼르소\n남\n9월 23일\nA\n188CM\n82KG
   źródło: StoryTheaterPersonality.json :: dataList[id=rcorp_meursault_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Meursault\nM\nSeptember 23rd\nA\n188CM (6'2")\n82KG (180lbs)
   PL: Meursault\nM\n23 września\nA\n188 CM\n82 KG
494. [Teatr Opowieści [rcorp_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=rcorp_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Teatr Opowieści [P10906] — tekst] 남부 츠바이 협회 5과, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10906].content
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Teatr Opowieści [zwei_rodion_profile] — tekst] 로쟈\n여\n9월 23일\nA\n182CM\n65KG
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_rodion_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rodion\nF\nSeptember 23rd\nA\n182CM (5'11")\n65KG (143.3lbs)
   PL: Rodion\nK\n23 września\nA\n182 CM\n65 KG
497. [Teatr Opowieści [zwei_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_rodion_analysis].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Teatr Opowieści [P10305] — tekst] 남부 섕크 협회 5과 부장, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10305].content
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Teatr Opowieści [cinq_donquixote_profile] — tekst] 돈키호테\n여\n9월 23일\nA\n163CM\n52KG
   źródło: StoryTheaterPersonality.json :: dataList[id=cinq_donquixote_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don Quixote\nF\nSeptember 23rd\nA\n163CM (5'3")\n52KG (114.64lbs)
   PL: Don Quixote\nK\n23 września\nA\n163 CM\n52 KG
500. [Teatr Opowieści [cinq_donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=cinq_donquixote_analysis].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Teatr Opowieści [P10807] — tekst] 어금니 보트 센터 해결사, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10807].content
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Teatr Opowieści [ucorp_ishmael_profile] — tekst] 이스마엘\n여\n9월 23일\nA\n171CM\n57KG
   źródło: StoryTheaterPersonality.json :: dataList[id=ucorp_ishmael_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ishmael\nF\nSeptember 23rd\nA\n171CM (5'7")\n57KG (125.66lbs)
   PL: Ishmael\nK\n23 września\nA\n171 CM\n57 KG
503. [Teatr Opowieści [ucorp_ishmael_analysis] — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=ucorp_ishmael_analysis].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Teatr Opowieści [P11007] — tekst] 어금니 보트 센터 해결사, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11007].content
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Teatr Opowieści [ucorp_sinclair_profile] — tekst] 싱클레어\n남\n9월 23일\nA\n163CM\n54KG
   źródło: StoryTheaterPersonality.json :: dataList[id=ucorp_sinclair_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sinclair\nM\nSeptember 23rd\nA\n163CM (5'4")\n54KG (119.05lbs)
   PL: Sinclair\nM\n23 września\nA\n163 CM\n54 KG
506. [Teatr Opowieści [ucorp_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=ucorp_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Teatr Opowieści [P11206] — tekst] 남부 츠바이 협회 4과, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11206].content
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Teatr Opowieści [zwei_gregor_profile] — tekst] 그레고르\n남\n9월 23일\nA\n167CM\n68KG
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_gregor_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gregor\nM\nSeptember 23rd\nA\n167CM (5'6")\n68KG (149.914lbs)
   PL: Gregor\nM\n23 września\nA\n167 CM\n68 KG
509. [Teatr Opowieści [zwei_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Teatr Opowieści [P10205] — tekst] 남부 츠바이 협회 4과, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10205].content
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Teatr Opowieści [zwei_faust_profile] — tekst] 파우스트\n여\n9월 23일\nA\n174CM\n59KG
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_faust_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Faust\nF\nSeptember 23rd\nA\n174CM (5'9")\n57KG (130.07lbs)
   PL: Faust\nK\n23 września\nA\n174 CM\n59 KG
512. [Teatr Opowieści [zwei_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=zwei_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Teatr Opowieści [P10405] — tekst] W사 3등급 정리 요원, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10405].content
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Teatr Opowieści [Wcorp_ryoshu_profile] — tekst] 료슈\n여\n9월 23일\nA\n171CM\n58KG
   źródło: StoryTheaterPersonality.json :: dataList[id=Wcorp_ryoshu_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ryōshū\nF\nSeptember 23rd\nA\n171CM (5'7")\n58KG (127.87lbs)
   PL: Ryōshū\nK\n23 września\nA\n171 CM\n58 KG
515. [Teatr Opowieści [Wcorp_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=Wcorp_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Teatr Opowieści [P10606] — tekst] W사 2등급 정리 요원, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10606].content
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Teatr Opowieści [Wcorp_honglu_profile] — tekst] 홍루\n남\n9월 23일\nA\n178CM\n74KG
   źródło: StoryTheaterPersonality.json :: dataList[id=Wcorp_honglu_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hong Lu\nM\nSeptember 23rd\nA\n178CM (5'10")\n74KG (163.14lbs)
   PL: Hong Lu\nM\n23 września\nA\n178 CM\n74 KG
518. [Teatr Opowieści [Wcorp_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=Wcorp_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Teatr Opowieści [P10206] — tekst] 남부 세븐 협회 4과, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10206].content
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Teatr Opowieści [seven_faust_profile] — tekst] 파우스트\n여\n9월 23일\nA\n174CM\n59KG
   źródło: StoryTheaterPersonality.json :: dataList[id=seven_faust_profile].content
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Teatr Opowieści [seven_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=seven_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Teatr Opowieści [P10706] — tekst] 남부 세븐 협회 4과, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10706].content
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Teatr Opowieści [seven_heathcliff_profile] — tekst] 히스클리프\n남\n9월 23일\nA\n180CM\n78KG
   źródło: StoryTheaterPersonality.json :: dataList[id=seven_heathcliff_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heathcliff\nM\nSeptember 23rd\nA\n180CM (5'11")\n54KG (171.96lbs)
   PL: Heathcliff\nM\n23 września\nA\n180 CM\n78 KG
524. [Teatr Opowieści [seven_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=seven_heathcliff_analysis].content
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Teatr Opowieści [P10105] — tekst] 어금니 사무소 해결사, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10105].content
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Teatr Opowieści [molar_yisang_profile] — tekst] 이상\n남\n9월 23일\nA\n176CM\n70KG
   źródło: StoryTheaterPersonality.json :: dataList[id=molar_yisang_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Yi Sang\nM\nSep. 23\nA\n176cm (5'9")\n70kg (154.3lbs)
   PL: Yi Sang\nM\n23 września\nA\n176 CM\n70 KG
527. [Teatr Opowieści [molar_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=molar_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Teatr Opowieści [P11105] — tekst] 어금니 사무소 해결사, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11105].content
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Teatr Opowieści [molar_outis_profile] — tekst] 오티스\n여\n9월 23일\nA\n177CM\n64KG
   źródło: StoryTheaterPersonality.json :: dataList[id=molar_outis_profile].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Outis\nF\nSeptember 23rd\nA\n177CM (5'9")\n64KG (141.1lbs)
   PL: Outis\nK\n23 września\nA\n177 CM\n64 KG
530. [Teatr Opowieści [molar_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=molar_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Teatr Opowieści [P10907] — tekst] 남부 디에치 협회 4과, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10907].content
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Teatr Opowieści [dieci_rodion_profile] — tekst] 로쟈\n여\n9월 23일\nA\n182CM\n65KG
   źródło: StoryTheaterPersonality.json :: dataList[id=dieci_rodion_profile].content
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Teatr Opowieści [dieci_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=dieci_rodion_analysis].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Teatr Opowieści [P10207] — tekst] 로보토미 E.G.O 후회, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10207].content
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Teatr Opowieści [lego_faust_profile] — tekst] 파우스트\n여\n9월 23일\nA\n174CM\n59KG
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_faust_profile].content
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Teatr Opowieści [lego_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Teatr Opowieści [P10607] — tekst] 갈고리 사무소 해결사, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10607].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Teatr Opowieści [hook_honglu_profile] — tekst] 홍루\n남\n9월 23일\nA\n178CM\n74KG
   źródło: StoryTheaterPersonality.json :: dataList[id=hook_honglu_profile].content
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Teatr Opowieści [hook_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=hook_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Teatr Opowieści [P10106] — tekst] W사 3등급 정리 요원, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10106].content
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Teatr Opowieści [wcorp_yisang_profile] — tekst] 이상\n남\n9월 23일\nA\n176CM\n70KG
   źródło: StoryTheaterPersonality.json :: dataList[id=wcorp_yisang_profile].content
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Teatr Opowieści [wcorp_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=wcorp_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Teatr Opowieści [P11207] — tekst] 쌍갈고리 해적단 부선장, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11207].content
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Teatr Opowieści [hook_gregor_profile] — tekst] 그레고르\n남\n9월 23일\nA\n167CM\n68KG
   źródło: StoryTheaterPersonality.json :: dataList[id=hook_gregor_profile].content
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Teatr Opowieści [hook_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=hook_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Teatr Opowieści [P10406] — tekst] LCCB 대리, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10406].content
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Teatr Opowieści [lccb_ryoshu_profile] — tekst] 료슈\n여\n9월 23일\nA\n171CM\n58KG
   źródło: StoryTheaterPersonality.json :: dataList[id=lccb_ryoshu_profile].content
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Teatr Opowieści [lccb_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=lccb_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Teatr Opowieści [P10306] — tekst] 중지 작은 아우, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10306].content
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Teatr Opowieści [middlefinger_donquixote_profile] — tekst] 돈키호테\n여\n9월 23일\nA\n163CM\n52KG
   źródło: StoryTheaterPersonality.json :: dataList[id=middlefinger_donquixote_profile].content
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Teatr Opowieści [middlefinger_donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=middlefinger_donquixote_analysis].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Teatr Opowieści [P10507] — tekst] 중지 작은 아우, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10507].content
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Teatr Opowieści [middlefinger_meursault_profile] — tekst] 뫼르소\n남\n9월 23일\nA\n188CM\n82KG
   źródło: StoryTheaterPersonality.json :: dataList[id=middlefinger_meursault_profile].content
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Teatr Opowieści [middlefinger_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=middlefinger_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Teatr Opowieści [P10707] — tekst] 피쿼드호 작살잡이, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10707].content
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Teatr Opowieści [qui_heathcliff_profile] — tekst] 히스클리프\n남\n9월 23일\nA\n180CM\n78KG
   źródło: StoryTheaterPersonality.json :: dataList[id=qui_heathcliff_profile].content
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Teatr Opowieści [qui_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=qui_heathcliff_analysis].content
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Teatr Opowieści [P10107] — tekst] 피쿼드호 일등 항해사, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10107].content
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Teatr Opowieści [starb_yisang_profile] — tekst] 이상\n남\n9월 23일\nA\n176CM\n70KG
   źródło: StoryTheaterPersonality.json :: dataList[id=starb_yisang_profile].content
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Teatr Opowieści [starb_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=starb_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Teatr Opowieści [P11008] — tekst] 남부 섕크 협회 4과 부장, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11008].content
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Teatr Opowieści [cinq_sinclair_profile] — tekst] 싱클레어\n남\n9월 23일\nA\n163CM\n54KG
   źródło: StoryTheaterPersonality.json :: dataList[id=cinq_sinclair_profile].content
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Teatr Opowieści [cinq_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=cinq_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Teatr Opowieści [P11106] — tekst] 남부 섕크 협회 4과, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11106].content
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Teatr Opowieści [cinq_outis_profile] — tekst] 오티스\n여\n9월 23일\nA\n177CM\n64KG
   źródło: StoryTheaterPersonality.json :: dataList[id=cinq_outis_profile].content
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Teatr Opowieści [cinq_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=cinq_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Teatr Opowieści [P11107] — tekst] 로보토미 E.G.O 마탄, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11107].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Teatr Opowieści [lego_outis_profile] — tekst] 오티스\n여\n9월 23일\nA\n177CM\n64KG
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_outis_profile].content
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Teatr Opowieści [lego_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Teatr Opowieści [P10307] — tekst] 로보토미 E.G.O 초롱, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10307].content
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Teatr Opowieści [lego_donquixote_profile] — tekst] 돈키호테\n여\n9월 23일\nA\n163CM\n52KG
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_donquixote_profile].content
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Teatr Opowieści [lego_donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=lego_donquixote_analysis].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Teatr Opowieści [P10608] — tekst] 남부 디에치 협회 4과, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10608].content
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Teatr Opowieści [dieci_honglu_profile] — tekst] 홍루\n남\n9월 23일\nA\n178CM\n74KG
   źródło: StoryTheaterPersonality.json :: dataList[id=dieci_honglu_profile].content
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Teatr Opowieści [dieci_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=dieci_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Teatr Opowieści [P10108] — tekst] 남부 디에치 협회 4과, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10108].content
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Teatr Opowieści [dieci_yisang_profile] — tekst] 이상\n남\n9월 23일\nA\n176CM\n70KG
   źródło: StoryTheaterPersonality.json :: dataList[id=dieci_yisang_profile].content
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Teatr Opowieści [dieci_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=dieci_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Teatr Opowieści [P10808] — tekst] 피쿼드호 선장, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10808].content
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Teatr Opowieści [ahab_ishmael_profile] — tekst] 이스마엘\n여\n9월 23일\nA\n171CM\n57KG
   źródło: StoryTheaterPersonality.json :: dataList[id=ahab_ishmael_profile].content
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Teatr Opowieści [P10508] — tekst] 검계 우두머리, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10508].content
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Teatr Opowieści [blade_meursault_profile] — tekst] 뫼르소\n남\n9월 23일\nA\n188CM\n82KG
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_meursault_profile].content
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Teatr Opowieści [blade_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Teatr Opowieści [P10208] — tekst] 검계 살수, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10208].content
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Teatr Opowieści [blade_faust_profile] — tekst] 파우스트\n여\n9월 23일\nA\n174CM\n59KG
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_faust_profile].content
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Teatr Opowieści [blade_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Teatr Opowieści [P11208] — tekst] 흑운회 부조장, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11208].content
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Teatr Opowieści [kurokumo_gregor_profile] — tekst] 그레고르\n남\n9월 23일\nA\n167CM\n68KG
   źródło: StoryTheaterPersonality.json :: dataList[id=kurokumo_gregor_profile].content
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Teatr Opowieści [kurokumo_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=kurokumo_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Teatr Opowieści [P10308] — tekst] 검계 살수, 돈키호테 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10308].content
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Teatr Opowieści [blade_donquixote_profile] — tekst] 돈키호테\n여\n9월 23일\nA\n163CM\n52KG
   źródło: StoryTheaterPersonality.json :: dataList[id=blade_donquixote_profile].content
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Teatr Opowieści [blade__donquixote_analysis] — tekst] 열정으로만 수감자들의 질을 다시 측량한다면 최고의 점수를 받을 수감자일 것입니다. 해결사라는 것들에 관해서는 대단한 수집가이자 열성적인 팬이므로 온몸에 주렁주렁 해결사 기념품을 지니곤 합니다. 전투에 딱히 영향을 주진 않을 테니 굳이 제재를 가하실 필요는 없습니다. 본인 또한 정의의 해결사라는(그런 게 존재했던 적이나 있었을까요?) 역할에 잔뜩 심취해 있으므로 삼류 배우와도 같은 과장된 행동거지를 합니다. 원활한 임무를 위해선 장단에 같이 맞춰주는 편이 좋습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=blade__donquixote_analysis].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Teatr Opowieści [P10908] — tekst] 남부 리우 협회 4과 부장, 로쟈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10908].content
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Teatr Opowieści [liu_rodion_profile] — tekst] 로쟈\n여\n9월 23일\nA\n182CM\n65KG
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_rodion_profile].content
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Teatr Opowieści [liu_rodion_analysis] — tekst] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다. 돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다. 지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는 경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다. 가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서 해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_rodion_analysis].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Teatr Opowieści [P10407] — tekst] 남부 리우 협회 4과, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10407].content
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Teatr Opowieści [liu_ryoshu_profile] — tekst] 료슈\n여\n9월 23일\nA\n171CM\n58KG
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_ryoshu_profile].content
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Teatr Opowieści [liu_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=liu_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Teatr Opowieści [P10708] — tekst] 남부 외우피 협회 3과, 히스클리프 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10708].content
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Teatr Opowieści [oufi_heathcliff_profile] — tekst] 히스클리프\n남\n9월 23일\nA\n180CM\n78KG
   źródło: StoryTheaterPersonality.json :: dataList[id=oufi_heathcliff_profile].content
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Teatr Opowieści [oufi_heathcliff_analysis] — tekst] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다. 생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로 관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...) 유발할 수도 있습니다. 수감자의 사고 체계에 심각한 문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안 분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록 생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: StoryTheaterPersonality.json :: dataList[id=oufi_heathcliff_analysis].content
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Teatr Opowieści [P11108] — tekst] 워더링하이츠 치프 버틀러, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11108].content
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Teatr Opowieści [butler_outis_profile] — tekst] 오티스\n여\n9월 23일\nA\n177CM\n64KG
   źródło: StoryTheaterPersonality.json :: dataList[id=butler_outis_profile].content
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Teatr Opowieści [butler_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=butler_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Teatr Opowieści [P10509] — tekst] 데드레빗츠 보스, 뫼르소 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10509].content
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Teatr Opowieści [deadrabbit_meursault_profile] — tekst] 뫼르소\n남\n9월 23일\nA\n188CM\n82KG
   źródło: StoryTheaterPersonality.json :: dataList[id=deadrabbit_meursault_profile].content
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Teatr Opowieści [deadrabbit_meursault_analysis] — tekst] 명확하며 짧은 지시를, 즉 개인의 판단을 맡기지 않는 명령을 요함.
   źródło: StoryTheaterPersonality.json :: dataList[id=deadrabbit_meursault_analysis].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Teatr Opowieści [P11209] — tekst] 에드가 가문 승계자, 그레고르 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11209].content
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Teatr Opowieści [wuthering_gregor_profile] — tekst] 그레고르\n남\n9월 23일\nA\n167CM\n68KG
   źródło: StoryTheaterPersonality.json :: dataList[id=wuthering_gregor_profile].content
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Teatr Opowieści [wuthering_gregor_analysis] — tekst] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다. 하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부, 간혹 가다가는 전부가 벌레 (갑각 충의 일부, ■■■■와 유사함)의 조직으로 변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만) 역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다. 냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이 가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=wuthering_gregor_analysis].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Teatr Opowieści [P10209] — tekst] 워더링하이츠 버틀러, 파우스트 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10209].content
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Teatr Opowieści [wuthering_faust_profile] — tekst] 파우스트\n여\n9월 23일\nA\n174CM\n59KG
   źródło: StoryTheaterPersonality.json :: dataList[id=wuthering_faust_profile].content
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Teatr Opowieści [wuthering_faust_analysis] — tekst] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다. 도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로 주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는 것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도 드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로 대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는 이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: StoryTheaterPersonality.json :: dataList[id=wuthering_faust_analysis].content
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Teatr Opowieści [P10408] — tekst] 에드가 가문 치프 버틀러, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10408].content
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Teatr Opowieści [butler_ryoshu_profile] — tekst] 료슈\n여\n9월 23일\nA\n171CM\n58KG
   źródło: StoryTheaterPersonality.json :: dataList[id=butler_ryoshu_profile].content
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Teatr Opowieści [butler_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=butler_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Teatr Opowieści [P10809] — tekst] 에드가 가문 버틀러, 이스마엘 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10809].content
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Teatr Opowieści [butler_ishmael_profile] — tekst] 이스마엘\n여\n9월 23일\nA\n171CM\n57KG
   źródło: StoryTheaterPersonality.json :: dataList[id=butler_ishmael_profile].content
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Teatr Opowieści [P11009] — tekst] 새벽 사무소 해결사, 싱클레어 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11009].content
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Teatr Opowieści [dawn_sinclair_profile] — tekst] 싱클레어\n남\n9월 23일\nA\n163CM\n54KG
   źródło: StoryTheaterPersonality.json :: dataList[id=dawn_sinclair_profile].content
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Teatr Opowieści [dawn_sinclair_analysis] — tekst] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을 구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여 처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인 성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는 당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고 있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로 적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=dawn_sinclair_analysis].content
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Teatr Opowieści [P10109] — tekst] 약지 점묘파 스튜던트, 이상 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10109].content
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Teatr Opowieści [rings_yisang_profile] — tekst] 이상\n남\n9월 23일\nA\n176CM\n70KG
   źródło: StoryTheaterPersonality.json :: dataList[id=rings_yisang_profile].content
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Teatr Opowieści [rings_yisang_analysis] — tekst] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해 우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은 관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로 대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의 침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로 너그럽게 기다려 주시는 걸 권장합니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=rings_yisang_analysis].content
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Teatr Opowieści [P11109] — tekst] 약지 점묘파 스튜던트, 오티스 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P11109].content
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Teatr Opowieści [rings_outis_profile] — tekst] 오티스\n여\n9월 23일\nA\n177CM\n64KG
   źródło: StoryTheaterPersonality.json :: dataList[id=rings_outis_profile].content
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Teatr Opowieści [rings_outis_analysis] — tekst] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다. 하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를 쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로 조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한 해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다. [주의] - 다른 수감자들과는 달리 과거 사의 열람이 허락되지 않습니다. [주의] - 임무외에 머리굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=rings_outis_analysis].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Teatr Opowieści [P10609] — tekst] 20구 유로지비, 홍루 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10609].content
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Teatr Opowieści [yuro_honglu_profile] — tekst] 홍루\n남\n9월 23일\nA\n178CM\n74KG
   źródło: StoryTheaterPersonality.json :: dataList[id=yuro_honglu_profile].content
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Teatr Opowieści [yuro_honglu_analysis] — tekst] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다. 그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가 제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과 모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이 있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로 서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=yuro_honglu_analysis].content
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Teatr Opowieści [P10409] — tekst] 20구 유로지비, 료슈 이야기
   źródło: StoryTheaterPersonality.json :: dataList[id=P10409].content
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Teatr Opowieści [yuro_ryoshu_profile] — tekst] 료슈\n여\n9월 23일\nA\n171CM\n58KG
   źródło: StoryTheaterPersonality.json :: dataList[id=yuro_ryoshu_profile].content
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Teatr Opowieści [yuro_ryoshu_analysis] — tekst] 수감자마다 그들만의 신조가 있는 법이고 그걸 존중해 주는 것이 마땅한 관리자의 소관이라고들 하겠지만 어떤 건 이해해 주는 시늉조차 힘들 때도 있을 겁니다. 해당 수감자는 평소에 담배만 태우며 과묵한 상태를 유지하지만 전투를 할 때만큼은 눈빛이 황홀함으로 아른거린다는 사실을 눈치챘을 테죠. 전투 중에 대책 없이 상대의 머리통을 으깨기만 하는 건 미를 퇴보시키는 무식한 행위라고 생각합니다. [경고] - 본 수감자는 우리 회사로도 감당이 어려운 뒷배경을 가졌으니 가능한 사적인 원한을 만들지 않도록 하십시오.
   źródło: StoryTheaterPersonality.json :: dataList[id=yuro_ryoshu_analysis].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Teatr Opowieści — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=ahab_ishmael_profile#2].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Teatr Opowieści — tekst] 관리자님이 하자가 많아 보이는 여러 수감자들을 보며 막막해 하고 있을지도 모르겠습니다. 안심하세요. 본 수감자는 비교적 군말 없이 일을 처리해 나갈 수 있는 몇 안 되는 유형입니다. 합리적인 의사결정을 내릴 가능성이 높은 유형이므로 조언을 구하고 싶을 땐 해당 수감자 쪽을 바라보며 화두를 꺼내는 것도 좋은 방법입니다. 하지만 잊지 마세요. 멀고도 거대한 물웅덩이에서 말도 안 되는 그 항해를 겪고 살아남은 수감자이니만큼 인내심은 길겠지만, 한 번 관계가 틀어지기 시작하면 회복하기 어려울 것입니다.
   źródło: StoryTheaterPersonality.json :: dataList[id=butler_ishmael_profile#2].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Teatr Opowieści: StoryTheaterUIText
- plik gry: `StoryTheaterUIText.json`

636. [Teatr Opowieści [MAINSTORY] — tekst] 주요이야기
   źródło: StoryTheaterUIText.json :: dataList[id=MAINSTORY].content
   limit: do 120 znaków
   EN: Main Story
   PL: Główna Opowieść
637. [Teatr Opowieści [PERSONALITYSTORY] — tekst] 인격 이야기
   źródło: StoryTheaterUIText.json :: dataList[id=PERSONALITYSTORY].content
   limit: do 120 znaków
   EN: Identity Archive
   PL: Historie Tożsamości
638. [Teatr Opowieści [NOTE_OF_DANTE] — tekst] 단테의 노트
   źródło: StoryTheaterUIText.json :: dataList[id=NOTE_OF_DANTE].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Teatr Opowieści [EPISODE] — tekst] {0}화
   źródło: StoryTheaterUIText.json :: dataList[id=EPISODE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ep. {0}
   PL: Odc. {0}
640. [Teatr Opowieści [PAGE] — tekst] {0}장
   źródło: StoryTheaterUIText.json :: dataList[id=PAGE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pg. {0}
   PL: Rozdz. {0}
641. [Teatr Opowieści [PROGRESS] — tekst] 진행도
   źródło: StoryTheaterUIText.json :: dataList[id=PROGRESS].content
   limit: do 120 znaków
   EN: Progress
   PL: Postęp
642. [Teatr Opowieści [Before] — tekst] 전투 전
   źródło: StoryTheaterUIText.json :: dataList[id=Before].content
   limit: do 120 znaków
   EN: Pre-battle
   PL: Przed walką
643. [Teatr Opowieści [After] — tekst] 전투 후
   źródło: StoryTheaterUIText.json :: dataList[id=After].content
   limit: do 120 znaków
   EN: Post-battle
   PL: Po walce
644. [Teatr Opowieści [ENTER] — tekst] 입장
   źródło: StoryTheaterUIText.json :: dataList[id=ENTER].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
645. [Teatr Opowieści [CLOSE] — tekst] 닫기
   źródło: StoryTheaterUIText.json :: dataList[id=CLOSE].content
   limit: do 120 znaków
   EN: Close
   PL: Zamknij
646. [Teatr Opowieści [MIRRORWOLDS] — tekst] 거울 세계들
   źródło: StoryTheaterUIText.json :: dataList[id=MIRRORWOLDS].content
   limit: do 120 znaków
   EN: Mirror Worlds
   PL: Światy Lustrzane
647. [Teatr Opowieści [STORY] — tekst] 스토리
   źródło: StoryTheaterUIText.json :: dataList[id=STORY].content
   limit: do 120 znaków
   EN: Story
   PL: Fabuła
648. [Teatr Opowieści [SECURITY_MATERIAL] — tekst] 보안 자료
   źródło: StoryTheaterUIText.json :: dataList[id=SECURITY_MATERIAL].content
   limit: do 120 znaków
   EN: Classified Logs
   PL: Akta Poufne
649. [Teatr Opowieści [SPEECH] — tekst] 대사
   źródło: StoryTheaterUIText.json :: dataList[id=SPEECH].content
   limit: do 120 znaków
   EN: Dialogue
   PL: Kwestie
650. [Teatr Opowieści [OPEN_CONDITION] — tekst] 개방 조건:
   źródło: StoryTheaterUIText.json :: dataList[id=OPEN_CONDITION].content
   limit: do 120 znaków
   EN: To Unlock:
   PL: Odblokowanie:
651. [Teatr Opowieści [DEEP_ANALYSIS] — tekst] 심층 분석:
   źródło: StoryTheaterUIText.json :: dataList[id=DEEP_ANALYSIS].content
   limit: do 120 znaków
   EN: In-depth:
   PL: Analiza:
652. [Teatr Opowieści [DATA_DOWNLOAD] — tekst] 데이터 다운로드
   źródło: StoryTheaterUIText.json :: dataList[id=DATA_DOWNLOAD].content
   limit: do 120 znaków
   EN: Data Download
   PL: Pobieranie danych
653. [Teatr Opowieści [DATA_DOWNLOAD_DESC] — tekst] 음성을 재생하시겠습니까?\n재생 시, 추가 데이터를 다운로드 합니다.
   źródło: StoryTheaterUIText.json :: dataList[id=DATA_DOWNLOAD_DESC].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Play sound files for voiced dialogue?\nAdditional data will be downloaded.
   PL: Odtworzyć nagrania głosowe dialogów?\nSpowoduje to pobranie dodatkowych danych.
654. [Teatr Opowieści [DATA_DOWNLOAD_NO] — tekst] 음성 없음\n(0.00MB)
   źródło: StoryTheaterUIText.json :: dataList[id=DATA_DOWNLOAD_NO].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unvoiced\n(0.00 MB)
   PL: Bez głosu\n(0.00 MB)
655. [Teatr Opowieści [DATA_DOWNLOAD_YES] — tekst] 음성 있음\n({0}MB)
   źródło: StoryTheaterUIText.json :: dataList[id=DATA_DOWNLOAD_YES].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Voiced\n({0} MB)
   PL: Z głosem\n({0} MB)
656. [Teatr Opowieści [CV_1] — tekst] 민승우
   źródło: StoryTheaterUIText.json :: dataList[id=CV_1].content
   limit: do 120 znaków
   EN: Min Seung-woo
   PL: Min Seung-woo
657. [Teatr Opowieści [CV_2] — tekst] 박지윤
   źródło: StoryTheaterUIText.json :: dataList[id=CV_2].content
   limit: do 120 znaków
   EN: Park Ji-yoon
   PL: Park Ji-yoon
658. [Teatr Opowieści [CV_3] — tekst] 김예림
   źródło: StoryTheaterUIText.json :: dataList[id=CV_3].content
   limit: do 120 znaków
   EN: Kim Yea-lim
   PL: Kim Yea-lim
659. [Teatr Opowieści [CV_4] — tekst] 이새아
   źródło: StoryTheaterUIText.json :: dataList[id=CV_4].content
   limit: do 120 znaków
   EN: Yi Sae-ah
   PL: Yi Sae-ah
660. [Teatr Opowieści [CV_5] — tekst] 권성혁
   źródło: StoryTheaterUIText.json :: dataList[id=CV_5].content
   limit: do 120 znaków
   EN: Kwon Sung-hyuk
   PL: Kwon Sung-hyuk
661. [Teatr Opowieści [CV_6] — tekst] 김신우
   źródło: StoryTheaterUIText.json :: dataList[id=CV_6].content
   limit: do 120 znaków
   EN: Kim Sin-woo
   PL: Kim Sin-woo
662. [Teatr Opowieści [CV_7] — tekst] 홍승효
   źródło: StoryTheaterUIText.json :: dataList[id=CV_7].content
   limit: do 120 znaków
   EN: Hong Seung-hyo
   PL: Hong Seung-hyo
663. [Teatr Opowieści [CV_8] — tekst] 장예나
   źródło: StoryTheaterUIText.json :: dataList[id=CV_8].content
   limit: do 120 znaków
   EN: Jang Ye-na
   PL: Jang Ye-na
664. [Teatr Opowieści [CV_9] — tekst] 윤아영
   źródło: StoryTheaterUIText.json :: dataList[id=CV_9].content
   limit: do 120 znaków
   EN: Yoon A-young
   PL: Yoon A-young
665. [Teatr Opowieści [CV_10] — tekst] 김다올
   źródło: StoryTheaterUIText.json :: dataList[id=CV_10].content
   limit: do 120 znaków
   EN: Kim Da-ol
   PL: Kim Da-ol
666. [Teatr Opowieści [CV_11] — tekst] 김보나
   źródło: StoryTheaterUIText.json :: dataList[id=CV_11].content
   limit: do 120 znaków
   EN: Kim Bo-na
   PL: Kim Bo-na
667. [Teatr Opowieści [CV_12] — tekst] 최한
   źródło: StoryTheaterUIText.json :: dataList[id=CV_12].content
   limit: do 120 znaków
   EN: Choi Han
   PL: Choi Han
668. [Teatr Opowieści [gacksung] — tekst] 동기화
   źródło: StoryTheaterUIText.json :: dataList[id=gacksung].content
   limit: do 120 znaków
   EN: Uptie
   PL: Synchronizacja
669. [Teatr Opowieści [EnterStoryPopupDesc] — tekst] {0}에\n입장하시겠습니까?
   źródło: StoryTheaterUIText.json :: dataList[id=EnterStoryPopupDesc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Will you enter\n{0}?
   PL: Czy chcesz wejść do:\n{0}?
670. [Teatr Opowieści [No] — tekst] 취소
   źródło: StoryTheaterUIText.json :: dataList[id=No].content
   limit: do 120 znaków
   EN: Cancel
   PL: Anuluj
671. [Teatr Opowieści [DetailStoryDungeon] — tekst] 스토리 던전 내부
   źródło: StoryTheaterUIText.json :: dataList[id=DetailStoryDungeon].content
   limit: do 120 znaków
   EN: Within Story Dungeon
   PL: Wewnątrz Lochu Fabularnego
672. [Teatr Opowieści [NeedsPersonality] — tekst] 필요 인격
   źródło: StoryTheaterUIText.json :: dataList[id=NeedsPersonality].content
   limit: do 120 znaków
   EN: Identity Required
   PL: Wymagana Tożsamość
673. [Teatr Opowieści [NeedsPersonalityButton] — tekst] 필요 인격 보기
   źródło: StoryTheaterUIText.json :: dataList[id=NeedsPersonalityButton].content
   limit: do 120 znaków
   EN: View Requirements
   PL: Pokaż wymagania
674. [Teatr Opowieści [MainStoryOpenCondition_101] — tekst] 1-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_101].content
   limit: do 120 znaków
   EN: Clear 1-1
   PL: Ukończ etap 1-1
675. [Teatr Opowieści [MainStoryOpenCondition_102] — tekst] 2-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_102].content
   limit: do 120 znaków
   EN: Clear 2-1
   PL: Ukończ etap 2-1
676. [Teatr Opowieści [MainStoryOpenCondition_103] — tekst] 3-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_103].content
   limit: do 120 znaków
   EN: Clear 3-1
   PL: Ukończ etap 3-1
677. [Teatr Opowieści [PersonalityStory_OpenCodition] — tekst] 인격 동기화 {0}단계 개방
   źródło: StoryTheaterUIText.json :: dataList[id=PersonalityStory_OpenCodition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Unlocked at Uptie Tier {0}
   PL: Odblokowanie na {0}. poz. Synchronizacji
678. [Teatr Opowieści [OTHERSTORY] — tekst] 그 밖의 이야기
   źródło: StoryTheaterUIText.json :: dataList[id=OTHERSTORY].content
   limit: do 120 znaków
   EN: Detour Tales
   PL: Opowieści Poboczne
679. [Teatr Opowieści [DanteNote_Record] — tekst] 기록
   źródło: StoryTheaterUIText.json :: dataList[id=DanteNote_Record].content
   limit: do 120 znaków
   EN: Record
   PL: Zapiski
680. [Teatr Opowieści [DanteNote_Time] — tekst] 시간순
   źródło: StoryTheaterUIText.json :: dataList[id=DanteNote_Time].content
   limit: do 120 znaków
   EN: Time
   PL: Chronologicznie
681. [Teatr Opowieści [DanteNote_Update] — tekst] 기록순
   źródło: StoryTheaterUIText.json :: dataList[id=DanteNote_Update].content
   limit: do 120 znaków
   EN: Update
   PL: Wg wpisu
682. [Teatr Opowieści [DanteNote_Main] — tekst] 어디서부터 써야 하는지 모르겠다.\n어디서부터 기억을 잃었는지도 모르겠으니까 당연한가.\n일단, 기억에 없는 것들을 마주치면 닥치는 대로 적어볼까 한다.
   źródło: StoryTheaterUIText.json :: dataList[id=DanteNote_Main].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I’m not sure where to even start.\nI guess it’s only natural, given that I can’t tell how much I forgot to begin with.\nMaybe I’ll start by making notes whenever I run into things I don’t remember.
   PL: Nie wiem nawet, od czego zacząć.\nNic dziwnego, skoro nie pamiętam nawet, jak wiele zapomniałem.\nNa początek będę po prostu zapisywał wszystko, czego nie ma w mojej pamięci, ilekroć na to natrafię.
683. [Teatr Opowieści [MINI] — tekst] MINI
   źródło: StoryTheaterUIText.json :: dataList[id=MINI].content
   limit: do 120 znaków
   EN: Mini
   PL: MINI
684. [Teatr Opowieści [DetailStoryMini] — tekst] 미니 에피소드
   źródło: StoryTheaterUIText.json :: dataList[id=DetailStoryMini].content
   limit: do 120 znaków
   EN: Mini Episodes
   PL: Miniepizody
685. [Teatr Opowieści [OtherStoryOpenCondition_9103] — tekst] 3.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9103].content
   limit: do 120 znaków
   EN: Clear 3.5-1
   PL: Ukończ etap 3.5-1
686. [Teatr Opowieści [OtherStoryOpenCondition_9010] — tekst] 3.5-9 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9010].content
   limit: do 120 znaków
   EN: Clear 3.5-9
   PL: Ukończ etap 3.5-9
687. [Teatr Opowieści [MainStoryOpenCondition_104] — tekst] 4-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_104].content
   limit: do 120 znaków
   EN: Clear 4-1
   PL: Ukończ etap 4-1
688. [Teatr Opowieści [OtherStoryOpenCondition_9104] — tekst] 4.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9104].content
   limit: do 120 znaków
   EN: Clear 4.5-1
   PL: Ukończ etap 4.5-1
689. [Teatr Opowieści [OtherStoryOpenCondition_9011] — tekst] 4.5-11 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9011].content
   limit: do 120 znaków
   EN: Clear 4.5-11
   PL: Ukończ etap 4.5-11
690. [Teatr Opowieści [MainStoryOpenCondition_105] — tekst] 5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_105].content
   limit: do 120 znaków
   EN: Clear 5-1
   PL: Ukończ etap 5-1
691. [Teatr Opowieści [OtherStoryOpenCondition_9012] — tekst] 5-36 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9012].content
   limit: do 120 znaków
   EN: Clear 5-36
   PL: Ukończ etap 5-36
692. [Teatr Opowieści [OtherStoryOpenCondition_9105] — tekst] 5.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9105].content
   limit: do 120 znaków
   EN: Clear 5.5-1
   PL: Ukończ etap 5.5-1
693. [Teatr Opowieści [OtherStoryOpenCondition_9013] — tekst] 5.5-12 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9013].content
   limit: do 120 znaków
   EN: Clear 5.5-12
   PL: Ukończ etap 5.5-12
694. [Teatr Opowieści [OtherStoryOpenCondition_9014] — tekst] 5.5-12 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9014].content
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Teatr Opowieści [OtherStoryOpenCondition_9107] — tekst] 5.5-13 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9107].content
   limit: do 120 znaków
   EN: Clear 5.5-13
   PL: Ukończ etap 5.5-13
696. [Teatr Opowieści [OtherStoryOpenCondition_9015] — tekst] 5.5-24 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9015].content
   limit: do 120 znaków
   EN: Clear 5.5-24
   PL: Ukończ etap 5.5-24
697. [Teatr Opowieści [MainStoryOpenCondition_106] — tekst] 6-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_106].content
   limit: do 120 znaków
   EN: Clear 6-1
   PL: Ukończ etap 6-1
698. [Teatr Opowieści [OtherStoryOpenCondition_9016] — tekst] 6-48 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9016].content
   limit: do 120 znaków
   EN: Clear 6-48
   PL: Ukończ etap 6-48
699. [Teatr Opowieści [theStoryOf] — tekst] 의 이야기
   źródło: StoryTheaterUIText.json :: dataList[id=theStoryOf].content
   limit: do 120 znaków
   EN: 's Story
   PL: — historia
700. [Teatr Opowieści [OtherStoryOpenCondition_9109] — tekst] 6.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9109].content
   limit: do 120 znaków
   EN: Clear 6.5-1
   PL: Ukończ etap 6.5-1
701. [Teatr Opowieści [OtherStoryOpenCondition_9017] — tekst] 6-48 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9017].content
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Teatr Opowieści [OtherStoryOpenCondition_9110] — tekst] 6.5-16 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9110].content
   limit: do 120 znaków
   EN: Clear 6.5-16
   PL: Ukończ etap 6.5-16
703. [Teatr Opowieści [personality_voice_section_before_clear_chapter_format] — tekst] {0}장 전
   źródło: StoryTheaterUIText.json :: dataList[id=personality_voice_section_before_clear_chapter_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Pre\nCanto {0}
   PL: Przed\nRozdz. {0}
704. [Teatr Opowieści [personality_voice_section_after_clear_chapter_format] — tekst] {0}장 후
   źródło: StoryTheaterUIText.json :: dataList[id=personality_voice_section_after_clear_chapter_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Post\nCanto {0}
   PL: Po\nRozdz. {0}
705. [Teatr Opowieści [PersonalityStory_OpenCodition_UnlockCode106] — tekst] 6장 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=PersonalityStory_OpenCodition_UnlockCode106].content
   limit: do 120 znaków
   EN: Clear Canto VI
   PL: Ukończ Rozdział 6
706. [Teatr Opowieści [PersoanlityStory_After] — tekst] (그 후)
   źródło: StoryTheaterUIText.json :: dataList[id=PersoanlityStory_After].content
   limit: do 120 znaków
   EN: (The After)
   PL: (Potem)
707. [Teatr Opowieści [OtherStoryOpenCondition_9018] — tekst] 6.5-30 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9018].content
   limit: do 120 znaków
   EN: Clear 6.5-30
   PL: Ukończ etap 6.5-30
708. [Teatr Opowieści [MainStoryOpenCondition_107] — tekst] 7-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_107].content
   limit: do 120 znaków
   EN: Clear 7-1
   PL: Ukończ etap 7-1
709. [Teatr Opowieści [OtherStoryOpenCondition_9019] — tekst] 7-36 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9019].content
   limit: do 120 znaków
   EN: Clear 7-36
   PL: Ukończ etap 7-36
710. [Teatr Opowieści [OtherStoryOpenCondition_9114] — tekst] 7.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9114].content
   limit: do 120 znaków
   EN: Clear 7.5-1
   PL: Ukończ etap 7.5-1
711. [Teatr Opowieści [OtherStoryOpenCondition_9116] — tekst] 7.5-15 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9116].content
   limit: do 120 znaków
   EN: Clear 7.5-15
   PL: Ukończ etap 7.5-15
712. [Teatr Opowieści [MainStoryOpenCondition_108] — tekst] 8-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_108].content
   limit: do 120 znaków
   EN: Clear 8-1
   PL: Ukończ etap 8-1
713. [Teatr Opowieści [OtherStoryOpenCondition_9020] — tekst] 8-33 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9020].content
   limit: do 120 znaków
   EN: Clear 8-33
   PL: Ukończ etap 8-33
714. [Teatr Opowieści [Inter] — tekst] 전투 중
   źródło: StoryTheaterUIText.json :: dataList[id=Inter].content
   limit: do 120 znaków
   EN: Battle In Progress
   PL: W trakcie walki
715. [Teatr Opowieści [ChapterTitleConfig_Arknights] — tekst] Arknights
   źródło: StoryTheaterUIText.json :: dataList[id=ChapterTitleConfig_Arknights].content
   limit: do 120 znaków
   EN: Arknights
   PL: Arknights
716. [Teatr Opowieści [OtherStoryOpenCondition_9119] — tekst] 8.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9119].content
   limit: do 120 znaków
   EN: Clear 8.5-1
   PL: Ukończ etap 8.5-1
717. [Teatr Opowieści [OtherStoryOpenCondition_9120] — tekst] LC-PC-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9120].content
   limit: do 120 znaków
   EN: Clear LC-PC-1
   PL: Ukończ etap LC-PC-1
718. [Teatr Opowieści [MainStoryOpenCondition_109] — tekst] 9-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_109].content
   limit: do 120 znaków
   EN: Clear 9-1
   PL: Ukończ etap 9-1
719. [Teatr Opowieści [OtherStoryOpenCondition_9021] — tekst] 제8회 발푸르기스의 밤 쉬움 난이도 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9021].content
   limit: do 120 znaków
   EN: Clear The 8th Walpurgis Night (Easy)
   PL: Ukończ 8. Noc Walpurgii (Łatwy)
720. [Teatr Opowieści [OtherStoryOpenCondition_9125] — tekst] 9.5-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9125].content
   limit: do 120 znaków
   EN: Clear 9.5-1
   PL: Ukończ etap 9.5-1
721. [Teatr Opowieści [OtherStoryOpenCondition_9127] — tekst] 9.5-15 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9127].content
   limit: do 120 znaków
   EN: Clear 9.5-15
   PL: Ukończ etap 9.5-15
722. [Teatr Opowieści [MainStoryOpenCondition_110] — tekst] 10-1 스테이지 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=MainStoryOpenCondition_110].content
   limit: do 120 znaków
   EN: Clear 10-1
   PL: Ukończ etap 10-1
723. [Teatr Opowieści [A] — tekst] A
   źródło: StoryTheaterUIText.json :: dataList[id=A].content
   limit: do 120 znaków
   EN: A
   PL: A
724. [Teatr Opowieści [B] — tekst] B
   źródło: StoryTheaterUIText.json :: dataList[id=B].content
   limit: do 120 znaków
   EN: B
   PL: B
725. [Teatr Opowieści [C] — tekst] C
   źródło: StoryTheaterUIText.json :: dataList[id=C].content
   limit: do 120 znaków
   EN: C
   PL: C
726. [Teatr Opowieści [OtherStoryOpenCondition_9022] — tekst] 제10회 발푸르기스의 밤 쉬움 난이도 클리어
   źródło: StoryTheaterUIText.json :: dataList[id=OtherStoryOpenCondition_9022].content
   limit: do 120 znaków
   EN: Clear The 10th Walpurgis Night (Easy)
   PL: Ukończ 10. Noc Walpurgii (Łatwy)

## Teatr Opowieści: StoryUIText
- plik gry: `StoryUIText.json`

727. [Teatr Opowieści [story_ui_clear_all_cathy_button] — tekst] 모든 캐시 삭제
   źródło: StoryUIText.json :: dataList[id=story_ui_clear_all_cathy_button].content
   limit: do 120 znaków
   EN: Clear All Cathy
   PL: Wyczyść całą Cathy
728. [Teatr Opowieści [story_ui_ask_clear_all_cathy] — tekst] 모든 캐시를 삭제하시겠습니까?
   źródło: StoryUIText.json :: dataList[id=story_ui_ask_clear_all_cathy].content
   limit: do 120 znaków
   EN: Clear All Cathy?
   PL: Wyczyścić całą Cathy?

## Teatr Opowieści: StoryVoiceSettingUI
- plik gry: `StoryVoiceSettingUI.json`

729. [Teatr Opowieści [select_all] — tekst] 전체 선택
   źródło: StoryVoiceSettingUI.json :: dataList[id=select_all].content
   limit: do 120 znaków
   EN: Select All
   PL: Zaznacz wszystko
730. [Teatr Opowieści [deselect_all] — tekst] 전체 해제
   źródło: StoryVoiceSettingUI.json :: dataList[id=deselect_all].content
   limit: do 120 znaków
   EN: Deselect All
   PL: Odznacz wszystko
731. [Teatr Opowieści [story_voice_setting_ui_title] — tekst] 스토리 보이스 관리
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_setting_ui_title].content
   limit: do 120 znaków
   EN: Story Voice Management
   PL: Zarządzanie głosami fabularnymi
732. [Teatr Opowieści [story_voice_setting_ui_desc] — tekst] 보이스를 적용할 항목을 선택해주세요.
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_setting_ui_desc].content
   limit: do 120 znaków
   EN: Select the Voice files you want to keep on your device.
   PL: Wybierz pliki głosowe, które mają być przechowywane na urządzeniu.
733. [Teatr Opowieści [story_voice_process_confirm_title] — tekst] 스토리 보이스 관리
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_confirm_title].content
   (powtórzenie elementu 731 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Teatr Opowieści [story_voice_process_confirm_main_title] — tekst] 아래 내용으로 보이스 데이터를 변경합니다.\n계속하시겠습니까?
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_confirm_main_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Applying the following changes to your local voice files.\nWould you like to continue?
   PL: Poniższe zmiany w danych głosowych zostaną zastosowane.\nKontynuować?
735. [Teatr Opowieści [story_voice_process_confirm_line] — tekst] [{0}] {1} - {2}
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_confirm_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: [{0}] {1} - {2}
   PL: [{0}] {1} - {2}
736. [Teatr Opowieści [story_voice_process_delete_label] — tekst] 삭제
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_delete_label].content
   limit: do 120 znaków
   EN: Delete
   PL: Usuń
737. [Teatr Opowieści [story_voice_process_download_label] — tekst] 다운로드
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_download_label].content
   limit: do 120 znaków
   EN: Download
   PL: Pobierz
738. [Teatr Opowieści [story_voice_process_progress_title] — tekst] 스토리 보이스 관리
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_progress_title].content
   (powtórzenie elementu 731 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Teatr Opowieści [story_voice_process_progress_desc] — tekst] 다운로드 상태 변경중입니다...
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_progress_desc].content
   limit: do 120 znaków
   EN: Processing voice file storage...
   PL: Zmienianie stanu pobranych plików…
740. [Teatr Opowieści [story_voice_process_applying_label] — tekst] 적용 중
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_applying_label].content
   limit: do 120 znaków
   EN: Applying...
   PL: Stosowanie…
741. [Teatr Opowieści [story_voice_process_complete_title] — tekst] 스토리 보이스 관리
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_complete_title].content
   (powtórzenie elementu 731 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Teatr Opowieści [story_voice_process_complete_desc] — tekst] 선택하신 챕터의 보이스 파일 상태를 변경했습니다.
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_complete_desc].content
   limit: do 120 znaków
   EN: Voice files for the selected Chapters have been adjusted.
   PL: Zmieniono stan plików głosowych dla wybranych rozdziałów.
743. [Teatr Opowieści [story_voice_process_progress_count] — tekst] {0}/{1}
   źródło: StoryVoiceSettingUI.json :: dataList[id=story_voice_process_progress_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}/{1}
   PL: {0}/{1}

## Rozdziały, etapy i zdolności Dantego: Ch8TextEffectSettings
- plik gry: `Ch8TextEffectSettings.json`

744. [Rozdziały, etapy i zdolności Dantego [S833I2] — tekst] 그리고 내일은 보옥 오라버니가 좋아하는 놀이를 하는 거야.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I2].effects[id=1].texts[#0].texts[#0].text
   limit: do 130 znaków
   EN: And tomorrow, we'll play whatever big bro Baoyu's favorite game is. How's that for a plan, huh?
   PL: A jutro pobawimy się w to, co braciszek Baoyu lubi najbardziej.
745. [Rozdziały, etapy i zdolności Dantego [S833I2] — tekst] 그래도 오라버니가 좋아하는 게 하나 정돈 있을 거 아니야?
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I2].effects[id=1].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: But what do <i>you</i> want? Here's some homework for you—when we meet tomorrow...
   PL: Przecież musi być choć jedna rzecz, którą lubisz, braciszku?
746. [Rozdziały, etapy i zdolności Dantego [S833I2] — tekst] 생각해 와. 알았지?
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I2].effects[id=1].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: ... you better have come up with something you like, okay?
   PL: Wymyśl coś na jutro. Zgoda?
747. [Rozdziały, etapy i zdolności Dantego [S833I3] — tekst] 모래들이랑 자갈이랑 나뭇잎이랑 씨앗을 섞어서 최고의 환을 만드는 사람이 승리!
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I3].effects[id=4].texts[#0].texts[#0].text
   limit: do 130 znaków
   EN: Gather a bunch of sand, and pebbles, and leaves, and seed to make a Bolus, and the best Bolus wins!
   PL: Kto zmiesza piasek, kamyki, listki i nasiona w najlepszy Bolus — ten wygrywa!
748. [Rozdziały, etapy i zdolności Dantego [S833I3] — tekst] 나는 환 만들기 놀이하고 싶은데!
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I3].effects[id=4].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: I wanna play a Bolus making game!
   PL: Ja chcę się pobawić w lepienie Bolusów!
749. [Rozdziały, etapy i zdolności Dantego [S833I32] — tekst] 형 말을 듣지 않아서 미안해…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I32].effects[id=4].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Bro...ther... I'm... sorry... I should've listened... to you...
   PL: Przepraszam, że cię nie posłuchałem, bracie…
750. [Rozdziały, etapy i zdolności Dantego [S833I32] — tekst] 형이 너무… 부러웠어…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I32].effects[id=4].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: But I was just so... envious...
   PL: Tak bardzo… ci zazdrościłem…
751. [Rozdziały, etapy i zdolności Dantego [S833I32] — tekst] 그곳에서 어떤… 결과를 보여줄지…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I32].effects[id=4].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: I just wanted to know… what they were gonna show here...
   PL: Chciałem tylko zobaczyć… jaki wynik tam pokażą…
752. [Rozdziały, etapy i zdolności Dantego [S833I4] — tekst] 보옥아 나오렴.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I4].effects[id=3].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Come, little Baoyu.
   PL: Chodź, mały Baoyu.
753. [Rozdziały, etapy i zdolności Dantego [S833I4] — tekst] 어르신들께 문안 인사 갈 시간이란다.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I4].effects[id=3].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: It is time for you to visit the elders.
   PL: Pora złożyć poranny pokłon starszyźnie.
754. [Rozdziały, etapy i zdolności Dantego [S833I4] — tekst] 선인들께서 기다리신단다.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I4].effects[id=3].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: The revered Xianren await us.
   PL: Czcigodni Xianren już czekają.
755. [Rozdziały, etapy i zdolności Dantego [S833I4] — tekst] 그분들은 네 문안인사 만을 기다리고 계시는데…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I4].effects[id=3].texts[#3].texts[#0].text
   limit: do 120 znaków
   EN: The revered Xianren await your arrival...
   PL: Czekają wyłącznie na twoje powitanie…
756. [Rozdziały, etapy i zdolności Dantego [S833I42] — tekst] 보옥아 나오렴.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I42].effects[id=3].texts[#0].texts[#0].text
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Rozdziały, etapy i zdolności Dantego [S833I42] — tekst] 어르신들께 문안 인사 갈 시간이란다.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I42].effects[id=3].texts[#1].texts[#0].text
   (powtórzenie elementu 753 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Rozdziały, etapy i zdolności Dantego [S833I42] — tekst] 선인들께서 기다리신단다.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I42].effects[id=3].texts[#2].texts[#0].text
   (powtórzenie elementu 754 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Rozdziały, etapy i zdolności Dantego [S833I42] — tekst] 그분들은 네 문안인사 만을 기다리고 계시는데…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I42].effects[id=3].texts[#3].texts[#0].text
   (powtórzenie elementu 755 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Rozdziały, etapy i zdolności Dantego [S833I42] — tekst] <b>어쩔 수 없습니다, 도련님.</b>
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I42].effects[id=3].texts[#4].texts[#0].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <b>, </b>
   EN: <b>It cannot be helped, young master.</b>
   PL: <b>Nic nie można na to poradzić, paniczku.</b>
761. [Rozdziały, etapy i zdolności Dantego [S833I42] — tekst] 그저 바라만 보고 계시는 것이 제일 현명하겠지요.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I42].effects[id=3].texts[#5].texts[#0].text
   limit: do 120 znaków
   EN: The prudent option would be to witness it all in silence.
   PL: Najrozsądniej będzie po prostu przyglądać się temu w milczeniu.
762. [Rozdziały, etapy i zdolności Dantego [S833I5] — tekst] 오빠는 방금… 나한테는 절대 하지 말아야 할 말을 했어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I5].effects[id=2].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: You... never should have said that. To me.
   PL: Właśnie powiedziałeś coś… czego nigdy nie wolno ci było mi powiedzieć, bracie.
763. [Rozdziały, etapy i zdolności Dantego [S833I5] — tekst] …이제 다시는 오빠 방으로 오지 않을 거야.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I5].effects[id=2].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: ... I won't be visiting you ever, ever again.
   PL: …Już nigdy więcej nie przyjdę do twojego pokoju.
764. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] 오빠는 방금… 나한테는 절대 하지 말아야 할 말을 했어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#0].texts[#0].text
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] …이제 다시는 오빠 방으로 오지 않을 거야.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#1].texts[#0].text
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] 네가… 네가 도와주기만 했어도…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: I... I didn't have to die yesterday...
   PL: Gdybyś tylko… gdybyś tylko mi pomógł…
767. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] 어제의 나는 살 수 있었어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#2].texts[#1].text
   limit: do 120 znaków
   EN: If you'd just helped me.
   PL: Wczorajszy ja mógłby przeżyć.
768. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] 목이 베어질 때 진짜 끔찍하게 아파.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#3].texts[#0].text
   limit: do 120 znaków
   EN: Do you have any idea how much it hurts when they chop off your neck?
   PL: Kiedy ścinają ci głowę, to boli tak potwornie.
769. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] 아픈데도 소리조차 못 질러. 너는 알아?
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#3].texts[#1].text
   limit: do 120 znaków
   EN: It hurts. It really, really hurts, but you can't even scream.
   PL: Boli, a nie możesz nawet krzyknąć. Wiesz, jakie to uczucie?
770. [Rozdziały, etapy i zdolności Dantego [S833I52] — tekst] …네가 평생 고통스러운 날만 보냈으면 좋겠어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I52].effects[id=2].texts[#3].texts[#2].text
   limit: do 120 znaków
   EN: ... I wish for nothing but the worst sufferings in what's left of your miserable life.
   PL: …Obyś do końca życia zaznawał już wyłącznie cierpienia.
771. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] 오빠는 방금… 나한테는 절대 하지 말아야 할 말을 했어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#0].texts[#0].text
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] …이제 다시는 오빠 방으로 오지 않을 거야.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#1].texts[#0].text
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] 어제의 나는 살 수 있었어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#2].texts[#0].text
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] …네가 평생 고통스러운 날만 보냈으면 좋겠어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#3].texts[#0].text
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] 보옥, 할머니랑 어머니가 그러는데,
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#4].texts[#0].text
   limit: do 120 znaków
   EN: Baoyu, grandma and mother tell me that...
   PL: Baoyu, babcia i mama mówią,
776. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] 이 대관원에서 나만큼 너랑 맺어질 수 있는 급의 여인은 없대.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#4].texts[#1].text
   limit: do 130 znaków
   EN: ...there are no other woman in Daguanyuan who can possibly hope to match up to you... other than me.
   PL: że w całym Daguanyuanie nie ma panny godnej ciebie poza mną.
777. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] 우리 가장 좋은 것만 보고 먹고 누리면서 행복하게 살자.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#5].texts[#0].text
   limit: do 160 znaków
   EN: We'll see only the pleasant sights, eat only the best food out there, and enjoy the beautiful luxuries life has to offer.
   PL: Będziemy oglądać tylko najpiękniejsze widoki, jadać najlepsze potrawy i żyć szczęśliwie w dostatku.
778. [Rozdziały, etapy i zdolności Dantego [S833I53] — tekst] 기대되지 않아?
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I53].effects[id=2].texts[#6].texts[#0].text
   limit: do 120 znaków
   EN: Aren't you excited?
   PL: Prawda, że nie możesz się doczekać?
779. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 오빠는 방금… 나한테는 절대 하지 말아야 할 말을 했어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#0].texts[#0].text
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] …이제 다시는 오빠 방으로 오지 않을 거야.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#1].texts[#0].text
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 어제의 나는 살 수 있었어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#2].texts[#0].text
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] …네가 평생 고통스러운 날만 보냈으면 좋겠어.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#3].texts[#0].text
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 이 대관원에서 나만큼 너랑 맺어질 수 있는 급의 여인은 없대.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#4].texts[#0].text
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 우리 가장 좋은 것만 보고 먹고 누리면서 행복하게 살자.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#5].texts[#0].text
   (powtórzenie elementu 777 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 기대되지 않아?
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#6].texts[#0].text
   (powtórzenie elementu 778 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 이제는 방에만 틀어박히시려는 건가요?
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#7].texts[#0].text
   limit: do 120 znaków
   EN: So now you'd rather isolate yourself in this room?
   PL: Zamierzasz teraz zamknąć się w czterech ścianach swojego pokoju?
787. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 저도 이제 어떻게 해야 할지 모르겠어요, 오라버니의 그 미소를 볼 때면…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#7].texts[#1].text
   limit: do 120 znaków
   EN: I don't know what to do anymore. Whenever I see your smile, I...
   PL: Sama już nie wiem, co mam robić, ilekroć widzę ten twój uśmiech, braciszku…
788. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 오라버니의 그 미소를 볼 때면…
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#8].texts[#0].text
   limit: do 120 znaków
   EN: Whenever I see your smile, I...
   PL: Ilekroć widzę ten twój uśmiech…
789. [Rozdziały, etapy i zdolności Dantego [S833I54] — tekst] 좋다가도… 한없이 보기 싫어져요.
   źródło: Ch8TextEffectSettings.json :: dataList[id=S833I54].effects[id=2].texts[#8].texts[#1].text
   limit: do 130 znaków
   EN: I find myself drawn to it… before I become so hateful of it that I never want to see it again.
   PL: Najpierw mnie przyciąga… a zaraz potem budzi taką odrazę, że nie mogę na niego patrzeć.

## Rozdziały, etapy i zdolności Dantego: Ch8VideoEffectSettings
- plik gry: `Ch8VideoEffectSettings.json`

790. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch1] — tekst] 고독
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch1].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Solitude
   PL: Osamotnienie
791. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch1] — tekst] 꿋꿋함
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch1].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Steadfast
   PL: Niezłomność
792. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch1] — tekst] 미련
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch1].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Lingering
   PL: Żal za utraconym
793. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch2] — tekst] 외로움
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch2].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Loneliness
   PL: Samotność
794. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch2] — tekst] 후회
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch2].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Regret
   PL: Skrucha
795. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch2] — tekst] 기대
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch2].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Anticipation
   PL: Oczekiwanie
796. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch3] — tekst] 갈등
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch3].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Conflict
   PL: Rozterka
797. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch3] — tekst] 고뇌
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch3].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Anguish
   PL: Udręka
798. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch3] — tekst] 용기
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch3].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Courage
   PL: Odwaga
799. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch4] — tekst] 그리움
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch4].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Longing
   PL: Tęsknota
