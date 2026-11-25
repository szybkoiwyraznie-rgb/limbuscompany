# Czytanki

Materiały do czytania fabuły i lore Limbus Company dla właściciela jako
gracza. Mają być wygodniejsze niż gra: ciągły tekst w dokładnej kolejności,
z nazwami Canto i etapów we właściwych miejscach i z mówcami. Do tego karty
osobowości (ID) i E.G.O pokazujące to, co jest w grze, w „ludzkiej” formie.
**Wzór: Czytanki SRW** (`srwy_episode_NN_PL.md` + `srwy_mission_deployments.md`)
oraz WWM.

**Status: specyfikacja (wymagania właściciela z 2026-11-25).** Generator
powstanie po pierwszym zbiorze danych (zbieracz 1.1.0, [COLLECTOR.md](COLLECTOR.md)).

## 1. Wymagania właściciela

1. **„Ludzkie” ułożenie**: czyta się jak scenariusz, a nie jak lista rekordów.
   Bez identyfikatorów technicznych przy każdej linijce.
2. **Dialogi w dokładnej chronologii**, w kolejności, w jakiej gra je pokazuje
   (sekcja 3).
3. **Nazwy Canto i etapów we właściwych miejscach**: Canto jako tytuł pliku i
   rozdziału, etap jako nagłówek przed jego scenami, „przed walką / po walce”
   jako podtytuł.
4. **Imiona mówiących jak w SRW**: `**Imię:** tekst`, narracja jako zwykły
   akapit lub kursywa.
5. **Plik z ID** pokazuje **faktycznie to, co jest w ID**: statystyki,
   odporności, umiejętności z monetami i efektami, pasywki, wsparcie, kwestie.
   Opisy, umiejętności i statystyki są w „ludzkiej” formie (sekcja 5).

## 2. Układ plików

```text
czytanki/
├── README.md                  spis treści, buildid gry, język wersji, legenda
├── fabula/
│   ├── 00_prolog.md           # Prolog — <tytuł>
│   ├── 01_canto-1.md          # Canto I — <tytuł>
│   ├── …
│   ├── intervallo-*.md
│   └── wydarzenia/<nazwa>.md
├── osobowosci/<grzesznik>.md  karty ID danego Grzesznika (sekcja 5)
├── ego/<grzesznik>.md         karty E.G.O
├── statusy.md                 słowniczek statusów i słów kluczowych (nazwa, opis, kolor)
└── postacie.md                indeks postaci: imię, przydomek, Canto, w których mówi
```

Pliki Markdown mają kodowanie UTF-8. Plik powyżej ok. 2,5 MB dzielimy na części
(`_a`, `_b`), jak w WWM i SRW. Generator jest deterministyczny, więc po
aktualizacji gry diff pokazuje tylko nowe i zmienione sceny.

## 3. Chronologia — skąd dokładna kolejność

- **Główne źródło: Teatr Opowieści gry** —
  `StaticData/static-data/storytheater-main/storytheater-main-<n>.json`. Dla
  każdego rozdziału (`subChapterId`, np. 101 = Canto I) zawiera listę
  `storyList` w kolejności gry. Każdy wpis ma `storyId` (plik sceny, np.
  `S107B`), `nodeId` (etap, np. 10107) i `stageDetail` (`Before`/`After`, czyli
  przed lub po walce). To ta sama kolejność, w której gra odtwarza fabułę.
  Format znamy z publicznej kopii danych z 2023 r. **[1]**. Na bieżącym zbiorze
  sprawdzimy, czy nadal tak wygląda.
- Uwaga: litera w nazwie pliku **nie** oznacza wprost „A = przed”. W danych
  z 2023 r. `S001B` = Before, `S001A` = After. Dlatego kolejność bierzemy z
  `storyList`, a nie z nazw.
- Sceny lochów w Canto (`1D101A` …) są w tej samej liście, przypięte do etapu.
  Nazwy pięter i sal pochodzą z `DungeonNode*`/`DungeonArea*`.
- Sceny spoza Teatru Opowieści (wydarzenia, opowieści osobowości) mają
  własne listy (`storytheater-other`, `storytheater-personality`). Gdy listy brak,
  kolejność wynika z nazw plików, a Czytanka **wyraźnie to zaznacza** (jak w
  SRW: „układ redakcyjny, nie dowód kolejności”).
- W obrębie sceny zachowujemy kolejność rekordów `dataList`.

## 4. Fabuła — wygląd

```markdown
# Canto I — <tytuł>

*Część: Inferno · <firma>, <dystrykt> · oś czasu: 984-01*

> <opis Canto z Teatru Opowieści>

---

## 1-1. <tytuł etapu>

*Miejsce etapu: <place z StageNode>*

> <opis etapu z gry, pisany przez Dantego>

### Przed walką

*<podpis miejsca ze sceny>*

<narracja: zwykły akapit>

**Gregor:** <kwestia>

**Ishmael:** <kwestia>

**Yuri** *(<tytuł>)*: <kwestia>

**Yuri:** <kwestia>

### Po walce

…

## 1-11. <tytuł etapu>

### Loch: <nazwa piętra / sali>

…
```

Zasady:

- **Mówca:** `model` → imię z `ScenarioModelCodes` (`name`). Gdy scena
  nadpisuje imię polem `teller`, wygrywa `teller`. Tytuł (`title`, np. ranga
  Fixera) pokazujemy kursywą przy pierwszej kwestii postaci w scenie i przy
  każdej zmianie tytułu.
- **Narracja:** rekord bez `model`/`teller` traktujemy jako narrację i
  pokazujemy jako zwykły akapit.
- **Miejsce:** pole `place` wyświetlamy kursywą jako podpis przy zmianie miejsca.
  Identyfikator tła (`bg` ze `Story/Effect`) **nie** trafia do tekstu, bo to
  nazwa techniczna.
- **Znaczniki:** `<color>`, `<b>` itp. zamieniamy na zwykły tekst. Pogrubienie i
  kursywa zostają tylko tam, gdzie znaczą to samo co w grze. `\n` staje się
  podziałem wiersza. Puste rekordy dźwiękowe (powtórzone `id`, pusty
  `content`) pomijamy.
- **Kwestie bitewne w scenach** (dymki w walce danego etapu) dajemy osobno
  pod etapem jako cytaty `>`, oznaczone jako warunkowe, gdy ich kolejność nie
  wynika z danych.

## 5. Karty osobowości (ID) i E.G.O — „to, co jest w ID”

Każda karta odpowiada ekranowi informacji o ID w grze. Wartości liczbowe
pochodzą z `StaticData`, a nazwy i opisy z `Localize`. Słowa kluczowe są
rozwinięte do nazw. Wygląd:

```markdown
## <tytuł ID> <imię Grzesznika>  ·  ID 10101  ·  ranga: 1 (gwiazdka)

*Sezon: 0 · Słowa kluczowe jednostki: <nazwy z UnitKeyword> · Sposób zdobycia: <…>*

| Statystyka | Wartość |
|---|---|
| HP | 72 na poz. 1, +2,48 na poziom → <wartość na maks. poziomie> |
| Szybkość | 4–6 (Uptie 1) · 4–7 (Uptie 2) · 4–8 (Uptie 3) |
| Obrona | 14 na poz. 1, +0,72 na poziom |
| Progi zachwiania (Stagger) | 65% · 35% · 15% HP |

**Odporności:** <typ 1> ×2,0 (<nazwa poziomu z gry>) · <typ 2> ×0,5 · <typ 3> ×1,0

### Umiejętność 1 — <nazwa>  (×3 w talii)

*Grzech: <nazwa z AttributeText> · Typ ataku: <nazwa z gry> · Cel: 1*

| Uptie | Moc bazowa | Moneta | Monet | Poziom ataku |
|---|---:|---:|---:|---:|
| 1 | 2 | +7 | 1 | <…> |
| 3 | 3 | +7 | 1 | <…> |

**Efekty:** <opis umiejętności, jeśli jest>

**Monety:**
1. *[<nazwa wyzwalacza>]* <opis monety z nazwą statusu> — 1 (Uptie 1) → 2 (Uptie 2+)

### Pasywka bitewna — <nazwa>
*Warunek: <grzech> ×3 (posiadane / rezonans)*
<opis>

### Pasywka wsparcia — <nazwa>
<opis>

### Kwestie
- **Zdobycie:** …
- **Rozmowa 1:** …
```

Zasady „ludzkiej” formy:

- **Słowa kluczowe rozwinięte:** wyzwalacz w opisie monety (np.
  `[OnSucceedAttackHead]`) zastępujemy nazwą z `BattleKeywords`. Status
  (`[Sinking]`) zastępujemy jego nazwą z `Bufs`. Opis statusu jest raz w
  `statusy.md`, a w karcie link do niego.
- **Uptie zestawione:** zamiast trzech powtórzonych bloków jedna tabela
  i opis zmian („1 → 2 od Uptie 2”).
- **Liczby po polsku:** przecinek dziesiętny, mnożniki odporności jako
  `×2,0`, zakresy szybkości jako `4–6`.
- **Nazwy poziomów odporności, grzechów i typów ataku** pochodzą z tekstów gry
  (`ResistText`, `AttributeText`, …), żeby zgadzały się z tym, co widać w grze.
  Po przekładzie są po polsku.
- Polskie nazwy (statusów, typów ataku, tytułów) pochodzą wyłącznie z przekładu
  Tłumacza. Agenci nie tłumaczą; w wersji EN są nazwy angielskie z gry.
- Nie zgadujemy niczego, czego nie ma w danych: brak opisu oznaczamy
  „gra nie zawiera opisu”, jak w SRW.
- **[?] Do sprawdzenia:** czy `StaticData` w bieżącej wersji gry jest w plikach
  tekstowych. W kopii z 2023 r. były to zwykłe JSON-y w
  `Assets/Resources_moved/StaticData/static-data/` (`personality`, `skill`,
  `passive`, `ego`, …). Jeśli dane przeniesiono lub zaszyfrowano, karty dostaną
  tylko nazwy i opisy, a brak statystyk zostanie oznaczony. Inne źródło
  zaproponujemy osobno.

## 6. Wersje językowe

- **Czytanka źródłowa — EN**: oficjalny przekład angielski, czytelny dla
  właściciela. Możliwa od razu po pierwszym zbiorze.
- **Czytanka polska** z przekładu Tłumacza. Fragmenty nieprzetłumaczone są po
  angielsku i oznaczone dyskretnie w README danej części, tak samo jak zapas
  EN w grze.
- Czytanki leżą w `czytanki/` w Git (decyzja właściciela,
  [DATA_POLICY.md](DATA_POLICY.md)). Generator i testy są w `tools/` i
  `tests/`.
