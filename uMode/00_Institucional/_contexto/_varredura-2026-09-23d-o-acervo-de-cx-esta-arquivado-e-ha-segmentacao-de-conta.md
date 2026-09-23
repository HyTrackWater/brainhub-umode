---
aliases:
  - "Varredura 23 set 2026 (d) — o acervo de CX está em `Arquivo`, e existe segmentação de conta"
tags:
  - tipo/registro
  - casa
---
# Varredura 23 set 2026 (d) — o acervo de CX está em `Arquivo`, e existe segmentação de conta

> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**
>
> Veio de mapear o terceiro acervo por cliente, que eu tinha achado horas antes. **Li o índice
> e consultei a base inteira por SQL: 30 documentos.** **Abri uma página.**

## 0 · 🔺 Correção de um caminho que eu escrevi hoje mesmo

No registro `(b)` § 10.2 e na lista de fontes eu escrevi:

> *"`Operação de Clientes / Área de CX / Documentação CX / Mapeamento de Contas`"*

> 🔴 **Faltou uma pasta. O caminho real é
> `Operação de Clientes / **Arquivo** / Área de CX / Documentação CX`.** `[C]`

**Por que importa, e não é detalhe:** ⚠ **o acervo está ARQUIVADO.** Eu o registrei como
"terceiro acervo de documentação por cliente" no mesmo peso dos outros dois. **Não é o mesmo
peso — é material que a própria uMode moveu para `Arquivo`.**

**Como eu errei:** li o caminho do campo `path` da resposta, que vem resumido, **em vez do
`ancestor-path`, que vem completo.** ⚠ **Duas representações do mesmo caminho na mesma
resposta, e eu peguei a curta.**

## 1 · A base `Documentação CX` — 30 documentos `[C]`

`collection://3a26629f-368a-4a19-a9ad-0559c0c7d7a7`, consultada por SQL.

| Campo | Valores |
|---|---|
| `Plataforma` | **Notion · Excel · Looker · PPT** |
| `Área` | Template · Atendimento · Clientes · Estratégico · Dashboards · Pesquisas · Treinamento Time |
| `Status` | Em Construção · Em Validação · Validado · Inativo |
| `Status 1` | Not started · In progress · Done |

### 1.1 · 🔴 Dois campos de status na mesma base, e eles discordam

| Documento | `Status` | `Status 1` |
|---|---|---|
| `Health Score` | **Em Construção** | **Not started** |
| `Pesquisa Satisfação Agosto/24` | **Validado** | **In progress** |
| `[CX] Plano do Sucesso do Cliente` | Validado | Done |

⚠ **É o mesmo defeito do `Status` × `Etapa` da base `Mapa de Clientes`.** 🔴 **Segundo caso —
vira hipótese: a uMode cria um segundo campo de status em vez de arrumar o primeiro.**

### 1.2 · ⚠ 11 dos 30 documentos têm `Nome Documento` VAZIO

**Mais de um terço da base não tem título.** Mesmo padrão da base `Usuários` da Lenny Niemeyer:
**estrutura criada, conteúdo parcial.**

## 2 · 🔴 Existe segmentação de conta, e o corpus não tem

| Documento | O que revela |
|---|---|
| **`[SaaS] Desenvolvimento (uFlow)`** | 🔴 há um segmento **SaaS** |
| **`[CX] Enterprise`** | 🔴 há um segmento **Enterprise** |
| `Vídeo Mapa de Produtos - Planilha IA - **SMB**` | 🔴 há um segmento **SMB** |

> 🔴 **Três rótulos de segmento — `SaaS`, `Enterprise`, `SMB` — e nenhuma ficha de cliente do
> corpus carrega segmento.**

🟢 **E isso dá sentido à fonte `Segmentação Grupos`**, que eu listava como não varrida sem
saber o que era. ⚠ **Não afirmo que são a mesma taxonomia** — afirmo que agora há duas pistas
apontando para o mesmo lugar.

## 3 · 🆕 O que mais a base nomeia

### 3.1 · Dashboards — e uma quarta ferramenta de BI

| Documento | Plataforma | Estado |
|---|---|---|
| 🔴 **`Health Score`** | **Looker** | **Em Construção desde fev/2025** |
| `Dash de Controle dos Clientes` | **Looker** | Validado |

> 🆕 **`Looker`.** Com `BigQuery`, `Blazzer` e `uDash`, são **quatro** superfícies de
> relatório. ⚠ **O corpus não tem nenhuma delas como ferramenta.**

🔴 **`Health Score` é exatamente a métrica de saúde de conta que falta no corpus** — e está
`Em Construção` há mais de um ano e meio.

### 3.2 · Templates que existem

| Documento | Estado |
|---|---|
| `Status Report para o Cliente [Template]` | In progress |
| `Template Planilha Plano Sucesso Cliente (KRs)` | **Validado** |
| `Cronograma Padrão de Implantação` | Em Construção |
| 🆕 **`Planilha de Cardápio de Dores e KRs`** | Em Construção |

> 🆕 **"Cardápio de Dores"** é vocabulário forte, e é **exatamente o que a varredura vem
> catalogando cliente a cliente.** ⚠ **Não abri.**

### 3.3 · Pesquisa de satisfação — existe estrutura e existe uma rodada

| Documento | Estado |
|---|---|
| `[CX] Estrutura de Pesquisa de Satisfação **Trimestral**` | **Validado** |
| `Pesquisa Satisfação **Agosto/24**` | Validado · In progress |

⚠ **Eu listava "pesquisas de CSat" como fonte não varrida, sem saber que havia estrutura
definida.** 🔴 **Trimestral, e a última nomeada é de ago/2024.**

### 3.4 · E dois documentos que explicam coisas que eu já tinha visto

| Documento | O que explica |
|---|---|
| **`Migração e Padronização de Ferramentas de Trabalho`** · `Done`, abr/2025 | 🟢 **provavelmente é a decisão que descontinuou o Kanbanize e o Linear.** ⚠ **Não abri — é hipótese** |
| **`Plano de Gestão de Risco - Legado`** · `Versão 1`, `Done` | ⚠ **"Legado" é o uFlow.** **Há um plano de risco escrito, e o corpus não o cita** |

🆕 **`Plano de Gestão de Risco - Legado` é o único documento da base com DOIS owners** e o
único com `Versão` preenchida.

## 4 · 🔺 Mais um documento que nasceu de IA

A página `Mapeamento de Contas` **não é um mapeamento — é a proposta de estrutura, escrita por
uma IA e colada inteira**, incluindo o fecho: *"Espero que esses dois exemplos de estrutura
atendam o que vocês precisam."* `[C]`

E a sub-página se chama **`Mapeamento da Conta da Puket seguindo análise do Chat GPT`.**

> 🔴 **Segundo método IA→documento no corpus**, com o playbook da Cambos. ⚠ **A diferença: o
> da Cambos virou `Documentação Homologada`; este virou `Arquivo`.**

### 4.1 · 🟢 E a estrutura proposta é quase o BrainHub

**AS IS → problemas → TO BE → roadmap → governança**, com a regra explícita:

> *"Sempre **salve** um 'arquivo-mestre' sem menções específicas ao cliente. Assim, basta
> duplicar e preencher com dados do cliente X ou Y."*

⚠ **A uMode já tentou padronizar documentação por cliente com template, em abril de 2025.**
🔴 **O resultado está numa pasta `Arquivo`, e a razão disso não está escrita em lugar nenhum
que eu tenha lido.**

## 5 · Dado concreto que ficou, mesmo sendo exemplo

Dentro do modelo, o exemplo usa a Puket com números reais: `[C]`

> *"Subida do Esqueleto via planilha — Produto usa **37 campos**, importados em lote; se faltar
> algum campo obrigatório, dá erro."*
> *"Validação 'Composição' = se Origem = '**Meias**', deve ser preenchido."*

⚠ **`Meias` é categoria de produto da Puket**, e a regra de validação condicional é real.
🔴 **Mas está dentro de um exemplo de template.** **Registro como pista, não como espec** —
foi exatamente assim que eu errei com o `entity_id = 3344`.

## 6 · As sub-páginas, não abertas

| Sub-página |
|---|
| `Mapeamento da Conta - Puket` |
| `Mapeamento de Contas - Caedu` |
| 🔴 **`Análise das Similaridades e Diferenças entre contas: Puket e Caedu`** |
| 🆕 `Devolutivas para Sandro` |
| `Indicadores e Rotinas de Acompanhamento` |

> 🔴 **A terceira é rara: comparação explícita entre duas contas.** É o tipo de leitura que a
> varredura vem fazendo à mão, e alguém já fez em 2025.

🆕 **`Sandro`** — ⚠ **nome novo.** **Não crio ficha: título de página não é fonte suficiente** —
mesma régua da `Flávia` e da `Laura`.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §0, §4, §5, §6 | Notion — `Mapeamento de Contas` (`1bdb1d38…`), **aberta por inteiro**; caminho conferido no `ancestor-path` | **23 set 2026** |
| §1–§3 | Notion — base `Documentação CX` (`collection://3a26629f-368a-4a19-a9ad-0559c0c7d7a7`), **30 linhas lidas por SQL** | **23 set 2026** |
