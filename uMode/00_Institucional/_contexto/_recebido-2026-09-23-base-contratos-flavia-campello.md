# Recebido 23 set 2026 — a base de contratos da Flávia Campello, e a terceira taxonomia

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
>
> **Fonte:** `clientes-umode.md` + `clientes-umode.json`, gerados em 23/09/2026 a partir da
> **planilha interna de controle de contratos (Google Sheets)** do Financeiro, entregues pelo
> Vinicius. **41 registros — 21 ativos, 20 ex-clientes.**
>
> **Tratamento:** a fonte declara fora de escopo os dados de faturamento. **Nenhum valor, prazo
> de pagamento ou dado de CA foi copiado.** Razão social e CNPJ são `T2`.

## 0 · Declaração de completude — o que este registro NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não fecha o mapeamento legado → Portfólio** | só **dois** estão confirmados no `CONTEXT.md`, e nada aqui autoriza confirmar um terceiro |
| 2 | **Não sei o que é `Fashion IA`** | 🔴 o termo tem **zero ocorrência** no corpus inteiro |
| 3 | **Não sei se `uBuy` é o EnriqueceAI** | há indício, e há um caso que o contradiz (§ 3) |
| 4 | **Não abri a planilha de origem** | trabalhei sobre o `.md`/`.json` derivados |
| 5 | **Não criei nenhum cliente novo** | 11 aparecem aqui e não no corpus; **criar é decisão** |

## 1 · 🔴 O achado estrutural: são TRÊS taxonomias, não duas

O corpus já mantinha duas listas separadas, e o `CONTEXT.md` proíbe fundi-las por nome parecido:

| # | Taxonomia | Onde vive | Quantos |
|---|---|---|---:|
| 1 | **Módulos contratáveis do uFlow** | campo `Módulos Contratados` do `Mapa de Clientes` | **7** |
| 2 | **Soluções do Portfólio** | `03_Produto-e-Solucoes/` | **16** |
| 3 | 🆕 **Serviços faturados** | **esta base do Financeiro** | **11** |

**A terceira é a que faltava — e ela não é paralela às outras duas. Ela MISTURA níveis na mesma
coluna `Serviços`:**

| Nível | Itens da base |
|---|---|
| **Plataforma** | `uFlow` · `uRocket` |
| **Produto separado** | `uBuy` · `uPick` · `uPlan` · `Fashion IA` |
| **Módulo dentro do uFlow** | `Gestão de coleções` · `Reports` |
| **Serviço, não software** | `Workshop` · `SaaS` · `IPSP` |

🔴 **Consequência prática:** a `Loungerie` aparece com o serviço **`Gestão de coleções` e sem
`uFlow`** — mas `Gestão de coleções` **é um módulo do uFlow**. **Contar clientes de uFlow por
esta coluna subconta.** Idem a `NV`, que tem `uFlow` **e** `Reports` lado a lado, sendo o
segundo um módulo do primeiro.

## 2 · 🟢 O que a base CONFIRMA — e é confirmação cruzada, de fonte independente

**`uPlan` → `PlanejAI`** está travado no `CONTEXT.md` desde 13 jul 2026, pelo Vinicius.
A ficha do PlanejAI diz: *Clientes que contrataram: **Reserva** — cliente âncora segundo o
ÍNDICE MESTRE*, com a ressalva explícita de que **o índice não qualificava se era
`(contratado)` ou `(piloto)`, e o protocolo exige o qualificador**.

🟢 **A base do Financeiro fecha isso: `Reserva` tem `uPlan` entre os serviços.**
**Está na planilha de contratos — logo é `(contratado)`, não piloto.**

🔴 **E isso responde direto o que o Vinicius levantou** sobre plataformas que ainda rodam no
Lovable e os clientes já usam: **o PlanejAI não é só usado, ele é faturado**, sob o nome legado
`uPlan`. **A solução é `MVP` na nossa própria ficha de maturidade e a receita já entra.**

## 3 · 🔴 O gap do EnriqueceAI — e por que eu NÃO afirmo que é o `uBuy`

O Vinicius aponta **EnriqueceAI em RESERVA e NV**. A ficha do EnriqueceAI registra **NV**
(*uso real confirmado em reuniões de jul 2026*), **sem Reserva**.

**Na base do Financeiro:**

| Cliente | Serviços |
|---|---|
| Reserva | `uFlow` · **`uBuy`** · `uPlan` |
| NV | `uFlow` · **`uBuy`** · `Reports` |
| Osklen | `uFlow` · **`uBuy`** |

**A interseção Reserva ∩ NV, fora do uFlow, é exatamente `uBuy`.** Tentador — e é onde eu paro.

🔴 **O que impede a conclusão: a Osklen também tem `uBuy`, e o Vinicius não a citou.**
Duas leituras sobrevivem, e a diferença entre elas muda a decisão:

- **(a)** `uBuy` **é** o nome de faturamento do EnriqueceAI → então a **Osklen também usa**, e a
  ficha do produto está incompleta em dois clientes.
- **(b)** `uBuy` **é outra coisa** → então o **EnriqueceAI não é faturado em ninguém**, e esse é
  exatamente o gap de receita que o Vinicius suspeita.

⚠ **O EnriqueceAI tem nome legado registrado, e não é `uBuy`:** a ficha diz **`CadastroAI`** —
*no desenho original era CadastroAI como módulo de enriquecimento*. **`CadastroAI` não aparece
na base do Financeiro.** Isso **pesa para a leitura (b)**, mas não fecha: nome de desenho e nome
de faturamento não precisam coincidir.

🔴 **É pergunta para o Comercial/Financeiro, não dedução minha.**

## 4 · 🔴 `Fashion IA` — um serviço faturado que o corpus não conhece

**3 clientes ATIVOS: `PUKET` · `AGUA DE COCO` · `INDUSTRIA E COMERCIO DE CONFECCOES LA MODA`.**

🔴 **O termo tem ZERO ocorrência em todo o corpus** — verificado por busca nos 2.513 `.md`.
Não está nos 7 módulos, não está nas 16 Soluções, não está em varredura nenhuma.

⚠ **E a Puket é um dos clientes mais varridos que temos** — 43 pessoas, página aberta,
treinamentos mapeados — **e nada em nenhuma dessas fontes menciona `Fashion IA`.**
**Não afirmo o que é. Afirmo que é receita ativa em 3 contas e que o cérebro não sabe que existe.**

## 5 · 🔴 Mentoria — o gap que o Vinicius apontou, confirmado

**Não existe serviço `Mentoria` na base do Financeiro.** O mais próximo é **`Workshop`**, em
**um** cliente (`SINBI`).

**Mas a mentoria existe e tem acervo próprio:**

- `AGENTES E PROJETOS / **Projeto: Mentoria (João Risoléo)**` — teamspace do Notion, listado
  como fonte **não varrida** nos 48 diários, junto de `Metodologia MBS`.
- O `protocolo-varredura-cliente.md` § 9 cita **um CRM de mentoria** como fonte de porte e CEO.
- A busca de 23 set achou `AGENTES E PROJETOS / Projeto: Mentoria / **CRM — EducAI**`.

🔴 **Há uma operação de mentoria com CRM próprio e acervo próprio, e ela não aparece na base de
contratos.** **Ou não é faturada por aqui, ou é faturada como `Workshop`.**

## 6 · 🔴 Onze clientes que a base tem e o corpus não

| Cliente | Status | Serviço |
|---|---|---|
| **SINBI** | 🔴 **ativo** | `Workshop` |
| **Tempo de Criança** | 🔴 **ativo** | `SaaS` |
| CRIS-FAEL · Tropical Fashion · Luxo das Marias · Opera Kids · Four One Moda · Aladim Decorações · Ribeiro e Pavani · Nanaminze · FORMITZ | ex-cliente | `uRocket` |

⚠ **Os dois ativos já eram conhecidos por outro caminho — e de forma que CONTRADIZ a base:**

- **`Sinbi`** está no `_backlog-infra-tecnologia.md` item 3.2b — *tem dezenas de submarcas sob
  ela*, vinda da base legada da Taxonomia. **Nunca como cliente com serviço contratado.**
- **`Tempo de Criança`** está no `_varredura-ferramentas-produtos-areas.md` com a anotação
  literal **(não existe no CRM)**, e o backlog 3.2 cita `Tempo de Criança (uRocket)` como exemplo
  de conta-por-módulo. 🔴 **A base do Financeiro diz que é cliente ATIVO com `SaaS`.**

🟢 **Os 9 ex-clientes de `uRocket` fecham uma dúvida antiga:** o uRocket teve **15 contas** e hoje
tem **uma** (`Cambos`). **O produto não foi só descontinuado — ele teve carteira própria, e ela
evaporou.** **É história de portfólio que o corpus não tinha.**

## 7 · O que fica como decisão

| # | Pergunta | Para quem |
|---|---|---|
| 1 | 🔴 **O que é `Fashion IA`?** É uma das 16 Soluções com outro nome, ou um 17º item? | Comercial |
| 2 | 🔴 **`uBuy` é o EnriqueceAI?** Se for, a Osklen também usa. Se não, o EnriqueceAI não é faturado. | Comercial |
| 3 | 🔴 **Mentoria é serviço faturável?** Tem CRM e acervo, não tem linha na base. | Vinicius / João |
| 4 | **`SINBI` e `Tempo de Criança` viram casa no corpus?** São ativos e não existem lá. | Vinicius |
| 5 | **`IPSP` e `uPick`** aparecem só na VIX. O corpus citava `IPSP` como **oportunidade na Cambos** — são a mesma coisa? | Comercial |
| 6 | **A coluna `Serviços` mistura plataforma, módulo e serviço.** Separamos na origem, ou traduzimos na entrada? | Vinicius |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — foto com data. Correção vira registro novo.
