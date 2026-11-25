# Sposób pracy (workflow)

Schemat jest przeniesiony z WWM i SRW, ale uproszczony, bo Limbus ma oficjalny
format tłumaczeń (CLS) i niewielkie pliki tekstowe JSON.

```
 [Właściciel]                 [Agenci]                               [Tłumacz]
 URUCHOM.bat ──ZIP──► Dysk ──► walidacja ─► rozpoznanie ─► wyciąg ─► Pakiet ──► przekład
                                                       │                           │
                                                       └─► Czytanki (źródło)       │
 test w grze ◄── instalator ◄── patch CLS Lang/pl ◄── kontrole ◄── import zwrotki ◄┘
      │                                                             │
      └──── zgłoszenia z gry (issue) ──────────────────────────────►└─► Czytanki PL
```

## Etapy

| # | Etap | Kto | Wejście → wyjście | Narzędzie |
|---|---|---|---|---|
| 0 | Zbieranie | Właściciel | gra → `LC_DANE_*.zip` na Dysku | `collector/` (gotowe) |
| 1 | Przyjęcie | Agent | ZIP → `local/zwroty/…`, wynik walidacji | `validate_collector_return.py` (gotowe) |
| 2 | Rozpoznanie | Agent | ZIP → `dist/rozpoznanie.json/.md`, fakty w `CLS_FORMAT.md` | `rozpoznanie_localize.py` (gotowe) |
| 3 | Wyciąg | Agent | ZIP → `wyciag/` (lokalnie, `lc-wyciag-v1`): jednostki tekstu z kluczami, mówcą, kontekstem, tokenami | do zrobienia |
| 4 | Pakiet | Agent | wyciąg → `paczki/<nazwa>/` (README, pliki tekstowe, `paczka.json`) | do zrobienia, [PAKIET_TLUMACZA.md](PAKIET_TLUMACZA.md) |
| 5 | Przekład | Tłumacz | pakiet → zwrotka (pliki z wypełnionym `PL:`) | — |
| 6 | Import | Agent | zwrotka → `tlumaczenie/` (`klucz → PL`), raport odrzuceń | do zrobienia |
| 7 | Kontrole | Agent | tokeny, znaczniki `<…>`, `\n`, długości, glosariusz, spójność nazw | do zrobienia |
| 8 | Patch CLS | Agent | źródło + `tlumaczenie/` → `Lang/<pl>/` + `Font/` + `config.json` | do zrobienia |
| 9 | Instalator | Agent | patch → `LC_PL_INSTALUJ.zip` (BAT + PS1, kopia i cofanie) | do zrobienia |
| 10 | Test w grze | Właściciel | zgłoszenie (issue „Zgłoszenie z gry”) | — |
| 11 | Aktualizacja gry | Właściciel + Agent | `URUCHOM_AKTUALIZACJE.bat` → różnice → pakiet tylko nowych/zmienionych jednostek | zbieracz (gotowe) + diff (do zrobienia) |

## Zasady przekazywania

- **Na Dysk** (folder „Limbus Company”, do utworzenia przez agenta przy
  pierwszej dostawie): zestawy BAT (zbieracz, instalator), zwroty zbieracza od
  właściciela, Pakiety dla Tłumacza, Czytanki (dopóki nie mogą być w Git). Każda
  dostawa: rozmiar + SHA-256, pobranie z powrotem i porównanie bajtów.
- **W Git**: wszystko, co nie jest tekstem gry (zob. [DATA_POLICY.md](DATA_POLICY.md)),
  oraz przekład Tłumacza.
- **Pakiety są deterministyczne**: ten sam wyciąg i te same parametry → te same
  bajty. Kopia przekazanego pakietu (bez tekstu gry, jeśli repo publiczne —
  sam `paczka.json`) zostaje w `paczki/`.

## Tygodniowy cykl aktualizacji gry

Limbus aktualizuje się zwykle w czwartki. Po aktualizacji:

1. Właściciel: `URUCHOM_AKTUALIZACJE.bat` → ZIP tylko ze zmienionymi plikami.
2. Agent: walidacja, diff względem poprzedniego wyciągu na poziomie jednostek
   (nowe / zmienione źródło / usunięte), wpis w `EXPERIMENT_LOG.md`.
3. Jednostki ze zmienionym źródłem tracą status „przetłumaczone” (klucz zawiera
   hash źródła) i trafiają do kolejnego pakietu. Patch zawsze budowany dla
   konkretnego `buildid`; niezgodność → ostrzeżenie w instalatorze.
4. Nowy rozdział/wydarzenie → osobny pakiet; Czytanki dostają nową część.

## Kontrola jakości przekładu (techniczna, nie językowa)

Agent sprawdza i raportuje — nie poprawia treści:

- zgodność tokenów: znaczniki `<color=…>`, `<sprite…>`, `<link…>`, `{0}`, `\n`;
- puste/nieprzetłumaczone pozycje, pozostałe znaki hangul/kana;
- spójność nazw własnych z glosariuszem (`tlumaczenie/glosariusz.*`, ustala Tłumacz);
- długość względem źródła (ostrzeżenie, nie błąd — limity UI ustala test w grze).

Jedyne dopuszczalne zmiany agenta: techniczne (np. przywrócenie tokenu), zapisane
w `tlumaczenie/KOREKTY.json` z uzasadnieniem, widoczne dla Tłumacza.
