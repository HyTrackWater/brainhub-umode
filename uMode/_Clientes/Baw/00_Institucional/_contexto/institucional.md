---
aliases:
  - "Baw · Institucional"
tags:
  - tipo/institucional
  - cliente/baw
  - status/sem-cs
---
# Baw · Institucional

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

- id: baw — [varredura do Notion · 2026-09-22]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: SMB — [varredura do Notion · 2026-09-23]
- status: Sem CS — [varredura do Notion · 2026-09-22]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: Sem Integração — [varredura do Notion · 2026-09-22]
- modulo-contratado: Gestão de Coleção — [varredura do Notion · 2026-09-22]
- modulo-contratado: Integração — [varredura do Notion · 2026-09-22]
- modulo-contratado: Relatórios — [varredura do Notion · 2026-09-22]
- modulo-contratado: Fornecedores — [varredura do Notion · 2026-09-22]
- contrato-situacao: Assinado — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: 2025-03-13 → 2028-03-11 · vigência 36 meses — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: Renovação Via assinatura · aviso prévio 90 dias — [planilha de contratos do Financeiro · 2026-09-23]
- indice-reajuste: IPCA — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: ? — [sem fonte]
- usuarios-conta: 3 pessoas com ficha própria no corpus — [varredura do Notion · 2026-09-22]
- atendimento: pessoa:laura.delgado@umode.com.br — [varredura do Notion · 2026-09-22]
- tamanho-atendimento: Laura, com 5 contas — [varredura do Notion · 2026-09-22]

## ⚠ O que este documento NÃO resolve
- 🔴 **A página do cliente não foi varrida.**
- 🔴 **Não sei por que esta conta está classificada como `Sem CS`** — ela quebra o padrão em todos os campos.
- **Não sei resolver a contradição** entre ter o módulo `Integração` e o ERP dizer `Sem Integração`.

## Identidade
### ID do cliente
`baw`

### Aliases do cliente
`Baw`

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
**`SMB`** — **Grupo 3**. `WIP Time 10` · `WIP Estratégico 1,75`.
> 🟢 **Lido ao vivo em 23 set 2026** resolvendo a relação. O corpus registrava como ausente.

## Operação uMode
### Status atual
**`Sem CS`** — lido na base em 22 set 2026.

🔴 **`Sem CS` NÃO é momento da jornada — é modo de atendimento**, e na prática um **SKU self-service**: `Atendimento = SMB` (que é segmento, não pessoa), `ERP = Sem Integração`, e **só o módulo `Gestão de Coleção`**. Ver [`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md).

### Data de ativação
`[a preencher]` — campo **vazio na base `Mapa de Clientes`**.
> 🔴 **Ausência VERIFICADA:** lido por SQL na base viva em **23/09/2026** e também no **export de 04/03/2026** que está no vault. **Vazio nos dois.**
> ⚠ **O campo está preenchido em 6 dos 49 clientes** — **não é lacuna deste cliente, é campo que a operação não preenche.**
### Módulos contratados
`Gestão de Coleção` · `Integração` · `Relatórios` · `Fornecedores` — **4 de 7**

### Usuários da conta
**3 pessoas com ficha própria** no corpus.

> 🔴 **Isto é contagem de PESSOA DOCUMENTADA, não de licença contratada** — o número contratado está em `## Contrato › Usuários contratados`. **Os dois divergem por natureza** e não devem ser somados nem comparados sem olhar a fonte de cada um.

> Índice: [`_pessoas/_indice.md`](../_pessoas/_indice.md)
### ERP / Integração
🔴 **`Sem Integração`** — **e isso contradiz o módulo contratado.**

> A conta tem **`Integração`** entre os módulos e o campo `ERP/Integração` diz **`Sem Integração`**. **Os dois não podem estar certos.** `[a preencher]`

### Responsável de atendimento (uMode)
**Laura** (2025) — **pessoa nomeada**, diferente dos outros 6 `Sem CS`, que têm `SMB`.

> A Laura atende também Cambos, Lofty Style, Luiza Barcelos e Moda Objetiva — **5 contas**.

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinado** — serviços faturados: `uFlow`.
### Vigência
**2025-03-13 → 2028-03-11** · vigência 36 meses
### Renovação e aviso prévio
Renovação **Via assinatura** · aviso prévio **90 dias**
### Índice de reajuste
IPCA
### Usuários contratados
`[a preencher]` — ⚠ **a própria planilha marca como A CONFIRMAR.**
### Pendências contratuais registradas
🔴 **não foi feito aditivo excluindo explosão MP**

> Texto literal do campo `OBS` da planilha de contratos. **Não interpretei.**
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
🔴 **A Baw é a única exceção ao padrão `Sem CS` da carteira.**

| | Os 6 outros `Sem CS` | **Baw** |
|---|---|---|
| Atendimento | `SMB` | **`Laura`** — pessoa nomeada |
| Módulos | 1 | **4** |
| Chamados em jan/2026 | 0 ou 2 | **9** |

> 🔴 **Um cliente com 4 módulos, atendimento nomeado e 9 chamados está classificado como "Sem CS".** **Ou o status está errado, ou a Baw é atendida sem que isso seja contabilizado.** `[D]` — **tem impacto em alocação.**

### 🔴 A frente aberta
**9 chamados em jan/2026, 4 abertos** — e **3 deles de instabilidade**.

⚠ **E há um chamado de um domínio externo** (`desenvolvimento@eczoz.com.br`) atribuído a esta conta: *"informou que as fotos do produto sumiram mas não respondeu mais"*. **Fornecedor ou terceiro operando dentro da conta** — mesmo padrão da Reserva.

### O que o cliente espera
`[a preencher]`

### As dores estruturais registradas
- **Material travado** (16/01/2026) — **também em NV e Lofty Style. Três clientes.**
- **Instabilidade recorrente** — 3 chamados.
- **Fotos de produto sumindo** — relatado por terceiro, **não respondido**.

### Tamanho de atendimento
**Laura**, com 5 contas — ⚠ **e esta conta não entra na contagem de CS**, por estar marcada `Sem CS`.

## Governança
### Responsável de atendimento (uMode)
Laura (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Todos os campos | Notion — base `Mapa de Clientes` | **varrido 22 set 2026** |
| 9 chamados e 3 pessoas | Notion — `Chamados & Atendimentos` | **varrido 22 set 2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Baw`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)

**Integração deste cliente:** [integracao.md](integracao.md)

**Registros:** **18 demandas** — [índice](../_demandas/_indice.md) · **4 RFIs** — [índice](../_rfis/_indice.md) · **3 fichas de pessoa** — [índice](../_pessoas/_indice.md)

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
