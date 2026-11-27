# Limbus Company — Faust: Identity

*Profil postaci: dane liczbowe z tabel gry, opisy z plików lokalizacji.*

## Zakres i zasady odczytu

- Teksty w wersji `en`; liczby z `StaticData` (wartości bazowe, bez E.G.O i bonusów).
- **Ulepszenie** = Uptie (gaksung) 1–4; tabela umiejętności pokazuje tylko wiersze, w których coś się zmienia. Moc ataku = moc bazowa + moc monety za każdą wyrzuconą reszkę/orła wg reguł gry.
- **Poziom ataku/obrony** to korekta względem poziomu postaci.
- **Odporności**: mnożnik obrażeń danego typu (×2 = Fatal, ×0,5 = Endured).
- Elementy bez opisu w danych są oznaczone „—”, nie zgadywane.

## Akta więźnia

> The Sinner who developed the engine of Mephistopheles, the bus operated by Limbus Company.
> She claims that there is no one in the City who could rival her library of knowledge and wisdom,
> and she isn't necessarily wrong.
> You might find her high and mighty attitude when she allows you to converse with her displeasing,
> but as seen with how she treats everyone with subtle gestures of arrogance, there is no hope of her parting with it, ever.
> We recommend simply nodding once and getting over it.
> Even though she has an unparalleled genius, we can't quite figure out how to use this one.
> Perhaps you could be the one to find out?

## Katalog Identity

| Rzadkość | Identity                                  |           Sezon | Grzech wyróżniony | Słowa kluczowe |
| -------: | ----------------------------------------- | --------------: | ----------------- | -------------- |
|        0 | LCB Sinner                                |               0 | Pride             | —              |
|       00 | W Corp. L2 Cleanup Agent                  |               0 | Envy              | Charge         |
|       00 | Lobotomy Corp. Remnant                    |               1 | Lust              | Rupture, Poise |
|      000 | The One Who Grips                         |               1 | Lust              | Bleed          |
|       00 | Zwei Assoc. South Section 4               |               0 | Envy              | —              |
|      000 | Seven Assoc. South Section 4              |               0 | Glut.             | Rupture        |
|      000 | Lobotomy E.G.O::Regret                    | wydarzenie 9101 | Wrath             | Tremor         |
|      000 | Blade Lineage Salsu                       |               3 | Pride             | Poise, Bleed   |
|       00 | Wuthering Heights Butler                  |               4 | Pride             | Sinking        |
|      000 | MultiCrack Office Rep                     |               4 | Gloom             | Charge         |
|      000 | LCE E.G.O:: Ardor Blossom Star            |               5 | Wrath             | Burn           |
|      000 | Heishou Pack - Mao Branch Adept           |               6 | Glut.             | Rupture        |
|      000 | Shi Assoc. East Section 3                 |               0 | Wrath             | Bleed, Poise   |
|      000 | The Index Proselyte: 【Paper Slip】       |               7 | Sloth             | Poise, Sinking |
|      000 | The House of Spiders: The Ring Apprentice |               7 | Glut.             | Bleed, Charge  |
|      000 | Dawn Office Fixer                         | wydarzenie 9109 | Pride             | Burn, Tremor   |

## Profile

### 0 LCB Sinner — Faust

> Faust’s 1st Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 0                                                          |
| Sezon                     | 0                                                          |
| HP                        | 84 (+2,9 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 1–3 / 2–3 / 2–4 / 2–4                                      |
| Poziom obrony             | poziom +1                                                  |
| Odporności                | Slash ×2 (Fatal), Pierce ×0,5 (Endured), Blunt ×1 (Normal) |
| Progi Stagger (HP)        | 60% / 30% / 15%                                            |
| Grzech wyróżniony         | Pride                                                      |
| Przynależność             | Limbus_Company, Limbus_Company_Lcb                         |
| Słowa kluczowe            | —                                                          |
| Data aktualizacji         | 20230227                                                   |

#### Umiejętność 1 (×3): Downward Slash

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Blunt |          2 |         +7 |      1 |           −1 |    1 |
|          3 | Pride  | Blunt |          3 |         +7 |      1 |           −1 |    1 |
|          4 | Pride  | Blunt |          4 |         +7 |      1 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 1: [Heads Hit] Inflict 1 [Paralyze]

*Od ulepszenia 2:* Moneta 1: [On Hit] Inflict 1 [Paralyze]

#### Umiejętność 2 (×2): Upward Slash

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Blunt |          3 |         +4 |      2 |           −1 |    1 |
|          3 | Sloth  | Blunt |          4 |         +4 |      2 |           −1 |    1 |
|          4 | Sloth  | Blunt |          5 |         +4 |      2 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Heads Hit] Inflict 2 [Offense Level Down] next turn

*Od ulepszenia 2:* Moneta 2: [On Hit] Inflict 3 [Offense Level Down] next turn

#### Umiejętność 3 (×1): Drilling Stab

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Glut.  | Pierce |          6 |         +2 |      2 |           −1 |    1 |
|          4 | Glut.  | Pierce |          7 |         +2 |      2 |           −1 |    1 |

Moneta 1: [Heads Hit] Inflict 1 [Attack Power Down] next turn  
Moneta 2: [On Hit] Inflict 1 [Attack Power Down] next turn

#### Obrona: Evade

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          2 |        +10 |      1 |           +1 |    1 |
|          4 | Pride   | obrona: unik |          2 |        +10 |      1 |           +1 |    1 |

#### Pasywka bojowa: Analytic Eye

*od ulepszenia 1; rezonans 2× Pride*

Deal +10% damage to targets that have negative status effects

#### Pasywka wsparcia: Keen Observation

*od ulepszenia 3; posiadane 3× Pride*

1 ally that has the highest max HP inflicts 2 [Offense Level Down] at 25% chance on hit

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

### 00 W Corp. L2 Cleanup Agent — Faust

> Faust’s 2nd Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 00                                                         |
| Sezon                     | 0                                                          |
| HP                        | 88 (+3,05 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 1–3 / 2–3 / 2–4 / 2–4                                      |
| Poziom obrony             | poziom +3                                                  |
| Odporności                | Slash ×1 (Normal), Pierce ×0,5 (Endured), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 60% / 30%                                                  |
| Grzech wyróżniony         | Envy                                                       |
| Przynależność             | W_Corp                                                     |
| Słowa kluczowe            | Charge                                                     |
| Data aktualizacji         | 20230227                                                   |

#### Umiejętność 1 (×3): Energy Cycle

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Blunt |          3 |         +6 |      1 |           −1 |    1 |
|          3 | Envy   | Blunt |          4 |         +6 |      1 |           −1 |    1 |
|          4 | Envy   | Blunt |          4 |         +8 |      1 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 1: [On Hit] Gain +1 [Charge] Count

*Od ulepszenia 2:* Moneta 1: [On Hit] Gain +2 [Charge] Count

*Od ulepszenia 4:* [On Use] Gain +2 [Charge] Count  
Moneta 1: [On Hit] Gain +2 [Charge] Count

#### Umiejętność 2 (×2): Leap

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | Blunt |          4 |         +4 |      2 |           −1 |    1 |
|          3 | Gloom  | Blunt |          5 |         +4 |      2 |           −1 |    1 |
|          4 | Gloom  | Blunt |          6 |         +4 |      2 |           −1 |    1 |

*Od ulepszenia 1:* Moneta 2: [On Hit] Consume 3 [Charge] Count to inflict 4 [Bind] next turn

*Od ulepszenia 2:* Moneta 2: [On Hit] Consume 3 [Charge] Count to inflict 4 [Bind] next turn

*Od ulepszenia 4:* [On Use] Gain +3 [Charge] Count  
Moneta 1: [On Hit] Gain +3 [Charge] Count  
Moneta 2: [On Hit] Consume 3 [Charge] Count to inflict 4 [Bind] next turn

#### Umiejętność 3 (×1): Overcharge

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Blunt |          6 |         +2 |      3 |           −1 |    1 |
|          4 | Wrath  | Blunt |          6 |         +3 |      3 |           −1 |    1 |

*Od ulepszenia 3:* Moneta 3: [On Hit] Consume 5 [Charge] Count to inflict 2 [Attack Power Down] and 3 [Paralyze] next turn

*Od ulepszenia 4:* At 5+ [Charge] Count, Clash Power +2  
Moneta 3: [On Hit] Consume 5 [Charge] Count to inflict 2 [Attack Power Down] and 3 [Paralyze] next turn

#### Obrona: Guard

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +2 |      1 |           +5 |    1 |
|          4 | Envy    | obrona: blok |         10 |         +2 |      1 |           +5 |    1 |

#### Pasywka bojowa: Self-charging

*od ulepszenia 2; posiadane 4× Envy*

Gain +1 [Charge] Count at Attack End

#### Pasywka bojowa: Self-charging

*od ulepszenia 4; posiadane 4× Envy*

Gain +1 [Charge] Count at Attack End  
A random ally gains +1 [Charge] Count at Attack End

#### Pasywka wsparcia: Radio Comms

*od ulepszenia 3; posiadane 3× Envy*

1 ally that has the lowest max HP gains +1 [Charge] Count

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

### 00 Lobotomy Corp. Remnant — Faust

> Faust’s 3rd Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 00                                                         |
| Sezon                     | 1                                                          |
| HP                        | 69 (+2,39 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 2–5 / 2–6 / 3–6 / 3–6                                      |
| Poziom obrony             | poziom −4                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×1 (Normal), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                            |
| Grzech wyróżniony         | Lust                                                       |
| Przynależność             | L_Corp                                                     |
| Słowa kluczowe            | Rupture, Poise                                             |
| Data aktualizacji         | 20230227                                                   |

#### Umiejętność 1 (×3): Sole Strike

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lust   | Slash |          2 |         +6 |      1 |           +3 |    1 |
|          3 | Lust   | Slash |          3 |         +6 |      1 |           +3 |    1 |
|          4 | Lust   | Slash |          3 |         +8 |      1 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Heads Hit] Inflict 1 [Rupture]

*Od ulepszenia 2:* Moneta 1: [On Hit] Inflict 2 [Rupture]

*Od ulepszenia 4:* [On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Inflict 2 [Rupture]

#### Umiejętność 2 (×2): Deep Cuts

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | Pierce |          3 |         +3 |      3 |           +3 |    1 |
|          3 | Gloom  | Pierce |          4 |         +3 |      3 |           +3 |    1 |
|          4 | Gloom  | Pierce |          5 |         +3 |      3 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Heads Hit] Gain 1 [Poise] next turn  
Moneta 2: [Heads Hit] Gain 1 [Poise] next turn  
Moneta 3: [Heads Hit] Gain 2 [Haste] next turn

*Od ulepszenia 2:* Moneta 1: [On Hit] Gain 1 [Poise] next turn  
Moneta 2: [On Hit] Gain 1 [Poise] next turn  
Moneta 3: [On Hit] Gain 4 [Haste] next turn

*Od ulepszenia 4:* Moneta 1: [On Hit] Gain 1 [Poise] next turn  
Moneta 2: [On Hit] Gain 1 [Poise] next turn  
Moneta 3: [On Hit] Gain 4 [Haste] next turn  
Moneta 3: [On Hit] Gain 1 [Poise] next turn

#### Umiejętność 3 (×1): Opportunistic Slash

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Envy   | Slash |          4 |         +8 |      2 |           +3 |    1 |

If this unit took no damage last turn, Coin Power +3  
Moneta 2: [Heads Hit] Inflict 5 [Rupture]

#### Obrona: Evade

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           +0 |    1 |
|          4 | Envy    | obrona: unik |          3 |        +10 |      1 |           +0 |    1 |

#### Pasywka bojowa: Resolution

*od ulepszenia 2; rezonans 2× Lust*

At the next Turn Start, at 4+ [Poise] Count, gain 2 [Haste]

#### Pasywka wsparcia: Backing

*od ulepszenia 3; rezonans 2× Lust*

1 ally that has the lowest max HP gains Final Power +2 for its Defense Skills

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

### 000 The One Who Grips — Faust

> Faust’s 4th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 1                                                          |
| HP                        | 66 (+2,28 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 4–5 / 4–6 / 4–7 / 4–7                                      |
| Poziom obrony             | poziom −1                                                  |
| Odporności                | Slash ×2 (Fatal), Pierce ×1 (Normal), Blunt ×0,5 (Endured) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                            |
| Grzech wyróżniony         | Lust                                                       |
| Przynależność             | N_Corp, N_Corp_Fnatic                                      |
| Słowa kluczowe            | Bleed                                                      |
| Data aktualizacji         | 20230323                                                   |

#### Umiejętność 1 (×3): Cackle

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Pierce |          3 |         +3 |      2 |           +4 |    1 |
|          3 | Envy   | Pierce |          4 |         +3 |      2 |           +4 |    1 |

*Od ulepszenia 1:* [Clash Win] Target loses 3 SP  
Moneta 1: [Heads Hit] Inflict 1 [Nails]  
Moneta 2: [On Hit] Inflict 1 [Bleed]

*Od ulepszenia 2:* [Clash Win] Target loses 3 SP  
Moneta 1: [On Hit] Inflict 1 [Nails]  
Moneta 2: [On Hit] Inflict 2 [Bleed]

#### Umiejętność 2 (×2): The Gripping

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lust   | Pierce |          4 |         +2 |      3 |           +4 |    1 |
|          3 | Lust   | Pierce |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 1:* Moneta 2: [On Hit] Inflict 3 [Nails]  
Moneta 3: [Heads Hit] Inflict [Gaze] next turn

*Od ulepszenia 2:* Moneta 2: [On Hit] Inflict 3 [Nails]  
Moneta 3: [Heads Hit] Inflict 1 [Paralyze] next turn  
Moneta 3: [On Hit] Inflict [Gaze] next turn

*Od ulepszenia 4:* Moneta 1: [On Hit] Inflict 2 [Nails]  
Moneta 2: [On Hit] Inflict 3 [Nails]  
Moneta 3: [Heads Hit] Inflict 1 [Paralyze] next turn  
Moneta 3: [On Hit] Inflict [Gaze] next turn

#### Umiejętność 3 (×1): Execution

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Pride  | Blunt |          6 |         +2 |      3 |           +4 |    1 |

*Od ulepszenia 3:* On kill, heal 10 SP for all allies and apply 1 [Pierce DMG Up] and [Blunt DMG Up]  
Moneta 1: [On Hit] Inflict 2 [Nails]  
Moneta 2: [Heads Hit] Inflict 2 [Nails]  
Moneta 3: Deal +50% damage to targets that have 5+ [Nails]

*Od ulepszenia 4:* On kill, heal 10 SP for all allies and apply 1 [Pierce DMG Up] and [Blunt DMG Up]  
Moneta 1: [On Hit] Inflict 2 [Nails]  
Moneta 2: [Heads Hit] Inflict 2 [Nails]  
Moneta 3: Deal +70% damage to targets that have 5+ [Nails]

#### Obrona: Such Filth

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          4 |        +10 |      1 |           +0 |    1 |
|          4 | Lust    | obrona: unik |          4 |        +10 |      1 |           +0 |    1 |

[On Evade] Target loses 3 SP

#### Pasywka bojowa: Whistles

*od ulepszenia 2; rezonans 4× Lust*

Combat Start: Heal 15 SP for 2 allies that have the lowest SP  
If the ally is an "N Corp. Fanatic", also apply 1 [Fanatic]

#### Pasywka bojowa: Whistles

*od ulepszenia 4; rezonans 4× Lust*

Combat Start: Heal 15 SP for 2 allies that have the lowest SP  
If the ally is an "N Corp. Fanatic", also apply 2 [Fanatic]

#### Pasywka wsparcia: Whispers

*od ulepszenia 3; rezonans 3× Lust*

Combat Start: Heal 15 SP for 1 ally that has the lowest SP  
If the ally is an "N Corp. Fanatic", also apply 1 [Fanatic]

#### Pasywka wsparcia: Whispers

*od ulepszenia 4; rezonans 3× Lust*

Combat Start: Heal 15 SP for 1 ally that has the lowest SP  
If the ally is an "N Corp. Fanatic", also apply 2 [Fanatic]

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

### 00 Zwei Assoc. South Section 4 — Faust

> Faust’s 5th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 00                                                         |
| Sezon                     | 0                                                          |
| HP                        | 82 (+2,82 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–5 / 4–5 / 4–6 / 4–6                                      |
| Poziom obrony             | poziom +2                                                  |
| Odporności                | Slash ×2 (Fatal), Pierce ×1 (Normal), Blunt ×0,5 (Endured) |
| Progi Stagger (HP)        | 55% / 20%                                                  |
| Grzech wyróżniony         | Envy                                                       |
| Przynależność             | Zwei                                                       |
| Słowa kluczowe            | —                                                          |
| Data aktualizacji         | 20230810                                                   |

#### Umiejętność 1 (×3): Patrolling

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Pierce |          2 |         +4 |      2 |           −1 |    1 |
|          3 | Envy   | Pierce |          3 |         +4 |      2 |           −1 |    1 |

*Od ulepszenia 1:* [Clash Lose] Gain 2 [Defense Level Up]  
Moneta 2: [Heads Hit] Gain 2 [Defense Level Up] next turn

*Od ulepszenia 2:* [Clash Lose] Gain 3 [Defense Level Up]  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn

*Od ulepszenia 4:* [On Use] Gain +2 [Aggro] to this Skill Slot next turn  
[Clash Lose] Gain 3 [Defense Level Up]  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn

#### Umiejętność 2 (×2): Client Protection

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | Slash |          3 |         +2 |      3 |           −1 |    1 |
|          3 | Gloom  | Slash |          3 |         +3 |      3 |           −1 |    1 |
|          4 | Gloom  | Slash |          4 |         +3 |      3 |           −1 |    1 |

*Od ulepszenia 1:* [On Use] Apply 2 [Defense Level Up] to the ally that has the lowest current HP percentage (3 times per turn)  
Moneta 1: [Heads Hit] Gain 1 [Defense Level Up] next turn  
Moneta 2: [Heads Hit] Gain 1 [Defense Level Up] next turn  
Moneta 3: [Heads Hit] Gain 1 [Defense Level Up] next turn

*Od ulepszenia 2:* [On Use] Apply 3 [Defense Level Up] to the ally that has the lowest current HP percentage (3 times per turn)  
At 5+ [Defense Level Up], Clash Power +1  
Moneta 1: [On Hit] Gain 1 [Defense Level Up] next turn  
Moneta 2: [On Hit] Gain 1 [Defense Level Up] next turn  
Moneta 3: [On Hit] Gain 1 [Defense Level Up] next turn

*Od ulepszenia 4:* [On Use] Apply 4 [Defense Level Up] to the ally that has the lowest current HP percentage (3 times per turn)  
At 5+ [Defense Level Up], Clash Power +2  
Moneta 1: [On Hit] Gain 1 [Defense Level Up] next turn  
Moneta 2: [On Hit] Gain 1 [Defense Level Up] next turn  
Moneta 3: [On Hit] Gain 1 [Defense Level Up] next turn

#### Umiejętność 3 (×1): Law and Order

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lust   | Slash |          5 |         +5 |      2 |           −1 |    1 |
|          4 | Lust   | Slash |          6 |         +5 |      2 |           −1 |    1 |

*Od ulepszenia 3:* At 5+ [Defense Level Up], Coin Power +1  
[Clash Win] Heal 2 HP  
Moneta 2: Apply 1 [Haste] and 2 [Defense Level Up] to the ally that has the lowest current HP percentage next turn

*Od ulepszenia 4:* At 5+ [Defense Level Up], Coin Power +1  
[Clash Win] Heal 4 HP  
Moneta 2: Apply 1 [Haste] and 2 [Defense Level Up] to the ally that has the lowest current HP percentage next turn  
Moneta 2: If the ally is a Zwei Association Fixer, apply an additional 1 [Haste], 1 [Defense Level Up]

#### Obrona: Guard

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +6 |      1 |           +2 |    1 |
|          4 | Gloom   | obrona: blok |         12 |         +6 |      1 |           +2 |    1 |

*Od ulepszenia 4:* [On Use] Gain +3 [Aggro] to this Skill Slot next turn

#### Pasywka bojowa: Territory Protection

*od ulepszenia 2; posiadane 4× Gloom*

Combat Start: Apply 2 [Defense Level Up] to the 2 allies adjacent to this unit on the Dashboard

#### Pasywka bojowa: Territory Protection

*od ulepszenia 4; posiadane 4× Gloom*

Combat Start: Apply 2 [Defense Level Up] to the 2 allies adjacent to this unit on the Dashboard  
If the allies have less than 50% HP, apply an additional 2 [Defense Level Up]

#### Pasywka wsparcia: Protection Request Received

*od ulepszenia 3; rezonans 2× Gloom*

Combat Start: Apply 2 [Defense Level Up] to the ally that has the lowest HP percentage  
If the ally has less than 50% HP, apply an additional 2 [Defense Level Up]

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

### 000 Seven Assoc. South Section 4 — Faust

> Faust’s 6th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 0                                                          |
| HP                        | 76 (+2,4 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–7 / 4–7 / 4–7                                      |
| Poziom obrony             | poziom −2                                                  |
| Odporności                | Slash ×1 (Normal), Pierce ×0,5 (Endured), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                            |
| Grzech wyróżniony         | Glut.                                                      |
| Przynależność             | Seven                                                      |
| Słowa kluczowe            | Rupture                                                    |
| Data aktualizacji         | 20230907                                                   |

#### Umiejętność 1 (×3): Predictive Analysis

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Slash |          3 |         +3 |      2 |           +3 |    1 |
|          3 | Envy   | Slash |          4 |         +3 |      2 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 2: [On Hit] Inflict 3 [Rupture]

*Od ulepszenia 2:* If target has 3+ Rupture, Coin Power +1  
Moneta 2: [On Hit] Inflict 3 [Rupture]

*Od ulepszenia 4:* Coin Power +1 for every 3 [Rupture] on target (max 2)  
Moneta 2: [On Hit] Inflict 3 [Rupture]

#### Umiejętność 2 (×2): Dissect Target

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | Slash |          3 |         +4 |      3 |           +3 |    1 |
|          3 | Gloom  | Slash |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* Moneta 1: [Heads Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] If target has 6+ Rupture, inflict [Weakness Analyzed] next turn

*Od ulepszenia 2:* If target has 6+ Rupture, Coin Power +1  
[Clash Win] Inflict +3 [Rupture] Count  
Moneta 1: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] If target has 6+ Rupture, inflict [Weakness Analyzed] next turn

*Od ulepszenia 4:* Coin Power +1 for every 6 [Rupture] on target (max 2)  
[Clash Win] Inflict +3 [Rupture] Count  
Moneta 1: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] If target has 6+ Rupture, inflict [Weakness Analyzed] next turn

#### Umiejętność 3 (×1): Profiling

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Glut.  | Slash |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* Deal +10% damage for every 3 [Rupture] on target (max 20%)  
Moneta 2: [On Hit] Inflict 3 Rupture  
Moneta 3: [Attack End] If target is Staggered or defeated, gain 1 [Haste], 1 [Slash Power Up] next turn

*Od ulepszenia 4:* Deal +10% damage for every 3 [Rupture] on target (max 50%)  
[Clash Win] Inflict +2 [Rupture] Count  
Moneta 2: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [Attack End] If target is Staggered or defeated, gain 1 [Haste], 1 [Slash Power Up] next turn

#### Obrona: Let's Wrap It Up

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +4 |      1 |           −2 |    1 |
|          4 | Lust    | obrona: blok |         10 |         +4 |      1 |           −2 |    1 |

*Od ulepszenia 1:* [On Use] Gain 1 [Haste] next turn (3 times per turn)

*Od ulepszenia 4:* [On Use] Gain 1 [Haste] next turn (3 times per turn)

#### Pasywka bojowa: Before the Tea Cools...

*od ulepszenia 2; posiadane 3× Glut.*

When attacking a target using a damage type the target is "Weak" or "Fatal" (Resistance>x1) to, gain [Poise] equal to [Rupture] on target before the attack (max 20 per turn)

#### Pasywka wsparcia: Seven Association Tea Time

*od ulepszenia 3; posiadane 4× Glut.*

1 ally with the fastest Speed deals +1.5% damage for every Rupture on target when attacking using a damage type that the target is "Fatal" (Resistance>x1.5) to (max 15%)

#### Pasywka wsparcia: Seven Association Tea Time

*od ulepszenia 4; posiadane 4× Glut.*

1 ally with the fastest Speed deals +1.5% damage for every Rupture on target when attacking using a damage type that the target is "Weak" or "Fatal" (Resistance>x1) to (max 15%)  
  
If the ally is a Seven Association Fixer, deal additional damage (+0.5% for every [Rupture]; max 5%)

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

### 000 Lobotomy E.G.O::Regret — Faust

> Faust’s 7th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | wydarzenie 9101                                            |
| HP                        | 82 (+2,82 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 2–5 / 2–5 / 3–6 / 3–6                                      |
| Poziom obrony             | poziom +1                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×2 (Fatal), Blunt ×1 (Normal) |
| Progi Stagger (HP)        | 65% / 35%                                                  |
| Grzech wyróżniony         | Wrath                                                      |
| Przynależność             | L_Corp                                                     |
| Słowa kluczowe            | Tremor                                                     |
| Data aktualizacji         | 20231026                                                   |

#### Umiejętność 1 (×3): Contracting Straight-jacket

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Blunt |          4 |         +6 |      1 |           +3 |    1 |
|          3 | Sloth  | Blunt |          4 |         +7 |      1 |           +3 |    1 |

*Od ulepszenia 1:* [On Use] Gain +3 [Tremor] Count  
Moneta 1: [On Hit] Gain +3 [Tremor] Count  
Moneta 1: [On Hit] Inflict +2 [Tremor] Count

*Od ulepszenia 2:* [On Use] Gain +3 [Tremor] Count  
Moneta 1: [On Hit] Gain +3 [Tremor] Count  
Moneta 1: [On Hit] Inflict +3 [Tremor] Count

*Od ulepszenia 4:* [On Use] Gain +3 [Tremor] Count  
[Clash Lose] Gain +3 [Tremor] Count  
Moneta 1: [On Hit] Gain +3 [Tremor] Count  
Moneta 1: [On Hit] Inflict +3 [Tremor] Count

#### Umiejętność 2 (×2): Metallic Ringing

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Blunt |          3 |         +4 |      3 |           +3 |    1 |
|          3 | Pride  | Blunt |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* [On Use] Gain +4 [Tremor] Count  
Moneta 1: [Heads Hit] Inflict 1 [Offense Level Down] next turn  
Moneta 3: [On Hit] Inflict 4 [Tremor]

*Od ulepszenia 2:* [Combat Start] Consume 5 [Tremor] Count on self and gain +1 Atk Weight for this Skill  
[On Use] Gain +4 [Tremor] Count  
Moneta 1: [Heads Hit] Gain +1 [Tremor] Count  
Moneta 1: [Heads Hit] Inflict 1 [Offense Level Down] next turn  
Moneta 3: [On Hit] Inflict 5 [Tremor]  
Moneta 3: [Heads Hit] Inflict 1 [Plus Coin Drop] next turn

*Od ulepszenia 4:* [Combat Start] Consume 5 [Tremor] Count on self and gain +1 Atk Weight for this Skill  
[On Use] Gain +4 [Tremor] Count  
Moneta 1: [Heads Hit] Gain +1 [Tremor] Count  
Moneta 1: [On Hit] Inflict 1 [Offense Level Down] next turn  
Moneta 3: [On Hit] Inflict 5 [Tremor]  
Moneta 3: [On Hit] Inflict 1 [Plus Coin Drop] next turn

#### Umiejętność 3 (×1): Unleashed Violence

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Blunt |          3 |         +5 |      3 |           +3 |    1 |

*Od ulepszenia 3:* [Combat Start] Consume 5 [Tremor] Count on self and gain +1 Atk Weight for this Skill (max +2)  
[Clash Lose] Lose 20 SP  
Deal +3% damage for every type of negative effect on target (max 15%)  
[On Kill] Gain +2 [Tremor] Count  
Moneta 1: [On Hit] Trigger [Tremor Burst],  
then deal Wrath damage equal to 20% of the final Stagger Threshold raised by [Tremor Burst] (max 13)  
Moneta 2: [On Hit] Trigger [Tremor Burst],  
then deal Wrath damage equal to 20% of the final Stagger Threshold raised by [Tremor Burst] (max 13)  
Moneta 3: [On Hit] Trigger [Tremor Burst],  
then deal Wrath damage equal to 20% of the final Stagger Threshold raised by [Tremor Burst] (max 13)  
Reduce [Tremor] Count by 3

*Od ulepszenia 4:* [Combat Start] Consume 5 [Tremor] Count on self and gain +1 Atk Weight for this Skill (max +2)  
[Clash Lose] Lose 20 SP  
Deal +6% damage for every type of negative effect on target (max 30%)  
[On Kill] Gain +2 [Tremor] Count  
Moneta 1: [On Hit] Trigger [Tremor Burst],  
then deal Wrath damage equal to 30% of the final Stagger Threshold raised by [Tremor Burst] (max 20)  
Moneta 2: [On Hit] Trigger [Tremor Burst],  
then deal Wrath damage equal to 30% of the final Stagger Threshold raised by [Tremor Burst] (max 20)  
Moneta 3: [On Hit] Trigger [Tremor Burst],  
then deal Wrath damage equal to 30% of the final Stagger Threshold raised by [Tremor Burst] (max 20)  
Reduce [Tremor] Count by 3

#### Obrona: Gathering Spite

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | obrona: kontra |          9 |         +6 |      1 |           +5 |    1 |

*Od ulepszenia 1:* [On Use] Gain +3 [Tremor] Count

*Od ulepszenia 4:* [On Use] Gain +6 [Tremor] Count

#### Pasywka bojowa: Coerced Regret

*od ulepszenia 2; posiadane 6× Wrath*

- In a Clash, if target has 3+ types of negative effect, target's Clash Power -1  
- When this unit is alive, enemies affected by [Tremor Burst] gain 2 [Defense Level Down] (once per enemy per turn)  
- Mental Corruption: If at less than -25 SP at Turn End, gain 2 [Bind] and 1 [Blunt Power Up] next turn

#### Pasywka bojowa: Coerced Regret

*od ulepszenia 4; posiadane 6× Wrath*

- In a Clash, target's Clash Power -1 for every 3 types of negative effect it has (max -2 Clash Power)  
- When this unit is alive, enemies affected by [Tremor Burst] gain 2 [Defense Level Down] (3 times per enemy per turn)  
- Mental Corruption: If at less than -25 SP at Turn End, gain 2 [Bind] and 1 [Blunt Power Up] next turn

#### Pasywka wsparcia: Repression Work

*od ulepszenia 3; posiadane 5× Wrath*

In a Clash, if the target of the ally with the slowest Speed has 3+ types of negative effect, target's Clash Power -1

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

### 000 Blade Lineage Salsu — Faust

> Faust’s 8th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 3                                                          |
| HP                        | 76 (+2,5 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–7 / 3–8 / 3–8                                      |
| Poziom obrony             | poziom −2                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×1 (Normal), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 65% / 35% / 15%                                            |
| Grzech wyróżniony         | Pride                                                      |
| Przynależność             | Blade_Lineage                                              |
| Słowa kluczowe            | Poise, Bleed                                               |
| Data aktualizacji         | 20240222                                                   |

#### Umiejętność 1 (×3): Moonlit Blade Dance

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Slash |          3 |         +1 |      3 |           +2 |    1 |
|          3 | Sloth  | Slash |          3 |         +2 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [On Use] Gain +2 [Poise] Count  
Moneta 3: [On Crit] Inflict 1 [Red Plum Blossom]

*Od ulepszenia 2:* [On Use] Gain +2 [Poise] Count  
Moneta 2: [Heads Hit] Gain 1 [Poise]  
Moneta 3: [On Crit] Inflict 1 [Red Plum Blossom]

*Od ulepszenia 4:* At 5+ [Poise], Coin Power +1  
[On Use] Gain +2 [Poise] Count  
Moneta 2: [Heads Hit] Gain 1 [Poise]  
Moneta 3: [On Crit] Inflict 1 [Red Plum Blossom]

#### Umiejętność 2 (×2): Acupuncture

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Pierce |          4 |         +5 |      2 |           +2 |    1 |
|          3 | Pride  | Pierce |          4 |         +6 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain +1 [Poise] Count  
Moneta 2: [On Crit] Inflict 2 [Red Plum Blossom]

*Od ulepszenia 2:* [On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain +2 [Poise] Count  
Moneta 1: Deal +30% damage on Critical Hit  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn  
Moneta 2: [On Crit] Inflict 2 [Red Plum Blossom]

*Od ulepszenia 4:* At 7+ [Poise], Coin Power +1  
[On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain +2 [Poise] Count  
Moneta 1: Deal +30% damage on Critical Hit  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn  
Moneta 2: [On Crit] Inflict 2 [Red Plum Blossom]

#### Umiejętność 3 (×1): Red Plum Blossoms Scatter

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gloom  | Slash |          5 |         +6 |      2 |           +2 |    1 |

*Od ulepszenia 3:* Deal +3% damage for every [Red Plum Blossom] on target  
[Clash Win] Consume half the [Poise] Count on self, then gain [Poise] equal to the [Poise] Count consumed (max 10)  
Moneta 1: [On Crit] Inflict 5 [Red Plum Blossom]  
Moneta 2: [On Crit] Inflict 5 [Red Plum Blossom]

*Od ulepszenia 4:* Deal +3% damage for every [Red Plum Blossom] on target  
Coin Power +1 for every 7 [Poise] on self (max 3)  
[Clash Win] Consume half the [Poise] Count on self, then gain [Poise] equal to the [Poise] Count consumed (max 10)  
This Skill does not consume [Red Plum Blossom] On Crit  
Moneta 1: [On Crit] Inflict 5 [Red Plum Blossom]  
Moneta 1: [On Crit] If target has 10 [Red Plum Blossom], inflict 1 [Slash Fragility]  
Moneta 2: [On Crit] Inflict 5 [Red Plum Blossom]  
Moneta 2: [On Crit] If target has 10 [Red Plum Blossom], inflict 1 [Slash Fragility]

#### Obrona: Redirect

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +4 |      1 |           +0 |    1 |
|          4 | Gloom   | obrona: blok |         10 |         +4 |      1 |           +0 |    1 |

*Od ulepszenia 1:* [On Use] For every 4 [Poise] on self, gain Final Power +1 (max 3)

*Od ulepszenia 4:* [On Use] For every 4 [Poise] on self, gain Final Power +1 (max 5)

#### Pasywka bojowa: Sanguine Plum Blossoms

*od ulepszenia 2; posiadane 4× Pride*

On Crit, inflict 1 [Red Plum Blossom] (max 3 times)

#### Pasywka bojowa: Sanguine Plum Blossoms

*od ulepszenia 4; posiadane 4× Pride*

On Crit, inflict 1 [Red Plum Blossom]  
If target has 10 [Red Plum Blossom], inflict 1 [Defense Level Down] instead (max 6 times)

#### Pasywka wsparcia: Lingering Bladepoint

*od ulepszenia 3; posiadane 4× Pride*

When the ally with the earliest Deployment order hits Critically using a Slash Skill, inflict 1 [Defense Level Down] (max 3 times per enemy per turn)

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

### 00 Wuthering Heights Butler — Faust

> Faust's 9th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 00                                                         |
| Sezon                     | 4                                                          |
| HP                        | 76 (+2,7 za poziom)                                        |
| Szybkość (ulepszenia 1–4) | 2–6 / 3–6 / 3–7 / 3–7                                      |
| Poziom obrony             | poziom −1                                                  |
| Odporności                | Slash ×1 (Normal), Pierce ×2 (Fatal), Blunt ×0,5 (Endured) |
| Progi Stagger (HP)        | 65% / 35% / 15%                                            |
| Grzech wyróżniony         | Pride                                                      |
| Przynależność             | Wuthering_Heights                                          |
| Słowa kluczowe            | Sinking                                                    |
| Data aktualizacji         | 20240404                                                   |

#### Umiejętność 1 (×3): Confiscation

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | Slash |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Gloom  | Slash |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* Moneta 2: [Heads Hit] Inflict 2 [Sinking]

*Od ulepszenia 2:* Moneta 2: [On Hit] Inflict 2 [Sinking]

*Od ulepszenia 4:* [On Use] If target has 6+ [Sinking], Coin Power +1  
Moneta 2: [On Hit] Inflict 2 [Sinking]

#### Umiejętność 2 (×2): Interloper Reception

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lust   | Blunt |          3 |         +5 |      2 |           +2 |    1 |
|          3 | Lust   | Blunt |          4 |         +5 |      2 |           +2 |    1 |

*Od ulepszenia 1:* Moneta 2: [Heads Hit] Inflict +2 [Sinking] Count

*Od ulepszenia 2:* [On Use] If target has 5+ [Sinking], Clash Power +1  
Moneta 2: [On Hit] Inflict +2 [Sinking] Count

*Od ulepszenia 4:* [On Use] If target has 5+ [Sinking], Clash Power +1  
[On Use] If target has 3+ [Sinking] Count, Coin Power +1  
Moneta 2: [On Hit] Inflict +3 [Sinking] Count

#### Umiejętność 3 (×1): Reception Arts 4: Heartseal

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Slash |          4 |         +2 |      4 |           +4 |    1 |

*Od ulepszenia 3:* Moneta 1: [On Hit] Inflict +3 [Sinking] Count  
Moneta 4: [On Hit] Inflict 2 [Echoes of the Manor] next turn  
Moneta 4: [On Hit] If target has [Echoes of the Manor], inflict +3 [Sinking] Count

*Od ulepszenia 4:* [On Use] If target has 5+ [Sinking] Count, Coin Power +2  
Moneta 1: [On Hit] Inflict +3 [Sinking] Count  
Moneta 4: [On Hit] Inflict 2 [Echoes of the Manor] next turn  
Moneta 4: [On Hit] If target has [Echoes of the Manor], inflict +3 [Sinking] Count

#### Obrona: Hunting Plans

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |          7 |         +6 |      1 |           +1 |    1 |
|          4 | Gloom   | obrona: blok |          7 |         +6 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [On Use] If target has 10+ [Sinking], Coin Power +3

*Od ulepszenia 4:* [On Use] If target has 10+ [Sinking], Coin Power +7

#### Pasywka bojowa: Butler Style Response

*od ulepszenia 2; posiadane 4× Gloom*

- Clash Win: Inflict 1 [Sinking] on target (3 times per turn)

#### Pasywka bojowa: Butler Style Response

*od ulepszenia 4; posiadane 4× Gloom*

- Clash Win: Inflict 1 [Sinking] on target (3 times per turn)  
- If the target has [Echoes of the Manor], inflict 3 [Sinking] instead

#### Pasywka wsparcia: Anticipatory Training

*od ulepszenia 3; posiadane 4× Gloom*

When 1 ally that has the lowest SP hits an enemy that has 5+ [Sinking], the ally heals 2 SP On Hit (4 times per turn)

#### Pasywka wsparcia: Anticipatory Training

*od ulepszenia 4; posiadane 4× Gloom*

When 1 ally that has the lowest SP hits an enemy that has 5+ [Sinking], the ally heals 3 SP On Hit (4 times per turn)

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

### 000 MultiCrack Office Rep — Faust

> Faust's 10th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 4                                                          |
| HP                        | 66 (+2,28 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                      |
| Poziom obrony             | poziom −1                                                  |
| Odporności                | Slash ×1 (Normal), Pierce ×2 (Fatal), Blunt ×0,5 (Endured) |
| Progi Stagger (HP)        | 70% / 40% / 20%                                            |
| Grzech wyróżniony         | Gloom                                                      |
| Przynależność             | Multi_Crack                                                |
| Słowa kluczowe            | Charge                                                     |
| Data aktualizacji         | 20240808                                                   |

#### Umiejętność 1 (×3): 40Y-3 Activation

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lust   | Slash |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Lust   | Slash |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [On Use] Consume 5 [Charge] Count to gain Coin Power +1  
Moneta 2: [On Hit] Gain +2 [Charge] Count

*Od ulepszenia 2:* [On Use] Consume 5 [Charge] Count to gain Coin Power +1  
Moneta 2: [On Hit] Gain +3 [Charge] Count

*Od ulepszenia 4:* [On Use] Consume 5 [Charge] Count to gain Coin Power +2  
Moneta 2: [On Hit] Gain +3 [Charge] Count

#### Umiejętność 2 (×2): Charge Countercurrent

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Blunt |          4 |         +3 |      3 |           +4 |    1 |
|          3 | Envy   | Blunt |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 1:* [On Use] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10  
[On Use] Consume 10 [Charge] Count to gain Coin Power +1  
Moneta 3: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +([Charge])% damage for every [Charge] Count consumed by this Skill (max 60%)

*Od ulepszenia 2:* [On Use] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10  
[On Use] Consume 10 [Charge] Count to gain Coin Power +1  
Moneta 3: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +([Charge] + 3)% damage for every [Charge] Count consumed by this Skill (max 120%)

*Od ulepszenia 4:* [On Use] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10  
[On Use] Consume 10 [Charge] Count to gain Coin Power +2  
Moneta 3: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +([Charge] + 4)% damage for every [Charge] Count consumed by this Skill (max 180%)

#### Umiejętność 3 (×1): 40Y-3 Charge

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gloom  | Blunt |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* At 2+ [Charge], Coin Power +2  
Moneta 1: [On Hit] Gain +([Charge] + 4) [Charge] Count (max 7)  
Moneta 2: [On Hit] Gain +([Charge] + 4) [Charge] Count (max 7)  
Moneta 4: At 3+ [Charge], deal +4% damage for every [Charge] (max 20%)

*Od ulepszenia 4:* Coin Power +1 for every [Charge] (max 4)  
Moneta 1: [On Hit] Gain +([Charge] + 5) [Charge] Count (max 8)  
Moneta 2: [On Hit] Gain +([Charge] + 5) [Charge] Count (max 8)  
Moneta 4: At 3+ [Charge], deal +8% damage for every [Charge] (max 40%)  
Moneta 4: [On Hit] Inflict 1 [Envy Fragility] next turn  
- At 2+ [Charge], inflict 1 additional [Envy Fragility]

#### Obrona: Charge

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         10 |         +4 |      1 |           +0 |    1 |
|          4 | Envy    | obrona: blok |         12 |         +6 |      1 |           +0 |    1 |

*Od ulepszenia 1:* [On Use] Gain +2 [Charge] Count (2 times per turn)

*Od ulepszenia 4:* [On Use] Gain +4 [Charge] Count (2 times per turn)

#### Pasywka bojowa: Electrocurrent Dismantling

*od ulepszenia 2; posiadane 3× Envy*

Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter  
At 2+ [Charge], deal +([Charge] x 3)% damage (max 15%)  
  
On Kill, this unit and 1 ally that has the lowest [Charge] Count gain [Charge] Count equal to [Charge] (max 3, prioritizes allies that consume or gain [Charge])

#### Pasywka bojowa: Electrocurrent Dismantling

*od ulepszenia 4; posiadane 3× Envy*

Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter  
At 2+ [Charge], deal +([Charge] x 3)% damage (max 15%)  
- If the target is at less than 50% HP, deal +([Charge] x 5)% more damage (max 25%)  
  
On Kill, this unit and 2 allies that have the lowest [Charge] Count gain [Charge] Count equal to ([Charge] + 2) (max 5, prioritizes allies that consume or gain [Charge])

#### Pasywka wsparcia: Auxiliary Dismantling Current

*od ulepszenia 3; posiadane 5× Envy*

When 1 ally that has the lowest [Charge] Count kills an enemy, the ally gains +2 [Charge] Count (once per turn, prioritizes allies that consume or gain [Charge])

#### Pasywka wsparcia: Auxiliary Dismantling Current

*od ulepszenia 4; posiadane 5× Envy*

When 1 ally that has the lowest [Charge] Count kills an enemy, the ally gains +3 [Charge] Count (once per turn, prioritizes allies that consume or gain [Charge])

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

### 000 LCE E.G.O:: Ardor Blossom Star — Faust

> Faust's 11th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 5                                                          |
| HP                        | 66 (+2,28 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                      |
| Poziom obrony             | poziom −1                                                  |
| Odporności                | Slash ×1 (Normal), Pierce ×2 (Fatal), Blunt ×0,5 (Endured) |
| Progi Stagger (HP)        | 50% / 20%                                                  |
| Grzech wyróżniony         | Wrath                                                      |
| Przynależność             | Limbus_Company, Limbus_Company_Lce                         |
| Słowa kluczowe            | Burn                                                       |
| Data aktualizacji         | 20250123                                                   |

#### Umiejętność 1 (×3): Ignition

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Blunt |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Sloth  | Blunt |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [On Use] At 10+ [Burn], deal +10% damage  
[On Use] Gain 7 [Burn] and +1 [Burn] Count  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 1: [On Hit] Gain 2 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] Gain 2 [Burn]

*Od ulepszenia 2:* [On Use] At 10+ [Burn], deal +10% damage  
[On Use] Gain 7 [Burn] and +1 [Burn] Count  
[On Use] At 10+ ([Burn] on self + [Burn] on target), Coin Power +1  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 1: [On Hit] Gain 2 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] At 10+ [Burn], inflict additional 1 [Burn]  
Moneta 2: [On Hit] Gain 2 [Burn]

*Od ulepszenia 4:* [On Use] At 10+ [Burn], deal +10% damage  
[On Use] Gain 7 [Burn] and +1 [Burn] Count  
[On Use] Coin Power +1 for every 10 ([Burn] on self + [Burn] on target) (max 2)  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 1: [On Hit] Gain 2 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] At 10+ [Burn], inflict additional 3 [Burn]  
Moneta 2: [On Hit] Gain 2 [Burn]

#### Umiejętność 2 (×2): E.G.O - A.B.S Activation

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Blunt |          2 |         +4 |      3 |           +3 |    1 |
|          3 | Pride  | Blunt |          3 |         +4 |      3 |           +3 |    1 |
|          4 | Pride  | Blunt |          4 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 1:* At 10+ [Burn], deal +10% damage  
[On Use] Gain +4 [Burn] Count  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Burn]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: [On Hit without Cracking] Inflict 2 [Burn]

*Od ulepszenia 2:* Deal +10% damage for every 10 [Burn] on self (max 20%)  
[On Use] Gain +4 [Burn] Count  
[On Use] At 4+ ([Burn] on self + [Burn] on target), Coin Power +1  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Burn]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: [On Hit without Cracking] Inflict 3 [Burn]

*Od ulepszenia 4:* Deal +10% damage for every 10 [Burn] on self (max 20%)  
[On Use] Gain +4 [Burn] Count  
[On Use] Coin Power +1 for every 4 ([Burn] on self + [Burn] on target) (max 2)  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Burn]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: [On Hit without Cracking] Inflict 3 [Burn]  
Moneta 3: [On Hit] If target has 15+ [Burn], inflict +2 [Burn] Count on target

#### Umiejętność 3 (×1): Drawn by Flame

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Blunt |          4 |         +4 |      3 |           +5 |    1 |
|          4 | Wrath  | Blunt |          5 |         +4 |      3 |           +5 |    1 |

*Od ulepszenia 3:* [Combat Start] Gain 7 [Burn] and +1 [Burn] Count  
[Before Use] At 30+ [Burn], activate "A.B.S Max Attunement 【Degraded Corrosion】" instead  
Deal +7.5% damage for every 5 [Burn] on self (max 30%)  
[On Use] At 10+ ([Burn] on self + [Burn] on target), Base Power +1  
[On Use] If this unit is missing 30%+ HP, Coin Power +1  
Moneta 1: [On Hit] Inflict 3 [Burn]  
Moneta 2: [On Hit] Inflict 3 [Burn]

*Od ulepszenia 4:* [Combat Start] Gain 7 [Burn] and +1 [Burn] Count  
[Before Use] At 30+ [Burn], activate "A.B.S Max Attunement 【Degraded Corrosion】" instead  
Deal +12.5% damage for every 5 [Burn] on self (max 50%)  
[On Use] Base Power +1 for every 10 ([Burn] on self + [Burn] on target) (max 2)  
[On Use] For every 30% missing HP on this unit, Coin Power +1 (max 2)  
Moneta 1: [On Hit] Inflict 3 [Burn]  
Moneta 2: [On Hit] Inflict 3 [Burn]

#### Umiejętność 4 (×0): A.B.S Max Attunement 【Degraded Corrosion】

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Blunt |          4 |         +4 |      3 |           +5 |    1 |
|          4 | Wrath  | Blunt |          5 |         +4 |      3 |           +5 |    1 |

*Od ulepszenia 1:* This unit dies after using this Skill  
- If HP drops to 1 while using this Skill, maintains HP at 1 for the duration of the Skill  
[On Use] Deal +7.5% damage for every 5 [Burn] on self (max 30%)  
[On Use] At 10+ ([Burn] on self + [Burn] on target), Base Power +1  
[On Use] Coin Power +1 for every 30% missing HP on self (max 2)  
[Before Attack] Atk Weight +1 for every 20% missing HP on self (max 2)  
Moneta 1: [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict 3 [Burn]  
Moneta 2: [Unbreakable Coin]  
Moneta 2: [On Hit] Inflict 3 [Burn]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: [On Hit] Deal +10% damage for every 20% missing HP on self (max 30%)

*Od ulepszenia 4:* This unit dies after using this Skill  
- If HP drops to 1 while using this Skill, maintains HP at 1 for the duration of the Skill  
[On Use] Deal +12.5% damage for every 5 [Burn] on self (max 50%)  
[On Use] Base Power +1 for every 10 ([Burn] on self + [Burn] on target) (max 2)  
[On Use] Coin Power +1 for every 30% missing HP on self (max 3)  
[Before Attack] Atk Weight +1 for every 20% missing HP on self (max 4)  
Moneta 1: [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict 4 [Burn]  
Moneta 2: [Unbreakable Coin]  
Moneta 2: [On Hit] Inflict 4 [Burn]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: [On Hit] Deal +10% damage for every 20% missing HP on self (max 30%)

#### Obrona: Resonating by Raising A.B.S Attunement.

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           −2 |    1 |
|          4 | Wrath   | obrona: unik |          4 |        +10 |      1 |           −2 |    1 |

*Od ulepszenia 1:* [On Use] Lose 5 [Burn] (once per turn)  
[On Evade] Lose 5 [Burn] (once per turn)

*Od ulepszenia 4:* [On Use] At 10+ [Burn], Coin Power +3  
[On Use] Lose 5 [Burn] (once per turn)  
[On Evade] Lose 5 [Burn] (once per turn)

#### Pasywka bojowa: Fireproof

*od ulepszenia 1*

Cannot be Staggered or fall below 1 HP due to [Burn] damage

#### Pasywka bojowa: Fireproof

*od ulepszenia 2*

Cannot be Staggered or fall below 1 HP due to [Burn] damage

#### Pasywka bojowa: Flame Moth

*od ulepszenia 2; posiadane 3× Wrath*

Combat Start: At 80%+ missing HP, and at less than 30 [Burn], gain up to 30 [Burn] (once per Encounter)  
  
Turn End: Gain 1 [Offense Level Up] next turn for every 6 [Burn] on self (max 5)  
  
On death, activate the following:  
- Inflict 2 [Burn] on all enemies and inflict this unit's [Burn] between all enemies (max 3 per enemy)  
- Gain 2 E.G.O resource for the 2 least-owned Affinities  
  
If this unit died due to the A.B.S. Max Attunement 【Degraded Corrosion】 Skill, enhance the effect:  
- Inflict 3 [Burn] on all enemies and inflict this unit's [Burn] between all enemies (max 5 per enemy)  
- Gain 2 E.G.O resource for 2 least-owned E.G.O resources  
- If this unit had 30+ [Burn], apply 3 [Offense Level Up] to 1 ally that Substitutes in

#### Pasywka wsparcia: Residual Heat

*od ulepszenia 3; rezonans 3× Wrath*

When 1 ally that has the lowest SP inflicts [Burn] with a Base Skill's On Hit effect, inflict 2 additional [Burn] (max 3 times)  
- If the target the ally is attacking has 30+ [Burn], inflict +1 [Burn] Count instead (max 3 times)

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

### 000 Heishou Pack - Mao Branch Adept — Faust

> Faust's 12th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 6                                                          |
| HP                        | 76 (+3,19 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–6 / 3–6 / 4–7 / 4–7                                      |
| Poziom obrony             | poziom +3                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×1 (Normal), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 50%                                                        |
| Grzech wyróżniony         | Glut.                                                      |
| Przynależność             | Black_Beast_Rabbit, H_Corp                                 |
| Słowa kluczowe            | Rupture                                                    |
| Data aktualizacji         | 20250522                                                   |

#### Umiejętność 1 (×3): Blinkstep

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Slash |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Sloth  | Slash |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [On Use] If target has 6+ [Rupture], Coin Power +1  
Moneta 1: [On Hit] Inflict 1 [Rupture]  
Moneta 2: [On Hit] Inflict +1 [Rupture] Count

*Od ulepszenia 2:* [On Use] If target has 4+ [Rupture], Coin Power +1  
[Clash Win] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict 1 [Rupture]  
Moneta 2: [On Hit] Inflict +1 [Rupture] Count  
Moneta 2: [On Hit] At 10+ Speed, Reuse Coin once (once per Skill)

*Od ulepszenia 4:* If this unit's Speed is faster than the target's by 3 or more, Coin Power +1  
[On Use] If target has 4+ [Rupture], Coin Power +1  
[Clash Win] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict 1 [Rupture]  
Moneta 2: [On Hit] Inflict +1 [Rupture] Count  
Moneta 2: [On Hit] At 10+ Speed, Reuse Coin once (once per Skill)

#### Umiejętność 2 (×2): Clearing the Path, My Lord.

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Slash |          3 |         +6 |      2 |           +2 |    1 |
|          3 | Pride  | Slash |          4 |         +6 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [On Use] If target has 4+ [Rupture], Coin Power +1  
[Clash Win] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 2: If target has [Deathrite【Haste】] or [Deathrite 【Fissure】], deal +30% damage

*Od ulepszenia 2:* [On Use] If target has 4+ [Rupture], Coin Power +1  
[On Use] Gain 2 [Haste] next turn (once per turn)  
[Clash Win] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 2: If target has [Deathrite【Haste】] or [Deathrite 【Fissure】], deal +30% damage

*Od ulepszenia 4:* If this unit's Speed is faster than the target's, deal +(Speed difference x [Tianjiu Star's Blade] on self)% damage (max 50%)  
If this unit's Speed is faster than the target's by 3 or more, Coin Power +1  
[On Use] If target has 4+ [Rupture], Coin Power +1  
[On Use] Gain 2 [Haste] next turn (once per turn)  
[Clash Win] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 2: [On Hit] Inflict 1 [Rupture]  
Moneta 2: If target has [Deathrite【Haste】] or [Deathrite 【Fissure】], deal +50% damage

#### Umiejętność 3 (×1): Traceless to Sight and Sound Alike.

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Glut.  | Slash |          5 |         +3 |      3 |           +3 |    1 |
|          4 | Glut.  | Slash |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* If this unit's Speed is faster than the target's, deal +(Speed difference x [Rupture] Potency on target)% damage (max 50%)  
If this unit's Speed is faster than the target's by 2 or more, Coin Power +1  
[Combat Start] Gain 1 [Assist Defense] (once per turn)  
[Before Use] At 10+ [Tianjiu Star's Blade], activate "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead  
[On Use] Gain 3 [Strider【Mao】]  
[Clash Win] Inflict +2 [Rupture] Count  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict [Deathrite【Haste】]  
Moneta 2: [On Hit] Inflict 1 [Rupture]  
Moneta 3: At 10+ Speed, deal +30% damage  
Moneta 3: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] At 10+ Speed, Reuse Coin once (once per Skill)

*Od ulepszenia 4:* If this unit's Speed is faster than the target's, deal +(Speed difference x [Rupture] Potency on target)% damage (max 50%)  
If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)  
[Combat Start] Gain 1 [Assist Defense] (once per turn)  
[Before Use] At 10+ [Tianjiu Star's Blade], activate "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead  
[On Use] If target has 15+ [Rupture], Coin Power +1  
[On Use] Gain 3 [Strider【Mao】]  
[Clash Win] Inflict +2 [Rupture] Count  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict [Deathrite【Haste】]  
Moneta 2: [On Hit] Inflict 1 [Rupture]  
Moneta 3: At 10+ Speed, deal +30% damage  
Moneta 3: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] At 10+ Speed, Reuse Coin once (once per Skill)  
Moneta 3: [Reuse - On Hit] Inflict [Deathrite【Haste】]

#### Umiejętność 4 (×0): Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Glut.  | Slash |          5 |         +3 |      3 |           +4 |    1 |
|          4 | Glut.  | Slash |          5 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 3:* If this unit's Speed is faster than the target's, deal +(Speed difference x [Rupture] Potency on target)% damage (max 50%)  
If this unit's Speed is faster than the target's by 2 or more, Coin Power +1  
[On Use] If target has 15+ [Rupture], Coin Power +1  
[On Use] At 10+ Speed, gain 20 [Poise]; if this unit has less than 4 [Poise] Count, raise [Poise] Count up to 4  
[On Use] Gain 3 [Strider【Mao】]  
[Clash Win] Inflict +2 [Rupture] Count  
[Attack End] Consume 10 [Tianjiu Star's Blade]  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict [Deathrite 【Fissure】]  
Moneta 1: [On Hit] Inflict [Deathrite【Haste】]  
Moneta 2: [On Hit] Inflict 1 [Rupture]  
Moneta 3: At 10+ Speed, deal +30% damage  
Moneta 3: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] At 10+ Speed, Reuse Coin once (once per Skill)  
Moneta 3: [Reuse - On Hit] Inflict [Deathrite 【Fissure】]

*Od ulepszenia 4:* If this unit's Speed is faster than the target's, deal +(Speed difference x [Rupture] Potency on target)% damage (max 50%)  
If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)  
[On Use] Coin Power +1 for every 10 [Rupture] on target (max 2)  
[On Use] At 10+ Speed, gain 20 [Poise]; if this unit has less than 4 [Poise] Count, raise [Poise] Count up to 4  
[On Use] Gain 3 [Strider【Mao】]  
[Clash Win] Inflict +2 [Rupture] Count  
[Attack End] Consume 10 [Tianjiu Star's Blade]  
Moneta 1: [On Hit] Inflict +1 [Rupture] Count  
Moneta 1: [On Hit] Inflict [Deathrite 【Fissure】]  
Moneta 1: [On Hit] Inflict [Deathrite【Haste】]  
Moneta 2: [On Hit] Inflict 1 [Rupture]  
Moneta 3: At 10+ Speed, deal +30% damage  
Moneta 3: [On Hit] Inflict 3 [Rupture]  
Moneta 3: [On Hit] At 10+ Speed, Reuse Coin once (once per Skill)  
Moneta 3: [Reuse - On Hit] Inflict [Deathrite 【Fissure】]  
Moneta 3: [Reuse - On Hit] Inflict [Deathrite【Haste】]

#### Obrona: It Shall Be Done.

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Glut.  | obrona: kontra |          5 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Clashable Counter]  
[Combat Start] Gain 1 [Assist Defense] (once per turn)  
[On Use] This Skill gains +1 Offense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)  
[On Use] Gain 3 [Strider【Mao】]  
Moneta 1: [On Hit] Inflict 1 [Rupture]  
Moneta 2: [On Hit] Inflict 1 [Rupture]

*Od ulepszenia 4:* [Clashable Counter]  
[Combat Start] Gain 1 [Assist Defense] (once per turn)  
[On Use] This Skill gains +1 Offense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)  
[On Use] Gain 3 [Strider【Mao】]  
[On Use] If this unit's Speed is faster than the target's by 2 or more, gain Base Power based on Speed difference (Base Power +1 for every 2 Speed difference; max 2)  
Moneta 1: [On Hit] Inflict 1 [Rupture]  
Moneta 2: [On Hit] Inflict 1 [Rupture]

#### Obrona: Swiftfeet Protection

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Glut.  | obrona: blok |          4 |         +8 |      1 |           +2 |    1 |
|          4 | Glut.  | obrona: blok |          4 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [Clashable Guard]  
Exclusive Skill for [Assist Defense]  
[Before Use] At 10+ [Tianjiu Star's Blade], activates "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead  
[On Use] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)  
[On Use] Cannot be Staggered by damage until this Skill ends  
[On Use] Gain 2 [Protection] (once per turn)  
Moneta 1: [Unbreakable Coin]

*Od ulepszenia 4:* [Clashable Guard]  
Exclusive Skill for [Assist Defense]  
[Before Use] At 10+ [Tianjiu Star's Blade], activates "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead  
[On Use] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)  
[On Use] Cannot be Staggered by damage until this Skill ends  
[On Use] Gain 2 [Protection] (once per turn)  
Moneta 1: [Unbreakable Coin]

#### Obrona: 1021207

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Glut.  | obrona: kontra |          5 |         +3 |      3 |           +4 |    1 |
|          4 | Glut.  | obrona: kontra |          5 |         +4 |      3 |           +4 |    1 |

#### Pasywka bojowa: Tianjiu Star

*od ulepszenia 1*

When [Deathrite 【Fissure】] Stack drops to 0 and expires, gain [Mark of Decay]

#### Pasywka bojowa: 1021202

*od ulepszenia 1*



#### Pasywka bojowa: Tianjiu Star

*od ulepszenia 2*

When [Deathrite 【Fissure】] Stack drops to 0 and expires, gain [Mark of Decay]

#### Pasywka bojowa: Heishou Mutation [Mao] / Mao Branch Adept

*od ulepszenia 2; posiadane 5× Glut.*

If this unit's Speed is faster than the target's, deal +2% more damage for every 1 Speed difference (max 10%)  
  
Gain 1 [Tianjiu Star's Blade] every time an ally triggers a Deathrite effect (5 times per turn)  
- If this unit triggered a Deathrite effect, gain 1 additional [Tianjiu Star's Blade]  
When activating the [Assist Defense] effect, gain 5 [Tianjiu Star's Blade]

#### Pasywka bojowa: 1021202

*od ulepszenia 2*



#### Pasywka wsparcia: Blinkblade

*od ulepszenia 3; rezonans 4× Glut.*

When 1 ally with the fastest Speed inflicts [Rupture] damage, gain 1 [Offense Level Up] next turn (3 times per turn)

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

### 000 Shi Assoc. East Section 3 — Faust

> Faust's 13th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 0                                                          |
| HP                        | 60 (+2,82 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                      |
| Poziom obrony             | poziom −1                                                  |
| Odporności                | Slash ×1 (Normal), Pierce ×0,5 (Endured), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 70% / 50% / 20%                                            |
| Grzech wyróżniony         | Wrath                                                      |
| Przynależność             | Shi                                                        |
| Słowa kluczowe            | Bleed, Poise                                               |
| Data aktualizacji         | 20251009                                                   |

#### Umiejętność 1 (×3): Cleave

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Wrath  | Slash |          3 |         +3 |      2 |           +1 |    1 |
|          3 | Wrath  | Slash |          4 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [On Use] Gain 1 [Poise]  
Moneta 1: [On Hit] Inflict 1 [Bleed]  
Moneta 2: [On Hit] Inflict 1 [Bleed]

*Od ulepszenia 2:* [On Use] At 4+ ([Poise] on self + [Bleed] on target), Coin Power +1  
[On Use] Gain 2 [Poise]  
Moneta 1: [On Hit] Inflict 1 [Bleed]  
Moneta 2: [On Hit] Inflict 1 [Bleed]

*Od ulepszenia 4:* [On Use] At 4+ ([Poise] on self + [Bleed] on target), Coin Power +1  
[On Use] Gain 2 [Poise]  
Moneta 1: [On Hit] Inflict 1 [Bleed]  
Moneta 2: [On Hit] Inflict 2 [Bleed]

#### Umiejętność 2 (×2): Positioning Maneuver

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Slash |          3 |         +3 |      3 |           +2 |    1 |
|          3 | Pride  | Slash |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [On Use] Deal +11% damage for every 4 [Poise] on self (max 44%)  
[On Use] Gain +1 [Poise] Count  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Gain 1 [Poise]  
Moneta 3: [On Crit] Inflict 2 [Bleed]

*Od ulepszenia 2:* [On Use] Clash Power +1 for every 4 ([Poise] on self + [Bleed] on target) (max 2)  
[On Use] Deal +11% damage for every 4 [Poise] on self (max 44%)  
[On Use] Gain +1 [Poise] Count  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Gain 2 [Poise]  
Moneta 3: [On Crit] Inflict 2 [Bleed]

*Od ulepszenia 4:* [On Use] Clash Power +1 for every 4 ([Poise] on self + [Bleed] on target) (max 4)  
[On Use] Deal +11% damage for every 4 [Poise] on self (max 44%)  
[On Use] Deal +11% damage for every [Arrow - Shi] spent (max 44%)  
[On Use] Gain +1 [Poise] Count  
Moneta 1: [On Hit] Inflict +2 [Bleed] Count  
Moneta 2: [On Hit] Gain 2 [Poise]  
Moneta 3: [On Hit] Inflict 2 [Bleed]

#### Umiejętność 3 (×1): Glimmering Bow [弓閃]

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lust   | Slash |          4 |         +2 |      4 |           +3 |    1 |
|          4 | Lust   | Slash |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* [On Use] Coin Power +1 for every 4 ([Poise] on self + [Bleed] on target) (max 2)  
[On Use] Deal +11% damage for every 4 [Poise] on self (max 44%)  
[On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 1: [On Crit] Gain +1 [Poise] Count  
Moneta 2: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Crit] Inflict +1 [Bleed] Count  
Moneta 3: [On Hit] Inflict 4 [Bleed]  
Moneta 4: [On Crit] Inflict 1 [Defense Level Down] next turn (once per turn)

*Od ulepszenia 4:* [On Use] Coin Power +1 for every 4 ([Poise] on self + [Bleed] on target) (max 2)  
[On Use] Deal +11% damage for every 4 [Poise] on self (max 44%)  
[On Use] Deal +11% damage for every [Arrow - Shi] spent (max 44%)  
[On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain 2 [Poise]  
Moneta 1: [On Crit] Gain +1 [Poise] Count  
Moneta 2: [On Hit] Inflict +2 [Bleed] Count  
Moneta 2: [On Crit] Inflict +1 [Bleed] Count  
Moneta 3: [On Hit] Inflict 4 [Bleed]  
Moneta 4: [On Crit] Inflict 2 [Defense Level Down] next turn (once per turn)

#### Umiejętność 4 (×0): Bow's Glimmer [閃弓]

| Ulepszenie | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lust   | Pierce |          4 |         +4 |      1 |           +5 |    1 |

*Od ulepszenia 3:* [Unclashable]  
External effects cannot trigger this Skill to be Reused  
Deal +24% damage for every [Target Aim] (max 72%)  
Deal +24% damage on Critical Hit for every [Target Aim] (max 72%)  
- At 4 [Target Aim], instead of the two above effects, deal +444% damage on Critical Hit  
[On Use] At 4+ [Poise], Base Power +2  
[On Use] Coin Power +2 for every [Target Aim] (max 4)  
[On Use] Gain 5 [Poise] for every [Target Aim]  
[Attack End] Lose ([Target Aim] x 5) [Poise]  
[Attack End] Remove [Ready to Loose] and [Target Aim] from self  
Moneta 1: [On Hit] Inflict 1 [Lodged Arrow]; once inflicted, lose 1 [Arrow - Shi]  
Moneta 1: [On Kill] Gain 1 [Liferender] next turn

*Od ulepszenia 4:* [Unclashable]  
External effects cannot trigger this Skill to be Reused  
Deal +48% damage for every [Target Aim] (max 144%)  
Deal +48% damage on Critical Hit for every [Target Aim] (max 144%)  
- At 4 [Target Aim], instead of the two above effects, deal +444% damage on Critical Hit  
[On Use] Base Power +2 for every 4 [Poise] on self (max 10)  
[On Use] Coin Power +4 for every [Target Aim] (max 10)  
[On Use] Gain 5 [Poise] for every [Target Aim]  
[Attack End] Lose (([Target Aim] - 1) x 5) [Poise]  
[Attack End] Remove [Ready to Loose] and [Target Aim] from self  
Moneta 1: [On Hit] Inflict 1 [Lodged Arrow]; once inflicted, lose 1 [Arrow - Shi]  
Moneta 1: [On Kill] Gain 1 [Liferender] next turn  
Moneta 1: [On Crit Kill Against Enemy] Gain +4 [Poise] Count

#### Obrona: Unfold Bowblade [弓刀]

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |         14 |         +4 |      1 |           +1 |    1 |
|          3 | Lust    | obrona: blok |         14 |         +4 |      1 |           +1 |    1 |

*Od ulepszenia 3:* If this unit does not have [Arrow - Shi], activate "Evade" instead  
  
[Combat Start] If this unit is about to use "Bow's Glimmer", use "Evade" instead  
[Combat Start] If this unit has [Ready to Loose], gain (36 / [Target Aim] Stack) Shield for the turn (once per turn)  
  
[Turn End] If this unit has [Ready to Loose], and did not use an Attack Skill this turn, gain 1 [Target Aim] next turn (once per turn)  
[Turn End] If this unit does not have [Ready to Loose], and has 1+ [Arrow - Shi], gain 1 of each [Ready to Loose] and [Target Aim] next turn (once per turn)

*Od ulepszenia 4:* If this unit does not have [Arrow - Shi], activate "Evade" instead  
  
[Combat Start] If this unit is about to use "Bow's Glimmer", use "Evade" instead  
[Combat Start] If this unit has [Ready to Loose], gain (60 / [Target Aim] Stack) Shield for the turn (once per turn)  
  
[Turn End] If this unit has [Ready to Loose], and did not use an Attack Skill this turn, gain 1 [Target Aim] next turn (once per turn)  
[Turn End] If this unit does not have [Ready to Loose], and has 1+ [Arrow - Shi], gain 1 of each [Ready to Loose] and [Target Aim] next turn (once per turn)

#### Obrona: Evade

| Ulepszenie | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lust   | obrona: unik |          4 |        +10 |      1 |           +1 |    1 |

*Od ulepszenia 1:* [On Evade] Gain +1 [Poise] Count (2 times per turn)

*Od ulepszenia 4:* [On Evade] Gain +1 [Poise] Count (3 times per turn)

#### Pasywka bojowa: Shi-no-Yumi

*od ulepszenia 2; posiadane 3× Lust*

At 4 [Arrow - Shi] Stack: When this unit gains [Poise] Potency from Base Attack Skill effects, gain +1 [Poise] Count (2 times per Encounter; per-Encounter cap resets when [Arrow - Shi] drops to 3)  
If this unit used "Bow's Glimmer" Skill at 2+ [Target Aim], gain 1 [Slash DMG Up] next turn

#### Pasywka bojowa: Snipe - Archery

*od ulepszenia 3*

If this unit is in [Ready to Loose] state, replace the leftmost Base Attack Skill equipped on the Dashboard with "Bow's Glimmer", then use it at Combat Start  
- If, at max [Target Aim] Stack, this unit's Skill 3 is on neither the Dashboard nor the upcoming list of Skills when this effect activates, the Defense Skill equipped on the leftmost Skill Slot counts as a Skill 3, and will be used to activate "Bow's Glimmer"  
  
Gain the following effects based on which Base Attack Skill was replaced (Sin Affinity carries over from the replaced Skill)  
- Skill 1: Base Power +1, deal +11% damage  
- Skill 2: Base Power +1, Coin Power +1, deal +22% damage  
- Skill 3: Base Power +4, Coin Power +4, deal +44% damage  
  
※ If an E.G.O Skill was equipped at Combat Start, remove [Ready to Loose] and this unit does not use "Bow's Glimmer"

#### Pasywka bojowa: Shi-no-Yumi

*od ulepszenia 3; posiadane 3× Lust*

At 4 [Arrow - Shi] Stack: When this unit gains [Poise] Potency from Base Attack Skill effects, gain +1 [Poise] Count (2 times per Encounter; per-Encounter cap resets when [Arrow - Shi] drops to 3)  
If this unit used "Bow's Glimmer" Skill at 2+ [Target Aim], gain 1 [Slash DMG Up] next turn

#### Pasywka bojowa: Snipe - Archery

*od ulepszenia 4*

If this unit is in [Ready to Loose] state, replace the leftmost Base Attack Skill equipped on the Dashboard with "Bow's Glimmer", then use it at Combat Start  
- If, at max [Target Aim] Stack, this unit's Skill 3 is on neither the Dashboard nor the upcoming list of Skills when this effect activates, the Defense Skill equipped on the leftmost Skill Slot counts as a Skill 3, and will be used to activate "Bow's Glimmer"  
  
Gain the following effects based on which Base Attack Skill was replaced (Sin Affinity carries over from the replaced Skill)  
- Skill 1: Base Power +1, deal +11% damage  
- Skill 2: Base Power +1, Coin Power +1, deal +22% damage  
- Skill 3: Base Power +4, Coin Power +4, deal +44% damage  
  
※ If an E.G.O Skill was equipped at Combat Start, remove [Ready to Loose] and this unit does not use "Bow's Glimmer"

#### Pasywka bojowa: Shi-no-Yumi

*od ulepszenia 4; posiadane 3× Lust*

At 4 [Arrow - Shi] Stack: When this unit gains [Poise] Potency from Base Attack Skill effects, gain +1 [Poise] Count (3 times per Encounter; per-Encounter cap resets when [Arrow - Shi] drops to 3)  
If this unit used "Bow's Glimmer" Skill at 2+ [Target Aim], gain 2 [Slash DMG Up] next turn

#### Pasywka wsparcia: Aiming for the Bullseye

*od ulepszenia 3; rezonans 4× Lust*

Turn End: Apply 1 [Pierce DMG Up] next turn to the ally who inflicted the most [Bleed] Potency to enemies with its Skills and Passives (includes those from E.G.O Skills; if multiple Identities share the highest [Bleed] inflicted record for the turn, select the Identity earliest in the Deployment order. Does not activate if no one inflicted [Bleed] Potency that turn)

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

### 000 The Index Proselyte: 【Paper Slip】 — Faust

> Faust's 14th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 7                                                          |
| HP                        | 57 (+2,69 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 3–7 / 3–7                                      |
| Poziom obrony             | poziom +1                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×2 (Fatal), Blunt ×1 (Normal) |
| Progi Stagger (HP)        | 60% / 30%                                                  |
| Grzech wyróżniony         | Sloth                                                      |
| Przynależność             | Index_Finger                                               |
| Słowa kluczowe            | Poise, Sinking                                             |
| Data aktualizacji         | 20251231                                                   |

#### Umiejętność 1 (×3): Unerringly, as the Prescript Demands

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Slash |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Sloth  | Slash |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* If this Skill is marked with [Mark of the Prescript], deal +10% damage  
[On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]

*Od ulepszenia 2:* If this Skill is marked with [Mark of the Prescript], deal +10% damage  
At 6+ ([Poise] on self + [Sinking] on target), Coin Power +1  
[On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]

*Od ulepszenia 4:* If this Skill is marked with [Mark of the Prescript], Clash Power +1 and deal +20% damage  
Coin Power +1 for every 6 ([Poise] on self + [Sinking] on target) (max 2)  
[On Use] Gain +2 [Poise] Count  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 2: [On Crit] Inflict 1 [Sinking]

#### Umiejętność 2 (×2): Undertake the Prescript, Again Undertake

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Slash |          4 |         +3 |      3 |           +2 |    1 |
|          3 | Pride  | Slash |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* If this Skill is marked with [Mark of the Prescript], Clash Power +1  
[On Use] Gain 3 [Poise]  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 3: [On Hit] Inflict 1 [Sinking]

*Od ulepszenia 2:* If this Skill is marked with [Mark of the Prescript], Clash Power +1  
At 6+ ([Poise] on self + [Sinking] on target), Coin Power +1  
[On Use] Gain 3 [Poise] and +1 [Poise] Count  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Hit] Inflict 1 [Sinking]

*Od ulepszenia 4:* If this Skill is marked with [Mark of the Prescript], Final Power +1  
Coin Power +1 for every 6 ([Poise] on self + [Sinking] on target) (max 2)  
[On Use] Gain 3 [Poise] and +2 [Poise] Count  
Moneta 1: [On Hit] Gain 2 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Crit] Inflict +2 [Sinking] Count

#### Umiejętność 3 (×1): As the Prescript Demands, You Will Be Eliminated.

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Gloom  | Slash |          3 |         +4 |      3 |           +3 |    1 |
|          4 | Gloom  | Slash |          5 |         +4 |      3 |           +3 |    1 |

*Od ulepszenia 3:* If this Skill is marked with [Mark of the Prescript], deal +20% damage on Critical Hit  
At 6+ ([Poise] on self + [Sinking] on target), Coin Power +1  
[Combat Start] At 6+ [Grace of the Prescript], convert all Coins of this Skill to [Unbreakable Coin]s  
[On Use] Gain +3 [Poise] Count  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 3: Deal +2.5% damage for every [Grace of the Prescript] (max 20%)  
- At 9 [Grace of the Prescript], deal +30% damage instead  
Moneta 3: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Crit] Inflict +2 [Sinking] Count

*Od ulepszenia 4:* If this Skill is marked with [Mark of the Prescript], Final Power +1 and deal +30% damage on Critical Hit  
Coin Power +1 for every 6 ([Poise] on self + [Sinking] on target) (max 2)  
[Combat Start] At 6+ [Grace of the Prescript], convert all Coins of this Skill to [Unbreakable Coin]s and deal +30% damage  
[On Use] Gain +3 [Poise] Count  
- Gain [Poise] equal to ([Grace of the Prescript]/3) (rounded down)  
Moneta 1: [On Hit] Gain 1 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 3: Deal +5% damage for every [Grace of the Prescript] (max 40%)  
- At 9 [Grace of the Prescript], deal +60% damage instead  
Moneta 3: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Crit] Inflict +3 [Sinking] Count

#### Obrona: Prescript-granted, Prescript-woven Fabric

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Gloom  | obrona: kontra |          3 |         +2 |      3 |           +2 |    1 |
|          4 | Gloom  | obrona: kontra |          3 |         +3 |      3 |           +2 |    1 |

*Od ulepszenia 1:* Final Power +1 for every 3 [Grace of the Prescript] (max 3)  
[Combat Start] Gain Shield equal to 10% of max HP (once per turn)  
- Reduce Shield gained by 1% for every 5 [Karmic Consequence]; at 50+ [Karmic Consequence], does not gain Shield  
[On Use] Gain 2 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Hit] Inflict 1 [Sinking]

*Od ulepszenia 4:* Final Power +1 and deal +10% damage for every 3 [Grace of the Prescript] (max 3 and 30%, respectively)  
[Combat Start] Gain Shield equal to 15% of max HP (once per turn)  
- Reduce Shield gained by 1.5% for every 5 [Karmic Consequence]; at 50+ [Karmic Consequence], does not gain Shield  
[On Use] Gain 2 [Poise]  
Moneta 2: [On Hit] Inflict 1 [Sinking]  
Moneta 3: [On Hit] Inflict 1 [Sinking]

#### Pasywka bojowa: Prescript Delivered on Paper Slips

*od ulepszenia 1*

Turn Start:  
- Gain [Prescript: [Paper Slip] I] / [Prescript: [Paper Slip] II] / [Prescript: [Paper Slip] III] / [Prescript: [Paper Slip] IV] based on [Grace of the Prescript] on self  
- Inflict [The Prescript's Target] to a random enemy (in Focused Encounters, the Part)  
- Apply [Mark of the Prescript] to Base Attack Skills on this unit's Dashboard (1 per Slot, max 2 Skills)  
· At 6+ [Grace of the Prescript], the effect above prioritizes Skill 3  
- All of the effects above and [Prescript] execution checks do not trigger when this unit is Staggered, Immobilized, in Panic, or in E.G.O Corrosion

#### Pasywka bojowa: Will of the Prescript

*od ulepszenia 1*

Turn End: If [Prescript] was executed this turn, heal 4 SP and gain 1 [Grace of the Prescript] (once per turn)  
- When executing [Prescript], if the main target has [The Prescript's Target], heal 8 SP and gain 3 [Grace of the Prescript] instead  
  
Turn End: If [Prescript] was not executed this turn, gain 5 [Karmic Consequence]  
- At 9 [Grace of the Prescript], does not gain [Karmic Consequence]  
- If this unit attempted to execute [Prescript] at Combat Start, but could not target the enemy during the combat phase, does not gain [Karmic Consequence]

#### Pasywka bojowa: Prescript Delivered on Paper Slips

*od ulepszenia 2*

Turn Start:  
- Gain [Prescript: [Paper Slip] I] / [Prescript: [Paper Slip] II] / [Prescript: [Paper Slip] III] / [Prescript: [Paper Slip] IV] based on [Grace of the Prescript] on self  
- Inflict [The Prescript's Target] to a random enemy (in Focused Encounters, the Part)  
- Apply [Mark of the Prescript] to Base Attack Skills on this unit's Dashboard (1 per Slot, max 2 Skills)  
· At 6+ [Grace of the Prescript], the effect above prioritizes Skill 3  
- All of the effects above and [Prescript] execution checks do not trigger when this unit is Staggered, Immobilized, in Panic, or in E.G.O Corrosion

#### Pasywka bojowa: Will of the Prescript

*od ulepszenia 2*

Turn End: If [Prescript] was executed this turn, heal 4 SP and gain 1 [Grace of the Prescript] (once per turn)  
- When executing [Prescript], if the main target has [The Prescript's Target], heal 8 SP and gain 3 [Grace of the Prescript] instead  
  
Turn End: If [Prescript] was not executed this turn, gain 5 [Karmic Consequence]  
- At 9 [Grace of the Prescript], does not gain [Karmic Consequence]  
- If this unit attempted to execute [Prescript] at Combat Start, but could not target the enemy during the combat phase, does not gain [Karmic Consequence]

#### Pasywka bojowa: Proselyte's Blade

*od ulepszenia 2; posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom*

Deal +2% damage with Skills marked with [Mark of the Prescript] for every [Grace of the Prescript] on self (max 16%)  
- At 9 [Grace of the Prescript], deal +20% damage with Base Skills instead  
  
On Hit with a Base Skill against target that has [The Prescript's Target], gain 1 [Poise] and inflict 1 [Sinking] (once per turn)  
- Increase the number of times this effect can trigger per turn by 1 for every 3 [Grace of the Prescript] (max 2)  
  
- At 9 [Grace of the Prescript], Base Skills inflict +1 more [Sinking] Potency and this unit gains +1 more [Poise] Potency

#### Pasywka wsparcia: As the Prescript Orders...

*od ulepszenia 3; posiadane 1× Sloth, posiadane 1× Pride, posiadane 1× Gloom*

Effects apply to the Identity with the earliest Deployment order  
- Prioritizes The Index-faction Identities  
  
Combat Start: If this unit's leftmost Skill on the Dashboard and other allies target the same enemy Slot, said Skill deals +5% damage for every ally targeting the same Slot excluding this unit (max 15%, applies when this unit and allies both use Base Attack Skills to main-target enemy Slot)

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

### 000 The House of Spiders: The Ring Apprentice — Faust

> Faust's 15th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | 7                                                          |
| HP                        | 92 (+3,19 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–4 / 3–5 / 3–6 / 3–6                                      |
| Poziom obrony             | poziom +2                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×1 (Normal), Blunt ×2 (Fatal) |
| Progi Stagger (HP)        | 50% / 30%                                                  |
| Grzech wyróżniony         | Glut.                                                      |
| Przynależność             | Ring_Finger_Physical, Ring_Finger, Spider_House            |
| Słowa kluczowe            | Bleed, Charge                                              |
| Data aktualizacji         | 20260402                                                   |

#### Umiejętność 1 (×3): Butcher - Ribs

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Glut.  | Slash |          2 |         +4 |      2 |           +1 |    1 |
|          3 | Glut.  | Slash |          3 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Iron Maiden] exclusive Skill  
Moneta 2: [On Hit] Inflict 2 [Defense Level Down] next turn (once per turn)  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn (once per turn)

*Od ulepszenia 2:* [Iron Maiden] exclusive Skill  
[On Use] Clash Power +1 for every type of negative effect on target (max 2)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 2)  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 2 [Defense Level Down] next turn (once per turn)  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn (once per turn)

*Od ulepszenia 4:* [Iron Maiden] exclusive Skill  
[On Use] Clash Power +1 for every type of negative effect on target (max 2)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 3)  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 2 [Defense Level Down] next turn (once per turn)  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn (once per turn)

#### Umiejętność 2 (×2): Fascia Hungers

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Slash |          3 |         +4 |      3 |           +2 |    1 |
|          3 | Envy   | Slash |          4 |         +4 |      3 |           +2 |    1 |

*Od ulepszenia 1:* [Iron Maiden] exclusive Skill  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 3: [On Hit] Gain +4 [Corpus Ingredient] Count

*Od ulepszenia 2:* [Iron Maiden] exclusive Skill  
[On Use] Clash Power +1 for every type of negative effect on target (max 2)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 2)  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +2 [Bleed] Count  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 3: [On Hit] Gain +4 [Corpus Ingredient] Count

*Od ulepszenia 4:* [Iron Maiden] exclusive Skill  
[On Use] Clash Power +1 for every type of negative effect on target (max 2)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 4)  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +2 [Bleed] Count  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 3: [On Hit] Gain +4 [Corpus Ingredient] Count

#### Umiejętność 3 (×1): Repressed Flesh

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lust   | Slash |          3 |         +3 |      4 |           +3 |    1 |
|          4 | Lust   | Slash |          4 |         +3 |      4 |           +3 |    1 |

*Od ulepszenia 3:* [Iron Maiden] exclusive Skill  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 2)  
[On Use] At 10+ [Corpus Ingredient] Count, consume up to 20 [Corpus Ingredient] Count to gain the following effects:  
- Final Power +2  
- Deal +3% damage for every [Corpus Ingredient] Count consumed  
Moneta 1: [On Hit] Inflict 3 [Bleed]  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 3: [On Hit] Inflict 1 [Damage Down] next turn (once per turn)  
Moneta 4: Deal +5% damage for every type of negative effect on target (max 30%)  
Moneta 4: [On Hit] Inflict +1 [Bleed] Count

*Od ulepszenia 4:* [Iron Maiden] exclusive Skill  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 3)  
[On Use] At 10+ [Corpus Ingredient] Count, consume up to 20 [Corpus Ingredient] Count to gain the following effects:  
- Final Power +2  
- Deal +3% damage for every [Corpus Ingredient] Count consumed  
Moneta 1: [On Hit] Inflict 4 [Bleed]  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 3: [On Hit] Inflict 1 [Damage Down] next turn (once per turn)  
Moneta 4: Deal +5% damage for every type of negative effect on target (max 30%)  
Moneta 4: [On Hit] Inflict +1 [Bleed] Count

#### Umiejętność 4 (×0): Butcher - Ribs

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Glut.  | Slash |          2 |         +4 |      2 |           +3 |    1 |
|          3 | Glut.  | Slash |          3 |         +4 |      2 |           +3 |    1 |

*Od ulepszenia 1:* [The Self Unbound - Flow State] exclusive Skill  
Moneta 2: [On Hit] Inflict 2 [Defense Level Down] next turn (once per turn)  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn (once per turn)

*Od ulepszenia 2:* [The Self Unbound - Flow State] exclusive Skill  
Deal +5% damage for every type of negative effect on target (max 20%)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 2)  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 2 [Defense Level Down] next turn (once per turn)  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn (once per turn)

*Od ulepszenia 4:* [The Self Unbound - Flow State] exclusive Skill  
Deal +10% damage for every type of negative effect on target (max 30%)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 3)  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 2 [Defense Level Down] next turn (once per turn)  
Moneta 2: [On Hit] Gain 2 [Defense Level Up] next turn (once per turn)

#### Umiejętność 5 (×0): Time for Your Meal, Fascia

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Envy   | Slash |          3 |         +4 |      3 |           +4 |    1 |
|          3 | Envy   | Slash |          4 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 1:* [The Self Unbound - Flow State] exclusive Skill  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 2: [On Hit] Gain 1 [Haste] next turn (once per turn)  
Moneta 3: [On Hit] Gain +4 [Corpus Ingredient] Count

*Od ulepszenia 2:* [The Self Unbound - Flow State] exclusive Skill  
Deal +5% damage for every type of negative effect on target (max 20%)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 2)  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +2 [Bleed] Count  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 2: [On Hit] Gain 1 [Haste] next turn (once per turn)  
Moneta 3: [On Hit] Gain +4 [Corpus Ingredient] Count

*Od ulepszenia 4:* [The Self Unbound - Flow State] exclusive Skill  
Deal +10% damage for every type of negative effect on target (max 30%)  
[On Use] Final Power +1 for every 4 [Bleed] on target (max 4)  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +2 [Bleed] Count  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 2: [On Hit] Gain 1 [Haste] next turn (once per turn)  
Moneta 3: [On Hit] Gain +4 [Corpus Ingredient] Count

#### Umiejętność 6 (×0): Liberation of the Repressed Flesh

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Lust   | Slash |          3 |         +3 |      4 |           +5 |    1 |
|          4 | Lust   | Slash |          4 |         +3 |      4 |           +5 |    1 |

*Od ulepszenia 3:* [The Self Unbound - Flow State] exclusive Skill  
[On Use] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)  
[On Use] Final Power +1 for every 4 [Bleed] on the main target (max 2)  
[On Use] At 10+ [Corpus Ingredient] Count, consume up to 20 [Corpus Ingredient] Count and gain the following effects:  
- Final Power +2  
- Deal +1% damage for every [Corpus Ingredient] Count consumed  
- At 3+/5+ [Corpus Ingredient], gain +1/+2 Atk Weight  
- Convert all Coins on this Skill to [Unbreakable Coin]s  
Moneta 1: [On Hit] Inflict 3 [Bleed]  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 2: [On Hit] Gain 1 [Haste] next turn (once per turn)  
Moneta 3: [On Hit] Inflict 1 [Damage Down] next turn (once per turn)  
Moneta 3: [On Hit] Gain 1 [Slash DMG Up] next turn (once per turn)  
Moneta 4: Deal +5% damage for every type of negative effect on target (max 30%)  
Moneta 4: [On Hit] Inflict +1 [Bleed] Count

*Od ulepszenia 4:* [The Self Unbound - Flow State] exclusive Skill  
[On Use] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)  
[On Use] Final Power +1 for every 4 [Bleed] on the main target (max 3)  
[On Use] At 10+ [Corpus Ingredient] Count, consume up to 20 [Corpus Ingredient] Count and gain the following effects:  
- Final Power +2  
- Deal +1% damage for every [Corpus Ingredient] Count consumed  
- At 3+/5+ [Corpus Ingredient], gain +1/+2 Atk Weight  
- Convert all Coins on this Skill to [Unbreakable Coin]s  
Moneta 1: [On Hit] Inflict 4 [Bleed]  
Moneta 2: [On Hit] Inflict 1 [Bind] next turn (once per turn)  
Moneta 2: [On Hit] Gain 1 [Haste] next turn (once per turn)  
Moneta 3: [On Hit] Inflict 1 [Damage Down] next turn (once per turn)  
Moneta 3: [On Hit] Gain 1 [Slash DMG Up] next turn (once per turn)  
Moneta 4: Deal +5% damage for every type of negative effect on target (max 30%)  
Moneta 4: [On Hit] Inflict +1 [Bleed] Count

#### Obrona: Exhibition Arrangements

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: blok |          3 |        +10 |      1 |           +5 |    1 |
|          4 | Lust    | obrona: blok |          4 |        +10 |      1 |           +5 |    1 |

*Od ulepszenia 1:* [Clashable Guard]  
[Iron Maiden] exclusive Skill  
[Clash Win] Inflict +1 [Bleed] Count on the attacker (2 times per turn)  
[Clash Win] Deal Pierce damage equal to [Bleed] Potency on the attacker (max damage: 20)  
Moneta 1: [Unbreakable Coin]

*Od ulepszenia 4:* [Clashable Guard]  
[Iron Maiden] exclusive Skill  
[Clash Win] Inflict +2 [Bleed] Count on the attacker (2 times per turn)  
[Clash Win] Deal Pierce damage equal to ([Bleed] Potency on the attacker x 2) (max damage: 30)  
Moneta 1: [Unbreakable Coin]

#### Obrona: The Exhibition Begins

| Ulepszenie | Grzech  | Typ          | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------- | ------------ | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Neutral | obrona: unik |          3 |        +10 |      1 |           +2 |    1 |
|          4 | Lust    | obrona: unik |          4 |        +10 |      1 |           +2 |    1 |

*Od ulepszenia 1:* [The Self Unbound - Flow State] exclusive Skill  
[Combat Start] Gain 1 [Assist Defense] (once per turn)  
[On Evade] Inflict 1 [Bind] next turn against the attacker (once per turn)

*Od ulepszenia 4:* [The Self Unbound - Flow State] exclusive Skill  
[Combat Start] Gain 1 [Assist Defense] (once per turn)  
[On Evade] Inflict 1 [Bind] next turn against the attacker (once per turn)  
[On Evade] Gain 1 [Haste] next turn (once per turn)

#### Obrona: No Acts of Vandalism Allowed.

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Lust   | obrona: kontra |          3 |         +4 |      2 |           +2 |    1 |
|          4 | Lust   | obrona: kontra |          4 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [Clashable Counter]  
[The Self Unbound - Flow State] exclusive Skill  
[Assist Defense] exclusive Skill  
Deal +5% damage for every type of negative effect on target (max 20%)  
[On Use] If target has 6+ [Bleed], Coin Power +1  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count

*Od ulepszenia 4:* [Clashable Counter]  
[The Self Unbound - Flow State] exclusive Skill  
[Assist Defense] exclusive Skill  
Deal +10% damage for every type of negative effect on target (max 30%)  
[On Use] Coin Power +1 for every 6 [Bleed] on target (max 2)  
[On Use] At 10+ [Corpus Ingredient] Count, consume 5 [Corpus Ingredient] Count to gain the following effects:  
- Clash Power +1  
- Convert the final Coin on this Skill to [Unbreakable Coin]  
Moneta 1: [On Hit] Inflict +1 [Bleed] Count  
Moneta 2: [On Hit] Inflict 2 [Bleed]

#### Pasywka bojowa: Fascia, My Precious Artwork

*od ulepszenia 1*

Upon entering the Encounter for the first time, gain +(# of The Ring-faction allies on the field x 2) [Corpus Ingredient] Count (max 10)  
  
Skill End: If the Skill dealt HP or Shield damage, gain +5 [Corpus Ingredient] Count  
- If target is killed, gain +3 additional [Corpus Ingredient] Count  
  
Gain 1 [Corpus Ingredient] every time this unit consumes 10 cumulative [Corpus Ingredient] Count in this Encounter  
- If the above effect brings this unit's [Corpus Ingredient] Potency to 2 or higher, gain [Artwork: Fascia]  
  
Base Attack Skills and Clashable Counter Skill count as Skills that gain [Charge] Count

#### Pasywka bojowa: Armor of Protection and Repression

*od ulepszenia 1*

Upon entering the Encounter for the first time, gain [Iron Maiden]  
  
Turn End: If this unit has [Artwork: Fascia], this unit loses [Iron Maiden] and gains [The Self Unbound - Flow State] (once per Encounter)  
- When Staggered, recover from Stagger (excluding forced Staggers)

#### Pasywka bojowa: Fascia, My Precious Artwork

*od ulepszenia 2*

Upon entering the Encounter for the first time, gain +(# of The Ring-faction allies on the field x 2) [Corpus Ingredient] Count (max 10)  
  
Skill End: If the Skill dealt HP or Shield damage, gain +5 [Corpus Ingredient] Count  
- If target is killed, gain +3 additional [Corpus Ingredient] Count  
  
Gain 1 [Corpus Ingredient] every time this unit consumes 10 cumulative [Corpus Ingredient] Count in this Encounter  
- If the above effect brings this unit's [Corpus Ingredient] Potency to 2 or higher, gain [Artwork: Fascia]  
  
Base Attack Skills and Clashable Counter Skill count as Skills that gain [Charge] Count

#### Pasywka bojowa: Armor of Protection and Repression

*od ulepszenia 2*

Upon entering the Encounter for the first time, gain [Iron Maiden]  
  
Turn End: If this unit has [Artwork: Fascia], this unit loses [Iron Maiden] and gains [The Self Unbound - Flow State] (once per Encounter)  
- When Staggered, recover from Stagger (excluding forced Staggers)

#### Pasywka bojowa: Inspired by Critique

*od ulepszenia 2; posiadane 4× Lust*

Double the amount of Speed, Clash Power, damage buff gained from [Somatic Frisson-inspiring Melody]  
  
On Hit, if the Attack Skill inflicted a negative effect, heal 4 SP at Attack End (2 times per turn)

#### Pasywka bojowa: Fascia, My Precious Artwork

*od ulepszenia 4*

Upon entering the Encounter for the first time, gain +(# of The Ring-faction allies on the field x 2) [Corpus Ingredient] Count (max 10)  
  
Skill End: If the Skill dealt HP or Shield damage, gain +5 [Corpus Ingredient] Count  
- If target is killed, gain +3 additional [Corpus Ingredient] Count  
  
Gain 1 [Corpus Ingredient] every time this unit consumes 10 cumulative [Corpus Ingredient] Count in this Encounter  
- If the above effect brings this unit's [Corpus Ingredient] Potency to 2 or higher, gain [Artwork: Fascia]  
  
Base Attack Skills and Clashable Counter Skill count as Skills that gain [Charge] Count

#### Pasywka bojowa: Armor of Protection and Repression

*od ulepszenia 4*

Upon entering the Encounter for the first time, gain [Iron Maiden]  
  
Turn End: If this unit has [Artwork: Fascia], this unit loses [Iron Maiden] and gains [The Self Unbound - Flow State] (once per Encounter)  
- When Staggered, recover from Stagger (excluding forced Staggers)

#### Pasywka bojowa: Inspired by Critique

*od ulepszenia 4; posiadane 4× Lust*

Double the amount of Speed, Clash Power, damage buff gained from [Somatic Frisson-inspiring Melody]  
  
On Hit, if the Attack Skill inflicted a negative effect, heal 4 SP at Attack End (2 times per turn)  
- If this unit's SP is at max, gain 1 [Slash DMG Up] next turn when this unit heals SP with this effect (once per turn)

#### Pasywka wsparcia: Iron Maiden - Spikes

*od ulepszenia 3; posiadane 1× Lust, posiadane 2× Envy*

When hit, allies that equipped Defense Skill on their Slots this turn inflict 4 [Bleed] on the attacker (2 times per turn)  
- If the attacker already has [Bleed], inflict +2 [Bleed] Count instead

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

### 000 Dawn Office Fixer — Faust

> Faust's 16th Identity

| Parametr                  | Wartość bazowa                                             |
| ------------------------- | ---------------------------------------------------------- |
| Rzadkość                  | 000                                                        |
| Sezon                     | wydarzenie 9109                                            |
| HP                        | 66 (+2,88 za poziom)                                       |
| Szybkość (ulepszenia 1–4) | 3–5 / 3–6 / 4–7 / 4–7                                      |
| Poziom obrony             | poziom +0                                                  |
| Odporności                | Slash ×0,5 (Endured), Pierce ×2 (Fatal), Blunt ×1 (Normal) |
| Progi Stagger (HP)        | 55% / 25%                                                  |
| Grzech wyróżniony         | Pride                                                      |
| Przynależność             | Dawn                                                       |
| Słowa kluczowe            | Burn, Tremor                                               |
| Data aktualizacji         | 20260709                                                   |

#### Umiejętność 1 (×3): Flash of Sunup

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Pride  | Slash |          3 |         +3 |      2 |           +2 |    1 |
|          3 | Pride  | Slash |          3 |         +4 |      2 |           +2 |    1 |

*Od ulepszenia 1:* [On Use] Clash Power +1 for every 10 [Fire Butterfly Coffin] (max 2)  
[On Use] At 20+ [Fire Butterfly Coffin], Reuse the final Coin once  
Moneta 1: [On Hit] Inflict 1 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Tremor]

*Od ulepszenia 2:* [On Use] Final Power +1 for every 4 ([Burn] + [Tremor]) on target (max 2)  
[On Use] Clash Power +1 for every 10 [Fire Butterfly Coffin] (max 2)  
[On Use] At 20+ [Fire Butterfly Coffin], Reuse the final Coin once  
Moneta 1: [On Hit] Inflict 2 [Burn]  
Moneta 2: [On Hit] Inflict 1 [Tremor]

*Od ulepszenia 4:* [On Use] Final Power +1 for every 4 ([Burn] + [Tremor]) on target (max 3)  
[On Use] Gain 4 [Fire Butterfly Coffin]  
[On Use] Clash Power +1 for every 10 [Fire Butterfly Coffin] (max 3)  
[On Use] At 20+ [Fire Butterfly Coffin], Reuse the final Coin once  
Moneta 1: [On Hit] Inflict 2 [Burn] and +1 [Burn] Count  
Moneta 2: [On Hit] Inflict 1 [Tremor]

#### Umiejętność 2 (×2): Butterfly Slash

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Sloth  | Slash |          4 |         +5 |      2 |           +3 |    1 |
|          3 | Sloth  | Slash |          4 |         +6 |      2 |           +3 |    1 |

*Od ulepszenia 1:* [On Use] For every 10 [Fire Butterfly Coffin], gain the following effects:  
- Clash Power +1 (max 2)  
- Reuse the final Coin once (2 times per Skill)  
Moneta 2: [On Hit] Inflict 1 [Tremor]  
Moneta 2: [Reuse - On Hit] Inflict 1 [Burn]  
Moneta 2: [Reuse - On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (once per Skill)

*Od ulepszenia 2:* [On Use] Final Power +1 for every 4 ([Burn] + [Tremor]) on target (max 2)  
[On Use] Gain 3 [Fire Butterfly Coffin]  
[On Use] For every 10 [Fire Butterfly Coffin], gain the following effects:  
- Clash Power +1 (max 2)  
- Reuse the final Coin once (2 times per Skill)  
Moneta 1: [On Hit] At 10+ [Fire Butterfly Coffin], gain the following effects:  
- Inflict +1 [Burn] Count  
- Inflict +1 [Tremor] Count  
Moneta 2: [On Hit] Inflict 1 [Tremor]  
Moneta 2: [Reuse - On Hit] Inflict 1 [Burn]  
Moneta 2: [Reuse - On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (once per Skill)

*Od ulepszenia 4:* [On Use] Final Power +1 for every 4 ([Burn] + [Tremor]) on target (max 3)  
[On Use] Gain 6 [Fire Butterfly Coffin]  
[On Use] For every 10 [Fire Butterfly Coffin], gain the following effects:  
- Clash Power +1 (max 3)  
- Reuse the final Coin once (2 times per Skill)  
Moneta 1: [On Hit] For every 10 [Fire Butterfly Coffin], gain the following effects:  
- Inflict +1 [Burn] Count (max 2)  
- Inflict +1 [Tremor] Count (max 2)  
Moneta 2: [On Hit] Inflict 1 [Tremor]  
Moneta 2: [Reuse - On Hit] Inflict 1 [Burn]  
Moneta 2: [Reuse - On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (once per Skill)

#### Umiejętność 3 (×1): Eject

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Slash |          3 |         +4 |      3 |           +4 |    1 |
|          4 | Wrath  | Slash |          5 |         +4 |      3 |           +4 |    1 |

*Od ulepszenia 3:* [Before Use] At 30 [Fire Butterfly Coffin], activate "Eject - High Noon" instead (once per turn)  
[On Use] If target has 6+ ([Burn] + [Tremor]), Coin Power +1  
[On Use] Gain 5 [Fire Butterfly Coffin]  
[On Use] For every 10 [Fire Butterfly Coffin], gain the following effects:  
- Clash Power +1 (max 2)  
- Inflict +1 [Burn] Count (max 2)  
- Inflict +1 [Tremor] Count (max 2)  
- Reuse the final Coin once (2 times per Skill)  
Moneta 1: [On Hit] Inflict 2 [Tremor]  
Moneta 2: [On Hit] Trigger [Amplitude Conversion] into [Tremor - Scorch]  
Moneta 3: [On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (2 times per Skill)  
Moneta 3: [Reuse - On Hit] Inflict 1 [Burn]

*Od ulepszenia 4:* [Before Use] At 30 [Fire Butterfly Coffin], activate "Eject - High Noon" instead (once per turn)  
[On Use] Coin Power +1 for every 6 ([Burn] + [Tremor]) on target (max 2)  
[On Use] Gain 8 [Fire Butterfly Coffin]  
[On Use] For every 10 [Fire Butterfly Coffin], gain the following effects:  
- Clash Power +1 (max 3)  
- Inflict +1 [Burn] Count (max 3)  
- Inflict +1 [Tremor] Count (max 3)  
- Reuse the final Coin once (2 times per Skill)  
Moneta 1: [On Hit] Inflict 3 [Tremor]  
Moneta 2: [On Hit] Trigger [Amplitude Conversion] into [Tremor - Scorch]  
Moneta 3: [On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (3 times per Skill)  
Moneta 3: [Reuse - On Hit] Inflict 1 [Burn]

#### Umiejętność 4 (×0): Seconded Offensive

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          2 | Glut.  | Slash |          3 |         +3 |      2 |           +1 |    1 |
|          3 | Glut.  | Slash |          4 |         +3 |      2 |           +1 |    1 |

*Od ulepszenia 2:* Moneta 1: [On Hit] Inflict +1 [Tremor] Count (2 times per turn)  
Moneta 2: [On Hit] Inflict +1 [Burn] Count (2 times per turn)

*Od ulepszenia 3:* [On Use] Deal +1% damage for every [Fire Butterfly Coffin] on self (max 30%)  
Moneta 1: [On Hit] Inflict +1 [Tremor] Count (2 times per turn)  
Moneta 2: [On Hit] Inflict +1 [Burn] Count (2 times per turn)

*Od ulepszenia 4:* [On Use] Gain the following effects based on [Fire Butterfly Coffin] Stack:  
- Deal +2% damage for every Stack (max 60%)  
- Final Power +1 for every 10 Stacks (max 3)  
Moneta 1: [On Hit] Inflict +1 [Tremor] Count (2 times per turn)  
Moneta 2: [On Hit] Inflict +1 [Burn] Count (2 times per turn)

#### Umiejętność 5 (×0): Eject - High Noon

| Ulepszenie | Grzech | Typ   | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | ----- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | Slash |          3 |         +4 |      3 |           +5 |    3 |
|          4 | Wrath  | Slash |          5 |         +4 |      3 |           +5 |    3 |

*Od ulepszenia 3:* [Unfocused Volley]  
Activate the following effects on target with every hit of this Skill:  
- Inflict 1 [Burn] or 1 [Tremor]  
- If target has no [Tremor - Scorch], trigger [Amplitude Conversion] into [Tremor - Scorch] (once per target)  
[On Use]  
- Clash Power +3  
- If the main target has 6+ ([Burn] + [Tremor]), Coin Power +1 and Clash Power +2  
- Inflict +2 [Burn] Count on all targets  
- Inflict +2 [Tremor] Count on all targets  
[Attack End]  
- Inflict 1 [Power Down] next turn on all targets hit (once per turn)  
- Gain 1 [Battle Instinct]  
- Gain 1 [Overheated Coffin]  
Moneta 1: [Unbreakable Coin]  
Moneta 2: [Unbreakable Coin]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: Reuse this Coin (max 2 times)  
Moneta 3: [On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (2 times per Skill)

*Od ulepszenia 4:* [Unfocused Volley]  
Deal +([Burn] on self + [Burn] on target)% damage (max 20%, counted per target)  
Activate the following effects on target with every hit of this Skill:  
- Inflict 1 [Burn] or 1 [Tremor]  
- If target has no [Tremor - Scorch], trigger [Amplitude Conversion] into [Tremor - Scorch] (once per target)  
[On Use]  
- Clash Power +3  
- Coin Power +1 and Clash Power +2 for every 6 ([Burn] + [Tremor]) on the main target (max 2 and 4 respectively)  
- Inflict +3 [Burn] Count on all targets  
- Inflict +3 [Tremor] Count on all targets  
[Attack End]  
- Inflict 1 [Power Down] next turn on all targets hit (once per turn)  
- Gain 1 [Battle Instinct]  
- Gain 1 [Overheated Coffin]  
Moneta 1: [Unbreakable Coin]  
Moneta 2: [Unbreakable Coin]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: Reuse this Coin (max 2 times)  
Moneta 3: If this unit has [Battle Instinct], deal +([Burn] Potency on target / 2)% damage (max 20%)  
Moneta 3: [On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (3 times per Skill)

#### Obrona: Stigmatize

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          1 | Wrath  | obrona: kontra |          3 |         +4 |      2 |           +1 |    1 |
|          4 | Wrath  | obrona: kontra |          5 |         +4 |      2 |           +1 |    1 |

*Od ulepszenia 1:* [Clashable Counter]  
[On Use] At 5+ [Burn], Coin Power +1  
[On Use] Lose 5 [Burn] (once per turn)  
[Clash Win] Lose 3 [Burn] (once per turn)  
Moneta 1: [On Hit] Inflict 1 [Burn] (2 times per turn)  
Moneta 2: [On Hit] Inflict 1 [Tremor] (2 times per turn)

*Od ulepszenia 3:* [Clashable Counter]  
[Before Use] At 30 [Fire Butterfly Coffin], activate "Dismemberment at High Noon" instead (once per turn)  
- If this unit has [Overheated Coffin], the effect above does not activate  
[On Use] At 5+ [Burn], Coin Power +1  
[On Use] Lose 5 [Burn] (once per turn)  
[Clash Win] Lose 3 [Burn] (once per turn)  
Moneta 1: [On Hit] Inflict 1 [Burn] (2 times per turn)  
Moneta 2: [On Hit] Inflict 1 [Tremor] (2 times per turn)

*Od ulepszenia 4:* [Clashable Counter]  
[Combat Start] Gain 6 [Fire Butterfly Coffin] (once per Encounter)  
[Before Use] At 30 [Fire Butterfly Coffin], activate "Dismemberment at High Noon" instead (once per turn)  
- If this unit has [Overheated Coffin], the effect above does not activate  
[On Use] Coin Power +1 for every 5 [Burn] on self (max 2)  
[On Use] Lose 5 [Burn] (once per turn)  
[Clash Win] Lose 3 [Burn] (once per turn)  
Moneta 1: [On Hit] Inflict 1 [Burn] (2 times per turn)  
Moneta 2: [On Hit] Inflict 1 [Tremor] (2 times per turn)

#### Obrona: Dismemberment at High Noon

| Ulepszenie | Grzech | Typ            | Moc bazowa | Moc monety | Monety | Poziom ataku | Cele |
| ---------: | ------ | -------------- | ---------: | ---------: | -----: | -----------: | ---: |
|          3 | Wrath  | obrona: kontra |          3 |         +4 |      3 |           +5 |    3 |
|          4 | Wrath  | obrona: kontra |          5 |         +4 |      3 |           +5 |    3 |

*Od ulepszenia 3:* [Unfocused Volley]  
Deal +(missing HP percentage on self / 2)% damage (max 25%)  
Activate the following effects on target with every hit of this Skill:  
- Inflict 1 [Burn] or 1 [Tremor]  
- If target does not have [Tremor - Scorch], trigger [Amplitude Conversion] into [Tremor - Scorch] (once per target)  
[On Use]  
- Clash Power +3  
- If the main target has 6+ ([Burn] + [Tremor]), Coin Power +1 and Clash Power +2  
- Inflict +2 [Burn] Count on all targets  
- Inflict +2 [Tremor] Count on all targets  
[Attack End]  
- Consume up to 30 [Burn] on self and heal (5 + [Burn] consumed)% HP (max 35%)  
- Consume all [Fire Butterfly Coffin] on self  
- Gain 3 [Battle Instinct]  
Moneta 1: [Unbreakable Coin]  
Moneta 2: [Unbreakable Coin]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: Reuse this Coin (max 2 times)  
Moneta 3: [On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (2 times per Skill)

*Od ulepszenia 4:* [Unfocused Volley]  
Deal +(missing HP percentage on self)% damage (max 50%)  
Deal +([Burn] Potency on target)% damage (max 20%, counted per target)  
Activate the following effects on target with every hit of this Skill:  
- Inflict 1 [Burn] or 1 [Tremor]  
- If target does not have [Tremor - Scorch], trigger [Amplitude Conversion] into [Tremor - Scorch] (once per target)  
[On Use]  
- Clash Power +3  
- Coin Power +1 and Clash Power +2 for every 6 ([Burn] + [Tremor]) on the main target (max 2 and 4 respectively)  
- Inflict +3 [Burn] Count on all targets  
- Inflict +3 [Tremor] Count on all targets  
[Attack End]  
- Consume up to 30 [Burn] on self and heal (20 + [Burn] consumed)% HP (max 50%)  
- Consume all [Fire Butterfly Coffin] on self  
- Gain 3 [Battle Instinct]  
Moneta 1: [Unbreakable Coin]  
Moneta 2: [Unbreakable Coin]  
Moneta 3: [Unbreakable Coin]  
Moneta 3: Reuse this Coin (max 2 times)  
Moneta 3: If this unit has [Battle Instinct], deal +([Burn] Potency on target)% damage (max 20%)  
Moneta 3: [On Hit] Trigger [Tremor Burst]; then, reduce target's [Tremor] Count by 1 (3 times per Skill)

#### Pasywka bojowa: Heatproof Coat

*od ulepszenia 1*

Upon entering the Encounter for the first time, gain 0 [Fire Butterfly Coffin]  
  
Cannot be Staggered or fall below 1 HP due to [Burn] damage  
Take -50% damage from [Burn] effects (rounded down)  
- At less than 50% HP, take -75% damage from [Burn] effects instead (rounded down)

#### Pasywka bojowa: Seonbae

*od ulepszenia 1*

If Dawn Office Fixer Sinclair is on the field, activate the following effects:  
- Dawn Office Fixer Sinclair gains [High Noon]  
- Turn Start: If Dawn Office Fixer Faust is defeated, convert [High Noon] on Dawn Office Fixer Sinclair into [Loneliness at High Noon]

#### Pasywka bojowa: Heatproof Coat

*od ulepszenia 2*

Upon entering the Encounter for the first time, gain 0 [Fire Butterfly Coffin]  
  
Cannot be Staggered or fall below 1 HP due to [Burn] damage  
Take -50% damage from [Burn] effects (rounded down)  
- At less than 50% HP, take -75% damage from [Burn] effects instead (rounded down)

#### Pasywka bojowa: Seonbae

*od ulepszenia 2*

If Dawn Office Fixer Sinclair is on the field, activate the following effects:  
- Dawn Office Fixer Sinclair gains [High Noon]  
- Turn Start: If Dawn Office Fixer Faust is defeated, convert [High Noon] on Dawn Office Fixer Sinclair into [Loneliness at High Noon]

#### Pasywka bojowa: Feuerfalter [Stigma Workshop]

*od ulepszenia 2; posiadane 3× Wrath*

When other Dawn Office Identities meet the following conditions, Dawn Office Fixer Faust uses the "Seconded Offensive" Skill against the targeted enemy (once per turn per Identity)  
- At Base Skill Attack End: If the enemy that was hit is Staggered, use "Seconded Offensive" against said enemy  
(Does not activate if the said enemy was already Staggered Before Attack of the said Skill)  
- At Attack End of the following Skills, use "Seconded Offensive" on the enemy they hit (prioritizes Staggered targets):  
  · Dawn Office Rep Gregor's "Dawnsplitter" and "Crack of Dawn"  
  · Dawn Office Fixer Sinclair's "Stigmatize" and "Blazing Strike"  
  
If Dawn Office Fixer Sinclair is on the field: On Hit using Reused Coins of Dawn Office Fixer Faust's Base Skills, deal additional Wrath damage equal to [Burn] on targeted enemy (max 10; max 20 per turn)  
- Counts as activating [Burn]

#### Pasywka bojowa: Heatproof Coat

*od ulepszenia 3*

Upon entering the Encounter for the first time, gain 0 [Fire Butterfly Coffin]  
  
Cannot be Staggered or fall below 1 HP due to [Burn] damage  
Take -50% damage from [Burn] effects (rounded down)  
- At less than 50% HP, take -75% damage from [Burn] effects instead (rounded down)

#### Pasywka bojowa: Seonbae

*od ulepszenia 3*

If Dawn Office Fixer Sinclair is on the field, activate the following effects:  
- Dawn Office Fixer Sinclair gains [High Noon]  
- Turn Start: If Dawn Office Fixer Faust is defeated, convert [High Noon] on Dawn Office Fixer Sinclair into [Loneliness at High Noon]

#### Pasywka bojowa: Feuerfalter [Stigma Workshop]

*od ulepszenia 3; posiadane 3× Wrath*

Combat Start: When this unit has [Battle Instinct], gain (Stack x 3) [Fire Butterfly Coffin]  
  
When other Dawn Office Identities meet the following conditions, Dawn Office Fixer Faust uses the "Seconded Offensive" Skill against the targeted enemy (once per turn per Identity)  
- At Base Skill Attack End: If the enemy that was hit is Staggered, use "Seconded Offensive" against said enemy  
(Does not activate if the said enemy was already Staggered Before Attack of the said Skill)  
- At Attack End of the following Skills, use "Seconded Offensive" on the enemy they hit (prioritizes Staggered targets):  
  · Dawn Office Rep Gregor's "Dawnsplitter" and "Crack of Dawn"  
  · Dawn Office Fixer Sinclair's "Stigmatize" and "Blazing Strike"  
  
If Dawn Office Fixer Sinclair is on the field: On Hit using Reused Coins of Dawn Office Fixer Faust's Base Skills, deal additional Wrath damage equal to [Burn] on the targeted enemy (max 10; max 20 per turn)  
- Counts as activating [Burn]

#### Pasywka wsparcia: The Lone Fixer

*od ulepszenia 3; posiadane 3× Wrath, posiadane 3× Lust*

Combat Start: If there is only 1 surviving Identity, including Backup units, the said Identity gains 3 [Offense Level Up] and 3 [Defense Level Up]

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
