# _boilerplate — Arquivos-raiz do boilerplate governado (encenados)

> Estes cinco arquivos são os **contratos de papel** que vão na **raiz do boilerplate de produção**.
> Eles vivem aqui, no `brainhub-umode`, porque **escrita direta no repo de produção da `UmodeApp` não
> é nossa** (é produção, só DEV trabalha lá). Isto é a versão encenada, pronta pra soltar na raiz por
> quem tiver acesso — a pendência de adoção (o PR no boilerplate) fica com o DEV.

## Os cinco arquivos (são um sistema, não avulsos)

| Arquivo | Papel | Vai na raiz de |
|---|---|---|
| `CLAUDE_OPERADOR.md` | Perfil do Operador (João/Vinícius/Pedro) — não muda por projeto | boilerplate |
| `CLAUDE_DIRETOR.md` | Diretor de Produto/Negócios (agente) | boilerplate |
| `CLAUDE.md` | CTO / Líder técnico (agente) — desenha e audita | boilerplate |
| `AGENTS.md` | Programador (HERMES · Codex · Claude Code) — regras de código | boilerplate (+ `.claude/*`, `.cursor/rules`) |
| `HERMES.md` | A esteira de produção `[P]` | boilerplate |

**Ordem de leitura em toda sessão:** `CLAUDE_OPERADOR` → `CLAUDE_DIRETOR` → `CLAUDE` → `AGENTS` →
`CONTEXT`/`docs` do projeto.

## Cânone travado `[D]`

O design system é a biblioteca publicada **`@umodeapporg/ui`** (preset Tailwind + Inter). O boilerplate
**canônico de front é `UmodeApp/umode-frontend-boilerplate-nextjs`, que NÃO usa shadcn/ui.** Decisão do
Vinicius (set/2026): o padrão é `@umodeapporg/ui`, não shadcn. `CLAUDE.md` e `AGENTS.md` já refletem isso.

## Como adotar (quem tem acesso ao repo de produção)

1. Copiar os cinco arquivos para a raiz do boilerplate.
2. Somar `.claude/*` e `.cursor/rules` espelhando o `AGENTS.md`.
3. Plugar `@umodeapporg/ui` (preset + `styles.css` + `base.css`) no `apps/web`.
4. Ligar os 3 gates (`ci.yml` + Marvin + security via `actions-shared`) como required checks.

## Fonte

Texto derivado de `_protocolos/treinamento-e-contratos-squad.md` (§2–§6) e
`_protocolos/contratos-agentes-por-dimensao.md`. Autoridade de conteúdo: CEO (João Risoléo).
