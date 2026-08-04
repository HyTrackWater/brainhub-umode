# FornecAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
FornecAI
### Nome legado
[a preencher — hipótese uBuy ≈ FornecAI levantada e NÃO confirmada pelo Vinicius, ver _pendencias-gerais.md item 10]
### Descrição
Ambiente do fornecedor, com três jornadas: (1) **Desenvolvimento** — recebe ficha técnica, faz piloto e orçamento; (2) **Operação** — portal recorrente com produtos ativos, mostruário, produção, status de pedidos e comunicação com a marca; (3) **Catálogo Reativo** — fornecedores sobem catálogos na mesma Taxonomia e a marca consulta em tempo real quem tem produto para a necessidade detectada.
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
Compras / Supply / Sourcing
### Geração
Nativa

## Maturidade
### Score de maturidade
Ideação
### Fonte e data da avaliação
"Arquitetura uMode — Especificação por Módulo (V1 — 24/04/2026)" (Notion `34db1d38e768814b8001d7cb6cacf4e5`), lida em 04 ago 2026. O título da própria seção é "Módulo 4 — ForneceAI (**em discussão na sessão**)"; as subseções são rotuladas "Implicações técnicas (**preliminares**)" e "Modelo de negócio — Híbrido com Network Effect", que abre com "**Hipótese central:**". Há bloco "Pendências para o time técnico" (esquemas de conta, permissionamento cruzado, pricing, UX dual, fornecedor convidado não-pago), e a skill `umode-arquitetura-tese` lista "FornecAI pricing" nas "Pendências honestas — não vender hipótese como decisão". **Não há entrada de projeto para FornecAI no ÍNDICE MESTRE**, nem no Domínio 3 nem no 4. Mantido em **Ideação** pela regra travada do protocolo: existe desenho e modelo de negócio, mas declaradamente como hipótese em discussão.
## Pipeline e relações
### Consome de (upstream)
CriAI (ficha técnica, jornada 1); Taxonomia (indexa os catálogos de fornecedor); GerenciAI (necessidade de estoque detectada loja a loja alimenta a consulta reativa).
### Produz para (downstream)
DesenvolvAI (piloto e orçamento devolvidos); pedido reativo ao fornecedor; vertical "Oportunidade de negócio" do AI First, que "nasce aqui".
### Módulos relacionados
Taxonomia (declarada como a razão de ela ser inegociável e transversal); GerenciAI, que precisa expor função tipo `buscar_oferta_compativel(demanda_loja, atributos, prazo)`; CriAI; DesenvolvAI.
## Adoção por cliente
### Clientes que contrataram
Nenhum — produto ainda não nasceu

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
- ⚠ **Contradição de grafia dentro da própria fonte canônica:** o cabeçalho da seção escreve "ForneceAI" e o corpo do mesmo documento escreve "FornecAI" em todas as demais menções. Isso **fecha a pendência de grafia** que estava aberta: a fonte canônica é inconsistente consigo mesma, e o ÍNDICE MESTRE grafa "FornecAI" — a mesma grafia de `CONTEXT.md`.
- ⚠ Implicação estratégica registrada na sessão: transforma a uMode "de 'SaaS B2B vendido marca por marca' em plataforma com dois lados", exigindo capacidade dedicada a fornecedor — "o time de implantação atual (Fernanda, Victor) atende marca". Decisões técnicas: dois tipos de conta com schemas distintos (`brand_organization`, `supplier_organization`) — "não é um único `organizations` com flag"; tabela N:N `brand_supplier_relations`; catálogo do fornecedor é dual (parte privada sob NDA implícito + parte pública reativa).
