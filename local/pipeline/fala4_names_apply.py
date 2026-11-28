#!/usr/bin/env python3
"""PRIORYTET-1 (2026-11-25) — nazwy przeciwników/skilli wg zasady usera:
- KR = fonetyczny zapis nazwy obcej -> zostaje zapis łaciński (EN 1:1, bez zmian);
- KR = konkretny koreański wyraz -> tłumaczenie polskie.
Zakres: wszystkie ledgery tlumaczenie/pliki/Enemies*.json + Skills_Enemy*.json
(stub pl==EN z EN w mapie) + piosenka BgmLyrics/BgmLyrics_Pv.json (22 seq).

Użycie: python3 local/pipeline/fala4_names_apply.py [--dry-run]
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.import_zwrotki import TranslationStore
from tools.package_views import compute_limit, encode_view_text, visible_len

ROOT = Path(__file__).resolve().parents[2]

# ---- indeks -> PL (klucze EN pobierane z local/fala4/base_todos.json) ----
IDX_PL = {
    0: "Główne Ciało",
    1: "Portret Pewnego Dnia",
    2: "Portret",
    3: "Marząca Elektryczna Owca",
    4: "Generator",
    5: "Król w Spętaniu",
    6: "Peccatulum Obżarstwa",
    7: "Tułów",
    8: "Były Szef Wydziału G Corp.",
    9: "Śpiwór Dni Przeszłych",
    10: "Czterysta Róż",
    11: "Strzelec Przeklętej Kuli",
    12: "Owoc",
    13: "Lewa Łodyga",
    14: "Prawa Łodyga",
    15: "Korzenie",
    16: "Lewe Ramię",
    17: "Prawe Ramię",
    18: "Twarz",
    19: "Lalka z Gliny Zagłady",
    20: "Płonąca Lalka z Gliny Zagłady",
    21: "Peccatulum Lenistwa",
    22: "Peccatulum Gniewu",
    23: "Nogi",
    24: "Fałszywe Jabłko",
    25: "Czy Zostałem Silniejszy? Naprawdę?",
    26: "Zrobiłem Się Mocny! Serio?",
    27: "Opętane Różowe Buciki",
    28: "Stuk-stuk? Marsz!",
    29: "Peccatulum Posępności",
    30: "Peccatulum Żądzy",
    31: "Peccatulum Pychy",
    32: "Sąsiad Zbudzony ze Snu",
    33: "Sąsiad Powstały Ponownie",
    34: "Zamierający z Zimna Niewolnik Kopalni",
    35: "Dygotający Niewolnik Kopalni",
    # 36 Baba Yaga — fonetyka, zostaje EN (skip)
    37: "Inkwizytor Idący Naprzód",
    38: "Czteronoga Bestia",
    39: "Inkwizytor Mający Wszystko",
    40: "Pełzający Inkwizytor",
    41: "Wijący Się Inkwizytor",
    42: "Wielka Paszcza",
    43: "Kromer Marząca o Ludzkiej Pełni",
    44: "Prawa Noga",
    45: "Lewa Noga",
    46: "Ogon",
    47: "Słup Energetyczny",
    48: "Człowiek",
    49: "Wijąca Się Bestia",
    50: "Głowokurczak a.k.a. Bongy",
    51: "Tata Bongy",
    52: "Kubeł Kurczaka",
    53: "Przyprawiony Tata Bongy",
    54: "Filmujący Dron K Corp.",
    55: "Lobotomy E.G.O::Mżawka - Dongbaek",
    56: "Dongbaek E.G.O::Kamelia",
    57: "Dongrang, Który Zaprzecza Wszystku",
    58: "Rozkwitłe E.G.O::Nadzorca Farmy",
    59: "Beczka Wina",
    60: "Stary Parasol",
    61: "Kwiat, Który Wkrótce Zakwitnie",
    62: "W Pełni Rozkwitły Kwiat",
    63: "Owoc Próżności",
    64: "Drzewo Próżności",
    65: "Uraza",
    66: "Drzewo Urazy",
    67: "Drzewo Pożądań",
    68: "Drzewo",
    69: "Chłonące Drzewo",
    70: "Wielki Liść",
    71: "Lewe Oko",
    72: "Prawe Oko",
    73: "Serce",
    74: "Serce Mieszkańca Miasteczka",
    75: "Posąg Buddy",
    76: "Kamienny Tron",
    77: "Forma, Którą Wypełnia Pustka",
    78: "Zwykły Wróg",
    79: "Zwabiony Guido",
    80: "Zwabiony Ayed",
    81: "Zwabiony Zgniły Szef Wydziału G Corp.",
    82: "Królowa Wróżek",
    83: "Zbitka Wróżek",
    84: "Umocniony Rozbity Żołnierz",
    85: "Zmroczony Rozbity Żołnierz",
    86: "Zacięty Rozbity Żołnierz",
    87: "Chuligan Liczący Liczby",
    88: "Ostry Chuligan",
    89: "Wygłodniały Chuligan",
    90: "Chuligan z Wielkim Łbem",
    91: "Rozgniewany Rozbity Żołnierz",
    92: "Zakłopotany Rozbity Żołnierz",
    93: "Obdarty Rozbity Żołnierz",
    94: "Podły Rozbity Żołnierz",
    95: "Brudnojęzyczny Rozbity Żołnierz",
    96: "Naostrzony Rozbity Żołnierz",
    97: "Zdeformowany Żołnierz Ze Wspomnień",
    98: "Rozpaczający Żołnierz Ze Wspomnień",
    99: "Skorodowany Żołnierz Ze Wspomnień",
    100: "Prowincjonalny Tingtangczyk",
    101: "Przechwalający Się Tingtangczyk",
    102: "Nienawidzący Fasoli Tingtangczyk",
    103: "Sztywny Ochroniarz Kasyna",
    104: "Pewny Siebie Ochroniarz Kasyna",
    105: "Skupiony Ochroniarz Kasyna",
    106: "Szef Ochroniarzy Kasyna",
    107: "Wesoły Członek Gangu Mariachi",
    108: "Ożywiony Członek Gangu Mariachi",
    109: "Zagrażający Członek Gangu Tieqiu",
    110: "Rozgrzewający Się Członek Gangu Tieqiu",
    111: "Spokojny Strażnik Punktu Kontrolnego K Corp.",
    112: "Cichy Strażnik Punktu Kontrolnego K Corp.",
    113: "Prostolinijny Strażnik Punktu Kontrolnego K Corp.",
    114: "Solidny Strażnik Punktu Kontrolnego K Corp.",
    115: "Hołdujący Inkwizytor N Corp.",
    116: "Uległy Inkwizytor N Corp.",
    117: "Służący Inkwizytor N Corp.",
    118: "Torturujący Inkwizytor N Corp.",
    119: "Przesłuchujący Inkwizytor N Corp.",
    120: "Sadystyczny Inkwizytor N Corp.",
    121: "Obsesyjny Inkwizytor N Corp.",
    122: "Najwyższej Radości Inkwizytor N Corp.",
    123: "Nieustraszony Inkwizytor N Corp.",
    124: "Skonfundowany Strażnik Punktu Kontrolnego K Corp.",
    125: "Przytłoczony Strażnik Punktu Kontrolnego K Corp.",
    126: "Oszołomiony Strażnik Punktu Kontrolnego K Corp.",
    127: "Oślepiony Strażnik Punktu Kontrolnego K Corp.",
    128: "Prymitywny Robot z Piłą",
    129: "Prymitywny Robot z Kulą Rozbiórkową",
    130: "Ukończony Robot z Piłą",
    131: "Ukończony Robot z Kulą Rozbiórkową",
    132: "Pewny Siebie Fikser Warsztatu Rosespanner",
    133: "Dumny Fikser Warsztatu Rosespanner",
    134: "Trzęsący Się Fikser Warsztatu Rosespanner",
    135: "Zastraszony Pracownik 1. Klasy K Corp.",
    136: "Zaniepokojony Pracownik 1. Klasy K Corp.",
    137: "Zhakowany Dron Regeneracyjny K Corp.",
    138: "Lobotomy E.G.O::Chlupotanie",
    139: "Lobotomy E.G.O::Czerwone Prześcieradło",
    140: "Ożywione Lobotomy E.G.O::Chlupotanie",
    141: "Ożywione Lobotomy E.G.O::Czerwone Prześcieradło",
    142: "Ożywiony Strażnik K Corp.",
    143: "Ożywiony Pracownik 1. Klasy K Corp.",
    144: "Ożywiony Pracownik 3. Klasy K Corp.",
    145: "Ożywiony Pracownik 3. Klasy K Corp. — Wzmocniony",
    146: "Wyobrażony Zbieracz 3. Klasy T Corp.",
    147: "Dron Zatrzymań K Corp.",
    148: "Przerażony Strażnik Punktu Kontrolnego K Corp.",
    149: "Trzęsący Się Strażnik Punktu Kontrolnego K Corp.",
    150: "Skamieniały Strażnik Punktu Kontrolnego K Corp.",
    151: "Skrępowany Strażnik Punktu Kontrolnego K Corp.",
    152: "Wróg-Boss",
    153: "Szef Wydziału G Corp. Ze Wspomnień — Zgniły",
    154: "Boss Gangu Tingtang",
    155: "Guido Wytrwały",
    156: "Solidny Robot Zespolony",
    157: "Rep Warsztatu Rosespanner Niko",
    158: "Lobotomy E.G.O::Czerwone Prześcieradło - Marile",
    159: "Ożywione Lobotomy E.G.O::Czerwone Prześcieradło - Marile",
    160: "Zwinny Wyznawca Głębin",
    161: "Wytrwały Wyznawca Głębin",
    162: "Biegacz Wybrzeża",
    163: "Ślizgacz Morskiej Niziny",
    164: "Żniwiarz Morskiej Niecki",
    165: "Założyciel Głębin",
    166: "Wydzielacz Głębin",
    167: "Urządzenie",
    168: "Dłoń Świętego",
    169: "Standardowy Wróg",
    # 170 Gimmick — fonetyka (기믹), zostaje EN (skip)
    171: "King Krab",
    172: "Ostry Krab",
    173: "Kolczasty Krab",
    174: "Twardy Krab",
    175: "Krab z Pociskami",
    176: "Krab z Bagnetem",
    177: "Unieszkodliwienie",
    178: "Zmiatanie",
    179: "Paskudny Atak",
    180: "Atak na Oślep",
    181: "Seria Pchnięć",
    182: "Głębienie Rany",
    183: "Wyczucie Słabości",
    184: "Nieudolna Rąbanka",
    185: "Skolcone Pchnięcie",
    186: "Słabiutkie Uderzenie",
    187: "Ciężki Cios",
    188: "Blok",
    189: "Blok Seryjny",
    190: "Zamach",
    191: "Paskudne Uderzenie",
    192: "Malutkie Marzenie",
    193: "Masywne Cięcie",
    194: "Kłucie",
    195: "Podłe Pchnięcie",
    196: "Wykryto Intruza!",
    197: "Ni z ruszenia!",
    198: "Ani kroku!",
    199: "Będzie Boleć!",
    200: "Intruz Namierzony",
    201: "Aresztowanie na Oślep",
    202: "Wykluczone",
    203: "Zatańczmy~",
    204: "Taniec Pokoju",
    205: "Pojedynek Taneczny",
    206: "Wesołe Pchnięcia",
    # 207 ¡Olé! — fonetyka, zostaje EN (skip)
    208: "Taniec Namiętności",
    209: "Porozrywam Cię na Strzępy",
    210: "Krwawe Powitanie",
    211: "Deszcz Obelg",
    212: "No!",
    213: "Na Co Patrzysz, Gało?",
    214: "Rozłupię Ci Ten Łeb",
    215: "Szturm",
    216: "Powstrzymanie",
    217: "Unieszkodliwienie Celu",
    218: "Aktywacja Pocisków HP",
    219: "Stłumienie",
    220: "Osłona",
    221: "Wbicie",
    222: "Gwoździowanie",
    223: "Stukanie",
    224: "Młotowanie",
    225: "Inkwizycja",
    226: "Surowe Gwoździowanie",
    227: "Agresywne Kazanie",
    228: "Ośmielasz Się!",
    229: "Zamaszyste Młotowanie",
    230: "Przytłaczające Kazanie",
    231: "Bezwzględna Inkwizycja",
    232: "Przebijający Gwóźdź",
    233: "Zbiórka",
    234: "Twarda Wiara",
    235: "Panujący Młot",
    236: "Jedność",
    237: "Masywna Inkwizycja",
    238: "Linia Śmierci",
    239: "Skrii",
    240: "Skriik",
    241: "Skriiiek",
    242: "Skrik!",
    243: "Skiek!",
    244: "Skrikiik",
    245: "Skriikki",
    246: "Początek Filmowania z Bliska",
    247: "Odwrot; Odwrot;",
    248: "Błysk; Błysk;",
    249: "Poszukuję słabości.",
    250: "Zatrzymuję ruch.",
    251: "Kroję.",
    252: "Skrobię.",
    253: "Ładuję… i strzelam",
    254: "Przygniatam.",
    255: "Piła… przygniata.",
    256: "Wejście w Tryb Obrony",
    257: "UWAGA, UWAGA: Niestabilność",
    258: "Zakręci Ci w Głowie",
    259: "Przyspieszenie Wibracji",
    260: "To Koniec!",
    261: "Zjedz To!",
    262: "Wzmocnienie Wibracji",
    263: "Koniec!",
    264: "Narastające Tarcie",
    265: "Zmielę Cię!",
    266: "Trzęs-Trzęs",
    267: "Powstrzymać Intruza",
    268: "Wstęp Wzbroniony",
    269: "Blokada Wejścia",
    270: "Krycie, Krycie!",
    271: "Pauza! Stój!",
    272: "Proszę Zatrzymać Się!",
    273: "Zatrzymuję!",
    274: "Zajmuję Osłonę!",
    275: "Podaję Ampułkę HP.",
    276: "Podaję Ampułkę Obrony.",
    277: "Wystrzał Ampułki Rozpadu, Wystrzał",
    278: "Rozpoczynam manewr uniku.",
    279: "Awaryjny Wystrzał Ampułki Rozpadu",
    280: "Ujawniam słabość, słabość.",
    281: "Proszę dalej walczyć.",
    282: "Proszę nie żałować sił.",
    283: "Odstępuję.",
    284: "Płyn Stłumienia",
    285: "Płyn Wybuchowy",
    286: "Chwiejny Płyn",
    287: "Płynna Osłona",
    288: "Raniąca Klątwa",
    289: "Rozrastająca Się Klątwa",
    290: "Rozwarta Rana",
    291: "Talizman Obrony",
    292: "Spętająca Klątwa",
    293: "Wyeksponowana Rana",
    294: "Wykryto Podejrzanych",
    295: "Blokada Podejrzanych",
    296: "Przeplatający Się Moment",
    297: "Pochłanianie Czasu",
    298: "Przyspieszający Moment",
    299: "Zatrzymuję.",
    300: "Rozdźwięk",
    301: "Rozkaz Obrony",
    302: "Fala Psychiczna",
    303: "Podcięcie Gardła",
    304: "Pokażę Ci, Co To Znaczy…!",
    305: "Iskrzące Marzenie",
    306: "Żarliwy Krok Taneczny",
    307: "To Wszystko, Co Masz?",
    308: "Ostro!",
    309: "Zwinnie~",
    # 310 Pañata Party~! — fonetyka (파냐타 파티), zostaje EN (skip)
    # 311 ¡Excelente! — fonetyka, zostaje EN (skip)
    312: "Wbicie Gwoździ",
    313: "Młoty, Słuchajcie Mnie…!",
    314: "Niezłomna Wiara",
    315: "Wielkie Dzieło Zostanie Spełnione…!",
    316: "Oczyść Się… z Grzechu!",
    317: "Ranię.",
    318: "Wykryto, Wykryto: Rana",
    319: "Wzmocnienie Drgnięć",
    320: "Zwalam.",
    321: "Ostrzegam, Ostrzegam: Drgnięcia",
    322: "Wykryto Słabość",
    323: "Oddaję przysługę.",
    324: "Proszę Się Odsunąć!",
    325: "Będzie Chwiejnie!",
    326: "Mocne Wzmocnienie",
    327: "Konwersja Wibracji",
    328: "Kompresja Wibracji",
    329: "Podbijmy Stawkę",
    330: "Ostatnie Rozgrzanie",
    331: "Klątwa Ciosów",
    332: "Mnożące Się Talizmany",
    333: "Paraliżująca Klątwa",
    334: "Duszący Talizman Klątwy",
    335: "Wygasający Talizman Klątwy",
    336: "Przenoszący Się Talizman Klątwy",
    337: "Gryzienie",
    338: "Natarcie",
    339: "Rozrzucanie Strzępów",
    340: "Skrawkowanie Życia",
    341: "Zbiór Substancji Odżywczych",
    342: "Rozcinający Zagryz",
    343: "Nieustanne Żerowanie",
    344: "Przebicie Życia",
    345: "Wyrzut",
}

# krmap reuse (kanon z wcześniejszych fal) — nadpisuje powyższe gdy KR się zgadza
KRMAP_REUSE = json.loads((ROOT / "local" / "fala4" / "base_krmap_hits.json").read_text(encoding="utf-8"))
# wyjątek: 'Shell' (KR 소라 w kontekście Trash Crab) — krmap 'Sora' pochodzi od imienia Sora
# (검지 제자 소라); dla części kraba poprawnie: Muszla.
KRMAP_REUSE.pop("Shell", None)
KRMAP_REUSE["Shell"] = "Muszla"

# ---- BgmLyrics_Pv (piosenka na koniec Prologu), seq -> PL (\n literalne) ----
SONG = {
    12241: "... Cmh.",
    12242: "Połknęliśmy czas\\nCofajmy",
    12243: "Zawodźcie\\nJeśli chciałeś, żebym żył",
    12244: "Jeśli chciałeś, żebym wybaczył",
    12245: "Jeśli chciałeś, byśmy udawali\\nludzi cywilizowanego społeczeństwa",
    12246: "W każdej pętli, w której umieramy\\n(w każdej pętli, w której umieramy)",
    12247: "Sprawiedliwość w moim wnętrzu,\\nhonor, który mnie broni,\\nusprawiedliwia mój grzech",
    12248: "Zawodźcie\\nCzemu śmierć przerywa mą torturę?",
    12249: "Czemu nikt nie może poczuć mojego bólu?",
    12250: "Czemu korona chwały\\nspada na najokrutniejszych?",
    12251: "W tym piekle\\n(w piekle)",
    12252: "Już odjeżdżamy, wrrum-wrrum.",
    12253: "Które sami zbudowaliśmy",
    12254: "W tym piekle wskrzeszając się nawzajem",
    12255: "Kierunek — piekło.",
    12256: "Szedłem drogą",
    12257: "Drogą prowadzącą w przeszłość",
    12258: "Z wyciągniętej gałęzi ukradłem coś",
    12259: "Przyjaciela żałujących\\n— zakazany owoc",
    12260: "Odgryzam skórkę\\nŻując jego czuły miąższ",
    12261: "Połknąłem kryjącą w środku letnią ropę",
    12262: "I stałeś się tym „mną”, którym tak gardziłeś.",
}


def load_pairs(prefix: str) -> dict[str, tuple[str | None, str | None]]:
    en_p = ROOT / f"index/localize/en/EN_{prefix}.json"
    kr_p = ROOT / f"index/localize/kr/KR_{prefix}.json"
    if not en_p.is_file() or not kr_p.is_file():
        return {}
    en = json.loads(en_p.read_text(encoding="utf-8"))
    kr = json.loads(kr_p.read_text(encoding="utf-8"))
    pairs: dict[str, tuple[str | None, str | None]] = {}
    dl_en = en.get("dataList", [])
    if dl_en and "levelList" in dl_en[0]:
        km: dict[str, str | None] = {}
        for x in kr.get("dataList", []):
            for lv in x.get("levelList", []):
                km[f'dataList[id={x["id"]}].levelList[level={lv["level"]}].name'] = lv.get("name")
        for x in dl_en:
            for lv in x.get("levelList", []):
                key = f'dataList[id={x["id"]}].levelList[level={lv["level"]}].name'
                pairs[key] = (lv.get("name"), km.get(key))
                if "desc" in lv:
                    pairs[f'dataList[id={x["id"]}].levelList[level={lv["level"]}].desc'] = (
                        lv.get("desc"),
                        None,
                    )
    else:
        km = {f'dataList[id={x["id"]}]': x for x in kr.get("dataList", [])}
        for x in dl_en:
            b = f'dataList[id={x["id"]}]'
            pairs[f"{b}.name"] = (x.get("name"), km.get(b, {}).get("name"))
            pairs[f"{b}.desc"] = (x.get("desc"), km.get(b, {}).get("desc"))
    return pairs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    todos = json.loads((ROOT / "local/fala4/base_todos.json").read_text(encoding="utf-8"))
    name_map: dict[str, str] = {}
    for i, (en_t, _kr_t) in enumerate(todos):
        if i in IDX_PL:
            name_map[en_t] = IDX_PL[i]
    for en_t, pl in KRMAP_REUSE.items():
        name_map[en_t] = pl
    for en_t, pl in name_map.items():
        if any(0xAC00 <= ord(c) <= 0xD7A3 for c in pl):
            print(f"HANGUL w PL dla {en_t!r}!")
            return 1

    store = TranslationStore.load(ROOT / "tlumaczenie")
    imported = collections.Counter()
    skipped_len = []
    for f in sorted((ROOT / "tlumaczenie/pliki").glob("Enemies*.json")) + sorted(
        (ROOT / "tlumaczenie/pliki").glob("Skills_Enemy*.json")
    ):
        base = f.name  # logical file name Z rozszerzeniem (konwencja store)
        pairs = load_pairs(f.stem)
        if not pairs:
            continue
        ledger = json.loads(f.read_text(encoding="utf-8"))["entries"]
        for addr, v in ledger.items():
            en_t, kr_t = pairs.get(addr, (None, None))
            if en_t is None:
                continue
            pl = v.get("pl", "")
            if not pl or pl != en_t:
                continue  # nie-stub albo brak
            new_pl = name_map.get(en_t)
            if new_pl is None:
                continue  # fonetyka/kod — zostaje EN
            lim = compute_limit(addr.split(".")[-1], encode_view_text(kr_t or ""), encode_view_text(en_t))
            if visible_len(new_pl.replace("\n", "\\n")) > lim:
                skipped_len.append((base, addr, new_pl, lim))
                continue
            imported[base] += 1
            if not args.dry_run:
                store.set_leaf(base, addr, new_pl, kr_t or "", en_t, "ai")

    # piosenka BgmLyrics_Pv
    scope = json.loads((ROOT / "local/fala4/scope.json").read_text(encoding="utf-8"))
    pv = [r for r in scope if r["fam"] == "BgmLyrics" and r["file"] == "BgmLyrics/BgmLyrics_Pv.json"]
    song_done = 0
    for rec in pv:
        pl = SONG.get(rec["seq"])
        if pl is None:
            print(f"BRAK piosenki dla seq {rec['seq']}")
            return 1
        lim = rec.get("lim", 120)
        if visible_len(pl) > lim:
            skipped_len.append(("BgmLyrics_Pv", rec["seq"], pl, lim))
            continue
        for lf, addr in rec["addrs"]:
            song_done += 1
            if not args.dry_run:
                store.set_leaf(lf, addr, pl, rec["kr"], rec["en"], "ai")

    print(f"nazwy: {sum(imported.values())} liści w {len(imported)} plikach | piosenka: {song_done} liści")
    for lf, n in sorted(imported.items()):
        print(f"  {lf:40s} {n}")
    if skipped_len:
        print(f"LEN-skip: {len(skipped_len)}")
        for s in skipped_len[:10]:
            print("  ", s)
    if args.dry_run:
        print("DRY-RUN OK — bez zapisu")
        return 0
    manifest = json.loads((ROOT / "tlumaczenie" / "MANIFEST.json").read_text(encoding="utf-8"))
    store.save_atomic(manifest)
    print("ZAPISANO tlumaczenie/ (atomic)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
