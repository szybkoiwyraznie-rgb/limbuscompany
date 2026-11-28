#!/usr/bin/env python3
"""P84-REDO (2026-11-25) — redo decyzji P84 „Nazwy 1:1 (EN)" zgodnie z ZASADĄ NAZW usera:
- KR = fonetyczny zapis nazwy obcej -> zostaje zapis łaciński (EN 1:1);
- KR = konkretny koreański wyraz -> tłumaczenie polskie.
Zakres: kategorie z bloku P84 SŁOWNIKA — wszyscy „Refracted …" (Enemies*, Skills_*,
Passives_* — wszystkie ledgery), skilli „It Shall …", „… Gossypium", Master-portret,
lista „Additionally" (passives/parts), Hongyu. Prefiks 굴절된 = „Załamany/-a/-e"
(kanon krmap: Załamana Determinacja / Załamane Ładowanie / załamany pracownik poboru).
Wyjątki: NOTHING TO SEE HERE / LOOK AWAY! = dev-placeholder (KR „tekst, który nie
powinien się pojawić") — zostaje EN; Generator (발전기) = identyczne PL==EN — zostaje stub.

Użycie: python3 local/pipeline/fala4_p84_apply.py [--dry-run]
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

# ---- mapowanie EN -> PL (klucz = dokładny EN .name z indeksu; KR rozstrzyga) ----
P84_MAP: dict[str, str] = {
    # --- statusy/skilli z prefiksem Refracted (KR 굴절 출혈 부과 / 굴절된 X와 Y) ---
    "Apply Refracted Bleed": "Nakłada Załamane Krwawienie",
    "Apply Refracted Burn": "Nakłada Załamane Podpalenie",
    "Apply Refracted Rupture": "Nakłada Załamane Rozdarcie",
    "Apply Refracted Sinking": "Nakłada Załamane Zatonięcie",
    "Apply Refracted Tremor": "Nakłada Załamany Wstrząs",
    "Refracted Bleed and Tremor": "Załamane Krwawienie i Wstrząs",
    "Refracted Burn and Bleed": "Załamane Podpalenie i Krwawienie",
    "Refracted Burn and Rupture": "Załamane Podpalenie i Rozdarcie",
    "Refracted Rupture and Sinking": "Załamane Rozdarcie i Zatonięcie",
    "Refracted Charge": "Załamane Ładowanie",  # krmap exact: 굴절된 충전
    # --- wrogowie Refracted: kotwica/morskie (Canto 5 / MD5) ---
    "Refracted Ahab": "Załamany Ahab",
    "Refracted Queequeg": "Załamany Queequeg",
    "Refracted Starbuck": "Załamany Starbuck",
    "Refracted Dulcinea": "Załamana Dulcynea",  # krmap: 돌시네아=Dulcynea
    "Refracted Twinhook Pirates First Mate Smee": "Załamany Pierwszy Oficer Piratów Podwójnego Haka Smee",
    "Refracted Agile Twinhooks Pirate": "Załamany Zwinny Pirat Podwójnego Haka",
    "Refracted Bandana-wearing Twinhooks Pirate": "Załamany Pirat Podwójnego Haka w Bandanie",
    "Refracted Moustachioed Twinhooks Pirate": "Załamany Pirat Podwójnego Haka z Wąsami",
    "Refracted Tough Twinhooks Pirate": "Załamany Krzepki Pirat Podwójnego Haka",
    "Refracted Blinded Pequod Town Villager": "Załamany Oślepiony Mieszkaniec Miasteczka Pequod",
    "Refracted Gagged Pequod Town Villager": "Załamany Zakneblowany Mieszkaniec Miasteczka Pequod",
    "Refracted Pallid Blue Mermaid": "Załamana Blada Błękitna Syrena",
    "Refracted Pallid White Mermaid": "Załamana Blada Biała Syrena",
    "Refracted Pallid Entwined Mermaid": "Załamana Blada Splątana Syrena",
    "Refracted Pallid and Blue Mermaid": "Załamana Blada i Błękitna Syrena",
    "Refracted Whale of the Porous Hand Mermaid": "Załamana Syrena Wieloryb Porowatej Dłoni",
    "Refracted Whale of the Porous Hand Soldier Mermaid": "Załamana Syrena Żołnierz Wieloryb Porowatej Dłoni",
    "Refracted Whale of the Thousand Strands Mermaid": "Załamana Syrena Wieloryb Tysiąca Pasem",
    "Refracted Pallidified Thing-Club": "Załamana Zbielała Rzecz-Maczuga",
    "Refracted Pallidified Thing-Hook": "Załamany Zbielały Rzecz-Hak",
    "Refracted Pallidified Thing-Pirate": "Załamany Zbielały Rzecz-Pirat",
    "Refracted Pallidified Thing-Shield": "Załamana Zbielała Rzecz-Tarcza",
    "Refracted Flotsam": "Załamany Dryfujący Przedmiot",
    "Refracted Ambling Pearl": "Załamana Krocząca Perła",  # krmap: 걷는 진주
    "Refracted Barbed Lasso": "Załamane Kolczaste Lasso",  # krmap: 가시 올가미
    "Refracted Shock Centipede": "Załamana Wstrząsowa Stonoga",  # krmap: 충격 지네
    "Refracted Dream-Devouring Siltcurrent": "Załamany Pożerający Sny Nurt Mułu",
    "Refracted Dreaming Electric Sheep": "Załamana Śniąca Elektryczna Owca",  # krmap: 꿈을 꾸는 전기양
    "Refracted Skin Prophet": "Załamany Prorok Skóry",  # krmap: 살갗=Skóra
    "Refracted Steam Transport Machine": "Załamana Maszyna Transportująca Parę",
    "Refracted Wayward Passenger": "Załamany Zbłąkany Pasażer",  # ThreadDungeon kanon
    "Refracted Egress": "Załamane Wyjście",  # krmap 출구=Wyjście
    "Refracted Headless Ichthys": "Załamany Bezgłowy Ichtis",  # krmap: 단수어
    "Refracted Alleyway Watchdog": "Załamany Pies Stróżujący Zaułków",  # krmap: 골목파수견
    "Refracted Drifting Fox": "Załamany Błędny Lis",  # krmap: 떠돌이 여우
    # --- wrogowie Refracted: Parade / Krew (Canto 7) ---
    "Refracted Bloodbag of the Painful Parade": "Załamany Worek Krwi Bolesnej Parady",
    "Refracted Bloodbag of the Rear Parade": "Załamany Worek Krwi Tylnej Parady",
    "Refracted Despairing Bloodbag": "Załamany Rozpaczający Worek Krwi",
    "Refracted Disgraced Bloodbag": "Załamany Upadły Worek Krwi",
    "Refracted Bloodfiend of the Happy Parade": "Załamany Krwiożerca Szczęśliwej Parady",
    "Refracted Bloodfiend of the Joyful Parade": "Załamany Krwiożerca Wesołej Parady",
    "The Refracted Barber": "Załamany Fryzjer",  # krmap: 이발사=Fryzjer
    "Refracted Josephine": "Załamana Josephine",  # krmap: 조세핀
    "Refracted Nelly": "Załamana Nelly",  # krmap: 넬리
    "Refracted Hindley, The Reaved Lamenter": "Załamany Hindley, Rozxebrany Zawodzący",
    "Refracted Hongyu, the Crimson Jade [紅玉]": "Załamany Hongyu, Szkarłatny Jadeit [紅玉]",
    # --- wrogowie Refracted: Kurokumo / Edgar / Wuthering (Canto 1/3/6) ---
    "Refracted Adept Kurokumo Henchwoman": "Załamana Biegła Członkini Klanu Kurokumo",
    "Refracted Determined Kurokumo Henchman": "Załamany Zdecydowany Członek Klanu Kurokumo",
    "Refracted Tense Kurokumo Henchman": "Załamany Napięty Członek Klanu Kurokumo",
    "Refracted Tired Kurokumo Henchwoman": "Załamana Senna Członkini Klanu Kurokumo",
    "Refracted Kurokumo Clan Captain Jun": "Załamany Jun, Kapitan Klanu Kurokumo",
    "Refracted Fast Edgar Family Butler": "Załamany Żwawy Kamerdyner Rodu Edgarów",
    "Refracted Shifty Edgar Family Butler": "Załamany Przebiegły Kamerdyner Rodu Edgarów",
    "Refracted Swift Edgar Family Butler": "Załamany Gibki Kamerdyner Rodu Edgarów",
    "Refracted Trained Edgar Family Butler": "Załamany Wyćwiczony Kamerdyner Rodu Edgarów",
    "Refracted Veteran Edgar Family Butler": "Załamany Doświadczony Kamerdyner Rodu Edgarów",
    "Refracted Hostile Wuthering Heights Butler": "Załamany Wrogi Kamerdyner Wichrowych Wzgórz",
    "Refracted Trained Wuthering Heights Butler": "Załamany Zahartowany Kamerdyner Wichrowych Wzgórz",
    "Refracted Old G Corp. Head Manager": "Załamany Były Szef Wydziału G Corp.",
    "Refracted T Corp. Class 3 Collector": "Załamany Zbieracz 3. Klasy T Corp.",
    "Refracted Distorted Hohenheim": "Załamany Distorted Hohenheim",  # Distorted=왜곡 canon EN-literal
    "Refracted Downcast Veteran": "Załamany Zmroczony Rozbity Żołnierz",  # 패잔병 kanon PRIORYTET-1
    # --- wrogowie Refracted: Ring / palec-korpusy (Canto 6/7) ---
    "Refracted Enamored Researcher of the Ring?": "Załamany Zachwycony Badacz Serdecznego?",
    "Refracted Mad Researcher of the Ring?": "Załamany Obłąkany Badacz Serdecznego?",
    "Refracted Pointillist Researcher of the Ring?": "Załamany Punktysystyczny Badacz Serdecznego?",
    "The Refracted Index Nursefather - Rien": "Załamany Ojciec Wskazującego - Rien",  # kanon 'Ojciec Wskazującego'
    "The Refracted Pinky Nursefather - Shiomi Yoru": "Załamany Ojciec Małego Palca - Shiomi Yoru",  # krmap: 소지 아비
    "The Refracted Ring Nursefather - Callisto": "Załamany Ojciec Serdecznego - Callisto",
    "The Refracted Ring Apprentice - Albina": "Załamana Uczennica Serdecznego - Albina",
    "The Refracted Priest": "Załamany Ksiądz",  # krmap: Priest=Ksiądz
    "The Refracted King in Binds": "Załamany Król w Spętaniu",  # krmap: 묶인 왕
    "Refracted Combative Fanghunt Office Fixer": "Załamany Bojowy Fikser Biura Łowców Kłów",
    "Refracted Prideful Fanghunt Office Fixer": "Załamany Dumny Fikser Biura Łowców Kłów",
    "Refracted Der Fluchschütze": "Załamany Strzelec Przeklętej Kuli",  # kanon base
    "Refracted Old Umbrella": "Załamany Stary Parasol",  # krmap: 낡은 우산
    "Refracted Fairy Gentleman": "Załamany Wróżkowy Dżentelmen",  # krmap
    "Refracted Fairy Wine": "Załamane Wino Wróżek",  # krmap: 요정주
    "Refracted Fairy-Long-Legs": "Załamana Długonoga Wróżka",  # krmap
    "Refracted Faelantern": "Załamana Wróżkowa Latarnia",  # krmap: 요정초롱
    "Refracted Ardor Blossom Moth": "Załamana Ćma Szkarłatnego Płomienia",  # ThreadDungeon kanon: 홍염나방
    "Refracted Electrifying Dimension": "Załamany Wymiar Tryskający Prądem",
    "Refracted Hemorrhaging Dimension": "Załamany Krwawiący Wymiar",
    "Refracted Poisonous Dimension": "Załamany Wymiar Wrzącej Trucizny",
    "Refracted Tremoring Dimension": "Załamany Nieustannie Wibrujący Wymiar",
    "Refracted Envy-drenched Rose": "Załamana Róża Nasiąknięta Zazdrością",
    "Refracted Gloom-drenched Rose": "Załamana Róża Nasiąknięta Posępnością",
    "Refracted Gluttony-drenched Rose": "Załamana Róża Nasiąknięta Obżarstwem",
    "Refracted Lust-drenched Rose": "Załamana Róża Nasiąknięta Żądzą",
    "Refracted Pride-drenched Rose": "Załamana Róża Nasiąknięta Pychą",
    "Refracted Sloth-drenched Rose": "Załamana Róża Nasiąknięta Lenistwem",
    "Refracted Wrath-drenched Rose": "Załamana Róża Nasiąknięta Gniewem",
    "Refracted Green Slime": "Załamany Zielony Śluz",  # krmap
    "Refracted Rose Hunter": "Załamany Łowca Róż",  # krmap
    "Refracted So That No One Will Cry": "Załamany By Nikt Nie Płakał",  # krmap
    "Refracted Sleeping Bag of a Bygone Day": "Załamany Śpiwór Dni Przeszłych",  # krmap
    "Refracted Spiral of Contempt": "Załamana Spirala Pogardy",  # krmap/P84: 경멸의 나선
    "Refracted Portrait": "Załamany Portret",
    "Refracted Portrait of a Certain Day": "Załamany Portret Pewnego Dnia",
    "Refracted Four-hundred Roses": "Załamane Czterysta Róż",  # kanon base
    "Refracted Sign of Roses": "Załamany Znak Róż",
    "Refracted Flower-burying Pin": "Załamany Klin Pogrzebania Kwiatów",  # krmap: 매화첨[埋花櫼]
    "Refracted Candle": "Załamana Świeca",  # P84 kanon: Candle=Świeca
    "Refracted Grasp": "Załamany Uchwyt",  # krmap Refraction3: Grasp=Uchwyt
    "Refracted Struggle": "Załamane Zmagania",
    "Refracted Sin": "Załamany Grzech",
    "Refracted Generator": "Załamany Generator",
    "Refracted Clover": "Załamany Clover",  # 클로버 fonetyka -> Latin
    "Refracted Yinglong": "Załamany Yinglong",  # krmap: 응룡=Yinglong
    "Refracted Hurting Teddy Bear": "Załamany Cierpiący Teddy",  # KR: 아파하는 테디
    "Refracted Will You Play?": "Załamany Zagrasz ze Mną?",  # KR: 놀아줄래
    "Refracted Effloresced E.G.O::GasHarpoon": "Załamane Rozkwitłe E.G.O::GasHarpoon",  # 개화 E.G.O -> Rozkwitłe E.G.O
    # --- Butterfly of Entangled Lives (krmap: 나생 -> Splątany Żywot) ---
    "Refracted Butterfly of Entangled Lives::Imago": "Załamany Motyl Splątanego Żywotu::Imago",
    "Refracted Butterfly of Entangled Lives::The Pupa": "Załamany Motyl Splątanego Żywotu::Poczwarka",
    "Refracted Illusory Butterfly of Entangled Lives::The Past": "Załamany Iluzoryczny Motyl Splątanego Żywotu::Przeszłość",
    "Refracted Illusory Butterfly of Entangled Lives::The Present": "Załamany Iluzoryczny Motyl Splątanego Żywotu::Teraźniejszość",
    "Refracted Illusory Butterfly of Entangled Lives::The Future": "Załamany Iluzoryczny Motyl Splątanego Żywotu::Przyszłość",
    # --- Peccatulum (marka łac. wg krmap, gatunek po polsku — kanon P180) ---
    "Refracted Peccatulum Invidiae": "Załamane Peccatulum Zazdrości",
    "Refracted Peccatulum Invidiae?": "Załamane Peccatulum Zazdrości?",
    "Refracted Peccatulum Irae??": "Załamane Peccatulum Gniewu??",
    "Refracted Peccatulum Morositatis??": "Załamane Peccatulum Posępności??",
    "Refracted Peccatulum Pigritiae??": "Załamane Peccatulum Lenistwa??",
    # --- skilli „It Shall …" (KR czasowniki z archaicznymi końcówkami -지어다/-지니) ---
    "It Shall Constrict": "Skuje",
    "It Shall Grip": "Uściska",
    "It Shall Penetrate": "Przebijie",
    "It Shall Shun": "Ominie",
    "It Shall Be Insidious": "Powoli Wsiąknie",
    "And it Shall Contempt All": "I Wszystkim Pogardzi",
    # --- „… Gossypium" (KR 목화 = Bawełna, kanon krmap) ---
    "Encroaching Gossypium": "Zalewająca Bawełna",
    "Flourishing Gossypium": "Pokrywająca Bawełna",
    "Flowering Gossypium": "Rozkwitająca Bawełna",
    "Scattering Gossypium": "Rozsypująca Się Bawełna",
    "Scattering Red-stained Gossypium": "Rozsypująca Się Czerwono Ubarwiona Bawełna",
    "Drenched Gossypium": "Nasiąknięta Bawełna",  # krmap: 머금은 목화
    "Refracted Drenched Gossypium": "Załamana Nasiąknięta Bawełna",
    # --- Master-portret (krmap: 주인님=Pan, 잔상=Powidło) ---
    "Master's Portrait": "Portret Pana",
    "My Master": "Mój Pan",
    "Master...?": "Panie...?",
    "Ooh, Dear Master...": "Ach, Panie…",
    "Portrait Afterimage Sighting": "Dostrzeżenie Powidła Portretu",
    # --- Additionally: passives/parts (KR konkretne) ---
    "Uncovered Abyss": "Odsłonięta Otchłań",  # krmap: 심연=Otchłań
    "Broken Stump": "Zniszczony Pniak",
    "Evolving Lure": "Ewoluujący Wabik",  # krmap: 미끼=Wabik
    "Fairy Dust": "Pył Wróżek",
    "Fairy Wine": "Wino Wróżek",  # krmap exact
    "Enticing Fairy Wine": "Wymarzone Wino Wróżek",
    "Deteriorated Persistence": "Podupadła Siła Życiowa",
    "Solid Exoskeleton": "Twardy Pancerz",
    "Living Nerves": "Żywe Nerwy",
    "Reminisced Augmentation": "Wspomniane Wzmocnione Ciało",
    "Lost Means": "Utracone Środki",
    "Damaged Shade": "Uszkodzony Cień",  # krmap: 그늘=Cień
    "Contaminating Leaf": "Skażające Liście",
    "Contaminating Slime": "Skażający Śluz",
    "Gathering Slime": "Zbierający Się Śluz",
    "Dimensional Escape": "Wymiarowa Ucieczka",
    "Trapped Dimensional Escape": "Uwięziona Wymiarowa Ucieczka",
    "Regenerate Dimensional Refraction Blade": "Odbudowa Wymiarowego Ostrza Załamania",
    "Forced Dimensional Breach Attempt - Partial Deterrence Release": "Próba Wymuszonego Otwarcia Wymiaru - Częściowe Zwolnienie Powstrzymania",
    "Eternal Yoke": "Wieczna Uzda",  # krmap exact: 굴레=Uzda
    "Broken Sign": "Rozbity Znak",
    "Scattered Flesh": "Rozproszone Kawałki Ciała",
    "Singular Vine": "Pojedyncza Winorośl",
    "Sin-drenched Brambles": "Ciernie Nasiąknięte Grzechem",
    "Blossoming Sins": "Rozkwitłe Grzechy",
    "Rose on a Vine": "Róża na Winorośli",
    "Shimmering Lust": "Drgająca Żądza",
    "Shimmering Gloom": "Drgająca Posępność",
    "Powerless": "Bezsilność",
    "Crushing Sloth": "Miażdżące Lenistwo",
    "Growing Gluttony": "Rozrastające się Obżarstwo",
    "Self Destruction": "Samozniszczenie",
    "Overinflated Pride": "Nadmuchana Pycha",
    "Glaring Envy": "Błyskająca Zazdrość",
    "Injected Hatred and Animosity": "Wstrzyknięta Nienawiść i Wrogość",
    "Flaming Ember": "Płonący Ognik",
    "Interlocking Ardor Blossom": "Zazębujący się Szkarłatny Płomień",
    "The Last Ember": "Ostatni Ognik",
    "Exposed Pearl": "Obnażona Perła",
    "Underwater Breathing": "Oddychanie Pod Wodą",
    "Melee Combat": "Walka Wręcz",
    "Charge Forth": "Szarża",
    "Deep Breath": "Głęboki Wdech",  # krmap exact: 깊은 들숨
    "Hands": "Ręce",
    "Wings": "Skrzydła",  # krmap: 날개
    "Stuffed Toy": "Pluszowa Zabawka",  # krmap: 봉제인형=Pluszowa Zabawka
    "Prone": "Kucnięcie",  # KR: 웅크리기
    "Wound": "Zadanie Rany",  # KR: 상처내기
}


def load_pairs(prefix: str) -> dict[str, tuple[str | None, str | None]]:
    """EN/KR źródła z indeksów (utf-8-sig: część indeksów ma BOM)."""
    en_p = ROOT / f"index/localize/en/EN_{prefix}.json"
    kr_p = ROOT / f"index/localize/kr/KR_{prefix}.json"
    if not en_p.is_file() or not kr_p.is_file():
        return {}
    en = json.loads(en_p.read_text(encoding="utf-8-sig"))
    kr = json.loads(kr_p.read_text(encoding="utf-8-sig"))
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
    else:
        km2 = {f'dataList[id={x["id"]}]': x for x in kr.get("dataList", [])}
        for x in dl_en:
            b = f'dataList[id={x["id"]}]'
            pairs[f"{b}.name"] = (x.get("name"), km2.get(b, {}).get("name"))
    return pairs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    for en_t, pl in P84_MAP.items():
        if any(0xAC00 <= ord(c) <= 0xD7A3 for c in pl):
            print(f"HANGUL w PL dla {en_t!r}!")
            return 1

    store = TranslationStore.load(ROOT / "tlumaczenie")
    imported = collections.Counter()
    skipped_len = []
    for f in sorted((ROOT / "tlumaczenie/pliki").glob("**/*.json")):
        base = f.name  # logical name Z rozszerzeniem (konwencja store)
        rel = f.relative_to(ROOT / "tlumaczenie/pliki").as_posix()
        prefix = rel[: -len(".json")]
        pairs = load_pairs(prefix)
        if not pairs:
            continue
        ledger = json.loads(f.read_text(encoding="utf-8-sig"))["entries"]
        for addr, v in ledger.items():
            if not addr.endswith(".name"):
                continue  # P84 = tylko nazwy
            en_t, kr_t = pairs.get(addr, (None, None))
            if en_t is None:
                continue
            pl = v.get("pl", "")
            if not pl or pl != en_t:
                continue  # nie-stub
            if en_t in {"NOTHING TO SEE HERE", "LOOK AWAY!"}:
                continue  # dev-placeholder — celowo EN
            new_pl = P84_MAP.get(en_t)
            if new_pl is None or new_pl == en_t:
                continue  # poza mapą albo identyczne PL==EN (Generator)
            lim = compute_limit(addr.split(".")[-1], encode_view_text(kr_t or ""), encode_view_text(en_t))
            if visible_len(new_pl.replace("\n", "\\n")) > lim:
                skipped_len.append((base, addr, new_pl, lim))
                continue
            imported[base] += 1
            if not args.dry_run:
                store.set_leaf(base, addr, new_pl, kr_t or "", en_t, "ai")

    total = sum(imported.values())
    uniq = len({e for e in P84_MAP})
    print(f"nazwy P84: {total} liści w {len(imported)} plikach (mapa: {uniq} EN)")
    for lf, n in sorted(imported.items()):
        print(f"  {lf:45s} {n}")
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
