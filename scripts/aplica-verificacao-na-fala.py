# -*- coding: utf-8 -*-
u"""
aplica-verificacao-na-fala.py - junta os vereditos da conferencia contra a fala
(`*.veredito.json`, na pasta temporaria) na tabela do corpus
`uMode/00_Institucional/_inbox-calls/_verificacao-na-fala.tsv`, que o extrator
de propostas le para marcar cada linha.

POR QUE UMA TABELA, E NAO EDITAR O INBOX. Os arquivos do `_inbox-calls/` sao
REGENERADOS pelo extrator a cada rodada. Anotar neles a mao se perderia na
rodada seguinte. A tabela e a memoria da conferencia; o extrator a aplica.

\U0001F534 O veredito vem de subagente, e passa pelos mesmos filtros de
sensibilidade que a proposta: `motivo` com T0, T0-P ou T1 e substituido por
"evidencia sensivel - nao descrita". O veredito fica; o teor sensivel nao.

Uso: python scripts/aplica-verificacao-na-fala.py
"""
import io, os, re, sys, json, glob, codecs, datetime, importlib.util

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    u"ext", os.path.join(RAIZ, u"scripts", u"extrai-propostas-de-resumo.py"))
ext = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ext)
TABELA = os.path.join(ext.INBOX, u"_verificacao-na-fala.tsv")
VALIDOS = (u"confirmada", u"parcial", u"contradita", u"nao_encontrada", u"fora_do_cliente")
CAB = u"arq\tid\tveredito\tts_fala\tfalantes\tmotivo\tconferido_em"


def limpa(s):
    s = re.sub(u"[\\t\\n\\r]+", u" ", s or u"").strip()
    if ext.T0.search(s) or ext.T1.search(s) or (ext.NOME.search(s) and ext.JUIZO.search(s)):
        return u"evidência sensível — não descrita"
    return s[:220]


def main():
    atual = {}
    if os.path.exists(TABELA):
        for l in io.open(TABELA, encoding=u"utf-8").read().splitlines()[1:]:
            c = l.split(u"\t")
            if len(c) == 7:
                atual[(c[0], c[1])] = c
    hoje = datetime.date.today().isoformat()
    novos, rejeitados = 0, 0
    for f in sorted(glob.glob(ext._SCRATCH + u"verificacao/*.veredito.json")):
        try:
            d = json.load(io.open(f, encoding=u"utf-8"))
        except Exception as e:
            print(u"\U0001F534 JSON invalido: %s (%s)" % (os.path.basename(f), e))
            continue
        pac = json.load(io.open(f.replace(u".veredito.json", u".pacote.json"), encoding=u"utf-8"))
        ids = set(p[u"id"] for p in pac[u"propostas"])
        for v in d.get(u"vereditos", []):
            if v.get(u"id") not in ids or v.get(u"veredito") not in VALIDOS:
                rejeitados += 1
                continue
            fal = u", ".join(limpa(x) for x in (v.get(u"falantes") or []))
            atual[(pac[u"arq"], v[u"id"])] = [pac[u"arq"], v[u"id"], v[u"veredito"],
                                               limpa(v.get(u"ts_fala")), fal,
                                               limpa(v.get(u"motivo")), hoje]
            novos += 1
    L = [CAB] + [u"\t".join(c) for _, c in sorted(atual.items())]
    io.open(TABELA, u"w", encoding=u"utf-8").write(u"\n".join(L) + u"\n")
    cont = {}
    for c in atual.values():
        cont[c[2]] = cont.get(c[2], 0) + 1
    print(u"vereditos aplicados: %d · rejeitados (id ou veredito invalido): %d" % (novos, rejeitados))
    print(u"tabela: %d linhas · %s" % (len(atual), u" · ".join(u"%s %d" % x for x in sorted(cont.items()))))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
