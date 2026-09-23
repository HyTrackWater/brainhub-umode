---
aliases:
  - "Oficina Reserva · Institucional"
tags:
  - tipo/institucional
  - cliente/oficina-reserva
  - status/ongoing
---
# Oficina Reserva · Institucional

> **Reescrito em 21 set 2026 a partir do Notion ao vivo.** Campo sem fonte fica `[a preencher]`.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- id: oficina-reserva — [varredura do Notion · 2026-09-21]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: Enterprise — [varredura do Notion · 2026-09-21]
- status: Ongoing — [varredura do Notion · 2026-09-21]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: SAP e Linx — [varredura do Notion · 2026-09-21]
- modulo-contratado: Gestão de Coleção — [varredura do Notion · 2026-09-21]
- modulo-contratado: Integração — [varredura do Notion · 2026-09-21]
- modulo-contratado: Relatórios — [varredura do Notion · 2026-09-21]
- modulo-contratado: Cronograma — [varredura do Notion · 2026-09-21]
- modulo-contratado: Fornecedores — [varredura do Notion · 2026-09-21]
- contrato-situacao: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-21]
- contrato-vigencia: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-21]
- contrato-renovacao: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-21]
- indice-reajuste: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-21]
- usuarios-contratados: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-21]
- usuarios-conta: 7 pessoas com ficha própria no corpus — [varredura do Notion · 2026-09-21]
- atendimento: Fernanda — [ambiguo: mais de um e-mail para este nome]
- tamanho-atendimento: Grupo Enterprise — [varredura do Notion · 2026-09-21]

## Identidade
### ID do cliente
`oficina-reserva`

### Aliases do cliente
`Oficina Reserva` · `Oficina` · domínio `oficinareserva.com`

### Quem são
🔴 **A Oficina Reserva NÃO é marca da Reserva. É marca do Grupo AR&CO.**

A fonte é uma mensagem do **João no grupo de Sales**, registrada na página e datada de
**26/06/2024**:

> *"Call com a Oficina agora, **marca do Grupo AR&CO**, e oficialmente se tornarão clientes nos
> próximos dias. A princípio **não haverá valor adicional, pois entrarão no mesmo pacote do
> Grupo**. Mas vale o registro no CRM e em breve subir a marca para o site.
> **Começarão apenas com uFlow.**"*

> 🔴 **Três fatos comerciais nessa única mensagem, e nenhum deles está em campo estruturado:**
> 1. **A conta pertence a um grupo**, não é independente.
> 2. **Entrou sem receita adicional** — está dentro do pacote do Grupo.
> 3. **A decisão de escopo foi "apenas uFlow"** desde o início.
>
> **Para a leitura da carteira isso muda tudo:** contar Oficina Reserva como cliente separado
> **infla o número de contas e não infla a receita.** `[D]` — **como o negócio quer contar?**

### ⚠ E há uma terceira empresa no meio
A mesma mensagem registra, sobre o cadastro de produto no SAP:

> *"Falta de time de apoio do SAP, **dependência do time da AREZZO**."*

**`Arezzo` está na base `Mapa de Clientes` com status `Pré Onboardings`.**

> **Ou seja: a Oficina Reserva depende operacionalmente do time de SAP da Arezzo, e a Arezzo é
> prospect da uMode.** **Não afirmo a relação societária entre AR&CO e Arezzo** — afirmo o que
> está escrito: **a dependência operacional existe e está registrada.**

### ⚠ Hipótese sobre o grupo de segmentação, não confirmada
A Oficina Reserva está no grupo **`Enterprise`**, cuja descrição na base é literalmente
**"Reserva + Soma"**, junto de **Reserva** e **NV**.

> **`AR&CO` não é `Soma`.** A descrição do grupo cita dois nomes e a conta pertence a um terceiro.
> **Pode ser que o grupo signifique "as contas dos dois grandes grupos" e a Oficina tenha entrado
> pela Reserva.** **Não afirmo. `[a preencher]` — confirmar a relação entre Reserva, Oficina
> Reserva, Simples (by Reserva), AR&CO, Arezzo e Soma.**

### O que fazem
`[a preencher]` — mas há **dimensão de coleção declarada**:

> **400 SKUs por coleção, 100 contínuos.**

**E um plano registrado:** *"Planejamento de lançamento de **marca feminina** com início no uMode."*

> 🟢 **É a única conta varrida com lançamento de marca previsto para nascer dentro da
> plataforma.** `[a preencher]` — **aconteceu?**

### Para quem fazem
`[a preencher]`

## Posicionamento
### Segmento
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 12 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.****, assim como `Cidade`, `Estado`,
`CNPJ`, `Razão Social`, `Área de Atuação` e `Receita Anual`.

> ⚠ **É a conta com mais campos vazios da base entre os Ongoing** — coerente com ter entrado
> *"no mesmo pacote do Grupo"*, sem ciclo comercial próprio.

### Receita anual
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 2 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
>
> ⚠ **A mensagem de Sales diz "não haverá valor adicional"** — 🔴 **isso é sobre cobrança da uMode, não sobre a receita do cliente.** São coisas diferentes e não devem ser lidas uma pela outra.

### Grupo de segmentação uMode
**`Enterprise`** — Grupo 1, descrição *"Reserva + Soma"*. `WIP Estratégico 6,00`.

## Operação uMode
### Status atual
**`Ongoing`** — lido na base em 21/09/2026.

### Data de ativação
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 6 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**

> **Mas a jornada comercial está datada com precisão incomum:**
> **26/06/2024** call de Sales · **01/07/2024** kick-off interno · **12/07/2024** kick-off cliente.
> Linha criada no Notion em **27/06/2024**, **um dia depois da call.**

### Módulos contratados
`Gestão de Coleção` · `Integração` · `Relatórios` · `Cronograma` · `Fornecedores` — **5 de 7**.

> ⚠ **A mensagem de Sales dizia *"começarão apenas com uFlow"*, e hoje há 5 módulos.**
> **O escopo cresceu.** `[a preencher]` — **quando e como?**
>
> 🟢 **`Fornecedores` está contratado** — e a relação com fornecedor era **a dor número 1.3**.
> **Coerente.**

### Usuários da conta
**7 pessoas com ficha própria** no corpus.

> 🔴 **Isto é contagem de PESSOA DOCUMENTADA, não de licença contratada** — o número contratado está em `## Contrato › Usuários contratados`. **Os dois divergem por natureza** e não devem ser somados nem comparados sem olhar a fonte de cada um.

> Índice: [`_pessoas/_indice.md`](../_pessoas/_indice.md)
### ERP / Integração
**`SAP e Linx`** — dois ERPs.

> ⚠ **A Reserva tem o mesmo par gravado como `Linx / SAP`.** **Mesmo par, grafia diferente,
> duas linhas da mesma base.** **Erro de taxonomia na origem** — preservado e sinalizado.

**E o SAP é o centro da dor:**
> *"Processo de cadastro de produto realizado **inteiramente no SAP**. Sistema pouco intuitivo e
> com muitas etapas entre SAP e Linx."* · *"**90% do tempo dedicado ao SAP**"* (pedido de compra).

### Responsável de atendimento (uMode)
**Fernanda** — campo `Atendimento 2025` da base `Mapa de Clientes`, lido ao vivo em 23 set 2026.
## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

> 🔴 **Ausência VERIFICADA em 23/09/2026: `Oficina Reserva` NÃO consta na base de contratos do Financeiro.** Os **41 registros** foram conferidos um a um.
> ⚠ **A base tem `Reserva`** — que o corpus trata como **cliente distinto**, com pasta própria e serviços próprios (`uFlow` · `uBuy` · `uPlan`). 🔴 **Não afirmo que sejam a mesma conta nem que sejam contas diferentes** — é exatamente o tipo de confusão que já aconteceu com `STZ` × `Studio Z`. **Quem confirma é o Financeiro.**
> ⚠ **Enquanto não se confirma, todo campo de contrato desta conta fica sem valor** — e a ausência está declarada, não esquecida.

### Situação do contrato

`[a preencher]` — **não consta na base de contratos do Financeiro** (41 registros, conferidos em 23/09/2026).

### Vigência

`[a preencher]` — **não consta na base de contratos do Financeiro** (41 registros, conferidos em 23/09/2026).

### Renovação e aviso prévio

`[a preencher]` — **não consta na base de contratos do Financeiro** (41 registros, conferidos em 23/09/2026).

### Índice de reajuste

`[a preencher]` — **não consta na base de contratos do Financeiro** (41 registros, conferidos em 23/09/2026).

### Usuários contratados

`[a preencher]` — **não consta na base de contratos do Financeiro** (41 registros, conferidos em 23/09/2026).

### Pendências contratuais registradas

`[a preencher]`

## Aliases de áreas
### Mapeamento alias → canônico

> ⚠ **Esta conta não tem lista de times, nem tabela de PLM varrida, nem pesquisa.**
> O que existe são **funções citadas dentro das dores**. **Fonte fraca, e declarada como tal.**

| Função citada na dor | → Área canônica | Evidência |
|---|---|---|
| **Cadastro de produto** | `08_Ecommerce-Cadastro` | *"há apenas uma pessoa dedicada ao cadastro"* |
| **Pedido de compra** | `06_Compras-Supply-Sourcing` | *"90% do tempo dedicado ao SAP"* |
| **Relação com fornecedor** | `06_Compras-Supply-Sourcing` | dor 1.3 · módulo `Fornecedores` contratado |
| **Lacre e mostruário** | `05_PCP` | *"status de lacre, desenvolvimento de MP e mostruário"* |
| **Auditoria de qualidade** | `04_Qualidade` | **feita pela Qualitá, empresa externa** |
| **Gestão de time / performance** | **transversal** | *"performance do time, análise do micro ao macro"* |

> **As outras oito áreas canônicas não são mencionadas em nenhuma fonte varrida.**


### 🟢 Perfis de acesso reais — fonte forte, lida em 17/03/2026

> 🔴 **Esta tabela PREVALECE sobre a de funções-citadas-em-dores acima**, que a própria
> se declara *"fonte fraca"*. **Aquela fica como histórico do que se sabia antes.**
> **Fonte:** Notion — `Perfil de Usuário e Permissionamentos OFICINA`.

| Perfil no PLM | → Área canônica |
|---|---|
| `Oficina - Master` | **transversal** — único com `Usuários da Conta` e `Editar Usuário` |
| `Oficina - Planner` | **transversal** — privilegiado, **não confundir com `Oficina - Planejamento`** |
| `Oficina - Estilo` | `02_Estilo-Criacao` |
| `Oficina - Planejamento` | `01_Planejamento` |
| `Oficina - Compras` | `06_Compras-Supply-Sourcing` — 🔴 **marcado para ser extinto** |
| `Oficina - Atacado` | `09_Comercial-Vendas` — o mais restrito dos oito |
| `Oficina - Qualitá` | `04_Qualidade` — 🔴 **perfil de EMPRESA EXTERNA** |
| `Oficina - Ecommerce Marketing` | 🔴 **`08_Ecommerce-Cadastro` E `10_Marketing`** — um perfil, duas áreas |

🔴 **Sete das 14 áreas canônicas não têm perfil:** PCP, Logística, Financeiro, Design,
Modelagem, Engenharia e Desenvolvimento de Coleção. ⚠ **Mas Engenharia existe como bloco da
ficha de produto** — **perfil e área não são a mesma coisa nesta conta.**

## Sistemas e fontes de verdade
### Drive de operação
⚠ **Não há pasta registrada na base** — campo ausente, diferente de todos os outros Ongoing.

### Outras fontes
| Fonte | Ferramenta | Estado |
|---|---|---|
| **Perfil de Usuário e Permissionamentos OFICINA** | Notion | 🔴 **não varrida** |
| Kick Off Interno — 01/07/24 | Notion | **não varrido** |
| Oficina Reserva \| Kick Off Cliente — 12/07/24 | Notion | **não varrido** |
| Reuniões com clientes · Demandas Oficina | Notion (2 bases) | **não varridas** |
| Duas páginas mencionadas sem título visível | Notion | **não varridas** |
| **SAP** | sistema do cliente | 🔴 **centro da dor, não capturado** |
| **Qualitá** | **empresa externa de auditoria** | 🔴 **não está no inventário** |
| **WhatsApp** (com a Qualitá) | WhatsApp | **não capturado** |
| **Google Drive** (gerenciamento de arquivos) | Google Drive | **não capturado** |
| **Corel** (documentos com fornecedor) | Corel | **não capturado** |
| `Chamados & Atendimentos` | Notion | ✅ **varrida — 7 chamados, 3 pessoas** |

> 🔴 **A `Qualitá` é uma empresa externa de auditoria de qualidade que opera no processo do
> cliente**, e **não está em nenhum inventário da uMode.** É um **terceiro ator** no fluxo,
> junto de fornecedores — como os quatro fornecedores que operam dentro da conta da Reserva.

## Contexto crítico
### Onde estamos
Conta que entrou pelo grupo em jul/2024, com **kick-off em duas semanas**.
**7 chamados em jan/2026, 3 abertos.**

### 🔴 A frente aberta
A mensagem de Sales define sucesso com prazo:

> *"Objetivo de estar **'rodando' no uMode em 6 meses**, resolvendo os itens 1 e 2 das dores.
> Interesse em um **MVP** para implementação rápida."*

**Seis meses a partir de 26/06/2024 é dezembro de 2024.** Hoje é **setembro de 2026** —
**mais de um ano e meio depois do prazo.**

> ⚠ **Não afirmo que o objetivo não foi atingido.** Afirmo que **nenhuma fonte varrida registra
> se foi.** `[a preencher]` — **e essa é a pergunta mais importante desta conta.**

**Os "próximos passos" registrados para o Holmer também não têm desfecho:**
definição da integração e dos reports · planejamento das ações ·
**"definição de celebração ao atingir o sucesso"** · planejamento do início do projeto.

> 🟢 **"Definição de celebração ao atingir o sucesso" é uma prática que só aparece nesta
> conta.** Vale para o brain da Casa: **é método, e está num só lugar.**

### O que o cliente espera
**Resolver as dores 1 e 2 — cadastro de produto e centralização de gestão — em 6 meses, via MVP.**

### As dores estruturais registradas
**Seis blocos, transcritos da mensagem de Sales de 26/06/2024:**

**1.1 · Cadastro de produto inteiramente no SAP**
*"Sistema pouco intuitivo e com muitas etapas entre SAP e Linx."* ·
*"Falta de time de apoio do SAP, **dependência do time da AREZZO**."* ·
*"Necessidade de ajustes em cor, grade, **NCM**, etc."* ·
*"**Há apenas uma pessoa dedicada ao cadastro**, mas gostaria de ter um papel mais tático."* ·
*"Informações desafiadoras de serem encontradas."*

> ⚠ **NCM aparece também como página dedicada na Lofty Style.** **Dois clientes com dor fiscal.**

**1.2 · Interação com a Qualitá — auditoria externa**
*"Processo todo feito pelo **WhatsApp**."* ·
*"Envio de FTs causa atrasos, pois **o inspetor chega para auditar e não tem o documento**."* ·
*"Gerenciamento de arquivos no Google Drive."* ·
*"**Má reputação entre as Fornecedores e Qualitá por não usarem uMode.**"*

> 🔴 **A última frase é notável: há custo reputacional em NÃO usar a plataforma**, percebido
> por terceiros no ecossistema. **É o argumento comercial mais forte que apareceu em toda a
> varredura, e está enterrado numa mensagem de grupo de 2024.**

**1.3 · Relação com o fornecedor**
*"Fornecedores justificam que **não realizaram tarefas por não receberem a demanda**."* ·
*"Muitos documentos separados para resolver a relação (e-mail, planilha, **Corel**, vídeos)."* ·
*"Percepção negativa por **ser a única marca diferente das demais**."*

**2 · Falta de centralização de gestão**
*"Ausência de governança devido a muitos controles paralelos, causando reuniões desnecessárias."* ·
*"**Criação de muitos rituais para suprir a falta de governança.**"*

> 🟢 **"Criação de muitos rituais para suprir a falta de governança" é a melhor formulação
> do problema que o BrainHub existe para resolver, encontrada em qualquer fonte.**
> **E foi dita pelo cliente, não pela uMode.**

**3 · Calendário** — status de lacre, desenvolvimento de MP e mostruário.
**4 · Gestão de time** — performance do time, *"análise do micro ao macro"*.

> ⚠ **Controles paralelos** aparecem também na **Cambos** (Trello) e na **NK** (planilhas).
> **Três clientes com a mesma dor estrutural.**

### Tamanho de atendimento
Grupo **`Enterprise`** · `WIP 6,00` · **Fernanda**, com 3 contas.

## Governança
### Responsável de atendimento (uMode)
Fernanda (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Grupo AR&CO, pacote sem valor adicional, escopo inicial, dores, sucesso, próximos passos | Notion — **mensagem do João no grupo de Sales**, na página | **26/06/2024** · varrida 21/09/2026 |
| Datas de kick-off | Notion — títulos das seções da página | **varrido 21/09/2026** |
| 7 chamados e 3 pessoas | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Status, módulos, ERP, segmentação | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Oficina Reserva`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)

**Integração deste cliente:** [integracao.md](integracao.md)

**Registros:** **28 demandas** — [índice](../_demandas/_indice.md) · **2 RFIs** — [índice](../_rfis/_indice.md) · **7 fichas de pessoa** — [índice](../_pessoas/_indice.md)

**As 14 áreas deste cliente:**

- [Planejamento](../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../02_Estilo-Criacao/_contexto/contexto-area.md)
- [Desenvolvimento de Colecao](../../03_Desenvolvimento-de-Colecao/_contexto/contexto-area.md)
- [Qualidade](../../04_Qualidade/_contexto/contexto-area.md)
- [PCP](../../05_PCP/_contexto/contexto-area.md)
- [Compras Supply Sourcing](../../06_Compras-Supply-Sourcing/_contexto/contexto-area.md)
- [Logistica CD](../../07_Logistica-CD/_contexto/contexto-area.md)
- [Ecommerce Cadastro](../../08_Ecommerce-Cadastro/_contexto/contexto-area.md)
- [Comercial Vendas](../../09_Comercial-Vendas/_contexto/contexto-area.md)
- [Marketing](../../10_Marketing/_contexto/contexto-area.md)
- [Financeiro](../../11_Financeiro/_contexto/contexto-area.md)
- [Design](../../12_Design/_contexto/contexto-area.md)
- [Modelagem](../../13_Modelagem/_contexto/contexto-area.md)
- [Engenharia](../../14_Engenharia/_contexto/contexto-area.md)

**Autoridades da Casa que governam este arquivo:**
[`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md) · [`_espec-pessoas-e-comunicacoes.md`](../../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) · [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
