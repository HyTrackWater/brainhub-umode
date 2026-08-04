# CadastrAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
CadastrAI
### Nome legado
Não descende de ferramenta anterior: **herdou o nome** `CadastrAI`, liberado na sessão de 24/04/2026 quando o antigo "CadastroAI" (módulo de enriquecimento) foi rebatizado para **EnriqueceAI**. O ÍNDICE MESTRE ainda titula a página do produto como "Projeto: CadastroAI", com a descrição já do núcleo de governança — título defasado, conteúdo atual.
### Descrição
**Núcleo de governança e fonte única de verdade do cadastro de produto** — não é módulo no fluxo, é plataforma-núcleo. Tem o miolo CADASTRO e, ao redor, serviços compartilhados: Taxonomia, Permissionamento, Login, Validações, Integrações, política de auditoria e pesos default da Taxonomia. Monitora o ERP em fluxo bidirecional e é **o único que escreve de volta nele**.
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
ÍNDICE MESTRE (Notion `34eb1d38e76881d984b8d3bc10efb095`, lido em 04 ago 2026), Domínio 3: "**Produto em produção.** Núcleo de governança. Clientes âncora: Luiza Barcelos, Reserva", status `ativo`. Corroborado pela Especificação por Módulo V1, que já lhe atribui 4 edge functions no plano de migração para o Hub de Agentes. Traduzido para **Escalável** pela regra travada do protocolo (declaração literal de produção com clientes âncora nomeados). Ressalva registrada na fonte: o modo (c) da política de auditoria é "provavelmente versão posterior".
## Pipeline e relações
### Consome de (upstream)
ERP do cliente (dado bruto, tratado conforme política de auditoria da marca); todos os módulos que devolvem produto enriquecido; EnriqueceAI (descrição gerada).
### Produz para (downstream)
Todos os módulos uMode (PlanejAI, CriAI, DesenvolvAI, FornecAI, EnriqueceAI, GerenciAI) consultam o CadastrAI; escrita de volta no ERP; distribuição para plataformas externas de e-commerce via serviço de Integrações — esta última ainda manual.
### Módulos relacionados
Taxonomia — descrita como serviço dentro do guarda-chuva CadastrAI, "provavelmente um microserviço independente exposto por API", com os módulos consumindo Taxonomia **diretamente** (não precisam pedir ao CadastrAI); Hub de Agentes (agente de auditoria de Taxonomia e `document-extractor` compartilhado com o CriAI); EnriqueceAI (loop fechado).
## Adoção por cliente
Não aplicável — produto interno, usado pela Casa para atender clientes, não contratado
individualmente por eles
### Clientes que contrataram
Luiza Barcelos e Reserva — clientes âncora segundo o ÍNDICE MESTRE. ⚠ A fonte **não qualifica** como `(contratado)` ou `(piloto)`, e o protocolo exige o qualificador; fica pendente de confirmação. ⚠ Isso **contradiz** o `Destino = Interna` registrado na lista travada de `CONTEXT.md`: o ÍNDICE MESTRE classifica o CadastrAI no **Domínio 3 — Produtos uMode**, não no Domínio 4 — Produtos Internos. Não resolvi por conta própria.
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
- ÍNDICE MESTRE (Notion `34eb1d38e76881d984b8d3bc10efb095`), Domínio 3. Página do projeto: `32cb1d38e7688119b873ff0e37d926b5` (não lida).
- "Plano Técnico — Hub de Agentes + Infraestrutura uMode" (Notion `340b1d38e768811fab17ca211fda8ef3`, v3.0 abr/2026), lido em 04 ago 2026: registra que a edge function `process-enrichment` do CadastrAI "tem 1.200+ linhas com lógica de negócio acoplada".
- ⚠ **A grafia nas fontes do Notion é `CadastroAI`**; `CONTEXT.md` grafa `CadastrAI`. Divergência real entre fontes, registrada e não resolvida por conta própria — é o segundo caso do tipo, junto de `FornecAI` × `ForneceAI`.
- Política de auditoria por marca em três modos: (a) flag through (`audit_status = pending`, não vai ao ERP até resolver), (b) quarentena (não entra no CadastrAI), (c) escala (entra com SLA e escalonamento) — "nenhum dos três é 'errado' — é maturidade do cliente". Implicações: coluna `audit_status`, tabela `org_audit_policy`, função compartilhada `canConsume(produto, módulo, política)`.
- Problema-motivador registrado: uma base sanitizada há 2 anos "está uma zona de novo" por falta de manutenção contínua.
