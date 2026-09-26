---
aliases:
  - "AGORA.md — onde o projeto está, em uma tela"
tags:
  - tipo/governanca
---
# AGORA.md — onde o projeto está, em uma tela

> **Este é o arquivo de orientação.** Serve para retomar o projeto de qualquer lugar, em
> qualquer workspace, sem ler as 2.700 linhas da `STATE.md`.
>
> **Atualizado em: 23 set 2026.** Se esta data não for de hoje ou de ontem, **desconfie** —
> confira o fim do `## Log de sessões` da [`STATE.md`](STATE.md) e o `git log -1`.
>
> *(Este arquivo não fixa hash de commit de propósito: ele envelheceria a cada commit e
> daria falsa impressão de desatualização. A data é o sinal.)*

---

## 1 · O papel

**Eu sou o executor técnico. Eu não decido arquitetura, hierarquia nem regra de negócio** — isso
está travado no `CONTEXT.md` e é decisão do Vinicius. Meu trabalho é **aplicar o padrão com
precisão e não inventar conteúdo**.

**As três regras que não se quebram:**
1. **Zero alucinação.** Sem fonte, o campo é `[a preencher]` — nunca um palpite.
2. **Ausência de fonte é hipótese, não conclusão.** Escrevo *"não encontrei em X"*, nunca
   *"não existe"*.
3. **Todo MD do mesmo tipo tem os mesmos títulos, sempre.** Conteúdo varia por cliente;
   **estrutura nunca varia.** Se o padrão mudar, muda para **toda a classe**, retroativamente.

**Escrita autorizada em um só repositório: `HyTrackWater/brainhub-umode`.** Todos os outros são
somente leitura — sem commit, sem push, sem checkout.

## 2 · O que estamos fazendo

Construindo o **cérebro institucional da uMode e de cada cliente**, em Markdown padronizado,
convergindo para uma plataforma com banco MongoDB.

**A hierarquia travada:**
```
Instituição (Casa uMode OU Cliente)
└── Institucional        identidade, voz, marca, taxonomia
    └── Áreas            8 internas / 14 canônicas de cliente
        └── Subáreas     nomes livres, inclui Produtos
            └── Pessoas  internas na Casa; do cliente, na casa do cliente
```

## 3 · Como estamos fazendo

**Varredura de fonte viva → formalização no padrão → verificação em número → commit.**

- **Fonte viva, nunca export.** Regra travada em 21 set 2026: o export versionado estava
  **seis meses defasado** e dava status errado. **Export não serve para afirmar estado.**
- **Grade de evidência em toda afirmação técnica:** `[C]` verificado na fonte, com a fonte
  citada · `[F]` existe mas atrás de flag · `[P]` proposta minha · `[D]` decisão que não é minha.
- **A lacuna vem antes da conquista.** Todo documento de estado abre declarando **o que ele não
  resolve**.
- **Um caso é anedota, dois é hipótese, três é padrão.** Não promovo antes da hora.
- **Cobertura em número verificável**, nunca em adjetivo.
- **Um assunto tem um dono.** Documento novo que vira autoridade marca o anterior como
  `SUPERSEDED` no que perdeu.

**Ferramentas de verificação**, ambas em `scripts/` e obrigatórias antes de todo commit:
`valida-padrao-corpus.py` (as 4 classes de MD de cliente) e `valida-documentacao.py`
(nenhum `.md` estrutural órfão do manifesto do `START.md` § 1).

## 4 · Onde está cada coisa

> 🔴 **O conjunto completo de documentação — "o time" — está declarado no
> [`START.md`](START.md) § 1**, com a classe de cada arquivo e quem é dono de qual assunto.
> **`python scripts/valida-documentacao.py` confere que nada ficou órfão.**

| Arquivo | O que é | Quando ler |
|---|---|---|
| **`START.md`** | **o manifesto e a ordem de leitura** | primeira mensagem da sessão |
| **`AGORA.md`** | este arquivo — orientação | **primeiro, sempre** |
| `CLAUDE.md` | papel, regras invioláveis, como executar | antes de qualquer tarefa |
| `CONTEXT.md` | decisões de arquitetura travadas | antes de mapear campo ou taxonomia |
| `STATE.md` | histórico completo, sessão a sessão | quando precisar do detalhe de algo |

**Autoridades temáticas** (em `uMode/00_Institucional/_contexto/`):

| Documento | É autoridade sobre |
|---|---|
| [`_espec-pessoas-e-comunicacoes.md`](uMode/00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) | pessoas e comunicações no banco |
| [`_taxonomia-status-cliente.md`](uMode/00_Institucional/_contexto/_taxonomia-status-cliente.md) | o campo `Status` do cliente |
| [`_varredura-2026-09-22-reunioes-compartilhadas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-22-reunioes-compartilhadas.md) | a base de reuniões do Notion |
| [`_proposta-grade-de-areas-revisao.md`](uMode/00_Institucional/_contexto/_proposta-grade-de-areas-revisao.md) | revisão da grade de áreas canônicas |
| [`_varredura-2026-09-21-fontes-e-lacunas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-21-fontes-e-lacunas.md) | fontes rastreadas e lacunas por cliente |
| 🟢 [`_dicionario-permissionamento-uflow.md`](uMode/00_Institucional/_contexto/_dicionario-permissionamento-uflow.md) | **como a permissão do uFlow funciona** — `Includes`/`Excludes`, `scopable`, `entity_configs`, 72 controllers |

> 🔴 **Onde buscar contexto novo no Notion — leia isto antes de abrir qualquer coisa lá.**
> **Cada cliente tem um `_pendencias-e-fontes.md`** em `uMode/_Clientes/<cliente>/00_Institucional/_contexto/`, e ele é **o diário de varredura**:
> **§ 3.1** fontes da carteira inteira já varridas · **§ 3.2** a página daquele cliente · **§ 3.3** sub-páginas dele já abertas · 🔴 **§ 4 fontes conhecidas e AINDA NÃO varridas.**
> **As §§ 3.1 e 4 são iguais nos 48 arquivos** — abrir um só basta para ter o mapa do Notion inteiro. **Não reabra o que a § 3 diz que já foi lido.**

**Protocolos** (em `uMode/00_Institucional/_protocolos/`): `protocolo-varredura-cliente.md` ·
`protocolo-criacao-cliente.md` · `protocolo-gestao-demanda.md` · `protocolo-gestao-rfi.md`.

## 5 · Passos já dados

| Fase | Quando | O que ficou pronto |
|---|---|---|
| **Hierarquia e volumetria** | jun–jul 2026 | 4 níveis travados · 8 áreas internas · 14 canônicas de cliente · template |
| **Replicação total** | ago 2026 | 46 clientes com casa no padrão · migração para Git |
| **Banco** | ago 2026 | espec de collections, campos e relações — desenho é nosso, implementação é do Bergson |
| **Varredura de fonte viva** | 19–21 set 2026 | 15 fontes · CAEDU e Puket fechadas · `protocolo-varredura-cliente.md` escrito |
| **Carteira inteira** | 22 set 2026 | **48 de 48 clientes** · taxonomia de `Status` travada |
| **Base de reuniões** | 22 set 2026 | 1.161 reuniões achadas · Recco e Luiza Barcelos varridas |
| **Modelo de documentação** | 22 set 2026 | **8 classes travadas · manifesto declarado no `START.md` § 1 · verificável por script** |
| **Pessoas e ferramentas** | 22 set 2026 | **enum de 7 módulos · atendimento de 17 contas · razão de pessoas datado em 17 clientes** |
| 🟢 **Permissionamento do uFlow** | **23 set 2026** | **as 10 matrizes lidas · o mecanismo virou autoridade (`_dicionario-permissionamento-uflow.md`) · os 4 acervos do Notion mapeados** |
| 🟢 **O grafo e o Obsidian** | **23 set 2026** | **2.840 links de área religados · órfãos 74 → 41 · `.obsidian/` versionado com 15 cores de entidade** |
| 🟢 **Ciclo da pergunta** | **23 set 2026** | **destinatário nomeado · estados `aprovada`/`recusada`/`alterada` com justificativa obrigatória** |

**Cobertura hoje, medida:** 🔺 **números refeitos em 23 set 2026 rodando os validadores.**
Os anteriores traziam três divergências — contagem de pendência em três arquivos diferentes,
a § 6 congelada uma sessão atrás, e a fila de perguntas inflada.

| | Número | Como se mede |
|---|---:|---|
| Clientes no corpus | **48** | pastas em `_Clientes/` |
| MDs em `uMode/` | **2.808** | `find` |
| `contexto-area.md` conformes | **694 / 694** | `valida-padrao-corpus.py` |
| `institucional.md` · `jornada.md` · `pessoas.md` | **50 · 49 · 49** | idem |
| Demandas | **999** — 994 de cliente + 5 da Casa | idem · 1 staging `SUPERSEDED` |
| RFIs | **87** | idem · 1 staging `SUPERSEDED` |
| 🟢 **Fichas de pessoa** | **479** — 402 de cliente + **77 da Casa** | `gera-fichas-pessoa.py` · `gera-fichas-umoder.py` |
| Fichas de ferramenta | **27** | `gera-fichas-ferramenta.py` |
| Soluções do Portfólio | **16** | `03_Produto-e-Solucoes/` |
| `integracao.md` | **11** | 5º MD de cliente |
| `.md` estruturais classificados | **90 / 90** | `valida-documentacao.py` ✅ |
| Atas de reunião lidas por inteiro | **8 de 1.162** | 🔺 a base tem 1.162, não 1.161 |
| Páginas de cliente abertas no Notion | **16 de 49** | |
| Matrizes `Perfil de Usuário` lidas | **10 de 10 — FECHADO** | |
| Decisões pendentes | **778** | `_pendencias-gerais.md` — **triadas na § 0** |
| Perguntas na fila | **46** — 43 abertas · 3 respondidas | `_perguntas-para-o-vinicius.md` |
| 🚨 Credenciais expostas conhecidas | **3** | NK STORE · Lofty Style · a própria plataforma |

### 5.1 · 🟢 O grafo — saneado em 23 set 2026

**O corpus agora é um cérebro navegável, e isso passou a ser verificável.**

| | Antes (22 set) | **Agora (23 set)** |
|---|---:|---:|
| Arquivos no grafo | 2.420 | **2.421** |
| Com alguma ligação | 2.351 · 97,1% | **2.382 · 98,4%** |
| **Órfãos** (ninguém cita) | 74 · 3,1% | **41 · 1,7%** |
| **Links de área que não resolviam** | **2.840** | **0** |
| Links quebrados | 20 | **16 — nenhum nosso** |
| Nomes ambíguos | 2 | **1** |

**Três defeitos reais foram encontrados e corrigidos** — nenhum deles aparecia em número antes:

1. 🔴 **`gera-conexoes.py` escrevia um `../` a mais** nos links de área de
   `institucional/jornada/pessoas.md`. **2.274 links em 145 arquivos apontavam para fora da pasta
   do cliente.** Era a membrana Instituição↔Área — **a ligação mais importante da hierarquia, e
   ela estava desligada em todos os 48 clientes.**
2. 🔴 **`00_Institucional` entrava na lista de áreas.** Gerava **824 links** para um
   `contexto-area.md` que nunca existiu ali. `00_Institucional` é o **nível 1** da hierarquia,
   não uma área.
3. 🔴 **Três entidades definidas não tinham camada de ligação e ficavam órfãs:** as **16 Soluções**
   do Portfólio, os **11 `integracao.md`** e as **5 demandas da Casa**.

**Os 41 órfãos que restam são legítimos e nomeados:** 20 do `_template_cliente` e outros templates
(molde não é nó), 10 do `brainwave/` e 6 do `_boilerplate/` (frentes paralelas, com governança
própria), 2 staging `SUPERSEDED`, e `CLAUDE.md`/`README.md`/`_indice/README.md`.
**Nenhum órfão é registro de cliente.**

**Os 16 links quebrados que restam não são nossos:** 9 estão no
`_recebido-2026-08-18-context-pack-brainhub-2.0.md`, **documento externo do João que não se edita**,
apontando para caminhos do vault dele; 1 é a proposta no `_inbox-hermes` apontando para o mesmo
vault; e **6 são falso-positivo** — a palavra `[[wikilinks]]` escrita dentro de texto que explica
o próprio sistema de links.

### 5.3 · 🔴 O esqueleto que ainda não tem carne — 657 áreas vazias

**97% dos `contexto-area.md` estão praticamente vazios: 657 de 680.**
**45 dos 49 clientes têm ZERO área preenchida.** Com conteúdo, só: **Casa 8/8 · CAEDU 7/14 ·
Osklen 7/14 · Oficina Reserva 1/14**.

🟢 **É esperado.** A replicação criou a **estrutura**; o **conteúdo** de uma área só existe se
alguém varreu aquela área naquele cliente. 🔴 **E a causa raiz é fonte ausente, não fila de
trabalho** — a página do cliente quase nunca traz área.

🔵 **O caminho é a CAEDU:** as 54 transcrições são a fonte que preenche as 14 áreas de um cliente.
**Se funcionar nela, vira método.** **Itens 572–575.**

### 5.2 · 🟢 Abrir no Obsidian — configurado em 23 set 2026

**Antes de hoje o repositório não tinha `.obsidian/`**: abria como cofre cru, sem cor, com órfão
e link não-resolvido poluindo a tela. Agora tem, e **está versionado** — quem clonar vê o mesmo.

🟢 **Desde 23 set 2026, todo `.md` tem `tags` em frontmatter** — `tipo/`, `cliente/`, `status/`
e `area/`. **É como se filtra o cérebro.** Na busca do grafo ou no `Ctrl+O`:

| Para ver | Digite |
|---|---|
| **só os clientes ativos** | `tag:#status/ongoing` |
| tudo de um cliente | `tag:#cliente/caedu` |
| todas as pessoas | `tag:#tipo/pessoa` |
| as áreas de Qualidade da carteira | `tag:#area/qualidade` |
| o que está em churn | `tag:#status/churn` |

**Os 17 grupos de cor do grafo agora são consultas de tag**, não de caminho.

🟢 **E todo `.md` tem `aliases` copiado do H1** — a busca
rápida (`Ctrl+O`) mostra *"Qualidade · Contexto de área — Caedu"* em vez de 694 `contexto-area`
idênticos. 🔴 **O rótulo do GRAFO continua sendo o nome do arquivo** — lá quem desambigua é a cor.

**15 grupos de cor, um por entidade** (`.obsidian/graph.json`): Instituição · Área · Pessoa ·
Demanda · RFI · Solução · Ferramenta · Integração · Jornada · Autoridade · Protocolo · Registro ·
Diário do cliente · Governança.

🔴 **A trava que faz isso funcionar:** `gera-conexoes.py` escreve **link relativo de markdown**,
nunca wikilink por nome. **Há 694 arquivos chamados `contexto-area.md` e 49 chamados `pessoas.md`**
— com wikilink por nome o Obsidian erraria o alvo em massa. Por isso a ambiguidade caiu de
2.840 referências para **1**.

## 6 · O que está sendo feito agora

🔵 **Frente ativa: varredura cliente a cliente, ABRINDO A PÁGINA de cada um.**

> 🔴 **A regra que mudou em 22 set 2026:** até aqui eu varria **bases** (SQL). A página
> do cliente **não é base** — e é onde vivem o **`cargo`**, a **área**, as **pessoas de
> diretoria**, as **sub-páginas de ata** e, em pelo menos um caso, uma **credencial de
> produção em texto claro**. **Consulta SQL não alcança nada disso.**

**O modelo, travado pelo Vinicius em 22 set 2026: ENTIDADE É ARQUIVO.**
*"praticamente tudo que for uma entidade é arquivo? Ou seja, ferramenta, pessoas, empresas,
áreas, demandas, RFIs, tudo... As reuniões, contextos gerais, e-mails, tudo isso vai estar de
alguma forma ligada a esses nós maiores."*

| Entidade | É arquivo? | Quantos | Ligada no grafo? |
|---|:-:|---:|:-:|
| Instituição | ✅ | 50 | ✅ |
| Área | ✅ | 694 | 🟢 **religada em 23 set** |
| Demanda | ✅ | 999 | ✅ |
| RFI | ✅ | 87 | ✅ |
| Pessoa | ✅ | **242** | ✅ |
| Ferramenta | ✅ | **27** | ✅ |
| **Solução do Portfólio** | ✅ | **16** | 🟢 **religada em 23 set** |
| **Integração** | ✅ | **11** | 🟢 **religada em 23 set** |
| Reunião / ata · E-mail · Agente | 🔴 **não** | 1.161 · 92 · 4 conhecidos | 🔴 **não existem como nó** |

> 🔺 **Corrigido em 23 set 2026.** Esta tabela trazia Pessoa 137 e Ferramenta 16 — números de uma
> sessão atrás — e Demanda 1.021 / RFI 102, que contavam os `_indice.md` gerados como se fossem
> registro. **Agora bate com o disco.**

**Páginas de cliente abertas: 16 de 49** — CAEDU · Osklen · NK STORE · Reserva · VIX ·
Lofty Style · Puket · NV · Oficina Reserva · Cambos · Luiza Barcelos · Moda Objetiva · Baw ·
Loungerie · Lenny Niemeyer · Recco.

### 🟢 RESOLVIDO em 23 set 2026 — o acesso ao Notion da uMode

O conector foi reautorizado no workspace **`uMode Mode's Notion`**. A causa era **escolha de
workspace na tela de OAuth**, não conta errada: o token vinha emitido para
`Notion de Vinícius Risoléo` (pessoal, 2 usuários).

⚠ **Lição de diagnóstico, para não repetir:** **`get-teams` não serve para validar acesso.**
Depois de reconectado ele devolveu `General`, `Inovação`, `Kudos`, `Recrutamento` — **nenhum dos
teamspaces reais.** Quem provou o acesso foi **uma busca por termo conhecido** (`Caedu`, que
devolvia zero e passou a devolver o acervo). **Item 501.**

### 🚨 CAEDU — a dor histórica dela mudou de natureza em 23 set 2026

**Fonte nova, fora do Notion:** `Extração Caedu - 28ago26.json` em `Downloads` — **48.551 linhas,
42.488 produtos, 17 campos**, datada de 28/08/2026.

🔴 **`Griffe › Linha › Grupo › Subgrupo` NÃO aninha como árvore nos dados da própria CAEDU.**
23 de 33 `Linha` têm mais de uma `Griffe`; 75 de 231 `Subgrupo` têm mais de um `Grupo`; `BOTTOM`
aparece sob **24 `Linha`**. **1.015 combinações reais num cartesiano de 8.828.820 — 0,01%.**
`[P]` **Comporta-se como facetas, não como cascata.**

🔴 **E `Griffe`/`Linha` são campos do LINX, enquanto `Grupo`/`Subgrupo` são do uFlow** — a
hierarquia pedida **atravessa dois sistemas**. **A dor de taxonomia é, no mecanismo, dor de
integração.**

⚠ **Isso põe em dúvida o precedente da Loungerie** como caso pronto para a CAEDU.
**Registro completo:** [`_varredura-2026-09-23e`](uMode/00_Institucional/_contexto/_varredura-2026-09-23e-a-dor-da-caedu-nao-e-arvore.md) · **itens 492–500.**

### 🔴 O que mudou em 23 set 2026, e o próximo agente precisa saber antes de tudo

**1 · As dez matrizes de permissão estão lidas. O conjunto fechou.**
Duas conclusões minhas caíram no processo: o `Fale com o Suporte` **não é padrão** (4 bloqueiam
× 6 liberam) e a dor de **excluir variante é configuração, não limitação** da plataforma — a
Recco tem a linha liberada.

**2 · O mecanismo de permissão virou autoridade.**
O `📕 Manual do Permissionamento` estava na minha lista de fontes não varridas **enquanto eu
registrava como pergunta uma coisa que ele responde desde 2024.** Virou
[`_dicionario-permissionamento-uflow.md`](uMode/00_Institucional/_contexto/_dicionario-permissionamento-uflow.md).

**3 · 🔴 Documentação de cliente mora em QUATRO lugares no Notion, não em um:**

| Acervo | Estado |
|---|---|
| `Databases / Mapa de Clientes` | 🟢 é por onde a varredura anda — **16 de 49 abertas** |
| **`uFlow / Documentação de Setup - PLM / CLIENTES`** | 🔴 **9 clientes, só a NV tocada** |
| `Operação de Clientes / **Arquivo** / Área de CX / Documentação CX` | ⚠ **arquivado** · 30 docs listados, nenhum aberto |
| **`Documentação Homologada`**, dentro do cliente | ⚠ vista na Cambos · **não sei quem mais tem** |

🔴 **NK STORE e VIX, que eu considerava bem varridas, têm um SEGUNDO endereço nunca aberto.**

**4 · 🚨 Há um terceiro risco de credencial, e ele é da plataforma.**
Uma página chamada **`Credenciais`** em `uFlow / Setup - PLM`, seção `Nova uFlow/uRocket`.
🔴 **NÃO a abri, de propósito** — o título basta para registrar o risco, e abrir traria segredo
para dentro do contexto. **Item 480 do `_pendencias-gerais.md`.**

**5 · 🔴 Existe segmentação de conta — `SaaS`, `Enterprise`, `SMB` — e nenhuma ficha de cliente
do corpus carrega segmento.** Os 48 vêm sendo tratados como um bloco só.

## 6-bis · 🟢 A camada de fato atômico (23 set 2026)

**O que mudou:** os MDs de entidade ganharam um bloco **`## Fatos`** no topo —
**3.393 fatos em 769 arquivos** (`institucional.md` 49 · `jornada.md` 48 ·
`contexto-area.md` 672), no formato `- chave: valor — [fonte · data]`.

🔴 **Decisão de desenho, e ela vale para todo MD de entidade daqui em diante:
o fato NÃO substitui a prosa — convive com ela.** A prosa é para pessoa (contexto,
citação, nuance); o bloco `## Fatos` é para máquina. **O agente de transcrição cruza
contra `## Fatos`, nunca contra a prosa.** Formato travado no
[`protocolo-fato-atomico.md`](uMode/00_Institucional/_protocolos/protocolo-fato-atomico.md).

| | |
|---|---:|
| fatos com fonte e data | **1.396** (41%) |
| 🔴 fatos `[sem fonte]` — **ninguém procurou** | **63** (2%) |
| 🟢 **clientes com ZERO `[sem fonte]`** | **34 de 48** |
| 🟢 ausência VERIFICADA no corpus | **1.921** (57%) — fonte nomeada e data |
| 🟢 **ausência VERIFICADA** — `[não consta em: X · data]` | **2** — só a CAEDU |
| chaves de vocabulário fechado | **35** |
| nomes indexados por e-mail, tirados do próprio corpus | **617** |

🟢 **E a identidade fechou.** O bloqueio era que nenhum dos 49 valores de `atendimento`
resolvia para e-mail. **Achei a base de pessoas que faltava** — `collection://c82a689c…`, a que o
campo `Atendimento 2024` aponta, **e que não é a `uModers`** — e preenchi 16 fichas da Casa.

| `atendimento` nos 49 clientes | |
|---|---:|
| 🟢 resolvido para `pessoa:<e-mail>` | **19** |
| 🔴 **ambíguo, e eu NÃO escolhi** — `Pedro` (6), `Fernanda` (3) | **9** |
| ⚠ `SMB` — segmento, não pessoa | 7 |
| campo vazio na origem | 24 |

🟢 **A CAEDU está com ZERO fatos `[sem fonte]`.** Os dois que restavam não foram
preenchidos — foram **verificados como ausentes em dois instantes** (base viva 23/09/2026 e
export de 04/03/2026 no vault) e agora dizem onde se procurou. 🔴 **`Receita Anual` está
preenchida em 2 dos 49 clientes; `Data Ativação` em 6** — não é lacuna da Caedu, é campo que
a operação não preenche. ⚠ **137 ocorrências de "campo vazio na base" em 44 clientes não
dizem QUAL base** — e ausência sem fonte nomeada não é ausência citável (item 618).

🟢 **A CAEDU resolve ponta a ponta:** `julianne.dias@` · `pedro.murillo@` · `andrea.holmer@`.
🔴 **E a Andrea está `Inativo` na base** — no cliente do teste da semana que vem (item 605).
🔴 **`Atendimento 2025` é `select`, não `relation`** — enquanto for, nunca vai resolver
sozinho (item 608). **Itens 598–610.**

**Dono:** `scripts/gera-fatos.py` · **Guarda:** `scripts/valida-fatos.py` (acusa chave fora do
vocabulário, forma e data inválidas — **não corrige**). **Rodar entre `gera-conexoes.py` e
`gera-frontmatter.py`.**

## 7 · Próximos passos, em ordem

> 🔴 **Antes de qualquer um destes: abra o `_pendencias-e-fontes.md` do cliente em questão e
> leia a § 3.** É o diário do que já foi varrido. **Repetir busca é o desperdício que o
> Vinicius nomeou explicitamente.**

> 🚨 **Os passos 1, 2 e 4 estão BLOQUEADOS** enquanto o Notion não for reconectado na conta da
> uMode (§ 6). **O que dá para fazer agora sem ele:** os 3 arquivos de CAEDU em `Downloads`
> (item 499), o `integracao.md` que falta à CAEDU (item 500), e as decisões 492–497.

0. 🚨 **CAEDU — prioridade declarada pelo Vinicius em 23 set 2026:** *"preciso finalizar o plano
   de ter TUDO da CAEDU contextualizado para o teste do brain da empresa na próxima semana."*
   **Distância medida hoje:** 61 MDs · 26 demandas · 4 RFIs · 10 fichas de pessoa · **~158
   campos `[a preencher]`** (5 em `institucional`, 4 em `jornada`, 15 em `pessoas`, ~134 nos 14
   `contexto-area.md`) · **`integracao.md` não existe.**

1. ✅ **`Setup - PLM / CLIENTES` — VARRIDO em 23 set 2026, e rendeu pouco.**
   🔴 **4 das 8 páginas estão vazias, inclusive a CAEDU.** VIX (2 páginas), NK Store (1) e
   StudioZ (1) têm pouco. **Só a RESERVA tem acervo real:** base `CENTRAL DE DOCUMENTAÇÕES`
   com **18 documentos** de regra de negócio, integração e operação — **o acervo por cliente
   mais estruturado que apareceu até hoje, e existe só para ela.**
   🔵 **O que sobrou deste caminho:** abrir os 18 da RESERVA e as 4 páginas de VIX/NK/StudioZ.
   **Itens 505 e o registro `_varredura-2026-09-23f`.**
2. 🔵 **As 33 páginas de cliente que faltam** em `Databases / Mapa de Clientes`. Segue sendo a
   fonte de maior rendimento: resolve `cargo`, `área` e a camada de liderança de uma vez.
   🚨 **Toda página aberta é varrida também em busca de segredo.**
3. 🚨 **Credenciais — agora são três.** NK STORE (lugar exato) · Lofty Style (lugar exato) ·
   **`Credenciais` do uFlow, não aberta.** **A rotação é ação do Vinicius, não minha.**
4. 🔵 **As seções do `Setup - PLM` que respondem dor aberta:** `Como é o processo de
   integração?` e `Logs e integração` (dor de CAEDU, VIX, Moda Objetiva, Luiza Barcelos) ·
   `Automações` (os IDs `#1136`, `#1175`, `#989` do playbook da Cambos) · `Traduções` (onde o
   apelido interno é operado) · `Ficha de Produto` e suas 7 sub-páginas.
5. 🔴 **Distribuir as perguntas.** São **46 na fila — 43 abertas**, em
   [`_perguntas-para-o-vinicius.md`](uMode/00_Institucional/_contexto/_perguntas-para-o-vinicius.md).
   🔺 **Corrigido em 23 set:** esta linha dizia 63.
   🔴 **As 43 estão com destinatário `⚠ a distribuir`** — e isso é de propósito. O Vinicius disse
   em 23 set 2026 que *provavelmente não será ele quem responde*; **assumir que são dele seria
   inventar um dado.** Atribuir dono é decisão, e não é minha.
   ✅ **A segmentação de conta saiu da fila em 23 set 2026** — respondida por fonte, não por
   pergunta: `Enterprise` (Grupo 1) · `Médios` (2) · `SMB` (3). **Item 502.**
   **As que sobram mais caras:** se `excluir variante` é mesmo só permissão · se a Cambos é
   fornecedora de marcas e não marca · qual campo manda, `Status` ou `Etapa`.
6. 🔵 **Fechar as 3 entidades que faltam: reunião, e-mail e agente.** Enquanto forem prosa, o
   grafo não liga ata a pessoa nem demanda a conversa.
7. ✅ **`Participantes` das reuniões — RESOLVIDO em 23 set 2026, e o resultado é NEGATIVO.**
   🔴 **Não dá presença nominal.** São 1.694 presenças em **25 IDs distintos**, e **24 não
   resolvem** — 99,2% ficam anônimas. Verificado por três vias; **a via está esgotada na API.**
   🔵 **A única que resta é humana:** abrir UMA reunião no Notion pela UI mostra o nome.
   **Os 5 uuids de topo somam 88% das presenças — cinco olhadas resolvem.**
   🟢 **O que saiu de novo:** intensidade de atendimento por conta (Luiza Barcelos 126 · NK STORE
   111 · Osklen 101 · … · **Caedu 35**). **Itens 551–561.**
8. 🔴 **Varrer `Segmentação Grupos` e `Atendimento 2024`** — a primeira ganhou urgência: há
   três rótulos de segmento (`SaaS`, `Enterprise`, `SMB`) sem dono no corpus.
9. 🔴 **Criar o campo `Data de Churn`** — segue sendo a lacuna mais cara do corpus.
10. 🔵 **Retomar a CAEDU** assim que as ~50 transcrições reais chegarem. 🟢 **E há precedente
    de método:** o `Playbook Cambos` nasceu de transcrição de treinamento processada com IA, em
    23/03/2026. **Já rodou uma vez.**
11. 🔴 **AO FIM DE TODA A VARREDURA, e só ao fim: o `HOJE` dos uModers.**
    **Decisão do Vinícius em 22 set 2026**, textual: *"os cargos dos demais também terão
    atualizações. Isso vai ser uma coisa recorrente e que teremos que corrigir somente ao
    final de toda a varredura: como é o HOJE dos uModers."* `[D]`

    🔴 **A regra que vale até lá: cargo lido em ata é cargo NAQUELA DATA, nunca cargo de
    hoje.** Toda ficha de uModer que receber cargo de uma fonte datada **cita a data junto**.
    ⚠ **Não corrigir de um em um pelo caminho** — ele pediu de uma vez, no fim, e corrigir aos
    pedaços só cria versões parciais conflitantes.

    **Já confirmado por ele em 22 set 2026 — quatro saídas:** Dalker Walter (Diretor de
    Operações) · Rafael Renaldim (Gerente de Experiência do Cliente) · Tais Moser
    (Customer Success) · Saulo (CTO). ⚠ **Data de saída de nenhum deles é conhecida.**

## 7-bis · 🔴 A TRIAGEM — leia antes de pegar qualquer item da § 8

**As pendências passaram de 557 e o arquivo virou ilegível como fila.** Em 23 set 2026 foi
inserida a **§ 0 de triagem** no topo do
[`_pendencias-gerais.md`](uMode/00_Institucional/_contexto/_pendencias-gerais.md), com o placar e
a **lista curta do que trava a CAEDU**. **Nenhum item foi apagado ou renumerado.**

| Balde | Itens |
|---|--:|
| ✅ Já resolvidos | 50 |
| 🚨 Segurança — **rotação é ação do Vinicius** | 18 |
| 🔵 Citam a CAEDU — **~12 travam de verdade** | 37 |
| 🔴 Decisão do Vinicius | 50 |
| ⚪ Arquivo / técnico — **não é para agora** | 402 |

🔴 **Regra que passa a valer: não abrir fonte nova enquanto a CAEDU não fechar.**
🔴 **E a métrica reportada passa a ser COMPLETUDE, não contagem de arquivo.**
**Hoje: CAEDU 0 de 259** — 158 lacunas de contexto + 100 cargos + 1 `integracao.md`.

## 8 · Decisões esperando o Vinicius

🔴 **O dono deste assunto é o [`_pendencias-gerais.md`](uMode/00_Institucional/_contexto/_pendencias-gerais.md)
— **487 itens datados** (numerados até 491, com saltos). 🔺 **Corrigido em 23 set 2026:** esta
linha dizia 349 e o `START.md` dizia 248. **Três números para o mesmo assunto** — exatamente o
defeito que o manifesto proíbe. **A contagem é feita no arquivo, não repetida de memória.** **Não crie tabela de pendência aqui nem em lugar nenhum: escreva lá.**

### 8.0 · 🔴 O que só ele responde tem UM caminho, e só um

**Decisão dele em 22 set 2026:** *"em dado momento, você montará uma lista de coisas que eu tenho
que perguntar e vou dar um jeito de responder ou por áudio ou numa transcrição de reunião mesmo."*

| Onde | O que é |
|---|---|
| `_Clientes/<Cliente>/…/_pendencias-e-fontes.md` **§ 2.1** | **onde a pergunta nasce** |
| [`_perguntas-para-o-vinicius.md`](uMode/00_Institucional/_contexto/_perguntas-para-o-vinicius.md) | **a lista que ele responde** — colhida pelo **mesmo script** |
| [`protocolo-perguntas-ao-vinicius.md`](uMode/00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md) | **o processo** — 🔴 **não criar um segundo** |

🔴 **A regra que decide:** pergunta é só o que **nenhuma fonte** responde. Dúvida que uma fonte
responde **não é pergunta — é varredura que falta fazer.**

### 8.0.1 · 🟢 O ciclo da pergunta, ampliado em 23 set 2026

**Pedido do Vinicius, textual:** *"as perguntas estão sendo acumuladas para coisas que não se têm
respostas... provavelmente não serei eu que responderei, mas temos um local organizado para depois
distribuir as perguntas e até considerar o fato de algumas delas nem terem que ser respondidas.
Então poderão ser aprovadas, recusadas ou alteradas com justificativas pra complementar o contexto."*

| Estado | O que significa | Justificativa obrigatória? |
|---|---|:-:|
| 🔴 `aberta` | ninguém decidiu ainda | — |
| 🟢 `aprovada` | a resposta virou contexto e já vale | ✅ o que passa a valer |
| ⚪ `recusada` | **decidiu-se que não precisa de resposta** | ✅ **por que não precisa** |
| 🟡 `alterada` | a pergunta mudou de forma ou escopo | ✅ como mudou e por quê |
| 🔵 `respondida` | respondida por fonte ou por pessoa | ✅ a resposta, com procedência |

🔴 **`recusada` é resposta, não desistência.** *"Isso não precisa ser respondido porque X"* é
conhecimento tão útil quanto a resposta — **e impede que a mesma dúvida volte na varredura
seguinte.** Por isso a justificativa entra no corpus nos quatro estados de saída.

**Cada pergunta carrega `quem responde`.** Processo completo em
[`protocolo-perguntas-ao-vinicius.md`](uMode/00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md) § 3.1 e § 4.1.

⚠ **Quando levar a lista até ele não é decisão minha.** Ele disse *"pensaremos nisso quando
chegar o momento"*. **Minha obrigação é manter a fila pronta e avisar se ela travar a varredura.**

### 8.1 · Dado sensível: `T0` / `T1` / `T2`

> 🔺 **Corrigido em 22 set 2026.** Até aqui eu usava rótulos meus — `INTERNAL_ONLY`,
> `NEVER_TO_THIRD_PARTY`. **Era uma segunda taxonomia para a mesma coisa**, o defeito que a
> gente critica. **O vocabulário é `T0`/`T1`/`T2`**, o mesmo que o João usa no vault, com
> definição operacional já registrada (item 96 do `_pendencias-gerais.md`).

| Tier | O que é | O que entra no corpus |
|:-:|---|---|
| **`T2`** | **equipe** — o padrão | nome, cargo, área, papel, escopo, marco, decisão, prazo |
| **`T1`** | **restrito** | valor de proposta, preço, margem, escopo confidencial — **entra, e fica só no `_contexto/` daquele cliente** |
| **`T0`** | **privado** | 🔴 **nunca entra por valor.** CPF, telefone pessoal, senha, token, string de conexão. **Entra por referência:** registro que existe e **onde** |

> `[P]` **Distinção que fiz em 22 set 2026 e que precisa do seu aval:** **e-mail CORPORATIVO é `T2` e entra** — é dado de contato de trabalho e é **a chave de identidade** que destrava a deduplicação de pessoa (item 252). **E-mail pessoal segue `T0`.** Telefone e CPF seguem `T0` em qualquer caso. **Precedente que já existia no corpus:** há ficha nomeada por e-mail na Reserva desde antes desta sessão.

**Onde isso vive, por cliente:** `_Clientes/<Cliente>/00_Institucional/_contexto/`
**`_pendencias-e-fontes.md`** — é a autoridade sobre as pendências **daquele** cliente e sobre
**onde já se varreu**. Gerado por `scripts/gera-pendencias-e-fontes.py`.

⚠ **O que NÃO fiz:** não copiei mecanismo nenhum do vault (a restrição continua valendo).
**Adotei o rótulo, que é vocabulário comum** — e vocabulário comum é exatamente o ponto.

## 9 · Como manter este arquivo vivo

**Este arquivo mente rápido se ninguém o atualizar.** A regra:

- **O ritual de fechamento completo está no [`START.md`](START.md) § 4** — são seis passos:
  `gera-conexoes.py`, `valida-indexacao.py`, `valida-padrao-corpus.py`,
  `valida-documentacao.py`, `STATE.md` e **este arquivo**.
  ⚠ **Corrigido em 23 set 2026:** esta linha mandava rodar um `propaga.py` que
  **não existe mais** — virou `scripts/valida-padrao-corpus.py`.
- **Toda sessão que gera commit atualiza `AGORA.md`** — no mínimo a data, os números da § 5 e as
  listas das § 6 e § 7.
- **`AGORA.md` é resumo, `STATE.md` é histórico.** O que aconteceu vai para a `STATE.md`;
  o que **vale agora** vive aqui. **Nada de histórico neste arquivo.**
- **Se este arquivo divergir da `STATE.md`, a `STATE.md` ganha** — e aí este aqui está com
  defeito e precisa ser corrigido na hora.
