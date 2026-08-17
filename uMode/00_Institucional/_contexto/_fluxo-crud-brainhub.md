# Plano de funcionamento do BrainHub no banco — hierarquias, endereçamentos e demandas

> Escrito em **17 ago 2026**, terceira e definitiva versão. **As duas anteriores estavam erradas** e o
> motivo está registrado na §1 — não por pudor, mas porque a causa se repete e precisa ficar anotada.
>
> **Não é implementação.** É o plano de o que se registra quando algo é criado, alterado ou removido;
> quem decidiu; se gerou demanda; e como isso fica rastreável.
>
> ---
> 🔺 **SUPERSEDED no que diz respeito ao FLUXO DE DADOS — 17 ago 2026, mesmo dia, algumas horas
> depois.** A autoridade sobre **o que se move, quando e disparado por quem** passou a ser
> **`_fluxo-dados-brainhub.md`**, escrito depois de eu ler o mecanismo real de disparo
> (`context_publication_outbox` → `RuntimeEventBus` → `loop_runs`), que **este documento não
> conhecia**. Três coisas que aqui estão desenhadas de forma que o código não sustenta:
> 1. **`addressings` não é coleção, é módulo com outbox transacional próprio** — o `RuntimeEventBus`
>    não tem endpoint público de ingestão.
> 2. **`approvals` não modela a resposta a um endereçamento** — o índice único
>    `{brainId, subjectType, subjectRef}` permite **um veredito por assunto, uma só vez**.
> 3. **O roteamento só tem dois eixos** (`categoryId`, `areaId`) — o payload do evento não carrega
>    tipo nem tier.
>
> O que **continua válido** aqui: as duas classes de agente, a lição da §1, e as regras de rastreio
> na medida em que o `_fluxo-dados-brainhub.md` §8 as confirma. **Em caso de conflito entre os dois
> documentos, vale o `_fluxo-dados-brainhub.md`.**
> ---

## 1 · Duas correções minhas, e a lição
**O clone da API veio com `--single-branch`.** O refspec era
`+refs/heads/main:refs/remotes/origin/main`: **1 branch local contra 114 no remoto.** Eu li o `main`
(08/08, 5 módulos) e concluí duas coisas falsas:
1. que faltavam `brains`, `agents`, `approvals`, `trash`, `audit` — **existem todos**;
2. que havia divergência entre o ledger do João e o código, sugerindo confirmar com o Bergson —
   **não havia divergência nenhuma.** Retratado.

**Lição, e é a segunda vez na mesma jornada:** antes de afirmar que algo não existe num repositório,
conferir o **refspec do clone** e as branches remotas. A primeira vez foi declarar indisponível a
fonte de julho das demandas, que estava no histórico do Git. **Ausência de fonte é hipótese, não
conclusão.**

---

# PARTE I — O que existe de fato

## 2 · A plataforma está muito mais construída do que eu supunha
Na branch mais completa (`codex/bhp-p16-federation-grants-back`, **17/08/2026**): **29 módulos, 632
arquivos em `src/`, 49 schemas.** Há commits de hoje. O ritmo é alto.

Os 29 domínios: `agent-execution` · `agents` · `approvals` · `areas` · `ask` · `brains` ·
`categories` · `context-mapping-preflight` · `context-packs` · `context-relations` · `contexts` ·
`conversations` · `embeddings` · `federation-connections` · `federation-discovery` · `files` ·
`folders` · `invitations` · `llm-connections` · `loop-execution` · `loops` · `memberships` ·
`organizations` · `people` · `runtime-definitions` · `seeds` · `session` · `tenants` · `trash`

## 3 · Os primitivos de rastreio já existem — e são melhores do que eu ia propor
| O que eu ia propor | O que já existe |
|---|---|
| `revisions` genérica | **versionamento por domínio:** `context-version` · `agent-version` · `loop-version` · `file-version` |
| `audit_events` centralizada | **auditoria por domínio: 14 schemas de evento** — `contexts/audit` (com `audit-action.enum` **e** `audit-reason-code.enum`), e audit próprio em agents, areas, approvals, categories, context-packs, context-relations, conversations, federation-connections, federation-discovery, files, folders, invitations, loops, runtime-definitions, agent-execution, tenants/bootstrap |
| `approvals` | `approvals/approval.schema.ts` + `approval-audit-event.schema.ts` |
| `context_relations` | `context-relations/context-relation.schema.ts` + audit próprio |
| `tombstones` / lixeira | módulo **`trash`** + `feat/bhp-s6-002-gate-legacy-delete` |
| `grants` / permissão | `memberships` · `areas/area-membership` · `categories/category-share` · `federation-connections` · **`session`** |
| triggers e rotinas | **`runtime-definitions/trigger.schema.ts`** · **`routine.schema.ts`** · **`runtime-event-bus.ts`** |
| `users` | `people/person.schema.ts` + `memberships/membership.schema.ts` |
| tenant | `tenants/tenant.schema.ts` + `brains/brain.schema.ts` |
| limite de custo | `agent-execution/run-daily-counter` · `ask/ask-daily-counter` |
| segredo de LLM | `llm-connections/vault/encrypted-credential.schema.ts` |

> **A auditoria ser por domínio, e não centralizada, é decisão de desenho com consequência:** cada
> domínio tem seu enum de ação e o `contexts` tem até `audit-reason-code`. Isso dá precisão semântica,
> mas **não existe uma view única de "tudo que aconteceu"**. Quem for montar a trilha completa de um
> endereçamento vai ter de compor 14 fontes. Registrar como ponto a resolver, não como defeito.

## 4 · O que NÃO existe — e é exatamente o seu objetivo da semana
Varredura das **114 branches**, por módulo e por nome de arquivo:

| Domínio | Existe? |
|---|---|
| **`demand` / `task`** | ❌ em nenhuma branch |
| **`addressing`** | ❌ em nenhuma branch |
| **`inbox`** | ❌ em nenhuma branch |
| **`notification`** | ❌ em nenhuma branch |

**São quatro coleções, e é toda a lacuna.** Tudo o mais que o fluxo precisa — decisão, aprovação,
versão, auditoria, trigger, rotina, permissão, lixeira — já está construído.

> **A leitura de gestão:** a plataforma resolveu **contexto, governança e execução**. Não resolveu
> **trabalho** — quem faz o quê, até quando, e como fica sabendo. É a camada operacional, e é
> precisamente o que você precisa definir hoje.

---

# PARTE II — O modelo conceitual vigente

## 5 · São três hierarquias, não uma (plano §5)
```
A · PESSOA                        B · EMPRESA / TENANT              C · VÍNCULO
   └── Personal Brain                └── Second Brain                  Pessoa ─membership─► Empresa
        ├── Pessoal                       ├── Áreas                    (N empresas, ou nenhuma)
        ├── Profissional                  ├── Pilares
        ├── Saúde                         ├── Contextos
        ├── Financeiro                    ├── Context Packs
        ├── Relacionamentos               ├── Agentes · Loops
        └── Sonhos e Propósito            ├── Rotinas · Triggers
                                          ├── Políticas · Aprovações
                                          └── Membros
```
**Fronteira inviolável (§5.1):** o Personal Brain tem identidade, armazenamento, política,
classificação, consentimento, auditoria e revogação **próprios**, e **nenhuma exposição automática à
empresa vinculada**. *"Nenhuma regra empresarial poderá abrir automaticamente o Personal Brain
completo de uma pessoa."* — isso tem de ser separação de escopo no dado, não policy de aplicação.

**Compartilhar tem 7 formas distintas (§5.2)**, e o banco precisa distingui-las: referência viva ·
cópia de conteúdo · trecho compartilhado · resultado derivado · publicação como contexto empresarial ·
compartilhamento temporário · compartilhamento revogável. Já há `category-share` para parte disso.

## 6 · Onde a nossa estrutura encaixa
| Nosso conceito | Na plataforma | Situação |
|---|---|---|
| Instituição (Casa/Cliente) | `tenants` + `brains` | ✅ existe |
| Institucional | contexto raiz | ✅ |
| **Área** (8/14) | **`areas`** | ✅ mesmo nome, e há `area-membership` |
| Subárea | `folders` ou Pilar | ✅ pasta é **projeção de navegação**, não estrutura física |
| Pessoa | `people` + `memberships` | ✅ nossa Pessoa vira duas coisas |
| Solução do Portfólio | contexto sob Área | ✅ |
| Integração | contexto + `context-relations` | ✅ |
| **Demanda / RFI** | — | ❌ **não existe** |
| — | **Personal Brain** | ❌ **não temos** |
| — | Loops · Rotinas · Triggers · Federação | ❌ não temos |

**As duas lacunas nossas são simétricas:** a plataforma não tem Demanda; nós não temos Personal Brain.

---

# PARTE III — O plano

## 7 · O princípio que governa o CRUD
**Plano §6.2:** *"Nenhuma ação de negócio ou governança poderá existir somente como script escondido,
comando manual ou alteração direta no banco."*
**D78, regra 2:** *"Endpoint que apenas registra intenção nunca pode declarar execução real. Deve
marcar `recorded_only` e `executed: false` até existir prova do executor."*

Logo: **entidade tem CRUD; ação de domínio tem comando explícito** — `POST /approvals/:id/decide`,
`POST /access-grants/:id/revoke` — em vez de disfarçar decisão como `PATCH`. A plataforma já segue
isso em `approvals`.

## 8 · As três coleções que faltam — desenhadas contra o contrato real
> ⚠ **Corrigido em 17 ago 2026 após ler `loops`, `loop_versions`, `loop_runs` e o catálogo de nós.**
> São **três** coleções, não quatro: `notification` já existe como **tipo de nó** do Loop, e o que
> falta ali é só o registro de entrega. E o encaixe é outro: **"criar demanda" é um nó `ACTION` dentro
> de um Loop**, não campo de trigger. Contratos em
> [`_dicionario-dados-brainhub.md`](_dicionario-dados-brainhub.md) §6-bis.

**A cadeia real, do disparo à demanda:**
```
trigger (eventType + clauses)  ─┐
routine (cron + dedupeKey)     ─┼─► loop_runs (sourceType, sourceId, maxCostUsd)
manual                         ─┘        │
                                         ├─ steps[] : nó ACTION      ──► demands      [FALTA]
                                         ├─ steps[] : nó APPROVAL    ──► approvals    [existe]
                                         └─ steps[] : nó NOTIFICATION ─► entrega      [sem registro]
                                                  │
                                        addressings [FALTA] ──► inbox_items [FALTA]
```
**A âncora de rastreio já existe e é dupla:** `loop_runs.sourceType`+`sourceId` diz **por que rodou**,
e `approvals.subjectType`+`subjectRef` é **polimórfico de propósito** — é onde o endereçamento se
pendura sem precisar de campo novo em `approvals`.

## 8-bis · Campos, seguindo as convenções do banco
Chave de ator é **`trustedSubjectId`** (o `sub` do Cognito), com `personId` ao lado quando há vínculo —
é a convenção de `areas.adminSubjectId` e de `loop_runs.createdBySubjectId`. Escopo é `immutable`,
índice único é parcial em `deletedAt: null`, e as coleções nascem `strict: 'throw'`.

```
addressings                                    demands
├─ brainId (immutable) · tenantId?             ├─ brainId (immutable) · tenantId? · areaId?
├─ areaId?                                     ├─ addressingId   ──► addressings._id
├─ sourceType: LOOP_RUN | APPROVAL |           ├─ title · demandType · state
│              CONTEXT | MANUAL                ├─ assigneeSubjectId? + assigneePersonId?
├─ sourceId       ──► loop_runs | approvals    ├─ dueAt? · priority
├─ sourceStepNodeId?  (qual nó ACTION gerou)   ├─ sensitivityTier   (D85: só T2 hoje)
├─ recipientKind: PERSON | AREA                ├─ closedAt? · closedReason?
├─ recipientSubjectId? | recipientAreaId?      ├─ createdBySubjectId + createdByPersonId
├─ reason  (por que chegou)                    └─ deletedAt? + deletedAuditEventId?
├─ demandId?      ──► demands._id
├─ sensitivityTier                             inbox_items
├─ createdBySubjectId + createdByPersonId      ├─ personSubjectId  ──► people.trustedSubjectId
├─ dedupeKey      (único por brain)            ├─ addressingId · demandId?
└─ revokedAt? · revokedReason?                 ├─ brainId · tenantId?
                                               ├─ readAt? · dismissedAt?
notificação: nó do Loop + registro de entrega  ├─ dedupeKey  (único por pessoa)
└─ falta a coleção de entrega: channel,        └─ createdAt
   state, dedupeKey, sentAt, error
```

**Três decisões de desenho que vêm do banco, não de mim:**
- **`dedupeKey` em `addressings` e em `inbox_items`**, único por escopo — é o padrão de `routines` e
  `loop_runs`, e é o que impede que um indicador oscilando gere 40 endereçamentos.
- **`sensitivityTier` em ambas, travado em T2 por D85** — igual a `context_relations` e
  `area_memberships`. Nasce compatível com a trava existente.
- **`deletedAt` + `deletedAuditEventId`** em `demands`, espelhando `contexts`: quem remove registra
  o id do evento de auditoria que registrou a remoção.

**Cinco regras que fazem isso ser rastreio, e não log:**
1. **Todo elo aponta para o anterior.** `inbox_item.addressingId` → `addressing.sourceId` → o registro
   de origem. De qualquer ponto se sobe até a causa.
2. **`addressing` é entidade, não campo.** É o que responde *"por que isso chegou para mim?"* e *"quem
   mais recebeu?"*. Sem ela, endereçamento é efeito colateral e não deixa rastro.
3. **Endereçamento pode existir sem demanda.** Avisar ≠ atribuir trabalho. `demandId` é opcional, e a
   ausência é informação.
4. **Uma demanda gera N itens de inbox e continua uma só.** `recipientType: area` faz **fan-out** para
   os membros via `area-membership` — sem isso, demanda de área não tem dono e ninguém pega.
5. **`notifications` é separada do `inbox_item`.** O item é o registro; a notificação é a tentativa de
   entrega, com `dedupeKey`, estado e erro. Juntar os dois faz perder ou o rastro ou a reentrega.

## 9 · A cadeia completa
```
① origem            contexto salvo · aprovação decidida · trigger disparado · rotina · agentRun · pedido humano
                          │ já existe: audit próprio de cada domínio grava o evento
② intenção          nas escritas governadas: recorded_only, executed: false        [existe]
③ decisão           approvals + approval-audit-event · autoridade = admin da conta (D92)   [existe]
④ execução          aplica no canônico + grava versão anterior (context-version)   [existe]
⑤ ENDEREÇAMENTO     addressings — a quem interessa e por quê                       [FALTA]
⑥ DEMANDA           demands, se gera trabalho                                      [FALTA]
⑦ INBOX             inbox_items, um por pessoa                                     [FALTA]
⑧ ENTREGA           notifications, com dedupe e estado                             [FALTA]
⑨ trilha            os 14 audit por domínio + os 4 novos                           [parcial]
```

## 10 · Relações entre hierarquias — contrato REAL lido no código
> ⚠ **Corrigido em 17 ago 2026 após ler o schema.** O plano §8.1 especifica 13 tipos; **o código tem
> 7**. Dicionário completo em [`_dicionario-dados-brainhub.md`](_dicionario-dados-brainhub.md) §5.

**`context_relations`, 7 tipos:** `RELATED_TO` · `SUPPORTS` · `CONTRADICTS` · `DERIVED_FROM` ·
`REFERENCES` · `DEPENDS_ON` · `SUPERSEDES`
**`provenanceKind`:** `MANUAL` · `GENERATED` · `IMPORTED` — distingue relação feita à mão, gerada por
agente e importada. **É o que nos permite migrar os nossos `[[wikilinks]]` como `IMPORTED` com rastro.**
Pertencimento a área **não é tipo de relação** — resolve por `sourceAreaId`/`targetAreaId`.
A relação é **immutable**: não se edita, apaga-se e recria. E **só T2 é permitido, por D85**.

Três regras que mudam como escrevemos nossos MDs:
- **Relação não revela o que a permissão nega** — o front mostra que existe contexto protegido e
  mascara conteúdo. O `permission_snapshot` existe para isso.
- **Mover contexto não pode quebrar** relação, Context Pack, embedding, agente ou loop — preserva ID,
  histórico, fontes, permissões e **localização anterior**.
- **O backend detecta link quebrado, órfão e ciclo proibido.**

## 11 · Triggers e rotinas (plano §9.3, e `runtime-definitions` já existe)
A rotina tem **14 atributos obrigatórios**: trigger · condição · janela temporal · frequência ·
**deduplicação** · owner · ação · canal · retry · **limite de custo** · fallback · auditoria · pausa ·
**teste seguro antes de ativar**.

Três merecem destaque porque é onde automação causa dano: **deduplicação** (senão o mesmo indicador
gera 40 demandas), **limite de custo** (já existe via `run-daily-counter`) e **teste seguro** (senão a
primeira execução é em produção).

Cinco gatilhos: HTTP · fila (BullMQ, existe) · cron (`routine.schema`) · **webhook do git** (commit no
nosso repositório propõe atualização de contexto) · **evento de domínio** (`runtime-event-bus`, existe).

## 12 · As duas classes de agente
Travado por Vinicius em 17 ago 2026, e tem de viver em **campo do schema**:
**Estruturais** — atualizam documentação, vistoriam padronização, acham `.md` órfão, cuidam de
indexação. **Não conversam com usuário final.** Escrevem intenção, nunca canônico.
**De interação** — atendem uma pessoa e geram addressing e demanda.
`agents.kind` = `structural | interaction` · `visibility` = `all | admin`.
E herdamos a regra §11/D62: **nenhum agente aparece `ativo` sem heartbeat e read-back** — default é
`sem evidência`.

---

# PARTE IV — Decisões e próximos passos

## 13 · Decisões que travam o desenho
Do plano §17, as que atingem hierarquia, endereçamento e demanda:
**hierarquia definitiva Tenant/Empresa/Área/Pilar** (§17.2) · **política de compartilhamento Personal
Brain ↔ empresa** (§17.3) · **quem concede exceção e por quanto tempo** (§17.4) · **política de purge
além do soft delete** (§17.10).

Nossas, que não estão no plano dele:
1. **Demanda é domínio novo ou entra em `approvals`?** Proposta: **domínio novo.** Aprovação decide;
   demanda executa. Misturar faz a fila de aprovação virar backlog de trabalho.
2. **A trilha unificada.** Com 14 audit por domínio, montar a história de um endereçamento exige
   compor 14 fontes. Proposta: **view de leitura** que agrega, sem centralizar a escrita.
3. **Canal de notificação.** Nada foi decidido em nenhuma fonte. O plano §9.3 cita WhatsApp no exemplo.
4. **Nosso Personal Brain.** Não temos os 6 domínios. É metade do produto e não está no nosso padrão.

## 14 · O que eu faço no nosso repositório sem depender de ninguém
1. **Tipar as relações** dos nossos MDs com os **7 tipos** da §10, marcando `provenanceKind: IMPORTED`
   — hoje são `[[links]]` e prosa.
2. **Renomear Subárea → Pilar** e registrar `folders` como projeção de navegação.
3. **Front-matter** com os campos que o banco exige (`tenantId`, `brainId`, `tier`, `tipo`, `origem`,
   `relations`) — é a decisão C2 do backlog de convergência, ainda sem seu aval.
4. **Abrir os 6 domínios do Personal Brain** como estrutura, ainda vazia.

## 14-bis · Onde a demanda encaixa — descoberta que muda o desenho
Trigger e rotina **disparam um Loop**, não uma ação arbitrária (`triggers.loopId`,
`routines.loopId`). Logo **"criar demanda no inbox" não é tipo de ação de trigger — é um nó dentro de
um Loop.** As quatro coleções novas não se penduram no trigger; penduram-se no **resultado da execução
do Loop** e no `approvals.subjectRef`, que é polimórfico exatamente para isso.

## 15 · O que ainda não li
Do plano consolidado: fases 0-10, segurança T0 detalhada, governança do Bergson, artefatos A-E ·
`_GOVERNANCA.md` · `DECISOES.md` · o código das branches (li a **estrutura**, não a implementação de
`s4-006`, `write-hardening`, `p12-trigger-events`, `personal-brain-contextos`) · o frontend
`UmodeApp/umode-brainhub` (não está no disco, **e não é necessário** — o comportamento em uso hoje
está no Lovable, que li em 04/08).
**O próximo passo mais útil é ler a implementação de `context-relations` e de `approvals`**, para o
desenho das 4 coleções novas encostar no contrato real e não no que eu suponho dele.

## Fontes e referências
### Documentos consultados
- `umode-brainhub-api` (`UmodeApp`) — **114 branches**, mais completa
  `codex/bhp-p16-federation-grants-back` (17/08, 29 módulos, 49 schemas, 632 arquivos em `src/`).
  Lidos por inteiro no `main`: README, 4 schemas, enums, `auth.middleware`, `whoami.service`.
- `umode-os-vault`, branch `origin/governance/brainhub-v1.5`: plano consolidado de 06/08 (§5, §5.1,
  §5.2, §6.2, §8.1, §9.3, §10.6, §13.3, §17 e ledger), `brainhub-arquitetura.md` (**superseded em
  08/08**), `brainhub-api-auth-guardrails.md` (D78), `agent-control-plane.md`, `_brainhub.md`,
  `BRAINHUB_BASTAO_VINICIUS.md` (01/07), PRD §8 e §11.
- `design-system-hub` — lido em 04 ago 2026; não avançou desde então. **É onde o comportamento de
  endereçamento e demanda existe hoje, com dado real.**
- **Leitura somente leitura. Nenhum commit, push ou checkout** fora do `brainhub-umode`.

## Governança
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**.
