# CliprocAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
CliprocAI
### Nome legado
[a preencher]
### Descrição
Decisão CLIente × PROduto × CAnal.
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
Comercial / Vendas
### Geração
Nativa

## Maturidade
### Score de maturidade
MVP
### Fonte e data da avaliação
Registrado em 14 jul 2026 (`_pendencias-gerais.md` item 22) a partir do PRD real na pasta Drive da Cambos: PRD v1.6 com 17 ADRs, protótipo navegável com dado real, mesmo padrão ADR-006 do VendeAI (fora da Arquitetura V1 oficial até validação), com meta de piloto ≥25% de conversão em 90 dias.

## Pipeline e relações
### Consome de (upstream)
[a preencher]
### Produz para (downstream)
[a preencher]
### Módulos relacionados
Fluxo oficial da Arquitetura uMode V1 (24/04/2026): PlanejAI → CriAI → DesenvolvAI →
FornecAI → EnriqueceAI → GerenciAI, com CadastrAI como núcleo e Hub de Agentes lateral.

## Adoção por cliente
### Clientes que contrataram
Cambos (piloto)

## Marcos
| Data | Evento/decisão | Responsável | Nota |
|---|---|---|---|
| 24/04/2026 | Arquitetura uMode V1 definida em sessão | João Risoléo | 6 módulos no fluxo + CadastrAI (núcleo) + Hub de Agentes (lateral) |
| 03/08/2026 | Registro formalizado no BrainHub | [a preencher] | Primeira vez que este item do Portfólio ganha `produto.md` real |

## Governança
### Owner / Estratégia
[a preencher]
### Operador
[a preencher]
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
