# Plan

Etapy są sekwencyjne tam, gdzie wymagają danych; w nawiasie — kto blokuje.

| Etap | Cel | Wynik | Blokuje |
|---|---|---|---|
| **0. Fundamenty** ✅ | repo, zasady, CI, zbieracz, walidator, inspekcja | ten PR | — |
| **1. Rozpoznanie** | pierwsza paczka ze zbieracza, fakty o formacie | [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md) z liczbami, E-005; wstępnie zrobione na publicznym lustrze (E-004) | właściciel (uruchomienie zbieracza) |
| **2. Wyciąg** | `tools/extract.py` → `index/` z manifestem; test spójności | `index/`, `docs/INDEX_FORMAT.md` | O-06 |
| **3. Droga end-to-end** | paczka testowa (1 tekst + polskie znaki), wybór czcionek | test w grze „Clear all caches” | właściciel (test), O-01, O-03 |
| **4. Pakiet 000 (UI)** | `build_package.py` (część `widoki`), `import_zwrotki.py`, `build_lang.py` na małym zakresie | pierwsza paczka `Lang/` z prawdziwym przekładem | tłumacz |
| **4a. Pakiet fabularny** ⏳ | `tools/build_package.py` w układzie SRW (D-07) | **prototyp z lustra gotowy** (E-005): 1001 scen z kontekstem | O-02 |
| **5. Czytanki** ⏳ | `tools/build_reading.py` (fabuła w kolejności z `wiedza/indeks_fabuly.json`), `tools/build_profiles.py` (plik ID) | **próbki z lustra gotowe** (E-005); wersja z paczki właściciela | O-04 (akceptacja układu) |
| **6. Aktualizacje** | `audit_update.py` (różnice po identyfikatorach, jak TW `update-kor.yml`), pakiety uzupełniające | obieg tygodniowy | — |
| **7. Skala** | słowa kluczowe, fabuła Canto po Canto, Identity/E.G.O | kolejne pakiety | tłumacz |
| **8. Wydawanie** | instrukcja instalacji (rozpakuj folder do `Lang/`, wybierz język) | paczka dla innych graczy | decyzja właściciela |

LimbusLocalizationManager (kimght) to tylko społecznościowy instalator wielu
tłumaczeń — **nie jest nam potrzebny**; paczkę instaluje się, rozpakowując
folder. Opcjonalnie można się tam kiedyś zgłosić, jeśli właściciel zechce
udostępnić przekład innym.

Pomysły na później: Czytanki dwujęzyczne EN/PL, słowniczek pojęć Miasta
generowany z danych, raport „co nowego w tym tygodniu” po każdej aktualizacji.
