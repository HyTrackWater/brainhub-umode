# Osklen · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
Osklen
### ERP / sistema integrado
Linx
### Repositório de código
`github.com/UmodeApp/integration-osklen-linx` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-osklen-linx`
### Documentação de referência
- `docs\documentacao-geral-osklen-linx.md` — 63 KB
- `docs\tabelas-do-linx-osklen.md` — 39 KB
- `.claude\skills\docs-integracao-osklen-linx\SKILL.md` — 9 KB
### Status da integração
Em produção — o documento descreve o stage `v1` (produção) com crons ativos; `dev`/`staging` só por HTTP manual.
## Arquitetura
### Direções de integração
Ambas. Escrita (uFlow → Linx) em **três momentos** (cadastro do produto; variantes/cores e materiais; código de barras). Leitura (Linx → uFlow): cores, fornecedores, grades e materiais.
### Mecanismo
AWS Lambda (Serverless v3, Node.js 18, TypeScript, us-east-2) + 5 filas SQS FIFO (`batchSize: 1`, timeout 900s). Toda conversa com o banco do Linx passa pelo interceptor/uConnect por HTTP (`INTERCEPTOR_BASE_URL`, header `x-interceptor-api-token`, timeout 120s), inclusive execução de stored procedure. uFlow via API REST (axios, `api_token` dentro do JWT). Leitura serve-se de snapshot MongoDB gerado pelo uConnect.
### Ambiente e execução
Serverless; padrão `enqueue*` (cron ou HTTP) → SQS FIFO → `*FromQueue`. Crons só em `v1`. `PARTNER_ID` `6723bb63c75700acba208eb2`. Credenciais do banco ficam no cadastro do parceiro no uConnect, não no código.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Momento 1: PRODUTOS, PROP_PRODUTOS (8 propriedades), PRODUTOS_PRECOS (21 linhas zeradas), PRODUTO_FICHA_VERSAO — mais a tabela auxiliar `PRODUTOS_DESIGN_OSK`. Momento 2: PRODUTO_CORES, PRODUTO_VERSAO_MATERIAL, PRODUTO_VERSAO_MATERIAL_COR e PRODUTOS_PRECO_COR (as duas últimas por variante). Momento 3: PRODUTOS_BARRA, via procedure. Rota de operação dedicada, PRODUTOS_MODELO, PRODUTOS_OPE_EXTRA, PRODUTOS_FOTO e PRODUTOS_INDICADOR_CFOP não são integradas.
### Gatilho e frequência
Cron `enqueueProducts` a cada 30 min, 04:00–19:30 BRT, seg–sex, até 30 produtos por execução (FIFO serial, dedup `<id>-<updated_at>`). Dentro de cada sincronização, os três momentos são **reavaliados**: Momento 1 sempre; Momento 2 se `liberado_integracao` (6810) estiver preenchido; Momento 3 se `status_atual` (5276) for `K;3` ou `F;3`. Força: lista de IDs ou `GET /products/{id}/force` (sem fila), ignorando os filtros.
### Regras e validações
Fila (AND): `last_integration` (6811) vazio, `linx_integration_error` (6812) vazio, não deletado, Validação 141 ("Integração Linx - Momento 1") em `passed`/`warning` — 14 itens, todos bloqueantes. No Momento 2, só entram variantes não deletadas e com `cor_conferida` (7086); variante sem cor gera erro silencioso. Insert vs. update pela presença de `reference`; update só grava colunas "sujas" (`undefined` não apaga, mas `null` explícito **pode** gravar NULL) e remove `DATA_CADASTRAMENTO`. Referência = sequencial puro lido/incrementado atomicamente em `SEQUENCIAIS` (`SEQ_PROD_OSKLEN.PRODUTO`). Contas contábeis vêm de `PARAMETROS` e **sobrescrevem** o corpo. `TABELA_OPERACOES` resolvida por comparação normalizada (CR/LF e NBSP) contra `PRODUTOS_TAB_OPERACOES`, com cache no interceptor; rota inexistente derruba o produto. Preços: flag `_shouldUpdate` só liga com valor diferente de zero — a uFlow nunca zera preço no Linx. Erro no código de barras interrompe o produto (as outras subetapas não).
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores (`CORES_BASICAS`), fornecedores (`FORNECEDORES`), grades (`PRODUTOS_TAMANHOS`) e materiais (`MATERIAIS` + `MATERIAIS_CORES` + `COLECOES`).
### Gatilho e frequência
Crons diários (BRT): cores 06:00, fornecedores 06:30, materiais 07:00, grades 07:30. O snapshot no Mongo é gerado por cron do uConnect às 23:00 UTC (20:00 BRT) com troca segura de lote — as leituras da manhã consomem a foto da noite anterior.
### Regras e validações
Carga inicial em 01/01/1970 para as quatro tabelas; depois incremental por `DATA_PARA_TRANSFERENCIA` com corte na `created_at` da última execução finalizada com sucesso (falha não avança a janela); IDs que erraram voltam como `errorsReferences` em condição "OU" com a data. Bloqueio de concorrência com liberação de execução abandonada (>1h). Erro por registro não interrompe — **exceção: grades não têm tratamento por item**. Cores: só `USO_MATERIAIS` ou `USO_PRODUTOS`; update só do nome; `rgb` sempre branco. Fornecedores: whitelist de 9 tipos, inativos não entram (mas também não são desativados na uFlow), casamento **pelo nome**. Grades: tamanhos com ponto ignorados e `items_csv` removido no update. Materiais: whitelist de 14 grupos, `INNER JOIN MATERIAIS_CORES`/`COLECOES`, inativos descartados e unidades `KT`, `LT`, `M3`, `ML`, `PL`, `RM` excluídas; variantes agrupadas sob um material pai.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
16 tabelas documentadas em `docs/tabelas-do-linx-osklen.md`. Escrita (10): produto e propriedades (PRODUTOS, PROP_PRODUTOS), design (PRODUTOS_DESIGN_OSK), preços (PRODUTOS_PRECOS, PRODUTOS_PRECO_COR), cor/variante (PRODUTO_CORES), ficha/empenho (PRODUTO_FICHA_VERSAO, PRODUTO_VERSAO_MATERIAL, PRODUTO_VERSAO_MATERIAL_COR), código de barras (PRODUTOS_BARRA). Leitura (6): CORES_BASICAS, FORNECEDORES, PRODUTOS_TAMANHOS, MATERIAIS, MATERIAIS_CORES, COLECOES. Também são tocadas, sem detalhamento naquele arquivo: PARAMETROS, SEQUENCIAIS, PRODUTOS_TAB_OPERACOES (consulta de rota) e OSK_INTEGRACAO_UMODE (trilha de auditoria).
### Endpoints externos utilizados
Interceptor/uConnect: rotas de escrita por tabela, `POST /interceptor/linx/:partnerId/execute-procedure` (procedure `LX_OSK_GERA_CODIGO_BARRAS`), `DELETE /interceptor/linx/osklen/product-route-operation-cache` (limpeza do cache de rotas), leituras de cores/fornecedores/grades/materiais e a rota de auditoria de integração. API REST da uFlow (`API_URL`). Webhook do Discord (`DISCORD_URL`). Rotas HTTP próprias: força por lista de IDs, `GET /products/{id}/force`, `/products/with-error`.
## Particularidades deste cliente
- Entre Lofty Style, NK STORE e Osklen, é o único com o modelo de **três momentos** e gatilhos distintos (Validação 141 → `liberado_integracao` → `status_atual` em `K;3`/`F;3`), e o único com filtro por variante via `cor_conferida`. A NV também é dividida em três momentos, com gate próprio (os "3 SIMs") — não é padrão exclusivo da Osklen na carteira.
- Entre Lofty Style, NK STORE e Osklen, é o único com **código de barras ativo**: procedure `LX_OSK_GERA_CODIGO_BARRAS` no Linx (toda a lógica do EAN-13 mora na procedure), idempotente por produto+cor, e pulada se o upsert retornou erro de `PRODUTOS_TAMANHOS` inexistente.
- Referência é **sequencial puro** de `SEQUENCIAIS` (não código composto por grupo/subgrupo como Lofty e NK).
- Em PRODUTO_CORES, `COR` recebe `colors[0].reference` e `COR_PRODUTO` o SKU — diferente de Lofty e NK, que usam o SKU nas duas colunas.
- 21 códigos de tabela de preço, com só 4 valores reais (`MO` ← `mao_obra`, `99` ← `custo_total`, `60` ← `preco_venda`, `PC` ← `tabela_pc`), enviados em lotes de 2; por desenho **não é possível zerar um preço do Linx a partir da uFlow**.
- Tabela auxiliar exclusiva `PRODUTOS_DESIGN_OSK` para `linguagem`/`localizacao`/`modelagem` (e `MODELAGEM` em `PRODUTOS` é sempre `null`).
- Trilha de auditoria gravada **dentro do próprio Linx** (`OSK_INTEGRACAO_UMODE`), com o SQL exato executado.
- Cadastro de rotas do Linx contém CR/LF e NBSP, exigindo resolução normalizada com cache e endpoint de invalidação.
- Trava operacional (não imposta por código): variante já integrada no Momento 2 não deve ser deletada na uFlow — cancelar mudando o status para `RESERVA TÉCNICA`, porque a etapa de cor não apaga registros no Linx.
- `SEXO_TIPO` por mapa fixo `{F:3, M:2, U:4}`.
- A parse monetária pt-BR remove pontos — um valor como `12.50` viraria `1250`.
## Auditoria e monitoramento
Sim, em duas camadas. (1) No Linx: cada insert/update/delete/procedure grava uma linha em `OSK_INTEGRACAO_UMODE` com ID uMode, usuário do banco, referência, data/hora, tipo de operação e o SQL executado. (2) Rota de auditoria do interceptor chamada ao final de cada produto, só em `v1`, com `{ executionId, productId, productReference, timestamp }`, gravando um item por (parceiro, dia, produto) e sobrescrevendo só se o timestamp for mais novo; falha de auditoria é ignorada. Há cron de validação no uConnect (~23:00 UTC / 20:00 BRT) comparando uFlow × Linx e gerando alertas de divergência. Execuções em `integration-executions` na uFlow e alertas no Discord (devs vs. CS) em `staging`/`v1`.
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
- Inventário de arquivos do repositório `integration-osklen-linx` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
