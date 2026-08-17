# Fluxo de dados do BrainHub — da escrita do MD ao ping na inbox

> Levantado em **17 ago 2026** por leitura de código em `umode-brainhub-api`, branch
> `codex/bhp-p16-federation-grants-back` (**115 branches remotas, 50 schemas**).
> **Somente leitura. Nenhum commit, push ou checkout fora do `brainhub-umode`.**
>
> **Este documento é a autoridade sobre o fluxo de dados.** As seções de fluxo do
> `_fluxo-crud-brainhub.md` ficam **superseded** por ele. O `_dicionario-dados-brainhub.md`
> continua sendo a autoridade sobre **campo a campo**; aqui é sobre **o que se move, quando e
> disparado por quem**.

## 0 · Grau de evidência — exigido em toda afirmação deste documento

| Grau | Significa | Como confio |
|---|---|---|
| **[C]** | **Código lido**, com arquivo citado. Nome de campo, enum, índice, invariante. | Alta. Não é interpretação. |
| **[F]** | Existe em código **mas está atrás de feature flag / allowlist** — escrito e desligado. | Existe ≠ vigente. |
| **[P]** | **Proposta minha.** Ancorada em [C], **não validada por ninguém.** | Baixa até o Vinicius travar. |
| **[D]** | **Decisão que não é minha** — do Vinicius ou do João. ⚠ **Nunca do Bergson:** ele implementa, não define. | Nula até ser tomada. |

⚠ **Toda a faixa [C] tem uma ressalva que vale para o documento inteiro:** o código está em
**branch, não na `main`**. A `main` tem 5 módulos; a branch lida tem 29. **Está construído e não
integrado.**

## 0-bis · Declaração de completude — o que este documento NÃO resolve

> Escrito no topo de propósito. Em 17 ago 2026 o Vinicius cobrou, com razão, que eu declarava
> etapa vencida e só listava a lacuna quando ele apertava. **A lacuna vem antes da conquista.**

| # | Não resolvido | Grau | Bloqueado por |
|---|---|---|---|
| 1 | O payload de evento não carrega tipo/tier (§2) | [C] estado atual | **Nada.** Especificado em §3-bis — é item de implementação, não restrição |
| 2 | ~~`metadata` sem contrato~~ → **resolvido:** o `_indice/` é o contrato de importação (pend. 191) | ✅ | — |
| 3 | **Resposta a endereçamento** não cabe em `approvals` (índice único) — precisa de collection | [P] | Nosso desenho a fechar |
| 4 | **Nenhuma superfície de conversa com agente** existe (§5) | [C] lacuna | Desenho + [D] do Vinicius |
| 5 | **29 dos 50 schemas** com campos não lidos — lista em `_dicionario-dados-brainhub.md` | — | Tempo de leitura |

**Cobertura de leitura desta sessão:** 21 dos 50 schemas campo a campo, mais 7 arquivos de
serviço lidos por inteiro. **O fluxo de escrita→disparo→execução está fechado em [C].** O fluxo
de endereçamento→resposta é [P] inteiro, porque **não existe uma linha dele no código**.

---

## 1 · O trecho RESOLVIDO — publicar um contexto e disparar automação

**Isto não é proposta. Está escrito e eu li os cinco arquivos.** É o único caminho de dados
completo que o BrainHub tem hoje, e é o molde de tudo que vamos acrescentar.

### 1.1 A escrita — transação com concorrência otimista `[C]`
`src/modules/contexts/repository/contexts.repository.ts` (~linha 370)

```
session.withTransaction:
  findOneAndUpdate({ _id, ...escopo, deletedAt: null, currentVersionId })   ← trava de concorrência
    $set: currentVersionId, title, content, metadata, indexStatus: PENDING
    $inc: { revision: 1 }
  insertOne('context_publication_outbox', effect)                           ← na MESMA transação
```

Três coisas que valem doutrina:
- **`currentVersionId` entra no filtro.** Se alguém publicou no meio, o update não casa e volta
  `CONTEXT_HEAD_NOT_UPDATED` → `null`. **Ninguém sobrescreve alteração de outro em silêncio.**
- O `_id` do efeito é **determinístico** (`publicationEffectId(contextId, versionId)`) → reinserção
  colide por chave duplicada. **Exactly-once por construção, não por tentativa.**
- Cabeça e outbox na **mesma transação**: é impossível a publicação existir sem o evento, ou o
  contrário.

### 1.2 → 1.5 O restante da cadeia `[C]`
`context-publication-outbox-drainer.service.ts` · `runtime-event-bus.ts`

| Etapa | Mecanismo | Números do código |
|---|---|---|
| **Drenagem** | Poll com lease por `workerId` | a cada **5 s**, lease **30 s**, lote máx **25** |
| **Reindexação** | Fila BullMQ `INGESTION_QUEUE` | `jobId: context-reindex-<ctx>-<rev>`, 3 tentativas, backoff exponencial |
| **Cache** | Invalida Redis (`BY_ID` + `LIST_PATTERN`) | antes de emitir o evento |
| **Evento** | `runtimeEventBus.publish({eventType:'context.published', scope:{brainId,tenantId}, payload})` | payload: `contextId, versionId, revision, categoryId, areaId` |
| **Casamento** | `listActiveTriggersByEvent` → `clauses` vs payload (`ALL`/`ANY`) | operadores `EQUALS, NOT_EQUALS, IN, EXISTS` |
| **Execução** | `loopExecutor.run(...)` | `sourceType: TRIGGER`, `dedupeKey: trigger:<id>:<eventId>` |
| **Falha** | Reagenda com backoff | teto de **15 min**; falha de 1 trigger não bloqueia as outras |

**A garantia de não-duplicidade é de banco, não de código:** `loop_runs` tem índice **único** em
`{brainId, dedupeKey}`. Como a chave é `trigger:<triggerId>:<eventId>`, o mesmo evento na mesma
trigger **não roda duas vezes nunca**, mesmo com o drenador reprocessando.

O caminho por tempo é gêmeo: `routines` com `schedule{kind:CRON, expression, timezone}`,
`nextRunAt`, e índice **único** em `{brainId, dedupeKey}` — mesma disciplina.

---

## 2 · Os cinco limites duros do disparo — isto restringe TODO o desenho

> Estes limites são o motivo de eu **não** poder desenhar "endereçamento dispara notificação"
> livremente sobre suposição. São **fato do código atual**.
>
> ⚠ **Mas não são restrições de projeto.** Desde que o Vinicius travou (17 ago 2026) que o Bergson
> traduziu o entendimento dele do que explicamos — e que **definir collections, campos e relações é
> nosso papel** — cada limite abaixo é **item de especificação, não muro**. Onde eu havia escrito
> "negociar com o Bergson", leia **"especificar para o Bergson implementar"**.

| # | Limite `[C]` | Consequência prática |
|---|---|---|
| **L1** | **Existe UM eventType: `context.published`.** Varri o repositório: é o único literal. | Não há `demand.created` nem `addressing.answered`. **Cada evento novo é código novo.** |
| **L2** | O payload tem **5 campos**: `contextId, versionId, revision, categoryId, areaId`. **Não carrega `metadata`, `type` nem `sensitivityTier`.** | Uma trigger **não consegue** distinguir "publicaram uma demanda" de "publicaram um institucional" — a não ser pela categoria. |
| **L3** | `scalarEquals` só compara **string com string**; `IN` exige array de string. | Número e booleano **não casam** (só `EXISTS`). Nada de "tier > 1". |
| **L4** | `RuntimeEventBus` **não tem endpoint público de ingestão** — comentário explícito: só publicam módulos cujo efeito já é durável. | **Não se emite evento de fora.** Módulo novo que queira disparar precisa do **próprio outbox transacional**. |
| **L5** | A trigger executa como **dona dela**: `resolveActiveById(trigger.ownerPersonId)` → `owner.trustedSubjectId`. | A automação age com a **autoridade do dono da trigger**, não de quem causou o evento. Quem possui trigger define o poder do robô. |

**L4 e L5 são os dois mais importantes e os que ninguém tinha escrito.** L4 diz que
`addressings` **não é uma collection — é um módulo com outbox**. L5 diz que a trigger é um objeto
de governança, não de configuração.

---

## 3 · Consequência: o roteamento só tem dois eixos — e isso decide nosso desenho

Do L2, o que uma trigger pode ler **hoje** é: `categoryId`, `areaId`, `contextId`, `versionId`,
`revision`. **Só isso.** Logo há dois caminhos — **e eu recomendo o segundo:**

> 🔺 **RECOMENDAÇÃO REVISTA em 17 ago 2026, no mesmo dia.** O Vinicius travou que **o Bergson traduziu
> o entendimento dele do que explicamos — logo não é referência de intenção, e definir collections,
> campos e relações é NOSSO papel.** Isso destrói a única vantagem que eu havia declarado para o
> Caminho A ("não depende de alteração no código do Bergson"). **Passa a valer o Caminho B como
> especificação**; A fica apenas como paliativo se precisarmos de roteamento antes da mudança de
> schema. Motivo de fundo: B mantém `Category` no papel para o qual foi desenhada — **audiência** — e
> põe o tipo onde ele pertence, **como atributo do próprio contexto**. Ver §3-bis.

**Caminho A — uma Category por tipo de entidade `[P]` ⚠ rebaixado a paliativo**
Cada tipo de MD vira uma `Category` própria, e `categoryId` passa a ser o discriminador de tipo.
Funciona hoje, sem alterar nada. **Mas gasta o eixo de audiência para carregar tipo** — e os dois
não convivem, porque categoria governada é amarrada a **uma** área. Serve como ponte se
precisarmos de roteamento antes de o schema mudar; **não é o modelo.**

**Caminho B — tipo como atributo do contexto `[P]` ✅ é a especificação**
`contexts.type` como campo de primeira classe, e `type` no payload do evento. Resolve o L2 **na
origem** em vez de contorná-lo, e devolve `Category` ao papel de audiência. Detalhado na §3-bis.

> **Decisão registrada, e revista no mesmo dia.** Eu havia escolhido **A**, e a justificativa era
> literalmente *"não depende de alteração no código do Bergson"*. **Essa justificativa nunca foi
> válida** — o Vinicius travou que definir o modelo é nosso papel e o Bergson implementa. Vale o
> **B**. Lição de método: **nunca escolher caminho técnico porque ele evita mexer no código de
> outro.** Isso não é prudência, é desenhar para a conveniência errada.

**Os nove tipos `[P]`** — agora como valores de `contexts.type`, não como categorias:
`institucional`, `jornada`, `pessoas`, `contexto-area`, `produto`, `integracao`, `protocolo`,
`demanda`, `rfi`.

## 3-bis · A especificação correta — tipo é atributo do contexto, não da categoria `[P]`

Com a autoridade de desenho do nosso lado, o modelo certo é simples e não sobrecarrega nada:

| O que especificamos | Onde | Por quê |
|---|---|---|
| **`contexts.type`** — enum com os 9 tipos de MD | campo de primeira classe em `contexts` | o tipo **é** atributo do documento; não é agrupamento nem audiência |
| **`type` no payload de `context.published`** | o evento passa a carregar 6 campos | resolve o **L2** na origem, em vez de contorná-lo |
| **`sensitivityTier` no payload** | idem | permite trigger sensível a confidencialidade sem gambiarra |
| **`Category` volta a ser só audiência** | como o schema já a desenhou | governada, por área, com `stewardAreaId` e `category_shares` |

**O que isso compra, e é muito:**
- A trigger casa `EQUALS` em `type` — string, dentro do **L3**, sem nenhuma torção.
- **Os dois eixos deixam de competir:** tipo e audiência passam a ser independentes. Um `jornada`
  pode ter audiências diferentes por área; uma área pode ter vários tipos. Hoje, com A, isso é
  impossível.
- **A contagem de categorias deixa de ser 423 buckets de tipo** e passa a ser o que o desenho de
  audiência pedir — que é decisão de governança, não subproduto de roteamento.
- E o `ask` ganha filtro por tipo de documento de graça ("pergunte só sobre jornadas").

**O custo honesto:** exige alteração em `contexts`, no payload do evento e no publisher — três
pontos, um deles no caminho quente. É trabalho de implementação, **não é obstáculo de projeto**.
Entra na especificação que vai para o Bergson, com o desenho pronto para ele implementar.

---

## 4 · Autorização — dois modelos, e uma correção do que eu te disse hoje

### 🔴 Correção
**Hoje eu te afirmei que os `readableTiers`/`writableTiers` de `area_memberships` "não são
consultados na autorização". Isso está errado.** Eles são consultados —
`category-audience-policy.service.ts:58` filtra membership por `readableTiers.includes(T2)`, e
`authorizeStewardWrite` exige `writableTiers.includes(T2)`. O certo é: **não são consultados no
`AccessScopeService`**; são consultados no caminho de audiência de categoria. São dois
autorizadores diferentes, e eu generalizei de um para o outro.

### 4.1 `AccessScopeService` — grosso, sempre ligado `[C]`
**18 operações** (`organizations.*`, `categories.*`, `contexts.*`, `ask.answer`), **nenhuma
`agents.*`**. Regra base: `requestedOrganizationId === executorOrganizationId`. Escape único:
`TrustedIndividualAccessException`, **máx 24 h**, ninguém concede a si mesmo, **fail-closed se a
auditoria estiver indisponível**, 8 motivos de negação enumerados.

### 4.2 `CategoryAudiencePolicyService` — fino, e **desligado** `[F]`
`AudienceMode = AREA | SELECTED_AREAS | TENANT_WIDE`, mais `category_shares` (ALLOW/DENY por
`targetAreaId`, com `approvalId` e `revokedAt`), mais `membership.grants[]` com capacidades
nomeadas (`categories.steward`, `categories.share.manage`).

A autorização é feita **filtrando a query**, não checando permissão depois
(`category-audience.filter.ts`) — quem não tem audiência **não vê o documento existir**.

⚠ **Mas:** exige `CATEGORY_AUDIENCE_FILTER=on` **e** o `brainId` numa allowlist
(`CATEGORY_AUDIENCE_BRAIN_ALLOWLIST`); fora disso lança `POLICY_DISABLED`. E **Personal Brain não
é suportado** (`PERSONAL_BRAIN_NOT_SUPPORTED`). O modelo fino existe e **está desligado**.

### 4.3 "Quem pode consumir cada agente" — o desenho, agora com o padrão da casa `[P]`
A resposta continua sendo que **não existe**. Mas eu não vou inventar um modelo: **copio o de
categoria**, que já foi pensado, revisado e tem contrato de negação enumerado.

| Peça nova | Espelha | Conteúdo |
|---|---|---|
| `agents.audienceMode` | `categories.audienceMode` | `AREA \| SELECTED_AREAS \| TENANT_WIDE` |
| `agents.stewardAreaId` | `categories.stewardAreaId` | área que responde pelo agente |
| `agent_shares` | `category_shares` | `subjectType: AGENT`, `targetAreaId`, `effect: ALLOW\|DENY`, `approvalId`, `revokedAt` |
| grant `agents.consume` | `categories.steward` | capacidade em `membership.grants[]` |
| operação `agents.run` | as 18 existentes | entra no `AccessScopeService` |

Para o **agente de suporte do uFlow** isso resolve o teu caso direto: `audienceMode:
TENANT_WIDE` — quase todos consultam — e a exceção passa a ser explícita e auditável, em vez de
implícita.

---

## 5 · Como a operação interage com o agente — as duas superfícies, e nenhuma serve

> Tua pergunta ("nem especifiquei isso") tem resposta de código: **hoje a operação não interage
> com agente nenhum.** Existem duas superfícies e as duas são o objeto errado.

| Superfície `[C]` | O que é | Por que não serve |
|---|---|---|
| `conversations` + `conversation_turns` | RAG sobre o acervo: `question`, `answer`, `sources[]` com `contextId`/`score`(0–1), `limit`(1–20), status `PENDING→ANSWERED\|FAILED` | **Não tem `agentId`.** Pergunta ao acervo, não ao agente. |
| `agent_runs` | Execução governada: `agentId`, `agentVersionId`, `input`, `output`, `retrievalStatus`, `costUsd` | **Single-shot.** Sem `conversationId`, sem `sequence`. **Não tem memória de conversa.** |

**A peça que falta é pequena e o desenho é óbvio `[P]`:** `conversations.agentId` (nullable — nulo
= RAG puro, preenchido = conversa com agente) e `conversation_turns.agentRunId`. Assim cada turno
de conversa aponta para a execução que o respondeu, com custo e versão de instrução. **Um turno
passa a ter procedência completa: qual instrução respondeu, com quais contextos, a que custo.**

E o `sources[]` já existente é o ouro disso: **toda resposta cita `contextId` com score.** É
rastreio de "qual MD nosso respondeu" que já vem de graça.

---

## 6 · Como os nossos MDs preenchem o banco `[P]`

> Tua pergunta "fica claro como nossos mds vão preencher o banco?". Não estava. **Agora está
> proposto, campo a campo.** A decisão do front-matter saiu (pend. 191): **o `_indice/` é o contrato.**

| Origem no MD | Destino | Observação |
|---|---|---|
| H1 do arquivo | `contexts.title` | |
| Corpo integral (markdown) | `contexts.content` | markdown cru, sem conversão |
| Tipo do MD | `contexts.categoryId` | via as 9 Categories do §3 — **é o discriminador** |
| Pasta de área (`01_Comercial`) | `contexts.areaId` | mapa pasta→`areaId` é tabela nossa |
| Cliente / Casa | `contexts.tenantId` + `brainId` | Second Brain por tenant |
| **Front-matter** | `contexts.metadata` | **[D] bloqueado na C2** |
| Commit que alterou o arquivo | `context_versions` (append-only) | 1 versão por commit; `contentHash` sha256 |
| `[[links]]` e `conecta_area_cliente` | `context_relations` | dos **7** tipos, `provenanceKind: IMPORTED` |

**Contrato mínimo de `metadata` `[P]`** — porque `contexts.metadata` é `Object` **livre**: sem
contrato nosso, cada importação inventa o seu.
`{ repoPath, commitSha, mdType, clientKey, generatedBy: 'brainhub-umode', importRunId }`

**Chave de idempotência da importação `[P]`:** `(tenantId, categoryId, repoPath)`. Sem ela, a
segunda importação duplica tudo. E como o publish exige `currentVersionId` no filtro (§1.1), o
importador tem de **ler a cabeça antes de publicar** e tratar `null` como "mudou no meio,
recarrega" — não como erro.

⚠ **Cuidado de schema:** `triggers`, `routines`, `conversations`, `conversation_turns` e
`category_shares` usam **`strict: 'throw'`** — campo desconhecido é **rejeitado**, não ignorado.
Não há como contrabandear campo nosso. Em `contexts` eu **não confirmei** o modo strict nesta
leitura; verificar antes de assumir.

---

## 7 · Endereçamento, decisão, demanda, inbox e **resposta** `[P]`

> **Nada disto existe.** Verifiquei com rigor: **115 branches**, e `Addressing`, `InboxItem` e
> `DemandStatus` aparecem em **0 commits** — nem como arquivo criado, nem no conteúdo de
> qualquer commit do histórico. A ausência está confirmada, não suposta.

### 7.1 O que dá para reusar sem pedir nada a ninguém
**`approvals.subjectType` é `String` livre, não enum `[C]`.** Então a **decisão** sobre um
endereçamento cabe em `approvals` **sem alteração de schema**: `subjectType: 'ADDRESSING'`,
`subjectRef: <addressingId>`, e já vêm de brinde `band` (a vazão: `AUTO_ARCHIVE`,
`WEEKLY_BATCH`, `JOAO_REQUIRED`, `AREA_LEAD_REQUIRED`), `decidedBy`, `decisionReason`,
`decidedAt`, `decisionAuthority`.

### 7.2 O que NÃO cabe — e o motivo é um índice
**`approvals` tem índice ÚNICO em `{brainId, subjectType, subjectRef}` (parcial em
`deletedAt: null`) `[C]`.** Ou seja: **uma aprovação por assunto, uma só vez.** E
`ApprovalStatus` é `PENDING | APPROVED | REJECTED | ARCHIVED` — **não há "devolvido com
pergunta" nem "reatribuído"**.

> Portanto: `approvals` modela **um veredito**, não uma **conversa de trabalho**. O vai-e-vem
> operacional — aceitar, recusar, devolver perguntando, reatribuir, concluir com evidência —
> **não cabe lá**, e isso é a lacuna que você encontrou hoje e eu não tinha considerado.

### 7.3 As quatro peças, e por que são quatro `[P]`

| Peça | Papel | Padrão da casa que ela copia |
|---|---|---|
| `addressings` | O ato de endereçar: de quem, para quem (`trustedSubjectId`), sobre qual assunto, prazo | `approvals` (polimórfico) + outbox próprio (L4) |
| `approvals` **reusado** | O **veredito**, com autoridade e vazão | já existe |
| `addressing_responses` | **Append-only.** Cada resposta: `decision`, `respondedBySubjectId/PersonId`, `justification`, `evidenceContextIds[]`, `generatedDemandIds[]` | `audit_events` / `context_versions` (append-only por guarda de schema) |
| `demands` | O trabalho que nasceu da resposta | módulo próprio, com outbox |
| `inbox_items` | A materialização do ping, com entrega e leitura | `context_publication_outbox` (lease + retry) |

**A máquina de estado da resposta `[P]`:** `ACCEPTED`, `REFUSED`, `RETURNED_WITH_QUESTION`,
`REASSIGNED`, `COMPLETED`. Só `COMPLETED` exige `evidenceContextIds[]` não-vazio — **conclusão
sem evidência não é conclusão.** `RETURNED_WITH_QUESTION` reabre o endereçamento sem apagar a
resposta anterior, porque a collection é append-only.

### 7.4 O disparo do ping — a consequência prática do L4 `[P]`
`inbox_items` **não pode** ser preenchida por um listener solto. Pelo L4, `addressings` precisa do
**próprio outbox transacional**, exatamente como `context_publication_outbox`:

```
1. escrita do endereçamento + insert no addressing_outbox  → MESMA transação (§1.1)
2. drenador com lease reivindica                            → 5s / 30s / lote 25
3. emite eventType 'addressing.created'                     → L1: eventType NOVO = código novo
4. RuntimeEventBus casa triggers por categoryId/areaId       → L2/L3
5. Loop com nó NOTIFICATION grava inbox_items                → o tipo de nó JÁ existe
6. marca dispatched; falha reagenda com backoff              → teto 15 min
```

O passo 5 é o que me fez corrigir "faltam 4 collections" para **3**: `NOTIFICATION` **já é tipo de
nó** do Loop. O que falta não é o conceito de notificar — é o **registro de entrega**.

---

## 8 · O rastreio — dado um MD, o que o banco responde

| Pergunta | Responde | Grau |
|---|---|---|
| Quem alterou, quando, quais campos | `audit_events` (append-only, `phase: PRE_MUTATION`, ator em 3 partes) | **[C]** |
| Qual era o conteúdo antes | `context_versions` (append-only, `contentHash` sha256) | **[C]** |
| Foi aprovado por quem, com que autoridade | `approvals.decidedBy` + `decisionAuthority` + `band` | **[C]** |
| A publicação disparou o quê | `context_publication_outbox._id` → `loop_runs.dedupeKey` (`trigger:<id>:<eventId>`) | **[C]** |
| Com que autoridade o robô agiu | `loop_runs.createdBySubjectId` = dono da trigger (L5) | **[C]** |
| Quanto custou | `loop_runs.costUsd` + `steps[].costUsd` por nó | **[C]** |
| Qual instrução respondeu ao usuário | `agent_runs.agentVersionId` → `agent_versions.contentHash` | **[C]** |
| Quais MDs sustentaram a resposta | `conversation_turns.sources[].contextId` + `score` | **[C]** |
| **Quem foi endereçado e o que respondeu** | **nada** | **[P]** §7 |

**A cadeia de rastreio do que existe é contínua e sem furo** — do commit ao custo por nó. Ela
**para** exatamente onde o §7 começa.

---

## 9 · O que depende de decisão, e de quem

> 🟢 **As duas decisões que dependiam do Vinicius foram TOMADAS em 17 ago 2026**, a pedido dele
> ("daquilo que trava da minha parte, você já não tem resposta para adotar e seguir?"). Ficam
> registradas abaixo como resolvidas, com o raciocínio em `_como-o-brainhub-funciona.md` §7 e nas
> pendências 191–192. **Restam apenas itens de IMPLEMENTAÇÃO** — que nós especificamos e o Bergson executa. Nenhum deles é decisão dele.

| # | Decisão | De quem | Trava o quê |
|---|---|---|---|
| ~~1~~ | ~~Front-matter nos MDs~~ → **NÃO. O `_indice/` é o contrato de importação.** A chave estável já vive no corpo do MD (`### ID do cliente`) e o CSV já a extrai; 1.316 MDs, zero front-matter. Front-matter seria segunda cópia de dado que já tem dono. | ✅ **resolvido** | destrava §6 |
| ~~2~~ | ~~As 9 Categories~~ → **ADOTADO: 9 por casa** (9 em cada cliente + 9 na Casa = 47 × 9 = 423). `institucional` · `jornada` · `pessoas` · `contexto-area` · `produto` · `integracao` · `protocolo` · `demanda` · `rfi`. Fechado por leitura de `organizations.schema.ts`: *"Organization legado → Tenant + um Second Brain"*; slug de organização é único **por brain**, e brain é **por cliente**. Isolamento por construção. | ✅ **resolvido** | destrava §3 |
| 3 | `agents.audienceMode` + `agent_shares` + grant `agents.consume` | **nós especificamos** → Bergson implementa | publicar o agente de suporte para a operação |
| 4 | `conversations.agentId` + `conversation_turns.agentRunId` | **nós especificamos** → Bergson implementa | a operação conversar com o agente |
| 5 | As 3 collections + `addressing_responses` + os outboxes | **nós especificamos** → Bergson implementa | §7 inteiro |
| 6 | Ligar `CATEGORY_AUDIENCE_FILTER` e allowlistar nosso brain | **operação** (é chave de config, não desenho) | permissão fina sair do papel |
| 7 | **Ampliar o payload de `context.published`** (§3-bis) — passou de "depois" para **parte do desenho base** | **nós especificamos, Bergson implementa** | tipo e audiência deixarem de competir |

---

## Fontes

**Código lido nesta sessão** (branch `codex/bhp-p16-federation-grants-back`, somente leitura):
`contexts/repository/contexts.repository.ts` ·
`contexts/services/context-publication-outbox-drainer.service.ts` ·
`runtime-definitions/services/runtime-event-bus.ts` · `runtime-definitions/trigger.schema.ts` ·
`runtime-definitions/routine.schema.ts` · `loop-execution/loop-run.schema.ts` ·
`conversations/conversation.schema.ts` · `agent-execution/agent-run.schema.ts` ·
`categories/categories.schema.ts` · `categories/category-share.schema.ts` ·
`categories/enums/category-audience.enum.ts` · `categories/query-builders/category-audience.filter.ts` ·
`categories/services/category-audience-policy.service.ts` · `approvals/approval.schema.ts` ·
`agents/agent.schema.ts` · `agents/agent-version.schema.ts` · `common/access-scope/access-scope.service.ts`

**Documentos irmãos:** `_dicionario-dados-brainhub.md` (campo a campo) ·
`_inventario-repositorios.md` (origens e o único gravável) · `_pendencias-gerais.md` (175–182)

## Governança
Somente o CEO altera conteúdo no BrainHub. Vinicius altera nesta fase por estar construindo.
Alteração neste documento exige **citar o arquivo de código** que sustenta a mudança.
