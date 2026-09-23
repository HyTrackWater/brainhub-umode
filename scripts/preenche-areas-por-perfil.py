# -*- coding: utf-8 -*-
u"""
preenche-areas-por-perfil.py - escreve no corpus as areas de VIX, Cambos,
Lenny Niemeyer, Recco, Moda Objetiva e NV, a partir das paginas de
`Perfil de Usuario e Permissionamentos` de cada uma.

NOVE clientes tem essa pagina. Oficina Reserva e NK STORE ja foram escritas;
estas seis fecham o conjunto.

O QUE A FONTE E. Matriz de permissao por perfil e por campo, mantida pelo
time de Atendimento. E a fonte mais forte que existe para "quem faz o que"
dentro do PLM de um cliente - melhor que ata, porque e configuracao aplicada.

O QUE ELA NAO E. Nao diz quantas PESSOAS ha em cada perfil (so a NK STORE e
a Caedu tem tabela de usuarios), e nao diz o organograma do cliente: diz o
que cada perfil PODE fazer no sistema. Perfil e area canonica nao sao a mesma
coisa - a Oficina Reserva ja provou isso.

TRES ACHADOS QUE MUDAM LEITURA, e cada um esta escrito na area afetada:
  - VIX tem CINCO perfis de Estilo, segmentados por LINHA DE PRODUTO.
  - Lenny e Recco nao tem segmentacao por area nenhuma: so Admin/Time/
    Fornecedor. As duas estao em Churn.
  - NV e a unica com perfil de Logistica e de Marketing, e a unica com aba
    de E-commerce na ficha.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")

FONTE = {
 u"VIX": (u"`[Vix] Perfil de Usuário e Permissionamento`", u"09/07/2025"),
 u"Cambos": (u"`Perfil de Usuário e Permissionamentos`", u"15/06/2026"),
 u"Lenny Niemeyer": (u"`Lenny | Perfil de Usuários e Permissionamentos`", u"21/07/2025"),
 u"Recco": (u"`Recco | Perfil de Usuários e Permissionamentos`", u"28/07/2025"),
 u"Moda Objetiva": (u"`Perfil de Usuário e Permissionamentos - Moda Objetiva`", u"29/07/2026"),
 u"NV": (u"`[NV] Permissionamento`", u"12/02/2025"),
}


def rod(cliente):
    doc, data = FONTE[cliente]
    return (u"\n\n⚠ **Fonte:** Notion — %s, lida em %s. **É matriz de permissão aplicada no "
            u"PLM, não organograma do cliente.**" % (doc, data))


V, C, L, R, O, N = u"VIX", u"Cambos", u"Lenny Niemeyer", u"Recco", u"Moda Objetiva", u"NV"

CONTEUDO = {
 V: {
  u"02_Estilo-Criacao": u"""\U0001F534 **A VIX segmenta Estilo por LINHA DE PRODUTO — são CINCO perfis, e nenhum outro cliente do corpus faz isso:**

`Vix-Estilo Biquini` · `Vix-Estilo Cover ups` · `Vix-Estilo PA` · `Vix-Estilo Roupas` · `Vix- Estilo Admim`

⚠ **`Vix- Estilo Admim`** tem espaço a mais e **\"Admim\" por \"Admin\"** — erro de digitação na origem. **A coluna está vazia em quase tudo:** a única célula preenchida é \U0001F7E2 em *\"Enviar para integração Linx\"*.

\U0001F534 **A conta tem DUAS fichas distintas** — `Ficha de PRODUTO` e `Ficha de ESTAMPA` — **cada uma com sua própria matriz de permissão.** É a única assim no corpus.""",

  u"04_Qualidade": u"""**Tem perfil próprio — e ele aparece com TRÊS grafias diferentes, uma por matriz:**

| Matriz | Grafia literal |
|---|---|
| Perfil de Usuário | `Vix- Qualidade` |
| Ficha de PRODUTO | `Vix qualidade` |
| Ficha de ESTAMPA | \U0001F534 `Vix qualdiade` — **letras trocadas** |

\U0001F534 **Três grafias do mesmo perfil, na mesma página.** ⚠ **Qualquer cruzamento por nome de perfil falha aqui** — e falha em silêncio.

⚠ **A ficha tem aba `Provas` e `Alterações Pós Lacre`**, que são etapas de controle desta área.""",

  u"13_Modelagem": u"""**Tem perfil próprio: `Vix-CAD`**, e a ficha de produto separa três abas que noutros clientes são uma só:

`Modelagem` · `CAD` · `Tabela de Medidas` · `Grade`

⚠ **Há também um perfil `Vix-Tabela`**, cujo escopo a fonte não explica. \U0001F534 **Não afirmo que seja tabela de medidas** — o nome sugere, a fonte não diz.""",

  u"05_PCP": u"""**Tem perfil próprio: `Vix-PCP`.**

⚠ **A ficha tem aba `Lotes` e `Alterações Pós Lacre`** — controle de produção depois do lacre, que é etapa típica desta área.""",

  u"06_Compras-Supply-Sourcing": u"""**Tem perfil próprio: `Vix-Compras`**, e a ficha traz `Fornecedor` e `Materiais em Desenvolvimento` como abas.

⚠ **Os relatórios de pendência são dois, e separam produto de material:** *\"Linx Produtos pendentes\"* e *\"Linx Materiais pendentes\"*.""",

  u"03_Desenvolvimento-de-Colecao": u"""**Tem perfil próprio: `Vix-Desenvolvimento`**, e há também `Vix-Produto TP`, cujo significado de `TP` a fonte **não explica**.

\U0001F534 **Seis funcionalidades estão desligadas para TODOS os perfis:** `Tipo de Produto` · `Campo Personalizado` · `Integração` · `Manual` · `Base de Importação` · `Excluir variante`.

⚠ **E a página registra o contorno operacional disso, literalmente:**
> *\"Quando um usuário que não tem permissionamento para deletar variante do produto fizer a solicitação no chat/atendimento, **pedir que faça a solicitação internamente**, para um usuário que tenha permissão.\"*""",

  u"14_Engenharia": u"""⚠ **Há um perfil `Vix-Ficha Tecnica`**, e a ficha tem aba `Ficha Técnica` própria.

\U0001F534 **Não afirmo que isso seja a área de Engenharia.** Em outros clientes a ficha técnica é responsabilidade dividida entre Estilo, Modelagem e Produto. **É pergunta para o atendimento.**

\U0001F534 **E há um perfil `uDash`** — único nome que **não segue o padrão `Vix-*`**. ⚠ **Aparenta ser perfil da própria uMode dentro da conta do cliente, como na Caedu. A página não explica.**""",
 },

 C: {
  u"03_Desenvolvimento-de-Colecao": u"""**Tem perfil próprio — e o nome muda entre as duas matrizes da MESMA página:**
`Cambos - Time Desenvolvimento` (matriz 1) × `Cambos - Desenvolvimento` (matriz 2).

\U0001F534 **A Cambos é facção, e a ficha dela prova isso.** A primeira linha do bloco Desenvolvimento é **`Todos os Clientes`** — nos outros clientes essa linha é *Todas as Coleções*. **Ela desenvolve para terceiros, não para marca própria.**

⚠ **As abas da ficha estão em CAIXA ALTA e trazem o termo do uFlow entre parênteses** — tradução do vocabulário da casa para o do produto:
`VERSÕES (Variante)` · `TECIDOS E AVIAMENTOS (Empenho)` · `TAMANHOS PILOTO (Grade)` · `QTD PARA PILOTAR (Lote)` · `FABRICAÇÃO (Fornecedor)` · `APROVAÇÕES DA PILOTO (Aprovações)` · `COSTURA E BORDADO` · `ORIGINAL` · `INTEGRAÇÃO SPI`

\U0001F7E2 **É um dicionário cliente↔produto escrito à mão, e é o único do corpus.**""",

  u"05_PCP": u"""\U0001F534 **PCP e Compras dividem UM único perfil: `Cambos - PCP/Compras`.**

**Não dá para separar as duas áreas pelo acesso** nesta conta — mesmo padrão de `Oficina - Ecommerce Marketing`.

⚠ **A ficha tem `QTD PARA PILOTAR (Lote)` e `TAMANHOS PILOTO (Grade)`**, que são controle de piloto.""",

  u"06_Compras-Supply-Sourcing": u"""\U0001F534 **Compras e PCP dividem UM único perfil: `Cambos - PCP/Compras`.**

⚠ **A integração com o SPI — sistema próprio da Cambos — tem cinco relatórios de pendência, e quatro são de suprimento:**
`[SPI] Aviamentos Pendentes` · `[SPI] Cores Pendentes` · `[SPI] Banhos Pendentes` · `[SPI] Fornecedores Pendentes` · `[SPI] Produtos Pendentes`

\U0001F7E2 **`Banhos` é vocabulário de beneficiamento** e não aparece em nenhum outro cliente.""",

  u"09_Comercial-Vendas": u"""**Tem perfil próprio: `Cambos - Comercial`.**

\U0001F534 **E há uma funcionalidade exclusiva desta conta, desligada para todos:**
> **`Novo Pedido (só a Cambos tem)`** — **o rótulo diz isso literalmente, e está \U0001F534 para os cinco perfis.**

⚠ **Funcionalidade feita sob medida e desativada** — vale perguntar se foi descontinuada ou se nunca entrou em uso.

\U0001F534 **Onze funcionalidades estão desligadas para todos os perfis:** `Novo Pedido` · `Tabela Dinâmica` · `Coordenado` · `Estampa` · `Composição de Custo` · `Tag` · `Pack` · `Campo Personalizado` · `Assinaturas` · `Faturas` · `Editar Usuario`.""",
 },

 L: {
  u"02_Estilo-Criacao": u"""\U0001F534 **A Lenny Niemeyer NÃO tem segmentação por área no PLM.** São três perfis, e nenhum é de área:

`LN - Admin` · `LN - Time` · `Fornecedor`

⚠ **`LN - Time` é um perfil único para toda a operação do cliente.** **Nenhuma área desta conta pode ser distinguida por acesso.**

⚠ **As colunas chamadas `Validação` na matriz NÃO são perfis** — são anotação de teste, quase todas vazias. \U0001F534 **Ler a matriz como se fossem cinco perfis seria erro.**

\U0001F534 **`Fornecedor` é acesso de TERCEIRO** — tem \U0001F534 em quase tudo e \U0001F7E2 só em `Notificações`, `Editar Usuario`, `Sair`, `Tarefa homepage` e `Tarefa ficha`.

⚠ **A conta está em `Churn`.** A matriz é de 21/07/2025.""",

  u"06_Compras-Supply-Sourcing": u"""⚠ **Não há perfil de Compras — a conta só tem `LN - Admin`, `LN - Time` e `Fornecedor`.**

\U0001F7E2 **Mas há um perfil de fornecedor externo com acesso ao PLM**, e quatro ações de criação estão \U0001F534 até para Admin e Time:
`> novo fornecedor` · `> nova grade` · `> nova cor` · `> nova mp`

\U0001F534 **E uma linha está INTEIRAMENTE vazia na matriz:** `> excluir variante` — **nenhum valor para nenhum perfil.** ⚠ **Não é \U0001F534 nem \U0001F7E2: é não-preenchido.**""",
 },

 R: {
  u"02_Estilo-Criacao": u"""\U0001F534 **A Recco NÃO tem segmentação por área no PLM** — e vai além: **os perfis nem levam o nome do cliente.**

`Admin` · `Time` · `Fornecedor`

⚠ **É a única das nove contas com matriz assim.** \U0001F534 **Sem prefixo, não dá para saber de que conta um perfil é só pelo nome** — e isso atrapalha qualquer cruzamento entre clientes.

\U0001F7E2 **A estrutura da ficha é quase idêntica à da Lenny Niemeyer**, com duas diferenças: **não há `Informações Complementares`**, e a última aba é **`Integração`** e não `Integração Linx`.

\U0001F534 **Nenhum ERP é nomeado nesta página** — não encontrei menção a Linx, SPI ou outro sistema. ⚠ **Não afirmo que não haja: não consta nesta fonte.**

⚠ **A conta está em `Churn`.** A matriz é de 28/07/2025.""",
 },

 O: {
  u"14_Engenharia": u"""\U0001F7E2 **A Moda Objetiva tem perfil `Objetiva - Engenharia` — e é o SEGUNDO cliente do corpus em que Engenharia existe de verdade**, ao lado da Oficina Reserva.

⚠ **Na Caedu, na Puket e na Luiza Barcelos, Engenharia não é nomeada em fonte nenhuma.** \U0001F534 **A área canônica `14_Engenharia` é, portanto, real em 2 de 49 clientes até agora.**

⚠ **A ficha da conta traz `Composição`, `Modelagem`, `Tabela de Medidas`, `EAN` e `Logística e Fiscal`** — estrutura de produto mais detalhada que a média do corpus.""",

  u"01_Planejamento": u"""**Tem perfil próprio: `Objetiva - Planejamento`.**

\U0001F7E2 **E é o único dos dez perfis com \U0001F7E2 no cadastro `Grupo`** — todos os outros nove não editam. **É sinal de que a taxonomia de produto é governada por Planejamento nesta conta.**""",

  u"06_Compras-Supply-Sourcing": u"""\U0001F534 **A conta separa compras em DOIS perfis:** `Objetiva - Compras` e **`Objetiva - Compras MP`** (matéria-prima).

⚠ **Nenhum outro cliente do corpus faz essa separação.** **Compra de produto e compra de insumo são acessos distintos aqui.**

⚠ **A aba `Integração` da ficha é \U0001F7E2 só para `Admin` e `Compras`** — os outros oito apenas visualizam.""",

  u"02_Estilo-Criacao": u"""**Tem perfil próprio: `Objetiva - Estilo`**, e a conta é a mais segmentada das nove — **dez perfis:**

`Admin` · `Estilo` · `Compras` · `Compras MP` · `Desenvolvimento de Produto` · `Engenharia` · `Estamparia` · `PCP` · `Planejamento` · `Consulta`

\U0001F534 **`Objetiva - Estamparia` não cabe nas 14 áreas canônicas** — mesmo caso de `Vix-Estamparia`. **São dois clientes com Estamparia como área de acesso.**

⚠ **Esta é a matriz mais recente das nove** (29/07/2026) **e a única sem o callout `Documentação tech →`** que as outras oito têm.""",

  u"05_PCP": u"""**Tem perfil próprio: `Objetiva - PCP`.**

\U0001F534 **Dez funcionalidades estão desligadas para TODOS os dez perfis:** `Tabela Dinâmica` · `Coordenado` · `Estampa` · `Composição de Custo` · `Ficha Técnica Base` · `Tag` · `Campo Personalizado` · `Assinaturas` · `Faturas` · `Salvar como Ficha Técnica Base`.

⚠ **`Composição de Custo` e `Ficha Técnica Base` desligados aparecem em quase todas as nove contas** — **é padrão de produto, não escolha de cliente.**""",

  u"03_Desenvolvimento-de-Colecao": u"""**Tem perfil próprio: `Objetiva - Desenvolvimento de Produto`.**

⚠ **A ficha desta conta tem `Custos` como aba própria** — e ao mesmo tempo `Composição de Custo` está \U0001F534 para todos. **Duas coisas diferentes com nomes próximos; não as confundi.**""",
 },

 N: {
  u"07_Logistica-CD": u"""\U0001F7E2 **A NV é o ÚNICO cliente do corpus com perfil de Logística no PLM: `NV - Logística`.**

⚠ **Em Caedu, Puket e Oficina Reserva, logística ou não aparece ou aparece só como destino do fluxo.** \U0001F534 **Aqui ela tem acesso próprio.**

⚠ **A NV é também a única com aba `E-commerce` na ficha de produto**, e com a ação `Enviar para e-commerce`.""",

  u"10_Marketing": u"""\U0001F7E2 **A NV é o ÚNICO cliente do corpus com perfil de Marketing no PLM: `NV - Marketing`.**

⚠ **Na Oficina Reserva, Marketing divide perfil com E-commerce. Na Caedu e na Puket, a função é absorvida por Estilo.** \U0001F534 **Aqui ela tem acesso próprio.**""",

  u"09_Comercial-Vendas": u"""**A NV tem DOIS perfis comerciais: `NV - Atacado` e `NV - Planejamento Comercial`.**

⚠ **`Planejamento Comercial` não é o mesmo que `01_Planejamento`** — a conta tem os dois, e também `NV - Planner` e `NV - Planner 2`. \U0001F534 **São quatro perfis com \"plan\" no nome e funções diferentes.** **Armadilha de leitura, como `Oficina - Planner` × `Oficina - Planejamento`.**""",

  u"04_Qualidade": u"""**Tem perfil próprio: `NV - Qualidade`**, e a ficha tem uma aba de datas dedicada a ela: **`Datas - Qualidade`**.

\U0001F7E2 **A NV é a única conta que separa datas por área na ficha:** `Datas - Estilo` · `Datas - Qualidade` · `Datas - Planner`. **É cronograma embutido no produto, por área responsável.**""",

  u"02_Estilo-Criacao": u"""**Tem perfil próprio: `NV - Estilo`**, com aba de datas própria (`Datas - Estilo`) e uma etapa de conferência nomeada: **`Conferência Cadastro Estilo`**.

\U0001F534 **A NV não usa matriz única: tem TREZE sub-páginas, uma por perfil** — `Geral`, `Master`, `Estilo`, `Qualidade`, `Planner`, `Planner 2`, `Compras`, `Planejamento Comercial`, `PCP`, `Atacado`, `Marketing`, `View`, `Logística`.
⚠ **Só UMA das treze foi lida** (`NV - Geral`). **As outras doze têm URL conhecida e não foram abertas.**

\U0001F534 **E o vocabulário diverge dentro da própria fonte:** a página-mãe define os modos como **`Inclusão`** e **`Restrição`**; a sub-página chama o mesmo modo de **`exclusão`**.""",

  u"05_PCP": u"""**Tem perfil próprio: `NV - PCP`.**

⚠ **A ficha da NV traz `Custos e Preços` como aba única** — nos outros clientes custo e preço aparecem separados ou nem existem.""",

  u"06_Compras-Supply-Sourcing": u"""**Tem perfil próprio: `NV - Compras`**, e a ficha traz `Fornecedores` e `Matéria-Prima e Aviamentos` como abas.

⚠ **No perfil `NV - Geral`, `Fornecedores` vem com a ressalva literal \U0001F7E2 `(não pode excluir)`** — permissão parcial escrita à mão na célula.""",

  u"01_Planejamento": u"""**A conta tem `NV - Planner` e `NV - Planner 2`**, mais a aba **`Datas - Planner`** na ficha.

\U0001F534 **`Planner 2` sugere desdobramento por pessoa ou por linha, e a fonte não explica qual.** ⚠ **Não deduzi.**

⚠ **E há `NV - Planejamento Comercial`, que é outra coisa** — ver `09_Comercial-Vendas`.""",

  u"14_Engenharia": u"""⚠ **Não há perfil de Engenharia na NV.** ⚠ **A ficha traz `Definição da Grade`, `Grade de Tamanhos` e `Tabela de Medidas`** — funções de engenharia de produto distribuídas entre os perfis existentes.

\U0001F534 **A integração da NV tem uma ação que nenhum outro cliente tem: `Audit uMode x Linx`.** ⚠ **É conferência entre os dois sistemas, e está \U0001F534 no perfil `NV - Geral`.**""",
 },
}


def substitui(txt, titulo, novo):
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


def anexa(txt, linha):
    if linha[:46] in txt:
        return txt
    marca = u"### Procedência\n"
    if marca not in txt:
        alvo = u"## Governança"
        if alvo not in txt:
            return txt
        return txt.replace(alvo, u"### Procedência\n| Bloco | Fonte | Data |\n|---|---|---|\n"
                           + linha + u"\n\n" + alvo, 1)
    antes, resto = txt.split(marca, 1)
    linhas = resto.split(u"\n")
    fim = 0
    for i, l in enumerate(linhas):
        if l.strip().startswith(u"|"):
            fim = i + 1
        elif fim:
            break
    if not fim:
        return txt
    return antes + marca + u"\n".join(linhas[:fim] + [linha] + linhas[fim:])


def main():
    escritos, blocos, falhas = 0, 0, []
    for cliente, areas in CONTEUDO.items():
        doc, data = FONTE[cliente]
        linha = (u"| Perfis de acesso, permissões e abas da ficha | Notion — %s | %s |"
                 % (doc, data))
        for area, corpo in sorted(areas.items()):
            caminho = os.path.join(CLI, cliente, area, u"_contexto", u"contexto-area.md")
            if not os.path.exists(caminho):
                falhas.append((cliente, area, u"arquivo nao existe"))
                continue
            txt = io.open(caminho, encoding=u"utf-8").read()
            antes = txt
            txt, ok = substitui(txt, u"O que esta área faz", corpo + rod(cliente))
            if ok:
                blocos += 1
            else:
                falhas.append((cliente, area, u"secao nao encontrada"))
            txt = anexa(txt, linha)
            if txt != antes:
                io.open(caminho, u"w", encoding=u"utf-8").write(txt)
                escritos += 1

    w = sys.stdout.write
    w(u"arquivos escritos : %d\n" % escritos)
    w(u"blocos escritos   : %d\n" % blocos)
    w(u"clientes          : %s\n" % u", ".join(sorted(CONTEUDO)))
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
