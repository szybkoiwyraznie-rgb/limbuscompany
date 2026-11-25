# Plan (roadmap)

Etapy są kolejne; każdy kończy się dowodem (test syntetyczny → kopia plików →
gra). Szczegóły etapów: [WORKFLOW.md](WORKFLOW.md).

## Faza 0 — fundamenty ✅ (2026-11-25)

- Zasady, dokumentacja, polityka danych, kontrola indeksu, CI (Linux + Windows).
- Zbieracz 1.0.0 z trybem aktualizacji; walidator zwrotu; rozpoznanie struktury.

## Faza 1 — rozpoznanie danych właściciela

- [ ] Pierwszy zbiór (`URUCHOM.bat`) → Dysk → walidacja → rozpoznanie.
- [ ] Uzupełnienie [CLS_FORMAT.md](CLS_FORMAT.md) faktami (liczby, pola, tokeny).
- [ ] `config/pola_tlumaczone.json` — biała lista pól tekstowych.
- [ ] Decyzje z [CEL.md](CEL.md) (język źródłowy, prywatność repo, AI, wydawanie).

## Faza 2 — test CLS w grze (dowód mechanizmu)

- [ ] Generator patcha CLS (`tools/build_cls_patch.py`): źródło + przekład →
      `Lang/<pl>/` (pełne JSON-y, podmienione tylko pola z białej listy) +
      `config.json`.
- [ ] Instalator BAT+PS1 (kopia `Lang/config.json`, instalacja tylko w `Lang/`,
      cofanie, sprawdzenie `buildid`) + test w CI na Windows.
- [ ] Test w grze: patch „znacznikowy” (np. `[PL]` przed kilkoma napisami UI —
      techniczny znacznik, nie przekład) + test polskich znaków i fontu.

## Faza 3 — pierwszy pakiet i pilot przekładu

- [ ] Wyciąg `lc-wyciag-v1` (jednostki z kluczami, mówcą, kontekstem, tokenami).
- [ ] Generator Pakietu `lc-paczka-v1` + import zwrotki + kontrole.
- [ ] Pilot: UI + krótki fragment fabuły → Tłumacz → patch → test w grze.
- [ ] Czytanki źródłowe (fabuła główna) — pierwsze części.

## Faza 4 — tłumaczenie właściwe

- [ ] Pakiety wg kolejności z [PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md).
- [ ] Cotygodniowy cykl aktualizacji: diff jednostek, pakiety przyrostowe.
- [ ] Czytanki PL.

## Faza 5 — wydanie (tylko po decyzji właściciela)

- [ ] Font z licencją pozwalającą na redystrybucję w `assets/fonts/` + licencja.
- [ ] Proces wydania (numeracja, `buildid` w nazwie, sumy SHA-256, instrukcja).
- [ ] Ponowne sprawdzenie zasad fanowskich Project Moon.

Nie włączaj automatycznej publikacji wydań, dopóki proces z fazy 5 nie jest
zaprojektowany i sprawdzony.
