# Lista definitiva de clientes reais — base da replicação total

> **Passo zero da ⭐ ORDEM DE PRIORIDADE** (`STATE.md`): antes de gerar qualquer casa de cliente,
> construir a lista definitiva e filtrada de quem é cliente uMode de verdade.
> Construída em 03 ago 2026 por cruzamento de fontes reais. Nenhum nome foi inventado; nenhuma
> linha foi classificada por semelhança de nome.

## Fontes cruzadas (todas reais, com ID de Drive)

| Fonte | O que é | ID / caminho | Data da fonte |
|---|---|---|---|
| CRM "Mapa de Clientes" | Base-mãe de clientes (49 linhas × 47 colunas) | `1_Bt8qKNeTVnlDAaeM1oOdoWgBmb6ek8k` (CSV) | 05 mar 2026 |
| Pasta Drive "Clientes" | Pasta própria por cliente/negócio | `14PwnAIF55IkdWNo90iEH9Ex5TusopsWO` | listagem de 03 ago 2026 |
| Base "Demandas de Clientes" | 836 demandas, todos os clientes | `1U3B3MwvjnImUXB4I4XDP906huCvflFVK` (CSV) | 05 mar 2026 |
| Base "Reuniões Compartilhadas com Clientes" | 939 reuniões, todos os clientes | `1mxs-UE3a_fF0MZMDlfh_zG9RldkbDmpa` (CSV) | 05 mar 2026 |
| Base "RFI Escopo - Lista de Entregáveis" | RFIs, todos os clientes | `12N_kgBHhrIKriPwrhaOpw1i5F4lSFHrc` (CSV) | 05 mar 2026 |

**Regra de autoridade aplicada:** o **CRM é a única fonte de "quem é cliente"**. A pasta Drive
"Clientes" é fonte de *conteúdo*, nunca de *estrutura* — é a mesma regra já travada em 10 jul 2026
("documento externo é fonte de informação, não de estrutura"). Um nome que existe só no Drive e
não no CRM **não vira casa de cliente** sem confirmação explícita.

## Decisão de escopo: 46 clientes reais

49 linhas no CRM − 3 linhas que não são cliente = **46 clientes reais**.

### As 3 linhas descartadas (não são cliente)
| Linha CRM | Por que não é cliente |
|---|---|
| `uMode` | É a própria Casa — já existe como `uMode/`, não como cliente. Status "Inativo" no CRM. |
| `. Página Cliente [Template]` | Linha de template do Notion (o ponto inicial no nome é a convenção de template do próprio Notion). |
| `Fornecedores` | Página de fornecedores, não organização atendida. Status "Inativo", 3 campos preenchidos. |

## Os 46 clientes reais

Colunas: **Status** = campo `Status` do CRM · **Drive** = tem pasta própria em "Clientes" ·
**Dem/Reu** = registros nas bases de Demandas/Reuniões · **CRM** = quantos dos 47 campos do CRM
estão preenchidos (indicador de riqueza de dado disponível, não de importância do cliente).

| # | Cliente | Status (CRM) | Drive | Dem | Reu | CRM | Situação no BrainHub |
|---|---|---|---|---|---|---|---|
| 1 | Lofty Style | Onboarding | — | 62 | 58 | 24 | ✅ casa existente (piloto) |
| 2 | Luiza Barcelos | Onboarding | ✅ | 61 | 111 | 29 | ✅ casa existente (piloto) |
| 3 | Cambos | Regime CS | ✅ | 39 | 55 | 27 | ✅ casa existente (piloto) |
| 4 | Moda Objetiva | Onboarding | — | 16 | 29 | 8 | ✅ casa existente (piloto) |
| 5 | NK STORE | Onboarding | — | 74 | 92 | 30 | a criar |
| 6 | NV | Regime CS | — | 95 | 64 | 25 | a criar |
| 7 | Osklen | Onboarding | ✅ | 93 | 55 | 25 | a criar |
| 8 | Reserva | Regime CS | ✅ | 111 | 13 | 19 | a criar |
| 9 | Lenny Niemeyer | Onboarding | — | 59 | 65 | 25 | a criar |
| 10 | VIX | Onboarding | — | 52 | 38 | 25 | a criar |
| 11 | Recco | Churn | — | 42 | 36 | 21 | a criar |
| 12 | Highstil | Onboarding | — | 14 | 52 | 21 | a criar |
| 13 | Oficina Reserva | Regime CS | — | 23 | 37 | 18 | a criar |
| 14 | Caedu | Regime CS | ✅ | 18 | 25 | 24 | a criar |
| 15 | Puket | Regime CS | — | 15 | 28 | 15 | a criar |
| 16 | Baw | Regime CS | — | 15 | 17 | 15 | a criar |
| 17 | DRO | Churn | — | 24 | 3 | 12 | a criar |
| 18 | Plie | Onboarding | — | 12 | 33 | 9 | a criar |
| 19 | Vivara | Churn | — | 0 | 33 | 16 | a criar |
| 20 | Seven Global | Churn | — | 0 | 23 | 17 | a criar |
| 21 | Hering | Negociação | ✅ | 0 | 19 | 7 | a criar |
| 22 | Studio Z | Churn | — | 0 | 17 | 17 | a criar |
| 23 | Básico&Co | Churn | — | 1 | 9 | 14 | a criar |
| 24 | NTK | Churn | — | 0 | 5 | 9 | a criar |
| 25 | Colmeia | Churn | — | 1 | 0 | 18 | a criar |
| 26 | Hyperlocal | Churn | — | 0 | 0 | 17 | a criar |
| 27 | 4takes | Regime CS | ✅ | 0 | 0 | 15 | a criar |
| 28 | Camys | Regime CS | — | 0 | 1 | 13 | a criar |
| 29 | Ladeira Bijuterias | Churn | — | 0 | 0 | 11 | a criar |
| 30 | Lojão do Brás | Churn | — | 0 | 0 | 9 | a criar |
| 31 | TDC | Regime CS | — | 0 | 0 | 7 | a criar |
| 32 | Studio Minah | Sem CS | — | 0 | 0 | 7 | a criar |
| 33 | Cavallari | Sem CS | — | 0 | 0 | 7 | a criar |
| 34 | Ton Age | Sem CS | — | 0 | 0 | 7 | a criar |
| 35 | Laces | Churn | — | 0 | 0 | 7 | a criar |
| 36 | Ricardo Almeida | Churn | — | 0 | 0 | 7 | a criar |
| 37 | Texneo | Churn | — | 0 | 0 | 6 | a criar |
| 38 | Estrela | Churn | — | 0 | 0 | 6 | a criar |
| 39 | Simples (by Reserva) | Inativo | — | 0 | 0 | 6 | a criar |
| 40 | Mondpars | Regime CS | — | 0 | 0 | 5 | a criar |
| 41 | Paloma concept | Inativo | — | 0 | 0 | 4 | a criar |
| 42 | Susie Modas | Inativo | — | 0 | 0 | 4 | a criar |
| 43 | Phos | Churn | — | 0 | 0 | 4 | a criar |
| 44 | Pampili Mini | Inativo | — | 0 | 0 | 3 | a criar |
| 45 | Agua de Coco | Inativo | — | 0 | 0 | 3 | a criar |
| 46 | La Moda | Inativo | — | 0 | 0 | 3 | a criar |

### Distribuição por Status (CRM)
Churn 16 · Regime CS 11 · Onboarding 9 · Inativo 6 · Sem CS 3 · Negociação 1 — soma 46.

**Decisão registrada:** cliente em `Churn`/`Inativo` **também recebe casa completa**. Motivo: a
estrutura é o schema (`CONTEXT.md` → "Como estamos construindo"), e o histórico de um cliente que
saiu é contexto institucional válido (por que saiu, o que usava, quem atendia). O `Status atual` do
`institucional.md` registra a situação real — não se apaga cliente, se registra o estado dele.

## Nomes que existem no Drive mas NÃO no CRM — pendência, não viraram casa

A pasta Drive "Clientes" tem 9 nomes com aparência de marca de moda que **não têm linha no CRM
"Mapa de Clientes"**. Pela regra de autoridade acima, nenhum deles foi criado como casa:

`Alpargatas` · `Polenectar` · `Genuo` · `Grupo Veste` · `Notre Dame` · `Arezzo` · `Posthaus` ·
`Esposende` · `Lupo`

Hipóteses possíveis (nenhuma confirmada): prospect/proposta em andamento, cliente antigo anterior
ao CRM atual, ou pasta de análise sem relação de contrato. **Aguarda confirmação do Vinicius** —
registrado em `_pendencias-gerais.md`.

## Nomes no Drive que aparentam ser outro negócio do CEO — confirmados fora do escopo

Mesma pasta "Clientes", mas sem linha no CRM e com nome que não é marca de moda-PLM:
`Kaizen` · `CrossX-JUMP3R` · `MBS-3-Mentorias` · `ALINVEST-IFT` · `Marcio Delbin (Tetris)` ·
`NV-Vinicius` · `_Propostas` · `_Análises` · `uMode`.

Já sinalizados como cuidado explícito na ⭐ ORDEM DE PRIORIDADE de 14 jul 2026 — mantidos fora.

⚠ **Não confundir `NV-Vinicius` (pasta Drive) com `NV` (linha real do CRM).** `NV` é cliente real
(Regime CS, Grupo 1: Azzas, 25 campos preenchidos, 95 demandas, 64 reuniões) e entra na lista acima.
A pasta `NV-Vinicius` é outra coisa e não foi usada como fonte — os dois **não foram fundidos**.

## Limitação conhecida das fontes (importante para quem ler depois)

As bases de Demandas/Reuniões/RFIs disponíveis no Drive são um **snapshot de 05 mar 2026**. Os 4
clientes-piloto foram formalizados a partir de exports mais recentes (jul 2026), fornecidos
diretamente pelo Vinicius, e por isso têm **mais** registros do que este snapshot mostra:

| Cliente | Demandas formalizadas (export jul 2026) | Demandas neste snapshot (mar 2026) |
|---|---|---|
| Lofty Style | 85 | 62 |
| Luiza Barcelos | 70 | 61 |
| Cambos | 47 | 39 |
| Moda Objetiva | 34 | 16 |

**Consequência:** os arquivos já formalizados dos 4 pilotos **não são regenerados** a partir do
snapshot (seria perda de dado). Para os 42 clientes novos, o snapshot de mar 2026 é a melhor fonte
disponível hoje — cada demanda/RFI gerada registra a data da fonte, e um re-export mais recente do
Notion permite completar depois sem retrabalho estrutural.
