---
aliases:
  - "Varredura 23 set 2026 (c) — o índice técnico do uFlow, e uma página chamada `Credenciais`"
tags:
  - tipo/registro
  - casa
---
# Varredura 23 set 2026 (c) — o índice técnico do uFlow, e uma página chamada `Credenciais`

> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**
>
> Veio de abrir `uMode Geral / uFlow / Documentação de Setup - PLM` (`b6f89329…`) e a sua
> sub-página `📑 CLIENTES (Em desenvolvimento)` (`bf9891a8…`).
>
> **Este registro é um MAPA, não uma leitura.** Li dois índices. **As ~70 páginas listadas
> aqui continuam fechadas.**

## 0 · 🚨 O primeiro item é de segurança

> 🔴 **Há uma página chamada `Credenciais` neste acervo**, na seção `Nova uFlow/uRocket`
> (`c422e214…`). `[C]`

**Eu não a abri, e a decisão é deliberada.** O título já é suficiente para registrar o risco;
abrir traria segredo para dentro do contexto e do histórico desta sessão **sem acrescentar
nada à ação que precisa acontecer**, que é sua.

| | NK STORE | Lofty Style | **esta** |
|---|---|---|---|
| O que é | credencial de produção do Linx | credencial do site de documentação | 🔴 **não sei, e não vou olhar** |
| De quem | de um cliente | de um cliente | 🔴 **da própria plataforma** |
| Estado | 🚨 exposta, não rotacionada | 🚨 exposta, não rotacionada | 🚨 **a verificar** |

⚠ **As duas primeiras eu achei sem querer, varrendo página de cliente. Esta estava no índice
técnico, com o nome na porta.**

## 1 · O acervo, em números

| | |
|---|---|
| Seções | **14** |
| Páginas listadas | **~70** |
| Páginas que eu abri | **1** — o `📕 Manual do Permissionamento`, antes deste registro |
| Última edição do índice | **29/10/2025** |

## 2 · 🟢 Aqui está o catálogo de automações que eu procurava

O playbook da Cambos citava `#1136`, `#1175`, `#1134`, `#989` e `#1135` **sem dizer onde essas
automações vivem.** A seção `👩🏾‍💻 Automações` tem oito páginas:

| Página | Por que importa |
|---|---|
| `Aprovação` | |
| `Calculadora de campos` | 🆕 **há cálculo de campo na plataforma** |
| `Gerador de Referencia` | 🟢 **é provavelmente o `#1136` da Cambos** — descrição concatenada |
| `Ação de destruir Materiais` | |
| `Habilitar mover card para etapa anterior` | ⚠ **workflow com volta, não só avanço** |
| `Ações com mais de uma expression` | 🆕 **`expression` — a linguagem de regra tem nome** |
| 🔴 **`Projeto Puket - Kanban de Estilo NOVO`** | **automação feita para UM cliente, com nome de projeto** |
| `Criar fornecedor no produto ao entrar em etapa do workflow` | 🟢 **gatilho por etapa** — mesma família do `#1175` |

⚠ **Nenhuma aberta.** **Não afirmo que o `#1136` é o `Gerador de Referencia`** — é o palpite
mais óbvio, e palpite óbvio já me enganou antes.

## 3 · 🔴 Cada `entity_config` tem página, e duas são NOMINAIS de cliente

O `Manual do Permissionamento` lista 20 configs **como exemplo**. Aqui elas aparecem como
páginas, na seção `🧾 Configs da Conta` — **18 delas**, e duas trazem o cliente no título:

| Página | Leitura |
|---|---|
| 🔴 **`[Vivara] Alterar nomes tecido/aviamento`** | **a Vivara é cliente da carteira.** É o **apelido interno** de novo — agora com config, título e documentação própria |
| 🔴 **`[NV] Bloquear Alteração de Elementos da Tabela na FT`** | trava de edição feita para a NV |

**As outras:** `Preview da impressão do mapa` · `Bloquear alteração de checklist` · `Separar
preço da exportação de fabricantes` · `Bloquear alteração de status` · `Padronizar valor de
moeda` · **`Habilitar Usuários específicos a gravar tabela de medida`** · `Colunas
Personalizadas - Tabela de Medidas` · `Bloqueio de duplicação de campos` · `Ocultar Colunas com
ponto "." no nome` · `Criação de EAN` · `Alterações de informações do Produto ao duplicar` ·
`Exibição no Mapa de Coleção - salvar filtros` · **`Inativação de Variantes`** · `Edição em
Massa` · `Edição da tabela de medidas com produtos associados` · `Configs da Conta` ·
`Impressão do mapa` · **`Ocultar botão de 'Exibições' do mapa de coleção`** ·
**`Fornecedor visualizar produto com algumas especificidades`** · `[BETA] Alterar empenho de
materiais em massa`.

> 🟢 **`Habilitar Usuários específicos a gravar tabela de medida` é o `scopable: user` outra
> vez** — a permissão nominal da Lofty Style tem, aqui, uma página de procedimento.

> 🟢 **`Ocultar botão de 'Exibições'` é o `hide_map_template`**, que explica o
> `Mapa de Coleção > Exibições` bloqueado na Recco e a regra do playbook da Cambos.

🆕 **`[BETA]`** — **há funcionalidade em beta, e o corpus não tinha esse estado.**

## 4 · 🟢 A cadeia do "apelido interno" está completa

| Camada | Onde |
|---|---|
| **Princípio** | Arquitetura V1, princípio nº 1 — o termo do cliente na frente, o canônico entre parênteses |
| **Evidência** | abas em caixa alta da Cambos · `Fabricantes` na Recco · `Chat NK`/`Chat NV` · campos `Referência NV` |
| **Mecanismo** | `model_name_brand` · `model_name_collection` · `model_name_theme` · `model_name_batch` |
| 🆕 **Procedimento** | seção **`Traduções`**: `Abas e nomes de campos da Ficha técnica` · `Campos Custom` · `Impressão` · **`Nomes de Modelos`** |
| 🆕 **Caso com nome** | `[Vivara] Alterar nomes tecido/aviamento` |

> 🟢 **É a primeira cadeia completa do corpus: princípio → evidência → mecanismo → procedimento
> → caso.** ⚠ **As quatro páginas de `Traduções` não foram abertas.**

## 5 · 🔴 O processo de integração está escrito, e ninguém tinha apontado onde

| Página | |
|---|---|
| **`Como é o processo de integração?`** | `e6ca5775…` |
| **`Logs e integração (Google Cloud Watch)`** | `eb6f3a42…` |

⚠ **A dor de integração atravessa CAEDU (três ciclos), VIX (DE/PARA campo a campo), Moda
Objetiva (`Dossiê Acompanhamento`) e Luiza Barcelos.** **O processo existe em duas páginas que
nenhum documento do corpus citava.** 🔴 **Não abertas.**

## 6 · 🆕 Três ferramentas que o corpus não tinha

| Ferramenta | Onde apareceu |
|---|---|
| **`BigQuery`** | `Utilização do BigQuery para consulta no banco` · `[Blazzer] Realizando consultas pelo BigQuery` · `Big Query` em `Nova uFlow/uRocket` |
| **`Blazzer`** | ⚠ **grafia da fonte.** O produto conhecido chama-se **`Blazer`** — não corrigi a fonte, registro a divergência |
| **`MongoDB Compass`** | `MongoDB Compass (Aggregations)`, em `Documentação DEV` |

> ⚠ **Mongo no acervo do uFlow é estranho.** O Mongo do corpus é o do **BrainHub**; o uFlow é
> Rails, com `jumper_*` e `J3`. **Ou há Mongo no uFlow, ou esta página fala de outro sistema.**
> **Não concluo — nomeio a estranheza.**

## 7 · O resto do índice, para quem for varrer depois

| Seção | Páginas |
|---|---|
| **Templates de Formulário** | 🔴 **`Ficha de Produto`** (`c3deb3dd…`, com 7 sub-páginas de permissionamento) · `Ficha de Impressão` |
| **Manual do Permissionamento** | 🟢 **LIDO** · ⚠ **e um PDF anexado, `manual_do_permissionamento_umode_(5).pdf`, versão 5 — não lido** |
| **Validação** | `Condição para Validação aparecer apenas para campos específicos` |
| **Checklists** | 6 páginas, incluindo `Checklist - Permissionamento` e `Campos Custom Checklist` |
| **Menus Personalizados** | `Associar usuário na uDash` · `Habilitar relatórios para perfil` · **`Habilitar relatórios para usuário`** · `Manual de Permissões - Aba de Cadastros` |
| **Mapa de Coleção** | `Permissionamento` |
| **Perfis - Permissionamento** | `f5d6395f…` |
| **Usuários** | `Desativação de usuário` |
| **Importação** | ⚠ **página VAZIA** — o Notion devolve *"este documento não tem conteúdo"* |
| **Campo custom para materiais** | `Processo para criação` |
| **Documentação DEV** | `Códigos` · `Traduções yml` · `Habilitar/Desabilitar edição no mapa de coleção` · `MongoDB Compass (Aggregations)` |
| **Relatórios** | 4 páginas · 🆕 **`[uDash] Configuração Relatórios da Coleção`** |
| **Deploys / Integrações** | `Deploy` · as duas de integração do § 5 |
| **E-mails Automatizados** | `Automatização de Emails` — ⚠ **o corpus tem 92 e-mails e nenhum modelo** |
| **Tabela de Medidas customizada** | `Comportamento ao duplicar produto` |
| **Material de estudos** | `30eb7fb6…` |
| **Nova uFlow/uRocket** | 🚨 **`Credenciais`** · `Big Query` |
| **Estudo de caso** | 🆕 `Estudo de caso do Card 17680` — **`Card` com ID de 5 dígitos, de sistema que não sei qual** |

## 8 · 🔴 O acervo por cliente tem NOVE clientes, e eu tinha tocado um

`📑 CLIENTES (Em desenvolvimento)` — **última edição 16/07/2025, mais de um ano.** `[C]`

| Cliente | Estado da minha varredura |
|---|---|
| **NV** | 🟢 página-mãe e `NV - Geral` lidas · ⚠ **12 sub-páginas de perfil fechadas** |
| RESERVA · BAW · OFICINA · VIX · **StudioZ** · PUKET · CAEDU · **NK Store** | 🔴 **nenhuma aberta** |

🆕 **`StudioZ`** — a pasta do corpus é `Studio Z`. ⚠ **Grafia diferente; não fundi.**

> 🔴 **Oito clientes com documentação de setup que ninguém leu.** E a NK STORE e a VIX, que eu
> considerava bem varridas, **têm um segundo endereço que eu não tinha aberto.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §0–§7 | Notion — `uMode Geral / uFlow / Documentação de Setup - PLM` (`b6f89329…`), **índice lido por inteiro; as páginas filhas NÃO** | **23 set 2026** |
| §8 | Notion — `📑 CLIENTES (Em desenvolvimento)` (`bf9891a8…`), **lida por inteiro** | **23 set 2026** |
| §3, §4 | cruzamento com [`_dicionario-permissionamento-uflow.md`](_dicionario-permissionamento-uflow.md) | **23 set 2026** |
