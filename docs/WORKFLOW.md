# Workflow projektu

## Kto co robi — obieg tygodniowy

```text
 WŁAŚCICIEL                         AGENT (Arena)                         TŁUMACZ
 ──────────                         ─────────────                         ───────
 1. po aktualizacji gry:
    uruchom grę, zamknij,
    URUCHOM.bat → LCB_DANE_*.zip
    → Dysk „Limbus Company”
                                    2. walidacja + inspekcja ZIP-a
                                       import_data → index/ (commit)
                                       audyt różnic z poprzednim buildem
                                    3. pakiet (pierwszy / uzupełniający)
                                       → Dysk właściciela
 4. przekazuje pakiet ────────────────────────────────────────────────▶  5. wypełnia PL:
                                                                            zwraca pliki .md
 6. wrzuca zwrotkę na Dysk  ◀────────────────────────────────────────────
                                    7. import (bramki), raport braków
                                       build_lang → dist/LCB_PL_*.zip
                                       Czytanki EN/PL
 8. instaluje Lang/, testuje w grze,
    zgłasza wynik / zrzuty           9. wpis w EXPERIMENT_LOG, STATUS,
                                       poprawki techniczne
```

Wczesne ostrzeżenie (O-07 = tak): publiczne lustro TW `story-data`
dostaje commit po każdej aktualizacji gry, więc agent może policzyć różnice
`kr` i przygotować audyt jeszcze przed paczką właściciela. Pakiet dla
tłumacza powstaje dopiero z paczki właściciela (znany build).

Komunikacja z właścicielem: krótko, po polsku, z jednym konkretnym krokiem do
zrobienia. Pytania tylko o otwarte decyzje z [DECYZJE.md](DECYZJE.md).

## Git i PR (każda sesja)

1. `git status --short --branch` i PR z bieżącej gałęzi
   (`gh pr list --state open --head "$(git branch --show-current)"`).
   Wyłącznie gałąź przydzielona sesji.
2. Brak PR → mały checkpoint, push, roboczy PR do `main` **przed** większą
   pracą.
3. Każdy spójny fragment: przegląd indeksu i diffu, kontrole z
   [ENVIRONMENT.md](../ENVIRONMENT.md), commit, push, sprawdzenie CI
   (`gh run list --branch <gałąź>`; błędy testów w adnotacjach:
   `gh api repos/<repo>/check-runs/<job>/annotations`).
4. W opisie PR: zakres, wyniki testów (Linux/Windows CI), ograniczenia, stan
   testów w grze. Bez scalania i zamykania bez prośby; bez force-push.
5. Po istotnej zmianie: [STATUS.md](STATUS.md); wyniki badań:
   [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md).

## Aktualne narzędzia

To jest **jedyne źródło prawdy**, którego narzędzia używać. Zastąpione
narzędzie dostaje `NIEAKTUALNE` w pierwszej linii docstringa i znika z tej
tabeli.

| Etap | Narzędzie | Stan |
|---|---|---|
| Zestaw zbieracza | `tools/build_collector_kit.py` (+ `collector/`) | gotowe, testy Linux + Windows CI |
| Kontrola ZIP-a od właściciela | `tools/validate_collector_return.py` | gotowe, testy syntetyczne |
| Rozpoznanie korpusu | `tools/inspect_localize.py` (czyta `tools/localize.py`) | gotowe, testy syntetyczne |
| Teksty gry → `index/` | `tools/import_data.py` | gotowe, zaimportowany aktualny build Steam `26917622` ([INDEX_FORMAT.md](INDEX_FORMAT.md)) |
| Audyt różnic buildów | `tools/audit_update.py` | gotowe, sprawdzone na żywej aktualizacji `26652290` → `26917622` (`--old-rev`, `--delta-scope {files,items}`, pakiet przyrostowy E-013) |
| Indeks fabuły (kolejność scen z danych gry) | `tools/story_index.py` (+ `tools/static_data.py`) → `wiedza/indeks_fabuly.json` | gotowe, testy syntetyczne; uruchamiane po nowym rozdziale lub historii Identity |
| Pakiet dla Tłumacza | `tools/build_package.py` (+ `tools/package_views.py`) | gotowe (`sceny.zip` + `widoki.zip` = 100% tekstów gry; `--wypelnij-pl` wpisuje przekład Tłumacza z pominięciem AI, `--tylko-ai` buduje pakiet weryfikacyjny — [PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md)) |
| Plan i paczki `AI-tymczasowe` (UI/meta) | `tools/prepare_ai_batches.py` → `paczki_ai/MANIFEST.json`, `local/paczki_ai/` | gotowe (`87` paczek `P01`–`P87` w 3 falach, `47 304` slotów UI/meta — [PLAN_TLUMACZENIA_AI.md](PLAN_TLUMACZENIA_AI.md)) |
| Import zwrotki | `tools/import_zwrotki.py` → `tlumaczenie/` | gotowe, pełny priorytet Tłumacza nad `--ai` (`"origin": "ai"`) + zgodność ze starszym pakietem (`--allow-older-package`) |
| Paczka `Lang/` | `tools/build_lang.py` → `dist/LCB_PL_*.zip` | gotowe, **potwierdzone w grze (`v.1.119.1`, E-012)**; domyślnie Tłumacz + AI, opcjonalnie `--no-ai` ([LANG_FORMAT.md](LANG_FORMAT.md)) |
| Kolejność fabuły (heurystyka storylogs, kontrola indeksu) | `tools/story_order.py` → `wiedza/kolejnosc_fabuly.json` | gotowe, testy syntetyczne |
| Czytanki fabularne | `tools/build_reading.py` (+ `tools/lcb_text.py`) → `czytanki/fabula_*` | gotowe, układ zaakceptowany i zamrożony (O-04, [CZYTANKI.md](CZYTANKI.md)) |
| Plik ID (profile Identity) | `tools/build_profiles.py` → `czytanki/plik_ID_*` | gotowe, układ zaakceptowany i zamrożony (O-04, [CZYTANKI.md](CZYTANKI.md)) |

## Bramki między etapami

| Krok | Wejście → wynik | Bramka |
|---|---|---|
| Zbieranie | gra właściciela → `LCB_DANE_*.zip` | walidator OK, znany build, SHA-256 |
| Rozpoznanie | ZIP → raport inspekcji, [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md) | pola tekstowe i tokeny opisane faktami z liczbami |
| Wyciąg | ZIP → `index/` | 100% plików `en` sparsowane, manifest, test spójności |
| Pakiet | `index/` → pakiet | kontekst scen, mówcy, tokeny, manifest |
| Zwrotka | pakiet + PL → `tlumaczenie/` | niezmienione EN, tokeny, atomowy zapis, raport |
| Paczka | `index/` + `tlumaczenie/` → `Lang/` | JSON-y parsują się, struktura = źródło, raport pokrycia |
| Gra | paczka → test właściciela | zgłoszenie z gry, wpis w dzienniku |
| Aktualizacja | stary + nowy `index/` → pakiet uzupełniający | nowe/zmienione/usunięte policzone, nic cicho nie przepada |

## CI

`.github/workflows/ci.yml`: kontrola indeksu i testy, Ubuntu i Windows ×
Python 3.11/3.12, dla PR do `main`, push na `main`/`arena/**` i ręcznie.
Uprawnienia tylko `contents: read`; CI **nie publikuje** wydań.
