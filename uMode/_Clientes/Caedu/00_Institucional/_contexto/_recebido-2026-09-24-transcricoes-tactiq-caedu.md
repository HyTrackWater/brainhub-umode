---
aliases:
  - "Recebido 24 set 2026 — as 53 transcrições Tactiq da CAEDU"
tags:
  - tipo/registro
  - cliente/caedu
  - status/ongoing
---
# Recebido 24 set 2026 — as 53 transcrições Tactiq da CAEDU

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
>
> **Fonte:** `transcricoes_caedu.zip`, entregue pelo Vinicius em 24/09/2026. **53 arquivos
> `.txt` do Tactiq**, 1,8 MB, de **25/06/2024 a 15/09/2026**.
>
> **Tratamento:** `T2` no que está aqui. ⚠ **As transcrições brutas NÃO entraram no
> repositório** — foram processadas em disco, fora dele. Nenhum trecho de valor de contrato,
> negociação ou dado pessoal foi copiado.

## 0 · 🔺 Este registro CORRIGE um negativo que eu fechei ontem

O `_varredura-2026-09-23g-participantes-das-reunioes-sao-anonimos.md` concluiu, com três vias
de verificação:

> *"presença nominal com data **NÃO sai por API**"* — 24 dos 25 uuids do campo `Participantes`
> do Notion não resolvem para nome nenhum; **99,2% das presenças ficam anônimas.**

🟢 **Aquilo continua verdadeiro para a API do Notion. E deixou de ser verdadeiro para a conta.**
A transcrição Tactiq traz exatamente o que faltava, em toda linha:

```
[00:35:34] Vanessa Rinaldi: Tá você o grupo subgrupo? Vamos pensar na hierarquia...
```

🔴 **Presença nominal, com data e com o que a pessoa disse.** ⚠ **A lição não é "eu estava
errado" — é que um negativo vale contra a FONTE testada, nunca contra o fato.**

## 1 · O que chegou, em número `[C]`

| | |
|---|---:|
| arquivos | **53** |
| datas distintas | **49** (4 datas têm 2 arquivos) |
| período | **25/06/2024 → 15/09/2026** |
| tempo gravado | **36,1 horas** |
| falas indexadas | **9.392** |
| falantes distintos | **42** |

**Por ano:** 2024: **18** · 2025: **17** · 2026: **14**.

🔴 **43 das 49 datas NÃO têm marco correspondente no `jornada.md`.** Só seis coincidem —
29/04/2025, 14/05/2025, 05/11/2025, 27/11/2025, 13/05/2026 e 03/06/2026.
🟢 **O material é complementar, não repetido.** ⚠ **E 11 marcos do corpus não têm transcrição**:
vieram da tabela de usuários, de atas e do vault.

## 2 · 🟢 A identidade: 19 dos 42 falantes resolvem para e-mail

**Feito por `scripts/resolve-falantes.py`, contra as fichas da Casa + as da Caedu.**

| Falante | Falas | Reuniões | Identidade |
|---|---:|---:|---|
| Julianne Rodrigues | **3.823** | **53 de 53** | `julianne.dias@umode.com.br` |
| Vitoria Meneghin | 1.805 | 22 | `vitoria.meneghin@caedu.com.br` |
| Marina Santoro | 603 | 12 | `marina.santoro@umode.com.br` |
| Juliana Ferré | 309 | 7 | `juliana.ferre@umode.com.br` |
| Ana Paula Ramos | 189 | 2 | `anapaula.ramos@umode.com.br` |
| Vanessa Rinaldi | 145 | 5 | `vanessa.rinaldi@umode.com.br` |
| Ronaldo Trentim | 134 | 2 | `ronaldo.trentim@caedu.com.br` |
| Elizabeth Alves | 124 | 1 | `elizabeth.alves@umode.com.br` |
| Fernanda Araujo | 103 | 4 | `fernanda.araujo@umode.com.br` |
| Victor Aragão | 87 | 3 | `victor.aragao@umode.com.br` |
| Sandro Costa · Felipe Sindeaux · Karina Gaino · Pedro Murillo · Williem Berg · Bárbara Macedo · cristiane moraes · Bergson Marques | — | — | resolvidos |

🔴 **A Julianne está em 53 de 53 reuniões.** ⚠ **É a conta inteira passando por uma pessoa** —
e ela é justamente a Key Account cuja ficha estava sem e-mail até ontem (item 599).

🟢 **`Vitoria Meneghin` é a contraparte do cliente**: 1.805 falas em 22 reuniões, a segunda
maior voz da conta.

### 2.1 · 🔺 O falso positivo que quase entrou, e a regra que nasceu dele

**Na primeira tentativa, o falante `Juliana` (2 falas) resolveu para `juliana@osklen.com.br`.**
🔴 **Pessoa de OUTRO cliente, numa reunião da CAEDU** — porque um nome de token único casou com
uma ficha de qualquer lugar do corpus.

**Três regras entraram no resolvedor por causa disso:**
1. **Escopo** — só ficha do próprio cliente e da Casa. **Nunca de cliente alheio.**
2. **Nome de um token só não resolve.** `Rose`, `Natália`, `Bruno`, `Mauricio`, `tamiris`,
   `Juliana` ficam como **apelido**, não como identidade.
3. **Casamento por token:** primeiro nome + pelo menos mais um. Foi assim que
   `Juliana Ferré` passou a resolver para `Juliana Ferré Esteves`.

## 3 · 🔴 13 pessoas falam nestas reuniões e NÃO existem no corpus

| Falante | Falas | Reuniões |
|---|---:|---:|
| **Cleiton Gomes** | **305** | **6** |
| Mariana Amaral | 124 | 3 |
| Roselene Gonçalves | 111 + 64 | 2 |
| Jonathan Lippmann | 64 | 1 |
| Oscar Cardoso | 54 | 1 |
| Raphael Caedu | 51 | 2 |
| Thiago Tadeu dos Santos Luiz | 40 | 1 |
| Rogerio Magoo · Karina Loira · Julia Rodrigues · Paulo Eduardo Devidé · Guto Blond · Douglas Luiz | ≤16 | 1–2 |

🔴 **`Cleiton Gomes` fala 305 vezes em 6 reuniões e o corpus não sabe que ele existe.**
⚠ **`Roselene` aparece com DUAS grafias** — `Roselene Goncalves` e
`Roselene Maria Temóteo Gonçalves Fanti`. **E ela já está no corpus por outro caminho:** a
demanda `D-2025-013` registra *"solicitado por: Roselene"*.

⚠ **Mais 5 aparecem só por apelido** (`Rose`, 733 falas em 7 reuniões — a terceira maior voz —
mais `tamiris`, `Natália`, `Mauricio`, `Bruno`). 🔴 **`Rose` pode ou não ser a `Roselene`.
Não decidi.**

## 4 · 🔴 A HIERARQUIA DE PRODUTO DA CAEDU — a pergunta que estava em aberto

**O corpus registrava como decisão pendente:** *"`Griffe › Linha › Grupo › Subgrupo` são 4 eixos
independentes ou uma cascata?"* 🟢 **A transcrição de 14/05/2025 responde, pela boca da própria
CAEDU.**

**`Linha` é o topo, e quem diz é a Vitoria Meneghin:**
> **Vanessa Rinaldi:** *"Vamos pensar na hierarquia de produtos de vocês, ele começa **a linha é
> o primeiro** para vocês."*
> **Vitoria Meneghin:** *"**A linha é o primeiro**, a linha grupo."*

**O exemplo que elas constroem:**
> **Vanessa:** *"A linha `Promocional`, o grupo é `Mesa`, e o subgrupo?"*

🔴 **E aqui está o problema que nenhuma tabela mostraria — o MESMO item muda de classificação
conforme a linha:**
> **Vitoria:** *"dentro do `promocional`, ele é uma **mesa**, mas dentro do `jovem`, dentro do
> `adulto`, ele é **top**."*

⚠ **`Grupo` e `Subgrupo` são sempre pareados:**
> **Vitoria:** *"num campo subgrupo, no outro — **os dois são juntos, sempre casadinho**."*

⚠ **E `Feminino / Masculino / Infantil` é OUTRA dimensão**, que a Vanessa teve de perguntar
onde entrava: *"pensando no cadastro total, **onde estão as estruturas de feminino e masculino e
infantil**?"*

**Volume:** *"tem **1195 grupo/sub** cadastrados"* — ⚠ **dito por falante não identificado
(`Speaker`), não confirmado.**

### 4.1 · 🔴 A consequência técnica, e ela é de modelo de dado

**O campo do uFlow que recebe isso é o `Product Type`:**
> **Julianne:** *"nosso `produto Type` como grupo subgrupo. Acho que de vocês é `tipo`, né?"*

🔴 **E ele é PLANO:**
> **Julianne:** *"aquele campo de `produto Type`, ele **não pode ter hierarquias depois dele**."*

**O que a CAEDU pede é filtro em cascata, e hoje não existe:**
> **Julianne:** *"Quando colocar a grife x e a linha tal, o campo grupo subgrupo **aparecesse
> essa listagem**?"*

**E a dor é antiga:**
> **Julianne:** *"eu vejo que isso é uma dor para eles **desde meados do ano passado**."*
> **Vitoria:** *"metade do problema foi grupo subgrupo que **não estava na listagem** e foi
> criado. E a outra metade foi grupo subgrupo que [já existia]."*

🟢 **Isso conecta direto com a dor estrutural nº 5 já registrada no `institucional.md`** — *"a
origem do produto vive na ficha, não na variante (...) **é problema de modelo de dado, não de
processo**"*. **São a mesma família de defeito.**

## 5 · Onde está o resto do material `[C]`

**Menções por tema, nas 53 transcrições:**

| Tema | Menções | Reunião mais densa |
|---|---:|---|
| **fornecedores** — a frente aberta | **506** | `2025-11-05_Caedu_Importacao_weekly` (67) |
| **planilha** — dado fora do uMode | **367** | `2025-05-14_uMode_e_Compras` (35) |
| importado / importação | 323 | `2025-05-14_uMode_e_Compras` (23) |
| Linx / integração | 229 | `2024-07-15_uMode_Caedu_Bi-Weekly` (36) |
| hierarquia grupo/subgrupo | 101 | `2025-10-21_Weekly` (11) |
| treinamento | 84 | `2024-07-24_Sugestoes_B2B` (16) |
| modelagem / piloto / fitting | 42 | `2025-11-27_CAEDU_Acompanhamento_PLM` (9) |
| e-commerce / SEO | 42 | `2025-04-22_Alinhamento` (10) |
| CAEDU 2.0 | 14 | `2024-11-27_Weekly` (6) |
| Macroplan | 9 | — |
| time de calçados | 6 | — |
| Merchandising | 4 | — |

🔴 **`fornecedores` com 506 menções é a veia mais rica, e é exatamente `A frente aberta` da
conta.** ⚠ **Ainda não foi lida.**

## 6 · O que fica como decisão

| # | Pergunta | Para quem |
|---|---|---|
| 1 | 🔴 **`Rose` (733 falas) é a `Roselene`?** Se for, é a 3ª maior voz da conta e tem ficha a criar | Atendimento |
| 2 | 🔴 **Quem é `Cleiton Gomes`** (305 falas, 6 reuniões) e por que não está no corpus? | Atendimento |
| 3 | 🔴 **O `Product Type` plano é limitação a aceitar ou item de especificação?** A CAEDU pede cascata desde meados de 2024 | Vinicius / Produto |
| 4 | ⚠ **Os 4 apelidos restantes** — `tamiris`, `Natália`, `Mauricio`, `Bruno` — são de quem? | Atendimento |
| 5 | ⚠ **As transcrições brutas ficam onde?** Não entraram no repositório. **Drive compartilhado?** | Vinicius |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — foto com data. Correção vira registro novo.
