# Instrukcje dla agentów — Limbus Company PL

Projekt nieoficjalnej polskiej wersji **Limbus Company** (Project Moon, Steam,
Windows) oraz **Czytanek** — materiałów do czytania fabuły i lore dla
właściciela jako gracza. Sposób pracy przeniesiono z projektów właściciela
[`wherewindsmeet`](https://github.com/szybkoiwyraznie-rgb/wherewindsmeet) (WWM)
i [`mtgcrawler`](https://github.com/szybkoiwyraznie-rgb/mtgcrawler) (SRW OE/Y/Z),
**nie ich dane ani ustalenia o formatach**: Limbus Company ma własny silnik
(Unity), własny format tekstów i — co najważniejsze — **oficjalny mechanizm
własnych tłumaczeń** ([FEASIBILITY.md](docs/FEASIBILITY.md)).

## Podział ról

- **Agenci (Arena)** odpowiadają za stronę techniczną: zbieracz, wyciąg tekstów,
  Pakiety dla Tłumacza, import zwrotek, budowę paczki `Lang/`, Czytanki,
  aktualizacje, testy i dokumentację. Ponadto — wzorem projektu `wherewindsmeet`
  ([`D-11`](docs/DECYZJE.md), [PLAN_TLUMACZENIA_AI.md](docs/PLAN_TLUMACZENIA_AI.md))
  — **po wyraźnym sygnale właściciela** agenci tworzą tymczasowy przekład
  `AI-tymczasowe` (`"origin": "ai"`) **wyłącznie** dla interfejsu (UI), opisów
  technicznych mechanik/statusów oraz kart meta/statystyk (Tożsamości, skille,
  pasywki, E.G.O, Dary E.G.O, statystyki wrogów, UI/zadania/przedmioty RPG).
- **Tłumacz zewnętrzny** (wyspecjalizowany) ma bezwzględny priorytet w całym
  projekcie i jest wyłącznym autorem przekładu całej fabuły, dialogów, kwestii
  głosowych, tekstów piosenek, dzienników obserwacji, opisów lore w Notatkach
  Dantego, zdarzeń Anomalii oraz narracji/dialogów RPG. **Agent nigdy nie
  nadpisuje ani nie „poprawia” przekładu Tłumacza**; zwrotki Tłumacza zawsze
  zastępują wpisy `AI-tymczasowe`, a pakiety generowane dla Tłumacza pomijają
  wpisy `"origin": "ai"`, zostawiając czyste puste pola `PL:`.
- **Właściciel** podejmuje decyzje ([DECYZJE.md](docs/DECYZJE.md)), daje sygnał
  do rozpoczęcia fal `AI-tymczasowe`, uruchamia zbieracz u siebie, przekazuje
  pliki przez Dysk Google i testuje w grze.

## Początek każdej sesji

1. Przeczytaj `README.md`, `ENVIRONMENT.md`, `LESSONS.md`, `docs/CEL.md`,
   `docs/STATUS.md`, `docs/DECYZJE.md`, `docs/WORKFLOW.md`,
   `docs/DATA_POLICY.md`, `docs/FORMAT_LOCALIZE.md` oraz ostatnie wpisy
   `docs/EXPERIMENT_LOG.md`. Zajrzyj do `docs/PRIOR_ART.md`, zanim zaczniesz
   badać coś, co inni już opisali. **Nie pytaj właściciela o rzeczy
   rozstrzygnięte** w `CEL.md` i `DECYZJE.md`.
2. Sprawdź bieżącą gałąź, `git status` i otwarty PR z tej gałęzi. Nie nadpisuj
   cudzych ani niezacommitowanych zmian. W Arena pracuj i wypychaj **wyłącznie
   na gałęzi przydzielonej bieżącej sesji**, nigdy na `main`; nie przełączaj jej
   i nie twórz innej. Stare nazwy gałęzi w dokumentach są nieaktualne.
3. **Od razu PR, potem ciągłe checkpointy** (wymóg właściciela z SRW,
   2026-10-17): jeśli nie ma PR z tej gałęzi, zrób najmniejszy sensowny commit,
   wypchnij i otwórz roboczy PR **przed** większą pracą. Commituj i wypychaj
   każdy spójny fragment; przed końcem tury lub czekaniem na użytkownika
   wypchnij wszystko, co nadaje się do repozytorium. Sprawdź, że push się udał
   i PR wskazuje nowy commit. Nigdy nie scalaj ani nie zamykaj PR bez prośby.
4. Przed commitem obejrzyj listę i diff plików w indeksie, uruchom kontrole z
   `ENVIRONMENT.md`. Nie używaj ślepego `git add -f`. Przy błędzie
   uwierzytelniania GitHub poproś o ponowne połączenie GitHub w Arena — nigdy
   nie proś o hasła, tokeny ani kody 2FA. Jeśli push lub PR jest niemożliwy,
   powiedz to wprost.

## Zasady projektu

- **Tylko oficjalna ścieżka.** Tłumaczenie instalujemy wyłącznie jako
  *Custom Language* w `LimbusCompany_Data/Lang/` (mechanizm opisany przez
  Project Moon 2025-03-31). Nie modyfikujemy plików gry poza `Lang/`, nie
  patchujemy bundli Unity, plików wykonywalnych ani pamięci, nie używamy
  BepInEx/MelonLoader i nie obchodzimy zabezpieczeń. Jeśli coś da się
  przetłumaczyć tylko inną drogą — zapisz to jako ograniczenie, nie obchodź.
- **Dane gry:** do Git trafiają teksty, wyciągi, indeksy, powiązania i
  dokumentacja; **binarne pliki gry, jej czcionki, archiwa i zrzuty zostają poza
  Git** ([DATA_POLICY.md](docs/DATA_POLICY.md)). Surowe kopie ze zbieracza żyją
  w ignorowanym `local/` / `google_drive/`. Budowanie paczek i Czytanek ma
  działać **wyłącznie z repozytorium** — nigdy z `local/` ani z Dysku.
- **Zbieracz zamiast ręcznych oględzin** ([COLLECTOR.md](docs/COLLECTOR.md)):
  właściciel uruchamia `URUCHOM.bat`, ZIP wraca przez Dysk, agent sprawdza go
  `tools/validate_collector_return.py` i bada prywatnie. Nie proś o cały katalog
  gry ani o pliki spoza zakresu zbieracza; gdy potrzeba czegoś więcej, rozbuduj
  zbieracz (nowa wersja, test na Windows CI) i opisz zakres.
- **Nie kopiujemy cudzych tłumaczeń.** Istniejące fanowskie tłumaczenia (także
  polskie) analizujemy wyłącznie technicznie (układ plików, czcionki, problemy),
  nigdy nie przenosimy ich tekstu ([PRIOR_ART.md](docs/PRIOR_ART.md)).
- **Fakty, hipotezy, niewiadome.** Każdy wynik badań zapisuj w
  `docs/EXPERIMENT_LOG.md` (wejście, wersja/build, metoda, liczby, SHA-256,
  ograniczenia); `docs/STATUS.md` wskazuje aktualny stan i następny krok.
  Rozróżniaj test syntetyczny, test na kopii plików i test w grze. Nie
  ogłaszaj działania w grze bez zgłoszenia właściciela.
- **Wiązanie z wersją.** Każdy pakiet, zwrotka, paczka `Lang/` i Czytanka ma
  manifest z buildem Steam i SHA-256 wejść. Niezgodność wersji, zepsuty
  znacznik lub niejednoznaczne dopasowanie **zatrzymuje** operację — bez
  częściowego, cichego zapisu i bez zgadywania kolejności scen.
- **Aktualne narzędzia.** Gdy powstaje nowy generator zastępujący stary, stary
  dostaje `NIEAKTUALNE` w pierwszej linii docstringa, a tabela „aktualne
  narzędzia” w `docs/WORKFLOW.md` jest uaktualniana (lekcja SRW Y z 2026-11-10,
  [LESSONS.md](LESSONS.md)).
- **Układ Czytanek zaakceptowany przez właściciela jest zamrożony** — nie
  zmieniaj go bez nowego polecenia.
- Nie przesyłaj tekstów gry do zewnętrznych usług poza uzgodnionym kanałem
  (Dysk właściciela). Nie publikuj prywatnych identyfikatorów plików Dysku ani
  ścieżek z nazwą użytkownika w publicznych logach i PR.
- Nie uruchamiaj automatycznych wydań, dopóki nie powstanie i nie zostanie
  sprawdzony bezpieczny proces wydawania.
