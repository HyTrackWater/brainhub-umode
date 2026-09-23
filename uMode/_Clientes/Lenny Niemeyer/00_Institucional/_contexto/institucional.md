---
aliases:
  - "Lenny Niemeyer · Institucional"
tags:
  - tipo/institucional
  - cliente/lenny-niemeyer
  - status/churn
---
# Lenny Niemeyer · Institucional

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

- id: lenny-niemeyer — [varredura do Notion · 2026-09-22]
- segmento: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: Churn — [base Segmentação Grupos · 2026-09-22]
- status: Churn — [varredura do Notion · 2026-09-22]
- data-ativacao: 03/02/2025 — [varredura do Notion · 2026-09-22]
- erp: Linx — [varredura do Notion · 2026-09-22]
- modulo-contratado: ? — [sem fonte]
- contrato-situacao: Assinado — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: 2025-02-03 → 2028-02-02 · vigência 36 meses — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: Renovação Automática · aviso prévio 60 dias — [planilha de contratos do Financeiro · 2026-09-23]
- indice-reajuste: IPCA — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: 42 internos — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-conta: 30 pessoas com ficha própria no corpus — [varredura do Notion · 2026-09-22]
- atendimento: pessoa:julianne.dias@umode.com.br — [varredura do Notion · 2026-09-22]
- atendimento: Pedro — [ambiguo: mais de um e-mail para este nome]
- tamanho-atendimento: ? — [sem fonte]

## ⚠ O que este documento NÃO resolve
- 🔴 **A página do cliente não foi varrida.** O que se sabe vem da **linha da base `Mapa de Clientes`**.
- 🔴 **NÃO SEI POR QUE ESTE CLIENTE SAIU.** **Nenhuma fonte varrida registra motivo de churn de nenhum cliente** — nem data de saída. **É a lacuna mais cara do corpus.**

## Identidade
### ID do cliente
`lenny-niemeyer`

### Aliases do cliente
`Lenny Niemeyer`

### Quem são
**Rio de Janeiro.** CNPJ `07.543.288/0001-90`. Financeiro: `contasapagar@lenny.com.br`.

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
**03/02/2025** — 🔴 **preenchida, e o cliente está em `Churn`.**

### Módulos contratados
`[a preencher]` — **campo vazio na base**

### Usuários da conta
**30 pessoas com ficha própria** no corpus.

> 🔴 **Isto é contagem de PESSOA DOCUMENTADA, não de licença contratada** — o número contratado está em `## Contrato › Usuários contratados`. **Os dois divergem por natureza** e não devem ser somados nem comparados sem olhar a fonte de cada um.

> Índice: [`_pessoas/_indice.md`](../_pessoas/_indice.md)
### ERP / Integração
**`Linx`**.

### Responsável de atendimento (uMode)
**Julianne & Pedro** (2025) — ⚠ **e a dupla segue atribuída a uma conta em churn**.

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinado** — serviços faturados: `uFlow`.
### Vigência
**2025-02-03 → 2028-02-02** · vigência 36 meses
### Renovação e aviso prévio
Renovação **Automática** · aviso prévio **60 dias**
### Índice de reajuste
IPCA
### Usuários contratados
42 internos
### Pendências contratuais registradas
Nenhuma registrada na planilha.
## Aliases de áreas
### Mapeamento alias → canônico
`[a preencher]`

## Sistemas e fontes de verdade
### Drive de operação
`[a preencher]` — **nenhuma pasta registrada na base**

### Outras fontes
| Fonte | Estado |
|---|---|
| **5 páginas de `Documentação Clientes`** | **não varrida** |
| Página do cliente no Notion | **não varrida** |

## Contexto crítico
### Onde estamos
🔴 **Cliente encerrado.** A casa existe no corpus porque **histórico de cliente perdido é exatamente o que o BrainHub existe para não perder** — e porque **churn tem causa, e causa é aprendizado.**

> 🔴 **A causa não está em lugar nenhum.** Varri a base, a base de chamados, a de segmentação e a de portais. **Nenhuma tem campo de motivo de saída nem data de saída.**

### 🔴 A frente aberta
🔴 **O cliente está em `Churn` E ABRIU 5 CHAMADOS EM JANEIRO DE 2026.**

> **Status na base ≠ uso real da plataforma.** Quatro pessoas distintas abriram chamado depois de a conta constar como encerrada.
>
> **Ou o churn é posterior a jan/2026, ou o status está errado, ou a conta continua no ar sem contrato.** **Nenhuma fonte varrida resolve.** `[D]`

### O que o cliente espera
`[a preencher]`

### As dores estruturais registradas
`[a preencher]`

### Tamanho de atendimento
`[a preencher]`

🔴 **ESTE CLIENTE FAZ PARTE DE UM COORTE QUE FALHOU INTEIRO.**

Três clientes têm `Data Ativação Cliente` preenchida **e estão em `Churn`** — e as três ativações acontecem em **oito dias**:

| Cliente | Ativado em | ERP |
|---|---|---|
| **Lenny Niemeyer** | **03/02/2025** | Linx |
| **Recco** | **06/02/2025** | Totvs |
| **Highstil** | **11/02/2025** | Totvs |

> **Três ativações consecutivas de fevereiro de 2025, todas terminadas em saída.**
>
> **Não afirmo a causa** — não li as páginas nem os contratos. Afirmo o padrão, com data, e que **nenhuma fonte varrida registra o motivo de nenhuma das três saídas**.
>
> **É a pergunta mais valiosa de toda a varredura de churn.** Ver [`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md).

> 🔴 **CORREÇÃO — 22 set 2026.** Esta leitura de "coorte" era minha e estava errada no que
> sugeria. As três contas foram **ativadas** em oito dias, mas **não morreram juntas**:
> **Recco ~8 meses** (última atividade **16/10/2025**) · **Lenny Niemeyer ~14 meses**
> (**01/04/2026**) · **Highstil ~14 meses** (**16/04/2026**). Lenny e Highstil seguiram com
> reunião até **abril de 2026**, já marcadas como `Churn`. **É coorte de ativação, não de morte.**
> ⚠ **"Última atividade observada" não é data de saída** — a base **não tem `Data de Churn`**.
> Ver `_varredura-2026-09-22-reunioes-compartilhadas.md` § 4.

## Governança
### Responsável de atendimento (uMode)
Julianne & Pedro (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Todos os campos | Notion — base `Mapa de Clientes` | **varrido 22 set 2026** |
| 5 chamados e 4 pessoas | Notion — `Chamados & Atendimentos` | **varrido 22 set 2026** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Lenny Niemeyer`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)


**Registros:** **69 demandas** — [índice](../_demandas/_indice.md) · **4 RFIs** — [índice](../_rfis/_indice.md) · **30 fichas de pessoa** — [índice](../_pessoas/_indice.md)

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
