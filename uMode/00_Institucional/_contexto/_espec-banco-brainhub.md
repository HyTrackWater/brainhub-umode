# ESPEC-BANCO-001 v2 — Especificação do banco do BrainHub

> Escrita em **17 ago 2026** por Vinicius Risoléo (com Claude Code) para implementação por Bergson.
> **Nomes de campo, collection e relação em inglês** — padrão travado no `CLAUDE.md`.
>
> **Autoridade:** definir collections, campos e forma de relacionamento é papel de quem vive a operação
> (Vinicius e João). O código atual é autoridade sobre **o que existe**, não sobre **o que deve
> existir** — foi escrito traduzindo uma explicação. Divergência entre este documento e o schema
> atual **não é erro de entendimento: é tradução a corrigir.**

## 0 · Declaração de completude — leia antes de confiar em qualquer linha

| # | O que este documento NÃO resolve | Por quê |
|---|---|---|
| 1 | Campos de **21 dos 50 schemas** existentes | Não lidos campo a campo. **v2: cobertura subiu de 21 para 29 lidos** — os que podiam mudar o desenho (`seeds`, `context_packs`, `files`/`folders`, `federation`) já foram lidos. Fila e risco na §6-bis.8. |
| 2 | Migração do dado do **Supabase/Lovable** | `inbox_items` e `approval_requests` existem lá com dado real; o plano de migração é trabalho separado. |
| ~~3~~ | ~~A membrana Casa↔cliente~~ → ✅ **RESOLVIDO na v2:** é uma `federation_connection` concedida, com 4 níveis (`discover`/`read`/`query`/`contribute`). Ver §6-bis.6. |
| 4 | Volumetria, sharding e retenção | Precisa de dado de uso que ainda não existe. |
| 5 | O **`context_policy` do João** traduzido campo a campo | Desenhado por ele em 09/07, **nunca implementado**. Proposta na §3.5, a validar com ele. |
| 6 | Se `02_Atendimento` pode **ajustar** algo do agente além de operar | Ambiguidade declarada na §1.2-bis. Especifiquei a leitura conservadora; um `agents.tune` precisa ser dito. |

**Grau por afirmação:** `[C]` código lido · `[J]` desenho do João, lido no vault dele · `[P]` proposta
nossa · `[D]` decisão pendente.

---

## 1 · Conformidade — o que já foi desenhado × o que o banco tem

> O Vinicius pediu garantia de que a estruturação está conforme o desenhado. **Fui verificar.
> Em hierarquia e decisão, está. Em agentes, não está — e a divergência é grande.**

### 1.1 Taxonomia estrutural — ✅ conforme
| O que desenhamos | No banco | Situação |
|---|---|---|
| Instituição → Institucional → Áreas → Subáreas → Pessoas | `tenants` → `brains` → `areas` → `area_memberships` → `people` | ✅ `[C]` |
| 8 áreas internas / 14 canônicas de cliente | `areas.slug` único por `brainId` | ✅ cabe sem alteração |
| Isolamento absoluto entre clientes | 1 Second Brain por tenant (índice único parcial) + cascade por `organizationId` | ✅ **invariante de banco**, não convenção |
| Pessoa interna nunca duplicada no cliente | `people` global + `memberships` por tenant | ✅ |
| Tiers T0/T1/T2 | `SensitivityTier`, travado em **T2 por D85** | ⚠ conforme, mas **T0/T1 bloqueados** até o João liberar |
| `ApprovalBand` (faixas de vazão de aprovação) | `ApprovalBand`: `AUTO_ARCHIVE`, `WEEKLY_BATCH`, `JOAO_REQUIRED`, `AREA_LEAD_REQUIRED` | ✅ `[C]` — e cobre o `EXIGE_JOAO` do João |

⚠ **Ressalva sobre "taxonomia":** o `TAXONOMIA_UMODE.md` do vault é **"Taxonomia uMode — Catalog
AI"**: hierarquia e grupos de atributos de **produto de moda**. **Não é a taxonomia estrutural do
BrainHub** e não entra nesta espec. Conformidade aqui é com a hierarquia, os tiers e as `ApprovalBand` de
decisão.

### 1.2 Agentes — 🔴 NÃO conforme, e é a divergência mais séria do banco

O João definiu a ficha de agente em **09 jul 2026**, promovida a canônica por **D32, aprovada por
ele** (`_sistema/brainhub/governance/template-ficha-agente.md`). O registry vigente
(`agent-control/runs/cron_registry_sync_20260716T150445/agents.json`) tem os campos em uso real.
**Comparação campo a campo:**

| Campo desenhado pelo João `[J]` | No banco `[C]` | Veredito |
|---|---|---|
| `kind`: **`agent` · `worker` · `poller` · `sentinel` · `reconciler`** | `AgentKind`: `INTERNAL` \| `USER_DEFINED` | 🔴 **semântica diferente.** O do João diz **o que o agente faz**; o do banco diz **quem o criou**. |
| `visibility`: **`operator` · `system`** | — | 🔴 **ausente.** É exatamente o eixo estrutural × interação. |
| `context_policy{}` (4 flags) | — | 🔴 **ausente.** É o eixo de "quem pode consumir". |
| `canonical_write: false` | — | 🔴 ausente. *"Escrita canônica direta é proibida."* |
| `external_send: false` | — | 🔴 ausente. Proibido por padrão. |
| `requires_guard: true` | — | 🔴 ausente |
| `reads[]` / `writes[]` | — | 🔴 ausente |
| `activation_requires_joao: true` | `ApprovalBand.JOAO_REQUIRED` | ⚠ **expressável**, mas não amarrado ao agente |
| `status`: 6 estados (`draft`, `aprovado`, `ativo_local`, `ativo_time`, `bloqueado`, `aposentado`) | `status` (default `INACTIVE`) | ⚠ **insuficiente** — perde `ativo_local` × `ativo_time`, que é a fronteira de exposição ao time |
| `execution_status` **separado de** `delivery_status` | `agent_runs.status` só | 🔴 **ausente, e é o achado — ver 1.3** |
| `skills[]` (nomeadas) | `tools[]` (`toolKey` + `config`) | ⚠ próximo, não igual |
| `model` / `provider` | `providerPolicy.defaultModel` / `allowedProviders[]` | ✅ conforme |
| `schedule` / `timezone` | `routines.schedule{kind,expression,timezone}` | ✅ conforme |
| `workflow_id` | `loops` (o Loop **é** o workflow) | ✅ conforme |
| `latest_output` / `last_error` | `agent_runs.output` / `.error` | ✅ conforme |
| `repeat{times, completed}` | — | ⚠ ausente (há `run_daily_counter`, não lido) |

> 🔴 **CORREÇÃO DE UMA AFIRMAÇÃO MINHA.** Eu disse ao Vinicius que "a regra de quem pode consumir um
> agente **não existe** — o eixo não existe". **Incompleto.** Não existe **no banco**. **No desenho do
> João existe desde 09/07**, como `context_policy` + `visibility` + `permissions`. Eu havia
> verificado o código e **não o desenho** — quarta vez que concluo sobre o sistema tendo olhado uma
> fonte só. O eixo não precisa ser inventado: **precisa ser implementado.**

### 1.2-bis O modelo de autoridade sobre agente — decidido pelo Vinicius em 17 ago 2026 `[D]` ✅
> Ele registrou: *"quem tem o poder de treinar, retreinar, aposentar, desativar — quem define como o
> agente vai trabalhar — é a área responsável (tecnologia no caso). A área de atendimento vai mexer
> direto... poderemos barrar que o comercial consuma esse agente."*

**São três papéis distintos, e o banco tem vocabulário para os três:**

| Papel | Área no caso do agente uFlow | O que pode | Como se expressa no dado |
|---|---|---|---|
| **Steward — define** | **`06_Tecnologia`** | treinar, retreinar, publicar versão, aposentar, desativar | `agents.stewardAreaId` + grant **`agents.steward`** + `decisionTiers` na `area_membership` |
| **Operador — usa direto** | **`02_Atendimento`** | consumir intensamente; acionar; **não** altera instrução | grant **`agents.operate`** |
| **Consumidor — pode ser barrado** | ex.: `01_Comercial` | consultar, se não houver negativa | `agent_shares` com `effect: DENY` no `targetAreaId` |

**Duas consequências de desenho que essa decisão trava:**

1. **O modelo é permitir-por-padrão-com-negativa-explícita**, não o inverso. A frase "poderemos
   barrar que o comercial consuma" só faz sentido assim. Traduz para
   **`audienceMode: TENANT_WIDE` + `agent_shares` com `effect: DENY`** por área.
   ✅ **E a precedência já está decidida em código:** o filtro de audiência de categoria faz
   `_id: { $nin: explicitlyDeniedCategoryIds }` **depois** do `$or` de permissões — ou seja,
   **DENY vence ALLOW**. `agent_shares` herda essa regra, não inventa outra.

2. **Definir ≠ operar.** Hoje `agents` tem um só `ownerPersonId`, o que funde os dois papéis. A
   separação exige `stewardAreaId` **mais** os dois grants distintos — senão quem opera acaba podendo
   republicar instrução, que é exatamente o que o Vinicius separou.

⚠ **Uma ambiguidade que eu não vou resolver por conta própria:** "a área de atendimento vai mexer
direto" admite duas leituras — *operar intensamente* ou *ajustar alguma configuração*. Eu especifiquei
como **operar, sem alterar instrução** (a leitura conservadora, porque a frase anterior diz que quem
define é Tecnologia). **Se Atendimento também puder ajustar algo — por exemplo o modelo ou o limite de
custo, sem tocar na instrução — isso é um terceiro grant (`agents.tune`) e precisa ser dito.**

### 1.3 Execução ≠ entrega — o achado que o João provou na prática `[J]`
No registry dele, o agente `pendencias-joao-lembrete` está com
`last_status: "ok"` **e** `last_delivery_error: "platform 'discord' not configured/enabled"`.
**Rodou certo e não chegou a ninguém.**

> **Portanto: `execution_status` e `delivery_status` são campos distintos e obrigatórios.** Um
> `loop_run` com `status: succeeded` cujo nó de notificação não entregou é um **falso positivo de
> operação** — o pior tipo de erro num sistema de endereçamento, porque parece que funcionou.
> O banco hoje tem **um** status. Precisa dos dois.

---

## 2 · Alterações em collections existentes

### 2.1 `contexts` — o tipo do documento vira campo de primeira classe `[P]`
```
+ type: string, required, enum:
    'institucional' | 'jornada' | 'pessoas' | 'contexto-area' | 'produto'
  | 'integracao'   | 'protocolo' | 'demanda' | 'rfi'
+ index: { brainId: 1, tenantId: 1, type: 1, updatedAt: -1 }
```
**Por quê:** o tipo **é** atributo do documento. Hoje não existe, e a única forma de roteá-lo seria
sobrecarregar `categories` — o que gastaria o eixo de audiência. **Ver §2.2.**

### 2.2 `context.published` — o payload do evento ganha dois campos `[P]`
```
payload atual:  { contextId, versionId, revision, categoryId, areaId }
payload novo:   { contextId, versionId, revision, categoryId, areaId,
                  type,              ← de contexts.type
                  sensitivityTier }  ← para trigger sensível a confidencialidade
```
**Por quê:** hoje uma `trigger` **não consegue distinguir** "publicaram uma demanda" de "publicaram
um institucional". Resolver na origem é uma linha no publisher; contornar custa o modelo inteiro.
⚠ A comparação de cláusula só aceita **string** — ambos os campos devem ser string.

### 2.3 `agents` — os campos de governança que o João definiu `[J]` + `[P]`
```
~ kind        → RENOMEAR o atual para `authorship` ('INTERNAL' | 'USER_DEFINED')
+ kind        → NOVO enum, semântica do João:
                'AGENT' | 'WORKER' | 'POLLER' | 'SENTINEL' | 'RECONCILER'
+ visibility  → 'OPERATOR' | 'SYSTEM'
+ lifecycle   → 'DRAFT'|'APPROVED'|'ACTIVE_LOCAL'|'ACTIVE_TEAM'|'BLOCKED'|'RETIRED'
+ canonicalWrite: boolean, default false
+ externalSend:   boolean, default false
+ requiresGuard:  boolean, default true
+ activationApprovalBand: string, default 'JOAO_REQUIRED'
+ readScopes:  string[], default []
+ writeScopes: string[], default []
+ audienceMode:   'AREA' | 'SELECTED_AREAS' | 'TENANT_WIDE'
+ stewardAreaId:  string
```
**Invariantes obrigatórias `[J]`:**
- `lifecycle` só sai de `DRAFT` com `approvals` aprovada de `subjectType: 'AGENT'`.
- `canonicalWrite: true` e `externalSend: true` exigem `ApprovalBand.JOAO_REQUIRED`, **sem exceção**.
- Todo agente nasce `DRAFT`. **Não há criação já ativa.**

> ⚠ **`kind` é renomeação, não adição.** Manter dois campos chamados `kind` com semânticas
> diferentes é como se perde um modelo. O atual classifica autoria — chame-o de `authorship`.

### 2.4 `conversations` / `conversation_turns` — a operação passa a poder falar com agente `[P]`
```
conversations:      + agentId: string | null    (null = RAG puro sobre o acervo)
conversation_turns: + agentRunId: string | null (aponta a execução que respondeu)
```
**O que compra:** cada turno passa a ter procedência completa — qual versão de instrução respondeu,
com quais contextos (o `sources[]` já existe, com `contextId` + `score`) e a que custo.

### 2.5 `loop_runs` / `agent_runs` — separar execução de entrega `[J]`
```
+ deliveryStatus: 'NOT_APPLICABLE' | 'PENDING' | 'DELIVERED' | 'FAILED', default NOT_APPLICABLE
+ deliveryError:  string | null
+ deliveryAt:     Date | null
```
**Invariante:** `status: succeeded` **com** `deliveryStatus: FAILED` **não conta como sucesso** em
nenhum painel ou métrica. É o caso real do `pendencias-joao-lembrete`.

---

## 3 · Collections novas

> Todas seguem os padrões que o banco já provou: `brainId` + `tenantId` obrigatórios, `deletedAt`
> nulo por padrão, `strict: 'throw'`, ator em **duas partes** (`...SubjectId` + `...PersonId`), e
> append-only por guarda de schema onde declarado.

### 3.1 `addressings` — o ato de endereçar `[P]`
```
brainId          string, required, immutable
tenantId         string | null, immutable
areaId           string | null
subjectType      string, required, immutable   -- 'CONTEXT' | 'DEMAND' | 'RFI' | 'AGENT_OUTPUT'
subjectRef       string, required, immutable
title            string, required, maxlength 200
body             string, maxlength 100000
fromSubjectId    string, required, immutable   -- quem endereçou
fromPersonId     string, required, immutable
toSubjectId      string, required              -- quem recebe (trustedSubjectId)
toPersonId       string, required
toAreaId         string | null                 -- endereçamento a ÁREA, não a pessoa
dueAt            Date | null
priority         string, enum LOW|NORMAL|HIGH|CRITICAL, default NORMAL
state            string, enum OPEN|ANSWERED|CLOSED|CANCELLED, default OPEN
sensitivityTier  string, required
sourceLoopRunId  string | null                 -- se nasceu de automação
deletedAt        Date | null

-- v1.1: campos acrescentados por conformidade com o idioma de `seeds` (§6-bis.1)
currentOwner     string, required              -- quem DETÉM o item agora
nextAction       string, required, enum        -- o que falta acontecer
stateTrail       [{ state, at, reason }]       -- trilha inline, como em seeds
integrityHash    string, match /^[0-9a-f]{64}$/  -- dedupe por conteúdo
consentRef       string | null                 -- LGPD
retentionPolicy  string | null                 -- LGPD
```
**Índice único adicional:** `{brainId, integrityHash}` — mesmo padrão de `seeds`.
**Collection irmã obrigatória:** `addressing_audit_events`, seguindo o padrão por módulo (§6-bis.2).
**Índices:** `{brainId, tenantId, toSubjectId, state, dueAt}` (a inbox) ·
`{brainId, subjectType, subjectRef}` · `{brainId, state, dueAt}` (os vencidos).

⚠ **`addressings` NÃO é só uma collection — é um MÓDULO.** O barramento de eventos **não tem endpoint
público de ingestão**: só publicam módulos cujo efeito já é durável. Logo exige
**`addressing_outbox` próprio**, espelhando `context_publication_outbox`:
`_id` determinístico, insert **na mesma transação** da escrita, drenador com lease.

### 3.2 `addressing_responses` — **append-only** `[P]`
```
addressingId        string, required, immutable
brainId, tenantId   required / nullable, immutable
sequence            number, required, min 1, immutable
decision            string, required, enum:
                    ACCEPTED | REFUSED | RETURNED_WITH_QUESTION | REASSIGNED | COMPLETED
respondedBySubjectId string, required, immutable
respondedByPersonId  string, required, immutable
justification        string | null, maxlength 20000
evidenceContextIds   string[], default []
generatedDemandIds   string[], default []
reassignedToSubjectId string | null
auditEventId         string, required          -- amarra na trilha
```
**Invariantes:**
- `pre('save')`: se `!this.isNew` → **erro**. Append-only, como `audit_events`.
- `REFUSED` e `RETURNED_WITH_QUESTION` **exigem `justification`** não-vazia.
- `COMPLETED` **exige `evidenceContextIds` não-vazio.** *Conclusão sem evidência não é conclusão.*
- `REASSIGNED` exige `reassignedToSubjectId` ≠ `respondedBySubjectId`.
- **Índice único** `{addressingId, sequence}`.

> **Por que collection separada e não campo em `approvals`:** `approvals` tem índice **único** em
> `{brainId, subjectType, subjectRef}` — **um veredito por assunto, uma só vez** — e o status é
> `PENDING|APPROVED|REJECTED|ARCHIVED`, **sem "devolvido com pergunta" nem "reatribuído"**.
> `approvals` modela veredito; isto modela **conversa de trabalho**. São coisas diferentes.
> ✅ **Reuso que serve:** `approvals.subjectType` é `String` **livre** — então
> `subjectType: 'ADDRESSING'` cabe **hoje, sem alterar schema**, para a decisão formal.

### 3.3 `demands` — o trabalho que nasceu `[P]`
```
brainId, tenantId, areaId
code             string, required   -- 'D-2026-002', a chave humana que já usamos
title            string, required
state            string, enum BACKLOG|PLANNED|IN_PROGRESS|BLOCKED|DONE|CANCELLED
ownerSubjectId   string | null
ownerPersonId    string | null
originAddressingId string | null
originResponseId   string | null    -- QUAL resposta gerou esta demanda
contextId        string | null      -- o MD da demanda no acervo
sensitivityTier  string, required
externalRefs     [{ system, externalId, url, syncedAt, syncState }]
dueAt, closedAt  Date | null
deletedAt        Date | null
```
**Índice único** `{brainId, code}` parcial em `deletedAt: null`.

**`externalRefs` é a resposta ao "as demandas poderão integrar com as plataformas internas".** É a
ponte para uFlow, CX Hub, IntHub: cada sistema externo com o próprio id, url e estado de
sincronização — **sem que o BrainHub finja ser a fonte de verdade daquele card.**

### 3.4 `inbox_items` — o registro de ENTREGA `[P]` + `[J]`
```
brainId, tenantId
recipientSubjectId string, required   -- trustedSubjectId
recipientPersonId  string, required
addressingId     string | null
demandId         string | null
approvalId       string | null
kind             string, enum ADDRESSING|DEMAND|APPROVAL|AGENT_OUTPUT|SYSTEM
channel          string, enum IN_APP|EMAIL|WHATSAPP|DISCORD
deliveryStatus   string, enum PENDING|DELIVERED|FAILED|SUPPRESSED
deliveryError    string | null
deliveredAt, readAt, dismissedAt  Date | null
dedupeKey        string, required
sourceLoopRunId  string | null
```
**Índices:** `{brainId, recipientSubjectId, readAt, createdAt: -1}` (a caixa) ·
**único** `{brainId, dedupeKey}` — **exactly-once por índice de banco**, como `loop_runs`.

> `NOTIFICATION` **já é tipo de nó** do Loop. O que falta não é o conceito de notificar — é o
> **registro de entrega**. E o `pendencias-joao-lembrete` do João é a prova de que sem ele o sistema
> mente: rodou ok, não entregou, ninguém soube.

### 3.5 `agent_shares` — quem pode consumir cada agente `[J]` + `[P]`
Espelha `category_shares`, que já foi pensado e revisado:
```
brainId, tenantId, agentId    required, immutable
targetAreaId    string, required, immutable
effect          string, enum ALLOW|DENY, immutable
grantedBy       string, required, immutable
approvalId      string | null, immutable
operationKey    string, required, immutable   -- 'agents.run' | 'agents.read'
revokedAt, revokedBy
```
**Mais três peças, para fechar o eixo:**
1. Grant nomeado **`agents.consume`** em `membership.grants[]` e `area_memberships.grants[]`.
2. Operação **`agents.run`** registrada no `AccessScopeService` — hoje ele enumera 18 operações e
   **nenhuma é `agents.*`**.
3. **`agent_context_policy`** — tradução do `context_policy` do João `[J]`:
   `perUserContext` · `adminCanViewAllContexts` · `sharedContextAfterApproval` ·
   `rawUserContextLeaksToOtherUsers` **(sempre `false`, invariante de schema, não default)**.

> Para o **agente de suporte do uFlow**: `audienceMode: TENANT_WIDE`. Quase todos consultam, e a
> exceção passa a ser explícita e auditável em vez de implícita.

---

## 4 · A matriz de rastreio — quem, quando, como, por quê

> O Vinicius pediu visibilidade de **quando, quem, como** para todo fluxo. Isto é a resposta, com o
> campo exato que responde cada pergunta.

| Pergunta | Campo que responde | Collection | Grau |
|---|---|---|---|
| **Quem** alterou | `actorSubjectId` + `actorPersonId` + `actorMembershipId` | `audit_events` | ✅ `[C]` |
| **Quando** | `createdAt` + `phase: PRE_MUTATION` | `audit_events` | ✅ `[C]` |
| **O que** mudou | `changedFields[]` | `audit_events` | ✅ `[C]` |
| **Qual era antes** | `contentHash` sha256, append-only | `context_versions` | ✅ `[C]` |
| **Quem autorizou** | `decidedBy` + `decisionAuthority` + `band` | `approvals` | ✅ `[C]` |
| **Por que disparou** | `sourceType` + `sourceId` + `dedupeKey` | `loop_runs` | ✅ `[C]` |
| **Com que autoridade o robô agiu** | `createdBySubjectId` = **dono da trigger** | `loop_runs` | ✅ `[C]` ⚠ |
| **Quanto custou** | `costUsd` + `steps[].costUsd` por nó | `loop_runs` | ✅ `[C]` |
| **Qual instrução respondeu** | `agentVersionId` → `contentHash` | `agent_runs` | ✅ `[C]` |
| **Quais MDs sustentaram** | `sources[].contextId` + `score` | `conversation_turns` | ✅ `[C]` |
| **Quem foi endereçado** | `toSubjectId` + `toAreaId` + `dueAt` | `addressings` | 🆕 `[P]` |
| **O que a pessoa respondeu** | `decision` + `justification` + `sequence` | `addressing_responses` | 🆕 `[P]` |
| **Com que evidência concluiu** | `evidenceContextIds[]` | `addressing_responses` | 🆕 `[P]` |
| **Chegou a quem?** | `deliveryStatus` + `deliveredAt` + `readAt` | `inbox_items` | 🆕 `[P]` `[J]` |
| **Que trabalho gerou** | `originResponseId` | `demands` | 🆕 `[P]` |
| **Refletiu no sistema externo** | `externalRefs[].syncState` | `demands` | 🆕 `[P]` |

⚠ **A linha do "dono da trigger" é a mais importante da tabela para governança.** A automação roda com
o crachá de quem **possui a trigger**, não de quem causou o evento. **Trigger é procuração, não
configuração** — e isso precisa aparecer em tela, não só em schema.

---

## 5 · Invariantes que não são negociáveis

Todas já existem em alguma collection do banco. A espec é: **valem para as collections novas também.**

1. **Append-only por guarda de schema**, não por convenção. `audit_events` e `context_versions` já
   lançam erro em reescrita. `addressing_responses` idem.
2. **Exactly-once por índice único**, não por tentativa. `loop_runs {brainId, dedupeKey}` é o
   padrão. `inbox_items` idem.
3. **Outbox na mesma transação da escrita**, com `_id` determinístico. Sem isso existe o instante em
   que o fato aconteceu e ninguém foi avisado.
4. **Concorrência otimista pelo ponteiro de versão.** `currentVersionId` no filtro do update: quem
   perdeu a corrida recebe "recarregue", não sobrescreve.
5. **Fail-closed na auditoria.** Sem gravador de auditoria disponível, **nega o acesso** — já é assim
   no `AccessScopeService`.
6. **Ninguém concede exceção a si mesmo.** `subjectId === grantedBySubjectId` é rejeitado.
7. **Ator em duas partes** em toda collection nova: `...SubjectId` (o `trustedSubjectId` do Cognito) **e**
   `...PersonId`. ⚠ `areas.adminSubjectId` guarda `trustedSubjectId`, **não ObjectId** — seguir a
   mesma convenção ou o JOIN não fecha.
8. **Escrita canônica direta por agente é proibida** `[J]`. Agente escreve em área de proposta; a
   promoção ao canônico passa por `approvals`.

---

## 6 · Inventário de agentes — o que existe, o que falta, o que é sobressalente

### 6.1 O que o João já tem rodando — 10 no registry Hermes `[J]`
Lido em `agent-control/runs/cron_registry_sync_20260716T150445/agents.json`, gerado **16 jul 2026**.

| id | nome | kind | visib. | agenda | estado |
|---|---|---|---|---|---|
| `a0aff9aff0a5` | daily inbox governance | agent | operator | 08:00 diário | ✅ healthy |
| `cb905f0e2a91` | weekly orphan radar | worker | operator | seg 08:00 | ✅ healthy |
| `aa0266d80322` | weekly MD size audit | worker | operator | seg 08:30 | ✅ healthy |
| `f35c289212ad` | queue-executor poll | poller | operator | 1 min | ✅ healthy · **2.566 execuções** |
| `55087ff1e84f` | call-classifier (Tactiq) | agent | operator | 07:00 diário | ✅ healthy |
| `fca3b54ede8a` | call distiller+classifier | agent | operator | 07:15 diário | ✅ healthy |
| `3091ff530969` | seed approval cards | worker | operator | 09:00 diário | ✅ healthy |
| `f11bfd6f06ab` | codex-inbox reconciler | reconciler | operator | seg 09:00 | ⚠ **never_run** |
| `776f13673318` | downloads-sentinel | sentinel | **system** | 07:30 diário | 🔴 **error** |
| `3898296727c8` | pendencias-joao-lembrete | sentinel | **system** | seg 09:00 | ⚠ **entrega falha** |

**4 workflows:** `calls-pipeline` (3 passos) · `governance-pipeline` (3) ·
`queue-executor-pipeline` (1) · `codex-reconciliation-pipeline` (1).

**Mais 3 na frota launchd** (`04_Dados-e-IA/frota/frota.json`, atualizado 10/06):
`driftsweep` (governança, report-only, sem IA) · `gitpullall` (ops, sem IA) ·
`brainhub-mine` (**usa IA**, a cada 30 min, destila transcrições em notas atômicas **como propostas
para aprovação**).

**Mais 4 treinados** (`frota/treinos/`, com front-matter e `id`): `classificador-cunho` ·
`filtro-sinal` · `juiz-contradicao` · `roteador-tier`.
> **Esses quatro são agentes estruturais e correspondem a tipos de nó que o banco já tem:**
> `juiz-contradicao` ↔ `JURY_CONSENSUS` · `filtro-sinal` ↔ `GATE` · `roteador-tier` ↔ classificação de
> tier · `classificador-cunho` ↔ classificação. **Migrar como `agent_versions`, não reinventar.**

### 6.2 🔴 O achado estrutural do inventário
**Todos os 10 são `deliver: "local"`, com `script_path` em `~/.hermes/` e agenda em launchd na
máquina do João.** Somando: **17 automações que não sobrevivem ao notebook dele desligar.**

> **Isso, e não a falta de ideias, é o argumento central desta espec.** O desenho existe, está
> provado em produção e roda há meses. O que falta é **deixar de ser pessoal e passar a ser
> plataforma** — o que significa exatamente as collections da §3 e os campos da §2.

### 6.3 O que é nosso hoje — 1 agente
`uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow.md` (18,7 KB), demanda **D-2026-002**.
⚠ **A instrução está incompleta:** o `TREINAMENTO-AGENTE-SUPORTE-UFLOW.md` tinha 1.084 linhas e
**818 foram preservadas** antes do arquivo sair do disco. **Faltam o fim do Anexo C, o Anexo D e o
Anexo E** — precisa reenvio.

### 6.4 O que ainda precisa ser criado e treinado `[P]`
| Agente | Classe | Por que | Prioridade |
|---|---|---|---|
| **Suporte uFlow** | interação · `TENANT_WIDE` | primeira entrega do BrainHub (D-2026-002) | 🔴 zero |
| **Importador MD → banco** | estrutural · `WORKER` | sem ele o acervo não se popula; consome o `_indice/` | 🔴 zero |
| **Roteador de endereçamento** | estrutural · `RECONCILER` | lê protocolo, cria endereçamento, escolhe destinatário | 🟠 |
| **Auditor de conformidade de MD** | estrutural · `SENTINEL` | valida títulos por tipo — hoje é script nosso; o João já tem o `md-size-auditor` | 🟠 |
| **Sentinela de entrega** | estrutural · `SENTINEL` | varre `inbox_items` com `deliveryStatus: FAILED` | 🟠 |
| **Agente de cliente (Hub de Agentes)** | interação · por tenant | é o produto: o BrainHub do cliente | 🟡 depois |

### 6.5 O que é sobressalente `[P]`
| Item | Por quê |
|---|---|
| `downloads-sentinel` | 🔴 quebrado (`InterruptedError` em `~/Downloads`) **e** é faxina de máquina local, **não domínio do BrainHub**. Não migrar. |
| `gitpullall` | Ops puro, `usa_ia: false`. Útil ao João, **irrelevante para a plataforma**. Não migrar. |
| `pendencias-joao-lembrete` | Lembrete pessoal com entrega quebrada. **O caso de uso vira `inbox_items` + `ApprovalBand`** — não vira agente. |
| `codex-inbox reconciler` | **Nunca rodou** desde 16/07. Não migrar sem antes provar que funciona. |
| `registry.v0.1.superado.json` | Marcado `_superado` pelo próprio João. Ignorar. |
| **Duplicidade de registry** | Existem **três** fontes de agente: `frota.json` (launchd), `~/.hermes/cron/jobs.json` (Hermes) e as fichas em `inbox/hermes/brainhub/agents/`. **Isso é o problema que a collection `agents` resolve** — uma fonte, não três. |

---

## 6-bis · REVISÃO v1.1 — o que a leitura dos schemas restantes corrigiu

> **Decisão de 17 ago 2026: não enviar esta espec com 42% de cobertura de leitura.** Quatro vezes
> nesta jornada eu errei concluindo de leitura parcial; nas quatro o custo foi meu. Enviar assim
> transfere o custo para o trabalho de outra pessoa — e **espec que contradiz código existente é pior
> que espec nenhuma.** Comecei pelos schemas com maior risco de colisão. Quatro achados imediatos:

### 6-bis.1 🔴 COLISÃO REAL — `seeds` já é o pipeline de "material bruto → aprovação → contexto"
`seeds` + `seed_batches` `[C]` existem e são exatamente a esteira que o `brainhub-mine` e o
`calls-pipeline` do João alimentam:

`sourceType` + `sourceRef` · `contentClassification` · `sensitivity` (`ApprovalTier`, default
`T2_RECORD`) · **`integrityHash` sha256 com índice ÚNICO por brain** (dedupe por conteúdo) ·
`processingStatus` · **`currentOwner`** · **`nextAction`** · **`stateTrail[{status, at, reason}]`** ·
`consentRef` · `retentionPolicy` · `contextId` · `approvalId` · `quarantineReason` · `batchId`.

**O que isso corrige na minha proposta:**
1. **`addressings` estava sem `currentOwner` e `nextAction`** — que é **o idioma que a casa já usa**
   para "quem detém isto e o que falta". Adicionar.
2. **Faltava `integrityHash`** para dedupe por conteúdo. Adicionar, com índice único por brain.
3. **Faltavam `consentRef` e `retentionPolicy`** — LGPD. **Eu não havia considerado**, e vale para
   qualquer collection que guarde dado de cliente. Adicionar em `addressings` e `demands`.
4. **`seeds` NÃO é substituto de `inbox_items`** — não tem nenhum campo de entrega. São camadas
   complementares: `seeds` é *o que aguarda decisão*; `inbox_items` é *o aviso de que aguarda você*.

### 6-bis.2 🔴 O padrão de auditoria é POR MÓDULO, e minha espec estava fora dele
Existem `approval_audit_events`, `category_policy_audit_events`,
`federation_connection_audit_events`, `invitation_audit_events` — **além** do `audit_events` geral.
> **Logo: `addressings` exige `addressing_audit_events` próprio.** Minha espec dizia só
> "`auditEventId` amarra na trilha" — subespecificado e **não conforme ao padrão da casa**. Corrigir.

### 6-bis.3 ⚠ A casa tem DOIS padrões de histórico, e eu ignorei um
- **Collection separada append-only:** `context_versions`, `audit_events`, `context_pack_versions`.
- **Trilha inline no documento:** `seeds.stateTrail[]`.

Mantenho `addressing_responses` como **collection separada** — porque carrega justificativa,
`evidenceContextIds[]` e `generatedDemandIds[]`, que é muito mais que uma trilha de status. **Mas a
escolha agora está justificada contra o idioma existente, não por omissão.**

### 6-bis.4 ✅ ACHADO QUE MUDA O PLANO DO AGENTE — `context_packs`
`context_packs` + `context_pack_versions` `[C]` são o que `agent_versions.contextPackRefs[]`
referencia. E a versão do pack é **imutável e endereçada por conteúdo**:
`contextIds[]` explícito · `limit` (1–50) · **`minScore`** (0–1) · **`sourcesHash` `sha256:`** ·
append-only imposto em **6 verbos de mutação + `bulkWrite`**.

> **Instrução e acervo são versionados juntos, com hash nos dois lados.** Uma versão de agente aponta
> uma versão de pack, que aponta uma lista fixa de contextos com os parâmetros de recuperação
> congelados. **É exatamente o rastreio de "qual instrução respondeu, com qual acervo, a que score".**

**E isto resolve a ordem de implementação com evidência, não com preferência:**
> Sem `context_pack`, o agente de suporte responde **só pela instrução** — sem `sources[]`, sem
> citação de contexto, sem rastreio de qual MD sustentou a resposta. **Perde-se exatamente a garantia
> de zero alucinação.** E o pack precisa de `contexts` populado, que precisa do importador, que
> precisa de `contexts.type`.
>
> **Portanto a onda 1 não é alternativa à entrega do agente — é pré-requisito da QUALIDADE dele.**
> Antecipar as ondas 4 e 5 entregaria um agente sem procedência de resposta. **Não invertemos.**

### 6-bis.5 `folders` + `files` — e a decisão de destino dos nossos MDs `[C]` + `[P]`
Existe um **sistema de arquivos completo**: `folders` com `parentFolderId` (hierarquia livre),
`files` com `folderId`, `nameKey` **único** por `{brainId, tenantId, areaId, folderId}` (é
exatamente o comportamento de pasta), `currentVersionId` + `versionSequence`, e — nos dois —
soft-delete com **ponteiro para o próprio evento de auditoria**
(`deletedAuditEventId`, `restoredAuditEventId`).

> **Decisão `[P]`: os nossos MDs vão para `contexts`, NÃO para `files`.** Motivo: `contexts` já tem
> `content`, chunking, embedding, relações e context pack — é a camada de **conhecimento que se
> recupera**. `files` é a camada de **artefato que se armazena**. Duplicar o MD nas duas é criar duas
> verdades para o mesmo texto.
>
> **`files` serve para o que não é conhecimento em si:** o PDF de uma ficha técnica, a planilha, a
> imagem. **E isso corrige uma lacuna da minha espec:** `addressings` não tinha como anexar nada.
> Acrescentar `attachmentFileIds: string[]`.

⚠ **Terceira correção de conformidade:** o padrão de soft-delete da casa é
`deletedAt` + `deletedBySubjectId` + `deletedByPersonId` + `deletedReason` +
**`deletedAuditEventId`** (e o espelho de `restored*`). Minha espec tinha só `deletedAt`. Aplicar o
padrão completo em `addressings`, `demands` e `inbox_items`.

### 6-bis.6 ✅ FIO SOLTO FECHADO — `federation_connections` é a membrana Casa↔cliente `[C]`
Eu havia declarado isto como fio solto a ler. Está lido, e é o mecanismo:

`sourceBrainId`/`sourceTenantId` → `targetBrainId`/`targetTenantId` — **conexão brain a brain**, com
`requestedLevel` e `grantedLevel` em **quatro níveis crescentes**:

| Nível | O que permite |
|---|---|
| `discover` | o brain de destino sabe que aquilo existe |
| `read` | pode ler o contexto |
| `query` | pode recuperar via busca / RAG |
| `contribute` | pode **escrever de volta** |

Ciclo: `REQUESTED` → `GRANTED`\|`REJECTED` → `REVOKED`, com `requestedBy` (pessoa + subject),
`decidedByPersonId`, `decisionReason`, `decidedAt`, `revokedAt`. **Índice único por par de brain**,
parcial em `REQUESTED|GRANTED` — **uma conexão viva por par**.

> **Tradução para o nosso modelo:** o `conecta_area_cliente` de cada Produto é a expressão de negócio
> daquilo que, no dado, é uma **federation connection concedida** entre o brain da Casa e o brain do
> cliente. O nível certo para leitura de contexto de produto é **`query`**; `contribute` só se o
> cliente puder alimentar o contexto do produto na Casa.
>
> ⚠ **Consequência volumétrica a dimensionar:** 16 Produtos × N clientes conectados = N conexões a
> conceder e governar, cada uma com decisão registrada. **Isso entra no
> `protocolo-criacao-cliente.md`** junto com as 14 áreas e as 9 categorias.

### 6-bis.7 ✅ `invitations` — NÃO colide `[C]`
É onboarding de pessoa em tenant (`email`, `roleId`, `grants[]`, `expiresAt`, único por
`{tenantId, email}` enquanto `PENDING`). **Não é atribuição de trabalho** — não conflita com
`addressings`. E confirma que **`grants: string[]` é o idioma de capacidade** que atravessa
invitation → membership → area_membership. **O nosso `agents.consume` entra nesse mesmo vocabulário.**

### 6-bis.8 Cobertura de leitura atualizada e a fila restante
**29 dos 50 schemas** lidos campo a campo (era 21). Acrescentados nesta rodada: `organizations` ·
`tenants` · `seeds` · `seed_batches` · `context_packs` (+`context_pack_versions`) · `files` ·
`folders` · `federation_connections` · `invitations`.

**Fila restante (21), por risco:**
🟠 `file-version` · `loop` · `loop-version` · `context-chunk` · `llm-connection` ·
`encrypted-credential` · `federation-discovery` (node + profile).
🟡 `run-daily-counter` · `ask-daily-counter` (quotas) · as **8 variantes de audit-event**
(o padrão já está entendido; falta o campo) · `tenant-bootstrap-audit` · `category-policy-audit-event`.

> **Nenhum item da fila restante bloqueia a v2.** Os que podiam mudar o desenho — `seeds`,
> `context_packs`, `files`/`folders`, `federation` — foram lidos. O resto é detalhe de campo, e está
> declarado.

---

## 7 · Ordem de implementação sugerida

| Onda | O que | Desbloqueia |
|---|---|---|
| **1** | `contexts.type` + os 2 campos no payload do evento (§2.1, §2.2) | roteamento por tipo — tudo depende disso |
| **2** | `inbox_items` + `deliveryStatus` em `loop_runs`/`agent_runs` (§3.4, §2.5) | parar de mentir sobre entrega |
| **3** | `addressings` + `addressing_outbox` + `addressing_responses` (§3.1, §3.2) | o ciclo de trabalho fecha |
| **4** | `agents` com os campos do João + `agent_shares` + `agents.run` (§2.3, §3.5) | publicar agente para a operação |
| **5** | `conversations.agentId` + `conversation_turns.agentRunId` (§2.4) | a operação conversar com o agente |
| **6** | `demands` + `externalRefs` (§3.3) | integração com uFlow / CX Hub / IntHub |
| **7** | Ligar `CATEGORY_AUDIENCE_FILTER` + allowlist do brain | permissão fina sair do papel |

**A onda 1 é o gargalo real.** Sem `type` no evento, nenhuma automação distingue tipos de documento, e
todo o resto vira contorno.

---

## Fontes

**Código lido** (`umode-brainhub-api`, branch `codex/bhp-p16-federation-grants-back`, somente
leitura): 21 dos 50 schemas + `runtime-event-bus` · `context-publication-outbox-drainer` ·
`access-scope.service` · `category-audience-policy.service` · `category-audience.filter` ·
`contexts.repository` · `organizations.schema`.

**Desenho do João** (`umode-os-vault`, branch `main`, somente leitura):
`_sistema/brainhub/governance/template-ficha-agente.md` (D32, 09/07) ·
`inbox/hermes/brainhub/governance/agent-control/runs/cron_registry_sync_20260716T150445/{agents,workflows}.json` ·
`BrainHub/uMode/04_Dados-e-IA/frota/frota.json` · `frota/treinos/*.md`.

**Nossos:** `_fluxo-dados-brainhub.md` (o fluxo) · `_dicionario-dados-brainhub.md` (campo a campo) ·
`_como-o-brainhub-funciona.md` (a aula) · `_pendencias-gerais.md` 183–200.

## Governança
Somente o CEO altera conteúdo no BrainHub. **Alteração nesta espec exige citar a fonte** — arquivo de
código, documento do João, ou decisão registrada. Proposta sem fonte não entra.
