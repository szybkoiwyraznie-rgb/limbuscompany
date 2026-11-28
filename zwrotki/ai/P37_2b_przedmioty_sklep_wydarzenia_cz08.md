# Paczka AI P37 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 8/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P37_2b_przedmioty_sklep_wydarzenia_cz08.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P37_2b_przedmioty_sklep_wydarzenia_cz08.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Przedmioty, sklep i profil gracza: IntroductionPreset
- plik gry: `IntroductionPreset.json`

1. [Przedmioty, sklep i profil gracza [introduce_sentence_245] — tekst] 흠… 어때, 훨씬 {0}해 보이지?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_245].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hmm... What d'you reckon? Looks more {0} now, don't it?
   PL: Hm… No i jak? Teraz to wygląda dużo bardziej {0}, nie?
2. [Przedmioty, sklep i profil gracza [introduce_word_246] — tekst] 야단
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_246].content
   limit: do 120 znaków
   EN: Itching
   PL: Zapale
3. [Przedmioty, sklep i profil gracza [introduce_sentence_246] — tekst] 이것 봐, 이 아이들이 너를 따라가고 싶어서… 이렇게 {0}이잖아.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_246].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Look! These little ones are {0} to tag along with you.
   PL: Spójrz! Te małe są w wielkim {0}, by pójść z tobą!
4. [Przedmioty, sklep i profil gracza [introduce_word_247] — tekst] 거미줄
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_247].content
   limit: do 120 znaków
   EN: Spider's Thread
   PL: Pajęcza Nić
5. [Przedmioty, sklep i profil gracza [introduce_sentence_247] — tekst] 자유로워질 수 없어. 이 {0}(을/를) 끊어내지 않고서는…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_247].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I cannot be free from here. Not without severing (the) {0}...
   PL: Nie mogę się stąd uwolnić. Nie bez odcięcia tej {0}…
6. [Przedmioty, sklep i profil gracza [introduce_word_248] — tekst] 전설의 검
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_248].content
   limit: do 120 znaków
   EN: Sword of Legends
   PL: Miecz Legend
7. [Przedmioty, sklep i profil gracza [introduce_sentence_248] — tekst] 의심 좀 받으면 어때? 이 {0}(이/가)… 내 손에 들어왔는데.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_248].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: What's a couple of pointed fingers when {0} (is/are)... resting all snug and sweet in my hands?
   PL: Niewiele znaczą te oskarżenia, skoro to {0}… już spoczywa w mych dłoniach.
8. [Przedmioty, sklep i profil gracza [introduce_word_249] — tekst] 검계
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_249].content
   limit: do 120 znaków
   EN: Blade Lineage
   PL: Ród Ostrza
9. [Przedmioty, sklep i profil gracza [introduce_sentence_249] — tekst] 그러니… 지금 {0}(이라는/라는) 이름을 마땅히 댈 수 있는 자는 저 하나 뿐이겠네요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_249].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Only I alone... remain unashamed to use the name "{0}."
   PL: Tylko ja jeden… godzien bez wstydu użyć imienia "{0}".
10. [Przedmioty, sklep i profil gracza [introduce_word_250] — tekst] 노비
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_250].content
   limit: do 120 znaków
   EN: Nobi
   PL: Nobi
11. [Przedmioty, sklep i profil gracza [introduce_sentence_250] — tekst] 저를 부르셨다는 건… 아하, {0}(이/가) 도망쳤군요?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_250].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If you've called for me... Aha. A runaway {0} to hunt, yes?
   PL: Skoro mnie wezwano… Aha. Zbiegłe {0} do złapania, tak?
12. [Przedmioty, sklep i profil gracza [introduce_word_251] — tekst] 그늘
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_251].content
   limit: do 120 znaków
   EN: Shade
   PL: Cień
13. [Przedmioty, sklep i profil gracza [introduce_sentence_251] — tekst] …그림자 없는 햇살은 없으니, 이 {0} 또한 기꺼이 받아낼 뿐.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_251].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ... No sun has ever risen without a shadow cast. So this {0}, too, shall I accept.
   PL: …Żadne słońce nie wschodzi bez rzuconego cienia. Przyjmę więc i ten {0}.
14. [Przedmioty, sklep i profil gracza [introduce_word_252] — tekst] 팔레르모
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_252].content
   limit: do 120 znaków
   EN: Palermitan Style
   PL: Styl Palermo
15. [Przedmioty, sklep i profil gracza [introduce_sentence_252] — tekst] 일대일 결투에선, {0}(을/를) 익힌 제가 유리합니다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_252].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: In one-on-one duels, my {0} has the advantage.
   PL: W pojedynku jeden na jeden moje {0} daje przewagę.
16. [Przedmioty, sklep i profil gracza [introduce_word_253] — tekst] 전쟁
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_253].content
   limit: do 120 znaków
   EN: War
   PL: Wojna
17. [Przedmioty, sklep i profil gracza [introduce_sentence_253] — tekst] 걸리적거리니까, 비켜. 쯧. 이래서 {0}도 안 겪어본 것들은…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_253].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Fall back—you're gettin' in the way. Tsk. I just can't with greenhorns who haven't had a taste of (the) {0}...
   PL: Odsuwaj się, bo zawadzasz. Cóż. Takich, co {0} nie kosztowali…
18. [Przedmioty, sklep i profil gracza [introduce_word_254] — tekst] 홈 파티
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_254].content
   limit: do 120 znaków
   EN: House Party
   PL: Impreza Domowa
19. [Przedmioty, sklep i profil gracza [introduce_sentence_254] — tekst] {0}(은/는) 못 하게 되겠군요.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_254].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (The) {0}... will have to be canceled.
   PL: {0} nie dojdzie do skutku.
20. [Przedmioty, sklep i profil gracza [introduce_word_255] — tekst] 쌍화차
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_255].content
   limit: do 120 znaków
   EN: Ssanghwa-cha
   PL: Ssanghwa-cha
21. [Przedmioty, sklep i profil gracza [introduce_sentence_255] — tekst] 나 때는… 이렇게 향긋한 {0} 냄새는 꿈도 꾸질 못했지.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_255].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: During those days... The luxury of {0} this fragrant was beyond anything I could imagine.
   PL: Za moich czasów… o tak pachnącym {0} śnić nie mogłem.
22. [Przedmioty, sklep i profil gracza [introduce_word_256] — tekst] 부고
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_256].content
   limit: do 120 znaków
   EN: Obituary
   PL: Nekrolog
23. [Przedmioty, sklep i profil gracza [introduce_sentence_256] — tekst] {0}(을/를) 전하겠소.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_256].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: I come bearing (a/an) {0}.
   PL: Niosę ci {0}.
24. [Przedmioty, sklep i profil gracza [introduce_word_257] — tekst] 행선지
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_257].content
   limit: do 120 znaków
   EN: Destination
   PL: Kierunek
25. [Przedmioty, sklep i profil gracza [introduce_sentence_257] — tekst] {0}(은/는) 정해졌소.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_257].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (The) {0} (has/have) been determined.
   PL: {0} — wyznaczony.
26. [Przedmioty, sklep i profil gracza [introduce_word_258] — tekst] 친구
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_258].content
   limit: do 120 znaków
   EN: Friend
   PL: Przyjaciel
27. [Przedmioty, sklep i profil gracza [introduce_sentence_258] — tekst] {0}(이다/다)! {0}(이/가) 왔어!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_258].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (A/An) {0}! (A/An) {0} is here!
   PL: {0}! Przyszedł {0}!
28. [Przedmioty, sklep i profil gracza [introduce_word_259] — tekst] 의뢰
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_259].content
   limit: do 120 znaków
   EN: Commission(s)
   PL: Zlecenie
29. [Przedmioty, sklep i profil gracza [introduce_sentence_259] — tekst] {0}의 초과 예약은 금지되어 있어서요~
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_259].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Oh, sorry. We're prohibited from overbooking {0}~
   PL: Ach, przepraszam. Nie wolno nam przyjmować {0} ponad stan~
30. [Przedmioty, sklep i profil gracza [introduce_word_260] — tekst] 포획
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_260].content
   limit: do 120 znaków
   EN: Capture
   PL: Pojmanie
31. [Przedmioty, sklep i profil gracza [introduce_sentence_260] — tekst] {0} 절차를 계속, 계속! 계속 수행해!!!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_260].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Protocol.... CONTINUE, CONTINUE! CONTINUE PROTOCOL EXECUTION!!
   PL: Procedura {0}… kontynuować, kontynuować! KONTYNUOWAĆ PROCEDURĘ!!
32. [Przedmioty, sklep i profil gracza [introduce_word_261] — tekst] 르누아르
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_261].content
   limit: do 120 znaków
   EN: Le Noir
   PL: Le Noir
33. [Przedmioty, sklep i profil gracza [introduce_sentence_261] — tekst] {0}의 미학은 절제에서 시작된다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_261].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The aesthetics of {0} are rooted in temperance.
   PL: Estetyka {0} rodzi się z umiaru.
34. [Przedmioty, sklep i profil gracza [introduce_word_262] — tekst] 르루주
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_262].content
   limit: do 120 znaków
   EN: Le Rouge
   PL: Le Rouge
35. [Przedmioty, sklep i profil gracza [introduce_sentence_262] — tekst] 더 많은 고객들이 {0}의 패션에 열광하도록!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_262].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: We'll have even more customers clamoring for the fashion only {0} can offer!
   PL: Niech jeszcze więcej klientów rozkocha się w modzie {0}!
36. [Przedmioty, sklep i profil gracza [introduce_word_263] — tekst] 원단
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_263].content
   limit: do 120 znaków
   EN: Fabric
   PL: Materiał
37. [Przedmioty, sklep i profil gracza [introduce_sentence_263] — tekst] 수준 높은 {0}(을/를) 원한다면 기다림의 시간을 가져야 할 거야.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_263].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If you're after quality {0}, you'll have to settle in for a wait.
   PL: Jeśli chcesz {0} najwyższej jakości, trzeba się uzbroić w cierpliwość.
38. [Przedmioty, sklep i profil gracza [introduce_word_264] — tekst] 손
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_264].content
   limit: do 120 znaków
   EN: Hand
   PL: Dłoń
39. [Przedmioty, sklep i profil gracza [introduce_sentence_264] — tekst] 다가오지 마, 내게 {0}(을/를) 내밀지 마!!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_264].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No! No, no! Stay away from me! Don't reach your {0} out to me!!
   PL: Nie podchodź! Nie wyciągaj do mnie swojej {0}!!
40. [Przedmioty, sklep i profil gracza [introduce_word_265] — tekst] 허상
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_265].content
   limit: do 120 znaków
   EN: Phantasm
   PL: Iluzja
41. [Przedmioty, sklep i profil gracza [introduce_sentence_265] — tekst] 나의 텅 빈 {0} 속으로.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_265].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ... And carry them into this hollow {0} of mine.
   PL: …I wnieść je w głąb tej mojej pustej {0}.
42. [Przedmioty, sklep i profil gracza [introduce_word_266] — tekst] 정의
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_266].content
   limit: do 120 znaków
   EN: Justice
   PL: Sprawiedliwość
43. [Przedmioty, sklep i profil gracza [introduce_sentence_266] — tekst] 길을 비켜라. 그리하면 그대들의 {0}(을/를) 의심치 아니하겠다.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_266].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thou shalt make way in anticipation of my coming. Do this, and (thy/thine) {0} shan't fall to doubt.
   PL: Ustąp z drogi, a wątpliwości nie dotkną waszej {0}.
44. [Przedmioty, sklep i profil gracza [introduce_word_267] — tekst] 잿빛
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_267].content
   limit: do 120 znaków
   EN: Ashen
   PL: Popiół
45. [Przedmioty, sklep i profil gracza [introduce_sentence_267] — tekst] 사람은 사라져, 오직 {0}만 남으리.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_267].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thus man has become null, leaving only (the) {0} behind.
   PL: Tak człowiek stał się nicością — zostaje już tylko {0}.
46. [Przedmioty, sklep i profil gracza [introduce_word_268] — tekst] 눈부심
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_268].content
   limit: do 120 znaków
   EN: Blinding Glare
   PL: Oślepiający Blask
47. [Przedmioty, sklep i profil gracza [introduce_sentence_268] — tekst] 탄환은 흑점에 겨눠, {0} 속에 꿰뚫어라.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_268].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sight the bullet on the sunspot... and take a clean shot through (the) {0}.
   PL: Wyceluj pocisk w plamę słońca… i przebij {0} na wylot.
48. [Przedmioty, sklep i profil gracza [introduce_word_269] — tekst] 백화점
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_269].content
   limit: do 120 znaków
   EN: Department Store
   PL: Dom Handlowy
49. [Przedmioty, sklep i profil gracza [introduce_sentence_269] — tekst] 우리는, 나는, {0}의 모든 것을 먹어치울 거다. 더 이상 그 누구도 굶주리지 않도록.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_269].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: We—I—shall devour (this/these) {0}, so that none among you shall ever scrape an empty plate again.
   PL: My — ja — pożremy to {0} do ostatka. By nikt więcej nie zaznał głodu.
50. [Przedmioty, sklep i profil gracza [introduce_word_270] — tekst] 땀수
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_270].content
   limit: do 120 znaków
   EN: Stitch Per Inch
   PL: Ścieg na Cal
51. [Przedmioty, sklep i profil gracza [introduce_sentence_270] — tekst] {0}… {0}… {0}, {0}, {0}, {0}, {0}, {0}, {0}!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_270].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}... {0}... {0}, {0}, {0}, {0}, {0}, {0}, {0}!
   PL: {0}… {0}… {0}, {0}, {0}, {0}, {0}, {0}, {0}!
52. [Przedmioty, sklep i profil gracza [introduce_word_271] — tekst] 경청
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_271].content
   limit: do 120 znaków
   EN: Listen
   PL: Słuchać
53. [Przedmioty, sklep i profil gracza [introduce_sentence_271] — tekst] {0}하셔야죠?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_271].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You should {0}, you know?
   PL: Powinno się {0}, wiesz?
54. [Przedmioty, sklep i profil gracza [introduce_word_272] — tekst] 쐐기
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_272].content
   limit: do 120 znaków
   EN: Wedge
   PL: Klin
55. [Przedmioty, sklep i profil gracza [introduce_sentence_272] — tekst] {0} 대형 전개!
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_272].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Assume {0} formation!
   PL: Tworzymy formację: {0}!
56. [Przedmioty, sklep i profil gracza [introduce_word_273] — tekst] 보험갱신
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_273].content
   limit: do 120 znaków
   EN: Insurance Renewal
   PL: Przedłużenie Ubezpieczenia
57. [Przedmioty, sklep i profil gracza [introduce_sentence_273] — tekst] 이번에 {0} 하는 거 까먹지 않았죠?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_273].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Please tell me you haven't forgotten the upcoming {0}.
   PL: Mów, że nie zapomniałeś o nadchodzącym {0}.
58. [Przedmioty, sklep i profil gracza [introduce_word_274] — tekst] 맹세
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_274].content
   limit: do 120 znaków
   EN: Vow(s)
   PL: Przysięgi
59. [Przedmioty, sklep i profil gracza [introduce_sentence_274] — tekst] 지키지 못한 {0}(으로/로) 벼려낸 이 검은…
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_274].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This sword, sharpened with unkept {0}...
   PL: Ten miecz, naostrzony na niespełnionych {0}…
60. [Przedmioty, sklep i profil gracza [introduce_word_275] — tekst] 욕망
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_275].content
   limit: do 120 znaków
   EN: Desire
   PL: Pożądanie
61. [Przedmioty, sklep i profil gracza [introduce_sentence_275] — tekst] {0}에 골몰중이오.
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_275].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} has completely occupied my interest.
   PL: W całości pochłonęło mnie {0}.
62. [Przedmioty, sklep i profil gracza [introduce_word_276] — tekst] 실
   źródło: IntroductionPreset.json :: dataList[id=introduce_word_276].content
   limit: do 120 znaków
   EN: Thread
   PL: Nić
63. [Przedmioty, sklep i profil gracza [introduce_sentence_276] — tekst] 그래, {0}(을/를) 잣고 싶나?
   źródło: IntroductionPreset.json :: dataList[id=introduce_sentence_276].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: So, got (some) {0}(s) you want spun?
   PL: No i jak, masz {0} do przędzenia?

## Przedmioty, sklep i profil gracza: Items-a1c10p1
- plik gry: `Items-a1c10p1.json`

64. [Przedmioty, sklep i profil gracza [111] — nazwa] 시즌 8 - 3성 인격 출현 추출 티켓
   źródło: Items-a1c10p1.json :: dataList[id=111].name
   limit: do 70 znaków
   EN: [Season 8] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 8] Bilet Dekaekstrakcji Gwarantowanej 3★
65. [Przedmioty, sklep i profil gracza [111] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 8에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items-a1c10p1.json :: dataList[id=111].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 8] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 8] pojawia się na pewno.
66. [Przedmioty, sklep i profil gracza [111] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items-a1c10p1.json :: dataList[id=111].flavor
   limit: do 210 znaków
   EN: A special ticket with a mark on it. It can extract an Identity from a world of unlikely possibilities with certainty. The paper is fiercely beating and pulsing.
   PL: Specjalny bilet oznaczony pewnym znakiem. Pozwala na pewne wydobycie Tożsamości ze świata nikłych możliwości. Papier gwałtownie drga i pulsuje.
67. [Przedmioty, sklep i profil gracza [1108] — nazwa] 시즌 8 자아 파편 상자
   źródło: Items-a1c10p1.json :: dataList[id=1108].name
   limit: do 40 znaków
   EN: [Season 8] Egoshard Crate
   PL: [Sezon 8] Skrzynia Odłamków E.G.O
68. [Przedmioty, sklep i profil gracza [1108] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c10p1.json :: dataList[id=1108].desc
   limit: do 120 znaków
   EN: Open to receive 1-3 Egoshards of random Sinners.
   PL: Po użyciu otrzymujesz 1–3 Odłamków E.G.O losowego Grzesznika.
69. [Przedmioty, sklep i profil gracza [1108] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items-a1c10p1.json :: dataList[id=1108].flavor
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Egoshards were randomly harvested and stored in these boxes. Its contents are a mystery.\nWhen you hold one in a quiet place, you can hear small fusses.
   PL: Odłamki E.G.O Grzeszników losowo zebrano i zapieczętowano w skrzyni. Kto tam siedzi — nikt nie wie.\nTrzymana w ciszy, zdaje się wydawać drobny łomot.
70. [Przedmioty, sklep i profil gracza [1208] — nazwa] 시즌 8 자아 파편 선택 상자
   źródło: Items-a1c10p1.json :: dataList[id=1208].name
   limit: do 50 znaków
   EN: [Season 8] Nominable Egoshard Crate
   PL: [Sezon 8] Skrzynia Wyboru Odłamków E.G.O
71. [Przedmioty, sklep i profil gracza [1208] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c10p1.json :: dataList[id=1208].desc
   limit: do 120 znaków
   EN: Open to receive 1-3 Egoshards of a Sinner of choice.
   PL: Po użyciu otrzymujesz 1–3 Odłamków E.G.O wybranego Grzesznika.
72. [Przedmioty, sklep i profil gracza [1208] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items-a1c10p1.json :: dataList[id=1208].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A crate that yields Egoshards of a Sinner you choose.\nAccording to Faust, the crate's content is determined once the manager makes their decision.
   PL: Skrzynia pozwalająca zdobyć odłamki E.G.O wybranego Grzesznika.\nWedle Faust zawartość zostaje utwierdzona w momencie wyboru dokonanego przez Zarządcę otwierającego skrzynię.
73. [Przedmioty, sklep i profil gracza [10008] — nazwa] 시즌 8 [선택한 수감자] 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10008].name
   limit: do 60 znaków
   EN: Season 8 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 8 [Wybranego Grzesznika]
74. [Przedmioty, sklep i profil gracza [10108] — nazwa] 시즌 8 이상 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10108].name
   limit: do 50 znaków
   EN: [Season 8] Yi Sang’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Yi Sanga
75. [Przedmioty, sklep i profil gracza [10108] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10108].desc
   limit: do 120 znaków
   EN: Used for purchasing Yi Sang’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Yi Sanga w Automacie.
76. [Przedmioty, sklep i profil gracza [10108] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10108].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fleeting moments from any point within the Sinner’s lifetime, condensed into physical form. The shards float in the air.\nPossibilities are transient things; they drift in the realm of uncertainty unless seized.
   PL: Ulotne chwile z dowolnego punktu życia Grzesznika, uwięzione w postaci fizycznej. Odłamki unoszą się w powietrzu.\nMożliwości są ulotne; dryfują w sferze niepewności, dopóki ktoś ich nie chwyci.
77. [Przedmioty, sklep i profil gracza [10208] — nazwa] 시즌 8 파우스트 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10208].name
   limit: do 40 znaków
   EN: [Season 8] Faust’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Faust
78. [Przedmioty, sklep i profil gracza [10208] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10208].desc
   limit: do 120 znaków
   EN: Used for purchasing Faust’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Faust w Automacie.
79. [Przedmioty, sklep i profil gracza [10208] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10208].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Przedmioty, sklep i profil gracza [10308] — nazwa] 시즌 8 돈키호테 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10308].name
   limit: do 50 znaków
   EN: [Season 8] Don Quixote’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Don Quixote
81. [Przedmioty, sklep i profil gracza [10308] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10308].desc
   limit: do 120 znaków
   EN: Used for purchasing Don Quixote’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Don Quixote w Automacie.
82. [Przedmioty, sklep i profil gracza [10308] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10308].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Przedmioty, sklep i profil gracza [10408] — nazwa] 시즌 8 료슈 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10408].name
   limit: do 40 znaków
   EN: [Season 8] Ryōshū’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Ryōshū
84. [Przedmioty, sklep i profil gracza [10408] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10408].desc
   limit: do 120 znaków
   EN: Used for purchasing Ryōshū’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Ryōshū w Automacie.
85. [Przedmioty, sklep i profil gracza [10408] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10408].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Przedmioty, sklep i profil gracza [10508] — nazwa] 시즌 8 뫼르소 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10508].name
   limit: do 50 znaków
   EN: [Season 8] Meursault’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Meursault
87. [Przedmioty, sklep i profil gracza [10508] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10508].desc
   limit: do 120 znaków
   EN: Used for purchasing Meursault’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Meursault w Automacie.
88. [Przedmioty, sklep i profil gracza [10508] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10508].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Przedmioty, sklep i profil gracza [10608] — nazwa] 시즌 8 홍루 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10608].name
   limit: do 50 znaków
   EN: [Season 8] Hong Lu’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Hong Lu
90. [Przedmioty, sklep i profil gracza [10608] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10608].desc
   limit: do 120 znaków
   EN: Used for purchasing Hong Lu’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Hong Lu w Automacie.
91. [Przedmioty, sklep i profil gracza [10608] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10608].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Przedmioty, sklep i profil gracza [10708] — nazwa] 시즌 8 히스클리프 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10708].name
   limit: do 50 znaków
   EN: [Season 8] Heathcliff’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Heathcliffa
93. [Przedmioty, sklep i profil gracza [10708] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10708].desc
   limit: do 120 znaków
   EN: Used for purchasing Heathcliff’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Heathcliffa w Automacie.
94. [Przedmioty, sklep i profil gracza [10708] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10708].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Przedmioty, sklep i profil gracza [10808] — nazwa] 시즌 8 이스마엘 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10808].name
   limit: do 50 znaków
   EN: [Season 8] Ishmael’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Ishmael
96. [Przedmioty, sklep i profil gracza [10808] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10808].desc
   limit: do 120 znaków
   EN: Used for purchasing Ishmael’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Ishmael w Automacie.
97. [Przedmioty, sklep i profil gracza [10808] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10808].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Przedmioty, sklep i profil gracza [10908] — nazwa] 시즌 8 로쟈 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=10908].name
   limit: do 40 znaków
   EN: [Season 8] Rodion's Egoshard
   PL: [Sezon 8] Odłamek E.G.O Rodion
99. [Przedmioty, sklep i profil gracza [10908] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=10908].desc
   limit: do 120 znaków
   EN: Used for purchasing Rodion’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Rodion w Automacie.
100. [Przedmioty, sklep i profil gracza [10908] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=10908].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Przedmioty, sklep i profil gracza [11008] — nazwa] 시즌 8 싱클레어 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=11008].name
   limit: do 50 znaków
   EN: [Season 8] Sinclair’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Sinclair
102. [Przedmioty, sklep i profil gracza [11008] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=11008].desc
   limit: do 120 znaków
   EN: Used for purchasing Sinclair’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Sinclair w Automacie.
103. [Przedmioty, sklep i profil gracza [11008] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=11008].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Przedmioty, sklep i profil gracza [11108] — nazwa] 시즌 8 오티스 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=11108].name
   limit: do 40 znaków
   EN: [Season 8] Outis’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Outis
105. [Przedmioty, sklep i profil gracza [11108] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=11108].desc
   limit: do 120 znaków
   EN: Used for purchasing Outis’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Outis w Automacie.
106. [Przedmioty, sklep i profil gracza [11108] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=11108].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Przedmioty, sklep i profil gracza [11208] — nazwa] 시즌 8 그레고르 자아 파편
   źródło: Items-a1c10p1.json :: dataList[id=11208].name
   limit: do 40 znaków
   EN: [Season 8] Gregor’s Egoshard
   PL: [Sezon 8] Odłamek E.G.O Gregora
108. [Przedmioty, sklep i profil gracza [11208] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c10p1.json :: dataList[id=11208].desc
   limit: do 120 znaków
   EN: Used for purchasing Gregor’s Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Gregora w Automacie.
109. [Przedmioty, sklep i profil gracza [11208] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c10p1.json :: dataList[id=11208].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Przedmioty, sklep i profil gracza [12008] — nazwa] 시즌 8 동기화 · 환상해석 전용 파편 (공용)
   źródło: Items-a1c10p1.json :: dataList[id=12008].name
   limit: do 80 znaków
   EN: Season 8 Uptie & Threadspinning only Shard (Universal)
   PL: Odłamek Sezonu 8 wyłącznie do Synchronizacji i Splotu Nici (Uniwersalny)
111. [Przedmioty, sklep i profil gracza [12008] — opis] 모든 수감자 인격의 동기화, E.G.O의 환상 해석을 진행할 때 사용할 수 있다.
   źródło: Items-a1c10p1.json :: dataList[id=12008].desc
   limit: do 120 znaków
   EN: Can be used to Uptie Identities and Threadspin E.G.O for all Sinners.
   PL: Można stosować przy Synchronizacji Tożsamości i Splacie Nici E.G.O wszystkich Grzeszników.
112. [Przedmioty, sklep i profil gracza [12008] — tekst klimatyczny] 인격의 동기화, E.G.O의 환상해석을 진행할 때 수감자와 관계없이 공용으로 쓸 수 있는 파편.\n대신 이 파편을 아무리 모아도 인격이나 E.G.O를 추출할 수는 없다.\n'이 파편은 무엇이든 될 수 있는 황금가지에 대한 연구의 일환으로, 그 어떤 거울의 심상이나 세계에도 채워 넣을 수 있습니다. 네? 추출이요? 그건 당연히 안되죠. 어느 세계든 채워줄 수 있다는 것은 곧 어떤 세계도 처음부터 쌓아 올릴 수 없다는 것과 같으니까. - LCA 거울세계관측부서 수석 연구원'
   źródło: Items-a1c10p1.json :: dataList[id=12008].flavor
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A universal shard that can be used to Uptie or Threadspin Identities & E.G.O for all Sinners.\nHowever, these shards cannot be used to extract Identities or E.G.O, no matter how many of these shards one collects.\n'These shards are products of our research into the omnitransformative nature of Golden Boughs; it can be used to fill any fathoms or worlds of mirrors. Huh? Extractions? Of course not. Its one-size-fits-all-worlds nature would mean that it obviously cannot have been made *for* any specific world, right? - LCA Mirror World Observatorium Department Chief Researcher'
   PL: Uniwersalny odłamek, służący do Synchronizacji Tożsamości i Splotu Nici E.G.O niezależnie od Grzesznika.\nNie da się nim jednak wydobyć Tożsamości ani E.G.O, choćby zgromadzić ich całe stosy.\n„Odłamki te są owocem badań nad wszechprzemiennością Złotych Gałęzi; można nimi napełnić każde wyobrażenie czy świat lustra. Co? Ekstrakcja? Oczywiście, że nie. Skoro nadaje się do napełnienia każdego świata, to znaczy, że nie mógł powstać *dla* żadnego konkretnego świata, prawda? - Naczelny Badacz, Obserwatorium Światów Lustra, Dział LCA”

## Przedmioty, sklep i profil gracza: Items-a1c6
- plik gry: `Items-a1c6.json`

113. [Przedmioty, sklep i profil gracza [107] — nazwa] 시즌 4 - 3성 인격 출현 추출 티켓
   źródło: Items-a1c6.json :: dataList[id=107].name
   limit: do 70 znaków
   EN: [Season 4] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 4] Bilet Dekaekstrakcji Gwarantowanej 3★
114. [Przedmioty, sklep i profil gracza [107] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 4에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items-a1c6.json :: dataList[id=107].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 4] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 4] pojawia się na pewno.
115. [Przedmioty, sklep i profil gracza [107] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items-a1c6.json :: dataList[id=107].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Przedmioty, sklep i profil gracza [1104] — nazwa] 시즌 4 자아 파편 상자
   źródło: Items-a1c6.json :: dataList[id=1104].name
   limit: do 40 znaków
   EN: [Season 4] Egoshard Crate
   PL: [Sezon 4] Skrzynia Odłamków E.G.O
117. [Przedmioty, sklep i profil gracza [1104] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c6.json :: dataList[id=1104].desc
   limit: do 120 znaków
   EN: Open to receive 1-3 random Egoshards.
   PL: Po użyciu otrzymujesz 1–3 losowych Odłamków E.G.O.
118. [Przedmioty, sklep i profil gracza [1104] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items-a1c6.json :: dataList[id=1104].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Przedmioty, sklep i profil gracza [1204] — nazwa] 시즌 4 자아 파편 선택 상자
   źródło: Items-a1c6.json :: dataList[id=1204].name
   limit: do 50 znaków
   EN: [Season 4] Nominable Egoshard Crate
   PL: [Sezon 4] Skrzynia Wyboru Odłamków E.G.O
120. [Przedmioty, sklep i profil gracza [1204] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c6.json :: dataList[id=1204].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Przedmioty, sklep i profil gracza [1204] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items-a1c6.json :: dataList[id=1204].flavor
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A crate that yields Egoshards of a Sinner you choose.\nAccording to Faust, its contents are determined once a manager makes their decision.
   PL: Skrzynia pozwalająca zdobyć odłamki E.G.O wybranego Grzesznika.\nWedle Faust zawartość zostaje utwierdzona w momencie wyboru dokonanego przez Zarządcę otwierającego skrzynię.
122. [Przedmioty, sklep i profil gracza [10104] — nazwa] 시즌 4 이상 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10104].name
   limit: do 50 znaków
   EN: [Season 4] Yi Sang’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Yi Sanga
123. [Przedmioty, sklep i profil gracza [10104] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10104].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Przedmioty, sklep i profil gracza [10104] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10104].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Przedmioty, sklep i profil gracza [10204] — nazwa] 시즌 4 파우스트 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10204].name
   limit: do 40 znaków
   EN: [Season 4] Faust’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Faust
126. [Przedmioty, sklep i profil gracza [10204] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10204].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Przedmioty, sklep i profil gracza [10204] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10204].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Przedmioty, sklep i profil gracza [10304] — nazwa] 시즌 4 돈키호테 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10304].name
   limit: do 50 znaków
   EN: [Season 4] Don Quixote’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Don Quixote
129. [Przedmioty, sklep i profil gracza [10304] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10304].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Przedmioty, sklep i profil gracza [10304] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10304].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Przedmioty, sklep i profil gracza [10404] — nazwa] 시즌 4 료슈 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10404].name
   limit: do 40 znaków
   EN: [Season 4] Ryōshū’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Ryōshū
132. [Przedmioty, sklep i profil gracza [10404] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10404].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Przedmioty, sklep i profil gracza [10404] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10404].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Przedmioty, sklep i profil gracza [10504] — nazwa] 시즌 4 뫼르소 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10504].name
   limit: do 50 znaków
   EN: [Season 4] Meursault’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Meursault
135. [Przedmioty, sklep i profil gracza [10504] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10504].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Przedmioty, sklep i profil gracza [10504] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10504].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Przedmioty, sklep i profil gracza [10604] — nazwa] 시즌 4 홍루 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10604].name
   limit: do 50 znaków
   EN: [Season 4] Hong Lu’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Hong Lu
138. [Przedmioty, sklep i profil gracza [10604] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10604].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Przedmioty, sklep i profil gracza [10604] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10604].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Przedmioty, sklep i profil gracza [10704] — nazwa] 시즌 4 히스클리프 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10704].name
   limit: do 50 znaków
   EN: [Season 4] Heathcliff’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Heathcliffa
141. [Przedmioty, sklep i profil gracza [10704] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10704].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Przedmioty, sklep i profil gracza [10704] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10704].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Przedmioty, sklep i profil gracza [10804] — nazwa] 시즌 4 이스마엘 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10804].name
   limit: do 50 znaków
   EN: [Season 4] Ishmael’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Ishmael
144. [Przedmioty, sklep i profil gracza [10804] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10804].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Przedmioty, sklep i profil gracza [10804] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10804].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Przedmioty, sklep i profil gracza [10904] — nazwa] 시즌 4 로쟈 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10904].name
   limit: do 40 znaków
   EN: [Season 4] Rodion's Egoshard
   PL: [Sezon 4] Odłamek E.G.O Rodion
147. [Przedmioty, sklep i profil gracza [10904] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=10904].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Przedmioty, sklep i profil gracza [10904] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=10904].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Przedmioty, sklep i profil gracza [11004] — nazwa] 시즌 4 싱클레어 자아 파편
   źródło: Items-a1c6.json :: dataList[id=11004].name
   limit: do 50 znaków
   EN: [Season 4] Sinclair’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Sinclair
150. [Przedmioty, sklep i profil gracza [11004] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=11004].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Przedmioty, sklep i profil gracza [11004] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=11004].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Przedmioty, sklep i profil gracza [11104] — nazwa] 시즌 4 오티스 자아 파편
   źródło: Items-a1c6.json :: dataList[id=11104].name
   limit: do 40 znaków
   EN: [Season 4] Outis’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Outis
153. [Przedmioty, sklep i profil gracza [11104] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=11104].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Przedmioty, sklep i profil gracza [11104] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=11104].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Przedmioty, sklep i profil gracza [11204] — nazwa] 시즌 4 그레고르 자아 파편
   źródło: Items-a1c6.json :: dataList[id=11204].name
   limit: do 40 znaków
   EN: [Season 4] Gregor’s Egoshard
   PL: [Sezon 4] Odłamek E.G.O Gregora
156. [Przedmioty, sklep i profil gracza [11204] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c6.json :: dataList[id=11204].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Przedmioty, sklep i profil gracza [11204] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c6.json :: dataList[id=11204].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Przedmioty, sklep i profil gracza [10004] — nazwa] 시즌4 [선택한 수감자] 자아 파편
   źródło: Items-a1c6.json :: dataList[id=10004].name
   limit: do 60 znaków
   EN: Season 4 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 4 [Wybranego Grzesznika]

## Przedmioty, sklep i profil gracza: Items-a1c7p1
- plik gry: `Items-a1c7p1.json`

159. [Przedmioty, sklep i profil gracza [108] — nazwa] 시즌 5 - 3성 인격 출현 추출 티켓
   źródło: Items-a1c7p1.json :: dataList[id=108].name
   limit: do 70 znaków
   EN: [Season 5] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 5] Bilet Dekaekstrakcji Gwarantowanej 3★
160. [Przedmioty, sklep i profil gracza [108] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 5에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items-a1c7p1.json :: dataList[id=108].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 5] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 5] pojawia się na pewno.
161. [Przedmioty, sklep i profil gracza [108] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items-a1c7p1.json :: dataList[id=108].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Przedmioty, sklep i profil gracza [225] — nazwa] 인격 특수 강화 티켓 V
   źródło: Items-a1c7p1.json :: dataList[id=225].name
   limit: do 40 znaków
   EN: Level Boost Ticket V
   PL: Bilet Specjalnego Wzmocnienia V
163. [Przedmioty, sklep i profil gracza [225] — opis] 사용 시, 인격의 레벨이 50까지 증가한다.
   źródło: Items-a1c7p1.json :: dataList[id=225].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 50.
   PL: Po użyciu podnosi poziom Tożsamości do 50.
164. [Przedmioty, sklep i profil gracza [225] — tekst klimatyczny] 인격 학습 티켓이 초과 경험을 할 수 있게 만드는 제한 해제형 티켓.\n"형언하기 힘들 정도의 지식과 정보가 뇌 속으로 밀려드는 감각이다. 이러한 경험이 최초는 아니지만, 쉽게 익숙해질 수 없다고 생각할 정도의 강렬함이다. 구토와 현기증, 그리고 안구의 혈관이 일부 파손되어 시야가 잠시 붉어지는 부작용을 체험했다. 그러나 확실하게, 강해졌다."
   źródło: Items-a1c7p1.json :: dataList[id=225].flavor
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limit-disengaging ticket that allows an Identity to hold excess experience.\n"Verbally incommunicable amount of knowledge and information deluges into my brain in such merciless brutality that the suggestion that one should acclimatize oneself to it is, despite having prior engagement with such a method, a rather ludicrous idea. The side effects of this procedure included vomiting, nausea, and rupturing of blood vessels within the ocular region, causing redness in vision. However, it can be said with certainty that we have been made stronger as a result."
   PL: Bilet z odblokowanym limitem — pozwala Tożsamości gromadzić nadwyżkę doświadczenia.\n„Czuję, jak nie do opisania masa wiedzy i informacji wlewa mi się do mózgu. Choć doświadczyłem tego już nie raz, jego intensywność nie pozwala się przyzwyczaić. Doświadczyłem wymiotów i zawrotów głowy, a pęknięte naczynia w oku na chwilę zabarwiły mi pole widzenia na czerwono. Niepodważalnie jednak stałem się silniejszy.”
165. [Przedmioty, sklep i profil gracza [1105] — nazwa] 시즌 5 자아 파편 상자
   źródło: Items-a1c7p1.json :: dataList[id=1105].name
   limit: do 40 znaków
   EN: [Season 5] Egoshard Crate
   PL: [Sezon 5] Skrzynia Odłamków E.G.O
166. [Przedmioty, sklep i profil gracza [1105] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c7p1.json :: dataList[id=1105].desc
   limit: do 120 znaków
   EN: Contains 1-3 Egoshards of a random Sinner.
   PL: Zawiera 1–3 Odłamków E.G.O losowego Grzesznika.
167. [Przedmioty, sklep i profil gracza [1105] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items-a1c7p1.json :: dataList[id=1105].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Przedmioty, sklep i profil gracza [1205] — nazwa] 시즌 5 자아 파편 선택 상자
   źródło: Items-a1c7p1.json :: dataList[id=1205].name
   limit: do 50 znaków
   EN: [Season 5] Nominable Egoshard Crate
   PL: [Sezon 5] Skrzynia Wyboru Odłamków E.G.O
169. [Przedmioty, sklep i profil gracza [1205] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c7p1.json :: dataList[id=1205].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Przedmioty, sklep i profil gracza [1205] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items-a1c7p1.json :: dataList[id=1205].flavor
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Przedmioty, sklep i profil gracza [10105] — nazwa] 시즌 5 이상 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10105].name
   limit: do 50 znaków
   EN: [Season 5] Yi Sang’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Yi Sanga
172. [Przedmioty, sklep i profil gracza [10105] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10105].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Przedmioty, sklep i profil gracza [10105] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10105].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Przedmioty, sklep i profil gracza [10205] — nazwa] 시즌 5 파우스트 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10205].name
   limit: do 40 znaków
   EN: [Season 5] Faust’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Faust
175. [Przedmioty, sklep i profil gracza [10205] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10205].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Przedmioty, sklep i profil gracza [10205] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10205].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Przedmioty, sklep i profil gracza [10305] — nazwa] 시즌 5 돈키호테 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10305].name
   limit: do 50 znaków
   EN: [Season 5] Don Quixote’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Don Quixote
178. [Przedmioty, sklep i profil gracza [10305] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10305].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Przedmioty, sklep i profil gracza [10305] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10305].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Przedmioty, sklep i profil gracza [10405] — nazwa] 시즌 5 료슈 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10405].name
   limit: do 40 znaków
   EN: [Season 5] Ryōshū’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Ryōshū
181. [Przedmioty, sklep i profil gracza [10405] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10405].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Przedmioty, sklep i profil gracza [10405] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10405].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Przedmioty, sklep i profil gracza [10505] — nazwa] 시즌 5 뫼르소 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10505].name
   limit: do 50 znaków
   EN: [Season 5] Meursault’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Meursault
184. [Przedmioty, sklep i profil gracza [10505] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10505].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Przedmioty, sklep i profil gracza [10505] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10505].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Przedmioty, sklep i profil gracza [10605] — nazwa] 시즌 5 홍루 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10605].name
   limit: do 50 znaków
   EN: [Season 5] Hong Lu’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Hong Lu
187. [Przedmioty, sklep i profil gracza [10605] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10605].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Przedmioty, sklep i profil gracza [10605] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10605].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Przedmioty, sklep i profil gracza [10705] — nazwa] 시즌 5 히스클리프 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10705].name
   limit: do 50 znaków
   EN: [Season 5] Heathcliff’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Heathcliffa
190. [Przedmioty, sklep i profil gracza [10705] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10705].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Przedmioty, sklep i profil gracza [10705] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10705].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Przedmioty, sklep i profil gracza [10805] — nazwa] 시즌 5 이스마엘 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10805].name
   limit: do 50 znaków
   EN: [Season 5] Ishmael’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Ishmael
193. [Przedmioty, sklep i profil gracza [10805] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10805].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Przedmioty, sklep i profil gracza [10805] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10805].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Przedmioty, sklep i profil gracza [10905] — nazwa] 시즌 5 로쟈 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10905].name
   limit: do 40 znaków
   EN: [Season 5] Rodion's Egoshard
   PL: [Sezon 5] Odłamek E.G.O Rodion
196. [Przedmioty, sklep i profil gracza [10905] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=10905].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Przedmioty, sklep i profil gracza [10905] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=10905].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Przedmioty, sklep i profil gracza [11005] — nazwa] 시즌 5 싱클레어 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=11005].name
   limit: do 50 znaków
   EN: [Season 5] Sinclair’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Sinclair
199. [Przedmioty, sklep i profil gracza [11005] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=11005].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Przedmioty, sklep i profil gracza [11005] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=11005].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Przedmioty, sklep i profil gracza [11105] — nazwa] 시즌 5 오티스 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=11105].name
   limit: do 40 znaków
   EN: [Season 5] Outis’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Outis
202. [Przedmioty, sklep i profil gracza [11105] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=11105].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Przedmioty, sklep i profil gracza [11105] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=11105].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Przedmioty, sklep i profil gracza [11205] — nazwa] 시즌 5 그레고르 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=11205].name
   limit: do 40 znaków
   EN: [Season 5] Gregor’s Egoshard
   PL: [Sezon 5] Odłamek E.G.O Gregora
205. [Przedmioty, sklep i profil gracza [11205] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c7p1.json :: dataList[id=11205].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Przedmioty, sklep i profil gracza [11205] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c7p1.json :: dataList[id=11205].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Przedmioty, sklep i profil gracza [12005] — nazwa] 시즌 5 동기화 · 환상해석 전용 파편 (공용)
   źródło: Items-a1c7p1.json :: dataList[id=12005].name
   limit: do 80 znaków
   EN: Season 5 Uptie & Threadspinning only Shard (Universal)
   PL: Odłamek Sezonu 5 wyłącznie do Synchronizacji i Splotu Nici (Uniwersalny)
208. [Przedmioty, sklep i profil gracza [12005] — opis] 모든 수감자 인격의 동기화, E.G.O의 환상 해석을 진행할 때 사용할 수 있다.
   źródło: Items-a1c7p1.json :: dataList[id=12005].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Przedmioty, sklep i profil gracza [12005] — tekst klimatyczny] 인격의 동기화, E.G.O의 환상해석을 진행할 때 수감자와 관계없이 공용으로 쓸 수 있는 파편.\n대신 이 파편을 아무리 모아도 인격이나 E.G.O를 추출할 수는 없다.\n'이 파편은 무엇이든 될 수 있는 황금가지에 대한 연구의 일환으로, 그 어떤 거울의 심상이나 세계에도 채워 넣을 수 있습니다. 네? 추출이요? 그건 당연히 안되죠. 어느 세계든 채워줄 수 있다는 것은 곧 어떤 세계도 처음부터 쌓아 올릴 수 없다는 것과 같으니까. - LCA 거울세계관측부서 수석 연구원'
   źródło: Items-a1c7p1.json :: dataList[id=12005].flavor
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Przedmioty, sklep i profil gracza [10005] — nazwa] 시즌 5 [선택한 수감자] 자아 파편
   źródło: Items-a1c7p1.json :: dataList[id=10005].name
   limit: do 60 znaków
   EN: Season 5 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 5 [Wybranego Grzesznika]

## Przedmioty, sklep i profil gracza: Items-a1c8p1
- plik gry: `Items-a1c8p1.json`

211. [Przedmioty, sklep i profil gracza [109] — nazwa] 시즌 6 - 3성 인격 출현 추출 티켓
   źródło: Items-a1c8p1.json :: dataList[id=109].name
   limit: do 70 znaków
   EN: [Season 6] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 6] Bilet Dekaekstrakcji Gwarantowanej 3★
212. [Przedmioty, sklep i profil gracza [109] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 6에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items-a1c8p1.json :: dataList[id=109].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 6] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 6] pojawia się na pewno.
213. [Przedmioty, sklep i profil gracza [109] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items-a1c8p1.json :: dataList[id=109].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Przedmioty, sklep i profil gracza [1106] — nazwa] 시즌 6 자아 파편 상자
   źródło: Items-a1c8p1.json :: dataList[id=1106].name
   limit: do 40 znaków
   EN: [Season 6] Egoshard Crate
   PL: [Sezon 6] Skrzynia Odłamków E.G.O
215. [Przedmioty, sklep i profil gracza [1106] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c8p1.json :: dataList[id=1106].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Przedmioty, sklep i profil gracza [1106] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items-a1c8p1.json :: dataList[id=1106].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Przedmioty, sklep i profil gracza [1206] — nazwa] 시즌 6 자아 파편 선택 상자
   źródło: Items-a1c8p1.json :: dataList[id=1206].name
   limit: do 50 znaków
   EN: [Season 6] Nominable Egoshard Crate
   PL: [Sezon 6] Skrzynia Wyboru Odłamków E.G.O
218. [Przedmioty, sklep i profil gracza [1206] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c8p1.json :: dataList[id=1206].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Przedmioty, sklep i profil gracza [1206] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items-a1c8p1.json :: dataList[id=1206].flavor
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Przedmioty, sklep i profil gracza [10106] — nazwa] 시즌 6 이상 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10106].name
   limit: do 50 znaków
   EN: [Season 6] Yi Sang’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Yi Sanga
221. [Przedmioty, sklep i profil gracza [10106] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10106].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Przedmioty, sklep i profil gracza [10106] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10106].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Przedmioty, sklep i profil gracza [10206] — nazwa] 시즌 6 파우스트 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10206].name
   limit: do 40 znaków
   EN: [Season 6] Faust’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Faust
224. [Przedmioty, sklep i profil gracza [10206] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10206].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Przedmioty, sklep i profil gracza [10206] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10206].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Przedmioty, sklep i profil gracza [10306] — nazwa] 시즌 6 돈키호테 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10306].name
   limit: do 50 znaków
   EN: [Season 6] Don Quixote’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Don Quixote
227. [Przedmioty, sklep i profil gracza [10306] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10306].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Przedmioty, sklep i profil gracza [10306] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10306].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Przedmioty, sklep i profil gracza [10406] — nazwa] 시즌 6 료슈 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10406].name
   limit: do 40 znaków
   EN: [Season 6] Ryōshū’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Ryōshū
230. [Przedmioty, sklep i profil gracza [10406] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10406].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Przedmioty, sklep i profil gracza [10406] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10406].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Przedmioty, sklep i profil gracza [10506] — nazwa] 시즌 6 뫼르소 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10506].name
   limit: do 50 znaków
   EN: [Season 6] Meursault’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Meursault
233. [Przedmioty, sklep i profil gracza [10506] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10506].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Przedmioty, sklep i profil gracza [10506] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10506].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Przedmioty, sklep i profil gracza [10606] — nazwa] 시즌 6 홍루 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10606].name
   limit: do 50 znaków
   EN: [Season 6] Hong Lu’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Hong Lu
236. [Przedmioty, sklep i profil gracza [10606] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10606].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Przedmioty, sklep i profil gracza [10606] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10606].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Przedmioty, sklep i profil gracza [10706] — nazwa] 시즌 6 히스클리프 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10706].name
   limit: do 50 znaków
   EN: [Season 6] Heathcliff’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Heathcliffa
239. [Przedmioty, sklep i profil gracza [10706] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10706].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Przedmioty, sklep i profil gracza [10706] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10706].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Przedmioty, sklep i profil gracza [10806] — nazwa] 시즌 6 이스마엘 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10806].name
   limit: do 50 znaków
   EN: [Season 6] Ishmael’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Ishmael
242. [Przedmioty, sklep i profil gracza [10806] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10806].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Przedmioty, sklep i profil gracza [10806] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10806].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Przedmioty, sklep i profil gracza [10906] — nazwa] 시즌 6 로쟈 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10906].name
   limit: do 40 znaków
   EN: [Season 6] Rodion's Egoshard
   PL: [Sezon 6] Odłamek E.G.O Rodion
245. [Przedmioty, sklep i profil gracza [10906] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=10906].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Przedmioty, sklep i profil gracza [10906] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=10906].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Przedmioty, sklep i profil gracza [11006] — nazwa] 시즌 6 싱클레어 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=11006].name
   limit: do 50 znaków
   EN: [Season 6] Sinclair’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Sinclair
248. [Przedmioty, sklep i profil gracza [11006] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=11006].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Przedmioty, sklep i profil gracza [11006] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=11006].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Przedmioty, sklep i profil gracza [11106] — nazwa] 시즌 6 오티스 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=11106].name
   limit: do 40 znaków
   EN: [Season 6] Outis’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Outis
251. [Przedmioty, sklep i profil gracza [11106] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=11106].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Przedmioty, sklep i profil gracza [11106] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=11106].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Przedmioty, sklep i profil gracza [11206] — nazwa] 시즌 6 그레고르 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=11206].name
   limit: do 40 znaków
   EN: [Season 6] Gregor’s Egoshard
   PL: [Sezon 6] Odłamek E.G.O Gregora
254. [Przedmioty, sklep i profil gracza [11206] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c8p1.json :: dataList[id=11206].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Przedmioty, sklep i profil gracza [11206] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c8p1.json :: dataList[id=11206].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Przedmioty, sklep i profil gracza [12006] — nazwa] 시즌 6 동기화 · 환상해석 전용 파편 (공용)
   źródło: Items-a1c8p1.json :: dataList[id=12006].name
   limit: do 80 znaków
   EN: Season 6 Uptie & Threadspinning only Shard (Universal)
   PL: Odłamek Sezonu 6 wyłącznie do Synchronizacji i Splotu Nici (Uniwersalny)
257. [Przedmioty, sklep i profil gracza [12006] — opis] 모든 수감자 인격의 동기화, E.G.O의 환상 해석을 진행할 때 사용할 수 있다.
   źródło: Items-a1c8p1.json :: dataList[id=12006].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Przedmioty, sklep i profil gracza [12006] — tekst klimatyczny] 인격의 동기화, E.G.O의 환상해석을 진행할 때 수감자와 관계없이 공용으로 쓸 수 있는 파편.\n대신 이 파편을 아무리 모아도 인격이나 E.G.O를 추출할 수는 없다.\n'이 파편은 무엇이든 될 수 있는 황금가지에 대한 연구의 일환으로, 그 어떤 거울의 심상이나 세계에도 채워 넣을 수 있습니다. 네? 추출이요? 그건 당연히 안되죠. 어느 세계든 채워줄 수 있다는 것은 곧 어떤 세계도 처음부터 쌓아 올릴 수 없다는 것과 같으니까. - LCA 거울세계관측부서 수석 연구원'
   źródło: Items-a1c8p1.json :: dataList[id=12006].flavor
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Przedmioty, sklep i profil gracza [10006] — nazwa] 시즌 6 [선택한 수감자] 자아 파편
   źródło: Items-a1c8p1.json :: dataList[id=10006].name
   limit: do 60 znaków
   EN: Season 6 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 6 [Wybranego Grzesznika]

## Przedmioty, sklep i profil gracza: Items-a1c9p1
- plik gry: `Items-a1c9p1.json`

260. [Przedmioty, sklep i profil gracza [110] — nazwa] 시즌 7 - 3성 인격 출현 추출 티켓
   źródło: Items-a1c9p1.json :: dataList[id=110].name
   limit: do 70 znaków
   EN: [Season 7] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 7] Bilet Dekaekstrakcji Gwarantowanej 3★
261. [Przedmioty, sklep i profil gracza [110] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 7에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items-a1c9p1.json :: dataList[id=110].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 7] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 7] pojawia się na pewno.
262. [Przedmioty, sklep i profil gracza [110] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items-a1c9p1.json :: dataList[id=110].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Przedmioty, sklep i profil gracza [226] — nazwa] 인격 특수 강화 티켓 VI
   źródło: Items-a1c9p1.json :: dataList[id=226].name
   limit: do 40 znaków
   EN: Level Boost Ticket VI
   PL: Bilet Specjalnego Wzmocnienia VI
264. [Przedmioty, sklep i profil gracza [226] — opis] 사용 시, 인격의 레벨이 60까지 증가한다.
   źródło: Items-a1c9p1.json :: dataList[id=226].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 60.
   PL: Po użyciu podnosi poziom Tożsamości do 60.
265. [Przedmioty, sklep i profil gracza [226] — tekst klimatyczny] 인격 학습 티켓이 초과 경험을 할 수 있게 만드는 제한 해제형 티켓.\n"티켓이라... 이건 승차권의 형태를 한 종이 재질의 티켓이군. 티켓은 어디론가 갈 수 있도록 하는 매개체. 무언가를 타거나, 어딘가로 입장하거나. 대가와 자격이 필요한 무언가에 접근할 수 있게 하는 화폐. 하지만 그건 물리적인 개념만을 다룬다고만 할 수 있겠지. 종이 형태가 아닌 그 무엇이든 티켓이 될 수 있다.\n몰락한 자신을, 구덩이에 빠진 자신을 끌어올려 줄 거미줄과 같은 동아줄도 누군가에게는 티켓이었다. 나를 끌어올려 주는 무언가. 나를 어디론가 초대해주는 것. 그런 것 모두 티켓이라 부를 수 있으니 이것도 티켓의 형태를 띤 것이겠지. 말이 길어졌군." - LCD 어느 팀장
   źródło: Items-a1c9p1.json :: dataList[id=226].flavor
   limit: do 1080 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limit-disengaging ticket that allows an Identity to hold excess experience.\n\nA "ticket..." Yes, this appears to be a boarding ticket made of paper. Tickets are, in a way, mediums that unlock destinations for us, a means by which we may travel to places. They also serve as transactional items—a permit to board, to enter. A currency that acts as both the price and right of access. But that is true only in a physical sense. A "ticket" need not be a slip of paper.\nSome considered that last spider's thread—the last lifeline of hope that could pull their downtrodden selves out of an inescapable pit—as a "ticket." Something that lifts me up or invites me somewhere may be called a ticket as well; it is likely that these artifacts assume the form of tickets for that precise reason. Perhaps this elaboration has been too verbose. - A Team Leader at LCD
   PL: Bilet z odblokowanym limitem — pozwala Tożsamości gromadzić nadwyżkę doświadczenia.\n\n„Bilet… Tak, to bilet w postaci papierowej przepustki. Bilet to medium pozwalające dotrzeć dokądś. Umożliwia wstęp albo przejazd. Waluta otwierająca dostęp do tego, co wymaga zapłaty i kwalifikacji. Ale to tylko fizyczne rozumienie. Biletem może stać się wszystko, czego formą nie jest papier.\nKtoś uznał za bilet ostatnią pajęczą nić — ostatnią nitkę nadziei, co wyciągnęła jego zdeptane ja z nieuniknionej studni. Wszystko, co podnosi mnie do góry, wszystko, co zaprasza mnie gdziekolwiek — również można nazwać biletem. Więc i to jest bilet, choćby formę miał inną. Za dużo mówiłem.” - Pewien Dowódca Zespołu LCD
266. [Przedmioty, sklep i profil gracza [1107] — nazwa] 시즌 7 자아 파편 상자
   źródło: Items-a1c9p1.json :: dataList[id=1107].name
   limit: do 40 znaków
   EN: [Season 7] Egoshard Crate
   PL: [Sezon 7] Skrzynia Odłamków E.G.O
267. [Przedmioty, sklep i profil gracza [1107] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c9p1.json :: dataList[id=1107].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Przedmioty, sklep i profil gracza [1107] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items-a1c9p1.json :: dataList[id=1107].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Przedmioty, sklep i profil gracza [1207] — nazwa] 시즌 7 자아 파편 선택 상자
   źródło: Items-a1c9p1.json :: dataList[id=1207].name
   limit: do 50 znaków
   EN: [Season 7] Nominable Egoshard Crate
   PL: [Sezon 7] Skrzynia Wyboru Odłamków E.G.O
270. [Przedmioty, sklep i profil gracza [1207] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items-a1c9p1.json :: dataList[id=1207].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Przedmioty, sklep i profil gracza [1207] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items-a1c9p1.json :: dataList[id=1207].flavor
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Przedmioty, sklep i profil gracza [10107] — nazwa] 시즌 7 이상 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10107].name
   limit: do 50 znaków
   EN: [Season 7] Yi Sang’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Yi Sanga
273. [Przedmioty, sklep i profil gracza [10107] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10107].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Przedmioty, sklep i profil gracza [10107] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10107].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Przedmioty, sklep i profil gracza [10207] — nazwa] 시즌 7 파우스트 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10207].name
   limit: do 40 znaków
   EN: [Season 7] Faust’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Faust
276. [Przedmioty, sklep i profil gracza [10207] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10207].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Przedmioty, sklep i profil gracza [10207] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10207].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Przedmioty, sklep i profil gracza [10307] — nazwa] 시즌 7 돈키호테 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10307].name
   limit: do 50 znaków
   EN: [Season 7] Don Quixote’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Don Quixote
279. [Przedmioty, sklep i profil gracza [10307] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10307].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Przedmioty, sklep i profil gracza [10307] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10307].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Przedmioty, sklep i profil gracza [10407] — nazwa] 시즌 7 료슈 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10407].name
   limit: do 40 znaków
   EN: [Season 7] Ryōshū’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Ryōshū
282. [Przedmioty, sklep i profil gracza [10407] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10407].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Przedmioty, sklep i profil gracza [10407] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10407].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Przedmioty, sklep i profil gracza [10507] — nazwa] 시즌 7 뫼르소 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10507].name
   limit: do 50 znaków
   EN: [Season 7] Meursault’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Meursault
285. [Przedmioty, sklep i profil gracza [10507] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10507].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Przedmioty, sklep i profil gracza [10507] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10507].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Przedmioty, sklep i profil gracza [10607] — nazwa] 시즌 7 홍루 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10607].name
   limit: do 50 znaków
   EN: [Season 7] Hong Lu’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Hong Lu
288. [Przedmioty, sklep i profil gracza [10607] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10607].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Przedmioty, sklep i profil gracza [10607] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10607].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Przedmioty, sklep i profil gracza [10707] — nazwa] 시즌 7 히스클리프 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10707].name
   limit: do 50 znaków
   EN: [Season 7] Heathcliff’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Heathcliffa
291. [Przedmioty, sklep i profil gracza [10707] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10707].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Przedmioty, sklep i profil gracza [10707] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10707].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Przedmioty, sklep i profil gracza [10807] — nazwa] 시즌 7 이스마엘 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10807].name
   limit: do 50 znaków
   EN: [Season 7] Ishmael’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Ishmael
294. [Przedmioty, sklep i profil gracza [10807] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10807].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Przedmioty, sklep i profil gracza [10807] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10807].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Przedmioty, sklep i profil gracza [10907] — nazwa] 시즌 7 로쟈 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10907].name
   limit: do 40 znaków
   EN: [Season 7] Rodion's Egoshard
   PL: [Sezon 7] Odłamek E.G.O Rodion
297. [Przedmioty, sklep i profil gracza [10907] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=10907].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Przedmioty, sklep i profil gracza [10907] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=10907].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Przedmioty, sklep i profil gracza [11007] — nazwa] 시즌 7 싱클레어 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=11007].name
   limit: do 50 znaków
   EN: [Season 7] Sinclair’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Sinclair
300. [Przedmioty, sklep i profil gracza [11007] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=11007].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Przedmioty, sklep i profil gracza [11007] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=11007].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Przedmioty, sklep i profil gracza [11107] — nazwa] 시즌 7 오티스 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=11107].name
   limit: do 40 znaków
   EN: [Season 7] Outis’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Outis
303. [Przedmioty, sklep i profil gracza [11107] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=11107].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Przedmioty, sklep i profil gracza [11107] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=11107].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Przedmioty, sklep i profil gracza [11207] — nazwa] 시즌 7 그레고르 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=11207].name
   limit: do 40 znaków
   EN: [Season 7] Gregor’s Egoshard
   PL: [Sezon 7] Odłamek E.G.O Gregora
306. [Przedmioty, sklep i profil gracza [11207] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items-a1c9p1.json :: dataList[id=11207].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Przedmioty, sklep i profil gracza [11207] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items-a1c9p1.json :: dataList[id=11207].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Przedmioty, sklep i profil gracza [12007] — nazwa] 시즌 7 동기화 · 환상해석 전용 파편 (공용)
   źródło: Items-a1c9p1.json :: dataList[id=12007].name
   limit: do 80 znaków
   EN: Season 7 Uptie & Threadspinning only Shard (Universal)
   PL: Odłamek Sezonu 7 wyłącznie do Synchronizacji i Splotu Nici (Uniwersalny)
309. [Przedmioty, sklep i profil gracza [12007] — opis] 모든 수감자 인격의 동기화, E.G.O의 환상 해석을 진행할 때 사용할 수 있다.
   źródło: Items-a1c9p1.json :: dataList[id=12007].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Przedmioty, sklep i profil gracza [12007] — tekst klimatyczny] 인격의 동기화, E.G.O의 환상해석을 진행할 때 수감자와 관계없이 공용으로 쓸 수 있는 파편.\n대신 이 파편을 아무리 모아도 인격이나 E.G.O를 추출할 수는 없다.\n'이 파편은 무엇이든 될 수 있는 황금가지에 대한 연구의 일환으로, 그 어떤 거울의 심상이나 세계에도 채워 넣을 수 있습니다. 네? 추출이요? 그건 당연히 안되죠. 어느 세계든 채워줄 수 있다는 것은 곧 어떤 세계도 처음부터 쌓아 올릴 수 없다는 것과 같으니까. - LCA 거울세계관측부서 수석 연구원'
   źródło: Items-a1c9p1.json :: dataList[id=12007].flavor
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Przedmioty, sklep i profil gracza [10007] — nazwa] 시즌 7 [선택한 수감자] 자아 파편
   źródło: Items-a1c9p1.json :: dataList[id=10007].name
   limit: do 60 znaków
   EN: Season 7 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 7 [Wybranego Grzesznika]
312. [Przedmioty, sklep i profil gracza [236] — nazwa] 인격 성장 도약 티켓 - ver.3
   źródło: Items-a1c9p1.json :: dataList[id=236].name
   limit: do 50 znaków
   EN: Identity Takeoff Ticket - ver.3
   PL: Bilet Skoku Rozwoju Tożsamości - ver.3
313. [Przedmioty, sklep i profil gracza [236] — opis] 사용 시, 인격의 레벨이 60, 동기화 단계가 4단계까지 증가한다.
   źródło: Items-a1c9p1.json :: dataList[id=236].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 60, and Uptie Tier up to Tier 4.
   PL: Po użyciu podnosi poziom Tożsamości do 60, a Stopień Synchronizacji do 4.
314. [Przedmioty, sklep i profil gracza [236] — tekst klimatyczny] 이 티켓은 찢어야 사용된다.\n어떤 차원이나 시공간을 찢어너머 인격의 성장을 비정상적인 속도로 동기화시키며 성장시킨다.\n티켓은 왜 찢기거나 구멍이 뚫리는 등의 손상을 통해서만 그 사용가치를 다하는 것일까.
   źródło: Items-a1c9p1.json :: dataList[id=236].flavor
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tear this ticket to activate it.\nIt tears through spacetime, uptying and enhancing an Identity at a ridiculous speed.\nTearing in half, punching a hole through—why are the means of extracting the full worth of tickets always so destructive?
   PL: Ten bilet trzeba rozdarć, by zadziałał.\nRozdziera wymiar lub czasoprzestrzeń, by w nienormalnym tempie synchronizować i rozwijać Tożsamość.\nCzemu bilet spełnia swoje przeznaczenie tylko przez zniszczenie — rozdarcie czy dziurę?
315. [Przedmioty, sklep i profil gracza [503] — nazwa] 시즌 3 인격 선택권
   źródło: Items-a1c9p1.json :: dataList[id=503].name
   limit: do 40 znaków
   EN: Nominable S3 Identity Ticket
   PL: Bilet Wyboru Tożsamości Sezonu 3
316. [Przedmioty, sklep i profil gracza [503] — opis] 사용 시, 시즌 3 인격(이벤트 포함) 중 하나를 선택하여 획득할 수 있다.
   źródło: Items-a1c9p1.json :: dataList[id=503].desc
   limit: do 120 znaków
   EN: Use this item to select a Season 3 Identity(including Event Identities) to obtain.
   PL: Po użyciu można wybrać jedną z Tożsamości Sezonu 3 (w tym Tożsamości Wydarzeń), by ją otrzymać.
317. [Przedmioty, sklep i profil gracza [503] — tekst klimatyczny] LCB팀의 황금가지를 쫓는 여로에서 특정 시점의 인격 중 하나를 관측하여 끌어낼 수 있는 티켓.\n'인격을 추출할 수 있는 범위가 LCB의 여정과 황금가지의 수복에 영향을 받는 것은 확실합니다.\n다만 궁금한 것은 LCB의 여정이 중요한 것일지, 아니면 황금가지 수복 정도가 중요한 것 일지군요.\n그 범위의 제약만 없어진다면 어쩌면…'-LCA 거울세계관측부서 거울 연구원
   źródło: Items-a1c9p1.json :: dataList[id=503].flavor
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket capable of observing and drawing out an Identity of a certain point in time during the LCB team's pursuit of the Golden Boughs.\n"The LCB's journey and Golden Bough restoration progress both affect the range of extractable Identities, that much is certain. What I'm really curious to find out is... which is more important? The LCB's journey, or the Golden Bough restoration progress? If we can somehow remove or circumvent these constraints, then maybe...' - LCA Mirror World Observatorium Department Mirror Researcher
   PL: Bilet pozwalający zaobserwować i wyciągnąć jedną z Tożsamości z określonego punktu podróży zespołu LCB za Złotymi Gałęziami.\n„Pewne jest, że zakres wydobywalnych Tożsamości zależy od wędrówki LCB i postępu odbudowy Złotych Gałęzi.\nCiekawi mnie jednak, co jest ważniejsze: wędrówka LCB, czy stopień odbudowy Gałęzi.\nGdyby tylko tę granicę móc znieść… może…” - Badacz Lustra, Obserwatorium Światów Lustra, Dział LCA
318. [Przedmioty, sklep i profil gracza [703] — nazwa] 3주년 기념 인격 선택권
   źródło: Items-a1c9p1.json :: dataList[id=703].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 3rd Anniversary\nNominable Identity Ticket
   PL: Bilet Wyboru Tożsamości\n3. Rocznicy
319. [Przedmioty, sklep i profil gracza [703] — opis] 사용 시, 시즌 7 시작 이전에 출시된 인격 (상시 인격과 이벤트를 포함한 시즌 1 ~ 시즌 6 인격) 중 하나를 선택하여 획득할 수 있다.\n(※ 발푸르기스의 밤 인격과 시즌 7 시작 이후에 출시된 인격의 경우, 획득 불가)
   źródło: Items-a1c9p1.json :: dataList[id=703].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use this item to obtain an Identity released prior to Season 7 commencement. (Standard Fare Identities & Identities from Season 1~6, including Event Identities)\n(※ Post-Season 7 commencement Identities and Walpurgis Night Identities cannot be obtained via this item)
   PL: Po użyciu można wybrać jedną z Tożsamości wydanych przed rozpoczęciem Sezonu 7 (Tożsamości Standardowe oraz Tożsamości Sezonów 1–6, w tym Tożsamości Wydarzeń), by ją otrzymać.\n(※ Tożsamości Nocy Walpurgii oraz Tożsamości wydane po rozpoczęciu Sezonu 7 są niedostępne)
320. [Przedmioty, sklep i profil gracza [703] — tekst klimatyczny] LCB팀의 황금가지를 쫓는 여로에서 특정 시점의 인격 중 하나를 관측하여 끌어낼 수 있는 티켓.\n'그냥 이런 기념 티켓이란거 계속 찍어낼 수는 없는 거야? 애초에 이 티켓은 누가 만드는 건데?\n어디 티켓나무에서라도 열리는… 뭐… 당신들 누구야!'-LCA 거울세계관측부서 거울 신입 연구원
   źródło: Items-a1c9p1.json :: dataList[id=703].flavor
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket capable of observing and drawing out an Identity of a certain point in time during the LCB team's pursuit of Golden Boughs.\n"Sure, it's an "Anniversary" ticket. But can't they just keep printing and mass-producing these things? Who even makes them in the first place? What, do these tickets grow on ticket trees or someth—whoa, hey! Who the hell are you people?!" - LCA Mirror World Observatorium Department Mirror Researcher(trainee)
   PL: Bilet pozwalający zaobserwować i wyciągnąć jedną z Tożsamości z określonego punktu podróży zespołu LCB za Złotymi Gałęziami.\n„No dobrze, „rocznicowy”. Ale czy nie da się ich po prostu drukować na potęgę? Kto je w ogóle produkuje? Co, rosną na drzewach biletowych, czy jak—ej, nio! Kto wy w ogóle jesteście?! ” - Badacz Lustra (Stażysta), Obserwatorium Światów Lustra, Dział LCA

## Przedmioty, sklep i profil gracza: Items-egoFifth
- plik gry: `Items-egoFifth.json`

321. [Przedmioty, sklep i profil gracza [202] — nazwa] 해석사슬
   źródło: Items-egoFifth.json :: dataList[id=202].name
   limit: do 40 znaków
   EN: Spinchains
   PL: Łańcuchy Splotu
322. [Przedmioty, sklep i profil gracza [202] — opis] 환상 해석 5단계를 진행할 때 사용한다.
   źródło: Items-egoFifth.json :: dataList[id=202].desc
   limit: do 120 znaków
   EN: Used for the Threadspinning of E.G.O to Tier V.
   PL: Służy do Splotu Nici E.G.O do Stopnia 5.
323. [Przedmioty, sklep i profil gracza [202] — tekst klimatyczny] 누군가를, 무언가를 해석한다는 것은 적극적으로 들여다보는 일. 그러기 위해서는 묶여있는 사슬을 풀어내야만 한다.\n하지만 이 사슬은 이미 내 시선으로 태어나졌으니, 금방에 다시 대상을 묶어버릴 것이다.\n사슬을 파헤치고 끊어내어 본질이란 것을 마주한다 해도 이윽고 그것을 바라보며 이해하려는 순간 다시 사슬로 엮어진다.\n그러나 이것이 의미가 없는 일은 아닐 것이다. 사슬은 이전과 다른 사슬이며, 우리는 사슬이란 것이 묶어내 준 형태 없이는 무언가를 인식할 수 없을 테니. 이것은 그렇게 만들어진 사슬에서 떨어져 나온 사슬의 일부.\n- ‘사슬에 사슬이 감길 수도 있나?’
   źródło: Items-egoFifth.json :: dataList[id=202].flavor
   limit: do 1080 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To decipher a person—or an object—is not to skim the surface with a passing glance, but to let one's gaze pierce through it. For that to be possible, the chains wrapped around the object must first be undone, link by link.\n\nHowever, it was by the gaze of the beholder that these chains were birthed to begin with. Even if one were to claw their way beneath them, tear them apart, and stand before what might be called the "essence" of things, the very first attempt to comprehend it would coil the chains back around the object and bind it once more.\nNonetheless, the attempt is not without merit; the chains remade would not be the same as they were before, and without the forms these chains bound into being, the concept of perception itself would not exist.\nThis is a link broken loose from a greater whole.\n\n- 'Can a chain be wound around another chain?'
   PL: Rozszyfrowywać kogoś — czy coś — to nie rzucić pół spojrzenia, lecz wpuścić wzrok w głąb. A by to było możliwe, łańcuchy owinięte wokół celu trzeba najpierw rozplątać, ogniwo po ogniwie.\n\nJednak to właśnie spojrzenie patrzącego powołało te łańcuchy do życia. Choćby ktoś podziobił się pod nie, rozerwał je i stanął twarzą w twarz z tym, co można by nazwać „istotą” rzeczy — pierwsza próba zrozumienia owinie łańcuchy z powrotem i zwiąże cel na nowo.\nNiemniej próba nie jest pozbawiona sensu; łańcuchy odtworzone nie będą tymi samymi, a bez form, które łańcuchy wiążą, samo pojęcie percepcji by nie istniało.\nTo ogniwo oderwane od większej całości.\n\n- „Czy łańcuch może być owinięty innym łańcuchem?”

## Przedmioty, sklep i profil gracza: Items-fools
- plik gry: `Items-fools.json`

324. [Przedmioty, sklep i profil gracza [9001] — nazwa] 꼬미의 선물
   źródło: Items-fools.json :: dataList[id=9001].name
   limit: do 40 znaków
   EN: Kkomi's Gift
   PL: Prezent od Kkomiego
325. [Przedmioty, sklep i profil gracza [9001] — opis] 사용 시, 무료 광기 401개를 획득한다.
   źródło: Items-fools.json :: dataList[id=9001].desc
   limit: do 120 znaków
   EN: Open to receive 401 Free Lunacy.
   PL: Po użyciu otrzymujesz 401 Darmowego Szaleństwa.
326. [Przedmioty, sklep i profil gracza [9001] — tekst klimatyczny] 희한한 꿈을 꾼 것 같다. 솜 주먹으로 때린 것에 대한 미안함인지 꼬미가 건네주고 간 한봄 밤의 선물. "꼬미, 다음에 또 보재" - 베르길리우스
   źródło: Items-fools.json :: dataList[id=9001].flavor
   limit: do 250 znaków
   EN: It's like waking up from the strangest dream. It's Kkomi's midspring night's apology gift, probably for beating the crap out of us with those plush fists. "Kkomi says seeya later" - Vergilius
   PL: Jakbym obudził się z najdziwniejszego snu. Apologetyczny prezent Kkomiego z połowy wiosny — pewnie za te ciosy pluszowymi pięściami. „Kkomi mówi: to do zobaczenia” - Vergilius

## Przedmioty, sklep i profil gracza: Items-x1p1c1
- plik gry: `Items-x1p1c1.json`

327. [Przedmioty, sklep i profil gracza [9002] — nazwa] 삑뚤픽뚫 롤링페이퍼
   źródło: Items-x1p1c1.json :: dataList[id=9002].name
   limit: do 60 znaków
   EN: Sinnerlings' Chicken-scratch Farewells
   PL: Skrobane Pożegnania Grzeszników
328. [Przedmioty, sklep i profil gracza [9002] — opis] 사용 시, 무료 광기 401개를 획득한다.
   źródło: Items-x1p1c1.json :: dataList[id=9002].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Przedmioty, sklep i profil gracza [9002] — tekst klimatyczny] 어지러운 꿈을 꾼 것만 같다. 병 안에는 아이들이 적은 듯 삐뚤빼뚤하게 감사를 표하는 것만 같은 쪽지들이 있었다. …그런데 왜 우리 수감자들이 떠오르지? 아직 잠이 덜 깼나.
   źródło: Items-x1p1c1.json :: dataList[id=9002].flavor
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's like waking up from the most chaotic dream. The jar contains several notes of sincere appreciation, scribbled in children's messy chicken scratches.\n\n... Why does this remind me of the Sinners? I must still be waking up.
   PL: Jakbym obudził się z najbardziej chaotycznego snu. W słoiku kilka notatek z serdecznymi podziękowaniami, wykrzaczanymi dziecinnym pismem.\n\n…Czemu przypominają mi moje Grzeszników? Chyba jeszcze nie dospane.

## Przedmioty, sklep i profil gracza: Items
- plik gry: `Items.json`

330. [Przedmioty, sklep i profil gracza [1] — nazwa] 유료 광기
   źródło: Items.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Paid Lunacy
   PL: Płatne Szaleństwo
331. [Przedmioty, sklep i profil gracza [1] — opis] 장미 모양으로 형상화된 결정체. 추출을 진행하거나 엔케팔린 박스를 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=1].desc
   limit: do 130 znaków
   EN: A rose-shaped crystalline material. Used for performing extractions and purchasing Enkephalin boxes.
   PL: Kryształ w kształcie róży. Służy do Ekstrakcji oraz zakupu Skrzynek Enkefaliny.
332. [Przedmioty, sklep i profil gracza [1] — tekst klimatyczny] 늘 어디론가 향하는 것만 같은 장미. 마치 인간과 같은 그것은 어느 강물을 머금어 꽃 피운다고 한다.
   źródło: Items.json :: dataList[id=1].flavor
   limit: do 200 znaków
   EN: A crystal rose that seems to be facing a certain direction at all times. This humanlike object is said to absorb the moisture from a certain river to bloom.
   PL: Kryształowa róża, która zdaje się wciąż patrzeć w jednym kierunku. Ta ludzka rzecz, jak powiadają, zakwita, napiwszy się wód pewnej rzeki.
333. [Przedmioty, sklep i profil gracza [2] — nazwa] 무료 광기
   źródło: Items.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Free Lunacy
   PL: Darmowe Szaleństwo
334. [Przedmioty, sklep i profil gracza [2] — opis] 장미 모양으로 형상화된 결정체. 추출을 진행하거나 엔케팔린 박스를 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=2].desc
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Przedmioty, sklep i profil gracza [2] — tekst klimatyczny] 늘 어디론가 향하는 것만 같은 장미. 마치 인간과 같은 그것은 어느 강물을 머금어 꽃 피운다고 한다.
   źródło: Items.json :: dataList[id=2].flavor
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Przedmioty, sklep i profil gracza [3] — nazwa] 광기
   źródło: Items.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Lunacy
   PL: Szaleństwo
337. [Przedmioty, sklep i profil gracza [3] — opis] 장미 모양으로 형상화된 결정체. 추출을 진행하거나 엔케팔린 박스를 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=3].desc
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Przedmioty, sklep i profil gracza [3] — tekst klimatyczny] 사람은 광기를 머금고 나서야 나아갈 수 있다.
   źródło: Items.json :: dataList[id=3].flavor
   limit: do 120 znaków
   EN: Embracing the madness is a necessary step for humans to move forward.
   PL: Człowiek może iść naprzód dopiero wtedy, gdy wchłonie Szaleństwo.
339. [Przedmioty, sklep i profil gracza [11] — nazwa] 엔케팔린 모듈
   źródło: Items.json :: dataList[id=11].name
   limit: do 40 znaków
   EN: Enkephalin Module
   PL: Moduł Enkefaliny
340. [Przedmioty, sklep i profil gracza [11] — opis] 던전을 입장할 때 사용한다.
   źródło: Items.json :: dataList[id=11].desc
   limit: do 120 znaków
   EN: Used for entering dungeons.
   PL: Służy do wstępu do Lochów.
341. [Przedmioty, sklep i profil gracza [11] — tekst klimatyczny] 특수 격리를 위한 밀폐 소재로 만들어진 구 형태의 모듈.\n[안내] 액화 엔케팔린을 일정량 투입하는 것으로, 기존의 불안정한 기화 엔케팔린 보다 안정적인 활용이 가능합니다.\n지정된 소켓에 모듈을 결합하는 것으로 엔케팔린을 에너지로 전환할 수 있습니다.\n[주의] 한 번 모듈화된 엔케팔린은 비가역적이며, 오직 소켓을 통한 소모용으로만 사용 가능합니다.\n용도 외의 사용 및 개조를 엄금합니다.
   źródło: Items.json :: dataList[id=11].flavor
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A spherical module designed for special containment.\n[NOTE] Utilizing a dosage of liquid Enkephalin allows for more stable usage compared to its gaseous form.\nThe Enkephalin can be converted into energy by plugging the module into a designated socket.\n[CAUTION] Modularization of Enkephalin is an irreversible process; the module may only be expended via a socket.\nUsage outside of intended purposes or modification is strictly forbidden.
   PL: Kulisty moduł zaprojektowany do specjalnej izolacji.\n[INFORMACJA] Dozowanie Enkefaliny w postaci płynnej zapewnia stabilniejsze użycie niż postać gazowa.\nEnkefalinę można przekształcić w energię, wsuwając moduł do wyznaczonego gniazda.\n[OSTRZEŻENIE] Modułowanie Enkefaliny jest procesem nieodwracalnym; moduł może być zużyty wyłącznie przez gniazdo.\nStosowanie niezgodne z przeznaczeniem oraz modyfikacje są surowo zabronione.
342. [Przedmioty, sklep i profil gracza [101] — nazwa] 추출 티켓
   źródło: Items.json :: dataList[id=101].name
   limit: do 40 znaków
   EN: Extraction Ticket
   PL: Bilet Ekstrakcji
343. [Przedmioty, sklep i profil gracza [101] — opis] 추출을 1회 진행할 수 있다.
   źródło: Items.json :: dataList[id=101].desc
   limit: do 120 znaków
   EN: Can be used to perform 1 extraction.
   PL: Pozwala dokonać 1 Ekstrakcji.
344. [Przedmioty, sklep i profil gracza [101] — tekst klimatyczny] 메피스토펠레스의 추출 동력원인 광기를 엮어 짜낸 소모성 지급품.\n얇은 종이처럼 보이지만, 무언가 내부에서 끈덕지게 박동하는 것만 같다.
   źródło: Items.json :: dataList[id=101].flavor
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A consumable item weaved from Lunacy, the source of Mephistopheles’ extractive energy.\nIt looks like a thin sheet of paper at a glance, but something seems to be pulsating inside.
   PL: Jednorazowa racja splatana ze Szaleństwa — źródła energii ekstrakcyjnej Mephistophelesa.\nNa pierwszy rzut oka cienka jak kartka, lecz coś wewnątrz zdaje się uparcie pulsować.
345. [Przedmioty, sklep i profil gracza [102] — nazwa] 추출 10회 티켓
   źródło: Items.json :: dataList[id=102].name
   limit: do 40 znaków
   EN: Decaextraction Ticket
   PL: Bilet Dekaekstrakcji
346. [Przedmioty, sklep i profil gracza [102] — opis] 추출을 10회 진행할 수 있다.
   źródło: Items.json :: dataList[id=102].desc
   limit: do 120 znaków
   EN: Can be used to perform 10 extractions.
   PL: Pozwala dokonać 10 Ekstrakcji.
347. [Przedmioty, sklep i profil gracza [102] — tekst klimatyczny] 메피스토펠레스의 추출 동력원인 광기를 엮어 짜낸 소모성 지급품.\n얇은 종이처럼 보이지만, 무언가 내부에서 끈덕지게 박동하는 것만 같다.
   źródło: Items.json :: dataList[id=102].flavor
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Przedmioty, sklep i profil gracza [103] — nazwa] 3성 인격 출현 추출 티켓
   źródło: Items.json :: dataList[id=103].name
   limit: do 50 znaków
   EN: 3★ Guarantee Decaextraction Ticket
   PL: Bilet Dekaekstrakcji Gwarantowanej 3★
349. [Przedmioty, sklep i profil gracza [103] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 3성 인격이 확정으로 등장한다.
   źródło: Items.json :: dataList[id=103].desc
   limit: do 120 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ pojawia się na pewno.
350. [Przedmioty, sklep i profil gracza [103] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items.json :: dataList[id=103].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Przedmioty, sklep i profil gracza [104] — nazwa] 시즌 1 - 3성 인격 출현 추출 티켓
   źródło: Items.json :: dataList[id=104].name
   limit: do 70 znaków
   EN: [Season 1] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 1] Bilet Dekaekstrakcji Gwarantowanej 3★
352. [Przedmioty, sklep i profil gracza [104] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 1에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items.json :: dataList[id=104].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 1] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 1] pojawia się na pewno.
353. [Przedmioty, sklep i profil gracza [104] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items.json :: dataList[id=104].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Przedmioty, sklep i profil gracza [105] — nazwa] 시즌 2 - 3성 인격 출현 추출 티켓
   źródło: Items.json :: dataList[id=105].name
   limit: do 70 znaków
   EN: [Season 2] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 2] Bilet Dekaekstrakcji Gwarantowanej 3★
355. [Przedmioty, sklep i profil gracza [105] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 2에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items.json :: dataList[id=105].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 2] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 2] pojawia się na pewno.
356. [Przedmioty, sklep i profil gracza [105] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items.json :: dataList[id=105].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Przedmioty, sklep i profil gracza [106] — nazwa] 시즌 3 - 3성 인격 출현 추출 티켓
   źródło: Items.json :: dataList[id=106].name
   limit: do 70 znaków
   EN: [Season 3] 3★ Guarantee Decaextraction Ticket
   PL: [Sezon 3] Bilet Dekaekstrakcji Gwarantowanej 3★
358. [Przedmioty, sklep i profil gracza [106] — opis] 추출을 10회 진행할 수 있으며, 이 중에서 시즌 3에 해당하는 3성 인격이 확정으로 등장한다.
   źródło: Items.json :: dataList[id=106].desc
   limit: do 130 znaków
   EN: Can be used to perform 10 extractions where one 3★ Identity from [Season 3] is guaranteed to appear.
   PL: Pozwala dokonać 10 Ekstrakcji, z których jedna Tożsamość 3★ z [Sezonu 3] pojawia się na pewno.
359. [Przedmioty, sklep i profil gracza [106] — tekst klimatyczny] 추출 티켓 위에 어떤 표식이 찍혀있는 특수한 물건. 희박한 가능성의 세계에 있는 인격을 확정적으로 추출할 수 있다. 종이는 격렬하게 요동치고 박동하고 있다.
   źródło: Items.json :: dataList[id=106].flavor
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Przedmioty, sklep i profil gracza [201] — nazwa] 끈
   źródło: Items.json :: dataList[id=201].name
   limit: do 40 znaków
   EN: Thread
   PL: Nić
361. [Przedmioty, sklep i profil gracza [201] — opis] 인격의 동기화나 E.G.O의 환상 해석을 진행할 때 사용한다.
   źródło: Items.json :: dataList[id=201].desc
   limit: do 120 znaków
   EN: Used for the Uptying of Identities and Threadspinning of E.G.O.
   PL: Służy do Synchronizacji Tożsamości oraz Splotu Nici E.G.O.
362. [Przedmioty, sklep i profil gracza [201] — tekst klimatyczny] 끈, 그것은 실의 형태로 모든 가능성을 하나로 엮어내기 위한 것입니다.\n우리 회사에서는, 이것을 여러 방식으로 활용해 인격을 동기화하거나 환상 해석을 할 때 사용하고 있습니다.
   źródło: Items.json :: dataList[id=201].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thread is a string-like object conceived to tie all possibilities into one place.\nOur company is utilizing Thread in various ways, such as Uptying Identities or Threadspinning E.G.O to better understand it.
   PL: Nić — coś w rodzaju sznura, stworzonego, by spleść wszystkie możliwości w jedno.\nNasza firma wykorzystuje Nić na różne sposoby — do Synchronizacji Tożsamości czy Splotu Nici E.G.O — by lepiej ją zgłębić.
363. [Przedmioty, sklep i profil gracza [211] — nazwa] 인격 학습 티켓 I
   źródło: Items.json :: dataList[id=211].name
   limit: do 40 znaków
   EN: Identity Training Ticket I
   PL: Bilet Treningu Tożsamości I
364. [Przedmioty, sklep i profil gracza [211] — opis] 사용 시, 인격의 경험치가 50만큼 증가한다.
   źródło: Items.json :: dataList[id=211].desc
   limit: do 120 znaków
   EN: Gives 50 Identity XP.
   PL: Daje 50 PD Tożsamości.
365. [Przedmioty, sklep i profil gracza [211] — tekst klimatyczny] 겪었던, 겪고 있는, 겪을 가능성이 서린 티켓.\n"경험하지 않았던 생각이 어느새 머리를 파고들어 와 있었소."
   źródło: Items.json :: dataList[id=211].flavor
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket bearing possibilities of the past, present, and future.\n“I found that a thought of something I’d never experienced planted itself firmly in my head.”
   PL: Bilet przesiąknięty możliwościami przeszłości, teraźniejszości i przyszłości.\n„Niepoznana myśl wdoła mi się w głowę, zanim zdążyłem mrugnąć.”
366. [Przedmioty, sklep i profil gracza [212] — nazwa] 인격 학습 티켓 II
   źródło: Items.json :: dataList[id=212].name
   limit: do 40 znaków
   EN: Identity Training Ticket II
   PL: Bilet Treningu Tożsamości II
367. [Przedmioty, sklep i profil gracza [212] — opis] 사용 시, 인격의 경험치가 200만큼 증가한다.
   źródło: Items.json :: dataList[id=212].desc
   limit: do 120 znaków
   EN: Gives 200 Identity XP.
   PL: Daje 200 PD Tożsamości.
368. [Przedmioty, sklep i profil gracza [212] — tekst klimatyczny] 겪었던, 겪고 있는, 겪을 가능성이 서린 티켓.\n"으음~ 나는 남쪽 도시에 가본 적이 없는데, 왜 익숙한 기분이 느껴지지...?"
   źródło: Items.json :: dataList[id=212].flavor
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket bearing possibilities of the past, present, and future.\n“Hmhm~ I’ve never been to the southern quarter before, so why does it feel so familiar…?”
   PL: Bilet przesiąknięty możliwościami przeszłości, teraźniejszości i przyszłości.\n„Mmm~ Nigdy nie byłem w południowej dzielnicy, to czemu wydaje mi się tak znajoma…?”
369. [Przedmioty, sklep i profil gracza [213] — nazwa] 인격 학습 티켓 III
   źródło: Items.json :: dataList[id=213].name
   limit: do 40 znaków
   EN: Identity Training Ticket III
   PL: Bilet Treningu Tożsamości III
370. [Przedmioty, sklep i profil gracza [213] — opis] 사용 시, 인격의 경험치가 1000만큼 증가한다.
   źródło: Items.json :: dataList[id=213].desc
   limit: do 120 znaków
   EN: Gives 1000 Identity XP.
   PL: Daje 1000 PD Tożsamości.
371. [Przedmioty, sklep i profil gracza [213] — tekst klimatyczny] 겪었던, 겪고 있는, 겪을 가능성이 서린 티켓.\n"...이런 편리한 걸 과거에 얻을 수 있었더라면, 그 지옥 같던 고비들을 편리하게 넘길 수 있었을 텐데요."
   źródło: Items.json :: dataList[id=213].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket bearing possibilities of the past, present, and future.\n“…If I could have had such a convenient thing in the past, those nightmarish plights would’ve been so simple to overcome.”
   PL: Bilet przesiąknięty możliwościami przeszłości, teraźniejszości i przyszłości.\n„…Gdybym miał coś tak wygodnego w przeszłości, te koszmarne opresje przeszłyby o wiele łatwiej.”
372. [Przedmioty, sklep i profil gracza [214] — nazwa] 인격 학습 티켓 IV
   źródło: Items.json :: dataList[id=214].name
   limit: do 40 znaków
   EN: Identity Training Ticket IV
   PL: Bilet Treningu Tożsamości IV
373. [Przedmioty, sklep i profil gracza [214] — opis] 사용 시, 인격의 경험치가 3000만큼 증가한다.
   źródło: Items.json :: dataList[id=214].desc
   limit: do 120 znaków
   EN: Gives 3000 Identity XP.
   PL: Daje 3000 PD Tożsamości.
374. [Przedmioty, sklep i profil gracza [214] — tekst klimatyczny] 겪었던, 겪고 있는, 겪을 가능성이 서린 티켓.\n"겪은 적이 없었던 기억이 강제로 채워지는 느낌입니다. 그다지 유쾌하지는 않지만, 지극히 효율적이라고 할 수 있습니다."
   źródło: Items.json :: dataList[id=214].flavor
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Ticket shimmering with possibilities we experienced, are experiencing, and will experience.\n"This is a feeling not unlike getting memories we did not experience forced into us. This is not the most pleasant feeling, but it is certainly efficient.
   PL: Bilet migoczący możliwościami przeżytymi, przeżywanymi i tymi, które nadejdą.\n„To uczucie niczym wspomnienia, których nie przeżyliśmy, wciskane siłą do głowy. Mało przyjemne, ale bezdyskusyjnie wydajne.”
375. [Przedmioty, sklep i profil gracza [221] — nazwa] 인격 특수 강화 티켓 I
   źródło: Items.json :: dataList[id=221].name
   limit: do 40 znaków
   EN: Level Boost Ticket I
   PL: Bilet Specjalnego Wzmocnienia I
376. [Przedmioty, sklep i profil gracza [221] — opis] 사용 시, 인격의 레벨이 10까지 증가한다.
   źródło: Items.json :: dataList[id=221].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 10.
   PL: Po użyciu podnosi poziom Tożsamości do 10.
377. [Przedmioty, sklep i profil gracza [221] — tekst klimatyczny] 인격 학습 티켓이 초과 경험을 할 수 있게 만드는 제한 해제형 티켓.\n"오오!! 그 어느 때 보다 정의를 구현하기에 걸맞은 몸이 되었군!"
   źródło: Items.json :: dataList[id=221].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limit-disengaging ticket that allows an Identity to hold excess experience.\n“Oho! Mine frame hath become more apt than ever to enact justice!”
   PL: Bilet z odblokowanym limitem — pozwala Tożsamości gromadzić nadwyżkę doświadczenia.\n„Oho! To ciało godniejsze jest niż kiedykolwiek, by sprawiedliwość wcielać!”
378. [Przedmioty, sklep i profil gracza [222] — nazwa] 인격 특수 강화 티켓 II
   źródło: Items.json :: dataList[id=222].name
   limit: do 40 znaków
   EN: Level Boost Ticket II
   PL: Bilet Specjalnego Wzmocnienia II
379. [Przedmioty, sklep i profil gracza [222] — opis] 사용 시, 인격의 레벨이 20까지 증가한다.
   źródło: Items.json :: dataList[id=222].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 20.
   PL: Po użyciu podnosi poziom Tożsamości do 20.
380. [Przedmioty, sklep i profil gracza [222] — tekst klimatyczny] 인격 학습 티켓이 초과 경험을 할 수 있게 만드는 제한 해제형 티켓.\n"이상하게... 마음이 안정되는 기분이에요. 예전에 못했던걸... 해낼 수 있을 것만 같고요."
   źródło: Items.json :: dataList[id=222].flavor
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limit-disengaging ticket that allows an Identity to hold excess experience.\n“It’s… strangely calming. I feel like I can do things I couldn’t before.”
   PL: Bilet z odblokowanym limitem — pozwala Tożsamości gromadzić nadwyżkę doświadczenia.\n„Dziwnie… uspokaja. Czuję, że dam radę z tym, czego kiedyś nie potrafiłem.”
381. [Przedmioty, sklep i profil gracza [223] — nazwa] 인격 특수 강화 티켓 III
   źródło: Items.json :: dataList[id=223].name
   limit: do 40 znaków
   EN: Level Boost Ticket III
   PL: Bilet Specjalnego Wzmocnienia III
382. [Przedmioty, sklep i profil gracza [223] — opis] 사용 시, 인격의 레벨이 30까지 증가한다.
   źródło: Items.json :: dataList[id=223].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 30.
   PL: Po użyciu podnosi poziom Tożsamości do 30.
383. [Przedmioty, sklep i profil gracza [223] — tekst klimatyczny] 인격 학습 티켓이 초과 경험을 할 수 있게 만드는 제한 해제형 티켓.\n"이런 게 전쟁 때도 있었다면 곤란했겠어. 몇 초 만에 짬이 차게 만드는 기술이라니 말이야."
   źródło: Items.json :: dataList[id=223].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limit-disengaging ticket that allows an Identity to hold excess experience.\n“This thing would’ve been a real menace if it was available during wartime. Imagine fostering veterans in mere seconds.”
   PL: Bilet z odblokowanym limitem — pozwala Tożsamości gromadzić nadwyżkę doświadczenia.\n„To by było groźne narzędzie na wojnie. Wyobraź sobie: weterani w kilka sekund.”
384. [Przedmioty, sklep i profil gracza [224] — nazwa] 인격 특수 강화 티켓 IV
   źródło: Items.json :: dataList[id=224].name
   limit: do 40 znaków
   EN: Level Boost Ticket IV
   PL: Bilet Specjalnego Wzmocnienia IV
385. [Przedmioty, sklep i profil gracza [224] — opis] 사용 시, 인격의 레벨이 40까지 증가한다.
   źródło: Items.json :: dataList[id=224].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 40.
   PL: Po użyciu podnosi poziom Tożsamości do 40.
386. [Przedmioty, sklep i profil gracza [224] — tekst klimatyczny] 인격 학습 티켓이 초과 경험을 할 수 있게 만드는 제한 해제형 티켓.\n"사. 기. 다.  사용한 적 없던 기예를 다년간 익힌 것 처럼 만든다니, 보람이라는 것이 사라지는 기분이다. 역겹군."
   źródło: Items.json :: dataList[id=224].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limit-disengaging ticket that allows an Identity to hold excess experience. \n"O.P. To give me years of experience in using a technique I've never used before...  there is no satisfaction here. Revolting."
   PL: Bilet z odblokowanym limitem — pozwala Tożsamości gromadzić nadwyżkę doświadczenia.\n„Ś. C. E. M. A. Lata doświadczenia w technice, której nigdy nie używałem… satysfakcji tu brak. Odrażające.”
387. [Przedmioty, sklep i profil gracza [231] — nazwa] 인격 성장 도약 티켓
   źródło: Items.json :: dataList[id=231].name
   limit: do 40 znaków
   EN: Identity Takeoff Ticket
   PL: Bilet Skoku Rozwoju Tożsamości
388. [Przedmioty, sklep i profil gracza [231] — opis] 사용 시, 인격의 레벨이 40, 동기화 단계가 4단계까지 증가한다.
   źródło: Items.json :: dataList[id=231].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 40, and Uptie Tier up to Tier 4.
   PL: Po użyciu podnosi poziom Tożsamości do 40, a Stopień Synchronizacji do 4.
389. [Przedmioty, sklep i profil gracza [231] — tekst klimatyczny] 이 티켓은 찢어야 사용된다.\n어떤 차원이나 시공간을 찢어너머 인격의 성장을 비정상적인 속도로 동기화 시키며 성장시킨다.\n찢는 소리가 중독적이어서 여러 개를 찢고 싶어진다고 한다.
   źródło: Items.json :: dataList[id=231].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tear this ticket to activate it.\nIt tears through the space-time, uptying and enhancing an Identity at a ridiculous speed.\nIt makes a pretty addicting sound when it tears; makes one want to tear more tickets.
   PL: Ten bilet trzeba rozdarć, by zadziałał.\nRozdziera wymiar lub czasoprzestrzeń, by w nienormalnym tempie synchronizować i rozwijać Tożsamość.\nPodobno dźwięk rozdzierania uzależnia — jednego biletu mało, chce się rwać kolejne.
390. [Przedmioty, sklep i profil gracza [301] — nazwa] 엔케팔린 박스
   źródło: Items.json :: dataList[id=301].name
   limit: do 40 znaków
   EN: Enkephalin Box
   PL: Skrzynka Enkefaliny
391. [Przedmioty, sklep i profil gracza [301] — opis] 사용 시, 엔케팔린을 60만큼 회복한다.
   źródło: Items.json :: dataList[id=301].desc
   limit: do 120 znaków
   EN: Recovers 60 Enkephalin when used.
   PL: Po użyciu odnawia 60 Enkefaliny.
392. [Przedmioty, sklep i profil gracza [301] — tekst klimatyczny] 액화 엔케팔린을 안정 보관하고 있는 컨테이너 박스.\n[주의] 정해진 절차를 따르지 않은 채 본 박스를 취급할 경우, 엔케팔린 누출 등의 사고를 초래할 수 있습니다.\n엔케팔린의 부적절한 흡입은 여러 검증되지 않은 정신 병리적 현상을 유발할 수 있습니다.
   źródło: Items.json :: dataList[id=301].flavor
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A stable container storing liquid Enkephalin.\n[CAUTION] Handling this box without following the prescribed procedures may result in accidents such as Enkephalin leakage.\nUnregulated ingestion of Enkephalin may cause a wide range of unverified psychopathological symptoms.
   PL: Stabilny pojemnik do przechowywania Enkefaliny w postaci płynnej.\n[OSTRZEŻENIE] Obchodzenie się z tym pudełkiem bez zachowania ustalonych procedur może skutkować wypadkami, w tym wyciekiem Enkefaliny.\nNiekontrolowane wdychanie Enkefaliny może wywołać całą gamę nieweryfikowanych objawów psychopatologicznych.
393. [Przedmioty, sklep i profil gracza [401] — nazwa] 끈 상자
   źródło: Items.json :: dataList[id=401].name
   limit: do 40 znaków
   EN: Thread Crate
   PL: Skrzynka Nici
394. [Przedmioty, sklep i profil gracza [401] — opis] 사용 시, 끈을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=401].desc
   limit: do 120 znaków
   EN: Open to receive 1-3 strands of Thread.
   PL: Po użyciu otrzymujesz 1–3 Nici.
395. [Przedmioty, sklep i profil gracza [401] — tekst klimatyczny] 가능성이 다발로 놓여있는 상자.\n얼만큼의 가능성을 이끌어 낼 수 있는지는 아무도 모른다.
   źródło: Items.json :: dataList[id=401].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A crate of bundled possibilities.\nNo one knows how much you can draw from it.
   PL: Skrzynia pełna związanych w kłębki możliwości.\nNikt nie wie, ile z niej wyciągniesz.
396. [Przedmioty, sklep i profil gracza [1101] — nazwa] 시즌 1 자아 파편 상자
   źródło: Items.json :: dataList[id=1101].name
   limit: do 40 znaków
   EN: [Season 1] Egoshard Crate
   PL: [Sezon 1] Skrzynia Odłamków E.G.O
397. [Przedmioty, sklep i profil gracza [1101] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=1101].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Przedmioty, sklep i profil gracza [1101] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items.json :: dataList[id=1101].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Przedmioty, sklep i profil gracza [1201] — nazwa] 시즌 1 자아 파편 선택 상자
   źródło: Items.json :: dataList[id=1201].name
   limit: do 50 znaków
   EN: [Season 1] Nominable Egoshard Crate
   PL: [Sezon 1] Skrzynia Wyboru Odłamków E.G.O
400. [Przedmioty, sklep i profil gracza [1201] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=1201].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Przedmioty, sklep i profil gracza [1201] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items.json :: dataList[id=1201].flavor
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Przedmioty, sklep i profil gracza [1102] — nazwa] 시즌 2 자아 파편 상자
   źródło: Items.json :: dataList[id=1102].name
   limit: do 40 znaków
   EN: [Season 2] Egoshard Crate
   PL: [Sezon 2] Skrzynia Odłamków E.G.O
403. [Przedmioty, sklep i profil gracza [1102] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=1102].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Przedmioty, sklep i profil gracza [1102] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items.json :: dataList[id=1102].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Przedmioty, sklep i profil gracza [1202] — nazwa] 시즌 2 자아 파편 선택 상자
   źródło: Items.json :: dataList[id=1202].name
   limit: do 50 znaków
   EN: [Season 2] Nominable Egoshard Crate
   PL: [Sezon 2] Skrzynia Wyboru Odłamków E.G.O
406. [Przedmioty, sklep i profil gracza [1202] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=1202].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Przedmioty, sklep i profil gracza [1202] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items.json :: dataList[id=1202].flavor
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Przedmioty, sklep i profil gracza [1103] — nazwa] 시즌 3 자아 파편 상자
   źródło: Items.json :: dataList[id=1103].name
   limit: do 40 znaków
   EN: [Season 3] Egoshard Crate
   PL: [Sezon 3] Skrzynia Odłamków E.G.O
409. [Przedmioty, sklep i profil gracza [1103] — opis] 사용 시, 무작위 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=1103].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Przedmioty, sklep i profil gracza [1103] — tekst klimatyczny] 수감자의 자아 파편을 무작위로 채집해 상자에 봉인했다. 누가 들어있을지 아무도 모른다.\n조용한 곳에서 들고 있으면 자그마한 소란이 들리는 것 같기도 하다.
   źródło: Items.json :: dataList[id=1103].flavor
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Przedmioty, sklep i profil gracza [1203] — nazwa] 시즌 3 자아 파편 선택 상자
   źródło: Items.json :: dataList[id=1203].name
   limit: do 50 znaków
   EN: [Season 3] Nominable Egoshard Crate
   PL: [Sezon 3] Skrzynia Wyboru Odłamków E.G.O
412. [Przedmioty, sklep i profil gracza [1203] — opis] 사용 시, 선택한 수감자의 자아 파편을 1~3개 획득한다.
   źródło: Items.json :: dataList[id=1203].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Przedmioty, sklep i profil gracza [1203] — tekst klimatyczny] 수감자의 자아 파편 중 원하는 것을 획득할 수 있는 상자.\n파우스트에 의하면, 상자를 개봉하는 관리자의 선택에 의해 확정된다고 한다.
   źródło: Items.json :: dataList[id=1203].flavor
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Przedmioty, sklep i profil gracza [10101] — nazwa] 시즌1 이상 자아 파편
   źródło: Items.json :: dataList[id=10101].name
   limit: do 50 znaków
   EN: [Season 1] Yi Sang’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Yi Sanga
415. [Przedmioty, sklep i profil gracza [10101] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10101].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Przedmioty, sklep i profil gracza [10101] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10101].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Przedmioty, sklep i profil gracza [10201] — nazwa] 시즌1 파우스트 자아 파편
   źródło: Items.json :: dataList[id=10201].name
   limit: do 40 znaków
   EN: [Season 1] Faust’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Faust
418. [Przedmioty, sklep i profil gracza [10201] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10201].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Przedmioty, sklep i profil gracza [10201] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10201].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Przedmioty, sklep i profil gracza [10301] — nazwa] 시즌1 돈키호테 자아 파편
   źródło: Items.json :: dataList[id=10301].name
   limit: do 50 znaków
   EN: [Season 1] Don Quixote’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Don Quixote
421. [Przedmioty, sklep i profil gracza [10301] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10301].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Przedmioty, sklep i profil gracza [10301] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10301].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Przedmioty, sklep i profil gracza [10401] — nazwa] 시즌1 료슈 자아 파편
   źródło: Items.json :: dataList[id=10401].name
   limit: do 40 znaków
   EN: [Season 1] Ryōshū’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Ryōshū
424. [Przedmioty, sklep i profil gracza [10401] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10401].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Przedmioty, sklep i profil gracza [10401] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10401].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fleeting moments from any point in the Sinner's time condensed into physical form. The shards float in the air.\nPossibilities are transient things; they drift in the realm of uncertainty unless seized.
   PL: Ulotne chwile Grzeszników uwięzione w postaci fizycznej. Odłamki unoszą się w powietrzu.\nMożliwości są ulotne; dryfują w sferze niepewności, dopóki ktoś ich nie chwyci.
426. [Przedmioty, sklep i profil gracza [10501] — nazwa] 시즌1 뫼르소 자아 파편
   źródło: Items.json :: dataList[id=10501].name
   limit: do 50 znaków
   EN: [Season 1] Meursault’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Meursault
427. [Przedmioty, sklep i profil gracza [10501] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10501].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Przedmioty, sklep i profil gracza [10501] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10501].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Przedmioty, sklep i profil gracza [10601] — nazwa] 시즌1 홍루 자아 파편
   źródło: Items.json :: dataList[id=10601].name
   limit: do 50 znaków
   EN: [Season 1] Hong Lu’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Hong Lu
430. [Przedmioty, sklep i profil gracza [10601] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10601].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Przedmioty, sklep i profil gracza [10601] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10601].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Przedmioty, sklep i profil gracza [10701] — nazwa] 시즌1 히스클리프 자아 파편
   źródło: Items.json :: dataList[id=10701].name
   limit: do 50 znaków
   EN: [Season 1] Heathcliff’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Heathcliffa
433. [Przedmioty, sklep i profil gracza [10701] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10701].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Przedmioty, sklep i profil gracza [10701] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10701].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Przedmioty, sklep i profil gracza [10801] — nazwa] 시즌1 이스마엘 자아 파편
   źródło: Items.json :: dataList[id=10801].name
   limit: do 50 znaków
   EN: [Season 1] Ishmael’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Ishmael
436. [Przedmioty, sklep i profil gracza [10801] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10801].desc
   limit: do 120 znaków
   EN: Used for purchasing Ishmael's Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Ishmael w Automacie.
437. [Przedmioty, sklep i profil gracza [10801] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10801].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Przedmioty, sklep i profil gracza [10901] — nazwa] 시즌1 로쟈 자아 파편
   źródło: Items.json :: dataList[id=10901].name
   limit: do 40 znaków
   EN: [Season 1] Rodion’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Rodion
439. [Przedmioty, sklep i profil gracza [10901] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10901].desc
   limit: do 120 znaków
   EN: Used for purchasing Rodya's Identities, E.G.O, and Thread from the Dispenser.
   PL: Służy do zakupu Tożsamości, E.G.O lub Nici Rodion w Automacie.
440. [Przedmioty, sklep i profil gracza [10901] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10901].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Przedmioty, sklep i profil gracza [11001] — nazwa] 시즌1 싱클레어 자아 파편
   źródło: Items.json :: dataList[id=11001].name
   limit: do 50 znaków
   EN: [Season 1] Sinclair’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Sinclair
442. [Przedmioty, sklep i profil gracza [11001] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11001].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Przedmioty, sklep i profil gracza [11001] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11001].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Przedmioty, sklep i profil gracza [11101] — nazwa] 시즌1 오티스 자아 파편
   źródło: Items.json :: dataList[id=11101].name
   limit: do 40 znaków
   EN: [Season 1] Outis’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Outis
445. [Przedmioty, sklep i profil gracza [11101] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11101].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Przedmioty, sklep i profil gracza [11101] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11101].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Przedmioty, sklep i profil gracza [11201] — nazwa] 시즌1 그레고르 자아 파편
   źródło: Items.json :: dataList[id=11201].name
   limit: do 40 znaków
   EN: [Season 1] Gregor’s Egoshard
   PL: [Sezon 1] Odłamek E.G.O Gregora
448. [Przedmioty, sklep i profil gracza [11201] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11201].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Przedmioty, sklep i profil gracza [11201] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11201].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Przedmioty, sklep i profil gracza [10001] — nazwa] 시즌1 [선택한 수감자] 자아 파편
   źródło: Items.json :: dataList[id=10001].name
   limit: do 60 znaków
   EN: Season 1 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 1 [Wybranego Grzesznika]
451. [Przedmioty, sklep i profil gracza [10102] — nazwa] 시즌2 이상 자아 파편
   źródło: Items.json :: dataList[id=10102].name
   limit: do 50 znaków
   EN: [Season 2] Yi Sang’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Yi Sanga
452. [Przedmioty, sklep i profil gracza [10102] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10102].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Przedmioty, sklep i profil gracza [10102] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10102].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Przedmioty, sklep i profil gracza [10202] — nazwa] 시즌2 파우스트 자아 파편
   źródło: Items.json :: dataList[id=10202].name
   limit: do 40 znaków
   EN: [Season 2] Faust’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Faust
455. [Przedmioty, sklep i profil gracza [10202] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10202].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Przedmioty, sklep i profil gracza [10202] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10202].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Przedmioty, sklep i profil gracza [10302] — nazwa] 시즌2 돈키호테 자아 파편
   źródło: Items.json :: dataList[id=10302].name
   limit: do 50 znaków
   EN: [Season 2] Don Quixote’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Don Quixote
458. [Przedmioty, sklep i profil gracza [10302] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10302].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Przedmioty, sklep i profil gracza [10302] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10302].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Przedmioty, sklep i profil gracza [10402] — nazwa] 시즌2 료슈 자아 파편
   źródło: Items.json :: dataList[id=10402].name
   limit: do 40 znaków
   EN: [Season 2] Ryōshū’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Ryōshū
461. [Przedmioty, sklep i profil gracza [10402] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10402].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Przedmioty, sklep i profil gracza [10402] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10402].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Przedmioty, sklep i profil gracza [10502] — nazwa] 시즌2 뫼르소 자아 파편
   źródło: Items.json :: dataList[id=10502].name
   limit: do 50 znaków
   EN: [Season 2] Meursault’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Meursault
464. [Przedmioty, sklep i profil gracza [10502] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10502].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Przedmioty, sklep i profil gracza [10502] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10502].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Przedmioty, sklep i profil gracza [10602] — nazwa] 시즌2 홍루 자아 파편
   źródło: Items.json :: dataList[id=10602].name
   limit: do 50 znaków
   EN: [Season 2] Hong Lu’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Hong Lu
467. [Przedmioty, sklep i profil gracza [10602] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10602].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Przedmioty, sklep i profil gracza [10602] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10602].flavor
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Przedmioty, sklep i profil gracza [10702] — nazwa] 시즌2 히스클리프 자아 파편
   źródło: Items.json :: dataList[id=10702].name
   limit: do 50 znaków
   EN: [Season 2] Heathcliff’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Heathcliffa
470. [Przedmioty, sklep i profil gracza [10702] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10702].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Przedmioty, sklep i profil gracza [10702] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10702].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Przedmioty, sklep i profil gracza [10802] — nazwa] 시즌2 이스마엘 자아 파편
   źródło: Items.json :: dataList[id=10802].name
   limit: do 50 znaków
   EN: [Season 2] Ishmael’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Ishmael
473. [Przedmioty, sklep i profil gracza [10802] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10802].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Przedmioty, sklep i profil gracza [10802] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10802].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Przedmioty, sklep i profil gracza [10902] — nazwa] 시즌2 로쟈 자아 파편
   źródło: Items.json :: dataList[id=10902].name
   limit: do 40 znaków
   EN: [Season 2] Rodion’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Rodion
476. [Przedmioty, sklep i profil gracza [10902] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10902].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Przedmioty, sklep i profil gracza [10902] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10902].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Przedmioty, sklep i profil gracza [11002] — nazwa] 시즌2 싱클레어 자아 파편
   źródło: Items.json :: dataList[id=11002].name
   limit: do 50 znaków
   EN: [Season 2] Sinclair’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Sinclair
479. [Przedmioty, sklep i profil gracza [11002] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11002].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Przedmioty, sklep i profil gracza [11002] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11002].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Przedmioty, sklep i profil gracza [11102] — nazwa] 시즌2 오티스 자아 파편
   źródło: Items.json :: dataList[id=11102].name
   limit: do 40 znaków
   EN: [Season 2] Outis’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Outis
482. [Przedmioty, sklep i profil gracza [11102] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11102].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Przedmioty, sklep i profil gracza [11102] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11102].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Przedmioty, sklep i profil gracza [11202] — nazwa] 시즌2 그레고르 자아 파편
   źródło: Items.json :: dataList[id=11202].name
   limit: do 40 znaków
   EN: [Season 2] Gregor’s Egoshard
   PL: [Sezon 2] Odłamek E.G.O Gregora
485. [Przedmioty, sklep i profil gracza [11202] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11202].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Przedmioty, sklep i profil gracza [11202] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11202].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Przedmioty, sklep i profil gracza [10103] — nazwa] 시즌3 이상 자아 파편
   źródło: Items.json :: dataList[id=10103].name
   limit: do 50 znaków
   EN: [Season 3] Yi Sang’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Yi Sanga
488. [Przedmioty, sklep i profil gracza [10103] — opis] 자판기에서 이상의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10103].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Przedmioty, sklep i profil gracza [10103] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10103].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Przedmioty, sklep i profil gracza [10203] — nazwa] 시즌3 파우스트 자아 파편
   źródło: Items.json :: dataList[id=10203].name
   limit: do 40 znaków
   EN: [Season 3] Faust’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Faust
491. [Przedmioty, sklep i profil gracza [10203] — opis] 자판기에서 파우스트의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10203].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Przedmioty, sklep i profil gracza [10203] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10203].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Przedmioty, sklep i profil gracza [10303] — nazwa] 시즌3 돈키호테 자아 파편
   źródło: Items.json :: dataList[id=10303].name
   limit: do 50 znaków
   EN: [Season 3] Don Quixote’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Don Quixote
494. [Przedmioty, sklep i profil gracza [10303] — opis] 자판기에서 돈키호테의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10303].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Przedmioty, sklep i profil gracza [10303] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10303].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Przedmioty, sklep i profil gracza [10403] — nazwa] 시즌3 료슈 자아 파편
   źródło: Items.json :: dataList[id=10403].name
   limit: do 40 znaków
   EN: [Season 3] Ryōshū’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Ryōshū
497. [Przedmioty, sklep i profil gracza [10403] — opis] 자판기에서 료슈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10403].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Przedmioty, sklep i profil gracza [10403] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10403].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Przedmioty, sklep i profil gracza [10503] — nazwa] 시즌3 뫼르소 자아 파편
   źródło: Items.json :: dataList[id=10503].name
   limit: do 50 znaków
   EN: [Season 3] Meursault’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Meursault
500. [Przedmioty, sklep i profil gracza [10503] — opis] 자판기에서 뫼르소의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10503].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Przedmioty, sklep i profil gracza [10503] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10503].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Przedmioty, sklep i profil gracza [10603] — nazwa] 시즌3 홍루 자아 파편
   źródło: Items.json :: dataList[id=10603].name
   limit: do 50 znaków
   EN: [Season 3] Hong Lu’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Hong Lu
503. [Przedmioty, sklep i profil gracza [10603] — opis] 자판기에서 홍루의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10603].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Przedmioty, sklep i profil gracza [10603] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10603].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Przedmioty, sklep i profil gracza [10703] — nazwa] 시즌3 히스클리프 자아 파편
   źródło: Items.json :: dataList[id=10703].name
   limit: do 50 znaków
   EN: [Season 3] Heathcliff’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Heathcliffa
506. [Przedmioty, sklep i profil gracza [10703] — opis] 자판기에서 히스클리프의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10703].desc
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Przedmioty, sklep i profil gracza [10703] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10703].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Przedmioty, sklep i profil gracza [10803] — nazwa] 시즌3 이스마엘 자아 파편
   źródło: Items.json :: dataList[id=10803].name
   limit: do 50 znaków
   EN: [Season 3] Ishmael’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Ishmael
509. [Przedmioty, sklep i profil gracza [10803] — opis] 자판기에서 이스마엘의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10803].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Przedmioty, sklep i profil gracza [10803] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10803].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Przedmioty, sklep i profil gracza [10903] — nazwa] 시즌3 로쟈 자아 파편
   źródło: Items.json :: dataList[id=10903].name
   limit: do 40 znaków
   EN: [Season 3] Rodion’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Rodion
512. [Przedmioty, sklep i profil gracza [10903] — opis] 자판기에서 로쟈의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=10903].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Przedmioty, sklep i profil gracza [10903] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=10903].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Przedmioty, sklep i profil gracza [11003] — nazwa] 시즌3 싱클레어 자아 파편
   źródło: Items.json :: dataList[id=11003].name
   limit: do 50 znaków
   EN: [Season 3] Sinclair’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Sinclair
515. [Przedmioty, sklep i profil gracza [11003] — opis] 자판기에서 싱클레어의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11003].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Przedmioty, sklep i profil gracza [11003] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11003].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Przedmioty, sklep i profil gracza [11103] — nazwa] 시즌3 오티스 자아 파편
   źródło: Items.json :: dataList[id=11103].name
   limit: do 40 znaków
   EN: [Season 3] Outis’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Outis
518. [Przedmioty, sklep i profil gracza [11103] — opis] 자판기에서 오티스의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11103].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Przedmioty, sklep i profil gracza [11103] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11103].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Przedmioty, sklep i profil gracza [11203] — nazwa] 시즌3 그레고르 자아 파편
   źródło: Items.json :: dataList[id=11203].name
   limit: do 40 znaków
   EN: [Season 3] Gregor’s Egoshard
   PL: [Sezon 3] Odłamek E.G.O Gregora
521. [Przedmioty, sklep i profil gracza [11203] — opis] 자판기에서 그레고르의 인격 혹은 E.G.O나 끈을 구입할 때 사용한다.
   źródło: Items.json :: dataList[id=11203].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Przedmioty, sklep i profil gracza [11203] — tekst klimatyczny] 수감자들의 언젠가가 조각의 형태로 구현된 것. 조각은 떠다닌다.\n가능성은 쥐지 않으면 가능성인 채로 그저 떠다니기 때문일 것이다.
   źródło: Items.json :: dataList[id=11203].flavor
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Przedmioty, sklep i profil gracza [10002] — nazwa] 시즌2 [선택한 수감자] 자아 파편
   źródło: Items.json :: dataList[id=10002].name
   limit: do 60 znaków
   EN: Season 2 [Selected Sinner]’s Egoshard
   PL: Odłamek E.G.O Sezonu 2 [Wybranego Grzesznika]
524. [Przedmioty, sklep i profil gracza [4] — nazwa] 이상 [理想]
   źródło: Items.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Yisang [Ideality]
   PL: Yi Sang [理想]
525. [Przedmioty, sklep i profil gracza [20001] — nazwa] 버스 개조용 폐품
   źródło: Items.json :: dataList[id=20001].name
   limit: do 40 znaków
   EN: Bus-modifying Scrap
   PL: Złom do Modyfikacji Autobusu
526. [Przedmioty, sklep i profil gracza [20001] — opis] 크<size=110%>랲</size>게에게서 뜯어낸 녹슨 철판이나 볼트 따위.\n메피스토펠레스를 개조하는 데 사용할 수 있다는 것 같다
   źródło: Items.json :: dataList[id=20001].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>, \n
   EN: Miscellaneous junk like rusted plates and bolts ripped from the backs of trash crabs.\nCould be used for modifying Mephistopheles.
   PL: Rdza blach, śruby i tym podobne — oderwane od pleców <size=110%>krab</size>ów śmietnikowych.\nPodobno nadaje się do modyfikacji Mephistophelesa.
527. [Przedmioty, sklep i profil gracza [20002] — nazwa] 희귀한 말굽이 포함된 버스 개조용 폐품
   źródło: Items.json :: dataList[id=20002].name
   limit: do 60 znaków
   EN: Rare Horseshoe with Bus-modifying Scrap
   PL: Złom do Modyfikacji Autobusu z Rzadką Podkową
528. [Przedmioty, sklep i profil gracza [20002] — opis] 킹크<size=110%>랲</size>게에게서 얻어낸 커다란 폐품. 말굽 모양으로 보인다.\n여러 개의 폐품이 해야할 역할을 대신할 수 있다는 것 같다.
   źródło: Items.json :: dataList[id=20002].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <size=110%>, </size>, \n
   EN: A large horseshoe-shaped item taken from the king trash crab.\nIt could substitute several pieces of scrap, or so we're told.
   PL: Duży przedmiot w kształcie podkowy, wyjęty od króla <size=110%>krab</size>ów śmietnikowych.\nPodobno może zastąpić kilka kawałków złomu naraz.
529. [Przedmioty, sklep i profil gracza [5] — nazwa] 자아 파편
   źródło: Items.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Egoshards
   PL: Odłamki E.G.O
530. [Przedmioty, sklep i profil gracza [20009] — nazwa] 장식 꾸러미
   źródło: Items.json :: dataList[id=20009].name
   limit: do 40 znaków
   EN: Trinkets Sack
   PL: Worek Ozdób
531. [Przedmioty, sklep i profil gracza [20009] — opis] 선물 공장에 여기저기 널려있던 꾸밀 거리를 급하게 쑤셔넣은 보따리.\n돈키호테가 메피스토펠레스를 꾸밀 때 유용하게 쓰일 것 같다.
   źródło: Items.json :: dataList[id=20009].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A sack full of trinkets and decorations hastily taken from the Gift Factory.\nDon Quixote will make good use of these to spruce up the Mephistopheles' interiors.
   PL: Toreba naprędce wypchana ozdobami porozrzucanymi po Fabryce Prezentów.\nDon Quixote świetnie je wykorzysta, by przyozdobić wnętrza Mephistophelesa.
532. [Przedmioty, sklep i profil gracza [20010] — nazwa] 거대한 장식 꾸러미
   źródło: Items.json :: dataList[id=20010].name
   limit: do 40 znaków
   EN: Huge Trinkets Sack
   PL: Ogromny Worek Ozdób
533. [Przedmioty, sklep i profil gracza [20010] — opis] 선물 공장에 장식용으로 쓰일 예정이었던 꾸밀 거리가 어마어마하게 많이 들어가 있는 보따리.\n돈키호테가 메피스토펠레스를 꾸밀 때 유용하게 쓰일 것 같다.
   źródło: Items.json :: dataList[id=20010].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A huge sack filled to the brim with trinkets and decorations from the Gift Factory.\nDon Quixote will make good use of these to spruce up the Mephistopheles' interiors.
   PL: Toreba zapełniona po brzegi ozdobami przeznaczonymi na Fabrykę Prezentów.\nDon Quixote świetnie je wykorzysta, by przyozdobić wnętrza Mephistophelesa.
534. [Przedmioty, sklep i profil gracza [20012] — nazwa] 피에 절은 검집
   źródło: Items.json :: dataList[id=20012].name
   limit: do 40 znaków
   EN: Bloodied Scabbard
   PL: Pochwa Nasiąknięta Krwią
535. [Przedmioty, sklep i profil gracza [20012] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>검을 휘둘러온 자들이 쓰러진 곳에 피에 절여진 검집이 남겨진다.\n검의 길을 가는 자들에게는 검집이야말로 그들의 집이다.</color>
   źródło: Items.json :: dataList[id=20012].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>Those who wield blades in life leave behind bloodied scabbards in death.\nThe true abode of those who walk the path of blades is their scabbard.</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Tam, gdzie padają ci, co machają ostrzami, zostaje pochwa nasiąknięta krwią.\nDla idących drogą miecza domem jest właśnie pochwa.</color>
536. [Przedmioty, sklep i profil gracza [20013] — nazwa] 한 서린 검집
   źródło: Items.json :: dataList[id=20013].name
   limit: do 40 znaków
   EN: Resentful Scabbard
   PL: Przepełniona Żalem Pochwa
537. [Przedmioty, sklep i profil gracza [20013] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>한이 맺힌 검을 휘둘러야 무릇 검귀라 한다.\n검귀에게 검집은 더 이상 필요하지 않으나, 집을 지니고 있는 까닭은 얕은 미련이 서린 한 때문이다.</color>
   źródło: Items.json :: dataList[id=20013].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>One who wields their blade with deep resentment is called a Demon of the Blade.\nDemon of the Blade no longer has need of a scabbard; yet they carry it, as that resentment is tinged with a lingering attachment.</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Ten, kto macha mieczem nasiąkniętym żalem, zwie się Demonem Ostrza.\nDemonowi Ostrza pochwa już niepotrzebna — nosi ją jednak, bo żal ten przetykany jest nikłym przywiązaniem.</color>
538. [Przedmioty, sklep i profil gracza [20017] — nazwa] 회중시계
   źródło: Items.json :: dataList[id=20017].name
   limit: do 40 znaków
   EN: Pocket Watch
   PL: Kieszonkowy Zegarek
539. [Przedmioty, sklep i profil gracza [20017] — opis] 모든 사람은 제각기 다른 속도로 움직이는 시계를 품고 살아간다.\n빠르게 흘러가는 시간, 느리게 흘러가는 시간.\n모두의 시간은 언제나 어긋나 있다.
   źródło: Items.json :: dataList[id=20017].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Everyone has their own timepiece, with varying time scales.\nTime that goes by quickly. Time that lingers.\nThe hours are always misaligned.
   PL: Każdy żyje z zegarem, który tyka w swoim rytmie.\nCzas płynący szybko. Czas płynący wolno.\nCzas wszystkich zawsze jest rozjechany.
540. [Przedmioty, sklep i profil gracza [20018] — nazwa] 회중시계 묶음
   źródło: Items.json :: dataList[id=20018].name
   limit: do 40 znaków
   EN: Pocket Watch Bundle
   PL: Zestaw Kieszonkowych Zegarków
541. [Przedmioty, sklep i profil gracza [20018] — opis] 결국 모든 시계는 같은 곳을 향한다.\n초침이 멈추고 숨이 멎는 순간, 비로소 모두의 시간은 같은 속도로 흘러간다.
   źródło: Items.json :: dataList[id=20018].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The same destination awaits every timepiece.\nThe hours finally align when the hands stop ticking down the seconds, when one breathes their final lungful of air.
   PL: Ostatecznie wszystkie zegarki dążą do tego samego.\nW chwili, gdy sekundnik zamiera i tchnienie ustaje, czas w końcu płynie w jednym tempie dla wszystkich.
542. [Przedmioty, sklep i profil gracza [20020] — nazwa] 일반 승객 복구팩
   źródło: Items.json :: dataList[id=20020].name
   limit: do 40 znaków
   EN: Civilian Recov. Pack
   PL: Pakiet Rekonstrukcyjny Cywila
543. [Przedmioty, sklep i profil gracza [20020] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>정리 요원들은 해당 팩에 승객 한 명분의 파편을 모아 넣어주시기를 바랍니다. 어떻게 정리해야 할지 막막한 승객도 작은 혈관 하나만큼으로 연결은 어떻게든 되어있으니, 인내심을 가지고 실을 감듯 하나하나 모아주세요.</color>
   źródło: Items.json :: dataList[id=20020].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>Notice to Cleanup Agents: please collect and store a single passenger's parts in this pack. No matter how difficult it may appear to collect their parts, do note that there is a single strand of vein connecting the passenger's parts together. Imagine you are spinning a yarn ball into shape, and patiently collect them one by one.</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Agenci Porządkowi: prosimy zbierać i przechowywać w tym pakiecie szczątki jednego pasażera. Choć zbieranie może sprawiać trudność, pamiętajcie — pojedyncza żyła łączy szczątki pasażera ze sobą. Wyobraźcie sobie nawijanie kłębka wełny i cierpliwie zbierajcie je jedno po drugim.</color>
544. [Przedmioty, sklep i profil gracza [20021] — nazwa] 해결사 승객 복구팩
   źródło: Items.json :: dataList[id=20021].name
   limit: do 40 znaków
   EN: Fixer Recov. Pack
   PL: Pakiet Rekonstrukcyjny Fiksera
545. [Przedmioty, sklep i profil gracza [20021] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 일반 승객 복구팩 20개로 전환된다.\n\n<color=#a16a3b>때로 의체를 장비한 승객들이 있습니다.\n전신 의체라 하더라도 승객의 뇌만큼은 존재합니다.\n승객의 뇌가 하나의 몸으로 인식했던 것이라면 워프 열차 안에서는 의체파편이라 해도 혈관이 이어져 있을 테니 걱정 안 하셔도 됩니다.\n피는 물보다 진하다는 점 기억해 주세요.</color>
   źródło: Items.json :: dataList[id=20021].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Civilian Recov. Pack immediately upon acquisition.\n\n<color=#a16a3b>On occasion, you may have to work on passengers equipped with prosthetics.\nPlease note that even full-body prosthetics do not remove the passenger's brain.\nAny prosthetic parts recognized by the brain as the passenger's own body will be connected by veins, so there is no need to worry about mix-and-matching them together.\nRemember: blood is thicker than water.</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Pakietów Rekonstrukcyjnych Cywila.\n\n<color=#a16a3b>Czasem trafią się pasażerowie w protezach.\nPamiętajcie: nawet pełna proteza nie usuwa mózgu pasażera.\nWszystko, co mózg uznaje za własne ciało, jest połączone żyłami — więc nie ma się czym martwić przy ich mieszaniu.\nPamiętajcie: krew jest gęstsza niż woda.</color>
546. [Przedmioty, sklep i profil gracza [232] — nazwa] 도약 모듈 - 인격 동기화
   źródło: Items.json :: dataList[id=232].name
   limit: do 40 znaków
   EN: Takeoff Module - ID Uptie
   PL: Moduł Skoku — Synchronizacja Tożsamości
547. [Przedmioty, sklep i profil gracza [232] — opis] 사용 시, 인격의 동기화 단계가 4단계까지 증가한다.
   źródło: Items.json :: dataList[id=232].desc
   limit: do 120 znaków
   EN: Raises an Identity’s Uptie Tier up to Tier 4.
   PL: Po użyciu podnosi Stopień Synchronizacji Tożsamości do 4.
548. [Przedmioty, sklep i profil gracza [232] — tekst klimatyczny] LCA 연구개발팀에서 제작한 첫 급속 인격 동기화 모듈.\n떨리고 빛나는 끈을 강제로 주입시키고 파편들을 엮어 특정 수준까지 동기화를 급가속시킨다.\n거울 밖에서는 모르겠지만, 그 거울 안에서는 파괴적인 주입이 단기간에 모든 것을 헤집으며 들이닥친다.
   źródło: Items.json :: dataList[id=232].flavor
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rapid Identity Uptie Module developed by LCA R&D Team.\nForcibly insert the shimmering threads and weave the shards together, rapidly raising the Uptie tier to a certain level.\nWhile those outside the mirror may not know, this devastating injection sweeps short-lived destruction through the mirror.
   PL: Moduł Błyskawicznej Synchronizacji Tożsamości opracowany przez zespół badawczo-rozwojowy LCA.\nWmusza drżące, lśniące nici i splata odłamki, gwałtownie podnosząc Synchronizację do ustalonego poziomu.\nCi spoza lustra mogą nie wiedzieć, lecz wewnątrz lustra to wyniszczające wstrzyknięcie zmiata wszystko w krótkiej chwili.
549. [Przedmioty, sklep i profil gracza [233] — nazwa] 도약 모듈 - E.G.O 해석 [WAW]
   źródło: Items.json :: dataList[id=233].name
   limit: do 60 znaków
   EN: Takeoff Module - E.G.O Spinning [WAW] x1
   PL: Moduł Skoku — Splot Nici E.G.O [WAW]
550. [Przedmioty, sklep i profil gracza [233] — opis] 사용 시, E.G.O의 환상 해석 단계가 4단계까지 증가한다. (최대 WAW 등급까지 적용 가능)
   źródło: Items.json :: dataList[id=233].desc
   limit: do 130 znaków
   EN: Raises an E.G.O's Threadspinning Tier up to Tier 4. (Usable only on E.G.Os WAW Level or lower)
   PL: Po użyciu podnosi Stopień Splotu Nici E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi WAW lub niższej)
551. [Przedmioty, sklep i profil gracza [233] — tekst klimatyczny] LCA 연구개발팀에서 제작한 첫 E.G.O 환상 해석 모듈.\n떨리고 빛나는 끈을 단기간에 대량의 파편들과 엮어 E.G.O의 해석을 특정 수준까지 급가속시킨다.\n환상이며 신비이기도 한 E.G.O를 편리 위주로 해석한다면... 언제까지 E.G.O라는 마음이 견뎌낼 수 있을지 아직은 미지수이다.
   źródło: Items.json :: dataList[id=233].flavor
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: E.G.O Threadspinning Module developed by LCA R&D Team.\nWeaves the shimmering threads with numerous shards, enhancing the E.G.O Threadspinning tier to a certain level at an accelerated pace.\nIt is yet to be known how much more of this pressure the heart known as E.G.O... can handle Threadspinning these Abnormal-Psychoment based E.G.Os so carelessly out of convenience.
   PL: Pierwszy moduł Splotu Nici E.G.O opracowany przez zespół badawczo-rozwojowy LCA.\nSplata drżące, lśniące nici z masą odłamków, przyspieszając Splot wybranego E.G.O do ustalonego poziomu.\nJeszcze nie wiadomo, ile tego nacisku serce zwane E.G.O znieść może, gdy tak lekkomyślnie Splata się te E.G.O zbudowane z Nienormalnych Psychomentów.
552. [Przedmioty, sklep i profil gracza [501] — nazwa] 시즌 1 인격 선택권
   źródło: Items.json :: dataList[id=501].name
   limit: do 40 znaków
   EN: Nominable S1 Identity Ticket
   PL: Bilet Wyboru Tożsamości Sezonu 1
553. [Przedmioty, sklep i profil gracza [501] — opis] 사용 시, 시즌 1 인격(이벤트 포함) 중 하나를 선택하여 획득할 수 있다.
   źródło: Items.json :: dataList[id=501].desc
   limit: do 120 znaków
   EN: Use this item to select a Season 1 Identity(including Event Identities) to obtain.
   PL: Po użyciu można wybrać jedną z Tożsamości Sezonu 1 (w tym Tożsamości Wydarzeń), by ją otrzymać.
554. [Przedmioty, sklep i profil gracza [501] — tekst klimatyczny] LCB팀의 황금가지를 쫓는 여로에서 특정 시점의 인격 중 하나를 관측하여 끌어낼 수 있는 티켓.\n'일정 기간 사이에서만 관측된 거울세계의 인격을 끌어올릴 수 있는 기술은 림버스컴퍼니의 비약적인 발전이라 할 수 있습니다. - LCA 거울세계관측부서 거울 연구원'
   źródło: Items.json :: dataList[id=501].flavor
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket capable of observing and drawing out an Identity of a particular period within the LCB team's pursuit of Golden Boughs.\n'The ability to target and pull up a specific period in which an Identity from an observed Mirror World demonstrates Limbus Company's vastly significant technological triumph. - LCA Mirror World Observatorium Department Mirror Researcher'
   PL: Bilet pozwalający zaobserwować i wyciągnąć jedną z Tożsamości z określonego punktu podróży zespołu LCB za Złotymi Gałęziami.\n„Technologia pozwalająca wyciągać Tożsamości Świata Lustra obserwowane wyłącznie w danym okresie zasługuje na miano skokowego rozwoju Limbus Company. - Badacz Lustra, Obserwatorium Światów Lustra, Dział LCA”
555. [Przedmioty, sklep i profil gracza [601] — nazwa] 시즌 1 배틀 패스 E.G.O 선택권
   źródło: Items.json :: dataList[id=601].name
   limit: do 60 znaków
   EN: Nominable S1 Battle Pass E.G.O Ticket
   PL: Bilet Wyboru E.G.O Przepustki Bitewnej Sezonu 1
556. [Przedmioty, sklep i profil gracza [601] — opis] 사용 시, 시즌 1 배틀 패스 E.G.O 중 하나를 선택하여 획득할 수 있다.
   źródło: Items.json :: dataList[id=601].desc
   limit: do 120 znaków
   EN: Use this item to select a Season 1 Battle Pass E.G.O to obtain.
   PL: Po użyciu można wybrać jedno z E.G.O Przepustki Bitewnej Sezonu 1, by je otrzymać.
557. [Przedmioty, sklep i profil gracza [601] — tekst klimatyczny] LCB팀의 황금가지를 쫓는 여로에서 특정 시점의 E.G.O중 하나를 관측하여 끌어낼 수 있는 티켓.\n'무작위한 E.G.O가 아닌 어느 시점에서 포착된 E.G.O를 저 밑에서부터 끌어올리는 건 인격을 골라내는 것보다 훨씬 어려운 연구죠 후후. - LCA 거울세계관측부서 관측 연구원'
   źródło: Items.json :: dataList[id=601].flavor
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A ticket capable of observing and drawing out an E.G.O of a particular period within the LCB team's pursuit of Golden Boughs.\n'Dragging up an E.G.O, observed within a specific period from the deep fathoms, is a much more complicated research than making Identities selectable. Fuhu. - LCA Mirror World Observatorium Department Observation Researcher'
   PL: Bilet pozwalający zaobserwować i wyciągnąć jedno z E.G.O z określonego punktu podróży zespołu LCB za Złotymi Gałęziami.\n„Wyciąganie z głębin E.G.O schwytanego w konkretnym okresie to o wiele trudniejsze badania niż wybieranie Tożsamości. Huhu. - Badacz Obserwacji, Obserwatorium Światów Lustra, Dział LCA”
558. [Przedmioty, sklep i profil gracza [12004] — nazwa] 시즌 4 동기화 · 환상해석 전용 파편 (공용)
   źródło: Items.json :: dataList[id=12004].name
   limit: do 80 znaków
   EN: Season 4 Uptie & Threadspinning only Shard (Universal)
   PL: Odłamek Sezonu 4 wyłącznie do Synchronizacji i Splotu Nici (Uniwersalny)
559. [Przedmioty, sklep i profil gracza [12004] — opis] 모든 수감자 인격의 동기화, E.G.O의 환상 해석을 진행할 때 사용할 수 있다.
   źródło: Items.json :: dataList[id=12004].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Przedmioty, sklep i profil gracza [12004] — tekst klimatyczny] 인격의 동기화, E.G.O의 환상해석을 진행할 때 수감자와 관계없이 공용으로 쓸 수 있는 파편.\n대신 이 파편을 아무리 모아도 인격이나 E.G.O를 추출할 수는 없다.\n'이 파편은 무엇이든 될 수 있는 황금가지에 대한 연구의 일환으로, 그 어떤 거울의 심상이나 세계에도 채워 넣을 수 있습니다. 네? 추출이요? 그건 당연히 안되죠. 어느 세계든 채워줄 수 있다는 것은 곧 어떤 세계도 처음부터 쌓아 올릴 수 없다는 것과 같으니까. - LCA 거울세계관측부서 수석 연구원'
   źródło: Items.json :: dataList[id=12004].flavor
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Przedmioty, sklep i profil gracza [234] — nazwa] 도약 모듈 - E.G.O 해석 [HE]
   źródło: Items.json :: dataList[id=234].name
   limit: do 60 znaków
   EN: Takeoff Module - E.G.O Spinning [HE] x1
   PL: Moduł Skoku — Splot Nici E.G.O [HE]
562. [Przedmioty, sklep i profil gracza [234] — opis] 사용 시, E.G.O의 환상 해석 단계가 4단계까지 증가한다. (최대 HE 등급까지 적용 가능)
   źródło: Items.json :: dataList[id=234].desc
   limit: do 130 znaków
   EN: Raises an E.G.O's Threadspinning Tier up to Tier 4. (Usable only on E.G.Os HE Level or lower)
   PL: Po użyciu podnosi Stopień Splotu Nici E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi HE lub niższej)
563. [Przedmioty, sklep i profil gracza [234] — tekst klimatyczny] LCA 연구개발팀에서 제작한 두번째 E.G.O 환상 해석 모듈. 떨리고 빛나는 끈을 단기간에 대량의 파편들과 엮어 [HE]급까지의 E.G.O의 해석을 특정 수준까지 급가속시킨다. 끈으로 파편을 엮어 실체를 짜낸다. 따스한 빛을 내는 끈은 어느날 오랫동안 도시를 비춘 빛과 닮아있다.
   źródło: Items.json :: dataList[id=234].flavor
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The second E.G.O Threadspinning Module developed by LCA R&D Team.\nWeaves the shimmering threads with numerous shards, enhancing the E.G.O Threadspinning tier of [HE]-level or lower E.G.O at an accelerated pace.\nWeave the shards together with the threads to compress together a form. The warm light of the threads is reminiscent of the light that had once showered the City for some time.
   PL: Drugi moduł Splotu Nici E.G.O opracowany przez zespół badawczo-rozwojowy LCA.\nSplata drżące, lśniące nici z masą odłamków, przyspieszając Splot E.G.O rangi [HE] lub niższej do ustalonego poziomu.\nSplot nici z odłamkami daje formę. Ciepłe światło nici przypomina to, które kiedyś przez długi czas zalewało Miasto.
564. [Przedmioty, sklep i profil gracza [20024] — nazwa] 정보서류
   źródło: Items.json :: dataList[id=20024].name
   limit: do 40 znaków
   EN: Amassed Data
   PL: Zgromadzone Dane
565. [Przedmioty, sklep i profil gracza [20024] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>LCE 주관으로 작성한 LCB, 뒤틀림, 죄종들에 대한 사소하고 번잡한 자료들. 여러 테스트, 실험, 조사 등이 되는대로 적힌 서류들이다.\n\n'자료 정리는 연구원의 소관이 아닐세. 조수의 업무 아니겠나.'</color>
   źródło: Items.json :: dataList[id=20024].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>Various disorganized and trivial documentation on LCB, Distortions, and the Peccatula are haphazardly scribbled here. These data have been collected by the LCE—messy records of tests, experiments, and research litter the papers.\n\n'It is not the duty of a researcher to organize their findings. That is the assistants' responsibility.'</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Rozmaite drobne, poukładane byle jak dokumenty o LCB, Wypaczeniach i Peccatula — spisane pod nadzorem LCE. Notatki z testów, eksperymentów i badań, gdzie się da.\n\n„Porządkowanie danych to nie zadanie badacza. To obowiązki asystenta.”</color>
566. [Przedmioty, sklep i profil gracza [20025] — nazwa] 기밀서류
   źródło: Items.json :: dataList[id=20025].name
   limit: do 40 znaków
   EN: Classified Data
   PL: Tajne Akta
567. [Przedmioty, sklep i profil gracza [20025] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 정보서류 20개로 전환된다.\n\n<color=#a16a3b>LCE의 보조 연구원들만 열람 가능한, 호엔하임이 수집한 기밀 자료들. 림버스 컴퍼니 수감자들의 개인적인 정보(생일, 출신 등)부터 LCE에서 보유한 환상체나 뒤틀림에 대한 심도 깊은 내용까지 빠짐없이 기록되어 있다.\n\n'자료는 나열된 것만으로는 가치가 없습니다. 무엇을 조합하고, 언제 공개하여, 어떻게 이용하는지가 중요하죠. 그제야 자료는 가치 있는 정보가 됩니다.' - LCA 간부 중 누군가</color>
   źródło: Items.json :: dataList[id=20025].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Amassed Data immediately upon acquisition.\n\n<color=#a16a3b>Classified data collected by Hohenheim himself, available for viewing only for LCE's assistant researchers. It contains all kinds of in-depth information about Limbus Company—from each Sinner's personal information(Birthdays, birthplaces, etc.) to analyses on Abnormalities and Distortions contained within the LCE.\n\n'The enumeration of data alone is worthless. What matters is which data connects to which, when they are unveiled, and how they are put to use. Only then is data transformed into intelligence of worth.' - Anonymous LCA Officer</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Zgromadzonych Danych.\n\n<color=#a16a3b>Poufne dane zebrane osobiście przez Hohenheima, dostępne do wglądu wyłącznie dla asystentów badawczych LCE. Od osobistych informacji Grzeszników Limbus Company (urodziny, pochodzenie i inne) po pogłębione analizy Abnormalności i Wypaczeń przechowywanych w LCE — zapisane niczego nie pomijając.\n\n„Dane same w sobie nic nie znaczą. Ważne jest to, co się z czym łączy, kiedy się to ujawni i jak się tego użyje. Dopiero wtedy dane stają się informacją o wartości.” - Któryś z oficerów LCA</color>
568. [Przedmioty, sklep i profil gracza [502] — nazwa] 시즌 2 인격 선택권
   źródło: Items.json :: dataList[id=502].name
   limit: do 40 znaków
   EN: Nominable S2 Identity Ticket
   PL: Bilet Wyboru Tożsamości Sezonu 2
569. [Przedmioty, sklep i profil gracza [502] — opis] 사용 시, 시즌 2 인격(이벤트 포함) 중 하나를 선택하여 획득할 수 있다.
   źródło: Items.json :: dataList[id=502].desc
   limit: do 120 znaków
   EN: Use this item to select a Season 2 Identity(including Event Identities) to obtain.
   PL: Po użyciu można wybrać jedną z Tożsamości Sezonu 2 (w tym Tożsamości Wydarzeń), by ją otrzymać.
570. [Przedmioty, sklep i profil gracza [502] — tekst klimatyczny] LCB팀의 황금가지를 쫓는 여로에서 특정 시점의 인격 중 하나를 관측하여 끌어낼 수 있는 티켓.\n'일정 기간 사이에서만 관측된 거울세계의 인격을 끌어올릴 수 있는 기술은 림버스컴퍼니의 비약적인 발전이라 할 수 있습니다. - LCA 거울세계관측부서 거울 연구원'
   źródło: Items.json :: dataList[id=502].flavor
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Przedmioty, sklep i profil gracza [235] — nazwa] 인격 성장 도약 티켓 - ver.2
   źródło: Items.json :: dataList[id=235].name
   limit: do 50 znaków
   EN: Identity Takeoff Ticket - ver.2
   PL: Bilet Skoku Rozwoju Tożsamości - ver.2
572. [Przedmioty, sklep i profil gracza [235] — opis] 사용 시, 인격의 레벨이 50, 동기화 단계가 4단계까지 증가한다.
   źródło: Items.json :: dataList[id=235].desc
   limit: do 120 znaków
   EN: Raises an Identity’s level to up to 50, and Uptie Tier up to Tier 4.
   PL: Po użyciu podnosi poziom Tożsamości do 50, a Stopień Synchronizacji do 4.
573. [Przedmioty, sklep i profil gracza [235] — tekst klimatyczny] 이 티켓은 찢어야 사용된다.\n어떤 차원이나 시공간을 찢어너머 인격의 성장을 비정상적인 속도로 동기화 시키며 성장시킨다.\n찢는 소리가 중독적이어서 여러 개를 찢고 싶어진다고 한다.
   źródło: Items.json :: dataList[id=235].flavor
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Przedmioty, sklep i profil gracza [20029] — nazwa] 청소부 액체 연료통
   źródło: Items.json :: dataList[id=20029].name
   limit: do 40 znaków
   EN: [Sweeper Fuel Cylinder]
   PL: Kanister Płynnego Paliwa Sprzątacza
575. [Przedmioty, sklep i profil gracza [20029] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>뒷골목의 밤마다 도시를 청소하는 청소부들의 연료가 담긴 통이에요. 매일같이 도시를 무대로 벌어지는 난장판 속에서도 청소부 덕분에 사람들은 아침마다 깨끗한 거리로 출근할 수 있죠. 청소부는 길가의 쓰레기나 허가받지 않은 건축물처럼 도시에 있어선 안될 것들을 액체 연료로 녹이며 물결을 이어갑니다. 이들은 정해진 시간마다 도시의 지하에서 올라오는데, 과연 얼마나 깊은 곳에서 오는 건지 궁금하네요. - 어느 LCCB 팀원의 인터뷰</color>
   źródło: Items.json :: dataList[id=20029].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>These fuel cylinders contain the energy source for the Sweepers, who cleanse the City every Night in the Backstreets. Despite the nightly chaos, people step out each morning to pristine streets on their way to work—all thanks to the Sweepers. Using their fluid fuel, they dissolve anything that doesn't belong in the City, from street litter to unauthorized structures, as they flood the streets at night. Like clockwork, they emerge from the subterranean depths beneath the City every night. I do wonder, though—just how deep do they come from? - Excerpt from an interview with an LCCB Employee</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>To cylindry z paliwem Sprzątaczy, którzy noc w noc czyszczą Miasto w Zaułkach. Mimo nocnych zamieszek dzięki nim ludzie każdego ranka wychodzą na czyste ulice, w drodze do pracy. Sprzątacze rozpuszczają w płynnym paliwie wszystko, czego w Mieście być nie powinno — jak śmieci czy nieautoryzowane zabudowania — i tak trwa dalej ta fala. Co noc, punktualnie, wynurzają się spod Miasta. Ciekawe tylko, z jakiej głębi? - Fragment wywiadu z pracownikiem LCCB</color>
576. [Przedmioty, sklep i profil gracza [20030] — nazwa] 특대형 액체 연료통
   źródło: Items.json :: dataList[id=20030].name
   limit: do 40 znaków
   EN: [Sweeper Fuel Tank]
   PL: Wielki Zbiornik Płynnego Paliwa
577. [Przedmioty, sklep i profil gracza [20030] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 청소부 액체 연료통 20개로 전환된다.\n\n<color=#a16a3b>청소부의 청소가 언제부터 시작되었고, 청소부가 어디에서 오는지에 대해선 아직도 많은 것이 베일에 싸여 있죠. 그들이 유일하게 협력하는 단체는 머리 뿐이라고 알려져 있으니까요. 청소부가 사용하는 액체 연료는 그들의 신체를 구성하는 물질이면서, 상대를 녹이는 융해 무기이며, 동시에 생존을 위한 영양분이기도 합니다. 개인적인 궁금증입니다만, 그들이 어떻게 개체수를 증식해왔는지 의문이네요. 아마 뒷골목의 밤에 아이들을 데려가거나, 외곽에 버려진 아이들을 납치하는 것이 그 단서가 되지 않을까 싶습니다. - 어느 LCCA 팀원의 인터뷰</color>
   źródło: Items.json :: dataList[id=20030].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Sweeper Fuel Cylinder immediately upon acquisition.\n\n<color=#a16a3b>Much about the Sweepers remains a mystery. When did they first begin their nightly labors? Where do they come from? It is said that the only institution they cooperate with is the Head. The Sweepers' fluid fuel is a multifunctional resource—it forms their bodies, serves as a weapon to dissolve whatever lies in their path, and sustains them. This is merely a personal curiosity, but I cannot help but wonder how they propagate. Perhaps they are the culprits behind reports of children vanishing during Nights in the Backstreets… or kidnappings from the Outskirts. - Excerpt from an interview with an LCCA Employee</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Kanistrów Płynnego Paliwa Sprzątacza.\n\n<color=#a16a3b>O Sprzątaczych wciąż wiele jest owiane tajemnicą. Kiedy rozpoczęli swoją nocną pracę? Skąd przychodzą? Podobno z instytucjami współpracują wyłącznie z Głową. Płynne paliwo Sprzątaczy buduje ich ciała, topi wrogów i służy za pokarm. Osobista ciekawostka: jak się rozmnażają? Może to ich sprawka — dzieci znikające w Nocach w Zaułkach… albo porywane na Obrzeżach. - Fragment wywiadu z pracownikiem LCCA</color>
578. [Przedmioty, sklep i profil gracza [30006] — nazwa] 영생의 별빛
   źródło: Items.json :: dataList[id=30006].name
   limit: do 40 znaków
   EN: Starlight of Immortality
   PL: Gwiezdny Blask Nieśmiertelności
579. [Przedmioty, sklep i profil gracza [30006] — opis] 거울 던전에서 사용된다.\n\n<color=#a16a3b>영생의 거울이 개방되는 동안 수집할 수 있는 별빛. 별빛들을 모아 이야기가 만들고 싶어도, 더 이상 하늘에 별이 없기에 사람은 땅으로 흩어진 별빛마저 긁어모은다.</color>
   źródło: Items.json :: dataList[id=30006].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used in Mirror Dungeons.\n\n<color=#a16a3b>Starlight that can be collected only as long as the Mirror of Immortality remains open. Wish as people might to weave new tales from Starlight, they can only scavenge for what earthbound Starlight there remains—for the stars in the sky are no more.</color>
   PL: Służy w Lustrzanych Lochach.\n\n<color=#a16a3b>Blask gwiazd, który można zbierać dopóty, dopóki Lustro Nieśmiertelności pozostaje otwarte. Ludzie, choćby chcieli utkać nowe opowieści z Gwiezdnego Blasku, muszą zgarniać ten, który został na ziemi — gwiazd na niebie już nie ma.</color>
580. [Przedmioty, sklep i profil gracza [30007] — nazwa] 이름과 거미의 별빛
   źródło: Items.json :: dataList[id=30007].name
   limit: do 50 znaków
   EN: Starlight of Names and Spiders
   PL: Gwiezdny Blask Imion i Pająków
581. [Przedmioty, sklep i profil gracza [30007] — opis] 거울 던전에서 사용된다.\n\n<color=#a16a3b>어느 기간 동안에만 수집할 수 있는 별빛. 하늘의 별을 바라본다. 바라보아져 떨어진 별들은 긁어모아진다. 그렇게 모아진 별들은 강제로 이어져, 이야기를 만들기 위해 빛을 내야만 한다.</color>
   źródło: Items.json :: dataList[id=30007].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used in Mirror Dungeons.\n\n<color=#a16a3b>Starlight that can be collected only within a fleeting span of time. The gaze is raised to the stars above. The stars beheld then fall, awaiting their gleaning. Harvested and tethered against their will, they are compelled to twinkle and shine, giving rise to new stories.</color>
   PL: Służy w Lustrzanych Lochach.\n\n<color=#a16a3b>Gwiezdny Blask, który można zbierać tylko przez ulotny czas. Wzrok uniesiony ku gwiazdom. Gwiazdy, które patrzyły, spadają, czekając na żniwiarza. Zebrane gwiazdy łączone są siłą — muszą lśnić, by rodziły nowe opowieści.</color>
582. [Przedmioty, sklep i profil gracza [30008] — nazwa] 시지프의 별빛
   źródło: Items.json :: dataList[id=30008].name
   limit: do 40 znaków
   EN: Starlight of Sisyphe
   PL: Gwiezdny Blask Sisyphe
583. [Przedmioty, sklep i profil gracza [30008] — opis] 거울 던전에서 사용된다.\n\n<color=#a16a3b>어느 기간 동안에만 수집할 수 있는 별빛. 하나하나 모인 별빛은 이윽고 다시 흩어진다. 반짝임과 사라짐이 언제까지 반복될지는 모른다. 그럼에도 우리는 다시금 별빛을 쌓아올리듯 그러모은다. 그리고 정상에 오른 이 별빛마저도 곧 굴러떨어지듯 사라질 것임을 당신은 분명 안다.</color>
   źródło: Items.json :: dataList[id=30008].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used in Mirror Dungeons.\n\n<color=#a16a3b>Starlight that can be collected only within a fleeting span of time. Starlights, gathered glint by glint, are destined to eventually scatter. Though no one knows how long this cycle of twinkling and fading will repeat, we continue to glean them into a neat pile. And all the same, once this starlight reaches the apex, it will soon disappear like a boulder rolling over the horizon, tumbling down the hill. You know this with absolute certainty.</color>
   PL: Służy w Lustrzanych Lochach.\n\n<color=#a16a3b>Gwiezdny Blask, który można zbierać tylko przez ulotny czas. Zebrany odłamka po odłamku, w końcu znów się rozprasza. Nikt nie wie, jak długo będzie się powtarzać ten cykl migotania i znikania. Mimo to znów gromadzimy Gwiezdny Blask, jakby układać go w stos. I tak samo dobrze wiesz, że i ten Blask, który doszedł na szczyt, wkrótce zniknie — jak głaz toczący się za horyzont, staczający się ze wzgórza.</color>
584. [Przedmioty, sklep i profil gracza [20034] — nazwa] 지·용·인 기초 입문서
   źródło: Items.json :: dataList[id=20034].name
   limit: do 40 znaków
   EN: Intro to Zhi, Yong, Ren
   PL: Wstęp do Zhi, Yong, Ren
585. [Przedmioty, sklep i profil gracza [20034] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>지혜로운 사람은 흔들리지 않으며, 용기 있는 자는 두려워하지 않고, 어진 사람은 근심이 없으니. 그 어떤 학문을 습득하더라도 지용인에 기초하여 그 토대를 쌓아간다면 기초가 단단하여 능히 무엇이라도 반석 위에 올리며 높은 곳을 향할 수 있을 터. 달리 말하면 모든 배움은 지용인으로 환원시켜 해석할 수 있지 않겠는가. -  천기성(天機星)</color>
   źródło: Items.json :: dataList[id=20034].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>The Wise are unshaken, the Brave are unafraid, and the Benevolent are untroubled. No matter what discipline it may be, to build the pillars of learning upon the three foundations of Zhi, Yong, and Ren is to build a soaring tower. Which summons forth an intriguing question: can not all of education be condensed into Zhi, Yong, and Ren? - Tianji Star(天機星)</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Mądry się nie waha, odważny się nie boi, dobroć nie zna trosk. Bez względu na dziedzinę — budować filary nauki na trzech fundamentach Zhi, Yong i Ren to budować wieżę sięgającą nieba. Stąd intrygujące pytanie: czy nie da się całej edukacji sprowadzić do Zhi, Yong i Ren? - Tianji Star(天機星)</color>
586. [Przedmioty, sklep i profil gracza [20035] — nazwa] 비급이 아닌 척하는 비전서
   źródło: Items.json :: dataList[id=20035].name
   limit: do 50 znaków
   EN: Definitely Not A Secret Scroll
   PL: Zdecydowanie Nie Tajny Zwój
587. [Przedmioty, sklep i profil gracza [20035] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 지·용·인 기초 입문 20개로 전환된다.\n\n<color=#a16a3b>비밀스럽게 전해져오는 지식이 담겨있는 두루마리군. 기초 따위는 무시하고 읽는 자로 하여금 굉장히 빠르게 원하는 지식과 기술을 습득하게 해준다. 두루마리 자체에 어떤 특이점이 있는 것일지 이 문자에 특이점이 있는 것일지 아니면 글씨를 이루는 먹물에 있을지는 아직 아무도 모를 터. 비전서를 탐하는 자들에게는 그 원리나 방식은 중요하지 않다. 하지만 급히 먹은 음식은 체하고 게워 내는 것이 이치. 분에 맞지 않는 것은 늘 경계하도록. - 어느 스승</color>
   źródło: Items.json :: dataList[id=20035].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Intro to Zhi, Yong, Ren immediately upon acquisition.\n\n<color=#a16a3b>A scroll filled with esoteric knowledge. It allows its readers to rapidly absorb its contents, wisdom or technique, disregarding the basics that must come before the learning. None know yet whether it is the paper that is a Singularity, or the letters that are a Singularity, or the ink that forms them that is a Singularity. This likely matters very little to those who covet this secret scroll. Yet, remember well that food ingested in haste risks sickness and vomiting. Always be acutely aware of your capabilities. - A Certain Master</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Wstępów do Zhi, Yong, Ren.\n\n<color=#a16a3b>Zwój napełniony ezoteryczną wiedzą. Pozwala czytelnikom błyskawicznie wchłaniać treść, mądrość czy techniki, ignorując podstawy, które powinny wyprzedzać naukę. Nikt jeszcze nie wie, czy punktem osobliwym jest sam papier, czy litery, czy tusz, który je tworzy. Tym, co pożądają Tajnego Zwoju, mało obchodzi jego zasada czy metoda. Lecz pamiętaj: jedzenie połknięte w pośpiechu odbija się i wywraca. Strzeż się zawsze własnych możliwości. - Pewien Mistrz</color>
588. [Przedmioty, sklep i profil gracza [20036] — nazwa] 시테러 표본
   źródło: Items.json :: dataList[id=20036].name
   limit: do 40 znaków
   EN: Sea Terror Sample
   PL: Próbka Morskiego Koszmaru
589. [Przedmioty, sklep i profil gracza [20036] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>연구를 위해 채취된 시테러의 파편. 불길하게 번지는 푸른빛 너머로, 잔잔한 파도 소리가 아득히 스며든다.</color>
   źródło: Items.json :: dataList[id=20036].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>Chunks of Sea Terror flesh, collected for research purposes. The calm noise of waves crest faintly through the insidious blue light.</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Odrywki ciała Morskiego Koszmaru, pobrane do badań. Przez złowieszcze, rozlewające się błękitne światło ledwo dochodzi szum spokojnych fal.</color>
590. [Przedmioty, sklep i profil gracza [20037] — nazwa] 빛나는 시테러 표본
   źródło: Items.json :: dataList[id=20037].name
   limit: do 40 znaków
   EN: Luminous Sea Terror Sample
   PL: Świecąca Próbka Morskiego Koszmaru
591. [Przedmioty, sklep i profil gracza [20037] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 시테러 표본 20개로 전환된다.\n\n<color=#a16a3b>연구를 위해 채취된 시테러. 경외하던 생명을 가르는 손끝에 망설임은 없었다. 꺼지지 않는 생명을 파헤치는 것은 진화를 위해 거쳐야 할 필연이기에.</color>
   źródło: Items.json :: dataList[id=20037].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Sea Terror Sample immediately upon acquisition.\n\n<color=#a16a3b>A Sea Terror specimen, collected for research purposes. There was no hesitation in the hand that clove through the life its owner had once beheld with awe. One must delve into the undying light to evolve. It is an inevitable step.</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Próbek Morskiego Koszmaru.\n\n<color=#a16a3b>Okaz Morskiego Koszmaru, pobrany do badań. W dłoni, co rozcięła życie, na które jej właściciel kiedyś patrzył z bojaźnią, nie było zawahania. Głębić niegasnące światło trzeba, by ewoluować. To nieunikniony krok.</color>
592. [Przedmioty, sklep i profil gracza [9900] — nazwa] 끈타래
   źródło: Items.json :: dataList[id=9900].name
   limit: do 40 znaków
   EN: Threadskein
   PL: Motek Nici
593. [Przedmioty, sklep i profil gracza [9900] — opis] 인격의 투영할 외형을 제작할 때 사용한다.\n\n<color=#a16a3b>빛으로 짜여진 끈을 모아 타래로 엮었다.\n빛의 끈에는 모든 것이 이어져 있어, 어느 끈이 떨리면 저 멀리의 끈도 덩달아 진동한다.\n그렇게 모든 것들은 저마다 이어진 떨림으로 짜여졌다.\n때문에 끈으로 짜여진 옷이 겉모습을 속이는 것은 결코 허황된 것이 아니게 된다.</color>
   źródło: Items.json :: dataList[id=9900].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to weave Façades of Identities to be projected.\n\n<color=#a16a3b>Wisps of light woven into threads, then twined into a skein.\nThe strands of light are components of a universal connection—should a thread in the weave tremble, so does a distant one, thereby making all that it connects interlinked by ties of vibrations.\nAs such, it is by no means absurd to consider an outfit made of threads a façade in all its meaning.</color>
   PL: Służy do utkania Fasady Tożsamości przeznaczonej do projekcji.\n\n<color=#a16a3b>Snopki światła zwite w nici, a nici zwinięte w kłębek.\nNici światła zawierają wszystko — gdy jedna z nich zadrży, daleka drgnie razem z nią.\nW ten sposób wszystko utkano z drgań, każde swoje.\nStąd ubranie utkane z nici oszukujące wyglądem nie jest niczym bajecznym.</color>
594. [Przedmioty, sklep i profil gracza [20043] — nazwa] 잘린 실
   źródło: Items.json :: dataList[id=20043].name
   limit: do 40 znaków
   EN: Severed Thread
   PL: Odcięta Nić
595. [Przedmioty, sklep i profil gracza [20043] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>무언가에 의해 끊어지고 베어진 실.\n한 가닥의 실이라 해도 그것은 한 가닥이 아니라 여러 겹의 가는 것들이 뭉쳐 한 가닥으로 보이는 것뿐. 순수하게 하나로 이루어진 것은 없다는 것일 테지. 그렇기에 실은 베여도 그 단면의 끝에서 여러 가닥이 펼쳐져 나간다. 펼쳐지고 나누어진 가닥은 시간이 흐름에 따라 다시 흩어지며, 아물지 않고 벌어져 상처를 남기고 끝내 아물지 못한다.</color>
   źródło: Items.json :: dataList[id=20043].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>Something has severed this thread, snapping it into strands.\nTruly, there is no such thing as an existence in complete homogeneity with another, for slicing a single thread reveals that it is in fact a twine of multiple fibers. When a thread is severed, it leaves not two separate threads, but a multitude of frayed strands—from this, we may learn that time indeed does not cure all wounds. The passage of time only unravels the frayed strands further, leaving weeping wounds that never heal.</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>Ktoś przeciął i ściął tę nić.\nChoćby nić była jedna, nie jest jedną — to wiele cienkich zwite w jedną. Nikt nie jest czysto jedną rzeczą. Dlatego nić po ucięciu nie zostawia dwóch osobnych nici, lecz mnóstwo wyszarpanych nitek — z tego poznajemy, że czas rzeczywiście nie leczy wszystkich ran. Upływ czasu tylko rozplata je dalej, zostawiając krwawiące rany, które nigdy się nie goją.</color>
596. [Przedmioty, sklep i profil gracza [20044] — nazwa] 잘리고 타버린 실뭉치
   źródło: Items.json :: dataList[id=20044].name
   limit: do 40 znaków
   EN: Severed and Scorched Skein
   PL: Odcięty i Nadpalony Motek
597. [Przedmioty, sklep i profil gracza [20044] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 잘린 실 20개로 전환된다.\n\n<color=#a16a3b>실을 완전히 끊어내기 위해서는 자르지 않고 태워야 한다. 무언가를 끊어낸다는 것은 날카로움만으로 이루어지는 것이 아니다. 진정으로 끊어낸다는 것은 단면이라는 개념조차 없애도록 뜨겁게 태워 녹여 버리는 것. 그런 각오와 마음이 있어야만 연결된 것을 끊어낼 수 있는 것이겠지.\n\n잘리고 타버린 이 실들을 모아 다시 실을 짜낸다면, 그 실은 아직 누군가를 이어주는 역할을 해낼 수 있을까. 아직은 알 수 없지만, 그럴 수 있다면 좋겠군.</color>
   źródło: Items.json :: dataList[id=20044].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Severed Thread immediately upon acquisition.\n\n<color=#a16a3b>To truly sever a thread, it must be burned, not cut. Keenness is a means insufficient to achieving the total annihilation that burns and melts away even the lingering remnants of an erstwhile connection down to the frayed ends of separated threads. It must be that only with resolute determination and heart can one sever such a connection.\n\nShould these skeins of severed and scorched strings be twined anew, perhaps the resulting new thread can be used to connect hearts once again? I certainly hope so, though there is no way for us to know at this moment.</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Odciętych Nici.\n\n<color=#a16a3b>Aby naprawdę przeciąć nić, trzeba ją spalić, nie ciąć. Ostrze nie wystarczy, by osiągnąć totalne unicestwienie — by palić i topić nawet resztki dawnych więzi, aż po wyszarpane końce rozdzielonych nici. Dopiero z determinacją i sercem można zerwać taką więź.\n\nGdyby z tych uciętych i spopielonych kłębów upleść nową nić — czy połączyłaby serca ponownie? Nie wiadomo. Ale gdyby tak było, byłoby pięknie.</color>
598. [Przedmioty, sklep i profil gracza [238] — nazwa] 도약 모듈 - E.G.O 해석 [ZAYIN]
   źródło: Items.json :: dataList[id=238].name
   limit: do 60 znaków
   EN: Takeoff Module - E.G.O Spinning [ZAYIN]
   PL: Moduł Skoku — Splot Nici E.G.O [ZAYIN]
599. [Przedmioty, sklep i profil gracza [238] — opis] 사용 시, E.G.O의 환상 해석 단계가 4단계까지 증가한다. (ZAYIN 등급만 적용 가능)\n\n<color=#a16a3b>단기간에 대량의 파편들과 엮어 [ZAYIN]급까지의 E.G.O의 해석을 특정 수준까지 급가속시킨다. ‘여기의 끈이 떨리면 언젠가 저기의 끈이 떨린다라… 여기 사람들 말대로 모든 것이 끈으로 엮여 있다면, 무언가를 해석한다는 건 끈을 풀어 헤쳐 간다는 건가. 날 감싼 끈이란 게 전부 풀리면 어떻게 되는 거지?’</color>
   źródło: Items.json :: dataList[id=238].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Raises an E.G.O's Threadspinning Tier up to Tier 4 (Usable only on ZAYIN-level E.G.O).\n\n<color=#a16a3b>Greatly accelerates the Threadspinning of a [ZAYIN]-level E.G.O by weaving it with a great number of shards in a short span of time. "Should a thread in the weave tremble, so does a distant one..." such were the words spoken by the people here. If all of these strands are components of a universal connection as they claim, then the act of deciphering a given object must also be the equivalent of unraveling the thread. I find myself thinking, what would come to pass if <i>all</i> of the threads wrapped around me are unraveled?</color>
   PL: Po użyciu podnosi Stopień Splotu Nici E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi ZAYIN)\n\n<color=#a16a3b>Gwałtownie przyspiesza Splot E.G.O rangi [ZAYIN], splatając go z masą odłamków w krótkim czasie. „Skądinąd: gdy drgnie tutaj nić, kiedyś drgnie tamta… jak tu mówią, wszystko splecione jest nićmi, to czy rozszyfrowywanie czegoś nie jest rozplątywaniem nici. Co się stanie, gdy wszystkie nici, które mnie owijają, się rozplączą?”</color>
600. [Przedmioty, sklep i profil gracza [20045] — nazwa] 익은 렌즈
   źródło: Items.json :: dataList[id=20045].name
   limit: do 40 znaków
   EN: Burnt-in Lens
   PL: Przepalona Soczewka
601. [Przedmioty, sklep i profil gracza [20045] — opis] ‘사영전투][투전영사’ 교환 상점에서 상시 보상을 교환할 때 사용한다.\n\n<size=75%><color=#a16a3b>왜곡된 유리를 통해 그것을 쏘아낸다. 이 렌즈에 비추어진 자들은 곧 필름 속에 붙여 넣어지고, 이윽고 거기서 벗겨져 나와 그림자가 되어 앞을 막아선다. 아쉽게도 렌즈에는 수명이 있어 온몸으로 작열하는 빛을 통과시킨 렌즈는 그대로 익어버리고, 영사된 그림자들을 남겨두기 위해 새로운 렌즈로 교체된다. 익은 렌즈는 그렇게 유품과도 같이 남겨진다.\n\n‘이 렌즈가 얼마나 비싼 건지나 알고 이렇게 막 써대는 것인지... 전투 수행 능력 향상, 과정 분석 같은 사유가 있다곤 해도 이렇게까지 써대는 건 이해가 안 된단 말이지. 이 회사는 진짜 돈이 썩어나나 보군.’</color></size>
   źródło: Items.json :: dataList[id=20045].desc
   limit: do 1200 znaków
   tokeny: zachowaj dokładnie: <size=75%>, <color=#a16a3b>, </color>, </size>, \n
   EN: Used for exchanging always-available, Standard Rewards at the "Reflectrial][lairtcelfeR" Reward Exchange shop.\n\n<size=75%><color=#a16a3b>Through warped glass it is fired. Those reflected in this lens are soon spliced into films, and before long, are peeled away from them; now untethered, they become shadows that bar one's path. Unfortunate as it is, every lens has a finite lifespan. Once a lens has let the searing light pass through the whole of its body, it becomes scorched and baked through—a fresh lens then takes its place to preserve the projected shadows. These burnt-in lenses are what remain in the wake of this process, much like keepsakes of the dead.\n\n"The way they're blowing through those lenses... Do they have the slightest clue how exorbitantly expensive those things are? Combat capability enhancement, process analysis—yes, I know the reasons are all valid, but I cannot wrap my head around using this many. The company really must be drowning in money."</color></size>
   PL: Służy do wymiany nagród stałych w sklepie wymiany „Reflectrial][lairtcelfeR”.\n\n<size=75%><color=#a16a3b>Wystrzeliwuje się to przez odkształcone szkło. Ci, którzy odbiją się w tej soczewce, wkrótce zostaną wklejeni w taśmę filmową, a po chwili z niej zdarti — jako cienie zasłaniają drogę. Niestety soczewka ma ograniczoną żywotność; ta, która przepuściła przez siebie palące całe ciało światło, piecze się przez i zostaje wymieniona na nową, by zachować rzucone cienie. Przepalone soczewki zostają w ten sposób jak pamiątki po zmarłych.\n\n„Czy oni w ogóle wiedzą, ile to kosztuje, tak to marnując…? Poprawa zdolności bojowych, analiza procesów — powody jak najbardziej ważne, ale tak to marnować jest ponad moje pojęcie. Ta firma musi mieć naprawdę forsy.”</color></size>
602. [Przedmioty, sklep i profil gracza [20046] — nazwa] 사진들
   źródło: Items.json :: dataList[id=20046].name
   limit: do 40 znaków
   EN: Photos
   PL: Zdjęcia
603. [Przedmioty, sklep i profil gracza [20046] — opis] 보상 교환 창에서 다양한 보상을 구입할 때 사용한다.\n\n<color=#a16a3b>찰칵. 이 소리는 망치가 못을 박는 소리다. 무엇이 박히는 것일까. 사진기는 어느 순간의 빛을 가로채고 사로잡아 거친 종이에 빛을 못 박아 전시한다. 기록하기 위해 찍힌 것인지, 기억하기 위해 찍힌 것인지 그 목적에 따라 사진의 명칭이 달라져야 하지 않을까. 기억되기 위해서가 아닌, 기록되기 위해 망치로 못 박힌 빛들은 안타까우니까. 인화된 사진에서 죽은 빛은 탄 채로 절규하고 있다. 못에 박혀 절규한 채로 죽은 빛은 사진에 누군가의 미소를 기록해낸다. </color>
   źródło: Items.json :: dataList[id=20046].desc
   limit: do 890 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Used to purchase various rewards from the Reward Exchange menu.\n\n<color=#a16a3b>*snap* The sound of a hammer driving a nail in. But what precisely is being "driven in?" The camera waylays the light of a given moment, then nails it onto rough paper for exhibition. Was the photograph taken as a record or a remembrance? Perhaps a photograph's name ought to change depending on which purpose it is made to serve. After all, beams of light nailed down by a hammer, only to be recorded and never remembered, are pitiable things. Within printed photographs, dead lights scream in despair, burned and blackened. The dead lights, perished screaming where they are nailed, record the smile of someone standing in the photograph.</color>
   PL: Służy do zakupu różnorodnych nagród w oknie wymiany.\n\n<color=#a16a3b>*pyk*. Dźwięk młota wbijającego gwóźdź. Co jest wbijane? Aparat przechwytuje światło danej chwili, przygarnia je i wbija w szorstki papier, by je wystawić. Czy zdjęcie robi się po to, by zapisać, czy po to, by zapamiętać? Może nazwa fotografii powinna zależeć od tego celu. Bo światło przybite młotem, które tylko zapisano, a nigdy nie zapamiętano, godne jest litości. W wydrukowanych fotografiach martwe światła krzyczą w rozpaczy, spalone i czarne. Martwe światła, które skonały krzycząc tam, gdzie je przybito, zapisują na zdjęciu czyjś uśmiech.</color>
604. [Przedmioty, sklep i profil gracza [20047] — nazwa] 사진더미들
   źródło: Items.json :: dataList[id=20047].name
   limit: do 40 znaków
   EN: Photo Bundles
   PL: Stosy Zdjęć
605. [Przedmioty, sklep i profil gracza [20047] — opis] 낮은 확률로 얻을 수 있으며, 획득 즉시 사진들 20개로 전환된다.\n\n<color=#a16a3b>‘회수된 사진들이 이렇게나 많군요. 아, 그거 아시나요? 이 사진들 뒤틀림이 만들어낸 물질들인데도 남아있어요. 어떤 뒤틀림의 부산물은 뒤틀림의 해결과 함께 사라지는데, 어떤 건 이렇게 뒤틀림이 해결되어도 남아버리네요. 뒤틀림의 성질에 따라 다른 걸까요? 이 뒤틀림은 무언가를 남기고 기록하고 기억하고 싶어했을 테니까.... 사진을 남긴 거고... 그래서 그 성질에 따라 이 부산물도 기록처럼 남아버린 걸까요? 무슨 차이로 뒤틀림마다 이런 특성이 나타나는지 좀 더 연구해봐야겠어요. LCD에서 일을 하다 보면 곧 알게 되겠죠. LCE랑 협력하기는 싫지만요.’</color>
   źródło: Items.json :: dataList[id=20047].desc
   limit: do 1040 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: Spawns rarely. Converted to 20 Photos immediately upon acquisition.\n\n<color=#a16a3b>'Quite a lot of photographs retrieved here. Oh, did you know? These photos are composed of matter produced by a Distortion, but they remain in existence. Some Distortion byproducts fade away when the case is resolved, but some don't, even after everything is over. I wonder if this has something to do with the nature of the Distortion. Well, we do know that this Distortion wished to record something and remember it... hence the photographs. Perhaps that's why these photographs are left behind as some kind of "record." This calls for research into exactly what results in the difference in a Distortion's property from another Distortion's. Well, working in LCD will probably give me some insight in due time... though I'd rather not cooperate with LCE.'</color>
   PL: Występuje rzadko; tuż po zdobyciu zamienia się w 20 Zdjęć.\n\n<color=#a16a3b>„Niesłychanie dużo zdjęć odzyskano. A, wiecie? Te zdjęcia, choć powstały z materii stworzonej przez Wypaczenie, wciąż istnieją. Niektóre produkty uboczne Wypaczenia znikają, gdy przypadek rozwiązano; inne — nie, nawet gdy wszystko się skończyło. Czy to z natury Wypaczenia wynika? To Wypaczenie chciało coś zapisywać i pamiętać… stąd zdjęcia… więc i ten produkt uboczny pozostał jak zapis, zgodnie z jego naturą? Co powoduje różnicę w takich cechach między Wypaczeniami — trzeba to zbadać. Pracując w LCD, pewnie się wkrótce dowiem. Współpracować z LCE nie chcę.”</color>
606. [Przedmioty, sklep i profil gracza [20048] — nazwa] 풀린 필름
   źródło: Items.json :: dataList[id=20048].name
   limit: do 40 znaków
   EN: Unrolled Film
   PL: Rozwinięta Taśma
607. [Przedmioty, sklep i profil gracza [20048] — opis] ‘사영전투][투전영사’ 교환 상점에서 한정 보상을 구입할 때 사용한다. 이벤트 보상 교환 기간 종료 시, 익은 렌즈로 전환된다.\n\n<size=75%><color=#a16a3b>빛이 쏘아져 필름에 새겨지듯 박힌다. 이 빛이 담은 정보는 다음 빛이 통과할 하나의 그을음과 다르지 않다. 마치 큰 폭발 뒤에 벽에 새겨지는 사람의 그을음과 같이. 그 자리에 박제된 빛은 어느 날의 누군가, 무언가를 담고 있다. 새로운 빛이 필름을 통과하고 렌즈까지 거치고 나면 그 끝에는 빛으로 맺혀진 것이 존재하게 된다. 우리는 그것을 통해 빛이 담고 있던 정보를 복기할 수 있다. 산 빛이 죽은 빛을 통과하며 스스로를 잃고 죽은 빛이 만들어놓은 시체의 형태로 상을 맺을 수 밖에 없는 아이러니. 그렇기에 투영은 산 것을 죽은 것에 통과시켜 죽이고, 산 것처럼 보이게 하는 쓰라린 기술이다.\n\n‘이런 필름은 어디에서 구해오는 거야? LCB에서 전투하던 걸 녹화하는 사람이나 기계가 따로 있는 거야? 그럴 리는 없을 거고… 아니면 이것도 설마…?’</color></size>
   źródło: Items.json :: dataList[id=20048].desc
   limit: do 1500 znaków
   tokeny: zachowaj dokładnie: <size=75%>, <color=#a16a3b>, </color>, </size>, \n
   EN: Used for purchasing Limited Rewards from the "Reflectrial][lairtcelfeR]" Reward Exchange shop.\n\n<size=70%><color=#a16a3b>Upon the film, the light is embedded and etched. A subsequent flash of light will soon penetrate the information contained within the preceding light etched like a silhouette—much like what remains when a human body is exposed to a devastating explosion of light and heat. The captured light, akin to a taxidermied still, contains the memories of someone, something. When new light passes through the film and the lens both, the plain ray is transfigurated into an image of light; through it, the information retained in the initial flash still remains. The image the living light forms is not one of itself but an image of a corpse, traces of dead light; how ironic, that the light that lives can form an image only when it passes through the light that has died? That is why the art of projection is a bitter one—the art that forces the living through the dead, killing it, only to project a mere simulacrum of life.\n\n"Where are ya even getting these films from? Is there, like, a dedicated documentarian or a recording machine that tapes LCB's battles? That can't be it... Or is this also...?"</color></size>
   PL: Służy do zakupu nagród limitowanych w sklepie wymiany „Reflectrial][lairtcelfeR”. Po zakończeniu okresu wymiany zamienia się w Przepalone Soczewki.\n\n<size=75%><color=#a16a3b>Światło trafia w taśmę i wyrywa się w niej jakby żłobienie. Informacja, którą niesie to światło, to nie więcej niż sadza dla kolejnego światła, które przez nią przejdzie — jak cień człowieka wypalony na śnie po wielkim wybuchu. Uwięzione w miejscu światło zawiera kogoś, coś z pewnego dnia. Gdy nowe światło przechodzi przez taśmę i soczewkę, na końcu powstaje coś splecionego ze światła. Przez to możemy odtworzyć informację, którą światło niosło. Żywe światło, przechodząc przez martwe, traci siebie i może wytworzyć obraz tylko w formie zwłok martwego światła — ironia. Dlatego projekcja to gorzka technologia: przepuszcza żywe przez martwe, zabijając je, by rzucić pozor życia.\n\n„Skąd się biorą te taśmy? Ktoś osobno nagrywa walki LCB? Racja, że nie… czyżby i to…?”</color></size>
608. [Przedmioty, sklep i profil gracza [751] — nazwa] 아나운서 선택권 [이상교환]
   źródło: Items.json :: dataList[id=751].name
   limit: do 60 znaków
   EN: Nominable Announcer Ticket [Yisang Exchange]
   PL: Bilet Wyboru Komentatora [Wymiana Yi Sanga]
609. [Przedmioty, sklep i profil gracza [751] — opis] 사용 시, 추출의 이상 교환에서 획득 가능한 아나운서 중 하나를 선택하여 획득할 수 있다.\n(※ 발푸르기스의 밤 아나운서의 경우, 획득 불가)
   źródło: Items.json :: dataList[id=751].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use this item to select and obtain an Announcer from a list of Announcers that can be acquired through Yisang Exchange on the Extraction menu.\n(※ Does not include Walpurgis Night Announcers)
   PL: Po użyciu można wybrać jednego z Komentatorów dostępnych w Wymianie Yi Sanga w menu Ekstrakcji.\n(※ Komentatorzy Nocy Walpurgii są niedostępni)
610. [Przedmioty, sklep i profil gracza [751] — tekst klimatyczny] 전투 상황을 알려주는 아나운서 녹음 기록들의 보관함.\n\n‘이 테이프에는 이미 죽은 사람의 목소리도 담겨 있던데, 어떻게 녹음한 거래?’\n‘거울세계 너머에서 관측된 소리들 중 쓸만한 것들을 잡아 가둔 것이라더군.’\n‘또 거울이야? 아주 그냥 이 회사의 모든 일을 거울로 해결해도 되겠어.’\n‘이미 그러고 있지 않아?’\n‘…그러면 이 기술의 대가는?’
   źródło: Items.json :: dataList[id=751].flavor
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains recordings of Announcers who relay the current battlefield status.\n\n"Hey, so... some of these tapes are recordings of people who are already long dead. Wonder where they got these voices from?"\n"By capturing and trapping a few—situationally relevant, of course—voices observed from beyond the Mirror Worlds, they say."\n"It's the Mirror again? Mirror this, Mirror that—might as well use the Mirror to deal with everything, this company!"\n"Aren't we already doing that?"\n"... Yeah, but... Have we thought about the consequences of using this technology...?"
   PL: Skrytka z nagraniami Komentatorów, którzy donoszą o stanie pola bitwy.\n\n„Hej, więc… na niektórych taśmach są nagrania głosów ludzi dawno martwych. Skąd te głosy?”\n„Mówili, że złapali i zamknęli kilka — takich, co się do sytuacji przydają — głosów zaobserwowanych z tamtej strony Światów Lustra.”\n„Znowu lustro? Lustro to, lustro tamto — równie dobrze moglibyście lustrem załatwić wszystko, ta firma!”\n„A czy już tak nie robimy?”\n„…Racja, ale… czy myśleliśmy kiedyś o cenie tej technologii…?”
611. [Przedmioty, sklep i profil gracza [752] — nazwa] 아나운서 선택권 [이상 교환] (도상구축 Beta)
   źródło: Items.json :: dataList[id=752].name
   limit: do 90 znaków
   EN: Nominable Announcer Ticket [Yisang Exchange] (Schemacraft Beta)
   PL: Bilet Wyboru Komentatora [Wymiana Yi Sanga] (Konstrukcja Schematów Beta)
612. [Przedmioty, sklep i profil gracza [752] — opis] 사용 시, 추출의 이상 교환에서 획득 가능한, 교환 가능 범위 내의 아나운서 중 하나를 선택하여 획득할 수 있다.\n(※ 발푸르기스의 밤 아나운서의 경우, 획득 불가)\n(※ 교환 가능 범위 : 시즌 8 종료일 이전까지 출시되는 아나운서)
   źródło: Items.json :: dataList[id=752].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use this item to select and obtain an Announcer from a limited list of Announcers that can be acquired through Yisang Exchange on the Extraction menu.\n(※ Does not include Walpurgis Night Announcers)\n(※ Only Announcers released up to the Season 8's end date can be obtained through this item)
   PL: Po użyciu można wybrać jednego z Komentatorów dostępnych w ograniczonym zakresie Wymiany Yi Sanga w menu Ekstrakcji.\n(※ Komentatorzy Nocy Walpurgii są niedostępni)\n(※ Zakres wymiany: Komentatorzy wydani do końca Sezonu 8)
613. [Przedmioty, sklep i profil gracza [752] — tekst klimatyczny] 전투 상황을 알려주는 아나운서 녹음 기록들의 보관함.\n\n'이 테이프에는 이미 죽은 사람의 목소리도 담겨 있던데, 어떻게 녹음한 거래?'\n'거울세계 너머에서 관측된 소리들 중 쓸만한 것들을 잡아 가둔 것이라더군.'\n'또 거울이야? 아주 그냥 이 회사의 모든 일을 거울로 해결해도 되겠어.'\n'이미 그러고 있지 않아?'\n'…그러면 이 기술의 대가는?'
   źródło: Items.json :: dataList[id=752].flavor
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains recordings of Announcers who relay the current battlefield status.\n\n"Hey, so... some of these tapes are recordings of people who are already long dead. Wonder where they got these voices from?"\n"By capturing and trapping a few—situationally relevant, of course—voices observed from beyond the Mirror Worlds, they say."\n"It's the Mirror again? Mirror this, Mirror that—might as well use the Mirror to deal with everything, this company!"\n"Aren't we already doing that?"\n"... Yeah, but... Have we thought about the consequences of using this technology...?"
   PL: Skrytka z nagraniami Komentatorów, którzy donoszą o stanie pola bitwy.\n\n„Hej, więc… na niektórych taśmach są nagrania głosów ludzi dawno martwych. Skąd te głosy?”\n„Mówili, że złapali i zamknęli kilka — takich, co się do sytuacji przydają — głosów zaobserwowanych z tamtej strony Światów Lustra.”\n„Znowu lustro? Lustro to, lustro tamto — równie dobrze moglibyście lustrem załatwić wszystko, ta firma!”\n„A czy już tak nie robimy?”\n„…Racja, ale… czy myśleliśmy kiedyś o cenie tej technologii…?”
614. [Przedmioty, sklep i profil gracza [237] — nazwa] 도약 모듈 - E.G.O 해석 [TETH]
   źródło: Items.json :: dataList[id=237].name
   limit: do 60 znaków
   EN: Takeoff Module - E.G.O Spinning [TETH]
   PL: Moduł Skoku — Splot Nici E.G.O [TETH]
615. [Przedmioty, sklep i profil gracza [237] — opis] 사용 시, E.G.O의 환상 해석 단계가 4단계까지 증가한다. (최대 TETH 등급까지 적용 가능)
   źródło: Items.json :: dataList[id=237].desc
   limit: do 130 znaków
   EN: Raises an E.G.O's Threadspinning Tier up to Tier 4. (Usable only on E.G.Os TETH Level or lower)
   PL: Po użyciu podnosi Stopień Splotu Nici E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi TETH lub niższej)
616. [Przedmioty, sklep i profil gracza [237] — tekst klimatyczny] LCA 연구개발팀에서 제작한 네 번째 E.G.O 환상 해석 모듈. 떨리고 빛나는 끈을 단기간에 대량의 파편들과 엮어 [TETH]급까지의 E.G.O의 해석을 특정 수준까지 급가속시킨다. 옷은 원단으로 조립되어 있고, 원단은 실들로 직조되어 있죠. 그리고 그 실은 또다시 가느다란 가닥들로 꼬여 있고요. 프랙탈이라고 하던가요? 가끔 이런 패턴의 반복에서 기시감을 느껴요. 뭔가가 반복되고 있어요.
   źródło: Items.json :: dataList[id=237].flavor
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The fourth E.G.O Threadspinning Module developed by LCA R&D Team.\nWeaves the shimmering threads with numerous shards, enhancing the E.G.O Threadspinning tier of [TETH]-level or lower E.G.O at an accelerated pace.\nClothes are assembled from fabric, and fabric is woven from threads. Those threads are themselves twisted together from still finer strands. What was the term for these repeating patterns again—a fractal? Sometimes, when I see these patterns, I get an odd sense of deja vu.\n\n<i>Something</i> is recurring.
   PL: Czwarty moduł Splotu Nici E.G.O opracowany przez zespół badawczo-rozwojowy LCA.\nSplata drżące, lśniące nici z masą odłamków, przyspieszając Splot E.G.O rangi [TETH] lub niższej do ustalonego poziomu.\nUbrania składają się z materiału, materiał jest tkany z nici. Te nici z kolei zwite są z jeszcze cieńszych włókien. Fraktal, czy jak to mówili? Czasem te powtarzające się wzory budzą we mnie dziwne déjà vu.\n\nCoś się powtarza.

## Przedmioty, sklep i profil gracza: MissionUIText
- plik gry: `MissionUIText.json`

617. [Przedmioty, sklep i profil gracza [acquire_personality_title] — tekst] 인격 선택
   źródło: MissionUIText.json :: dataList[id=acquire_personality_title].content
   limit: do 120 znaków
   EN: Select Identity
   PL: Wybór Tożsamości
618. [Przedmioty, sklep i profil gracza [ask_acquire_personality] — tekst] {1}의 [{0}] 인격을 선택하시겠습니까?
   źródło: MissionUIText.json :: dataList[id=ask_acquire_personality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Select {1}'s [{0}] Identity?
   PL: Wybrać Tożsamość [{0}] dla {1}?
619. [Przedmioty, sklep i profil gracza [ask_use_item_for_acquire_personality] — tekst] {0}을 사용하시겠습니까
   źródło: MissionUIText.json :: dataList[id=ask_use_item_for_acquire_personality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Use {0}?
   PL: Użyć {0}?
620. [Przedmioty, sklep i profil gracza [tip_able_to_check_personality_by_longclick] — tekst] ※ 롱클릭 시 인격 상세 정보 확인이 가능합니다.
   źródło: MissionUIText.json :: dataList[id=tip_able_to_check_personality_by_longclick].content
   limit: do 120 znaków
   EN: ※ Press and hold to view detailed information of the Identity.
   PL: ※ Przytrzymaj, by zobaczyć szczegółowe informacje o Tożsamości.
621. [Przedmioty, sklep i profil gracza [luxcavation_bonus_on] — tekst] 채광 보너스 적용중
   źródło: MissionUIText.json :: dataList[id=luxcavation_bonus_on].content
   limit: do 120 znaków
   EN: Lux. Bonus Activated
   PL: Aktywny Bonus Wydobycia
622. [Przedmioty, sklep i profil gracza [ask_acquire_personality_already_owned] — tekst] {1}의 [{0}] 인격을 선택하시겠습니까?\n보유 중인 인격 선택 시 파편으로 교환됩니다.
   źródło: MissionUIText.json :: dataList[id=ask_acquire_personality_already_owned].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: Select {1}'s [{0}] Identity?\nSelecting an already-owned Identity will automatically convert your selection to Shards.
   PL: Wybrać Tożsamość [{0}] dla {1}?\nWybranie posiadanej Tożsamości zamieni wybór na Odłamki.
623. [Przedmioty, sklep i profil gracza [acquire_ego_title] — tekst] E.G.O 선택
   źródło: MissionUIText.json :: dataList[id=acquire_ego_title].content
   limit: do 120 znaków
   EN: Selecting E.G.O
   PL: Wybór E.G.O
624. [Przedmioty, sklep i profil gracza [ask_acquire_ego] — tekst] {1}의 [{0}] E.G.O를 선택하시겠습니까?
   źródło: MissionUIText.json :: dataList[id=ask_acquire_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Select {1}'s [{0}] E.G.O?
   PL: Wybrać E.G.O [{0}] dla {1}?
625. [Przedmioty, sklep i profil gracza [ask_acquire_ego_already_owned] — tekst] {1}의 [{0}] E.G.O를 선택하시겠습니까?\n보유 중인 E.G.O 선택 시 파편으로 교환됩니다.
   źródło: MissionUIText.json :: dataList[id=ask_acquire_ego_already_owned].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: Select {1}'s [{0}] E.G.O?\nSelecting an already-owned E.G.O will automatically convert your selection to Shards.
   PL: Wybrać E.G.O [{0}] dla {1}?\nWybranie posiadanego E.G.O zamieni wybór na Odłamki.

## Przedmioty, sklep i profil gracza: Quest
- plik gry: `Quest.json`

626. [Przedmioty, sklep i profil gracza [1] — tekst] {0}턴 이내 클리어
   źródło: Quest.json :: dataList[id=1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear within {0} turns
   PL: Ukończ w ciągu {0} tur
627. [Przedmioty, sklep i profil gracza [2] — tekst] 던전 보스 제압 완료
   źródło: Quest.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Suppress the Dungeon Boss
   PL: Opanuj Bossa Lochu
628. [Przedmioty, sklep i profil gracza [3] — tekst] 스테이지 클리어
   źródło: Quest.json :: dataList[id=3].content
   limit: do 120 znaków
   EN: Clear Stage
   PL: Ukończ Etap
629. [Przedmioty, sklep i profil gracza [40000] — tekst] 모든 아군의 체력이 50% 이상 남은 상태로 클리어하기
   źródło: Quest.json :: dataList[id=40000].content
   limit: do 120 znaków
   EN: Clear Encounter with all allies at 50%+ HP
   PL: Ukończ starcie z całą drużyną przy 50%+ PZ
630. [Przedmioty, sklep i profil gracza [50000] — tekst] 죄종을 제한된 턴 안에 처리하기
   źródło: Quest.json :: dataList[id=50000].content
   limit: do 120 znaków
   EN: Defeat the Peccatula within the turn limit
   PL: Pokonaj Peccatula w limicie tur
631. [Przedmioty, sklep i profil gracza [60000] — tekst] 적을 자폭하지 못하도록 처리하기
   źródło: Quest.json :: dataList[id=60000].content
   limit: do 120 znaków
   EN: Defeat the enemies before they self-detonate
   PL: Pokonaj wrogów, zanim się wysadzą
632. [Przedmioty, sklep i profil gracza [70000] — tekst] 전투를 진행하는 동안 인격이 10회 이상 피격당하지 않기
   źródło: Quest.json :: dataList[id=70000].content
   limit: do 120 znaków
   EN: Do not take 10+ hits during the Encounter for each Identity
   PL: Żadna Tożsamość nie przyjmie 10+ trafień podczas starcia
633. [Przedmioty, sklep i profil gracza [80000] — tekst] 각자 자신의 모습을 한 죄종 1회 처치
   źródło: Quest.json :: dataList[id=80000].content
   limit: do 120 znaków
   EN: Each unit defeats the Peccatulum that has taken their shape once
   PL: Każda jednostka pokona raz Peccatulum przybierające jej postać

## Przedmioty, sklep i profil gracza: ShopItemCount
- plik gry: `ShopItemCount.json`

634. [Przedmioty, sklep i profil gracza [item_count_basic] — tekst] {1} {0}개
   źródło: ShopItemCount.json :: dataList[id=item_count_basic].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: {1} x{0}
   PL: {1} x{0}
635. [Przedmioty, sklep i profil gracza [item_count_page] — tekst] {1} {0}장
   źródło: ShopItemCount.json :: dataList[id=item_count_page].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: {0} {1}(s)
   PL: {0} {1}(y)
636. [Przedmioty, sklep i profil gracza [item_count_lunacy_free] — tekst] 즉시 광기 {0}(무료) 지급
   źródło: ShopItemCount.json :: dataList[id=item_count_lunacy_free].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Get {0} Free Lunacy as a bonus
   PL: Otrzymaj {0} Darmowego Szaleństwa w prezencie

## Przedmioty, sklep i profil gracza: ShopUI
- plik gry: `ShopUI.json`

637. [Przedmioty, sklep i profil gracza [mainui_shop_charge_enkephalin_tab] — tekst] 엔케팔린 충전
   źródło: ShopUI.json :: dataList[id=mainui_shop_charge_enkephalin_tab].content
   limit: do 120 znaków
   EN: Charge Enkephalin
   PL: Ładowanie Enkefaliny
638. [Przedmioty, sklep i profil gracza [mainui_shop_buy_enkephalin_box_tab] — tekst] 엔케팔린 박스 구매
   źródło: ShopUI.json :: dataList[id=mainui_shop_buy_enkephalin_box_tab].content
   limit: do 120 znaków
   EN: Purchase Enkephalin Box
   PL: Zakup Skrzynki Enkefaliny
639. [Przedmioty, sklep i profil gracza [mainui_shop_buy_enkephalin_box] — tekst] 엔케팔린 박스를 구매하였습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_buy_enkephalin_box].content
   limit: do 120 znaków
   EN: Enkephalin Box purchased.
   PL: Zakupiono Skrzynkę Enkefaliny.
640. [Przedmioty, sklep i profil gracza [mainui_shop_scarce_madness] — tekst] 보유 광기가 부족합니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_scarce_madness].content
   limit: do 120 znaków
   EN: You don’t have enough Lunacy.
   PL: Nie masz wystarczająco Szaleństwa.
641. [Przedmioty, sklep i profil gracza [mainui_shop_ask_buy_enkephalin_box] — tekst] 엔케팔린 박스를 구매하시겠습니까?
   źródło: ShopUI.json :: dataList[id=mainui_shop_ask_buy_enkephalin_box].content
   limit: do 120 znaków
   EN: Would you like to purchase Enkephalin Boxes?
   PL: Czy kupić Skrzynki Enkefaliny?
642. [Przedmioty, sklep i profil gracza [mainui_shop_own] — tekst] 소지
   źródło: ShopUI.json :: dataList[id=mainui_shop_own].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
643. [Przedmioty, sklep i profil gracza [mainui_shop_enkephalin_fulled] — tekst] 엔케팔린 최대치를 초과하여 충전할 수 없습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_enkephalin_fulled].content
   limit: do 120 znaków
   EN: Enkephalin is already at max capacity.
   PL: Enkefalina osiągnęła już maksimum.
644. [Przedmioty, sklep i profil gracza [mainui_shop_ask_charge_enkephalin] — tekst] 엔케팔린을 충전하시겠습니까?
   źródło: ShopUI.json :: dataList[id=mainui_shop_ask_charge_enkephalin].content
   limit: do 120 znaków
   EN: Would you like to charge Enkephalin?
   PL: Czy naładować Enkefalinę?
645. [Przedmioty, sklep i profil gracza [mainui_shop_charge_enkephalin] — tekst] 엔케팔린을 충전했습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_charge_enkephalin].content
   limit: do 120 znaków
   EN: Enkephalin charged.
   PL: Naładowano Enkefalinę.
646. [Przedmioty, sklep i profil gracza [mainui_shop_enkephalin_number] — tekst] 엔케팔린 수치
   źródło: ShopUI.json :: dataList[id=mainui_shop_enkephalin_number].content
   limit: do 120 znaków
   EN: Enkephalin
   PL: Stan Enkefaliny
647. [Przedmioty, sklep i profil gracza [mainui_shop_madness_tab] — tekst] 광기 상점
   źródło: ShopUI.json :: dataList[id=mainui_shop_madness_tab].content
   limit: do 120 znaków
   EN: Lunacy Shop
   PL: Sklep Szaleństwa
648. [Przedmioty, sklep i profil gracza [mainui_shop_package_tab] — tekst] 패키지 상점
   źródło: ShopUI.json :: dataList[id=mainui_shop_package_tab].content
   limit: do 120 znaków
   EN: Packs
   PL: Pakiety
649. [Przedmioty, sklep i profil gracza [mainui_shop_only_once] — tekst] 초회 한정
   źródło: ShopUI.json :: dataList[id=mainui_shop_only_once].content
   limit: do 120 znaków
   EN: First-time Offers
   PL: Oferty Pierwszego Zakupu
650. [Przedmioty, sklep i profil gracza [mainui_shop_additional_give] — tekst] 추가 증정
   źródło: ShopUI.json :: dataList[id=mainui_shop_additional_give].content
   limit: do 120 znaków
   EN: Bonus Supplies
   PL: Bonusowe Zapasy
651. [Przedmioty, sklep i profil gracza [mainui_shop_not_free] — tekst] 유료
   źródło: ShopUI.json :: dataList[id=mainui_shop_not_free].content
   limit: do 120 znaków
   EN: Paid
   PL: Płatne
652. [Przedmioty, sklep i profil gracza [mainui_shop_purchase_per_today_fulled] — tekst] 하루에 구매 가능한 엔케팔린 박스의 수를 초과했습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_purchase_per_today_fulled].content
   limit: do 120 znaków
   EN: You’ve reached the maximum of Enkephalin Box purchases for today.
   PL: Przekroczono dzienny limit zakupów Skrzynek Enkefaliny.
653. [Przedmioty, sklep i profil gracza [mainui_shop_purchase_success] — tekst] 구매를 성공했습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_purchase_success].content
   limit: do 120 znaków
   EN: Purchase successful.
   PL: Zakup zakończony sukcesem.
654. [Przedmioty, sklep i profil gracza [mainui_shop_enkephalin_box_scarce] — tekst] 보유한 엔케팔린 박스가 부족합니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_enkephalin_box_scarce].content
   limit: do 120 znaków
   EN: You don’t have enough Enkephalin Boxes.
   PL: Nie masz wystarczająco Skrzynek Enkefaliny.
655. [Przedmioty, sklep i profil gracza [mainui_shop_lunacy_scarce] — tekst] 보유한 광기가 부족합니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_lunacy_scarce].content
   limit: do 120 znaków
   EN: You don’t have enough Lunacy.
   PL: Nie masz wystarczająco Szaleństwa.
656. [Przedmioty, sklep i profil gracza [mainui_shop_limit_purchase_permanent] — tekst] {0}회 한정
   źródło: ShopUI.json :: dataList[id=mainui_shop_limit_purchase_permanent].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Left
   PL: Zostało {0}
657. [Przedmioty, sklep i profil gracza [mainui_shop_limit_purchase_periodic] — tekst] {0}회 가능
   źródło: ShopUI.json :: dataList[id=mainui_shop_limit_purchase_periodic].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} in Stock
   PL: {0} w Magazynie
658. [Przedmioty, sklep i profil gracza [mainui_shop_acquire_at_mailbox] — tekst] ※우편함에서 수령할 수 있습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_acquire_at_mailbox].content
   limit: do 120 znaków
   EN: ※ Redeemable at the mailbox.
   PL: ※ Do odbioru w skrzynce pocztowej.
659. [Przedmioty, sklep i profil gracza [mainui_shop_purchase_product_success] — tekst] {0}(을)를\n구입했습니다.
   źródło: ShopUI.json :: dataList[id=mainui_shop_purchase_product_success].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Successfully purchased\n{0}.
   PL: Pomyślnie zakupiono\n{0}.
660. [Przedmioty, sklep i profil gracza [mainui_shop_remain_days_minutes] — tekst] {0}일 {1}시간
   źródło: ShopUI.json :: dataList[id=mainui_shop_remain_days_minutes].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}D {1}H remain
   PL: {0}D {1}H pozostało
661. [Przedmioty, sklep i profil gracza [shopui_use_enkephalin_box] — tekst] 엔케팔린 박스 사용
   źródło: ShopUI.json :: dataList[id=shopui_use_enkephalin_box].content
   limit: do 120 znaków
   EN: Use Enkephalin Box
   PL: Użycie Skrzynki Enkefaliny
662. [Przedmioty, sklep i profil gracza [shopui_use_lunacy] — tekst] 광기 사용
   źródło: ShopUI.json :: dataList[id=shopui_use_lunacy].content
   limit: do 120 znaków
   EN: Use Lunacy
   PL: Użycie Szaleństwa
663. [Przedmioty, sklep i profil gracza [shopui_no_more_purchase_chance_today] — tekst] 금일 구매 횟수를 모두 소진하였습니다.
   źródło: ShopUI.json :: dataList[id=shopui_no_more_purchase_chance_today].content
   limit: do 120 znaków
   EN: Reached the daily purchase limit.
   PL: Wyczerpano dzienny limit zakupów.
664. [Przedmioty, sklep i profil gracza [shopui_scarce_lunacy] — tekst] 광기가 부족합니다.
   źródło: ShopUI.json :: dataList[id=shopui_scarce_lunacy].content
   limit: do 120 znaków
   EN: You don’t have enough Lunacy.
   PL: Nie masz wystarczająco Szaleństwa.
665. [Przedmioty, sklep i profil gracza [shopui_scarce_enkephalin_box] — tekst] 엔케팔린 박스가 부족합니다.
   źródło: ShopUI.json :: dataList[id=shopui_scarce_enkephalin_box].content
   limit: do 120 znaków
   EN: You don’t have enough Enkephalin Boxes.
   PL: Nie masz wystarczająco Skrzynek Enkefaliny.
666. [Przedmioty, sklep i profil gracza [shopui_scarce_enkephalin] — tekst] 엔케팔린이 부족합니다.
   źródło: ShopUI.json :: dataList[id=shopui_scarce_enkephalin].content
   limit: do 120 znaków
   EN: Insufficient Enkephalin.
   PL: Za mało Enkefaliny.
667. [Przedmioty, sklep i profil gracza [shopui_make_enkephalin_module] — tekst] 엔케팔린 모듈 제작
   źródło: ShopUI.json :: dataList[id=shopui_make_enkephalin_module].content
   limit: do 120 znaków
   EN: Assemble Enkephalin Modules
   PL: Produkcja Modułów Enkefaliny
668. [Przedmioty, sklep i profil gracza [shopui_charge_enkephalin_about] — tekst] 엔케팔린을 {0} 만큼 충전하시겠습니까?
   źródło: ShopUI.json :: dataList[id=shopui_charge_enkephalin_about].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Recharge {0} Enkephalin?
   PL: Naładować {0} Enkefaliny?
669. [Przedmioty, sklep i profil gracza [shopui_recover_enkephalin_after_time] — tekst] {0} 이후 엔케팔린 {1} 회복
   źródło: ShopUI.json :: dataList[id=shopui_recover_enkephalin_after_time].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} Enkephalin recovered in {0}.
   PL: {1} Enkefaliny odnowi się za {0}.
670. [Przedmioty, sklep i profil gracza [shopui_ask_create_enkephalin_module] — tekst] 엔케팔린 모듈을 제작하시겠습니까?
   źródło: ShopUI.json :: dataList[id=shopui_ask_create_enkephalin_module].content
   limit: do 120 znaków
   EN: Would you like to assemble Enkephalin Modules?
   PL: Czy wyprodukować Moduły Enkefaliny?
671. [Przedmioty, sklep i profil gracza [shopui_charge_as_lunacy] — tekst] 광기로 충전
   źródło: ShopUI.json :: dataList[id=shopui_charge_as_lunacy].content
   limit: do 120 znaków
   EN: Use Lunacy
   PL: Ładowanie za Szaleństwo
672. [Przedmioty, sklep i profil gracza [shopui_charge_as_box] — tekst] 박스로 충전
   źródło: ShopUI.json :: dataList[id=shopui_charge_as_box].content
   limit: do 120 znaków
   EN: Use Boxes
   PL: Ładowanie za Skrzynki
673. [Przedmioty, sklep i profil gracza [shopui_create_module] — tekst] 모듈 제작
   źródło: ShopUI.json :: dataList[id=shopui_create_module].content
   limit: do 120 znaków
   EN: Modules
   PL: Moduły
674. [Przedmioty, sklep i profil gracza [remain_days] — tekst] {0}일
   źródło: ShopUI.json :: dataList[id=remain_days].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}d
   PL: {0}d
675. [Przedmioty, sklep i profil gracza [remain_hours] — tekst] {0}시간
   źródło: ShopUI.json :: dataList[id=remain_hours].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}h
   PL: {0}h
676. [Przedmioty, sklep i profil gracza [remain_minutes] — tekst] {0}분
   źródło: ShopUI.json :: dataList[id=remain_minutes].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}m
   PL: {0}m
677. [Przedmioty, sklep i profil gracza [enkephalin_charge_finished] — tekst] 엔케팔린 충전 완료
   źródło: ShopUI.json :: dataList[id=enkephalin_charge_finished].content
   limit: do 120 znaków
   EN: Enkephalin Charged
   PL: Enkefalina Naładowana
678. [Przedmioty, sklep i profil gracza [unable_to_charge] — tekst] 충전 불가
   źródło: ShopUI.json :: dataList[id=unable_to_charge].content
   limit: do 120 znaków
   EN: Cannot Charge
   PL: Nie można ładować
679. [Przedmioty, sklep i profil gracza [lack_of_enkephalin_box] — tekst] 엔케팔린 박스 부족
   źródło: ShopUI.json :: dataList[id=lack_of_enkephalin_box].content
   limit: do 120 znaków
   EN: Not Enough Boxes
   PL: Za mało Skrzynek
680. [Przedmioty, sklep i profil gracza [enkephalin_full] — tekst] 엔케팔린 수치 최대
   źródło: ShopUI.json :: dataList[id=enkephalin_full].content
   limit: do 120 znaków
   EN: Max Enkephalin
   PL: Stan Enkefaliny maksymalny
681. [Przedmioty, sklep i profil gracza [purchase_limitation_full] — tekst] 구매 상한 도달
   źródło: ShopUI.json :: dataList[id=purchase_limitation_full].content
   limit: do 120 znaków
   EN: Purchase Limit Reached
   PL: Limit zakupów osiągnięty
682. [Przedmioty, sklep i profil gracza [lack_of_lunacy] — tekst] 광기 부족
   źródło: ShopUI.json :: dataList[id=lack_of_lunacy].content
   limit: do 120 znaków
   EN: Not Enough Lunacy
   PL: Za mało Szaleństwa
683. [Przedmioty, sklep i profil gracza [create_enkephalin_module_success] — tekst] 엔케팔린 모듈 제작 완료
   źródło: ShopUI.json :: dataList[id=create_enkephalin_module_success].content
   limit: do 120 znaków
   EN: Module Assembled
   PL: Moduł wyprodukowany
684. [Przedmioty, sklep i profil gracza [unable_to_create_enkephalin_module] — tekst] 엔케팔린 모듈 제작 불가
   źródło: ShopUI.json :: dataList[id=unable_to_create_enkephalin_module].content
   limit: do 120 znaków
   EN: Cannot Assemble Modules
   PL: Nie można wyprodukować Modułów
685. [Przedmioty, sklep i profil gracza [lack_of_enkephalin] — tekst] 엔케팔린 부족
   źródło: ShopUI.json :: dataList[id=lack_of_enkephalin].content
   limit: do 120 znaków
   EN: Not Enough Enkephalin
   PL: Za mało Enkefaliny
686. [Przedmioty, sklep i profil gracza [remain_days_with_number] — tekst] 남은 기간 {0}일
   źródło: ShopUI.json :: dataList[id=remain_days_with_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}d left
   PL: Pozostało {0}d
687. [Przedmioty, sklep i profil gracza [enkephalin_module] — tekst] 엔케팔린 모듈
   źródło: ShopUI.json :: dataList[id=enkephalin_module].content
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Przedmioty, sklep i profil gracza [enkephalin_box] — tekst] 엔케팔린 박스
   źródło: ShopUI.json :: dataList[id=enkephalin_box].content
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Przedmioty, sklep i profil gracza [today_purchase_count] — tekst] 금일 구매 횟수
   źródło: ShopUI.json :: dataList[id=today_purchase_count].content
   limit: do 120 znaków
   EN: Daily Count
   PL: Dzienny licznik
690. [Przedmioty, sklep i profil gracza [lack_of_lunacy_ask_to_move_shop] — tekst] 보유 광기가 부족합니다. 상점으로 이동하시겠습니까?
   źródło: ShopUI.json :: dataList[id=lack_of_lunacy_ask_to_move_shop].content
   limit: do 120 znaków
   EN: You don’t have enough Lunacy. Would you like to head to the shop?
   PL: Nie masz wystarczająco Szaleństwa. Przejść do sklepu?
691. [Przedmioty, sklep i profil gracza [remain_hours_with_number] — tekst] 남은 기간 {0}시간
   źródło: ShopUI.json :: dataList[id=remain_hours_with_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}h left
   PL: Pozostało {0}h
692. [Przedmioty, sklep i profil gracza [enkephalin_module_count_max] — tekst] 엔케팔린 모듈 수치 최대
   źródło: ShopUI.json :: dataList[id=enkephalin_module_count_max].content
   limit: do 120 znaków
   EN: Max Enkephalin Modules
   PL: Moduły Enkefaliny maksymalne
693. [Przedmioty, sklep i profil gracza [enkephalin_module_count_max_desc] — tekst] 엔케팔린 모듈 최대치를 초과하여 제작할 수 없습니다.
   źródło: ShopUI.json :: dataList[id=enkephalin_module_count_max_desc].content
   limit: do 120 znaków
   EN: Cannot assemble Modules; you have too many in storage.
   PL: Nie można wyprodukować Modułów — masz ich za dużo w magazynie.
694. [Przedmioty, sklep i profil gracza [mainui_shop_lunacy_package_tab] — tekst] 패키지 상점 2
   źródło: ShopUI.json :: dataList[id=mainui_shop_lunacy_package_tab].content
   limit: do 120 znaków
   EN: Packs #2
   PL: Pakiety #2
695. [Przedmioty, sklep i profil gracza [mainui_shop_until_season_finished] — tekst] 시즌 7 업데이트 전\n까지
   źródło: ShopUI.json :: dataList[id=mainui_shop_until_season_finished].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Until Season 7 Update
   PL: Do aktualizacji\nSezonu 7
696. [Przedmioty, sklep i profil gracza [mainui_shop_purchase] — tekst] 구매
   źródło: ShopUI.json :: dataList[id=mainui_shop_purchase].content
   limit: do 120 znaków
   EN: Purchase
   PL: Kup
697. [Przedmioty, sklep i profil gracza [mainui_shop_popup_title] — tekst] 상점
   źródło: ShopUI.json :: dataList[id=mainui_shop_popup_title].content
   limit: do 120 znaków
   EN: Shop
   PL: Sklep
698. [Przedmioty, sklep i profil gracza [paidShop_category_SPECIAL] — tekst] 특별
   źródło: ShopUI.json :: dataList[id=paidShop_category_SPECIAL].content
   limit: do 120 znaków
   EN: Special
   PL: Specjalne
699. [Przedmioty, sklep i profil gracza [paidShop_category_PACKAGE] — tekst] 패키지
   źródło: ShopUI.json :: dataList[id=paidShop_category_PACKAGE].content
   limit: do 120 znaków
   EN: Packs
   PL: Pakiety
700. [Przedmioty, sklep i profil gracza [paidShop_category_LUNACY] — tekst] 광기
   źródło: ShopUI.json :: dataList[id=paidShop_category_LUNACY].content
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Przedmioty, sklep i profil gracza [paidShop_category_GROWTH] — tekst] 성장
   źródło: ShopUI.json :: dataList[id=paidShop_category_GROWTH].content
   limit: do 120 znaków
   EN: Growth
   PL: Rozwój
702. [Przedmioty, sklep i profil gracza [returnpolicy_info_title] — tekst] 청약철회 안내
   źródło: ShopUI.json :: dataList[id=returnpolicy_info_title].content
   limit: do 120 znaków
   EN: Refund Policy
   PL: Informacja o zwrotach
703. [Przedmioty, sklep i profil gracza [paidShop_Tab_LIMITED] — tekst] 한정
   źródło: ShopUI.json :: dataList[id=paidShop_Tab_LIMITED].content
   limit: do 120 znaków
   EN: Limited
   PL: Limitowane
704. [Przedmioty, sklep i profil gracza [paidShop_Tab_WEEKLY] — tekst] 주간
   źródło: ShopUI.json :: dataList[id=paidShop_Tab_WEEKLY].content
   limit: do 120 znaków
   EN: Weekly
   PL: Tygodniowe
705. [Przedmioty, sklep i profil gracza [paidShop_Tab_MONTHLY] — tekst] 월간
   źródło: ShopUI.json :: dataList[id=paidShop_Tab_MONTHLY].content
   limit: do 120 znaków
   EN: Monthly
   PL: Miesięczne
706. [Przedmioty, sklep i profil gracza [paidShop_Tab_ALWAYS] — tekst] 상시
   źródło: ShopUI.json :: dataList[id=paidShop_Tab_ALWAYS].content
   limit: do 120 znaków
   EN: Always Available
   PL: Zawsze dostępne
707. [Przedmioty, sklep i profil gracza [go_to_mail_popup] — tekst] 우편함으로 이동
   źródło: ShopUI.json :: dataList[id=go_to_mail_popup].content
   limit: do 120 znaków
   EN: To Inbox
   PL: Do skrzynki pocztowej
708. [Przedmioty, sklep i profil gracza [membership_remain_side_title] — tekst] [패키지 기간 알림]
   źródło: ShopUI.json :: dataList[id=membership_remain_side_title].content
   limit: do 120 znaków
   EN: [Pack Expiry Notice]
   PL: [Powiadomienie o wygaśnięciu pakietu]
709. [Przedmioty, sklep i profil gracza [membership_remain_side_desc] — tekst] {0}의 이용 기간이 {1}일 남았습니다.
   źródło: ShopUI.json :: dataList[id=membership_remain_side_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} day(s) remaining for your {0}.
   PL: Pozostało {1} dni ważności {0}.
710. [Przedmioty, sklep i profil gracza [returnpolicy_table_battlePassPackge] — tekst] 림버스 패스 패키지
   źródło: ShopUI.json :: dataList[id=returnpolicy_table_battlePassPackge].content
   limit: do 120 znaków
   EN: Limbus Pass Package
   PL: Pakiet Limbus Pass
711. [Przedmioty, sklep i profil gracza [paid_runacy_lack] — tekst] 유료 광기가 부족하여 구매할 수 없습니다.
   źródło: ShopUI.json :: dataList[id=paid_runacy_lack].content
   limit: do 120 znaków
   EN: Not enough paid Lunacy.
   PL: Nie można kupić — za mało Płatnego Szaleństwa.
712. [Przedmioty, sklep i profil gracza [membership_remain_side_desc_oneDay] — tekst] {0}의 이용 기간 만료일입니다.
   źródło: ShopUI.json :: dataList[id=membership_remain_side_desc_oneDay].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} expires today.
   PL: {0} wygasa dzisiaj.
713. [Przedmioty, sklep i profil gracza [restore_purchase_btn] — tekst] 구매 복구
   źródło: ShopUI.json :: dataList[id=restore_purchase_btn].content
   limit: do 120 znaków
   EN: Restore Purchase
   PL: Przywróć Zakup
714. [Przedmioty, sklep i profil gracza [restore_purchase_no_product] — tekst] 복구 가능한 상품이 없습니다.
   źródło: ShopUI.json :: dataList[id=restore_purchase_no_product].content
   limit: do 120 znaków
   EN: No product available for restoration.
   PL: Brak produktów do przywrócenia.
715. [Przedmioty, sklep i profil gracza [restore_purchase_succeed] — tekst] 미수령 상품의 복구가 완료되었습니다.
   źródło: ShopUI.json :: dataList[id=restore_purchase_succeed].content
   limit: do 120 znaków
   EN: Your unclaimed products have been restored.
   PL: Przywrócono nieodebrane produkty.
716. [Przedmioty, sklep i profil gracza [paid_already] — tekst] 이미 구매한 상품입니다.
   źródło: ShopUI.json :: dataList[id=paid_already].content
   limit: do 120 znaków
   EN: This item has already been purchased.
   PL: Ten produkt został już kupiony.

## Przedmioty, sklep i profil gracza: UserBanner-a1c7p3
- plik gry: `UserBanner-a1c7p3.json`

717. [Przedmioty, sklep i profil gracza [44] — nazwa — tylko EN w danych gry] Season 5 Celebratory Banner
   źródło: UserBanner-a1c7p3.json :: dataList[id=44].name
   limit: do 40 znaków
   EN: Season 5 Celebratory Banner
   PL: Banner Świętowania Sezonu 5
718. [Przedmioty, sklep i profil gracza [44] — opis — tylko EN w danych gry] Obtained at Season 5 Free Pass Level 1
   źródło: UserBanner-a1c7p3.json :: dataList[id=44].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie Darmowej Przepustki Sezonu 5
719. [Przedmioty, sklep i profil gracza [45] — nazwa — tylko EN w danych gry] Season 5 Completion Banner
   źródło: UserBanner-a1c7p3.json :: dataList[id=45].name
   limit: do 40 znaków
   EN: Season 5 Completion Banner
   PL: Banner Ukończenia Sezonu 5
720. [Przedmioty, sklep i profil gracza [45] — opis — tylko EN w danych gry] Obtained at Season 5 Limbus Pass Level 120
   źródło: UserBanner-a1c7p3.json :: dataList[id=45].desc
   limit: do 120 znaków
   EN: Obtained at Season 5 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 5
721. [Przedmioty, sklep i profil gracza [46] — nazwa — tylko EN w danych gry] Season 5 Limbus Package Special Banner
   źródło: UserBanner-a1c7p3.json :: dataList[id=46].name
   limit: do 60 znaków
   EN: Season 5 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 5
722. [Przedmioty, sklep i profil gracza [46] — opis — tylko EN w danych gry] Obtained from Season 5 Limbus Pass Package
   źródło: UserBanner-a1c7p3.json :: dataList[id=46].desc
   limit: do 120 znaków
   EN: Obtained from Season 5 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 5
723. [Przedmioty, sklep i profil gracza [47] — nazwa — tylko EN w danych gry] Season 5 Limbus Package Special Banner II
   źródło: UserBanner-a1c7p3.json :: dataList[id=47].name
   limit: do 60 znaków
   EN: Season 5 Limbus Package Special Banner II
   PL: Specjalny Banner Pakietu Limbus Sezonu 5 II
724. [Przedmioty, sklep i profil gracza [47] — opis — tylko EN w danych gry] Obtained from Season 5 Limbus Pass Package
   źródło: UserBanner-a1c7p3.json :: dataList[id=47].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserBanner-a1c8p1
- plik gry: `UserBanner-a1c8p1.json`

725. [Przedmioty, sklep i profil gracza [60] — nazwa — tylko EN w danych gry] Season 6 Celebratory Banner
   źródło: UserBanner-a1c8p1.json :: dataList[id=60].name
   limit: do 40 znaków
   EN: Season 6 Celebratory Banner
   PL: Banner Świętowania Sezonu 6
726. [Przedmioty, sklep i profil gracza [60] — opis — tylko EN w danych gry] Obtained at Season 6 Free Pass Level 1
   źródło: UserBanner-a1c8p1.json :: dataList[id=60].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie Darmowej Przepustki Sezonu 6
727. [Przedmioty, sklep i profil gracza [61] — nazwa — tylko EN w danych gry] Season 6 Completion Banner
   źródło: UserBanner-a1c8p1.json :: dataList[id=61].name
   limit: do 40 znaków
   EN: Season 6 Completion Banner
   PL: Banner Ukończenia Sezonu 6
728. [Przedmioty, sklep i profil gracza [61] — opis — tylko EN w danych gry] Obtained at Season 6 Limbus Pass Level 120
   źródło: UserBanner-a1c8p1.json :: dataList[id=61].desc
   limit: do 120 znaków
   EN: Obtained at Season 6 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 6
729. [Przedmioty, sklep i profil gracza [62] — nazwa — tylko EN w danych gry] Season 6 Limbus Package Special Banner
   źródło: UserBanner-a1c8p1.json :: dataList[id=62].name
   limit: do 60 znaków
   EN: Season 6 Limbus Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Sezonu 6
730. [Przedmioty, sklep i profil gracza [62] — opis — tylko EN w danych gry] Obtained from Season 6 Limbus Pass Package
   źródło: UserBanner-a1c8p1.json :: dataList[id=62].desc
   limit: do 120 znaków
   EN: Obtained from Season 6 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 6
731. [Przedmioty, sklep i profil gracza [63] — nazwa — tylko EN w danych gry] Magical Girl
   źródło: UserBanner-a1c8p1.json :: dataList[id=63].name
   limit: do 40 znaków
   EN: Magical Girl
   PL: Czarodziejska Panienka
732. [Przedmioty, sklep i profil gracza [63] — opis — tylko EN w danych gry] Obtained from the 6th Walpurgis Night event
   źródło: UserBanner-a1c8p1.json :: dataList[id=63].desc
   limit: do 120 znaków
   EN: Obtained from the 6th Walpurgis Night event
   PL: Zdobyto z wydarzenia 6. Nocy Walpurgii
733. [Przedmioty, sklep i profil gracza [64] — nazwa — tylko EN w danych gry] Spring Cultivation
   źródło: UserBanner-a1c8p1.json :: dataList[id=64].name
   limit: do 40 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
734. [Przedmioty, sklep i profil gracza [64] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserBanner-a1c8p1.json :: dataList[id=64].desc
   limit: do 120 znaków
   EN: Obtained from the 'Spring Cultivation' event
   PL: Zdobyto z wydarzenia „Wiosenny Szlif”
735. [Przedmioty, sklep i profil gracza [65] — nazwa — tylko EN w danych gry] Spring Cultivation - Special Banner
   źródło: UserBanner-a1c8p1.json :: dataList[id=65].name
   limit: do 50 znaków
   EN: Spring Cultivation - Special Banner
   PL: Wiosenny Szlif — Specjalny Banner
736. [Przedmioty, sklep i profil gracza [65] — opis — tylko EN w danych gry] Obtained from the 'Spring Cultivation' event
   źródło: UserBanner-a1c8p1.json :: dataList[id=65].desc
   (powtórzenie elementu 734 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Przedmioty, sklep i profil gracza [69] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion
   źródło: UserBanner-a1c8p1.json :: dataList[id=69].name
   limit: do 40 znaków
   EN: Pilgrimage of Compassion
   PL: Pielgrzymka Współczucia
738. [Przedmioty, sklep i profil gracza [69] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserBanner-a1c8p1.json :: dataList[id=69].desc
   limit: do 120 znaków
   EN: Obtained from the Pilgrimage of Compassion event
   PL: Zdobyto z wydarzenia Pielgrzymki Współczucia
739. [Przedmioty, sklep i profil gracza [70] — nazwa — tylko EN w danych gry] Pilgrimage of Compassion - Special Banner
   źródło: UserBanner-a1c8p1.json :: dataList[id=70].name
   limit: do 60 znaków
   EN: Pilgrimage of Compassion - Special Banner
   PL: Pielgrzymka Współczucia — Specjalny Banner
740. [Przedmioty, sklep i profil gracza [70] — opis — tylko EN w danych gry] Obtained from the Pilgrimage of Compassion event
   źródło: UserBanner-a1c8p1.json :: dataList[id=70].desc
   (powtórzenie elementu 738 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: UserBanner
- plik gry: `UserBanner.json`

741. [Przedmioty, sklep i profil gracza [1] — nazwa] 시즌 1 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Season 1 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 1
742. [Przedmioty, sklep i profil gracza [1] — opis] 시즌 1 오리엔테이션 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=1].desc
   limit: do 120 znaków
   EN: Obtained at Season 1 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 1: Orientation
743. [Przedmioty, sklep i profil gracza [2] — nazwa] 시즌 1 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Season 1 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 1
744. [Przedmioty, sklep i profil gracza [2] — opis] 시즌 1 오리엔테이션 림버스 패스 보상 60레벨에 획득
   źródło: UserBanner.json :: dataList[id=2].desc
   limit: do 120 znaków
   EN: Obtained at Season 1 Limbus Pass Level 60
   PL: Zdobyto na 60. Poziomie Limbus Pass Sezonu 1: Orientation
745. [Przedmioty, sklep i profil gracza [3] — nazwa] 근무 실적 우수 사원
   źródło: UserBanner.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Proof of Diligent Attendance
   PL: Świadectwo Pilnej Obecności
746. [Przedmioty, sklep i profil gracza [3] — opis] 신입 관리자 근태 보상 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=3].desc
   limit: do 120 znaków
   EN: Obtained from the New-hire’s Attendance Rewards event.
   PL: Zdobyto z wydarzenia nagród obecności nowo zatrudnionych Zarządców.
747. [Przedmioty, sklep i profil gracza [4] — nazwa] 상냥한 관리자
   źródło: UserBanner.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Kind Manager
   PL: Łagodny Zarządca
748. [Przedmioty, sklep i profil gracza [4] — opis] 신입 관리자 근태 보상 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=4].desc
   (powtórzenie elementu 746 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Przedmioty, sklep i profil gracza [5] — nazwa] 거울굴절철도 1호선 기념 배너 I
   źródło: UserBanner.json :: dataList[id=5].name
   limit: do 60 znaków
   EN: Refraction Railway Line 1 Basic Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 1 I
750. [Przedmioty, sklep i profil gracza [5] — opis] 거울굴절철도 1호선 13단계 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=5].desc
   limit: do 120 znaków
   EN: Obtained by clearing Station 13 of Refraction Railway Line 1.
   PL: Zdobyto za ukończenie 13. Stacji Kolei Załamania — Linia 1.
751. [Przedmioty, sklep i profil gracza [6] — nazwa] 거울굴절철도 1호선 기념 배너 II
   źródło: UserBanner.json :: dataList[id=6].name
   limit: do 60 znaków
   EN: Refraction Railway Line 1 Decorated Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 1 II
752. [Przedmioty, sklep i profil gracza [6] — opis] 거울굴절철도 1호선 13단계 클리어, 누적 턴 120 이하 시 획득
   źródło: UserBanner.json :: dataList[id=6].desc
   limit: do 120 znaków
   EN: Obtained by clearing Station 13 of Refraction Railway Line 1 under 120 Total Turns.
   PL: Zdobyto za ukończenie 13. Stacji Kolei Załamania — Linia 1 w limicie 120 tur łącznych.
753. [Przedmioty, sklep i profil gracza [7] — nazwa] 거울굴절철도 1호선 기념 배너 III
   źródło: UserBanner.json :: dataList[id=7].name
   limit: do 60 znaków
   EN: Refraction Railway Line 1 Embellished Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 1 III
754. [Przedmioty, sklep i profil gracza [7] — opis] 거울굴절철도 1호선 13단계 클리어, 누적 턴 120 이하 조건을 이벤트 2주차에 완료 시 획득
   źródło: UserBanner.json :: dataList[id=7].desc
   limit: do 160 znaków
   EN: Obtained by clearing Station 13 of Refraction Railway Line 1 under 120 Total Turns during the first two weeks of the event.
   PL: Zdobyto za ukończenie 13. Stacji Kolei Załamania — Linia 1 w limicie 120 tur łącznych w pierwszych dwóch tygodniach wydarzenia.
755. [Przedmioty, sklep i profil gracza [8] — nazwa] 헬스 치킨
   źródło: UserBanner.json :: dataList[id=8].name
   limit: do 40 znaków
   EN: Hell’s Chicken
   PL: Piekielny Kurczak
756. [Przedmioty, sklep i profil gracza [8] — opis] 헬스 치킨 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=8].desc
   limit: do 120 znaków
   EN: Obtained from the Hell’s Chicken event.
   PL: Zdobyto z wydarzenia Piekielnego Kurczaka.
757. [Przedmioty, sklep i profil gracza [9] — nazwa] 어머니께...
   źródło: UserBanner.json :: dataList[id=9].name
   limit: do 40 znaków
   EN: To My Mother…
   PL: Dla Mojej Matki…
758. [Przedmioty, sklep i profil gracza [9] — opis] 헬스 치킨 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=9].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Przedmioty, sklep i profil gracza [10] — nazwa] 시즌 2 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=10].name
   limit: do 40 znaków
   EN: Season 2 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 2
760. [Przedmioty, sklep i profil gracza [10] — opis] 시즌 2 레미니센스 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=10].desc
   limit: do 120 znaków
   EN: Obtained at Season 2 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 2: Reminiscence
761. [Przedmioty, sklep i profil gracza [11] — nazwa] 시즌 2 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=11].name
   limit: do 40 znaków
   EN: Season 2 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 2
762. [Przedmioty, sklep i profil gracza [11] — opis] 시즌 2 레미니센스 림버스 패스 보상 60레벨에 획득
   źródło: UserBanner.json :: dataList[id=11].desc
   limit: do 120 znaków
   EN: Obtained at Season 2 Limbus Pass Level 60
   PL: Zdobyto na 60. Poziomie Limbus Pass Sezonu 2: Reminiscence
763. [Przedmioty, sklep i profil gracza [12] — nazwa] 우.미.다 장식 배너
   źródło: UserBanner.json :: dataList[id=12].name
   limit: do 50 znaków
   EN: S.E.A Event Ornamental Banner
   PL: Ozdobny Banner M.O.R.Z.E.
764. [Przedmioty, sklep i profil gracza [12] — opis] 우.미.다 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=12].desc
   limit: do 120 znaków
   EN: Obtained from the S.E.A event.
   PL: Zdobyto z wydarzenia M.O.R.Z.E.
765. [Przedmioty, sklep i profil gracza [13] — nazwa] 거울굴절철도 2호선 기념 배너 I
   źródło: UserBanner.json :: dataList[id=13].name
   limit: do 60 znaków
   EN: Refraction Railway Line 2 Basic Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 2 I
766. [Przedmioty, sklep i profil gracza [13] — opis] 순환 횟수 3 이상으로 2호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=13].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 2 with 3 or more Cycle Counts
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 3 lub więcej
767. [Przedmioty, sklep i profil gracza [14] — nazwa] 거울굴절철도 2호선 기념 배너 II
   źródło: UserBanner.json :: dataList[id=14].name
   limit: do 60 znaków
   EN: Refraction Railway Line 2 Decorated Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 2 II
768. [Przedmioty, sklep i profil gracza [14] — opis] 순환 횟수 5 이상으로 2호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=14].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycle Counts
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej
769. [Przedmioty, sklep i profil gracza [15] — nazwa] 거울굴절철도 2호선 기념 배너 III
   źródło: UserBanner.json :: dataList[id=15].name
   limit: do 60 znaków
   EN: Refraction Railway Line 2 Embellished Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 2 III
770. [Przedmioty, sklep i profil gracza [15] — opis] 순환 횟수 5 이상, 누적 턴 수 200턴 이하로 2호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=15].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycle Counts and under 200 Total Turns
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej i limitem 200 tur łącznych
771. [Przedmioty, sklep i profil gracza [16] — nazwa] 거울굴절철도 2호선 특별 기념 배너 I
   źródło: UserBanner.json :: dataList[id=16].name
   limit: do 70 znaków
   EN: Special Refraction Railway Line 2 Basic Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 2 I
772. [Przedmioty, sklep i profil gracza [16] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 3 이상으로 2호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=16].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 2 with 3 or more Cycle Counts before Season 2: Reminiscence ends
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 3 lub więcej przed końcem Sezonu 2: Reminiscence
773. [Przedmioty, sklep i profil gracza [17] — nazwa] 거울굴절철도 2호선 특별 기념 배너 II
   źródło: UserBanner.json :: dataList[id=17].name
   limit: do 70 znaków
   EN: Special Refraction Railway Line 2 Decorated Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 2 II
774. [Przedmioty, sklep i profil gracza [17] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상으로 2호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=17].desc
   limit: do 120 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycle Counts before Season 2: Reminiscence ends
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej przed końcem Sezonu 2: Reminiscence
775. [Przedmioty, sklep i profil gracza [18] — nazwa] 거울굴절철도 2호선 특별 기념 배너 III
   źródło: UserBanner.json :: dataList[id=18].name
   limit: do 70 znaków
   EN: Special Refraction Railway Line 2 Embellished Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 2 III
776. [Przedmioty, sklep i profil gracza [18] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 200턴 이하로 2호선 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=18].desc
   limit: do 160 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycle Counts and 200 or less Total Turns before Season 2: Reminiscence ends
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej i limitem 200 tur łącznych przed końcem Sezonu 2: Reminiscence
777. [Przedmioty, sklep i profil gracza [19] — nazwa] 거울굴절철도 2호선 특별 기념 배너 IV
   źródło: UserBanner.json :: dataList[id=19].name
   limit: do 80 znaków
   EN: Special Refraction Railway Line 2 Distinguished Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 2 IV
778. [Przedmioty, sklep i profil gracza [19] — opis] 시즌 2 레미니센스 기간 내에 순환 횟수 5 이상, 누적 턴 수 150턴 이하로 2호선 클리어 시 획득 (단, 23/09/15 20:15 (KST) 이후에 새롭게 시작한 기록을 기준으로 함)
   źródło: UserBanner.json :: dataList[id=19].desc
   limit: do 220 znaków
   EN: Obtained by clearing Line 2 with 5 or more Cycles and under 150 Total Turns before the end of Season 2: Reminiscence (Must be a record made after 2023.09.15 20:15(KST))
   PL: Zdobyto za ukończenie Linii 2 z liczbą Cykli 5 lub więcej i limitem 150 tur łącznych przed końcem Sezonu 2: Reminiscence (dotyczy rekordów rozpoczętych po 23/09/15 20:15 (KST))
779. [Przedmioty, sklep i profil gracza [20] — nazwa] 시즌 3 시작 기념 배너
   źródło: UserBanner.json :: dataList[id=20].name
   limit: do 40 znaków
   EN: Season 3 Celebratory Banner
   PL: Banner Uczczenia Startu Sezonu 3
780. [Przedmioty, sklep i profil gracza [20] — opis] 시즌 3 본 보야지 무료 보상 1레벨에 획득
   źródło: UserBanner.json :: dataList[id=20].desc
   limit: do 120 znaków
   EN: Obtained at Season 3 Free Pass Level 1
   PL: Zdobyto na 1. Poziomie darmowych nagród Sezonu 3: Bon Voyage
781. [Przedmioty, sklep i profil gracza [21] — nazwa] 시즌 3 완료 기념 배너
   źródło: UserBanner.json :: dataList[id=21].name
   limit: do 40 znaków
   EN: Season 3 Completion Banner
   PL: Banner Uczczenia Ukończenia Sezonu 3
782. [Przedmioty, sklep i profil gracza [21] — opis] 시즌 3 본 보야지 림버스 패스 보상 120레벨에 획득
   źródło: UserBanner.json :: dataList[id=21].desc
   limit: do 120 znaków
   EN: Obtained at Season 3 Limbus Pass Level 120
   PL: Zdobyto na 120. Poziomie Limbus Pass Sezonu 3: Bon Voyage
783. [Przedmioty, sklep i profil gracza [22] — nazwa] 시즌 3 림버스 패키지 특별 배너
   źródło: UserBanner.json :: dataList[id=22].name
   limit: do 60 znaków
   EN: Season 3 Limbus Pass Package Special Banner
   PL: Specjalny Banner Pakietu Limbus Pass Sezonu 3
784. [Przedmioty, sklep i profil gracza [22] — opis] 시즌 3 본 보야지 림버스 패스 패키지 구매 시 획득
   źródło: UserBanner.json :: dataList[id=22].desc
   limit: do 120 znaków
   EN: Obtained from Season 3 Limbus Pass Package
   PL: Zdobyto z Pakietu Limbus Pass Sezonu 3
785. [Przedmioty, sklep i profil gracza [23] — nazwa] 20번구의 기적
   źródło: UserBanner.json :: dataList[id=23].name
   limit: do 40 znaków
   EN: Miracle in District 20
   PL: Cud w Dystrykcie 20
786. [Przedmioty, sklep i profil gracza [23] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=23].desc
   limit: do 120 znaków
   EN: Obtained from the Miracle in District 20 Event
   PL: Zdobyto z wydarzenia Cud w Dystrykcie 20
787. [Przedmioty, sklep i profil gracza [24] — nazwa] 20번구의 기적 - 특별 배너
   źródło: UserBanner.json :: dataList[id=24].name
   limit: do 60 znaków
   EN: Miracle in District 20 - Special Banner
   PL: Cud w Dystrykcie 20 — Specjalny Banner
788. [Przedmioty, sklep i profil gracza [24] — opis] 20번구의 기적 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=24].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Przedmioty, sklep i profil gracza [25] — nazwa] 2024 - 녹빛 여명
   źródło: UserBanner.json :: dataList[id=25].name
   limit: do 40 znaków
   EN: 2024 - Dawn of Green
   PL: 2024 — Świt Zieleni
790. [Przedmioty, sklep i profil gracza [25] — opis] 제2회 발푸르기스의 밤 이벤트에서 획득
   źródło: UserBanner.json :: dataList[id=25].desc
   limit: do 120 znaków
   EN: Obtained from the 2nd Walpurgis Night Event
   PL: Zdobyto z wydarzenia 2. Nocy Walpurgii
791. [Przedmioty, sklep i profil gracza [26] — nazwa] 거울굴절철도 3호선 기념 배너 I
   źródło: UserBanner.json :: dataList[id=26].name
   limit: do 60 znaków
   EN: Refraction Railway Line 3 Basic Banner
   PL: Banner Pamiątkowy Kolei Załamania — Linia 3 I
792. [Przedmioty, sklep i profil gracza [26] — opis] 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: UserBanner.json :: dataList[id=26].desc
   limit: do 120 znaków
   EN: Obtained by clearing the Terminus of Refraction Railway Line 3
   PL: Zdobyto za ukończenie stacji końcowej Kolei Załamania — Linia 3.
793. [Przedmioty, sklep i profil gracza [27] — nazwa] 거울굴절철도 3호선 특별 기념 배너 I
   źródło: UserBanner.json :: dataList[id=27].name
   limit: do 70 znaków
   EN: Special Refraction Railway Line 3 Basic Banner
   PL: Specjalny Banner Pamiątkowy Kolei Załamania — Linia 3 I
