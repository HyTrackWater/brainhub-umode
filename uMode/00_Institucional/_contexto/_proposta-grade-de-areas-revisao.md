# PROPOSTA — revisão da grade de áreas canônicas de cliente

> Escrita em **21 set 2026** por Vinicius Risoléo (com Claude Code) e **revisada em 22 set 2026**,
> a partir da varredura ao vivo do Notion em **10 clientes** — **todos os `Ongoing`**:
> Caedu, Puket, Reserva, NV, NK STORE, VIX, Lofty Style, Cambos, Oficina Reserva e Luiza Barcelos.
>
> 🔴 **A revisão de 22/09 fortaleceu a proposta e mudou uma recomendação.** Ver §7.
>
> **Isto é proposta, não decisão.** A grade de 14 áreas está travada no `CONTEXT.md`, e o
> `CLAUDE.md` proíbe alterá-lo sem confirmação explícita. **Nada foi alterado.** Este documento
> existe para que a decisão seja tomada com a evidência na mesa.

**Grau por afirmação:** `[C]` verificado na fonte viva, com a fonte citada · `[P]` proposta ·
`[D]` decisão que não é minha.

---

## 0 · Declaração de completude

| # | O que esta proposta NÃO resolve | Por quê |
|---|---|---|
| 1 | **A evidência vem de 10 de 46 clientes.** | Os 10 são **todos os `Ongoing`** — a carteira viva. Os outros 36 (Churn, Sem CS, Inativo, Pré-Onboarding) **não foram varridos**. |
| 2 | **Não sei o custo de mexer na grade.** | 46 clientes × 14 pastas já existem no corpus. A migração é trabalho real e não foi dimensionada. |
| 3 | **Não li o `uFlow` nem o schema de `areas`.** | A grade também vive em código. Mudança aqui pode exigir mudança lá. |
| 4 | **Não consultei o João.** | A hierarquia é decisão conjunta registrada no `CONTEXT.md`. |

---

## 1 · O achado: três clientes, três nomes, a mesma lacuna `[C]`

> ⚠ **SUPERSEDED pela §7 (22 set 2026).** Esta seção foi escrita com **6 clientes** e a §7 refaz a conta com **10**. **Leia a §7 antes de agir por esta.**


A grade canônica tem 14 áreas. **Nenhuma delas cobre produção própria.**

| Cliente | Nome na origem | Onde aparece |
|---|---|---|
| **NV** | **`Atelier`** | campo *"Departamentos engajados"* do template de transição, preenchido pelo cliente |
| **NK STORE** | **`Oficina`** | desenho de processo na página: `Planejamento → Estilo → Compras/Merchandising → PCP → Oficina` |
| **VIX** | **`Vix-Estamparia`** | perfil de acesso no PLM, entre os 17 da conta |

**Três clientes independentes, três fontes diferentes, o mesmo buraco.**

O critério que venho usando nesta varredura — **um caso é anedota, dois é hipótese, três é
padrão** — foi atingido.

### Por que as áreas existentes não servem
- **`13_Modelagem`** é desenvolvimento de molde, não produção de peça.
- **`14_Engenharia`** é engenharia de produto (ficha técnica, consumo), não chão de fábrica.
- **`05_PCP`** *planeja e controla* a produção — não a executa. Na NK, `PCP` e `Oficina` aparecem
  como **etapas distintas e sequenciais** no mesmo fluxo `[C]`.

> **Forçar `Atelier` em `13_Modelagem` destruiria a informação.** Foi por isso que deixei
> `[a preencher]` nos três casos em vez de encaixar.

## 2 · Proposta A — criar `15_Producao-Interna` `[P]`

**Nome proposto:** `15_Producao-Interna`
**Aliases esperados:** `Atelier` · `Oficina` · `Estamparia` · `Facção interna` · `Piloto`

**O que ela é:** a área que **transforma material em peça dentro da casa do cliente**, distinta de
quem planeja (`05_PCP`), de quem desenha o molde (`13_Modelagem`) e de quem especifica
(`14_Engenharia`).

**Custo:** 46 clientes ganham uma pasta nova com `contexto-area.md` de ausência declarada.
Pelo padrão já aplicado nesta varredura, **isso é ganho, não custo** — *lacuna visível vale mais
que cobertura aparente*. Mas **são 46 arquivos novos e a decisão é sua `[D]`.**

### Contraproposta B — manter 14 e usar Subárea `[P]`
`Atelier`, `Oficina` e `Estamparia` entrariam como **Subárea (nível 3)** sob `05_PCP`.

**A favor:** não mexe na grade; o nível 3 já aceita nomes livres.
**Contra:** na NK, `PCP` e `Oficina` são **etapas distintas do mesmo fluxo** `[C]` — pendurar uma
na outra afirma uma hierarquia que a fonte não mostra. E o brain responderia errado a
*"quem produz?"*.

> **Minha recomendação é a Proposta A**, porque a evidência mostra produção como etapa própria,
> não como subordinada ao planejamento. **Mas a decisão é sua.**

---

## 3 · O segundo achado: Subárea não é hipótese, já existe no dado `[C]`

A hierarquia do `CONTEXT.md` prevê **nível 3 — Subáreas, nomes livres**. A VIX mostra esse nível
**já implementado, no perfil de acesso do PLM**:

| Perfil na VIX | Subárea que ele declara |
|---|---|
| `Vix-Estilo Biquini` | linha **Biquíni** |
| `Vix-Estilo Cover ups` | linha **Saídas de praia** |
| `Vix-Estilo Roupas` | linha **Roupas** |
| `Vix-Estilo PA` | **Produto Acabado** |
| `Vix- Estilo Admim` | administração de Estilo |

**Cinco perfis, uma área canônica (`02_Estilo-Criacao`), quatro linhas de produto.**

> **Isto não pede mudança na grade — pede mudança no modelo de dados.**
> O mapeamento perfil → área precisa de **dois campos**, não um:
> `areaId` **e** `subAreaLabel`.
>
> Já registrado como item na
> [`_espec-pessoas-e-comunicacoes.md`](_espec-pessoas-e-comunicacoes.md) §3.2. **Sem isso, a
> tradução `Vix-Estilo Biquini → 02_Estilo-Criacao` perde a informação que mais importa.**

---

## 4 · O terceiro achado: nomes que não resolvem, e que não inventei `[C]`

> ⚠ **SUPERSEDED pela §7 (22 set 2026).** Esta seção foi escrita com **6 clientes** e a §7 refaz a conta com **10**. **Leia a §7 antes de agir por esta.**


Seis rótulos de área apareceram na varredura **sem correspondência clara**, e ficaram
`[a preencher]` em vez de virar palpite:

| Rótulo | Cliente | Por que não resolvi |
|---|---|---|
| `Merchandising` | NK STORE · Reserva | Na NK, a Diretora de Merchandising responde por **Compras, Industrial e Compliance** — três áreas canônicas diferentes |
| `Planejamento Comercial` | NV | O nome junta `01_Planejamento` e `09_Comercial-Vendas` |
| `Curadoria` | NK STORE | Compra de produto acabado de marca parceira — ramo próprio no fluxo |
| `TEX` | Puket | **Sigla não explicada em nenhuma fonte** |
| `Vix-Produto TP` | VIX | **`TP` não explicado em nenhuma fonte** |
| `Vix-Ficha Tecnica` | VIX | `03_Desenvolvimento-de-Colecao` ou `14_Engenharia`? |

> ⚠ **CORRIGIDO na §7.2:** `Merchandising` chegou a **três clientes** (NK STORE, Reserva,
> **Luiza Barcelos**) e o limiar foi atingido. **Mas a recomendação mudou para NÃO criar área**,
> porque os três escopos são diferentes. **Ver §7.2.**

---

## 5 · O que a grade acertou `[C]`

> ⚠ **SUPERSEDED pela §7 (22 set 2026).** Esta seção foi escrita com **6 clientes** e a §7 refaz a conta com **10**. **Leia a §7 antes de agir por esta.**


Vale registrar o que **não** precisa mudar. Estas áreas apareceram com correspondência direta e
sem ambiguidade em múltiplos clientes:

`02_Estilo-Criacao` · `03_Desenvolvimento-de-Colecao` · `04_Qualidade` · `05_PCP` ·
`06_Compras-Supply-Sourcing` · `13_Modelagem`

**A grade está certa no núcleo.** O problema é na borda da produção e nas funções compostas.

### Cobertura observada, cliente a cliente
| Área canônica | Caedu | Puket | Reserva | NV | NK | VIX |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `01_Planejamento` | ✅ | — | — | ⚠ | ⚠ | — |
| `02_Estilo-Criacao` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `03_Desenvolvimento-de-Colecao` | ✅ | ✅ | ✅ | — | — | ✅ |
| `04_Qualidade` | ✅ | ✅ | — | — | — | ✅ |
| `05_PCP` | — | ✅ | — | ✅ | ✅ | ✅ |
| `06_Compras-Supply-Sourcing` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `07_Logistica-CD` | — | — | — | ✅ | — | — |
| `08_Ecommerce-Cadastro` | ✅ | — | ✅ | ✅ | — | — |
| `09_Comercial-Vendas` | — | — | — | ✅ | — | — |
| `10_Marketing` | — | — | — | ✅ | — | — |
| `11_Financeiro` | — | ✅ | — | — | ✅ | — |
| `12_Design` | — | ✅ | — | — | — | — |
| `13_Modelagem` | ✅ | — | — | — | ✅ | ✅ |
| `14_Engenharia` | — | — | ✅ | ✅ | — | — |
| 🔴 **produção interna** | — | — | — | **✅** | **✅** | **✅** |

⚠ **A tabela acima cobre 6 clientes. A §7.6 tem a de 10** — use aquela.

---

## 6 · O que decidir

> ⚠ **SUPERSEDED pela §7 (22 set 2026).** Esta seção foi escrita com **6 clientes** e a §7 refaz a conta com **10**. **Leia a §7 antes de agir por esta.**


1. **Criar `15_Producao-Interna`?** `[D]` — Proposta A, recomendada. Afeta 46 clientes e o
   `CONTEXT.md`.
2. **Adicionar `subAreaLabel` ao modelo de vínculo pessoa↔área?** `[D]` — a VIX prova que a
   informação existe e se perde sem ele.
3. **`Merchandising` vira área canônica?** `[D]` — **aguardar mais um caso**, por disciplina.
4. **`12_Design` se sustenta?** `[D]` — reavaliar ao fim da varredura, com os 46.

## Fontes
| Bloco | Fonte | Data |
|---|---|---|
| `Atelier` | Notion — template de transição na página `NV` | varrido 21/09/2026 |
| `Oficina` | Notion — desenho de processo na página `NK STORE` | varrido 21/09/2026 |
| `Vix-Estamparia` e as 4 linhas de Estilo | Notion — *[Vix] Perfil de Usuário e Permissionamento* | varrida 21/09/2026 |
| `Merchandising` | Notion — páginas `NK STORE` e `Reserva` | varrido 21/09/2026 |
| Cobertura por cliente | os 6 `institucional.md` escritos nesta varredura | 21/09/2026 |

## Governança
### Quem decide
**Vinicius Risoléo**, com o João quando a decisão tocar a hierarquia travada no `CONTEXT.md`.

### Quem pode alterar este documento
Vinicius Risoléo. **Enquanto for proposta, permanece proposta** — se e quando for decidida, a
decisão vai para o `CONTEXT.md` e este documento é marcado `SUPERSEDED` apontando para lá.

---

## 7 · REVISÃO de 22 set 2026 — os 4 clientes restantes confirmaram e ampliaram

Com **Lofty Style, Cambos, Oficina Reserva e Luiza Barcelos**, fecha-se **10 de 10 `Ongoing`**.

### 7.1 · Produção interna chegou a **quatro** clientes `[C]`

| Cliente | Nome na origem | Fonte |
|---|---|---|
| NV | `Atelier` | template de transição preenchido pelo cliente |
| NK STORE | `Oficina` | desenho de processo na página |
| VIX | `Vix-Estamparia` | perfil de acesso no PLM |
| **Cambos** | **`Pilotagem`** | **bloco *Times Envolvidos*, na fábrica de MG** |

**Quatro clientes, quatro tipos de fonte, quatro nomes, a mesma lacuna.**
**A Proposta A — criar `15_Producao-Interna` — sai de "recomendada" para "sustentada".**

### 7.2 · 🔴 `Merchandising` atingiu três — e por isso mudo a recomendação

A versão de 21/09 dizia: *"aparece em dois clientes... **não proponho ainda**"*. **O terceiro chegou.**

| Cliente | Como aparece |
|---|---|
| **NK STORE** | **Diretora de Merchandising** respondendo por **Compras, Industrial e Compliance** |
| **Reserva** | `Merchan` no *"Comitê uMode <> Reserva"* |
| **Luiza Barcelos** | time **`Produto e Merchandising`** — e **o Líder Central do Projeto é Coordenador de Merchandising** |

> **Mas os três escopos são diferentes.** Na NK cobre Compras+Industrial+Compliance; na Luiza
> Barcelos vem colado a Produto; na Reserva é só um nome em grupo.
> **`Merchandising` em moda é cargo de escopo variável, não função estável.**
>
> **`[P]` Recomendo NÃO criar área canônica para Merchandising** — tratá-lo como **Subárea** ou
> **papel que atravessa áreas**. **Criar área para um nome que significa três coisas é pior que
> deixar `[a preencher]`.** `[D]`

### 7.3 · Subárea tem **dois** eixos, não um `[C]`

| Cliente | Eixo | Exemplo |
|---|---|---|
| **VIX** | **linha de produto** | `Vix-Estilo Biquini` · `Cover ups` · `Roupas` · `PA` |
| **Cambos** | **local** | Desenvolvimento **MG** (Modelagem e Pilotagem) × **SP** (Pesquisa e Criação) |

> **`subAreaLabel` precisa de um companheiro `subAreaKind`** (`PRODUCT_LINE` · `LOCATION` ·
> `OTHER`). Item para a [`_espec-pessoas-e-comunicacoes.md`](_espec-pessoas-e-comunicacoes.md) §3.2.

### 7.4 · Dois rótulos novos sem área, ambos da Luiza Barcelos `[C]`

| Rótulo | Onde | Por que não resolvi |
|---|---|---|
| **`Precificação`** | sub-time de `Operações` | Em moda costuma ser comercial ou merchandising, **não financeiro**. **Um caso só — anedóta.** |
| **`Estratégia, Processos e Projetos`** | time próprio | É **transversal**, como `Projetos` no Puket e `BI` na NK. **Não é área, é função de governança.** |

### 7.5 · Uma pessoa pode cobrir meia cadeia `[C]`

Na **Luiza Barcelos**, o **Gerente de Operação do Sul** tem escopo declarado:
> *"**Logística e Cadastro** — **Desenvolvimento até a Precificação** está no guarda-chuva dele."*

**Quatro áreas numa pessoa.** **`person_memberships` tem que aceitar N áreas** — já estava
implícito, **agora tem caso com nome e cargo.**

### 7.6 · Cobertura nos 10 `Ongoing`

| Área canônica | Cae | Puk | Res | NV | NK | VIX | Lof | Cam | Ofi | LB | **Total** |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `01_Planejamento` | ✅ | — | — | ⚠ | ⚠ | — | ✅ | — | — | — | **4** |
| `02_Estilo-Criacao` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | **9** |
| `03_Desenvolvimento-de-Colecao` | ✅ | ✅ | ✅ | — | — | ✅ | — | ⚠ | — | ✅ | **6** |
| `04_Qualidade` | ✅ | ✅ | — | — | — | ✅ | — | — | ✅ | — | **4** |
| `05_PCP` | — | ✅ | — | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | **6** |
| `06_Compras-Supply-Sourcing` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **10** |
| `07_Logistica-CD` | — | — | — | ✅ | — | — | — | — | — | ⚠ | **2** |
| `08_Ecommerce-Cadastro` | ✅ | — | ✅ | ✅ | — | — | — | — | ✅ | ✅ | **5** |
| `09_Comercial-Vendas` | — | — | — | ✅ | — | — | — | ✅ | — | — | **2** |
| `10_Marketing` | — | — | — | ✅ | — | — | — | — | — | — | **1** |
| `11_Financeiro` | — | ✅ | — | — | ✅ | — | — | ✅ | — | ✅ | **4** |
| `12_Design` | — | ✅ | — | — | — | — | — | — | — | — | **1** |
| `13_Modelagem` | ✅ | — | — | — | ✅ | ✅ | ✅ | ✅ | — | — | **5** |
| `14_Engenharia` | — | — | ✅ | ✅ | — | — | — | — | — | — | **2** |
| 🔴 **produção interna** | — | — | — | ✅ | ✅ | ✅ | — | ✅ | — | — | **4** |

**Leitura:**
- 🟢 **`06_Compras-Supply-Sourcing` em 10 de 10.** A única universal.
- 🟢 **`02_Estilo-Criacao` em 9 de 10.** Núcleo duro com Compras.
- 🔴 **`10_Marketing` e `12_Design` em 1 de 10 cada** — **menos que a produção interna, que
  aparece em 4 e não existe na grade.**
  > **Isso inverte o argumento:** a grade **tem** área canônica para o que aparece uma vez e
  > **não tem** para o que aparece quatro.
- ⚠ `07_Logistica-CD`, `09_Comercial-Vendas` e `14_Engenharia` em **2 de 10**.

### 7.7 · O que decidir — lista atualizada
1. 🔴 **Criar `15_Producao-Interna`?** `[D]` — **4 casos.** **Recomendado.**
2. 🔴 **`12_Design` e `10_Marketing` se sustentam?** `[D]` — **1 caso cada.**
   **A pergunta agora é se sobra área, não só se falta.**
3. **`Merchandising`** — **`[P]` recomendo NÃO criar área**, por escopo variável. `[D]`
4. **`subAreaKind`** (`PRODUCT_LINE` · `LOCATION`) no modelo de vínculo. `[D]`
5. **`person_memberships` com N áreas por pessoa** — caso concreto na Luiza Barcelos. `[D]`
6. **`Precificação`** — **aguardar segundo caso.** 1 de 10.
