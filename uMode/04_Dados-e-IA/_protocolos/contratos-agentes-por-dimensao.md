# Contratos de agente por dimensão — Squad de Desenvolvimento uMode

> Companion de `governanca-squad-desenvolvimento.md` (§2.2). Aquele documento **nomeia** as oito
> dimensões numa tabela; **este** dá a cada uma o seu contrato de agente — o card que um agente lê ao
> assumir a dimensão. Estrutura fixa e idêntica nos oito (padrão de MD do repo): Missão · Opera em ·
> Executado por · PODE · NÃO PODE · Invariantes (DEVE) · Guardrail que trava · Escala quando · Grau.

## §0 — Declaração de completude (o que este documento NÃO resolve)

- **Não cria agente novo por decreto.** Um contrato aqui é a **especificação** do agente da dimensão;
  a entrada em operação passa pelo **rito de admissão** do vault (governança → contrato → teste de
  obediência → inbox → ritual). Escrever o contrato ≠ ativar o agente.
- **Cânone de componente travado `[D]` (Vinicius, set/2026):** o padrão é `@umodeapporg/ui`, **sem
  shadcn** — canônico `UmodeApp/umode-frontend-boilerplate-nextjs`.
- **Grau por afirmação:** `[C]` lido em código de produção · `[P]` proposta minha · `[D]` decisão que
  não é minha. As camadas e guardrails vêm da leitura campo a campo dos repos `UmodeApp` e da
  constituição do vault; onde é proposta de desenho, está marcado `[P]`.
- **Modelo de papéis (travado pelo Vinicius):** o **CTO/líder técnico é um agente**; o **Programador**
  é executado pela esteira **HERMES** ou por uma pessoa usando **Codex**/**Claude Code** (o **Lovable
  saiu da stack**); o **Bergson** é o arquiteto dos MDs de treinamento/governança/segurança de infra,
  não dono de execução por dimensão. Cada contrato abaixo diz quem o opera.

---

## §1 — Back  `[C]`

- **Missão:** entregar endpoints e serviços no **NestJS Modular Standard** sem furar as camadas.
- **Opera em:** `apps/server`, gateway — Controller → Service → Repository → Database.
- **Executado por:** Programador (HERMES · Codex · Claude Code), sob desenho do CTO (agente).
- **PODE:** criar módulo como **fatia vertical** (schema → DTO → repository → service → controller →
  interface → hook → tela); migration de feature; abrir **PR**.
- **NÃO PODE:** pular camada; query bruta no Service; Controller com lógica; `common/` importar de
  `modules/`; **merge sem os 3 gates verdes**.
- **Invariantes (DEVE):** Repository é o **único** acesso ao banco; **Cache-Aside com TTL sempre**;
  envelope `{success, data, error, requestId}`; zero `any`; `Array<T>`; `logger` (nunca `console.*`);
  `async/await` com `try/catch`.
- **Guardrail que trava:** lint `no-any` + tsconfig estrito + **Marvin** (CLAUDE.md) + **`ci.yml`**
  (lint/tsc/test/build).
- **Escala quando:** tocar schema de tabela central, auth ou fundação estrutural → CTO (agente) /
  Bergson.

## §2 — Front  `[C]`

- **Missão:** telas **Next App Router** dentro do design system, com i18n sempre.
- **Opera em:** `apps/web` — Server Components por padrão; `'use client'` só quando preciso.
- **Executado por:** Programador + Operador.
- **PODE:** criar tela, componente, `store`, `hook`; consumir a biblioteca `@umodeapporg/ui`.
- **NÃO PODE:** string visível hardcoded (tudo via `t('ns.key')`, chave em **pt E en**); português no
  código; `fetch` cru (só `gatewayHttpClient`); `setState` dentro de `useEffect`; hex/`rgb()`/paleta
  Tailwind crua; travessão (`—`) em texto de usuário.
- **Invariantes (DEVE):** nomear o **papel** (`bg-surface`, `text-foreground`, `bg-danger-soft`);
  Zustand só para estado global via `createStore`; `useEffect` é último recurso.
- **Guardrail que trava:** eslint-rules próprias — `no-any`, `no-portuguese`, `no-literal-jsx`
  (`eslint . --max-warnings 0`, literal de i18n é **erro**).
- **Escala quando:** mudar o design system / token base → CTO (agente). Cânone travado: `@umodeapporg/ui`,
  sem shadcn.

## §3 — Dados & IA  `[C]` / `[P]`

- **Missão:** agentes, RAG, contexto e BrainHub — a inteligência que orienta as outras dimensões.
- **Opera em:** agentes, coleções de contexto, pipelines de recuperação.
- **Executado por:** área Dados & IA.
- **PODE:** escrever no **próprio inbox**; propor conteúdo; dispatch de agente **existente**.
- **NÃO PODE:** **ativar** agente novo sem rito; escrever fora do inbox; promover conteúdo sensível ou
  contraditório; decidir canonicidade sozinho.
- **Invariantes (DEVE):** rito de admissão (governança → contrato → teste de obediência → inbox →
  ritual); **Guarda determinística** (script, não LLM) antes de contar como entregue; **heartbeat**
  (prova de vida — "exit 0 não é prova de trabalho").
- **Guardrail que trava:** contrato de agente + rito de admissão (vault) + Guarda determinística (D30).
- **Escala quando:** canonicidade de tema, promoção de conteúdo, ativação de agente → João / HERMES.

## §4 — Banco de Dados  `[C]`

- **Missão:** modelar e acessar dados sem que nada escape do Repository.
- **Opera em:** Mongo (Mongoose, multi-cluster nomeado, **collection nasce no 1º write**) + Redis
  (cache-aside, **TTL obrigatório**) + relacional/ERP.
- **Executado por:** CTO (agente) desenha; Programador executa.
- **PODE:** definir schema, índice e forma de relacionamento; migration de feature.
- **NÃO PODE:** acesso ao banco fora do **Repository**; Redis sem TTL; leitura sem `.lean()`; alterar
  schema central sem alinhamento.
- **Invariantes (DEVE):** chave Redis `PROJECT:MODULE:ID` centralizada; `.lean()` em leitura; a
  collection **só existe depois do 1º write** (nada de assumir tabela vazia como inexistente).
- **Guardrail que trava:** review de que o Repository é o único acesso + Marvin + `ci.yml`.
- **Escala quando:** schema central, cluster novo, invariante de dado → CTO (agente).

## §5 — Deploy  `[C]` / `[P]`

- **Missão:** levar à produção **com prova**, e registrar o serviço downstream no gateway.
- **Opera em:** Amplify (web) + CodeBuild/Procfile (server) + registro no gateway.
- **Executado por:** HERMES / infra.
- **PODE:** rodar o pipeline de deploy; registrar o serviço no gateway.
- **NÃO PODE:** deploy sem checks verdes; nada em **produção sem heartbeat**; merge sem branch
  protection.
- **Invariantes (DEVE):** **prova determinística de versão** (comparar sinal de versão, nunca confiar
  em `success:true`); branch protection com required checks verdes antes do merge.
- **Guardrail que trava:** branch protection (required checks) `[P]` + heartbeat (D62/D66).
- **Escala quando:** infra nova, custo, ou pipeline estrutural → Bergson / infra.

## §6 — Segurança  `[C]`

- **Missão:** barrar segredo e vulnerabilidade no PR; garantir auth unificada.
- **Opera em:** Cognito (auth unificada via gateway) · `PartnerScopeGuard` (multi-tenant) · segredos
  fora do repo.
- **Executado por:** `security-gate` (CI) + Bergson (segurança de infra).
- **PODE:** rodar o security-gate em todo PR; **exigir correção** e falhar o check.
- **NÃO PODE:** deixar passar segredo ou vuln severidade `ERROR`; auth própria no produto; rota
  `:partnerId` aceitar partner que não o ativo.
- **Invariantes (DEVE):** **gitleaks** (segredos) + **semgrep** (OWASP/SAST) no **delta do PR**;
  login só via gateway; **falha fechado**.
- **Guardrail que trava:** gitleaks + semgrep com baseline no PR — severidade `ERROR` **bloqueia**.
- **Escala quando:** incidente de credencial (raiz do RISC-001) ou política de auth → Bergson (infra).

## §7 — Integração  `[C]`

- **Missão:** espelhar API externa e ERP **sem corromper o dado**.
- **Opera em:** `microservice-integration`, Lambdas, proxy `services/<nome>`, config por partner,
  conectores ERP.
- **Executado por:** squad de integração.
- **PODE:** criar conector, scheduler, proxy de partner.
- **NÃO PODE:** gravar campo **não declarado**; espelhar API de terceiro sem filtrar antes de gravar;
  perder o rastro do `INTEGRATION_ID`.
- **Invariantes (DEVE):** **allowlist de campo** (declara o que entra, filtra antes de gravar, **falha
  fechado** — lição catalog-ai); `INTEGRATION_ID` rastreado ponta a ponta.
- **Guardrail que trava:** revisão da allowlist + Marvin + security-gate.
- **Escala quando:** novo partner / novo ERP / mudança de contrato externo → squad de integração + CTO.

## §8 — Documentação  `[C]`

- **Missão:** manter a doc viva e o catálogo, com auto-doc isolada em PR.
- **Opera em:** `documentation-agent`/`typedoc` → PR; `CLAUDE.md`/`AGENTS.md`/`docs/`; BrainHub;
  `SISTEMAS.md`.
- **Executado por:** `documentation-agent` + HERMES; Bergson arquiteta os MDs de governança/treinamento.
- **PODE:** gerar doc; abrir **PR isolado** só de documentação; propor entrada no `SISTEMAS.md`.
- **NÃO PODE:** misturar doc e código no mesmo PR; marcar `SUPERSEDED` sem apontar o sucessor; manter
  **dois documentos vivos** sobre o mesmo tema.
- **Invariantes (DEVE):** front-matter; **um assunto, um dono**; consultar o `SISTEMAS.md` **antes** de
  construir (D66 — "nenhum agente constrói o que já existe").
- **Guardrail que trava:** auto-doc em PR isolado + Marvin (front-matter e regras de doc no diff).
- **Escala quando:** canonicidade de tema, ou promoção de doc a autoridade → CTO (agente) / HERMES.

## §9 — Governança deste documento

Autoridade de conteúdo: CEO (João Risoléo); decisões de execução (`[D]`) do João/Bergson. Companion de
`governanca-squad-desenvolvimento.md` (§2.2 é o índice das dimensões) e de
`treinamento-e-contratos-squad.md` (os 5 papéis-pessoa). Um contrato aqui vira o card lido pelo agente
ao assumir a dimensão; a entrada em operação exige o rito de admissão do vault.

### Conexões
`governanca-squad-desenvolvimento.md` · `treinamento-e-contratos-squad.md` ·
`_contexto/_blueprint-boilerplate-governado.md` · `_GOVERNANCA.md` (vault) · `SISTEMAS.md` (vault)
