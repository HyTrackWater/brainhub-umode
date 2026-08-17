# Backlog de convergência — nosso BrainHub × o vault do João

> Criado em **04 ago 2026** a partir de vistoria **somente leitura** de
> `C:\Ambientes Virtuais\BrainHub - João Risoléo` (1.435 arquivos, 887 `.md`, 69,9 MB). **Nada foi
> alterado lá, nenhum commit, nenhum push** — restrição explícita de Vinicius.
>
> **Foco: arquitetura, não conteúdo.** A pergunta que este documento responde é "quanto estamos
> distantes em termos de hierarquia e de como desenhamos as relações", porque o destino é banco de
> dados operado por agentes que criam demanda no inbox de cada colaborador ou área.

## Cobertura desta vistoria
### O que foi lido por inteiro
`_CANON.md` (3 KB) · `MANIFEST.md` (8 KB) · `2026-08-03-BRIEF-PARA-HERMES-redesenho-do-zero.md`
(7 KB) · `ARQUIVO_FINAL_HANDOFF_REDESENHO_UMODE_2026-08-04.md` (25 KB) · varredura estrutural
completa das 1.435 entradas, com contagem de front-matter em todos os 884 `.md` do vault.
### O que NÃO foi lido — e é onde pode haver correção do que está abaixo
**`DECISOES.md` (156 KB)** · `SISTEMAS.md` (51 KB) · `_GOVERNANCA.md` (21 KB) · `CATALOGO.md` (20 KB)
· `COBERTURA_DOCUMENTS.md` · `AGENTS.md` · `CLAUDE.md` · `CLAUDE_OPERADOR.md` · `SYNC_EXCLUDE.md` ·
os **426 `.md` do `BrainHub/` dele** · os **273 do `inbox/`** · as **46 skills** · o
`2026-08-03-...-DUMP-vinicius.md` (23 KB) e o mapa visual HTML.
⚠ O `_GOVERNANCA.md` é chamado por ele de **"constituição do vault"**, e o `DECISOES.md` é o registro
de decisões citado por número no código de outros repositórios. **São as duas leituras que faltam
para este backlog virar definitivo.**

## Onde já convergimos — e é mais do que eu esperava
Isto importa porque significa que **não estamos recomeçando**:
- **A taxonomia de Área é idêntica, com a mesma numeração:** `00_Institucional`, `01_Comercial`,
  `02_Atendimento`, `03_Produto-e-Solucoes`, `04_Dados-e-IA`, `06_Tecnologia`, `07_People`,
  `08_Operacoes`, e `_Clientes` no mesmo nível. Não é semelhança — é o mesmo conjunto.
- **A convenção `_contexto/` e `_protocolos/`** é a mesma.
- **Os tiers T0/T1/T2** são os mesmos, com a mesma semântica.
- **"Agente nenhum escreve no canônico"** — a regra dele é a mesma disciplina que aplicamos aqui: os
  coletores só leem, a escrita fica com um ponto único.
- **"`exit 0` não prova trabalho"** é irmã da nossa regra de validar por diff de headings em vez de
  confiar no que o script diz ter feito.
- A separação **rascunho × canônico** é a nossa regra de ouro de zero alucinação, dita de outro jeito.

## As divergências que bloqueiam o banco
> Ordenadas por quanto travam o desenho do schema. As três primeiras precisam de decisão **antes** de
> qualquer modelagem.

### 1 · A chave de cliente não é a mesma coisa nos dois lados
Nossas pastas são **nome comercial**: `NK STORE`, `Luiza Barcelos`, `Oficina Reserva`. As dele são
**slug**: `nk-store`, `luiza-barcelos`, `oficina-reserva`. O `CONTEXT.md` já trava `client_id` como
slug estável — mas **o nome da pasta não é o `client_id`**, e no dele é.
**Ele está à frente aqui.** Pasta = chave é o que permite JOIN sem tabela de tradução.
### 2 · Front-matter: 75% dele, 0% nosso
**665 dos 884 `.md` do vault têm front-matter YAML; nenhum dos nossos 1.327 tem.** As chaves que ele
usa são exatamente metadado de linha de banco: `origem` · `tipo` · `entidade` · `sync` · `criado_em` ·
`atualizado_em` · `status` · `versao` · `caminho_origem` · `extraido_em`.
⚠ **Isto contradiz de frente uma decisão que eu tomei** e registrei como "índice derivado, não
front-matter". **Eu revisaria essa decisão**, e é importante dizer por quê: minha objeção era criar
duas fontes de verdade para o **mesmo campo de conteúdo** — o heading e o metadado. Mas
`origem`, `tipo` e `entidade` **não estão em heading nenhum**; são metadado que hoje só existe na
minha cabeça e no caminho do arquivo. As duas coisas não competem: **front-matter é a fonte,
o índice derivado é a materialização.** Sem front-matter, migrar 1.327 arquivos para banco exige
inferir `tipo` e `entidade` do caminho — que é exatamente o tipo de dedução frágil que queremos evitar.
### 3 · O modelo interno do cliente é incompatível
**Nenhum dos 47 clientes dele tem pastas de área** — zero. O nosso cliente é 14 áreas canônicas com
4 MDs de contexto. O dele é **um índice `_<slug>.md`** (39 de 47 têm) mais artefatos organizados por
**programa e entregável**: `programa-2026/`, `contrato/`, `relatorios/`, `relatorios-assinados/`, com
nomes datados no padrão `<slug>_<YYMMDD>_<assunto>.md`.
São dois modelos de mundo: o nosso classifica por **função organizacional**, o dele organiza por
**unidade de entrega**. Podem ser ortogonais e complementares — mas **isso precisa ser decidido, não
descoberto na migração**.
### 4 · Ele tem um nível de instituição acima do nosso
A raiz do BrainHub dele tem `uMode`, `João` e `SoulGames` como **irmãos**. A nossa raiz **é** a uMode.
Para o banco isso é uma tabela de `tenant` acima de `instituição` — ou a decisão explícita de que o
BrainHub da uMode não hospeda os outros negócios.
### 5 · Os dois universos de cliente quase não se sobrepõem
Depois de normalizar para slug: **23 em comum**, **21 só dele**, **~20 só nossos**. E os 21 dele
incluem justamente os nomes que eu vinha registrando como "cliente sem casa" em outras fontes:
`arezzo`, `alpargatas`, `polenectar`, `genuo`, `grupo-veste`, `posthaus`, `esposende`, `lupo`,
`beira-rio`, `dakota`, `grendene`, `via-marte`, `sinbi`, `meta`, `renner`, `aramis`, `santa-lolla`,
`nilit`, `basico-co`, `crossx-jump3r`, `marcio-delbin`, `alinvest-ift`.
**O vault dele é a fonte de cliente que faltava.** E `alinvest-ift` sugere que parte do universo dele
é **mentoria/programa**, não cliente de plataforma — o que pode explicar a divergência e apontar para
duas classes de instituição, não uma lista só.

## As divergências que bloqueiam agentes
### 6 · Não temos `inbox` nem promoção
Nele, agentes escrevem em `inbox/<agente>/` e **só o João promove ao canônico**. Aqui, eu escrevo
direto no canônico. Funciona com um agente disciplinado; **não funciona com uma frota**. E o destino
declarado é frota.
### 7 · Não temos Context Pack
Ele identifica **quatro espécies de conteúdo**: Agente (quem é) · Skill (como fazer) · Conhecimento
(o que é verdade) · **Context Pack** (pacote versionado de contexto para um assunto, com
`manifest.json`, hash das fontes, tier, runtimes autorizados e política de write-back).
A ausência disso é o diagnóstico dele para o contexto que ficou preso nos Claude Projects. **É
exatamente o risco da nossa `D-2026-002`:** o agente de suporte uFlow tem papel e treinamento em
arquivos soltos, não em pacote versionado — e os arquivos de origem já sumiram do disco uma vez.
### 8 · Não temos evidência de execução
Ele planeja `agent_runs` e `agent_health` com a regra: `sem heartbeat = vermelho` · `sem run evidence
= inválido` · `exit 0 sem evidência = falha` · `sem read-back = não entregue`. Nós não temos nenhum
registro de execução de agente.

## As divergências que bloqueiam confiança no dado
### 9 · Não temos registro de decisão endereçável
As decisões dele são **citadas por número dentro do código de outros repositórios** — `D11`, `D32`,
`D47/D49`, `D51`, `D67`. O nosso `CONTEXT.md` tem as decisões travadas em prosa e **não é citável**.
⚠ Achado lateral: o `DECISOES.md` dele tem 156 KB, mas **só 1 título casa com o padrão `### D<n>`** —
o registro dele também não é parseável por número de forma consistente. Nenhum dos dois lados resolveu
isto.
### 10 · Não temos registro de fonte canônica
O `MANIFEST.md` dele declara, bloco por bloco: **Bloco | Camada | Nível | Canônico | Consumido por |
Versão | Revisão**, com a regra "cada bloco tem UM canônico; os demais lugares são espelho".
Nós não declaramos em lugar nenhum qual arquivo é canônico para qual fato, nem quem consome. Para o
banco, **isso é a tabela de procedência**.
### 11 · Não temos asserção de fato verificável
O `_CANON.md` dele é um bloco legível por máquina — `kind :: scope :: value :: files`, com regras
`present` e `absent` — lido por `_tools/drift_sweep.sh`. Se um número canônico muda, o guardrail passa
a cobrar o novo valor **sem tocar no script**.
Nós validamos **estrutura** (diff de headings) e nunca **fato**. Um número errado num MD nosso não
dispara nada.
### 12 · Não temos modelo de publicação
Ele move confidencialidade de **localização** para **sincronização**: tudo mora no vault, e
`SYNC_EXCLUDE.md` é a autoridade única de o que não sobe para o Drive do time. Nós temos a pergunta
do T1 da Cambos aberta desde julho e **nenhum modelo de publicação**.

---

# BACKLOG

> Prioridade declarada por Vinicius em 04 ago 2026: executar **depois** dos enriquecimentos ainda
> pendentes, e antes da migração para banco. Cada frente traz o que fazer e o critério de pronto.
> **Nada aqui altera o vault dele.**

## Tier 0 — sem isso o schema não fecha

**C1 · Tornar a pasta do cliente igual ao `client_id`**
Renomear as 46 pastas de cliente para slug, preservando o nome comercial dentro do
`institucional.md`. Atualizar os 6 CSVs do índice, os scripts geradores e os caminhos citados nos MDs.
**Pronto quando:** nome da pasta == `client_id`, e os 23 clientes em comum têm pasta com o mesmo nome
nos dois repositórios. **Dependência:** nenhuma. **É a primeira, porque toda reconciliação depende dela.**

**C2 · Decidir front-matter e, se aprovado, aplicar nos 1.327 arquivos**
Adotar o conjunto de chaves dele (`origem`, `tipo`, `entidade`, `sync`, `criado_em`, `atualizado_em`,
`status`, `versao`) e gerar por script, com o valor derivado do que já sabemos do caminho e do
conteúdo. Manter o índice derivado como materialização, não como substituto.
**Pronto quando:** 100% dos MDs têm front-matter válido e o índice é gerado a partir dele, não do
caminho. **Dependência:** C1 (o `entidade` usa o slug). **Precisa da sua decisão — reverte uma minha.**

**C3 · Reconciliar o modelo interno do cliente**
Decidir se **Área** (nosso) e **Programa/Entregável** (dele) são o mesmo eixo ou eixos ortogonais. Se
ortogonais — que é a minha leitura — o cliente passa a ter **duas dimensões**: classificação por área e
organização por unidade de entrega. Desenhar as duas no schema antes de migrar qualquer coisa.
**Pronto quando:** existe um desenho único de "o que é um cliente" que acomoda os dois repositórios sem
perder informação. **Dependência:** C1.

**C4 · Definir o nível acima da uMode**
Decidir se o BrainHub hospeda só a uMode ou também `João` e `SoulGames` como instituições irmãs. Muda
a raiz do schema.
**Pronto quando:** a decisão está no `CONTEXT.md` e o mapa de entidades reflete. **Dependência:** nenhuma.

## Tier 1 — sem isso a frota de agentes não roda

**C5 · Criar `inbox/` e o contrato de promoção**
Agente escreve em `inbox/<agente>/`; promoção ao canônico exige destino, índice e aprovação. Definir o
que promove sozinho (T2 seguro, destino inequívoco) e o que exige humano.
**Pronto quando:** nenhum agente escreve canônico direto, e existe fila de promoção com owner e
próxima ação. **Dependência:** nenhuma. **Bloqueia a `D-2026-002` em produção.**

**C6 · Formalizar Context Pack como 4ª espécie**
Estrutura: `CONTEXT.md`, `INSTRUCTIONS.md`, `DECISIONS.md`, `SOURCES.md`, `SKILLS.md`, `EXAMPLES.md`,
`LIMITS.md`, `manifest.json` com pack ID, versão, hash das fontes, tier, runtimes autorizados e
política de write-back.
**Primeiro caso de uso, já disponível:** empacotar o agente de suporte uFlow da `D-2026-002` — hoje
ele vive em dois MDs soltos, e os arquivos de origem **já sumiram do disco uma vez**.
**Pronto quando:** o mesmo agente abre em dois runtimes sem perder instrução, fonte, decisão e limite.
**Dependência:** C5.

**C7 · Registro de execução e saúde de agente**
Tabelas `agent_runs` e `agent_health`, com a regra "sem heartbeat = vermelho, `exit 0` sem evidência =
falha". Enquanto não há banco, o equivalente em MD com data e prova.
**Pronto quando:** toda execução de agente deixa registro consultável com prova de conteúdo.
**Dependência:** C6.

## Tier 2 — sem isso não se confia no dado

**C8 · Registro de decisões numerado e citável**
Migrar as decisões travadas do `CONTEXT.md` para um registro numerado (`D001`…), com data, autor,
motivo e consequência, no formato que permita citar por número em código, protocolo e commit.
Reservar faixa para não colidir com a numeração dele.
**Pronto quando:** toda decisão travada tem número, e o `CONTEXT.md` aponta para o registro em vez de
narrar. **Dependência:** nenhuma. ⚠ Combinar a faixa de numeração com o João antes de começar.

**C9 · Registro de fonte canônica (nosso MANIFEST)**
Declarar, por bloco de conhecimento: qual arquivo é canônico, quem consome, nível de sensibilidade,
versão e data de revisão. É a tabela de procedência do banco.
**Pronto quando:** todo fato relevante tem um canônico declarado e nenhum tem dois.
**Dependência:** C2 (o front-matter alimenta metade disso).

**C10 · Asserção de fato verificável (nosso CANON + drift sweep)**
Bloco legível por máquina no formato `kind :: scope :: value :: files`, com `present`/`absent`, e um
script que roda contra o repositório. Começar pelos números que já erramos: contagens, IDs de
integração, nomes de produto.
**Pronto quando:** mudar um número canônico num MD sem atualizar o CANON faz a verificação falhar.
**Dependência:** C9.

**C11 · Modelo de publicação e sincronização**
Definir o equivalente ao `SYNC_EXCLUDE.md`: o que do nosso repositório pode ir para onde. Fecha, de
passagem, a pergunta do T1 da Cambos, aberta desde julho.
**Pronto quando:** existe autoridade única declarando o que publica e o que não.
**Dependência:** C2 (a chave `sync` do front-matter é o mecanismo).

## Tier 3 — completa o modelo

**C12 · Reconciliar as duas listas de cliente**
23 em comum, 21 só dele, ~20 só nossos. Investigar se os dele são clientes de plataforma ou de
mentoria/programa (`alinvest-ift` é o indício) — o que pode virar **duas classes de instituição**.
**Pronto quando:** existe uma lista mestra única com a origem de cada cliente declarada.
**Dependência:** C1. ⚠ Esta é a frente com maior ganho de conteúdo: **o vault dele é a fonte de
cliente que eu vinha procurando desde julho.**

**C13 · Programa e Projeto como entidades**
Confirmado por **duas fontes independentes**: o `programa-2026/` dos clientes dele e a hierarquia
`Programa → Projeto → Demanda → Subdemanda` do CX Hub. Nós não temos nenhuma das duas.
**Pronto quando:** as duas entidades existem no modelo, com vínculo opcional para Demanda.
**Dependência:** C3.

**C14 · Fechar a enumeração de Área**
Ele tem **`_Parceiros`** e não tem `05_Financeiro`; nós temos `05_Financeiro` e não temos
`_Parceiros`. Decidir a enumeração final das duas listas (8 internas, 14 de cliente).
**Pronto quando:** a enumeração é a mesma nos dois repositórios, ou a diferença está justificada por
escrito. **Dependência:** nenhuma.

**C15 · Convenção de nome de arquivo**
Ele usa `<slug>_<YYMMDD>_<assunto>.md`, que carrega entidade e data no nome. Nós usamos nome
semântico (`institucional.md`, `D-2025-001.md`). Decidir se convergimos ou se a diferença é
justificada por tipo de arquivo — o nosso é contexto estável, o dele é artefato datado.
**Pronto quando:** a regra está no protocolo. **Dependência:** C2 (se o front-matter carrega a data, o
nome não precisa).

**C16 · Catálogo de sistemas e o crosswalk repositório ↔ produto**
O `MANIFEST.md` dele **já resolve** o que eu tinha registrado como pendência aberta: `catalogcraft-ai`
= **EnriqueceAI (ex-CadastroAI)** — confirmação independente do que deduzimos —,
`umode-design-guardian` = **AlocAI**, `umode-vendeai` = **VendeAI (≠ Sales Hub)**,
`umode-gest-o-de-opera-o-2f6bdc59` = **ONB HUB**, `gist-sparkle` = CX Hub oficial,
`integration-pulse-check` = **IntHub, e ele o chama de gold standard de formato**. Trazer para o nosso
lado, com procedência.
**Pronto quando:** os 16 itens do Portfólio têm repositório confirmado ou "não existe" declarado.
**Dependência:** nenhuma. **É a frente mais barata de todas e fecha várias pendências de uma vez.**

**C17 · Modelo de disposição e tombstone**
Ele define 6 disposições finais obrigatórias (`PROMOVER_CANONICO`, `ATUALIZAR_CONTEXTO_PACK`,
`CRIAR_TREINAMENTO_OU_SKILL`, `ARQUIVAR_HISTORICO`, `QUARENTENA_EXIGE_JOAO`,
`REJEITAR_DUPLICADO_BAIXO_VALOR`), máquina de estados de `DISCOVERED` a `VERIFIED`, e **tombstone com
hash e motivo para tudo que é rejeitado** — nada é apagado em silêncio.
Nossas 148 pendências são uma fila sem disposição: não têm estado, owner nem próxima ação.
**Pronto quando:** toda pendência tem disposição, owner e próxima ação. **Dependência:** C8.

---

## O que precisa de decisão antes de começar
1. **C2 — front-matter.** Reverte uma decisão minha. Precisa do seu aval.
2. **C4 — nível acima da uMode.** Só você e o João decidem.
3. **C8 — faixa de numeração de decisões.** Combinar com o João para não colidir.
4. **C12 — as duas classes de cliente.** Plataforma × mentoria/programa é hipótese minha, não fato.
5. **C14 — `_Parceiros` e `05_Financeiro`.** Enumeração de Área é decisão travada; mudar exige aval.

## Fontes e referências
### Documentos consultados
- `C:\Ambientes Virtuais\BrainHub - João Risoléo` — vistoria somente leitura em 04 ago 2026. Vault
  em `umode-os-vault` (repositório `HyTrackWater/umode-os-vault`, 145 commits, último em 28/07/2026
  por `joaorisoleo`). **Nada foi alterado, nenhum commit, nenhum push.**
- Cobertura da leitura declarada no topo deste documento.

## Governança
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**.
Vinicius está alterando tudo neste momento porque está na fase de construção do cérebro — é exceção
declarada de construção, não a regra de operação.
