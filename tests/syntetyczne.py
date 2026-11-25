"""Wymyślone dane testowe w układzie Localize i zwrotu zbieracza (bez tekstów gry)."""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import zipfile


def _json(obj: object) -> bytes:
    # BOM jak w wielu plikach Unity — moduł ma go tolerować.
    return b"\xef\xbb\xbf" + json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")


def drzewo_localize() -> dict[str, bytes]:
    """Ścieżka względna od folderu Localize → bajty. Treść jest zmyślona."""
    pliki: dict[str, bytes] = {}
    for jezyk, prefiks, slowo in (("kr", "KR_", "가나다"), ("en", "EN_", "Lorem"), ("jp", "JP_", "あいう")):
        pliki[f"{jezyk}/{prefiks}MainUIText.json"] = _json(
            {"dataList": [{"id": "ui_start", "content": f"{slowo} start"},
                          {"id": "ui_quit", "content": f"{slowo} quit"}]}
        )
        pliki[f"{jezyk}/{prefiks}Skills_personality-01.json"] = _json(
            {"dataList": [{"id": 1, "levelList": [{"level": 1, "name": f"{slowo} cios", "desc": "",
                                                   "coinlist": [{"coindescs": [{"desc": f"{slowo} moneta"}]}]}]}]}
        )
        story = [{"id": 0, "model": "모델A", "teller": f"{slowo} narrator", "content": f"{slowo} jeden"},
                 {"id": 1, "content": f"{slowo} dwa", "place": f"{slowo} miejsce"},
                 {"id": -1, "content": ""},
                 {"id": -1, "content": ""}]
        pliki[f"{jezyk}/StoryData/{prefiks}S101B.json"] = _json({"dataList": story})
    # Plik tylko w jednym języku i plik z rozjechanymi id.
    pliki["en/EN_OnlyEnglish.json"] = _json({"dataList": [{"id": 5, "content": "Lorem only"}]})
    pliki["jp/JP_MainUIText.json"] = _json(
        {"dataList": [{"id": "ui_start", "content": "あいう start"}, {"id": "ui_other", "content": "x"}]}
    )
    pliki["kr/KR_Broken.json"] = b"{not json"
    pliki["en/EN_Broken.json"] = _json({"dataList": []})
    return pliki


def zapisz_drzewo(korzen: Path, pliki: dict[str, bytes]) -> None:
    for wzgledna, dane in pliki.items():
        sciezka = korzen / wzgledna
        sciezka.parent.mkdir(parents=True, exist_ok=True)
        sciezka.write_bytes(dane)


def zwrot_zbieracza(pliki: dict[str, bytes], *, tryb: str = "pelny", buildid: str = "123456",
                    lang_config: bytes | None = b'{"lang": "x"}', psuj: str | None = None) -> bytes:
    """Zbuduj ZIP w formacie ``lc-zbior-v1`` tak, jak robi to zbierz.ps1."""
    rekordy = []
    czlonki: dict[str, bytes] = {}
    for wzgledna, dane in sorted(pliki.items()):
        sciezka = "Assets/Resources_moved/Localize/" + wzgledna
        czlonki["pliki/" + sciezka] = dane
        rekordy.append({"sciezka": sciezka, "czlon": "pliki/" + sciezka, "rozmiar": len(dane),
                        "sha256": hashlib.sha256(dane).hexdigest()})
    if lang_config is not None:
        czlonki["pliki/Lang/config.json"] = lang_config
        rekordy.append({"sciezka": "Lang/config.json", "czlon": "pliki/Lang/config.json",
                        "rozmiar": len(lang_config), "sha256": hashlib.sha256(lang_config).hexdigest()})
    inwentarz = "".join(
        json.dumps({"p": r["sciezka"], "s": r["rozmiar"], "m": "2026-11-25T00:00:00Z"}) + "\n" for r in rekordy
    )
    raport = {
        "format": "lc-zbior-v1", "zbieracz": "LC_ZBIERZ_DANE 1.0.0", "tryb": tryb, "zbior_id": "abcdef01",
        "utworzono_utc": "2026-11-25T00:00:00Z", "czesc": 1, "czesci": 1,
        "gra": {"appid": "1973530", "buildid": buildid, "folder_gry": "Limbus Company"},
        "localize": {"istnieje": True, "jezyki": ["en", "jp", "kr"]},
        "lang": {"istnieje": True, "podfoldery": [], "config_json": lang_config is not None},
        "stan": {"uzyty": tryb == "aktualizacja", "plikow_w_stanie": 0, "niezmienione": 0, "usuniete": []},
        "inwentarz": {"w_tej_czesci": True, "wierszy": len(rekordy), "ograniczony": False},
        "wszystkie_czesci": [{"czesc": 1, "plikow": len(rekordy), "bajtow": sum(r["rozmiar"] for r in rekordy)}],
        "pliki": rekordy, "pominiete": [], "problemy": [], "stan_zbioru": "kompletny",
    }
    if psuj == "sha":
        raport["pliki"][0]["sha256"] = "0" * 64
    if psuj == "nadmiarowy":
        czlonki["pliki/Assets/Resources_moved/Localize/en/ukryty.exe"] = b"MZ"
    if psuj == "traversal":
        czlonki["../poza.json"] = b"{}"
    bufor = io.BytesIO()
    with zipfile.ZipFile(bufor, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for nazwa, dane in czlonki.items():
            zf.writestr(nazwa, dane)
        zf.writestr("INWENTARZ.jsonl", inwentarz)
        zf.writestr("RAPORT.json", json.dumps(raport, ensure_ascii=False, indent=2))
        zf.writestr("RAPORT.txt", "Stan: kompletny\r\n")
    return bufor.getvalue()
