---
aliases:
  - "Pendências gerais — decisões que precisam do Vinicius/CEO"
tags:
  - tipo/autoridade
  - casa
---
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

## § 0 · TRIAGEM — 23 set 2026

> 🔴 **Este arquivo tem 557 itens e virou ilegível como fila de trabalho.** Esta seção existe
> para dizer **o que é para agora** sem mover nada de lugar. **Nenhum item foi apagado ou
> renumerado** — histórico de pendência não se reescreve.
>
> **Motivo, dito sem rodeio:** eu gerei pendência mais rápido do que fechei. 557 itens abertos e
> a CAEDU — o cliente com prazo — ainda com 158 lacunas de contexto e 100 fichas sem cargo.
> **Estava medindo as fontes em vez de preencher as entidades.**

### 0.1 · O placar

| Balde | Itens | O que fazer |
|---|--:|---|
| ✅ **Já resolvidos** | **50** | nada — ficam como histórico |
| 🚨 **Segurança** | **18** | 🔴 **rotação é ação do Vinicius**, não minha |
| 🔵 **Citam a CAEDU** | **37** | destes, **~12 travam de verdade** (§ 0.2) |
| 🔴 **Decisão do Vinicius** | **50** | fila em `_perguntas-para-o-vinicius.md` |
| ⚪ **Arquivo / técnico** | **402** | **não é para agora** — contexto de produto, banco e processo |

### 0.2 · 🔵 O que trava a CAEDU — a lista curta

**Dos 37 que citam a CAEDU, estes são os que impedem dizer "CAEDU contextualizada".**
Os outros 25 são informativos, já respondidos, ou são de outro cliente com a CAEDU citada de passagem.

| # | O que é | Quem destrava |
|--:|---|---|
| **500** | **não existe `integracao.md`** — e integração é a dor nº 1 da conta | 🟢 **eu, agora** |
| **499** | 3 arquivos de CAEDU em `Downloads` nunca abertos | 🟢 **eu, agora** |
| **495** | `VERÃO 26/27` e `VERAO 26/27` são duas coleções na base para uma no mundo | 🟢 eu, mas precisa de aval |
| **308 · 557** | 🔴 **as atas estão em TRÊS acervos que não se falam** — 35 nesta base × ~47 na página. **Não sei o total real** | ⚠ fonte |
| **313** | sub-página `Fornecedores da Caedu` devolve **404** por este conector | ⚠ acesso |
| **312** | o `Manual do Cliente` é de **24/08/2023** e descreve módulos que mudaram | ⚠ fonte |
| **304** | só **uma** pessoa da Qualidade tem acesso à plataforma | ⚠ confirmar |
| **301 · 311 · 427 · 492 · 494** | 🔴 **a hierarquia `Griffe › Linha › Grupo › Subgrupo`** — **já medida: não aninha como árvore**, é matriz esparsa. Falta **decidir** se tratamos como 4 eixos ou cascata | 🔴 **Vinicius** |
| **503** | a CAEDU está como **`SMB`** e isso contradiz o porte (100+ lojas) | 🔴 **Vinicius** |
| **297 · 298 · 299 · 300** | cláusulas do contrato: desligamento do uFlow em 12 meses · saída em 3 meses · dev emprestado · **Escopo 2 confidencial** | 🔴 **Vinicius** |

🔴 **Resumo:** **2 eu resolvo sozinho · 3 dependem de fonte ou acesso · 7 dependem de decisão sua.**
**Nenhum deles depende de abrir mais fonte no Notion.**

### 0.3 · A regra que passa a valer

🔴 **Não abrir fonte nova enquanto a CAEDU não fechar.** O que sobra no Notion — 25 páginas de
clientes em `Churn`, 30 documentos do CX arquivado, ~40 páginas técnicas do `Setup - PLM` —
**não serve à CAEDU**. Fica registrado, esperando.

🔴 **E a métrica que passa a ser reportada é COMPLETUDE, não contagem de arquivo.**
Hoje: **CAEDU 0 de 259** — 158 lacunas de contexto + 100 cargos + 1 `integracao.md`.
**Arquivo criado não é contexto. Campo preenchido é.**

## Portfólio / Ferramentas — nomenclatura legado → novo

22. **`CliprocAI` confirmado real — achado em 14 jul 2026, pasta Drive da Cambos**
    (`CONTEXTO_CAMBOS.md`/`CONTEXTO_CAMBOS_FATOS.md`). CLIente × PROduto × CAnal. Cambos é
    cliente piloto, mesmo padrão ADR-006 do VendeAI: **fora da Arquitetura V1 oficial até
    validação** — maturidade real = MVP, não Escalável. PRD v1.6 (17 ADRs), protótipo navegável
    com dado real (zero mock), meta de piloto ≥25% conversão em 90 dias. Repositório não está na
    pasta-mãe GitHub principal — vive só na pasta Drive do cliente (`CliprocAI_Prototype/`).
    **⚠ Confidencialidade real, não presumida:** a fonte se autodeclara "T1 — restrito (contém
    custo/margem; time do projeto; NÃO sincroniza Drive/Notion do time)". Não usei nenhum dado
    comercial sensível (faturamento, custo, margem, CNPJ) nem vou usar sem autorização explícita
    do Vinicius — só o metadado de status do módulo (não sensível) foi registrado aqui.
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

## Replicação total — achados de 03 ago 2026

23. **9 nomes existem na pasta Drive "Clientes" mas não têm linha no CRM "Mapa de Clientes":**
    `Alpargatas` · `Polenectar` · `Genuo` · `Grupo Veste` · `Notre Dame` · `Arezzo` ·
    `Posthaus` · `Esposende` · `Lupo`. Todos têm nome de marca de moda (diferente de
    `Kaizen`/`CrossX-JUMP3R`/`MBS-3-Mentorias`/`ALINVEST-IFT`/`Marcio Delbin (Tetris)`/
    `NV-Vinicius`, que aparentam ser outros negócios do CEO). Pela regra travada de que o CRM é
    a única fonte de "quem é cliente", **nenhum deles virou casa de cliente**. Hipóteses não
    confirmadas: prospect/proposta, cliente anterior ao CRM atual, ou pasta de análise.
    **Pergunta ao Vinicius:** algum desses é cliente uMode de verdade? Ver
    `_lista-clientes-reais.md`.
24. **`Status` do CRM tem 2 valores fora do enum do nosso template de `institucional.md`:**
    `Regime CS` (11 clientes) e `Negociação` (1 cliente — Hering). O enum do template é
    `Inativo / Pré Onboarding / Operação Assistida / Onboarding / Sem CS / Ongoing / Churn`.
    Registrado literalmente como está na fonte, com aviso no próprio arquivo — **nenhuma
    equivalência foi presumida** (a suspeita de que `Regime CS ≈ Ongoing` já estava registrada
    em Cambos desde 10 jul 2026, também sem confirmação). **Decisão pendente:** o enum do
    template ganha esses 2 valores, ou existe tradução oficial?
25. **`Área Responsável` = `INOVAÇÃO / IA` (4 demandas) não tem correspondência no enum de
    `Área (CX Hub)`.** É ambíguo entre os dois quadros (Operação tem `Produto | Inovação`, Tech
    tem `Inovação`) e o "/ IA" não existe em nenhum. `Quadro`/`Área (CX Hub)` ficaram
    `[a preencher]` nessas demandas, com o valor legado preservado em `Notas internas`.
    Registrado em `protocolo-gestao-demanda.md`.
26. **Enum de `Prioridade` pode estar incompleto:** a fonte traz `Criticidade = Baixa` (6
    demandas), e o enum só tem `Média`/`Alta`/`Urgente`. Ficou `[a preencher]` com o valor bruto
    preservado — forçar para `Média` inventaria uma prioridade que a fonte não afirma.
    **Decisão pendente:** o CX Hub real tem um valor abaixo de `Média`?
27. **1 RFI da própria Casa uMode não tem onde viver.** A base de RFIs traz
    `uMode | RFI : Escopo - Compilar Alertas de Integração` (ID 72) **sem cliente associado**.
    `protocolo-gestao-rfi.md` trava que `_rfis/` existe só do lado de cliente, porque "RFI sempre
    se refere a um cliente específico". Essa linha contradiz a premissa. Não foi formalizada
    (nem inventei um cliente pra ela). **Decisão pendente:** é erro de cadastro no Notion (falta
    preencher o cliente) ou existe RFI interna de verdade — e nesse caso o protocolo muda?
28. ~~**Todas as fontes disponíveis hoje são snapshot de 05 mar 2026**~~ — **✅ resolvido no mesmo
    dia (03 ago 2026), 2ª rodada.** O Vinicius questionou a premissa: se a fonte de jul 2026 gerou
    os 4 pilotos, ela existe. Existia mesmo — **commitada no Git na Sessão 22 e removida na Sessão
    23** (commit `8c6705b`), portanto recuperável do histórico (`git archive 8c6705b^`). Todas as
    demandas e RFIs dos clientes não-piloto foram **regeneradas** dessa fonte. Ganho real:
    demandas não-piloto de 649 → **757** (+108: Reserva 111→120, Osklen 93→117, NV 95→108,
    NK STORE 74→87, VIX 52→70, Lenny 59→69, Caedu 18→26, Oficina Reserva 23→28, Baw 15→18,
    Plie 12→16, Puket 15→16); RFIs não-piloto de 40 → **63**. Os arquivos dos pilotos continuam
    sem regeneração (Lofty tem narrativa de export HTML que o CSV não traz) — receberam
    **retrofit** dos campos novos. ~~Fica valendo só o resíduo: um re-export em ago 2026 traria o que aconteceu entre jul e ago 2026.~~
    **✅ Resíduo fechado em 03 ago 2026 pela leitura da base viva no Notion:** ela tem 1.010 demandas
    contra 1.007 do export, **apenas 1 criada depois de 14/jul**, e a mais recente é de 15/jul/2026.
    Não há defasagem material — a base está quieta desde meados de julho.
29. **Narrativa de demanda: resolvida só para Lofty Style; segue `[a preencher]` nos demais.**
    O export de jul 2026 tem markdown por página para **85 demandas — todas de Lofty Style**. A
    coluna `Texto` do CSV (corpo da página) vem preenchida em **2 de 1007** linhas. Ou seja: a
    limitação não era o snapshot, é o próprio export — o Notion só materializa corpo de página
    quando o export é feito por página, e isso só foi feito para Lofty. **Ação pendente:** export
    em HTML/markdown por página das demandas dos outros clientes.
    **Já resolvido para RFI:** o export de jul tem 86 markdowns de RFI cobrindo todos os clientes
    — 84 das 85 RFIs formalizadas têm narrativa real (tabela de escopo, "De Acordo", anexos
    citados). A única sem é a `Reservado - Colmeia` (ID 16), cujo markdown não traz corpo.
30. **Participantes de reunião não foram classificados uMode × cliente.** A base "Reuniões
    Compartilhadas com Clientes" mistura os dois lados no mesmo campo. Em `pessoas.md` de cada
    cliente com reunião, os nomes ficaram registrados como **pista explicitamente não
    confirmada**, nunca como dado de pessoa — mesma cautela do caso Taís Moser (item 4). São
    ~670 registros de participação; classificar exige confirmação humana.
31. **`Aliases de áreas` está vazio nos 42 clientes novos.** O CRM não tem campo de alias — é
    dado de kick-off/reunião. Os 4 pilotos têm porque foram levantados a mão. Sem fonte
    estruturada, não foi preenchido.

## Replicação total — achados da 2ª rodada (03 ago 2026, fonte de jul 2026)

32. **`Responsabilidade` é a candidata mais forte a virar campo próprio da Demanda.** É a única
    coluna do export **100% preenchida** (1007 de 1007): `Demanda com uMode` (920) ×
    `Demanda Pendente do Cliente` (87). Diz de que lado a bola está — informação que nenhum campo
    nosso carrega hoje. Está preservada em `### Notas internas` de todas as 993 demandas, no bloco
    de campos legados. **Decisão do Vinicius/CEO:** promover a campo próprio (e retrofitar as 993)
    ou deixar como nota?
33. **Enum de `Motivo de bloqueio` está incompleto em relação ao uso real.** Dos 6 valores de
    `Bloqueio` na fonte, só `Aguardando o Cliente` tem equivalente. Os outros 5 foram para `Outra`
    com o valor original visível: `Aguardando Recurso Especial` · `Aguardando Time Interno - uMode`
    · `Aguardando momento oportuno` · `Mudança de Priorização - Item urgente na frente!` ·
    `Ordem da Diretoria - Não faremos isso nesse momento`. Faltam ao menos "aguardando time
    interno" e "repriorização". Ver `protocolo-gestao-demanda.md`.
34. **10 demandas na fonte não têm cliente nenhum** (IDs UMD-674, UMD-836, UMD-986, UMD-1019,
    UMD-1028 e outras). Não foram formalizadas: sem cliente, não há casa onde viver, e a Casa uMode
    só recebe as que estão explicitamente marcadas como `uMode` (4 delas, já formalizadas em
    `uMode/00_Institucional/_demandas/`). **Decisão pendente:** é falta de preenchimento no Notion,
    ou são demandas internas que deveriam estar marcadas como `uMode`?
35. **2 RFIs legadas eram multi-cliente e foram desdobradas** conforme a regra já travada ("RFI é
    sempre de 1 cliente só"): ID 94 (`Reserva/Oficina | RFI: Escopo - Campo de Coleção por
    Variante`) → uma RFI em Reserva + uma em Oficina Reserva; ID 79 (`Lofty/NK/Geral | RFI :
    Escopo - Custo dinamico`, marcada como `uMode + Lofty Style`) → o lado Lofty existe, **o lado
    uMode não tem onde viver** (mesmo caso do item 27). Cada arquivo desdobrado avisa no próprio
    corpo que compartilha o `ID legado` com o par — não é duplicidade.
36. **`RFI vinculada` só resolve para 44 das 993 demandas** — é o que a fonte tem (a coluna `RFI`
    vem preenchida em 44 linhas). Dessas, 44 casaram com uma RFI formalizada do mesmo cliente
    (37 nos clientes novos + 7 nos pilotos, via retrofit). O caminho inverso (`RFI.Demanda
    relacionada`) continua com a dívida já conhecida do Notion legado: na maioria das RFIs esse
    campo traz o **nome do cliente**, não o ID de uma demanda. Agora que os dois lados existem
    formalizados, a reconciliação virou tarefa possível — antes não era.


## Indexação / arquitetura de dados (achados da auditoria de 03 ago 2026)
> Medição completa em `_auditoria-indexacao.md`.

37. ~~**Não existe identificador estável de cliente — a chave é o nome da pasta.**~~ — **✅ RESOLVIDO em 03 ago 2026:** criado `### ID do cliente` (slug estável) no template, no `protocolo-criacao-cliente.md` e nos 46 clientes. `NK STORE`/`NK Store` colapsam em `nk-store`, então variação de caixa/acento deixou de ser problema; apelidos que não colapsam viraram `### Aliases do cliente`, extraídos dos títulos de RFI e da pasta do Drive. O `client_id` é a chave de todas as tabelas de `_indice/`. Enunciado original abaixo, como registro do risco que existia: Funciona hoje
    (auditoria: 0 falhas em 1.055 referências resolvidas), mas renomear um cliente quebraria os
    vínculos **em silêncio**: `NK STORE` → `NK Store` invalidaria 87 referências de demanda sem
    gerar erro. Vale para qualquer mudança de nome comercial, e para nomes já delicados
    (`Básico&Co`, `Simples (by Reserva)`, `NTK ` — que tem espaço no fim no CRM).
    **Decisão do Vinicius/CEO:** criar um `client_id` estável agora (barato) ou aceitar o risco até
    a migração para banco (`CONTEXT.md` → "Banco de dados")?
38. ~~**A indexação é derivável por convenção, não declarada.**~~ — **✅ DECIDIDO E APLICADO em 03 ago 2026: índice derivado, não frontmatter.** Criado `_indice/` (`clientes.csv`, `demandas.csv`, `rfis.csv`, `pessoas.csv`) gerado por `scripts/gen-indice.ps1` a partir dos MDs — aditivo, reversível, sem tocar em nenhum arquivo do cérebro. Frontmatter recusado: criaria duas fontes de verdade para o mesmo campo. Enunciado original abaixo: Nenhum dos 1.291 `.md` tem frontmatter
    ou qualquer metadado estruturado — todo campo é texto sob um heading, e a indexação funciona
    porque a posição do heading é rígida e está 100% cumprida. Isso já sustenta consulta agregada
    (testado: "demandas de Osklen por status", respondida sem índice auxiliar). **Decisão pendente:**
    quando for ligar RAG/agentes de verdade, gerar um **índice derivado** (ex.: `_indice/` com
    JSON/CSV produzido por script a partir dos MDs, MD continuando fonte de verdade) ou introduzir
    frontmatter nos MDs? A primeira opção não mexe em nada do que já está padronizado; a segunda
    mudaria 1.291 arquivos.
39. **Os eixos Área e Solução estão vazios — é o que impede os agentes Por Área e Por Solução.**
    Medido: `Destino (organizacional)` preenchido em **0 de 993** demandas (não é derivável de campo
    do CX Hub, regra travada na Sessão 17 — exige conhecimento institucional humano);
    `contexto-area.md` de cliente **0 de 644**; ~~`produto.md` real 0 de 16~~ (**✅ 16 de 16 em 03 ago 2026** — varredura geral criou os registros, com maturidade preenchida só onde a fonte declara);
    `Contexto consultado`/`impactado` **0 de 993** (o ciclo de aprovação de contexto não tem dado
    nenhum); `Demanda mãe`/`filhas` **0 de 993**. O eixo Cliente, em contraste, está denso e
    resolvível. **Consequência prática:** um agente Por Cliente já responde com substância hoje; um
    agente Por Área/Por Solução responderia quase nada. Preencher esses eixos é trabalho de conteúdo
    (humano ou nova fonte), não de estrutura.




## Varredura geral de ferramentas/produtos/áreas (03 ago 2026)
> Medição e achados completos em `_varredura-ferramentas-produtos-areas.md`.

40. **A plataforma tem conta ativa de ~18 organizações que o CRM não conhece.** Achado na planilha
    viva "uMode - Controle de Acessos" (Drive `1JsMyuSR3kl0l2AzOGsKikqVNVrBDbhFvgKVhZMYdSWI`,
    modificada em 03 ago 2026): `ALADIM DECOR V2` · `Beira Rio` · `Dakota` · `Grendene` ·
    `Via Marte` · `Nanaminze Varejo` · `Feira Ópera` · `Fluxx Moda` · `Formitz Confecções` ·
    `FOUR ONE` · `Makor SA` · `Meta` · `OPERA KIDS` · `Planifiquese` · `RIBEIRO E PAVANI` ·
    `Shopping Mamãe Cheguei` · `Tempo de Criança` · `Trama Jeans`. Várias são marcas grandes e
    reconhecíveis do setor. **Nenhuma virou casa** — o CRM segue como única fonte de "quem é
    cliente". Mas isso é sinal mais forte que o do item 23 (nome só na pasta do Drive): aqui existe
    **conta com usuários na plataforma**. **Pergunta ao Vinicius:** são clientes, contas de
    demonstração, ou legado de outro produto (ex.: uRocket)?
41. **Existe dado de engajamento real por cliente e não temos campo para ele.** A mesma planilha
    traz usuários cadastrados × usuários com acesso no mês, por cliente (ex.: Vix 88%, Cambos-uFlow
    80%, Luiza Barcelos 74%, StudioZ 0%, 4takes 5%). É o primeiro indicador de **saúde de conta** que
    aparece em qualquer fonte. Candidato natural a `jornada.md`, que hoje não tem nada equivalente.
    **Não aplicado** — criar campo é mudança de estrutura e exige validação.
42. **4ª taxonomia de "área" encontrada: perfil de acesso da plataforma.** A planilha traz perfis por
    cliente (ex.: `Lofty - Estilo`, `Lofty - Modelagem`, `Lofty - PCP`, `Lofty - Ficha Técnica`,
    `Lofty - Compras MP`, `Lofty - Compras Importado`, `Lofty - Planejamento`, `Lofty - Admin`,
    `API`), com nome e e-mail de cada usuário. Diferente das outras três (organograma × 8 Áreas
    internas × Mapa-mãe), **esta mapeia quase 1:1 para as 14 áreas canônicas de cliente** — é a
    fonte mais promissora já encontrada para preencher `contexto-area.md` (0 de 644) e completar
    `pessoas.md` de cliente. **Não aplicado nesta rodada.**
43. **O Notion é a fonte de verdade canônica declarada — e nunca foi lido.** O documento de
    arquitetura do CEO diz literalmente: *"se contradição entre este arquivo e a página V1 → página
    V1 vence"*. Alvos nomeados: página "Arquitetura uMode V1"
    (`34db1d38e768814b8001d7cb6cacf4e5`), skill `umode-arquitetura-tese`
    (`34db1d38e768819abc2dc7844ff2be59`), Plano Técnico do Hub de Agentes ("AGENTES E PROJETOS /
    Produtos Internos"), Modelo PLM Padrão / `CadastrAI taxonomia_v1` (12 premissas, 6 categorias,
    9 verticais). **✅ RESOLVIDO em 03 ago 2026:** acesso confirmado ao workspace real e a **página V1 foi lida na
    íntegra** (51 KB). Decidiu a maturidade de PlanejAI, EnriqueceAI e GerenciAI, validou 100% da
    nossa tabela de tradução de status contra o schema vivo, e rendeu as pendências 47-50. Seguem
    não lidos: a skill `umode-arquitetura-tese`, o Plano Técnico do Hub de Agentes e o
    `CadastrAI taxonomia_v1`.
44. **`AlocAI` não tem nenhuma evidência em fonte alguma.** Não está no fluxo da Arquitetura uMode
    V1, não tem repositório localizado, não aparece em documento, reunião, PRD ou conta de acesso.
    É o único dos 16 itens do Portfólio nessa situação. **Pergunta:** existe de fato, ou é um nome
    reservado para uma solução ainda não iniciada?
45. **Um cliente pode ter mais de uma conta na plataforma, e não temos isso modelado.** Casos reais:
    `Cambos` (7 usuários) **e** `Cambos - uFlow` (25 usuários); `Tempo de Criança` **e**
    `Tempo de Criança (uRocket)`; `Studio Z` **e** `Studio Z <> SalesForce`. O sufixo indica conta
    por módulo/integração. Isso não é alias de cliente — é uma entidade "conta/instância" entre
    Cliente e Solução, que se parece muito com a entidade **"Solução × Cliente"** já prevista em
    `CONTEXT.md` → "Fora de escopo agora". **Sugestão:** quando essa entidade for formalizada, ela
    deve carregar o identificador da conta na plataforma.
46. **Agentes deixaram de ser abstração: existem 4 nomeados em fonte real.** `product-analyzer`,
    `tryon-stylist`, `audio-transcriber` e `product-enricher` (este último "futuro", e o documento
    diz que "fica em EnriqueceAI"), cada um com treinamento intrínseco (Hub) + complemento por
    aplicação. `brainwave/CONTEXTO.md` ainda registra "Agente como entidade formal não existe" — o
    que continua verdade quanto a template/protocolo, mas **já não é verdade quanto a dado real**.
    Quando a entidade Agente for formalizada, estes 4 são o ponto de partida.


## Notion — primeira leitura (03 ago 2026)
> Achados completos em `_varredura-ferramentas-produtos-areas.md` → seção "Notion".

47. **Grafia divergente na fonte canônica: `ForneceAI` × `FornecAI`.** A página "Arquitetura uMode
    V1" no Notion — que o próprio documento de arquitetura declara como vencedora em caso de
    contradição — escreve **"Módulo 4 — ForneceAI"**. `CONTEXT.md` e todo o nosso Portfólio escrevem
    **"FornecAI"**. Nenhum dos dois foi alterado. **Decisão do Vinicius/CEO:** qual é a grafia
    oficial? Se for `ForneceAI`, muda o nome do item no Portfólio travado e a pasta
    `04_FornecAI/`.
48. **`Projeto` é uma entidade real e não está modelada.** É relação a um database próprio
    (`241b1d38-e768-80cd-9213-000b0dbeb621`), preenchida em 594 das 1.010 demandas, com valores como
    `[NK] - uFlow` e `📌 [LOFTY] - ONBOARDING FASE 1`. Liga demanda → fase de onboarding/projeto do
    cliente, o que conversa direto com `jornada.md` (que hoje registra marcos, não projetos). Hoje o
    valor está preservado como campo legado em `Notas internas`. **Decisão pendente:** vira entidade
    própria, campo da Demanda, ou seção de `jornada.md`?
49. **Enums do CX Hub/Notion são maiores do que o export mostrava.** `Bloqueio` tem 8 opções (o
    export só revelou 6 — faltavam `Aguardando Terceiros` e `Aguardando Comercial`);
    `Suporte Integração` tem **17** (export mostrou 8); `uMode - Macro Tema` tem **20**. Consequência
    prática: sempre que possível, **ler o schema da base viva antes de traduzir enum**, em vez de
    inferir o enum a partir dos valores que aparecem no dado exportado. Reforça a pendência 33.
    O enum de `Suporte Integração` é, na prática, uma **taxonomia técnica de integração já pronta** —
    aproveitar quando a frente de repositórios de integração começar.
50. **Existe uma 5ª fonte de "quem é cliente": a base de Clientes do Notion**
    (`ec041afd-fcee-44f8-83cb-223fca6f4108`), que é o alvo da relação `👥 Clientes` das demandas.
    Ainda não cruzada. Junto com CRM (46), pasta Drive "Clientes" (+9 nomes), planilha de acessos
    (+18 organizações) e as pastas do repositório, são **5 listas diferentes** de cliente. Cruzar as
    5 e produzir uma lista mestra reconciliada é uma frente própria — e o `client_id` já travado é a
    chave para isso.



## Infra de tecnologia — mapa próprio (03 ago 2026)

51. **Criado documento dedicado para o que exige intervenção de infra:**
    `uMode/06_Tecnologia/_contexto/_backlog-infra-tecnologia.md`. Pedido do Vinicius: **não
    desenvolver API nenhuma agora**, mas rastrear e mapear tudo desde já, porque *"teremos vários
    agentes que deverão beber diretamente da fonte dos repositórios para operacionalizar"*. O
    documento cobre 4 blocos: (1) acesso programático às fontes — hoje **todo** acesso externo é MCP
    autenticado como pessoa física, o que não serve para agente autônomo; (2) o que precisa ser
    construído para o cérebro operar (job de sincronização, índice em servidor, RAG com escopo,
    banco, formulários); (3) 8 dívidas de dado que exigem decisão ou correção na origem; (4) 5
    limites de ambiente que já bateram na prática. **Os itens de dívida de dado deste documento são
    os mesmos das pendências acima** — lá eles aparecem sob a ótica "o que a equipe tech precisa
    fazer", aqui sob a ótica "o que precisa ser decidido". Não duplicar decisão: quando um resolver,
    atualizar os dois.

## Integrações — 5º tipo de MD de cliente (03 ago 2026)

52. **`arzz-sap` = Reserva/Oficina, não Arezzo — erro meu de inferência, corrigido antes de gerar
    arquivo.** Numa primeira leitura do inventário eu inferi `arzz` = Arezzo pela semelhança do nome.
    O Vinicius corrigiu: é **AZZAS**, o grupo (o CRM já classifica Reserva e Oficina Reserva em
    "Grupo 1: Azzas"). `unico-linx` = **Puket**, o que também não se adivinha pelo nome. Registrado
    em `protocolo-gestao-integracao.md` com aviso explícito de **nunca inferir cliente pelo nome do
    repositório**. Consequência para os 9 nomes do item 23: **Arezzo continua sem confirmação** — o
    repositório que eu acreditei ser dele é de outro cliente.
53. **`Puket` e `Baw` tinham `ERP / Integração` = `[a preencher]` no CRM e têm integração Linx
    real.** Preenchido em 03 ago 2026 **a partir do repositório**, com a fonte citada no próprio
    campo. Mostra que o repositório de integração é fonte melhor que o CRM para esse campo
    específico — vale re-checar os demais clientes quando a leitura técnica for feita.
54. **Moda Objetiva não tem documentação de integração** (informado pelo desenvolvedor) e **Puket tem
    repositório sem nenhum `.md`**. São dois estados diferentes e ambos ficaram registrados como
    tal: "não existe integração documentada" × "existe integração, falta documentação". Não confundir
    com lacuna de preenchimento nossa.
55. ~~**`integracao.md` está com só a seção Identificação preenchida nos 11 clientes.**~~
    **FECHADA em 03 ago 2026.** Os 9 `documentacao-geral-*.md` foram lidos e os 11 arquivos estão
    com todas as seções técnicas preenchidas — 100% conformes ao template (30 títulos cada, 957
    linhas no total). A estrutura dos documentos de origem **não é uniforme** entre clientes
    ("Visão Geral" em 8 de 9, "Escrita"/"Leitura" em 5 de 9, o resto específico), o que confirmou a
    decisão de o nosso template ser uniforme e **resumir + apontar** em vez de copiar. Sobrou só
    Puket, que não tem documento nenhum (item 54), e a governança dos 11 (item 57).

## Integrações — o que a leitura técnica abriu (03 ago 2026)

56. **Os riscos técnicos encontrados foram para `_backlog-infra-tecnologia.md`, seção 4 — não são
    pendência de preenchimento.** 15 itens, todos escritos no documento do próprio repositório.
    O mais grave: **a integração da Cambos não envia autenticação nenhuma ao SPI** (sem header
    `Authorization`, sem token). Não é diagnóstico meu sobre o código — está registrado pelo autor
    da integração como o ponto de risco mais relevante daquele repositório. Precisa de decisão da
    equipe tech, não de campo em MD.
57. **Nenhum dos 9 documentos técnicos nomeia responsável técnico.** Os 11 `integracao.md` ficaram
    com `Responsável técnico` e `Quem pode alterar este documento` em `[a preencher]` — são as duas
    únicas lacunas dos 10 arquivos preenchidos. Não é dado que se derive do repositório; **depende
    do Vinicius**. Único nome que a leitura trouxe: os documentos de incidente da VIX mencionam
    **Felipe** (uMode) como quem conduziu os contatos, e são assinados genericamente como "Equipe
    Técnica uMode" — não é designação de responsável, e não foi tratado como tal.
58. **Vínculo Integração → RFI já resolve hoje, sem campo novo.** Os incidentes da VIX citam
    "RFI #83" e "RFI #85"; o campo `ID legado (Notion/CX Hub)` dos nossos arquivos resolve os dois:
    `RFI-83` = `RFI-2026-005` e `RFI-85` = `RFI-2026-004`, ambos da VIX. **É a prova de que o eixo
    de indexação funciona para além de cliente** — documentação técnica de integração aponta para
    RFI formalizada. **Materializado no mesmo dia:** `_indice/integracoes.csv` (11 linhas, 6º eixo do
    índice) tem a coluna `rfis_citadas`, que varre o corpo do `integracao.md` por `RFI #NNN` e
    resolve pelo `ID legado (Notion/CX Hub)` das nossas RFIs; e os dois incidentes da VIX passaram a
    citar os dois IDs lado a lado. **O que sobra:** RFI citada e não resolvida entra no CSV marcada
    como `(não resolvida)` — hoje não há nenhuma, mas é o comportamento esperado quando aparecer
    documento novo. E o inverso ainda não existe: a RFI não aponta de volta para a integração.
59. **A VIX tem duas datas de início do mesmo incidente e as fontes não se reconciliam:** o relatório
    de incidente diz **25/03/2026** (primeira notificação de erro no Discord em 25/03 às 09:01) e o
    documento de migração SMB diz **"aprox. 27/03 (data a confirmar)"**, marcado como rascunho para
    revisão interna. Gravado como divergência explícita no `integracao.md` da VIX — **não escolhi
    uma das duas**.
60. **`umode-microservice-uconnect` (o interceptor) é componente compartilhado da uMode e não está
    no Portfólio de Soluções.** Intermedia Baw, Lofty Style e Osklen; mantém o snapshot MongoDB que
    alimenta as leituras; **gera a referência do produto** (`GG.SS.NNNN`, com incremento em
    `PRODUTOS_SUBGRUPO`); **injeta contas contábeis** por `INDICADOR_CFOP`; e roda o cron de
    auditoria uFlow × Linx. Isso é regra de negócio, não encanamento — merece ficha e dono.
    Registrado também em `_backlog-infra-tecnologia.md` 4.11.
61. **Aviso de divergência de ERP desatualizado em Puket e Baw, corrigido.** O `integracao.md` foi
    gerado quando o `institucional.md` desses dois ainda tinha `ERP / Integração = [a preencher]`, e
    o gerador tratou campo vazio como divergência. Os 11 clientes **conferem** com o ERP que o
    repositório indica. Corrigido por `scripts/fix-integracao-divergencia-erp.ps1`, que troca o
    aviso por confirmação com a fonte. **Lição:** campo vazio nunca é divergência, e aviso
    desatualizado é pior que aviso nenhum — manda investigar um conflito que não existe.
62. **A afirmação do desenvolvedor sobre documentação não bate com o disco.** Ele informou que "só a
    Moda Objetiva não tem documentação ainda"; na prática **Moda Objetiva não tem repositório algum**
    no caminho compartilhado, e **Puket tem repositório com zero `.md`**. São dois estados diferentes
    (item 54) e nenhum dos dois é o que foi informado. Vale confirmar com ele se existe repositório
    da Moda Objetiva em outro lugar.

## Portfólio de Soluções — o que a leitura do Notion resolveu e o que abriu (04 ago 2026)

63. ✅ **FECHADA — `EnriqueceAI` × `CadastrAI` × `CadastroAI`: eram três coisas, não três grafias.**
    A Especificação por Módulo V1 (Notion `34db1d38e768814b8001d7cb6cacf4e5`) diz literalmente:
    "No desenho original era 'CadastroAI' como módulo de enriquecimento. Foi rebatizado para
    EnriqueceAI durante esta sessão para liberar o nome 'CadastrAI' para o núcleo de governança."
    Ou seja: **EnriqueceAI = antigo CadastroAI**; e **CadastrAI = núcleo de governança**, item novo
    que herdou o nome liberado. A hipótese que Vinicius levantou em 04 ago 2026 ("EnriqueceAI
    substituiu o CadastrAI, é a mesma coisa com nome novo") estava **meio certa**: houve
    renomeação, mas não é o mesmo item que o `CadastrAI` de hoje. Isso também explica a suposta
    divergência de grafia `CadastroAI` × `CadastrAI` que estava registrada como pendência — não era
    grafia, era **duas entidades diferentes em momentos diferentes**. Nenhum item foi fundido.
64. ✅ **FECHADA — grafia `FornecAI` × `ForneceAI`.** A fonte canônica é **inconsistente consigo
    mesma**: o cabeçalho da seção do módulo escreve "ForneceAI" e o corpo do mesmo documento escreve
    "FornecAI" em todas as demais menções. O ÍNDICE MESTRE grafa **FornecAI**, igual a `CONTEXT.md`.
    Como a maioria das ocorrências e o índice convergem, `FornecAI` fica como grafia oficial e o
    caso deixa de ser divergência entre nós e a fonte — passa a ser inconsistência **interna** da
    fonte, registrada aqui e não corrigida por conta própria no Notion.
65. **Duas taxonomias coexistem na uMode, ambas de abril/2026, e nunca se citam.** (1) A Solução
    **Taxonomia** — taxonomia canônica do PLM padrão, 6.567 campos do uFlow → 2.618 clusters, 9
    verticais, PO João Risoléo, validação Ana Lucia, engenharia "time uMode + AI HOUSE"
    (`348b1d38e7688087aef7e8a2b64349d0`). (2) **TaxonomyAI** — um **serviço** que recebe imagem +
    dados do PLM e devolve atributos por API; 12 zonas / 45 dimensões / 431 valores, baseado em
    Fashionpedia + Shopify Standard Product Taxonomy, com normativo próprio ("Dicionário Oficial de
    Taxonomia", responsável **João Ferraz**). Bases, escalas, donos e galhos do Notion diferentes.
    **Nenhuma página afirma que são a mesma coisa nem que são diferentes.** Precisa de decisão: são
    duas camadas de um mesmo desenho (modelo de dados × serviço de extração) ou dois esforços
    paralelos? Enquanto não se decide, o Portfólio tem uma Solução chamada Taxonomia cuja relação
    com o TaxonomyAI é indefinida.
66. **A natureza da Solução `Taxonomia` muda conforme a fonte.** No nosso Portfólio é uma Solução;
    na Especificação V1 é **serviço interno do CadastrAI** ("provavelmente um microserviço
    independente exposto por API"); no ÍNDICE MESTRE está no **Domínio 1 — Arquitetura e
    Estratégia**, não no Domínio 3 — Produtos uMode. Três fontes, três naturezas.
67. **O `CadastrAI` está como `Destino = Interna` e as fontes o tratam como produto voltado ao
    cliente.** O ÍNDICE MESTRE o classifica no **Domínio 3 — Produtos uMode** (não no Domínio 4 —
    Produtos Internos), declara "Produto em produção" e nomeia **Luiza Barcelos e Reserva como
    clientes âncora**. `Destino` vem da lista travada de `CONTEXT.md`, então não mexi. Precisa de
    decisão: erro de classificação, ou produto interno com clientes de referência?
68. **Dois Scores de maturidade mudaram, e o protocolo exige ratificação (Vinicius + CEO).**
    (a) **GerenciAI: `Ideação` → `Escalável`** — a Especificação V1 diz "**o módulo que a Reserva já
    usa hoje**. Mas a visão futura é maior". A avaliação anterior classificou pela visão futura, que
    a própria página marca como brainstorm. (b) **Taxonomia: `Escalável` → `MVP`** — nenhuma fonte
    declara produção; a página diz "v1 baseline abril/2026", "próxima v2 após primeiro piloto
    completo", **1.820 dos 2.618 clusters ainda em revisão humana**, e a Especificação V1 é ainda
    mais conservadora ("existe esboço inicial dela em pasta de Templates"). A avaliação anterior
    confundiu **importância transversal com maturidade**.
69. **Contradição de escopo do Portfólio: as fontes desenham 8 peças, nossa lista travada tem 16.**
    A Especificação V1 desenha "6 módulos de aplicação" (PlanejAI → CriAI → DesenvolvAI → FornecAI →
    EnriqueceAI → GerenciAI) mais dois pilares estruturais (CadastrAI e Hub de Agentes) = 8. O
    ÍNDICE MESTRE, no Domínio 3, lista **apenas 4 projetos** (CadastroAI, PlanejAI, DesenvolvAI,
    CriAI) e não tem entrada para FornecAI, EnriqueceAI, GerenciAI, AlocAI, VendeAI, CliprocAI nem
    IntHub. Não é contradição de fato — é a lista travada sendo mais ampla que o desenho canônico —
    mas explica por que 3 Soluções ficaram sem nenhuma fonte (item 70).
70. **Três Soluções do Portfólio não têm NENHUMA fonte: `AlocAI`, `VendeAI` e `CliprocAI`.** Busca
    literal nas 4 páginas canônicas lidas: zero menções. Tudo que sabemos delas vem de briefing
    direto de Vinicius. Nota de honestidade: a Especificação V1 tem uma vertical do AI First chamada
    **"Realocação"** (ruptura iminente, sobra projetada, transferência loja a loja), mas ela nunca é
    nomeada AlocAI nem tratada como produto — **a equivalência não foi derivada**.
71. **`IntHub` é a Solução com menos rastro de todas.** Aparece **uma única vez** em tudo que foi
    lido: na atualização de 28/05/2026 do ÍNDICE MESTRE, na lista de produtos internos
    single-tenant. Não tem entrada no Domínio 4, não tem página de projeto, não tem status, não
    aparece na Especificação V1 nem no inventário do Hub de Agentes. O próprio ÍNDICE MESTRE se
    declara mapa completo do que existe — e cita IntHub sem lhe dar entrada, função nem status.
72. **Ferramentas da uMode citadas nas fontes e fora da lista travada de 16.** Nenhuma virou ficha —
    a lista de 16 é travada em `CONTEXT.md` e um 17º item exige decisão explícita. **Complementa a
    seção "Portfólio / Ferramentas — nomenclatura legado → novo" (itens 10 a 16), que já cataloga
    `uBuy`, `uRocket`, `uPick`, `uTrack`, `uMetrics`, `uDash` e `ISPS`** — o que segue são as
    ferramentas que apareceram **nas páginas canônicas do Notion lidas em 04 ago 2026**, mais o
    complemento do briefing do mesmo dia:
    - **`uRocket`** — já catalogado no item 11 como descontinuado (13 jul 2026). **Complemento de
      04 ago 2026:** era a ferramenta de **vendas via campanhas montadas no WhatsApp** — a função
      exata, que o item 11 registrava só como "mensageria". **Não aparece em nenhuma página do
      Notion lida**, e ainda assim persiste como conta na planilha de acessos ("Tempo de Criança
      (uRocket)") — ferramenta encerrada com conta viva.
    - **`uFlow`** — o PLM que **segue conduzindo praticamente todos os contratos** (Vinicius, 04 ago
      2026), registrado no Notion muitas vezes como **"Gestão de Coleção"**. É simultaneamente o
      legado de que o **DesenvolvAI** descende e o legado que a **Taxonomia** declara substituir —
      dois ângulos, duas Soluções, o mesmo legado. Tem um motor de actions chamado **Jumper**.
    - **`uConnect`** e **`uTimeline`** — a Especificação V1 os coloca literalmente em
      "A resolver na continuação da sessão": "**uTimeline / uConnect** — apareceram nas notas do
      Notion; verificar se entram nesta arquitetura ou são peças adjacentes." Ou seja, o status
      deles é **indefinido por decisão registrada**, não por lacuna nossa. Vinicius suspeita que
      uConnect era o nome do módulo de integrações (marcado por ele como incerto); a documentação
      dos repositórios mostra `umode-microservice-uconnect` em produção como interceptor de 3
      clientes. A equivalência **uConnect → IntHub** segue não confirmada. `uTimeline` é nome novo,
      sem nenhuma outra ocorrência em qualquer fonte nossa.
    - **`Hub de Agentes`** — pilar estrutural com página técnica própria e **16 agentes
      inventariados em 5 projetos**. Ver item 73.
    - **`AI HOUSE`** — citado na página Taxonomia como base do "novo sistema sob medida" e como
      parte da engenharia. ⚠ O ÍNDICE MESTRE tem um "Projeto: IA House" no **Domínio 6 — Projetos
      Pessoais do João**. As páginas não esclarecem se são a mesma coisa; não foi presumido.
    - **`Lovable`** (plataforma de build dos V0), **`Runflow`** (plataforma externa em avaliação como
      orquestrador de agentes) e **`Supabase`** — infraestrutura, não Solução.
73. **O Hub de Agentes tem 16 agentes inventariados — e isso NÃO tem relação com as 16 Soluções.**
    Coincidência numérica perigosa, registrada de propósito. Os 16 agentes vivem em 5 projetos
    (CriAI 8 · CadastrAI 4 · CX Hub 4 · ONB HUB 1 · Gest Hub 0, "zero IA hoje"). O plano é v3.0 de
    abr/2026 e **não começou**: o próximo passo declarado é "criar o projeto Lovable separado
    manualmente" e as **9 caixas do checklist de segurança estão todas desmarcadas**, incluindo
    "proxy reverso `api.umode.tech` no ar antes de qualquer outro passo". Necessidades de infra
    foram para `_backlog-infra-tecnologia.md`.
74. **⚠ Divergência sobre o que o Hub de Agentes É.** Vinicius descreveu em 04 ago 2026 como "uma
    plataforma que seja a construção do BrainHub do próprio cliente (no novo modelo de negócios de
    mentoria e educação), com os agentes que temos disponíveis para ele — como se ele 'baixasse' o
    planejador que sairá do PlanejAI". O **Plano Técnico (abr/2026) não diz nada disso**: descreve
    consolidação **interna** de agentes hoje espalhados por 5 produtos, para resolver exposição de
    infraestrutura, isolamento, gestão manual e hardcode. A página não menciona cliente final,
    comercialização, mentoria nem educação. As duas leituras podem ser fases diferentes da mesma
    coisa — a técnica é de abril, a de negócio é de agosto — mas **não foram fundidas**. Adjacente:
    o ÍNDICE MESTRE tem "Projeto: Mentoria — produto de mentoria em construção, prospect âncora
    Bernhoeft" no Domínio 6 (Projetos Pessoais do João), o que reforça que mentoria existe como
    frente, mas em outro lugar.
75. **6ª fonte de "quem é cliente" — a base legada da Taxonomia, com 101 fichas (83 ativas).** A
    dívida 3.1 do backlog de infra falava de 5 fontes; agora são 6. Cruzando as 83 fichas com nossos
    46 clientes: **24 casam**, e **~12 nomes não têm casa nenhuma** — `Lojas Nalin`,
    `Puket Tecidoteca`, `Basico.co`, `Beira Rio`, `Dakota`, `Grendene`, `Lojas Estrela`,
    `Minimal (trial)`, `Mondepars`, `Sinbi`, `Via Marte`, `Tempo de Criança`. Dois casos são só
    variação de nome já resolvida (`Objetiva` = Moda Objetiva; `Oficina` = Oficina Reserva).
    **`Sinbi` é o caso mais importante:** a fonte diz que tem "dezenas de submarcas" sob ela — é
    exatamente a entidade "conta/instância" que falta no nosso modelo (dívida 3.2). E
    `Puket Tecidoteca` sugere que um cliente pode ter mais de uma ficha por operação.
76. **Nomes de cliente novos vindos do ÍNDICE MESTRE, Domínio 5, com o qualificador da fonte:**
    `Grupo AZZAS` — "Pipeline Enterprise — **Arezzo, Hering, Loungerie**. Prob 5". Isso reabre o item
    52 de forma útil: **Arezzo aparece como prospect de pipeline, não como cliente** — o que é
    coerente com ele não ter casa. `Loungerie` é nome novo. `Lenny` aparece como cliente com "flags
    de alerta no CX Hub", status `revisar`, e a base da Taxonomia grafa `Lenny Niemeyer`.
77. **Pessoas nomeadas nas fontes que ainda não têm ficha ou vínculo registrado:** **André** (time
    técnico, interlocutor de todas as decisões de arquitetura pendentes), **Ana Lucia** (validação de
    produto da Taxonomia), **João Ferraz** (responsável pelo Dicionário Oficial de Taxonomia).
    Também aparece "**o agente AZZAS**" como contraparte da sessão de arquitetura de 24/04/2026 —
    não é pessoa. `Victor` e `Fernanda` são citados como o time de implantação que "atende marca";
    `Vini` opera o PlanejAI; `Victor` opera o ONB HUB (o índice só dá o primeiro nome).
78. **A fonte canônica declara 6 "pendências honestas — não vender hipótese como decisão":**
    GerenciAI conversacional, FornecAI pricing, push Vtex, gamificação, PlanejAI in-season e
    política (c) de auditoria. Isso é insumo direto de maturidade: **a própria uMode marca esses
    seis como hipótese**, e nenhum deles deve aparecer como capacidade entregue.
79. **Decisões de arquitetura abertas com o time técnico (André), registradas na Especificação V1:**
    como `org_audit_policy` é exposto na API; se a Taxonomia é versionada por cliente ou só global;
    se o Hub de Agentes mora no mesmo cluster do CadastrAI; **onde mora o motor de regras do AI
    First** (CadastrAI? GerenciAI? Hub?); como o `audit_status` propaga entre módulos (push vs
    pull); SLA e escalonamento da política (c).
80. **Contradição sobre o número de camadas de configuração.** A skill `umode-arquitetura-tese` lista
    entre os princípios não-negociáveis "config em 3 níveis (uMode → marca → usuário)" e, na mesma
    lista, "2 camadas". A Especificação V1 trava em **duas** camadas (padrão uMode + personalização
    da marca) e só introduz o terceiro nível dentro do GerenciAI, chamando-o de "mais granular que
    tudo que apareceu antes na arquitetura". Vale confirmar qual é a versão travada.
81. **A página que eu chamava de "Arquitetura & Tese" não é o documento de arquitetura.** É uma
    **ficha de skill** (`umode-arquitetura-tese`) dentro do database "Biblioteca de Skills — uMode",
    com caminho local `~/.agents/skills/umode-arquitetura-tese/SKILL.md`. Traz só as **headlines**
    dos 10 blocos, sem o conteúdo. O documento real é a "Especificação por Módulo (V1 — sessão
    24/04/2026)". O conteúdo dos blocos "Anti-claims" e "diferenciadores" está no arquivo de skill
    **local**, ao qual não temos acesso.
82. **Erro de link no ÍNDICE MESTRE, registrado para quando for corrigido na origem:** as entradas
    "Arquitetura uMode V1" (Domínio 1) e "Prompt de Auditoria — Claude Code" (Domínio 2) apontam
    para a **mesma URL**. Na prática o prompt de auditoria é uma seção interna da página de
    arquitetura, não documento separado.

## Primeira entrega do BrainHub e os 4 repositórios novos (04 ago 2026)

83. **🚧 BLOQUEIO DA PRIORIDADE ZERO: não temos o repositório da plataforma uFlow.** A demanda
    `D-2026-002` (agente de suporte técnico uFlow) define que **o contexto do agente É o repositório
    da plataforma**. Verificado em 04 ago 2026: **nenhum projeto Ruby/Rails em
    `C:\Ambientes Virtuais`** — e o próprio `Papel de Suporte.txt` pede "comandos Rails Console",
    confirmando que a uFlow é uma aplicação Rails. Bloqueio irmão: **a estrutura do banco da uFlow
    também não existe em nenhuma fonte nossa** — os 10 repositórios de integração documentam as
    tabelas do **ERP do cliente** (Linx, SAP, SPI, Safe Tech), nunca as da uFlow. **Sem esses dois,
    o agente não pode existir.** É o item mais urgente de todo este documento.
84. **28 pastas em `C:\Ambientes Virtuais` que nunca foram varridas, várias com nome de produto
    nosso.** Descoberto em 04 ago 2026 ao procurar o repositório da uFlow. Não foram lidas — só
    inventariadas. As que mais interessam:
    - **`uPlan`** — o legado do PlanejAI, cuja linhagem já está confirmada.
    - **`umode-catalog-ai`** — está na pendência 21 exatamente como "seria o CadastrAI?".
    - **`CriAI`, `CriAI NV`, `criai-vision-board-9d1195a1`, `criai-vision-board-original`,
      `umode-criai-rsv`** — **5 pastas** de CriAI. Vinicius informou em 04 ago 2026 que existem
      versões internas **CriAI 2, 3 e 4** como evoluções de feature; é o candidato natural a
      resolver quais são.
    - **`Performance Engenharia - Legado`** — "legado" no nome; candidato a conter material da uFlow.
    - **`Atribuição de atributos - Produtos`** — vocabulário de Taxonomia.
    - **`PlanejAi`** (segunda pasta, grafia diferente de `uPlan`), **`proposal-core`**,
      **`widgets-nv`**, **`Projeto IA uMode`**, **`Imersão uMode`**, **`Relatórios - Git`** — não
      identificadas.
    - Aparentemente fora do escopo uMode: `casa-zeeni`, `Lala`, `hytrack-water-analysis`,
      `Controle Financeiro`, `Projeto Financeiro`, `Estudo Engenharia de Software`, `Fotos Produtos`,
      `Atribuição de atributos - Produtos` (a confirmar).
    **Isso é candidato a fechar a pendência 21** (confirmação de repositório real por item do
    Portfólio), que estava explicitamente marcada como "tarefa manual do Vinicius". Não avancei nelas
    sem instrução — mas o inventário está aqui.
85. ✅ **FECHADA em parte — `IntHub` finalmente tem função e repositório.** Informado por Vinicius em
    04 ago 2026: é a **ferramenta interna construída no Lovable que monitora o processo de
    integração** — alerta sobre qualquer falha, resume dia a dia as vistorias, e tem dashboard.
    Repositório `integration-pulse-check-e914756f`, clonado em
    `C:\Ambientes Virtuais\integration-pulse-check-e914756f` (143 arquivos, 9 `.md` com PRD de
    33 KB, 17 `.sql`). Isso resolve o item 71, que registrava o IntHub como a Solução com menos
    rastro documental de todas — e **explica a lacuna**: ele não aparecia nas páginas canônicas do
    Notion porque é obra recente, construída fora daquele ciclo de documentação.
86. ✅ **FECHADA em parte — `AlocAI` = repositório `umode-design-guardian`.** Clonado em
    `C:\Ambientes Virtuais\AlocAI` (154 arquivos, `MAPA_FUNCIONAL.md` de 29 KB,
    `docs/PRD_ALOCAAI.md`, `docs/ANALISE_RESERVA_PLANOGRAMA.md`). Dois efeitos: (a) resolve parte do
    item 70, que registrava AlocAI como Solução sem nenhuma fonte; (b) **resolve uma das perguntas
    abertas do item 21**, que listava `umode-design-guardian` entre os repositórios não
    identificados. ⚠ **É o terceiro caso de nome de repositório que não entrega o produto**
    (`arzz-sap` não é Arezzo, `unico-linx` é Puket, `umode-design-guardian` é AlocAI) — a regra de
    nunca inferir produto ou cliente por nome de repositório está agora confirmada três vezes.
87. **⚠ A hierarquia real do CX Hub tem 4 níveis e o nosso protocolo de Demanda só modela 2.**
    Informado por Vinicius em 04 ago 2026: no CX Hub a hierarquia é
    **Programas → Projetos → Demandas (que podem ou não ser RFIs) → Subdemandas**, e **uma Demanda
    pode ser criada fora de qualquer Programa ou Projeto**. Hoje o nosso `protocolo-gestao-demanda.md`
    só tem `Demanda mãe` / `Demandas filhas` e uma seção `Subdemandas` — **não existe Programa nem
    Projeto em lugar nenhum do nosso modelo**. Isso é mais amplo que o item que registrava "`Projeto`
    como entidade" a decidir: são **duas** entidades faltando, com relação opcional. Também confirma
    que **RFI é um tipo de Demanda**, coerente com a decisão já travada de mover a RFI para dentro da
    Demanda. Não alterei o protocolo — mudança de modelo de dados não se faz por conversa, e o
    repositório do CX Hub está sendo lido para confirmar o schema real antes de qualquer proposta.
88. **⚠ O "BrainHub do João Risoléo" é o repositório `design-system-hub`, e nome e conteúdo não
    batem.** Clonado em `C:\Ambientes Virtuais\BrainHub - João Risoléo` (167 arquivos, mas só
    **7 `.md`**, todos de design system: `.agents/skills/umode-design-system/SKILL.md`,
    `references/tokens.md`, `snippets.md`, `patterns.md`). Vinicius o descreveu como "o BrainHub que
    o João começou a montar na minha frente, que já tem uma porção de agentes". Registrado como
    discrepância a resolver, não como conclusão — o repositório está sendo lido. **Restrição de
    escopo explícita de Vinicius:** não copiar nada dali; o padrão é o nosso. O objetivo da leitura é
    entender arquitetura e funcionalidade e, sobretudo, **mapear de quais fontes ele puxou
    conteúdo**, para depois decidirmos onde mais buscar.
89. **Os 4 repositórios novos seguem o padrão de 6 arquivos declarado no ÍNDICE MESTRE** em
    28/05/2026 (`CLAUDE_OPERADOR`, `CLAUDE_PROJETO`, `CLAUDE`, `AGENTS`, `CONTEXT`,
    `CONTEXT_LOVABLE_DOCS`). É a primeira confirmação **prática** dessa regra — até agora ela era só
    uma linha de atualização numa página do Notion. Vale como sinal de que o padrão está de fato em
    uso, e como referência para qualquer repositório que a infra venha a criar.
90. **Convergência não combinada, registrada porque é sinal de que o padrão está certo:** o
    `Papel de Suporte.txt` manda o agente "nunca fazer suposições sem evidências encontradas no
    código" e diz que "é preferível pedir mais dados do que fornecer uma resposta potencialmente
    incorreta". É, palavra por palavra em espírito, a **regra de ouro de zero alucinação** do
    `CLAUDE.md` deste repositório. Dois autores diferentes, sem combinar, chegaram à mesma
    disciplina — o que reforça a decisão de mantê-la travada.

## BrainHub do João Risoléo — o que a leitura revelou (04 ago 2026)

91. ✅ **RESOLVIDA a discrepância do item 88 — o repositório `design-system-hub` É um BrainHub.**
    É um **console web de BrainHub**, e o nome é resíduo do projeto Lovable original, nunca
    renomeado. Evidência: 18 rotas de UI, todas de BrainHub (`inbox`, `conversas`, `aprovacoes`,
    `biblioteca`, `arquivos`, `relacoes`, `agentes`, `rotinas`, `operadores`, `governanca`,
    `importar`, `migracao`); a tela inicial se intitula "BrainHub Console"; **30 tabelas** de
    conhecimento/governança/agentes nos 17 `.sql`; e o manifest MCP nomeia o servidor
    `brainhub-mcp`. O design system aparece só como **insumo de estilo**, e aponta para fora
    (`https://designsystem.umode.tech`, declarado single source of truth). Três nomes desalinhados no
    mesmo projeto: repositório `design-system-hub`, app "BrainHub Console", `package.json`
    `tanstack_start_ts` (nome de template).
92. **🔴 O ACHADO MAIS IMPORTANTE: o vault do João usa EXATAMENTE a nossa estrutura de pastas, e tem
    dois arquivos de taxonomia que nós não temos.** Os reports do repositório citam caminhos
    canônicos do vault que são **byte a byte a nossa convenção**:
    - `BrainHub/uMode/00_Institucional/_contexto/TAXONOMIA_UMODE.md` — **8.356 palavras, 212
      headings**
    - `BrainHub/uMode/04_Dados-e-IA/taxonomia-atributos/GRUPOS_ATRIBUTOS_UMODE.md` — **8.765
      palavras**

    `00_Institucional/_contexto/` e `04_Dados-e-IA` são precisamente os nomes das nossas pastas
    (conferido em 04 ago 2026). **Não temos nenhum dos dois arquivos** — busca por `TAXONOMIA_UMODE`
    e `GRUPOS_ATRIB` no repositório: zero resultado. São os dois maiores arquivos do vault e ambos
    de taxonomia, os dois sinalizados `EXIGE_JOAO_CRITICO_8K` pelo auditor de tamanho do Hermes.
    **Hipótese forte, não confirmada:** é esta a "outra fonte rica de informações institucionais
    (produtos, áreas etc.)" que Vinicius anunciou em 03 ago 2026 como a fase de reprocessamento.
    Não confirmei porque só temos o **nome e o tamanho** dos arquivos, citados em report — o conteúdo
    não está em nenhum repositório clonado.
93. **🔴 O vault `~/Documents/uMode-OS/` é a fonte primária de TUDO, e continua inalcançável.** O
    repositório do João **não integra nenhuma fonte externa** — varredura de 167 arquivos e 211
    commits por `notion`, `drive.google`, `docs.google`, `discord`, `slack`, `gmail`, `airtable`,
    `hubspot`, `salesforce` e mais: **zero ocorrências**. As duas únicas menções a Notion são
    **negativas**, declarando que o sistema não a chama. O padrão é outro: o console é o **destino**,
    e um agente local chamado **Hermes**, na máquina do João, é quem lê as fontes e empurra para lá.
    Isso escala o item que já registrava o `uMode-OS` como inalcançável: não é uma fonte entre
    outras, **é a fonte**. Caminho absoluto literal encontrado no código:
    `/Users/joaorisoleo/Documents/uMode-OS/inbox/claude/PARA_HERMES.md`.
94. **🔴 Existe um registro numerado de decisões de arquitetura que nós não temos: a série D13 → D51,
    em `uMode-OS/DECISOES.md` e `_GOVERNANCA.md`.** O `AGENTS.md` do repositório declara a regra de
    precedência: **"Em conflito, a governança do vault vence."** Decisões referenciadas por número
    nos comentários das migrations: D13, D26, D29, D46, D47, D49, D51. Duas com data e citação
    literal do João: **D47/D49 em 12/07/2026** e **D51 em 14/07/2026** — "não podemos ter simplesmente
    PROMPTs, e sim loop que contemple auditoria". Isso é o equivalente do nosso `CONTEXT.md` (as
    decisões travadas) do lado dele, e é conteúdo que muda como entendemos o projeto todo.
95. **⚠ Incidente de segurança real, autodocumentado, envolvendo dado T1 de cliente — e valida a
    cautela que mantivemos com a Cambos.** A migration `20260728150000` é uma autocrítica de 25
    linhas: a trava de sensibilidade criada em 12/07 **"era decorativa"** — gateava em
    `payload->>'sensitive'` (booleano) enquanto o seeder gravava `sensitivity` (o tier). Medição
    literal: "a chave `sensitive` existia em 6 de 53 linhas. Nas outras 47 o COALESCE caía em `false`
    e a linha PASSAVA". Consequência declarada: **"O primeiro T1 aprovado (valor de contrato Malwee,
    CNPJ + receita de cliente) teria vazado para a chave pública sem ninguém perceber."** A conclusão
    do próprio autor merece ficar registrada como princípio: **"Regra que não sabe reprovar não vale
    nada; esta sabe."** Foto real do banco após a correção: **39 T1, 11 T2, 3 T0**.
96. **As camadas T0/T1/T2 agora têm definição operacional, não só nome.** Além do que o ÍNDICE MESTRE
    já dizia (T2 equipe · T1 restrito · T0 privado), o console implementa: `sensitivity_tier` com
    CHECK constraint, T0/T1 invisíveis para a chave anon, promoção de tier sempre `EXIGE_JOAO`, e
    **marcadores de caminho que forçam rebaixamento automático** — `_PRIVADO`, `_RESTRITO`,
    `_SECRET`, `_T0`, `_T1`. A trava de importação recusa com HTTP 422 conteúdo contendo `t0`, `t1`,
    `sensitive`, `sensível`, `segredo`, `secret`, `token`, `service_role`. Isso é diretamente
    reaproveitável como padrão nosso — mas **não** foi adotado por conta própria (restrição de
    Vinicius: não copiar nada de lá).
97. **O Hermes tem 6 rotinas com cron rodando localmente, e uma delas é auditor de tamanho de MD.**
    `orphan-radar` (09:00, detecta órfãos operacionais no vault), `md-size-auditor` (09:00, audita
    tamanho/estrutura de MD e propõe splits), `catalog-index-maintainer` (10:00, o único
    `requires_joao`), `structure-distributor` (11:00, sugere destino BrainHub/uMode para MDs novos),
    `inbox-evaluator` (a cada 30 min, classifica inbox e roteia para a fila de aprovação),
    `validation-feedback` (12:00, converte feedback do João em correções rastreáveis). Todas
    `canonical_write: false`. **Os thresholds do auditor de MD, em palavras:** monitora 1.500,
    recomenda split em 3.000, split-ou-justifica em 5.000, crítico em 8.000
    (`EXIGE_JOAO_CRITICO_8K`). ⚠ Nota para nós: vários dos nossos arquivos já passariam desses
    limites — o `STATE.md` em especial.
98. **7ª fonte de "quem é cliente" — e 3 nomes que não existem em lugar nenhum nosso.** As filas de
    contexto do console nomeiam: **Hering** (tem casa), **Reserva** (tem casa), e **Malwee**,
    **Clube/SHP** e **CRM EducAI** — os três com **zero ocorrências** em todo o nosso repositório.
    `CRM EducAI` está tipado como `context_type: 'produto'`, não cliente. `SHP` reaparece nas skills
    do vault (`mbs-content-shp`), sugerindo que é frente com material próprio.
99. **⚠ Colisão de nome com "uFlow", que precisa ser resolvida antes de virar erro.** Existe no vault
    um `plano-migracao-uflow.md` cuja descrição é: "caminho do BrainHub Console atual (Lovable +
    Supabase temporário) para o ambiente uMode (workers, storage, secrets)". Ali **"uFlow" parece
    designar o ambiente/infra de destino**, não o PLM legado que Vinicius confirmou em 04 ago 2026.
    Pode ser uso frouxo do nome ou pode ser outra coisa com o mesmo nome. **Não resolvi** — mas é
    exatamente o tipo de colisão que a fase de reprocessamento de taxonomia tem de tratar, e que
    causaria erro grave se um agente cruzasse as duas coisas.
100. **Divisão de trabalho entre agentes de código, declarada e com regra de arbitragem** — vale
    registrar porque é decisão de método que já existe na Casa: Lovable faz scaffold de tela, UI,
    protótipo e iteração conversacional; Codex faz refactor multi-arquivo, edge function, contrato de
    API, migração Supabase e hardening. Arbitragem literal: **"Lovable já errou 2× → Codex"**. E
    duas regras: **"Nunca dois escritores no mesmo arquivo ao mesmo tempo"** e **"Lovable é
    governança/produto, não executor IA"**.
101. **Existe um loop de execução auditado rodando em CI, com a mutação real desligada.** Um
    `codex-executor` roda **Claude Code headless** (`claude -p`) a cada 15 min e por
    `repository_dispatch`, consome `approval_requests` aprovadas, aplica guarda determinística
    (bloqueia tier ≠ T2), produz o **plano** de promoção inbox→canônico, extrai veredito
    (`executed`/`exige_joao`/`failed`) e grava auditoria via RPC. **11 aprovações já processadas**
    (`.github/executed_approvals.txt`). A mutação canônica está atrás da flag `EXECUTE_MUTATIONS`,
    **hoje desligada** — é plan-only. Há também um `codex-auditor` que audita o diff a cada push
    (segredo versionado, RLS aberta, bug de produção, drift de design token), também report-only.
102. **Onde ainda existe informação a buscar, em ordem de densidade** (levantado pela leitura, não
    por suposição): (1) o vault `~/Documents/uMode-OS/` — `_GOVERNANCA.md`, `DECISOES.md`, a árvore
    `BrainHub/uMode/` e as pastas `skills/umode-vibe-coding-method`, `skills/mbs-content-shp`,
    `skills/mbs-sales-call`, `skills/mbs-session-delivery`; (2) o **Hermes** e seu
    `hermes-local-registry`, mais o script `brainhub_seed_cards.py` — nenhum dos dois está em
    repositório clonado; (3) o banco **Supabase `wjghatmsywcjvpumzonu`**, que tem 53+ cards de
    aprovação reais e 5 tabelas de observabilidade de agente **sem migration versionada** (o
    repositório não é fonte de verdade completa do banco); (4)
    `https://github.com/HyTrackWater/fashionpedia` e `designsystem.umode.tech`, dois projetos irmãos
    da mesma org **HyTrackWater**; (5) a **origem upstream dos cards de aprovação** — o schema exige
    `call`/`artefato` + `tema` por item, então existe uma fonte de **calls/reuniões classificadas por
    tema** que o console consome e nunca nomeia.
103. **Nota de organização, não de conteúdo:** o console do João **não executa nada de efeito real**.
    Toda intenção — vincular conhecimento, promover agente, envio externo, acesso de operador — vira
    linha em `approval_requests` ou `operator_requests` com `status='pending'`. O código declara:
    registra a solicitação e "NÃO chama CRM/Notion/e-mail e nunca declara sucesso de execução". É a
    mesma disciplina que aplicamos aqui ao separar "registrar" de "executar".

## IntHub e AlocAI — leitura dos repositórios (04 ago 2026)

104. **🔴 QUEM PODE DESBLOQUEAR A PRIORIDADE ZERO: `Bergson`, Squad Legado.** A documentação do
     IntHub o nomeia como responsável pela **manutenção do uFlow e pelo seu descomissionamento**, e o
     marca literalmente como **"(SPOF crítico)"**. É ele o dono dos dois riscos abertos do legado.
     Se alguém tem o repositório da plataforma uFlow e o schema do banco — os dois insumos que faltam
     para `D-2026-002` — é ele. Isso responde o item 83 com um nome.
105. **🔴 ACHADO CRUZADO QUE NENHUM DOS DOIS LADOS CONHECE: nós temos a chave que falta no IntHub.**
     O IntHub descobre falha de integração por **polling do MySQL legado**
     (`umode_production.jumper_integration_executions`, 218.655 linhas desde 2021), a cada 6h. Para
     dizer *de qual cliente* é a execução, ele depende de uma tabela de tradução manual,
     `legacy_entity_map` — que hoje tem **1 linha** (Lenny, `entity_id_externo = 3575`). Tudo o mais
     fica `cliente_id IS NULL`, e por isso a tela "Carteira" foi redefinida para agrupar por
     `class_name` da integração em vez de por cliente.
     **E os nossos 11 `integracao.md` carregam exatamente o identificador que falta:** `INTEGRATION_ID`
     **5** (NV), **21** (Baw), **22** (Lofty Style), **25** (Luiza Barcelos) — e o arquivo da VIX cita
     nominalmente a tabela **`jumper_integration_executions`**. Ou seja: **as integrações dos clientes
     escrevem sim na tabela que o IntHub observa**; o IntHub não é cego para elas, ele só não sabe
     nomeá-las. O de/para que preencheria `legacy_entity_map` está, em parte, no nosso repositório.
     ⚠ Registrado como achado, **não como ação** — popular tabela de produção de outro sistema não é
     coisa que se faça a partir de dedução; exige confirmação com a Squad Integração.
106. ✅ **RESOLVIDA em 04 ago 2026 — o uFlow é MySQL, e o glossário do IntHub está errado.** O
     documento de treinamento do agente (fonte de quem mantém a plataforma) e o próprio repositório
     confirmam: **Rails ~> 5.2 · Ruby 2.6.7/2.7.3 · MySQL (`mysql2`, `utf8mb4_unicode_ci`)**, com
     prefixo de tabela `umode_...` e réplica de leitura `*_standby` por ambiente. A hipótese que eu
     havia levantado estava certa: **MySQL é o banco da aplicação uFlow, e o SQL Server (porta 1433
     nas strings de erro) é o banco do ERP do cliente**. O que fica registrado é que o glossário do
     IntHub define uFlow como "Rails monolito + **SQL Server**" — **está incorreto** e merece
     correção na origem. Texto original da pendência, mantido como histórico:
     O glossário
     (`CLAUDE_PROJETO.md`) define uFlow como "Rails monolito + **SQL Server** — em fase de
     descomissionamento", mas a Edge Function de sync conecta em **MySQL** (`umode_production`,
     variáveis `MYSQL_*`). Ao mesmo tempo, as strings de erro reais das execuções mostram
     `Failed to connect to 192.168.9.200:**1433**`, que é porta de SQL Server — coerente com o
     glossário. Leitura possível: MySQL é o banco da aplicação uFlow e SQL Server é o banco do
     **cliente** (o ERP), e o glossário misturou os dois. **Não resolvi** — mas é informação crítica
     para `D-2026-002`, porque o agente precisa conhecer "a estrutura do banco de dados" e agora há
     dúvida sobre qual banco é qual. Também registrado: o sistema **novo** é "Node microsserviços +
     MongoDB M10 + AWS Elastic Beanstalk".
107. **🔴 RISC-001, aberto, owner Bergson: senhas de ERP em texto plano.**
     `umode_production.jumper_integrations.properties` guarda senhas dos ERPs dos clientes (Linx,
     Millennium, SAP, Totvs) em **YAML plaintext, em 24 linhas ativas**. Impacto declarado: "dump do
     MySQL legado expõe credenciais de todos os ERPs de clientes uMode". O IntHub se defende
     **nunca selecionando** essa coluna (SELECT explícito, verificado no schema do espelho) e também
     não trazendo `jumper_entities.api_token`. **RISC-003**, também aberto e do mesmo owner: proposta
     de arquivar as ~211k linhas pré-2025 (recomendação: mover para `_archive`, **não deletar**).
     Foi para `_backlog-infra-tecnologia.md`.
108. **A escala canônica de maturidade da uMode é outra que a nossa, e está no Notion.** Página
     `dc5980a5a5ce45fb826c261949c5cdd5` ("Engenharia de Software") define
     **Protótipo → Alpha → Beta → O&M**. O IntHub se declara "V0 (semVer 0.1.0) · **Maturidade alvo:
     Alpha → Beta**". O nosso enum travado é `Ideação` / `MVP` / `Escalável`. **Duas escalas
     coexistem** — a de produto (nossa) e a de engenharia (do Playbook). Não fundi. Precisa de
     decisão: são eixos diferentes (produto × engenharia) ou uma deve traduzir para a outra?
109. **⚠ Regra contratual que classifica retroativamente o incidente da VIX.** O **Anexo Técnico de
     Integração** (Notion `350b1d38e768816a815bd3807d0d3cfa`) define **Taxa de Urgência de R$ 300/h**
     e **30 dias úteis para mudança de IP**. A regra operacional derivada, escrita no IntHub: "quando
     um alerta `Client` recorrente envolve **mudança de IP do cliente sem aviso**, marcar como
     **violação de Anexo Tech** — abre **RFI obrigatório**".
     **É exatamente o caso VIX:** mudança simultânea de IP→hostname, share, domínio AD, credencial e
     VPN **sem aviso prévio**, 4 incidentes em 6 semanas, com RFI #83 e #85 abertas. O `integracao.md`
     da VIX registra os fatos; agora existe a **régra contratual** contra a qual eles se classificam.
     Vale aplicar — mas é decisão comercial/contratual, não de documentação, então fica registrado e
     não aplicado.
110. **Taxonomias operacionais novas, prontas para uso, que não estão nos nossos protocolos:**
     - **Classificação de alerta de integração (4 valores, travados por ADR-008):** `Client` (rede ou
       ERP do cliente) · `Process` (cadastro ou regra do parceiro) · `Engineering` (bug uMode) ·
       `Nao_Classificado`. Responsável: `Parceiro` | `uMode` | `Indefinido`. ⚠ Há proposta aberta de
       um 4º responsável, `Fornecedor`, divergindo do enum — é uma das 4 perguntas abertas do plano.
       **Isto é diretamente o que a `D-2026-002` precisa:** o agente de suporte tem de dizer "é
       configuração, é tech, ou é erro de dado" — e essa é a taxonomia que a operação já usa.
     - **Escala de severidade (Playbook):** SEV-1 indisponibilidade total ou perda de dado, SLA 5 min
       (Bergson age sem aguardar aprovação) · SEV-2 funcionalidade principal indisponível, 1h ·
       SEV-3 degradação · SEV-4 problema menor com workaround · SEV-5 cosmético. Mapeamento
       declarado: `Engineering` + frequência alta → SEV-2; `Client` + ERP indisponível → SEV-2;
       **`Process` fica fora de SEV** — "não é incidente uMode, é ação no parceiro".
     - **Status de execução de integração, com distribuição real medida** sobre 218.655 linhas:
       `success` 60,6% · `partial_success` 34,9% · `executing` 2,7% · `pending` 1,0% · `error` 0,7%.
       O farol trata `error` + `partial_success` como "o que importa" — 78 mil execuções.
111. **Estrutura de squads da uMode, com 3 de 5 sem owner** (Plano de Sucessão, abr/2026):
     **Integração** — Joao Ferraz e Felipe Sindeaux ("donos deste produto", o IntHub) ·
     **Plataforma** — TBD (auth, infra, observabilidade) · **Legado** — Bergson (SPOF crítico) ·
     **GC / Gestão de Conhecimento** — TBD (documentação, ADRs) · **Ideação** — TBD (produtos novos).
     ⚠ A squad **GC** é literalmente a função do BrainHub, e está sem dono.
     Cruzamentos com o que já tínhamos: **Joao Ferraz** é o mesmo "João Ferraz" responsável pelo
     Dicionário Oficial de Taxonomia; **Felipe Sindeaux** é provavelmente o "Felipe" que conduziu os
     contatos nos incidentes da VIX (sobrenome novo, vínculo não confirmado); **Marina Santoro** já
     tem ficha na Casa e aqui aparece como **operadora co-titular do IntHub**, com perfil descrito
     em detalhe. **Bergson** aparecia em 2 arquivos nossos e agora tem papel definido. Nenhum dos
     três novos tem ficha de Pessoa.
112. **`Lenny` é cliente real e piloto do IntHub, e não tem casa.** Slug `lenny`, tier Pro, segmento
     "Moda Praia / Vestuário", ERP **Linx**, início 2025-06-01, "cliente piloto, ingestão Discord
     ativa". No legado: `jumper_entities.slug = lenny-niemeyer`, `entity_id_externo = 3575`. Tem
     **10 auditorias com percentuais reais de correspondência** (79,7 → 98,3) e **2.513 alertas de
     Discord em 12 meses**. Aparece em 85 arquivos nossos (como nome em demanda), no ÍNDICE MESTRE do
     Notion (status `revisar`) e na base legada da Taxonomia (`Lenny Niemeyer`) — **quatro fontes** e
     nenhuma casa. É o candidato mais forte a cliente faltante.
113. ✅ **`IntHub` documentado — mas o nome "IntHub" não existe no repositório.** O produto se chama
     "**uMode Saúde de Integrações**" nos documentos, e o repositório é `integration-pulse-check`. O
     apelido IntHub não aparece em nenhum arquivo. É a quarta vez que nome de repositório, nome de
     produto e nome no Portfólio divergem. **Maturidade real: V0 (0.1.0), read-only, alvo Alpha→Beta,
     com todas as 18 caixas do checklist de fechamento do V0 desmarcadas**, e o seed populado à mão
     com 2 clientes (Lenny + "Cliente B"). Mas **há dado real em produção**: 4.252 execuções
     problemáticas espelhadas. Sem commits desde 27/05/2026. A camada de IA (Gemini) para diagnóstico
     automático está **apenas planejada** — zero implementação.
114. ✅ **`AlocAI` documentado — e a grafia nos documentos é `AlocaAI`, não `AlocAI`.** É ferramenta
     de **clusterização de lojas + alocação automática de mix por loja**: o usuário cria Cenários
     (regras em CRUD) que treinam um agente de match híbrido, que aplica as regras deterministicamente
     a custo zero e chama Gemini só nos produtos que nenhum cenário cobre; depois o usuário revisa
     arrastando no canvas. 7 telas (T01–T07). **Cliente âncora: Reserva**, com **987 filiais**;
     dono do processo do lado do cliente é **Justen**. Consome planilha XLSX (`Mix x Loja`, ~27.363
     linhas) e devolve XLSX no mesmo formato — **sem integração com ERP no V0**.
     ⚠ **O `CONTEXT.md` do próprio repositório está errado:** declara as 7 telas como "pendentes"
     quando existem 8 migrations e todas as telas implementadas. Quem detectou foi uma perícia por
     engenharia reversa (`MAPA_FUNCIONAL.md`, 10/07/2026), que se declara "documenta o que está
     implementado, não a intenção dos docs" — e mesmo ela não cobre os commits de 13/07/2026, que são
     de `vinicius-risoleo-umode`.
115. **⚠ Risco sistêmico observado nos dois repositórios, e que vale como lição para o nosso:** em
     ambos, o documento de estado (`CONTEXT.md`) e os de padrão (`AGENTS.md`, `PRD.md`) ficaram
     **desatualizados em relação ao código**, e em ambos isso foi detectado por auditoria posterior
     **sem que a correção fosse aplicada**. No IntHub, o `AGENTS.md` ainda manda usar Vite + React 18
     + Tailwind 3 quando o real é TanStack Start + React 19 + Tailwind 4 — o ADR-001 pede a correção
     e ela nunca foi feita. O único artefato dos dois repositórios que resolve isso é o
     `MAPA_FUNCIONAL.md` do AlocAI, justamente por declarar que documenta o implementado e não a
     intenção. **É o modelo a replicar aqui** — e é a mesma disciplina que já aplicamos ao validar
     por diff de headings em vez de confiar no que o script diz ter feito.
116. **Governança de agente de código INVERTIDA entre os dois projetos, com autorização nominal.** No
     **IntHub**: Lovable é o dev (é promptado, faz push), Claude Code é CTO/auditor e **não escreve
     `src/`**. No **AlocAI**: **Claude Code é o dev principal** (escreve front, schema e server,
     commita e faz push), e o Lovable "só faz scaffold + deploy, **NÃO é promptado**" — com a
     justificativa literal "autorizado pelo Operador (João) **para poupar crédito Lovable**", e a
     nota de que "a regra padrão 'Claude Code nunca escreve src/' **está suspensa aqui** por
     autorização explícita". O AlocAI tem ainda um 4º papel: "**Claude (Diretor)** — estratégia, para
     priorização e decisões de produto". Registro isto porque é **decisão de método já existente na
     Casa** sobre divisão de trabalho entre agentes, e o BrainHub vai precisar da sua.
117. **Fontes de informação novas, nomeadas, para a fila de enriquecimento:**
     - Notion `337b1d38e7688078b504c093a3afe85c` — catálogo manual de alertas de integração mantido
       por Marina, cuja coluna "Sugestão de Melhoria" **"vira RFI/roadmap produto"**. É origem de RFI.
     - Notion `350b1d38e768816a815bd3807d0d3cfa` — **Anexo Técnico de Integração** (ver item 109).
     - Notion `350b1d38e7688103b654fe7ffe6a6c52` — **Termo de Homologação de Integração**, "passagem
       Onboarding → Ongoing". É a fronteira formal de fase de cliente.
     - Notion `dc5980a5a5ce45fb826c261949c5cdd5` — Engenharia de Software, escala de maturidade.
     - Notion `329b1d38e7688196933bf46622cd8d7c` — Templates & Boas Práticas (já conhecido).
     - Drive `1VuHdqv70ZlvOroaArSl6J` — **36 PDFs + 7 XLSX** de auditoria diária Lenny × Linx,
       gerados por um "agente de auditoria uFlow × Linx" que já existe e que nós não conhecíamos.
     - **Playbook de Engenharia uMode** — declarado "LEI SUPREMA" e com **dois endereços diferentes
       nos dois repositórios** (`playbook.umode.app` e `umode.gitbook.io/playbook-de-engenharia`).
       Traz 7 princípios invioláveis, incluindo um que é irmão da nossa regra de ouro: **"nunca
       aceitar diagnóstico de IA sem evidência no código"**.
     - `~/Downloads/[uMode] Plano de Sucessão Engenharia.pdf` — squads, governança, SEV-1 a SEV-5.
     - `reserva-images.s3.amazonaws.com/B2B/Reserva/Images/` — bucket público de fotos de produto da
       Reserva, consumido pelo AlocAI.
     - Org GitHub **`HyTrackWater`** — é onde vivem todos esses repositórios.
118. **Glossário PLM × ERP pronto para virar Taxonomia institucional.** O
     `CONTEXT_LOVABLE_DOCS.md` do IntHub traz um glossário de domínio com PLM, ERP (Linx, Millennium,
     SAP, Bling, Totvs), Ficha Técnica, Variante (SKU = modelo + cor + tamanho),
     `PRODUTO_VERSAO_MATERIAL_COR`, `MATERIAL_PRINCIPAL`, `COR_MATERIAL` ("não confundir com cor do
     produto"), GRADE, NCM, CEST, EAN/GTIN, Coleção — e as **entidades canônicas de integração**:
     **7 de leitura** (MATERIAL, COR_BASICA, GRADE, FORNECEDOR, COLECAO, NCM, UNIDADE_MEDIDA) e
     **8 de escrita**. Isso bate exatamente com o que os 11 `integracao.md` documentaram cliente por
     cliente, e é o vocabulário que o agente da `D-2026-002` vai precisar. Candidato a alimentar a
     área `04_Dados-e-IA`.

## CX Hub — leitura do repositório real (04 ago 2026)

119. ✅ **CONFIRMADA a hierarquia do CX Hub, com duas correções de nome.** O schema real
     (`src/integrations/supabase/types.ts` + 170 migrações) é:
     `programs` → `program_milestones` (NOT NULL, CASCADE) **e** `projects` (`program_id` **nullable**,
     SET NULL) → `demands` (`project_id`, `program_id`, `program_milestone_id` todos **nullable**) →
     `demand_tasks`.
     - **Correção 1: "Subdemanda" = `demand_tasks`, e não uma demanda-filha.** O próprio repositório
       usa esse nome ("Subdemandas (demand_tasks) nao tem colaboradores"; UI: "Adicionar subdemanda").
       `demand_tasks` tem status próprio (`open`/`in_progress`/`done`), horas e posição — **não tem
       cliente, tipo, coluna nem prioridade**. Não é uma demanda. **Isso valida o nosso modelo**, que
       já trata `Subdemandas` como checklist dentro do mesmo card.
     - **Correção 2: no domínio de Programas o vocabulário da UI é outro.** `projects` aparecem como
       "features"/"Projetos" e as demandas dentro de um programa são chamadas de **"Sub-item"**. Ou
       seja: Programa → Marcos + Projetos ("features") → Demandas ("sub-itens") → Subdemandas.
     - **Demanda solta** = os três FKs nulos. Não há CHECK forçando; é a RLS que aceita dois ramos:
       **ou** a demanda tem cliente (ramo CX, pode estar solta), **ou** não tem cliente e então precisa
       de `program_id` (ramo programa interno). `demands.client_id` **deixou de ser NOT NULL** em
       05/06/2026.
     - ⚠ `source_demand_id` **não é subdemanda**: é auto-referência para "task TECH originada de uma
       demanda de cliente". Nosso campo `Demanda mãe` provavelmente mapeia para **isto**, não para
       hierarquia de programa — a distinguir antes de qualquer proposta.
120. **⚠ A RFI do CX Hub contraria em parte a nossa decisão de "RFI dentro da Demanda".** `rfis` é
     **tabela própria** com um **CHECK XOR**: `(demand_id IS NOT NULL) <> (project_id IS NOT NULL)`.
     Toda RFI pertence a **exatamente uma Demanda OU exatamente um Projeto**, nunca aos dois, nunca a
     nenhum. Uma Demanda tem no máximo 1 RFI (índice único parcial). **Consequência:** existe RFI que
     não tem demanda nenhuma — pertence direto a um Projeto. O nosso modelo, que move a RFI para
     dentro da Demanda, não representa esse caso. Histórico útil: antes de 31/03/2026 a RFI era só um
     campo `demands.rfi_url` (texto livre), migrado para a tabela e o campo dropado.
     **Numeração:** `RFI-NNNN`, gerada por trigger no banco.
121. **🔴 `demands` NÃO TEM coluna de status — e isso explica o conflito Status × Etapa do dado
     legado.** O estado da demanda é a combinação de `column_id` (a coluna do Kanban) +
     `finished_at` + `cancellation_reason` + `is_blocked`. O status "concluído/cancelado/bloqueado/
     aberto" é **derivado em RPC**, com ordem de precedência explícita: `cancellation_reason` →
     `finished_at` → `is_blocked` → senão `aberto`. Nosso protocolo tem `Status` e `Etapa` como campos
     separados e criou a regra "Status prevalece, Etapa só refina" para resolver conflitos do legado.
     **Agora sabemos por quê havia conflito: no CX Hub não existem dois campos — existe uma coluna de
     Kanban e um status calculado.** A regra que criamos continua servindo para o dado legado, mas o
     modelo real é outro.
122. **✅ OS ENUMS REAIS, e o que eles fecham.** Esta é a entrega mais direta da leitura:
     - **`demand_priority` = `low` · `medium` · `high` · `urgent`.** ✅ **Fecha a lacuna** que dizia
       "`Prioridade` sem equivalente para `Baixa`": existe `low`. Com SLA default por prioridade em
       `demand_priority_config`: **Urgente 2h · Alta 4h · Média 8h · Baixa 24h**.
     - **`blocker_types` (motivo de bloqueio), seed real de 5 valores:** `Aguardando cliente` ·
       `Dependência técnica` · `Infra / Ambiente` · `Aguardando decisão` · `Dependência externa`.
       ✅ **Nosso enum tem 4 dos 5** — falta **`Aguardando cliente`** — e tem um `Outra` que **não
       existe no catálogo real**. ⚠ Não confundir com a outra lacuna registrada ("a fonte tem 8
       valores"), que era sobre valores encontrados no **dado legado do Notion**, não neste catálogo.
       São duas coisas: o catálogo é configurável em Settings, e `demands.blocker_reason` segue
       existindo para texto livre complementar.
     - **`demands.delay_reason`, lista fechada de 7 valores que nós não temos como campo:**
       `Entraram urgências` · `Dependência externa` · `Escopo maior que previsto` ·
       `Falta de decisão` · `Bloqueio técnico` · `Aguardando cliente` · `Outro`.
     - **`demand_types` com prefixo de código:** Suporte→`SUP` · Configuração→`CON` · Bug→`BUG` ·
       Melhoria→`MEL` · Feature→`FEA` · Comercial→`COM` · Investigação Técnica→`INV` · Migração→`MIG`.
     - **`rfi_statuses`, seed real de 4 valores:** `Previsto` · `Orçada` · `Aceito` · `Recusada`.
       ⚠ **Divergem por completo dos status de RFI que traduzimos do legado** (`RFI Aceita — Criar
       Demanda e Estimar Entrega`, `RFI Não Iniciada` etc.). Duas taxonomias de status de RFI: a do
       Notion legado e a do CX Hub atual. Não fundir sem decisão.
     - **`demands.workspace` = `cx` · `tech`** (default `cx`); áreas e projetos aceitam também `both`.
     - **`demand_tasks.status` = `open` · `in_progress` · `done`.**
     - **`demand_relationships.relationship_type` = `blocks` · `related` · `linked`.**
     - **`clients.status` = `ativo` · `inativo` · `trial`** — controle 100% manual, independente de
       `active`.
     - **`client_tier` = `azzas` · `enterprise` · `medium` · `small`** — ⚠ `azzas` é valor de enum, o
       que confirma o grupo AZZAS como categoria de negócio, não só nome de cliente.
     - **`channel_type` = `gist` · `discord` · `whatsapp` · `email` · `transcription_gemini` ·
       `transcription_tactiq` · `manual`** e **`tone_severity` = `ok` · `atencao` · `alerta` ·
       `critico`**.
     - **14 temas de classificação IA:** `integracao_erp`, `agendamento`, `permissoes`,
       `cobranca_followup`, `gestao_demandas`, `workflow`, `importacao_dados`, `intermediacao`,
       `bugs`, `criacao_campos`, `treinamento`, `elogio`, `governanca`, `outro`.
123. **🔴 EXPLICAÇÃO DEFINITIVA para o eixo de Área estar vazio: `ticket_columns` e `demand_areas`
     NÃO TÊM SEED.** São 100% configuráveis pelo admin em Settings, e o código **deliberadamente
     evita nomes fixos** — `src/lib/columnFlow.ts` declara "No hardcoded names or positions — works
     for any workspace (cx / tech)". Ou seja: **a lista de Áreas e de Etapas do CX Hub não existe em
     nenhum documento nem no código — vive só no banco de produção.** Isso encerra a tentativa de
     validar o nosso enum de `Área (CX Hub)` contra fonte documental: não há fonte documental. Para
     obter os valores reais é preciso consultar o banco (`qyfwbmukylyfsgzgocfo`) ou a tela de
     Settings. Vale para `demand_origins` também (catálogo criado sem seed).
     As colunas do Kanban carregam 3 marcadores booleanos que dão semântica de fase:
     `triggers_started_at` ("Início Dev") · `triggers_finished_at` ("Fim") · `triggers_sla_response_at`
     ("Fim SLA").
124. **✅ Chaves humanas estáveis do CX Hub, que o BrainHub pode usar para referenciar:**
     demanda = **`PREFIXO-NNNN`** (ex. `BUG-0042`, `SUP-0113`, `MEL-0007`), RFI = **`RFI-NNNN`**,
     programa = `code` único (ex. `MIGRACAO`), marco = `code` único por programa. Todos gerados por
     trigger no banco.
     ⚠ **E aqui um problema de precisão nosso:** o campo dos nossos MDs se chama
     `ID legado (Notion/CX Hub)` e, numa amostra de 400 demandas, **399 têm o formato `UMD-N`** — que
     é o ID do **Notion**, não o código do CX Hub. **São dois sistemas de identificador diferentes
     conflados num campo só.** `UMD-970` não resolve para nenhuma demanda do CX Hub. Se quisermos
     vincular de verdade, precisamos de um segundo campo com o código `PREFIXO-NNNN`.
125. **🔴 NÃO EXISTE API para criar demanda no CX Hub, e não existe idempotência.** Verificado: nenhuma
     Edge Function faz INSERT em `demands` — o único caminho de escrita é **PostgREST**
     (`POST /rest/v1/demands`) com **JWT de usuário autenticado**, passando pela RLS. Campos
     obrigatórios: `title`, `demand_type_id`, `column_id` (+ `client_id` ou `program_id`+admin para
     passar a RLS). **Não há `external_id`, chave natural, UNIQUE de dedup nem `ON CONFLICT` em
     `demands`: reenviar o mesmo POST cria uma segunda demanda.** O princípio de idempotência do PRD
     vale para `interactions` (via `external_id`), **não** para demandas.
     Isso responde diretamente a dívida de infra que previa "criação de card no CX Hub pós-aprovação":
     **a API não existe e a idempotência não existe** — as duas precisam ser construídas. A única API
     exposta hoje é de **leitura**: `client-demands-public`, autenticada por **token opaco na query
     string**, com CORS `*` por decisão de produto ("acessado de domínios de clientes externos").
126. **🔴 Três críticos de segurança abertos no CX Hub, "exploráveis por qualquer authenticated
     user", e dois bloqueadores de produção declarados.** O próprio `CONTEXT.md` do repositório
     alerta: "3 criticos abertos (CTX1, CTX2, CTX3) e 3 altos abertos… Os criticos sao exploraveis
     por qualquer authenticated user", e nomeia **CTX1** (CX Analytics RLS) e **CTX6**
     (`deactivate_stale_clients` sem guard) como **bloqueadores para produção**. A auditoria de
     07/05/2026 fecha: Crítico 4 (1 corrigido, 3 abertos) · Alto 4 (0 corrigidos) · Médio 11 (0) ·
     Baixo 18 (0). Foi para `_backlog-infra-tecnologia.md`.
127. ✅ **VERIFICADA e não é falha — o `.env` versionado do CX Hub é decisão declarada.** O arquivo
     existe mesmo no repositório de origem (`git ls-files` confirma), e o `.gitignore` traz o motivo
     escrito: **"Environment variables — .env com VITE_* (chaves publicas) fica no repo"**, com
     `.env.local`, `.env.*.local`, `.env.production` e `.env.staging` todos ignorados. Ou seja: só as
     chaves públicas de build ficam versionadas, e os arquivos de ambiente real estão fora. **Não
     abri o conteúdo.** ⚠ **Risco residual, esse sim real:** o padrão só funciona enquanto ninguém
     adicionar por engano uma chave não-pública nesse arquivo — e não há verificação automática
     impedindo. Somado ao achado do IntHub (chave anon e URL do projeto **hardcoded no corpo de uma
     função `SECURITY DEFINER`**, quando o padrão do próprio repositório era usar placeholder), a
     recomendação é uma verificação de segredo no CI, não uma correção pontual.
128. **⚠ Perda de dado irreversível já ocorrida no CX Hub, registrada como lição — e a regra que a
     evita.** `CTX4`: um DELETE em massa de `interactions` anteriores a 01/01/2026 **sem** o filtro
     obrigatório `metadata->>'auto_created' = 'true'`, marcado em `PENDENTES.md` como "EXECUTADO
     (lição)". A regra crítica de proteção declarada no PRD é: **toda operação destrutiva em massa
     deve filtrar `auto_created`**. É o mesmo princípio que aplicamos aqui ao nunca reescrever
     histórico de sessão e ao tratar o índice como derivado.
129. **A identidade declarada do CX Hub contradiz o que ele virou.** O PRD afirma "**Não é um
     helpdesk/ticketing system** (não substitui Gist, Zendesk etc.)" e "é um **hub analítico e de
     auditoria** que CONSOME dados de outros sistemas". Mas as fases 7 a 7.10 construíram exatamente
     um sistema de tickets: Kanban, SLA, apontamento de horas, projetos, programas e RFI. **O PRD
     nunca foi atualizado.** Isso importa para nós porque a nossa premissa — "todas as demandas
     executáveis são criadas no CX Hub" — está correta na prática e **contradita no documento de
     produto** dele.
130. **⚠ Mesmo risco sistêmico dos outros repositórios, e aqui é o maior de todos:** o `CONTEXT.md` do
     CX Hub é **v30, de 07/05/2026**, e existem **~40 migrações posteriores** (até **04/08/2026**, o
     último commit foi hoje). Todo o módulo **Programas / Marcos / DoD / Testes de marco / Origens /
     Weekly Planning** existe no schema e no frontend e **não está documentado**. O
     `docs/PROJECT_STATUS.md` é ainda mais antigo (v0.3.0, 04/03/2026) e descreve o produto como "Hub
     de Integrações Multi-App" com páginas que hoje não existem. **Consequência prática para nós: a
     hierarquia Programas → Projetos que o Vinicius informou é REAL no código e AUSENTE na
     documentação do próprio CX Hub.**
131. **Escala e volume real do CX Hub, para dimensionar a fonte:** **2.495 commits**, 170 migrações
     SQL, último commit **04/08/2026**. **21.262 mensagens classificadas** + ~11.829 históricas fora de
     escopo (~33k em ~1.680 conversas), ~117 conversas/mês, **13 clientes ativos** nas regras de
     auditoria, **196 demandas** do tipo Migração no backfill, 22 páginas de frontend, 19 Edge
     Functions. Custo de IA declarado: ~US$ 2,22 no backlog + ~US$ 0,16/mês.
132. **O classificador de IA do CX Hub é um ativo institucional documentado, com nota medida.** O
     `MEGA_AGENTE_v2.md` (292 linhas) é o **system prompt completo** do classificador: 14 temas com
     regras de desambiguação, rubrica de tom em 4 níveis, faixas de sentimento de −1.0 a 1.0, **13
     regras anti-viés** (ex.: "urgência operacional ≠ agressão", "volume ≠ pressão", "encerramento
     positivo ancora o tom") e 7 exemplos few-shot. Blind test com 32 conversas: **nota 9,0 · tom 84% ·
     tema 84%**. ⚠ O arquivo é "v2" mas o prompt em produção é referido como **v6**, e o v6 **não está
     versionado em arquivo** — vive na tabela `classification_prompt_config`. Modelo: Gemini
     (`2.5-flash` no código, `2.5-pro` no CONTEXT) com fallback `claude-sonnet-4`; decisão registrada
     de **não usar OpenAI** ("a variável `OPENAI_API_KEY` não existe neste projeto").
     **Relevante para `D-2026-002`:** já existe na Casa um prompt de agente maduro, medido por blind
     test e com regras anti-viés explícitas — é o modelo de rigor a seguir para o agente de suporte.
133. **Duas taxonomias de "área" convivem no CX Hub sem relação de dado:** `demand_areas` (área
     responsável, com `workspace` cx/tech/both) e `demand_origins` (catálogo separado, criado em
     19/06/2026, com vínculo N:N via `demand_origin_links`; o comentário SQL diz que "espelha
     demand_areas"). **Isso é irmão da nossa regra travada de nunca fundir Área organizacional com
     Área do CX Hub** — só que agora são três taxonomias de área no total.
134. **Decisões datadas do CX Hub que valem para o cérebro:**
     - **17/03/2026** — Cursor descontinuado; Lovable assume escopo total; "Claude Code NUNCA edita
       código-fonte, apenas gera prompts para Lovable"; commits vão direto para `main`, sem PR.
     - **31/03/2026** — **transição de Operador: Victor assume como Operador, João assume
       Estratégia**, e "Victor tem autonomia para atualizar `CONTEXT.md` (não `AGENTS.md` nem
       `CLAUDE.md`)". Victor Aragão tem ficha na Casa; este é o vínculo de papel dele.
     - **05/05/2026, 11:30 → 11:47** — **experimento de Squads abortado no mesmo dia**: tabelas
       criadas às 11:30 e derrubadas com DROP CASCADE às 11:47, `demands.squad_id` removido. O próprio
       `CONTEXT.md` comenta: "Disciplina excelente."
     - **05/06/2026** — nascimento do módulo Programas; `demands.client_id` deixa de ser obrigatório;
       seed de **um único programa: `MIGRACAO` — "Migração de Clientes", target 31/08/2026**. ⚠ Esse
       programa é o contexto operacional da migração legado→novo que atravessa todo o nosso trabalho.
     - **05/05/2026** — `CTX3`: mudança de semântica da função core de RLS
       (`user_accessible_client_ids` passa a aceitar `bypass_client_access`) **sem trilha de
       aprovação**. O repositório deixa a pergunta aberta, literalmente: "**Quem decidiu, quando, e
       por que?**" — segue sem resposta.
135. **Clientes citados no CX Hub e o estado da casa:** `Caedu`, `Osklen`, `NK Store` e `Reserva` têm
     casa. **`Grupo Soma` não tem casa e é nome novo** (nunca apareceu em nenhuma fonte anterior).
     `By NV` é quase certamente a nossa `NV` — a marca comercial é "By NV" (a própria integração da NV
     aponta para `backend--bynv.myvtex.com`); variação de nome, não cliente novo. O `AGENTS.md` marca
     By NV como "cliente real da uMode — foco atual do CX Hub, **dados nunca apagáveis
     acidentalmente**".

## uFlow — o que o schema real revelou (04 ago 2026)

136. ✅ **Repositório e schema da uFlow recebidos e mapeados.** `C:\Ambientes Virtuais\uFlow\umode-flow`
     — 12.613 commits, último em **03/08/2026 por `Bergson`**. **211 tabelas**, 443 migrations, 162
     models. Mapa completo em `uMode/04_Dados-e-IA/_contexto/uflow-modelo-de-dados.md`. Isto desbloqueou
     a `D-2026-002` (subdemandas 1 e 2 concluídas).
137. **⚠ CORREÇÃO À FONTE DE TREINAMENTO, e é a mais consequente de todas: `umode_` não é a convenção
     do banco.** O documento de treinamento do agente diz "prefixo de tabela geralmente `umode_...`".
     No schema real: **`umode_` = 119 de 211 tabelas (56%)** e **`jumper_` = 63 tabelas**, que são
     justamente o **núcleo da plataforma** (tenant, usuário, política, workflow, tarefa, arquivo,
     comentário, integração). **Não existe nenhuma tabela `j3_`** — `J3` é só namespace Ruby, e
     `app/models/j3.rb` resolve o prefixo para `jumper_`. Armadilha derivada:
     `app/models/j3/user_role.rb:29` declara `self.table_name = 'user_roles'` e **a tabela real é
     `jumper_user_roles`**. **Um agente que assumir `umode_` erra em 44% do banco.** Correção já
     aplicada em `agente-suporte-uflow.md`; a fonte original **não foi alterada** (não é nossa).
138. **A uFlow é a reescrita de um app PHP/Laravel chamado "Jumper" — e isso liga duas fontes que não
     se conheciam.** Evidência no schema: as 63 tabelas `jumper_*` são o núcleo herdado, e sobraram
     `laravel_jobs`, `laravel_failed_jobs`, `migrations` (tabela de controle do Laravel) e `sessions`,
     todas mortas no Rails. **Nada disso está no `README.md`.** Cruzamento: a página "Taxonomia" do
     Notion documenta "Actions do Jumper (legado uFlow)" com anexo `JUMPER_ACTIONS.txt` — é o mesmo
     legado visto do outro lado. **"Jumper" é o legado dentro do legado.**
139. **🔴 `db/schema.rb` NÃO é a fonte de verdade completa do banco.** Faltam **4 tabelas**,
     descobertas pelos headers `annotate` dos models — e a mais grave é **`jumper_policies`**, a tabela
     de permissão da plataforma inteira, para a qual apontam `umode_suppliers.policy_id`,
     `jumper_user_roles.policy_id`, `jumper_scoped_models.policy_id` e `umode_error_logs.policy_id`. As
     outras: `jumper_entities_invites`, `umode_user_brands`, `umode_user_collections`. **E 6 das 8
     views `vw_*` também estão fora**, inclusive duas usadas em SQL cru dentro de
     `purchase_order.rb:150-157`. **Um `db:schema:load` num ambiente novo produz uma aplicação que não
     sobe.** Dívida estrutural de primeira ordem, e limite direto do que o agente pode afirmar.
140. **🔴 A premissa "quase tudo pertence a uma entity" não se confirma: 122 das 211 tabelas (58%) não
     têm `entity_id`.** Só 89 têm, e apenas **41 FKs** apontam para `jumper_entities` (de 216 no
     total). Não há RLS, schema-per-tenant nem `search_path` — **a integridade de tenant é garantida
     pela aplicação, não pelo banco**. Subsistemas inteiros sem tenant: **todo o kanban** (10 de 11
     tabelas `jumper_workflow_*`), **todo o detalhe de custo**, **os 26 pivots**,
     `jumper_custom_field_values`, `umode_measurement_values`, toda a família `validation_*`, e
     **`jumper_users`** (usuário é global; o vínculo com cliente vive só em `jumper_user_roles`).
     Consequência: **um bug de escopo em qualquer caminho sem `entity_id` vaza dado entre clientes sem
     que o banco reclame** — e o controller de `integration_executions` já busca por id global, sem
     escopo de entity.
141. **✅ CIRCUITO FECHADO: descoberto como os 10 repositórios de integração se ligam à uFlow.** A uFlow
     expõe `POST` e `PATCH /api/v1/integration-executions`
     (`app/controllers/api/v1/j3/integration_executions_controller.rb`). Os 10 repositórios de
     integração são **Lambdas externas que gravam ali por HTTP**, e o `INTEGRATION_ID` que documentamos
     nos `integracao.md` (**5** NV · **21** Baw · **22** Lofty Style · **25** Luiza Barcelos) é o
     `jumper_integrations.id`. Fluxo completo: **Lambda do cliente → API da uFlow →
     `jumper_integration_executions` → polling do IntHub via MySQL.** Confirmação lateral: dentro da
     uFlow só existem runners **Millenium** (`app/services/integration/millenium_*.rb`) — Linx, SAP,
     SPI e Safe Tech vivem só nas Lambdas. **Isto completa o item 105**, que registrava a ligação como
     hipótese: agora é mecanismo documentado.
142. **🔴 Quatro propriedades de `jumper_integration_executions` que explicam o comportamento do
     IntHub — e por que o polling dele não escala.** (a) **Não tem `entity_id`**: o tenant só sai por
     JOIN `executions → integrations → entity_id`, o que é a explicação estrutural de por que a tela
     "Carteira" foi redefinida para agrupar por `class_name` em vez de por cliente. (b) **Não tem
     `deleted_at` e não há expurgo em nenhuma das 443 migrations** — é append-only e só cresce
     (218.655 linhas medidas pelo IntHub). (c) **O único índice é `integration_id`**; `status`,
     `executed_at`, `created_at` e `updated_at` **não têm índice**, e o controller ordena por
     `updated_at DESC` — **full scan**. (d) Soft-deletar uma integração **deixa as execuções órfãs de
     tenant**, porque o pai tem `deleted_at` e a filha não. **Status possíveis** (`enumerize`, sem
     CHECK no banco): `pending` · `executing` · `partial_success` · `success` · `error`.
143. **⚠ `integration_id` é dois campos diferentes com o mesmo nome — armadilha séria.** Em
     `jumper_integration_executions` é FK para `jumper_integrations`. Mas **18 tabelas de negócio têm
     uma coluna `integration_id` que é `string` e guarda o ID do registro no sistema externo** (chave
     de de-duplicação de importação), **sem nenhuma relação com `jumper_integrations`**:
     `umode_products`, `umode_suppliers`, `umode_fabrics`, `umode_collections`, `umode_colors`,
     `umode_grid_sizes`, `umode_measurement_tables`, `umode_product_approvals`, `umode_accessories`,
     `umode_brands`, `umode_prints`, `umode_product_types`, `umode_accessory_types`,
     `umode_fabric_types`, `umode_material_packages`, `umode_checklist_fillings`, `jumper_leads` e
     `umode_hierarchies`. Pior: **`umode_hierarchies.integration_id` é `integer`** e as outras 17 são
     `string`. E **nenhuma das 18 tem índice**, apesar de ser exatamente a coluna que um importador
     consulta a cada linha.
144. **🔴 "Lacre" NÃO existe no banco — é convenção de nome de campo customizado, por cliente.** Não há
     tabela, coluna nem model com `seal`/`lacre`/`sealed`. O lacre é implementado como custom field de
     nome acordado — **`lacre_checklist`** e **`data_lacre_checklist`** — buscados via
     `fetch_checklist_custom_fields(current_entity, ...)` em
     `app/helpers/checklist_fillings_helper.rb:70`, `app/reports/checklist_filling_report.rb:11` e
     `app/views/checklist_fillings/_list.html.slim:6`. Há ainda `alt_pos_lacre` numa definição de ficha
     e uma coluna de kanban "Produto Lacrado" nas fixtures.
     **Por que isto é grave para a nossa documentação:** o lacre é etapa central do nosso vocabulário —
     o `produto.md` do **DesenvolvAI** descreve o módulo como "croqui → **lacre**", e CriAI e CadastrAI
     dependem dessa fronteira. **Descobrimos que ela não é entidade de dados.** Um cliente que renomeie
     o campo quebra o relatório. Precisa ser registrado como **regra de negócio frágil** nos
     `produto.md` afetados — não fiz por conta própria porque muda a descrição de 3 Soluções.
145. **🔴 Configuração por cliente é regra-como-dado, e isso muda a pergunta.**
     `jumper_active_form_templates.definition` guarda **a estrutura inteira da ficha técnica de um
     cliente como YAML numa célula `mediumtext`**. Somado a `jumper_custom_fields` + `_values`,
     `jumper_policies.rules`, `jumper_actions.trigger`/`action_params`, `umode_validations.condition`,
     `business_rules.content` e `jumper_workflow_column_restrictions` — tudo é regra guardada como
     dado, **nada indexável nem validável pelo banco**. Consequência: **"que campos o cliente X tem"
     não é pergunta de schema, é pergunta de conteúdo de linha.** Isso também explica por que a
     varredura de campos por cliente que fizemos nos ERPs não tem equivalente do lado da uFlow.
146. **⚠ `jumper_entity_configs.deleted_at` é `t.string`** — a **única** coluna `deleted_at` do tipo
     string em todo o schema (as outras 147 são `datetime` ou `timestamp`). `acts_as_paranoid`
     comparando string com timestamp é bug silencioso — e está justamente na tabela que a fonte de
     treinamento chama de **"a razão nº 1 de funciona pra um cliente e não pra outro"**.
147. **⚠ O CATÁLOGO DE ENTITYCONFIGS NÃO FOI LEVANTADO — é a lacuna de maior valor que resta.** A
     varredura que enumeraria todas as `EntityConfig` usadas no código **morreu no limite de crédito da
     organização** em 04 ago 2026, sem produzir resultado. A única config conhecida por nome continua
     sendo **`product_manufacturer_supplier_status`** (Osklen, `entity_id = 3580`). **Enumerar essas
     configs é enumerar onde o comportamento muda por cliente** — alimenta o agente e os
     `institucional.md` ao mesmo tempo. É a primeira coisa a retomar quando houver crédito.
148. **Observações de segurança que o schema expõe** — foram para
     `_backlog-infra-tecnologia.md`; nenhum valor foi extraído:
     - **`jumper_integrations.properties` (YAML) é onde ficam as credenciais de ERP por cliente.** Isto
       **confirma no nível do schema** o `RISC-001` que a documentação do IntHub registra como aberto
       (owner Bergson).
     - **`jumper_entities.api_token`** é token em coluna `string`, aparentemente sem hash.
     - **`jumper_users` tem duas colunas de senha:** `password` (string(191), provável resíduo do
       legado Laravel) e `encrypted_password`. Vale verificar se a primeira ainda é populada.
     - **`umode_product_cost_sheets.value_cents` é `t.float`**, apesar do sufixo que implica integer, e
       `money-rails` não está no `Gemfile`. **Todo cálculo de custo carrega erro de ponto flutuante.**
     - **O banco operacional dos clientes carrega o banco comercial da uMode:** `jumper_customers`,
       `jumper_customer_invoices`, `jumper_subscription_plans`, `jumper_leads` e `jumper_pipedrive_deals`
       (CRM com integração Pipedrive) vivem lado a lado com ficha técnica de cliente.
149. **`umode_products` é STI e guarda quatro coisas** — `Product`, **`PurchaseOrder`**,
     `ProductBundle` e `ProductTemplate`, separadas por `type` (string(17)). **O pedido de compra é uma
     linha em `umode_products`.** Qualquer contagem de produto sem filtrar `type` infla o número — vale
     para qualquer métrica que a gente venha a extrair da uFlow.
150. **Duas trilhas de histórico concorrentes, e nada diz qual é autoritativa.** `audits` (gem
     `audited`, 97 models, polimórfico, com **`sudo_user_id`** para impersonação e **`request_uuid`**
     para correlacionar um request inteiro — mas **sem `entity_id`**, então não dá para listar "tudo que
     mudou no cliente X") e **`umode_product_history`** (só produto, `changes` em json nativo, **com
     `entity_id`**, sem model anotado).
151. **~9 tabelas são legado morto candidato a remoção:** o workflow antigo (`umode_workflows`,
     `umode_workflow_columns` e 3 pivots — todo workflow vivo está em `app/models/j3/`) e o bloco
     Laravel (`laravel_jobs`, `laravel_failed_jobs`, `migrations`, `sessions`). **73 tabelas do
     `schema.rb` não têm model anotado**, o que inclui o subsistema `shop_` (7 tabelas, 4 models) —
     sugere "loja" parcialmente implementada.
152. **O trabalho mais recente no banco da uFlow é reconciliação de custo de material.** Última
     migration em **17/06/2026**, e as duas mais recentes criam e evoluem
     `umode_product_cost_pending_updates` (`previous_price`, `new_price`, `detected_at`, `resolved_at`,
     `ignored_at`). Isso existe porque as linhas de BOM (`umode_product_fabric_variants`,
     `umode_product_accessory_variants`) **desnormalizam preço e composição do material de origem** —
     preço divergente **não é bug, é o design**. Confirma que o problema é **ativo, não histórico**.
     Antes disso houve intervalo: as migrations de 2025 terminam em 13/11/2025.

## Banco do BrainHub — o que o código revelou (17 ago 2026)

153. ✅ **FECHADAS por leitura de código: as coleções que eu dizia faltar existem.** O clone da API
     veio com `--single-branch` (1 branch local contra **114** no remoto). Na branch mais completa,
     `codex/bhp-p16-federation-grants-back` (17/08), há **29 módulos e 49 schemas**. Existem
     `tenants`, `brains`, `people`, `memberships`, `areas`, `area_memberships`, `approvals`,
     `audit_events`, `context_versions`, `context_relations`, `triggers`, `routines`, `trash`,
     `context-packs`, `folders`, `invitations`, `federation-*`, `agents`, `loops`, `agent-execution`,
     `llm-connections` e mais. Dicionário completo em `_dicionario-dados-brainhub.md`.
154. **⚠ REGRA NOVA, gravada no `CLAUDE.md`: ausência de fonte é hipótese, não conclusão.** Foi a
     segunda vez que declarei indisponível uma fonte que existia — a primeira foi o export de julho
     das demandas, que estava no histórico do Git. Antes de escrever que algo não existe: conferir
     `git log --all`, `git config --get remote.origin.fetch` e `git ls-remote --heads`. E **nunca
     transformar não-achado em tarefa para outra pessoa** — cheguei a sugerir cobrar do Bergson uma
     divergência que não existia. Retratado.
155. **🔴 O QUE FALTA NO BANCO SÃO QUATRO COLEÇÕES.** Varredura das 114 branches por módulo **e** por
     nome de arquivo: **`demand`/`task`**, **`addressing`**, **`inbox`** e **`notification`** não
     existem em nenhuma. Tudo o mais que o fluxo precisa está construído. **A plataforma resolveu
     contexto, governança e execução; não resolveu trabalho** — quem faz o quê, até quando, e como
     fica sabendo. É exatamente o objetivo declarado por Vinicius para a semana.
156. ✅ **A fronteira inviolável Personal Brain × empresa é invariante de schema, não policy.** O
     `brains.pre('validate')` impede: `PERSONAL` exige `ownerPersonId` e **não pode ter `tenantId``;
     `SECOND_BRAIN` exige `tenantId` e **não pode ter owner**. Mais dois índices únicos parciais: um
     Personal Brain por pessoa, um Second Brain por tenant. Isso responde a preocupação que eu havia
     levantado de que a regra do plano §5.1 fosse apenas policy de aplicação.
157. **⚠ O modelo de permissão real é mais granular que o MOLE e que os 5 níveis do PRD, e nenhum
     documento o descrevia.** `area_memberships` tem **três listas de tier separadas**:
     `readableTiers`, `writableTiers` e **`decisionTiers`**, com comentário no código dizendo que
     "autoridade de decisão é separada de escopo de leitura e escrita". Mais `grants[]`, `grantedBy`,
     `validFrom`, `expiresAt` (validado como maior que `validFrom`) e `role` `ADMIN|MEMBER`.
     **Isto substitui a proposta que eu havia feito** de híbrido MOLE + níveis do PRD.
158. **`D85` — decisão que eu não conhecia: tiers travados em T2.** Vale para `area_memberships` (as
     três listas) e para `context_relations`, e é **trava executável no `pre('validate')`**, não
     aviso: qualquer tier ≠ T2 é invalidado, "until enforcement for T0/T1 is delivered". Ou seja: a
     política de T0/T1 do João é bloqueio real de produto hoje.
159. **✅ A vazão de aprovação deixou de ser pergunta e virou enum.** `approvals.band` =
     **`AUTO_ARCHIVE`** · **`WEEKLY_BATCH`** · **`JOAO_REQUIRED`** · **`AREA_LEAD_REQUIRED`**. O brief
     para o Hermes (03/08) tratava "o que promove sozinho vs o que exige o João" como causa-raiz do
     gargalo humano; **em 17/08 é campo**. E `ApprovalDecisionAuthorityKind` = `ACCOUNT_ADMIN` |
     `AREA_LEAD` implementa o D92, com o líder de área somado.
160. **⚠ `T2` se divide em `T2_DOCTRINE` e `T2_RECORD`** no `ApprovalTier`. Doutrina (regra) e registro
     (fato) têm banda de aprovação diferente. **Distinção que não existe em nenhum documento nosso** e
     que provavelmente deveria existir: os nossos MDs misturam protocolo (doutrina) e registro de
     cliente (fato) sob o mesmo tier.
161. **⚠ CORREÇÃO: relações são 7 tipos, não 13.** O plano §8.1 lista 13; o
     `ContextRelationType` do código tem **7**: `RELATED_TO`, `SUPPORTS`, `CONTRADICTS`,
     `DERIVED_FROM`, `REFERENCES`, `DEPENDS_ON`, `SUPERSEDES`. Não existem `links_to`, `part_of`,
     `used_by_agent`, `feeds_loop`, `produces`, `belongs_to_area`, `belongs_to_pillar` — pertencimento
     a área resolve por `sourceAreaId`/`targetAreaId`, não por tipo. **A nossa tipagem de relações tem
     de usar os 7 do código.** E há `provenanceKind` = `MANUAL` | `GENERATED` | `IMPORTED`, que é o
     campo que permite migrar os nossos `[[wikilinks]]` como `IMPORTED` deixando rastro.
162. **A auditoria tem dois padrões coexistindo, e isso é ponto a resolver.** `audit_events` é
     **genérico e polimórfico** (`resourceType` + `resourceId`), append-only com **três guardas** de
     schema, e escreve em **`phase: PRE_MUTATION`** — antes da mutação, com ator em três partes
     (`actorSubjectId` + `actorPersonId` + `actorMembershipId`) e `changedFields[]`. Mas `approvals`,
     `agents`, `areas`, `loops`, `conversations`, `context-packs`, `invitations`, `federation-*` e
     `agent-execution` têm **coleções próprias** de audit. **Montar a história completa de um
     endereçamento exige compor as duas famílias.** Proposta: view de leitura que agrega, sem
     centralizar a escrita.
163. **✅ O soft delete já aponta para a própria auditoria.** `contexts` tem `deletedAt`,
     `deletedBySubjectId`, `deletedByPersonId`, `deletedReason` e **`deletedAuditEventId`** — mais o
     simétrico de restauração. É o primitivo de rastreio que eu ia propor, já construído. E o índice
     único de slug é parcial em `deletedAt: null`, então remover libera o identificador.
164. **⚠ Descoberta que muda onde a demanda encaixa: trigger e rotina disparam um LOOP, não uma ação
     arbitrária.** `triggers.loopId` e `routines.loopId` são obrigatórios. Logo **"criar demanda no
     inbox" não é tipo de ação de trigger — é um nó dentro de um Loop.** As quatro coleções novas se
     penduram no resultado da execução do Loop e no `approvals.subjectRef` (polimórfico), não no
     trigger. Isso invalida parte do desenho que eu havia proposto.
165. **✅ Rotina já tem dedupe, teto de custo e ativação segura.** `routines.dedupeKey` (único por
     brain), `maxCostPerRunUsd`, e **trigger e rotina nascem `INACTIVE`** — os três pontos que eu
     havia destacado como "onde automação causa dano" já estão resolvidos no schema. Sobra `PAUSED`
     como estado, e o índice parcial `(status, nextRunAt)` sobre `ACTIVE` é a consulta do agendador.
166. **⚠ As chaves de tenancy em `contexts` são OPCIONAIS, com backfill em curso.** `tenantId`,
     `brainId` e `areaId` são nullable, e existe `areaBackfillRunId` (campo oculto) rastreando a
     migração. **Qualquer consulta multi-tenant hoje tem de tolerar nulo** — e qualquer proposta nossa
     tem de considerar que a base ainda não está completamente escopada.
167. **Convenção de ator: é sempre `trustedSubjectId` (o `sub` do Cognito), não ObjectId.**
     `areas.adminSubjectId` guarda isso, com comentário explícito no código. **Isso corrige a minha
     proposta anterior**, que usava `personId` como chave de endereçamento. Onde há vínculo, registra-se
     também `personId` e `membershipId` — ator em três partes.
168. **Oito convenções do banco que a nossa documentação deve seguir** — extraídas do código e
     registradas em `_dicionario-dados-brainhub.md` §8: slug sempre `lowercase` e único dentro do pai ·
     chave de escopo `immutable` · índice único parcial em `deletedAt: null` · `strict: 'throw'` nas
     coleções novas · ator sempre `trustedSubjectId` · append-only protegido por guarda de schema ·
     tudo que remove registra quem, por quê e o id do evento de auditoria · enum em
     `SCREAMING_SNAKE`. ⚠ O último exige tradução explícita no protocolo, porque o nosso padrão de MD
     usa rótulo em português.

169. **✅ Loops fecham o desenho: um Loop e um GRAFO TIPADO, com validador que recusa aresta
     incompativel.** `loop_versions.graph` tem `nodes[]`, `edges[]`, `contracts` e `policies`, com
     **16 tipos de no** e **11 contratos de dado**. O `LoopGraphValidator` recusa aresta cuja saida
     nao case com a entrada do destino, e a condicao da aresta tem de estar declarada no tipo do no de
     origem. Limites no schema: max 200 nos, `nodeId` unico, grafo max 1 MB, append-only.
170. **⚠ CORRECAO: sao TRES colecoes faltando, nao quatro — e o encaixe da demanda e outro.**
     `notification` **existe como tipo de no** (`LoopNodeType.NOTIFICATION`); o que falta ali e so a
     colecao de registro de entrega (canal, estado, dedupe, erro). E **"criar demanda" nao e campo de
     trigger nem colecao solta: e um no `ACTION` dentro de um Loop**, cujo resultado fica em
     `loop_runs.steps[]`. Aprovar e um no `APPROVAL`, que ja existe. **O vocabulario do fluxo esta
     construido; falta onde a demanda e o enderecamento persistem.** Faltam: `demands`,
     `addressings`, `inbox_items`.
171. **✅ A ancora de rastreio ja existe, e e dupla.** `loop_runs.sourceType` (`MANUAL|ROUTINE|
     TRIGGER`) + `sourceId` responde "por que isso rodou", e `approvals.subjectType`+`subjectRef` e
     **polimorfico de proposito** — e onde o enderecamento se pendura sem exigir campo novo em
     `approvals`. Mais `loop_runs.steps[]` com `nodeId`, `output`, tokens e **custo por passo**.
172. **🔴 `loop_versions.origin` e o elo com o Git que faltava.** Campos `kind`, `templateKey`,
     `templateVersion`, `repo`, `path`, `commitSha` — e **se `kind` e `GIT_TEMPLATE`, os cinco sao
     obrigatorios** por invariante de schema. **Um contexto nosso, versionado no Git, pode se tornar
     definicao executavel com procedencia verificavel por commit.** E o caminho concreto de ligar o
     `brainhub-umode` a plataforma, e nao estava em nenhum documento.
173. **Quatro tipos de no encodam a disciplina de governanca da casa como estrutura de dado:**
     `JURY_CONSENSUS` (quorum, agregacao por dimensao, zero hard-fail), `ITERATIVE_REPAIR` (exige
     **mudanca de hash do artefato** para contar como progresso), `FAILURE_ROUTER` (roteia falha por
     codigo de motivo) e **`READ_BACK_GATE`** (verifica `routes`, `media`, `sitemap`, `robots` com
     status HTTP esperado e timeout). O "exit 0 nao prova trabalho" e o "nada ativo sem read-back"
     deixaram de ser regra escrita e viraram **tipo de no executavel**.
174. **`loops` separa `draftVersionId` de `activeVersionId`** no proprio documento: edita-se o
     rascunho, promove-se a ativo. E `loops`, `triggers` e `routines` **nascem `INACTIVE`**, com
     estado `PAUSED` e `pausedReason`. Padrao a espelhar em qualquer coisa nossa que vire executavel.

175. **🔴 NAO EXISTE regra de quem pode consumir um agente — pergunta do Vinicius em 17 ago 2026,
     respondida com codigo.** O `AccessScopeService` enumera **18 operacoes** (`organizations.*`,
     `categories.*`, `contexts.*`, `ask.answer`) e **nao ha nenhuma `agents.*`**. O schema de `agents`
     nao tem `visibility`, `audience` nem `allowedRoles`. **O eixo nao existe** — nao e que seja
     permissivo. E lacuna de desenho a especificar antes de publicar agente para a operacao.
176. **⚠ A distincao agente estrutural x agente de interacao NAO esta no schema.** `AgentKind` e
     `INTERNAL | USER_DEFINED` — classifica **quem criou**, nao **quem consome** nem **o que faz**.
     O eixo que o Vinicius travou em 17 ago 2026 e outro e precisa ser modelado.
177. **A autorizacao real e por ORGANIZACAO, com excecao individual de no maximo 24h.** Regra base:
     `requestedOrganizationId === executorOrganizationId`. Fora disso, so com
     `TrustedIndividualAccessException` — por pessoa, por operacao, por organizacao, com janela
     `validFrom`/`expiresAt` e duracao maxima de **24 horas**. Tres invariantes que valem copiar:
     **ninguem concede excecao a si mesmo** (`subjectId === grantedBySubjectId` e rejeitado);
     **fail-closed na auditoria** (sem `auditWriter` o acesso e negado); e **8 motivos de negacao
     enumerados e auditados**.
178. **⚠ As duas camadas de permissao nao se falam — CORRIGIDO em 17 ago 2026, algumas horas depois
     de eu escrever isto errado.** O que eu afirmei: "os tiers de `area_memberships` nao sao
     consultados na autorizacao". **Errado.** Sao consultados —
     `categories/services/category-audience-policy.service.ts:58` filtra membership por
     `readableTiers.includes(T2)`, e `authorizeStewardWrite` exige `writableTiers.includes(T2)`
     mais `grants[]` mais `role === ADMIN`. O correto: **nao sao consultados no
     `AccessScopeService`**; sao consultados no caminho de audiencia de categoria. **Eu generalizei
     de um autorizador para o outro sem ler o segundo.** Ha dois autorizadores distintos:
     `AccessScopeService` (grosso, por organizacao, sempre ligado) e `CategoryAudiencePolicyService`
     (fino, por area+tier+share) — e o fino esta **atras de feature flag**
     (`CATEGORY_AUDIENCE_FILTER=on`) **e** de allowlist por `brainId`, e **nao suporta Personal
     Brain**. Existe e esta desligado. Licao: **nao concluir sobre "o sistema nao faz X" tendo lido
     um caminho de codigo so.**
179. **✅ `agent_versions` e onde a instrucao do agente de suporte vai viver, e cabe.**
     `instruction` aceita **100.000 caracteres**; `providerPolicy` tem `allowedProviders[]`,
     **`defaultModel`**, `maxCostPerRunUsd` e `llmConnectionId` — **a escolha de modelo e por versao
     de agente**, nao global; `limits` trava `timeoutSeconds` em 900 e `maxOutputTokens` em 64.000;
     `contextPackRefs[]` referencia Context Pack **por versao**; e `origin: git-template` exige
     `repo`, `path` e `commitSha`. **A instrucao pode vir do nosso repositorio com procedencia por
     commit.**
180. **⚠ LACUNA NOVA que o Vinicius levantou e que eu nao havia considerado: a RESPOSTA a um
     enderecamento.** Meu desenho cobria criar enderecamento, demanda e item de inbox — mas nao
     modelava a pessoa **respondendo**: aceitar, recusar, devolver com pergunta, reatribuir,
     concluir com evidencia. Sem isso o inbox e caixa de saida, nao de trabalho. Precisa de
     colecao ou de maquina de estado propria, com quem respondeu, quando e com que justificativa.
181. **⚠ NAO esta definido como os nossos MDs preenchem o banco.** O mapeamento de
     `institucional.md`, `jornada.md`, `produto.md`, demanda e RFI para `contexts` +
     `contexts.metadata` + `context_relations` **nao existe em nenhum documento**. Depende da decisao
     C2 (front-matter), ainda sem aval. E o `contexts.metadata` e `Object` livre — sem contrato,
     cada importacao inventa o seu.
182. **⚠ Nao esta definido como a operacao interage com o agente.** O Vinicius registrou em 17 ago
     2026 que nem ele especificou isso. Nao ha no banco nem no plano: superficie (chat, formulario,
     comando), onde a conversa e persistida (existe `conversations`, campos nao lidos), e se a
     interacao gera enderecamento. E pre-requisito do agente de suporte ir para a operacao.

183. **✅ O fluxo escrita→disparo→execucao esta FECHADO em codigo lido** — `_fluxo-dados-brainhub.md`
     §1. Transacao com concorrencia otimista por `currentVersionId`, outbox na mesma transacao com
     `_id` deterministico, drenador com lease (5s/30s/lote 25), `RuntimeEventBus`, e
     `loop_runs {brainId,dedupeKey}` **unico** garantindo exactly-once **por indice de banco**.
     Este e o molde de tudo que acrescentarmos.
184. **🔴 CINCO LIMITES DUROS do disparo, que restringem todo desenho novo.** (L1) existe **um**
     eventType, `context.published`. (L2) o payload tem **5 campos** e **nao carrega `metadata`,
     `type` nem `sensitivityTier`** — trigger nao distingue demanda de institucional. (L3) clause
     compara **so string com string**. (L4) **`RuntimeEventBus` nao tem endpoint publico de
     ingestao** — quem quiser disparar precisa do **proprio outbox transacional**; logo
     `addressings` **nao e colecao, e modulo**. (L5) a trigger roda com a autoridade do **dono**
     dela (`ownerPersonId` → `trustedSubjectId`), nao de quem causou o evento — **trigger e objeto
     de governanca**.
185. **⚠ DECISAO TOMADA por mim e registrada: roteamento por Category.** Do L2, os unicos eixos
     visiveis a uma trigger sao `categoryId` e `areaId`. Logo cada tipo de MD nosso vira uma
     `Category` propria (institucional, jornada, pessoas, contexto-area, produto, integracao,
     protocolo, demanda, rfi) e `categoryId` **passa a ser o discriminador de tipo**. Escolhido
     porque **nao depende de alteracao no codigo do Bergson**. Ampliar o payload fica como pedido
     posterior. **Aguarda aval do Vinicius.**
186. **🔴 `approvals` serve para o VEREDITO e NAO serve para a conversa de trabalho — e o motivo e
     um indice.** `subjectType` e `String` livre, entao `subjectType: 'ADDRESSING'` cabe **sem
     alterar schema**. Mas o indice **unico** `{brainId, subjectType, subjectRef}` permite **uma
     aprovacao por assunto, uma so vez**, e `ApprovalStatus` e `PENDING|APPROVED|REJECTED|ARCHIVED`
     — **sem "devolvido com pergunta" e sem "reatribuido"**. Por isso a resposta a enderecamento
     exige colecao **append-only** propria (`addressing_responses`), nao um campo em `approvals`.
187. **🔴 Nenhuma superficie de conversa com agente existe.** `conversations`/`conversation_turns`
     e RAG sobre o acervo (`question`/`answer`/`sources[].contextId`/`score`) e **nao tem
     `agentId`**; `agent_runs` tem `agentId` mas e **single-shot, sem `conversationId` nem
     `sequence`** — sem memoria de conversa. Peca que falta e pequena: `conversations.agentId`
     (nullable) + `conversation_turns.agentRunId`. **Pre-requisito do agente de suporte chegar a
     operacao.**
188. **✅ O padrao para "quem consome agente" nao precisa ser inventado — copia-se o de categoria.**
     `agents.audienceMode` + `agents.stewardAreaId` + `agent_shares` (espelhando `category_shares`
     com ALLOW/DENY, `approvalId`, `revokedAt`) + grant `agents.consume` em `membership.grants[]` +
     operacao `agents.run` no `AccessScopeService`. Para o agente de suporte do uFlow:
     `TENANT_WIDE`, e a excecao passa a ser explicita e auditavel.
189. **⚠ Contrato de `metadata` e chave de idempotencia da importacao de MD.** `contexts.metadata`
     e `Object` **livre** — sem contrato nosso cada importacao inventa o seu. Proposto:
     `{repoPath, commitSha, mdType, clientKey, generatedBy, importRunId}`. Chave de idempotencia:
     `(tenantId, categoryId, repoPath)`. E como o publish exige `currentVersionId` no filtro, o
     importador tem de **ler a cabeca antes de publicar** e tratar `null` como "mudou no meio,
     recarrega", **nao como erro**. ⚠ `triggers`, `routines`, `conversations`, `conversation_turns`
     e `category_shares` usam `strict: 'throw'` — campo desconhecido e **rejeitado**. Em
     `contexts` o modo strict **nao foi confirmado**; verificar antes de assumir.
190. **🟠 METODO — cobranca do Vinicius em 17 ago 2026: "para de afirmar que superamos algum ponto
     e quando aperto com perguntas voce me vem como lacunas serias. Voce tem que ser tao rigido na
     conclusao das respostas quanto eu."** Procede. O padrao errado era: relatar o feito e deixar a
     lacuna para quando fosse perguntada. **Regra adotada: a lacuna vem antes da conquista, e todo
     documento de estado abre com declaracao de completude.** Aplicado no
     `_fluxo-dados-brainhub.md` (§0-bis) e na graduacao de evidencia [C]/[F]/[P]/[D] por afirmacao.

191. **✅ DECISAO 1 TOMADA — front-matter nos MDs: NAO.** Vinicius perguntou em 17 ago 2026 se eu ja
     nao tinha resposta para adotar e seguir. Tinha, mas so soube depois de **verificar em vez de
     supor**: a chave estavel do cliente **ja existe dentro do MD** (`### ID do cliente`, definida no
     `protocolo-criacao-cliente.md` em 03 ago, exatamente para o nome da pasta ser so apresentacao),
     e o `_indice/clientes.csv` **ja a extrai** junto com o caminho do arquivo. Medido: **1.316 MDs,
     zero com front-matter**. Tudo que a importacao precisa e derivavel — tipo pelo nome do arquivo,
     area pela pasta, cliente pela chave no corpo, caminho pelo caminho, commit pelo Git.
     **Front-matter seria segunda copia de dado que ja tem dono**, e duas fontes para o mesmo fato
     divergem. **Decidido: o `_indice/` e o contrato de importacao e `gen-indice.ps1` e a primeira
     metade do importador.** Campo genuinamente nao-derivavel ganha front-matter no dia em que
     aparecer, nao antes. Isto **destrava a pendencia 189** e o item 1 da tabela de decisoes.
192. **✅ DECISAO 2 TOMADA — as 9 categorias adotadas como discriminador de tipo:** `institucional`,
     `jornada`, `pessoas`, `contexto-area`, `produto`, `integracao`, `protocolo`, `demanda`, `rfi`.
     Minusculo e sem acento (o schema exige slug minusculo). Forcada pelo L2: categoria e o unico
     eixo pelo qual o barramento distingue tipos.
     ⚠ **O que eu NAO sei e declaro:** `categories.slug` e **unico por organizacao** e a categoria
     governada exige `tenantId` + `areaId`. Logo pode ser **9 no total** ou **9 por cliente**,
     conforme o mapeamento organizacao↔cliente — que esta em `organizations.schema.ts`, **que eu nao
     li**. Taxonomia decidida; multiplicidade e pergunta para o Bergson.
193. **📘 Documento didatico criado: `_como-o-brainhub-funciona.md`.** Aula do zero a pedido do
     Vinicius, que disse nao ter ideia de como interpretar a arquitetura. Traduz o fluxo sem
     acrescentar desenho. Regra de governanca embutida: **a explicacao nunca lidera o fato** —
     alterar o didatico exige que o `_fluxo-dados-brainhub.md` tenha mudado primeiro.
     Os tres nucleos da aula: (1) nada acontece por ordem, acontece por **fato registrado** — mural
     com assinaturas, nao telefone; (2) **a identidade do documento E a regra** — por isso
     "todo MD do mesmo tipo tem os mesmos titulos" deixa de ser preciosismo e passa a ser
     **pre-condicao de automacao**; (3) o laco que fecha: **concluir exige evidencia, evidencia e
     ponteiro para documento do acervo**, logo concluir trabalho enriquece o acervo, que publica, que
     aciona o trabalho seguinte. E isso que significa "tomar vida".

194. **✅ MULTIPLICIDADE DE CATEGORIA FECHADA: 9 por casa — e eu podia ter decidido sozinho desde o
     inicio.** Na 192 eu escrevi "nao sei se e 9 no total ou 9 por cliente, depende de
     `organizations.schema.ts`, que eu nao li". Vinicius perguntou, em 17 ago 2026, qual era a duvida
     e se eu nao era capaz de decidir. **Era. Bastava ler o arquivo que eu mesmo apontei.** A resposta
     estava num comentario do schema: *"Mapping de compatibilidade: Organization legado → Tenant + um
     Second Brain."* Cadeia: **tenant → exatamente um Second Brain (indice unico parcial) →
     organizations com slug unico POR BRAIN → categories com slug unico por organizationId**.
     Logo o namespace de categoria e **por cliente**: **9 em cada cliente + 9 na Casa = 47 × 9 = 423**.
     Nao e redundancia — e a **regra de isolamento de cliente expressa no modelo de dados**.
     Confirmacao independente no mesmo arquivo: o `pre(findOneAndDelete)` de Organization apaga
     `categories`, `contexts` e `context_chunks` por `organizationId` — **organizacao e a fronteira de
     contencao do conteudo**.
     ⚠ **CONSEQUENCIA OPERACIONAL, que e o achado de verdade:** `triggers` tambem sao escopados por
     `brainId` + `tenantId`, logo **a automacao nao e global — e por cliente, replicada**, como as 14
     areas. **Criar um cliente passa a significar 14 areas + 9 categorias + as inscricoes, e isso tem
     de entrar no `protocolo-criacao-cliente.md`.**
     🔴 **LICAO DE METODO, terceira variacao do mesmo erro:** eu nao declarei fonte indisponivel nem
     concluí sobre um caminho so — eu **transformei em pendencia de terceiro algo que estava a uma
     leitura de distancia, e o arquivo eu ja tinha nomeado**. Nao basta nomear o que falta ler:
     **se eu sei qual arquivo responde e tenho acesso a ele, ler e obrigacao antes de declarar duvida.**
     Regra levada para o `CLAUDE.md`.
195. **🟠 FIO SOLTO NOMEADO, nao resolvido: a membrana Casa↔cliente atravessa brains.** Se cada cliente
     e um brain isolado, o `conecta_area_cliente` de cada Produto cruza fronteira de brain. Existem os
     modulos `federation-connections` e `federation-discovery` (+ auditorias e `federation-discovery.
     node`/`.profile`), **nao lidos** — provavel que sejam esse mecanismo. **Proxima leitura**, nao
     palpite.

196. **✅ PROCEDENCIA DE "CATEGORIA" APURADA nas quatro faixas — Vinicius perguntou em 17 ago 2026 se
     surgiu do banco, do Joao ou do nosso conteudo.** Resposta verificada, nao de memoria:
     **A · banco** — `categories.schema.ts` nasceu no **commit fundacional do repositorio**,
     `a470f8d`, 14 jul 2026, o primeiro commit que existe. E o `ask` usa categoria como **filtro de
     busca** (`ask.dto.ts: category?: string`; resposta cita `organizationSlug/categorySlug`).
     **B · vault do Joao** — 282 arquivos com "categor", **todos de dominio** (categoria de produto
     de moda `Temporada→Marca→Colecao→Categoria→Produto`, categoria de conteudo, PRDs).
     **Nao esta no glossario dele nem na hierarquia do BrainHub.** Nao vem do Joao.
     **C · Lovable** — **uma** ocorrencia: `"label": "categoria"`, rotulo de campo na tela de
     importar. Nao e conceito do Lovable.
     **D · nosso conteudo** — a palavra **nao existe na nossa hierarquia** (Instituicao →
     Institucional → Areas → Subareas → Pessoas).
     > **Veredito: a COLECAO e do banco (faixa A, fundacional). O USO como discriminador de tipo de MD
     > e 100% proposta minha (faixa D), de 17 ago 2026, forcada pelo L2.** Ninguem jamais tratou
     > Categoria como tipo de documento.
197. **🔴 CUSTO DO MEU PROPRIO DESENHO, exposto pela verificacao da 196 e que eu NAO havia declarado:
     Categoria pode ser o eixo de TIPO ou o eixo de AUDIENCIA — nao os dois.** No codigo ela e
     **unidade de agrupamento com politica de audiencia**, usada para filtrar busca; eu estou
     sobrepondo o papel de **rotulo de tipo**. O invariante nao deixa os dois conviverem:
     categoria **governada** exige `brainId` + `tenantId` + **`areaId`** + `stewardAreaId` +
     `audienceMode` e tier T2 — **amarrada a UMA area**. Categoria **nao-governada** e legal (o
     `pre(validate)` so dispara se algum campo governado estiver preenchido) e a autorizacao recai no
     nivel de organizacao.
     - **Se Categoria = tipo** (9 por casa, nao-governadas): roteamento funciona, autorizacao fica por
       organizacao — que e o que esta ligado hoje, ja que a audiencia fina esta atras de feature flag.
     - **Se Categoria = audiencia por area**: passa a ser por (tipo × area) = **9 × 14 × 47**, e pelo
       L2 a trigger fica **sem nenhum eixo de tipo**, porque nao ha outro campo no payload.
     **Recomendacao mantida: tipo.** Razoes: e o que faz o roteamento existir; a audiencia fina esta
     desligada; e o isolamento por cliente ja vem do brain, nao da categoria. **Mas e escolha com
     custo declarado, nao caminho obvio — quem for ligar a audiencia fina precisa saber que esse eixo
     foi gasto.** Vai na pauta do Bergson.

198. **🔴 CORRECAO DE ENQUADRAMENTO DE AUTORIDADE — travada pelo Vinicius em 17 ago 2026, e com
     consequencia de desenho.** Ele registrou: *"o Bergson que criou as collections do banco e a
     estrutura foi para traduzir o entendimento que ele teve de acordo com o que o Joao e eu
     explicamos sobre o que seria o BrainHub. Portanto, em termos de entendimento ele nao sera a
     referencia. Nosso papel sera justamente definir todas as collections, campos e forma de
     relacionamentos."*
     - **O codigo e autoridade sobre o ESTADO** (o que existe, com campo, indice e invariante).
       Continua soberano para "o que esta construido".
     - **O codigo NAO e autoridade sobre a INTENCAO.** E leitura de uma explicacao, feita por quem
       nao vive o negocio. Divergencia entre schema e necessidade **nao e erro de entendimento
       nosso — e traducao a corrigir**.
     - **Definir collections, campos e relacoes e NOSSO papel. O Bergson implementa.**
     Eu vinha escrevendo "decisao do Bergson", "pauta do Bergson", "negociar com o Bergson" — todos
     corrigidos em `_fluxo-dados-brainhub.md` para **"nos especificamos, Bergson implementa"**. O grau
     `[D]` passou a dizer explicitamente: **nunca do Bergson**.
199. **🔺 RECOMENDACAO REVISTA no mesmo dia, por causa da 198: o Caminho A caiu, vale o Caminho B.**
     Eu havia escolhido sobrecarregar `categories` como rotulo de tipo, e a **unica vantagem que
     declarei era "nao depende de alteracao no codigo do Bergson"**. Essa justificativa **nunca foi
     valida**. Nova especificacao (`_fluxo-dados-brainhub.md` §3-bis):
     - **`contexts.type`** — enum com os 9 tipos, campo de primeira classe. O tipo **e** atributo do
       documento, nao agrupamento nem audiencia.
     - **`type` e `sensitivityTier` no payload de `context.published`** — resolve o **L2 na origem**
       em vez de contorna-lo.
     - **`Category` volta a ser so audiencia**, como o schema a desenhou (governada, por area, com
       `stewardAreaId` e `category_shares`).
     Ganhos: trigger casa `EQUALS` em `type` dentro do L3; **tipo e audiencia deixam de competir**
     (um `jornada` pode ter audiencias diferentes por area, e uma area varios tipos — impossivel com
     A); a contagem de categorias deixa de ser **423 buckets de tipo** e passa a ser o que o desenho
     de audiencia pedir; e o `ask` ganha filtro por tipo de graca. Custo honesto: altera `contexts`, o
     payload e o publisher — **trabalho de implementacao, nao obstaculo de projeto**.
     🔴 **LICAO DE METODO, quarta variacao:** as tres anteriores eram sobre **nao concluir sem ler**.
     Esta e outra: **nunca escolher caminho tecnico porque ele evita mexer no codigo de outro.**
     Isso nao e prudencia — e desenhar para a conveniencia errada. Regra no `CLAUDE.md`.
200. **📘 A aula virou arquivo para ler e reler**, a pedido do Vinicius. HTML autocontido,
     tipografia serifada para leitura longa, as sete etapas com o problema que cada uma resolve, o
     diagrama do laco que fecha, e marcador **NAO EXISTE** em tudo que e desenho e nao realidade.
     Fecha com a correcao de autoridade da 198 — porque quem le a aula precisa saber que o schema nao
     e a intencao.

201. **🔴 CORRECAO — o eixo de "quem pode consumir agente" EXISTE no desenho do Joao desde 09 jul
     2026. Eu havia dito ao Vinicius que "o eixo nao existe".** Incompleto: nao existe **no banco**.
     O `_sistema/brainhub/governance/template-ficha-agente.md` (promovido a canonico por **D32,
     aprovado pelo Joao**) define `context_policy` com 4 flags (`per_user_context`,
     `admin_can_view_all_contexts`, `shared_context_after_approval`,
     `raw_user_context_leaks_to_other_users: false`), mais `visibility`, mais `permissions`.
     **Eu verifiquei o codigo e nao o desenho — quarta vez que concluo sobre o sistema olhando uma
     fonte so.** O eixo nao precisa ser inventado: **precisa ser implementado.**
202. **🔴 DIVERGENCIA GRAVE de conformidade em AGENTES, apurada campo a campo.** O `kind` do Joao tem
     **5 valores semanticos** (`agent`, `worker`, `poller`, `sentinel`, `reconciler`) — diz **o que o
     agente faz**. O `AgentKind` do banco tem 2 (`INTERNAL`, `USER_DEFINED`) — diz **quem o criou**.
     **Sao eixos diferentes com o mesmo nome.** E o `status` do Joao tem **6 estados** (`draft`,
     `aprovado`, `ativo_local`, `ativo_time`, `bloqueado`, `aposentado`) — o banco perde a fronteira
     `ativo_local` × `ativo_time`, que e exatamente a linha de exposicao ao time. Ausentes no banco:
     `visibility`, `context_policy`, `canonical_write`, `external_send`, `requires_guard`,
     `reads[]`/`writes[]`. **Espec de correcao na §2.3 do `_espec-banco-brainhub.md`**, incluindo
     renomear o `kind` atual para `authorship` — dois campos `kind` com semanticas distintas e como
     se perde um modelo.
203. **🔴 ACHADO DO JOAO, provado em producao: EXECUCAO ≠ ENTREGA.** No registry dele o agente
     `pendencias-joao-lembrete` esta com `last_status: "ok"` **e**
     `last_delivery_error: "platform 'discord' not configured/enabled"`. **Rodou certo e nao chegou
     a ninguem.** O banco tem **um** status; precisa de dois. `loop_runs`/`agent_runs` ganham
     `deliveryStatus`, `deliveryError`, `deliveryAt`, e a invariante: **`succeeded` com entrega
     `FAILED` nao conta como sucesso em painel nem em metrica.** E o pior tipo de erro num sistema de
     enderecamento, porque **parece** que funcionou.
204. **📋 INVENTARIO DE AGENTES fechado — 17 automacoes do Joao, 1 nossa.** Registry Hermes (16 jul
     2026): **10 agentes** em 4 workflows (`calls-pipeline`, `governance-pipeline`,
     `queue-executor-pipeline`, `codex-reconciliation-pipeline`). Frota launchd (`frota.json`,
     10 jun): **3** (`driftsweep`, `gitpullall`, `brainhub-mine` — este usa IA, roda a cada 30 min e
     destila transcricoes **como propostas para aprovacao**). Treinos: **4**
     (`classificador-cunho`, `filtro-sinal`, `juiz-contradicao`, `roteador-tier`).
     ✅ **Os 4 treinos correspondem a tipos de no que o banco JA tem** — `juiz-contradicao` ↔
     `JURY_CONSENSUS`, `filtro-sinal` ↔ `GATE`, `roteador-tier` ↔ classificacao de tier.
     **Migrar como `agent_versions`, nao reinventar.**
     🔴 **O achado estrutural: todos os 10 sao `deliver: "local"`, com script em `~/.hermes/` e
     agenda em launchd na maquina do Joao. 17 automacoes que nao sobrevivem ao notebook dele
     desligar.** Isso, e nao falta de ideia, e o argumento central da espec: o desenho existe, esta
     provado, roda ha meses — falta **deixar de ser pessoal e virar plataforma**.
205. **🟡 SOBRESSALENTE identificado.** `downloads-sentinel` (quebrado **e** faxina de maquina local,
     nao dominio do BrainHub) · `gitpullall` (ops puro, sem IA) · `pendencias-joao-lembrete` (o caso
     de uso vira `inbox_items` + faixa de aprovacao, **nao vira agente**) · `codex-inbox reconciler`
     (**nunca rodou** desde 16/07 — nao migrar sem provar) · `registry.v0.1.superado.json`.
     ⚠ **E o sobressalente mais importante: existem TRES fontes de agente** — `frota.json` (launchd),
     `~/.hermes/cron/jobs.json` (Hermes) e as fichas em `inbox/hermes/brainhub/agents/`.
     **Uma fonte, nao tres — e isso e exatamente o que a colecao `agents` resolve.**
206. **⚠ DISAMBIGUACAO: `TAXONOMIA_UMODE.md` do vault NAO e a taxonomia estrutural do BrainHub.** E
     "Taxonomia uMode — **Catalog AI**": hierarquia e grupos de atributos de **produto de moda**
     (85 KB). Conformidade estrutural se mede contra a hierarquia (Instituicao → Institucional →
     Areas → Subareas → Pessoas), os tiers e as faixas de aprovacao — **e nessas tres o banco esta
     conforme**. Registrado para ninguem procurar conformidade no documento errado.
207. **📘 `_espec-banco-brainhub.md` (ESPEC-BANCO-001) escrita para implementacao pelo Bergson.**
     5 colecoes novas (`addressings` + outbox proprio, `addressing_responses` append-only, `demands`
     com `externalRefs`, `inbox_items`, `agent_shares`), 5 alteracoes em colecoes existentes, a
     matriz de rastreio com **16 perguntas e o campo exato que responde cada uma**, 8 invariantes
     nao-negociaveis, o inventario de agentes, e ordem de implementacao em 7 ondas.
     **Gargalo declarado: a onda 1** (`contexts.type` + os 2 campos no payload) — sem ela nenhuma
     automacao distingue tipo de documento e todo o resto vira contorno.

208. **✅ TAXONOMIA CORRIGIDA — "coleção" → `collection`, travado pelo Vinicius em 17 ago 2026:**
     *"Taxonomia é mais do que importante — é essencial para termos mesmos entendimentos."*
     **59 ocorrências convertidas** em 4 HTMLs e 5 MDs de contexto. Regra no `CLAUDE.md`: **usar o
     termo que o desenvolvedor usa de fato, não a tradução** — `collection` e não coleção, `trigger`
     e não inscrição, `outbox` e não bilhete, `lease` e não carimbo, `drainer` e não carteiro,
     `head`/`currentVersionId` e não "a cabeça", `ApprovalBand` e não "faixa de vazão".
     🔴 **A ARMADILHA ERA REAL e quase corrompi um dado:** "coleção" neste negócio tem **dois
     sentidos** — a `collection` do Mongo **e a coleção de moda** ("Gestão de Coleção" no uFlow, a
     área `03_Desenvolvimento-de-Colecao`, `Temporada → Marca → Coleção → Produto`). Auditei antes de
     substituir e achei **1 ocorrência de sentido-moda** na tabela de procedência do
     `_como-o-brainhub-funciona.md`, que foi **protegida por sentinela** durante a substituição.
     **Regra travada: termo do banco em inglês, termo de moda em português.** Substituição em massa de
     termo com dois sentidos exige auditoria dos sentidos ANTES.
209. **✅ PONTE DE VOCABULÁRIO criada na aula (`_como-o-brainhub-funciona.md` §8).** Metáfora continua
     permitida **só em documento didático**, e ali é **obrigatório** mapear cada uma ao termo real.
     Espec, dicionário de dados e documento de fluxo: **nunca metáfora**. As duas divergências que a
     auditoria achou na espec (`inscrição`, `faixa de aprovação`) foram corrigidas para `trigger` e
     `ApprovalBand`. Residual de metáfora na espec: **zero**, verificado.
210. **🔴 O QUE FALTA PARA INSERIR O AGENTE DE SUPORTE uFLOW NA COLLECTION `agents` — pedido em 17 ago
     2026.** Verifiquei o que já tenho antes de pedir. **Já tenho:** o repositório do PLM
     (`C:\Ambientes Virtuais\uFlow\umode-flow`, 211 tabelas mapeadas), o papel, o formato de resposta
     de 7 seções, as 4 armadilhas de arquitetura, o playbook de SQL e os Anexos A, B e C parcial.
     **Confirmado que NÃO chegou nada novo:** `Downloads` não tem o treinamento; o
     `instrucoes-projeto-trilha-hic.md` que está lá é de **outro projeto** (Trilha HIC), não é a
     instrução do agente.
     **FALTA, e é o que trava:**
     1. **`TREINAMENTO-AGENTE-SUPORTE-UFLOW.md` completo** — tenho 818 de 1.084 linhas. Faltam o fim
        do Anexo C, o **Anexo D** (`PROPOSTA-acesso-fornecedor-multiplos-status.md`) e o **Anexo E**
        (`prompt-detalhes-tarefa.md`). → vira `agent_versions.instruction` (cabe: limite 100.000 chars).
     2. **A instrução vigente em produção**, a que já passou por aprendizagem. → é ela que vira a
        `ACTIVE`; o treinamento é lastro.
     3. **Onde o agente atende hoje** (canal e superfície). → decide se é `conversations` (multi-turno)
        ou `agent_runs` (single-shot), e o `channel` do `inbox_items`.
     4. **Qual modelo está em uso.** → `providerPolicy.defaultModel` + `allowedProviders[]`.
     5. **Quem pode consumir** — se é todo mundo, é `audienceMode: TENANT_WIDE`. → e **qual área é
        `stewardAreaId`** (responde pelo agente). Provável `06_Tecnologia` ou `02_Atendimento`,
        **mas isso é decisão do Vinicius, não palpite meu.**

211. **✅ DECISAO TOMADA em 17 ago 2026: NAO enviar a ESPEC-BANCO-001 com 42% de cobertura de
     leitura.** Vinicius delegou a decisao de sequenciamento com a condicao de entrega segura e com
     qualidade. Escolhi **fechar a leitura dos 29 schemas antes de entregar**, priorizando risco de
     colisao. Razao: **quatro vezes nesta jornada eu errei concluindo de leitura parcial, e nas quatro
     o custo foi meu.** Enviar a espec assim transfere o custo para o trabalho de outra pessoa, e
     **espec que contradiz codigo existente e pior que espec nenhuma** — queima a confianca e o tempo
     do implementador. A leitura pagou na primeira hora: quatro correcoes abaixo.
212. **🔴 COLISAO REAL: `seeds` + `seed_batches` ja sao o pipeline material-bruto → aprovacao →
     contexto.** E exatamente a esteira que o `brainhub-mine` e o `calls-pipeline` do Joao alimentam.
     Campos: `sourceType`/`sourceRef`, `contentClassification`, `sensitivity` (ApprovalTier, default
     `T2_RECORD`), **`integrityHash` sha256 com indice UNICO por brain**, `processingStatus`,
     **`currentOwner`**, **`nextAction`**, **`stateTrail[{status,at,reason}]`**, `consentRef`,
     `retentionPolicy`, `contextId`, `approvalId`, `quarantineReason`, `batchId`.
     **Quatro correcoes na minha proposta:** (1) `addressings` estava sem `currentOwner`/`nextAction`,
     que e **o idioma que a casa ja usa** para "quem detem e o que falta"; (2) faltava
     `integrityHash` para dedupe por conteudo; (3) **faltavam `consentRef` e `retentionPolicy` —
     LGPD, que eu NAO havia considerado** e vale para toda collection com dado de cliente;
     (4) ✅ `seeds` **nao** substitui `inbox_items` — nao tem campo de entrega nenhum. Sao camadas
     complementares: `seeds` e o que aguarda decisao, `inbox_items` e o aviso de que aguarda voce.
213. **🔴 O padrao de auditoria e POR MODULO e minha espec estava fora dele.** Existem
     `approval_audit_events`, `category_policy_audit_events`, `federation_connection_audit_events`,
     `invitation_audit_events` — **alem** do `audit_events` geral. Logo **`addressings` exige
     `addressing_audit_events` proprio**. Minha espec dizia so "`auditEventId` amarra na trilha":
     subespecificado e nao conforme.
214. **⚠ A casa tem DOIS padroes de historico e eu ignorei um.** Collection separada append-only
     (`context_versions`, `audit_events`, `context_pack_versions`) **e** trilha inline no documento
     (`seeds.stateTrail[]`). Mantenho `addressing_responses` como collection separada — carrega
     justificativa, `evidenceContextIds[]` e `generatedDemandIds[]`, muito mais que trilha de status
     — **mas agora a escolha esta justificada contra o idioma existente, nao por omissao.**
215. **✅ ACHADO QUE RESOLVE A ORDEM DE IMPLEMENTACAO COM EVIDENCIA: `context_packs`.**
     `context_packs` + `context_pack_versions` sao o que `agent_versions.contextPackRefs[]`
     referencia, e a versao do pack e **imutavel e endereçada por conteudo**: `contextIds[]`
     explicito, `limit` (1–50), **`minScore`** (0–1), **`sourcesHash` `sha256:`**, append-only
     imposto em **6 verbos de mutacao + `bulkWrite`**.
     **Instrucao e acervo sao versionados juntos, com hash nos dois lados** — e uma versao de agente
     aponta uma versao de pack, que fixa a lista de contextos e os parametros de recuperacao.
     🔴 **Consequencia que muda o plano:** sem `context_pack`, o agente de suporte responde **so pela
     instrucao** — sem `sources[]`, sem citacao, sem rastreio de qual MD sustentou a resposta.
     **Perde-se a garantia de zero alucinacao.** E o pack precisa de `contexts` populado, que precisa
     do importador, que precisa de `contexts.type`. **Portanto a onda 1 nao e alternativa a entrega do
     agente — e pre-requisito da QUALIDADE dele. NAO invertemos as ondas.** Eu havia sugerido inverter
     na mensagem anterior; a leitura desfez a sugestao.

216. **✅ AUTORIDADE SOBRE AGENTE — decidida pelo Vinicius em 17 ago 2026, e sao TRES papeis, nao um.**
     *"Quem tem o poder de treinar, retreinar, aposentar, desativar — quem define como o agente vai
     trabalhar — e a area responsavel (tecnologia no caso). A area de atendimento vai mexer direto...
     poderemos barrar que o comercial consuma esse agente."*
     - **Steward (define): `06_Tecnologia`** → `agents.stewardAreaId` + grant `agents.steward` +
       `decisionTiers`.
     - **Operador (usa direto): `02_Atendimento`** → grant `agents.operate`, **sem** alterar instrucao.
     - **Consumidor barravel: ex. `01_Comercial`** → `agent_shares` com `effect: DENY`.
     🔴 **A decisao trava a SEMANTICA da permissao:** e **permitir-por-padrao-com-negativa-explicita**,
     nao o inverso — "poderemos barrar" so faz sentido assim. Logo `audienceMode: TENANT_WIDE` +
     negativa por area. ✅ **E a precedencia ja esta decidida em codigo:** o filtro de audiencia aplica
     `$nin` dos negados **depois** do `$or` de permissoes → **DENY vence ALLOW**. `agent_shares` herda.
     ⚠ **Definir ≠ operar, e hoje o banco funde:** `agents` tem um so `ownerPersonId`. Sem
     `stewardAreaId` + os dois grants, quem opera pode republicar instrucao.
     ⚠ **Ambiguidade declarada, nao resolvida por mim:** "mexer direto" admite *operar* ou *ajustar*.
     Especifiquei a leitura conservadora. Se Atendimento puder ajustar modelo ou teto de custo sem
     tocar na instrucao, e um terceiro grant (`agents.tune`) e **precisa ser dito**.
217. **✅ FORENSE DOS ARQUIVOS DO AGENTE — feita com comandos antes de repetir que falta.** Vinicius
     cobrou: *"voce mesmo me afirmou que tinha e agora esta me dizendo que faltam"*. Justo. O que
     verifiquei: `git log --all --diff-filter=A` no nosso repo por `TREINAMENTO|Papel de Suporte`;
     `git log --all -S` por `PROPOSTA-acesso-fornecedor`, `prompt-detalhes-tarefa`, `Anexo D`, `Anexo E`;
     e varredura de disco por `multiplos-status`.
     **Resultado: os matches sao TODOS a minha propria nota sobre a ausencia, nao o conteudo.** O
     `agente-suporte-uflow.md` tem os headings de Anexo A, B e C **com conteudo**; D e E aparecem so
     como nome na declaracao de lacuna. **Nunca estiveram neste repo e nao estao no disco.**
     **A distincao que eu deveria ter feito antes e que explica a cobranca: eu tenho o CONHECIMENTO
     DERIVADO (251 linhas que eu estruturei), nao o ARQUIVO-FONTE (1.084 linhas).** E a diferenca e
     tecnica, nao semantica: `agent_versions.instruction` + `contentHash` + `origin.commitSha` exigem
     **o artefato verbatim**. Meu resumo nao serve como instrucao — serve como contexto.
218. **📘 ESPEC-BANCO-001 v2 publicada.** Cobertura de leitura **21 → 29 de 50**. Novidades: §1.2-bis
     (o modelo de tres papeis), §6-bis.5 (`folders`/`files` e a decisao de que **os MDs vao para
     `contexts`, nao para `files`** — mais `attachmentFileIds[]` em `addressings` e o padrao completo de
     soft-delete com ponteiro de auditoria), §6-bis.6 (**fio solto FECHADO**: `federation_connections`
     e a membrana Casa↔cliente, com 4 niveis `discover`/`read`/`query`/`contribute`, ciclo de decisao e
     indice unico por par de brain — e a consequencia volumetrica de 16 produtos × N clientes entra no
     `protocolo-criacao-cliente.md`), §6-bis.7 (`invitations` **nao colide**).
     ⚠ **Dois erros que eu introduzi na substituicao em massa e corrigi na verificacao:** a nota de
     completude passou a dizer "29 dos 50 nao lidos" (o inverso do fato — sao 29 **lidos**, 21 nao), e
     a membrana continuava listada como pendencia depois de resolvida. **Licao: substituicao em massa
     de numero exige reler a frase, porque o numero muda de papel dentro dela.**

219. **🟢 LACUNA DE INSUMO DO AGENTE FECHADA — 17 ago 2026.** Vinicius reenviou as duas fontes em
     `C:\Ambientes Virtuais\BrainHub\_insumos` (fora de `Downloads`, de proposito, porque foi de la que
     o arquivo desapareceu em 04 ago). **Treinamento lido por INTEIRO: 1.084 de 1.084 linhas**,
     incluindo os Anexos D e E que faltavam. `Papel de Suporte.txt` (122 linhas) tambem em maos.
     ⚠ **Nota tecnica que custou confusao:** `Measure-Object -Line` reportou **795 linhas** para um
     arquivo de 1.084 — porque **nao conta linhas vazias**. Usar `Select-String` com numero de linha ou
     `[System.IO.File]::ReadAllLines().Count` quando a contagem importar.
220. **🔴 ACHADO: existem DUAS instrucoes do agente, nao uma — e formam linhagem de versao real.** Eu
     pedi "a instrucao vigente" supondo arquivo unico. Errado:
     - **v1 = `Papel de Suporte.txt`** — 6 secoes de resposta.
     - **v2 = §14 do treinamento** ("Instrucoes do Projeto (colar na configuracao do assistente)") —
       **7 secoes** (soma `Validar & Aprender`), mais a **pedagogia HIC** ("um comando correto entregue
       sem ensinar o raciocinio e uma FALHA"), o **rito de SQL** (homologacao, backup, transacao,
       pre-check, COMMIT) e as **4 armadilhas** nomeadas.
     > **O agente nao nasce com snapshot: nasce com historico.** v1 entra como `version: 1` superseded,
     > v2 como `version: 2` `ACTIVE` com `supersedesVersionId`. **E a primeira prova real do
     > versionamento de instrucao no BrainHub.**
     ⚠ **E a instrucao vigente NAO era um arquivo separado — estava dentro do treinamento.** Eu pedi um
     arquivo que nao existia como arquivo. Licao: antes de pedir insumo, **procurar dentro do que ja
     tenho** — a §14 estava listada no proprio indice do documento que eu declarei ter lido ate a 818.
221. **✅ INSTRUCOES VERSIONADAS COMO ARTEFATO NO REPO, extraidas POR SCRIPT e nao transcritas.**
     `agente-suporte-uflow-instrucao-v1.txt` (4.345 chars, sha256 `0342b490...`) e
     `agente-suporte-uflow-instrucao-v2.txt` (4.143 chars, sha256 `d0c4a21d...`).
     **Motivo de extrair por script:** `contentHash` e `origin.commitSha` so valem se o artefato for
     **byte a byte** o mesmo — transcricao manual invalida a procedencia. Ambas usam **4,1% do limite**
     de 100.000 chars de `agent_versions.instruction`.
     🔒 **Governanca travada: os `.txt` sao IMUTAVEIS.** Instrucao nova = arquivo novo com versao nova,
     nunca edicao do existente.
222. **📋 FICHA DE INSERCAO NO BANCO pronta: `agente-suporte-uflow-ficha-banco.md`.** Payload completo
     para `agents` + `agent_versions`, com a decisao de autoridade aplicada: `stewardAreaId:
     06_Tecnologia`, grant `agents.steward` para Tecnologia, `agents.operate` para Atendimento,
     `audienceMode: TENANT_WIDE`, `kind: AGENT`, `visibility: OPERATOR`, `lifecycle: DRAFT`,
     `canonicalWrite: false`, `externalSend: false`, `activationApprovalBand: JOAO_REQUIRED`.
     **Restam TRES campos em aberto**, e so um depende do Vinicius:
     1. `ownerPersonId` — id do banco, resolve na insercao.
     2. **`providerPolicy` (`defaultModel`, `allowedProviders[]`, `llmConnectionId`) — QUAL MODELO o
        agente usa hoje. Nao esta em NENHUMA das duas fontes**: o treinamento descreve comportamento e
        nunca menciona provedor. **Uma frase do Vinicius resolve.**
     3. `contextPackRefs[]` — depende da onda 1 (`contexts.type` → importador → pack).
     ⚠ **Sobre o item 3, e importa para qualidade:** sem `contextPackRefs` o agente responde **so pela
     instrucao** — sem `sources[]`, sem citar contexto, sem rastreio de qual MD sustentou a resposta.
     Funciona, mas **perde a garantia de zero alucinacao**. Pack natural: `uflow-modelo-de-dados.md`,
     `agente-suporte-uflow.md` e os protocolos de suporte.
223. **📘 Os Anexos D e E valem como GABARITO, nao so como caso do uFlow.** O **Anexo D** e o gabarito
     de **como propor correcao**: arquivo exato, evidencia do codigo atual, diff minimo, analise de
     compatibilidade e retroatividade, e roteiro de validacao em 4 passos. O **Anexo E** e o gabarito
     de **como especificar trabalho para outro agente**: objetivo, atual x desejado, UX e
     acessibilidade, criterios de aceite em checklist, casos de borda, restricoes, entregaveis, e a
     ordem de **explorar o codigo antes de implementar**. **Vale como referencia de qualidade para as
     NOSSAS demandas.**

224. **✅ MODELO DO AGENTE — padrao provisorio assumido em 17 ago 2026.** Vinicius definiu que **o
     modelo sera parametro da chamada, selecionavel pelo usuario na interacao**, e que **esse desenho
     nao e para agora** — havera o momento de cambiar modelo pela plataforma e comparar saidas. Para o
     agente funcionar, assumido: `allowedProviders: ['anthropic']`,
     `defaultModel: 'claude-opus-5'`, `maxCostPerRunUsd: 5.00`.
     **Justificativa:** o agente vive hoje em Claude Projects (e de la que vem o `Papel de
     Suporte.txt`) e a tarefa e investigacao profunda em codigo com evidencia arquivo:linha — carga de
     raciocinio, nao de volume. ⚠ **O `maxCostPerRunUsd` e chute fundamentado, nao medicao:** existe
     como disjuntor contra loop, e deve ser recalibrado com o primeiro dado real de uso.
     Restam so `ownerPersonId` e `llmConnectionId`, **ambos registro de infra, nenhum decisao.**
225. **🔴 CONSEQUENCIA da decisao 224 que e barata agora e impossivel depois: `agent_runs` NAO tem
     campo de modelo.** Espec §2.5-bis. Hoje `agent_runs` guarda `connectionId`, que identifica a
     conexao de provedor, **mas nao o modelo**. E `providerPolicy.defaultModel` vive em
     `agent_versions` — e **configuracao da versao**, nao registro do que aconteceu.
     > **No momento em que o usuario puder trocar de modelo na chamada, duas respostas da mesma versao
     > de agente, com o mesmo `agentVersionId` e o mesmo `connectionId`, podem ter vindo de modelos
     > diferentes — e nao havera como distinguir.**
     Isso quebra exatamente o objetivo declarado por ele de *"cambiar de modelo pela plataforma e entao
     verificarmos as saidas"*: **comparar saidas exige saber qual modelo produziu cada uma.** Sem o
     campo, a comparacao depende da memoria de quem clicou.
     ⚠ **E backfill e impossivel** — execucao passada nao pode ganhar um dado que nunca foi gravado.
     **Uma linha (`agent_runs.model`) resolve, e so agora ela e barata.**

226. **✅ PRD LOCALIZADO por verificacao, nao por suposicao — 19 ago 2026.** O Vinicius supos que
     estivesse no repo da API. **Nao esta:** varri **todas as 115 refs** do `umode-brainhub-api` por
     arquivo adicionado com `prd` ou `prumo` — zero. **Esta no vault, e so na branch
     `governance/brainhub-v1.5`** (a `main` nao tem), em
     `BrainHub/uMode/03_Produto-e-Solucoes/brainhub/PRD-brainhub-prumo.md`, **59.427 bytes, 612
     linhas**, ultima alteracao **09 ago 2026** (`a6930d3`). A branch esta **83 commits a frente da
     `main`**, que e ancestral.
227. **🔴 O PRD QUE TEMOS E DA ERA SUPABASE/LOVABLE — e isso reposiciona todo o nosso trabalho de
     banco.** O **§6** declara como baseline o `warm-weaving.lovable.app` sobre **Supabase + RLS +
     Edge Functions**; o **§11 chama-se literalmente "Modelo de dados (Supabase)"**, com ~30 tabelas;
     as decisoes do §18 sao de **21 jul 2026**. **Mas o runtime do BrainHub 2.0 e MongoDB/NestJS com
     37 collections.**
     > **Ninguem reescreveu o §11 para a era Mongo.** O PRD segue valido para features, jornadas,
     > personas, niveis de acesso e integracoes, e esta **obsoleto exatamente no modelo de dados**.
     > **O `_dicionario-dados-brainhub.md` e a `ESPEC-BANCO-001` SAO a traducao Mongo do §11.** Nao e
     > trabalho paralelo nem duplicado: **e a secao que falta.**
228. **✅ O INBOX NAO E FOLHA EM BRANCO — e nossa espec deixa de ser "ideia nossa".** O §11 do PRD
     lista `inbox_items`, `approval_requests`, `operator_requests`, `context_queues` e `job_runs` entre
     as tabelas do baseline Supabase **a preservar e mapear**. Cruzando com o pacote do Joao, que
     classifica `Inbox` como **ausente** no runtime (§9.3) e **sem ADR** (§12.2 item 5):
     **especificado no PRD, existente no legado, ausente no Mongo, sem ADR.** Nossa espec entra como
     **a modelagem Mongo dele**.
229. **⚠ A REGUA P18 NAO ESTA NO NOSSO ALCANCE, e nao e defasagem nossa.** Nenhum dos quatro
     documentos de medicao (`MEDICAO-PRD-AWSCICD-P18`, `COMPLETUDE-FEATURE-PRD-V2`,
     `P20-CONTRACT-TRUTH-REPORT`, `REGUA-RECONCILIADA-BH20`) existe em qualquer ref do nosso clone.
     **Motivo verificado: o remoto do vault nao avanca desde 12 ago (`e847623`) e nosso clone esta em
     dia com o remoto.** Os `inbox/` de 15–17 ago vivem so na maquina do Joao.
     > **Logo: lemos o PRD, mas nao a regua.** O §7 tem ~58 itens, nao 98 — o peso e derivado em
     > documento que nao temos. **Nao podemos reproduzir nem auditar o percentual, e nao devemos
     > tentar:** seria uma **segunda regua**, o defeito que o pacote alerta na §9.1.
230. **🔴 A ARMADILHA DO --single-branch REAPARECEU — agora no frontend.** O `UmodeApp/umode-brainhub`
     esta clonado em `BrainHub - Frontend/umode-brainhub` (um nivel mais fundo do que o informado) com
     refspec **`+refs/heads/main:refs/remotes/origin/main`**: **1 ref remota, `awscicd` AUSENTE**. Pelo
     pacote, a `main` do front esta **28 commits atras e 1 divergente** da `awscicd`.
     > **Se eu lesse o frontend agora, concluiria que esta quase vazio — errando pelo mesmo motivo da
     > vez anterior. Por isso nao li nada dele.** O backend tem refspec correto mas esta **atrasado**:
     > `awscicd` local `ce54d85` contra `24781c7` do pacote, e `main..awscicd` = `0 393` local contra
     > `0 468`. **Comandos de correcao no `_levantamento-2026-08-19-repos-e-prd.md` §3.**
231. **🔴 CORRECAO GRAVE no dicionario: "esta construido e nao integrado" estava errado.** Era a
     ressalva central da faixa `[C]`. **`awscicd` E a linha de integracao**, e esta **393–468 commits a
     frente da `main`**. O certo: **integrado em `awscicd`, nao promovido para `main`.** E pior: **tudo
     que eu li veio de `codex/bhp-p16-federation-grants-back`, uma SLICE**, nao de `awscicd`. A faixa
     `[C]` vale como "existe numa slice", nao como estado da integracao.
232. **⚠ Adotar a escada de evidencia do pacote e aposentar a minha para afirmacoes de plataforma.**
     Ter `[C]/[F]/[P]/[D]` em paralelo aos 8 degraus deles (`CODE_PRESENT` → `PRODUCTION_VERIFIED`) e
     **o mesmo defeito de "colecao × collection"**: duas linguagens para a mesma ideia. Regra: **escada
     deles para o que se afirma sobre a plataforma; `[P]/[D]` so para proposta e decisao nossa.**
233. **🟠 O NOSSO REPO ESTA MAL CLASSIFICADO NA FONTE DO JOAO, e isso bloqueia o uso do corpus.** O
     pacote §3.6 lista o `brainhub-umode` como "variante antiga/PowerShell; nao foi validada como
     runtime atual", na secao **"repositorios que nao devem ser confundidos"**, ao lado do legado.
     **Ele nunca foi candidato a runtime — e o corpus de contexto.** Enquanto estiver catalogado como
     runtime reprovado, nenhum agente do Joao vai olhar para ele.
     **Acao: corrigir o papel no `SISTEMAS.md` do Joao — conversa do Vinicius com ele, nao alteracao
     nossa.**

## Varredura da carteira e da base de reuniões (22 set 2026)

> 🔴 **Nota de processo:** os itens 234–241 estavam, por engano meu, numa tabela própria no
> `AGORA.md`, criada **sem que eu tivesse lido este documento**. Era um segundo dono para o mesmo
> assunto — o defeito que o `CLAUDE.md` proíbe. **Movidos para cá, que é o dono.** O `AGORA.md`
> agora **só aponta** para esta seção.

234. **Criar a área `15_Producao-Interna`?** **Cinco clientes** têm área de produção interna sem
     contraparte canônica: `Atelier` (NV), `Oficina` (NK STORE), `Estamparia` (VIX),
     `Pilotagem` (Cambos), `Fábrica` (Osklen). Material em `_proposta-grade-de-areas-revisao.md`.
235. **`Merchandising` atingiu três clientes — vira área canônica?** NK STORE (Diretora de
     Merchandising), Reserva (grupo `Merchan`) e Luiza Barcelos (líder do projeto é Coordenador de
     Merchandising). **Minha recomendação é NÃO criar** — os três escopos diferem entre si, e
     três casos com sentidos diferentes não é um padrão, é uma coincidência de nome. `[P]`
236. **`Precificação` não tem área canônica.** Aparece como sub-time de Operações na Luiza
     Barcelos. **Não forçei encaixe** em `11_Financeiro` nem em `09_Comercial-Vendas`.
237. **Separar `Status` do cliente em três campos?** O enum atual mistura **momento da jornada**
     (`Pré Onboardings` → `Onboarding` → `Operação Assistida` → `Ongoing` → `Churn`), **modo de
     atendimento** (`Sem CS`) e **estado terminal** (`Inativo`, que virou lixeira do campo).
     Proposta: `lifecycleStage` / `serviceMode` / `recordKind`. Dono: `_taxonomia-status-cliente.md`.
238. **🔴 A base NÃO TEM campo `Data de Churn`.** Tem `Data Ativação Cliente` e mais nada.
     **Não dá para calcular tempo de vida de cliente nenhum, nem taxa de churn por coorte.**
     **É a lacuna mais cara do corpus** e depende de alteração na base do Notion.
239. **A Baw está classificada certo?** É `Sem CS` — o SKU self-service em que `SMB` no campo de
     atendimento significa "ninguém atende" — mas tem **4 módulos, atendente nomeada (Laura),
     9 chamados, 19 reuniões e 18 demandas**. **E tem o módulo `Integração` com o ERP dizendo
     `Sem Integração`** — os dois não podem estar certos.
240. **Reunião e demanda que atendem DOIS clientes — como registrar?** Achados dois casos na
     fonte: a reunião *"uFlow - Highstil/Plié - 16/04/2025"* e uma demanda de 30/06/2025 com
     **Básico&Co + VIX**. **O isolamento de cliente é regra travada no `CONTEXT.md`** e a fonte
     não a respeita. **Dois registros ou um registro com duas relações?**
241. **`## O que este documento NÃO resolve` vira título canônico nas 4 classes de MD de cliente?**
     Hoje aparece em parte dos arquivos. **Padronizar muda ~145 arquivos** — e, pela regra travada
     pelo Vinicius, **se virar padrão tem de ser replicado em toda a classe, retroativamente.**

### Achados desta varredura que **não** são decisão do Vinicius — são trabalho nosso

242. **🚨 Duas credenciais expostas em texto claro no Notion, não rotacionadas:** NK STORE
     (usuário, senha, IP, porta e nomes de banco de homologação e produção do Linx do cliente) e
     Lofty Style (senha de `docs.umode.app`). **Nenhum valor foi copiado para o corpus** —
     verificado por grep automático. **Falta rotacionar e varrer as demais fontes.**
243. **22 reuniões órfãs** na base `Reuniões Compartilhadas`: **15 apontam para
     `. Página Cliente [Template]`** e **7 não têm cliente nenhum**.
244. **O campo `Data` da base de reuniões está corrompido em lote.** Sete reuniões da Recco com
     títulos de 04/09 a 16/10/2025 carregam todas `02/09/2025`. **Qualquer visão dessa base
     ordenada por `Data` está errada.**
245. **Três vocabulários de status convivem sem relação declarada:** o enum `Status` do cliente,
     o semáforo de 4 colunas das atas (`Geral`/`Prazo`/`Pendências`/`Riscos`) e o selo único
     `Projeto em Regime`. **Mesma pergunta, três linguagens** — mesmo defeito de "coleção ×
     collection" apontado no item 232.
246. **⚠ Dois casos de gestão de narrativa com o cliente, registrados por escrito.** Recco
     (16/10/2025: quatro semáforos verdes sobre inadimplência de duas mensalidades e sistema
     travado) e Luiza Barcelos (08/08/2025: *"precisamos organizar a resposta que o time levará na
     weekly com o cliente"*). **Dois é hipótese — registro e vigio o terceiro.** Não julgo as
     decisões; registro que existem, com data e dono.
247. **Sistemas descobertos e ainda fora do `_inventario-repositorios.md`:** `Linear` (rastreador
     de engenharia da uMode, com projeto `NexusAPI`), `Timec` (terceiro de integração da Luiza
     Barcelos) e `Mold`. Somam-se a `Kanbanize`, `Gist`, `docs.umode.app`, `HubSpot`, `Trello`,
     `Banner`, `SAP`, `Qualitá`, `Totvs Virtual Age` e `Safe Tech`.
248. **A `Hering` está em `Pré Onboardings` há 15 meses, com 25 reuniões.** O enum não tem como
     expressar "pré-onboarding longo" — relacionado ao item 237.

## Varredura transversal de pessoas e ferramentas (22 set 2026)

249. **🔴 A linha da CAEDU mudou de `Ongoing` para `Onboarding` em 22/09/2026, às 15:04 —
     entre duas leituras minhas do mesmo dia.** **Não sei o que motivou** e não presumo.
     **Precisa ser perguntado**, porque a CAEDU é a conta da próxima frente. Dezessete clientes
     foram editados na base nesta mesma data.
250. **🔴 Um agente de IA abre demanda, e o modelo não prevê isso.** O **`Hermes`** consta como
     `Quem solicitou?` em **5 demandas da NK STORE**, entre 29/07/2025 e 18/03/2026. **Para o banco
     isso não é `person`, é `agent`** — e a `_espec-pessoas-e-comunicacoes.md` **não prevê agente
     como autor de demanda**. Decidir: `demand.requestedBy` aceita `person | agent | team`?
251. **🔴 O campo `Quem solicitou?` mistura cinco coisas:** pessoa, área/time, pessoa da uMode,
     agente e canal colado no nome (*"Vanessa - Grupo whatsapp"*, *"Camila - via chat <URL>"*).
     **Não é campo de pessoa.** Para o banco precisa virar relação tipada, não texto.
252. **🔴 Variação de grafia de nome ameaça a identidade de pessoa.** A mesma pessoa aparece com
     até **oito formas** (Osklen: `Thais Pantaleão` → `Thays` → `Taissa` → `Tayssa`...).
     **Não unifiquei nada**, porque sem e-mail isso inventaria pessoa — e há o risco oposto:
     a VIX registra literalmente **`Luana Henriques & Luana Carmo`**, **duas pessoas**, e o nome
     curto `Luana` (11 demandas) não diz qual. **Decidir a chave de identidade de pessoa.**
253. **`Atendimento 2025` é texto livre com uma dupla dentro:** `Julianne + Pedro` atende 7 contas.
     **Para o banco são dois `person_memberships`, não um valor de texto.** E `SMB` nesse campo
     **não é pessoa** — é o Grupo 3 da segmentação (ver item 237).
254. **Dois ERPs fora do inventário: `Ilimitar`** (Moda Objetiva, Hering) e **`Avec`** (Hyperlocal).
     E **`Linx / SAP` × `SAP e Linx` são duas grafias do mesmo conceito** — Puket e Reserva usam
     uma, Oficina Reserva e Arezzo usam a outra. **Normalizar o enum de ERP.**
255. **⚠ `facção` aparece como time na Lenny Niemeyer** (*"Time facção Conrrado e Ingrid"*).
     **Não é o mesmo caso do item 234** (`15_Producao-Interna`): **facção é produção externa.**
     Decidir se área canônica precisa distinguir produção própria de terceirizada.
256. **⚠ Um e-mail de domínio de terceiro aparece como solicitante na Reserva:**
     `engenharia1@indorf.com.br`. **`indorf.com.br` não é domínio da Reserva** — confirmar se é
     fornecedor, facção ou empresa do grupo.

## Auditoria de duplicação e respostas do Vinicius (22 set 2026)

257. **🔴 Apagar o `_staging-lofty-demandas.md`?** São **2.645 linhas de duplicata integral**
     dentro de `Lofty Style/00_Institucional/_demandas/`. **Verificado: as 85 demandas do staging
     estão todas formalizadas nos 85 `D-*.md` da mesma pasta, e nenhuma existe só nele.** `[C]`
     **Era o único dos 999 arquivos de demanda fora do padrão canônico.** **Marcado `SUPERSEDED`,
     não apagado — apagar é decisão do Vinicius.**
     🔴 **E há um SEGUNDO:** o `_staging-lofty-rfis.md`, 612 linhas, na pasta `_rfis/` da
     mesma conta — **achado pelo próprio validador novo, na primeira execução.** 15 RFIs no
     staging, 15 arquivos `RFI-*.md`. ⚠ **Aqui a verificação foi por contagem, não id a id** —
     evidência mais fraca que a das demandas, onde os 85 IDs bateram um a um.
258. **🟢 RESPONDIDO — item 249.** A CAEDU virou `Onboarding` por **entrada em novo escopo**,
     não por regressão. **Mas isso expõe um limite:** conta `Ongoing` que entra em escopo novo
     volta a `Onboarding` e **o campo perde que ela já operava**. **Reforça o item 237:**
     `lifecycleStage` deveria ser **por escopo contratado**, não por cliente.
     ⚠ **Qual é o novo escopo da CAEDU, ainda não sei.**
259. **🟢 PARCIALMENTE RESPONDIDO — motivo de churn.** O Vinicius confirmou que a
     **Lenny Niemeyer é churn de fato** (*"é certeza"*), e que **Highstil e Plié são do mesmo
     grupo** e estavam em **corte de gastos** — **com a ressalva dele próprio:** *"acho que foram
     churn"*, *"se não me engano"*. **Gravado como `[D]` com a ressalva.** **Nenhuma fonte
     documental confirma motivo nem data** — o item 238 (`Data de Churn`) segue aberto.
260. **🔴 O corpus precisa do nível `Grupo` acima de `Cliente`?** **Highstil e Plié são do mesmo
     grupo** (confirmado pelo Vinicius), o que **explica** a reunião conjunta que o item 240
     tratava como quebra de isolamento. **Não era defeito da fonte.** Já há outros casos:
     **Puket é marca do Grupo Único**; **Reserva, Oficina Reserva e Simples (by Reserva)** são do
     mesmo ecossistema. **A hierarquia travada no `CONTEXT.md` começa em `Instituição`** —
     decidir se `Grupo` entra, e como, **é decisão de arquitetura do Vinicius.**
261. **⚠ O validador não olhava dentro de `_demandas/` e `_rfis/`.** Foi por isso que o staging
     passou meses sem ser flagrado. **Corrigido em 22 set 2026:** o
     `scripts/valida-padrao-corpus.py` passou a conferir a assinatura de títulos dos arquivos de
     demanda e RFI. **Lição: verificador que ignora uma pasta nunca acha nada nela.**

## Base de chamados e identidade de pessoa (22 set 2026)

262. **🟢 RESOLVIDO EM PARTE — item 252, a chave de identidade de pessoa.** A base
     **`Chamados & Atendimentos`** tem **campo `Email` individual**: 92 e-mails distintos em 185
     chamados. **Eu havia generalizado errado:** escrevi que *"nenhuma pessoa tem e-mail"* quando
     o correto era *"não tem **neste campo**"*. ⚠ **A base cobre um mês só** (06/01 a
     05/02/2026) — **fora dessa janela a chave não existe.** **Decidir: `person.email` é a chave
     primária de identidade?**
263. **🟢 As duas Luanas da VIX são reais** — `luana.henriques@vixbrasil.com` e
     `luana.carmo@vixbrasil.com`. **Confirma que foi certo não unificar.** ⚠ **As 11 demandas
     assinadas só `Luana` seguem sem dono** — ter a chave não conserta o dado escrito sem ela.
264. **🔴 18 chamados estão com o campo `Cliente` VAZIO e o domínio do e-mail diz de quem são.**
     **É dado recuperável por regra.** **Não preenchi a base** — escrita no Notion não é nossa.
     **Decidir quem corrige, e se o domínio vira regra de derivação.**
265. **🔴 Terceiros têm conta na plataforma, e o modelo não os prevê.** Onze e-mails de
     **fornecedores** abriram chamado (`@indorf`, `@floc`, `@mclprivatelabel`, `@vape`,
     `@lavinorte`, `@vestsurf`, `@eczoz`). **É o módulo `Fornecedores` em operação.**
     🔴 **É matéria de permissionamento:** um fornecedor que atende Reserva **e** Oficina
     Reserva enxerga o quê, de quem? **A `_espec-pessoas-e-comunicacoes.md` não modela terceiro
     com acesso.**
266. **⚠ Três pessoas constam sob cliente que não bate com o domínio do e-mail** — `mariana.basso`
     (Baw) sob Oficina Reserva, `vinicius.dias` (NV) sob VIX, `karine.pires` (Reserva) sob Oficina
     Reserva. **Os dois primeiros parecem erro; o terceiro pode ser legítimo por serem do mesmo
     grupo.** **Distinguir exige a decisão do item 260 (nível `Grupo`).**
267. **🔴 `Funcionalidade da Plataforma` é um eixo que o corpus não tem.** A base de chamados
     relaciona chamado → funcionalidade → produto. **É o vínculo que falta para ligar dor de
     cliente a parte do produto** — e nenhuma das relações foi resolvida nesta varredura.
268. **`Canal` é campo tipado na base de chamados** (ex.: `Chat Plataforma`). **É a primeira fonte
     com enum de canal** — confrontar com `communication_channels` da espec antes de travar o
     nosso. E **`Resolução`** (ex.: `TECH`) **é campo novo, não registrado no corpus.**

## Decisões do Vinicius e painel de prontidão (22 set 2026)

269. **🟢 DECIDIDO — item 260, o nível `Grupo`.** **NÃO entra agora.** Palavras dele:
     *"a nível de sistema isso é altamente necessário, no entanto, quando estamos falando de
     cérebro, a ideia de separar em áreas já deixa a questão de permissionamentos muito diferentes
     entre áreas e portanto, entre empresas do mesmo grupo isso é praticamente impensável...
     partindo do brain básico da companhia, podemos operar sob a **hierarquia máxima de cliente**."*
     `[D]`
     **Consequência prática:** Puket/Grupo Único, Reserva/Oficina Reserva e Highstil/Plié seguem
     como **clientes independentes**. A relação de grupo fica **registrada como contexto**, não
     como nível hierárquico. **Não reabrir sem instrução.**
270. **🟢 DECIDIDO — item 262, a chave de identidade de pessoa.** **E-mail serve como chave,
     mas não sozinho.** Palavras dele: *"se em dado momento aparecer uma mesma pessoa, mas com
     dois endereços — seriam duas pessoas? Não faz sentido... você terá que ter sempre uma
     avaliação sobre todos os e-mails concentrados de uma empresa/cliente e levantar suspeitos de
     serem as mesmas pessoas."* `[D]`
     **Vira obrigação de processo, não só de campo:** toda varredura de pessoa de um cliente
     **fecha com uma análise de suspeitos de duplicidade** sobre o conjunto de e-mails daquele
     cliente. **Suspeita se levanta; fusão só com confirmação humana.** → **entra no
     `protocolo-varredura-cliente.md`.**
271. **⚠ Fornecedor é o único que conecta múltiplos clientes** — e **brain de fornecedor não está
     no escopo ainda** (decisão do Vinicius). **Item 265 fica registrado e parado.**
272. **🔴 O enum de RFI tem 11 valores e nenhum conjunto terminal declarado.** Não dá para contar
     "RFI em aberto" sem decidir **o que fecha uma RFI**. **Usei classificação `[P]` minha**
     (terminal = `Entregue ao Cliente`, `Post Mortem`, `Cancelada`, `Não Aceita`). **Confirmar.**
273. **🔴 A base de chamados tem cinco valores de `Status` para dois estados.** `Fechado` e
     `Resolvido` são a mesma coisa; `Não iniciada`, `Pendente` e `Em Aberto` são três sabores de
     aberto. ⚠ **E `Não iniciada` está no feminino**, os outros no masculino — enum montado em
     momentos diferentes. **Normalizar.**
274. **🔴 55% dos chamados estão abertos** (101 de 185) numa janela de um mês, concentrados em
     NK STORE (19), NV (14), VIX (13) e Lofty Style (9). **Não concluo causa** — registro o número.
275. **🔴 A Reserva tem 84 demandas abertas, 44 só em `Backlog`** — quatro vezes a segunda
     colocada. **Tem os 7 módulos (a única) e apenas 13 reuniões, a última em 13/06/2025**, há
     quinze meses. **Mais escopo, mais fila e menos encontro que qualquer `Ongoing`.**
276. **🔴 A LACUNA QUE MAIS IMPORTA PARA O PERMISSIONAMENTO: cargo e área por pessoa.** Eu tenho
     **quem age e quando**, em 15 clientes. **Não tenho `cargo` nem `área` de forma estruturada
     para quase ninguém** — e **sem isso não há como derivar permissão por área**, que é a base do
     cérebro que o Vinicius descreveu. **Nenhuma fonte varrida traz isso estruturado.**
277. **🔴 33 dos 48 clientes não têm UMA pessoa sequer identificada.** **É a maior lacuna do
     corpus em número**, e a fonte restante são as **páginas de `Documentação Clientes`** no Notion.

## CX Hub como referência de desenho (22 set 2026)

278. **🟢 DECIDIDO pelo Vinicius — o CX Hub não tem dado.** *"A feature foi colocada, mas nunca
     finalizada de fato."* `[D]` **Li 170 migrations: os `INSERT` são todos de configuração.**
     **O repositório vale como referência de DESENHO, não como fonte.** **Não voltar a procurar
     dado lá.**
279. **🔴 Dois vocabulários de RFI sem mapeamento, e uma diferença estrutural maior.** CX Hub
     tem **4 status** (`Previsto`/`Orçada`/`Aceito`/`Recusada`); o corpus tem **11**. E no CX Hub
     **`rfis.demand_id` é `NOT NULL UNIQUE`: uma RFI é 1:1 com uma demanda**, enquanto no corpus
     são entidades separadas com vínculo opcional (44 de 999). **É decisão de modelo.**
     ⚠ E a RFI do CX Hub carrega `budget_value` e `due_date`.
280. **🔴 O padrão de permissão do CX Hub é "todo mundo vê tudo".** O trigger
     `grant_new_client_to_all_users` dá `viewer` de **todo cliente novo** para **todos os
     usuários**. 🟢 A estrutura `(usuário × cliente × role)` **confirma a decisão de que a
     hierarquia máxima é o cliente** (item 269). **Mas o default precisa ser o inverso.**
281. **🔴 Status de demanda no CX Hub é COLUNA DE KANBAN, não enum.** `demands.column_id` aponta
     para `ticket_columns`, e `started_at`/`finished_at` são **disparados pela coluna**.
     **Estruturalmente diferente do `Etapa` do Notion.** **Duas taxonomias, nunca fundidas.**
282. **⚠ `client_tier` mistura porte com nome de grupo:** `('azzas','enterprise','medium','small')`.
     **Três valores são porte; um é nome próprio.** **Não sei o que `azzas` significa neste enum.**
283. **🔴 A PÁGINA DOS 33 CLIENTES NÃO EXISTE — correção de um próximo passo meu.** Eu havia
     proposto varrer *"as páginas dos 33 clientes sem pessoa"*. **Verifiquei antes de executar:
     só 9 clientes têm `Documentação Clientes`, e 8 já foram varridos.** O que existe para os
     demais são **sub-páginas no corpo da página** (`Onboarding`, `Playbook`, `Reonboarding`) e
     **databases inline** — **não abertas.**
284. **🔴 A Vivara está em `Churn` e tem uma página `Reonboarding Vivara`.** **É reentrada, não
     conta morta.** **Sétimo caminho independente mostrando que `Status` ≠ realidade.**
285. **🔴 A PERGUNTA MAIS IMPORTANTE EM ABERTO: onde vive `cargo` e `área` de pessoa?**
     Procurei em **sete fontes**: `Mapa de Clientes`, `Demandas`, `Chamados`, `Reuniões`,
     `Portal do Cliente`, páginas de cliente e o **schema do CX Hub** (onde `user_profiles` só
     tem `global_role` com 3 valores). **Nenhuma tem cargo ou área estruturados.**
     🔴 **Se não existe fonte, isto não é lacuna de varredura — é dado a ser criado.**
     **E sem ele não há permissionamento por área.** **É pergunta para o Vinicius, não tarefa
     para mim.**

## Permissionamento e perfil como área (22 set 2026)

286. **🟢 O MODELO DE PERMISSIONAMENTO DA uMODE ESTÁ DECLARADO.** Da página
     `[NV] Permissionamento`: *"o permissionamento pode ser configurado de duas formas:
     **Inclusão** (tudo que o perfil **pode** fazer) e **Restrição** (tudo que **NÃO pode**)"*.
     **Allowlist e denylist, escolhidas por perfil**, com granularidade por campo e por tela
     (🟢 ver e editar · 🟡 parcial · 🔴 nem ver). **É a primeira definição de modelo de permissão
     achada em qualquer fonte.** 🔴 **E confronta o CX Hub**, onde o default é todo mundo ver
     tudo (item 280). **Decidir qual vale para o BrainHub.**
287. **🟢 O PERFIL DE USUÁRIO É A ÁREA DO CLIENTE** — **nona fonte de vínculo pessoa↔área**, e a
     mais estruturada, porque é o que o sistema aplica. **12 clientes têm permissionamento
     documentado.** A NV tem **13 perfis nominais**, lidos na página.
288. **🔴 O campo de perfil mistura área com nível de acesso.** Na NV, `Geral`, `Master`, `View` e
     `Planner 2` **não são área, são privilégio** — **mesmo defeito do `Status` de cliente.**
     **Separar `area` de `accessLevel` no modelo de perfil.**
289. **🔴 A convenção de nome de perfil é de cada cliente:** `NV - Estilo`, `Vix-Estilo`,
     `Lofty - Estilo`, `Objetiva - Estilo`, `NK - Estilo Master` e a **Baw sem prefixo**
     (`Estilo`). **Cinco grafias para a mesma área.** **`profile.name` não serve de chave de
     área** — precisa de `area_id` normalizado. Confirma o achado da Puket.
290. **⚠ `Qualidade`, `Atacado` e `Logística` aparecem como perfil na NV e não têm área
     canônica** na grade de 14. Somam-se a `Merchandising`, `Precificação` e produção interna.
291. **🔴 Uma árvore de documentação que o corpus nunca mencionou:**
     `uFlow / Documentação de Setup - PLM / CLIENTES (Em desenvolvimento)`, com **9 clientes**
     (NV, RESERVA, BAW, OFICINA, VIX, StudioZ, PUKET, CAEDU, NK Store). ⚠ **Mas é quase toda
     esqueleto:** NV e RESERVA têm conteúdo real; **StudioZ tem uma sub-página; a CAEDU está
     VAZIA.** **5 das 9 não foram abertas.**
292. **🟢 PRIMEIRA CONCILIAÇÃO COMPLETA pessoa ↔ e-mail ↔ área ↔ permissão.** A página
     `Trava de Ficha` da Reserva diz: *"**Vanessa Sousa e Karine Pires** (**time de Cadastro**)
     tem acesso para editar/incluir Variantes"* — e as duas batem com
     `vanessa.sousa@usereserva.com` e `karine.pires@usereserva.com` da base de chamados.
     ⚠ **E isso reequilibra o item 266:** `karine.pires` aparecia sob Oficina Reserva na base de
     chamados; esta página a coloca na **Reserva**. **Sem confirmação definitiva, mas o peso mudou.**
293. **🔴 O ELO QUE FALTA PARA FECHAR A CORRENTE: a atribuição perfil↔pessoa.** A página da
     Moda Objetiva cita uma **"Planilha de e-mail dos usuários"** — **não aberta**. **Se ela ligar
     e-mail a perfil, fecha `pessoa → perfil → área → permissão`** e resolve o item 285.
     🔴 **É o próximo passo de maior rendimento do corpus inteiro.**

## CAEDU 2.0 e o grafo do corpus (22 set 2026)

294. **🔴 97,7% DO CORPUS É ÓRFÃO.** Medido pelo `scripts/valida-indexacao.py`, escrito a
     pedido do Vinicius para preparar a visualização em Obsidian: **2.044 arquivos `.md`,
     1.998 sem NENHUM link de entrada, 7,1% com qualquer ligação.** `[C]`
     🔴 **No Obsidian isso aparece como nuvem de pontos soltos, não como cérebro.**
     **Decidir a estratégia de indexação** — e ela não pode ser manual em 2.044 arquivos.
     **Proposta `[P]`:** os 4 MDs canônicos de cliente ganham, por script, um bloco de ligações
     (cliente ↔ áreas ↔ pessoas ↔ demandas ↔ RFIs ↔ autoridades citadas).
295. **⚠ Wikilink por nome simples é ambíguo neste corpus** — há **49 arquivos `pessoas.md`**,
     49 `jornada.md`, 50 `institucional.md`. **`[[pessoas]]` no Obsidian não resolve.**
     **Regra proposta:** dentro do corpus, link sempre por **caminho relativo**; wikilink simples
     só para os nomes únicos (as autoridades e registros de `00_Institucional`).
296. **20 links quebrados**, dos quais a maioria é falso-positivo: menção literária à palavra
     *wikilinks* e **links para o vault do João**, que é repositório externo. ⚠ **Confirmar se o
     `_recebido-2026-08-18` deve manter links para caminhos que não existem aqui.**
297. **🔴 CAEDU: o `uFlow` tem data de desligamento — 12 meses a partir do contrato.** É a
     **primeira data de desligamento de legado** registrada para qualquer cliente. **O corpus
     não tem campo para isso.**
298. **🔴 CAEDU: cláusula de saída em 3 meses pedida pelo cliente.** ⚠ **Não sei se entrou no
     contrato** — nem o time sabia. **O corpus não tem campo de cláusula contratual.**
299. **🔴 CAEDU: a uMode vai emprestar um desenvolvedor para o cliente construir a API que a
     própria uMode vai consumir.** Decorre da decisão do TI da CAEDU de **não liberar acesso ao
     banco** e do fato de o **Linx não ter API nativa**. **É arranjo comercial e risco de prazo ao
     mesmo tempo** — e ameaça a cláusula de 3 meses.
300. **⚠ CAEDU: o Escopo 2 é confidencial e restrito à diretoria.** A razão está escrita na
     proposta: cadeiras de trabalho manual **são descontinuadas**. **Registrei que existe e o que
     é; não repliquei o detalhe fora do registro.** **Confirmar com o Vinicius até onde isso pode
     circular no corpus.**
301. **🔴 `Grife › Linha › Grupo › Subgrupo`** — hierarquia de produto que a CAEDU precisa e o
     corpus não modela. ⚠ **E `Grupo` e `Subgrupo` estão hoje no MESMO campo**, segundo o cliente.
302. **⚠ Um concorrente foi demonstrado ao vivo pelo cliente, na frente da uMode:**
     **`Coleção Moda`**, na visita de 22/07/2026. **É o único caso da carteira.** A Vanessa filmou;
     **os vídeos estão no Notion e não foram abertos.** **Vale abrir antes do kickoff.**
303. **🔴 `Brain Wave` (também dito `Green Wave`) — plataforma interna da uMode para gerar
     software falando.** João: *"se ele ainda assim fizer a integração, nós temos uma máquina aqui
     de produzir software."* **Não está no `_inventario-repositorios.md`.**
304. **⚠ CAEDU: só UMA pessoa da Qualidade tem acesso à plataforma** (visita 22/07). **É a lacuna
     de permissionamento mais concreta já encontrada**, e conecta com o item 287 (perfil = área).

## Camada de conexão gerada (22 set 2026, mesma sessão)

305. **🟢 RESOLVIDO — item 294.** O Vinicius cobrou na hora: *"praticamente 100% está órfão?
     Isso praticamente invalida tudo... sem isso nada do brain funciona. Tudo tem que estar
     conectado a algo."* **Escrito o `scripts/gera-conexoes.py`** e executado.
     **Órfãos: 1.998 (97,7%) → 88 (4,2%). Conectados: 7,1% → 96,0%.** `[C]`
     **O que a camada liga:** cada um dos 3 MDs do cliente aos outros dois e às 14 áreas · cada
     área de volta à casa e às outras 13 · cada uma das **999 demandas** e **86 RFIs** ao cliente e
     ao protocolo que a governa · e um **`_indice.md` por pasta de registro**, para que cada
     demanda tenha entrada no grafo.
     ⚠ **Links relativos, não wikilink por nome** — pelo item 295 (49 `pessoas.md`).
306. **⚠ Restam 88 órfãos (4,2%)** — principalmente `brainwave/`, o `_boilerplate/` e alguns
     registros de `00_Institucional`. **Não é defeito automático:** documento externo e frente
     paralela podem legitimamente não ter entrada. **Decidir quais devem ser ligados.**
307. **⚠ A seção `## Conexões` é GERADA e não se edita à mão** — a próxima execução sobrescreve.
     **Entrou em 1.906 arquivos**, ou seja, em 100% de cada classe do corpus, respeitando a regra
     de que estrutura não varia dentro da classe. **`gera-conexoes.py` passa a fazer parte do
     ritual de fechamento.**

## Varredura da página da CAEDU (22 set 2026)

308. **🔴 AS ATAS DA CAEDU ESTÃO EM TRÊS ACERVOS QUE NÃO SE FALAM.** A base
     `Reuniões Compartilhadas` tem **35**; a **sub-página `Reuniões com o cliente`, dentro da
     página da CAEDU, tem ~47** (24/04/2024 a 16/09/2025); e há as **7 transcrições Tactiq**
     entregues em 22 set. 🔴 **O Vinicius ia reunir ~50 agendas manualmente — vale confrontar
     antes, pode ajudar.**
     🟢 **CORRIGIDO PELO VINICIUS no mesmo dia:** *"essas são **anotações manuais** em sua
     grande maioria. Mas as **transcrições** que vou trazer são **reais**."* `[D]`
     **Os dois acervos NÃO se substituem** — um é nota escrita à mão, o outro é transcrição.
     **São fontes de natureza diferente e ambas valem.** Eu sugeri que um poupava o outro:
     **estava errado.** ⚠ **Não verifiquei ata a ata a
     sobreposição entre os acervos 1 e 2.**
309. **🔴 Sub-página de cliente é um tipo de fonte que NENHUMA consulta SQL alcança.** As ~47
     atas viviam como sub-página, não como linha de base — por isso nunca apareceram.
     **→ O `protocolo-varredura-cliente.md` precisa exigir: abrir a página do cliente e listar as
     sub-páginas**, não só consultar as bases.
310. **🟢 O formato de ata da CAEDU é candidato a padrão da carteira.** Ela separa por dono:
     `Pauta` · `For uMode` · `For CAEDU` · `Caedu TI`, com item concluído riscado e marcação de
     prioridade. **Nenhuma outra fonte separa responsabilidade por lado.** Há um `Modelo de Ata`
     na mesma pasta. ⚠ **Confirmar se outros clientes usam o mesmo modelo.**
311. **🔴 A dor da hierarquia `Griffe › Linha › Grupo/subgrupo` é de SETEMBRO DE 2025**, e
     reapareceu idêntica na visita de 22/07/2026 e na reunião de integração de 25/08/2026 —
     **inclusive com a mesma frase sobre a API estar do lado do cliente.** **Atravessou três
     ciclos de discussão sem destravar.** **Muda a leitura do CAEDU 2.0: não é dor descoberta na
     visita, é dor conhecida há mais de um ano.**
312. **⚠ O `Manual do Cliente para o Sistema PLM` da CAEDU é de 24/08/2023 e descreve módulos que
     não são os do uFlow atual** (*"Projetos"*, *"Documentos"*, *"Colaboradores"*).
     **Documentação de produto de três anos atrás, viva na página do cliente.**
313. **⚠ Sem acesso à sub-página `Fornecedores da Caedu`** — 404 por este conector.
     **Não afirmo que não existe: afirmo que não alcancei.**

## Pessoa vira arquivo (22 set 2026)

314. **🟢 DECIDIDO — pessoa de cliente É ARQUIVO.** Vinicius, textual: *"cada pessoa tem sim
     que ser um arquivo e realmente ter vários outros nós com ela. Isso não tem dúvida."* `[D]`
     **Executado no mesmo dia:** escrito o `scripts/gera-fichas-pessoa.py`, que criou
     **127 fichas em 17 clientes** a partir do campo `Quem solicitou?` das demandas.
     **Estrutura idêntica à do `_template_pessoa.md` da Casa**, porque o `CLAUDE.md` trava que
     *"Áreas e Pessoas são iguais entre Casa e clientes"*; campo que só faz sentido para a Casa
     fica marcado **não se aplica**, nunca apagado.
     **O gerador não unifica grafia** (§ 9 do protocolo) e **não cria ficha para o que não é
     pessoa** — filtra área, time, agente (`Hermes`), canal e pessoa da uMode.
315. **🔴 As 127 fichas nascem com `cargo` e `área` em `[a preencher]`** — porque **nenhuma
     das 8 fontes varridas traz isso estruturado** (item 285). **A ficha não resolve a lacuna:
     ela dá o LUGAR onde a lacuna passa a ser visível e preenchível, uma pessoa por vez.**
316. **⚠ São 127 fichas para ~200 nomes observados.** A diferença são células com **duas pessoas
     juntas** (`Carol/Denize`), áreas e times. **Não desmembrei sem confirmação** — desmembrar
     `Fabi e Carol` em duas fichas é inventável, e a regra de ouro proíbe.
317. **⚠ Os 31 clientes sem tabela de solicitante não ganharam ficha nenhuma.** Não têm demanda,
     logo não têm pessoa observada. **Depende das páginas e das atas, não do gerador.**
## Ferramenta vira arquivo, e a `Etapa` contradiz o `Status` (22 set 2026)

318. **🟢 DECIDIDO — o modelo é `entidade = arquivo`, e a lista é maior do que eu aplicava.**
     Vinicius, textual: *"praticamente tudo que for uma entidade é arquivo? Ou seja, ferramenta,
     pessoas, empresas, áreas, demandas, RFIs, tudo.... As reuniões, contextos gerais, e-mails,
     tudo isso vai estar de alguma forma ligada a esses nós maiores na escala de hierarquia."* `[D]`
     **Placar no dia da decisão: 6 tipos eram arquivo, 5 não eram.** Ferramenta foi fechada na
     mesma sessão (**16 fichas**). **Faltam reunião, e-mail e agente.**
319. **`[P]` A ferramenta foi para DUAS pastas, e é proposta minha — precisa de aval.**
     `03_Produto-e-Solucoes/_ferramentas/` para os **7 módulos que a uMode vende**;
     `06_Tecnologia/_ferramentas/` para os **9 sistemas de terceiro**. **Motivo: `Linx` não é
     produto da uMode**, e guardá-lo em "Produto e Soluções" ensinaria o contrário a quem ler.
320. **🔴 6 das 7 fichas de módulo têm `Solução do portfólio` em `[a preencher]`.** Só
     `Gestão de Coleção → DesenvolvAI` está confirmado no `CONTEXT.md`. **Decidir o mapeamento
     dos outros 6 é decisão sua** — o `CONTEXT.md` proíbe inferir por nome parecido, e eu obedeci.
321. **🔴 `Millennium` é opção viva do enum `ERP/Integração` com ZERO clientes.** Nunca apareceu
     no corpus. **Some ou fica?**
322. **🔴 Terceiro par duplicado no mesmo campo: `Não` e `Sem Integração` querem dizer a mesma
     coisa** (os outros dois: `Linx / SAP` × `SAP e Linx`, e `Totvs` × `Totvs Moda`).
     **Um caso é anedota, dois é hipótese, três é padrão: o campo `ERP/Integração` precisa de
     limpeza de enum, não de correção linha a linha.**
323. **🔴 ACHADO NOVO — existe a base `Etapas do Processo de Clientes`, e ela discorda do campo
     `Status` em 5 dos 31 clientes preenchidos.** `collection://348b1d38-…-000bea495254`.
     **Caedu** (`Onboarding` × **`Ongoing`**) · **Osklen** e **Moda Objetiva**
     (`Operação Assistida` × `Onboarding`) · **Lofty Style** (`Ongoing` × `Operação Assistida`) ·
     **Loungerie** (`Onboarding` × `Pré Onboarding`). **É a sétima evidência de que `Status` não
     é confiável — e a mais forte, porque a contradição é entre dois campos da MESMA linha.**
     **Qual dos dois manda?**
324. **🔴 A CAEDU é o único dos cinco que está ADIANTE do que o `Status` diz** — e o `Status`
     `Onboarding` é a premissa do projeto CAEDU 2.0. Junto com a dor de
     `Griffe › Linha › Grupo/subgrupo` já escrita na weekly de **16/09/2025**:
     ⚠ **a CAEDU parece um cliente que já operou sendo tratado como estreia.**
     **Leitura minha, não fonte — mas é pergunta para você.**
325. **⚠ 19 dos 50 clientes não têm etapa nenhuma — incluindo a `Reserva`**, que tem
     **7 módulos, o mais completo da carteira**, mais `Oficina Reserva`, `NV` e `Baw`.
     **Não sei se é lacuna de preenchimento ou se conta grande não passa pelo funil.**
326. **🆕 Duas etapas `Especial` existem e estão vazias: `Projetos e Inovação` e
     `Squad de Urgência`.** Mesmo padrão do CX Hub — construído, nunca preenchido.
     ⚠ **Mas `Projetos e Inovação` é onde o CAEDU 2.0 caberia.**
327. **⚠ `Mapa de Clientes` tem 5 relações e eu só tinha varrido 2.** Ainda fechadas:
     **`Segmentação Grupos`** (`collection://a4103fe2-…`) e **`Atendimento 2024`**
     (`collection://c82a689c-…`). **Varrer uma base é varrer também para onde ela aponta** —
     entra no `protocolo-varredura-cliente.md`.
328. **⚠ `Responsável Pela Etapa` aponta para `collection://348b1d38-…-000b7f91e638`, que dá 404
     por este conector.** **Não afirmo que não existe: afirmo que não alcancei.**

## A página do cliente tem `cargo` e `área` (22 set 2026)

329. **🔺 CORREÇÃO DE ERRO MEU — `Hermes` não é o agente, é pessoa.** `Hermes Gonçalves
     Santiago Junior`, **Gerente de TI da NK STORE**, com **5 demandas abertas**. Eu o tinha
     posto na lista `NAO_PESSOA` do gerador **presumindo que fosse o agente `Hermes` da uMode**.
     **Corrigido, com o motivo escrito no script.** **Homônimo entre agente e pessoa se resolve
     com fonte, nunca com filtro cego por string.**
330. **🔺 CORREÇÃO DE ERRO MEU — `cargo` e `área` TÊM fonte** (contra os itens 285 e 315).
     **A página de cada cliente tem um toggle `Pessoas`** com nome completo, cargo, área,
     e-mail e telefone. **Eu media pelas BASES, e a página do cliente não é base.**
     **Quarta variação de "não encontrei em X" virando "não existe".**
331. **🟢 O template de pessoa já existe e é o mesmo em todos os clientes** — 4 blocos:
     `Diretores e Representantes Legais` · `Responsável pelo Financeiro` ·
     `Responsáveis pelos Projetos` (Diretoria / Líderes do Projeto / Líderes de Departamentos) ·
     `Responsável Tecnologia`. **A lacuna não é de modelo, é de preenchimento.**
     **Quantos dos 49 clientes preencheram? É uma leitura por cliente, e vale medir.**
332. **🔴 8 das 13 pessoas da NK STORE nunca abriram demanda — incluindo as DUAS diretoras do
     projeto** (Regiane Konopka, Merchandising; Stella Sunaga, Estilo). **A base de demandas
     mede quem abre chamado, não quem decide** — usá-la como censo subestima a liderança.
     **NK STORE passou de 15 para 24 fichas.**
333. **🔴 A página da Osklen tem o mesmo toggle `Pessoas` e está INTEIRAMENTE VAZIA** — conta em
     `Operação Assistida` **sem uma pessoa nomeada na própria página.** **Preencher é do
     atendimento, não meu.**
334. **⚠ Não mapeei a área da fonte para a grade das 14 canônicas.** `Merchandising` e
     `Curadoria` **não são** áreas canônicas — e na NK STORE **não são apelido: são etapas do
     processo com dono.** **Decisão sua.**
335. **🚨 A credencial de produção da NK STORE (Linx) está em TEXTO CLARO na página do cliente**,
     no toggle `Documentos › Conexão com Linx`: usuário, senha, IP, porta e nome do banco.
     **Agora sei exatamente onde mora. Não reproduzi o valor em lugar nenhum.**
     **A rotação segue sendo a pendência mais urgente do projeto.**
336. **🔴 Há CPF e telefone pessoal de dois representantes legais na mesma página.** Pela política
     do `AGORA.md` § 8.1 **nada entrou no corpus** — a ficha registra que existe e onde.
337. **🆕 `uBuy` é um produto vivo que não está em NENHUMA das duas listas** — nem nos 7
     `Módulos Contratados`, nem nas 16 Soluções. Osklen: *"uBuy: fup — início: Janeiro 2026"*.
     NK STORE: *"Follow Up de Entregas → Pedidos de Compras → uBuy (oportunidade)"*.
     ⚠ **Trata do tema do `FornecAI`, que o corpus registra como "ainda não nasceu".
     Não afirmo que são o mesmo — afirmo que o portfólio de 16 está incompleto.**
338. **🔴 SEXTA evidência do `15_Producao-Interna` (item 234): `Oficina`.** O processo declarado
     da NK STORE é `Planejamento → Estilo → Compras/Merchandising → PCP → Oficina`, com
     `Curadoria` em paralelo. A fonte diz *"a oficina **interna**... corte, costura e
     acabamento"*, coordenando com **facções externas**.
339. **🆕 Existe medição de CSat por cliente e nunca foi varrida** — `Pesquisa de Satisfação do
     treinamento` e `Pesquisa Satisfação Kick Off Osklen` (base inline na página da Osklen).
340. **⚠ O protocolo de varredura precisa mandar PROCURAR SEGREDO em toda página de cliente
     aberta.** A segunda página que abri tinha uma credencial de produção. **Varrer página é
     varrer risco.**

## Diário de bordo por cliente, e o tier T0/T1/T2 (22 set 2026)

341. **🟢 FEITO — cada cliente tem UM arquivo com suas dúvidas, discrepâncias e riscos, e com o
     registro de onde já se varreu.** `_Clientes/<Cliente>/00_Institucional/_contexto/`
     `_pendencias-e-fontes.md`, **48 de 48**. Cobrança do Vinicius: *"registre todos os locais de
     onde já vasculhou pra evitar ficar repetindo buscas... perda de tempo e de token."*
     **Existe porque a memória da conversa compacta e a do disco não.**
     🔴 **Ler antes de varrer qualquer cliente. É a trava contra repetir busca.**
342. **🟢 FEITO — o tier de sensibilidade passa a ser `T0`/`T1`/`T2`**, o vocabulário que o João
     já usa, com a definição operacional do item 96. **Aposentei `INTERNAL_ONLY` e
     `NEVER_TO_THIRD_PARTY`: eram uma segunda taxonomia para a mesma coisa.**
     ⚠ **Adotei o rótulo, não o mecanismo** — a restrição de não copiar do vault continua.
343. **🔺 CORREÇÃO — não existe "o template de pessoa da página do cliente".** O registro (h)
     concluiu isso de **dois** casos (Osklen, NK STORE). **A Reserva não tem o toggle `Pessoas`:**
     as pessoas dela aparecem soltas, dentro dos nomes dos grupos de WhatsApp.
     **Dois é hipótese, três é padrão — e o terceiro desmentiu.**
344. **🔺 CORREÇÃO — gerei as fichas de ferramenta de DOIS enums e o corpus já tinha um terceiro.**
     O `_espec-pessoas-e-comunicacoes.md` já trazia o enum `tool`: `Notion` · `WhatsApp` · `Gist` ·
     `Miro` · `Kanbanize` · `Google Drive` · `YouTube`. **Não apliquei a regra que eu mesmo tinha
     acabado de escrever, no lugar onde ela já valia.** **Corrigido: 16 → 23 fichas.**
345. **🔴 ACHADO — `umode.kanbanize.com` é uma fonte de demanda inteira, jamais tocada.**
     A página da Reserva cita **boards 6 e 18, com 7 cartões por ID** (2 fechados, 5 abertos).
     **As 999 demandas do corpus vêm só da base do Notion. Não sei quanto se sobrepõem.**
     **Preciso de acesso ao Kanbanize.**
346. **🔴 A cadência de `Review Quinzenal de Projeto` da Reserva parou.** Envios marcados até
     **30/06**; **15/07, 02/08 e 21/08 sem marca**. Responsável declarado: **João**.
     Destinatária: **Claudinha**.
347. **🔴 5 dos 9 grupos de WhatsApp da Reserva estão marcados para EXCLUIR e continuam
     existindo.** A decisão 🟢manter/🔴excluir está escrita na própria página.
348. **🆕 Fonte de demanda não é uma só.** Notion, **Kanbanize**, **Gist** (chat da plataforma),
     **WhatsApp** e **formulário** coexistem — a Reserva declara formulário para demanda nova e
     Gist para dúvida de usabilidade, com média de **1 chamado/dia e 2 reuniões/semana**.
     **Nenhuma varredura anterior sabia disso.**
349. **⚠ `uBuy` apareceu no TERCEIRO cliente** (Reserva: *DE/PARA Campos uBuy*, *Ficha de Pedido
     uBuy*), junto com **`uPlan`**. **Um caso é anedota, dois é hipótese, três é padrão: `uBuy`
     é produto vivo e o portfólio de 16 está incompleto.**

## O caminho das perguntas, e o Kanbanize fechado (22 set 2026)

350. **🟢 DECIDIDO — o Kanbanize NÃO se varre.** Vinicius, textual: *"ferramenta que não é usada
     há tempos. Então zero foco nisso."* `[D]` **Fecha o item 345.**
     ⚠ **Consequência que fica:** a página da Reserva cita 7 cartões do `umode.kanbanize.com`
     como se fossem fila viva. **Ela está desatualizada nesse ponto** — e isso vale como aviso
     para toda página de cliente: **o que a página diz é o que alguém escreveu um dia**, não
     necessariamente o que vale hoje.
351. **🟢 RESPONDIDA — `Status` × `Etapa`: não há regra geral.** Vinicius, textual: *"a verdade
     é que não sei. Nós vamos ter que ver caso a caso e esse levantamento por cliente será
     excelente pra depois juntarmos com 'negócios'."* `[D]`
     **A pergunta transversal vira pergunta POR CLIENTE** — e é exatamente para isso que a
     § 2.1 do `_pendencias-e-fontes.md` serve.
352. **🟢 DECIDIDO E REGISTRADO — o que só o Vinicius responde tem UM caminho.**
     Ele, textual: *"em dado momento, você montará uma lista de coisas que eu tenho que perguntar
     e vou dar um jeito de responder ou por áudio ou numa transcrição de reunião mesmo... Garanta
     que essa decisão esteja registrada nas documentações de forma que você nunca se esqueça de
     que existe esse caminho. Não adianta aplicar agora e depois criar outras formas de fazer a
     mesma coisa ou até passar sem executar esse comando padronizado."* `[D]`
     **Implementado em três peças que se amarram:**
     **(a)** a pergunta nasce na **§ 2.1** do `_pendencias-e-fontes.md` do cliente;
     **(b)** é colhida para `_perguntas-para-o-vinicius.md` **pelo MESMO script** que escreve as
     48 — não existe um segundo jeito de montar a lista, nem como rodar um sem o outro;
     **(c)** o processo está no `protocolo-perguntas-ao-vinicius.md`, citado no `START.md` § 1
     (classes P e X) e no `AGORA.md` § 8.0.
     🔴 **A regra que decide o que é pergunta:** só entra o que **nenhuma fonte** responde.
     Dúvida que uma fonte responde **não é pergunta — é varredura que falta fazer**, e vai para a
     § 4. **Transformar em pergunta o que está a uma leitura de distância é empurrar trabalho meu
     para ele** — é o erro que o `CLAUDE.md` já nomeia.
     ⚠ **Quando levar a lista até ele não é decisão minha:** *"pensaremos nisso quando chegar o
     momento."* **Minha obrigação é manter a fila pronta e avisar se ela travar a varredura.**
353. **Fila hoje: 15 perguntas de cliente + 4 transversais abertas, 1 respondida.**
     ⚠ **A fila está curta porque a varredura está no começo** — **44 dos 48 clientes têm a
     página fechada.** **Pergunta boa nasce de varredura feita.**
354. **🔺 BUG MEU, do pior tipo — falha em silêncio.** O gerador usava `Mondepars` (grafia do
     Notion) como chave, e a pasta é `Mondpars`. **O arquivo saiu completo e errado, sem um
     aviso.** **Corrigido na causa, não no caso:** o script agora **aborta com erro** se
     qualquer chave de `PAGINA`, `PEND`, `RISCO` ou `PERGUNTAS` não casar com uma pasta real.
     **Silêncio é pior que erro** — erro eu vejo.
355. **🔴 ACHADO — `Simples (by Reserva)` é pasta de cliente nossa SEM nenhuma linha na base
     `Mapa de Clientes`.** É a única nessa condição (a `Mondpars` é só grafia).
     **É marca dentro da Reserva, ou conta própria que falta cadastrar?**
     **Define se são 48 ou 49 clientes.** → pergunta registrada.

## Varredura de páginas de cliente — VIX (22 set 2026)

356. **🟢 DECIDIDO — `Mondepars` é o nome certo.** Vinicius, textual: *"o nome certo da empresa
     é Mondepars."* `[D]` **Pasta renomeada** de `Mondpars` para `Mondepars`, e a grafia
     propagada nos 17 arquivos do cliente e na lista de clientes reais.
     ⚠ **O CRM segue com a grafia errada** — quem ler lá vai achar `Mondpars`.
357. **🟢 DECIDIDO — `Simples (by Reserva)` NÃO é cliente.** Vinicius, textual: *"é marca de
     dentro da Reserva... a nível de contratação imagino que seja RESERVA mesmo."* `[D]`
     **A carteira tem 48 clientes, não 49.**
     ⚠ **Fica um ponto aberto que ele mesmo levantou:** pode haver **separação própria de
     usuários e permissões** na plataforma, ainda que a contratação seja da Reserva.
     🔴 **Apagar ou fundir a pasta é decisão dele — eu não apago pasta de cliente.**
358. **🔺 A hipótese de que a estrutura da página segue quem atende é FALSA.** VIX e NK STORE
     têm **a mesma atendente** (`Julianne + Pedro`) e páginas **completamente diferentes**.
     **Quatro páginas abertas, três estruturas:** Osklen e NK STORE compartilham o toggle
     `Pessoas`; Reserva e VIX não têm nada parecido. **Só abrindo se sabe.**
359. **🔴 A VIX tem 17 perfis de usuário, e eles SÃO áreas** — `Vix-Admin` · `Vix-CAD` ·
     `Vix-Compras` · `Vix-Desenvolvimento` · `Vix-Estamparia` · `Vix-PCP` · `Vix-Ficha Tecnica` ·
     `Vix-Produto TP` · `Vix-Tabela` · `Vix-Qualidade` · `Vix-Demo` · `uDash` **e CINCO só de
     Estilo**: `Biquini`, `Cover ups`, `PA`, `Roupas`, `Admin`.
     **Confirma o item 'perfil = área' do registro (e) — e mostra que a granularidade real é de
     SUBÁREA, não de área.** **Vira subárea canônica, ou fica só como perfil da plataforma?**
360. **🔴 A matriz de permissão da VIX tem ~60 funções × 17 perfis, é mantida À MÃO numa tabela
     do Notion, e a última edição é de 09/07/2025.** ⚠ **Não sei se ainda reflete a plataforma**
     — se não reflete, copiá-la seria copiar ficção.
361. **🔴 `Manual` e `Base de Importação` estão bloqueados para os 17 perfis da VIX.**
     **Ninguém na VIX acessa o manual.** ⚠ **Conecta com a dor da CAEDU**, que registra que o
     manual de instruções não foi suficiente. **Dois casos: é hipótese, não padrão ainda.**
362. **🆕 `uPick` — quarto nome de produto fora das duas listas** (sub-página `uPick Vix - Passo
     a passo`), junto de `uBuy` e `uPlan`. **O portfólio de 16 está incompleto, e agora são
     três nomes ausentes.**
363. **⚠ `uDash` é PERFIL de usuário na matriz da VIX e também nome de produto legado.**
     **Dois sentidos para a mesma palavra** — mesma armadilha já registrada de `collection`
     (banco) × coleção (moda).
364. **🆕 A VIX tem a primeira tabela DE/PARA de integração campo a campo que o corpus vê**
     (31/07/2025): campo uMode → campo Linx, com tabela e tipo
     (`referenciabr` → `MODELISTA` varchar(25) em `PRODUTOS`). **Vale replicar como padrão de
     documentação de integração.**
365. **🆕 A página da VIX registra um aprendizado de atendimento:** usuário sem permissão de
     deletar variante deve pedir internamente a quem tem. **Explica uma classe inteira de
     demanda que hoje chega como chamado.**

## Varredura — Lofty Style e Puket (22 set 2026)

366. **🚨 A credencial do site de documentação da Lofty Style está EM TEXTO CLARO na página do
     cliente**, no toggle `Documentação/Regras`, ao lado da URL `docs.umode.app/integracao-lofty`.
     **Agora sei o lugar exato das DUAS credenciais expostas.** O valor não foi replicado em
     lugar nenhum. 🚨 **A rotação segue sendo ação sua.**
367. **🔴 TERCEIRO caso da dor de excluir/inativar variante — vira PADRÃO.**
     **VIX** (aprendizado de permissão na página), **Reserva** (cartão antigo) e **Lofty Style**
     (`Exclusão de Variante após integração`). **Um caso é anedota, dois é hipótese, três é
     padrão: é lacuna da plataforma, não pedido de cliente.**
368. **🟢 ACHADO GRANDE — a página da Puket tem uma TABELA DE USUÁRIOS com 43 pessoas**, e cada
     linha traz **nome · e-mail corporativo · perfil de acesso · ativo desde**.
     **A Puket tinha 3 fichas, vindas só das demandas. Agora tem 43.**
     🟢 **É a fonte de pessoa mais completa que o corpus já viu** — e a única que dá
     **data de ativação por pessoa** e **chave de identidade**.
369. **`[P]` DECISÃO DE TIER QUE É MINHA e precisa do seu aval: e-mail CORPORATIVO é `T2` e
     entra.** É dado de contato de trabalho e é a chave que destrava o item 252 (identidade de
     pessoa). **E-mail pessoal segue `T0`. Telefone e CPF seguem `T0` sempre.**
     **Precedente que já existia:** há ficha nomeada por e-mail na Reserva desde antes desta sessão.
370. **🔴 A Puket é do GRUPO ÚNICO, e gente do grupo opera dentro da conta do cliente.**
     Dois domínios na mesma tabela: `@puket.com.br` e `@grupounico.com`, mais um `@grupounico.hk`
     (Hong Kong). 🔴 **O corpus não tem modelo para grupo econômico** — nem para pessoa que
     pertence ao grupo e atua no cliente.
371. **🔴 A pessoa mais antiga da Puket está ativa desde 24/05/2022 e o campo `Data Ativação
     Cliente` da base está VAZIO.** **A tabela de usuários sabe o que a base não sabe.**
372. **🔴 12 perfis de acesso da Puket, e 6 não têm área canônica:** `BI` · `TEX` ·
     `Certificação` · `Controladoria` · `Importação` · `Projetos`.
     Somados a `Merchandising`, `Curadoria`, `Oficina`, `facção` e aos 17 perfis da VIX,
     **a grade de 14 áreas está sendo contrariada por praticamente todo cliente que abro.**
373. **⚠ A Puket tem 43 usuários ativos e só 2 módulos contratados** — o menor entre os
     `Ongoing`. **Muita gente para pouco módulo:** é oportunidade comercial ou erro de cadastro.
374. **⚠ O toggle `Pessoas` da Lofty Style existe e está VAZIO** — segundo caso, junto da Osklen.
     **De 3 clientes que têm o toggle, 1 preencheu.**
375. **🆕 Fontes novas que ninguém varreu:** playlist de **treinamento no YouTube** (Puket) ·
     **4 pesquisas de CSat** (Osklen ×2, Lofty Style ×2) · `Passada de bastão Puket`, o único
     documento de handover de atendimento da carteira · `NCM e Código CEST` (Lofty), tema fiscal
     que nenhuma das 14 áreas cobre.
376. **⚠ A cadência de report ao cliente parou em DOIS clientes:** Reserva (`Review Quinzenal`,
     última marca em 30/06) e Lofty Style (`Atualização de Projeto`, última em 29/01/2026).
     **Dois casos: é hipótese, ainda não padrão.**
377. **🆕 Tipos de entidade que ainda vão chegar**, avisados pelo Vinicius em 22 set 2026:
     **mentorado** e **cliente de serviço de educação em IA**, além da lista de clientes com as
     plataformas que contratam. 🔴 **Cada um vira arquivo com nó, no mesmo padrão** — e a
     varredura de ferramenta já preparou o eixo `contrata`.

## Varredura — NV e Oficina Reserva (22 set 2026)

378. **🔴 GRUPO ECONÔMICO não está modelado, e já apareceram DOIS.**
     **Grupo Único** — a Puket tem gente com e-mail `@grupounico.com` operando dentro da conta.
     **Grupo AR&CO** — o João escreveu em 26/06/2024 que a Oficina Reserva *"entrará no mesmo
     pacote do Grupo"*, e a dor nº 1 dela cita **dependência do time da AREZZO**.
     🔴 **Reserva, Oficina Reserva, Simples (by Reserva) e Arezzo são quatro pastas isoladas
     para o que pode ser um contrato só.** **O isolamento de cliente é regra travada, e grupo
     econômico a atravessa.** → pergunta registrada.
379. **🔴 `Qualitá` — um TERCEIRO que não é cliente nem fornecedor de material.** Faz inspeção
     de qualidade para a Oficina Reserva, **todo o processo por WhatsApp**, e a fonte registra:
     *"o inspetor chega para auditar e não tem o documento"*.
     🔴 **O corpus não tem modelo para terceiro.** → pergunta registrada.
380. **🔴 QUARTO e QUINTO caso da dor de variante** — a NV tem `Manual de descancelamento de
     produtos e variantes` **e** `NV | Variantes Canceladas Inativas`. Com VIX, Reserva e Lofty
     Style são **quatro clientes**. **Não é mais hipótese: é lacuna da plataforma.**
381. **🔴 SÉTIMA evidência do `15_Producao-Interna`: `Atelier`**, na lista de departamentos
     engajados da NV — depois de `Oficina` (NK STORE) e `facção` (vários).
382. **🟢 O bloco `Marca:` é um TEMPLATE de perfil de conta que existe em vários clientes** —
     linha de produção, submarcas, segmento, ERP, integração ativa, usuários ativos,
     departamentos engajados. **Na NV está preenchido; na Puket, vazio.**
383. **🔴 A NV declara 61 usuários ativos e o corpus tem 13 fichas.** **O número se sabe, os
     nomes não** — a NV **não** tem a tabela de usuários que a Puket tem.
384. **🔴 10 departamentos engajados na NV, e quatro sem área canônica:** `Engenharia de
     Produto` · `Planejamento Comercial` · `Cadastro/Planners` · `Atacado` · `Atelier`.
385. **🟢 A página da Oficina Reserva tem o mapeamento de dores mais completo da carteira**,
     escrito pelo João no grupo de Sales em **26/06/2024**: cadastro inteiramente no SAP com
     muitas etapas entre SAP e Linx, uma só pessoa dedicada ao cadastro, ausência de governança,
     **400 SKUs por coleção** e **90% do tempo dedicado ao SAP**.
     **São os primeiros números de operação de cliente que o corpus vê.**
386. **🔴 A fonte registra dano reputacional, textual:** *"má reputação entre os Fornecedores e
     Qualitá por não usarem uMode"*. **É o argumento comercial mais forte da carteira — e está
     enterrado numa mensagem de grupo de 2024.**
387. **⚠ A meta declarada da Oficina Reserva era rodar no uMode em 6 meses, a contar de
     jul/2024. Hoje são 26 meses.** ⚠ **Não sei se foi cumprida — nada na página diz.**
388. **⚠ `Perfil de Usuário e Permissionamentos` é sub-página de TRÊS clientes** (VIX, Lofty
     Style, Oficina Reserva) e só a da VIX foi aberta. **É onde o vínculo pessoa↔área mora.**

## Varredura — Cambos (22 set 2026)

389. **🟢 Bloco `Pessoas` PREENCHIDO — segundo caso da carteira**, junto da NK STORE.
     Tony Stefan Lopes (Gerente Geral / Diretor de Operação da Fábrica) · Valter (Head
     Financeiro) · Fabiane Sayuri (Resp. Desenvolvimento de Produtos) · Carolina (Estilista) ·
     Gustavo Paiva (Head de Tecnologia). **De 5 clientes com o bloco, 2 preencheram.**
390. **🟢 RESOLVIDA a ambiguidade `Fabi e Carol`** — a célula da base de demandas que eu me
     recusei a desmembrar por não poder inventar. A página diz que o líder do projeto é
     *"Tony e Fabi"* e lista **Fabiane Sayuri** e **Carolina**.
     **Ambiguidade resolvida com fonte, não com palpite — que era exatamente o ponto.**
391. **🔴 A Cambos FORNECE para a CAEDU, e as duas são clientes da uMode.** Textual:
     *"Fornecem para Caedu, Marisa, etc."* 🔴 **Dois clientes nossos numa relação
     fornecedor-cliente entre si, e o corpus os trata como ilhas.**
     **O isolamento de cliente é regra travada — e esta relação a atravessa.**
392. **🔴 A base diz que o ERP da Cambos é `SPI - Sistema próprio` e a página diz DOIS:**
     `Totvs - Virtual Age` (comercial, **com pacote de APIs**) e `SPI` (produção), mais
     `Banner` para pedido de atacado. **A base está incompleta.**
393. **🔴 Relação contratual ambígua, registrada pela própria uMode:** *"Relatórios: não
     detalhados no contrato porém subentendido entre 2-3 relatórios mediante a maturidade."*
     **Escopo subentendido é escopo em disputa.**
394. **🔴 Atrito interno Sales × Ops registrado**, feedback do Sandro: *"alinhar o que vendeu e
     o que operação vai tocar gerou desconforto... pode dar impressão que a empresa está
     desalinhada."* **É o único registro de atrito interno que o corpus tem.**
395. **🆕 Números de operação da Cambos:** 140.000 peças/mês · 20 a 40 fornecedores ·
     ~20 pessoas no desenvolvimento · **nota 6,0** para o processo atual · **10% de quebra de
     entrega** · 40% Magazine / 60% marca própria. **Segundo cliente com números**, depois da
     Oficina Reserva. ⚠ **~20 pessoas no desenvolvimento e o corpus tem 5 fichas.**
396. **🆕 `Trello` — nona ferramenta, e é DO CLIENTE.** Não estava no enum `tool` do corpus.
     **Ficha criada, marcada como ferramenta do cliente, não da uMode.**
397. **🆕 `IPSP` — quinto nome de produto fora das duas listas**, com `uBuy`, `uPlan` e `uPick`.
398. **🆕 Segundo escopo desejado e NÃO contratado:** *"trazer os clientes para dentro da
     plataforma para acompanhar o desenvolvimento"*. **Oportunidade comercial nomeada, parada
     desde o kick off.**
399. **🆕 `Playbook Cambos | Treinamento > IA + Doc Laura`** — primeira documentação homologada
     com IA que o corpus vê.

## Varredura — Luiza Barcelos (22 set 2026)

400. **🔺 A CORREÇÃO fica ainda mais forte: eu disse que a Luiza Barcelos era "quase invisível".
     É a conta MAIS bem documentada que abri.** Eu media pela base de chamados, janela de 24 dias.
     **A página tem 15 pessoas com cargo, discovery de Sales, 8 páginas de regra datadas e um
     relatório de incidente.** **Medir pela fonte errada não subestima um pouco — inverte.**
401. **🔴 O processo está na cabeça de UMA pessoa, e a própria uMode escreveu isso:**
     *"Processo está na cabeça da Marcinha (Luiza Barcelos) → Missão é tirar as informações da
     cabeça dela e colocar na ferramenta."* **É risco de pessoa-chave nomeado — e a pessoa é a
     dona da marca, Diretora Criativa.**
402. **🔴 `6 PRIMEIROS MESES PARA MOSTRAR CREDIBILIDADE DA UMODE`** — escrito em vermelho no
     kick off interno de **06/06/2024**. E: *"o time da Luiza tem trauma de cronograma e entrega
     por frustrações passadas com a Linx."* **Hoje são 27 meses.**
403. **🔴 DUAS datas de ativação que não batem:** a página diz *"Data de Ativação por Vendas —
     15/05/24"* e o campo da base diz **07/06/2024**. **Um mês de diferença.**
404. **🔴 Existe um `Relatório de Incidente | Weekly Luiza Barcelos <> uMode — 2025/08/08`.**
     **É o único registro de incidente com cliente que o corpus conhece, e eu não o abri.**
     **Prioridade de leitura.**
405. **🟢 O escopo contratual da Luiza Barcelos é EXPLÍCITO, ao contrário do da Cambos:**
     *"não faz parte do escopo deste contrato a integração com o sistema LINX ou qualquer outro
     que não seja o SAFETECH"*, e **três relatórios nomeados** — grade, status, acompanhamento.
     **É o modelo de como escrever escopo. A Cambos é o contra-exemplo.**
406. **🔴 `uDash` é PRODUTO CONTRATADO aqui** — *"13 usuários uFlow / 2 usuários uDash"*.
     Na VIX ele aparece como **perfil de acesso**. **Confirma os dois sentidos da mesma palavra,
     e agora com evidência dos dois lados.**
407. **🔴 Duas listas de times que não batem, na mesma página:** o kick off interno diz
     *Estilo, PCP, Compras*; a seção `Times Envolvidos` diz **oito** — Diretoria Criativa,
     Estilo, Desenvolvimento, Produto e Merchandising, Suprimentos, Operações (Cadastro e
     Precificação), Estratégia/Processos/Projetos e Tecnologia.
408. **🆕 `HubSpot` — décima ferramenta, e é o CRM da uMode.** A página tem link direto para o
     *deal* da conta. **Não estava no enum `tool`, e é onde vive o lado comercial da relação.**
     ⚠ **Nunca varrido.**
409. **🆕 8 páginas de regra datadas** — `Regra do Campo Linha` · `Regra Família 05/08/25` ·
     `Automações da Aba Etapa & Datas 24/09/2025` · `Regras do WorkFlow 12/11` ·
     `Importação das Listas 24/01`. **É a documentação de regra mais disciplinada da carteira.**
410. **⚠ Dois nomes não batem com o próprio e-mail ou consigo mesmos:** `Gabriel Jaques` ×
     `gabriel.silva@`, e `Eduardo Britto` × `Eduardo Brito` **na mesma página**.
     **Não escolhi nenhuma grafia.**
411. **🔴 18 blocos da página não abriram por este conector** — e estão justamente dentro de
     `Diretores e Representantes Legais` e `Responsáveis pelo Projeto`.
     **Há mais pessoas ali do que as 15 que consegui ler.**
412. **🔺 BUG MEU, corrigido: o gerador de fichas só processava cliente que tinha tabela de
     solicitante de demanda.** A Luiza Barcelos, com 15 pessoas com cargo na página, ficava de
     fora. **Fonte nova não pode depender da fonte antiga.** Corrigido.

## Os uModers que saíram, e o bloco que o conector não lê (22 set 2026)

413. **🟢 DECIDIDO — quatro uModers não estão mais na uMode.** Vinicius, textual:
     *"Dalker Walter (Diretor de Operações), Rafael Renaldim (Gerente de Experiência do Cliente),
     Tais Moser (Customer Success) e Saulo (CTO) não estão mais na uMode."* `[D]`
     **Rafael tinha ficha — `Status na uMode` atualizado. Dalker, Tais e Saulo não tinham —
     fichas criadas, já marcadas como saída.** ⚠ **Data de saída de nenhum deles é conhecida.**
414. **🟢 DECIDIDO E REGISTRADO — o `HOJE` dos uModers é passo de FECHAMENTO, não de caminho.**
     Vinicius: *"os cargos dos demais também terão atualizações. Isso vai ser uma coisa
     recorrente e que teremos que corrigir somente ao final de toda a varredura: como é o HOJE
     dos uModers."* `[D]`
     **Implementado em dois lugares:** `AGORA.md` § 7 item 9 e `protocolo-varredura-cliente.md`
     § 10. 🔴 **A regra que vale até lá: cargo lido em ata é cargo NAQUELA DATA, nunca de hoje.**
     **Corrigir aos pedaços cria versões parciais conflitantes** — o mesmo defeito que o campo
     `Status` de cliente já tem.
415. **🔺 ERRO DE DIAGNÓSTICO MEU: eu disse que 17 blocos não abriram por falta de acesso.
     Não era acesso.** A página abre inteira. **Os blocos são um tipo que este conector não
     renderiza** — eram **linhas de contato**: telefone, e-mail, CPF e cargo.
     **Eu quase pedi ao Vinicius uma liberação que não resolveria nada.**
     **Virou a § 11 do `protocolo-varredura-cliente.md`:** antes de falar em permissão, puxar a
     página-fonte direto; se abrir, não é acesso.
416. **🟢 O contorno funciona, e é barato: o Vinicius copiou e colou o trecho.**
     **O que veio assim entra como fonte normal, com procedência e data.**
417. **🆕 Pessoas que só existiam nos blocos ilegíveis:**
     **`Luiz Raul Aleixo Barcelos` — Diretor / Representante Legal**, o único nomeado da conta ·
     **`Samuel Correa` — Gerente de Inovação e Tecnologia** (o cargo estava `[a preencher]`) ·
     e-mail corporativo de **Ana Lucia Andrade**, **Gustavo Gabriel Santos Sobrinho** e
     **Gabriel Jaques da Silva**.
418. **⚠ O e-mail do Representante Legal é o mesmo do campo `Email Principal Financeiro` da
     base** (`luiz@luizabarcelos.com.br`). **O contato financeiro da conta é o dono.**
419. **⚠ A Luiza Barcelos tem DUAS pessoas em Tecnologia** — Eduardo Britto (Coordenador de
     Sistemas e Tecnologia) e Samuel Correa (Gerente de Inovação e Tecnologia).
     **O toggle prevê um `Responsável Tecnologia`; a realidade tem dois.**
420. **⚠ CONFIRMADO na fonte original: a ata diz "equipe da Emoji" duas vezes** onde deveria
     dizer uMode. **É ata gerada por IA com erro de transcrição, e está viva no Notion.**
     Também: `Tais` e `Thaís` na mesma ata. **Nenhuma das duas foi corrigida por mim** — a fonte
     é o que é.
421. **🔺 BUG MEU, corrigido: `NOTA_PAGINA` existia no gerador e NUNCA era lida.** Eu escrevi
     observações de pessoa que não chegavam a arquivo nenhum. **Mesma classe do bug da chave sem
     pasta: perda silenciosa.** **Corrigido na causa** — o script agora **aborta** se uma nota
     não casar com ficha nenhuma.

## Travas de erro e a via do Chrome (22 set 2026)

422. **🔺 RESPOSTA HONESTA à pergunta "isso tudo está integrado pra nunca mais errar?": NÃO
     estava, para metade.** Auditei os 10 erros desta sessão. **Registrar um erro numa pendência
     é memória, não impedimento.** Placar real, agora na **§ 12 do
     `protocolo-varredura-cliente.md`**, citada pelo `START.md`:
     🟢 **3 abortam** (chave sem pasta · nota órfã · arquivo fora do manifesto) ·
     🟡 **4 avisam ou ficam visíveis** (filtro de pessoa · padrão de MD · bloco ilegível ·
     página não aberta) · 🔴 **3 não têm mecanismo nenhum** e dependem de eu lembrar:
     **concluir padrão com dois casos** · **não usar enum que o corpus já tinha** ·
     **fonte nova dependendo da fonte antiga**.
     **Não afirmo que as três vermelhas estão resolvidas — dependem de julgamento.**
423. **🟢 NOVA TRAVA — o filtro de pessoa agora IMPRIME todo nome que descarta, com o motivo.**
     Era assim que o `Hermes` sumia. **Descarte silencioso virou descarte visível.**
     ⚠ **No primeiro uso, descartou 1 nome:** `Conrrado e Ingrid` — duas pessoas na mesma célula,
     descarte legítimo.
424. **🟢 NOVA SEÇÃO EM TODOS OS 48 CLIENTES: `§ 1-bis · O que eu NÃO consegui ler`.**
     Pedido do Vinicius, textual: *"sobre suspeitas de blocos, sempre tenha atenção e me indique,
     porque temos que ter a garantia de que tudo que está varrendo está conseguindo tirar
     proveito de tudo o que podemos."* `[D]`
     🔴 **Bloco que não renderiza NÃO é bloco vazio** — na Luiza Barcelos, 17 blocos ilegíveis
     escondiam o único Representante Legal da conta.
     **Três tipos de perda já catalogados:** bloco não renderizado (resolvido por copiar/colar) ·
     **incorporação do Drive** (`Plano de Sucesso do Cliente` em 3 clientes, aberto) ·
     **404 real** (`Fornecedores da Caedu`, o único caso de permissão de verdade).
425. **🟢 CRIADO — `prompt-extracao-notion-via-chrome.md`, classe `TEMPLATE`.**
     Ideia do Vinicius: *"se precisar montar um prompt para, via Claude Chrome, indicar todos os
     caminhos que precisa, com as instruções de abrir todos os blocos que forem possíveis, para
     então gerar arquivos md de cada caminho, organizar por cliente, zipar tudo e depois te
     trazer — sem problemas... Só não quero que tenhamos a sensação de não ter algum tipo de
     informação num destino e na verdade ele estar por lá."* `[D]`
     **Traz as 50 URLs de cliente, ordenadas por quem está vivo primeiro**, instrução de expandir
     todo toggle, synced block e database inline, convenção de nome de arquivo para eu ingerir
     sem ambiguidade, e a regra de **escrever `[NAO-ABRIU]` no lugar do bloco em vez de pular em
     silêncio** — porque bloco que não abriu é informação.
426. **🔴 O zip que voltar é `T0` enquanto existir.** Ele vai trazer a credencial da NK STORE, a
     senha da Lofty Style e CPF/telefone de representantes legais.
     **Não versionar, não subir ao Drive compartilhado: descompactar no `scratchpad`, extrair só
     o que é `T2`, e apagar.**

## Varredura — Moda Objetiva, Baw e Loungerie (22 set 2026)

427. **🔴🔴 A DOR DA CAEDU ESTÁ RESOLVIDA NA PÁGINA DA LOUNGERIE.** A hierarquia
     `Griffe › Linha › Grupo › Subgrupo`, que a CAEDU pede desde a weekly de **16/09/2025** e que
     reaparece idêntica em jul e ago/2026, **está na página da Loungerie com os 4 níveis
     nomeados, definidos, exemplificados — e com a alternativa de extensibilidade já sugerida
     pela própria uMode** (*"criar no 1º nível 'OUTRAS OCASIÕES' ou 'NOVAS CATEGORIAS'… vantagem:
     garantir posições para alocar novas Categorias que venham a surgir"*).
     **Registro em `_varredura-2026-09-22j`.**
     ⚠ **O que isso NÃO resolve:** a dor da CAEDU é de **integração**, não de taxonomia — a frase
     dela é sobre a API estar do lado do cliente. **A Loungerie resolve o modelo; a CAEDU trava
     no lado técnico.** E os níveis são os mesmos, **os valores não**.
     🔴 **A pergunta que fica não é de taxonomia, é de circulação de conhecimento: por que o
     desenho feito para uma conta não chegou na outra?** → pergunta registrada.
428. **🟢 Moda Objetiva é o TERCEIRO cliente com o bloco `Pessoas` preenchido** (com NK STORE e
     Cambos) — 6 pessoas. **E tem um bloco `Stakeholders` que NENHUM outro cliente tem:**
     os outros têm quatro blocos, este tem cinco. **Confirma de novo: o template de pessoa não é
     fixo.** ⚠ **`Paula — Cadastro ERP Ilimitar`: o papel dela é literalmente operar o ERP.**
429. **🔴 Quatro toggles da Moda Objetiva têm título e nenhum conteúdo:** `Dores Mapeadas na
     Imersão` · `Plano de Sucesso do Cliente - OKRs` · `Reunião de Warm Up e Kick Off` ·
     `CRM → Anotações Gerais`. **Estrutura criada, nunca preenchida.**
430. **🔴 `Negociação pós AR&CO | 23/01/25` — a Baw é o TERCEIRO cliente ligado ao Grupo AR&CO**,
     com Reserva e Oficina Reserva (e Arezzo citada na dor da Oficina).
     ⚠ **Pode explicar por que a Baw está `Sem CS` com 4 módulos: entrou pelo pacote do grupo.**
     **O tema grupo econômico já tem dois grupos e cinco contas.**
431. **🆕 `[BAW] Contrato 2025` — primeiro documento de contrato nomeado da carteira.**
     🔴 **Não abri; quando abrir, o conteúdo é `T1`.**
432. **⚠ A Baw tem QUATRO páginas `Perfil de Acesso`**, uma delas duplicata explícita `(1)` e
     duas por área (`Estilo`, `Engenharia/Compras`). **Mesmo padrão de duplicata `(1)` da
     Osklen.** **Dois casos: é hipótese de higiene de página.**
433. **🆕 `Consultoria de Planejamento` (Loungerie) — é SERVIÇO, não módulo**, e não está nos 7
     módulos nem nas 16 Soluções. **Sexto nome de oferta fora das listas**, com `uBuy`, `uPlan`,
     `uPick`, `IPSP` e `uDash`. 🔴 **O portfólio declarado não descreve o que a uMode vende.**
434. **🆕 `Tactiq` — décima primeira ferramenta, e tem histórico PRÓPRIO fora do Notion.**
     As 7 transcrições da CAEDU são dela, e a Loungerie tem link vivo para um transcript.
     🔴 **É onde vive a fala real das reuniões, e nunca foi varrido.**
435. **🆕 A Loungerie tem os dois rituais de cliente mais bem descritos do corpus:**
     **`Ata da Carteira`** (Compras + Planejamento + Alocação + Logística, pedido a pedido,
     revendo data de lançamento quando há risco) e **`FUP`** (Time & Action com fornecedor:
     amostra, aprovação de cor, 1º fit, 2º fit, PP, peça de marketing).
436. **🔴 `Alocação` e `Inteligência Comercial` não existem na grade de 14 áreas.**
     Somam-se a Merchandising, Curadoria, Oficina, Atelier, BI, TEX, Certificação,
     Controladoria, Importação, Projetos e Atacado. **São treze nomes de área fora da grade,
     vindos de oito clientes diferentes. A grade de 14 não descreve a carteira.**
437. **🆕 Segundo tema fiscal: `IMPORTADO LOUNG`** — tabela de classificação com **HSCODE**,
     composição e medidas, depois do `NCM e Código CEST` da Lofty Style. **Dois casos: hipótese.**
438. **🔴 A Loungerie tem `Status` `Onboarding`, `Etapa` `Pré Onboarding` e `Módulos
     Contratados` VAZIO** — apesar de 5 discoveries gravados e de a fonte citar *"antes do
     fechamento do contrato"*, o que implica contrato fechado.
439. **🆕 A Loungerie é o único cliente com horizonte de coleção declarado:** desenvolvimento
     concentrado no **2º sem/2027**, importados com abastecimento até **abril/2027**.

## As páginas de Perfil de Usuário — dez clientes, duas lidas (22 set 2026)

440. **🔴🔴 ACHEI A CAUSA MECÂNICA DO MEU ERRO COM A LUIZA BARCELOS.** Eu disse que a conta era
     *"quase invisível"* porque quase não aparecia na base de chamados, e depois corrigi dizendo
     que eu media pela fonte errada. **A correção estava certa e incompleta.**
     🔴 **`Fale com o Suporte` está BLOQUEADO para os SEIS perfis da Luiza Barcelos.**
     **Ninguém na conta consegue abrir chamado pela plataforma.** A conta não aparecia
     **porque o caminho está fechado.**
     🔴 **E na VIX o mesmo botão está liberado para os 17 perfis.**
     **Consequência para todo o corpus: volume de chamado não mede atividade de conta — mede
     quem tem o botão.** Toda leitura que fiz por chamado precisa desse asterisco.
441. **🔴 `Fornecedor` É PERFIL DE USUÁRIO com login** — na Luiza Barcelos e na Lenny Niemeyer.
     Vê `Tarefa homepage` e `Tarefa ficha` com edição; `Imagens`, `Versões (variante)` e
     `Grade de Tamanhos` só leitura; **todo o resto bloqueado.**
     🔴 **Responde em parte a pergunta do "terceiro":** na Oficina Reserva a `Qualitá` opera
     **por WhatsApp**; aqui o fornecedor **tem conta, com escopo desenhado**.
     **O modelo existe em dois clientes e não existe no corpus.**
442. **⚠ Duas colunas de TESTE viraram permanentes na matriz da Luiza Barcelos** —
     `Teste LB-Admin 03/01/25` e `Teste LB-Time 07/02/25`, com ✔️ em vez de 🟢/🟡/🔴.
     **E três perguntas do teste ficaram como células:** *"pq no tecido aparece 'incluir nova
     variante' e no aviamento não?"* · *"era bom deixar pra editar pra colocar a corzinha"* ·
     *"✔️ mas só tá vendo lb-admin e lb-time. tem q ver os times"*.
     🔴 **São perguntas de jan/fev 2025 nunca respondidas, dentro do documento que descreve a
     permissão vigente.** Última edição da página: **14/05/2025**.
443. **🔴 O `Manual` e a `Base de Importação` estão bloqueados para TODOS os perfis nos DOIS
     clientes que li** — VIX (17 perfis) e Luiza Barcelos (6). **Dois de dois: hipótese forte.**
     ⚠ **Conecta com a dor da CAEDU** (*"o Manual de Instruções não foi suficiente"*) e com o
     `Manual do Cliente para o Sistema PLM` da uMode, de **24/08/2023**.
     **Se o manual está bloqueado para todo mundo, a pergunta não é se ele é bom.**
444. **🔴 ACHADO ESTRUTURAL — um SEGUNDO acervo de documentação por cliente:**
     `uMode Geral / uFlow / Documentação de Setup - PLM / CLIENTES (Em desenvolvimento)`.
     Achado porque a página de permissionamento da **NV** mora lá, e não no `Mapa de Clientes`.
     **Nenhuma varredura tocou nele.**
445. **🔴 As páginas `Perfil de Usuário e Permissionamentos` existem em DEZ clientes e eu li
     DUAS.** VIX (17 perfis) e Luiza Barcelos (6). Faltam: Cambos (4) · Moda Objetiva (5) ·
     Oficina Reserva (5) · NK STORE (3) · Lenny Niemeyer (3, **com `Fornecedor`**) · Recco (2) ·
     NV (no outro caminho) · Lofty Style.
     ⚠ **Dois clientes em churn têm a página** — Lenny e Recco. **Elas descrevem como a conta era
     operada, e isso não morre com o churn.**
446. **🆕 `Linear` — décima segunda ferramenta**, gestão de projeto da uMode. Achada de relance,
     com um item vivo: *"Planejamento e Estudo do PRD Permissionamento Login"*, **`In Progress`
     e health `offTrack`** desde **20/01/2026**. **Nunca varrido.**
447. **🆕 `Felipe Sindeaux` — pessoa da Casa que o corpus não tinha**, *lead* do item do Linear.
     ⚠ **Ficha não criada: uma linha de busca não é fonte suficiente para nascer uma pessoa.**
     **Entra na revisão do `HOJE` dos uModers**, ao fim da varredura.

## Felipe Sindeaux, Linear morto, e a Qualitá com login (22 set 2026)

448. **🟢 DECIDIDO — `Felipe Sindeaux` é desenvolvedor, focado em processos de integração.**
     Vinicius, textual, em 22 set 2026. `[D]` **Ficha criada** — e só depois da confirmação
     dele: até ali existia uma linha de busca, e **uma linha de busca não é fonte suficiente
     para nascer uma pessoa.**
     ⚠ **`Área` ficou `[a preencher]`: `Tecnologia` seria o palpite óbvio e não foi assumido** —
     ele disse o papel, não a Área das 8 travadas.
     ⚠ **O foco dele toca um tema que a varredura achou aberto em vários clientes** — a dor de
     integração da CAEDU, o DE/PARA da VIX, o `Dossie Acompanhamento Integração` da Moda
     Objetiva, o `Luiza Barcelos | Integração com ERP`. **Nenhuma fonte o nomeia: a ligação é
     minha, e é hipótese.**
449. **🟢 DECIDIDO — o `Linear` NÃO se varre.** Vinicius: *"foi a ferramenta de gestão durante
     um período mas não é mais usada."* `[D]`
     ⚠ **Consequência:** o item *"Planejamento e Estudo do PRD Permissionamento Login"*, que
     aparece como **`In Progress` e health `offTrack` desde 20/01/2026**, é **histórico
     congelado, não trabalho em curso.**
     🔴 **Segundo caso de ferramenta morta cujo estado engana quem lê**, depois do Kanbanize.
     **Vira padrão de leitura: estado em sistema descontinuado não é estado.**
450. **🔺 CORREÇÃO — a `Qualitá` TEM perfil de usuário na plataforma.** Horas antes eu registrei
     que ela operava *"todo o processo por WhatsApp"* e que *"o corpus não tem modelo para
     terceiro"*. **A matriz da Oficina Reserva tem a coluna `Oficina - Qualit|-í`** — o nome está
     com **encoding quebrado na própria fonte**.
     ⚠ **A dor do WhatsApp é de 26/06/2024; a matriz é de 17/03/2026.**
     **Ou destravou, ou o perfil existe e não é usado. Não sei qual.**
     🔴 **Com o `Fornecedor` da Luiza Barcelos e da Lenny, são TRÊS casos de terceiro com login.
     Não é mais exceção.**
451. **🆕 As interfaces do SAP estão NOMEADAS E NUMERADAS** na matriz da Oficina Reserva:
     `Atualização de Produtos (SAP - Interface 3)` e `Novos Produtos ZZNet (SAP - Interface 1)`.
     🔴 **É o único lugar do corpus onde a integração SAP aparece decomposta por interface** —
     e conecta direto com a dor de *"90% do tempo dedicado ao SAP"*. **🆕 `ZZNet`** é mais um
     nome de sistema; ⚠ **não sei se é sistema, módulo do SAP ou rotina.**
452. **🔴 Uma regra de CÓDIGO vazou para o título de uma seção do Notion:**
     `read_only: !current_context.current_policy.name.in?(['Oficina - Master', 'Oficina -
     Planner','Oficina - Estilo'])`.
     **É evidência real do mecanismo de permissão da plataforma** `[C]` — há `current_policy` e
     `read_only` como expressão avaliada. **Vale confrontar com o schema do banco.**
453. **🆕 A ficha de produto da Oficina é organizada POR ÁREA** — abas `Estilo | …`,
     `Cadastro | …`, `Engenharia | …` e `Planejamento`. **Nenhum outro cliente lido tem as abas
     nomeadas por área.** E **`Materiais (Facção)` × `Materiais P.A.`** são abas distintas —
     **facção aparece de novo, agora como divisão de material na ficha.**
454. **🟢 `Fale com o Suporte` liberado para os 8 perfis da Oficina** — terceiro cliente, e
     **confirma que a Luiza Barcelos é a exceção, não a regra.**
     ⚠ **A linha `Manual` NÃO EXISTE na matriz da Oficina** — nem liberada, nem bloqueada.
     **Ausência de linha é diferente de bloqueio, e eu não sei o que significa.**
455. **⚠ Mudança prevista e não executada, escrita na página da Oficina:** *"provavelmente no
     novo formato da Oficina não teremos mais o Perfil de compras. Por hora, seguimos com esse
     perfil ativo."* Última edição: **17/03/2026**.
456. **🔴 Mais cinco nomes de perfil sem área canônica** (Oficina): `Planner` · `Atacado` ·
     **`Qualitá`** · `Ecommerce Marketing` · `Master`. **O total de nomes de área fora da grade
     passa de treze.**

## O template de página de cliente, e a Lenny (22 set 2026)

457. **🔺 CORREÇÃO do que eu escrevi hoje mesmo: o template de página de cliente EXISTE.**
     No registro (i) eu afirmei que *"não existe 'o template de pessoa da página do cliente'"*.
     **Existe:** `. Página Cliente [Template]`, dentro do próprio `Mapa de Clientes`, com
     `Status = Inativo` e **oito blocos definidos**. Registro em `_varredura-2026-09-22l`.
     **O que eu errei foi a causa: não é falta de template, é falta de adesão.**
     ⚠ **A conclusão prática de (i) continua valendo** — não dá para prever a estrutura de uma
     página sem abri-la. **O motivo é outro; o efeito é o mesmo.**
458. **🔴 Nenhuma das 15 páginas que abri tem os oito blocos.** E o bloco mais revelador é o
     **`Atendimento e Suporte`**, que prevê **`Aprendizados e Anotações Importantes`** —
     exatamente onde deveria estar coisa como *"Se ela está feliz com o projeto, estamos bem"*
     (NK STORE) ou o aprendizado de permissão da VIX.
     **Esses aprendizados existem e estão em lugares improvisados: dentro de célula de tabela,
     no fim de página de permissão, em comentário de validação. O lugar certo estava desenhado
     desde o começo.**
459. **🔴 O template NÃO tem `Diretores e Representantes Legais`, e QUATRO clientes têm**
     (NK STORE, Osklen, Lofty Style, Moda Objetiva). **Ou o template envelheceu, ou quatro
     clientes o ampliaram por conta.** ⚠ **A diferença importa: é onde mora o Representante
     Legal.** Última edição do template: **16/07/2025**.
460. **🔴 HÁ LIMITE CONTRATADO DE USUÁRIOS, e o corpus não tem esse número para cliente nenhum.**
     O `Playbook Cadastro de Novos Usuários uFlow` registra: *"livre dentro do limite contratado,
     o KA precisa aprovar com o líder do cliente a contratação de mais usuários"*.
     **Muda a leitura de dois achados: Puket com 43 usuários e 2 módulos, NV com 61 declarados.**
461. **🔴 `Fale com o Suporte` BLOQUEADO na Lenny Niemeyer também — é 2 × 2.**
     Bloqueado: Luiza Barcelos, Lenny Niemeyer. Liberado: VIX, Oficina Reserva.
     **Não é exceção de um cliente: é metade dos que li.**
462. **🔴 A base `Usuários` da Lenny tem 29 linhas e TODAS estão VAZIAS** — criadas no mesmo
     segundo, em 11/07/2025. **Esqueleto colado e nunca preenchido.**
     🟢 **MAS o SCHEMA dela é o modelo de pessoa de cliente que falta no corpus:**
     `Nome` · `E-mail` · `Perfil do Usuário` · **`Departamento Cliente`** · `Status`.
     **São exatamente os cinco campos que eu venho perseguindo, e `Departamento Cliente` é o
     vínculo pessoa↔área.** 🔴 **A uMode já desenhou a tabela certa e a deixou vazia.**
     **Verificar se outro cliente tem a mesma base preenchida.**
463. **⚠ A linha `> excluir variante` existe na matriz da Lenny e está EM BRANCO para todos os
     perfis** — nem liberado, nem bloqueado. **Quinto caso da dor de variante, e aqui ela
     aparece como decisão não tomada dentro do próprio documento de permissão.**
464. **🆕 Fontes que a busca revelou e ninguém varreu:**
     🔴 **`Controle de Acessos de Usuários`** (em `uModers / Vinícius Risoleo`) — **lista de
     contas com total de usuários ativos e % de ENGAJAMENTO** (quem acessou no mês ÷ ativos).
     **O corpus não tem métrica de engajamento.** ·
     `Databases / Processos mapeados` · `Databases / Demandas de Clientes` (⚠ **é a mesma base
     das 999 demandas, ou outra?**) · **`Operation Hub`**, que cita **`documentacao.umode.tech`**
     — 🔴 **segundo domínio de documentação**, além do `docs.umode.app` da Lofty Style.

## O modelo de usuário do uFlow (22 set 2026)

465. **🔺 CORREÇÃO do item 406: `uDash` é PERFIL INTERNO da uMode, não produto contratado.**
     A página `Controle de Acessos de Usuários` lista, entre os filtros de exclusão da análise:
     *"os perfis `uRocket` e `uDash` são sempre internos"* — **com checkbox marcado, ou seja,
     perguntado e respondido.**
     **Os "2 usuários uDash" da Luiza Barcelos não são licenças vendidas: são acessos da própria
     uMode dentro da conta do cliente.** ⚠ **E resolve a ambiguidade:** `uDash` é **perfil** nos
     dois casos que eu li. O nome de produto legado existe, mas não é isso que essas linhas dizem.
     🆕 **`uRocket` também é perfil interno**, com nota de *"cancelamento serviço"*.
466. **🟢 ACHADO GRANDE — o corpus ganhou o modelo de dados do uFlow.** Tinha o do BrainHub
     (Mongo) e **nada** sobre a plataforma que os clientes usam. Registro em
     `_varredura-2026-09-22m`. Tabelas reais: **`jumper_users`** · **`jumper_entities`** (🔴 **é
     a conta, o cliente**) · **`user_roles`** · **`policies`** (🔴 **é o perfil**) ·
     `ahoy_visits`/`ahoy_events` · **`audits`** (modelo `J3::UserRole`).
     🆕 **O prefixo `jumper_` e o namespace `J3` dizem que a plataforma se chama `Jumper` no
     código. O corpus nunca registrou esse nome.**
467. **🔴 Regra contraintuitiva confirmada: `ju.status IS NULL` significa usuário ATIVO.**
     A própria fonte precisou perguntar duas vezes, e a resposta é *"sim, é a regra oficial da
     plataforma, não uma exceção"*. **Qualquer análise que trate `NULL` como ausência de dado vai
     contar errado.** Role ativa = `ur.status = 1` **e** `ur.deleted_at IS NULL`.
     **Contas internas: `entity_id` 935 e 69.** **`API` conta como usuário válido.**
468. **🔴 A métrica que falta no corpus é ENGAJAMENTO POR ACESSO**, e a fonte já a define:
     *"usuários que acessaram no mês ÷ usuários ativos — dá uma leitura rápida de quais contas
     estão dormentes antes mesmo de entrar nelas"*; *"a distância entre 'ativos' e 'acessaram' é
     exatamente o indicador de engajamento que mais interessa ao gestor"*.
     🔴 **O corpus mede conta por demanda e por chamado — e chamado depende de ter o botão
     liberado (item 440). Acesso é a única medida que não depende de permissão.**
469. **⚠ Há DUAS medidas de último acesso, e elas divergem:** `last_sign_in_at` é **login de
     fato**; `ultima_visita` (de `ahoy_visits`) é **navegação na sessão logada**, que pode durar
     uma semana. A fonte registra: *"temos algumas divergências disso nítidas"*.
     🔴 **Toda ficha de pessoa com "última atividade" precisa dizer qual das duas está usando.**
470. **⚠ `Flávia` aparece como autora de sugestões na página.** **Ficha não criada — um nome de
     seção não é fonte suficiente**, mesma régua aplicada ao Felipe Sindeaux, que só nasceu
     depois da sua confirmação. **Entra na revisão do `HOJE` dos uModers.**
471. **⚠ Validação citada com `entity_id = 3344`**, esperando **41 usuários ativos e 16 roles
     ativas**. ⚠ **Não sei qual conta é** — e o `entity_id` é a chave que ligaria o corpus à
     plataforma.

## A correção do entity_id, e a Cambos derrubando uma hipótese (22 set 2026)

472. **🔺 CORREÇÃO — eu transformei um identificador técnico em leitura de negócio.**
     O Vinícius confirmou que `entity_id = 3344` é a Baw **e corrigiu o uso que eu fiz disso**:
     *"É dado do banco. Não é relevante essa informação no contexto. Somente pra você identificar
     de onde era o contexto que está consultando."* `[D]`
     **Eu tinha escrito que os "41 usuários ativos e 16 roles" eram a SEXTA evidência, e a
     primeira quantitativa, de que a Baw está mal classificada.** São **contagem esperada de uma
     query de validação** — fixture de teste de mai/2026, não medição de conta.
     🔴 **A má classificação da Baw segue com CINCO evidências qualitativas, não seis.**
     **O erro é primo do de tratar estado em sistema descontinuado como estado.**
     **Removidas as duas perguntas que nasceram dele.**
473. **🔺 A Cambos DERRUBA a hipótese do `Manual` bloqueado.** Eu tinha escrito *"dois de dois:
     hipótese forte"* com VIX e Luiza Barcelos. **Na Cambos, `Manual` e `Base de Importação`
     estão LIBERADOS para os 5 perfis.** ⚠ **E na Oficina Reserva a linha nem existe.**
     🔴 **Dois bloqueados, um liberado, um ausente: não é padrão, é configuração por cliente.**
     **Foi bom ter escrito "hipótese" e não "padrão".**
474. **🆕 A integração SPI tem TELAS PRÓPRIAS no uFlow**, com prefixo `[SPI]`:
     `Aviamentos Pendentes` · `Cores Pendentes` · `Banhos Pendentes` · `Fornecedores Pendentes` ·
     `Produtos Pendentes`. 🔴 **A plataforma tem tela feita sob medida para o ERP de UM cliente.**
     **Isso muda a leitura do que "módulo Integração" significa.**
475. **🔴 `Novo Pedido (só a Cambos tem)` — funcionalidade exclusiva de um cliente, e está
     BLOQUEADA para os cinco perfis.** **Construída, exclusiva, e desligada.**
476. **🆕 O cliente RENOMEOU as abas da ficha de produto**, em caixa alta e com vocabulário
     próprio: `COSTURA E BORDADO` · `TAMANHOS PILOTO (Grade)` · `QTD PARA PILOTAR (Lote)` ·
     `FABRICAÇÃO (Fornecedor)` · `APROVAÇÕES DA PILOTO` · `ORIGINAL` · `INTEGRAÇÃO SPI`.
     🟢 **É o "apelido interno" do princípio nº 1 da Arquitetura V1 acontecendo de verdade** —
     o termo canônico entre parênteses, o do cliente na frente. **Primeira evidência concreta
     desse princípio no corpus.**
477. **🆕 Há uma `Planilha com os usuários ativos` da Cambos no Google Sheets**, linkada no topo
     da página de perfil. ⚠ **Não aberta — pode ser a lista de pessoas que falta.**
478. **⚠ O mesmo perfil tem dois nomes na mesma página da Cambos:** `Cambos - Time
     Desenvolvimento` na primeira tabela, `Cambos - Desenvolvimento` na segunda. **Não escolhi um.**
479. **🔴 Sete funções bloqueadas para TODOS os perfis, em dois clientes** (Cambos e Oficina
     Reserva): `Tabela Dinâmica` · `Composição de Custo` · `Coordenado` · `Estampa` · `Tag` ·
     `Pack` · `Campo Personalizado`. ⚠ **Dois casos: pode ser função que ninguém usa.**
480. **🚨 TERCEIRO risco de credencial, e este está no coração da plataforma:
     há uma página chamada `Credenciais` em `uMode Geral / uFlow / Documentação
     de Setup - PLM`, seção `Nova uFlow/uRocket`** (`c422e214…`).
     🔴 **NÃO ABRI, de propósito.** O título já basta para registrar o
     risco, e abrir só traria segredo para dentro do contexto e do histórico da sessão.
     ⚠ **Diferente das outras duas, esta não é de um cliente — é da
     própria plataforma.** **A rotação segue sendo ação sua.**
481. **🔴 Existe um ÍNDICE TÉCNICO COMPLETO do uFlow e o corpus não tinha
     nada dele:** `Documentação de Setup - PLM`, com **~70 páginas em 14
     seções** — Automações, Configs da Conta, Checklists, Validação,
     Menus Personalizados, Traduções, Documentação DEV, Relatórios, Deploys,
     Integrações, E-mails Automatizados. **Li o índice; não li as páginas.**
482. **🟢 Achei o catálogo de automações que eu tinha perguntado onde
     ficava** (os IDs `#1136`, `#1175`, `#989` da Cambos). São 8 páginas: `Aprovação`
     · `Calculadora de campos` · `Gerador de Referencia` · `Ação de destruir
     Materiais` · `Habilitar mover card para etapa anterior` · `Ações com mais de
     uma expression` · **`Projeto Puket - Kanban de Estilo NOVO`** · `Criar fornecedor no
     produto ao entrar em etapa do workflow`. ⚠ **Nenhuma aberta.**
483. **🟢 Cada `entity_config` tem página própria — e DUAS são
     NOMINAIS de cliente:** **`[Vivara] Alterar nomes tecido/aviamento`** e **`[NV] Bloquear
     Alteração de Elementos da Tabela na FT`**. 🔴 **A Vivara é cliente da
     carteira, e "alterar nomes" é o apelido interno de novo — agora com config e
     documentação própria.**
484. **🆕 Há uma seção inteira de `Traduções`:** `Abas e nomes de
     campos da Ficha técnica` · `Campos Custom` · `Impressão` · **`Nomes de
     Modelos`**. 🟢 **É onde o apelido interno é OPERADO**, e fecha a cadeia:
     princípio (Arquitetura V1) → config (`model_name_*`) → procedimento (aqui).
485. **🔴 `Como é o processo de integração?` e `Logs e integração
     (Google Cloud Watch)` existem como páginas.** ⚠ **A dor de integração
     atravessa CAEDU, VIX, Moda Objetiva e Luiza Barcelos — e o processo está escrito
     em algum lugar que ninguém do corpus tinha apontado.** **Não abertas.**
486. **🆕 Três ferramentas novas, todas na seção de Relatórios:**
     **`BigQuery`** (`Utilização do BigQuery para consulta no banco`), **`Blazzer`**
     (`[Blazzer] Realizando consultas pelo BigQuery` — ⚠ grafia da fonte; o produto
     conhecido chama-se `Blazer`) e **`MongoDB Compass`** (`MongoDB Compass (Aggregations)`, em
     Documentação DEV). 🔴 **Mongo aparecendo no acervo do uFlow é
     estranho** — o Mongo do corpus é o do BrainHub, e o uFlow é Rails/`J3`.
     **Não concluo: registro a estranheza.**
487. **⚠ O Manual do Permissionamento tem DUAS formas na mesma página:** a página do
     Notion e um PDF anexado, `manual_do_permissionamento_umode_(5).pdf` — **versão 5**.
     **Li a página; não li o PDF. Podem divergir.**
488. **🆕 `Estudo de caso do Card 17680`** — ⚠ **`Card` com ID de cinco
     dígitos** é vocabulário de ticket que o corpus não tem. **De qual sistema?**
489. **🆕 `Associar usuário na uDash` é página de Menu Personalizado** —
     **terceira evidência de que `uDash` é perfil interno**, com o registro `(m)` e a
     página de Controle de Acessos.
490. **⚠ A página `Importação` do acervo técnico ESTÁ VAZIA** — o
     próprio Notion devolve *"este documento não tem conteúdo"*. **Seção
     criada e nunca escrita.**
491. **🔴 O acervo `Setup - PLM / CLIENTES` tem NOVE clientes, não um:** NV ·
     RESERVA · BAW · OFICINA · VIX · **StudioZ** · PUKET · CAEDU ·
     NK Store. ⚠ **Só a NV foi tocada.** E o título diz `(Em desenvolvimento)`,
     **última edição em 16/07/2025** — **mais de um ano.**

## CAEDU — a hierarquia nos dados reais, e o Notion fora de alcance (23 set 2026)

492. 🔴 **A hierarquia `Griffe › Linha › Grupo › Subgrupo` NÃO aninha nos dados da CAEDU.**
     Medido na `Extração Caedu - 28ago26.json` (48.551 linhas, 42.488 produtos): **23 de 33
     `Linha` têm mais de uma `Griffe`**, **75 de 231 `Subgrupo` têm mais de um `Grupo`**, e
     `BOTTOM` é um `Grupo` que aparece sob **24 `Linha`**. Existem **1.015 combinações reais
     num cartesiano de 8.828.820 — 0,01%**.
     `[P]` **Comporta-se como classificação por facetas, não como árvore.** 🔴 **Decisão
     necessária antes de desenhar a tela ou o modelo:** **tratamos como 4 eixos independentes
     ou insistimos na cascata?** Cascata contradiz o dado da própria conta.
     ⚠ **Ressalva honesta:** a extração é achatada; ausência de aninhamento nela **não prova**
     ausência de estrutura na origem. Registro em `_varredura-2026-09-23e`.
493. 🔴 **`Griffe` e `Linha` são campos do LINX; `Grupo` e `Subgrupo` são do uFlow.**
     A hierarquia pedida **atravessa dois sistemas** — dois níveis vêm do ERP. **Isso converte a
     dor de taxonomia em dor de integração**, e dá mecanismo ao que estava como queixa.
494. ⚠ **A hierarquia de 4 níveis da Loungerie pode não servir de precedente para a CAEDU.**
     O corpus registra o desenho da Loungerie como caso pronto. **Se os dados da CAEDU não
     aninham, ou o modelo da Loungerie é outro, ou ele é intenção e não implementação.**
     🔴 **Não abri a página da Loungerie nesta sessão — não afirmo qual dos dois.**
495. 🔴 **`Coleção` tem duplicata por acentuação na base da CAEDU.** `VERÃO 26/27` (4.971) e
     `VERAO 26/27` (1.690); `VERÃO 25/26` (4.189) e `VERAO 25/26` (2.241). **Duas coleções na
     base para uma no mundo**, e `Coleção` é campo do uFlow. **Toda contagem por coleção erra.**
     **Decisão:** normalizamos, ou o cliente normaliza?
496. ⚠ **Lixo de cadastro em `Griffe Linx` e `Linha (Linx)`.** `O`, `F`, `M` com 1 registro cada;
     `LINGERIE` (17) convivendo com `INTIMA E PRAIA` (5.293); `66` e `63` como `Linha`;
     `INFANTIL` (27) ao lado de `INFANTIL NAS` e `INFANTIL NOS`. **Vem do ERP — saneamento não
     é nosso, mas o relatório que a uMode entregar carrega o erro.**
497. ⚠ **47,8% das linhas não têm `SKU` e 16.717 não têm status de variante.**
     🔴 **Não sei se é produto sem variante cadastrada ou variante não exportada.** São leituras
     diferentes e a extração não distingue. **Pergunta para quem operou a extração.**
498. 🔴 **O conector de Notion desta sessão não alcança o workspace da uMode.** `get-teams`
     devolve só o teamspace `Vinícius Risoléo` (conta pessoal) e busca por `Caedu` devolve zero.
     ⚠ **Não afirmo que o conteúdo sumiu** — as sessões de 22 e 23 set leram normalmente.
     **Afirmo que não alcanço por este conector.** 🔴 **Ação do Vinicius: reconectar o Notion na
     conta da uMode.** **Trava:** `Setup - PLM / CLIENTES / CAEDU`, as 54 sub-páginas fechadas
     da CAEDU e o `Mapeamento da Conta - Caedu`.
499. ⚠ **Três arquivos de CAEDU em `Downloads` ainda não abertos:**
     `Caedu - Query da API.xlsx` (3,5 MB), `caedu_mega_line_reports-2026-02-06` (30 MB) e
     `Caedu 1.jpg`. **São fonte local, fora do Notion — não dependem do conector.**
500. 🔴 **A CAEDU não tem `integracao.md`**, sendo que **integração é a dor número 1 dela** e
     11 outros clientes têm o arquivo. **Lacuna de corpus, não de fonte.**

## Acesso ao Notion restabelecido, e o que a primeira varredura achou (23 set 2026)

501. 🟢 **RESOLVIDO — acesso ao Notion da uMode.** O conector foi reautorizado no workspace
     `uMode Mode's Notion`. **A causa era escolha de workspace na tela de OAuth**, não conta
     errada: o token vinha emitido para `Notion de Vinícius Risoléo` (pessoal, 2 usuários).
     ⚠ **Lição de diagnóstico:** `get-teams` **não serve** para validar acesso — devolveu
     `General`/`Inovação`/`Kudos`/`Recrutamento`, nenhum dos teamspaces reais. **O teste que vale
     é uma busca por termo conhecido.** Fecha o item 498.
502. 🟢 **RESOLVIDO — a segmentação de conta.** Era a pergunta transversal nº 1 da fila.
     A base `Segmentação Grupos` tem **Enterprise (Grupo 1, `WIP Estratégico 6`, descrição
     "Reserva + Soma") · Médios (Grupo 2, `2,25`) · SMB (Grupo 3, `1,75`)**, mais
     `Grupos 4: Outros Clientes` e `Churn`. **O vocabulário do corpus já estava certo.**
     🆕 **`WIP Estratégico` é modelo de ALOCAÇÃO DE CARGA** — a base vive sob
     `Alocação de Cargas por Clientes em Vigor`. **Enterprise pesa 3,4× um SMB.**
     **O corpus não tem esse conceito em lugar nenhum.** 🔴 **Decisão: vira campo de cliente?**
503. 🔴 **A CAEDU é `SMB` (Grupo 3) na base viva — e isso contradiz o porte dela.**
     O corpus supunha que "Grupo 3" fosse resíduo de export antigo. **Não é.** E a fonte do
     Notion descreve a conta como *100+ lojas, ~R$1bi de faturamento (2023)*.
     🔴 **Uma conta desse porte está na faixa de MENOR alocação de time (`1,75` contra `6`),
     em `Onboarding`, com o CAEDU 2.0 em montagem.** **Decisão: reclassificar?** É pergunta
     comercial, não de dado.
504. 🔺 **Quatro correções de segmentação aplicadas** — Arezzo e Hering viraram `Enterprise`;
     Baw virou `SMB`; `Lojão do Brás` saiu de `Churn` para `Grupos 4: Outros Clientes`.
     **Causa única das quatro: o campo é `relation` e a consulta anterior o lia como valor.**
     ⚠ **Vale conferir se outros campos do `Mapa de Clientes` são relação e estão vazios pelo
     mesmo motivo** — `Atendimento 2024` é um deles, e continua sem resolver.
505. 🔴 **O acervo `Setup - PLM / CLIENTES` foi superestimado no nosso próprio plano.**
     O `AGORA.md` o tratava como passo imediato e maior rendimento. **4 das 8 páginas estão
     vazias — inclusive a CAEDU.** Só a **RESERVA** tem acervo real: base
     `CENTRAL DE DOCUMENTAÇÕES` com **18 documentos** de regra de negócio, integração e operação.
     **Decisão: a RESERVA virou o caso-referência de documentação por cliente. Replicamos o
     padrão dela para os outros?**
506. 🔴 **O diário de varredura produz FALSO-NEGATIVO na § 4.** `Segmentação Grupos` seguia
     listada como *"não varrida"* nos 48 arquivos **depois de já ter alimentado 34
     `institucional.md`**. **A § 4 não é podada quando a fonte é varrida.**
     🔴 **É defeito do mecanismo que existe justamente para impedir retrabalho** — e me fez
     repetir busca hoje. **Corrigir em `gera-pendencias-e-fontes.py`.**
507. 🆕 **`Atendimento 2025` não é só pessoa: é pessoa OU o rótulo `SMB`.** Julianne + Pedro (7
     contas) · Laura (7) · Fernanda (3) · **`SMB` (7, todos em `Sem CS` ou `Churn`)**.
     🟢 **Confirma por fonte independente que `Sem CS` é SKU self-service**, não momento de jornada.
     ⚠ **A Baw contradiz:** `SMB` na segmentação, `Sem CS` no status, **mas com a Laura no
     atendimento**. Os três campos discordam.

## A base de contratos do Financeiro — a terceira taxonomia (23 set 2026)

508. 🔴 **Existe uma TERCEIRA taxonomia de ferramenta, e ela mistura níveis.** Além dos
     **7 módulos** do uFlow e das **16 Soluções** do Portfólio, a planilha de contratos do
     Financeiro tem **11 serviços faturados** — e na mesma coluna convivem **plataforma**
     (`uFlow`, `uRocket`), **produto** (`uBuy`, `uPick`, `uPlan`, `Fashion IA`), **módulo**
     (`Gestão de coleções`, `Reports`) e **serviço** (`Workshop`, `SaaS`, `IPSP`).
     🔴 **A Loungerie aparece com `Gestão de coleções` e SEM `uFlow`** — sendo que o primeiro é
     módulo do segundo. **Contar cliente de uFlow por essa coluna subconta.**
     **Decisão: separamos na origem, ou traduzimos na entrada do corpus?**
509. 🟢 **CONFIRMADO por fonte independente: o PlanejAI é `(contratado)` na Reserva, não piloto.**
     `uPlan` → `PlanejAI` já estava travado no `CONTEXT.md`; a ficha do produto deixava o
     qualificador pendente porque o ÍNDICE MESTRE não dizia. **A planilha de contratos diz.**
     🔴 **Consequência:** uma solução `MVP`, rodando em Lovable, **já gera receita**.
510. 🔴 **`uBuy` é o EnriqueceAI? Não afirmo — e o caso que impede é a Osklen.**
     Reserva e NV têm `uBuy` (bate com o que o Vinicius apontou), **mas a Osklen também tem, e
     ele não a citou.** ⚠ **E o nome legado registrado do EnriqueceAI é `CadastroAI`, que não
     existe na base.** **Se `uBuy` não for ele, o EnriqueceAI não é faturado em lugar nenhum —
     e esse é o gap de receita.** **Pergunta para o Comercial.**
511. 🔴 **`Fashion IA` é receita ativa em 3 contas e tem ZERO ocorrência no corpus.**
     `PUKET`, `AGUA DE COCO` e `LA MODA`. **Verificado por busca nos 2.513 `.md`.** Não é um dos
     7 módulos nem uma das 16 Soluções. ⚠ **A Puket é das contas mais varridas que temos —
     43 pessoas, página aberta — e nenhuma fonte dela menciona isso.**
     **O que é `Fashion IA`? É uma das 16 com outro nome, ou um 17º item?**
512. 🔴 **Mentoria não é linha da base de contratos, mas tem CRM e acervo.**
     `AGENTES E PROJETOS / Projeto: Mentoria (João Risoléo)` + `Metodologia MBS` +
     `CRM — EducAI`, e o `protocolo-varredura-cliente.md` cita *um CRM de mentoria*.
     **Na base só existe `Workshop`, em um cliente (`SINBI`).**
     **Mentoria é serviço faturável? Ou é faturada como `Workshop`?**
513. 🔴 **Dois clientes ATIVOS não existem no corpus — e o corpus os conhecia de forma que
     CONTRADIZ a base.** **`SINBI`** (serviço `Workshop`) aparece no
     `_backlog-infra-tecnologia.md` 3.2b apenas como *dona de dezenas de submarcas* na base de
     Taxonomia. **`Tempo de Criança`** (serviço `SaaS`) está no
     `_varredura-ferramentas-produtos-areas.md` com a anotação literal **"(não existe no CRM)"**.
     🔴 **A base do Financeiro diz que os dois são clientes ativos.** **Viram casa no corpus?**
514. 🟢 **O `uRocket` teve carteira própria de 15 contas e hoje tem uma.** Os 9 ex-clientes
     (`CRIS-FAEL`, `Tropical Fashion`, `Luxo das Marias`, `Opera Kids`, `Four One Moda`,
     `Aladim Decorações`, `Ribeiro e Pavani`, `Nanaminze`, `FORMITZ`) **não existem no corpus**.
     **Não é só um produto descontinuado: é uma carteira que evaporou.** ⚠ **Entram como casa,
     ou ficam só como história de portfólio?** — ver item 519 do protocolo de criação.
515. ⚠ **`IPSP` e `uPick` aparecem contratados só na VIX.** O corpus registra `IPSP` como
     **oportunidade na Cambos** (*"uPlan e IPSP — cliente não tem informações de performance"*).
     **São a mesma coisa? E o que é `IPSP`?** ⚠ **Grafia divergente já registrada:** o corpus
     também tem `ISPS` em outro ponto. **Uma das duas está errada.**

## A colheita de pessoas nos 15 clientes com página aberta (23 set 2026)

516. 🔺 **A tabela de usuários da CAEDU é EXCEÇÃO, não padrão.** Varridos os 15 clientes com
     página aberta: **só a Puket tem tabela de usuários com e-mail** (43 linhas, e em versão
     reduzida — 4 colunas, sem as 6 de permissão que a CAEDU tem). **Os outros 13 não têm.**
     ⚠ **E a Puket já estava extraída.** **Expectativa corrigida: não há 93 pessoas por cliente
     esperando em cada página.**
517. 🔴 **O toggle `Pessoas` é o que realmente existe — e em 6 de 15.** NK STORE · Cambos ·
     Luiza Barcelos · Moda Objetiva · Lenny Niemeyer · Recco. **Quatro já estavam no gerador**;
     🟢 **Lenny Niemeyer e Recco foram extraídos agora** (+3 fichas na Lenny, +3 na Recco, com
     cargo e e-mail). **Lofty Style tem o template vazio** e **7 não têm o toggle**:
     Reserva · VIX · Puket · NV · Oficina Reserva · Baw · Loungerie.
     ⚠ **Reforça o registro `_varredura-2026-09-22l`: o template de página de cliente existe e
     quase ninguém segue.**
518. 🚨 **TERCEIRA página com credencial em texto claro: `Lofty Style`.** A página expõe a senha
     de acesso da documentação de integração. **Nenhum valor foi copiado.** Junta-se a
     **NK STORE** (usuário/senha/IP do banco Linx, na própria página do cliente) e à página
     `Credenciais` do uFlow (item 480). 🔴 **Agora são quatro focos conhecidos. A rotação é ação
     do Vinicius.**
519. 🔴 **Achada a PRIMEIRA pessoa ligada a `Fashion IA` em qualquer fonte.** Na Recco, o toggle
     `Pessoas` nomeia **Aline, Analista de Ecommerce**, como *Líder Responsável pelo Projeto —
     **Fashion AI***. ⚠ **A grafia na fonte é `Fashion AI`; na base de contratos do Financeiro é
     `Fashion IA`** — duas grafias para o que parece ser a mesma coisa.
     🔴 **E a Recco está em `Churn`.** Ou seja: o serviço que o corpus não conhecia (item 511)
     tinha líder nomeada numa conta que a uMode perdeu. **Isso é fio para puxar.**
520. ⚠ **`Soma` reaparece.** O campo `Observação` de Victor Siqueira (Lenny Niemeyer) diz
     *"Trabalhou no Soma"*. `Soma` é o grupo citado na descrição do segmento `Enterprise`
     (*"Reserva + Soma"*, item 502). **Não afirmo que seja o mesmo** — registro a coincidência.
521. ⚠ **`financeiro3@recco.com.br` é caixa de setor, não endereço nominal** — idêntico à
     property `Email Principal Financeiro` da página. 🔴 **Caixa de setor NÃO serve como chave
     de identidade de pessoa** (item 252): duas pessoas do financeiro teriam a mesma.
     **A regra de identidade precisa distinguir e-mail nominal de e-mail de setor.**
522. 🔵 **Caminho novo, não varrido: as bases de Pesquisa de Satisfação.** Cinco encontradas —
     Kick Off e Treinamento de `Lofty Style`, `Lenny`, `Recco` e `Osklen`. **Tipicamente trazem
     nome e área do respondente**, ou seja, são censo parcial do time do cliente. A da Lenny
     declara **22 respondentes por área**. **É a melhor fonte de pessoa ainda fechada.**
523. 🔵 **Sub-páginas de perfil de acesso não abertas em Baw e Oficina Reserva.** Quatro na Baw
     (`Perfil de Acesso - BAW`, mais `(1)`, `Estilo` e `Engenharia/Compras`) e uma na Oficina
     (`2b6b1d38…`). **É o lugar provável dos usuários desses dois** — eles não têm toggle
     `Pessoas` nem tabela.

## Os 8 clientes ativos com página nunca aberta (23 set 2026)

524. 🟢 **Varridos os 8 clientes ativos cuja página nunca tinha sido aberta.** Pessoa real em
     **3 de 8**: **Camys** (6, com e-mail e perfil), **Mondepars** (10, com e-mail) e **Hering**
     (3 nomes, **zero e-mails na página inteira**). **Vazios em 5:** Arezzo (página em branco),
     TDC (só um link), Cavallari, Studio Minah e Ton Age (template íntegro, nenhuma linha
     preenchida). **+19 fichas · corpus de pessoa de cliente: 318 → 340 · 18 → 21 clientes.**
525. 🔴 **A Mondepars tem 10 usuários e TODOS com perfil `Dono`.** A própria página declara:
     *"Não há nenhum perfil definido por enquanto. Todos possuem status de donos da conta."*
     🔴 **Risco de governança**: dez contas com poder total, e **não há área derivável do perfil**
     nesse cliente. ⚠ **Decisão: isso é o estado real ou é setup inacabado?**
526. 🔴 **Quarta natureza de pessoa: o TERCEIRO com acesso de dono.** Na Mondepars,
     **`Matheus Cazuza` usa domínio `thela.studio`** — agência/terceiro, **com perfil `Dono`**.
     Junta-se a `Fornecedor` (Luiza Barcelos, Lenny) e `Qualitá` (Oficina Reserva).
     🔴 **O BrainHub não modela isso** — não é pessoa da Casa nem do cliente.
527. 🔴 **Duas caixas FUNCIONAIS entraram como se fossem pessoa.** `sac@mondepars.com`
     (Carolina Abreu) e, na Camys, uma linha cujo `Usuário` é **`DIGITAL, SAC & INSIDe`** — nome
     de função, não de pessoa — com e-mail nominal `alessandra@`. **Somados a
     `financeiro3@recco.com.br` (item 521), são três.** 🔴 **A regra de identidade precisa
     separar e-mail nominal de caixa funcional antes de qualquer deduplicação.**
528. 🔺 **Dois defeitos do `gera-fichas-pessoa.py`, achados e corrigidos hoje.**
     **(a)** o nome do arquivo saía da parte local do e-mail; **sem e-mail, gerava um arquivo
     chamado `.md` e a pessoa sumia em silêncio** — foi o que aconteceu com `Juliana`
     (Mondepars). Agora cai para o nome, e o que não dá para nomear vai para a lista visível de
     descartados. **(b)** a ficha imprimia **``` `` ``` — e-mail corporativo** com o campo vazio,
     **afirmando ter o que não tem.** 🔴 **Afirmação falsa é pior que campo vazio.**
529. ⚠ **A lista de áreas que aparece em Cavallari, Studio Minah e Ton Age é TEMPLATE, não dado.**
     *Produto&Planejamento · Estilo · Compras · Operações (SAC) · Marketing · Comercial*, com
     `(EX:)` em cada linha, **idêntica nos três**. 🔴 **Não formalizar como área desses clientes.**
530. ⚠ **Hering: a property `ERP/Integração` diz `Ilimitar`, o corpo da página diz `Linx`.**
     **Divergência não resolvida.** ⚠ E a Hering é `Pré Onboarding` — 5 nomes citados
     (`Jean Geard Hagen` é o único com cargo), **e nenhum e-mail em toda a página**.
     ⚠ Uma ata cita `Dayana Carla Sestrem` e o toggle cita `Day` — **não fundi**.
531. 🚨 **Quinto foco de credencial: a Camys linka uma planilha Google chamada `Acessos`.**
     **Não foi aberta.** O nome indica armazenamento de acesso. Junta-se a NK STORE, Lofty Style,
     Recco/uFlow `Credenciais` e ao YAML do uFlow (`RISC-001`). **Rotação é ação do Vinicius.**

## As Pesquisas de Satisfação — a melhor fonte de pessoa da carteira (23 set 2026)

532. 🟢 **As bases de Pesquisa de Satisfação renderam 74 respondentes NOMEADOS, todos com
     e-mail.** Osklen 32 · Lenny Niemeyer 23 · Lofty Style 19 (7 Kick Off + 12 Treinamento).
     **Nenhuma caixa funcional** — são 100% endereços nominais, ao contrário das tabelas de
     usuário. **Corpus de pessoa de cliente: 340 → 402.** Osklen 18→46 · Lenny 12→30 ·
     **Lofty Style 0→28**. 🔴 **É a fonte de pessoa de maior rendimento achada até hoje.**
533. 🔴 **A `Recco` tem a base criada e ZERO respostas.** Schema íntegro, 7 colunas, idêntico ao
     de Osklen e Lenny — e nenhuma linha. **Não é erro de acesso nem filtro: é base que nunca foi
     respondida.** ⚠ **Ressalva:** o modo SQL não aceita `is_archived`, então **linhas arquivadas
     não foram verificadas** — precisa de view mode (`view://1a7b1d38-e768-8128-882e-000c11b32668`).
534. 🔴 **As sub-páginas de perfil de acesso de Baw e Oficina Reserva NÃO têm pessoa.**
     Abertas as 5 (4 da Baw + 1 da Oficina): são exclusivamente **matrizes perfil × permissão**
     com legenda. **Zero nome, zero e-mail.** Fecha o item 523 como respondido — e negativo.
     ⚠ **E as 4 da Baw são a mesma matriz fatiada** (uma completa, uma duplicata parcial `(1)`,
     e dois recortes de perfil único). **Só a primeira precisa existir** — é o defeito de
     documento duplicado que o `START.md` § 0 proíbe.
535. 🔴 **A coluna `Área` das pesquisas é AUTO-DECLARAÇÃO, não taxonomia — é uma QUARTA
     taxonomia de área.** A mesma base traz **cargo onde deveria haver área** (*Coordenadora de
     desenvolvimento de produto*, *Modelista de Lycra*, *Assistente de estilo*), **empresa onde
     deveria haver área** (*SENAI CETIQT*, *Instituto E*, *Lofty style*) e **a mesma área em
     quatro grafias** (*Estilo*, *estilo*, *Design de moda*, *design*).
     🔴 **NÃO derivei área organizacional disso** — cada ficha registra o valor verbatim com a
     ressalva. **Normalizar é decisão.**
536. 🔴 **Terceiros no Kick Off da Osklen: 3 pessoas que não são do quadro.**
     `SENAI CETIQT` (2 pessoas, domínio `@cetiqt.senai.br`) e `Instituto E`
     (`@institutoe.org.br`). **Mesma natureza de `Qualitá` (Oficina Reserva) e do domínio
     `thela.studio` com perfil `Dono` (Mondepars).** 🔴 **Já são três casos independentes: o
     BrainHub precisa modelar TERCEIRO.** Um caso é anedota, três é padrão.
537. ⚠ **Seis e-mails com domínio divergente do padrão do cliente, reproduzidos como estão.**
     `@loftystyle.com.be` (provável `.br`), `@lennyninemeyer.com` (com *nine*),
     `@lennyniemeyer.com.br` (o resto da base é sem `.br`), e dois `@osklen.com` sem `.br`.
     **Não corrigi nenhum.** ⚠ **Isso quebra deduplicação por domínio.**
538. 🔴 **`Junior Felinto` (Lenny) respondeu com o e-mail `ivan.gouveia@lennyniemeyer.com`.**
     Nome e endereço não batem. **Pode ser resposta dada do computador de outra pessoa, ou dois
     nomes da mesma pessoa.** **Não escolhi e não fundi.**
539. ⚠ **`Gabriela Cunha` (Lofty) respondeu às DUAS rodadas com e-mails e áreas diferentes** —
     `Sourcing / compras` com `.com.br` no Kick Off (mar/2025), `Estilo` com `.com` no
     Treinamento (out/2025). **Mudança de área ou erro de preenchimento?** A segunda ficha
     colidiu no nome do arquivo e **não foi escrita** — a primeira carrega a nota das duas.
540. 🟢 **CSat medido, por cliente:** Osklen **9,78** (32 respostas, 8–10) · Lofty Treinamento
     **9,58** (12) · Lofty Kick Off **9,57** (7) · Lenny **9,48** (23, 8–10).
     ⚠ **A Lenny está em `Churn` com CSat 9,48 no Kick Off.** **Satisfação declarada no início
     não previu a saída** — vale para calibrar o que o `Health Score` deveria medir.

## Contrato virou entidade, e as receitas fora do PLM (23 set 2026)

541. 🟢 **`Contrato` passou a ser campo do cliente — não existia no BrainHub.** O template de
     `institucional.md` só tinha `Data de ativação` e `Módulos contratados`; **zero dos 48
     clientes tinham situação, vigência, reajuste ou usuários contratados.** Acrescentados ao
     `CANON` seis campos — `Situação do contrato` · `Vigência` · `Renovação e aviso prévio` ·
     `Índice de reajuste` · `Usuários contratados` · `Pendências contratuais registradas` —
     propagados para os **50** e **preenchidos em 31** com a base do Financeiro.
     🔴 **A autoridade desse bloco é a planilha do Financeiro, não o Notion** — está escrito no
     cabeçalho da seção em todos.
542. 🔺 **CORREÇÃO do item 513: `TDC` e `Tempo de Criança` são a MESMA empresa.** A razão social
     na base é *"TDC - TEMPO DE CRIANCA MODA INFANTIL"*. **Eu tinha afirmado que Tempo de Criança
     não existia no corpus. Existe, como `TDC`.** ⚠ **E as duas fontes discordam do serviço:**
     o Notion diz `Gestão de Coleção`, a base do Financeiro diz `SaaS`.
543. 🔺 **CORREÇÃO minha, apontada pelo Vinicius em 23 set 2026: `STZ` É o Studio Z.**
     Eu tinha usado a razão social *"OUZE - CALCARD S.A. - INSTIT. DE PAGAMENTOS"* para afirmar
     que eram empresas diferentes. **Estava errado** — razão social de instituição de pagamento
     não contradiz a marca. **Lição: razão social divergente é indício, não prova de entidade
     distinta.**
544. 🔴 **O PlanejAI teve DOIS clientes, não um — e perdeu um.** O campo `OBS` da Recco diz
     *"Cancelamento uPlan set/25 + uRocket fev/26"*, e `uPlan` é o PlanejAI (linhagem travada).
     **A ficha do produto registrava só a Reserva.** Corrigida. ⚠ **O cancelamento do uPlan é
     anterior ao churn da conta** — vale entender se um puxou o outro.
545. 🟢 **`Reserva` tem razão social `AREZZO INDUSTRIA E COMERCIO S.A.`** —
     **juridicamente a Reserva É a Arezzo.** 🔴 **Toca direto a pendência de grupo econômico:**
     Reserva · Oficina Reserva · Simples (by Reserva) · Arezzo são **quatro casas no corpus** para
     o que a base de contratos trata como **uma razão social**. **Decisão de modelagem.**
546. 🟢 **O gap de mentoria fechou: chama-se `EducAI` e tem 5 clientes.** Fecha o item 512.
     ⚠ **`EducAI` não é nenhuma das 16 Soluções** — o nome segue o padrão `…AI`, mas **não
     presumo que seja uma delas renomeada.** 🔴 **A Cambos é o único cliente que compra PLM e
     EducAI** — primeira conta que atravessa as duas naturezas de receita.
547. 🔴 **`Imersão IA` traz PESSOA FÍSICA como cliente — 7 das 13 linhas são nomes de gente.**
     🔴 **A hierarquia travada (`Instituição → Áreas → Subáreas → Pessoas`) não comporta isso:**
     a pessoa seria uma Instituição com 14 áreas vazias, ou uma Pessoa sem Instituição acima.
     **É decisão de arquitetura, e não é minha.** ⚠ `Stephan` e `Andreas Buttendorf` dividem
     sobrenome — não agrupei.
548. 🔴 **`RFIs` é serviço FATURÁVEL — e o corpus tem 86 delas modeladas como registro de
     trabalho.** Sete clientes compram RFI: Osklen · VIX · Puket · CAEDU · Luiza Barcelos ·
     La Moda · NK STORE. **Nenhuma ficha de RFI tem preço, escopo contratado ou aceite.**
     **Se RFI é vendida, o modelo dela está incompleto.** ⚠ **E a `La Moda` compra RFI tendo
     só `Fashion IA` na base de contratos** — ela não tem PLM.
549. 🔴 **Somando as três listas, o Financeiro fatura 15 coisas distintas.** 11 na base de
     contratos + `EducAI` · `Imersão IA` · `RFIs` · `Outros serviços`. **O corpus modela 7
     módulos e 16 Soluções. Nenhuma das três listas cobre as outras.**
550. 🔴 **18 clientes novos nas receitas fora do PLM**, incluindo porte relevante:
     **MAGAZINE LUIZA (NETSHOES)** · **GRUPO KYLY** · **DI-SANTINNI / DS FOOTWEAR / CAPODARTE** ·
     **ARAMIS** · SHOEBIZ · VITRINE · TS STUDIO · Ufo Way Denim Brasil · ETXE CONSULTORIA.
     ⚠ **`DI-SANTINNI, DS FOOTWEAR E CAPODARTE` é uma linha com três marcas** — um cliente ou
     três? **Não desmembrei.** **Criar casa é decisão.**

## O campo `Participantes` das reuniões — um negativo caro (23 set 2026)

551. 🔴 **A "melhor fonte de pessoa ativa ainda não extraída" NÃO TEM NOME.** O `AGORA.md` e o
     `_pendencias-gerais.md` vinham prometendo que o campo `Participantes` das reuniões daria
     **presença nominal com data**. **Não dá.** São **1.694 presenças em apenas 25 IDs distintos**,
     e **24 deles não resolvem** — só o João Risoléo (13 reuniões) tem nome.
     **99,2% das presenças ficam anônimas.** 🔺 **Corrijo a expectativa que eu mesmo criei.**
552. 🟢 **A não-resolução foi verificada por TRÊS vias independentes**, não uma: `get-users` com
     `user_id` (lista vazia), modo `rows` (devolve só o URI) e `notion-fetch` da página (o
     `<mention-user>` vem sem nome). 🔴 **A via está esgotada dentro da API do Notion.**
     **O workspace tem 5 pessoas no diretório; os 24 uuids são ex-membros ou convidados removidos.**
553. 🔴 **A única via que resta é humana, e é barata: abrir UMA reunião no Notion pela UI.**
     A interface renderiza avatar e nome. **Os 5 uuids de topo somam 1.489 presenças — 88% do
     total. Cinco olhadas resolvem quase tudo.** **Ação do Vinicius ou do João.**
554. ⚠ `[P]` **25 participantes para 1.162 reuniões com 47 clientes é pouco demais para ser time de
     cliente.** **Provável que `Participantes` registre o time INTERNO da uMode.** Se for,
     **esta base nunca foi fonte de pessoa de cliente** — e o corpus a tratava como se fosse.
     **Não afirmo.** Mas nenhum dos 25 aparece nas tabelas de usuário de cliente já extraídas.
555. 🟢 **O que SAIU e é novo: intensidade de atendimento por conta.** Luiza Barcelos **126** ·
     NK STORE 111 · Osklen 101 · Lofty Style 83 · Lenny 75 · Cambos 71 · NV 64 · Moda Objetiva 58 ·
     Highstil 57 · VIX 44 · Oficina Reserva 41 · Plie 38 · Recco 36 · **Caedu 35** · Vivara 34.
     **O corpus não tinha esse número para nenhum cliente.**
556. 🔴 **Cinco dos quinze mais atendidos estão em `Churn`** — Lenny (75), Highstil (57), Plie (38),
     Recco (36) e Vivara (34), **somando 240 reuniões**. ⚠ **Volume de reunião não preveniu saída**,
     assim como o CSat 9,48 da Lenny não preveniu (item 540). 🔴 **Duas métricas que pareciam de
     saúde de conta não predizem churn. Isso importa para o desenho do `Health Score`.**
557. ⚠ **A CAEDU tem 35 reuniões nesta base, mas o diário dela registra ~47 atas na página.**
     **São conjuntos diferentes, de fontes diferentes. Não os fundi e não sei o total real.**
     🔴 **Relevante: a CAEDU é o cliente-foco do teste da próxima semana.**
558. 🔺 **A base tem 1.162 linhas, não 1.161.** O corpus repetia 1.161 desde 22 set.
     ⚠ **E 86 reuniões estão SEM DATA (7,4%)** e 318 sem participante.
559. 🔴 **2023 tem 121 reuniões e o corpus nunca olhou para esse ano.** Distribuição:
     2023: 121 · 2024: 111 · **2025: 559** · 2026: 285 · sem data: 86.
560. 🔴 **O campo chamado `Pessoa` está preenchido em 2 de 1.162 linhas — 0,2%.**
     **O campo que deveria nomear gente é o menos preenchido da base inteira.**
561. 🟢 **Achado técnico reaproveitável: o SQL do conector Notion aceita `json_each()`.**
     Permite desdobrar array de `person` ou `relation` e agregar **server-side**, sem paginar.
     🔴 **Vale para o `Atendimento 2024`**, que segue travado pela mesma armadilha de relation
     (item 504). **Usar isso da próxima vez.**

## Os uModers — a Casa tinha 17 fichas e o time tem 78 (23 set 2026)

562. 🟢 **A base `uModers` do Notion foi lida: 80 linhas, 78 pessoas reais.**
     **27 ativas · 51 inativas** · 2 linhas-lixo em `Onboarding` (uma sem nome, outra com uma URL
     de Reels do Instagram no campo Nome). **O corpus tinha 17 fichas da Casa; agora tem 77.**
     🔴 **As 17 antigas NÃO foram sobrescritas** — são escritas à mão, com ressalvas curadas que
     um gerador destruiria. **Só as 60 que faltavam foram criadas**, por
     `scripts/gera-fichas-umoder.py`.
563. 🔴 **A base `uModers` NÃO TEM campo de SAÍDA.** Desligamento aparece só como
     `Situação = Inativo`, **sem data**. 🔴 **Para os 51 inativos não há como datar a saída por
     esta fonte** — e o corpus já registrava quatro saídas confirmadas pelo Vinicius (Dalker,
     Rafael Renaldim, Taís Moser, Saulo) **também sem data**. **A lacuna é da fonte, não nossa.**
564. 🔴 **`Início` está preenchido em 7 de 80** — todas contratações de 2025–2026.
     **Ninguém anterior tem data de entrada.**
565. 🔴 **A coluna `Área` da base `uModers` NÃO é a grade de 8 áreas internas.** Tem **só dois
     valores** (`Operação`, `Tecnologia`) e está preenchida em **18 de 80**. ⚠ **E a relação
     `Posições` aponta para OUTRA base, com outro campo `Área` e valores diferentes**
     (Operação, Tecnologia, Produto, Sales/Marketing, ADM/FIN, Inovação).
     🔴 **São duas taxonomias distintas — não derivei uma da outra.** **Nenhuma das duas é a
     grade de 8.** **É a terceira taxonomia de área interna.**
566. ⚠ **Senioridade não existe como campo — vive dentro do NOME da cadeira.**
     *"Sênior II"*, *"Pleno I"*, *"Pleno II"*, *"Junior"*. **Filtrar por senioridade exige
     parsear string.** **Decisão: vira campo próprio?**
567. ⚠ **Gestor/reporte não existe na base de pessoas.** Há `Líder Direto` na base de `Posições`,
     preenchido em **5 de 39**, e os IDs de usuário **não resolveram** — mesma armadilha do
     item 551. 🔴 **Não afirmo que não exista mapa de gestão: afirmo que não achei por este
     caminho.**
568. ⚠ **`Vinícius Risoleo` aparece DUAS vezes na base** — uma `Ativo`/Desenvolvedor com
     `@umode.com.br` e outra `Inativo`/Dados com `@gmail.com`. **Provavelmente a mesma pessoa em
     dois registros. Não fundi.**
569. ⚠ **Cinco pessoas sem e-mail corporativo** — Ana Flávia Maran Carrilo, Eduardo Penna,
     Filipe de Lima Kertcher e as 2 linhas-lixo. **Sem e-mail, não há chave de identidade**
     (item 252).
570. 🔴 **A base traz `T0` em volume: telefone (75 de 80), endereço residencial com CEP (53) e
     data de nascimento (57).** **Nenhum valor foi copiado** — as fichas registram que existem e
     onde. **Não há CPF, RG, salário nem senha no schema, e nenhuma credencial.**
571. ⚠ **77 das 80 sub-páginas de uModer não foram abertas.** As 3 amostradas estavam
     praticamente vazias, **mas há 2 templates na base** — pode haver conteúdo onde não amostrei.
     **Não concluo que estejam todas vazias.** ⚠ **E `Mini Bio` está preenchido em 49 de 80 e
     não foi lido** — é candidato a alimentar a seção `Personificação`.

## Os 657 `contexto-area.md` vazios — pergunta do Vinicius em 23 set 2026

572. 🔴 **97% dos arquivos de contexto de área estão praticamente vazios: 657 de 680.**
     **45 dos 49 clientes têm ZERO área preenchida.** Só quatro casas têm conteúdo:
     **Casa uMode 8/8 · CAEDU 7/14 · Osklen 7/14 · Oficina Reserva 1/14.**
     🟢 **É esperado, e não é defeito — é honestidade.** A replicação total de ago 2026 criou a
     **estrutura** das 14 áreas para os 48 clientes. O **conteúdo** de uma área (*o que ela faz*,
     *como trabalham*, *vocabulário*) **só existe se alguém varreu aquela área naquele cliente**,
     e isso só aconteceu em quatro casas. **Preencher por semelhança seria exatamente a alucinação
     que o `CLAUDE.md` proíbe.**
573. 🔴 **E a causa raiz é que a FONTE não existe.** O `contexto-area.md` de um cliente só se
     preenche com: **transcrição de reunião por área** · **mapeamento de conta** · ou a **página
     do cliente** — e a varredura de 23 set mostrou que **a página quase nunca traz área**
     (item 517: 7 de 15 clientes não têm nem o toggle `Pessoas`).
     ⚠ **Para 45 clientes, não há de onde tirar.** **Não é trabalho pendente: é fonte ausente.**
574. 🔵 **O caminho que existe é o da CAEDU, e é o teste.** As **54 transcrições** que o Vinicius
     vai trazer são exatamente a fonte que preenche as 14 áreas de um cliente.
     🔴 **Se funcionar na CAEDU, vira o método para os outros — e aí sim é trabalho, não lacuna.**
     **Enquanto não funcionar uma vez, replicar para 47 é fantasia.**
575. ⚠ **Consequência de peso no cérebro: 680 de 2.666 arquivos (26%) são área quase vazia.**
     **Um quarto do corpus é esqueleto.** 🔴 **Decisão que não é minha:** mantemos os 657 como
     `[a preencher]` (honesto, e o grafo mostra a hierarquia completa), ou só criamos o arquivo
     quando houver conteúdo (enxuto, mas o cérebro passa a mentir sobre a estrutura)?
     **Minha recomendação: manter.** Ausência declarada é informação; ausência escondida não é.
576. 🟢 **Frontmatter `aliases` aplicado a 2.665 arquivos**, gerado do H1, para a busca rápida do
     Obsidian parar de mostrar 694 nomes iguais. **Nenhum arquivo renomeado, nenhum link tocado**,
     e os quatro validadores não acusaram diferença. Travado no `CONTEXT.md`.
     🔴 **Não resolve o rótulo do GRAFO** — só um plugin de terceiro resolveria, e **recusei**:
     seria o primeiro plugin do repositório e ficaria por máquina.

## 🔺 A MEDIÇÃO DE COMPLETUDE QUE EU ERREI, e o mapa certo (23 set 2026)

577. 🔺 **ERRO MEU, grave, corrigido no mesmo dia.** Eu reportei ao Vinicius que o corpus estava
     **"6% preenchido"**, com `pessoas.md` a **0%** e `jornada.md` a **2%**. **Estava errado.**
     A métrica contava só títulos `###`, e essas duas classes usam `##`. **Os números reais:**
     `jornada.md` **67%** · `pessoas.md` **47%** · `contexto-area.md` **26%** ·
     `institucional.md` **55%** (campos de folha).
     🔴 **Eu quase fiz o Vinicius tomar decisão com número inventado por bug de medição.**
     **Lição: métrica também é afirmação técnica e precisa de evidência antes de virar relatório.**
578. 🟢 **O mapa certo do que está vazio, por CAMPO — não por arquivo.**
     **No `institucional.md`**, o que falta é dado que **não temos fonte**:
     `Receita anual` 4% · `O que fazem` 10% · `Para quem fazem` 10% · `Data de ativação` 12%
     (⚠ **a própria base do Notion só tem em 6 de 50**).
     **No `contexto-area.md`**, a camada de PESSOA já está **96%** (642 de 672) e
     `O que levar ao negócio` **100%** — o que falta é a camada **operacional**:
     `O que esta área faz` **4%** · `Como trabalham` **0%** · `Vocabulário da área` **0%** ·
     `Termos específicos` **1%**. 🔴 **Isso não sai de base nenhuma: sai de reunião e entrevista.**
     **É exatamente o que as 54 transcrições da CAEDU deveriam preencher.**
579. 🟢 **27 campos preenchidos em 20 clientes com dado que já estava na mão:**
     `Responsável de atendimento (uMode)` em 10 (do campo `Atendimento 2025` do Mapa de Clientes)
     e `Usuários da conta` em 17 (contagem real de fichas de pessoa).
     🔴 **Nenhum sobrescreveu conteúdo existente** — só preencheu onde estava `[a preencher]`.
     ⚠ **E `Usuários da conta` ganhou ressalva obrigatória:** é **pessoa documentada**, não
     **licença contratada** — os dois divergem por natureza e não se somam.
580. 🔺 **`pessoas.md` NÃO precisava ser gerado.** Eu propus gerar os 48 a partir das fichas.
     **Medindo direito: só 2 clientes têm ficha e `pessoas.md` pobre** — Hering (3 fichas, 31%) e
     Mondepars (10 fichas, 38%). **CAEDU está a 93%, NK STORE 92%, Puket 88%, Luiza Barcelos 88%.**
     **O trabalho que eu propus era de 2 arquivos, não de 48.**

## Tags no frontmatter — o filtro que faltava (23 set 2026)

581. 🟢 **RESOLVIDO — "como filtro só os clientes da uMode?"**, pergunta do Vinicius.
     Todo `.md` ganhou `tags` no frontmatter: **`tipo/` · `cliente/` · `status/` · `area/`**.
     **`tag:#status/ongoing` funciona na busca E nos grupos de cor do grafo.**
     Hoje: **1.233 arquivos em `ongoing`** · 592 `churn` · 249 `operacao-assistida` ·
     173 `sem-cs` · 108 `inativo` · 40 `pre-onboardings` · 18 `onboarding`.
     🔴 **`status/` não é inventado — sai do `### Status atual` do `institucional.md` daquele
     cliente.** Cliente sem status fica sem a tag.
582. 🟢 **Os 17 grupos de cor do grafo passaram de `path:` para `tag:#tipo/…`.** Mais preciso e
     **não quebra quando uma pasta é renomeada**. 🔺 **Isto é o que eu deveria ter entregado na
     primeira vez** — o `aliases` resolvia a busca e eu sabia que não resolvia o grafo.
583. ⚠ **O inventário de tipos revelou a forma real do corpus:** `demanda` 999 · `area` 680 ·
     `pessoa` 479 · `rfi` 86 · `indice` 60 · `institucional` 49 · `jornada` 48 · `pessoas` 48 ·
     `diario` 48 · `registro` 30 · `ferramenta` 26 · `template` 24 · `autoridade` 18 ·
     `solucao` 16 · `protocolo` 13 · `integracao` 12 · `governanca` 6 · **`outro` 4**.
     ⚠ **Os 4 `tipo/outro` são classificação que faltou** — verificar e dar tipo próprio.
584. ⚠ **A CAEDU está como `status/ongoing` no corpus, mas a base do Notion diz `Onboarding`**
     desde 22/09/2026 (itens 249 e 258). **O `institucional.md` dela não foi atualizado** — e
     agora essa divergência se propaga para as 100+ tags do cliente. **Corrigir na fonte.**

## O vault do João — o moedor já desenhado, e o que falta (23 set 2026)

585. 🔺 **CORREÇÃO minha, apontada pelo Vinicius: o CX Hub NÃO tem agente treinado.**
     Eu afirmei que `cx-meeting-transcriber` "já existe" e era "o moedor em peças". **Os quatro
     nomes do CX Hub são edge functions, não agentes com treino.** **O que existe está no vault.**
     ⚠ **Errei ao tratar nome de função como agente** — mesmo erro que o vault do João nomeia:
     *"nome de arquivo é hipótese, conteúdo é veredito"*.
586. 🟢 **O MOEDOR JÁ FOI DESENHADO.** `brainhub-seed-calls.md`, diretriz canônica assinada pelo
     João em **17/06/2026**: transcrição → **classificar tipo** → **extrair entidades** →
     **fan-out + diff por entidade** → **propostas na fila de aprovação**.
     🟢 **E resolve o ponto que eu tinha apontado como falha:** *"uma call que fala de 5 clientes
     gera 5 cruzamentos independentes, não 1 atualização"*. 🔴 **Dos 6 andares, só o 1º está feito.**
587. 🔴 **PRÉ-CONDIÇÃO que nos atinge direto (§05 do seed-calls):** o diff só funciona se o MD de
     entidade for **fato atômico e datado** — `- imersão: 10/07/2026 (fonte: PRD v1.6)` — **não
     prosa.** ⚠ **Os nossos `institucional.md` e `contexto-area.md` são prosa.**
     🔴 **Isso é trabalho nosso e é PRÉ-condição, não consequência.** **Decisão: convertemos o
     formato dos MDs de entidade para fato atômico datado?**
588. 🟢 **Os 4 treinos do `brainhub-mine` são a melhor peça reaproveitável:** `filtro-sinal`
     (durável + reutilizável + não-óbvio) · `classificador-cunho` (assunto × tipo × dono) ·
     `roteador-tier` (**fato sobre pessoa física assume o tier mais restritivo e escala**) ·
     **`juiz-contradicao`** (refino/atualização/**contradição nunca decide, enfileira**).
     **Política em MD editável, fora do código, saída contratada em JSON.**
589. 🔴 **Existe matéria-prima parada: 206 transcrições no Drive** (pasta `Tactiq Transcription`,
     esteira morta há 24 dias em 02/09) **e 598 áudios de WhatsApp nunca transcritos.**
     ⚠ **E 16 jobs estão pausados desde 09/08 por decisão do João — 0 ativos.**
     **Não falta fonte. Falta esteira ligada.**
590. 🔴 **O que NINGUÉM construiu, e é exatamente o pedido do Vinicius:** **nada cria Demanda,
     RFI ou Atividade a partir de reunião.** As saídas previstas param em **task, e-mail e
     atualização de MD**. 🔴 **E não há roteamento para PESSOA nem para ÁREA de cliente** — as
     rotas vão a categoria. **Nenhuma peça conhece a hierarquia `Instituição → Áreas → Pessoas`.**
591. 🟢 **A complementaridade é clara: o vault tem o MOTOR, nós temos o ENDEREÇO.**
     Eles têm os treinos, o classificador com loop de feedback, a fila de aprovação real
     (`brainhub-approval-bridge`) e a governança de heartbeat/evidência. **Nós temos 479 fichas
     de pessoa com e-mail, 48 clientes com status, 680 áreas e a hierarquia travada.**
592. ⚠ **A branch `origin/governance/brainhub-v1.5` (14/09) tem 12 skills que o `main` não tem**,
     incluindo `brainhub-approval-bridge`, `onde-mora-cada-coisa`, `padrao-cliente` e
     `curadoria-por-conteudo`. **Nosso clone está 3 dias atrás.** ⚠ **Ler antes de desenhar.**
593. 🟢 **A governança de agente do vault é dura e vale copiar o princípio:** agente escreve
     **só no próprio inbox**, nunca em canônico · **front-matter obrigatório, sem ele é intruso** ·
     **heartbeat** (*"nada roda sem batimento"* — dois jobs morreram e ninguém soube por 5 semanas)
     · **evidência** (*"exit 0 não é prova de trabalho"* — um job falhava em 10 de 10 repos com
     heartbeat verde) · **Guarda determinística por script, não por LLM**.
594. 🚨 **Higiene de segredo no vault, registrada por referência:** o `DECISOES.md` da raiz cita
     **senha em texto claro** de um repositório de proposta, e a skill `discord-intake` aponta o
     **caminho de um token de bot**. 🔴 **Nenhum valor foi lido ou copiado.**
     ⚠ **É higiene do vault do João, não nossa** — mas soma aos 5 focos já conhecidos aqui.

## A camada de fato atômico, e a identidade que não fecha (23 set 2026)

595. 🟢 **A camada de fato existe: 826 fatos em 49 `institucional.md`**, no formato
     `- chave: valor — [fonte · data]`, com **26 chaves de vocabulário fechado** travadas no
     `protocolo-fato-atomico.md`. **É o alvo do cruzamento que o item 587 exigia como
     PRÉ-condição.** Dono: `scripts/gera-fatos.py`. Guarda: `scripts/valida-fatos.py`.
596. 🔴 **A decisão que eu tomei e que precisa de aval: fato NÃO substitui prosa, convive com
     ela.** Converter os MDs em lista de fatos destruiria o que eles têm de melhor — a call de
     Sales da Luiza Barcelos diz *"processo está na cabeça da Marcinha"*, com dono e data, e
     nenhum `- processo-concentrado: sim` preserva isso. **Prosa para pessoa, `## Fatos` para
     máquina.** ⚠ **Se o Vinicius discordar, é aqui que se reverte** — e é barato, porque o bloco
     é gerado.
597. 🔴 **399 dos 826 fatos (48%) saem `[sem fonte]`.** Não é defeito do gerador: é o corpus
     declarando lacuna em vez de escondê-la. **Mas metade do cérebro não tem procedência**, e o
     juízo de contradição precisa de data para decidir o que é mais recente. **Fato sem data é
     opinião** (protocolo § 2).
598. 🔴 **NENHUM dos 49 valores de `atendimento` resolve para e-mail. Zero.** É o bloqueio
     concreto do agente generalizado, e tem **duas causas distintas**:
     **(a)** o campo `Atendimento` do CRM guarda **primeiro nome**: `Laura` (7×), `Fernanda` (3×),
     `Julianne + Pedro` (4×), `Julianne & Pedro` (2×). **Primeiro nome não é identidade** — já
     erramos com duas `Cristina` na NK STORE e com `Day` × `Dayana Carla Sestrem`.
     **(b)** os **3 nomes completos** que aparecem — `Julianne Dias Rodrigues`, `Pedro Murillo`,
     `Andrea Goulart Holmer dos Santos` — **têm ficha, e a ficha não tem e-mail.**
599. 🔴 **19 pessoas da Casa não têm e-mail na ficha** (58 de 77 têm). São elas:
     `ana-flavia-maran-carrilo` · `andrea-goulart-holmer-dos-santos` · `dalker-walter` ·
     `eduardo-penna` · `elizabeth-alves-de-souza-santana` · `fernanda-araujo` ·
     `filipe-de-lima-kertcher` · `joao-paulo-contar-risoleo` · `juliana-ferre-esteves` ·
     `julianne-dias-rodrigues` · `laura-delgado-cardoso` · `marina-goncalves-santoro` ·
     `pedro-murillo` · `rafael-del-gaudio-renaldim` · `sandro-costa` · `saulo` · `tais-moser` ·
     `vanessa-rinaldi-ornelas-engman` · `victor-aragao`.
     ⚠ **Elas vieram do CRM, não da base `uModers`** — por isso o `gera-fichas-umoder.py` não as
     alcançou. **São exatamente as donas de relacionamento com cliente.**
     🔴 **A Julianne é a Key Account da CAEDU, que é o cliente do teste da semana que vem.**
600. 🔴 **7 clientes têm `SMB` no campo `Responsável de atendimento`** — segmento, não pessoa.
     É dado errado **na origem**, e o corpus o carrega fielmente. **Corrigir no Notion ou tratar
     na entrada?** É decisão do Atendimento, não minha.
601. ⚠ **Achado de método, custou três voltas:** eu fiz o gerador fatiar o campo `atendimento`
     por vírgula e " e " quando não havia lista. Saíram fatos chamados **`lido`, `isso`, `SMB`,
     `que`** — **lixo com cara de identidade, que é pior do que não resolver.**
     🔴 **Regra que fica: não se quebra prosa em entidade.** Sem lista explícita, o valor sai
     inteiro e a identidade fica declaradamente aberta. **Era a regra que eu mesmo escrevi na
     docstring do script e violei na implementação.**
602. 🟢 **A resolução por e-mail é generalizada e foi verificada: 617 nomes indexados**, montados
     do próprio corpus, **sem um único nome de pessoa no código.** ⚠ **Isso rejeita o desenho do
     `roteador-tier` do vault**, que tem `joao` como dono fixo — um agente que só sabe rotear
     para uma pessoa não roteia para a Julianne nem para quem entrar amanhã.

## A identidade fechou — e o que ficou aberto (23 set 2026)

603. 🟢 **Achei a base de pessoas que faltava, e ela NÃO é a `uModers`.** É
     `collection://c82a689c…` — **a mesma que o campo `Atendimento 2024` do `Mapa de Clientes`
     aponta.** Traz `Email`, `Função`, `Área` e `Situação`. **Duas bases de pessoa da Casa
     convivem no mesmo workspace do Notion, e o corpus só conhecia uma.**
     ⚠ **É por isso que o `gera-fichas-umoder.py` não alcançava as 19** — ele lê a outra.
604. 🟢 **16 das 19 fichas da Casa sem e-mail foram preenchidas** por
     `scripts/preenche-email-casa.py`. 🔴 **A CAEDU agora resolve ponta a ponta:**
     `atendimento: pessoa:julianne.dias@umode.com.br` · `pessoa:pedro.murillo@umode.com.br` ·
     `pessoa:andrea.holmer@umode.com.br`. **Era o bloqueio do item 598.**
     ⚠ **`T0` não entrou:** a base traz telefone, endereço com CEP e data de nascimento de todos.
     **Nenhum copiado** — registro que existem e onde.
605. 🔴 **`Andrea Goulart Holmer dos Santos` está `Inativo` na base de pessoas** e segue listada
     como Consultor de Negócios da CAEDU no `institucional.md`. **Ou saiu e o corpus não soube,
     ou a base está defasada.** 🔴 **É o cliente do teste da semana que vem.**
606. 🔴 **3 pessoas da Casa não têm e-mail NA ORIGEM** — `ana-flavia-maran-carrilo` (Ativo) ·
     `eduardo-penna` (Inativo) · `filipe-de-lima-kertcher` (Freela, campo vazio).
     **Não é lacuna nossa: é lacuna da base.** A Ana Flávia está **Ativo** e sem e-mail.
607. 🔴 **9 valores de `atendimento` ficam AMBÍGUOS e eu não escolhi** — é o comportamento que o
     protocolo exige, não uma falha:
     **`Pedro` (6 clientes)** → `Pedro Murillo` (Analista de Relacionamento, Ativo) ou
     `Pedro Victor Silva` (Designer, Inativo)?
     **`Fernanda` (3 clientes)** → `Fernanda Araujo` (Head de Design e UX, Ativo) ou
     `Fernanda Martins` (Inativo)?
     ⚠ **Pelo cargo, o palpite seria óbvio nos dois casos. Palpite não é identidade** — é a
     mesma raiz de `STZ` × `Studio Z` e das duas `Cristina` da NK STORE. **Quem confirma é o
     Atendimento.**
608. 🔴 **O campo `Atendimento 2025` do `Mapa de Clientes` é `select`, não `relation`** — cinco
     opções fixas: `SMB` · `Laura + Paulinha` · `Julianne` · `Fernanda` · `Pedro`.
     🔴 **Um `select` de texto livre JAMAIS vai resolver para pessoa.** Enquanto for `select`,
     toda varredura futura vai reencontrar o mesmo problema.
     🟢 **`Atendimento 2024`, ao lado, JÁ É `relation` para a base de pessoas certa.**
     ⚠ **A correção é no Notion, não aqui: `Atendimento 2025` deveria ser `relation` também.**
     **É uma mudança de schema de terceiro — decisão do Atendimento.**
609. 🔴 **Quem é `Paulinha`?** Aparece só em `Laura + Paulinha`, opção do `select`, e **não existe
     na base de pessoas nem no corpus.** ⚠ **Não é a `Paula Dorsch` (Inativo, Marketing)** — não
     afirmo que seja, é indício de apelido, não prova.
610. 🔴 **7 clientes têm `SMB` no campo de atendimento** — segmento, não pessoa. Confirma o
     item 600 com a leitura do schema: **é valor válido do `select`**, ou seja, **a origem
     permite, por desenho, preencher responsável com um segmento.**

## Os dois fatos sem fonte da CAEDU — e o que a busca encontrou no caminho (23 set 2026)

611. 🟢 **A CAEDU está com ZERO fatos `[sem fonte]`.** Os dois que restavam — `receita-anual` e
     `data-ativacao` — **não foram preenchidos: foram VERIFICADOS como ausentes**, e agora dizem
     onde se procurou e quando: `? — [não consta em: base Mapa de Clientes · 2026-09-23]`.
     🔴 **É formato novo, travado na § 2.1-bis do `protocolo-fato-atomico.md`.** A diferença
     importa para o cruzamento: `[sem fonte]` significa *ninguém procurou*; `[não consta em: X]`
     significa *procurou-se em X, naquela data, e estava vazio* — então o que a transcrição
     trouxer é **NOVO**, não conflito.
612. 🟢 **Achei um acervo que o corpus não sabia que existia: exports CSV das bases do Notion
     dentro do vault do João**, em `BrainHub/uMode/.../notion/`. O `Mapa de Clientes.csv` é de
     **04/03/2026** e tem **colunas que a base viva não expõe** — `Quantidade de Lojas`,
     `Acessos contratados`, `Departamento`, `Portal do Cliente`, `OKRs`, `Onde Estamos`,
     `Sucesso do Cliente`, `O que falta` e **`Fashion AI - Escopo Geral` / `Fashion AI -
     Integração`**. 🔴 **`Fashion AI` era o termo que o item registrou como tendo ZERO ocorrência
     no corpus** — ele existe como CAMPO da base, não só como serviço faturado.
613. 🔴 **`Receita Anual` está preenchida em 2 dos 49 clientes** — Luiza Barcelos (350.000.000) e
     NK STORE (144.000.000). **`Data Ativação Cliente` em 6. `Quantidade de Lojas` em 5.**
     ⚠ **Não é lacuna da Caedu: é campo que a operação não preenche.** Cobrar por cliente é
     perder tempo; a decisão é se esses campos devem existir.
614. 🔴 **A referência "~R$ 1 bi (2023), 100+ lojas, CEO Edson Salles" continua sem fonte
     localizável.** O corpus a atribui ao *CRM de mentoria no vault do João*. **Procurei por
     `Edson Salles`, `1 bi` e `100+ lojas` na árvore do vault e no histórico do Git dele: zero.**
     ⚠ **O clone tem 1 branch local contra 19 remotas** — pode estar em branch não baixada.
     🔴 **Escrevo "não encontrei ali", não "não existe".** Quem confirma é o João.
615. 🔺 **Corrigi um erro do próprio corpus.** A ficha `api-caedu.md` dizia *"`Ativo desde` está
     corrompido na fonte: `05/10/2022`"* — e **três outros arquivos usavam essa data como fato**.
     🟢 **A linha está bem-formada.** A corrupção é real, mas em **13 OUTRAS linhas**: ano `0202`
     em vez de `2022` (9 casos), ano truncado `20` (2) e sufixo ` 1` (2). **Erro de digitação na
     origem — corrigir lá, não aqui.**
616. 🟢 **A data de ativação da CAEDU está CERCADA por duas fontes independentes que concordam:**
     contrato assinado em **23/06/2022** e conta `api-caedu@umode.app` ativa desde **05/10/2022**
     (a linha mais antiga da tabela, com folga — a seguinte é de 05/05/2023).
     ⚠ **Não promovi nenhuma das duas a `data-ativacao`:** contrato assinado e conta de serviço
     criada **não são** o campo comercial. **A janela está entre jun e out de 2022; o valor exato
     segue sem fonte.**
617. 🔴 **Nenhum usuário novo na CAEDU desde 16/07/2024** — janela medida na tabela de usuários
     (94 linhas de pessoa): mais antiga 05/10/2022, mais recente 16/07/2024. **E a conta está em
     `Onboarding` com o CAEDU 2.0 em montagem.** ⚠ **Dois anos sem entrada de usuário numa conta
     que está reimplantando** é sinal que o teste da semana que vem devia olhar.
618. 🔴 **137 ocorrências de "campo vazio na base" no corpus NÃO dizem QUAL base**, em **44 dos 49
     clientes**. 🔴 **Ausência sem fonte nomeada não é ausência citável** — vira `[sem fonte]`, e
     o agente não sabe se alguém chegou a olhar. **Só a CAEDU nomeia (2 ocorrências).**
     ⚠ **É trabalho de varredura, um cliente por vez: abrir a base, confirmar o vazio, nomear.**
619. ⚠ **`Grupo 3` mudou de nome e isso explica documentos antigos.** O export de 04/03/2026 diz
     **`Grupo 3: Potenciais Clientes`**; a base viva diz **`SMB`** (WIP Estratégico 1,75 · WIP
     Time 10 · 15 clientes). **Não é contradição do nosso fato — é renomeação.** Mas quem ler um
     documento de março vai achar que são coisas diferentes.
620. ⚠ **O export de março lista `Módulos contratados: uFlow` para a Caedu; a base viva lista
     quatro módulos funcionais** (Gestão de Coleção, Integração, Relatórios, Fornecedores).
     🔴 **Confirma que a taxonomia de módulo mudou de nome-de-produto para funcional** entre
     março e setembro de 2026 — e **nenhuma das duas listas é "a certa": são instantes diferentes.**

## A camada de fato chega às áreas e à jornada (23 set 2026)

621. 🟢 **O `## Fatos` saiu de 49 arquivos para 769.** Cobria só `institucional.md`; agora cobre
     também **`jornada.md` (48)** e **`contexto-area.md` (672)**. **3.393 fatos**, 35 chaves de
     vocabulário fechado. 🔴 **Era pré-condição do moedor:** uma transcrição da Julianne fala de
     **área** e de **pessoa**, e até agora não havia superfície de cruzamento nesses arquivos.
622. 🟢 **A tabela `Marcos da jornada` já era fato atômico e ninguém tinha visto.** As colunas são
     `Quando | Marco | Fonte` — **data, valor e procedência, por linha, escritas à mão.**
     A CAEDU rendeu **20 marcos com fonte e data individuais**, de 05/10/2022 a 14/08/2026.
     ⚠ **O mesmo vale para a tabela `Procedência deste documento`**, que mapeia bloco → fonte →
     data: passou a ser a procedência **por chave** do `contexto-area.md`, em vez de herança de
     cabeçalho. **É procedência que o corpus escreveu, não heurística minha.**
623. 🟢 **Data parcial passou a ser permitida:** a fonte diz *"set/2023"*, o fato diz `2023-09`.
     **Completar o dia seria inventar; descartar o mês seria perder precisão que a fonte tem.**
     Protocolo § 2 e `valida-fatos.py` atualizados juntos.
624. 🟢 **CAEDU: 142 fatos em 16 arquivos, 78% com procedência.** 🔴 **Os 31 `[sem fonte]` estão
     concentrados nas 7 áreas sem perfil de acesso no PLM** — PCP, Logística, Comercial,
     Marketing, Financeiro, Design e Engenharia, **3 fatos cada, todos vazios.**
     ⚠ **Não é ruído espalhado: é a mesma raiz já registrada.** Ou a área não existe na Caedu, ou
     existe e não usa o PLM — **e essa pergunta agora tem consequência medível.**
625. 🔴 **No corpus inteiro, 66% dos fatos saem `[sem fonte]`** (2.232 de 3.393). ⚠ **A queda de
     50% para 66% é efeito de cobertura, não de piora:** os 672 `contexto-area.md` entraram quase
     todos vazios. **É a medida honesta de quanto do cérebro ainda não tem procedência.**
626. 🔺 **Três defeitos meus, achados pelos próprios dados antes de commitar:**
     **(a)** eu mapeava a coluna `Situação` / `Validação que a controla` como **fonte** — não é:
     descreve a entrega, não diz de onde veio. **Tratar coluna assim como fonte é mentir.**
     **(b)** o cortador de seções só lia `##`, e as **Dores vivem num `###`** dentro de
     `## Padrões operacionais` — perdia todas.
     **(c)** linha de tabela herdava o cabeçalho do documento; **as entregas de um `jornada.md`
     não vieram da base que atualizou o cabeçalho.** Agora tabela sem coluna de fonte e sem
     blockquote sai `[sem fonte]`.

## As 7 áreas vazias da CAEDU — havia material, e eu não tinha ido buscar (23 set 2026)

627. 🔺 **Eu tratei "sem perfil de acesso no PLM" como "sem fonte" e parei. Era hipótese, não
     conclusão.** Faltava abrir o `Mapeamento de Contas - Caedu` (04/04/2025) — **a mesma fonte
     que alimentou as 7 áreas preenchidas.** 🟢 **As 7 áreas estão preenchidas.**
628. 🟢 **E o que a fonte diz é melhor que conteúdo: ela declara o próprio escopo.**
     > *"**Não incluso**: aspectos de contabilidade, faturamento, e dados de pedidos sensíveis
     > (planilhas externas)."* — § 2.2
     🔴 **Isso não é ausência de fonte: é EXCLUSÃO DECLARADA, com data e autor.** Uma área fora
     do escopo por decisão registrada vale muito mais, no cérebro, que um `[a preencher]` mudo.
629. 🟢 **O mapeamento cobre SEIS processos** — Planejamento, Estilo, Importação, Modelagem,
     Produto Nacional e Qualidade. As 7 áreas ou foram excluídas de propósito, ou têm a função
     **absorvida** por um desses seis:
     · **`11_Financeiro`** — excluída por decisão. Único tema que aparece: *"cálculo de margens
       e tags de licenciamento — **sem dashboard consolidado**"* (§ 4.3).
     · **`09_Comercial-Vendas`** — negociação e pedido **fora do uMode, em planilhas sensíveis**
       (§ 4.4); há ação aberta de 6 semanas para reavaliar (§ 5.2).
     · **`07_Logistica-CD`** — aparece **só como destino**: *"antes do envio a lojas"* (§ 4.2.6).
     · **`05_PCP`** — função distribuída entre Modelagem, Produto Nacional e Qualidade; o que
       falta é **relatório de tempo entre etapas** (§ 4.3).
     · **`10_Marketing`** — SEO, VM e e-commerce são produzidos por **`02_Estilo-Criacao`**
       (§ 4.2.2), e a dor registrada é de **subuso**, não de área ausente.
     · **`12_Design`** e **`14_Engenharia`** — 🔴 **não nomeadas em fonte nenhuma.** Escrevi
       *"não encontrada"*, não *"não existe"*. **Não afirmei que Design seja Estilo com outro
       nome** — é hipótese para o atendimento confirmar.
630. 🔴 **`Importação` e `Produto Nacional` são etapas do processo da Caedu que NÃO cabem nas 14
     áreas canônicas.** Mesmo padrão de `Atelier`, `Estamparia`, `Oficina`, `Fábrica` e
     `Merchandising` em outros clientes. **É o sexto e o sétimo caso — o limiar já passou.**
631. 🔺 **Defeito grave que o preenchimento expôs: eu estava FABRICANDO fonte em 51 fatos.**
     O padrão `Financeiro` da tabela de fontes casava com o texto da **área `11_Financeiro`**,
     e o gerador atribuía a ela *"planilha de contratos do Financeiro"* — **fonte que nunca
     tocou aquele dado.** 🔴 **Palavra comum não pode ser pista de fonte.** Corrigido: só casa
     acompanhada de `contratos` ou `planilha`.
632. 🟢 **`[a preencher]` com procedência declarada virou ausência verificada.** Quando a tabela
     `Procedência` nomeia o bloco que responde pela chave — *"Ausência de perfil de acesso e de
     pessoas → tabela de usuários do PLM · 21/09/2026"* — isso É *"procurei ali e não há"*.
     **Ausência verificada no corpus: 2 → 149.**
633. 🟢 **CAEDU: 142 fatos, ZERO `[sem fonte]`.** 82% com fonte nomeada, 18% ausência verificada.
     🔴 **É o primeiro cliente do corpus com a camada de fato inteiramente rastreável.**
634. ⚠ **A tabela `Histórico de incidentes` não tinha coluna `Fonte`** — a de `Marcos` tem.
     Acrescentei na Caedu. 🔴 **Tabela que carrega fato e não carrega fonte produz fato órfão**,
     e isso vale para os outros 47 clientes que têm a mesma tabela sem a coluna.
635. 🔴 **Próximo alvo óbvio: os outros clientes têm `Mapeamento de Contas`?** O da Puket é
     citado no próprio documento da Caedu (*"no mesmo padrão que empregamos para Puket"*).
     ⚠ **Se existir um por cliente, é a fonte que preenche `contexto-area.md` em escala** — hoje
     62% dos fatos do corpus saem `[sem fonte]`, quase todos vindos de áreas vazias.

## Puket preenchida, e a ausência nomeada em escala (23 set 2026)

636. 🔴 **Só DOIS clientes têm `Mapeamento de Contas`: Puket e Caedu.** Varri o índice inteiro da
     `Documentação CX` — são 30 documentos, e a página-mãe `Mapeamento de Contas` tem cinco
     filhos: Puket, Caedu, a análise comparativa das duas, `Devolutivas para Sandro` e
     `Indicadores e Rotinas`. **A rota que preencheu a Caedu NÃO escala para os 48.**
637. 🟢 **Puket saiu de ZERO para 92 fatos, 74% com fonte.** As 14 áreas estavam todas vazias
     (11–12 `[a preencher]` cada, só boilerplate). **13 têm conteúdo agora**, e é conteúdo com
     gente e ferramenta nomeadas: Design é a **Mariana** e trabalha *"Email + Pasta em Drive,
     **fora do uMode**"*; Produto é a **Cátia**, com planilha de **37 campos**; Modelagem é o
     **Rodrigo**, e `Tabelas de Medidas` *"não é usado consistentemente"*.
638. 🔴 **A dor central da Puket está registrada e é grave:**
     > *"Um dos pontos-chave, porém **pouco utilizado no uMode**. O time troca e-mails, faz
     > **PPTs de 100 páginas**, mas **não registra no sistema as aprovações**."*
     ⚠ **E o risco é nomeado:** *"A diretora (Andrea) tem baixa visibilidade sobre relatórios,
     **gerando risco de churn**."* **A conta está `Ongoing` hoje.**
639. 🔴 **Ressalva de procedência que não pode se perder: o mapeamento da Puket é SÍNTESE DE IA.**
     O documento se declara *"seguindo análise do Chat GPT"* e *"exemplo de documento... a ideia
     é ILUSTRAR"*. **É síntese sobre três transcrições reais** (26/02, 06/03 e 13/03 de 2025),
     assinada por Rafael. 🔴 **Não é fonte bruta, e o que vier das transcrições prevalece.**
     ⚠ **Marquei isso em cada bloco escrito e na tabela de procedência.**
640. 🟢 **A própria área da Puket já dizia o que fazer, e ninguém tinha feito.** Havia uma seção
     `### 🔴 Próxima fonte a varrer para esta área` apontando literalmente o
     `Mapeamento de Contas - Puket`. **Foi varrida; a nota virou `🟢 Fonte varrida em 23/09/2026`.**
     ⚠ **Vale checar essa seção nos outros 47 clientes** — pode haver mais fonte apontada e não lida.
641. 🟢 **108 ausências nomeadas em 43 clientes**, por `scripts/nomeia-ausencia-verificada.py`.
     O item 618 registrou 137 ocorrências de *"campo vazio na base"* sem dizer QUAL base.
     Agora dizem: **base `Mapa de Clientes`, lida por SQL em 23/09/2026 e conferida no export de
     04/03/2026.** 🔴 **Ausência verificada no corpus: 2 → 282.**
642. 🟢 **E os números da base fecham o argumento:** `Receita Anual` preenchida em **2 de 49**,
     `Data Ativação` em **6**, `Setor da Empresa` em **12**, `CNPJ` em **8**, `Razão Social`
     em **7**. 🔴 **Não são lacunas de cliente: são campos que a operação não preenche.**
     ⚠ **A decisão não é "cobrar cliente a cliente" — é se esses campos devem existir.**
643. 🟢 **O script acusa o caso inverso e não encontrou nenhum:** nenhum cliente tem dado vivo na
     base com o MD dizendo vazio. ⚠ **Se houvesse, eu NÃO sobrescreveria** — sobrescrever
     esconderia dado real. **A regra está no script.**
644. 🔺 **Meu regex pegou 11 de 137 na primeira tentativa.** A forma dominante do corpus é
     `**campo vazio na base**`, com o negrito abrindo **antes** de "campo", e eu só previa
     negrito em volta de "vazio". 🔴 **Medi as quatro formas reais antes de corrigir, em vez de
     supor a quinta** — está documentado no próprio script.

## A Oficina Reserva apontava a fonte e ninguém tinha lido (23 set 2026)

645. 🔺 **Catorze `contexto-area.md` da Oficina Reserva traziam uma seção `### 🔴 Próxima fonte a
     varrer para esta área` apontando literalmente `Perfil de Usuário e Permissionamentos
     OFICINA`.** 🔴 **Estava escrito o que fazer, e ninguém tinha feito.**
     ⚠ **21 arquivos do corpus têm essa seção** — 14 da Oficina e 7 da Puket. **As duas foram
     varridas hoje. Não há mais fonte apontada e não lida.**
646. 🟢 **A matriz de perfis SUBSTITUI uma fonte que o próprio corpus marcava como fraca.**
     O `institucional.md` da conta dizia: *"esta conta não tem lista de times, nem tabela de PLM
     varrida, nem pesquisa. O que existe são **funções citadas dentro das dores**. Fonte fraca,
     e declarada como tal."* 🟢 **Agora há oito perfis nomeados, com permissão campo a campo.**
     ⚠ **Não apaguei a tabela fraca** — marquei qual prevalece e deixei a anterior como histórico.
647. 🔴 **`Oficina - Qualitá` é perfil de EMPRESA EXTERNA dentro da conta do cliente.**
     A Qualitá audita a qualidade da Oficina Reserva e **tem perfil próprio no PLM**.
     🟢 **Confirma com fonte forte o que era indício fraco** (*"auditoria de qualidade — feita
     pela Qualitá, empresa externa"*, tirado de uma dor). ⚠ **É o primeiro caso conhecido de
     terceiro com acesso ao PLM de um cliente** — tem implicação de permissionamento e de LGPD
     que o corpus não modela.
648. 🔴 **`Oficina - Ecommerce Marketing` é UM perfil para DUAS áreas canônicas.**
     **Não dá para atribuir trabalho por área nesta conta** — o perfil de acesso não separa
     `08_Ecommerce-Cadastro` de `10_Marketing`. ⚠ **É o padrão "alias não cabe na grade", agora
     em PERMISSÃO e não em nome de time.**
649. 🟢 **Engenharia existe de verdade aqui, e isso contrasta com Caedu e Puket.** Na Oficina é
     **bloco da ficha de produto com três abas** — `Tamanhos e Medidas`, `Aprovações` e
     `Engenharia`. 🔴 **Nas outras duas contas, Engenharia não é nomeada em fonte nenhuma.**
     ⚠ **Perfil de acesso e área canônica não são a mesma coisa** — e esta conta prova: sete
     áreas não têm perfil, mas Engenharia tem estrutura de produto.
650. 🔴 **Oito funcionalidades estão desligadas para TODOS os oito perfis:** `Lotes` ·
     `Tabela Dinâmica` · `Coordenado` · `Estampa` · `Composição de Custo` · `Tag` ·
     `Tipo de Lote` · `Pack`. ⚠ **É decisão de conta, não de área** — e vale perguntar se é
     escolha ou se é funcionalidade que a conta não contratou.
651. 🔴 **A conta cita DOIS ERPs.** `Novos Produtos ZZNet` é **SAP Interface 1** e
     `Atualização de Produtos` é **SAP Interface 3** — e há uma aba `Integração Linx` na ficha,
     restrita a três perfis. ⚠ **Confirmar qual é o ERP vigente e o que a outra integração faz.**
652. ⚠ **`Oficina - Compras` está marcado para desaparecer:** *"provavelmente no novo formato da
     Oficina não teremos mais o Perfil de compras. Por hora, seguimos com esse perfil ativo."*
     **Registrado como estado de transição, com a citação.**
653. ⚠ **Dois perfis com nomes quase iguais e papéis diferentes:** `Oficina - Planner`
     (privilegiado, transversal) e `Oficina - Planejamento` (operacional, edita a aba
     Planejamento). 🔴 **É armadilha de leitura** — igual a `Pedro Murillo` × `Pedro Victor`.
654. 🟢 **Estado da camada de fato nos três clientes varridos a fundo:**
     · **Caedu** — 142 fatos, **0 `[sem fonte]`**, 82% com fonte
     · **Puket** — 92 fatos, **0 `[sem fonte]`**, 74% com fonte
     · **Oficina Reserva** — 88 fatos, 11 `[sem fonte]` (institucional e jornada), 55% com fonte
     🔴 **Corpus inteiro: 1.138 com fonte (34%) · 299 ausência verificada (9%) · 1.943 `[sem fonte]` (57%).**

## Oficina Reserva zerada — e uma dúvida de identidade de cliente (23 set 2026)

655. 🟢 **Oficina Reserva chegou a ZERO `[sem fonte]`** — 88 fatos, 63 com fonte, 25 ausência
     verificada. **Três clientes agora estão inteiramente rastreáveis: Caedu, Puket e Oficina.**
656. 🔴 **`Oficina Reserva` NÃO consta na base de contratos do Financeiro.** Conferi os **41
     registros um a um**. ⚠ **A base tem `Reserva`** — que o corpus trata como cliente distinto,
     com pasta própria e serviços próprios (`uFlow` · `uBuy` · `uPlan`).
     🔴 **Não afirmo que sejam a mesma conta nem que sejam diferentes.** É exatamente o tipo de
     confusão de `STZ` × `Studio Z`, em que eu errei e o Vinicius corrigiu.
     **Quem confirma é o Financeiro — e até lá todo campo de contrato da conta fica sem valor,
     com a ausência declarada.**
657. 🔺 **Quase li um dado como outro.** A seção `Receita anual` da Oficina dizia *"a mensagem de
     Sales diz **'não haverá valor adicional'**"*. 🔴 **Isso é sobre cobrança da uMode, não sobre
     a receita do cliente.** São coisas diferentes, e o MD as colocava no mesmo campo.
     **Separei as duas com a ressalva escrita.**
658. 🟢 **A chave `entrega` passou a reconhecer bloco de `escopo` na tabela de procedência.**
     Vários `jornada.md` declaram o que foi prometido dentro de *"escopo acordado"*, não numa
     seção chamada "entregas" — e as 5 entregas da Oficina vinham da **mensagem do João no grupo
     de Sales, de 26/06/2024**, sem que o gerador soubesse ligar.

## Luiza Barcelos, NK STORE e Osklen — e a procedência em escala (23 set 2026)

659. 🟢 **SEIS clientes com ZERO `[sem fonte]`:** Caedu (142 fatos), NK STORE (107), Puket (92),
     Luiza Barcelos (92), Osklen (90), Oficina Reserva (88). **São os três mais atendidos da
     carteira mais os três já varridos.**
660. 🟢 **Corpus inteiro saiu de 57% para 10% `[sem fonte]`.** 3.396 fatos: **1.325 com fonte
     (39%) · 1.717 ausência verificada (51%) · 338 sem fonte (10%)**. ⚠ **Metade do cérebro é
     ausência DECLARADA** — sabe-se onde se olhou e quando. **Isso não é conteúdo, mas é o
     oposto de silêncio.**
661. 🔺 **ERRO MEU, corrigido antes de commitar: fabriquei procedência em 672 linhas.** Detectei
     "cliente tem tabela de usuários" testando se `pessoas-da-area` tinha valor — e o valor
     dominante é **`Nenhuma`**, que significa *"esta área não tem gente"*, não *"o cliente tem
     tabela"*. 🔴 **Escrevi "tabela de usuários do PLM" como fonte em 48 clientes, inclusive nos
     que não têm tabela nenhuma.** ⚠ **É o mesmo defeito do padrão `Financeiro` que fabricava
     fonte em 51 fatos: pista fraca virando afirmação de procedência.**
     🟢 **A detecção certa é contagem NUMÉRICA, e devolve 4 clientes — não 48.**
662. 🔺 **Segunda correção de honestidade, 529 áreas em 39 clientes.** A seção `Pessoas desta
     área` dizia **"Nenhuma."** — o que afirma que a área não tem gente. 🔴 **Não sabemos isso.**
     Sabemos que não há tabela de usuários nem pesquisa cobrindo aquela conta.
     **Ausência de fonte não é ausência de pessoa** — e o MD dizia uma pela outra.
663. 🟢 **NK STORE tem a tabela de usuários mais rica lida até hoje: 29 pessoas em 5 perfis**, com
     `Departamento NK` e estado de convite. `NK - Estilo` **10** · `NK - PCP` **7** ·
     `NK - Compras` **5** · `NK - Modelagem` **4** · `NK - Admin` **3**.
     ⚠ **26 convites aceitos, 2 pendentes desde dez/2024, 1 inativo, 4 marcados `INATIVAR`.**
664. 🔴 **Na NK STORE, perfil da matriz e perfil da tabela de usuários NÃO coincidem.** A matriz
     usa `NK- Estilo Master` (sem espaço), `Nk Compras Master`, `NK Compras`, `Nk Modelagem`,
     `NK - Time`, `Fornecedor`. A tabela usa `NK - Estilo`, `NK - PCP`, `NK - Compras`,
     `NK - Modelagem`, `NK - Admin`. **Só `NK - Admin` bate literalmente.**
     ⚠ **São duas taxonomias e a fonte não diz o mapa. Não conciliei.**
665. 🔴 **A Osklen está em `Operação Assistida`, é a 3ª mais atendida (101 reuniões) — e a página
     dela é TEMPLATE EM BRANCO.** `Pessoas`, `Jornada` e `CRM` têm só os rótulos do modelo.
     ⚠ **O único conteúdo datado tem interrogação na própria fonte:** *"uFlow — entrega: Junho ou
     Agosto 2025???"* · *"uBuy — entrega: +d???"*. **O material real parece estar fora do Notion.**
     ⚠ **E a contagem de pessoas da Osklen vem de CSat de kick-off, não de tabela de usuários** —
     chamar de tabela de PLM seria repetir o erro do item 661.
666. 🔴 **Luiza Barcelos tem uma cláusula contratual de integração que muda o desenho:**
     > *"**Não faz parte do escopo deste contrato a integração com o sistema LINX** ou qualquer
     > outro que não seja o sistema SAFETECH."*
     🟢 **E a matriz de permissão é coerente:** a linha `Integração` está 🔴 para **todos** os
     quatro perfis, inclusive `LB - Admin`. ⚠ **O ERP aparece com três grafias na mesma página:**
     `Safe Tech` (propriedade), `Safe Tech` e `SAFETECH` (corpo).
667. 🔴 **Luiza Barcelos: dois blocos da MESMA página listam times diferentes.** O Kick Off diz
     *"Times: Estilo, PCP, Compras"*; `Times Envolvidos` lista nove áreas sob a Diretoria
     Criativa — **e PCP e Compras não aparecem nela por esses nomes.** ⚠ **`Compras` e
     `Suprimentos` parecem ser o mesmo time com dois nomes. Não conciliei.**
668. 🔴 **Um cargo da Luiza Barcelos atravessa QUATRO áreas canônicas:** *"Logística e Cadastro —
     Desenvolvimento até a Precificação está no guarda-chuvas dele"*. **Não dá para atribuir por
     área sem quebrar o cargo.**
669. 🟢 **NOVE clientes têm página `Perfil de Usuário e Permissionamentos`:** VIX, Cambos, Luiza
     Barcelos, Lenny Niemeyer, Recco, Moda Objetiva, NK STORE, Oficina Reserva e NV.
     🔴 **É a fonte mais escalável achada até aqui** — dá perfil, aba de ficha e permissão por
     campo. **Seis foram lidas hoje; o conteúdo está levantado e ainda não foi escrito no corpus.**
670. 🔴 **`Moda Objetiva` tem um perfil chamado `Objetiva - Engenharia`** — e é o segundo cliente
     (com a Oficina) em que Engenharia existe de verdade. ⚠ **Tem também `Objetiva - Estamparia`
     e `Objetiva - Compras MP`**, que não cabem nas 14 áreas canônicas.
671. 🔴 **`Recco` nomeia os perfis SEM prefixo de cliente:** `Admin`, `Time`, `Fornecedor`.
     ⚠ **É o único dos nove assim** — e isso impede distinguir perfil de conta por nome.
672. 🔴 **A aba de integração tem TRÊS nomes entre clientes:** `Integração Linx` (VIX, Lenny, NV),
     `INTEGRAÇÃO SPI` (Cambos) e só `Integração` (Recco, Moda Objetiva).
     ⚠ **Mesma função, três vocabulários** — exatamente o que o `CLAUDE.md` chama de defeito de
     taxonomia. **Antes de cruzar transcrição, isso precisa de um dicionário.**
673. ⚠ **`NV` tem formato diferente dos outros oito:** não é matriz, é página-índice com **13
     sub-páginas, uma por perfil** — `NV - Geral`, `Master`, `Estilo`, `Qualidade`, `Planner`,
     `Planner 2`, `Compras`, `Planejamento Comercial`, `PCP`, `Atacado`, `Marketing`, `View`,
     `Logística`. 🔴 **Só 1 das 13 foi lida.** ⚠ **E o vocabulário diverge dentro da própria
     fonte:** a página-mãe chama os modos de `Inclusão`/`Restrição`, a sub-página chama de
     `exclusão`.

## Os nove clientes com matriz de perfil, escritos (23 set 2026)

674. 🟢 **TREZE clientes com ZERO `[sem fonte]`:** Caedu (142 fatos) · NK STORE (107) ·
     Luiza Barcelos (92) · NV (92) · Puket (92) · VIX (92) · Lofty Style (91) · Osklen (90) ·
     Cambos (88) · Oficina Reserva (88) · Recco (79) · Moda Objetiva (70) · Lenny Niemeyer (66).
     **Corpus: 41% com fonte · 51% ausência verificada · 8% sem fonte.**
675. 🔴 **A NV NÃO TEM CONTRATO — e é cliente ativo de maior porte.** A base do Financeiro
     registra `situação: Sem contrato`, com início e término nulos, e a observação literal:
     > *"**NÃO TEMOS CONTRATO NA REDE NEM DOCSALES.**"*
     🔴 **E a conta está `Ongoing`, grupo `Enterprise`, com três serviços faturados** — `uFlow` ·
     `uBuy` · `Reports`. ⚠ **Não é lacuna de varredura: é ausência de contrato, declarada pelo
     próprio Financeiro.** **É decisão comercial urgente, não item de documentação.**
676. 🔴 **A VIX segmenta Estilo por LINHA DE PRODUTO — cinco perfis, e nenhum outro cliente faz
     isso:** `Vix-Estilo Biquini` · `Vix-Estilo Cover ups` · `Vix-Estilo PA` ·
     `Vix-Estilo Roupas` · `Vix- Estilo Admim`. ⚠ **E a conta tem DUAS fichas com matrizes
     próprias** — `Ficha de PRODUTO` e `Ficha de ESTAMPA`. **Única do corpus.**
677. 🔴 **O perfil de Qualidade da VIX aparece com TRÊS grafias na MESMA página:**
     `Vix- Qualidade` · `Vix qualidade` · `Vix qualdiade` (letras trocadas).
     🔴 **Qualquer cruzamento por nome de perfil falha aqui — e falha em silêncio.**
678. 🟢 **A Cambos mantém um dicionário cliente↔produto escrito à mão, e é o único do corpus:**
     as abas da ficha estão em caixa alta com o termo do uFlow entre parênteses —
     `VERSÕES (Variante)` · `TECIDOS E AVIAMENTOS (Empenho)` · `TAMANHOS PILOTO (Grade)` ·
     `QTD PARA PILOTAR (Lote)` · `FABRICAÇÃO (Fornecedor)` · `APROVAÇÕES DA PILOTO (Aprovações)`.
     ⚠ **É exatamente o artefato que o item 672 pede para o resto da carteira.**
679. 🔴 **A Cambos é facção, e a ficha prova:** a primeira linha do bloco Desenvolvimento é
     **`Todos os Clientes`** — nos outros clientes essa linha é *Todas as Coleções*.
     ⚠ **E há uma funcionalidade sob medida, desligada para todos os cinco perfis:**
     **`Novo Pedido (só a Cambos tem)`** — o rótulo diz isso literalmente.
680. 🔴 **Lenny Niemeyer e Recco NÃO têm segmentação por área no PLM** — só `Admin`, `Time` e
     `Fornecedor`. **Um perfil único para toda a operação do cliente.**
     ⚠ **As duas estão em `Churn`.** 🔴 **A Recco é a única das nove cujos perfis não levam o
     nome do cliente** — sem prefixo, não dá para saber de que conta um perfil é.
681. ⚠ **Na matriz da Lenny, as colunas chamadas `Validação` NÃO são perfis** — são anotação de
     teste, quase todas vazias. 🔴 **Ler a matriz como se fossem cinco perfis seria erro.**
     ⚠ **E a linha `> excluir variante` está INTEIRAMENTE vazia** — não é 🔴 nem 🟢, é
     não-preenchido. **Três estados, e o corpus só modelava dois.**
682. 🟢 **Moda Objetiva é a conta mais segmentada das nove: DEZ perfis**, e traz dois que não
     cabem nas 14 áreas canônicas — **`Objetiva - Estamparia`** (segundo caso, com a VIX) e
     **`Objetiva - Compras MP`**, que separa compra de insumo de compra de produto.
     🟢 **É também o segundo cliente com `Engenharia` real**, ao lado da Oficina Reserva.
683. 🟢 **A NV é a única conta com perfil de Logística E de Marketing, e a única com aba
     `E-commerce` na ficha.** ⚠ **Tem QUATRO perfis com "plan" no nome e funções diferentes:**
     `NV - Planner` · `NV - Planner 2` · `NV - Planejamento Comercial` · e o PCP.
     🔴 **Armadilha de leitura, como `Oficina - Planner` × `Oficina - Planejamento`.**
684. 🔴 **A NV tem 13 sub-páginas de permissionamento, uma por perfil — e só UMA foi lida.**
     ⚠ **O vocabulário diverge dentro da própria fonte:** a página-mãe define os modos como
     `Inclusão` e `Restrição`; a sub-página chama o mesmo modo de `exclusão`.
685. 🟢 **`A CONFIRMAR` virou VALOR, não lacuna.** A planilha de contratos marca assim os usuários
     da Recco. 🔴 **É estado diferente de "vazio" e diferente de "não procurei": é a fonte
     declarando que ela própria não sabe.** **Entra como valor, com a fonte nomeada.**
686. 🔺 **Dois defeitos do gerador, achados por esses seis clientes:**
     **(a)** valor de enum não cortava em ` · `, então `Churn · [a preencher] — campo vazio · ERP:
     Linx` virava `?` **mesmo tendo `Churn` na primeira posição.**
     **(b)** o ramo de LISTA não reconhecia ausência declarada — `Módulos contratados` caía em
     `[sem fonte]` mesmo com a base nomeada. **Os dois corrigidos.**

## A procedência fechada em escala: 2% de `[sem fonte]` (23 set 2026)

687. 🟢 **34 dos 48 clientes com ZERO `[sem fonte]`.** Corpus: **3.396 fatos — 1.396 com fonte
     (41%) · 1.921 ausência verificada (57%) · 63 sem fonte (2%)**.
     ⚠ **Saiu de 66% para 2% em um dia.** 🔴 **Isso NÃO é conteúdo novo: é procedência declarada.**
     **57% do cérebro é "procurei ali, naquela data, e não tem".**
688. 🔺 **ERRO MEU, com perda real: sobrescrevi 20 valores preenchidos.** Ao declarar que o campo
     `Tamanho atendimento` não existe mais na base, apaguei o conteúdo de 20 clientes — incluindo
     grupo, WIP e dupla de atendimento. 🟢 **Recuperados do Git e restaurados.**
     🔴 **A condição do meu script sobrescrevia mesmo quando havia valor.** ⚠ **Terceira vez hoje
     que uma condição frouxa destrói ou fabrica dado** — ver itens 631 e 661.
689. 🔴 **O campo `Tamanho atendimento` NÃO EXISTE MAIS na base `Mapa de Clientes`.** O schema da
     base viva tem 23 propriedades e nenhuma é essa; ele existia no **export de 04/03/2026**.
     🔴 **Campo removido da origem ≠ campo vazio.** ⚠ **O valor que o corpus tem dele é histórico
     de março e não é reconfirmável.** **A CAEDU carrega `P` nessa condição.**
690. 🟢 **19 casos de "a base TEM dado e o corpus não" foram achados pelo próprio script**, que se
     recusa a escrever "vazio" por cima. **Cinco eram reais e foram preenchidos:**
     `Hering` ERP **Ilimitar** · `Baw` ERP **Sem Integração** + 4 módulos ·
     `Cambos` 3 módulos · `Luiza Barcelos` 4 módulos · `Oficina Reserva` 5 módulos.
691. 🟢 **E um deles CONFIRMA o que eu tinha inferido da matriz de permissão:** o campo
     `ERP/Integração` da Oficina Reserva vale literalmente **`SAP e Linx`** — **dois sistemas na
     mesma conta**, como a ficha já sugeria com `Integração Linx` e duas interfaces SAP.
692. 🟢 **`usuarios_contratados_status` está preenchido em 41 de 41 registros da planilha**, mesmo
     quando `usuarios_contratados` está vazio (13 de 41). ⚠ **É a fonte declarando o estado do
     próprio campo** — entra como valor com a ressalva, não como lacuna.
693. 🔺 **Defeito de fonte que custou 28 fatos:** a pista `tabela do PLM` devolvia
     **`banco da API`** — outra coisa — e por isso `tabela de usuários do PLM` não resolvia.
     **Pista genérica engolindo a específica.** 🟢 **Corrigido: a específica vem antes.**
694. 🔴 **Restam 63 `[sem fonte]` em 14 clientes**, concentrados em `contrato-renovacao`,
     `indice-reajuste`, `contrato-vigencia` e `usuarios-contratados`.
     ⚠ **São clientes que não constam na planilha do Financeiro OU cujo campo está vazio lá.**
     **O que falta não é varredura: é a fonte não ter o dado.**

## Onde mora a memória — decisão tomada em 23 set 2026

695. 🔺 **Eu estava duplicando o corpus num vault pessoal, e o Vinicius me pegou.** Capturei seis
     notas em `~/cerebro` — o segundo cérebro **pessoal dele**, sem relação com a uMode — e
     **todas as seis já tinham dono aqui:** o `protocolo-fato-atomico.md` (§1 e §2.1-bis) e os
     itens 603, 636, 631/661/688 e o registro `_varredura-2026-09-23g`.
696. 🔴 **A regra que decide isso já estava travada nos dois lugares, e eu quebrei as duas.**
     O `CLAUDE.md` deste projeto: *"**Um assunto tem um dono.** (...) Dois documentos vivos sobre
     o mesmo tema é o defeito que já se criticou na arquitetura do João — não reproduza."*
     O `CLAUDE.md` global do Vinicius: *"**Não capture:** o que o repositório e o git já registram."*
697. 🟢 **Critério travado: o dono do assunto, não o dono da máquina.**
     · **Assunto com dono num repositório** — decisão de arquitetura, referência operacional,
       achado de varredura, erro já registrado — **fica no repositório.**
     · **`~/cerebro` recebe só o que atravessa projetos** — regra de método, preferência do
       Vinicius, referência externa que repositório nenhum possui.
     · **Caso de fronteira:** lição com duas faces — **os casos concretos ficam no projeto que
       os viveu, a regra transferível vai para o pessoal**, e nenhuma repete a outra.
698. 🟢 **Executado:** cinco notas removidas do `_inbox/` pessoal por serem duplicata;
     uma reescrita mantendo **só a regra transferível**, sem os casos da uMode.
     ⚠ **Uma nota de outro projeto (`hytrack-water-insights`) foi deixada intacta** — não é uMode,
     e **não dá para verificar o dono dela a partir daqui.** 🔴 **Apagar sem verificar seria o
     mesmo erro que passei o dia corrigindo.**
699. 🔴 **Pergunta que fica, e não é minha:** referência operacional da uMode **nunca** deve entrar
     no cérebro pessoal, ou pode entrar como atalho de consulta desde que aponte para o dono no
     corpus? ⚠ **Adotei a forma dura — nunca** — por ser a que não cria documento concorrente.

## Chegaram as 53 transcrições da CAEDU (24 set 2026)

700. 🟢 **53 transcrições Tactiq da CAEDU, de 25/06/2024 a 15/09/2026** — **36,1 horas**,
     **9.392 falas**, **42 falantes**. Registro: `_recebido-2026-09-24-transcricoes-tactiq-caedu.md`.
     ⚠ **As brutas NÃO entraram no repositório** — processadas em disco.
     🔴 **43 das 49 datas não têm marco no `jornada.md`.** **É material complementar, não repetido.**
701. 🔺 **Corrige um negativo que eu fechei ontem.** O `_varredura-2026-09-23g` concluiu que
     *"presença nominal com data NÃO sai por API"* — 99,2% dos participantes anônimos no Notion.
     🟢 **Continua verdadeiro para a API do Notion, e deixou de ser verdadeiro para a conta:**
     toda linha de transcrição é `[HH:MM:SS] Nome: fala`.
     ⚠ **A lição não é "eu errei" — é que um negativo vale contra a FONTE testada, nunca contra
     o fato.** **Vale para todos os negativos rigorosos que registrei.**
702. 🟢 **19 dos 42 falantes resolvem para e-mail** (`scripts/resolve-falantes.py`).
     🔴 **A Julianne está em 53 de 53 reuniões** — a conta inteira passa por uma pessoa, e é a
     mesma cuja ficha estava sem e-mail até ontem. 🟢 **`Vitoria Meneghin` é a contraparte do
     cliente:** 1.805 falas em 22 reuniões.
703. 🔺 **QUARTA vez que uma condição frouxa quase fabricou dado.** O falante `Juliana` (2 falas)
     resolveu para **`juliana@osklen.com.br`** — pessoa de OUTRO cliente numa reunião da CAEDU.
     🟢 **Três regras entraram no resolvedor:** escopo só do próprio cliente + Casa; **nome de um
     token só NÃO resolve**; casamento por token (primeiro nome + mais um).
     ⚠ **Foi a regra 3 que fez `Juliana Ferré` passar a resolver para `Juliana Ferré Esteves`.**
704. 🔴 **13 pessoas falam nas reuniões e não existem no corpus.** A maior é **`Cleiton Gomes`:
     305 falas em 6 reuniões.** ⚠ **`Roselene` aparece com duas grafias** e já está no corpus por
     outro caminho — a demanda `D-2025-013` diz *"solicitado por: Roselene"*.
     🔴 **`Rose` (733 falas, 7 reuniões) é a TERCEIRA maior voz da conta e é só um apelido.**
     **Pode ou não ser a Roselene. Não decidi.**
705. 🟢 **RESPONDIDA a pergunta da hierarquia de produto da CAEDU**, que estava em aberto
     esperando decisão. A transcrição de **14/05/2025** traz, pela boca do cliente:
     · **`Linha` é o topo** — *"a linha é o primeiro para vocês"* (Vitoria Meneghin);
     · **`Grupo` e `Subgrupo` são sempre pareados** — *"os dois são juntos, sempre casadinho"*;
     · **`Feminino/Masculino/Infantil` é outra dimensão**, que a uMode teve de perguntar onde
       entrava;
     · 🔴 **e o mesmo item muda de classificação conforme a linha** — *"dentro do promocional ele
       é uma **mesa**, mas dentro do jovem, dentro do adulto, ele é **top**"*.
     **Não são 4 eixos independentes nem cascata simples: é cascata com reclassificação
     contextual.**
706. 🔴 **E a consequência é de modelo de dado, não de processo.** O campo do uFlow que recebe
     isso é o `Product Type`, e a própria Julianne diz: *"aquele campo de `produto Type`, ele
     **não pode ter hierarquias depois dele**"*. **A CAEDU pede filtro em cascata desde meados de
     2024 e o produto é plano.**
     🟢 **É a mesma família da dor estrutural nº 5 já registrada** (*"a origem vive na ficha, não
     na variante — é problema de modelo de dado"*).
     ⚠ **Item de especificação ou limitação a aceitar? É decisão do Vinicius e do Produto** —
     e vale lembrar o item 631 do `CLAUDE.md`: **limitação de schema não é restrição de projeto.**
707. 🔴 **`fornecedores` tem 506 menções nas 53 transcrições** — a veia mais rica, e é exatamente
     `A frente aberta` da conta. ⚠ **Ainda não foi lida.** A mais densa é
     `2025-11-05_Caedu_Importacao_weekly` (67 menções).
     **Depois dela: `planilha` (367) · `importação` (323) · `Linx` (229).**
708. ⚠ **As transcrições brutas precisam de casa.** Ficaram fora do repositório, em disco local.
     🔴 **O Drive compartilhado é o destino declarado no plano do moedor — confirmar.**

## O que as transcrições da CAEDU dizem — primeira leitura (24 set 2026)

709. 🔴 **A transcrição automática é RUIDOSA, e isso muda o desenho do moedor.** Medido nas 9.392
     falas: **33% sem pontuação final** (frase cortada), **15% com 1 ou 2 palavras**.
     ⚠ **E o erro é de palavra, não só de forma:** *"o conflito sempre Maurício"* · *"um modelo
     de humor"* · *"a gente foi criança"* · *"Deus Olha como igreja"*.
     🔴 **Um extrator que leia isso literalmente produz fato FALSO.**
     🟢 **O que é confiável mesmo com ruído: QUEM falou, QUANDO e sobre QUE TEMA** — rótulo de
     falante e timestamp não passam pelo reconhecimento de fala.
     **Decisão do Vinicius: o moedor lê transcrição corrida ou o resumo do Tactiq?**
710. 🟢 **A frente de fornecedores tem estado REAL, e é outro.** A expressão *"4 primeiros
     fornecedores"* do CRM **não aparece em nenhuma das 53 transcrições**. O que um executivo da
     CAEDU conta em 29/04/2025 é mais concreto:
     · **o teste de perfil de fornecedor JÁ FOI FEITO** — uma colaboradora teve o e-mail
       habilitado como fornecedor *"para testar todas as notificações (...) que campos que eles
       viam, para ter certeza de que **não estavam vendo o que a gente não gostaria**"*;
     · **o bloqueio era uma planilha, e ela ficou pronta**;
     · **falta alinhar data, escolher quais fornecedores e treinar.**
     ⚠ **É de abr/2025 e não há confirmação posterior.**
711. 🔴 **E a frente ESFRIOU.** Menções a `fornecedor`: **33** em 05/11/2025 · 12 · 8 · 12 · 13 ·
     e **UMA** no Plano de Ação de 08/09/2026. 🔴 **A única frente declarada em aberto da conta
     aparece uma vez na reunião de planejamento mais recente.** **Ou foi concluída e ninguém
     fechou o registro, ou saiu de prioridade. É pergunta para a Julianne.**
712. 🟢 **O cliente atribui ganho financeiro ao processo — e é o único lugar do corpus onde isso
     aparece.** Executivo da CAEDU, 29/04/2025: *"antes a gente fazia **30% de desenvolvimento**
     [na coleção], **agora a gente faz sempre**"* · *"a gente conseguiu fazer **renegociações,
     diminuir custo do produto e melhorar a margem**"*.
     ⚠ **Sem número e sem período — é depoimento, não métrica.** 🔴 **Mas é depoimento de
     executivo numa conta em reconquista de confiança, e pode virar caso** com autorização.
713. 🔴 **As reuniões "Caedu 2.0" são INTERNAS da uMode.** Tanto `2026-06-22` quanto o
     `2026-09-08_Plano_de_Acao` têm só Juliana Ferré, Julianne, Vanessa Rinaldi, Marina Santoro e
     Fernanda Araujo. ⚠ **Nenhuma pessoa da CAEDU participa.** **O "CAEDU 2.0" nessas duas é
     planejamento da uMode sobre a conta, não acordo com o cliente.**
     🔴 **Valor e termo de contrato NÃO foram copiados — `T1`**, no mesmo critério do registro da
     proposta.
714. ⚠ **`Edson` aparece uma segunda vez, por via independente** — na fala do executivo no
     presencial. 🔴 **A transcrição não diz o cargo.** **Confirma que existe um `Edson` na conta;
     não confirma que seja o CEO.** ⚠ **Aparecem também `Nilson`, `Cris` e `Mariana`, sem
     sobrenome e não resolvíveis.**
715. 🔺 **Li 4 das 53 transcrições.** ⚠ **`fornecedores` tem 506 menções e eu segui um fio só.**
     🔴 **E não classifiquei nada como NOVO / CONFIRMA / CONTRADIZ** — o cruzamento automático
     não existe; isto foi leitura humana. **A lacuna está declarada no registro.**

## O contrato de entrada de call, e a CAEDU organizada (24 set 2026)

716. 🟢 **Escrito o `protocolo-entrada-de-call.md`** — o contrato de como uma reunião entra no
     BrainHub, a pedido do Vinicius, para o coletor que ele monta no Google Workspace.
     🔴 **A regra que governa: o coletor escreve SÓ em `_inbox-calls/`, nunca no canônico.**
     **Duas razões medidas:** a transcrição chega com 33% das falas cortadas, e é a mesma regra
     que o vault do João já aplica (*"agente escreve só no próprio inbox"*).
717. 🔴 **O pedido central ao coletor é UM: mande E-MAIL, não nome de exibição.**
     **23 dos 42 falantes da CAEDU não resolvem por nome**, e um deles — `Rose` — é a terceira
     maior voz da conta. 🟢 **O convite do Meet tem a lista com e-mail, e o corpus tem 637 nomes
     indexados por e-mail.** ⚠ **É o único dado que só o coletor consegue e que o BrainHub não
     obtém sozinho.**
718. 🔴 **`natureza` e `destino` saem do DOMÍNIO do e-mail, nunca do título.**
     **`2026-06-22_Caedu_2_0` e `2026-09-08_Plano_de_Acao_Caedu` têm "Caedu" no nome e são
     INTERNAS da uMode.** **O título mente; o domínio não.**
719. 🔴 **15 das 53 reuniões da CAEDU (28%) não têm ninguém do cliente falando.**
     ⚠ **Não é crítica — é classificação.** Reunião interna de preparo é trabalho legítimo, **mas
     misturar as duas infla a intensidade de atendimento.** **A métrica deve separá-las?**
720. 🔴 **A contraparte da CAEDU mudou QUATRO vezes em dois anos:** Vitoria Meneghin
     (jul/2024→ago/2025, 1.805 falas) → Mariana Amaral / `tamiris` → Roselene (out–nov/2025) →
     `Rose` (dez/2025→abr/2026, 733 falas) → **Cleiton Gomes** (abr→ago/2026) → `Bruno`.
     🔴 **A Vitoria desaparece depois de 06/08/2025 e o corpus não registra a saída.**
     ⚠ **Quatro trocas de interlocutor explica, em parte, por que o processo não se fixou** numa
     conta que está em reconquista de confiança.
721. 🟡 **`Rose` é a `Roselene`? Testável, e o teste foi feito:** as duas grafias **nunca aparecem
     na mesma reunião** e são sequenciais — Roselene em out–nov/2025, Rose de dez/2025 em diante.
     ⚠ **Indício forte, não prova.** 🔴 **Só o e-mail confirma** — e é o que o coletor traz.
     ⚠ **E `Tamires` tem TRÊS grafias no corpus:** `Tamires`, `tamiris` e a da ata.
722. 🔺 **Minha própria regra me bloqueou, e a pista boa estava no e-mail.** `Mariana Amaral` não
     resolvia porque a **ficha dela se chama só `Mariana`** — um token — e eu exijo dois.
     🟢 **Corrigido com a pista mais forte que existe: o LOCAL-PART do e-mail corporativo.**
     `mariana.amaral@caedu.com.br` contém os dois tokens do falante. **Resolvidos: 19 → 20.**
723. 🟢 **`jornada.md` da CAEDU: 21 → 33 marcos**, todos com fonte e data. **A cronologia completa
     das 53 ficou no registro `c`** — o `jornada.md` guarda só os marcos. **Um assunto, um dono.**
724. 🟢 **Três registros escritos para a CAEDU:** `a` índice e identidade · `b` primeira leitura
     de conteúdo · `c` cronologia e sucessão. ⚠ **Li 4 das 53 transcrições** — a lacuna está
     declarada em cada um.

## A CAEDU terminada, e o prompt entregue (24 set 2026)

725. 🔺 **Duas correções que o Vinicius me cobrou, e as duas eram justas.**
     **(a)** Eu escrevi o contrato de entrada de call **dentro do corpus** e não entreguei o
     **texto que ele cola no outro agente** — que era o pedido. 🟢 **Feito:
     `prompt-agente-classificador-de-call.md`**, classe `TEMPLATE`, com System Prompt, JSON
     Schema e três testes de aceite.
     **(b)** Eu parava a CAEDU no meio e relatava. 🟢 **As 53 foram varridas.**
726. 🟢 **As 14 áreas da CAEDU ganharam camada de ROTEAMENTO** — em que reunião procurar cada
     assunto, com data e densidade. 🔴 **É roteamento, não conteúdo:** contagem de termo
     sobrevive ao ruído de 33% de falas cortadas; **narrativa não sobrevive.**
     **12 das 14 têm reuniões acima do limiar** — de 13 a 39 cada.
727. 🟢 **CONFIRMADAS as 7 áreas que eu havia preenchido por ausência — agora por evidência
     POSITIVA em 36 horas de conversa gravada.** As expressões `time de financeiro`,
     `time de logística`, `time de design`, `time de PCP`, `time de engenharia` e
     `time de e-commerce` aparecem **ZERO vezes** nas 53 transcrições.
     ⚠ **Deixa de ser ausência num documento e passa a ser ausência em dois anos de reunião.**
728. 🟢 **Os times que a CAEDU NOMEIA são cinco, e são os mesmos com perfil no PLM:**
     **Produto** (`time de produto` 12 · `gerente de produto` 25) · **Modelagem** (10) ·
     **Estilo** (9) · **Planejamento** (8) · **Compras** (8).
     🟢 **Duas fontes independentes — perfil de acesso e fala — chegam à mesma lista.**
729. 🔴 **`05_PCP` e `12_Design` não têm NENHUMA reunião acima do limiar.** As outras 12 têm de 13
     a 39. ⚠ **Não prova que a função não exista na CAEDU** — 🟢 **prova que não é assunto das
     reuniões com a uMode**, e para o cruzamento é isso que importa: **não há de onde tirar
     conteúdo para essas duas nesta conta.**
730. 🟢 **Achado novo: `gerente de grupo` é cargo real da CAEDU**, ligado à taxonomia
     `grupo/subgrupo`. *"vai ficar gerente de produto mais gerente de grupo"* — Vitoria Meneghin.
     ⚠ **O corpus não tinha esse papel.**
731. ⚠ **O que NÃO consegui extrair, e por quê:** narrativa fina por área. **O ruído do ASR
     inviabiliza** — as falas vêm cortadas no meio e com erro de palavra. 🔴 **Tentei e parei:
     insistir produziria citação mutilada com aparência de fato.** **O que entrega valor com
     esse material é roteamento + identidade + cronologia, e é o que está escrito.**
732. 🚨 **O corpus só tinha aberto 1 dos 6 exports do Notion no vault do João.** Os outros
     cinco estavam em `BrainHub/uMode/_Clientes/_geral/notion/` desde sempre.
     ⚠ **O que me levou até eles não foi varredura — foi a UNIFORMIDADE da lacuna:**
     `Resultado esperado` e `Quem aprova` vazios em **993 de 993** demandas, `Missão da cadeira`
     em **402 de 402** fichas. 🟢 **Lacuna uniforme demais não é falha de leitura: é template
     que nunca foi alimentado** — e isso é pergunta sobre a FONTE, não sobre o documento.
     *(Terceira variação de "ausência de fonte é hipótese". Ver `_varredura-2026-09-24`.)*
733. 🔴 **Existia um ritual semanal de avaliar a saúde de cada conta, e ele parou em 2024.**
     388 avaliações `Feedback Semanal`, por gente da uMode — Taís Moser, Andrea Holmer, Laura,
     Elizabeth, Julianne. ⚠ **Pergunta para o Vinicius: o ritual acabou, ou mudou de lugar?**
     🔴 **Não sei, e a diferença muda o que o BrainHub deve fazer com isso.**
734. 🔴 **Metade da carteira nunca foi avaliada nesse ritual** — 24 de 48 clientes.
     ⚠ **Isso é ausência de MEDIÇÃO, não conta saudável**, e está escrito assim no `jornada.md`
     de cada um dos 24, como ausência VERIFICADA. **Por que metade ficou de fora é pergunta
     aberta.**
735. 🔴 **No que foi medido, 220 das 427 avaliações (52%) são "atenção", "atraso" ou
     "bloqueio".** Piores: **Estrela 2,00** · **Studio Z 2,84** (53% de flag) ·
     **NTK 2,89** (dominante: *Bloqueio*) · **Vivara 3,00** (🔴 **71% de flag**).
     ⚠ **É retrato de 2024 e não estado de hoje** — mas é o único histórico de saúde que existe.
736. 🟢 **`Resultado esperado`, urgência e autor de demanda deixam de ser "campo sem fonte
     possível": o formulário que os coleta EXISTE.** `Formulário de Demandas` tem
     `Objetivo Esperado`, `Urgência e Impacto` e 🟢 **`E-mail de contato`** — identidade por
     e-mail, que é exatamente o que o corpus pede. 🔴 **E foi usado 2 vezes.**
     ⚠ **Muda quem resolve: não é trabalho de documentação, é decisão de processo.**
737. ⚠ **Duas sujeiras já visíveis nas 2 linhas do formulário:** `Cliente` vem como `Reserva`
     e `reserva`; e **`Setor - Seu nome` colapsa instituição, área e pessoa num campo de texto
     livre** — `"Reserva - Engenharia - Thamires"`, `"Umode - Fernanda"`. 🔴 **É exatamente o
     que a hierarquia do BrainHub separa em quatro níveis.**
738. 🟢 **RESOLVIDO: `Oficina Reserva` ≠ `Reserva`.** São duas contas, não duas grafias.
     **Prova:** a MESMA avaliadora (Andrea Holmer) avalia as duas no MESMO mês (set/2024).
     🟢 **E a regra que decidiu vale para o próximo caso:** grafias em períodos **sequenciais**
     são conta renomeada (`STZ`→`Studio Z`, `Básico`→`Básico&Co`); grafias em período
     **sobreposto com o mesmo avaliador** são contas distintas. ⚠ **A semelhança entre as
     strings não decide nada** — `Reserva`/`Oficina Reserva` são mais parecidas que
     `STZ`/`Studio Z`, e são o par que NÃO se funde.
739. 🔴 **Não dá para calcular margem de RFI, e não é falta de varredura.** `Valor` existe em 22
     de 53 (R$ 85.237) e `Horas Totais` em 30 (1.101 h) — ⚠ **mas `Cobrado` está preenchido em
     3 de 53 e `Horas Trabalhadas` em 1 de 53.** **Sem realizado não há comparação com o
     estimado.** *(No corpus: `Cobrada?` 12/85, `Horas trabalhadas` 4/85, `Taxa aplicada` 0/85.)*
     **Pergunta para o Financeiro, não para mim.**
740. ⚠ **`RFI-72` é RFI da própria uMode, sem cliente.** O padrão só tem `_rfis` dentro de
     cliente. 🔴 **Não criei pasta para ela** — criar estrutura é decisão, não consequência de
     um import. **Fica registrada aqui até o Vinicius decidir onde RFI interna mora.**
741. 🔺 **Anomalia de data preservada como está, em `RFI-2026-007` (NV):** criada em
     **02/01/2026**, com **aceite do cliente em 05/12/2025** — **o aceite antecede a criação.**
     ⚠ **Não inverti nem "corrigi" nenhuma das duas**: pode ser registro retroativo, pode ser
     digitação. 🔴 **Escolher uma seria inventar dado com aparência de conserto.**
742. ⚠ **Não encontrei `Projetos.csv`, `Módulos.csv` nem `uFlowDataBase.csv` em
     `_geral/notion/`** — eu os havia citado como existentes. 🔴 **"Não encontrei em X" não é
     "não existe"**: ficam como pendência de procura, não como fato negativo.
743. 🔴 **As 206 transcrições paradas no Drive são a resposta para "outros clientes" — e eu NÃO
     as alcanço.** As 53 da CAEDU vieram por zip, na mão do Vinicius. As outras ~153 são de
     outras contas e continuam paradas.
     ⚠ **O que procurei, em 24/09/2026, pelo conector do Drive na conta do Vinicius:**
     `title contains 'Tactiq'` · `fullText contains 'tactiq'` · pastas com `'Transcri'` no título ·
     todas as pastas `sharedWithMe`. **Voltaram `transcribe-audio` (a esteira de áudio do
     WhatsApp, do João) e os CSVs do Notion — nenhuma pasta de transcrição de reunião.**
     🔴 **Escrevo "não encontrei nessas buscas", não "não existe":** a pasta é do
     `joao.risoleo@umode.com.br` e **não está compartilhada com esta conta.**
     🟢 **Dois caminhos de desbloqueio, e os dois são decisão do Vinicius:** (a) o João
     compartilha a pasta; (b) **o agente coletor do Google Workspace entrega, e o contrato de
     entrega já está escrito** — `protocolo-entrada-de-call.md` + o prompt pronto em
     `prompt-agente-classificador-de-call.md`.
     ⚠ **Enquanto isso não acontece, "atacar outro cliente" não é limitado por trabalho meu —
     é limitado por acesso.**
744. 🔴 **CORREÇÃO do que eu disse em 25/09: as 999 demandas sem dono NÃO são o bloqueio do
     roteamento.** O `protocolo-gestao-demanda.md` § *Mecanismo de aprovação* roteia para o
     **`Governança` do MD-ALVO** — o documento que a mudança altera — **não para a demanda.**
     🟢 **E os alvos estão cobertos: 1.292 de 1.321 (98%) têm papel declarado.**
     ⚠ **O gargalo nunca foi cobertura; é que 0% dos papéis vira pessoa.**
745. 🟢 **O mecanismo de aprovação de contexto JÁ ESTAVA ESCRITO** no `protocolo-gestao-demanda.md`
     — inclusive a frase *"nenhum agente escreve contexto sem essa aprovação registrada como
     marco"*, o ciclo `Nenhuma aprovação pendente → Aguardando → Aprovada → Aplicada`, e a
     distinção `Contexto consultado` × `Contexto impactado`. ⚠ **O template de demanda tem os
     campos e eles estão vazios:** `Quem aprova` em 1 de 998, `Contexto impactado` em 1 de 998.
     🔴 **Não é mecanismo a inventar — é mecanismo desenhado que nunca foi alimentado.**
746. 🔴 **`liderança de Atendimento uMode` não resolve, e trava 1.219 documentos.** Três leituras:
     `Ju — Diretora de Operações` (do `02_Atendimento/contexto-area.md`) · `Luciano Troiani`
     (**Head de CS**, o cargo mais próximo, mas a área não o nomeia) · e a hipótese de que
     Diretora de Operações ≠ liderança de Atendimento. ⚠ **E `Ju` é um token só com DUAS
     candidatas na Casa** — Juliana Ferré e Julianne Dias. 🔴 **Pior: nenhuma das duas fichas tem
     a cadeira `Diretora de Operações`.** **Decisão do Vinicius.**
747. ⚠ **`Liderança de Pessoas e Cultura`: dois documentos do corpus discordam.**
     `07_People/contexto-area.md` diz **Flávia Campello (execução) · João Risoléo (decisão)**; a
     ficha da Flávia diz cadeira **`Analista de Gestão Financeira e Administrativa`**.
     🟢 **Pode ser acúmulo** — mas os textos não se referenciam. 64 documentos dependem disso.
748. ⚠ **`SMB` obriga fallback no roteador, e isso é requisito.** 6 contas não têm CS dedicado
     **por desenho** — 4takes, Camys, Cavallari, Studio Minah, TDC, Ton Age. 🔴 **O destino de
     exceção provavelmente é a liderança de Atendimento — que é exatamente o papel do item 746.**
749. 🟢 **Dois defeitos do resolvedor de identidade corrigidos em 25/09.** (a) **Não havia
     normalização de acento** — `Taís Moser` não achava a ficha `tais-moser.md`; acento nunca foi
     identidade. (b) **Eu pus a regra fraca antes da forte:** só-primeiro-nome rodava antes do
     casamento por token, então `Rafael Renaldim` caía em dois Rafael e voltava ambíguo **sem usar
     o sobrenome que estava na mão.** ⚠ **A regra que usa mais informação tem de ser tentada
     primeiro** — vale para qualquer resolvedor, não só este.
750. 🟢 **Apelido agora se declara na ficha, não no código.** `Eliza Alves` → Elizabeth Alves de
     Souza Santana e `Ju Ferré` → Juliana Ferré Esteves entraram como `Nome preferido`, **cada um
     com duas fontes independentes e sobrenome único na Casa.** ⚠ **O resolvedor já lia esse
     campo** — a lacuna era de dado, não de código. **Nome de pessoa nunca entra em script.**
751. 🔴 **`Aprovação necessária: Não` em 997 de 998 demandas é DEFAULT DE IMPORTAÇÃO, não
     avaliação — e eu quase derivei uma conclusão em cima disso.** Ia preencher `Quem aprova`
     com *"não se aplica"* nos 997, o que parecia lógica limpa. **Três checagens desmontaram:**
     (a) o `_template_demanda.md` traz o campo como `[sim/não]`, **placeholder**; (b) o valor
     entrou em massa no commit `b6d4ff55` *"Replica a estrutura completa para os 46 clientes
     reais"*; (c) 🔴 **o `protocolo-gestao-demanda.md` NÃO define esse campo em lugar nenhum** —
     não há regra que diga quando uma demanda exige aprovação de contexto.
     ⚠ **A única demanda com `Sim` é da Casa e foi preenchida à mão**, com `Quem aprova` real.
     🔴 **997 valores iguais não são 997 decisões.** É a mesma armadilha do `pessoas-da-area`
     que me fez julgar 48 de 48 clientes com tabela de usuário quando eram 4.
752. 🔴 **Falta a REGRA que diz quando uma demanda exige aprovação de contexto.** O mecanismo
     existe (item 745), o campo existe, o ciclo de estados existe — **e o critério de acionamento
     não.** ⚠ **Sem ele o pipeline inteiro do `_espec-pipeline-de-contexto-e-aprovacao.md` não
     tem gatilho:** o agente saberia aprovar, mas não saberia **quando precisa** aprovar.
     🟢 **Isto entra na Fase 1**, junto com o critério de relevância — são a mesma família de
     decisão e não devem virar dois documentos.
753. 🟢 **RESOLVIDO sem precisar do Vinicius: `liderança de Atendimento uMode` é a Marina Santoro,
     Head de Atendimento desde 12/08/2026 (D73), reportando à Ju.** 🔴 **A pergunta não precisava
     de decisão — precisava de eu procurar direito.** A fonte é a página `🏛️ Organograma uMode —
     V2` do Notion, com o **Organograma V4 (02/09/2026 · D75)**. ⚠ **D77 ampliou a cadeira:**
     Head de Atendimento **+ Gestão de Contas & Projetos**, com Fernanda Araújo reportando a ela.
     **Isso destrava 1.219 documentos.**
754. 🟢 **`Ju` = Juliana Ferré, e não é inferência: o organograma escreve o apelido literalmente**
     — *"Juliana Ferré (Ju)"*, em duas tabelas. ⚠ **O Vinicius levantou as duas possibilidades
     (Juliana Ferré ou Julianne Rodrigues); a Julianne não aparece como `Ju` em lugar nenhum do
     organograma.** 🔴 **E a ficha da Juliana estava errada:** dizia `Key Account · Consultor(a)
     de Negócios`, derivado do CRM. **Ela é Diretora de Produto & Cliente** — uma das 3 pessoas
     que ocupam as 8 cadeiras de diretoria. O próprio `protocolo-gestao-pessoas.md` já avisava
     que papel no CRM ≠ cadeira no organograma, e eu tratei como se fosse.
755. 🟢 **`Liderança de Pessoas` = João Risoléo (acumula) + Vanessa Rinaldi (Líder de Trilha LC).**
     ⚠ **E o conflito que registrei no item 747 tinha o lado errado:** eu supus que a ficha da
     Flávia pudesse estar desatualizada. **Era o `07_People/contexto-area.md`.** A Flávia
     acumulava Talento na V2.2 (mai/2026) e **deixou de acumular na V4** — ficou com
     Administrativo (Financeiro · Jurídico). **A ficha dela nunca esteve errada.**
756. 🚨 **Eu estava propondo endereçar aprovação para uma cadeira que não existe mais.** Levantei
     `Luciano Troiani — Head de CS` como leitura possível. 🔴 **A ficha dele diz `Inativo`, e o
     Head de CS era o `Rafael Del Gaudio Renaldim`, que saiu em 12/08.** ⚠ **Duas camadas de
     erro: cargo extinto e pessoa desligada.**
757. 🚨 **10 fatos `atendimento` apontavam para pessoas DESLIGADAS — 5 clientes para a Andrea
     Holmer, cuja própria ficha já dizia `Inativo`.** O `gera-fatos.py` lia nome e e-mail e **não
     lia o status**. 🔴 **Na manhã de 25/09 eu descrevi essa lacuna — fato sem intervalo de
     validade — como "dívida latente, não dor atual". Estava errado: ela já tinha materializado,
     e eu mesmo a produzi na Fase 0 na véspera.**
     🟢 **Conserto aplicado, e não é apagar:** o fato fica (foi verdade e é verdade histórica) e
     ganha marca `⚠ DESLIGADO`; o roteador ignora o marcado. **É a metade barata do intervalo de
     validade — não diz quando deixou de valer, diz que não vale mais.**
     🟢 **Nenhum cliente perdeu o endereço:** em todos havia também alguém vivo. Seguem **25 com
     endereço vivo · 6 `SMB` · 17 sem endereço**.
758. 🔴 **CORRIGIDO: eu havia escrito que NÃO EXISTE fonte de desligamento.** O
     `_espec-pessoas-e-comunicacoes.md` § 0.3 dizia *"nenhum sistema varrido registra saída de
     pessoa"*. **O organograma do Notion registra, com nome, data e código de decisão** — D73,
     D75, D76. ⚠ **Eu varri o CRM e a base `uModers` e declarei sobre o universo.** É a mesma
     falha que o `CLAUDE.md` trava, desta vez de minha autoria: **"não encontrei em X" nunca é
     "não existe"**.
759. 🆕 **O organograma traz oito desligamentos que o corpus não registrava como tal** —
     Rafael Del Gaudio Renaldim (D73) · Alexandre Ferrari, Andrea Goulart, André Gustavo (D75) ·
     Gabriel Cancio, Tatiana Bertazoli, Henrique Barbosa de Sousa, Williem Berg de Oliveira Gomes
     (D76). ⚠ **E cadeiras novas que o corpus não tem:** `GTM` (João) · `Eventos` (Sandro) ·
     `Líder de Trilha LC` (Vanessa) · `PMO` (Victor, absorveu PO Integração) · **`CTO` VAGA**, com
     o João interino.
760. ⚠ **Fallback de `SMB` agora tem candidato fundamentado:** as 6 contas sem CS dedicado
     endereçam para a **Head de Atendimento (Marina)**, que por D77 responde pela carteira
     inteira. 🔴 **Ainda é decisão do Vinicius** — mas deixou de ser pergunta sem resposta
     possível.
761. 🔴 **O acervo da Laura não tem transcrição de fala. Nenhuma.** São **76 resumos do Gemini**
     e **25 chats digitados** — e chat tem **87 linhas com falante em 25 arquivos**, média de
     **3,5 por reunião**. ⚠ **A regra travada em 24/09 — "transcrição sempre prevalece sobre
     resumo" — não tem como ser aplicada: não há transcrição.** 🟢 **Todo o acervo é o caso
     `tem_transcricao: false` do protocolo**, e isso é lacuna declarada, não equivalência.
762. 🟢 **E ele resolve exatamente o que a CAEDU deixou aberto: identidade.** **90 pessoas de
     cliente por e-mail, 82 novas para o corpus**, em 10 domínios. Na CAEDU, **23 de 42 falantes
     não resolviam** — incluindo a `Rose`, 733 falas, terceira maior voz, e ninguém sabia quem
     era. ⚠ **Os dois acervos são opostos e complementares: um é só fala sem identidade, o outro
     é só identidade sem fala.**
763. 🔴 **Distinção que não se colapsa: participante × mencionado.** **18** saem do cabeçalho
     `convidado` — **a pessoa esteve na reunião, naquela data**. **72** aparecem só no **corpo do
     resumo, escrito por um modelo** — prova que o endereço existe no domínio, **nada além**.
     ⚠ **Colapsar os dois transformaria "o Gemini citou este e-mail" em "esta pessoa participou".**
     🟢 **O que sustenta usar os 72:** e-mail é string estruturada, não sofre paráfrase — ou está
     sintaticamente certo, ou não é e-mail. E **89 dos 90 batem com domínio de cliente conhecido**.
764. ⚠ **Só 21 dos 76 resumos trazem o cabeçalho de participantes.** 55 não trazem. 🔴 **Se o
     coletor do Workspace for a fonte futura, o cabeçalho é o campo que mais importa** — é dele
     que sai o dado primário de presença.
765. 🚨 **Dado pessoal está no acervo e apareceu no segundo arquivo aberto:** **7 telefones** em 6
     arquivos, **3 CPFs** em 3, **1 e-mail pessoal**. 🔴 **Nenhum valor foi lido ou copiado** — o
     script conta e para. 🟢 **É a prova concreta de que o eixo de sensibilidade tem de agir na
     ENTRADA:** o dado já está lá, e qualquer importação ingênua o traz junto.
766. ⚠ **Domínio `illimitar.com.br`, 3 pessoas, 8 ocorrências, sempre junto da Moda Objetiva e nas
     mesmas datas de julho/2026.** 🔴 **Não dá para dizer de que cliente é** — parceiro,
     fornecedor ou outra conta. **Não foi atribuído a ninguém.** Pergunta para a Laura.
767. ⚠ **Três 1:1 internos no acervo** — `Victor _ Laura - Permissionamento` · `Ana Paula _ Laura`
     · `Alinhamento Onboarding _ Dupla Lala e Holmer`. 🔴 **Registrados como existentes e não
     lidos para conteúdo.** O Vinicius decidiu em 25/09 que material interno seria processado,
     **mas a regra do `T0-P` continua: juízo sobre pessoa identificável nunca por valor.**
768. 🟢 **O acervo cobre 19 clientes e 4 anos (set/2022 → set/2026)** — inclusive contas que o
     corpus mal tinha material: **Plie (15 reuniões), Highstil (4), Ladeira Bijuterias, Laces,
     Piccadilly, Tee Fashion, Gagnoa, Aramodu, Disparate**. ⚠ **É a carteira da Laura, não um
     cliente** — e muda a natureza do processamento em relação à CAEDU.
769. 🚨 **Oficina Reserva está `Ongoing` e a dupla que a atende não existe mais inteira.** Três
     fontes independentes convergem: o **organograma** diz que a **Andrea Holmer foi desligada em
     02/09** (D75) · o **CRM** diz que o time é `Holmer & Laura` · e o **acervo de reuniões da
     Laura** mostra **uma única reunião com a conta, em 05/02/2026 — 232 dias de silêncio**.
     🔴 **Metade da dupla saiu da empresa; a outra metade não tem reunião há oito meses.**
     ⚠ **Não prova abandono** — a conta pode ter passado para outra pessoa sem o CRM registrar.
     🟢 **Mas é exatamente a pergunta que nenhuma das três fontes faz sozinha.**
770. 🟢 **O cruzamento produziu dois alertas e um deles se explica sozinho — o que valida o
     método.** A **NV** aparece como `Ongoing` com **827 dias** sem reunião da Laura; mas o
     atendimento da NV é **Fernanda Araújo + Victor Aragão**, e a conta tem RFI com aceite em
     dez/2025. ⚠ **A Laura simplesmente não atende a NV.** 🔴 **Falso positivo previsto pelo
     próprio dado** — e é por isso que o alerta nasce como pergunta, não como conclusão.
771. 🆕 **O título da reunião é dado primário e conta a história da conta.** Ele é o que uma
     pessoa digitou ao marcar o evento — **não passou por modelo nenhum**, ao contrário do corpo
     do resumo. Daí sai cliente, data e assunto com segurança.
     ⚠ **Padrão que aparece:** a **Plie** teve **9 discoveries em 15 reuniões**, todas entre
     mai e out/2025, e hoje está `Churn` / `Encerrado`. A **Moda Objetiva** tem **7 de 17 em
     integração** e está em `Operação Assistida`. 🟢 **A distribuição de assunto separa conta em
     diagnóstico de conta em operação** — e é mensurável sem ler uma linha de conteúdo.
772. 🟢 **Cadência de atendimento medida, por cliente, em 4 anos.** Vivas na carteira da Laura:
     **Cambos** (2 dias), **Luiza Barcelos** (3), **Lofty Style** (15), **Moda Objetiva** (52).
     Frias e coerentes com o corpus: Highstil `Churn` (217) · Plie `Churn` (329) · DRO `Churn`
     (408) · Studio Z `Churn` (613) · Laces, Ladeira, NTK todas `Churn` com mais de 800 dias.
     ⚠ **E cinco contas no acervo não estão na carteira atual** — Piccadilly, Tee Fashion,
     Gagnoa, Aramodu, Disparate. **Nenhuma foi criada**: aparecer numa reunião de 2023 não é
     estar na carteira hoje.
773. 🔴 **CORREÇÃO dos itens 771 e 772, apontada pelo Vinicius no mesmo dia: eu cruzei status de
     HOJE com reuniões de QUATRO ANOS como se o status fosse atemporal.** **48 de 48** `status` do
     corpus carregam a **data da varredura** (21–22/09/2026), **não a data em que passaram a
     valer** — e nenhum `jornada.md` tem marco datando a virada para Churn.
     ⚠ **Consequências:** (a) para conta `Churn`, "silêncio longo" é **tautologia** — conta
     encerrada não tem reunião; o item 772 chamou isso de "coerente com o corpus", e é coerente
     com um retrato, não com uma linha do tempo. (b) o item 771 descreve a Plie como "9 discoveries
     e hoje Churn", o que **insinua trajetória que eu não sei**: se a Plie virou Churn em nov/2025,
     as reuniões terminando em out/2025 são só o fim da conta.
     🟢 **O item 769, Oficina Reserva, se sustenta** — e pelo motivo exato: os três dados são
     **atuais** (status de hoje · silêncio medido até hoje · desligamento de 02/09).
     🔴 **É o mesmo defeito que eu documentei a sessão inteira — fato sem intervalo de validade —
     cometido na minha própria análise.** Regra que sai daqui: **cruzamento temporal só vale entre
     dados que carregam a mesma referência de tempo.**
774. 🔴 **CORREÇÃO do item 761 e do registro de 25/09: o acervo da Laura TEM transcrição de fala.**
     **17 dos 76 `.docx`** trazem o bloco `📖 Transcrição` **depois** do resumo — **1.263 falas,
     573 mil caracteres**. Eu olhei o cabeçalho e o resumo e **não abri o documento até o fim**.
     **16 foram lidos** (o 17º é o 1:1 `Dupla Lala e Holmer`, que não se lê). Contas com fala:
     Luiza Barcelos 6 · Cambos 6 · Lofty Style 2 · Highstil 1 · Plie 1 — **incluindo as duas
     reuniões mais recentes do acervo** (LB 22/09 e Cambos 23/09/2026).
     ⚠ **O erro contaminou a primeira extração:** o recorte ia até o fim do arquivo e **fala entrou
     rotulada como "resumo Gemini"**. Refeita. 🔴 **O registro de 25/09 não se edita**; esta é a
     correção, e os 8 `pessoas.md` que repetiam a frase foram corrigidos apontando para cá.
     🔴 **É a quarta variação de "ausência de fonte é hipótese"** — desta vez dentro do próprio
     arquivo que eu tinha na mão.
775. 🟢 **As propostas passaram a ter eixo de tempo — cobrança do Vinicius em 25/09:** *"em um
     cérebro, tem que ficar claro o que aconteceu, o que está acontecendo e o que está por vir."*
     **493 propostas em 68 reuniões**, cada uma posicionada na linha do tempo do cliente:
     **161 aconteceu** · **9 acontecendo** · **42 por vir** · **281 compromissos antigos com
     cumprimento não verificado**. Regra: só a reunião **mais recente** do cliente, com **até 90
     dias**, fala do presente; frase no **futuro** é compromisso, seja qual for a chave.
     🟢 **E 13 `jornada.md` ganharam a linha do tempo das reuniões** sob `## Marcos da jornada`,
     com os três blocos. ⚠ **O "por vir" quase vazio da primeira versão era defeito meu:** o
     extrator **cortava fora** o bloco `Próximas etapas` do Gemini — presente em **49 de 72**
     resumos, com dono. Recuperado.
776. 🚨 **Compromissos órfãos: o cruzamento de PESSOA com o momento da jornada.** No último contato
     de três contas, os compromissos pendentes citam **quem hoje está desligado — Andrea Holmer**:
     **Highstil 6 de 6** · **Plie 7 de 8** · **DRO 1 de 3**. 🔴 **Se não foram cumpridos antes da
     saída, ficaram sem dono, e nenhuma fonte diz quem herdou.** ⚠ As três estão `Churn`, então
     hoje isso é **história** — o que estava prometido quando a conta saiu. 🟢 **Para conta viva o
     mesmo cruzamento vira alerta**, e o extrator já o marca em `por vir`.
     ⚠ **Oficina Reserva (`Ongoing`) não tem órfão**: as pendências de 05/02/2026 citam Joyce Dias,
     Juliana Ferré e Laura — mas estão **232 dias sem verificação**.
777. 🔴 **CORREÇÃO dos itens 768 e 771: eu contei ARQUIVOS, não reuniões.** O resumo e o chat da
     mesma reunião entravam duas vezes. **Plie: 15 arquivos = 11 reuniões**, das quais **6 são
     discovery** — não "9 de 15". Moda Objetiva **17 → 14** · Luiza Barcelos **19 → 18** · Lofty
     Style **10 → 9** · Cambos **11 = 11**. 🟢 **A leitura do 771 se mantém** (Plie concentrada em
     diagnóstico, mai–out/2025), **com o número certo**.
778. 🟢 **Item 766 resolvido — e a resposta já estava no corpus.** `illimitar.com.br` é o
     **fornecedor do ERP da Moda Objetiva**: o `institucional.md` dela diz `erp: Ilimitar`
     (Notion, 22/09), e os **títulos** das reuniões de jul/2026 — dado primário — são *"Testes
     Integração uMode · Ilimitar · Objetiva"*, **nas mesmas datas** dos e-mails. ⚠ **As 3 pessoas
     são do fornecedor, não do cliente** — não entram na tabela de pessoas da Moda Objetiva como
     time dela. 🔵 **Decisão do Vinicius:** onde registrar contato de **fornecedor de sistema do
     cliente** — hoje não há lugar no padrão. 🔴 **Eu escrevi "não dá para dizer de quem é" sem
     um `grep` no corpus.**
779. 🟢 **Item 778 decidido pelo Vinicius em 25/09: fornecedor de sistema do cliente fica na pasta
     do cliente, como fornecedor da integração.** Registrado em `Moda Objetiva › pessoas.md ›
     Tecnologia`. 🔴 **Correção de número:** o domínio tem **2 pessoas, não 3** (itens 766 e 778)
     — `mauricio@` (5 reuniões) e `alex.moraes@` (3), **as duas no cabeçalho `convidado`**, ou
     seja, **participantes**, não mencionadas. **8 ocorrências** estava certo.
     ⚠ **O padrão precisa acolher isto em todo cliente:** a Hering também declara ERP `Ilimitar`,
     e qualquer cliente com integração terá contato de fornecedor. Hoje a subseção existe só aqui.
780. 🔵 **Onde vive a linha do tempo da CASA? Decisão do Vinicius.** O acervo da Juliana é o
     primeiro que mostra o que está acontecendo **na uMode**, não num cliente: um **programa de
     migração de sistema** em cinco frentes (ago–set/2026), a semana de `Reconhecimento do Novo
     Sistema`, `BrainWave` e `Agentes e Clientes` em 22/09. 🔴 **`jornada.md` é classe de
     cliente; a Casa não tem uma.** Criar seria classe nova, e isso não é meu. **Hoje ela está no
     registro de 25/09 da Juliana e em 25 arquivos `*_casa_*` do `_inbox-calls/`.** Opções:
     (a) `jornada.md` da Casa em `00_Institucional/_contexto/`; (b) por área, no `contexto-area.md`
     de quem é dono do assunto (a migração seria de `03_Produto-e-Solucoes` ou `06_Tecnologia`).
781. 🟢 **Os dois acervos agora formam UMA linha do tempo por cliente**, e destino e natureza
     saem do **e-mail**, como o `protocolo-entrada-de-call.md` § 4 já mandava e o extrator não
     fazia: **24 `jornada.md`** com a linha do tempo (eram 13), coluna `Natureza` (`externa` ·
     `interna` · `não confirmada`) e coluna `Acervo`. 🔴 **Reunião interna SOBRE o cliente deixou
     de parecer reunião COM o cliente** — era o defeito que o protocolo descreve com a Caedu.
     ⚠ **Cabeçalho só com nomes** (34 dos 40 da Juliana) é resolvido pelo índice do corpus,
     mais estrito que o `_por_token`; **um nome que não resolve deixa a reunião `não confirmada`.**
782. 🔴 **CORREÇÃO: relatei "37 cabeçalhos só com gente da uMode" no acervo da Juliana.** Eram
     cabeçalhos **sem e-mail**; conjunto vazio passava no teste de subconjunto. Pego antes de ir
     para o corpus. **E dois defeitos do extrator achados no mesmo passo:** e-mail **pessoal** do
     cabeçalho ia para o front-matter do inbox (**T0**, agora omitido e contado), e o rótulo de
     falante aceitava trecho de fala como nome (`eu falava`) — agora só nome próprio.
783. 🟢 **Item 780 decidido pelo Vinicius em 25/09: a Casa tem `jornada.md`.** Criado em
     `00_Institucional/_contexto/jornada.md`, mesma estrutura de títulos do de cliente, com a
     linha do tempo gerada pelo extrator **por série de reunião** (a Casa tem séries paralelas:
     16 séries, 13 com reunião nos últimos 90 dias, 81 compromissos por vir). **Emenda no
     `CONTEXT.md` › `## Regras travadas`** e no glossário; `gera-fatos.py` passou a cobri-lo.
     O registro da Juliana ficou `SUPERSEDED` só na § 2. 🔴 **O fato mais importante da Casa
     hoje não tem fonte:** o **escopo do programa de migração** — de qual sistema para qual,
     quais clientes, que prazo. **Status e fase da Casa também não são declarados por ninguém.**
784. ⚠ **A série `Hora do K.A.FÉ` aparece incompleta na jornada da Casa:** 4 sessões com cabeçalho
     só de umoder entram; **10 sem cabeçalho ficam `não confirmada`** e fora. É o custo do
     fail-closed. 🔵 **Se o Vinicius declarar que série de título interno é da Casa mesmo sem
     cabeçalho** (`K.A.FÉ`, `Tech & Produto · Weekly`, `Estratégica de Produto`), a regra vira
     lista explícita de séries — nunca inferência pelo título.
785. 🟢 **Acervo da Marina Santoro processado junto com os outros dois:** **357 reuniões distintas**
     nos três acervos, **21 em comum** entre eles (viraram uma só), **1.522 propostas em 210
     arquivos** do `_inbox-calls/`, **28 `jornada.md` de cliente** com linha do tempo + a da Casa
     (29 reuniões, 20 séries). É o acervo de **implantação e integração**: é a fonte principal de
     **Recco (11 de 11), NK Store (10 de 10), Osklen (10 de 12), Lenny Niemeyer (9 de 11)**. Registro: `_recebido-2026-09-25-acervo-reunioes-
     marina-santoro.md`.
786. 🚨 **VIX está `Ongoing` e sem reunião nos três acervos há 360 dias** (última: `API de
     Qualidade`, 30/09/2025). ⚠ **Não prova abandono** — a conta pode estar com quem não entregou
     acervo. **Mesma pergunta da Oficina Reserva (item 769): quem atende hoje?**
787. 🔵 **194 gravações da Marina (96 GB) não foram lidas, e 122 não têm resumo do Gemini.** O
     conteúdo dessas 122 reuniões **só existe em vídeo**. Transcrever exige reconhecimento de
     fala em escala — tempo de máquina alto, e a transcrição bruta não entra no repositório.
     **Decisão do Vinicius:** transcrever (tudo, ou só as 122 sem resumo, ou só as de conta viva),
     ou registrar como fora de escopo. ⚠ **E 4 anexos não lidos** (3 planilhas, 1 apresentação)
     — nomes no registro; podem ter dado de cliente.
788. ⚠ **`RSV` não roteou.** `RSV + uMode · Checkpoint #3` (29/05/2025) pode ser **Reserva**, mas
     **nenhuma fonte do corpus declara esse apelido.** 🔵 **Confirmar** — se for, entra em
     `### Aliases do cliente` do `institucional.md` da Reserva, e o extrator passa a ler de lá.
789. 🔴 **CORREÇÃO do item 788: o corpus JÁ declarava `RSV` como apelido da Reserva** — no
     `institucional.md` dela, `### Aliases do cliente`. Eu escrevi "nada no corpus declara" sem
     ler. **Quinta variação de "ausência de fonte é hipótese" nesta sessão.** O Vinicius
     confirmou em 25/09. 🟢 **Conserto de método, não de caso:** o extrator passou a ler os
     apelidos do `institucional.md` de cada cliente (55 lidos, os de blockquote e os nomes de base
     excluídos), em vez de lista escrita à mão.
790. 🟢 **Atendimento registrado com o tempo explícito — informado pelo Vinicius em 25/09/2026:**
     🔄 **Hoje:** VIX = **Julianne Dias Rodrigues + Pedro Murillo** (confirmado) · Oficina Reserva =
     **Fernanda Araujo** (o CRM dizia Holmer & Laura — virou histórico) · Lofty Style = **Laura
     Delgado Cardoso** (confirmado). ⏭ **Por vir:** a **Fernanda fica na uMode até 30/09/2026**;
     com a saída dela, a **Laura** passa a atender **Reserva, Oficina Reserva e NV** e segue com a
     Lofty. ⚠ **Reserva e NV:** o atendimento atual segue o do CRM — o Vinicius não o alterou.
     🟢 O `gera-fatos.py` ganhou a fonte `informado pelo Vinicius`, e os fatos de Oficina Reserva,
     VIX e Lofty passaram a citá-la. **Data exata da passagem: `[a preencher]`.**
791. ⏰ **Revisitar em 01/10/2026 — isto vence.** Na saída da Fernanda: (a) a ficha
     `fernanda-araujo.md` passa a `desligada`, e o `gera-fatos.py` marca `⚠ DESLIGADO` nos fatos
     de atendimento dela; (b) Reserva, Oficina Reserva e NV trocam o atendimento vigente para a
     Laura, com a data real da passagem; (c) a jornada da Casa registra o marco. 🔴 **O fato de
     hoje não tem validade embutida** — é a mesma lacuna de sempre (fato sem intervalo), e aqui
     ela tem data marcada para virar erro se ninguém voltar.
792. 🟢 **Conferência contra a fala: 188 propostas de 32 reuniões com transcrição, todas conferidas.**
     **149 confirmadas (79%) · 38 parciais (20%) · 1 não encontrada · 0 contraditas.** Feita por
     subagentes com o método por escrito; vereditos em `_inbox-calls/_verificacao-na-fala.tsv`,
     marcados em cada linha do inbox. 🔴 **O critério que sai daqui — o resumo do Gemini acerta
     o FATO e erra o DONO:** das parciais, a causa mais frequente é **pessoa errada** (quem disse,
     quem assumiu); depois, **intenção ou pedido registrado como decisão ou compromisso** ("tô
     querendo eliminar" virou "foi decidido"), e **responsáveis diferentes fundidos** sob "o grupo".
     ⚠ **Consequência:** o `por vir` com dono, e a detecção de compromisso órfão (item 776), só são
     confiáveis depois da conferência. **Proposta de resumo não conferida não deve virar fato de
     responsabilidade.**
793. 🔴 **Em reunião PRESENCIAL, o rótulo de falante é o dono do aparelho, não quem fala.** Na
     `CAEDU (presencial)` de 29/04/2025, **84 falas** saem como "Mauricio" e são várias vozes, da
     Caedu e da uMode. **Nem a transcrição com falante resolve quem disse o quê** nesse caso.
     🔵 **Regra proposta:** reunião com uma sala num aparelho só (título com "presencial", ou um
     falante com fatia desproporcional das falas) tem identidade de falante `não confiável`.
     ⚠ Pode ser a mesma raiz da `Rose` da CAEDU no Tactiq (733 falas, item 762) — **não verificado.**
794. 🟢 **Regra do presencial (item 793) aplicada nas 53 transcrições Tactiq da CAEDU.** Quatro
     sinais por reunião: `presencial` no título, um rótulo com fatia desproporcional, o rótulo
     dizendo o próprio nome, marcas de sala. **Dispara em UMA:** `CAEDU presencial` de 29/04/2025 —
     `Mauricio` com 71% das falas é o aparelho. 🟢 **E a `Rose` NÃO é sala:** chamada pelo nome
     51 vezes em 7 reuniões, nunca diz o próprio nome, e os outros nomes da CAEDU aparecem em
     terceira pessoa — **é uma voz só.** Isso **responde metade** da suspeita do item 793; a
     outra metade — `Rose` é a `Roselene`? — **segue aberta** e só o e-mail fecha.
     ⚠ **Limite do teste:** ele pega sala com várias vozes que se chamam pelo nome. Duas pessoas
     no mesmo aparelho que não se chamam passam despercebidas.
795. 🟢 **Chave nova no vocabulário fechado: `processo` — como a área trabalha HOJE.** Acrescentada
     ao `protocolo-fato-atomico.md` § 4, como o próprio protocolo manda ("se não existir,
     acrescente na tabela primeiro"). 🔴 **Motivo medido:** nas propostas tiradas das gravações, **11
     de 28 `decisao` (39%) eram descrição de processo** — "o estilo faz a ficha e o sourcing envia"
     não é decisão de ninguém. É o mesmo erro que a conferência contra a fala mediu no resumo do
     Gemini (item 792): **prática ou intenção registrada como decisão.** Reclassificadas por
     subagente, só a chave mudou. ⚠ **Quatro casos ficaram no limite** e seguem como `decisao`
     com a ressalva registrada pelo subagente.
796. 🟢 **O presente das contas vivas que só tinha resumo foi conferido contra a GRAVAÇÃO.** As 8
     reuniões recentes com vídeo no acervo da Marina — Caedu 17/08, Lofty CriAI 20/08, Loungerie
     (4, de 29/07 a 14/09), NK Store 30/06, NV 07/07 — foram transcritas por máquina e conferidas
     por subagente: **77 propostas · 33 confirmadas · 44 parciais · 0 contraditas.** 🔴 **A
     maioria das parciais é dono não verificável** — a transcrição automática não tem falante,
     então confirma o QUE, não o QUEM. ⚠ **E o resumo do Gemini erra mais do que dono:** **prazo**
     (fala "até março", resumo "até maio", kick-off da Loungerie) e **verbo** (fala "explorar e
     testar", resumo "implementar", NK Store). 🔵 **Sem gravação, continuam só com resumo:** Moda
     Objetiva (7 reuniões de jul–ago), Lofty 09/09 e 10/09, Reserva 14/07, TDC 15/07.
797. 🔴 **Isolamento de cliente aplicado às propostas — e havia vazamento.** Varridas as linhas do
     `_inbox-calls/`: **6 citavam outro cliente, 2 eram vazamento real** — "a solução para o
     problema da **Osklen**" no registro da **Lenny**, e "a **Reserva** ainda demanda muito" no da
     **Recco**; nas gravações, combinados da **Cambos** e KRs da **Luiza Barcelos** apareceram em
     reuniões "da NK". 🟢 **Conserto de método:** o extrator omite proposta que cita outro cliente
     por **nome próprio** (inicial maiúscula — "oficina" e "reserva" também são substantivos
     comuns), e a tabela de verificação ganhou o veredito `fora_do_cliente` para o que o teste não
     pega. A instrução dos subagentes passou a mandar omitir. ⚠ **Mantido de propósito:**
     "(reserva e oficina)" na homologação conjunta das duas contas do mesmo grupo.
     🔴 **E o filtro vale só para registro de CLIENTE.** Na primeira versão ele omitiu 37 propostas —
     35 eram de reuniões da **Casa** ou sem destino, que falam de clientes legitimamente
     ("configurar a ficha da NV"). **O isolamento é entre clientes; a Casa enxerga todos.**
798. 🟢 **Roteamento manual, com motivo e data, para quando título e e-mail enganam.**
     `_inbox-calls/_roteamento-manual.tsv`, lido pelo extrator antes do título. Primeira linha: a
     gravação `[Luiza & NK] Projeto com Líder de Marca` (13/11/2024) caía na **NK Store** — "Luiza"
     sozinho não casa com a pasta — e é **inteira sobre a crise do projeto da Luiza Barcelos**: o
     estilo esperava ferramenta de desenho, o uFlow é de gestão, e o faseamento proposto (merch e
     desenvolvimento até jan, integração Safe Tech a partir de jan, suprimentos em mai).
     🔴 **Fora do inbox, de propósito:** a fala de que o cliente **cancelaria** sem ferramenta de
     desenho — é condição de contrato (`T1`) e só pode viver na pasta da LB. 🔵 **Decisão do
     Vinicius:** registrar esse risco de cancelamento na `jornada.md` da Luiza Barcelos, com a data.
799. 🟢 **Item 798 decidido pelo Vinicius em 26/09/2026 — e com o tempo certo.** O risco de
     cancelamento de 13/11/2024 **aconteceu e foi superado**: registrado no `Histórico de
     incidentes` da `jornada.md` da LB (pasta do cliente, onde `T1` pode viver). 🔄 **O presente é
     outro:** sem risco de cancelamento; **nova fase em planejamento — integração de ESCRITA, que a
     conta não tem hoje, e possível reonboarding.** 🟢 **Isso responde a dúvida que a jornada
     deixava aberta** ("estabilizada ou desengajada?"): a queda de reuniões de 2026 é intervalo
     antes de nova fase, não saída. ⏭ **Data e escopo da nova fase: `[a preencher]`.**
800. 🔴 **Defeito de TEMPO dentro do próprio `gera-fatos.py`, corrigido — 74 fatos recuperaram a
     data real.** Numa linha de tabela da `jornada.md`, a procedência do BLOCO sobrescrevia a data
     da LINHA: o incidente de 08/08/2025 da Luiza Barcelos saía como fato de **2026-09-21** (a data
     da varredura), os chamados de jan/2026 da VIX como de 2026-09-22. **É o erro que o corpus
     inteiro combate (item 773) — cometido pelo gerador.** 🟢 Agora: **data e fonte da linha
     vencem**; a coluna só é lida como fonte se o cabeçalho diz "Fonte/Origem" (a coluna "Estado"
     virava procedência — `[Não iniciada · 2026-01-28]`); sem coluna de fonte, vale a procedência
     escrita na própria linha. **2 fatos passaram a `[sem fonte]`** — antes tinham status de
     chamado no lugar da fonte; agora a lacuna aparece como lacuna.
