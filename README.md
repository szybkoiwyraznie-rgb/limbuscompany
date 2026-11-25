# Limbus Company — nieoficjalne polskie tłumaczenie

Repozytorium techniczne nieoficjalnej polskiej wersji językowej gry
**Limbus Company** (Project Moon) oraz **Czytanek** — materiałów do czytania
fabuły i lore. Projekt fanowski, niepowiązany z Project Moon. Tłumaczenie
korzysta wyłącznie z oficjalnego mechanizmu *Custom Language* gry: nie
modyfikuje plików gry, a odinstalowanie to usunięcie folderu.

**Stan:** fundamenty gotowe, czekamy na pierwszą paczkę danych ze zbieracza —
[docs/STATUS.md](docs/STATUS.md).

## Dla właściciela — co zrobić teraz

1. Na GitHubie: **Code → Download ZIP**, rozpakuj na Pulpicie.
2. Jeśli gra była właśnie aktualizowana: uruchom ją raz, poczekaj na
   pobieranie danych, zamknij.
3. Kliknij dwa razy `collector/URUCHOM.bat`. Na Pulpicie powstanie
   `LCB_DANE_<data>_<id>.zip`.
4. Wgraj ten ZIP na Dysk Google (folder „Limbus Company”) i daj znać.

Szczegóły i prywatność: [collector/CZYTAJ_TO.txt](collector/CZYTAJ_TO.txt),
[docs/COLLECTOR.md](docs/COLLECTOR.md). Powtarzaj po każdej aktualizacji gry.

## Jak to działa

```text
gra właściciela ──URUCHOM.bat──▶ LCB_DANE_*.zip ──Dysk──▶ agent: walidacja, wyciąg → index/
                                                              │
     tłumacz ◀── Pakiet dla Tłumacza (sceny w kolejności, mówcy, tokeny) ◀┘
        │
        └─ zwrotka PL ──▶ import ──▶ tlumaczenie/ ──▶ Lang/<Nazwa>/ (paczka do gry)
                                               └───▶ Czytanki (EN, potem PL)
```

Podział ról: agenci robią całą technikę, zewnętrzny tłumacz tłumaczy z
Pakietów, właściciel decyduje i testuje w grze — [docs/WORKFLOW.md](docs/WORKFLOW.md).

## Dokumentacja

| Dokument | O czym |
|---|---|
| [AGENTS.md](AGENTS.md) | zasady dla agentów — czytać na początku każdej sesji |
| [ENVIRONMENT.md](ENVIRONMENT.md) | wymagania, kontrole, narzędzia, katalogi |
| [LESSONS.md](LESSONS.md) | lekcje z projektów WWM i SRW |
| [docs/CEL.md](docs/CEL.md) | cel, kryteria odbioru, rzeczy rozstrzygnięte |
| [docs/DECYZJE.md](docs/DECYZJE.md) | decyzje podjęte i otwarte |
| [docs/STATUS.md](docs/STATUS.md) | stan i następny krok |
| [docs/WORKFLOW.md](docs/WORKFLOW.md) | obieg pracy, aktualne narzędzia, bramki |
| [docs/FEASIBILITY.md](docs/FEASIBILITY.md) | oficjalny Custom Language, ryzyka |
| [docs/COLLECTOR.md](docs/COLLECTOR.md) | zbieracz danych |
| [docs/DATA_POLICY.md](docs/DATA_POLICY.md) | co trafia do Git, prywatność |
| [docs/FORMAT_LOCALIZE.md](docs/FORMAT_LOCALIZE.md) | format źródła `Localize` |
| [docs/LANG_FORMAT.md](docs/LANG_FORMAT.md) | format paczki `Lang/`, czcionki |
| [docs/PAKIET_TLUMACZA.md](docs/PAKIET_TLUMACZA.md) | Pakiety dla Tłumacza i import zwrotek |
| [docs/CZYTANKI.md](docs/CZYTANKI.md) | Czytanki |
| [docs/EXPERIMENT_LOG.md](docs/EXPERIMENT_LOG.md) | dziennik badań z liczbami i hashami |
| [docs/PRIOR_ART.md](docs/PRIOR_ART.md) | wcześniejsze prace (tylko wiedza techniczna) |
| [docs/ROADMAP.md](docs/ROADMAP.md) | etapy |

## Dla deweloperów

Python 3.11+, tylko biblioteka standardowa:

```sh
python tools/check_repository.py
python tools/run_tests.py
```

Testy używają wyłącznie danych wymyślonych; testy zbieracza z prawdziwym
PowerShell działają w Windows CI. Pliki binarne gry nigdy nie trafiają do Git
([docs/DATA_POLICY.md](docs/DATA_POLICY.md)).
