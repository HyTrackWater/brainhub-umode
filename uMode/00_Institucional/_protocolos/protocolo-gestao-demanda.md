# Protocolo · Gestão de demanda

> Define natureza, ciclo de vida, marcos, hierarquia pai/filha e o mecanismo de aprovação que
> conecta demandas à atualização de contexto — mais a taxonomia operacional herdada do CX Hub
> (ferramenta oficial de gestão de demandas). Aplica-se a qualquer casa — Casa uMode ou
> Cliente — sem distinção.

## O que é uma demanda
Qualquer unidade de trabalho necessária para o ecossistema funcionar. Não é limitada por
área, por nível de complexidade, nem por envolver ou não um cliente. Definição completa em
`CONTEXT.md` → Glossário.

## Toda demanda nasce interna — o CX Hub é um destino possível, não a origem
> Decisão travada em 13 jul 2026, a partir de conversa sobre o fluxo conversacional da
> plataforma (ver `STATE.md`).

Toda demanda no BrainHub nasce como **demanda interna**: o gatilho é sempre alguém (pessoa ou
**agente de área**, ver seção "Criador" abaixo) percebendo algo que precisa manter o ecossistema
— o conjunto de MDs — atualizado. Isso é anterior e independente de qualquer ferramenta
operacional. A demanda interna **pode, dependendo do que for**, virar um card real no CX Hub
(quando o achado exige trabalho de configuração/entrega rastreável na ferramenta operacional) —
mas nem toda demanda interna vira card, e a demanda interna nunca deixa de existir quando isso
acontece: o card é uma consequência, não uma substituição.

Não criamos um tipo de documento separado para isso — é a **mesma** `Demanda`, com a seção
"Taxonomia CX Hub" abaixo tratada como **opcional/condicional**: fica inteira `[a preencher]`
até a demanda efetivamente ganhar um vínculo real. O campo `Vinculada?` (novo, ver abaixo) é o
que registra essa transição. Hoje esse vínculo é criado manualmente, por decisão de quem
aprovou; a automação (agente cria o registro sozinho ao aprovar) é evolução futura, fora de
escopo agora.

As 236 demandas já formalizadas dos 4 clientes-piloto (Lofty Style, Cambos, Luiza Barcelos,
Moda Objetiva) são todas migração de dado que **já nasceu** como card no CX Hub/Notion — para
elas, `Vinculada?` é sempre `Sim`, com `Vínculo = CX Hub — ID: [mesmo valor de ID legado]`. É o
caso invertido do fluxo novo (que nasce interno e depois, talvez, ganha vínculo) — aqui já
nasceu com card, e nós é que formalizamos o registro histórico depois.

### Nota de visão — resolvida em 14 jul 2026 (generalização do campo aplicada)
Registrada originalmente como "não resolver agora": o destino de uma demanda aprovada depende
da **cadeira/área do colaborador**, não é sempre CX Hub — ex.: demandas nascidas pra equipe de
Vendas provavelmente não devem alimentar o CX Hub, e vão precisar de um destino próprio. O
Vinicius decidiu resolver na hora, ao desenhar a tela de Demandas: campo generalizado de
`Vinculada ao CX Hub?` (binário) para `Vinculada?` + `Vínculo` (lista, aceita mais de um
sistema) — ver "Taxonomia operacional" acima. O fluxo de destino pra sistemas além do CX Hub
continua **não desenhado** (nenhuma sub-taxonomia própria criada ainda) — só o campo que vai
guardar essa informação no futuro já existe.

### Canais de abastecimento futuros (14 jul 2026, registrado pelo Vinicius — não construir agora)
Hoje toda demanda nasce por relato manual (pessoa) ou por conferência de agente de área (já
formalizado acima). Canais adicionais previstos, nenhum construído ainda: canais do Discord,
conteúdo/transcrição de reuniões, upload de arquivo, e inserção manual em linguagem natural
(usuário explica o que quer registrar, um agente interpreta e associa à área/cliente/pessoa
correta). Mesma disciplina de sempre: cada canal novo vira protocolo próprio quando for
construído, não uma lista de possibilidades tratada como já implementada.

## Regra de nomenclatura: duas taxonomias, nunca fundidas
Este protocolo combina dois vocabulários que **parecem** se sobrepor mas não têm relação de
dado entre si:
- **Taxonomia organizacional (BrainHub)** — a hierarquia travada em `CONTEXT.md`
  (Institucional → Áreas → Subáreas → Pessoas). Campos: `Natureza`, `Origem (organizacional)`,
  `Destino (organizacional)`.
- **Taxonomia operacional (CX Hub)** — o vocabulário da ferramenta de gestão de demandas em
  uso hoje (ambientes Operação e Tech). Campos: `Quadro`, `Área (CX Hub)`, `Origem (CX Hub)`,
  `Status`, `Prioridade`, `Tipo`.

Toda vez que um termo colide entre as duas (`Área`, `Origem`), o campo é escrito com a
etiqueta de origem entre parênteses — nunca deixar ambíguo de qual estrutura ele vem.

## Natureza (enum fechado, organizacional)
| Natureza | Descrição |
|---|---|
| Interna | 100% dentro da Casa, sem relação com cliente |
| Inter-área | Entre duas áreas da mesma casa |
| Intra-área | Dentro de uma única área |
| Casa-cliente | Liga um escopo da Casa a um escopo do cliente |

## Onde vive
Um único registro por casa/cliente, em `00_Institucional/_demandas/`. Nunca duplicado dentro
da(s) área(s) envolvida(s) — mesma lógica já aplicada a Pessoa interna: vive uma vez, é
referenciada por metadata (`Origem`/`Destino` organizacionais), nunca copiada.

## Identificação
Convenção de ID: `D-AAAA-NNN`, sequencial por casa/cliente **dentro do ano** — `AAAA` é o ano
da abertura real da demanda (`Data de Solicitação`/`Criado em`), não o ano da formalização.
Isso preserva ordem cronológica mesmo formalizando dados legados anos depois.
Endereçamento: `Casa › Demandas › D-2026-014` ou `Cliente:X › Demandas › D-2026-014`.
- **ID legado (Notion/CX Hub)** — guarda o ID original do sistema de origem (ex.: `UMD-317`),
  quando a demanda vier de migração. Não existe para demandas nativas do nosso padrão.

## Taxonomia operacional (CX Hub) — padrão oficial a partir de agora
O CX Hub tem dois ambientes (quadros): **Operação** (CX Hub propriamente dito) e **Tech**.
Todos os campos abaixo são iguais nos dois quadros, exceto `Área (CX Hub)`.

- **Vinculada?** — `Não` (padrão para toda demanda nova/interna) ou `Sim`. **Generalizado em 14
  jul 2026** (antes era `Vinculada ao CX Hub?`) — o destino de uma demanda aprovada nem sempre é
  o CX Hub (ver nota de visão em "Toda demanda nasce interna" acima: cadeiras/áreas diferentes
  podem ter destino operacional diferente, ex.: Vendas). Enquanto `Não`, o resto desta seção
  fica `[a preencher]` — não é obrigatório e não deve ser adivinhado.
- **Vínculo** — lista de uma ou mais entradas, cada uma no formato `Sistema — ID: XXXX` (ex.:
  `CX Hub — ID: UMD-317`). Aceita mais de uma entrada quando a demanda gerou registro em mais
  de um sistema. Só preenchido quando `Vinculada? = Sim`. Os campos abaixo (Quadro, Status,
  Prioridade, Tipo, Área, Origem) são especificamente do **CX Hub** — só valem quando `Vínculo`
  inclui uma entrada `CX Hub`; outros sistemas de destino, quando existirem, terão sua própria
  sub-seção de taxonomia no futuro (não construído agora).
- **Quadro:** `Operação` | `Tech`
- **Status:** `Backlog` · `Análise` · `A fazer` · `Em Progresso` · `Aguardando Validação` ·
  `Em Revisão` · `Concluído` · `Cancelado`
- **Prioridade:** `Média` · `Alta` · `Urgente`
- **Tipo:** `Configuração` · `Bug` · `Melhoria` · `Feature` · `Investigação Técnica` ·
  `Migração` · `Integração` · `Produto` · `Relatório` · `Suporte`
  > Os últimos 4 foram **adicionados em 08 jul 2026**, a partir dos dados reais de Lofty
  > Style: o enum original (6 valores) cobria só 2 dos 6 tipos realmente usados no Notion
  > legado (`Configuração` bateu exato, `Erro/Bug` virou `Bug`). `Integração`, `Produto`,
  > `Relatório` e `Suporte` são categorias de uso real e frequente — não fazia sentido forçar
  > esses casos dentro de um tipo que não descreve o que é. Enum expandido em vez de distorcer
  > dado real para caber num enum incompleto.
- **Área (CX Hub)** — depende do quadro. É uma classificação de squad interna da ferramenta,
  **não tem relação com a Área organizacional** da hierarquia BrainHub:
  - Quadro Operação: `Operação | KA` · `Produto | Inovação` · `Sem Área`
  - Quadro Tech: `Suporte Tech` · `Dados` · `Integração` · `Inovação` · `Migração` · `Infra` ·
    `Sem área`
- **Origem (CX Hub)** — motivo/gatilho de abertura, seleção múltipla: `Jornada de Teste` ·
  `Escopo Inicial` · `Revisão do Processo`. Não confundir com `Origem (organizacional)`
  (quem/onde abriu) — são dados diferentes que só coincidem no nome.
- **Criador** / **Responsável** / **Co-responsáveis** — pessoa física, **ou agente** quando a
  demanda nasce de uma "conferência" automática de área (achado do agente vira demanda direto,
  sem estágio intermediário de triagem humana — decisão travada em 13 jul 2026). Quando o
  Criador é um agente, o nome do agente entra normalmente no campo (mesmo formato de texto que
  já usamos pra pessoa) — não criamos um tipo de ficha "Agente" agora, só quando o volume/uso
  real justificar (mesmo critério já aplicado a outras decisões de estrutura deste protocolo).
  Isso não muda quem aprova: `Aprovação de contexto` continua resolvida pelo campo `Governança`
  do MD-alvo, nunca pelo Criador da demanda.
- **Datas:** `Início Previsto` · `Entrega Prevista` · `Início Real` · `Conclusão Real`
- **RFI vinculada** — ID da RFI, se houver (ver seção RFI abaixo)
- **Horas atribuídas** — na demanda e/ou em cada subdemanda
- **Motivo de bloqueio** (só quando o Status indica bloqueio): `Aguardando Cliente` ·
  `Dependência Técnica` · `Infra / Ambiente` · `Aguardando Decisão` · `Dependência Externa` ·
  `Outra`

### Estrutura de conteúdo (espelha as abas do card no CX Hub)
- **Conteúdo** — Descrição · Resultado Esperado · Notas internas · Resolução · Anexos e Links
- **Subdemandas** — checklist tático de atividades dentro do **mesmo card**, cada uma podendo
  ter horas atribuídas. **Diferente de "Demanda filha"** (ver Hierarquia pai/filha): subdemanda
  não muda de área/casa nem tem ciclo de aprovação próprio; é só o passo a passo interno.
- **Conversas** — histórico de comunicação livre entre a equipe sobre a demanda
- **Atividades** — log automático de tudo que foi feito no card, sem edição manual. No MD
  (fase atual, sem automação de agente) isso não é gerado sozinho — fica como seção manual até
  o dia em que houver ferramenta/agente registrando automaticamente.

## Tradução Notion legado → padrão (aplicada na migração)
> Tabela construída com dados reais de Lofty Style (08 jul 2026) — vale como referência para
> qualquer cliente migrado do Notion, não só Lofty. Combos que ainda não apareceram na vida
> real ficam de fora até serem observados.

**Status + Etapa (Notion, 2 níveis) → Status (CX Hub, 1 nível):**
| Status (Notion) | Etapa (Notion) | → Status (CX Hub) | Observação |
|---|---|---|---|
| Não iniciada | Backlog | Backlog | — |
| Não iniciada | (vazio) | Backlog | Status prevalece quando Etapa não vem preenchida |
| Standby - Produto | Backlog | Backlog | + `Motivo de bloqueio: Aguardando Decisão` |
| Standby - Produto | Na Fila | Backlog | + `Motivo de bloqueio: Aguardando Decisão` — combo achado em 10 jul 2026 (Cambos/Luiza Barcelos), mesmo tratamento de "Standby - Produto" |
| Nível de Análise | Análise Cliente | Análise | — |
| Nível de Análise | Em Validação - Cliente | Análise | Achado em 10 jul 2026 — Status prevalece sobre a nuance de Etapa |
| Demanda Aceita | Em Desenvolvimento | Em Progresso | Achado em 10 jul 2026 (Cambos) |
| Demanda Aceita | Em Validação - Cliente | Aguardando Validação | Achado em 10 jul 2026 — "Em Validação - Cliente" mapeia para o status que nomeia exatamente essa espera |
| Demanda Aceita | Em Teste | Em Revisão | Achado em 10 jul 2026 — teste interno (sem "- Cliente" no nome), distinto de "Aguardando Validação" |
| Concluída | Demanda Concluída | Concluído | — |
| Concluída | Em Validação - Cliente | Concluído | Achado em 10 jul 2026 (1 caso) — dado legado conflitante (Status já concluída, Etapa ainda indica validação em aberto); Status prevalece, conflito registrado como observação na demanda, não resolvido por conta própria |
| Encerrada | Demanda Cancelada | Cancelado | — |

**Combos achados em 03 ago 2026** (replicação total — 652 demandas dos 42 clientes fora do
piloto). Regra usada, já implícita na tabela acima e agora escrita explicitamente: **o `Status`
(Notion) determina o status; a `Etapa` só refina quando nomeia um estágio operacional distinto**
(foi o que já valia para `Em Validação - Cliente` e `Em Teste`). Quando os dois se contradizem,
`Status` prevalece e o conflito é registrado como observação dentro da própria demanda — nunca
resolvido por conta própria.

| Status (Notion) | Etapa (Notion) | → Status (CX Hub) | Observação |
|---|---|---|---|
| Nível de Análise | Análise uMode | Análise | `Análise uMode` é o espelho interno de `Análise Cliente` (já mapeado) — mesmo destino |
| Nível de Análise | Na Fila | Análise | Status prevalece — segue em análise |
| Nível de Análise | Backlog | Análise | Status prevalece |
| Nível de Análise | (vazio) | Análise | Mesma regra de "Não iniciada \| (vazio)" |
| Demanda Aceita | Na Fila | A fazer | Primeiro uso real do valor `A fazer` do enum: aceita e enfileirada, ainda não iniciada. Não confundir com `Standby - Produto \| Na Fila` (acima), que é bloqueio e continua Backlog |
| Demanda Aceita | Análise uMode | Análise | Etapa nomeia estágio distinto (mesma lógica de `Em Teste` → Em Revisão) |
| Demanda Aceita | Análise Cliente | Análise | idem |
| Demanda Aceita | Demanda Concluída | Em Progresso | ⚠ dado legado conflitante — Status prevalece, conflito registrado em `Notas internas` |
| Standby - Produto | Análise uMode | Backlog | + `Motivo de bloqueio: Aguardando Decisão` — Standby prevalece, como nos outros combos de Standby |
| Concluída | Na Fila | Concluído | ⚠ conflitante — Status prevalece, conflito registrado |
| Não iniciada | Análise uMode | Backlog | ⚠ conflitante — Status prevalece, conflito registrado |
| Não iniciada | Em Desenvolvimento | Backlog | ⚠ conflitante — Status prevalece, conflito registrado |
| Encerrada | Demanda Concluída | Cancelado | ⚠ conflitante — Status prevalece, conflito registrado |
| Encerrada | Backlog | Cancelado | Status prevalece |
| Encerrada | Em Validação - Cliente | Cancelado | ⚠ conflitante — Status prevalece, conflito registrado |
| Encerrada | Análise uMode | Cancelado | ⚠ conflitante — Status prevalece, conflito registrado |

**Combos achados em 03 ago 2026 (2ª rodada — fonte de jul 2026, recuperada do histórico do Git).**
A 1ª rodada usou um snapshot de mar 2026; ao trocar para o export de jul 2026 (mais completo,
761 demandas não-piloto em vez de 649) apareceram 6 combos que o snapshot menor não continha:

| Status (Notion) | Etapa (Notion) | → Status (CX Hub) | Observação |
|---|---|---|---|
| Concluída | (vazio) | Concluído | Mesma regra de "Não iniciada \| (vazio)": Status prevalece quando Etapa não vem preenchida |
| Standby - Produto | (vazio) | Backlog | + `Motivo de bloqueio: Aguardando Decisão` |
| Standby - Produto | Análise Cliente | Backlog | + `Motivo de bloqueio: Aguardando Decisão` — Standby prevalece, como nos outros combos de Standby |
| Encerrada | Na Fila | Cancelado | Status prevalece |
| Não iniciada | Análise Cliente | Backlog | ⚠ conflitante — Status prevalece, conflito registrado (mesmo tratamento de "Não iniciada \| Análise uMode") |
| Demanda Aceita | Backlog | A fazer | **Não** é conflito: no 1º nível a demanda foi aceita, e a Etapa (`Backlog`) só diz que ainda não começou — exatamente o que `A fazer` nomeia. Mesmo destino de `Demanda Aceita \| Na Fila`. Distinto de `Nível de Análise \| Backlog` → `Análise`, onde a demanda **não** foi aceita ainda: o 1º nível é que decide se houve aceite, e a Etapa só diz em que ponto está |

**Área Responsável (Notion) → Área (CX Hub) + Quadro** — só dentro da taxonomia operacional,
nunca cruza para o lado organizacional (ver regra no topo deste documento: `Área (CX Hub)` não
tem relação com a Área organizacional da hierarquia BrainHub):
| Área Responsável (Notion) | Quadro | Área (CX Hub) |
|---|---|---|
| KA | Operação | Operação \| KA |
| OPERAÇÃO | Operação | Sem Área *(sem match exato — ver nota)* |
| PRODUTO | Operação | Produto \| Inovação |
| TECH | Tech | Suporte Tech *(default — pode refinar por conteúdo)* |
| INOVAÇÃO / IA | `[a preencher]` | `[a preencher]` *(achado em 03 ago 2026 — ver nota)* |
| vazio | `[a preencher]` | `[a preencher]` |

> **`INOVAÇÃO / IA` (achado em 03 ago 2026, 4 registros):** não foi mapeado de propósito. O valor
> é genuinamente ambíguo entre os dois quadros — o quadro Operação tem `Produto | Inovação` e o
> quadro Tech tem `Inovação`, e nada na fonte diz qual dos dois; além disso o "/ IA" não existe em
> nenhum dos dois enums. Escolher um seria inventar. `Quadro` e `Área (CX Hub)` ficam
> `[a preencher]`, e o valor legado bruto é preservado em `### Notas internas` da demanda para não
> perder o dado. Pendência aberta em `_pendencias-gerais.md`.

> Nota: `OPERAÇÃO` (genérico) não tem correspondente exato no enum de Área (CX Hub) definido
> a partir da descrição original (só existe `Operação | KA`, não um "Operação" puro) — mapeado
> para `Sem Área` por ser a opção menos distorciva. Avaliar se o enum do CX Hub real precisa
> de um valor "Operação" genérico.
>
> **`Destino (organizacional)` não é derivável de `Área Responsável` (Notion) nem de nenhum
> campo CX Hub — são taxonomias sem relação de dado.** Nos dados legados de Notion migrados,
> `Destino (organizacional)` fica `[a preencher]` até alguém com conhecimento institucional
> real (não um campo de ferramenta) decidir qual área da Casa efetivamente responde por
> aquela demanda. **Correção registrada em 08 jul 2026** — a primeira formalização de Lofty
> Style tinha esse cruzamento indevido; foi corrigida.

**Tipo de Demanda (Notion) → Tipo (CX Hub):** idêntico exceto `Erro/ Bug` → `Bug` e
`Melhoria / Desenvolvimento` → `Melhoria` (achado em 10 jul 2026, dados de Cambos — variante de
nome do mesmo enum, sem ambiguidade de sentido). Os demais (`Configuração`, `Integração`,
`Produto`, `Relatório`, `Suporte`) passam direto — ver enum expandido acima.

**`Criticidade` (Notion, campo solto) → `Prioridade` (CX Hub), só como fallback:** achado em
10 jul 2026 (dados de Cambos/Luiza Barcelos/Moda Objetiva) — quando `Prioridade` (Notion) vem
vazio e `Criticidade` tem um valor que cabe no enum de Prioridade (`Média`/`Alta`/`Urgente`),
usa-se `Criticidade` como fonte. Não é campo novo do nosso padrão — é só reaproveitar um sinal
real do Notion legado que aponta pro mesmo conceito. Valores de `Prioridade` (Notion) fora do
enum (ex.: valor numérico solto como `"2"`) ficam `[a preencher]`, registrados como observação
— não convertidos por suposição de escala.

**Valores de `Criticidade` achados em 03 ago 2026** (replicação total), registrados antes de
aplicar:
| Criticidade (Notion) | → Prioridade (CX Hub) | Decisão |
|---|---|---|
| `Alta` · `Média` | `Alta` · `Média` | passam direto (já valia) |
| `Crítica / Urgente` | `Urgente` | variante de nome do mesmo valor do enum — mesma classe de tradução já aceita em `Erro/ Bug` → `Bug` e `Melhoria / Desenvolvimento` → `Melhoria` |
| `Baixa` | `[a preencher]` | **não** mapeado: o enum de Prioridade só tem `Média`/`Alta`/`Urgente`, não existe valor abaixo de Média. Forçar para `Média` inventaria uma prioridade que a fonte não afirma. Valor bruto preservado em `### Notas internas` |

> Consequência aceita: o enum de Prioridade pode estar incompleto em relação ao CX Hub real (falta
> um valor tipo `Baixa`). Registrado como pendência em `_pendencias-gerais.md` em vez de resolvido
> aqui — mudar enum de ferramenta não é decisão desta formalização.

### Colunas do Notion aproveitadas na 2ª rodada (03 ago 2026)
A 1ª rodada usava 16 das 35 colunas do export. Ao "dissecar tudo" (pedido do Vinicius), estas
passaram a ser aproveitadas — nenhuma delas exigiu campo novo:

| Coluna (Notion) | Preench. | → Onde entra | Decisão |
|---|---|---|---|
| `RFI` | 44 | `### RFI vinculada` | É o vínculo bidirecional que o protocolo exige e que estava `[a preencher]` em todas as demandas. Resolvido contra as RFIs já formalizadas do mesmo cliente (casamento por nome); quando não resolve, guarda o nome bruto da RFI |
| `Bloqueio` | 37 | `### Motivo de bloqueio` | Ver tabela de tradução abaixo. Prevalece sobre a regra automática de `Standby - Produto` quando os dois existem — é o motivo real, não o inferido |
| `Texto` | 2 | `### Descrição` | Corpo da página, quando o export o trouxe |

**`Bloqueio` (Notion) → `Motivo de bloqueio`:**
| Valor no Notion | → | Decisão |
|---|---|---|
| `Aguardando o Cliente` | `Aguardando Cliente` | variante de nome do mesmo valor do enum |
| `Aguardando Recurso Especial` · `Aguardando Time Interno - uMode` · `Aguardando momento oportuno` · `Mudança de Priorização - Item urgente na frente!` · `Ordem da Diretoria - Não faremos isso nesse momento` | `Outra` | nenhum tem equivalente no enum (`Dependência Técnica`/`Infra`/`Aguardando Decisão`/`Dependência Externa` descrevem outra coisa). Usa `Outra` — que existe exatamente pra isso — e **mantém o valor original visível na mesma linha**, para não perder o motivo real |

> Consequência aceita: o enum de `Motivo de bloqueio` provavelmente está incompleto em relação ao
> uso real (faltam pelo menos "aguardando time interno" e "repriorização"). Registrado como
> pendência em `_pendencias-gerais.md` em vez de resolvido aqui.

### Colunas do Notion preservadas sem campo próprio (03 ago 2026)
Estas colunas têm dado real e **nenhum campo equivalente** no nosso padrão. Em vez de descartar
(perda de dado) ou inventar campo (proibido sem validação), vão para `### Notas internas` num
bloco rotulado `[Campos legados do Notion sem campo equivalente no padrão]`, cada um com nome e
valor. Assim a informação fica no registro e a decisão de promover algum a campo próprio pode ser
tomada depois, com o dado já em mãos:

| Coluna (Notion) | Preench. (de 1007) | Por que é candidata a campo próprio |
|---|---|---|
| `Responsabilidade` | **1007 — 100%** | `Demanda com uMode` (920) × `Demanda Pendente do Cliente` (87). Diz de que lado a bola está; é o campo com maior cobertura de toda a base e não temos nada equivalente. **Candidato mais forte a virar campo próprio** — decisão do Vinicius/CEO |
| `Projeto` | 594 | Projeto/fase de onboarding do cliente (ex.: `[NK] - uFlow`, `📌 [LOFTY] - ONBOARDING FASE 1`) — se conecta com `jornada.md`, não com a demanda em si |
| `uMode - Macro Tema` | 184 | Tema/assunto macro (ex.: `permissionamento`, `template de ficha`) — parece taxonomia de agrupamento, não status |
| `Comentário uMode` | 163 | Comentário interno. Já foi **descartado no modelo de RFI** por decisão do CEO (ver `protocolo-gestao-rfi.md`); para Demanda nunca houve decisão, então é preservado como legado |
| `Suporte Integração` | 57 | Classificação técnica de erro de integração (`Escrita - Erro`, `Leitura - Material pendente`…) |
| `Tempo de Resolução` | 49 | Valor numérico sem unidade declarada na fonte — **não** foi tratado como horas, justamente por isso |
| `Nível de Esforço` | 29 | `Baixo`/`Médio`/`Alto`/`Muito Alto` — não confundir com `Prioridade` nem com `Horas atribuídas` |

> `Total de Horas` e `Fórmula` vêm 100% vazias no export (colunas calculadas do Notion, que o CSV
> não materializa) — nada a preservar.

**Natureza (organizacional):** toda demanda vinda do Notion de um cliente é `casa-cliente` por
padrão — é trabalho entre a Casa e aquele cliente, mesmo quando "Quem solicitou" está vazio
(nesse caso, a origem provável é a própria Casa observando algo no cliente).

## Status (interno) — execução da demanda dentro do BrainHub
> Adicionado em 13 jul 2026, junto com `Vinculada?` (na época `Vinculada ao CX Hub?`, renomeado
> em 14 jul 2026 — ver "Taxonomia operacional" acima) — fecha uma lacuna real: demandas que
> nunca ganharam vínculo nenhum (ex.: "avisar que fulano saiu da empresa", "mandar e-mail com
> detalhamento de permissionamento") não tinham nenhum campo que dissesse se foram concluídas.

Um terceiro eixo, em `## Identificação`, separado tanto do `Status` operacional do sistema de
destino (existe só quando `Vinculada? = Sim`) quanto do `Ciclo de vida institucional` abaixo
(existe só quando há `Contexto impactado`). `Status (interno)` existe **sempre**, em toda
demanda, e responde a uma pergunta só: "o BrainHub já cumpriu a parte que era dele aqui?"

Enum: `Aberta` · `Em andamento` · `Concluída` · `Cancelada`.

O que "Concluída" significa depende de `Vinculada?`:
- **`Não`** — acompanha a demanda inteira, do início ao fim. "Concluída" quer dizer que a
  atividade em si foi feita (o e-mail foi enviado, o MD foi atualizado etc.).
- **`Sim`** — acompanha só a parte que cabe ao BrainHub: perceber a demanda e fazê-la virar um
  registro real no sistema de destino, com o `Vínculo` preenchido. Assim que esse vínculo
  existe, `Status (interno) = Concluída` — **não** significa que o trabalho foi executado, só
  que a demanda foi criada e entregue pro destino. A execução de fato segue seu próprio ciclo no
  `Status` operacional do sistema vinculado (seção acima, hoje só CX Hub tem taxonomia própria),
  fora do escopo deste campo.

## Ciclo de vida institucional (aprovação de contexto)
Um quarto eixo, também separado dos outros três acima — controla especificamente a permissão
para escrever em contexto institucional, não a execução da demanda em si:
`Nenhuma aprovação pendente` → `Aguardando aprovação de contexto` → `Aprovada` → `Aplicada`.

## Marcos
Log append-only dentro de cada demanda: `Data | Evento/decisão | Responsável | Novo status`.
Nunca se reescreve um marco antigo — só se adiciona um novo.

Três registros distintos, não confundir:
- **Marcos** (aqui) — decisões pontuais e institucionais dentro de uma demanda.
- **Marcos da jornada** (`jornada.md`) — fases macro da relação uMode↔cliente.
- **Conversas** / **Atividades** (CX Hub, acima) — comunicação livre e log automático bruto.

## Hierarquia pai/filha
Uma demanda mãe pode gerar N demandas filhas em áreas ou casas diferentes (ex.: uma reunião
gera 5 demandas em 3 áreas distintas). Cada filha referencia `Demanda mãe`; a mãe lista
`Demandas filhas`, cada uma com a flag "bloqueia conclusão da mãe: sim/não". A mãe só fecha
quando as filhas marcadas como bloqueantes fecham — as demais são apenas rastreadas.

## RFI
Nem toda demanda vira RFI; toda RFI nasce de uma demanda. Uma demanda pode, conforme sua
classificação e aprovações (apresentação ao cliente → aprovação para desenvolvimento), virar
uma RFI — nesse caso, a demanda ganha o campo `RFI vinculada` preenchido, e a RFI guarda
`Demanda relacionada` apontando de volta (vínculo sempre bidirecional). No CX Hub, a RFI é
criada de dentro do próprio card da demanda — nunca como registro independente.
Modelo completo (campos, ciclo de vida, onde vive): `protocolo-gestao-rfi.md`.

## Mecanismo de aprovação e retroalimentação
1. Pessoa relata um fato → demanda é aberta (por pessoa ou por outro processo).
2. Se a demanda exige alteração de contexto, ela entra em "Aguardando aprovação de contexto",
   referenciando exatamente quais MDs/campos mudariam (`Contexto impactado`).
3. Pessoa com permissão — já registrada no campo "Governança" do MD-alvo — aprova.
4. Agente aplica a mudança nos MDs referenciados.
5. Demanda registra um novo Marco: "Contexto atualizado em [data], aprovado por [pessoa]".
6. Ciclo institucional vai para "Aplicada".

Nenhum agente escreve contexto sem essa aprovação registrada como marco — rastreabilidade
ponta a ponta.

## Contexto consultado vs. contexto impactado
- **Consultado** — MDs que a demanda precisa ler para decidir algo (ex.: checar
  `institucional.md` do cliente antes de liberar novos usuários, para saber se o plano
  contratado permite).
- **Impactado** — MDs que devem ser atualizados quando a demanda fecha.

Uma demanda pode ter só consultado, só impactado, os dois, ou nenhum.

## Governança
- Abertura de demanda → qualquer pessoa autorizada na casa/cliente.
- Aprovação de mudança de contexto → responsável definido no campo "Governança" do MD-alvo.
- Este protocolo → Vinicius Risoléo + CEO.
