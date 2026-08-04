# uFlow · Modelo de dados

> Levantado em **04 ago 2026** por leitura direta de `C:\Ambientes Virtuais\uFlow\umode-flow` —
> `db/schema.rb` (3.246 linhas), `db/migrate/` (443 migrations), `app/models/` (263 arquivos) e
> `Gemfile`. É o primeiro documento nosso sobre a estrutura do banco da plataforma legada, e existe
> porque a demanda [`D-2026-002`](../../00_Institucional/_demandas/D-2026-002.md) exige que o agente
> de suporte domine o schema.
>
> **Escopo:** descreve o que o schema diz. Não é proposta de mudança, não é auditoria pedida pela
> equipe de tecnologia, e não substitui o `schema.rb` — aponta para ele.

## Escala
### Números
**211 tabelas** · versão do schema **`2026_06_17_150000`** · **443 migrations** (a primeira de
27/07/2019, a última de **17/06/2026**) · 263 arquivos em `app/models/`, dos quais **162 classes
herdam de `ApplicationRecord`** (105 na raiz, 60 em `j3/`, 4 em `shop/`, 3 em `ahoy/`, 2 em
`umode3a/`) · **142 tabelas anotadas** nos headers dos models pela gem `annotate`.
### Última atividade
Última migration em **17/06/2026**, coerente com a versão do schema. As duas mais recentes criam e
evoluem `umode_product_cost_pending_updates` — ou seja, **o trabalho mais recente no banco é
reconciliação de custo de material**. Antes disso houve um intervalo: as migrations de 2025 terminam
em 13/11/2025.

## Convenção de nomes — e a correção que ela impõe
### Os prefixos reais
| prefixo | tabelas |
|---|---|
| `umode_` | **119** |
| `jumper_` | **63** |
| `shop_` | 7 |
| `blazer_` | 5 |
| `ahoy_` | 3 |
| `vw_` | 2 |
| `taggable_` · `laravel_` · `active_storage_` | 2 cada |
| sem prefixo (`audits`, `business_rules`, `migrations`, `sessions`, `tokens`, `mailkick_opt_outs`) | 6 |
### ⚠ Correção à fonte de treinamento
O documento de treinamento do agente diz "prefixo de tabela geralmente `umode_...`". **É verdade,
mas incompleto e por isso perigoso:** `umode_` cobre **119 de 211 tabelas (56%)** — as outras **92
não seguem**, e as **63 `jumper_*` são o núcleo da plataforma** (tenant, usuário, política, workflow,
tarefa, arquivo, comentário, integração). Um agente que assumir `umode_` como regra vai errar em
**44% do banco**, incluindo justamente as tabelas de acesso e de integração.
### `j3_` não existe
**Zero tabelas com prefixo `j3_`.** `J3` é **apenas um namespace Ruby**: `app/models/j3.rb` define
`self.table_name_prefix` que resolve para **`jumper_`**. Consequência prática, e é armadilha real:
`app/models/j3/user_role.rb:29` declara `self.table_name = 'user_roles'` e **a tabela real é
`jumper_user_roles`**.
> **Regra para qualquer investigação:** nunca confie no literal de `self.table_name` sem somar o
> prefixo do namespace. `ApplicationRecord` força `umode_`; `app/models/j3.rb` força `jumper_`;
> `app/models/shop.rb` força `shop_`.

## De onde a plataforma veio
### A uFlow é a reescrita de um app PHP/Laravel chamado "Jumper"
Evidência no próprio schema: as **63 tabelas `jumper_*`** são o núcleo herdado, e sobraram
`laravel_jobs`, `laravel_failed_jobs`, `migrations` (a tabela de controle de migration do Laravel) e
`sessions` — todas mortas no Rails. As **119 `umode_*`** são a camada de domínio PLM de moda
construída sobre esse núcleo. `J3` é o namespace Ruby que encapsula o legado Jumper.
**Nada disso está no `README.md`** — o contexto existe só no schema e nos nomes de arquivo.
> **Cruzamento com o que já sabíamos:** a página "Taxonomia" do Notion documenta "Actions do Jumper
> (legado uFlow)" com um anexo `JUMPER_ACTIONS.txt`, e registra 6.567 campos originais do uFlow. Os
> dois achados são a mesma coisa vista de dois lados — **"Jumper" é o nome do legado de dentro do
> legado**.

## Domínios
| Domínio | Tabelas principais |
|---|---|
| **Core multi-tenant (J3)** | `jumper_entities` · `jumper_entity_configs` · `jumper_entity_relations` · `jumper_subscription_plans` · `jumper_customers` · `jumper_customer_invoices` |
| **Usuários e acesso** | `jumper_users` · `jumper_user_roles` · `jumper_user_profiles` · `jumper_profiles` · `jumper_user_or_policy_accesses` · `jumper_scoped_models` · **`jumper_policies` (fora do `schema.rb`)** |
| **Produto e variante** | `umode_products` · `umode_product_variants` · `umode_product_types` · `umode_model_types` · `umode_product_associations` · `umode_product_history` · `umode_eans` · `umode_ncms` |
| **Ficha técnica e campos dinâmicos** | `jumper_active_form_templates` · `jumper_custom_fields` · `jumper_custom_field_values` · `umode_hierarchies` · `umode_custom_statuses` |
| **Materiais — tecidos** | `umode_fabrics` · `umode_fabric_variants` · `umode_fabric_types` · `umode_fabric_locations` · `umode_fabric_variant_suppliers` · `umode_product_fabric_variants` |
| **Materiais — aviamentos** | `umode_accessories` · `umode_accessory_variants` · `umode_accessory_types` · `umode_accessory_locations` · `umode_product_accessory_variants` |
| **Fornecedores e fabricantes** | `umode_suppliers` · `umode_product_manufacturers` · `umode_service_types` · `umode_product_supplier_services` |
| **Grades e medidas** | `umode_grid_sizes` · `umode_grid_size_item` · `umode_sizes` · `umode_measurement_tables` · `umode_measurement_types` · `umode_measurement_values` · `umode_measurement_customs` |
| **Cores e estampas** | `umode_colors` · `umode_prints` · pivots correspondentes |
| **Custos** | `umode_product_cost_sheets` · `umode_product_cost_sheet_details` · `umode_product_cost_compositions` · **`umode_product_cost_pending_updates`** · `umode_price_ranges` · `umode_currencies` |
| **Aprovações** | `umode_product_approvals` · `umode_product_approval_types` |
| **Checklists e validações (QA)** | `umode_checklists` · `umode_checklist_items` · `umode_checklist_fillings` · `umode_checklist_filling_items` · `umode_checklist_filling_measurements` · `umode_validations` · `umode_validation_results` |
| **Coleções e mapas** | `umode_collections` · `umode_brands` · `umode_themes` · `umode_fashion_levels` · `umode_collection_map_exports` · `jumper_map_templates` |
| **Pedidos de compra** | `umode_batches` · `umode_batch_products` · `umode_purchase_order_batches` · `umode_purchase_order_balances` · 2 views `vw_*` — **mas o pedido em si mora em `umode_products` via STI** |
| **Workflow / kanban (atual)** | `jumper_workflows` · `jumper_workflow_columns` · `jumper_workflow_cards` · `jumper_workflow_card_moves` · `jumper_workflow_column_restrictions` · `jumper_workflow_column_user_policies` |
| **Workflow legado (sem model)** | `umode_workflows` · `umode_workflow_columns` · 3 pivots |
| **Tarefas e calendário** | `jumper_tasks` · `jumper_task_types` · `jumper_calendars` · `jumper_events` |
| **Integrações e importações** | `jumper_integrations` · `jumper_integration_executions` · `jumper_actions` · `jumper_imports` · `umode_email_automations` |
| **Auditoria** | `audits` · `umode_product_history` · `umode_error_logs` |
| **Arquivos e mídia** | `jumper_files` · `jumper_pictures` · `jumper_attachments` · `active_storage_*` |
| **Comunicação** | `jumper_comments` · `jumper_notification` · `jumper_message_templates` · `jumper_whatsapp_messages` · `ahoy_messages` |
| **⚠ Fora do PLM, no mesmo banco** | `jumper_leads` · `jumper_pipedrive_deals` (CRM) · `jumper_customers` + `jumper_customer_invoices` + `jumper_subscription_plans` (faturamento da própria uMode) · `blazer_*` (BI) · `ahoy_*` (analytics) · `shop_*` (vitrine) |
| **Legado morto** | `laravel_jobs` · `laravel_failed_jobs` · `migrations` · `sessions` |

## Multi-tenant: o isolamento depende de JOIN
### O número que corrige a premissa
A documentação interna diz "quase tudo pertence a uma entity". **O schema não confirma:**
**89 tabelas têm `entity_id`; 122 não têm — 58% do banco.** E há apenas **41 `add_foreign_key`
apontando para `jumper_entities`** (de 216 FKs no total), então menos da metade das tabelas com
`entity_id` tem FK real garantindo o tenant.
Não há RLS, não há schema-per-tenant, não há `search_path`. É **discriminator column** em coluna
comum, e **a integridade de tenant é garantida pela aplicação, não pelo banco**.
### Subsistemas inteiros sem `entity_id`
- **Todo o kanban atual:** das 11 tabelas `jumper_workflow_*`, **só `jumper_workflows` tem
  `entity_id`**. Qualquer query de kanban por cliente exige subir até lá.
- **Todo o detalhe de custo:** `umode_product_cost_sheets`, `_details`,
  `_composition_fields`, `_composition_values`.
- **Todos os 26 pivots `umode_pivot_*`.**
- `jumper_custom_field_values` e `jumper_custom_field_associations` — só o `jumper_custom_fields` pai
  tem tenant.
- `umode_measurement_values` — só via `measurement_table_id`.
- `umode_checklist_items`, `_filling_items`, `_filling_measurements`, e toda a família `validation_*`.
- **`jumper_users` não tem `entity_id`** — usuário é global, e o vínculo com cliente vive só em
  `jumper_user_roles` (`user_id` + `entity_id` + `policy_id`). Um e-mail existe uma vez para a base
  inteira.
- **`audits` não tem `entity_id`** — ver Auditoria.
- **`umode_themes` não tem `entity_id`**, sendo que `umode_collections` e `umode_brands` têm. Anomalia
  dentro do mesmo domínio.
### `entity_id` nullable com significado
`NULL` costuma querer dizer "global da uMode, herdado por todos": `umode_collections.entity_id`,
**`jumper_active_form_templates.entity_id`** (template de ficha global), `jumper_actions.entity_id`,
`umode_colors.entity_id`, `umode_grid_size_item.entity_id`, `umode_product_manufacturers.entity_id`.
### `entity_id` sem índice — filtro de tenant faz full scan
`umode_product_approvals` · `umode_batch_products` · `umode_error_logs` · `umode_grid_size_item` ·
`umode_hierarchies` · `umode_collection_map_prints` · `jumper_custom_reports`.

## Integrações — e a ligação com o resto da Casa
### `jumper_integrations` — a configuração
`entity_id` (NOT NULL, indexado, FK) · **`class_name`** (nome da classe Ruby do runner, resolvido por
`constantize`) · **`properties`** (text, **YAML**, lido com `YAML.safe_load`) · `deleted_at`.
⚠ **É aqui que moram as credenciais do ERP de cada cliente**, dentro do YAML de `properties`.
### `jumper_integration_executions` — a tabela que o IntHub observa
`integration_id` (bigint, NOT NULL, FK) · `status` (string(15)) · `properties` (snapshot do YAML no
disparo) · **`report` (json nativo)** · `executed_at` · `created_at` · `updated_at`.
**Status possíveis** (gem `enumerize`, **sem CHECK no banco**): `pending` · `executing` ·
`partial_success` · `success` · `error`.
### 🔴 Quatro propriedades desta tabela que explicam o comportamento do IntHub
1. **Não tem `entity_id`.** O tenant só se resolve por JOIN obrigatório:
   `jumper_integration_executions.integration_id` → `jumper_integrations.id` →
   `jumper_integrations.entity_id` → `jumper_entities.id`. **Não existe query de execução por cliente
   sem esse JOIN.** É a explicação estrutural de por que a tela "Carteira" do IntHub foi redefinida
   para agrupar por `class_name` em vez de por cliente.
2. **Não tem `deleted_at`** e **não há expurgo em nenhuma das 443 migrations** — é append-only e só
   cresce.
3. **O único índice é `integration_id`.** `status`, `executed_at`, `created_at` e `updated_at` **não
   têm índice** — e o controller ordena por `updated_at DESC`. Um poller que filtra por status ou
   ordena por data faz **full scan**.
4. **Soft-deletar uma integração deixa as execuções órfãs de tenant** — o pai tem `deleted_at`, a
   filha não, então o JOIN com `acts_as_paranoid` passa a não casar.
### ✅ A API existe — e fecha o circuito com os 10 repositórios de integração
`app/controllers/api/v1/j3/integration_executions_controller.rb`:
`GET /api/v1/integration-executions` (com **ransack**, `includes(:integration)`, ordem
`updated_at DESC`, paginado) · `GET /:id` · **`POST`** (cria execução externamente) · **`PATCH /:id`**
(append incremental no `report` — acumula, remove de `pending` o que já apareceu em
`created`/`updated`/`error`, e promove o status).
> **Síntese que nenhum documento da Casa tinha:** os 10 repositórios de integração por cliente são
> Lambdas **externas** que gravam aqui por HTTP. O `INTEGRATION_ID` que documentamos nos
> `integracao.md` (**5** NV · **21** Baw · **22** Lofty Style · **25** Luiza Barcelos) é o
> `jumper_integrations.id`. Ou seja: **Lambda do cliente → `POST /api/v1/integration-executions` →
> linha em `jumper_integration_executions` → polling do IntHub via MySQL.** O circuito está fechado, e
> o `INTEGRATION_ID` é a chave que ligaria execução a cliente no IntHub.
### ⚠ Dois pontos de atenção no controller
`set_integration_execution` usa `J3::IntegrationExecution.find(params[:id])` **sem escopo de entity**
— o registro é buscado pelo id global. E o `rescue` do `update` **está comentado** no código.
### Runners dentro da uFlow: só Millenium
`app/services/integration/` tem `base_integration.rb`, `millenium_api.rb`, `millenium_material.rb`,
`millenium_product.rb`, `millenium_service.rb`. **O único ERP integrado por dentro da uFlow é o
Millenium** — Linx, SAP, SPI e Safe Tech vivem nas Lambdas externas. Há também
`app/services/j3/action/run_integration.rb`, que dispara integração pelo motor de `jumper_actions`.
### `jumper_imports` é outro caminho, com outra máquina de estado
`entity_id` (tem) · `deleted_at` (**não tem**) · `model` (classe alvo) · `content` (**longtext**) ·
`report_json` (**text**, parseado na aplicação) · status com **7 valores**: `pending` · `running` ·
`error` · `partial_success` · `success` · `rollback` · `cancelled`.
⚠ **Vocabulário diferente dos 5 de execution — não são a mesma máquina de estado.** E `report` é
`json` nativo numa tabela e `text` na outra: duas implementações para a mesma ideia.
### 🔴 `integration_id` é dois campos com o mesmo nome
**18 tabelas de negócio têm uma coluna `integration_id` que é `string` e guarda o ID do registro no
sistema externo** (chave de de-duplicação de importação) — **não é FK para `jumper_integrations`**:
`jumper_leads`, `umode_accessories`, `umode_accessory_types`, `umode_brands`,
`umode_checklist_fillings`, `umode_collections`, `umode_colors`, `umode_fabric_types`,
`umode_fabrics`, `umode_grid_sizes`, `umode_material_packages`, `umode_measurement_tables`,
`umode_prints`, `umode_product_approvals`, `umode_product_types`, `umode_products`, `umode_suppliers`,
`umode_hierarchies`.
Pior: **`umode_hierarchies.integration_id` é `integer`**, não `string`. E **nenhuma das 18 tem
índice**, apesar de ser exatamente a coluna que um importador consulta a cada linha
(`WHERE entity_id = ? AND integration_id = ?`).
`jumper_custom_fields.integrated` (boolean) marca quais campos customizados a integração pode escrever.

## Configuração por cliente: regra é dado, não schema
### O que isso significa na prática
`jumper_active_form_templates.definition` guarda **a estrutura inteira da ficha técnica de um cliente
como YAML numa célula `mediumtext`**. Somado a `jumper_custom_fields` + `_values` (campo arbitrário em
qualquer entidade), `jumper_policies.rules`, `jumper_actions.trigger`/`action_params`,
`umode_validations.condition`, `business_rules.content` e
`jumper_workflow_column_restrictions.trigger` — tudo é **regra-como-dado**.
> **Consequência crítica para o agente e para nós:** "que campos o cliente X tem" **não é pergunta de
> schema, é pergunta de conteúdo de linha**. Nenhum desses campos é indexável nem validável pelo
> banco.
### 🔴 `jumper_entity_configs.deleted_at` é `t.string`
É a **única** coluna `deleted_at` do tipo `string` em todo o schema (as outras 147 são `datetime` ou
`timestamp`). `acts_as_paranoid` comparando string com timestamp aqui é fonte de bug silencioso — e
isto está justamente na tabela que a fonte de treinamento chama de **"a razão nº 1 de funciona pra um
cliente e não pra outro"**.
### ⚠ O catálogo de EntityConfigs não foi levantado
A varredura que enumeraria **todas** as `EntityConfig` usadas no código foi interrompida em 04 ago
2026 por limite de crédito da organização, antes de produzir resultado. **A única config conhecida
por nome continua sendo `product_manufacturer_supplier_status`** (da Osklen, `entity_id = 3580`).
Enumerar essas configs é enumerar **onde o comportamento muda por cliente** — é a lacuna de maior
valor que resta neste documento.

## "Lacre" não existe no banco
Não há tabela, coluna nem model com `seal`, `lacre` ou `sealed`. **O lacre é implementado por cliente,
como campo customizado**, com nome acordado: `app/helpers/checklist_fillings_helper.rb:70`,
`app/reports/checklist_filling_report.rb:11` e `app/views/checklist_fillings/_list.html.slim:6`
buscam os custom fields chamados **`lacre_checklist`** e **`data_lacre_checklist`** via
`fetch_checklist_custom_fields(current_entity, ...)`. Há ainda um custom field `alt_pos_lacre`
("IMPORTANTE Alteração Pós Lacre") numa definição de ficha e uma coluna de kanban chamada "Produto
Lacrado" nas fixtures.
> **Por que isto importa muito para nós:** o lacre é etapa central no nosso vocabulário — o
> `produto.md` do **DesenvolvAI** descreve o módulo como "croqui → lacre", e o do **CriAI** e o do
> **CadastrAI** dependem dessa fronteira. **Descobrimos que ela é convenção de nome de campo, não
> entidade de dados.** Um cliente que renomeie o campo quebra o relatório. É regra de negócio frágil e
> precisa ser registrada como tal.

## Armadilhas do schema
### Estrutura
- **`umode_products` é STI e guarda quatro coisas.** `type` (string(17)) separa `Product`,
  **`PurchaseOrder`**, `ProductBundle` e `ProductTemplate`. **O pedido de compra é uma linha em
  `umode_products`** — `order_approved_at`/`order_expected_at`/`order_issued_at` só fazem sentido
  nessas linhas. **Contar produtos sem filtrar `type` infla o número.**
- Existe `umode_product_bundles` (tabela) **e** `ProductBundle` (STI) — coisas diferentes com o mesmo
  nome. Idem `umode_template_product_types` vs `ProductTemplate`.
- **`umode_product_variants` não tem coluna de cor.** A cor vem por pivot ou pelas linhas de BOM —
  contra-intuitivo para quem espera "variante = cor".
- **3 tabelas com PK composta** (todas `shop_`), que o Rails 5.2 não suporta nativamente.
  **7 tabelas com `id: false`.** `taggable_tags` usa PK `tag_id`.
- **Duas famílias de tag coexistem:** `taggable_*` e `umode_tags`/`umode_products_tags`.
### 🔴 O `schema.rb` não é a fonte de verdade completa
**4 tabelas existem no banco e não estão no `schema.rb`** — descobertas pelos headers `annotate` dos
models. A mais grave é **`jumper_policies`**, a tabela de permissão da plataforma inteira, para a qual
apontam `umode_suppliers.policy_id`, `jumper_user_roles.policy_id`, `jumper_scoped_models.policy_id` e
`umode_error_logs.policy_id`. As outras: `jumper_entities_invites`, `umode_user_brands`,
`umode_user_collections`.
**E 6 das 8 views `vw_*` também estão fora** — inclusive `vw_purchase_order_product` e
`vw_purchase_order_product_variant`, usadas em SQL cru dentro de `purchase_order.rb:150-157`.
**Um `db:schema:load` num ambiente novo produz uma aplicação que não sobe.**
⚠ As duas `vw_*_materialized` presentes **não são materialized views** — MySQL não tem esse recurso.
São tabelas comuns populadas por processo externo; o nome engana.
### Tipos e enums
- **Dinheiro como `float`.** `umode_product_cost_sheets.value_cents` é `t.float`, apesar do sufixo
  `_cents` que na convenção implica integer. Idem `_details.value_cents`,
  `umode_product_manufacturers.manufactory_price_cents`, `umode_fabrics.price`,
  `umode_accessories.price`. **`money-rails` não está no `Gemfile`.** Todo cálculo de custo neste
  schema carrega erro de ponto flutuante.
- **Enums são string sem CHECK** (gem `enumerize`, 33 models) — qualquer valor inválido entra por SQL
  direto. Vários com `limit` apertado: `umode_products.status limit:9` (e `"cancelled"` tem
  exatamente 9 chars — **no limite**), `material_status limit:7`, `type limit:17`,
  `jumper_integration_executions.status limit:15`, `umode_product_approvals.status limit:21`.
- **`umode_checklists.review_required` é `t.string` com default `"true"`** — booleano como texto.
- **`jumper_entities` tem `status` (string) e `status_i` (integer)** — dois campos de status na mesma
  tabela, e **só `status_i` tem índice**. Já `jumper_users.status` é integer.
- `umode_grid_sizes.custom` é `integer` e `umode_measurement_tables.custom` é `boolean` — mesmo
  conceito, tipos divergentes.
- **camelCase no meio do snake_case:** `sizeRange`, `priceUnit`, `minPurchase`, `dateStart`. E o mesmo
  conceito grafado nos dois estilos: `price_unit` nas tabelas de material vs `priceUnit` nas de BOM.
### Soft delete
Gem `paranoia ~> 2.2`, **114 models** com `acts_as_paranoid`. **148 das 211 tabelas têm
`deleted_at`; 63 não têm.** O tipo é inconsistente: **99 `datetime`, 48 `timestamp`, 1 `string`**.
As centrais que **não** têm — onde um `WHERE deleted_at IS NULL` quebra:
**`jumper_integration_executions`** · **`jumper_imports`** · `umode_purchase_order_balances` ·
`umode_checklist_filling_items` e `_measurements` (o pai `umode_checklist_fillings` tem — apagar o pai
deixa itens órfãos visíveis) · `umode_validation_results` e `_items` ·
`umode_measurement_table_exports` · todas as junções puras · **14 dos 26 `umode_pivot_*`** (enquanto
os outros 12 têm — inconsistência na mesma família).
Observação inversa: **`audits` TEM `deleted_at`** e índice nele — o próprio log é soft-deletável.
### Polimorfismo
**48 colunas `*_type`/`*_id`.** As mais relevantes: `jumper_workflow_cards.record_type/record_id`
(qualquer entidade pode ser card), `jumper_workflow_associations` com um **segundo discriminador
`record_subtype`** (para separar as STI de `umode_products`),
`jumper_custom_field_values.target_type/target_id`,
`umode_product_cost_sheets.record_type/record_id`, `umode_checklist_fillings.target_type/target_id`,
`umode_material_package_materials` com **duas** polimórficas na mesma linha, e
`umode_product_associations` polimórfico **nas duas pontas**.
⚠ **Falsos polimórficos** — colunas `*_type` que são só enum de texto, sem par `*_id`:
`umode_suppliers.supplier_type`, `umode_collections.template_type`,
`jumper_custom_fields.field_type`, `umode_product_history.history_type`, e outras.
**`jumper_integration_executions.integration_type` cai aqui:** parece o par polimórfico de
`integration_id`, mas `integration_id` tem FK dura — a coluna `_type` é resíduo redundante.
### Desnormalização deliberada de custo
`umode_product_fabric_variants` e `umode_product_accessory_variants` **copiam** `reference`, `name`,
`composition`, `grammage`, `width`, `price` e `priceUnit` do material de origem para a linha de BOM.
**Preço divergente entre `umode_fabrics.price` e `umode_product_fabric_variants.price` não é bug — é o
design.** A tabela `umode_product_cost_pending_updates` existe exatamente para reconciliar
(`previous_price`, `new_price`, `detected_at`, `resolved_at`, `ignored_at`) — e é o trabalho mais
recente do banco, o que confirma que o problema é **ativo, não histórico**.
Há **quatro caminhos concorrentes** para chegar ao material na mesma linha de BOM: `fabric_id`,
`fabric_variant_id`, `fabric_variant_supplier_id`, `material_package_material_id`.
### Padrão de "cópia customizada" por auto-referência
`umode_measurement_tables.original_table_id` + `custom` · `umode_measurement_types.original_type_id` ·
`umode_grid_sizes.custom` · `umode_products.parent_product_id` · `umode_hierarchies.parent_id` ·
`jumper_policies.parent_policy_id`. O cliente clona um template global e edita — **a mesma tabela
guarda o catálogo canônico e as N variações por cliente**, distinguidos por flag. Investigar medida
sem checar `custom`/`original_table_id` leva a conclusão errada.
### Colunas quentes sem índice
`jumper_integration_executions`: `status`, `executed_at`, `created_at`, `updated_at` · `entity_id` em
7 tabelas · `integration_id` (string) em todas as 18 · `purchase_order_id` nas 3 tabelas de pedido ·
`umode_measurement_values.value` · **nenhuma coluna `position` tem índice**.
### `position` sem gem gerenciando
**15 tabelas têm `position`, mas só 5 models declaram `acts_as_list`** (`checklist_item`,
`j3/workflow_card`, `j3/workflow_column`, `product_approval`, `validation_item`). Nas outras 10 a
ordenação é manual e pode ter duplicatas e buracos.
### Fila dentro da tabela
`umode_collection_map_exports` implementa fila com heartbeat em coluna (`heartbeat_at`,
`heartbeat_total_rows`, `heartbeat_current_row`, `heartbeat_priority`, `heartbeat_performance` json) —
job longo monitorado por polling de coluna, não por sistema de fila. E
`umode_collection_map_exports.model` é **`t.virtual`**, gerada por `json_extract(options,'$.model')`:
editar `options` muda `model` silenciosamente.

## Auditoria
### `audits` — a trilha global
Gem `audited ~> 4.9`, **97 models** auditados, tabela única. Colunas relevantes: `auditable_type` +
`auditable_id` (polimórfico) · `associated_type` + `associated_id` (agrupamento) · `user_id` +
`username` (desnormalizado, sobrevive ao delete do usuário) · **`sudo_user_id`** (campo **custom**,
não é da gem — registra **impersonação**) · `action` · `audited_changes` (mediumtext, `{campo =>
[antes, depois]}`) · `version` · `remote_address` · **`request_uuid`** (correlaciona todas as mudanças
de um mesmo request) · `deleted_at`.
**Permite** replayar uma alteração de ficha técnica campo a campo, com autor, IP, versão e
agrupamento por request — e ver se foi por impersonação.
**Não permite** listar "tudo que mudou no cliente X": **`audits` não tem `entity_id`**. É preciso
resolver `auditable_type`/`auditable_id` contra cada tabela de negócio; se o registro foi
hard-deleted, o tenant é irrecuperável. O `username` desnormalizado existe para mitigar parte disso.
### Trilha paralela
**`umode_product_history`** — `user_id`, `product_id`, **`entity_id`** (tem), `history_type`,
`changes` (json nativo), `deleted_at`. Duplica parcialmente a função de `audits` só para produto, mas
**com tenant**. Sem model anotado. **Duas fontes de verdade para histórico de produto, e nada indica
qual é autoritativa.**

## Observações de segurança
> Levantadas por leitura de schema, sem extrair nenhum valor. Não é auditoria de segurança — são
> pontos que a estrutura expõe e que a equipe de tecnologia precisa avaliar.
- **`jumper_integrations.properties` (YAML) é onde ficam as credenciais de ERP por cliente.** Isto
  **confirma no nível do schema** o `RISC-001` que a documentação do IntHub registra como aberto
  ("senhas de ERP em YAML plaintext em 24 linhas ativas", owner Bergson).
- **`jumper_entities.api_token`** é um token em coluna `string`, aparentemente sem hash.
- **`jumper_users` tem duas colunas de senha:** `password` (string(191)) e `encrypted_password` (not
  null, default `""`). A primeira parece resíduo do legado Laravel — vale verificar se ainda é
  populada.
- **O isolamento entre clientes depende da aplicação em 58% das tabelas.** Um bug de escopo em
  qualquer caminho sem `entity_id` vaza dado entre clientes **sem que o banco reclame**. O controller
  de `integration_executions` já busca por id global, sem escopo.
- **O banco operacional dos clientes carrega o banco comercial da uMode** — faturamento, plano de
  assinatura e CRM (com integração Pipedrive) vivem lado a lado com ficha técnica de cliente.

## Legado candidato a remoção
**~9 tabelas sem nenhum model as referenciando:** o workflow antigo (`umode_workflows`,
`umode_workflow_columns` e 3 pivots — todo workflow vivo está em `app/models/j3/`) e o bloco Laravel
(`laravel_jobs`, `laravel_failed_jobs`, `migrations`, `sessions`).
**73 tabelas do `schema.rb` não têm model anotado** — além das legadas, isso inclui os 26 pivots
(normal, acessados por `has_and_belongs_to_many`) e o subsistema `shop_` (7 tabelas, 4 models), o que
sugere que a "loja" está parcialmente implementada.

## Gems que moldam o schema
`paranoia ~> 2.2` (114 models) · `audited ~> 4.9` (97 models) · `enumerize` (33 models) ·
`acts_as_list` (5 models, 15 colunas `position`) · `annotate` (dev) · `blazer` ·
`ahoy_matey` / `ahoy_email` · `mailkick 0.4.3`.

## Fontes e referências
### Documentos consultados
- `C:\Ambientes Virtuais\uFlow\umode-flow\db\schema.rb` (3.246 linhas, versão `2026_06_17_150000`)
- `db/migrate/` — 443 migrations, de 27/07/2019 a 17/06/2026
- `app/models/` (263 arquivos), `app/controllers/api/v1/j3/integration_executions_controller.rb`,
  `app/services/integration/`, `app/models/j3/integration.rb`, `app/models/j3/integration_execution.rb`,
  `app/models/j3/import.rb`, `app/models/application_record.rb`, `app/models/j3.rb`, `Gemfile`
- Headers `annotate` dos models — em vários casos **mais fiéis ao banco real que o `schema.rb`**
- Leitura feita em 04 ago 2026, somente leitura, nada alterado no repositório da uFlow

## Governança
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**.
Vinicius está alterando tudo neste momento porque está na fase de construção do cérebro — é exceção
declarada de construção, não a regra de operação.
