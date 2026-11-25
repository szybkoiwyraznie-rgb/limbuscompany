# Format Custom Language Support (CLS)

Oznaczenia: **[F]** fakt z oficjalnego źródła, **[P]** potwierdzone w publicznych
paczkach fanowskich (format, nie treść), **[H]** hipoteza do sprawdzenia na
danych właściciela, **[?]** niewiadoma. Aktualizuj po każdym rozpoznaniu.

## Źródła

- Steam, „Custom Language Translation Support”, 2025-03-31 (wersja 1.73.0):
  <https://store.steampowered.com/news/app/1973530/view/533220039674824263>
- Steam, notka wersji 1.74.0 (2025-04-18): foldery fontów.
- Publiczne paczki CLS (do analizy struktury): FR
  (Eden-Office/LimbusCompanyBusFR), PT-BR, ES, RU, zh-CN — [PRIOR_ART.md](PRIOR_ART.md).

## Źródło tekstów w grze

- **[F]** `LimbusCompany_Data/Assets/Resources_moved/Localize/` z podfolderami
  `kr`, `en`, `jp`.
- **[F]** Nazwy plików mają prefiks języka, np. `KR_MainUIText.json`,
  `EN_MainUIText.json`.
- **[P]** Pliki to JSON UTF-8 (czasem z BOM); większość ma układ
  `{"dataList": [ {...}, ... ]}`.

## Paczka tłumaczenia

- **[F]** Folder `LimbusCompany_Data/Lang/<nazwa>/` z **tą samą strukturą
  katalogów** co folder języka w `Localize`, nazwy **bez prefiksu**
  (`KR_MainUIText.json` → `MainUIText.json`).
- **[F]** `LimbusCompany_Data/Lang/config.json` wybiera aktywny folder.
- **[F]** W grze: ustawienia → „Select Custom Language” → restart. Przy testach
  zalecane „Clear all caches” po zmianie plików.
- **[F]** (1.74.0) Fonty: `Lang/<nazwa>/Font/Title/` i `Lang/<nazwa>/Font/Context/`.
- **[P]** `config.json` (paczka FR):
  `{"lang": "<nazwa>", "titleFont": "", "contextFont": "", "samplingPointSize": …, "padding": …}`
  — dokładne znaczenie i wymagalność pól **[H]**.
- **[P]** Brakujący plik w `Lang/<nazwa>/` → gra używa języka bazowego **[H]**
  (do potwierdzenia testem: paczka z jednym plikiem UI).
- **[P]** Ograniczenia (FAQ PT-BR): jeden font tytułów i jeden treści dla
  całej gry; część tekstów jest na sprite'ach/obrazkach (nieprzetłumaczalna
  przez CLS); tylko PC (na telefonie nie ruszać plików — ryzyko konta).

## Struktura (paczka FR, ~2430 plików — stan z 2025/2026)

| Katalog | Plików (ok.) | Zawartość **[P]** |
|---|---:|---|
| korzeń | ~977 | UI, umiejętności, osobowości (Identity), E.G.O, przedmioty, statusy, słowniki |
| `StoryData/` | ~999 | fabuła: sceny (np. `S101B.json`) |
| `PersonalityVoiceDlg/` | ~196 | kwestie głosowe osobowości |
| `RPGSystem/` | ~157 | tryby/wydarzenia w stylu RPG |
| `BattleAnnouncerDlg/` | ~64 | komentator bitwy |
| `BgmLyrics/` | ~17 | teksty piosenek |
| `EGOVoiceDig/` | ~14 | kwestie E.G.O (literówka w nazwie jest oryginalna) |
| `Font/Title`, `Font/Context` | — | fonty paczki |

Liczby dla aktualnej wersji gry ustali `tools/rozpoznanie_localize.py`.

## Schematy (format, nie treść)

- **StoryData** **[P]**: `{"dataList": [{"id": <int>, "content": "...",
  "model": "...", "teller": "...", "title": "...", "place": "..."}]}` — pola
  poza `id`/`content` występują opcjonalnie.
  - `model` to **identyfikator zasobu** (portret/model postaci), nie tekst do
    tłumaczenia; oficjalny przekład chiński zostawia go po koreańsku **[P]**.
  - Wyświetlane imiona mówców są w `ScenarioModelCodes-AutoCreated.json`
    (tabela kod → imię/alias) **[P]**; `teller`/`title` w scenie **[H]**: nadpisania.
  - `id` mogą się powtarzać (np. `-1` dla wpisów dźwiękowych z pustym
    `content`) **[P]** → klucz jednostki musi uwzględniać numer wystąpienia
    (`plik#id~n`). Rozpoznanie raportuje `duplikaty_id`.
- **Umiejętności** (`Skills_*.json`) **[P]**: `dataList[{id, levelList[{level,
  name, desc, coinlist[{coindescs[{desc}]}]}]}]`.
- **Dialogi bitewne** (`BattleSpeechBubbleDlg*.json`), `PersonalityVoiceDlg/`
  **[P]**: osobne pliki z kwestiami.
- **Znaczniki w tekście** **[P/H]**: Unity rich text (`<color=#…>`, `<b>`,
  `<size=…>`, `<sprite name=…>`), linki do słów kluczowych, `\n`. Uwaga: `<…>`
  bywa też cudzysłowem w dialogach — tagi rozpoznajemy po zamkniętej liście
  nazw (`tools/lc_tokeny.py`, [METODA.md](METODA.md), punkt 4); rozpoznanie
  raportuje kandydatów na nowe nazwy.

## Wnioski dla narzędzi

1. Wyciąg działa na **nazwach logicznych** (bez prefiksu) i wiąże pliki
   kr/en/jp po tej nazwie (`tools/lc_localize.py`).
2. Patch odtwarza **pełny JSON** pliku bazowego (**EN** — język zapasowy,
   [CEL.md](CEL.md)) z podmienionymi tylko polami
   tekstowymi z białej listy (wzór: `translatable_keys.json` z
   Noplch0/limbus-ai-localization); pola identyfikatorów (`id`, `model`, klucze
   techniczne) pozostają bez zmian.
3. Biała lista pól powstaje z rozpoznania (`pola` w raporcie) i jest wersjonowana
   w Git (`config/pola_tlumaczone.json` — do zrobienia).
4. Klucz jednostki: `<zakres>/<plik_logiczny>#<id>[~n]#<ścieżka_pola>` (schemat
   AutoLocalization) + hash źródła KR — zmiana źródła po aktualizacji gry
   unieważnia przekład ([METODA.md](METODA.md), punkt 2).

## Niewiadome do sprawdzenia na danych właściciela

- [?] Aktualna liczba i układ plików, rozmiar `Localize` (spodziewane: setki MB).
- [?] Czy wszystkie pliki mają odpowiedniki we wszystkich trzech językach i czy
  `id` się zgadzają (raport `parzystosc`).
- [?] Pliki spoza `dataList`; inne kodowania; pliki nie-JSON.
- [?] Czy `Lang/config.json` istnieje domyślnie i jaką ma treść w czystej grze.
- [?] Zachowanie gry przy brakującym pliku/polu w paczce (test w grze).
- [?] Polskie znaki w domyślnym foncie (test w grze z jednym ekranem UI).
