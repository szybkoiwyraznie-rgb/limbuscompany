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
- Teksty innych fanowskich tłumaczeń ([PRIOR_ART.md](PRIOR_ART.md)).
- Kopie publicznych luster oryginalnych plików (O-07) i raporty z nich —
  wyłącznie w ignorowanym `local/`.

`tools/check_repository.py` odrzuca pliki > 10 MiB, typowe rozszerzenia
binariów gry i czcionki poza `assets/fonts/`. To nie jest skaner treści —
diff przeglądaj samodzielnie.

## W Git

- Kod, testy na danych wymyślonych, dokumentacja, manifesty.
- **`wiedza/`:** wiedza o strukturze gry bez tekstu gry (nazwy plików,
  identyfikatory, liczby), np. `indeks_fabuly.json`, `kolejnosc_fabuly.json`.
- Pliki gry i lustra (także StaticData) są analizowane tylko poza repo
  (`local/`, `/tmp`; D-06); do Git trafiają wyłącznie pochodne identyfikatory.
- **`index/` (planowane, D-02):** znormalizowany wyciąg tekstów z
  `Localize/kr` (źródło, D-05), `en` (odniesienie) i `jp` z manifestem buildu Steam i SHA-256 plików
  źródłowych. Budowanie Pakietów, paczki `Lang/` i Czytanek czyta tylko stąd.
  Format zostanie opisany w `docs/INDEX_FORMAT.md` przy pierwszym wyciągu.
- **`tlumaczenie/`, `zwrotki/` (planowane):** przyjęte przekłady i rejestr
  zwrotek tłumacza z raportami importu.
- **`assets/fonts/` (planowane):** wyłącznie czcionki na licencji pozwalającej
  na redystrybucję (np. SIL OFL) razem z plikiem licencji.

> **Do potwierdzenia przez właściciela (O-06 w [DECYZJE.md](DECYZJE.md)):**
> w WWM i SRW właściciel zgodził się na teksty gry w repozytorium. Przed
> pierwszym commitem `index/` agent pyta jednym zdaniem, czy repozytorium
> pozostaje publiczne, czy ma zostać przełączone na prywatne. Do tego czasu
> prawdziwe wyciągi zostają w `local/`.

## Wyjścia narzędzi

- `validate_collector_return.py` — tylko liczby; można wkleić do
  `EXPERIMENT_LOG.md` i PR.
- `inspect_localize.py` — na standardowe wyjście tylko liczby; plik raportu w
  `local/inspekcja/` zawiera nazwy plików i pól, a z `--probki N` także
  **fragmenty tekstu gry** → prywatny, nie wklejać do PR.
- Testy i CI nigdy nie dotykają prawdziwych danych.

## Przekazywanie tekstów

Pakiety dla Tłumacza trafiają do tłumacza przez Dysk właściciela. Nie
przesyłamy tekstów gry do innych zewnętrznych usług bez decyzji właściciela.
