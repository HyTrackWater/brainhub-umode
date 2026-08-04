# ONB HUB · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
ONB HUB
### Nome legado
[a preencher]
### Descrição
Onboarding e operação de implantação.
### Destino
Interna
### Área canônica do cliente conectada
[não aplicável — produto interno]
### Geração
Nativa

## Maturidade
### Score de maturidade
Escalável
### Fonte e data da avaliação
ÍNDICE MESTRE (Notion `34eb1d38e76881d984b8d3bc10efb095`, lido em 04 ago 2026), Domínio 4 — Produtos Internos: "Projeto: ONB HUB — Gantt Operacional concluído. Fase 4 próxima. Operado por Victor." Traduzido para **Escalável** pela regra travada do protocolo (entrega concluída e fases em andamento).
## Pipeline e relações
### Consome de (upstream)
[a preencher]
### Produz para (downstream)
[a preencher]
### Módulos relacionados
No Plano Técnico do Hub de Agentes é o **módulo consumidor da Fase 4, risco baixo**: 1 edge function e 1 agente próprio (`onb-contract-extractor`, extração de contrato, Vision + Texto). A página registra pendência de segurança: "adicionar CORS restrito e auth-guard (hoje não tem)".
## Adoção por cliente
Não aplicável — produto interno, usado pela Casa para atender clientes, não contratado
individualmente por eles
### Clientes que contrataram
[não aplicável — Destino = Interna]

## Marcos
| Data | Evento/decisão | Responsável | Nota |
|---|---|---|---|
| 24/04/2026 | Arquitetura uMode V1 definida em sessão | João Risoléo | 6 módulos no fluxo + CadastrAI (núcleo) + Hub de Agentes (lateral) |
| 03/08/2026 | Registro formalizado no BrainHub | [a preencher] | Primeira vez que este item do Portfólio ganha `produto.md` real |

## Governança
### Owner / Estratégia
[a preencher]
### Operador
Victor — o ÍNDICE MESTRE registra apenas o primeiro nome. **Provavelmente Victor Aragão**, a única pessoa com esse nome com ficha na Casa, mas a fonte não confirma o sobrenome.
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
- ÍNDICE MESTRE, Domínio 4. Página do projeto: `32cb1d38e7688118a394ec3d74f66cb4` (não lida).
