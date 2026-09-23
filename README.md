---
aliases:
  - "BrainHub · uMode"
---
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

👉 **[`START.md`](START.md)** — **o condutor da triagem**: declara o conjunto completo de
documentação ("o time"), a classe de cada arquivo, quem é dono de qual assunto, e **a ordem de
leitura conforme a tarefa**.

👉 **[`AGORA.md`](AGORA.md)** — onde o projeto está hoje, em uma tela.

Para abrir uma sessão de trabalho com a LLM, cole apenas: `Leia START.md`

**Verificação antes de todo commit:**

```
python scripts/valida-padrao-corpus.py # padrao canonico do corpus
python scripts/valida-documentacao.py # nenhum .md estrutural orfao
```

## Documentação base

| Arquivo | O que é |
|---|---|
| **`AGORA.md`** | **orientação — o estado atual, em uma tela** |
| **`START.md`** | **o manifesto e a ordem de leitura** — começe por ele |
| `CLAUDE.md` | papel do executor, regras invioláveis, como executar tarefas |
| `CONTEXT.md` | objetivo, hierarquia, regras travadas, portfólio |
| `STATE.md` | **histórico** completo, sessão a sessão — não é orientação |
