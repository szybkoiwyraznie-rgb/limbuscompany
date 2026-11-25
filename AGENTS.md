# Instrukcje dla agentów — Limbus Company PL

Nieoficjalne polskie tłumaczenie **Limbus Company** (Project Moon, Steam
`1973530`, Windows) oraz **Czytanki** — materiały do czytania fabuły i lore dla
właściciela. Agenci (Arena) odpowiadają za stronę techniczną. **Tekst tłumaczy
zewnętrzny Tłumacz** na podstawie Pakietu dla Tłumacza.

Sposób pracy przejmujemy z projektów właściciela
[`wherewindsmeet`](https://github.com/szybkoiwyraznie-rgb/wherewindsmeet) i
[`mtgcrawler`](https://github.com/szybkoiwyraznie-rgb/mtgcrawler) (SRW OE/Y) —
zob. [docs/PRIOR_ART.md](docs/PRIOR_ART.md) i [LESSONS.md](LESSONS.md).
**Nie przenoś na Limbus ich ustaleń o silniku, formatach, kluczach ani
patcherze.** Limbus ma oficjalny mechanizm tłumaczeń (Custom Language Support,
[docs/CLS_FORMAT.md](docs/CLS_FORMAT.md)) — nie ma tu binarnego patchowania.

## Początek każdej sesji

1. Przeczytaj w tej kolejności: `README.md`, `ENVIRONMENT.md`, `LESSONS.md`,
   `docs/CEL.md`, `docs/STATUS.md`, `docs/DATA_POLICY.md`, `docs/WORKFLOW.md`,
   `docs/CLS_FORMAT.md`, `docs/COLLECTOR.md` oraz ostatnie wpisy
   `docs/EXPERIMENT_LOG.md`. Przed badaniem czegoś od nowa zajrzyj do
   `docs/PRIOR_ART.md`. **Nie pytaj właściciela o rzeczy rozstrzygnięte w
   `docs/CEL.md`** — otwarte pytania są tam w osobnej sekcji.
2. Sprawdź bieżącą gałąź, `git status` i otwarty PR z tej gałęzi. Nie nadpisuj
   cudzych ani niezacommitowanych zmian. W Arena pracuj i wypychaj **wyłącznie
   na gałęzi przydzielonej bieżącej sesji** — nie na `main`, nie twórz i nie
   przełączaj gałęzi. Stara nazwa gałęzi z dokumentacji nie obowiązuje.
3. Jeśli z tej gałęzi nie ma PR, zrób najmniejszy sensowny checkpoint, wypchnij
   go i **od razu otwórz roboczy PR**, zanim zaczniesz większą pracę. Potem
   commituj i wypychaj **każdy spójny fragment**. Przed końcem tury i przed
   czekaniem na właściciela wypchnij wszystko, co nadaje się do repozytorium.
   Snapshoty sandboksa i pliki na Dysku **nie zastępują pusha**. Sprawdź, czy
   push się udał i czy PR wskazuje właściwy commit. Nie scalaj i nie zamykaj
   PR bez prośby właściciela.
4. Przed commitem obejrzyj listę i diff plików w indeksie i uruchom kontrole z
   `ENVIRONMENT.md`. Nigdy `git add -f` na pliki ignorowane. Przy błędzie
   uwierzytelniania GitHub poproś o ponowne połączenie GitHub w Arena — nigdy
   nie proś o hasła, tokeny ani kody 2FA.

## Zasady projektu

### Co wolno zmieniać w grze

- **Wyłącznie oficjalna ścieżka CLS**: folder `LimbusCompany_Data/Lang/<nazwa>/`
  z plikami JSON o strukturze identycznej z oryginałem, `Font/` i
  `Lang/config.json`. Tak wydawca opisał tłumaczenia fanowskie.
- **Zakaz**: BepInEx, MelonLoader, wstrzykiwania DLL, modyfikacji plików
  wykonywalnych, assetów Unity, pamięci procesu, ruchu sieciowego i podmiany
  plików w czasie działania gry. Project Moon zapowiedział egzekwowanie zakazu
  modyfikacji klienta (2025-09-26). Nie obiecuj bezpieczeństwa konta.
- Instalator ma robić kopię `Lang/config.json`, umieć wszystko cofnąć i nie
  dotykać niczego poza `Lang/`.

### Dane gry i Git

- Repozytorium jest **publiczne**. Pliki gry (także surowe JSON-y z `Localize`),
  ich kopie, archiwa zbieracza, zapisy i zrzuty zostają poza Git — w
  ignorowanym `local/` i na prywatnym Dysku. **Wyciąg tekstu gry i Czytanki
  nie trafiają do Git**, dopóki `config/polityka_danych.json` ma
  `"tekst_gry_w_git": false`. Przestawienie flagi wymaga decyzji właściciela i
  prywatnego repozytorium (`gh repo view --json isPrivate`). Pilnuje tego
  `tools/check_repository.py`, ale ręczny przegląd diffu jest obowiązkowy.
- Do Git trafiają: kod, testy na **wymyślonych** danych, dokumentacja, manifesty
  z liczbami i SHA-256, zwrotki/przekłady Tłumacza (`tlumaczenie/`) oraz
  zagregowane statystyki struktury (nazwy plików i pól, liczby — bez treści).
- Do publicznych logów, PR i CI nie wpisuj tekstu gry, prywatnych ścieżek z
  nazwą użytkownika ani identyfikatorów prywatnych plików z Dysku.
- Tekstu gry nie wysyłaj do zewnętrznych modeli/usług bez zgody właściciela
  (Project Moon zakazuje trenowania AI na swoich materiałach).

### Tłumaczenie

- **Agent nie tłumaczy linii gry.** Jedyne dopuszczalne zmiany tekstu to
  poprawki techniczne (tokeny, znaczniki, limity) zapisane jako jawne korekty
  z uzasadnieniem. Nic po cichu.
- Nie kopiuj cudzych tłumaczeń fanowskich (także istniejącego polskiego).
  Analizować wolno ich **format i narzędzia** ([docs/PRIOR_ART.md](docs/PRIOR_ART.md)).
- Nie zgaduj dopasowań. Błąd tokenu, niezgodność wersji źródła albo nieznany
  klucz zatrzymuje operację — bez częściowego, cichego zapisu.
- Patch ma zawierać 100% tego, co przysłał Tłumacz i co przeszło kontrole;
  odrzucone wpisy są w raporcie z plikiem i numerem linii.

### Praca z plikami u właściciela

- Właściciel nie uruchamia Pythona. Dostaje **ZIP z BAT + PowerShell**
  (zbieracz, instalator), wynik ląduje na Pulpicie i wraca przez Dysk. Wzór i
  zasady: [docs/COLLECTOR.md](docs/COLLECTOR.md). Nie zastępuj tego prośbą o
  ręczne kopiowanie folderów.
- Nie proś o cały katalog gry, dane logowania ani pliki spoza zakresu.
- **Budowanie nie zależy od Dysku ani `local/`** w chwili, gdy wyciąg jest już
  w repozytorium. Do tego czasu narzędzia przyjmują ścieżkę wejścia jawnie.

### Dowody i dokumentacja

- Oddzielaj **fakt / hipotezę / niewiadomą** oraz **test syntetyczny / test na
  kopii plików / test w grze**. Nie zgłaszaj działania w grze bez zgłoszenia
  właściciela.
- Każdą próbę zapisz w `docs/EXPERIMENT_LOG.md` (wejście, wersja/build, SHA-256,
  polecenie, liczby, ograniczenia, następny krok). `docs/STATUS.md` ma zawsze
  wskazywać aktualny stan i następny krok.
- Dostawy na Dysk: rozmiar, SHA-256, pobranie z powrotem i porównanie bajtów.
- Wnioski, które przydadzą się kolejnym sesjom, dopisz do `LESSONS.md`.
- Nie uruchamiaj automatycznej publikacji wydań, dopóki proces wydania nie
  zostanie zaprojektowany i sprawdzony ([docs/ROADMAP.md](docs/ROADMAP.md)).
