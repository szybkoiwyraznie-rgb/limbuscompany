# Czcionki dla paczki Custom Language (`assets/fonts/`)

Od wersji `1.74.0` (sprawdzone w grze na `v.1.119.1`, build Steam `26652290`,
eksperyment `E-011`) oficjalny mechanizm `LimbusCompany_Data/Lang/<Nazwa>/`
wymaga obecności plików czcionek w podkatalogach `Font/Context/` oraz
`Font/Title/`. Bez nich gra pomija własny język nawet wtedy, gdy nazwa języka
widnieje na liście `Select Custom Language` i w `Lang/config.json`.

Katalog zawiera wyłącznie **niemodyfikowane** pliki z oficjalnych źródeł na
licencji **SIL Open Font License 1.1**, odpowiadające krojom używanym przez
samą grę:

| Rola w `Lang/<Nazwa>/` | Plik | Autor i wersja | Licencja | Rozmiar | SHA-256 |
|---|---|---|---|---:|---|
| `Font/Context/Pretendard-Regular.ttf` | `Context/Pretendard-Regular.ttf` | Kil Hyung-jin (`orioncactus/pretendard`), v1.309 | SIL OFL 1.1 (`OFL-Pretendard.txt`, Reserved Font Name `Pretendard`) | 2 725 828 B | `6d0af5258997aec7354a6e340fc2325ba321c410ca48b3af858c8c3d6e92a324` |
| `Font/Title/Mikodacs.otf` | `Title/Mikodacs.otf` | Grzegorz Luk (`gluk`, `glukfonts.pl`), v0.28 | SIL OFL 1.1 (`OFL-Mikodacs.txt`, Reserved Font Name `Mikodacs`) | 110 228 B | `d685ef7fb3b0c88a8c830fb664079d30bacfb5a5dbb0d58d6170f732391b8d30` |

## Zgodność licencyjna i pokrycie znaków

- Oba pliki binarne są **w 100% niemodyfikowane** względem oryginałów autorów,
  dzięki czemu zachowanie zastrzeżonych nazw (`Pretendard`, `Mikodacs`) jest
  w pełni zgodne z punktem 3 licencji SIL OFL 1.1.
- Obie czcionki zawierają komplet **18/18 polskich znaków diakrytycznych**
  (`ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ`) oraz **8/8 znaków polskiej typografii**
  (`„”«»–—…•`) zweryfikowanych na tablicy OpenType `cmap`.
- Podczas budowy archiwum `tools/build_lang.py` kopiuje do
  `LimbusCompany_Data/Lang/<Nazwa>/Font/{Context,Title}/` wyłącznie pliki
  `.ttf`/`.otf` (aby automatyczny wybór pierwszego pliku przy `titleFont: ""`
  i `contextFont: ""` nigdy nie trafił na plik tekstowy), natomiast pełne
  teksty licencji dołącza do każdego archiwum `.zip` w katalogu
  `LICENCJE_CZCIONEK/`.
