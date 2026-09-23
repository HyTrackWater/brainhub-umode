# -*- coding: utf-8 -*-
u"""
preenche-areas-oficina.py - preenche as areas da Oficina Reserva a partir da
matriz de perfis e permissionamentos, que estava APONTADA e nao lida.

POR QUE ESTA FONTE. Catorze `contexto-area.md` da Oficina Reserva traziam uma
secao `### Proxima fonte a varrer para esta area` apontando literalmente a
pagina `Perfil de Usuario e Permissionamentos OFICINA`. **Estava escrito o que
fazer e ninguem tinha feito.**

O QUE ELA MUDA. O `institucional.md` da conta declarava a propria fonte como
fraca: "esta conta nao tem lista de times, nem tabela de PLM varrida, nem
pesquisa. O que existe sao funcoes citadas dentro das dores. Fonte fraca, e
declarada como tal." Agora ha fonte forte: OITO perfis nomeados, com matriz
de permissao campo a campo, lida em 17/03/2026.

DOIS ACHADOS QUE O CORPUS NAO TINHA:
  1. `Oficina - Qualita` e perfil de EMPRESA EXTERNA - a Qualita audita a
     qualidade da conta, e tem perfil proprio no PLM do cliente.
  2. `Oficina - Ecommerce Marketing` e UM perfil para DUAS areas canonicas.
     E o mesmo padrao de alias que nao cabe na grade, agora em permissao.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, u"uMode", u"_Clientes", u"Oficina Reserva")

F = u"`Perfil de Usuário e Permissionamentos OFICINA`, lida em 17/03/2026"
AVISO = u"\n\n⚠ **Fonte:** Notion — %s, na página da conta em `Databases / Mapa de Clientes`." % F

# 8 funcionalidades estao 🔴 para TODOS os perfis - e decisao de conta, nao
# de area, entao entra em toda ficha como contexto comum.
DESLIGADO = (u"\n\n\U0001F534 **Oito funcionalidades estão desligadas para TODOS os oito perfis:** "
             u"`Lotes` · `Tabela Dinâmica` · `Coordenado` · `Estampa` · `Composição de Custo` · "
             u"`Tag` · `Tipo de Lote` · `Pack`. **É decisão de conta, não de área.**")

CONTEUDO = {
 u"02_Estilo-Criacao": {
  u"O que esta área faz": u"""**Tem perfil próprio no PLM: `Oficina - Estilo`**, e é um dos três perfis de maior alcance da conta.

\U0001F7E2 **É um dos três perfis que a regra de permissão trata como privilegiados**, e a regra está escrita na própria fonte:
> `!current_context.current_policy.name.in?(['Oficina - Master', 'Oficina - Planner', 'Oficina - Estilo'])`

⚠ **As sete abas de Estilo na ficha de produto são:** `Informações Gerais` · `Ficha Técnica` · `Variantes` · `Materiais (Facção)` · `Materiais P.A.` · `Imagens` · `Arquivos`.

\U0001F534 **E há uma exceção dura:** `Estilo | Ficha Técnica` é **\U0001F534 para todos os perfis menos o Master** — inclusive para o próprio Estilo.""" + AVISO + DESLIGADO,
 },

 u"01_Planejamento": {
  u"O que esta área faz": u"""**Tem perfil próprio: `Oficina - Planejamento`**, e é o único perfil não-privilegiado com **edição** na aba `Planejamento` da ficha.

⚠ **Também edita, ao contrário dos demais perfis operacionais:** `Marca`, `Coleção`, `Tema`, `Associar Workflow`, `Todas as Entradas` e `Meus Produtos`.

\U0001F534 **Há um perfil vizinho e distinto — `Oficina - Planner`** — que é privilegiado e não se confunde com este. **São dois perfis diferentes com nomes quase iguais.**""" + AVISO,
 },

 u"06_Compras-Supply-Sourcing": {
  u"O que esta área faz": u"""**Tem perfil próprio: `Oficina - Compras`.**

\U0001F534 **E ele está marcado para desaparecer:**
> *"Provavelmente no **novo formato da Oficina não teremos mais o Perfil de compras**. Por hora, seguimos com esse perfil ativo."*

⚠ **Hoje o perfil vê o custo:** `Relatório de Pré Custo` está \U0001F7E1 para Compras, e \U0001F534 para Atacado, Qualitá e Ecommerce.""" + AVISO,
 },

 u"04_Qualidade": {
  u"O que esta área faz": u"""\U0001F534 **A auditoria de qualidade é feita por EMPRESA EXTERNA, e ela tem perfil próprio no PLM do cliente:** `Oficina - Qualitá`.

⚠ **Isso confirma, com fonte forte, o que o `institucional.md` registrava como indício fraco** (*"auditoria de qualidade — feita pela Qualitá, empresa externa"*, tirado de uma dor).

\U0001F534 **É um perfil de terceiro dentro da conta do cliente** — e o acesso dele é restrito: `Histórico de Movimentações`, `Integração Linx`, `Engenharia | Aprovações` e `Relatório de Pré Custo` estão **\U0001F534** para ele.""" + AVISO,
 },

 u"09_Comercial-Vendas": {
  u"O que esta área faz": u"""**Tem perfil próprio: `Oficina - Atacado`** — o canal atacado é o recorte comercial que a conta modela.

\U0001F534 **É o perfil mais restrito dos oito.** Estão **\U0001F534** para ele: `Mapa > Exibição`, `Atualização de Produtos (SAP)`, `Novos Produtos ZZNet (SAP)`, `Ficha Técnica Base`, `Mover`, `Duplicar`, `Excluir Produto`, `Histórico`, `Relatório de Pré Custo`, `Histórico de Movimentações`, `Integração Linx` e `Engenharia | Aprovações`.

⚠ **Na prática, o Atacado consulta e não constrói produto.**""" + AVISO,
 },

 u"08_Ecommerce-Cadastro": {
  u"O que esta área faz": u"""\U0001F534 **E-commerce e Marketing compartilham UM único perfil: `Oficina - Ecommerce Marketing`.**

⚠ **É um perfil para DUAS áreas canônicas** — `08_Ecommerce-Cadastro` e `10_Marketing`. **Não dá para separar quem fez o quê pelo perfil de acesso**, e isso limita qualquer atribuição por área nesta conta.

⚠ **O `institucional.md` já registrava, de fonte fraca, que *"há apenas uma pessoa dedicada ao cadastro"*.** \U0001F7E2 **A matriz de perfis é coerente com isso.**""" + AVISO,
 },

 u"10_Marketing": {
  u"O que esta área faz": u"""\U0001F534 **Não há perfil de Marketing próprio: ele divide o perfil `Oficina - Ecommerce Marketing` com `08_Ecommerce-Cadastro`.**

⚠ **Mesmo padrão de alias que não cabe na grade das 14 áreas** — agora aparecendo em **permissão**, não em nome de time. **Ver `_pendencias-gerais.md`.**

\U0001F534 **O perfil é de consulta:** `Homepage` e `Desenvolvimento` estão \U0001F7E1, e `Mapa > Exibição`, `Ficha Técnica Base`, `Mover`, `Duplicar` e `Excluir Produto` estão \U0001F534.""" + AVISO,
 },

 u"14_Engenharia": {
  u"O que esta área faz": u"""\U0001F7E2 **Aqui Engenharia NÃO é hipótese: é um bloco da ficha de produto, com três abas próprias.**

| Aba | Quem edita |
|---|---|
| `Engenharia \\| Tamanhos e Medidas` | Master, Planner, Estilo |
| `Engenharia \\| Aprovações` | Master, Planner, Estilo — **\U0001F534 Atacado e Ecommerce não veem** |
| `Engenharia \\| Engenharia` | Master, Planner, Estilo |

⚠ **Não existe perfil de acesso chamado Engenharia.** O bloco existe na ficha e é operado pelos três perfis privilegiados.

\U0001F534 **Contraste que vale registrar:** na Caedu e na Puket, Engenharia **não é nomeada em fonte nenhuma**. Aqui ela é estrutura de produto.""" + AVISO,
 },

 u"13_Modelagem": {
  u"O que esta área faz": u"""⚠ **Não há perfil de Modelagem na Oficina Reserva.** A função vive na aba **`Engenharia | Tamanhos e Medidas`** da ficha, editada por Master, Planner e Estilo.

⚠ **O cadastro `Tabela de Medidas` está \U0001F7E2 só para Master e Planner**; os outros seis perfis apenas visualizam.""" + AVISO,
 },

 u"03_Desenvolvimento-de-Colecao": {
  u"O que esta área faz": u"""**É o bloco `Desenvolvimento` do PLM**, e a conta o divide em cinco entradas: `Todas as Entradas` · `Mapa de Coleção` · `Meus Produtos` · `Lotes` · e as duas interfaces SAP.

\U0001F534 **A conta integra com SAP por DUAS interfaces nomeadas:**
- **`Novos Produtos ZZNet` — SAP Interface 1**
- **`Atualização de Produtos` — SAP Interface 3**

⚠ **E também há `Integração Linx` como aba da ficha** — restrita a Master, Planner e Estilo. **São dois ERPs citados na mesma conta.**

\U0001F534 **`Lotes` está desligado para todos os oito perfis.**""" + AVISO,
 },
}

# A matriz e fonte FORTE e substitui o mapeamento alias que o proprio corpus
# marcava como fraco. Nao apaga o anterior: acrescenta e diz qual prevalece.
BLOCO_ALIAS = u"""
### \U0001F7E2 Perfis de acesso reais — fonte forte, lida em 17/03/2026

> \U0001F534 **Esta tabela PREVALECE sobre a de funções-citadas-em-dores acima**, que a própria
> se declara *"fonte fraca"*. **Aquela fica como histórico do que se sabia antes.**
> **Fonte:** Notion — `Perfil de Usuário e Permissionamentos OFICINA`.

| Perfil no PLM | → Área canônica |
|---|---|
| `Oficina - Master` | **transversal** — único com `Usuários da Conta` e `Editar Usuário` |
| `Oficina - Planner` | **transversal** — privilegiado, **não confundir com `Oficina - Planejamento`** |
| `Oficina - Estilo` | `02_Estilo-Criacao` |
| `Oficina - Planejamento` | `01_Planejamento` |
| `Oficina - Compras` | `06_Compras-Supply-Sourcing` — \U0001F534 **marcado para ser extinto** |
| `Oficina - Atacado` | `09_Comercial-Vendas` — o mais restrito dos oito |
| `Oficina - Qualitá` | `04_Qualidade` — \U0001F534 **perfil de EMPRESA EXTERNA** |
| `Oficina - Ecommerce Marketing` | \U0001F534 **`08_Ecommerce-Cadastro` E `10_Marketing`** — um perfil, duas áreas |

\U0001F534 **Sete das 14 áreas canônicas não têm perfil:** PCP, Logística, Financeiro, Design,
Modelagem, Engenharia e Desenvolvimento de Coleção. ⚠ **Mas Engenharia existe como bloco da
ficha de produto** — **perfil e área não são a mesma coisa nesta conta.**

"""


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


NOTA_VELHA = u"### \U0001F534 Próxima fonte a varrer para esta área"
NOTA_NOVA = u"### \U0001F7E2 Fonte varrida em 23/09/2026"

PROC = u"""| Perfis de acesso, permissões e abas da ficha | Notion — `Perfil de Usuário e Permissionamentos OFICINA` | 17/03/2026 |
"""


def anexa_procedencia(txt):
    if u"Permissionamentos OFICINA`" in txt.split(u"### Procedência", 1)[-1][:700]:
        return txt
    marca = u"### Procedência\n"
    if marca not in txt:
        alvo = u"## Governança"
        if alvo not in txt:
            return txt
        nova = u"### Procedência\n| Bloco | Fonte | Data |\n|---|---|---|\n" + PROC + u"\n"
        return txt.replace(alvo, nova + alvo, 1)
    antes, resto = txt.split(marca, 1)
    linhas = resto.split(u"\n")
    fim = 0
    for i, l in enumerate(linhas):
        if l.strip().startswith(u"|"):
            fim = i + 1
        elif fim:
            break
    return antes + marca + u"\n".join(linhas[:fim] + [PROC.rstrip(u"\n")] + linhas[fim:])


def main():
    escritos, blocos, falhas = 0, 0, []
    for area, secoes in sorted(CONTEUDO.items()):
        caminho = os.path.join(BASE, area, u"_contexto", u"contexto-area.md")
        if not os.path.exists(caminho):
            falhas.append((area, u"arquivo nao existe"))
            continue
        txt = io.open(caminho, encoding=u"utf-8").read()
        antes = txt
        for titulo, corpo in secoes.items():
            txt, ok = substitui_secao(txt, titulo, corpo)
            if ok:
                blocos += 1
            else:
                falhas.append((area, u"secao nao encontrada: " + titulo))
        txt = anexa_procedencia(txt)
        txt = txt.replace(NOTA_VELHA, NOTA_NOVA, 1)
        if txt != antes:
            io.open(caminho, u"w", encoding=u"utf-8").write(txt)
            escritos += 1

    # a tabela de perfis vai para o institucional, que e o dono dos aliases
    inst = os.path.join(BASE, u"00_Institucional", u"_contexto", u"institucional.md")
    alias_ok = False
    if os.path.exists(inst):
        t = io.open(inst, encoding=u"utf-8").read()
        if u"Perfis de acesso reais" not in t and u"## Sistemas e fontes de verdade" in t:
            t = t.replace(u"## Sistemas e fontes de verdade",
                          BLOCO_ALIAS + u"## Sistemas e fontes de verdade", 1)
            io.open(inst, u"w", encoding=u"utf-8").write(t)
            alias_ok = True

    w = sys.stdout.write
    w(u"areas preenchidas   : %d de 10 com material\n" % escritos)
    w(u"blocos escritos     : %d\n" % blocos)
    w(u"tabela de perfis no institucional: %s\n" % (u"sim" if alias_ok else u"ja estava"))
    if falhas:
        w(u"\U0001F534 falhas:\n")
        for a, m in falhas:
            w(u"   - %s: %s\n" % (a, m))
        return 1
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
