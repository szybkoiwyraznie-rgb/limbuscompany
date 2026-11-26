# Słownik terminów i konwencji dla tymczasowego przekładu UI/meta (`AI-tymczasowe`, `D-11`)

Ten plik obowiązuje wszystkie agenty Arena wykonujące tymczasowy przekład interfejsu, opisów technicznych oraz kart meta/statystyk (`"origin": "ai"`).
**Zasada nadrzędna (`D-11`):** przekład ludzkiego Tłumacza ma zawsze bezwzględny priorytet — każda forma ustalona przez Tłumacza w `tlumaczenie/` (obecnie `LC_PL1.zip`) jest wiążąca i nie wolno jej zmieniać.

---

## 1. Terminy kanoniczne ustalone przez Tłumacza (`LC_PL1.zip`)

| KR | EN | Kanoniczny przekład PL (Tłumacz) | Uwagi |
|---|---|---|---|
| 수감자 | Sinner / Sinners | **Grzesznik** / **Grzesznicy** | `LCB Sinner` → **Grzesznik LCB** |
| 인격 | Identity / Identities | **Tożsamość** / **Tożsamości** | `Identity Story` → **Historia Tożsamości** |
| 환상체 | Abnormality / Abnormalities | **Anomalia** / **Anomalie** | |
| 뒤틀림 | Distortion | **Wypaczenie** / **Wypaczenia** | |
| E.G.O | E.G.O | **E.G.O** | bez kropki na końcu (`E.G.O`, nie `E.G.O.`) |
| 엔케팔린 | Enkephalin | **Enkefalina** | `Enkephalin Module` → **Moduł Enkefaliny**, `Enkephalin Box` → **Skrzynka Enkefaliny** |
| 끈 | Thread | **Nić** | |
| 황금가지 | The Golden Boughs | **Złote Gałęzie** (l.poj. **Złota Gałąź**) | |
| 메피스토펠레스 | Mephistopheles | **Mefistofeles** | autobus LCB |
| 관리자 | Manager / Executive Manager | **Kierownik** / **Kierownik Wykonawczy** | zwracanie się do Dantego |
| 도시 | The City | **Miasto** | wielką literą w znaczeniu świata gry |
| 날개 | The Wings | **Skrzydła** (l.poj. **Skrzydło**) | Korporacje A–Z |
| 둥지 | The Nests | **Gniazda** (l.poj. **Gniazdo**) | |
| 뒷골목 | The Backstreets | **Zaułki** | |
| 특이점 | Singularity / Singularities | **Osobliwość** / **Osobliwości** | |
| 해결사 | Fixer / Fixers | **Fikser** / **Fikserzy** | pisownia przez `ks`! |
| 사무소 | Office / Offices | **Biuro** / **Biura** | |
| 조직 | Syndicate / Syndicates | **Syndykat** / **Syndykaty** | |
| 협회 | Association | **Stowarzyszenie** | np. `Seven Association South Section 6` → **Południowa Sekcja 6 Stowarzyszenia Seven** |
| 검계 | The Blade Lineage | **Ród Ostrza** | np. `Blade Lineage Salsu` → **Salsu z Rodu Ostrza** |
| 흑운회 | The Kurokumo Clan | **Klan Kurokumo** | np. `Kurokumo Wakashu` → **Wakashu z Klanu Kurokumo** |
| 료.고.파 | R.B. | **R.P.M.** | ustalone w `LC_PL1.zip` |
| 거울 세계 | Mirror World | **Świat Lustrzany** / **Światy Lustrzane** | `Mirror Dungeon` → **Lustrzany Loch** / **Lustrzane Lochy** |
| 단테의 노트 | Dante's Notes | **Notatki Dantego** | |

---

## 2. Odmiana imion 12 Grzeszników (ustalona w `StoryTheaterMirrorWorldStoryTitle.json`)

| Nr | Imię (M.) | Dopełniacz (D. — *czyja?*) | Celownik (C.) | Narzędnik (N.) | Uwagi |
|---|---|---|---|---|---|
| 01 | **Yi Sang** | **Yi Sanga** | Yi Sangowi | Yi Sangiem | odmienne |
| 02 | **Faust** | **Faust** | Faust | Faust | nieodmienne (r. żeński) |
| 03 | **Don Quixote** | **Don Quixote** | Don Quixote | Don Quixote | nieodmienne (r. żeński w LCB!) |
| 04 | **Ryōshū** | **Ryōshū** | Ryōshū | Ryōshū | nieodmienne, zachowaj makrony `ō`/`ū` |
| 05 | **Meursault** | **Meursaulta** | Meursaultowi | Meursaultem | odmienne |
| 06 | **Hong Lu** | **Hong Lu** | Hong Lu | Hong Lu | nieodmienne |
| 07 | **Heathcliff** | **Heathcliffa** | Heathcliffowi | Heathcliffem | odmienne |
| 08 | **Ishmael** | **Ishmael** | Ishmael | Ishmael | nieodmienne (r. żeński) |
| 09 | **Rodion** | **Rodion** | Rodion | Rodion | nieodmienne (`Rodia` → D. `Rodii`) |
| 10 | **Sinclair** | **Sinclaira** | Sinclairowi | Sinclairem | odmienne |
| 11 | **Outis** | **Outis** | Outis | Outis | nieodmienne (r. żeński) |
| 12 | **Gregor** | **Gregora** | Gregorowi | Gregorem | odmienne |

---

## 3. Konwencje techniczno-bojowe dla UI i kart (`Fala 1` → `Fala 2` → `Fala 3`)

> Paczka `P01` (`1A Fundament bojowy`) jako pierwsza utrwala dokładne brzmienie etykiet `[SkillTag]`, grzechów i odporności; kolejne paczki **muszą** sprawdzać już zaimportowane wpisy w `tlumaczenie/pliki/` i trzymać 100% spójności.

### Grzechy / Atrybuty (`AttributeText.json`)
- `Wrath` (분노) → **Gniew**
- `Lust` (색욕) → **Żądza**
- `Sloth` (나태) → **Lenistwo**
- `Gluttony` (탐식) → **Obżarstwo**
- `Gloom` (우울) → **Posępność**
- `Pride` (오만) → **Pycha**
- `Envy` (질투) → **Zawiść**

### Typy ataku i odporności (`ResistText.json`)
- `Slash` (참격) → **Cięcie** (obrażenia **cięte**)
- `Pierce` (관통) → **Kłucie** (obrażenia **kłute**)
- `Blunt` (타격) → **Obuch** (obrażenia **obuchowe**)
- Odporności: `Fatal` → **Zabójcza**, `Weak` → **Słaba**, `Normal` → **Zwykła**, `Endured` → **Odporna**, `Ineff.` → **Nieskut.**

### Mechanika walki i rozwoju
- `Clash` (합) → **Starcie** (`Clash Power` → **Moc Starcia**, `[Clash Win]` → **[Wygrane Starcie]**, `[Clash Lose]` → **[Przegrane Starcie]**)
- `Coin` (코인) → **Moneta** (`Coin Power` → **Moc Monety**, `Heads` → **Awers**, `Tails` → **Rewers**, `[On Hit]` → **[Przy Trafieniu]**, `[Heads Hit]` → **[Trafienie Awersem]**, `[On Use]` → **[Przy Użyciu]**, `[Combat Start]` → **[Początek Walki]**, `[Turn End]` → **[Koniec Tury]**)
- `Base Power` / `Final Power` → **Moc Bazowa** / **Moc Końcowa**
- `Offense Level` / `Defense Level` → **Poziom Ataku** / **Poziom Obrony**
- `Sanity (SP)` (정신력) → **Poczytalność (SP)** (`Panic` → **Panika**, `Low Morale` → **Niskie Morale**)
- `Stagger` (흐트러짐) → **Oszołomienie** (`Stagger Threshold` → **Próg Oszołomienia**)
- `Resonance` / `Absolute Resonance` → **Rezonans** / **Rezonans Absolutny**
- `Uptie` (동기화) → **Synchronizacja** (`Uptie Tier` → **Poziom Synchronizacji**)
- `Threadspin` (환상해체 / 끈 엮기) → **Splot Nici**
- `E.G.O Gift` → **Dar E.G.O**, `E.G.O Corrosion` → **Korozja E.G.O**, `Awakening` → **Przebudzenie**
- `Lunacy` (광기) → **Szaleństwo** (`Paid Lunacy` → **Płatne Szaleństwo**, `Free Lunacy` → **Darmowe Szaleństwo**), `Egoshard` → **Odłamek E.G.O**

### 7 głównych archetypów statusów (`Potency` → **Siła**, `Count` → **Licznik**)
- `Burn` (화상) → **Podpalenie**
- `Bleed` (출혈) → **Krwawienie** (`Bleed Deluge` → **Potop Krwawienia**)
- `Tremor` (진동) → **Wstrząs** (`Tremor Burst` → **Wyładowanie Wstrząsu**, `Amplitude Entanglement` → **Splątanie Amplitudy**)
- `Rupture` (파열) → **Rozdarcie**
- `Sinking` (침잠) → **Zatonięcie** (`Sinking Deluge` → **Potop Zatonięcia**)
- `Poise` (호흡) → **Oddech**
- `Charge` (충전) → **Ładunek**

### Podstawowe wzmocnienia, osłabienia i pojęcia frakcyjne (`P01–P02`)
- `Haste` / `Bind` → **Pośpiech** / **Spętanie**
- `Protection` / `Fragile` → **Ochrona** / **Wrażliwość**
- `Attack Power Up` / `Attack Power Down` → **Wzrost Mocy Ataku** / **Spadek Mocy Ataku**
- `Defense Power Up` / `Defense Power Down` → **Wzrost Mocy Obrony** / **Spadek Mocy Obrony**
- `Damage Up` / `Damage Down` → **Wzrost Obrażeń** / **Spadek Obrażeń**
- `Offense Level Up` / `Offense Level Down` → **Wzrost Poziomu Ataku** / **Spadek Poziomu Ataku**
- `Defense Level Up` / `Defense Level Down` → **Wzrost Poziomu Obrony** / **Spadek Poziomu Obrony**
- `Unopposed Attack` → **Atak Jednostronny**, `Atk Weight` → **Waga Ataku**, `Guard` / `Evade` / `Counter` → **Garda** / **Unik** / **Kontra**
- `Bloodfiend` / `Bloodbag` / `Kindred` → **Krwiożerca** / **Worek Krwi** / **Pokrewny** (`First/Second/Third Kindred` → **Pierwszy/Drugi/Trzeci Pokrewny**)
- Palce: `The Thumb` → **Kciuk**, `The Index` → **Wskazujący**, `The Middle` → **Środkowy**, `The Ring` → **Serdeczny**, `The Pinky` → **Mały Palec** (`Prescript` → **Nakaz**)

### Tryby gry, Lustrzane Lochy i wydarzenia (`Fala 1: P03–P14`)
- Menu główne i rozwój: `Window` → **Okno**, `Drive` → **Jazda** (`Intervallo` → **Intervallo**, `Deviazione` → **Deviazione**), `Theater` → **Teatr** (`Main Story` → **Główna Opowieść**, `Detour Tales` → **Opowieści Poboczne**), `Extract` → **Ekstrakcja** (`Ideality` → **Wymiana Yisanga**), `Dispenser` → **Automat**, `Jukebox` → **Szafa grająca**, `Announcer` → **Komentator**, `Dashboard` → **Panel dowodzenia**, `Skin Projection` → **Projekcja Wyglądu** (`Create Projection` → **Tworzenie Projekcji**), `Sapling of Light` → **Sadzonka Światła**
- Walka zaawansowana: `Focused Encounter` → **starcie skupione**, `Chain Battle` → **Walka Seryjna** (`Backup` / `Sub-in` → **Rezerwa** / **Wejście Rezerwy**), `E.G.O Overclock` → **Przeciążenie E.G.O** (`Stable` / `Unstable Overclock` → **Stabilne** / **Niestabilne Przeciążenie**), `Abnormality Guide` → **Kompendium Anomalii** (`Observation Level` → **Poziom Obserwacji**, `Part Break` → **Zniszczenie części**, `Sever` → **Odcięcie**), bazowe E.G.O Heathcliffa `Bodysack` (`시체자루`) → **Worek na Zwłoki**
- `Luxcavation` (채광) → **Lochy Wydobywcze** (`EXP Luxcavation` → **Lochy Wydobywcze PD**, `Thread Luxcavation` → **Lochy Wydobywcze Nici**, `Training Ticket` → **Bilet Treningowy** / **Bilet szkoleniowy**)
- `Refraction Railway` (거울굴절철도) → **Kolej Załamania** (`Line 1..6` → **Linia 1..6**, `BokGak` → **BokGak**, `First/Terminus/Way Station` → **Stacja początkowa/końcowa/postojowa**, `Section` → **Odcinek**, `Cycle` → **Cykl**, `Lost & Found` → **Biuro Rzeczy Znalezionych**)
- `Mirror Dungeon` (거울 던전) → **Lustrzane Lochy**:
  - Edycje: `Mirror of the Beginning` → **Lustro Początku**, `Mirror of Mirrors` → **Lustro Luster**, `Mirror of the Lake` → **Lustro Jeziora**, `Mirror of the Wuthering` → **Lustro Wichury** (`Simulation` / `Ritornello` → **Symulacja** / **Ritornello**), `Mirror of the Dreaming` → **Lustro Snu**, `Mirror of the Immortality` → **Lustro Nieśmiertelności**, `Mirror of Names and Spiders` → **Lustro Imion i Pająków**, `Mirror of Sisyphe` → **Lustro Sisyphe**
  - Mechaniki: `Starlight` → **Gwiezdny Blask** (`Starlight Bonus` → **Premia Gwiezdnego Blasku**), `Engrave Stars` → **Wyryj gwiazdy**, `Wish of Stars` → **Życzenie Gwiazd**, `Grace of Stars` → **Błogosławieństwo Gwiazd** (`Śniącej Gwiazdy` / `Nieśmiertelnej Gwiazdy` / `Gwiazdy Imion i Pająków` / `Gwiazdy Sisyphe`), `Star Cluster's Grace` → **Łaska Gromady Gwiazd**, `Theme Pack` → **Pakiet Tematyczny** (`Pack Observation` → **Obserwacja Pakietów Tematycznych**, `Gift Observation` → **Obserwacja Darów E.G.O**), `Squad Rental` → **Wypożyczenie składu**, `Cost` → **Koszt**, `Rest Stop` → **Przystanek Odpoczynku**, `Rest Bonus` → **Premia Odpoczynku**, `Weekly Bonus` → **Cotygodniowa Premia**, `Super Shop` → **Wzmocniony Sklep**, `Enhance` / `Fuse` (`Fusion`) / `Sell` → **Ulepsz** / **Syntezuj** (**Synteza**) / **Sprzedaj**, `Parallel Superposition Mode` → **Tryb Superpozycji Równoległej** (`EXTREME`), `Projection Rate` → **Stopień Projekcji**, `Adversities` → **Utrudnienia**, `Mounting Trials` → **Próby**
- Inne tryby z `P12–P13`: `Projection Battle][elttaB noitcejorP` → **Walka Projekcyjna][anjyckejorP aklaW** (`Reflection Effects` → **Efekty Odbicia**, `Scorched Lens` → **Wypalona Soczewka**, `Developed Film` → **Rozwinięta Klisza**), `Diagram Construction` → **Konstrukcja Schematów** (`Diagram` → **Schemat**, `Representation` → **Reprezentacja**, `Diagram Distortion` → **Wypaczenie Schematu**, `Construction Power` → **Siła Konstrukcji**, `Shard` / `Universal Shard` → **Okruch** / **Okruch Uniwersalny**, `Defense Policy` → **Polityka obrony**)
- Wydarzenia (`Intervallo` / sezonowe): `Hell's Chicken` → **Piekielny Kurczak** (`Bongy Plushie` → **Pluszak Bongy**), `S.E.A.` → **M.O.R.Z.E.**, `Miracle in District 20` → **Cud w Dystrykcie 20**, `Walpurgis Night` → **Noc Walpurgii**, `Yield My Flesh to Claim Their Bones` → **Oddam Ciało, by Złamać Ich Kości**, `Timekilling Time` → **Czas Zabijania Czasu**, `Murder on the WARP Express` → **Morderstwo w Ekspresie WARP**, `LCB Regular Check-up` → **Okresowe Badania LCB**, `Nocturnal Sweeping` → **Nocne Sprzątanie**, `Spring Cultivation` → **Wiosenny Szlif** (`Jia Xichun`), `Pilgrimage of Compassion` → **Pielgrzymka Współczucia**, `Strands Caught, Woven` → **Splatanie Pasm**, `Memory of Experience` → **Pamięć Doświadczenia**

### Słowa kluczowe walki — BossRaid / Le Noir / Pequod (`Fala 2: P15`)
- Nowe pojęcia statusów: `Tętnienie` (맥동) / `Bezruch` (박동), `Poczucie Winy` (죄악감), `Igłogwóźdź` (바늘못), `Dowód Spowiedzi` (고백의 증거), `Maks. HP` (최대 체력), `Wstrząs - Zachowanie` (방해 - 보존), `Błąd Synchronizacji` (동기화 오류), `Zataksydermizowany` (박제 상태), `Cień Projekcji […]` (사영 […])
- System Sisyphe (`BossRaid`): `Strażnik` / `Kapłan` Wyroku Sisyphe (간수/신부), `Obcy` (이방인), `Utrapienie` (고난), `Zapisano w Księdzie` (장부에 적힘), `Zdobycz` (사냥감), `Zachowanie Systemu Sisyphe` (시지프 시스템 보존), `Chwiejna Teofania` (흔들리는 현신); cytowane nazwy umiejętności w opisach: `Śmierć Skazanym` (사형 집행), `Przymusowe Wygnanie` (강제 퇴장), `Sąd...! Wyrok...! Potępienie...!` (심판…! 선고…! 단죄…!), `Czy naprawdę próbujesz zepsuć System Sisyphe?` (시지프 시스템을 진짜 망가트리려고?)
- Gwoździe: `Młotogwóźdź [Sąd]` / `Młotogwóźdź [Potępienie]` (망치 못[심판/단죄]), `Gwóźdź [Kara]` / `Gwóźdź [Pokuta]` (못[형벌/속죄]), `Gwóźdź [Console]` / `Gwóźdź [Breakpoint]` / `Gwóźdź [Exception]` dosłowne (못[Console/Breakpoint/Exception]); nazwa słowa kluczowego `〜` pozostaje dosłowna
- Czarny/Czerwony Bóg: `Głos Czarnego Boga` / `Wszechmoc Czarnego Boga` (검은 신의 목소리/전능), `Głos Czerwonego Boga` (붉은 신의 목소리), `[완숙]` → **[Dorosłość]**, `Niepowstrzymana Furia [Le Désir]` (폭주), `Błogosławieństwo Czarnego Boga` (검은 신의 축복)
- Grand Magasin / Le Noir (a1c10): `Grand Magasin` (백화점), nazwy francuskie dosłowne: `Le Noir`, `Le Vomissement`, `Le Désir`, `La Nausée`, `Engagement`, `Être-pour-autrui` / `Être-pour-soi`, `Pathos - Désir d'être`, `Logos - Manque d'être`, `Désespoir`, `Délaissement`, `L'Abject`; `Jeanne` i zwrot „ma puce" bez tłumaczenia; `Przybity` (몰림); klejnoty Sisyphusa: `Topaz`/`Ametyst`/`Bursztyn`/`Szmaragd`/`Złoto`/`Rubin`/`Safir`/`Onyks`/`Diament`; `Warstwowy Patchwork` (다층 레이어 패치워크), `Czujność` (경계심), `Wdzięczność za Wysłuchanie` (경청에 대한 감사), `Pikantno-Pikantny Sos` (매콤매콤소스), `Sous-chef` (수셰프), zasady Garbarni: `Zasada: Zakaz …` / `Naruszenie Zasad Garbarni`
- Pequod / Ahab (a1c5): `Blady Szum` (창백한 소음), `Panika Szumu` (소음 공황), `Blada Panika` (하얀 공황 — zgodnie z `P02`), `Piętno Zdobyczy` (사냥감의 징표), `Splecenie` (결박, EN `Tangle` — rozróżnione od `Spętanie` = 속박 `Bind`), `Pojmanie` (포획), `Ego Pipa` / `Ego Starbucka` / `Ego Queequeg` (핍/스타벅/퀴케그의 자아), `Obrona Wsparcia` / `Tarcza Obrony Wsparcia` (원호 방어/보호막), `Rozkaz Bez Dyskusji` (거역할 수 없는 명령), `Kompulsja` (강박), `Nieczystość` (불순), `Zemsta` (앙갚음), `Oznaczony` (표식), `Odłamek Świetlówki` (형광등 파편), `Zaślepiona Obsesja` (맹목), `Larwa` (유충), `Zielony Śluz` (녹색 점액), `Nierówny Oddech` (거친 호흡), `Pwie` (뿌이), `Doświadczenie z Pwie`, `Niepowstrzymana Furia`; nazwiska `Ahab`, `Queequeg`, `Ishmael` i `Blady Wieloryb` bez zmian (zgodnie z `P06`)

### Słowa kluczowe walki — Cantos 5–9 i wydarzenia (`Fala 2: P16`)
- Nowe pojęcia: `Twarda Krew` (경혈, EN `Hardblood` — stopnie 1./2./3.), `Krwawa Uczta` (혈찬; skonsumowana → `Skonsumowana Krwawa Uczta`), `Gorączka Święta` (축제의 열기), `Obrzęd Śmierci 【…】` (주살, EN `Deathrite` — warianty 【Halt/Impede/Wane/Enfeeble/Haste】 pozostają dosłowne), `Siła Skryta [底力]` / `Siła Skrajna [極力]` (저력/극력 — Hanja dosłowne), `Gwiazda Tiantui [天退星]` / `Shin (心) - …` (bez tłumaczenia), `Splot Powideł` (잔상 얽힘, EN `Afterimage Entanglement` — stopnie I–IV jako `Splot Powideł 1.–4. stopnia`), `Rozcinające Cięcie [切斬]` (Hanja dosłowne), `Dudnienie Gungnira` (궁니르 공명), `Wbity Harpun [Żądło/Żądło Osy]` (박힌 작살 [벌침/말벌침]), `Żółty Harpun` (노란작살), `Krwawe Ostrza Nożyc` (핏빛 가위날), `Kwitnący Cierń` i pochodne (`Krwawo Utkany Cierń`, `Ulepiony z Krwi Cierń`), `Krwawa Dłoń` (피로 물든 손), `Powracający Popęd Krwi` (다시 도는 피의 충동), `Złowieszczy Talizman` (불길한 부적), `Serce Zła`/`Głębokie Serce Zła` (사심/짙은 사심)
- Fingery / Index: `Nakaz` (지령 — wg słownika `Prescript` → **Nakaz**), `Znak Nakazu` (지령 표식), `Cel Nakazu` (지령 대상), `Łaska Nakazu` (지령의 가호), `Nakaz [Kartka]` / `Nakaz [Urządzenie]` (지령[쪽지/단말기]), `Odblokowanie - I/II/III` (해금), `Karma` (카르마); `Wskazujący` (검지, EN `The Index` — wg słownika), `Ojciec Kciuka` (엄지 아비), `Uczeń Kciuka - Lucio` (엄지 제자), `Ojciec Małego Palca` (소지 아비), `Środkowy` (중지)
- Rodzina Jia i Canto 8–9: `Jia Mu` (가모), `Jia Huan` (가환), `Jia Qiu` (가치우), `Gubo` (구보), `Hongyuan` (홍원), `część Lektyki` (가마 부위), `część Tułowia` (몸통 부위), stan `Jadeitu` (보옥), `Hong Lu`, `Lei Heng` (뇌횡), `Vespa`, `Wykrzywiony Hohenheim` (뒤틀린 호엔하임), `Dom Pajęczyn` (거미집), `Faelantern` (요정 초롱, dosłownie) / `Wróżka` (요정), `Moses`, `Carmilla`, `Camille`, `Lucio`; `Don Quixote`, `Sancho` i `Dulcinea` nieodmienne (wg słownika); `Miłosierdzie Cheseda` (헤세드의 자비), `Panowanie Malkuth - Niedoskonała Manifestacja` (말쿠트의 통치)
- Pojedynki: `Wyzwanie na Pojedynek - …` (결투 선포), `Atak Skupiony` (집중 공격), `Specjalista od Pojedynków` (1:1 전력), `Honorowy Pojedynek` (명예로운 결투), `Eskalacja Pojedynku` (결투 고조), `Nieostrożny Pojedynek` (무모한 결투), `Noc w Zaułkach` (뒷골목의 밤), `Pierwsza/Druga/Trzecia Fala` (제 1/2/3파)
- Kwantyfikatory powtarzalne: `Podstawowy Poziom Ataku/Obrony` (기본 공격/방어 레벨), `Wzrost Leczenia HP` (체력 회복 증가), `Spadek Wydajności Leczenia Poczytalności` (정신력 회복 효율 감소), `Spadek Mocy Ataku/Obrony` (공격/수비 위력 감소), `Wrażliwość na Rozdarcie` (파열 취약), `Niezniszczalne Monety` (파괴 불가 코인), `Osłabienie Monet Plus` (더하기 코인 약화), `wymuszone Oszołomienie` (강제 흐트러짐), `Specjalna amunicja` (특수 탄환), `1. stopnia` (1단계)
- Cytowane umiejętności: „Z rozkazu...” (명령을 받들어...), „Parada powtarza się wiecznie” (퍼레이드는 영원히 반복될거야), „Uciskane Ciało” (억압당한 육체), „Podwójne/Potrójne Cięcie - Wybuch” (이연참-폭/삼연격-폭), „Jeszcze nie pojmujesz, jak głęboka jest moc tego oka i jego szczególna natura” (너희는 그 눈의 힘과 특별함을 아직도 한참을 모르고 있구나)

---

## 4. Twarde reguły techniczne walidatora (`tools/import_zwrotki.py --ai`)

1. **Nigdy nie tłumacz identyfikatorów w nawiasach kwadratowych `[…]` należących do silnika gry** (np. `[OnSucceedAttack]`, `[Combustion]`, `[Laceration]`, `[Vibration]`, `[Burst]`, `[Sinking]`, `[Breath]`, `[Charge]`, `[Protection]`) — gra sama podmienia je na przetłumaczone nazwy z `SkillTag.json` i `BattleKeywords.json`! (Wyjątkiem są dosłowne napisy w samym `SkillTag.json`, gdzie cały tekst źródłowy to np. `[On Hit]` i nie ma on linii `tokeny: zachowaj dokładnie: [...]`).
2. **Zachowaj placeholdery i walidację tagów TMP względem KR (`D-05`)**:
   - Placeholdery `{0}`, `{1}`, `%d`, `%s`, `<sprite name="…">` oraz znaki nowej linii zapisywane jako dwuznakowe `\n` (w jednej linii `PL:`) muszą być zachowane 1:1.
   - Walidator `validate_tokens` porównuje bilans tagów TMP (`<color=…>`, `<b>`, `<i>`, `<size=…>`, `<font=…>`) względem **oryginału KR** (`net_kr`), a nie EN: nie dodawaj tagów występujących wyłącznie w EN (`<i>`, `<size=…>`), zachowuj kolejność zamykania LIFO, a tam, gdzie KR używa niezamkniętych par `<color=#f8c200>…<color=#ebcaa2>`, zachowaj dokładną liczbę tagów `<color=…>` z KR.
   - Wewnątrz `<font="BebasKai SDF">…</font>` używaj wyłącznie znaków ASCII (font ekspozycyjny nie posiada polskich znaków diakrytycznych).
   - Zamiast ostrych nawiasów `<…>` dla wyróżnień pojęć z KR (np. `<합>`, `<회피>`) stosuj polskie cudzysłowy `„…”` lub `[…]` (np. `„Starcie”`, `„Unik”`), aby silnik Unity TMP nigdy nie zinterpretował `<s…>` / `<u…>` jako przekreślenia `<s>` lub podkreślenia `<u>`.
3. **Nie wpisuj nic w elementach oznaczonych `(powtórzenie elementu N — nie wpisuj tu nic…)`** — importer dziedziczy je automatycznie.
4. **Styl UI i kart**: zwięzły, precyzyjny, naturalny polski język gier RPG; bez anglicyzmów tam, gdzie istnieje czytelny odpowiednik, i z poszanowaniem podanego `limit: do N znaków`.
