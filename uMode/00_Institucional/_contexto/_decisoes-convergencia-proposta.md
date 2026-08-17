# Convergência com o vault do João — diferenças e decisão proposta

> Para a conversa com o João. **Uma linha por diferença, minha decisão, e o porquê em até 2 linhas.**
> Base: vistoria somente leitura de `BrainHub - João Risoléo` em 04 ago 2026 (1.435 arquivos, 887 MD).
> Detalhe e critério de pronto de cada frente em `_backlog-convergencia-brainhub.md`.

**Não muda nada:** a taxonomia de Área é **idêntica** nos dois (mesmos nomes, mesma numeração) e os
tiers **T0/T1/T2** também. A convergência é de mecanismo, não de hierarquia.

**Cobertura:** li `_CANON.md`, `MANIFEST.md`, o brief para o Hermes e o handoff de 04/08. **Não li**
`DECISOES.md` (156 KB), `_GOVERNANCA.md` (a "constituição do vault") e `SISTEMAS.md` (51 KB) — podem
corrigir o que está abaixo.

---

## Bloqueia o schema

| # | Tema | Como está hoje | Minha decisão | Por quê |
|---|---|---|---|---|
| 1 | **Chave de cliente** | Nossa pasta é nome comercial (`NK STORE`); a dele é slug (`nk-store`) | **Adotar o dele:** pasta = `client_id` | Pasta igual à chave elimina tabela de tradução, e os 23 clientes em comum passam a casar direto. |
| 2 | **Front-matter** | 665 de 884 arquivos dele têm; **0 dos nossos 1.327** | **Adotar** as chaves dele (`origem`, `tipo`, `entidade`, `sync`, `criado_em`, `status`, `versao`) e **manter** o índice derivado | `tipo` e `entidade` não existem em heading nenhum: sem front-matter, migrar exige inferir do caminho. Reverte decisão minha. |
| 3 | **Modelo interno do cliente** | Nós: 14 áreas. Ele: programa/entregável, **zero áreas** | **Manter os dois como eixos ortogonais** — Área classifica, Programa entrega | Nenhum dos dois é redundante; fundir perde informação de um dos lados. |
| 4 | **Nível acima da uMode** | Raiz dele tem `uMode`, `João`, `SoulGames` como irmãos; a nossa **é** a uMode | **Criar o nível no schema**, mas instanciar só a uMode | O banco precisa da tabela; hospedar os outros negócios é decisão de negócio, não de arquitetura. |
| 5 | **Classes de instituição** | Ele tem `alinvest-ift` com contrato e relatórios assinados — não parece cliente de plataforma | **Separar `cliente` de `programa`** como classes distintas | Mentoria e SaaS têm ciclo, entregável e área diferentes; misturar polui as duas listas. |
| 6 | **Enumeração de Área** | Ele tem `_Parceiros` e não tem `05_Financeiro`; nós, o inverso | **Adotar `_Parceiros` e manter `05_Financeiro`** | Parceiro/facção já aparece nas integrações e não tem casa; Financeiro é área viva da Casa. |

## Bloqueia a frota de agentes

| # | Tema | Como está hoje | Minha decisão | Por quê |
|---|---|---|---|---|
| 7 | **`inbox` e promoção** | Nele o agente escreve em `inbox/<agente>/` e só o João promove; aqui eu escrevo direto no canônico | **Adotar** | Escrever direto funciona com um agente disciplinado, não com frota. |
| 8 | **Context Pack** | Ele tem 4 espécies (Agente · Skill · Conhecimento · **Context Pack**); nós, nenhuma formalizada | **Adotar**, começando pelo agente uFlow da `D-2026-002` | O papel e o treinamento dele estão em MDs soltos, e os originais já sumiram do disco uma vez. |
| 9 | **Evidência de execução** | Ele planeja `agent_runs`/`agent_health`; nós não registramos execução | **Adotar** | Sem prova de conteúdo, "rodou" não significa nada — foi o erro que custou semanas a ele. |

## Bloqueia confiança no dado

| # | Tema | Como está hoje | Minha decisão | Por quê |
|---|---|---|---|---|
| 10 | **Registro de decisões** | As dele são citadas por número no código (`D11`, `D47`, `D67`); nosso `CONTEXT.md` não é citável | **Criar registro numerado, faixa a partir de `D200`** | Ele já usa D1–D67; faixa separada evita colisão sem renumerar ninguém. |
| 11 | **Fonte canônica declarada** | `MANIFEST.md` dele declara o canônico de cada bloco e quem consome; nós não declaramos | **Adotar** | É a tabela de procedência do banco; hoje não sabemos qual arquivo é canônico para qual fato. |
| 12 | **Asserção de fato** | `_CANON.md` dele é legível por máquina e um script cobra; nós validamos só estrutura | **Adotar** | Validamos heading e nunca fato — os números que já erramos passariam de novo. |
| 13 | **Publicação / sync** | `SYNC_EXCLUDE.md` decide o que sobe; nós não temos modelo de publicação | **Adotar** | Confidencialidade por sincronização resolve, de passagem, o T1 da Cambos aberto desde julho. |

## Completa o modelo

| # | Tema | Como está hoje | Minha decisão | Por quê |
|---|---|---|---|---|
| 14 | **Programa e Projeto** | Ele tem `programa-2026/`; o CX Hub tem `Programa → Projeto`; nós não temos nenhum | **Criar as duas entidades, vínculo opcional** | Confirmado por duas fontes independentes; sem elas não há agregação por programa. |
| 15 | **Nome de arquivo** | Ele usa `<slug>_<YYMMDD>_<assunto>.md`; nós usamos nome semântico | **Manter o nosso para contexto; adotar o dele só para artefato datado** | Contexto estável não deveria carregar data no nome; artefato deveria. |
| 16 | **Crosswalk repo ↔ produto** | O `MANIFEST.md` dele já resolve o que era pendência nossa | **Importar o dele como canônico** | Já validado com o João, e confirma de forma independente que `catalogcraft-ai` = EnriqueceAI. |
| 17 | **Disposição e tombstone** | Ele tem 6 disposições finais e tombstone para tudo rejeitado; nossas 148 pendências não têm estado | **Adotar as 6 disposições** | 148 pendências sem estado nem owner são uma fila, não um backlog. |

---

## Não é minha decisão — preciso de vocês dois
1. **Item 4** — o BrainHub da uMode hospeda `João` e `SoulGames`? É decisão de negócio.
2. **Item 10** — a faixa `D200` precisa do aval do João para não colidir com a numeração dele.
3. **Item 5** — "cliente × programa" é **hipótese minha** a partir do `alinvest-ift`, não fato lido.
4. **Item 2** — reverte uma decisão que eu já havia travado; quero o aval explícito.
5. **Item 13** — a autorização de uso do conteúdo T1 da Cambos continua pendente desde julho.

## O que eu faria primeiro, se fosse só comigo
**Itens 1 e 16.** O 1 destrava toda reconciliação e não depende de ninguém; o 16 é o mais barato de
todos e fecha várias pendências nossas de uma vez.

## Governança
### Quem pode alterar este documento
CEO (João Risoléo). Decisão de Vinicius Risoléo em 04 ago 2026: **no BrainHub, somente o CEO altera**.
