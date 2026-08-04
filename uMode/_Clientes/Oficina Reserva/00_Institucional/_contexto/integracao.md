# Oficina Reserva · Integração

> Criado em 03 ago 2026 a partir do repositório de integração real, e **preenchido com a
> documentação técnica do próprio repositório** em 03 ago 2026. Ver `protocolo-gestao-integracao.md`.

## Identificação
### Cliente
Oficina Reserva
### ERP / sistema integrado
SAP
### Repositório de código
`github.com/UmodeApp/arzz-sap` · clone local em `C:\Ambientes Virtuais\uMode-Integracoes\arzz-sap`
> ⚠ **Este repositório atende mais de um cliente:** Oficina Reserva + Reserva.
> Cada casa tem o seu `integracao.md` (isolamento entre casas é regra travada em
> `CONTEXT.md`), os dois apontando para o mesmo repositório. Não é duplicidade — é a
> mesma integração registrada em cada casa que ela serve. O nome `arzz` é **AZZAS**,
> o grupo ao qual os dois pertencem (o CRM já os classifica em "Grupo 1: Azzas").
### Documentação de referência
- `docs\documentacao-geral-arzz-sap.md` — 40 KB
- `.claude\skills\docs-integracao-arzz-sap\SKILL.md` — 10 KB
- `README.md` — 3 KB
### Status da integração
Em produção — o documento descreve o stage `v1` (produção) como ativo, com cron de 30 min existente **só** em produção, e trata Reserva (`entity.id` 3298) e Oficina (3562) como marcas ativas; Baw (3344) está descontinuada e bloqueada no código. O próprio documento a classifica como a integração mais antiga e legada da uMode.
## Arquitetura
### Direções de integração
Ambas. Saída (uFlow → SAP/Linx): CSV para o ZZNet (Interface 1), ficha do produto acabado (Interface 3) e modificação do produto acabado (Interface 8). Entrada (SAP/Linx → uFlow): gravação dos códigos SAP/Linx no produto (Interface 6) e criação/atualização de matéria-prima e cores (endpoint de materiais).
### Mecanismo
API REST em ambos os sentidos + arquivo CSV com upload manual. **Não acessa o banco do Linx** — toda comunicação com SAP/Linx passa pelas interfaces REST da AR&CO (RESTAdapter do PI/PO), com HTTP Basic. Do lado uFlow: leitura direta do MySQL (Knex) + chamadas à API REST da uFlow. Fila SQS FIFO desacopla coleta e envio; erros vão para webhook do Discord.
### Ambiente e execução
AWS Lambda (Serverless Framework v3, Node.js 16, região us-east-2). Gatilhos: endpoints HTTP (JWT na query string `?token=`), cron `rate(30 minutes)` — **só no stage `v1`/produção** — e evento SQS FIFO com `batchSize: 1`. Em `staging` o enfileiramento só é manual, por rota HTTP.
## Escrita (uMode → sistema do cliente)
### O que é enviado
CSV de variantes sem código SAP para upload no ZZNet (Interface 1); ficha do produto acabado / "tabelão" — cabeçalho do produto + ficha técnica de materiais e consumos (Interface 3); campos de modificação do produto acabado já existente no SAP (Interface 8); e, de volta na uFlow, `sap_last_integration` e `cor_fabricante = CANCEL`.
### Gatilho e frequência
Interface 1: 100% manual (tela de listagem, seleção de variantes, download do CSV e upload manual no ZZNet). Interfaces 3+8: envio manual de uma variante (`GET /produtos/lista-tecnica/{id}`) ou cron a cada 30 min (só produção) que enfileira até 500 variantes por marca na SQS; o consumo da fila é serial (um grupo por dia, `batchSize: 1`).
### Regras e validações
- Orquestração `sendProduct` = Interface 3 → Interface 8 → gravação de `sap_last_integration`; a data só é gravada se ambas tiverem sucesso, então falha volta a ficar pendente.
- Elegibilidade da Interface 3: variante da marca do token, produto não deletado, **Linha preenchida** (efeito colateral de um INNER join, vale até com `only3`), validação "Integração SAP/Linx" em `passed`/`warning` e produto fora de `backlog`.
- Variante deletada **não** é filtrada: é reenviada uma última vez com `cor_fabricante='CANCEL'` para cancelar a cor no SAP (idempotente pela própria marcação).
- Produto cancelado → `inativo_produto=1`, `status_pa='05'`, `tipo_status_pa=1`.
- Composição sempre perde o 1º caractere; valor da variante tem precedência sobre o do produto; idem coleção (custom field distinto).
- `codigo_linx` só é enviado se casar o formato `7 dígitos . 3 dígitos`; senão vai `null`.
- Interface 8 só é sucesso com HTTP 200 e `body.status == 'S'`; de/para de griffe que resulte em `ERRO:` aborta a integração. Todo o JSON passa por `latinize` (SAP não aceita acento).
- A listagem e o envio usam consultas **diferentes**: o envio manual não checa coleção em `dev` nem marca/coleção deletadas.
## Leitura (sistema do cliente → uMode)
### O que é importado
Códigos gerados no SAP e no Linx, gravados no produto/variante da uFlow (`reference`, `integration_id`, custom field `codigo_sap`); e matéria-prima do SAP: materiais-base (tecido/aviamento), variantes de cor, composição, largura, fornecedor, preço, unidades e fator de conversão.
### Gatilho e frequência
Sem agendamento: os dois fluxos são **push do SAP**. O SAP chama `POST /produtos/alterar` quando o produto já existe no SAP e no Linx, e `POST /materiais` sempre que um material é criado ou alterado. Não é possível excluir materiais por essa interface.
### Regras e validações
- Interface 6: `reference` = `cod_linx` antes do 1º ponto; `integration_id` = 10 primeiros chars do `cod_sap`; custom field `codigo_sap` = `cod_sap` completo.
- Trava de consistência: se `reference`/`integration_id` já estão preenchidos e **divergem** do recebido, nada é gravado (nenhum PATCH), a resposta ao SAP sai com `status: 502` + `msg_erro` e dispara Discord. Grava só na 1ª vez ou em reescrita idêntica.
- Materiais: `desc_grupo_mercadoria` decide tipo — `Tecidos` → `fabric`/prefixo `T`, `Aviamentos` → `accessory`/prefixo `A`; qualquer outro valor lança erro (comparação exata).
- Presença de `desc_cor` decide material-base × variante de cor; na variante, `active` do material é removido e a inatividade migra para o fornecedor.
- `desc_cor`: 3 primeiros chars = código da cor, nome a partir do 5º — o 4º caractere é descartado.
- NCM do material entra **cru, sem pontuação** (diferente do CSV e da Interface 8, que formatam `XXXX.XX.XX`).
- Baw bloqueada por `cod_griffe == '00056'` (na Interface 1 a Baw é o código `66` — dois códigos diferentes para a mesma marca).
- De/para de unidade SAP→uFlow: `KI→cx`, `BOT→gr`, `TH→mil`, `PAA→par`, `ST→pc`, `PAK→pac`; fora da tabela vai em minúsculas.
## Tabelas e endpoints
### Tabelas do ERP mapeadas
Nenhuma. Esta é a única das integrações da carteira que **não mapeia tabelas do ERP** — não há acesso ao banco do SAP nem do Linx; tudo trafega pelas interfaces REST da AR&CO. As tabelas lidas diretamente são do **banco MySQL da uFlow** (produtos, variantes, coleções, custom fields, `umode_validation_results`, aprovações), sem documento de schema equivalente aos `tabelas-do-linx-*.md` dos clientes Linx.
### Endpoints externos utilizados
- `POST http://{ARZZ_API_ENDPOINT_URL}:50000/RESTAdapter/pi/umode/fichaprodutoacabado` (Interface 3, timeout 10 s)
- `POST http://{ARZZ_API_ENDPOINT_URL}:50000/RESTAdapter/pi/umode/modificaprodacabado` (Interface 8, timeout 25 s; 90 s quando vem da SQS)
- API REST da uFlow (`api_token` na query string) + banco MySQL da uFlow via Knex
- Webhook do Discord (URL e menção chumbadas em `src/discord.js`)
- Endpoints expostos e chamados **pelo SAP**: `POST /produtos/alterar` e `POST /materiais`
## Particularidades deste cliente
- Único ERP SAP da carteira e único caso **sem acesso a banco do ERP**: a AR&CO expõe interfaces numeradas (1 a 8, sem a 7) e a uMode é responsável apenas pelas 1, 3, 6, 8 e matéria-prima; as 2, 4 e 5 são internas do cliente.
- Único fluxo com **etapa manual obrigatória**: o CSV gerado pela Interface 1 é subido à mão no ZZNet.
- Duas marcas numa mesma integração (Reserva 3298 e Oficina 3562), com **IDs de custom field distintos por marca e por ambiente**, resolvidos por `getConfig` — nunca chumbados.
- Regra de griffe: `c.reference` no formato `$griffe|ESTACAO|` faz MARCA/COLEÇÃO serem resolvidas por uma lista fixa de códigos de griffe (`03,09,36,33,71,72,77,78` → `RESERVA MINI`/`N01`; `66` → `BAW`/`W01`; demais → `RESERVA`/`T01`); `ROTEIRO` vira `BAW` na griffe 66.
- `LINHA_CALCADO` existe **só na Oficina**: sobrescreve a coluna LINHA e prefixa o `COD_ANTIGO`/`codigo_umode`; na Reserva o campo não existe e o código engole a falha num try/catch silencioso.
- Cancelamento de cor por `cor_fabricante='CANCEL'` (variante deletada reenviada uma única vez) — mecanismo que não aparece nas integrações Linx.
- `custo_rep1` vai **em centavos**, sem dividir por 100.
- O enfileiramento automático ignora o token do chamador e processa as duas marcas fixas no código, em sequência.
- Parâmetro `only3` como modo de depuração: ignora validação e `backlog` e pula a Interface 8.
- Nota sobre o documento-fonte: o sumário anuncia as seções 10 (comportamentos frágeis/bugs latentes) e 11 (pontos que precisam de validação), e a numeração salta de 9.1 para 9.4 — esses trechos **não existem** no corpo do arquivo lido.
## Auditoria e monitoramento
Sem tabela de execuções de integração (diferente de NV e VIX). O controle é por custom field `sap_last_integration` no produto e na variante (vazio = pendente) mais as telas HTML de pendências das Interfaces 1 e 3/8, com permissão somente-leitura por `READ_ONLY_POLICY_IDS`. Erros: handler central `exceptionResponse` → log + webhook do Discord + HTTP 500; praticamente toda falha vira 500 (o status real vai no corpo JSON). Não há retry automático de banco ou de API. No consumo da fila, erros são acumulados e não derrubam o lote.
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
- Inventário de arquivos do repositório `arzz-sap` (leitura de conteúdo pendente)
- **Conteúdo técnico extraído em 03 ago 2026** da documentação real do repositório clonado
  (`docs/documentacao-geral-*.md`). Resumo com ponteiro, conforme o protocolo — a
  especificação completa continua no repositório, não foi copiada para cá.
