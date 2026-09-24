# -*- coding: utf-8 -*-
u"""
indexa-transcricoes.py - le um diretorio de transcricoes Tactiq e devolve o
INDICE: data, titulo, duracao, falantes e volume de fala por pessoa.

POR QUE INDICE ANTES DE CONTEUDO. Sao 1,8 MB de texto corrido. Ler tudo para
dentro do contexto e desperdicio e, pior, e como se perde precisao: o que
importa primeiro e QUEM falou, QUANDO, e QUANTO - isso sai por contagem, nao
por leitura.

O QUE A FONTE TEM, E O CORPUS NAO TINHA. O registro
`_varredura-2026-09-23g-participantes-das-reunioes-sao-anonimos.md` fechou
como negativo rigoroso: "presenca nominal com data NAO sai por API" - 24 dos
25 uuids do campo `Participantes` do Notion nao resolvem para nome nenhum.

\U0001F534 **A transcricao Tactiq tem exatamente isso**, no formato
`[HH:MM:SS] Nome Sobrenome: fala`. **O negativo continua verdadeiro para a
API do Notion e deixa de ser verdadeiro para a conta como um todo.**

NAO ESCREVE NADA NO CORPUS. Este script so le e reporta. O que entra no
corpus e decisao de leitura, uma reuniao por vez.
"""
import io, os, re, sys, codecs, collections

RE_CAB = re.compile(u"^(Titulo|Título|Data|Link):\\s*(.+)$")
RE_FALA = re.compile(u"^\\[(\\d{2}):(\\d{2}):(\\d{2})\\]\\s*([^:]{1,60}?):\\s*(.*)$")


def le(caminho):
    u"""Devolve (cabecalho, [(segundos, falante, texto)])."""
    cab, falas = {}, []
    with io.open(caminho, encoding=u"utf-8", errors=u"replace") as f:
        for ln in f:
            ln = ln.rstrip(u"\n")
            m = RE_CAB.match(ln)
            if m and not falas:
                cab[m.group(1).lower().replace(u"í", u"i")] = m.group(2).strip()
                continue
            m = RE_FALA.match(ln)
            if m:
                seg = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
                falas.append((seg, m.group(4).strip(), m.group(5).strip()))
    return cab, falas


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else u"."
    arquivos = sorted(f for f in os.listdir(base) if f.endswith(u".txt"))
    w = sys.stdout.write

    total_falas = 0
    por_pessoa = collections.Counter()
    reunioes_por_pessoa = collections.defaultdict(set)
    linhas = []

    for fn in arquivos:
        cab, falas = le(os.path.join(base, fn))
        if not falas:
            linhas.append((fn, cab.get(u"data", u"?"), 0, 0, []))
            continue
        dur = falas[-1][0]
        pessoas = collections.Counter(f[1] for f in falas)
        for p, c in pessoas.items():
            por_pessoa[p] += c
            reunioes_por_pessoa[p].add(fn)
        total_falas += len(falas)
        linhas.append((fn, cab.get(u"data", u"?"), dur, len(falas), pessoas.most_common()))

    w(u"== INDICE DE TRANSCRICOES ==\n")
    w(u"arquivos        : %d\n" % len(arquivos))
    w(u"falas indexadas : %d\n" % total_falas)
    horas = sum(l[2] for l in linhas) / 3600.0
    w(u"tempo gravado   : %.1f horas\n" % horas)
    w(u"pessoas distintas: %d\n\n" % len(por_pessoa))

    w(u"%-56s %-11s %6s %6s %s\n" % (u"ARQUIVO", u"DATA", u"DUR", u"FALAS", u"PESSOAS"))
    for fn, data, dur, nf, pessoas in linhas:
        w(u"%-56s %-11s %5dm %6d %d\n"
          % (fn[:56], data, dur // 60, nf, len(pessoas)))

    w(u"\n== QUEM FALA, e em quantas reunioes ==\n")
    w(u"%-34s %8s %10s\n" % (u"PESSOA", u"FALAS", u"REUNIOES"))
    for p, c in por_pessoa.most_common():
        w(u"%-34s %8d %10d\n" % (p[:34], c, len(reunioes_por_pessoa[p])))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
