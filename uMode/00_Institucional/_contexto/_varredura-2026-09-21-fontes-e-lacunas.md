---
aliases:
  - "Varredura 21 set 2026 — fontes rastreadas e o mapa de lacunas de todos os clientes"
tags:
  - tipo/registro
  - casa
---
# Varredura 21 set 2026 — fontes rastreadas e o mapa de lacunas de todos os clientes

> Varredura geral a pedido do Vinicius: **todo e qualquer cliente**, não só a CAEDU.
> **Somente leitura em todas as fontes.** Nenhum commit, push ou checkout fora do
> `HyTrackWater/brainhub-umode`.
>
> **Aliases:** **corpus** = `HyTrackWater/brainhub-umode` · **vault** = `HyTrackWater/umode-os-vault`
> · **api** = `UmodeApp/umode-brainhub-api` · **front** = `UmodeApp/umode-brainhub` · **uflow** =
> `UmodeApp/umode-flow` · **cx-hub** = `HyTrackWater/gist-sparkle-d86e356b` · **legado** =
> `HyTrackWater/design-system-hub`.

## 0 · Declaração de completude — o que esta varredura NÃO alcançou

| # | Fonte | Situação | Consequência |
|---|---|---|---|
| 1 | **Dados do cx-hub** | 🔴 **travada** — o repositório tem o *schema* (114 objetos), os **registros vivem no Supabase** | Vejo a estrutura de pessoas, times e demandas; **não vejo as pessoas** |
| 2 | **Dados do legado** | 🔴 **travada** — mesmo caso: Supabase dentro do Lovable Cloud | ~30 tabelas conhecidas por nome, sem registro |
| 3 | **Notion ao vivo** | ⚠ não acessado — usei os **exports versionados no vault** | O export do Mapa é de **04/03/2026**; pode haver deriva |
| 4 | **uFlow — dados de conta** | ⚠ só o código | 43 chaves de config lidas; **quais contas usam quais, não** |
| 5 | **Drive de operação** | ⚠ não varrido | 29 dos 49 clientes têm link de Drive no Mapa |
| 6 | **Moda Objetiva — doc da integração** | ⚠ **acesso ainda não concedido** | repo de documentação pendente com o desenvolvedor |

## 1 · As fontes efetivamente rastreadas

| # | Fonte | Caminho / ref | O que rendeu |
|---|---|---|---|
| 1 | **corpus** | `main` @ `9ef6be4` | 46 clientes · 1.229 MDs · estado de preenchimento |
| 2 | **vault — pastas de cliente** | `governance/brainhub-v1.5` | **62 pastas**, 64 notas-hub (96 KB) |
| 3 | **vault — índice de clientes** | `_Clientes/_Clientes.md` | 294 linhas, folder-note recursiva |
| 4 | **vault — Notion: Mapa de Clientes** | `_Clientes/_geral/notion/Mapa de Clientes.csv` | **49 clientes × 48 colunas** |
| 5 | **vault — Notion: Demandas** | `_Clientes/_geral/notion/Demandas de Clientes.csv` | **836 linhas × 34 colunas** (393 KB) |
| 6 | **vault — Notion: Feedback** | `_Clientes/_geral/notion/Feedback Interno Clientes.csv` | 428 × 15 |
| 7 | **vault — Notion: Projetos** | `08_Operacoes/notion/Projetos.csv` | 36 × 27 (137 KB) |
| 8 | **vault — Notion: Assuntos** | `08_Operacoes/notion/AssuntosUMODE.csv` | 220 × 5 |
| 9 | **vault — Notion: uFlowDataBase** | `03_Produto-e-Solucoes/notion/uFlowDataBase.csv` | 234 × 6 |
| 10 | **vault — Notion: Backlog** | `03_Produto-e-Solucoes/notion/[Produto] Backlog Geral.csv` | 207 × 16 |
| 11 | **vault — resumos curados** | `01_Comercial/_contexto/notion-{mapa-clientes,demandas,feedback-clientes}.md` | leitura já destilada do funil |
| 12 | **vault — Notion por cliente** | `_Clientes/<slug>/notion/**` | FORMS, RFI Etapa 1/2, pesquisas de satisfação, perfis de permissionamento |
| 13 | **uflow** | `master` @ `84c35c19a` | **43 chaves de EntityConfig** |
| 14 | **cx-hub** | `main`, 636 arquivos | **114 objetos de schema** |
| 15 | **integrações** | 11 repositórios | cliente ↔ ERP confirmado |

## 2 · O universo de clientes — três rosters conciliados

| Roster | Quantos |
|---|---:|
| **corpus** (`uMode/_Clientes/`) | **46** |
| **vault** (`BrainHub/uMode/_Clientes/`) | **62** pastas (inclui pessoas, produtos e internos) |
| **Notion — Mapa de Clientes** | **49** registros |

### ✅ O corpus cobre 100% dos clientes reais
Dos 49 registros do Mapa, **46 estão no corpus**. Os 3 ausentes **não são clientes**:
`uMode` (registro interno), `. Página Cliente [Template]` e `Fornecedores` — todos `Inativo`.

### Distribuição por status do funil (Notion, n=49)
| Status | Qtd |
|---|---:|
| **Churn** | 16 |
| **Regime CS** | 11 |
| **Onboarding** | 9 |
| Inativo | 9 |
| Sem CS | 3 |
| Negociação | 1 |

> **21 clientes vivos** (Regime CS + Onboarding + Negociação) — **e todos os 21 já têm pasta no
> corpus.** É esse o alvo da missão.

## 3 · Os 21 clientes vivos, com módulo e ERP

| Cliente | Status | Módulos contratados | ERP / Integração |
|---|---|---|---|
| Reserva | Regime CS | — | Linx / SAP |
| Puket | Regime CS | — | — |
| Caedu | Regime CS | uFlow | Linx |
| Camys | Regime CS | — | — |
| 4takes | Regime CS | uFlow | Não |
| NV | Regime CS | uFlow | Linx |
| Baw | Regime CS | — | — |
| TDC | Regime CS | — | — |
| Cambos | Regime CS | uFlow, uRocket | SPI (sistema próprio) |
| Oficina Reserva | Regime CS | uFlow | SAP e Linx |
| Mondpars | Regime CS | — | — |
| VIX | Onboarding | uFlow, uMetrics, uPick | Linx |
| Lofty Style | Onboarding | uFlow | Linx |
| Luiza Barcelos | Onboarding | uDash, uFlow | Linx e Safe Tech |
| Osklen | Onboarding | uBuy, uFlow | Linx |
| NK STORE | Onboarding | uFlow | Linx |
| Lenny Niemeyer | Onboarding | uFlow | Linx |
| Highstil | Onboarding | Cronograma, uDash, uFlow | Totvs |
| Plie | Onboarding | — | — |
| Moda Objetiva | Onboarding | uFlow | Ilimitar |
| Hering | Negociação | uFlow | Ilimitar |

⚠ **Seis clientes vivos estão sem módulo e sem ERP declarados** no Mapa: Puket, Camys, Baw, TDC,
Plie, Mondpars. **É lacuna de negócio, não de varredura** — a coluna está vazia na fonte.

### Validação cruzada: os repositórios de integração confirmam o ERP
`arzz-sap` (Arezzo/SAP) · `integracao-linx-nv` (NV) · `integration-baw-linx` (Baw) ·
`integration-cambos-spi` (Cambos) · `integration-lofty-linx` · `integration-luiza-barcelos-sft` ·
`integration-nk-linx` · `integration-objetiva-illimitar` · `integration-osklen-linx` ·
`integration-vix-linx` · `unico-linx` (parado desde 2023).

> ⚠ **Baw aparece com repositório `integration-baw-linx` e ERP vazio no Mapa.** O repositório prova
> a integração Linx. **A fonte de negócio está desatualizada em relação ao código.**

## 4 · O mapa de lacunas do corpus

### Totais
| Métrica | Valor |
|---|---:|
| Clientes | **46** |
| MDs de cliente | **1.229** |
| **Ocorrências de `[a preencher]`** | **26.593** |
| `institucional.md` | ✅ **46/46** |
| `jornada.md` | ✅ **46/46** |
| `pessoas.md` | ✅ **46/46** |
| **`contexto-area.md`** | 🔴 **0 de 644** |
| Demandas importadas | 994 |
| RFIs importados | 86 |

### 🔴 A lacuna estrutural número um
**Nenhum dos 46 clientes tem um único `contexto-area.md`.** São **644 arquivos que não existem** —
14 áreas × 46 clientes.

> É exatamente onde mora *o que a área faz, as ferramentas que usa, o vocabulário e as pessoas dela*.
> **Sem isso não há brain de área — e sem brain de área o brain da empresa é só uma capa.**

### Os 21 vivos, por volume de lacuna
| Cliente | MDs | Lacunas | Demandas | RFIs |
|---|---:|---:|---:|---:|
| Reserva | 126 | 3.188 | 120 | 2 |
| NV | 122 | 2.948 | 108 | 10 |
| Osklen | 124 | 2.932 | 117 | 3 |
| NK STORE | 103 | 2.359 | 87 | 12 |
| Lofty Style | 106 | 2.060 | 86 | 16 |
| VIX | 85 | 1.871 | 70 | 11 |
| Lenny Niemeyer | 76 | 1.832 | 69 | 4 |
| Luiza Barcelos | 78 | 1.768 | 70 | 4 |
| Cambos | 54 | 1.133 | 47 | 3 |
| Moda Objetiva | 37 | 806 | 34 | 0 |
| Oficina Reserva | 34 | 747 | 28 | 2 |
| **Caedu** | **33** | **696** | **26** | **4** |
| Puket | 29 | 515 | 16 | 9 |
| Baw | 26 | 492 | 18 | 4 |
| Plie | 19 | 397 | 16 | 0 |
| Highstil | 17 | 375 | 14 | 0 |
| Hering · Mondpars · TDC · Camys · 4takes | 3 cada | 17–34 | 0 | 0 |

> **Cinco clientes vivos têm só os 3 MDs canônicos e nada mais** — Hering, Mondpars, TDC, Camys e
> 4takes. Para eles o corpus é casca.

## 5 · Onde está a matéria-prima que preenche as lacunas

**A informação existe.** O que falta é transporte e padronização, não descoberta.

| Lacuna no corpus | Fonte que responde |
|---|---|
| Identidade, razão social, CNPJ, endereço | Mapa de Clientes — ⚠ **CNPJ só 7/49, endereço 5/49** |
| Status, funil, "onde estamos", "o que falta", OKRs | Mapa de Clientes — 16–17/49 |
| Key Account, consultor, time de atendimento | Mapa de Clientes — **Key Account 33/49** |
| Módulos e acessos contratados | Mapa de Clientes — 22/49 |
| ERP e integração | Mapa (20/49) **+ os 11 repositórios** (mais confiável) |
| Demandas e RFIs | 836 linhas do Notion · já há 994+86 no corpus |
| Pessoas da uMode, times, horas | **cx-hub** — `user_profiles`, `project_members`, `get_hours_by_member_area` 🔴 **dados travados** |
| Pessoas do cliente | Notion por cliente: *Perfil de Usuários e Permissionamentos* (NK, Lenny) |
| Configuração de conta no produto | **uflow** — 43 chaves de EntityConfig |
| Satisfação e feedback | Pesquisas de kick-off (Lofty, Osklen, Plie, Highstil, Lenny) · Feedback Interno 428 linhas |
| Propostas, contratos, atas | **vault** — artefatos datados `<slug>_YYMMDD_<assunto>.md` |

### As 43 chaves de configuração de conta da uFlow
`batch_custom_fields` · `block_checklist_for` · `block_highlight` ·
`block_measurement_table_name` · `can_edit_measurement_table_with_products` ·
`can_save_custom_measurement_table` · `can_save_custom_measurement_table_to_database` ·
`collection_map_exports_priority` · `collection_map_print_preview_mode` · `consumption_unit_block` ·
`default_currency` · `enable_collection_map_bulk_update` · `has_eans` ·
`hide_collection_map_columns_for` · `hide_map_template` · `hide_product_approval_dropdown` ·
`hide_search_bar` · `hierarchy_config` · `inactivate_variant_condition` · `material_grid_size` ·
`material_status_block` · `measurement_table_custom_default` · `measurement_table_limit` ·
`model_name_batch_gender` · `multi_collection_enabled` · `notification_block` ·
`order_collection_map` · `print_datasheet_reference_read_only` · `product_global_search` ·
`product_material_allow_duplicated` · `product_material_apply_to_all_variants` ·
`product_materials_ignored_custom_field_ids` · `product_reference_read_only` ·
`product_variant_global_search` · `read_only_config_block` · `rebriefing_dates` ·
`should_show_menu_ubuy` · `show_checklist_comments` · `show_checklist_measures_for` ·
`standard_currency` · `status_block` · `update_manufacturers` · `update_variants`

> **Cada uma dessas chaves é uma diferença de comportamento por cliente.** É material de
> `contexto-area.md` e de `institucional.md` — hoje invisível no corpus.

### O cx-hub é a fonte das pessoas, e está travado
114 objetos de schema, entre eles: `user_profiles` (papel global admin/analyst/viewer) ·
`project_members` · `demand_assignees` · `demand_collaborators` · `demand_watchers` ·
`demand_areas` · `clients` · `client_documents` · `client_rules` · `programs` · `projects` ·
`rfis` · `demand_time_entries` · e funções de agregação por pessoa
(`get_hours_person_breakdown`, `get_hours_by_member_area`, `get_wip_person_demands`).

> 🔴 **O repositório dá a estrutura; os registros estão no Supabase.** Para trazer as pessoas da
> uMode ao corpus é preciso acesso aos dados — export ou credencial de leitura.

### 📌 Achado lateral relevante para o projeto de transcrições
O cx-hub tem **módulo de Pautas de Reunião concluído** (Fase 9): `meeting_agendas`,
`meeting_participants`, `meeting_homework_items`, com *homework → tickets* e prompt de IA.
**Já existe um caminho de reunião para tarefa dentro de casa** — que o projeto de transcrições
precisa conhecer antes de desenhar o seu.

## 6 · O que vai para o negócio responder

Lacunas que **nenhuma fonte cobre** e que só o negócio resolve:

1. **CNPJ, razão social e endereço** — 7/49 e 5/49 no Mapa; a fonte real é o ERP ou o financeiro.
2. **Receita anual** — 2/49.
3. **Módulo e ERP dos seis vivos sem declaração** — Puket, Camys, Baw, TDC, Plie, Mondpars.
4. **Quantidade de lojas e usuários ativos** — 5/49 e 4/49.
5. **Quem é quem no cliente** — só NK Store e Lenny Niemeyer têm perfil de usuários no Notion.
6. **O que cada uma das 14 áreas faz em cada cliente** — 644 arquivos inexistentes. **Este é o maior,
   e é o que define se existe brain de empresa ou não.**

## Fontes
Varredura direta em 21 set 2026 nas 15 fontes da §1 · tabelas de trabalho em
`scratchpad/MESTRE-clientes.csv` e `scratchpad/CORPUS-preenchimento.csv`

## Governança
Somente o CEO altera conteúdo no BrainHub. **Números de varredura vencem** — o Mapa de Clientes é
export de **04/03/2026** e o corpus muda a cada commit. Refazer antes de citar.

---

# 🔴 CORREÇÃO — 21 set 2026, mesma data, depois de varrer a Puket

## A afirmação de cobertura acima está errada como escrita

Este documento afirma que os **46 clientes do corpus cobrem 100% dos clientes reais do Notion**.

**Isso foi medido contra uma fonte só** — a base `Mapa de Clientes`. Contra ela, a afirmação
se sustenta (falta apenas `Loungerie`). **Mas `Mapa de Clientes` não é a única lista de clientes
que existe no Notion.**

É exatamente o modo de falha que o `CLAUDE.md` nomeia: **concluir cobertura a partir de um caminho
só.** Procurei a segunda lista depois, e ela existe.

## A segunda lista: a base `Portal do Cliente`

`collection://6548a3ae-bdc2-41cb-a412-f179d36f5c76`, em `Databases / 12. Portal do Cliente`.

São **32 linhas**: 28 portais de cliente, 2 templates, 1 `[TESTE]` e 2 sem nome. Cada portal é uma
página **voltada ao cliente** — logo da marca, link de Ouvidoria, contatos na uMode e uma base
`Projetos do cliente` própria.

### Sete clientes têm portal e **não têm linha no `Mapa de Clientes` nem casa no corpus**

| Cliente | Portal criado em |
|---|---|
| **Inbrands** | 27/09/2023 |
| **Malwee** | 30/11/2023 |
| Innocence Fashion | 15/09/2023 |
| Alcance Jeans | 30/08/2023 |
| Disparate Jeans | 18/09/2023 |
| Navarro | 11/10/2023 |
| Tee Fashion | 16/08/2023 |

**Verificado num caso:** o portal da **Malwee** tem conteúdo real — ícone da marca, callout de
projetos em curso, base `Projetos do cliente`, link de Ouvidoria e um contato nomeado
(*Alexandre Ferrari*). Última edição em **01/12/2023**.

> ⚠ **Não afirmo que são clientes ativos, nem que foram perdidos.** Afirmo o que está verificado:
> **existe portal, não existe linha no `Mapa de Clientes`, não existe casa no corpus** — e o único
> que abri tem conteúdo real. **O que aconteceu com esses sete é pergunta para o negócio.**
>
> Inbrands e Malwee **não são contas pequenas**. Se passaram pela uMode e sumiram do mapa,
> isso é história institucional perdida — que é precisamente o que o BrainHub existe para impedir.

### Dois erros de grafia na origem, entre as duas listas
| `Portal do Cliente` | `Mapa de Clientes` |
|---|---|
| `Basíco&Co` | `Básico&Co` |
| `StudioZ` | `Studio Z` |

**Corrigir é na fonte.** Aqui ficam registrados para que a próxima reconciliação automática não os
conte como clientes distintos — **eu mesmo quase contei.**

### Dos 13 clientes vivos, só 6 têm portal
**Têm:** NV · Oficina · Osklen · Puket · Reserva · Vix (+ `Simples Reserva`)
**Não têm:** Caedu · Cambos · Lofty Style · Luiza Barcelos · NK STORE · Moda Objetiva · Loungerie

E a relação `Clientes` da base `Portal do Cliente` está **vazia em todas as 32 linhas** — o portal
**não aponta de volta** para o cliente no `Mapa`. **São duas listas que não se falam.**

## O que isso muda no método
1. **Nenhuma afirmação de cobertura sem dizer contra qual fonte foi medida.** A frase correta é
   *"o corpus cobre 100% do `Mapa de Clientes`, menos Loungerie"* — nunca *"100% dos clientes"*.
2. **`Portal do Cliente` entra na lista de fontes** a varrer por cliente.
3. **Reconciliar as duas listas** é tarefa aberta, e leva os sete nomes acima ao negócio.
