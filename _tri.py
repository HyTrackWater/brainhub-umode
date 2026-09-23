# -*- coding: utf-8 -*-
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
t = io.open("uMode/00_Institucional/_contexto/_pendencias-gerais.md", encoding="utf-8").read()
linhas = t.split("\n")
itens, atual = [], None
for l in linhas:
    m = re.match(r"^(\d+)\. (.*)$", l)
    if m:
        if atual: itens.append(atual)
        atual = [int(m.group(1)), m.group(2), []]
    elif atual is not None and l.startswith("     "):
        atual[2].append(l.strip())
if atual: itens.append(atual)
print("itens parseados: %d  (numeracao vai ate %d)" % (len(itens), max(i[0] for i in itens)))

def limpa(s):
    s = re.sub(r"[*`🔴🟢🟡🔺⚠🚨🆕⚪🔵✅]", "", s)
    return re.sub(r"\s+", " ", s).strip()

RESOLV = re.compile(r"RESOLVIDO|✅|respondida em|j.{0,2} resolvid", re.I)
SEG    = re.compile(r"credencial|senha|RISC-|token|segredo", re.I)
CAEDU  = re.compile(r"\bcaedu\b", re.I)
DEC    = re.compile(r"decis[ãa]o|decidir|decide|pergunta para|vira campo|criamos\?|normalizar|modelar|reclassific", re.I)
b = collections.OrderedDict((k, []) for k in
    ["RESOLVIDO", "SEGURANCA", "TRAVA CAEDU", "DECISAO DO VINICIUS", "ARQUIVO / TECNICO"])
for n, cab, corpo in itens:
    txt = cab + " " + " ".join(corpo)
    if RESOLV.search(txt):      k = "RESOLVIDO"
    elif SEG.search(txt):       k = "SEGURANCA"
    elif CAEDU.search(txt):     k = "TRAVA CAEDU"
    elif DEC.search(txt):       k = "DECISAO DO VINICIUS"
    else:                       k = "ARQUIVO / TECNICO"
    b[k].append((n, limpa(cab)[:120]))
print()
for k, v in b.items():
    print("%-22s %4d" % (k, len(v)))
print("\n" + "="*90)
print("OS QUE CITAM A CAEDU (%d) — candidatos a travar o teste" % len(b["TRAVA CAEDU"]))
print("="*90)
for n, c in b["TRAVA CAEDU"]:
    print("%3d  %s" % (n, c))
print("\n" + "="*90)
print("SEGURANCA (%d)" % len(b["SEGURANCA"]))
print("="*90)
for n, c in b["SEGURANCA"]:
    print("%3d  %s" % (n, c[:110]))
