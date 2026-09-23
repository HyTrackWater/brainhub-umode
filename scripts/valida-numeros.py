# -*- coding: utf-8 -*-
u"""valida-numeros.py - confere se os numeros do AGORA.md batem com o disco.

POR QUE EXISTE
--------------
Tres vezes em 23 set 2026 o `AGORA.md` mentiu: dizia 2.403 MDs quando havia 2.648,
487 pendencias quando havia 572, 1.161 reunioes quando eram 1.162. Numero escrito a
mao envelhece em silencio, e o `AGORA.md` e o primeiro arquivo que todo mundo le.

Este script NAO corrige nada - ele ACUSA a divergencia. Corrigir e decisao de quem
esta editando, porque as vezes o numero do disco e que esta errado.

Rodar junto do ritual de fechamento (START.md secao 4).
"""
import io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = os.path.join(RAIZ, u"uMode")

def conta(raiz, cond):
    n = 0
    for dp, dn, fn in os.walk(raiz):
        dn[:] = [d for d in dn if d not in (u"__pycache__",)]
        for f in fn:
            if cond(os.path.join(dp, f).replace(os.sep, u"/"), f):
                n += 1
    return n

def md(p, f):    return f.endswith(u".md")
def reg(pasta):
    def _(p, f):
        return (u"/%s/" % pasta) in p and f.endswith(u".md") \
               and not f.startswith(u"_template") and f != u"_indice.md"
    return _

def main():
    real = {
        u"MDs em `uMode/`":        conta(U, md),
        u"Clientes no corpus":     len([d for d in os.listdir(os.path.join(U, u"_Clientes"))
                                        if not d.startswith(u"_")]),
        u"Demandas":               conta(U, reg(u"_demandas")),
        u"RFIs":                   conta(U, reg(u"_rfis")),
        u"Fichas de pessoa":       conta(U, reg(u"_pessoas")),
        u"Fichas de ferramenta":   conta(U, lambda p, f: u"/_ferramentas/" in p
                                          and f.endswith(u".md") and f != u"_indice.md"),
    }
    pend = io.open(os.path.join(U, u"00_Institucional", u"_contexto",
                                u"_pendencias-gerais.md"), encoding="utf-8").read()
    real[u"Decisões pendentes"] = len(re.findall(u"(?m)^[0-9]+\\. ", pend))

    ag = io.open(os.path.join(RAIZ, u"AGORA.md"), encoding="utf-8").read()
    print(u"%-26s %10s %10s" % (u"MÉTRICA", u"AGORA.md", u"DISCO"))
    print(u"-" * 50)
    ruim = 0
    for k, v in real.items():
        m = re.search(u"\\|\\s*(?:[^|]*?)%s[^|]*\\|\\s*\\*{0,2}([\\d.]+)" % re.escape(k), ag)
        dito = m.group(1).replace(u".", u"") if m else None
        if dito is None:
            print(u"%-26s %10s %10d   ⚠ não declarado no AGORA.md" % (k, u"—", v)); ruim += 1
        elif int(dito) != v:
            print(u"%-26s %10s %10d   🔴 DIVERGE" % (k, dito, v)); ruim += 1
        else:
            print(u"%-26s %10s %10d   ok" % (k, dito, v))
    print()
    if ruim:
        print(u"🔴 %d métrica(s) fora. O AGORA.md é o primeiro arquivo que todo mundo lê —" % ruim)
        print(u"   número errado ali vira decisão errada depois. Corrija antes de commitar.")
        return 1
    print(u"✅ Os números do AGORA.md batem com o disco.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
