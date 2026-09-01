# AGENTS.md — Programador

> Arquivo-raiz do boilerplate governado da uMode. Lido pelo executor de código em **toda sessão** — a
> esteira **HERMES**, ou uma pessoa usando **Codex** ou **Claude Code** direto. (O **Lovable saiu da
> stack de execução**.) Implementação sobre documentação. Companion: `.claude/*` e `.cursor/rules`
> carregam as mesmas regras no editor.

## Proibições estritas

- **NUNCA** rodar git (`add`/`commit`/`push`) sem pedido explícito.
- **NUNCA** criar `.md`/`.csv`/README/docs sem pedido explícito.
- **NUNCA** usar `any` — tipo específico ou `unknown`; `Array<T>`, nunca `T[]`.
- **NUNCA** `console.*` — usar o `logger`.
- **NUNCA** promise chaining (`.then/.catch/.finally`) nem `void fn()` — sempre `async/await` com `try/catch`.
- **NUNCA** omitir chaves em condicional/loop/arrow com corpo.
- **NUNCA** string visível hardcoded — tudo via `t('ns.key')`, chave em **pt E en**.
- **NUNCA** português no código; nome de rota/identificador em inglês.
- **NUNCA** `fetch` cru para backend — sempre `gatewayHttpClient`.
- **NUNCA** `setState` dentro de `useEffect`; `useEffect` é último recurso.
- **NUNCA** travessão (`—`) em texto visível ao usuário.

## Design system (obrigatório)

Fonte única: a **biblioteca publicada `@umodeapporg/ui`** — tokens claro/escuro, preset Tailwind,
componentes e `<UmodeLogo/>`; referência viva em `designsystem.umode.tech`.

- **Cânone travado `[D]`:** o padrão é `@umodeapporg/ui`. **NÃO usar shadcn/ui** — o boilerplate
  canônico (`UmodeApp/umode-frontend-boilerplate-nextjs`) não tem shadcn. Antes de escrever um
  componente, procurar na biblioteca; se já existe (`ControlledButton`, `DataTable`, `UnifiedSearchBar`…),
  usar, nunca reimplementar.
- **Nunca** hex/`rgb()`/paleta Tailwind crua — nomear o **papel** (`bg-surface`, `text-foreground`,
  `bg-danger-soft`). Plugue: `presets: [preset]` no `tailwind.config`, `import '@umodeapporg/ui/styles.css'`
  e `base.css` no entry.
- **Zustand** só para estado global, via `createStore`.

## Arquitetura

- **Back:** camadas estritas **Controller → Service → Repository → Database**; Repository é o único
  acesso ao banco; Cache-Aside com **TTL sempre**, chave `PROJECT:MODULE:ID`; envelope
  `{success, data, error, requestId}`.
- **Front:** **Server Components por padrão**, `'use client'` só quando preciso; HTTP só via
  `gatewayHttpClient`.
- **Auth:** login unificado uMode (Cognito via gateway) — o produto **não tem login próprio**;
  multi-tenant via `PartnerScopeGuard`.

## Definition of done

`eslint . --max-warnings 0` passa (literal de i18n é **erro** de lint; `no-any`, `no-portuguese`,
`no-literal-jsx` são regras próprias). Seguir o padrão existente — **não inventar padrão novo**.

## Regra anti-reversão

Ao editar arquivo de outro agente, o prompt lista as linhas a mudar e manda **preservar todo o resto**;
o CTO (`CLAUDE.md`) audita o diff.

---
_O executor nunca faz merge — abre PR. O PR passa pelos 3 gates (`ci.yml` + Marvin + security); ver
`HERMES.md`._
