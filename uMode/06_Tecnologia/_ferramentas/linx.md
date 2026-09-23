---
aliases:
  - "Linx · Ferramenta"
tags:
  - tipo/ferramenta
  - casa
---
# Linx · Ferramenta

> **Ficha gerada por `scripts/gera-fichas-ferramenta.py` em 22 set 2026.**
> **O nome está exatamente como o enum da fonte o escreve.** Grafias parecidas **não
> foram fundidas** — mesma regra do `protocolo-varredura-cliente.md` § 9.
> Campo sem fonte fica `[a preencher]` — **nada foi inferido.**

## Identificação
### Nome na fonte
**`Linx`**
### Natureza
**Sistema de terceiro** — ERP/integração do cliente. 🔴 **Não é produto da uMode.**
### Fornecedor
Linx
### Observação de taxonomia
o ERP mais frequente da carteira

## Adoção
### Quantos clientes
**12** de 49 clientes do corpus
### Quais clientes
| Cliente | `Status` na base | Valor literal do campo |
|---|---|---|
| [Arezzo](../../_Clientes/Arezzo/00_Institucional/_contexto/institucional.md) | `Pré Onboardings` | `SAP e Linx` |
| [Caedu](../../_Clientes/Caedu/00_Institucional/_contexto/institucional.md) | `Onboarding` | `Linx` |
| [Lenny Niemeyer](../../_Clientes/Lenny Niemeyer/00_Institucional/_contexto/institucional.md) | `Churn` | `Linx` |
| [Lofty Style](../../_Clientes/Lofty Style/00_Institucional/_contexto/institucional.md) | `Ongoing` | `Linx` |
| [Loungerie](../../_Clientes/Loungerie/00_Institucional/_contexto/institucional.md) | `Onboarding` | `Linx` |
| [NK STORE](../../_Clientes/NK STORE/00_Institucional/_contexto/institucional.md) | `Ongoing` | `Linx` |
| [NV](../../_Clientes/NV/00_Institucional/_contexto/institucional.md) | `Ongoing` | `Linx` |
| [Oficina Reserva](../../_Clientes/Oficina Reserva/00_Institucional/_contexto/institucional.md) | `Ongoing` | `SAP e Linx` |
| [Osklen](../../_Clientes/Osklen/00_Institucional/_contexto/institucional.md) | `Operação Assistida` | `Linx` |
| [Puket](../../_Clientes/Puket/00_Institucional/_contexto/institucional.md) | `Ongoing` | `Linx / SAP` |
| [Reserva](../../_Clientes/Reserva/00_Institucional/_contexto/institucional.md) | `Ongoing` | `Linx / SAP` |
| [VIX](../../_Clientes/VIX/00_Institucional/_contexto/institucional.md) | `Ongoing` | `Linx` |

> ⚠ **Isto é o que o campo declara, não o que está em uso.** O campo `Status` da
> mesma base já se contradisse por sete caminhos independentes — ver
> [`_taxonomia-status-cliente.md`](../../00_Institucional/_contexto/_taxonomia-status-cliente.md).

## Relações
### Solução do portfólio correspondente
⚠ **não se aplica** — é sistema de terceiro

O que conversa com ele é o módulo [`Integração`](../../03_Produto-e-Solucoes/_ferramentas/integracao.md).
### Áreas que usam
`[a preencher]` — 🔴 **nenhuma fonte varrida liga ferramenta a área.**
### Demandas e RFIs que a citam
`[a preencher]` — 🔴 **o campo não existe na base de demandas nem na de RFIs.**

### ⚠ Vínculo por valor composto
Parte dos clientes acima chega aqui por um valor **composto** do campo — `Linx / SAP` · `SAP e Linx`.
**Não desmembrei o valor em dois vínculos:** a fonte não diz se o cliente usa os
dois sistemas ou um para cada coisa. E as grafias `Linx / SAP` e `SAP e Linx`
🔴 **são o mesmo conceito escrito de dois jeitos** — defeito já registrado.

## Governança
### Quem pode alterar este documento
Liderança de Produto e Soluções. **A lista de clientes é gerada por script** —
corrigir na fonte, não aqui.

## Fontes e referências
### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Identificação · Adoção | Notion - base `Mapa de Clientes`, `collection://ec041afd-...`, via SQL | **22 set 2026** |

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Natureza:** sistema de terceiro (ERP/integração do cliente).

**As outras ferramentas desta classe:** [índice](_indice.md)

**Área da Casa que guarda esta ficha:** [Tecnologia](../_contexto/contexto-area.md)

**Institucional da Casa:** [institucional.md](../../00_Institucional/_contexto/institucional.md)
