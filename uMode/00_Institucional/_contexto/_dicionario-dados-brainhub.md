# Dicionário de dados do BrainHub — o que existe no banco

> Levantado em **17 ago 2026** por leitura do código real em
> `umode-brainhub-api`, branch `codex/bhp-p16-federation-grants-back` (17/08, a mais completa:
> **29 módulos, 50 schemas, 632 arquivos em `src/`**).
> **Somente leitura. Nenhum commit, push ou checkout fora do `brainhub-umode`.**
>
> Este documento descreve **o que está construído**, com campo e invariante. Não é proposta.
> **O fluxo de dados — o que se move, quando, disparado por quem — está em
> `_fluxo-dados-brainhub.md`**, que é a autoridade sobre fluxo. Aqui é a autoridade sobre
> **campo a campo**. (O `_fluxo-crud-brainhub.md` ficou superseded no que diz respeito a fluxo.)

## Procedência — o que é código lido, o que é documento, o que é proposta minha
> Escrito em 17 ago 2026 a pedido de Vinicius, que perguntou qual das quatro coisas eu estava
> passando: entendimento meu, entendimento do Bergson, o banco do Lovable, ou dedução. **Estavam
> misturados no que eu escrevi antes.** Aqui ficam separados, e cada afirmação deste documento cai
> numa das quatro faixas.

| Faixa | O que é | Confiabilidade |
|---|---|---|
| **A · CÓDIGO LIDO** | Os **21 schemas** e **7 serviços/query-builders**, mais o catálogo de nós, lidos linha a linha em `umode-brainhub-api`. Nome de campo, tipo, enum, índice e invariante de `pre('validate')`. **Nada aqui é interpretação.** | **Alta.** É o que está escrito no repositório do Bergson. ⚠ Mas ver a ressalva abaixo. |
| **B · DOCUMENTO DO JOÃO** | Plano consolidado de 06/08 (espec vigente), PRD, `brainhub-api-auth-guardrails` (D78), bastão de 01/07, `agent-control-plane`. É **intenção declarada**. | **Média-alta** para intenção, **baixa** para estado real: o próprio ledger dele tem duas retratações de entregas que não existiam. |
| **C · BANCO DO LOVABLE** | As ~30 tabelas do Supabase, lidas em **04 ago** — `inbox_items`, `approval_requests`, `context_queues`, `agent_configs`, `job_runs`, `file_assets`. É o **legado/sandbox**, declarado "produção preservada e fonte de migração". | **Média.** É o que roda hoje com dado real, mas **não é o destino**, e não reli desde 04/08. |
| **D · PROPOSTA MINHA** | As três collections (`demands`, `addressings`, `inbox_items`), a cadeia de 8 elos, as cinco regras de rastreio, a view de auditoria agregada, e "demanda é módulo próprio". | **É proposta.** Ancorada em A, mas **não validada por ninguém**. |

### ⚠ A ressalva que qualifica a faixa A
**O código que eu li está em BRANCH, não na `main`.** A `main` do `umode-brainhub-api` tem **5
módulos** (08/08); a branch mais completa tem **29** (17/08). Ou seja: **está construído e não
integrado.** Tudo na faixa A é "existe como código escrito", não "existe em produção".

### 🔴 Qual é a fonte da verdade — e a resposta incomoda
**Nenhuma das quatro, isoladamente. E isso é achado, não desculpa.**
- Para **o que existe**: o **código** (faixa A) é soberano. Documento não sobrepõe schema.
- Para **o que se pretende**: o **plano consolidado** (faixa B) é a espec vigente declarada.
- Para **o que roda hoje com dado real**: o **Lovable** (faixa C).

E há um vazio no meio: a diretriz `brainhub-arquitetura.md` está `superseded` desde 08/08 e nomeia
como sucessores **`UmodeApp/umode-brainhub@docs/CONTEXT.md`** e
**`UmodeApp/umode-brainhub-api@docs/CONTEXT.md`**. **O segundo não existe no repositório.**
> **Portanto: hoje o BrainHub não tem fonte de verdade declarada e existente para arquitetura de
> dados.** O que existe é código numa branch, um plano num vault, e um sandbox rodando. Fechar isso é
> decisão de governança, não de engenharia — e é a pergunta que vale levar ao João e ao Bergson.

### Um dado da faixa C que muda a leitura da lacuna
**O banco do Lovable TEM `inbox_items` e `approval_requests`.** As duas coisas que faltam no Mongo
**existem no sandbox** — ou seja, a camada operacional foi construída lá e **não foi levada** ao
backend novo. Não é conceito ausente: é migração não feita.

## Cobertura
> ⚠ **Contagem corrigida:** `git ls-tree` na branch conta **50 arquivos `*.schema.ts`**, não 49.
> O cabeçalho deste documento dizia 49 — errado por um.

**Campos lidos por inteiro (21 de 50 schemas):** `tenants` · `brains` · `people` · `memberships` ·
`areas` · `area_memberships` · `approvals` · `approval_audit_events` · `audit_events` ·
`context_relations` · `contexts` · `context_versions` · `triggers` · `routines` · `agents` ·
`agent_versions` · `agent_runs` · `categories` · `category_shares` · `conversations` (+
`conversation_turns`) · `loop_runs`.

**Serviços e query-builders lidos por inteiro (7):** `access-scope.service` ·
`runtime-event-bus` · `context-publication-outbox-drainer.service` ·
`category-audience-policy.service` · `category-audience.filter` ·
`contexts.repository` (transação de publicação) · `category-audience.enum`.

**Collection fora da lista de schemas:** `context_publication_outbox` — é collection **crua**, acessada
por `db.collection(...)` sem schema Mongoose. Existe no banco e **não aparece em nenhuma
varredura por `*.schema.ts`**. Provável que haja outras; verificar antes de afirmar total.

**Nomes conhecidos, campos NÃO lidos (29 schemas):** run-daily-counter · execution-audit-event ·
agent-audit-event · area-membership-audit-event · category-policy-audit-event · context-chunk ·
context-pack (+audit) · conversation-audit-event · federation-connection (+audit) ·
federation-discovery (node, profile, audit) · file · file-version · folder · invitation (+audit) ·
llm-connection · encrypted-credential · loop · loop-version · loop-audit-event · organizations ·
seed · seed-batch · tenant-bootstrap-audit · ask-daily-counter.

---

## 1 · A cadeia de hierarquia — fechada e verificada

```
tenants ──┬──► brains (SECOND_BRAIN) ──► areas ──► area_memberships ──► people
          │                                │
          └──► memberships ────────────────┘
people ──────► brains (PERSONAL)
```

### `tenants`
`slug` (obrigatório, **lowercase**, único) · `name` · `status` `ACTIVE|INACTIVE` · timestamps.

### `brains` — onde a fronteira inviolável é invariante de schema
`type` `PERSONAL|SECOND_BRAIN` (**immutable**) · `name` · `ownerPersonId?` (immutable) ·
`tenantId?` (immutable) · `status`.

> **`pre('validate')` impede a violação no dado, não na aplicação:**
> `PERSONAL` exige `ownerPersonId` e **não pode ter `tenantId`** · `SECOND_BRAIN` exige `tenantId` e
> **não pode ter `ownerPersonId`**.
> Dois índices únicos parciais: **um Personal Brain por pessoa** e **um Second Brain por tenant**.

### `people`
**`trustedSubjectId`** (único, **immutable**) — é o `sub` do Cognito, via `req.executor` ·
`email` (lowercase) · `status`.

### `memberships`
`personId` + `tenantId` (**únicos juntos**, ambos immutable) · `roleId` (string, referência — não é
enum) · `grants: string[]` · `status` `ACTIVE|INACTIVE|REVOKED`.

### `areas`
`tenantId` + `brainId` (**immutable**) · `slug` (**lowercase**, único por `brainId`) · `name` ·
**`adminSubjectId`** · `status`. **`strict: 'throw'`** — campo desconhecido lança erro.
> ⚠ **`adminSubjectId` guarda `Person.trustedSubjectId`, NÃO um ObjectId de Person** — está
> comentado no código. Qualquer collection nova tem de seguir a mesma convenção, senão o JOIN não fecha.

### `area_memberships` — o modelo de permissão real
`personId` + `areaId` (únicos juntos) · `role` `ADMIN|MEMBER` · **`readableTiers[]`** ·
**`writableTiers[]`** · **`decisionTiers[]`** · `grants: string[]` · `grantedBy` · `validFrom` ·
`expiresAt?` · `status`.

> **Três descobertas que nenhum documento continha:**
> 1. **Autoridade de decisão é separada de leitura e escrita** — três listas de tier distintas, com
>    comentário explícito no código. É mais granular que o MOLE do bastão **e** que os 5 níveis do PRD.
> 2. **D85 trava tudo em T2.** O `pre('validate')` invalida qualquer tier ≠ T2 nas três listas, até o
>    João resolver a política de T0/T1. É trava executável, não aviso.
> 3. `expiresAt` tem de ser maior que `validFrom`, validado no schema.

---

## 2 · Contexto, versão e remoção

### `contexts`
`organizationId` (obrigatório) · `tenantId?` · `brainId?` · `areaId?` · `categoryId` · `slug` ·
`title` · `content` · **`metadata: Object`** · `source` `browser|api|seed` · `revision` ·
`currentVersionId?` · `versionSequence` (oculto) · **`approvalTier?`** · `indexStatus` ·
`indexedRevision` · `chunkCount` · `indexError?`
**Remoção e restauração com procedência completa:**
`deletedAt?` · `deletedBySubjectId?` · `deletedByPersonId?` · `deletedReason?` ·
**`deletedAuditEventId?`** · `restoredAt?` · `restoredBySubjectId?` · `restoredByPersonId?` ·
**`restoredAuditEventId?`**

> **O soft delete aponta para o próprio evento de auditoria que o registrou.** É o primitivo de
> rastreio que eu ia propor, já implementado. O índice único de slug é parcial
> (`deletedAt: null`), então remover libera o slug.
> ⚠ **`tenantId`, `brainId` e `areaId` são OPCIONAIS** — há backfill em curso (`areaBackfillRunId`).
> Qualquer consulta multi-tenant hoje tem de tolerar nulo.

### `context_versions` — append-only e endereçado por conteúdo
Tudo **immutable**, `strict: 'throw'`. `contextId` · `brainId` · `tenantId?` · `version` (≥1) ·
`title` · `content` (máx **1.000.000** chars) · `metadata` (máx **100.000 bytes**) ·
**`contentHash`** com formato obrigatório `sha256:[64 hex]` · **`supersedesVersionId?`** · `createdBy`.
**Dois guardas rejeitam qualquer mutação:** `delete|findOneAndDelete|findOneAndReplace|findOneAndUpdate|replace|update` e `bulkWrite` lançam `"ContextVersion is append-only"`.

---

## 3 · Decisão — `approvals`

`brainId` · `tenantId?` · `areaId?` · **`subjectType` + `subjectRef`** (alvo polimórfico) ·
`requestedTier` · `classifiedTier?` · **`band`** · `classificationReason` · `status` ·
`createdBy` · `decidedBy?` · `decisionReason?` · `decidedAt?` · **`decisionAuthority?`** · `deletedAt?`

| Enum | Valores |
|---|---|
| `ApprovalTier` | `T0` · `T1` · **`T2_DOCTRINE`** · **`T2_RECORD`** |
| **`ApprovalBand`** | **`AUTO_ARCHIVE`** · **`WEEKLY_BATCH`** · **`JOAO_REQUIRED`** · **`AREA_LEAD_REQUIRED`** |
| `ApprovalDecisionAuthorityKind` | `ACCOUNT_ADMIN` · `AREA_LEAD` |
| `ApprovalStatus` | `PENDING` · `APPROVED` · `REJECTED` · `ARCHIVED` |

> **`ApprovalBand` é a resposta ao problema de vazão** que o brief para o Hermes chamava de gargalo
> humano: o que arquiva sozinho, o que vai em lote semanal, o que exige o João e o que exige o líder
> da área. **Estava como pergunta aberta em julho; hoje é enum.**
> **T2 é dividido em `DOCTRINE` e `RECORD`** — doutrina (regra) e registro (fato) têm bandas
> diferentes. Distinção que não existe em nenhum documento nosso.
> `subjectType` + `subjectRef` sendo polimórfico é **onde o endereçamento vai se pendurar**.

### `approval_audit_events`
`brainId` · `tenantId?` · `areaId?` · `approvalId` · `actorPersonId` · **`fromStatus` → `toStatus`** ·
`reason` (obrigatório) · `occurredAt` · `decisionAuthority?`. É log de **transição de estado**, não de
snapshot.

---

## 4 · Auditoria — `audit_events`

`action` (enum) · **`resourceType` + `resourceId`** (polimórfico) · `occurredAt` ·
**`phase`** (default **`PRE_MUTATION`**) · `brainId` · `tenantId?` · `categoryId?` · `areaId?` ·
**`actorSubjectId` + `actorPersonId` + `actorMembershipId?`** · `reason?` · **`changedFields[]`**

> **Três invariantes que tornam isso trilha e não log:**
> 1. **Append-only com três guardas:** `pre('save')` lança se não for novo; o regex de mutação lança;
>    `bulkWrite` lança. Mensagem: `"AuditEvent is append-only"`.
> 2. **`phase: PRE_MUTATION`** — a auditoria é escrita **antes** da mutação. Se a mutação falhar,
>    existe registro da tentativa. É o oposto de logar depois do fato.
> 3. **Ator em três partes:** subject do Cognito + person local + membership. Permite responder "com
>    que vínculo ele fez isso", não só "quem fez".

⚠ **Dois padrões de auditoria coexistem:** este `audit_events` é **genérico** (polimórfico por
`resourceType`), mas `approvals`, `agents`, `areas`, `loops`, `conversations`, `context-packs`,
`invitations`, `federation-*` e `agent-execution` têm **collections próprias** de audit. **Montar a
história completa de um endereçamento exige compor as duas famílias.** Ponto a resolver, registrado
como item 2 da §13 do plano.

---

## 5 · Relações — `context_relations`

`brainId` · `tenantId?` · `sourceContextId` · `targetContextId` · `sourceAreaId?` · `targetAreaId?` ·
`relationType` · **`provenanceKind`** · `provenanceSourceRef?` · `ownerPersonId` ·
`sensitivityTier` · `deletedAt?` — **quase tudo `immutable`**, `strict: 'throw'`.

**`ContextRelationType` — 7 valores, não 13:**
`RELATED_TO` · `SUPPORTS` · `CONTRADICTS` · `DERIVED_FROM` · `REFERENCES` · `DEPENDS_ON` · `SUPERSEDES`

**`ContextRelationProvenanceKind`:** `MANUAL` · `GENERATED` · `IMPORTED`

> ⚠ **Correção do que eu havia escrito.** O plano §8.1 lista 13 tipos; **o código tem 7.** Não
> existem `links_to`, `part_of`, `used_by_agent`, `feeds_loop`, `produces`, `belongs_to_area` nem
> `belongs_to_pillar`. **Nossa tipagem de relações tem de usar os 7 do código**, não os 13 do
> documento. Pertencimento a área já é resolvido por `sourceAreaId`/`targetAreaId`, não por tipo.
>
> **Relação é immutable — não se edita, se apaga e recria.** E `provenanceKind` distingue relação
> feita à mão de relação gerada por agente ou importada: é exatamente o que precisamos para migrar
> os nossos `[[wikilinks]]` como `IMPORTED` e deixar rastro.
> Invariantes: não existe auto-relação (`source ≠ target`), e **só T2 é permitido, por D85**.

---

## 6 · Disparo — `triggers` e `routines`

### `triggers` — dispara um Loop por evento
`brainId` · `tenantId?` · **`loopId` + `loopVersionId?`** · `name` (máx 120) · `status` ·
**`eventType`** (lowercase, immutable) · **`matchMode`** `ALL|ANY` · **`clauses[]`** · `ownerPersonId` ·
`deletedAt?`
`TriggerClauseOperator`: `EQUALS` · `NOT_EQUALS` · `IN` · `EXISTS`
`TriggerStatus`: `ACTIVE` · `INACTIVE` · `PAUSED` — **default `INACTIVE`**

### `routines` — dispara um Loop por cron
`brainId` · `tenantId?` · `loopId` + `loopVersionId?` · `name` · `input?` (máx 100k) · `status` ·
**`schedule: { kind: CRON, expression, timezone }`** · **`dedupeKey`** (immutable) ·
**`maxCostPerRunUsd?`** · `nextRunAt?` · `lastEnqueuedAt?` · `ownerPersonId` · `deletedAt?`

> **Quatro das regras que eu ia propor já estão no schema:**
> **deduplicação** (`dedupeKey`, único por brain), **limite de custo** (`maxCostPerRunUsd`),
> **teste seguro antes de ativar** (default `INACTIVE` nos dois) e **pausa** (status `PAUSED`).
> O índice parcial `(status, nextRunAt)` só sobre `ACTIVE` é a consulta do agendador.
>
> ⚠ **Nota de desenho importante:** trigger e rotina **disparam um Loop**, não uma ação arbitrária.
> Logo "criar demanda no inbox" **não é um tipo de ação de trigger** — é um **nó dentro de um Loop**.
> Isso muda onde a nossa camada de demanda se encaixa.

---

## 6-bis · Loops — o executor, e onde a demanda vai nascer

### `loops`
`brainId` · `tenantId?` · `slug` (lowercase, único por brain enquanto vivo) · `name` · `status`
`ACTIVE|INACTIVE|PAUSED` (**default `INACTIVE`**) · `pausedReason?` · **`activeVersionId?`** ·
**`draftVersionId?`** · `ownerPersonId` · `sensitivityTier` · `deletedAt?`. `strict: 'throw'`.
> Separação **draft × active** no próprio documento: edita-se o rascunho, promove-se a ativo.

### `loop_versions` — append-only, e um Loop é um GRAFO TIPADO
Tudo immutable. `loopId` · `brainId` · `tenantId?` · `version` · `status` `DRAFT|ACTIVE` ·
**`graph: { nodes[], edges[], contracts, policies }`** · `agentVersionIds[]` ·
**`contractHash`** `sha256:...` · **`origin`** · `supersedesVersionId?` · `createdBy`.

**`origin` é a procedência da definição:** `kind` · `templateKey` · `templateVersion` · `repo` ·
`path` · `commitSha` — e **se `kind` é `GIT_TEMPLATE`, os cinco são obrigatórios**.
> **Isto é o elo com repositório Git que faltava:** um Loop pode ter origem declarada em `repo` +
> `path` + `commitSha`. É o mecanismo pelo qual um contexto nosso, versionado no Git, se torna
> definição executável com procedência verificável.

Invariantes do grafo: máximo **200 nós** · `nodeId` único · aresta só entre nós existentes ·
grafo máximo **1 MB**. Mais dois guardas de append-only.

### `loop_runs` — a execução, com procedência de disparo
`brainId` · `tenantId?` · `loopId` · `loopVersionId` · `status` `queued|running|succeeded|failed` ·
`input` · **`sourceType` `MANUAL|ROUTINE|TRIGGER`** · **`sourceId?`** · `scheduledFor?` ·
`dedupeKey?` (único por brain) · `queueJobId?` · `maxCostUsd?` · `output?` · **`steps[]`** ·
`inputTokens?` · `outputTokens?` · `costUsd?` · `error?` ·
**`createdByPersonId` + `createdBySubjectId`** · `startedAt?` · `finishedAt?`

Cada `step`: `nodeId` · `type` · `status` `skipped|succeeded|failed` · `agentVersionId?` ·
`output?` · tokens · `costUsd?` · `error?`.
> **`sourceType` + `sourceId` é a resposta a "por que isso rodou".** E `steps[]` guarda o resultado
> **por nó**, com custo — é onde o resultado de um nó de ação fica registrado.

### O catálogo de nós — **16 tipos com contrato de dado tipado**
`TRIGGER` · `GATE` · **`ACTION`** · `AGENT` · `WRITEBACK` · **`NOTIFICATION`** · `METRIC` ·
**`APPROVAL`** · `TERMINAL` · `JURY_CONSENSUS` · `PARALLEL_MAP` · `ITERATIVE_REPAIR` ·
`FAILURE_ROUTER` · `PAIR_BARRIER` · `COLLECTION_BARRIER` · `READ_BACK_GATE`

**11 contratos de dado:** `ANY` · `COLLECTION` · `ITEM` · `JURY_RESULT` · `DECISION` · `FAILURE` ·
`REPAIR_DIRECTIVE` · `ARTIFACT` · `PAIRED_COLLECTION` · `RELEASE` · `READ_BACK_EVIDENCE`

> **O `LoopGraphValidator` recusa aresta cuja saída não case com a entrada do destino** — um Loop é
> **grafo de dataflow tipado**, não fluxograma livre. E a condição da aresta tem de estar **declarada**
> no tipo do nó de origem (`pass`, `hold`, `publish`, `forEachItem`, `repairable`,
> `attemptsExhausted`, `artifactChanged`, `complete`, `merged`…).
>
> **Quatro tipos de nó encodam a disciplina de governança da casa como estrutura de dado:**
> `JURY_CONSENSUS` (quórum, agregação por dimensão, zero hard-fail) · `ITERATIVE_REPAIR` (exige
> **mudança de hash do artefato** para contar como progresso) · `FAILURE_ROUTER` (roteia falha por
> código de motivo) · **`READ_BACK_GATE`** (verifica `routes`, `media`, `sitemap`, `robots` com
> status HTTP esperado e timeout). O "exit 0 não prova trabalho" e o "nada ativo sem read-back"
> viraram tipo de nó.

## 6-ter · Agentes e autorização — e a lacuna que o Vinicius encontrou

### `agents`
`brainId` · `tenantId?` · `slug` (lowercase, único por brain) · `name` · **`kind`** (immutable) ·
`status` (default `INACTIVE`) · `currentVersionId?` · `ownerPersonId` · **`sensitivityTier`**
(immutable) · `deletedAt?`. `strict: 'throw'`.

**`AgentKind` = `INTERNAL` | `USER_DEFINED`.**
> ⚠ **A distinção que o Vinicius travou — agente estrutural × agente de interação — NÃO existe no
> schema.** `kind` classifica **quem criou** (interno da plataforma × definido pelo usuário), não
> **quem consome** nem **o que faz**. São eixos diferentes e o eixo dele não está modelado.

### `agent_versions` — append-only, e é onde a instrução do agente vive
Tudo immutable. `agentId` · `brainId` · `tenantId?` · `version` · `status` `DRAFT|ACTIVE` ·
**`instruction`** (máx **100.000 chars**) · **`tools[]`** (`toolKey` + `config`) ·
**`providerPolicy`** · **`contextPackRefs[]`** (`packId` + `packVersion`) · **`limits`** ·
`contentHash` sha256 · **`origin`** · `supersedesVersionId?` · `createdBy`.

- **`providerPolicy`**: `allowedProviders[]` · **`defaultModel`** · `maxCostPerRunUsd?` ·
  `llmConnectionId`. **É aqui que se escolhe o modelo** — por versão de agente, não global.
- **`limits`**: `timeoutSeconds` (máx **900**) · `maxOutputTokens` (máx **64.000**).
- **`origin`**: `kind` `user` | **`git-template`** — e se for `git-template`, exige `repo`, `path` e
  `commitSha`. **A instrução de um agente pode vir do nosso repositório Git, com procedência por
  commit.**

### 🔴 Como se decide quem pode consumir um agente — **não se decide**
O `AccessScopeService` (`src/common/access-scope/access-scope.service.ts`) é a autorização real, e
enumera **18 operações**: `organizations.*` · `categories.*` · `contexts.*` (incl. `reindex` e
`search`) · **`ask.answer`**.

**Não existe nenhuma operação `agents.*` na lista.** E `agents` não tem `visibility`, `audience`,
`allowedRoles` nem qualquer campo de consumo. Logo:
> **A pergunta "quem pode consumir este agente" não tem resposta no banco hoje.** Não é que a resposta
> seja permissiva — é que o eixo não existe.

**O que existe de autorização, e é elegante:**
1. **Regra base:** `requestedOrganizationId === executorOrganizationId` → permite. Diferente → nega
   com `organization-mismatch`. O escopo é **organização**, não área nem pessoa.
2. **Exceção individual governada** (`TrustedIndividualAccessException`): por pessoa, por operação,
   por organização, com `validFrom`/`expiresAt` e **duração máxima de 24 horas**.
3. **Segregação de funções por invariante:** `subjectId === grantedBySubjectId` é rejeitado —
   **ninguém concede exceção a si mesmo**.
4. **Fail-closed na auditoria:** se o `auditWriter` não estiver disponível, o acesso é **negado**
   (`exception-audit-unavailable`). Não há acesso sem trilha.
5. **8 motivos de negação enumerados**, cada um auditado: `missing-context` ·
   `organization-mismatch` · `invalid-operation` · `invalid-exception` · `expired-exception` ·
   `revoked-exception` · `exception-scope-mismatch` · `exception-audit-unavailable`.
6. A exceção "deve ser resolvida por armazenamento interno governado, **nunca aceita de input do
   cliente**" — está no comentário do código.

### 🔺 CORREÇÃO — há um SEGUNDO autorizador, e é ele que usa os tiers
> Escrito primeiro assim: *"os `readableTiers`/`writableTiers`/`decisionTiers` de `area_memberships`
> NÃO estão ligados à autorização — existem como dado e não são consultados"*. **Errado.** Eu havia
> lido **um** caminho de código e generalizei para o sistema. Corrigido no mesmo dia.

`CategoryAudiencePolicyService` (`src/modules/categories/services/category-audience-policy.service.ts`)
**consulta os tiers**: a linha 58 filtra membership por `readableTiers.includes(T2)`, e
`authorizeStewardWrite` exige `writableTiers.includes(T2)` **mais** `grants[]` **mais**
`role === ADMIN`. **Existem dois autorizadores distintos:**

| | `AccessScopeService` | `CategoryAudiencePolicyService` |
|---|---|---|
| Granularidade | **organização** | **área + tier + share** |
| Vigência | **sempre ligado** | **[F] atrás de flag** `CATEGORY_AUDIENCE_FILTER=on` **+ allowlist por `brainId`** |
| Escopo de brain | qualquer | **só Second Brain** (`PERSONAL_BRAIN_NOT_SUPPORTED`) |
| Mecanismo | checa e nega | **filtra a query** — quem não tem audiência não vê o documento existir |

**`AudienceMode` = `AREA` | `SELECTED_AREAS` | `TENANT_WIDE`** (`category-audience.enum.ts`), com
`category_shares` (`subjectType` `CATEGORY|CONTEXT` · `targetAreaId` · `effect` `ALLOW|DENY` ·
`approvalId?` · `revokedAt?`, tudo immutable) e **12 códigos de motivo enumerados**.
`membership.grants[]` carrega capacidades nomeadas: `categories.steward`, `categories.share.manage`.

> **Este é o padrão a copiar para agentes** — `agents.audienceMode`, `agent_shares`, grant
> `agents.consume` — em vez de inventar modelo novo. Desenho em `_fluxo-dados-brainhub.md` §4.3.
>
> ⚠ **O modelo fino existe e está DESLIGADO.** "Existe em código" ≠ "está vigente".

## 7 · O que NÃO existe — corrigido depois de ler o catálogo de nós
Varredura por módulo **e** por nome de arquivo nas **115** branches — reconfirmada em 17/08 com `git log --all -S`: `Addressing`, `InboxItem` e `DemandStatus` aparecem em **0 commits**, nem como arquivo criado nem no conteúdo de qualquer commit do histórico:

| Domínio | Situação |
|---|---|
| **`demands` / `task`** | ❌ não existe como collection **nem** como tipo de nó |
| **`addressings`** | ❌ não existe |
| **`inbox_items`** | ❌ não existe |
| `notification` | ⚠️ **existe como TIPO DE NÓ** (`LoopNodeType.NOTIFICATION`), mas **não há collection** que registre a entrega — canal, estado, dedupe, erro |

> ⚠ **Correção do que eu havia escrito.** Eu disse "quatro collections faltam". São **três collections**
> (`demands`, `addressings`, `inbox_items`) mais **uma lacuna menor**: notificação já é vocabulário do
> Loop, falta o registro de entrega.
>
> **E o encaixe é outro do que eu propunha.** "Criar demanda" não é campo de trigger nem collection
> solta: é um **nó `ACTION`** dentro de um Loop, cujo resultado fica em `loop_runs.steps[]`. Avisar é
> um nó **`NOTIFICATION`**. Aprovar é um nó **`APPROVAL`**, que já existe. **O vocabulário do fluxo
> está construído; falta onde a demanda e o endereçamento persistem.**

Decisão, aprovação, banda de vazão, versão append-only, auditoria pré-mutação, relação com
procedência, trigger com cláusulas, rotina com dedupe e teto de custo, permissão por três tiers,
lixeira com procedência, grafo tipado com 16 nós e execução com custo por passo: **tudo já está
construído.**

---

## 8 · Convenções do banco que a nossa documentação deve seguir
Extraídas do código, e valem como padrão para qualquer coisa que a gente proponha:
1. **`slug` é sempre `lowercase`** e único **dentro do pai** — nunca global, exceto `tenants`.
2. **Chave de escopo é `immutable`.** `tenantId`, `brainId`, `areaId` não se alteram depois de criados.
3. **Índice único é parcial em `deletedAt: null`** — remover libera o identificador.
4. **`strict: 'throw'`** nas collections novas: campo desconhecido é erro, não é ignorado.
5. **Ator é sempre `trustedSubjectId`** (o `sub` do Cognito), não ObjectId — e quando há vínculo,
   registra-se também `personId` e `membershipId`.
6. **Append-only se protege por guarda de schema**, não por convenção.
7. **Tudo que remove registra quem, por quê e o id do evento de auditoria.**
8. **Enum é `SCREAMING_SNAKE` em maiúsculas.** O nosso padrão de MD usa rótulo em português; a
   tradução tem de ser explícita no protocolo, não implícita.

## Fontes e referências
### Documentos consultados
- `umode-brainhub-api` (`UmodeApp`), branch `codex/bhp-p16-federation-grants-back`, 17 ago 2026.
  Schemas lidos por inteiro: os 14 listados na cobertura.
- Decisões referenciadas no próprio código: **D85** (tiers de Área travados em T2) e
  **D92** (autoridade de aprovação), citadas em comentário de schema.
- **Leitura somente leitura. Nenhum commit, push ou checkout** fora do `brainhub-umode`.

## Governança
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**.
