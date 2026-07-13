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
até a demanda efetivamente virar um card no CX Hub. O campo `Vinculada ao CX Hub?` (novo, ver
abaixo) é o que registra essa transição. Hoje esse vínculo é criado manualmente, por decisão de
quem aprovou; a automação (agente cria o card sozinho ao aprovar) é evolução futura, fora de
escopo agora.

As 236 demandas já formalizadas dos 4 clientes-piloto (Lofty Style, Cambos, Luiza Barcelos,
Moda Objetiva) são todas migração de dado que **já nasceu** como card no CX Hub/Notion — para
elas, `Vinculada ao CX Hub?` é sempre `Sim`, com o mesmo ID que já está em `ID legado
(Notion/CX Hub)`. É o caso invertido do fluxo novo (que nasce interno e depois, talvez, ganha
card) — aqui já nasceu com card, e nós é que formalizamos o registro histórico depois.

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

- **Vinculada ao CX Hub?** — `Não` (padrão para toda demanda nova/interna) ou `Sim — ID: XXXX`
  (quando a demanda ganhou um card real no CX Hub). Enquanto `Não`, todo o resto desta seção
  fica `[a preencher]` — não é obrigatório e não deve ser adivinhado. Ver seção "Toda demanda
  nasce interna" acima.
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

**Área Responsável (Notion) → Área (CX Hub) + Quadro** — só dentro da taxonomia operacional,
nunca cruza para o lado organizacional (ver regra no topo deste documento: `Área (CX Hub)` não
tem relação com a Área organizacional da hierarquia BrainHub):
| Área Responsável (Notion) | Quadro | Área (CX Hub) |
|---|---|---|
| KA | Operação | Operação \| KA |
| OPERAÇÃO | Operação | Sem Área *(sem match exato — ver nota)* |
| PRODUTO | Operação | Produto \| Inovação |
| TECH | Tech | Suporte Tech *(default — pode refinar por conteúdo)* |
| vazio | `[a preencher]` | `[a preencher]` |

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

**Natureza (organizacional):** toda demanda vinda do Notion de um cliente é `casa-cliente` por
padrão — é trabalho entre a Casa e aquele cliente, mesmo quando "Quem solicitou" está vazio
(nesse caso, a origem provável é a própria Casa observando algo no cliente).

## Status (interno) — execução da demanda dentro do BrainHub
> Adicionado em 13 jul 2026, junto com `Vinculada ao CX Hub?` — fecha uma lacuna real: demandas
> que nunca viram card no CX Hub (ex.: "avisar que fulano saiu da empresa", "mandar e-mail com
> detalhamento de permissionamento") não tinham nenhum campo que dissesse se foram concluídas.

Um terceiro eixo, em `## Identificação`, separado tanto do `Status` operacional do CX Hub
(existe só quando `Vinculada ao CX Hub? = Sim`) quanto do `Ciclo de vida institucional` abaixo
(existe só quando há `Contexto impactado`). `Status (interno)` existe **sempre**, em toda
demanda, e responde a uma pergunta só: "o BrainHub já cumpriu a parte que era dele aqui?"

Enum: `Aberta` · `Em andamento` · `Concluída` · `Cancelada`.

O que "Concluída" significa depende de `Vinculada ao CX Hub?`:
- **`Não`** — acompanha a demanda inteira, do início ao fim. "Concluída" quer dizer que a
  atividade em si foi feita (o e-mail foi enviado, o MD foi atualizado etc.).
- **`Sim`** — acompanha só a parte que cabe ao BrainHub: perceber a demanda e fazê-la virar um
  card real no CX Hub, com o vínculo (`Vinculada ao CX Hub? = Sim` + `ID legado`) registrado.
  Assim que esse vínculo existe, `Status (interno) = Concluída` — **não** significa que o
  trabalho foi executado, só que a demanda foi criada e entregue pro CX Hub. A execução de fato
  segue seu próprio ciclo no `Status` operacional do CX Hub (seção acima), fora do escopo deste
  campo.

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
