# -*- coding: utf-8 -*-
u"""
preenche-areas-caedu.py - preenche as 7 areas da Caedu que estavam vazias.

POR QUE ELAS ESTAVAM VAZIAS. Sao as 7 sem perfil de acesso no PLM. O corpus
tratou isso como "sem fonte" e parou. Era hipotese, nao conclusao: faltava
abrir o `Mapeamento de Contas - Caedu` (04/04/2025), que e a fonte que
alimentou as 7 areas preenchidas.

O QUE A FONTE DIZ, E MUDA O QUADRO. O Mapeamento declara o proprio escopo:

    "Nao incluso: aspectos de contabilidade, faturamento, e dados de pedidos
     sensiveis (planilhas externas)."                          -- secao 2.2

Isso NAO e ausencia de fonte: e EXCLUSAO DECLARADA, com data e autor. E uma
area de fora do escopo por decisao registrada vale muito mais, no cerebro,
que um `[a preencher]` mudo.

O que a fonte cobre sao SEIS processos: Planejamento, Estilo, Importacao,
Modelagem, Produto Nacional e Qualidade. As 7 areas tratadas aqui ou foram
excluidas de proposito, ou tem a funcao ABSORVIDA por um desses seis.

REGRA QUE NAO FOI QUEBRADA. Nada aqui foi inferido: cada bloco escrito cita a
secao do Mapeamento de onde saiu. Onde a fonte nao diz, continua
`[a preencher]` - `12_Design` e `14_Engenharia` seguem quase vazias porque a
fonte realmente nao as nomeia, e inventar conteudo para elas seria pior que
o vazio.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, u"uMode", u"_Clientes", u"Caedu")

FONTE = u"`Mapeamento de Contas - Caedu` (AS IS / TO BE), 04/04/2025"

# area -> {secao: conteudo}. Cada bloco cita a secao da fonte.
CONTEUDO = {
 u"11_Financeiro": {
  u"O que esta área faz": u"""\U0001F534 **A área foi EXPLICITAMENTE excluída do escopo do mapeamento de conta** — não é lacuna de varredura, é decisão registrada.

> *"**Não incluso**: aspectos de contabilidade, faturamento, e dados de pedidos sensíveis (planilhas externas)."*
> — %s, § 2.2 *Escopo do Mapeamento*

⚠ **O único tema financeiro que aparece na plataforma é cálculo de margem**, e aparece como lacuna de relatório:

> *"Cálculo de margens e tags de licenciamento — **sem dashboard consolidado**."*
> — %s, § 4.3 *Indicadores e Relatórios*""" % (FONTE, FONTE),

  u"O que não fazem": u"""- **Não usam o uFlow para contabilidade nem para faturamento** — excluído do escopo por decisão registrada (§ 2.2 do mapeamento).
- **Não mantêm dados de pedido na plataforma** — vivem em planilhas externas.""",

  u"Produto conectado": u"""**Nenhum módulo contratado atende esta área.** Os quatro módulos da Caedu — Gestão de Coleção, Integração, Relatórios e Fornecedores — cobrem desenvolvimento de produto, não financeiro.

⚠ **`Relatórios` toca o tema de margem**, mas o próprio mapeamento registra que não há dashboard consolidado.""",
 },

 u"09_Comercial-Vendas": {
  u"O que esta área faz": u"""\U0001F534 **O dado comercial da Caedu vive FORA do uMode, por decisão, e isso está registrado como dor.**

> *"**Sensibilidade de Dados** (parte de negociação e pedido) está fora da uMode."* — § 4.4, dor 2
> *"Parte da negociação de pedidos é feita em **planilhas sensíveis**."* — § 4.2.3

⚠ **O que chega à plataforma é a emissão do pedido, não a negociação:**

> *"Integração com **Linx** para geração de pedidos e controle de estoque."* — § 2.1

**Fonte de tudo acima:** %s.""" % FONTE,

  u"Com quem se relaciona (interno e externo)": u"""- **`03_Desenvolvimento-de-Colecao`** — recebe o produto liberado; a validação *"Liberado para emissão"* é o ponto de passagem (§ 4.2.5).
- **Linx (ERP)** — é por onde o pedido é gerado e o estoque controlado (§ 2.1).
- ⚠ **Planilhas externas** — onde a negociação acontece hoje. **Não é sistema mapeado.**""",

  u"O que não fazem": u"""- **Não negociam dentro do uMode.** A negociação e o dado sensível de pedido estão em planilhas externas — e há ação aberta no roadmap para reavaliar isso (§ 5.2, *Segurança de Dados — rever permissão de pedidos*, responsável **Time Caedu + uMode**, prazo previsto de **6 semanas**, contado de 04/04/2025).""",

  u"Produto conectado": u"""**`Integração`** (uFlow) — módulo contratado pela Caedu. É o que liga a liberação do produto à emissão de pedido no **Linx**.

⚠ **Não há módulo que cubra negociação comercial** — e isso é escopo declarado, não falha.""",
 },

 u"07_Logistica-CD": {
  u"O que esta área faz": u"""⚠ **A logística da Caedu não está na plataforma. Ela aparece apenas como o DESTINO do fluxo**, depois da última validação de Qualidade:

> *"Controle de amostras de produção, reprovando ou aprovando (lacrando) **antes do envio a lojas**."*
> — %s, § 4.2.6 *Qualidade*

⚠ **Dois vestígios a mais, e só dois:** o campo **`Localização de loja`** na ficha de produto (§ 4.2.2) e o **planejamento de loja e cluster** previsto no Macroplan, que o próprio mapeamento classifica como **pouco explorado** (§ 4.4, dor 4).

\U0001F534 **Nenhuma fonte descreve operação de CD, expedição ou armazenagem da Caedu.**""" % FONTE,

  u"Produto conectado": u"""**Nenhum módulo contratado atende esta área.**

⚠ **`Gestão de Coleção` faz fronteira com ela** no campo `Localização de loja` e no Macroplan — **que está registrado como subutilizado.**""",
 },

 u"05_PCP": {
  u"O que esta área faz": u"""⚠ **Não existe área de PCP mapeada na Caedu.** As funções que um PCP teria estão **distribuídas entre Modelagem, Produto Nacional e Qualidade** — e o que falta delas está registrado como **lacuna de relatório**, não como área ausente:

> *"Há alto volume de produtos/variantes, com necessidade de **acompanhamento de cronogramas**."* — § 1
> *"Falta de relatórios unificados que mostrem **por departamento se algo está pendente**."* — § 4.2.5
> *"Lacunas: relatórios automáticos de repilotagem, **tempo entre etapas**."* — § 4.3

**Fonte:** %s.""" % FONTE,

  u"Com quem se relaciona (interno e externo)": u"""- **`13_Modelagem`** — onde ficam piloto, fitting e repilotagem (§ 4.2.4).
- **`04_Qualidade`** — amostras de produção e liberação final (§ 4.2.6).
- **`03_Desenvolvimento-de-Colecao`** — liberação para emissão de pedido (§ 4.2.5).""",

  u"Produto conectado": u"""**`Relatórios`** (uFlow) — módulo contratado. É onde o acompanhamento de cronograma e tempo entre etapas **deveria** aparecer.

\U0001F534 **E é exatamente o que o mapeamento aponta como lacuna** (§ 4.3): não há relatório de tempo entre etapas nem de repilotagem.""",
 },

 u"10_Marketing": {
  u"O que esta área faz": u"""⚠ **Não existe área de Marketing mapeada na Caedu. O conteúdo que seria dela — e-commerce, SEO e visual merchandising — é produzido por `02_Estilo-Criacao`:**

> *"Estilo aprova produtos, libera ficha para e-commerce (campos de **SEO**, licenciamento, cor e variação)... atributos de **V.M.**"* — § 4.2.2
> *"Diversos campos (licenciamento, atributos e **visual merchandising**) são críticos para e-commerce e planejamento de loja."* — § 1

\U0001F534 **E a dor registrada é de subuso, não de ausência de área:**

> *"Falta de maior exploração de **visual merchandising** e macros de cor."* — § 4.2.2, Dores

**Fonte:** %s.""" % FONTE,

  u"Com quem se relaciona (interno e externo)": u"""- **`02_Estilo-Criacao`** — é quem preenche SEO, título, imagem e atributos de VM na ficha (§ 4.2.2).
- **`08_Ecommerce-Cadastro`** — consome a ficha liberada.""",

  u"Produto conectado": u"""**`Gestão de Coleção`** (uFlow) — os campos de e-commerce e VM vivem na ficha de produto.

⚠ **A ação de roadmap é de adoção, não de construção:** *"ampliar uso de campos de VM e e-commerce"* (§ 5.1). **Os campos já existem.**""",
 },

 u"12_Design": {
  u"O que esta área faz": u"""\U0001F534 **Nenhuma fonte varrida nomeia uma área de Design na Caedu.** Não é o mesmo que dizer que ela não existe — **é dizer que não foi encontrada em nenhuma das quatro fontes abaixo.**

⚠ **O mapeamento de conta cobre seis processos e Design não é um deles:** Planejamento, Estilo, Importação, Modelagem, Produto Nacional e Qualidade (§ 2.2).

⚠ **A criação de produto está sob `02_Estilo-Criacao`**, que é quem aprova produto e preenche ficha técnica (§ 4.2.2). \U0001F534 **Não afirmo que Design seja Estilo com outro nome** — é hipótese a confirmar com o atendimento.""",
 },

 u"14_Engenharia": {
  u"O que esta área faz": u"""\U0001F534 **Nenhuma fonte varrida nomeia uma área de Engenharia na Caedu.** Como acima: **não encontrada**, e não *inexistente*.

⚠ **As funções típicas de engenharia de produto aparecem, mas sob outras áreas:**
- **ficha técnica** → `02_Estilo-Criacao` (§ 4.2.2);
- **tabela de medidas e checklist de aprovação** → `13_Modelagem` (§ 4.2.4);
- **tabela de medidas de importados** → o processo de Importação (§ 4.2.3).

\U0001F534 **`Importação` e `Produto Nacional` são etapas do processo da Caedu que NÃO cabem nas 14 áreas canônicas** — mesmo padrão de `Atelier`, `Estamparia` e `Oficina` em outros clientes. **Ver `_pendencias-gerais.md`.**""",
 },
}

# a linha da tabela `Fontes varridas` que muda: agora e exclusao declarada
LINHA_VELHA = (u"| Notion — `Mapeamento de Contas - Caedu` | "
               u"área não consta no escopo mapeado |")
LINHA_NOVA = {
 u"11_Financeiro": u"| Notion — `Mapeamento de Contas - Caedu` | \U0001F534 **excluída do escopo POR DECISÃO** — § 2.2 diz literalmente *\"não incluso: contabilidade, faturamento\"* |",
 u"09_Comercial-Vendas": u"| Notion — `Mapeamento de Contas - Caedu` | \U0001F534 **excluída do escopo POR DECISÃO** (§ 2.2, *dados de pedidos sensíveis*) — **mas há dor e ação registradas** (§ 4.4 e § 5.2) |",
 u"07_Logistica-CD": u"| Notion — `Mapeamento de Contas - Caedu` | ⚠ aparece **só como destino do fluxo** (*\"antes do envio a lojas\"*, § 4.2.6) |",
 u"05_PCP": u"| Notion — `Mapeamento de Contas - Caedu` | ⚠ **função distribuída** entre Modelagem, Produto Nacional e Qualidade; o que falta é **relatório** (§ 4.3) |",
 u"10_Marketing": u"| Notion — `Mapeamento de Contas - Caedu` | ⚠ **função absorvida por `02_Estilo-Criacao`** (SEO, VM, e-commerce — § 4.2.2) |",
 u"12_Design": u"| Notion — `Mapeamento de Contas - Caedu` | \U0001F534 **não nomeada** — os 6 processos mapeados não incluem Design (§ 2.2) |",
 u"14_Engenharia": u"| Notion — `Mapeamento de Contas - Caedu` | \U0001F534 **não nomeada** — funções aparecem sob Estilo, Modelagem e Importação |",
}


# As 7 areas nunca tiveram tabela de `Procedencia` - so a de `Fontes varridas`,
# que registra o que NAO se achou. Agora que tem conteudo, precisam declarar de
# onde ele veio: e essa tabela que o `gera-fatos.py` le para dar fonte por
# chave. Sem ela, todo fato da area sai `[sem fonte]` mesmo tendo origem clara.
PROCEDENCIA = u"""### Procedência deste documento
| Bloco | Fonte | Data |
|---|---|---|
| O que a área faz, relações, o que não fazem | Notion — `Mapeamento de Contas - Caedu` (AS IS / TO BE) | 04/04/2025 |
| Módulos e produto conectado | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |
| Ausência de perfil de acesso e de pessoas | Notion — página `Caedu`, tabela de usuários do PLM | varrido 21/09/2026 |

⚠ **O mapeamento de conta é de abr/2025 — tem 17 meses.** Revalidar com a dupla de atendimento
antes de usar como diagnóstico atual.

"""


def substitui_secao(txt, titulo, novo):
    u"""Troca o corpo de uma secao, preservando o resto do arquivo."""
    marca = u"\n" + (u"### " if titulo in (u"O que não fazem",) else u"## ") + titulo + u"\n"
    if marca not in txt:
        marca = u"\n### " + titulo + u"\n"
        if marca not in txt:
            return txt, False
    antes, resto = txt.split(marca, 1)
    # o corpo vai ate o proximo heading de qualquer nivel
    corte = len(resto)
    for h in (u"\n## ", u"\n### "):
        i = resto.find(h)
        if i != -1:
            corte = min(corte, i)
    return antes + marca + u"\n" + novo + u"\n" + resto[corte:], True


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
        if LINHA_VELHA in txt and area in LINHA_NOVA:
            txt = txt.replace(LINHA_VELHA, LINHA_NOVA[area], 1)
        marca = u"### Fontes varridas"
        if u"### Procedência deste documento" not in txt and marca in txt:
            txt = txt.replace(marca, PROCEDENCIA + marca, 1)
        if txt != antes:
            io.open(caminho, u"w", encoding=u"utf-8").write(txt)
            escritos += 1

    w = sys.stdout.write
    w(u"areas preenchidas : %d de 7\n" % escritos)
    w(u"blocos escritos   : %d\n" % blocos)
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
