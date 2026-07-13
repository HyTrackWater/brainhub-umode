# brainwave/CONTEXTO.md — Referência de produto para prompts do BrainWave

> **Isto não é lido pelo BrainWave.** O BrainWave é uma ferramenta tipo Lovable — sem acesso a
> este repositório, sem leitura de arquivo nenhum. Ele só aplica, direto no frontend, o que o
> Vinicius digita nele. Este documento é a fonte que **nós** usamos aqui pra derivar o texto
> dos prompts de tarefa. É referência de quem escreve o prompt, não instrução de quem executa.

## A pasta `brainwave/`

Guarda o histórico de toda instrução de frontend já dada ao BrainWave. Convenção:
- `CONTEXTO.md` (este arquivo) — referência de produto, sempre atual, nunca numerado.
- `01-esqueleto.md`, `02-...md`, `03-...md` — uma tarefa por arquivo, em ordem cronológica,
  numeração nunca reaproveitada mesmo se uma tarefa for abandonada.
- Cada arquivo de tarefa tem uma seção `## Resultado`, preenchida depois — **o Vinicius é a
  interface entre o BrainWave e este repositório**: ele cola o prompt na ferramenta, e quando
  ela responde, traz o resultado de volta pra cá pra registrar. Eu (ou quem estiver na sessão)
  nunca invento o que o BrainWave fez — só registro o que o Vinicius reportar.

## Fonte de verdade pra quem escreve o prompt

Antes de escrever ou revisar um prompt pro BrainWave, releia por inteiro: `CLAUDE.md`,
`CONTEXT.md`, `STATE.md`. Eles definem a hierarquia, as regras de padronização e o estado atual
do projeto — o prompt precisa refletir isso corretamente, já que o BrainWave não vai conferir
sozinho.

**Regra mais importante deste arquivo:** o repositório é a fonte de verdade. `uMode/` já tem
toda a estrutura, os templates e o conteúdo real de 4 clientes-piloto (Lofty Style, Cambos,
Luiza Barcelos, Moda Objetiva) formalizados em Markdown padronizado. As telas que você vai
construir **leem e escrevem nesses mesmos arquivos** — não são um sistema paralelo com dado
próprio. Se existe um `docs/brainhub_plataforma.html` no repositório, ele é um protótipo
histórico anterior a este brief e **não é fonte de estrutura** — não copie dele.

## O que é a plataforma

Uma interface visual sobre o cérebro institucional da uMode: a hierarquia fixa
`Instituição (Casa ou Cliente) → Institucional → Áreas → Subáreas (inclui Produtos) → Pessoas`,
mais duas entidades transversais — `Demanda` e `RFI` — que registram trabalho e mudança de
contexto. Tudo isso já vive como Markdown padronizado; a plataforma é a camada de visualização,
edição e criação por cima.

## As 6 abas de navegação

**Alterado em 13 jul 2026 (task 03, confirmada pelo Vinicius):** "Instituições" e "Pessoas"
deixaram de ser abas de topo independentes. No lugar, existem duas abas de topo — **uMode** e
**Clientes** — cada uma com a mesma estrutura interna fixa em 4 sub-abas: **Instituições ·
Áreas · Subáreas · Pessoas** (Subáreas presente porém desabilitada — sem template/dado ainda).
A aba uMode tem só 1 instituição (a Casa); a aba Clientes lista os clientes (hoje 4) na sua
sub-aba Instituições, e escolher um define o "cliente ativo" que escopa o que aparece nas
sub-abas Áreas e Pessoas daquela aba, até outro cliente ser escolhido. Ver
`brainwave/03-uMode-e-clientes.md` pro prompt completo.

**Alterado em 13 jul 2026 (task 04, confirmada pelo Vinicius):** o "cliente ativo" da aba
Clientes precisa ficar visível e trocável **de dentro de qualquer uma das 4 sub-abas** — um
seletor fixo no topo, não só clicável via cartão em Instituições. Sem cliente ativo escolhido,
Áreas e Pessoas mostram estado vazio ("selecione um cliente"), nunca uma lista misturada de
todos os clientes. A sub-aba Pessoas (com cliente ativo já escolhido) ganha também um filtro
**opcional** por Área, por padrão "todas". A aba uMode não tem esse seletor — só 1 instituição,
sem necessidade de escolha. Ver `brainwave/04-seletor-cliente-ativo.md` pro prompt completo.

| Aba | Lista | Abre (detalhe) | Navega pra | Cria |
|---|---|---|---|---|
| **uMode** ↳ Instituições | Só a uMode (Casa), 1 cartão | `institucional.md` da Casa | Sub-abas Áreas/Pessoas abaixo, já no escopo Casa | Não é fluxo de uso comum |
| **uMode** ↳ Áreas | As 8 internas | `contexto-area.md` da Casa | Produto conectado · Pessoas da área · Demandas com Origem/Destino nessa área | Não é fluxo de uso comum — lista de áreas é fixa/travada em `CONTEXT.md` |
| **uMode** ↳ Subáreas | *(desabilitada — sem template/dado ainda)* | — | — | — |
| **uMode** ↳ Pessoas | Fichas da Casa (`uMode/00_Institucional/_pessoas/`), em cartão (nome/email/área) | *(tela de detalhe ainda não construída — fora do escopo da task 03)* | — | Nova ficha — `protocolo-gestao-pessoas.md` |
| **Clientes** ↳ Instituições | Cada Cliente (hoje: 4 pilotos), em cartão | `institucional.md` + `jornada.md` + `pessoas.md` daquele cliente | Define o "cliente ativo" das sub-abas Áreas/Pessoas abaixo | Novo cliente — segue `uMode/00_Institucional/_protocolos/protocolo-criacao-cliente.md` (5 passos) |
| **Clientes** ↳ Áreas | As 14 canônicas do cliente ativo | `contexto-area.md` do cliente ativo (hoje quase tudo `[a preencher]` — esperado) | Produto conectado · Pessoas da área · Demandas com Origem/Destino nessa área | Não é fluxo de uso comum |
| **Clientes** ↳ Subáreas | *(desabilitada — sem template/dado ainda)* | — | — | — |
| **Clientes** ↳ Pessoas | Pessoas listadas em `pessoas.md` do cliente ativo, em cartão (nome/email/área), com filtro opcional por Área (task 04) | *(tela de detalhe ainda não construída — fora do escopo da task 03)* | — | Nova ficha — `protocolo-gestao-pessoas.md` |
| **Produtos** | Os 16 do Portfólio (`CONTEXT.md` → "Decisão: camada Produto na hierarquia") — 9 voltados ao cliente + 7 internos | Descrição · Área conectada (`conecta_area_cliente`) · clientes que usam (via "Módulos contratados" de cada `institucional.md`) | Área · Agentes que rodam nele (ver Agentes) | Não é fluxo de uso comum — Portfólio é decisão travada |
| **Demandas** | Feed conversacional, Casa + todos os clientes | A demanda renderizada como conversa — cada linha da tabela `Marcos` (append-only) vira uma mensagem na thread | Cliente/Área (Origem/Destino organizacional) · RFI vinculada · MD impactado · card no CX Hub (se `Vinculada ao CX Hub? = Sim`) | Pessoa **ou agente** abre — mecanismo já formalizado em `protocolo-gestao-demanda.md` |
| **RFIs** | Por cliente, com dado comercial (horas, valor) | Escopo, comercial, aprovação de escopo | Demanda de origem (sempre exatamente 1, nunca solta) | Nasce sempre de dentro de uma Demanda — nunca criada do zero |
| **Agentes** | *(entidade ainda não formalizada — ver seção abaixo)* | — | Produto e/ou Área onde roda · Demandas que abriu como Criador | — |

## O mecanismo central: Demanda como fluxo conversacional e de aprovação

Toda demanda nasce **interna** (BrainHub — manter o ecossistema/contexto atualizado), aberta
por uma pessoa **ou por um agente de área** fazendo uma "conferência". Ela só vira um card real
no CX Hub depois, se o que for encontrado exigir trabalho operacional rastreável lá — isso é
opcional e hoje é manual (campo `Vinculada ao CX Hub?`, Não por padrão).

Fluxo de aprovação (já formalizado em `protocolo-gestao-demanda.md`, seção "Mecanismo de
aprovação e retroalimentação" — a tela só precisa dar interface a isso, não reinventar):
1. Demanda é aberta, referenciando `Contexto impactado` (quais MDs mudariam).
2. Status `Aguardando aprovação de contexto`.
3. A pessoa nomeada no campo `Governança` **do MD-alvo específico** — não uma cadeira fixa —
   aprova ou recusa. É dinâmico, MD a MD, nunca uma tabela de permissão solta.
4. Aprovado → o MD é atualizado, um novo `Marco` é registrado ("Contexto atualizado em [data],
   aprovado por [pessoa]"), status vai para `Aplicada`.

## Visibilidade por perfil

Não existe tabela de permissão separada — é função de campos que já existem na ficha de
Pessoa: `Cadeira`, `Área organizacional`, `Clientes atuais atendidos`. Exemplo real e concreto
(os únicos perfis formalizados até agora, nenhum outro é válido como referência):
- **CEO** (João Risoléo) — nomeado na `Governança` do `institucional.md` da Casa. Vê tudo.
- **Key Account** (Laura Delgado Cardoso, Andrea Goulart Holmer dos Santos) e **Consultora de
  Negócios** (Marina Gonçalves Santoro, Vanessa Rinaldi Ornelas Engman) — fichas em
  `uMode/00_Institucional/_pessoas/`, cada uma com `Clientes atuais atendidos` real (hoje: os 4
  pilotos, mesmo time atende todos). Não veem estrutura interna da Casa fora do que a própria
  função exige — veem tudo dos clientes que atendem.

Não use o organograma antigo, o Mapa-mãe do Drive, nem `docs/brainhub_plataforma.html` como
fonte de cadeira/perfil — nenhum desses é válido como estrutura agora.

## O que ainda não existe — não inventar, sinalizar

- **Agente como entidade formal.** `CONTEXT.md` descreve o "Hub de Agentes" como conceito
  (skills reativas + agentes proativos, treinamento em duas camadas: padrão uMode transversal +
  complemento por aplicação), mas não existe `_template_agente.md` nem protocolo — sem onde
  vive, quem cria, quem aprova. Construa a aba com dado de exemplo por ora; **não trave a
  estrutura de dado real sem alinhar antes** (mesmo processo já usado pra Demanda/RFI/Pessoa:
  protocolo primeiro, template depois, registrado em `uMode/00_Institucional/_protocolos/`).
- **`contexto-area.md` real dos clientes.** Hoje 0 de 56 combinações (14 áreas × 4 clientes)
  estão preenchidas — só o template existe. A aba Áreas vai mostrar `[a preencher]` na maioria
  dos casos; isso é esperado, não é bug.
- **Handoff automático Demanda → CX Hub.** Hoje é manual (alguém aprova, alguém cria o card lá).
  Não construa a automação agora — é evolução futura, fora de escopo.

## Regras de padronização (mesma disciplina de `CLAUDE.md`)

- Nunca funda taxonomias diferentes — em especial `Área (CX Hub)` (squad da ferramenta) com
  `Área organizacional` (hierarquia BrainHub). Já houve uma correção real nesse ponto neste
  projeto; não repetir.
- Use sempre os templates existentes (`uMode/**/_template_*.md`) como schema — nunca invente
  campo novo sem checar se já existe algo equivalente.
- Se um dado estiver faltando ou uma estrutura não estiver clara, registre como pendência
  (mesmo padrão de `uMode/00_Institucional/_contexto/_pendencias-gerais.md`) em vez de assumir
  ou preencher com dado plausível.
- Qualquer mudança de estrutura (novo campo, novo tipo de documento) é decisão a validar antes
  de aplicar — nunca uma correção silenciosa.

## Estado de origem deste brief

Escrito em 13 jul 2026, a partir de uma sessão de alinhamento de produto registrada em
`STATE.md` (Sessão 22). Antes de começar a construir, confirme com o Vinicius se algo mudou
desde então — este arquivo descreve uma decisão em um ponto no tempo, `STATE.md` é sempre a
fonte mais atual sobre o que mudou depois.
