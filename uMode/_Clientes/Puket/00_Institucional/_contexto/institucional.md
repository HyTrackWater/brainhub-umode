---
aliases:
  - "Puket · Institucional"
tags:
  - tipo/institucional
  - cliente/puket
  - status/ongoing
---
# Puket · Institucional

> **Reescrito em 21 set 2026 a partir do Notion ao vivo** — base `Mapa de Clientes`, página do
> cliente, base `Segmentação Grupos`, base `Reuniões com o cliente` e base
> `Chamados & Atendimentos`. Campo sem fonte fica `[a preencher]` — nada foi inferido.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- id: puket — [base Segmentação Grupos · 2026-09-21]
- segmento: ? — [sem fonte]
- receita-anual: ? — [sem fonte]
- grupo-segmentacao: SMB — [base Segmentação Grupos · 2026-09-21]
- status: Ongoing — [base Segmentação Grupos · 2026-09-21]
- data-ativacao: ? — [sem fonte]
- erp: Linx / SAP — [base Segmentação Grupos · 2026-09-21]
- modulo-contratado: Gestão de Coleção · Integração — [base Segmentação Grupos · 2026-09-21]
- contrato-situacao: Assinado — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: Fashion IA — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: 2022-03-09 → 2024-03-09 · vigência 24 meses — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: Renovação Automática · aviso prévio 90 dias — [planilha de contratos do Financeiro · 2026-09-23]
- indice-reajuste: IPCA — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: 60 — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-conta: 43 com acesso ao PLM, em 13 perfis. Detalhe nominal em pessoas.md — [base Segmentação Grupos · 2026-01-08]
- atendimento: pessoa:julianne.dias@umode.com.br — [base Mapa de Clientes · 2026-09-21]
- atendimento: Pedro — [ambiguo: mais de um e-mail para este nome]
- tamanho-atendimento: Grupo SMB · WIP Estratégico 1,75 · dupla Julianne & Pedro, que atende também Caedu — [base Segmentação Grupos · 2026-09-21]

## Identidade
### ID do cliente
`puket`

### Aliases do cliente
`Puket` · `Grupo Único` (a holding — ver abaixo)

### Quem são
🔴 **Puket é marca do Grupo Único, e a conta cobre as duas camadas.** A evidência é o domínio dos
43 usuários do PLM:

| Domínio | Pessoas | Camada |
|---|---:|---|
| `@grupounico.com` | 20 | **holding** — Sourcing, Qualidade, Controladoria, Importação, Projetos, BI, Certificação |
| `@puket.com.br` | 22 | **marca** — Estilo, Design, maior parte de Produto, PCP, TEX |
| `@grupounico.hk` | 1 | **Hong Kong** — perfil Estilo, indica sourcing internacional |

> **Isso não é detalhe de e-mail — é desenho de brain.** O corte funcional segue o corte
> societário: a holding faz suprimento, controle e qualidade; a marca faz criação e produto.
> **Confirmar com o atendimento** se o contrato é com Puket ou com o Grupo Único.

### O que fazem
`[a preencher]` — nenhuma fonte varrida descreve o negócio. Os campos `Razão Social`,
`Setor da Empresa`, `Área de Atuação`, `Cidade`, `Estado` e `CNPJ` estão **vazios na base**.

### Para quem fazem
`[a preencher]`

## Posicionamento
### Segmento
`[a preencher]` — campo `Setor da Empresa` vazio na base.

### Receita anual
`[a preencher]` — campo vazio na base.

### Grupo de segmentação uMode
**`SMB`** — Grupo 3 da base `Segmentação Grupos`. `WIP Time 10` · `WIP Estratégico 1,75`.

A grade completa da uMode, varrida por inteiro:

| Grupo | Nome | WIP Estratégico | Clientes vivos |
|---|---|---:|---|
| 1 | **Enterprise** (*"Reserva + Soma"*) | 6,00 | Reserva · Oficina Reserva · NV |
| 2 | **Médios** | 2,25 | Cambos · Lofty Style · Luiza Barcelos · NK STORE · VIX · Osklen · Moda Objetiva · Loungerie |
| 3 | **SMB** | 1,75 | **Puket** · Caedu |
| 4 | Outros Clientes | — | — |
| — | Churn | — | — |

> ⚠ **Tensão a levar ao negócio:** a Puket é classificada como **SMB**, o grupo de menor alocação —
> tendo **43 usuários em duas camadas societárias e presença em Hong Kong**. A CAEDU, no mesmo
> grupo, tem 93 usuários. **A segmentação não parece acompanhar o tamanho da conta.**
>
> ⚠ A base `Segmentação Grupos` está sob a pasta **`Arquivo`** no Notion. **Confirmar se ainda
> é a segmentação vigente** ou se foi substituída.

## Operação uMode
### Status atual
**`Ongoing`** — valor lido na base em 21/09/2026.

Enum completo do campo `Status` na origem: `Inativo · Pré Onboardings · Operação Assistida ·
Onboarding · Sem CS · Ongoing · Churn`.

### Data de ativação
`[a preencher]` — o campo `Data Ativação Cliente` está **vazio na base**.

> **Mas há um piso verificável:** o primeiro acesso ao PLM é de **24/05/2022** (maria.germano e
> gabriela.begnini, perfil `Projetos`). A conta opera **desde maio de 2022, no mínimo**.
> A linha do cliente no Notion só foi criada em **22/05/2023** — um ano depois.

### Módulos contratados
**`Gestão de Coleção`** · **`Integração`**

> 🔴 **Só dois módulos — é a conta `Ongoing` mais enxuta da carteira.** Para comparação, na mesma
> varredura: Reserva tem 7, Oficina Reserva e Osklen têm 5, Caedu / NK STORE / Luiza Barcelos têm 4.
>
> Taxonomia vigente do campo, varrida na origem: `Gestão de Coleção · Integração · Relatórios ·
> Cronograma · Aposta · Planejamento · Fornecedores`.
>
> ⚠ **A Puket não tem `Relatórios`** — e há um chamado de janeiro/2026 reclamando do **tempo de
> exportação**. Vale checar se a dor é exatamente a ausência desse módulo.

### Usuários da conta
**43** com acesso ao PLM, em **13 perfis**. Detalhe nominal em [`pessoas.md`](pessoas.md).

> ⚠ **A lista está desatualizada.** `beatriz.fraga@puket.com.br` abriu chamado em 08/01/2026 e
> **não consta entre os 43**. A tabela da página não é o cadastro vivo do PLM.

### ERP / Integração
**`Linx / SAP`** — dois ERPs, como Reserva. (Oficina Reserva aparece como `SAP e Linx`, o mesmo
par com grafia diferente — **erro de taxonomia na origem**.)

### Responsável de atendimento (uMode)
**Julianne + Pedro** — campo `Atendimento 2025` da base `Mapa de Clientes`, lido ao vivo em 23 set 2026.
## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinado** — serviços faturados: `uFlow` · `Fashion IA`.
### Vigência
**2022-03-09 → 2024-03-09** · vigência 24 meses
### Renovação e aviso prévio
Renovação **Automática** · aviso prévio **90 dias**
### Índice de reajuste
IPCA
### Usuários contratados
60
### Pendências contratuais registradas
🔴 **Criar aditivo atualização valores / falta anexo B no contrato com forma pgto**

> Texto literal do campo `OBS` da planilha de contratos. **Não interpretei.**
## Aliases de áreas
### Mapeamento alias → canônico

> A fonte é o **perfil de acesso no PLM** — o único vínculo pessoa↔área que existe em alguma fonte
> da uMode.
>
> 🔴 **A convenção de nome de perfil é de cada cliente, não da uMode.** A CAEDU usa
> `<Cliente>-<Área>`; a **Puket usa nomes de função puros**. O protocolo de varredura previa o
> padrão da CAEDU — **está corrigido a partir daqui**.

| Perfil no PLM | Pessoas | → Área canônica |
|---|---:|---|
| `Estilo` | 8 | `02_Estilo-Criacao` |
| `Produto` | 7 | `03_Desenvolvimento-de-Colecao` |
| `Sourcing Nacional` | 7 | `06_Compras-Supply-Sourcing` |
| `Projetos` | 4 | **transversal — não derivável** |
| `Qualidade` | 4 | `04_Qualidade` |
| `Design` | 4 | `12_Design` |
| `Importação` | 2 | `06_Compras-Supply-Sourcing` |
| `TEX` | 2 | ⚠ `[a preencher]` — sigla não explicada em nenhuma fonte |
| `Certificação` | 1 | `04_Qualidade` — **provisório, confirmar** |
| `PCP` | 1 | `05_PCP` |
| `BI` | 1 | **transversal — não derivável** |
| `Controladoria` | 2 | `11_Financeiro` — 1 dos 2 **riscado na origem** |

**Sete das 14 áreas canônicas têm gente.** Sem perfil correspondente:
`01_Planejamento` · `07_Logistica-CD` · `08_Ecommerce-Cadastro` · `09_Comercial-Vendas` ·
`10_Marketing` · `13_Modelagem` · `14_Engenharia`.

> **A grade de 14 áreas não se preenche igual em dois clientes — e isso é informação.**
> Puket tem **PCP, Design e Financeiro**, que a CAEDU não tem. Não tem **Planejamento, E-commerce
> nem Modelagem**, que a CAEDU tem.

> ⚠ **A lista de setores da página NÃO é esta taxonomia.**
A página do cliente traz um bloco *"Perfis de Acesso e Setor Operacional"* com
`Produto&Planejamento · Estilo · Compras · Operações (SAC) · Marketing · Comercial`.

**Não use esse bloco como fonte.** Cada item vem seguido de `(EX: ...)` — **são exemplos do
template, não a configuração da conta.** A taxonomia real é a tabela acima, extraída dos perfis
efetivamente atribuídos.

## Sistemas e fontes de verdade
### Drive de operação
Pasta do Google Drive registrada na base — `1dWv3w9Czh2W7r5DyHDRa4wC0BoWRaFy3`. **Não varrida.**

### Outras fontes
| Fonte | Onde | Estado |
|---|---|---|
| Playbooks | sub-página `5c5cabb0…` | **não varrida** |
| Treinamentos gravados | playlist no YouTube | **não varrida** |
| Miro Regras e restrições | sub-página `8822d890…` | **não varrida** |
| Onboarding → Ongoing | sub-página `3b7b8c08…` | **não varrida** |
| MAIO 2025 \| Evolução de Conta | sub-página `201b1d38…` | **não varrida** |
| Passada de bastão Puket | sub-página `855b8f8f…` | **não varrida** |
| Itens no sistema a serem vistos | sub-página `19f7f538…` | **não varrida** |
| `Mapeamento de Contas - Puket` | Documentação CX | **não localizada nesta varredura** |
| Análise Puket × Caedu | Documentação CX | **não localizada nesta varredura** |
| Reuniões com o cliente | `collection://c1120e06…` | ✅ **varrida — 23 atas** |
| Chamados & Atendimentos | `collection://2c5b1d38…` | ✅ **varrida — 5 chamados** |

## Contexto crítico
### Onde estamos
Conta `Ongoing` com **dois módulos**, **43 usuários** e **atendimento em silêncio**: a última ata
é de **08/01/2026** e o último chamado de **29/01/2026**. São **8 meses sem registro** até hoje.

### 🔴 A frente aberta

**A passada de bastão foi aberta e nunca preenchida.**
A página do cliente tem um título `Passada bastão Luciano` **sem nenhum conteúdo abaixo** e um
template de transição cujos campos estão **todos em branco ou com placeholder**:

`Marca` · `Linha de produção` · `Submarcas` · `Segmento` · `ERP` · `Integração ativa` ·
`Usuários Ativos` · `Departamentos engajados` · `Estrutura Template Product_datasheet` ·
`Estrutura Template Print` · `Aprovação` · `Workflow` · `Validações` · `Tarefas` ·
`Restrições` · `Link do Miro`

**O único bloco com dado real em toda a passada de bastão é a tabela de 43 usuários.**

> **Isso não é problema da Puket — é problema do ritual.** O template de handover existe e não está
> sendo concluído. **Vale checar quantas outras contas têm a passada de bastão em branco.**
> Quem é `Luciano`, quem saiu e quem assumiu: `[a preencher]`.

### O que o cliente espera
`[a preencher]` — nenhuma fonte varrida registra expectativa declarada.

### As dores estruturais registradas
Só há dor registrada em chamado; **não foi localizado mapeamento de conta para a Puket**.

1. **Tempo de exportação** (08/01/2026, `beatriz.fraga`, tipo `USABILIDADE`, **fechado**).
   > ⚠ **É a mesma dor estrutural da CAEDU** — lá o mapeamento mostrou que a origem do produto vive
   > na ficha e não na variante, e como a validação é por variante isso obriga exportações extensas.
   > **Se confirmar na Puket, é dor de modelo de dado comum à carteira, não caso isolado.**
2. **Perfil `Importação` não pode criar tarefas** (06/01/2026, `eduarda.souza`, **em aberto**).
   > Evidência direta de que **o perfil de acesso governa permissão funcional** — o que reforça o
   > perfil como o eixo pessoa↔área.

### Tamanho de atendimento
Grupo **SMB** · `WIP Estratégico 1,75` · dupla **Julianne & Pedro**, que atende também Caedu,
NK STORE, VIX, Osklen e Loungerie — **6 contas**.

## Governança
### Responsável de atendimento (uMode)
Julianne & Pedro (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Status, módulos, ERP, dupla, segmentação | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |
| Grade de segmentação e WIP | Notion — base `Segmentação Grupos` | **varrido 21/09/2026** |
| Usuários, perfis, domínios, datas | Notion — página `Puket`, tabela do PLM | **varrido 21/09/2026** |
| Atas e cadência | Notion — `Reuniões com o cliente (1)` | **varrido 21/09/2026** |
| Chamados e dores | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Estado da passada de bastão | Notion — corpo da página `Puket` | **varrido 21/09/2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Puket`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)

**Integração deste cliente:** [integracao.md](integracao.md)

**Registros:** **16 demandas** — [índice](../_demandas/_indice.md) · **9 RFIs** — [índice](../_rfis/_indice.md) · **43 fichas de pessoa** — [índice](../_pessoas/_indice.md)

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
