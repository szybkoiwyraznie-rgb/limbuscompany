# Limbus Company — 3. Noc Walpurgii — deploymenty misji

Dla każdego etapu: fale przeciwników, a pod nimi pełne karty (statystyki, opis, umiejętności z mocami monet, pasywki; Anomalie z częściami). Dane celowo powtarzają się między etapami. „poz.” = poziom jednostki w etapie; „(wsparcie)” = jednostka towarzysząca; „×N” = liczba sztuk. Wartości bazowe z StaticData. Walki z Anomaliami bez przypisanego etapu (lochy) → sekcja „Spotkania z Anomalią”.

## Część: Część `wp3`

### Etap 5-55

- **Fala 1:** Królowa Wróżek ×1 (poz. 45); Zbitka Wróżek ×3 (poz. 45)

#### Królowa Wróżek

*Wystąpienia: ×1 (poz. 45).*

| Parametr   | Wartość               |
| ---------- | --------------------- |
| Poziom     | —                     |
| HP         | 705 (+24,3 za poziom) |
| Odporności | wszystkie ×1 (Normal) |

*Opis:* Główne Ciało

**Części (anatomia):**

##### Tułów

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 639 (+22,02 za poziom)                                                                                                                                    |
| Szybkość           | 1–4                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Prawe Ramię

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 115 (+3,96 za poziom)                                                                                                                                     |
| Szybkość           | 1–4                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Lewe Ramię

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 115 (+3,96 za poziom)                                                                                                                                     |
| Szybkość           | 1–4                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Umiejętność: Dekret Królowej

| Poz. | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | obrona: blok |         10 |        +10 |      1 |    1 |

##### Umiejętność: Uderzenie Skrzydłami

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          3 |         +5 |      2 |    1 |

##### Umiejętność: Drapieżność

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Żądza  | Cięcie |          6 |        +10 |      1 |    1 |

##### Umiejętność: Głodne Trzepotanie

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Żądza  | Cięcie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Zarłaczny Głód

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Gniew  | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Wytchnienie

| Poz. | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: unik |          5 |        +10 |      1 |    1 |

**Pasywki:**

- **Momentary Satiation** — na koniec tury: jeżeli sojusznik z [Przygotowane Mięso] ma 1 HP, zabija tego sojusznika; następnie wszystkie Części zyskują 5 [Wrażliwość], [Spadek Mocy Ataku] i [Spadek Mocy Obrony].
- **Ravening Hunger** — na początku tury: jeżeli są żyjący sojusznicy z HP 25%- lub mniej, zabija wszystkich sojuszników.
przywraca HP równe (zabici sojusznicy x 5)% Maks. HP Core.
na koniec tury: bez żyjących sojuszników, zyskuje 20 [Wzrost Mocy Ataku] w następnej turze.
- **Torn Arm** — gdy Ramię zostaje zniszczone, co turę na początku tury Korpus zyskuje 5 Krwawienia.
- **Invitation to a Meal** — na koniec tury: wszyscy Grzesznicy przywracają 10 Poczytalności i zyskują +1 zasobu E.G.O każdego Atrybutu

#### Zbitka Wróżek

*Wystąpienia: ×3 (poz. 45).*

| Parametr   | Wartość               |
| ---------- | --------------------- |
| Poziom     | —                     |
| HP         | 34 (+1,18 za poziom)  |
| Odporności | wszystkie ×1 (Normal) |

*Opis:* Główne Ciało

**Części (anatomia):**

##### Tułów

| Parametr           | Wartość                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                                   |
| HP                 | 34 (+1,18 za poziom)                                                                                                                                                |
| Szybkość           | 2–5                                                                                                                                                                 |
| Progi oszołomienia | 60%                                                                                                                                                                 |
| Odporności         | Cięcie ×1,5; Obuch ×0,75; Gniew ×1,2; Żądza ×1,5 (Weak); Lenistwo ×0,75 (Endured); Pycha ×0,75 (Endured); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Umiejętność: Chrup Chrup

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          3 |         +1 |      2 |    1 |

##### Umiejętność: Żarłoczność

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          4 |        +10 |      1 |    1 |

##### Umiejętność: Małe Trzepotanie

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Gniew  | Cięcie |          3 |         +3 |      3 |    1 |

##### Umiejętność: Wytchnienie

| Poz. | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: unik |          5 |         +1 |      1 |    1 |

**Pasywki:**

- **Care** — na początku tury: przywraca HP równe 15% Maks. HP
- **Keep It Fresh** — HP nie spada poniżej 1

### Etap 5-56

- **Fala 1:** Królowa Wróżek ×1 (poz. 45); Zbitka Wróżek ×3 (poz. 45); Zbitka Wróżek ×1 (poz. 45) (wsparcie)

#### Królowa Wróżek

*Wystąpienia: ×1 (poz. 45).*

| Parametr   | Wartość               |
| ---------- | --------------------- |
| Poziom     | —                     |
| HP         | 705 (+24,3 za poziom) |
| Odporności | wszystkie ×1 (Normal) |

*Opis:* Główne Ciało

**Części (anatomia):**

##### Tułów

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 639 (+22,02 za poziom)                                                                                                                                    |
| Szybkość           | 5–7                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Prawe Ramię

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 115 (+3,96 za poziom)                                                                                                                                     |
| Szybkość           | 5–8                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Lewe Ramię

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 115 (+3,96 za poziom)                                                                                                                                     |
| Szybkość           | 5–9                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Umiejętność: Dekret Królowej

| Poz. | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | obrona: blok |         10 |        +10 |      1 |    1 |

##### Umiejętność: Uderzenie Skrzydłami

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          3 |         +5 |      2 |    1 |

##### Umiejętność: Drapieżność

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Żądza  | Cięcie |          6 |        +10 |      1 |    1 |

##### Umiejętność: Głodne Trzepotanie

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Żądza  | Cięcie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Zarłaczny Głód

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Gniew  | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Wytchnienie

| Poz. | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: unik |          5 |        +10 |      1 |    1 |

##### Umiejętność: Czas Zapłacić za Moją Opiekę

| Poz. | Grzech   | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | -------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Lenistwo | obrona: blok |          5 |         +5 |      1 |    1 |

**Pasywki:**

- **Torn Arm** — gdy Ramię zostaje zniszczone, co turę na początku tury Korpus zyskuje 5 Krwawienia.
- **Empty Belly** — na koniec tury: jeżeli sojusznik z [Przygotowane Mięso] jest Oszołomiony, zabija tego sojusznika.
- **Bottomless Hunger** — po zabiciu sojusznika przywraca 20 HP Core, a w następnej turze zyskuje 1 [Wrażliwość].
- **Hunger** — na koniec tury: jeżeli jednostka nie zdołała zabić sojusznika z Prepared Meat, zyskuje 1 [Głód]. przy 75%- HP, zyskuje 2. przy 50%- HP, zyskuje 3.
na początku tury: jeżeli jednostka zabiła sojusznika z Prepared Meat, traci 1 [Głód].
- **Momentary Satiation** — na koniec tury: przy 0 [Głód], zyskuje (liczba sojuszników zabitych w tej turze x 3) [Spadek Poziomu Ataku] i [Spadek Poziomu Obrony].
- **Ravening Hunger** — na koniec tury: przy 4 [Głód], zmienia wzór na silniejszy.
- **Invitation to a Meal** — na koniec tury: wszyscy Grzesznicy przywracają 10 Poczytalności i zyskują +1 zasobu E.G.O każdego Atrybutu

#### Zbitka Wróżek

*Wystąpienia: ×4 (poz. 45) · też jako wsparcie.*

| Parametr   | Wartość               |
| ---------- | --------------------- |
| Poziom     | —                     |
| HP         | 57 (+1,97 za poziom)  |
| Odporności | wszystkie ×1 (Normal) |

*Opis:* Główne Ciało

**Części (anatomia):**

##### Tułów

| Parametr           | Wartość                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                                   |
| HP                 | 57 (+1,97 za poziom)                                                                                                                                                |
| Szybkość           | 2–5                                                                                                                                                                 |
| Progi oszołomienia | 60%                                                                                                                                                                 |
| Odporności         | Cięcie ×1,5; Obuch ×0,75; Gniew ×1,2; Żądza ×1,5 (Weak); Lenistwo ×0,75 (Endured); Pycha ×0,75 (Endured); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Umiejętność: Chrup Chrup

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          3 |         +1 |      2 |    1 |

##### Umiejętność: Żarłoczność

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          4 |        +10 |      1 |    1 |

##### Umiejętność: Małe Trzepotanie

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Gniew  | Cięcie |          3 |         +3 |      3 |    1 |

##### Umiejętność: Wytchnienie

| Poz. | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: unik |          5 |         +1 |      1 |    1 |

**Pasywki:**

- **Care** — na początku tury: przywraca HP równe 15% Maks. HP

### Etap 5-57

- **Fala 1:** Królowa Wróżek ×1 (poz. 45); Zbitka Wróżek ×3 (poz. 45)

#### Królowa Wróżek

*Wystąpienia: ×1 (poz. 45).*

| Parametr   | Wartość               |
| ---------- | --------------------- |
| Poziom     | —                     |
| HP         | 705 (+24,3 za poziom) |
| Odporności | wszystkie ×1 (Normal) |

*Opis:* Główne Ciało

**Części (anatomia):**

##### Tułów

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 639 (+22,02 za poziom)                                                                                                                                    |
| Szybkość           | 1–4                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Prawe Ramię

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 115 (+3,96 za poziom)                                                                                                                                     |
| Szybkość           | 1–4                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Lewe Ramię

| Parametr           | Wartość                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                         |
| HP                 | 115 (+3,96 za poziom)                                                                                                                                     |
| Szybkość           | 1–4                                                                                                                                                       |
| Progi oszołomienia | 50%                                                                                                                                                       |
| Odporności         | Cięcie ×1,2; Obuch ×0,5; Gniew ×1,5 (Weak); Żądza ×1,2; Lenistwo ×0,5 (Ineff.); Pycha ×0,75 (Endured); Zawiść ×1,2; Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Umiejętność: Dekret Królowej

| Poz. | Grzech | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | obrona: blok |         10 |        +10 |      1 |    1 |

##### Umiejętność: Uderzenie Skrzydłami

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          3 |         +5 |      2 |    1 |

##### Umiejętność: Drapieżność

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Żądza  | Cięcie |          6 |        +10 |      1 |    1 |

##### Umiejętność: Głodne Trzepotanie

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Żądza  | Cięcie |          4 |         +3 |      3 |    1 |

##### Umiejętność: Zarłaczny Głód

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Gniew  | Cięcie |          5 |        +10 |      1 |    1 |

##### Umiejętność: Wytchnienie

| Poz. | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: unik |          5 |        +10 |      1 |    1 |

**Pasywki:**

- **Momentary Satiation** — na koniec tury: jeżeli sojusznik z [Przygotowane Mięso] ma 1 HP, zabija tego sojusznika; następnie wszystkie Części zyskują 5 [Wrażliwość], [Spadek Mocy Ataku] i [Spadek Mocy Obrony].
- **Ravening Hunger** — na początku tury: jeżeli są żyjący sojusznicy z HP 25%- lub mniej, zabija wszystkich sojuszników.
przywraca HP równe (zabici sojusznicy x 5)% Maks. HP Core.
na koniec tury: bez żyjących sojuszników, zyskuje 20 [Wzrost Mocy Ataku] w następnej turze.
- **Torn Arm** — gdy Ramię zostaje zniszczone, co turę na początku tury Korpus zyskuje 5 Krwawienia.
- **Invitation to a Meal** — na koniec tury: wszyscy Grzesznicy przywracają 10 Poczytalności i zyskują +1 zasobu E.G.O każdego Atrybutu

#### Zbitka Wróżek

*Wystąpienia: ×3 (poz. 45).*

| Parametr   | Wartość               |
| ---------- | --------------------- |
| Poziom     | —                     |
| HP         | 34 (+1,18 za poziom)  |
| Odporności | wszystkie ×1 (Normal) |

*Opis:* Główne Ciało

**Części (anatomia):**

##### Tułów

| Parametr           | Wartość                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poziom             | —                                                                                                                                                                   |
| HP                 | 34 (+1,18 za poziom)                                                                                                                                                |
| Szybkość           | 2–5                                                                                                                                                                 |
| Progi oszołomienia | 60%                                                                                                                                                                 |
| Odporności         | Cięcie ×1,5; Obuch ×0,75; Gniew ×1,2; Żądza ×1,5 (Weak); Lenistwo ×0,75 (Endured); Pycha ×0,75 (Endured); Zawiść ×1,5 (Weak); Szaleń. ×2 (Fatal); Trwoga ×2 (Fatal) |

*Opis:* Część

##### Umiejętność: Chrup Chrup

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          3 |         +1 |      2 |    1 |

##### Umiejętność: Żarłoczność

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Obżar. | Cięcie |          4 |        +10 |      1 |    1 |

##### Umiejętność: Małe Trzepotanie

| Poz. | Grzech | Typ    | Moc bazowa | Moc monety | Monety | Cele |
| ---: | ------ | ------ | ---------: | ---------: | -----: | ---: |
|    1 | Gniew  | Cięcie |          3 |         +3 |      3 |    1 |

##### Umiejętność: Wytchnienie

| Poz. | Grzech    | Typ          | Moc bazowa | Moc monety | Monety | Cele |
| ---: | --------- | ------------ | ---------: | ---------: | -----: | ---: |
|    1 | Posępność | obrona: unik |          5 |         +1 |      1 |    1 |

**Pasywki:**

- **Care** — na początku tury: przywraca HP równe 15% Maks. HP
- **Keep It Fresh** — HP nie spada poniżej 1
