---
aliases:
  - "Varredura 23 set 2026 — a hierarquia que a CAEDU pede não é árvore nos dados dela"
---
# Varredura 23 set 2026 — a hierarquia que a CAEDU pede não é árvore nos dados dela

> **Classe: `REGISTRO`.** Evidência datada de uma varredura. 🔴 **Não é autoridade e não se
> edita.** Se algum achado daqui deve virar regra, vira parágrafo numa `AUTORIDADE` — este
> arquivo fica como prova.
>
> **Fonte:** `Extração Caedu - 28ago26.json` — 28 MB, **48.551 linhas**, em
> `C:\Users\Vinicius\Downloads`. Extração de produto × variante da conta CAEDU,
> **datada de 28/08/2026**, com os campos do uFlow e os campos espelhados do Linx.
>
> **Tratamento:** `T2`. São dados de **taxonomia e catálogo** — não há preço, custo, margem,
> CPF, telefone nem credencial entre os 17 campos. **Nenhum valor comercial foi copiado.**

## 0 · Declaração de completude — o que este registro NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não diz se a árvore existe em outro lugar** | esta é uma **exportação achatada**. Ausência de aninhamento aqui **não prova** ausência de estrutura no sistema de origem — prova que **esta exportação não a carrega** |
| 2 | **Não cobre a integração em si** | os campos `(Linx)` estão presentes, mas o **mecanismo** que os traz está em `Como é o processo de integração?`, no Notion — **não varrido** |
| 3 | **Não tem a data de corte confiável** | `Alterado em` vem como texto `dd/mm/aaaa`; ordenar como texto dá janela errada. **Não afirmo período** |
| 4 | **Não foi cruzado com a página da CAEDU no Notion** | 🔴 **o conector de Notion desta sessão não alcança o workspace da uMode** (§ 4) |
| 5 | **Não abri** `Caedu - Query da API.xlsx` nem `caedu_mega_line_reports-2026-02-06` | estão no mesmo `Downloads`, ainda fechados |

## 1 · O que a extração é `[C]`

| | Número |
|---|---:|
| Linhas (produto × variante) | **48.551** |
| Produtos distintos (`ID`) | **42.488** |
| Campos | **17** |

**Preenchimento dos quatro campos da dor — todos praticamente completos `[C]`:**

| Campo | Origem | Preenchido | Valores distintos |
|---|---|---:|---:|
| `Griffe Linx` | **Linx** | 99,9% | **12** |
| `Linha (Linx)` | **Linx** | 99,9% | **34** |
| `Grupo` | **uFlow** | 100% | **84** |
| `Subgrupo` | **uFlow** | 100% | **231** |

🔴 **Primeiro fato que muda o enquadramento:** **`Griffe` e `Linha` são campos do Linx; `Grupo` e
`Subgrupo` são do uFlow.** A hierarquia que a CAEDU pede **atravessa dois sistemas** — dois níveis
vêm do ERP e dois da plataforma. **Isso é coerente com a leitura que já estava no corpus de que a
dor dela é de integração**, e dá a ela um mecanismo concreto.

## 2 · 🔴 O achado principal: não é árvore, é matriz esparsa `[C]`

**Testei se cada filho tem um pai único. Nenhum dos quatro níveis passa.**

| Relação testada | Filhos | Filhos com **mais de um pai** | Veredito |
|---|---:|---:|---|
| `Linha` dentro de `Griffe` | 33 | **23** | 🔴 não é árvore |
| `Subgrupo` dentro de `Grupo` | 231 | **75** | 🔴 não é árvore |
| `Grupo` dentro de `Griffe` | 82 | **26** | 🔴 não é árvore |
| `Grupo` dentro de `Linha` | 82 | **49** | 🔴 não é árvore |

**Exemplos concretos `[C]`:**

- **`FEMININO` é uma `Linha` que aparece sob 7 `Griffe` diferentes** — ACESSORIOS, CALCADOS,
  FEMININO, INTIMA E PRAIA, JEANS, LINGERIE, OFERTA RELAMPAGO.
- **`COMPLEMENTO` é um `Subgrupo` que aparece em 7 `Grupo`** — BEBE, CARNAVAL, COMPLEMENTO,
  ESCRITÓRIO, INVERNO, LINHA PRAIA, PET.
- **`BOTTOM` é um `Grupo` que aparece sob 24 `Linha`.**

**A densidade confirma:**

| Combinação | Existem de fato | Cartesiano seria |
|---|---:|---:|
| `Griffe × Linha` | **99** | 455 |
| `Grupo × Subgrupo` | **350** | 19.404 |
| **`Griffe × Linha × Grupo × Subgrupo`** | **1.015** | **8.828.820** |

**1.015 combinações reais em 8,8 milhões possíveis — 0,01% de densidade.**

### 2.1 · `[P]` O que eu leio disso — e é interpretação, não fato

**`Griffe › Linha › Grupo › Subgrupo` se comporta como classificação por facetas, não como
caminho hierárquico.** Um produto é classificado em quatro eixos independentes que se combinam
de forma esparsa; ele não *desce* por uma árvore.

🔴 **Por que isso importa antes de desenhar qualquer coisa:** desenhar como árvore encadeada
(escolher a Griffe restringe as Linhas, que restringem os Grupos) **contradiz os dados reais da
conta**. Em 24 dos casos o mesmo `Grupo` aparece sob `Linha` diferentes — um seletor em cascata
mostraria o mesmo item em dezenas de caminhos ou o esconderia no caminho errado.

⚠ **E isso levanta uma dúvida sobre o precedente da Loungerie**, que já está registrado no corpus
como desenho de 4 níveis com exemplos: **ou o modelo dela é diferente do da CAEDU, ou ele descreve
uma intenção que os dados da CAEDU não sustentam.** **Não abri a página da Loungerie nesta
sessão — não afirmo qual dos dois.**

## 3 · 🔴 Qualidade de dado — o que vai quebrar relatório `[C]`

**1 · `Coleção` tem duplicata por acentuação.** 55 valores distintos, e entre eles:

| Grafia | Linhas |
|---|---:|
| `VERÃO 26/27` | 4.971 |
| `VERAO 26/27` | **1.690** |
| `VERÃO 25/26` | 4.189 |
| `VERAO 25/26` | **2.241** |

🔴 **São duas coleções na base para uma coleção no mundo.** Qualquer contagem por coleção erra
em ~25% nessas duas — e `Coleção` é campo de uFlow, não do Linx.

**2 · `Griffe Linx` tem lixo de cadastro:** ao lado de INFANTIL (14.252) e FEMININO (10.202),
existem **`O`, `F` e `M` com 1 registro cada**, e **`LINGERIE` (17) convivendo com
`INTIMA E PRAIA` (5.293)**.

**3 · `Linha (Linx)` idem:** `66` e `63` como valores, e **`INFANTIL` (27) ao lado de
`INFANTIL NAS` (2.759) e `INFANTIL NOS` (2.452)**.

**4 · Cobertura de variante é parcial:** `SKU` preenchido em **47,8%**, `ID da variant` e
`Cor` em **65,6%**. **16.717 linhas não têm status de variante.** ⚠ **Não sei se é produto sem
variante cadastrada ou variante não exportada** — são leituras diferentes e a extração não
distingue.

**5 · `Status do Produto`:** Finalizado 22.854 · Backlog 16.463 · Desenvolvimento 7.380 ·
Cancelado 1.760 · Stand By 78 · Revisão 16. **`Backlog` é 34% da base.**

## 4 · 🔴 O bloqueio desta varredura

**O conector de Notion desta sessão não alcança o workspace da uMode.** `get-teams` devolve
**um único teamspace, `Vinícius Risoléo`** (a conta pessoal), e uma busca por `Caedu` devolve
**zero resultados**.

⚠ **Não afirmo que o conteúdo sumiu** — as sessões de 22 e 23 set 2026 leram esse workspace sem
problema. **Afirmo que não o alcanço por este conector, nesta sessão.** É troca de conta
autenticada, e **quem reconecta é o Vinicius**.

**O que ficou parado por causa disso:** `Setup - PLM / CLIENTES / CAEDU`, as **54 sub-páginas**
ainda fechadas da página da CAEDU, e o `Mapeamento da Conta - Caedu`.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — foto com data. Correção vira registro novo.
