# Taxonomia · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
Taxonomia
### Nome legado
[a preencher]
### Descrição
Taxonomia canônica do PLM padrão da uMode — modelo de dados que **substitui o legado uFlow** e vira base do novo sistema sob medida (AI HOUSE) e da migração dos clientes existentes. Entregável central é um de/para campo a campo (`de_para_completo.csv`, 6.567 linhas), a planilha mestra `Modelo_PLM_Padrao.xlsx` (13 abas) e `classification.json` (2.618 clusters, declarado pela própria página como fonte de verdade). O modelo novo é uma ficha de produto com 11 blocos (Identificação, Variantes, Composição/BOM como N:N, Fornecimento, Consumos/Medidas, Artes/Etiquetas, Cuidados, Aprovações, Detalhamento, Comercial, Notas) + 4 views paralelas (Workflow, Timeline, Integração read-only, Histórico/audit log).
### Destino
Interna
### Área canônica do cliente conectada
[não aplicável — produto interno]
### Geração
Nativa

## Maturidade
### Score de maturidade
MVP
### Fonte e data da avaliação
Duas fontes canônicas lidas em 04 ago 2026, e **as duas apontam para estágio anterior a produção**. Página "Taxonomia" (Notion `348b1d38e7688087aef7e8a2b64349d0`): "versão atual: v1 — baseline abril/2026"; "próxima (v2): após curadoria da cauda longa + **primeiro piloto completo**"; **1.820 dos 2.618 clusters ainda em revisão humana**; "clientes piloto: NV (DesenvolvAI), **a confirmar**". Especificação por Módulo V1 (`34db1d38e768814b8001d7cb6cacf4e5`), ainda mais conservadora: "existe **esboço inicial** dela em pasta de Templates do Notion". Traduzido para **MVP** pela regra travada do protocolo: modelo especificado e baseline versionada em git, mas sem piloto completo e com a cauda longa pendente. ⚠ **Mudança de score — era `Escalável`.** A avaliação anterior partiu do papel transversal que a Taxonomia tem no desenho ("idioma comum entre todos os módulos"), que é importância, não maturidade. Nenhuma fonte declara produção.
## Pipeline e relações
### Consome de (upstream)
Legado uFlow: 101 fichas técnicas e 6.567 campos originais, mais os artefatos `COLUNAS_DE_WORKFLOW.txt` e `JUMPER_ACTIONS.txt` (o legado tem um componente chamado **Jumper**). Também consome validação de produto com Ana Lucia.
### Produz para (downstream)
O novo sistema sob medida (**AI HOUSE**) e a migração dos clientes existentes, via "de/para mestre (como era × como fica)" em 3 ondas. Consumidor citado: DesenvolvAI, pelo piloto na NV.
### Módulos relacionados
AI HOUSE (engenharia e destino do modelo) e DesenvolvAI (cliente piloto). ⚠ **Nenhum outro módulo AI é citado nesta página** — nem CriAI, nem CadastrAI, nem EnriqueceAI.
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
- Página "Taxonomia" (Notion `348b1d38e7688087aef7e8a2b64349d0`), lida por inteiro em 04 ago 2026. PO: **João Risoléo**; validação de produto: **Ana Lucia**; engenharia: "time uMode + AI HOUSE". Traz decisões versionadas (`02-premissas` com Premissas P1–P12 rotuladas "regras invioláveis", `04-decisoes-unificacao`, `05-decisoes-remocao`, `06-decisoes-transformacao`). Métricas: 77 campos CORE em ≥3 verticais, 10 campos presentes em todas as 9 verticais, dedupe médio 2,5×.
- ⚠ **~20 subpáginas e ~100 anexos desta página NÃO foram lidos** — inclusive `00-visao-geral.md` e `09-de-para-mestre.md`. Lacuna conhecida, não silenciosa.
- ⚠ **Existe uma segunda taxonomia** na base uMode, com origem e escala diferentes: "TaxonomyAI — Decisão Arquitetural" (Notion `33fb1d38e76881668ab6e516763d703f`) descreve um **serviço** (não um modelo de dados) com taxonomia de 12 zonas / 45 dimensões / 431 valores, baseada em Fashionpedia + Shopify Standard Product Taxonomy. Ver `_pendencias-gerais.md`.
- ⚠ **Ambiguidade de natureza a resolver:** no nosso Portfólio a Taxonomia é uma Solução; na Especificação V1 ela é descrita como **serviço interno do CadastrAI**; e no ÍNDICE MESTRE está no **Domínio 1 (Arquitetura e Estratégia)**, não no Domínio 3 (Produtos uMode). Três fontes, três naturezas.
- ⚠ **Existem duas taxonomias distintas na base uMode, ambas de abril/2026, que nunca se citam:** (1) esta, do PLM padrão — 6.567 campos do uFlow → 2.618 clusters, 9 verticais, PO João Risoléo, validação Ana Lucia, engenharia "time uMode + AI HOUSE"; (2) **TaxonomyAI** (Notion `33fb1d38e76881668ab6e516763d703f`), um **serviço** que recebe imagem + dados do PLM e devolve atributos estruturados por API — taxonomia de 12 zonas / 45 dimensões / 431 valores, baseada em Fashionpedia + Shopify Standard Product Taxonomy, com documento normativo próprio ("Dicionário Oficial de Taxonomia", `33bb1d38e768810db75bcd26f5759c08`, responsável João Ferraz). Bases, escalas, donos e galhos do Notion diferentes. Nenhuma das páginas afirma que são a mesma coisa nem que são diferentes.
- ⚠ Bloqueio declarado pela própria página do TaxonomyAI, sob o título "Decisão pendente antes de construir": "modelo de confiança — quais campos o cadastro PLM sempre prevalece sobre a imagem? Quais a imagem é mais confiável? Sem isso definido, o sistema vai gerar inconsistências silenciosas."
- ⚠ **~20 subpáginas e ~100 anexos da página "Taxonomia" não foram lidos**, inclusive `00-visao-geral.md` e `09-de-para-mestre.md`.
