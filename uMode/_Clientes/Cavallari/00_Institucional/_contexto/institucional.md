---
aliases:
  - "Cavallari · Institucional"
tags:
  - tipo/institucional
  - cliente/cavallari
  - status/sem-cs
---
# Cavallari · Institucional

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

- id: cavallari — [varredura do Notion · 2026-09-22]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: SMB — [varredura do Notion · 2026-09-22]
- status: Sem CS — [varredura do Notion · 2026-09-22]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: Sem Integração — [varredura do Notion · 2026-09-22]
- modulo-contratado: Gestão de Coleção — [varredura do Notion · 2026-09-22]
- contrato-situacao: Assinado — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: 2021-02-15 → sem data de término · vigência Indeterminado — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: Renovação N/A · aviso prévio 150 dias — [planilha de contratos do Financeiro · 2026-09-23]
- indice-reajuste: IGPM — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: ? — [sem fonte]
- usuarios-conta: ? — [sem fonte]
- atendimento: SMB — [nao resolvido: sem ficha com e-mail para este nome]
- tamanho-atendimento: Grupo SMB · WIP Estratégico 1,75 · sem pessoa de atendimento nomeada — [varredura do Notion · 2026-09-22]

## ⚠ O que este documento NÃO resolve
- 🔴 **A página do cliente não foi varrida.** O que se sabe vem da linha da base.
- **Nenhuma pessoa foi identificada** além das que abriram chamado.
- **Não sei se a conta está em uso.** `Sem CS` não diz nada sobre uso.

## Identidade
### ID do cliente
`cavallari`

### Aliases do cliente
`Cavallari`

### Quem são
`[a preencher]`

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
`SMB` — Grupo 3. `WIP Estratégico 1,75`.

## Operação uMode
### Status atual
**`Sem CS`** — lido na base em 22 set 2026.

🔴 **`Sem CS` NÃO é momento da jornada — é modo de atendimento**, e na prática um **SKU self-service**: `Atendimento = SMB` (que é segmento, não pessoa), `ERP = Sem Integração`, e **só o módulo `Gestão de Coleção`**. Ver [`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md).

### Data de ativação
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 6 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
### Módulos contratados
`Gestão de Coleção` — **1 de 7**

### Usuários da conta
`[a preencher]`

### ERP / Integração
**`Sem Integração`** — declarado na base.

> ⚠ **É o mesmo valor nos 7 clientes `Sem CS`.** **Não há integração com ERP nesta conta**, o que é coerente com o único módulo contratado.

### Responsável de atendimento (uMode)
🔴 **`SMB`** — **e isso não é uma pessoa.**

> `SMB` é o nome do **Grupo 3 da base `Segmentação Grupos`**, colocado num campo que nos outros clientes contém nome de gente (Julianne & Pedro, Laura, Fernanda). **É a forma que a base encontrou de dizer "ninguém atende".**

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinado** — serviços faturados: `uFlow`.
### Vigência
**2021-02-15 → **sem data de término**** · vigência Indeterminado
### Renovação e aviso prévio
Renovação **N/A** · aviso prévio **150 dias**
### Índice de reajuste
IGPM
### Usuários contratados
`[a preencher]` — ⚠ **a própria planilha marca como A CONFIRMAR.**
### Pendências contratuais registradas
Nenhuma registrada na planilha.
## Aliases de áreas
### Mapeamento alias → canônico
`[a preencher]`

## Sistemas e fontes de verdade
### Drive de operação
Pasta registrada na base — **não varrida**.

### Outras fontes
| Fonte | Estado |
|---|---|
| Página do cliente no Notion | **não varrida** |

## Contexto crítico
### Onde estamos
Conta **self-service**: 1 módulo, sem integração, sem CS dedicado.

🔴 **Os 7 clientes `Sem CS` têm exatamente o mesmo perfil:** `Atendimento = SMB` (que é **grupo de segmentação, não pessoa**), `ERP = Sem Integração` e **só o módulo `Gestão de Coleção`**. **É um SKU self-service, não um estágio de jornada.** Ver [`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md).

### 🔴 A frente aberta
`[a preencher]`

### O que o cliente espera
`[a preencher]`

### As dores estruturais registradas
`[a preencher]`

### Tamanho de atendimento
Grupo **`SMB`** · `WIP Estratégico 1,75` · **sem pessoa de atendimento nomeada**.

## Governança
### Responsável de atendimento (uMode)
`SMB` — sem CS dedicado

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Todos os campos | Notion — base `Mapa de Clientes` | **varrido 22 set 2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Cavallari`

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
