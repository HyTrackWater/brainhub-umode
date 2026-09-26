---
aliases:
  - "Recebido 25 set 2026 — o acervo de reuniões da Juliana Ferré"
tags:
  - tipo/registro
  - casa
---
# Recebido 25 set 2026 — o acervo de reuniões da Juliana Ferré

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
> **Fonte:** `Juliana Ferré-20260924T203544Z-1-001.zip`, **172 arquivos**, entregue pelo Vinicius
> em 25/09/2026. 🔴 **O bruto não entrou no repositório** — foi lido em pasta temporária.
> **Processado por** `scripts/extrai-propostas-de-resumo.py`, **junto com o acervo da Laura**:
> uma linha do tempo por cliente, não uma por acervo.

## 0 · 🔴 O que este acervo NÃO é

| # | Lacuna | Medida |
|---|---|---|
| 1 | 🔴 **Não é acervo de cliente.** É a agenda de uma diretora de Produto & Cliente | **25** reuniões confirmadas da Casa · **37** com cliente no título ou no e-mail · **88** sem destino |
| 2 | 🔴 **59% das reuniões não roteiam** | **88 de 150**: sem cabeçalho de participantes **e** sem cliente no título. `destino` fica vazio — **chutar é pior que não classificar** |
| 3 | ⚠ **Cabeçalho sem e-mail** | **34 dos 40** cabeçalhos trazem só **nomes colados** (`Ana Paula Ramos Ana Lucia Fernanda Araujo`) — resolvidos pelo índice do corpus, fail-closed |
| 4 | ⚠ **Pouca fala** | **6** dos 89 resumos têm transcrição |
| 5 | 🔴 **Cinco reuniões não foram lidas** | 1:1 e dupla interna — `Victor · Ju · 1_1` · `Saulo · Juliana` · `Ana · Juliana` (2) · `Weekly · Dupla Sinistra` |

## 1 · O que ele é

| | |
|---|---:|
| arquivos | **172** (89 resumos do Gemini + 83 chats) |
| reuniões distintas | **150** |
| período | **2022-08 → 2026-09** |
| por ano | 2022 · 4 · 2023 · 25 · 2024 · 29 · 2025 · 34 · **2026 · 58** |
| clientes com reunião roteada | **16** |
| propostas geradas (os dois acervos) | **1.108** em **146** arquivos do `_inbox-calls/` |

🟢 **Contas que ganharam linha do tempo por causa deste acervo:** Caedu · Reserva · NV · VIX ·
Loungerie · Hering · Lenny Niemeyer · Colmeia · Osklen · Puket · TDC.

## 2 · 🟢 O que ele traz que nenhuma fonte tinha: a linha do tempo da CASA

A Casa **não tem documento de jornada** — `jornada.md` é classe de cliente. **Onde a linha do
tempo da Casa deve viver é decisão do Vinicius** (pendência 780). Até lá, ela fica registrada
aqui, datada.

### ✅ Aconteceu

| Série (do título) | Reuniões | De | Até |
|---|---:|---|---|
| `Hora do K.A.FÉ` | **4** internas confirmadas + **10** não confirmadas | 2025-11-13 | 2026-08-07 |
| `Relatório de Lacre` | 1 | 2026-04-30 | — |
| `Migração · Próximos Passos` | 1 | 2026-05-11 | — |
| `💜 Reconhecimento do Novo Sistema` | **5** | 2026-08-04 | 2026-08-11 |
| `Migração PLM` | 1 | 2026-08-05 | — |

### 🔄 Acontecendo — agosto e setembro de 2026

- 🔴 **Um programa de migração de sistema, em frentes paralelas.** `🚚 Migração de Sistema` aparece
  em **cinco frentes** entre 17/08 e 02/09: **Grupo Azzas** (3 reuniões), **Loungerie** (2, roteadas
  ao cliente), **Lala**, **Lala e Marina**, **Pedro**. Antes dele: `Migração PLM` (05/08) e a
  semana de `Reconhecimento do Novo Sistema` (04–11/08).
- **22/09/2026:** `BrainWave` e `Agentes e Clientes` — **a reunião mais recente do acervo.**
- ⚠ **`Grupo Azzas` não é pasta de cliente** do corpus. Pelo próprio corpus, o grupo reúne
  contas que **são** clientes: o CRM classifica **Reserva** e **Oficina Reserva** em `Grupo 1:
  Azzas`, e o pipeline Enterprise põe **Arezzo, Hering e Loungerie** sob `Grupo AZZAS`
  (`_pendencias-gerais.md`, itens da varredura do CRM). **Não foi atribuído a nenhuma** — é a
  Casa organizando a migração de um grupo. ⚠ **A frente `Loungerie` (2 reuniões) é do mesmo
  grupo** e foi roteada ao cliente porque o nome dele está no título.

### ⏭ Por vir

**81 compromissos** das reuniões recentes da Casa, todos `⚠ PROPOSTA · DERIVADA`, nos arquivos
`*_casa_*` do `_inbox-calls/`. Os maiores blocos: `Migração de Sistema - Pedro` (12) · `- Lala` (11)
· `- Lala e Marina` (10) · `Reconhecimento do Novo Sistema` (9) · `Migração PLM` (9).

## 3 · 🔴 Erro meu, pego antes de ir para o corpus

Relatei ao Vinicius que **37 dos 40 cabeçalhos eram "só gente da uMode"**. **Falso:** eram
cabeçalhos **sem nenhum e-mail**, e conjunto vazio de domínios passava no meu teste de
subconjunto. Com os nomes resolvidos pelo índice, **34 reuniões são internas confirmadas** (somando os dois acervos) — e
toda reunião com **um nome que não resolve** fica `não confirmada`, porque o nome desconhecido
pode ser do cliente.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É registro datado. **O que mudar entra em registro novo**, apontando para este.

### Conexões
- [`_recebido-2026-09-25-acervo-reunioes-laura-cardoso.md`](_recebido-2026-09-25-acervo-reunioes-laura-cardoso.md)
  — o outro acervo, processado junto.
- [`protocolo-entrada-de-call.md`](../_protocolos/protocolo-entrada-de-call.md) — § 4, destino e
  natureza pelo e-mail.
- [`_espec-pipeline-de-contexto-e-aprovacao.md`](_espec-pipeline-de-contexto-e-aprovacao.md) — § 1,
  material interno: o critério entra, o teor não.
