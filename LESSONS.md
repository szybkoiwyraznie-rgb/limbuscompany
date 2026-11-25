# Wnioski (LESSONS)

Krótkie, sprawdzone wnioski dla kolejnych sesji. Dopisuj na górze sekcji.
Wnioski przeniesione z WWM/SRW są oznaczone źródłem.

## Proces

- **PR od razu, push każdego fragmentu.** Snapshot sandboksa i Dysk nie
  zastępują pusha. (WWM, SRW)
- **Nie zgłaszaj działania w grze bez zgłoszenia właściciela.** Testy
  syntetyczne i CI to dowody innego rodzaju — nazywaj je wprost. (WWM)
- **Nie pytaj o rzeczy rozstrzygnięte w `docs/CEL.md`** ani o tematy, które
  właściciel wyłączył z projektu (np. AI — „nie jest tematem tego projektu”). Otwarte pytania zbieraj
  w jednym miejscu i zadawaj razem. (SRW)
- **Dostawa na Dysk = rozmiar + SHA-256 + pobranie z powrotem.** Dysk raz
  zablokował ZIP zbieracza; plan awaryjny: archiwum repozytorium z GitHub. (WWM)
- **Agent nie tłumaczy**; korekty techniczne zawsze jawne. Patch = 100%
  zaakceptowanej zwrotki. (SRW)

## Windows / zbieracz

- **PowerShell 5.1 czyta `.ps1` bez BOM jako ANSI** — `zbierz.ps1` trzyma się
  ASCII w kodzie i ma UTF-8 z BOM + CRLF; BAT — czyste ASCII + CRLF. Builder to
  sprawdza i odmawia budowania. (WWM)
- **Narzędzia edycji w sandboksie zapisują LF bez BOM.** Po każdej edycji
  `.ps1`/`.bat` przekonwertuj (Python: `utf-8-sig`, CRLF) i uruchom testy.
- **`.gitattributes`: `*.bat`/`*.ps1` jako `-text`**, żeby Git nie zmieniał bajtów.
- **Wartość zwracana z funkcji PowerShell to cały potok.** Każde
  `.Add()`/`New-Item` itp. bez `[void]` dokłada wartość; dlatego kod wyjścia
  bierzemy jako ostatni element: `$result = @(Main); exit ([int] $result[-1])`.
- **PowerShell 5.1: nie wstawiaj potoków ani `@(…)` do zagnieżdżonych literałów
  `[ordered]@{ … }`** — kompilator zgłasza „Argument types do not match”.
  Najpierw zmienna, potem `$dict['klucz'] = $zmienna`.
- **Komunikat `BLAD:` ma numer linii** (`$_.InvocationInfo.ScriptLineNumber`) —
  bez tego błędy z CI Windows są trudne do zlokalizowania.
- **pwsh nie da się zainstalować w sandboksie** (blokada pobrań z GitHub
  release assets). PowerShell testujemy tylko w CI na `windows-latest`.

## Limbus Company

- **Tylko CLS** (`Lang/<nazwa>/`), bez modyfikacji klienta — Project Moon
  zapowiedział egzekwowanie zakazu modyfikacji (2025-09-26).
- **`model` w StoryData to identyfikator zasobu**, nie imię do tłumaczenia;
  imiona są w `ScenarioModelCodes-AutoCreated.json`.
- **`id` w plikach nie jest unikalne** (np. `-1`) — klucze z numerem wystąpienia.
- **Gra aktualizuje się co tydzień** — klucz jednostki zawiera hash źródła;
  zbieracz ma tryb aktualizacji.

## Sandbox / narzędzia

- **Lokalna historia Git potrafi wrócić do commita bazowego** między turami
  (pliki zostają). Przed pushem: `git fetch` i `git diff --stat origin/<gałąź> HEAD`;
  jeśli różnica to tylko nowa praca — `git reset --soft origin/<gałąź>` i commit.
  Nigdy `--force`.
- Klon bez blobów (`--filter=blob:none`) potrafi zawiesić `git ls-tree`/`show`
  na leniwym pobieraniu: `GIT_NO_LAZY_FETCH=1` i `timeout`.
- `gh repo view --json isPrivate` (pole `visibility` nie jest wspierane).
