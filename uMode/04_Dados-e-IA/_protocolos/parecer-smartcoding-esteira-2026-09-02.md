# Parecer Claude — Revisão adversarial da esteira SmartCoding governada (2026-09-02)

> Revisão read-only do pacote do HERMES (PR #15 do `umode-os-vault`, branch
> `hermes/smartcoding-claude-review-2026-09-02`). Fonte primária: `SOURCE_GOVERNANCA_SQUAD.md`
> (537 linhas, citadas como `SRC:Lnn`). Propostas auditadas: `SMARTCODING_GOVERNED_PRODUCTION_REVIEW`
> (`REV §x`) e `HERMES_TRAINING_PROPOSAL` (`TRAIN §x`). Nada foi alterado nem promovido.
> Autoridade: fonte primária = direção do João; documentos do HERMES = propostas a auditar.

## Nota de método e de conflito de interesse

A fonte primária (`plano.html`) **fui eu quem construiu** nesta mesma linha de trabalho. Portanto este
parecer é, em parte, **auto-revisão** — exatamente o defeito que o HERMES aponta (`REV P0.3`). Registro
isso na abertura e recomendo que o parecer final passe por um **segundo revisor independente** (Bergson
ou um agente-auditor exact-SHA) antes de virar decisão. Não me dou o benefício da dúvida onde o HERMES
me pegou.

Verifiquei uma amostra das citações do HERMES contra a fonte: todas conferem. O pacote é **bem
fundamentado**; a maioria das críticas P0 é real. Onde diverjo, é por **excesso de máquina para o
estágio atual** (a esteira ainda não tem nem o `ci.yml` — `SRC:L528`), não por discordância de mérito.

---

# Veredito executivo

O documento-fonte é uma **constituição de PR forte** (identidade, papéis, 8 dimensões, determinístico-
antes-de-LLM, fail-closed, loop de aprendizado) e **ainda não é uma especificação de entrega até
produção**. O HERMES diagnostica isso corretamente: falta **autoridade por transição, identidade
imutável da release, state machine, evidência e recuperação**. Aceito o **diagnóstico central** e a
maioria das correções P0, com duas ressalvas de rigor:

1. **O maior risco não é falta de máquina — é máquina que não vai ser aplicada.** A esteira hoje não
   tem `ci.yml`, branch protection é `[P]` (`SRC:L205, L528`). Publicar uma state machine de 27 estados
   e um evidence ledger com SBOM/provenance **antes dos 3 gates existirem** reproduz o defeito que a
   própria constituição do vault critica: **controle decorativo** ("promoção sem índice não está
   promovida, está solta" — `_GOVERNANCA §3-bis`). Por isso **MODIFICO** boa parte das propostas de
   ALVO→já: aceito o **vocabulário** e o **alvo**, faseio o **enforcement**.
2. **Há uma falha P0 de segurança que é minha e é imediata:** a página que publiquei expõe o perfil do
   Operador (`SRC:L369–405`) num arquivo estático público atrás de um gate só client-side. Isso é `REV
   P0.1` e está **correto**. É a coisa mais urgente deste parecer — acima de qualquer state machine.

Frase central mantida (`SRC:L5`), com a emenda do HERMES aceita:
> Autonomia para criar, sem autonomia para ferir o protocolo — **toda autonomia é uma capability
> temporária; toda transição tem owner, identidade, evidência, falha e rollback.**

---

# 1. Contribuições do HERMES

## Aceitar como está

| # | Contribuição | Por quê | Citação |
|---|---|---|---|
| A1 | **Auditor Independente como papel** — quem escreve o head não audita o head | Quebra a auto-revisão do CTO, defeito real | `REV P0.3` × `SRC:L18,L35,L442` |
| A2 | **P0.1 — conteúdo interno fora de asset público**; gate client-side não é controle de acesso | Verdadeiro e crítico; expõe perfil do Operador | `REV P0.1` × `SRC:L369–405` |
| A3 | **ALVO / IMPLEMENTADO / ATIVO E VERIFICADO** em todo controle | É a nossa própria regra `[C]/[F]/[P]` aplicada com rigor; resolve a contradição "3 gates no presente × ci.yml não existe" | `REV P0.2, 6.1` × `SRC:L61,L528` |
| A4 | **Merge ≠ deploy ≠ runtime ≠ aceite** — separar os estados colapsados | `Merge → Deploy` num passo é subespecificação real | `REV P0.5` × `SRC:L84` |
| A5 | **Identidade imutável da release** (base/head/tree SHA; qualquer commit invalida gates) | "3× verde" não prova que review/CI/deploy são os mesmos bytes | `REV P0.6` × `SRC:L91,L285` |
| A6 | **Nomear os required checks** `ci-deterministic` / `policy-semantic` / `security`; editor e pré-commit são feedback, crédito de promoção zero | Desfaz a ambiguidade "3 camadas × 3 gates" | `REV P1.1` × `SRC:L262–287` |
| A7 | **Marvin é review semântica versionada, não determinismo**; temp 0 não é determinismo; publicar model/prompt/rules SHA + schema | Correto e alinhado à nossa própria regra "IA não valida em 1 rodada" | `REV P0.9,1.4` × `SRC:L281,L455` |
| A8 | **Learning record com destino explícito** (Memory/Skill/Vault/STATE) + supersession, não "editar MD" | Torna o loop `SRC:L289–308` operável e casa com o rito do vault | `REV 1.5` × `TRAIN §17,§20` |

## Aceitar com modificação

| # | Contribuição | Modificação que exijo | Citação |
|---|---|---|---|
| M1 | **State machine de 27 estados** (`REV §5`) | Aceitar como **vocabulário-alvo**. Implementar **agora** só o núcleo executável: `INTENT → READINESS → SCOPE/PLAN_APPROVED → BRANCH_LEASED → LOCAL_GREEN → INDEPENDENT_REVIEW → FULL_GATES → PR/CI_EXACT_SHA → MERGE_AUTHORIZED → DEPLOYED_STAGING → RUNTIME_READBACK → OWNER_ACCEPTED → LEARNING_PROMOTED`. Os estados de canário/SBOM/drift entram **marcados ALVO** até haver pipeline. Sem isso, é burocracia não-enforçável. | `REV §5` |
| M2 | **Topologia AGENTS-first** (`REV §4`, `TRAIN §2`): `AGENTS.md` único bootstrap auto-descoberto, `CLAUDE.md` vira adaptador, papéis em `governance/roles/`, `HERMES.md` fora da raiz, `context.manifest.yaml` com hashes | **Aceito o princípio** (o problema multi-vendor é real: Claude lê `CLAUDE.md`, Codex/Cursor leem `AGENTS.md`; `HERMES.md` na raiz pode mascarar `AGENTS.md`). **Modificação:** nosso `_boilerplate/` hoje tem `CLAUDE.md` + `AGENTS.md` na raiz (`SRC:L316–345`). Migrar para roles/ + manifest é **P1**, não P0 — e o `CLAUDE.md` adaptador tem que continuar carregando o essencial, porque hoje é o Claude que roda. | `REV §4` × `SRC:L316–368` |
| M3 | **Branch lease / capability** (`REV P0.8, 6.5`, `TRAIN §6`) | Aceito — fecha corrida multiagente. **Modificação:** manter o YAML **mínimo** (`repo, branch, write_set, expires_at, reviewer, merge_allowed:false`). Não exigir worktree/idempotency-key na v1 — é peso que uma squad de 3 não mantém. Ausência de lease = read-only: **isso sim** entra já. | `REV 6.5` × `TRAIN §6` |
| M4 | **Auditor Independente = 6º head humano** | **Modificação:** é uma **cadeira read-only exact-SHA**, preenchível por **um agente-auditor ou uma pessoa diferente do autor** — não headcount novo. Numa squad de 3, exigir um 6º humano trava a esteira. O invariante é "não-autor + exact-SHA", não "mais um humano". | `REV P0.3, 6.3` |
| M5 | **Evidence ledger / attestation com SBOM/provenance** (`REV P0.10, 6.2`, `TRAIN §10`) | Aceito o **ledger append-only** (base/head/tree, comando, resultado, limitação) — isso é barato e entra já. **SBOM/provenance/build-once-attested** ficam **P2 marcados ALVO**: exigir provenance antes de existir `ci.yml` é inverter a ordem de custo. | `REV P0.10` × `SRC:L528` |
| M6 | **Regras absolutas ganham escopo/exceção/escalada** (`REV P1.2`) | Aceito o princípio (toda regra: glob+enforcement+exceção+escalada). **Modificação:** não transformar cada invariante num formulário — basta uma convenção curta no topo do `AGENTS.md` + marcar as 3–4 regras que já têm exceção real (i18n pt/en é catálogo, não "português no código"; docs release-blocking acompanham o código). Excesso de metadado por regra é a burocracia que o próprio HERMES pede pra evitar. | `REV P1.2` × `SRC:L467,L256` |
| M7 | **CODEOWNERS por risco, Bergson não-universal** (`REV P1.3`) | Aceito. **Modificação:** hoje a fonte já diz "Bergson não é dono de execução por dimensão" (`SRC:L53`) mas o fluxo manda todo PR pra ele (`SRC:L497`) — contradição real. Corrigir: Bergson é `A` só em infra/governança/security estrutural; o resto tem CODEOWNERS por dimensão + Auditor. | `REV P1.3` × `SRC:L53,L497` |

## Rejeitar (ou rebaixar para depois)

| # | Contribuição | Por quê rejeito/adio | Citação |
|---|---|---|---|
| R1 | **Adotar a state machine e o evidence ledger completos como processo vigente agora** | Rejeito o "agora". Enforcement sem os 3 gates é decoração; a squad reproduz o defeito do heartbeat decorativo (`_GOVERNANCA §11-bis`). Vai como ALVO. | `REV §5,§6` |
| R2 | **Matriz de Skills obrigatórias por fase** (`TRAIN §7`) com ~25 skills (`governed-multi-agent-engineering`, `bh2-governed-delivery`, `governed-ci-causality`…) | Rejeito como **obrigatório** enquanto não verificado. Regra D66 do vault: **não se referencia o que não está catalogado**. Vários desses nomes não constam no `SISTEMAS`/`skills/` que li. Antes de tornar obrigatória, cada skill tem que existir e passar verificação real. | `TRAIN §7` × `_GOVERNANCA §13` |
| R3 | **Closeout ponderado / registry que soma 100 / weighted acceptance** (`TRAIN §5,§22`) | Adio para P2. É maquinário de campanha de marketing (peso por estado, planned×realized) que não tem lastro na esteira de código atual. Entra se e quando houver campanha ponderada; hoje é peso morto. | `TRAIN §5,§22` |

---

# 2. Falhas adicionais encontradas por Claude (não estavam no pacote do HERMES)

- **C1 — `[C]` mentido no Deploy.** A linha da dimensão Deploy é tag `[C]` (lido em produção) mas seu
  guardrail é `branch protection [P]` (`SRC:L106` vs `L205`). Pela nossa própria régua (`CLAUDE.md`:
  "existe ≠ vigente"), Deploy é no máximo `[F]`/`[P]`. Corrigir a etiqueta — senão o documento afirma
  vigência que não tem, que é o pecado do `REV P0.2`.
- **C2 — Marvin como gate bloqueante contradiz a nossa própria regra.** `SRC:L455` (contrato do CTO)
  diz **"IA não valida em 1 rodada só"**; `SRC:L280` põe o Marvin (uma passada de LLM) como gate que
  **bloqueia merge**. Ou o Marvin é **advisory**, ou precisa dos controles de determinismo do HERMES
  (model/prompt/rules SHA + schema + política de repetição). Não pode ser as duas coisas.
- **C3 — o loop referencia `STATE.md` e `CONTEXT.md` que não existem no conjunto de arquivos-raiz.**
  `SRC:L296` manda a sessão abrir lendo `CONTEXT · STATE · CLAUDE.md`, mas os 5 arquivos-raiz
  (`SRC:L316–345`) são OPERADOR/DIRETOR/CLAUDE/AGENTS/HERMES — **sem `CONTEXT.md`, sem `STATE.md`**.
  O loop aponta pra arquivos que o boilerplate não tem. Adicionar `docs/project/CONTEXT.md` +
  `STATE.md` (a topologia do HERMES em `REV §4` já resolve — mais uma razão para M2).
- **C4 — o rito termina em ator não-humano.** `SRC:L358`: a ronda final é "do CTO/HERMES". CTO é
  agente, HERMES é sistema. O rito do vault (`_GOVERNANCA §8–9`) termina em **ronda do João** (humano).
  Um rito cujo passo final de aceite é de um agente é auto-aprovação institucional. Terminar em
  **owner humano** (João/Bergson).
- **C5 — HERMES é papel-contrato E esteira ao mesmo tempo.** `SRC:L44` lista HERMES como um dos
  papéis-contrato; `SRC:L45,L481` diz que é a esteira (sistema). Isso é a raiz do `REV P0.3`
  (concentração): decidir de vez — **HERMES é sistema/mecanismo, nunca `A` no RACI**, e sai da lista de
  "papéis-contrato" (fica como sistema que aplica transições já autorizadas).
- **C6 — "vibecoda/vibecoding" e a marca.** `SRC:L18,L23,L61` usam "vibecoda/vibecoding". Pela
  `identidade-verbal.md` do vault, o **método autoral é SmartCoding, nunca "Vibe Coding"** — "Vibe
  Coding" só como fenômeno de mercado. Aqui está como contraste ("vibecoding no Lovable"), o que é
  tolerado, mas o **método da squad deve ser nomeado SmartCoding** no documento, senão a peça oficial
  de produção contradiz o canon de marca.

---

# 3. RACI final recomendado

Adoto o do HERMES (`REV §3`) com os ajustes M4/M7. **HERMES nunca é `A`.** O Auditor é cadeira
read-only não-autor (M4).

| Atividade | Operador | Diretor | CTO(agente) | Programador | Auditor | HERMES(sistema) | Bergson/Infra |
|---|---|---|---|---|---|---|---|
| Problema / prioridade / aceite | **A** | R | C | I | I | I | I |
| PRD / briefing / critério de aceite | A | **R** | C | I | I | I | I |
| Desenho não-infra | C | C | **A/R** | C | I | I | I |
| Infra / IAM / rede / auth / pipeline | C | C | R | I | C | I | **A** |
| Implementação (código, testes) | I | I | C | **A/R** | I | suporte | C |
| Auditoria exact-SHA | I | I | C | I | **A/R** | evidência | C |
| Merge autorizado | I | I | I | I | parecer | executor | **A** só se infra |
| Deploy staging/prod | I | I | C | evidência | parecer | executor | A conforme ambiente |
| Aceite funcional | **A** | R | C | I | I | registra | I |
| Rollback | I | I | C | I | I | executor | **A** conforme ambiente |

Invariante: **quem escreveu o head não emite o parecer desse head** (mata a auto-revisão do CTO).

---

# 4. State machine final recomendada (núcleo vigente + alvo)

**Vigente já (implementável sem pipeline novo, só disciplina + branch protection):**
```text
INTENT_RECORDED → READINESS_PASS → SCOPE_APPROVED → TECH_PLAN_APPROVED
→ BRANCH_LEASED → RED_OBSERVED → LOCAL_GREEN → INDEPENDENT_REVIEW_PASS
→ FULL_GATES_PASS(ci-deterministic, policy-semantic, security @ mesmo head)
→ PR_CI_PASS_EXACT_SHA → MERGE_AUTHORIZED → DEPLOYED_STAGING
→ RUNTIME_READBACK_PASS → OWNER_ACCEPTED → LEARNING_PROMOTED → CLOSED
```
**Alvo (marcar ALVO até haver pipeline):** `RELEASE_CANDIDATE_ATTESTED` (digest/SBOM), `PREDEPLOY_DRIFT_PASS`,
`PROD_CANARY_PASS`, `PROD_EXPANDED`, `ROLLBACK_PROVEN`.

**Laterais (entram já, são baratos):** `READINESS_BLOCKED`, `CHANGE_REQUIRED`, `CI_RED`,
`WAITING_CAUSAL_EVIDENCE`, `BLOCKED_DRIFT`, `EVIDENCE_UNKNOWN`, `ROLLED_BACK`, `INCIDENT_OPEN`,
`SUPERSEDED`, `DECLINED`.

Regra: **nenhum estado implica o próximo automaticamente** (aceito de `TRAIN §8`).

---

# 5. Topologia final dos MDs (aceita com faseamento — M2)

```text
<repo>/
├── AGENTS.md                    # ÚNICO bootstrap auto-descoberto (vendor-neutral)
├── CLAUDE.md                    # adaptador: aponta pra AGENTS + carrega o essencial p/ Claude
├── governance/
│   ├── context.manifest.yaml    # lista docs, versões, hashes  [P1]
│   ├── roles/{OPERADOR,DIRETOR_PRODUTO,CTO,PROGRAMADOR,AUDITOR,HERMES}.md
│   ├── HERMES_TRAINING.md        # apontado por AGENTS, não por HERMES.md raiz
│   ├── DELEGATION_LEASE.template.md
│   └── decisions/
└── docs/project/{CONTEXT.md, STATE.md}   # resolve C3
```
Ordem real de leitura: runtime carrega `AGENTS.md` → valida manifesto → identifica papel+lease (sem
ambos = read-only) → lê 1 contrato de papel → CONTEXT+STATE → Issue/PRD/ADR/lease. **Regra local só
restringe, nunca revoga a raiz.** Hoje temos CLAUDE+AGENTS na raiz (`SRC:L316–345`); a migração para
`roles/`+manifest é **P1**.

---

# 6. Revisão do `HERMES_TRAINING.md`

**Decisão estrutural (aceita):** é **contrato persistente**, não diário de campanha; canônico em
`_protocolos/HERMES_TRAINING.md`; apontado por `AGENTS.md`; outcomes em learning records append-only;
só lição validada promove Memory/Skill/policy (`TRAIN §8 recomendado do REV`).

- **Remover / adiar:** matriz de Skills obrigatórias enquanto não verificadas (R2, `TRAIN §7`); closeout
  ponderado e registry-soma-100 (R3, `TRAIN §5,§22`) → P2; qualquer menção a status corrente.
- **Adicionar:** a marcação **ALVO/IMPLEMENTADO/ATIVO** por invariante (A3); o vínculo explícito com o
  `_GOVERNANCA` do vault (rito de admissão §8, Guarda §8, heartbeat §11 já existem lá — **não duplicar**,
  apontar); o destino de learning batendo com a **retention matrix** (`TRAIN §19`) — que é excelente e
  fica.
- **Reescrever:** §2 "como carregar" para casar com o nosso `_boilerplate/` real (CLAUDE+AGENTS na raiz
  hoje), não com a topologia-alvo, senão o contrato descreve um repo que ainda não existe.

O `HERMES_TRAINING.md` **não** vira `HERMES.md` da raiz (M2/C5) e **não** repete o que o `_GOVERNANCA`
do vault já governa (evitar "dois documentos vivos" — nossa própria regra `SRC:L256`).

---

# 7. Texto exato para inserir na Governança da Squad

Aceito os blocos `REV §6.1–6.8` como base, com estas versões enxutas (sem o maquinário P2):

**STATUS OPERACIONAL** — "Cada controle é ALVO (desenhado, sem enforcement), IMPLEMENTADO (código/config
existe) ou ATIVO E VERIFICADO (required no repo/ambiente, lido de volta com evidência e data). Diagrama
ou check local não é enforcement. Este documento nunca descreve no presente um gate em ALVO." → corrige
`SRC:L61,L528` e o C1.

**AUTORIDADE POR TRANSIÇÃO** — o RACI da seção 3 em prosa; "quem escreveu o head não audita o head;
aprovar PR, migration, merge e promoção são ações diferentes."

**CONTRATO DOS GATES** — required checks `ci-deterministic`, `policy-semantic`, `security` no mesmo head;
editor/pré-commit são feedback; Marvin registra model/prompt/rules SHA + schema (resolve C2); timeout/
output inválido/ausência bloqueiam; **proibido rerodar até passar**.

**SENSIBILIDADE** — todo MD/deck declara `PUBLIC | INTERNAL | CONFIDENTIAL`; perfil do Operador,
contratos internos, credenciais e infra **nunca** em `public/` nem atrás de gate client-side; a fonte
canônica é o Markdown versionado, o HTML é artefato gerado com digest/backlink. → é a correção do P0.1.

---

# 8. Plano de migração (sem big-bang)

**P0 (agora, barato, destrava o essencial):**
1. **Tirar conteúdo interno do `public/` do Lovable** (P0.1/A2) — o `plano.html` e `designsystem.html`
   expõem o perfil do João. Ação imediata: classificar como INTERNAL, mover para rota server-protected
   ou tirar do ar até haver auth server-side. **Isto é o item nº 1 de tudo.**
2. Etiquetar **ALVO/IMPLEMENTADO/ATIVO** e corrigir os claims no presente (A3, C1).
3. **Construir o `ci.yml`** determinístico + branch protection real (fecha a lacuna #3 do próprio doc,
   `SRC:L528`). Sem ele, o resto é decoração.
4. Introduzir **Auditor Independente** (cadeira read-only não-autor, M4) e o invariante "não-autor
   audita".
5. **Ausência de lease = read-only** (M3) — regra de uma linha, entra já.

**P1:** topologia AGENTS-first + `roles/` + `context.manifest.yaml` (M2, C3); branch lease YAML mínimo;
evidence ledger append-only (M5 parte barata); CODEOWNERS por dimensão (M7); separar merge/deploy/
runtime/aceite como estados (A4).

**P2:** artifact attestation/SBOM/build-once; staging/canário/drift/rollback state machines; Marvin
versionado com eval-set; matriz de Skills (só depois de verificar cada uma, R2); weighted acceptance
(R3, se houver campanha).

---

# 9. Riscos residuais e decisões do João / Bergson

- **[D-João] Superfície pública do Lovable.** Manter o doc no Lovable exige auth server-side (Lovable
  Cloud/Supabase) ou tirar o conteúdo interno do ar. Decisão de arquitetura de acesso. *(Bloqueia: é o
  P0.1.)*
- **[D-Bergson] `ci.yml` e branch protection** nos repos de produção UmodeApp — quem escreve, onde,
  quando. É o gate que falta; é infra, logo é do Bergson (`A`).
- **[D-João/Bergson] Quem preenche a cadeira de Auditor Independente** hoje (agente-auditor? Bergson em
  PRs não-dele? Claude Approvals?). Sem alguém não-autor, a segregação continua no papel.
- **[D-Bergson] CODEOWNERS por dimensão** — o mapa risco→dono que substitui o Bergson-universal.
- **[D-João] Escopo do `HERMES_TRAINING.md`** — o que é contrato persistente vs. o que fica em Skill/
  STATE. E se o HERMES do vault ganha a permissão §3-bis para promover (hoje não tem).
- **[decisão de marca] SmartCoding × vibecoding** no texto oficial (C6) — alinhar com `identidade-verbal`.

## Respostas às 14 perguntas obrigatórias (resumo)

1. **Segregação evita autoaprovação?** Não hoje: o CTO desenha+audita+implementa (`SRC:L35,L442`). Fecha com o Auditor Independente (A1).
2. **HERMES = sistema, nunca `A`?** Sim — e sai da lista de papéis-contrato (C5).
3. **`AGENTS.md` único bootstrap?** Sim (M2), com `CLAUDE.md` adaptador; migração P1.
4. **State machine tem estados demais/de menos?** Demais para o estágio: núcleo vigente + resto ALVO (M1).
5. **Que transições exigem humano/CI/auditor/runtime/rollback?** Aceite e promoção-prod = humano; gates = CI; parecer = Auditor; readback = runtime; rollback = incident owner (RACI seção 3).
6. **Lease fecha corridas sem burocracia?** Sim, com o YAML mínimo (M3).
7. **Marvin = review semântica versionada?** Sim (A7) — e resolve a contradição C2.
8. **Evidence ledger suficiente p/ exact-SHA/digest/deploy/readback?** O ledger append-only sim (já); SBOM/attestation é P2 (M5).
9. **Readiness evita confundir técnico com entrada em campo?** Sim (READINESS_PASS antes do relógio, `TRAIN §5`) — aceito.
10. **`HERMES_TRAINING` separa Memory/Skill/Vault/STATE?** Sim, e bem (`TRAIN §19`); remover o que duplica o vault (seção 6).
11. **Que regras ficam stale/caras?** Skills obrigatórias não-verificadas (R2), closeout ponderado (R3), regras absolutas sem escopo (M6).
12. **O que entra agora / depois / rejeitar?** Seção 1 (tabelas) + seção 8 (P0/P1/P2).
13. **Lovable expõe material interno?** Sim (P0.1) — fonte canônica é o Markdown versionado; HTML é artefato; interno exige auth server-side.
14. **Como migrar sem big-bang?** Seção 8.

## Conexões
`governanca-squad-desenvolvimento.md` · `treinamento-e-contratos-squad.md` ·
`contratos-agentes-por-dimensao.md` · `_contexto/_blueprint-boilerplate-governado.md` ·
pacote HERMES: `umode-os-vault` PR #15 (`inbox/hermes/smartcoding-claude-review-2026-09-02/`)
