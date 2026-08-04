# GerenciAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
GerenciAI
### Nome legado
[a preencher]
### Descrição
Módulo de gestão. Hoje é painel de controle; a visão futura é um ambiente AI First em quatro camadas: (1) conversacional (áudio, linguagem natural, gráficos e relatórios sob demanda); (2) lista de insights por prioridade configurada pelo usuário individual; (3) navegação por indicadores clássicos (legado em transição); (4) drill-down granular até SKU/loja/transação. Inclui motor de auditoria e alertas com regras criadas pelo próprio usuário.
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
Planejamento + Financeiro
### Geração
Nativa

## Maturidade
### Score de maturidade
Escalável
### Fonte e data da avaliação
"Arquitetura uMode — Especificação por Módulo (V1 — 24/04/2026)" (Notion `34db1d38e768814b8001d7cb6cacf4e5`), lida em 04 ago 2026: "**O módulo que a Reserva já usa hoje.** Mas a visão futura é maior." Traduzido para **Escalável** pela regra travada do protocolo (uso real declarado em cliente nomeado). ⚠ **Mudança de score — era `Ideação`.** A avaliação anterior tratou o módulo pela visão futura, que a própria página marca como brainstorm: "**Brainstorm consolidado, não decisão final**. João explicitou: 'estou no campo do brainstorm, não tenho opinião formada, vou ter que conceber'. Tratar como visão direcional para discussão com André, não como spec fechada." O módulo **atual** está em uso; a **visão AI First** é hipótese, e "GerenciAI conversacional" consta das "Pendências honestas". Os dois fatos coexistem: score reflete o que roda, não o que está desenhado.
## Pipeline e relações
### Consome de (upstream)
Eventos estruturados dos demais módulos. A página é explícita: "o **GerenciAI é consumidor**, não originador — ele renderiza, agrega, prioriza. A detecção mora em quem está mais perto do dado." Consome também do PlanejAI in-season (foto do realizado loja a loja) e das verticais do AI First.
### Produz para (downstream)
Alertas em central interna e e-mail; detecção de necessidade de estoque loja a loja que dispara a consulta ao Catálogo Reativo do FornecAI, para o que precisa expor `buscar_oferta_compativel(demanda_loja, atributos, prazo)`.
### Módulos relacionados
PlanejAI (integração ativa no modo in-season); FornecAI (jornada 3); CadastrAI (conector de e-mail provavelmente via Integrações); Hub de Agentes, com um provável agente novo `gerenciai-assistant` — pendência aberta é se ele é agente único ou orquestrador.
## Adoção por cliente
### Clientes que contrataram
Reserva — "o módulo que a Reserva já usa hoje" (Especificação por Módulo V1). ⚠ A fonte **não qualifica** como `(contratado)` ou `(piloto)`, e o protocolo exige o qualificador; fica pendente de confirmação.
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
- Teses registradas literalmente e atribuídas a João Risoléo: "o dashboard tradicional vai desaparecer. Dado vai até o usuário, não usuário até o dado"; sobre a camada 3, "mundo que tende a desaparecer… existe pra transição, não como destino"; "o que não é visto não é lembrado, e as pessoas não são cobradas. O sistema autogerencia, trabalha pelo gestor e diretor".
- Decisão pragmática registrada: "**WhatsApp ficou fora do escopo** para simplificar. GerenciAI é ferramenta de trabalho, não canal de mensagem instantânea."
- Introduz configuração por usuário individual (tabela `user_insight_preferences`), descrita como "mais granular que tudo que apareceu antes na arquitetura".
