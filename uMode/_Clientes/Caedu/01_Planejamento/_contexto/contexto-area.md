# Planejamento · Contexto de área — Caedu

> Criado em **21 set 2026** por varredura do Notion ao vivo. Campo sem fonte fica `[a preencher]`.

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

**As outras 14 áreas deste cliente:**

- [Institucional](../../00_Institucional/_contexto/contexto-area.md)
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
