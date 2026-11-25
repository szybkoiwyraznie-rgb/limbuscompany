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

- **Źródłowa (EN, opcjonalnie KR obok)** — możliwa od razu po pierwszym zbiorze.
- **Polska** — z przekładu Tłumacza, gdy dany fragment jest przetłumaczony;
  nieprzetłumaczone fragmenty oznaczone i w języku źródłowym.

## Zasady

- Czytanki zawierają tekst gry → przy `tekst_gry_w_git: false` leżą w `local/`
  i na Dysku (folder „Limbus Company/Czytanki”), nie w Git
  ([DATA_POLICY.md](DATA_POLICY.md)). W Git jest tylko generator i testy.
- Generator jest deterministyczny i nie dodaje treści od siebie — żadnych
  streszczeń ani komentarzy AI bez zgody właściciela ([CEL.md](CEL.md), pyt. 4).
- Kolejność scen: z danych gry (nazwy/ID rozdziałów); gdzie kolejność jest
  hipotezą, Czytanka to zaznacza.
- Format: Markdown UTF-8, części ~2,5 MB, `README.md` ze spisem treści i
  `buildid`, z którego powstały.
