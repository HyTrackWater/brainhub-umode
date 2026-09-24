---
aliases:
  - "Varredura 24 set 2026 — os exports do vault que ninguém tinha aberto"
tags:
  - tipo/varredura
  - casa
---
# Varredura 24 set 2026 — os exports do vault que ninguém tinha aberto

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
> **Fonte:** `umode-os-vault` → `BrainHub/uMode/_Clientes/_geral/notion/`, **6 arquivos**,
> lidos em 24/09/2026. **Leitura apenas** — o vault não foi tocado.

## 0 · ⚠ O que esta varredura NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não fecha as ~32.000 lacunas de `[a preencher]`** | a maior parte vem de **processo**, não de varredura — § 4 |
| 2 | **Não explica por que a série de saúde para em 2024** | a base acaba ali. **Não perguntei a ninguém ainda** |
| 3 | **Não valida a nota contra o cliente** | `[D]` a base é a leitura da uMode; **não há CSat aqui** |
| 4 | **`Projetos.csv`, `Módulos.csv` e `uFlowDataBase.csv` não estão nesta pasta** | eu os havia citado como existentes. **Não os encontrei em `_geral/notion/`** — o que não é o mesmo que dizer que não existem |

## 1 · 🔴 Como isto foi achado, e a lição vale mais que o achado

Eu estava a um passo de escrever que **24.422 lacunas de demanda eram "campo que nenhuma fonte
tem"**. O que me segurou foi a **uniformidade**: `Destino organizacional`, `Co-responsáveis`,
`Datas`, `Resultado esperado`, `Quem aprova` estavam vazios em **993 de 993** arquivos. E
`Missão da cadeira`, `Como se descreve`, `Personalidade` em **402 de 402** fichas.

⚠ **Lacuna uniforme demais não é falha de varredura — é template que nunca foi alimentado.**
🟢 **Isso é pergunta sobre a FONTE DE ALIMENTAÇÃO, não sobre o documento.** Foi essa virada que
levou à pasta. **O corpus só tinha usado 1 dos 6 exports** (`Mapa de Clientes.csv`).

*(É a terceira variação de **"ausência de fonte é hipótese, não conclusão"**. As duas anteriores
estão no `STATE.md`: o export de julho que estava no histórico do Git, e os módulos que estavam
atrás de um clone `--single-branch`.)*

## 2 · O placar dos 6 arquivos — **medido, não estimado**

| Arquivo | Linhas | Estado | Ganho real |
|---|---|---|---|
| `Mapa de Clientes.csv` | — | já usado antes | — |
| `Reuniões Compartilhadas com Clientes.csv` | — | já lido em 22/09 | — |
| **`Demandas de Clientes.csv`** | 836 | 🟢 **aplicado hoje** | **524 demandas enriquecidas**; lacunas 24.422 → **22.441** |
| **`Feedback Interno Clientes.csv`** | 428 | 🟢 **aplicado hoje** | **24 clientes** ganharam histórico de saúde — § 3 |
| **`RFI Escopo - Lista de Entregáveis.csv`** | 53 | ⚠ **quase todo absorvido** | **3 campos** e **2 RFIs** — § 5 |
| **`Formulário de Demandas.csv`** | **2** | 🔴 **o menor arquivo é o mais importante** — § 4 | muda a natureza da lacuna |

⚠ **O RFI é o caso que justifica medir antes de construir.** Eu ia escrever um script de
enriquecimento inteiro para ele. **A medição mostrou que o corpus já tinha 85 RFIs contra 53 do
CSV, e 41 valores contra 24.** O CSV é export mais **pobre** e mais **antigo** que a fonte que o
corpus já tinha consumido. **Um script teria rodado, reportado sucesso e escrito quase nada.**

## 3 · 🔴 O health score que o corpus não tinha

**388 das 428 linhas são `Feedback Semanal`.** Havia um **ritual semanal de avaliar cada conta**.

🔴 **Isto NÃO é satisfação do cliente.** O campo `Quem` é sempre alguém da uMode — Taís Moser,
Andrea Holmer, Laura, Elizabeth, Julianne. **É a leitura que a uMode fazia da própria carteira.**
⚠ **Não confundir com CSat**, que vem de pesquisa **com** o cliente e é outra coisa.

| Cliente | n | média | flags | Percepção dominante |
|---|---:|---:|---:|---|
| **Estrela** | 7 | 🔴 **2,00** | **57%** | Cronograma atrasado **e cliente insatisfeito** |
| **Studio Z** | 38 | 🔴 **2,84** | **53%** | Cronograma atrasado **e cliente insatisfeito** |
| **NTK** | 18 | 🔴 **2,89** | **50%** | **Bloqueio** |
| Oficina Reserva | 12 | 🔴 2,92 | 8% | Precisamos de atenção e foco |
| **Vivara** | 17 | 🔴 **3,00** | 🔴 **71%** | Precisamos de atenção e foco |
| Seven Global | 9 | 🔴 3,22 | 33% | Cronograma atrasado e cliente insatisfeito |
| Ladeira Bijuterias | 2 | 🔴 3,50 | 0% | Tudo em dia |
| 4takes | 15 | ⚠ 3,60 | 13% | Precisamos de atenção e foco |
| Lojão do Brás | 13 | ⚠ 3,62 | 15% | Tudo em dia |
| Reserva | 27 | ⚠ 3,70 | 4% | Precisamos de atenção e foco |
| Colmeia | 28 | ⚠ 3,79 | 14% | Precisamos de atenção e foco |
| Básico&Co | 17 | ⚠ 3,82 | 18% | Tudo em dia |
| VIX | 29 | ⚠ 3,83 | 14% | Precisamos de atenção e foco |
| Caedu | 21 | ⚠ 3,86 | 10% | Precisamos de atenção e foco |
| Puket | 23 | ⚠ 3,96 | 0% | Precisamos de atenção e foco |
| Camys | 6 | ⚠ 4,00 | 0% | Tudo em dia |
| Laces | 11 | ⚠ 4,00 | 0% | Tudo em dia |
| NV | 25 | 🟢 4,12 | 4% | Precisamos de atenção e foco |
| DRO | 15 | 🟢 4,27 | 13% | Tudo em dia |
| Luiza Barcelos | 19 | 🟢 4,42 | 16% | Tudo em dia |
| Baw | 28 | 🟢 4,43 | 7% | Tudo em dia |
| Cambos | 27 | 🟢 4,85 | 4% | Tudo em dia |
| NK STORE | 19 | 🟢 4,89 | 0% | Tudo em dia |
| Hyperlocal | 1 | 🟢 5,00 | 0% | Tudo em dia |

**No agregado: 220 das 427 avaliações (52%) são "atenção", "atraso" ou "bloqueio".**

### 3.1 · ⚠ As duas leituras que a tabela NÃO autoriza

1. 🔴 **A série termina em 2024.** Não há avaliação posterior nesta base. **Isso significa que o
   ritual parou, ou que passou a viver noutro lugar — e eu não sei qual dos dois.**
   ⚠ **`Vivara` com 71% de flag é um retrato de 2024**, e a Vivara hoje está em churn. **A nota
   não é o estado de hoje; é o que se registrava quando se registrava.**
2. 🔴 **24 dos 48 clientes não aparecem nesta base** — `Agua de Coco`, `Arezzo`, `Cavallari`,
   `Hering`, `Highstil`, `La Moda`, `Lenny Niemeyer`, `Lofty Style`, `Loungerie`, `Moda Objetiva`,
   `Mondepars`, `Osklen`, `Paloma concept`, `Pampili Mini`, `Phos`, `Plie`, `Recco`,
   `Ricardo Almeida`, `Simples (by Reserva)`, `Studio Minah`, `Susie Modas`, `TDC`, `Texneo`,
   `Ton Age`. **Metade da carteira.**
   ⚠ **Ausência aqui é ausência de MEDIÇÃO, não conta saudável.** Ler a tabela como ranking
   completo da carteira é exatamente o erro.

### 3.2 · 🟢 O teste que decidiu três nomes ambíguos — e é a forma que importa

O CSV usa 27 grafias. Três pares pareciam o mesmo cliente. **Nenhum foi decidido por semelhança
de string:**

| Par | Decisão | Por quê |
|---|---|---|
| `STZ` (34) + `Studio Z` (4) | 🟢 **mesmo cliente** | o `institucional.md` **já dizia, com fonte**: *"STZ é o Studio Z"*. E o CSV corrobora: `STZ` vai até **30/08/2024**, `Studio Z` começa em **21/10/2024** |
| `Básico` (11) + `Básico&Co` (6) | 🟢 **mesmo cliente** | mesmo padrão: até 27/09 (Elizabeth) → a partir de 25/10 (Julianne) |
| `Reserva` (27) + `Oficina Reserva` (12) | 🔴 **clientes DIFERENTES** | **a MESMA avaliadora (Andrea Holmer) avalia as duas no MESMO mês.** E as duas têm pasta própria |

🟢 **A regra generalizável:** **duas grafias em períodos sequenciais são uma conta renomeada; duas
grafias em período sobreposto, com o mesmo avaliador, são duas contas.** ⚠ **A distância entre as
strings não decide nenhum dos dois casos** — `Reserva`/`Oficina Reserva` são *mais* parecidas que
`STZ`/`Studio Z`, e são o par que **não** se funde.

*(Isto fecha a pergunta em aberto sobre a identidade `Oficina Reserva` × `Reserva`.)*

## 4 · 🔴 O arquivo de 2 linhas que muda a natureza da lacuna

`Formulário de Demandas.csv` tem **2 linhas de dado e 20 colunas**. **São as colunas que importam:
elas são o formulário de abertura de demanda.**

```
Título da Demanda · A demanda está relacionada a um chamado anterior? · Arquivos e mídia ·
Categoria da Demanda · Cliente · Data e horário aproximado em que o problema ocorreu ·
Descrição detalhada do problema ou necessidade · E-mail de contato · Especifique a categoria ·
Essa solicitação está impedindo o uso da plataforma? · Horário do envio ·
Navegador ou dispositivo usado · Objetivo Esperado · Participante ·
Qual o impacto dessa solicitação? · Setor - Seu nome · Status ·
URL ou caminho da tela onde ocorreu · Urgência e Impacto
```

🟢 **Três dos campos que eu estava prestes a declarar "sem fonte possível" estão aqui:**

| Lacuna no corpus | Campo do formulário |
|---|---|
| `Resultado esperado` — **vazio em 993/993** | **`Objetivo Esperado`** |
| `Criticidade` / urgência | **`Urgência e Impacto`** + `Qual o impacto dessa solicitação?` |
| identidade de quem abriu | 🟢 **`E-mail de contato`** — **o formulário já pede e-mail, não nome** |

🔴 **Logo, a lacuna não é "campo que nenhuma fonte tem". É "formulário que existe e foi usado
duas vezes".** ⚠ **Isso muda quem resolve:** não é trabalho de documentação, **é decisão de
processo** — e é o tipo de coisa que o Vinicius disse que iríamos *"conversar internamente para
avaliar"*.

⚠ **Duas sujeiras visíveis já nas 2 linhas**, e as duas são as mesmas de sempre:
- **`Cliente` vem como `Reserva` e `reserva`** — grafia livre onde devia haver chave estável.
- **`Setor - Seu nome` mistura três coisas num campo só:** `"Reserva - Engenharia - Thamires"` e
  `"Umode - Fernanda"`. 🔴 **Instituição, área e pessoa colapsadas em texto livre** — exatamente o
  que a hierarquia do BrainHub separa em quatro níveis.

## 5 · RFI — o que o CSV ainda acrescenta, e é pouco

**51 dos 53 RFIs do CSV já estão no corpus, mais ricos.** Ganho marginal medido: **1 `Valor`**,
**2 `Motivo do cancelamento`**. E **2 RFIs que o corpus não tem**:

| ID | Cliente | Assunto | Status |
|---|---|---|---|
| **RFI-37** | **NV** | Escopo — Relatório de Tarefas · **52 h** · aceite do cliente em **05/12/2025** | `RFI Q&A Negócios` |
| **RFI-72** | **uMode** *(sem cliente)* | Escopo — Compilar Alertas de Integração | `RFI em Rascunho` |

⚠ **`RFI-72` não tem cliente: é RFI da própria Casa.** O corpus só tem `_rfis` dentro de cliente.
🔴 **RFI interna é uma forma que o padrão ainda não previu** — não inventei pasta para ela.

### 5.1 · A pergunta em aberto sobre RFI ser serviço faturado — respondida, e mal

**Os números do CSV:** `Valor` em **22 de 53** RFIs, somando **R$ 85.237**; `Horas Totais` em 30,
somando **1.101 h**. 🔴 **Mas `Cobrado` está preenchido em 3 de 53** — *Sim* em 2, *Não* em 1.

⚠ **Então sim, RFI tem valor e horas.** 🔴 **E não, não dá para dizer o que foi faturado:** o
campo que responderia isso está vazio em 94% das linhas. **`Horas Trabalhadas` está em 1 de 53** —
**não há como comparar estimado contra realizado.**

*(No corpus a situação é a mesma: `Cobrada?` em 12 de 85, `Horas trabalhadas` em 4 de 85,
`Taxa aplicada (R$/h)` em **0 de 85**.)*

## 6 · 🟢 O que fica decidido aqui

1. **O `Feedback Interno Clientes` é a base de saúde da conta** e vive no `jornada.md` de cada
   cliente, em seção própria, **sempre marcada como leitura interna e não como CSat.**
2. **`STZ` = `Studio Z`; `Básico` = `Básico&Co`; `Oficina Reserva` ≠ `Reserva`.**
3. **O CSV de RFI está absorvido.** ⚠ **Não gerar script para ele** — foi medido.
4. **A lacuna de `Resultado esperado`, urgência e autor de demanda é de processo, não de
   documentação.** O formulário existe. **Decidir usá-lo é do Vinicius.**

## 7 · ⚠ O que isto deixa em aberto — para a conversa interna

| # | Pergunta | Para quem |
|---|---|---|
| 1 | **O ritual semanal de saúde parou em 2024, ou mudou de lugar?** | Vinicius / CX |
| 2 | **Por que metade da carteira nunca foi avaliada?** | Vinicius / CX |
| 3 | **O formulário de demanda volta a ser o caminho de entrada?** Se sim, `Objetivo Esperado` e `Urgência` deixam de ser lacuna sozinhos | Vinicius |
| 4 | 🔴 **`Cobrado` e `Horas Trabalhadas` quase não são preenchidos.** Sem eles **não existe margem de RFI** | Vinicius / Financeiro |
| 5 | **RFI da própria Casa (`RFI-72`) não tem onde morar no padrão** | Vinicius |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É registro datado. **O que mudar entra em registro novo**, apontando para este.

### Conexões
- [`_varredura-2026-09-23g`](_varredura-2026-09-23g-participantes-das-reunioes-sao-anonimos.md) — a
  outra vez em que um negativo valia contra a **fonte testada**, não contra o fato.
- [`_pendencias-gerais.md`](_pendencias-gerais.md) — as perguntas do § 7 entram lá.
