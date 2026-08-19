# Levantamento 19 ago 2026 — os cinco repositórios, e onde o PRD está de fato

> Feito por **verificação direta na máquina do Vinicius**, não por leitura do pacote de contexto. O
> pacote do João (18/08) aponta caminhos da máquina **dele**; aqui está o que existe **aqui** e o que
> falta buscar.
>
> **Autorização reconfirmada em 19 ago 2026:** leitura em todos os repositórios. **Escrita somente no
> `HyTrackWater/brainhub-umode`.** Sem commit, push ou checkout fora dele.
>
> Complementa o `_inventario-repositorios.md`, que continua sendo a autoridade sobre **papéis**;
> aqui é a autoridade sobre **estado dos clones e localização do PRD**.

## 1 · Onde o PRD está — resolvido

O Vinicius supôs que estivesse no repo da API. **Não está.** Verifiquei por arquivo adicionado em
**todas as 115 refs** do `umode-brainhub-api`: nenhum arquivo com `prd` ou `prumo` em commit algum.

**Está no vault, e só numa branch:**

| Item | Valor |
|---|---|
| Repositório | `HyTrackWater/umode-os-vault` |
| **Branch** | **`governance/brainhub-v1.5`** — **não está na `main`** |
| Caminho | `BrainHub/uMode/03_Produto-e-Solucoes/brainhub/PRD-brainhub-prumo.md` |
| Tamanho | **59.427 bytes · 612 linhas** |
| Última alteração do arquivo | **09 ago 2026**, commit `a6930d3` — *"promo: BrainHub gradua a PRODUTO — cluster migra 04_Dados-e-IA → 03_Produto-e-Solucoes"* |
| Estrutura | 18 seções + Conexões. O **§7 "Features detalhadas (por módulo)"** tem ~58 linhas de item |
| `governance/brainhub-v1.5` × `main` | `0 83` — a `main` é ancestral; a branch está **83 commits à frente** |

**Para abrir sem tocar em nada:**

```bash
git -C "C:\Ambientes Virtuais\BrainHub - João Risoléo\umode-os-vault" \
  show "origin/governance/brainhub-v1.5:BrainHub/uMode/03_Produto-e-Solucoes/brainhub/PRD-brainhub-prumo.md"
```

### 🔴 O achado que importa mais que a localização

**O PRD que temos é da era Supabase/Lovable.** O **§6** declara como baseline o
`warm-weaving.lovable.app` sobre **Supabase + RLS + Edge Functions**, e o **§11 chama-se literalmente
"Modelo de dados (Supabase)"**, com ~30 tabelas. As decisões do §18 são de **21 jul 2026**.

**Mas o runtime do BrainHub 2.0 é MongoDB/NestJS, com 37 collections.**

> **Ninguém reescreveu o §11 para a era Mongo.** O PRD segue válido para features, jornadas, personas,
> níveis de acesso e integrações — e está **obsoleto exatamente na seção de modelo de dados**.
>
> É essa a lacuna que o `_dicionario-dados-brainhub.md` e a `ESPEC-BANCO-001` preenchem: elas **são**
> a tradução Mongo do §11. **Não é trabalho paralelo — é a seção que falta.**

### E o Inbox não é folha em branco

O **§11 do PRD lista `inbox_items`, `approval_requests`, `operator_requests`, `context_queues` e
`job_runs`** entre as tabelas do baseline Supabase **a preservar e mapear**. Cruzando com o pacote do
João, que classifica `Inbox` como **"ausente"** no runtime (§9.3) e **sem ADR** (§12.2, item 5):

> **O Inbox está especificado no PRD, existe no legado Supabase, está ausente no runtime Mongo e não
> tem ADR.** Nossa espec entra como **a modelagem Mongo dele** — não como proposta nova. Isso muda o
> enquadramento: deixa de ser "ideia nossa" e passa a ser "a tradução que ninguém fez".

## 2 · Os documentos da RÉGUA não estão no nosso alcance

O pacote baseia os **60,5%** na régua P18. Verifiquei: **nenhum dos quatro documentos de medição
existe em qualquer ref do nosso clone do vault.**

| Documento | No nosso clone |
|---|---|
| `2026-08-17-BHP-MEDICAO-PRD-AWSCICD-P18.md` | ❌ ausente |
| `2026-08-15-COMPLETUDE-FEATURE-PRD-V2.md` | ❌ ausente |
| `2026-08-17-BHP-P20-CONTRACT-TRUTH-REPORT.md` | ❌ ausente |
| `2026-08-15-REGUA-RECONCILIADA-BH20.md` | ❌ ausente |

**Motivo, verificado:** o remoto do vault **não avança desde 12 ago** (`e847623`) — e o nosso clone
**está em dia com o remoto**. Ou seja: **não é defasagem nossa, é conteúdo não publicado.** Os
`inbox/codex/` e `inbox/claude/` de 15–17 ago vivem só na máquina do João.

> **Consequência prática:** conseguimos ler o **PRD**, mas **não a régua** que o converte em 98 pontos
> por lado. O §7 do PRD tem ~58 itens, não 98 — o peso é derivado em documento que não temos.
> **Portanto não podemos reproduzir nem auditar o percentual.** Qualquer número nosso seria uma
> **segunda régua**, que é precisamente o defeito que o pacote alerta em §9.1 ("não misturar o número
> antigo de 37,8% com a régua P18").

## 3 · Estado real dos clones, e o que falta buscar

| Repositório | Caminho local | Refspec | Estado | Ação |
|---|---|---|---|---|
| `HyTrackWater/brainhub-umode` (**nosso**) | `...\BrainHub\brainhub-umode` | completo | ✅ em dia · **único gravável** | nenhuma |
| `HyTrackWater/umode-os-vault` | `...\BrainHub - João Risoléo\umode-os-vault` | `+refs/heads/*` ✅ | ✅ **em dia com o remoto** (`e847623`, 12/08) · 11 branches | nenhuma nossa. Falta o **João publicar** os `inbox/` de 15–17/08 |
| `UmodeApp/umode-brainhub-api` (**backend**) | `...\BrainHub - API e Banco\umode-brainhub-api` | `+refs/heads/*` ✅ | ⚠ **atrasado**: `awscicd` local `ce54d85` (17/08); o pacote cita `24781c7` (18/08). `main..awscicd` = **`0 393` local** × `0 468` no pacote | **`git fetch --all --prune`** |
| `UmodeApp/umode-brainhub` (**frontend**) | `...\BrainHub - Frontend\umode-brainhub` | 🔴 **`+refs/heads/main:refs/remotes/origin/main`** | 🔴 **CLONE SINGLE-BRANCH.** 1 ref remota. **`awscicd` AUSENTE.** Só a `main`, em `80582cb` | **corrigir refspec + buscar tudo** |
| `HyTrackWater/design-system-hub` (legado) | `...\BrainHub Lovable\design-system-hub` | — | legado preservado, **não é runtime** | nenhuma |

⚠ **O caminho do frontend é um nível mais fundo** do que o informado: o `.git` está em
`BrainHub - Frontend\umode-brainhub`, não em `BrainHub - Frontend`.

### 🔴 A armadilha do `--single-branch` reapareceu — agora no frontend

É **exatamente** o erro que me fez declarar módulos inexistentes na API semanas atrás. O frontend está
clonado só com a `main`, e a `main` do front está — pelo pacote — **28 commits atrás e 1 commit
divergente** da `awscicd`.

> **Se eu lesse o frontend agora, concluiria que está quase vazio, e estaria errado pelo mesmo motivo
> da vez anterior. Por isso não li nada dele.**

### Comandos para o Vinicius rodar

```bash
# 1. FRONTEND — tirar do single-branch e buscar todas as branches
cd "C:\Ambientes Virtuais\BrainHub - Frontend\umode-brainhub"
git config --unset-all remote.origin.fetch
git config --add remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
git fetch --all --prune

# 2. BACKEND — só atualizar (o refspec já está correto)
cd "C:\Ambientes Virtuais\BrainHub - API e Banco\umode-brainhub-api"
git fetch --all --prune

# 3. conferir que a linha de integração apareceu nos dois
git -C "C:\Ambientes Virtuais\BrainHub - Frontend\umode-brainhub"        rev-parse --short origin/awscicd
git -C "C:\Ambientes Virtuais\BrainHub - API e Banco\umode-brainhub-api" rev-parse --short origin/awscicd
```

### As branches que eu preciso poder ler

| Repo | Branch | Para quê |
|---|---|---|
| backend | **`origin/awscicd`** | é a linha de integração — **tudo que li antes veio de uma branch de slice**, não dela |
| frontend | **`origin/awscicd`** | idem; a `main` não representa o estado |
| vault | **`origin/governance/brainhub-v1.5`** | é onde o PRD vive |
| ambos | `origin/main` | só para medir divergência de promoção |

**Não preciso de branch de slice.** As `codex/*` são trabalho em curso — ler slice foi justamente o
meu erro anterior.

## 4 · Correções que este levantamento impõe aos nossos documentos

| Onde eu errei | Correção |
|---|---|
| `_dicionario-dados-brainhub.md`: *"está construído e não integrado"* | **Errado.** `awscicd` **é** a linha de integração e está **393–468 commits à frente da `main`**. O certo: **integrado em `awscicd`, não promovido para `main`.** |
| Toda a faixa `[C]` do dicionário e do fluxo | Foi lida em **`codex/bhp-p16-federation-grants-back`** — uma **slice**, não `awscicd`. Vale como "existe numa slice", não como estado da integração. |
| `_espec-banco-brainhub.md` §6.2: *"17 automações que não sobrevivem ao notebook desligado"* | **Confundi duas coisas.** A plataforma **existe**: EB, ECS Fargate, Atlas, Redis Cloud, staging em pé, Terraform. A frota Hermes no Mac do João é **governança do processo de desenvolvimento**, não runtime de produto. |
| Contagem de collections | Contei **50 arquivos `*.schema.ts`**; o pacote conta **37 nomes de collection**. Os dois podem estar certos (várias schemas por collection). Mas eu **nunca vi** `cost_daily_counters`, `file_versions`, `llm_connections` nem `llm_credentials` — e a última é o meu `[a preencher] llmConnectionId`. |
| Grade `[C]/[F]/[P]/[D]` | **Duas linguagens para a mesma ideia** — o mesmo defeito do "coleção × collection". Adotar a **escada de 8 degraus do pacote** (`CODE_PRESENT` → `PRODUCTION_VERIFIED`) para afirmações sobre a plataforma; manter `[P]/[D]` só para proposta e decisão nossa. |

## 5 · O nosso repositório está mal classificado na fonte do João

O pacote, §3.6, lista o `HyTrackWater/brainhub-umode` como *"variante antiga/PowerShell; não foi
validada como runtime atual"* — na mesma seção do legado `design-system-hub`, sob o título
**"repositórios que não devem ser confundidos"**.

> **Ele nunca foi candidato a runtime.** É o **corpus de contexto**: 1.316 MDs padronizados, com chave
> estável de cliente e índice derivado. Enquanto estiver catalogado como runtime reprovado, nenhum
> agente do João vai olhar para ele.
>
> **Ação: corrigir o papel no `SISTEMAS.md` do João.** É conversa do Vinicius com ele — não é
> alteração que nos cabe fazer.

## Fontes
Verificação direta em 19 ago 2026 nos cinco repositórios locais ·
`_recebido-2026-08-18-context-pack-brainhub-2.0.md` (pacote do João) ·
`_inventario-repositorios.md` (papéis) · `_pendencias-gerais.md`

## Governança
Somente o CEO altera conteúdo no BrainHub. **Alteração aqui exige refazer a verificação** — este
documento é estado de clone, e estado de clone muda com um `fetch`.
