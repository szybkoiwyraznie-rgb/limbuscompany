# Limbus Company — Sinclair: Identity

*Profil postaci: dane liczbowe z tabel gry, opisy z plików lokalizacji.*

## Zakres i zasady odczytu

- Teksty w wersji `pl`; wpisy bez przekładu pozostają w oryginale (angielskim); liczby z `StaticData` (wartości bazowe, bez E.G.O i bonusów).
- **Ulepszenie** = Uptie (gaksung) 1–4; tabela umiejętności pokazuje tylko wiersze, w których coś się zmienia. Moc ataku = moc bazowa + moc monety za każdą wyrzuconą reszkę/orła wg reguł gry.
- **Poziom ataku/obrony** to korekta względem poziomu postaci.
- **Odporności**: mnożnik obrażeń danego typu (×2 = Fatal, ×0,5 = Endured).
- Elementy bez opisu w danych są oznaczone „—”, nie zgadywane.

## Akta więźnia

> Nawet biorąc poprawkę na burzliwy okres dorastania, Grzesznik wyróżnia się tym,
> że zagadnięty, wyjątkowo łatwo się wzdryga albo krzywi. Nie jest też obyty
> z walką, więc na początku może mu być ciężko nawet patrzeć na wnętrzności.
> Wśród Grzeszników są osoby skłonne do przemocy, dlatego zalecamy,
> by Kierownik stosował wobec niego raczej marchewkę niż kij.
> Bywa, że ma w oczach żądzę mordu, której sam nie jest świadom, co jednak
> oznacza potencjał w dziedzinie działalności naszej firmy; przy odpowiednich bodźcach liczymy, że wyrośnie na znakomitego fachowca.

## Katalog Identity

| Rzadkość | Identity                                         |           Sezon | Grzech wyróżniony | Słowa kluczowe         |
| -------: | ------------------------------------------------ | --------------: | ----------------- | ---------------------- |
|        0 | LCB Grzesznik                                    |               0 | Pycha             | Rozdarcie              |
|      000 | Ród Ostrza Salsu                                 |               0 | Obżar.            | Oddech, Krwawienie     |
|       00 | Południowe Stowarzyszenie Zwei Sekcja 6          |               0 | Posępność         | Wstrząs                |
|       00 | Los Mariachis Jefe                               |               1 | Lenistwo          | Oddech, Zatonięcie     |
|      000 | Ten, Który Zaciska Uścisk                        |               1 | Gniew             | Krwawienie, Podpalenie |
|       00 | Lobotomy E.G.O:: Czerwony Arkusz                 |               2 | Żądza             | Rozdarcie              |
|       00 | Centrum Łodzi Trzonowca Fikser                   |               2 | Posępność         | Wstrząs                |
|      000 | Południowe Stowarzyszenie Cinq Sekcja 4 Dyrektor |               0 | Obżar.            | Oddech                 |
|      000 | Biuro Świtu Fikser                               | wydarzenie 9103 | Posępność         | Podpalenie             |
|       00 | Zachodnie Stowarzyszenie Zwei Sekcja 3           |               5 | Żądza             | Wstrząs                |
|      000 | Północne Stowarzyszenie Devyat' Sekcja 3         |               0 | Obżar.            | Rozdarcie              |
|      000 | Środkowego Młodsza Siostra                       |               0 | Obżar.            | Krwawienie             |
|      000 | Kciuk Wschodni Soldato II                        |               6 | Gniew             | Podpalenie, Wstrząs    |
|      000 | Wataha Heishou - Gałąź You                       |               6 | Żądza             | Rozdarcie, Podpalenie  |
|      000 | Dom Pajęczyn: Uczeń Małego Palca                 |               7 | Posępność         | Oddech, Krwawienie     |
|      000 | Haute Couture:: Szkarłatny Bóg Le Rouge          |               8 | Obżar.            | Ładowanie, Krwawienie  |
|      000 | Biuro Klin Fikser                                | wydarzenie 9110 | Obżar.            | Oddech, Wstrząs        |

## Profile

### 0 LCB Grzesznik — Sinclair

> Pierwsza Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 0                                                           |
| Sezon                     | 0                                                           |
| HP                        | 60 (+2,07 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom −4                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×2 (Fatal), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Pycha                                                       |
| Przynależność             | Limbus_Company, Limbus_Company_Lcb                          |
| Słowa kluczowe            | Rozdarcie                                                   |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Cięcie w Dół

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Cięcie |          2 |         +7 |      1 |           +3 |    1 |
|          3 | Pycha  | Cięcie |          3 |         +7 |      1 |           +3 |    1 |
|          4 | Pycha  | Cięcie |          4 |         +7 |      1 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Nakłada 2 Rozdarcia

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Nakłada 2 Rozdarcia

#### Umiejętność 2 (×2): Kombinacja Topora

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | Cięcie |          3 |         +2 |      3 |           +3 |    1 |
|          3 | Gniew  | Cięcie |          4 |         +2 |      3 |           +3 |    1 |

*Od ulepszenia 1:* [Wygrane Starcie] Zadaje +10% obrażeń

*Od ulepszenia 2:* [Wygrane Starcie] Zadaje +30% obrażeń

#### Umiejętność 3 (×1): Rozdzierające Cięcie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Zawiść | Cięcie |          5 |         +2 |      3 |           +3 |    1 |
|          4 | Zawiść | Cięcie |          5 |         +3 |      3 |           +3 |    1 |

*Od ulepszenia 3:* [Wygrane Starcie] Zyskuje 1 Wzrost Mocy Ataku

*Od ulepszenia 4:* [Wygrane Starcie] Zyskuje 1 Wzrost Mocy Ataku  
Moneta 1: [Trafienie Awersem] Nakłada 1 Rozdarcia  
Moneta 2: [Trafienie Awersem] Nakłada 1 Rozdarcia  
Moneta 3: [Trafienie Awersem] Nakłada 1 Rozdarcia

#### Obrona: Kontra

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | obrona: kontra |          7 |         +4 |      1 |           +3 |    1 |

#### Pasywka bojowa: Postanowienie

*od ulepszenia 1; posiadane 3× Pycha*

Jeżeli w tej turze ginie sojusznik, zyskuje 1 Wzrost Mocy Ataku w następnej turze

#### Pasywka wsparcia: Uraza

*od ulepszenia 3; posiadane 3× Pycha*

1 Sojusznik z najniższą Poczytalnością: zyskuje 1 Wzrost Mocy Ataku w turze po śmierci innego sojusznika

#### Kwestie

- **Identity Acquisition:** I’m Sinclair… Emil Sinclair. Oh, my number is, uhm… eleven.
- **Morning Greeting:** Good morning! Did you have a good… Oh, you can sleep, right, Manager…?
- **Afternoon Greeting:** I feel the most comfortable at this time of the day. Have a nice afternoon, Manager.
- **Evening Greeting:** How was your day? As for me… I couldn’t really focus on my tasks, I think.
- **Chatter #1:** I don’t think I could ever have imagined doing this… Oh, it’s not that I dislike my job or anything, it’s just… something that randomly occurred to me.
- **Chatter #2:** You really are amazing, Manager… I’m still struggling to adjust, and you’re leading us like a pro despite your memory loss.
- **Chatter #3:** Look, Rodya gave me some snacks. I’m gonna save some for later. Hehe.
- **Chatter #4:** Say, Dante… Do you… really feel nothing having that for your head? Is the world… still normal to you?
- **Chatter #5:** So, if you don’t remember your past, I guess that means you don’t have regrets either, right, Dante? It might be rude of me to say this, but… I envy that. You get to completely focus on the present.
- **Idle:** Um, Manager…? Where are you? Are you busy?
- **Deployment:** Umm… You want me? Mmh… I will do my best…
- **Stage Entry:** I guess this is for the best, right…?
- **Viewed in Battle:** Did I do something wrong…?
- **Commencing Attack:** I’ll try…!
- **Enemy Stagger:** I did it, right…?
- **Staggered:** Ngh…!
- **Enemy Killed:** I did it!
- **Ally Death:** Will that happen to me too…?
- **Check Passed:** Thank goodness I made it…
- **Check Failed:** It’s all my fault…
- **Victory Cry:** Umm… Did we make it? I’m so relieved.
- **Extra Conditions Fulfilled:** I don’t really think it’s thanks to me. I appreciate the compliment, though. I was reminded of my mother for a moment.
- **Defeat Wail:** Sorry. I should have done better… I still have a lot of room for improvement.

### 000 Ród Ostrza Salsu — Sinclair

> Druga Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 0                                                           |
| HP                        | 86 (+2,96 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 1–4 / 1–5 / 2–5 / 2–5                                       |
| Poziom obrony             | poziom +2                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×2 (Fatal), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 60% / 30%                                                   |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Blade_Lineage                                               |
| Słowa kluczowe            | Oddech, Krwawienie                                          |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Ciącie, potem Pchnięcie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Kłucie |          4 |         +1 |      2 |           +2 |    1 |
|          3 | Obżar. | Kłucie |          5 |         +1 |      2 |           +2 |    1 |
|          4 | Obżar. | Kłucie |          5 |         +2 |      2 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 2: [Trafienie Awersem] Zwiększa własny Licznik [Oddech] o 1

*Od ulepszenia 2:* Moneta 2: [Przy Trafieniu] Zyskuje +2 Licznika Oddechu

*Od ulepszenia 4:* Jeżeli ma 3+ Licznika [Oddech], Moc Monet +1  
Moneta 2: [Przy Trafieniu] Zyskuje +2 Licznika Oddechu

#### Umiejętność 2 (×2): Seria Cięć

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | Cięcie |          5 |         +1 |      3 |           +2 |    1 |
|          3 | Gniew  | Cięcie |          6 |         +1 |      3 |           +2 |    1 |
|          4 | Gniew  | Cięcie |          6 |         +2 |      3 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Zyskuje 2 Oddechu  
Moneta 2: [Trafienie Awersem] Zyskuje 1 Oddechu  
Moneta 3: [Trafienie Awersem] Zyskuje 1 Oddechu

*Od ulepszenia 2:* [Przegrane Starcie] Zyskuje 2 Wzrostu Mocy Ataku w następnej turze  
Moneta 1: [Przy Trafieniu] Zyskuje 2 Oddechu  
Moneta 2: [Przy Trafieniu] Zyskuje 1 Oddechu  
Moneta 3: [Przy Trafieniu] Zyskuje 1 Oddechu

*Od ulepszenia 4:* [Przegrane Starcie] Zyskuje 2 Wzrostu Mocy Ataku w następnej turze  
[Wygrane Starcie] Nie zużywa Licznika [Oddech] przy trafieniach krytycznych zadanych tą Umiejętnością  
Moneta 1: [Przy Trafieniu] Zyskuje 2 Oddechu  
Moneta 2: [Przy Trafieniu] Zyskuje 1 Oddechu  
Moneta 3: [Przy Trafieniu] Zyskuje 1 Oddechu

#### Umiejętność 3 (×1): Łamanie Kości

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Pycha  | Cięcie |          8 |        +14 |      1 |           +2 |    1 |
|          4 | Pycha  | Cięcie |          8 |        +18 |      1 |           +2 |    1 |

*Od ulepszenia 3:* Moneta 1: [Przy Trafieniu] Nakłada 5 Paraliżu  
Moneta 1: [Przy Trafieniu] Nakłada 3 Krwawienia

*Od ulepszenia 4:* Przy 10+ Licznika [Oddech] +150% obrażeń krytycznych  
Moneta 1: [Przy Trafieniu] Nakłada 5 Paraliżu  
Moneta 1: [Przy Trafieniu] Nakłada 3 Krwawienia

#### Obrona: Kontra - Nowe Wyskoki

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | obrona: kontra |          9 |         +6 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zyskuje 1 Wzrost Obrażeń w następnej turze

*Od ulepszenia 4:* [Przy Użyciu] Zyskuje 1 Wzrost Obrażeń w następnej turze  
[Przy Użyciu] Zwiększa Licznik [Oddech] o 3

#### Pasywka bojowa: Zabójca

*od ulepszenia 2; rezonans 2× Pycha*

Ostatnia moneta ostatniej Umiejętności w łańcuchu zadaje +20% obrażeń

#### Pasywka bojowa: Slayer

*od ulepszenia 4; rezonans 2× Pycha*

The last Coin on the last skill in the chain deals +20% damage.  
Whenever an ally other than this unit gains Poise Count, this unit gains +1 Poise Count at a 50% chance.

#### Pasywka wsparcia: Krwawe Dłonie

*od ulepszenia 3; rezonans 3× Pycha*

1 Sojusznik z najniższą Szybkością zyskuje Moc Końcowa +1 swojej ostatniej Umiejętności

#### Kwestie

- **Identity Acquisition:** Tell me… What do I need to cut?
- **Morning Greeting:** There’s nothing refreshing like swinging my sword through the morning air.
- **Afternoon Greeting:** Manager, who do you usually have your lunch with? Um… As for me, I tend to eat alone. I’m more comfortable that way.
- **Evening Greeting:** It’s dark out. The sky would be brighter if I could cut out the moon. …I’m kidding, of course.
- **Chatter #1:** Are you satisfied with what you’re doing, Manager? Is your job fulfilling?
- **Chatter #2:** Oh, hi, Manager! I was just standing guard. You’ll join me…? Mmm… Sure! Go ahead.
- **Chatter #3:** I envy Ms. Rodya. She never thinks too deeply and has no problem following her heart. It’s something I could never do.
- **Post-Uptie Chat 1:** I was taught that you should show no hesitation when you wield a sword. But I can’t help but keep questioning myself… asking if it’s really okay to take others’ lives so easily…
- **Post-Uptie Chat 2:** However, when I actually cut someone down… I would get such a rush. I guess that’s my nature.
- **Idle:** Huh? Manager, where did you go? Is this some kind of prank?
- **Uptying:** I’ll become a sharper blade.
- **Deployment:** Without hesitation.
- **Stage Entry:** This will help me hone my edge, right…?
- **Viewed in Battle:** Please trust my blade…
- **Commencing Attack:** I won’t hesitate…!
- **Enemy Stagger:** I’ll be able to cut them down next, right?
- **Staggered:** Hng…!
- **Enemy Killed:** I slew them!
- **Ally Death:** Don’t joke with me like this…
- **Check Passed:** You have no hesitation!
- **Check Failed:** This was inconceivable…
- **Victory Cry:** I was a little nervous… but it’s nice to see that it ended well.
- **Extra Conditions Fulfilled:** To slay others… was more delightful than I thought.
- **Defeat Wail:** I let my reluctance hold me back when it mattered most. It’s my fault.

### 00 Południowe Stowarzyszenie Zwei Sekcja 6 — Sinclair

> Trzecia Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 0                                                           |
| HP                        | 88 (+3,05 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 1–3 / 2–3 / 2–4 / 2–4                                       |
| Poziom obrony             | poziom +3                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×1 (Normal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 55% / 20%                                                   |
| Grzech wyróżniony         | Posępność                                                   |
| Przynależność             | Zwei                                                        |
| Słowa kluczowe            | Wstrząs                                                     |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Obuch

| Ulepszenie | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Obuch |          3 |         +6 |      1 |           −2 |    1 |
|          3 | Posępność | Obuch |          4 |         +6 |      1 |           −2 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Nakłada 2 [Wstrząs]

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Nakłada 2 [Wstrząs]

*Od ulepszenia 4:* [Przegrane Starcie] Zyskuje 2 Ochrony  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Wstrząs]

#### Umiejętność 2 (×2): Powstrzymanie

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | Obuch |          5 |         +1 |      2 |           −2 |    1 |
|          3 | Gniew  | Obuch |          6 |         +1 |      2 |           −2 |    1 |
|          4 | Gniew  | Obuch |          6 |         +2 |      2 |           −2 |    1 |

*Od ulepszenia 1:* Moneta 2: [Trafienie Awersem] Nakłada 3 Wstrząsu  
Moneta 2: [Przy Trafieniu] Nakłada 1 Spadek Obrażeń w następnej turze

*Od ulepszenia 2:* Moneta 2: [Przy Trafieniu] Nakłada 6 [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 2 Spadek Obrażeń w następnej turze

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa w następnej turze Prowokację tego slotu Umiejętności o 4  
[Przegrane Starcie] Nakłada 6 [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 6 [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 2 Spadek Obrażeń w następnej turze

#### Umiejętność 3 (×1): Hak

| Ulepszenie | Grzech   | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lenistwo | Obuch |          7 |        +13 |      1 |           −2 |    1 |

*Od ulepszenia 3:* [Przy Użyciu] W następnej turze nakłada 1 Ochrony na Sojusznika z najniższym obecnym HP  
Moneta 1: [Przy Trafieniu] Wybuch Wstrząsu  
Moneta 1: [Przy Trafieniu] Nakłada 2 Wrażliwości na Uderzenie

*Od ulepszenia 4:* [Przy Użyciu] W następnej turze nakłada 1 Ochrony na Sojusznika z najniższym obecnym HP  
[Przy Użyciu] Zwiększa w następnej turze Prowokację tego slotu Umiejętności o 10  
Moneta 1: [Przy Trafieniu] Wybuch Wstrząsu  
Moneta 1: [Przy Trafieniu] Przy [Wybuch Wstrząsu], jeżeli cel ma 5+ [Wstrząs], zyskuje 2 Ochrony w następnej turze  
Moneta 1: [Przy Trafieniu] Nakłada 2 Wrażliwości na Uderzenie

#### Obrona: Blok

| Ulepszenie | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral   | obrona: blok |         10 |         +3 |      1 |           +5 |    1 |
|          4 | Posępność | obrona: blok |         12 |         +6 |      1 |           +5 |    1 |

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa Prowokację tego slotu Umiejętności o 4 w następnej turze

#### Pasywka bojowa: Twoja Tarcza

*od ulepszenia 2; rezonans 2× Posępność*

Na początku walki nakłada 2 Wzrost Mocy Obrony i 1 Ochrony na postacie przylegające do tej jednostki na panelu

#### Pasywka wsparcia: Upór

*od ulepszenia 3; posiadane 4× Posępność*

1 Sojusznik z najniższym obecnym HP otrzymuje -10% obrażeń

#### Kwestie

- **Identity Acquisition:** I’ll protect you with all I can, Manager! Oh, um… Don’t go too far ahead…
- **Morning Greeting:** Have you had a good night’s sleep? Sorry? Oh, you’re wondering why I’m up so early? That’s just what the Zwei are like.
- **Afternoon Greeting:** It’s lunchtime. I usually have food that’s easy to carry around. I guess I’ve grown a habit from my training days.
- **Evening Greeting:** I should stay wide awake at night. You never know when an ambush might happen.
- **Chatter #1:** Even if I can’t land a devastating blow… I can take one for you.
- **Chatter #2:** Wagh, you startled me…! Sorry, I just don’t really like being snuck up on.
- **Chatter #3:** When I first started joint training with Don Quixote, it was rather troubling… But now, I’ve gotten quite used to her antics.
- **Post-Uptie Chat 1:** In the past… I’d lost many precious people because I didn’t know what to do. That experience taught me desperation. It’s what drives me to do my best now.
- **Post-Uptie Chat 2:** I’d rather be a broken shield than a runaway. …I don’t want to suffer losing anyone else.
- **Idle:** Manager…? Please let me know in advance if you plan to go somewhere… I’m worried sick.
- **Uptying:** I’ll work even harder! I’ll be sure to not let you down.
- **Deployment:** To be an unyielding shield.
- **Stage Entry:** I’ll protect you with all my strength!
- **Viewed in Battle:** I’ll try my best to keep the others safe!
- **Commencing Attack:** This way!
- **Enemy Stagger:** Now’s our chance!
- **Staggered:** Ah!
- **Enemy Killed:** I did it!
- **Ally Death:** I couldn’t protect you…
- **Check Passed:** Thank you for having faith in me!
- **Check Failed:** I couldn’t keep harm away…
- **Victory Cry:** I think I’m on the way to becoming a proper guardian.
- **Extra Conditions Fulfilled:** I gave it my all, and I’m glad my effort paid off.
- **Defeat Wail:** I couldn’t protect the others. I thought things would be different this time…

### 00 Los Mariachis Jefe — Sinclair

> Czwarta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 1                                                           |
| HP                        | 95 (+3,26 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 1–2 / 1–2 / 2–3 / 2–3                                       |
| Poziom obrony             | poziom +3                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×1 (Normal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 50%                                                         |
| Grzech wyróżniony         | Lenistwo                                                    |
| Przynależność             | Mariachi                                                    |
| Słowa kluczowe            | Oddech, Zatonięcie                                          |
| Data aktualizacji         | 20230227                                                    |

#### Umiejętność 1 (×3): Taniec

| Ulepszenie | Grzech   | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Obuch |          3 |         +2 |      2 |           −3 |    1 |
|          3 | Lenistwo | Obuch |          4 |         +2 |      2 |           −3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Nakłada 2 Zatonięcia

*Od ulepszenia 2:* Moneta 1: [Trafienie Awersem] Nakłada 4 [Zatonięcie]

*Od ulepszenia 4:* Jeżeli cel ma 4+ [Zatonięcie], Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 4 [Zatonięcie]

#### Umiejętność 2 (×2): Danza de Pasión

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Obuch |          4 |         +1 |      3 |           −3 |    1 |
|          3 | Zawiść | Obuch |          5 |         +1 |      3 |           −3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Przy Trafieniu] Zyskuje 2 Oddechu  
Moneta 2: [Przy Trafieniu] Nakłada 1 Zatonięcia  
Moneta 3: [Przy Trafieniu] Nakłada 1 Zatonięcia

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Zyskuje 2 Oddechu  
Moneta 1: [Trafienie Awersem] Zwiększa własny Licznik [Oddech] o 1  
Moneta 2: [Przy Trafieniu] Nakłada 2 Zatonięcia  
Moneta 2: [Trafienie Awersem] Nakłada +1 Licznika Zatonięcia  
Moneta 3: [Przy Trafieniu] Nakłada 2 Zatonięcia

*Od ulepszenia 4:* Jeżeli cel ma 6+ [Zatonięcie], Moc Monet +2  
Moneta 1: [Przy Trafieniu] Zyskuje 2 Oddechu  
Moneta 1: [Przy Trafieniu] Zwiększa własny Licznik [Oddech] o 1  
Moneta 2: [Przy Trafieniu] Nakłada 2 Zatonięcia  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika Zatonięcia  
Moneta 3: [Przy Trafieniu] Nakłada 2 Zatonięcia

#### Umiejętność 3 (×1): Pañata Party

| Ulepszenie | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Posępność | Obuch |          8 |        +11 |      1 |           −3 |    1 |

*Od ulepszenia 3:* Jeżeli Poczytalność celu jest poniżej 0, zwiększa szansę trafienia krytycznego proporcjonalnie do Poczytalności celu  
Moneta 1: [Trafienie Awersem] Obniża Próg Oszołomienia o 50% zadanych obrażeń

*Od ulepszenia 4:* Jeżeli Poczytalność celu jest poniżej 0, zwiększa szansę trafienia kryt. proporcjonalnie do Poczytalności celu  
Przy 5+ Licznika [Oddech] +30% obrażeń kryt.  
Moneta 1: [Przy Trafieniu] Obniża Próg Oszołomienia o 50% zadanych obrażeń

#### Obrona: Unik

| Ulepszenie | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral   | obrona: unik |          5 |        +10 |      1 |           +5 |    1 |
|          4 | Posępność | obrona: unik |          5 |        +10 |      1 |           +5 |    1 |

*Od ulepszenia 4:* [Udany Unik] Zwiększa Licznik [Oddech] o 1

#### Pasywka bojowa: Júbilo Hedonista

*od ulepszenia 2; rezonans 3× Posępność*

Po skutecznym uniku, z szansą (Rezonans Posępności x 5)%, Obniża Próg Oszołomienia o Moc Umiejętności uniku

#### Pasywka wsparcia: Jugar con Enemigos

*od ulepszenia 3; posiadane 4× Posępność*

1 Sojusznik z najwyższą Poczytalnością zadaje +10% obrażeń wrogom z niższą Poczytalnością niż jego własna

#### Kwestie

- **Identity Acquisition:** Salutations… I’ve been told that this is… where I’ll stir with entertainment.
- **Morning Greeting:** A fresh morning. Let’s kick off today with an energetic start.
- **Afternoon Greeting:** What a lazy afternoon… When I feel drowsy, I tend to shake the instruments in my hands to whatever rhythm. Like this, and like that.
- **Evening Greeting:** The favorite hours of the dead… When do you go to sleep, Dante?
- **Chatter #1:** Oh… You wanna hear my music? Hmm… I’ll shake something out, if you insist.
- **Chatter #2:** You should keep your head empty in a fight. It’s all about the rhythm. Stay lively, but without missing a beat.
- **Chatter #3:** What do you do when your mind is disturbed, Manager? How about learning to play music with me? It’s something that helped me a lot.
- **Post-Uptie Chat 1:** I wasn’t always like this. One day, I chanced upon music and dance… They opened a window into my own psyche.
- **Post-Uptie Chat 2:** I know of a way to shake off the agony, fear, anxiety, and all else that weighs you down. Just surrender yourself to the rhythm, and it will lead you.
- **Idle:** …Did you not like my performance?
- **Uptying:** I’ll repay you with merrier music.
- **Deployment:** Let’s shake it.
- **Stage Entry:** Is this the right choice…?
- **Viewed in Battle:** What’s up, Dante…?
- **Commencing Attack:** I’ll bust your head.
- **Enemy Stagger:** I’ll take your head next.
- **Staggered:** Unk!
- **Enemy Killed:** Too easy.
- **Ally Death:** Who’s up next…?
- **Check Passed:** That was easier than I thought.
- **Check Failed:** Not what I wished for…
- **Victory Cry:** Just as I was about to feel some enthusiasm… it’s over already.
- **Extra Conditions Fulfilled:** Today’s performance was satisfying. It entertained me to no end.
- **Defeat Wail:** We can always try again. Nothing says we can’t give it another shake.

### 000 Ten, Który Zaciska Uścisk — Sinclair

> Piąta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 1                                                           |
| HP                        | 79 (+2,73 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–7 / 3–8 / 3–8                                       |
| Poziom obrony             | poziom −4                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×1 (Normal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 70% / 30%                                                   |
| Grzech wyróżniony         | Gniew                                                       |
| Przynależność             | N_Corp, N_Corp_Fnatic                                       |
| Słowa kluczowe            | Krwawienie, Podpalenie                                      |
| Data aktualizacji         | 20230504                                                    |

#### Umiejętność 1 (×3): Przymuszony Wyrok

| Ulepszenie | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Obuch |          7 |         −2 |      2 |           +4 |    1 |
|          3 | Posępność | Obuch |          8 |         −2 |      2 |           +4 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Traci 7 Poczytalności  
Moneta 2: [Trafienie Rewersem] Nakłada 2 Podpalenia

*Od ulepszenia 2:* [Przy Użyciu] Traci 7 Poczytalności  
Moneta 2: [Trafienie Rewersem] Zyskuje 1 Fanatyzmu w następnej turze  
Moneta 2: [Przy Trafieniu] Nakłada 2 Podpalenia

*Od ulepszenia 4:* [Przy Użyciu] Traci 7 Poczytalności  
Moneta 2: [Trafienie Rewersem] Zyskuje 1 Fanatyzmu w następnej turze  
Moneta 2: [Przy Trafieniu] Nakłada 3 Podpalenia

#### Umiejętność 2 (×2): Amoralne Wykonanie

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Obuch |         12 |         −3 |      4 |           +5 |    1 |
|          3 | Żądza  | Obuch |         16 |         −4 |      4 |           +5 |    1 |

*Od ulepszenia 1:* - [Przy Użyciu] Traci 10 Poczytalności  
- Jeżeli ma Fanatyzm, zadaje +5% obrażeń  
Moneta 2: [Trafienie Rewersem] Nakłada 1 Podpalenia  
Moneta 3: [Trafienie Rewersem] Nakłada 1 Podpalenia  
Moneta 4: [Przy Trafieniu] Nakłada 2 Krwawienia

*Od ulepszenia 2:* - [Przy Użyciu] Traci 10 Poczytalności  
- Jeżeli ma Fanatyzm, zadaje +10% obrażeń  
Moneta 2: [Trafienie Rewersem] Nakłada 2 Podpalenia  
Moneta 2: [Przy Trafieniu] Nakłada 1 Podpalenia  
Moneta 3: [Trafienie Rewersem] Nakłada 2 Podpalenia  
Moneta 3: [Przy Trafieniu] Nakłada 1 Podpalenia  
Moneta 4: [Trafienie Rewersem] Zwiększa Licznik Podpalenia o 1  
Moneta 4: [Przy Trafieniu] Nakłada 2 Krwawienia

#### Umiejętność 3 (×1): Samodestrukcyjne Oczyszczenie

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Obuch |         30 |        −12 |      3 |           +5 |    1 |

*Od ulepszenia 3:* - [Przy Użyciu] Traci 15 Poczytalności  
- Jeżeli ma Fanatyzm, zadaje +15% obrażeń  
- Jeżeli cel jest „Zlewem Mechanicznym”, zadaje +10% obrażeń  
Moneta 2: [Przy Trafieniu] Podnosi Próg Oszołomienia o 50% zadanych obrażeń  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 5+ Krwawienia, nakłada 5 Podpalenia  
Moneta 3: [Przy Zabiciu] Zyskuje 1 Wzrost Mocy Uderzenia w następnej turze

*Od ulepszenia 4:* - [Przy Użyciu] Traci 15 Poczytalności  
- Jeżeli ma Fanatyzm, zadaje +15% obrażeń  
- Jeżeli cel jest „Zlewem Mechanicznym”, zadaje +10% obrażeń  
Moneta 2: [Przy Trafieniu] Podnosi Próg Oszołomienia o 50% zadanych obrażeń  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 5+ Krwawienia, nakłada 7 Podpalenia  
Moneta 3: [Przy Zabiciu] Zyskuje 1 Wzrost Mocy Uderzenia w następnej turze

#### Obrona: Dość...

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | obrona: blok |         17 |         −7 |      1 |           +2 |    1 |

[Początek Walki] Odzyskuje 5-10 Poczytalności

#### Pasywka bojowa: Obłędny Płomień

*od ulepszenia 2; posiadane 2× Gniew*

Odzyskuje o 50% mniej Poczytalności za wygrane starcie lub pokonanie wroga

#### Pasywka bojowa: Mad Flame

*od ulepszenia 4; posiadane 2× Gniew*

Heal 50% less SP from winning a clash or defeating an enemy.  
If 5 or more surviving units, including this unit, are 'N Corp. Fanatics', they deal +10% damage.

#### Pasywka wsparcia: Osaczanie

*od ulepszenia 3; posiadane 6× Gniew*

1 Sojusznik z najniższą Poczytalnością zadaje +10% obrażeń Uderzenia  
Jeżeli Poczytalność tego sojusznika jest poniżej 0, im niższa Poczytalność, tym więcej obrażeń Uderzenia (maks. +10%)

#### Kwestie

- **Identity Acquisition:** Everything—I’ll burn it all… and my whole disgusting life, too.
- **Morning Greeting:** So it’s you. Have you slept well? As for me… sleep wouldn’t come.
- **Afternoon Greeting:** I don’t feel like eating. You should take off your mask and have a nice meal.
- **Evening Greeting:** Have you ever been afraid of dreaming? …I wish I were like you.
- **Chatter #1:** Ever since I realized that my life had been intertwined with disgusting beings, my every memory haunts me as its own nightmare.
- **Chatter #2:** I burned and scorched them away… I saw them turn to ashes before my eyes, yet they still torment me.
- **Chatter #3:** …She is right—I must carry out more purification… That will then purify my mind with certainty.
- **Post-Uptie Chat 1:** I skewered sixteen today. Tomorrow, I will nail and cremate twice as many. Huhu… It gets fun as you keep at it, doesn’t it?
- **Post-Uptie Chat 2:** The power to cleanse filth with fire… Indeed, it was certainly a good idea to listen to her.
- **Idle:** …If you have nothing to say, then may I go see her now?
- **Uptying:** This doesn’t really feel special. I have… always had talent… as the chosen one.
- **Deployment:** I’ll wrest them upon stakes.
- **Stage Entry:** To purge the grounds with fire, and build anew a clean world.
- **Viewed in Battle:** I’m busy right now.
- **Commencing Attack:** Unto the fire.
- **Enemy Stagger:** …Good.
- **Staggered:** Huch!
- **Enemy Killed:** …Go down in flames.
- **Death:** Was this… not the answer…?
- **Check Passed:** That wasn’t troublesome at all.
- **Check Failed:** Tsk, I knew that wouldn’t work.
- **Victory Cry:** I think… I did well enough to be acknowledged by her.
- **Extra Conditions Fulfilled:** It’s only natural. Because I… am the chosen one… Isn’t that right?
- **Defeat Wail:** Scheiße, just how did—? Grrmgh…

### 00 Lobotomy E.G.O:: Czerwony Arkusz — Sinclair

> Szósta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 2                                                           |
| HP                        | 76 (+2,7 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 2–6 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 30%                                                   |
| Grzech wyróżniony         | Żądza                                                       |
| Przynależność             | Atl                                                         |
| Słowa kluczowe            | Rozdarcie                                                   |
| Data aktualizacji         | 20230629                                                    |

#### Umiejętność 1 (×3): Uwydatnienie Rany

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Obuch |          4 |         +5 |      1 |           +0 |    1 |
|          3 | Obżar. | Obuch |          5 |         +5 |      1 |           +0 |    1 |

*Od ulepszenia 1:* Moneta 1: [Przy Trafieniu] Nakłada 2 Rozdarcia

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Nakłada 2 Rozdarcia  
Moneta 1: [Trafienie Awersem] Jeżeli cel ma 5+ [Rozdarcie], zyskuje 1 Talizmanu

*Od ulepszenia 4:* Moneta 1: [Przy Trafieniu] Nakłada 2 Rozdarcia  
Moneta 1: [Przy Trafieniu] Jeżeli cel ma 5+ [Rozdarcie], zyskuje 1 Talizmanu

#### Umiejętność 2 (×2): Rozrastające się Talizmany

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Obuch |          3 |         +3 |      3 |           +0 |    1 |
|          3 | Pycha  | Obuch |          4 |         +3 |      3 |           +0 |    1 |

*Od ulepszenia 1:* Moneta 1: [Trafienie Awersem] Zyskuje 1 Talizmanu  
Moneta 2: [Trafienie Awersem] Zyskuje 1 Talizmanu  
Moneta 3: [Przy Trafieniu] Zyskuje 1 Talizmanu

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Zyskuje 1 Talizmanu  
Moneta 2: [Przy Trafieniu] Zyskuje 1 Talizmanu  
Moneta 3: [Przy Trafieniu] Zyskuje 1 Talizmanu  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma 3+ [Rozdarcie], zyskuje 1 Talizmanu

*Od ulepszenia 4:* Moneta 1: [Przy Trafieniu] Zyskuje 1 Talizmanu  
Moneta 1: [Przy Trafieniu] Jeżeli cel ma [Rozdarcie], zyskuje 1 Talizmanu  
Moneta 2: [Przy Trafieniu] Zyskuje 1 Talizmanu  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma [Rozdarcie], zyskuje 1 Talizmanu  
Moneta 3: [Przy Trafieniu] Zyskuje 1 Talizmanu  
Moneta 3: [Przy Trafieniu] Jeżeli cel ma [Rozdarcie], zyskuje 1 Talizmanu

#### Umiejętność 3 (×1): Talizman Rozdarcia

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Kłucie |          5 |         +6 |      2 |           +0 |    1 |

*Od ulepszenia 3:* Moneta 1: [Przy Trafieniu] Zużywa 5 Talizmanów; nakłada 5 Talizmanów  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma [Talizman], zwiększa Licznik Rozdarcia o 1

*Od ulepszenia 4:* Moneta 1: [Przy Trafieniu] Zużywa 5 Talizmanów; nakłada 5 Talizmanów  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma [Talizman], zwiększa Licznik Rozdarcia o 3

#### Obrona: Blok

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |          8 |         +5 |      1 |           +1 |    1 |
|          4 | Obżar.  | obrona: blok |          8 |         +8 |      1 |           +1 |    1 |

[Przy Użyciu] Zyskuje 1 Talizmanu

#### Pasywka bojowa: Zdejmowanie Talizmanów

*od ulepszenia 2; rezonans 3× Obżar.*

Przy trafieniu, jeżeli cel ma [Rozdarcie], zyskuje 1 Talizmanu

#### Pasywka wsparcia: Talizman Życzenia

*od ulepszenia 3; posiadane 4× Obżar.*

1 Sojusznik z najwyższym obecnym HP nakłada o 1 więcej Mocy Rozdarcia Umiejętnościami ataku i Kontry

#### Kwestie

- **Identity Acquisition:** Ah... You've done it, you've... found me.
- **Morning Greeting:** Is there anything you wish? Why don't you come over... and try this with me?
- **Afternoon Greeting:** Judging from the slanted ray of sunlight seeping in... Now must be noon. That's what time it is.
- **Evening Greeting:** I should light more candles. If it's too dark... you won't see well in the night.
- **Chatter #1:** It was such a long time... How many hours have passed while we stayed in here?
- **Chatter #2:** The talismans... shouldn't be too sparse. But... there shouldn't be too many of them on my body, either.
- **Chatter #3:** These talismans... can impede movement. The more of them are attached... the more the curse piles up.
- **Post-Uptie Chat 1:** Ah... You'll use them with me... thank you. ...Ah! Y-You shouldn't attach them to me, even as a prank!
- **Post-Uptie Chat 2:** The ones on my body... I can't remove on my own. It's... that kind of curse.
- **Idle:** If you have the time, I'd suggest resting while watching fire. It calms your mind.
- **Uptying:** For the liberation... I'll bear this, even if it's a curse.
- **Deployment:** So there's something you want cursed.
- **Stage Entry:** I'll follow.
- **Viewed in Battle:** Stay... focused.
- **Commencing Attack:** Stop there, and stay there.
- **Enemy Stagger:** They've become sluggish.
- **Staggered:** Hkh...
- **Enemy Killed:** Into the curse they sink.
- **Death:** Ah... So it stops... in the end...
- **Check Passed:** It worked as we wished.
- **Check Failed:** This, too, is a curse...
- **Victory Cry:** We did it. Phew... I hope this brings us closer to the liberation.
- **Extra Conditions Fulfilled:** They have all been stopped... Now, we'll be able to liberate technology.
- **Defeat Wail:** It must be... that the cursed can't so much as curse others...

### 00 Centrum Łodzi Trzonowca Fikser — Sinclair

> Siódma Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 2                                                           |
| HP                        | 69 (+2,39 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–5 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom −2                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×0,5 (Endured), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 65% / 35% / 15%                                             |
| Grzech wyróżniony         | Posępność                                                   |
| Przynależność             | Molar                                                       |
| Słowa kluczowe            | Wstrząs                                                     |
| Data aktualizacji         | 20230727                                                    |

#### Umiejętność 1 (×3): Gwałtowny Szturm

| Ulepszenie | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Obuch |          2 |         +1 |      4 |           +1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 1  
Moneta 4: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 1

*Od ulepszenia 2:* Przy 10+ Licznika Wstrząsu Moc Monet +1  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 2: [Trafienie Awersem] Nakłada +1 Licznika Wstrząsu  
Moneta 4: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 4: [Trafienie Awersem] Nakłada +1 Licznika Wstrząsu

*Od ulepszenia 4:* Przy 10+ Licznika Wstrząsu Moc Monet +1  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 4: [Przy Trafieniu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 4: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]

#### Umiejętność 2 (×2): Spokojnie...

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Kłucie |          3 |        +12 |      1 |           +1 |    1 |
|          3 | Zawiść | Kłucie |          4 |        +12 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Wstrząs]

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 4  
Moneta 1: [Przy Trafieniu] Nakłada 4 Wstrząsu

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa własny Licznik Wstrząsu o 6  
Moneta 1: [Przy Trafieniu] Nakłada 6 Wstrząsu

#### Umiejętność 3 (×1): Zakład

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Kłucie |          4 |         +6 |      2 |           +1 |    1 |

*Od ulepszenia 3:* Moneta 1: [Przy Trafieniu] Przy 10+ Licznika Wstrząsu zużywa cały Licznik Wstrząsu, aby nakładać na cel tyle samo Licznika Wstrząsu  
[Przy Trafieniu] Przy mniej niż 10 Licznika Wstrząsu zyskuje 6 Wstrząsu i wywołuje na sobie [Wybuch Wstrząsu]  
Zadaje celowi obrażenia Uderzenia równe obrażeniom [Wybuch Wstrząsu]

*Od ulepszenia 4:* Moc Monet +1 za każde 10 Licznika Wstrząsu (maks. 2)  
Moneta 1: [Przy Trafieniu] Przy 10+ Licznika Wstrząsu zużywa cały Licznik Wstrząsu, aby nakładać na cel tyle samo Licznika Wstrząsu  
[Przy Trafieniu] Przy mniej niż 10 Licznika Wstrząsu zyskuje 10 Wstrząsu i wywołuje na sobie [Wybuch Wstrząsu]  
Zadaje celowi obrażenia Uderzenia równe obrażeniom [Wybuch Wstrząsu]

#### Obrona: Skorupiaki-Chamy...!

| Ulepszenie | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral   | obrona: blok |          8 |         +5 |      1 |           −2 |    1 |
|          4 | Posępność | obrona: blok |          8 |         +8 |      1 |           −2 |    1 |

[Przy Użyciu] Zyskuje 1 Ochrony przed Rozdarciami (maks. 3 razy na turę)

#### Pasywka bojowa: Niestabilne Wyjście Mocy

*od ulepszenia 2; posiadane 4× Posępność*

Przy trafieniu awersem przy 10+ Licznika Wstrząsu, efekty monet nakładają o 1 więcej Wstrząsu i Licznika Wstrząsu

#### Pasywka wsparcia: Zmodyfikowane Wyjście Mocy

*od ulepszenia 3; posiadane 4× Posępność*

1 Sojusznik z najwyższym Maks. HP nakłada o 1 więcej Wstrząsu efektami swoich Umiejętności ataku i monet

#### Kwestie

- **Identity Acquisition:** Mm... Are you here to get your boat fixed up? We'll take good care of it.
- **Morning Greeting:** The shop isn't open yet... Oh, I'll get you a chair so you can sit and rest while you wait.
- **Afternoon Greeting:** Mmgh... I wanna eat something else for once... We've made all kinds of dishes out of those trash crabs—steamed, stewed, roasted, souped, you name it... but none of them ever taste any good!
- **Evening Greeting:** Ah! Did the flash from the welding rod hurt your eyes? Sorry about that... There's work to be done even after the shop's closed.
- **Chatter #1:** When I first got up and found myself here, I had no idea what to make of anything... I almost starved to death wandering around.
- **Chatter #2:** I'm not all too used to handling machinery...but I've got to practice hard if I want to get back to where I used to live. And who knows, this experience might be pretty handy in the future.
- **Chatter #3:** I'm used to it now, but U Corp's Singularity was always so fascinating to me... Attaching parts with this thing melds them together, as though they were made this way from the start.
- **Post-Uptie Chat 1:** This weapon too, was made from mechanical knowledge and welding skills I learned here. It doesn't look very sophisticated, but... Not bad, right?
- **Post-Uptie Chat 2:** We could come this far thanks to all the help from people in other boat shops here. ...They're no longer around, though.
- **Idle:** Hmm... I should read more books on maintenance in the meantime.
- **Uptying:** The upgrade certainly improved the output... but it kinda feels redundant if all I'm doing with it is catching more crabs.
- **Deployment:** The gears are in motion.
- **Stage Entry:** Häää? What's wrong with the power output...?
- **Viewed in Battle:** Need something repaired?
- **Commencing Attack:** Stabilizing output... There!
- **Enemy Stagger:** Good going...!
- **Staggered:** Ngh…
- **Enemy Killed:** Phew, took care of that one.
- **Death:** No... They're... waiting... for me.
- **Check Passed:** That was the right answer!
- **Check Failed:** This... wasn't quite it.
- **Victory Cry:** I should go back and deal with the remaining work.
- **Extra Conditions Fulfilled:** That was clean, wasn't it? I'm pretty proud of it if I do say so myself. Huh, my weapon's going... Wha, what's wrong with it?
- **Defeat Wail:** Noo... I didn't think it'd go this way... What was I missing...

### 000 Południowe Stowarzyszenie Cinq Sekcja 4 Dyrektor — Sinclair

> Ósma Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 0                                                           |
| HP                        | 79 (+2,73 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 4–6 / 4–7 / 4–8 / 4–8                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×0,5 (Endured), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 65% / 35%                                                   |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Cinq                                                        |
| Słowa kluczowe            | Oddech                                                      |
| Data aktualizacji         | 20231221                                                    |

#### Umiejętność 1 (×3): Remise

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Kłucie |          2 |         +4 |      2 |           +2 |    1 |
|          3 | Obżar. | Kłucie |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Trafienie Awersem] Zyskuje 1 [Pośpiech] w następnej turze  
Moneta 2: [Trafienie Awersem] Zyskuje 1 [Pośpiech] w następnej turze

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Pośpiech] w następnej turze  
Moneta 2: [Przy Trafieniu] Zyskuje 1 [Pośpiech] w następnej turze

*Od ulepszenia 4:* Jeżeli Szybkość jest o 2 lub więcej wyższa niż celu, Moc Monet +1  
[Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Pośpiech] w następnej turze  
Moneta 2: [Przy Trafieniu] Zyskuje 1 [Pośpiech] w następnej turze

#### Umiejętność 2 (×2): Engagement

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Kłucie |          3 |         +4 |      3 |           +2 |    1 |
|          3 | Pycha  | Kłucie |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [Wygrane Starcie] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Trafienie Awersem] Zwiększa własny Licznik [Oddech] o 1  
Moneta 2: [Trafienie Awersem] Zwiększa własny Licznik [Oddech] o 1

*Od ulepszenia 2:* Jeżeli Szybkość jest o 2 lub więcej wyższa niż celu, Moc Monet +1  
[Wygrane Starcie] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]  
Moneta 2: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]

*Od ulepszenia 4:* Jeżeli Szybkość jest wyższa niż celu, Moc Monet +1 za każdą różnicę Szybkości 2 (maks. 2)  
[Wygrane Starcie] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]  
Moneta 2: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]

#### Umiejętność 3 (×1): Contre Attaque

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Kłucie |          5 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 3:* Jeżeli Szybkość jest o 2 lub więcej wyższa niż celu, Moc Monet +1  
[Wygrane Starcie] Zużywa 10 Licznika [Oddech]. Zyskuje [Oddech] równy zużytym Licznikom [Oddech].  
[Wygrane Starcie] Jeżeli przeprowadzono [Pojedynek Jeden na Jednego] z Umiejętnością ataku w slocie wroga, przy trafieniu nakłada 1 [Wrażliwość] (2 razy na turę)  
Moneta 1: [Przy Trafieniu] Nakłada [Wyzwanie na Pojedynek - Sinclair]  
Moneta 3: Zadaje +30% obrażeń przy trafieniu krytycznym

*Od ulepszenia 4:* Jeżeli Szybkość jest wyższa niż celu, Moc Monet +1 za każdą różnicę Szybkości 2 (maks. 3)  
[Wygrane Starcie] Zużywa 10 Licznika [Oddech]. Zyskuje [Oddech] równy zużytym Licznikom [Oddech]. Przeciwko celowi z [Wyzwanie na Pojedynek - Sinclair] zamiast tego zyskuje (Zużyte Liczniki [Oddech] x 2) [Oddech]  
[Wygrane Starcie] Jeżeli przeprowadzono [Pojedynek Jeden na Jednego] z Umiejętnością ataku w slocie wroga, przy trafieniu nakłada 1 [Wrażliwość] (2 razy na turę)  
Moneta 1: [Przy Trafieniu] Nakłada [Wyzwanie na Pojedynek - Sinclair]  
Moneta 3: Zadaje +50% obrażeń Krytycznych

#### Obrona: Défensive

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          4 |        +10 |      1 |           +3 |    1 |
|          4 | Obżar.  | obrona: unik |          4 |        +10 |      1 |           +3 |    1 |

#### Pasywka bojowa: Uśpiona Żądza Krwi

*od ulepszenia 2; posiadane 5× Pycha*

Na koniec tury Maks. Szybkość +2 w następnej turze za każde 5 Licznika [Oddech] (maks. 6)

#### Pasywka bojowa: Uśpiona Żądza Krwi

*od ulepszenia 4; posiadane 5× Pycha*

Na koniec tury Maks. Szybkość +2 w następnej turze za każde 5 Licznika [Oddech] (maks. 6)  
Na początku walki, jeżeli Szybkość wszystkich sojuszników jest wyższa niż wszystkich wrogów, zyskuje 1 [Wzrost Obrażeń Przebicia]

#### Pasywka wsparcia: Za Wolno

*od ulepszenia 3; rezonans 3× Pycha*

1 Sojusznik z najwyższą Szybkością zyskuje 1 [Pośpiech] w następnej turze po skutecznym uniku (maks. 5 razy)

#### Kwestie

- **Identity Acquisition:** O—oh, I'm sorry! W-was I too rough...?!
- **Morning Greeting:** Ah, hello~ Having a good morning today? You're looking pretty upbeat!
- **Afternoon Greeting:** How about we grab lunch together today— Ah, uh... Give me a second. Haah, I'm sorry. My coworkers are calling me over, and I shouldn't refuse them.
- **Evening Greeting:** I love breathing in the night air. It helps me focus solely on my sword... All I can see are the tip of my blade and my enemy's throat.
- **Chatter #1:** Sometimes... I wonder if the sword is wielding me and not the other way around. I sometimes lose myself and get too aggressive, even during a friendly spar.
- **Chatter #2:** I'm a bit all over the place, and I make a lot of mistakes... but I like it here! My coworkers are so nice to me. Mmm... Sometimes, they give me worried looks, though. I guess they're worried that I might stumble into another blunder?
- **Chatter #3:** So uh... I just need to use my arm to... Woaaah?! Did I do that right...? I can just topple them, just like that?!
- **Post-Uptie Chat 1:** Imagine that the end of the blade is already touching the enemy's vitals. Did you ever learn about the exercise where you can make your fingers touch just by imagining it really hard? It's just like that. See?
- **Post-Uptie Chat 2:** When I'm ready to duel, my surroundings fade away. A part of me does, too. There is nothing before me but the enemy in a dark, dark place.
- **Idle:** Ah! I'm finally free from work! Now we can talk... Ah, where are you?
- **Uptying:** I'll show you impeccable focus. Though you will never see as I do.
- **Deployment:** Is it work?
- **Stage Entry:** Focus... on the tip of my blade...
- **Viewed in Battle:** .......
- **Commencing Attack:** There it is.
- **Enemy Stagger:** More.
- **Staggered:** Hah?!
- **Enemy Killed:** I've hit all of your vital areas.
- **Death:** Huh? No... I thought... the duel was... going well...
- **Check Passed:** Hmph... Huh? That worked?
- **Check Failed:** That didn't work? Then how about here? No, here?!
- **Victory Cry:** Well, that worked out... somehow! Whew, I guess I didn't make any mistakes this time.
- **Extra Conditions Fulfilled:** More... Oh hey, guys! Uh... why are you backing away?
- **Defeat Wail:** It can't end like this. I have—I know I can do better!

### 000 Biuro Świtu Fikser — Sinclair

> Dziewiąta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | wydarzenie 9103                                             |
| HP                        | 66 (+2,28 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Posępność                                                   |
| Przynależność             | Dawn                                                        |
| Słowa kluczowe            | Podpalenie                                                  |
| Data aktualizacji         | 20240502                                                    |

#### Umiejętność 1 (×3): Gwałtowny Napór

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Cięcie |          2 |         +7 |      1 |           +2 |    1 |
|          3 | Posępność | Cięcie |          3 |         +7 |      1 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 1: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 1: [Trafienie Awersem] Jeżeli jest w stanie Niestabilnego E.G.O, ponownie używa monetę (1 raz na Umiejętność)

*Od ulepszenia 2:* Moneta 1: [Przy Trafieniu] Nakłada 2 [Podpalenie]  
Moneta 1: [Trafienie Awersem] Jeżeli jest w stanie Niestabilnego E.G.O, ponownie używa monetę (1 raz na Umiejętność)

*Od ulepszenia 4:* Moneta 1: [Przy Trafieniu] Nakłada 2 [Podpalenie]  
Moneta 1: [Trafienie Awersem] Jeżeli jest w stanie Niestabilnego E.G.O, ponownie używa monetę (1 raz na Umiejętność)

#### Umiejętność 2 (×2): Miecz Zachodzącego Słońca

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Cięcie |          4 |         +3 |      3 |           +2 |    1 |
|          3 | Zawiść | Cięcie |          5 |         +3 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] W stanie Niestabilnego E.G.O zużywa 5 Poczytalności  
[Przed Atakiem] W stanie Niestabilnego E.G.O Waga ataku +1  
[Koniec Ataku] W stanie Niestabilnego E.G.O zużywa 5 Poczytalności  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1

*Od ulepszenia 2:* Jeżeli cel ma 4+ [Podpalenie], Moc Starcia +1  
[Przy Użyciu] W stanie Niestabilnego E.G.O zużywa 5 Poczytalności  
[Przed Atakiem] W stanie Niestabilnego E.G.O Waga ataku +1  
[Koniec Ataku] W stanie Niestabilnego E.G.O zużywa 5 Poczytalności  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1

*Od ulepszenia 4:* Jeżeli cel ma 4+ [Podpalenie], Moc Starcia +1  
[Przy Użyciu] Jeżeli jest w stanie Niestabilnego E.G.O, zużywa 5 Poczytalności  
[Przed Atakiem] Jeżeli jest w stanie Niestabilnego E.G.O, Waga ataku +1  
- Przy 45 Poczytalności zamiast tego Waga ataku +2  
[Koniec Ataku] Jeżeli jest w stanie Niestabilnego E.G.O, zużywa 5 Poczytalności  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1

#### Umiejętność 3 (×1): Napiętnowanie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Kłucie |          4 |         +7 |      2 |           +3 |    1 |

*Od ulepszenia 3:* Jeżeli cel ma 10+ [Podpalenie], Moc Monet +1  
Jeżeli jest w stanie Niestabilnego E.G.O, stosuje się jako „Płonący Cios”  
[Wygrane Starcie] Odzyskuje 10 Poczytalności  
[Przegrane Starcie] Traci 10 Poczytalności  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]

*Od ulepszenia 4:* Moc Monet +1 za każde 7 [Podpalenie] celu (maks. 2)  
Jeżeli jest w stanie Niestabilnego E.G.O, stosuje się jako „Płonący Cios”  
[Wygrane Starcie] Odzyskuje 10 Poczytalności  
[Przegrane Starcie] Traci 10 Poczytalności  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]

#### Umiejętność 4 (×0): Płonący Cios

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |         13 |        +15 |      1 |           +5 |    1 |

*Od ulepszenia 3:* Moc Monet +1 za każde 4 (suma Mocy [Podpalenie] wszystkich wrogów) (maks. 8)  
[Wygrane Starcie] Odzyskuje 10 Poczytalności  
[Przegrane Starcie] Traci 30 Poczytalności  
Zadaje +5% obrażeń za każdy Rezonans Gniewu (maks. 30%)  
[Koniec Ataku] Traci 15 Poczytalności  
Moneta 1: Zadaje +2.5% obrażeń za każde 1 [Podpalenie] celu (maks. 100%)  
Moneta 1: [Przy Trafieniu] Jeżeli cel ma 10+ [Podpalenie], nakłada 2 [Podpalenie] na (najwyższy Rezonans) losowych wrogów  
Moneta 1: [Przy Trafieniu] Nakłada 10 [Podpalenie]  
Moneta 1: [Przy Zabiciu] Rozdziela Moc [Podpalenie] pokonanego celu losowo między wrogów (maks. 10; w walkach skupionych Party)

*Od ulepszenia 4:* Moc Monet +2 za każde 4 (suma Mocy [Podpalenie] wszystkich wrogów) (maks. 8)  
[Wygrane Starcie] Odzyskuje 10 Poczytalności  
[Przegrane Starcie] Traci 30 Poczytalności  
Zadaje +10% (maks. 60%) obrażeń za każdy Rezonans Gniewu  
Przy 4+ najwyższym Pełnym Rezonansie Gniewu zamiast tego zadaje +20% obrażeń za każdy Rezonans Gniewu (maks. 120%)  
[Koniec Ataku] Traci 15 Poczytalności  
Moneta 1: Zadaje +4% (maks. 120%) obrażeń za każde 1 [Podpalenie] celu  
Moneta 1: [Przy Trafieniu] Jeżeli cel ma 10+ [Podpalenie], nakłada 2 [Podpalenie] na (najwyższy Rezonans) losowych wrogów  
- Jeżeli ten Rezonans był Rezonansem Gniewu, dodatkowo nakłada 1 Licznika [Podpalenie]  
Moneta 1: [Przy Trafieniu] Nakłada 10 [Podpalenie]  
Moneta 1: [Przy Zabiciu] Rozdziela Moc [Podpalenie] pokonanego celu losowo między wrogów (maks. 10; w walkach skupionych Party)

#### Obrona: Skrucha

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         15 |         +5 |      1 |           +5 |    1 |
|          4 | Żądza   | obrona: blok |         15 |         +5 |      1 |           +5 |    1 |

*Od ulepszenia 3:* Jeżeli jest w stanie Niestabilnego E.G.O, Moc Bazowa +1 za każde 2 [Podpalenie] celu (maks. 10)

*Od ulepszenia 4:* Jeżeli jest w stanie Niestabilnego E.G.O, Moc Bazowa +1 za każde 2 [Podpalenie] celu (maks. 20)

#### Pasywka bojowa: Niestabilna Skorupa Ego

*od ulepszenia 1*

Na początku tury, przy Poczytalności 40 lub wyższej, zużywa 20 Poczytalności, aby wejść w stan Niestabilnego E.G.O::Woskowe Skrzydło. (efekt „na początku tury” nie uruchamia się ponownie)  
Albo, gdy 2 lub więcej sojuszników ginie w jednej turze, na koniec tury, jeżeli Poczytalność nie wynosi -45, zmienia ją na 20, po czym wchodzi w stan Niestabilnego E.G.O::Woskowe Skrzydło. (jeżeli oba warunki zostały spełnione jednocześnie, wyższa wartość Poczytalności decyduje)  
  
Wchodząc w stan Niestabilnego E.G.O, jeżeli zostanie Ogłuszona obrażeniami albo Podniesieniem Progu Oszołomienia, dochodzi z Ogłuszenia. Jeżeli Ogłuszenia nie można naturalnie wyleczyć, nie może wejść w stan Niestabilnego E.G.O.  
  
W stanie Niestabilnego E.G.O zyskuje [Niestabilne Namiętności].  
  
Na początku tury, przy Poczytalności 0 lub niższej, stan Niestabilnego E.G.O zostaje zdjęty.

#### Pasywka bojowa: 1100903

*od ulepszenia 1*



#### Pasywka bojowa: Niestabilna Skorupa Ego

*od ulepszenia 2*

Na początku tury, przy Poczytalności 40 lub wyższej, zużywa 20 Poczytalności, aby wejść w stan Niestabilnego E.G.O::Woskowe Skrzydło. (efekt „na początku tury” nie uruchamia się ponownie)  
Albo, gdy 2 lub więcej sojuszników ginie w jednej turze, na koniec tury, jeżeli Poczytalność nie wynosi -45, zmienia ją na 20, po czym wchodzi w stan Niestabilnego E.G.O::Woskowe Skrzydło. (jeżeli oba warunki zostały spełnione jednocześnie, wyższa wartość Poczytalności decyduje)  
  
Wchodząc w stan Niestabilnego E.G.O, jeżeli zostanie Ogłuszona obrażeniami albo Podniesieniem Progu Oszołomienia, dochodzi z Ogłuszenia. Jeżeli Ogłuszenia nie można naturalnie wyleczyć, nie może wejść w stan Niestabilnego E.G.O.  
  
W stanie Niestabilnego E.G.O zyskuje [Niestabilne Namiętności].  
  
Na początku tury, przy Poczytalności 0 lub niższej, stan Niestabilnego E.G.O zostaje zdjęty.

#### Pasywka bojowa: 1100903

*od ulepszenia 2*



#### Pasywka bojowa: Broń Warsztatu Stigma / Pasja

*od ulepszenia 2; posiadane 5× Gniew*

Nakłada o 1 więcej Mocy [Podpalenie] Umiejętnościami (uruchamia się 6 razy na turę)  
W stanie Niestabilnego E.G.O, przy Poczytalności 0 lub wyższej, Moc Monet +(Poczytalność / 20). Przy 45 Poczytalności zamiast tego Moc Monet +3

#### Pasywka bojowa: Niestabilna Skorupa Ego

*od ulepszenia 4*

Na początku tury, przy Poczytalności 40 lub wyższej, zużywa 20 Poczytalności, aby wejść w stan Niestabilnego E.G.O::Woskowe Skrzydło. (efekt „na początku tury” nie uruchamia się ponownie)  
Albo, gdy 2 lub więcej sojuszników ginie w jednej turze, na koniec tury, jeżeli Poczytalność nie wynosi -45, zmienia ją na 20, po czym wchodzi w stan Niestabilnego E.G.O::Woskowe Skrzydło. (jeżeli oba warunki zostały spełnione jednocześnie, wyższa wartość Poczytalności decyduje)  
  
Wchodząc w stan Niestabilnego E.G.O, jeżeli zostanie Ogłuszona obrażeniami albo Podniesieniem Progu Oszołomienia, dochodzi z Ogłuszenia. Jeżeli Ogłuszenia nie można naturalnie wyleczyć, nie może wejść w stan Niestabilnego E.G.O.  
  
W stanie Niestabilnego E.G.O zyskuje [Niestabilne Namiętności].  
  
Na początku tury, przy Poczytalności 0 lub niższej, stan Niestabilnego E.G.O zostaje zdjęty.

#### Pasywka bojowa: 1100903

*od ulepszenia 4*



#### Pasywka bojowa: Broń Warsztatu Stigma / Pasja

*od ulepszenia 4; posiadane 5× Gniew*

Nakłada o 1 więcej Mocy i Licznika [Podpalenie] Umiejętnościami (uruchamia się 6 razy na turę)  
W stanie Niestabilnego E.G.O, przy Poczytalności 0 lub wyższej, Moc Monet +(Poczytalność / 20). Przy 45 Poczytalności zamiast tego Moc Monet +3

#### Pasywka wsparcia: Kipiący Miecz

*od ulepszenia 3; rezonans 3× Gniew*

Gdy Sojusznik przydzielony na 1. pozycji trafi awersem, nakłada 1 Licznika [Podpalenie] (uruchamia się 4 razy na turę)

#### Kwestie

- **Identity Acquisition:** Sometimes I get hand tremors... I hope that doesn't make me look like a coward.
- **Morning Greeting:** Oh! You're back early. As always, I placed any and all contract requests we received today on your desk.
- **Afternoon Greeting:** We should get to work soon. Or our Office might not make our next month's rent.
- **Evening Greeting:** It's pretty cold tonight. How about a warm cup of ssanghwa-cha?
- **Chatter #1:** Do you listen to music from time to time? I enjoy the sound of cello myself. One day, I hope to have a chance to try my hand at learning it. I'm sure creating music with my own hands feels different.
- **Chatter #2:** Weapons from Stigma Workshop brand their victims with their unique 'stigma'. Even if they were to survive the fight, they'll have to live with that mark for the rest of their lives.
- **Chatter #3:** Oh, did you enjoy the ssanghwa-cha? Huh? They'd call me 'The Yellow Ssanghwa' if I ever became a Color...? I mean, I guess my blonde hair does resemble an egg yolk, but... Come on, don't tease me like that.
- **Post-Uptie Chat 1:** Are people of the City... not allowed to do anything on behalf of others?
- **Post-Uptie Chat 2:** "For them". "For the others". "For someone else's sake"... You know, they were all just... selfish disguises to hide my true self. Have you ever pretended to be something you're not?
- **Idle:** Everyone... needs the time to collect their thoughts.
- **Uptying:** No one's going to shed their tears on behalf of my sorrow.
- **Deployment:** Do we have... a contract? Okay, I'll go get ready.
- **Stage Entry:** I'll try my best not to hold you back.
- **Viewed in Battle:** Give me the courage to stand up to something...
- **Commencing Attack:** I will follow your judgment.
- **Commencing Attack 2:** I'm just as scared as I was before. But... despite everything, I don't want to stop.
- **Enemy Stagger:** I shouldn't hesitate...
- **Staggered:** I feel like I'm just causing you concern...
- **Enemy Killed:** ... I have to be bold!
- **Death:** I thought... I'd be there for you all the way...
- **Check Passed:** It was for everyone's sake.
- **Check Failed:** I didn't want to be a baggage... to you all...
- **Victory Cry:** We did suffer some losses, but... only the outcome matters in the end.
- **Extra Conditions Fulfilled:** That was certainly a perfect victory. How about we throw a house party like we did last time?
- **Defeat Wail:** Not yet... I've got to, I've got to go ask for help...!

### 00 Zachodnie Stowarzyszenie Zwei Sekcja 3 — Sinclair

> Dziesiąta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 00                                                          |
| Sezon                     | 5                                                           |
| HP                        | 86 (+2,96 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom +4                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×2 (Fatal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 60%                                                         |
| Grzech wyróżniony         | Żądza                                                       |
| Przynależność             | Zwei                                                        |
| Słowa kluczowe            | Wstrząs                                                     |
| Data aktualizacji         | 20241010                                                    |

#### Umiejętność 1 (×3): Powstrzymuję.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Cięcie |          2 |         +4 |      2 |           +0 |    1 |
|          3 | Żądza  | Cięcie |          3 |         +4 |      2 |           +0 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 3 w następnej turze  
[Przy Użyciu] Zyskuje 1 [Wzrost Poziomu Obrony]  
[Wygrane Starcie] Zwiększa własny Licznik [Wstrząs] o 2  
Moneta 1: [Trafienie po Wygranym Starciu] Zwiększa Licznik [Wstrząs] o 1  
Moneta 2: [Trafienie Awersem] Zyskuje 2 [Wzrost Poziomu Obrony] w następnej turze

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu Umiejętności o 3 w następnej turze  
[Przy Użyciu] Zyskuje 2 [Wzrost Poziomu Obrony]  
[Przy Użyciu] Jeżeli cel ma 4+ Licznika [Wstrząs], Moc Starcia +1  
[Wygrane Starcie] Zwiększa własny Licznik [Wstrząs] o 2  
Moneta 1: [Trafienie po Wygranym Starciu] Zwiększa Licznik [Wstrząs] o 2  
Moneta 2: [Trafienie Awersem] Zyskuje 2 [Wzrost Poziomu Obrony] w następnej turze

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu Umiejętności o 3 w następnej turze  
[Przy Użyciu] Zyskuje 2 [Wzrost Poziomu Obrony]  
[Przy Użyciu] Jeżeli cel ma 4+ Licznika [Wstrząs], Moc Starcia +2  
[Wygrane Starcie] Zwiększa własny Licznik [Wstrząs] o 3  
Moneta 1: [Trafienie po Wygranym Starciu] Zwiększa Licznik [Wstrząs] o 2  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Wzrost Poziomu Obrony] w następnej turze

#### Umiejętność 2 (×2): Przygotowanie do walki

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Cięcie |          3 |         +5 |      2 |           +1 |    1 |
|          3 | Posępność | Cięcie |          4 |         +5 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 3 w następnej turze  
[Wygrane Starcie] Zwiększa własny Licznik [Wstrząs] o 2  
Moneta 2: [Przy Trafieniu] Nakłada (([Wzrost Poziomu Obrony] sojusznika)/3) [Wzrost Poziomu Ataku] w następnej turze na 1 Sojusznika z [Wzrost Poziomu Obrony] poza tą jednostką (1 raz na turę; maks. 3 nakładów)

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu Umiejętności o 3 w następnej turze  
[Przy Użyciu] Zyskuje 1 [Wzrost Poziomu Obrony] za każde 2 Licznika [Wstrząs] (maks. 3)  
[Przy Użyciu] Przy 4+ [Wzrost Poziomu Obrony] Moc Monet +1  
[Wygrane Starcie] Zwiększa własny Licznik [Wstrząs] o 3  
Moneta 1: [Trafienie po Wygranym Starciu] Nakłada 2 Wzrostu Poziomu Obrony w następnej turze na 1 Sojusznika z najniższym procentem HP poza tą jednostką  
Moneta 2: [Przy Trafieniu] Nakłada (([Wzrost Poziomu Obrony] sojusznika)/2) [Wzrost Poziomu Ataku] w następnej turze na 1 Sojusznika z [Wzrost Poziomu Obrony] poza tą jednostką (1 raz na turę; maks. 3 nakładów)

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu Umiejętności o 3 w następnej turze  
[Przy Użyciu] Zyskuje 1 [Wzrost Poziomu Obrony] za każde 2 Licznika [Wstrząs] (maks. 3)  
[Przy Użyciu] Przy 4+ [Wzrost Poziomu Obrony] Moc Monet +1  
[Wygrane Starcie] Zwiększa własny Licznik [Wstrząs] o 3  
Moneta 1: [Trafienie po Wygranym Starciu] Nakłada 2 Wzrostu Poziomu Obrony w następnej turze na 2 Sojuszników z najniższym procentem HP poza tą jednostką  
Moneta 2: [Przy Trafieniu] Nakłada (([Wzrost Poziomu Obrony] sojusznika)/2) [Wzrost Poziomu Ataku] w następnej turze na 2 Sojuszników z [Wzrost Poziomu Obrony] poza tą jednostką (1 raz na turę; maks. 3 nakładów)

#### Umiejętność 3 (×1): Ogrodzenie

| Ulepszenie | Grzech   | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lenistwo | Obuch |          4 |         +3 |      3 |           +2 |    1 |

*Od ulepszenia 3:* [Przy Użyciu] Zyskuje 1 [Wzrost Poziomu Obrony] za każde 2 Licznika [Wstrząs] (maks. 2)  
[Przy Użyciu] Moc Monet +1 za każde 3 [Wzrost Poziomu Obrony] (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Wzrost Poziomu Obrony] w następnej turze na 1 Sojusznika z najniższym procentem obecnego HP poza tą jednostką  
Moneta 3: [Przy Trafieniu] Zużywa do 8 Licznika [Wstrząs], nakładając na cel tyle samo Licznika [Wstrząs]  
Moneta 3: [Przy Trafieniu] Wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

*Od ulepszenia 4:* [Przy Użyciu] Zyskuje 1 [Wzrost Poziomu Obrony] za każde 2 Licznika [Wstrząs] (maks. 4)  
[Przy Użyciu] Moc Monet +1 za każde 3 [Wzrost Poziomu Obrony] (maks. 3)  
Moneta 1: [Przy Trafieniu] Nakłada 4 [Wzrost Poziomu Obrony] w następnej turze na 1 Sojusznika z najniższym procentem obecnego HP poza tą jednostką  
Moneta 3: [Przy Trafieniu] Zużywa do 8 Licznika [Wstrząs], nakładając na cel tyle samo Licznika [Wstrząs]  
Moneta 3: [Przy Trafieniu] Wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

#### Obrona: Forma Wielkiego Miecza Rycerzy Zwei - Garda

| Ulepszenie | Grzech   | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral  | obrona: blok |          2 |         +7 |      1 |           +0 |    1 |
|          4 | Lenistwo | obrona: blok |          2 |         +9 |      1 |           +0 |    1 |

*Od ulepszenia 1:* [Blok Zdatny do Starcia]  
[Początek Walki] Zwiększa [Wartość Prowokacji] tego slotu Umiejętności o 5 w następnej turze  
[Przy Użyciu] Zwiększa własny Licznik [Wstrząs] o 2 (1 raz na turę)  
[Wygrane Starcie] Wywołuje [Wybuch Wstrząsu]  
Moneta 1: [Moneta Niezniszczalna]

*Od ulepszenia 4:* [Blok Zdatny do Starcia]  
[Początek Walki] Zwiększa [Wartość Prowokacji] tego slotu Umiejętności o 5 w następnej turze  
[Przy Użyciu] Zwiększa własny Licznik [Wstrząs] o 3 (1 raz na turę)  
[Wygrane Starcie] Wywołuje [Wybuch Wstrząsu]  
Moneta 1: [Moneta Niezniszczalna]

#### Pasywka bojowa: Rozpoczęcie Misji Ochronnej

*od ulepszenia 2; posiadane 5× Lenistwo*

Na początku walki zyskuje [Wzrost Poziomu Obrony] równy własnym Licznikom [Wstrząs] (maks. 5)

#### Pasywka wsparcia: Ochrona Celu Zlecenia

*od ulepszenia 3; posiadane 4× Lenistwo*

Na koniec tury nakłada 1 [Pośpiech] i 3 [Wzrost Poziomu Obrony] w następnej turze na 1 Sojusznika z najniższym procentem HP

#### Kwestie

- **Identity Acquisition:** We'll rescue the survivor like you requested, so... can you stop pointing that finger at me...?
- **Morning Greeting:** ... I-it's morning already?! I gotta run if I wanna suit up and make it to the morning assembly—
- **Afternoon Greeting:** There's a lot of paperwork to be done. Hopefully we can take care of this process before the sun goes down... Let's hurry.
- **Evening Greeting:** Can't be too careful when taking on late night rescue contracts. It often ends up putting us in danger, too.
- **Chatter #1:** The Zwei Knights wear these gaudy armors not only because it's our uniform... but also because it draws attention away from our clients when the battle gets messy. And here I was, thinking that this cape was bothersome... I guess everything has a reason.
- **Chatter #2:** There's something I realized whenever I go on joint operations with other Association Fixers... It's that most people don't care about protecting or saving someone. I know that we only move when we're paid to do so, but... our Association's the best when it comes to protecting their clients.
- **Chatter #3:** Sometimes, we receive contracts that are clearly above our pay grade. I hate taking those contracts, but... If they pay enough, us Zwei Fixers have no choice but to do as our Association tells us to do.
- **Post-Uptie Chat 1:** I hate myself for growing so accustomed to people dying around me. I know, I don't have a choice. But... ... No. I can't be so weak-willed... I can't protect anything like this. Just like that day...
- **Post-Uptie Chat 2:** I don't think there's anything wrong with wishing safety for everyone. It's just that it's... impossible. It's the City. We can't even protect the people we love.
- **Idle:** ... Huh? O-oh! Please don't go wandering off on your own!
- **Uptying:** Don't worry. You're my target... so I'll protect you no matter what.
- **Deployment:** Quest... confirmed.
- **Stage Entry:** Thus becomes your blade and shield, this greatsword...
- **Viewed in Battle:** I thought I submitted everything...? What's wrong?
- **Commencing Attack:** Securing personnel...!
- **Enemy Stagger:** Get behind me, now...!
- **Staggered:** Nngh...
- **Enemy Killed:** Excluding high-risk individuals...
- **Death:** I'll be fine... so run... get as far away as you can from here...
- **Check Passed:** I can protect one more person, yeah... But only this time, okay? I can't do this again.
- **Check Failed:** ... I'm sorry. This was not a part of my contract.
- **Victory Cry:** We suffered some losses, but... I guess it couldn't be helped. There's only so much a shield can protect.
- **Extra Conditions Fulfilled:** We actually rescued everyone. I guess days of hard work does pay off... sometimes.
- **Defeat Wail:** We... failed the contract. I couldn't protect anyone... They're... all dead...

### 000 Północne Stowarzyszenie Devyat' Sekcja 3 — Sinclair

> Jedenasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 0                                                           |
| HP                        | 73 (+2,39 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 2–5 / 3–6 / 3–7 / 3–7                                       |
| Poziom obrony             | poziom −2                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×1 (Normal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Devyat                                                      |
| Słowa kluczowe            | Rozdarcie                                                   |
| Data aktualizacji         | 20241128                                                    |

#### Umiejętność 1 (×3): Kufer Kurierski - Młot Rozkładu

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Obuch |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Żądza  | Obuch |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania Licznika [Rozdarcie] nakładają 2 [Spadek Poziomu Obrony] (1 raz na monetę)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Kufer Kuriera - Sinclair]  
- Przy mniej niż 15 [Kufer Kuriera - Sinclair] zyskuje dodatkowo 1 [Kufer Kuriera - Sinclair]  
Moneta 2: [Przy Trafieniu] Nakłada +2 Licznika [Rozdarcie]

*Od ulepszenia 2:* Przy 10+ [Kufer Kuriera - Sinclair], albo gdy cel ma 6+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania Licznika [Rozdarcie] nakładają 2 [Spadek Poziomu Obrony] (1 raz na monetę)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Kufer Kuriera - Sinclair]  
- Przy mniej niż 15 [Kufer Kuriera - Sinclair] zyskuje dodatkowo 1 [Kufer Kuriera - Sinclair]  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Rozdarcie] o 2  
- Przy 15+ [Kufer Kuriera - Sinclair] zwiększa dodatkowo Licznik [Rozdarcie] o 1

*Od ulepszenia 4:* Moc Monet +1 za każde 10 [Kufer Kuriera - Sinclair] albo za każde 6 [Rozdarcie] celu (maks. 2)  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania Licznika [Rozdarcie] nakładają 2 [Spadek Poziomu Obrony] (1 raz na monetę)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Kufer Kuriera - Sinclair]  
- Przy mniej niż 15 [Kufer Kuriera - Sinclair] zyskuje dodatkowo 1 [Kufer Kuriera - Sinclair]  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Rozdarcie] o 2  
- Przy 15+ [Kufer Kuriera - Sinclair] zwiększa dodatkowo Licznik [Rozdarcie] o 1

#### Umiejętność 2 (×2): Kufer Kurierski - Gadżet Burzący

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Obuch |          3 |         +4 |      3 |           +3 |    1 |
|          3 | Obżar. | Obuch |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania [Rozdarcie] i Licznika [Rozdarcie] nakładają 2 [Spadek Poziomu Obrony] (1 raz na monetę)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Kufer Kuriera - Sinclair]  
- Przy mniej niż 15 [Kufer Kuriera - Sinclair] zyskuje dodatkowo 2 [Kufer Kuriera - Sinclair]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]

*Od ulepszenia 2:* Przy 10+ [Kufer Kuriera - Sinclair], albo gdy cel ma 6+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania [Rozdarcie] i Licznika [Rozdarcie] nakładają 2 [Spadek Poziomu Obrony] (1 raz na monetę)  
[Przy Użyciu] Przy 20 lub mniej [Kufer Kuriera - Sinclair] zyskuje 1 [Pośpiech] w następnej turze (maks. 1 raz na turę)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Kufer Kuriera - Sinclair]  
- Przy mniej niż 15 [Kufer Kuriera - Sinclair] zyskuje dodatkowo 2 [Kufer Kuriera - Sinclair]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Rozdarcie]  
- Przy 15+ [Kufer Kuriera - Sinclair] zwiększa Licznik [Rozdarcie] o 1  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
- Przy 15+ [Kufer Kuriera - Sinclair] zwiększa Licznik [Rozdarcie] o 1

*Od ulepszenia 4:* Moc Monet +1 za każde 10 [Kufer Kuriera - Sinclair] albo za każde 6 [Rozdarcie] celu (maks. 2)  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania [Rozdarcie] i Licznika [Rozdarcie] nakładają 2 [Spadek Poziomu Obrony] (1 raz na monetę)  
[Przy Użyciu] Przy 30 lub mniej [Kufer Kuriera - Sinclair] zyskuje 1 [Pośpiech] w następnej turze (maks. 1 raz na turę)  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Kufer Kuriera - Sinclair]  
- Przy mniej niż 15 [Kufer Kuriera - Sinclair] zyskuje dodatkowo 2 [Kufer Kuriera - Sinclair]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Rozdarcie]  
- Przy 15+ [Kufer Kuriera - Sinclair] zwiększa Licznik [Rozdarcie] o 2  
Moneta 3: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
- Przy 15+ [Kufer Kuriera - Sinclair] zwiększa Licznik [Rozdarcie] o 2

#### Umiejętność 3 (×1): Południca... Ufam Ci!

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Obuch |          5 |         +4 |      3 |           +5 |    1 |

*Od ulepszenia 3:* Przy 10+ [Kufer Kuriera - Sinclair], albo gdy cel ma 6+ [Rozdarcie], Moc Monet +1  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania [Rozdarcie] i Licznika [Rozdarcie] zwiększają Moc Monet ostatniej monety o +2  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie], zadaje +3% obrażeń za każde 1 [Kufer Kuriera - Sinclair] (maks. 90%)  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Rozdarcie] o 1  
- Zwiększa dodatkowo Licznik [Rozdarcie] o 1 za każde 10 [Kufer Kuriera - Sinclair] (maks. 2)  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
- Nakłada dodatkowo 1 [Rozdarcie] za każde 10 [Kufer Kuriera - Sinclair] (maks. 2)  
Moneta 3: [Przy Trafieniu] Jeżeli efekt zwiększania Mocy Monet ostatniej monety nie zadziałał, zyskuje 1 [Pośpiech] w następnej turze

*Od ulepszenia 4:* Moc Monet +1 za każde 10 [Kufer Kuriera - Sinclair] albo za każde 6 [Rozdarcie] celu (maks. 2)  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie] i 3+ Licznika [Rozdarcie], efekty trafienia tej Umiejętności zamiast nakładania [Rozdarcie] i Licznika [Rozdarcie] zwiększają Moc Monet ostatniej monety o +4  
[Przy Użyciu] Jeżeli cel ma 15+ [Rozdarcie], zadaje +4% obrażeń za każde 1 [Kufer Kuriera - Sinclair] (maks. 120%)  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Rozdarcie] o 1  
- Zwiększa dodatkowo Licznik [Rozdarcie] o 1 za każde 10 [Kufer Kuriera - Sinclair] (maks. 3)  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Rozdarcie]  
- Nakłada dodatkowo 1 [Rozdarcie] za każde 8 [Kufer Kuriera - Sinclair] (maks. 4)  
Moneta 3: [Przy Trafieniu] Jeżeli efekt zwiększający Moc Monet ostatniej monety tej Umiejętności nie uruchomił się, zyskuje 2 [Pośpiech] w następnej turze

#### Obrona: System Wsparcia Dostaw i Kontroli Sytuacji

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | obrona: kontra |          9 |         +7 |      1 |           +3 |    1 |

*Od ulepszenia 1:* [Początek Walki] Przy 15+ [Kufer Kuriera - Sinclair] stosuje się jako „Z-zaraz, muszę coś wyregulować...!” (1 raz na turę)  
[Początek Walki] Jeżeli Umiejętność ma się uruchomić, zyskuje Tarczę równą ([Kufer Kuriera - Sinclair]/2)% Maks. HP (maks. 15%, 1 raz na turę)

*Od ulepszenia 4:* [Początek Walki] Przy 15+ [Kufer Kuriera - Sinclair] stosuje się jako „Z-zaraz, muszę coś wyregulować...!” (1 raz na turę)  
[Początek Walki] Jeżeli Umiejętność ma się uruchomić, zyskuje Tarczę równą ([Kufer Kuriera - Sinclair])% Maks. HP (maks. 25%, 1 raz na turę)

#### Obrona: Z-zaraz, muszę coś wyregulować...!

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | obrona: kontra |          9 |         +7 |      1 |           +3 |    1 |

*Od ulepszenia 1:* [Początek Walki] Jeżeli Umiejętność ma się uruchomić, zyskuje Tarczę równą ([Kufer Kuriera - Sinclair]/2)% Maks. HP (maks. 15%, 1 raz na turę)  
[Koniec Tury] Uruchamia [Tryb Strategicznego Odpoczynku]

*Od ulepszenia 4:* [Początek Walki] Jeżeli Umiejętność ma się uruchomić, zyskuje Tarczę równą ([Kufer Kuriera - Sinclair])% Maks. HP (maks. 25%, 1 raz na turę)  
[Koniec Tury] Uruchamia [Tryb Strategicznego Odpoczynku]

#### Pasywka bojowa: Następnym razem dowieziemy porządnie...

*od ulepszenia 1*

\<Na walki łańcuchowe> Gdy po Odwrócie wywołanym przez „[Tryb Strategicznego Odpoczynku]” jednostka ponownie przystępuje do walki, zmniejsza [Kufer Kuriera - Sinclair] o połowę (1 raz na spotkanie, zaokrąglone w górę)

#### Pasywka bojowa: Następnym razem dowieziemy porządnie...

*od ulepszenia 2*

\<Na walki łańcuchowe> Gdy po Odwrócie wywołanym przez „[Tryb Strategicznego Odpoczynku]” jednostka ponownie przystępuje do walki, zmniejsza [Kufer Kuriera - Sinclair] o połowę (1 raz na spotkanie, zaokrąglone w górę)

#### Pasywka bojowa: Chwileczkę, proszę...

*od ulepszenia 2; posiadane 4× Obżar.*

Na początku tury, przy Szybkości 6 lub wyższej, albo przy posiadaniu [Pośpiech], zyskuje Tarczę równą ([Kufer Kuriera - Sinclair])% Maks. HP (maks. 20%)

#### Pasywka bojowa: Następnym razem dowieziemy porządnie...

*od ulepszenia 4*

\<Na walki łańcuchowe> Gdy po Odwrócie wywołanym przez „[Tryb Strategicznego Odpoczynku]” jednostka ponownie przystępuje do walki, zmniejsza [Kufer Kuriera - Sinclair] o połowę (1 raz na spotkanie, zaokrąglone w górę)

#### Pasywka bojowa: Chwileczkę, proszę...

*od ulepszenia 4; posiadane 4× Obżar.*

Na początku tury, przy Szybkości 6 lub wyższej, albo przy posiadaniu [Pośpiech], zyskuje Tarczę równą ([Kufer Kuriera - Sinclair])% Maks. HP (maks. 20%)  
Przy Odwrócie nakłada 1 [Wzrost Mocy Starcia] w następnej turze na 2 Sojuszników (najpierw Tożsamości, które Weszły z rezerwy, następnie w kolejności przydziału)  
- Wydłuża trwanie o 1 turę za każde 15 [Kufer Kuriera - Sinclair] (maks. o 2 tury)

#### Pasywka wsparcia: Szybka Kurierka

*od ulepszenia 3; posiadane 6× Obżar.*

Gdy 1 Sojusznik z najwyższą Szybkością trafi wroga z [Rozdarcie], nakłada 1 [Spadek Poziomu Obrony] (maks. 3 razy na wroga na turę)

#### Kwestie

- **Identity Acquisition:** I think I can lump this package with that one, and... let's see where this one's gotta go... W-why is the sorting process so complicated this time?
- **Morning Greeting:** I haven't been sleeping well, with the recent surge of late-night delivery contracts... I'll try to get some sleep in now.
- **Afternoon Greeting:** Boxed lunches usually end up freezing solid when we're making deliveries through the cold. That's why some Fixers keep their lunches in the Courier Trunks they've been assigned, but... that's a violation of the Devyat' Association rules...
- **Evening Greeting:** It's dangerous to travel at night, but... I don't have a choice. There's a package that needs to be delivered before the Night in the Backstreets.
- **Chatter #1:** It's important for Fixers of the Devyat' Association to keep themselves up-to-date about cultures of each District. Speed is one thing, but we also have to be careful not to accidentally break a Taboo of a Wing or a Syndicate's rule.
- **Chatter #2:** Why don't I just drive there, you ask? Um... I'm pretty sure going on foot and following Poludnitsa's shortcut directions would get me there much faster than driving would.
- **Chatter #3:** I can survive most risky situations by having Poludnitsa disengage the output threshold. But that'll deduct way too much money from my payout... If it doesn't kill me in the process.
- **Post-Uptie Chat 1:** *[Possible delivery delay detected: Syndicate altercation 200m ahead. Rerouting.]* Lots of route adjustments today, huh... Left turn, then? *[New route discovered; navigating courier.]* You want me to... *scale* the building?!
- **Post-Uptie Chat 2:** Only lower-rung Syndicate henchmen who don't know about these dimensional bags are dumb enough to attack us. Courier Trunks are locked by Protection Mode anyway, so... Oh, what about members of the Fingers? They're... we usually meet them as our clients.
- **Idle:** Poludnitsa, I'm bored. Can you play me a song? *[Poludnitsa does not support the requested functionality.]* Huh? But Miss Rodya said— *[Correction. This AI model does not support the requested functionality.]*
- **Uptying:** Ugh, I really hoped it wouldn't have to come to this, but I need to get there in time...! Poludnitsa, engage mode conversion! *[Hammer mode engaged. Swing to the undulation of decay particles.]*
- **Deployment:** Is it a new delivery order?
- **Stage Entry:** My next destination is...
- **Viewed in Battle:** Uh... did you call me? Oh, did you order something through the Devyat'?
- **Commencing Attack:** I still have time...
- **Enemy Stagger:** Can you clear the way, please...?
- **Staggered:** Nngh...
- **Enemy Killed:** ... I said move!
- **Death #1:** Poludnitsa... help... *[Pathfinding failed. Courier absence detected. Poludnitsa, engaging Protection Mode.]*
- **Death #2:** N-no! Please, please give me another chance! I've never been late bef— *[Update. Delivery failed. The courier will be collected shortly. Thank you for your service. Poludnitsa, engaging Protection Mode.]*
- **Check Passed:** ... I'm not running an errand like this for you again.
- **Check Failed:** I-I'm busy, okay?
- **Victory Cry:** AAAHHHHH! Your package has been delivered! I'm not late, am I? I'm on time for the delivery, right?
- **Extra Conditions Fulfilled:** This package will be delivered earlier than expected. The client will be happy to hear that.
- **Defeat Wail:** Pant... pant... I-I'm almost there, Poludnitsa! I just need five more minutes, please...!

### 000 Środkowego Młodsza Siostra — Sinclair

> Dwunasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 0                                                           |
| HP                        | 92 (+3,05 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom +5                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×2 (Fatal), Obuch ×0,5 (Endured) |
| Progi Stagger (HP)        | 50% / 20%                                                   |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Middle_Finger                                               |
| Słowa kluczowe            | Krwawienie                                                  |
| Data aktualizacji         | 20250403                                                    |

#### Umiejętność 1 (×3): To ty?!

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Obuch |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Obżar. | Obuch |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 2 w następnej turze  
[Przy Użyciu] Odzyskuje 5 Poczytalności  
Moneta 1: [Trafienie Awersem] Nakłada 1 [Krwawienie]  
Moneta 2: [Trafienie Awersem] Nakłada 1 [Krwawienie]

*Od ulepszenia 2:* Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 3 w następnej turze  
[Przy Użyciu] Odzyskuje 5 Poczytalności  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

*Od ulepszenia 4:* Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 5 w następnej turze  
[Przy Użyciu] Odzyskuje 5 Poczytalności  
- Przy pełnej Poczytalności zamiast tego Moc Starcia +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

#### Umiejętność 2 (×2): Zwróć z Nawiązką

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | Obuch |          4 |         +3 |      3 |           +3 |    1 |
|          3 | Zawiść | Obuch |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 2 w następnej turze  
[Początek Walki] Ta Umiejętność zyskuje (najwyższy Rezonans / 3) Poziomu Ataku (maks. 2, zaokrąglone w dół)  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 3: Przy Rezonansie 4+, w skład którego wchodzi ta Umiejętność, zadaje +10% obrażeń

*Od ulepszenia 2:* Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 3 w następnej turze  
[Początek Walki] Ta Umiejętność zyskuje (najwyższy Rezonans / 2) Poziomu Ataku (maks. 3, zaokrąglone w dół)  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 3: Przy Rezonansie 4+, w skład którego wchodzi ta Umiejętność, zadaje +15% obrażeń

*Od ulepszenia 4:* Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Zwiększa [Wartość Prowokacji] tego slotu o 5 w następnej turze  
[Początek Walki] Ta Umiejętność zyskuje (najwyższy Rezonans / 2) Poziomu Ataku (maks. 3, zaokrąglone w dół)  
- Jeżeli ten Rezonans zawiera Pełny Rezonans, zyskany tą efektem wartość Poziomu Ataku podwaja się  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 3: Przy Rezonansie 3+, w skład którego wchodzi ta Umiejętność, zadaje +20% obrażeń

#### Umiejętność 3 (×1): Zapisz Wszystkich

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Zawiść | Obuch |          5 |         +3 |      3 |           +4 |    1 |
|          4 | Zawiść | Obuch |          5 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 3:* Zadaje +1% obrażeń za każde 2 [Rejestr Odwetu [Sinclair]] (maks. 15%)  
Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Początek Walki] Ta Umiejętność zyskuje (najwyższy Rezonans / 2) Poziomu Ataku (maks. 3, zaokrąglone w dół)  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 3: Zadaje +2.5% obrażeń za każdy Rezonans, w skład którego wchodzi ta Umiejętność (maks. 15%)  
Moneta 3: Zadaje +7.5% obrażeń za każde 10 [Rejestr Odwetu [Sinclair]] (maks. 22.5%)

*Od ulepszenia 4:* Zadaje +1% obrażeń za każde 1 [Rejestr Odwetu [Sinclair]] (maks. 30%)  
Moc Monet +1 za każde 6 [Krwawienie] celu (maks. 2)  
[Początek Walki] Ta Umiejętność zyskuje (najwyższy Rezonans / 2) Poziomu Ataku (maks. 3, zaokrąglone w dół)  
- Jeżeli ten Rezonans zawiera Pełny Rezonans, zyskany tą efektem wartość Poziomu Ataku podwaja się  
Moneta 2: [Przy Trafieniu] Nakłada 4 [Krwawienie]  
Moneta 3: Zadaje +5% (maks. 30%) obrażeń za każdy Rezonans, w skład którego wchodzi ta Umiejętność  
Moneta 3: Zadaje +15% (maks. 45%) obrażeń za każde 10 [Rejestr Odwetu [Sinclair]]

#### Obrona: Rozgrzewka na Wschodzie

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | obrona: kontra |          5 |         +4 |      2 |           +5 |    1 |

*Od ulepszenia 1:* [Początek Walki] Zyskuje Tarczę równą 20% brakującego HP (1 raz na turę)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

*Od ulepszenia 4:* [Początek Walki] Zachowanie Umiejętności zmienia się zależnie od sumy Pełnych Rezonansów Zazdrości:  
- Przy sumie 4+ stosuje „Zwróć z Nawiązką” jako Kontrę  
- Przy sumie 6+ stosuje „Zapisz Wszystkich” jako Kontrę  
(uruchamia się od lewego slotu na panelu; maks. 2 razy na turę)  
[Początek Walki] Zyskuje Tarczę równą 30% brakującego HP (1 raz na turę)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

#### Obrona: 1101205

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Zawiść | obrona: kontra |          4 |         +3 |      3 |           +3 |    1 |
|          3 | Zawiść | obrona: kontra |          4 |         +4 |      3 |           +3 |    1 |

#### Obrona: 1101206

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Zawiść | obrona: kontra |          5 |         +3 |      3 |           +4 |    1 |
|          4 | Zawiść | obrona: kontra |          5 |         +4 |      3 |           +4 |    1 |

#### Pasywka bojowa: Środkowy Nigdy Nie Zapomina

*od ulepszenia 2; posiadane 3× Zawiść*

Za każdym razem, gdy zostaje zaatakowana przez wroga, nakłada 3 [Cel Zemsty] na agresora (lub Party) (1 raz na turę)  
  
Za każdym razem, gdy inny sojusznik zostaje zaatakowany przez wroga, nakłada 2 [Cel Zemsty] na agresora (lub Party) (1 raz na turę na Tożsamość)  
  
Na koniec ataku podstawową Umiejętnością ataku albo Umiejętnością Kontry zużywa cały [Cel Zemsty] celu  
- Za każde zużycie [Cel Zemsty] wroga zyskuje tyle samo [Rejestr Odwetu [Sinclair]]

#### Pasywka bojowa: Środkowy Nigdy Nie Zapomina

*od ulepszenia 4; posiadane 3× Zawiść*

Za każdym razem, gdy zostaje zaatakowana przez wroga, nakłada 5 [Cel Zemsty] na agresora (lub Party) (1 raz na turę)  
  
Za każdym razem, gdy inny sojusznik zostaje zaatakowany przez wroga, nakłada 2 [Cel Zemsty] na agresora (lub Party) (1 raz na turę na Tożsamość)  
- Jeżeli ten sojusznik należy do Środkowego, nakłada dodatkowo 3 [Cel Zemsty]  
  
Na koniec ataku podstawową Umiejętnością ataku albo Umiejętnością Kontry zużywa cały [Cel Zemsty] celu  
- Za każde zużycie [Cel Zemsty] wroga zyskuje tyle samo [Rejestr Odwetu [Sinclair]]

#### Pasywka wsparcia: Mamy twoje plecy

*od ulepszenia 3; posiadane 5× Zawiść*

Na początku walki 1 Sojusznik z najniższym procentem obecnego HP zyskuje 2 [Wzrost Poziomu Obrony]

#### Pasywka wsparcia: Mamy twoje plecy

*od ulepszenia 4; posiadane 5× Zawiść*

Na początku walki 1 Sojusznik z najniższym procentem obecnego HP zyskuje 2 [Wzrost Poziomu Obrony]  
- Jeżeli ten sojusznik należy do Środkowego, dodatkowo zyskuje 2 [Wzrost Poziomu Ataku]

#### Kwestie

- **Identity Acquisition:** We crossed off everyone on the list for today, and... Alright, time to tell Big Brother we’re all set to chase down those hair coupon thieves.
- **Morning Greeting:** Uh-huh. Good morning to you, too. ... Hey, just a heads-up, apparently the Great Sister's coming down to join us during mealtime. ... Don't freak out, I'll be right there with you for the prep.
- **Afternoon Greeting:** Sorry, I won't be joining for lunch today. Gotta start getting ready to head east.
- **Evening Greeting:** All good? Phew... it's sundown already, huh. Looks like the Young Brother's gone out to check on our 'businesses', and... we're... hm. Let's start by taking care of some easier targets in the Book. We'll have to clear our schedule if we want to keep up with the Big Brother.
- **Chatter #1:** It's one of those Restructuring Days at H Corp. soon, isn't it? That'll get all the vermin hiding in the Backstreets maze to come out crawling... Disgusting fugitives of the Book of Vengeance, wastes of paper... Let's take this chance to clear out the trash.
- **Chatter #2:** Normally, this would fall under our eastern family's jurisdiction, but... our Big Brother was dead set on personally handling this specific case.
- **Chatter #3:** Looks like... some District 8 family's Vengeance list has been added to our own. Right, so we take care of these guys, and they'll overlook us starting a ruckus in the east, huh. What was that saying again? We scratch their backs, and they scratch ours, yeah.
- **Post-Uptie Chat 1:** You're making things hard for both of us. Why don't you just accept your punishment instead of fighting back and making a mess? You know that once your name's in the book, the Middle'll stop at nothing to track you down wherever you go, right?
- **Post-Uptie Chat 2:** They're really doing us a solid by letting these one or two favors pay for our Big Brother's request. Awfully generous of them. We should gift them some expensive Boluses as thanks, at least...
- **Idle:** ... Would you like some recommendations on places to visit in District 8, Big Bro?
- **Uptying:** Aha... Yeah, yeah. Pipe down, one at a time. Where's Big Brother headed to again?
- **Deployment:** You can count on me to guide your way through H Corp. and District 8.
- **Stage Entry:** Let's take care of one Vengeance at a time.
- **Viewed in Battle:** Who meddles in our business?
- **Commencing Attack:** I'll pummel them to dust.
- **Enemy Stagger:** Don't resist.
- **Staggered:** You... little... shit!
- **Enemy Killed:** ... Nice, now I can cross that off the book.
- **Death:** Heh... heh. Killing me won't clear your name off the book.
- **Check Passed:** I am glad you found my guidance helpful, Big Bro.
- **Check Failed:** ... Why don't we just break this thing in half?
- **Victory Cry:** We finally had our vengeance, but many of the family died in the process. Even those that I shared a meal with just a few hours ago... I'll... avenge you, I swear I will.
- **Extra Conditions Fulfilled:** Big Brother gave us some tortoise Boluses as a reward for a job well done. Here's some info for the Brothers and Sisters who've never been to District 8 before—these things are pretty darn rare. So consider yourselves lucky.
- **Defeat Wail:** ... I don't care that we failed. It's my failure, not the Middle's. And the Middle always pays its debts.

### 000 Kciuk Wschodni Soldato II — Sinclair

> Trzynasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 6                                                           |
| HP                        | 79 (+2,96 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×2 (Fatal), Kłucie ×0,5 (Endured), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                             |
| Grzech wyróżniony         | Gniew                                                       |
| Przynależność             | Thumb_Finger                                                |
| Słowa kluczowe            | Podpalenie, Wstrząs                                         |
| Data aktualizacji         | 20250619                                                    |

#### Umiejętność 1 (×3): Zgodnie z Etykietą.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Kłucie |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Żądza  | Kłucie |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]

*Od ulepszenia 2:* [Przy Użyciu] Moc Monet +1 za każde 6 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]

*Od ulepszenia 4:* [Przy Użyciu] Moc Monet +1 za każde 6 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Jeżeli [Wstrząs] celu jest „Wstrząsem Specjalnym”, Moc Starcia +1  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Wstrząs]

#### Umiejętność 2 (×2): Szacunek dla Kciuka.

| Ulepszenie | Grzech   | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Kłucie |          4 |         +5 |      2 |           +3 |    1 |
|          3 | Lenistwo | Kłucie |          4 |         +6 |      2 |           +3 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Wstrząs]), Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Wstrząs]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma 6+ [Wstrząs], wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

*Od ulepszenia 2:* [Przy Użyciu] Moc Monet +1 za każde 6 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Wstrząs]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma 10+ [Wstrząs - Żar], zwiększa Licznik [Podpalenie] celu o 1  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma 6+ [Wstrząs], wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

*Od ulepszenia 4:* [Przy Użyciu] Moc Monet +1 za każde 6 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Zadaje +10% obrażeń za każde 4 (suma [Podpalenie] i [Wstrząs] celu) (maks. 30%)  
[Przy Użyciu] Jeżeli cel ma 10+ „Wstrząsu Specjalnego”, Moc Bazowa +2  
Moneta 1: [Przy Trafieniu] Nakłada 2 [Wstrząs]  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma 10+ [Wstrząs - Żar], zwiększa Licznik [Podpalenie] celu o 2  
Moneta 2: [Przy Trafieniu] Jeżeli cel ma 6+ [Wstrząs], wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

#### Umiejętność 3 (×1): Sprężanie Ciągu

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |          4 |         +4 |      3 |           +5 |    1 |
|          4 | Gniew  | Cięcie |          5 |         +4 |      3 |           +5 |    1 |

*Od ulepszenia 3:* [Przy Użyciu] Moc Monet +1 za każde 8 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Przy 3+ [Żarzący się Pocisk Napędowy] Moc Bazowa +1  
Moneta 1: Zużywa 1 [Żarzący się Pocisk Napędowy]  
Moneta 1: Jeżeli tym efektem monety zużyto [Żarzący się Pocisk Napędowy], zadaje +20% obrażeń  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 2  
Moneta 1: [Przy Trafieniu] Wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar]  
Moneta 2: Zużywa 1 [Żarzący się Pocisk Napędowy]  
Moneta 2: Jeżeli tym efektem monety zużyto [Żarzący się Pocisk Napędowy], zadaje +20% obrażeń  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 3: Zużywa 1 [Żarzący się Pocisk Napędowy]  
Moneta 3: Jeżeli tym efektem monety zużyto [Żarzący się Pocisk Napędowy], zadaje +20% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 3: [Przy Trafieniu] Nakłada 4 [Podpalenie]  
Moneta 3: [Przy Trafieniu] Wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1  
Moneta 3: [Przy Trafieniu] Jeżeli zużyto [Żarzący się Pocisk Napędowy], wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

*Od ulepszenia 4:* [Przy Użyciu] Moc Monet +1 za każde 8 (suma [Podpalenie] i [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Przy 3+ [Żarzący się Pocisk Napędowy] Moc Bazowa +3, zadaje +30% obrażeń, a monety stają się [Moneta Niezniszczalna]ami  
Moneta 1: Zużywa 1 [Żarzący się Pocisk Napędowy]  
Moneta 1: Jeżeli tym efektem monety zużyto [Żarzący się Pocisk Napędowy], zadaje +25% obrażeń  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 3  
Moneta 1: [Przy Trafieniu] Wywołuje [Konwersja Amplitudy] do [Wstrząs - Żar]  
Moneta 2: Zużywa 1 [Żarzący się Pocisk Napędowy]  
Moneta 2: Jeżeli tym efektem monety zużyto [Żarzący się Pocisk Napędowy], zadaje +25% obrażeń  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Podpalenie]  
Moneta 3: Zużywa 1 [Żarzący się Pocisk Napędowy]  
Moneta 3: Jeżeli tym efektem monety zużyto [Żarzący się Pocisk Napędowy], zadaje +25% obrażeń  
Moneta 3: [Przy Trafieniu] Nakłada +1 Licznika [Wstrząs]  
Moneta 3: [Przy Trafieniu] Nakłada 4 [Podpalenie]  
Moneta 3: [Przy Trafieniu] Wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1  
Moneta 3: [Przy Trafieniu] Jeżeli zużyto [Żarzący się Pocisk Napędowy], wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1  
Moneta 3: [Przy Trafieniu] Jeżeli ta Umiejętność zużyła 3 [Żarzący się Pocisk Napędowy], wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

#### Obrona: Obrona Żelaza

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |          9 |         +6 |      1 |           +3 |    1 |
|          4 | Pycha   | obrona: blok |          9 |         +6 |      1 |           +3 |    1 |

*Od ulepszenia 1:* Przy otrzymaniu ataku, dopóki ma Tarczę, nakłada 1 [Wstrząs] na agresora za każdym razem (uruchamia się 3 razy na turę)

*Od ulepszenia 4:* Przy otrzymaniu ataku, dopóki ma Tarczę, nakłada 2 [Wstrząs] na agresora za każdym razem (uruchamia się 4 razy na turę)

#### Pasywka bojowa: Bagnet

*od ulepszenia 2*

Zawsze aktywne: rozpoczyna spotkania z 15 [Żarzący się Pocisk Napędowy]  
  
Jeżeli zużyto [Żarzący się Pocisk Napędowy] Umiejętnościami albo pasywkami, zyskuje tyle [Wzrost Obrażeń], ile zużyto, w następnej turze (maks. 3)  
  
Przy rzucie monetą zużywającą [Żarzący się Pocisk Napędowy] atak nie zostaje odwołany, nawet gdy nie ma już [Żarzący się Pocisk Napędowy], ale efekty trafienia tej monety „nakłada [Podpalenie]” i „zwiększa Licznik [Podpalenie]” nie uruchamiają się

#### Pasywka bojowa: Trybut Amunicji

*od ulepszenia 2; rezonans 3× Pycha*

Gdy zakończy atak 1 Sojusznik przydzielony najwcześniej na pozycji wśród Tożsamości używających [Amunicja], jeżeli jego obecny Licznik [Amunicja] wynosi mniej niż połowę (zaokrąglone w górę), zużywa tyle własnego [Żarzący się Pocisk Napędowy], ile wynosi łączna liczba zużytych przez tę jednostkę [Amunicja], i uzupełnia tyle [Amunicja], których ta jednostka używa, ile zużyto [Żarzący się Pocisk Napędowy]. (maks. zużycie: 3) (1 raz na spotkanie)  
  
- Jeżeli otrzymującym [Amunicja] Tożsamością jest Tożsamość Kciuka o wyższej randze, uzupełnia dodatkowo 1 [Amunicja], których ta jednostka używa  
- [Amunicja] z oddzielnymi wartościami Mocy i Licznika uzupełnia losowo  
- Jeżeli Moc albo Licznik osiągnęły wartość maksymalną, uzupełnia tym [Amunicja], którego wartość nie jest maksymalna

#### Pasywka bojowa: Bagnet

*od ulepszenia 3*

Zawsze aktywne: rozpoczyna spotkania z 15 [Żarzący się Pocisk Napędowy]  
  
Jeżeli zużyto [Żarzący się Pocisk Napędowy] Umiejętnościami albo pasywkami, zyskuje tyle [Wzrost Obrażeń], ile zużyto, w następnej turze (maks. 3)  
  
Przy rzucie monetą zużywającą [Żarzący się Pocisk Napędowy] atak nie zostaje odwołany, nawet gdy nie ma już [Żarzący się Pocisk Napędowy], ale efekty trafienia tej monety „nakłada [Podpalenie]” i „zwiększa Licznik [Podpalenie]” nie uruchamiają się

#### Pasywka bojowa: Trybut Amunicji

*od ulepszenia 3; rezonans 3× Pycha*

Gdy zakończy atak 1 Sojusznik przydzielony najwcześniej na pozycji wśród Tożsamości używających [Amunicja], jeżeli jego obecny Licznik [Amunicja] wynosi mniej niż połowę (zaokrąglone w górę), zużywa tyle własnego [Żarzący się Pocisk Napędowy], ile wynosi łączna liczba zużytych przez tę jednostkę [Amunicja], i uzupełnia tyle [Amunicja], których ta jednostka używa, ile zużyto [Żarzący się Pocisk Napędowy]. (maks. zużycie: 3) (1 raz na spotkanie)  
  
- Jeżeli otrzymującym [Amunicja] Tożsamością jest Tożsamość Kciuka o wyższej randze, uzupełnia dodatkowo 1 [Amunicja], których ta jednostka używa  
- [Amunicja] z oddzielnymi wartościami Mocy i Licznika uzupełnia losowo  
- Jeżeli Moc albo Licznik osiągnęły wartość maksymalną, uzupełnia tym [Amunicja], którego wartość nie jest maksymalna

#### Pasywka bojowa: Bagnet

*od ulepszenia 4*

Zawsze aktywne: rozpoczyna spotkania z 15 [Żarzący się Pocisk Napędowy]  
  
Jeżeli zużyto [Żarzący się Pocisk Napędowy] Umiejętnościami albo pasywkami, zyskuje tyle [Wzrost Obrażeń], ile zużyto, w następnej turze (maks. 3)  
  
Przy rzucie monetą zużywającą [Żarzący się Pocisk Napędowy] atak nie zostaje odwołany, nawet gdy nie ma już [Żarzący się Pocisk Napędowy], ale efekty trafienia tej monety „nakłada [Podpalenie]” i „zwiększa Licznik [Podpalenie]” nie uruchamiają się

#### Pasywka bojowa: Trybut Amunicji

*od ulepszenia 4; rezonans 3× Pycha*

Gdy zakończy atak 1 Sojusznik przydzielony najwcześniej na pozycji wśród Tożsamości używających [Amunicja], jeżeli jego obecny Licznik [Amunicja] wynosi mniej niż połowę (zaokrąglone w górę), zużywa tyle własnego [Żarzący się Pocisk Napędowy], ile wynosi łączna liczba zużytych przez tę jednostkę [Amunicja], i uzupełnia tyle [Amunicja], których ta jednostka używa, ile zużyto [Żarzący się Pocisk Napędowy]. (maks. zużycie: 5) (1 raz na spotkanie)  
  
- Jeżeli otrzymującym [Amunicja] Tożsamością jest Tożsamość Kciuka o wyższej randze, uzupełnia dodatkowo 1 [Amunicja], których ta jednostka używa  
- [Amunicja] z oddzielnymi wartościami Mocy i Licznika uzupełnia losowo  
- Jeżeli Moc albo Licznik osiągnęły wartość maksymalną, uzupełnia tym [Amunicja], którego wartość nie jest maksymalna

#### Pasywka wsparcia: Przeładowanie

*od ulepszenia 3; rezonans 4× Pycha*

Gdy zakończy atak 1 Sojusznik przydzielony najwcześniej na pozycji wśród Tożsamości używających [Amunicja], jeżeli jego obecny Licznik [Amunicja] wynosi mniej niż połowę, odzyskuje połowę maksymalnej pojemności [Amunicja] (zaokrąglone w górę; 1 raz na spotkanie; maks. odzysk [Amunicja]: 5)  
  
- [Amunicja] z oddzielnymi wartościami Mocy i Licznika odzyskuje losowo  
- Jeżeli Moc albo Licznik [Amunicja] osiągnęły wartość maksymalną, odzyskuje tym [Amunicja], którego wartość nie jest maksymalna  
- Ten efekt nie uruchamia się, gdy nie ma Tożsamości używających [Amunicja]

#### Kwestie

- **Identity Acquisition:** I listen carefully to every order I'm given. I... just look to the ground to not risk staring at my superiors straight in their eyes.
- **Morning Greeting:** ... Sun's up. Time to collect some protection fees. If I don't get right on it, my superiors might be compelled to act, and that's... well, I wouldn't deserve to be a member of The Thumb if I let that happen.
- **Afternoon Greeting:** Lunch is still a while away for me. Soldato Terzo and Quarto, my superiors, have to finish eating their meals first before I eat dinner.
- **Evening Greeting:** I usually study other Syndicates at night, trying to learn more about companies and organizations' internal structure to gauge their hierarchy. I have to... try my best to uphold the perfect manners and etiquette.
- **Chatter #1:** Hm. I think I can leave the ammo-cleaning job for the Soldato Primo juniors. I'm a Soldato Secondo, you know...? It's about time I moved away from ammo cleaning duty to something more important, like ammo carrying duty for the esteemed Capos.
- **Chatter #2:** It's important to learn how to think before we speak. Treating punished tongues or jaws can get pretty expensive. Well... sure, replacing them with prosthetics can be a lot cheaper. I don't like it, though...
- **Chatter #3:** ... Anyone in The Thumb has to know how to wield bayonets. Nothing like the sharp blade and the hard stock of a rifle in situations when we can't use ammunition. It's also something The Thumb's eastern branch specializes in, in combination with the usage of propellant rounds... so we're pretty good at it.
- **Post-Uptie Chat 1:** The Thumb is very gentlemanly. We don't subscribe to the patternless Prescripts, vicious philosophies on art, or a sense of brotherhood that's more akin to chains. There's nothing difficult about what we do, right? It's just a recognition of the accomplishments, and giving them the respect they deserve.
- **Post-Uptie Chat 2:** Primo, Secondo, Terzo, Quarto. Even within the same ranks there exists distinctly tiered subdivisions. It's those details that allow us to be more... gentlemanly and courteous toward anyone we come across.
- **Idle:** ... Speaking thoughtlessly is a good way to display bad manners. Even by accident.
- **Uptying:** Daring to breathe when you haven't even followed the underboss's command? Now that's quite discourteous.
- **Deployment:** I will await your next command at this spot.
- **Stage Entry:** As you command.
- **Viewed in Battle:** Progressing through the mission as commanded.
- **Commencing Attack:** I will follow your command.
- **Enemy Stagger:** We all have our lots...
- **Staggered:** So, in this life dedicated to propriety...
- **Enemy Killed:** ... there's no need for sympathy, mutual or otherwise.
- **Death:** I don't think I was discourteous...
- **Check Passed:** Mission completed as ordered.
- **Check Failed:** ... I failed to complete my duties. This is but a punishment I deserve.
- **Victory Cry:** That wasn't perfect, but I completed every one of your orders! I hope... you like it.
- **Extra Conditions Fulfilled:** I am honored to report that we have achieved a most perfect victory! All credits go to my superiors, including the manager.
- **Defeat Wail:** I won't blame anyone else or make excuses. ... I must pay for my inadequacies.

### 000 Wataha Heishou - Gałąź You — Sinclair

> Czternasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 6                                                           |
| HP                        | 75 (+2,5 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom −4                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×1 (Normal), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 65% / 35% / 15%                                             |
| Grzech wyróżniony         | Żądza                                                       |
| Przynależność             | Black_Beast_Chicken, H_Corp                                 |
| Słowa kluczowe            | Rozdarcie, Podpalenie                                       |
| Data aktualizacji         | 20250828                                                    |

#### Umiejętność 1 (×3): O, Zapach Płonącej Krwi...

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Żądza  | Cięcie |          2 |         +2 |      3 |           +1 |    1 |
|          3 | Żądza  | Cięcie |          2 |         +3 |      3 |           +1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1

*Od ulepszenia 2:* [Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Rozdarcie]), Moc Monet +1  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Rozdarcie]), Moc Monet +1  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Trafienie Awersem] Nakłada 1 [Podpalenie]  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 3: [Trafienie Awersem] Zwiększa Licznik [Rozdarcie] celu o 1

#### Umiejętność 2 (×2): ... Rozpal moją Furię.

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Cięcie |          3 |         +3 |      3 |           +2 |    1 |
|          3 | Obżar. | Cięcie |          3 |         +4 |      3 |           +2 |    1 |
|          4 | Obżar. | Cięcie |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Trafienie Awersem] Jeżeli ma [Krwawy Płomień [血炎]], albo jej obecne HP jest poniżej 50% Maks. HP, ponownie używa tę monetę (1 raz na Umiejętność)

*Od ulepszenia 2:* [Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Rozdarcie]), Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Trafienie Awersem] Jeżeli ma [Krwawy Płomień [血炎]], albo jej obecne HP jest poniżej 50% Maks. HP, ponownie używa tę monetę (1 raz na Umiejętność)

*Od ulepszenia 4:* [Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Rozdarcie]), Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 1: [Trafienie Awersem] Zwiększa Licznik [Rozdarcie] celu o 1  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 2: [Trafienie Awersem] Zwiększa Licznik [Rozdarcie] celu o 1  
Moneta 3: [Trafienie Awersem] Jeżeli ma [Krwawy Płomień [血炎]], albo jej obecne HP jest poniżej 50% Maks. HP, ponownie używa tę monetę (1 raz na Umiejętność)  
Moneta 3: [Trafienie Awersem] Zadaje dodatkowe obrażenia Gniewu równe 10% końcowych obrażeń tej monety

#### Umiejętność 3 (×1): Rzeź Krwawego Płomienia [血炎亂舞]

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |          3 |         +3 |      4 |           +3 |    3 |
|          4 | Gniew  | Cięcie |          4 |         +3 |      4 |           +3 |    3 |

*Od ulepszenia 3:* [Ostrzał Bez Celowania]  
[Początek Walki] Jeżeli ma [Krwawy Płomień [血炎]], albo jej obecne HP jest poniżej 50% Maks. HP, wszystkie monety stają się [Moneta Niezniszczalna]ami  
[Przy Użyciu] Zyskuje 1 [Krwawy Płomień [血炎]]  
[Przy Użyciu] Jeżeli cel ma 6+ (suma [Podpalenie] i [Rozdarcie]), Moc Monet +1  
[Przegrane Starcie] Nakłada 2 [Podpalenie] na cel i na siebie  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 4: [Przy Trafieniu] Nakłada 2 [Podpalenie]  
Moneta 4: [Przy Trafieniu] Nakłada 2 [Rozdarcie]

*Od ulepszenia 4:* [Ostrzał Bez Celowania]  
Zadaje +1% obrażeń za każde 2% (procent brakującego HP celu + procent brakującego HP własnego) (maks. 50%)  
[Początek Walki] Jeżeli ma [Krwawy Płomień [血炎]], albo jej obecne HP jest poniżej 50% Maks. HP, wszystkie monety stają się [Moneta Niezniszczalna]ami  
[Przy Użyciu] Zyskuje 1 [Krwawy Płomień [血炎]]  
[Przy Użyciu] Moc Monet +1 za każde 6 (suma [Podpalenie] i [Rozdarcie] celu) (maks. 2)  
[Przy Użyciu] Moc Starcia +1 za każde 20% brakującego HP (maks. 2)  
[Przegrane Starcie] Nakłada 2 [Podpalenie] na cel i na siebie  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Podpalenie] celu o 1  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Podpalenie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Rozdarcie]  
Moneta 3: [Trafienie Awersem] Zadaje dodatkowe obrażenia Łaknienia równe 10% końcowych obrażeń tej monety  
Moneta 4: [Przy Trafieniu] Nakłada 2 [Podpalenie]  
Moneta 4: [Przy Trafieniu] Nakłada 2 [Rozdarcie]  
Moneta 4: [Trafienie Awersem] Zadaje dodatkowe obrażenia Łaknienia równe 20% końcowych obrażeń tej monety wszystkim celom

#### Obrona: Zabójczy Cios Koguta [鷄窮則殺]

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | obrona: kontra |          4 |         +4 |      2 |           +2 |    1 |
|          4 | Obżar. | obrona: kontra |          5 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Kontra Starciowa]  
[Przy Użyciu] Zyskuje 3 [Krwawy Płomień [血炎]] w następnej turze  
[Przy Użyciu] Jeżeli ma [Krwawy Płomień [血炎]], Moc Monet +1  
[Przegrane Starcie] Nakłada 2 [Podpalenie] na cel i na siebie  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]

*Od ulepszenia 4:* [Kontra Starciowa]  
[Przy Użyciu] Zyskuje 3 [Krwawy Płomień [血炎]] w następnej turze  
[Przy Użyciu] Jeżeli cel ma 10+ (suma [Podpalenie] i [Rozdarcie]), Moc Bazowa +1  
[Przy Użyciu] Jeżeli ma [Krwawy Płomień [血炎]], Moc Monet +1  
[Przy Użyciu] Ta Umiejętność zadaje +1% obrażeń za każde 3% HP łącznie utracone w tej walce (maks. 30%)  
[Przegrane Starcie] Nakłada 2 [Podpalenie] na cel i na siebie  
Moneta 1: [Przy Trafieniu] Nakłada +1 Licznika [Rozdarcie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Podpalenie]

#### Pasywka bojowa: Walki Kogutów

*od ulepszenia 1*

Przy uruchomieniu [Czcigodny Rozkaz], Wataha Heishou: Lord Hongyuan Hong Lu zyskuje poniższy efekt jako [Heishou - Zakażenie [黑獣丸染]]:  
- Przy nakładaniu Mocy albo Licznika [Rozdarcie] Umiejętnością nakłada 1 [Podpalenie] (3 razy na turę)  
  
Nie może zostać Ogłuszona ani spaść poniżej 1 HP z powodu obrażeń [Podpalenie].  
  
Zyskuje 3 [Krwawy Płomień [血炎]] w turze, w której Weszła z rezerwy albo Powróciła

#### Pasywka bojowa: Walki Kogutów

*od ulepszenia 2*

Przy uruchomieniu [Czcigodny Rozkaz], Wataha Heishou: Lord Hongyuan Hong Lu zyskuje poniższy efekt jako [Heishou - Zakażenie [黑獣丸染]]:  
- Przy nakładaniu Mocy albo Licznika [Rozdarcie] Umiejętnością nakłada 1 [Podpalenie] (3 razy na turę)  
  
Nie może zostać Ogłuszona ani spaść poniżej 1 HP z powodu obrażeń [Podpalenie].  
  
Zyskuje 3 [Krwawy Płomień [血炎]] w turze, w której Weszła z rezerwy albo Powróciła

#### Pasywka bojowa: Upijmy się Walką

*od ulepszenia 2; posiadane 3× Gniew, posiadane 3× Obżar.*

Przy trafieniu celu z 7+ [Rozdarcie], z szansą (najwyższy Rezonans x 15)% nakłada 1 [Podpalenie] (4 razy na turę)  
  
Na koniec walki, jeżeli ma [Podpalenie], na początku następnej tury zyskuje 1 [Krwawy Płomień [血炎]], 1 [Wzrost Obrażeń Gniewu] i 1 [Wzrost Obrażeń Obżarstwa]  
  
Na początku walki zyskuje 1 [Wzrost Poziomu Ataku] i 1 [Wzrost Poziomu Obrony] za każde 20% brakującego HP (maks. 3)

#### Pasywka wsparcia: Krwawopłomienny Miecz [血炎刀]

*od ulepszenia 3; posiadane 3× Gniew, posiadane 3× Obżar.*

Gdy Sojusznik z najwyższą Szybkością nakłada Moc [Podpalenie] albo [Rozdarcie] swoimi Umiejętnościami, nakłada 1 Mocy [Podpalenie] i [Rozdarcie] (1 raz na turę)

#### Kwestie

- **Identity Acquisition:** The lord has finally permitted the roosters to crow. The time to exterminate the vermin infesting Hongyuan... has come.
- **Morning Greeting:** It's so boring to just sit on a perch and doze off... I hope the new lord calls upon us roosters soon.
- **Afternoon Greeting:** Lunch...? I've got to let off some of this steam first. If I'm not getting sent on a mission today, I'm gonna have to go beat up—I mean, spar with a fellow rooster.
- **Evening Greeting:** Leave it to roosters to count the night(使鷄司夜). The sun's set, but if you don't mind the whole world finding out about the deed, why don't you leave it to us roosters instead of snakes or rabbits?
- **Chatter #1:** From the moment we were infused with the You Boluses, the roosters are cursed with an endless hunger for battle. To find a field of war where blood rains and embers rise, to spread and thrash our wings there! ... And that became our only joy in life.
- **Chatter #2:** Each one of the twelve branches of the Heishou inspire fear in people for different reasons, but most of the average citizenry that're not involved with Hongyuan's politics fear us roosters the most. That's because the sight of our branch walking down the main street in serried ranks usually implies that... an all-out war's about to break out somewhere.
- **Chatter #3:** Once the mission begins, we'll jump and peck at every little thing, every brief passing shadow. So... keep your distance, huh? Unless you're one of us, I won't have the wherewithal to tell whether I'm ripping up an enemy or a friend.
- **Post-Uptie Chat 1:** You think jumping around all over the place makes me look clownish? I don't care. I don't care as long as I get to cut more of 'em down, as long as I get to enjoy the slaughter a little more... I cut, I cut, I cut, and I cut... that's all there is to it.
- **Post-Uptie Chat 2:** Xueyan(Bloodflame) Blade, ironically enough, doesn't have a long blade. Instead, there's a special H Corp. oil flowing inside—the kind of oil that sparks into flames from the friction of this weapon hitting blood.
- **Idle:** ... We're alert even in sleep, so rest easy.
- **Uptying:** There's nothing unfair about the way you're going out. It's not bad luck or the lord's disfavor that killed you here today. It's your weakness.
- **Deployment:** The lord has given us feed...
- **Stage Entry:** From the perch to the battlefield.
- **Viewed in Battle:** ... Stop gawking around like a chicken in a battlefield. A rooster with a particularly violent streak might just peck you to death.
- **Commencing Attack:** Spread my wings, and bore them with my talons.
- **Enemy Stagger:** You're cornered. Nowhere to go.
- **Staggered:** ... **spits**
- **Enemy Killed:** ... Dead. Where to next...
- **Death:** I wanted to see the sun rise... over this battlefield...
- **Check Passed:** ... That ended even before I had the chance to heat up.
- **Check Failed:** I must've been too drunk on the heat of battle...
- **Victory Cry:** This isn't enough. This isn't enough to achieve my lord's goals. I gotta be wilder, hotter, and puff my feathers up.
- **Extra Conditions Fulfilled:** A family has been reduced to ash(家門一消). Just give us roosters feed... and we'll make sure the sand circle's picked clean of any vermin. Now that you've seen how useful the roosters can be, my lord, command us to our next battlefield, so that we may spread our wings there.
- **Defeat Wail:** My talons may break... my wings may burn... and my flesh may tear, but... I need to fight... more...! More...! Nngh...

### 000 Dom Pajęczyn: Uczeń Małego Palca — Sinclair

> Piętnasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 7                                                           |
| HP                        | 66 (+2,28 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom −2                                                   |
| Odporności                | Cięcie ×0,5 (Endured), Kłucie ×2 (Fatal), Obuch ×1 (Normal) |
| Progi Stagger (HP)        | 65% / 35%                                                   |
| Grzech wyróżniony         | Posępność                                                   |
| Przynależność             | Spider_House                                                |
| Słowa kluczowe            | Oddech, Krwawienie                                          |
| Data aktualizacji         | 20260205                                                    |

#### Umiejętność 1 (×3): Seria Ciosów [連擊]

| Ulepszenie | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | --------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Posępność | Cięcie |          3 |         +3 |      2 |           +1 |    1 |
|          3 | Posępność | Cięcie |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 2  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada +1 Licznika [Krwawienie]

*Od ulepszenia 2:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 3  
[Przy Użyciu] Przy 6+ [Oddech] Moc Monet +1  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 1  
Moneta 2: [Przy Trafieniu] Zyskuje 1 [Pośpiech] w następnej turze (1 raz na turę)

*Od ulepszenia 4:* [Przy Użyciu] Zwiększa własny Licznik [Oddech] o 3  
[Przy Użyciu] Moc Monet +1 za każde 6 [Oddech] (maks. 2)  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Zyskuje 1 [Pośpiech] w następnej turze (1 raz na turę)  
Moneta 2: [Krytyk - Trafienie Awersem] Zyskuje 1 [Pośpiech] w następnej turze (1 raz na turę)

#### Umiejętność 2 (×2): Bezimienny Cios [無名斬]

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Cięcie |          5 |         +5 |      2 |           +3 |    3 |
|          3 | Pycha  | Cięcie |          6 |         +5 |      2 |           +3 |    3 |

*Od ulepszenia 1:* [Ostrzał Bez Celowania]  
Moneta 1: [Przy Trafieniu] Zyskuje 3 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]  
Moneta 2: Zadaje +10% obrażeń przy trafieniu krytycznym  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]

*Od ulepszenia 2:* [Ostrzał Bez Celowania]  
[Przy Użyciu] Przy 6+ [Oddech] Moc Bazowa +1  
Moneta 1: [Przy Trafieniu] Zyskuje 3 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]  
Moneta 2: Zadaje +10% obrażeń przy trafieniu krytycznym  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Krytyk - Trafienie Awersem] Ponownie używa tę monetę (1 raz na Umiejętność)

*Od ulepszenia 4:* [Ostrzał Bez Celowania]  
[Przy Użyciu] Moc Bazowa +1 za każde 6 [Oddech] (maks. 2)  
Moneta 1: [Przy Trafieniu] Zyskuje 3 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje +1 Licznika [Oddech]  
Moneta 2: Zadaje +10% obrażeń przy trafieniu krytycznym  
Moneta 2: [Przy Trafieniu] Zwiększa własny Licznik [Oddech] o 1  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 2: [Krytyk - Trafienie Awersem] Ponownie używa tę monetę (1 raz na Umiejętność)  
Moneta 2: [Ponowne Użycie - Trafienie Awersem] Przy 10+ [Błękitne Ostrze w Blasku Księżyca] ponownie używa tę monetę (1 raz na Umiejętność)

#### Umiejętność 3 (×1): Zabójca Spadającej Gwiazdy [落星一殺]

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Cięcie |          6 |        +12 |      1 |           +5 |    1 |
|          4 | Gniew  | Cięcie |          8 |        +14 |      1 |           +5 |    1 |

*Od ulepszenia 3:* Zadaje +30% obrażeń za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów (w walkach skupionych Party)  
[Przy Użyciu] Przy 20 [Błękitne Ostrze w Blasku Księżyca] wszystkie monety tej Umiejętności stają się [Moneta Niezniszczalna]ami  
[Przy Użyciu] Moc Monet +1 za każde 4 [Oddech] (maks. 3)  
[Przy Użyciu] Moc Bazowa +1 za każde 4 [Błękitne Ostrze w Blasku Księżyca] (maks. 3)  
[Przy Użyciu] Zyskuje 5 [Oddech]  
  
[Przed Atakiem] Waga ataku +1 za każde 10 [Błękitne Ostrze w Blasku Księżyca] (maks. 2)  
[Koniec Ataku] Zużywa 7 [Błękitne Ostrze w Blasku Księżyca] za każdy 1 Waga ataku zyskany efektem tej Umiejętności  
Moneta 1: Zadaje +50% obrażeń Krytycznych  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 1: [Krytyk - Trafienie Awersem] Zadaje obrażenia Sieczne równe 25% końcowych obrażeń tej monety

*Od ulepszenia 4:* Zadaje +50% obrażeń za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów (w walkach skupionych Party)  
[Przy Użyciu] Przy 20 [Błękitne Ostrze w Blasku Księżyca] wszystkie monety tej Umiejętności stają się [Moneta Niezniszczalna]ami  
[Przy Użyciu] Moc Monet +1 za każde 4 [Oddech] (maks. 5)  
[Przy Użyciu] Moc Bazowa +1 za każde 4 [Błękitne Ostrze w Blasku Księżyca] (maks. 5)  
[Przy Użyciu] Zyskuje 7 [Oddech]  
  
[Przed Atakiem] Waga ataku +1 za każde 10 [Błękitne Ostrze w Blasku Księżyca] (maks. 2)  
[Koniec Ataku] Zużywa 5 [Błękitne Ostrze w Blasku Księżyca] za każdy 1 Waga ataku zyskany efektem tej Umiejętności  
Moneta 1: Zadaje +70% obrażeń przy trafieniu krytycznym  
Moneta 1: [Przy Trafieniu] Nakłada 5 [Krwawienie]  
Moneta 1: [Krytyk - Trafienie Awersem] Zadaje obrażenia Sieczne równe 25% końcowych obrażeń tej monety

#### Obrona: Obrona [守]

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |          2 |         +8 |      1 |           +2 |    1 |
|          4 | Pycha   | obrona: blok |          3 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [Blok Zdatny do Starcia]  
Na początku tury, przy Mocy [Oddech] 25 lub wyższej, zamienia się w „Zwrot [回]”  
  
[Początek Walki] Zyskuje 6 [Oddech] (1 raz na turę)  
[Początek Walki] Zwiększa własny Licznik [Oddech] o 1 (1 raz na turę)  
Moneta 1: [Moneta Niezniszczalna]

*Od ulepszenia 4:* [Blok Zdatny do Starcia]  
Na początku tury, przy Mocy [Oddech] 25 lub wyższej, zamienia się w „Zwrot [回]”  
  
[Początek Walki] Zyskuje 8 [Oddech] (1 raz na turę)  
[Początek Walki] Zwiększa własny Licznik [Oddech] o 2 (1 raz na turę)  
Moneta 1: [Moneta Niezniszczalna]

#### Obrona: Zwrot [回]

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          4 |        +10 |      1 |           +3 |    1 |
|          4 | Pycha   | obrona: unik |          4 |        +10 |      1 |           +3 |    1 |

*Od ulepszenia 1:* [Początek Walki] Zyskuje Tarczę równą stosom [Błękitne Ostrze w Blasku Księżyca] (1 raz na turę)  
[Początek Walki] Zwiększa własny Licznik [Oddech] o 4 (1 raz na turę)

*Od ulepszenia 4:* [Początek Walki] Zyskuje Tarczę równą stosom [Błękitne Ostrze w Blasku Księżyca] (1 raz na turę)  
[Początek Walki] Zwiększa własny Licznik [Oddech] o 4 (1 raz na turę)  
[Udany Unik] Zyskuje 1 [Wzrost Obrażeń Krytycznych] w następnej turze (maks. 2 razy na turę)

#### Pasywka bojowa: Jedność Umysłu

*od ulepszenia 1*

Na koniec tury zamienia nadwyżkę Mocy [Oddech] ponad 25, do maks. 15, na [Błękitne Ostrze w Blasku Księżyca]  
  
Na początku walki, jeżeli w tej turze nie wyposażyła Umiejętności ataku (w tym Umiejętności E.G.O), odzyskuje 5 Poczytalności i zyskuje 1 [Wzrost Mocy Cięcia] w następnej turze

#### Pasywka bojowa: Jedność Umysłu

*od ulepszenia 2*

Na koniec tury zamienia nadwyżkę Mocy [Oddech] ponad 25, do maks. 15, na [Błękitne Ostrze w Blasku Księżyca]  
  
Na początku walki, jeżeli w tej turze nie wyposażyła Umiejętności ataku (w tym Umiejętności E.G.O), odzyskuje 5 Poczytalności i zyskuje 1 [Wzrost Mocy Cięcia] w następnej turze

#### Pasywka bojowa: Ortodoksyjne Ostrze [整劍]

*od ulepszenia 2; rezonans 2× Pycha*

Na początku walki zyskuje ((Rezonans Pychy / 2) + 1) [Oddech] (maks. 4, w dół)  
  
Na koniec walki, przy Mocy [Oddech] 20+, zwiększa własny Licznik [Oddech] o 1

#### Pasywka wsparcia: Ukojenie [靜念]

*od ulepszenia 3; rezonans 2× Pycha*

1 Sojusznik z najwyższą Szybkością odzyskuje 5 Poczytalności i zyskuje 5 Tarczy, jeżeli rozpoczyna walkę z Umiejętnością obrony

#### Kwestie

- **Identity Acquisition:** This lowly self of mine is yet to deserve the name of a Star. Until such a time arrives that I might inherit the title, I shall continue to be of service to my master and hone myself without end.
- **Morning Greeting:** The day has dawned—I must pay my morning respects to master. Though I may find no welcome there, to hear my master groan so in constant torment, doomed to never know the reprieve of peaceful sleep, is... Yes, I must act as Ren (仁)—the Virtue of Humanity—dictates.
- **Afternoon Greeting:** Once again, half the day has already slipped away. My humble self grows restless with such squandering of time, for it calls to mind the impending end of my existence. And yet... Whenever I witness the disorder and havoc those others raise, I find myself musing upon the merits of idleness.
- **Evening Greeting:** As my master expects naught from my insignificant self... I must polish my blade through the dark of the night and persistently sharpen the form of my body so I may endure the dullness of todays and the emptiness of morrows.
- **Chatter #1:** The child of the Thumb... appears to have been brutally manhandled by the Nursefather yet again. While it is indeed of great import to instruct one's apprentice with a stern hand, this lack of restraint hardly conforms to Li (禮)—the Virtue of Propriety. I see the child, though thrashed and beaten down into the dust, dutifully bring the Nursefather a fresh round of liquor...
- **Chatter #2:** Keep silent for a moment, if you would. On a day such as this, with no duty calling my humble self beyond the House, there is a certain someone I must be wary of. Let us tread lightly here... Huh? You stayed put at the House of Spiders all day? Okay, then didya check out *The Cloudburst Blade* I told ya about? Hey, wait! Where are you going?!
- **Chatter #3:** The depths of man's heart is indeed beyond fathoming. The hand that now pats the head of his apprentice—is it a gesture given out of sincere affection, or merely an act performed at the behest of the Prescript?
- **Post-Uptie Chat 1:** Though this blade of mine may impeccably mimic that of the one who came before me... they say the one true apprentice of the House had a prowess that my humble self cannot ever hope to match. What kind of warrior that one was, I have but my imagination to rely upon. And so my lowly self brandishes this blade in training, forever simulating, approaching the height to which I aspire.
- **Post-Uptie Chat 2:** The Nursefathers of the House of Spiders each receive a task of their own from the upper echelons of the Fingers, and their apprentices, in turn, either assist them with it or are given separate charges. Yet... they say the one who came before me used to complete all of those tasks single-handedly. To house within one's self the teachings and trials that embody each Nursefather's art of battle—the road toward such a realm seems unimaginably taxing.
- **Idle:** I do not well understand these other Nursefathers... But at times, I find myself stricken... with envy. Whether it be affection or resentment, such attentiveness to one's apprentice evinces a degree of care.
- **Uptying:** A rare assignment my master has bestowed upon me. I shall treasure this chance, so as not to cast shame upon the Moonlit Azure Blade (月下靑刀) my master has imparted unto me.
- **Deployment:** A summons? Then I shall gladly answer it.
- **Stage Entry:** ... At long last.
- **Viewed in Battle:** A single straight stroke to fell them all...!
- **Commencing Attack:** Permit me to demonstrate.
- **Enemy Stagger:** One mustn't submit so easily.
- **Staggered:** Hngh...!
- **Enemy Killed:** Another step closer to that singular Way of the Blade.
- **Death:** A life so fleeting, a death meant to be... But this failure to inherit the name of a Star... is my woeful regret.
- **Check Passed:** Such trifling matters does my master entrust me with...
- **Check Failed:** No outcome is without reason... This must be why I am yet unworthy of standing as one of The Pinky.
- **Victory Cry:** My endeavors were rather... wanting, but I shall not be dismayed. Though I may fail to inherit the name of a Star in this life, following in my master's footsteps shall sharpen and temper this insignificant self of mine.
- **Extra Conditions Fulfilled:** How did you find the demonstration? My humble self is inclined to believe that I have gained something of value. Should I return bearing the heads of these fallen foes... Then perhaps, this time, my master might speak of the name Dihui Star... and how I am growing to deserve it.
- **Defeat Wail:** It seems my lowly self's usefulness... has run its course here. This sword of mine is still soft and dull—unable to safeguard the fragile, delicate master I serve, nor attain the uttermost height of the Way of the Blade. In the end, I have achieved nothing of worth...

### 000 Haute Couture:: Szkarłatny Bóg Le Rouge — Sinclair

> Szesnasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | 8                                                           |
| HP                        | 77 (+2,9 za poziom)                                         |
| Szybkość (ulepszenia 1–4) | 3–6 / 4–6 / 4–7 / 4–7                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×0,5 (Endured), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 55%                                                         |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Le_Rouge, Sisyphe                                           |
| Słowa kluczowe            | Ładowanie, Krwawienie                                       |
| Data aktualizacji         | 20261015                                                    |

#### Umiejętność 1 (×3): La Pulsion

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Kłucie |          4 |         +5 |      1 |           +1 |    1 |
|          3 | Obżar. | Kłucie |          4 |         +6 |      1 |           +1 |    1 |
|          4 | Obżar. | Kłucie |          5 |         +6 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [Stały Cel]  
[Dwubiegunowość]  
  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 5  
- Jeżeli celem jest sojusznik, zwiększa dodatkowo własny Licznik [Pulsacja] o 5  
Moneta 1: [Koniec Ataku Tej Monety] Jeżeli celem jest sojusznik, uruchamia poniższe efekty (2 razy na turę):  
- Cel odzyskuje 10% HP  
  · Jeżeli cel należy do Le Rouge, zamiast tego zużywa 20% Maks. HP celu i nakłada 2 [Wzrost Mocy]  
- Cel odzyskuje 10 Poczytalności  
  · Jeżeli Poczytalność celu jest pełna, zamiast tego zwiększa Licznik [Ładowanie] celu o 4

*Od ulepszenia 2:* [Stały Cel]  
[Dwubiegunowość]  
  
[Przy Użyciu] Moc Starcia +1 za każde 4 [Krwawienie] celu (maks. 2)  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 5  
- Jeżeli celem jest sojusznik, zwiększa dodatkowo własny Licznik [Pulsacja] o 5  
Moneta 1: [Koniec Ataku Tej Monety] Jeżeli celem jest sojusznik, uruchamia poniższe efekty (2 razy na turę):  
- Cel odzyskuje 10% HP  
  · Jeżeli cel należy do Le Rouge, zamiast tego zużywa 20% Maks. HP celu i nakłada 2 [Wzrost Mocy]  
- Cel odzyskuje 10 Poczytalności  
  · Jeżeli Poczytalność celu jest pełna, zamiast tego zwiększa Licznik [Ładowanie] celu o 4

*Od ulepszenia 4:* [Stały Cel]  
[Dwubiegunowość]  
  
[Przy Użyciu] Zyskuje (Moc [Pulsacja] - 1) Wagi ataku (maks. 2)  
- Cele dodatkowe: najpierw sojusznicy Le Rouge, wybierani według rosnącego procentu HP  
  
[Przy Użyciu] Moc Starcia +1 za każde 4 [Krwawienie] celu (maks. 2)  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 5  
- Jeżeli celem jest sojusznik, zwiększa dodatkowo własny Licznik [Pulsacja] o 5  
Moneta 1: [Koniec Ataku Tej Monety] Jeżeli celem jest sojusznik, uruchamia poniższe efekty (2 razy na turę):  
- Cel odzyskuje (10 + Moc [Pulsacja])% HP (maks. 15%)  
· Jeżeli cel należy do Le Rouge, zamiast tego zużywa 20% Maks. HP celu i nakłada 2 [Wzrost Mocy]  
- Cel odzyskuje (10 + Moc [Pulsacja]) Poczytalności (maks. 15)  
· Jeżeli Poczytalność celu jest pełna, zamiast tego zwiększa Licznik [Ładowanie] celu o 4

#### Umiejętność 2 (×2): L'Appétit

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gniew  | Kłucie |          4 |         +4 |      2 |           +2 |    1 |
|          3 | Gniew  | Kłucie |          4 |         +5 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Stały Cel]  
[Dwubiegunowość]  
  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 3  
[Przy Użyciu] Jeżeli celem jest sojusznik, uruchamia wyłącznie efekty monety 1, po czym kończy Umiejętność  
Moneta 1: [Koniec Ataku Tej Monety] Jeżeli celem jest sojusznik, uruchamia poniższe efekty:  
- Nakłada 1 [Rozpaczliwy Głód]  
- Jeżeli celem jest [Osobowość Ładowania], nakłada 4 Licznika [Ładowanie]  
- Jeżeli cel należy do Le Rouge, zużywa 10% Maks. HP celu i nakłada 2 [Wzrost Poziomu Ataku]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]

*Od ulepszenia 2:* [Stały Cel]  
[Dwubiegunowość]  
  
[Przy Użyciu] Moc Starcia +1 za każde 3 Licznika [Pulsacja] (maks. 3)  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 3  
[Przy Użyciu] Jeżeli celem jest sojusznik, uruchamia wyłącznie efekty monety 1, po czym kończy Umiejętność  
Moneta 1: [Koniec Ataku Tej Monety] Jeżeli celem jest sojusznik, uruchamia poniższe efekty:  
- Nakłada 1 [Rozpaczliwy Głód]  
- Jeżeli celem jest [Osobowość Ładowania], nakłada 4 Licznika [Ładowanie]  
- Jeżeli cel należy do Le Rouge, zużywa 10% Maks. HP celu i nakłada 2 [Wzrost Poziomu Ataku]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]

*Od ulepszenia 4:* [Stały Cel]  
[Dwubiegunowość]  
  
[Przy Użyciu] Waga ataku +1 za każde 2 Mocy [Pulsacja] (maks. 2)  
- Cele dodatkowe: najpierw sojusznicy Le Rouge, wybierani według malejącego procentu HP  
  
[Przy Użyciu] Moc Starcia +1 za każde 3 Licznika [Pulsacja] (maks. 3)  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 3  
[Przy Użyciu] Jeżeli celem jest sojusznik, uruchamia wyłącznie efekty monety 1, po czym kończy Umiejętność  
Moneta 1: [Koniec Ataku Tej Monety] Jeżeli celem jest sojusznik, uruchamia poniższe efekty:  
- Nakłada 1 [Wzrost Mocy Starcia] i 1 [Rozpaczliwy Głód]  
- Jeżeli celem jest [Osobowość Ładowania], nakłada 4 Licznika [Ładowanie]  
- Jeżeli cel należy do Le Rouge, zużywa 10% Maks. HP celu i nakłada 2 [Wzrost Poziomu Ataku]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]

#### Umiejętność 3 (×1): Le Baptême rouge

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Kłucie |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* [Początek Walki] Zużywa 15% Maks. HP na 2 Sojuszników poza tą jednostką i nakłada 3 [Wzrost Poziomu Ataku]  
- Wybiera według malejącego obecnego HP wśród sojuszników z 50%+ HP  
- Sojusznicy Le Rouge: jeżeli mają 2+ HP, są wybierani priorytetowo niezależnie od HP; zamiast tego zużywa 25% Maks. HP i nakłada dodatkowo 1 [Wzrost Mocy Ataku]  
  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
  
[Przy Użyciu] Jeżeli jest w stanie [Paroksyzm], wszystkie monety stają się [Moneta Niezniszczalna]ami  
- Przy 10+ Licznika [Pulsacja] zużywa do 10 Licznika [Pulsacja], aby zyskać Waga ataku +2 i Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 3

*Od ulepszenia 4:* [Początek Walki] Zużywa 15% Maks. HP na 2 Sojuszników poza tą jednostką i nakłada 3 [Wzrost Poziomu Ataku]  
- Wybiera według malejącego obecnego HP wśród sojuszników z 50%+ HP  
- Sojusznicy Le Rouge: jeżeli mają 2+ HP, są wybierani priorytetowo niezależnie od HP; zamiast tego zużywa 25% Maks. HP i nakłada dodatkowo 1 [Wzrost Mocy Ataku]  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 2)  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
  
[Przy Użyciu] Jeżeli jest w stanie [Paroksyzm], wszystkie monety stają się [Moneta Niezniszczalna]ami  
- Przy 10+ Licznika [Pulsacja] zużywa do 10 Licznika [Pulsacja], aby zyskać Waga ataku +2 i Moc Monet +1  
[Przy Użyciu] Zadaje +50% obrażeń za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów (w walkach skupionych Party)  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 1: [Przy Trafieniu] Zyskuje 3 [Nieustający Głód]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Zyskuje 3 [Nieustający Głód]  
Moneta 3: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 3  
Moneta 3: [Przy Trafieniu] Zyskuje 3 [Nieustający Głód]

#### Umiejętność 4 (×0): Je vous aide

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | Kłucie |          4 |         +5 |      1 |           +1 |    1 |
|          3 | Pycha  | Kłucie |          4 |         +6 |      1 |           +1 |    1 |
|          4 | Pycha  | Kłucie |          5 |         +6 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [Niestarciowy]  
Ta Umiejętność nie uruchamia Umiejętności obrony  
  
Jeżeli jest w stanie [Paroksyzm], zadaje +50% obrażeń  
[Przy Użyciu] Zyskuje 5 [Nieustający Głód]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2

*Od ulepszenia 2:* [Niestarciowy]  
Ta Umiejętność nie uruchamia Umiejętności obrony  
  
Jeżeli jest w stanie [Paroksyzm], zadaje +50% obrażeń  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 4)  
[Przy Użyciu] Zyskuje 5 [Nieustający Głód]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2

*Od ulepszenia 4:* [Niestarciowy]  
Ta Umiejętność nie uruchamia Umiejętności obrony  
  
Jeżeli jest w stanie [Paroksyzm], zadaje +50% obrażeń  
Zadaje +5% obrażeń za każde 1% brakującego HP celu (maks. 100%)  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 4)  
[Przy Użyciu] Zyskuje 5 [Nieustający Głód]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Wrażliwość na Żądzę] (1 raz na turę)

#### Umiejętność 5 (×0): Je m'expulse

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Kłucie |          3 |         +3 |      3 |           +3 |    1 |

*Od ulepszenia 3:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 3  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [L'Abject]

*Od ulepszenia 4:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Przy Użyciu] Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Zwiększa własny Licznik [Pulsacja] o 3  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 3: [Przy Trafieniu] Nakłada 2 [L'Abject]

#### Umiejętność 6 (×0): Je m'abjecte

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gniew  | Kłucie |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 3:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
  
[Przed Atakiem] Zużywa 15% Maks. HP na 2 Sojuszników poza tą jednostką  
- Najpierw sojusznicy Le Rouge, wybierani według malejącego obecnego HP  
- Zadaje +15% obrażeń za każdego sojusznika, któremu zużyto HP  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 2 [L'Abject]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [L'Abject]  
- Jeżeli jest w stanie [Paroksyzm], zamiast tego nakłada 2 [L'Abject]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Wrażliwość na Żądzę] (1 raz na turę)

*Od ulepszenia 4:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Przy Użyciu] Jeżeli cel ma 6+ [Krwawienie], Moc Monet +1  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
  
[Przed Atakiem] Zużywa 15% Maks. HP na 2 Sojuszników poza tą jednostką  
- Najpierw sojusznicy Le Rouge, wybierani według malejącego obecnego HP  
- Zadaje +15% obrażeń za każdego sojusznika, któremu zużyto HP  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 2 [L'Abject]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [L'Abject]  
- Jeżeli jest w stanie [Paroksyzm], zamiast tego nakłada 2 [L'Abject]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Wrażliwość na Żądzę] (1 raz na turę)

#### Umiejętność 7 (×0): La Demande

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Pycha  | Kłucie |          5 |         +5 |      2 |           +3 |    1 |

*Od ulepszenia 3:* [Niestarciowy]  
[Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
Ta Umiejętność nie uruchamia Umiejętności obrony  
  
Zadaje +5% obrażeń za każde 3 [Krwawienie] celu (maks. 30%)  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Usuwa cały [L'Abject] celu i nakłada 1 [Wrażliwość na Żądzę] w następnej turze (1 raz na turę)

*Od ulepszenia 4:* [Niestarciowy]  
[Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
Ta Umiejętność nie uruchamia Umiejętności obrony  
  
Zadaje +5% obrażeń za każde 3 [Krwawienie] celu (maks. 30%)  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
Moneta 1: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 3 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Usuwa cały [L'Abject] celu i nakłada 2 [Wrażliwość na Żądzę] w następnej turze (1 raz na turę)

#### Umiejętność 8 (×0): Le Manque-à-être

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Obżar. | Kłucie |          7 |         +8 |      1 |           +3 |    1 |

*Od ulepszenia 3:* [Niestarciowy]  
[Stały Cel]  
[Dwubiegunowość]  
Zewnętrzne efekty nie mogą ponownie użyć tej Umiejętności  
  
[Przy Użyciu] Zyskuje 5 [Spętanie] w następnej turze  
Moneta 1: [Koniec Ataku Tej Monety] Dochodzi z Ogłuszenia celu

*Od ulepszenia 4:* [Niestarciowy]  
[Stały Cel]  
[Dwubiegunowość]  
Zewnętrzne efekty nie mogą ponownie użyć tej Umiejętności  
Moneta 1: [Koniec Ataku Tej Monety] Dochodzi z Ogłuszenia celu  
Moneta 1: [Koniec Ataku Tej Monety] Cel odzyskuje HP równy 15% Maks. HP celu

#### Umiejętność 9 (×0): La Voracité

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Kłucie |          5 |         +3 |      4 |           +5 |    1 |

*Od ulepszenia 3:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
Na początku tury, przy 150 [Nieustający Głód], zamienia się w „La Castration” (1 raz na turę)  
  
[Przy Użyciu] Jeżeli jest w stanie [Paroksyzm], wszystkie monety stają się [Moneta Niezniszczalna]ami  
- Przy 10+ Licznika [Pulsacja] zużywa do 10 Licznika [Pulsacja], aby zyskać Waga ataku +2 i Moc Monet +1  
  
[Przed Atakiem] Zużywa 15% Maks. HP na 3 Sojuszników poza tą jednostką  
- Najpierw sojusznicy Le Rouge, wybierani według malejącego obecnego HP  
- Zadaje +10% obrażeń za każdego sojusznika, któremu zużyto HP  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 1: [Przy Trafieniu] Jeżeli jest głównym celem, nakłada dodatkowo 1 [L'Abject] za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 3: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 4: [Przy Trafieniu] Uruchamia [Krwawienie] celu 1 raz. Cel traci 1 Licznika [Krwawienie]

*Od ulepszenia 4:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
Na początku tury, przy 150 [Nieustający Głód], zamienia się w „La Castration” (1 raz na turę)  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 2)  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
  
[Przy Użyciu] Jeżeli jest w stanie [Paroksyzm], wszystkie monety stają się [Moneta Niezniszczalna]ami  
- Przy 10+ Licznika [Pulsacja] zużywa do 10 Licznika [Pulsacja], aby zyskać Waga ataku +2 i Moc Monet +1  
[Przy Użyciu] Zadaje +50% obrażeń za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów (w walkach skupionych Party)  
  
[Przed Atakiem] Zużywa 15% Maks. HP na 3 Sojuszników poza tą jednostką  
- Najpierw sojusznicy Le Rouge, wybierani według malejącego obecnego HP  
- Zadaje +10% obrażeń za każdego sojusznika, któremu zużyto HP  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 1: [Przy Trafieniu] Jeżeli jest głównym celem, nakłada dodatkowo 1 [L'Abject] za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 3: [Przy Trafieniu] Nakłada 2 [Krwawienie]  
Moneta 4: [Przy Trafieniu] Uruchamia [Krwawienie] celu 1 raz. Cel traci 1 Licznika [Krwawienie]

#### Umiejętność 10 (×0): La Castration

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | Kłucie |          4 |         +3 |      5 |           +5 |    3 |

*Od ulepszenia 3:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Przed Użyciem] Przy mniej niż 150 [Nieustający Głód] zamienia się w „La Voracité”  
  
[Początek Walki] Zużywa 50% obecnego HP wszystkich sojuszników Le Rouge poza tą jednostką, nakładając na nich 3 [Paroksyzm]  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] głównego celu (maks. 2)  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
[Koniec Ataku] Zużywa cały [Nieustający Głód]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 1: [Przy Trafieniu] Jeżeli jest głównym celem, nakłada dodatkowo 1 [L'Abject] za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 4: [Moneta Niezniszczalna]  
Moneta 4: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 4: [Przy Trafieniu] Usuwa cały [L'Abject] celu i nakłada w następnej turze tyle [Wrażliwość na Żądzę], ile usunięto (maks. 3)  
Moneta 5: [Moneta Niezniszczalna]  
Moneta 5: [Przy Trafieniu] Uruchamia [Krwawienie] celu 1 raz. Cel traci 1 Licznika [Krwawienie]

*Od ulepszenia 4:* [Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Przed Użyciem] Przy mniej niż 150 [Nieustający Głód] zamienia się w „La Voracité”  
  
[Początek Walki] Zużywa 50% obecnego HP wszystkich sojuszników Le Rouge poza tą jednostką, nakładając na nich 3 [Paroksyzm]  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] głównego celu (maks. 2)  
[Przy Użyciu] Przy 3+ Mocy [Pulsacja] Moc Monet +1  
[Przy Użyciu] Jeżeli jest w stanie [Paroksyzm], Moc Monet +1  
[Przy Użyciu] Zadaje +50% obrażeń za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów (w walkach skupionych Party)  
  
[Koniec Ataku] Zużywa cały [Nieustający Głód]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zwiększa Licznik [Krwawienie] celu o 2  
Moneta 1: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 1: [Przy Trafieniu] Jeżeli jest głównym celem, nakłada dodatkowo 1 [L'Abject] za każdy nadmiarowy Waga ataku ponad liczbę rzeczywistych celów  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 4: [Moneta Niezniszczalna]  
Moneta 4: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 4: [Przy Trafieniu] Usuwa cały [L'Abject] celu i nakłada w następnej turze tyle [Wrażliwość na Żądzę], ile usunięto (maks. 3)  
Moneta 5: [Moneta Niezniszczalna]  
Moneta 5: [Początek Monety] Zużywa do 15 Licznika [Pulsacja] i zadaje +(zużyte Liczniki [Pulsacja] x 3)% obrażeń  
Moneta 5: [Przy Trafieniu] Uruchamia [Krwawienie] celu 1 raz. Cel traci 1 Licznika [Krwawienie]

#### Obrona: La Fuite

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           +2 |    1 |
|          4 | Żądza   | obrona: unik |          3 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [Początek Walki] Jeżeli nie ma [Paroksyzm] i ma mniej niż 15 Licznika [Pulsacja], zużywa (15 - obecne Liczniki [Pulsacja])% HP, aby zwiększyć Licznik [Pulsacja] do 15 (1 raz na turę)  
  
[Udany Unik] Zwiększa własny Licznik [Pulsacja] o 2 (2 razy na turę)

*Od ulepszenia 4:* [Początek Walki] Jeżeli nie ma [Paroksyzm] i ma mniej niż 15 Licznika [Pulsacja], zużywa (15 - obecne Liczniki [Pulsacja])% HP, aby zwiększyć Licznik [Pulsacja] do 15 (1 raz na turę)  
  
[Udany Unik] Zwiększa własny Licznik [Pulsacja] o 2 (2 razy na turę)

#### Obrona: La Garde

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | obrona: blok |          2 |         +7 |      1 |           +0 |    1 |

[Blok Zdatny do Starcia]  
Ta Umiejętność traktowana jest jako Assist Defense wyłącznie dla użytkownika  
Gdy użytkownik zostanie trafiony podczas użycia tej Umiejętności, Haute Couture::Szkarłatny Bóg Le Rouge Sinclair zyskuje 2 [Nieustający Głód]  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 3)  
Moneta 1: [Moneta Niezniszczalna]

#### Obrona: Le Trait unaire

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Żądza  | obrona: kontra |          4 |         +4 |      2 |           +2 |    1 |
|          4 | Żądza  | obrona: kontra |          5 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 3:* [Kontra Starciowa]  
[Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Początek Walki] Jeżeli nie ma [Paroksyzm] i ma mniej niż 15 Licznika [Pulsacja], zużywa (15 - obecne Liczniki [Pulsacja])% HP, aby zwiększyć Licznik [Pulsacja] do 15 (1 raz na turę)  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 2)  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [L'Abject]

*Od ulepszenia 4:* [Kontra Starciowa]  
[Szlachetna Duma] Umiejętność wyłącznie dla tego stanu  
[Początek Walki] Jeżeli nie ma [Paroksyzm] i ma mniej niż 15 Licznika [Pulsacja], zużywa (15 - obecne Liczniki [Pulsacja])% HP, aby zwiększyć Licznik [Pulsacja] do 15 (1 raz na turę)  
  
[Przy Użyciu] Moc Końcowa +1 za każde 4 [Krwawienie] celu (maks. 2)  
[Przy Użyciu] Przy Mocy [Pulsacja] 3/5+ Moc Monet +1/+2  
Moneta 1: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 1: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [Krwawienie]  
Moneta 2: [Przy Trafieniu] Nakłada 1 [L'Abject]  
Moneta 2: [Przy Trafieniu] Jeżeli jest w stanie [Paroksyzm], nakłada 1 [L'Abject]

#### Pasywka bojowa: La Moisson

*od ulepszenia 1*

Gdy efekty jej podstawowych Umiejętności zużywają HP sojusznika, ten nie zostaje Ogłuszony tymi efektami, a jego HP nie spada poniżej 1  
  
Przy Rezonansie Żądzy 3+, na koniec walki nakłada [Rozpaczliwy Głód] w następnej turze na (Rezonans Żądzy / 3) Sojuszników poza tą jednostką (zaokrąglone w górę)  
- Najpierw sojusznicy Le Rouge, nakładane w kolejności przydziału  
  
Przy użyciu Umiejętności [Dwubiegunowość] na sojuszniku nakłada 1 [Asysta przy Boskości] na działającego sojusznika Le Rouge z najwyższym obecnym HP (1 raz na turę)  
Na koniec podstawowego ataku [Osobowość Ładowania] poza tą jednostką, jeżeli główny cel nie zginął, stosuje „Je vous aide” przeciwko temu wrogowi (1 raz na turę)

#### Pasywka bojowa: La Jouissance phallique

*od ulepszenia 1*

Zwiększa własny Licznik [Pulsacja] o 1 za każde uruchomienie [Krwawienie] podczas walki (maks. 10 razy na turę)  
  
Na koniec walki, jeżeli nie jest w stanie [Paroksyzm] i ma 15+ Licznika [Pulsacja], zużywa cały Licznik [Pulsacja], aby w następnej turze zyskać 3 [Paroksyzm]  
- Odzyskuje Poczytalność równą (3 x Liczniki [Pulsacja] zużyte ponad 15) (maks. 15)  
  
Po wygaśnięciu [Paroksyzm] zużywa cały własny Licznik [Pulsacja], odzyskując HP równy (zużyte Liczniki [Pulsacja] x 2)  
  
Zyskuje 1 Mocy [Pulsacja] za każde łączne zużycie 10 własnego Licznika [Pulsacja] podczas walki  
  
Podstawowe Umiejętności ataku i umiejętności Kontry możliwe w starciu traktowane są jako Umiejętności zyskujące Licznik [Ładowanie]

#### Pasywka bojowa: La Moisson

*od ulepszenia 2*

Gdy efekty jej podstawowych Umiejętności zużywają HP sojusznika, ten nie zostaje Ogłuszony tymi efektami, a jego HP nie spada poniżej 1  
  
Przy Rezonansie Żądzy 3+, na koniec walki nakłada [Rozpaczliwy Głód] w następnej turze na (Rezonans Żądzy / 3) Sojuszników poza tą jednostką (zaokrąglone w górę)  
- Najpierw sojusznicy Le Rouge, nakładane w kolejności przydziału  
  
Przy użyciu Umiejętności [Dwubiegunowość] na sojuszniku nakłada 1 [Asysta przy Boskości] na działającego sojusznika Le Rouge z najwyższym obecnym HP (1 raz na turę)  
Na koniec podstawowego ataku [Osobowość Ładowania] poza tą jednostką, jeżeli główny cel nie zginął, stosuje „Je vous aide” przeciwko temu wrogowi (1 raz na turę)

#### Pasywka bojowa: La Jouissance phallique

*od ulepszenia 2*

Zwiększa własny Licznik [Pulsacja] o 1 za każde uruchomienie [Krwawienie] podczas walki (maks. 10 razy na turę)  
  
Na koniec walki, jeżeli nie jest w stanie [Paroksyzm] i ma 15+ Licznika [Pulsacja], zużywa cały Licznik [Pulsacja], aby w następnej turze zyskać 3 [Paroksyzm]  
- Odzyskuje Poczytalność równą (3 x Liczniki [Pulsacja] zużyte ponad 15) (maks. 15)  
  
Po wygaśnięciu [Paroksyzm] zużywa cały własny Licznik [Pulsacja], odzyskując HP równy (zużyte Liczniki [Pulsacja] x 2)  
  
Zyskuje 1 Mocy [Pulsacja] za każde łączne zużycie 10 własnego Licznika [Pulsacja] podczas walki  
  
Podstawowe Umiejętności ataku i umiejętności Kontry możliwe w starciu traktowane są jako Umiejętności zyskujące Licznik [Ładowanie]

#### Pasywka bojowa: La Fin de l'Enfance

*od ulepszenia 3*

Zyskuje [Nieustający Głód] według następujących warunków (maks. 50 na turę):  
- Zużywając Licznik [Pulsacja], zyskuje stosy równy zużytym Licznikom  
- Gdy podstawowe Umiejętności odzyskują HP innym sojusznikom, zyskuje stosy równy rzeczywistej wartości leczenia  
- Zyskuje 1 stos za każde łączne utracone 10 HP sojuszników  
- Przy trafieniu podstawowym atakiem innego sojusznika Le Rouge zyskuje 2 stosy  
- Na koniec tury zyskuje 5 stosów za każdego sojusznika Le Rouge na polu poza tą jednostką  
  
Na koniec tury, przy 100+ [Nieustający Głód], jeżeli nie ma [Szlachetna Duma], na początku następnej tury zamienia Umiejętność dolnego wiersza lewego slotu na „La Voracité”  
  
Na początku walki, jeżeli po raz pierwszy w tej walce wyposażona jest „La Voracité” albo „La Castration”, zyskuje [Rozpaczliwy Głód] i [Szlachetna Duma] oraz usuwa swój Próg Oszołomienia  
- Zamienia wyposażone podstawowe Umiejętności na Umiejętności wyłączne [Szlachetna Duma]  
- Podstawowe Umiejętności celujące w sojuszników atakują nieoparciego losowego wroga  
- Na koniec ataku Umiejętności uruchomionej tym efektem zużywa cały [Nieustający Głód]  
  
Na koniec tury, przy 150 [Nieustający Głód], jeżeli ma [Szlachetna Duma], a na początku następnej tury nie ma „La Voracité” na panelu, zamienia jedną podstawową Umiejętność na „La Voracité” (najpierw dolna Umiejętność lewego slotu)

#### Pasywka bojowa: La Moisson

*od ulepszenia 3*

Gdy efekty jej podstawowych Umiejętności zużywają HP sojusznika, ten nie zostaje Ogłuszony tymi efektami, a jego HP nie spada poniżej 1  
  
Przy Rezonansie Żądzy 3+, na koniec walki nakłada [Rozpaczliwy Głód] w następnej turze na (Rezonans Żądzy / 3) Sojuszników poza tą jednostką (zaokrąglone w górę)  
- Najpierw sojusznicy Le Rouge, nakładane w kolejności przydziału  
- Jeżeli ma [Szlachetna Duma], nakłada ten efekt na +1 więcej sojusznika (maks. 4)  
  
Jeżeli nie ma [Szlachetna Duma]:  
- Przy użyciu Umiejętności [Dwubiegunowość] na sojuszniku nakłada 1 [Asysta przy Boskości] na działającego sojusznika Le Rouge z najwyższym obecnym HP (1 raz na turę)  
- Na koniec podstawowego ataku [Osobowość Ładowania] poza tą jednostką, jeżeli główny cel nie zginął, stosuje „Je vous aide” przeciwko temu wrogowi (1 raz na turę)  
  
Jeżeli ma [Szlachetna Duma]:  
- Zyskuje [Czerwona Kołyska]  
- Aktywuje [Bufet【Buffet】] na obecnym polu bitwy  
- Na koniec tury zyskuje [Rozpaczliwy Głód] w następnej turze  
- Na początku walki nakłada 1 [Asysta przy Boskości] na działającego sojusznika Le Rouge z najwyższym obecnym HP  
- Na koniec ataku podstawową Umiejętnością ataku przeciwko wrogom, jeżeli główny cel ma 5 stosów [L'Abject], stosuje „La Demande” (1 raz na turę)

#### Pasywka bojowa: La Jouissance phallique

*od ulepszenia 3*

Zwiększa własny Licznik [Pulsacja] o 1 za każde uruchomienie [Krwawienie] podczas walki (maks. 10 razy na turę)  
  
Na koniec walki, jeżeli nie jest w stanie [Paroksyzm] i ma 15+ Licznika [Pulsacja], zużywa cały Licznik [Pulsacja], aby w następnej turze zyskać 3 [Paroksyzm]  
- Odzyskuje Poczytalność równą (3 x Liczniki [Pulsacja] zużyte ponad 15) (maks. 15)  
  
Po wygaśnięciu [Paroksyzm] zużywa cały własny Licznik [Pulsacja], odzyskując HP równy (zużyte Liczniki [Pulsacja] x 2)  
  
Zyskuje 1 Mocy [Pulsacja] za każde łączne zużycie 10 własnego Licznika [Pulsacja] podczas walki  
  
Podstawowe Umiejętności ataku i umiejętności Kontry możliwe w starciu traktowane są jako Umiejętności zyskujące Licznik [Ładowanie]

#### Pasywka bojowa: Les Pouvoirs de la vie

*od ulepszenia 3; posiadane 2× Żądza, posiadane 2× Obżar.*

Gdy sojusznik Le Rouge zostaje Ogłuszony obrażeniami, stosuje na nim „Le Manque-à-être” (1 raz na turę, z wyłączeniem wymuszonego Ogłuszenia)  
  
Jeżeli nie ma [Szlachetna Duma]:  
- Gdy sojusznik spoza Le Rouge zostaje Ogłuszony obrażeniami, stosuje na nim „Le Manque-à-être” (1 raz na spotkanie, z wyłączeniem wymuszonego Ogłuszenia)  
  
Jeżeli ma [Szlachetna Duma]:  
- Gdy inny sojusznik Le Rouge otrzymuje obrażenia sprowadzające HP do 0, HP nie spada poniżej 1, a ten sojusznik odzyskuje 50% Maks. HP (zaokrąglone w górę, 1 raz na spotkanie na Tożsamość)

#### Pasywka wsparcia: Obżeranie się

*od ulepszenia 3; rezonans 3× Żądza*

Na początku walki nakłada 2 [Wzrost Poziomu Ataku] na 1 Sojusznika z najniższym HP  
Na koniec ataku Umiejętnością ataku ten sojusznik odzyskuje 5% Maks. HP (min. 1, 1 raz na turę)

#### Kwestie

- **Identity Acquisition:** Memories. Experiences. What could be the proof of "me," I wonder? I've made the climb again to find the answer no one's been able to give me.
- **Morning Greeting:** A season begins again, and before long, it comes to an end. Then when one season ends, another begins. Season after season, the events within remain the same; but they are, in truth, trapped in a greater cycle: the cycle of the Voices—or, rather, the "Giants."
- **Afternoon Greeting:** I thought the sunlight, the alien Voice... held the answer to my question. But... the sunlight gave me no answers, instead offering only encouragement... Maybe I don't yet have anything that I... truly desire...
- **Evening Greeting:** Off-season... sale...? But why keep these piled here? I don't get it. If they don't sell, just eat them up. Start with the nearest dish, then move on to the next one until there's none left.
- **Chatter #1:** Watching everything unfold exactly as I'd known it would is... such a scary feeling. So why does the Obsidian God keep trying to decide how everything must end? What worth could there be in a hollow cycle... that only spins in place...?
- **Chatter #2:** ... The longer the adventure gets, the more I find words and expressions that I can't share with others. And even when I do, they don't seem to understand me. Maybe that's why I've begun talking to myself more and more frequently. At least the hunger subsides a little when I'm chewing on something.
- **Chatter #3:** Why does everything have to end with death? Why can't we just start from the beginning again? I... don't get it. I don't like it. Why can't we just start over after we die? That way, we wouldn't ever have to hesitate before making a choice... That way, we could keep experiencing...
- **Post-Uptie Chat 1:** As I uncovered more and more of the unknown world, the cold retreated to an unseen corner of my mind; the hunger beneath my notice as the hollow of my heart filled. But now that I have learned all there is to be learned... I feel only the cold... and the loneliness.
- **Post-Uptie Chat 2:** This insatiable emptiness... this unquenchable thirst... Neither of these is mine, yet I cannot help but think they are. Every thread that comprises my being is... a wish of another, nailed into the sense of hunger. Then, this instinctive, unbearable voracity has to be... my nature, my fate to bear.
- **Idle:** Undo only the silkiest threads... Grow tall and strong...
- **Uptying:** At long last, the Buffet is served. We—I—shall devour this department store from foundation to apex, so that none among you shall ever scrape an empty plate again.
- **Deployment:** I can't stop if I'm going to reach what I desire.
- **Stage Entry:** I don the virtues and ascend.
- **Viewed in Battle 1:** ... Why did you call me?
- **Viewed in Battle 2:** ... If you have questions to ask, raise your hand and wait. I will answer them one at a time.
- **Commencing Attack 1:** I can't stop myself anymore.
- **Commencing Attack 2:** Pour forth.
- **Enemy Staggered 1:** Move...
- **Enemy Staggered 2:** I drink when my throat burns with thirst.
- **Staggered 1:** It hurts...
- **Staggered 2:** It hurts...
- **On Kill 1:** ... To the rock bottom you fall.
- **On Kill 2:** I eat when I'm hungry, no more, no less.
- **Death #1:** Next time... I'll... climb higher...
- **Death #2:** ... I didn't want to... hurt anymore...
- **Check Passed:** I just happened to know the answer ahead of time. It wasn't... a divine prophecy or anything.
- **Check Failed:** There is no better way to escape our fate.
- **Victory Cry:** I am a being woven from threads of fathomless hunger... This paltry "feast" cannot fill me. Bring me more. Scour for the Obsidian God's delicacies and present them before me—I should like to devour all that comes within my sight.
- **Extra Conditions Fulfilled:** Mark my words, Obsidian God. At the end of this adventure... I *will* wrest free of my fate as you have gazed it.
- **Defeat Wail:** ... I am once again reduced to an experience. I am still nothing more than an experience that ravenously devours...

### 000 Biuro Klin Fikser — Sinclair

> Siedemnasta Tożsamość Sinclair

| Parametr                  | Wartość bazowa                                              |
| ------------------------- | ----------------------------------------------------------- |
| Rzadkość                  | 000                                                         |
| Sezon                     | wydarzenie 9110                                             |
| HP                        | 72 (+2,52 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–6 / 4–6                                       |
| Poziom obrony             | poziom +0                                                   |
| Odporności                | Cięcie ×1 (Normal), Kłucie ×0,5 (Endured), Obuch ×2 (Fatal) |
| Progi Stagger (HP)        | 60% / 30%                                                   |
| Grzech wyróżniony         | Obżar.                                                      |
| Przynależność             | Wedge                                                       |
| Słowa kluczowe            | Oddech, Wstrząs                                             |
| Data aktualizacji         | 20261112                                                    |

#### Umiejętność 1 (×3): Zderzenie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Obżar. | Kłucie |          2 |         +4 |      2 |           +2 |    1 |
|          3 | Obżar. | Kłucie |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zyskuje 1 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +1  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Ponownie używa ostatnią monetę 1 raz  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Wstrząs]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Klin - Don Kichot]

*Od ulepszenia 2:* [Przy Użyciu] Moc Końcowa +1 za każde 4 (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) (maks. 2)  
[Przy Użyciu] Zyskuje 2 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +2  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Ponownie używa ostatnią monetę 1 raz  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Wstrząs]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Klin - Don Kichot]

*Od ulepszenia 4:* [Przy Użyciu] Moc Końcowa +1 za każde 4 (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) (maks. 3)  
[Przy Użyciu] Zyskuje 2 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +2  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Ponownie używa ostatnią monetę 1 raz  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada 2 [Wstrząs]  
Moneta 2: [Ponowne Użycie - Przy Trafieniu] Nakłada 1 [Klin - Don Kichot]

#### Umiejętność 2 (×2): Korzystając z Impetu

| Ulepszenie | Grzech   | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | -------- | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lenistwo | Kłucie |          3 |         +4 |      3 |           +2 |    1 |
|          3 | Lenistwo | Kłucie |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Zyskuje 2 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje 1 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada +2 Licznika [Wstrząs]

*Od ulepszenia 2:* [Przy Użyciu] Przy 6+ (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 3 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada +2 Licznika [Wstrząs]  
Moneta 3: Zadaje +5% obrażeń za każde 1 [Ocena Pola Walki] (maks. 15%)

*Od ulepszenia 4:* [Przy Użyciu] Przy 6+ (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 3 [Oddech]  
Moneta 1: [Przy Trafieniu] Zyskuje 2 [Oddech]  
Moneta 2: [Przy Trafieniu] Nakłada +2 Licznika [Wstrząs]  
Moneta 3: Zadaje +5% obrażeń za każde 1 [Ocena Pola Walki] (maks. 20%)

#### Umiejętność 3 (×1): Zamieć Włócznią

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Pycha  | Kłucie |          3 |         +3 |      4 |           +3 |    1 |
|          4 | Pycha  | Kłucie |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* [Przy Użyciu] Przy 6+ (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 2 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +1  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Zadaje +20% obrażeń  
Moneta 2: [Przy Trafieniu] Zyskuje 4 [Oddech]  
Moneta 3: [Przy Trafieniu] Nakłada +3 Licznika [Wstrząs]  
Moneta 4: Zadaje +10% obrażeń za każde 1 [Ocena Pola Walki] (maks. 40%)  
Moneta 4: Jeżeli cel jest w stanie [Konwersja Amplitudy] lub [Splątanie Amplitudy], zadaje +20% obrażeń  
Moneta 4: [Przy Trafieniu] Jeżeli cel nie jest w stanie [Konwersja Amplitudy], wywołuje [Konwersja Amplitudy] do [Wstrząs - Rozpad]  
Moneta 4: [Przy Trafieniu] Wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

*Od ulepszenia 4:* [Przy Użyciu] Przy 6+ (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 2 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +3  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Zadaje +30% obrażeń  
Moneta 2: [Przy Trafieniu] Zyskuje 4 [Oddech]  
Moneta 3: [Przy Trafieniu] Nakłada +3 Licznika [Wstrząs]  
Moneta 4: Zadaje +10% obrażeń za każde 1 [Ocena Pola Walki] (maks. 40%)  
Moneta 4: Jeżeli cel jest w stanie [Konwersja Amplitudy] lub [Splątanie Amplitudy], zadaje +30% obrażeń  
Moneta 4: [Przy Trafieniu] Jeżeli cel nie jest w stanie [Konwersja Amplitudy], wywołuje [Konwersja Amplitudy] do [Wstrząs - Rozpad]  
Moneta 4: [Przy Trafieniu] Wywołuje [Wybuch Wstrząsu]. Zmniejsza Licznik [Wstrząs] celu o 1

#### Umiejętność 4 (×0): Przebiję cię Szybko i Pewnie

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Pycha  | Kłucie |          4 |         +5 |      3 |           +4 |    1 |
|          4 | Pycha  | Kłucie |          5 |         +5 |      3 |           +4 |    1 |

*Od ulepszenia 3:* Ta Umiejętność traktowana jest jako Umiejętność ataku nawet przy uruchomieniu zamiast Umiejętności obrony; nie podlega efektom zmieniającym Moc obrony, a podlega efektom zmieniającym Moc ataku  
Moc Starcia +1 za każde 2 [Klin - Don Kichot] celu (maks. 4)  
[Przy Użyciu] Przy 6+ (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 2 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +1  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Zadaje +20% obrażeń  
[Koniec Ataku] Usuwa cały [Klin - Don Kichot] celu  
[Koniec Ataku] Sojusznik Tożsamości Wedge Office Rep Outis zyskuje 3 [Przewaga]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zyskuje 4 [Oddech]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 2: [Przy Trafieniu] Nakłada +3 Licznika [Wstrząs]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: Zadaje +10% obrażeń za każde 1 [Ocena Pola Walki] (maks. 40%)  
Moneta 3: Jeżeli cel jest w stanie [Konwersja Amplitudy] lub [Splątanie Amplitudy], zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Ponownie używa tę monetę (1 raz na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Jeżeli cel nie jest w stanie [Konwersja Amplitudy], uruchamia [Konwersja Amplitudy] w [Wstrząs - Rozpad]  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Zadaje obrażenia Przebijające równe ([Klin - Don Kichot] celu x 6)% końcowych obrażeń tej monety (maks. 48%)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Wywołuje [Wybuch Wstrząsu] 2 razy. Zmniejsza Licznik [Wstrząs] celu o 2

*Od ulepszenia 4:* Ta Umiejętność traktowana jest jako Umiejętność ataku nawet przy uruchomieniu zamiast Umiejętności obrony; nie podlega efektom zmieniającym Moc obrony, a podlega efektom zmieniającym Moc ataku  
Moc Starcia +1 za każde 2 [Klin - Don Kichot] celu (maks. 4)  
[Przy Użyciu] Przy 6+ (suma Mocy [Oddech] własnej i Mocy [Wstrząs] celu) Moc Monet +1  
[Przy Użyciu] Zyskuje 2 [Oddech]  
[Więź]: Po Rezonansie z Umiejętnościami Wedge Office Fikser Don Quixote uruchamia poniższe efekty (1 raz na turę):  
- [Przy Użyciu] Moc Starcia +3  
- [Przy Użyciu] Zyskuje 1 [Ocena Pola Walki]  
- [Przy Użyciu] Zadaje +30% obrażeń  
[Koniec Ataku] Usuwa cały [Klin - Don Kichot] celu  
[Koniec Ataku] Sojusznik Tożsamości Wedge Office Rep Outis zyskuje 3 [Przewaga]  
Moneta 1: [Moneta Niezniszczalna]  
Moneta 1: [Przy Trafieniu] Zyskuje 4 [Oddech]  
Moneta 2: [Moneta Niezniszczalna]  
Moneta 2: [Przy Trafieniu] Nakłada +3 Licznika [Wstrząs]  
Moneta 3: [Moneta Niezniszczalna]  
Moneta 3: Zadaje +10% obrażeń za każde 1 [Ocena Pola Walki] (maks. 40%)  
Moneta 3: Jeżeli cel jest w stanie [Konwersja Amplitudy] lub [Splątanie Amplitudy], zadaje +30% obrażeń  
Moneta 3: [Przy Trafieniu] Ponownie używa tę monetę (1 raz na Umiejętność)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Jeżeli cel nie jest w stanie [Konwersja Amplitudy], uruchamia [Konwersja Amplitudy] w [Wstrząs - Rozpad]  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Zadaje obrażenia Przebijające równe ([Klin - Don Kichot] celu x 6)% końcowych obrażeń tej monety (maks. 48%)  
Moneta 3: [Ponowne Użycie - Przy Trafieniu] Wywołuje [Wybuch Wstrząsu] 2 razy. Zmniejsza Licznik [Wstrząs] celu o 2

#### Obrona: Wyrównanie Oddechu

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pycha  | obrona: unik |          3 |        +10 |      1 |           +2 |    1 |
|          4 | Pycha  | obrona: unik |          4 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [Przy Użyciu] Przy 6+ Mocy [Oddech] Moc Monet +1  
[Udany Unik] Zyskuje 1 [Oddech] (3 razy na turę)  
[Koniec Walki] Jeżeli ta jednostka nie zyskała w tej turze [Ocena Pola Walki] efektami Umiejętności, zyskuje 1 [Ocena Pola Walki] (1 raz na turę)

*Od ulepszenia 3:* [Początek Walki] Jeżeli cel ma 4+ [Klin - Don Kichot], zamiast tego stosuje „Przebiję cię Szybko i Pewnie” (1 raz na turę; uruchamia się także przy atakach nieopartych)  
[Przy Użyciu] Przy Mocy [Oddech] 6 lub wyższej Moc Monet +1  
[Udany Unik] Zyskuje 2 [Oddech] (3 razy na turę)  
[Koniec Walki] Jeżeli w tej turze nie zyskała [Ocena Pola Walki] efektami Umiejętności, zyskuje 1 [Ocena Pola Walki] (1 raz na turę)

*Od ulepszenia 4:* [Początek Walki] Jeżeli cel ma 4+ [Klin - Don Kichot], zamiast tego stosuje „Przebiję cię Szybko i Pewnie” (1 raz na turę; uruchamia się także przy atakach nieopartych)  
[Przy Użyciu] Przy Mocy [Oddech] 6 lub wyższej Moc Monet +1  
[Udany Unik] Zyskuje 2 [Oddech] (3 razy na turę)  
[Udany Unik] Zyskuje 1 [Pośpiech] w następnej turze (1 raz na turę)  
[Koniec Walki] Jeżeli w tej turze nie zyskała [Ocena Pola Walki] efektami Umiejętności, zyskuje 1 [Ocena Pola Walki] (1 raz na turę)

#### Pasywka bojowa: Panie Don Quixote... skupmy się na zadaniu.

*od ulepszenia 1*

W menu wyposażenia drużyny:  
- Wybranie Wedge Office Fikser Sinclair automatycznie wybiera Tożsamość Don Quixote jako Wedge Office Fikser Don Quixote  
- Odwołanie Wedge Office Fikser Don Quixote automatycznie wybiera Tożsamość Sinclair jako najnowszą wybraną Tożsamość, która nie jest Wedge Office Fikser Sinclair (jeżeli Tożsamość Wedge Office Fikser Sinclair była już wybrana przy wejściu do menu wyposażenia, jej odwołanie automatycznie wybierze LCB Grzesznik Sinclair)  
  
Od początku tury do rozpoczęcia walki, jeżeli Szybkość jest niższa niż Szybkość sojusznika Tożsamości Wedge Office Fikser Don Quixote, Szybkość rośnie, aż wartości się zrównają (ten efekt nie uruchamia się, jeżeli którakolwiek z tych dwóch Tożsamości ma -45 Poczytalności albo działa na nią efekt unieruchamiający Szybkość)

#### Pasywka bojowa: Wbijanie Klinu

*od ulepszenia 1*

Na początku tury zyskuje 1 [Ocena Pola Walki]  
  
Po spełnieniu któregokolwiek z poniższych warunków nakłada 1 [Klin - Sinclair] na główny cel (1 raz na turę)  
- Przy trafieniu ostatnią monetą Umiejętności ataku w główny cel  
- Przy skutecznym uniku wszystkich monet Umiejętności agresora Umiejętnością uniku

#### Pasywka bojowa: Ramię w ramię w świetle świtu

*od ulepszenia 1*

Gdy sojusznik Tożsamości Dawn Office Fikser Faust używa Umiejętności „Rozczłonkowanie w Południe”, moneta 2 tej Umiejętności zyskuje poniższe efekty (1 raz na turę):  
- [Więź]: Wedge Office Fikser Sinclair  
· [Przy Trafieniu] Nakłada 2 [Podpalenie] i zwiększa Licznik [Podpalenie] o 2  
· [Przy Trafieniu] Nakłada 2 [Wstrząs]  
· [Przy Trafieniu] Nakłada 1 [Klin - Sinclair]  
· [Przy Trafieniu] Sojusznik Tożsamości Wedge Office Rep Outis zyskuje 1 [Braterstwo Świtu]

#### Pasywka bojowa: Panie Don Quixote... skupmy się na zadaniu.

*od ulepszenia 2*

W menu wyposażenia drużyny:  
- Wybranie Wedge Office Fikser Sinclair automatycznie wybiera Tożsamość Don Quixote jako Wedge Office Fikser Don Quixote  
- Odwołanie Wedge Office Fikser Don Quixote automatycznie wybiera Tożsamość Sinclair jako najnowszą wybraną Tożsamość, która nie jest Wedge Office Fikser Sinclair (jeżeli Tożsamość Wedge Office Fikser Sinclair była już wybrana przy wejściu do menu wyposażenia, jej odwołanie automatycznie wybierze LCB Grzesznik Sinclair)  
  
Od początku tury do rozpoczęcia walki, jeżeli Szybkość jest niższa niż Szybkość sojusznika Tożsamości Wedge Office Fikser Don Quixote, Szybkość rośnie, aż wartości się zrównają (ten efekt nie uruchamia się, jeżeli którakolwiek z tych dwóch Tożsamości ma -45 Poczytalności albo działa na nią efekt unieruchamiający Szybkość)

#### Pasywka bojowa: Wbijanie Klinu

*od ulepszenia 2*

Na początku tury zyskuje 1 [Ocena Pola Walki]  
  
Po spełnieniu któregokolwiek z poniższych warunków nakłada 1 [Klin - Sinclair] na główny cel (1 raz na turę)  
- Przy trafieniu ostatnią monetą Umiejętności ataku w główny cel  
- Przy skutecznym uniku wszystkich monet Umiejętności agresora Umiejętnością uniku

#### Pasywka bojowa: Ramię w ramię w świetle świtu

*od ulepszenia 2*

Gdy sojusznik Tożsamości Dawn Office Fikser Faust używa Umiejętności „Rozczłonkowanie w Południe”, moneta 2 tej Umiejętności zyskuje poniższe efekty (1 raz na turę):  
- [Więź]: Wedge Office Fikser Sinclair  
· [Przy Trafieniu] Nakłada 2 [Podpalenie] i zwiększa Licznik [Podpalenie] o 2  
· [Przy Trafieniu] Nakłada 2 [Wstrząs]  
· [Przy Trafieniu] Nakłada 1 [Klin - Sinclair]  
· [Przy Trafieniu] Sojusznik Tożsamości Wedge Office Rep Outis zyskuje 1 [Braterstwo Świtu]

#### Pasywka bojowa: Łowcy Miasta

*od ulepszenia 2; posiadane 2× Lenistwo, posiadane 2× Pycha*

Na koniec walki przy 10+ Mocy [Oddech] zyskuje w następnej turze 1 [Pośpiech]  
  
Przy ponad 20 Mocy [Oddech] podstawowe Umiejętności zadają +(nadwyżka)% więcej obrażeń przy trafieniu krytycznym (maks. 15%)

#### Pasywka bojowa: Panie Don Quixote... skupmy się na zadaniu.

*od ulepszenia 4*

W menu wyposażenia drużyny:  
- Wybranie Wedge Office Fikser Sinclair automatycznie wybiera Tożsamość Don Quixote jako Wedge Office Fikser Don Quixote  
- Odwołanie Wedge Office Fikser Don Quixote automatycznie wybiera Tożsamość Sinclair jako najnowszą wybraną Tożsamość, która nie jest Wedge Office Fikser Sinclair (jeżeli Tożsamość Wedge Office Fikser Sinclair była już wybrana przy wejściu do menu wyposażenia, jej odwołanie automatycznie wybierze LCB Grzesznik Sinclair)  
  
Od początku tury do rozpoczęcia walki, jeżeli Szybkość jest niższa niż Szybkość sojusznika Tożsamości Wedge Office Fikser Don Quixote, Szybkość rośnie, aż wartości się zrównają (ten efekt nie uruchamia się, jeżeli którakolwiek z tych dwóch Tożsamości ma -45 Poczytalności albo działa na nią efekt unieruchamiający Szybkość)

#### Pasywka bojowa: Wbijanie Klinu

*od ulepszenia 4*

Na początku tury zyskuje 1 [Ocena Pola Walki]  
  
Po spełnieniu któregokolwiek z poniższych warunków nakłada 1 [Klin - Sinclair] na główny cel (1 raz na turę)  
- Przy trafieniu ostatnią monetą Umiejętności ataku w główny cel  
- Przy skutecznym uniku wszystkich monet Umiejętności agresora Umiejętnością uniku

#### Pasywka bojowa: Ramię w ramię w świetle świtu

*od ulepszenia 4*

Gdy sojusznik Tożsamości Dawn Office Fikser Faust używa Umiejętności „Rozczłonkowanie w Południe”, moneta 2 tej Umiejętności zyskuje poniższe efekty (1 raz na turę):  
- [Więź]: Wedge Office Fikser Sinclair  
· [Przy Trafieniu] Nakłada 2 [Podpalenie] i zwiększa Licznik [Podpalenie] o 2  
· [Przy Trafieniu] Nakłada 2 [Wstrząs]  
· [Przy Trafieniu] Nakłada 1 [Klin - Sinclair]  
· [Przy Trafieniu] Sojusznik Tożsamości Wedge Office Rep Outis zyskuje 1 [Braterstwo Świtu]

#### Pasywka bojowa: Łowcy Miasta

*od ulepszenia 4; posiadane 2× Lenistwo, posiadane 2× Pycha*

Na koniec walki przy 10+ Mocy [Oddech] zyskuje w następnej turze 1 [Pośpiech]  
  
Przy ponad 20 Mocy [Oddech] podstawowe Umiejętności zadają +(nadwyżka)% więcej obrażeń przy trafieniu krytycznym (maks. 25%)

#### Pasywka wsparcia: Dostosowanie Tempa

*od ulepszenia 3; posiadane 4× Pycha*

Na koniec tury nakłada 1 [Pośpiech] w następnej turze na 1 Tożsamość sojusznika z najniższą Szybkością (najpierw Fikserzy)  
- Jeżeli ta Tożsamość sojusznika jest Fikserem, zamiast tego nakłada 1 [Pośpiech] i 1 [Wzrost Poziomu Ataku] w następnej turze

#### Kwestie

- **Identity Acquisition:** 'Twas my spear that skewered the foe's throat last! Surely that kill is mine to claim? That leaves thee with two, young Sinclair. Fair's fair. What kind of logic is that? We *both* ran that one through—so that's two and a half each. Seriously, how do you say that with a straight face?
- **Morning Greeting:** Young Sinclair!! Come thee to the cupboard...! Prithee, fetch down the cereal...! Who saw fit to place it at such a lofty height?! ... I did. When I used to be able to reach it. Now I can't. W-well, that's... You know, if you'd actually bothered to read the fine print on the insurance, I wouldn't have been stuck like this...
- **Afternoon Greeting:** "Tangsu*yuk*". "Yukgae*jang*"! "Jambon-beur*re*". Re... "Reblochon on potato gra*tin*"! Ugh... Tang... "Tangba*o*"...? O... "Omuri*ce*"! What sayest thou to that? Heh. "Smørre*brød*". Ehhhh?! "Ble"? "Bro"? What manner of food is that?! It's an open-faced sandwich. All right, then. Guess you're buying lunch today. *groan* Very well. I shall fetch some omurice... to go.
- **Evening Greeting:** Nnngh...! *huff* *huff* Every evening... 'tis the same nightmare—those wretches tearing young Sinclair limb from limb, again and again... ...? Did you call me? Ah, n-nay! 'Tis nothing, nothing at all!
- **Chatter #1:** ... Don Quixote, please tell me you haven't forgotten the upcoming insurance renewal. Hm?! N-nay, of course not...! ... And go over the add-ons. I swear, if you forget to get the clone body's growth shots covered again, I'm gonna... *sigh* 'Twas my fault, forsooth... Have I not admitted my guilt often enough...?
- **Chatter #2:** Ugh... You know, you're getting *insufferable*. Nobody said you were wrong or anything. Verily, we ought to give him some space, young Sinclair... He hath yet to recover... No, enough is enough. All we said was we'll work together on this one job 'cause Fixers who think like you aren't a good fit for our Office, simple as that. And you had to be a miserable ass about it out of the blue! Could you please... never mind. Look, you little—stop frowning already, would you?
- **Chatter #3:** A wedge, thou seest, is a weapon most divorced from cleaving and crushing. Behold the pinpoint-keen tip of this spear mine: dost thou see?! 'Tis a weapon of unparalleled efficiency! A strike most singular and focus most fine requireth little strength to execute. Such is the work befitting a "Wedge!" Consequently! Those who seek our Office with a quest in their bosom expect no brute strength, nay; 'tis swiftness and precision... founded upon the bedrock of shrewd and precise situational assessment! Heh heh, *that* is what our Office is!
- **Post-Uptie Chat 1:** Not exactly the kind of situation where we can afford to be polite. I'll get to skewering you right away. As a Fixer, I can scarce afford proper etiquette when lives stand at stake! Surely thou canst understand!
- **Post-Uptie Chat 2:** Our Office has particularly low tolerance for dickheads who like to dress themselves up as "selfless." Doubly so when the most selfish of them don't seem to realize that himself.
- **Idle:** ... How long is that punk going to leech on our Office? Prithee, practice patience! Thou recallest Lady Outis's reassurance, dost thou not? He shall depart anon following this contract's completion.
- **Uptying:** Hey, don't glare at us now. We just poked you to make sure. Heh heh, I had heard that thou wert supposed to be "nice"—I expect naught else but the maximum generosity from thee!
- **Deployment:** ... Are you trying to pick a fight with me?
- **Stage Entry:** I'll skewer you all.
- **Viewed in Battle:** ... Don Quixote told you to talk to me, didn't she? Tell her I don't have time for chit-chat either!
- **Commencing Attack:** Skewer!
- **Enemy Stagger:** Let's make this quick.
- **Staggered:** Tsk, no help at all...
- **Enemy Killed:** You guys always end up on a skewer, anyway.
- **Death:** What an... idiotic move...
- **Check Passed:** ... All in a day's work.
- **Check Failed:** ... Heard you the first time! C'mon, this *has* to be right...
- **Victory Cry:** Phew... That be one quest behind us! What sayest thou, young Sinclair, to a moment's respite? We still have some headaches to deal with, but... Eh, it's whatever at this point, right?
- **Extra Conditions Fulfilled:** They gave us some trouble, but— —verily, once accepted, no contract is beyond us! Yeah, this contract was also— —settled in the Wedgiest fashion! ARRRGH!!!!! Holy shit, can you stop cutting me off for one damn second?!
- **Defeat Wail:** Damn punk... I knew he'd hightail it the moment shit hit the fan... Alas... 'twas an expected outcome, was it not...? Tsk, don't talk...! You're gonna lose more blood than insurance's willing to cover...
