# NK STORE · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
NK STORE
### ERP / sistema integrado
Linx
### Repositório de código
`github.com/UmodeApp/integration-nk-linx` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-nk-linx`
### Documentação de referência
- `docs\documentacao-geral-nk-linx.md` — 60 KB
- `docs\tabelas-do-linx-nk.md` — 45 KB
- `.claude\skills\docs-integracao-nk-linx\SKILL.md` — 7 KB
### Status da integração
Em produção — o documento descreve o stage `v1` (produção) com crons ativos; `dev`/`staging` só por HTTP.
## Arquitetura
### Direções de integração
Ambas. Escrita (uFlow → Linx): produto, variantes, ficha técnica, medidas e rota de operação. Leitura (Linx → uFlow): cores, fornecedores, grades e materiais.
### Mecanismo
AWS Lambda (Serverless, Node.js 18, TypeScript, us-east-2) + 6 filas SQS FIFO (`product`, `color`, `supplier`, `grid-size`, `material`, `grupo`; `batchSize: 1`). **Acesso direto ao banco** SQL Server do Linx via Knex (serviço `LinxDB.nk`, `requestTimeout` 60s), com as Lambdas dentro de uma VPC (security group + 2 subnets) — sem interceptor e sem abertura/fechamento de VPN. uFlow via API REST (axios, JWT).
### Ambiente e execução
Serverless; workers com timeout 900s. Padrão `enqueue*` (cron ou HTTP) → SQS FIFO → `*FromQueue`. Crons só em `v1`. Funções manuais: `forceSyncProduct`, `forceImportSync*`, telas de pendências/erros, `healthCheck`. Os fluxos de Campos Personalizados e de Grupos existem no código mas com crons comentados (não rodam em produção).
## Escrita (uMode → sistema do cliente)
### O que é enviado
15 tabelas: PRODUTOS, PROP_PRODUTOS, PRODUTOS_TAB_OPERACOES + PRODUTO_OPERACOES_ROTAS (rota, quando `rota_operacao` preenchido) + `UPDATE PRODUTOS.TABELA_OPERACOES`, PRODUTOS_PRECOS, PRODUTO_FICHA_VERSAO, PRODUTO_VERSAO_MATERIAL, PRODUTOS_TAB_MEDIDAS, PRODUTOS_MEDIDAS + MEDIDAS; por variante: PRODUTO_CORES, PRODUTO_VERSAO_MATERIAL_COR, PROP_PRODUTO_CORES, PRODUTOS_PRECO_COR. PRODUTOS_BARRA está desativado.
### Gatilho e frequência
Cron `enqueueProducts` a cada 30 min, 04:00–19:30 BRT, seg–sex, até 30 produtos por execução; FIFO serial com dedup `<id>-<updated_at>` (janela de 5 min). Endpoints de força por lista de IDs ou ID único ignoram o filtro de pendência.
### Regras e validações
Fila (AND): `last_integration` (4723) vazio, `linx_integration_error` (4971) vazio, produto não deletado e Validação 137 em `passed`/`warning` (22 itens; 3 são aviso). Insert vs. update: sem `reference` → insert; com `reference`, valida no Linx o par produto + propriedade `00102` (ID uMode) — divergência, duplicidade ou ausência do `00102` lançam erro. Código do produto gerado como `[grupo 2][subgrupo 2][sequencial 4]` (8 dígitos, sem pontos) com incremento em `PRODUTOS_SUBGRUPO`. No update, `PRODUTO`, `DATA_CADASTRAMENTO` e `GRUPO_PRODUTO` nunca são alterados e só campos alterados são gravados. Label de `subgrupo` é resolvido **filtrando pelo grupo** do produto. Erros mapeados/não mapeados interrompem o produto; silenciosos (ex.: material inexistente em `MATERIAIS`, `XFK13435`, empenho duplicado, nome de medida >40 chars) seguem. `trimAllValues` em tudo que vem do Linx (colunas CHAR com padding). PRODUTOS_PRECOS é insert-only; empenhos e medidas órfãos são deletados; propriedades não têm delete.
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores (`CORES_BASICAS`), fornecedores (`FORNECEDORES`), grades (`PRODUTOS_TAMANHOS`) e materiais (`MATERIAIS`, com apoio de `MATERIAIS_CORES`, `MATERIAIS_COMPOSICAO`, `ESTOQUE_MAT_PECA`, `FORNECEDORES` e da função `FX_NK_CUSTO_FICHA_TECNICA`).
### Gatilho e frequência
Crons diários (BRT): cores 00:00, fornecedores 00:30, materiais 01:00, grades 01:30. Leitura direto no banco do Linx (não há snapshot intermediário). Modo forçado reimporta itens específicos ignorando filtros de tipo e data.
### Regras e validações
Carga inicial por tabela: cores e grades em 01/01/1970; fornecedores e materiais em 01/01/2023. Depois, incremental por `DATA_PARA_TRANSFERENCIA` com corte na última execução finalizada com sucesso, **menos 1 hora** de margem; reprocesso dos registros que erraram. Bloqueio de concorrência com liberação de execução `stale` (>1h presa sem finalizar). Erro por registro não interrompe (`partial_success`); erro estrutural é marcado explicitamente como `error` para não travar os dias seguintes. Cores: update só do nome; `rgb` fixo `'[255,255,255]'`. Fornecedores: whitelist de 6 tipos e **apenas `name` e `reference`** são importados. Grades: só `GRADE LIKE '%*%'` e com `GRADE_BASE`; tamanhos só na criação. Materiais: só grupos `TECIDOS`/`AVIAMENTOS`, precisam ter cor, unidade `ENV` descartada, nome = `DESC_MATERIAL + COD_FORNECEDOR`, largura vinda do menor valor positivo em `ESTOQUE_MAT_PECA`.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
23 tabelas documentadas em `docs/tabelas-do-linx-nk.md`. Escrita (15): produto e propriedades (PRODUTOS, PROP_PRODUTOS, PROP_PRODUTO_CORES), rota de operação (PRODUTOS_TAB_OPERACOES, PRODUTO_OPERACOES_ROTAS), preços (PRODUTOS_PRECOS, PRODUTOS_PRECO_COR), ficha/empenho (PRODUTO_FICHA_VERSAO, PRODUTO_VERSAO_MATERIAL, PRODUTO_VERSAO_MATERIAL_COR), medidas (PRODUTOS_TAB_MEDIDAS, PRODUTOS_MEDIDAS, MEDIDAS), cor/variante (PRODUTO_CORES), código de barras (PRODUTOS_BARRA, desativado). Leitura (8): CORES_BASICAS, FORNECEDORES, PRODUTOS_TAMANHOS, MATERIAIS, MATERIAIS_CORES, MATERIAIS_COMPOSICAO, ESTOQUE_MAT_PECA, COLECOES. Também são consultadas TABELAS_PRECO, PRODUTOS_SUBGRUPO, TABELA_LX_NCM, TABELA_LX_CEST, CEST_NCM, PARAMETRO_CONTA_CONTABIL_UMODE e PARAMETRO_CONTA_CONTABIL_EXCECAO_UMODE.
### Endpoints externos utilizados
API REST da uFlow (`API_URL`/`UMODE_URL`). Webhook do Discord (`DISCORD_URL`). API da GS1 Brasil (`GS1_API_URL`, OAuth) — **não é chamada em produção** hoje. O Linx é acessado por conexão de banco (Knex/SQL Server), não por endpoint HTTP. Endpoints HTTP próprios para força/telas/`healthCheck`.
## Particularidades deste cliente
- Entre Lofty Style, NK STORE e Osklen, é a única que **não usa o interceptor/uConnect** — as Lambdas rodam em VPC e falam direto com o SQL Server (NV e VIX também acessam o banco direto, cada uma por caminho próprio).
- Entre todos os clientes com repositório lido, é a única que integra **medidas**: `PRODUTOS_TAB_MEDIDAS` sempre, mas as linhas (`PRODUTOS_MEDIDAS`) só quando o label de `status_produto` é exatamente `'APROVADO PARA COLECAO'`; o catálogo global `MEDIDAS` só cresce.
- Única com **rota de operação viva** entre Lofty Style, NK STORE e Osklen: copia um registro-modelo do Linx (`rota_operacao` = código da rota-modelo), sobrescreve custos com beneficiamentos da uFlow e adiciona a etapa de costura por griffe (`ZE`→05/05/297, `38`→100/950/950, `37`→60/60/5520; griffe fora do mapa não gera costura, silenciosamente).
- Contas contábeis têm **camada de exceção por coleção** (`PARAMETRO_CONTA_CONTABIL_EXCECAO_UMODE` por `INDICADOR_CFOP` + `COLECAO`, com fallback para a tabela principal).
- Entre Lofty Style, NK STORE e Osklen, é a única que envia **preço real por cor**: `01` atacado, `02` varejo, `03` custo da peça, `04` custo total — com exceção COURO somando 6,5% sobre o custo da peça.
- `INDICADOR_CFOP` = 13 para uniforme (`brand.id 3207`, marca ACOES), 11 para griffe `NK FORNECEDOR`, senão 10; `REVENDA` só se griffe = `ZC`; piloto (`piloto_producao = 'PI'`) muda `REDE_LOJAS` para `'PL'`.
- `SEXO_TIPO` é fixo `3` e `LINHA` fixa `'NACIONAL'`.
- Variante com `status_variante = '0'` é inativada com `FIM_VENDAS` retroativo (1990).
- Grades só entram se o nome contiver asterisco.
- Se reativado, o código de barras viria da **API externa da GS1** (GTIN-13), não de sequência interna do Linx.
## Auditoria e monitoramento
Não há serviço de auditoria pós-integração documentado (nada equivalente ao `/audit` de Lofty/Osklen nem tabela de trilha no Linx). O monitoramento se dá pela tabela `integration-executions` da uFlow (relatório de criados/atualizados/erros e status `pending`/`executing`/`success`/`partial_success`/`error`), pelas notificações no Discord (devs para erro não mapeado, CS para mapeado e silencioso, só em `staging`/`v1`), pelas telas de pendências/erros e pelo endpoint `healthCheck`.
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
- Inventário de arquivos do repositório `integration-nk-linx` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
