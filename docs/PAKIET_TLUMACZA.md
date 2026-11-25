# Pakiet dla Tłumacza (plan: `lc-paczka-v1`)

Format przejęty z WWM (`wwm-paczka-v1`) i SRW, dopasowany do JSON-ów CLS.
**Status: projekt.** Szczegóły pól ustalimy po rozpoznaniu danych.
**Źródło: koreański** (decyzja 2026-11-25, [CEL.md](CEL.md)); EN obok jako
odniesienie.

## Zawartość ZIP-a

```
LC_PAKIET_<nazwa>_<data>.zip
├── README.txt          instrukcja dla Tłumacza (PL), zasady, glosariusz-skrót
├── sceny/              fabuła: jeden plik .txt na rozdział/scenę, w kolejności gry
├── teksty/             UI, umiejętności, statusy… pogrupowane tematycznie
├── glosariusz.txt      ustalone nazwy własne (z tlumaczenie/glosariusz.*)
└── paczka.json         manifest: wersja formatu, buildid, lista jednostek (klucz,
                        plik, hash źródła KR), liczby

Kopia każdego wysłanego pakietu (rozpakowana) zostaje w repozytorium w
paczki/<nazwa>/, ZIP do przekazania Tłumaczowi — na Dysku.
```

Pakiet jest deterministyczny (te same dane → te same bajty), kodowanie UTF-8
z BOM i CRLF (Notatnik), rozmiar części ~2–3 MB.

## Element do przetłumaczenia

```
17. [Kwestia — Dante] StoryData/S101B.json
klucz: 3f9a0c51d2e8b7a4
tokeny: <color=#f8c200> </color> \n
KR: (źródło — oryginał)
EN: (oficjalny przekład angielski, tylko do wglądu)
PL:
```

- `klucz` — 16 znaków hex z SHA-256 (plik logiczny + ścieżka/id + numer
  wystąpienia + hash źródła KR). Tłumacz go nie zmienia.
- `tokeny` — znaczniki i zmienne, które muszą pojawić się w PL bez zmian
  (kolejność może się zmienić, jeśli gramatyka wymaga; liczba — nie).
- Jedna pozycja na unikalny tekst w obrębie pakietu; powtórzenia są
  wymienione jako „także w: …”.
- Znaki specjalne: `\n` (nowa linia w grze), `\t`, `\\`.
- Kontekst sceny (mówca, miejsce, poprzednia kwestia) w nagłówku i w kolejności
  pliku — Tłumacz czyta scenę jak tekst, a nie listę oderwanych linii.

## Zwrotka i import

- Tłumacz odsyła te same pliki z wypełnionym `PL:` (może być w częściach).
- Import czyta **tylko** `klucz` i `PL`. Odrzuca: nieznany klucz, klucz
  nieaktualny (zmienione źródło), niezgodne tokeny, sprzeczne wersje tego
  samego klucza. Raport: plik + numer linii, bez cytowania treści.
- Wynik: `tlumaczenie/<obszar>.jsonl` (`{"klucz", "pl", "zrodlo_hash", "pakiet"}`)
  w Git. Korekty techniczne agentów: `tlumaczenie/KOREKTY.json`.
- Patch zawiera 100% zaakceptowanych pozycji; pozostałe zostają w języku
  zapasowym (EN albo KR — [CEL.md](CEL.md), pytanie 1).

## Kolejność pakietów (propozycja)

1. **Pilot**: wybrane `MainUIText` + jeden krótki fragment fabuły — test
   formatu, fontu i polskich znaków w grze.
2. UI i system (menu, statusy, słowa kluczowe) + glosariusz nazw.
3. Fabuła w kolejności Cantów (prolog, Canto I…), równolegle Czytanki PL.
4. Osobowości (Identity) i E.G.O: umiejętności, pasywki, opisy, kwestie.
5. Wydarzenia, Mirror Dungeon / Refraction Railway, dialogi bitewne, reszta.
