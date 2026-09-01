# Blueprint — Boilerplate de produção governado + treinamento de squads/agentes/operadores

> Documento de espec e decisão. Nasce da missão do Vinicius (set/2026): ter um repositório-padrão de
> produção onde um operador de negócio (ele, o João, o Pedro) **vibecoda com autonomia, na stack real
> da uMode, sem poder ferir o protocolo** — com o HERMES como esteira de produção, o CTO/líder técnico
> como agente e o Bergson como arquiteto dos MDs de treinamento, governança e segurança de infra.
> Autoridade de conteúdo: CEO (João Risoléo), conforme governança travada em 17 ago 2026.

## §0 — Declaração de completude (o que este documento NÃO resolve)

Regra da casa ("a lacuna vem antes da conquista"): o que falta, antes do que fecha.

- **O gate foi lido (fechado em 01 set 2026).** O `UmodeApp/actions-shared` (`pr-claude-md-gate` =
  "Marvin" + `pr-security-gate`) foi lido campo a campo [C], commit `5d82fa2`. A mecânica está na §5.4.
  Não há mais `[pendente actions-shared]`.
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
| `UmodeApp/actions-shared` | **mecanismo dos gates (Marvin + security)** | `5d82fa2` | `d2a266…87f4f8` | [C] |

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
| **CTO Full Stack** (Claude Code) | `CLAUDE.md` | um **agente** que desenha o *como* e audita (não é o Bergson — ele é o arquiteto dos MDs de treinamento/governança/segurança de infra) | backend-boilerplate [C] |
| **Programador** (Lovable) | `AGENTS.md` + `.claude/*` + `.cursor/rules` | o executor que escreve código sob lint-as-código + design system: esteira **HERMES** · **Codex** · **Claude Code** (o **Lovable saiu da stack**) | fullstack/back/integration [C] |
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

1. **`.github/workflows/` com os 3 gates**, reusando `UmodeApp/actions-shared` (mecânica lida — §5.4):
   - `marvin-check.yml` → `uses: UmodeApp/actions-shared/.github/workflows/pr-claude-md-gate.yml@main`
     + `secrets: inherit` (trava PR por conformidade com CLAUDE.md; `mode: block`). [C]
   - `security-gate.yml` → `uses: .../pr-security-gate.yml@main` (semgrep + gitleaks). [C]
   - **`ci.yml` NOVO:** `npm run lint` + `tsc --noEmit` + `npm test` + `npm run build` nos dois apps,
     como **required checks** na branch protection de `main`/`awscicd`. **É a trava determinística que
     ainda falta** — o `actions-shared` só cobre Marvin (LLM) + security, não build/test/lint verde.
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
9. **Adotar o design system publicado `@umodeapporg/ui`** no `apps/web` (preset Tailwind + `base.css`
   + `styles.css` + componentes) — já vive no boilerplate só-front, falta no fullstack. Detalhe em §5.5.

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

### 5.4 A mecânica do gate `actions-shared` (lido — `5d82fa2` [C])

Repositório minúsculo (2 workflows), reusáveis via `workflow_call`. Um repo-alvo adota com um `uses:`
+ `secrets: inherit`; **nada mais precisa existir no alvo além do `CLAUDE.md` e do gatilho de PR.**

**`pr-claude-md-gate.yml` (Marvin) — como decide:**
- Inputs: `claude_md_path` (default `CLAUDE.md`), `model` (default `openai/gpt-4o-mini`, GitHub
  Models), `mode` (`block`|`warn`, default `block`), `max_diff_bytes` (120000).
- Fluxo: se não achar o `CLAUDE.md`, **pula** (não trava). Extrai o **diff do PR** (`base...head`,
  truncado a 120KB) → chama `https://models.github.ai/inference/chat/completions` com `temperature 0`,
  `response_format: json_object`, e system prompt estrito: *"identifique APENAS violações de regras
  explicitamente declaradas no CLAUDE.md — não invente regras"*, schema `{compliant, violations[],
  summary}` → posta **comentário sticky** (marcador `<!-- claude-md-gate -->`, faz PATCH no existente)
  → **falha o check** se `compliant=false` e `mode=block`. Auth: só `GITHUB_TOKEN` (`models: read`).
- **Consequências de desenho** que o boilerplate deve respeitar:
  - O gate julga **o diff, não o repo inteiro** → regra do `CLAUDE.md` que só se verifica olhando o
    arquivo todo (ex.: "nunca dois documentos vivos do mesmo tema") **não é pega**. Regra que se quer
    travada tem que ser **verificável no diff**.
  - **É um LLM barato (gpt-4o-mini) a temperatura 0** — bom para regras explícitas e literais ("nunca
    `any`", "nada de português no código"), fraco para julgamento sutil. Por isso ele é a **terceira**
    camada, depois do lint determinístico (§5.2), nunca a primeira.
  - `CLAUDE.md` **explícito e enumerável** = gate eficaz. Regra vaga = gate inútil. Isso **eleva o
    `CLAUDE.md`** de documentação a **contrato executável** — escrever a regra bem é o trabalho.
  - Sem `CLAUDE.md`, o gate se auto-pula → **todo repo do template nasce com `CLAUDE.md`**, senão a
    trava é decorativa (mesmo modo de falha do heartbeat "decorativo" do vault).

**`pr-security-gate.yml` — o que varre:** dois jobs bloqueantes, **só o delta do PR**:
- **semgrep** (`p/owasp-top-ten`, `p/security-audit`, `p/javascript`, `p/typescript`, `p/nodejs`,
  `--baseline-commit=<base>` = só achados NOVOS, `--severity=ERROR --error`).
- **gitleaks** (segredos no range `base..head`, `--redact --exit-code=1`).
- Nenhuma chave paga; roda no `GITHUB_TOKEN`. **É defesa de "operador não commita segredo/vuln"** — a
  contraparte de segurança do Marvin, e a resposta direta aos incidentes de credencial em texto plano
  já registrados no vault (RISC-001) e nos guardrails do catalog-ai.

**Lacuna que o `actions-shared` NÃO cobre (e o boilerplate precisa somar):** não há job de
**lint + typecheck + test + build** verde. Marvin valida *conformidade com regra*; security valida
*vulnerabilidade/segredo*; **nada valida que o código compila e passa nos testes.** O `ci.yml` da
§5.1 é essa peça — determinística, a mais barata, e a que falta.

### 5.5 O design system é uma biblioteca publicada: `@umodeapporg/ui`

O design system da uMode **não é para reimplementar por projeto** — ele já está empacotado, versionado
e publicado. Lido campo a campo no tarball `@umodeapporg/ui@0.4.1` (npm público, `registry.npmjs.org`,
sem token) e no repo `UmodeApp/umode-ui`.

- **O que o pacote entrega** [C — `package.json`/`README.md`/`theme.css` lidos no tarball]:
  - **Tokens de tema** (`@umodeapporg/ui/theme.css`): fonte única de cor, claro **e** escuro, em canais
    RGB separados por espaço (para o modificador de opacidade do Tailwind). Cada par verificado em
    **WCAG 2.1 AA** (AAA para texto de corpo). Papéis, nunca shades: `surface`, `foreground`, `border`,
    `primary`(roxo `#973BEB` claro / `140 63 214` escuro), `secondary`(teal), `accent`(magenta),
    `success/warning/danger/info`, `chart-1..8`.
  - **Preset Tailwind** (`@umodeapporg/ui/tailwind-preset`): expõe os tokens como utilidades semânticas
    (`bg-surface`, `text-foreground`, `border-strong`, `shadow-md`…), a família `Inter`, a escala de
    movimento (`duration-fast|base|slow`, easings enter/exit), a rampa de elevação e os breakpoints.
  - **Camada base** (`base.css` / `styles.css`): aplica os tokens à raiz + o swap de tema atômico
    (`.theme-switching`) sem flash e sem blend.
  - **Componentes React** (import raso ou profundo): `Form/*` (Controlled*), `UI/*` (`DataTable`,
    `Kanban`, `MaterialSymbol`, `Toast`, `CustomChart`…), `Search` (`UnifiedSearchBar`+filtros),
    `Navigation` (`PageTitle` com breadcrumb automático), e o `<UmodeLogo/>` (SVG inline que herda
    `currentColor` — o logo segue o tema sem segundo asset).
  - **Helpers/hooks puros** e locales `pt`/`en`.
- **Como um app adota** [C — README]: `presets: [preset]` no `tailwind.config.js` + `content` incluindo
  `node_modules/@umodeapporg/ui/dist/**/*.js`; `import '@umodeapporg/ui/styles.css'` e `base.css` no entry.
- **Release** [C — README]: merge na `main` **é** o release — `semantic-release` lê Conventional Commits
  (`fix`→patch, `feat`→minor, `feat!`→major), publica no npm, cria tag+changelog; label `canary`
  publica `0.0.0-canary.<sha>` para testar uma PR num app antes do merge.

**Estado da adoção** [D — relatado pelo desenvolvedor via Vinicius, 1 set 2026]:
- **Boilerplate só-front** (`boilerplate.umode.app`) — **já usa** `@umodeapporg/ui`. ✅
- **`fullstack-boilerplate`** — **ainda não**, "porque a galera está usando". ⏳ **Item de spec deste
  ciclo:** adicionar `@umodeapporg/ui` como dependência do `apps/web`, plugar o preset + `base.css` +
  `styles.css`, e trocar o design system local por consumo da biblioteca. É a peça que faltava no
  §5.3 (o "design system" que o template deveria herdar agora tem nome, versão e registry).

**Consequência para os gates:** com o design system como pacote, a regra "não reinventar componente/token"
vira verificável — um `ControlledButton` reescrito à mão no `apps/web` é desvio de `@umodeapporg/ui`, não
liberdade de tela. Candidato a regra explícita no `CLAUDE.md` do boilerplate (logo, pegável pelo Marvin
no diff — §5.4) e a entrada no `SISTEMAS.md` (§7): *o UI kit da casa já existe; não se reconstrói.*

## §6 — Os 4 contratos de papel (elenco desta fase)

Esboço; o texto final entra no boilerplate. Elenco travado pelo Vinicius: HERMES é a esteira de
produção (e um dos executores do Programador, junto de Codex e Claude Code); o CTO/líder técnico é um
**agente**; o Bergson é o **arquiteto dos MDs de treinamento, governança e segurança de infra**;
operadores João/Vinícius/Pedro (mais via BrainHub). O **Lovable saiu da stack de execução**. A camada
de orquestração humana ganha mais pessoas depois desta fase.

- **`CLAUDE_DIRETOR.md` — Diretor de Produto/Negócios** (Claude Project). Pensa por quê/o quê; escreve
  PRD/ADR; prioriza; questiona quando a sequência cria risco pro cliente real. **Não** commita/roda
  SQL/deploya. Base: catalog-ai [C].
- **`CLAUDE.md` — CTO / Líder técnico (agente).** Guardião da qualidade (camadas, cache-aside, no-any,
  definition of done); desenha o *como* e audita; dono da doc de papéis. **Não é o Bergson** — o
  Bergson é o arquiteto dos MDs de treinamento, governança e segurança de infra (autoridade sobre o
  padrão e destino de escalonamento, não executor por dimensão). A execução fica com o Programador.
  Base: backend-boilerplate [C].
- **`AGENTS.md` + `.claude/*` + `.cursor/rules` — Programador** (esteira **HERMES** · **Codex** ·
  **Claude Code**; o **Lovable saiu da stack de execução**). Escreve sob lint-as-código + design
  system (`@umodeapporg/ui`, referência em `designsystem.umode.tech`) + i18n obrigatório; cânone
  shadcn × `@umodeapporg/ui` ainda `[D]` em aberto. Regra anti-reversão. Base: fullstack/frontend [C].
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

1. ~~Ler `actions-shared`~~ ✅ feito (§5.4).
2. **Escrever os 4 contratos de papel** com o elenco desta fase (entregável textual).
3. **Endurecer o fullstack-boilerplate** (§5.1): os 3 gates (Marvin + security + `ci.yml` novo) +
   branch protection (required checks) + CODEOWNERS + PR template + husky/lint-staged/commitlint.
4. **Piloto:** João/Vinícius/Pedro criam 1 projeto do template e tentam furar o protocolo — o gate
   tem que barrar. (É o "teste de obediência" do rito, aplicado ao humano.)
5. **Uniformizar o rigor** do gateway (dívida priorizada: `no-any: error` + tsconfig estrito).
6. **SISTEMAS.md** recebe a produção `UmodeApp` (proposta ao João/HERMES).

## §9 — Governança deste documento
Autoridade de conteúdo: CEO (João Risoléo). Alteração aqui exige refazer a leitura das fontes.
Grau geral: retrato de código lido campo a campo em **8 repos** (5 produção UmodeApp + 2 Lovable +
`actions-shared`) mais a constituição do vault; **zero dependências abertas** — o gate foi lido
(§5.4). Fonte de trabalho: `scratchpad/achados-repos-producao.md` (dumps verbatim do CODEX, com
commit+SHA-256 por repo).

### Conexões
`_recebido-2026-08-18-context-pack-brainhub-2.0.md` · `_inventario-repositorios.md` ·
`SISTEMAS.md` (vault) · `_GOVERNANCA.md` (vault) · Playbook de Engenharia uMode (GitBook)
