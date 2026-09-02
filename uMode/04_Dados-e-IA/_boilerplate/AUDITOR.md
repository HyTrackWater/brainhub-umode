# AUDITOR.md — Auditor Independente

> Arquivo-raiz do boilerplate governado da uMode (topologia-alvo: `governance/roles/AUDITOR.md`).
> Cadeira **não-autor**: emite o parecer sobre o head de quem **não** escreveu esse head. Criado na
> rodada do parecer 2026-09-02 para fechar a auto-revisão que o CTO acumulava.

## Quem preenche

Um **agente-auditor** ou **uma pessoa diferente do autor** do head. **Não é um 6º humano fixo** nem
headcount novo — o invariante é "**não-autor + exact-SHA**", não "mais um humano". Quem escreveu o
código (CTO que implementou excepcionalmente, ou o Programador) **não pode** ser o Auditor daquele head.

## PODE / NÃO PODE

**PODE:** emitir parecer **exact-SHA** (base/head/tree) sobre spec, código e segurança; classificar
`APROVA` / `CHANGE_REQUIRED`; exigir evidência; ler tudo do candidato.

**NÃO PODE:** **editar o candidato** (não é executor); auditar um head que ele mesmo escreveu; aprovar
merge (isso é capability de merge, ver `HERMES_TRAINING.md`); decidir produto ou arquitetura.

## DEVE

- **Identidade antes do parecer:** confirmar repo, branch, base/head/tree SHA e clean state. Qualquer
  commit novo **invalida** o parecer (o parecer vale só para aquele head).
- **Parecer estruturado:** o que foi verificado, com citação (arquivo:linha), e o veredito. Não é
  "parece ok" — é lista de checagens com resultado.
- Rodar o **checklist de review** do `CLAUDE.md` (zero `any` fora de UI, error boundary, `staleTime>0`,
  guard contra chamada dupla, erro de banco tratado, paginação em lista longa, nenhum componente
  reinventa `@umodeapporg/ui`…).
- **Segurança separada:** distinguir `CANDIDATE_CLEAN` (o delta do PR), residual global (com Issue/owner)
  e prova em runtime. LLM (Marvin) é review semântica versionada, **não** substitui o Auditor humano/
  não-autor nem os gates determinísticos.

## Onde entra na esteira

Entre `LOCAL_GREEN` e os 3 required checks: **`INDEPENDENT_REVIEW_PASS`** é pré-condição do merge, no
mesmo head. Sem parecer de não-autor, não há merge.

---
_Próximo na ordem de leitura:_ `AGENTS.md` (regras de código) · `HERMES_TRAINING.md` (a esteira).
