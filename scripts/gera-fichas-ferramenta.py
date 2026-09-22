# -*- coding: utf-8 -*-
u"""
gera-fichas-ferramenta.py - cria UMA FICHA POR FERRAMENTA.

Decisao do Vinicius em 22 set 2026, textual: "praticamente tudo que for uma
entidade e arquivo? Ou seja, ferramenta, pessoas, empresas, areas, demandas,
RFIs, tudo.... As reunioes, contextos gerais, e-mails, tudo isso vai estar de
alguma forma ligada a esses nos maiores na escala de hierarquia."

Ate aqui, ferramenta era MENCAO EM PROSA em 249 arquivos. Mencao nao e no de
grafo. Com ficha, o eixo cliente<->ferramenta existe.

Fonte unica: base `Mapa de Clientes` do Notion,
`collection://ec041afd-fcee-44f8-83cb-223fca6f4108`, lida por SQL em 22 set 2026.
Dois campos: `Modulos Contratados` (multi_select, 7 opcoes) e `ERP/Integracao`
(multi_select, 13 opcoes).

DUAS NATUREZAS, DUAS PASTAS - de proposito:
  - `03_Produto-e-Solucoes/_ferramentas/` = os 7 modulos que a uMode VENDE;
  - `06_Tecnologia/_ferramentas/`         = os sistemas de TERCEIRO com que a
    uMode integra. Linx nao e produto da uMode; junta-los numa pasta so
    "Produto e Solucoes" induziria o leitor ao erro.

O que NAO faz:
  - NAO funde `Modulo Contratado` com as 16 Solucoes do Portfolio. O CONTEXT.md
    trava: so `uPlan -> PlanejAI` e `uFlow -> DesenvolvAI` estao confirmados,
    e proibe inferir por nome parecido.
  - NAO desmembra `Linx / SAP` nem `SAP e Linx` em dois vinculos. Sao valores
    compostos do campo; o cliente fica citado com o valor literal.
  - NAO funde `Totvs` com `Totvs Moda`, nem `Sem Integracao` com `Nao`. Suspeita
    se levanta, fusao so com confirmacao humana (protocolo-varredura-cliente
    secao 9, mesma regra que vale para pessoa).
  - NAO cria ficha para `Sem Integracao` e `Nao`: sao marcas de AUSENCIA de
    ferramenta, nao ferramentas.

Uso:  python scripts/gera-fichas-ferramenta.py
"""
import io
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UMODE = os.path.join(RAIZ, u"uMode")
DATA = u"22 set 2026"
FONTE = u"Notion - base `Mapa de Clientes`, `collection://ec041afd-...`, via SQL"

# (cliente, status, [modulos], [valores de ERP]) - copia literal do SQL.
CARTEIRA = [
    (u"4takes", u"Churn", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"Arezzo", u"Pré Onboardings", [], [u"SAP e Linx"]),
    (u"Baw", u"Sem CS", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Fornecedores"], [u"Sem Integração"]),
    (u"Caedu", u"Onboarding", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Fornecedores"], [u"Linx"]),
    (u"Cambos", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios"], [u"SPI - Sistema próprio da Cambos"]),
    (u"Camys", u"Sem CS", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"Cavallari", u"Sem CS", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"Colmeia", u"Churn", [], [u"Totvs Moda"]),
    (u"Hering", u"Pré Onboardings", [], [u"Ilimitar"]),
    (u"Highstil", u"Churn", [], [u"Totvs"]),
    (u"Hyperlocal", u"Churn", [], [u"Avec"]),
    (u"Lenny Niemeyer", u"Churn", [], [u"Linx"]),
    (u"Lofty Style", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Cronograma"], [u"Linx"]),
    (u"Loungerie", u"Onboarding", [], [u"Linx"]),
    (u"Luiza Barcelos", u"Ongoing", [u"Gestão de Coleção", u"Relatórios", u"Integração", u"Fornecedores"], [u"Safe Tech"]),
    (u"Moda Objetiva", u"Operação Assistida", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Cronograma"], [u"Ilimitar"]),
    (u"Mondepars", u"Sem CS", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"NK STORE", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Fornecedores"], [u"Linx"]),
    (u"NV", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Cronograma"], [u"Linx"]),
    (u"Oficina Reserva", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Cronograma", u"Fornecedores"], [u"SAP e Linx"]),
    (u"Osklen", u"Operação Assistida", [u"Gestão de Coleção", u"Fornecedores", u"Integração", u"Cronograma", u"Relatórios"], [u"Linx"]),
    (u"Puket", u"Ongoing", [u"Gestão de Coleção", u"Integração"], [u"Linx / SAP"]),
    (u"Recco", u"Churn", [], [u"Totvs"]),
    (u"Reserva", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Cronograma", u"Aposta", u"Planejamento", u"Fornecedores"], [u"Linx / SAP"]),
    (u"Seven Global", u"Churn", [u"Gestão de Coleção"], []),
    (u"Studio Minah", u"Sem CS", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"Studio Z", u"Churn", [u"Gestão de Coleção"], [u"SAP"]),
    (u"TDC", u"Sem CS", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"Ton Age", u"Sem CS", [u"Gestão de Coleção"], [u"Sem Integração"]),
    (u"Vivara", u"Churn", [u"Gestão de Coleção"], [u"SAP"]),
    (u"VIX", u"Ongoing", [u"Gestão de Coleção", u"Integração", u"Relatórios", u"Aposta"], [u"Linx"]),
]

# Os 7 modulos, na ordem do enum do Notion.
MODULOS = [u"Gestão de Coleção", u"Integração", u"Relatórios",
           u"Cronograma", u"Aposta", u"Planejamento", u"Fornecedores"]

# Sistemas de terceiro ATOMICOS. `Sem Integracao`/`Nao` sao ausencia, nao entram.
TERCEIROS = [
    (u"Linx", u"Linx", u"o ERP mais frequente da carteira"),
    (u"SAP", u"SAP", u"`[a preencher]`"),
    (u"Totvs", u"TOTVS", u"⚠ **suspeita de mesma origem que `Totvs Moda`** — não fundidos"),
    (u"Totvs Moda", u"TOTVS", u"⚠ **suspeita de mesma origem que `Totvs`** — não fundidos"),
    (u"Millennium", u"Millennium", u"\U0001F534 **opção do enum que NENHUM cliente usa** — nunca apareceu no corpus"),
    (u"Ilimitar", u"Ilimitar", u"⚠ não estava no corpus antes de 03 ago 2026"),
    (u"Avec", u"Avec", u"⚠ não estava no corpus antes de 03 ago 2026"),
    (u"Safe Tech", u"Safe Tech", u"`[a preencher]`"),
    (u"SPI - Sistema próprio da Cambos", u"Cambos (o próprio cliente)",
     u"\U0001F534 **não é produto de mercado** — é sistema interno do cliente"),
]

# Canais e ferramentas de TRABALHO. O enum ja existia no corpus, em
# `_espec-pessoas-e-comunicacoes.md`, campo `tool` - e eu nao o usei na primeira
# passada. Enum de fonte e fonte de entidade, inclusive o enum que e nosso.
# Formato: (nome, fornecedor, nota)
CANAIS = [
    (u"Notion", u"Notion Labs",
     u"\U0001F7E2 **\u00e9 o \u00fanico leg\u00edvel pelo BrainHub hoje** \u2014 as bases de cliente, "
     u"demanda, RFI e reuni\u00e3o vivem aqui"),
    (u"Kanbanize", u"Businessmap (Kanbanize)",
     u"🔴 **DESCONTINUADA.** Vinícius em 22 set 2026, textual: *\"ferramenta "
     u"que não é usada há tempos. Então zero foco nisso.\"* `[D]` "
     u"🔴 **Não varrer.** Os 7 cartões que a página da Reserva cita "
     u"(`umode.kanbanize.com`, boards 6 e 18) são **histórico**, não fila viva — "
     u"e a página que os cita **está desatualizada nesse ponto**"),
    (u"Gist", u"Gist",
     u"**o chat da plataforma** \u2014 canal oficial declarado para *\"d\u00favidas de usabilidade "
     u"& plataforma\"*. \u26a0 **nunca varrido**"),
    (u"WhatsApp", u"Meta",
     u"\u26a0 **canal real de opera\u00e7\u00e3o, fora de qualquer sistema.** A Reserva tem "
     u"**9 grupos mapeados**, com decis\u00e3o de manter ou excluir"),
    (u"Miro", u"Miro",
     u"quadros de regra e restri\u00e7\u00e3o \u2014 Reserva e CAEDU citam `Miro Regras e restri\u00e7\u00f5es`"),
    (u"Google Drive", u"Google",
     u"pastas de opera\u00e7\u00e3o por cliente \u2014 o campo `Drive Opera\u00e7\u00e3o` da base aponta para c\u00e1"),
    (u"YouTube", u"Google",
     u"grava\u00e7\u00e3o de reuni\u00e3o e treinamento \u2014 \u26a0 **nunca varrido**"),
    (u"HubSpot", u"HubSpot",
     u"🔴 **é o CRM da uMode** — a página da Luiza Barcelos tem link direto "
     u"para o *deal* da conta. **Não estava no enum `tool` do corpus**, e é onde vive o "
     u"lado comercial da relação. ⚠ **Nunca varrido.**"),
    (u"Trello", u"Atlassian",
     u"⚠ **ferramenta DO CLIENTE, não da uMode.** A Cambos usa para gestão do "
     u"processo. 🔴 **Não estava no enum `tool` do corpus** — achada ao abrir "
     u"a página do cliente em 22 set 2026"),
]

COMPOSTOS = {u"Linx / SAP": (u"Linx", u"SAP"), u"SAP e Linx": (u"SAP", u"Linx")}

MOD_LEGADO = {
    u"Gestão de Coleção": (u"[DesenvolvAI](../03_DesenvolvAI/_contexto/produto.md)",
        u"\U0001F7E2 **Confirmado no `CONTEXT.md`** — `uFlow` (módulo de Gestão de Coleção, "
        u"carro-chefe) → `DesenvolvAI`. **É um dos dois únicos mapeamentos confirmados.**"),
}

NAO_CONF = (u"`[a preencher]`",
    u"⚠ **Não confirmado.** O `CONTEXT.md` registra que o campo `Módulos contratados` "
    u"*\"só cita nomes legados em texto livre, sem vínculo de dado nenhum com os 16 itens do "
    u"Portfólio\"* — e **proíbe presumir mapeamento a partir de nome parecido.**")


def slug(s):
    s = unicodedata.normalize(u"NFKD", s).encode(u"ascii", u"ignore").decode(u"ascii")
    return re.sub(u"[^a-zA-Z0-9]+", u"-", s).strip(u"-").lower()


def esc(p, s):
    d = os.path.dirname(p)
    if not os.path.isdir(d):
        os.makedirs(d)
    if os.path.exists(p) and io.open(p, encoding="utf-8").read() == s:
        return 0
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    return 1


def ficha(nome, natureza, fornecedor, nota, clientes, sucessor, nota_suc, extra=None):
    L = []
    L.append(u"# %s · Ferramenta" % nome)
    L.append(u"")
    L.append(u"> **Ficha gerada por `scripts/gera-fichas-ferramenta.py` em %s.**" % DATA)
    L.append(u"> **O nome está exatamente como o enum da fonte o escreve.** Grafias parecidas **não")
    L.append(u"> foram fundidas** — mesma regra do `protocolo-varredura-cliente.md` § 9.")
    L.append(u"> Campo sem fonte fica `[a preencher]` — **nada foi inferido.**")
    L.append(u"")
    L.append(u"## Identificação")
    L.append(u"### Nome na fonte")
    L.append(u"**`%s`**" % nome)
    L.append(u"### Natureza")
    L.append(natureza)
    L.append(u"### Fornecedor")
    L.append(fornecedor)
    L.append(u"### Observação de taxonomia")
    L.append(nota)
    L.append(u"")
    L.append(u"## Adoção")
    L.append(u"### Quantos clientes")
    L.append(u"**%d** de 49 clientes do corpus" % len(clientes))
    L.append(u"### Quais clientes")
    if clientes:
        L.append(u"| Cliente | `Status` na base | Valor literal do campo |")
        L.append(u"|---|---|---|")
        for c, st, lit in clientes:
            L.append(u"| [%s](../../_Clientes/%s/00_Institucional/_contexto/institucional.md) | `%s` | `%s` |"
                     % (c, c, st, lit))
    else:
        L.append(u"\U0001F534 **Nenhum.** A opção existe no enum e **nenhum cliente a usa.**")
    L.append(u"")
    L.append(u"> ⚠ **Isto é o que o campo declara, não o que está em uso.** O campo `Status` da")
    L.append(u"> mesma base já se contradisse por sete caminhos independentes — ver")
    L.append(u"> [`_taxonomia-status-cliente.md`](../../00_Institucional/_contexto/_taxonomia-status-cliente.md).")
    L.append(u"")
    L.append(u"## Relações")
    L.append(u"### Solução do portfólio correspondente")
    L.append(sucessor)
    L.append(u"")
    L.append(nota_suc)
    L.append(u"### Áreas que usam")
    L.append(u"`[a preencher]` — \U0001F534 **nenhuma fonte varrida liga ferramenta a área.**")
    L.append(u"### Demandas e RFIs que a citam")
    L.append(u"`[a preencher]` — \U0001F534 **o campo não existe na base de demandas nem na de RFIs.**")
    if extra:
        L.append(u"")
        L.extend(extra)
    L.append(u"")
    L.append(u"## Governança")
    L.append(u"### Quem pode alterar este documento")
    L.append(u"Liderança de Produto e Soluções. **A lista de clientes é gerada por script** —")
    L.append(u"corrigir na fonte, não aqui.")
    L.append(u"")
    L.append(u"## Fontes e referências")
    L.append(u"### Procedência")
    L.append(u"| Bloco | Fonte | Data |")
    L.append(u"|---|---|---|")
    L.append(u"| Identificação · Adoção | %s | **%s** |" % (FONTE, DATA))
    L.append(u"")
    return chr(10).join(L) + chr(10)



def indice(titulo, intro, pasta, itens, carteira_por_cliente, rel):
    L = []
    L.append(u"# " + titulo)
    L.append(u"")
    L.append(u"> **DERIVADO.** Gerado por `scripts/gera-fichas-ferramenta.py`. **Nao se edita a mao.**")
    L.append(u"")
    L.append(intro)
    L.append(u"")
    L.append(u"## Por ferramenta")
    L.append(u"")
    L.append(u"| Ferramenta | Clientes |")
    L.append(u"|---|---:|")
    for nome, arq, n in itens:
        L.append(u"| [%s](%s) | %s |" % (nome, arq, (u"**%d**" % n) if n else u"🔴 **0**"))
    L.append(u"")
    L.append(u"## Por cliente")
    L.append(u"")
    L.append(u"| Cliente | " + rel + u" |")
    L.append(u"|---|---|")
    for c in sorted(carteira_por_cliente):
        v = carteira_por_cliente[c]
        L.append(u"| [%s](../../_Clientes/%s/00_Institucional/_contexto/institucional.md) | %s |"
                 % (c, c, v if v else u"—"))
    L.append(u"")
    L.append(u"## Governanca")
    L.append(u"### Quem pode alterar este documento")
    L.append(u"🔴 **Ninguem.** E `DERIVADO` — corrigir na fonte, e rodar o script.")
    L.append(u"")
    return chr(10).join(L) + chr(10)


def main():
    n = 0
    pm = os.path.join(UMODE, u"03_Produto-e-Solucoes", u"_ferramentas")
    pt = os.path.join(UMODE, u"06_Tecnologia", u"_ferramentas")

    for m in MODULOS:
        cl = [(c, st, m) for (c, st, mods, _e) in CARTEIRA if m in mods]
        suc, nsuc = MOD_LEGADO.get(m, NAO_CONF)
        n += esc(os.path.join(pm, slug(m) + u".md"), ficha(
            m, u"**Módulo contratável da plataforma uMode** (nome legado do uFlow)",
            u"uMode", u"`[a preencher]`", cl, suc, nsuc))

    # --- 2-bis) canais e ferramentas de trabalho ---
    # Nao tem coluna de cliente numa base: o vinculo e por citacao em pagina, e
    # cada ficha diz onde foi visto. Lista vazia e honesto: nao ha campo que diga
    # "cliente X usa Miro" - ha pagina que cita.
    for nome, forn, nota in CANAIS:
        n += esc(os.path.join(pt, slug(nome) + u".md"), ficha(
            nome, u"**Canal / ferramenta de trabalho** \u2014 software de terceiro que a uMode "
                  u"opera. \U0001F534 **N\u00e3o \u00e9 produto da uMode e n\u00e3o \u00e9 ERP de cliente.**",
            forn, nota, [], u"\u26a0 **n\u00e3o se aplica**",
            u"\U0001F534 **O v\u00ednculo com cliente N\u00c3O vem de campo de base** \u2014 nenhuma base diz "
            u"quem usa o qu\u00ea. Vem de **cita\u00e7\u00e3o na p\u00e1gina do cliente**, e s\u00f3 existe onde a "
            u"p\u00e1gina foi aberta. **Lista vazia aqui significa \"n\u00e3o varrido\", nunca "
            u"\"n\u00e3o usado\".**"))

    for nome, forn, nota in TERCEIROS:
        cl = []
        for (c, st, _m, erps) in CARTEIRA:
            for e in erps:
                if e == nome or (e in COMPOSTOS and nome in COMPOSTOS[e]):
                    cl.append((c, st, e))
        extra = None
        comp = sorted(set(l for (_c, _s, l) in cl if l in COMPOSTOS))
        if comp:
            extra = [u"### ⚠ Vínculo por valor composto",
                     u"Parte dos clientes acima chega aqui por um valor **composto** do campo — "
                     + u" · ".join(u"`%s`" % x for x in comp) + u".",
                     u"**Não desmembrei o valor em dois vínculos:** a fonte não diz se o cliente usa os",
                     u"dois sistemas ou um para cada coisa. E as grafias `Linx / SAP` e `SAP e Linx`",
                     u"\U0001F534 **são o mesmo conceito escrito de dois jeitos** — defeito já registrado."]
        n += esc(os.path.join(pt, slug(nome) + u".md"), ficha(
            nome, u"**Sistema de terceiro** — ERP/integração do cliente. "
                  u"\U0001F534 **Não é produto da uMode.**",
            forn, nota, cl, u"⚠ **não se aplica** — é sistema de terceiro",
            u"O que conversa com ele é o módulo "
            u"[`Integração`](../../03_Produto-e-Solucoes/_ferramentas/integracao.md).", extra))

    # --- 3) os dois indices, com as DUAS leituras: por ferramenta e por cliente ---
    im = [(m, slug(m) + u".md", len([1 for (_c, _s, mods, _e) in CARTEIRA if m in mods]))
          for m in MODULOS]
    cm = {}
    for (c, _s, mods, _e) in CARTEIRA:
        cm[c] = u" · ".join(u"[%s](%s)" % (x, slug(x) + u".md") for x in mods)
    n += esc(os.path.join(pm, u"_indice.md"), indice(
        u"Ferramentas da uMode · índice",
        u"Os **7 módulos contratáveis** da plataforma uMode, como o campo "
        u"`Módulos Contratados` da base `Mapa de Clientes` os nomeia. "
        u"🔴 **São nomes legados do uFlow** — **não foram fundidos** com as "
        u"[16 Soluções do Portfólio](../_contexto/), porque o `CONTEXT.md` proíbe "
        u"inferir o mapeamento por nome parecido.",
        pm, im, cm, u"Módulos contratados"))

    it = [(nome, slug(nome) + u".md", 0) for nome, _f, _nt in CANAIS]
    for nome, _f, _nt in TERCEIROS:
        k = 0
        for (_c, _s, _m, erps) in CARTEIRA:
            for e in erps:
                if e == nome or (e in COMPOSTOS and nome in COMPOSTOS[e]):
                    k += 1
        it.append((nome, slug(nome) + u".md", k))
    ct = {}
    for (c, _s, _m, erps) in CARTEIRA:
        ct[c] = u" · ".join(
            (u"[%s](%s)" % (e, slug(e) + u".md")) if any(e == x for x, _f, _t in TERCEIROS)
            else u"`%s`" % e for e in erps)
    n += esc(os.path.join(pt, u"_indice.md"), indice(
        u"Sistemas de terceiro · índice",
        u"Os **sistemas de ERP/integração dos clientes**. "
        u"🔴 **Nenhum é produto da uMode** — por isso não vivem em "
        u"`03_Produto-e-Solucoes`. Valores como `Sem Integração`, `Não`, "
        u"`Linx / SAP` e `SAP e Linx` aparecem **entre crases**: são valores do campo, "
        u"não sistemas — e **não foram desmembrados nem fundidos.**",
        pt, it, ct, u"`ERP/Integração`"))

    print(u"fichas de ferramenta criadas/atualizadas: %d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
