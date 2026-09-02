# Governança da Squad de Desenvolvimento uMode

> Documento de governança do desenvolvimento de software na uMode. Define **quem faz o quê** (os
> personagens), **sob quais premissas** (padrão, segurança), **como se audita** tudo isso, e **como o
> aprendizado retroalimenta** os documentos vivos (CLAUDE.md, CONTEXT, README, docs).
> Lastro: leitura campo a campo dos 5 repositórios de produção da `UmodeApp`, dos 2 repositórios da era
> Lovable (`HyTrackWater`) e da constituição do vault (`_GOVERNANCA.md`). Procedência por commit+SHA
> em `_contexto/_blueprint-boilerplate-governado.md` §1. Autoridade de conteúdo: CEO (João Risoléo).

## §0 — Declaração de completude (o que este documento NÃO resolve)

- **Descreve o alvo, não o estado.** O padrão descrito aqui é o que a análise recomenda; **hoje ele
  está desigual entre os repos** (o `backend-boilerplate` já cumpre quase tudo; o `fullstack` e o
  `gateway` não têm os gates). Cada afirmação carrega grau: `[C]` lido em código (arquivo citado no
  blueprint) · `[F]` existe mas só em parte dos repos · `[P]` proposta minha · `[D]` decisão do João/Bergson.
- **Não implementa.** É governança escrita; a aplicação nos repos da `UmodeApp` é escrita naquela org
  (fora do alcance de escrita deste projeto, que só grava no `brainhub-umode`).
- **A árvore de permissão fina** (quem aprova o quê, CODEOWNERS exato) fica `[D]` do João/Bergson.
- **O contrato do HERMES para código** (hoje ele é esteira do vault) é `[P]` — não existe ainda.

## §0-bis — Estado de cada controle (regra de honestidade — parecer 2026-09-02)

Todo controle deste documento é um de três estados. **Diagrama ou check local não é enforcement.**
Este documento **nunca descreve no presente** um gate que está em `ALVO`.

- `ALVO` — desenhado, **sem enforcement**.
- `IMPLEMENTADO` — código/config existe.
- `ATIVO E VERIFICADO` — required no repo/ambiente **+ lido de volta com evidência e data**.

O método da squad é o **SmartCoding** (nome autoral uMode — nunca "Vibe Coding"; `identidade-verbal` do vault).
Companion vivo desta versão: `parecer-smartcoding-esteira-2026-09-02.md` (revisão adversarial do pacote
HERMES, PR #15 do `umode-os-vault`).

## §1 — Objetivo e escopo

Permitir que **operadores de negócio experientes** (João, Vinícius, Pedro e futuros) criem software na
**stack real da uMode** — como faziam no Lovable — mas com **padrão, qualidade, auditoria e segurança
travados por máquina**, não por confiança. O princípio-mestre:

> **Autonomia para criar, sem autonomia para ferir o protocolo.** A regra não é um PDF que se pede
> para ler; é um gate que barra o merge.

Escopo: todo repositório de produto/serviço da uMode (front, back, integração), a partir de um
**boilerplate-template governado**. Fora de escopo: o runtime do BrainHub 2.0 (Mongo/NestJS do João),
tratado em `_espec-banco-brainhub.md`.

## §2 — Os personagens

A squad tem **duas camadas de personagens**: os **papéis-contrato** (quem decide/executa/opera, herdados
da era Lovable) e as **oito dimensões funcionais** (as especialidades que a arquitetura exige). Cada
dimensão tem um **dono**, uma **camada de código** e um **guardrail** que a trava.

### 2.1 Papéis-contrato (arquivos lidos no início de toda sessão)

| Papel | Arquivo-contrato | Quem é | Pode / Não pode |
|---|---|---|---|
| **Operador** | `CLAUDE_OPERADOR.md` | João, Vinícius, Pedro (humanos) | Traz demanda, decide prioridade/jornada, valida entrega. Não presume aprovação sem especificar. |
| **Diretor de Produto** | `CLAUDE_DIRETOR.md` | Claude (Project) | Escreve **PRD/briefing/aceite** + decisão de produto (o **ADR técnico é do CTO**), pensa por quê/o quê, prioriza. Não commita, não roda SQL, não deploya. |
| **CTO / Líder técnico** | `CLAUDE.md` | **agente** (não é o Bergson) | Desenha o *como*, dono da doc de papéis. **NÃO audita o próprio head** (isso é do Auditor). Não altera fundação sem alinhar. |
| **Programador** | `AGENTS.md` + `.claude/*` + `.cursor/rules` | esteira **HERMES** · **Codex** · **Claude Code** | Escreve sob lint-as-código + design system. Regra anti-reversão. **Não aprova o próprio head.** |
| **Auditor Independente** | `governance/roles/AUDITOR.md` `[P]` | cadeira **não-autor** (agente-auditor ou pessoa ≠ autor) | Parecer **exact-SHA** sobre spec/código/segurança de quem não escreveu o head. Não edita o candidato. |
| **HERMES** | `HERMES_TRAINING.md` `[P]` | **sistema / esteira** | Aplica transições **já autorizadas**; Guarda determinística, heartbeat, leases. **Nunca é "A" no RACI**; não decide canonicidade nem produto. |

> **Fora do elenco de execução, dois pontos fixos:** o **Bergson** é o **arquiteto dos MDs de
> treinamento, governança e segurança de infra** (autoridade sobre o padrão e destino de escalonamento,
> não dono de execução por dimensão); o **Lovable saiu da stack de execução**. A **camada de orquestração
> humana** ganha mais pessoas depois desta fase.

### 2.2 As oito dimensões funcionais

| Dimensão | Dono | Camada de código | Guardrail que a trava |
|---|---|---|---|
| **Back** | CTO (agente) + Programador | `apps/server`, gateway (NestJS Modular Standard: Controller→Service→Repository, cache-aside) [C] | lint `no-any`, tsconfig estrito, Marvin (CLAUDE.md), `ci.yml` (test/build) |
| **Front** | Programador + Operador | `apps/web` (Next App Router, **`@umodeapporg/ui`** — sem shadcn; canônico `umode-frontend-boilerplate-nextjs`) [C]/[D] | eslint-rules próprias: `no-any`, `no-portuguese`, `no-literal-jsx` (i18n obrigatório) |
| **Dados & IA** | área Dados & IA | agentes, RAG, contexto, BrainHub | contratos de agente + rito de admissão (vault) |
| **Banco de Dados** | CTO (agente) — desenho | Mongo (Mongoose, multi-cluster nomeado, collection nasce no 1º write) + Redis (cache-aside, TTL obrigatório) + relacional/ERP [C] | Repository é o único acesso; chave Redis `PROJECT:MODULE:ID`; `.lean()` em leitura |
| **Deploy** | HERMES / infra | Amplify (web) + CodeBuild/Procfile (server) + registro downstream no gateway [C runtime] | branch protection + required checks: **`[P]` — ainda NÃO vigente** (o `ci.yml` não existe; parecer C1) |
| **Segurança** | security-gate + Bergson (infra) | Cognito (auth unificada), `PartnerScopeGuard` (multi-tenant), segredos fora do repo [C] | **gitleaks** (segredos) + **semgrep** (OWASP/SAST) no PR; auth via gateway, nunca própria |
| **Integração** | squad de integração | `microservice-integration`, Lambdas, proxy `services/<nome>`, config por partner, conectores ERP [C] | allowlist de campo ao espelhar API externa (lição catalog-ai); `INTEGRATION_ID` rastreado |
| **Documentação** | documentation-agent + HERMES | `documentation-agent`/`typedoc` → PR; `CLAUDE.md`/`AGENTS.md`/`docs/`; BrainHub [C] | auto-doc em PR isolado; front-matter; `SISTEMAS.md` (D66) |

### 2.3 Diagrama — os personagens e como se ligam

```mermaid
flowchart TB
    OP["👤 OPERADOR<br/>João · Vinícius · Pedro<br/>(CLAUDE_OPERADOR.md)"]
    DIR["🎯 DIRETOR DE PRODUTO<br/>Claude Project<br/>PRD · briefing · aceite<br/>(CLAUDE_DIRETOR.md)"]
    CTO["🛠️ CTO / LÍDER TÉCNICO<br/>agente · desenha + ADR técnico<br/>não audita o próprio head<br/>(CLAUDE.md)"]
    PROG["⌨️ PROGRAMADOR<br/>HERMES · Codex · Claude Code<br/>(AGENTS.md · .cursor/rules)"]
    AUDIT["🔎 AUDITOR INDEPENDENTE<br/>não-autor · exact-SHA<br/>(AUDITOR.md)"]
    HERMES["🔁 HERMES (sistema)<br/>esteira: ronda · auto-doc<br/>executa merge já autorizado"]

    OP -->|demanda| DIR
    DIR -->|PRD / aceite| CTO
    CTO -->|padrão + ADR técnico| PROG
    PROG -->|candidato| AUDIT
    AUDIT -->|parecer não-autor| GATES

    subgraph DIM["8 DIMENSÕES FUNCIONAIS"]
        BACK["Back<br/>NestJS Modular"]
        FRONT["Front<br/>Next + @umodeapporg/ui + i18n"]
        DADOS["Dados & IA<br/>agentes · RAG"]
        DB["Banco<br/>Mongo · Redis · SQL"]
        DEPLOY["Deploy<br/>Amplify · CodeBuild"]
        SEC["Segurança<br/>Cognito · tenant · segredos"]
        INT["Integração<br/>gateway · Lambdas · ERP"]
        DOC["Documentação<br/>auto-doc · CLAUDE.md"]
    end

    PROG --- DIM
    GATES{{"⛔ GATES DE AUDITORIA<br/>(§6)"}}
    GATES -->|3× verde @ mesmo head| MERGE["merge autorizado<br/>(≠ deploy ≠ aceite)"]
    GATES -->|vermelho| PROG
    MERGE -->|aprendizado / incidente| HERMES
    HERMES -->|atualiza MDs / regras| CTO
    HERMES -.->|catálogo / contexto| DOC
```

### 2.4 Autoridade por transição (RACI) — parecer 2026-09-02

**Invariante que fecha a auto-revisão: quem escreveu o head não emite o parecer desse head.**
Aprovar PR, migration, merge e promoção são ações **diferentes**. **HERMES nunca é `A`** (é sistema).

| Atividade | Operador | Diretor | CTO | Program. | Auditor | HERMES | Bergson |
|---|---|---|---|---|---|---|---|
| Prioridade / aceite funcional | **A** | R | C | · | · | · | · |
| PRD / critério de aceite | C | **A** | C | · | · | · | · |
| Desenho não-infra | C | C | **A** | C | · | · | · |
| Infra / IAM / auth / pipeline | C | · | R | · | C | · | **A** |
| Implementação (código+testes) | · | · | C | **A** | · | sup | C |
| Auditoria exact-SHA | · | · | C | · | **A** | evid | C |
| Merge autorizado (não-infra) | **A** | · | R | · | parecer | exec | · |
| Merge autorizado (infra/auth/pipeline) | C | · | R | · | parecer | exec | **A** |
| Deploy staging/prod | · | · | C | evid | parecer | exec | **A** conforme ambiente |
| Rollback | · | · | C | · | · | exec | **A** conforme ambiente |

`exec` = HERMES executa uma capability **já autorizada** (não decide, nunca é `A`). **Um único `A` por
classe de merge:** merge **não-infra** é `A` do **Operador** (owner humano — "aprovar merge" é ação só
do humano, `CLAUDE_OPERADOR.md`); merge que toca **infra/IAM/auth/pipeline** é `A` do **Bergson**. Em
ambos, **pré-condições** (não substituem o `A`): parecer do **Auditor não-autor** + **CODEOWNERS por
dimensão** + **3 required checks verdes @ mesmo head** + sem conflito. **Sem autoaprovação:** o `A` de
merge **nunca é quem escreveu o head** — se o próprio owner vibecodou o head, o `A` passa ao **segundo
decisor** (readiness gate, `HERMES_TRAINING.md` §2). O **Auditor é só parecer, nunca `A`**.

## §3 — Premissas de desenvolvimento (as regras travadas)

Regras identificadas nos repos de produção `[C]`, que todo projeto herda do boilerplate:

**Arquitetura (back):** camadas estritas **Controller → Service → Repository → Database**, nunca pular;
Controller sem lógica; Service sem query bruta; Repository é o **único** acesso ao banco; `common/`
nunca importa de `modules/`. **Cache-Aside** obrigatório em leitura (Redis com **TTL sempre**), chave
`PROJECT:MODULE:ID` centralizada. Envelope de resposta `{success, data, error, requestId}`.

**Arquitetura (front):** **Server Components por padrão**, `'use client'` só quando preciso; `useEffect`
é último recurso, nunca `setState` dentro dele; **`@umodeapporg/ui`** é o padrão de UI (sem shadcn); **Zustand** só para
estado global; HTTP só via `gatewayHttpClient` (nunca `fetch` cru).

**Tipagem e estilo:** **proibido `any`** (erro de lint), `Array<T>` (não `T[]`), sem `console.*` (usar
`logger`), sem `.then/.catch` (usar `async/await`), sem chaves omitidas. **tsconfig estrito**
(`noImplicitAny`, `strictNullChecks`).

**Internacionalização (i18n):** **nenhuma string visível hardcoded** — tudo via `t('namespace.key')`,
chave presente em `pt` **e** `en`; **proibido português no código** (regra de lint própria). Sem
travessão (`—`) em texto de usuário.

**Design system:** fonte é a **biblioteca publicada `@umodeapporg/ui`** (tokens claro/escuro, preset
Tailwind, componentes, `<UmodeLogo/>`); referência viva em `designsystem.umode.tech`. **Nunca**
hex/`rgb()`/paleta Tailwind crua — nomear o **papel** (`bg-surface`, `text-foreground`,
`bg-danger-soft`). **Cânone travado `[D]` (Vinicius, set/2026):** o padrão é `@umodeapporg/ui`, **sem
shadcn** — o boilerplate canônico de front é `UmodeApp/umode-frontend-boilerplate-nextjs`.

**Auth:** **login unificado uMode** (Cognito via gateway) — o produto **não tem login próprio**;
consome o gateway (`AUTH_MODE` gateway/whoami/none, `req.executor`). Multi-tenant via
`PartnerScopeGuard` — rota com `:partnerId` só aceita o partner ativo.

**Commits:** Conventional Commits em inglês (`feat(escopo): ...`); **nunca** trailer de co-autoria de IA
nas mensagens de commit de produto.

## §4 — O padrão (o boilerplate-template)

Não se cria projeto do zero: parte-se do **`umode-fullstack-boilerplate` endurecido** como *template
repository*. "Use this template" → o repo novo **já nasce** com: os contratos de papel (Operador,
Diretor, CTO, Programador, Auditor) + o HERMES como sistema, o lint-as-código,
o design system, o plugue do gateway, e os **3 gates de auditoria** (§6). Estrutura fixa:
`apps/web` (Next) + `apps/server` (Nest) + `.env` único na raiz. Módulo = **fatia vertical**
(schema → DTO → repository → service → controller → interface → repository front → store → hook → tela).
Nomenclatura: arquivos kebab-case, classes PascalCase com sufixo, tudo em inglês.

**Boas práticas HyTrack/Lovable que agregam ao padrão** (não estavam na produção): **PRD + ADR antes do
código** (skills `adr-writing`/`doc-coauthoring`); **guardrails de dados** do catalog-ai (allowlist de
campo ao espelhar API externa; prova determinística de deploy; "IA não valida em 1 rodada só").

## §5 — Segurança

- **Segredo nunca no repo nem em Downloads** — vai direto ao gerenciador de senhas (regra do vault,
  reforçada pelos incidentes RISC-001: credenciais de ERP em texto plano). `.env` nunca versionado.
- **gitleaks** varre segredos no range de commits de todo PR (bloqueante). `[C]`
- **semgrep** varre OWASP Top Ten + SAST js/ts/node **só no delta do PR** (achado novo = falha). `[C]`
- **Menor privilégio:** usuário de banco com role mínima por cluster; auth sempre pelo gateway;
  isolamento por tenant (`PartnerScopeGuard`) não é opcional.
- **Espelhar dado de terceiro é allowlist, nunca "traz tudo"** — filtra antes de gravar, falha fechado.

## §6 — O processo de auditoria (três camadas, determinístico antes de LLM)

A trava tem **três camadas**, do mais barato ao mais caro. Princípio herdado do vault: **o
determinístico vem antes do LLM** (a Guarda de Governança do HERMES é script, não modelo).

1. **Editor (enquanto escreve):** `.cursor/rules` + `CLAUDE.md`/`AGENTS.md` orientam o agente/operador.
2. **Pré-commit (local):** husky + lint-staged rodam o lint-as-código (`no-any`, i18n, `no-portuguese`).
   O erro aparece na hora, não no PR. `[P]`
3. **CI (no PR, três required checks nomeados, todos no MESMO head — qualquer commit novo invalida os três):**
   - **`ci-deterministic`** (`ci.yml`, o mais barato): `lint` + `tsc --noEmit` + `test` + `build` nos dois
     apps. **É a peça que o `actions-shared` não cobre e precisa ser criada.** `[P]`
   - **`policy-semantic`** (Marvin, `pr-claude-md-gate`): LLM (GitHub Models, gpt-4o-mini, `temperature 0`)
     lê o **diff** contra o `CLAUDE.md` → `{compliant, violations[]}`, sticky, **block** em violação. **É
     review semântica versionada, NÃO determinismo** — temperatura 0 não é determinismo. Deve registrar
     model/prompt/rules SHA + schema; vale a nossa própria regra "IA não valida em 1 rodada só" (parecer
     C2): ou é advisory, ou é versionado com política de repetição. `[C]`
   - **`security`** (`pr-security-gate`): semgrep + gitleaks no delta. `[C]`

   **Merge ≠ deploy ≠ runtime ≠ aceite** (parecer P0.5). O **Auditor Independente** (não-autor, exact-SHA)
   emite parecer **antes** dos gates; o **aceite** é sempre decisão autenticada de um humano.

**Consequência de desenho:** o Marvin julga **o diff, não o repo inteiro**, e é um LLM literal —
então **o `CLAUDE.md` tem que ser explícito, enumerável e verificável no diff** para o gate ter dente.
Isso eleva o `CLAUDE.md` de documentação a **contrato executável**: escrever a regra bem É o trabalho de
governança. Sem `CLAUDE.md`, o Marvin se auto-pula → **todo repo do template nasce com um**.

Acima das três camadas, **code review humano** (Bergson + CODEOWNERS) para o que a máquina não pega:
decisão de arquitetura, jornada de produto. E **branch protection**: PR obrigatório, sem push direto em
`main`/`awscicd`.

### 6.1 Diagrama — pipeline de auditoria

```mermaid
flowchart LR
    DEV["Operador / Programador<br/>escreve código"]
    R1["1 · EDITOR<br/>.cursor/rules · CLAUDE.md"]
    R2["2 · PRÉ-COMMIT<br/>husky + lint-staged<br/>(no-any · i18n · no-pt)"]
    PR(["Pull Request<br/>→ main / awscicd"])

    subgraph CI["3 · CI — required checks (bloqueiam o merge)"]
        direction TB
        CIYML["ci.yml (determinístico)<br/>lint · tsc · test · build"]
        MARVIN["Marvin (LLM)<br/>diff × CLAUDE.md<br/>→ block em violação"]
        SEC["Segurança<br/>semgrep + gitleaks"]
    end

    AUDIT["Auditor independente<br/>exact-SHA · não-autor"]
    REVIEW["Code review humano<br/>CODEOWNERS por dimensão"]
    MERGE{{"3× verde @ MESMO head?"}}
    STG["Deploy staging<br/>Amplify · CodeBuild"]
    RB["Runtime readback<br/>request real · redigido"]
    ACC["Aceite<br/>owner humano"]
    PROD["Prod autorizado<br/>+ readback"]

    DEV --> R1 --> R2 --> PR --> AUDIT --> CI
    CIYML --> MERGE
    MARVIN --> MERGE
    SEC --> MERGE
    PR --> REVIEW --> MERGE
    MERGE -->|sim| STG --> RB --> ACC --> PROD
    MERGE -->|não · sticky| DEV
```

### 6.2 A esteira estado a estado (enriquecimento do parecer)

A constituição de PR vira **esteira executável**: cada transição tem owner, identidade (base/head/tree
SHA), evidência e recuperação. **Nenhum estado implica o próximo automaticamente.** Núcleo **aplicável
já por disciplina humana + branch protection** — mas **ainda NÃO travado por máquina** (`ci.yml`/required
checks e o rito de admissão são **`ALVO`**, não existem hoje; parecer C1) — vs. `ALVO` puro (entra
quando houver pipeline). "Aplicável por disciplina" ≠ "em vigor automático".

```mermaid
flowchart LR
    A["1 INTENT"] --> B["2 READINESS"] --> C["3 SCOPE OK"] --> D["4 PLAN OK"] --> E["5 LEASE<br/>(sem lease = read-only)"]
    E --> F["6 RED"] --> G["7 LOCAL GREEN"] --> H["8 AUDIT independente<br/>não-autor · exact-SHA"]
    H --> I["9 3 CHECKS @head<br/>ci-det · policy · security"] --> J["10 PR CI @head"] --> K["11 MERGE autorizado"]
    K --> L["12 DEPLOY staging"] --> M["13 RUNTIME readback"] --> N["14 ACEITE (owner humano)"]
    N --> O["15 LEARNING + supersession"] --> P["16 CLOSED"]

    ALVO["ALVO (quando houver pipeline):<br/>release-attested · drift · canário · rollback-proven"]
    EXC["Exceções: READINESS_BLOCKED · CHANGE_REQUIRED · CI_RED<br/>WAITING_CAUSAL_EVIDENCE · ROLLED_BACK · SUPERSEDED · DECLINED"]
    L -.-> ALVO
```

**Merge ≠ deploy ≠ runtime ≠ aceite.** "3× verde" só conta no mesmo head. O Auditor (8) entra antes dos
gates; o aceite (14) é sempre humano. Publicar a máquina inteira antes do `ci.yml` existir seria controle
decorativo — por isso os estados de attestation/canário ficam `ALVO`.

## §7 — Retroalimentação: aprender e atualizar os MDs

O sistema **aprende com o próprio erro** e transforma aprendizado em **regra executável**. O gatilho é
sempre um evento real (incidente, revisão, decisão do João); o destino é um **documento vivo**
(`CLAUDE.md`, `DECISOES.md`, `CONTEXT`, `README`, `docs/`), e — quando vira regra — o **gate passa a
cobrá-la**. Fecha o ciclo.

**As engrenagens (todas identificadas em código/governança real):**
- **`DECISOES.md` (registro-fonte):** toda decisão do João espelha-se aqui **antes** de ser executada
  (data · decisão · status). Decisão não escrita é decisão não tomada. `[C]` vault.
- **Aprendizado → regra no `CLAUDE.md`:** quando um erro se repete, ele vira uma linha explícita e
  enumerável no `CLAUDE.md` — e, por §6, o **Marvin passa a barrá-la no diff**. (Ex.: "nunca `any`"
  não é conselho, é lint + Marvin.)
- **Auto-doc (documentation-agent / typedoc):** a cada push na `main`, um agente regenera `docs/` e
  **abre um PR isolado** (nunca commita direto) — a doc segue o código sem trabalho manual. `[C]`
- **Promoção assistida (D63) + Guarda determinística (D30):** o HERMES promove contexto **seguro**
  para canônico só se o contrato dele conceder, e **todo lote passa por script determinístico** antes de
  contar como entregue. Sensível/contraditório escala para o João. `[C]` vault.
- **BrainHub como memória institucional:** o contexto refinado (este documento incluído) vira fonte
  que agentes "Por Área/Por Cliente/Por Solução" bebem — o cérebro que não reconstrói o que já sabe
  (regra D66 do `SISTEMAS.md`).

### 7.1 Diagrama — loop de retroalimentação

```mermaid
flowchart TB
    EVENT["📌 Evento real<br/>incidente · review · decisão do João"]
    DEC["DECISOES.md<br/>(registro-fonte, antes de executar)"]
    RULE["Regra vira EXPLÍCITA<br/>no CLAUDE.md / AGENTS.md"]
    GATE["⛔ Marvin passa a cobrar<br/>a regra no diff do PR"]
    CODE["Código passa a nascer conforme"]

    AUTODOC["📄 documentation-agent<br/>regenera docs/ → PR isolado"]
    HERMES["🔁 HERMES<br/>promoção assistida (D63)<br/>sob Guarda determinística (D30)"]
    BRAIN["🧠 BrainHub<br/>memória institucional<br/>(SISTEMAS.md · contexto por área)"]

    EVENT --> DEC --> RULE --> GATE --> CODE
    CODE -->|push na main| AUTODOC
    CODE --> HERMES
    AUTODOC --> HERMES
    HERMES -->|contexto seguro| BRAIN
    HERMES -->|sensível / contraditório| JOAO["👑 João aprova"]
    JOAO --> DEC
    BRAIN -.->|alimenta agentes e squads| EVENT
```

## §8 — Boas práticas do HyTrack/vault que agregam (e por quê)

Do mundo `HyTrackWater` (era Lovable + vault do João), o que **soma** à governança de produção:

- **Rito de admissão de agente/operador** (governança → contrato aprovado → **teste de obediência** →
  inbox → ritual): é o trilho para "criar mais operadores via BrainHub" sem afrouxar o padrão. `[C]`
- **Heartbeat (D62) + "exit 0 não é prova de trabalho" (D66):** nada entra em produção sem prova de
  vida vigiada; job que termina ≠ job que trabalhou. Aplica-se a todo cron/deploy do boilerplate. `[C]`
- **Hierarquia de verdade + `_CANON`/front-matter:** um dono por assunto; documento superado é marcado
  `SUPERSEDED` apontando o sucessor — evita "dois documentos vivos do mesmo tema". `[C]`
- **`SISTEMAS.md` (D66) — "não se constrói o que já existe":** catálogo consultado antes de criar
  pipeline/app. **Ação pendente:** trazer a produção `UmodeApp` para esse catálogo (hoje ele só tem os
  repos HyTrackWater). `[P]`
- **Os papéis-contrato e o glossário risolês** (`CLAUDE_OPERADOR.md`) — a linguagem e o modo de
  decidir do João, que não mudam por projeto.

## §8-bis — Plano de migração (sem big-bang — parecer 2026-09-02)

**P0 (agora, barato, destrava o essencial):**
1. **Tirar conteúdo interno do `public/` do Lovable** — a página de governança expõe o perfil do
   Operador num asset público atrás de gate só client-side (parecer **P0.1**). Classificar `INTERNAL`;
   auth server-side ou tirar do ar. **Decisão do João. É o item nº 1.**
2. **Construir o `ci.yml`** determinístico + branch protection real (infra → **Bergson**). Sem ele, o
   resto é decoração.
3. **Auditor Independente** (cadeira não-autor, exact-SHA) + o invariante "não-autor audita" — quem
   preenche a cadeira hoje é decisão João/Bergson.
4. **Ausência de lease = read-only** (regra de uma linha).
5. Etiquetar `ALVO`/`IMPLEMENTADO`/`ATIVO` em todo controle e corrigir os claims no presente (parecer
   A3, C1).

**P1:** topologia AGENTS-first (`AGENTS.md` único bootstrap, papéis em `governance/roles/`,
`context.manifest.yaml` com hashes) + adicionar `CONTEXT.md`/`STATE.md` ao conjunto-raiz (parecer C3);
branch lease YAML mínimo; evidence ledger append-only; CODEOWNERS por dimensão.

**P2:** artifact attestation/SBOM/build-once; state machines de staging/canário/drift/rollback; Marvin
com eval-set; matriz de Skills obrigatórias **só depois de verificar cada uma** (D66).

> Parecer completo: `parecer-smartcoding-esteira-2026-09-02.md`. Espelho visual (com os diagramas
> desta seção como SVG): projeto Lovable `governanca-squad-umode` — **INTERNAL**, pendente do P0.1.

## §9 — Governança deste documento

Autoridade de conteúdo: CEO (João Risoléo); decisões de execução (`[D]`) do João/Bergson. Alteração
aqui exige refazer a leitura das fontes. Companion técnico: `_contexto/_blueprint-boilerplate-governado.md`
(a espec do boilerplate, com procedência por commit+SHA dos 8 repositórios lidos).

### Conexões
`_contexto/_blueprint-boilerplate-governado.md` · `_recebido-2026-08-18-context-pack-brainhub-2.0.md` ·
`SISTEMAS.md` (vault) · `_GOVERNANCA.md` (vault) · `protocolo-gestao-integracao.md` ·
Playbook de Engenharia uMode (GitBook)
