# BrainHub · uMode

Repositório de contexto institucional do projeto BrainHub.
Fonte de verdade dos MDs de contexto, protocolos e documentação de arquitetura.

## Estrutura

```
uMode/                         # Casa interna
  00_Institucional/
    _contexto/                 # institucional.md
    _protocolos/               # protocolo-criacao-cliente.md
  01_Comercial ... 08_Operacoes/
    _contexto/                 # contexto-area.md
    _protocolos/
  _Clientes/
    _template_cliente/         # template base para novos clientes
    [Nome do cliente]/         # uma pasta por cliente
      00_Institucional/
        _contexto/             # institucional.md · jornada.md · pessoas.md
      01_Planejamento ... 14_Engenharia/
docs/                          # HTMLs de registro de arquitetura
CONTEXT.md                     # core: o quê e como
STATE.md                       # avanço: sprints e backlog
```

## Por onde começar

👉 **[`AGORA.md`](AGORA.md)** — onde o projeto está hoje, em uma tela: papel, método,
cobertura em número, frente ativa, próximos passos e decisões em aberto.

Para abrir uma sessão de trabalho com a LLM, cole apenas: `Leia START.md`

## Documentação base

| Arquivo | O que é |
|---|---|
| **`AGORA.md`** | **orientação — o estado atual, em uma tela** |
| `START.md` | protocolo de abertura de sessão |
| `CLAUDE.md` | papel do executor, regras invioláveis, como executar tarefas |
| `CONTEXT.md` | objetivo, hierarquia, regras travadas, portfólio |
| `STATE.md` | **histórico** completo, sessão a sessão — não é orientação |
