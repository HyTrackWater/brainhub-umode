# Inventário de repositórios — origens e papéis no nosso desenvolvimento

> Levantado em **17 ago 2026** por varredura somente leitura do disco (33 repositórios git
> encontrados). **Nenhum `fetch`, nenhum `pull`, nenhuma alteração em nenhum repositório.**
>
> Objetivo: dizer o que é cada repositório, qual papel ele tem no **nosso** trabalho, e o que precisa
> ser atualizado antes de seguirmos.

## 🔒 Regra de autorização vigente neste momento
**Estamos autorizados a escrever em UM único repositório: `HyTrackWater/brainhub-umode`** — o que o
Vinicius começou e que preenchemos seguindo o nosso padrão.

Todos os demais são **somente leitura**: sem edição, sem commit, sem push, sem `fetch`. Isso inclui
explicitamente o vault do João e o frontend do BrainHub no Lovable. Declarado por Vinicius em
17 ago 2026.

## ⚠ Defasagem detectada
| O quê | Estado |
|---|---|
| Nossa documentação | escrita em **04 ago**; hoje é **17 ago** — 13 dias sem atualização |
| Clone local do vault do João | último commit **28/07** — pelo menos **20 dias defasado**, e ele avançou muito |
| Frontend do BrainHub (Lovable) | **não está no disco** — foi substituído pelo vault na mesma pasta |
| Nosso repositório | 3 arquivos não commitados, da sessão de 04/08 |

---

## Os cinco papéis

### A · O nosso — única fonte de verdade do nosso padrão
| Repositório | Caminho | Último commit |
|---|---|---|
| `HyTrackWater/brainhub-umode` | `BrainHub\brainhub-umode` | 04/08 · vinicius-risoleo-umode · 23 commits · **3 alterações pendentes** |

Papel: onde o padrão vive e onde escrevemos. 1.328 `.md`, 46 clientes, 998 demandas, 85 RFIs,
16 Soluções, 11 integrações. É o único repositório com autorização de escrita.

### B · Padrão de referência — o vault do João
| Repositório | Caminho | Último commit |
|---|---|---|
| `HyTrackWater/umode-os-vault` | `BrainHub - João Risoléo\umode-os-vault` | **28/07** · joaorisoleo · 145 commits |

Papel: **é a régua de comparação de contexto.** Trabalho equivalente ao nosso, feito em paralelo, com
mecanismos que nós não temos (`_CANON.md`, `MANIFEST.md`, `DECISOES.md`, `SYNC_EXCLUDE.md`, front-matter
em 75% dos arquivos, `inbox/` + promoção). É a fonte da comparação em
`_decisoes-convergencia-proposta.md`.
**Precisa de `pull`** — 20 dias defasado, e o próprio Vinicius diz que avançou muito.

### C · A aplicação — o BrainHub do Lovable
| Repositório | Caminho | Estado |
|---|---|---|
| `HyTrackWater/design-system-hub` | — | **🔴 AUSENTE DO DISCO** |

Papel: **é o produto** — o frontend em `brainhub.umode.tech`, projeto Lovable `8c3e784d`, Supabase
`wjghatmsywcjvpumzonu`. É onde estão as abas de navegação, os agentes criados pelo João, as
aprovações e as interações que precisamos inventariar.
⚠ **Este é o repositório mais importante para o objetivo da semana e ele não está aqui.** Estava na
pasta `BrainHub - João Risoléo` numa sessão anterior e foi substituído pelo vault. **Precisa ser
clonado de novo** — sem ele não há inventário de abas, agentes nem regras da aplicação.
O nome engana: **é um console de BrainHub, não um design system** — o nome é resíduo do projeto Lovable
original, nunca renomeado.

### D · Fontes de conteúdo e de contexto — leitura para enriquecer o nosso
| Repositório | Caminho | Último | Papel |
|---|---|---|---|
| `UmodeApp/umode-flow` | `uFlow\umode-flow` | 03/08 · Bergson · 12.613c | **A plataforma legada (PLM).** Contexto do agente da `D-2026-002`; `db/schema.rb` com 211 tabelas |
| `HyTrackWater/gist-sparkle-d86e356b` | `CX Hub\gist-sparkle-d86e356b` | **04/08** · bot · 2.495c | **CX Hub** — onde as demandas executáveis nascem. Hierarquia Programa→Projeto→Demanda→Subdemanda |
| `HyTrackWater/integration-pulse-check-e914756f` | `integration-pulse-check-e914756f` | 27/05 · bot · 190c | **IntHub** — monitor de integrações. João o chama de *gold standard de formato* |
| `HyTrackWater/smart-code-hug` | `AlocAI\umode-design-guardian` | 13/07 · vinicius · 182c | **AlocAI** — ⚠ ver divergências de nome abaixo |
| `UmodeApp/arzz-sap` | `uMode-Integracoes\arzz-sap` | 17/06 · Felipe Sindeaux · 229c | Integração **Reserva + Oficina Reserva** (SAP) |
| `UmodeApp/integracao-linx-nv` | `uMode-Integracoes\...` | 23/07 · Felipe Sindeaux · 378c | Integração **NV** |
| `UmodeApp/integration-nk-linx` | `uMode-Integracoes\...` | 23/07 · Felipe Sindeaux · 130c | Integração **NK STORE** |
| `UmodeApp/integration-osklen-linx` | `uMode-Integracoes\...` | 23/07 · Felipe Sindeaux · 93c | Integração **Osklen** |
| `UmodeApp/integration-lofty-linx` | `uMode-Integracoes\...` | 23/07 · Felipe Sindeaux · 70c | Integração **Lofty Style** |
| `UmodeApp/integration-baw-linx` | `uMode-Integracoes\...` | 23/07 · Felipe Sindeaux · 74c | Integração **Baw** |
| `UmodeApp/integration-vix-linx` | `uMode-Integracoes\...` | 23/07 · Felipe Sindeaux · 164c | Integração **VIX** |
| `UmodeApp/integration-luiza-barcelos-sft` | `uMode-Integracoes\...` | 25/06 · Felipe Sindeaux · 26c | Integração **Luiza Barcelos** (Safe Tech) |
| `UmodeApp/integration-cambos-spi` | `uMode-Integracoes\...` | 25/06 · Felipe Sindeaux · 81c | Integração **Cambos** (SPI) |
| `UmodeApp/unico-linx` | `uMode-Integracoes\unico-linx` | **26/01/2023** · Saulo Arruda · 25c | Integração **Puket** — sem nenhum `.md`, e é o mais antigo de todos |

### E · Produtos do Portfólio com clone local — não vistoriados ainda
| Repositório | Caminho | Último | Produto provável |
|---|---|---|---|
| `HyTrackWater/umode-planejai` | `PlanejAi\umode-planejai` | 30/07 · vinicius · 1.127c | **PlanejAI** |
| `HyTrackWater/umode-catalog-ai` | `umode-catalog-ai` | 31/07 · vinicius · 815c | candidato a **EnriqueceAI/CadastrAI** — o MANIFEST do João marca como `_ARQUIVADO` |
| `HyTrackWater/criai-vision-board-9d1195a1` | `criai-vision-board-9d1195a1` | **02/08** · vinicius · 2.410c | **CriAI** |
| `HyTrackWater/criai-vision-board-9d1195a1` | `criai-vision-board-original` | 15/07 · bot · 2.382c | **CriAI** — mesmo remote, segundo clone |
| `HyTrackWater/criai-vision-board` | `CriAI NV\criai-vision-board` | 09/07 · vinicius · 2.041c | **CriAI** (variante NV) |
| `HyTrackWater/umode-criai-rsv` | `umode-criai-rsv` | 21/07 · vinicius · 2.448c | **CriAI** (variante Reserva) |
| `HyTrackWater/ai-mood-creator-19ba6349` | `CriAI\ai-mood-creator-19ba6349` | 01/07 · **joaorisoleo** · 2.257c | **CriAI** — o MANIFEST do João aponta este como o do CriAI |
| `HyTrackWater/proposal-core` | `proposal-core` | 19/07 · vinicius · 56c | não identificado |

⚠ **Cinco clones de CriAI.** Isso provavelmente responde a pergunta aberta sobre "CriAI 2, 3 e 4" que
o Vinicius levantou — mas **não foi verificado**, é leitura de nome de pasta.

### F · Fora do escopo uMode — não inventariar
`nova-mulher-cadastros` (07/08) · `casa-zeeni\casazeeni-financeiro` · `hytrack-water-analysis` ·
`Controle Financeiro` (`vini-lala-s-finances`) · `Imersão uMode\dashboard-vendas-imersao` ·
`Relatórios - Git\03mar26\umode-dashboard-embedded-reports` ·
`Performance Engenharia - Legado\reserva-dashwidgets` · `widgets-nv\nv-dashwidgets` (duplicado,
último commit **11/04/2025**).

---

## ⚠ Divergências de nome já confirmadas — repositório ≠ produto
Quatro casos. **A regra de nunca inferir produto ou cliente por nome de repositório está confirmada
quatro vezes** e está travada em `protocolo-gestao-integracao.md`.

| Nome do repositório | O que é de fato | Como se descobriu |
|---|---|---|
| `arzz-sap` | Reserva + Oficina Reserva (`arzz` = **AZZAS**, não Arezzo) | informado pelo desenvolvedor |
| `unico-linx` | **Puket** | informado pelo desenvolvedor |
| `design-system-hub` | **o BrainHub Console** (não um design system) | leitura do repositório |
| `umode-design-guardian` → remote **`smart-code-hug`** | **AlocAI** | 🆕 **novo em 17/08:** a pasta local diz `umode-design-guardian`, mas o remote é `smart-code-hug`. O `MANIFEST.md` do João registra `umode-design-guardian` = AlocAI — ou o repositório foi renomeado no GitHub, ou são dois. **Não resolvido.** |

## Citados em fonte e ausentes do disco
Nenhum destes está aqui, e todos aparecem no `MANIFEST.md` do João ou na documentação da uFlow:
**`design-system-hub`** (crítico — ver papel C) · `umode-desenvolvai` (DesenvolvAI) ·
`umode-gesthub` / `gest-hub-elevate` (Gest Hub) · `umode-vendeai` (VendeAI) ·
`umode-gest-o-de-opera-o-2f6bdc59` (ONB HUB) · `taxonomia_v1` (Taxonomia) ·
`catalogcraft-ai` (EnriqueceAI) · `fashionpedia` · **`j3-components`** (a gem privada com parte do core
`J3::` da uFlow — bloqueio residual da `D-2026-002`).

---

## O que atualizar, em ordem
1. **Clonar `HyTrackWater/design-system-hub`** — é o frontend do BrainHub e **o único caminho para o
   objetivo da semana**. Sem ele não há inventário de abas, agentes, interações nem regras da
   aplicação. Sugestão de caminho, para não colidir com o vault:
   `C:\Ambientes Virtuais\BrainHub - João Risoléo\design-system-hub`.
2. **`pull` no `umode-os-vault`** — 20 dias defasado; é a régua de comparação de contexto.
3. **Confirmar o repositório do banco e das APIs** — o Vinicius mencionou que existe estrutura criada
   no **MongoDB** da empresa, com database e collections isoladas para o BrainHub. **Esse repositório
   não foi identificado no disco** e é o que define o CRUD.
4. **Resolver `smart-code-hug` × `umode-design-guardian`** — pergunta para o João.
5. Opcional, se entrarem no escopo: `taxonomia_v1`, `catalogcraft-ai`, `j3-components`.

## Princípio a não perder — duas classes de agente
Registrado a pedido de Vinicius em 17 ago 2026, **antes** de inventariar os agentes do Lovable, para
que a distinção não se perca no caminho:

- **Agentes estruturais** — fazem a máquina girar: atualizam documentação, vistoriam padronização,
  identificam `.md` órfãos, cuidam de identificadores e de indexação. **Não conversam com o usuário
  final.**
- **Agentes de interação** — atendem uma pessoa, executam tarefa a pedido, criam demanda no inbox do
  colaborador ou da área.

São coisas distintas e **não podem ser confundidas**. Hipótese de visibilidade a maturar: o CEO vê
todos, com números de resumo; o usuário comum vê só os de interação. **Ainda não é decisão.**

## Fora do escopo desta rodada
Não foi feito nesta sessão, por instrução explícita: inventário de abas e agentes do Lovable (falta o
repositório), desenho do fluxo CRUD, triggers, permissionamento, e qualquer alteração fora do
`brainhub-umode`.

## Fontes e referências
### Documentos consultados
- Varredura somente leitura do disco em 17 ago 2026: 33 repositórios git em
  `C:\Ambientes Virtuais`, sem `fetch` e sem alteração.
- `MANIFEST.md` do vault do João (lido em 04 ago 2026) — origem do crosswalk repositório ↔ produto.
- `_decisoes-convergencia-proposta.md` e `_backlog-convergencia-brainhub.md` — a comparação de
  arquitetura que este inventário complementa.

## Governança
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**.
