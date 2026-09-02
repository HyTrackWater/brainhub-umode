# _boilerplate — Arquivos-raiz do boilerplate governado (encenados)

> Estes são os **contratos de papel** que vão na raiz do boilerplate de produção. Vivem aqui, no
> `brainhub-umode`, porque **escrita direta no repo de produção da `UmodeApp` não é nossa**.
>
> **`PENDING_MIGRATION` (parecer 2026-09-02):** este conjunto está **em transição** para a topologia
> **AGENTS-first** — **não** "prontos pra soltar" como estavam. As contradições de papel (CTO
> auto-audita, PRD×ADR, HERMES-merge) **já foram corrigidas**; a **migração de pastas** (papéis para
> `governance/roles/`, `CLAUDE.md` adaptador, `HERMES.md` fora da raiz, `context.manifest.yaml`,
> `CONTEXT.md`/`STATE.md`) é **P1**, ainda não feita.

## Os arquivos (um sistema, não avulsos)

| Arquivo | Papel | Estado |
|---|---|---|
| `CLAUDE_OPERADOR.md` | Perfil do Operador (João/Vinícius/Pedro) — não muda por projeto | ok |
| `CLAUDE_DIRETOR.md` | Diretor de Produto — PRD/briefing/aceite (ADR técnico é do CTO) | corrigido |
| `CLAUDE.md` | CTO / Líder técnico (agente) — desenha; **não** audita o próprio head | corrigido |
| `AUDITOR.md` | **Auditor Independente** — parecer exact-SHA, cadeira não-autor | **novo** |
| `AGENTS.md` | Programador (HERMES · Codex · Claude Code) — único bootstrap na topologia-alvo | corrigido |
| `HERMES_TRAINING.md` | Contrato persistente da esteira (substitui o `HERMES.md` da raiz) | **novo** |
| `HERMES.md` | Resumo da esteira `[P]` — sai da raiz na migração P1 | pending |

**Ordem de leitura (topologia-alvo):** `AGENTS.md` (bootstrap) → papel (`governance/roles/*`) →
`CONTEXT.md`/`STATE.md` → Issue/PRD/ADR/lease. Hoje (transição): `CLAUDE_OPERADOR` → `CLAUDE_DIRETOR` →
`CLAUDE` → `AGENTS` → `CONTEXT`/`docs`.

## Cânone travado `[D]`

O design system é a biblioteca publicada **`@umodeapporg/ui`** (preset Tailwind + Inter). O boilerplate
**canônico de front é `UmodeApp/umode-frontend-boilerplate-nextjs`, que NÃO usa shadcn/ui.** Decisão do
Vinicius (set/2026): o padrão é `@umodeapporg/ui`, não shadcn. `CLAUDE.md` e `AGENTS.md` já refletem isso.

## Como adotar (quem tem acesso ao repo de produção)

> **Não copiar o conjunto antigo como está.** A adoção acontece **junto** da migração para a topologia
> AGENTS-first (P1) — copiar hoje os arquivos como pré-migração fixaria a estrutura errada.

1. **Migrar para a topologia-alvo** (P1): `AGENTS.md` único bootstrap; papéis (incl. `AUDITOR.md`) em
   `governance/roles/`; `CLAUDE.md` adaptador; `HERMES_TRAINING.md` no lugar do `HERMES.md` de raiz;
   `context.manifest.yaml` + `CONTEXT.md`/`STATE.md`.
2. Somar `.claude/*` e `.cursor/rules` espelhando o `AGENTS.md`.
3. Plugar `@umodeapporg/ui` (preset + `styles.css` + `base.css`) no `apps/web`.
4. Ligar os 3 required checks (`ci-deterministic` + `policy-semantic`/Marvin + `security`) + branch
   protection. Enquanto a migração P1 não fecha, estes arquivos são **referência corrigida**, não drop-in.

## Fonte

Texto derivado de `_protocolos/treinamento-e-contratos-squad.md` (§2–§6) e
`_protocolos/contratos-agentes-por-dimensao.md`. Autoridade de conteúdo: CEO (João Risoléo).
