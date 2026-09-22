# Varredura 22 set 2026 (h) — a página do cliente tem `cargo` e `área`, e eu tinha dito que não

> Varredura cliente a cliente, **abrindo a página de cada um**, como o registro (f) determinou.
> Começou por Osklen e NK STORE.
>
> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**

## 0 · Declaração de completude — e duas correções de erro meu, antes de tudo

### 🔺 CORREÇÃO 1 — eu apaguei uma pessoa real

O `gera-fichas-pessoa.py` tinha **`hermes` na lista `NAO_PESSOA`**. Eu o filtrei **presumindo que
fosse o agente `Hermes` da uMode**.

> 🔴 **É `Hermes Gonçalves Santiago Junior`, Gerente de TI da NK STORE** — e **abriu 5 demandas.**

**Presumir que um nome conhecido num contexto é o mesmo nome noutro contexto é exatamente o que a
regra de ouro proíbe.** Homônimo entre agente e pessoa é problema de desambiguação, e desambiguação
se faz **com fonte** — nunca com um filtro cego por string. **Corrigido: `hermes` saiu da lista**,
e o motivo ficou escrito no script para não voltar.

### 🔺 CORREÇÃO 2 — `cargo` e `área` TÊM fonte

Eu escrevi, nos itens 285 e 315 e em 128 fichas: *"nenhuma fonte varrida traz cargo de pessoa de
cliente"*.

> 🔴 **Errado. A página de cada cliente tem um toggle `Pessoas` com nome completo, cargo, área,
> e-mail e telefone.** Eu não tinha aberto a página.

**É a quarta variação do mesmo erro** — *"não encontrei em X" virou "não existe"*. As três
anteriores estão no `STATE.md`. **Agora a raiz tem nome: eu media pelas BASES, e a página do
cliente não é base.**

### O que esta varredura ainda NÃO alcançou

| # | Lacuna | Consequência |
|---|---|---|
| 1 | **Abri 2 das 49 páginas de cliente** | o `cargo` só foi preenchido onde eu li |
| 2 | 🔴 **A página da Osklen tem o MESMO toggle, e está vazia** | o template existe; **preencher é do atendimento, não meu** |
| 3 | ⚠ **Não mapeei a área da fonte para a grade das 14 canônicas** | `Merchandising` e `Curadoria` **não são** áreas canônicas |
| 4 | ⚠ **Um bloco da página da NK não abriu** (`unknown_block`) | é o `Plano de Sucesso do Cliente` |

## 1 · 🟢 O achado estrutural: existe um TEMPLATE de pessoa na página do cliente `[C]`

**Osklen e NK STORE têm o mesmo toggle `Pessoas`, com os mesmos 4 blocos:**

| Bloco | O que pede |
|---|---|
| `Diretores e Representantes Legais` | Nome · Cargo · E-mail · Telefone |
| `Responsável pelo Financeiro` | Nome · Telefone · E-mail |
| `Responsáveis pelos Projetos` | **Diretoria** · **Líderes do Projeto** · **Líderes de Departamentos** |
| `Responsável Tecnologia` | Nome · Cargo · Telefone · E-mail · Observação |

🟢 **É o mapa de pessoa que o corpus precisava, e ele já estava desenhado.**
🔴 **Na Osklen está com os rótulos e sem uma linha preenchida** — template nunca usado.

> **Isto muda o plano:** a lacuna `cargo`/`área` **não é falta de modelo, é falta de
> preenchimento.** E dá para medir cliente a cliente quantos preencheram.

## 2 · NK STORE — 13 pessoas com cargo e área, das quais 8 eram invisíveis `[C]`

| Pessoa | Cargo | Área (como a fonte nomeia) | Tinha ficha antes? |
|---|---|---|:-:|
| Regiane Konopka | **Diretora de Merchandising** (Compras, Industrial, Compliance) | Merchandising | ❌ |
| Stella Sunaga | **Diretora de Estilo** | Estilo | ❌ |
| Larissa Cid Castilho Batista | Gerente de Projeto / Gerente de Produto | `[a preencher]` | ✅ |
| Marina Sacramento | **PMO** — Compradora de Produtos Acabados | Compras | ❌ |
| Robson Bazan | Gerente Industrial → PCP | PCP | ❌ |
| Andressa | Coordenadora do PCP | PCP | ✅ |
| Bruna | Coordenadora do Planejamento | Planejamento | ✅ |
| Julia | Coordenadora de Estilo | Estilo | ✅ |
| Samuel | Coordenador de Estilo | Estilo | ❌ |
| **Hermes Gonçalves Santiago Junior** | **Gerente de TI** | Tecnologia | 🔺 **apagado por mim** |
| Alexandre de Sá Pereira | Representante Legal | Diretoria | ❌ |
| Gustavo Annechino de Souza e Almeida | Representante Legal | Diretoria | ❌ |
| Silvia Shirlei Dias | Responsável pelo Financeiro | Financeiro | ❌ |

> 🔴 **8 das 13 nunca abriram demanda — e por isso não existiam no corpus.** Entre elas as **duas
> diretoras do projeto**. **A base de demandas mede quem abre chamado, não quem manda.**

**A NK STORE passou de 15 para 24 fichas.** As 11 vindas só das demandas seguem sem cargo — e
agora a ficha diz **por quê**: *"não aparece no toggle `Pessoas` da página do cliente"*.

### 2.1 · ⚠ Uma frase da fonte que vale mais que um cargo

Sobre a Coordenadora do PCP, a página anota, escrito pela própria uMode:

> *"Se ela está feliz com o projeto, estamos bem."*

**É um termômetro de projeto declarado, numa pessoa nomeada.** Ficou na ficha dela.

## 3 · 🚨 A credencial de produção da NK STORE está em texto claro na página

O toggle `Documentos › Conexão com Linx` traz **usuário, senha, IP, porta e o nome do banco de
produção**. `[C]`

> 🚨 **É a mesma credencial que já estava na lista de rotação desde 21 set 2026 — e agora sei
> exatamente onde ela mora.** **Não reproduzo o valor aqui nem em ficha nenhuma.**
> **A rotação continua sendo ação sua, e continua sendo a pendência mais urgente do projeto.**

**Também há CPF e telefone pessoal de dois representantes legais.** Pela política do
`AGORA.md` § 8.1, **nada disso entrou no corpus** — a ficha registra que existe e onde.

## 4 · 🆕 `uBuy` — um produto que não está em nenhuma das duas listas `[C]`

| Onde | O que diz |
|---|---|
| Página da **Osklen** | *"**uBuy: fup** — início: Janeiro 2026 — entrega: +d???"* |
| Página da **NK STORE** | *"Follow Up de Entregas → Pedidos de Compras → **uBuy (oportunidade)**"* |

🔴 **`uBuy` não é um dos 7 `Módulos Contratados` nem uma das 16 Soluções do Portfólio.**
É nome da família legada (`uFlow`, `uPlan`, `uRocket`, `uDash`) e trata de **follow-up de entrega e
pedido de compra** — tema de `FornecAI`, que o corpus registra como *"ainda não nasceu"*.

> ⚠ **Não afirmo que `uBuy` é o `FornecAI`.** Afirmo que **existe um produto vivo com data de
> início e não está no portfólio de 16.**

## 5 · 🔴 `Oficina` — a sexta evidência de que falta uma área de produção interna

O processo da NK STORE, descrito na própria página, tem **`Oficina` como etapa**: *"A oficina
**interna** é responsável pela produção das peças... recebem as modelagens e tecidos do
departamento de estilo e realizam o corte, costura e acabamento"*, e **coordena com as facções
externas**.

**O fluxo declarado:** `Planejamento → Estilo → Compras/Merchandising → PCP → Oficina`,
com `Curadoria` como ramo paralelo a partir do Planejamento.

> 🔴 **É a sexta evidência independente do item 234 (`15_Producao-Interna`).**
> E traz um segundo problema: **`Merchandising` e `Curadoria` também não existem na grade
> canônica de 14** — e aqui não são apelido, são etapas do processo com dono.

## 6 · Osklen — o que a página entrega, e o que ela denuncia `[C]`

| Achado | Leitura |
|---|---|
| `uFlow (nova tecnologia)` — **início fev/2025**, entrega *"Junho ou Agosto 2025???"* | ⚠ **as três interrogações são da fonte.** Data de entrega nunca cravada |
| `uBuy: fup` — início **jan/2026**, entrega `+d???` | mesma marca de indefinição, um ano depois |
| Toggle `Pessoas` **inteiramente vazio** | 🔴 conta em `Operação Assistida` **sem uma pessoa nomeada na própria página** |
| `Documentos Implantação uFlow` — 11 itens listados **como texto, não como link** | ⚠ **nomeados e não endereçáveis** |
| `Pesquisa de Satisfação do treinamento` · `Pesquisa Satisfação Kick Off` | 🆕 **existe medição de CSat por cliente** — fonte nunca varrida |
| `Integração de Escrita - Plano de Comunicação` **e** `(1)` | ⚠ duas páginas, mesmo nome |

## 7 · O que isso muda no plano de varredura

1. 🔴 **Abrir a página do cliente deixa de ser opcional: é onde `cargo`, `área` e as pessoas de
   diretoria vivem.** Nenhuma base tem isso.
2. 🔴 **A base de demandas mede quem abre chamado, não quem decide.** Usá-la como censo de pessoa
   subestima exatamente a camada de liderança.
3. **Medir quantos clientes preencheram o toggle `Pessoas`** é medir a prontidão do atendimento —
   e é barato, uma leitura por cliente.
4. **Varrer página é varrer risco:** a segunda página que abri tinha uma credencial de produção.
   **O protocolo precisa mandar procurar segredo em toda página de cliente aberta.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1–§5 | Notion — página `NK STORE` (`0f24dfbe…`), **aberta por inteiro** | **22 set 2026** |
| §1, §4, §6 | Notion — página `Osklen` (`6463bb11…`), **aberta por inteiro** | **22 set 2026** |
| §0 | `scripts/gera-fichas-pessoa.py`, versão anterior a esta sessão | **22 set 2026** |
