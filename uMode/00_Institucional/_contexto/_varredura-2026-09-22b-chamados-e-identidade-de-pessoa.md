---
aliases:
  - "Varredura 22 set 2026 (b) — a base de chamados e a chave de identidade de pessoa"
tags:
  - tipo/registro
  - casa
---
# Varredura 22 set 2026 (b) — a base de chamados e a chave de identidade de pessoa

> Continuação da varredura transversal do mesmo dia. **Registro separado, e não emenda ao
> anterior**, porque `REGISTRO` é imutável — regra do `START.md` § 0.
>
> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**

## 0 · Declaração de completude

| # | Lacuna | Consequência |
|---|---|---|
| 1 | 🔴 **A base cobre UM MÊS: 06/01/2026 a 05/02/2026** | **Não é histórico.** É uma janela. Quem não abriu chamado nesse mês **não aparece** |
| 2 | **185 chamados, 92 e-mails** | Fora dessa janela, **a identidade de pessoa continua sem chave** |
| 3 | ⚠ **Não abri nenhum chamado individualmente** | Tenho o metadado; **o conteúdo de cada um não foi lido** |
| 4 | **`Funcionalidade da Plataforma`, `Produto` e `Projeto Relacionado` são relações não resolvidas** | Há três eixos aqui que **não foram puxados** |

## 1 · 🟢 A chave de identidade existe — e eu havia declarado que não

**Na varredura (a) de hoje eu escrevi:** *"Nenhuma pessoa tem e-mail neste campo... nenhuma é
conciliável com a base de usuários da plataforma"*, e registrei no item 252 das pendências que
**faltava decidir a chave de identidade de pessoa**.

🟢 **A chave existe: a base `Chamados & Atendimentos` tem campo `Email` individual.** `[C]`

```
samara.santos@caedu.com.br · luana.henriques@vixbrasil.com · ticiane.rosa@luizabarcelos.com.br
```

> **A afirmação anterior estava certa sobre a base de demandas e errada como conclusão geral.**
> **A lição é a de sempre: "não encontrei em X" ≠ "não existe".** Eu havia escrito a forma certa
> no registro (a) — *"nenhuma pessoa tem e-mail **neste campo**"* — mas a pendência 252
> generalizou. **Corrigido aqui.**

## 2 · 🟢 O caso das duas Luanas está resolvido

A varredura (a) registrou que a VIX tinha `Luana Henriques` (27 demandas) e `Luana` (11), com a
fonte dizendo literalmente `Luana Henriques & Luana Carmo` — e que **eu não unificaria, porque
sem e-mail unificar inventaria pessoa.**

🟢 **A base de chamados confirma: são duas pessoas reais, com e-mails distintos.** `[C]`

| Pessoa | E-mail | Chamados | Janela |
|---|---|---:|---|
| **Luana Henriques** | `luana.henriques@vixbrasil.com` | 6 | 08/01 → 28/01/2026 |
| **Luana Carmo** | `luana.carmo@vixbrasil.com` | 3 | 08/01 → 09/01/2026 |

> ⚠ **O que continua sem resposta:** as **11 demandas assinadas só `Luana`** seguem sem dono.
> **Ter a chave não resolve retroativamente o dado escrito sem ela.**

## 3 · 🟢 O domínio de e-mail identifica o cliente

**Mapa derivado dos 92 e-mails** — e ele **resolve dado que estava vazio**:

| Domínio | Cliente |
|---|---|
| `@vixbrasil.com` | VIX |
| `@bynv.com.br` | NV |
| `@nkstore.com.br` | NK STORE |
| `@loftystyle.com.br` | Lofty Style |
| `@caedu.com.br` | Caedu |
| `@usereserva.com` | Reserva |
| `@oficinareserva.com` | Oficina Reserva |
| `@puket.com.br` · `@grupounico.com` | Puket — 🟢 **o segundo domínio confirma a holding** |
| `@bawclothing.com.br` | Baw |
| `@lennyniemeyer.com` | Lenny Niemeyer |
| `@cambos.com.br` · `@souzacambos.com.br` | Cambos — **dois domínios** |
| `@camys.com.br` | Camys |
| `@osklen.com.br` | Osklen |
| `@luizabarcelos.com.br` | Luiza Barcelos |
| `@basico.com` | Básico&Co |

🔴 **18 chamados estão com o campo `Cliente` VAZIO — e o e-mail diz de quem são.**
Exemplos: `thais.rsilva@bynv.com.br` (NV), `paula.silva@caedu.com.br` (Caedu),
`mariane.araujo@oficinareserva.com` (Oficina Reserva). **É dado recuperável por regra, não por
palpite** — mas **não preenchi a base**: escrita no Notion não é nossa.

## 4 · 🔴 O módulo `Fornecedores` traz terceiros para dentro da plataforma

**Onze e-mails não pertencem ao domínio do cliente** e abriram chamado mesmo assim:

| E-mail | Consta sob | O que parece ser |
|---|---|---|
| `engenharia1@indorf.com.br` | Reserva | fornecedor de engenharia |
| `controle@floc.com.br` | Reserva | fornecedor |
| `compras1@mclprivatelabel.com.br` | Reserva | **private label** |
| `cesar@vape.com.br` | Reserva | fornecedor |
| `vanessa.riato@lavinorte.com.br` | Reserva | fornecedor |
| `faturamento@vestsurf.com.br` | Oficina Reserva | fornecedor |
| `desenvolvimento@eczoz.com.br` | Baw | fornecedor |

> 🟢 **Isto explica o módulo `Fornecedores`:** ele **dá conta na plataforma para empresas de
> fora**. **A carteira não é só de clientes — é de clientes e das cadeias deles.**
>
> 🔴 **E isso é matéria de permissionamento, não de cadastro.** Um fornecedor que atende
> **Reserva e Oficina Reserva** (mesmo grupo) precisa enxergar o quê, de quem? **A
> `_espec-pessoas-e-comunicacoes.md` não modela terceiro com acesso.**

⚠ **Quatro e-mails são pessoais (`@gmail.com`)**, entre eles um de modelagem na Luiza Barcelos e
um em Susie Modas. **Não foram copiados para o corpus**, conforme a política do `AGORA.md` § 8.1 —
**registro que existem e onde.**

## 5 · ⚠ Pessoas aparecem sob o cliente errado

| E-mail | Consta sob | Domínio diz |
|---|---|---|
| `mariana.basso@bawclothing.com.br` | **Oficina Reserva** | **Baw** |
| `vinicius.dias@bynv.com.br` | **VIX** | **NV** |
| `karine.pires@usereserva.com` | **Oficina Reserva** | Reserva — ⚠ **mesmo grupo, pode ser correto** |

> **Não corrigi nada.** Os dois primeiros parecem erro de preenchimento; o terceiro é
> provavelmente legítimo porque **Reserva e Oficina Reserva são o mesmo ecossistema.**
> **Distinguir erro de estrutura de grupo exige a decisão sobre o nível `Grupo`** — item 260.

## 6 · Vocabulário operacional que a base traz `[C]`

- **`Canal`** — ex.: `Chat Plataforma`. 🟢 **É o primeiro campo de canal tipado que encontro
  numa fonte** — a `_espec-pessoas-e-comunicacoes.md` propõe `communication_channels` e **aqui há
  um enum real para confrontar.**
- **`Tipo de Chamado`** — ex.: `INSTABILIDADE`. 🟢 **Confirma o enum já travado na espec.**
- **`Criticidade`** — ex.: `URGENTE`.
- **`Resolução`** — ex.: `TECH`. **Campo novo**, não registrado no corpus.
- **`Qntd. Chamados (DIA)`** — contador por dia.
- **Relações não resolvidas:** `Funcionalidade da Plataforma`, `Produto`, `Projeto Relacionado`.
  🔴 **`Funcionalidade da Plataforma` é um eixo que o corpus não tem** — liga chamado a
  funcionalidade, que é o que falta para ligar **dor de cliente a parte do produto.**

## 7 · Pessoas com e-mail, por cliente — a janela de jan/2026

| Cliente | E-mails distintos | Mais ativos |
|---|:-:|---|
| **NV** | **17** | `maria.palhano` 6 · `erika.leuterio` 6 · `sandy.candido` 4 |
| **VIX** | **13** | `luana.henriques` 6 · `priscilla.souza` 5 · `luana.carmo` 3 |
| **NK STORE** | **8** | `caroline.silva` 8 · `isabely.consul` 6 · `lais.batista` 3 |
| **Reserva** | **9** | `vanessa.sousa` 4 · **+5 fornecedores** |
| **Lofty Style** | **5** | `amanda.lunardelli` 5 · `luciana.nunes` 4 |
| **Oficina Reserva** | **6** | `pamela.sanzana` 3 · `joyce.dias` 3 |
| **Puket** | **4** | `giulia.gomes` 2 · **+1 do Grupo Único** |
| **Lenny Niemeyer** | **4** | `giuliana.ghanem` 2 — 🔴 **conta em `Churn` com chamado em 28/01/2026** |
| **Baw** | **3** | `mariana.basso` 6 |
| **Cambos** | 1 | `carolina@cambos.com.br` 6 |
| **Osklen** · **Camys** | 2 cada | — |
| **Caedu** · **Luiza Barcelos** · **Básico&Co** · **Paloma** · **Susie** | 1–2 | — |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Tudo | Notion — `collection://2c5b1d38-e768-805a-99b1-000b4da25cc4`, 185 linhas, via SQL | **22 set 2026** |
