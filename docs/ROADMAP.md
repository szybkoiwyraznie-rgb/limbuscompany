# Plan

Etapy są sekwencyjne tam, gdzie wymagają danych; w nawiasie — kto blokuje.

| Etap | Cel | Wynik | Blokuje |
|---|---|---|---|
| **0. Fundamenty** ✅ | repo, zasady, CI, zbieracz, walidator, inspekcja | ten PR | — |
| **1. Rozpoznanie** | pierwsza paczka ze zbieracza, fakty o formacie | [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md) z liczbami, E-003 | właściciel (uruchomienie zbieracza) |
| **2. Wyciąg** | `tools/extract.py` → `index/` z manifestem; test spójności | `index/`, `docs/INDEX_FORMAT.md` | O-06 |
| **3. Droga end-to-end** | paczka testowa (1 tekst + polskie znaki), wybór czcionek | test w grze „Clear all caches” | właściciel (test), O-01, O-03 |
| **4. Pakiet 000 (UI)** | `bundle.py`, `import_zwrotki.py`, `build_lang.py` na małym zakresie | pierwsza paczka `Lang/` z prawdziwym przekładem | tłumacz |
| **5. Czytanki EN** | `tools/czytanki.py`: fabuła w kolejności, profile Identity | pierwsza Czytanka | O-04 |
| **6. Aktualizacje** | `audit_update.py`, pakiety uzupełniające | obieg tygodniowy | — |
| **7. Skala** | słowa kluczowe, fabuła Canto po Canto, Identity/E.G.O | kolejne pakiety | tłumacz |
| **8. Wydawanie** | instrukcja instalacji, ewentualnie prosty instalator `Lang/` | paczka dla innych graczy | decyzja właściciela |

Pomysły na później: Czytanki dwujęzyczne EN/PL, słowniczek pojęć Miasta
generowany z danych, raport „co nowego w tym tygodniu” po każdej aktualizacji.
