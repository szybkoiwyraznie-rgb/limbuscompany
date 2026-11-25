# Wcześniejsze prace (prior art)

Zasada: z cudzych projektów bierzemy **wiedzę o formacie i problemach**,
nigdy ich tekstu przekładu (także z polskiego tłumaczenia). Testy używają
wyłącznie danych wymyślonych.

| Projekt | Co z niego wiemy | Uwagi |
|---|---|---|
| [Ogłoszenie Project Moon, 2025-03-31](https://store.steampowered.com/news/app/1973530/view/533220039674824263) | oficjalny mechanizm Custom Language, położenie `Localize`, `Lang/`, `config.json`, `Font/` | źródło faktów, [FEASIBILITY.md](FEASIBILITY.md) |
| [Echodial/Limbus-Company-PL-Tlumaczenie](https://github.com/Echodial/Limbus-Company-PL-Tlumaczenie) | istniejące fanowskie tłumaczenie PL (folder `Polish`, ~1980 plików; Selva Obscura, Canto I, część Identity i umiejętności); czcionki Pretendard / Mikodacs; `Font/replacement_map.json` (znaki → PUA) | **tylko technika**, zero tekstu; nasza nazwa języka musi się różnić (O-01) |
| [Eden-Office/LimbusCompanyBusFR](https://github.com/Eden-Office/LimbusCompanyBusFR) | pełny układ paczki `Lang/fr`: ~2423 JSON, ~34 MB; podfoldery; schematy `dataList`; klucze `config.json` | podstawa hipotez w [FORMAT_LOCALIZE.md](FORMAT_LOCALIZE.md) |
| LocalizeLimbusCompany (LLC, zh-CN; CC BY-NC-SA) | README: kilka plików istnieje w ich wydaniu, a nie w oficjalnym EN | sprawdzimy parowanie języków inspekcją |
| jinglejingle3344/LCB-translation-randomizer | usuwanie prefiksów `EN_`/`KR_`/`JP_` przy kopiowaniu do `Lang/` | zgodne z naszym modelem ścieżek logicznych |
| Skrypty dwujęzycznego łączenia (SunZheee) | łączenie dwóch języków w jednym tekście | pomysł na Czytanki dwujęzyczne |
| Poradnik „Limbus Custom Language” (gitbook) | narzędzie podglądu; `Bufs`, `BattleKeywords`, `SkillTag` z fallbackiem do `Localize/en` | do sprawdzenia w grze |
| Poradniki PT-BR / RU / FR | brak ryzyka bana; jedna czcionka na slot (Context/Title); część tekstów nieprzetłumaczalna; brak wsparcia mobile | obserwacje, nie fakty |
| WhenThe1/Limbus-Company-Identities-Battle-Dialogues | układ kwestii bitewnych Identity | struktura, nie treść |

Projekty właściciela, z których przejęliśmy sposób pracy: WWM i SRW
([LESSONS.md](../LESSONS.md)).
