# -*- coding: utf-8 -*-
u"""
preenche-areas-lb-nk-osklen.py - preenche as areas de Luiza Barcelos, NK STORE
e Osklen, os tres clientes com mais reunioes registradas (126, 111 e 101).

AS TRES SAO CASOS DIFERENTES, e o script trata cada uma como ela e:

  NK STORE       - tem tabela de usuarios: 29 pessoas em 5 perfis, com
                   contagem. E a fonte mais forte das tres.
  Luiza Barcelos - tem matriz de 4 perfis mas NAO tem tabela de pessoas.
                   Em compensacao tem prosa rica: times, cargos e escopo
                   nomeados na ata de Kick Off e nas Definicoes do Projeto.
  Osklen         - a pagina e TEMPLATE EM BRANCO. Pessoas, Jornada e CRM sao
                   so rotulos. E a unica em "Operacao Assistida" nessa
                   condicao, e isso e dado, nao lacuna de varredura.

RESSALVA QUE VIAJA COM O CONTEUDO DA NK. A descricao de processo por
departamento saiu de um bloco "Levantamentos e Pesquisa por IA dentro da
reuniao - IA Tactiq", dentro da ata. E SAIDA DE IA REGISTRADA NUMA ATA, nao
documento validado pelo cliente. Cada bloco que usa isso diz isso.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")

F_NK = u"página `NK STORE` e sua sub-página `Perfil de Usuário e Permissionamentos`, varridas em 23/09/2026"
F_LB = u"página `Luiza Barcelos` — ata do *Kick Off Interno* (06/06/2024) e *Definições do Projeto*, varridas em 23/09/2026"
IA = (u"\n\n\U0001F534 **Ressalva de fonte:** este trecho saiu do bloco *\"Levantamentos e Pesquisa "
      u"por IA dentro da reunião — IA Tactiq\"*, dentro da ata. **É saída de IA registrada numa "
      u"ata, não documento validado pelo cliente.**")

CONTEUDO = {
 u"NK STORE": {
  u"02_Estilo-Criacao": u"""**Tem perfil próprio no PLM: `NK - Estilo` — e é o maior da conta, com 10 das 29 pessoas.**

> *"O departamento de estilo é encarregado de **desenvolver as peças de moda**, incluindo a criação de modelagens, escolha de tecidos e estampas, e realização de provas de roupa. Eles trabalham em colaboração com **fornecedores externos e a oficina interna** para produzir as peças."*

⚠ **A matriz de permissão usa outro nome:** `NK- Estilo Master` — **sem espaço depois de \"NK\"**. \U0001F534 **Perfil da matriz e perfil da tabela de usuários não coincidem** (§ abaixo).""" + IA,

  u"05_PCP": u"""**Tem perfil próprio: `NK - PCP` — 7 das 29 pessoas, o segundo maior da conta.**

> *"O departamento de PCP **coordena a produção interna e externa**, garantindo que os prazos sejam cumpridos e que a qualidade dos produtos seja mantida. Eles trabalham em estreita colaboração com a **oficina interna e as facções externas**."*

\U0001F534 **A qualidade é responsabilidade do PCP nesta conta**, não de uma área própria — não há perfil de Qualidade.

⚠ **A Coordenadora do PCP carrega uma nota literal na ficha de pessoas:** *\"(Se ela está feliz com o projeto, estamos bem)\"*.""" + IA,

  u"06_Compras-Supply-Sourcing": u"""**Tem perfil próprio: `NK - Compras` — 5 das 29 pessoas.**

> *"O departamento de compras é responsável por **adquirir a matéria-prima** necessária para a produção das peças de moda. Eles trabalham em estreita colaboração com o departamento de estilo."*

⚠ **Na matriz de permissão aparecem DOIS perfis de compras:** `Nk Compras Master` e `NK Compras` — **grafias diferentes, e nenhuma bate com `NK - Compras` da tabela de usuários.**

\U0001F534 **Há também um perfil `Fornecedor`** na matriz — acesso de terceiro, como na Oficina Reserva.""" + IA,

  u"13_Modelagem": u"""**Tem perfil próprio: `NK - Modelagem` — 4 das 29 pessoas, o menor perfil operacional.**

⚠ **A criação das modelagens, porém, é descrita como trabalho de Estilo**, não desta área:
> *"O departamento de estilo é encarregado de desenvolver as peças (...) incluindo a **criação de modelagens**."*

\U0001F534 **Perfil existe, atribuição está descrita noutra área.** ⚠ **Confirmar com o atendimento quem faz o quê.**""" + IA,

  u"01_Planejamento": u"""\U0001F534 **Não tem perfil de acesso próprio**, mas é descrito como **o ponto de partida de todo o fluxo da conta**:

> *"O departamento de planejamento é responsável por **definir as estratégias de coleção**, selecionar as marcas e produtos a serem incluídos, e realizar o **cadastro dos produtos** no sistema."*
> *"Planejamento: é o ponto de partida para **ambos os fluxos**, definindo as coleções e direcionando o desenvolvimento e a curadoria."*

⚠ **A conta tem uma Coordenadora do Planejamento nomeada** na lista de participantes.""" + IA,

  u"08_Ecommerce-Cadastro": u"""⚠ **Não há perfil de acesso nem departamento próprio.** O cadastro é descrito como tarefa do **Planejamento**:

> *"(Planejamento) realizar o **cadastro dos produtos no sistema**."*

⚠ **E o canal digital aparece sob Merchandising:**
> *"(Merchandising) também são responsáveis por garantir que os produtos estejam disponíveis nas **lojas físicas e no site** da empresa."*""" + IA,
 },

 u"Luiza Barcelos": {
  u"02_Estilo-Criacao": u"""**É uma das oito áreas sob a Diretoria Criativa**, e tem Gerente de Estilo nomeado no projeto.

> **Times Envolvidos:** *\"Diretoria Criativa — **Estilo** · Desenvolvimento · Produto e Merchandising · Suprimentos · Operações (Cadastro, Precificação) · Estratégia, Processos e Projetos · Tecnologia\"*

\U0001F7E2 **A expectativa do Gerente de Estilo está registrada literalmente:**
> *\"Animado com a implementação da Ferramenta — Expectativas: **Foco na Coleção e Estilo / Eficiência no Setor**\"*

⚠ **A Diretora Criativa nomeia uma oportunidade e um fracasso anterior:**
> *\"Expectativa maior é gerar inovação no processo criativo (...) **Oportunidade: Processo de Pesquisa — Fizeram várias tentativas, com várias ferramentas, e não tiveram sucesso.**\"*""",

  u"03_Desenvolvimento-de-Colecao": u"""**É `Desenvolvimento` na estrutura da Diretoria Criativa**, com Gerente de Desenvolvimento de Produto nomeado.

\U0001F534 **A tese do projeto inteiro está nesta área, dita na ata de 06/06/2024:**
> *\"**Processo está na cabeça da Marcinha** (Luiza Barcelos) → Missão é tirar as informações da cabeça dela e colocar na ferramenta.\"*

⚠ **E a complexidade declarada:**
> *\"Complexidade de varejo — **fábrica, produto acabado, importado**\"* · *\"Tem **fábrica própria**\"* · *\"Varejo, Atacado, Omnichannel\"*""",

  u"06_Compras-Supply-Sourcing": u"""**É `Suprimentos` na estrutura da Diretoria Criativa**, com Gerente de Levantamento de Suprimentos nomeado.

⚠ **Foi a única área que NÃO coube na agenda presencial do Kick Off:**
> *\"Fechar agenda da **reunião online com Suprimentos**.\"*

\U0001F534 **E aparece com outro nome na ata de Kick Off Interno:** *\"Times: Estilo, PCP, **Compras**\"* — **`Compras` e `Suprimentos` são o mesmo time com dois nomes na mesma página.**""",

  u"07_Logistica-CD": u"""\U0001F534 **A logística está sob o Gerente de Operação do Sul, e o escopo dele é declarado literalmente:**

> *\"**Logística e Cadastro** — Desenvolvimento até a Precificação está no guarda-chuvas dele\"*

⚠ **É um cargo que atravessa quatro áreas canônicas** — `07_Logistica-CD`, `08_Ecommerce-Cadastro`, `03_Desenvolvimento-de-Colecao` e `11_Financeiro`. **Não dá para atribuir por área sem quebrar o cargo.**""",

  u"08_Ecommerce-Cadastro": u"""**É `Cadastro`, uma das duas subáreas de `Operações`** na estrutura da Diretoria Criativa.

> **Times Envolvidos:** *\"Operações — **Cadastro** · Precificação\"*

⚠ **Há pessoa nomeada só como \"Cadastro\"** na lista de participantes, e o Gerente de Operação do Sul declara ter `Cadastro` no escopo dele.""",

  u"11_Financeiro": u"""**É `Precificação`, a outra subárea de `Operações`** — e é a única função de natureza financeira nomeada no projeto.

> **Times Envolvidos:** *\"Operações — Cadastro · **Precificação**\"*
> *\"Desenvolvimento até a **Precificação** está no guarda-chuvas dele\"* — Gerente de Operação do Sul

\U0001F534 **Não há menção a Financeiro, contabilidade ou faturamento** em nenhum bloco da página.""",

  u"14_Engenharia": u"""⚠ **Não há área de Engenharia. O que existe é `Tecnologia`**, uma das oito da Diretoria Criativa, com **Coordenador de Sistemas e Tecnologia** nomeado.

\U0001F534 **E há uma cláusula contratual sobre integração que mora aqui:**
> *\"**Não faz parte do escopo deste contrato a integração com o sistema LINX** ou qualquer outro que não seja o sistema SAFETECH.\"*

⚠ **A linha `Integração` está \U0001F534 para TODOS os quatro perfis da matriz — inclusive `LB - Admin`.** **É coerente com a cláusula.**""",

  u"09_Comercial-Vendas": u"""**É parte de `Produto e Merchandising`**, e o **Coordenador de Merchandising é o Líder Central do Projeto** — não um papel periférico.

> **Times Envolvidos:** *\"Diretoria Criativa — (...) **Produto e Merchandising**\"*

⚠ **A conta opera três canais:** *\"**Varejo, Atacado, Omnichannel**\"* (Kick Off Interno, 06/06/2024).

\U0001F534 **`Merchandising` não cabe nas 14 áreas canônicas** — e este é mais um cliente onde ele aparece. **Ver `_pendencias-gerais.md`.**""",

  u"12_Design": u"""⚠ **Não há área de Design nomeada. O que existe é a `Diretoria Criativa`**, que é o guarda-chuva de oito áreas — não uma área de desenho.

\U0001F534 **A Diretora Criativa nomeia o problema criativo da conta:**
> *\"Expectativa maior é gerar **inovação no processo criativo, trazendo agilidade e gestão sem perder a criatividade**. Oportunidade: **Processo de Pesquisa** — Fizeram várias tentativas, com várias ferramentas, e não tiveram sucesso.\"*

⚠ **Pesquisa de referência é a dor criativa declarada, e nenhuma ferramenta resolveu até hoje.**""",
 },
}

# Osklen e um caso a parte: nao ha o que preencher, e a ausencia e o achado.
OSKLEN = u"""\U0001F534 **A página da Osklen no Notion é TEMPLATE EM BRANCO** — varrida em 23/09/2026.

Os blocos `Pessoas`, `Jornada do Cliente e seus Marcos` e `CRM → Anotações Gerais` existem e contêm **apenas os rótulos do modelo**, sem nenhum dado:
> *\"Diretores e Representantes Legais — Nome: / Cargo: / E-mail: / Telefone:\"*
> *\"Jornada do Cliente Resumida · Output de cada marco\"*

\U0001F534 **E não há página de perfil de usuário da Osklen** — nem na página do cliente, nem na busca do workspace, que retorna essa página para **Luiza Barcelos, Cambos, NK STORE, Moda Objetiva, Oficina Reserva e Recco**. ⚠ **Não afirmo que não exista: não encontrei no Notion.** O Drive de Operação da conta não foi aberto.

\U0001F534 **A conta está em `Operação Assistida` com 101 reuniões registradas** — a terceira mais atendida da carteira — **e a página dela não tem estrutura.** ⚠ **O material real parece estar fora do Notion.**

⚠ **O único conteúdo datado da página tem interrogação na própria fonte:**
> *\"uFlow — início: Fevereiro 2025 · entrega: **Junho ou Agosto 2025???**\"* · *\"uBuy — início: Janeiro 2026 · entrega: **+d???**\"*
"""

PROC = {
 u"NK STORE": u"| O que a área faz, perfis e contagem de pessoas | Notion — `NK STORE` + `Perfil de Usuário e Permissionamentos` | varrido 23/09/2026 |",
 u"Luiza Barcelos": u"| O que a área faz, times, cargos e escopo | Notion — `Luiza Barcelos`, ata do *Kick Off Interno* e *Definições do Projeto* | 06/06/2024 · varrido 23/09/2026 |",
 u"Osklen": u"| Estrutura da conta | Notion — página `Osklen`, **template em branco** | varrido 23/09/2026 |",
}


def substitui_secao(txt, titulo, novo):
    for nivel in (u"\n## ", u"\n### "):
        marca = nivel + titulo + u"\n"
        if marca in txt:
            antes, resto = txt.split(marca, 1)
            corte = len(resto)
            for h in (u"\n## ", u"\n### "):
                i = resto.find(h)
                if i != -1:
                    corte = min(corte, i)
            return antes + marca + u"\n" + novo + u"\n" + resto[corte:], True
    return txt, False


MODULOS = (u"| Módulos e produto conectado | Notion — base `Mapa de Clientes` "
           u"| varrido 23/09/2026 |")


def anexa_procedencia(txt, linha):
    # duas linhas, porque sao duas fontes: a ata diz o que a area faz,
    # a base diz quais modulos a conta tem. Misturar seria atribuir a
    # uma o que veio da outra.
    for l in (linha, MODULOS):
        txt = _anexa(txt, l)
    return txt


def _anexa(txt, linha):
    if linha[:46] in txt:
        return txt
    marca = u"### Procedência\n"
    if marca not in txt:
        alvo = u"## Governança"
        if alvo not in txt:
            return txt
        nova = u"### Procedência\n| Bloco | Fonte | Data |\n|---|---|---|\n" + linha + u"\n\n"
        return txt.replace(alvo, nova + alvo, 1)
    antes, resto = txt.split(marca, 1)
    linhas = resto.split(u"\n")
    fim = 0
    for i, l in enumerate(linhas):
        if l.strip().startswith(u"|"):
            fim = i + 1
        elif fim:
            break
    return antes + marca + u"\n".join(linhas[:fim] + [linha] + linhas[fim:])


def main():
    escritos, blocos, falhas = 0, 0, []

    for cliente, areas in sorted(CONTEUDO.items()):
        for area, corpo in sorted(areas.items()):
            caminho = os.path.join(CLI, cliente, area, u"_contexto", u"contexto-area.md")
            if not os.path.exists(caminho):
                falhas.append((cliente, area, u"arquivo nao existe"))
                continue
            txt = io.open(caminho, encoding=u"utf-8").read()
            antes = txt
            txt, ok = substitui_secao(txt, u"O que esta área faz", corpo)
            if ok:
                blocos += 1
            else:
                falhas.append((cliente, area, u"secao nao encontrada"))
            txt = anexa_procedencia(txt, PROC[cliente])
            if txt != antes:
                io.open(caminho, u"w", encoding=u"utf-8").write(txt)
                escritos += 1

    # Osklen: a mesma declaracao de vazio verificado nas 14 areas
    base = os.path.join(CLI, u"Osklen")
    for area in sorted(os.listdir(base)):
        caminho = os.path.join(base, area, u"_contexto", u"contexto-area.md")
        if not os.path.exists(caminho):
            continue
        txt = io.open(caminho, encoding=u"utf-8").read()
        antes = txt
        txt, ok = substitui_secao(txt, u"O que esta área faz", OSKLEN)
        if ok:
            blocos += 1
        txt = anexa_procedencia(txt, PROC[u"Osklen"])
        if txt != antes:
            io.open(caminho, u"w", encoding=u"utf-8").write(txt)
            escritos += 1

    w = sys.stdout.write
    w(u"arquivos escritos : %d\n" % escritos)
    w(u"blocos escritos   : %d\n" % blocos)
    if falhas:
        w(u"\U0001F534 falhas:\n")
        for c, a, m in falhas:
            w(u"   - %s / %s: %s\n" % (c, a, m))
        return 1
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
