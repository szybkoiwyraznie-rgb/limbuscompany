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

**Warunek:** tłumacz czyta po koreańsku (O-05). Jeśli nie, wracamy do
schematu z D-03 (źródło EN, KR do wglądu), a właściciel decyduje, czy szukać
tłumacza KR→PL. Narzędzia piszemy niezależnie od języka źródłowego (parametr
`--zrodlo kr|en`), więc zmiana nie wymaga przepisywania kodu.

## Otwarte (decyduje właściciel; agent przygotowuje opcje)

| Nr | Pytanie | Kiedy potrzebne | Uwagi |
|---|---|---|---|
| O-01 | Nazwa języka w `config.json` / folderu (`Polski`? `PL`?) | przed pierwszą paczką testową | nazwa widoczna w grze; inna niż w istniejącej fanowskiej paczce `Polish`, by mogły współistnieć |
| O-02 | Kolejność prac: interfejs najpierw czy fabuła (Prologue + Canto I) najpierw | przed pierwszym pakietem | sugestia agenta: mały pakiet UI (test drogi end-to-end), potem fabuła |
| O-03 | Czcionki: które wolne czcionki z polskimi znakami (Context/Title) | przed testem w grze | licencja OFL; patrz [LANG_FORMAT.md](LANG_FORMAT.md) |
| O-04 | Format Czytanek (HTML, EPUB, DOCX, Markdown) i zakres pierwszej | przed pierwszą Czytanką | w SRW i WWM sprawdził się HTML + DOCX |
| O-05 | Czy tłumacz czyta po koreańsku — **warunek D-05** | **przed pierwszym pakietem** | jeśli nie: źródło EN (D-03) albo szukanie tłumacza KR→PL |
| O-06 | Czy repozytorium ma pozostać publiczne, skoro `index/` zawiera tekst gry | przed pierwszym commitem `index/` | patrz [DATA_POLICY.md](DATA_POLICY.md) |
