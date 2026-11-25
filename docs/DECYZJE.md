# Decyzje

Każda decyzja ma numer, datę, uzasadnienie i ewentualne warunki rewizji.
Decyzji podjętych **nie** przedstawiamy właścicielowi ponownie, chyba że
zmieniły się fakty (wtedy nowy wpis odwołuje stary).

## Podjęte

### D-01 · 2026-11-25 · Pliki gry dostarcza zbieracz, nie ręczny upload katalogu

Pliki tekstowe Limbus Company są małe (spodziewane ~35–40 MB dla jednego
języka), więc dało się je wrzucić ręcznie na Dysk, jak w SRW OE. Wybrano jednak
zbieracz (wzorzec WWM), bo:

- właściciel nie musi szukać folderu gry ani wiedzieć, które pliki są potrzebne;
- zbieracz odczytuje **build Steam** (`appmanifest_1973530.acf`) — bez tego nie
  da się powiązać tekstu z wersją gry ani wykryć aktualizacji;
- kopie są weryfikowane SHA-256, a inwentarz (`INWENTARZ.jsonl`) pokazuje, co
  jeszcze jest w instalacji, bez przesyłania tego;
- ten sam `URUCHOM.bat` służy co tydzień po aktualizacji gry (nowy ZIP, stary
  zostaje).

Ręczny upload folderu `Localize` na Dysk pozostaje **awaryjnym wyjściem**, gdy
zbieracz nie działa. Wtedy agent zapisuje w `EXPERIMENT_LOG.md`, że brak buildu
i hashy źródłowych.

### D-02 · 2026-11-25 · Wyciąg tekstów jest wersjonowany w `index/`

Jak w WWM i SRW: teksty potrzebne do budowania pakietów, paczki `Lang/` i
Czytanek są w Git (znormalizowane, z manifestem buildu). Pozwala to budować bez
dostępu do Dysku i robić diffy między wersjami gry. Szczegóły i granice:
[DATA_POLICY.md](DATA_POLICY.md).

### D-03 · 2026-11-25 · ~~Przekład z angielskiego~~ — ZASTĄPIONA przez D-05

Angielski jest językiem, z którego pracuje tłumacz. Oryginał koreański (`kr`) i
japoński (`jp`) zbieramy, bo pomagają rozstrzygać niejasności (płeć, ton, gry
słów); Pakiety mogą je dołączać jako informację, nie jako tekst do przekładu.
Rewizja, jeśli tłumacz zna koreański i woli pracować z oryginału.

### D-04 · 2026-11-25 · Tylko oficjalny Custom Language

Żadnych modyfikacji bundli Unity, pliku wykonywalnego ani loaderów modów.
Uzasadnienie: oficjalne wsparcie od wersji 1.73.0, brak ryzyka bana zgłaszany
przez społeczność, odinstalowanie przez usunięcie folderu. Teksty, których ten
mechanizm nie obejmuje (np. wpisane w grafiki), są poza zakresem i trafiają do
listy ograniczeń. [FEASIBILITY.md](FEASIBILITY.md).

### D-05 · 2026-11-25 · Przekład z koreańskiego; angielski jako odniesienie

Kierunek wskazany przez właściciela: Limbus Company jest napisane po
koreańsku, a angielski to już przekład. Tłumaczenie z angielskiego byłoby
„pochodną pochodnej”: przenosiłoby jego skróty, wybory i błędy. Dlatego:

- **Źródłem jest `kr`.** To z niego tłumacz robi przekład. Import sprawdza, że
  linia `KR:` w zwrotce się nie zmieniła; klucz przekładu to SHA-256 tekstu
  koreańskiego.
- **`en` to odniesienie (benchmark):** widoczne przy każdym elemencie. Pomaga
  przy ustalonej terminologii znanej graczom (słowa kluczowe, nazwy statusów),
  przy szacowaniu długości tekstu w interfejsie (polski jest bliższy długością
  angielskiemu niż zwięzłemu koreańskiemu) i jako druga opinia przy
  niejasnościach.
- **`jp`:** opcjonalnie do wglądu (również przekład z koreańskiego).
- **Tokeny i znaczniki** bierzemy z `kr` i porównujemy z `en`; różnice trafiają
  do raportu (mogą oznaczać różnice w lokalizacji, a nie błąd).
- **Słowniczek** ma kolumny KR | oficjalne EN | PL. Nazwy własne
  (Sinnerzy, Miasto) w transkrypcji ustala właściciel z tłumaczem;
  domyślnie oficjalna pisownia angielska, bo tę znają gracze.
- Paczka `Lang/` i fallback dla nieprzetłumaczonych tekstów: bez zmian (tekst
  angielski, który gracz w Polsce zrozumie), z wpisem w raporcie pokrycia.

**Potwierdzone 2026-11-25:** tłumacz czyta po koreańsku (O-05 = tak). Pakiet
fabularny ma koreański w linii elementu i `EN:` jako odniesienie
([PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md)).

### D-06 · 2026-11-25 · Lustra i pliki gry — swobodnie w piaskownicy, nigdy w repozytorium

Odpowiedź właściciela na O-07: wolno pracować na plikach gry i publicznych
lustrach (TW `story-data`, OpenLethe `StaticData`, także binaria), ale **tylko
poza repozytorium** (`local/`, `/tmp`). W piaskownicy można je dowolnie
analizować i przetwarzać.

- Do Git trafiają wyłącznie **narzędzia, testy na danych wymyślonych i
  pochodne identyfikatory/liczby** (np. `wiedza/indeks_fabuly.json`: numery
  rozdziałów, węzłów, nazwy plików scen) — bez tekstu gry i bez kopii tabel.
- OpenLethe nie ma licencji: nie kopiujemy jego plików do repozytorium; służy
  jako lokalne źródło struktury (Teatr Opowieści, etapy, walki, statystyki).
- Czytanki i pakiety zbudowane z luster są próbkami do oceny układu; wersje
  „oficjalne” (pakiety dla tłumacza, `index/`) budujemy z paczki zbieracza
  właściciela (znany build), gdy przyjdzie. Narzędzia czytają oba źródła tak
  samo.

### D-07 · 2026-11-25 · Pakiet i Czytanki w układzie SRW, z maksimum kontekstu

Polecenie właściciela:

- **Pakiet dla tłumacza** wzorowany na SRW Y: README + `sceny.zip`, element
  `N. [Dialog - mówca] źródło` / `limit:` / `tokeny:` / `EN:` / `PL:`, nagłówek
  sceny z kontekstem (rozdział, etap, miejsce, moment walki, sąsiednie sceny,
  uczestnicy), spisy rozdziałów i scen, mówcy/miejsca tłumaczone raz.
- **Czytanka** w „ludzkim” układzie: dokładna chronologia, nazwy Canto i etapów
  we właściwych miejscach, mówcy jak w SRW (`**Imię:** tekst`), bez
  identyfikatorów w tekście.
- **Plik ID** (profile Identity): co naprawdę jest w danej Identity —
  statystyki, umiejętności, pasywki, opisy i kwestie w czytelnej formie.

Szczegóły: [PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md), [CZYTANKI.md](CZYTANKI.md).

## Otwarte (decyduje właściciel; agent przygotowuje opcje)

| Nr | Pytanie | Kiedy potrzebne | Uwagi |
|---|---|---|---|
| O-01 | Nazwa języka w `config.json` / folderu (`Polski`? `PL`?) | przed pierwszą paczką testową | nazwa widoczna w grze; inna niż w istniejącej fanowskiej paczce `Polish`, by mogły współistnieć |
| O-02 | Kolejność prac: interfejs najpierw czy fabuła (Prologue + Canto I) najpierw | przed pierwszym pakietem | sugestia agenta: mały pakiet UI (test drogi end-to-end), potem fabuła |
| O-03 | Czcionki: czy domyślna czcionka gry wystarcza dla polskich znaków | przed testem w grze | właściciel: prawdopodobnie tak — **najpierw test bez własnych czcionek**; zewnętrzne (OFL) tylko awaryjnie; patrz [LANG_FORMAT.md](LANG_FORMAT.md) |
| O-04 | Akceptacja układu Czytanek (próbki w Markdown; ewentualnie HTML/DOCX) | po lekturze próbek | układ wg D-07; po akceptacji zamrożony |
| ~~O-05~~ | ~~Czy tłumacz czyta po koreańsku~~ | — | **zamknięte 2026-11-25: tak** → D-05 potwierdzona |
| O-06 | Czy repozytorium ma pozostać publiczne, skoro `index/` zawiera tekst gry | przed pierwszym commitem `index/` | patrz [DATA_POLICY.md](DATA_POLICY.md) |
| ~~O-07~~ | ~~Czy wolno pracować na publicznych lustrach~~ | — | **zamknięte 2026-11-25: tak, poza repozytorium** → D-06 |
