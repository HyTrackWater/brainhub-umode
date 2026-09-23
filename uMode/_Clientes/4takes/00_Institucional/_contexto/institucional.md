---
aliases:
  - "4takes · Institucional"
tags:
  - tipo/institucional
  - cliente/4takes
  - status/churn
---
# 4takes · Institucional

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

- id: 4takes — [varredura do Notion · 2026-09-22]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: Churn — [base Segmentação Grupos · 2026-09-22]
- status: Churn — [varredura do Notion · 2026-09-22]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: Sem Integração — [varredura do Notion · 2026-09-22]
- modulo-contratado: Gestão de Coleção — [varredura do Notion · 2026-09-22]
- contrato-situacao: Assinar renovação — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: 2020-11-13 → 2022-11-03 — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: ? — [sem fonte]
- indice-reajuste: IGPM — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: ? — [sem fonte]
- usuarios-conta: ? — [sem fonte]
- atendimento: SMB — [nao resolvido: sem ficha com e-mail para este nome]
- tamanho-atendimento: ? — [sem fonte]

## ⚠ O que este documento NÃO resolve
- 🔴 **A página do cliente não foi varrida.** O que se sabe vem da **linha da base `Mapa de Clientes`**.
- 🔴 **NÃO SEI POR QUE ESTE CLIENTE SAIU.** **Nenhuma fonte varrida registra motivo de churn de nenhum cliente** — nem data de saída. **É a lacuna mais cara do corpus.**

## Identidade
### ID do cliente
`4takes`

### Aliases do cliente
`4takes`

### Quem são
**São Paulo (SP).**

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
`Churn` — grupo próprio na base `Segmentação Grupos`.

## Operação uMode
### Status atual
**`Churn`** — lido na base em 22 set 2026.

🔴 **`Churn`** — **fim de relação.** O cliente saiu. **A casa continua a existir no corpus** porque **histórico de cliente perdido é exatamente o que o BrainHub existe para não perder** — e porque **churn tem causa, e causa é aprendizado.**

### Data de ativação
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 6 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
### Módulos contratados
`Gestão de Coleção` — **1 de 7**

### Usuários da conta
`[a preencher]`

### ERP / Integração
**`Sem Integração`** — mesmo perfil dos clientes `Sem CS`.

### Responsável de atendimento (uMode)
**`SMB`** — ⚠ **segmento, não pessoa.** Mesmo padrão dos clientes `Sem CS`.

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinar renovação** — serviços faturados: `uFlow`.
### Vigência
**2020-11-13 → 2022-11-03** · vigência 24 meses
### Renovação e aviso prévio
Renovação **Via assinatura** · aviso prévio `[a preencher]`
### Índice de reajuste
IGPM
### Usuários contratados
`[a preencher]` — ⚠ **a própria planilha marca como A CONFIRMAR.**
### Pendências contratuais registradas
🔴 **Contrato vencido em 2023 (valores desatualizados)**

> Texto literal do campo `OBS` da planilha de contratos. **Não interpretei.**
## Aliases de áreas
### Mapeamento alias → canônico
`[a preencher]`

## Sistemas e fontes de verdade
### Drive de operação
`[a preencher]` — **nenhuma pasta registrada na base**

### Outras fontes
| Fonte | Estado |
|---|---|
| `[a preencher]` | — |

## Contexto crítico
### Onde estamos
🔴 **Cliente encerrado.** A casa existe no corpus porque **histórico de cliente perdido é exatamente o que o BrainHub existe para não perder** — e porque **churn tem causa, e causa é aprendizado.**

> 🔴 **A causa não está em lugar nenhum.** Varri a base, a base de chamados, a de segmentação e a de portais. **Nenhuma tem campo de motivo de saída nem data de saída.**

### 🔴 A frente aberta
**Nenhuma — o cliente saiu.**

> ⚠ **E a data de saída também não existe.** A base tem `Data Ativação Cliente` e **não tem `Data de Churn`**. **Não dá para calcular tempo de vida de cliente nenhum.**

### O que o cliente espera
`[a preencher]`

### As dores estruturais registradas
`[a preencher]`

### Tamanho de atendimento
`[a preencher]`

## Governança
### Responsável de atendimento (uMode)
`SMB`

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Todos os campos | Notion — base `Mapa de Clientes` | **varrido 22 set 2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `4takes`

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
