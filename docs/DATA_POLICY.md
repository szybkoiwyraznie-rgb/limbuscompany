# Dane gry, prywatność i Git

Repozytorium jest **publiczne**. Zasady przejęte z WWM i SRW
([LESSONS.md](../LESSONS.md), lekcje 9–11).

## Nigdy w Git

- Pliki binarne gry: bundle Unity, `*.assets`, `*.resS`, pliki wykonywalne i
  biblioteki, archiwa, czcionki gry, zrzuty pamięci.
- ZIP-y od właściciela (`LCB_DANE_*.zip`) w całości — trzymamy je w
  ignorowanym `google_drive/` lub `local/`.
- Dane konta, zapisy, logi gry, prywatne zrzuty ekranu, identyfikatory i linki
  do prywatnych plików Dysku, pełne ścieżki z nazwą użytkownika Windows.
- Teksty innych fanowskich tłumaczeń ([PRIOR_ART.md](PRIOR_ART.md)) — także
  chińskie/inne przekłady z luster (do `index/` kopiujemy tylko `kr` i `en`).
- Całe klony luster (`.git`, skrypty, inne języki) — tylko w `/tmp` lub
  `local/`; do repo trafiają skopiowane z nich pliki JSON z tekstami gry.

`tools/check_repository.py` odrzuca pliki > 10 MiB, typowe rozszerzenia
binariów gry i czcionki poza `assets/fonts/`. To nie jest skaner treści —
diff przeglądaj samodzielnie.

## W Git

- Kod, testy na danych wymyślonych, dokumentacja, manifesty.
- **Teksty gry jako JSON/MD (D-06, jak w WWM i SRW):**
  - **`index/`** — pliki tekstowe gry w formie JSON: `index/localize/kr` (źródło,
    D-05) i `index/localize/en` (odniesienie) bajt w bajt jak w grze oraz
    potrzebne tabele `index/static-data/` (Teatr Opowieści, etapy, walki,
    Identity, umiejętności, pasywki), z `index/MANIFEST.json` (źródło, liczby,
    SHA-256). Opis: [INDEX_FORMAT.md](INDEX_FORMAT.md). Wszystkie narzędzia domyślnie czytają
    stąd, a `git diff index/` po aktualizacji pokazuje, co zmieniła gra.
  - **`czytanki/`** — wygenerowane Czytanki i pliki ID w Markdown
    ([CZYTANKI.md](CZYTANKI.md)).
- **`wiedza/`:** wiedza o strukturze gry (nazwy plików, identyfikatory,
  liczby), np. `indeks_fabuly.json`, `kolejnosc_fabuly.json`.
- **`tlumaczenie/`, `zwrotki/` (planowane):** przyjęte przekłady i rejestr
  zwrotek tłumacza z raportami importu.
- **`assets/fonts/` (planowane):** wyłącznie czcionki na licencji pozwalającej
  na redystrybucję (np. SIL OFL) razem z plikiem licencji.

Teksty gry w repozytorium potwierdził właściciel 2026-11-25 (O-06 zamknięte;
repozytorium zostaje publiczne, jak WWM i SRW). Pliki binarne gry nadal
**nigdy** nie trafiają do Git.

## Wyjścia narzędzi

- `validate_collector_return.py` — tylko liczby; można wkleić do
  `EXPERIMENT_LOG.md` i PR.
- `inspect_localize.py` — na standardowe wyjście tylko liczby; plik raportu w
  `local/inspekcja/` zawiera nazwy plików i pól, a z `--probki N` także
  **fragmenty tekstu gry** → prywatny, nie wklejać do PR.
- Testy jednostkowe działają na danych wymyślonych (szybkie, niezależne od
  aktualizacji gry); `index/` służy do budowania wyników, nie do testów CI.

## Przekazywanie tekstów

Pakiety dla Tłumacza trafiają do tłumacza przez Dysk właściciela. Nie
przesyłamy tekstów gry do innych zewnętrznych usług bez decyzji właściciela.
