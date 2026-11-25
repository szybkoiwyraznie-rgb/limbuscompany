# Czytanki

Materiały do czytania fabuły i lore Limbus Company dla właściciela — wygodniejsze
niż gra: ciągły tekst z mówcami, miejscami i spisem treści. Wzór: Czytanki z
projektów WWM/SRW (Markdown w częściach ~2,5 MB z indeksem `README.md`).

## Zawartość (plan)

1. **Fabuła główna** w kolejności Cantów i Intervallo: rozdział → scena
   (`StoryData`), kwestie jako `**Mówca:** tekst`, narracja kursywą, zmiany
   miejsca jako nagłówki.
2. **Opowieści osobowości i E.G.O** (kwestie, opisy, „wspomnienia”) pogrupowane
   według Grzesznika (Sinner).
3. **Wydarzenia** — osobno, z datą wydarzenia, jeśli da się ją ustalić.
4. **Indeksy**: postaci (z `ScenarioModelCodes`), miejsca, pojęcia (słowa
   kluczowe gry), z odsyłaczami do rozdziałów.

## Wersje

- **Źródłowa (KR z EN obok)** — możliwa od razu po pierwszym zbiorze.
- **Polska** — z przekładu Tłumacza, gdy dany fragment jest przetłumaczony;
  nieprzetłumaczone fragmenty oznaczone i w języku źródłowym.

## Zasady

- Czytanki leżą w repozytorium w `czytanki/` (jak w WWM/SRW,
  [DATA_POLICY.md](DATA_POLICY.md)); generator i testy w `tools/`/`tests/`.
- Generator jest deterministyczny: ten sam wyciąg → te same pliki, więc diff
  po aktualizacji gry pokazuje tylko nowe/zmienione sceny.
- Kolejność scen: z danych gry (nazwy/ID rozdziałów); gdzie kolejność jest
  hipotezą, Czytanka to zaznacza.
- Format: Markdown UTF-8, części ~2,5 MB, `README.md` ze spisem treści i
  `buildid`, z którego powstały.
