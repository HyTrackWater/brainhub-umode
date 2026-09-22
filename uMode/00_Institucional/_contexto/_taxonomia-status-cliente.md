# Taxonomia — o que `Status` de cliente significa, e o que ele mistura

> Escrito em **22 set 2026** por Vinicius Risoléo (com Claude Code), a partir de uma correção dele:
>
> > *"Operação assistida é momento e não cliente, certo?"*
>
> **Está certo, e a consequência é maior do que a pergunta.** Fui verificar o enum inteiro contra
> os dados dos 46 clientes e ele **mistura três coisas diferentes no mesmo campo**.

**Grau por afirmação:** `[C]` verificado na base viva, com o número · `[P]` proposta ·
`[D]` decisão que não é minha.

---

## 0 · Declaração de completude

| # | O que este documento NÃO resolve | Por quê |
|---|---|---|
| 1 | **Não sei se o enum é editável.** | Campo `Status` é `select` no Notion. Mudar afeta 50 linhas e qualquer view/filtro que dependa dele. Não mexi. |
| 2 | **Não li o schema de `organizations` da API.** | O mesmo conceito provavelmente existe no código, e pode divergir. |
| 3 | **Não sei o que `Operação Assistida` significa operacionalmente.** | Sei que é momento. **Não sei o que a uMode faz de diferente nesse momento.** Nenhuma fonte varrida define. |
| 4 | **Não entrevistei ninguém.** | Tudo aqui saiu de dado, não de conversa. |

---

## 1 · O enum vigente `[C]`

`Inativo` · `Pré Onboardings` · `Operação Assistida` · `Onboarding` · `Sem CS` · `Ongoing` · `Churn`

**Sete valores, 50 linhas na base.** Distribuição verificada em 22/09/2026:

| Status | Linhas | Destas, clientes reais |
|---|---:|---:|
| `Churn` | 20 | 20 |
| `Ongoing` | 10 | 10 |
| `Sem CS` | 7 | 7 |
| `Inativo` | 8 | **5** (3 são template, `Fornecedores` e `uMode`) |
| `Operação Assistida` | 2 | 2 |
| `Pré Onboardings` | 2 | 2 |
| `Onboarding` | 1 | 1 |

---

## 2 · 🔴 O campo mistura três eixos diferentes

### Eixo A — momento da jornada (o que o Vinicius apontou)
`Pré Onboardings` → `Onboarding` → `Operação Assistida` → `Ongoing` → `Churn`

**É uma linha do tempo.** Um cliente atravessa esses estados. **`Operação Assistida` é momento, e
Osklen e Moda Objetiva são clientes tão reais quanto os dez `Ongoing`** — em outro ponto da linha.

> **Prova de que não é "estágio menor":** a **Osklen** tem **5 de 7 módulos contratados** — mais
> que 8 dos 10 `Ongoing` `[C]`.

### Eixo B — modo de atendimento
**`Sem CS` não é momento. É modo.** Um cliente `Sem CS` pode estar operando normalmente — só não
tem Customer Success dedicado.

### Eixo C — estado terminal
`Inativo` e `Churn` são fins, mas **de naturezas diferentes**: `Churn` é cliente que saiu;
`Inativo` inclui **linhas que nunca foram cliente**.

> 🔴 **Três linhas `Inativo` não são clientes:** `. Página Cliente [Template]`, `Fornecedores` e
> `uMode` (a própria casa) `[C]`. **Mais três stubs criados em 09/02/2026 e nunca editados:**
> `Agua de Coco`, `La Moda` — campos todos vazios, zero edições.
>
> **`Inativo` virou lixeira do campo.** Quem contar clientes por status conta errado.

---

## 3 · 🔴 O achado maior: `Sem CS` é um SKU, não um estado `[C]`

Os sete clientes `Sem CS` têm **exatamente o mesmo perfil**, sem exceção de campo:

| Campo | Valor, nos 7 |
|---|---|
| `Atendimento 2025` | **`SMB`** |
| `ERP/Integração` | **`Sem Integração`** |
| `Módulos Contratados` | **só `Gestão de Coleção`** |

**Camys · Cavallari · Mondepars · Studio Minah · TDC · Ton Age** — seis idênticos.

> 🔴 **E `SMB` não é uma pessoa.** É o nome de um **grupo de segmentação** (Grupo 3 da base
> `Segmentação Grupos`), colocado num campo que nos outros 39 clientes contém nome de gente
> (Julianne & Pedro, Laura, Fernanda).
>
> **Um segmento no campo de pessoa é a forma que a base encontrou de dizer "ninguém atende".**
> Para o modelo de pessoas isso importa: `Atendimento` precisa distinguir **pessoa** de
> **modo de cobertura**.

**A leitura correta:** `Sem CS` + `Sem Integração` + 1 módulo é um **produto self-service**.
Não é fase de jornada nem falha de atendimento — **é uma oferta.** `[P]`

### ⚠ E há exatamente uma exceção, que vale investigar
**A Baw** é `Sem CS` e **quebra o padrão em tudo** `[C]`:

| | Os 6 outros `Sem CS` | **Baw** |
|---|---|---|
| Atendimento | `SMB` | **`Laura`** — pessoa nomeada |
| Módulos | 1 | **4** (`Gestão de Coleção`, `Integração`, `Relatórios`, `Fornecedores`) |
| Chamados em jan/2026 | 0 | **8** |

> 🔴 **Um cliente com 4 módulos, atendimento nomeado e 8 chamados está classificado como
> "Sem CS".** **Ou o status está errado, ou a Baw é atendida sem que isso seja contabilizado.**
> `[D]` — **é pergunta para o negócio, e tem impacto em alocação.**
>
> ⚠ **E há uma contradição interna:** a Baw tem o módulo **`Integração`** contratado e o campo
> `ERP/Integração` diz **`Sem Integração`**. **Os dois não podem estar certos.**

---

## 4 · 🔴 Um coorte de churn que ninguém olhou junto `[C]`

Três clientes têm `Data Ativação Cliente` preenchida **e estão em `Churn`**:

| Cliente | Ativado em | Status hoje | ERP |
|---|---|---|---|
| **Lenny Niemeyer** | **03/02/2025** | `Churn` | Linx |
| **Recco** | **06/02/2025** | `Churn` | Totvs |
| **Highstil** | **11/02/2025** | `Churn` | Totvs |

**Três clientes ativados em oito dias, todos os três em churn.**

> 🔴 **Isso é um coorte, e ele falhou inteiro.** **Não afirmo a causa** — não li as páginas nem os
> contratos. Afirmo que **três ativações consecutivas de fevereiro de 2025 terminaram em saída**,
> e que **nenhuma fonte varrida registra o motivo de nenhuma delas.**
>
> **É a pergunta mais valiosa desta taxonomia:** o que aconteceu com o coorte de fev/2025?
>
> ⚠ **E há um detalhe que agrava:** a **Lenny Niemeyer abriu 5 chamados em janeiro de 2026** —
> **depois de constar como churn** `[C]`. **Status na base ≠ uso real da plataforma.**

**Mais dois casos de churn rápido:**
- **Phos** — linha criada em **30/01/2026**, `Churn` em **abril/2026**. **Menos de três meses.**
- **Plie** — criada em **11/04/2025**, `Churn`, atendimento **Laura**.

---

## 5 · O que isto muda no corpus e no banco

### No corpus, agora
1. **Todo cliente tem casa, qualquer que seja o status.** Um `Churn` guarda o histórico — e
   **histórico de cliente perdido é exatamente o que o BrainHub existe para não perder.**
2. **`Status` entra em `institucional.md` com a nota de que é momento, não tipo.**
3. **As três linhas que não são clientes** (template, `Fornecedores`, `uMode`) **não ganham casa
   de cliente.**

### No banco `[P]`
O campo único deve virar **três**, na `_espec-pessoas-e-comunicacoes.md` e na `ESPEC-BANCO-001`:

| Campo proposto | Valores | Natureza |
|---|---|---|
| `lifecycleStage` | `PROSPECT` · `ONBOARDING` · `ASSISTED` · `STEADY` · `CHURNED` | **momento**, com transição datada |
| `serviceMode` | `MANAGED_CS` · `SELF_SERVE` | **modo de atendimento** |
| `recordKind` | `CLIENT` · `INTERNAL` · `TEMPLATE` · `STUB` | **o que a linha é** |

> **E `lifecycleStage` precisa de histórico, não só de estado corrente** — pelo mesmo motivo que
> `person_memberships` precisa: **sem transição datada, não dá para perguntar "quanto tempo em
> onboarding?" nem "quando virou churn?"** — e a segunda pergunta é a que explica um coorte.

---

## 6 · O que decidir

1. 🔴 **O que aconteceu com o coorte de fev/2025** (Lenny Niemeyer, Recco, Highstil)? `[D]`
2. 🔴 **A Baw está classificada certo?** 4 módulos, atendimento nomeado, 8 chamados, `Sem CS`. `[D]`
3. **`Sem CS` vira `serviceMode` em vez de status?** `[D]`
4. **As 3 linhas não-cliente saem do campo `Status` ou ganham `recordKind`?** `[D]`
5. **Os stubs de 09/02/2026** (`Agua de Coco`, `La Moda`) **são clientes ou ruído?** `[D]`
6. **Clientes em `Churn` continuam abrindo chamado** — Lenny Niemeyer (5), Básico&Co (2),
   Paloma Concept, Susie Modas. **A base diz uma coisa e o uso diz outra.** `[D]`

## Fontes
| Bloco | Fonte | Data |
|---|---|---|
| Enum, distribuição, campos dos 7 `Sem CS`, coorte de fev/2025 | Notion — base `Mapa de Clientes`, 50 linhas | **varrida 22/09/2026** |
| `SMB` como grupo de segmentação | Notion — base `Segmentação Grupos` | varrida 21/09/2026 |
| Chamados de clientes em churn | Notion — `Chamados & Atendimentos` | varrido 21/09/2026 |

> 🔴 **CORREÇÃO — 22 set 2026.** Esta leitura de "coorte" era minha e estava errada no que
> sugeria. As três contas foram **ativadas** em oito dias, mas **não morreram juntas**:
> **Recco ~8 meses** (última atividade **16/10/2025**) · **Lenny Niemeyer ~14 meses**
> (**01/04/2026**) · **Highstil ~14 meses** (**16/04/2026**). Lenny e Highstil seguiram com
> reunião até **abril de 2026**, já marcadas como `Churn`. **É coorte de ativação, não de morte.**
> ⚠ **"Última atividade observada" não é data de saída** — a base **não tem `Data de Churn`**.
> Ver `_varredura-2026-09-22-reunioes-compartilhadas.md` § 4.


## Governança
### Quem decide
**Vinicius Risoléo.** A correção que originou este documento é dele.

### Quem pode alterar este documento
Vinicius Risoléo. **Este documento é a autoridade sobre o significado de `Status` de cliente** —
o que outros documentos disserem sobre isso fica `SUPERSEDED` por ele.
