# Protocolo — varredura e preenchimento de contexto de cliente

> Escrito em **21 set 2026**, depois de fechar a **CAEDU** como caso de prova: 33 → 47 MDs,
> `contexto-area.md` de **0/14 para 14/14**, e os três MDs canônicos reescritos a partir do
> **Notion ao vivo**.
>
> Este protocolo existe para que os outros 21 clientes vivos não exijam redescobrir o caminho.
> **Ordem importa** — ela foi determinada por onde a informação de fato está.

## 0 · Antes de começar: a regra que evita o retrabalho

🔴 **Não use export.** O vault tem exports de Notion versionados em Git, e eles **estavam seis meses
desatualizados**. Na CAEDU isso significava: status errado, taxonomia de módulo errada, e quatro
clientes listados como vivos que já estavam em churn.

**Vá à base viva pelo MCP do Notion. Sempre.** O export serve para conferir histórico, nunca para
afirmar estado.

## 1 · A ordem de varredura

| # | Fonte | O que ela dá | Como chegar |
|---|---|---|---|
| 1 | **Base `Mapa de Clientes`** | status, módulos, ERP, dupla de atendimento, setor, cidade | `notion-query-data-sources` em `collection://ec041afd-fcee-44f8-83cb-223fca6f4108` |
| 2 | **Página do cliente** dentro da base | 🎯 **a tabela de usuários do PLM** — nome, e-mail, perfil, data | `notion-fetch` na `url` da linha do cliente |
| 3 | **`Mapeamento de Contas - <cliente>`** | AS IS, dores, fluxo por área, plano de ação | busca em `Operação de Clientes / Área de CX / Documentação CX` |
| 4 | **Sub-páginas da página do cliente** | Fornecedores, Playbooks, Manual, Onboarding→Ongoing | listadas no `<content>` da página |
| 5 | **Atas** em `Reuniões com o cliente` | marcos datados, pessoas nomeadas, decisões | idem |
| 6 | **vault `_Clientes/<slug>/`** | propostas, contratos, cronogramas, atas destiladas | `git show` na branch `governance/brainhub-v1.5` |
| 7 | **Repositório de integração** | confirma o ERP de verdade | `C:\Ambientes Virtuais\uMode-Integracoes\` |

## 2 · 🎯 O achado que destrava tudo

> **O perfil de acesso no PLM é o único vínculo pessoa↔área que existe em alguma fonte da uMode.**

Na CAEDU, 93 usuários em 14 perfis mapearam assim:

| Perfil | → Área canônica |
|---|---|
| `<Cliente>-Estilo` | `02_Estilo-Criacao` |
| `<Cliente>-Produto` | `03_Desenvolvimento-de-Colecao` |
| `<Cliente>-Planejamento` | `01_Planejamento` |
| `<Cliente>-Modelagem` | `13_Modelagem` |
| `<Cliente>-Qualidade` | `04_Qualidade` |
| `<Cliente>-E-commerce` | `08_Ecommerce-Cadastro` |
| `<Cliente>-Geral` · `-Gerentes` · `-Admin` | **transversal — não derivável** |
| `Fornecedor` | externo · `06_Compras-Supply-Sourcing` |
| `Dono da Conta` | conta de serviço, **não é pessoa** |

**Isso preenche de uma vez:** a seção *Aliases de áreas* do `institucional.md`, a seção *Time do
projeto por área* do `pessoas.md`, e a seção *Pessoas desta área* de cada `contexto-area.md`.

## 3 · As sete travas que a CAEDU revelou

**1 · Extrair por script, nunca transcrever.** 93 linhas de tabela transcritas à mão erram. Use
regex sobre o resultado salvo do `notion-fetch` e gere o markdown por script.

**2 · A página do cliente pode estourar o limite de resposta.** A da CAEDU tem 52 KB, e boa parte é
um ícone em base64. O resultado é salvo em arquivo — leia por fatia, e **pule direto ao `<content>`**.

**3 · PowerShell 5.1 lê `.ps1` sem BOM como ANSI** e destrói todo acento. Ao gerar script com
acentuação, **grave com UTF-8 BOM** ou ele quebra no parser.

**4 · Erros de digitação vêm da origem.** Na CAEDU: `Caedu- Planejamento` com espaço a mais,
`Caedu-Admim` por *Admin*, datas como `08/11/0202`. **Preserve e sinalize — corrigir é na fonte.**

**5 · A ausência de perfil é achado, não falha.** Sete das 14 áreas da CAEDU não têm perfil no PLM.
Isso **é** a informação: ou a área não existe no cliente, ou existe e não usa a plataforma.

**6 · Arquivo de área vazio ainda deve ser criado.** Com estrutura, com a lista de fontes varridas e
o que cada uma **não** trouxe, e com as perguntas a levar ao negócio.
> **A contagem de lacunas sobe, e isso é correto.** Na CAEDU foi de 691 para 743 — porque 56 lacunas
> que antes eram invisíveis passaram a ser endereçáveis. **Lacuna visível vale mais que cobertura
> aparente.**

**7 · Datar tudo e marcar o que não foi confirmado.** O mapeamento de conta da CAEDU tem 17 meses e
já contém correções posteriores no próprio texto. O porte e o CEO vieram de um CRM de mentoria e
**não** do atendimento — ficaram marcados como não confirmados.

## 4 · O que produzir, por cliente

| Arquivo | Fonte principal |
|---|---|
| `00_Institucional/_contexto/institucional.md` | base `Mapa de Clientes` + perfis do PLM (aliases de área) |
| `00_Institucional/_contexto/pessoas.md` | tabela de usuários do PLM + atas (liderança) |
| `00_Institucional/_contexto/jornada.md` | atas datadas + mapeamento + vault |
| `<NN_Area>/_contexto/contexto-area.md` × 14 | mapeamento de conta + perfis + sub-páginas |

**Em todo arquivo:** tabela de **Procedência** no fim, com bloco, fonte e data.

## 5 · Ordem de ataque dos 21 restantes

Priorizar por **status e volume de material**, não por ordem alfabética:

1. **Ongoing com mapeamento de conta** — Puket (tem análise comparativa com a Caedu), Reserva, NV,
   Cambos, Osklen
2. **Ongoing restantes** — Lofty Style, Luiza Barcelos, NK STORE, Oficina Reserva, VIX
3. **Operação Assistida** — Moda Objetiva, Osklen
4. **Onboarding** — Loungerie ⚠ **não existe no corpus, precisa ser criado**
5. **Pré Onboardings** — Arezzo, Hering
6. **Sem CS** — Baw, Camys, Cavallari, Mondepars, Studio Minah, TDC, Ton Age
   > Estes provavelmente só têm `Gestão de Coleção` e pouca ata. **Esperar pouco material** — e
   > registrar isso como fato do cliente.

## Governança
Somente o CEO altera conteúdo no BrainHub. **Alterar este protocolo exige ter executado a varredura
de pelo menos um cliente com o método novo** — protocolo não se corrige por opinião.
