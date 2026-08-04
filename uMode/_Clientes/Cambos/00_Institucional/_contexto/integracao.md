# Cambos · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
Cambos
### ERP / sistema integrado
SPI
### Repositório de código
`github.com/UmodeApp/integration-cambos-spi` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-cambos-spi`
### Documentação de referência
- `docs\documentacao-geral-cambos-spi.md` — 38 KB
- `.claude\skills\docs-integracao-cambos-spi\SKILL.md` — 11 KB
- `README.md` — 0 KB
### Status da integração
Em produção — o documento descreve o stage `v1` (produção) com crons ativos nos dois sentidos.
## Arquitetura
### Direções de integração
Ambas. Escrita uFlow → SPI cobre **produtos** (criação e depois a ficha completa). Leitura SPI → uFlow cobre dados de referência: **cores, banhos, fornecedores, tecidos e aviamentos**.
### Mecanismo
**API HTTP do SPI** (axios, base `SPI_API_URL`) para os dois sentidos — **não há conexão com banco de dados do cliente**. Lado uFlow, **API REST** (axios) autenticada por `api_token` na query string, derivado do JWT recebido. Enfileiramento por **SQS FIFO**. Algumas funções devolvem **HTML** (templates `pug`) como telas de operação manual.
### Ambiente e execução
**AWS Lambda** (Serverless Framework v3, Node.js 16, TypeScript, região `us-east-2`). **6 filas SQS FIFO**: `product-queue` (escrita) + `color-queue`, `banho-queue`, `fabric-queue`, `accessory-queue`, `supplier-queue` (leitura) — todas `batchSize: 1`, timeout 900s. Padrão `enqueue*` + worker `*FromQueue`. Stages `dev`, `staging`, `v1`; **crons só no `v1`**.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Produtos: `POST /Produto` com a identificação mínima (`codigoumode`, `iddetalhe`, `idgenero`, `idtamanho`, `idtipo`, `idmodelagem`) e depois `PUT /Produto/{codigo}` com a ficha completa — dados de estilo/modelagem, responsáveis, lacres/aprovações, observações, campos de acabamento (linha de costura, travete, caseado, passante, bordado) e as sublistas `AviamentoList`, `TecidoList` e `LavagemList`.
### Gatilho e frequência
Cron `enqueueProducts` a cada 30 min, **seg–sex, 24h por dia**, até **30 produtos por execução**. Produtos pendentes no fim de semana só entram na fila na segunda. Também manual por lista de IDs, por ID único, ou `GET /products/{id}/force` (direto, sem fila e sem filtro). `MessageGroupId` fixo `sync_product` (serial); dedup por `<productId>-<updated_at>`. O throttle de 10 min **não** se aplica à escrita.
### Regras e validações
Fila automática (AND): `spi_last_integration` vazio, produto não deletado e **Validação id 131** em `passed`/`warning` (modelagem, `tipo`, `genero`, `familia_tamanho`, `detalhe`, `liberado_integracao` e material principal na location 1990).
`detalhe`, `genero`, `familia_tamanho` e `tipo` são **revalidados dentro do código** na escrita — falta gera erro mapeado ("Preencha o campo X do produto"), que vai para o CS.
Insert vs. update pela `reference` do SPI já gravada: sem referência → `POST` + gravação da referência + `PUT`; com referência → só `PUT`. Produto novo gera **dois registros** no relatório (`created` + `updated`).
A ficha completa usa **uma única variante** — a ativa mais recente (não deletada); sem variante ativa, erro "No active variant found for product id X".
Conversões: preços/custos via `getCostValue` (limpa símbolos, vírgula → ponto, vazio → `0`); HTML → texto puro em observações; campos "SIM/NÃO" convertidos para `1`/`0`.
Aviamentos e tecidos **sem referência são silenciosamente pulados** (apenas logados); `principal` do tecido é `'S'` só quando a localização é exatamente `PRINCIPAL`.
`idcliente` vem de `product.collection.reference` e é convertido **sem validação** (pode virar `NaN`); `idtecido` é sempre `0`; `datapedido` é sempre a data atual.
No sucesso: grava a referência, marca `spi_last_integration`, limpa `integration_error` e `non_mapped_error` — mas **não limpa** `silent_error`.
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores (`/Cores`), banhos de aviamento (`/BanhosAviamento`, importados **como Cores** na uFlow), fornecedores (`/FornecedoresAviamento`), tecidos (`/Tecidos` → Material tipo fabric) e aviamentos (`/Aviamentos` → Material tipo accessory).
### Gatilho e frequência
Crons diários escalonados: cores 00:00, banhos 00:30, fornecedores 01:00, tecidos 01:30, aviamentos 02:00 (BRT). Uma mensagem por tipo, `MessageGroupId` fixo (`sync_cor`, `sync_banho`, `sync_tecido`, `sync_aviamento`, `sync_fornecedor`). Chunking de 500 só quando o payload traz lista explícita de itens; no cron a paginação real acontece na leitura do SPI.
### Regras e validações
Antes de enfileirar: **bloqueio de concorrência** por tipo (com exceção para execução stale > 1h) **e throttle de 10 minutos** desde o último `executed_at` — o throttle vale só para leitura.
Cutoff incremental: `start_datetime` → `created_at` da **última execução finalizada** (`getSaoPauloDate` subtrai **3h fixas**, ignora horário de verão) → piso `1970-01-01`, exceto **FORNECEDOR, cujo piso é `2000-01-01`**. A data enviada é **date-only**, o que combinado com o −3h **pode reprocessar o dia inteiro**.
Todos os registros importados entram como `active: true`; **não há fluxo de inativação/baixa** — item removido no SPI não é desativado na uFlow.
Cores: `name` = `"<descricao> <tom>"` **sem trim** (sobra espaço se `tom` vazio); matching por `reference` × `codigo`; ignora se o `name` é idêntico; `rgb` sempre branco; `book` recebe o pantone.
Banhos: código com prefixo fixo **`BAN-<id>`** (evita colisão com as cores normais) e `integration_id` com o id puro; no update atualiza **só o `name`**.
Fornecedores: só `reference` + `name`; sem filtros; se existe, **sempre atualiza**; registra a lista de referências como `pending` (os outros fluxos usam só o sentinela).
Tecidos: `material_type_name` fixo `INDEFINIDO`, fornecedor fixo **"Cambos"** com unidade `m`; sem `codigo_cor`, cria variante `"SEM COR"`.
Aviamentos: fluxo mais complexo, cruza **5 endpoints auxiliares**; exclui unidades `['BO','CN','FR','IN','JD','ML','MT²','Rl']`; converte unidades por `unidadeMapping`; identifica por `codigo` (não `id`); a "cor" da variante é o banho `BAN-<id>`.
Erro de item individual não derruba a importação; erro estrutural força a execução para `error`.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
Nenhuma. O SPI é acessado **exclusivamente pela API HTTP** — o documento é explícito quanto a não haver conexão com banco do cliente, e não existe documento de tabelas neste repositório (diferente da Baw, que tem `tabelas-do-linx-baw.md`). O mapeamento documentado é por **endpoint/recurso do SPI** (12 endpoints, ver `docs/documentacao-geral-cambos-spi.md`, Seção 4).
### Endpoints externos utilizados
SPI: `POST /Produto`, `PUT /Produto/{codigo}`, `GET /Cores` (paginado), `GET /Tecidos` (paginado), `GET /Aviamentos` (paginado), `GET /BanhosAviamento`, `GET /FornecedoresAviamento`, `GET /MateriaisAviamento`, `GET /DetalhesAviamento`, `GET /TamanhosAviamento`, `GET /TiposAviamento`, `GET /Modelagens` (health check / import manual, sem cron). uFlow: `/products`, `/colors`, `/suppliers`, `/materials`, `/integration-executions`. Outros: AWS SQS FIFO e webhook do Discord.
## Particularidades deste cliente
- **O SPI não tem autenticação nas chamadas** — o documento registra explicitamente que o código não envia header `Authorization`, token nem `api_token` ao SPI; o único comportamento do cliente HTTP é injetar `updatedAtAfter=1970-01-01` em GETs que não o tenham. É o ponto de risco técnico mais relevante do repositório.
- Escrita em **duas etapas obrigatórias** (`POST` para criar e obter o código, depois `PUT` com a ficha completa) — os outros clientes não têm esse padrão de duas chamadas.
- A ficha do SPI é **por variante única**: só a variante ativa mais recente é enviada, então o produto no SPI representa uma cor só.
- Existe o conceito de **"banho"** (acabamento de aviamento), inexistente nos outros ERPs; o SPI força modelá-lo como **Cor** na uFlow com prefixo `BAN-`, o que cria dependência de **ordem entre crons** (banhos às 00:30 antes de aviamentos às 02:00).
- **Lacres** (aprovações de produto) alimentam `lacre1/2/3`, `datapilotocliente` e `ajuste` a partir do último `product_approval` não deletado — vocabulário e etapa próprios da Cambos.
- Entre Baw, Cambos e Luiza Barcelos, é a única com **throttle de 10 minutos** entre execuções de leitura, e a única com **piso de data distinto por tipo** (`2000-01-01` para fornecedores).
- Runtime **Node.js 16** (Baw e Luiza Barcelos estão em 18).
- Contrato do SPI tem um **typo** na paginação (`meta.currantpage`), replicado no código.
- Paginação heterogênea: `/Cores`, `/Tecidos` e `/Aviamentos` são paginados; os auxiliares e `/BanhosAviamento`/`/FornecedoresAviamento` não.
- Tecidos entram todos com fornecedor fixo **"Cambos"** e tipo `INDEFINIDO` — a integração não traz fornecedor real de tecido.
- Única do lote com **telas de operação manual funcionais** (pendências com checkbox e botão "Enviar" que dispara o enfileiramento).
## Auditoria e monitoramento
Toda execução em `integration-executions` da uFlow, com o **mesmo `INTEGRATION_ID` para todos os tipos** no mesmo stage — os tipos se distinguem pelo campo `integration_type`. Status calculado por `getIntegrationStatus` (`pending`/`executing`/`success`/`partial_success`/`error`), com `finish('error')` forçado em erro estrutural para não deixar a execução presa. Erros gravados em `integration_error` / `non_mapped_error` (só para tipos de escrita) e notificados por **webhook no Discord** (devs ou CS conforme `shouldNotifyDevs`), só em `staging`/`v1`. Telas `/*/pendings` e `/products/with-error` para operação manual. Sem auditoria pós-integração comparando SPI × uFlow.
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
- Inventário de arquivos do repositório `integration-cambos-spi` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
