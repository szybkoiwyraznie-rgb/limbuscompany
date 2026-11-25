# Plan

Etapy są sekwencyjne tam, gdzie wymagają danych; w nawiasie — kto blokuje.

| Etap | Cel | Wynik | Blokuje |
|---|---|---|---|
| **0. Fundamenty** ✅ | repo, zasady, CI, zbieracz, walidator, inspekcja | ten PR | — |
| **1. Rozpoznanie** ✅ | pierwsza paczka ze zbieracza, fakty o formacie | [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md), E-004, E-007 (build Steam `26652290`) | — |
| **2. Dane w repo** ✅ | `tools/import_data.py` → `index/` (Localize kr/en + tabele StaticData) z manifestem | `index/`, [INDEX_FORMAT.md](INDEX_FORMAT.md) (build Steam `26652290`, E-007) | — |
| **3. Droga end-to-end** ⏳ | paczka testowa `Lang/Polski/` (przycisk „Clear all caches” + 18 polskich znaków), wybór czcionek | `LCB_TEST_DROGI_Polski_26652290.zip` gotowa na Dysku (E-009) — czeka na test w grze | właściciel (test w grze → O-03) |
| **4. Rurociąg przekładu (100% gry)** ✅ | `build_package.py` + `package_views.py` (`sceny.zip` + `widoki.zip`), `import_zwrotki.py`, `build_lang.py` | kompletny pakiet `plik_dla_tlumacza_v2.zip` na Dysku (D-08, E-008) + gotowy importer i generator `Lang/Polski/` (E-009) | tłumacz (pierwsza zwrotka) |
| **5. Czytanki** ✅ | `tools/build_reading.py` (fabuła w kolejności z `wiedza/indeks_fabuly.json`), `tools/build_profiles.py` (plik ID) | `czytanki/` w repo; układ zaakceptowany i zamrożony (D-07, O-04 zamknięte) | — |
| **6. Aktualizacje** | `audit_update.py` (różnice po identyfikatorach, jak TW `update-kor.yml`), pakiety uzupełniające | obieg tygodniowy | — |
| **7. Skala** | słowa kluczowe, fabuła Canto po Canto, Identity/E.G.O | kolejne pakiety | tłumacz |
| **8. Wydawanie** | instrukcja instalacji (rozpakuj folder do `Lang/`, wybierz język) | paczka dla innych graczy | decyzja właściciela |

LimbusLocalizationManager (kimght) to tylko społecznościowy instalator wielu
tłumaczeń — **nie jest nam potrzebny**; paczkę instaluje się, rozpakowując
folder. Opcjonalnie można się tam kiedyś zgłosić, jeśli właściciel zechce
udostępnić przekład innym.

Pomysły na później: Czytanki dwujęzyczne EN/PL, słowniczek pojęć Miasta
generowany z danych, raport „co nowego w tym tygodniu” po każdej aktualizacji.
