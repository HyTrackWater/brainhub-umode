---
aliases:
  - "Planejamento · Contexto de área — Caedu"
tags:
  - tipo/area
  - cliente/caedu
  - status/ongoing
  - area/planejamento
---
# Planejamento · Contexto de área — Caedu

> Criado em **21 set 2026** por varredura do Notion ao vivo. Campo sem fonte fica `[a preencher]`.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- produto-conectado: Gestão de Coleção — [base Mapa de Clientes · 2026-09-21]
- pessoas-da-area: 8 pessoas com perfil Caedu- Planejamento — [página Caedu em Databases / Mapa de Clientes · 2026-09-21]
- responsavel-area: ? — [não consta em: página Caedu em Databases / Mapa de Clientes · 2026-09-21]
- entrega: Criação dos produtos da coleção · importação de planilha base — [Mapeamento de Contas - Caedu · 2025-04-04]
- entrega: Sortimento e faixa de preço · definidos na planilha — [Mapeamento de Contas - Caedu · 2025-04-04]
- entrega: Campos obrigatórios iniciais · Nome, Linha, Origem, Departamento — [Mapeamento de Contas - Caedu · 2025-04-04]
- dor: Necessita padronização e conferência para evitar duplicidade — é o ponto crítico declarado no mapeamento de conta — [Mapeamento de Contas - Caedu · 2025-04-04]
- dor: Macroplan pouco explorado. Não há uso efetivo de um fluxo macro para agrupar coleções, o que gera risco de *overlap* entre produto Nacional e Importado — [Mapeamento de Contas - Caedu · 2025-04-04]

## O que esta área faz
É a **porta de entrada do fluxo**. O time de Planejamento ou os Gerentes de Produto importam a
planilha base que cria os produtos da coleção no PLM, com os campos obrigatórios iniciais:
**Nome, Linha, Origem e Departamento**.

Define sortimento e faixas de preço. Internamente a Caedu chama essa subida de
**"plano de sofrimento"**.

## Com quem se relaciona (interno e externo)
- **Entrega para** `02_Estilo-Criacao` — os produtos criados aqui é que serão aprovados lá.
- Depende de padronização da planilha para não gerar duplicidade.

## Entregas e responsabilidades
| Entrega | Como acontece |
|---|---|
| Criação dos produtos da coleção | importação de planilha base |
| Sortimento e faixa de preço | definidos na planilha |
| Campos obrigatórios iniciais | Nome, Linha, Origem, Departamento |

## Padrões operacionais

### Como trabalham

### Como trabalhamos
- A criação é **em lote, por importação** — não produto a produto.

### ⚠ Dores registradas
1. **Necessita padronização e conferência para evitar duplicidade** — é o ponto crítico declarado
   no mapeamento de conta.
2. **Macroplan pouco explorado.** Não há uso efetivo de um fluxo macro para agrupar coleções, o
   que gera risco de *overlap* entre produto Nacional e Importado.

### O que não fazem

`[a preencher]`

## Vocabulário da área

### Termos específicos

| Termo | O que significa aqui |
|---|---|
| **Plano de sofrimento** | nome interno da Caedu para a planilha base de sortimento |
| **Macroplan** | fluxo macro para agrupar coleções — existe e é subutilizado |
| **Sortimento** | composição da coleção por linha, faixa de preço e departamento |

## Pessoas desta área
**8 pessoas** com perfil `Caedu- Planejamento`.
Lista nominal em [`pessoas.md`](../../00_Institucional/_contexto/pessoas.md).
> ⚠ O perfil na origem tem **espaço a mais** (`Caedu- Planejamento`) — erro de digitação a
> corrigir na fonte.

## Produto conectado
**Gestão de Coleção** (uFlow). Módulo **Planejamento** **não** está contratado pela Caedu.

### 🟢 Onde esta área foi discutida — as 53 transcrições Tactiq

> **Varrido em 24/09/2026.** 🔴 **Isto é ROTEAMENTO, não conteúdo:** diz em que reunião
> procurar, não o que foi dito. ⚠ **A transcrição automática tem 33% das falas cortadas** —
> contagem de termo sobrevive ao ruído, narrativa não.

**17 das 53 reuniões tocam esta área.** As mais densas:

| Data | Reunião | Menções |
|---|---|---:|
| 14/05/2025 | uMode e Compras Caedu | 33 |
| 22/08/2024 | CAEDU - Treinamento Estilo | 31 |
| 05/11/2025 | Caedu Importacao weekly | 18 |
| 22/06/2026 | Caedu 2.0 | 15 |
| 24/07/2024 | Sugestões B2B CAEDU | 15 |
| 27/11/2024 | Weekly Caedu | 14 |
| 29/04/2025 | CAEDU (presencial) | 8 |
| 04/12/2024 | Weekly quinzenal CAEDU | 7 |

⚠ **Termos contados:** `planejamento` · `sortimento` · `macroplan`.

## Fontes e referências

### Documentos que esta área consome

### Procedência deste documento
| Bloco | Fonte | Data |
|---|---|---|
| Fluxo, campos, validações e dores | Notion — `Mapeamento de Contas - Caedu` (AS IS / TO BE) | 04/04/2025 |
| Pessoas e perfis de acesso | Notion — página `Caedu` em `Databases / Mapa de Clientes` | varrido 21/09/2026 |
| Módulos, ERP e dupla de atendimento | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |

⚠ **O mapeamento de conta é de abr/2025 — 17 meses.** A própria fonte já registra correções
posteriores. **Revalidar com a dupla de atendimento antes de usar como diagnóstico atual.**

### Documentos que esta área produz

`[a preencher]`

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Módulos e produto conectado | Notion — base `Mapa de Clientes` | varrido 23/09/2026 |
| Pessoas e responsáveis de área | Notion — página `Caedu`, tabela de usuários do PLM | varrido 21/09/2026 |

## Governança
### Responsável pela área
`[a preencher]` — nenhuma fonte da uMode nomeia o líder desta área na Caedu.

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Responsável na empresa cliente

`[a preencher]`

### Responsável de atendimento (uMode)

`[a preencher]`

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`.**

**Área:** `01_Planejamento` · **Cliente:** `Caedu`

**A casa deste cliente:** [institucional.md](../../00_Institucional/_contexto/institucional.md) · [jornada.md](../../00_Institucional/_contexto/jornada.md) · [pessoas.md](../../00_Institucional/_contexto/pessoas.md)

**A mesma área na Casa uMode:** ver `uMode/00_Institucional/_contexto/institucional.md`

**As outras 13 áreas deste cliente:**

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
