# CriAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
CriAI
### Nome legado
[a preencher]
### Descrição
Criação de roupas a partir de referências, via ferramentas de IA. Direcionada principalmente à **equipe de Estilo** do cliente. Tem uma versão em produção atendendo o cliente final e sendo comercializada, e versões internas (**CriAI 2, 3 e 4**) que são evoluções de features a serem incorporadas ao módulo de produção.
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
Estilo / Criação
### Geração
Nativa

## Maturidade
### Score de maturidade
Escalável
### Fonte e data da avaliação
Briefing de Vinicius Risoléo em 04 ago 2026: "do novo portfólio, temos o CriAI já com uma versão em produção para atender diretamente ao cliente final (...) dos IAs é o mais maduro, pois tem versão em produção e sendo comercializada com clientes, mas tem outras versões que serão evoluções de features que serão adicionadas ao módulo de produção." Traduzido para **Escalável** pela regra travada do protocolo (produção real com comercialização). ⚠ **Divergência de fonte não resolvida:** o ÍNDICE MESTRE do Notion (26/04/2026, atualizado 28/05/2026) classifica o CriAI como "em especificação", status `em construção`. As duas afirmações são de datas diferentes — a de agosto é mais recente e vem de quem, pelo protocolo, tem autoridade sobre Score de maturidade — e a do Notion **não foi alterada por conta própria**.
## Pipeline e relações
### Consome de (upstream)
PlanejAI (mix sugerido / briefing, com atributos e quantidades por caixinha); Taxonomia (extração de atributos de cada imagem); pesquisa própria via extensão Chrome e upload manual; DesenvolvAI (taxa de aprovação V1 volta como sinal).
### Produz para (downstream)
DesenvolvAI (ficha pré-preenchida); produtos em desenho, looks combinados e try-on; sinal contínuo de planejado vs realizado que alimenta a vertical "Criação" do AI First.
### Módulos relacionados
As versões internas CriAI 2, 3 e 4 são evoluções de feature do mesmo módulo, não itens separados do Portfólio — **não abrem 17º item na lista travada**.
## Adoção por cliente
### Clientes que contrataram
[a preencher]

## Marcos
| Data | Evento/decisão | Responsável | Nota |
|---|---|---|---|
| 24/04/2026 | Arquitetura uMode V1 definida em sessão | João Risoléo | 6 módulos no fluxo + CadastrAI (núcleo) + Hub de Agentes (lateral) |
| 03/08/2026 | Registro formalizado no BrainHub | [a preencher] | Primeira vez que este item do Portfólio ganha `produto.md` real |
| 04/08/2026 | Maturidade confirmada como Escalável | Vinicius Risoléo | Versão em produção e comercializada ao cliente final; CriAI 2, 3 e 4 são evoluções internas de feature do mesmo módulo |

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
- ÍNDICE MESTRE (Notion `34eb1d38e76881d984b8d3bc10efb095`), Domínio 3: "Projeto: CriAI — Canvas criativo + coleta de referências. **Em especificação**", status `em construção`. ⚠ Isso **contradiz** o estágio informado por Vinicius em 04 ago 2026 (versão em produção e comercializada); o índice é de 26/04/2026 com atualização em 28/05/2026, anterior à informação de agosto. Registrado sem escolher lado no campo de maturidade — ver `Fonte e data da avaliação`.
- "Plano Técnico — Hub de Agentes" (Notion `340b1d38e768811fab17ca211fda8ef3`): 3 personas hardcoded em `useAgents.ts` a extrair para banco; "Este projeto CriAI não será alterado até que o Hub esteja operacional".
- "Arquitetura uMode — Especificação por Módulo (V1 — 24/04/2026)" (Notion `34db1d38e768814b8001d7cb6cacf4e5`), lida em 04 ago 2026. Decisão registrada: "Auditoria em tempo real é feature do CriAI, não só do CadastrAI". A extração de atributos das imagens de pesquisa "é cobrada — usuário precisa selecionar (não roda em massa automaticamente)". Loop com DesenvolvAI: estilista com baixa taxa de V1 "pode ter briefing endurecido".
- ⚠ **A funcionalidade de try-on aparece aqui, no CriAI** (agente `tryon-stylist`), e não no VendeAI. Ver a nota correspondente na ficha do VendeAI.
