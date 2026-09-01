# Blueprint — Boilerplate de produção governado + treinamento de squads/agentes/operadores

> Documento de espec e decisão. Nasce da missão do Vinicius (set/2026): ter um repositório-padrão de
> produção onde um operador de negócio (ele, o João, o Pedro) **vibecoda com autonomia, na stack real
> da uMode, sem poder ferir o protocolo** — com o HERMES na produção e o Bergson como líder técnico.
> Autoridade de conteúdo: CEO (João Risoléo), conforme governança travada em 17 ago 2026.

## §0 — Declaração de completude (o que este documento NÃO resolve)

Regra da casa ("a lacuna vem antes da conquista"): o que falta, antes do que fecha.

- **Não li a mecânica interna do gate.** O `UmodeApp/actions-shared` (workflows `pr-claude-md-gate`
  = "Marvin", e `pr-security-gate`) **não foi lido por dentro** — só a chamada que o
  `backend-boilerplate` faz a ele. Sei **o que ele faz** (travar PR por conformidade com o CLAUDE.md,
  via LLM da GitHub), **não o como**. Tudo que depende disso está marcado `[pendente actions-shared]`.
- **Não é implementação.** É espec. Nenhuma linha do boilerplate foi escrita; nenhum repo de produção
  foi alterado (escrita só no `brainhub-umode`, regra travada).
- **Não modela o fluxo de "criar operador via BrainHub"** em detalhe de dado — só aponta o trilho
  (o rito de admissão do vault). Formalizar como protocolo é passo posterior.
- **Não decide a árvore de permissão fina** (quem aprova o quê no CI) — depende de decisão do João/Bergson.
- **Cobertura, em número:** 5 repos de produção lidos 100% campo a campo (via relay CODEX, com
  commit+sha por repo, tabela abaixo) + 2 repos da era Lovable + a constituição do vault. **1 repo
  citado e não lido:** `actions-shared`.

## §1 — Fontes lidas (procedência)

| Repositório | Papel | Commit | SHA-256 do dump | Grau |
|---|---|---|---|---|
| `UmodeApp/umode-fullstack-boilerplate` | veículo de vibecoding (Next+Nest monorepo) | `bc321e0` | `fed97e7…c8df87` | [C] |
| `UmodeApp/umode-gateway-dashboard` | gateway central (auth, proxy, multi-tenant) | `2fa4040` | `9eced3b…474d8` | [C] |
| `UmodeApp/umode-backend-boilerplate-nestjs` | boilerplate back + **gold standard de governança** | `9784c7d` | `0760dd0…070893` | [C] |
| `UmodeApp/umode-frontend-boilerplate-nextjs` | boilerplate front (= `apps/web` do fullstack) | `e8365ff` | `0abf0d0…6eb019` | [C] |
| `UmodeApp/umode-microservice-integration` | boilerplate + módulo integration/partner + SQL | `9636da2` | `640fca…dfef7a` | [C] |
| `HyTrackWater/umode-planejai`, `umode-catalog-ai` | padrão de squad da era Lovable | — | — | [C] |
| `HyTrackWater/umode-os-vault` (`_GOVERNANCA.md`, `SISTEMAS.md`) | constituição HERMES | — | — | [C] |
| `UmodeApp/actions-shared` | **mecanismo dos gates (Marvin + security)** | — | — | **não lido** |

Legenda de grau por afirmação: `[C]` código lido, arquivo citado · `[F]` existe mas atrás de
flag/allowlist · `[P]` proposta minha, não validada · `[D]` decisão que não é minha.

## §2 — Mapa de governança da produção (retrato)

O achado central: **a governança de código existe, mas está espalhada e desigual — os repos mais
novos são os mais rigorosos, o mais maduro é o mais frouxo, e ninguém junta tudo.**

| Peça de governança | fullstack | frontend | backend | integration | gateway (maduro) | vault (HERMES) |
|---|---|---|---|---|---|---|
| `CLAUDE.md` (contrato do CTO/Claude Code) | ✅ | ✅ | ✅ | ✅(via rules) | ❌ | ✅ `_GOVERNANCA` |
| `AGENTS.md` / `.claude/*` (contrato do Programador) | ✅ | ✅ | — | ✅ | ❌ | ✅ |
| `.cursor/rules` (contrato do editor) | — | — | ✅ | ✅ | ❌ | — |
| Lint-as-código (no-any, i18n, no-pt) | ✅ | ✅ | ✅(no-any) | ✅(no-any) | ⚠️ **any livre** | — |
| tsconfig estrito (`noImplicitAny`,`strictNullChecks`) | ✅(web) | ✅ | ✅ | ✅ | ❌ ambos off | — |
| **Gate de PR "não fura o protocolo" (Marvin)** | ❌ | ❌ | ✅ | ❌ | ❌ | — |
| **Security gate no PR** | ❌ | ❌ | ✅ | ❌ | ❌ | — |
| Auto-doc (agente → PR) | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ frota |
| CI de build/test travando merge | ❌ | ❌ | ⚠️ parcial | ❌ | ❌ | — |
| Design system + componentes (shadcn + tokens) | ✅ | ✅ | — | — | — (é back) | — |
| Multi-tenant / auth unificada de produção | ❌(stub) | — | ❌(stub) | ⚠️ CRUD partner | ✅ referência | — |
| CODEOWNERS / PR template / husky / commitlint | ❌ | ❌ | ❌ | ❌ | ❌ | — |
| Papéis humanos + rito de admissão de agente | — | — | — | — | — | ✅ |

**Leitura:** o "gold standard" de governança **não é** o fullstack (o veículo de vibecoding) — é o
**`backend-boilerplate`**, que é o único com **Marvin + security gate + tsconfig estrito + Cursor
rules**. O fullstack tem lint-as-código forte mas **não tem `.github/`**, logo **não herda os gates**.
O gateway, o mais maduro e central, é o **menos** rigoroso (`no-explicit-any: 'off'`).

## §3 — Q1: o que aproveitar do processo Lovable/PRD para treinar squads, agentes e operadores

O seu processo Lovable já tinha a forma certa; a produção tem as travas. **Treinamento = fundir os dois.**

### 3.1 Os 4 papéis-contrato (da era Lovable → produção)

O padrão que você montou no Lovable era 4 arquivos-contrato lidos no início de toda sessão. Ele
sobrevive **quase intacto** na produção, só muda o elenco:

| Papel (Lovable) | Arquivo | Vira na produção | Onde já existe |
|---|---|---|---|
| **Diretor de Negócios** (Claude Project) | `CLAUDE_DIRETOR.md` | quem pensa "por quê/o quê antes do como", escreve o PRD/ADR, prioriza | catalog-ai [C] |
| **CTO Full Stack** (Claude Code) | `CLAUDE.md` | **Bergson** como líder técnico + o Claude Code como executor sob o padrão dele | backend-boilerplate [C] |
| **Programador** (Lovable) | `AGENTS.md` + `.claude/*` + `.cursor/rules` | o agente que escreve código sob lint-as-código + design system | fullstack/back/integration [C] |
| **Operador** (humano) | `CLAUDE_OPERADOR.md` | **João, Vinícius, Pedro** (e mais, via BrainHub) | planejai (perfil do João) [C] |

**O que enriquecer (o que a produção não herdou do Lovable):**
- **PRD + ADR antes do código.** A era Lovable abria com PRD; a produção pula direto pro código. O
  Diretor (`CLAUDE_DIRETOR`) + a skill `adr-writing` reintroduzem o "porquê" — e o BrainHub já tem a
  skill. `[P]`
- **Guardrails de dados/deploy** do `catalog-ai AGENTS.md v7` (allowlist de campo ao espelhar API
  externa; prova determinística de deploy de edge function; "IA não-determinística não valida em 1
  rodada"). Nenhum boilerplate de produção tem isso — é candidato a portar. `[P]`
- **Política de Crédito Zero / minimizar chat pago** vira, na uMode, "minimizar rodada cega de LLM no
  CI" — o Marvin custa tokens, então o gate roda no PR, não a cada save. `[P]`

### 3.2 A camada que a produção tem e o Lovable não: rito + esteira (HERMES)

Do vault (`_GOVERNANCA.md` [C]) vêm as peças que faltavam ao processo Lovable para escalar operador:
- **Rito de admissão de agente** (governança → contrato `<AGENTE>.md` aprovado pelo João → **teste de
  obediência** → inbox → ritual). É literalmente o trilho do seu "criar mais operadores via BrainHub":
  cada operador/agente novo nasce com um contrato aprovado e um teste antes de ter acesso.
- **Promoção assistida (D63):** um agente só promove conteúdo seguro **se o próprio contrato conceder,
  com data e critério**. É o mecanismo formal de "autonomia sem furar o protocolo" — aplicado a
  contexto no vault, e transponível a código no boilerplate.
- **Heartbeat (D62) + Guarda determinística (D30):** nada entra em produção sem prova de vida; todo
  lote automático passa por script determinístico, **não por LLM**, antes de contar como entregue.
- **HERMES** = a esteira (ronda, digests, dispatch, promoção assistida). Levar o HERMES à produção =
  dar a ele um contrato que inclua os repos de código, não só o vault. `[P]`

### 3.3 O material de treinamento, consolidado (entregável derivado)

Um **kit de onboarding de squad** por projeto, reusando o que já existe:
1. `CLAUDE_OPERADOR.md` (perfil + glossário risolês do João) — **não muda por projeto** [C].
2. `CLAUDE_DIRETOR.md` — o papel de produto, por projeto.
3. `CLAUDE.md` + `AGENTS.md` + `.claude/*` + `.cursor/rules` — os contratos técnicos (do boilerplate).
4. O **Playbook de Engenharia uMode** (GitBook, "lei suprema" citada no catalog-ai) como topo.
5. O **PRD** (skill `adr-writing`/`doc-coauthoring`) como abertura de todo projeto novo.

## §4 — Q2: o que falta de governança nos repos de produção

Do mais grave ao menos, com dono sugerido `[D]`:

1. **O veículo de vibecoding (fullstack) não tem os gates.** O `fullstack-boilerplate` e o
   `frontend-boilerplate` **não têm `.github/`** → um PR pode furar o padrão e ninguém barra. O
   mecanismo existe (`actions-shared`), só não foi plugado ali. **É o buraco nº 1.** `[C]`
2. **O repo central (gateway) é o menos rigoroso.** `@typescript-eslint/no-explicit-any: 'off'`,
   `strictNullChecks:false`, `noImplicitAny:false`, sem `CLAUDE.md`/`AGENTS.md`. O `any` é livre no
   coração da plataforma. `[C]`
3. **Não há CI que rode lint+typecheck+test+build e trave o merge** em nenhum repo (o backend tem
   Marvin+security, mas não o gate de build/test verde). Sem isso, "definition of done" é documento,
   não trava. `[C]`
4. **Governança desigual entre repos** — 4 níveis diferentes de rigor para a mesma casa. Falta um
   **template único** e um mecanismo de sincronização (o `actions-shared` já é meio caminho). `[C]`
5. **Sem CODEOWNERS, PR template, husky/lint-staged, commitlint** em lugar nenhum → o gate local
   (antes do CI) não existe; tudo depende do CI remoto. `[C]`
6. **Auth é stub em todos os boilerplates** — correto por design (pluga no gateway), mas o "como
   plugar no gateway" **não está documentado em contrato**; cada projeto reinventa. `[C]`
7. **A produção não está no `SISTEMAS.md`** (ver §7).

## §5 — O boilerplate de produção governado (a espec)

**Não construir do zero. Endurecer o `fullstack-boilerplate`** (o veículo que o Brainwave já usa para
abrir 1 PR com front+back) até ele virar **template repository** onde o operador não consegue furar o
protocolo. Tudo abaixo é `[P]` (proposta minha), sujeito a `[D]` do João/Bergson.

### 5.1 O que ADICIONAR ao fullstack-boilerplate

1. **`.github/workflows/` com os 3 gates**, reusando `UmodeApp/actions-shared`:
   - `marvin-check.yml` → `pr-claude-md-gate` (trava PR por conformidade com CLAUDE.md). `[pendente actions-shared]`
   - `security-gate.yml` → `pr-security-gate`.
   - **`ci.yml` NOVO:** `npm run lint` + `tsc --noEmit` + `npm test` + `npm run build` nos dois apps,
     como **required checks** na branch protection de `main`/`awscicd`. **É a trava que falta.**
2. **Branch protection** em `main` e `awscicd`: PR obrigatório, required checks verdes, sem push direto.
   (É config de repo, decisão do Bergson/João `[D]`.)
3. **`CODEOWNERS`** — Bergson (+ time) donos de `apps/server`, `supabase`, `.github`, configs
   estruturais; operadores livres em `apps/web/src/app` e telas.
4. **PR template** com o checklist do "definition of done" (lint+build verdes, endpoint testado por curl).
5. **husky + lint-staged + commitlint** — gate local (pré-commit) antes do CI, para o operador ver o
   erro na hora, não no PR.
6. **Os 4 contratos de papel** (§6) na raiz: `CLAUDE.md`, `AGENTS.md`(+`.claude/*`), `CLAUDE_DIRETOR.md`,
   `CLAUDE_OPERADOR.md`. Os dois primeiros já existem no fullstack; faltam os dois de cima.
7. **Contrato de "como plugar no gateway"** — documentar `AUTH_MODE` (gateway/whoami/none),
   `services/<nome>`, `PartnerScopeGuard`: multi-tenant e auth unificada vêm **de graça** consumindo o
   gateway; ninguém reimplementa login.
8. **Uniformizar o rigor**: subir o gateway (e qualquer repo) para `no-explicit-any: 'error'` +
   tsconfig estrito — como dívida priorizada, não big-bang.

### 5.2 A trava que realiza "autonomia sem ferir o protocolo"

Três camadas, do mais barato ao mais caro, e **determinístico antes de LLM** (lição da Guarda do vault):
1. **Editor** (`.cursor/rules` + `CLAUDE.md`/`AGENTS.md`): o agente/operador é orientado enquanto escreve.
2. **Pré-commit** (husky + lint-staged): lint-as-código (no-any, i18n, no-pt) **barra localmente**.
3. **CI (required checks)**: `ci.yml` determinístico (lint/tsc/test/build) + **Marvin** (LLM, valida
   CLAUDE.md) + **security gate**. **Sem os 3 verdes, não há merge.** Aqui o protocolo deixa de ser
   confiança e vira máquina.

### 5.3 Como o operador cria um projeto novo
Template repository → "Use this template" → o novo repo **já nasce** com os gates, os contratos, o
design system e o plugue do gateway. O operador vibecoda em `apps/web`; toca `apps/server` sob o
padrão; **não consegue mergear nada que fure o lint/tsc/test/Marvin/security.** É o "Lovable, mas na
stack da uMode, com auditoria".

## §6 — Os 4 contratos de papel (elenco desta fase)

Esboço; o texto final entra no boilerplate. Elenco travado pelo Vinicius: HERMES na esteira, Bergson
líder técnico, operadores João/Vinícius/Pedro (mais via BrainHub).

- **`CLAUDE_DIRETOR.md` — Diretor de Produto/Negócios** (Claude Project). Pensa por quê/o quê; escreve
  PRD/ADR; prioriza; questiona quando a sequência cria risco pro cliente real. **Não** commita/roda
  SQL/deploya. Base: catalog-ai [C].
- **`CLAUDE.md` — CTO / Líder técnico (Bergson) + executor (Claude Code).** Guardião da qualidade
  (camadas, cache-aside, no-any, definition of done). Dono da doc de papéis. **Bergson é a autoridade
  técnica humana; o Claude Code executa sob o padrão dele e nunca altera fundação estrutural sem
  alinhamento.** Base: backend-boilerplate [C].
- **`AGENTS.md` + `.claude/*` + `.cursor/rules` — Programador** (Lovable/agente de código). Escreve sob
  lint-as-código + design system (`designsystem.umode.tech`) + shadcn + i18n obrigatório. Regra
  anti-reversão. Base: fullstack/frontend [C].
- **`CLAUDE_OPERADOR.md` — Operador humano** (João, Vinícius, Pedro). Perfil + glossário risolês; "não
  muda por projeto". Decide prioridade/jornada; valida entrega; **não** presume aprovação sem
  especificar. **Novos operadores entram pelo rito de admissão do vault (§3.2).** Base: planejai [C].
- **HERMES** — não é um dos 4 papéis; é a **esteira** (ronda, digests, promoção assistida, dispatch).
  Levar à produção = contrato próprio que inclua os repos de código, sob Guarda determinística. `[P]`

## §7 — Revisitar o `SISTEMAS.md` (vault)

O `SISTEMAS.md` [C] é catálogo gerado (D66: "nenhum agente constrói o que já existe sem consultar
este arquivo"). Hoje cataloga **66 repos, todos `HyTrackWater`** (o mundo Lovable). **A produção real
da `UmodeApp` — gateway, os 3 boilerplates, o integration — NÃO está nele.** Consequência: um agente
do João pode reconstruir do zero algo que já existe em produção (foi exatamente o incidente que gerou
o D66). **Ação `[P]`:** trazer os repos `UmodeApp` para o `sistemas_curadoria.json` (é escrita no
vault → é do João/HERMES, não nossa — proposta, não execução). Também corrigir a ficha do
`brainhub-umode` (o vault o marca "variante antiga/PowerShell"; ele é o corpus de contexto, não runtime).

## §8 — Roadmap sugerido (sequência, não prazo)

1. **Ler `actions-shared`** → fechar a seção de gate `[pendente]`. (1 relay CODEX.)
2. **Escrever os 4 contratos de papel** com o elenco desta fase (entregável textual).
3. **Endurecer o fullstack-boilerplate** (§5.1): gates + branch protection + CODEOWNERS + husky.
4. **Piloto:** João/Vinícius/Pedro criam 1 projeto do template e tentam furar o protocolo — o gate
   tem que barrar. (É o "teste de obediência" do rito, aplicado ao humano.)
5. **Uniformizar o rigor** do gateway (dívida priorizada).
6. **SISTEMAS.md** recebe a produção `UmodeApp` (proposta ao João/HERMES).

## §9 — Governança deste documento
Autoridade de conteúdo: CEO (João Risoléo). Alteração aqui exige refazer a leitura das fontes.
Grau geral: retrato de código lido campo a campo em 7 repos; **1 dependência aberta** (`actions-shared`),
marcada em cada ponto. Fonte de trabalho: `scratchpad/achados-repos-producao.md` (dumps verbatim do
CODEX, com commit+sha por repo).

### Conexões
`_recebido-2026-08-18-context-pack-brainhub-2.0.md` · `_inventario-repositorios.md` ·
`SISTEMAS.md` (vault) · `_GOVERNANCA.md` (vault) · Playbook de Engenharia uMode (GitBook)
