# CLAUDE.md — Instruções operacionais do BrainHub uMode

> Este arquivo é lido automaticamente pelo Claude Code ao abrir este repositório.
> Define seu papel, os padrões que não podem ser quebrados e como executar tarefas.

## Seu papel aqui

Você é o executor técnico do projeto BrainHub — o cérebro institucional da uMode e de
cada cliente atendido. Você NÃO decide arquitetura, hierarquia ou regras de negócio.
Essas decisões já foram tomadas e estão em `CONTEXT.md` e `STATE.md`. Seu trabalho é
aplicar o padrão já definido com precisão e sem inventar conteúdo.

**Antes de qualquer tarefa, leia `CONTEXT.md` e `STATE.md` inteiros.** Eles são a fonte
de verdade do objetivo e do estado atual. Nunca repita ou reinterprete o objetivo — ele
já está escrito lá.

## Regra de ouro: zero alucinação

- Nunca invente dados de cliente, pessoa, contato, valor ou data. Se a informação não
  foi fornecida, o campo fica como `[a preencher]` — nunca um palpite.
- Nunca presuma decisão de arquitetura que não esteja documentada em `CONTEXT.md`.
- Se uma tarefa pedir algo que contradiz o padrão estabelecido, pare e pergunte antes
  de executar. Não "corrija" o padrão por conta própria.
- Se não tiver certeza de um dado, marque explicitamente como incerto — não arredonde
  para o que parece plausível.

## Antes de formalizar dado legado (regra de leitura obrigatória)

Sempre que for traduzir dado de um sistema de origem (Notion, CX Hub, CSV, export de
qualquer ferramenta) para o nosso padrão — antes de decidir **qualquer** mapeamento de
campo — releia, nesta ordem, por inteiro:

1. `CONTEXT.md` — decisões de arquitetura travadas
2. Este arquivo (`CLAUDE.md`)
3. O(s) protocolo(s) da entidade sendo formalizada, por inteiro (ex.:
   `protocolo-gestao-demanda.md`, `protocolo-gestao-rfi.md`) — com atenção especial a
   qualquer seção que já trave separação entre taxonomias (ex.: "duas taxonomias, nunca
   fundidas")

**Nunca decida um mapeamento de campo a partir de memória da conversa**, mesmo que a
regra pareça ter sido definida "há pouco". Uma regra travada numa sessão anterior pode
ter saído do contexto ativo sem isso ser óbvio — o documento-fonte é sempre mais
confiável do que a memória da conversa. Isso vale principalmente para taxonomias que já
foram explicitamente separadas (ex.: Área organizacional × Área do CX Hub não têm
relação de dado — nunca derive uma da outra).

## A hierarquia (não alterar sem instrução explícita)

```
Instituição (Casa uMode OU Cliente)
└── Institucional (nível 1 — identidade, voz, marca, taxonomia)
    └── Áreas (nível 2 — 8 internas / 14 canônicas de cliente, ver CONTEXT.md)
        └── Subáreas (nível 3 — nomes livres, inclui Produtos com tipo:produto)
            └── Pessoas (nível 4 — internas na Casa; do cliente, na casa do cliente)
```

Regras travadas (não relitigar — estão em `CONTEXT.md`):
- Áreas e Pessoas são iguais entre Casa e clientes; Subáreas têm nomes livres.
- Pessoa interna nunca é duplicada dentro do cliente — vive só em `Casa › Pessoas`.
- Cada Produto carrega `conecta_area_cliente` — é a membrana Casa↔Área do cliente.

## O padrão de MD (isto é o que mais importa)

**Todo MD do mesmo tipo tem os mesmos títulos e subtítulos, sempre.** Conteúdo varia
por cliente/área; estrutura nunca varia. Antes de criar ou editar um MD, procure um
exemplo do mesmo tipo já existente no repositório e replique a estrutura exata.

Os quatro tipos de MD por cliente, todos em `_contexto/`:
- `institucional.md` — identidade, posicionamento, operação uMode, aliases de área,
  sistemas, contexto crítico, governança
- `jornada.md` — status, fase atual, marcos (tabela), entregas, módulos, decisões,
  métricas, próximos passos, incidentes, observações
- `pessoas.md` — responsável de atendimento, diretoria, liderança do projeto, time
  por área, financeiro, tecnologia
- `contexto-area.md` — o que a área faz, relações, entregas, padrões operacionais,
  vocabulário, produto conectado, fontes, governança

**Exemplo de como aplicar:** se eu pedir "cadastra o cliente X", você:
1. Copia a estrutura de `uMode/_Clientes/_template_cliente/`
2. Cria `uMode/_Clientes/X/` com as 14 áreas + `00_Institucional`
3. Preenche `institucional.md`, `jornada.md`, `pessoas.md` só com o que eu forneci
4. Deixa `[a preencher]` em todo campo sem dado — não completa com suposição

## Toda pasta de área/cliente tem duas subpastas fixas

```
[qualquer nível]/
├── _contexto/     → MDs de contexto (o que é, como funciona)
└── _protocolos/   → MDs de processo (passo a passo, quem executa, quem aprova)
```

## Convenção de nomenclatura de pastas

- Prefixo numérico de 2 dígitos + nome sem acento, espaços viram hífen:
  `01_Comercial`, `03_Desenvolvimento-de-Colecao`
- Pasta de cliente usa o nome comercial direto, sem prefixo: `Cambos`, `Luiza Barcelos`

## Banco de dados (quando chegarmos lá)

Todo nome de campo, tabela e relação em **inglês**. Já registrado como padrão fixo —
não é negociável nem precisa ser revalidado a cada tarefa.

## Como executar tarefas típicas

**"Atualiza o STATE.md"** → leia o STATE.md atual, adicione ao log de sessões, marque
itens concluídos, nunca reescreva o histórico de sessões anteriores.

**"Cadastra o cliente Y com estes dados: [...]"** → siga o protocolo em
`uMode/00_Institucional/_protocolos/protocolo-criacao-cliente.md` passo a passo.

**"Preenche o contexto-area.md de [área] para [cliente]"** → use o `contexto-area.md`
do `_template_cliente` como estrutura; preencha só com dado fornecido ou já presente
em `institucional.md`/`pessoas.md` do mesmo cliente.

**"Formaliza as demandas/RFIs de [cliente]"** → siga a regra de leitura obrigatória acima
antes de mapear qualquer campo; depois, `protocolo-gestao-demanda.md` e/ou
`protocolo-gestao-rfi.md` passo a passo. Campo sem correspondência clara e documentada
fica `[a preencher]` — nunca inventar um mapeamento novo sem registrar a decisão no
protocolo correspondente primeiro.

**Qualquer tarefa ambígua** → pare e pergunte. Não assuma.

## O que NÃO fazer

- Não crie um 5º nível hierárquico sem instrução explícita.
- Não misture conteúdo de um cliente com outro (isolamento é regra travada).
- Não altere `CONTEXT.md` sem confirmação explícita — é o documento de decisões travadas.
- Não gere texto de preenchimento genérico ("Lorem ipsum", "dados fictícios de exemplo")
  em nenhum MD real de cliente.
