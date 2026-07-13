# STATE.md — Estado do projeto

> Estrutura fixa. Não repetir objetivo aqui — ver `CONTEXT.md`.
> Este arquivo só registra **avanço**: o que foi feito, o que está em andamento, o que vem a
> seguir e o que está no backlog (priorizado conforme a fila anda).

## Sprint atual
**Sprint 02 — Estrutura de pastas no Drive + simulação com clientes-piloto**

### Em andamento
- [ ] Testar template de cliente com ao menos 5 clientes reais (fase cadastral)
      — Luiza Barcelos: ✅ concluído (v1)
      — Cambos: ✅ concluído (v1)
      — Lofty Style: ✅ concluído (v1)
      — Moda Objetiva: ✅ concluído (v1)
      — Cliente 5: pausado — prioridade agora é pilotar o modelo de demandas com 1 cliente
        já cadastrado antes de expandir para um 5º
- [x] Migração para repositório Git (Claude Code) — **concluída em 10 jul 2026**. Todo o
      projeto (CONTEXT.md, CLAUDE.md, STATE.md, `uMode/`, `docs/`, `scripts/`, e as pastas de
      dados brutos usadas como fonte) commitado e enviado (`push`) para
      `github.com/HyTrackWater/brainhub-umode` (branch `main`, commit `6867890`, 1267 arquivos).
      Antes só existia 1 commit trivial no repositório — 21 sessões de trabalho estavam
      sentadas como alterações não commitadas na máquina local, sem backup nenhum. Corrigido a
      pedido explícito do Vinicius (preparação para migrar de workspace do Claude Code).
- [x] Piloto de demandas com Lofty Style — **formalizado**. 85 arquivos `D-AAAA-NNN.md` em
      `uMode/_Clientes/Lofty Style/00_Institucional/_demandas/`, estrutura idêntica ao
      template (validado por diff), campos vazios sempre `[a preencher]`
- [x] Piloto de RFIs com Lofty Style — **formalizado**. 15 arquivos `RFI-AAAA-NNN.md` em
      `uMode/_Clientes/Lofty Style/00_Institucional/_rfis/`, mesma validação estrutural
- [x] **Demandas/RFIs replicadas para Cambos, Luiza Barcelos e Moda Objetiva** — mesmo padrão
      de Lofty, agora a partir de um export "Totais" (todos os clientes) achado em
      `Demandas Totais CSV e Markdown/` e `RFIs Totais CSV e Markdown/` (narrativa já em
      markdown, não precisou extração de HTML desta vez). 151 demandas + 7 RFIs gerados:
      Cambos 47+3, Luiza Barcelos 70+4, Moda Objetiva 34+0 (cliente ainda não tem RFI real).
      Scripts reutilizáveis criados em `scripts/gen-demandas.ps1` e `scripts/gen-rfis.ps1`
      (parametrizados por cliente — servem para o cliente 5 e para reprocessar se o Notion for
      re-exportado). Tabela de tradução Status+Etapa e Tipo do `protocolo-gestao-demanda.md`
      **estendida** com 9 combos novos achados nos dados reais desses 3 clientes (todos
      registrados no protocolo antes de aplicar, seguindo a regra já travada). Todos os 151+7
      arquivos validados por diff de headings contra o template — 0 divergências.
- [x] **Auditoria final de padronização em todos os níveis** (pedido explícito do Vinicius) —
      conferido `institucional.md`/`jornada.md`/`pessoas.md` dos 4 clientes, `contexto-area.md`
      das 8 Áreas da Casa, as 4 fichas de Pessoa, e as 85+151 demandas / 15+7 RFIs, todos por
      diff de headings contra o template correspondente. Resultado: tudo bate, exceto 2 achados
      novos registrados em `_pendencias-gerais.md` (itens 8 e 9) — o variante 1ª-pessoa do
      `contexto-area.md` das 8 Áreas da Casa nunca foi formalizado como template próprio; e
      **nenhum dos 4 clientes-piloto tem `contexto-area.md` preenchido em nenhuma das 14 áreas**
      (gap de conteúdo real, não erro desta sessão — só a primeira vez que essa camada foi
      checada especificamente).
- [ ] Varredura Google Drive (pasta hub institucional) — retomada, foco em ferramentas
      internas/produtos × Áreas. Notas em
      `uMode/00_Institucional/_contexto/_varredura-drive-notas.md`. `Histórico (2025)` do
      design org já lido (confirmado: evolução do mesmo organograma, não taxonomia nova). As
      58 atas de Lofty amostradas (5 lidas na íntegra) e encerradas — conteúdo é Q&A técnico
      de mapeamento de campo ERP↔uFlow, não institucional, já coberto pelos marcos de
      `jornada.md`; por decisão do Vinicius, não lidas as 53 restantes. Pendente: 3 páginas
      Notion linkadas no CRM, pasta Drive própria de Lofty
      (`1sP7YqvkGtyoCXkk6BUZwaUzIBaK9JHXV`) — Notion fica para o próximo momento (decisão do
      Vinicius)
- [x] `Sistema-Operacional/*.html` lido na íntegra — deck institucional (28 mai 2026): tese do
      pivot, dogfooding real (74→28 pessoas, 22 SaaS→2), e a arquitetura "Sistema Operacional
      uMode" como 5 componentes (CadastrAI-Conhecimento, Hub de Agentes, Sync Engine,
      Indicadores, SMART CODE). `institucional.md` da Casa ganhou nova seção "Contexto crítico"
      com a narrativa completa do pivot. Tentativa inicial de tratar os 5 componentes como
      substituição do Portfólio interno em `CONTEXT.md` foi corrigida depois de achar um
      documento mais recente e mais diretamente sobre BrainHub (ver item abaixo) — os 5
      componentes ficaram documentados como nível de arquitetura de operação, à parte do
      Portfólio de produtos, nunca fundidos.
- [x] `brainhub_mapa.html` ("BrainHub — Mapa-mãe · uMode", 10/06/2026, o mais recente e
      diretamente sobre BrainHub encontrado até agora) e `arquitetura_umode_4.extracted.txt`
      ("Arquitetura uMode — Especificação por Módulo", 24/04/2026) lidos na íntegra — ambos do
      CEO. Confirmaram que a lista original do Portfólio interno em `CONTEXT.md` (CadastrAI,
      Taxonomia, CX Hub, ONB HUB, IntHub, Gest Hub, Sales Hub) estava certa — a edição anterior
      (que a tinha substituído pelos 5 componentes) foi revertida. Confirmação extra via
      `launch.json` do CEO: repositório de código ativo para CX Hub, ONB HUB, IntHub e Gest
      Hub. Achado também: regra de arquitetura do produto real citada como "não-negociável" —
      "toda marca herda a mesma estrutura, não existe campo custom" — validação direta da
      mesma filosofia de padronização que já seguimos no BrainHub. O Mapa-mãe trouxe ainda uma
      3ª lista de 8 Áreas internas (com "Jurídico", que não existe nas outras duas) — por
      decisão do Vinicius, documentos externos são fonte de informação, não de estrutura; as 8
      Áreas já travadas em `CONTEXT.md` não foram alteradas, só registrada a pendência.
- [x] Documento central de pendências criado: `_pendencias-gerais.md`
      (`uMode/00_Institucional/_contexto/`) — consolida dúvidas antes espalhadas em notas de
      varredura e observações de cliente (Cadeira×Área, Taís Moser, ERP/Notion de Luiza
      Barcelos, CRM desatualizado, etc.), todas ainda aguardando decisão do Vinicius/CEO.
- [x] Novo tipo de MD criado: **ficha de Pessoa** (`_template_pessoa.md` +
      `protocolo-gestao-pessoas.md`) — operacionaliza regra já travada ("Pessoa vive só em
      Casa › Pessoas"), nunca implementada como arquivo até agora. 4 fichas reais geradas
      (Laura Delgado Cardoso, Andrea Goulart Holmer dos Santos, Marina Gonçalves Santoro,
      Vanessa Rinaldi Ornelas Engman) — as 4 pessoas com dado mais sólido, confirmadas
      atendendo os 4 clientes-piloto (não só Lofty — mesmo time serve os 4). Estrutura
      validada por diff, 0 divergências. Campos de personificação (personalidade,
      autodescrição) ficam `[a preencher]` até formulário — nunca inferidos de documento.
- [x] `institucional.md`, `jornada.md`, `pessoas.md` dos **4 clientes-piloto** (Lofty Style,
      Cambos, Luiza Barcelos, Moda Objetiva) enriquecidos com dado real do CRM "Mapa de
      Clientes" e da base "Reuniões Compartilhadas com Clientes" (Drive/Notion-Export): CNPJ,
      módulos contratados, time de atendimento com nomes completos, timeline de marcos
      reconstruída por cliente (a mais rica: Luiza Barcelos, 111 reuniões desde jun/2024).
      Discrepâncias entre fontes registradas como observação em cada cliente, nunca resolvidas
      por conta própria (ex.: Status "Onboarding" no CRM vs "Ongoing"/"Operação Assistida" já
      registrado, em Lofty e Luiza Barcelos).
- [x] **Correção estrutural em todos os 4 clientes** — auditoria pós-enriquecimento achou
      divergências pré-existentes (de antes desta sessão) entre `jornada.md`/`pessoas.md` e o
      template: seções inteiras faltando (Lofty Style e Moda Objetiva tinham só 3-4 das 9
      seções de `jornada.md`; Cambos e Luiza Barcelos faltavam 1-2 cada), heading fora de
      ordem (Luiza Barcelos `pessoas.md`: "Diretoria e decisores" e "Financeiro" na posição
      errada), heading renomeado (Moda Objetiva: "Stakeholders por área" → "Time do projeto
      por área"). Todas as 12 combinações (4 clientes × institucional/jornada/pessoas)
      revalidadas por diff — 0 divergências, exceto uma conhecida e sinalizada (Luiza Barcelos
      `institucional.md` tem `### ERP` e `### Notion (cadastro de cliente)` como subseções
      extras, pré-existentes — decisão pendente do Vinicius: formalizar no template ou
      remover).

### Concluído nesta sprint
- [x] Mapeamento e consolidação das 14 áreas canônicas do cliente de moda (ver `CONTEXT.md`)
- [x] Lista final de áreas dos clientes recebida e cruzada — 3 novas áreas adicionadas
- [x] Portfólio completo documentado: 9 produtos voltados ao cliente + 7 internos
- [x] Vínculo `conecta_area_cliente` definido para cada produto externo
- [x] Estrutura de pastas criada no Drive: uMode (8 áreas) + _Clientes/_template_cliente
- [x] Convenção `_contexto` e `_protocolos` por pasta definida e aplicada em toda a estrutura
- [x] Templates de MD criados: `institucional.md`, `jornada.md`, `pessoas.md` e
      `contexto-area.md` em todas as áreas do template de cliente e da uMode
- [x] Protocolo de criação de cliente criado em `uMode/00_Institucional/_protocolos/`
      — fluxo de 5 passos projetado para execução por agente
- [x] 3 novas áreas canônicas adicionadas (Design · Modelagem · Engenharia)
- [x] Luiza Barcelos: pasta criada no Drive + v1 dos 3 arquivos de contexto institucional
- [x] Cambos: pasta criada no Drive + v1 dos 3 arquivos de contexto institucional
- [x] Lofty Style: pasta criada no Drive + v1 dos 3 arquivos de contexto institucional
- [x] Moda Objetiva: pasta criada no Drive + v1 dos 3 arquivos de contexto institucional
- [x] Padrão de contextualização de fase cadastral validado com 4 clientes — template estável
- [x] Contexto institucional da uMode preenchido a partir do Drive do CEO:
      `institucional.md` + `contexto-area.md` para todas as 8 áreas internas
- [x] Modelo de demandas desenhado e formalizado: natureza, ciclo de vida, marcos (log
      append-only), hierarquia pai/filha, mecanismo de aprovação/retroalimentação — registrado
      em `CONTEXT.md` (`## Demandas`) e detalhado em
      `uMode/00_Institucional/_protocolos/protocolo-gestao-demanda.md`
- [x] Nova subpasta fixa `_demandas/` criada no nível Institucional da Casa e do
      `_template_cliente`, com `_template_demanda.md`
- [x] Taxonomia de demanda refinada com dados reais do Notion (legado) e do CX Hub (padrão
      oficial): Status, Prioridade, Tipo, Área (CX Hub), Origem (CX Hub), Responsável/
      Co-responsáveis, datas, horas, motivo de bloqueio, Subdemandas — regra travada de nunca
      fundir taxonomia organizacional com a do CX Hub
- [x] RFI modelada como entidade própria (nasce sempre de dentro de uma demanda, vínculo
      bidirecional `RFI vinculada` ⟷ `Demanda relacionada`); nova subpasta fixa `_rfis/` só do
      lado de cliente, com `_template_rfi.md`; registrada em
      `uMode/00_Institucional/_protocolos/protocolo-gestao-rfi.md`
- [x] Campos de RFI ajustados contra a tabela real do Notion: `Justificativa da estimativa`
      (condicional > 10h) e "Aprovação de escopo (De Acordo)" incorporados; 3 colunas
      redundantes descartadas com registro de equivalência para a migração futura
- [x] `docs/volumetria-hierarquia.html` atualizado para v0.2 — regra de "Comunicação" corrigida
      (demanda não é mais só Casa↔cliente) e nova seção "Demandas & RFI" adicionada
- [x] 85 demandas de Lofty Style com narrativa completa em staging — export HTML do Notion
      (não CSV) provou ser a via confiável para extrair conteúdo de página em lote

---

## Sprint 01 — Sacramentar volumetria e hierarquia ✓ concluída

- [x] Desenho da volumetria: Plataforma → Casa / Cliente, com 4 níveis
- [x] Regras travadas: Áreas/Pessoas iguais; Subáreas livres; vínculo de atendimento;
      canal demanda/contexto; isolamento entre clientes
- [x] HTML de registro `volumetria-hierarquia.html` criado e adicionado ao projeto
- [x] `CONTEXT.md` e `STATE.md` criados
- [x] 8 Áreas internas confirmadas
- [x] Decisão travada: Produtos são subáreas com atributo `tipo: produto`
- [x] Decisão refinada: cada Produto carrega atributo `conecta_area_cliente`

## Próximas atividades (fila da Sprint 02)
1. **Frente ativa: BrainWave/frontend.** `brainwave/01-esqueleto.md`, `brainwave/02-home.md`,
   `brainwave/03-uMode-e-clientes.md`, `brainwave/04-seletor-cliente-ativo.md` e
   `brainwave/05-solucoes.md` enviados, todos aguardando o Vinicius trazer o `## Resultado`
   formal de volta pra registrar aqui. A tarefa 03 reestrutura o menu principal (remove as abas
   soltas "Instituições" e "Pessoas", cria "uMode" e "Clientes", cada uma com 4 sub-abas:
   Instituições/Áreas/Subáreas(desabilitada)/Pessoas, com "cliente ativo" escopando Áreas/Pessoas
   dentro da aba Clientes) — conteúdo validado pelo Vinicius em 13 jul 2026. Ao navegar no
   resultado da tarefa 03, o Vinicius identificou que o "cliente ativo" não ficava
   visível/trocável fora da sub-aba Instituições — a tarefa 04 corrige isso: seletor de cliente
   fixo em todas as 4 sub-abas, estado vazio quando nenhum cliente está ativo, e filtro opcional
   por Área na sub-aba Pessoas. A tarefa 05 renomeia "Produtos" pra **"Soluções"**: grade única
   dos 16 do Portfólio (sem sub-abas), filtros combináveis (Destino/Geração/Maturidade — os dois
   últimos são campos novos), cadastro por solução, com "Clientes que contrataram" deixado como
   pendente/placeholder (ver "Decisões em aberto" abaixo — entidade Solução×Cliente ainda não
   formalizada). `brainwave/CONTEXTO.md` (tabela de navegação) já atualizado pra refletir as
   tarefas 03, 04 e 05.
2. Preencher `contexto-area.md` real das 14 áreas em pelo menos 1 cliente-piloto (gap achado na
   auditoria final de 10 jul — 0 de 56 combinações cliente×área preenchidas hoje; exige dado
   real por área, não dá para formalizar sem levantamento novo)
3. Decidir com o Vinicius: formalizar o variante 1ª-pessoa de `contexto-area.md` das 8 Áreas da
   Casa como template próprio (`_pendencias-gerais.md` item 8)
4. Definir a escala/critério de triagem do campo `Nível HIC` (Pessoa) — hoje só o campo existe
5. Continuar a varredura Google Drive com foco em ferramentas internas × Áreas — próximos
   destinos: pasta Drive própria de Lofty, 3 páginas Notion linkadas no CRM
6. Revisar com o Vinicius as pendências centralizadas em `_pendencias-gerais.md` (9 itens):
   Cadeira×Área (3 taxonomias diferentes), `Área (CX Hub)`="OPERAÇÃO" sem match, Tamanho
   atendimento×Grupo de segmentação, Taís Moser (uMode ou cliente?), "Laura" da Alocação
   contratual, `### ERP`/`### Notion` em Luiza Barcelos, CRM desatualizado, os 2 achados da
   auditoria final (itens 8 e 9)
7. Cadastrar cliente 5 e fechar validação do template com 5 cases (retomado após o piloto
   de demandas)
8. Montar simulação de fluxos para apresentação 17/07
9. Decidir sobre o formulário de personificação de Pessoas (Lovable) — campos documentáveis
   já estão preenchidos nas 4 fichas existentes; falta só a parte de personificação

## Backlog (não priorizado / aguardando a fila andar)
- Subáreas internas da Casa por Área (nomes — contexto vem com o CEO)
- Fluxo interno de People (reuniões, transcrições, controle de atividades)
- Formulário interno de cadastro de clientes (após validação dos 5 cases)
- Matriz de permissionamento por tipo de demanda/RFI
- Plano de migração estrutura de pastas → banco de dados
- Definição de agentes (tipo, escopo, gatilho)

## Decisões em aberto
- **Entidade "Solução × Cliente".** O Vinicius travou em 13 jul 2026 que a relação entre uma
  Solução do Portfólio e um Cliente que a contratou precisa virar entidade própria (condução,
  integração, particularidades por cliente) — não só um campo de referência. Formalizar
  (protocolo + template + onde vive) fica pra depois da varredura de nomenclatura legado→novo
  (ver `CONTEXT.md` → "Nomenclatura legado → novo Portfólio"). A tela de Soluções (task 05 do
  BrainWave) já foi desenhada prevendo esse link, com o clique em "Clientes que contrataram"
  reservado/placeholder até a entidade existir.

## Log de sessões
- **30 jun 2026** — Sessão 1: volumetria desenhada e travada; HTML gerado; CONTEXT.md e
  STATE.md criados; rascunho de Áreas internas proposto.
- **01 jul 2026** — Sessão 2: 8 Áreas internas confirmadas; decisão sobre Produtos como
  subáreas; Sprint 01 encerrada; Sprint 02 aberta.
- **01 jul 2026** — Sessão 3: refinamento vínculo Produto↔Área cliente via `conecta_area_cliente`.
- **01 jul 2026** — Sessão 4: portfólio completo mapeado; 11 áreas canônicas definidas.
- **02 jul 2026** — Sessão 5: estrutura completa de pastas no Drive; MDs template criados;
  protocolo de criação de cliente escrito; 3 novas áreas adicionadas (14 no total).
- **03 jul 2026** — Sessão 6: template atualizado com `jornada.md` e `pessoas.md`;
  Luiza Barcelos criada no Drive com v1 dos 3 arquivos institucionais; padrão de
  contextualização de fase cadastral estabelecido; pronto para replicar com próximos clientes.
- **06 jul 2026** — Sessão 7: Cambos, Lofty Style e Moda Objetiva criados no Drive (v1);
  template validado com 4 clientes — padrão estável; contexto institucional da uMode
  preenchido a partir do Drive do CEO (institucional.md + 8 contexto-area.md); migração
  para repositório Git iniciada.
- **06 jul 2026** — Sessão 8: cadastro do cliente 5 pausado a pedido do CEO/Vinicius —
  prioridade passou a ser modelar o conceito de Demandas antes de escalar para mais clientes.
  Modelo formalizado: natureza (interna/inter-área/intra-área/casa-cliente), ciclo de vida,
  marcos como log append-only (distintos dos marcos de `jornada.md`), hierarquia pai/filha,
  e mecanismo de retroalimentação (agente propõe mudança de contexto, pessoa com permissão
  no campo "Governança" do MD-alvo aprova, demanda registra o marco da aprovação). Decisão
  de estrutura: demanda vive 1x em `00_Institucional/_demandas/` por casa/cliente, nunca
  duplicada por área. `CONTEXT.md` atualizado (`## Demandas` + Glossário); criado
  `protocolo-gestao-demanda.md` e `_template_demanda.md` (Casa + `_template_cliente`).
  Na sequência, taxonomia refinada com os dados reais do Notion (legado) e do CX Hub
  (ferramenta oficial adotada a partir de agora): Status, Prioridade, Tipo, Área (CX Hub —
  squad interna, sem relação com a Área organizacional), Origem (CX Hub — motivo/gatilho,
  distinto de Origem organizacional), Responsável/Co-responsáveis, datas previstas/reais,
  horas, motivo de bloqueio, RFI vinculada e Subdemandas (checklist tático, distinto de
  Demanda filha). Regra travada: as duas taxonomias (organizacional × CX Hub) nunca se
  fundem — todo campo que colide de nome carrega a etiqueta de origem. RFI em si fica para
  depois do piloto. Próximo passo: escolher 1 cliente já cadastrado para pilotar demandas
  reais.
- **06 jul 2026** — Sessão 9: RFI modelada como entidade própria (não é uma demanda) a partir
  dos dados reais do Notion (legado). Toda RFI nasce de dentro de uma demanda — nunca é aberta
  do zero — e o vínculo é bidirecional (`Demanda.RFI vinculada` ⟷ `RFI.Demanda relacionada`).
  Nem toda demanda vira RFI. Ciclo de vida em dois níveis (Grupo: A fazer/Em andamento/
  Concluídos → Status específico, 12 estados) adotado do Notion como base de trabalho —
  sujeito a ajuste quando o CX Hub expuser sua própria taxonomia de RFI. Decisão de estrutura:
  `_rfis/` é subpasta fixa só do lado de cada Cliente (`00_Institucional/_rfis/`), não existe
  do lado da Casa, porque RFI sempre tem um cliente associado. Criado `protocolo-gestao-rfi.md`
  e `_template_rfi.md` (`_template_cliente`); `protocolo-gestao-demanda.md` e os
  `_template_demanda.md` atualizados com a referência cruzada. Próximo passo segue o mesmo:
  escolher 1 cliente já cadastrado para pilotar demandas e RFIs reais; depois, traduzir
  demanda a demanda e RFI a RFI do Notion/CX Hub para este padrão.
- **06 jul 2026** — Sessão 10: revisão da tabela de itens da RFI no Notion (Demanda Cliente,
  Detalhamento Cliente, Estimativa uMode, Comentário uMode) e do bloco "De Acordo". Três
  colunas descontinuadas por redundância (já cobertas por `Demanda relacionada`, `Nome`/
  `Resumo do assunto`, `Horas estimadas`); `Comentário uMode` descartado por decisão do
  CEO/Vinicius. Dois gaps reais incorporados: `Justificativa da estimativa` (obrigatória só
  se Horas estimadas > 10h) e a seção "Aprovação de escopo (De Acordo)" — responsável nomeado
  + data de aprovação dos dois lados (uMode e Cliente), substituindo o antigo campo solto
  `Data aceite do cliente`. Atualizado `protocolo-gestao-rfi.md` (com tabela de campos
  descartados, para consulta na migração) e `_template_rfi.md`.
- **06 jul 2026** — Sessão 11: checkpoint de acompanhamento — conferido que `STATE.md` e os
  templates de Demanda/RFI estavam consistentes entre protocolo e template (sem órfãos).
  `docs/volumetria-hierarquia.html` (registro visual v0.1, de 30 jun 2026, antes do modelo de
  Demandas existir) estava com uma regra desatualizada ("demanda é o único canal entre as
  casas") e sem a camada de Demandas/RFI. Atualizado para v0.2: regra de Comunicação corrigida
  e nova seção "Demandas & RFI" adicionada, espelhando `CONTEXT.md`. Nenhum bloqueio para o
  próximo passo — segue pendente escolher o cliente-piloto.
- **08 jul 2026** — Sessão 12: piloto de Lofty Style escolhido; cliente 5 pausado. 10 demandas
  reais (UMD-209 a UMD-309) coletadas manualmente campo a campo + narrativa completa. Cliente
  trouxe export CSV do Notion (`Untitled...csv`, só Lofty, 14 colunas) e um consolidado
  (`Demandas de Clientes..._all.csv`, 1.007 linhas, 20 clientes, 35 colunas) — confirmado que
  o pequeno é subconjunto exato do grande; adotado o consolidado como fonte estruturada padrão
  para qualquer cliente daqui pra frente. Descoberta crítica: a coluna `Texto` (corpo da
  página) só vem preenchida em 2 das 1.007 linhas — CSV nunca traz a narrativa, só campos de
  banco. As 75 demandas restantes de Lofty (total 85) foram preenchidas com campos
  estruturados via CSV; narrativa marcada `[a preencher]`. Hipótese inicial de formato MM/DD
  para `Data de Previsão de Entrega` foi testada e **corrigida** — o CSV grafado por extenso
  prova formato DD/MM em tudo; a inconsistência (previsão antes da solicitação) é dado ruim
  real do Notion legado, não erro de leitura. Tentativa de acesso direto ao Notion via
  navegador (`claude-in-chrome`): sem sucesso — a sessão de navegador controlada pelo Claude
  está autenticada como `vinicius.risoleo@gmail.com`, sem acesso ao workspace uMode; o
  Vinicius usa `vinicius.risoleo@umode.com.br` no navegador que ele vê — sessões diferentes, e
  Claude não loga por política de segurança. Pendência de acesso registrada em
  `_staging-lofty-demandas.md`; retomar quando resolvida (MCP do Notion com token, ou
  compartilhamento direto da página).
- **08 jul 2026** — Sessão 13: RFI. Vinicius trouxe pasta `Particular e Compartilhado/` com
  export do Notion: CSV filtrado de Lofty (15 RFIs) + CSV consolidado de todos os clientes (87
  RFIs) — mesmo padrão de subconjunto exato validado com as demandas. Pasta que deveria trazer
  o conteúdo de página das RFIs (`RFI Escopo - Lista de Entregáveis/`) veio **vazia** — mesma
  limitação de narrativa das demandas, ainda pior (nem os 2/1.007 casos de exceção). Revisão
  contra `protocolo-gestao-rfi.md` decidida pelo Vinicius, ponto a ponto: (1) "Aprovação de
  escopo (De Acordo)" não é campo de banco — é conteúdo de página; `Data aceite do cliente`
  volta a ser campo estruturado real (não é mais substituído); (2) `Demanda relacionada`
  apontando para nome de cliente em vez de ID de demanda é dívida do Notion legado, resolvida
  na migração RFI a RFI, não muda o padrão; (3) RFI multi-cliente (achado 1 caso: uMode +
  Lofty Style) vira duas RFIs separadas na migração — regra "RFI = 1 cliente" mantida; (4)
  `Cobrada? (sim/não)` mapeado para o campo `Cobrado` do CSV (Sim/Não/vazio), campo `Cobrada?`
  com emoji é ruído descartado; (5) `Task (Linear)` — e qualquer referência a Linear —
  descartado do modelo; (6) `Data planejada de execução` passa a aceitar data única ou
  intervalo. `protocolo-gestao-rfi.md` e `_template_rfi.md` atualizados. Criado `_rfis/` para
  Lofty Style com `_staging-lofty-rfis.md` — 15 RFIs completas em campos estruturados,
  narrativa pendente do mesmo acesso ao Notion.
- **08 jul 2026** — Sessão 14: acesso ao Notion testado via navegador (`claude-in-chrome`) —
  funcionou para a base de Demandas (não RFI ainda; campo `👥 Clientes` segue bloqueado). Uma
  demanda (UMD-317) lida manualmente via navegador para validar o método — funcionou, mas
  `get_page_text`/`read_page` não extraem o conteúdo em bloco do Notion (só leitura visual por
  screenshot), tornando 75 páginas uma a uma inviável em ritmo razoável. Pausa combinada com o
  Vinicius. Resolução real: export da base "Demandas de Clientes" em **HTML** (não CSV) via
  Notion — pasta `Demandas Totais - Lofty/`, 85 arquivos `.html` (um por demanda, narrativa
  completa) + subpastas de anexo (imagem/áudio/vídeo) quando havia mídia. Validado
  byte a byte contra as 2 demandas já confirmadas manualmente (UMD-209, UMD-307) — bateu
  exato, incluindo formatação e anexos (as imagens que antes eram só "IMAGEM" no texto agora
  são arquivos reais). Script escrito para extrair as 75 narrativas restantes (remove CSS/JS,
  preserva parágrafos, marca imagem como `[IMG]`, corrige acentuação) e mesclar no staging —
  as 85 demandas de Lofty Style estão com narrativa completa. Bônus: o campo `👥 Clientes`
  (bloqueado no navegador) vem preenchido no HTML, porque quem exportou tinha acesso.
  Descoberta importante: exports em CSV nunca trazem corpo de página (Notion só exporta
  propriedades da base); export em HTML por página é a via correta para narrativa em lote.
  Próximo passo: aplicar a mesma técnica de export HTML para a base de RFI (pendente o
  Vinicius gerar esse export) e então formalizar demandas e RFIs de Lofty Style no padrão.
- **08 jul 2026** — Sessão 15: Vinicius exportou a base de RFI em HTML (`RFIs Gerais -
  Lofty/`) — mesma técnica das demandas. No processo, achado um bug no script de extração:
  quando a página tem uma tabela dentro do corpo (não só a de propriedades),
  `LastIndexOf('</table>')` pega a tabela errada e corta a narrativa — foi exatamente o que
  aconteceu na primeira tentativa com a RFI 79 (multi-cliente), que voltou com texto vazio.
  Corrigido usando `</table></header>` como âncora (marca o fim da seção de propriedades,
  única no documento), com fallback para `</header><div class="page-body">` em páginas sem
  tabela de propriedades (ex.: a subpágina "Análise Tech" da RFI 104, que não é um registro
  de banco). As 15 RFIs de Lofty foram extraídas com a versão corrigida e batem — inclusive
  confirmando em dados reais a seção "De Acordo" que já tínhamos modelado a partir da
  descrição do Vinicius. A pasta `Demandas Totais - Lofty/` tinha sido removida pelo Vinicius
  (intencional, trabalho de demandas já concluído) antes de eu poder reconferir as 85
  demandas contra esse mesmo bug — só `UMD-321` ficou com narrativa vazia sem confirmação se é
  legítimo ou cortado; risco baixo, registrado como observação aberta em
  `_staging-lofty-demandas.md`, não bloqueia nada. Lofty Style agora tem 85 demandas + 15 RFIs
  completas em staging, prontas para a formalização no padrão
  (`protocolo-gestao-demanda.md`/`protocolo-gestao-rfi.md`).
- **08 jul 2026** — Sessão 16: formalização de Lofty Style — 85 demandas + 15 RFIs geradas
  como arquivos individuais (`D-AAAA-NNN.md` / `RFI-AAAA-NNN.md`), `AAAA` sendo o ano real de
  abertura (não o ano da formalização), sequencial dentro do ano. 100% das 100 geradas com a
  estrutura de headings idêntica ao template (validado por diff automatizado, 0 divergências).
  Todo campo sem dado ficou `[a preencher]`, nunca vazio silenciosamente. Decisões de tradução
  Notion→padrão documentadas em `protocolo-gestao-demanda.md`: (1) enum `Tipo` (CX Hub)
  expandido de 6 para 10 valores — dados reais mostraram que `Integração`, `Produto`,
  `Relatório` e `Suporte` são categorias frequentes que o enum original não cobria; decisão
  foi expandir o enum em vez de distorcer dado real; (2) tabela de tradução Status+Etapa
  (Notion, 2 níveis) → Status (CX Hub, 1 nível), com `Standby - Produto` também gerando
  `Motivo de bloqueio: Aguardando Decisão`; (3) tabela de tradução `Área Responsável` (Notion)
  → `Área (CX Hub)` + `Quadro` (só dentro da taxonomia operacional — ver correção na Sessão 17
  abaixo). Campo novo `ID legado (Notion/CX Hub)` adicionado aos dois templates (demanda e
  RFI) para rastreabilidade de migração — decisão que ficara em aberto desde a Sessão 8.
  Corrigida a UMD-209 no staging (único registro com título e narrativa misturados no mesmo
  campo, de antes da convenção se firmar). Dois bugs de script encontrados e corrigidos
  durante a geração (escaping duplo de parênteses no campo `Demanda relacionada`; barra
  invertida solta em `Taxa aplicada (R$/h)`) — sempre com validação estrutural completa (diff
  de headings) depois de cada correção. Staging files mantidos (não são o padrão final, mas
  guardam o histórico de decisões e ficam claramente marcados pelo prefixo `_staging-`).
  Lofty Style está formalizada — 85 demandas + 15 RFIs.
- **08 jul 2026** — Sessão 17: correção crítica apontada pelo Vinicius — a tabela de tradução
  criada na Sessão 16 usava `Área Responsável` (Notion/CX Hub) para derivar
  `Destino (organizacional)`, violando a própria regra já travada no protocolo desde a Sessão
  9 ("Área (CX Hub) não tem relação com a Área organizacional da hierarquia BrainHub"). Não
  foi releitura incompleta pontual — foi decidir um mapeamento sem reconferir a regra travada
  primeiro. Corrigido: `protocolo-gestao-demanda.md` não deriva mais `Destino
  (organizacional)` de nenhum campo CX Hub — fica `[a preencher]` até alguém com conhecimento
  institucional real decidir. Os 85 arquivos de demanda já formalizados foram corrigidos (70
  tinham o valor indevido `Casa › X`, todos voltaram para `[a preencher]`) — revalidado por
  diff de headings, 0 divergências. **Nova regra travada em `CLAUDE.md`:** antes de formalizar
  qualquer dado legado, reler `CONTEXT.md` → `CLAUDE.md` → o(s) protocolo(s) da entidade por
  inteiro, nesta ordem, antes de decidir qualquer mapeamento de campo — nunca decidir a partir
  de memória de conversa, mesmo que a regra pareça recente.
- **09 jul 2026** — Sessão 18: varredura do Google Drive (pasta hub institucional, Notion
  deixado para depois). Achados principais: organograma real da Casa (27 pessoas, cadeiras,
  Design Org & Metas 2026 — confirma termos já em `institucional.md` da Casa: HIC, Cadeira,
  Botão FUDEU, ONEPAGER); CRM "Mapa de Clientes" com registro completo de Lofty Style (CNPJ,
  módulos, Key Account); base "Reuniões Compartilhadas com Clientes" com 58 registros reais de
  Lofty (timeline completa do Kick off até fev/2026, revelando uma transição de time de
  atendimento não documentada em nenhum outro lugar); confirmação de que Lofty nunca teve
  registro na base de Feedback Interno (gap real). Descoberta de que existe uma segunda
  taxonomia de área/diretoria (a do organograma) diferente das 8 Áreas internas já travadas em
  `CONTEXT.md` — registrada como divergência em aberto, não fundida.
  Questionado pelo Vinicius se dava para pausar a varredura e já padronizar — decisão: sim.
  Executado: (1) `institucional.md`/`jornada.md`/`pessoas.md` de Lofty Style enriquecidos com
  dado real, discrepâncias entre fontes registradas sem resolver por conta própria; (2) novo
  tipo de MD criado — ficha de Pessoa (`_template_pessoa.md` + `protocolo-gestao-pessoas.md`),
  operacionalizando a regra "Pessoa vive só em Casa › Pessoas" já travada mas nunca
  implementada como arquivo; campos documentáveis (cadeira, área, clientes atendidos)
  separados de campos de personificação (personalidade — só via formulário, nunca inferido);
  nota explícita de que "Cadeira" do organograma não é a mesma coisa que "Área" do BrainHub
  (mesmo padrão de cuidado da Sessão 17, aplicado preventivamente aqui); (3) 4 fichas reais
  geradas para as pessoas com dado mais sólido ligadas a Lofty Style. `CONTEXT.md` atualizado
  com nova seção "Pessoas (ficha individual)". Estrutura de tudo validada por diff, 0
  divergências. Varredura registrada como pausada (não abandonada) em
  `_varredura-drive-notas.md`, com lista clara do que falta para retomar.
- **09 jul 2026** — Sessão 19: computador do Vinicius desligou no meio da execução da Sessão
  18 (replicação para os outros 3 clientes-piloto, pedida antes do desligamento). Retomado
  conferindo o log e o estado real dos arquivos em disco antes de continuar — tudo que já
  tinha sido escrito (4 fichas de Pessoa) estava íntegro. Concluído: (1) CRM "Mapa de
  Clientes" e base "Reuniões Compartilhadas com Clientes" filtrados para Cambos, Luiza
  Barcelos e Moda Objetiva (reaproveitando os CSVs já baixados na Sessão 18 — sem nova
  varredura no Drive); (2) confirmado que os 4 clientes-piloto são atendidos pelo mesmo time
  (Laura Delgado Cardoso + Andrea Goulart Holmer dos Santos como Key Account em todos; Marina
  Gonçalves Santoro e Vanessa Rinaldi Ornelas Engman como Consultoras em subconjuntos
  diferentes) — nenhuma ficha de Pessoa nova precisou ser criada, só atualizadas as 4
  existentes com "Clientes atuais atendidos" reais; (3) achado um nome completo mais preciso
  para Marina Santoro (Marina Gonçalves Santoro, via CRM de Luiza Barcelos) — ficha renomeada
  de `marina-santoro.md` para `marina-goncalves-santoro.md`; (4) `institucional.md`/
  `jornada.md`/`pessoas.md` de Cambos, Luiza Barcelos e Moda Objetiva enriquecidos com o mesmo
  padrão usado em Lofty Style — discrepâncias entre fontes registradas sem resolver; (5) achado
  um gap de classificação: **Taís Moser**, presente em quase todas as reuniões de onboarding
  de Luiza Barcelos em 2024, não pôde ser classificada como uMode ou cliente — nenhuma ficha
  criada até confirmar, para não arriscar tratar pessoa de cliente como se fosse da Casa (ou
  vice-versa); (6) auditoria estrutural pós-enriquecimento achou e corrigiu divergências
  pré-existentes de padrão (não introduzidas nesta sessão) em `jornada.md` e `pessoas.md` dos
  4 clientes — seções inteiras faltando, um heading fora de ordem, um heading renomeado; (7)
  também corrigida uma inconsistência que eu mesmo tinha introduzido na Sessão 18 (dei ao CRM
  da Lofty uma subseção própria em `institucional.md`, mas nos outros dobrei o mesmo tipo de
  dado dentro de "Contexto crítico" — uniformizado para o segundo padrão, mais leve). Todas as
  12 combinações (4 clientes × institucional/jornada/pessoas) revalidadas por diff — 0
  divergências, exceto uma pré-existente e sinalizada em Luiza Barcelos (`### ERP` / `###
  Notion` extras em `institucional.md`, decisão pendente do Vinicius). 4 fichas de Pessoa
  revalidadas por diff também, 0 divergências.
- **10 jul 2026** — Sessão 20: criado documento central de pendências
  (`_pendencias-gerais.md`), consolidando 7 dúvidas antes espalhadas em notas/observações de
  cliente. Retomada a varredura do Drive com foco pedido pelo Vinicius: ferramentas internas ×
  Áreas. Lidos na íntegra os dois HTMLs de `Sistema-Operacional/` (28 mai 2026) — narrativa
  institucional mais recente e completa encontrada até agora: tese do pivot ("não somos mais
  empresa de tecnologia, viramos empresa de educação"), 4 causas do teto estrutural do modelo
  antigo, dados reais de dogfooding (74→28 pessoas em 6 anos mantendo capacidade, 22 SaaS
  substituídos por 2, uFlow refeito do zero em um fim de semana), e o "Sistema Operacional
  uMode" descrito como 5 componentes integrados (CadastrAI-Conhecimento, Hub de Agentes, Sync
  Engine, Indicadores, SMART CODE), cada um com status real, operando sob "duas lentes"
  (interna/dogfooding e cliente/produto vendável — mesmo padrão arquitetural). Achado crítico:
  essa lista de 5 não batia com o Portfólio de ferramentas internas já travado em `CONTEXT.md`
  (CadastrAI, Taxonomia, CX Hub, ONB HUB, IntHub, Gest Hub, Sales Hub) — reportado ao Vinicius
  antes de decidir sozinho, por ser mudança estrutural. Decisão do Vinicius: o deck é o modelo
  atual. Aplicado: `CONTEXT.md` → Portfólio Internos reescrito como os 5 componentes, com
  tabela de reconciliação explícita para os nomes antigos (relação inferida, não confirmada
  pela fonte, marcada como tal; onde não há correspondência, `[a preencher]` — CX Hub mantido
  como ferramenta real e distinta, não fundida com "Hub de Agentes"). `institucional.md` da
  Casa ganhou nova seção "Contexto crítico" com a narrativa completa do pivot e os dados de
  dogfooding. Continuando a varredura por ferramentas internas específicas (busca por "ONB
  HUB", "Sales Hub", "IntHub" no Drive), achado um segundo documento, mais recente e mais
  diretamente sobre o próprio BrainHub: `brainhub_mapa.html` ("BrainHub — Mapa-mãe · uMode",
  10/06/2026, também do João) e `arquitetura_umode_4.extracted.txt` ("Arquitetura uMode —
  Especificação por Módulo", 24/04/2026). A tabela de Plataformas do Mapa-mãe confirmou que a
  lista ORIGINAL do Portfólio interno (antes de eu tê-la substituído pelos 5 componentes) era
  a correta — reportado o conflito ao Vinicius de novo antes de prosseguir. Decisão: reverter
  `CONTEXT.md` para a lista original (agora com dupla confirmação de fonte: Mapa-mãe +
  documento de arquitetura técnica + `launch.json` do CEO mostrando repositório de código real
  para CX Hub/ONB HUB/IntHub/Gest Hub), mantendo os "5 componentes"/Sistema Operacional como
  nível de arquitetura documentado à parte, nunca fundido com o Portfólio de produtos. Achado
  também: a regra de arquitetura do produto real ("toda marca herda a mesma estrutura, não
  existe campo custom") valida diretamente a mesma filosofia de padronização já seguida neste
  projeto. O Mapa-mãe trouxe ainda uma 3ª lista de 8 Áreas internas (com "Jurídico", inédito
  nas outras duas) — por decisão explícita do Vinicius, documentos externos do Drive são fonte
  de informação, nunca fonte de estrutura: a estruturação de referência é sempre o
  repositório/padrão definido aqui; as 8 Áreas internas já travadas em `CONTEXT.md`
  permanecem inalteradas, só registrada a pendência de reconciliação futura. Confirmado também
  que nenhum dos 5 componentes/produtos internos é exclusivo de uma Área interna — são
  transversais — o que muda a forma da pergunta original sobre "ferramenta × área" (não é uma
  tabela simples 1:1). Pendências resolvidas removidas/atualizadas em `_pendencias-gerais.md`.
  Varredura segue aberta: próximo destino é `Histórico (2025)` do design org e as 58 atas de
  Lofty.
- **10 jul 2026** — Sessão 21: computador do Vinicius desligou de novo no meio da varredura.
  Retomado conferindo o estado real em disco antes de continuar (nenhum arquivo de demanda/RFI
  havia sido escrito ainda para os 3 clientes restantes — nada perdido). `Histórico (2025)` lido
  (confirmado: evolução do mesmo organograma, não taxonomia nova); as 58 atas de Lofty
  amostradas (5 lidas na íntegra) e encerradas por decisão do Vinicius — conteúdo é Q&A técnico
  de mapeamento de campo ERP↔uFlow, já coberto pelos marcos de `jornada.md`, sem valor
  institucional adicional que justifique ler as 53 restantes.
  Pedido do Vinicius: replicar o piloto de demandas/RFI (já validado com Lofty) para Cambos,
  Luiza Barcelos e Moda Objetiva, garantindo o mesmo padrão de `_template_*`. Achado no
  processo: pastas `Demandas Totais CSV e Markdown/` e `RFIs Totais CSV e Markdown/` já tinham
  um export "Totais" (todos os clientes da uMode, não só Lofty) com narrativa já em markdown —
  mais rápido que a extração HTML usada em Lofty. Reledos os protocolos por inteiro antes de
  mapear qualquer campo (regra travada). Escopo real: Cambos 47 demandas + 3 RFIs, Luiza
  Barcelos 70 demandas + 4 RFIs, Moda Objetiva 34 demandas + 0 RFIs (151 demandas + 7 RFIs no
  total). `protocolo-gestao-demanda.md` estendido com 9 combos novos de Status+Etapa e a
  variante de Tipo "Melhoria / Desenvolvimento", achados nos dados reais desses 3 clientes —
  registrados no protocolo antes de aplicar, mesma disciplina já usada para Lofty.
  Construídos `scripts/gen-demandas.ps1` e `scripts/gen-rfis.ps1` (parametrizados por cliente,
  reutilizáveis para o cliente 5 e para re-exports futuros do Notion). Dois bugs reais de
  PowerShell encontrados e corrigidos durante a geração: (1) pipeline `-split | ForEach-Object |
  Where-Object` que retorna 1 único item vira **scalar string**, não array — `$lines[0]` nesse
  caso indexava por caractere, não por linha, cortando títulos de demanda para 1 letra só
  (corrigido com `@(...)` forçando array); (2) narrativa de RFI extraída do Notion trazia
  headings markdown reais (`# De Acordo`) que colidiam estruturalmente com os headings do nosso
  próprio template — convertidos para negrito antes de gravar. Todos os 151 demandas + 7 RFIs
  gerados e validados por diff de headings contra o template — 0 divergências.
  Por pedido explícito do Vinicius, rodada uma **auditoria final de padronização em todos os
  níveis**: `institucional.md`/`jornada.md`/`pessoas.md` dos 4 clientes, `contexto-area.md` das
  8 Áreas da Casa, as 4 fichas de Pessoa, e todas as demandas/RFIs (Lofty + os 3 novos) — todos
  por diff de headings. Dois achados novos, registrados em `_pendencias-gerais.md` (itens 8 e
  9): o `contexto-area.md` das 8 Áreas da Casa usa consistentemente um variante em 1ª pessoa
  (sem "Produto conectado", só 1 campo de responsável em vez de 2) nunca formalizado como
  template próprio; e **nenhum dos 4 clientes-piloto tem `contexto-area.md` preenchido em
  nenhuma das 14 áreas** — pastas existem, conteúdo real nunca foi levantado, gap pré-existente
  não introduzido nesta sessão, só agora identificado porque foi a primeira vez que essa camada
  foi auditada especificamente. Nada inventado para fechar o gap — fica como próximo passo.
- **10 jul 2026** — Sessão 22: migração completa pro Git resolvida a pedido do Vinicius, que
  precisa levar o projeto pra um novo workspace do Claude Code em breve e queria garantir que
  nada do trabalho de 21 sessões ficasse perdido. Achado crítico: só existia 1 commit trivial
  no repositório — tudo (CONTEXT.md, CLAUDE.md, STATE.md, `uMode/` inteiro, protocolos,
  templates, conteúdo real dos 4 clientes) estava como alteração não commitada, sem nenhum
  backup real além da máquina local. Resolvido: commit + push de tudo (1267 arquivos,
  `github.com/HyTrackWater/brainhub-umode`, branch `main`), incluindo as pastas de dados
  brutos usadas como fonte (decisão explícita do Vinicius: "tudo que estamos documentando de
  forma padronizada será o cérebro... não faz sentido" deixar algo de fora). No caminho, achado
  e resolvido um limite real do Windows (260 caracteres por caminho) que travava o `git add` em
  ~146 arquivos de sub-exports do Notion muito aninhados — corrigido encurtando nomes de pasta
  (sem tocar em `git config`, proibido pelas minhas regras), não excluindo nada.
  Na sequência, começou o desenho de telas da plataforma (agentes que aplicam mudança direto na
  tela, tipo Lovable interno) por perfil de usuário/cadeira. Dois erros reais cometidos e
  corrigidos no processo: (1) montei um mockup usando dado inventado a partir de notas próprias
  sobre o Mapa-mãe, sem checar se já existia um artefato real — existia:
  `docs/brainhub_plataforma.html`, um protótipo navegável de 764 linhas já construído antes
  desta sessão, com 9 telas (Início, uGentes, Builder, Cérebro, Conversa, Aprovações, Aferição,
  Plataformas, Verticais); (2) ao descobrir esse arquivo, tratei ele (e o organograma
  V2.2/Mapa-mãe do Drive) como fonte válida pra desenhar telas novas — o Vinicius corrigiu:
  nada de artefato antigo/externo vale como fonte de estrutura agora, só o que já está
  formalizado na nossa própria hierarquia (`CONTEXT.md`, os MDs reais). Reiniciado do zero.
  Alinhamento de produto resultante (sem nenhuma tela construída ainda): (a) visibilidade por
  perfil é função de campos que já existem na ficha de Pessoa (`Cadeira`, `Área organizacional`,
  `Clientes atuais atendidos`), não uma tabela de permissão nova; (b) o fluxo de aprovação que
  o Vinicius descreveu (agente de área faz "conferência", abre demanda, alguém aprova, contexto
  é atualizado) já existe formalizado por inteiro em `protocolo-gestao-demanda.md` — só nunca
  virou tela; (c) **decisão de modelagem travada**: toda demanda nasce "interna" (BrainHub,
  manutenção do ecossistema/contexto) e pode, dependendo do que for, ganhar um card real no CX
  Hub depois — não são dois tipos de documento, é a mesma `Demanda`, com a seção "Taxonomia CX
  Hub" inteira condicional a um novo campo `Vinculada ao CX Hub?` (Não/Sim + ID). As 236
  demandas já formalizadas (histórico migrado, todas nasceram como card real) foram
  retrofitadas com esse campo (`Sim — ID: [mesmo valor de ID legado]`), revalidadas por diff —
  0 divergências. Também decidido: quando um agente de área abre a demanda sozinho (sem
  triagem humana prévia), o campo `Criador` aceita nome de agente, não só pessoa física —
  registrado no protocolo.
  Na sequência, alinhamento de produto pra desenho de telas (papel de responsável técnico,
  pensando em produtos/áreas/agentes): proposta e travamento de **6 abas de navegação**
  (Instituições — com Áreas navegável só por dentro dela, não é aba de topo —, Pessoas,
  Produtos, Demandas, RFIs, Agentes), cada uma mapeada 1:1 a uma entidade já formalizada na
  hierarquia, com relação clara de o que lista/abre/navega/cria. Decisão explícita: "Agentes"
  ainda não é entidade formal (sem template, sem protocolo, sem onde vive) — desenhamos a aba
  com dado de exemplo agora, formalizamos a entidade depois, quando o uso real deixar claro o
  formato — mesma disciplina já usada pra Demanda/RFI/Pessoa, só que na ordem inversa
  (protótipo primeiro, modelo formal depois, por decisão explícita do Vinicius desta vez).
  Criado `BRAINWAVE.md` (raiz do repositório, fora da hierarquia `uMode/`) — brief de
  instrução pro agente interno de frontend "BrainWave" construir essas telas, com a estrutura
  das 6 abas, o mecanismo de aprovação (já formalizado, só precisa de interface), a regra de
  visibilidade por Cadeira/Área/Clientes atendidos, e a lista explícita do que ainda não existe
  (Agente formal, `contexto-area.md` real, automação Demanda→CX Hub) pra não ser inventado.
  Criado também `START.md` (raiz) — ponto de entrada único pra qualquer sessão nova (BrainWave
  ou não): define a ordem exata de leitura (`CLAUDE.md` → `CONTEXT.md` → `STATE.md` →
  `BRAINWAVE.md`), proíbe qualquer alteração na primeira resposta, e trava um contrato de saída
  de 4 pontos (o que é o projeto, qual o papel da sessão, última atividade registrada, próximo
  passo) — pedido explícito do Vinicius pra nunca precisar reexplicar o projeto do zero. A
  primeira mensagem de qualquer sessão nova passa a ser só "Leia START.md".
  Antes de escrever o prompt de execução real pro BrainWave, 3 parâmetros do setup dele foram
  confirmados (perguntados, não presumidos): (1) BrainWave constrói num repositório separado
  de `brainhub-umode`, hoje sem acesso de leitura a ele — nesta primeira tarefa não há dado
  real disponível; (2) o stack técnico do BrainWave não foi informado — o próprio agente vai
  declarar isso sozinho, mesmo princípio do `START.md`; (3) escopo do primeiro entregável
  definido como só a casca de navegação, sem dado, sem tela de detalhe, sem criação/edição.
  Criado `BRAINWAVE_TAREFA_ESQUELETO.md` (raiz) — a tarefa concreta de execução: construir as 6
  abas com rota funcionando, cada uma com placeholder textual (nome + descrição de uma linha,
  copiado de `BRAINWAVE.md`), Áreas sem virar 7ª aba, nenhum dado real ou inventado, e um
  contrato de saída pedindo que o BrainWave liste decisões próprias tomadas por falta de
  definição, sem prosseguir pra próxima tarefa sem confirmação.
  **Correção do Vinicius, importante pra não repetir**: BrainWave não é uma sessão de Claude
  Code que lê o repositório — é ferramenta tipo Lovable, sem acesso a arquivo nenhum daqui.
  Ele só aplica no frontend o que é digitado direto nele; o Vinicius usa o resultado pra abrir
  PR pra equipe tech. O fluxo "Leia START.md" é exclusivo de sessões de Claude Code (ex.: a
  migração de workspace discutida antes) — nunca do BrainWave. Corrigidos os dois arquivos:
  `BRAINWAVE.md` virou referência interna nossa pra escrever prompt (não é lido pelo
  BrainWave); `BRAINWAVE_TAREFA_ESQUELETO.md` reescrito como texto 100% autocontido, pronto
  pra colar direto na ferramenta, sem nenhuma referência a "leia X".
  Criada a pasta `brainwave/` (raiz do repositório) pra guardar o histórico de toda instrução
  de frontend já dada ao BrainWave — pedido explícito do Vinicius. Estrutura: `CONTEXTO.md`
  (a antiga `BRAINWAVE.md`, movida pra dentro, sempre atual, nunca numerada) + arquivos de
  tarefa numerados sequencialmente (`01-esqueleto.md` é o primeiro, movido da raiz). Cada
  arquivo de tarefa ganhou uma seção `## Resultado`, hoje `[a preencher]` com status "Enviado
  — aguardando resultado" — **o Vinicius é a interface entre o BrainWave e este repositório**:
  ele cola o prompt na ferramenta e traz o resultado de volta pra registrar aqui; nunca se
  inventa o que o BrainWave fez. `START.md` atualizado pra apontar pro novo caminho
  (`brainwave/CONTEXTO.md` em vez de `BRAINWAVE.md` na raiz).
  **Combinado novo com o Vinicius sobre cadência de commit**: não commitar/dar push a cada
  alteração — só manter a documentação sempre atualizada (o que este próprio log faz). Ele
  commita manualmente quando quiser; a documentação corrente é que garante segurança pra
  trocar de sessão, não a frequência dos commits. Registrado como memória de feedback pra não
  esquecer em sessões futuras.
  Desenho da tela **Home** (personalizada por pessoa/cadeira) iniciado. Avaliação do template
  de Pessoa: quase suficiente — único campo realmente faltando era **Foto** (nunca existiu).
  Adicionado `### Foto` em `_template_pessoa.md` (Identificação, logo após Nome preferido/
  antes... na verdade logo no início da seção) + `protocolo-gestao-pessoas.md` atualizado +
  as 4 fichas reais retrofitadas (`[a preencher]`) e revalidadas por diff — 0 divergências.
  Resto do que a Home precisa já existia: Data de entrada (tempo na uMode é calculado, não
  campo novo), Cadeira, Missão/Responsabilidades (serve de resumo documentável quando
  Personificação ainda não foi respondida — é o caso das 4 fichas hoje), Clientes atuais
  atendidos. O "Inbox" da Home não precisa de campo novo — é um recorte filtrado de `Demanda`
  (Criador/Responsável = a pessoa), mesma lógica já desenhada pra aba Demandas.
  **Dado real atualizado**: Andrea Goulart Holmer dos Santos não faz mais parte do time da
  uMode (informado pelo Vinicius, 13 jul 2026 — data exata de saída não informada). Isso
  expôs um campo que faltava na ficha de Pessoa: não existia jeito de marcar alguém como
  inativo. Adicionados `Status na uMode` (Ativo/Inativo) e `Data de saída da uMode` ao
  template + protocolo + nas 4 fichas reais (3 Ativo, Andrea Inativo). Ficha da Andrea:
  `Clientes atuais atendidos` movido pra `Clientes atendidos historicamente` (ela não atende
  mais de verdade, mesmo que o registro documental do que fez fique). Ficha da Laura:
  removida a menção "sempre em par com Andrea" de Responsabilidades/Interfaces — `Interfaces`
  volta a `[a preencher]` com nota do que mudou, sem inventar um par novo que não foi
  confirmado. **Pendência aberta, não resolvida ainda**: Andrea também aparece em 11 outros
  arquivos (institucional/jornada/pessoas.md dos 4 clientes-piloto) como Key Account ativa —
  o Vinicius pediu só os dados da Laura nesta rodada; esses 11 arquivos ficam desatualizados
  até confirmação explícita de que devem ser atualizados também.
  **Nova 3ª classe de campo criada na ficha de Pessoa: Competências** (Experiência
  profissional anterior, Skills/habilidades técnicas, Cursos e certificações, Ferramentas e
  plataformas que domina) — pedido do Vinicius, com um propósito de produto explícito
  registrado no protocolo: virar fonte de busca de "quem sabe sobre X" quando as fichas
  estiverem interligadas com Demanda/Produto/Área (nenhuma busca construída ainda, só a
  estrutura de dado). Mesma disciplina de nunca inferir — só com fonte real citada (CV,
  LinkedIn, certificado) ou resposta via formulário. Adicionada ao template, ao protocolo
  (que passou de "duas classes de campo" pra "três"), e às 4 fichas reais — todas `[a
  preencher]` hoje, nenhum dado real disponível ainda. Revalidado por diff — 0 divergências.
  **Pendência dos 11 arquivos resolvida** (a pedido do Vinicius: "pode atualizar"). Atualizados
  8 dos 11 (`institucional.md` × 4 — seção "Responsável de atendimento" + Governança — e
  `pessoas.md` × 4): Andrea removida da lista de time **atual**, com nota explícita de que saiu
  (13 jul 2026) e que o time de atendimento atual não está confirmado além da Laura. Os outros
  3 (`jornada.md` de Cambos/Lofty Style/Luiza Barcelos) **não foram tocados de propósito** —
  citam a Andrea dentro de Marcos (tabela append-only de reuniões que realmente aconteceram
  com ela presente) e numa observação de "última reunião registrada" também histórica; alterar
  isso seria reescrever fato passado, o que contraria a mesma regra de Marcos já aplicada a
  Demanda. Revalidado por diff todas as 8 edições — só as divergências já conhecidas (nome do
  cliente no H1, `### ERP`/`### Notion` pendente da Luiza Barcelos), nada novo quebrado.
  **Campo novo na ficha de Pessoa: `Nível HIC`** — pedido do Vinicius, representa a jornada de
  aprendizagem/uso de ferramentas e conhecimento em IA do colaborador (conceito HIC já definido
  em `CONTEXT.md` → Taxonomia). Só o campo foi criado — a escala/critério de triagem **ainda
  não existe**, decisão explícita de não inventar uma provisória. Adicionado ao template
  (Identificação, logo após Cadeira), ao protocolo, e às 4 fichas reais (todas `[a preencher]`).
  Revalidado por diff — 0 divergências.
  Criado `brainwave/02-home.md` — segunda tarefa de execução pro BrainWave: construir o
  conteúdo da aba Home (personalizada por pessoa logada). Campos especificados: Foto (vazia),
  Nome preferido, Cadeira, Nível HIC (omitido quando vazio, não quebra layout), Área
  organizacional, **Data de entrada na uMode mostrada explicitamente** (pedido do Vinicius —
  antes só o "Tempo na uMode" calculado estava no mockup, faltava a data crua) + Tempo na uMode
  calculado, Resumo (autodescrição se existir, senão papel/responsabilidades, com indicação de
  qual fonte foi usada), Clientes atuais atendidos, e Inbox (demandas em aberto onde é
  Criador/Responsável). Autocontido, dado só de exemplo marcado como tal (BrainWave segue sem
  acesso a este repositório), com seção `## Resultado` aguardando o Vinicius rodar e reportar.
  Sessão perto de trocar de workspace — toda a documentação relevante está atualizada nesta
  entrada; nada pendente de escrita no momento desta nota.
- **13 jul 2026** — Sessão 23: (1) Removidas do repositório as 3 pastas de dado bruto usadas só
  como fonte pra gerar demandas/RFIs (`Demandas Totais CSV e Markdown/`, `RFIs Gerais - Lofty/`,
  `RFIs Totais CSV e Markdown/` — 947 arquivos, CSV/HTML/planilhas/PDFs do Notion/Drive), a
  pedido do Vinicius: o repositório é essencialmente só `.md`, nada referencia essas pastas.
  (2) `brainwave/03-uMode-e-clientes.md` (redigido e validado antes, nunca commitado) e
  `brainwave/04-seletor-cliente-ativo.md` — o Vinicius navegou no resultado da tarefa 03 e notou
  que o "cliente ativo" da aba Clientes não ficava visível/trocável fora da sub-aba Instituições;
  tarefa 04 corrige com seletor fixo nas 4 sub-abas + estado vazio + filtro opcional por Área em
  Pessoas. `brainwave/CONTEXTO.md` atualizado pra refletir as duas. (3) **Correção de
  nomenclatura Demanda vs. CX Hub**, a pedido do Vinicius, depois de reler
  `protocolo-gestao-demanda.md` por inteiro (regra obrigatória): a separação conceitual já
  estava travada (toda demanda nasce interna, CX Hub é destino opcional), mas faltava um campo
  de status pra demandas que nunca vinculam ao CX Hub e não mudam nenhum MD (ex.: "avisar que
  fulano saiu da empresa", "mandar e-mail de detalhamento de permissionamento") — hoje nenhum
  campo dizia se essas foram concluídas. Adicionado `Status (interno)` (`Aberta / Em andamento /
  Concluída / Cancelada`) em `## Identificação`, terceiro eixo de status, separado do `Status`
  operacional do CX Hub e do `Ciclo de vida institucional` (aprovação de contexto). Refinamento
  do próprio Vinicius: quando `Vinculada ao CX Hub? = Sim`, `Status (interno) = Concluída`
  significa que a demanda foi criada e vinculada ao CX Hub — não que o trabalho foi executado (a
  execução segue no `Status` do CX Hub, campo separado). Aplicado nos 2 templates (Casa e
  cliente) e retrofitado nas 236 demandas já formalizadas via
  `scripts/retrofit-status-interno.ps1` — todas ganharam `Concluída` (as 236 já eram `Vinculada
  ao CX Hub? = Sim`). **Bug de encoding recorrente**: primeira rodada do script gerou mojibake
  (`ConcluÃ­da`) porque o `.ps1` foi salvo sem BOM UTF-8 — mesmo problema já visto em sessões
  anteriores com literais acentuados em PowerShell 5.1. Revertidos os 236 arquivos via
  `git checkout --`, script resalvo com BOM (`Set-Content -Encoding UTF8`), rerodado com
  sucesso; também corrigido um typo próprio ("ja"/"execucao" sem acento) nos 236 arquivos e no
  script. Revalidado por diff de headings — 0 divergências; confirmado que os 236 arquivos têm
  o campo novo.
