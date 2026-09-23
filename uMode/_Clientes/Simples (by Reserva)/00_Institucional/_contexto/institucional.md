---
aliases:
  - "Simples (by Reserva) · Institucional"
tags:
  - tipo/institucional
  - cliente/simples-by-reserva
  - status/inativo
---
# Simples (by Reserva) · Institucional

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

- id: simples-by-reserva — [varredura do Notion · 2026-09-22]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- status: Inativo — [varredura do Notion · 2026-09-22]
- data-ativacao: ? — [sem fonte]
- erp: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- modulo-contratado: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- contrato-situacao: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-23]
- indice-reajuste: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: ? — [não consta em: planilha de contratos do Financeiro · 2026-09-23]
- usuarios-conta: ? — [não consta em: tabela de usuários do PLM · 2026-09-23]
- atendimento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- tamanho-atendimento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]

## ⚠ O que este documento NÃO resolve
- 🔴 **ESTE CLIENTE NÃO EXISTE NA BASE `Mapa de Clientes`.** Ele existe no **corpus** e na base **`Portal do Cliente`** — e **em nenhuma das 50 linhas da base principal.**
- 🔴 **Portanto não há status, módulos, ERP, atendimento nem segmentação.** O `Inativo` acima **é marcação minha por ausência de fonte, não valor lido.**
- **A página do portal não foi varrida.**

## Identidade
### ID do cliente
`simples-by-reserva`

### Aliases do cliente
`Simples (by Reserva)` (corpus) · **`Simples Reserva`** (base `Portal do Cliente`) — ⚠ **duas grafias, e nenhuma delas está no `Mapa de Clientes`**

### Quem são
`[a preencher]` — **o nome indica marca do ecossistema Reserva**, junto de `Reserva` e `Oficina Reserva`. **Não confirmado em fonte.**

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

`[a preencher]` — campo **`Segmentação Grupos` vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** os 50 registros da base foram lidos por SQL em **23/09/2026**. **Vazio neste cliente.**

## Operação uMode
### Status atual
**`Inativo`** — lido na base em 22 set 2026.

⚠ **`Inativo`** — **estado terminal ou linha de apoio.** ⚠ **Cuidado:** algumas linhas `Inativo` da base **não são clientes** (template, `Fornecedores`, `uMode`). Esta foi tratada como cliente porque tem nome de empresa.

### Data de ativação
`[a preencher]` — **o campo não existe para este cliente.**

### Módulos contratados

`[a preencher]` — campo **`Módulos Contratados` vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** os 50 registros da base foram lidos por SQL em **23/09/2026**. **Vazio neste cliente.**

### Usuários da conta

`[a preencher]` — 🔴 **não há tabela de usuários do PLM varrida para esta conta.**
> **Ausência VERIFICADA em 23/09/2026.** No corpus inteiro, só **Caedu, Puket e NK STORE** têm tabela de usuários lida. ⚠ **Não afirmo que a conta não tenha usuários** — afirmo que **não há fonte varrida que os liste.**

### ERP / Integração

`[a preencher]` — campo **`ERP/Integração` vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** os 50 registros da base foram lidos por SQL em **23/09/2026**. **Vazio neste cliente.**

### Responsável de atendimento (uMode)

`[a preencher]` — campo **`Atendimento 2025` vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** os 50 registros da base foram lidos por SQL em **23/09/2026**. **Vazio neste cliente.**

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato

`[a preencher]` — 🔴 **`Simples (by Reserva)` não consta na planilha de contratos do Financeiro.**
> **Ausência VERIFICADA:** os **41 registros** da base foram conferidos um a um em **23/09/2026**. ⚠ **A ausência é da fonte** — ou o contrato existe fora dela, ou não existe. **Quem confirma é o Financeiro.**

### Vigência

`[a preencher]` — 🔴 **`Simples (by Reserva)` não consta na planilha de contratos do Financeiro.**
> **Ausência VERIFICADA:** os **41 registros** da base foram conferidos um a um em **23/09/2026**. ⚠ **A ausência é da fonte** — ou o contrato existe fora dela, ou não existe. **Quem confirma é o Financeiro.**

### Renovação e aviso prévio

`[a preencher]` — 🔴 **`Simples (by Reserva)` não consta na planilha de contratos do Financeiro.**
> **Ausência VERIFICADA:** os **41 registros** da base foram conferidos um a um em **23/09/2026**. ⚠ **A ausência é da fonte** — ou o contrato existe fora dela, ou não existe. **Quem confirma é o Financeiro.**

### Índice de reajuste

`[a preencher]` — 🔴 **`Simples (by Reserva)` não consta na planilha de contratos do Financeiro.**
> **Ausência VERIFICADA:** os **41 registros** da base foram conferidos um a um em **23/09/2026**. ⚠ **A ausência é da fonte** — ou o contrato existe fora dela, ou não existe. **Quem confirma é o Financeiro.**

### Usuários contratados

`[a preencher]` — 🔴 **`Simples (by Reserva)` não consta na planilha de contratos do Financeiro.**
> **Ausência VERIFICADA:** os **41 registros** da base foram conferidos um a um em **23/09/2026**. ⚠ **A ausência é da fonte** — ou o contrato existe fora dela, ou não existe. **Quem confirma é o Financeiro.**

### Pendências contratuais registradas

`[a preencher]`

## Aliases de áreas
### Mapeamento alias → canônico
`[a preencher]` — nenhuma fonte varrida menciona área deste cliente.

## Sistemas e fontes de verdade
### Drive de operação
`[a preencher]` — **não há linha na base para registrar pasta.**

### Outras fontes
| Fonte | Estado |
|---|---|
| **Portal uMode | Simples Reserva** — criado em **18/10/2024** | **não varrida** |
| Qualquer página de cliente — **não existe** | **não varrida** |

## Contexto crítico
### Onde estamos
🔴 **É o caso inverso da Loungerie — e fecha o diagnóstico das duas listas.**

| | Existe no `Mapa de Clientes`? | Existe no `Portal do Cliente`? | Existe no corpus? |
|---|:-:|:-:|:-:|
| **Loungerie** | ✅ | — | ❌ **até 22/09/2026** |
| **Simples (by Reserva)** | ❌ | ✅ | ✅ |
| **Inbrands, Malwee e outros 5** | ❌ | ✅ | ❌ |

> 🔴 **As duas bases de cliente do Notion não se falam**, e o corpus herdou o resultado de ambas sem saber. A relação `Clientes` da base `Portal do Cliente` está **vazia nas 32 linhas** — nenhum portal aponta de volta para o cliente.
>
> Registrado na [`_varredura-2026-09-21-fontes-e-lacunas.md`](../../../../00_Institucional/_contexto/_varredura-2026-09-21-fontes-e-lacunas.md).

### 🔴 A frente aberta
🔴 **Reconciliar as duas listas de cliente do Notion.**

**Este cliente é a prova de que a reconciliação tem que ser nos dois sentidos** — não basta criar no corpus o que falta do `Mapa de Clientes`; **há cliente no corpus que o `Mapa` não conhece.**

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
| Existência do portal | Notion — base `Portal do Cliente` | **varrido 21/09/2026** |
| **Ausência** no `Mapa de Clientes` | Notion — base `Mapa de Clientes`, 50 linhas | **varrida 22 set 2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Simples (by Reserva)`

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
