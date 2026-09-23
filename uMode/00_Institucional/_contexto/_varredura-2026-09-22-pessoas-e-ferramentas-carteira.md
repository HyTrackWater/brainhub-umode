---
aliases:
  - "Varredura 22 set 2026 — pessoas, áreas e ferramentas contratadas, carteira inteira"
---
# Varredura 22 set 2026 — pessoas, áreas e ferramentas contratadas, carteira inteira

> Varredura transversal a pedido do Vinicius: *"retome a varredura de todos os clientes pra
> puxarmos tudo — pessoas, áreas, quais ferramentas têm contratada."*
>
> **Classe: `REGISTRO`.** Evidência datada — **não é autoridade e não se edita.** O que daqui
> virar regra vira parágrafo numa `AUTORIDADE`; as decisões foram para o
> [`_pendencias-gerais.md`](_pendencias-gerais.md).
>
> **Somente leitura no Notion.** Nenhuma escrita fora do `brainhub-umode`.

## 0 · Declaração de completude — o que esta varredura NÃO alcançou

| # | Lacuna | Consequência |
|---|---|---|
| 1 | **As pessoas vêm do campo `Quem solicitou?` das 985 demandas** | Quem **nunca abriu demanda** não aparece aqui — **ausência não é inatividade** |
| 2 | 🔴 **Nenhuma pessoa tem e-mail neste campo** — é texto livre | **Nenhuma é conciliável** com a base de usuários da plataforma |
| 3 | **27 clientes não têm demanda nenhuma** | Para eles esta varredura **não acrescenta pessoa** |
| 4 | **O campo `Participantes` das 1.161 reuniões não foi resolvido** | São IDs de usuário do Notion, não nomes — exigem `get-users` |
| 5 | **Áreas do cliente:** só apareceram as que alguém escreveu no campo de pessoa | **Não é um mapa de áreas** — é o que vazou por um campo de texto |

## 1 · Ferramentas contratadas — o enum completo, e quem tem o quê `[C]`

**O campo é `Módulos Contratados` e o enum tem 7 valores:**
`Gestão de Coleção` · `Integração` · `Relatórios` · `Fornecedores` · `Cronograma` ·
`Aposta` · `Planejamento`

| Cliente | Status | Módulos | # | ERP |
|---|---|---|:-:|---|
| **Reserva** | `Ongoing` | Gestão de Coleção · Integração · Relatórios · Cronograma · **Aposta** · **Planejamento** · Fornecedores | **7** | Linx / SAP |
| **Oficina Reserva** | `Ongoing` | Gestão de Coleção · Integração · Relatórios · Cronograma · Fornecedores | **5** | SAP e Linx |
| **Osklen** | `Operação Assistida` | Gestão de Coleção · Fornecedores · Integração · Cronograma · Relatórios | **5** | Linx |
| **Caedu** | 🔴 `Onboarding` | Gestão de Coleção · Integração · Relatórios · Fornecedores | 4 | Linx |
| **NK STORE** | `Ongoing` | Gestão de Coleção · Integração · Relatórios · Fornecedores | 4 | Linx |
| **Luiza Barcelos** | `Ongoing` | Gestão de Coleção · Relatórios · Integração · Fornecedores | 4 | Safe Tech |
| **NV** | `Ongoing` | Gestão de Coleção · Integração · Relatórios · Cronograma | 4 | Linx |
| **VIX** | `Ongoing` | Gestão de Coleção · Integração · Relatórios · **Aposta** | 4 | Linx |
| **Lofty Style** | `Ongoing` | Gestão de Coleção · Integração · Relatórios · Cronograma | 4 | Linx |
| **Moda Objetiva** | `Operação Assistida` | Gestão de Coleção · Integração · Relatórios · Cronograma | 4 | **Ilimitar** |
| ⚠ **Baw** | `Sem CS` | Gestão de Coleção · **Integração** · Relatórios · Fornecedores | **4** | **`Sem Integração`** |
| **Cambos** | `Ongoing` | Gestão de Coleção · Integração · Relatórios | 3 | **SPI — sistema próprio** |
| **Puket** | `Ongoing` | Gestão de Coleção · Integração | **2** | Linx / SAP |
| 4takes · Camys · Cavallari · Mondepars · Studio Minah · TDC · Ton Age | `Sem CS`/`Churn` | Gestão de Coleção | 1 | Sem Integração |
| Seven Global · Studio Z · Vivara | `Churn` | Gestão de Coleção | 1 | — / SAP |
| **Os outros 21** | `Churn`/`Inativo`/`Pré Onboardings` | **campo vazio** | 0 | vários |

### O que a tabela mostra

- 🔴 **`Aposta` e `Planejamento` só existem na Reserva** — e `Aposta` também na VIX.
  **São os dois módulos menos vendidos da carteira.**
- 🔴 **A anomalia da Baw se confirma pela quarta vez:** tem o módulo **`Integração`** contratado
  **e o ERP diz `Sem Integração`**. Os dois não podem estar certos.
- **`Gestão de Coleção` é universal** — nenhum cliente tem outro módulo sem ter este.
- **ERPs na carteira:** `Linx` (dominante) · `SAP` · `Linx / SAP` · `SAP e Linx` · `Totvs` ·
  `Totvs Moda` · `Safe Tech` · **`Ilimitar`** · **`Avec`** · **`SPI`** (próprio da Cambos) ·
  `Sem Integração`. ⚠ **`Ilimitar` e `Avec` não estavam no corpus.**
- ⚠ **`Linx / SAP` e `SAP e Linx` são o mesmo conceito com duas grafias** — Puket e Reserva usam
  a primeira; Oficina Reserva e Arezzo, a segunda.

## 2 · Atendimento — três unidades para dezessete contas `[C]`

**O campo `Atendimento 2025` é texto livre e tem apenas quatro valores distintos:**

| Quem atende | Contas | Quais |
|---|:-:|---|
| **Julianne + Pedro** | **7** | Caedu · Lenny Niemeyer · Loungerie · NK STORE · Osklen · Puket · VIX |
| **Laura** | **7** | Baw · Cambos · Highstil · Lofty Style · Luiza Barcelos · Moda Objetiva · Plie |
| **Fernanda** | **3** | NV · Oficina Reserva · Reserva |
| `SMB` | 7 | os sete `Sem CS` — **não é pessoa, é o Grupo 3 da segmentação** |
| *(vazio)* | 24 | todos os demais |

- 🔴 **Highstil, Lenny Niemeyer e Plie estão em `Churn` e têm atendente nomeado em 2025** — e as
  três linhas foram **editadas hoje**. Reforça, por um sexto caminho, que `Status` ≠ realidade.
- ⚠ **`Julianne + Pedro` é uma dupla num campo de pessoa.** Para o banco isso é
  `person_memberships` com dois vínculos, não um valor de texto.
- **A Fernanda concentra o ecossistema Reserva inteiro** (Reserva, Oficina Reserva) mais a NV.

## 3 · 🔴 A base foi editada HOJE, durante esta sessão

**Dezessete clientes têm `Última edição` = 22/09/2026.** E um mudou de estado **entre duas
leituras minhas, no mesmo dia**:

| Cliente | Li de manhã | Li às 15h |
|---|---|---|
| **Caedu** | **`Ongoing`** | 🔴 **`Onboarding`** |

> **É a prova mais forte possível da regra "fonte viva, nunca export".** Um export de hoje de
> manhã já estaria errado hoje à tarde. `[C]`
>
> ⚠ **Não sei o que motivou a mudança** e não presumo. **Registro o fato, com as duas leituras e
> a hora.** A CAEDU é justamente a conta da próxima frente — **isto precisa ser perguntado.**

## 4 · Pessoas com atividade datada — por cliente `[C]`

**Fonte: `Quem solicitou?` das demandas.** Cada linha traz o nome **exatamente como está na
fonte**, o número de demandas e a janela de observação. **Nada foi unificado nem inferido.**

| Cliente | Pessoas nomeadas | As mais ativas (demandas · janela) |
|---|:-:|---|
| **NK STORE** | **21** | Cris 12 · Cristina 9 · Vanessa 6 · Nathalia 6 · Julia 6 · Andressa 6 · **Hermes 5** |
| **Osklen** | **31** | Ana 12 · Maria Clara 6 · Thais Pantaleão 5 · Priscila 4 · Thayssa 3 · Marcelle 3 |
| **Lofty Style** | **28** | Gustavo 17 · Amanda 10 · Gabriela 7 · Marcello 4 |
| **Luiza Barcelos** | **25** | Gustavo 15 · Gabriel 8 · Michelle 6 · Gabriel Dart 4 · Ticiane 3 |
| **Lenny Niemeyer** | **21** | **Mariana 30** · Andre 6 · Renato 5 · Giuliana 4 · Gabi 4 |
| **Reserva** | **18** | Raquel 11 · thamires 6 · **Sourcing 6** · **Merchan 5** · Vanessa 3 |
| **Caedu** | **17** | Vitória 3 · Roselene 3 · Rose 3 · Mariana 2 |
| **NV** | **16** | Vinicius 7 · Karina 3 · Vinicius Dias 2 · Thais 2 |
| **VIX** | **8** | **Luana Henriques 27** · Luana 11 · Evelyn e Luana 3 · Catherine 3 |
| **Cambos** | **12** | Louise 9 · Carol 8 · Fabi 6 |
| **Recco** | **9** | Vitor 13 · Patricia 11 · Patrícia 7 |
| **Oficina Reserva** | **10** | Mari 7 · Mariane/Joyce 4 · Mariane 4 · Joyce 3 |
| **Moda Objetiva** | **9** | Carol 10 · Thamires 8 · Caio/Carol 2 |
| **Highstil** | **8** | Ariana 4 · Ari/Angelica 2 · Angelica 2 · Geysla 1 |
| **Puket** | **5** | Catarina 5 · Vanessa e Catarina 3 · Vanessa 3 |
| **Baw** | **6** | Mariana Basso 5 · Mari 5 · Mariana 4 |
| **Plie** | **3** | Carol/Denize/Jéssica 3 · Carol 3 |
| **DRO** | **1** | **José 13** — única pessoa, e a conta está em `Churn` |
| **uMode** | **2** | Marina 2 — a Casa como cliente de si mesma |
| **Colmeia** | **1** | *"Rafael Renaldim após reunião"* |

## 5 · 🔴 O campo `Quem solicitou?` mistura cinco coisas diferentes

**Não é um campo de pessoa. É um campo de texto onde cabe qualquer coisa.** `[C]`

| O que aparece | Exemplos reais |
|---|---|
| **Pessoa** | `Gustavo` · `Luana Henriques` · `Thais Pantaleão` |
| **Área ou time** | `Compras` · `Estilo` · `Sourcing` · `Merchan` · `Planejamento` · `Negócios` · `Treinamento` · `Contrato` · `Time Lofty` · `Time Objetiva` · `Time Osklen` |
| **Pessoa da uMode** | `Marina uMode` · `Interno uMode` · `Tech uMode` · `Time uMode` · `KA` |
| 🔴 **Um agente de IA** | **`Hermes` — 5 demandas na NK STORE**, de 29/07/2025 a 18/03/2026 |
| **Canal, colado no nome** | `Vanessa - Grupo whatsapp` · `João Neto - Via chat e e-mail.` · `Camila - via chat <URL do Gist>` · `Ana Paula Queiroz via chat` |
| **E-mail de terceiro** | `engenharia1@indorf.com.br` (Reserva) — **domínio que não é do cliente** |
| **Frase** | `Rafael Renaldim após reunião` · `Karina (04/09) e Thais Pantaleão (09/09)` · `Taissa - Reunião Key Users` |

> 🔴 **O `Hermes` abrindo demanda é o primeiro caso de agente como solicitante na carteira.**
> Para o banco isso não é `person` — é `agent`. **A `_espec-pessoas-e-comunicacoes.md` não prevê
> agente como autor de demanda.** Registrado como pendência.

## 6 · 🔴 Variação de nome é epidemia, e ameaça a identidade de pessoa

**A mesma pessoa aparece com até oito grafias.** Alguns casos, com a contagem de cada forma:

| Cliente | Grafias encontradas |
|---|---|
| **Osklen** | `Thais Pantaleão` · `Thays Pantaleão` · `Thays Pantelão` · `Tays pantaleão` · `Thays` · `Taissa` · `Tayssa` · `Thayssa` — **8 formas** |
| **NK STORE** | `Cris` · `Cristina` · `Maria Cristina` · `Cristiane` · e `Kemely` · `Kemelly` · `Kemmely` |
| **Recco** | `Patricia` · `Patrícia` · `Paty` · e `Vitor` · `vitor` · `Victor` · `Vitor Daniel` |
| **Lofty Style** | `Gabriela` · `Gabi` · `Gabriela Cunha` · e `Michelle` · `Michelle Nogueira` |
| **Puket** | `Vanessa` · `Vanesssa` |
| **Oficina Reserva** | `Mariane` · `Mari` · `Joyce` · `Joyce Dias` |
| **Baw** | `Mariana Basso` · `Mariana` · `Mari` · `Mariane` |

⚠ **E há o risco oposto — colapsar duas pessoas numa só.** Na **VIX** a fonte registra
literalmente **`Luana Henriques & Luana Carmo`**: **são duas Luanas distintas**, e o nome curto
`Luana` (11 demandas) **não diz qual das duas**.

> 🔴 **Por isso não unifiquei nada.** Sem e-mail ou identificador, **unificar por semelhança
> gráfica inventaria pessoa** — o oposto da regra de ouro. **Cada forma entrou como está,
> marcada como variante a resolver.**

## 7 · Áreas do cliente que vazaram pelo campo de pessoa

**Não é um mapa de áreas** — é o que apareceu escrito onde deveria haver nome:

`Compras` (NK STORE, Caedu) · `Estilo` (Caedu, NK STORE) · `Sourcing` (Reserva) ·
`Merchan` (Reserva) · `Planejamento` (Lenny Niemeyer) · `Negócios` (Osklen) ·
`Treinamento` (Osklen) · `Contrato` (Cambos) · `supply` (Osklen — *"Anderson supply"*) ·
`facção` (Lenny Niemeyer — *"Time facção Conrrado e Ingrid"*) ·
`designers de moda` (Osklen — *"Marcia e designers de moda"*)

- 🔴 **`Merchan` na Reserva confirma o terceiro caso de `Merchandising`** já registrado.
- ⚠ **`facção` é produção terceirizada** — não tem área canônica, e é parente do tema
  `15_Producao-Interna` (item 234 das pendências), mas **não é a mesma coisa: facção é externa.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — evidência datada de 22 set 2026. Correção se faz em documento novo.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1, §2, §3 | Notion — base `Mapa de Clientes`, 50 linhas, via SQL | **22 set 2026** |
| §4, §5, §6, §7 | Notion — base `Demandas compartilhadas`, 985 linhas, via SQL | **22 set 2026** |
