# -*- coding: utf-8 -*-
u"""
enriquece-demandas-do-vault.py - preenche campos das demandas a partir do
export `Demandas de Clientes.csv` que estava no vault do Joao, nao lido.

COMO ISTO FOI ACHADO, e a licao vale mais que o script. Eu estava prestes a
declarar 24.422 lacunas de demanda como "campo que nenhuma fonte tem" - e a
pista de que estavam TODAS nos mesmos campos, em 100% dos 993 arquivos, e que
me fez desconfiar: lacuna uniforme demais nao e lacuna de varredura, e
template que nunca foi alimentado. Ai fui procurar a fonte de alimentacao.

O `BrainHub/uMode/_Clientes/_geral/notion/` do vault tem SEIS exports do
Notion. O corpus so usava um (`Mapa de Clientes.csv`). Os outros cinco nunca
foram abertos.

O QUE ESTE CSV TEM E O CORPUS NAO:
  Etapa                   813 de 836   Key Account/Responsavel  347
  Data de Conclusao       129          Comentario uMode         103
  Criticidade              54          Bloqueio                  35
  Nivel de Esforco         29

824 das 993 demandas do corpus casam por `ID legado`.

REGRA: so escreve onde o MD tem `[a preencher]`. NUNCA sobrescreve valor que
ja existe - foi assim que apaguei 20 clientes por engano ontem.
"""
import csv, io, os, re, sys, codecs, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = (u"C:/Ambientes Virtuais/BrainHub - Jo\u00e3o Risol\u00e9o/umode-os-vault/"
       u"BrainHub/uMode/_Clientes/_geral/notion/Demandas de Clientes.csv")
FONTE = u"export `Demandas de Clientes` do vault, conferido em 24/09/2026"

# secao do MD -> (coluna do CSV, como formatar)
MAPA = [
    (u"### Respons\u00e1vel",      u"Key Account/Respons\u00e1vel", None),
    (u"### Motivo de bloqueio", u"Bloqueio",                  None),
    (u"### Horas atribu\u00eddas",  u"Horas de Demanda",         None),
    (u"### Resolu\u00e7\u00e3o",         u"Coment\u00e1rio uMode",         None),
    (u"### Notas internas",     u"Observa\u00e7\u00f5es",              None),
]


def bloco(txt, sec):
    m = u"\n" + sec + u"\n"
    if m not in txt:
        return None
    antes, resto = txt.split(m, 1)
    corte = len(resto)
    for h in (u"\n## ", u"\n### "):
        i = resto.find(h)
        if i != -1:
            corte = min(corte, i)
    return antes, m, resto[:corte], resto[corte:]


def main():
    if not os.path.exists(CSV):
        sys.stderr.write("CSV nao encontrado\n")
        return 2
    linhas = list(csv.DictReader(io.open(CSV, encoding=u"utf-8-sig", newline=u"")))
    por_id = {}
    for x in linhas:
        i = (x.get(u"ID") or u"").strip()
        if i:
            por_id[i] = x

    escritos, campos = 0, collections.Counter()
    datas, etapas = 0, 0
    for dirpath, _, filenames in os.walk(os.path.join(RAIZ, u"uMode", u"_Clientes")):
        if u"_demandas" not in dirpath.replace(os.sep, u"/"):
            continue
        for fn in filenames:
            if not fn.startswith(u"D-") or not fn.endswith(u".md"):
                continue
            p = os.path.join(dirpath, fn)
            txt = io.open(p, encoding=u"utf-8").read()
            m = re.search(u"### ID legado \\(Notion/CX Hub\\)\n(.+)", txt)
            if not m:
                continue
            reg = por_id.get(m.group(1).strip())
            if not reg:
                continue
            antes_txt = txt

            for sec, col, _f in MAPA:
                v = (reg.get(col) or u"").strip()
                if not v:
                    continue
                b = bloco(txt, sec)
                if not b or u"a preencher" not in b[2]:
                    continue
                corpo = u"**%s**\n> Fonte: %s \u2014 campo `%s`." % (v[:600], FONTE, col)
                txt = b[0] + b[1] + corpo + b[3]
                campos[sec] += 1

            # Datas: tres colunas numa secao so
            b = bloco(txt, u"### Datas")
            if b and u"a preencher" in b[2]:
                pares = [(u"solicita\u00e7\u00e3o", u"Data da Solicita\u00e7\u00e3o"),
                         (u"previs\u00e3o de entrega", u"Data de Previs\u00e3o de Entrega"),
                         (u"conclus\u00e3o", u"Data de Conclus\u00e3o")]
                got = [(r, (reg.get(c) or u"").strip()) for r, c in pares]
                got = [(r, v) for r, v in got if v]
                if got:
                    corpo = u"\n".join(u"- **%s:** %s" % (r, v) for r, v in got)
                    corpo += u"\n\n> Fonte: %s." % FONTE
                    txt = b[0] + b[1] + corpo + b[3]
                    datas += 1

            # Etapa do CX Hub: vai para Status do CX Hub se estiver vazio
            et = (reg.get(u"Etapa") or u"").strip()
            if et:
                b = bloco(txt, u"### Status")
                if b and u"a preencher" in b[2]:
                    txt = b[0] + b[1] + (u"**%s**\n> Fonte: %s \u2014 campo `Etapa`."
                                         % (et, FONTE)) + b[3]
                    etapas += 1

            if txt != antes_txt:
                io.open(p, u"w", encoding=u"utf-8").write(txt)
                escritos += 1

    w = sys.stdout.write
    w(u"demandas no CSV       : %d\n" % len(por_id))
    w(u"demandas enriquecidas : %d\n" % escritos)
    w(u"  campo `Datas`       : %d\n" % datas)
    w(u"  campo `Status`      : %d\n" % etapas)
    for k, v in campos.most_common():
        w(u"  %-26s: %d\n" % (k, v))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
