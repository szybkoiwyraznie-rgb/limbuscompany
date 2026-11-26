# Słownik terminów i konwencji dla tymczasowego przekładu UI/meta (`AI-tymczasowe`, `D-11`)

Ten plik obowiązuje wszystkie agenty Arena wykonujące tymczasowy przekład interfejsu, opisów technicznych oraz kart meta/statystyk (`"origin": "ai"`).
**Zasada nadrzędna (`D-11`):** przekład ludzkiego Tłumacza ma zawsze bezwzględny priorytet — każda forma ustalona przez Tłumacza w `tlumaczenie/` (obecnie `LC_PL1.zip`) jest wiążąca i nie wolno jej zmieniać.

---

## 1. Terminy kanoniczne ustalone przez Tłumacza (`LC_PL1.zip`)

| KR | EN | Kanoniczny przekład PL (Tłumacz) | Uwagi |
|---|---|---|---|
| 수감자 | Sinner / Sinners | **Grzesznik** / **Grzesznicy** | `LCB Sinner` → **Grzesznik LCB** |
| 인격 | Identity / Identities | **Tożsamość** / **Tożsamości** | `Identity Story` → **Historia Tożsamości** |
| 환상체 | Abnormality / Abnormalities | **Anomalia** / **Anomalie** | |
| 뒤틀림 | Distortion | **Wypaczenie** / **Wypaczenia** | |
| E.G.O | E.G.O | **E.G.O** | bez kropki na końcu (`E.G.O`, nie `E.G.O.`) |
| 엔케팔린 | Enkephalin | **Enkefalina** | `Enkephalin Module` → **Moduł Enkefaliny**, `Enkephalin Box` → **Skrzynka Enkefaliny** |
| 끈 | Thread | **Nić** | |
| 황금가지 | The Golden Boughs | **Złote Gałęzie** (l.poj. **Złota Gałąź**) | |
| 메피스토펠레스 | Mephistopheles | **Mefistofeles** | autobus LCB |
| 관리자 | Manager / Executive Manager | **Kierownik** / **Kierownik Wykonawczy** | zwracanie się do Dantego |
| 도시 | The City | **Miasto** | wielką literą w znaczeniu świata gry |
| 날개 | The Wings | **Skrzydła** (l.poj. **Skrzydło**) | Korporacje A–Z |
| 둥지 | The Nests | **Gniazda** (l.poj. **Gniazdo**) | |
| 뒷골목 | The Backstreets | **Zaułki** | |
| 특이점 | Singularity / Singularities | **Osobliwość** / **Osobliwości** | |
| 해결사 | Fixer / Fixers | **Fikser** / **Fikserzy** | pisownia przez `ks`! |
| 사무소 | Office / Offices | **Biuro** / **Biura** | |
| 조직 | Syndicate / Syndicates | **Syndykat** / **Syndykaty** | |
| 협회 | Association | **Stowarzyszenie** | np. `Seven Association South Section 6` → **Południowa Sekcja 6 Stowarzyszenia Seven** |
| 검계 | The Blade Lineage | **Ród Ostrza** | np. `Blade Lineage Salsu` → **Salsu z Rodu Ostrza** |
| 흑운회 | The Kurokumo Clan | **Klan Kurokumo** | np. `Kurokumo Wakashu` → **Wakashu z Klanu Kurokumo** |
| 거울 세계 | Mirror World | **Świat Lustrzany** / **Światy Lustrzane** | `Mirror Dungeon` → **Lustrzany Loch** / **Lustrzane Lochy** |
| 단테의 노트 | Dante's Notes | **Notatki Dantego** | |

---

## 2. Odmiana imion 12 Grzeszników (ustalona w `StoryTheaterMirrorWorldStoryTitle.json`)

| Nr | Imię (M.) | Dopełniacz (D. — *czyja?*) | Celownik (C.) | Narzędnik (N.) | Uwagi |
|---|---|---|---|---|---|
| 01 | **Yi Sang** | **Yi Sanga** | Yi Sangowi | Yi Sangiem | odmienne |
| 02 | **Faust** | **Faust** | Faust | Faust | nieodmienne (r. żeński) |
| 03 | **Don Quixote** | **Don Quixote** | Don Quixote | Don Quixote | nieodmienne (r. żeński w LCB!) |
| 04 | **Ryōshū** | **Ryōshū** | Ryōshū | Ryōshū | nieodmienne, zachowaj makrony `ō`/`ū` |
| 05 | **Meursault** | **Meursaulta** | Meursaultowi | Meursaultem | odmienne |
| 06 | **Hong Lu** | **Hong Lu** | Hong Lu | Hong Lu | nieodmienne |
| 07 | **Heathcliff** | **Heathcliffa** | Heathcliffowi | Heathcliffem | odmienne |
| 08 | **Ishmael** | **Ishmael** | Ishmael | Ishmael | nieodmienne (r. żeński) |
| 09 | **Rodion** | **Rodion** | Rodion | Rodion | nieodmienne (`Rodia` → D. `Rodii`) |
| 10 | **Sinclair** | **Sinclaira** | Sinclairowi | Sinclairem | odmienne |
| 11 | **Outis** | **Outis** | Outis | Outis | nieodmienne (r. żeński) |
| 12 | **Gregor** | **Gregora** | Gregorowi | Gregorem | odmienne |

---

## 3. Konwencje techniczno-bojowe dla UI i kart (`Fala 1` → `Fala 2` → `Fala 3`)

> Paczka `P01` (`1A Fundament bojowy`) jako pierwsza utrwala dokładne brzmienie etykiet `[SkillTag]`, grzechów i odporności; kolejne paczki **muszą** sprawdzać już zaimportowane wpisy w `tlumaczenie/pliki/` i trzymać 100% spójności.

### Grzechy / Atrybuty (`AttributeText.json`)
- `Wrath` (분노) → **Gniew**
- `Lust` (색욕) → **Żądza**
- `Sloth` (나태) → **Lenistwo**
- `Gluttony` (탐식) → **Obżarstwo**
- `Gloom` (우울) → **Posępność**
- `Pride` (오만) → **Pycha**
- `Envy` (질투) → **Zawiść**

### Typy ataku i odporności (`ResistText.json`)
- `Slash` (참격) → **Cięcie** (obrażenia **cięte**)
- `Pierce` (관통) → **Kłucie** (obrażenia **kłute**)
- `Blunt` (타격) → **Obuch** (obrażenia **obuchowe**)
- Odporności: `Fatal` → **Zabójcza**, `Weak` → **Słaba**, `Normal` → **Zwykła**, `Endured` → **Odporna**, `Ineff.` → **Nieskut.**

### Mechanika walki i rozwoju
- `Clash` (합) → **Starcie** (`Clash Power` → **Moc Starcia**, `[Clash Win]` → **[Wygrane Starcie]**, `[Clash Lose]` → **[Przegrane Starcie]**)
- `Coin` (코인) → **Moneta** (`Coin Power` → **Moc Monety**, `Heads` → **Awers**, `Tails` → **Rewers**, `[On Hit]` → **[Przy Trafieniu]**, `[Heads Hit]` → **[Trafienie Awersem]**, `[On Use]` → **[Przy Użyciu]**, `[Combat Start]` → **[Początek Walki]**, `[Turn End]` → **[Koniec Tury]**)
- `Base Power` / `Final Power` → **Moc Bazowa** / **Moc Końcowa**
- `Offense Level` / `Defense Level` → **Poziom Ataku** / **Poziom Obrony**
- `Sanity (SP)` (정신력) → **Poczytalność (SP)** (`Panic` → **Panika**, `Low Morale` → **Niskie Morale**)
- `Stagger` (흐트러짐) → **Oszołomienie** (`Stagger Threshold` → **Próg Oszołomienia**)
- `Resonance` / `Absolute Resonance` → **Rezonans** / **Rezonans Absolutny**
- `Uptie` (동기화) → **Synchronizacja** (`Uptie Tier` → **Poziom Synchronizacji**)
- `Threadspin` (환상해체 / 끈 엮기) → **Splot Nici**
- `E.G.O Gift` → **Dar E.G.O**, `E.G.O Corrosion` → **Korozja E.G.O**, `Awakening` → **Przebudzenie**
- `Lunacy` (광기) → **Szaleństwo** (`Paid Lunacy` → **Płatne Szaleństwo**, `Free Lunacy` → **Darmowe Szaleństwo**), `Egoshard` → **Odłamek E.G.O**

### 7 głównych archetypów statusów (`Potency` → **Siła**, `Count` → **Licznik**)
- `Burn` (화상) → **Podpalenie**
- `Bleed` (출혈) → **Krwawienie**
- `Tremor` (진동) → **Wstrząs** (`Tremor Burst` → **Wyładowanie Wstrząsu**)
- `Rupture` (파열) → **Rozdarcie**
- `Sinking` (침잠) → **Zatonięcie**
- `Poise` (호흡) → **Oddech**
- `Charge` (충전) → **Ładunek**

---

## 4. Twarde reguły techniczne walidatora (`tools/import_zwrotki.py --ai`)

1. **Nigdy nie tłumacz identyfikatorów w nawiasach kwadratowych `[…]` należących do silnika gry** (np. `[OnSucceedAttack]`, `[Combustion]`, `[Laceration]`, `[Vibration]`, `[Burst]`, `[Sinking]`, `[Breath]`, `[Charge]`, `[Protection]`) — gra sama podmienia je na przetłumaczone nazwy z `SkillTag.json` i `BattleKeywords.json`! (Wyjątkiem są dosłowne napisy w samym `SkillTag.json`, gdzie cały tekst źródłowy to np. `[On Hit]` i nie ma on linii `tokeny: zachowaj dokładnie: [...]`).
2. **Zachowaj 1:1 wszystkie placeholdery i tagi TMP**: `{0}`, `{1}`, `%d`, `%s`, `<color=#…>…</color>`, `<sprite name="…">`, `<i>…</i>`, `<b>…</b>`, `\n`.
3. **Nie wpisuj nic w elementach oznaczonych `(powtórzenie elementu N — nie wpisuj tu nic…)`** — importer dziedziczy je automatycznie.
4. **Styl UI i kart**: zwięzły, precyzyjny, naturalny polski język gier RPG; bez anglicyzmów tam, gdzie istnieje czytelny odpowiednik, i z poszanowaniem podanego `limit: do N znaków`.
