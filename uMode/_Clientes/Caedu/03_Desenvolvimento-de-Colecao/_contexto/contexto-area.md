# Desenvolvimento de Coleção · Contexto de área — Caedu

> Criado em **21 set 2026** por varredura do Notion ao vivo. Campo sem fonte fica `[a preencher]`.

## O que esta área faz
Conduz o produto da aprovação de Estilo até a **liberação para emissão de pedido**. O fluxo
**bifurca pela origem** definida em Estilo:

- **Produto Nacional** → passa por `13_Modelagem` e `04_Qualidade` antes de liberar
- **Produto Importado** → preenche propriedades e tabela de medidas, e vai direto à integração

## Com quem se relaciona (interno e externo)
- **Recebe de** `02_Estilo-Criacao` — produtos com `Aprovado pré-line = SIM` e origem definida
- **Passa por** `13_Modelagem` e `04_Qualidade` no caminho nacional
- **Entrega para** o ERP **Linx**, via integração, na emissão do pedido
- **Depende de** `06_Compras-Supply-Sourcing` para o cadastro de fornecedor

## Entregas e responsabilidades
| Entrega | Validação que a controla |
|---|---|
| Produto liberado para pedido | `Liberado para emissão` |
| Envio ao ERP | `Integração Linx` |
| Propriedades do importado | `Produto repeat ou com tabela?` |

## Padrões operacionais

### Como trabalham

### ⚠ Dores registradas
1. **Falta de relatório unificado** que mostre, por departamento, o que está pendente. É a dor
   mais citada da área.
2. **Possível overlap** entre a visão de desenvolvimento Nacional e Importado — consequência do
   Macroplan subutilizado.
3. 🔴 **Origem vive na ficha, não na variante** — como o acompanhamento é por variante, obriga
   exportações extensas no mapa.

### O que não fazem

`[a preencher]`

## Vocabulário da área

### Termos específicos

| Termo | O que significa aqui |
|---|---|
| **Liberado para emissão** | validação que autoriza gerar o pedido |
| **Repeat** | produto que se repete de coleção anterior |
| **NAC / IMP** | abreviação de Nacional e Importado |

## Pessoas desta área
**22 pessoas** com perfil `Caedu-Produto` — a segunda maior concentração da conta.
Lista nominal em [`pessoas.md`](../../00_Institucional/_contexto/pessoas.md).

## Produto conectado
**Gestão de Coleção** + **Integração** (uFlow). ERP: **Linx**.

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

**Área:** `03_Desenvolvimento-de-Colecao` · **Cliente:** `Caedu`

**A casa deste cliente:** [institucional.md](../../00_Institucional/_contexto/institucional.md) · [jornada.md](../../00_Institucional/_contexto/jornada.md) · [pessoas.md](../../00_Institucional/_contexto/pessoas.md)

**A mesma área na Casa uMode:** ver `uMode/00_Institucional/_contexto/institucional.md`

**As outras 13 áreas deste cliente:**

- [Planejamento](../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../02_Estilo-Criacao/_contexto/contexto-area.md)
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
