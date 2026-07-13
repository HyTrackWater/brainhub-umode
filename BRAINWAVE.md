# BRAINWAVE.md — Instruções para o agente de frontend BrainWave

> Este arquivo não faz parte do cérebro institucional (a hierarquia em `uMode/`). É a instrução
> de trabalho pro agente de frontend interno **BrainWave**, que vai construir a interface visual
> da plataforma BrainHub em cima do cérebro que já existe. Vive na raiz do repositório, ao lado
> de `CLAUDE.md`/`CONTEXT.md`/`STATE.md` — mesmo padrão, público diferente.

## Antes de qualquer tela

Leia, nesta ordem, por inteiro: `CLAUDE.md`, `CONTEXT.md`, `STATE.md`. Eles definem a
hierarquia, as regras de padronização e o estado atual do projeto. Não pule essa leitura — é a
mesma regra que qualquer agente que trabalha neste repositório segue.

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

| Aba | Lista | Abre (detalhe) | Navega pra | Cria |
|---|---|---|---|---|
| **Instituições** | Casa uMode + cada Cliente (hoje: 4 pilotos) | `institucional.md` + `jornada.md` + `pessoas.md` daquela instituição | Áreas dela (ver abaixo) · Pessoas que atendem | Novo cliente — segue `uMode/00_Institucional/_protocolos/protocolo-criacao-cliente.md` (5 passos) |
| **↳ Áreas** (só dentro de uma Instituição, não é aba de topo) | As 8 internas (Casa) ou as 14 canônicas (cliente aberto) | `contexto-area.md` | Produto conectado · Pessoas da área · Demandas com Origem/Destino nessa área | Não é fluxo de uso comum — lista de áreas é fixa/travada em `CONTEXT.md` |
| **Pessoas** | Fichas da Casa (`uMode/00_Institucional/_pessoas/`) + pessoas listadas em `pessoas.md` de cada cliente | Ficha individual (Casa) ou o bloco dela dentro de `pessoas.md` (cliente) | Clientes que atende · Área/Cadeira · Demandas onde é Criador/Responsável | Nova ficha — `protocolo-gestao-pessoas.md` |
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
