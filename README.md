# Limbus Company — polska wersja językowa (nieoficjalna)

Fanowski projekt polskiego tłumaczenia gry **Limbus Company** (Project Moon,
Steam `1973530`) oraz **Czytanek** — czytelnych materiałów do poznawania
fabuły i lore. Projekt nie jest powiązany z Project Moon.

Gra od wersji 1.73.0 (2025-03-31) **oficjalnie obsługuje tłumaczenia
fanowskie** (Custom Language Support): tłumaczenie to folder z plikami JSON w
`LimbusCompany_Data/Lang/`, bez modyfikowania plików gry
([docs/CLS_FORMAT.md](docs/CLS_FORMAT.md)).

## Obieg

```text
gra u właściciela ──ZBIERACZ (BAT+PS1)──► ZIP na Pulpicie ──Dysk──► local/ (poza Git)
        │                                                              │
        │                                         tools/rozpoznanie_localize.py
        │                                         (struktura, bez treści)
        │                                                              ▼
        │                                 wyciag/ (KR źródło + EN/JP) + sceny + mówcy
        │                                         │                  │
        │                       Pakiet dla Tłumacza (KR→PL)     czytanki/ (KR/EN → PL)
        │                                         │
        │                         zwrotka Tłumacza → import z kontrolami → tlumaczenie/
        │                                         │
        └──── INSTALATOR (BAT+PS1) ◄── folder Lang/<pl> + Font + config.json
po aktualizacji gry: ZBIERACZ (tryb aktualizacji) → audyt różnic → pakiet uzupełniający
```

**Stan (2026-11-25):** fundamenty repozytorium, zasady, zbieracz Windows i
narzędzie rozpoznania struktury. Plików gry jeszcze nie odebrano. Szczegóły i
następny krok: [docs/STATUS.md](docs/STATUS.md).

## Od czego zacząć

- [Cel, kryteria akceptacji i otwarte decyzje](docs/CEL.md) · [Stan](docs/STATUS.md) · [Plan etapów](docs/ROADMAP.md)
- [Sposób pracy (Git, PR, obieg tłumaczenia)](docs/WORKFLOW.md) · [Lekcje z poprzednich projektów](LESSONS.md)
- [Format tłumaczeń CLS](docs/CLS_FORMAT.md) · [Zbieracz plików gry](docs/COLLECTOR.md)
- [Pakiet dla Tłumacza — projekt](docs/PAKIET_TLUMACZA.md) · [Czytanki — projekt](docs/CZYTANKI.md)
- [Dane gry, prywatność i Git](docs/DATA_POLICY.md) · [Wzorce i cudze projekty](docs/PRIOR_ART.md) · [Metoda i indeksy przejęte od innych](docs/METODA.md)
- [Dziennik eksperymentów](docs/EXPERIMENT_LOG.md) · [Środowisko i kontrole](ENVIRONMENT.md) · [Instrukcje dla agentów](AGENTS.md)

## Kontrole

```sh
python tools/check_repository.py
python tools/run_tests.py
```

## Układ repozytorium

```text
.github/       CI (Ubuntu i Windows × Python 3.11/3.12), szablony PR i zgłoszeń
collector/     źródła zbieracza Windows (BAT + PowerShell 5.1, tylko odczyt)
config/        polityka danych (co z danych gry może trafić do Git)
docs/          cel, stan, format CLS, projekty pakietu i Czytanek, dziennik
tools/         kontrola repozytorium, budowa i walidacja zbieracza, rozpoznanie
tests/         testy na wymyślonych danych (bez plików gry)
local/         surowe pliki gry i ZIP-y zbieracza — ignorowane przez Git
build/, dist/  lokalne wyniki (ZIP-y) — ignorowane przez Git
```

Planowane katalogi (powstaną, gdy będą potrzebne): `wyciag/` (wyciągnięte
teksty KR/EN/JP z kluczami i indeksami), `czytanki/`, `paczki/` (wysłane Pakiety
dla Tłumacza), `zwrotki/`, `tlumaczenie/` (magazyn przekładów), `instalator/`,
`assets/fonts/` (czcionki z licencją). Zasady: [DATA_POLICY.md](docs/DATA_POLICY.md).
