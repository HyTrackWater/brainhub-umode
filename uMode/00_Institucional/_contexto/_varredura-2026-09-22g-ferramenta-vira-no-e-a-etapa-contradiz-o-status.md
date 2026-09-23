---
aliases:
  - "Varredura 22 set 2026 (g) — ferramenta vira nó, e a `Etapa` contradiz o `Status`"
tags:
  - tipo/registro
  - casa
---
# Varredura 22 set 2026 (g) — ferramenta vira nó, e a `Etapa` contradiz o `Status`

> Continuação da varredura. O Vinicius travou o modelo, textual: *"praticamente tudo que for uma
> entidade é arquivo? Ou seja, ferramenta, pessoas, empresas, áreas, demandas, RFIs, tudo... As
> reuniões, contextos gerais, e-mails, tudo isso vai estar de alguma forma ligada a esses nós
> maiores na escala de hierarquia."*
>
> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**

## 0 · Declaração de completude — o que esta varredura NÃO alcançou

| # | Lacuna | Consequência |
|---|---|---|
| 1 | 🔴 **Reunião, e-mail e agente continuam sem ser arquivo** | **3 dos 5 tipos que faltavam seguem como prosa** |
| 2 | 🔴 **A ficha de ferramenta não liga a área nem a demanda** | o campo **não existe** em nenhuma das duas bases |
| 3 | ⚠ **`Responsável Pela Etapa` aponta para uma base que dá 404** | não sei quem responde por etapa nenhuma |
| 4 | ⚠ **Não abri as 5 páginas de etapa** | sei o nome e o tipo, **não o conteúdo do processo** |
| 5 | ⚠ **`Segmentação Grupos` é outra relação não varrida** | mais um eixo de cliente ainda fechado |

## 1 · O placar de "entidade = arquivo", antes e depois `[C]`

| Entidade | Antes | Depois |
|---|---:|---:|
| Instituição (Casa + 49 clientes) | ✅ 50 | ✅ 50 |
| Área | ✅ 694 | ✅ 694 |
| Pessoa | ✅ 158 | ✅ 158 |
| Demanda | ✅ 1.021 | ✅ 1.021 |
| RFI | ✅ 102 | ✅ 102 |
| Solução do portfólio | ✅ 16 | ✅ 16 |
| **Ferramenta** | 🔴 **0** — prosa em 249 arquivos | 🟢 **16** |
| Reunião / ata | 🔴 0 | 🔴 **0** — 1.161 conhecidas |
| E-mail | 🔴 0 | 🔴 **0** — 92 conhecidos |
| Agente | 🔴 0 | 🔴 **0** — 4 nomeados na Arquitetura V1 |

**Seis tipos eram nó. Agora são sete. Faltam três.**

### 1.1 · Por que a ferramenta foi para duas pastas, e não uma

| Pasta | O que guarda | Quantas |
|---|---|---:|
| `03_Produto-e-Solucoes/_ferramentas/` | os **módulos que a uMode vende** | **7** |
| `06_Tecnologia/_ferramentas/` | os **sistemas de terceiro** com que a uMode integra | **9** |

> **Linx não é produto da uMode.** Guardar `Linx` dentro de "Produto e Soluções" faria um leitor
> futuro concluir o contrário. `[P]` **A separação é proposta minha** — item nas pendências.

### 1.2 · O que o gerador se recusou a fazer

- **Não fundiu módulo com Solução do portfólio.** O `CONTEXT.md` trava que só `uPlan → PlanejAI`
  e `uFlow → DesenvolvAI` estão confirmados, e **proíbe inferir por nome parecido**. Das 7 fichas
  de módulo, **1 tem sucessor confirmado e 6 ficaram `[a preencher]`**.
- **Não desmembrou `Linx / SAP` nem `SAP e Linx`** em dois vínculos. O cliente aparece nas duas
  fichas, **com o valor literal citado**, e a ficha diz que não se decidiu.
- **Não fundiu `Totvs` com `Totvs Moda`.** Suspeita se levanta, fusão só com confirmação humana.
- **Não criou ficha para `Sem Integração` nem `Não`** — são marcas de **ausência** de ferramenta.

## 2 · 🔴 `Millennium` é opção viva que nenhum cliente usa `[C]`

O enum `ERP/Integração` tem **13 opções**. O corpus conhecia **11**.

**As duas que faltavam:** `Millennium` e `Não`.

- 🔴 **`Millennium`: zero clientes.** Opção construída e nunca usada.
- 🔴 **`Não` e `Sem Integração` são o mesmo conceito com dois rótulos** — mesmo defeito já
  registrado em `Linx / SAP` × `SAP e Linx`. **É o terceiro par duplicado no mesmo campo.**

## 3 · 🔴 O achado: existe uma base `Etapas do Processo de Clientes` — e ela discorda do `Status`

`collection://348b1d38-e768-80d0-847e-000bea495254`. **Nunca apareceu em varredura nenhuma.** `[C]`

**7 etapas, em dois tipos:**

| Tipo | Etapas | `Status` da etapa |
|---|---|---|
| **`Padrão`** (5) | Pré Onboarding → Onboarding → Operação Assistida → Ongoing → Churn | Churn é `Not started`; as 4 são `In progress` |
| 🆕 **`Especial`** (2) | **`Projetos e Inovação`** · **`Squad de Urgência`** | ambas `In progress` |

> 🔴 **`Projetos e Inovação` e `Squad de Urgência` não têm um cliente sequer.** Duas etapas
> declaradas, vivas, e **vazias** — o mesmo padrão do CX Hub: estrutura criada, nunca preenchida.
> ⚠ **Mas `Projetos e Inovação` é exatamente onde o CAEDU 2.0 caberia.**

### 3.1 · 🔴 Cinco clientes têm `Status` e `Etapa` dizendo coisas diferentes `[C]`

| Cliente | `Status` diz | `Etapa` diz | Distância |
|---|---|---|---|
| 🔴 **Caedu** | **`Onboarding`** | **`Ongoing`** | **um passo à frente** |
| **Osklen** | `Operação Assistida` | `Onboarding` | um passo atrás |
| **Moda Objetiva** | `Operação Assistida` | `Onboarding` | um passo atrás |
| **Lofty Style** | `Ongoing` | `Operação Assistida` | um passo atrás |
| **Loungerie** | `Onboarding` | `Pré Onboarding` | um passo atrás |

**26 dos 31 batem. 5 não batem.** E os 5 **não erram para o mesmo lado**.

> 🔴 **É o sétimo caminho independente mostrando que `Status` ≠ realidade** — e o mais forte de
> todos, porque **a contradição é interna à mesma base, entre dois campos da mesma linha.** Não é
> o corpus discordando do Notion: **é o Notion discordando de si mesmo.**

### 3.2 · 🔴 E o que isso faz com a leitura do CAEDU

A CAEDU é o único dos cinco que está **adiante** do que o `Status` declara. E o `Status`
`Onboarding` é **a premissa sobre a qual o projeto CAEDU 2.0 está sendo montado**.

Some-se ao que a varredura (f) já achou — a dor de `Griffe › Linha › Grupo/subgrupo` escrita na
weekly de **16/09/2025**, repetida em **jul/2026** e **ago/2026**:

> **A CAEDU não é um cliente entrando. É um cliente que já operou, tem ~47 atas de weekly desde
> abr/2024, e está sendo tratado como estreia.** ⚠ **Isto é leitura minha, não fonte** — mas as
> duas evidências apontam na mesma direção, e é pergunta para o Vinicius.

### 3.3 · ⚠ E dezenove clientes não têm etapa nenhuma — incluindo o maior

**31 de 50 linhas têm `Etapa`. 19 não têm.** Entre as 19:

🔴 **`Reserva`** — **7 módulos contratados, o mais completo da carteira** — ·
**`Oficina Reserva`** (5 módulos) · **`NV`** (4) · **`Baw`** (4).

> **Os quatro estão fora do processo declarado.** ⚠ **Não sei se é lacuna de preenchimento ou se
> contas grandes simplesmente não passam pelo funil.** As duas leituras cabem no dado.

## 4 · O que entra no protocolo de varredura

1. **`Mapa de Clientes` tem 5 relações, e eu só tinha varrido 2.** Ainda fechadas:
   `Etapas do Processo de Clientes` (agora aberta), **`Segmentação Grupos`**,
   **`Atendimento 2024`**, `Documentação Clientes`, `Chamado&Atendimento`.
   **Varrer uma base é varrer também para onde ela aponta.**
2. **Enum é fonte de entidade.** Um `multi_select` de 7 opções são 7 nós — e a opção **sem nenhum
   uso** (`Millennium`) é tão informativa quanto a mais usada.
3. **Dois campos da mesma linha podem discordar.** Ler um só é escolher uma verdade sem saber.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1 | contagem por script sobre o próprio corpus | **22 set 2026** |
| §2, §3 | Notion — `collection://ec041afd-…` e `collection://348b1d38-…-000bea495254`, via SQL | **22 set 2026** |
