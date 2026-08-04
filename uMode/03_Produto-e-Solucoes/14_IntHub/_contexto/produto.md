# IntHub · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
IntHub
### Nome legado
[a preencher — hipótese levantada por Vinicius Risoléo em 04 ago 2026 e por ele mesmo marcada como incerta ("não tenho certeza, mas acho"): o **uConnect** seria o nome do módulo de integrações. Evidência independente que apoia a existência do uConnect, mas **não** a equivalência com IntHub: a documentação técnica dos repositórios de integração descreve `umode-microservice-uconnect` como o interceptor em produção que intermedia Baw, Lofty Style e Osklen, mantém o snapshot MongoDB, gera a referência do produto e injeta contas contábeis. Nenhuma página do Notion lida até 04 ago 2026 cita uConnect — nem o ÍNDICE MESTRE, nem o Plano Técnico do Hub de Agentes, nem as páginas de Taxonomia. A equivalência uConnect → IntHub segue **não confirmada**]
### Descrição
Integrações · gold standard.
### Destino
Interna
### Área canônica do cliente conectada
[não aplicável — produto interno]
### Geração
Nativa

## Maturidade
### Score de maturidade
[a preencher — o ÍNDICE MESTRE do Notion **não lista IntHub** no Domínio 4 (Produtos Internos), apesar de citá-lo nominalmente na atualização de 28/05/2026 como produto interno single-tenant. Não há página de projeto nem declaração de estágio em nenhuma fonte lida até 04 ago 2026]
### Fonte e data da avaliação
Repositório de código ativo confirmado (`integration-pulse-check-e914756f`, via `launch.json` do CEO, registrado em 10 jul 2026), sem declaração de estágio em nenhuma fonte.

## Pipeline e relações
### Consome de (upstream)
[a preencher]
### Produz para (downstream)
[a preencher]
### Módulos relacionados
Produto interno **single-tenant** pela regra confirmada em 28/05/2026 no ÍNDICE MESTRE (`organization_id`/multi-tenancy só em produtos comerciais). ⚠ **Não é citado em nenhum ponto do Plano Técnico do Hub de Agentes**, diferente de CriAI, CadastrAI, CX Hub, ONB HUB e Gest Hub.
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
- ÍNDICE MESTRE (Notion `34eb1d38e76881d984b8d3bc10efb095`): citado só na atualização de 28/05/2026, sem entrada própria no Domínio 4 e sem página de projeto. É a Solução do Portfólio com menos rastro documental de todas as 16.
