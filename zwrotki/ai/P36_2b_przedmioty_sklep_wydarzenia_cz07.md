# Paczka AI P36 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 7/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P36_2b_przedmioty_sklep_wydarzenia_cz07.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P36_2b_przedmioty_sklep_wydarzenia_cz07.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Przedmioty, sklep i profil gracza: IAPProduct
- plik gry: `IAPProduct.json`

1. [Przedmioty, sklep i profil gracza [141] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 3
   źródło: IAPProduct.json :: dataList[id=141].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Decaextraction Ticket x3
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 3
2. [Przedmioty, sklep i profil gracza [142] — nazwa] 월간 추출 티켓 패키지 II
   źródło: IAPProduct.json :: dataList[id=142].name
   limit: do 50 znaków
   EN: Monthly Extraction Ticket Pack II
   PL: Miesięczny Pakiet Biletów Ekstrakcji II
3. [Przedmioty, sklep i profil gracza [142] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 5
   źródło: IAPProduct.json :: dataList[id=142].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Decaextraction Ticket x5
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 5
4. [Przedmioty, sklep i profil gracza [143] — nazwa] 주간 추출 티켓 패키지 I
   źródło: IAPProduct.json :: dataList[id=143].name
   limit: do 50 znaków
   EN: Weekly Extraction Ticket Pack I
   PL: Tygodniowy Pakiet Biletów Ekstrakcji I
5. [Przedmioty, sklep i profil gracza [143] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 추출 티켓 x10
   źródło: IAPProduct.json :: dataList[id=143].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Extraction Ticket x10
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Bilet Ekstrakcji x 10
6. [Przedmioty, sklep i profil gracza [144] — nazwa] 월간 경험치 패키지 I
   źródło: IAPProduct.json :: dataList[id=144].name
   limit: do 40 znaków
   EN: Monthly EXP Pack I
   PL: Miesięczny Pakiet PD I
7. [Przedmioty, sklep i profil gracza [144] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 특수 강화 티켓 IV x2\n· 인격 학습 티켓 IV x20\n· 인격 학습 티켓 III x20
   źródło: IAPProduct.json :: dataList[id=144].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Level Boost Ticket IV x2\n· Identity Training Ticket IV x20\n· Identity Training Ticket III x20
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Specjalnego Wzmocnienia Tożsamości IV x 2\n· Bilet Treningu Tożsamości IV x 20\n· Bilet Treningu Tożsamości III x 20
8. [Przedmioty, sklep i profil gracza [145] — nazwa] 월간 경험치 패키지 II
   źródło: IAPProduct.json :: dataList[id=145].name
   limit: do 40 znaków
   EN: Monthly EXP Pack II
   PL: Miesięczny Pakiet PD II
9. [Przedmioty, sklep i profil gracza [145] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 특수 강화 티켓 IV x4\n· 인격 학습 티켓 IV x20\n· 인격 학습 티켓 III x20
   źródło: IAPProduct.json :: dataList[id=145].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Level Boost Ticket IV x4\n· Identity Training Ticket IV x20\n· Identity Training Ticket III x20
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Specjalnego Wzmocnienia Tożsamości IV x 4\n· Bilet Treningu Tożsamości IV x 20\n· Bilet Treningu Tożsamości III x 20
10. [Przedmioty, sklep i profil gracza [146] — nazwa] 월간 경험치 패키지 III
   źródło: IAPProduct.json :: dataList[id=146].name
   limit: do 40 znaków
   EN: Monthly EXP Pack III
   PL: Miesięczny Pakiet PD III
11. [Przedmioty, sklep i profil gracza [146] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 특수 강화 티켓 IV x8\n· 인격 학습 티켓 IV x40\n· 인격 학습 티켓 III x40
   źródło: IAPProduct.json :: dataList[id=146].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Level Boost Ticket IV x8\n· Identity Training Ticket IV x40\n· Identity Training Ticket III x40
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Specjalnego Wzmocnienia Tożsamości IV x 8\n· Bilet Treningu Tożsamości IV x 40\n· Bilet Treningu Tożsamości III x 40
12. [Przedmioty, sklep i profil gracza [147] — nazwa] 월간 끈 패키지 I
   źródło: IAPProduct.json :: dataList[id=147].name
   limit: do 40 znaków
   EN: Monthly Thread Pack I
   PL: Miesięczny Pakiet Nici I
13. [Przedmioty, sklep i profil gracza [147] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 끈 x300
   źródło: IAPProduct.json :: dataList[id=147].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Thread x300
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Nić x 300
14. [Przedmioty, sklep i profil gracza [148] — nazwa] 월간 끈 패키지 II
   źródło: IAPProduct.json :: dataList[id=148].name
   limit: do 40 znaków
   EN: Monthly Thread Pack II
   PL: Miesięczny Pakiet Nici II
15. [Przedmioty, sklep i profil gracza [148] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 끈 x500
   źródło: IAPProduct.json :: dataList[id=148].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Thread x500
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Nić x 500
16. [Przedmioty, sklep i profil gracza [149] — nazwa] 월간 끈 패키지 III
   źródło: IAPProduct.json :: dataList[id=149].name
   limit: do 40 znaków
   EN: Monthly Thread Pack III
   PL: Miesięczny Pakiet Nici III
17. [Przedmioty, sklep i profil gracza [149] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 끈 x1000
   źródło: IAPProduct.json :: dataList[id=149].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Thread x1000
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Nić x 1000
18. [Przedmioty, sklep i profil gracza [201] — nazwa] 1주년 기념 패키지
   źródło: IAPProduct.json :: dataList[id=201].name
   limit: do 40 znaków
   EN: 1st Anniversary Pack
   PL: Pakiet 1. Rocznicy
19. [Przedmioty, sklep i profil gracza [201] — opis] 1주년 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 앤젤라 아나운서 즉시 이용 가능\n· 3성 인격 출현 추출 티켓 x1\n· 인격 성장 도약 티켓 x1\n\n※ 앤젤라 아나운서를 이미 보유한 경우, 끈 상자 x50을 획득합니다.\n※ 인격 성장 도약 티켓 사용 시, 선택한 인격의 레벨이 40, 동기화 단계가 4단계까지 증가합니다.
   źródło: IAPProduct.json :: dataList[id=201].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 1st Anniversary Pack. Contains the following items:\n\n· Immediate access to Angela Announcer\n· 3★ Guarantee Decaextraction Ticket x1\n· Identity Takeoff Ticket x1\n\n※ If you have already obtained the Angela Announcer, acquire x50 Thread Crates instead.\n※ Identity Takeoff Ticket raises an Identity’s level to up to 40, and Uptie Tier up to Tier 4.
   PL: Pakiet limitowany na 1. Rocznicy — zawiera następujące składniki:\n\n· Natychmiastowy dostęp do Komentatorki Angela\n· Bilet Dekstrakcji Gwarantowanej 3★ x 1\n· Bilet Skoku Rozwoju Tożsamości x 1\n\n※ Jeśli już posiadasz Komentatorkę Angela, otrzymasz zamiast niej 50 Skrzynek Nici.\n※ Bilet Skoku Rozwoju Tożsamości podnosi poziom wybranej Tożsamości do 40, a Stopień Synchronizacji do 4.
20. [Przedmioty, sklep i profil gracza [999] — nazwa] 림버스 패스
   źródło: IAPProduct.json :: dataList[id=999].name
   limit: do 40 znaków
   EN: Limbus Pass
   PL: Limbus Pass
21. [Przedmioty, sklep i profil gracza [999] — opis] 배틀 패스를 림버스 패스로 업그레이드할 수 있습니다.\n\n※ 새로운 시즌이 시작되면 기존 효과가 만료됩니다.
   źródło: IAPProduct.json :: dataList[id=999].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upgrades the Battle Pass into the Limbus Pass.\n\n※ Only applies for the current season’s pass.
   PL: Można ulepszyć Przepustkę Bitewną do Limbus Pass.\n\n※ Po rozpoczęciu nowego sezonu dotychczasowe efekty wygasają.
22. [Przedmioty, sklep i profil gracza [124] — nazwa] 시즌 4 시작 광기 패키지
   źródło: IAPProduct.json :: dataList[id=124].name
   limit: do 50 znaków
   EN: Season 4 Commencement Lunacy Pack
   PL: Pakiet Szaleństwa Startowego Sezonu 4
23. [Przedmioty, sklep i profil gracza [124] — opis] 매 시즌마다 초기화되는 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 1300
   źródło: IAPProduct.json :: dataList[id=124].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Seasonal offer that contains the following:\n\n· Lunacy x1300\n\n※ Please note that all Lunacy contained in this pack is Paid Lunacy.
   PL: Oferta sezonowa — zawiera następujące składniki:\n\n· Szaleństwo x 1300\n\n※ Całe Szaleństwo z tego pakietu to Płatne Szaleństwo.
24. [Przedmioty, sklep i profil gracza [125] — nazwa] 시즌 4 정착 지원품
   źródło: IAPProduct.json :: dataList[id=125].name
   limit: do 40 znaków
   EN: Season 4 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 4
25. [Przedmioty, sklep i profil gracza [125] — opis] 시즌 4 클리어 올 캐시 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 특수 강화 티켓 III x 1\n· 인격 학습 티켓 III x 30\n· 끈 x 80\n· 시즌 4 자아 파편 선택 상자 x 40
   źródło: IAPProduct.json :: dataList[id=125].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during Season 4. The pack contains the following:\n\n· Lunacy x5040\n· Decaextraction Ticket x3\n· Level Boost Ticket III x1\n· Identity Training Ticket III x30\n· Thread x80\n· Season 4 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 4: Clear All Cathy — zawiera następujące składniki:\n\n· Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Specjalnego Wzmocnienia Tożsamości III x 1\n· Bilet Treningu Tożsamości III x 30\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 4 x 40
26. [Przedmioty, sklep i profil gracza [150] — nazwa] 주간 경험치 패키지
   źródło: IAPProduct.json :: dataList[id=150].name
   limit: do 40 znaków
   EN: Weekly EXP Pack
   PL: Tygodniowy Pakiet PD
27. [Przedmioty, sklep i profil gracza [150] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 25\n· 인격 학습 티켓 III x 18
   źródło: IAPProduct.json :: dataList[id=150].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Identity Training Ticket IV x25\n· Identity Training Ticket III x18
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 25\n· Bilet Treningu Tożsamości III x 18
28. [Przedmioty, sklep i profil gracza [151] — nazwa] 월간 경험치 패키지 I
   źródło: IAPProduct.json :: dataList[id=151].name
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Przedmioty, sklep i profil gracza [151] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x72\n· 인격 학습 티켓 III x48
   źródło: IAPProduct.json :: dataList[id=151].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x72\n· Identity Training Ticket III x48
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 72\n· Bilet Treningu Tożsamości III x 48
30. [Przedmioty, sklep i profil gracza [152] — nazwa] 월간 경험치 패키지 II
   źródło: IAPProduct.json :: dataList[id=152].name
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Przedmioty, sklep i profil gracza [152] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x125\n· 인격 학습 티켓 III x72
   źródło: IAPProduct.json :: dataList[id=152].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x125\n· Identity Training Ticket III x72
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 125\n· Bilet Treningu Tożsamości III x 72
32. [Przedmioty, sklep i profil gracza [153] — nazwa] 월간 경험치 패키지 III
   źródło: IAPProduct.json :: dataList[id=153].name
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Przedmioty, sklep i profil gracza [153] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x250\n· 인격 학습 티켓 III x144
   źródło: IAPProduct.json :: dataList[id=153].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x250\n· Identity Training Ticket III x144
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 250\n· Bilet Treningu Tożsamości III x 144
34. [Przedmioty, sklep i profil gracza [202] — nazwa] Full Moon 2024\n기념 인격 성장 패키지
   źródło: IAPProduct.json :: dataList[id=202].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full Moon 2024\nCommemorative\nID Upgrade Pack
   PL: Pakiet Rozwoju Tożsamości\nFull Moon 2024
35. [Przedmioty, sklep i profil gracza [202] — opis] Full Moon 2024 캠페인 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n\n※ 도약 모듈 - 인격 동기화 사용 시, 선택한 인격의 동기화 단계가 4단계까지 증가합니다.
   źródło: IAPProduct.json :: dataList[id=202].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited Full Moon 2024 Campaign Commemorative Pack. Contains the following items:\n\n· Takeoff Module - ID Uptie x1\n· Identity Training Ticket IV x80\n\n※ Using the Takeoff Module - ID Uptie raises the selected Identity's Uptie Tier to 4.
   PL: Pakiet limitowany z okazji kampanii Full Moon 2024 — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n\n※ Moduł Skoku — Synchronizacja Tożsamości podnosi Stopień Synchronizacji wybranej Tożsamości do 4.
36. [Przedmioty, sklep i profil gracza [203] — nazwa] Full Moon 2024\n기념 E.G.O 성장 패키지
   źródło: IAPProduct.json :: dataList[id=203].name
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full Moon 2024\nCommemorative\nE.G.O Upgrade Pack
   PL: Pakiet Rozwoju E.G.O\nFull Moon 2024
37. [Przedmioty, sklep i profil gracza [203] — opis] Full Moon 2024 캠페인 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 3\n· 도약 모듈 - E.G.O 해석 [WAW] x 1\n\n※ 도약 모듈 - E.G.O 해석 [WAW] 사용 시, 선택한 E.G.O의 환상 해석 단계가 4단계까지 증가합니다. (최대 WAW 등급까지 적용 가능)
   źródło: IAPProduct.json :: dataList[id=203].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited Full Moon 2024 Campaign Commemorative Pack. Contains the following items:\n\n· Decaextraction Ticket x3\n· Takeoff Module - E.G.O Spinning [WAW] x1\n\n※ Using the Takeoff Module - E.G.O Spinning [WAW] raises the selected E.G.O's Threadspinning tier to 4. (Usable only on E.G.Os WAW Level or lower)
   PL: Pakiet limitowany z okazji kampanii Full Moon 2024 — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 3\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1\n\n※ Moduł Skoku — Splot Nici E.G.O [WAW] podnosi Stopień Splotu Nici wybranego E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi WAW lub niższej)
38. [Przedmioty, sklep i profil gracza [204] — nazwa] Full Moon 2024\n기념 종합 성장 패키지
   źródło: IAPProduct.json :: dataList[id=204].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full Moon 2024\nCommemorative\nComplete Pack
   PL: Pakiet Kompleksowy\nFull Moon 2024
39. [Przedmioty, sklep i profil gracza [204] — opis] Full Moon 2024 캠페인 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4\n· 도약 모듈 - 인격 동기화 x 1\n· 도약 모듈 - E.G.O 해석 [WAW] x 1\n· 인격 학습 티켓 IV x 80\n· 끈 x 100\n\n※ 도약 모듈 - 인격 동기화 사용 시, 선택한 인격의 동기화 단계가 4단계까지 증가합니다.\n\n※ 도약 모듈 - E.G.O 해석 [WAW] 사용 시, 선택한 E.G.O의 환상 해석 단계가 4단계까지 증가합니다. (최대 WAW 등급까지 적용 가능)
   źródło: IAPProduct.json :: dataList[id=204].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited Full Moon 2024 Campaign Commemorative Pack. Contains the following items:\n\n· Decaextraction Ticket x4\n· Takeoff Module - ID Uptie x1\n· Takeoff Module - E.G.O Spinning [WAW] x1\n· Identity Training Ticket IV x80\n· Threads x100\n\n※ Using the Takeoff Module - ID Uptie raises the selected Identity's Uptie Tier to 4.\n\n※ Using the Takeoff Module - E.G.O Spinning [WAW] raises the selected E.G.O's Threadspinning tier to 4. (Usable only on E.G.Os WAW Level or lower)
   PL: Pakiet limitowany z okazji kampanii Full Moon 2024 — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1\n· Bilet Treningu Tożsamości IV x 80\n· Nić x 100\n\n※ Moduł Skoku — Synchronizacja Tożsamości podnosi Stopień Synchronizacji wybranej Tożsamości do 4.\n\n※ Moduł Skoku — Splot Nici E.G.O [WAW] podnosi Stopień Splotu Nici wybranego E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi WAW lub niższej)
40. [Przedmioty, sklep i profil gracza [401] — nazwa] 복귀 한정 패키지
   źródło: IAPProduct.json :: dataList[id=401].name
   limit: do 40 znaków
   EN: Back to Office Pack
   PL: Pakiet „Powrót do Biura”
41. [Przedmioty, sklep i profil gracza [401] — opis] 복귀 유저 대상 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n※ 복귀 유저에게만 표시되며, 복귀 이벤트 기간 동안에만 구매할 수 있습니다.\n\n· 추출 티켓 x 5\n· 인격 학습 티켓 IV x 45\n· 끈 x 100
   źródło: IAPProduct.json :: dataList[id=401].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited package for returning managers. Contains the following items:\n※ This item is only visible to returning users, and can be purchased only during the return event period.\n\n· Extraction Ticket x5\n· Identity Training Ticket IV x45\n· Thread x100
   PL: Pakiet limitowany dla powracających Kierowników — zawiera następujące składniki:\n※ Widoczny wyłącznie dla powracających użytkowników; do zakupu wyłącznie w okresie wydarzenia powrotu.\n\n· Bilet Ekstrakcji x 5\n· Bilet Treningu Tożsamości IV x 45\n· Nić x 100
42. [Przedmioty, sklep i profil gracza [402] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=402].name
   limit: do 40 znaków
   EN: Target Extraction Pack
   PL: Pakiet Ekstrakcji Celowanej
43. [Przedmioty, sklep i profil gracza [402] — opis] 「특정 추출 - 라만차랜드 실장 돈키호테」 출시 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=402].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「Target Extraction - The Manager of La Manchaland Don Quixote」release commemorative limited pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet limitowany z okazji premiery „Ekstrakcja Celowana: Zarządczyni La Manchalandu Don Quixote” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
44. [Przedmioty, sklep i profil gracza [403] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=403].name
   limit: do 40 znaków
   EN: Identity Growth Pack
   PL: Pakiet Rozwoju Tożsamości
45. [Przedmioty, sklep i profil gracza [403] — opis] 「특정 추출 - 라만차랜드 실장 돈키호테」 출시 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=403].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「Target Extraction - The Manager of La Manchaland Don Quixote」release commemorative limited pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet limitowany z okazji premiery „Ekstrakcja Celowana: Zarządczyni La Manchalandu Don Quixote” — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
46. [Przedmioty, sklep i profil gracza [404] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=404].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Przedmioty, sklep i profil gracza [404] — opis] 「5.5장 20번구의 기적 BokGak」 이벤트 등장 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=404].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo III: Miracle in District 20 BokGak」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Intervallo III: Cud w Dystrykcie 20 BokGak” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
48. [Przedmioty, sklep i profil gracza [405] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct.json :: dataList[id=405].name
   limit: do 40 znaków
   EN: E.G.O Upgrade Pack
   PL: Pakiet Rozwoju E.G.O
49. [Przedmioty, sklep i profil gracza [405] — opis] 「5.5장 20번구의 기적 BokGak」 이벤트 등장 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct.json :: dataList[id=405].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo III: Miracle in District 20 BokGak」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Intervallo III: Cud w Dystrykcie 20 BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
50. [Przedmioty, sklep i profil gracza [406] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=406].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Przedmioty, sklep i profil gracza [406] — opis] 「제5회 발푸르기스의 밤」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=406].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 5th Walpurgis Night」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji 5. Nocy Walpurgii — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
52. [Przedmioty, sklep i profil gracza [407] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=407].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Przedmioty, sklep i profil gracza [407] — opis] 「제5회 발푸르기스의 밤」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=407].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「The 5th Walpurgis Night」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji 5. Nocy Walpurgii — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
54. [Przedmioty, sklep i profil gracza [408] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct.json :: dataList[id=408].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Przedmioty, sklep i profil gracza [408] — opis] 「제5회 발푸르기스의 밤」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct.json :: dataList[id=408].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 5th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji 5. Nocy Walpurgii — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
56. [Przedmioty, sklep i profil gracza [409] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=409].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Przedmioty, sklep i profil gracza [409] — opis] 「LCB 정기검진」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=409].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「LCB Regular Check-up」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji Okresowych Badań LCB — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
58. [Przedmioty, sklep i profil gracza [410] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=410].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Przedmioty, sklep i profil gracza [410] — opis] 「LCB 정기검진」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=410].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「LCB Regular Check-up」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji Okresowych Badań LCB — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
60. [Przedmioty, sklep i profil gracza [411] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct.json :: dataList[id=411].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Przedmioty, sklep i profil gracza [411] — opis] 「LCB 정기검진」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct.json :: dataList[id=411].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「LCB Regular Check-up」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji Okresowych Badań LCB — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
62. [Przedmioty, sklep i profil gracza [412] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=412].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Przedmioty, sklep i profil gracza [412] — opis] 「육참골단 BokGak」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=412].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Yield My Flesh to Claim Their Bones BokGak」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Oddam Ciało, by Złamać Ich Kości BokGak” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
64. [Przedmioty, sklep i profil gracza [413] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=413].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Przedmioty, sklep i profil gracza [413] — opis] 「육참골단 BokGak」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=413].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Yield My Flesh to Claim Their Bones BokGak」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Oddam Ciało, by Złamać Ich Kości BokGak” — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
66. [Przedmioty, sklep i profil gracza [414] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=414].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Przedmioty, sklep i profil gracza [414] — opis] 「신규 인격 · E.G.O 특정 추출 남부 리우 협회 3과 이상 · 흉통 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=414].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「New Identity & E.G.O Target Extraction - Liu Association South Section 3 Yi Sang & Thoracalgia Faust」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Sekcja 3 Południowego Stowarzyszenia Liu Yi Sang i Torakalgia Faust” — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
68. [Przedmioty, sklep i profil gracza [415] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct.json :: dataList[id=415].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Przedmioty, sklep i profil gracza [415] — opis] 「신규 인격 · E.G.O 특정 추출 남부 리우 협회 3과 이상 · 흉통 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct.json :: dataList[id=415].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「New Identity & E.G.O Target Extraction - Liu Association South Section 3 Yi Sang & Thoracalgia Faust」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Sekcja 3 Południowego Stowarzyszenia Liu Yi Sang i Torakalgia Faust” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
70. [Przedmioty, sklep i profil gracza [416] — nazwa] 2주년 기념\n추출 티켓 패키지
   źródło: IAPProduct.json :: dataList[id=416].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 2nd Anniversary\nExtraction Ticket Pack
   PL: Pakiet Biletów Ekstrakcji\n2. Rocznicy
71. [Przedmioty, sklep i profil gracza [416] — opis] 2주년 기념 한정 상품으로, 추출과 관련된 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 5
   źródło: IAPProduct.json :: dataList[id=416].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 2nd Anniversary Pack. Contains the following items:\n\n· Decaextraction Ticket x5
   PL: Pakiet limitowany na 2. Rocznicy — zawiera następujące składniki związane z Ekstrakcją:\n\n· Bilet Dekaekstrakcji x 5
72. [Przedmioty, sklep i profil gracza [417] — nazwa] 2주년 기념\n인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=417].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 2nd Anniversary\nIdentity Growth Pack
   PL: Pakiet Rozwoju Tożsamości\n2. Rocznicy
73. [Przedmioty, sklep i profil gracza [417] — opis] 2주년 기념 한정 상품으로, 인격 육성과 관련된 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 125\n· 끈 x 400
   źródło: IAPProduct.json :: dataList[id=417].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 2nd Anniversary Pack. Contains the following items:\n\n· Identity Training Ticket IV x125\n· Thread x400
   PL: Pakiet limitowany na 2. Rocznicy — zawiera następujące składniki związane z rozwojem Tożsamości:\n\n· Bilet Treningu Tożsamości IV x 125\n· Nić x 400
74. [Przedmioty, sklep i profil gracza [418] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=418].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Przedmioty, sklep i profil gracza [418] — opis] 「신규 특정 추출 동부 섕크 협회 3과 돈키호테 · 불주먹 사무소 생존자 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=418].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「New Target Extraction - Cinq Association East Section 3 Don Quixote & Firefist Office Survivor Gregor」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Sekcja 3 Wschodniego Stowarzyszenia Cinq Don Quixote i Ocalały z Biura Ognistej Pięści Gregor” — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
76. [Przedmioty, sklep i profil gracza [419] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=419].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Przedmioty, sklep i profil gracza [419] — opis] 「심야청소」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=419].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Nocturnal Sweeping」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji Nocnego Sprzątania — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
78. [Przedmioty, sklep i profil gracza [420] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=420].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Przedmioty, sklep i profil gracza [420] — opis] 「심야청소」 이벤트 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=420].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Nocturnal Sweeping」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji Nocnego Sprzątania — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
80. [Przedmioty, sklep i profil gracza [205] — nazwa] 2주년 기념\n패키지
   źródło: IAPProduct.json :: dataList[id=205].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 2nd Anniversary Pack
   PL: Pakiet 2. Rocznicy
81. [Przedmioty, sklep i profil gracza [205] — opis] 2주년 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 베르길리우스 아나운서 즉시 이용 가능\n· 3성 인격 출현 추출 티켓 x1\n· 인격 성장 도약 티켓 - ver.2 x1\n\n※ 베르길리우스 아나운서를 이미 보유한 경우, 끈 상자 x50을 획득합니다.\n※ 인격 성장 도약 티켓 - ver.2 사용 시, 선택한 인격의 레벨이 50, 동기화 단계가 4단계까지 증가합니다.
   źródło: IAPProduct.json :: dataList[id=205].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 2nd Anniversary Pack. Contains the following items:\n\n· Immediate access to Vergilius Announcer\n· 3★ Guarantee Decaextraction Ticket x1\n· Identity Takeoff Ticket - ver.2 x1\n\n※ If you have already obtained the Vergilius Announcer, acquire x50 Thread Crates instead.\n※ Identity Takeoff Ticket - ver.2 raises an Identity’s level to up to 50, and Uptie Tier up to Tier 4.
   PL: Pakiet limitowany na 2. Rocznicy — zawiera następujące składniki:\n\n· Natychmiastowy dostęp do Komentatora Vergiliusa\n· Bilet Dekstrakcji Gwarantowanej 3★ x 1\n· Bilet Skoku Rozwoju Tożsamości - ver.2 x 1\n\n※ Jeśli już posiadasz Komentatora Vergiliusa, otrzymasz zamiast niego 50 Skrzynek Nici.\n※ Bilet Skoku Rozwoju Tożsamości - ver.2 podnosi poziom wybranej Tożsamości do 50, a Stopień Synchronizacji do 4.
82. [Przedmioty, sklep i profil gracza [421] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=421].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Przedmioty, sklep i profil gracza [421] — opis] 「신규 특정 추출 중지 작은 아우 싱클레어」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=421].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Middle Little Brother Sinclair」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Młodszy Brat Środkowego Sinclair” — zawiera następujące składniki:\n\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
84. [Przedmioty, sklep i profil gracza [422] — nazwa] 특별 추출 패키지
   źródło: IAPProduct.json :: dataList[id=422].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Przedmioty, sklep i profil gracza [422] — opis] 「신규 E.G.O 특정 추출 지정 재판 로쟈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct.json :: dataList[id=422].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「E.G.O Target Extraction - Indicant's Trial Rodion」 release commemorative pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana E.G.O: Próba Wskazującego dla Rodion” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
86. [Przedmioty, sklep i profil gracza [423] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct.json :: dataList[id=423].name
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Przedmioty, sklep i profil gracza [423] — opis] 「신규 E.G.O 특정 추출 지정 재판 로쟈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [WAW] x 1
   źródło: IAPProduct.json :: dataList[id=423].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「E.G.O Target Extraction - Indicant's Trial Rodion」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [WAW] x1
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana E.G.O: Próba Wskazującego dla Rodion” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1
88. [Przedmioty, sklep i profil gracza [424] — nazwa] 인격 육성 패키지
   źródło: IAPProduct.json :: dataList[id=424].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Przedmioty, sklep i profil gracza [424] — opis] 「신규 특정 추출 R사 제 4무리 순록팀 홍루」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=424].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - R Corp. 4th Pack Reindeer Hong Lu」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 50\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Zespół Reniferów 4. Stada R Corp. Hong Lu” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20

## Przedmioty, sklep i profil gracza: IAPSticker
- plik gry: `IAPSticker.json`

90. [Przedmioty, sklep i profil gracza [135] — tekst] 인격 1인 LV 40 성장 가능
   źródło: IAPSticker.json :: dataList[id=135].content
   limit: do 120 znaków
   EN: Can level x1 ID to 40
   PL: Można wytrenować 1 Tożsamość do poz. 40
91. [Przedmioty, sklep i profil gracza [144] — tekst] 인격 2인 LV 40 성장 가능
   źródło: IAPSticker.json :: dataList[id=144].content
   limit: do 120 znaków
   EN: Can level x2 IDs to 40
   PL: Można wytrenować 2 Tożsamości do poz. 40
92. [Przedmioty, sklep i profil gracza [145] — tekst] 인격 4인 LV 40 성장 가능
   źródło: IAPSticker.json :: dataList[id=145].content
   limit: do 120 znaków
   EN: Can level x4 IDs to 40
   PL: Można wytrenować 4 Tożsamości do poz. 40
93. [Przedmioty, sklep i profil gracza [146] — tekst] 인격 9인 LV 40 성장 가능
   źródło: IAPSticker.json :: dataList[id=146].content
   limit: do 120 znaków
   EN: Can level x9 IDs to 40
   PL: Można wytrenować 9 Tożsamości do poz. 40

## Przedmioty, sklep i profil gracza: IntroductionPreset
- plik gry: `IntroductionPreset.json`

94. [Przedmioty, sklep i profil gracza [introduce_word_1] — tekst] 부릉부릉
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_1].content
   limit: do 120 znaków
   EN: Vroom-Vroom
   PL: Wrum-Wrum
95. [Przedmioty, sklep i profil gracza [introduce_word_2] — tekst] 덜컹덜컹
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_2].content
   limit: do 120 znaków
   EN: Rumble-Tumble
   PL: Tąp-Tąp
96. [Przedmioty, sklep i profil gracza [introduce_word_3] — tekst] 시계 대가리
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_3].content
   limit: do 120 znaków
   EN: Clockface
   PL: Zegarowy Łeb
97. [Przedmioty, sklep i profil gracza [introduce_word_4] — tekst] 벌레 양반
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_4].content
   limit: do 120 znaków
   EN: Bug Guy
   PL: Panicz Robak
98. [Przedmioty, sklep i profil gracza [introduce_word_5] — tekst] 모.분.조.도
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_5].content
   limit: do 120 znaków
   EN: TRANCHES
   PL: TRANCHES
99. [Przedmioty, sklep i profil gracza [introduce_word_6] — tekst] 빨래
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_6].content
   limit: do 120 znaków
   EN: Laundry
   PL: Pranie
100. [Przedmioty, sklep i profil gracza [introduce_word_7] — tekst] 버스 청소
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_7].content
   limit: do 120 znaków
   EN: Bus Jannie
   PL: Sprzątanie Autobusu
101. [Przedmioty, sklep i profil gracza [introduce_word_8] — tekst] 정의 구현
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_8].content
   limit: do 120 znaków
   EN: Enactor of Justice
   PL: Realizator Sprawiedliwości
102. [Przedmioty, sklep i profil gracza [introduce_word_9] — tekst] 두근두근
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_9].content
   limit: do 120 znaków
   EN: Pit-a-pat
   PL: Łomot-Lomot
103. [Przedmioty, sklep i profil gracza [introduce_word_10] — tekst] 쌈박질
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_10].content
   limit: do 120 znaków
   EN: Brawling
   PL: Bijatyka
104. [Przedmioty, sklep i profil gracza [introduce_word_11] — tekst] 질문
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_11].content
   limit: do 120 znaków
   EN: Questions
   PL: Pytania
105. [Przedmioty, sklep i profil gracza [introduce_word_12] — tekst] 댄스 타임
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_12].content
   limit: do 120 znaków
   EN: Dance Time
   PL: Czas na Taniec
106. [Przedmioty, sklep i profil gracza [introduce_word_13] — tekst] 기도
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_13].content
   limit: do 120 znaków
   EN: Prayer
   PL: Modlitwa
107. [Przedmioty, sklep i profil gracza [introduce_word_14] — tekst] 엔케팔린
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_14].content
   limit: do 120 znaków
   EN: Enkephalin
   PL: Enkefalina
108. [Przedmioty, sklep i profil gracza [introduce_word_15] — tekst] 림버스 컴퍼니
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_15].content
   limit: do 120 znaków
   EN: Limbus Company
   PL: Limbus Company
109. [Przedmioty, sklep i profil gracza [introduce_word_16] — tekst] 황금가지
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_16].content
   limit: do 120 znaków
   EN: Golden Bough
   PL: Złote Gałęzie
110. [Przedmioty, sklep i profil gracza [introduce_word_17] — tekst] 빵빵
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_17].content
   limit: do 120 znaków
   EN: Honk-Honk
   PL: Pip-Pip
111. [Przedmioty, sklep i profil gracza [introduce_word_18] — tekst] 우회전
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_18].content
   limit: do 120 znaków
   EN: Right Turn
   PL: Skręt w Prawo
112. [Przedmioty, sklep i profil gracza [introduce_word_19] — tekst] 째깍째깍
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_19].content
   limit: do 120 znaków
   EN: Tick-Tock
   PL: Tik-Tak
113. [Przedmioty, sklep i profil gracza [introduce_word_20] — tekst] 유행
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_20].content
   limit: do 120 znaków
   EN: In Fashion
   PL: Na Topie
114. [Przedmioty, sklep i profil gracza [introduce_word_21] — tekst] 이상
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_21].content
   limit: do 120 znaków
   EN: Yi Sang
   PL: Yi Sang
115. [Przedmioty, sklep i profil gracza [introduce_word_22] — tekst] 빨간색
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_22].content
   limit: do 120 znaków
   EN: Red
   PL: Czerwony
116. [Przedmioty, sklep i profil gracza [introduce_word_23] — tekst] 그레고르
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_23].content
   limit: do 120 znaków
   EN: Gregor
   PL: Gregor
117. [Przedmioty, sklep i profil gracza [introduce_word_24] — tekst] 로쟈
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_24].content
   limit: do 120 znaków
   EN: Rodion
   PL: Rodion
118. [Przedmioty, sklep i profil gracza [introduce_word_25] — tekst] 이스마엘
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_25].content
   limit: do 120 znaków
   EN: Ishmael
   PL: Ishmael
119. [Przedmioty, sklep i profil gracza [introduce_word_26] — tekst] 파우스트
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_26].content
   limit: do 120 znaków
   EN: Faust
   PL: Faust
120. [Przedmioty, sklep i profil gracza [introduce_word_27] — tekst] 돈키호테
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_27].content
   limit: do 120 znaków
   EN: Don Quixote
   PL: Don Quixote
121. [Przedmioty, sklep i profil gracza [introduce_word_28] — tekst] 오티스
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_28].content
   limit: do 120 znaków
   EN: Outis
   PL: Outis
122. [Przedmioty, sklep i profil gracza [introduce_word_29] — tekst] 홍루
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_29].content
   limit: do 120 znaków
   EN: Hong Lu
   PL: Hong Lu
123. [Przedmioty, sklep i profil gracza [introduce_word_30] — tekst] 뫼르소
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_30].content
   limit: do 120 znaków
   EN: Meursault
   PL: Meursault
124. [Przedmioty, sklep i profil gracza [introduce_word_31] — tekst] 히스클리프
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_31].content
   limit: do 120 znaków
   EN: Heathcliff
   PL: Heathcliff
125. [Przedmioty, sklep i profil gracza [introduce_word_32] — tekst] 단테
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_32].content
   limit: do 120 znaków
   EN: Dante
   PL: Dante
126. [Przedmioty, sklep i profil gracza [introduce_word_33] — tekst] 싱클레어
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_33].content
   limit: do 120 znaków
   EN: Sinclair
   PL: Sinclair
127. [Przedmioty, sklep i profil gracza [introduce_word_34] — tekst] 료슈
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_34].content
   limit: do 120 znaków
   EN: Ryōshū
   PL: Ryōshū
128. [Przedmioty, sklep i profil gracza [introduce_word_35] — tekst] 크리스마스
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_35].content
   limit: do 120 znaków
   EN: Christmas
   PL: Boże Narodzenie
129. [Przedmioty, sklep i profil gracza [introduce_word_36] — tekst] 닭꼬치
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_36].content
   limit: do 120 znaków
   EN: Chicken Kebab
   PL: Szaszłyk z Kurczaka
130. [Przedmioty, sklep i profil gracza [introduce_word_37] — tekst] 수염
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_37].content
   limit: do 120 znaków
   EN: Mustache
   PL: Wąsy
131. [Przedmioty, sklep i profil gracza [introduce_word_38] — tekst] 못과 망치
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_38].content
   limit: do 120 znaków
   EN: Nagel und Hammer
   PL: Nagel und Hammer
132. [Przedmioty, sklep i profil gracza [introduce_word_39] — tekst] 폐기물
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_39].content
   limit: do 120 znaków
   EN: Waste
   PL: Odpad
133. [Przedmioty, sklep i profil gracza [introduce_word_40] — tekst] 수감자
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_40].content
   limit: do 120 znaków
   EN: Sinner
   PL: Grzesznik
134. [Przedmioty, sklep i profil gracza [introduce_sentence_1] — tekst] {0} 해도 돼?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Permission to {0}?
   PL: Zezwolenie na {0}?
135. [Przedmioty, sklep i profil gracza [introduce_sentence_2] — tekst] 안녕하세요, {0}입니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Greetings, I’m {0}.
   PL: Dzień dobry, jestem {0}.
136. [Przedmioty, sklep i profil gracza [introduce_sentence_3] — tekst] {0}(은/는) 4구로 간다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} will go to District 4.
   PL: {0} jedzie do Dystryktu 4.
137. [Przedmioty, sklep i profil gracza [introduce_sentence_4] — tekst] {0} 같은 사람이 되고 싶어.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I wanna be just like {0}.
   PL: Chcę być jak {0}.
138. [Przedmioty, sklep i profil gracza [introduce_sentence_5] — tekst] {0}, 도착하면 아무나 깨워라
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_5].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}, wake me up when we’re there.
   PL: {0}, obudź mnie, jak dojedziemy.
139. [Przedmioty, sklep i profil gracza [introduce_sentence_6] — tekst] {0}(이라면/라면) 괜찮지 않을까요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_6].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} should suffice, don’t you think?
   PL: {0} powinno wystarczyć, nie sądzisz?
140. [Przedmioty, sklep i profil gracza [introduce_sentence_7] — tekst] 그저 무의미한 {0}일 뿐.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_7].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} is an idle affair.
   PL: Po prostu bezsensowne {0}.
141. [Przedmioty, sklep i profil gracza [introduce_sentence_8] — tekst] 관리자님, 저런 {0} 같은 건 그냥 무시하시는 게 좋습니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_8].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I suggest that you ignore such {0}, Executive Manager.
   PL: Radzę po prostu zignorować takie {0}, Kierowniku.
142. [Przedmioty, sklep i profil gracza [introduce_sentence_9] — tekst] 우린 일개 {0}(이지/지), 정의를 위해 나서는 히어로는 아니니까요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_9].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: We’re {0}, not “heroes” fighting for justice.
   PL: Jesteśmy po prostu {0}, nie „bohaterami” walczącymi o sprawiedliwość.
143. [Przedmioty, sklep i profil gracza [introduce_sentence_10] — tekst] 삶은 늘 {0}일 뿐.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_10].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Life is full of {0}.
   PL: Życie jest pełne {0}.
144. [Przedmioty, sklep i profil gracza [introduce_sentence_11] — tekst] 늘 하고 있던 {0} 중이다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_11].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Handling {0} as usual.
   PL: Jak zwykle — {0} w toku.
145. [Przedmioty, sklep i profil gracza [introduce_sentence_12] — tekst] 다들 와서 {0} 좀 보게나!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_12].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Come hither, fellows, and behold this {0}!
   PL: Chodźcie tu i patrzcie: {0}!
146. [Przedmioty, sklep i profil gracza [introduce_sentence_13] — tekst] 나는 {0}만 보며 살아가기로 결심했어!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_13].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I decided to forget and focus on {0}!
   PL: Postanowiłem żyć, patrząc już tylko na {0}!
147. [Przedmioty, sklep i profil gracza [introduce_sentence_14] — tekst] 각오가 되어 있으면 {0} 해보던가.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_14].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Go ahead and {0}, if you dare.
   PL: Jeśli masz odwagę, śmiało — {0}!
148. [Przedmioty, sklep i profil gracza [introduce_sentence_15] — tekst] 이런 {0} 본 적 있소?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_15].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hath you seen such {0}?
   PL: Widziano kiedyś takie {0}?
149. [Przedmioty, sklep i profil gracza [introduce_sentence_16] — tekst] 나는 울적할 때 {0} 하곤 해.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_16].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Whenever I’m feeling down, I indulge in a bit of {0}.
   PL: W smutne chwile oddaję się trochę {0}.
150. [Przedmioty, sklep i profil gracza [introduce_sentence_17] — tekst] {0}(이/가) 언제나 옳지는 않아요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_17].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} isn’t always correct.
   PL: {0} nie zawsze ma rację.
151. [Przedmioty, sklep i profil gracza [introduce_sentence_18] — tekst] 이제는 {0} 뿐이야.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_18].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All we can count on now is {0}.
   PL: Teraz pozostaje już tylko {0}.
152. [Przedmioty, sklep i profil gracza [introduce_sentence_19] — tekst] 기분 좋은 {0}, 기분 좋게 도착.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_19].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cock-a-hoop {0}’s cock-a-hoop parking.
   PL: Pod nastrojowe {0} — nastrojowy przyjazd.
153. [Przedmioty, sklep i profil gracza [introduce_sentence_20] — tekst] 약자에게 {0}(을/를) 주기 위해 왔노라!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_20].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I am come to liberate the weak and {0}!
   PL: Przybyłem, by słabym ofiarować: {0}!
154. [Przedmioty, sklep i profil gracza [introduce_sentence_21] — tekst] {0}만으로는 부족해…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_21].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} won’t cut it…
   PL: {0}… to za mało…
155. [Przedmioty, sklep i profil gracza [introduce_sentence_22] — tekst] 그렇게 쳐다봐도 소용없습니다, {0}.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_22].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You won’t sway me with that look, {0}.
   PL: To spojrzenie mnie nie zmiękczy, {0}.
156. [Przedmioty, sklep i profil gracza [introduce_sentence_23] — tekst] 우린 세상에서 제일 의미 없는 {0}(을/를) 하고 있어!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_23].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This has got to be the most pointless {0} in the world!
   PL: To chyba najbardziej bezsensowne {0} na świecie!
157. [Przedmioty, sklep i profil gracza [introduce_sentence_24] — tekst] 그래… 이딴 {0}도 있는 거군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_24].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Really… {0} can be rubbish like this, huh…
   PL: No tak… są i takie {0}, hm…
158. [Przedmioty, sklep i profil gracza [introduce_sentence_25] — tekst] 어디서 굴러온 {0}(이지/지)?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_25].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: From under what stone did {0} come out?
   PL: Skąd tu wylazło to {0}?
159. [Przedmioty, sklep i profil gracza [introduce_sentence_26] — tekst] 아, {0} 할 시간입니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_26].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Oh, it is time for {0}.
   PL: Ach, pora na {0}.
160. [Przedmioty, sklep i profil gracza [introduce_sentence_27] — tekst] 나도 그대처럼 엄청난 {0}(이/가) 되는 것이 꿈이오!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_27].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I set my heart on becoming a magnificent {0} such as you!
   PL: Moim marzeniem jest stać się takim wspaniałym {0} jak Wy!
161. [Przedmioty, sklep i profil gracza [introduce_sentence_28] — tekst] 늦었어, {0}까지 셌는데도 너희 안 왔어.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_28].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You’re late. Counted to {0} and you still didn’t come.
   PL: Późno! Policzyłem do {0}, a was dalej nie ma.
162. [Przedmioty, sklep i profil gracza [introduce_sentence_29] — tekst] 나는 {0}(을/를) 기억할 것입니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_29].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I will remember {0}.
   PL: Będę pamiętać {0}.
163. [Przedmioty, sklep i profil gracza [introduce_sentence_30] — tekst] 미안해, 다음에 {0} 사줄게.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_30].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sorry about that. I’ll buy you {0} later.
   PL: Przepraszam. Następnym razem kupię ci {0}.
164. [Przedmioty, sklep i profil gracza [introduce_sentence_31] — tekst] 어떻게 {0}(을/를) 그냥 지나칠 수 있겠소?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_31].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I cannot turn a blind eye to {0}, can I?
   PL: Nie sposób przejść obok {0} obojętnie, prawda?
165. [Przedmioty, sklep i profil gracza [introduce_sentence_32] — tekst] {0}(을/를) 기억하고 있겠지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_32].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I’m sure you remember {0}.
   PL: Na pewno pamiętasz {0}.
166. [Przedmioty, sklep i profil gracza [introduce_sentence_33] — tekst] 왜 나를 야리냐? {0} 하고 싶냐?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_33].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Why are you gawking at me? Looking to get {0}?
   PL: Czemu się gapisz? Chcesz {0}?
167. [Przedmioty, sklep i profil gracza [introduce_sentence_34] — tekst] 윽… {0}(이네요/네요), 정말.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_34].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ugh… What a mess {0} is, huh.
   PL: Ech… ale {0}, prawda…
168. [Przedmioty, sklep i profil gracza [introduce_sentence_35] — tekst] 날 보러와, {0}!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_35].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Come see me, {0}!
   PL: Odwiedź mnie, {0}!
169. [Przedmioty, sklep i profil gracza [introduce_sentence_36] — tekst] 하지만 너는 내 {0}(이야/야).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_36].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Well, you are my {0}.
   PL: Jesteś przecież moim {0}.
170. [Przedmioty, sklep i profil gracza [introduce_sentence_37] — tekst] 메피가 좋아하는 {0}.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_37].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mephi loves {0}.
   PL: Mephi kocha {0}.
171. [Przedmioty, sklep i profil gracza [introduce_sentence_38] — tekst] 야! {0} 더 없냐? 맛있네.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_38].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Oi! Got more of this {0}? It’s peak.
   PL: Hej! Nie ma więcej {0}? Kapitalne!
172. [Przedmioty, sklep i profil gracza [introduce_sentence_39] — tekst] {0}(이라고/라고) 불러주시오.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_39].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Call me {0}, if you please.
   PL: Nazywajcie mnie {0}, jeśli wolno.
173. [Przedmioty, sklep i profil gracza [introduce_sentence_40] — tekst] 최선을 다해 주세요, {0}.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_40].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Please do your best, {0}.
   PL: Proszę dać z siebie wszystko, {0}.
174. [Przedmioty, sklep i profil gracza [introduce_word_41] — tekst] 소화
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_41].content
   limit: do 120 znaków
   EN: Churning
   PL: Trawienie
175. [Przedmioty, sklep i profil gracza [introduce_word_42] — tekst] 구휼
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_42].content
   limit: do 120 znaków
   EN: Succor
   PL: Wsparcie
176. [Przedmioty, sklep i profil gracza [introduce_sentence_41] — tekst] {0}(을/를) 데우기 위한 수프를 찾으셨나요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_41].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Looking for the soup to warm up your {0}?
   PL: Szukasz zupy, by ogrzać {0}?
177. [Przedmioty, sklep i profil gracza [introduce_sentence_42] — tekst] 이보게!!!!!! {0} 하고 가시게!!!!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_42].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Salutations!!!!!! I implore thee to try this {0}!!!!
   PL: Witajcie!!!!!! Do spróbowania: {0}!!!!
178. [Przedmioty, sklep i profil gracza [introduce_word_43] — tekst] 치킨
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_43].content
   limit: do 120 znaków
   EN: Chicken
   PL: Kurczak
179. [Przedmioty, sklep i profil gracza [introduce_word_44] — tekst] 재료 손질
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_44].content
   limit: do 120 znaków
   EN: Ingredient Trimming
   PL: Przygotowanie Składników
180. [Przedmioty, sklep i profil gracza [introduce_sentence_43] — tekst] {0}, 튀겨버린다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_43].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}, rev up those fryers.
   PL: {0}, ruszaj frytkownicami.
181. [Przedmioty, sklep i profil gracza [introduce_word_45] — tekst] 심판
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_45].content
   limit: do 120 znaków
   EN: Judgement
   PL: Wyrok
182. [Przedmioty, sklep i profil gracza [introduce_sentence_45] — tekst] {0}의 말을 어찌 믿겠나!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_45].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Nay, {0}’s words cannot be trusted!
   PL: Słowa {0} nie zasługują na wiarę!
183. [Przedmioty, sklep i profil gracza [introduce_word_46] — tekst] 정화
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_46].content
   limit: do 120 znaków
   EN: Purification
   PL: Oczyszczenie
184. [Przedmioty, sklep i profil gracza [introduce_sentence_46] — tekst] {0} 해도 되겠죠…?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_46].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} should be okay, I hope…?
   PL: {0} będzie ok… chyba?
185. [Przedmioty, sklep i profil gracza [introduce_word_47] — tekst] 뚫린 골목
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_47].content
   limit: do 120 znaków
   EN: Open Alley
   PL: Przebity Zaułek
186. [Przedmioty, sklep i profil gracza [introduce_sentence_47] — tekst] 기실, {0}(이요/요).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_47].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: As a matter of fact, it is {0}.
   PL: A w rzeczywistości — to {0}.
187. [Przedmioty, sklep i profil gracza [introduce_word_48] — tekst] 세상
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_48].content
   limit: do 120 znaków
   EN: World
   PL: Świat
188. [Przedmioty, sklep i profil gracza [introduce_sentence_48] — tekst] 다음 {0}(으로/로) 넘어가려면…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_48].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: To bound over to the next {0}…
   PL: By przeskoczyć do następnego {0}…
189. [Przedmioty, sklep i profil gracza [introduce_word_49] — tekst] 공방
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_49].content
   limit: do 120 znaków
   EN: Workshop
   PL: Warsztat
190. [Przedmioty, sklep i profil gracza [introduce_sentence_49] — tekst] …네, 전화 받았습니다. {0}입니다. 말씀하십시오.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_49].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: …Yes, this is {0} on the phone. Please speak.
   PL: …Tak, słucham. Z tej strony {0}. Proszę mówić.
191. [Przedmioty, sklep i profil gracza [introduce_word_50] — tekst] 올인
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_50].content
   limit: do 120 znaków
   EN: All In
   PL: Vabank
192. [Przedmioty, sklep i profil gracza [introduce_sentence_50] — tekst] 자… {0}(이라구/라구)~ 어디 덤벼 보던가!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_50].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Alright... I'm {0}~ Come at me if you can!
   PL: Dobrze… oto {0}~ Kto śmie, niech podejdzie!
193. [Przedmioty, sklep i profil gracza [introduce_word_51] — tekst] 이쪽
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_51].content
   limit: do 120 znaków
   EN: This Way
   PL: Tędy
194. [Przedmioty, sklep i profil gracza [introduce_sentence_51] — tekst] 자… {0} 입니다!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_51].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Come on… {0}!
   PL: No więc… oto {0}!
195. [Przedmioty, sklep i profil gracza [introduce_word_52] — tekst] 경기장
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_52].content
   limit: do 120 znaków
   EN: Bullring
   PL: Arena Byków
196. [Przedmioty, sklep i profil gracza [introduce_sentence_52] — tekst] 네가 날뛸 수 있는 최고의 {0}(이지/지).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_52].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The best {0} you could ask for a stampede.
   PL: Najlepsze {0}, żeby móc wariować.
197. [Przedmioty, sklep i profil gracza [introduce_word_53] — tekst] 동료
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_53].content
   limit: do 120 znaków
   EN: Colleagues
   PL: Koledzy
198. [Przedmioty, sklep i profil gracza [introduce_sentence_53] — tekst] 이제, 나한테 {0}(이라곤/라곤) 더 이상 없으니까.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_53].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I have no {0} left now.
   PL: Nie mam już {0}.
199. [Przedmioty, sklep i profil gracza [introduce_word_54] — tekst] 프림
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_54].content
   limit: do 120 znaków
   EN: Creamer
   PL: Śmietanka
200. [Przedmioty, sklep i profil gracza [introduce_sentence_54] — tekst] {0} 안 탔네? 고맙구만…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_54].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No {0}, huh? You really care...
   PL: Bez {0}? No proszę, jak miło…
201. [Przedmioty, sklep i profil gracza [introduce_word_55] — tekst] 방출
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_55].content
   limit: do 120 znaków
   EN: Discharge
   PL: Wyzwolenie
202. [Przedmioty, sklep i profil gracza [introduce_sentence_55] — tekst] {0}할 시간이다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_55].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Time to {0}.
   PL: Czas na {0}.
203. [Przedmioty, sklep i profil gracza [introduce_word_56] — tekst] 관심
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_56].content
   limit: do 120 znaków
   EN: Attention
   PL: Uwaga
204. [Przedmioty, sklep i profil gracza [introduce_sentence_56] — tekst] 쓸데 없는 {0}(은/는)… 필요 없다!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_56].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I don't need... any pointless {0}!
   PL: Zbędne {0}… niepotrzebne!
205. [Przedmioty, sklep i profil gracza [introduce_word_57] — tekst] 눈
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_57].content
   limit: do 120 znaków
   EN: Eyes
   PL: Oczy
206. [Przedmioty, sklep i profil gracza [introduce_sentence_57] — tekst] {0} 앞이 캄캄해질걸.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_57].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Your {0} will be in the dark.
   PL: Wkrótce {0} pogrąży się w ciemności.
207. [Przedmioty, sklep i profil gracza [introduce_word_58] — tekst] 우산
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_58].content
   limit: do 120 znaków
   EN: Umbrella
   PL: Parasol
208. [Przedmioty, sklep i profil gracza [introduce_sentence_58] — tekst] {0}(이/가) 새지나 않나 모르겠소.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_58].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I worry that it may leak through the {0}.
   PL: Obawiam się, że to {0} gdzieś przecie.
209. [Przedmioty, sklep i profil gracza [introduce_word_59] — tekst] 향
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_59].content
   limit: do 120 znaków
   EN: Scent
   PL: Zapach
210. [Przedmioty, sklep i profil gracza [introduce_sentence_59] — tekst] 나는 그 {0}(이/가) 퍽 아름다워 보이오.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_59].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: That {0} seems quite attractive to me.
   PL: Tamto {0} robi dość uroczą wrażenie.
211. [Przedmioty, sklep i profil gracza [introduce_word_60] — tekst] 요정주
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_60].content
   limit: do 120 znaków
   EN: Fairy Wine
   PL: Wino Wróżek
212. [Przedmioty, sklep i profil gracza [introduce_sentence_60] — tekst] 음… {0} 한 잔…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_60].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mmm... A glass of {0}...
   PL: Mmm… kieliszek {0}…
213. [Przedmioty, sklep i profil gracza [introduce_word_61] — tekst] 투입
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_61].content
   limit: do 120 znaków
   EN: Deployment
   PL: Wtrącenie
214. [Przedmioty, sklep i profil gracza [introduce_sentence_61] — tekst] 아~ 이제야 {0}(을/를) 해주시는군요~
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_61].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ahh~ You're finally ordering my {0}~
   PL: Ah~ Nareszcie {0} w wykonaniu waszym~
215. [Przedmioty, sklep i profil gracza [introduce_word_62] — tekst] 부적
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_62].content
   limit: do 120 znaków
   EN: Talisman
   PL: Talizman
216. [Przedmioty, sklep i profil gracza [introduce_sentence_62] — tekst] {0}(을/를) 붙여야만 해…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_62].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Must attach the {0}...
   PL: Trzeba koniecznie przykleić {0}…
217. [Przedmioty, sklep i profil gracza [introduce_word_63] — tekst] 거미
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_63].content
   limit: do 120 znaków
   EN: Spider
   PL: Pająk
218. [Przedmioty, sklep i profil gracza [introduce_sentence_63] — tekst] {0}들이 좋아하겠어…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_63].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0}s will like this...
   PL: To spodoba się takim jak {0}…
219. [Przedmioty, sklep i profil gracza [introduce_word_64] — tekst] 많은 눈
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_64].content
   limit: do 120 znaków
   EN: Many Eyes
   PL: Wiele Oczu
220. [Przedmioty, sklep i profil gracza [introduce_sentence_64] — tekst] {0}(을/를) 떴지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_64].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0} opened.
   PL: Otworzyło się {0}.
221. [Przedmioty, sklep i profil gracza [introduce_word_65] — tekst] 우육면
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_65].content
   limit: do 120 znaków
   EN: Beef Noodles
   PL: Makaron Wołowy
222. [Przedmioty, sklep i profil gracza [introduce_sentence_65] — tekst] 가는 길에 {0} 드실래요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_65].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wanna have some {0} on the way back?
   PL: Zjecie może {0} w drodze powrotnej?
223. [Przedmioty, sklep i profil gracza [introduce_word_66] — tekst] 코뿔소팀
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_66].content
   limit: do 120 znaków
   EN: Rhino Team
   PL: Zespół Nosorożców
224. [Przedmioty, sklep i profil gracza [introduce_sentence_66] — tekst] {0}, 돌진합니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_66].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}, charging ahead.
   PL: {0}, szarżuje.
225. [Przedmioty, sklep i profil gracza [introduce_word_67] — tekst] 잠복임무
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_67].content
   limit: do 120 znaków
   EN: Stealth Mission
   PL: Misja Ukryta
226. [Przedmioty, sklep i profil gracza [introduce_sentence_67] — tekst] 쉿, {0} 중이야.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_67].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Shh, I'm in the middle of a {0}.
   PL: Cii, właśnie trwa {0}.
227. [Przedmioty, sklep i profil gracza [introduce_word_68] — tekst] 유치
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_68].content
   limit: do 120 znaków
   EN: Childish
   PL: Dziecinne
228. [Przedmioty, sklep i profil gracza [introduce_sentence_68] — tekst] 어때, 아직도 {0}한가?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_68].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: What say you, is it still a {0}?
   PL: No i jak, wciąż {0}?
229. [Przedmioty, sklep i profil gracza [introduce_word_69] — tekst] 헛짓거리
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_69].content
   limit: do 120 znaków
   EN: Strugglin'
   PL: Krzątanina
230. [Przedmioty, sklep i profil gracza [introduce_sentence_69] — tekst] 가만히 있어라… {0}하지 말고!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_69].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sit still... Quit {0}!
   PL: Siedź cicho… koniec z {0}!
231. [Przedmioty, sklep i profil gracza [introduce_word_70] — tekst] 용접
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_70].content
   limit: do 120 znaków
   EN: Welding
   PL: Spawanie
232. [Przedmioty, sklep i profil gracza [introduce_sentence_70] — tekst] 좋아… 다음은 {0}…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_70].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Right... Now let's get to {0}...
   PL: Dobrze… a teraz {0}…
233. [Przedmioty, sklep i profil gracza [introduce_word_71] — tekst] 변신
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_71].content
   limit: do 120 znaków
   EN: Transformation
   PL: Przemiana
234. [Przedmioty, sklep i profil gracza [introduce_sentence_71] — tekst] 자아~ {0} 완료!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_71].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Tadaa~ {0} complete!
   PL: Tadaa~ {0} — zakończono!
235. [Przedmioty, sklep i profil gracza [introduce_word_72] — tekst] 안심
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_72].content
   limit: do 120 znaków
   EN: Relax
   PL: Ukojenie
236. [Przedmioty, sklep i profil gracza [introduce_sentence_72] — tekst] 자, 다들 아가리 벌려. {0}하고 쳐마셔보라고, 후후.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_72].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Go on, open wide. {0} and cram this drink down your throats, heheh.
   PL: No to otwierajcie paszcze. {0} — i wpychajcie ten napój, hehe.
237. [Przedmioty, sklep i profil gracza [introduce_word_73] — tekst] 아저씨
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_73].content
   limit: do 120 znaków
   EN: Some Old Guy
   PL: Jakiś Dziadek
238. [Przedmioty, sklep i profil gracza [introduce_sentence_73] — tekst] {0}(이라니/라니), 말이 심하시네…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_73].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}? Come on…
   PL: {0}? Cóż za śmiałość…
239. [Przedmioty, sklep i profil gracza [introduce_word_74] — tekst] 관찰
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_74].content
   limit: do 120 znaków
   EN: Observation
   PL: Obserwacja
240. [Przedmioty, sklep i profil gracza [introduce_sentence_74] — tekst] 저는 {0} 대상이 아닙니다만…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_74].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I am not some {0} target…
   PL: Nie jestem żadnym {0} celem…
241. [Przedmioty, sklep i profil gracza [introduce_word_75] — tekst] 교육
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_75].content
   limit: do 120 znaków
   EN: Training
   PL: Szkolenie
242. [Przedmioty, sklep i profil gracza [introduce_sentence_75] — tekst] 어이가 없군. {0}(이나/나) 하고 있으라니.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_75].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Absurd. Can't believe I'm relegated to {0}.
   PL: To absurd. Mnie mieli zlecić {0}…
243. [Przedmioty, sklep i profil gracza [introduce_word_76] — tekst] 워프 열차
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_76].content
   limit: do 120 znaków
   EN: Those WARP Trains
   PL: Pociągi WARP
244. [Przedmioty, sklep i profil gracza [introduce_sentence_76] — tekst] {0}(이라는/라는) 거, 생각보다 좁던데요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_76].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} tend to be rather cramped, don't you think?
   PL: Te {0} są jednak ciasniejsze, niż myślałem, nie?
245. [Przedmioty, sklep i profil gracza [introduce_word_77] — tekst] 홍차
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_77].content
   limit: do 120 znaków
   EN: Black Tea
   PL: Czarna Herbata
246. [Przedmioty, sklep i profil gracza [introduce_sentence_77] — tekst] 주문은 {0}(이/가) 맡겠습니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_77].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} will take your orders.
   PL: Zamówienia przyjmie {0}.
247. [Przedmioty, sklep i profil gracza [introduce_word_78] — tekst] 사건
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_78].content
   limit: do 120 znaków
   EN: Case
   PL: Sprawa
248. [Przedmioty, sklep i profil gracza [introduce_sentence_78] — tekst] {0}(을/를) 끝내러 가볼까?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_78].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let's go solve this {0}, yeah?
   PL: Idziemy załatwić {0}?
249. [Przedmioty, sklep i profil gracza [introduce_word_79] — tekst] 우리
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_79].content
   limit: do 120 znaków
   EN: Ourselves
   PL: My Sami
250. [Przedmioty, sklep i profil gracza [introduce_sentence_79] — tekst] 결국, {0}(이/가) 나서서 처리해야겠구료.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_79].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Alas, it appears that we must involve {0} in this matter.
   PL: Widać, znów do akcji musi ruszyć {0}.
251. [Przedmioty, sklep i profil gracza [introduce_word_80] — tekst] 물
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_80].content
   limit: do 120 znaków
   EN: Water
   PL: Woda
252. [Przedmioty, sklep i profil gracza [introduce_sentence_80] — tekst] {0}… {0}(을/를) 좀 마셔둬야겠어…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_80].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}... I need some {0}...
   PL: {0}… dobrze byłoby napić się {0}…
253. [Przedmioty, sklep i profil gracza [introduce_word_81] — tekst] 고통
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_81].content
   limit: do 120 znaków
   EN: Pain
   PL: Ból
254. [Przedmioty, sklep i profil gracza [introduce_sentence_81] — tekst] {0} 없이 지식을 얻지 못한다나 뭐라나…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_81].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No knowledge is earned without {0}... or whatever, blah blah...
   PL: Bez {0} nie ma wiedzy… czy coś w tym stylu…
255. [Przedmioty, sklep i profil gracza [introduce_word_82] — tekst] 숲
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_82].content
   limit: do 120 znaków
   EN: Woods
   PL: Las
256. [Przedmioty, sklep i profil gracza [introduce_sentence_82] — tekst] {0}에 발을 들일 때는… 조심했어야죠!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_82].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Should've watched your steps in the {0}...!
   PL: Wchodząc w {0}, trzeba było patrzeć pod nogi…!
257. [Przedmioty, sklep i profil gracza [introduce_word_83] — tekst] 순환
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_83].content
   limit: do 120 znaków
   EN: Samsara
   PL: Sansara
258. [Przedmioty, sklep i profil gracza [introduce_sentence_83] — tekst] {0}의 고리가 일순한다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_83].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The wheel of {0} turns once.
   PL: Obrót koła: {0}.
259. [Przedmioty, sklep i profil gracza [introduce_word_84] — tekst] 지휘팀
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_84].content
   limit: do 120 znaków
   EN: Control Team
   PL: Zespół Kontroli
260. [Przedmioty, sklep i profil gracza [introduce_sentence_84] — tekst] 지금은… {0} 부서로 이동하고 있는 중입니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_84].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Currently... Moving to {0} Department.
   PL: Obecnie… w drodze do następnego oddziału: {0}.
261. [Przedmioty, sklep i profil gracza [introduce_word_85] — tekst] 갈고리 사무소
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_85].content
   limit: do 120 znaków
   EN: Hook Office
   PL: Biuro Haka
262. [Przedmioty, sklep i profil gracza [introduce_sentence_85] — tekst] 흠… 하지만 왠지 이 {0}, 오래 못 갈 거 같단 말이죠.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_85].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hm... I have a feeling that {0} won't last long.
   PL: Hm… mam wrażenie, że to {0} nie wytrzyma długo.
263. [Przedmioty, sklep i profil gracza [introduce_word_86] — tekst] 폭력
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_86].content
   limit: do 120 znaków
   EN: Violence
   PL: Przemoc
264. [Przedmioty, sklep i profil gracza [introduce_sentence_86] — tekst] 이 구속구가 나의 {0}(을/를) 저지하기엔, 턱없이 모자르지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_86].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This straight-jacket... isn't nearly enough to hold my {0} back.
   PL: Ta kaftan bezpieczeństwa… za mało na moje {0}.
265. [Przedmioty, sklep i profil gracza [introduce_word_87] — tekst] 출근
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_87].content
   limit: do 120 znaków
   EN: Labor
   PL: Praca
266. [Przedmioty, sklep i profil gracza [introduce_sentence_87] — tekst] …나의 삶은 이 {0}(과/와) 다르지 않다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_87].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ... The existence of this {0} is no different from that of mine.
   PL: …Moje życie jest jak to {0} — bez różnicy.
267. [Przedmioty, sklep i profil gracza [introduce_word_88] — tekst] 손님
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_88].content
   limit: do 120 znaków
   EN: Guest
   PL: Gość
268. [Przedmioty, sklep i profil gracza [introduce_sentence_88] — tekst] 자, 잘 보세요~ 미래의 {0}~
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_88].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Now, lookee here~ My future {0}~
   PL: No, patrzcie tylko~ przyszłość w postaci {0}~
269. [Przedmioty, sklep i profil gracza [introduce_word_89] — tekst] 일
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_89].content
   limit: do 120 znaków
   EN: Work
   PL: Robota
270. [Przedmioty, sklep i profil gracza [introduce_sentence_89] — tekst] 난 재밌으려고 {0}한다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_89].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I {0} for fun.
   PL: Ja tu {0} — dla zabawy.
271. [Przedmioty, sklep i profil gracza [introduce_word_90] — tekst] 아이수크륌
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_90].content
   limit: do 120 znaków
   EN: ICEEE-CRRREAM
   PL: LODYYYY
272. [Przedmioty, sklep i profil gracza [introduce_sentence_90] — tekst] 본인은! {0}(이/가)! 먹고 싶소!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_90].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I! WANT! TO! EAT! {0}!
   PL: Ja! CHCĘ! ZJEŚĆ! {0}!
273. [Przedmioty, sklep i profil gracza [introduce_word_91] — tekst] 복수
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_91].content
   limit: do 120 znaków
   EN: Vengeance
   PL: Zemsta
274. [Przedmioty, sklep i profil gracza [introduce_sentence_91] — tekst] 목숨을 끊어야만 {0}(이/가) 완료된다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_91].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Only by your death shall this {0} be fulfilled.
   PL: Dopiero twa śmierć spełni {0}.
275. [Przedmioty, sklep i profil gracza [introduce_word_92] — tekst] 진리
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_92].content
   limit: do 120 znaków
   EN: The Truth
   PL: Prawda
276. [Przedmioty, sklep i profil gracza [introduce_sentence_92] — tekst] {0}(이/가) 눈 앞에 있어…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_92].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} (is/are) right before me...
   PL: {0} tuż przede mną…
277. [Przedmioty, sklep i profil gracza [introduce_word_93] — tekst] 더러움
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_93].content
   limit: do 120 znaków
   EN: Filth
   PL: Brud
278. [Przedmioty, sklep i profil gracza [introduce_sentence_93] — tekst] {0}(을/를) 머금어… 쓸모 있게 만드는 거지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_93].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} nest(s) inside me... so that they may be reborn as something useful.
   PL: {0} gniazduje we mnie… i odradza się jako coś pożytecznego.
279. [Przedmioty, sklep i profil gracza [introduce_word_94] — tekst] 멸망
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_94].content
   limit: do 120 znaków
   EN: Ruin
   PL: Ruina
280. [Przedmioty, sklep i profil gracza [introduce_sentence_94] — tekst] 여기에는 네 {0}도 쓰여있지… 자, 여기!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_94].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Your {0} is written... right here!
   PL: Zapisano tu i twoje {0}… No, patrz!
281. [Przedmioty, sklep i profil gracza [introduce_word_95] — tekst] 진주
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_95].content
   limit: do 120 znaków
   EN: Pearl
   PL: Perła
282. [Przedmioty, sklep i profil gracza [introduce_sentence_95] — tekst] {0}(으로/로) 만들 가치도 없네!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_95].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Not even worth turning(it) into a {0}!
   PL: Z tego nie zrobi się nawet {0}!
283. [Przedmioty, sklep i profil gracza [introduce_word_96] — tekst] 조명
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_96].content
   limit: do 120 znaków
   EN: The Lights
   PL: Światła
284. [Przedmioty, sklep i profil gracza [introduce_sentence_96] — tekst] 총원, {0}(이/가) 점멸하는 저 곳으로.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_96].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All hands, full speed toward where {0} flicker(s).
   PL: Cała załoga, pełną parą tam, gdzie migoczą {0}.
285. [Przedmioty, sklep i profil gracza [introduce_word_97] — tekst] 파도
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_97].content
   limit: do 120 znaków
   EN: Waves
   PL: Fale
286. [Przedmioty, sklep i profil gracza [introduce_sentence_97] — tekst] 이 {0} 속에서 움직일 수 있는 건, 오직 나다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_97].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I am the only one who moves in these {0}.
   PL: Jedynie ja zdołam się poruszać w tych {0}.
287. [Przedmioty, sklep i profil gracza [introduce_word_98] — tekst] 밧줄
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_98].content
   limit: do 120 znaków
   EN: Rope
   PL: Lina
288. [Przedmioty, sklep i profil gracza [introduce_sentence_98] — tekst] {0}, 단단히 묶어라.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_98].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}. Knot tight.
   PL: {0}, zawiązać szczelnie.
289. [Przedmioty, sklep i profil gracza [introduce_word_99] — tekst] 항해
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_99].content
   limit: do 120 znaków
   EN: Voyage
   PL: Żegluga
290. [Przedmioty, sklep i profil gracza [introduce_sentence_99] — tekst] …이 {0}만 끝난다면.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_99].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: "… Once this {0} is over."
   PL: …Gdy tylko {0} dobiegnie końca.
291. [Przedmioty, sklep i profil gracza [introduce_word_100] — tekst] 집행
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_100].content
   limit: do 120 znaków
   EN: Executed
   PL: Egzekucja
292. [Przedmioty, sklep i profil gracza [introduce_sentence_100] — tekst] 그분이 적으신 대로, 모든 것을 {0}할테니.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_100].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All shall be {0}, as it is written.
   PL: Wszystko czeka na {0} — zgodnie z zapisem.
293. [Przedmioty, sklep i profil gracza [introduce_word_101] — tekst] 검
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_101].content
   limit: do 120 znaków
   EN: Blade
   PL: Ostrze
294. [Przedmioty, sklep i profil gracza [introduce_sentence_101] — tekst] {0} 끝을… 바라본다…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_101].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Focus... on the tip of my {0}...
   PL: Patrzę… na to, gdzie kończy się {0}…
295. [Przedmioty, sklep i profil gracza [introduce_word_102] — tekst] 상대
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_102].content
   limit: do 120 znaków
   EN: Opponent
   PL: Przeciwnik
296. [Przedmioty, sklep i profil gracza [introduce_sentence_102] — tekst] 나의 {0}(은/는), 어디 있는가!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_102].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Step forth, my {0}!
   PL: Staw się, mój {0}!
297. [Przedmioty, sklep i profil gracza [introduce_word_103] — tekst] 선물
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_103].content
   limit: do 120 znaków
   EN: Gift
   PL: Prezent
298. [Przedmioty, sklep i profil gracza [introduce_sentence_103] — tekst] 하, 좋은 {0}(이/가) 되겠군!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_103].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hah, you'll make a fine {0}!
   PL: Ha! Z ciebie będzie pierwsza klasa: {0}!
299. [Przedmioty, sklep i profil gracza [introduce_word_104] — tekst] 분노
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_104].content
   limit: do 120 znaków
   EN: Wrath
   PL: Gniew
300. [Przedmioty, sklep i profil gracza [introduce_sentence_104] — tekst] 네 놈의 덧없는 {0}(을/를) 담아… 이 선물을 퍼부어주도록 하지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_104].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I'll stuff your futile {0} in this gift sack... and hurl it right back at your face.
   PL: Upakuję twój próżny {0} w tym woreku… i obiorę ci nim w twarz.
301. [Przedmioty, sklep i profil gracza [introduce_word_105] — tekst] 계약
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_105].content
   limit: do 120 znaków
   EN: Contract
   PL: Kontrakt
302. [Przedmioty, sklep i profil gracza [introduce_sentence_105] — tekst] 좋다. {0}(을/를) 받아들이지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_105].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Fine. I accept your {0}.
   PL: Niech będzie. Przyjmuję twój {0}.
303. [Przedmioty, sklep i profil gracza [introduce_word_106] — tekst] 일기
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_106].content
   limit: do 120 znaków
   EN: Journaling
   PL: Dziennik
304. [Przedmioty, sklep i profil gracza [introduce_sentence_106] — tekst] 오늘의 {0}(은/는), 여기까지!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_106].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thus doth my daily {0} come to an end!
   PL: Na dziś — koniec mojego {0}!
305. [Przedmioty, sklep i profil gracza [introduce_word_107] — tekst] 열쇠
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_107].content
   limit: do 120 znaków
   EN: Key
   PL: Klucz
306. [Przedmioty, sklep i profil gracza [introduce_sentence_107] — tekst] {0}(이/가) 필요하신가요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_107].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Looking for a {0}?
   PL: Potrzebny ci {0}?
307. [Przedmioty, sklep i profil gracza [introduce_word_108] — tekst] 책
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_108].content
   limit: do 120 znaków
   EN: Books
   PL: Książki
308. [Przedmioty, sklep i profil gracza [introduce_sentence_108] — tekst] {0}에 적힌 대로구료.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_108].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: As I have read in my {0}.
   PL: Zgodnie z tym, co głosi {0}.
309. [Przedmioty, sklep i profil gracza [introduce_word_109] — tekst] 고래
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_109].content
   limit: do 120 znaków
   EN: Whale
   PL: Wieloryb
310. [Przedmioty, sklep i profil gracza [introduce_sentence_109] — tekst] 이 모든 건 {0} 탓이군!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_109].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Once again, the fault lies with {0}! All of it!
   PL: Za wszystko odpowiada {0}!
311. [Przedmioty, sklep i profil gracza [introduce_word_110] — tekst] 돌
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_110].content
   limit: do 120 znaków
   EN: Rock
   PL: Kamień
312. [Przedmioty, sklep i profil gracza [introduce_sentence_110] — tekst] 자아, 빌어보세! 이 {0}(이/가) 기꺼이 그대에게 가서 맞기를!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_110].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I wish for this {0} to smite thee true and willing!
   PL: Módlmy się! Niech to {0} chętnie poleci i trafi!
313. [Przedmioty, sklep i profil gracza [introduce_word_111] — tekst] 훈수
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_111].content
   limit: do 120 znaków
   EN: Unsolicited Advice
   PL: Nieproszona Rada
314. [Przedmioty, sklep i profil gracza [introduce_sentence_111] — tekst] {0}(은/는), 금기다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_111].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I will not accept any {0}.
   PL: {0} — to tabu.
315. [Przedmioty, sklep i profil gracza [introduce_word_112] — tekst] 꽃
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_112].content
   limit: do 120 znaków
   EN: Flowers
   PL: Kwiaty
316. [Przedmioty, sklep i profil gracza [introduce_sentence_112] — tekst] {0}(을/를) 피워볼까요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_112].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let the {0} bloom.
   PL: Niech zakwitną {0}.
317. [Przedmioty, sklep i profil gracza [introduce_word_113] — tekst] 산책
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_113].content
   limit: do 120 znaków
   EN: Stroll
   PL: Spacer
318. [Przedmioty, sklep i profil gracza [introduce_sentence_113] — tekst] 잠시 둘러보며 {0}(이나/나) 해도 되겠는가?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_113].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wouldst thou mind if I should go on a little {0} to investigate?
   PL: Czy godzisz się na krótkie {0} — dla rozpoznania?
319. [Przedmioty, sklep i profil gracza [introduce_word_114] — tekst] 술
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_114].content
   limit: do 120 znaków
   EN: Liquor
   PL: Alkohol
320. [Przedmioty, sklep i profil gracza [introduce_sentence_114] — tekst] {0}(이나/나) 빨리 따르라니까…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_114].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: C'mon, pour me some {0} already...
   PL: Nalewaj już {0}…
321. [Przedmioty, sklep i profil gracza [introduce_word_115] — tekst] 저항
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_115].content
   limit: do 120 znaków
   EN: Resist
   PL: Opór
322. [Przedmioty, sklep i profil gracza [introduce_sentence_115] — tekst] 괜히 {0}하지 말고 받아들여.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_115].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Stop {0}-ing and just accept it.
   PL: Koniec z {0} — przyjmij to.
323. [Przedmioty, sklep i profil gracza [introduce_word_116] — tekst] 불
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_116].content
   limit: do 120 znaków
   EN: Fire
   PL: Ogień
324. [Przedmioty, sklep i profil gracza [introduce_sentence_116] — tekst] 흠. 뭐, {0}(이/가) 필요하나?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_116].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hm. What, need some {0}?
   PL: Hm. Co, przyda się {0}?
325. [Przedmioty, sklep i profil gracza [introduce_word_117] — tekst] 덩굴
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_117].content
   limit: do 120 znaków
   EN: Brambles
   PL: Pnącza
326. [Przedmioty, sklep i profil gracza [introduce_sentence_117] — tekst] 이 {0}(을/를) 풀어내려 하지 마.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_117].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Don't try to untangle these {0}.
   PL: Te {0} — nie ruszaj, nie rozwiązuj.
327. [Przedmioty, sklep i profil gracza [introduce_word_118] — tekst] 방해꾼
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_118].content
   limit: do 120 znaków
   EN: Obstacle
   PL: Przeszkoda
328. [Przedmioty, sklep i profil gracza [introduce_sentence_118] — tekst] {0} 하나가 사라졌군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_118].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Now that's one less {0} in our way.
   PL: O jedno {0} mniej.
329. [Przedmioty, sklep i profil gracza [introduce_word_119] — tekst] 오찬
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_119].content
   limit: do 120 znaków
   EN: Luncheon
   PL: Uczta
330. [Przedmioty, sklep i profil gracza [introduce_sentence_119] — tekst] 다음 {0}까지는 돌아오겠습니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_119].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I shall return before the next {0}.
   PL: Wrócę, zanim nastąpi kolejne {0}.
331. [Przedmioty, sklep i profil gracza [introduce_word_120] — tekst] 시간
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_120].content
   limit: do 120 znaków
   EN: Time
   PL: Czas
332. [Przedmioty, sklep i profil gracza [introduce_sentence_120] — tekst] 필요 없는 {0}(은/는) 가져가지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_120].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I will take what surplus {0} they have.
   PL: Zabiorę to, co mają z nadmiaru — {0}.
333. [Przedmioty, sklep i profil gracza [introduce_word_121] — tekst] 악몽
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_121].content
   limit: do 120 znaków
   EN: Nightmare
   PL: Koszmara
334. [Przedmioty, sklep i profil gracza [introduce_sentence_121] — tekst] 또 그 지긋지긋한 {0}인가…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_121].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Another damned {0}…
   PL: Znów to przeklęte {0}…
335. [Przedmioty, sklep i profil gracza [introduce_word_122] — tekst] 사냥
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_122].content
   limit: do 120 znaków
   EN: Hunt
   PL: Polowanie
336. [Przedmioty, sklep i profil gracza [introduce_sentence_122] — tekst] 주인님의 말씀대로 {0}(을/를) 준비중입니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_122].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Preparing for the {0} as per our Master's orders.
   PL: Jak rozkazał Pan — przygotowuję {0}.
337. [Przedmioty, sklep i profil gracza [introduce_word_123] — tekst] 불청객
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_123].content
   limit: do 120 znaków
   EN: Interloper
   PL: Nieproszony Gość
338. [Przedmioty, sklep i profil gracza [introduce_sentence_123] — tekst] {0}(은/는) 당장 나가시오, {0}(은/는)…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_123].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Leave at once, {0}! Leave this place...!
   PL: {0}! Natychmiast się stąd wynoś, {0}…!
339. [Przedmioty, sklep i profil gracza [introduce_word_124] — tekst] 저택
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_124].content
   limit: do 120 znaków
   EN: Manor
   PL: Rezydencja
340. [Przedmioty, sklep i profil gracza [introduce_sentence_124] — tekst] {0}(을/를)… 안내해주지…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_124].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Allow me... to introduce you to this {0}...
   PL: Pozwól, że cię przywitam w tym {0}…
341. [Przedmioty, sklep i profil gracza [introduce_word_125] — tekst] 불꽃
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_125].content
   limit: do 120 znaków
   EN: Spark
   PL: Iskra
342. [Przedmioty, sklep i profil gracza [introduce_sentence_125] — tekst] 그대에게 보이는 이 {0}(은/는)… 무슨 색을 띄고 있는가!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_125].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: What color do thine eyes behold in this {0}?!
   PL: W jakim kolorze lśni tobie to {0}?!
343. [Przedmioty, sklep i profil gracza [introduce_word_126] — tekst] 전기
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_126].content
   limit: do 120 znaków
   EN: Electricity
   PL: Prąd
344. [Przedmioty, sklep i profil gracza [introduce_sentence_126] — tekst] 이제 가진 것은 이 {0}밖에 없는데… 큭, 이것까지…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_126].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This {0} is all I have left... I can't...!
   PL: To {0} to wszystko, co mi zostało… nie, nie…!
345. [Przedmioty, sklep i profil gracza [introduce_word_127] — tekst] 권위
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_127].content
   limit: do 120 znaków
   EN: Authority
   PL: Autorytet
346. [Przedmioty, sklep i profil gracza [introduce_sentence_127] — tekst] 감히… {0}에 도전하는가?!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_127].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You dare... challenge my {0}?!
   PL: Śmiesz podważać moje {0}?!
347. [Przedmioty, sklep i profil gracza [introduce_word_128] — tekst] 왕좌
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_128].content
   limit: do 120 znaków
   EN: Throne
   PL: Tron
348. [Przedmioty, sklep i profil gracza [introduce_sentence_128] — tekst] 나는 이 {0}에 묶여 홀로 통치하는 자일지니…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_128].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I am bound to reign alone atop this solitary {0}...
   PL: Ja, związany z tym {0}, panować będę sam…
349. [Przedmioty, sklep i profil gracza [introduce_word_129] — tekst] 주인놈
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_129].content
   limit: do 120 znaków
   EN: Foolish Master
   PL: Głupawy Mistrz
350. [Przedmioty, sklep i profil gracza [introduce_sentence_129] — tekst] {0} 뜻에 따라, 준비 완료.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_129].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ready, as per that {0}'s orders.
   PL: {0} tak chciał — gotowe.
351. [Przedmioty, sklep i profil gracza [introduce_word_130] — tekst] 버틀러
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_130].content
   limit: do 120 znaków
   EN: Butler
   PL: Kamerdyner
352. [Przedmioty, sklep i profil gracza [introduce_sentence_130] — tekst] 저는 유능한 {0}(이니까요/니까요).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_130].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: But of course. I am a competent {0}.
   PL: Ależ naturalnie. Jestem zdatnym {0}.
353. [Przedmioty, sklep i profil gracza [introduce_word_131] — tekst] 슬픔
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_131].content
   limit: do 120 znaków
   EN: Sorrow
   PL: Smutek
354. [Przedmioty, sklep i profil gracza [introduce_sentence_131] — tekst] 차라리… 이 {0}(과/와) 함께 일어서겠어.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_131].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Then... I choose to rise with this {0} instead.
   PL: Zamiast tego… wstanę, gdy {0} stanie ze mną.
355. [Przedmioty, sklep i profil gracza [introduce_word_132] — tekst] 발목
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_132].content
   limit: do 120 znaków
   EN: Ankle
   PL: Kostka
356. [Przedmioty, sklep i profil gracza [introduce_sentence_132] — tekst] 그러니 네 {0}(을/를) 잘라버리면…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_132].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: So once I chop off your {0}...!
   PL: A gdy odetnę ci {0}…!
357. [Przedmioty, sklep i profil gracza [introduce_word_133] — tekst] 고기
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_133].content
   limit: do 120 znaków
   EN: Meat
   PL: Mięso
358. [Przedmioty, sklep i profil gracza [introduce_sentence_133] — tekst] 상처난 {0}(은/는) 맛없으니까.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_133].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Scarred {0} isn't... tasty.
   PL: Poszarpane {0} nie smakuje.
359. [Przedmioty, sklep i profil gracza [introduce_word_134] — tekst] 작업
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_134].content
   limit: do 120 znaków
   EN: Task
   PL: Zadanie
360. [Przedmioty, sklep i profil gracza [introduce_sentence_134] — tekst] 주어진 {0}(을/를) 끝내기 전까지, 누구도 잠들 수 없다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_134].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: None of us are going to sleep until we deal with this {0}.
   PL: Nikt nie zaśnie, dopóki {0} nie będzie skończone.
361. [Przedmioty, sklep i profil gracza [introduce_word_135] — tekst] 영감
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_135].content
   limit: do 120 znaków
   EN: Inspiration
   PL: Natchnienie
362. [Przedmioty, sklep i profil gracza [introduce_sentence_135] — tekst] 그대께서 새로운 {0}(을/를) 불러와주시겠는가.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_135].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Will you rekindle the {0} within me anew?
   PL: Czyzbyś chciał przebudzić we mnie nowe {0}?
363. [Przedmioty, sklep i profil gracza [introduce_word_136] — tekst] 눈물
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_136].content
   limit: do 120 znaków
   EN: Tear
   PL: Łza
364. [Przedmioty, sklep i profil gracza [introduce_sentence_136] — tekst] 모든 슬픔과 {0}(을/를) 그러모아, 대신 울어드릴 수 있다면…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_136].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If only I could gather all the sorrow, all the {0} together, and cry in their stead...
   PL: Gdybym mogła zebrać wszystkie smutki i {0}, by płakać za innych…
365. [Przedmioty, sklep i profil gracza [introduce_word_137] — tekst] 마음
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_137].content
   limit: do 120 znaków
   EN: Heart
   PL: Serce
366. [Przedmioty, sklep i profil gracza [introduce_sentence_137] — tekst] 슬픔에 흔들린 {0}(은/는) 이렇게… 터져버리죠.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_137].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: A {0} shaken by sorrow bursts... like this.
   PL: Tak pęka {0} wstrząśnięte smutkiem…
367. [Przedmioty, sklep i profil gracza [introduce_word_138] — tekst] 정답
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_138].content
   limit: do 120 znaków
   EN: Answer
   PL: Odpowiedź
368. [Przedmioty, sklep i profil gracza [introduce_sentence_138] — tekst] 이 렌즈 너머로는 항상 {0}(이/가) 보인다구요~
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_138].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0} always reveals itself through this lens~
   PL: Przez tę soczewkę zawsze prześwituje {0}~
369. [Przedmioty, sklep i profil gracza [introduce_word_139] — tekst] 나사
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_139].content
   limit: do 120 znaków
   EN: Screw
   PL: Śruba
370. [Przedmioty, sklep i profil gracza [introduce_sentence_139] — tekst] 네놈 머리에 {0}(이/가) 빠졌나 보군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_139].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Looks like you've got a {0} loose yourself.
   PL: Wygląda na to, że w twojej głowie {0} poluzował.
371. [Przedmioty, sklep i profil gracza [introduce_word_140] — tekst] 정지
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_140].content
   limit: do 120 znaków
   EN: Cease
   PL: Bezruch
372. [Przedmioty, sklep i profil gracza [introduce_sentence_140] — tekst] 그대로. {0}하는 겁니다. 멈춰진 시간 속에. 영원히.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_140].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thus. You {0} to move. Trapped in the stopped time. For eternity.
   PL: Tak właśnie. Pozostaje {0}. W zatrzymanym czasie. Na wieczność.
373. [Przedmioty, sklep i profil gracza [introduce_word_141] — tekst] 시계
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_141].content
   limit: do 120 znaków
   EN: Watch
   PL: Zegarek
374. [Przedmioty, sklep i profil gracza [introduce_sentence_141] — tekst] 이 {0}(은/는) T사에 입사하게 되면 지급받는 것일세!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_141].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: T Corp. Employment means that thou shalt be bestowed with this {0}!
   PL: To {0} otrzymasz, gdy zostaniesz zatrudniony w T Corp.!
375. [Przedmioty, sklep i profil gracza [introduce_word_142] — tekst] 색
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_142].content
   limit: do 120 znaków
   EN: Color
   PL: Kolor
376. [Przedmioty, sklep i profil gracza [introduce_sentence_142] — tekst] 차라리 아예 {0}(을/를) 모른 채 자랐으면 좋았을 텐데.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_142].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I wish I'd never seen {0} growing up...
   PL: Chciałbym, bym nigdy nie poznał {0}…
377. [Przedmioty, sklep i profil gracza [introduce_word_143] — tekst] 주먹
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_143].content
   limit: do 120 znaków
   EN: Fist
   PL: Pięść
378. [Przedmioty, sklep i profil gracza [introduce_sentence_143] — tekst] {0}(으로/로) 매만지며 탐구할 순간.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_143].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let my {0} be the conduit through which I attain knowledge.
   PL: Nauka płynąca przez moje {0}.
379. [Przedmioty, sklep i profil gracza [introduce_word_144] — tekst] 추악함
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_144].content
   limit: do 120 znaków
   EN: Squalidity
   PL: Szpetota
380. [Przedmioty, sklep i profil gracza [introduce_sentence_144] — tekst] {0}에 모든 시선이 이끌릴지어다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_144].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Scatter. Every gaze shall be drawn to this {0}.
   PL: Każde oko spocznie na tym {0}.
381. [Przedmioty, sklep i profil gracza [introduce_word_145] — tekst] 정리
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_145].content
   limit: do 120 znaków
   EN: Cleanup
   PL: Sprzątanie
382. [Przedmioty, sklep i profil gracza [introduce_sentence_145] — tekst] {0}(이/가) 예상보다 일찍 끝났군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_145].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0} ended way ahead of schedule.
   PL: No i {0} zakończone szybciej niż planowano.
383. [Przedmioty, sklep i profil gracza [introduce_word_146] — tekst] 기억
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_146].content
   limit: do 120 znaków
   EN: Memory
   PL: Pamięć
384. [Przedmioty, sklep i profil gracza [introduce_sentence_146] — tekst] 총성과 연기에… 모든 {0}(이/가) 파묻힐 때까지…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_146].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Until echoes of gunshots and plumes of smoke bury my every {0}...!
   PL: Póki ryk strzałów i kłęby dymu nie pochłoną {0}…!
385. [Przedmioty, sklep i profil gracza [introduce_word_147] — tekst] 계획
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_147].content
   limit: do 120 znaków
   EN: Plan
   PL: Plan
386. [Przedmioty, sklep i profil gracza [introduce_sentence_147] — tekst] 이 허점투성이 {0}(을/를) 완전무결하게 만들어드리죠.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_147].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: While there are numerous deficiencies to this {0}, it will be honed into perfection.
   PL: Ten {0} pełen dziur dopracuję do doskonałości.
387. [Przedmioty, sklep i profil gracza [introduce_word_148] — tekst] 의체
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_148].content
   limit: do 120 znaków
   EN: Prosthetic Body
   PL: Ciało Protezowe
388. [Przedmioty, sklep i profil gracza [introduce_sentence_148] — tekst] {0}(을/를) 가진 놈들은 전투에서 겁을 먹지 않는다나 뭐라나.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_148].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Somethin' about how having a {0} helps dull the fear in combat, I think.
   PL: Ktoś gadał: kto ma {0}, ten się w walce nie boi.
389. [Przedmioty, sklep i profil gracza [introduce_word_149] — tekst] 방황
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_149].content
   limit: do 120 znaków
   EN: Wandering
   PL: Błądzenie
390. [Przedmioty, sklep i profil gracza [introduce_sentence_149] — tekst] 한순간이라도 놓친다면, 영원히 {0}할 테니.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_149].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Do not avert your eyes, lest you be ensnared in an eternal {0}.
   PL: A odwrócisz wzrok — wieczność w {0} spędzisz.
391. [Przedmioty, sklep i profil gracza [introduce_word_150] — tekst] 듀라한
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_150].content
   limit: do 120 znaków
   EN: Dullahan
   PL: Dullahan
392. [Przedmioty, sklep i profil gracza [introduce_sentence_150] — tekst] {0}(이여/여)! 죽도록 달릴 시간이다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_150].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ride to your demise, O {0}!
   PL: {0}! Czas galopować aż do śmierci.
393. [Przedmioty, sklep i profil gracza [introduce_word_151] — tekst] 본성
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_151].content
   limit: do 120 znaków
   EN: Instinct
   PL: Instynkt
394. [Przedmioty, sklep i profil gracza [introduce_sentence_151] — tekst] 흥, 그 따위 마음은 그저 저주받은 {0}에 지나지 않지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_151].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hmph. It's nothing more than the curse of {0}.
   PL: Hmph. To nic innego jak przeklęty {0}.
395. [Przedmioty, sklep i profil gracza [introduce_word_152] — tekst] 애도
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_152].content
   limit: do 120 znaków
   EN: Condolences
   PL: Kondolencje
396. [Przedmioty, sklep i profil gracza [introduce_sentence_152] — tekst] {0}에 미사여구는 필요치 않겠소.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_152].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: There is no need for showy, purple prose in expressing {0}.
   PL: {0} nie potrzebuje ozdobnych fraz.
397. [Przedmioty, sklep i profil gracza [introduce_word_153] — tekst] 믿음
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_153].content
   limit: do 120 znaków
   EN: Faith
   PL: Wiara
398. [Przedmioty, sklep i profil gracza [introduce_sentence_153] — tekst] 그 {0}(은/는) 헛된 바람일 뿐이지 않나…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_153].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: That {0} is just a hollow wish, isn't it...?
   PL: To {0} to jedynie czcze życzenie, nieprawdaż…?
399. [Przedmioty, sklep i profil gracza [introduce_word_154] — tekst] 가방
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_154].content
   limit: do 120 znaków
   EN: Trunk
   PL: Walizka
400. [Przedmioty, sklep i profil gracza [introduce_sentence_154] — tekst] 아… 이렇게 나도 {0}만… 남기게 되나…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_154].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ah... I'll be... just another {0} recovery mission, huh...
   PL: Ah… zostanie po mnie… tylko {0}…
401. [Przedmioty, sklep i profil gracza [introduce_word_155] — tekst] 청소
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_155].content
   limit: do 120 znaków
   EN: Cleaning
   PL: Sprzątanie
402. [Przedmioty, sklep i profil gracza [introduce_sentence_155] — tekst] {0}(이/가) 끝나질 않잖아…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_155].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: There's no end to this {0}...
   PL: To {0} nie ma końca…
403. [Przedmioty, sklep i profil gracza [introduce_word_156] — tekst] 츠바이
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_156].content
   limit: do 120 znaków
   EN: Zwei
   PL: Zwei
404. [Przedmioty, sklep i profil gracza [introduce_sentence_156] — tekst] {0}의 명예가 땅에 떨어지겠네요…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_156].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I guess this mistake will cost {0} its honor...
   PL: Cóż, honor {0} polegnie w błocie…
405. [Przedmioty, sklep i profil gracza [introduce_word_157] — tekst] 시청자
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_157].content
   limit: do 120 znaków
   EN: Viewers
   PL: Widzowie
406. [Przedmioty, sklep i profil gracza [introduce_sentence_157] — tekst] {0} 중에, 이것의 해결법을 아는 자가…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_157].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Is there anyone among my {0}(s) who knows the answer...?
   PL: Czy któryś z moich {0} zna rozwiązanie…?
407. [Przedmioty, sklep i profil gracza [introduce_word_158] — tekst] 안전
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_158].content
   limit: do 120 znaków
   EN: Safety
   PL: Bezpieczeństwo
408. [Przedmioty, sklep i profil gracza [introduce_sentence_158] — tekst] 만인의 {0}(을/를) 바라는 게 잘못된 건 아니라고 생각해요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_158].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I don't think there's anything wrong with wishing {0} for everyone.
   PL: Wszyscy mają prawo pragnąć {0} — to nie wina.
409. [Przedmioty, sklep i profil gracza [introduce_word_159] — tekst] 가면
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_159].content
   limit: do 120 znaków
   EN: Mask
   PL: Maska
410. [Przedmioty, sklep i profil gracza [introduce_sentence_159] — tekst] 내 {0}(이/가) 밤거리를 거니는 걸 보면 피곤한 기분 따위는 싹 날아가지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_159].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Feasting my eyes on my {0}(s) in the night streets does wonders for the fatigue.
   PL: Obserwować, jak moje {0} noca po ulicach — i zmęczenie znikło.
411. [Przedmioty, sklep i profil gracza [introduce_word_160] — tekst] 실력
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_160].content
   limit: do 120 znaków
   EN: Skill
   PL: Kunszt
412. [Przedmioty, sklep i profil gracza [introduce_sentence_160] — tekst] {0} 없으면 따라오지 마세요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_160].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Don't bother coming along if you don't have the {0}(s).
   PL: Kto nie ma {0} — niech zostaje.
413. [Przedmioty, sklep i profil gracza [introduce_word_161] — tekst] 사과
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_161].content
   limit: do 120 znaków
   EN: Apple
   PL: Jabłko
414. [Przedmioty, sklep i profil gracza [introduce_sentence_161] — tekst] {0}(은/는) 어디에 숨겼지?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_161].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Where did you hide (the) {0}?!
   PL: No gdzie schowałeś {0}?!
415. [Przedmioty, sklep i profil gracza [introduce_word_162] — tekst] 주제
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_162].content
   limit: do 120 znaków
   EN: Place
   PL: Miejsce
416. [Przedmioty, sklep i profil gracza [introduce_sentence_162] — tekst] {0}도 모르고 도망치면… 이렇게 되는 거죠.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_162].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This is what happens when you don't know your {0}... and run away.
   PL: Tak kończy ten, kto ucieka, nie znając swojego {0}.
417. [Przedmioty, sklep i profil gracza [introduce_word_163] — tekst] 목마름
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_163].content
   limit: do 120 znaków
   EN: Thirst
   PL: Pragnienie
418. [Przedmioty, sklep i profil gracza [introduce_sentence_163] — tekst] 우리의 {0}(을/를) 너희는 몰라!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_163].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You do not know of our {0}!
   PL: Nasze {0} jest wam obce!
419. [Przedmioty, sklep i profil gracza [introduce_word_164] — tekst] 피
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_164].content
   limit: do 120 znaków
   EN: Blood
   PL: Krew
420. [Przedmioty, sklep i profil gracza [introduce_sentence_164] — tekst] {0}(으로/로)부터 피어올라라.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_164].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blossom from (the) {0}.
   PL: Rozkwitaj z tego, co daje {0}.
421. [Przedmioty, sklep i profil gracza [introduce_word_165] — tekst] 테디
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_165].content
   limit: do 120 znaków
   EN: Teddy
   PL: Teddy
422. [Przedmioty, sklep i profil gracza [introduce_sentence_165] — tekst] 자, {0}~ 나를 따라 해보는 거야! 짜잔!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_165].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Now, little {0}~ Dance after me! Ta-da!
   PL: No więc, {0}~ Powtarzaj po mnie! Tadaa!
423. [Przedmioty, sklep i profil gracza [introduce_word_166] — tekst] 저주
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_166].content
   limit: do 120 znaków
   EN: Curse
   PL: Klątwa
424. [Przedmioty, sklep i profil gracza [introduce_sentence_166] — tekst] 누군가에게 {0}받는 기분이 어떤 것인지…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_166].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Feel what it's like to have someone {0} you.
   PL: Czuj, co znaczy {0} spadające na kark.
425. [Przedmioty, sklep i profil gracza [introduce_word_167] — tekst] 혈액바
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_167].content
   limit: do 120 znaków
   EN: Hemobar
   PL: Hemobar
426. [Przedmioty, sklep i profil gracza [introduce_sentence_167] — tekst] {0}(이/가) 위대하다고 믿어 의심치 않던 시절도 있었지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_167].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: There once was a time when I believed in the greatness of {0}(s).
   PL: Były czasy, gdy {0} uważałem za wielkie.
427. [Przedmioty, sklep i profil gracza [introduce_word_168] — tekst] 퍼레이드
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_168].content
   limit: do 120 znaków
   EN: Parade
   PL: Parada
428. [Przedmioty, sklep i profil gracza [introduce_sentence_168] — tekst] 끝없는 {0}(을/를), 함께 해주시겠나요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_168].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Will you join us in this... eternal {0}?
   PL: Czy przyłączycie się do tego… wiecznego {0}?
429. [Przedmioty, sklep i profil gracza [introduce_word_169] — tekst] 흉탄
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_169].content
   limit: do 120 znaków
   EN: Fell Bullet
   PL: Złowroga Kula
430. [Przedmioty, sklep i profil gracza [introduce_sentence_169] — tekst] 흉악한 {0}(이/가) 저들을 관통하리라…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_169].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let this accursed {0} pierce through them...!
   PL: Oto {0} — niech przebije ich na wskroś…!
431. [Przedmioty, sklep i profil gracza [introduce_word_170] — tekst] 심부름
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_170].content
   limit: do 120 znaków
   EN: Errand
   PL: Zlecenie
432. [Przedmioty, sklep i profil gracza [introduce_sentence_170] — tekst] …다음엔 이런 {0}(은/는) 안 해드릴 거예요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_170].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ... I'm not doing (a/an) {0} like this for you again.
   PL: …Nie powtórzy się takie {0}.
433. [Przedmioty, sklep i profil gracza [introduce_word_171] — tekst] 균형
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_171].content
   limit: do 120 znaków
   EN: Balance
   PL: Równowaga
434. [Przedmioty, sklep i profil gracza [introduce_sentence_171] — tekst] {0}(을/를) 잃은 게 아냐.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_171].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I ain't off {0}.
   PL: {0} dalej przy mnie — spokojnie.
435. [Przedmioty, sklep i profil gracza [introduce_word_172] — tekst] 꿈
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_172].content
   limit: do 120 znaków
   EN: Dream
   PL: Sen
436. [Przedmioty, sklep i profil gracza [introduce_sentence_172] — tekst] 그 허황되고 유치한 {0}(은/는) 즐거우셨습니까.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_172].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Was it sweet, your hollow, juvenile {0}?
   PL: Czy słodki był twój pusty, dziecienny {0}?
437. [Przedmioty, sklep i profil gracza [introduce_word_173] — tekst] 호기심
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_173].content
   limit: do 120 znaków
   EN: Curiosity
   PL: Ciekawość
438. [Przedmioty, sklep i profil gracza [introduce_sentence_173] — tekst] {0}(은/는) 나쁜 거야…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_173].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} is a dangerous thing, you know...
   PL: {0} — to niebezpieczna rzecz…
439. [Przedmioty, sklep i profil gracza [introduce_word_174] — tekst] 괴물
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_174].content
   limit: do 120 znaków
   EN: Monster
   PL: Potwór
440. [Przedmioty, sklep i profil gracza [introduce_sentence_174] — tekst] 어두운 침대 밑에는… {0}(이/가) 살고 있지!!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_174].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: In the shadow beneath your bed lies... (a) {0}!!
   PL: Pod łóżkiem, w cieniu… mieszka {0}!!
441. [Przedmioty, sklep i profil gracza [introduce_word_175] — tekst] 마침표
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_175].content
   limit: do 120 znaków
   EN: Full-Stop
   PL: Kropka
442. [Przedmioty, sklep i profil gracza [introduce_sentence_175] — tekst] 그 삶에… {0}(을/를).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_175].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: A {0}... to your life.
   PL: Do twego życia… {0}.
443. [Przedmioty, sklep i profil gracza [introduce_word_176] — tekst] 저격
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_176].content
   limit: do 120 znaków
   EN: Snipe
   PL: Snajperstwo
444. [Przedmioty, sklep i profil gracza [introduce_sentence_176] — tekst] 좋아, {0} 준비 끝.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_176].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Right, then. Ready to {0}.
   PL: Dobrze, {0} — gotowe.
445. [Przedmioty, sklep i profil gracza [introduce_word_177] — tekst] 마법의 탄환
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_177].content
   limit: do 120 znaków
   EN: Magic Bullet
   PL: Magiczna Kula
446. [Przedmioty, sklep i profil gracza [introduce_sentence_177] — tekst] 역시 네놈 말대로 어떤 사람이라도 맞출 수 있는 {0}(이로/로)군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_177].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: It really is as you say; this is a {0} that will never miss.
   PL: Mówiłeś prawdę: {0} zawsze trafia.
447. [Przedmioty, sklep i profil gracza [introduce_word_178] — tekst] 함정
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_178].content
   limit: do 120 znaków
   EN: Trap
   PL: Pułapka
448. [Przedmioty, sklep i profil gracza [introduce_sentence_178] — tekst] 아. 이번엔 {0}(이/가) 아니라, 진짜요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_178].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ah, worry not, for there is no {0} waiting for you this time.
   PL: Tym razem żadnego {0} — spokojnie.
449. [Przedmioty, sklep i profil gracza [introduce_word_179] — tekst] 불빛
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_179].content
   limit: do 120 znaków
   EN: Flicker of Flame
   PL: Łuna Ognia
450. [Przedmioty, sklep i profil gracza [introduce_sentence_179] — tekst] 마치, {0}에 홀려 모여든 나방떼처럼.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_179].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Like moths drawn to (a) {0}.
   PL: Jak ćmy, które zwabiło {0}.
451. [Przedmioty, sklep i profil gracza [introduce_word_180] — tekst] 원망
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_180].content
   limit: do 120 znaków
   EN: Resentment
   PL: Tęsknota
452. [Przedmioty, sklep i profil gracza [introduce_sentence_180] — tekst] {0}도 뉘우침도 소용이 없었으니.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_180].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}, penance... all of it, to no avail.
   PL: {0} i pokuta — wszystko na próżno.
453. [Przedmioty, sklep i profil gracza [introduce_word_181] — tekst] 식구
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_181].content
   limit: do 120 znaków
   EN: Clan
   PL: Rodzina
454. [Przedmioty, sklep i profil gracza [introduce_sentence_181] — tekst] 우리 {0}(을/를) 건드렸겠다?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_181].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Oh, you don't mess with our {0} and just walk away.
   PL: Z kimś, kto ruszył nasze {0}, tak się nie kończy.
455. [Przedmioty, sklep i profil gracza [introduce_word_182] — tekst] 결전
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_182].content
   limit: do 120 znaków
   EN: Showdown
   PL: Pojedynek
456. [Przedmioty, sklep i profil gracza [introduce_sentence_182] — tekst] 당신의 {0} 신청, 받아들이죠.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_182].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I accept your {0} challenge.
   PL: Przyjmuję twój wniosek: {0}.
457. [Przedmioty, sklep i profil gracza [introduce_word_183] — tekst] 잔불
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_183].content
   limit: do 120 znaków
   EN: Embers
   PL: Żar
458. [Przedmioty, sklep i profil gracza [introduce_sentence_183] — tekst] 아, {0}에 주의하시오.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_183].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ah, be wary of (the) {0}.
   PL: Ach, ostrożnie — {0}.
459. [Przedmioty, sklep i profil gracza [introduce_word_184] — tekst] 숨통
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_184].content
   limit: do 120 znaków
   EN: Breathe
   PL: Tchnienie
460. [Przedmioty, sklep i profil gracza [introduce_sentence_184] — tekst] 처음으로 {0}(이/가) 트였던 순간을 기억하나요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_184].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Do you recall the moment when you could {0} free for the first time?
   PL: Pamiętasz moment, gdy {0} po raz pierwszy się uwolniło?
461. [Przedmioty, sklep i profil gracza [introduce_word_185] — tekst] 고수
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_185].content
   limit: do 120 znaków
   EN: Hidden Dragon
   PL: Ukryty Smok
462. [Przedmioty, sklep i profil gracza [introduce_sentence_185] — tekst] 이 넓은 식당 안에 하나쯤은… {0}(이/가) 섞여 있기 마련 아니겠나?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_185].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thou should have expected to find... (a/an) {0} amongst the patrons, hm?
   PL: W tak szerokiej jadłodajni… {0} na pewno się znajdzie, hm?
463. [Przedmioty, sklep i profil gracza [introduce_word_186] — tekst] 불주먹 사무소
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_186].content
   limit: do 120 znaków
   EN: Firefist Office
   PL: Biuro Ognistej Pięści
464. [Przedmioty, sklep i profil gracza [introduce_sentence_186] — tekst] 이건… 우리 {0}의 복장이군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_186].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: They're... all from our {0}.
   PL: To… stroje naszego {0}.
465. [Przedmioty, sklep i profil gracza [introduce_word_187] — tekst] 토끼
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_187].content
   limit: do 120 znaków
   EN: Hares
   PL: Zające
466. [Przedmioty, sklep i profil gracza [introduce_sentence_187] — tekst] 몰랐나? {0}(은/는) 원래 야행성이다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_187].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Didn't you know? {0} (is/are) nocturnal.
   PL: Nie wiedziałeś? {0} żyje nocą.
467. [Przedmioty, sklep i profil gracza [introduce_word_188] — tekst] 주군
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_188].content
   limit: do 120 znaków
   EN: My Lord
   PL: Mój Panie
468. [Przedmioty, sklep i profil gracza [introduce_sentence_188] — tekst] 주군께선 {0}의 집무에 충실하소서.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_188].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Focus on your business of the day, {0}.
   PL: Panie, proszę o wierność obowiązkom: {0}.
469. [Przedmioty, sklep i profil gracza [introduce_word_189] — tekst] 장부
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_189].content
   limit: do 120 znaków
   EN: Book
   PL: Księga
470. [Przedmioty, sklep i profil gracza [introduce_sentence_189] — tekst] 내가 죽어도… 넌 {0}에 남는다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_189].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Killing me won't clear your name off (the) {0}.
   PL: Zabij mnie — i tak imię twoje zostanie w {0}.
471. [Przedmioty, sklep i profil gracza [introduce_word_190] — tekst] 뼛조각
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_190].content
   limit: do 120 znaków
   EN: Bones
   PL: Kości
472. [Przedmioty, sklep i profil gracza [introduce_sentence_190] — tekst] 매달고, 불태우거라. 끝끝내 {0} 하나 남지 않도록.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_190].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hang them, burn them. Reduce their {0} to cinders.
   PL: Powiesić, spalić. Zero {0} na koniec.
473. [Przedmioty, sklep i profil gracza [introduce_word_191] — tekst] 순록
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_191].content
   limit: do 120 znaków
   EN: Reindeer
   PL: Renifer
474. [Przedmioty, sklep i profil gracza [introduce_sentence_191] — tekst] 하… 이번엔 {0}(이/가) 가장 먼저 투입되는 건가?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_191].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Haah... They're sending in (the) {0} herd first?
   PL: Ha… najpierw ruszają {0}?
475. [Przedmioty, sklep i profil gracza [introduce_word_192] — tekst] 도구
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_192].content
   limit: do 120 znaków
   EN: Tool
   PL: Narzędzie
476. [Przedmioty, sklep i profil gracza [introduce_sentence_192] — tekst] 낯선 {0}에 원한을 품는 건, 이상하잖아?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_192].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: It'd be weird to take revenge on a {0}, right?
   PL: Mścić się na {0} — dziwactwo, nie?
477. [Przedmioty, sklep i profil gracza [introduce_word_193] — tekst] 짐승
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_193].content
   limit: do 120 znaków
   EN: Animal
   PL: Bestia
478. [Przedmioty, sklep i profil gracza [introduce_sentence_193] — tekst] 이걸로 팔십… 조금만 더 채우면 {0}(으로/로) 사는 것도 끝일 거야.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_193].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: That makes it eighty missions... Just a few more, and I won't have to live like some {0} anymore.
   PL: To już osiemdziesiąt… kilka jeszcze, i {0} przestanie być moim losem.
479. [Przedmioty, sklep i profil gracza [introduce_word_194] — tekst] 배움
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_194].content
   limit: do 120 znaków
   EN: Learning
   PL: Nauka
480. [Przedmioty, sklep i profil gracza [introduce_sentence_194] — tekst] {0}(을/를) 위해서라면, 다소의 꺼려짐도 감수해야 하는 일이겠죠.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_194].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Yet, one must face their disinclinations for the pursuit of {0}.
   PL: {0} kosztuje — trzeba znieść trochę niechęci.
481. [Przedmioty, sklep i profil gracza [introduce_word_195] — tekst] 소원
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_195].content
   limit: do 120 znaków
   EN: Wish
   PL: Życzenie
482. [Przedmioty, sklep i profil gracza [introduce_sentence_195] — tekst] 후훗! 이 수많은 {0}들 중… 그대가 이루고 싶은 {0}(은/는) 무엇인가!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_195].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Heheh! Thou art quite full of {0}(es)... Which of them dost thou desire to see come true?!
   PL: Heheh! Mnóstwo tu {0}… Które chcecie spełnić?!
483. [Przedmioty, sklep i profil gracza [introduce_word_196] — tekst] 의심
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_196].content
   limit: do 120 znaków
   EN: Doubt
   PL: Zwątpienie
484. [Przedmioty, sklep i profil gracza [introduce_sentence_196] — tekst] {0} 끊고. 믿음 새겨. 그저 맹목적으로… 기도해.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_196].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No {0}. Engrave faith. Pray in darkness... Pray with obsession.
   PL: Odpuść {0}. Wyryj wiarę. Módl się ślepo… i obsesyjnie.
485. [Przedmioty, sklep i profil gracza [introduce_word_197] — tekst] 형벌
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_197].content
   limit: do 120 znaków
   EN: Retribution
   PL: Odweta
486. [Przedmioty, sklep i profil gracza [introduce_sentence_197] — tekst] 눈을 감고, 하늘께서 명하신 {0}(을/를).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_197].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Shut your eyes, now. Accept the {0} of the heavens.
   PL: Oczy zamknąć — niebiańskie {0} przyjąć.
487. [Przedmioty, sklep i profil gracza [introduce_word_198] — tekst] 하늘
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_198].content
   limit: do 120 znaków
   EN: Sky(ies)
   PL: Niebo
488. [Przedmioty, sklep i profil gracza [introduce_sentence_198] — tekst] 더럽혀진 몸은 오를 {0}조차 없다시니…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_198].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This tarnished, filthy body has no {0} to rise to…
   PL: Ciało splamione — {0} dla niego nie istnieje…
489. [Przedmioty, sklep i profil gracza [introduce_word_199] — tekst] 봄
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_199].content
   limit: do 120 znaków
   EN: Spring
   PL: Wiosna
490. [Przedmioty, sklep i profil gracza [introduce_sentence_199] — tekst] {0} 한 번… 짧기도 하지…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_199].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: What a... short-lived {0} this is...
   PL: Oto {0}… takie krótkie…
491. [Przedmioty, sklep i profil gracza [introduce_word_200] — tekst] 목
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_200].content
   limit: do 120 znaków
   EN: Head
   PL: Głowa
492. [Przedmioty, sklep i profil gracza [introduce_sentence_200] — tekst] 그렇게 서 있으면, {0}(이/가) 떨어질 수 밖에.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_200].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Standing around as you did is what cost you your {0}.
   PL: Tak stojąc, {0} i tak spadnie.
493. [Przedmioty, sklep i profil gracza [introduce_word_201] — tekst] 엄지
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_201].content
   limit: do 120 znaków
   EN: The Thumb
   PL: Kciuk
494. [Przedmioty, sklep i profil gracza [introduce_sentence_201] — tekst] 제가 동부의 {0}(이라서/라서) 다행이라고 생각해요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_201].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: These are the moments when I feel so lucky to be a part of {0} in the east.
   PL: Szczęście, że jestem częścią {0} ze wschodu.
495. [Przedmioty, sklep i profil gracza [introduce_word_202] — tekst] 전율
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_202].content
   limit: do 120 znaków
   EN: Frisson
   PL: Dreszczyk
496. [Przedmioty, sklep i profil gracza [introduce_sentence_202] — tekst] 저들은 {0}하리라.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_202].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: They will shiver with {0}.
   PL: Ich przejmie {0}.
497. [Przedmioty, sklep i profil gracza [introduce_word_203] — tekst] 사랑
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_203].content
   limit: do 120 znaków
   EN: Love
   PL: Miłość
498. [Przedmioty, sklep i profil gracza [introduce_sentence_203] — tekst] {0}(과/와) 정의의 이름으로~ 지금 이 곳에 등장!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_203].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: In the name of {0} and Justice~ Here cometh Magical Maiden!
   PL: W imię {0} i Sprawiedliwości~ Oto nadchodzi Czarodziejska Panienka!
499. [Przedmioty, sklep i profil gracza [introduce_word_204] — tekst] 배신
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_204].content
   limit: do 120 znaków
   EN: Betrayal
   PL: Zdrada
500. [Przedmioty, sklep i profil gracza [introduce_sentence_204] — tekst] 자, 봤지? 난 믿어주면… {0}하지 않아.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_204].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: See? Trust me... and there'll never be {0} from me.
   PL: Widzisz? Zaufaj — i żadnego {0} ode mnie.
501. [Przedmioty, sklep i profil gracza [introduce_word_205] — tekst] 빛
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_205].content
   limit: do 120 znaków
   EN: Light
   PL: Światło
502. [Przedmioty, sklep i profil gracza [introduce_sentence_205] — tekst] 나 여기서 {0}에 맹세한다!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_205].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I shall make this oath to (the) {0}!
   PL: Ślubuję przy tym {0}!
503. [Przedmioty, sklep i profil gracza [introduce_word_206] — tekst] 모자
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_206].content
   limit: do 120 znaków
   EN: Hat
   PL: Kapelusz
504. [Przedmioty, sklep i profil gracza [introduce_sentence_206] — tekst] 이 {0}(은/는) 신분의 표시…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_206].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This {0}'s a status symbol...
   PL: To {0} to znak pozycji…
505. [Przedmioty, sklep i profil gracza [introduce_word_207] — tekst] 증기
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_207].content
   limit: do 120 znaków
   EN: Steam
   PL: Para
506. [Przedmioty, sklep i profil gracza [introduce_sentence_207] — tekst] 압축, 압축. {0} 역류 무시… 무시 불가.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_207].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Compress. Compress. Ignore {0} reflux... cannot ignore.
   PL: Ściskać, ściskać. {0} wraca — ignorować… nie da się.
507. [Przedmioty, sklep i profil gracza [introduce_word_208] — tekst] 홍원
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_208].content
   limit: do 120 znaków
   EN: Hongyuan
   PL: Hongyuan
508. [Przedmioty, sklep i profil gracza [introduce_sentence_208] — tekst] 내가 {0}(을/를) 다스리는 유일한 군주다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_208].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I shall be the sole, absolute lord of {0}.
   PL: Ja — jedyny, absolutny władca {0}.
509. [Przedmioty, sklep i profil gracza [introduce_word_209] — tekst] 말
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_209].content
   limit: do 120 znaków
   EN: Steed
   PL: Wierzchowiec
510. [Przedmioty, sklep i profil gracza [introduce_sentence_209] — tekst] 이것이 {0}의 행진이요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_209].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0} marches forth.
   PL: {0} wyrusza — taki to marsz.
511. [Przedmioty, sklep i profil gracza [introduce_word_210] — tekst] 횃대
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_210].content
   limit: do 120 znaków
   EN: Perch
   PL: Żerdź
512. [Przedmioty, sklep i profil gracza [introduce_sentence_210] — tekst] {0}에서 내려, 전장으로.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_210].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: From the {0} to the battlefield.
   PL: {0} zostaje — ja ruszam na pole bitwy.
513. [Przedmioty, sklep i profil gracza [introduce_word_211] — tekst] 시선
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_211].content
   limit: do 120 znaków
   EN: Gaze
   PL: Spojrzenie
514. [Przedmioty, sklep i profil gracza [introduce_sentence_211] — tekst] 그 {0}… 경멸스럽군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_211].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: That {0}... how contemptuous.
   PL: To {0}… pełne pogardy.
515. [Przedmioty, sklep i profil gracza [introduce_word_212] — tekst] 미래
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_212].content
   limit: do 120 znaków
   EN: Future
   PL: Przyszłość
516. [Przedmioty, sklep i profil gracza [introduce_sentence_212] — tekst] 먼지 위를 걸어, 고독을 쥐고, 아스라이 먼 {0}(으로/로) 나아가라.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_212].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Walk across the dust, grasp the solitude, and forge on toward the faint and far {0}.
   PL: Krocz po kurzu, ściskaj samotność — przed tobą {0}.
517. [Przedmioty, sklep i profil gracza [introduce_word_213] — tekst] 용
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_213].content
   limit: do 120 znaków
   EN: Loong
   PL: Loong
518. [Przedmioty, sklep i profil gracza [introduce_sentence_213] — tekst] 시구의 한 획, {0}(이/가) 되어 빈 벼루에 남았구나.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_213].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: A poem's brushstroke becomes (a/an) {0} atop a dry inkstone.
   PL: Jeden suwnik wiersza: {0} na wyschłym kamieniu do tuszu.
519. [Przedmioty, sklep i profil gracza [introduce_word_214] — tekst] 바다
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_214].content
   limit: do 120 znaków
   EN: Sea
   PL: Morze
520. [Przedmioty, sklep i profil gracza [introduce_sentence_214] — tekst] 뒤엉킨 악몽과 함께 너의 {0}(으로/로)!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_214].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Rise from the long dark, journey with the torturous nightmare to your {0}!
   PL: Koszmarny sen prowadzi cię do twego {0}!
521. [Przedmioty, sklep i profil gracza [introduce_word_215] — tekst] 영광
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_215].content
   limit: do 120 znaków
   EN: Glory
   PL: Chwała
522. [Przedmioty, sklep i profil gracza [introduce_sentence_215] — tekst] 이 검은! 이 명예는! 이 {0}(은/는)! …빛바래지 않을 테니.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_215].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Be assured, this sword, this honor, this {0}…! …Won’t be tarnished.
   PL: Ten miecz! Ten zaszczyt! To {0}! …Nie wyblaknie.
523. [Przedmioty, sklep i profil gracza [introduce_word_216] — tekst] 빗소리
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_216].content
   limit: do 120 znaków
   EN: Pelting Rain
   PL: Deszczowe Bicie
524. [Przedmioty, sklep i profil gracza [introduce_sentence_216] — tekst] {0} 속에 묻히도록.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_216].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let (the) {0} bury you.
   PL: Niech {0} cię pogrzebie.
525. [Przedmioty, sklep i profil gracza [introduce_word_217] — tekst] 가족
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_217].content
   limit: do 120 znaków
   EN: Family
   PL: Rodzina
526. [Przedmioty, sklep i profil gracza [introduce_sentence_217] — tekst] 너는… {0}(이/가) 되기엔 약하군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_217].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You... are too feeble to join (the) {0}.
   PL: Za słaby jesteś, by {0} cię przyjęło.
527. [Przedmioty, sklep i profil gracza [introduce_word_218] — tekst] 일등석
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_218].content
   limit: do 120 znaków
   EN: First Class
   PL: Pierwsza Klasa
528. [Przedmioty, sklep i profil gracza [introduce_sentence_218] — tekst] 까놓고 말해서 {0}(이/가) 돈값 못하는 걸 누가 몰라?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_218].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: There's not a soul up 'ere that thinks {0} is worth the brass.
   PL: Każdy wie: {0} — pieniądze w błoto.
529. [Przedmioty, sklep i profil gracza [introduce_word_219] — tekst] 짝패
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_219].content
   limit: do 120 znaków
   EN: Matching Hand
   PL: Ręka
530. [Przedmioty, sklep i profil gracza [introduce_sentence_219] — tekst] 당신, {0}(이군/군)요!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_219].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hey now, that makes (a/an) {0}!
   PL: No proszę — to {0}!
531. [Przedmioty, sklep i profil gracza [introduce_word_220] — tekst] 운명
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_220].content
   limit: do 120 znaków
   EN: Fate
   PL: Los
532. [Przedmioty, sklep i profil gracza [introduce_sentence_220] — tekst] 도망친다고… 달라질 {0}(은/는) 아니었나…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_220].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I guess running away... did nothing to unseal our {0}...
   PL: No cóż, ucieczka… {0} nie zmieni.
533. [Przedmioty, sklep i profil gracza [introduce_word_221] — tekst] 양 떼
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_221].content
   limit: do 120 znaków
   EN: Pack of Sheep
   PL: Stado Owiec
534. [Przedmioty, sklep i profil gracza [introduce_sentence_221] — tekst] {0}(이/가) 그대들을 가로막는 모든 것들을 박살 내줄 테니!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_221].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0} shall break and shatter all that standeth before ye!
   PL: {0} rozbije wszystko, co wam zagradza drogę!
535. [Przedmioty, sklep i profil gracza [introduce_word_222] — tekst] 모래판
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_222].content
   limit: do 120 znaków
   EN: Sand Circle
   PL: Piaskowe Koło
536. [Przedmioty, sklep i profil gracza [introduce_sentence_222] — tekst] {0}에 모이가 남지 않을 때까지…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_222].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 'Till there's no more feed left on the {0}...!
   PL: Póki na {0} jest jeszcze ziarno…!
537. [Przedmioty, sklep i profil gracza [introduce_word_223] — tekst] 길
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_223].content
   limit: do 120 znaków
   EN: Path
   PL: Droga
538. [Przedmioty, sklep i profil gracza [introduce_sentence_223] — tekst] {0}(이/가) 같으니, 거들어주지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_223].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Our {0}(s) align. I'll lend you a hand.
   PL: Skoro {0} się zgadza — pomogę.
539. [Przedmioty, sklep i profil gracza [introduce_word_224] — tekst] 축복
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_224].content
   limit: do 120 znaków
   EN: Blessing(s)
   PL: Błogosławieństwo
540. [Przedmioty, sklep i profil gracza [introduce_sentence_224] — tekst] 이 은혜로운 밤에 나와서 일하고 있는 너희나, 우리들에게… {0} 같은 게 있기를.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_224].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let there be {0} or whatever to all the poor souls working the holy night away.
   PL: Niech was i nas w tej świętej nocnej harówce dopisze jakieś {0}.
541. [Przedmioty, sklep i profil gracza [introduce_word_225] — tekst] 지령
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_225].content
   limit: do 120 znaków
   EN: Prescript
   PL: Nakaz
542. [Przedmioty, sklep i profil gracza [introduce_sentence_225] — tekst] {0}(은/는) 수행되었습니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_225].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (The) {0} has been fulfilled.
   PL: {0} — wykonano.
543. [Przedmioty, sklep i profil gracza [introduce_word_226] — tekst] 우제트
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_226].content
   limit: do 120 znaków
   EN: Udjat
   PL: Udżat
544. [Przedmioty, sklep i profil gracza [introduce_sentence_226] — tekst] 전술 시야 전개. {0}의 눈으로.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_226].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Activating tactical vision. The {0} Eye.
   PL: Pole widzenia taktycznego. Oko — {0}.
545. [Przedmioty, sklep i profil gracza [introduce_word_227] — tekst] 삐삐님
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_227].content
   limit: do 120 znaków
   EN: Beeper
   PL: Beeper
546. [Przedmioty, sklep i profil gracza [introduce_sentence_227] — tekst] 이것 또한 마법의 {0}(이/가) 속삭여준 지령의 뜻.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_227].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 'Twas but the Will of the Prescript, whispered by the Great Magicked {0}.
   PL: Oto wola Nakazu — to wielkie magiczne {0} jej strzegło.
547. [Przedmioty, sklep i profil gracza [introduce_word_228] — tekst] 기념품
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_228].content
   limit: do 120 znaków
   EN: Tour Souvenir
   PL: Pamiątka z Wycieczki
548. [Przedmioty, sklep i profil gracza [introduce_sentence_228] — tekst] 잠깐, 정지. 너… {0}(을/를) 두고 갔잖아?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_228].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Easy—halt. You've... gone and left the {0} behind, haven't you?
   PL: Chwilka, stop. A {0}? Zostało, hm?
549. [Przedmioty, sklep i profil gracza [introduce_word_229] — tekst] 가위
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_229].content
   limit: do 120 znaków
   EN: Scissor(s)
   PL: Nożyczki
550. [Przedmioty, sklep i profil gracza [introduce_sentence_229] — tekst] {0}(은/는) 주먹을 이겨.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_229].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} beat(s) rock.
   PL: {0} bije kamień.
551. [Przedmioty, sklep i profil gracza [introduce_word_230] — tekst] 역사
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_230].content
   limit: do 120 znaków
   EN: History(ies)
   PL: Historia
552. [Przedmioty, sklep i profil gracza [introduce_sentence_230] — tekst] 가루된 나의 {0}(은/는) 기어이! 흩어져 소멸… 하리라.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_230].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The {0} of myself, ground into dust, shall, at last, scatter... and meet annihilation.
   PL: Zmielone w pył — {0} moje zginie w rozproszeniu…
553. [Przedmioty, sklep i profil gracza [introduce_word_231] — tekst] 삼천대세계
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_231].content
   limit: do 120 znaków
   EN: Sanzendaisekai
   PL: Wielki Trichiliokosm
554. [Przedmioty, sklep i profil gracza [introduce_sentence_231] — tekst] {0}.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_231].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}.
   PL: {0}.
555. [Przedmioty, sklep i profil gracza [introduce_word_232] — tekst] 사인
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_232].content
   limit: do 120 znaków
   EN: (an) autograph(s)
   PL: Autograf
556. [Przedmioty, sklep i profil gracza [introduce_sentence_232] — tekst] 아. 죽이기 전에 {0}도 받아뒀어야 했는데…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_232].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ugh. I really should've gotten {0} before I kicked his ass into the afterlife.
   PL: Ech. Powinienem był wziąć {0}, zanim wywaliłem go w zaświaty…
557. [Przedmioty, sklep i profil gracza [introduce_word_233] — tekst] 월하청도
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_233].content
   limit: do 120 znaków
   EN: Moonlit Azure Blade
   PL: Błękitne Ostrze w Blasku Księżyca
558. [Przedmioty, sklep i profil gracza [introduce_sentence_233] — tekst] 사사받은 {0}(이/가) 부끄럽지 않을 수 있도록, 이 기회를 소중히…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_233].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I shall treasure this chance, so as not to cast shame upon (the) {0} my master has imparted unto me.
   PL: Cenić tę szansę, by {0} przekazane przez mistrza nie zawstydziło.
559. [Przedmioty, sklep i profil gracza [introduce_word_234] — tekst] 괴수
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_234].content
   limit: do 120 znaków
   EN: Beast
   PL: Wielka Bestia
560. [Przedmioty, sklep i profil gracza [introduce_sentence_234] — tekst] 당신이… 이 숲의 {0}(이로/로)군.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_234].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: It's you... You are (the) {0} of this forest.
   PL: To ty… {0} tego lasu — ty.
561. [Przedmioty, sklep i profil gracza [introduce_word_235] — tekst] 동화책
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_235].content
   limit: do 120 znaków
   EN: Storybook
   PL: Bajka
562. [Przedmioty, sklep i profil gracza [introduce_sentence_235] — tekst] 이번에 읽어줄 {0}(은/는) 이것으로.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_235].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thus it is decided, (the) {0} for today's reading.
   PL: Dziś na lekturę — {0}.
563. [Przedmioty, sklep i profil gracza [introduce_word_236] — tekst] 공허
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_236].content
   limit: do 120 znaków
   EN: Void
   PL: Pustka
564. [Przedmioty, sklep i profil gracza [introduce_sentence_236] — tekst] 채워지지 않을 {0}(을/를) 남겨주지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_236].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I'll fire into you (a/an) {0} that cannot be filled.
   PL: Zostawię w tobie {0} — niewypełnialne.
565. [Przedmioty, sklep i profil gracza [introduce_word_237] — tekst] 군락
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_237].content
   limit: do 120 znaków
   EN: Colony
   PL: Kolonia
566. [Przedmioty, sklep i profil gracza [introduce_sentence_237] — tekst] 큭… {0}의 방어를 목표로.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_237].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Nngh... Defend (the) {0}.
   PL: Nngh… obrona: {0}.
567. [Przedmioty, sklep i profil gracza [introduce_word_238] — tekst] 하모니
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_238].content
   limit: do 120 znaków
   EN: Harmony
   PL: Harmonia
568. [Przedmioty, sklep i profil gracza [introduce_sentence_238] — tekst] 최상의… {0}(이야/야).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_238].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Such wondrous... {0}.
   PL: Coś nadzwyczajnego… {0}.
569. [Przedmioty, sklep i profil gracza [introduce_word_239] — tekst] 시험
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_239].content
   limit: do 120 znaków
   EN: Test and Trial
   PL: Egzamin
570. [Przedmioty, sklep i profil gracza [introduce_sentence_239] — tekst] 어디, {0}해보지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_239].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Let us run (a/an) {0}.
   PL: No to — {0}.
571. [Przedmioty, sklep i profil gracza [introduce_word_240] — tekst] 일렁임
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_240].content
   limit: do 120 znaków
   EN: Blazing Haze
   PL: Falująca Łuna
572. [Przedmioty, sklep i profil gracza [introduce_sentence_240] — tekst] {0}에 닿을 때까지, 몇 번이고…!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_240].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Once more and yet again, until we touch (the) {0}...!
   PL: Jeszcze raz — {0} tuż-tuż!
573. [Przedmioty, sklep i profil gracza [introduce_word_241] — tekst] 감상
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_241].content
   limit: do 120 znaków
   EN: Impression(s)
   PL: Wrażenia
574. [Przedmioty, sklep i profil gracza [introduce_sentence_241] — tekst] {0}(은/는) 어떤가요!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_241].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Please, do share your {0}!
   PL: No i co powiecie? {0}!
575. [Przedmioty, sklep i profil gracza [introduce_word_242] — tekst] 파시아
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_242].content
   limit: do 120 znaków
   EN: Fascia
   PL: Powięź
576. [Przedmioty, sklep i profil gracza [introduce_sentence_242] — tekst] 두려우신가요, {0}?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_242].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Are you afraid, {0}?
   PL: Boisz się, {0}?
577. [Przedmioty, sklep i profil gracza [introduce_word_243] — tekst] 심사
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_243].content
   limit: do 120 znaków
   EN: Evaluation
   PL: Ocena
578. [Przedmioty, sklep i profil gracza [introduce_sentence_243] — tekst] 엄중한 {0}, 부탁드립니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_243].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Requesting your most rigorous {0}.
   PL: Proszę o surowość: {0}.
579. [Przedmioty, sklep i profil gracza [introduce_word_244] — tekst] 색채
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_244].content
   limit: do 120 znaków
   EN: Palette of Colors
   PL: Paleta Barw
580. [Przedmioty, sklep i profil gracza [introduce_sentence_244] — tekst] 어디에서도 볼 수 없을 {0}(으로/로).
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_244].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: With (a/an) {0} out of this world.
   PL: A {0} — jakiej świat nie widział!
581. [Przedmioty, sklep i profil gracza [introduce_word_245] — tekst] 푹신
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_245].content
   limit: do 120 znaków
   EN: Luscious
   PL: Puszysto
