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
### ⚠ Dores registradas
1. **Falta de relatório unificado** que mostre, por departamento, o que está pendente. É a dor
   mais citada da área.
2. **Possível overlap** entre a visão de desenvolvimento Nacional e Importado — consequência do
   Macroplan subutilizado.
3. 🔴 **Origem vive na ficha, não na variante** — como o acompanhamento é por variante, obriga
   exportações extensas no mapa.

## Vocabulário da área
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
### Procedência deste documento
| Bloco | Fonte | Data |
|---|---|---|
| Fluxo, campos, validações e dores | Notion — `Mapeamento de Contas - Caedu` (AS IS / TO BE) | 04/04/2025 |
| Pessoas e perfis de acesso | Notion — página `Caedu` em `Databases / Mapa de Clientes` | varrido 21/09/2026 |
| Módulos, ERP e dupla de atendimento | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |

⚠ **O mapeamento de conta é de abr/2025 — 17 meses.** A própria fonte já registra correções
posteriores. **Revalidar com a dupla de atendimento antes de usar como diagnóstico atual.**

## Governança
### Responsável pela área
`[a preencher]` — nenhuma fonte da uMode nomeia o líder desta área na Caedu.

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode