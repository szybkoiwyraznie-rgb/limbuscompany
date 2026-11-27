# Limbus Company — Faust: Identity

*Profil postaci: dane liczbowe z tabel gry, opisy z plików lokalizacji.*

## Zakres i zasady odczytu

- Teksty w wersji `pl`; wpisy bez przekładu pozostają w oryginale (angielskim); liczby z `StaticData` (wartości bazowe, bez E.G.O i bonusów).
- **Ulepszenie** = Uptie (gaksung) 1–4; tabela umiejętności pokazuje tylko wiersze, w których coś się zmienia. Moc ataku = moc bazowa + moc monety za każdą wyrzuconą reszkę/orła wg reguł gry.
- **Poziom ataku/obrony** to korekta względem poziomu postaci.
- **Odporności**: mnożnik obrażeń danego typu (×2 = Fatal, ×0,5 = Endured).
- Elementy bez opisu w danych są oznaczone „—”, nie zgadywane.

## Akta więźnia

> Grzesznica, która opracowała silnik Mephistophelesa, autobusu Limbus Company.
> Twierdzi, że w całym Mieście nikt nie dorównuje jej wiedzą ani mądrością,
> i nie ma w tym przesady. Może pana razić jej postawa, jakby rozmawiała
> z Kierownikiem wyłącznie z konieczności. Ponieważ tę samą wyniosłość,
> skrywaną przed światem, okazuje wszystkim, nie ma szans na poprawę;
> zalecamy po prostu kiwnąć głową. To geniusz jak nikt inny, ale my
> nie wiemy, jak z niego korzystać. Może to pan odkryje?

## Katalog Identity

| Rzadkość | Identity                                 |           Sezon | Grzech wyróżniony | Słowa kluczowe        |
| -------: | ---------------------------------------- | --------------: | ----------------- | --------------------- |
|        0 | LCB Grzesznik                            |               0 | Pycha             | —                     |
|       00 | W Corp. L2 Agentka Oczyszczania          |               0 | Zawiść            | Ładowanie             |
|       00 | Ocalała pracownica Lobotomy Corporation  |               1 | Żądza             | Rozdarcie, Oddech     |
|      000 | Ta, Która Ściska                         |               1 | Żądza             | Krwawienie            |
|       00 | Południowe Stowarzyszenie Zwei Sekcja 4  |               0 | Zawiść            | —                     |
|      000 | Południowe Stowarzyszenie Seven Sekcja 4 |               0 | Obżar.            | Rozdarcie             |
|      000 | Lobotomy E.G.O:: Skrucha                 | wydarzenie 9101 | Gniew             | Wstrząs               |
|      000 | Ród Ostrza Salsu                         |               3 | Pycha             | Oddech, Krwawienie    |
|       00 | Wichrowe Wzgórza Kamerdyner              |               4 | Pycha             | Zatonięcie            |
|      000 | Biuro MultiCrack Szefowa                 |               4 | Posępność         | Ładowanie             |
|      000 | LCE E.G.O:: Gwiazda Żarzącego Kwiatu     |               5 | Gniew             | Podpalenie            |
|      000 | Wataha Heishou - Gałąź Mao, Adept        |               6 | Obżar.            | Rozdarcie             |
|      000 | Wschodnie Stowarzyszenie Shi Sekcja 3    |               0 | Gniew             | Krwawienie, Oddech    |
|      000 | Akolitka Wskazującego: 【Karteczka】     |               7 | Lenistwo          | Oddech, Zatonięcie    |
|      000 | Dom Pajęczyn: Uczeń Serdecznego          |               7 | Obżar.            | Krwawienie, Ładowanie |
|      000 | Biuro Świtu Fikser                       | wydarzenie 9109 | Pycha             | Podpalenie, Wstrząs   |

## Profile

### 0 LCB Grzesznik — Faust

> Pierwsza Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 0                                                           |
| Sezon                     | 0                                                           |
| HP                        | 84 (+2,9 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 1–3 / 2–3 / 2–4 / 2–4                                       |
| Poziom obrony             | poziom +1                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×0,5 (Endured), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 60% / 30% / 15%                                             |
| Grzech wyróżniony         | Pycha                                                       |
| Przynależność             | Limbus_Company, Limbus_Company_Lcb                          |
| Słowa kluczowe            | —                                                           |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Cięcie w Dół

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Obuch |          2 |         +7 |      1 |           −1 |    1 |
|          3 | Pycha  | Obuch |          3 |         +7 |      1 |           −1 |    1 |
|          4 | Pycha  | Obuch |          4 |         +7 |      1 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Nakłada 1 Paraliżu

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Nakłada 1 Paraliżu

#### Umiejętność 2 (×2): Cięcie w Górę

| Ulepszenie | Grzech   | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Obuch |          3 |         +4 |      2 |           −1 |    1 |
|          3 | Lenistwo | Obuch |          4 |         +4 |      2 |           −1 |    1 |
|          4 | Lenistwo | Obuch |          5 |         +4 |      2 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Trafienie Awersem] Nakłada w następnej turze 2 Spadku Poziomu Ataku

*Od ulepszenia 2:* Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 3 Spadku Poziomu Ataku

#### Umiejętność 3 (×1): Wiercące Pchnięcie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Kłucie |          6 |         +2 |      2 |           −1 |    1 |
|          4 | Obżar. | Kłucie |          7 |         +2 |      2 |           −1 |    1 |

Moneta 1: [Trafienie Awersem] Nakłada w następnej turze 1 Spadku Mocy Ataku  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 Spadku Mocy Ataku

#### Obrona: Unik

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          2 |        +10 |      1 |           +1 |    1 |
|          4 | Pycha   | obrona: unik |          2 |        +10 |      1 |           +1 |    1 |

#### Pasywka bojowa: Analiza

*od ulepszenia 1; rezonans 2× Pycha*

Zadaje +10% obrażeń celom z negatywnymi efektami

#### Pasywka wsparcia: Obserwacja

*od ulepszenia 3; posiadane 3× Pycha*

1 Sojusznik z najwyższym Maks. HP: przy trafieniu atakiem z 25% szansą nakłada 2 Spadku Poziomu Ataku

#### Kwestie

- **Identity Acquisition:** It’s Faust. A genius with whom you’re lucky to cross paths even once in your life.
- **Morning Greeting:** I would always get up after three hours of sleep. I thought it was a natural phenomenon, but I later learned it wasn’t the case for every individual.
- **Afternoon Greeting:** Faust considers short periods of exposure to sunlight to be a useful activity.
- **Evening Greeting:** Though I don’t bother myself much with hobbies, I once enjoyed stargazing.
- **Chatter #1:** …If you’re the type of person who likes to summon others before considering what to say, I would suggest using documents to communicate.
- **Chatter #2:** I’m considering adjusting my level of speech for different Sinners. Repeating myself twice or more can be rather inefficient.
- **Chatter #3:** Dante, I want you to understand that omniscience does not necessarily mean a willingness to answer your every question.
- **Idle:** Brief deviations are within permitted ranges.
- **Deployment:** I’ll tag along.
- **Stage Entry:** I’m ready to accompany you.
- **Viewed in Battle:** What is it, Manager?
- **Commencing Attack:** Commencing action.
- **Enemy Stagger:** An opportunity has arrived.
- **Staggered:** Ugh!
- **Enemy Killed:** An obvious outcome.
- **Ally Death:** That wasn’t the most efficient.
- **Check Passed:** Try not to cling to this success.
- **Check Failed:** Try not to dwell on this failure.
- **Victory Cry:** Is there a reason to be excited over this?
- **Extra Conditions Fulfilled:** You’ve become more competent than once expected.
- **Defeat Wail:** Much wasn’t expected out of you.

### 00 W Corp. L2 Agentka Oczyszczania — Faust

> Druga Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 0                                                           |
| HP                        | 88 (+3,05 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 1–3 / 2–3 / 2–4 / 2–4                                       |
| Poziom obrony             | poziom +3                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×0,5 (Endured), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 60% / 30%                                                   |
| Grzech wyróżniony         | Zawiść                                                      |
| Przynależność             | W_Corp                                                      |
| Słowa kluczowe            | Ładowanie                                                   |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Obieg Energii

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Obuch |          3 |         +6 |      1 |           −1 |    1 |
|          3 | Zawiść | Obuch |          4 |         +6 |      1 |           −1 |    1 |
|          4 | Zawiść | Obuch |          4 |         +8 |      1 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik Ładowania o 1

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Zyskuje +2 Licznika Ładowania

*Od ulepszenia 4:* [Przy Użyciu] Zyskuje +2 Licznika Ładowania  
Moneta 1: [Przy Trafieniu] Zyskuje +2 Licznika Ładowania

#### Umiejętność 2 (×2): Skok

| Ulepszenie | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Obuch |          4 |         +4 |      2 |           −1 |    1 |
|          3 | Posępność | Obuch |          5 |         +4 |      2 |           −1 |    1 |
|          4 | Posępność | Obuch |          6 |         +4 |      2 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Przy Trafieniu] Zużywa 3 Licznika Ładowania, aby w następnej turze nałożyć 4 Spętania

*Od ulepszenia 2:* Moneta 2: [Przy Trafieniu] Zużywa 3 Licznika Ładowania, aby w następnej turze nałożyć 4 Spętania

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa własny Licznik Ładowania o 3  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik Ładowania o 3  
Moneta 2: [Przy Trafieniu] Zużywa 3 Licznika Ładowania, aby w następnej turze nałożyć 4 Spętania

#### Umiejętność 3 (×1): Nadładowanie

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Obuch |          6 |         +2 |      3 |           −1 |    1 |
|          4 | Gniew  | Obuch |          6 |         +3 |      3 |           −1 |    1 |

*Od ulepszenia 3:* Moneta 3: [Przy Trafieniu] Zużywa 5 Licznika Ładowania, aby w następnej turze nałożyć 2 Spadku Mocy Ataku. Nakłada 3 Paraliżu

*Od ulepszenia 4:* Przy 5+ Licznikach Ładowania Moc Starcia +2  
Moneta 3: [Przy Trafieniu] Zużywa 5 Licznika Ładowania, aby w następnej turze nałożyć 2 Spadku Mocy Ataku. Nakłada 3 Paraliżu

#### Obrona: Garda

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +2 |      1 |           +5 |    1 |
|          4 | Zawiść  | obrona: blok |         10 |         +2 |      1 |           +5 |    1 |

#### Pasywka bojowa: Samoładowanie

*od ulepszenia 2; posiadane 4× Zawiść*

Zyskuje 1 Licznik Ładowania na koniec ataku

#### Pasywka bojowa: Self-charging

*od ulepszenia 4; posiadane 4× Zawiść*

Gain +1 [Ładowanie] Count at Attack End  
A random ally gains +1 [Ładowanie] Count at Attack End

#### Pasywka wsparcia: Krótkofalówka

*od ulepszenia 3; posiadane 3× Zawiść*

1 Sojusznik z najniższym Maks. HP: wartość zyskiwanych Liczników Ładowania +1

#### Kwestie

- **Identity Acquisition:** Your problems… will be dealt with posthaste.
- **Morning Greeting:** Faust doesn’t particularly enjoy locomotive travel. On a trip, it doesn’t always have to be the body that moves from one place to another.
- **Afternoon Greeting:** It’s important to see through to the essence of things. For instance, your clock isn’t really a clock, and WARP trains don’t exactly warp.
- **Evening Greeting:** Don’t let rumors slip under your notice, Dante. Every canard starts from a crumb of truth.
- **Chatter #1:** To tell you the truth, Faust did not enjoy cleaning. It was the opposite, rather.
- **Chatter #2:** Do the ends really justify the means? Is the excruciating pain you bear really worth bringing them back?
- **Chatter #3:** You don’t seem to be as inquisitive of your situation as I am. Rather, have you decided to accept it, perhaps?
- **Post-Uptie Chat 1:** One day, I plan to collect every secret of the City and paint them all on a canvas. It’ll be something to appreciate.
- **Post-Uptie Chat 2:** Faust likes to travel from place to place. There is no better occupation than this in that regard.
- **Idle:** …They apparently disappear without notice on occasion. End of log.
- **Uptying:** I’m starting to get a good grasp of this place.
- **Deployment:** Got it, let’s move.
- **Stage Entry:** Faust, commencing battle.
- **Viewed in Battle:** Things are rather busying at the moment.
- **Commencing Attack:** It will be quick work.
- **Enemy Stagger:** Weakness noted.
- **Staggered:** Tch!
- **Enemy Killed:** The job is done.
- **Ally Death:** This is why I dislike trains.
- **Check Passed:** Faust, mission accomplished.
- **Check Failed:** Perhaps we were too hasty?
- **Victory Cry:** Let’s try and make it quicker next time.
- **Extra Conditions Fulfilled:** Faust, reporting in with another flawless success.
- **Defeat Wail:** Some personnel made rather unnecessary movements.

### 00 Ocalała pracownica Lobotomy Corporation — Faust

> Trzecia Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 1                                                           |
| HP                        | 69 (+2,39 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 2–5 / 2–6 / 3–6 / 3–6                                       |
| Poziom obrony             | poziom −4                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Żądza                                                       |
| Przynależność             | L_Corp                                                      |
| Słowa kluczowe            | Rozdarcie, Oddech                                           |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Samotne Uderzenie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Cięcie |          2 |         +6 |      1 |           +3 |    1 |
|          3 | Żądza  | Cięcie |          3 |         +6 |      1 |           +3 |    1 |
|          4 | Żądza  | Cięcie |          3 |         +8 |      1 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Nakłada 1 Rozdarcia

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Nakłada 2 Rozdarcia

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa Licznik Oddechu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 2 Rozdarcia

#### Umiejętność 2 (×2): Głębokie Cięcia

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Kłucie |          3 |         +3 |      3 |           +3 |    1 |
|          3 | Posępność | Kłucie |          4 |         +3 |      3 |           +3 |    1 |
|          4 | Posępność | Kłucie |          5 |         +3 |      3 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Zyskuje w następnej turze 1 Oddechu  
Moneta 2: [Trafienie Awersem] Zyskuje w następnej turze 1 Oddechu  
Moneta 3: [Trafienie Awersem] Zyskuje 2 Pośpiechu w następnej turze

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Zyskuje 1 Oddech w następnej turze  
Moneta 2: [Przy Trafieniu] Zyskuje 1 Oddech w następnej turze  
Moneta 3: [Przy Trafieniu] Zyskuje 4 Pośpiechu w następnej turze

*Od ulepszenia 4:* Moneta 1: [Przy Trafieniu] Zyskuje 1 Oddech w następnej turze  
Moneta 2: [Przy Trafieniu] Zyskuje 1 Oddech w następnej turze  
Moneta 3: [Przy Trafieniu] Zyskuje 4 Pośpiechu w następnej turze  
Moneta 3: [Przy Trafieniu] Zyskuje 1 Oddech w następnej turze

#### Umiejętność 3 (×1): Celowanie w Okazję

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Zawiść | Cięcie |          4 |         +8 |      2 |           +3 |    1 |

Gdy ta jednostka nie otrzymała obrażeń w poprzedniej turze, Moc Monet +3  
Moneta 2: [Trafienie Awersem] Nakłada 5 Rozdarcia

#### Obrona: Unik

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           +0 |    1 |
|          4 | Zawiść  | obrona: unik |          3 |        +10 |      1 |           +0 |    1 |

#### Pasywka bojowa: Postanowienie

*od ulepszenia 2; rezonans 2× Żądza*

Na początku następnej tury przy 4+ Liczniku Oddechu zyskuje 2 Pośpiechu

#### Pasywka wsparcia: Poparcie

*od ulepszenia 3; rezonans 2× Żądza*

1 Sojusznik z najniższym Maks. HP: Moc Końcowa Umiejętności obrony +2

#### Kwestie

- **Identity Acquisition:** This is Faust, a pleasure to meet you.
- **Morning Greeting:** I’d gained a habit of carefully observing my surroundings. I’ve got your current destination down, too.
- **Afternoon Greeting:** It’s beneficial to allocate a time of the day when all of us can relax. Mental health management can be surprisingly difficult.
- **Evening Greeting:** I’m used to darkness. One time, I stayed alone in a cramped room with no power for 59 days.
- **Chatter #1:** My old workplace was underground. A cold artificial light was all we had.
- **Chatter #2:** While I strive to comprehend most laws and denizens of the world… Some things are simply not meant to be understood.
- **Chatter #3:** …My old job had a manager, too. Though I never had a chance to talk with them directly like I do now. This is new to me… but it isn’t bad.
- **Post-Uptie Chat 1:** I often had to clean up the bodies of coworkers with whom I had dined the day before. Here… I don’t experience such things, at least. Yes, I’d say it’s not too bad here.
- **Post-Uptie Chat 2:** Intolerable pain, unknowable monsters, dying colleagues… Those aren’t what I fear. Rather, it’s…
- **Idle:** A sudden disappearance, often seen.
- **Uptying:** I suppose I’ll put forth some effort one more time.
- **Deployment:** I’m ready.
- **Stage Entry:** Hopefully this goes well.
- **Viewed in Battle:** What was done wrong?
- **Commencing Attack:** There’s no fear right now.
- **Enemy Stagger:** You’re up next.
- **Staggered:** Ah!
- **Enemy Killed:** That wasn’t scary.
- **Ally Death:** It’s good to have had you, at least.
- **Check Passed:** Preparation makes things easy.
- **Check Failed:** I’m all too used to this.
- **Victory Cry:** This is far from the hardest battle I’ve fought.
- **Extra Conditions Fulfilled:** Faust has always been competent.
- **Defeat Wail:** It’s fortunate that we have another chance.

### 000 Ta, Która Ściska — Faust

> Czwarta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 1                                                           |
| HP                        | 66 (+2,28 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 4–5 / 4–6 / 4–7 / 4–7                                       |
| Poziom obrony             | poziom −1                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×1 (Normal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Żądza                                                       |
| Przynależność             | N_Corp, N_Corp_Fnatic                                       |
| Słowa kluczowe            | Krwawienie                                                  |
| Data aktualizacji         | 20230323                                                    |

#### Umiejętność 1 (×3): Chichot

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Kłucie |          3 |         +3 |      2 |           +4 |    1 |
|          3 | Zawiść | Kłucie |          4 |         +3 |      2 |           +4 |    1 |

*Od ulepszenia 1:* [Wygrane Starcie] Cel traci 3 Poczytalności  
Moneta 1: [Trafienie Awersem] Nakłada 1 Gwoździa  
Moneta 2: [Przy Trafieniu] Nakłada 1 Krwawienia

*Od ulepszenia 2:* [Wygrane Starcie] Cel traci 3 Poczytalności  
Moneta 1: [Przy Trafieniu] Nakłada 1 Gwoździa  
Moneta 2: [Przy Trafieniu] Nakłada 2 Krwawienia

#### Umiejętność 2 (×2): Ściskanie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Kłucie |          4 |         +2 |      3 |           +4 |    1 |
|          3 | Żądza  | Kłucie |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 1:* Moneta 2: [Przy Trafieniu] Nakłada 3 Gwoździ  
Moneta 3: [Trafienie Awersem] Nakłada w następnej turze Spojrzenie

*Od ulepszenia 2:* Moneta 2: [Przy Trafieniu] Nakłada 3 Gwoździ  
Moneta 3: [Trafienie Awersem] Nakłada w następnej turze 1 Paraliżu  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze Spojrzenie

*Od ulepszenia 4:* Moneta 1: [Przy Trafieniu] Nakłada 2 Gwoździ  
Moneta 2: [Przy Trafieniu] Nakłada 3 Gwoździ  
Moneta 3: [Trafienie Awersem] Nakłada w następnej turze 1 Paraliżu  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze Spojrzenie

#### Umiejętność 3 (×1): Egzekucja

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Pycha  | Obuch |          6 |         +2 |      3 |           +4 |    1 |

*Od ulepszenia 3:* Po zabiciu wroga tą Umiejętnością sojusznicy odzyskują 10 Poczytalności i zyskują 1 Wzrost Obrażeń Kłucia i Uderzenia  
Moneta 1: [Przy Trafieniu] Nakłada 2 Gwoździ  
Moneta 2: [Trafienie Awersem] Nakłada 2 Gwoździ  
Moneta 3: Jeżeli cel posiada 5+ Gwoździ, Zadaje +50% obrażeń

*Od ulepszenia 4:* Po zabiciu wroga tą Umiejętnością sojusznicy odzyskują 10 Poczytalności i zyskują 1 Wzrost Obrażeń Kłucia i Uderzenia  
Moneta 1: [Przy Trafieniu] Nakłada 2 Gwoździ  
Moneta 2: [Trafienie Awersem] Nakłada 2 Gwoździ  
Moneta 3: Jeżeli cel posiada 5+ Gwoździ, Zadaje +70% obrażeń

#### Obrona: Nieczystość

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          4 |        +10 |      1 |           +0 |    1 |
|          4 | Żądza   | obrona: unik |          4 |        +10 |      1 |           +0 |    1 |

[Udany Unik] Cel traci 3 Poczytalności

#### Pasywka bojowa: Gwizd

*od ulepszenia 2; rezonans 4× Żądza*

Na początku walki odzyskuje 15 Poczytalności dla 2 sojuszników z najniższą Poczytalnością.  
Jeżeli celem jest Fanatyk Korporacji N, nakłada 1 Fanatyzmu

#### Pasywka bojowa: Whistles

*od ulepszenia 4; rezonans 4× Żądza*

Combat Start: Heal 15 SP for 2 allies that have the lowest SP  
If the ally is an "N Corp. Fanatic", also apply 2 [Fanatyzm]

#### Pasywka wsparcia: Szepty

*od ulepszenia 3; rezonans 3× Żądza*

Na początku walki odzyskuje 15 Poczytalności dla 1 sojusznika z najniższą Poczytalnością.  
Jeżeli celem jest Fanatyk Korporacji N, nakłada 1 Fanatyzmu

#### Pasywka wsparcia: Whispers

*od ulepszenia 4; rezonans 3× Żądza*

Combat Start: Heal 15 SP for 1 ally that has the lowest SP  
If the ally is an "N Corp. Fanatic", also apply 2 [Fanatyzm]

#### Kwestie

- **Identity Acquisition:** Will you join me… in the great task to purify the abominable filth?
- **Morning Greeting:** You came just in time for the sermons! Huhu, you deserve some praise.
- **Afternoon Greeting:** Oh… Is it lunchtime outside? Keehee… Pardon, I couldn’t care less about such things.
- **Evening Greeting:** It is the time of purification… the hour for us to remove filth from the soil of purity.
- **Chatter #1:** You must accept the pain! You have to transcend it… Only then may you be reborn.
- **Chatter #2:** Come, follow Faust… You will be gripped by my hands… Keehee.
- **Chatter #3:** What constitutes a human is flesh, blood… and bone. All else is filth. …I can give that mask of yours a pass. It’s essentially a piece of clothing.
- **Post-Uptie Chat 1:** Do you… not wash your hands when they are begrimed? Keekee… See now, to cleanse filth is a natural thing to do.
- **Post-Uptie Chat 2:** The company… doesn’t always have the right answer. At times… you need to forge your own path, you know?
- **Idle:** You’ve been keeping Faust here with nothing to say…? Hah, forgiveness comes to you just this once.
- **Uptying:** Higher… Still higher! Let me advance… toward a purer body… Huhu!
- **Deployment:** With hammer in hand.
- **Stage Entry:** This had better be worthy of Faust’s participation.
- **Viewed in Battle:** Save your confession for later.
- **Commencing Attack:** Purge!
- **Enemy Stagger:** From dirt…
- **Staggered:** …Goodness.
- **Enemy Killed:** …to dirt!
- **Death:** I’ve… yet to be whole…
- **Check Passed:** Naturally!
- **Check Failed:** How could…?
- **Victory Cry:** Is the purification over…? Heeheh.
- **Extra Conditions Fulfilled:** Toward the purest world!
- **Defeat Wail:** Defeat…? This is unbelievable. Where are my hammers?

### 00 Południowe Stowarzyszenie Zwei Sekcja 4 — Faust

> Piąta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 0                                                           |
| HP                        | 82 (+2,82 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 4–5 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom +2                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×1 (Normal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 55% / 20%                                                   |
| Grzech wyróżniony         | Zawiść                                                      |
| Przynależność             | Zwei                                                        |
| Słowa kluczowe            | —                                                           |
| Data aktualizacji         | 20230810                                                    |

#### Umiejętność 1 (×3): Patrol

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Kłucie |          2 |         +4 |      2 |           −1 |    1 |
|          3 | Zawiść | Kłucie |          3 |         +4 |      2 |           −1 |    1 |

*Od ulepszenia 1:* [Przegrane Starcie] Zyskuje 2 Wzrosty Poziomu Obrony  
Moneta 2: [Trafienie Awersem] Zyskuje w następnej turze 2 Wzrosty Poziomu Obrony

*Od ulepszenia 2:* [Przegrane Starcie] Zyskuje 3 Wzrosty Poziomu Obrony  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 Wzrosty Poziomu Obrony

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa w następnej turze Prowokację slotu tej Umiejętności o 2  
[Przegrane Starcie] Zyskuje 3 Wzrosty Poziomu Obrony  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 Wzrosty Poziomu Obrony

#### Umiejętność 2 (×2): Ochrona Klienta

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Cięcie |          3 |         +2 |      3 |           −1 |    1 |
|          3 | Posępność | Cięcie |          3 |         +3 |      3 |           −1 |    1 |
|          4 | Posępność | Cięcie |          4 |         +3 |      3 |           −1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Nakłada 2 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP (maks. 3 razy na turę)  
Moneta 1: [Trafienie Awersem] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony  
Moneta 2: [Trafienie Awersem] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony  
Moneta 3: [Trafienie Awersem] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony

*Od ulepszenia 2:* [Przy Użyciu] Nakłada 3 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP (maks. 3 razy na turę)  
Przy 5+ Wzrostach Poziomu Obrony Moc Starcia +1  
Moneta 1: [Przy Trafieniu] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony  
Moneta 3: [Przy Trafieniu] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony

*Od ulepszenia 4:* [Przy Użyciu] Nakłada 4 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP (maks. 3 razy na turę)  
Przy 5+ Wzrostach Poziomu Obrony Moc Starcia +2  
Moneta 1: [Przy Trafieniu] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony  
Moneta 3: [Przy Trafieniu] Zyskuje w następnej turze 1 Wzrost Poziomu Obrony

#### Umiejętność 3 (×1): Porządek Publiczny

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Cięcie |          5 |         +5 |      2 |           −1 |    1 |
|          4 | Żądza  | Cięcie |          6 |         +5 |      2 |           −1 |    1 |

*Od ulepszenia 3:* Przy 5+ Wzrostach Poziomu Obrony Moc Monet +1  
[Wygrane Starcie] Odzyskuje 2 HP  
Moneta 2: Nakłada w następnej turze 1 Pośpiechu i 2 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP

*Od ulepszenia 4:* Przy 5+ Wzrostach Poziomu Obrony Moc Monet +1  
[Wygrane Starcie] Odzyskuje 4 HP  
Moneta 2: Nakłada w następnej turze 1 Pośpiechu i 2 Wzrosty Poziomu Obrony na sojusznika z najniższym procentem aktualnego HP  
Moneta 2: Jeżeli celem jest Fikser Stowarzyszenia Zwei, nakłada dodatkowo 1 Pośpiechu i 1 Wzrost Poziomu Obrony

#### Obrona: Garda

| Ulepszenie | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral   | obrona: blok |         10 |         +6 |      1 |           +2 |    1 |
|          4 | Posępność | obrona: blok |         12 |         +6 |      1 |           +2 |    1 |

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa w następnej turze Prowokację slotu tej Umiejętności o 3

#### Pasywka bojowa: Ochrona Obszaru

*od ulepszenia 2; posiadane 4× Posępność*

Na początku walki nakłada 2 Wzrosty Poziomu Obrony na sojuszników po obu stronach w Panelu Sterowania

#### Pasywka bojowa: Ochrona Obszaru

*od ulepszenia 4; posiadane 4× Posępność*

Na początku walki nakłada 2 Wzrosty Poziomu Obrony na sojuszników po obu stronach w Panelu Sterowania.  
Jeżeli ich HP jest poniżej 50%, nakłada dodatkowo 2 Wzrosty Poziomu Obrony

#### Pasywka wsparcia: Otrzymano Wezwanie do Ochrony

*od ulepszenia 3; rezonans 2× Posępność*

Na początku walki nakłada 2 Wzrosty Poziomu Obrony na 1 sojusznika z najniższym procentem HP.  
Jeżeli jego HP jest poniżej 50%, nakłada dodatkowo 2 Wzrosty Poziomu Obrony

#### Kwestie

- **Identity Acquisition:** Request received. This is Faust. Advancing to protection target location.
- **Morning Greeting:** A safe morning. As always, we are committed to ensuring the security of the local premises. Have a nice day.
- **Afternoon Greeting:** Reporting in to inform you that no issues were detected during the noon patrol. Ah... There is no need to be worried about whether we've had our meal. While Faust dines, her partner handles the patrolling. Oh, there is no need to be worried about said partner, either; Faust works with an exceptional individual from Section 4. Faust is still superior, however.
- **Evening Greeting:** During nighttime... Please remain in close proximity to Faust. The narrowed field of vision may delay the protective maneuvers.
- **Chatter #1:** Territory protection requires significant manpower as well as individual capability, as personnel must be deployed over the entire contract area. While the service is costly... the added safety is well worth the price.
- **Chatter #2:** We try to dress ourselves in civilian clothes for territory protection contracts. It is better to hide in plain sight to recognize those that seek to harm our clients.
- **Chatter #3:** Not all Zwei agents accept territory protection contracts. Of course, territory protection contracts aren't the sole dedication of Section 4, either.
- **Post-Uptie Chat 1:** Normally, these contracts are signed when the client requests several protection targets.  Therefore... we often end up defending our clients against multiple threats. And so does Faust.
- **Post-Uptie Chat 2:** Is my work strenuous, you ask? Such details are not a part of my consideration. Faust considers only the safety of her protection targets.
- **Idle:** If there is nothing else, I would like to leave for my next scheduled patrol.
- **Uptying:** Yes, indeed. It is only natural that greater responsibilities are assigned to finer agents. I look forward to working with you.
- **Deployment:** On standby.
- **Stage Entry:** Protection request received.
- **Viewed in Battle:** Do other territories require my attention?
- **Commencing Attack:** Moving to protect.
- **Enemy Stagger:** You've been immobilized.
- **Staggered:** Ngh...
- **Enemy Killed:** Hostiles eliminated.
- **Death:** Worry... not. My colleagues will... protect...
- **Check Passed:** An elementary problem.
- **Check Failed:** This did not align with Faust's strengths.
- **Victory Cry:** Protection request fulfilled. Returning to patrol.
- **Extra Conditions Fulfilled:** We have taken care of all potential troubles in this territory. Let us end our patrol for the day here.
- **Defeat Wail:** It's... okay. There are other shields at Zwei. Please reconsider your decision to terminate our contract...

### 000 Południowe Stowarzyszenie Seven Sekcja 4 — Faust

> Szósta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 0                                                           |
| HP                        | 76 (+2,4 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–7 / 4–7 / 4–7                                       |
| Poziom obrony             | poziom −2                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×0,5 (Endured), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Seven                                                       |
| Słowa kluczowe            | Rozdarcie                                                   |
| Data aktualizacji         | 20230907                                                    |

#### Umiejętność 1 (×3): Analiza Predykcyjna

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Cięcie |          3 |         +3 |      2 |           +3 |    1 |
|          3 | Zawiść | Cięcie |          4 |         +3 |      2 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 2: [Przy Trafieniu] Nakłada 3 Rozdarcia

*Od ulepszenia 2:* Jeżeli cel ma 3+ Rozdarcia, Moc Monet +1  
Moneta 2: [Przy Trafieniu] Nakłada 3 Rozdarcia

*Od ulepszenia 4:* Moc Monet +1 za każde 3 Rozdarcia na celu (maks. 2)  
Moneta 2: [Przy Trafieniu] Nakłada 3 Rozdarcia

#### Umiejętność 2 (×2): Rozbieranie Celu

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Cięcie |          3 |         +4 |      3 |           +3 |    1 |
|          3 | Posępność | Cięcie |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Nakłada 3 Rozdarcia  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 6+ Rozdarcia, nakłada w następnej turze Analizę Słabości

*Od ulepszenia 2:* Jeżeli cel ma 6+ Rozdarcia, Moc Monet +1  
[Wygrane Starcie] Zwiększa Licznik Rozdarcia celu o 3  
Moneta 1: [Przy Trafieniu] Nakłada 3 Rozdarcia  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 6+ Rozdarcia, nakłada w następnej turze Analizę Słabości

*Od ulepszenia 4:* Moc Monet +1 za każde 6 Rozdarcia na celu (maks. 2)  
[Wygrane Starcie] Zwiększa Licznik Rozdarcia celu o 3  
Moneta 1: [Przy Trafieniu] Nakłada 3 Rozdarcia  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 6+ Rozdarcia, nakłada w następnej turze Analizę Słabości

#### Umiejętność 3 (×1): Profilowanie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Cięcie |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* Zadaje +10% obrażeń za każde 3 Rozdarcia na celu (maks. 20%)  
Moneta 2: [Przy Trafieniu] Nakłada 3 Rozdarcia  
Moneta 3: [Koniec Ataku] Jeżeli cel zostanie Ogłuszony lub zginie, zyskuje w następnej turze 1 Pośpiechu i 1 Wzrost Mocy Cięcia

*Od ulepszenia 4:* Zadaje +10% obrażeń za każde 3 Rozdarcia na celu (maks. 50%)  
[Wygrane Starcie] Zwiększa Licznik Rozdarcia celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada 3 Rozdarcia  
Moneta 3: [Koniec Ataku] Jeżeli cel zostanie Ogłuszony lub zginie, zyskuje w następnej turze 1 Pośpiechu i 1 Wzrost Mocy Cięcia

#### Obrona: Załatwmy to szybko

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +4 |      1 |           −2 |    1 |
|          4 | Żądza   | obrona: blok |         10 |         +4 |      1 |           −2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zyskuje w następnej turze 1 Pośpiechu (maks. 3 razy na turę)

*Od ulepszenia 4:* [Przy Użyciu] Zyskuje w następnej turze 1 Pośpiechu (maks. 3 razy na turę)

#### Pasywka bojowa: Zanim Herbata Ostygnie...

*od ulepszenia 2; posiadane 3× Obżar.*

Gdy atakuje atrybutem Słabości lub Wrażliwości (przy odporności powyżej 1), zyskuje przed atakiem Oddech w liczbie Rozdarcia celu (maks. 20 na turę)

#### Pasywka wsparcia: Herbatka Stowarzyszenia Seven

*od ulepszenia 3; posiadane 4× Obżar.*

1 Sojusznik z najwyższą Szybkością: gdy atakuje atrybutem Wrażliwości (przy odporności powyżej 1.5), zadaje obrażenia proporcjonalnie do Rozdarcia celu  
(Za każde 1 Rozdarcie 1.5%. Maks. 15%)

#### Pasywka wsparcia: Herbatka Stowarzyszenia Seven

*od ulepszenia 4; posiadane 4× Obżar.*

1 Sojusznik z najwyższą Szybkością: gdy atakuje atrybutem Słabości lub Wrażliwości (przy odporności powyżej 1), zadaje obrażenia proporcjonalnie do Rozdarcia celu  
(Za każde 1 Rozdarcie 1.5%. Maks. 15%)  
Jeżeli sojusznik, który otrzymał ten efekt, jest Fikserem Stowarzyszenia Seven, zadaje dodatkowe obrażenia  
(Za każde 1 Rozdarcie 0.5%. Maks. 5%)

#### Kwestie

- **Identity Acquisition:** Welcome. I will take your orders here.
- **Morning Greeting:** This cafeteria is consistently bustling, but now is its busiest hour. Quite understandable, as to go through a day without a cup of tea would be to stumble through it with a mind that is only half awake.
- **Afternoon Greeting:** Designating time for quick elevenses or an afternoon tea is a wise managerial choice, considering they are known to improve work efficiency. I will take your orders here.
- **Evening Greeting:** We take orders into the late hours for our colleagues working night shifts or overtime. If you are off duty tonight, may I brew you some nice tea with a dash of Sherry or Brandy?
- **Chatter #1:** This cafeteria is an employee—run establishment by members of the Seven Association who love tea more than anything else in the world. Shifts are all voluntary, and we return to our usual duties on our off hours. Ah, and it goes without saying that all profits go to purchasing higher—quality tea leaves and teapots.
- **Chatter #2:** THE MILK!...should already be in the cup before the tea is poured. That is our...recommended way.
- **Chatter #3:** You'd like some... ice? Apologies, but this establishment does not serve iced 'tea'. If it is of no trouble to you, may I take a moment of your time to explicate why black tea must be enjoyed at higher temperatures?
- **Post-Uptie Chat 1:** Ah, I am occupied at the present moment. While I always enjoy our tea discussions, it must wait for now.
- **Post-Uptie Chat 2:** Precise work ethic and talent for brewing tea of exact, pure flavor. Faust considers these as her two primary objectives.
- **Idle:** To over—infuse your tea is to allow impure flavors to surface. Please refrain from doing so.
- **Uptying:** Yes, of course. You may call upon me at any time should the need arise. Unless it's tea time, that is.
- **Deployment:** An urgent order, yes?
- **Stage Entry:** I will rendezvous with you out in the field.
- **Viewed in Battle:** Before the tea cools.
- **Commencing Attack:** Flawless.
- **Enemy Stagger:** Like shattered tea leaves.
- **Staggered:** Ah…
- **Enemy Killed:** There is no more information to be gained.
- **Death:** Haah... But... I don't have anyone... to cover my next shift...
- **Check Passed:** A result of meticulous observation.
- **Check Failed:** ... I should have observed more carefully.
- **Victory Cry:** This mission was a success. Ah, now I must leave for my shift at the cafeteria. So, if you will excuse me...
- **Extra Conditions Fulfilled:** Milk tea, please. Poured, not stirred. Indeed, tea tastes better when it is served to you rather than when you serve it yourself.
- **Defeat Wail:** That was... unexpected. We must not have ingested enough tea. Let us take some time off for tea before our next attempt.

### 000 Lobotomy E.G.O:: Skrucha — Faust

> Siódma Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | wydarzenie 9101                                             |
| HP                        | 82 (+2,82 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 2–5 / 2–5 / 3–6 / 3–6                                       |
| Poziom obrony             | poziom +1                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×2 (Fatal), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 65% / 35%                                                   |
| Grzech wyróżniony         | Gniew                                                       |
| Przynależność             | L_Corp                                                      |
| Słowa kluczowe            | Wstrząs                                                     |
| Data aktualizacji         | 20231026                                                    |

#### Umiejętność 1 (×3): Ściskające Kajdany

| Ulepszenie | Grzech   | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Obuch |          4 |         +6 |      1 |           +3 |    1 |
|          3 | Lenistwo | Obuch |          4 |         +7 |      1 |           +3 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 3  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 3  
Moneta 1: [Przy Trafieniu] Nakłada +2 Licznika Wstrząsu

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 3  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 3  
Moneta 1: [Przy Trafieniu] Nakłada +3 Licznika Wstrząsu

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 3  
[Przegrane Starcie] Zwiększa własny Licznik Wstrząsu o 3  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 3  
Moneta 1: [Przy Trafieniu] Nakłada +3 Licznika Wstrząsu

#### Umiejętność 2 (×2): Metaliczna Dźwięczność

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Obuch |          3 |         +4 |      3 |           +3 |    1 |
|          3 | Pycha  | Obuch |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 4  
Moneta 1: [Trafienie Awersem] Nakłada w następnej turze 1 Spadku Poziomu Ataku  
Moneta 3: [Przy Trafieniu] Nakłada 4 Wstrząsu

*Od ulepszenia 2:* [Początek Walki] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1  
[Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 4  
Moneta 1: [Trafienie Awersem] Zwiększa własny Licznik Wstrząsu o 1  
Moneta 1: [Trafienie Awersem] Nakłada w następnej turze 1 Spadku Poziomu Ataku  
Moneta 3: [Przy Trafieniu] Nakłada 5 Wstrząsu  
Moneta 3: [Trafienie Awersem] Nakłada w następnej turze 1 Osłabienie Monet Plus

*Od ulepszenia 4:* [Początek Walki] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1  
[Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 4  
Moneta 1: [Trafienie Awersem] Zwiększa własny Licznik Wstrząsu o 1  
Moneta 1: [Przy Trafieniu] Nakłada w następnej turze 1 Spadku Poziomu Ataku  
Moneta 3: [Przy Trafieniu] Nakłada 5 Wstrząsu  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze 1 Osłabienie Monet Plus

#### Umiejętność 3 (×1): Uwolniona Brutalność

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Obuch |          3 |         +5 |      3 |           +3 |    1 |

*Od ulepszenia 3:* [Początek Walki] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1 (maks. +2)  
[Przegrane Starcie] Traci 20 Poczytalności  
Zadaje +3% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 15%)  
[Przy Zabiciu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 1: [Przy Trafieniu] Wybuch Wstrząsu  
Przy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 20% końcowego podniesienia Progu Oszołomienia (maks. 13)  
Moneta 2: [Przy Trafieniu] Wybuch Wstrząsu  
Przy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 20% końcowego podniesienia Progu Oszołomienia (maks. 13)  
Moneta 3: [Przy Trafieniu] Wybuch Wstrząsu  
Przy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 20% końcowego podniesienia Progu Oszołomienia (maks. 13)  
Zmniejsza Licznik Wstrząsu o 3

*Od ulepszenia 4:* [Początek Walki] Zużywa 5 własnego Licznika Wstrząsu, aby zwiększyć wagę ataku tej Umiejętności o 1 (maks. +2)  
[Przegrane Starcie] Traci 20 Poczytalności  
Zadaje +6% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
[Przy Zabiciu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 1: [Przy Trafieniu] Wybuch Wstrząsu  
Przy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 30% końcowego podniesienia Progu Oszołomienia (maks. 20)  
Moneta 2: [Przy Trafieniu] Wybuch Wstrząsu  
Przy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 30% końcowego podniesienia Progu Oszołomienia (maks. 20)  
Moneta 3: [Przy Trafieniu] Wybuch Wstrząsu  
Przy Wybuchu Wstrząsu zadaje obrażenia Gniewu równe 30% końcowego podniesienia Progu Oszołomienia (maks. 20)  
Zmniejsza Licznik Wstrząsu o 3

#### Obrona: Narastająca Uraza

| Ulepszenie | Grzech    | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | obrona: kontra |          9 |         +6 |      1 |           +5 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 3

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 6

#### Pasywka bojowa: Wymuszona Skrucha

*od ulepszenia 2; posiadane 6× Gniew*

- Podczas Starcia: jeżeli cel ma 3+ rodzajów negatywnych efektów, Moc Starcia celu -1  
- Dopóki ta jednostka żyje, wróg dotknięty [Wybuch Wstrząsu] zyskuje 2 Spadki Poziomu Obrony (maks. 1 raz na turę na wroga)  
- Skażenie Umysłu: jeżeli na koniec tury Poczytalność jest poniżej -25, zyskuje w następnej turze 2 Spętania i 1 Wzrost Mocy Uderzenia

#### Pasywka bojowa: Wymuszona Skrucha

*od ulepszenia 4; posiadane 6× Gniew*

- Podczas Starcia: Moc Starcia celu -1 za każde 3 rodzaje negatywnych efektów (maks. -2 Moc Starcia)  
- Dopóki ta jednostka żyje, wróg dotknięty [Wybuch Wstrząsu] zyskuje 2 Spadki Poziomu Obrony (maks. 3 razy na turę na wroga)  
- Skażenie Umysłu: jeżeli na koniec tury Poczytalność jest poniżej -25, zyskuje w następnej turze 2 Spętania i 1 Wzrost Mocy Uderzenia

#### Pasywka wsparcia: Praca Tłumiąca

*od ulepszenia 3; posiadane 5× Gniew*

Gdy 1 Sojusznik z najniższą Szybkością prowadzi Starcie, jeżeli jego cel ma 3+ rodzajów negatywnych efektów, Moc Starcia celu -1

#### Kwestie

- **Identity Acquisition:** Starting work on Contained Abnormality T-01-54.
- **Morning Greeting:** Good morning, Manager. Please share with me today's descending list of Work for the Abnormalities, and I will relay it to the team.
- **Afternoon Greeting:** It seems to me that the Clerks are having a nice lunch together. Us Control Team Agents don't particularly prefer to dine in groups... But I must wonder if that is what Ms. Malkuth would want us to do.
- **Evening Greeting:** Work progress at 95%. We should have no trouble reaching our target PE-Box goal today. Good work.
- **Chatter #1:** The 'Forsaken Murderer'? Hm. I suppose it stands out in that it does not have a particular preference for any kind of Work. It seemed that avoiding Repression Work is advisable, however.
- **Chatter #2:** I foresee little trouble ahead, as long as the assigned employee has a decent understanding of this Work. A bad result, however, may lead to Abnormalities breaching containment.
- **Chatter #3:** The E.G.O suits assigned to us seem adequate. However, I have been hearing reports from employees with weaker mental fortitude that it feels as though the straight-jacket is contracting around them. These suits are weak to WHITE damage, after all...
- **Post-Uptie Chat 1:** This E.G.O gift isn't as uncomfortable as I expected. Though it was equipped without my knowledge.
- **Post-Uptie Chat 2:** I am curious: how does it feel when its head slowly turns into metal? Can it feel that? Does its head ring when this hammer crushes our enemies?
- **Idle:** ... More banging noises, again...
- **Uptying:** Control Team Captain, Agent Faust. Commencing suppression of the Green Dawn Ordeal as per the Manager's orders.
- **Deployment:** I am ready.
- **Stage Entry:** Preparing to suppress.
- **Viewed in Battle:** Do you require more Work to be done?
- **Commencing Attack:** Containment Breach confirmed.
- **Enemy Stagger:** The entity is weakening.
- **Staggered:** Uh...
- **Enemy Killed:** Escaped entity neutralized.
- **Death:** Suppression Work failed...
- **Check Passed:** That was an adequate side work.
- **Check Failed:** This Work does not align with my strengths... I will make a note of it in the logs.
- **Victory Cry:** We can end the Suppression Work here. Returning to management.
- **Extra Conditions Fulfilled:** Threat Suppressed. I recommend that you familiarize yourself with these alarms. Faust knows that we have many days to go before the 50th day.
- **Defeat Wail:** Control Team's Suppression Work failed. Requesting assistance from the other departments...

### 000 Ród Ostrza Salsu — Faust

> Ósma Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 3                                                           |
| HP                        | 76 (+2,5 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–7 / 3–8 / 3–8                                       |
| Poziom obrony             | poziom −2                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 65% / 35% / 15%                                             |
| Grzech wyróżniony         | Pycha                                                       |
| Przynależność             | Blade_Lineage                                               |
| Słowa kluczowe            | Oddech, Krwawienie                                          |
| Data aktualizacji         | 20240222                                                    |

#### Umiejętność 1 (×3): Taniec Ostrza przy Księżycu

| Ulepszenie | Grzech   | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Cięcie |          3 |         +1 |      3 |           +2 |    1 |
|          3 | Lenistwo | Cięcie |          3 |         +2 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 3: [Trafienie Krytyczne] Nakłada 1 [Czerwony Kwiat Śliwy]

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 2: [Trafienie Awersem] Zyskuje 1 [Oddech]  
Moneta 3: [Trafienie Krytyczne] Nakłada 1 [Czerwony Kwiat Śliwy]

*Od ulepszenia 4:* Przy 5+ [Oddech] Moc Monet +1  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 2: [Trafienie Awersem] Zyskuje 1 [Oddech]  
Moneta 3: [Trafienie Krytyczne] Nakłada 1 [Czerwony Kwiat Śliwy]

#### Umiejętność 2 (×2): Akupunktura

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Kłucie |          4 |         +5 |      2 |           +2 |    1 |
|          3 | Pycha  | Kłucie |          4 |         +6 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]  
Moneta 2: [Trafienie Krytyczne] Nakłada 2 [Czerwony Kwiat Śliwy]

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje +2 Licznika [Oddech]  
Moneta 1: Zadaje +30% obrażeń przy trafieniu krytycznym  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 Spętania  
Moneta 2: [Trafienie Krytyczne] Nakłada 2 [Czerwony Kwiat Śliwy]

*Od ulepszenia 4:* Przy 7+ [Oddech] Moc Monet +1  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje +2 Licznika [Oddech]  
Moneta 1: Zadaje +30% obrażeń przy trafieniu krytycznym  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 Spętania  
Moneta 2: [Trafienie Krytyczne] Nakłada 2 [Czerwony Kwiat Śliwy]

#### Umiejętność 3 (×1): Rozsypane Kwiaty Śliwy

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Posępność | Cięcie |          5 |         +6 |      2 |           +2 |    1 |

*Od ulepszenia 3:* Zadaje +3% obrażeń za każdy 1 [Czerwony Kwiat Śliwy] na celu  
[Wygrane Starcie] Zużywa połowę własnego Licznika [Oddech], po czym zyskuje [Oddech] w liczbie zużytego Licznika (maks. 10)  
Moneta 1: [Trafienie Krytyczne] Nakłada 5 [Czerwony Kwiat Śliwy]  
Moneta 2: [Trafienie Krytyczne] Nakłada 5 [Czerwony Kwiat Śliwy]

*Od ulepszenia 4:* Zadaje +3% obrażeń za każdy 1 [Czerwony Kwiat Śliwy] na celu  
Moc Monet +1 za każde 7 [Oddech] (maks. 3)  
[Wygrane Starcie] Zużywa połowę własnego Licznika [Oddech], po czym zyskuje [Oddech] w liczbie zużytego Licznika (maks. 10)  
Trafienia krytyczne tą Umiejętnością nie zużywają [Czerwony Kwiat Śliwy]  
Moneta 1: [Trafienie Krytyczne] Nakłada 5 [Czerwony Kwiat Śliwy]  
Moneta 1: [Trafienie Krytyczne] Jeżeli cel ma 10 [Czerwony Kwiat Śliwy], nakłada 1 Wrażliwość na Cięcie  
Moneta 2: [Trafienie Krytyczne] Nakłada 5 [Czerwony Kwiat Śliwy]  
Moneta 2: [Trafienie Krytyczne] Jeżeli cel ma 10 [Czerwony Kwiat Śliwy], nakłada 1 Wrażliwość na Cięcie

#### Obrona: Przekierowanie

| Ulepszenie | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral   | obrona: blok |         10 |         +4 |      1 |           +0 |    1 |
|          4 | Posępność | obrona: blok |         10 |         +4 |      1 |           +0 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Moc Końcowa +1 za każde 4 [Oddech] (maks. 3)

*Od ulepszenia 4:* [Przy Użyciu] Moc Końcowa +1 za każde 4 [Oddech] (maks. 5)

#### Pasywka bojowa: Krwawe Kwiaty Śliwy

*od ulepszenia 2; posiadane 4× Pycha*

Przy trafieniu krytycznym nakłada 1 [Czerwony Kwiat Śliwy] (maks. 3 razy)

#### Pasywka bojowa: Krwawe Kwiaty Śliwy

*od ulepszenia 4; posiadane 4× Pycha*

Przy trafieniu krytycznym nakłada 1 [Czerwony Kwiat Śliwy]. Jeżeli cel ma 10 [Czerwony Kwiat Śliwy], nakłada zamiast tego 1 Spadek Poziomu Obrony (maks. 6 razy)

#### Pasywka wsparcia: Ostrze Karmione Żalem

*od ulepszenia 3; posiadane 4× Pycha*

Gdy sojusznik z pierwszą kolejnością przydziału trafi krytycznie Umiejętnością Cięcia, nakłada 1 Spadek Poziomu Obrony (maks. 3 razy na turę na wroga)

#### Kwestie

- **Identity Acquisition:** A night before a battle is always so silent. Ah, and the moon has waxed full tonight, too.
- **Morning Greeting:** Good morning. This is an opportune time for a modest meal and a warm cup of tea. There is no need for urgency.
- **Afternoon Greeting:** I plan to postpone my noon training until next time. I... believe that it is best that I review my book of techniques to ensure that I have not left anything behind.
- **Evening Greeting:** The pale moon glimmers white. With no trace of shadows, bright. Now is the time most apt.
- **Chatter #1:** I once trained my precision by casting the red plum petals under the starry sky... and rending them before they hit the floor. The sight of scattering red petals was... I daresay that it was quite beautiful. I witness that beauty still, from time to time. The only difference is that the petals are more liquid than solid.
- **Chatter #2:** Obsession with the blade is a shared passion among those who are a part of the Lineage. But I believe that I am past the stage of learning via muscle memory. Now, I train with my mind.
- **Chatter #3:** Witness the whirling arc of the blade. Does it not resemble art beyond the realms of martial techniques? Let the sky be the paper upon which my blade draws an arc that breaks not... Ah, I seem to have lost myself for a moment.
- **Post-Uptie Chat 1:** After going through so much trouble to advance before our gates under the cover of night... is this all you could muster, Kurokumo Clan? You scatter so helplessly.
- **Post-Uptie Chat 2:** They will not, to their last moments of consciousness, understand that they have become naught but red petals blowing in the wind. Though our tools are much alike, I remain a step above them still.
- **Idle:** You may remain still all day. I shall converse with the moon.
- **Uptying:** This is a good night to engage in a dance of blades. Particularly exquisite are the flowers blossoming from the tip of a moon-dipped blade. Why not go and appreciate the petals?
- **Deployment:** So we march.
- **Stage Entry:** Let the flowers bloom.
- **Viewed in Battle:** Are you enjoying yourself?
- **Commencing Attack:** Scoundrels.
- **Enemy Stagger:** Let it blossom.
- **Staggered:** Mmm.
- **Enemy Killed:** Like a bed of flowers.
- **Death:** So... the red plum blossom... blooms from me all the same...
- **Check Passed:** No cause for it to be amiss.
- **Check Failed:** It was fated to be amiss.
- **Victory Cry:** I have cast the unsightly flowers from here. Let us see where we will now reside.
- **Extra Conditions Fulfilled:** When the flowers wither, a new tree shall take root here. It will grow to be a pillar that will protect our home. I am certain of that.
- **Defeat Wail:** We are... wanderers without destinations. Seeds without soil to take root in... When will our home be found?

### 00 Wichrowe Wzgórza Kamerdyner — Faust

> Dziewiąta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 4                                                           |
| HP                        | 76 (+2,7 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 2–6 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom −1                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×2 (Fatal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 65% / 35% / 15%                                             |
| Grzech wyróżniony         | Pycha                                                       |
| Przynależność             | Wuthering_Heights                                           |
| Słowa kluczowe            | Zatonięcie                                                  |
| Data aktualizacji         | 20240404                                                    |

#### Umiejętność 1 (×3): Konfiskata

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Cięcie |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Posępność | Cięcie |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Trafienie Awersem] Nakłada 2 [Zatonięcie]

*Od ulepszenia 2:* Moneta 2: [Przy Trafieniu] Nakłada 2 [Zatonięcie]

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli cel ma 6+ [Zatonięcie], Moc Monet +1  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Zatonięcie]

#### Umiejętność 2 (×2): Powitanie Natręta

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Obuch |          3 |         +5 |      2 |           +2 |    1 |
|          3 | Żądza  | Obuch |          4 |         +5 |      2 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 2: [Trafienie Awersem] Zwiększa Licznik [Zatonięcie] o 2

*Od ulepszenia 2:* [Przy Użyciu] Jeżeli cel ma 5+ [Zatonięcie], Moc Starcia +1  
Moneta 2: [Przy Trafieniu] Nakłada +2 Licznika [Zatonięcie]

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli cel ma 5+ [Zatonięcie], Moc Starcia +1  
[Przy Użyciu] Jeżeli cel ma 3+ Licznik [Zatonięcie], Moc Monet +1  
Moneta 2: [Przy Trafieniu] Nakłada +3 Licznika [Zatonięcie]

#### Umiejętność 3 (×1): Sztuka Gościny 4: Pieczęć Serca

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |          4 |         +2 |      4 |           +4 |    1 |

*Od ulepszenia 3:* Moneta 1: [Przy Trafieniu] Nakłada +3 Licznika [Zatonięcie]  
Moneta 4: [Przy Trafieniu] Nakłada w następnej turze 2 [Echa Rezydencji]  
Moneta 4: [Przy Trafieniu] Jeżeli cel ma [Echa Rezydencji], zwiększa Licznik [Zatonięcie] o 3

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli cel ma 5+ Licznik [Zatonięcie], Moc Monet +2  
Moneta 1: [Przy Trafieniu] Nakłada +3 Licznika [Zatonięcie]  
Moneta 4: [Przy Trafieniu] Nakłada w następnej turze 2 [Echa Rezydencji]  
Moneta 4: [Przy Trafieniu] Jeżeli cel ma [Echa Rezydencji], zwiększa Licznik [Zatonięcie] o 3

#### Obrona: Przygotowanie do Polowania

| Ulepszenie | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral   | obrona: blok |          7 |         +6 |      1 |           +1 |    1 |
|          4 | Posępność | obrona: blok |          7 |         +6 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli cel ma 10+ [Zatonięcie], Moc Monet +3

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli cel ma 10+ [Zatonięcie], Moc Monet +7

#### Pasywka bojowa: Reakcja według Kamerdynera

*od ulepszenia 2; posiadane 4× Posępność*

- Po wygranym Starciu nakłada na cel 1 [Zatonięcie] (3 razy na turę)

#### Pasywka bojowa: Reakcja według Kamerdynera

*od ulepszenia 4; posiadane 4× Posępność*

- Po wygranym Starciu nakłada na cel 1 [Zatonięcie] (3 razy na turę)  
- Jeżeli cel ma [Echa Rezydencji], nakłada zamiast tego 3 [Zatonięcie]

#### Pasywka wsparcia: Trening na Ten Dzień

*od ulepszenia 3; posiadane 4× Posępność*

Gdy 1 Sojusznik z najniższą Poczytalnością trafi wroga z 5+ [Zatonięcie], odzyskuje 2 Poczytalności (4 razy na turę)

#### Pasywka wsparcia: Trening na Ten Dzień

*od ulepszenia 4; posiadane 4× Posępność*

Gdy 1 Sojusznik z najniższą Poczytalnością trafi wroga z 5+ [Zatonięcie], odzyskuje 3 Poczytalności (4 razy na turę)

#### Kwestie

- **Identity Acquisition:** Excuse me. Here is a cup of afternoon tea, courtesy of this house. Please, enjoy your time here.
- **Morning Greeting:** We have prepared a simple spread of custard and a glass of wine for your breakfast. Please relax and enjoy; a cup of black tea will be provided after this meal.
- **Afternoon Greeting:** This manor rarely gets any sunlight. Fuel has been added to the wood stove as per Chief Butler Outis' orders. Warm yourself by the flame, if you will.
- **Evening Greeting:** A warm, thick duck-down bedding has been prepared in anticipation of the cold. Please have a restful night. We must depart to join a meeting regarding a hunt.
- **Chatter #1:** Chief Butler Outis converses day and night with the Mistress in our stead. Some nights, her communication with the mistress lasts until sunrise.
- **Chatter #2:** You may hear some... commotion coming from the basement. The Butlers are training in preparation for the hunt; please do not allow the sounds of clashing metal to worry your mind.
- **Chatter #3:** This tea is prepared using leaves delivered to this location by the Devyat' Association, which are then infused directly without being broken. It would be no hyperbole to say that this tea variety represents the utmost excellence of Wuthering Heights that has been passed down through the generations.
- **Post-Uptie Chat 1:** Ah, has the noise disturbed you? Our sincere apologies. An uninvited guest had appeared on the premises... and it took the Butlers quite the effort to persuade them to leave the premises. Please, do understand.
- **Post-Uptie Chat 2:** Naturally, any and all damages or stains incurred in response to the uninvited guests will be taken care of by the excellent cleaning-expert Butlers of this manor. There is no need for the Master to worry; it will all be returned to as it was before.
- **Idle:** ... If my presence disturbs your deliberation, then the room will be vacated for your sole use.
- **Uptying:** ... Come this way, dear guests. For any and all uninvited guests, though we sincerely apologize for this impudence, we must ask you to immediately vacate the premises.
- **Deployment:** Always ready to be summoned.
- **Stage Entry:** Faust will receive the guests.
- **Viewed in Battle:** Is something not to your liking?
- **Commencing Attack:** ... This way, please.
- **Enemy Stagger:** How ill-mannered.
- **Staggered:** Hup...
- **Enemy Killed:** Please vacate the premises. Immediately.
- **Death:** My deepest apologies, Lady Outis, Mistress. I have failed to complete my... duties...
- **Check Passed:** Effortless.
- **Check Failed:** These deficiencies were unexpected...
- **Victory Cry:** The uninvited guests have been properly taken care of. A few possible points of failure for the hunt have been identified. They will be addressed.
- **Extra Conditions Fulfilled:** A perfect response. Let this success inspire us to lead the Chief Butler's hunt to victory.
- **Defeat Wail:** My most sincere apologies; our response was far from acceptable. ... I shall try my utmost to not disappoint you.

### 000 Biuro MultiCrack Szefowa — Faust

> Dziesiąta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 4                                                           |
| HP                        | 66 (+2,28 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom −1                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×2 (Fatal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Posępność                                                   |
| Przynależność             | Multi_Crack                                                 |
| Słowa kluczowe            | Ładowanie                                                   |
| Data aktualizacji         | 20240808                                                    |

#### Umiejętność 1 (×3): Aktywacja 40Y-3

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Cięcie |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Żądza  | Cięcie |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zużywa 5 Licznika [Ładowanie], aby zyskać Moc Monet +1  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o 2

*Od ulepszenia 2:* [Przy Użyciu] Zużywa 5 Licznika [Ładowanie], aby zyskać Moc Monet +1  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o 3

*Od ulepszenia 4:* [Przy Użyciu] Zużywa 5 Licznika [Ładowanie], aby zyskać Moc Monet +2  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o 3

#### Umiejętność 2 (×2): Wsteczny Prąd Ładowania

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Obuch |          4 |         +3 |      3 |           +4 |    1 |
|          3 | Zawiść | Obuch |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli Licznik [Ładowanie] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Ładowanie])% Maks. HP, aby zwiększyć Licznik [Ładowanie] do 10  
[Przy Użyciu] Zużywa 10 Licznika [Ładowanie], aby zyskać Moc Monet +1  
Moneta 3: Jeżeli Rezonans (z tą Umiejętnością włącznie) wynosi 3 lub więcej, zużywa cały posiadany Licznik [Ładowanie] i zadaje +([Ładowanie])% obrażeń za każdy 1 [Ładowanie] zużyty tą Umiejętnością (maks. 60%)

*Od ulepszenia 2:* [Przy Użyciu] Jeżeli Licznik [Ładowanie] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Ładowanie])% Maks. HP, aby zwiększyć Licznik [Ładowanie] do 10  
[Przy Użyciu] Zużywa 10 Licznika [Ładowanie], aby zyskać Moc Monet +1  
Moneta 3: Jeżeli Rezonans (z tą Umiejętnością włącznie) wynosi 3 lub więcej, zużywa cały posiadany Licznik [Ładowanie] i zadaje obrażenia +([Ładowanie] + 3)% za każdy 1 [Ładowanie] zużyty tą Umiejętnością (maks. 120%)

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli Licznik [Ładowanie] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Ładowanie])% Maks. HP, aby zwiększyć Licznik [Ładowanie] do 10  
[Przy Użyciu] Zużywa 10 Licznika [Ładowanie], aby zyskać Moc Monet +2  
Moneta 3: Jeżeli Rezonans (z tą Umiejętnością włącznie) wynosi 3 lub więcej, zużywa cały posiadany Licznik [Ładowanie] i zadaje obrażenia +([Ładowanie] + 4)% za każdy 1 [Ładowanie] zużyty tą Umiejętnością (maks. 180%)

#### Umiejętność 3 (×1): Ładowanie 40Y-3

| Ulepszenie | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Posępność | Obuch |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* Przy 2+ [Ładowanie] Moc Monet +2  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o ([Ładowanie] + 4) (maks. 7)  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o ([Ładowanie] + 4) (maks. 7)  
Moneta 4: Przy 3+ [Ładowanie] zadaje +4% obrażeń za każdy 1 [Ładowanie] (maks. 20%)

*Od ulepszenia 4:* Moc Monet +1 za każdy 1 [Ładowanie] (maks. 4)  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o ([Ładowanie] + 5) (maks. 8)  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik [Ładowanie] o ([Ładowanie] + 5) (maks. 8)  
Moneta 4: Przy 3+ [Ładowanie] zadaje +8% obrażeń za każdy 1 [Ładowanie] (maks. 40%)  
Moneta 4: [Przy Trafieniu] Nakłada w następnej turze 1 Wrażliwość na Zazdrość  
- Przy 2+ [Ładowanie] nakłada dodatkowo 1 Wrażliwość na Zazdrość

#### Obrona: Ładowanie

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +4 |      1 |           +0 |    1 |
|          4 | Zawiść  | obrona: blok |         12 |         +6 |      1 |           +0 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik [Ładowanie] o 2 (2 razy na turę)

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa własny Licznik [Ładowanie] o 4 (2 razy na turę)

#### Pasywka bojowa: Rozkład Prądem

*od ulepszenia 2; posiadane 3× Zawiść*

Za każde łączne zużycie 10 własnego Licznika [Ładowanie] podczas walki zyskuje 1 [Ładowanie]  
Przy 2+ [Ładowanie] zadaje +([Ładowanie] x 3)% obrażeń (maks. 15%)  
  
Przy zabiciu wroga ta jednostka i 1 Sojusznik z najniższym Licznikiem [Ładowanie] zyskują Licznik [Ładowanie] równy [Ładowanie] (maks. 3; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Ładowanie])

#### Pasywka bojowa: Rozkład Prądem

*od ulepszenia 4; posiadane 3× Zawiść*

Za każde łączne zużycie 10 własnego Licznika [Ładowanie] podczas walki zyskuje 1 [Ładowanie]  
Przy 2+ [Ładowanie] zadaje +([Ładowanie] x 3)% obrażeń (maks. 15%)  
- Jeżeli cel ma poniżej 50% HP, zadaje dodatkowo +([Ładowanie] x 5)% obrażeń (maks. 25%)  
  
Przy zabiciu wroga ta jednostka i 2 Sojuszników z najniższym Licznikiem [Ładowanie] zyskują Licznik [Ładowanie] równy (2 + [Ładowanie]) (maks. 5; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Ładowanie])

#### Pasywka wsparcia: Pomocniczy Prąd Rozkładu

*od ulepszenia 3; posiadane 5× Zawiść*

Gdy 1 Sojusznik z najniższym Licznikiem [Ładowanie] zabije wroga, zyskuje 2 Licznika [Ładowanie] (1 raz na turę; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Ładowanie])

#### Pasywka wsparcia: Pomocniczy Prąd Rozkładu

*od ulepszenia 4; posiadane 5× Zawiść*

Gdy 1 Sojusznik z najniższym Licznikiem [Ładowanie] zabije wroga, zyskuje 3 Licznika [Ładowanie] (1 raz na turę; najpierw sojusznicy z Umiejętnościami zużywającymi lub samodzielnie zyskującymi [Ładowanie])

#### Kwestie

- **Identity Acquisition:** While there are numerous deficiencies and points of failure to this plan, Faust will hone it into utter, unfailing perfection.
- **Morning Greeting:** An arm can always be spared for a cup of coffee in the morning. There are three more arms to utilize, after all.
- **Afternoon Greeting:** Please remember to submit the receipts after using a corporate credit card. This Office may no longer provide a lunch budget should the employees continuously fail to submit their receipts.
- **Evening Greeting:** The prosthetic body does not feel muscular pain, even if it were to be put to work from sunrise to sunset. ... However, a regular maintenance may be needed to prevent creaking.
- **Chatter #1:** If you would ever consider replacing more parts of your body than your head with prostheses, a good recommendation would be the Tres Association certified G10 model prosthetic legs. A high-performance ambulatory apparatus is very useful for making oneself scarce from high-risk situations.
- **Chatter #2:** The WARP train round trip ticket has been purchased via private funds, with Faust reserving a first class seat. I do not yet know why the first class ticket has been purchased instead of the economy class ticket; however, Faust must know of the reason.
- **Chatter #3:** A whole-body prosthetic has been considered, yes. ... However, the upgrade budget for higher-quality prosthetics and the related risks were too significant to be followed through. Faust believed it would be more efficient to slowly upgrade this body toward an increasingly stronger partial prosthetic.
- **Post-Uptie Chat 1:** A greatsword of this size can be wielded by any individual as long as they possess sufficient budget, enough time to acclimatize, and the work of a trusted workshop. Of course, it is up to each individual as to what kind of combat style they wish to employ.
- **Post-Uptie Chat 2:** Prosthetic bodies are rarely installed with pain receptors. Therefore, Fixers such as ourselves who utilize prosthetic bodies do not fear pain or injury. ... It is much more expensive to fix a prosthetic than it is to heal flesh, however.
- **Idle:** To summon someone and not address them is a highly inefficient action.
- **Uptying:** The contract target has been taken care of. The meticulous preparation for this contract expedition has certainly borne fruit.
- **Deployment:** All preparations have been made. Let us depart.
- **Stage Entry:** Model 40Y-3 fully charged. Ready for deployment.
- **Viewed in Battle:** Have you forgotten the plan?
- **Commencing Attack:** Attack range confirmed.
- **Enemy Stagger:** Efficiently...
- **Staggered:** Uh...
- **Enemy Killed:** ... dispatched.
- **Death:** I have... insurance...
- **Check Passed:** As per Faust's calculations.
- **Check Failed:** There was an error.
- **Victory Cry:** A predictable victory, guided by Faust's knowledge.
- **Extra Conditions Fulfilled:** This contract was completed far ahead of schedule. A majority of credit would go to Faust and my expertise, but your effort was at an acceptable level as well.
- **Defeat Wail:** This expedition was a failure. Expeditious retreat and prosthetic replacement are necessary before we prepare for the expedition once again.

### 000 LCE E.G.O:: Gwiazda Żarzącego Kwiatu — Faust

> Jedenasta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 5                                                           |
| HP                        | 66 (+2,28 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom −1                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×2 (Fatal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 50% / 20%                                                   |
| Grzech wyróżniony         | Gniew                                                       |
| Przynależność             | Limbus_Company, Limbus_Company_Lce                          |
| Słowa kluczowe            | Podpalenie                                                  |
| Data aktualizacji         | 20250123                                                    |

#### Umiejętność 1 (×3): Zapłon

| Ulepszenie | Grzech   | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Obuch |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Lenistwo | Obuch |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Przy 10+ [Podpalenie] zadaje +10% obrażeń  
[Przy Użyciu] Zyskuje 7 [Podpalenie] i zwiększa własny Licznik [Podpalenie] o 1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Podpalenie]

*Od ulepszenia 2:* [Przy Użyciu] Przy 10+ [Podpalenie] zadaje +10% obrażeń  
[Przy Użyciu] Zyskuje 7 [Podpalenie] i zwiększa własny Licznik [Podpalenie] o 1  
[Przy Użyciu] Przy 10+ ([Podpalenie] własnej + [Podpalenie] celu) Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Przy 10+ [Podpalenie] nakłada dodatkowo 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Podpalenie]

*Od ulepszenia 4:* [Przy Użyciu] Przy 10+ [Podpalenie] zadaje +10% obrażeń  
[Przy Użyciu] Zyskuje 7 [Podpalenie] i zwiększa własny Licznik [Podpalenie] o 1  
[Przy Użyciu] Moc Monet +1 za każde 10 ([Podpalenie] własnej + [Podpalenie] celu) (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Przy 10+ [Podpalenie] nakłada dodatkowo 3 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Podpalenie]

#### Umiejętność 2 (×2): E.G.O Gwiazda Żarzącego Kwiatu

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Obuch |          2 |         +4 |      3 |           +3 |    1 |
|          3 | Pycha  | Obuch |          3 |         +4 |      3 |           +3 |    1 |
|          4 | Pycha  | Obuch |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* Przy 10+ [Podpalenie] zadaje +10% obrażeń  
[Przy Użyciu] Zwiększa własny Licznik [Podpalenie] o 4  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Trafienie bez Pęknięcia] Nakłada 2 [Podpalenie]

*Od ulepszenia 2:* Zadaje +10% obrażeń za każde 10 [Podpalenie] (maks. 20%)  
[Przy Użyciu] Zwiększa własny Licznik [Podpalenie] o 4  
[Przy Użyciu] Przy 4+ ([Podpalenie] własnej + [Podpalenie] celu) Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Trafienie bez Pęknięcia] Nakłada 3 [Podpalenie]

*Od ulepszenia 4:* Zadaje +10% obrażeń za każde 10 [Podpalenie] (maks. 20%)  
[Przy Użyciu] Zwiększa własny Licznik [Podpalenie] o 4  
[Przy Użyciu] Moc Monet +1 za każde 4 ([Podpalenie] własnej + [Podpalenie] celu) (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Trafienie bez Pęknięcia] Nakłada 3 [Podpalenie]  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 15+ [Podpalenie], zwiększa Licznik [Podpalenie] celu o 2

#### Umiejętność 3 (×1): Pociągnięta Płomieniem

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Obuch |          4 |         +4 |      3 |           +5 |    1 |
|          4 | Gniew  | Obuch |          5 |         +4 |      3 |           +5 |    1 |

*Od ulepszenia 3:* [Początek Walki] Zyskuje 7 [Podpalenie] i zwiększa własny Licznik [Podpalenie] o 1  
[Przed Użyciem] Przy 30+ [Podpalenie] zamiast tego uruchamia „Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】”  
Zadaje +7.5% obrażeń za każde 5 [Podpalenie] (maks. 30%)  
[Przy Użyciu] Przy 10+ ([Podpalenie] własnej + [Podpalenie] celu) Moc Bazowa +1  
[Przy Użyciu] Jeżeli brakuje tej jednostce 30%+ HP, Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]

*Od ulepszenia 4:* [Początek Walki] Zyskuje 7 [Podpalenie] i zwiększa własny Licznik [Podpalenie] o 1  
[Przed Użyciem] Przy 30+ [Podpalenie] zamiast tego uruchamia „Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】”  
Zadaje +12.5% obrażeń za każde 5 [Podpalenie] (maks. 50%)  
[Przy Użyciu] Moc Bazowa +1 za każde 10 ([Podpalenie] własnej + [Podpalenie] celu) (maks. 2)  
[Przy Użyciu] Moc Monet +1 za każde 30% brakującego HP tej jednostki (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]

#### Umiejętność 4 (×0): Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Obuch |          4 |         +4 |      3 |           +5 |    1 |
|          4 | Gniew  | Obuch |          5 |         +4 |      3 |           +5 |    1 |

*Od ulepszenia 1:* Ta jednostka umiera po zakończeniu ataku tą Umiejętnością.  
- Jeżeli podczas używania tej Umiejętności HP spadnie do 1, pozostaje na poziomie 1 do końca działania Umiejętności.  
[Przy Użyciu] Zadaje +7.5% obrażeń za każde 5 [Podpalenie] (maks. 30%)  
[Przy Użyciu] Przy 10+ ([Podpalenie] własnej + [Podpalenie] celu) Moc Bazowa +1  
[Przy Użyciu] Moc Monet +1 za każde 30% brakującego HP tej jednostki (maks. 2)  
[Przed Atakiem] Waga ataku +1 za każde 20% brakującego HP tej jednostki (maks. 2)  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Przy Trafieniu] Zadaje +10% obrażeń za każde 20% brakującego HP tej jednostki (maks. 30%)

*Od ulepszenia 4:* Ta jednostka umiera po zakończeniu ataku tą Umiejętnością.  
- Jeżeli podczas używania tej Umiejętności HP spadnie do 1, pozostaje na poziomie 1 do końca działania Umiejętności.  
[Przy Użyciu] Zadaje +12.5% obrażeń za każde 5 [Podpalenie] (maks. 50%)  
[Przy Użyciu] Moc Bazowa +1 za każde 10 ([Podpalenie] własnej + [Podpalenie] celu) (maks. 2)  
[Przy Użyciu] Moc Monet +1 za każde 30% brakującego HP tej jednostki (maks. 3)  
[Przed Atakiem] Waga ataku +1 za każde 20% brakującego HP tej jednostki (maks. 4)  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada 4 [Podpalenie]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 2: [Przy Trafieniu] Nakłada 4 [Podpalenie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Przy Trafieniu] Zadaje +10% obrażeń za każde 20% brakującego HP tej jednostki (maks. 30%)

#### Obrona: Rezonans przez Dostrojenie Gwiazdy Żarzącego Kwiatu.

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           −2 |    1 |
|          4 | Gniew   | obrona: unik |          4 |        +10 |      1 |           −2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Traci 5 [Podpalenie] (1 raz na turę)  
[Udany Unik] Traci 5 [Podpalenie] (1 raz na turę)

*Od ulepszenia 4:* [Przy Użyciu] Przy 10+ [Podpalenie] Moc Monet +3  
[Przy Użyciu] Traci 5 [Podpalenie] (1 raz na turę)  
[Udany Unik] Traci 5 [Podpalenie] (1 raz na turę)

#### Pasywka bojowa: Ognioodporność

*od ulepszenia 1*

Nie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Podpalenie].

#### Pasywka bojowa: Ognioodporność

*od ulepszenia 2*

Nie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Podpalenie].

#### Pasywka bojowa: Ćma Płomieni

*od ulepszenia 2; posiadane 3× Gniew*

Na początku walki, jeżeli brakuje tej jednostce 80%+ HP i [Podpalenie] jest poniżej 30, zyskuje [Podpalenie] do 30. (1 raz na spotkanie)  
  
Na koniec tury zyskuje w następnej turze 1 [Wzrost Poziomu Ataku] za każde 6 [Podpalenie] (maks. 5)  
  
Po śmierci uruchamia następujące efekty:  
- Nakłada 2 [Podpalenie] na wszystkich wrogów i dzieli własne [Podpalenie] między nich (maks. 3 na wroga)  
- Zyskuje po 2 zasoby E.G.O dla 2 atrybutów o najmniejszym stanie  
  
Jeżeli ta jednostka umarła wskutek efektu Umiejętności „Maks. Dostrojenie Gwiazdy Żarzącego Kwiatu 【Degradacja】”, efekt jest wzmocniony:  
- Nakłada 3 [Podpalenie] na wszystkich wrogów i dzieli własne [Podpalenie] między nich (maks. 5 na wroga)  
- Zyskuje po 2 zasoby E.G.O dla 2 atrybutów o najmniejszym stanie  
- Jeżeli ta jednostka miała 30+ [Podpalenie], nakłada 3 [Wzrost Poziomu Ataku] na 1 Sojusznika wchodzącego z rezerwy

#### Pasywka wsparcia: Ciepło Resztkowe

*od ulepszenia 3; rezonans 3× Gniew*

Gdy 1 Sojusznik z najniższą Poczytalnością nakłada [Podpalenie] efektem trafienia Umiejętności podstawowej, nakłada dodatkowo 2 [Podpalenie] (maks. 3 razy)  
- Jeżeli atakowany cel ma 30+ [Podpalenie], zamiast tego zwiększa Licznik [Podpalenie] o 1 (maks. 3 razy)

#### Kwestie

- **Identity Acquisition:** Subject's engagement threat level: moderately high. However, considering its self-destructive nature under specific circumstances... Ardor Blossom Moth final designation: WAW-5.
- **Morning Greeting:** The following tasks must be completed this morning: Distortion progression rate check, Peccatula population inspection, and Abnormality containment work. There is much to be done today.
- **Afternoon Greeting:** The After Team of the Clearance department has captured a new Abnormality, which is currently en route to this facility. It may be best that we replace today's allotted lunchtime with... research time for the new Abnormality.
- **Evening Greeting:** Yi Sang. Your passion is admirable, but delayed bedtime may adversely affect the efficacy of your research contributions. LCE promotes the timely departure of its employees— ... Well, I don't suppose mere words will make him budge. J-just a moment, I implore you to leave the lights on for now. There is still much—
- **Chatter #1:** Mm. If merit were to be the sole criterion by which one's aptitude for the LCE Chief researcher position may be measured, then that role would have rightly gone to Faust. Yet... that is simply not my place to be as I am now.
- **Chatter #2:** Unless one is a genius of Faust's caliber, one mustn't approach Distortions and Abnormalities equipped with only basic statistics and theories. The other ingredients include intuition to be able to identify and read the trends, passion for the academics, and... some luck.
- **Chatter #3:** LCE extracts Enkephalin in PE-Box forms and even employs a former L Corp. branch researcher... It would be no hyperbole to say that LCE has, in every way that matters, succeeded Lobotomy Corporation. Though we are still quite busy playing catch-up, we will one day surpass them.
- **Post-Uptie Chat 1:** Given that wings were not originally a part of the human set of limbs, the very first attempts at flight with this E.G.O gear resulted in several... trials and errors. Using this experience as a lesson, perhaps it would be wise to raise the ceilings of the experiment sector somewhat.
- **Post-Uptie Chat 2:** Most researchers here at the LCE were enticed by the promise of new knowledge—like moths drawn to a flicker of flame. So was Faust. Perhaps that explains the assignment of this E.G.O.
- **Idle:** ... If you have completed your observation, it is recommended that you turn off the device.
- **Uptying:** Those enticed by the lapping flames will be incinerated without a trace.
- **Deployment:** What kind of experiment is it, this time?
- **Stage Entry:** Subject type identified.
- **Viewed in Battle:** Keep your distance. This flame spreads far.
- **Commencing Attack:** Proceeding with subject repression.
- **Enemy Stagger:** Structural integrity collapse confirmed.
- **Staggered:** Hngh...
- **Enemy Killed:** Subject incinerated.
- **Death:** This experiment... will be a failure...
- **Check Passed:** Experiment success. As expected.
- **Check Failed:** ... New variable identified. The hypothesis will have to be updated.
- **Victory Cry:** Experiment complete. No progress from the preceding research data. Not a failure, but this can hardly be deemed a success.
- **Extra Conditions Fulfilled:** E.G.O Synchronization rate normal. Subject behavior pattern extraction complete. Progressing to the next research seems viable at this level of success.
- **Defeat Wail:** ... E.G.O:Ardor Blossom Star damage level at 70%. Experiment continuation is infeasible. ... Further preparation seems necessary before the continuation of this experiment.

### 000 Wataha Heishou - Gałąź Mao, Adept — Faust

> Dwunasta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 6                                                           |
| HP                        | 76 (+3,19 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–6 / 4–7 / 4–7                                       |
| Poziom obrony             | poziom +3                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 50%                                                         |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Black_Beast_Rabbit, H_Corp                                  |
| Słowa kluczowe            | Rozdarcie                                                   |
| Data aktualizacji         | 20250522                                                    |

#### Umiejętność 1 (×3): Szybki Krok

| Ulepszenie | Grzech   | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Cięcie |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Lenistwo | Cięcie |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli cel ma 6+ [Rozdarcie], Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]

*Od ulepszenia 2:* [Przy Użyciu] Jeżeli cel ma 4+ [Rozdarcie], Moc Monet +1  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)

*Od ulepszenia 4:* Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1  
[Przy Użyciu] Jeżeli cel ma 4+ [Rozdarcie], Moc Monet +1  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)

#### Umiejętność 2 (×2): Przedrę drogę, mój Panie.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Cięcie |          3 |         +6 |      2 |           +2 |    1 |
|          3 | Pycha  | Cięcie |          4 |         +6 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli cel ma 4+ [Rozdarcie], Moc Monet +1  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 1  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: Jeżeli cel ma [Obrzęd Śmierci 【Haste】] lub [Obrzęd Śmierci 【Szczelina】], zadaje +30% obrażeń

*Od ulepszenia 2:* [Przy Użyciu] Jeżeli cel ma 4+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Zyskuje w następnej turze 2 [Pośpiech] (1 raz na turę)  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 1  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: Jeżeli cel ma [Obrzęd Śmierci 【Haste】] lub [Obrzęd Śmierci 【Szczelina】], zadaje +30% obrażeń

*Od ulepszenia 4:* Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x własne [Ostrze Gwiazdy Tianjiu])% obrażeń (maks. 50%)  
Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1  
[Przy Użyciu] Jeżeli cel ma 4+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Zyskuje w następnej turze 2 [Pośpiech] (1 raz na turę)  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 1  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: Jeżeli cel ma [Obrzęd Śmierci 【Haste】] lub [Obrzęd Śmierci 【Szczelina】], zadaje +50% obrażeń

#### Umiejętność 3 (×1): Ani oko, ani ucho nie dogoni.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Cięcie |          5 |         +3 |      3 |           +3 |    1 |
|          4 | Obżar. | Cięcie |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Rozdarcie] celu)% obrażeń (maks. 50%)  
Jeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1  
[Początek Walki] Zyskuje 1 [Obrona Wsparcia] (1 raz na turę)  
[Przed Użyciem] Przy 10+ [Ostrze Gwiazdy Tianjiu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”  
[Przy Użyciu] Zyskuje 3 [Biegacz【Mao】]  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 2  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 1: [Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Haste】]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: Przy 10+ Szybkości zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)

*Od ulepszenia 4:* Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Rozdarcie] celu)% obrażeń (maks. 50%)  
Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)  
[Początek Walki] Zyskuje 1 [Obrona Wsparcia] (1 raz na turę)  
[Przed Użyciem] Przy 10+ [Ostrze Gwiazdy Tianjiu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Zyskuje 3 [Biegacz【Mao】]  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 2  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 1: [Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Haste】]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: Przy 10+ Szybkości zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Haste】]

#### Umiejętność 4 (×0): Wyższy Heishou - Technika Mao: Objawienie Morza Chmur

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Cięcie |          5 |         +3 |      3 |           +4 |    1 |
|          4 | Obżar. | Cięcie |          5 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 3:* Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Rozdarcie] celu)% obrażeń (maks. 50%)  
Jeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Przy 10+ Szybkości zyskuje 20 [Oddech]; jeżeli Licznik [Oddech] jest poniżej 4, zyskuje Licznik [Oddech] do maks. 4  
[Przy Użyciu] Zyskuje 3 [Biegacz【Mao】]  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 2  
[Koniec Ataku] Zużywa 10 [Ostrze Gwiazdy Tianjiu]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 1: [Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Szczelina】]  
Moneta 1: [Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Haste】]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: Przy 10+ Szybkości zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Szczelina】]

*Od ulepszenia 4:* Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Rozdarcie] celu)% obrażeń (maks. 50%)  
Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)  
[Przy Użyciu] Moc Monet +1 za każde 10 [Rozdarcie] na celu (maks. 2)  
[Przy Użyciu] Przy 10+ Szybkości zyskuje 20 [Oddech]; jeżeli Licznik [Oddech] jest poniżej 4, zyskuje Licznik [Oddech] do maks. 4  
[Przy Użyciu] Zyskuje 3 [Biegacz【Mao】]  
[Wygrane Starcie] Zwiększa Licznik [Rozdarcie] o 2  
[Koniec Ataku] Zużywa 10 [Ostrze Gwiazdy Tianjiu]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 1: [Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Szczelina】]  
Moneta 1: [Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Haste】]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: Przy 10+ Szybkości zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Przy 10+ Szybkości używa tej monety ponownie (1 raz na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Szczelina】]  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Nakłada [Obrzęd Śmierci 【Haste】]

#### Obrona: Zostanie to wykonane.

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | obrona: kontra |          5 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Kontra Starciowa]  
[Początek Walki] Zyskuje 1 [Obrona Wsparcia] (1 raz na turę)  
[Przy Użyciu] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)  
[Przy Użyciu] Zyskuje 3 [Biegacz【Mao】]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]

*Od ulepszenia 4:* [Kontra Starciowa]  
[Początek Walki] Zyskuje 1 [Obrona Wsparcia] (1 raz na turę)  
[Przy Użyciu] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)  
[Przy Użyciu] Zyskuje 3 [Biegacz【Mao】]  
[Przy Użyciu] Zyskuje Moc Bazową zależnie od przewagi Szybkości (Moc Bazowa +1 za każde 2 różnicy Szybkości; maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]

#### Obrona: Ochrona Zwinnych Stóp

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | obrona: blok |          4 |         +8 |      1 |           +2 |    1 |
|          4 | Obżar. | obrona: blok |          4 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [Blok Zdatny do Starcia]  
Umiejętność wyłącznie dla [Obrona Wsparcia]  
[Przed Użyciem] Przy 10+ [Ostrze Gwiazdy Tianjiu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”  
[Przy Użyciu] Ta Umiejętność zyskuje +1 Poziomu Obrony za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)  
[Przy Użyciu] Do końca działania tej Umiejętności nie zostaje Ogłuszona przez obrażenia  
[Przy Użyciu] Zyskuje 2 [Ochrona] (1 raz na turę)  
Moneta 1: [Moneta Niezniszczalna]

*Od ulepszenia 4:* [Blok Zdatny do Starcia]  
Umiejętność wyłącznie dla [Obrona Wsparcia]  
[Przed Użyciem] Przy 10+ [Ostrze Gwiazdy Tianjiu] zamiast tego uruchamia „Wyższy Heishou - Technika Mao: Objawienie Morza Chmur”  
[Przy Użyciu] Ta Umiejętność zyskuje +1 Poziomu Obrony za każde 10% łącznie utraconego HP tej jednostki podczas tej potyczki (maks. 6; według Maks. HP z chwili uruchomienia)  
[Przy Użyciu] Do końca działania tej Umiejętności nie zostaje Ogłuszona przez obrażenia  
[Przy Użyciu] Zyskuje 2 [Ochrona] (1 raz na turę)  
Moneta 1: [Moneta Niezniszczalna]

#### Obrona: 1021207

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | obrona: kontra |          5 |         +3 |      3 |           +4 |    1 |
|          4 | Obżar. | obrona: kontra |          5 |         +4 |      3 |           +4 |    1 |

#### Pasywka bojowa: Gwiazda Tianjiu

*od ulepszenia 1*

Gdy Licznik [Obrzęd Śmierci 【Szczelina】] spadnie do 0 i efekt wygaśnie, zyskuje [Znak Rozkładu]

#### Pasywka bojowa: 1021202

*od ulepszenia 1*



#### Pasywka bojowa: Gwiazda Tianjiu

*od ulepszenia 2*

Gdy Licznik [Obrzęd Śmierci 【Szczelina】] spadnie do 0 i efekt wygaśnie, zyskuje [Znak Rozkładu]

#### Pasywka bojowa: Mutacja Heishou [Mao] / Adept Gałęzi Mao

*od ulepszenia 2; posiadane 5× Obżar.*

Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +2% obrażeń za każde 1 różnicy Szybkości (maks. 10%)  
  
Za każdym razem, gdy sojusznik uruchomi Obrzęd Śmierci podczas walki, zyskuje 1 [Ostrze Gwiazdy Tianjiu] (maks. 5 razy na turę)  
- Jeżeli ta jednostka go uruchomiła, zyskuje dodatkowo 1 [Ostrze Gwiazdy Tianjiu]  
Przy uruchomieniu efektu [Obrona Wsparcia] zyskuje 5 [Ostrze Gwiazdy Tianjiu]

#### Pasywka bojowa: 1021202

*od ulepszenia 2*



#### Pasywka wsparcia: Błyskawiczne Ostrze

*od ulepszenia 3; rezonans 4× Obżar.*

Gdy sojusznik z najwyższą Szybkością zadaje obrażenia [Rozdarcie], zyskuje w następnej turze 1 [Wzrost Poziomu Ataku] (maks. 3 razy na turę)

#### Kwestie

- **Identity Acquisition:** That answer will suffice, my lord.
- **Morning Greeting:** The outcome of the night's assignment can be reviewed here. All has been done as willed.
- **Afternoon Greeting:** Though there is no immediate path toward learning all of my lord's teachings, I will attempt to acquire them in full while the sun shines. It is Faust's expertise.
- **Evening Greeting:** My purpose is to fade with the night's glint of the moon. Yet, should I be summoned, I shall stand by my lord as the moon shelters behind the clouds.
- **Chatter #1:** What use is there to learning, to questioning...? A conundrum that had once harrowed my mind. Were it not for my lord... I would have been a mere ordinary human, not Faust.
- **Chatter #2:** A Heishou may be but a tool... but Faust is different. As a beast of the Heishou - Mao Branch... as a Pinky... I am, with my name restored, a loyal blade and a devoted disciple of my lord.
- **Chatter #3:** Accessing the Gesellschaft is... necessary, but I do so with reluctance. They attempt again and again to instruct and enlighten me, but gaining an understanding of my lord's teachings already consumes a majority of my days. ... Yet, one must face their disinclinations for the pursuit of learning.
- **Post-Uptie Chat 1:** Cloudsplitting Manifestation(雲解顯現). Beasts of the Mao must follow in my wake, for my lord has bestowed me the leash.
- **Post-Uptie Chat 2:** My lord has impressed upon us many times that the righteous do not make weapons of their might. Yet... even I, a brute whose blade swings before her lips speak, persevere toward righteousness... perhaps that is a road, a way(道) for one to walk down.
- **Idle:** I must be one of the great humans as well, as I have no resentment or covetousness in me. ... My lord, do not laugh.
- **Uptying:** Your will is understood; that vision of righteousness shall swiftly be realized.
- **Deployment:** To restore the righteousness that was lost.
- **Stage Entry:** Adept Heishou, into the fray.
- **Viewed in Battle:** Command without hesitation.
- **Commencing Attack:** Futility inheres in impossibility(不可違也). I will not be restrained.
- **Enemy Stagger:** Futile.
- **Staggered:** ... Indeed.
- **Enemy Killed:** Find your enlightenment, now.
- **Death:** ... Please straighten my bamboo hat. Yes. That is... enough...
- **Check Passed:** There are times when a blade has the makings of a solution.
- **Check Failed:** Failed to read the situation at hand.
- **Victory Cry:** Perpetual flawlessness is an impossibility. Yet, perseverance in that infinite approach to perfection makes this a non-issue.
- **Extra Conditions Fulfilled:** Today was a day of no shame, for I have made my contributions to bringing about righteousness. I shall face tomorrow with pride.
- **Defeat Wail:** ... The rising sun brings me shame. ... My display of incompetence today was no different from my years as an ordinary human.

### 000 Wschodnie Stowarzyszenie Shi Sekcja 3 — Faust

> Trzynasta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 0                                                           |
| HP                        | 60 (+2,82 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom −1                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×0,5 (Endured), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 50% / 20%                                             |
| Grzech wyróżniony         | Gniew                                                       |
| Przynależność             | Shi                                                         |
| Słowa kluczowe            | Krwawienie, Oddech                                          |
| Data aktualizacji         | 20251009                                                    |

#### Umiejętność 1 (×3): Rozcięcie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | Cięcie |          3 |         +3 |      2 |           +1 |    1 |
|          3 | Gniew  | Cięcie |          4 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zyskuje 1 [Oddech]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

*Od ulepszenia 2:* [Przy Użyciu] Przy 4+ (suma własnej [Oddech] i [Krwawienie] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 2 [Oddech]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

*Od ulepszenia 4:* [Przy Użyciu] Przy 4+ (suma własnej [Oddech] i [Krwawienie] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 2 [Oddech]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]

#### Umiejętność 2 (×2): Zabezpieczenie Dystansu

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Cięcie |          3 |         +3 |      3 |           +2 |    1 |
|          3 | Pycha  | Cięcie |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zadaje +11% obrażeń za każde 4 [Oddech] (maks. 44%)  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 1  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 3: [Trafienie Krytyczne] Nakłada 2 [Krwawienie]

*Od ulepszenia 2:* [Przy Użyciu] Moc Starcia +1 za każde 4 (suma własnej [Oddech] i [Krwawienie] celu) (maks. 2)  
[Przy Użyciu] Zadaje +11% obrażeń za każde 4 [Oddech] (maks. 44%)  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 1  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 3: [Trafienie Krytyczne] Nakłada 2 [Krwawienie]

*Od ulepszenia 4:* [Przy Użyciu] Moc Starcia +1 za każde 4 (suma własnej [Oddech] i [Krwawienie] celu) (maks. 4)  
[Przy Użyciu] Zadaje +11% obrażeń za każde 4 [Oddech] (maks. 44%)  
[Przy Użyciu] Zadaje +11% obrażeń za każdy 1 zużyty [Strzała - Shi] (maks. 44%)  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 1  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 3: [Przy Trafieniu] Nakłada 2 [Krwawienie]

#### Umiejętność 3 (×1): Lśniący Łuk [弓閃]

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Cięcie |          4 |         +2 |      4 |           +3 |    1 |
|          4 | Żądza  | Cięcie |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* [Przy Użyciu] Moc Monet +1 za każde 4 (suma własnej [Oddech] i [Krwawienie] celu) (maks. 2)  
[Przy Użyciu] Zadaje +11% obrażeń za każde 4 [Oddech] (maks. 44%)  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 1: [Trafienie Krytyczne] Zyskuje +1 Licznika [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Trafienie Krytyczne] Zwiększa Licznik [Krwawienie] celu o 1  
Moneta 3: [Przy Trafieniu] Nakłada 4 [Krwawienie]  
Moneta 4: [Trafienie Krytyczne] Nakłada w następnej turze 1 [Spadek Poziomu Obrony] (1 raz na turę)

*Od ulepszenia 4:* [Przy Użyciu] Moc Monet +1 za każde 4 (suma własnej [Oddech] i [Krwawienie] celu) (maks. 2)  
[Przy Użyciu] Zadaje +11% obrażeń za każde 4 [Oddech] (maks. 44%)  
[Przy Użyciu] Zadaje +11% obrażeń za każdy 1 zużyty [Strzała - Shi] (maks. 44%)  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 1: [Trafienie Krytyczne] Zyskuje +1 Licznika [Oddech]  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Trafienie Krytyczne] Zwiększa Licznik [Krwawienie] celu o 1  
Moneta 3: [Przy Trafieniu] Nakłada 4 [Krwawienie]  
Moneta 4: [Trafienie Krytyczne] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)

#### Umiejętność 4 (×0): Błysk Łuku [閃弓]

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Kłucie |          4 |         +4 |      1 |           +5 |    1 |

*Od ulepszenia 3:* [Niestarciowy]  
Zewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności  
Zadaje +24% obrażeń za każdy 1 [Namierzenie Celu] (maks. 72%)  
Zadaje +24% obrażeń przy trafieniu krytycznym za każdy 1 [Namierzenie Celu] (maks. 72%)  
- Przy 4 [Namierzenie Celu] zamiast dwóch powyższych efektów zadaje +444% obrażeń przy trafieniu krytycznym  
[Przy Użyciu] Przy 4+ [Oddech] Moc Bazowa +2  
[Przy Użyciu] Moc Monet +2 za każdy 1 [Namierzenie Celu] (maks. 4)  
[Przy Użyciu] Zyskuje 5 [Oddech] za każdy 1 [Namierzenie Celu]  
[Koniec Ataku] Traci ([Namierzenie Celu] x 5) [Oddech]  
[Koniec Ataku] Usuwa [Postawa Snajperska] i [Namierzenie Celu]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Wbita Strzała]; przy pomyślnym nałożeniu traci 1 [Strzała - Shi]  
Moneta 1: [Przy Zabiciu] Zyskuje w następnej turze 1 [Kres Życia]

*Od ulepszenia 4:* [Niestarciowy]  
Zewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności  
Zadaje +48% obrażeń za każdy 1 [Namierzenie Celu] (maks. 144%)  
Zadaje +48% obrażeń przy trafieniu krytycznym za każdy 1 [Namierzenie Celu] (maks. 144%)  
- Przy 4 [Namierzenie Celu] zamiast dwóch powyższych efektów zadaje +444% obrażeń przy trafieniu krytycznym  
[Przy Użyciu] Moc Bazowa +2 za każde 4 [Oddech] (maks. 10)  
[Przy Użyciu] Moc Monet +4 za każdy 1 [Namierzenie Celu] (maks. 10)  
[Przy Użyciu] Zyskuje 5 [Oddech] za każdy 1 [Namierzenie Celu]  
[Koniec Ataku] Traci (([Namierzenie Celu] - 1) x 5) [Oddech]  
[Koniec Ataku] Usuwa [Postawa Snajperska] i [Namierzenie Celu]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Wbita Strzała]; przy pomyślnym nałożeniu traci 1 [Strzała - Shi]  
Moneta 1: [Przy Zabiciu] Zyskuje w następnej turze 1 [Kres Życia]  
Moneta 1: [Zabójstwo Krytyczne Wroga] Zwiększa własny Licznik [Oddech] o 4

#### Obrona: Rozwinięcie Łuk-Ostrza [弓刀]

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         14 |         +4 |      1 |           +1 |    1 |
|          3 | Żądza   | obrona: blok |         14 |         +4 |      1 |           +1 |    1 |

*Od ulepszenia 3:* Jeżeli ta jednostka nie ma [Strzała - Shi], zamiast tego uruchamia „Unik”  
  
[Początek Walki] Jeżeli ma zostać użyty „Błysk Łuku”, zamiast tego używa „Uniku”  
[Początek Walki] Jeżeli ta jednostka ma [Postawa Snajperska], zyskuje Tarczę równą (36 / stos [Namierzenie Celu]) na tę turę (1 raz na turę)  
  
[Koniec Tury] Jeżeli ta jednostka ma [Postawa Snajperska] i nie użyła w tej turze Umiejętności ataku, zyskuje w następnej turze 1 [Namierzenie Celu] (1 raz na turę)  
[Koniec Tury] Jeżeli ta jednostka nie ma [Postawa Snajperska] i ma 1+ [Strzała - Shi], zyskuje w następnej turze po 1 [Postawa Snajperska] i [Namierzenie Celu] (1 raz na turę)

*Od ulepszenia 4:* Jeżeli ta jednostka nie ma [Strzała - Shi], zamiast tego uruchamia „Unik”  
  
[Początek Walki] Jeżeli ma zostać użyty „Błysk Łuku”, zamiast tego używa „Uniku”  
[Początek Walki] Jeżeli ta jednostka ma [Postawa Snajperska], zyskuje Tarczę równą (60 / stos [Namierzenie Celu]) na tę turę (1 raz na turę)  
  
[Koniec Tury] Jeżeli ta jednostka ma [Postawa Snajperska] i nie użyła w tej turze Umiejętności ataku, zyskuje w następnej turze 1 [Namierzenie Celu] (1 raz na turę)  
[Koniec Tury] Jeżeli ta jednostka nie ma [Postawa Snajperska] i ma 1+ [Strzała - Shi], zyskuje w następnej turze po 1 [Postawa Snajperska] i [Namierzenie Celu] (1 raz na turę)

#### Obrona: Unik

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | obrona: unik |          4 |        +10 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [Udany Unik] Zwiększa własny Licznik [Oddech] o 1 (2 razy na turę)

*Od ulepszenia 4:* [Udany Unik] Zwiększa własny Licznik [Oddech] o 1 (3 razy na turę)

#### Pasywka bojowa: Shi-no-Yumi

*od ulepszenia 2; posiadane 3× Żądza*

Przy 4 [Strzała - Shi]: gdy ta jednostka zyskuje Moc [Oddech] efektem podstawowej Umiejętności ataku, zwiększa Licznik [Oddech] o 1 (2 razy na spotkanie; licznik limitu resetuje się, gdy [Strzała - Shi] spadnie do 3)  
Jeżeli ta jednostka użyła Umiejętności „Błysk Łuku” przy 2+ [Namierzenie Celu], zyskuje w następnej turze 1 [Wzrost Obrażeń Cięcia]

#### Pasywka bojowa: Celowanie - Łuk

*od ulepszenia 3*

Jeżeli ta jednostka jest w stanie [Postawa Snajperska], zamienia skrajnie lewą podstawową Umiejętność ataku na „Błysk Łuku” i używa jej na początku walki.  
- Jeżeli przy uruchomieniu tego efektu [Namierzenie Celu] osiąga maksimum, a Umiejętność 3 nie ma ani w Panelu Sterowania, ani w rezerwowym slocie Umiejętności,  
umiejętność obrony w skrajnie lewym slocie jest traktowana jako Umiejętność 3 i zamieniana na „Błysk Łuku”  
  
Zależnie od użytej podstawowej Umiejętności ataku stosuje poniższe efekty (atrybut Grzechu pochodzi z użytej Umiejętności)  
- Umiejętność 1: Moc Bazowa +1, obrażenia +11%  
- Umiejętność 2: Moc Bazowa +1, Moc Monet +1, obrażenia +22%  
- Umiejętność 3: Moc Bazowa +4, Moc Monet +4, obrażenia +44%  
  
※ Jeżeli na początku walki wyposażono Umiejętność E.G.O, [Postawa Snajperska] zostaje zdjęty, a „Błysk Łuku” nie jest używany.

#### Pasywka bojowa: Shi-no-Yumi

*od ulepszenia 3; posiadane 3× Żądza*

Przy 4 [Strzała - Shi]: gdy ta jednostka zyskuje Moc [Oddech] efektem podstawowej Umiejętności ataku, zwiększa Licznik [Oddech] o 1 (2 razy na spotkanie; licznik limitu resetuje się, gdy [Strzała - Shi] spadnie do 3)  
Jeżeli ta jednostka użyła Umiejętności „Błysk Łuku” przy 2+ [Namierzenie Celu], zyskuje w następnej turze 1 [Wzrost Obrażeń Cięcia]

#### Pasywka bojowa: Celowanie - Łuk

*od ulepszenia 4*

Jeżeli ta jednostka jest w stanie [Postawa Snajperska], zamienia skrajnie lewą podstawową Umiejętność ataku na „Błysk Łuku” i używa jej na początku walki.  
- Jeżeli przy uruchomieniu tego efektu [Namierzenie Celu] osiąga maksimum, a Umiejętność 3 nie ma ani w Panelu Sterowania, ani w rezerwowym slocie Umiejętności,  
umiejętność obrony w skrajnie lewym slocie jest traktowana jako Umiejętność 3 i zamieniana na „Błysk Łuku”  
  
Zależnie od użytej podstawowej Umiejętności ataku stosuje poniższe efekty (atrybut Grzechu pochodzi z użytej Umiejętności)  
- Umiejętność 1: Moc Bazowa +1, obrażenia +11%  
- Umiejętność 2: Moc Bazowa +1, Moc Monet +1, obrażenia +22%  
- Umiejętność 3: Moc Bazowa +4, Moc Monet +4, obrażenia +44%  
  
※ Jeżeli na początku walki wyposażono Umiejętność E.G.O, [Postawa Snajperska] zostaje zdjęty, a „Błysk Łuku” nie jest używany.

#### Pasywka bojowa: Shi-no-Yumi

*od ulepszenia 4; posiadane 3× Żądza*

Przy 4 [Strzała - Shi]: gdy ta jednostka zyskuje Moc [Oddech] efektem podstawowej Umiejętności ataku, zwiększa Licznik [Oddech] o 1 (3 razy na spotkanie; licznik limitu resetuje się, gdy [Strzała - Shi] spadnie do 3)  
Jeżeli ta jednostka użyła Umiejętności „Błysk Łuku” przy 2+ [Namierzenie Celu], zyskuje w następnej turze 2 [Wzrost Obrażeń Cięcia]

#### Pasywka wsparcia: Celowanie w Punkt

*od ulepszenia 3; rezonans 4× Żądza*

Na koniec tury nakłada w następnej turze 1 [Wzrost Obrażeń Przebicia] na sojusznika, który w tej walce nałożył najwięcej Mocy [Krwawienie] na wrogów Umiejętnościami i Pasywkami (łącznie z Umiejętnościami E.G.O; przy remisie wygrywa Tożsamość wcześniejsza w kolejności przydziału; nie uruchamia się, jeżeli nikt nie nałożył Mocy [Krwawienie] w tej turze)

#### Kwestie

- **Identity Acquisition:** Rain pelts awake hearts, Alleyways puddle with steps; The rest is silence.
- **Morning Greeting:** It is an unfounded rumor that the Association operates only at night; there is no specific time during which we carry out our operations, as they are practicality-based decisions that vary for each target. We also exist in the liminal space between the first light and the early scent of dawn.
- **Afternoon Greeting:** Will you not take a moment to imbibe a cup of tea? One must never forget to take breaks, even when swamped by continuous work. By disregarding this simple fact, one may even be forced to let live a life that was not supposed to see tomorrow.
- **Evening Greeting:** The hour is late. Rest, and do not unnecessarily expose yourself to the night air. ... Faust prefers to see only one type of life at this hour: moving targets.
- **Chatter #1:** There is no single correct answer to assassinations. Anything—a sword, an arrow, or even a pebble on the ground—can be an effective tool for the task. Each branch has simply chosen different weapons that fit their environs better. And for us, it happens to be the bowblade.
- **Chatter #2:** One may wonder if the supply is far behind demand in this business... and so does Faust, to a degree. Resentment floods the City like this pouring rain, after all. ... Which is why... it cannot be helped that only a few can carry out the deed.
- **Chatter #3:** A straight shot will always strike true. If it hasn't, there can be only one explanation: an excessive, unnecessary attachment to the target. The target has no face, no history, no family or friends. Those who see them have no place in this business.
- **Post-Uptie Chat 1:** Even in the City of inequities, one thing remains fair: death. Fairness for the beggar who kneels over the wet pavement... and for the loan shark who disparages him from above. ... Both contracts completed.
- **Post-Uptie Chat 2:** Bows are not universally applicable tools, of course, and that is why it has a blade as well. An assassin equipped for both ranged and melee combat makes for a rather... formidable opponent.
- **Idle:** ... Will you listen to the rain, together?
- **Uptying:** Nock the arrow, pull, loose—it punches through the target, felling it. It is simple, manual labor with very little chance of error.
- **Deployment:** Has the target been designated?
- **Stage Entry:** Uchiokoshi.
- **Viewed in Battle 1:** Waiting for the right moment.
- **Viewed in Battle 2:** ... Target locked.
- **Commencing Attack:** Let the pelting rain bury you.
- **Enemy Stagger:** Clean shot through the lung.
- **Staggered:** Mm...
- **Enemy Killed:** Bullseye.
- **Death:** Again, fairness is simply a universal concept—even... for me.
- **Check Passed:** Elementary work for an assassin.
- **Check Failed:** ... Aimed too high.
- **Victory Cry:** Contract fulfilled. While having to resort to melee was regrettable... as always, there were no witnesses.
- **Extra Conditions Fulfilled:** The pelting raindrops shroud the falling arrows, and they will die in the downpour without knowing what killed them. This is how the eastern branch kills.
- **Defeat Wail:** Though I infused this bow with my very own blood... neither opportunity nor luck were on my side. As a failure to complete a contract results in death... this shall be my end, for I have slipped to the wrong side of the boundary of death.

### 000 Akolitka Wskazującego: 【Karteczka】 — Faust

> Czternasta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 7                                                           |
| HP                        | 57 (+2,69 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom +1                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×2 (Fatal), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 60% / 30%                                                   |
| Grzech wyróżniony         | Lenistwo                                                    |
| Przynależność             | Index_Finger                                                |
| Słowa kluczowe            | Oddech, Zatonięcie                                          |
| Data aktualizacji         | 20251231                                                    |

#### Umiejętność 1 (×3): Niezawodnie, zgodnie z Nakazem

| Ulepszenie | Grzech   | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Cięcie |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Lenistwo | Cięcie |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], zadaje +10% obrażeń  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]

*Od ulepszenia 2:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], zadaje +10% obrażeń  
Przy 6+ (suma własnej [Oddech] i [Zatonięcie] celu) Moc Monet +1  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]

*Od ulepszenia 4:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], Moc Starcia +1 i zadaje +20% obrażeń  
Moc Monet +1 za każde 6 (suma własnej [Oddech] i [Zatonięcie] celu) (maks. 2)  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 2: [Trafienie Krytyczne] Nakłada 1 [Zatonięcie]

#### Umiejętność 2 (×2): Wypełnia Nakaz i doskonali siebie.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Cięcie |          4 |         +3 |      3 |           +2 |    1 |
|          3 | Pycha  | Cięcie |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], Moc Starcia +1  
[Przy Użyciu] Zyskuje 3 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]

*Od ulepszenia 2:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], Moc Starcia +1  
Przy 6+ (suma własnej [Oddech] i [Zatonięcie] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 3 [Oddech] i zwiększa własny Licznik [Oddech] o 1  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]

*Od ulepszenia 4:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], Moc Końcowa +1  
Moc Monet +1 za każde 6 (suma własnej [Oddech] i [Zatonięcie] celu) (maks. 2)  
[Przy Użyciu] Zyskuje 3 [Oddech] i zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Trafienie Krytyczne] Zwiększa Licznik [Zatonięcie] celu o 2

#### Umiejętność 3 (×1): Zgodnie z Nakazem, zostaniesz wyeliminowany.

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Posępność | Cięcie |          3 |         +4 |      3 |           +3 |    1 |
|          4 | Posępność | Cięcie |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], zadaje +20% obrażeń przy trafieniu krytycznym  
Przy 6+ (suma własnej [Oddech] i [Zatonięcie] celu) Moc Monet +1  
[Początek Walki] Przy 6+ [Łaska Nakazu] wszystkie Monety tej Umiejętności zmieniają się w [Moneta Niezniszczalna]  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 3  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: Zadaje +2.5% obrażeń za każdy 1 [Łaska Nakazu] (maks. 20%)  
- Przy 9 [Łaska Nakazu] zamiast tego zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Trafienie Krytyczne] Zwiększa Licznik [Zatonięcie] celu o 2

*Od ulepszenia 4:* Jeżeli ta Umiejętność ma wyryte [Znak Nakazu], Moc Końcowa +1 i zadaje +30% obrażeń przy trafieniu krytycznym  
Moc Monet +1 za każde 6 (suma własnej [Oddech] i [Zatonięcie] celu) (maks. 2)  
[Początek Walki] Przy 6+ [Łaska Nakazu] wszystkie Monety tej Umiejętności zmieniają się w [Moneta Niezniszczalna] i zadaje +30% obrażeń  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 3  
- Zyskuje Oddech równy ([Łaska Nakazu]/3) (zaokrąglone w dół)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: Zadaje +5% obrażeń za każdy 1 [Łaska Nakazu] (maks. 40%)  
- Przy 9 [Łaska Nakazu] zamiast tego zadaje +60% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Trafienie Krytyczne] Zwiększa Licznik [Zatonięcie] celu o 3

#### Obrona: Tkanina utkana z zesłanego Nakazu

| Ulepszenie | Grzech    | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | obrona: kontra |          3 |         +2 |      3 |           +2 |    1 |
|          4 | Posępność | obrona: kontra |          3 |         +3 |      3 |           +2 |    1 |

*Od ulepszenia 1:* Moc Końcowa +1 za każde 3 [Łaska Nakazu] (maks. 3)  
[Początek Walki] Zyskuje Tarczę równą 10% Maks. HP (1 raz na turę)  
- Za każde 5 [Karma] wartość Tarczy uzyskiwanej tym efektem maleje o 1%; przy 50+ [Karma] nie zyskuje Tarczy  
[Przy Użyciu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]

*Od ulepszenia 4:* Moc Końcowa +1 i zadaje +10% obrażeń za każde 3 [Łaska Nakazu] (maks. odpowiednio 3 i 30%)  
[Początek Walki] Zyskuje Tarczę równą 15% Maks. HP (1 raz na turę)  
- Za każde 5 [Karma] wartość Tarczy uzyskiwanej tym efektem maleje o 1.5%; przy 50+ [Karma] nie zyskuje Tarczy  
[Przy Użyciu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Zatonięcie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Zatonięcie]

#### Pasywka bojowa: Nakaz przekazany Karteczką

*od ulepszenia 1*

Na początku tury  
- Zyskuje [Nakaz [Kartka] I] / [Nakaz [Kartka] II] / [Nakaz [Kartka] III] / [Nakaz [Kartka] IV] zależnie od własnej wartości [Łaska Nakazu]  
- Nakłada [Cel Nakazu] na 1 losowego wroga (w walce skupionej: na część ciała)  
- Nakłada [Znak Nakazu] na własne podstawowe Umiejętności ataku w Panelu Sterowania (1 na slot, maks. 2 Umiejętności)  
· Przy 6+ [Łaska Nakazu] efekt nakłada najpierw na Umiejętność 3  
- Jeżeli ta jednostka jest Ogłuszona, Niezdolna do działania, w Panice lub w Korozji E.G.O, żaden z powyższych efektów ani warunek wykonania [Nakaz] nie działa

#### Pasywka bojowa: Wola Nakazu

*od ulepszenia 1*

Na koniec tury: jeżeli [Nakaz] został wykonany w tej turze, odzyskuje 4 Poczytalności i zyskuje 1 [Łaska Nakazu] (1 raz na turę)  
- Jeżeli przy wykonywaniu [Nakaz] główny cel ma [Cel Nakazu], zamiast tego odzyskuje 8 Poczytalności i zyskuje 3 [Łaska Nakazu]  
  
Na koniec tury: jeżeli [Nakaz] nie został wykonany w tej turze, zyskuje 5 [Karma]  
- Przy 9 [Łaska Nakazu] nie zyskuje [Karma]  
- Jeżeli ta jednostka próbowała wykonać [Nakaz] na początku walki, ale nie mogła namierzyć celu podczas walki, nie zyskuje [Karma]

#### Pasywka bojowa: Nakaz przekazany Karteczką

*od ulepszenia 2*

Na początku tury  
- Zyskuje [Nakaz [Kartka] I] / [Nakaz [Kartka] II] / [Nakaz [Kartka] III] / [Nakaz [Kartka] IV] zależnie od własnej wartości [Łaska Nakazu]  
- Nakłada [Cel Nakazu] na 1 losowego wroga (w walce skupionej: na część ciała)  
- Nakłada [Znak Nakazu] na własne podstawowe Umiejętności ataku w Panelu Sterowania (1 na slot, maks. 2 Umiejętności)  
· Przy 6+ [Łaska Nakazu] efekt nakłada najpierw na Umiejętność 3  
- Jeżeli ta jednostka jest Ogłuszona, Niezdolna do działania, w Panice lub w Korozji E.G.O, żaden z powyższych efektów ani warunek wykonania [Nakaz] nie działa

#### Pasywka bojowa: Wola Nakazu

*od ulepszenia 2*

Na koniec tury: jeżeli [Nakaz] został wykonany w tej turze, odzyskuje 4 Poczytalności i zyskuje 1 [Łaska Nakazu] (1 raz na turę)  
- Jeżeli przy wykonywaniu [Nakaz] główny cel ma [Cel Nakazu], zamiast tego odzyskuje 8 Poczytalności i zyskuje 3 [Łaska Nakazu]  
  
Na koniec tury: jeżeli [Nakaz] nie został wykonany w tej turze, zyskuje 5 [Karma]  
- Przy 9 [Łaska Nakazu] nie zyskuje [Karma]  
- Jeżeli ta jednostka próbowała wykonać [Nakaz] na początku walki, ale nie mogła namierzyć celu podczas walki, nie zyskuje [Karma]

#### Pasywka bojowa: Ostrze Akolity

*od ulepszenia 2; posiadane 1× Lenistwo, posiadane 1× Pycha, posiadane 1× Posępność*

Zadaje +2% obrażeń Umiejętnościami z [Znak Nakazu] za każdy 1 [Łaska Nakazu] (maks. 16%)  
- Przy 9 [Łaska Nakazu] zamiast tego zadaje +20% obrażeń podstawowymi Umiejętnościami  
  
Przy trafieniu podstawową Umiejętnością w cel z [Cel Nakazu], zyskuje 1 [Oddech] i nakłada 1 [Zatonięcie] (1 raz na turę)  
- Za każde 3 [Łaska Nakazu] liczba uruchomień tego efektu na turę rośnie o 1 (maks. 2)  
  
Przy 9 [Łaska Nakazu] podstawowe Umiejętności nakładają +1 więcej Mocy Zatonięcia, a ta jednostka zyskuje +1 więcej Mocy Oddechu

#### Pasywka wsparcia: Tak, jak Nakaz nakazuje...

*od ulepszenia 3; posiadane 1× Lenistwo, posiadane 1× Pycha, posiadane 1× Posępność*

Efekt stosuje do Tożsamości pierwszej w kolejności przydziału  
- Najpierw Tożsamości frakcji Wskazującego  
  
Na początku walki, jeżeli inni sojusznicy namierzyli ten sam slot wroga, co skrajnie lewa Umiejętność tej jednostki w Panelu Sterowania, ta Umiejętność zadaje +5% obrażeń za każdego 1 sojusznika namierzającego ten slot, nie licząc tej jednostki  
(maks. 15%; działa, gdy ta jednostka i sojusznicy namierzają główny cel podstawową Umiejętnością ataku)

#### Kwestie

- **Identity Acquisition:** You may brood over curiosities regarding the Will of the Prescript, yet inquiry bears no weight in its execution. What is absolute can only be obeyed.
- **Morning Greeting:** I drink a liter of juice in the morning and warm up before I set out to escort the Proxies. This Prescript has no defined time limit—thus, I remain in perpetual execution of it.
- **Afternoon Greeting:** ... The appointed time has lapsed. The Prescript's deadline was until noon. ... It's unfortunate, but you were the fifth person who smiled at me among all the people I encountered yesterday, so I must proceed by severing your left earlobe. Resistance is ill-advised. Such cases, with prevailing regularity, result in new Prescripts that dictate deeper and broader excision of the flesh.
- **Evening Greeting:** "Split the nocturnal lights of the Backstreets thrice before 6 months pass." ... I have yet to determine the exact method of carrying out this Prescript. And so each night, I pace the neon-lit alleys in nocturnal contemplation.
- **Chatter #1:** It is said that the Will of the Prescript and the Will of the City are one and the same. Whether this is true or not, the Prescript's intent is not to be fathomed—just as my following the Prescript does not require Faust's understanding. The true value of things lies solely in undertaking and fulfilling the Prescript.
- **Chatter #2:** At times, the Prescript feels reminiscent of Faust. Through its Messengers, the Prescript busily wends its way through the City, as Faust once did in pursuit of curiosity. But such moments must now be set aside. Follow where the Prescript leads, and the Will of the City shall reveal itself in due course.
- **Chatter #3:** Faust seems blind to the reality that the accumulation and interpretation of knowledge is ultimately futile within the City. Perhaps that nescience explains their attempts to seize my access rights... that failed at every turn. That, too, must be the Will of the Prescript.
- **Post-Uptie Chat 1:** The index finger points; as does the Prescript that indicates the path we must tread. That is what gives the Index its name. None of this is mere happenstance. Even should individuals unite in defiance of the Prescript, such resistance falls within the Will of the Prescript.
- **Post-Uptie Chat 2:** To be appointed a Proxy or a Messenger holds no particular appeal for Faust; such things are not for Faust to decide. Cutting these people down, receiving the Prescript, assuming any role within the Index—it is all the same.
- **Idle:** Hmm. Refraction of light through a polygonal mirror... This cannot be an appropriate interpretation of the Prescript to "split the lights."
- **Uptying:** A new Prescript has arrived: "Behead seven dwellers of the Backstreets who resist when a blade touches their throat." The tally aligns—seven of you stand before me. I shall commence.
- **Deployment:** The Prescript is received.
- **Stage Entry:** To where the Prescript points.
- **Viewed in Battle:** To converse is not a violation of the Prescript.
- **Commencing Attack:** As the Prescript commands—my blade strikes.
- **Enemy Stagger:** Please hold. You are to be cleaved five more times.
- **Staggered:** Nngh...
- **Enemy Killed:** It is done.
- **Death:** Did the Prescript... point toward death...? If not... whose will... could this be...?
- **Check Passed:** It is concluded.
- **Check Failed:** The Prescript has demanded this failure.
- **Victory Cry:** Those who have neglected to carry out the Prescript are being taken care of in order. The process is slightly delayed as I perform the following task: "Shear 663 strands of hair and enclose them in an envelope, to be deposited at Ticket Gate 3." There is no cause for concern.
- **Extra Conditions Fulfilled:** The Prescript has been carried out. Its clarity made its execution simple and convenient. Though there were many who resisted, their defiance proved meaningless, as you have witnessed.
- **Defeat Wail:** ... I do not deem this a failure of the Prescript—it is I who have failed, and that, too, is part of the Prescript's design. I am but a speck that will fade from the City, and soon, another Proselyte or Proxy will arrive to take my place. Such must be the direction to which the Prescript points.

### 000 Dom Pajęczyn: Uczeń Serdecznego — Faust

> Piętnasta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 7                                                           |
| HP                        | 92 (+3,19 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–4 / 3–5 / 3–6 / 3–6                                       |
| Poziom obrony             | poziom +2                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 50% / 30%                                                   |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Ring_Finger_Physical, Ring_Finger, Spider_House             |
| Słowa kluczowe            | Krwawienie, Ładowanie                                       |
| Data aktualizacji         | 20260402                                                    |

#### Umiejętność 1 (×3): Ubój - Żebra

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Cięcie |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Obżar. | Cięcie |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* Umiejętność wyłącznie dla [Iron Maiden]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 [Wzrost Poziomu Obrony] (1 raz na turę)

*Od ulepszenia 2:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 [Wzrost Poziomu Obrony] (1 raz na turę)

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 3)  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 [Wzrost Poziomu Obrony] (1 raz na turę)

#### Umiejętność 2 (×2): Fascia jest głodna.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Cięcie |          3 |         +4 |      3 |           +2 |    1 |
|          3 | Zawiść | Cięcie |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zwiększa własny Licznik [Materiał Biologiczny] o 4

*Od ulepszenia 2:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 2)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zwiększa własny Licznik [Materiał Biologiczny] o 4

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Moc Starcia +1 za każdy 1 rodzaj negatywnych efektów na celu (maks. 2)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 4)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zwiększa własny Licznik [Materiał Biologiczny] o 4

#### Umiejętność 3 (×1): Tłumione Ciało

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Cięcie |          3 |         +3 |      4 |           +3 |    1 |
|          4 | Żądza  | Cięcie |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 2)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa do 20 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Końcowa +2  
- Zadaje +3% obrażeń za każdy 1 zużytego Licznika [Materiał Biologiczny]  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze 1 [Spadek Obrażeń] (1 raz na turę)  
Moneta 4: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
Moneta 4: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Iron Maiden]  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 3)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa do 20 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Końcowa +2  
- Zadaje +3% obrażeń za każdy 1 zużytego Licznika [Materiał Biologiczny]  
Moneta 1: [Przy Trafieniu] Nakłada 4 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze 1 [Spadek Obrażeń] (1 raz na turę)  
Moneta 4: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
Moneta 4: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]

#### Umiejętność 4 (×0): Ubój - Żebra

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Cięcie |          2 |         +4 |      2 |           +3 |    1 |
|          3 | Obżar. | Cięcie |          3 |         +4 |      2 |           +3 |    1 |

*Od ulepszenia 1:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 [Wzrost Poziomu Obrony] (1 raz na turę)

*Od ulepszenia 2:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 20%)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 [Wzrost Poziomu Obrony] (1 raz na turę)

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Zadaje +10% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 3)  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 2 [Spadek Poziomu Obrony] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 2 [Wzrost Poziomu Obrony] (1 raz na turę)

#### Umiejętność 5 (×0): Czas na Posiłek dla Fascii.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Cięcie |          3 |         +4 |      3 |           +4 |    1 |
|          3 | Zawiść | Cięcie |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 1:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 [Pośpiech] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zwiększa własny Licznik [Materiał Biologiczny] o 4

*Od ulepszenia 2:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 20%)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 2)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 [Pośpiech] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zwiększa własny Licznik [Materiał Biologiczny] o 4

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Zadaje +10% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na celu (maks. 4)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 [Pośpiech] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zwiększa własny Licznik [Materiał Biologiczny] o 4

#### Umiejętność 6 (×0): Wyzwolenie Tłumionego Ciała

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Cięcie |          3 |         +3 |      4 |           +5 |    1 |
|          4 | Żądza  | Cięcie |          4 |         +3 |      4 |           +5 |    1 |

*Od ulepszenia 3:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
[Przy Użyciu] Zadaje +30% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: liczy się części ciała)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na głównym celu (maks. 2)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa do 20 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Końcowa +2  
- Zadaje +1% obrażeń za każdy 1 zużytego Licznika [Materiał Biologiczny]  
- Przy 3+/5+ [Materiał Biologiczny] Waga ataku +1/+2  
- Wszystkie Monety tej Umiejętności stają się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 [Pośpiech] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze 1 [Spadek Obrażeń] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zyskuje w następnej turze 1 [Wzrost Obrażeń Cięcia] (1 raz na turę)  
Moneta 4: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
Moneta 4: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
[Przy Użyciu] Zadaje +30% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: liczy się części ciała)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] na głównym celu (maks. 3)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa do 20 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Końcowa +2  
- Zadaje +1% obrażeń za każdy 1 zużytego Licznika [Materiał Biologiczny]  
- Przy 3+/5+ [Materiał Biologiczny] Waga ataku +1/+2  
- Wszystkie Monety tej Umiejętności stają się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada 4 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada w następnej turze 1 [Spętanie] (1 raz na turę)  
Moneta 2: [Przy Trafieniu] Zyskuje w następnej turze 1 [Pośpiech] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Nakłada w następnej turze 1 [Spadek Obrażeń] (1 raz na turę)  
Moneta 3: [Przy Trafieniu] Zyskuje w następnej turze 1 [Wzrost Obrażeń Cięcia] (1 raz na turę)  
Moneta 4: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
Moneta 4: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]

#### Obrona: Przygotowanie Wystawy

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |          3 |        +10 |      1 |           +5 |    1 |
|          4 | Żądza   | obrona: blok |          4 |        +10 |      1 |           +5 |    1 |

*Od ulepszenia 1:* [Blok Zdatny do Starcia]  
Umiejętność wyłącznie dla [Iron Maiden]  
[Wygrane Starcie] Zwiększa Licznik [Krwawienie] atakującego o 1 (maks. 2 razy na turę)  
[Wygrane Starcie] Zadaje atakującemu obrażenia Kłucia równe jego Mocy [Krwawienie] (maks. 20 obrażeń)  
Moneta 1: [Moneta Niezniszczalna]

*Od ulepszenia 4:* [Blok Zdatny do Starcia]  
Umiejętność wyłącznie dla [Iron Maiden]  
[Wygrane Starcie] Zwiększa Licznik [Krwawienie] atakującego o 2 (maks. 2 razy na turę)  
[Wygrane Starcie] Zadaje atakującemu obrażenia Kłucia równe (Moc [Krwawienie] atakującego x 2) (maks. 30 obrażeń)  
Moneta 1: [Moneta Niezniszczalna]

#### Obrona: Wystawa się rozpoczęła

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           +2 |    1 |
|          4 | Żądza   | obrona: unik |          4 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
[Początek Walki] Zyskuje 1 [Obrona Wsparcia] (1 raz na turę)  
[Udany Unik] Nakłada w następnej turze 1 [Spętanie] na atakującego (1 raz na turę)

*Od ulepszenia 4:* Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
[Początek Walki] Zyskuje 1 [Obrona Wsparcia] (1 raz na turę)  
[Udany Unik] Nakłada w następnej turze 1 [Spętanie] na atakującego (1 raz na turę)  
[Udany Unik] Zyskuje w następnej turze 1 [Pośpiech] (1 raz na turę)

#### Obrona: Wandalizmy się nie toleruje.

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | obrona: kontra |          3 |         +4 |      2 |           +2 |    1 |
|          4 | Żądza  | obrona: kontra |          4 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Kontra Starciowa]  
Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Umiejętność wyłącznie dla [Obrona Wsparcia]  
Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 20%)  
[Przy Użyciu] Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]

*Od ulepszenia 4:* [Kontra Starciowa]  
Umiejętność wyłącznie dla [Uwolnienie Jaźni - Stan Przepływu]  
Umiejętność wyłącznie dla [Obrona Wsparcia]  
Zadaje +10% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)  
[Przy Użyciu] Moc Monet +1 za każde 6 [Krwawienie] na celu (maks. 2)  
[Przy Użyciu] Przy 10+ Liczniku [Materiał Biologiczny] zużywa 5 Licznika [Materiał Biologiczny] i stosuje poniższe efekty:  
- Moc Starcia +1  
- Ostatnia Moneta tej Umiejętności staje się [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]

#### Pasywka bojowa: Fascia, Moje Ukochane Dzieło

*od ulepszenia 1*

Przy pierwszym pojawieniu się na polu zyskuje (liczba sojuszników frakcji Serdecznego na polu x 2) Licznika [Materiał Biologiczny] (maks. 10)  
  
Na koniec Umiejętności: jeżeli ta Umiejętność zadała obrażenia HP lub Tarczy, zwiększa własny Licznik [Materiał Biologiczny] o 5  
- Jeżeli cel zginął, zwiększa Licznik dodatkowo o 3  
  
Za każde łączne zużycie 10 własnego Licznika [Materiał Biologiczny] podczas walki zyskuje 1 [Materiał Biologiczny]  
- Jeżeli wskutek tego efektu Moc [Materiał Biologiczny] osiągnie 2 lub więcej, zyskuje [Dzieło: Fascia]  
  
Podstawowe Umiejętności ataku i Kontrę zdolną do Starcia traktuje się jak Umiejętności zyskujące Licznik [Ładowanie]

#### Pasywka bojowa: Zbroja dla Ochrony i Tłumienia

*od ulepszenia 1*

Przy pierwszym pojawieniu się na polu zyskuje [Iron Maiden]  
  
Na koniec tury: jeżeli ta jednostka ma [Dzieło: Fascia], traci [Iron Maiden] i zyskuje [Uwolnienie Jaźni - Stan Przepływu] (1 raz na spotkanie)  
- Jeżeli jest Ogłuszona, dochodzi do siebie z Ogłuszenia (nie licząc wymuszonego Ogłuszenia)

#### Pasywka bojowa: Fascia, Moje Ukochane Dzieło

*od ulepszenia 2*

Przy pierwszym pojawieniu się na polu zyskuje (liczba sojuszników frakcji Serdecznego na polu x 2) Licznika [Materiał Biologiczny] (maks. 10)  
  
Na koniec Umiejętności: jeżeli ta Umiejętność zadała obrażenia HP lub Tarczy, zwiększa własny Licznik [Materiał Biologiczny] o 5  
- Jeżeli cel zginął, zwiększa Licznik dodatkowo o 3  
  
Za każde łączne zużycie 10 własnego Licznika [Materiał Biologiczny] podczas walki zyskuje 1 [Materiał Biologiczny]  
- Jeżeli wskutek tego efektu Moc [Materiał Biologiczny] osiągnie 2 lub więcej, zyskuje [Dzieło: Fascia]  
  
Podstawowe Umiejętności ataku i Kontrę zdolną do Starcia traktuje się jak Umiejętności zyskujące Licznik [Ładowanie]

#### Pasywka bojowa: Zbroja dla Ochrony i Tłumienia

*od ulepszenia 2*

Przy pierwszym pojawieniu się na polu zyskuje [Iron Maiden]  
  
Na koniec tury: jeżeli ta jednostka ma [Dzieło: Fascia], traci [Iron Maiden] i zyskuje [Uwolnienie Jaźni - Stan Przepływu] (1 raz na spotkanie)  
- Jeżeli jest Ogłuszona, dochodzi do siebie z Ogłuszenia (nie licząc wymuszonego Ogłuszenia)

#### Pasywka bojowa: Natchnienie z Krytyki

*od ulepszenia 2; posiadane 4× Żądza*

Efekty [Melodia Drgającego Ciała] zwiększające Szybkość, Moc Starcia i obrażenia działają 2 razy silniej  
  
Przy trafieniu: jeżeli ta Umiejętność ataku nałożyła negatywny efekt, odzyskuje 4 Poczytalności na koniec ataku (2 razy na turę)

#### Pasywka bojowa: Fascia, Moje Ukochane Dzieło

*od ulepszenia 4*

Przy pierwszym pojawieniu się na polu zyskuje (liczba sojuszników frakcji Serdecznego na polu x 2) Licznika [Materiał Biologiczny] (maks. 10)  
  
Na koniec Umiejętności: jeżeli ta Umiejętność zadała obrażenia HP lub Tarczy, zwiększa własny Licznik [Materiał Biologiczny] o 5  
- Jeżeli cel zginął, zwiększa Licznik dodatkowo o 3  
  
Za każde łączne zużycie 10 własnego Licznika [Materiał Biologiczny] podczas walki zyskuje 1 [Materiał Biologiczny]  
- Jeżeli wskutek tego efektu Moc [Materiał Biologiczny] osiągnie 2 lub więcej, zyskuje [Dzieło: Fascia]  
  
Podstawowe Umiejętności ataku i Kontrę zdolną do Starcia traktuje się jak Umiejętności zyskujące Licznik [Ładowanie]

#### Pasywka bojowa: Zbroja dla Ochrony i Tłumienia

*od ulepszenia 4*

Przy pierwszym pojawieniu się na polu zyskuje [Iron Maiden]  
  
Na koniec tury: jeżeli ta jednostka ma [Dzieło: Fascia], traci [Iron Maiden] i zyskuje [Uwolnienie Jaźni - Stan Przepływu] (1 raz na spotkanie)  
- Jeżeli jest Ogłuszona, dochodzi do siebie z Ogłuszenia (nie licząc wymuszonego Ogłuszenia)

#### Pasywka bojowa: Natchnienie z Krytyki

*od ulepszenia 4; posiadane 4× Żądza*

Efekty [Melodia Drgającego Ciała] zwiększające Szybkość, Moc Starcia i obrażenia działają 2 razy silniej  
  
Przy trafieniu: jeżeli ta Umiejętność ataku nałożyła negatywny efekt, odzyskuje 4 Poczytalności na koniec ataku (2 razy na turę)  
- Jeżeli Poczytalność tej jednostki jest pełna, odzyskując Poczytalność tym efektem zyskuje w następnej turze 1 [Wzrost Obrażeń Cięcia] (1 raz na turę)

#### Pasywka wsparcia: Żelazna Dziewica - Kolce

*od ulepszenia 3; posiadane 1× Żądza, posiadane 2× Zawiść*

Gdy w tej turze sojusznik z wyposażoną Umiejętnością obrony zostanie trafiony, nakłada 4 [Krwawienie] na atakującego (2 razy na turę)  
- Jeżeli atakujący ma już [Krwawienie], zamiast tego zwiększa jego Licznik [Krwawienie] o 2

#### Kwestie

- **Identity Acquisition:** Have you woken up, Fascia? Faust has been waiting—there is a new friend Faust wants to introduce to Fascia. How is it? Such a splendid piece of corpus our new friend has, yes?
- **Morning Greeting:** Fascia is a sleepyhead. Please refrain from visiting Faust in the early hours.
- **Afternoon Greeting:** The critique session has been canceled—now there is some time left. How would you propose we spend this leisure in a more creative manner, Fascia? Hmm... Yes. *chuckle* Faust is in agreement.
- **Evening Greeting:** When sunlight fades and luminous intensity attenuates, new ideas, untethered from prior renderings, begin to articulate themselves. It is a time when bright-red organs desaturate into earthen brown, and their three-dimensionality, released from chiaroscuro, returns to a state of unmediated neutrality... Ah, of course...! The assignment was never about amending the work, but light itself!
- **Chatter #1:** A pleasure. Would you be willing to spend some time getting to know each other? Surely it won't be too hard to become friends—even for those who aren't geniuses like Faust. It's as simple as sharing the things we love, our hobbies, our dreams... yes, such things should be enough. Ah, but preferably, something that excludes Fixer stories and the Prescripts. There has been an overload of such tales lately.
- **Chatter #2:** If it's not too much trouble, could you gift a piece of your brain to Faust? Friends are supposed to exchange gifts, aren't they? Faust wishes to give Fascia a fresh taste of an unfamiliar brain, you see. She's already had a few slices of Faust's own, and carving away more would risk losing Faust... Please, your generosity would be most welcome.
- **Chatter #3:** Aesthetics concerns itself entirely with the visible, yet this self-evident familiarity often invites neglect that overlooks the inherent significance of what is seen. It is because of this that Faust forged this panoply. Not merely to provide a veil behind which the bashful Fascia might reside, but also to stage a dual aesthetic: the weighted inertia of the armored body against the beautiful liberation of the repressed flesh upon shedding the encasement. The thrill of the gap that arises when the unseen becomes seen... does it resonate with you?
- **Post-Uptie Chat 1:** Now then, shall we deepen our friendship one step further? Let us examine the artistry of anatomization together as you critique the assembly that forms my body. A candid, impartial assessment would be most welcome—Faust is eager to identify areas for further refinement.
- **Post-Uptie Chat 2:** Let the cadence of your heartbeat surge, Fascia. As your blood quickens, so too will hunger. Today is a day that calls for a feast. Please eat up—there is no need to hold yourself back. Grow corpulent with each piece of corpus consumed. Such excess will elevate you into a more beautiful composition.
- **Idle:** ... Fascia needs rest. Perhaps Faust does, too.
- **Uptying:** Focus your ears and listen. Listen to Fascia's heartbeat... this pulsating sound of life!
- **Deployment:** This quivering... Are you excited too, Fascia?
- **Stage Entry:** A critique salon! Exhilarating prospect.
- **Viewed in Battle:** Please observe from a distance—it's for viewing only.
- **Commencing Attack:** A spark of inspiration.
- **Enemy Stagger:** These blood vessels are sufficiently thick. Not bad at all.
- **Staggered:** Are you afraid, Fascia?
- **Enemy Killed:** Only now have we become friends.
- **Death:** Fa... scia...
- **Check Passed:** Che bello. Exquisite.
- **Check Failed:** Non è bello. Devoid of beauty.
- **Victory Cry:** The artwork is only a borderline pass at best; however, the critique salon this time around yielded neither improvement nor insight for further refinement. Fascia is anxious to reach completion... Perhaps it will be more fruitful to return and work on practice pieces among embalmed corpora.
- **Extra Conditions Fulfilled:** At long last, Faust has completed the masterpiece that even the Maestro will have no choice but to approve. *chuckle* Oh, Fascia also agrees with Faust.
- **Defeat Wail:** Faust only wished to be friends with you... Is this where the curtains are drawn upon Faust's art? Ah... Sorry, Fascia... Faust was in too much of a hurry...

### 000 Biuro Świtu Fikser — Faust

> Szesnasta Tożsamość Faust

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | wydarzenie 9109                                             |
| HP                        | 66 (+2,88 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–7 / 4–7                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×2 (Fatal), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 55% / 25%                                                   |
| Grzech wyróżniony         | Pycha                                                       |
| Przynależność             | Dawn                                                        |
| Słowa kluczowe            | Podpalenie, Wstrząs                                         |
| Data aktualizacji         | 20260709                                                    |

#### Umiejętność 1 (×3): Błysk Świtu

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Cięcie |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Pycha  | Cięcie |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Moc Starcia +1 za każde 10 [Trumna Ognistych Motyli] (maks. 2)  
[Przy Użyciu] Przy 20+ [Trumna Ognistych Motyli] używa ostatniej monety ponownie  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]

*Od ulepszenia 2:* [Przy Użyciu] Moc Końcowa +1 za każde 4 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Moc Starcia +1 za każde 10 [Trumna Ognistych Motyli] (maks. 2)  
[Przy Użyciu] Przy 20+ [Trumna Ognistych Motyli] używa ostatniej monety ponownie  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]

*Od ulepszenia 4:* [Przy Użyciu] Moc Końcowa +1 za każde 4 (suma [Podpalenie] i [Wstrząs] celu) (maks. 3)  
[Przy Użyciu] Zyskuje 4 [Trumna Ognistych Motyli]  
[Przy Użyciu] Moc Starcia +1 za każde 10 [Trumna Ognistych Motyli] (maks. 3)  
[Przy Użyciu] Przy 20+ [Trumna Ognistych Motyli] używa ostatniej monety ponownie  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Podpalenie] i zwiększa Licznik [Podpalenie] o 1  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]

#### Umiejętność 2 (×2): Cięcie Motyla

| Ulepszenie | Grzech   | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Cięcie |          4 |         +5 |      2 |           +3 |    1 |
|          3 | Lenistwo | Cięcie |          4 |         +6 |      2 |           +3 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Za każde 10 [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Moc Starcia +1 (maks. 2)  
- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1 (1 raz na Umiejętność)

*Od ulepszenia 2:* [Przy Użyciu] Moc Końcowa +1 za każde 4 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Zyskuje 3 [Trumna Ognistych Motyli]  
[Przy Użyciu] Za każde 10 [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Moc Starcia +1 (maks. 2)  
- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)  
Moneta 1: [Przy Trafieniu] Przy 10+ [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Zwiększa Licznik [Podpalenie] o 1  
- Zwiększa Licznik [Wstrząs] o 1  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1 (1 raz na Umiejętność)

*Od ulepszenia 4:* [Przy Użyciu] Moc Końcowa +1 za każde 4 (suma [Podpalenie] i [Wstrząs] celu) (maks. 3)  
[Przy Użyciu] Zyskuje 6 [Trumna Ognistych Motyli]  
[Przy Użyciu] Za każde 10 [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Moc Starcia +1 (maks. 3)  
- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)  
Moneta 1: [Przy Trafieniu] Za każde 10 [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Zwiększa Licznik [Podpalenie] o 1 (maks. 2)  
- Zwiększa Licznik [Wstrząs] o 1 (maks. 2)  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1 (1 raz na Umiejętność)

#### Umiejętność 3 (×1): Wystrzał

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |          3 |         +4 |      3 |           +4 |    1 |
|          4 | Gniew  | Cięcie |          5 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 3:* [Przed Użyciem] Przy 30 [Trumna Ognistych Motyli] zamiast tego uruchamia „Wystrzał - Południe” (1 raz na turę)  
[Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Wstrząs]), Moc Monet +1  
[Przy Użyciu] Zyskuje 5 [Trumna Ognistych Motyli]  
[Przy Użyciu] Za każde 10 [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Moc Starcia +1 (maks. 2)  
- Zwiększa Licznik [Podpalenie] celu o 1 (maks. 2)  
- Zwiększa Licznik [Wstrząs] celu o 1 (maks. 2)  
- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Wstrząs]  
Moneta 2: [Przy Trafieniu] Wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar]  
Moneta 3: [Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1 (2 razy na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Podpalenie]

*Od ulepszenia 4:* [Przed Użyciem] Przy 30 [Trumna Ognistych Motyli] zamiast tego uruchamia „Wystrzał - Południe” (1 raz na turę)  
[Przy Użyciu] Moc Monet +1 za każde 6 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Zyskuje 8 [Trumna Ognistych Motyli]  
[Przy Użyciu] Za każde 10 [Trumna Ognistych Motyli] zyskuje następujące efekty:  
- Moc Starcia +1 (maks. 3)  
- Zwiększa Licznik [Podpalenie] celu o 1 (maks. 3)  
- Zwiększa Licznik [Wstrząs] celu o 1 (maks. 3)  
- Używa ostatniej monety ponownie (maks. 2 razy na Umiejętność)  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Wstrząs]  
Moneta 2: [Przy Trafieniu] Wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar]  
Moneta 3: [Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1 (3 razy na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Podpalenie]

#### Umiejętność 4 (×0): Łączenie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          2 | Obżar. | Cięcie |          3 |         +3 |      2 |           +1 |    1 |
|          3 | Obżar. | Cięcie |          4 |         +3 |      2 |           +1 |    1 |

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Wstrząs] o 1 (2 razy na turę)  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] o 1 (2 razy na turę)

*Od ulepszenia 3:* [Przy Użyciu] Zadaje +1% obrażeń za każdy 1 [Trumna Ognistych Motyli] (maks. 30%)  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Wstrząs] o 1 (2 razy na turę)  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] o 1 (2 razy na turę)

*Od ulepszenia 4:* [Przy Użyciu] Zyskuje następujące efekty zależnie od stosu [Trumna Ognistych Motyli]:  
- Zadaje +2% obrażeń za każdy 1 stos (maks. 60%)  
- Moc Końcowa +1 za każde 10 stosów (maks. 3)  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Wstrząs] o 1 (2 razy na turę)  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] o 1 (2 razy na turę)

#### Umiejętność 5 (×0): Wystrzał - Południe

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |          3 |         +4 |      3 |           +5 |    3 |
|          4 | Gniew  | Cięcie |          5 |         +4 |      3 |           +5 |    3 |

*Od ulepszenia 3:* [Ostrzał Bez Celowania]  
Przy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:  
- Nakłada 1 [Podpalenie] lub 1 [Wstrząs]  
- Jeżeli cel nie ma [Wstrząs - Żar], wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar] (1 raz na cel)  
[Przy Użyciu]  
- Moc Starcia +3  
- Jeżeli główny cel ma 6+ (suma [Podpalenie] i [Wstrząs]), Moc Monet +1 i Moc Starcia +2  
- Zwiększa Licznik [Podpalenie] wszystkich celów o 2  
- Zwiększa Licznik [Wstrząs] wszystkich celów o 2  
[Koniec Ataku]  
- Nakłada w następnej turze 1 [Spadek Mocy] na wszystkich trafionych celów (1 raz na turę)  
- Zyskuje 1 [Wyczucie Walki]  
- Zyskuje 1 [Przegrzana Trumna]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: Używa tej monety ponownie (maks. 2 razy)  
Moneta 3: [Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik Wstrząsu celu o 1 (2 razy na Umiejętność)

*Od ulepszenia 4:* [Ostrzał Bez Celowania]  
Zadaje +(suma Mocy [Podpalenie] tej jednostki i celu)% obrażeń (maks. 20%; liczone osobno dla każdego celu)  
Przy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:  
- Nakłada 1 [Podpalenie] lub 1 [Wstrząs]  
- Jeżeli cel nie ma [Wstrząs - Żar], wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar] (1 raz na cel)  
[Przy Użyciu]  
- Moc Starcia +3  
- Moc Monet +1 i Moc Starcia +2 za każde 6 (suma [Podpalenie] i [Wstrząs] głównego celu) (maks. odpowiednio 2 i 4)  
- Zwiększa Licznik [Podpalenie] wszystkich celów o 3  
- Zwiększa Licznik [Wstrząs] wszystkich celów o 3  
[Koniec Ataku]  
- Nakłada w następnej turze 1 [Spadek Mocy] na wszystkich trafionych celów (1 raz na turę)  
- Zyskuje 1 [Wyczucie Walki]  
- Zyskuje 1 [Przegrzana Trumna]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: Używa tej monety ponownie (maks. 2 razy)  
Moneta 3: Jeżeli ta jednostka ma [Wyczucie Walki], zadaje +(Moc [Podpalenie] celu / 2)% obrażeń (maks. 20%)  
Moneta 3: [Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik Wstrząsu celu o 1 (3 razy na Umiejętność)

#### Obrona: Napiętnowanie

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | obrona: kontra |          3 |         +4 |      2 |           +1 |    1 |
|          4 | Gniew  | obrona: kontra |          5 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Kontra Starciowa]  
[Przy Użyciu] Przy 5+ [Podpalenie] Moc Monet +1  
[Przy Użyciu] Traci 5 [Podpalenie] (1 raz na turę)  
[Wygrane Starcie] Traci 3 [Podpalenie] (1 raz na turę)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie] (2 razy na turę)  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs] (2 razy na turę)

*Od ulepszenia 3:* [Kontra Starciowa]  
[Przed Użyciem] Przy 30 [Trumna Ognistych Motyli] zamiast tego uruchamia „Rozczłonkowanie w Południe” (1 raz na turę)  
- Jeżeli ta jednostka ma [Przegrzana Trumna], ten efekt nie uruchamia się  
[Przy Użyciu] Przy 5+ [Podpalenie] Moc Monet +1  
[Przy Użyciu] Traci 5 [Podpalenie] (1 raz na turę)  
[Wygrane Starcie] Traci 3 [Podpalenie] (1 raz na turę)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie] (2 razy na turę)  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs] (2 razy na turę)

*Od ulepszenia 4:* [Kontra Starciowa]  
[Początek Walki] Zyskuje 6 [Trumna Ognistych Motyli] (1 raz na spotkanie)  
[Przed Użyciem] Przy 30 [Trumna Ognistych Motyli] zamiast tego uruchamia „Rozczłonkowanie w Południe” (1 raz na turę)  
- Jeżeli ta jednostka ma [Przegrzana Trumna], ten efekt nie uruchamia się  
[Przy Użyciu] Moc Monet +1 za każde 5 [Podpalenie] (maks. 2)  
[Przy Użyciu] Traci 5 [Podpalenie] (1 raz na turę)  
[Wygrane Starcie] Traci 3 [Podpalenie] (1 raz na turę)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie] (2 razy na turę)  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs] (2 razy na turę)

#### Obrona: Rozczłonkowanie w Południe

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | obrona: kontra |          3 |         +4 |      3 |           +5 |    3 |
|          4 | Gniew  | obrona: kontra |          5 |         +4 |      3 |           +5 |    3 |

*Od ulepszenia 3:* [Ostrzał Bez Celowania]  
Zadaje +(brakujące % HP tej jednostki / 2)% obrażeń (maks. 25%)  
Przy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:  
- Nakłada 1 [Podpalenie] lub 1 [Wstrząs]  
- Jeżeli cel nie ma [Wstrząs - Żar], wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar] (1 raz na cel)  
[Przy Użyciu]  
- Moc Starcia +3  
- Jeżeli główny cel ma 6+ (suma [Podpalenie] i [Wstrząs]), Moc Monet +1 i Moc Starcia +2  
- Zwiększa Licznik [Podpalenie] wszystkich celów o 2  
- Zwiększa Licznik [Wstrząs] wszystkich celów o 2  
[Koniec Ataku]  
- Zużywa do 30 [Podpalenie] i odzyskuje HP równe (5 + zużyte [Podpalenie])% Maks. HP (maks. 35%)  
- Zużywa całe [Trumna Ognistych Motyli]  
- Zyskuje 3 [Wyczucie Walki]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: Używa tej monety ponownie (maks. 2 razy)  
Moneta 3: [Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik Wstrząsu celu o 1 (2 razy na Umiejętność)

*Od ulepszenia 4:* [Ostrzał Bez Celowania]  
Zadaje +(brakujące % HP tej jednostki)% obrażeń (maks. 50%)  
Zadaje +(Moc [Podpalenie] celu)% obrażeń (maks. 20%; liczone osobno dla każdego celu)  
Przy każdym trafieniu tej Umiejętności stosuje na celu następujące efekty:  
- Nakłada 1 [Podpalenie] lub 1 [Wstrząs]  
- Jeżeli cel nie ma [Wstrząs - Żar], wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar] (1 raz na cel)  
[Przy Użyciu]  
- Moc Starcia +3  
- Moc Monet +1 i Moc Starcia +2 za każde 6 (suma [Podpalenie] i [Wstrząs] głównego celu) (maks. odpowiednio 2 i 4)  
- Zwiększa Licznik [Podpalenie] wszystkich celów o 3  
- Zwiększa Licznik [Wstrząs] wszystkich celów o 3  
[Koniec Ataku]  
- Zużywa do 30 [Podpalenie] i odzyskuje HP równe (20 + zużyte [Podpalenie])% Maks. HP (maks. 50%)  
- Zużywa całe [Trumna Ognistych Motyli]  
- Zyskuje 3 [Wyczucie Walki]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: Używa tej monety ponownie (maks. 2 razy)  
Moneta 3: Jeżeli ta jednostka ma [Wyczucie Walki], zadaje +(Moc [Podpalenie] celu)% obrażeń (maks. 20%)  
Moneta 3: [Przy Trafieniu] [Wybuch Wstrząsu]. Zmniejsza Licznik Wstrząsu celu o 1 (3 razy na Umiejętność)

#### Pasywka bojowa: Płaszcz Termiczny

*od ulepszenia 1*

Przy pierwszym pojawieniu się na polu zyskuje 0 [Trumna Ognistych Motyli]  
  
Nie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Podpalenie]  
Otrzymuje -50% obrażeń od efektów [Podpalenie] (zaokrąglone w dół)  
- Przy HP poniżej 50% efekt się wzmacnia: otrzymuje -75% obrażeń od efektów [Podpalenie] (zaokrąglone w dół)

#### Pasywka bojowa: Seonbae

*od ulepszenia 1*

Jeżeli na polu jest Fikser Biura Świtu Sinclair, uruchamia następujące efekty:  
- Fikser Biura Świtu Sinclair zyskuje [Samo Południe]  
- Na początku tury: jeżeli Fikserka Biura Świtu Faust jest pokonana, [Samo Południe] Fiksera Biura Świtu Sinclaira zmienia się w [Samotne Południe]

#### Pasywka bojowa: Płaszcz Termiczny

*od ulepszenia 2*

Przy pierwszym pojawieniu się na polu zyskuje 0 [Trumna Ognistych Motyli]  
  
Nie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Podpalenie]  
Otrzymuje -50% obrażeń od efektów [Podpalenie] (zaokrąglone w dół)  
- Przy HP poniżej 50% efekt się wzmacnia: otrzymuje -75% obrażeń od efektów [Podpalenie] (zaokrąglone w dół)

#### Pasywka bojowa: Seonbae

*od ulepszenia 2*

Jeżeli na polu jest Fikser Biura Świtu Sinclair, uruchamia następujące efekty:  
- Fikser Biura Świtu Sinclair zyskuje [Samo Południe]  
- Na początku tury: jeżeli Fikserka Biura Świtu Faust jest pokonana, [Samo Południe] Fiksera Biura Świtu Sinclaira zmienia się w [Samotne Południe]

#### Pasywka bojowa: Feuerfalter [Pracownia Stigmy]

*od ulepszenia 2; posiadane 3× Gniew*

Jeżeli inne Tożsamości Biura Świtu spełnią poniższe warunki, Fikserka Biura Świtu Faust używa Umiejętności „Łączenie” na namierzonym wrogu (1 raz na turę na Tożsamość)  
- Na koniec ataku podstawowej Umiejętności: jeżeli trafiony wróg został Ogłuszony, używa „Łączenia” na tym wrogu  
(Nie uruchamia się, jeżeli wróg był już Ogłuszony przed atakiem tej Umiejętności)  
- Na koniec ataku Umiejętności „Ostrze Rozcinające Świt” i „Biały Świt” Szefa Biura Świtu Gregora albo Umiejętności „Napiętnowanie” i „Płonące Uderzenie” Fiksera Biura Świtu Sinclaira używa „Łączenia” na trafionym wrogu (najpierw Ogłuszeni)  
  
Jeżeli na polu jest Fikser Biura Świtu Sinclair, gdy ponownie użyte monety podstawowych Umiejętności Fikserki Biura Świtu Faust trafią, zadaje dodatkowe obrażenia Gniewu równe Mocy [Podpalenie] namierzonego wroga (maks. 10, maks. 20 na turę)  
- Liczy się jako uruchomienie [Podpalenie]

#### Pasywka bojowa: Płaszcz Termiczny

*od ulepszenia 3*

Przy pierwszym pojawieniu się na polu zyskuje 0 [Trumna Ognistych Motyli]  
  
Nie może zostać Ogłuszona ani spaść poniżej 1 HP od obrażeń [Podpalenie]  
Otrzymuje -50% obrażeń od efektów [Podpalenie] (zaokrąglone w dół)  
- Przy HP poniżej 50% efekt się wzmacnia: otrzymuje -75% obrażeń od efektów [Podpalenie] (zaokrąglone w dół)

#### Pasywka bojowa: Seonbae

*od ulepszenia 3*

Jeżeli na polu jest Fikser Biura Świtu Sinclair, uruchamia następujące efekty:  
- Fikser Biura Świtu Sinclair zyskuje [Samo Południe]  
- Na początku tury: jeżeli Fikserka Biura Świtu Faust jest pokonana, [Samo Południe] Fiksera Biura Świtu Sinclaira zmienia się w [Samotne Południe]

#### Pasywka bojowa: Feuerfalter [Pracownia Stigmy]

*od ulepszenia 3; posiadane 3× Gniew*

Na początku walki, gdy ta jednostka ma [Wyczucie Walki], zyskuje (stos x 3) [Trumna Ognistych Motyli]  
  
Jeżeli inne Tożsamości Biura Świtu spełnią poniższe warunki, Fikserka Biura Świtu Faust używa Umiejętności „Łączenie” na namierzonym wrogu (1 raz na turę na Tożsamość)  
- Na koniec ataku podstawowej Umiejętności: jeżeli trafiony wróg został Ogłuszony, używa „Łączenia” na tym wrogu  
(Nie uruchamia się, jeżeli wróg był już Ogłuszony przed atakiem tej Umiejętności)  
- Na koniec ataku Umiejętności „Ostrze Rozcinające Świt” i „Biały Świt” Szefa Biura Świtu Gregora albo Umiejętności „Napiętnowanie” i „Płonące Uderzenie” Fiksera Biura Świtu Sinclaira używa „Łączenia” na trafionym wrogu (najpierw Ogłuszeni)  
  
Jeżeli na polu jest Fikser Biura Świtu Sinclair, gdy ponownie użyte monety podstawowych Umiejętności Fikserki Biura Świtu Faust trafią, zadaje dodatkowe obrażenia Gniewu równe Mocy [Podpalenie] namierzonego wroga (maks. 10, maks. 20 na turę)  
- Liczy się jako uruchomienie [Podpalenie]

#### Pasywka wsparcia: Samotny Fixer

*od ulepszenia 3; posiadane 3× Gniew, posiadane 3× Żądza*

Na początku walki, jeżeli na polu jest tylko 1 Tożsamość — łącznie z rezerwą —  
ta Tożsamość zyskuje 3 [Wzrost Poziomu Ataku] i 3 [Wzrost Poziomu Obrony]

#### Kwestie

- **Identity Acquisition:** Black needles. Symbols of an irregular, atypical pattern. Faust has surmised correctly. The architect of this incident... appears to have been that individual.
- **Morning Greeting:** Warm tea in the early morning is, from a medical perspective, recommended for the regulation of circadian rhythm and the stimulation of gastrointestinal tract reflexes.... *cough* However, may I recommend broadening your options to other forms of beverages, Herr Gregor? ... If you are opposed to the idea, then please consider giving the room some much-needed ventilation, at the very least.
- **Afternoon Greeting:** A surprise explosion of such nature in the very center of downtown at high noon... This incident hardly seems to reflect the ordinary reality of urban violence. Balloons, swollen far past their elastic tension would allow, popped synchronically and without warning—except, they were actually people swelling up and scattering thousands of needles in every direction. If the phenomenon is to be put into words... perhaps that would be the closest approximation.
- **Evening Greeting:** You haven't clocked out yet, Herr Gregor? Not yet... You staying to clear some backlog, too? No. Though Faust has concluded all assigned tasks, she will not be calling it a day just yet—please feel free to share any remaining workload with Faust. Thanks, really... But what's got you sticking around this late when you don't have to? There is something... I would personally like to investigate. Lemme guess... Brainstem Focus Resonator, is it? You're trying to trace where it came from. ... Correct.
- **Chatter #1:** It strains the realm of believability... But this observation leads one to conjecture that "magic"—or what could crudely be described as such, at least—does exist... No, Faust would rather dignify the hypothesis that it involves something of Outskirts origin that has not yet been cataloged by Faust... for lack of a better explanation. Perhaps this matter calls Faust to confer with the other Fausts.
- **Chatter #2:** While it is undeniably problematic that embedded needles can dissolve the structural body of buildings... More hazardous would be the chain reaction they cause: civilians and passersby explode simply by being struck by those needles.
- **Chatter #3:** Entrusting this sort of rote drudgery to Faust is no less than a tremendous waste of her operational capacity. Sinclair, you certainly possess a remarkable ability in brewing ssanghwa-cha, but I trust that you did not register as a Fixer to be this Office's resident Grade 5 Tea-brewer. Please take over this task instead. You sure you're not just shirking your duties and offloading your work on him? ... Please stop with the absurd jokes, Herr Gregor. It does not contribute in any shape or form to Sinclair's progress as a Fixer.
- **Post-Uptie Chat 1:** Yesterday's Promise... Faust knows that you are the mastermind behind not only the Thousand Needles, but also the series of incidents that have occurred throughout the City of late. All that's left is to gather a threadable clue on the rumored "contract" of which you are the point of origin...
- **Post-Uptie Chat 2:** If Faust is to arrive at the truth she seeks... Settling this Office's monthly rent should be the priority. With our Office located in a Nest, the rent payable is astronomical... But Herr Gregor said that resolving this contract on the "Library" will keep us afloat for at least 3 months. Let us deal with these Librarians first and slowly pace the investigation into the true nature of the demon.
- **Idle:** There is sufficient time to spare. I will finalize our expense calculations in the meantime. Sinclair? Milk tea for me, please.
- **Uptying:** Let us cut the conversation short, shall we? Herr Gregor, Sinclair... Let us proceed at once.
- **Deployment:** Has this request been assigned exclusively to our Office?
- **Stage Entry:** Faust shall launch a preemptive strike before the opponents begin their offensive.
- **Viewed in Battle:** This place offers many hazards. There is no need to overdo it—please stay behind and focus on providing support.
- **Commencing Attack:** Ejecting blades.
- **Enemy Stagger:** Not a bad attempt.
- **Staggered:** Hngh...
- **Enemy Killed:** Suffice it to say that you could not capitalize on your skills.
- **Death:** The fault lies... in Faust's—no, my ineptitude...
- **Check Passed:** At times, it feels as though Faust is the only working member who sustains this Office.
- **Check Failed:** Every responsibility has been mine thus far. I would like to entrust this one to you.
- **Victory Cry:** This should have been a trivial enough request... for an Office of our level to handle. *sigh* In any case, we did manage to accomplish at least some part of the objective. Limited satisfaction would be permissible.
- **Extra Conditions Fulfilled:** This ended smoothly, without overstrenuous complications initially anticipated... An outcome that may be attributed to your competence that Faust had possibly underestimated. Let us utilize this opportunity and retrieve the Book of Zwei Association per the request.
- **Defeat Wail:** The house party... will have to be canceled, Herr Gregor. Sinclair... I wonder if he has made his escape unharmed...
