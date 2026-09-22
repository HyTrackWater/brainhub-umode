# -*- coding: utf-8 -*-
u"""
gera-fichas-pessoa.py - cria UMA FICHA POR PESSOA de cliente.

Decisao do Vinicius em 22 set 2026, textual: "cada pessoa tem sim que ser um
arquivo e realmente ter varios outros nos com ela. Isso nao tem duvida."

Ate aqui, pessoa de cliente era LINHA DE TABELA dentro de `pessoas.md`. Linha de
tabela nao e no de grafo: nao pode ser apontada, nao pode apontar, e nao pode
ligar a ferramenta, area ou demanda. Com ficha, pode.

Fonte: as tabelas `#### Solicitantes de demanda` que a varredura de 22 set 2026
escreveu no `pessoas.md` de cada cliente, a partir do campo `Quem solicitou?` das
demandas. Cada linha vira uma ficha.

O que NAO faz:
  - nao inventa cargo, area, e-mail nem nada que a fonte nao diga;
  - nao unifica grafias (regra do protocolo-varredura-cliente.md secao 9:
    suspeita se levanta, fusao so com confirmacao humana);
  - nao cria ficha para valor que nao e pessoa (area, time, agente, canal).

Estrutura: a MESMA do `_pessoas/_template_pessoa.md`, porque CLAUDE.md trava que
"Areas e Pessoas sao iguais entre Casa e clientes". Campo que so faz sentido para
a Casa fica marcado como nao aplicavel, nao apagado.

Uso:  python scripts/gera-fichas-pessoa.py
"""
import io
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")

# Valores que aparecem na coluna de nome e NAO sao pessoa.
# CORRECAO de 22 set 2026: `hermes` SAIU desta lista.
# Eu o tinha filtrado presumindo que fosse o agente `Hermes` da uMode. A pagina
# da NK STORE no Notion mostra `Hermes Goncalves Santiago Junior - Gerente de TI`,
# pessoa real do cliente, com 5 demandas abertas. Presumir que um nome conhecido
# num contexto e o mesmo nome noutro contexto e exatamente o erro que a regra de
# ouro proibe. Homonimo entre agente e pessoa e problema de desambiguacao, e a
# desambiguacao se faz com fonte - nunca com um filtro cego por string.
NAO_PESSOA = set(u"""
compras estilo sourcing merchan planejamento negocios treinamento contrato
ka smb interno time supply faccao qualidade cadastro comercial
""".split())


def slug(s):
    s = unicodedata.normalize(u"NFKD", s).encode(u"ascii", u"ignore").decode(u"ascii")
    s = re.sub(u"[^a-zA-Z0-9]+", u"-", s).strip(u"-").lower()
    return s


def limpa(cel):
    u"""Tira negrito, backtick e emoji de uma celula de tabela."""
    c = cel.strip()
    c = c.replace(u"**", u"").replace(u"`", u"")
    c = re.sub(u"[\U0001F300-\U0001FAFF⚠✅❌]", u"", c)
    return c.strip()


def e_pessoa(nome):
    n = slug(nome).replace(u"-", u" ")
    if not n or len(n) < 2:
        return False
    for t in NAO_PESSOA:
        if n == t or n.startswith(t + u" ") or n.endswith(u" " + t):
            return False
    if u" e " in n or u"/" in nome or u"+" in nome:
        return False  # duas pessoas na mesma celula: nao desmembro sem confirmacao
    if u"umode" in n:
        return False  # pessoa da Casa nao se duplica dentro do cliente
    return True


# ---------------------------------------------------------------------------
# SEGUNDA FONTE: a pagina do cliente no Notion (toggle `Pessoas`).
#
# Achado de 22 set 2026: a base de demandas NAO e a unica fonte de pessoa, e
# nao e a melhor. Cada pagina de cliente tem um toggle `Pessoas` com um
# template de 4 blocos - Diretores/Representantes Legais, Responsavel pelo
# Financeiro, Responsaveis pelos Projetos, Responsavel Tecnologia - e quando
# esta preenchido traz NOME COMPLETO, CARGO e AREA.
#
# Ate 22 set 2026 eu afirmei que `cargo` e `area` nao tinham fonte no corpus
# (item 285/315). Tinham. Eu nao tinha aberto a pagina do cliente.
#
# NAO ENTRA AQUI, por decisao de dado sensivel (AGORA.md secao 8.1):
#   CPF, telefone pessoal e e-mail. Registro que existem e onde - nunca o valor.
#
# Formato: cliente -> [(nome como a pagina escreve, cargo, area, bloco)]
DA_PAGINA = {
    u"NK STORE": [
        (u"Alexandre de S\u00e1 Pereira", u"Representante Legal",
         u"Diretoria", u"Diretores e Representantes Legais"),
        (u"Gustavo Annechino de Souza e Almeida", u"Representante Legal",
         u"Diretoria", u"Diretores e Representantes Legais"),
        (u"Silvia Shirlei Dias", u"Respons\u00e1vel pelo Financeiro",
         u"Financeiro", u"Respons\u00e1vel pelo Financeiro"),
        (u"Regiane Konopka", u"Diretora de Merchandising \u2014 Compras, Industrial e Compliance",
         u"Merchandising", u"Diretoria Respons\u00e1vel pelo Projeto"),
        (u"Larissa Cid Castilho Batista", u"Gerente de Projeto / Gerente de Produto",
         u"`[a preencher]`", u"L\u00edderes Respons\u00e1veis pelo Projeto"),
        (u"Marina Sacramento", u"PMO \u2014 Compradora de Produtos Acabados",
         u"Compras", u"L\u00edderes Respons\u00e1veis pelo Projeto"),
        (u"Stella Sunaga", u"Diretora de Estilo", u"Estilo",
         u"L\u00edderes de Departamentos"),
        (u"Samuel", u"Coordenador de Estilo", u"Estilo", u"L\u00edderes de Departamentos"),
        (u"Julia", u"Coordenadora de Estilo", u"Estilo", u"L\u00edderes de Departamentos"),
        (u"Robson Bazan", u"Gerente Industrial \u2192 PCP", u"PCP",
         u"L\u00edderes de Departamentos"),
        (u"Andressa", u"Coordenadora do PCP", u"PCP", u"L\u00edderes de Departamentos"),
        (u"Bruna", u"Coordenadora do Planejamento", u"Planejamento",
         u"L\u00edderes de Departamentos"),
        (u"Hermes Gon\u00e7alves Santiago Junior", u"Gerente de TI", u"Tecnologia",
         u"Respons\u00e1vel Tecnologia"),
    ],
}

# Observacao por pessoa, quando a fonte diz algo que nao cabe em cargo/area.
NOTA_PAGINA = {
    (u"NK STORE", u"Larissa Cid Castilho Batista"): u"a fonte anota: *\"J\u00e1 implantou PLM em v\u00e1rias empresas\"*",
    (u"NK STORE", u"Stella Sunaga"): u"a fonte anota: *\"H\u00e1 10 anos na empresa\"*",
    (u"NK STORE", u"Andressa"): u"\u26a0 a fonte anota: *\"Se ela est\u00e1 feliz com o projeto, estamos bem\"* \u2014 **\u00e9 termometro de projeto, dito pela pr\u00f3pria uMode**",
}


# ---------------------------------------------------------------------------
# TERCEIRA FONTE: a TABELA DE USUARIOS da pagina do cliente.
# Achada em 22 set 2026 na Puket. Nome + e-mail corporativo + perfil + data.
# E a unica fonte que da DATA DE ATIVACAO por pessoa, e a unica com chave de
# identidade. Formato: cliente -> [(nome, email, perfil, ativo_desde, obs)]
DA_PLATAFORMA = {
    u"Puket": [
        (u"Michele Lunkes", u"michele.lunkes@grupounico.com", u"Sourcing Nacional", u"02/12/2022", u""),
        (u"Yves", u"yves.pancotti@puket.com.br", u"Produto", u"02/02/2023", u""),
        (u"Tayna Basile", u"tayna.basile@puket.com.br", u"Design", u"03/06/2022", u""),
        (u"pedro.pereira", u"pedro.pereira@puket.com.br", u"Design", u"03/06/2022", u""),
        (u"gabriela.araujo", u"gabriela.araujo@puket.com.br", u"Design", u"03/06/2022", u""),
        (u"vinicius.cesar", u"vinicius.cesar@grupounico.com", u"BI", u"04/10/2022", u""),
        (u"rosimare.simoes", u"rosimare.simoes@puket.com.br", u"TEX", u"09/06/2022", u""),
        (u"vanessa.facci", u"vanessa.facci@puket.com.br", u"Estilo", u"09/06/2022", u""),
        (u"isadora.koch", u"isadora.koch@grupounico.com", u"Certifica\u00e7\u00e3o", u"09/06/2022", u""),
        (u"luciene.comenalli", u"luciene.comenalli@grupounico.com", u"Sourcing Nacional", u"09/06/2022", u""),
        (u"catarina.bassotto", u"catarina.bassotto@grupounico.com", u"Produto", u"09/06/2022", u""),
        (u"giuliana.zuttion", u"giuliana.zuttion@puket.com.br", u"Estilo", u"09/06/2022", u""),
        (u"ana.ballestero", u"ana.ballestero@grupounico.com", u"Qualidade", u"09/06/2022", u""),
        (u"andreza.zan", u"andreza.zan@grupounico.com", u"Sourcing Nacional", u"09/06/2022", u""),
        (u"renata.ortiz", u"renata.ortiz@puket.com.br", u"Estilo", u"09/06/2022", u""),
        (u"girlaine.rocha", u"girlaine.rocha@puket.com.br", u"TEX", u"09/06/2022", u""),
        (u"gabriela.fonseca", u"gabriela.fonseca@puket.com.br", u"Estilo", u"10/06/2022", u""),
        (u"audria.monteiro", u"audria.monteiro@grupounico.com", u"Sourcing Nacional", u"10/06/2022", u""),
        (u"giulia.gomes", u"giulia.gomes@puket.com.br", u"Estilo", u"13/06/2022", u""),
        (u"thalita.santana", u"thalita.santana@puket.com.br", u"Produto", u"14/12/2022", u""),
        (u"leticia.martins", u"leticia.martins@puket.com.br", u"Produto", u"14/06/2022", u""),
        (u"andressa.grilli", u"andressa.grilli@puket.com.br", u"Produto", u"14/06/2022", u""),
        (u"luciana.ribeiro", u"luciana.ribeiro@puket.com.br", u"PCP", u"16/08/2022", u""),
        (u"Carla", u"carla.luz@grupounico.com", u"Controladoria", u"16/06/2023", u""),
        (u"Sarah Nunes", u"sarah.nunes@grupounico.com", u"Controladoria", u"16/06/2023",
         u"\U0001F534 **O perfil est\u00e1 RISCADO na fonte** \u2014 marca de desativa\u00e7\u00e3o. "
         u"\u26a0 **N\u00e3o afirmo que saiu:** afirmo que a fonte riscou."),
        (u"Isabela Pereira", u"isabela.cipriani@grupounico.com", u"Importa\u00e7\u00e3o", u"19/06/2023",
         u"\u26a0 **nome e e-mail divergem** (`Pereira` \u00d7 `cipriani`) \u2014 n\u00e3o resolvi"),
        (u"karina.ossugui", u"karina.ossugui@puket.com.br", u"Design", u"20/12/2022", u""),
        (u"aline.soares", u"aline.soares@puket.com.br", u"Estilo", u"20/06/2022", u""),
        (u"leticia.lopes", u"leticia.lopes@puket.com.br", u"Estilo", u"20/06/2022", u""),
        (u"Marcela Polyana", u"marcela.figueiredo@puket.com.br", u"Produto", u"20/06/2022",
         u"\u26a0 **nome e e-mail divergem** (`Polyana` \u00d7 `figueiredo`) \u2014 n\u00e3o resolvi"),
        (u"andressa.duarte", u"andressa.duarte@puket.com.br", u"Produto", u"21/06/2022", u""),
        (u"Eduarda de Souza", u"eduarda.souza@grupounico.com", u"Importa\u00e7\u00e3o", u"21/06/2023", u""),
        (u"lara.cunha", u"lara.cunha@grupounico.com", u"Qualidade", u"21/09/2022", u""),
        (u"luiza.pavanate", u"luiza.pavanate@grupounico.com", u"Qualidade", u"21/09/2022", u""),
        (u"jessica.cesar", u"jessica.cesar@grupounico.com", u"Sourcing Nacional", u"22/06/2022", u""),
        (u"andrea.nunes", u"andrea.nunes@grupounico.com", u"Sourcing Nacional", u"23/06/2022", u""),
        (u"paulo.pelaes", u"paulo.pelaes@grupounico.com", u"Qualidade", u"23/09/2022", u""),
        (u"maria.germano", u"maria.germano@grupounico.com", u"Projetos", u"24/05/2022", u""),
        (u"gabriela.begnini", u"gabriela.begnini@grupounico.com", u"Projetos", u"24/05/2022", u""),
        (u"Eli", u"elisangela.silva@puket.com.br", u"Projetos", u"24/05/2023", u""),
        (u"andrea.mendes", u"andrea.mendes@grupounico.com", u"Projetos", u"25/11/2022", u""),
        (u"Romina Torres", u"romina.torres@puket.com.br", u"Sourcing Nacional", u"27/04/2023", u""),
        (u"natasha.maruno", u"natasha.maruno@grupounico.hk", u"Estilo", u"30/06/2022",
         u"\u26a0 **dom\u00ednio `.hk`** \u2014 Hong Kong. \u00danica da carteira fora do Brasil."),
    ],
}


def casa_plataforma(cliente, nome_curto):
    u"""Casa um nome da base de demandas com a tabela de usuarios da plataforma.

    Casa por primeiro nome OU pela parte local do e-mail. Ambiguidade devolve
    None: suspeita se levanta, fusao so com confirmacao humana.
    """
    alvo = slug(nome_curto)
    hits = []
    for r in DA_PLATAFORMA.get(cliente, ()):
        if slug(r[0]).split(u"-")[0] == alvo or slug(r[1].split(u"@")[0]) == alvo:
            hits.append(r)
    return hits[0] if len(hits) == 1 else None


def casa_pagina(cliente, nome_curto):
    u"""Acha o registro da pagina para um nome da base de demandas.

    A base de demandas escreve primeiro nome (`Andressa`); a pagina escreve nome
    completo (`Hermes Goncalves Santiago Junior`). Caso o primeiro nome bata com
    MAIS DE UM registro, devolve None: ambiguidade se declara, nao se resolve no
    palpite (mesma regra da secao 9 do protocolo).
    """
    alvo = slug(nome_curto)
    hits = [r for r in DA_PAGINA.get(cliente, ()) if slug(r[0]).split(u"-")[0] == alvo]
    return hits[0] if len(hits) == 1 else None


def ficha(cliente, nome, demandas, pri, ult, obs, pag=None, plat=None):
    L = []
    L.append(u"# %s · Pessoa · %s" % (cliente, nome))
    L.append(u"")
    L.append(u"> **Ficha gerada por `scripts/gera-fichas-pessoa.py` em 22 set 2026.**")
    L.append(u"> Campo sem fonte fica `[a preencher]` — **nada foi inferido.**")
    L.append(u"> **O nome está exatamente como aparece na fonte. Variantes não foram fundidas** —")
    L.append(u"> ver `protocolo-varredura-cliente.md` § 9.")
    L.append(u"")
    L.append(u"## Identificação")
    L.append(u"### Foto")
    L.append(u"`[a preencher]`")
    L.append(u"### Nome completo")
    if pag:
        L.append(u"**%s** \u2014 da p\u00e1gina do cliente. A base de demandas a escreve como `%s`."
                 % (pag[0], nome))
    else:
        L.append(u"`[a preencher]` \u2014 a fonte registra **`%s`**" % nome)
    L.append(u"### Nome preferido / como é chamado(a)")
    L.append(u"**%s**" % nome)
    L.append(u"### Email")
    if plat:
        L.append(u"**`%s`** — e-mail **corporativo**, da tabela de usuários da "
                 u"plataforma." % plat[1])
        L.append(u"")
        L.append(u"🟢 **É a chave de identidade desta pessoa** — o que resolve "
                 u"grafia diferente sem inventar gente (item 252). Tier `T2`.")
        L.append(u"")
        L.append(u"⚠ **E-mail corporativo entra; e-mail pessoal, telefone e CPF não** "
                 u"— `AGORA.md` § 8.1.")
    elif pag:
        L.append(u"🔴 **Existe na página do cliente e NÃO foi replicado aqui.**")
        L.append(u"Mesma decisão vale para telefone e CPF — `AGORA.md` § 8.1.")
        L.append(u"**Registro que existe e onde; o valor fica na fonte.**")
    else:
        L.append(u"`[a preencher]`")
    L.append(u"### Cadeira / cargo atual")
    if pag:
        L.append(u"**%s**" % pag[1])
        L.append(u"")
        L.append(u"Fonte: p\u00e1gina do cliente no Notion, toggle `Pessoas` \u203a `%s`." % pag[3])
    else:
        L.append(u"`[a preencher]` \u2014 \u26a0 **esta pessoa n\u00e3o aparece no toggle `Pessoas` da")
        L.append(u"p\u00e1gina do cliente**, que \u00e9 onde o cargo vive quando existe.")
    L.append(u"### Nível HIC")
    L.append(u"⚠ **não se aplica** — é campo da Casa uMode")
    L.append(u"### \u00c1rea (organizacional)")
    if plat:
        L.append(u"**%s** — **`Perfil de Acesso`** na tabela de usuários da plataforma."
                 % plat[2])
        L.append(u"")
        L.append(u"⚠ **Perfil de acesso NÃO é área canônica** — é como o "
                 u"cliente nomeia. **Não mapeei para a grade de 14** sem sua confirmação.")
    elif pag:
        L.append(u"**%s** — ⚠ **como a fonte a nomeia**, não necessariamente uma das"
                 % pag[2])
        L.append(u"14 áreas canônicas. **Não mapeei para a grade** sem sua confirmação.")
    else:
        L.append(u"`[a preencher]` — 🔴 **o vínculo pessoa e área é a "
                 u"lacuna aberta do corpus**")
    L.append(u"### Data de entrada na uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"### Status na uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"### Data de saída da uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"")
    L.append(u"## Papel")
    L.append(u"### Missão da cadeira")
    L.append(u"`[a preencher]`")
    L.append(u"### Responsabilidades principais")
    L.append(u"`[a preencher]`")
    L.append(u"### Interfaces")
    L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Histórico")
    L.append(u"### Áreas de atuação histórica")
    L.append(u"`[a preencher]`")
    L.append(u"### Clientes atuais atendidos")
    L.append(u"⚠ **não se aplica** — esta pessoa **é** do cliente `%s`" % cliente)
    L.append(u"### Clientes atendidos historicamente")
    L.append(u"⚠ **não se aplica**")
    L.append(u"")
    L.append(u"## Personificação")
    for h in (u"Como se descreve", u"Personalidade / forma de trabalhar",
              u"O que a diferencia", u"Curiosidade / algo pessoal"):
        L.append(u"### %s" % h)
        L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Competências")
    for h in (u"Experiência profissional anterior", u"Skills / habilidades técnicas",
              u"Cursos e certificações", u"Ferramentas e plataformas que domina"):
        L.append(u"### %s" % h)
        L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Atividade observada")
    L.append(u"")
    L.append(u"> **Uma pessoa não é ativa porque tem cadastro. É ativa porque agiu, numa data que")
    L.append(u"> dá para citar.**")
    L.append(u"")
    L.append(u"| Sinal | Valor |")
    L.append(u"|---|---|")
    L.append(u"| **Demandas abertas** | **%s** |" % demandas)
    L.append(u"| Primeira atividade observada | %s |" % (pri or u"`[a preencher]`"))
    L.append(u"| Última atividade observada | %s |" % (ult or u"`[a preencher]`"))
    L.append(u"| Fonte | campo `Quem solicitou?` da base de demandas do Notion |")
    if plat:
        L.append(u"| **Ativo na plataforma desde** | **%s** |" % plat[3])
        L.append(u"| Fonte | tabela de usuários da página do cliente |")
    if obs and obs != u"—":
        L.append(u"")
        L.append(u"**Observação da fonte:** %s" % obs)
    L.append(u"")
    L.append(u"## Governança")
    L.append(u"### Quem pode alterar este documento")
    L.append(u"Responsável de atendimento + liderança de Atendimento uMode")
    L.append(u"")
    return u"\n".join(L) + u"\n"


def main():
    criadas = 0
    clientes = 0
    for c in sorted(os.listdir(CLI)):
        base = os.path.join(CLI, c)
        pm = os.path.join(base, u"00_Institucional", u"_contexto", u"pessoas.md")
        if not os.path.exists(pm):
            continue
        s = io.open(pm, encoding="utf-8").read()
        if u"#### Solicitantes de demanda" not in s:
            continue
        bloco = s[s.index(u"#### Solicitantes de demanda"):]
        fim = bloco.find(u"\n## ")
        if fim > 0:
            bloco = bloco[:fim]
        destino = os.path.join(base, u"00_Institucional", u"_pessoas")
        if not os.path.isdir(destino):
            os.makedirs(destino)
        n_cli = 0
        usados = set()
        usados_plat = set()
        for linha in bloco.split(u"\n"):
            if not linha.startswith(u"| ") or linha.startswith(u"|---") or u"Demandas |" in linha:
                continue
            cels = [limpa(x) for x in linha.strip().strip(u"|").split(u"|")]
            if len(cels) < 5:
                continue
            nome = cels[0]
            if not e_pessoa(nome):
                continue
            pag = casa_pagina(c, nome)
            plat = casa_plataforma(c, nome)
            if plat:
                usados_plat.add(plat[1])
            if pag:
                usados.add(pag[0])
            p = os.path.join(destino, slug(nome) + u".md")
            novo = ficha(c, nome, cels[1], cels[2], cels[3],
                         cels[4] if len(cels) > 4 else u"", pag, plat)
            if os.path.exists(p) and io.open(p, encoding="utf-8").read() == novo:
                continue
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1
        # Pessoa que aparece na PAGINA do cliente e nunca abriu demanda
        # tambem e pessoa. Ate aqui ela nao existia no corpus: a base de
        # demandas era a unica fonte, e quem nao abre chamado ficava invisivel.
        for r in DA_PAGINA.get(c, ()):
            if r[0] in usados:
                continue
            p = os.path.join(destino, slug(r[0]) + u".md")
            novo = ficha(c, r[0], u"0", u"", u"",
                         u"nao aparece na base de demandas", r)
            if os.path.exists(p) and io.open(p, encoding="utf-8").read() == novo:
                continue
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1
        # Quem existe SO na tabela de usuarios da plataforma tambem e pessoa -
        # e traz o que nenhuma outra fonte traz: e-mail e data de ativacao.
        for r in DA_PLATAFORMA.get(c, ()):
            if r[1] in usados_plat:
                continue
            base_nome = r[0] if u" " in r[0] else r[1].split(u"@")[0].replace(u".", u" ")
            pth = os.path.join(destino, slug(r[1].split(u"@")[0]) + u".md")
            novo = ficha(c, base_nome, u"0", u"", u"",
                         r[4] or u"nao aparece na base de demandas", None, r)
            if os.path.exists(pth) and io.open(pth, encoding="utf-8").read() == novo:
                continue
            io.open(pth, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1

        if n_cli:
            clientes += 1
            print(u"  %-20s %3d fichas" % (c, n_cli))
    print(u"")
    print(u"fichas de pessoa de cliente criadas/atualizadas: %d em %d clientes"
          % (criadas, clientes))
    print(u"Rode `python scripts/gera-conexoes.py` em seguida para ligá-las ao grafo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
