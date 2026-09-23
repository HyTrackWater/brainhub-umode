# Recebido 23 set 2026 — as receitas fora do PLM: EducAI, Imersão IA, RFIs

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
>
> **Fonte:** lista `Serviço; Cliente` entregue pelo Vinicius em 23/09/2026, como complemento à
> base de contratos da Flávia Campello. **26 linhas, 4 serviços.**
>
> **Tratamento:** `T2`. A lista não traz valor, prazo nem condição comercial — só o par
> serviço × cliente. **Nada de faturamento foi copiado.**

## 0 · Declaração de completude — o que este registro NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não sei o que é `Imersão IA` nem `Outros serviços`** | a lista dá o nome e o cliente, nada mais |
| 2 | **Não sei se `EducAI` é o mesmo que "mentoria"** | há forte indício (§ 2), **não é confirmação** |
| 3 | **Não criei casa para nenhum dos 18 clientes novos** | **criar cliente é decisão**, não consequência de aparecer numa lista |
| 4 | **Não sei o período de nenhuma dessas receitas** | a lista não tem data |
| 5 | **`PEDRO ALEXANDRE MACHADO COSTA (BASIC)`** | o `(BASIC)` sugere ligação com `Básico&Co`, que está no corpus. **Não afirmo que seja** |

## 1 · O que a lista traz `[C]`

| Serviço | Linhas | Já existem no corpus | **Não existem** |
|---|---:|---:|---:|
| **Imersão IA** | 13 | 0 | **13** |
| **EducAI** | 5 | 1 (Cambos) | **4** |
| **RFIs** | 7 | **7** | 0 |
| **Outros serviços** | 1 | 0 | **1** (ARAMIS) |
| | **26** | 8 | **18** |

🔴 **São mais quatro serviços, e nenhum deles é software de PLM.** Somados aos 11 da base de
contratos, o Financeiro fatura **15 coisas diferentes** — e o corpus modela **7 módulos** e
**16 Soluções**. **Nenhuma das três listas cobre as outras.**

## 2 · 🟢 `EducAI` fecha o gap de mentoria (item 512)

O item 512 registrou: *"há uma operação de mentoria com CRM próprio e acervo próprio, e ela não
aparece na base de contratos"*. As evidências eram o teamspace
`AGENTES E PROJETOS / **Projeto: Mentoria (João Risoléo)**`, a `Metodologia MBS`, a menção a
*"um CRM de mentoria"* no `protocolo-varredura-cliente.md`, e a página
`Projeto: Mentoria / **CRM — EducAI**` achada na busca de 23 set.

🟢 **A linha de receita existe e se chama `EducAI`.** Cinco clientes:

| Cliente | No corpus? |
|---|---|
| MAGAZINE LUIZA (NETSHOES) | 🔴 não |
| PEDRO ALEXANDRE MACHADO COSTA (BASIC) | ⚠ o `(BASIC)` sugere `Básico&Co` — **não confirmado** |
| ETXE CONSULTORIA (MARCOS) | 🔴 não |
| FRANCO MATHEUS | 🔴 não |
| **Cambos Jeans** | 🟢 **sim** |

⚠ **`EducAI` também não é nenhuma das 16 Soluções do Portfólio.** O nome segue o padrão `…AI`
dos produtos nativos, **mas não está na lista.** ⚠ **Não presumo que seja um deles renomeado** —
é o mesmo erro que o `CONTEXT.md` proíbe para `uBuy` e `uPick`.

🔴 **A Cambos é o único cliente de PLM que também compra EducAI.** É o primeiro caso de conta que
atravessa as duas naturezas de receita.

## 3 · 🔴 `Imersão IA` traz um tipo de cliente que a hierarquia não comporta

**Sete das treze linhas são nomes de PESSOA FÍSICA:**
Nicola Ecio Stella · Sasha Bernhardt · Stephan Buttendorf · Andreas Buttendorf ·
GIOVANNA L G STACHE · BRUNO BEWALSKI · (e `FRANCO MATHEUS`, em EducAI).

⚠ **`Stephan Buttendorf` e `Andreas Buttendorf` compartilham sobrenome** — provável mesma família
ou mesma empresa. **Não os agrupei.**

🔴 **A hierarquia travada no `CONTEXT.md` é `Instituição → Áreas → Subáreas → Pessoas`.**
**Uma pessoa física como CLIENTE não tem onde morar nesse modelo:** ela seria uma Instituição com
14 áreas canônicas e nenhuma pessoa dentro, ou uma Pessoa sem Instituição acima.
**É decisão de arquitetura, e não é minha.**

As outras seis são empresas, e **nenhuma existe no corpus**: VITRINE · TS STUDIO · SHOEBIZ ·
Ufo Way Denim Brasil · **GRUPO KYLY** · **DI-SANTINNI, DS FOOTWEAR E CAPODARTE**.

⚠ **A última linha nomeia três marcas numa célula só** — mesmo padrão de `Conrrado e Ingrid` que o
`gera-fichas-pessoa.py` recusa desmembrar sem confirmação. **Não desmembrei.**

## 4 · 🔴 `RFIs` é serviço faturável — e o corpus tem 86 delas sem saber disso

**Sete clientes, todos já no corpus:** Osklen · VIX · Puket · CAEDU · Luiza Barcelos · La Moda ·
NK STORE.

🔴 **O corpus tem 86 RFIs formalizadas, com protocolo próprio
(`protocolo-gestao-rfi.md`) — e o modela como REGISTRO DE TRABALHO, nunca como receita.**
Não há campo de faturamento, de contrato ou de cobrança em nenhuma ficha de RFI.

**Isso muda o que uma RFI é:** se ela é faturada, ela tem preço, escopo contratado e aceite —
e nada disso está no nosso modelo. ⚠ **E a `La Moda` aparece aqui comprando RFI, sendo que na
base de contratos o único serviço dela é `Fashion IA`.**

## 5 · `Outros serviços` — uma linha, um cliente

**ARAMIS.** 🔴 **Não existe no corpus.** O rótulo `Outros serviços` não diz o que foi vendido.
**Não deduzi.**

## 6 · O que fica como decisão

| # | Pergunta | Para quem |
|---|---|---|
| 1 | 🔴 **`EducAI` é uma das 16 Soluções com outro nome, ou um item novo?** E é o mesmo que "mentoria"? | Vinicius / João |
| 2 | 🔴 **Pessoa física pode ser cliente?** Se sim, onde ela mora na hierarquia? | Vinicius |
| 3 | 🔴 **RFI é serviço faturável.** O modelo de RFI ganha preço/escopo/aceite? | Vinicius |
| 4 | **Os 18 clientes novos viram casa no corpus?** Incluindo Magazine Luiza, Grupo Kyly e Aramis | Vinicius |
| 5 | **O que é `Imersão IA`? E o que foi vendido como `Outros serviços` à ARAMIS?** | Comercial |
| 6 | ⚠ **`DI-SANTINNI, DS FOOTWEAR E CAPODARTE` é uma linha com três marcas.** Um cliente ou três? | Comercial |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — foto com data. Correção vira registro novo.
