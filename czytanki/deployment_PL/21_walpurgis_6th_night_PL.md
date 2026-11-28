# Limbus Company — 6. Noc Walpurgii — deploymenty misji

Dla każdego etapu: fale przeciwników, a pod nimi pełne karty (statystyki, opis, umiejętności z mocami monet, pasywki; Anomalie z częściami). Dane celowo powtarzają się między etapami. „poz.” = poziom jednostki w etapie; „(wsparcie)” = jednostka towarzysząca; „×N” = liczba sztuk. Wartości bazowe z StaticData. Walki z Anomaliami bez przypisanego etapu (lochy) → sekcja „Spotkania z Anomalią”.

## Część: Część `wp6`

### Etap 5-66

- **Fala 1:** Rycerz Rozpaczy ×1 (poz. 55); Sword of a Forgotten Knight ×1 (poz. 55) (wsparcie); Sword of a Forgotten Knight ×1 (poz. 55) (wsparcie); Sword of a Forgotten Knight ×1 (poz. 55) (wsparcie)

#### Rycerz Rozpaczy

*Wystąpienia: ×1 (poz. 55).*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 783 (+27 za poziom)   |
| Sloty akcji | start: 3 · maks. 4    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr           | Wartość                               |
| ------------------ | ------------------------------------- |
| Poziom             | —                                     |
| HP                 | 783 (+27 za poziom)                   |
| Szybkość           | 2–4                                   |
| Progi oszołomienia | 90% / 10%                             |
| Odporności         | Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Part

##### Umiejętność: Kaskada Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Ostre Łzy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      3 |    1 |

##### Umiejętność: Płynące Łzy Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      5 |    1 |

##### Umiejętność: Dzielony Smutek, Stępiały

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |        +11 |      1 |    1 |

##### Umiejętność: Gwałtowna Kaskada Pustej Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          6 |        +10 |      1 |   10 |

##### Umiejętność: Arkan: Łza i Przebicie

| Poz. | Grzech    | Typ            | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | -------------- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: kontra |          4 |         +4 |      5 |   10 |

**Pasywki:**

- **Rycerz Rozpaczy** — otrzymuje -50% obrażeń z [Podpalenie], [Krwawienie], [Wstrząs], [Rozdarcie] i [Zatonięcie] (zaokrąglone w dół)
jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu (nie zużywa też Licznika)
- **River of Helpless Tears** — na początku tury, jeżeli żaden z mieczy na polu nie ma [Bezsilne Łzy], nakłada [Bezsilne Łzy] na 1 losowy miecz (1 raz na turę; nie aktywuje się, jeżeli jakiś miecz ma [Bezsilne Łzy])
- **Shared Sorrow** — przy pierwszym Oszołamieniu dochodzi do siebie z Oszołamienia w następnej turze, po czym co turę zyskuje 10 [Ochrona] i 500 Tarczy
w następnej turze przyzywa Sword of a Forgotten Knight
- **Weathered Knight** — za każdym razem, gdy miecz wbije się w tę jednostkę, zyskuje 1 [Pokruszona Duma], a zyskiwane co turę [Ochrona] maleje o 3, a zyskiwane co turę HP Tarczy maleje o 100
przy 3 [Pokruszona Duma] jednostka przestaje zyskiwać [Ochrona] i Tarczę co turę, a zamiast tego zostaje Oszołamiona w następnej turze i zyskuje [Zwietczały Rycerz]
- **Hollow Pride** — na koniec tury po pierwszym Oszołamieniu, jeżeli jakiś Grzesznik ma 5+ [Zimne, Czarne Łzy], używa w następnej turze Umiejętności obszarowej
na koniec tury po pierwszym Oszołamieniu, jeżeli wszyscy Grzesznicy mają [Zimne, Czarne Łzy], zyskuje w następnej turze [Błogosławieństwo Rozpaczy]
- **One Last Justice** — gdy ta jednostka zostanie trafiona ARCANA SLAVE mając [Zwietczały Rycerz]: nie traci HP poniżej 5%, a na koniec tury unicestwia się

#### Sword of a Forgotten Knight

*Wystąpienia: ×3 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 42 (+1,45 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                |
| HP         | 42 (+1,45 za poziom)                                                                                                                             |
| Szybkość   | 1–3                                                                                                                                              |
| Odporności | Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          3 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

### Etap 5-67

- **Fala 1:** Rycerz Rozpaczy ×1 (poz. 55); Heart-breaking Sword ×1 (poz. 55) (wsparcie); Heart-tearing Sword ×1 (poz. 55) (wsparcie); Heart-piercing Sword ×1 (poz. 55) (wsparcie)

#### Rycerz Rozpaczy

*Wystąpienia: ×1 (poz. 55).*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 783 (+27 za poziom)   |
| Sloty akcji | start: 4 · maks. 4    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr           | Wartość                               |
| ------------------ | ------------------------------------- |
| Poziom             | —                                     |
| HP                 | 783 (+27 za poziom)                   |
| Szybkość           | 2–4                                   |
| Progi oszołomienia | 90% / 10%                             |
| Odporności         | Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Part

##### Umiejętność: Kaskada Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Ostre Łzy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      3 |    1 |

##### Umiejętność: Płynące Łzy Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      5 |    1 |

##### Umiejętność: Dzielony Smutek, Stępiały

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |        +11 |      1 |    1 |

##### Umiejętność: Gwałtowna Kaskada Pustej Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          6 |        +10 |      1 |   10 |

##### Umiejętność: Arkan: Łza i Przebicie

| Poz. | Grzech    | Typ            | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | -------------- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: kontra |          4 |         +4 |      5 |   10 |

**Pasywki:**

- **Rycerz Rozpaczy** — otrzymuje -50% obrażeń z [Podpalenie], [Krwawienie], [Wstrząs], [Rozdarcie] i [Zatonięcie] (zaokrąglone w dół)
jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu (nie zużywa też Licznika)
- **River of Helpless Tears** — na początku tury, jeżeli żaden z mieczy na polu nie ma [Bezsilne Łzy], nakłada [Bezsilne Łzy] na 1 losowy miecz (1 raz na turę; nie aktywuje się, jeżeli jakiś miecz ma [Bezsilne Łzy])
- **Shared Sorrow** — przy pierwszym Oszołamieniu dochodzi do siebie z Oszołamienia w następnej turze, po czym co turę zyskuje 10 [Ochrona] i 500 Tarczy
w następnej turze przyzywa Heart-breaking Sword, Heart-tearing Sword i Heart-piercing Sword
- **Weathered Knight** — za każdym razem, gdy miecz wbije się w tę jednostkę, zyskuje 1 [Pokruszona Duma], a zyskiwane co turę [Ochrona] maleje o 3, a zyskiwane co turę HP Tarczy maleje o 100
przy 3 [Pokruszona Duma] jednostka przestaje zyskiwać [Ochrona] i Tarczę co turę, a zamiast tego zostaje Oszołamiona w następnej turze i zyskuje [Zwietczały Rycerz]
- **Hollow Pride** — na koniec tury po pierwszym Oszołamieniu, jeżeli jakiś Grzesznik ma 5+ [Zimne, Czarne Łzy], używa w następnej turze Umiejętności obszarowej
na koniec tury po pierwszym Oszołamieniu, jeżeli wszyscy Grzesznicy mają [Zimne, Czarne Łzy], zyskuje w następnej turze [Błogosławieństwo Rozpaczy]
- **One Last Justice** — gdy ta jednostka zostanie trafiona ARCANA SLAVE mając [Zwietczały Rycerz] i mniej niż 600 HP: nie traci HP poniżej 5%, a na koniec tury unicestwia się

#### Heart-breaking Sword

*Wystąpienia: ×1 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 63 (+2,17 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                                                    |
| HP         | 63 (+2,17 za poziom)                                                                                                                                                                 |
| Szybkość   | 1–3                                                                                                                                                                                  |
| Odporności | Cięcie ×0,1; Kłucie ×0,1; Obuch ×2; Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          4 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          4 |         +5 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy, po czym w następnej turze przenosi swoją odporność „Fatal" na 1 inny losowy Miecz
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

#### Heart-tearing Sword

*Wystąpienia: ×1 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 63 (+2,17 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                                                    |
| HP         | 63 (+2,17 za poziom)                                                                                                                                                                 |
| Szybkość   | 1–3                                                                                                                                                                                  |
| Odporności | Cięcie ×2; Kłucie ×0,1; Obuch ×0,1; Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          4 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          4 |         +5 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy, po czym w następnej turze przenosi swoją odporność „Fatal" na 1 inny losowy Miecz
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

#### Heart-piercing Sword

*Wystąpienia: ×1 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 63 (+2,17 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                                                    |
| HP         | 63 (+2,17 za poziom)                                                                                                                                                                 |
| Szybkość   | 1–3                                                                                                                                                                                  |
| Odporności | Cięcie ×0,1; Kłucie ×2; Obuch ×0,1; Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +5 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy, po czym w następnej turze przenosi swoją odporność „Fatal" na 1 inny losowy Miecz
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

### Etap 5-68

- **Fala 1:** Rycerz Rozpaczy ×1 (poz. 55); Sword of a Forgotten Knight ×1 (poz. 55) (wsparcie); Sword of a Forgotten Knight ×1 (poz. 55) (wsparcie); Sword of a Forgotten Knight ×1 (poz. 55) (wsparcie)

#### Rycerz Rozpaczy

*Wystąpienia: ×1 (poz. 55).*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 783 (+27 za poziom)   |
| Sloty akcji | start: 3 · maks. 4    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr           | Wartość                               |
| ------------------ | ------------------------------------- |
| Poziom             | —                                     |
| HP                 | 783 (+27 za poziom)                   |
| Szybkość           | 2–4                                   |
| Progi oszołomienia | 90% / 10%                             |
| Odporności         | Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Part

##### Umiejętność: Kaskada Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Ostre Łzy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      3 |    1 |

##### Umiejętność: Płynące Łzy Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      5 |    1 |

##### Umiejętność: Dzielony Smutek, Stępiały

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |        +11 |      1 |    1 |

##### Umiejętność: Gwałtowna Kaskada Pustej Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          6 |        +10 |      1 |   10 |

##### Umiejętność: Arkan: Łza i Przebicie

| Poz. | Grzech    | Typ            | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | -------------- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: kontra |          4 |         +4 |      5 |   10 |

**Pasywki:**

- **Rycerz Rozpaczy** — otrzymuje -50% obrażeń z [Podpalenie], [Krwawienie], [Wstrząs], [Rozdarcie] i [Zatonięcie] (zaokrąglone w dół)
jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu (nie zużywa też Licznika)
- **River of Helpless Tears** — na początku tury, jeżeli żaden z mieczy na polu nie ma [Bezsilne Łzy], nakłada [Bezsilne Łzy] na 1 losowy miecz (1 raz na turę; nie aktywuje się, jeżeli jakiś miecz ma [Bezsilne Łzy])
- **Shared Sorrow** — przy pierwszym Oszołamieniu dochodzi do siebie z Oszołamienia w następnej turze, po czym co turę zyskuje 10 [Ochrona] i 500 Tarczy
w następnej turze przyzywa Sword of a Forgotten Knight
- **Weathered Knight** — za każdym razem, gdy miecz wbije się w tę jednostkę, zyskuje 1 [Pokruszona Duma], a zyskiwane co turę [Ochrona] maleje o 3, a zyskiwane co turę HP Tarczy maleje o 100
przy 3 [Pokruszona Duma] jednostka przestaje zyskiwać [Ochrona] i Tarczę co turę, a zamiast tego zostaje Oszołamiona w następnej turze i zyskuje [Zwietczały Rycerz]
- **Hollow Pride** — na koniec tury po pierwszym Oszołamieniu, jeżeli jakiś Grzesznik ma 5+ [Zimne, Czarne Łzy], używa w następnej turze Umiejętności obszarowej
na koniec tury po pierwszym Oszołamieniu, jeżeli wszyscy Grzesznicy mają [Zimne, Czarne Łzy], zyskuje w następnej turze [Błogosławieństwo Rozpaczy]
- **One Last Justice** — gdy ta jednostka zostanie trafiona ARCANA SLAVE mając [Zwietczały Rycerz]: nie traci HP poniżej 5%, a na koniec tury unicestwia się

#### Sword of a Forgotten Knight

*Wystąpienia: ×3 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 42 (+1,45 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                |
| HP         | 42 (+1,45 za poziom)                                                                                                                             |
| Szybkość   | 1–3                                                                                                                                              |
| Odporności | Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          3 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

### Etap 5-69

- **Fala 1:** Rycerz Rozpaczy ×1 (poz. 55); Heart-breaking Sword ×1 (poz. 55) (wsparcie); Heart-tearing Sword ×1 (poz. 55) (wsparcie); Heart-piercing Sword ×1 (poz. 55) (wsparcie)

#### Rycerz Rozpaczy

*Wystąpienia: ×1 (poz. 55).*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 783 (+27 za poziom)   |
| Sloty akcji | start: 4 · maks. 4    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr           | Wartość                               |
| ------------------ | ------------------------------------- |
| Poziom             | —                                     |
| HP                 | 783 (+27 za poziom)                   |
| Szybkość           | 2–4                                   |
| Progi oszołomienia | 90% / 10%                             |
| Odporności         | Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Part

##### Umiejętność: Kaskada Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Ostre Łzy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      3 |    1 |

##### Umiejętność: Płynące Łzy Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +3 |      5 |    1 |

##### Umiejętność: Dzielony Smutek, Stępiały

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |        +11 |      1 |    1 |

##### Umiejętność: Gwałtowna Kaskada Pustej Rozpaczy

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          6 |        +10 |      1 |   10 |

##### Umiejętność: Arkan: Łza i Przebicie

| Poz. | Grzech    | Typ            | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | -------------- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: kontra |          4 |         +4 |      5 |   10 |

**Pasywki:**

- **Rycerz Rozpaczy** — otrzymuje -50% obrażeń z [Podpalenie], [Krwawienie], [Wstrząs], [Rozdarcie] i [Zatonięcie] (zaokrąglone w dół)
jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu (nie zużywa też Licznika)
- **River of Helpless Tears** — na początku tury, jeżeli żaden z mieczy na polu nie ma [Bezsilne Łzy], nakłada [Bezsilne Łzy] na 1 losowy miecz (1 raz na turę; nie aktywuje się, jeżeli jakiś miecz ma [Bezsilne Łzy])
- **Shared Sorrow** — przy pierwszym Oszołamieniu dochodzi do siebie z Oszołamienia w następnej turze, po czym co turę zyskuje 10 [Ochrona] i 500 Tarczy
w następnej turze przyzywa Heart-breaking Sword, Heart-tearing Sword i Heart-piercing Sword
- **Weathered Knight** — za każdym razem, gdy miecz wbije się w tę jednostkę, zyskuje 1 [Pokruszona Duma], a zyskiwane co turę [Ochrona] maleje o 3, a zyskiwane co turę HP Tarczy maleje o 100
przy 3 [Pokruszona Duma] jednostka przestaje zyskiwać [Ochrona] i Tarczę co turę, a zamiast tego zostaje Oszołamiona w następnej turze i zyskuje [Zwietczały Rycerz]
- **Hollow Pride** — na koniec tury po pierwszym Oszołamieniu, jeżeli jakiś Grzesznik ma 5+ [Zimne, Czarne Łzy], używa w następnej turze Umiejętności obszarowej
na koniec tury po pierwszym Oszołamieniu, jeżeli wszyscy Grzesznicy mają [Zimne, Czarne Łzy], zyskuje w następnej turze [Błogosławieństwo Rozpaczy]
- **One Last Justice** — gdy ta jednostka zostanie trafiona ARCANA SLAVE mając [Zwietczały Rycerz] i mniej niż 600 HP: nie traci HP poniżej 5%, a na koniec tury unicestwia się

#### Heart-breaking Sword

*Wystąpienia: ×1 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 63 (+2,17 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                                                    |
| HP         | 63 (+2,17 za poziom)                                                                                                                                                                 |
| Szybkość   | 1–3                                                                                                                                                                                  |
| Odporności | Cięcie ×0,1; Kłucie ×0,1; Obuch ×2; Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          4 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          4 |         +5 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ   | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ----- | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Obuch |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy, po czym w następnej turze przenosi swoją odporność „Fatal" na 1 inny losowy Miecz
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

#### Heart-tearing Sword

*Wystąpienia: ×1 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 63 (+2,17 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                                                    |
| HP         | 63 (+2,17 za poziom)                                                                                                                                                                 |
| Szybkość   | 1–3                                                                                                                                                                                  |
| Odporności | Cięcie ×2; Kłucie ×0,1; Obuch ×0,1; Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          4 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          4 |         +5 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Cięcie |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy, po czym w następnej turze przenosi swoją odporność „Fatal" na 1 inny losowy Miecz
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum

#### Heart-piercing Sword

*Wystąpienia: ×1 (poz. 55) · też jako wsparcie.*

| Parametr    | Wartość               |
| ----------- | --------------------- |
| Poziom      | —                     |
| HP          | 63 (+2,17 za poziom)  |
| Sloty akcji | start: 1 · maks. 2    |
| Odporności  | wszystkie ×1 (Normal) |

*Opis:* Wróg zwykły

**Części (anatomia):**

##### Korpus

| Parametr   | Wartość                                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Poziom     | —                                                                                                                                                                                    |
| HP         | 63 (+2,17 za poziom)                                                                                                                                                                 |
| Szybkość   | 1–3                                                                                                                                                                                  |
| Odporności | Cięcie ×0,1; Kłucie ×2; Obuch ×0,1; Gniew ×0,8; Żądza ×0,8; Lenistwo ×0,8; Obżar. ×0,8; Posępność ×1,1; Pycha ×1,5 (Weak); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* KoD Sword Part

##### Umiejętność: Wyblakła Wiara

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +4 |      2 |    1 |

##### Umiejętność: Zwietrzała Duma

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          4 |         +5 |      2 |    1 |

##### Umiejętność: Nieskończona Rozpacz

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |         +5 |      2 |    1 |

##### Umiejętność: Miecz Zaostrzony Łzami

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Klinga Przesiąknięta Żałobą

| Poz. | Grzech    | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | Kłucie |          8 |         +8 |      1 |    1 |

**Pasywki:**

- **Despair-piercing Sword** — jeżeli miecz z [Bezsilne Łzy] osiągnie 0 HP, wbija się w Rycerza Rozpaczy, po czym w następnej turze przenosi swoją odporność „Fatal" na 1 inny losowy Miecz
- **Sword of a Forgotten Knight** — jeżeli trafi zniszczonym [Moneta Niezniszczalna], nie aktywuje efektu [Zatonięcie] celu
- **The Sword Points Toward Those Who Could Not be Protected** — jeżeli jest wróg z [Inkantacja - Arcana Slave], priorytet: ta jednostka
- **Respite** — HP tej jednostki nie spada poniżej 1, gdy nie ma [Bezsilne Łzy]
na koniec tury, jeżeli HP tej jednostki spadnie do 1, gdy nie ma [Bezsilne Łzy], przywraca HP do maksimum
