# Varredura 23 set 2026 — o campo `Participantes` das 1.162 reuniões não tem nome

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
>
> **Fonte:** base `Reuniões Compartilhadas com Clientes`,
> `collection://09a4a94e-036c-4836-a097-de8feda4df1c`, consultada por SQL em 23/09/2026.
>
> **Tratamento:** `T2`. Nenhum telefone, CPF ou credencial apareceu.

## 0 · 🔴 Declaração de completude — este registro é um NEGATIVO

**O alvo era presença nominal com data.** O `AGORA.md` listava este campo como *"a melhor fonte de
pessoa ativa ainda não extraída"*, e o `_pendencias-gerais.md` o repetia desde 22 set.

🔴 **Ela não existe. 24 dos 25 IDs de participante não resolvem para nome nenhum.**
**99,2% das presenças ficam anônimas.** O que sai é uma **matriz de atividade com uuid estável e
data** — não uma lista de pessoas.

⚠ **Corrijo a expectativa que eu mesmo criei nos dois documentos.**

## 1 · O que a base é `[C]`

**1.162 linhas** — e não 1.161, como o corpus vinha repetindo desde 22 set.

| Campo | Preenchido | % |
|---|---:|---:|
| `Cliente` | 1.155 | **99,4%** |
| `date:Data:start` | 1.076 | 92,6% |
| `Participantes` | 844 | 72,6% |
| `Tipo Reunião` | 440 | 37,9% |
| `Áreas` | 178 | 15,3% |
| `Tactiq` | 114 | 9,8% |
| `Pendências` | 33 | 2,8% |
| `Gravação` | 17 | 1,5% |
| 🔴 **`Pessoa`** | **2** | **0,2%** |

🔴 **O campo chamado `Pessoa` está vazio em 99,8% das linhas.** O campo que deveria nomear gente
é o menos preenchido da base inteira.

**`Tipo Reunião` tem 5 valores:** Weekly Projeto (218) · Status Report (153) ·
Alinhamento de Projeto (67) · Treinamento (1) · CX (1).

## 2 · 🔴 Por que a presença é anônima `[C]`

**1.694 pares participante-reunião, em apenas 25 IDs distintos.**

**Resolve: 1 de 25.**

| Nome | E-mail | Reuniões | Primeira | Última |
|---|---|---:|---|---|
| João Risoléo | `joao.risoleo@umode.com.br` | 13 | 2024-07-10 | 2025-06-13 |

**Não resolvem: 24 de 25** — os 10 maiores:

| uuid | Reuniões | Primeira | Última |
|---|---:|---|---|
| `bab7e908…` | **427** | 2023-06-05 | 2026-09-17 |
| `c7bd6203…` | **317** | 2023-06-19 | 2026-09-17 |
| `6fce79e0…` | **313** | 2025-01-24 | 2026-09-24 |
| `0e5d14d4…` | **243** | 2023-08-15 | 2026-08-20 |
| `ffbf0278…` | **189** | 2024-10-15 | 2026-09-18 |
| `401fae20…` | 47 | 2025-04-24 | 2026-07-14 |
| `05735673…` | 40 | 2024-04-09 | 2024-10-18 |
| `a565ac87…` | 17 | 2024-06-13 | 2026-07-30 |
| `44b67484…` | 16 | 2023-08-31 | 2026-07-30 |
| `97ff192a…` | 14 | 2025-05-06 | 2026-05-20 |

**A via está esgotada dentro da API, e isso foi verificado por TRÊS caminhos independentes:**
`get-users` com `user_id` devolve lista vazia · o modo `rows` devolve só o URI · e o `fetch` da
página traz `<mention-user url="user://…">` **sem nome**.

🔴 **O workspace inteiro tem 5 pessoas e 9 bots no diretório.** Os 24 uuids não estão entre eles —
são **ex-membros ou convidados removidos**, cujo registro o Notion não devolve mais.

### 2.1 · `[P]` O que 25 IDs em 3 anos significam — e é interpretação

**25 participantes distintos para 1.162 reuniões com 47 clientes** é pouco demais para ser o time
dos clientes. `[P]` **O campo `Participantes` registra o time INTERNO da uMode, não quem estava do
lado do cliente.** Se for isso, **esta base nunca foi fonte de pessoa de cliente** — e o corpus a
tratava como se fosse.

⚠ **Não afirmo.** Mas nenhum dos 25 aparece nas tabelas de usuário de cliente que já extraímos.

## 3 · 🟢 O que SAIU de aproveitável: intensidade de atendimento por conta `[C]`

**Dado novo, que o corpus não tinha em número nenhum.**

| Reuniões | Cliente | Status hoje |
|---:|---|---|
| **126** | Luiza Barcelos | Ongoing |
| **111** | NK STORE | Ongoing |
| **101** | Osklen | Operação Assistida |
| 83 | Lofty Style | Ongoing |
| 75 | Lenny Niemeyer | 🔴 **Churn** |
| 71 | Cambos | Ongoing |
| 64 | NV | Ongoing |
| 58 | Moda Objetiva | Operação Assistida |
| **57** | Highstil | 🔴 **Churn** |
| 44 | VIX | Ongoing |
| 41 | Oficina Reserva | Ongoing |
| 38 | Plie | 🔴 **Churn** |
| 36 | Recco | 🔴 **Churn** |
| **35** | **Caedu** | **Onboarding** |
| 34 | Vivara | 🔴 **Churn** |

🔴 **Cinco dos quinze mais atendidos estão em `Churn`** — Lenny (75), Highstil (57), Plie (38),
Recco (36) e Vivara (34). **Somam 240 reuniões.** ⚠ **Volume de reunião não preveniu saída** —
mesma leitura do CSat 9,48 da Lenny (item 540).

🔴 **A CAEDU tem 35 reuniões nesta base, e é o cliente-foco do teste.** ⚠ **E o diário da CAEDU
registra ~47 atas de weekly na página dela** — **são conjuntos diferentes**, com fontes diferentes.
**Não os fundi e não sei qual é o total real.**

**Distribuição por ano:** 2023: **121** · 2024: 111 · **2025: 559** · 2026: 285 ·
🔴 **sem data: 86**.

⚠ **2023 tem 121 reuniões e o corpus nunca olhou para esse ano.**

## 4 · 🟢 Achado técnico reaproveitável

**O SQL do conector Notion aceita `json_each()`.** Isso permite desdobrar array de `person` ou de
`relation` e agregar **server-side**, dispensando paginação. As 1.162 linhas foram agregadas sem
uma única chamada paginada.

🔴 **Vale para qualquer array do Notion daqui em diante** — inclusive o `Atendimento 2024`, que
continua não resolvido pela mesma armadilha de relation (item 504).

## 5 · O que fica como decisão

| # | Pergunta | Para quem |
|---|---|---|
| 1 | 🔴 **Quem são os 5 uuids de topo?** Abrir UMA reunião no Notion pela UI mostra avatar e nome — **cinco olhadas cobrem 88% das presenças.** É a única via que resta | Vinicius / João |
| 2 | ⚠ **`Participantes` é o time da uMode ou do cliente?** Muda o que a base significa | Vinicius |
| 3 | 🔴 **86 reuniões sem data e 318 sem participante** — completar ou aceitar? | Atendimento |
| 4 | **As 35 reuniões da CAEDU aqui × as ~47 atas na página dela** — qual é o total real? | Atendimento |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — foto com data. Correção vira registro novo.
