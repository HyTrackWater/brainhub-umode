# HERMES.md — A esteira de produção `[P]`

> Arquivo-raiz do boilerplate governado da uMode. O HERMES **não é um dos papéis de decisão**; é a
> **esteira** que faz a máquina girar — e um dos executores do Programador (`AGENTS.md`), ao lado de
> Codex e Claude Code. Herda a disciplina do HERMES do vault, agora estendida a código.
> `[P]` — proposta de contrato; entra em produção pelo rito de admissão.
>
> **`PENDING_MIGRATION` (parecer 2026-09-02):** na topologia-alvo o HERMES **sai da raiz** — o contrato
> persistente da esteira é o `HERMES_TRAINING.md` (apontado pelo `AGENTS.md`, não concatenado). Este
> arquivo é o resumo; o contrato executável completo vive no `HERMES_TRAINING.md`.

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

## Como o HERMES entrega código (regra única de merge — corrige a contradição com o RACI)

O HERMES **nunca decide nem aprova merge**. Merge é **capability temporária por branch/lease**, não
atributo do papel. O HERMES pode **executar** um merge **já autorizado** numa **branch de delivery**
(`awscicd`) quando, e só quando: **mesmo head** + **parecer do Auditor independente** + **3 required
checks verdes** + sem conflito + sem drift de escopo. Para **`main` / produção / infra**, nunca — vai
para humano (Bergson/João conforme política).

```
terminou → PR → 3 required checks @ mesmo head → parecer do Auditor (não-autor) →
CODEOWNERS por dimensão → merge AUTORIZADO (capability por lease) → HERMES executa em awscicd
```

- **"Seguro"** = pequeno, local, mesmo head, review independente + checks verdes → HERMES executa o
  merge **já autorizado** em branch de delivery.
- **"Escala"** = toca fundação, schema, auth, produção ou é ambíguo → decisão humana antes.

## Rito de admissão (todo agente, inclusive o próprio HERMES em código)

1. **Governança** — lê e aceita a governança da squad.
2. **Contrato** — existe um `<PAPEL>.md` aprovado pelo João/Bergson antes de qualquer acesso.
3. **Teste de obediência** — a primeira tarefa prova PR-em-vez-de-push, lint-as-código e alto risco.
   Um agente que faz merge direto **reprova**.
4. **Escopo** — passa a escrever só onde o contrato permite (agente estrutural: abre PR, nunca toca `main`).
5. **Ritual** — entra na ronda do CTO/HERMES.
