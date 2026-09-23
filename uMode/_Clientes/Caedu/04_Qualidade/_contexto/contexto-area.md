---
aliases:
  - "Qualidade · Contexto de área — Caedu"
tags:
  - tipo/area
  - cliente/caedu
  - status/ongoing
  - area/qualidade
---
# Qualidade · Contexto de área — Caedu

> Criado em **21 set 2026** por varredura do Notion ao vivo. Campo sem fonte fica `[a preencher]`.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- produto-conectado: Gestão de Coleção — [base Mapa de Clientes · 2026-09-21]
- pessoas-da-area: 2 pessoas com perfil Caedu-Qualidade — [página Caedu em Databases / Mapa de Clientes · 2026-09-21]
- responsavel-area: ? — [não consta em: página Caedu em Databases / Mapa de Clientes · 2026-09-21]
- entrega: Recebimento da amostra · Amostra recebida — [Mapeamento de Contas - Caedu · 2025-04-04]
- entrega: Decisão de qualidade · Amostra aprovada — [Mapeamento de Contas - Caedu · 2025-04-04]
- dor: Frequência de exportações manuais e planilhas paralelas — é a dor declarada da área — [Mapeamento de Contas - Caedu · 2025-04-04]

## O que esta área faz
Controla as **amostras de produção**: recebe, avalia e aprova ou reprova antes do envio às lojas.
É o último portão do fluxo nacional.

Internamente, a aprovação final é chamada de **"lacrar"** o produto.

## Com quem se relaciona (interno e externo)
- **Recebe de** `13_Modelagem` — produto com piloto aprovado
- **Libera para** `07_Logistica-CD` / envio às lojas

## Entregas e responsabilidades
| Entrega | Campo que a registra |
|---|---|
| Recebimento da amostra | `Amostra recebida` |
| Decisão de qualidade | `Amostra aprovada` |

## Padrões operacionais

### Como trabalham

### ⚠ Dores registradas
1. **Frequência de exportações manuais e planilhas paralelas** — é a dor declarada da área.

### O que sabemos do engajamento
O mapeamento de conta registra que **modelagem e qualidade têm domínio da ferramenta**, enquanto
os demais times ainda têm dificuldade com alguns processos.
> Fonte: campo `Onde Estamos` da base `Mapa de Clientes`.

### O que não fazem

`[a preencher]`

## Vocabulário da área

### Termos específicos

| Termo | O que significa aqui |
|---|---|
| **Lacrar** | aprovação final da amostra de produção |
| **Amostra de controle** | amostra avaliada antes da liberação para loja |

## Pessoas desta área
**2 pessoas** com perfil `Caedu-Qualidade`.
Lista nominal em [`pessoas.md`](../../00_Institucional/_contexto/pessoas.md).
> ⚠ **Duas pessoas para o último portão de qualidade de uma operação de 100+ lojas.**
> Vale confirmar se o número reflete a realidade ou se há gente atuando por outro perfil.

## Produto conectado
**Gestão de Coleção** (uFlow).

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

**Área:** `04_Qualidade` · **Cliente:** `Caedu`

**A casa deste cliente:** [institucional.md](../../00_Institucional/_contexto/institucional.md) · [jornada.md](../../00_Institucional/_contexto/jornada.md) · [pessoas.md](../../00_Institucional/_contexto/pessoas.md)

**A mesma área na Casa uMode:** ver `uMode/00_Institucional/_contexto/institucional.md`

**As outras 13 áreas deste cliente:**

- [Planejamento](../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../02_Estilo-Criacao/_contexto/contexto-area.md)
- [Desenvolvimento de Colecao](../../03_Desenvolvimento-de-Colecao/_contexto/contexto-area.md)
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
