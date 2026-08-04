# DesenvolvAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
DesenvolvAI
### Nome legado
uFlow (linhagem confirmada por Vinicius Risoléo, 13 jul 2026 — módulo de Gestão de Coleção). Complemento de 04 ago 2026: o uFlow **segue em operação** como a ferramenta de PLM que conduz praticamente todos os contratos, e é o que resume o plano de migração até aqui. No Notion é registrado muitas vezes como **"Gestão de Coleção"** — o de/para de Soluções é justamente o que responde essa equivalência de nomes.
### Descrição
Funil de desenvolvimento: a ficha pré-preenchida do CriAI vira piloto físico, é validada e segue para lacre; ao lacrar, o produto é enviado automaticamente ao ERP via CadastrAI. Modela o produto como **árvore explícita de versões** (V1, V2, … → lacre ou cancelamento com motivo categorizado), não como status.
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
Desenvolvimento de Coleção
### Geração
Nativa

## Maturidade
### Score de maturidade
Escalável
### Fonte e data da avaliação
Uso em produção em escala, medido na planilha "uMode - Controle de Acessos" (Drive `1JsMyuSR3kl0l2AzOGsKikqVNVrBDbhFvgKVhZMYdSWI`, viva — última modificação 03 ago 2026): 1.376 usuários cadastrados em contas de uFlow, 653 com acesso em jul/2026 (65% de engajamento), distribuídos em ~20 organizações — inclui contas nomeadas explicitamente como uFlow (ex.: "Cambos - uFlow"). Também é módulo oficial da V1.

## Pipeline e relações
### Consome de (upstream)
CriAI (ficha pré-preenchida, especificação já resolvida no digital) e FornecAI jornada 1 (fornecedor devolve piloto e orçamento via DesenvolvAI).
### Produz para (downstream)
CadastrAI (produto lacrado → ERP); CriAI (taxa de V1 volta como input do ciclo seguinte); vertical "Desenvolvimento" do AI First (produto em V_n com sinal de morte, queda de V1 por estilista, tempo médio de piloto por fornecedor, concentração de motivo de cancelamento).
### Módulos relacionados
CriAI (acoplados por dado, não só por workflow), FornecAI, CadastrAI, e GerenciAI como consumidor dos eventos.
## Adoção por cliente
### Clientes que contrataram
NV — cliente âncora segundo o ÍNDICE MESTRE do Notion. ⚠ O índice **não qualifica** se é `(contratado)` ou `(piloto)`; o protocolo exige o qualificador, então fica pendente de confirmação. A planilha de acessos mostra ~20 organizações com conta de uFlow, o que indica muito mais que um cliente — a reconciliação conta↔cliente↔módulo continua não feita.
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
- ÍNDICE MESTRE (Notion `34eb1d38e76881d984b8d3bc10efb095`), Domínio 3: "Projeto: DesenvolvAI — Em desenvolvimento ativo. 6 P0s para GTM. Cliente âncora: NV." Página do projeto: `32db1d38e76881779359cd9bc1adde90` (não lida).
- Página "Taxonomia" (Notion `348b1d38e7688087aef7e8a2b64349d0`) registra **NV como cliente piloto do DesenvolvAI** no contexto da migração de taxonomia.
- "Arquitetura uMode — Especificação por Módulo (V1 — 24/04/2026)" (Notion `34db1d38e768814b8001d7cb6cacf4e5`), lida em 04 ago 2026. Motivos de cancelamento são lista controlada (Custo, Tecido, Modelagem, Qualidade, Prazo, Fornecedor incapaz, Decisão comercial, Outro) — "senão os rankings não funcionam". A página declara que "**rankings são a feature comercial**" (de fornecedores e de estilistas). Configuração por marca: stop-loss em N versões e limite de desvio de custo, cada um em modo alerta ou bloqueia — "régua é da marca, não da uMode".
- Briefing de Vinicius Risoléo em 04 ago 2026 sobre o papel atual do uFlow (PLM ativo, conduz quase todos os contratos, aparece no Notion como "Gestão de Coleção").
- ⚠ **Tensão de linhagem a resolver:** o uFlow é ao mesmo tempo (a) o legado de que o DesenvolvAI descende e (b) o legado que a Solução **Taxonomia** declara substituir ("modelo de dados que substitui o legado uFlow", 6.567 campos → 2.618 clusters). Duas Soluções do Portfólio reivindicam relação com o mesmo legado, por ângulos diferentes: DesenvolvAI é o sucessor funcional, Taxonomia é o sucessor do modelo de dados. Registrado sem escolher lado.
