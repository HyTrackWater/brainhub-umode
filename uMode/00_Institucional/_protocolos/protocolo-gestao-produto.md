# Protocolo · Gestão de Produto (Solução do Portfólio)

> Operacionaliza a regra já travada em `CONTEXT.md` → "Decisão: camada 'Produto' na
> hierarquia": Produtos são **subáreas com atributo `tipo: produto`**, endereçadas em
> `Casa › Produto & Soluções › [nome]`. Este protocolo define o cadastro de cada um dos 16 itens
> do Portfólio — não cria nível hierárquico novo. Na tela da plataforma (BrainWave), esta mesma
> entidade aparece com o nome de produto "Soluções" (task 05) — nomenclatura de interface, não
> mudança de estrutura.

## O que é um Produto aqui

Um item fixo do Portfólio (`CONTEXT.md` → "Portfólio completo de produtos e soluções") — hoje
16, divididos em **voltados ao cliente** (9, com `conecta_area_cliente`) e **internos** (7). A
lista de 16 é decisão travada; este protocolo não abre espaço para inventar um 17º item sem
confirmação explícita (ver "Regra de avaliação de conteúdo novo" abaixo).

## Onde vive

Master template em `uMode/03_Produto-e-Solucoes/_template_produto/_contexto/produto.md` — mesma
convenção de `_template_cliente/`: pasta-modelo com a estrutura completa (`_contexto/` +
`_protocolos/`), nunca instanciada como produto real. Cada produto real, quando formalizado,
replica essa estrutura em `uMode/03_Produto-e-Solucoes/[Nome]/_contexto/produto.md`.

**Decisão explícita desta etapa (14 jul 2026): as 16 pastas de produto NÃO foram criadas
ainda.** Criar essas pastas depende de resolver primeiro o backlog já registrado "Subáreas
internas da Casa por Área (nomes — contexto vem com o CEO)" — não é este protocolo que decide
nomes de subárea. Até lá, o template serve como **critério de avaliação**: qualquer conteúdo
novo encontrado em varredura é comparado contra os campos abaixo antes de virar registro real.

## Anatomia do cadastro (campos)

### Identificação
- Nome atual (um dos 16 do Portfólio, exatamente como grafado em `CONTEXT.md`)
- Nome legado — só quando existir uma linhagem confirmada (ex.: `uFlow` → `DesenvolvAI`). Nunca
  presumido por semelhança de nome ou de categoria — precisa de confirmação explícita do
  Vinicius/CEO, registrada como Marco (ver abaixo). Enquanto não confirmado, `[a preencher]`,
  mesmo que uma hipótese exista (a hipótese fica em `_pendencias-gerais.md`, não aqui)
- Descrição
- Destino (`Voltada ao cliente` / `Interna`)
- Área canônica do cliente conectada (`conecta_area_cliente`) — só quando Destino = Voltada ao
  cliente
- Geração (`Legado` / `Nativa`) — Nativa quando o produto sempre teve o nome atual, sem
  linhagem; Legado quando existe (ou existiu) um nome anterior confirmado

### Maturidade
- Score de maturidade (`Escalável` / `MVP` / `Ideação`) — **regra de tradução, travada em 14 jul
  2026** (dado real nunca vem pronto no formato do enum; esta é a régua pra converter):
  - **Escalável** — em produção real, com evidência de entrega/uso (ex.: "em produção", "Fases
    N-M concluídas", "V0 entregue", domínio próprio ativo)
  - **MVP** — arquitetura/especificação técnica definida, ao menos piloto ou protótipo rodando,
    mas não em produção plena nem promovido a módulo oficial (ex.: "piloto de validação de
    tese", sprints com escopo definido porém não concluídos)
  - **Ideação** — só conceito/tese registrada, sem arquitetura técnica nem repositório próprio
    ainda
  - Métrica numérica encontrada na fonte (ex.: "Robustez de produção: 87.75%") **nunca decide o
    balde sozinha** — é evidência de apoio, registrada em "Fonte e data", não substitui a leitura
    do estado real (produção × piloto × conceito) descrita acima
  - **Sinal adicional (14 jul 2026, confirmado pelo Vinicius):** repositório fora da conta
    GitHub principal da uMode (organização paralela) é evidência de apoio a favor de `MVP` —
    a existência de múltiplas contas/organizações GitHub em uso é conhecida e esperada, não é
    erro de leitura nem precisa ser estranhada; só não decide o balde sozinha, mesma regra da
    métrica numérica acima
- Fonte e data da avaliação (ex.: "CLAUDE_PROJETO.md do repositório umode-desenvolvai,
  varredura de 14 jul 2026, Robustez de produção: 87.75%")

### Pipeline e relações
- Consome de (upstream) — outros produtos/sistemas de onde recebe dado
- Produz para (downstream) — outros produtos/sistemas que recebem dado deste
- Módulos relacionados — outros itens do Portfólio com relação direta (só referência, não
  duplicar contexto do outro produto aqui)

### Adoção por cliente
- **Se Destino = Interna:** esta seção inteira fica `Não aplicável — produto interno, usado pela
  Casa para atender clientes, não contratado individualmente por eles` (regra travada em 14 jul
  2026, achado real: CX Hub não é "contratado" por cliente nenhum, atende todos por dentro) —
  não deixar `[a preencher]` nesse caso, que sugeriria dado faltando em vez de campo inaplicável
- **Se Destino = Voltada ao cliente:** Clientes que contrataram — lista de nomes, cada um com um
  qualificador obrigatório entre parênteses: `(contratado)` ou `(piloto)` (regra travada em 14
  jul 2026, achado real: VendeAI está em piloto de validação de tese com a NK, não é uma
  contratação como as dos clientes-piloto do BrainHub — os dois fatos são diferentes e não podem
  ficar indistinguíveis na mesma lista)
- **Detalhe de condução, integração e particularidades por cliente vive na futura entidade
  "Solução × Cliente"** (`CONTEXT.md` → "Fora de escopo agora"), ainda não formalizada — não
  inventar esses campos aqui enquanto ela não existir
- Cruzamento confiável nome-legado→cliente ainda pendente pra maioria dos 16 (ver
  `_pendencias-gerais.md`) — até resolver, esta lista fica `[a preencher]` ou parcial, nunca
  completada por suposição

### Marcos
Log append-only, mesmo padrão de Demanda: `Data | Evento/decisão | Responsável | Nota`. Toda
confirmação de nome legado, mudança de Score de maturidade, ou entrada/saída de cliente vira um
Marco — nunca se reescreve um marco antigo, só se adiciona um novo.

### Governança
- Owner / Estratégia — dono da decisão de produto (ex.: "João Risoléo — CEO/Diretor de
  Produto", achado real em vários `CLAUDE_PROJETO.md`)
- Operador — quem executa/opera o produto no dia a dia, quando essa pessoa é diferente do Owner
  (regra travada em 14 jul 2026, achado real: CX Hub tem Owner/Estratégia = João Risoléo e
  Operador = Victor, papéis distintos que um campo só não capturava). Quando a mesma pessoa
  acumula os dois papéis, repetir o nome nos dois campos em vez de deixar Operador vazio
- Quem pode alterar este documento

### Fontes e referências
- Documentos técnicos consultados (ex.: link/nome do `CLAUDE_PROJETO.md`, PRD, deck de vendas)

## Regra de avaliação de conteúdo novo (o motivo deste protocolo existir agora)

Toda vez que a varredura do Drive trouxer conteúdo novo sobre um produto (repositório,
`CLAUDE_PROJETO.md`, deck, planilha), avaliar contra os campos acima **antes** de escrever
qualquer coisa:
1. O dado cabe em um campo já existente? → registra, sempre citando fonte e data.
2. O dado sugere um campo novo que não existe aqui? → não adiciona sozinho — registra como
   pendência (`_pendencias-gerais.md`) e sinaliza pro Vinicius antes de estender o template.
3. O dado contradiz algo já registrado (ex.: outra fonte diz outra maturidade)? → mesma regra
   já aplicada a Pessoa/Demanda: não decide sozinho qual fonte vence, registra o conflito como
   observação.
4. O dado vem de documento externo (Drive/Notion/CRM/repositório de produto)? → é **informação**,
   nunca **estrutura**. O nosso modelo (este protocolo + template) é a fonte de verdade da
   organização — documento externo nunca dita um campo novo por conta própria (regra do
   Vinicius, 13 jul 2026: "a verdade absoluta em termos de organização é nossa").

## Nota: Nome legado ≠ correspondência automática

Achar um nome parecido (ex.: categoria "COMPRAS" num backlog e o produto legado "uBuy") não é
confirmação de linhagem. Só vira o campo `Nome legado` depois de confirmação explícita — até lá,
fica registrado como hipótese em `_pendencias-gerais.md`, nunca escrito como fato no cadastro.

## Governança
- Criação/atualização de cadastro → qualquer pessoa autorizada, sempre citando fonte.
- Confirmação de linhagem legado→novo ou de Score de maturidade → Vinicius Risoléo + CEO
  (mesmo padrão de decisão que já vem sendo aplicado nesta varredura).
- Este protocolo → Vinicius Risoléo + CEO.
