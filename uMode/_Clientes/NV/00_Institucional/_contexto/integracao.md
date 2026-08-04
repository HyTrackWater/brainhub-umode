# NV · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
NV
### ERP / sistema integrado
Linx
### Repositório de código
`github.com/UmodeApp/integracao-linx-nv` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integracao-linx-nv`
### Documentação de referência
- `docs\documentacao-geral-linx-nv.md` — 75 KB
- `docs\tabelas-do-linx-nv.md` — 43 KB
- `.claude\skills\docs-integracao-linx-nv\SKILL.md` — 9 KB
- `README.md` — 2 KB
### Status da integração
Em produção — o documento descreve os agendamentos ativos do stage `v1` (produção) e os apps PM2 `nv-v1-worker`/`nv-staging-worker`; em `dev`/`staging` não há cron, apenas endpoints HTTP.
## Arquitetura
### Direções de integração
Ambas. Escrita: produtos (uFlow → Linx), programações de produção (uFlow → Linx) e tabela de medidas de e-commerce (uFlow → **API da NV**, que repassa à VTEX — a uMode não fala com a VTEX). Leitura: cores básicas e materiais (com cores e fornecedores) do Linx para a uFlow.
### Mecanismo
Acesso direto ao banco do Linx (SQL Server via Knex `mssql`/`tedious`, `requestTimeout` 60 s) com INSERT/UPDATE e execução de stored procedures; filas SQS FIFO; API REST da uFlow autenticada por JWT; e um POST HTTP para a API da NV no fluxo de e-commerce. Alerta por webhook do Discord.
### Ambiente e execução
AWS Lambda (Serverless, Node.js 16, us-east-2) com 4 filas SQS FIFO via `serverless-lift` (`product-queue`, `programacao-queue`, `ecommerce-post-tabela-queue`, `material-queue`), todas `batchSize: 1` e timeout de 900 s. Peculiaridade central: existe um **worker Express rodando em PM2** num servidor com acesso à rede do Linx — várias Lambdas apenas repassam o evento por HTTP (`WORKER_API_URL`) e é o worker que executa todo o consumo de fila e todo acesso pesado ao banco do Linx.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Produto e suas cores no Linx (cadastro básico, propriedades, cores + código de barras, ficha-versão, preços, materiais da ficha, cores de material e rota de operações); programações de produção (cabeçalho, propriedades e quantidades por cor/tamanho); e o payload da tabela de medidas para o e-commerce.
### Gatilho e frequência
Crons em UTC (BRT = UTC−3): produtos a cada 30 min, 24/7 (`cron(0/30 * ? * * *)`); programações a hh:15 e hh:45 das 04:15 às 19:45, seg–sex; tabela de medidas e-commerce 00:30 e 12:30. Produtos e programações: até 30 registros por execução; e-commerce: paginado de 50 em 50 até esgotar. Há endpoints manuais de enfileirar, forçar sem fila e telas de pendentes/erros. `MessageGroupId` fixo por fila força processamento estritamente serial — uma mensagem travada bloqueia a fila inteira.
### Regras e validações
- Fila de produtos: coleção em `dev`, não deletado, `linx_last_integration` (2346) vazio, `linx_integration_error` (4924) vazio, marca fixa 2568 ou criada a partir de 2023-06-19, e ter `reference` **ou** a Validação 40 em `passed`. Erro não mapeado (7778) e silencioso (7779) **não** bloqueiam — o produto volta à fila a cada 30 min.
- Integração em **três momentos**: Momento 1 sempre (PRODUTOS, PROP_PRODUTOS); Momento 2 só com os "3 SIMs" (`cadastro_finalizado`, `enviar_planner`, `liberado_integracao` todos `'SIM'`) → cores, ficha, preços; Momento 3, aninhado no 2, só com `material_status` ∈ {`done`,`dev`} → materiais e rota. Sem os 3 SIMs, o update grava apenas `STATUS_PRODUTO`.
- Rastreio do produto pela propriedade `PROP_PRODUTOS.PROPRIEDADE = '00209'` = ID uMode; mais de um registro é erro; zero registros ou ID divergente → erro `This product was not created by uMode` **e o produto é marcado como integrado** para sair da fila em definitivo (workaround explícito).
- Referência gerada = `rede_loja` (fallback `'16'`) + referência da coleção + sequencial de 4 dígitos; exceção para `reference` começando com `UMD`, usada como está.
- Todos os updates passam por `dirtyAttributes` — só colunas com valor diferente são gravadas; sem mudança, nenhum UPDATE.
- Truncamentos silenciosos no insert de PRODUTOS: `COMPOSICAO` → 6 chars, `GRUPO_PRODUTO` → 25, `TRIBUT_ORIGEM` → 3; propriedades truncadas a 70 chars.
- Cancelamentos: `status_atual = 'REPROVADO'` → update só de `DESC_PRODUTO` (+ " - CANCELADO") e `STATUS_PRODUTO`; `status_cor` preenchido na variante → cor cancelada (`STATUS_VENDA_ATUAL='2'`).
- Filtro de variantes/empenhos: variante não deletada e com `check_variant`; empenho `checked`, `responsavel_material === 'NV'`, nome do material sem "indefinido" (case-insensitive) e material com `reference`. Programações: só variantes com `amount > 0` e `sku`; nome do batch limitado a 25 chars; registro criado manualmente no Linx (sem marcador `UMODE`) nunca é sobrescrito.
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores básicas (código e nome) e materiais (tecidos e aviamentos) com tipo, NCM, observações, status ativo, unidades, fator de conversão e uma variante por cor de material, incluindo composição, fornecedor e preço.
### Gatilho e frequência
Crons diários de madrugada, executados no worker: materiais 00:00 BRT (`cron(0 3 * * ? *)`) e cores 00:24 BRT (`cron(24 3 * * ? *)`). Há também o caminho manual por fila (`POST /import-materials/enqueue`) e telas de pendentes. Sem cron em `dev`/`staging`.
### Regras e validações
- Janela incremental por `DATA_PARA_TRANSFERENCIA > corte`, com o corte vindo da **última execução finalizada** (`success`/`partial_success`) — execução com status `error` nunca avança a janela, então um dia de falha é relido no dia seguinte. A rota de create/update da uFlow é idempotente por referência/código, então reler janela maior não duplica.
- Cores: `CORES_BASICAS` com `USO_PRODUTOS = true`, `COR LIKE 'NV%'` e `DESC_COR <> 'DISPONIVEL PARA NV'`; carga inicial `new Date(0)`. Cor existente → atualiza só o nome; cor nova → criada com `rgb` fixo `'[255,255,255]'`. **Não há reprocessamento automático de erros** neste fluxo.
- Materiais: só griffes `'NATI VOZZA'` e `'NV PETIT'`; corte por `start_datetime` → `created_at` da última execução finalizada (−3h) → carga inicial `2026-01-19`. `start_datetime` anterior a 2026-01-19 ativa um filtro extra de lista fixa de coleções históricas, para backfill não trazer coleção fora de escopo.
- `type`: `M.TIPO` contendo `'PANO'` → `fabric`, senão `accessory`; o campo é usado como chave do payload e removido antes do envio. `name` = `DESC_MATERIAL` + código do fornecedor. `active` = inverso de `INATIVO`. `price` = `CUSTO_REPOSICAO` com fallback `GS_CUSTO_NEGOCIADO`.
- O JOIN com `COLECOES` existe na consulta, mas `collection` é **descartado** e não vai para a uFlow.
- Bloqueio de concorrência em materiais, com exceção para execução stale (sem `executed_at` e criada há mais de 1 hora). Materiais com erro são relidos nas execuções seguintes até entrarem com sucesso.
- Erro num registro não interrompe os demais → execução termina `partial_success`; erro estrutural é gravado explicitamente como `error` (terminal).
## Tabelas e endpoints
### Tabelas do ERP mapeadas
17 tabelas com schema documentado, todas em `docs/tabelas-do-linx-nv.md` (seções 9.1–9.17), sem cópia aqui. Por assunto: **produto** — PRODUTOS, PROP_PRODUTOS, PRODUTO_CORES, PRODUTO_FICHA_VERSAO, PRODUTOS_PRECOS; **materiais do produto e rota** — PRODUTO_VERSAO_MATERIAL, PRODUTO_VERSAO_MATERIAL_COR, PRODUTOS_TAB_OPERACOES, PRODUTO_OPERACOES_ROTAS; **programação de produção** — PRODUCAO_PROGRAMA, PROP_PRODUCAO_PROGRAMA, PRODUCAO_PROG_PROD; **leitura** — CORES_BASICAS, MATERIAIS, MATERIAIS_CORES, MATERIAIS_COMPOSICAO, FORNECEDORES. Consultadas como lookup (sem schema no documento): PRODUTOS_STATUS, PRODUTOS_SUBCATEGORIA, PRODUTOS_TAMANHOS, FILIAIS, PRODUCAO_RECURSOS, COLECOES. Procedures acionadas: `PROC_GS_GERA_CODIGO_BARRAS` e `LX_CALCULA_CUSTO_EFETIVO_PRODUTO`.
### Endpoints externos utilizados
- API REST da uFlow: `https://api-uflow.umode.app/api/v1` (produção), JWT
- `POST https://backend--bynv.myvtex.com/v1/post-tabela` — API da NV (URL hardcoded), até 3 tentativas com 20 s de espera
- Worker Express interno via `WORKER_API_URL` (PM2)
- Banco SQL Server do Linx (`LINX_DB_*`)
- Webhook do Discord (menção a devs ou ao CS conforme a categoria do erro)
## Particularidades deste cliente
- **Arquitetura Lambda + worker PM2**: entre os clientes Linx, é o único descrito com um worker Express externo que executa o consumo de fila e o acesso ao banco; as Lambdas atuam como proxy.
- **Gate dos "3 SIMs" e Momento 3 por `material_status`** — modelo de liberação em três estágios que não existe nas outras integrações.
- **Fluxo exclusivo de tabela de medidas de e-commerce** enviado a uma API da NV (não à VTEX), com regra de negócio própria: só sobem as linhas de medida marcadas com o custom `ecommerce = 1`. Não há campo de controle "já enviado" — o critério é `updated_at ≥ corte` (corte = `created_at` da última execução do tipo; na primeira execução de todas, ontem). Resposta final ≠ 200 **não** gera erro no produto, só é registrada em `linx_last_integration_response`.
- **Fluxo exclusivo de programações de produção** (batches) com validação 138 e campo de erro próprio (`linx_programmation_error` 7816).
- **Quantidades por tamanho posicionais**: `P1`–`P16` são resolvidas localizando o nome do tamanho na coluna `TAMANHO_n` da grade em `PRODUTOS_TAMANHOS` — correção histórica motivada pelo caso dos calçados, em que gravar na ordem do batch jogava volume na posição errada.
- **`MATERIAL`/`COR_MATERIAL` de `PRODUTO_CORES` hardcoded** em `'30.02.0053'`/`'0158'`, sobrescrevendo o cálculo anterior (código morto) — listado como ponto pendente de validação no próprio documento.
- **Rota de operações por posição fixa**: `RECURSO_PRODUTIVO` e `CUSTO_SUGERIDO` são gravados só no 2º registro da rota-modelo, cuja query não tem `ORDER BY` — também marcado como pendente de validação. No update, só a linha com `FASE_PRODUCAO = '006'` é tocada.
- **Erro no PROP_PRODUTOS se autoanula**: o campo de erro é preenchido, sobrescrito pela etapa seguinte e depois limpo, resultando em produto sem erro e sem data de integração, que simplesmente volta à fila.
- `rede_loja` dinâmico com fallback `'16'` (CON-054) alimentando tanto a referência quanto a propriedade `01005` da programação.
- Filtro de leitura restrito às griffes `NATI VOZZA`/`NV PETIT` e a cores com código `NV%`.
- As tabelas das Validações 40 e 138 vivem na configuração da uFlow, não no código — o documento avisa que precisam de atualização manual.
## Auditoria e monitoramento
Toda execução é registrada em `integration-executions` da uFlow com `INTEGRATION_ID = 5`, acumulando relatório de criados/atualizados/erros e status (`pending`, `executing`, `success`, `partial_success`, `error`). Erros classificados em três categorias com campo custom próprio no produto (mapeado 4924, não mapeado 7778, silencioso 7779) e notificação no Discord mencionando devs ou CS conforme a categoria — apenas nos stages `staging`, `v1` e `v2`. Telas HTML de pendentes e de erros por fluxo (produtos, programações, e-commerce, materiais) e função `healthCheck`. `silent_error` nunca é limpo automaticamente.
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
- Inventário de arquivos do repositório `integracao-linx-nv` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
