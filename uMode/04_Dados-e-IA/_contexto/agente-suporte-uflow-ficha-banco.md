# Ficha de inserção no banco — Agente de Suporte Técnico uFlow

> Escrita em **17 ago 2026**, depois de receber as fontes completas em
> `C:\Ambientes Virtuais\BrainHub\_insumos`. **Este documento é o payload pronto para inserção** nas
> collections `agents` e `agent_versions`, conforme a `ESPEC-BANCO-001 v2`.
>
> Campos em `[a preencher]` são **três**, e cada um está justificado no fim. Nenhum deles impede
> gravar o registro em `DRAFT` — que é o estado obrigatório de nascimento.

## Procedência das fontes — o que mudou em 17 ago 2026

| Fonte | Estado anterior | Agora |
|---|---|---|
| `TREINAMENTO-AGENTE-SUPORTE-UFLOW.md` | ❌ 818 de 1.084 linhas; Anexos D e E ausentes | ✅ **completo, 1.084 linhas**, Anexos D e E lidos |
| `Papel de Suporte.txt` | ⚠ conteúdo preservado, arquivo perdido | ✅ **arquivo em mãos**, 122 linhas |
| Instrução vigente | ❌ "nunca me foi enviada" | ✅ **estava na §14 do treinamento**, extraída verbatim |
| Repositório do PLM | ✅ em mãos | ✅ inalterado, 211 tabelas mapeadas |

### 🔴 O achado: existem DUAS versões de instrução, não uma
Eu pedi "a instrução vigente" supondo um arquivo único. **São duas, e formam linhagem real** — o que
é exatamente o que `agent_versions` existe para modelar:

| | Origem | Seções de resposta | O que tem que a outra não tem |
|---|---|---|---|
| **v1** | `Papel de Suporte.txt` | **6** | — |
| **v2** | §14 do treinamento | **7** (+ `Validar & Aprender`) | a pedagogia **HIC**, o **rito de SQL** (transação, pré-check, COMMIT), e as **4 armadilhas** nomeadas |

> **Portanto o agente não nasce com um snapshot: nasce com histórico.** A v1 entra como `version: 1`
> superseded, a v2 como `version: 2` `ACTIVE`. É a primeira prova real do versionamento de instrução
> no BrainHub.

## Artefatos versionados neste repositório

Extraídos **por script, não transcritos** — porque `contentHash` e `origin.commitSha` só valem se o
artefato for byte a byte o mesmo.

| Versão | Caminho | Chars | `contentHash` (sha256) |
|---|---|---|---|
| v1 | `uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow-instrucao-v1.txt` | 4.345 | `0342b490777efa27828afbf878e56fe805994a3be7bed8fdd398a9105f6d314f` |
| v2 | `uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow-instrucao-v2.txt` | 4.143 | `d0c4a21d9baa7b1f8864df439dcf791dd7854eefb130ff63446b031a48172edc` |

✅ **Ambas cabem folgado:** o limite de `agent_versions.instruction` é **100.000 chars**; a maior usa
**4,1%** dele.

---

## Documento para `agents`

```
slug              suporte-tecnico-uflow
name              Agente de Suporte Técnico uFlow
kind              AGENT                     -- não é WORKER/POLLER/SENTINEL/RECONCILER: atende pessoa
authorship        USER_DEFINED              -- (o campo `kind` atual, renomeado pela espec §2.3)
visibility        OPERATOR                  -- não é agente de sistema
lifecycle         DRAFT                     -- obrigatório: todo agente nasce DRAFT
sensitivityTier   T2                        -- travado por D85
stewardAreaId     06_Tecnologia             -- DECIDIDO: quem treina, retreina, aposenta, desativa
audienceMode      TENANT_WIDE               -- DECIDIDO: quase todos consultam
canonicalWrite    false                     -- agente não escreve no canônico
externalSend      false                     -- proibido por padrão
requiresGuard     true
activationApprovalBand  JOAO_REQUIRED       -- sair de DRAFT exige aprovação registrada
readScopes        ["contexts.read", "contexts.search"]
writeScopes       []                        -- não escreve nada
ownerPersonId     [a preencher · 1]
brainId/tenantId  o Second Brain da Casa uMode
```

### Permissões por área — a decisão de 17 ago 2026 aplicada
```
grant  agents.steward   → 06_Tecnologia    -- define como o agente trabalha
grant  agents.operate   → 02_Atendimento   -- usa direto, sem alterar instrução
agent_shares (nenhum por enquanto)         -- TENANT_WIDE + DENY quando necessário
```
> Exemplo do próprio Vinicius: para barrar o Comercial, cria-se um `agent_share` com
> `targetAreaId: 01_Comercial` e `effect: DENY`. **DENY vence ALLOW** — a precedência já está no
> código do filtro de audiência, não é regra nova.

---

## Documentos para `agent_versions`

### `version: 1` — a instrução original
```
version           1
status            (superseded pela 2)
instruction       ← conteúdo de agente-suporte-uflow-instrucao-v1.txt
contentHash       sha256:0342b490777efa27828afbf878e56fe805994a3be7bed8fdd398a9105f6d314f
origin.kind       git-template
origin.repo       HyTrackWater/brainhub-umode
origin.path       uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow-instrucao-v1.txt
origin.commitSha  ← o commit que introduziu o arquivo
tools             []
contextPackRefs   []
limits            timeoutSeconds 900 · maxOutputTokens 64000
providerPolicy    [a preencher · 2]
```

### `version: 2` — a vigente, pós-aprendizagem
```
version              2
status               ACTIVE
supersedesVersionId  ← o _id da version 1
instruction          ← conteúdo de agente-suporte-uflow-instrucao-v2.txt
contentHash          sha256:d0c4a21d9baa7b1f8864df439dcf791dd7854eefb130ff63446b031a48172edc
origin.kind          git-template
origin.repo          HyTrackWater/brainhub-umode
origin.path          uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow-instrucao-v2.txt
origin.commitSha     ← o commit que introduziu o arquivo
tools                []
contextPackRefs      [a preencher · 3]
limits               timeoutSeconds 900 · maxOutputTokens 64000
providerPolicy       [a preencher · 2]
```

---

## Os três campos em aberto, e por que cada um está aberto

| # | Campo | Por que falta | Quem responde |
|---|---|---|---|
| **1** | `ownerPersonId` | Depende de o `people` do BrainHub ter a pessoa cadastrada. É id do banco, não decisão. | ao inserir |
| **2** | `providerPolicy` — `defaultModel`, `allowedProviders[]`, `llmConnectionId`, `maxCostPerRunUsd` | **Eu não sei qual modelo o agente usa hoje.** Não está em nenhuma das duas fontes — o treinamento fala do comportamento, nunca do provedor. | **Vinicius** (uma frase) |
| **3** | `contextPackRefs[]` | O pack precisa de `contexts` populado, que precisa do importador, que precisa de `contexts.type` (**onda 1** da espec). | dependência de implementação |

⚠ **Sobre o item 3, e é o ponto que mais importa para a qualidade:** sem `contextPackRefs`, este
agente responde **só pela instrução** — sem `sources[]`, sem citar contexto, sem rastreio de qual
documento sustentou a resposta. Funciona, mas **perde a garantia de zero alucinação**. O pack natural
dele é: `uflow-modelo-de-dados.md` (211 tabelas), `agente-suporte-uflow.md` (as 4 armadilhas e os
5 anexos) e os protocolos de suporte.

## Fontes
`_insumos/TREINAMENTO-AGENTE-SUPORTE-UFLOW.md` (1.084 linhas, completo) ·
`_insumos/Papel de Suporte.txt` (122 linhas) · `agente-suporte-uflow.md` (o contexto estruturado) ·
`_espec-banco-brainhub.md` v2 §1.2-bis e §2.3 · demanda `D-2026-002`

## Governança
Somente o CEO altera conteúdo no BrainHub. **Alterar as instruções versionadas é proibido:** os
arquivos `.txt` são artefatos imutáveis endereçados por hash. Instrução nova = **arquivo novo com
versão nova**, nunca edição do existente — é o que sustenta `contentHash` e `origin.commitSha`.
