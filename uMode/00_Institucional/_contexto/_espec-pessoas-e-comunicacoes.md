---
aliases:
  - "ESPEC-PESSOAS-001 v1 — Pessoas e comunicações como entidades do banco"
tags:
  - tipo/autoridade
  - casa
---
# ESPEC-PESSOAS-001 v1 — Pessoas e comunicações como entidades do banco

> Escrita em **21 set 2026** por Vinicius Risoléo (com Claude Code), a partir da varredura ao vivo
> do Notion. **Nomes de campo, collection e relação em inglês** — padrão travado no `CLAUDE.md`.
>
> **Por que existe.** Instrução do Vinicius em 21/09/2026: *"é muito importante rastrear as pessoas
> que estão ativas ou inativas, porque será muito importante para a jornada do usuário para saber
> quem atende o que e em relação a quais ferramentas e áreas. Começaremos a tornar as comunicações
> entidades do próprio banco de forma que isso comece a gerar as indexações do cérebro para se
> comunicarem."*
>
> **Autoridade:** definir collections, campos e forma de relacionamento é nosso papel. O schema
> atual é autoridade sobre o que existe, nunca sobre o que deve existir.

**Relação com as outras especificações:**
- **`_espec-banco-brainhub.md` (ESPEC-BANCO-001)** continua dono do banco como um todo — hierarquia,
  `brains`, `seeds`, `context_packs`, outbox, federação. **Este documento não o substitui.**
- Este documento é **dono exclusivo** de `people`, `person_memberships`, `communication_channels`,
  `communication_events` e `channel_participations`. Qualquer coisa que a ESPEC-BANCO diga sobre
  pessoa ou comunicação fica **`SUPERSEDED`** por este.

**Grau por afirmação:** `[C]` verificado na fonte viva, com a fonte citada · `[P]` proposta nossa,
não validada · `[D]` decisão que não é minha.

---

## 0 · Declaração de completude — leia antes de confiar em qualquer linha

| # | O que este documento NÃO resolve | Por quê |
|---|---|---|
| 1 | **A janela de observação é de 24 dias.** | A única fonte de evidência de ação que existe é `Chamados & Atendimentos`, com **182 tickets entre 06 e 29/01/2026** `[C]`. Fora disso, não há como provar que alguém agiu. **Todo estado `CADASTRADO` neste modelo é um limite da instrumentação, não um fato sobre a pessoa.** |
| 2 | **Nenhuma ata foi aberta.** | Varri título e data de 23 atas do Puket `[C]`. Participantes, decisões e nomes estão dentro delas. `communication_events` nasce sem o campo mais rico que teria. |
| 3 | 🔴 **CORRIGIDO em 25/09/2026 — a fonte de desligamento EXISTE.** | Esta linha dizia *"nenhum sistema varrido registra saída de pessoa"*. **Falso.** A página `🏛️ Organograma uMode — V2` do Notion registra desligamento **com nome, data e código de decisão** — D73 (Rafael Renaldim), D75 (Alexandre Ferrari, Andrea Goulart, André Gustavo), D76 (Gabriel Cancio, Tatiana Bertazoli, Henrique Sousa, Williem Gomes) `[C]`. ⚠ **Eu escrevi "não existe" tendo varrido o CRM e a base `uModers`, e não o organograma** — terceira variação de *ausência de fonte é hipótese*, desta vez de minha autoria. 🟢 **Consequência: `DESATIVADO` deixa de ser "raro e subnotificado" e passa a ter fonte data**. |
| 4 | **WhatsApp é canal declarado, não capturado.** | A página da Reserva lista **9 grupos** com marcação de manter/excluir `[C]`, mas o conteúdo não é acessível ao BrainHub. Entra como canal, nunca como evento. |
| 5 | **Kanbanize não foi varrido.** | A Reserva referencia cards em `umode.kanbanize.com`, boards 6 e 18 `[C]`. É um sistema inteiro fora do inventário. |
| 6 | **Volumetria, retenção e LGPD** | Este modelo guarda nome, e-mail corporativo e histórico de ação de pessoa identificada. **Retenção e base legal são decisão `[D]`, não minha.** |

---

## 1 · O achado que obriga este modelo

> **Cadastro e atividade são coisas diferentes, e hoje o BrainHub só enxerga cadastro.**

Verificado em dois clientes `[C]`:

| | Caedu | Puket |
|---|---:|---:|
| Pessoas na tabela do PLM | 93 | 43 |
| Com evidência de ação na janela | **3** | **3** |
| **Agiram e não constam na tabela** | **2** | **2** |
| Baixa declarada na origem | 0 | 1 |

**Quatro pessoas reais usaram a plataforma e não existem na lista de usuários do cliente:**
`paula.silva@caedu.com.br`, `joao.neto@caedu.com.br`, `beatriz.fraga@puket.com.br`,
`geane.oliveira@puket.com.br` `[C]`.

E a tabela do Puket tem **última data de acesso em 21/06/2023** — três anos atrás `[C]`.

> **A conclusão não é "a tabela está errada".** É que **tabela transcrita à mão numa página de
> Notion não é cadastro**. O vínculo pessoa↔área precisa vir do PLM por integração, e o vínculo
> pessoa↔atividade precisa vir do canal. São duas fontes, não uma.

---

## 2 · `people` — a pessoa, uma vez só

**Identidade:** o e-mail normalizado é a chave natural. `[P]`

| Campo | Tipo | Regra |
|---|---|---|
| `_id` | ObjectId | |
| `primaryEmail` | string | **único global**, lowercase, trim. É a chave natural. |
| `alternateEmails` | string[] | mesma pessoa em outro domínio |
| `displayName` | string | como a fonte escreve. **Preservar, não normalizar** — ver §6 |
| `canonicalName` | string? | nome civil quando conhecido; `null` é aceitável |
| `relationType` | enum | `INTERNAL` · `CLIENT` · `SUPPLIER` · `PARTNER` · `UNKNOWN` |
| `createdFrom` | enum | `PLM_ROSTER` · `TICKET` · `MEETING` · `MANUAL` |
| `firstSeenAt` / `lastSeenAt` | date | menor e maior evidência **de qualquer canal** |
| `mergedInto` | ObjectId? | desduplicação nunca apaga; aponta |

**Invariante P1.** Uma pessoa **nunca** é duplicada por cliente. `natasha.maruno@grupounico.hk` é
uma pessoa; a relação dela com Puket é uma `person_membership`. Isso já é a regra da hierarquia
(*"pessoa interna nunca é duplicada dentro do cliente"*) — aqui ela vale também para pessoa de
cliente, porque **fornecedor aparece em mais de uma conta** `[C]`.

**Invariante P2.** `relationType = SUPPLIER` não é inferido de domínio. Foi observado que
`controle@floc.com.br`, `compras1@mclprivatelabel.com.br`, `engenharia1@indorf.com.br`,
`vanessa.riato@lavinorte.com.br` e `cesar@vape.com.br` abrem chamado **na conta da Reserva** `[C]`.
São fornecedores operando dentro da conta de um cliente. **O tipo vem do vínculo, não do e-mail.**

---

## 3 · `person_memberships` — o vínculo, com tempo e com estado

Uma linha por (pessoa × organização × papel). É aqui que mora a resposta a *"quem atende o quê, em
qual ferramenta, em qual área"*.

| Campo | Tipo | Regra |
|---|---|---|
| `personId` | ObjectId | → `people` |
| `organizationId` | ObjectId | → `organizations` |
| `orgLayer` | string? | **camada societária** dentro do cliente — ver §3.1 |
| `accessProfile` | string | **o perfil exatamente como o cliente o nomeia** — ver §3.2 |
| `areaId` | ObjectId? | área canônica resolvida; `null` quando não derivável |
| `areaResolution` | enum | `DERIVED` · `DECLARED` · `TRANSVERSAL` · `UNRESOLVED` |
| `tools` | string[] | `uFlow/PLM` · `Linx` · `SAP` · … |
| `activityState` | enum | `ATIVO` · `CADASTRADO` · `DESATIVADO` · `ATIVO_SEM_CADASTRO` · `INDETERMINADO` |
| `activityEvidenceRef` | ObjectId? | → `communication_events`. **Obrigatório** se `ATIVO` |
| `activityEvidenceAt` | date? | **Obrigatório** se `ATIVO` ou `DESATIVADO` |
| `observationWindow` | {from, to} | **a janela em que se pôde observar** — ver §3.3 |
| `accessGrantedAt` | date? | "ativo desde" do PLM |
| `deactivatedAt` | date? | só com marcação na fonte |

### 3.1 · `orgLayer` — porque cliente nem sempre é uma empresa `[C]`

No Puket, os 43 usuários se dividem em `@puket.com.br` (22), `@grupounico.com` (20) e
`@grupounico.hk` (1). **Puket é marca do Grupo Único.** A holding concentra Sourcing, Qualidade,
Controladoria, Importação, Projetos, BI e Certificação; a marca concentra Estilo, Design, Produto,
PCP e TEX; e há sourcing em **Hong Kong**.

Na Cambos o mesmo padrão aparece com `cambos.com.br` e `souzacambos.com.br` `[C]`.

> **Sem `orgLayer`, o brain da Puket mistura holding com marca** e responde errado a *"quem decide
> compra?"*. **`orgLayer` é preenchido, nunca inferido do domínio** — o domínio é a pista, a
> confirmação é do atendimento.

### 3.2 · `accessProfile` é string livre, e isso é deliberado `[C]`

A convenção de nome de perfil **é de cada cliente**:

| Cliente | Convenção | Exemplos |
|---|---|---|
| Caedu | `<Cliente>-<Área>` | `Caedu-Estilo` · `Caedu-Produto` · `Caedu-Gerentes` |
| Puket | **nome de função puro** | `Sourcing Nacional` · `TEX` · `PCP` · `BI` · `Controladoria` |

**Invariante P3. Nunca faça parsing do nome do perfil para achar a área.** A resolução vive numa
tabela de mapeamento por organização, preenchida por pessoa, e o que não resolve fica
`UNRESOLVED` — **não vira palpite**. No Puket, `TEX` continua sem significado conhecido em nenhuma
fonte varrida `[C]`; ele deve chegar ao banco como `UNRESOLVED`, não como "têxtil".

**Invariante P4. O perfil governa permissão, não só rótulo.** Evidência: em 06/01/2026
`eduarda.souza@grupounico.com`, perfil `Importação`, abriu chamado pedindo que **o perfil pudesse
criar tarefas** `[C]`. Logo `accessProfile` é dado operacional, não etiqueta descritiva.

### 3.3 · `observationWindow` — o campo que impede a leitura errada

**`CADASTRADO` significa "nenhuma evidência dentro da janela", nunca "inativo".**

Hoje a janela real é `{from: 2026-01-06, to: 2026-01-29}` `[C]`. Sem esse campo gravado ao lado do
estado, daqui a um ano alguém vai ler `CADASTRADO` em 90 pessoas da Caedu e concluir que a conta
está morta — quando o que se sabe é que **a instrumentação durou 24 dias**.

**Invariante P5.** `activityState` é **derivado, nunca digitado**. Recalcula quando entra
`communication_event`. O único estado que aceita origem manual é `DESATIVADO`, e exige
`sourceMarking` — no Puket o sinal foi literalmente **texto tachado** `[C]`.

---

## 4 · `communication_channels` — o canal é entidade

> **É esta collection que gera a indexação que faz um brain falar com outro.** Um canal tem
> participante, cadência, dono e assunto. Um brain que não sabe por onde a conversa passa não
> consegue endereçar nada.

| Campo | Tipo | Regra |
|---|---|---|
| `kind` | enum | `MEETING_SERIES` · `TICKET_QUEUE` · `CHAT_GROUP` · `PLATFORM_CHAT` · `EMAIL_THREAD` · `DOC_SPACE` · `BOARD` · `TRAINING` |
| `name` | string | como a operação chama |
| `organizationId` | ObjectId | de quem é o canal |
| `tool` | string | `Notion` · `WhatsApp` · `Gist` · `Miro` · `Kanbanize` · `Google Drive` · `YouTube` |
| `externalRef` | string? | id na origem (`collection://…`, url do board) |
| `cadence` | enum | `WEEKLY` · `BIWEEKLY` · `ON_DEMAND` · `UNKNOWN` |
| `status` | enum | `ACTIVE` · `DORMANT` · `RETIRED` · `TO_RETIRE` |
| `lastEventAt` | date? | **derivado** do último `communication_event` |
| `ownerPersonId` | ObjectId? | quem responde pelo canal |
| `isCaptured` | bool | **o BrainHub consegue ler o conteúdo?** |

**Invariante P6. `isCaptured` é obrigatório e quase sempre `false`.** Dos canais observados, só
`Notion` é legível pelo BrainHub hoje. WhatsApp, Gist, Miro, Kanbanize, Drive e YouTube aparecem
como canal e **não entregam conteúdo** `[C]`. **Canal não capturado é lacuna visível; canal omitido
é lacuna invisível.**

**`TO_RETIRE` não é invenção.** A página da Reserva marca 9 grupos de WhatsApp com 🟢 manter e
🔴 excluir `[C]` — **a operação já faz curadoria de canal à mão.** O modelo só formaliza.

---

## 5 · `communication_events` — a comunicação individual

| Campo | Tipo | Regra |
|---|---|---|
| `channelId` | ObjectId | → `communication_channels` |
| `kind` | enum | `TICKET` · `MEETING_MINUTE` · `VISIT` · `REVIEW` · `MESSAGE` |
| `occurredAt` | date | **campo, nunca string dentro do título** — ver §5.1 |
| `participants` | [{personId, role}] | `role`: `REQUESTER` · `HANDLER` · `ATTENDEE` · `MENTIONED` |
| `subjectType` | string? | tipo do chamado, quando houver |
| `state` | string? | estado na origem |
| `summary` | string? | resumo curto |
| `areaIds` | ObjectId[] | áreas tocadas |
| `toolsInvolved` | string[] | `uFlow` · `Linx` · `SAP` · … |
| `disclosurePolicy` | enum | `OPEN` · `INTERNAL_ONLY` · `NEVER_TO_THIRD_PARTY` — ver §5.2 |
| `seedId` | ObjectId? | → `seeds`, quando o evento vira matéria-prima de contexto |

### 5.1 · Data de reunião tem que ser campo `[C]`

Das 23 atas do Puket, **apenas 3 têm `Data da Reunião` preenchida**. A data real vive **dentro do
título**, como texto — e há um caso em que o título (*"Weekly 05/12/24"*) **não bate** com a data de
criação (29/08/2024) `[C]`.

> **Sem `occurredAt` como campo, não há como ordenar, filtrar, nem disparar trigger por data.**
> É item de especificação, não reclamação de formatação.

### 5.2 · `disclosurePolicy` — uma regra de negócio que hoje só existe na cabeça de quem atende

Em 29/01/2026, um fornecedor pediu o nome de quem havia alterado uma referência. O registro do
atendimento diz: *"Informei que não podemos passar"* `[C]`. E em 20/01/2026, outro caso idêntico:
*"Perguntou quem inseriu o consumo incorreto... foi a simone mas não informei"* `[C]`.

> **Duas vezes, a mesma regra, aplicada por julgamento individual e registrada em texto livre.**
> Quem atende sabe; o sistema não. Quando o agente do BrainHub responder no lugar da pessoa, ele
> **precisa** dessa regra como campo. `NEVER_TO_THIRD_PARTY` existe por causa desses dois tickets.

---

## 6 · Vocabulário travado — o que veio da fonte, sem tradução

**`Tipo de Chamado`** `[C]`, exatamente como a origem escreve:
`TAREFA/CONFIG` · `USABILIDADE` · `INSTABILIDADE` · `BUG` · `NOVO ACESSO` ·
`MELHORIA NA PLATAFORMA` · `BURLAR PROCESSO` · `FINANCEIRO` · `OUTROS`

> 🔴 **`BURLAR PROCESSO` é uma categoria oficial de chamado.** Sete ocorrências, **todas na NV**
> `[C]`. Um cliente tentando contornar o processo é evento nomeado, não acidente — e isso é
> informação de produto, de atendimento e de risco ao mesmo tempo.

**`Status`** `[C]`: `Não iniciada` · `Em Aberto` · `Pendente` · `Resolvido` · `Fechado`

> ⚠ **`Resolvido` e `Fechado` coexistem sem diferença declarada.** Não invente a distinção —
> registre como `[D]` e pergunte a quem atende.

**Invariante P7. Preservar a grafia da origem.** A tabela da Caedu tem `Caedu- Planejamento` com
espaço a mais, `Caedu-Admim` por *Admin*, e data `08/11/0202` `[C]`. O Portal escreve `Basíco&Co` e
o Mapa escreve `Básico&Co`; o Portal escreve `StudioZ` e o Mapa `Studio Z` `[C]`.
**Corrigir é na fonte.** No banco, entra `rawValue` + `normalizedValue`, e a divergência vira
alerta de reconciliação — **quase contei os dois como clientes distintos.**

---

## 7 · Como isso vira indexação do cérebro

O elo com a **ESPEC-BANCO-001** é um só e é direto:

```
communication_event  ──► seeds  ──► context_pack_version  ──► context.published
   (uma ata, um chamado)      (matéria-prima)     (imutável, content-addressed)
```

`communication_events.seedId` é a ponte. Um chamado de `INSTABILIDADE` na NV vira `seed`, entra no
`context_pack` da área, e o brain da NV passa a saber que aquilo aconteceu — **com participante,
data, área e ferramenta**, que é exatamente o que falta hoje.

**Invariante P8.** Um `communication_event` só vira `seed` com `disclosurePolicy` avaliada. Evento
`NEVER_TO_THIRD_PARTY` **nunca** entra em `context_pack` que atravesse `federation_connection`.

---

## 8 · O que levar ao negócio antes de implementar

1. **A instrumentação de chamado parou.** 182 tickets em 24 dias de janeiro de 2026, e **106 ainda
   abertos** `[C]`. Foi piloto, foi abandono, ou migrou para outro sistema? **Sem isso, `people` já
   nasce com a série temporal interrompida.**
2. **Clientes `Churn` e `Inativo` abriram chamado em janeiro de 2026** — Lenny Niemeyer (5),
   Básico&Co (2), Paloma Concept, Susie Modas `[C]`. **Status na base ≠ uso real da plataforma.**
   Qual das duas verdades o banco vai gravar?
3. **`Resolvido` × `Fechado`** — decidir ou fundir. `[D]`
4. **Retenção e base legal** para histórico de ação de pessoa identificada. `[D]`
5. **`TEX`, `Certificação`, `Projetos`, `BI`** — resolver o mapeamento de área do Puket, ou aceitar
   `UNRESOLVED` permanente. `[D]`

## Fontes
| Bloco | Fonte | Data |
|---|---|---|
| 182 chamados, tipos, status, e-mails | Notion — `Chamados & Atendimentos` (`collection://2c5b1d38-e768-805a-99b1-000b4da25cc4`) | varrido 21/09/2026 |
| 43 usuários e 13 perfis do Puket | Notion — página `Puket`, tabela do PLM | varrido 21/09/2026 |
| 93 usuários e 14 perfis da Caedu | Notion — página `Caedu`, tabela do PLM | varrido 21/09/2026 |
| 23 atas e o campo de data vazio | Notion — `Reuniões com o cliente (1)` | varrido 21/09/2026 |
| Grupos de WhatsApp, Kanbanize, uBuy, uPlan | Notion — página `Reserva` | varrido 21/09/2026 |
| Duas listas de cliente divergentes | Notion — `Mapa de Clientes` × `Portal do Cliente` | varrido 21/09/2026 |

## Governança
### Quem pode alterar este documento
Vinicius Risoléo. **Este documento é a autoridade sobre pessoa e comunicação no banco** — a
`_espec-banco-brainhub.md` fica `SUPERSEDED` no que tratar desses dois assuntos.

### Procedência
Escrito em 21 set 2026 a partir da varredura ao vivo do Notion, durante o preenchimento dos brains
de Caedu e Puket. **Nenhuma afirmação `[C]` foi escrita sem a fonte ao lado.**
