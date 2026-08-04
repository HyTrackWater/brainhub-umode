# Luiza Barcelos · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
Luiza Barcelos
### ERP / sistema integrado
Safe Tech
### Repositório de código
`github.com/UmodeApp/integration-luiza-barcelos-sft` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\integration-luiza-barcelos-sft`
### Documentação de referência
- `docs\documentacao-geral-luiza-barcelos-sft.md` — 31 KB
- `.claude\skills\docs-integracao-luiza-barcelos-sft\SKILL.md` — 13 KB
### Status da integração
Em produção (somente leitura) — crons ativos no stage `v1` para os quatro fluxos de leitura; a escrita de produtos existe no código mas está **desabilitada** (handler comentado em `index.ts` e cron comentado no `serverless.yml`).
## Arquitetura
### Direções de integração
Somente **leitura** (SFT → uFlow), em quatro fluxos: **cores**, **fornecedores**, **materiais** (tecidos e aviamentos/enfeites) e **NCM** (opções de campo personalizado). **Não há escrita de volta para o SFT.**
### Mecanismo
**API HTTP do SFT** (axios, base `SFT_API_URL`), com header `Authorization` preenchido a partir de `SFT_API_TOKEN`. **Sem conexão direta com banco do cliente** — `mssql` e `knex` estão no `package.json` mas não são usados. Lado uFlow, **API REST** autenticada por `api_token` na query string, derivado do JWT. **SQS FIFO** para três dos quatro fluxos. Telas HTML (`pug`) apenas para visualização.
### Ambiente e execução
**AWS Lambda** (Serverless Framework v3, Node.js 18, TypeScript, região `us-east-2`), `memorySize: 512` (o default de 128 MB estrangulava o laço de upsert). Timeout padrão **29s**; workers de fila sobrescrevem para **900s**. Três filas SQS FIFO efetivamente usadas — `color-queue`, `supplier-queue`, `material-queue` — todas `batchSize: 1`, `maxRetries: 5` e **DLQ** auto-provisionado pelo `serverless-lift`. O fluxo de **NCM roda direto na Lambda HTTP**, sem fila, limitado a 29s. Crons só no stage `v1`.
## Escrita (uMode → sistema do cliente)
### O que é enviado
Nada. A integração é somente de leitura; o fluxo de escrita de produtos está desabilitado e fora do escopo documentado.
### Gatilho e frequência
Não aplicável — sem escrita ativa. O cron de produtos está comentado no `serverless.yml`.
### Regras e validações
Não aplicável — sem escrita ativa.
## Leitura (sistema do cliente → uMode)
### O que é importado
Cores (`/sftcorlog` → Cor na uFlow), fornecedores (`/sftforlog` → Fornecedor), materiais (`/sftitemlog` → Material tipo fabric ou accessory) e NCM (`/sftncmlog` → opções do campo personalizado NCM, id **5017** em `v1`).
### Gatilho e frequência
Crons diários escalonados: cores 01:15, fornecedores 01:30, materiais 02:00 (BRT); **NCM 02:30 apenas seg–sex**. Todos enviam o `SCHEDULE_TOKEN`; o de NCM envia também o parâmetro fixo `customField: "NCM"`. Também disparo HTTP manual (`forceImportSync*`). Cores/fornecedores/materiais processam **chunks de 500 com auto-continuação**: cada invocação faz uma fatia e re-enfileira a próxima com a janela de datas fixada, até o último chunk chamar `finalize`.
### Regras e validações
Cutoff por **intervalo** `[datinic, datfim]`: `datinic` = `start_datetime` → `created_at` da última execução finalizada (`getSaoPauloDate`, −3h) → piso `1970-01-01` (igual para todos os fluxos); `datfim` = `end_datetime` ou hoje.
Cada fluxo faz **duas requisições** ao SFT quando o cron não informa `tipolog` — `tipo='A'` (alteração) e `tipo='I'` (inclusão) — e concatena. **404 do SFT é tratado como lista vazia**; qualquer outro erro interrompe.
Bloqueio de concorrência por tipo (exceção para execução stale > 1h). **Não há throttle de tempo mínimo** entre execuções.
Erro estrutural dentro do worker é **re-lançado** para o SQS reentregar só aquele chunk (reprocesso idempotente); `finish('error')` fica reservado aos caminhos fora da fila.
Cores: matching por `reference` × `code` (= `CODIGO_COR`); ignora se o `name` é idêntico; no update envia só `name` + `integration_id`; `rgb` fixo branco e nunca atualizado; sem `book`/pantone.
Fornecedores: só `reference` + `name`; sem filtros; se existe, **sempre atualiza**.
Materiais: `TIPO` = `MP-AVIAMENTOS` ou `MP-ENFEITES` → accessory, qualquer outro → fabric; `material_type_name` recebe o `TIPO` cru; `name` cai para `CODIGO_ITEM` se a descrição vier vazia; reenvio integral a cada execução.
NCM: cria/atualiza opções e **nunca remove** as que saem do SFT; usa `findLast` (não `findLastFinished`), então **uma execução que falhou avança a janela**; cria a execução só no final e apenas se houve alteração.
Nenhum fluxo importa exclusões ou baixas.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
Nenhuma. O acesso é 100% por API HTTP; não há documento de tabelas neste repositório. O que existe são **tabelas de log do SFT expostas como endpoints** — 4 usadas em produção (`/sftcorlog`, `/sftforlog`, `/sftitemlog`, `/sftncmlog`), cada uma marcando os registros com `TIPOLOG` (A/I). Campos por endpoint estão detalhados em `docs/documentacao-geral-luiza-barcelos-sft.md`, Seções 2 a 5.
### Endpoints externos utilizados
SFT: `GET /sftcorlog`, `GET /sftforlog`, `GET /sftitemlog`, `GET /sftncmlog` (todos com `datinic`/`datfim`/`tipo`, não paginados); `GET /sftmaterial` (campo personalizado MATERIAL, sem cron em produção); `GET /sftitem` (paginado, **código comentado, não usado**). uFlow: `/colors`, `/suppliers`, `/materials`, `/custom-fields`, `/integration-executions`. Outros: AWS SQS FIFO e webhook do Discord.
## Particularidades deste cliente
- Entre Baw, Cambos e Luiza Barcelos, é a única **sem escrita ativa** — a uFlow só consome cadastros; o código de escrita de produtos existe mas está comentado nos dois lugares (handler e cron).
- É também a única das três em que as chamadas ao ERP **enviam autenticação** (header `Authorization` com `SFT_API_TOKEN`) — o inverso do caso Cambos.
- O SFT expõe **tabelas de log**, não entidades: cada leitura precisa de duas chamadas (`TIPOLOG` `A` e `I`) e recebe tudo do período **sem paginação**, acumulado em memória.
- Única do lote com **chunking de 500 com auto-continuação e janela de datas fixada** entre chunks, com ordenação determinística por referência (offset só é estável se a lista vier igual). Consequência aceita: registro novo inserido no mesmo dia durante a corrida pode ser pulado, e o cutoff diário re-cobre no dia seguinte.
- Única do lote com **`maxRetries: 5` + DLQ** e com `memorySize` ajustado para 512 MB.
- Única com um fluxo que sincroniza **opções de campo personalizado** (NCM) em vez de entidade — e esse fluxo é o mais frágil: sem fila, limitado a 29s, sem bloqueio de concorrência, e usa `findLast`, de modo que uma falha avança a janela e pode deixar NCMs de fora.
- Material importado é um **"esqueleto"**: só identidade (código, nome, tipo, ativo), com uma variante e um fornecedor fixos chamados `INDEFINIDO` — sem cor real, fornecedor real, composição, preço ou consumo. É bem mais pobre que os materiais da Baw e da Cambos.
- Telas de pendências são **somente visualização** — os botões de "Enviar para integração" estão comentados nos templates.
- Existe um alvo `MATERIAL` para o mecanismo de campo personalizado, configurado só em `staging` (id `0` em `v1`).
## Auditoria e monitoramento
Execuções registradas em `integration-executions` da uFlow (`INTEGRATION_ID` **25** em `v1`, 20 em staging/dev), com o mesmo ID para todos os tipos e diferenciação por `integration_type`. Status calculado (`pending`/`executing`/`success`/`partial_success`/`error`), com sentinela `'uMode Integration'` no `pending` mantido pelos chunks intermediários e removido no `finalize`. **Não existem campos de erro por item** — por ser somente leitura, o erro fica apenas no relatório da execução e no **Discord** (devs ou CS, só em `staging`/`v1`). Telas `/colors/pendings`, `/suppliers/pendings`, `/materials/pendings` mostram o que o cutoff traria e um ícone de alerta com o texto do último erro. Sem auditoria pós-integração comparando SFT × uFlow.
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
- Inventário de arquivos do repositório `integration-luiza-barcelos-sft` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
