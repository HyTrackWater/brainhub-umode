# Pendências gerais — decisões que precisam do Vinicius/CEO

> Documento central de dúvidas levantadas durante varreduras e formalizações. Não é padrão
> final de nenhum cliente/área — é só a lista viva de "o que precisa de confirmação humana
> antes de virar decisão travada". Quando resolvida, uma pendência sai daqui e vira nota no
> documento definitivo (`CONTEXT.md`, protocolo, ou MD do cliente/área correspondente).

> **Nota de processo (13 jul 2026, confirmada pelo Vinicius):** este documento continuará
> crescendo por varredura; em algum momento futuro haverá uma passada dedicada de triagem —
> "o que o CEO precisa responder", "o que Operação precisa completar", etc. — para dar dono a
> cada item abaixo. Essa triagem **ainda não aconteceu**; não atribuir responsável a nenhum item
> por conta própria até lá.

## Portfólio / Ferramentas — nomenclatura legado → novo

10. **`uBuy` ≈ `FornecAI`? Não confirmado — pendência explícita.** Hipótese levantada a partir
    da categoria "COMPRAS" no backlog real de produto (`_varredura-drive-notas.md`), mas o
    Vinicius não confirma: "uBuy era algo próximo a um módulo de gestão de carteira. Não sei se
    o FornecAI tem esse viés." Não presumir a equivalência até confirmação real.
11. **`uRocket`** — produto de mensageria (montagem de campanhas via WhatsApp). **Descontinuado**
    (confirmado pelo Vinicius, 13 jul 2026). Não corresponde a nenhum dos 16 itens do Portfólio
    atual — fica registrado como ferramenta legada encerrada, não como Solução ativa.
12. **`uPick`** — módulo de "apostas" (achado real: aparece como módulo "Apostas" na base
    "Mapa de Clientes"). Se existir equivalente no Portfólio novo, seria `ApostAI` — **não
    confirmado que esse item existe hoje na lista travada de 16** (ver `CONTEXT.md` →
    "Decisão: camada Produto na hierarquia"). Gap real, possivelmente uma área/solução ainda
    sem contraparte formal.
13. **`uTrack`** — descontinuado (confirmado pelo Vinicius, 13 jul 2026). Sem sucessor conhecido.
14. **`uMetrics`** — o Vinicius acha que nunca foi pra frente como produto, mas classificou a
    própria resposta como "achismo" — não tratar como fato confirmado.
15. **`uDash`** — ferramenta legada de relatórios, contratada por Luiza Barcelos (já registrado
    em `institucional.md` dela). Segundo o Vinicius, está caindo em desuso à medida que o novo
    sistema (Portfólio atual) se estrutura — **sem substituto 1:1 confirmado ainda**.
16. **`ISPS`** — aparece uma vez na base "Mapa de Clientes" (combo de módulos de 1 cliente). O
    Vinicius não sabe do que se trata. Não investigado ainda.

## Template de Produto — achados do teste contra dado real (14 jul 2026) — ✅ resolvidos
> Os 4 itens abaixo (17-20) foram decididos pelo Vinicius em 14 jul 2026 e já aplicados em
> `protocolo-gestao-produto.md` e `_template_produto.md` — mantidos aqui só como histórico do
> teste que os originou, não são mais pendência ativa: (17) regra de tradução do Score de
> maturidade travada (produção/piloto/conceito, métrica numérica é só evidência de apoio); (18)
> `Clientes que contrataram` agora exige qualificador `(contratado)`/`(piloto)`; (19)
> `Adoção por cliente` vira "Não aplicável" quando Destino = Interna; (20) Governança separou
> `Owner / Estratégia` de `Operador`.

## Repositórios reais do Portfólio — confirmação manual pendente (14 jul 2026)

21. **Confirmação de repositório real por item do Portfólio — tarefa manual do Vinicius, sem
    prazo definido.** A varredura via Drive já achou repositório próprio pra 9 dos 16 itens
    (PlanejAI, CriAI, DesenvolvAI, VendeAI, CX Hub, Gest Hub, ONB HUB, IntHub, Taxonomia) e não
    achou pra 6 (FornecAI, EnriqueceAI, GerenciAI, AlocAI, CliprocAI, Sales Hub) — candidato a
    maturidade Ideação, não confirmado. O Vinicius vai trazer a confirmação real (quais
    repositórios existem de fato, incluindo os que estão em conta GitHub paralela à principal da
    uMode — sinal adicional de MVP já registrado em `protocolo-gestao-produto.md`) quando puder;
    é atividade manual dele, não retomar a varredura desse ponto sozinho até a devolução chegar.
    Relacionado: item 2 do "Template de Produto" (`catalogcraft-ai`/`umode-catalog-ai` = CadastrAI?)
    e a pergunta 3 sobre `CopAI`/`umode-identidade`/`umode-design-guardian`/
    `journey-insight-whisper`/`u-mode-blueprint` (`_varredura-drive-notas.md`).

## Taxonomia / estrutura

1. **Cadeira (organograma) vs. Área (BrainHub) — não reconciliadas, e agora uma 3ª lista.**
   O organograma real da Casa (Design Org & Metas 2026) usa cadeiras/diretorias próprias (CEO,
   Tecnologia/CTO, Vendas, Marketing, Operações, Produto, Administrativo, Pessoas) diferentes
   das 8 Áreas internas já travadas em `CONTEXT.md` (Comercial, Atendimento, Produto &
   Soluções, Dados & IA, Financeiro, Tecnologia, People, Operações). Ex.: não há "Atendimento"
   como diretoria no organograma — pode estar dentro de Operações. **10 jul 2026:** achado o
   `brainhub_mapa.html` ("BrainHub — Mapa-mãe · uMode", 10/06/2026, o documento mais recente e
   diretamente sobre o BrainHub encontrado até agora), que traz uma **3ª lista** de 8 Áreas
   internas (Comercial/Vendas, Marketing/Growth, Produto, Tecnologia, Financeiro/
   Controladoria, **Jurídico** — não existe em nenhuma das outras duas listas —, CS/
   Atendimento, Cultura/Pessoas), cada uma com chips de atividades típicas e um conceito de
   "uGentes por área" (força de trabalho de IA por cadeira). Por decisão do Vinicius (10 jul
   2026): documentos externos (Drive, decks, mapas do CEO) são **fonte de informação**, não
   fonte de estrutura — a estruturação de referência é sempre o repositório/padrão que estamos
   definindo aqui. As 8 Áreas internas de `CONTEXT.md` **permanecem travadas, não alteradas**.
   Esta pendência registra a existência de 3 taxonomias de área diferentes (organograma,
   BrainHub, Mapa-mãe) para reconciliação futura, se e quando fizer sentido — não é uma fila de
   substituição automática do que já está travado.
2. **`Área (CX Hub)` = "OPERAÇÃO" genérica não tem match no enum documentado.** Só existe
   `Operação | KA` no enum de Área (CX Hub) para o quadro Operação — nenhum valor "Operação"
   puro. Mapeado para `Sem Área` como opção menos distorciva (ver
   `protocolo-gestao-demanda.md`). Avaliar se o CX Hub real precisa desse valor.
3. **`Tamanho atendimento` (CRM, valores P/G) vs. `Grupo de segmentação uMode` (Médios,
   Pequenos etc., já em `institucional.md` de cada cliente)** — não sei se são a mesma escala
   ou classificações diferentes. Registrado como observação em Lofty Style e Cambos, não
   fundido em nenhum dos dois.

## Pessoas

4. **Taís Moser (Luiza Barcelos)** — presente em quase todas as reuniões de onboarding de 2024
   junto com Marina Santoro. Não confirmado se é uMode ou do próprio cliente. Nenhuma ficha de
   Pessoa criada até resolver.
5. **"Laura" na "Alocação contratual (NV)" do organograma (frente CriAI/Tech)** — não confirmado
   se é a mesma Laura Delgado Cardoso (Key Account). Nome comum, sem evidência forte. Não
   fundidas.

## Estrutura de documento

6. **`institucional.md` de Luiza Barcelos tem `### ERP` e `### Notion (cadastro de cliente)`**
   como subseções extras dentro de "Sistemas e fontes de verdade", não previstas no template.
   Pré-existente (não introduzido nesta sessão de varredura). Decisão: formalizar como padrão
   (replicar pros outros 3 clientes) ou remover para bater com o template estrito?

## Dados desatualizados ou conflitantes entre fontes

7. **Status "Onboarding" no CRM "Mapa de Clientes"** (última edição 04/03/2026) aparece para
   Lofty Style e Luiza Barcelos, mas ambos já têm marcos mais recentes indicando fase avançada
   (Operação Assistida / Ongoing) em `jornada.md`. CRM provavelmente desatualizado — não
   corrigido no CRM (fora do nosso escopo de escrita), só não usado como fonte de verdade nos
   nossos MDs.

## Estrutura de documento (achados da auditoria final de 10 jul 2026)

8. ~~`contexto-area.md` das 8 Áreas internas da Casa difere consistentemente do template usado
   pelas 14 Áreas de cliente~~ — **✅ resolvido em 14 jul 2026.** Formalizado como template
   oficial (opção já esperada, sem alterar conteúdo real das 8 áreas):
   `uMode/00_Institucional/_contexto/_template_contexto_area_casa.md`, registrado em
   `CONTEXT.md` → "Áreas internas — nomes". Validado por diff de headings contra as 8 áreas
   reais — 0 divergências.
9. **`contexto-area.md` não existe em nenhuma das 14 áreas de nenhum dos 4 clientes-piloto
   (Lofty Style, Cambos, Luiza Barcelos, Moda Objetiva) — 0 de 14 em cada um, 0 de 56 no
   total.** As pastas `_contexto/` de cada área existem (estrutura de pastas criada na Sessão
   5/7), mas o arquivo em si nunca foi preenchido para nenhum cliente real — só o
   `_template_cliente/` tem os 14 arquivos (vazios com `[a preencher]`, como template deve
   ser). Diferente de `institucional.md`/`jornada.md`/`pessoas.md` (nível Institucional), que
   foram preenchidos com dado real em sessões anteriores. Gap real de conteúdo, não erro desta
   sessão — registrado aqui porque a auditoria final (10 jul 2026) foi a primeira vez que
   alguém checou essa camada especificamente. Preencher exigiria dado real de cada área de cada
   cliente (não temos ainda) — não vou inventar conteúdo para fechar esse gap.
