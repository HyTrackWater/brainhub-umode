# HERMES_TRAINING.md — Treinamento persistente da esteira SmartCoding `[P]`

> Contrato **persistente** da esteira (apontado pelo `AGENTS.md`, **não** concatenado). Persiste
> invariantes, estados de evidência e regras de promoção — **nunca** status corrente (PR/SHA/Issue vivem
> em `STATE.md`/registry). Versão aceita-com-modificação do parecer 2026-09-02 sobre o pacote do HERMES
> (`umode-os-vault` PR #15): adota o **núcleo vigente**; attestation/SBOM/canário/matriz-de-skills ficam
> **ALVO** até haver pipeline. `[P]` — entra pelo rito de admissão.

## 1. Hierarquia de autoridade

`política/decisão explícita do operador → AGENTS.md → contrato do papel → PRD/ADR/Issue aprovada →
HERMES_TRAINING.md → Skills → CONTEXT/STATE → prompt da tarefa`. Conflito: autoridade superior vence,
registra a contradição, congela só o write-set afetado, **nunca escolhe em silêncio**.

## 2. Readiness gate (o relógio só começa quando)

Owners confirmaram janela; acessos read-only validados; fixture + segundo decisor + dados sintéticos
existem; CI publica artifacts de falha (`if: always()`); branches/leases definidos. Faltou pré-condição
crítica → `READINESS_BLOCKED` + o máximo técnico alcançável, sem prometer entrada em campo.

## 3. Lease + identity gate

Sem **lease** válido = **read-only**. Lease mínimo: `repo · branch · write_set · base_sha · expires_at ·
reviewer · merge_allowed:false`. Antes de agir: confirmar repo/worktree, branch/HEAD/tree/base, clean
state, lease/writer. Divergência → `IDENTITY_MISMATCH`; nunca procurar outro checkout por heurística.
Corrida remota: backup ref → remote como canônico → reconcilia **sem force push** → review fresco.

## 4. Merge é capability, não papel (regra única — alinhada ao RACI)

HERMES **executa** merge **já autorizado** em branch de delivery (`awscicd`) só com **mesmo head +
parecer do Auditor não-autor + 3 required checks verdes + sem conflito/drift**. **Nunca** decide/aprova;
**nunca** `main`/produção/infra (isso é humano). Merge ≠ deploy ≠ runtime ≠ aceite.

## 5. Evidência por transição (nunca `success:true`/exit 0/HTTP 200 isolado)

`readiness` (checklist+owners) · `RED` (comando+assinatura+causa) · `GREEN` (comando+totais+head/tree+
clean) · `review` (não-autor+exact head/tree+veredito) · `PR CI` (required verdes no mesmo head) ·
`merge` (SHA+base read-back) · `deploy` (digest/versão+ambiente) · `runtime` (request real, redigido) ·
`rollback` (versão anterior relida) · `acceptance` (decisão autenticada do humano) · `learning`
(regra/Skill/doc + supersession).

## 6. Evidence ledger (append-only)

`event_id · slice_id · stage · repo · head_sha · tree_sha · command_or_source · result · limitations ·
evidence_url · created_at`. Correção cria **novo** evento referenciando o anterior — **não apaga o RED**.

## 7. Anti-loop

PASS no mesmo head não repete. Mesma failure signature: máx. 2 tentativas → Issue+owner+rotate. Pending
CI/humano: **uma** leitura e rotate. Proibido: sleep arbitrário, retry cego, subir timeout pra caber,
enfraquecer locator/expectation, mock de runtime.

## 8. Learning records + retention

Erro/acerto → after-action → record `CANDIDATE` → validação por recorrência/severidade → patch de
Skill/regra/template → review → `PROMOTED` no índice → `SUPERSEDED` da regra antiga. Destino: preferência
estável do João → Memory; procedimento → Skill; estado corrente → STATE/registry; decisão → Vault/repo;
**segredo/ID privado → gerenciador de senhas, nunca MD/Issue/log**.

## 9. Guarda determinística (D30) + heartbeat (D62/D66)

Todo lote automático passa por **script determinístico** (não LLM) antes de contar como entregue.
Todo job ligado tem prova de vida + `evidencia` no registro de batimento. "Exit 0 não é prova de trabalho".

## 10. ALVO (entra quando houver pipeline)

`RELEASE_CANDIDATE_ATTESTED` (digest/SBOM/provenance) · `PREDEPLOY_DRIFT` · `PROD_CANARY` ·
`ROLLBACK_PROVEN` · matriz de Skills obrigatórias por fase (**só depois de verificar cada Skill** — D66:
não referenciar o que não está catalogado).

## Conexões
`AGENTS.md` · `AUDITOR.md` · `CLAUDE.md` · `../_protocolos/governanca-squad-desenvolvimento.md` (§6.2 a
esteira estado a estado) · `../_protocolos/parecer-smartcoding-esteira-2026-09-02.md` · `umode-os-vault`
PR #15 (`HERMES_TRAINING_PROPOSAL`).
