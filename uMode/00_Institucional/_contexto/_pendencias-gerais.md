# Pendências gerais — decisões que precisam do Vinicius/CEO

> Documento central de dúvidas levantadas durante varreduras e formalizações. Não é padrão
> final de nenhum cliente/área — é só a lista viva de "o que precisa de confirmação humana
> antes de virar decisão travada". Quando resolvida, uma pendência sai daqui e vira nota no
> documento definitivo (`CONTEXT.md`, protocolo, ou MD do cliente/área correspondente).

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

8. **`contexto-area.md` das 8 Áreas internas da Casa difere consistentemente do template usado
   pelas 14 Áreas de cliente** — mesma divergência nas 8, sem exceção: "Como trabalham"/"O que
   não fazem" (3ª pessoa, template de cliente) vira "Como trabalhamos"/"O que não fazemos" (1ª
   pessoa, faz sentido para área interna da própria Casa); a seção `## Produto conectado`
   inteira não existe nas 8 áreas da Casa; e `### Responsável na empresa cliente` +
   `### Responsável de atendimento (uMode)` (2 campos, um por lado) vira só
   `### Responsável pela área` (1 campo, sem "lado cliente" porque não existe). Consistência
   perfeita nas 8 sugere decisão deliberada de uma sessão anterior, mas **nunca foi formalizada
   como um template próprio** (`_template_contexto_area_casa.md` ou similar) — hoje o único
   template escrito em disco é o de cliente, e a Casa diverge dele sem documento-fonte. Decisão
   pendente: formalizar o variante da Casa como template oficial (replicando a mesma estrutura
   já usada nas 8, sem alterar conteúdo real) ou conformar as 8 áreas da Casa ao template de
   cliente (o que exigiria inventar "Produto conectado" e "Responsável na empresa cliente" para
   áreas que não têm cliente — parece semanticamente errado).
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
