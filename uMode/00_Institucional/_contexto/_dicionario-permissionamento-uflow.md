---
aliases:
  - "Dicionário do permissionamento do uFlow — como a permissão funciona de verdade"
tags:
  - tipo/autoridade
  - casa
---
# Dicionário do permissionamento do uFlow — como a permissão funciona de verdade

> **Classe: `CORPUS`.** É a **autoridade** sobre *como o permissionamento do uFlow funciona*.
> As matrizes por cliente (`Perfil de Usuário e Permissionamentos`) dizem **o que está ligado
> em cada conta**; este documento diz **com que mecanismo**.
>
> **Fonte única:** `📕 [Notion] - Manual do Permissionamento` (`6d0379fa…`), em
> `uMode Geral / uFlow / Documentação de Setup - PLM`. **Aberta por inteiro em 23 set 2026**,
> incluindo a base inline `Traduzindo o tecniquês` (`collection://ecb435c6-…`, **72 linhas**).
> Última edição da fonte: **01/09/2024**.
>
> **Escrita própria da uMode, para uso interno.** Todo `[C]` aqui é leitura dessa página.

## 0 · O que este documento NÃO resolve

- ⚠ **Não é leitura de código.** É leitura do **manual** que a uMode escreveu sobre o próprio
  código. **Se o código mudou depois de 01/09/2024, este documento não sabe.**
- ⚠ **Os links de exemplo apontam para `umode.app/admin/...` com IDs concretos**
  (`j3_entity_configs/530`). **Não abri nenhum** — é painel administrativo de produção.
- 🔴 **O manual lista 20 `entity_configs` como exemplo, não como catálogo.** **Não sei quantas
  existem.** O que está aqui é o que o manual nomeia.
- 🔴 **Não sei quais configs estão ativas em qual conta.** Isso vive no admin, não aqui.

## 1 · 🔴 A permissão mora em TRÊS lugares, não em um `[C]`

| Parte | Onde | O que governa |
|---|---|---|
| **Perfis de usuário** | `umode.app/admin/j3_policies` | o que o perfil pode/não pode, por controller |
| 🔴 **Configs de conta** | `umode.app/admin/j3_entity_configs` | comportamento **da conta inteira**, fora do escopo padrão |
| **Templates de formulário** | `umode.app/admin/j3_active_form_templates` | o que cada perfil vê e edita **dentro da ficha** |

> 🔴 **Toda leitura que o corpus fez de matriz de permissão supôs UM lugar.** A matriz do
> Notion é o retrato do primeiro. **Uma linha 🔴 pode estar vindo de qualquer um dos três.**

⚠ **É por isso que "bloqueado por permissão" e "funcionalidade desligada" aparecem iguais na
matriz:** o primeiro é `policy`, o segundo costuma ser `entity_config`.

## 2 · `Includes` e `Excludes` — os dois tipos de perfil `[C]`

| Tipo | O que a configuração enumera |
|---|---|
| **`Includes`** | tudo aquilo que o perfil **pode** ter. Ex. citado: `Fornecedores / Clientes / Externos` |
| **`Excludes`** | tudo aquilo que o perfil **NÃO** pode ter |

A fonte sugere o critério de escolha: *"pensar no tipo de perfil pela quantidade de regras de
inclusão e exclusão pensada para este perfil"*.

### 2.1 · 🔺 Três vocabulários para a mesma coisa

| Documento | Palavras |
|---|---|
| 🟢 **Este manual** (técnico, o que existe em código) | **`Includes`** / **`Excludes`** |
| `[NV] Permissionamento`, página-mãe | `Inclusão` / **`Restrição`** |
| `NV - Geral`, sub-página | `inclusão` / **`exclusão`** |

> 🔴 **O manual é o que nomeia o código.** ⚠ **Mas quem escreve documentação de cliente usa
> outras duas palavras** — e o `CLAUDE.md` trava taxonomia como essencial.
> **Registro a divergência; a escolha é do Vinicius.**

## 3 · Os três `controllers` `[C]`

Toda regra começa declarando o `controllers`.

| Controller | O que é |
|---|---|
| **`J3`** | áreas do sistema **que não pertencem a uma ficha**. Ex.: a aba de tarefas — existe no sistema, aparece na ficha, mas não se relaciona diretamente com ela |
| **`datasheet`** | áreas **diretamente ligadas à ficha** (template de formulário). Ex.: `datasheet/product_approvals: [index]` |
| 🆕 **`fields`** | **o mais recente.** Inclui ou exclui **campos** dos filtros do mapa de coleção |

> 🟢 **`J3` explica o `J3::UserRole` que o registro `(m)` achou na tabela `audits`** — e
> explica o prefixo `jumper_`/`J3` do código.

**`fields` funciona em três formatos:** `product_datasheet` (produto) · `product_variant`
(variante) · `product_approval` (aprovação). **Valor `write` inclui o campo no mapa; valor
`none` o remove da visualização.**

## 4 · 🟢 `scopable` — a permissão PODE ser de uma pessoa

> *"o **`scopable`** está diretamente relacionado com **quem** estará apto a fazer essa ação,
> ou seja, todo o perfil ou apenas um usuário desse perfil? essa distinção é feita através dos
> termos **`user`** ou **`policy`**"* `[C]`

| Valor | Alcance |
|---|---|
| **`policy`** | **o perfil inteiro.** Exemplo da fonte: `Seven - Client 1` |
| 🔴 **`user`** | **um usuário específico.** Exemplo da fonte: um e-mail nominal |

**Vale nas áreas de** marcas · produtos · coleções · temas · workflows. A regra tem duas
partes: **`actions`** (o que pode ser feito) e **`scopable`** (por quem).

### 4.1 · 🔺 Isto responde uma pergunta que eu tinha acabado de registrar

Ao ler a matriz da **Lofty Style** eu achei *"(Liberado só Isadora desse Perfil)"* e
*"(Somente a Dora)"* e escrevi que **o modelo de dados do uFlow não tinha onde guardar
permissão nominal**, deixando como pergunta ao Vinicius.

> 🔴 **Tinha onde. Chama-se `scopable: user`, está documentado desde 2024, e eu não tinha
> aberto esta página.**

**O que eu errei:** o registro `(m)` leu uma **query de análise de acesso** — `jumper_users` →
`user_roles` → `policies` — e eu tratei aquele recorte como **o modelo inteiro**.
⚠ **Era o recorte de uma consulta, não o schema.** É parente do erro do `entity_id = 3344`:
**tomar o alcance de um artefato pelo alcance do sistema.**

**A pergunta ao Vinicius muda de forma:** não é mais *"como isso está implementado?"* — é
**"a Isadora tem `scopable: user` de fato, ou é combinado que ninguém aplicou?"**

🆕 **E há um controller dedicado:** `j3/user_or_policy_accesses` — *"item de adicionar
usuários em marcas, coleções e/ou produtos"*. **O nome diz `user OR policy`.**

## 5 · Os parâmetros de `actions` `[C]`

| Parâmetro | O que faz |
|---|---|
| `index` | exibe ou não a aba relacionada |
| `show` | análogo a `index` |
| `new` | mostra o botão que leva ao formulário de cadastro |
| `create` | **grava de fato.** Sem ele, o formulário preenche e **não salva**. Depende de `new` |
| `edit` | permite a visualização detalhada de um item |
| `update` | **edita de fato.** 🔴 **Sem `edit` não aparecem os 3 pontinhos** |
| `destroy` | **permite excluir** um item cadastrado |
| `pdf` | download de uma impressão |
| `print` | habilita a impressão no produto |
| `review` · `review_checklist` · `send_checklist` | revisar e enviar checklist (dentro de `checklist_filling_items`) |
| `configure` | configuração pelo usuário no mapa de coleção |
| `filter` | habilita filtro. ⚠ **nem toda parte do sistema aceita filtro** |
| `autocomplete` | traz conjunto de resultados |
| `active_form` | permite ver tabelas/formulários em abas — ex.: a aba de variantes |
| `activate` · `deactivate` | ativar e **inativar** itens |
| `status` | exibe status em itens como a área de tasks |
| `duplicate` | duplicar, principalmente no contexto de produto |
| `move` | **só habilita o campo.** Para mover de fato, precisa de `move_to_*` |
| `move_to_variant` · `move_to_product` | mover imagem entre produto e variante. 🔴 **A fonte cita o cliente `NV` como quem mais usa** |
| `export` | exportar itens |

### 5.1 · 🟢 Três coisas do corpus que estes parâmetros explicam

| Achado anterior | Explicação |
|---|---|
| **NK STORE**, validação 04/12: *"não pode aparecer os 3 pontinhos"* | 🟢 **é `update` sem `edit`.** A resposta técnica existe desde 2024 |
| **Recco** libera `> excluir variante`, outros quatro bloqueiam | 🟢 **é `destroy` presente ou ausente.** **Confirma: configuração, não limitação** |
| **NV** tem abas de imagem ligadas a variante | 🟢 **`move_to_variant` / `move_to_product`, e a fonte nomeia a NV** |

## 6 · As `entity_configs` que o manual nomeia `[C]`

> *"O objetivo geral da criação de uma configuração de conta é tornar possível uma solicitação
> **não prevista no escopo padrão do sistema**."*

**Quem cria:** se a config **não existe**, é preciso **código** — dev. Se **já existe**, basta
cadastrar pelo admin apontando para a conta. **Dica da própria fonte: duplicar uma config já
ativa em outra conta.**

### 6.1 · 🟢 O mecanismo do "apelido interno" tem nome

| Config | O que faz |
|---|---|
| **`model_name_brand`** | altera o nome da área de **Marcas** |
| **`model_name_collection`** | altera o nome da área de **Coleções** |
| **`model_name_theme`** | altera o nome da área de **Temas** |
| **`model_name_batch`** | altera o nome da área de **Lotes** |

> 🟢 **O princípio nº 1 da Arquitetura V1 — o apelido do cliente na frente, o termo canônico
> entre parênteses — não é só prática observada: é configuração com nome.**
> As abas em caixa alta da **Cambos**, o `Fabricantes` da **Recco**, o `Chat NK` e o `Chat NV`
> estão todos nessa família. ⚠ **Não verifiquei config por config em qual conta está ativa.**

### 6.2 · As que governam o que o FORNECEDOR enxerga

| Config | O que faz |
|---|---|
| 🔴 **`product_manufacturer_supplier_status`** | *"quando o Fornecedor tiver sido mencionado no produto com o status do Fornecedor em **'Produção'**, esse Perfil do Fornecedor conseguirá visualizar esse produto"* |
| 🔴 **`hide_collection_map_columns_for`** | remove colunas do mapa. Exemplo da fonte: *"remover colunas de preço para que fornecedores não tenham acesso aos preços dos demais fornecedores"* |
| `separate_manufacturer_price_in_export` | separa o preço do fornecedor nas exportações de produto, variante e estampa |

> 🟢 **É o modelo de terceiro que o corpus procurava.** `Fornecedor` é perfil com login em
> Luiza Barcelos, Lenny Niemeyer, NK STORE e Recco — **e a visibilidade dele é governada por
> status de produto e por ocultação de coluna, não só por `policy`.**

### 6.3 · As demais que o manual nomeia

| Config | O que faz |
|---|---|
| **`has_eans`** | habilita a aba de **EANs** para a conta. 🟢 **explica por que só a Moda Objetiva tem a aba `EAN`** |
| **`hide_map_template`** | remove o botão de **exibições** para certos perfis. 🟢 **explica `Mapa de Coleção > Exibições` bloqueado na Recco** |
| **`status_block`** | bloqueia perfis de alterar o status dos produtos |
| **`block_checklist_for`** | bloqueia alteração do checklist |
| **`show_checklist_comments`** | libera comentários em todas as opções do checklist |
| `exclude_custom_fields_ids` | ao duplicar um produto, os campos listados **não** vão para a cópia |
| `select_product_info` | altera informações do produto ao duplicar |
| `enable_collection_map_bulk_update` | ativa **edição em massa** na conta |
| `collection_map_print_preview_mode` | ativa preview da impressão do mapa |
| `measurement_table_custom_default` | cria colunas personalizadas na tabela de medidas |
| `can_edit_measurement_table_with_products` | permite editar tabela de medidas com produtos associados |
| `gridSize_ignore_dots` | oculta colunas com `.` no nome |
| `stantard_currency` | moeda padrão da conta. ⚠ **o nome está escrito assim na fonte, com erro de grafia** |

## 7 · Permissionamento nos templates `[C]`

O template de formulário é **individual por conta**, e o permissionamento dentro dele segue o
mesmo padrão: pode ser igual para todos os usuários da conta, ou específico por usuário.

**Casos de uso que a fonte lista, cada um com link para a página `Ficha de Produto`:**
retirar o breadcrumb · desabilitar a impressora na ficha · manter colunas da ficha técnica como
apenas leitura · ocultar colunas do mapa na ficha técnica · liberar visualização de campos ou
abas · **bloquear edição de abas** · 🔴 **permitir que exclusivamente algum usuário ou perfil
edite informações na ficha técnica**.

> 🔴 **O último caso é o `scopable: user` de novo, agora dentro do template.** ⚠ **Não abri a
> página `Ficha de Produto` (`c3deb3dd…`) nem nenhuma das sete sub-páginas.**

## 8 · O mapa `controller → área do sistema` — 72 linhas `[C]`

**É o dicionário que traduz o que está na `policy` para o que o usuário vê.**

### 8.1 · Cadastros (menu `Cadastro` da matriz)

| Controller | Item na tela | URL |
|---|---|---|
| `product_types:` | Tipo de Produto | `/product-types` |
| `fabrics:` | Tecido | `/fabrics` |
| `fabric_types:` | Tipo de Tecido | `/fabric-types` |
| `accessories:` | Aviamento | `/accessories` |
| `accessory_types:` | Tipo de Aviamento | `/accessory-types` |
| `suppliers:` | Fornecedores | `/suppliers` |
| `colors:` | Cores | `/colors` |
| `product_bundles:` | Coordenado | `/product_bundles/new` |
| `prints:` | Estampas | `/prints` |
| `grid_sizes:` | Grades | `/grid-sizes` |
| `measurement_tables:` | Tabela de Medidas | `/measurement-tables` |
| `service_types:` | Tipo de Beneficiamento | `/service-types` |
| `supplier_service_types:` | Beneficiamento | `/supplier-service-types` |
| `product_cost_compositions:` | Composição de Custos | `/product-cost-compositions` |
| `product_templates:` | Ficha Técnica Base | `/product_templates` |
| `tags:` | Tag | `/tags` |
| `picture_categories:` | Categoria de Imagens | `/picture-categories` |
| `batch_types:` | Tipo de Lote | `/batch-types` |
| `j3/task_types:` | Tipo de Tarefa | `/task-types` |
| `packs:` | Pack | `/packs` |
| `j3/custom_fields:` | Campos Personalizados | `/custom-fields` |
| `material_packages:` | Pacote de Materiais | `/material-packages` |
| `importer:` | Importação | `/importer` |
| `integration:` | Integração | `/integration` |

> 🟢 **Cada linha `Cadastro` das dez matrizes tem aqui o seu controller.** A matriz vira
> legível em código.

### 8.2 · A ficha de produto (`datasheet/`)

| Controller | Aba |
|---|---|
| `datasheet/products:` | os produtos do sistema |
| `datasheet/product_info:` | informações gerais — **tipo usado em abas de formulário** |
| `datasheet/product_pictures:` | Imagens |
| `datasheet/product_variants:` | Variantes |
| `datasheet/product_sizes:` | Grade |
| `datasheet/product_materials:` | Materiais |
| `datasheet/product_manufacturers:` | Fornecedores **do produto** |
| `datasheet/product_measurement_table:` | Tabela de Medidas |
| `datasheet/product_approvals:` | Aprovações |
| `datasheet/product_files:` | Arquivos |
| `datasheet/product_comments:` | comentários do produto |
| `batch_products:` | Lotes do produto |
| `eans:` | cadastro de **EAN** no sistema e/ou no produto |
| `validation_popup:` | ver as **validações** pelo produto |
| `j3/task_popup:` | ver a aba de **atividades** no produto |

### 8.3 · Materiais, em detalhe

| Controller | O que é |
|---|---|
| `materials:` | os materiais do sistema |
| `fabric_variants:` | itens classificados como **tecido** na aba de materiais |
| `accessory_variants:` | itens classificados como **aviamento** na aba de materiais |
| `fabric_locations:` | **locais de aplicação do tecido** |
| `accessory_locations:` | **locais de aplicação do aviamento** |

### 8.4 · Checklists e relatórios

| Controller | O que é |
|---|---|
| `checklist_fillings:` | aba de checklists de um produto, dentro de aprovações |
| `checklist_filling_items:` | itens de um checklist |
| `checklist_filling_pictures:` | upload de imagem no comentário de um checklist |
| `reports/approvals:` | campos **expostos** na aba de aprovações |
| `reports/checklist_fillings:` | campos de checklist **expostos** na aba de aprovações |

### 8.5 · Estrutura, conta e usuário

| Controller | O que é |
|---|---|
| `products:` | **todos** os produtos (produto, variante, estampa…) |
| `product_datasheets:` | a ficha de produto como **template de formulário** |
| `j3/map_templates:` | **a ficha que compõe a estrutura de um produto** |
| `j3/active_form:` | controller de **página em formato de formulário** |
| `collection_map:` | mapa de coleção · `/collection_map` |
| `brands:` · `collections:` · `themes:` | marcas · coleções · temas |
| `j3/workflows:` | Workflows · `/workflows` |
| `j3/tasks:` | tarefas · `/tasks` |
| `calendar:` | calendário · `/calendar` |
| `menu:` | aba **Atividades** e tudo dentro dela |
| `today:` | atividades diárias, opcional no menu |
| `j3/pictures:` | as imagens do sistema |
| `j3/comments:` | os comentários do sistema |
| `j3/trix_attachments:` | upload de imagem e arquivo, gravar comentário |
| `j3/entities:` · `j3/entity_members:` | **usuários da conta** · `/entity-members` |
| `j3/entity_invites:` | convidar usuários · `/entity-invites/new` |
| `j3/entity_invoices:` | faturas · `/entity/invoices` |
| `j3/entity_subscriptions:` | assinaturas · `/entity/subscriptions` |
| `j3/users:` | a lista de usuários |
| `user_registrations:` | registro de usuários |
| 🔴 `j3/user_roles:` | **aba com `inativar usuário` e `acessar como`** |
| 🔴 `j3/user_or_policy_accesses:` | **adicionar usuários em marcas, coleções e/ou produtos** |

> 🔴 **`acessar como` existe.** ⚠ **É impersonação, e o corpus não tinha registro disso.**
> **Não sei quem pode usar.**

## 9 · O que fica aberto daqui

| Item | Estado |
|---|---|
| Página `Ficha de Produto` (`c3deb3dd…`) e suas 7 sub-páginas de permissionamento em template | 🔴 **não abertas** |
| Página `Fornecedor visualizar produto com algumas especificidades` (`10db406b…`) | 🔴 **não aberta** |
| `umode.app/admin/j3_entity_configs` — **quais configs existem e em que conta** | 🔴 **painel de produção, não acessado** |
| Quantas `entity_configs` existem no total | ⚠ **o manual lista 20 como exemplo** |
| 🆕 `williemberg@umode.com.br` aparece como **e-mail de exemplo** | ⚠ **não virou ficha** — um nome em exemplo não é fonte suficiente, mesma régua do Felipe Sindeaux e da Flávia |
| `Seven - Client 1` citado como exemplo de `policy` | ⚠ **`Seven Global` é cliente da carteira** — não confirmei que é a mesma conta |

## Governança

### Quem pode alterar este documento
Quem trouxer **leitura nova da fonte** — o `📕 Manual do Permissionamento` — ou **leitura do
código**. 🔴 **Este documento descreve um manual de 01/09/2024. Código lido vence manual.**

### O que este documento supersede
Nada é apagado. **Mas o registro `_varredura-2026-09-23a` § 5-bis afirma que o uFlow não tem
onde guardar permissão nominal, e isso está ERRADO** — o `scopable: user` existe. O registro é
`REGISTRO` e não se edita; **a correção vive aqui, e o registro aponta para cá.**

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1–§7, §9 | Notion — `📕 [Notion] - Manual do Permissionamento` (`6d0379fa…`), **aberta por inteiro** | **23 set 2026** |
| §8 | Notion — base inline `Traduzindo o tecniquês` (`collection://ecb435c6-e644-4d76-a41c-c5d24ff4ba94`), **72 linhas lidas por SQL** | **23 set 2026** |
| §5.1, §6.1–§6.3 | cruzamento com as dez matrizes de `Perfil de Usuário e Permissionamentos` | **23 set 2026** |
