# Polityka danych

Plik maszynowy: [`config/polityka_danych.json`](../config/polityka_danych.json)
(`lc-polityka-danych-v1`). Egzekwuje go `tools/check_repository.py` w CI.

## Stan obecny (2026-11-25)

- Repozytorium jest **publiczne** i nie ma licencji.
- `tekst_gry_w_git: false` — wyciąg tekstu gry (`wyciag/`) i Czytanki
  (`czytanki/`) **nie mogą** być w indeksie Git. Kontrola odrzuca też surowe
  pliki lokalizacji (`KR_*.json`, `EN_*.json`, `JP_*.json`), katalogi
  `LimbusCompany_Data/`, `Resources_moved/`, `Localize/`, binaria Unity, archiwa
  i fonty poza `assets/fonts/`.

## Uzasadnienie

- Teksty gry są własnością Project Moon. Publiczne repo z pełnym tekstem
  koreańskim/angielskim to „udostępnianie zasobów gry” — Project Moon wymienił
  je wśród naruszeń w komunikacie o zasadach twórczości fanowskiej (2025-09-26),
  obok modyfikacji klienta i trenowania AI.
- Paczka CLS z polskim tekstem to praktyka akceptowana przez wydawcę (sam
  zapowiedział i opisał CLS dla tłumaczeń fanowskich). Polskie przekłady
  Tłumacza są pracą zależną — publikujemy je w formie patcha, tak jak inne
  społeczności (PT-BR, ES, FR, RU, zh-CN).
- Zasady fanowskie Project Moon są w trakcie aktualizacji; obowiązują stare.
  Przy każdej zmianie zasad wydawcy zaktualizuj ten plik i `PRIOR_ART.md`.

## Co gdzie leży

| Dane | Miejsce |
|---|---|
| Kod, testy (dane **wymyślone**), dokumentacja, polityka | Git |
| Statystyki struktury: liczby, nazwy plików i pól, SHA-256, `buildid` | Git (po przeglądzie) |
| Przekład Tłumacza (`tlumaczenie/`), glosariusz, korekty | Git |
| Zwroty zbieracza `LC_DANE_*.zip` | Dysk (folder „Limbus Company”) + `local/zwroty/` |
| Wyciąg tekstu gry, Czytanki | `local/` + Dysk (przy `tekst_gry_w_git: false`) |
| Pakiety dla Tłumacza (zawierają źródło) | Dysk; w `paczki/` tylko `paczka.json` (manifest bez treści) |
| Zbudowane ZIP-y (zbieracz, patch, instalator) | `dist/` (ignorowane) → Dysk / Releases po decyzji |

## Zmiana polityki

Przestawienie na `tekst_gry_w_git: true` wymaga:

1. decyzji właściciela (zapisanej w [CEL.md](CEL.md));
2. repozytorium prywatnego (`gh repo view --json isPrivate` → `true`) i
   ustawienia `"repozytorium_publiczne": false` w polityce;
3. osobnego commita zmieniającego tylko politykę, przed dodaniem tekstu.

Kontrola odrzuci flagę `true` przy `repozytorium_publiczne: true`.

## Prywatność właściciela

- Zbieracz zapisuje ścieżki **względne** od `LimbusCompany_Data` i tylko nazwę
  folderu gry; nie zbiera zapisów, logów, poświadczeń.
- W publicznych logach, PR i CI nie podawaj ścieżek z nazwą użytkownika ani ID
  prywatnych plików na Dysku.

## AI

- Nie wysyłaj tekstu gry do zewnętrznych modeli/usług bez zgody właściciela.
- Nie trenuj ani nie dostrajaj modeli na tekście gry.
- Czy Tłumacz może używać AI — decyduje właściciel ([CEL.md](CEL.md), pytanie 4).
