# Lofty Style · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
Lofty Style
### ERP / sistema integrado
Linx
### Repositório de código
`github.com/UmodeApp/integration-lofty-linx` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-lofty-linx`
### Documentação de referência
- `docs\documentacao-geral-lofty-linx.md` — 65 KB
- `docs\tabelas-do-linx-lofty.md` — 33 KB
- `.claude\skills\docs-integracao-lofty-linx\SKILL.md` — 11 KB
- `AGENTS.md` — 2 KB
### Status da integração
Em produção — o documento descreve o stage `v1` (produção) com crons ativos; `dev`/`staging` rodam só por chamada HTTP manual.
## Arquitetura
### Direções de integração
Ambas. Escrita (uFlow → Linx): produtos e suas tabelas satélites. Leitura (Linx → uFlow): cadastros de base (cores, fornecedores, grades, materiais), nunca apagando registros na uFlow.
### Mecanismo
AWS Lambda (Serverless v3, Node.js 18, TypeScript, us-east-2) + 5 filas SQS FIFO (`product`, `color`, `supplier`, `grid-size`, `material`, `batchSize: 1`). A Lofty **não** acessa o banco do Linx: toda conversa é por HTTP com o interceptor/uConnect (`INTERCEPTOR_BASE_URL`, header `x-interceptor-api-token`, timeout 120s), que fala com o SQL Server do Linx via Knex. uFlow via API REST (axios, `api_token` dentro do JWT). Leitura serve-se de snapshot MongoDB, não do Linx ao vivo.
### Ambiente e execução
Serverless (Lambda), sem servidor permanente; workers com timeout 900s e rotas HTTP de enfileiramento com 29s. Padrão `enqueue*` (cron ou HTTP) → SQS FIFO → worker `*FromQueue`. Crons só no stage `v1`. `PARTNER_ID` `67d189e96fda67dd673dd7b6`; `INTEGRATION_ID` 22.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Produto e 9 tabelas, nesta ordem: PRODUTOS, PROP_PRODUTOS, PRODUTOS_PRECOS, PRODUTO_CORES, PRODUTO_FICHA_VERSAO, PRODUTO_VERSAO_MATERIAL, PRODUTOS_OPE_EXTRA (costura por fornecedor), PRODUTO_VERSAO_MATERIAL_COR e PRODUTOS_PRECO_COR (as duas últimas por variante). Código de barras (PRODUTO_BARRA) está desativado.
### Gatilho e frequência
Cron `enqueueProducts` a cada 30 min, 04:00–19:30 BRT, seg–sex, até 30 produtos por execução (`MessageGroupId` fixo = processamento serial; dedup por `<id>-<updated_at>`). Modos forçados que ignoram todos os filtros: `POST /products/enqueue` (lista de IDs), `GET /products/{id}`, `GET /products/{id}/force` (sync imediato, fora da fila).
### Regras e validações
Fila (AND): `last_integration` vazio, `linx_integration_error` vazio, `liberado_integracao` preenchido, produto não deletado e Validação 140 em `passed`/`warning` (27 itens, 24 bloqueantes). `liberado_integracao` é só filtro de fila — não destrava etapas internas; todas as tabelas rodam em sequência numa única execução. Insert vs. update decidido pela presença de `reference`; update só grava colunas "sujas" (`undefined` nunca apaga valor). Referência gerada no interceptor no formato `GG.SS.NNNN` (sequencial por grupo+subgrupo) e nunca regerada. Contas contábeis puxadas da tabela `PARAMETROS` do Linx. Erros em 3 categorias: mapeado (`linx_integration_error`, avisa CS), não mapeado (`non_mapped_error`, avisa devs), silencioso (`silent_error`, não aborta e **não** é limpo no sucesso). Sem transação entre tabelas e sem retry no interceptor. PROP_PRODUTOS deleta órfãos — propriedades cadastradas manualmente no Linx são apagadas a cada integração. PRODUTOS_PRECOS tem update no-op (protege preço real).
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores (`CORES_BASICAS`), fornecedores (`FORNECEDORES`), grades (`PRODUTOS_TAMANHOS`) e materiais (`MATERIAIS` + `MATERIAIS_CORES` + `COLECOES`).
### Gatilho e frequência
Crons diários (BRT): cores 05:00, fornecedores 05:30, materiais 06:00, grades 06:30. O snapshot que alimenta as leituras é gerado por cron **dentro do uConnect** às 23:00 UTC (20:00 BRT) — as leituras da madrugada consomem a foto da noite anterior. Também há POST de leitura forçada por lista de referências (ignora a data).
### Regras e validações
Incremental por `DATA_PARA_TRANSFERENCIA`, com corte na `created_at` da última execução **finalizada com sucesso** (`success`/`partial_success`) — falha não avança a janela; primeira execução usa epoch. Erros da última execução são reenviados (`errorsReferences`) fora do filtro de data. Bloqueio de concorrência ("Já existe uma integração em andamento"), com liberação de execução abandonada (>1h presa sem `executed_at`). Cores: só com `USO_MATERIAIS` ou `USO_PRODUTOS`; no update só o `name` muda. Fornecedores: whitelist de 7 tipos, inativos descartados, casamento **pelo nome** (risco de duplicidade se o nome mudar no Linx). Grades: tamanhos com ponto são ignorados e `items_csv` só é gravado na criação. Materiais: whitelist de 4 grupos, `INNER JOIN MATERIAIS_CORES`/`COLECOES` (material sem cor ou sem coleção nunca chega), inativos descartados, unidades convertidas por de-para. Nunca há delete na uFlow.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
15 tabelas documentadas com campo/tipo/obrigatoriedade em `docs/tabelas-do-linx-lofty.md`. Escrita (9): produto e propriedades (PRODUTOS, PROP_PRODUTOS), preços (PRODUTOS_PRECOS, PRODUTOS_PRECO_COR), cor/variante (PRODUTO_CORES), ficha técnica e empenho (PRODUTO_FICHA_VERSAO, PRODUTO_VERSAO_MATERIAL, PRODUTO_VERSAO_MATERIAL_COR), operações (PRODUTOS_OPE_EXTRA). Leitura (6): CORES_BASICAS, FORNECEDORES, PRODUTOS_TAMANHOS, MATERIAIS, MATERIAIS_CORES, COLECOES. A documentação geral ainda cita tabelas consultadas mas não detalhadas ali: PARAMETROS, PRODUTOS_GRUPO, PRODUTOS_SUBGRUPO, W_SEXO_TIPO, TABELA_LX_NCM, TABELA_LX_CEST, CEST_NCM.
### Endpoints externos utilizados
Interceptor/uConnect: rotas de escrita por tabela, `product-props-with-delete`, `POST /interceptor/linx/:partnerId/execute-procedure` (usada só pelo código de barras, desativado), leituras `GET /interceptor/:partnerId/colors|suppliers|grid-sizes|materials`, `POST /audit/:partnerId/integration`. API REST da uFlow (`API_URL`). Webhook do Discord (`DISCORD_URL`). Rotas HTTP próprias de uso manual: `POST /products/enqueue`, `GET /products/{id}`, `GET /products/{id}/force`, `/products/with-error`.
## Particularidades deste cliente
- Entre Lofty Style, NK STORE e Osklen, é a única que grava **PRODUTOS_OPE_EXTRA** — a costura por fornecedor/facção (`OPERACAO_EXTRA = "COSTURA [<fornecedor>]"`), com exclusão de órfãos e custo desativado; produto de revenda envia lista vazia e apaga as operações existentes.
- PROP_PRODUTOS com 18 propriedades fixas **mais propriedade dinâmica de armário** (o valor do custom `armario_entrada_cor` vira o próprio código `PROPRIEDADE`), enviadas em lotes de 5, com deleção de órfãos.
- Referência composta `GG.SS.NNNN` com sequencial por subgrupo — e, como `GRUPO_PRODUTO`/`SUBGRUPO_PRODUTO` passaram a ir no update, um produto pode ficar com referência divergente do grupo/subgrupo atuais.
- `SEXO_TIPO` é enviado como descrição e resolvido pelo interceptor contra `W_SEXO_TIPO`.
- `COR_FABRICANTE` = custom `familia_variante` (coluna de 20 caracteres, aceita nulo).
- Na leitura de cores, a coluna `COD_RGB` do Linx da Lofty **não contém RGB** — traz o caminho da foto ou `'SEM RGB'`, então as cores tendem a entrar na uFlow com branco `[255,255,255]`.
- VPN e validação do `x-interceptor-api-token` estão comentadas no código.
- Código de barras (procedure `LFT_GERA_COD_BARRAS`) desativado — e o documento é explícito de que `status_atual` **não** é gatilho de barra nesta integração.
## Auditoria e monitoramento
Sim. Ao final de cada produto (só em `v1`), `POST /audit/:partnerId/integration` com `{ executionId, productId, productReference, timestamp }`; o uConnect grava em Mongo deduplicando por parceiro+dia+item e guarda um "raw" buscado na uFlow. Falha de auditoria é engolida e não quebra a integração. Há cron de validação de auditoria no uConnect (23:00 UTC / 20:00 BRT) comparando uFlow × Linx. Toda execução fica em `integration-executions` na uFlow; erros notificam Discord (devs ou CS) apenas em `staging`/`v1`.
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
- Inventário de arquivos do repositório `integration-lofty-linx` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
