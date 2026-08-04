# Baw · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
Baw
### ERP / sistema integrado
Linx
> Confirmado contra o `institucional.md` deste cliente, que registra
> `ERP / Integração` = "Linx".
### Repositório de código
`github.com/UmodeApp/integration-baw-linx` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-baw-linx`
### Documentação de referência
- `docs\documentacao-geral-baw-linx.md` — 59 KB
- `docs\tabelas-do-linx-baw.md` — 32 KB
- `.claude\skills\docs-integracao-baw-linx\SKILL.md` — 11 KB
### Status da integração
Em produção — o documento descreve o stage `v1` (produção) com crons ativos nos dois sentidos.
## Arquitetura
### Direções de integração
Ambas. Escrita uFlow → Linx cobre **produtos** (produto-pai, preços-esqueleto, cores/variantes, ficha técnica, empenho de materiais e empenho por cor). Leitura Linx → uFlow cobre os cadastros de base: **cores, fornecedores, grades (tabelas de medidas) e materiais**.
### Mecanismo
Nenhum acesso direto ao banco: a integração chama por **HTTP** uma API intermediária, o **interceptor / uConnect** (`umode-microservice-uconnect`), que é quem conversa com o **SQL Server do Linx** (via Knex). Lado uFlow, **API REST** (axios). Enfileiramento por **SQS FIFO**. Leitura não é ao vivo: responde de um **snapshot em MongoDB** gerado por processo agendado dentro do uConnect (≈23:00 UTC / 20:00 BRT, substituição completa diária com swap por `processId`).
### Ambiente e execução
**AWS Lambda** (Serverless Framework v3, Node.js 18, TypeScript, região `us-east-2`). **5 filas SQS FIFO**: `product-queue`, `color-queue`, `supplier-queue`, `grid-size-queue`, `material-queue` — todas `batchSize: 1`, timeout 900s; Lambdas HTTP/enfileiradoras com timeout 29s. Padrão `enqueue*` (cria a execução e enfileira) + worker `*FromQueue` (faz o trabalho). Stages `dev`, `staging`, `v1`; **só o `v1` tem cron** — nos outros, apenas disparo HTTP manual. Túnel **VPN** até o servidor do cliente é aberto no primeiro produto da execução e fechado no último.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Produtos, em 7 tabelas do Linx na ordem fixa: `PRODUTOS` → `PRODUTOS_PRECOS` → `PRODUTO_CORES` → `PRODUTO_FICHA_VERSAO` → `PRODUTO_VERSAO_MATERIAL` → `PRODUTO_VERSAO_MATERIAL_COR` [por variante] → `PRODUTOS_PRECO_COR` [por variante]. **Não** envia `PROP_PRODUTOS`, `PRODUTOS_OPE_EXTRA` nem código de barras.
### Gatilho e frequência
Cron `enqueueProducts` a cada 30 min, **04:00–19:30 BRT, seg–sex**, até **30 produtos por execução** (excedente cai nas execuções seguintes). Também manual: `POST /products/enqueue` (lista de IDs), `GET /products/{id}` (enfileira um) e `GET /products/{id}/force` (sincroniza na hora, sem fila). `MessageGroupId` fixo `sync_product` → processamento estritamente serial; dedup por `<id>-<updated_at>`.
### Regras e validações
Fila automática (AND): `last_integration` vazio, `linx_integration_error` vazio, `liberado_integracao` preenchido, produto não deletado e **Validação 6 (Integração Linx)** em `passed`/`warning`. Os caminhos "force" ignoram todos esses filtros.
Insert vs. update decidido pela presença da `reference` do produto; no update, `DATA_CADASTRAMENTO`, `GRUPO_PRODUTO` e `SUBGRUPO_PRODUTO` são removidos do corpo.
Update **"dirty"** no interceptor: compara campo a campo e só atualiza colunas que mudaram (com `trim`, datas normalizadas); campo não enviado nunca apaga valor existente.
Referência do produto gerada pelo interceptor no formato **`GG.SS.NNNN`** (grupo.subgrupo.sequencial), com incremento do sequencial em `PRODUTOS_SUBGRUPO` — numeração por grupo+subgrupo; grupo/subgrupo inexistente faz falhar.
Preços são **esqueleto**: 4 linhas fixas (`'01'`,`'02'`,`'04'`,`'14'`) **sem valor** — reprocesso é no-op, preços existentes preservados.
Três categorias de erro: mapeado (`linx_integration_error` → CS), não mapeado (`non_mapped_error` → devs) e silencioso (`silent_error`, não interrompe e **não é limpo** no sucesso).
Órfãos são deletados só em `PRODUTO_VERSAO_MATERIAL` e `PRODUTO_VERSAO_MATERIAL_COR`; variantes/cores removidas na uFlow **não** são apagadas de `PRODUTO_CORES`.
Sem transação entre tabelas e sem retry no interceptor — recuperação depende do reprocesso pela fila.
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores (`CORES_BASICAS`), fornecedores (`FORNECEDORES`), grades / tabelas de medidas (`PRODUTOS_TAMANHOS`) e materiais (`MATERIAIS` + `MATERIAIS_CORES`, com joins em `COLECOES` e `FORNECEDORES`).
### Gatilho e frequência
Crons diários escalonados em produção: cores 06:00, fornecedores 06:30, materiais 07:00, grades 07:30 (BRT). Uma mensagem única por fila (lista forçada acima de 500 itens é dividida em lotes de 500). Como o snapshot no Mongo é gerado ≈20:00 BRT do dia anterior, as leituras da manhã consomem a fotografia da noite anterior.
### Regras e validações
Janela incremental (`updatedAtAfter`): `start_datetime` manual → `created_at` da **última execução finalizada com sucesso** (−3h fixas, fuso SP) → `01/01/1970` na primeira execução. Execução que falhou por completo **não avança a janela**. Filtro compara com a coluna `DATA_PARA_TRANSFERENCIA`.
IDs que falharam na última execução voltam como `errorsReferences`, em condição "OU" com o filtro de data.
Bloqueio de concorrência por tipo, com exceção para execução presa em `pending`/`executing` há mais de 1 hora (stale).
Cores: todas entram, sem filtro; update só do `name`; `rgb` sempre branco `[255,255,255]`.
Fornecedores: whitelist de `TIPO` (`PRODUTOS ACABADOS` / `MATERIA PRIMA`); **inativos são importados** e nunca desativados; matching por **nome** (não por referência).
Grades: `items_csv` monta `TAMANHO_1..48` pulando vazios e valores com ponto; **erro em uma grade derruba o lote inteiro** (as outras leituras pulam o item e seguem).
Materiais: grupo `AVIAMENTOS` → accessory, qualquer outro → fabric; `active` é o inverso de `INATIVO`; `name` = `DESC_MATERIAL` + código do fornecedor; cor sempre com `book` fixo `MATERIAIS_CORES`; unidades passam por mapa de valores.
Nenhum fluxo faz exclusão de órfãos — o que sai do Linx permanece na uFlow.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
**13 tabelas do Linx** documentadas com DDL completo em `docs/tabelas-do-linx-baw.md`: 7 de **escrita** (produto — `PRODUTOS`, `PRODUTOS_PRECOS`, `PRODUTO_CORES`, `PRODUTO_FICHA_VERSAO`, `PRODUTO_VERSAO_MATERIAL`, `PRODUTO_VERSAO_MATERIAL_COR`, `PRODUTOS_PRECO_COR`) e 6 de **leitura** (cadastros base — `CORES_BASICAS`, `FORNECEDORES`, `PRODUTOS_TAMANHOS`, `MATERIAIS`, `MATERIAIS_CORES`, `COLECOES`). Além delas, tabelas auxiliares apenas **lidas** durante a escrita: `PRODUTOS_GRUPO` e `PRODUTOS_SUBGRUPO` (geração da referência), `MATERIAIS` (fase/setor de produção), `MATERIAIS_CORES` (cor do material) e `PRODUTOS_TAMANHOS` (grade para consumo por tamanho).
### Endpoints externos utilizados
Interceptor/uConnect (`INTERCEPTOR_BASE_URL`, timeout 120s): rotas de upsert por tabela, roteadas por `partnerId`, mais `vpn-connect` e `vpn-disconnect`. API REST da uFlow (`API_URL`), incluindo `integration-executions` (`INTEGRATION_ID` = 21). AWS SQS (5 filas FIFO). Webhook do Discord (`DISCORD_URL`).
## Particularidades deste cliente
- Entre Baw, Cambos e Luiza Barcelos, é a única que usa **interceptor/uConnect + VPN + banco SQL Server** — as outras duas falam direto com a API HTTP do ERP.
- Leitura **não é ao vivo**: passa por snapshot diário em MongoDB gerado pelo uConnect, então os dados lidos de manhã têm até ~10h de defasagem.
- **Não gera código de barras** — não há etapa (nem comentada), nem stored procedure, e `status_atual` não é gatilho de barra (o doc destaca isso como diferença explícita frente a outras integrações Linx).
- Referência do produto (`GG.SS.NNNN`) é **gerada e sequenciada dentro do interceptor**, com incremento em `PRODUTOS_SUBGRUPO` — só a tabela `PRODUTO` tem código específico da Baw; as demais usam a implementação genérica do Linx.
- **Contas contábeis fixas por `INDICADOR_CFOP`** injetadas pelo interceptor (não vêm da uFlow e não são lidas de `PARAMETROS`); podem, por si só, disparar um update "dirty".
- Validação pesada na uFlow: **Validação 6** com ~26 itens (marca, coleção, hierarquia, NCM, nome ≤40, grade, rota de operação compatível com o grupo, tecido/aviamento, consumo, etc.).
- `COR`/`COR_PRODUTO` recebem o **SKU** da variante, não a referência da cor da uFlow; `CLASSIF_FISCAL`, `TRIBUT_ORIGEM`, `COMPOSICAO` e `MATERIAL` são herdados do produto por todas as variantes.
- Consumo por tamanho espalhado em 48 colunas `C1..C48`, casadas com a grade pelo interceptor; sem grade no Linx, erro bloqueante.
- Fornecedores casados por **nome** (não por código) — divergência de nomenclatura cria duplicidade.
- Grades são o único fluxo de leitura **sem tratamento de erro por item**.
## Auditoria e monitoramento
Toda execução registrada em `integration-executions` da uFlow (`INTEGRATION_ID` = 21) com relatório de criados/atualizados/erros e status (`pending`, `executing`, `partial_success`, `success`, `error`). Erros gravados em campos custom do produto (`linx_integration_error`, `non_mapped_error`, `silent_error`) e notificados por **webhook no Discord**, mencionando devs ou CS conforme a categoria — só em `staging`/`v1`. Tela `/products/with-error` lista produtos com qualquer um dos três campos de erro. Sem menção a auditoria pós-integração comparando Linx × uFlow.
## Incidentes registrados
| Data | Incidente | Resolução | Fonte |
|---|---|---|---|

## Governança
### Responsável técnico
[a preencher]
### Quem pode alterar este documento
[a preencher]

## Fontes
### Documentos consultados
- Mapeamento repositório → cliente informado pelo desenvolvedor via Vinicius em 03 ago 2026
  (registrado em `protocolo-gestao-integracao.md`)
- Inventário de arquivos do repositório `integration-baw-linx` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
