# VIX · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
VIX
### ERP / sistema integrado
Linx
### Repositório de código
`github.com/UmodeApp/integration-vix-linx` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-vix-linx`
### Documentação de referência
- `docs\documentacao-geral-vix-linx.md` — 44 KB
- `docs\tabelas-do-linx-vix.md` — 34 KB
- `docs\migracao-smb-cliente.md` — 28 KB
- `docs\relatorio-incidente-imagens-vix.md` — 12 KB
- `.claude\skills\docs-integracao-vix-linx\SKILL.md` — 6 KB
- `README.md` — 0 KB
### Status da integração
Em produção — o documento geral descreve os agendamentos ativos do stage `v1` e o relatório de incidente confirma a integração de imagens restabelecida e em funcionamento desde 05/05/2026.
## Arquitetura
### Direções de integração
Ambas. Escrita (uFlow → Linx): produtos, com a particularidade de que **cada variante da uFlow vira um produto no Linx**, incluindo modelagem, propriedades, custos extras de fornecedor, fotos, CFOP, preços, cores, código de barras, ficha-versão e materiais. Leitura (Linx → uFlow): cores básicas e materiais com suas cores e fornecedores.
### Mecanismo
Acesso direto ao banco do Linx (SQL Server via Knex, serviço `LinxDB.vix`), filas SQS FIFO, API REST da uFlow via axios com JWT, e **gravação de imagens por SMB** — hoje delegada a um microserviço próprio. Conectividade de rede por VPC + VPN acionada via uConnect. Alerta por webhook do Discord.
### Ambiente e execução
AWS Lambda (Serverless, Node.js 16, código em **TypeScript** via `serverless-plugin-typescript`, us-east-2), com 3 filas SQS FIFO (`product-queue`, `color-queue`, `material-queue`), `batchSize: 1` e timeout 900 s. As Lambdas executam a lógica diretamente — não há worker intermediário. O consumidor de produtos roda **dentro de uma VPC** e, a cada lote, abre e fecha a VPN via uConnect: chama `vpn-connect` ao processar o primeiro produto e `vpn-disconnect` no último, deduzindo "primeiro/último" do campo `TOTAL` da execução versus a quantidade ainda `pending`. Após o incidente de 2026, a entrega de imagens passou a ser feita por um microserviço NestJS em instância EC2 dedicada com `samba-client` nativo, chamado por HTTP pela Lambda legada.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Modelagem (PRODUTOS_MODELO), produto (um por variante), propriedades, operações extras de fornecedor, fotos de produto, indicador CFOP por filial, linhas de tabela de preço, cores, códigos de barras EAN-13, ficha-versão e ficha de materiais (material e material×cor).
### Gatilho e frequência
Cron `cron(0/30 11-20 ? * MON-FRI *)` = a cada 30 min, das 08:00 às 17:30 BRT, seg–sex; até 30 produtos por execução, excedente na execução seguinte. Uma mensagem SQS por produto, `MessageGroupId` fixo `sync_product` → processamento estritamente serial. Também disponíveis `forceSyncProduct` e `syncOperationRoute` por HTTP. Sem cron em `dev`/`staging`.
### Regras e validações
- Fila: Validação 59 em `passed` ou `warning`, `linx_last_integration` (3009) vazio, `linx_integration_error` (4918) vazio e produto fora das coleções 5442 (Matérias Primas) e 5443 (Produtos Acabados).
- Ordem fixa de 12 tabelas; erro mapeado ou não mapeado **interrompe** o produto e nenhuma tabela seguinte é processada; erro silencioso (7763) só pula a tabela afetada e o produto pode terminar com `linx_last_integration` preenchido.
- Variante sem cor é ignorada com erro silencioso; variante sem `sku` em PRODUTO_CORES lança erro.
- Variante deletada é ignorada, exceto se tiver `cod_linx` — nesse caso é atualizada; e o cancelamento no Linx exige `status_produto` = `'I'` ou `'R'`, situação em que **só** a coluna `STATUS_PRODUTO` é atualizada.
- `subgrupo` (3114) e `subcategoria` (3022) são campos com dois valores separados por `;`: no subgrupo usa-se apenas o segundo; na subcategoria a escolha depende da categoria (PRINT/SOLID → 1º valor; ESTAMPADO/LISO → 2º).
- Contas contábeis vêm dinamicamente de `PARAMETROS`; `ID_CEST_NCM` de `TABELA_LX_NCM`; filiais de `FILIAIS`; tabelas de preço de `TABELAS_PRECO` (só insert, sem update, e sem valor).
- Código de barras: gerado por regra de workflow (linha `USA` nunca gera; workflows 1339, 1245 pos.≥6, 1235 pos.≥3), montado como prefixo EAN_13 de `PARAMETROS` + sequencial de `SEQUENCIAIS` + dígito verificador; se o resultado não tiver 13 caracteres é rejeitado com erro, e há 4 novas tentativas em caso de falha na primeira geração.
- PRODUTOS_OPE_EXTRA só integra fornecedores com `definicao_custo` `BORDADO` ou `FACÇÃO`, e erro se houver dois com a mesma definição. `DESC_USO_MATERIAL` é truncado em 40 chars. Empenho existente no Linx e ausente na uMode é excluído do Linx; foto existente no Linx e ausente na uFlow também.
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores básicas (código, nome, `rgb` fixo branco, `active` true) e materiais com tipo (`fabric`/`accessory`), NCM, observações, data de cadastro, status ativo, unidades, fator de conversão, e uma variante por cor de material com composição, fornecedor e custo.
### Gatilho e frequência
Crons diários: cores 00:02 BRT (`cron(2 3 * * ? *)`) e materiais 00:30 BRT (`cron(30 3 * * ? *)`). Cada `enqueueImport` cria uma única mensagem com o lote, dividida em mensagens de até 500 itens quando necessário. Também há `forceImportSyncColors`/`forceImportSyncMaterials` por HTTP. Sem cron em `dev`/`staging`.
### Regras e validações
- Janela incremental com cutoff da **última execução finalizada com sucesso** (`success`/`partial_success`); execução `error` não avança a janela, então o dia seguinte recupera os registros. A rota de create/update da uFlow é idempotente por referência/código.
- Cargas iniciais: cores `new Date(0)` (01/01/1970); materiais 01/01/2023.
- Bloqueio de concorrência por tipo de tabela, com exceção de execução stale (em `executing`/`pending`, sem `executed_at`, criada há mais de 1 hora).
- Cores: matching pelo código `COR`; se existir, só o nome é atualizado.
- Materiais: unidades `CRT` e `FARDO` são ignoradas (sem equivalente na uFlow); `type` decidido pelo `GRUPO` — `AVIAMENTOS`, `EMBALAGEM LOJA`, `EMBALAGENS`, `ESTOQUE REGULADOR`, `MAT. CONSUMO` → `accessory`, o resto → `fabric`; `name` = `${MATERIAL} ${DESC_MATERIAL}`; `active` = inverso de `INATIVO`; `OBS`+`COMPRIMENTO`+`LARGURA` concatenados em `observations`.
- `book` é sempre enviado como `'MATERIAIS_CORES'`, para que cores criadas pela importação de materiais (e não pela de cores) sejam identificáveis na uFlow.
- Erro por registro vira `partial_success` e não interrompe os demais; erro estrutural é marcado explicitamente como `error` (terminal); registros com erro são relidos na execução seguinte até entrarem com sucesso.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
17 tabelas com schema documentado em `docs/tabelas-do-linx-vix.md`, dividido em "escrita" e "leitura" — sem cópia aqui. Escrita (12): **produto/modelagem** — PRODUTOS, PRODUTOS_MODELO, PROP_PRODUTOS, PRODUTO_CORES, PRODUTO_FICHA_VERSAO; **fiscal e preço** — PRODUTOS_INDICADOR_CFOP, PRODUTOS_PRECOS; **custo de fornecedor** — PRODUTOS_OPE_EXTRA; **imagem** — PRODUTOS_FOTO; **identificação** — PRODUTOS_BARRA; **materiais do produto** — PRODUTO_VERSAO_MATERIAL, PRODUTO_VERSAO_MATERIAL_COR. Leitura (5): CORES_BASICAS, MATERIAIS, MATERIAIS_CORES, COLECOES, FORNECEDORES (MATERIAIS_COMPOSICAO aparece no mapeamento, sem seção de schema). Lookups sem schema: PARAMETROS, FILIAIS, TABELAS_PRECO, PRODUTOS_STATUS, TABELA_LX_NCM, SEQUENCIAIS, PRODUTOS_TAMANHOS, MATERIAL_FOTO.
### Endpoints externos utilizados
- API REST da uFlow (`API_URL`, axios + JWT)
- uConnect: `…/vpn-connect` e `…/vpn-disconnect` (`UCONNECT_BASE_URL`, `UCONNECT_PARTNER_ID`, `UCONNECT_INTEGRATION_ID`)
- Compartilhamento SMB de imagens do Linx (`LINX_SMB_IMAGES_PATH`), hoje via microserviço NestJS em EC2 chamado por HTTP interno
- Banco SQL Server do Linx (`LINX_DB_*`)
- Webhook do Discord (`DISCORD_URL`), com menção a devs ou CS
## Particularidades deste cliente
- **Uma variante da uFlow = um produto no Linx** (chave `cod_linx`), ao contrário da NV, em que o produto vira um produto e as variantes viram cores. Isso muda a granularidade de praticamente todas as tabelas.
- **Único cliente com integração de imagens**: PRODUTOS_FOTO por SMB (só fotos de categoria 208 "Desenho LS" e `record_type = 'ProductVariant'`) e MATERIAL_FOTO em base64. Existe flag `LINX_IMAGE_INTEGRATION_ENABLED` (default `true`) para desligar só a imagem de produto sem parar o resto; a imagem de material não é afetada.
- **VPN aberta e fechada por lote via uConnect**, com "primeiro/último produto" inferido do relatório da execução — mecanismo que não aparece nos outros clientes; o consumidor de produtos roda dentro de VPC.
- **Geração de código de barras EAN-13 dentro da integração** (prefixo de `PARAMETROS`, sequencial de `SEQUENCIAIS`, dígito verificador calculado), com regra de elegibilidade baseada em **posição no workflow** da uFlow — na NV o código de barras é delegado a uma stored procedure do Linx.
- **Referência gerada com letra da griffe**: `[1ª letra da griffe][colecao][grupo][sequencial]`, ex. `VG271237` — formato completamente diferente do padrão `rede_loja + coleção + sequencial` da NV.
- **Tabelas exclusivas** frente à NV: PRODUTOS_MODELO, PRODUTOS_OPE_EXTRA, PRODUTOS_INDICADOR_CFOP (um registro por filial com `INDICADOR_FISCAL_TERCEIRO = 1`, `INATIVO = false` e `MATRIZ like 'IT%'`), PRODUTOS_BARRA e PRODUTOS_FOTO.
- **Sem fluxo de programações de produção** e sem fluxo de e-commerce, ao contrário da NV — que é, entre os 9 repositórios lidos, o único cliente com esses dois fluxos.
- Código em TypeScript, sem worker externo — as Lambdas executam a lógica diretamente.
- Campos de erro com IDs próprios: mapeado 4918, não mapeado 7764, silencioso 7763, `linx_last_integration` 3009.
- `FASE_PRODUCAO`/`SETOR_PRODUCAO` vêm de um único custom `fase_producao` dividido por `;`.
- Cliente com **histórico de mudanças de infraestrutura sem aviso prévio** (host, domínio AD, share, credencial, VPN, usuário de banco) — é o único com relatório formal de incidente e recomendações operacionais de aviso prévio, canal técnico direto e janela de homologação.
## Auditoria e monitoramento
Toda execução é registrada na tabela de execuções da uFlow (`integration-executions` / `jumper_integration_executions`, identificada por `INTEGRATION_ID`), com relatório de criados/atualizados/erros e ciclo de status `pending` → `executing` → `success`/`partial_success`/`error` (este último gravado explicitamente no catch, tornando a execução terminal e fora do cálculo do cutoff). Erros em três categorias com campo custom no produto (4918 / 7764 / 7763) e webhook do Discord mencionando devs ou CS. Há telas HTTP de pendências e de erros e uma função `healthCheck`. O relatório de incidente cita explicitamente as notificações de erro no canal do Discord (`STATUS_NO_LOGIN_SERVERS`, `STATUS_ACCESS_DENIED`) como primeiro sinal detectado.
## Incidentes registrados
| Data | Incidente | Resolução | Fonte |
|---|---|---|---|
| 25/03/2026 a 05/05/2026 | Integração de imagens parou após mudança simultânea de endereço (IP → hostname `VIX-APP01G2.vixbrasil.lan`), share, domínio AD (`vixbrasil.local` → `vixbrasil.lan`), credencial e modelo de resolução DNS no ambiente VIX; a lib `marsaud-smb2` só aceita IP e o AWS Lambda não executa binário nativo (`samba-client`) | Imagens desligadas temporariamente para não travar o restante do produto; construído microserviço NestJS dedicado em AWS EC2 com `samba-client` nativo, chamado por HTTP pela Lambda legada; RFI #83 = `RFI-2026-005` (estimativa 40–52 h); restabelecido em 05/05/2026 às 16h | `relatorio-incidente-imagens-vix.md` e `migracao-smb-cliente.md` |
| 01/04/2026 a 02/04/2026 | Perda de acesso ao banco do Linx: numa atualização emergencial do Linx o cliente desativou os usuários de banco, incluindo o da uMode, sem comunicação prévia | Cliente reconheceu e reverteu; RFI #85 = `RFI-2026-004` aberta pela urgência | `relatorio-incidente-imagens-vix.md` |
| 13/04/2026 | Nova instabilidade na integração, formalizada por e-mail | Estabilizada no mesmo dia | `relatorio-incidente-imagens-vix.md` |
| 15/04/2026 a 24/04/2026 | Falha na conexão da VPN | VIX disponibilizou nova VPN, testada e aprovada em reunião em 24/04/2026; ajuste retomado em 27/04 | `relatorio-incidente-imagens-vix.md` |

> ⚠ **Divergência de data não reconciliada entre as fontes.** O relatório de incidente
> datou o início em **25/03/2026** (primeiras notificações de erro no Discord em 25/03 às
> 09:01); o documento de migração SMB registra a mudança no ambiente VIX como
> **"aprox. 27/03 (data a confirmar)"** e está marcado como rascunho para revisão interna.
> As duas datas não foram reconciliadas nos documentos-fonte e não foram reconciliadas aqui.

## Governança
### Responsável técnico
[a preencher] — nenhum dos documentos designa um responsável técnico. Os documentos de incidente mencionam apenas Felipe (uMode) como quem conduziu os contatos, Patrick Wallace e Francis (VIX) e Luana no lado do cliente, e são assinados genericamente como "Equipe Técnica uMode".
### Quem pode alterar este documento
[a preencher]

## Fontes
### Documentos consultados
- Mapeamento repositório → cliente informado pelo desenvolvedor via Vinicius em 03 ago 2026
  (registrado em `protocolo-gestao-integracao.md`)
- Inventário de arquivos do repositório `integration-vix-linx` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
