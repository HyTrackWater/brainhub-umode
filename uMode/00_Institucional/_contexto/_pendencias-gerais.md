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
