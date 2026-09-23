---
aliases:
  - "Varredura 22 set 2026 (e) — o modelo de permissionamento e o perfil como área"
tags:
  - tipo/registro
  - casa
---
# Varredura 22 set 2026 (e) — o modelo de permissionamento e o perfil como área

> Instrução do Vinicius: *"Acessa tudo no Notion dentro dos clientes pra buscar informações."*
>
> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**

## 0 · Declaração de completude

| # | Lacuna | Situação |
|---|---|---|
| 1 | **Abri 5 páginas desta árvore** | `[NV] Permissionamento`, `CLIENTES`, `StudioZ`, `CAEDU`, e o índice. **As demais vêm de trecho de busca, não de leitura** |
| 2 | 🔴 **As 13 páginas de perfil da NV não foram abertas** | Tenho **os nomes**; **não tenho a matriz de permissão de nenhuma** |
| 3 | ⚠ **Os perfis dos outros 11 clientes vêm de `highlight` de busca** | **evidência mais fraca** — pode haver perfil que o trecho não mostrou |
| 4 | **A planilha de e-mail dos usuários** (citada na Moda Objetiva) | 🔴 **não aberta** — é o que ligaria pessoa → perfil → área |

## 1 · 🟢 O modelo de permissionamento da uMode está declarado, e é simples

**Texto literal da página `[NV] Permissionamento`:** `[C]`

> *"Na uMode, o permissionamento pode ser configurado de **duas formas**:*
> **Inclusão** *→ Quando a configuração determina tudo aquilo que o perfil* **pode** *fazer.*
> **Restrição** *→ Quando a configuração determina tudo aquilo que o perfil* **NÃO pode** *fazer."*

> 🟢 **É a primeira definição de modelo de permissão encontrada em qualquer fonte.** Duas
> estratégias — *allowlist* e *denylist* — **escolhidas por perfil.**
>
> 🔴 **E isso confronta direto o que o CX Hub faz:** lá o trigger `grant_new_client_to_all_users`
> dá `viewer` de tudo a todos — **é `Restrição` implícita e permissiva.** **Duas visões de
> permissionamento coexistindo**, uma documentada e outra implementada.

**A granularidade é por campo e por tela**, com três estados visuais que já apareceram nas
páginas de perfil: **🟢 visualizar e editar · 🟡 parcial · 🔴 não visualiza e não edita.**

## 2 · 🟢 O perfil de usuário É a área do cliente

**É a nona fonte distinta de vínculo pessoa↔área encontrada na carteira** — e a mais estruturada
de todas, porque **o perfil é o que o sistema realmente aplica.**

### 2.1 · NV — 13 perfis, lidos na página `[C]`

`NV - Geral` · `NV - Master` · `NV - Estilo` · `NV - Qualidade` · `NV - Planner` ·
`NV - Planner 2` · `NV - Compras` · `NV - Planejamento Comercial` · `NV - PCP` ·
`NV - Atacado` · `NV - Marketing` · `NV - View` · `NV - Logística`

> 🔴 **Quatro deles não são área, são nível de acesso:** `Geral`, `Master`, `View` e `Planner 2`.
> **O mesmo campo mistura área com privilégio** — mesmo defeito do `Status` de cliente.
> ⚠ **`Qualidade`, `Atacado` e `Logística` não têm área canônica na grade de 14.**

### 2.2 · Os demais — de trecho de busca, **não de leitura** ⚠

| Cliente | Perfis vistos no trecho |
|---|---|
| **VIX** | `Vix-Admin` · `Vix-CAD` · `Vix-Compras` · `Vix-Demo` · `Vix-Desenvolvimento` · `Vix-Estamparia` · `Vix-Estilo` · 🟢 **+ `uDash` como perfil à parte** |
| **Lofty Style** | `Lofty - Admin` · `Ficha Técnica` · `Compras Nacional` · `Compras Importado` · `Estilo` |
| **Cambos** | `Cambos - Admin` · `Comercial` · `Time Desenvolvimento` · `PCP/Compras` · `Consulta` |
| **Moda Objetiva** | `Objetiva - Admin` · `Estilo` · `Compras` · `Compras MP` · `Desenvolvimento` |
| **NK STORE** | `NK - Admin` · `NK - Time` · `NK - Estilo Master` · `NK Compras Master` |
| **Baw** | `Engenharia/Compras` · `Ecommerce/Logística` · `Marketing` · `Estilo` · `Comercial` |
| **Luiza Barcelos** | `LB - Admin` · `LB - Time` |
| **Lenny Niemeyer** | `LN - Admin` · … |
| **Oficina Reserva** | `Oficina - …` — com nota: *"provavelmente no novo formato não teremos mais o perfil de compras"* |
| **Recco** | `Admin` · `Time` · … |

**Também têm página de permissionamento:** Reserva (`Permissões`) e o índice do CX Hub.
**Total: 12 clientes com permissionamento documentado.**

### 2.3 · 🔴 A convenção de nome do perfil é de cada cliente

`NV - Estilo` · `Vix-Estilo` · `Lofty - Estilo` · `Objetiva - Estilo` · `NK - Estilo Master` ·
e a **Baw sem prefixo nenhum**: `Estilo`.

> **Confirma o achado da Puket** (a convenção é do cliente, não nossa). **Cinco grafias para a
> mesma área.** **Para o banco, `profile.name` não é chave de área** — precisa de um campo
> `area_id` normalizado.

## 3 · 🔴 Uma árvore de documentação que o corpus nunca mencionou

**`uMode Geral / uFlow / Documentação de Setup - PLM / CLIENTES (Em desenvolvimento)`**

**Nove clientes têm pasta:** NV · RESERVA · BAW · OFICINA · VIX · **StudioZ** · PUKET ·
**CAEDU** · NK Store.

⚠ **Mas a árvore é quase toda esqueleto.** Verificado abrindo: `[C]`

| Cliente | Conteúdo real |
|---|---|
| **NV** | 🟢 **13 páginas de perfil** + a definição do modelo |
| **RESERVA** | 🟢 `CENTRAL DE DOCUMENTAÇÕES` com `Permissões` e `Trava de Ficha` |
| **StudioZ** | ⚠ **uma sub-página só** (`Studioz - Fornecedores`) |
| **CAEDU** | 🔴 **vazia** |
| Os outros 5 | ⚠ **não abertos** |

> 🔴 **A CAEDU — a conta da próxima frente — tem pasta de setup e ela está vazia.**
> **Registro o fato, não a causa.**

## 4 · 🟢 Uma pessoa com área, achada de raspão na Reserva

A página `✍🏻 Trava de Ficha` (Reserva) traz:
> *"**Vanessa Sousa e Karine Pires**) (**time de Cadastro**) tem acesso para editar/incluir
> Variantes (incluindo os campos NCM e COMPOSIÇÃO)"*

🟢 **São as duas únicas pessoas da carteira com nome + área + permissão explícita, numa frase.**
E **batem com os e-mails da base de chamados** — `vanessa.sousa@usereserva.com` e
`karine.pires@usereserva.com`. **Primeira conciliação completa pessoa ↔ e-mail ↔ área ↔ permissão.**

> ⚠ **E `karine.pires@usereserva.com` aparecia na base de chamados sob Oficina Reserva.**
> Com esta página, **ela é da Reserva** — o registro `d` havia marcado como possível erro.
> **Continua sem confirmação definitiva**, mas o peso mudou.

## 5 · O que isso muda na pergunta de cargo e área

**A lacuna nº 5 do painel de prontidão não está fechada, mas está reformulada:** `[P]`

| | Antes | Agora |
|---|---|---|
| **Cargo** | 🔴 sem fonte | 🔴 **continua sem fonte em nenhuma das 8 varridas** |
| **Área** | 🔴 sem fonte | 🟡 **existe via PERFIL, em 12 clientes** — mas **não ligada à pessoa** |

> 🔴 **O elo que falta é a atribuição perfil↔pessoa.** A Moda Objetiva cita uma
> *"Planilha de e-mail dos usuários"* — **não aberta.** **Se ela ligar e-mail a perfil, a
> corrente fecha:** `pessoa (e-mail) → perfil → área → permissão`.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| §1, §2.1 | Notion — `[NV] Permissionamento`, **página aberta** | **22 set 2026** |
| §2.2 | Notion — **trechos de busca**, ⚠ não leitura de página | **22 set 2026** |
| §3 | Notion — `CLIENTES (Em desenvolvimento)`, `StudioZ`, `CAEDU`, **abertas** | **22 set 2026** |
| §4 | Notion — `✍🏻 Trava de Ficha` (trecho) + base de chamados | **22 set 2026** |
