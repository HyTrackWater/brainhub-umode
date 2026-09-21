# Estilo e Criação · Contexto de área — Caedu

> Criado em **21 set 2026**. **Primeiro `contexto-area.md` de cliente do BrainHub** — serve de
> modelo para as outras 13 áreas da Caedu e para os demais clientes.
>
> **Procedência de cada bloco está declarada no fim.** Campo sem fonte fica `[a preencher]` —
> nada foi inferido.

## O que esta área faz
Aprova produtos e libera a ficha para e-commerce. É a área que decide se o produto segue no fluxo:
a validação **`Aprovado pré-line = SIM`** é a porta de entrada de todo o desenvolvimento.

É também aqui que se define a **origem do produto** — e essa decisão bifurca o fluxo inteiro:
- `Origem = Nacional` → segue para Modelagem e Produto Nacional
- `Origem = Importado` → segue para o fluxo de Importação

Preenche na ficha: localização de loja, licenciamento, descrição de e-commerce, cor e variação,
e atributos de Visual Merchandising.

## Com quem se relaciona (interno e externo)
- **Recebe de** `01_Planejamento` — a planilha base com sortimento, faixa de preço e campos
  obrigatórios iniciais (Nome, Linha, Origem, Departamento).
- **Entrega para** `13_Modelagem` (quando nacional) e para o fluxo de importação (quando importado).
- **Alimenta** `08_Ecommerce-Cadastro` — SEO, título, imagens e atributos de VM saem daqui.
- **Na uMode:** dupla de atendimento **Julianne & Pedro**.

## Entregas e responsabilidades
| Entrega | Validação que a controla |
|---|---|
| Aprovação de produto | `Aprovado pré-line = SIM` |
| Definição de origem | `Origem = Nacional` \| `Importado` |
| Ficha liberada para e-commerce | campos de SEO, título e imagem preenchidos |
| Atributos de licenciamento | campo de licenciamento na ficha |
| Atributos de Visual Merchandising | campos de VM |

## Padrões operacionais
### Como trabalhamos
- O produto só avança com a aprovação pré-line explícita.
- A origem é registrada **na ficha de produto**, não na variante.

### O que não fazemos
- Não se decide negociação nem pedido nesta área — isso está fora da uMode, em planilhas
  sensíveis do cliente.

### ⚠ Dores registradas no mapeamento de conta
1. **Visual merchandising é subexplorado** — os campos existem e não são usados com disciplina.
2. **Macros de cor pouco usadas.**
3. 🔴 **A origem vive na ficha, não na variante.** Como a validação acontece por variante, isso
   obriga **exportações extensas no mapa** para acompanhar. É um problema de modelo de dado, não
   de processo — e foi o achado mais citado do diagnóstico.

## Vocabulário da área
### Termos específicos
| Termo | O que significa aqui |
|---|---|
| **Pré-line** | aprovação que libera o produto a seguir no fluxo |
| **Origem** | Nacional ou Importado — bifurca o fluxo inteiro |
| **VM** | Visual Merchandising — atributos de exposição em loja |
| **Licenciamento** | marca/personagem licenciado no produto; crítico para e-commerce |
| **Repeat** | produto que se repete de coleção anterior |

## Pessoas desta área
**31 pessoas** com perfil `Caedu-Estilo`, mais **5** com `Gerente de Estilo / Caedu-Estilo` —
**36 no total**, a maior concentração de usuários da conta.

A lista nominal com e-mail e data de ativação está em
[`pessoas.md`](../../00_Institucional/_contexto/pessoas.md), agrupada por perfil de acesso.

> **O perfil de acesso no PLM é o que liga pessoa a área.** Não há outro vínculo pessoa↔área em
> nenhuma fonte da uMode hoje.

## Produto conectado
**Gestão de Coleção** (uFlow) — módulo contratado pela Caedu.
Demais módulos da conta: Integração, Relatórios, Fornecedores.
ERP integrado: **Linx**.

## Fontes e referências
### Documentos que esta área consome
- Planilha base de sortimento vinda de `01_Planejamento`

### Documentos que esta área produz
- Ficha de produto aprovada, com campos de e-commerce e VM

### Procedência deste documento
| Bloco | Fonte | Data |
|---|---|---|
| Fluxo, validações, campos e dores | Notion — `Mapeamento de Contas - Caedu` (AS IS / TO BE), em `Operação de Clientes / Área de CX / Documentação CX` | 04/04/2025 |
| Contagem e nomes das pessoas | Notion — página `Caedu` em `Databases / Mapa de Clientes`, tabela de usuários do PLM | varrido 21/09/2026 |
| Módulos, ERP e dupla | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |

⚠ **O mapeamento de conta é de abr/2025 — tem 17 meses.** Duas correções já foram anotadas na
própria fonte (o Kanban foi simplificado desde então). **Revalidar o AS IS com a dupla de
atendimento antes de usar como diagnóstico atual.**

## Governança
### Responsável pela área
`[a preencher]` — o mapeamento de conta não nomeia o líder de Estilo da Caedu.
Há 5 usuários com perfil `Gerente de Estilo`; **confirmar qual responde pela área.**

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode
