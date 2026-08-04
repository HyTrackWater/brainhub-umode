# EnriqueceAI · Produto

> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue
> `protocolo-gestao-produto.md`. Campo sem fonte explícita fica `[a preencher]` — inclusive
> o score de maturidade, que **não** é escolhido por intuição.

## Identificação
### Nome atual
EnriqueceAI
### Nome legado
**CadastroAI** — o módulo de enriquecimento do desenho original. Literal da fonte canônica: "No desenho original era 'CadastroAI' como módulo de enriquecimento. Foi rebatizado para EnriqueceAI durante esta sessão para liberar o nome 'CadastrAI' para o núcleo de governança." ⚠ **Atenção à nuance:** o EnriqueceAI é o antigo **CadastroAI** renomeado; ele **não** é o `CadastrAI` de hoje, que é outra coisa (o núcleo de governança, que herdou o nome liberado). Os dois itens do Portfólio continuam distintos.
### Descrição
Definição de descrição de produto para ferramentas de e-commerce, a partir de agentes especialistas em SEO com aprendizado. Faz a **finalização do cadastro com base na foto do produto**.
### Destino
Voltada ao cliente
### Área canônica do cliente conectada
E-commerce / Cadastro
### Geração
Nativa

## Maturidade
### Score de maturidade
MVP
### Fonte e data da avaliação
"Arquitetura uMode — Especificação por Módulo (V1 — 24/04/2026)" (Notion `34db1d38e768814b8001d7cb6cacf4e5`), lida em 04 ago 2026. A favor de maturidade alta: seção "Detecção de atributos por imagem (cerne do módulo, **já existe hoje**)" — "a detecção de atributos a partir da foto do produto JÁ EXISTE e é a espinha dorsal do módulo atual". Contra: o push para o canal externo é marcado "**[ROADMAP — não existe ainda]** o push automático para Vtex/plataforma de e-commerce ainda não está implementado. Hoje a descrição volta pro CadastrAI, mas a propagação para o canal externo é manual"; e o gatilho é manual — "não é fluxo automático no lacre. **Usuário clica para gerar**". Além disso não há entrada de projeto para EnriqueceAI no ÍNDICE MESTRE, e "push Vtex" está nas "Pendências honestas". Mantido em **MVP** pela regra travada do protocolo: o cerne roda de verdade, mas a cadeia não está em produção plena. Reavaliar se o status "em produção" do antigo CadastroAI for formalmente transferido para cá.
## Pipeline e relações
### Consome de (upstream)
CadastrAI (produto já passou pela Taxonomia e já tem atributos detectados) e as fotos do próprio produto lacrado — "não imagens de pesquisa, não catálogo de fornecedor".
### Produz para (downstream)
CadastrAI — "devolve enriquecimento pro CadastrAI; o CadastrAI armazena e pode distribuir adiante"; daí para plataformas de e-commerce (Vtex, Shopify etc.) via serviço de Integrações do CadastrAI, hoje manual.
### Módulos relacionados
CadastrAI (loop fechado, e dono da distribuição externa — "distribuição para canais externos é responsabilidade do CadastrAI, não do EnriqueceAI"); Taxonomia; Hub de Agentes, via `product-enricher`, `brand-dna-analyst` e `persona-extractor`.
## Adoção por cliente
### Clientes que contrataram
NV (uso real confirmado em reuniões de jul 2026 — qualificador contratado/piloto a confirmar)

## Marcos
| Data | Evento/decisão | Responsável | Nota |
|---|---|---|---|
| 24/04/2026 | Arquitetura uMode V1 definida em sessão | João Risoléo | 6 módulos no fluxo + CadastrAI (núcleo) + Hub de Agentes (lateral) |
| 03/08/2026 | Registro formalizado no BrainHub | [a preencher] | Primeira vez que este item do Portfólio ganha `produto.md` real |
| 04/08/2026 | Hipótese de renomeação levantada e resolvida na mesma sessão | Vinicius Risoléo | Vinicius suspeitou que EnriqueceAI = CadastrAI renomeado; a Especificação por Módulo V1 confirmou que o EnriqueceAI é o antigo CadastroAI, e que o nome CadastrAI foi liberado para o núcleo de governança — item distinto |

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
- Achado que **resolve a hipótese levantada por Vinicius em 04 ago 2026**: ele suspeitava que "EnriqueceAI substituiu o CadastrAI, é a mesma coisa com nome novo". A fonte canônica confirma metade e corrige a outra: o EnriqueceAI é o antigo **CadastroAI** renomeado na sessão de 24/04/2026, e o nome **CadastrAI** foi liberado nessa mesma sessão para batizar o núcleo de governança — que é item distinto. Ou seja: houve renomeação, mas **não** é "a mesma coisa" que o CadastrAI atual.
- ⚠ Isso também explica a divergência de grafia `CadastroAI` × `CadastrAI` que estava registrada como pendência: **não eram duas grafias do mesmo item, eram dois itens diferentes** — o antigo (hoje EnriqueceAI) e o novo (hoje CadastrAI).
- Briefing de Vinicius Risoléo em 04 ago 2026: descrição funcional (agentes especialistas em SEO com aprendizado, finalização de cadastro a partir da foto) e a hipótese de equivalência com o CadastrAI, que ele mesmo marcou "a confirmar" — **e que foi confirmada com correção na mesma sessão**, ver `Nome legado`.
- ⚠ Vocabulário adjacente, sem valor confirmatório: a página "TaxonomyAI — Decisão Arquitetural" cita um serviço externo `data-enrichment-api` no diagrama do CTO e usa o termo "atributos enriquecidos (JSON)". É vocabulário de enriquecimento, **não** o nome EnriqueceAI.
