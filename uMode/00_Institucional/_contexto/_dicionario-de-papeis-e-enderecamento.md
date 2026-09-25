---
aliases:
  - "Dicionário de papéis — de quem é o contexto, e para quem vai a aprovação"
tags:
  - tipo/dicionario
  - casa
---
# Dicionário de papéis — de quem é o contexto, e para quem vai a aprovação

> **Classe: `DICIONÁRIO`.** 🔴 **Dono único da tradução `papel declarado` → `pessoa:<e-mail>`.**
>
> **Fase 0, item 3** do [`_espec-pipeline-de-contexto-e-aprovacao.md`](_espec-pipeline-de-contexto-e-aprovacao.md).
> Escrito em 25/09/2026.
>
> **Por que ele existe:** o `protocolo-gestao-demanda.md` § *Mecanismo de aprovação* manda a
> aprovação para *"pessoa com permissão — já registrada no campo Governança do MD-alvo"*.
> 🔴 **Esse campo guarda PAPEL em prosa, não pessoa.** Sem esta tradução, **o roteador não tem
> para onde mandar nada.**

## 0 · 🔴 Declaração de completude — o placar honesto

**Dos 5 papéis usados no corpus, 2 resolvem, 1 tem contradição entre documentos, 1 não resolve,
e o que NÃO resolve é justamente o mais usado — 1.219 dos 1.292 documentos.**

| # | Não resolve | Por quê |
|---|---|---|
| 1 | 🔴 **`liderança de Atendimento uMode`** | **três leituras possíveis, nenhuma provada** — § 3 |
| 2 | ⚠ **`Liderança de Pessoas e Cultura`** | **dois documentos do corpus discordam** — § 4 |
| 3 | ⚠ **`Responsável de atendimento` em 17 clientes** | ausência verificada em 3 fontes |

## 1 · 🟢 O que esta Fase 0 já corrigiu, e onde estava o engano

⚠ **Eu disse ao Vinicius que o bloqueio eram as 999 demandas sem dono. Estava errado, e a
correção importa.** O protocolo **não** roteia para a demanda: roteia para o **MD-alvo** — o
documento que a mudança de contexto vai alterar.

🟢 **E os MDs-alvo estão cobertos: 1.292 de 1.321 (98%) têm papel declarado.**

| Alvo de mudança de contexto | com papel | sem |
|---|---:|---:|
| `contexto-area.md` | 680 | 14 |
| ficha de pessoa | 466 | 14 |
| `institucional.md` | 50 | 0 |
| `jornada.md` | 48 | 1 |
| `pessoas.md` | 48 | 0 |

🔴 **Logo o gargalo nunca foi cobertura. É que 0% dos papéis vira pessoa.**

## 2 · A tabela de tradução

| Papel declarado | Ocorrências | Resolve para | Estado |
|---|---:|---|---|
| **`Responsável de atendimento`** | 1.219 | fato `atendimento` do **próprio cliente** | 🟢 **25 clientes** · ⚠ 6 `SMB` · 🔴 17 sem |
| **`liderança de Atendimento uMode`** | 1.219 | — | 🔴 **§ 3** |
| **`Liderança de Pessoas e Cultura`** / `Liderança de People` | 64 | — | ⚠ **§ 4** |
| **`CEO`** | 69 | **João Risoléo** — [`joao-paulo-contar-risoleo`](../_pessoas/joao-paulo-contar-risoleo.md) | 🟢 **resolve** |
| **`Responsável da área`** | 8 | fato `responsavel-area` da área **daquele cliente** | 🟢 resolve onde o fato existe |

🟢 **`Responsável de atendimento` é o único que virou endereço nesta fase** — de **14 para 25
clientes**, mais 6 `SMB`. ⚠ **Mas ele quase nunca aparece sozinho:** vem sempre como
`Responsável de atendimento + liderança de Atendimento uMode`. 🔴 **A segunda metade não resolve,
então o par fica pela metade em 1.219 documentos.**

## 3 · 🔴 `liderança de Atendimento uMode` — três leituras, e eu não escolho

| Leitura | Fonte no corpus | Problema |
|---|---|---|
| **`Ju` — Diretora de Operações** | `02_Atendimento/_contexto/contexto-area.md` § Responsável pela área | 🔴 **`Ju` é um token só, e há DUAS na Casa:** [`juliana-ferre-esteves`](../_pessoas/juliana-ferre-esteves.md) e [`julianne-dias-rodrigues`](../_pessoas/julianne-dias-rodrigues.md) |
| **`Luciano Troiani` — Head de CS** | ficha dele, § Cadeira | ⚠ **`Head de CS` é o cargo mais próximo de "liderança de Atendimento"** — mas o `contexto-area.md` da área **não o nomeia** |
| **Diretora de Operações ≠ liderança de Atendimento** | — | ⚠ `02_Atendimento` e `08_Operacoes` declaram **a mesma pessoa** (`Ju`) — pode ser acúmulo, pode ser erro de preenchimento |

🔴 **E há uma contradição que sozinha já impede escolher:** o `contexto-area.md` de
`02_Atendimento` diz **`Ju — Diretora de Operações`**, mas **nenhuma das duas fichas `Ju` tem
essa cadeira** — a da Juliana Ferré diz `Key Account · Consultor(a) de Negócios`.

⚠ **Escolher aqui endereçaria 1.219 aprovações para possivelmente a pessoa errada.**
🔴 **Endereçar aprovação para quem não é dono é pior que não endereçar** — a aprovação volta
assinada e parece legítima.

**Decisão do Vinicius.** Até lá, o roteador trata este papel como **não resolvido** e
🔴 **falha alto**.

## 4 · ⚠ `Liderança de Pessoas e Cultura` — dois documentos discordam

| Documento | O que diz |
|---|---|
| `07_People/_contexto/contexto-area.md` | **`Flávia Campello` (execução) · `João Risoléo` (decisão)** |
| ficha da [`flavia-bonalume-campello`](../_pessoas/flavia-bonalume-campello.md) § Cadeira | **`Analista de Gestão Financeira e Administrativa`** |

⚠ **Não é necessariamente conflito** — pode ser acúmulo de função. 🔴 **Mas como os dois textos
não se referenciam, o roteador não tem como saber**, e **conflito é dado, não erro a apagar**
(`protocolo-fato-atomico.md` § 2.2).

🟢 **A metade `CEO` resolve**, então uma aprovação deste par **pode seguir para o João** enquanto
a outra metade fica aberta.

## 5 · 🟢 A regra de resolução, para o roteador implementar

```
papel                              → fonte                                → escopo
Responsável de atendimento         → fato `atendimento`                   → o PRÓPRIO cliente
Responsável da área                → fato `responsavel-area`              → área daquele cliente
CEO                                → ficha fixa (João Risoléo)            → Casa
liderança de <Área> uMode          → `### Responsável pela área` da Área  → Casa
```

### 5.1 · 🔴 As três invariantes

1. 🔴 **Escopo é sempre o próprio cliente.** Resolver o papel de um cliente com evidência de
   outro é a falha que já casou o falante `Juliana` da CAEDU com `juliana@osklen.com.br`.
2. 🔴 **Nome de um token só nunca resolve.** `Ju`, `Pedro`, `Rose` não são identidade.
   ⚠ **`Pedro` foi resolvido em 5 clientes** — não afrouxando a regra, e sim trazendo um
   **segundo sinal do mesmo cliente** (nome completo na base de demandas). **Onde o segundo
   sinal não existiu — Loungerie — continua aberto.**
3. 🔴 **Falhar alto.** Papel não resolvido **para o fluxo e nomeia o que falta.** Nunca escolhe
   o candidato mais plausível.

### 5.2 · ⚠ `SMB` obriga um fallback, e isso é requisito, não detalhe

**6 contas não têm CS dedicado por desenho** — `4takes`, `Camys`, `Cavallari`, `Studio Minah`,
`TDC`, `Ton Age`. 🔴 **Não há pessoa de atendimento a quem endereçar, e isso não é lacuna.**
⚠ **O roteador precisa de um destino de exceção para elas** — provavelmente a liderança de
Atendimento, **que é exatamente o papel que não resolve (§ 3).**

## 6 · 🔴 O que só o Vinicius decide

| # | Pergunta | Trava |
|---|---|---|
| 1 | **Quem é `liderança de Atendimento uMode`?** | **1.219 documentos** |
| 2 | **`Ju` é a Juliana Ferré ou a Julianne Dias?** E a cadeira `Diretora de Operações` está certa nas fichas? | § 3 |
| 3 | **`Flávia Campello` acumula People, ou o `contexto-area.md` está desatualizado?** | 64 documentos |
| 4 | **Para quem vai a aprovação de uma conta `SMB`?** | 6 contas |
| 5 | **Quem é dono de demanda e de RFI?** ⚠ **Não é urgente como eu disse** — o protocolo roteia para o MD-alvo. Mas segue vazio em 999 e 87 | edição do próprio registro |

## Governança

### Quem pode alterar este documento
Vinicius + CEO. 🔴 **Este documento decide para quem vai toda aprovação de contexto** — mudança
aqui muda quem assina no BrainHub inteiro.

### Quando ler
🔴 **Antes de implementar o roteador** (§ 5) e sempre que um papel novo aparecer num campo
`Quem pode alterar este documento`.

### Conexões
- [`_espec-pipeline-de-contexto-e-aprovacao.md`](_espec-pipeline-de-contexto-e-aprovacao.md) § 5.
- [`protocolo-gestao-demanda.md`](../_protocolos/protocolo-gestao-demanda.md) § *Mecanismo de
  aprovação e retroalimentação* — 🟢 **o mecanismo já está escrito lá e é a autoridade dele.**
