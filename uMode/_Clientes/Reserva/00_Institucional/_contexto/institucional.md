---
aliases:
  - "Reserva · Institucional"
tags:
  - tipo/institucional
  - cliente/reserva
  - status/ongoing
---
# Reserva · Institucional

> **Reescrito em 21 set 2026 a partir do Notion ao vivo** — base `Mapa de Clientes`, página do
> cliente, base `Segmentação Grupos` e base `Chamados & Atendimentos`.
> Campo sem fonte fica `[a preencher]` — nada foi inferido.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- id: reserva — [base Segmentação Grupos · 2026-09-21]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: Enterprise — [base Segmentação Grupos · 2026-09-21]
- status: Ongoing — [base Segmentação Grupos · 2026-09-21]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: Linx / SAP — [base Segmentação Grupos · 2026-09-21]
- modulo-contratado: Gestão de Coleção — [base Segmentação Grupos · 2026-09-21]
- modulo-contratado: Integração — [base Segmentação Grupos · 2026-09-21]
- modulo-contratado: Relatórios — [base Segmentação Grupos · 2026-09-21]
- modulo-contratado: Cronograma — [base Segmentação Grupos · 2026-09-21]
- modulo-contratado: Aposta — [base Segmentação Grupos · 2026-09-21]
- contrato-situacao: Assinar renovação — [planilha de contratos do Financeiro · 2026-09-21]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-21]
- servico-faturado: uBuy — [planilha de contratos do Financeiro · 2026-09-21]
- servico-faturado: uPlan — [planilha de contratos do Financeiro · 2026-09-21]
- contrato-vigencia: 2020-07-20 → 2021-01-20 · vigência 6 meses — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: ? — [sem fonte]
- indice-reajuste: IGPM — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: ? — [sem fonte]
- usuarios-conta: 13 pessoas com ficha própria no corpus — [base Segmentação Grupos · 2026-09-21]
- atendimento: Fernanda — [ambiguo: mais de um e-mail para este nome]
- tamanho-atendimento: Grupo Enterprise · WIP Estratégico 6,00 · Fernanda, que atende as 3 contas — [base Segmentação Grupos · 2026-09-21]

## Identidade
### ID do cliente
`reserva`

### Aliases do cliente
`Reserva` · `RSV` (usado nos nomes de grupo de WhatsApp da própria operação) ·
domínio `usereserva.com`

> ⚠ **Reserva não é uma conta só.** No corpus existem também `Oficina Reserva` e
> `Simples (by Reserva)`, ambas com casa própria. O grupo de segmentação da uMode se chama
> **`Enterprise`** e tem a descrição literal **"Reserva + Soma"**. **Confirmar a relação
> societária entre as três contas e o grupo Soma** — nenhuma fonte varrida a declara.

### Quem são
`[a preencher]` — os campos `Razão Social`, `Setor da Empresa`, `Área de Atuação`, `Cidade`,
`Estado`, `CNPJ` e `Receita Anual` estão **todos vazios na base**.

### O que fazem
`[a preencher]`

### Para quem fazem
`[a preencher]`

## Posicionamento
### Segmento
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 12 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**

### Receita anual
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 2 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**

### Grupo de segmentação uMode
**`Enterprise`** — Grupo 1, descrição **"Reserva + Soma"**.
`WIP Time 10` · **`WIP Estratégico 6,00`** — **a maior alocação da carteira**.

| Grupo | Nome | WIP Estratégico | Clientes vivos |
|---|---|---:|---|
| 1 | **Enterprise** | **6,00** | **Reserva** · Oficina Reserva · NV |
| 2 | Médios | 2,25 | Cambos · Lofty Style · Luiza Barcelos · NK STORE · VIX · Osklen · Moda Objetiva · Loungerie |
| 3 | SMB | 1,75 | Caedu · Puket |

> ⚠ A base `Segmentação Grupos` está sob a pasta **`Arquivo`** no Notion. **Confirmar vigência.**

## Operação uMode
### Status atual
**`Ongoing`** — lido na base em 21/09/2026.

### Data de ativação
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 6 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.****.

> **Piso verificável:** a linha do cliente no Notion foi criada em **24/05/2023**, e há um
> documento *Solicitações Raquel* datado de **21/06/2023**. A conta opera **desde meados de 2023,
> no mínimo**.

### Módulos contratados
**`Gestão de Coleção`** · **`Integração`** · **`Relatórios`** · **`Cronograma`** · **`Aposta`** ·
**`Planejamento`** · **`Fornecedores`**

> 🔴 **Sete de sete. É a única conta da carteira com a taxonomia completa de módulos.**
> Para comparação: Oficina Reserva e Osklen têm 5, a maioria tem 4, a Puket tem 2.

### Usuários da conta
**13 pessoas com ficha própria** no corpus.

> 🔴 **Isto é contagem de PESSOA DOCUMENTADA, não de licença contratada** — o número contratado está em `## Contrato › Usuários contratados`. **Os dois divergem por natureza** e não devem ser somados nem comparados sem olhar a fonte de cada um.

> Índice: [`_pessoas/_indice.md`](../_pessoas/_indice.md)
### ERP / Integração
**`Linx / SAP`** — dois ERPs. Há um grupo de WhatsApp chamado
*"PROBLEMAS DIÁRIOS PA"* cujos participantes declarados são **SAP, Linx, Cadastro RSV e Cadastro
Oficina** — **a convivência dos dois ERPs tem canal próprio e diário.**

### Responsável de atendimento (uMode)
**Fernanda** — campo `Atendimento 2025` da base `Mapa de Clientes`, lido ao vivo em 23 set 2026.
## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinar renovação** — serviços faturados: `uFlow` · `uBuy` · `uPlan`.
> 🔴 **A razão social da Reserva na base de contratos é `AREZZO INDUSTRIA E COMERCIO S.A.`**
> — **juridicamente, a Reserva é a Arezzo.** Isso toca a questão de **grupo econômico** já aberta
> (Reserva · Oficina Reserva · Simples · Arezzo como quatro casas para o que pode ser um contrato só).
### Vigência
**2020-07-20 → 2021-01-20** · vigência 6 meses
### Renovação e aviso prévio
Renovação **Via assinatura** · aviso prévio `[a preencher]`
### Índice de reajuste
IGPM
### Usuários contratados
`[a preencher]` — ⚠ **a própria planilha marca como A CONFIRMAR.**
### Pendências contratuais registradas
🔴 **CONTRATO DESATUALIZADO**

> Texto literal do campo `OBS` da planilha de contratos. **Não interpretei.**
## Aliases de áreas
### Mapeamento alias → canônico

> 🔴 **Aqui a fonte é outra.** Sem tabela de PLM, o único vínculo pessoa↔área que existe na
> conta está nos **nomes dos grupos de WhatsApp** e nos títulos de documento da própria página.
>
> **É fonte fraca e está declarada como tal** — mas é a que existe.

| Alias na operação | Onde aparece | → Área canônica |
|---|---|---|
| `Estilo` | grupo *"Comitê uMode <> Reserva"*, *"uMode - Importante"* (Adriana) | `02_Estilo-Criacao` |
| `Cadastro` | grupos *"Migração PA"*, *"PROBLEMAS DIÁRIOS PA"* (Raquel) | `08_Ecommerce-Cadastro` |
| `Compras` | grupos *"Comitê Compras | RSV + uMode"*, *"Compras e Umode"* (Claudinha) | `06_Compras-Supply-Sourcing` |
| `Sourcing` | grupo *"RSV & uMode | Sourcing"* (Bruno) · *Termo de abertura de Projeto - Sourcing* | `06_Compras-Supply-Sourcing` |
| `Eng` / `Engenharia` | grupo *"Comitê uMode <> Reserva"*, *"uMode - Importante"* (Raquel) | `14_Engenharia` |
| `Merchan` | grupo *"Comitê uMode <> Reserva"* · documento *Demandas Merchan* | ⚠ `[a preencher]` — ver abaixo |
| `Produto` | documento *Demandas de Produto* | `03_Desenvolvimento-de-Colecao` |

### ⚠ `Merchan` exige decisão, não palpite
*Merchandising* em moda costuma ficar entre planejamento e comercial, e a grade canônica tem
`01_Planejamento` e `09_Comercial-Vendas` como candidatos. **Nenhuma fonte varrida diz qual.**
Fica `[a preencher]` até alguém do atendimento responder — **derivar dos dois seria inventar.**

### O que isso cobre e o que não cobre
**Sete áreas têm alias**, seis delas resolvidas. **As outras sete não têm nenhum sinal**:
`04_Qualidade` · `05_PCP` · `07_Logistica-CD` · `10_Marketing` · `11_Financeiro` ·
`12_Design` · `13_Modelagem`.

> **Não conclua que elas não existem na Reserva.** Conclua que **nenhuma das fontes varridas as
> menciona** — e que a conta não tem a fonte (tabela de PLM) que as revelaria.

## Sistemas e fontes de verdade
### Drive de operação
Pasta registrada na base — `1vMZkhGi91KZ_D_r5FGCfhNxIBXAfUldl`. **Não varrida.**

### Outras fontes
| Fonte | Ferramenta | Estado |
|---|---|---|
| 🔴 **Kanbanize** — `umode.kanbanize.com`, **boards 6 e 18** | Kanbanize | **não varrido — sistema inteiro fora do inventário** |
| Formulário de novas demandas | Notion | **não varrido** |
| Chat da plataforma — **Gist** | Gist | **não varrido** |
| Review Quinzenal de Projeto | Google Slides | **não varrido** — 6 PPTs referenciados |
| Playbooks Reserva | Notion | **não varrida** |
| Miro Regras e restrições | Miro | **não varrida** |
| Termo de abertura de Projeto - Sourcing | Notion | **não varrido** |
| Roundtable · Blazers · Onboarding>Ongoing | Notion | **não varridas** |
| Portal uMode \| Reserva | Notion | **não varrido** |
| Reuniões & Demandas · Atas de Reunião | Notion | **não varridas** |
| `Chamados & Atendimentos` | Notion | ✅ **varrida — 8 chamados de `@usereserva.com` + 5 de fornecedor** |
| `Mapa de Clientes` · `Segmentação Grupos` | Notion | ✅ **varridas** |

> 🔴 **Produtos citados na página que não são o uFlow/PLM: `uBuy` e `uPlan`.**
> Aparecem em *"DE/PARA Campos uBuy"*, *"Ficha de Pedido uBuy"* e *"Dados para uPlan"*.
> **Não estão no inventário de produtos do BrainHub.**

## Contexto crítico
### Onde estamos
Conta **`Enterprise`**, a de maior alocação e única com os **7 módulos**. É também a conta com a
**operação mais instrumentada** que se viu: comunicação oficial declarada por escrito, cadência
nomeada, curadoria de canal e review quinzenal formal.

**A cadência declarada na própria página:** *"Média de Atendimento: 1 chamado por dia | 2 reuniões
por semana"*.

### 🔴 A frente aberta
**A página lista sete cards do Kanbanize, e cinco seguem em aberto** — marcados como
*"IMPORTANTES DE SEREM FINALIZADOS OU DE TEREM SOLUÇÃO PLANEJADA"* para uma visita presencial
de **13 e 14/ago/2024**:

| Card | Board | Estado na página |
|---|---|---|
| Reunião Preço | 6 / 15416 | ✅ finalizado |
| Dash Bazar | 6 / 14778 | ✅ finalizado |
| **Lentidão Follow/filtros** | 18 / 15464 | ⬜ **aberto** — vídeo da Ju, e-mail do João em 30/07 |
| **Dificuldade de Exportação/edição do Mapa** | 18 / 15148 | ⬜ **aberto** — vídeo da Ju, e-mail do João em 30/07 |
| **Inativar Variantes de Materiais** | 18 / 15040 | ⬜ **aberto** |
| **Erro Filtro de Composição** | 18 / 14971 | ⬜ **aberto** |
| **Carta Lacre com somente itens aprovados** | 18 / 14890 | ⬜ **aberto** |

> ⚠ **A página foi editada pela última vez em 30/06/2026** e esses cards continuam marcados como
> abertos desde **agosto de 2024**. **Quase dois anos.** Não afirmo que seguem abertos no Kanbanize
> — **afirmo que a página do cliente os mostra assim, e que o Kanbanize não foi varrido.**

**Assuntos declarados como pendentes na mesma preparação:** DE/PARA Campos uBuy · Ficha de Pedido
uBuy · Explosão MP · Dados para uPlan · Cronograma.

### O que o cliente espera
**Review Quinzenal de Projeto**, enviado à **Claudinha** a cada quinzena, em PPT sobre template
fixo. **Início em 16/05.** O registro diz: *"João está como responsável para estruturar essa
task"*.

> ⚠ **Dos 6 envios listados, 4 estão marcados como feitos e 2 não** (15/07 e 02/08), mais um
> **21/08 sem link**. **A cadência prometida degrada no próprio registro.**

### As dores estruturais registradas
1. **Dificuldade de exportação/edição do Mapa** — card aberto no board 18.
   > 🔴 **É a terceira vez que esta dor aparece, em três clientes diferentes.** Na Caedu, o
   > mapeamento de conta mostrou que a origem do produto vive na ficha e não na variante, e como a
   > validação é por variante isso obriga exportações extensas. No Puket, virou chamado de
   > usabilidade sobre **tempo de exportação**. Aqui, card de Kanbanize com vídeo e e-mail.
   > **Três casos independentes deixam de ser anedota: é defeito de modelo de dado.**
2. **Lentidão em Follow e filtros** — card aberto, com vídeo.
3. **Erro no filtro de composição** · **inativar variantes de materiais** · **carta lacre** — abertos.
4. **Confidencialidade de autoria.** Duas vezes em janeiro de 2026 um fornecedor pediu **o nome de
   quem alterou uma referência**, e o atendimento negou — *"Informei que não podemos passar"*.
   > **É regra de negócio aplicada por julgamento individual, registrada em texto livre.** Virou o
   > campo `disclosurePolicy` na [`_espec-pessoas-e-comunicacoes.md`](../../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md).

### Tamanho de atendimento
Grupo **`Enterprise`** · `WIP Estratégico 6,00` · **Fernanda**, que atende as **3 contas
Enterprise** (Reserva, Oficina Reserva, NV).

## Governança
### Responsável de atendimento (uMode)
Fernanda (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Status, módulos, ERP, atendimento, segmentação | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |
| Grade de segmentação e WIP | Notion — base `Segmentação Grupos` | **varrido 21/09/2026** |
| Aliases de área, canais, cards, review | Notion — corpo da página `Reserva` | **varrido 21/09/2026** |
| Chamados, pessoas e confidencialidade | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Reserva`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)

**Integração deste cliente:** [integracao.md](integracao.md)

**Registros:** **120 demandas** — [índice](../_demandas/_indice.md) · **2 RFIs** — [índice](../_rfis/_indice.md) · **13 fichas de pessoa** — [índice](../_pessoas/_indice.md)

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
