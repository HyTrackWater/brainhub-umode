# Proposta de promoção ao vault — Governança da Squad (SmartCoding)

> **Escrita no vault não é minha** (`CLAUDE.md`: escrita só no `brainhub-umode`; vault é read-only).
> Este arquivo é o **pacote-proposta** com blocos prontos pra colar. Quem aplica: **João / HERMES**
> (promoção assistida D63). Emenda ao `_GOVERNANCA.md` é **exclusiva do João** (§10 — "nunca por
> iniciativa de agente"). Fonte canônica dos docs = repo vivo `brainhub-umode@<commit>` (§5): o vault
> **aponta**, não copia (evita "dois documentos vivos").

## 1. `_GOVERNANCA.md` — SÓ o João emenda (§10). Proposta de emenda:

Registrar, se o João concordar, na tabela §8 e/ou como decisão datada:
- **Lovable saiu da stack de execução** de código (era "escreve nos repos de produto"); executores hoje =
  HERMES · Codex · Claude Code.
- **HERMES ganha (ou não) a permissão §3-bis** para promover contexto seguro dos repos de código — hoje o
  `HERMES.md` do vault concede só para o vault; estender exige decisão do João.
- Apontar o corpus da squad: `brainhub-umode/uMode/04_Dados-e-IA/_protocolos/` + `_boilerplate/`.

## 2. `CATALOGO.md` — adicionar (promoção assistida pode, com índice na mesma ação):

```
### Governança da Squad de Desenvolvimento (SmartCoding)  [origem: brainhub-umode repo vivo]
- governanca-squad-desenvolvimento.md — a constituição da esteira (papéis, RACI, 8 dimensões, gates, state machine)
- treinamento-e-contratos-squad.md — os 5 contratos de papel (íntegra)
- contratos-agentes-por-dimensao.md — os 8 contratos de agente
- _blueprint-boilerplate-governado.md — a espec do boilerplate governado
- _boilerplate/ — os 5 arquivos-raiz (CLAUDE_OPERADOR/DIRETOR/CLAUDE/AGENTS/HERMES)
- parecer-smartcoding-esteira-2026-09-02.md — revisão adversarial do pacote HERMES (PR #15)
  origem: brainhub-umode@<commit> · classificação INTERNAL · pinta-se com @umodeapporg/ui
```

## 3. `_INDEX.md` — indexar o hub novo:

```
- [[_smartcoding-governanca]] — hub da Governança da Squad (ponteiro p/ brainhub-umode, repo vivo)
```

E criar `tecnico/smartcoding-governanca/_smartcoding-governanca.md` como **hub-ponteiro** (`origem:
brainhub-umode@<commit>`), não cópia.

## 4. `DECISOES.md` — registrar (espelha antes de executar, §2):

```
- <data> — CTO/Líder técnico é AGENTE, não o Bergson. Bergson = arquiteto dos MDs de governança/treinamento/segurança de infra; não é dono de execução por dimensão nem revisor universal. [Vinicius, set/2026]
- <data> — Lovable fora da stack de EXECUÇÃO de código. Executores: HERMES · Codex · Claude Code. [Vinicius]
- <data> — Cânone de componente = @umodeapporg/ui, SEM shadcn. Boilerplate canônico de front = umode-frontend-boilerplate-nextjs. [Vinicius]
- <data> — Os 3 required checks (ci-deterministic + policy-semantic/Marvin + security) travam o merge no MESMO head. ci.yml ainda NÃO existe ([P]). [parecer 2026-09-02]
- <data> — HERMES é SISTEMA/esteira, nunca "A" no RACI. Auditor Independente (não-autor, exact-SHA) é cadeira própria — quem escreve o head não audita o head. [parecer 2026-09-02]
- <data> — P0.1: documento de governança no Lovable expõe conteúdo interno em asset público atrás de gate só client-side. Exige auth server-side. [parecer 2026-09-02, decisão do João]
```

## 5. `SISTEMAS` (`sistemas_curadoria.json`) — a produção UmodeApp que falta (§13):

`verificado_em` só com verificação real (curl/login/request — ler código NÃO é verificar):

```
- umode-fullstack-boilerplate — o veículo de vibecoding (front+back num PR)
- umode-backend-boilerplate-nestjs — gold standard (tem os gates via actions-shared)
- umode-frontend-boilerplate-nextjs — CANÔNICO de front, @umodeapporg/ui, sem shadcn
- gateway-dashboard — auth unificada Cognito, PartnerScopeGuard (mais maduro, menos estrito)
- microservice-integration — partner CRUD + scheduler + conectores ERP
- @umodeapporg/ui (npm público) — design system publicado, v0.4.1
- UmodeApp/actions-shared — os gates reusáveis (Marvin pr-claude-md-gate + pr-security-gate)
- Lovable governanca-squad-umode → governanca-squad-umode.lovable.app (INTERNAL, pendente P0.1)
```

## 6. Prompt pro orquestrador (pronto pra enviar)

```
[Orquestrador — promoção ao vault: Governança da Squad / SmartCoding]

1. NÃO copiar os docs pro vault: brainhub-umode é repo vivo e canônico (§5). Criar só o hub-ponteiro
   tecnico/smartcoding-governanca/_smartcoding-governanca.md (origem: brainhub-umode@<commit>) e indexá-lo
   no _INDEX.md e no CATALOGO.md — na MESMA ação (§3-bis passo 3).
2. Registrar as 6 decisões no DECISOES.md (bloco 4 acima), espelhando antes de executar (§2).
3. Adicionar ao sistemas_curadoria.json a produção UmodeApp (bloco 5), verificado_em só com verificação real.
4. _GOVERNANCA.md só o João emenda (§10) — levar o bloco 1 pra decisão dele.
5. Classificar cada item SEGURO/SENSÍVEL/CONTRADITÓRIO (§3-bis); promover só o SEGURO; o resto vai pra fila.
6. Promoção assistida só se o HERMES.md do vault conceder o job para repos de código; senão é do João.

Não promover nada antes do parecer parecer-smartcoding-esteira-2026-09-02.md ser aceito pelo João.
```

## Conexões
`../_protocolos/parecer-smartcoding-esteira-2026-09-02.md` ·
`../_protocolos/governanca-squad-desenvolvimento.md` · `_GOVERNANCA.md` (vault) · `CATALOGO.md` (vault) ·
`_INDEX.md` (vault) · `DECISOES.md` (vault) · `SISTEMAS.md` (vault) · `umode-os-vault` PR #15
