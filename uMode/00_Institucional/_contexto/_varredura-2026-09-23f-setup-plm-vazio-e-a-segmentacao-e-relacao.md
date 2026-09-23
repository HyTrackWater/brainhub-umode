---
aliases:
  - "Varredura 23 set 2026 — o acervo `Setup - PLM` é quase vazio, e a segmentação era uma relação"
---
# Varredura 23 set 2026 — o acervo `Setup - PLM` é quase vazio, e a segmentação era uma relação

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
>
> **Acesso:** primeira varredura depois de reconectar o conector de Notion ao workspace
> `uMode Mode's Notion`. Antes disso o token apontava para o workspace pessoal — ver
> `_pendencias-gerais.md`, item 498.
>
> **Tratamento:** `T2`. Nenhum valor comercial, CPF, telefone ou credencial foi copiado.

## 0 · Declaração de completude — o que este registro NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não abri os 18 documentos da RESERVA** | mapeei a base `CENTRAL DE DOCUMENTAÇÕES`; li os títulos, categorias e datas, **não o conteúdo** |
| 2 | **Não abri as 4 páginas de conteúdo do acervo** | `[NK Store] Macroplan Calçados`, `[Permissionamento] Vix - Ficha Tecnica`, `[Card 20994] Vix - CAD`, `Studioz - Fornecedores` |
| 3 | **Não resolvi a camada de pessoa da CAEDU** | os e-mails nominais (`@caedu.com.br`) aparecem em sub-página da conta, **não abri** |
| 4 | **Não sei quem são os 16 clientes sem grupo** | o campo está vazio na base, não é falha de leitura |
| 5 | **`Atendimento 2024` é relação e não foi resolvido** | mesma armadilha da segmentação; resolvi só a segmentação |

## 1 · 🔴 O acervo `Setup - PLM / CLIENTES` foi superestimado no nosso plano `[C]`

O `AGORA.md` listava este acervo como **passo imediato e "fonte de maior rendimento"**.
**Abri os 9 e medi.**

| Cliente | O que tem | Última edição |
|---|---|---|
| **RESERVA** | 🟢 base **`CENTRAL DE DOCUMENTAÇÕES`** com **18 documentos** categorizados | 04/07/2025 |
| **VIX** | 🟡 2 páginas — `[Permissionamento] Vix - Ficha Tecnica` · `[Card - 20994] Mudanças no perfil Vix - CAD` | 06/07/2025 |
| **NK Store** | 🟡 1 página — `[NK Store] - Macroplan Calçados` | 16/07/2025 |
| **StudioZ** | 🟡 1 página — `Studioz - Fornecedores` | 30/01/2025 |
| **CAEDU** | 🔴 **VAZIA** | 30/01/2025 |
| **BAW** | 🔴 **VAZIA** | 30/01/2025 |
| **OFICINA** | 🔴 **VAZIA** | 30/01/2025 |
| **PUKET** | 🔴 **VAZIA** | 30/01/2025 |
| NV | lida em sessão anterior | — |

🔴 **Quatro das oito estão vazias, e uma delas é a CAEDU** — o cliente com prazo declarado.
**Este caminho não contribui nada para a CAEDU.** O título do acervo diz
`(Em desenvolvimento)` e o pai não é editado desde **16/07/2025**.

🟢 **O que salva o acervo é a RESERVA:** 18 documentos com `Categoria` (`Operacional`,
`Integração`, `Regras de Negócio`), autor e data. Entre eles **`Regras de Integração`**,
**`Workflow / Regras`**, **`Permissões`**, **`Relatórios e Views`**, **`Ações e Configs`**,
`✍🏻 Trava de Ficha`, `✍🏻 Alteração de Status`, `Relatório de Custos e MO`,
`Macro desenvolvimento de Produto`, `Gestão de Estampas`. **É o acervo de regra de negócio
por cliente mais estruturado que apareceu até aqui** — e existe **só para a RESERVA**.

## 2 · 🔺 A segmentação já tinha sido varrida — o que faltava era resolver a relação `[C]`

**`Segmentação Grupos` está na § 4 do diário de todos os 48 clientes como fonte NÃO varrida.
Está errado: ela já tinha sido varrida.** 34 clientes já traziam o grupo preenchido no
`institucional.md`, com `WIP Estratégico` e tudo.

**Mas cinco estavam errados ou vazios, e todos pela mesma causa técnica.** O `institucional.md`
da CAEDU registrava textualmente: *"o campo mudou de tipo na base viva (virou relação) e não
trouxe valor na consulta"*. **É isso: o campo é `relation`.** Consultado como valor, volta vazio.
**Resolvendo a relação, os cinco fecham.**

**A base `Segmentação Grupos` (`collection://a4103fe2-…`) tem 5 linhas:**

| Linha | Grupo | Descrição | `WIP Time` | `WIP Estratégico` |
|---|:-:|---|--:|--:|
| **Enterprise** | **1** | *"Reserva + Soma"* | 10 | **6** |
| **Médios** | **2** | — | 10 | **2,25** |
| **SMB** | **3** | — | 10 | **1,75** |
| Grupos 4: Outros Clientes | — | — | — | — |
| Churn | — | — | — | — |

🟢 **Isso fecha a pergunta transversal nº 1 da fila.** Os rótulos que eu tinha visto soltos na
`Documentação CX` (`[SaaS]`, `[CX] Enterprise`, `SMB`) são **Enterprise · Médios · SMB**, mais
duas linhas de controle. **O vocabulário do corpus já estava certo** — faltavam o conjunto
fechado e o número do grupo.

🆕 **`WIP Estratégico` é descoberta lateral e vale mais que o rótulo.** A base vive sob
`Operação de Clientes / Arquivo / **Alocação de Cargas por Clientes em Vigor**`: é um **modelo de
capacidade** — quantas contas daquele porte um time de 10 sustenta. **Enterprise pesa 3,4× um SMB.**

### 2.1 · As cinco correções aplicadas `[C]`

| Cliente | Estava | Passou a ser |
|---|---|---|
| 🔴 **CAEDU** | `[a preencher]` — *"provável resíduo"* | **`SMB` · Grupo 3** |
| **Arezzo** | `[a preencher]` — sem grupo | **`Enterprise` · Grupo 1** |
| **Hering** | `[a preencher]` — sem grupo | **`Enterprise` · Grupo 1** |
| **Baw** | `[a preencher]` — sem grupo | **`SMB` · Grupo 3** |
| **Lojão do Brás** | `Churn` | **`Grupos 4: Outros Clientes`** |

🔴 **A correção da CAEDU derruba uma hipótese nossa e abre um problema de negócio.**
O corpus supunha que *"Grupo 3"* fosse resíduo de export antigo, *"classificação incompatível com
um cliente em `Ongoing`"*. **Não é resíduo: é o valor vivo.** E a fonte do próprio Notion descreve
a CAEDU como *varejista de moda popular, 100+ lojas, ~R$1bi de faturamento (2023)*.
**Uma conta desse porte classificada na faixa de menor alocação de time (`1,75` contra `6`),
em `Onboarding`, com o projeto CAEDU 2.0 em montagem.**

## 3 · 🆕 `Atendimento 2025` não é só pessoa — é pessoa OU `SMB` `[C]`

| Valor | Clientes |
|---|---|
| **Julianne + Pedro** | Caedu · Lenny Niemeyer · Loungerie · NK STORE · Osklen · Puket · VIX |
| **Laura** | Baw · Cambos · Highstil · Lofty Style · Luiza Barcelos · Moda Objetiva · Plie |
| **Fernanda** | NV · Oficina Reserva · Reserva |
| 🔴 **`SMB`** | 4takes · Camys · Cavallari · Mondepars · Studio Minah · TDC · Ton Age |

🔴 **`SMB` no campo de ATENDIMENTO é ausência de pessoa designada — é o modo self-service.**
**Todos os 7 estão em `Sem CS` ou `Churn`.** Isso confirma, por fonte independente, a leitura já
registrada de que `Sem CS` é um SKU self-service e não um momento da jornada.

⚠ **Uma divergência:** a **Baw** é `SMB` na segmentação e `Sem CS` no status, **mas tem a Laura
no atendimento**. Os três campos discordam.

## 4 · 🔴 O achado de processo: o diário produz falso-negativo

**A § 4 do `_pendencias-e-fontes.md` — *"fontes conhecidas e AINDA NÃO varridas"* — não é podada
quando a fonte é varrida.** `Segmentação Grupos` continuava listada lá nos 48 arquivos **depois de
já ter alimentado 34 `institucional.md`**.

🔴 **O diário existe para impedir retrabalho e, nesta seção, ele causa retrabalho.** Eu fui até a
base porque o diário disse que ela não tinha sido varrida. **A § 3 (já varridas) está correta; a
§ 4 é que não se atualiza.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`. Correção vira registro novo.
