# Lekcje przeniesione z wcześniejszych projektów

Wyciąg z doświadczeń projektów właściciela: **WWM** (Where Winds Meet,
`szybkoiwyraznie-rgb/wherewindsmeet`) oraz **SRW OE / Y / Z**
(`szybkoiwyraznie-rgb/mtgcrawler`). Ani w jednym, ani w drugim repo nie było
osobnego pliku z lekcjami — poniższe zebrano z ich `AGENTS.md`,
`ENVIRONMENT.md`, `docs/CEL.md` i dzienników eksperymentów. Każda lekcja ma
krótkie „dlaczego” i to, jak stosujemy ją w Limbus Company (LCB).

Nowe lekcje z tego projektu dopisuj na końcu, z datą i odnośnikiem do wpisu w
`docs/EXPERIMENT_LOG.md`.

## Organizacja pracy

1. **Roboczy PR od pierwszego commita, potem ciągłe checkpointy.** (SRW,
   2026-10-17.) Sesja potrafi się urwać; praca niewypchnięta przepada, a
   właściciel nie widzi postępu. → LCB: patrz `AGENTS.md`, punkt 3.
2. **Jedna gałąź na sesję; nigdy nie scalaj sam.** (WWM, SRW.) Arena śledzi
   sesję po gałęzi. Scalanie to decyzja właściciela.
3. **Nie pytaj o rzeczy rozstrzygnięte.** (WWM `CEL.md`.) Decyzje zapisuje się
   raz w `docs/CEL.md` / `docs/DECYZJE.md` i każda sesja zaczyna od ich
   przeczytania. Pytanie właściciela o to samo drugi raz kosztuje jego zaufanie.
4. **Status i dziennik są osobne.** `STATUS.md` mówi „gdzie jesteśmy i co
   dalej” w kilku linijkach; `EXPERIMENT_LOG.md` gromadzi dowody (liczby,
   hashe, metodę). Mieszanie ich robi z `STATUS` nieczytelną kronikę.
5. **Nieaktualne narzędzia oznaczaj wprost.** (SRW Y, 2026-11-10: agent użył
   starego generatora i zbudował paczkę w odrzuconym układzie.) Stary skrypt
   dostaje `NIEAKTUALNE` w pierwszej linii docstringa, a tabela aktualnych
   narzędzi w `docs/WORKFLOW.md` jest jedynym źródłem prawdy.
6. **Zaakceptowany układ jest zamrożony.** (SRW Y czytanki.) Gdy właściciel
   zaakceptuje wygląd Czytanek lub pakietu, kolejne sesje go nie „ulepszają”.

## Dane i dowody

7. **Fakt ≠ hipoteza ≠ test syntetyczny ≠ test w grze.** (WWM.) Każde
   twierdzenie o formacie ma etykietę i źródło. „Działa w grze” wolno napisać
   dopiero po zgłoszeniu właściciela.
8. **Liczby i SHA-256 w każdym wpisie.** (WWM, SRW.) Bez nich nie da się po
   aktualizacji gry stwierdzić, co się zmieniło, ani powtórzyć eksperymentu.
9. **Testy tylko na danych wymyślonych.** (WWM.) Repo jest publiczne; testy
   nie mogą wymagać plików gry ani zawierać jej tekstów. Generator danych
   syntetycznych (`tests/synthetic_localize.py`) naśladuje strukturę, nie treść.
10. **Binaria gry poza Git, teksty w Git.** (WWM, SRW.) Wyciągnięte teksty i
    indeksy są potrzebne do budowania z repozytorium i do diffów między
    wersjami; binaria, czcionki gry i archiwa — nie.
11. **Budowanie tylko z repozytorium.** (WWM.) Gdy build czyta Dysk albo
    `local/`, wyniku nie da się odtworzyć ani zweryfikować w CI.
12. **Wiązanie z wersją gry i odmowa przy niezgodności.** (WWM łatki.) Paczka
    zbudowana dla starego buildu wgrana po aktualizacji to najczęstsze źródło
    „zepsutego tłumaczenia”. Manifest z buildem Steam i hashami wejść; brak
    zgodności zatrzymuje operację.
13. **Nie zgaduj kolejności scen ani mówców.** (WWM `CEL.md`.) Lepszy jawny
    brak niż ciche, błędne dopasowanie — błąd kontekstu psuje przekład.

## Współpraca z właścicielem

14. **Zbieracz zamiast instrukcji klikania.** (WWM.) Właściciel uruchamia
    jeden `URUCHOM.bat`; skrypt sam znajduje grę, kopiuje tylko potrzebne pliki
    z kontrolą SHA-256, nie modyfikuje gry i pakuje wynik do ZIP-a.
    Niejednoznaczności rozstrzyga raport, nie rozmowa.
15. **Pliki dla Windows: CRLF, `.ps1` z BOM i ASCII, `-text` w
    `.gitattributes`.** (WWM.) PowerShell 5.1 bez BOM czyta skrypt w
    stronie kodowej ANSI, a LF w `.bat` potrafi zepsuć skoki do etykiet.
16. **Ścieżki z polskimi znakami, spacjami i nawiasami są normą.** (WWM.)
    Testy integracyjne zbieracza używają takich ścieżek celowo.
17. **Kanał zwrotny: Dysk Google.** (WWM.) Zbieracz zapisuje ZIP na Pulpicie;
    właściciel wrzuca go na Dysk. W WWM konektor Dysku odrzucał ZIP z `.ps1`;
    w LCB (2026-11-25) wgranie zestawu się udało, z zgodnym SHA-256 (E-003).
    Zawsze sprawdzaj `sha256Checksum` po wgraniu; zapasowo — „Code → Download
    ZIP” z GitHuba.

## Pakiety dla Tłumacza

18. **Kontekst przed tekstem.** (WWM `CEL.md`, SRW Y.) Tłumacz dostaje sceny w
    kolejności fabuły, z mówcą, miejscem i sąsiednimi kwestiami, a nie listę
    oderwanych identyfikatorów.
19. **Format elementu jak w SRW Y** — numer, typ i mówca, limit, tokeny do
    zachowania dokładnie, tekst źródłowy i puste pole `PL:`. Pliki dłuższe niż
    ~8000 linii dzielone na `_a`/`_b`, ze spisem scen. Szczegóły:
    [docs/PAKIET_TLUMACZA.md](docs/PAKIET_TLUMACZA.md).
20. **Przyrostowo: łatka → audyt → pakiet uzupełniający.** (WWM.) Po
    aktualizacji gry tłumacz dostaje tylko nowe i zmienione teksty, a import
    odrzuca zwrotkę dla innej wersji źródła.
21. **Kryterium odbioru: 100% tekstów, mówców i granic scen** w zakresie
    pakietu, z raportem braków. „Prawie wszystko” nie jest stanem końcowym.

## Środowisko agenta

22. **PowerShell nie działa w sandboxie Arena.** (LCB, 2026-11-25: pobranie
    PowerShell 7 dla Linuksa kończy się błędem SSL.) Skrypty `.ps1` sprawdzamy
    testami bajtów lokalnie, a ich działanie — wyłącznie w zadaniu Windows CI.
23. **Logi CI są niedostępne z sandboxa** (host z logami jest zablokowany).
    `tools/run_tests.py` wypisuje błędy jako adnotacje GitHub Actions; odczyt:
    `gh api repos/<repo>/check-runs/<job_id>/annotations`.
24. **W Windows PowerShell 5.1 unikaj cmdletów z modułów skryptowych**
    (`Get-FileHash`, `Compress-Archive`, `New-Guid`…). (LCB, 2026-11-25: na
    Windows CI `Get-FileHash` był „nierozpoznany”, bo PSModulePath wskazywał
    moduły PowerShell 7 — to samo może się zdarzyć u właściciela.) Używaj .NET;
    pilnuje tego `tests/test_collector_kit.py`.

## Rozpoznanie (LCB)

25. **Najpierw sprawdź, co zrobiła społeczność.** (LCB, 2026-11-25.) Lustra
    oryginalnych plików, kolejność fabuły i znane pułapki formatu (przesunięcia
    wierszy, „Unknown” przy braku elementu) były gotowe w publicznych repo.
    Bierzemy wiedzę i dane strukturalne, nigdy tekst przekładu ani kod GPL;
    każdą liczbę z cudzego lustra potwierdzamy na plikach właściciela.
26. **Tokeny wykrywaj listą znanych nazw, nie ogólnym wzorcem.** (LCB,
    2026-11-25.) `<…>` łapało dialogi w nawiasach ostrych (3190 tekstów).
    Przy okazji: czytnik zwraca bajty — zawsze przez `load_json`, inaczej
    statystyka po cichu wychodzi zerowa.
27. **Chronologię bierz z menu gry, nie z heurystyk.** (LCB, 2026-11-25.)
    Teatr Opowieści (`storytheater-*` w StaticData) podaje kolejność scen,
    węzeł etapu i moment walki; heurystyka po nazwach plików i dopasowanie do
    fanowskiej biblioteki były tylko przybliżeniem. Zawsze sprawdź, czy gra
    sama nie trzyma potrzebnej tabeli.
28. **Dane gry bywają „luźnym” JSON-em i mają BOM.** (LCB, 2026-11-25.)
    StaticData: część plików z BOM, jeden z przecinkiem przed `]`. Czytnik
    toleruje oba przypadki i raportuje pominięte pliki zamiast się wywracać.
29. **Nie zaostrzaj zasad właściciela na własną rękę.** (LCB, 2026-11-25.)
    Zgoda „wolno pracować na plikach gry” została błędnie zawężona do „teksty
    tylko poza repo”, choć w WWM i SRW teksty gry są w Git. Zasada jest prosta:
    **teksty gry (JSON/MD) w repozytorium, binaria nigdy**. Przy wątpliwości
    zapytaj, zamiast pisać w raporcie ograniczenie, którego nikt nie ustalił.
30. **Custom Language w `v.1.119.1` wymaga pełnego 5-kluczowego `config.json`
    oraz czcionek w `Font/Context/` i `Font/Title/`.** (LCB, 2026-11-25,
    `E-010`–`E-012`.) Bez niepustych plików `.ttf`/`.otf` w obu podkatalogach
    silnik pomija własny język po cichu nawet po wybraniu go w `Select Custom
    Language`; wewnątrz `Font/{Context,Title}/` trzymaj wyłącznie pliki
    czcionek (licencje osobno), a na przyciskach UI pilnuj limitów długości, bo
    stałe ramki nie zmniejszają czcionki automatycznie.
