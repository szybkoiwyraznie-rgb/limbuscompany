#!/usr/bin/env python3
"""Dump/apply/krmap helpers for provisional AI batch (paczka) Markdown files.

Subcommands:
  dump   <paczka.md> [--json OUT] [--work OUT]   — parse TODO paczka into per-seq records
  apply  <paczka.md> <allp.json> --out OUT.md    — fill PL values into a copy of the paczka
  krmap  [--out OUT.json]                        — rebuild KR->PL map from index+tlumaczenie
  krmatch <paczka.md> <krmap.json> --out OUT.json — prefill seqs whose KR already has a PL
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

ENTRY_RE = re.compile(r"^(\d+)\. \[(.*?)\] (.*)$")
SECTION_RE = re.compile(r"^## (.*?) \[(.*?)\] — (\S+)$")
LIMIT_RE = re.compile(r"^   limit: do (\d+) znak")
REPEAT_RE = re.compile(r"^   \(powtórzenie elementu (\d+)")
TOKEN_RE = re.compile(r"\{[0-9]+\}|<color=[^>]*>|</color>|\\n")


def parse_paczka(path: Path) -> dict[int, dict]:
    entries: dict[int, dict] = {}
    section = ("", "", "")
    cur = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = SECTION_RE.match(raw)
        if m:
            section = (m.group(1), m.group(2), m.group(3))
            continue
        m = ENTRY_RE.match(raw)
        if m:
            seq = int(m.group(1))
            cur = {
                "seq": seq,
                "sect": section[0],
                "layer": section[1],
                "file": section[2],
                "key": m.group(2),
                "kr": m.group(3),
                "lim": None,
                "tok": "",
                "en": "",
                "repeat": None,
            }
            entries[seq] = cur
            continue
        if cur is None:
            continue
        m = LIMIT_RE.match(raw)
        if m:
            cur["lim"] = int(m.group(1))
            continue
        m = REPEAT_RE.match(raw)
        if m:
            cur["repeat"] = int(m.group(1))
            continue
        if raw.startswith("   EN: "):
            cur["en"] = raw[7:]
    for cur in entries.values():
        cur["tok"] = ", ".join(sorted(set(TOKEN_RE.findall(cur["kr"]))))
    return entries


def clean_kr(kr: str) -> str:
    m = re.match(r"^— [^\]]*\]\s?", kr)
    return kr[m.end():] if m else kr


def cmd_dump(args: argparse.Namespace) -> int:
    entries = parse_paczka(Path(args.paczka))
    lines = []
    for seq in sorted(entries):
        if args.skip_repeats and entries[seq]["repeat"] is not None:
            continue
        e = entries[seq]
        lines.append(f"### {seq} (L{e['lim']}) {e['sect']} [{e['layer']}] — {e['file']}")
        lines.append(f"TOK: {e['tok']}")
        lines.append(f"KR: {e['kr']}")
        if e["repeat"] is not None:
            lines.append(f"REPEAT: {e['repeat']} — inherit")
        else:
            lines.append(f"EN: {e['en']}")
        lines.append("")
    out = "\n".join(lines) + "\n"
    if args.json:
        Path(args.json).write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    if args.work:
        Path(args.work).write_text(out, encoding="utf-8")
    sys.stdout.write(out)
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    src = Path(args.paczka)
    entries = parse_paczka(src)
    values = json.loads(Path(args.allp).read_text(encoding="utf-8"))
    need = [seq for seq, e in entries.items() if e["repeat"] is None]
    missing = [seq for seq in need if str(seq) not in values]
    extra = [k for k in values if int(k) not in entries]
    on_repeat = [k for k in values if entries[int(k)]["repeat"] is not None]
    if missing or extra or on_repeat:
        print(f"BŁĄD: missing={missing[:20]} extra={extra[:20]} on_repeat={on_repeat[:20]}")
        return 1
    out_lines = []
    cur = None
    filled = 0
    for raw in src.read_text(encoding="utf-8").splitlines():
        m = ENTRY_RE.match(raw)
        if m:
            cur = int(m.group(1))
            out_lines.append(raw)
            continue
        if raw == "   PL:" and cur is not None and entries[cur]["repeat"] is None:
            out_lines.append("   PL: " + values[str(cur)])
            filled += 1
            continue
        out_lines.append(raw)
    out = "\n".join(out_lines) + "\n"
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(out, encoding="utf-8")
    status = "OK" if filled == len(need) else "[NIEPELNE!]"
    print(f"Zapisano {args.out}: wpisano={filled}, oczekiwano={len(need)} {status}")
    return 0 if filled == len(need) else 1


def cmd_krmap(args: argparse.Namespace) -> int:
    from tools.localize import Snapshot, iter_strings

    kr_map: dict[str, str] = {}
    pl_dir = ROOT / "tlumaczenie" / "pliki"
    tl_files = sorted(pl_dir.rglob("*.json"))
    with Snapshot.open(ROOT / "index" / "localize") as snap:
        kr_files = snap.files.get("kr", {})
        paired = 0
        for pl_path in tl_files:
            logical = str(pl_path.relative_to(pl_dir))
            if logical not in kr_files:
                continue
            paired += 1
            kr_data = json.loads(snap.read("kr", logical).decode("utf-8-sig"))
            pl_data = json.loads(pl_path.read_text(encoding="utf-8"))
            if isinstance(pl_data, dict) and isinstance(pl_data.get("entries"), dict):
                pl_data = pl_data["entries"]
            if not isinstance(pl_data, dict):
                continue
            kr_strings = dict(iter_strings(kr_data))
            for address, meta in pl_data.items():
                if not isinstance(meta, dict):
                    continue
                pl = meta.get("pl")
                if not pl:
                    continue
                kr_text = kr_strings.get(address)
                if kr_text is None:
                    continue
                key = kr_text.replace("\n", "\\n")
                if key not in kr_map:
                    kr_map[key] = pl.replace("\n", "\\n")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(kr_map, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"krmap: {len(kr_map)} KR->PL z {paired} sparowanych plików -> {out}")
    return 0


def cmd_krmatch(args: argparse.Namespace) -> int:
    entries = parse_paczka(Path(args.paczka))
    kr_map = json.loads(Path(args.krmap).read_text(encoding="utf-8"))
    hits = {}
    for seq in sorted(entries):
        e = entries[seq]
        if e["repeat"] is not None:
            continue
        pl = kr_map.get(clean_kr(e["kr"]))
        if pl is not None:
            hits[str(seq)] = pl
    Path(args.out).write_text(json.dumps(hits, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"krmatch: {len(hits)} / {sum(1 for e in entries.values() if e['repeat'] is None)} -> {args.out}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("dump")
    d.add_argument("paczka")
    d.add_argument("--json")
    d.add_argument("--work")
    d.add_argument("--skip-repeats", action="store_true")
    d.set_defaults(func=cmd_dump)

    a = sub.add_parser("apply")
    a.add_argument("paczka")
    a.add_argument("allp")
    a.add_argument("--out", required=True)
    a.set_defaults(func=cmd_apply)

    k = sub.add_parser("krmap")
    k.add_argument("--out", default=str(ROOT / "local" / "krmap.json"))
    k.set_defaults(func=cmd_krmap)

    m = sub.add_parser("krmatch")
    m.add_argument("paczka")
    m.add_argument("krmap")
    m.add_argument("--out", required=True)
    m.set_defaults(func=cmd_krmatch)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
