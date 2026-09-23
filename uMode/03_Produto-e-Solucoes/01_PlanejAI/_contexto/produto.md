---
aliases:
  - "PlanejAI · Produto"
---
# PlanejAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
PlanejAI
### Nome legado
uPlan (linhagem confirmada pelo Vinicius, 13 jul 2026)
### Descrição
Módulo de planejamento de mix e entrada do ciclo: lê o histórico já sanitizado no CadastrAI e roda análise top-down + bottom-up sobre quatro indicadores (ROI, giro, margem, cobertura). Analisa cada SKU como interseção de grupo de produto × faixa de preço × loja/cluster × produto (a "caixinha"), gerando o porquê do corte. Dois modos: **PRÉ-SEASON** (modo atual — estúdio sob demanda) e **IN-SEASON** (modo futuro).
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
Planejamento
### Geração
Nativa

## Maturidade
### Score de maturidade
MVP
### Fonte e data da avaliação
Briefing de Vinicius Risoléo em 04 ago 2026: "saiu de uma ideia aplicada em planilhas, de forma que hoje está num protótipo do Lovable e que tem sido conduzido via entregas aos clientes (com pequenos marcos). Essa é a maturidade da ferramenta." Traduzido para **MVP** pela regra travada do protocolo: protótipo rodando com entregas reais a cliente, mas não em produção plena. Corroborado pelo ÍNDICE MESTRE do Notion ("Sprint 2 concluída"). Linhagem legado→novo já confirmada: **uPlan → PlanejAI** (13 jul 2026).
## Pipeline e relações
### Consome de (upstream)
CadastrAI (histórico de produto já tratado a partir do ERP) e Taxonomia (atributos e pesos).
### Produz para (downstream)
CriAI — "mix sugerido" (atributos da Taxonomia + pesos da marca) que vira input do CriAI em modo briefado; "plano loja a loja" (profundidade por SKU por cluster). No modo in-season, emite eventos para o GerenciAI (ruptura iminente, sobra projetada, sugestão de remanejamento).
### Módulos relacionados
GerenciAI (o modo in-season "exige integração ativa com GerenciAI"); Taxonomia; vertical "Realocação" do AI First, cuja porta de entrada é o modo in-season.
## Adoção por cliente
### Clientes que contrataram
**Reserva (contratado)** — 🟢 **qualificador confirmado em 23 set 2026 pela base de contratos do
Financeiro**, que lista `uPlan` entre os serviços faturados da conta. O ÍNDICE MESTRE do Notion já
a apontava como cliente âncora, mas **não dizia se era contratado ou piloto**; o protocolo exige o
qualificador e agora ele tem fonte.

🔴 **Recco (contratado — CANCELADO em set/2025).** A base de contratos registra, no campo `OBS` da
conta: *"Cancelamento uPlan set/25 + uRocket fev/26"*. **`uPlan` é o PlanejAI** — linhagem travada
no `CONTEXT.md` desde 13 jul 2026.

⚠ **Esta ficha registrava um cliente. Foram dois, e um cancelou** — e o cancelamento é anterior ao
churn da própria conta. **Nenhuma fonte do corpus tinha esse dado até a base do Financeiro chegar.**

## Marcos
| Data | Evento/decisão | Responsável | Nota |
|---|---|---|---|
| 24/04/2026 | Arquitetura uMode V1 definida em sessão | João Risoléo | 6 módulos no fluxo + CadastrAI (núcleo) + Hub de Agentes (lateral) |
| 03/08/2026 | Registro formalizado no BrainHub | [a preencher] | Primeira vez que este item do Portfólio ganha `produto.md` real |
| 04/08/2026 | Maturidade confirmada como MVP e operador identificado | Vinicius Risoléo | Protótipo no Lovable, conduzido por entregas ao cliente com pequenos marcos; origem em planilhas |

## Governança
### Owner / Estratégia
[a preencher]
### Operador
Vinicius Risoléo — o ÍNDICE MESTRE registra "Operado por Vini".
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**. Vinicius está alterando tudo neste momento porque está na fase de construção do cérebro — é exceção declarada de construção, não a regra de operação.
## Fontes e referências
### Documentos técnicos consultados
- `CONTEXT.md` → "Portfólio completo de produtos e soluções" (lista travada dos 16 itens)
- documento "ARQUITETURA_UMODE_REF.md — Bússola Arquitetural" (v1.0, abr 2026, João Risoléo — Drive `1xCFtkT5krc-VATCC26MeQHWOWH1BOMlE`), que registra a Arquitetura uMode V1 da sessão de 24/04/2026
- ⚠ **Fonte de verdade canônica declarada está no Notion**, não no Drive: página "Arquitetura
  uMode V1" (`34db1d38e768814b8001d7cb6cacf4e5`) e skill `umode-arquitetura-tese`
  (`34db1d38e768819abc2dc7844ff2be59`). O próprio documento de arquitetura diz: "se
  contradição entre este arquivo e a página V1 → página V1 vence".
- ✅ **A página V1 do Notion foi lida na íntegra em 03 ago 2026** (51 KB, especificação módulo a
  módulo). É de onde vêm as decisões de maturidade desta rodada. Nota de nomenclatura: a página
  canônica escreve **"ForneceAI"**, e `CONTEXT.md` escreve **"FornecAI"** — divergência real
  entre fontes, registrada em `_pendencias-gerais.md`; nenhum dos dois foi alterado por conta
  própria.
- ÍNDICE MESTRE — Fonte de Verdade uMode (Notion `34eb1d38e76881d984b8d3bc10efb095`, gerado 26/04/2026, última atualização registrada 28/05/2026), Domínio 3: "Projeto: PlanejAI — Sprint 2 concluída. Cliente âncora: Reserva. Operado por Vini." Página do projeto: `32db1d38e7688106bdc0f126dea75fab` (não lida).
- "Arquitetura uMode — Especificação por Módulo (V1 — sessão 24/04/2026)" (Notion `34db1d38e768814b8001d7cb6cacf4e5`), lida por inteiro em 04 ago 2026. Premissas nomeadas: Product Score (labels A–E, calibrável por marca), sazonalidade aplicada depois do score, Potencial Inexplorado (acertou · estoque zerado · perdeu venda · produziu demais · sem referência).
- ⚠ Decisão de escopo registrada na sessão: "a queima direcionada a clientes específicos é uma feature comercial nova que implica conexão com base de clientes — está fora do escopo desta sessão".
- ⚠ O **modo in-season está na lista "Pendências honestas — não vender hipótese como decisão"** da skill `umode-arquitetura-tese`.

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Solução:** `01_PlanejAI` — uma das 16 do Portfólio.

**Protocolo que governa esta ficha:** [`protocolo-gestao-produto.md`](../../../00_Institucional/_protocolos/protocolo-gestao-produto.md)

**Institucional da Casa:** [institucional.md](../../../00_Institucional/_contexto/institucional.md)

**As outras 15 Soluções do Portfólio:**

- [CriAI](../../02_CriAI/_contexto/produto.md)
- [DesenvolvAI](../../03_DesenvolvAI/_contexto/produto.md)
- [FornecAI](../../04_FornecAI/_contexto/produto.md)
- [EnriqueceAI](../../05_EnriqueceAI/_contexto/produto.md)
- [GerenciAI](../../06_GerenciAI/_contexto/produto.md)
- [AlocAI](../../07_AlocAI/_contexto/produto.md)
- [VendeAI](../../08_VendeAI/_contexto/produto.md)
- [CliprocAI](../../09_CliprocAI/_contexto/produto.md)
- [CadastrAI](../../10_CadastrAI/_contexto/produto.md)
- [Taxonomia](../../11_Taxonomia/_contexto/produto.md)
- [CX Hub](../../12_CX-Hub/_contexto/produto.md)
- [ONB HUB](../../13_ONB-HUB/_contexto/produto.md)
- [IntHub](../../14_IntHub/_contexto/produto.md)
- [Gest Hub](../../15_Gest-Hub/_contexto/produto.md)
- [Sales Hub](../../16_Sales-Hub/_contexto/produto.md)
