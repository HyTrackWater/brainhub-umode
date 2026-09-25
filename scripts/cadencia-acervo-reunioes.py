# -*- coding: utf-8 -*-
u"""
cadencia_laura.py - cadencia de atendimento por cliente, a partir do NOME do
arquivo, e cruzamento com o `status` que o corpus declara.

POR QUE O NOME DO ARQUIVO E DADO PRIMARIO. Ele e o titulo do evento na agenda,
digitado por uma pessoa quando marcou a reuniao. \U0001F534 O corpo do resumo e
gerado por modelo e e derivado; o nome nao passou por modelo nenhum.

Entao daqui sai, com seguranca: QUE cliente, QUE dia, QUE assunto foi marcado.
Nao sai: o que foi dito, o que foi decidido, quem falou o que.

E o cruzamento que interessa: cliente que o corpus diz `Ongoing` e que nao tem
reuniao ha muito tempo. \u26a0 Isso nao prova abandono - a Laura e uma pessoa de
uma carteira, e a conta pode estar com outro. Mas e pergunta que so aparece
quando se cruza.
"""
import io, os, re, sys, codecs, collections, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(AQUI, u"laura2")
CORPUS = u"C:/Ambientes Virtuais/BrainHub/brainhub-umode"
HOJE = datetime.date(2026, 9, 25)

RE_DATA = re.compile(u"(\\d{4})[_-](\\d{2})[_-](\\d{2})")

CLIENTES = [
    (u"Luiza Barcelos", u"Luiza Barcelos"), (u"Moda Objetiva", u"Moda Objetiva"),
    (u"Objetiva", u"Moda Objetiva"), (u"Cambos", u"Cambos"),
    (u"Lofty Style", u"Lofty Style"), (u"Lofty", u"Lofty Style"),
    (u"Plie", u"Plie"), (u"Highstil", u"Highstil"), (u"HighStil", u"Highstil"),
    (u"DRO", u"DRO"), (u"Ladeira", u"Ladeira Bijuterias"), (u"Laces", u"Laces"),
    (u"Piccadilly", None), (u"Tee Fashion", None), (u"Gagnoa", None),
    (u"Aramodu", None), (u"Disparate", None), (u"STZ", u"Studio Z"),
    (u"Oficina", u"Oficina Reserva"), (u"NTK", u"NTK"), (u"NV", u"NV"),
]

# assunto a partir de palavra no titulo - so rotulo, nunca conteudo
ASSUNTOS = [
    (u"discovery", u"discovery"), (u"treinamento", u"treinamento"),
    (u"integra", u"integra\u00e7\u00e3o"), (u"onboarding", u"onboarding"),
    (u"alinhamento quinzenal", u"ritual quinzenal"), (u"quinzenal", u"ritual quinzenal"),
    (u"alinhamento", u"alinhamento"), (u"d\u00favida", u"d\u00favidas"),
    (u"duvida", u"d\u00favidas"), (u"feedback", u"feedback"),
    (u"cronograma", u"cronograma"), (u"fechamento", u"fechamento"),
    (u"teste", u"teste"), (u"importa", u"importa\u00e7\u00e3o"),
    (u"permissionamento", u"permissionamento"), (u"ficha", u"ficha t\u00e9cnica"),
    (u"custo", u"custos"), (u"tabela de medidas", u"tabela de medidas"),
]


def status_do_corpus(cli):
    p = os.path.join(CORPUS, u"uMode", u"_Clientes", cli,
                     u"00_Institucional", u"_contexto", u"institucional.md")
    if not os.path.exists(p):
        return None
    t = io.open(p, encoding=u"utf-8", errors=u"replace").read()
    m = re.search(u"^- status: (.+?)(?: \u2014 |$)", t, re.M)
    return m.group(1).strip() if m else u"?"


def main():
    w = sys.stdout.write
    mapa = {}
    for l in io.open(os.path.join(BASE, u"_mapa.tsv"),
                     encoding=u"utf-8").read().splitlines()[1:]:
        c = l.split(u"\t")
        if len(c) >= 2:
            mapa[c[0]] = c[1]

    porcli = collections.defaultdict(list)
    assuntos = collections.defaultdict(collections.Counter)
    sem = []

    for fn, nome in sorted(mapa.items(), key=lambda x: x[1]):
        md = RE_DATA.search(nome)
        if not md:
            sem.append(nome)
            continue
        try:
            d = datetime.date(int(md.group(1)), int(md.group(2)), int(md.group(3)))
        except ValueError:
            sem.append(nome)
            continue
        alvo = None
        for chave, pasta in CLIENTES:
            if chave.lower() in nome.lower():
                alvo = pasta if pasta else u"~%s (fora da carteira atual)" % chave
                break
        if not alvo:
            alvo = u"(sem cliente no t\u00edtulo)"
        porcli[alvo].append(d)
        for chave, rot in ASSUNTOS:
            if chave in nome.lower():
                assuntos[alvo][rot] += 1
                break

    w(u"=" * 78 + u"\n")
    w(u"CAD\u00caNCIA DE ATENDIMENTO \u00b7 acervo da Laura \u00b7 do nome do arquivo\n")
    w(u"=" * 78 + u"\n\n")
    w(u"%-30s %4s %11s %11s %7s  %s\n"
      % (u"CLIENTE", u"REU", u"PRIMEIRA", u"\u00daLTIMA", u"SIL\u00caNCIO", u"STATUS NO CORPUS"))

    linhas = []
    for cli, ds in porcli.items():
        ds.sort()
        dias = (HOJE - ds[-1]).days
        st = status_do_corpus(cli) if not cli.startswith((u"~", u"(")) else None
        linhas.append((dias, cli, ds, st))
    linhas.sort()

    alertas = []
    for dias, cli, ds, st in linhas:
        marca = u""
        if st and st.lower().startswith(u"ongoing") and dias > 180:
            marca = u"  \U0001F534"
            alertas.append((cli, dias, st))
        w(u"%-30s %4d %11s %11s %5dd  %s%s\n"
          % (cli[:30], len(ds), ds[0].isoformat(), ds[-1].isoformat(), dias,
             (st or u"\u2014")[:26], marca))

    w(u"\nASSUNTO DOMINANTE POR CLIENTE (r\u00f3tulo do t\u00edtulo, nunca conte\u00fado)\n")
    for _, cli, ds, _ in linhas[:12]:
        a = assuntos[cli].most_common(3)
        if a:
            w(u"   %-26s %s\n" % (cli[:26], u" \u00b7 ".join(u"%s %d" % x for x in a)))

    if alertas:
        w(u"\n\U0001F534 CLIENTE `Ongoing` NO CORPUS E SEM REUNI\u00c3O NESTE ACERVO H\u00c1 MAIS DE 6 MESES\n")
        for cli, dias, st in alertas:
            w(u"   %-26s %4d dias \u00b7 corpus diz: %s\n" % (cli, dias, st))
        w(u"   \u26a0 N\u00c3O prova abandono: este \u00e9 o acervo de UMA pessoa, e a conta pode estar\n")
        w(u"     com outro atendente. \U0001F7E2 \u00c9 pergunta que s\u00f3 aparece no cruzamento.\n")

    if sem:
        w(u"\n\u26a0 sem data no nome: %d\n" % len(sem))
        for n in sem[:5]:
            w(u"   %s\n" % n[:74])
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
