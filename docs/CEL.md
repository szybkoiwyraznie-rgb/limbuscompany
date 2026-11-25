# Cel projektu i decyzje

## Cel

1. **Polskie tłumaczenie Limbus Company** (nieoficjalne, fanowskie) przez
   oficjalny mechanizm gry *Custom Language Support* (CLS): folder
   `LimbusCompany_Data/Lang/<nazwa>/` + `Lang/config.json`. Bez modyfikacji
   klienta. Docelowo cała gra (fabuła, UI, umiejętności, opisy, dialogi bitewne);
   kolejność wynika z [ROADMAP.md](ROADMAP.md).
2. **Czytanki** — materiały do czytania fabuły i lore dla właściciela jako
   gracza: fabuła w kolejności, z mówcami i miejscami, z indeksem postaci,
   rozdziałów i pojęć. Najpierw ze źródła (EN/KR), potem z polskim przekładem
   ([CZYTANKI.md](CZYTANKI.md)).

## Podział ról

| Kto | Co robi |
|---|---|
| Właściciel | Uruchamia zbieracz/instalator (BAT), wgrywa ZIP-y na Dysk, testuje w grze, podejmuje decyzje. |
| Agenci Arena | Narzędzia, zbieracz, wyciąg, pakiety, import, kontrole, patch CLS, instalator, Czytanki, dokumentacja. |
| Tłumacz (zewnętrzny, wyspecjalizowany) | Tłumaczy na podstawie Pakietu dla Tłumacza i odsyła zwrotkę. **Jedyne źródło polskiego tekstu.** |

## Decyzje podjęte (nie pytaj o nie ponownie)

- **2026-11-25 — Zbieracz zamiast ręcznego wgrania folderu gry.** Pliki są małe
  (rzędu setek MB), więc technicznie mogłyby iść na Dysk w całości jak w SRW OE,
  ale wybrano ZBIERACZ (BAT + PowerShell → ZIP na Pulpicie → Dysk), bo:
  zbiera dokładnie `Localize` (kr/en/jp) + `Lang/config.json` + spis nazw,
  zapisuje `buildid` ze Steam i SHA-256 każdego pliku, ma tryb **aktualizacji**
  (gra aktualizuje się co tydzień — wysyła tylko zmienione pliki i listę
  usuniętych), nie wymaga od właściciela szukania folderów i jest testowany w
  CI na Windows. Szczegóły: [COLLECTOR.md](COLLECTOR.md).
- **2026-11-25 — Tylko oficjalny CLS.** Wynik: `Lang/<pl>/` + `Font/` +
  `config.json`. Żadnego BepInEx/MelonLoader ani patchowania assetów.
- **2026-11-25 — Repozytorium publiczne jak WWM/SRW:** żadnych binariów ani
  surowych plików gry, ale wyciągnięte teksty, indeksy, Czytanki, pakiety i
  tłumaczenia są w repozytorium ([DATA_POLICY.md](DATA_POLICY.md)).
- **2026-11-25 — Język źródłowy: koreański (oryginał).** Tłumacz przekłada z
  KR. EN (oficjalny przekład wydawcy) i JP są w wyciągu i w pakiecie jako
  odniesienie, ale tokeny, klucze i kompletność sprawdzamy względem KR.
  Patch CLS budujemy na bazie plików `kr` (nieprzetłumaczone pozycje zostają
  po koreańsku, chyba że właściciel zdecyduje o EN jako zapasie — zob. pytania).
- **2026-11-25 — Istniejące polskie tłumaczenie fanowskie ignorujemy.** Projekt
  jest niezależny; bez kontaktu, bez korzystania z jego tekstu.
- **Konwencje z WWM/SRW:** sesyjna gałąź + wczesny PR, STATUS/EXPERIMENT_LOG/
  LESSONS, pakiety dla Tłumacza z kluczami SHA-256 i tokenami, import tylko
  `klucz`/`PL`, patch = 100% zwrotki, korekty agentów jawne.

## Otwarte pytania do właściciela

Stan na 2026-11-25. Po odpowiedzi przenieś punkt wyżej z datą.

1. **Zapas dla nieprzetłumaczonych pozycji:** gdy fragment nie ma jeszcze
   polskiego przekładu, patch ma pokazywać tekst **angielski** (czytelny dla
   gracza) czy **koreański** (oryginał)? Propozycja: EN — można grać, zanim
   całość będzie przetłumaczona.
2. **Wydawanie:** tylko dla siebie, czy publicznie (Steam Guide / GitHub
   Releases)? Wpływa na instalator, nazwę folderu `Lang/` i kredyty.
3. **Font:** CLS pozwala na jeden font tytułów i jeden treści (`Font/Title`,
   `Font/Context`). Domyślny font gry może nie mieć polskich znaków — trzeba
   wybrać font z licencją pozwalającą na redystrybucję (np. OFL). Do ustalenia
   po teście w grze.
