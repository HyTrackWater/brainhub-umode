# -*- coding: utf-8 -*-
u"""
nomeia-ausencia-verificada.py - transforma "campo vazio na base" em ausencia
CITAVEL, nomeando a base e as datas em que se olhou.

O PROBLEMA. 137 ocorrencias de "campo vazio na base" em 44 dos 49 clientes
NAO dizem QUAL base. Ausencia sem fonte nomeada nao e ausencia citavel: o
agente de transcricao nao sabe se alguem chegou a procurar, e todo fato
derivado sai `[sem fonte]` (protocolo secao 2.1-bis).

O QUE ESTE SCRIPT FAZ. Para os tres campos que vem do CRM, compara DOIS
instantes independentes - a base viva, lida por SQL em 23/09/2026, e o export
de 04/03/2026 que esta no vault do Joao - e:

  vazio nos dois   -> reescreve nomeando a base e as duas datas
  \u26a0 CHEIO na base   -> NAO reescreve: ACUSA. Se a base tem dado e o corpus
                        diz vazio, o corpus e que esta defasado, e sobrescrever
                        isso esconderia dado real.

A leitura da base viva esta embutida abaixo como DADO DATADO, nao como
verdade permanente: e uma foto de 23/09/2026 e o cabecalho diz isso.
"""
import io, os, re, sys, codecs, csv

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_VAULT = (u"C:/Ambientes Virtuais/BrainHub - Jo\u00e3o Risol\u00e9o/umode-os-vault/"
             u"BrainHub/uMode/_Clientes/_geral/notion/Mapa de Clientes.csv")

LIDO_EM = u"23/09/2026"
EXPORT_EM = u"04/03/2026"

# base viva, lida por SQL em 23/09/2026. Clientes NAO listados tem os tres
# campos vazios. Aqui so quem tem ALGUM campo preenchido.
CHEIOS = {
    u"Caedu":          {u"setor"},
    u"Cambos":         {u"setor"},
    u"Colmeia":        {u"setor"},
    u"Highstil":       {u"ativacao"},
    u"Hyperlocal":     {u"setor"},
    u"Lenny Niemeyer": {u"ativacao"},
    u"Lofty Style":    {u"ativacao"},
    u"Luiza Barcelos": {u"receita", u"ativacao", u"setor"},
    u"NK STORE":       {u"receita", u"ativacao", u"setor"},
    u"NV":             {u"setor"},
    u"Osklen":         {u"setor"},
    u"Recco":          {u"ativacao", u"setor"},
    u"Seven Global":   {u"setor"},
    u"Studio Z":       {u"setor"},
    u"Vivara":         {u"setor"},
    u"VIX":            {u"setor"},
}

# secao do institucional -> (campo, coluna no export, quantos clientes tem)
CAMPOS = [
    (u"### Receita anual",      u"receita",  u"Receita Anual",          2),
    (u"### Data de ativa\u00e7\u00e3o", u"ativacao", u"Data Ativa\u00e7\u00e3o Cliente", 6),
    (u"### Segmento",           u"setor",    u"Setor da Empresa",       12),
]

# As quatro formas que o corpus usa de fato, medidas nos 48 arquivos:
#   `[a preencher]` \u2014 **campo vazio na base**            (74 ocorrencias)
#   `[a preencher]` \u2014 campo **vazio na base `X`**.       (11)
#   `[a preencher]` \u2014 campo vazio.                       (10)
#   `[a preencher]` \u2014 campo **vazio** na base `X`.        (2)
# O negrito abre ANTES de "campo" na forma dominante, e era isso que a
# primeira versao deste regex nao previa - casava 11 de 137.
RE_VAZIO = re.compile(
    u"`\\[a preencher\\]`\\s*\u2014\\s*\\*{0,2}(?:o\\s+)?campo\\s*"
    u"(?:`[^`]+`\\s*)?\\*{0,2}(?:est\u00e1\\s+)?\\*{0,2}vazi[ao]\\*{0,2}"
    u"(?:\\s+n[ao]\\s+base(?:\\s*`[^`]+`)?)?\\*{0,2}\\s*\\.?", re.I)


def export_vazio():
    u"""cliente -> conjunto de campos vazios no export de 04/03/2026."""
    out = {}
    if not os.path.exists(CSV_VAULT):
        return None
    with io.open(CSV_VAULT, encoding=u"utf-8-sig", newline=u"") as f:
        for linha in csv.DictReader(f):
            nome = (linha.get(u"Nome Fantasia") or u"").strip()
            if not nome:
                continue
            vazios = set()
            for _, campo, coluna, _ in CAMPOS:
                if not (linha.get(coluna) or u"").strip():
                    vazios.add(campo)
            out[nome] = vazios
    return out


def nome_do_cliente(caminho):
    p = caminho.replace(os.sep, u"/")
    return p.split(u"uMode/_Clientes/")[1].split(u"/")[0] if u"_Clientes/" in p else u"uMode"


def texto_novo(campo, qtd, tem_export):
    dois = (u" e tamb\u00e9m no **export de %s** que est\u00e1 no vault" % EXPORT_EM) if tem_export else u""
    return (u"`[a preencher]` \u2014 campo **vazio na base `Mapa de Clientes`**.\n"
            u"> \U0001F534 **Aus\u00eancia VERIFICADA:** lido por SQL na base viva em **%s**%s. "
            u"**Vazio nos dois.**\n"
            u"> \u26a0 **O campo est\u00e1 preenchido em %d dos 49 clientes** \u2014 "
            u"**n\u00e3o \u00e9 lacuna deste cliente, \u00e9 campo que a opera\u00e7\u00e3o n\u00e3o preenche.**"
            % (LIDO_EM, dois, qtd))


def main():
    exp = export_vazio()
    alvos = []
    base = os.path.join(RAIZ, u"uMode", u"_Clientes")
    for dirpath, _, filenames in os.walk(base):
        if u"_template" in dirpath or u"00_Institucional" not in dirpath:
            continue
        if u"institucional.md" in filenames:
            alvos.append(os.path.join(dirpath, u"institucional.md"))

    escritos, trocas, acusados, ja_ok = 0, 0, [], 0
    for caminho in sorted(alvos):
        cli = nome_do_cliente(caminho)
        txt = io.open(caminho, encoding=u"utf-8").read()
        antes = txt
        for titulo, campo, _, qtd in CAMPOS:
            if titulo not in txt:
                continue
            cabeca, resto = txt.split(titulo, 1)
            corte = len(resto)
            for h in (u"\n## ", u"\n### "):
                i = resto.find(h)
                if i != -1:
                    corte = min(corte, i)
            corpo, cauda = resto[:corte], resto[corte:]

            if u"Aus\u00eancia VERIFICADA" in corpo:
                ja_ok += 1
                continue
            if not RE_VAZIO.search(corpo):
                continue
            if campo in CHEIOS.get(cli, set()):
                # base TEM dado e o corpus diz vazio: nao sobrescrever, acusar
                acusados.append((cli, titulo))
                continue
            tem_export = exp is not None and campo in exp.get(cli, set())
            corpo = RE_VAZIO.sub(texto_novo(campo, qtd, tem_export), corpo, count=1)
            txt = cabeca + titulo + corpo + cauda
            trocas += 1
        if txt != antes:
            io.open(caminho, u"w", encoding=u"utf-8").write(txt)
            escritos += 1

    w = sys.stdout.write
    w(u"institucional.md lidos : %d\n" % len(alvos))
    w(u"arquivos reescritos    : %d\n" % escritos)
    w(u"aus\u00eancias nomeadas     : %d\n" % trocas)
    w(u"ja estavam nomeadas    : %d\n" % ja_ok)
    if exp is None:
        w(u"\u26a0 export do vault nao encontrado: citada so a base viva\n")
    if acusados:
        w(u"\n\U0001F534 CORPUS DEFASADO (%d) - a base TEM dado e o MD diz vazio.\n" % len(acusados))
        w(u"   Nao reescrevi: sobrescrever esconderia dado real. Varrer estes:\n")
        for cli, titulo in acusados:
            w(u"   - %-18s %s\n" % (cli, titulo))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
