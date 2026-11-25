# Czytanki

Materiały **do czytania przez właściciela jako gracza** — fabuła i lore
Limbus Company w wygodnej formie, niezależnie od postępu przekładu. Wzorzec:
czytanki WWM i SRW Y (HTML/DOCX, kolejność gry, mówcy, jawne luki).

## Planowane serie

| Seria | Źródło | Zawartość |
|---|---|---|
| **Fabuła** | `StoryData` | Prolog, Canto, Intervallo, wydarzenia — sceny w kolejności, z mówcą i miejscem |
| **Sinnerzy i Identity** | pliki postaci/osobowości, kwestie głosowe | dla każdej Identity: opis, historia (jeśli jest), kwestie |
| **E.G.O** | pliki E.G.O | opisy, kwestie, powiązane Abnormality |
| **Miasto (lore)** | opisy przedmiotów, słowa kluczowe, teksty interfejsu | słowniczek pojęć: Skrzydła, Dystrykty, Palce… |

Każda Czytanka ma wersję **EN** (od razu po pierwszym wyciągu) i później
**PL** (z przyjętego przekładu, z angielskim tam, gdzie przekładu brak —
oznaczonym).

## Zasady

- Budowane **tylko z `index/` i `tlumaczenie/`** (planowany
  `tools/czytanki.py`), z manifestem buildu.
- Kolejność opiera się na danych gry (identyfikatory scen, nazwy plików,
  ewentualne tabele kolejności). Niepewność kolejności = jawna uwaga w
  dokumencie, nie zgadywanie.
- Format i układ ustala właściciel (O-04). **Po akceptacji układ jest
  zamrożony** (lekcja SRW Y).
- Czytanki z tekstem gry są prywatne: trafiają na Dysk właściciela, nie do Git
  (w Git — generator i ewentualnie mały przykład na danych wymyślonych).

## Otwarte pytania (wymagają danych)

- Czy prefiksy `StoryData` (`1D`…`8D`, `E`, `ES`, `P`, `PC`, `S`) odpowiadają
  Canto / wydarzeniom / Intervallo i jak sortować wewnątrz grupy.
- Czy w plikach są tytuły rozdziałów i scen (`title`), czy trzeba je brać z UI.
- Gdzie są historie Identity (osobny plik? tekst w opisach?).
