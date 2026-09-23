---
aliases:
  - "Arezzo · Institucional"
tags:
  - tipo/institucional
  - cliente/arezzo
  - status/pre-onboardings
---
# Arezzo · Institucional

> **Criado/reescrito em 22 set 2026 por varredura do Notion ao vivo.**
> Campo sem fonte fica `[a preencher]` — **nada foi inferido.**

> 🔴 **`Status` é estado de ciclo de vida, não tipo de cliente.**
> Enum vigente: `Inativo · Pré Onboardings · Operação Assistida · Onboarding · Sem CS · Ongoing · Churn`.
> Travado pelo Vinicius em 22 set 2026. Ver [`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md).

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- id: arezzo — [varredura do Notion · 2026-09-22]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: Enterprise — [varredura do Notion · 2026-09-23]
- status: Pré Onboardings — [varredura do Notion · 2026-09-22]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: SAP e Linx — [varredura do Notion · 2024-06-26]
- modulo-contratado: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- contrato-situacao: ? — [sem fonte]
- contrato-vigencia: ? — [sem fonte]
- contrato-renovacao: ? — [sem fonte]
- indice-reajuste: ? — [sem fonte]
- usuarios-contratados: ? — [sem fonte]
- usuarios-conta: ? — [não consta em: tabela de usuários do PLM · 2026-09-23]
- atendimento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- tamanho-atendimento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]

## ⚠ O que este documento NÃO resolve
- 🔴 **ESTA CASA ACABOU DE SER CRIADA.** A Arezzo **existia na base e não tinha casa no corpus**.
- 🔴 **A página não foi varrida** e **quase todos os campos da base estão vazios.**
- 🔴 **Não afirmo relação societária** entre Arezzo, AR&CO e Oficina Reserva. **Afirmo a dependência operacional registrada**, e nada além.

## Identidade
### ID do cliente
`arezzo`

### Aliases do cliente
`Arezzo`

### Quem são
`[a preencher]`

### O que fazem
`[a preencher]`

### Para quem fazem
`[a preencher]`

## Posicionamento
### Segmento
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026**. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 12 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
### Receita anual
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026**. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 2 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
### Grupo de segmentação uMode
**`Enterprise`** — **Grupo 1**, descrição *"Reserva + Soma"*. `WIP Time 10` · `WIP Estratégico 6`.
> 🟢 **Lido ao vivo em 23 set 2026** resolvendo a relação. O corpus registrava como ausente.

## Operação uMode
### Status atual
**`Pré Onboardings`** — lido na base em 22 set 2026.

⚠ **`Pré Onboardings`** — **ainda não é cliente**: está em ciclo comercial ou pré-implantação. **A casa existe para receber o contexto quando virar.**

### Data de ativação
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026**. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 6 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
### Módulos contratados

`[a preencher]` — campo **`Módulos Contratados` vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** os 50 registros da base foram lidos por SQL em **23/09/2026**. **Vazio neste cliente.**

### Usuários da conta

`[a preencher]` — 🔴 **não há tabela de usuários do PLM varrida para esta conta.**
> **Ausência VERIFICADA em 23/09/2026.** No corpus inteiro, só **Caedu, Puket e NK STORE** têm tabela de usuários lida. ⚠ **Não afirmo que a conta não tenha usuários** — afirmo que **não há fonte varrida que os liste.**

### ERP / Integração
**`SAP e Linx`** — 🔴 **exatamente a mesma grafia da Oficina Reserva.**

> **E isso não é coincidência de campo.** A página da **Oficina Reserva** registra, numa mensagem de Sales de 26/06/2024, que o cadastro de produto deles sofre por *"falta de time de apoio do SAP, **dependência do time da AREZZO**"*.
>
> **A Arezzo já opera dentro do processo de um cliente da uMode, e é prospect.**

### Responsável de atendimento (uMode)

`[a preencher]` — campo **`Atendimento 2025` vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** os 50 registros da base foram lidos por SQL em **23/09/2026**. **Vazio neste cliente.**

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato

`[a preencher]`

### Vigência

`[a preencher]`

### Renovação e aviso prévio

`[a preencher]`

### Índice de reajuste

`[a preencher]`

### Usuários contratados

`[a preencher]`

### Pendências contratuais registradas

`[a preencher]`

## Aliases de áreas
### Mapeamento alias → canônico
`[a preencher]`

## Sistemas e fontes de verdade
### Drive de operação
`[a preencher]` — **nenhuma pasta registrada na base**

### Outras fontes
| Fonte | Estado |
|---|---|
| Página do cliente no Notion | **não varrida** |

## Contexto crítico
### Onde estamos
**Prospect em pré-onboarding**, com quase todos os campos vazios.

🔴 **Mas há um fato que muda a leitura:** a **Oficina Reserva**, cliente `Ongoing`, **depende operacionalmente do time de SAP da Arezzo** — registrado em mensagem de Sales de **26/06/2024**.

> **A uMode já tem contato indireto com a operação da Arezzo, através de um cliente.** **Isso é informação comercial, e está enterrada num bloco recolhido de outra página.**

### 🔴 A frente aberta
🔴 **Ciclo comercial.** E há um ângulo registrado: a Oficina Reserva reclama de *"falta de time de apoio do SAP, dependência do time da AREZZO"*. **A dor de um cliente é a porta de entrada do outro.**

### O que o cliente espera
`[a preencher]`

### As dores estruturais registradas
`[a preencher]`

### Tamanho de atendimento

`[a preencher]` — 🔴 **o campo `Tamanho atendimento` NÃO EXISTE MAIS na base `Mapa de Clientes`.**
> **Verificado em 23/09/2026:** o schema da base viva tem 23 propriedades e **nenhuma delas é `Tamanho atendimento`**. ⚠ **Ele existia no export de 04/03/2026**, que o traz preenchido para vários clientes.
> 🔴 **Campo removido da origem, não campo vazio.** São coisas diferentes, e o valor que o corpus tiver dele é histórico de março — **não reconfirmável na base de hoje.**

## Governança
### Responsável de atendimento (uMode)
`[a preencher]`

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Todos os campos | Notion — base `Mapa de Clientes` | **varrido 22 set 2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Arezzo`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)


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
