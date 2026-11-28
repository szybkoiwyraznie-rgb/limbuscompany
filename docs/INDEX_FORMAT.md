# `index/` — teksty gry w repozytorium

Decyzje: [DECYZJE.md](DECYZJE.md) D-02 i D-06; zasady: [DATA_POLICY.md](DATA_POLICY.md).
W `index/` leżą **teksty gry jako JSON** — źródło każdego budowania (pakiety
dla tłumacza, Czytanki, plik ID, docelowo paczka `Lang/`). **Plików binarnych
gry tu nie ma i nie będzie.**

## Układ

```text
index/
├── MANIFEST.json                    źródło, liczby plików i bajtów, SHA-256
├── localize/
│   ├── kr/  KR_*.json, StoryData/KR_*.json, …   źródło przekładu (D-05)
│   └── en/  EN_*.json, StoryData/EN_*.json, …   odniesienie
└── static-data/                     tabele struktury (nie tekst do przekładu)
    ├── storytheater-main/ storytheater-other/ storytheater-personality/ storytheater-mirrorworld/
    ├── story/ battle-story/ battle-ab/ RPGSystem/  etapy, walki, trasy
    └── personality/ skill/ personality-passive/ passive/   Identity, umiejętności, pasywki
```

- **`localize/<lang>/`** — pliki `Localize` dokładnie tak, jak je ma gra:
  te same nazwy i podkatalogi, **bajt w bajt** (także UTF-8 BOM w części
  plików). `.gitattributes` wyłącza dla nich konwersję końców wierszy, więc
  SHA-256 w Git = SHA-256 w grze. Format opisuje
  [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md).
- **`static-data/<tabela>/`** — tylko tabele, które czytają narzędzia
  (`tools/static_data.py`): kolejność scen z Teatru Opowieści, etapy i walki,
  statystyki Identity, umiejętności i pasywki.
- Japoński i inne języki nie są kopiowane (nie są potrzebne do przekładu; JP
  można dodać tym samym narzędziem, `--langs kr en jp`).

Dlaczego bez normalizacji do jednego pliku: pliki bajt w bajt sprawdza się
hashem, narzędzia czytają `index/localize` tak samo jak ZIP zbieracza
(`tools/localize.py`), a `git diff index/` po aktualizacji gry pokazuje
zmienione kwestie w ich naturalnym miejscu. Żaden plik nie przekracza 5 MB
(limit kontroli repozytorium: 10 MiB).

## `MANIFEST.json`

```json
{
 "format": "lcb-index-v1",
 "localize": {"zrodlo": "…", "jezyki": {"kr": {"pliki": 2449, "bajty": 24594177, "sha256": "…"}, "en": {…}}},
 "static_data": {"zrodlo": "…", "tabele": {"skill": {"pliki": 147, "bajty": 14629086, "sha256": "…"}, …}}
}
```

`sha256` katalogu to SHA-256 z kolejnych `ścieżka\0sha256(pliku)` w porządku
alfabetycznym — jedna liczba mówi, czy zawartość się zmieniła.

## Stan obecny (2026-11-25)

| Część | Źródło | Pliki | Bajty |
|---|---|---|---|
| `localize/kr` | zbieracz właściciela `LCB_DANE_20261125_190908_2e6403.zip` (build Steam **`26652290`**, E-007) | 2449 | 25 222 309 |
| `localize/en` | jw. (build Steam **`26652290`**) | 2406 | 26 225 485 |
| `static-data/` (12 tabel) | lustro `LEAGUE-OF-NINE/OpenLethe` @ `8f24cba5` (dane 2026-11-12; build nieznany, brak pliku licencji) | 1153 | 21 620 590 |

Pliki `localize/{kr,en}` pochodzą już bezpośrednio z instalacji Steam
właściciela (build `26652290`, oryginalne CRLF + BOM). `INWENTARZ.jsonl` ze
zbieracza potwierdził, że `StaticData` nie występuje w katalogu Steam jako
luźne pliki JSON, więc tabele struktury pozostają z lustra OpenLethe.

## Odświeżenie

```sh
# z paczki zbieracza właściciela (Localize kr + en)
python tools/import_data.py --localize google_drive/LCB_DANE_....zip --localize-source "zbieracz, build …"
# z lustra (katalog z kr/ en/) i StaticData
python tools/import_data.py --localize <story-data> --localize-source "…" \
    --static-data <…/StaticData> --static-source "…"
# potem przebuduj wyniki i zacommituj razem
python tools/story_index.py
python tools/build_reading.py --lang en && python tools/build_reading.py --lang kr
python tools/build_profiles.py --lang en && python tools/build_profiles.py --lang kr
```

Import zastępuje w całości podane języki/tabele, więc pliki usunięte z gry
znikają też z `index/` (widać to w `git diff --stat`).
