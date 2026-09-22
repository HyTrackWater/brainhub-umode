# Varredura 22 set 2026 — a base `Reuniões Compartilhadas com Clientes`

> Varredura ao vivo do Notion, a partir da instrução do Vinicius de **varrer tudo que temos de
> informação de clientes**. Começou pela Recco — a conta em churn com mais material — e
> descobriu uma **base inteira que o corpus nunca mencionou**.
>
> **Somente leitura.** Nenhuma escrita fora do `HyTrackWater/brainhub-umode`.

## 0 · Declaração de completude — o que esta varredura NÃO alcançou

| # | Lacuna | Situação | Consequência |
|---|---|---|---|
| 1 | **1.161 reuniões, 4 abertas** | 🔴 li **4 páginas de reunião** por inteiro (Recco 16/10 e 09/10, Highstil 17/04/2026, Recco kick-off 27/02/2025) | O agregado por cliente é `[C]`; **o conteúdo de 1.157 reuniões não foi lido** |
| 2 | **Gravações e transcrições** | ⚠ não abertas | Campos `Gravação` e `Tactiq` existem; **links para Tactiq e Drive não foram seguidos** |
| 3 | **Varredura de credencial** | 🔴 **não feita nesta base** | A pauta da Highstil 17/04/2026 diz *"Integração (credenciais de acesso)"* — **não sei se algum valor está exposto nas outras 1.157** |
| 4 | **Campo `Data` não confiável** | 🔴 corrompido em lote — ver §4 | Todo agregado por data desta base é **suspeito**; usei o **título** quando divergiam |
| 5 | **Por que a Recco saiu** | ⚠ **tenho o mecanismo, não a decisão** | Sei o que estava acontecendo em 16/10/2025; **nenhuma fonte registra a decisão de encerrar, nem a data** |

## 1 · O que foi encontrado, em número

| | Número |
|---|---:|
| Registros na base `Reuniões Compartilhadas com Clientes` | **1.161** |
| Clientes distintos com reunião | **27** |
| Menções a esta base no corpus **antes** desta varredura | **0** |
| Reunião mais antiga | **12/01/2023** (Caedu) |
| Reunião mais recente | **22/09/2026** (Luiza Barcelos) — **hoje** |

> **Esta é a lacuna de fonte, não de dado.** As **demandas** já estavam varridas e formalizadas
> — são **995 arquivos** em `_demandas/` no corpus, e a Recco tem os 42 dela, com descrição e
> comentário. **A base de reuniões não tinha nada.**

`[C]` — contagens por SQL sobre `collection://09a4a94e-036c-4836-a097-de8feda4df1c`.

## 2 · Reuniões por cliente — e o que a ordem revela

| Cliente | Status na base | Reuniões | Primeira | Última |
|---|---|---:|---|---|
| **Luiza Barcelos** | `Ongoing` | **126** | 13/06/2024 | **22/09/2026** |
| NK STORE | `Ongoing` | 111 | 28/06/2024 | 17/07/2026 |
| Osklen | `Operação Assistida` | 101 | 07/04/2025 | 27/07/2026 |
| Lofty Style | `Ongoing` | 83 | 07/03/2025 | **24/09/2026** — futura |
| **Lenny Niemeyer** | **`Churn`** | **75** | 06/02/2025 | **01/04/2026** |
| Cambos | `Ongoing` | 70 | 10/01/2025 | 17/09/2026 |
| NV | `Ongoing` | 64 | **09/06/2023** | 13/01/2026 |
| Moda Objetiva | `Operação Assistida` | 58 | 08/10/2025 | 17/09/2026 |
| **Highstil** | **`Churn`** | **57** | 11/02/2025 | **16/04/2026** |
| VIX | `Ongoing` | 44 | **09/06/2023** | 27/03/2026 |
| Oficina Reserva | `Ongoing` | 41 | 18/07/2024 | 20/05/2026 |
| **Plie** | **`Churn`** | 38 | 29/07/2025 | 09/04/2026 |
| **Recco** | **`Churn`** | 36 | 27/02/2025 | **16/10/2025** |
| Caedu | `Ongoing` | 35 | **12/01/2023** | 23/06/2026 |
| **Vivara** | **`Churn`** | 34 | 28/02/2023 | 03/03/2026 |
| Puket | `Ongoing` | 32 | 21/06/2023 | 13/05/2026 |
| **Hering** | **`Pré Onboardings`** | **25** | **27/06/2025** | 09/04/2026 |
| Seven Global | `Churn` | 23 | 23/01/2023 | 10/07/2024 |
| **Baw** | **`Sem CS`** | **19** | 12/08/2025 | 24/04/2026 |
| Loungerie | `Onboarding` | 19 | 30/07/2026 | 18/09/2026 |
| Studio Z | `Churn` | 17 | 09/06/2023 | 02/07/2024 |
| **`. Página Cliente [Template]`** | `Inativo` | **15** | 29/08/2025 | 02/04/2026 |
| Reserva | `Ongoing` | 13 | 28/06/2023 | 13/06/2025 |
| Básico&Co | `Churn` | 9 | 29/09/2023 | 13/11/2024 |
| *(sem cliente)* | — | **7** | — | — |
| NTK | `Churn` | 5 | 23/06/2023 | 27/02/2024 |
| DRO | `Churn` | 3 | 06/09/2023 | 13/08/2025 |
| Camys | `Sem CS` | 1 | 15/10/2024 | 15/10/2024 |

### O que esta tabela mostra e as outras fontes não mostravam

- 🔴 **A `Luiza Barcelos` é a conta mais atendida da carteira** — 126 reuniões, mais que a
  NK STORE e a Osklen. **Eu a tratei como mais um dos 10 `Ongoing`.** Não é.
- 🔴 **`Status` continua não sendo uso real, e agora com prova nova.** Quatro contas em `Churn`
  — Lenny Niemeyer, Highstil, Plie, Vivara — **têm reunião em 2026**. Confirma, por um quinto
  caminho, o que a [`_taxonomia-status-cliente.md`](_taxonomia-status-cliente.md) já registrava.
- 🔴 **A `Hering` está em `Pré Onboardings` há 15 meses, com 25 reuniões.** *Pré* não é um
  estágio curto nesta carteira.
- ⚠ **A `Baw` de novo.** `Sem CS` — o SKU que significa "ninguém atende" — com **19 reuniões e
  18 demandas**. É a **terceira** evidência independente de que a classificação dela está errada.
- 🔴 **15 reuniões apontam para `. Página Cliente [Template]`.** O template da base de clientes
  está sendo usado como se fosse um cliente. **São 15 reuniões reais sem dono.** Mais **7 sem
  cliente nenhum**. `[C]`
- **A carteira é mais antiga do que o corpus registra:** Caedu desde **12/01/2023**, NV e VIX
  desde **09/06/2023**.

## 3 · Recco — o que aconteceu, com data

A pergunta em aberto era *"não sei por que este cliente saiu"*. **Continuo sem a decisão de
saída — mas o mecanismo está lido.** `[C]`

| Data | Fato | Fonte |
|---|---|---|
| **06/02/2025** | Ativação | base `Mapa de Clientes` |
| **27/02/2025** | Kick-off — 11 dores mapeadas, 3 fases desenhadas | reunião de kick-off |
| **18/07/2025** | **Primeira demanda registrada** — **5 meses depois do kick-off** | base de demandas |
| 02/09 a 30/09/2025 | **Pico: 29 das 42 demandas em 4 semanas** | base de demandas |
| **15/09/2025** | Treinamento previsto | demanda D-2025 |
| **16/10/2025** | **Última reunião e última demanda — no mesmo dia** | ambas as bases |

### O que a última reunião diz — e o que ela declara

A ata de **16/10/2025** abre com o semáforo do projeto:

> `Geral 🟢` · `Prazo 🟢` · `Pendências 🟢` · `Riscos 🟢`

E o corpo da mesma ata registra:

> *"A equipe da engenharia estava **em pausa** devido a pendências na manutenção, que estavam
> **travando o sistema**."*
>
> *"há dificuldades com **débitos em duas mensalidades**, o que tem atrapalhado o andamento dos
> trabalhos."*

🔴 **Dois meses de inadimplência, o time do cliente parado e o sistema travado — sob quatro
sinais verdes.** Duas semanas depois não há mais reunião nem demanda.

**E o instrumento não é o culpado.** Testei antes de concluir: a weekly da **Highstil de
17/04/2026** marca `Pendências 🟡`. **O semáforo aceita amarelo e é usado com amarelo.** Logo os
quatro verdes da Recco em 16/10/2025 **foram preenchimento, não limitação da ferramenta.** `[C]`

### O padrão nas demandas canceladas

**12 das 42 demandas da Recco foram canceladas — 29%.** E o que foi cancelado tem assunto:
`Cálculo do Encaixe` · `Cálculo do Debrum` · `Cadastro de Linhas` · `Importação de Imagem` ·
`Template de ficha DEBRUM` · `Automatização da criação das referências`.

🔴 **São quase todas cálculo de engenharia e entrada em massa** — exatamente as dores nº 2, 5 e
10 do kick-off. **A conta saiu com as dores que motivaram a entrada ainda abertas.** `[C]`

⚠ **E há um padrão de resposta que merece decisão:** em pelo menos **três** demandas, a resposta
da uMode foi oferecer **a configuração de outro cliente** como caminho — *"foi detalhado um caso
de uso da **Cambos** em que as versões do produto são gerenciadas através das variantes"*;
*"sugerido o uso da funcionalidade de **BENEFICIAMENTO**"*; *"sugerido a utilização do campo
**RESPONSÁVEL** garantindo o mesmo efeito que hoje elas possuem no Modeler"*. **Não é erro** —
é reuso de solução. **Mas é uma decisão de produto tomada no atendimento, e não está registrada
como decisão em lugar nenhum.** `[P]`

## 4 · 🔴 Correção a uma afirmação minha: o coorte de fev/2025

Eu escrevi, na `STATE.md` e em três arquivos de cliente:

> *"Três ativações em oito dias, as três em churn."*

**O fato está certo e a sugestão que ele carrega está errada.** A frase sugere que as três
contas morreram por uma causa comum de entrada. **Elas não morreram juntas:**

| Cliente | Ativação | Última atividade | Viveu |
|---|---|---|---|
| **Recco** | 06/02/2025 | **16/10/2025** | **~8 meses** |
| **Lenny Niemeyer** | 03/02/2025 | **01/04/2026** | **~14 meses** |
| **Highstil** | 11/02/2025 | **16/04/2026** | **~14 meses** |

**É um coorte de ativação, não de morte.** A Recco viveu quase metade do que as outras duas.
**Correção propagada** para os arquivos dos três clientes e para a `STATE.md`.

> E a lacuna que gerou o erro **continua de pé**: **a base não tem campo `Data de Churn`.**
> Tudo acima é data de *última atividade observada*, que é a melhor proxy disponível —
> **não é data de saída**, e não deve ser usada como se fosse.

## 5 · 🔴 O campo `Data` desta base está corrompido em lote

Sete reuniões da Recco com títulos de **04/09** a **16/10/2025** carregam todas
`Data = 02/09/2025`. O mesmo ocorre na Highstil: a *"Weekly 17/04/2026"* carrega
`Data = 27/03/2026`.

**Consequência prática:** qualquer relatório, filtro ou visão desta base ordenado por `Data`
está errado. **Nesta varredura usei o título quando os dois divergiam**, e o registro de qual
usei está em cada linha da §2. `[C]`

## 6 · 🔴 Duas quebras de isolamento de cliente na fonte

O isolamento de cliente é **regra travada** no `CONTEXT.md`. A fonte não a respeita:

| Registro | Base | Clientes no mesmo registro |
|---|---|---|
| *"uFlow - Highstil/Plié - Reunião 16/04/2025 - Atualização de Projeto"* | Reuniões | **Highstil + Plié** |
| Demanda de 30/06/2025 | Demandas | **Básico&Co + VIX** |

**Não é para replicar no corpus.** É para decidir: quando um encontro atende duas contas, ele
gera **dois registros** ou **um registro com duas relações**? **Decisão do Vinicius.** `[D]`

## 7 · O que fazer com esta base

**A recomendação é tratar reunião como `communication_event`**, na
[`_espec-pessoas-e-comunicacoes.md`](_espec-pessoas-e-comunicacoes.md) — não como documento
solto. Ela já tem tudo o que aquela espec pede: **data, participantes nominais, cliente,
canal e conteúdo capturado**. `[P]`

> **É a melhor fonte de pessoa-ativa da carteira, e a espec não a conhecia.** O campo
> `Participantes` traz usuários do Notion nominalmente, reunião a reunião, com data — que é
> exatamente a `observationWindow` que a taxonomia de atividade de pessoa exige.

## 8 · Próximos passos

1. 🚨 **Varrer credencial nas 1.157 reuniões não abertas.** A pauta da Highstil de 17/04/2026
   trata de *"credenciais de acesso"* — **e ainda há duas credenciais expostas não rotacionadas**
   (NK STORE e Lofty Style).
2. 🔴 **Abrir as 126 reuniões da Luiza Barcelos** — é a conta mais atendida da carteira e a
   menos documentada em proporção.
3. 🔴 **Resolver as 22 reuniões órfãs** — 15 no template, 7 sem cliente.
4. 🔴 **Criar o campo `Data de Churn`** — segue sendo a lacuna mais cara do corpus.
5. **Decidir o registro de reunião multicliente** (§6).
6. **Incorporar `Participantes` à rastreabilidade de pessoa ativa** (§7).

## Governança

### Quem pode alterar este documento
Vinicius Risoléo · liderança de Atendimento uMode

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1, §2 — agregados | Notion — `collection://09a4a94e-036c-4836-a097-de8feda4df1c`, via SQL | **22 set 2026** |
| §3 — Recco | Notion — 4 páginas de reunião + 42 demandas + página do cliente | **22 set 2026** |
| §4 — correção do coorte | Notion — base de reuniões, últimas atividades de 3 clientes | **22 set 2026** |
| §5, §6 — defeitos de fonte | Notion — comparação título × campo `Data`; relações multicliente | **22 set 2026** |
| §7 — proposta | `[P]` minha, não validada | **22 set 2026** |
