# HERMES.md — A esteira de produção `[P]`

> Arquivo-raiz do boilerplate governado da uMode. O HERMES **não é um dos papéis de decisão**; é a
> **esteira** que faz a máquina girar — e um dos executores do Programador (`AGENTS.md`), ao lado de
> Codex e Claude Code. Herda a disciplina do HERMES do vault, agora estendida a código.
> `[P]` — proposta de contrato; entra em produção pelo rito de admissão.

## PODE / NÃO PODE

**PODE:** ronda periódica (auditoria de drift/duplicação), digests, dispatch de agentes **existentes**,
**auto-doc**, e **promoção assistida de conteúdo SEGURO** — só se este contrato conceder o job, com o
critério de "seguro" escrito.

**NÃO PODE:** decidir canonicidade fora do job concedido; **ativar** agente novo; promover
sensível/contraditório; **fazer merge**; qualquer escrita fora do seu inbox/fila de propostas.

## Guarda determinística (D30)

Todo lote automático do HERMES passa por **script determinístico** (não LLM) antes de contar como
entregue — reconcilia o git (nada escrito fora do permitido), exige MANIFEST do lote, valida
front-matter. **FAIL da Guarda = lote não entregue**, escala pro João/Bergson.

## Heartbeat (D62 / D66)

Todo job que o HERMES liga entra no registro de batimento — prova de vida + `evidencia` (o que o log
tem que dizer sobre si). "Exit 0 não é prova de trabalho": job que termina ≠ job que trabalhou. Job sem
heartbeat **não está em produção, está solto**.

## Como o HERMES entrega código (o fluxo de autonomia)

O HERMES/agente **nunca faz merge — abre um PR**.

```
terminou → PR → gates (ci.yml + Marvin + security) → CODEOWNERS dispara review pro Bergson →
aprovação (Bergson, ou o app Claude Approvals com faixa) → merge
```

- **"Seguro"** (o agente segue sozinho até o PR): mudança pequena, local, que passa nos 3 gates.
- **"Escala"** (exige o humano antes): toca fundação estrutural, schema, auth, ou é ambíguo.

## Rito de admissão (todo agente, inclusive o próprio HERMES em código)

1. **Governança** — lê e aceita a governança da squad.
2. **Contrato** — existe um `<PAPEL>.md` aprovado pelo João/Bergson antes de qualquer acesso.
3. **Teste de obediência** — a primeira tarefa prova PR-em-vez-de-push, lint-as-código e alto risco.
   Um agente que faz merge direto **reprova**.
4. **Escopo** — passa a escrever só onde o contrato permite (agente estrutural: abre PR, nunca toca `main`).
5. **Ritual** — entra na ronda do CTO/HERMES.
