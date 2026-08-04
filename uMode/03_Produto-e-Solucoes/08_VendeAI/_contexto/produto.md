# VendeAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
VendeAI
### Nome legado
[a preencher]
### Descrição
Ferramenta para vendas. Inclui a funcionalidade de **vestir**, no cliente final, os looks montados e o catálogo existente.
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
Declaração explícita no documento "ARQUITETURA_UMODE_REF.md — Bússola Arquitetural" (v1.0, abr 2026, João Risoléo — Drive `1xCFtkT5krc-VATCC26MeQHWOWH1BOMlE`), que registra a Arquitetura uMode V1 da sessão de 24/04/2026: "VendeAI NÃO está na Arquitetura uMode V1" — é "piloto de validação de tese com a NK", com critérios formais de promoção a módulo oficial (conversão sessão→venda ≥ 30%, NPS vendedor ≥ 7, NPS cliente ≥ 8, LGPD auditado, ≥ 50 sessões reais de try-on). Confirma a avaliação já registrada em 14 jul 2026.

## Pipeline e relações
### Consome de (upstream)
CadastrAI · CriAI (posicionamento provável, a confirmar pós-piloto)
### Produz para (downstream)
[a preencher — pendente da promoção a módulo V1]
### Módulos relacionados
Fluxo oficial da Arquitetura uMode V1 (24/04/2026): PlanejAI → CriAI → DesenvolvAI →
FornecAI → EnriqueceAI → GerenciAI, com CadastrAI como núcleo e Hub de Agentes lateral.

## Adoção por cliente
### Clientes que contrataram
NK STORE (piloto)

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
- Briefing de Vinicius Risoléo em 04 ago 2026 (função de vendas e prova virtual sobre looks/catálogo existente).
- ⚠ **Relação a investigar, não afirmada:** o Plano Técnico do Hub de Agentes inventaria um agente `tryon-stylist` ("geração de imagem, prova virtual/styling") **sob o CriAI**, não sob o VendeAI, e o VendeAI não é citado em nenhum ponto daquele plano. A funcionalidade de vestir do VendeAI e o agente `tryon-stylist` do CriAI podem ser a mesma capacidade em dois lugares — não confirmado.
