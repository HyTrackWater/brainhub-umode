# -*- coding: utf-8 -*-
u"""
prepara-verificacao-na-fala.py - monta, para cada reuniao que TEM transcricao
de fala, um pacote de conferencia: as propostas do `_inbox-calls/` (que vieram
do RESUMO do Gemini) + a transcricao da mesma reuniao.

POR QUE. A regra travada em 24/09 e "a transcricao e sempre mais rica; se for
eleger um, sempre transcricao". 34 reunioes dos acervos tem as duas coisas, e
as propostas delas estao marcadas `DERIVADA` porque ninguem conferiu contra a
fala. Conferir transforma "o Gemini disse que" em "foi dito, por X, no minuto Y".

\U0001F534 O pacote vive na pasta temporaria da sessao: tem fala bruta, e fala
bruta nao entra no repositorio. O que volta para o corpus e so o VEREDITO
(`_verificacao-na-fala.tsv`), aplicado pelo extrator.

Uso: python scripts/prepara-verificacao-na-fala.py [slug ...]   (vazio = todas)
"""
import io, os, re, sys, json, hashlib, codecs, importlib.util

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    u"ext", os.path.join(RAIZ, u"scripts", u"extrai-propostas-de-resumo.py"))
ext = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ext)
PACOTES = ext._SCRATCH + u"verificacao/"
RE_LINHA = re.compile(u"^- ([a-z-]+): (.+) — \\[resumo Gemini (\\d{4}-\\d{2}-\\d{2})(?: · ([^\\]]+))?\\]")


def chave(arq, texto):
    return hashlib.sha1((arq + u"|" + texto).encode(u"utf-8")).hexdigest()[:12]


def main():
    alvo = set(sys.argv[1:])
    os.makedirs(PACOTES, exist_ok=True)
    reunioes, _ = ext.le_acervo()
    n = 0
    for r in reunioes:
        if not r[u"docxs"]:
            continue
        cam = max(r[u"docxs"], key=os.path.getsize)
        t = ext.docx(cam)
        ti = t.find(ext.MARCA_TR)
        if ti == -1:
            continue
        r[u"emails"], r[u"falantes"], r[u"n_falas"] = [], [], 0
        ext.le_resumo(cam)
        if ext.le_resumo.cab:
            r[u"resolvidos"], r[u"sobra"] = ext.resolve_cabecalho(ext.le_resumo.cab)
        det, et, r[u"emails"], r[u"falantes"], r[u"n_falas"] = ext.le_resumo(cam)
        ext.roteia(r)
        if alvo and r[u"slug"] not in alvo:
            continue
        # o arquivo do inbox desta reuniao
        pref = u"%s_%s_" % (r[u"data"].isoformat(), r[u"slug"] or u"sem-destino")
        cands = [f for f in os.listdir(ext.INBOX)
                 if f.startswith(pref) and ext.kebab(r[u"titulo"]) in f]
        if not cands:
            continue
        arq = cands[0][:-3]
        props = []
        for l in io.open(os.path.join(ext.INBOX, cands[0]), encoding=u"utf-8"):
            m = RE_LINHA.match(l)
            if m:
                props.append({u"id": chave(arq, m.group(2)), u"chave": m.group(1),
                              u"texto": m.group(2), u"ts": m.group(4) or u""})
        if not props:
            continue
        base = PACOTES + arq
        io.open(base + u".transcricao.txt", u"w", encoding=u"utf-8").write(t[ti:])
        json.dump({u"arq": arq, u"titulo": r[u"titulo"], u"data": r[u"data"].isoformat(),
                   u"cliente": r[u"pasta"] or r[u"slug"], u"transcricao": base + u".transcricao.txt",
                   u"saida": base + u".veredito.json", u"propostas": props},
                  io.open(base + u".pacote.json", u"w", encoding=u"utf-8"), ensure_ascii=False, indent=1)
        n += 1
        print(u"%s  %-16s %3d propostas  %s" % (r[u"data"], (r[u"pasta"] or u"-")[:16], len(props), r[u"titulo"][:50]))
    print(u"pacotes: %d em %s" % (n, PACOTES))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
