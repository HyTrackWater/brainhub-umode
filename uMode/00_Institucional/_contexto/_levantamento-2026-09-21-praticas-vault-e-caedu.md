---
aliases:
  - "Levantamento 21 set 2026 — práticas do vault, estado dos repos e a lacuna da CAEDU"
---
# Levantamento 21 set 2026 — práticas do vault, estado dos repos e a lacuna da CAEDU

> Verificação direta, a pedido do Vinicius. Missão declarada por ele nesta data: **chegar ao brain
> mais completo possível de empresas e pessoas — uMode e clientes — com a CAEDU como alvo da próxima
> semana.**
>
> **Aliases travados nesta data:** **corpus** = `HyTrackWater/brainhub-umode` (nosso, único gravável)
> · **front** = `UmodeApp/umode-brainhub` · **api** = `UmodeApp/umode-brainhub-api` · **vault** =
> `HyTrackWater/umode-os-vault` · **legado** = `HyTrackWater/design-system-hub` ·
> **cx-hub** = `CX Hub/gist-sparkle-d86e356b` · **uflow** = `UmodeApp/umode-flow`.

## 0 · Declaração de completude

| # | O que este documento NÃO resolve | Por quê |
|---|---|---|
| 1 | Estado atual do **api** e do **front** | Buscados (307 e 199 refs), **ainda não lidos** na `awscicd` |
| 2 | Conteúdo do commit do João de 02/09 | Puxado, **ainda não lido** (1.971 linhas) |
| 3 | Fontes fora do Git (Notion, Drive, CX Hub rodando) | Varredura ainda não feita |
| 4 | Vault atualizado | 🔴 **acesso ainda bloqueado** — ver §1 |

## 1 · Pulls de 21 set 2026

| Alias | Antes | Depois | Nota |
|---|---|---|---|
| **corpus** | `71e3279` (19/08) | ✅ **`9ef6be4`** (02/09) | estava 1 commit atrás |
| **front** | 🔴 1 ref, single-branch | ✅ **199 refs** · `awscicd` `44e8476` | refspec corrigido |
| **api** | 115 refs | ✅ **307 refs** · `awscicd` `9979ac9c` | **commit de 21/09** |
| **uflow** | 388 refs | ✅ 390 refs · mais novo 14/09 | branch `master` |
| **cx-hub** | — | ✅ 2 refs · mais novo 04/08 | `CX Hub\gist-sparkle-d86e356b` |
| **integrações** | 11 repos | ✅ todos atualizados | `integracao-linx-nv` 01/09 · `integration-osklen-linx` 18/09 · `integration-objetiva-illimitar` 1→3 refs |
| **vault** | 15 refs | 🔴 **bloqueado** | |
| **legado** | 1 ref | 🔴 **bloqueado** | |

### 🔴 O bloqueio do vault — diagnóstico exato
A chave SSH desta máquina autentica como **`vinicius-risoleo-umode`** — confirmado por
`ssh -T git@github.com` — que é exatamente a conta a quem o acesso foi concedido. Mesmo assim:

```
git ls-remote git@github.com:HyTrackWater/umode-os-vault.git
  → ERROR: Repository not found.
```

> **Diagnóstico: o convite de colaborador está pendente de aceite.** O GitHub responde
> `Repository not found` (e não `Permission denied`) justamente quando a conta ainda não aceitou.
> **Ação: aceitar em `github.com/HyTrackWater/umode-os-vault/invitations`** — e o mesmo para o
> `design-system-hub`.
>
> Enquanto isso, o clone local do vault serve, **mas é de 24 ago** e não pode ser atualizado.

## 2 · As boas práticas do vault — investigadas, e nós não temos quase nenhuma

### 2.1 Slug de cliente: minúsculo com hífen, e é a pasta
**49 pastas de cliente** no vault (`BrainHub/uMode/_Clientes/`). **1 com maiúscula, 0 com espaço.**
Exemplos: `alinvest-ift`, `basico-co`, `beira-rio`, `luiza-barcelos`, `caedu`.

**No corpus a pasta é o nome comercial:** `Caedu`, `Luiza Barcelos`, `Cambos` — com maiúscula e
espaço. É divergência direta, e a nossa própria `CLAUDE.md` a institui
(*"Pasta de cliente usa o nome comercial direto"*).

> ⚠ Nós **temos** o slug estável — mas como **campo dentro do MD** (`### ID do cliente`), não como
> nome de pasta. O vault usa o slug **como caminho**, o que torna o caminho previsível e indexável
> sem abrir o arquivo.

### 2.2 Nomenclatura de arquivo: `<slug>_YYMMDD_<assunto>.md`
Dos 116 `.md` em `_Clientes` do vault, **34 seguem** o padrão datado:
`alinvest-ift_260119_contrato-mentoria.md` · `arezzo_241100_dores-solucoes-oracle-azzas.md` ·
`caedu_260600_proposta-12-meses.md`.

E convivem com dois outros tipos:
- **`_<slug>.md`** — a nota-índice do cliente (`_4takes.md`, `_alinvest-ift.md`)
- **`00_README.md`, `00_CONTEXT_AGENTE.md`** — contexto de pasta

> **Leitura:** o vault separa **artefato datado** (proposta, contrato, ata — o nome carrega cliente,
> data e assunto) de **nota viva** (o `_<slug>.md`, que é o hub). **O nosso corpus só tem nota viva**
> — `institucional.md`, `jornada.md`, `pessoas.md` — e **nenhum lugar para artefato datado**.
> É por isso que proposta, contrato e ata de visita não têm onde morar no nosso padrão.

### 2.3 Front-matter: 99 de 120 MDs amostrados têm, e os campos têm função
| Campo | Frequência | Para que serve |
|---|---:|---|
| `origem` | 99 | quem produziu (codex, hermes, claude, humano) |
| `tipo` | 99 | classifica o documento — **alimenta o catálogo** |
| `entidade` | 98 | a que cliente/sistema pertence — **alimenta o índice** |
| `sync` | 98 | `manual` / `exclude` — **controla promoção** |
| `criado_em` | 92 | data |
| `promovido_em` / `promovido_por` | 30 | trilha de promoção ao canônico |
| `importado_por` | 25 | procedência de importação |
| `atualizado_em` | 18 | |
| `resgatado`, `balde`, `uso`, `ingerido_em`, `extraido_em` | 6–14 | estágios da esteira de ingestão |

**No corpus: 0 de 1.335 MDs têm front-matter.**

### 2.4 Índice e catálogo: existem como arquivo e como política
`CATALOGO.md` · `DECISOES.md` · `SISTEMAS.md` · `_GOVERNANCA.md` na raiz ·
`_sistema/_INDEX.md` · `_sistema/TRIAGEM_DECISOES.md` · `_sistema/context-index/C4-sistemas.md` ·
**`BrainHub/uMode/_Clientes/_Clientes.md`** (índice de clientes) ·
**`_sistema/brainhub/governance/politica-catalogo-index-orfaos.md`** — há política escrita sobre
catálogo, índice e **documentos órfãos**.

**No corpus: nenhum desses arquivos existe.** Temos `_indice/*.csv` derivado por script — que é bom
para importação, **mas não é navegável nem tem política de órfão**.

### 2.5 Conexões e wikilinks
Vault: **152 de 250** MDs amostrados têm seção `## Conexões` com `[[wikilinks]]`.
Corpus: **8 de 1.335** têm seção Conexões; **6** têm wikilink.

### 🔴 Autocrítica registrada
Em 17 ago 2026 (pendência 191) **eu decidi não adotar front-matter**, argumentando que o `_indice/`
derivado já era o contrato. **O argumento era sobre importação para o banco.** O front-matter do
vault serve a outra coisa — **governança**: `sync` controla promoção, `tipo` e `entidade` alimentam
catálogo e índice, `promovido_por` dá trilha.

> **Avaliei uma prática pelo critério errado e descartei.** A decisão do `_indice/` continua válida
> para importação; **a conclusão de que front-matter era redundante, não.** São mecanismos com
> propósitos diferentes e ficamos sem o segundo.

## 3 · A CAEDU — o quadro exato

### 3.1 No corpus: estrutura completa, conteúdo quase vazio
`uMode/_Clientes/Caedu/` tem **as 14 áreas + `00_Institucional`** ✅ e **33 arquivos**:

| O que | Quantos | Estado |
|---|---:|---|
| `institucional.md` · `jornada.md` · `pessoas.md` | 3 | existem, **com lacunas** |
| Demandas `D-2025-001` … `D-2026-012` | 28 | 22–26 lacunas cada |
| RFIs `RFI-2025-001` … `RFI-2026-003` | 4 | com narrativa real do Notion |
| **`contexto-area.md` nas 14 áreas** | **0 de 14** | 🔴 **as áreas estão vazias** |

**Total: 691 ocorrências de `[a preencher]`, em 33 de 33 arquivos.**

> **Diagnóstico:** o esqueleto está de pé e a camada de demanda/RFI foi importada do Notion. **O que
> falta é o miolo:** quem são as pessoas, o que cada área faz, quais ferramentas estão contratadas.
> Exatamente o que a missão pede.

### 3.2 No vault: pouco arquivo, muita menção
| Onde | O que há |
|---|---|
| `_Clientes/caedu/caedu_260600_proposta-12-meses.md` | a proposta de 12 meses |
| `_Clientes/caedu/notion/FORMS.csv` | export de formulários do Notion |
| `_arquivo-morto/.../DISTILADO_caedu-feedback-visita-van_2026-07-28.md` | ata destilada de visita (28/07) |
| **77 arquivos do vault citam CAEDU** | escada de valor, mapa de clientes do Notion, feedback de clientes, MEGA_AGENTE do CX Hub, narrativa e one-pager institucionais |

> **A informação da CAEDU existe — está espalhada em 77 arquivos do vault e em fontes fora do Git.**
> O trabalho não é criar do zero: é **rastrear, consolidar e padronizar**.

## 4 · Quanto teríamos que adequar a estrutura — não respondido hoje

O **api** foi de 115 para **307 refs** e tem commit de **21/09**; o **front** de 1 para **199**.
Tudo que li do banco foi numa **branch de slice de agosto**, e o PRD que temos é da **era Supabase**.

> **Afirmar conformidade agora seria repetir o erro que já cometi duas vezes.** A resposta exige
> reler o **api** em `awscicd` (`9979ac9c`) e o **front** em `awscicd` (`44e8476`) — este último
> nunca lido.

## 5 · Fontes ainda não varridas

Notion (principal) · CX Hub em execução · Drive · `cx-hub` repo · os 11 repos de integração ·
**pendente:** repositório de documentação da integração **Moda Objetiva** (acesso solicitado ao
desenvolvedor, ainda não concedido).

## Fontes
Verificação direta em 21 set 2026 · `_levantamento-2026-08-19-repos-e-prd.md` ·
`_recebido-2026-08-18-context-pack-brainhub-2.0.md` · vault em
`origin/governance/brainhub-v1.5` (clone de 24/08)

## Governança
Somente o CEO altera conteúdo no BrainHub. **Estado de repositório vence com um `fetch`** — refazer
a verificação antes de citar qualquer número deste documento.
