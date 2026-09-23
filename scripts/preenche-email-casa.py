# -*- coding: utf-8 -*-
u"""
preenche-email-casa.py - grava o e-mail corporativo nas fichas da Casa que
estavam com `[a preencher]`, a partir da base de PESSOAS do Notion
(`collection://c82a689c-704c-42aa-8752-bfae592f91bd`), lida em 23/09/2026.

POR QUE ESTE SCRIPT EXISTE. O e-mail e a chave de identidade do corpus
(item 252). Sem ele, o campo `atendimento` dos 49 `institucional.md` nao
resolve para pessoa nenhuma, e o agente de transcricao nao sabe a quem
enderecar nada. Era o bloqueio dos itens 598-599.

POR QUE NAO E O `gera-fichas-umoder.py`. Aquele le a base `uModers`, que NAO
contem estas pessoas. Esta e outra base - a que o campo `Atendimento 2024` do
`Mapa de Clientes` aponta. Duas bases de pessoa convivem no mesmo workspace.

O QUE NAO ENTRA. A base traz telefone, endereco com CEP e data de nascimento.
Tudo `T0`: nada disso foi lido para ca. So nome, e-mail, funcao e situacao.

O QUE NAO FOI DECIDIDO. O CRM diz `Fernanda` e existem DUAS: `Fernanda Araujo`
(Ativo) e `Fernanda Martins` (Inativo). O script grava o e-mail de cada uma na
ficha DELA - o que nao se faz e dizer qual das duas atende os 3 clientes.
Isso e pendencia, nao palpite.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHAS = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_pessoas")

FONTE = (u"base de pessoas do Notion "
         u"(`collection://c82a689c…`, a mesma que o campo `Atendimento 2024` "
         u"do `Mapa de Clientes` aponta), lida em 23/09/2026")

# arquivo da ficha -> (email, funcao, area, situacao)
# Copiado literalmente da consulta. Campo vazio na origem fica None.
DADOS = {
    u"andrea-goulart-holmer-dos-santos": (u"andrea.holmer@umode.com.br", u"Key Account", u"Operação", u"Inativo"),
    u"dalker-walter":                    (u"dalker@umode.com.br", None, None, u"Inativo"),
    u"elizabeth-alves-de-souza-santana": (u"elizabeth.alves@umode.com.br", u"CS", None, u"Inativo"),
    u"fernanda-araujo":                  (u"fernanda.araujo@umode.com.br", u"Head de Design e UX", u"Operação", u"Ativo"),
    u"joao-paulo-contar-risoleo":        (u"joao.risoleo@umode.com.br", u"CEO", None, u"Ativo"),
    u"juliana-ferre-esteves":            (u"juliana.ferre@umode.com.br", u"CPO", u"Operação", u"Ativo"),
    u"julianne-dias-rodrigues":          (u"julianne.dias@umode.com.br", u"Key Account", u"Operação", u"Ativo"),
    u"laura-delgado-cardoso":            (u"laura.delgado@umode.com.br", u"CS", u"Operação", u"Ativo"),
    u"marina-goncalves-santoro":         (u"marina.santoro@umode.com.br", u"Head de Onboarding", u"Operação", u"Ativo"),
    u"pedro-murillo":                    (u"pedro.murillo@umode.com.br", u"Analista de Relacionamento", u"Operação", u"Ativo"),
    u"rafael-del-gaudio-renaldim":       (u"rafael@umode.com.br", u"Head de CX", u"Operação", u"Inativo"),
    u"sandro-costa":                     (u"sandro@umode.com.br", None, None, u"Ativo"),
    u"saulo":                            (u"saulo@umode.com.br", u"CTO", None, u"Inativo"),
    u"tais-moser":                       (u"tais.moser@umode.com.br", u"Key Account", None, u"Inativo"),
    u"vanessa-rinaldi-ornelas-engman":   (u"vanessa.rinaldi@umode.com.br", u"Consultora", u"Operação", u"Ativo"),
    u"victor-aragao":                    (u"victor.aragao@umode.com.br", u"Analista de Suporte", u"Operação", u"Ativo"),
}

# Consultadas e SEM e-mail na origem. Ficam como estao: a ausencia e o dado.
SEM_EMAIL_NA_ORIGEM = [
    u"ana-flavia-maran-carrilo",   # campo Email vazio, Situacao Ativo
    u"eduardo-penna",              # campo Email vazio, Situacao Inativo
    u"filipe-de-lima-kertcher",    # campo Email string vazia, Funcao Freela
]


def bloco_email(email, funcao, area, situacao):
    linhas = [
        u"**`%s`** — e-mail **corporativo**, da %s." % (email, FONTE),
        u"",
        u"\U0001F7E2 **É a chave de identidade desta pessoa** (item 252). Tier `T2`.",
    ]
    extra = []
    if funcao:
        extra.append(u"`Função` na origem: **%s**" % funcao)
    if area:
        extra.append(u"`Área`: **%s**" % area)
    if situacao:
        extra.append(u"`Situação`: **%s**" % situacao)
    if extra:
        linhas += [u"", u"⚠ " + u" · ".join(extra) + u"."]
    linhas += [
        u"",
        u"⚠ **A mesma origem traz telefone, endereço com CEP e data de nascimento — `T0`, "
        u"nenhum copiado.** Registro que existem e onde.",
    ]
    return u"\n".join(linhas)


def main():
    escritos, ja_tinham, nao_achados = 0, 0, []
    for slug, (email, funcao, area, situacao) in sorted(DADOS.items()):
        caminho = os.path.join(FICHAS, slug + u".md")
        if not os.path.exists(caminho):
            nao_achados.append(slug)
            continue
        txt = io.open(caminho, encoding=u"utf-8").read()
        if u"### Email" not in txt:
            nao_achados.append(slug)
            continue
        antes, resto = txt.split(u"### Email", 1)
        corpo, depois = resto.split(u"\n### ", 1)
        if u"@" in corpo:
            ja_tinham += 1
            continue
        novo = antes + u"### Email\n" + bloco_email(email, funcao, area, situacao) \
            + u"\n### " + depois
        io.open(caminho, u"w", encoding=u"utf-8").write(novo)
        escritos += 1

    w = sys.stdout.write
    w(u"fichas com e-mail gravado : %d\n" % escritos)
    w(u"ja tinham e-mail          : %d\n" % ja_tinham)
    w(u"consultadas e SEM e-mail na origem: %d  -> %s\n"
      % (len(SEM_EMAIL_NA_ORIGEM), u", ".join(SEM_EMAIL_NA_ORIGEM)))
    if nao_achados:
        w(u"\U0001F534 ficha nao encontrada: %s\n" % u", ".join(nao_achados))
        return 1
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
