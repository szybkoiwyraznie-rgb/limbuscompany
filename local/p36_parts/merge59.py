# -*- coding: utf-8 -*-
import json, re, importlib.util, sys

D = json.load(open('/home/user/limbuscompany/local/praca_ai/P59/parsed.json'))
KEYP = json.load(open('/home/user/limbuscompany/local/praca_ai/P59/krmatch.json'))
ROOT = '/home/user/limbuscompany'

FILES = ['build59_%d.py' % i for i in range(1, 22)]
PARTS = []
for fn in FILES:
    spec = importlib.util.spec_from_file_location(fn[:-3], ROOT + '/local/p36_parts/' + fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    PARTS.extend((seq, pl.replace(chr(10), '\\n')) for seq, pl in m.PART)

for seq in KEYP:
    PARTS.append((int(seq), KEYP[seq]))

seen = {}
for seq, pl in PARTS:
    if seq in seen and seen[seq] != pl:
        print('DUP CONFLICT', seq, repr(seen[seq])[:40], repr(pl)[:40]); sys.exit(1)
    seen[seq] = pl

nonrepeat = {int(s) for s, e in D.items() if e.get('en')}
dropped = sorted(set(seen) - nonrepeat)
seen = {k: v for k, v in seen.items() if int(k) in nonrepeat}
missing = sorted(nonrepeat - set(seen))
phantom = sorted(set(seen) - nonrepeat)
print('non-repeat:', len(nonrepeat), '| merged:', len(seen), '| dropped EN-empty repeats:', len(dropped))
print('missing:', missing)
print('phantom:', phantom)

TMP_TAG = re.compile(
    r"</?(?:(?:i|b|u|s|br|sup|sub|nobr|noparse)|(?:color|size|sprite|link|style|font|mark|align|ruby|voffset|line-height|cspace|material)(?:[= ][^<>]*)?)>",
    re.I)

def visible_len(s):
    return len(TMP_TAG.sub('', s.replace('\\n', '\n')))

strip_prefix = re.compile(r'^— [^\]]*\]\s?')
sc = lambda s: re.sub(r'<[^>]+>', '', s)

bad_len, bad_hangul, bad_tags, bad_num, bad_tok, bad_nl = [], [], [], [], [], []
for seq, pl in sorted(seen.items()):
    e = D.get(str(seq))
    if not e or not e.get('en'):
        continue
    kr = strip_prefix.sub('', e['kr'])
    lim = e.get('lim') or 120
    v = visible_len(pl)
    if v > lim:
        bad_len.append((seq, lim, v, pl[:60]))
    if re.search(r'[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]', pl):
        bad_hangul.append(seq)
    krtags = set(re.findall(r'\[([A-Za-z_0-9]+)\]', kr))
    pltags = set(re.findall(r'\[([A-Za-z_0-9]+)\]', pl))
    if krtags - pltags:
        bad_tags.append((seq, sorted(krtags - pltags)))
    kd, pd = set(re.findall(r'\d+', sc(kr))), set(re.findall(r'\d+', sc(pl)))
    if kd - pd:
        bad_num.append((seq, sorted(kd - pd), kr[:60]))
    krt, plt = set(re.findall(r'\{\d+\}', kr)), set(re.findall(r'\{\d+\}', pl))
    if krt != plt:
        bad_tok.append((seq, krt, plt))
    if '\\n' in e['kr'] and '\\n' not in pl:
        bad_nl.append(seq)

print('LEN over:', len(bad_len))
for x in bad_len: print('  LEN', x[0], 'lim', x[1], 'vis', x[2], repr(x[3]))
print('HANGUL:', bad_hangul)
print('MISSING TAGS:', len(bad_tags))
for x in bad_tags[:30]: print('  TAG', x[0], x[1])
print('NUM:', len(bad_num))
for x in bad_num[:20]: print('  NUM', x[0], x[1], '|', x[2])
print('TOK:', bad_tok)
print('NL KR-has but PL-not:', bad_nl)

json.dump({str(k): v for k, v in sorted(seen.items())}, open('/home/user/limbuscompany/local/praca_ai/P59/merged.json', 'w'))
print('OK -> local/praca_ai/P59/merged.json')
