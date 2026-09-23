---
aliases:
  - "Comercial e Vendas · Contexto de área — Caedu"
tags:
  - tipo/area
  - cliente/caedu
  - status/ongoing
  - area/comercial-vendas
---
# Comercial e Vendas · Contexto de área — Caedu

> Criado em **21 set 2026**. ⚠ **Esta área não tem conteúdo em nenhuma fonte varrida.**
>
> O arquivo existe para que a lacuna seja **visível e endereçável**, não para simular cobertura.
> **Nada aqui foi inferido.**

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- produto-conectado: Integração — [base Mapa de Clientes · 2026-09-21]
- pessoas-da-area: ? — [não consta em: página Caedu, tabela de usuários do PLM · 2026-09-21]
- responsavel-area: ? — [não consta em: página Caedu, tabela de usuários do PLM · 2026-09-21]

## O que esta área faz

🔴 **O dado comercial da Caedu vive FORA do uMode, por decisão, e isso está registrado como dor.**

> *"**Sensibilidade de Dados** (parte de negociação e pedido) está fora da uMode."* — § 4.4, dor 2
> *"Parte da negociação de pedidos é feita em **planilhas sensíveis**."* — § 4.2.3

⚠ **O que chega à plataforma é a emissão do pedido, não a negociação:**

> *"Integração com **Linx** para geração de pedidos e controle de estoque."* — § 2.1

**Fonte de tudo acima:** `Mapeamento de Contas - Caedu` (AS IS / TO BE), 04/04/2025.

## Com quem se relaciona (interno e externo)

- **`03_Desenvolvimento-de-Colecao`** — recebe o produto liberado; a validação *"Liberado para emissão"* é o ponto de passagem (§ 4.2.5).
- **Linx (ERP)** — é por onde o pedido é gerado e o estoque controlado (§ 2.1).
- ⚠ **Planilhas externas** — onde a negociação acontece hoje. **Não é sistema mapeado.**

## Entregas e responsabilidades
`[a preencher]`

## Padrões operacionais

### Como trabalham

`[a preencher]`

### O que não fazem

- **Não negociam dentro do uMode.** A negociação e o dado sensível de pedido estão em planilhas externas — e há ação aberta no roadmap para reavaliar isso (§ 5.2, *Segurança de Dados — rever permissão de pedidos*, responsável **Time Caedu + uMode**, prazo previsto de **6 semanas**, contado de 04/04/2025).

## Vocabulário da área

### Termos específicos

`[a preencher]`

## Pessoas desta área
`[a preencher]` — **não existe perfil de acesso correspondente** na conta Caedu do PLM.
Os perfis existentes são: Estilo, Produto, Planejamento, Modelagem, Qualidade, E-commerce,
Gerentes, Geral e Admin.

## Produto conectado

**`Integração`** (uFlow) — módulo contratado pela Caedu. É o que liga a liberação do produto à emissão de pedido no **Linx**.

⚠ **Não há módulo que cubra negociação comercial** — e isso é escopo declarado, não falha.

## Fontes e referências

### Documentos que esta área consome

`[a preencher]`

### Documentos que esta área produz

`[a preencher]`

### Procedência deste documento
| Bloco | Fonte | Data |
|---|---|---|
| O que a área faz, relações, o que não fazem | Notion — `Mapeamento de Contas - Caedu` (AS IS / TO BE) | 04/04/2025 |
| Módulos e produto conectado | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |
| Ausência de perfil de acesso e de pessoas | Notion — página `Caedu`, tabela de usuários do PLM | varrido 21/09/2026 |

⚠ **O mapeamento de conta é de abr/2025 — tem 17 meses.** Revalidar com a dupla de atendimento
antes de usar como diagnóstico atual.

### Fontes varridas e o que cada uma não trouxe
| Fonte | Resultado |
|---|---|
| Notion — página `Caedu` em `Databases / Mapa de Clientes` | sem perfil de acesso para esta área |
| Notion — `Mapeamento de Contas - Caedu` | 🔴 **excluída do escopo POR DECISÃO** (§ 2.2, *dados de pedidos sensíveis*) — **mas há dor e ação registradas** (§ 4.4 e § 5.2) |
| Notion — base `Mapa de Clientes` | sem campo correspondente |
| vault do João — pasta `caedu` | proposta e cronograma, sem detalhe de área |

### O que levar ao negócio
1. Esta área **existe na Caedu**? Se não existir, registrar a ausência como fato do cliente.
2. Se existir, **quem responde por ela** e ela interage com a uMode?
3. Se não interage com o PLM hoje, **deveria**?

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Pessoas e responsáveis de área | Notion — página `Caedu`, tabela de usuários do PLM | varrido 21/09/2026 |

## Governança
### Responsável pela área
`[a preencher]`

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Responsável na empresa cliente

`[a preencher]`

### Responsável de atendimento (uMode)

`[a preencher]`

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`.**

**Área:** `09_Comercial-Vendas` · **Cliente:** `Caedu`

**A casa deste cliente:** [institucional.md](../../00_Institucional/_contexto/institucional.md) · [jornada.md](../../00_Institucional/_contexto/jornada.md) · [pessoas.md](../../00_Institucional/_contexto/pessoas.md)

**A mesma área na Casa uMode:** ver `uMode/00_Institucional/_contexto/institucional.md`

**As outras 13 áreas deste cliente:**

- [Planejamento](../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../02_Estilo-Criacao/_contexto/contexto-area.md)
- [Desenvolvimento de Colecao](../../03_Desenvolvimento-de-Colecao/_contexto/contexto-area.md)
- [Qualidade](../../04_Qualidade/_contexto/contexto-area.md)
- [PCP](../../05_PCP/_contexto/contexto-area.md)
- [Compras Supply Sourcing](../../06_Compras-Supply-Sourcing/_contexto/contexto-area.md)
- [Logistica CD](../../07_Logistica-CD/_contexto/contexto-area.md)
- [Ecommerce Cadastro](../../08_Ecommerce-Cadastro/_contexto/contexto-area.md)
- [Marketing](../../10_Marketing/_contexto/contexto-area.md)
- [Financeiro](../../11_Financeiro/_contexto/contexto-area.md)
- [Design](../../12_Design/_contexto/contexto-area.md)
- [Modelagem](../../13_Modelagem/_contexto/contexto-area.md)
- [Engenharia](../../14_Engenharia/_contexto/contexto-area.md)
