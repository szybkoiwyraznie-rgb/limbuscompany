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
  zbiera dokładnie `Localize` (kr/en/jp) + `Lang/config.json` + spis nazw
  (od wersji 1.1.0 także dane pomocnicze `StaticData` i `Story` dla Czytanek),
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
  Klucze i hashe źródła liczone są na KR.
- **2026-11-25 — Zapas EN.** Pozycje bez (aktualnego) polskiego przekładu
  pokazują w grze tekst **angielski**. Patch budujemy na bazie plików `en` z
  podmienionymi polami przetłumaczonymi; zawiera komplet plików
  ([METODA.md](METODA.md), punkt 5).
- **2026-11-25 — Bez wydań.** Nie robimy GitHub Releases ani publikacji.
  Pakiety patcha (ZIP + sumy SHA-256) agenci wgrywają na Dysk do folderu
  „Limbus Company”; właściciel instaluje je u siebie.
- **2026-11-25 — Korzystamy z dorobku innych projektów tłumaczeń Limbus.**
  Przejmujemy ich metody i indeksy (klucze, biała lista pól, tokeny, zapas EN,
  kontrole) zamiast wymyślać od nowa; kod piszemy od nowa, tekstów przekładów
  nie kopiujemy ([METODA.md](METODA.md), [PRIOR_ART.md](PRIOR_ART.md)).
- **2026-11-25 — Font: najpierw domyślny font gry.** Limbus to gra na Windows;
  w WWM i SRW Y domyślne fonty miały polskie znaki, więc i tu jest na to duża
  szansa (zdanie właściciela). Pilot testuje polskie znaki bez własnego fontu
  (`titleFont`/`contextFont` puste w `config.json`). Własny font z licencją na
  redystrybucję tylko wtedy, gdy test pokaże braki.
- **2026-11-25 — Pakiet dla Tłumacza wzorowany na SRW** (pakiet SRW Y v8 / OE):
  `README.md` + `sceny.zip` + `widoki.zip`, element `N. [etykieta] KR` /
  `tokeny:` / `EN:` / `PL:`, nagłówki scen z maksimum kontekstu (mówcy,
  miejsca, Canto/etap, chronologia), spisy rozdziałów i scen
  ([PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md)).
- **2026-11-25 — Czytanki „ludzkie”:** dialogi w dokładnej chronologii, nazwy
  Canto i etapów we właściwych miejscach, `**Imię:** tekst` jak w SRW, karty ID
  pokazujące to, co jest w ID (statystyki, umiejętności, pasywki) w ludzkiej
  formie ([CZYTANKI.md](CZYTANKI.md)).
- **2026-11-25 — Istniejące polskie tłumaczenie fanowskie ignorujemy.** Projekt
  jest niezależny; bez kontaktu, bez korzystania z jego tekstu.
- **Konwencje z WWM/SRW:** sesyjna gałąź + wczesny PR, STATUS/EXPERIMENT_LOG/
  LESSONS, pakiety dla Tłumacza z tokenami i manifestem importu (klucze poza
  widokiem Tłumacza, jak w SRW), import tylko wartości `PL:`, patch = 100%
  zwrotki, korekty agentów jawne.

## Otwarte pytania do właściciela

Stan na 2026-11-25. Po odpowiedzi przenieś punkt wyżej z datą.

Brak otwartych pytań. Do potwierdzenia testem w grze (nie pytaniem): polskie
znaki w domyślnym foncie ([METODA.md](METODA.md), punkt 9).
