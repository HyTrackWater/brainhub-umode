# STATE.md — Estado do projeto

> Estrutura fixa. Não repetir objetivo aqui — ver `CONTEXT.md`.
> Este arquivo só registra **avanço**: o que foi feito, o que está em andamento, o que vem a
> seguir e o que está no backlog (priorizado conforme a fila anda).

## Sprint atual
**Sprint 02 — Estrutura de pastas no Drive + simulação com clientes-piloto**

### Em andamento
- [x] **REPLICAÇÃO TOTAL — concluída em 03 ago 2026 (o "rolo compressor"), em 2 rodadas.** Todos os
      **46 clientes reais** têm casa no padrão: 42 criadas nesta sessão + os 4 pilotos. Números
      finais, todos validados por diff de headings (0 divergências, exceto a de Luiza Barcelos já
      conhecida e sinalizada): 138 arquivos de `institucional.md`/`jornada.md`/`pessoas.md`
      (46 × 3); **993 demandas** de cliente (236 dos pilotos + 757 de 16 clientes); **85 RFIs**
      (22 + 63 de 12 clientes), **84 delas com narrativa real de página**; **4 demandas da própria
      Casa** (`Natureza: interna`, primeiras a existir em `uMode/00_Institucional/_demandas/`);
      13 fichas de Pessoa (4 + 9 novas). Repositório passou de ~330 para **1.291 arquivos `.md`**.
      Lista definitiva e filtrada em `uMode/00_Institucional/_contexto/_lista-clientes-reais.md`.
- [x] **2ª rodada — fonte de jul 2026 recuperada do histórico do Git.** A 1ª rodada usou snapshots
      de mar 2026 do Drive e eu registrei como pendência "falta um re-export mais recente". O
      Vinicius questionou a premissa (a fonte que gerou os pilotos existe) e estava certo: os
      exports de jul 2026 foram **commitados na Sessão 22 e removidos na Sessão 23** (commit
      `8c6705b`) — recuperados com `git archive 8c6705b^`. Todas as demandas e RFIs não-piloto
      foram regeneradas dessa fonte (+108 demandas, +23 RFIs), a narrativa de RFI entrou de
      verdade, e o vínculo `Demanda ⟷ RFI` passou a existir pela primeira vez.
- [ ] Testar template de cliente com ao menos 5 clientes reais (fase cadastral)
      — ⚠ **item superado pela replicação total acima**: não são mais 5 clientes, são 46
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

## 🔴 PRIORIDADE ZERO — 04 ago 2026: primeira ENTREGA do BrainHub

> Isto passa na frente de tudo abaixo, inclusive do "rolo compressor". Declaração literal do
> Vinicius em 04 ago 2026: "temos uma demanda já para entrega de BrainHub, **antes de finalizar
> qualquer outra coisa**, que será construir um agente que vai servir para a operação."

**Demanda formalizada:** [`D-2026-002`](uMode/00_Institucional/_demandas/D-2026-002.md) —
Agente de Suporte Técnico uFlow.

**O que é:** o primeiro agente operacional do BrainHub. Analista técnico de suporte especializado na
**uFlow** (o PLM legado), cujo contexto é **o próprio repositório da plataforma**, com domínio da
estrutura do banco. Diagnostica de que **tipo** é o problema — correção de configuração, questão para
tech, erro de inserção de dado — para a operação saber o que fazer com ele. Desenho central: **não
tem acesso direto ao banco**; quando precisa de dado, pede ao usuário que consulte e traga, e só
então conclui.

**Papel já recebido e formalizado:** `Papel de Suporte.txt` (04 ago 2026), com estrutura obrigatória
de resposta em 6 seções (Entendimento · Investigação · Evidências · Hipóteses · Dados Necessários ·
Próximos Passos) e a regra "é preferível pedir mais dados do que fornecer uma resposta potencialmente
incorreta" — que é, sem ter sido combinado, a mesma regra de ouro de zero alucinação do nosso
`CLAUDE.md`.

**✅ DESBLOQUEADA em 04 ago 2026.** Vinicius entregou os três insumos: o repositório
(`C:\Ambientes Virtuais\uFlow\umode-flow` — Rails real, **12.613 commits**, último em **03/08/2026 por
`Bergson`**), o **`db/schema.rb`** (172 KB, **211 tabelas**) e o `.md` de **aprendizado contínuo**
(1.084 linhas). Os dois primeiros já foram mapeados em
[`uflow-modelo-de-dados.md`](uMode/04_Dados-e-IA/_contexto/uflow-modelo-de-dados.md); o terceiro foi
preservado em [`agente-suporte-uflow.md`](uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow.md).

**⚠ Problema de custódia:** os dois arquivos que o Vinicius forneceu (`Papel de Suporte.txt` e
`TREINAMENTO-AGENTE-SUPORTE-UFLOW.md`) **saíram de `Downloads` depois de lidos**. O conteúdo foi
materializado no repositório, mas **só 818 das 1.084 linhas do treinamento foram lidas** — faltam o fim
do Anexo C, o **Anexo D** e o **Anexo E**, que não existem em nenhuma cópia nossa. **Precisa do arquivo
de novo.**

**Bloqueios residuais, ambos nomeados:** (a) a gem privada **`j3_components`**
(`UmodeApp/j3-components`) não está no repositório e **parte do core `J3::` vive nela**; (b) o
**catálogo de `EntityConfig`** — a lacuna de maior valor que resta — não foi levantado porque a
varredura **morreu no limite de crédito da organização**. É a primeira coisa a retomar.

---

## ⭐ ORDEM DE PRIORIDADE — reconfirmada e ampliada em 03 ago 2026 pelo Vinicius ("rolo compressor")
> Leia isto primeiro. Os itens numerados logo abaixo ("fila da Sprint 02") continuam como
> **referência detalhada** de tudo que já foi feito/descoberto — não foram apagados, só não são
> mais a ordem de execução. A ordem de execução real é esta:

**Instrução literal do Vinicius em 03 ago 2026: "passar o rolo compressor".** 100% da energia vai
para **alimentar de informação a estrutura que já validamos** — clientes, produtos e tudo o mais —
replicando o padrão já aplicado, "de forma que vamos inflando cada vez mais e explorando cada vez
mais tudo que já temos". Não é uma nova frente de modelagem: é escala sobre o padrão existente.

**Sequência travada:**
1. **Esgotar TODAS as fontes já mapeadas**, replicando o padrão para TODOS os clientes reais (não
   só os 4 piloto). É o que está em execução agora.
2. **Só depois** — nova fase: o Vinicius tem **outra fonte rica de informação institucional**
   (produtos, áreas etc.) que vai ser reprocessada para **adequar/corrigir conteúdo que já
   firmamos antes**. Ou seja: o que for gerado agora não é definitivo por decreto — vai passar por
   um ciclo de correção com fonte melhor. Isso reforça (não dispensa) a disciplina de marcar fonte
   e data em tudo que for gerado, para saber depois o que revisar.

**Estado do item 1 no fim da Sessão 25 (03 ago 2026) — o que já foi esgotado e o que sobrou:**

| Fonte / frente | Estado | Volume |
|---|---|---|
| CRM "Mapa de Clientes" → casas de cliente | ✅ esgotada | 46 casas, 138 MDs institucionais |
| Demandas (fonte de julho recuperada do Git) | ✅ esgotada | 997 (993 de cliente + 4 da Casa) |
| RFIs | ✅ esgotada | 85, sendo 84 com narrativa real |
| Fichas de Pessoa (Key Account / Consultor do CRM) | ✅ esgotada | 13 |
| Portfólio de Soluções | ✅ esgotada | 16 `produto.md`, 14 com maturidade decidida |
| Notion — 3 páginas canônicas de produto | ✅ esgotada | Especificação V1, Plano do Hub, Taxonomia + Índice Mestre |
| Narrativa do Notion — demandas **em aberto** | ✅ fila zerada | 208 de 208 processadas |
| Repositórios de integração (9 documentos técnicos) | ✅ esgotada | 11 `integracao.md`, 11/11 conformes |
| Notion — subpáginas da Taxonomia | ⬜ aberta | ~20 subpáginas e ~100 anexos, inclusive `00-visao-geral.md` e `09-de-para-mestre.md` |
| Notion — páginas de projeto por produto | ⬜ aberta | 8 páginas de projeto identificadas no ÍNDICE MESTRE e não lidas |
| `uMode-OS` (pasta local no Mac do João) | 🔒 inalcançável | `MANIFEST.md` + crosswalk repositório↔produto — só o João pode passar |
| Perfis de acesso → `contexto-area.md` | ⬜ aberta | **0 de 644** — o maior vazio medido do cérebro |
| Narrativa das demandas **encerradas** | ⬜ despriorizada | 679 (`Concluído` 552 / `Cancelado` 127) |

**Próximo alvo recomendado: `contexto-area.md`.** É o eixo de indexação que a auditoria mediu como
**vazio** (o eixo cliente já resolve, o de Área não), e a fonte já foi encontrada: os perfis da
planilha de acessos mapeiam quase 1:1 para as 14 áreas canônicas. Enquanto ele não for preenchido,
um agente "Por Área" não tem de onde beber.

**Duas pendências que seguem abertas por decisão explícita do Vinicius (não bloqueiam, não
esquecer):** (a) mudou muita coisa entre 14 jul e 03 ago 2026 que não está registrada neste log —
o Vinicius confirmou que segue acontecendo e que não é para gastar energia nisso agora; (b) a
confidencialidade do conteúdo T1-restrito da Cambos continua sem resposta — nenhum dado comercial
sensível (custo/margem/faturamento) desses arquivos pode ser usado até ela chegar.

**Virou prioridade total: a transição pra construção de fato do BrainHub — isso significa
buscar TODAS as informações de TODOS os clientes reais, não só os 4 piloto.**

1. **[NOVO — prioridade máxima] Replicar pra todos os clientes reais tudo que já validamos nos
   4 piloto.** Pipeline já existe e funciona: `institucional.md`+`jornada.md`+`pessoas.md` (via
   CRM "Mapa de Clientes" + Notion), Demandas (`scripts/gen-demandas.ps1`), RFIs
   (`scripts/gen-rfis.ps1`). **Passo zero — ✅ concluído em 03 ago 2026:** lista definitiva e
   filtrada em `uMode/00_Institucional/_contexto/_lista-clientes-reais.md` — **46 clientes reais**
   (49 linhas do CRM − 3 que não são cliente: a própria uMode, a linha de template do Notion e
   "Fornecedores"), 4 já com casa, 42 a criar. Os 9 nomes que existem só na pasta Drive "Clientes"
   e não no CRM (Alpargatas, Polenectar, Genuo, Grupo Veste, Notre Dame, Arezzo, Posthaus,
   Esposende, Lupo) **não viraram casa** — pendência registrada. Enunciado original do passo zero,
   mantido como referência: construir a lista
   definitiva e **filtrada** de clientes reais — cruzar as ~49 linhas do CRM "Mapa de Clientes"
   com a pasta Drive "Clientes" (achada em 14 jul 2026, `14PwnAIF55IkdWNo90iEH9Ex5TusopsWO` —
   tem CAEDU, Alpargatas, Cambos, 4Takes, Polenectar, Osklen, Genuo, Grupo Veste, Luiza
   Barcelos, Esposende, Reserva, Hering, Arezzo, e mais via paginação). **Cuidado real**: nem
   tudo nessa pasta é cliente uMode moda-PLM — `Kaizen`, `CrossX-JUMP3R`, `MBS-3-Mentorias`,
   `ALINVEST-IFT`, `Marcio Delbin (Tetris)`, `NV-Vinicius` parecem outros negócios/mentorias do
   próprio CEO, não clientes da vertical de moda — não replicar o padrão de cliente uMode neles
   sem confirmar.
2. **[NOVO] Ir atrás de tudo que já sabemos que existe mas nunca foi tocado.** Ex.: as 3 páginas
   Notion linkadas no CRM (nunca abertas), o resto da pasta "Clientes" do Drive (só Cambos foi
   aberta até agora), pastas irmãs achadas na mesma raiz (`1LPFb_DUTzFngwBpjj-zP0ZcmOTviMbM5`):
   `BrainHub/` (dono vinicius.risoleo@gmail.com, nunca aberta), `DUMP THREAD/` (nunca aberta),
   `Mídia/` (nunca aberta).
3. **[Modus operandi, contínuo]** A cada assunto fechado, buscar a próxima parte identificada
   como necessária — sempre nos nossos padrões já travados (protocolo primeiro, nunca inventar
   campo, fonte externa é informação não estrutura), reforçando o processo de contextualização.

**Frentes que ficam pausadas até a replicação total avançar** (não canceladas, só depois):
BrainWave/frontend (item 1 da fila antiga — construir mais tela não ajuda enquanto a maioria
dos clientes reais nem tem `institucional.md`), Sprint 03 formulários/Lovable/agentes (linha
328 abaixo), varredura de nomenclatura legado→novo do Portfólio (item 2 da fila antiga).

**Carregado da sessão anterior, ainda sem resposta — não esquecer:** confidencialidade do
conteúdo real da Cambos (`CONTEXTO_CAMBOS.md`/`_FATOS.md`, autodeclarado "T1 — restrito, contém
custo/margem, NÃO sincroniza Drive/Notion do time"). Perguntei ao Vinicius se precisa de
anonimização ou se simplesmente não entra no repositório — **ainda sem resposta**. Não usar
nenhum dado comercial sensível desses arquivos até isso ser resolvido, mesmo que pareça útil
pra replicação.

## Próximas atividades (fila da Sprint 02 — referência histórica, ver ordem nova acima)
1. **Frente ativa: BrainWave/frontend.** `brainwave/01-esqueleto.md`, `brainwave/02-home.md`,
   `brainwave/03-uMode-e-clientes.md`, `brainwave/04-seletor-cliente-ativo.md`,
   `brainwave/05-solucoes.md`, `brainwave/06-demandas.md`, `brainwave/07-demandas-tabela-e-acoes.md`,
   `brainwave/08-agentes-duvidas.md`, `brainwave/09-agentes-categorias.md` e
   `brainwave/10-agentes-filtros-e-chat.md` enviados. **A tarefa 10 é correção** — o Vinicius já
   rodou algo no BrainWave e a aba Agentes voltou com os agentes "jogados" sem filtro nenhum
   aplicado (mesmo tendo sido pedido na tarefa 09), e sem a interface de chat (histórico +
   campo de texto) que uma versão anterior já tinha construído. A tarefa 10 corrige os dois:
   exige filtro em chip **funcional** por categoria (Geral/Por Área/Por Cliente/Por Solução/
   Personalizado), e exige que a interface de chat reservada volte a aparecer em **todo**
   agente aberto, não só no Dúvidas — mesmo sem IA conectada, só pra dar visibilidade de como
   vai funcionar. **A tarefa
   06 já foi rodada pelo Vinicius no
   BrainWave** (confirmado em 14 jul 2026) — `## Resultado` ainda não reportado formalmente
   aqui. Como 06 já foi executada, as mudanças de tela pedidas depois viraram tarefas novas em
   vez de edição no lugar (mesmo padrão já usado em 03→04): a tarefa 07 altera a aba Demandas
   que o 06 construiu — lista de cartões vira **tabela compacta**, e o detalhe ganha **Conversas**
   (chat informal, separado dos Marcos) e ação **Reatribuir** (troca Responsável/Destino, gera
   Marco automático). A tarefa 08 preenche a aba Agentes com grade de cartões de exemplo e
   **reserva um cartão pro agente de "Dúvidas"** — abre um chat sem IA conectada, só a interface.
   **A tarefa 09 reorganiza Agentes em 4 classes** (pedido do Vinicius, confirmado em 14 jul
   2026): Por Área (lê `contexto-area.md`), Por Cliente (lê `institucional.md`+`jornada.md`+
   `pessoas.md`), Por Solução (lê `produto.md`), Personalizado (skill criada por usuário, com
   cartão "Criar agente" que gera pedido de aprovação — mesmo mecanismo já formalizado em
   `protocolo-gestao-demanda.md`, não um fluxo novo). Dúvidas (task 08) fica fora das 4 classes,
   geral. Cada agente ganha perguntas sugeridas estilo FAQ, coerentes com seu escopo. Nota
   explícita registrada: "oportunidade de upsell" (agente Por Cliente) não é campo que existe —
   seria resposta calculada comparando módulos contratados com o Portfólio completo, não
   inventar esse campo como se já existisse. Consequência registrada em `brainwave/CONTEXTO.md`:
   agentes Por Área/Por Solução vão nascer com pouco conteúdo real até `contexto-area.md` e
   `produto.md` serem preenchidos de verdade — mais um motivo pra priorizar esse preenchimento.
   Isso resolve a arquitetura de comunicação interna discutida na sessão: 3 padrões distintos —
   (1) agente de consulta geral = skill reativa do Hub de Agentes, reservada na aba Agentes; (2)
   comunicação entre colaboradores numa Demanda = campo `Conversas` que já existia no template,
   agora com tela; (3) "transferência" = reatribuição de campos existentes + Marco automático,
   não um sistema novo. Nota completa em `brainwave/CONTEXTO.md` → "Comunicação interna — 3
   padrões". A tarefa 03 reestrutura o menu principal (remove as abas
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
2. **Varredura de nomenclatura legado→novo Portfólio — em andamento (14 jul 2026).** Achados
   registrados em `_varredura-drive-notas.md`. Base "Mapa de Clientes" completa (49 clientes,
   não só 1) revelou `uDash` (Luiza Barcelos) e `uRocket` (Cambos) contratados — **já
   corrigido** nos `institucional.md` reais, cada um com nota de que é ferramenta legada
   descontinuada/em desuso. Vocabulário legado levantado: uFlow, uPlan, uBuy, uPick, uRocket,
   uTrack, uDash, uMetrics, ISPS, Cronograma, Fashion AI — respostas do Vinicius (13 jul 2026)
   registradas: uRocket e uTrack descontinuados; uPick = módulo "apostas" (candidato `ApostAI`
   se existir, não confirmado); uMetrics e ISPS incertos/desconhecidos; `uBuy ≈ FornecAI`
   **pendência explícita, não confirmada** — tudo formalizado em `_pendencias-gerais.md` itens
   10-16, com nota de que uma futura varredura de triagem (CEO/Operação/etc.) vai dar dono a
   cada item. Repositórios reais de produto encontrados (`umode-desenvolvai/`,
   `umode-planejai/`, + outros): CriAI (maturidade real "87.75% robustez"), VendeAI (confirmado
   **fora** da Arquitetura uMode V1 oficial — só piloto de tese com a NK, sinal de maturidade
   MVP/Ideação), CX Hub (confirmado "Fases 0-9 concluídas, em produção" — sinal de maturidade
   Escalável, e é literalmente a mesma ferramenta operacional do campo `Vinculada ao CX Hub?`).
   **Protocolo + template de Produto criados (14 jul 2026)** — pedido do Vinicius, pra usar como
   critério de avaliação antes de continuar puxando os 12 itens restantes do Portfólio:
   `uMode/00_Institucional/_protocolos/protocolo-gestao-produto.md` +
   `uMode/03_Produto-e-Solucoes/_template_produto/_contexto/produto.md` (mesma convenção de
   `_template_cliente/`). Campos: Identificação (nome atual/legado/descrição/destino/área
   conectada/geração), Maturidade (score + fonte e data — nunca solto), Pipeline e relações
   (upstream/downstream/módulos relacionados), Adoção por cliente (lista simples — detalhe de
   condução fica pra futura entidade Solução×Cliente), Marcos (append-only), Governança, Fontes.
   **Decisão explícita: as 16 pastas de produto reais não foram criadas ainda** — depende do
   backlog "Subáreas internas da Casa por Área" (nomes vêm do CEO), item 3 abaixo. `CONTEXT.md`
   já referencia o novo protocolo na seção "Decisão: camada Produto na hierarquia".
   **Teste do template contra dado real (14 jul 2026) — 4 ajustes decididos e aplicados.**
   CriAI, VendeAI e CX Hub preenchidos como rascunho (não registro real, pastas de produto ainda
   não existem) em `_varredura-drive-notas.md`. Os 4 gaps achados no teste foram resolvidos pelo
   Vinicius e aplicados em `protocolo-gestao-produto.md` + `_template_produto.md`
   (`_pendencias-gerais.md` itens 17-20, marcados resolvidos): (a) Score de maturidade ganhou
   regra de tradução fixa (produção→Escalável / piloto com arquitetura definida→MVP /
   conceito→Ideação; métrica numérica é só evidência de apoio) — aplicada: CriAI=Escalável,
   VendeAI=MVP, CX Hub=Escalável; (b) `Clientes que contrataram` agora exige qualificador
   `(contratado)`/`(piloto)` — ex.: "NK (piloto)" pra VendeAI; (c) `Adoção por cliente` vira
   texto fixo "Não aplicável" quando Destino = Interna; (d) Governança separou `Owner /
   Estratégia` de `Operador` (CX Hub: João Risoléo × Victor). Template e protocolo agora
   refletem a versão testada — próximo passo é retomar a varredura dos 12 itens restantes do
   Portfólio já com essas regras em uso.
   **Inventário completo de repositórios reais achado (14 jul 2026)** — em vez de buscar
   produto por produto, achei a pasta-mãe de todos os repositórios (`_varredura-drive-notas.md`
   → "Inventário completo de repositórios reais"). Confirma repositório próprio pra 9 dos 16
   itens (PlanejAI, CriAI, DesenvolvAI, VendeAI, CX Hub, Gest Hub, ONB HUB, IntHub, Taxonomia —
   este último só a pasta, conteúdo não lido ainda). **6 itens sem repositório encontrado**
   (FornecAI, EnriqueceAI, GerenciAI, AlocAI, CliprocAI, Sales Hub) — candidato forte a
   maturidade Ideação pela regra do protocolo, mas não confirmado sozinho. CadastrAI tem
   candidato forte (`catalogcraft-ai`/`umode-catalog-ai`, uso real com Luiza Barcelos), mas nome
   exato não confirmado no documento. Achados **5 repositórios fora dos 16 do Portfólio**
   (`CopAI`, `umode-identidade`, `umode-design-guardian`, `journey-insight-whisper`,
   `u-mode-blueprint`). **`umode-brainhub-console` aberto e lido (14 jul 2026): NÃO é a
   plataforma BrainHub/BrainWave que estamos desenhando** — hipótese descartada por conteúdo
   real. É um console interno de operação/design system já em uso (rotas `/frota`,
   `/aprovacoes`, `/cores`, `/tipografia`...), cujo backend lê `~/Documents/uMode-OS/frota/`
   local — **confirma que o guardrail "Drift Sweep" do Sistema Operacional uMode
   (`CONTEXT.md`) está implementado de verdade**, não é só conceito. Risco de colisão de nome
   registrado: "BrainHub Console" (este app) ≠ "BrainHub" (nosso projeto) — não fundir. Nenhum
   dos nomes novos foi adicionado ao Portfólio sozinho — tudo pergunta em aberto pro Vinicius.
   **Sinal de maturidade adicional registrado no protocolo** (confirmado pelo Vinicius):
   repositório fora da conta GitHub principal da uMode (organização paralela) é evidência de
   apoio a favor de `MVP` — múltiplas contas GitHub em uso é esperado, não estranhar.
   **Confirmação de repositórios reais virou pendência formal** (`_pendencias-gerais.md` item
   21) — é atividade manual do Vinicius, sem prazo definido; a varredura desse ponto específico
   não avança sozinha até a devolução chegar. Frente de Soluções/Portfólio pausada aqui.

   **Tarefa 06 — aba Demandas, com RFI dobrada dentro (14 jul 2026).** A aba "RFIs" deixou de
   ser aba de topo — RFI vira seção dentro do detalhe da Demanda (só aparece quando `RFI
   vinculada` existe). Conceito central da tela: toda atividade de colaborador nasce como
   Demanda; a fila "Aguardando minha aprovação" é o filtro mais importante (aprovar/reprovar em
   destaque no detalhe). **Campo generalizado**: `Vinculada ao CX Hub?` (binário) virou
   `Vinculada?` (Sim/Não) + `Vínculo` (lista, aceita mais de um sistema) — decisão do Vinicius
   pra já comportar destinos além do CX Hub no futuro (ex.: Vendas), sem esperar o caso real
   aparecer. Aplicado em `protocolo-gestao-demanda.md`, nos 2 templates, e retrofitado nas 236
   demandas reais via `scripts/retrofit-vinculada-generico.ps1` (0 divergências na revalidação
   de headings). `brainwave/CONTEXTO.md` atualizado: 6 abas → 5, mecanismo de aprovação e tabela
   de navegação refletindo `Vinculada?`/`Vínculo`. Duas notas de visão registradas no protocolo
   (não construídas agora): destino de demanda pode variar por cadeira/área do colaborador (não
   só CX Hub); canais futuros de abastecimento de demanda (Discord, transcrição de reunião,
   upload de arquivo, inserção manual processada por agente).
3. **Preencher `contexto-area.md` real de 1 área de 1 cliente-piloto — tentado, bloqueado em 14
   jul 2026.** Fonte mais promissora (pasta "Drive Operação" própria de Lofty Style,
   `1sP7YqvkGtyoCXkk6BUZwaUzIBaK9JHXV`, já mapeada em varredura anterior) **não está mais
   acessível** (`get_file_metadata` retornou "entidade não encontrada" — permissão revogada ou
   pasta movida/removida). A pasta de atas gerais (`Cronograma e Relatórios`) mistura todos os
   clientes sem filtro por título — abrir atas uma a uma pra achar conteúdo real de uma área
   específica de Lofty é exploração grande, não faço sem alinhar com o Vinicius antes. Continua
   pendente — não inventei conteúdo pra fechar isso.
4. ~~Decidir com o Vinicius: formalizar o variante 1ª-pessoa de `contexto-area.md` das 8 Áreas da
   Casa como template próprio~~ — **✅ resolvido em 14 jul 2026.**
   `uMode/00_Institucional/_contexto/_template_contexto_area_casa.md` criado, validado por diff
   contra as 8 áreas reais (0 divergências), registrado em `CONTEXT.md`. `_pendencias-gerais.md`
   item 8 marcado resolvido.
5. Definir a escala/critério de triagem do campo `Nível HIC` (Pessoa) — hoje só o campo existe.
   **Backlog confirmado pelo Vinicius em 14 jul 2026: importante, mas não mexer agora.**
6. Continuar a varredura Google Drive com foco em ferramentas internas × Áreas — próximos
   destinos: 3 páginas Notion linkadas no CRM (pasta própria de Lofty não está mais acessível,
   ver item 3 acima)
7. Revisar com o Vinicius as pendências centralizadas em `_pendencias-gerais.md` (agora 20
   itens vivos, itens 8 e 17-20 já resolvidos): Cadeira×Área (3 taxonomias diferentes),
   `Área (CX Hub)`="OPERAÇÃO" sem match, Tamanho atendimento×Grupo de segmentação, Taís Moser
   (uMode ou cliente?), "Laura" da Alocação contratual, `### ERP`/`### Notion` em Luiza
   Barcelos, CRM desatualizado, `contexto-area.md` de cliente vazio (item 9), nomenclatura
   legado→novo do Portfólio (itens 10-16), repositórios reais (item 21). **Backlog confirmado
   pelo Vinicius em 14 jul 2026: importante, mas não mexer agora.**
8. Cadastrar cliente 5 e fechar validação do template com 5 cases (retomado após o piloto
   de demandas)
9. Montar simulação de fluxos para apresentação 17/07
10. Decidir sobre o formulário de personificação de Pessoas (Lovable) — campos documentáveis
    já estão preenchidos nas 4 fichas existentes; falta só a parte de personificação.
    **Backlog confirmado pelo Vinicius em 14 jul 2026: importante, mas não mexer agora.**

## Frente Formulários/Lovable/Agentes — PAUSADA (proposta em 14 jul 2026, adiada no mesmo dia)
> **Status: pausada.** No mesmo dia em que foi proposta, o Vinicius redefiniu a prioridade
> máxima como "replicar tudo que já validamos pra todos os clientes reais" (ver ⭐ ORDEM DE
> PRIORIDADE no topo deste arquivo). Esta frente (formulários padronizados, réplica em Lovable,
> agente de transcrição, agente de card no CX Hub) continua válida e registrada — só não é o
> próximo passo. Retomar depois que a replicação total avançar.

**Acesso Drive ampliado, achado nesta sessão.** O Vinicius indicou
`drive.google.com/drive/folders/1LPFb_DUTzFngwBpjj-zP0ZcmOTviMbM5` — raiz que contém, entre
outras, uma pasta **"Clientes"** nunca mapeada antes, com pasta própria por cliente real
(Cambos, Luiza Barcelos, e outros fora do nosso piloto). Achado imediato em `Cambos/`:
`CONTEXTO_CAMBOS.md` + `CONTEXTO_CAMBOS_FATOS.md` (contexto de negócio real, denso) e confirmação
de que **CliprocAI é real** — módulo CLIente×PROduto×CAnal, Cambos como cliente piloto, mesmo
padrão ADR-006 do VendeAI (fora da Arquitetura V1 oficial, maturidade MVP não Escalável),
registrado em `_pendencias-gerais.md` item 22. **Achado crítico de confidencialidade**: a fonte
se autodeclara "T1 — restrito, contém custo/margem, NÃO sincroniza Drive/Notion do time" — não
usei nenhum dado comercial sensível (faturamento/custo/margem/CNPJ) e não vou usar sem
autorização explícita, mesmo sendo dado real e disponível.

4 frentes novas trazidas pelo Vinicius, ainda não iniciadas — tamanho estimado, pra decidir
prioridade antes de começar a construir:

1. **Formulários padronizados de coleta de dado (Lovable).** Objetivo: identificar quais campos
   `[a preencher]` já têm formulário possível de montar (payload = nosso schema de MD), sem
   decidir quem é o responsável agora. Como os formulários vão ser iguais na casca, a saída é um
   **prompt único e parametrizado** (só as perguntas variam). **Tamanho: pequeno pra mapear quais
   campos valem a pena (auditoria), médio pra desenhar o prompt-molde.** Regra do próprio
   Vinicius: só vale a pena agora se a falta do dado estiver travando algo real da evolução —
   não fazer só porque "seria bom ter".
2. **Réplica das 10 tarefas do BrainWave num projeto Lovable do zero**, com os `.md` reais
   subidos direto no repositório que o Lovable cria — funcionando como um "Obsidian" sobre o
   nosso próprio cérebro, não mais telas com dado de exemplo. Motivo: a URL do BrainHub (via
   BrainWave) não tem acesso ao ecossistema de MDs — Lovable, com upload direto, teria. Permite
   testar de verdade contra documentação real. **Tamanho: grande** — não é só portar os 10
   prompts, é redesenhá-los sabendo que agora há acesso a arquivo real (menos "[exemplo]", mais
   leitura direta).
3. **Dentro da frente 2 — arquitetar o agente de transcrição de reuniões**: o que precisa
   incrementar na nossa estrutura de pastas atual (onde uma transcrição vive, como vira Demanda
   ou alimenta Conversas, etc.) — ainda não desenhado.
4. **Dentro da frente 2 — arquitetar o agente de criação de card no CX Hub pós-aprovação**:
   precisa entender o repositório real do CX Hub (`gist-sparkle`, já parcialmente lido nesta
   sessão), os contratos/API usados, como criaria um card, e como validaríamos a criação.
   Destrava a automação já sinalizada como "fora de escopo" em `protocolo-gestao-demanda.md`.

**Sequência recomendada (proposta, não decidida ainda):** 1 (rápido, só a auditoria de quais
campos travam algo) → 3 e 4 (arquitetura, ainda em papel, sem construir) → 2 (a resposta técnica
grande, feita só depois de 1/3/4 estarem claros o suficiente pra não redesenhar no meio do
caminho).

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
- **14 jul 2026** — Sessão 24: sessão longa, telas do BrainWave + varredura de Portfólio +
  reprioritização geral no fim. **Telas do BrainWave**: task 05 (Soluções — grade, filtros
  Destino/Geração/Maturidade), task 06 (Demandas, RFI ainda separada), tasks 07 (Demandas vira
  tabela + Conversas + Reatribuir, RFI dobrada pra dentro), 08/09/10 (aba Agentes — reserva do
  agente geral "Dúvidas", depois 4 classes com RAG por escopo — Por Área/Por Cliente/Por
  Solução/Personalizado —, depois correção de filtro funcional + chat que tinha sumido).
  Arquitetura de "comunicação interna" registrada em `brainwave/CONTEXTO.md` (3 padrões: agente
  geral, Conversas na Demanda, Reatribuir). **Varredura de Portfólio**: protocolo + template de
  Produto criados e testados contra CriAI/VendeAI/CX Hub reais (4 ajustes aplicados); inventário
  completo de repositórios achado (9/16 confirmados, 6 sem repositório, 5 nomes fora do
  Portfólio, `umode-brainhub-console` descartado como candidato à plataforma BrainWave — é outro
  app real, "BrainHub Console", que confirmou o guardrail Drift Sweep implementado de verdade).
  Campo `Vinculada ao CX Hub?` generalizado pra `Vinculada?`+`Vínculo` (retrofit nas 236
  demandas). Template do `contexto-area.md` da Casa formalizado (`_template_contexto_area_casa.md`,
  resolve pendência 8). **Tentativa de preencher `contexto-area.md` real de um cliente-piloto
  falhou** — pasta Drive antes mapeada da Lofty não está mais acessível. **Acesso Drive
  ampliado no fim da sessão**: o Vinicius indicou a pasta-raiz `1LPFb_DUTzFngwBpjj-zP0ZcmOTviMbM5`,
  nunca explorada — revelou uma pasta "Clientes" com conteúdo real por cliente (achado imediato:
  `CONTEXTO_CAMBOS.md`/`_FATOS.md`, confirmando CliprocAI como módulo real MVP piloto da Cambos,
  mesmo padrão do VendeAI — mas **autodeclarado T1-restrito, contém custo/margem, não pode
  sincronizar Drive/Notion do time** — pergunta de confidencialidade feita ao Vinicius, **ainda
  sem resposta ao fim da sessão**, nenhum dado sensível usado). **Reprioritização geral, pedida
  pelo Vinicius antes de migrar de workspace**: a prioridade deixa de ser telas/varredura de
  Portfólio e vira "replicar tudo que já validamos (institucional/jornada/pessoas/demandas/RFIs)
  pra TODOS os clientes reais", não só os 4 piloto — com o cuidado explícito de primeiro filtrar
  quem realmente é cliente uMode moda-PLM na pasta "Clientes" (tem entradas que parecem ser
  outros negócios do CEO, não clientes). Registrado como "⭐ ORDEM DE PRIORIDADE" no topo deste
  arquivo. `START.md` conferido — continua válido, nenhuma mudança necessária pra a próxima
  sessão se orientar sozinha lendo `CLAUDE.md`→`CONTEXT.md`→`STATE.md`→`brainwave/CONTEXTO.md`.
- **03 ago 2026** — Sessão 25: **replicação total ("rolo compressor"), 1ª passada.** O Vinicius
  reconfirmou e ampliou a prioridade: 100% da energia em alimentar de informação a estrutura já
  validada, para TODOS os clientes — e avisou que existe uma outra fonte rica de informação
  institucional (produtos, áreas) que vai reprocessar/corrigir conteúdo já firmado numa fase
  seguinte. `⭐ ORDEM DE PRIORIDADE` reescrita no topo deste arquivo com essa sequência.
  **Passo zero — lista definitiva de clientes:** as pastas de dado bruto saíram do repositório na
  Sessão 23, então todas as fontes foram puxadas de novo do Drive via MCP e processadas em disco,
  sem passar conteúdo bruto pelo contexto: CRM "Mapa de Clientes" (49 linhas × 47 colunas),
  "Demandas de Clientes" (836), "Reuniões Compartilhadas com Clientes" (939), "RFI Escopo - Lista de
  Entregáveis" (53) — todos snapshot de 05 mar 2026, com ID de Drive registrado em cada arquivo
  gerado. Cruzando CRM × pasta Drive "Clientes": **46 clientes reais** (49 − 3 que não são cliente:
  a própria uMode, a linha de template do Notion, e "Fornecedores"). Registrado em
  `uMode/00_Institucional/_contexto/_lista-clientes-reais.md`, com a regra de autoridade explícita
  (**o CRM é a única fonte de "quem é cliente"**; Drive é fonte de conteúdo, nunca de estrutura) —
  por isso os 9 nomes que só existem no Drive (Alpargatas, Polenectar, Genuo, Grupo Veste, Notre
  Dame, Arezzo, Posthaus, Esposende, Lupo) **não viraram casa**, viraram pendência. Decisão
  registrada: cliente em Churn/Inativo também recebe casa completa — a estrutura é o schema, e o
  histórico de quem saiu é contexto válido; o `Status atual` registra a situação real.
  **Gerado:** 42 casas novas (estrutura de pastas + `institucional.md`/`jornada.md`/`pessoas.md`),
  649 demandas de 16 clientes, 40 RFIs de 10 clientes, 3 demandas da própria Casa (as primeiras com
  `Natureza: interna`, em `uMode/00_Institucional/_demandas/`), e 9 fichas de Pessoa novas (Rafael
  Del Gaudio Renaldim, Pedro Murillo, Julianne Dias Rodrigues, Juliana Ferré Esteves, Fernanda
  Araujo, Victor Aragão, Sandro Costa, João Paulo Contar Risoleo, Elizabeth Alves de Souza Santana)
  — pessoas da Casa que o CRM nomeia como Key Account/Consultor e que nunca tinham ficha. Total: 46
  casas, 138 MDs institucionais, 885 demandas, 62 RFIs, 13 fichas de Pessoa; repositório de ~330
  para 1.159 `.md`. **Tudo validado por diff de headings contra o template correspondente — 0
  divergências**, exceto a já conhecida de Luiza Barcelos (`### ERP`/`### Notion`).
  **Lacuna antiga fechada:** as 4 fichas de Pessoa existentes diziam "possivelmente outros clientes
  fora do piloto, não verificado" — agora verificado nos 46: Laura 9 clientes como KA, Andrea 9 KA +
  4 como Consultora (tudo em "historicamente", já que está Inativa), Vanessa 10 como Consultora + 1
  como KA, Marina 1. Achado registrado sem resolver: em NV, Vanessa aparece nos dois papéis ao mesmo
  tempo.
  **Disciplina de mapeamento mantida — nada aplicado antes de registrar no protocolo.** Releitura
  integral de `CONTEXT.md`, `CLAUDE.md`, `protocolo-gestao-demanda.md`, `protocolo-gestao-rfi.md`,
  `protocolo-criacao-cliente.md` e dos templates antes de decidir qualquer campo. Achados novos nos
  dados reais, todos registrados **antes** de rodar: 16 combos novos de Status+Etapa em
  `protocolo-gestao-demanda.md` (com a regra que já era implícita agora escrita: Status prevalece,
  Etapa só refina quando nomeia estágio distinto; conflito vira observação dentro da demanda);
  primeiro uso real do status `A fazer` (`Demanda Aceita | Na Fila`); `Criticidade: Crítica /
  Urgente` → `Urgente` (variante de nome), `Baixa` → `[a preencher]` (não existe valor abaixo de
  Média no enum); `Área Responsável: INOVAÇÃO / IA` → **não mapeado de propósito** (ambíguo entre os
  dois quadros do CX Hub), valor bruto preservado em `Notas internas`; 2 status de RFI legados
  traduzidos em `protocolo-gestao-rfi.md` (`RFI Aceita - Criar no Linear e Estimar Entrega` → `RFI
  Aceita — Criar Demanda e Estimar Entrega`, coerente com a decisão já travada de descartar
  referência ao Linear; e `RFI Não iniciada` → `RFI Não Iniciada`).
  **Scripts atualizados para v2 e parametrizados** (a pasta de dado bruto não vive mais no
  repositório): `gen-demandas.ps1` (agora emite `Status (interno)`/`Vinculada?`/`Vínculo`, que antes
  vinham de scripts de retrofit separados; aceita mês em inglês; ganhou `-Casa`), `gen-rfis.ps1`, e
  dois novos: `gen-clientes-crm.ps1` e `gen-pessoas-crm.ps1`. Todos com rede de segurança contra
  nome de coluna inexistente (que descartaria dado em silêncio) e salvos com BOM UTF-8 — o bug de
  mojibake em literal acentuado no PowerShell 5.1 reapareceu e foi contornado do mesmo jeito das
  sessões anteriores.
  **9 pendências novas** em `_pendencias-gerais.md` (itens 23-31), as mais relevantes: os 9 nomes do
  Drive sem linha no CRM; `Regime CS`/`Negociação` fora do enum de Status do template; 1 RFI da
  própria Casa **sem cliente**, que contradiz a premissa "RFI sempre tem cliente" do protocolo; e o
  fato de **todas as fontes serem de mar 2026** — os pilotos, formalizados de exports de jul 2026,
  têm mais registros (Lofty 85 demandas vs 62 no snapshot), então **não foram regenerados** (seria
  perda de dado). Um re-export das bases do Notion em ago 2026 completa os 42 clientes novos sem
  retrabalho estrutural. Narrativa de demanda/RFI dos clientes novos segue `[a preencher]` — CSV do
  Notion nunca traz corpo de página (limitação já conhecida desde a Sessão 12).

- **03 ago 2026** — Sessão 25 (continuação): **2ª rodada da replicação total — a fonte de julho
  estava no histórico do Git.** Fechei a 1ª rodada registrando como pendência que "todas as fontes
  disponíveis são snapshot de mar 2026" e que faltava o Vinicius gerar um re-export do Notion. O
  Vinicius questionou a premissa — se eu sei qual fonte gerou os 4 pilotos com dado de jul 2026,
  por que não usar a mesma para os outros 42? Estava certo, e o erro era meu: as pastas de export
  (`Demandas Totais CSV e Markdown/`, `RFIs Totais CSV e Markdown/`, `RFIs Gerais - Lofty/`, 947
  arquivos) foram **commitadas na Sessão 22 e removidas na Sessão 23** (commit `8c6705b`) — ou
  seja, sempre estiveram recuperáveis do histórico. Recuperadas com
  `git archive 8c6705b^ -- <pastas>` para fora do repositório (o repositório continua só com `.md`,
  decisão da Sessão 23 preservada). Confirmação de que é a mesma fonte dos pilotos: Lofty 85,
  Luiza Barcelos 70, Cambos 47, Moda Objetiva 34 — batem exato com o que já estava formalizado.
  **Ganho de volume:** demandas não-piloto de 649 → **757** (+108: Reserva 111→120, Osklen 93→117,
  NV 95→108, NK STORE 74→87, VIX 52→70, Lenny Niemeyer 59→69, Caedu 18→26, Oficina Reserva 23→28,
  Baw 15→18, Plie 12→16, Puket 15→16); RFIs não-piloto de 40 → **63**. Os 689 arquivos gerados da
  fonte de março foram apagados e regenerados da fonte de julho — os pilotos não foram tocados.
  **Ganho de conteúdo (o mais importante):** o export de julho tem **86 markdowns de RFI, um por
  página, cobrindo todos os clientes** — casados por `ID` da base. Resultado: **84 das 85 RFIs
  formalizadas agora têm narrativa real** (tabela Demanda Cliente/Detalhamento/Estimativa, bloco
  "De Acordo", anexos citados), contra 22 antes. Headings markdown da fonte convertidos em negrito
  para não colidir com os headings do template — mesma solução da Sessão 21. Só a
  `Reservado - Colmeia` (ID 16) segue sem narrativa, porque o markdown dela não tem corpo.
  A narrativa de **demanda**, porém, continua `[a preencher]` fora de Lofty: o export tem markdown
  de 85 demandas e **todas são de Lofty Style**; a coluna `Texto` (corpo da página) vem preenchida
  em **2 de 1007** linhas. A limitação não era o snapshot — é que o export por página só foi feito
  para Lofty (pendência 29, reescrita).
  **"Dissecar tudo" — 10 colunas do export que eu não estava aproveitando.** A 1ª rodada usava 16
  das 35 colunas. Registradas no protocolo **antes** de aplicar: (a) `RFI` (44 linhas) → o campo
  `RFI vinculada`, que estava `[a preencher]` em 100% das demandas — resolvido contra as RFIs
  formalizadas do mesmo cliente por casamento de nome; **o vínculo bidirecional Demanda ⟷ RFI
  passou a existir de verdade** em 44 demandas; (b) `Bloqueio` (37) → `Motivo de bloqueio`, com
  tabela de tradução (só `Aguardando o Cliente` tem equivalente exato; os outros 5 valores vão pra
  `Outra` mantendo o valor original visível, e o motivo real prevalece sobre o `Aguardando Decisão`
  que a v1 inferia da regra de Standby); (c) `Texto` → `Descrição`; (d) 7 colunas com dado real e
  **nenhum campo equivalente** (`Responsabilidade` — 100% preenchida —, `Projeto`,
  `uMode - Macro Tema`, `Comentário uMode`, `Suporte Integração`, `Tempo de Resolução`,
  `Nível de Esforço`) preservadas em `### Notas internas` num bloco rotulado de campos legados, em
  vez de descartadas (perda de dado) ou promovidas a campo novo (mudança de estrutura que exige
  validação). `Responsabilidade` ficou registrada como candidata mais forte a campo próprio
  (pendência 32).
  **Pilotos ficaram temporariamente mais pobres que os novos** — foram gerados pela v1, sem esses
  campos. Resolvido por **retrofit** e não por regeneração, porque as 85 demandas de Lofty têm
  narrativa vinda de export HTML por página que o CSV não contém: `retrofit-demandas-campos-julho.ps1`
  tocou só 3 campos nas 236 demandas dos 4 pilotos (7 vínculos de RFI, 3 motivos de bloqueio, 236
  blocos de campos legados), casando por `ID legado` ↔ `ID` do CSV, 0 sem match.
  **6 combos novos de Status+Etapa** apareceram na fonte maior e foram registrados antes de rodar
  (`Concluída|(vazio)`, `Standby - Produto|(vazio)`, `Standby - Produto|Análise Cliente`,
  `Encerrada|Na Fila`, `Não iniciada|Análise Cliente`, `Demanda Aceita|Backlog`). O último rendeu a
  regra explícita que faltava: **o 1º nível decide se houve aceite, a Etapa só diz em que ponto
  está** — por isso `Demanda Aceita|Backlog` → `A fazer` (aceita, não iniciada) e não é conflito,
  enquanto `Nível de Análise|Backlog` → `Análise`.
  **Regra de multi-cliente de RFI aplicada pela primeira vez:** 2 linhas legadas listavam 2
  clientes; ID 94 virou duas RFIs (Reserva + Oficina Reserva), cada arquivo avisando no corpo que
  compartilha o `ID legado` com o par. ID 79 (`uMode + Lofty Style`) só tem o lado Lofty — o lado
  uMode não tem onde viver, mesmo caso da RFI 72 (pendência 27/35).
  **Bug real de PowerShell, novo na lista:** `$l` e `$L` são **a mesma variável** (PowerShell não
  diferencia caixa em nome de variável) — o loop que escrevia a narrativa (`foreach ($l in ...)`)
  sobrescrevia a lista de saída `$L`, e o `.Add` seguinte estourava com "[System.String] não contém
  um método denominado 'Add'". Corrigido renomeando a variável de loop, com comentário no script
  pra não repetir. Reapareceu também o já conhecido: pipeline que devolve 1 item vira string
  escalar, resolvido com `@(...)`.
  **Validação final:** 993 demandas de cliente + 85 RFIs + 4 demandas da Casa, todas por diff de
  headings contra o template — **0 divergências**. Nenhum combo de status caiu no default. 5
  pendências novas (32-36) e as pendências 28/29 reescritas: a 28 está resolvida, a 29 passou a
  descrever com precisão o que ainda falta (export por página das demandas dos clientes que não
  são Lofty).


- **03 ago 2026** — Sessão 25 (fecho): **auditoria de padronização e indexação**, a pedido do
  Vinicius. Registrada em `uMode/00_Institucional/_contexto/_auditoria-indexacao.md`.
  Padronização **confirmada**: 1.241 arquivos reais auditados por diff de headings contra o template
  correspondente, **1.240 conformes** — a única divergência é a de `Luiza Barcelos/institucional.md`
  (`### ERP`/`### Notion`), pré-existente e já pendente de decisão. Integridade de ID: 0 duplicados
  (demanda e RFI, por cliente), 0 `ID legado` reutilizado, 0 mojibake, encoding uniforme.
  Indexação **medida, não opinada**: o que resolve por máquina hoje é o eixo Cliente — Demanda → casa
  993/993 (100%), Pessoa → clientes atendidos 62/62, Demanda → RFI 44/44, Demanda → CX Hub 993/993; e
  consulta agregada funciona sem índice auxiliar (testado com Osklen por status). O que está vazio são
  os eixos Área e Solução: `Destino (organizacional)` 0/993, `Contexto consultado`/`impactado`
  0/993, `Demanda mãe`/`filhas` 0/993, `contexto-area.md` de cliente 0/644, `produto.md` 0/16, e
  RFI → Demanda 0/85 (dívida do Notion legado). Densidade geral: 19,2% das linhas são `[a preencher]`.
  Diagnóstico registrado: um agente **Por Cliente** já tem substância real; um agente **Por Área** ou
  **Por Solução** ainda não teria quase nada — preencher isso é trabalho de conteúdo, não de estrutura.
  3 pendências novas (37-39): falta de `client_id` estável (o nome da pasta é a chave — 0 falhas hoje,
  mas renomear quebraria vínculos em silêncio); indexação derivável por convenção e não declarada
  (0 de 1.291 arquivos com frontmatter) com a decisão de índice derivado vs. frontmatter; e o
  levantamento dos eixos Área/Solução como o gargalo real dos agentes.

- **03 ago 2026** — Sessão 25 (fecho 2): **posicionamento pedido pelo Vinicius — as 3 pendências de
  padronização/indexação foram decididas e aplicadas, não devolvidas como opção.** (1) **Divergência
  de Luiza Barcelos resolvida:** era lacuna do template, não erro do cliente — `### ERP` removido
  (duplicava `ERP / Integração`, com a restrição de escopo preservada como nota) e
  `### Notion (cadastro de cliente)` virou item de uma seção nova `### Outras fontes`, porque o
  problema era geral: o CRM traz rotineiramente Portal do Cliente/Documentação/OKRs/material/WhatsApp/
  chamados, que na 1ª rodada eu havia jogado em `Contexto crítico` por falta de lugar. Template
  atualizado, 42 clientes regenerados, 4 pilotos retrofitados — **46 de 46 conformes, 0 divergências**.
  (2) **Índice implementado agora:** `_indice/` com `clientes.csv` (46), `demandas.csv` (997),
  `rfis.csv` (85) e `pessoas.csv` (13), gerado por `scripts/gen-indice.ps1` a partir dos MDs —
  aditivo, reversível, sem tocar em nenhum MD. **Frontmatter recusado** (criaria duas fontes de verdade
  pro mesmo campo e mexeria em 1.292 arquivos pra resolver um problema que não existe: o parsing por
  heading funciona em 100%). Testes relacionais imediatos: demandas em aberto por cliente (Reserva 78 ·
  NV 36 · Osklen 15) e valor negociado em RFI por cliente (NV R\$ 30.651 · NK STORE R\$ 26.250).
  (3) **Problema do nome resolvido em vez de registrado:** `### ID do cliente` (slug estável) nos 46 —
  `NK STORE`/`NK Store` colapsam em `nk-store`, então a variação de caixa/acento deixa de ser
  problema; apelidos que não colapsam (`Lofty`, `Lenny`, `OFICINA`) foram extraídos dos títulos de
  RFI e viraram `### Aliases do cliente`. Ambos os campos entraram no template e no
  `protocolo-criacao-cliente.md`. `CONTEXT.md` não foi tocado — são decisões de padrão de documento,
  não de hierarquia. Pendências 37 e 38 resolvidas; 39 (eixos Área/Solução vazios) segue aberta, é
  trabalho de conteúdo. **2 bugs de PowerShell novos, documentados nos scripts:** função não pode se
  chamar `Ls` (alias tem precedência sobre função e devolvia FileInfo em vez das linhas — deixou o
  índice inteiro vazio na 1ª execução); e `Corpo` devolvendo 1 item vira string escalar, fazendo
  `[0]` retornar o primeiro **caractere** em vez da linha.

- **03 ago 2026** — Sessão 25 (fecho 3): **`client_id` travado em `CONTEXT.md`** (autorização
  explícita do Vinicius) na seção "Endereçamento de volume" — chave estável, nunca muda, absorve
  variação de caixa/acento, candidata a chave primária quando o banco existir. Em seguida,
  **varredura geral no Drive sobre ferramentas/produtos/áreas**, registrada em
  `uMode/00_Institucional/_contexto/_varredura-ferramentas-produtos-areas.md`.
  **Entrega principal: as 16 Soluções do Portfólio saíram de 0 para 16 `produto.md`** em
  `uMode/03_Produto-e-Solucoes/01_PlanejAI/` … `16_Sales-Hub/` — o eixo mais vazio do cérebro
  segundo a auditoria. Validados por diff contra `_template_produto`, 0 divergências. Maturidade
  preenchida **só onde a fonte declara**: Escalável em DesenvolvAI/CriAI/Taxonomia/CX Hub, MVP em
  VendeAI/CliprocAI, **Ideação em FornecAI e GerenciAI** (achado novo: declarações literais
  "FornecAI ainda não nasceu" e "GerenciAI ainda em brainstorm"); os 8 restantes ficaram
  `[a preencher]` com a evidência citada, em vez de balde escolhido por intuição.
  **Fonte-âncora achada:** `ARQUITETURA_UMODE_REF.md` (v1.0 abr 2026, do CEO, Drive
  `1xCFtkT5krc-VATCC26MeQHWOWH1BOMlE`) define o **fluxo oficial da Arquitetura uMode V1**
  (PlanejAI → CriAI → DesenvolvAI → FornecAI → EnriqueceAI → GerenciAI + CadastrAI núcleo + Hub de
  Agentes lateral), decidido em 24/04/2026. Isso preencheu com fonte o `Pipeline e relações` dos 6
  módulos — antes `[a preencher]` em tudo — e o índice já reconstrói o fluxo inteiro. Trouxe também
  6 princípios transversais, o dimensionamento real da Taxonomia (**12 zonas, 42 dimensões, 419
  valores**) e **4 agentes nomeados** (`product-analyzer`, `tryon-stylist`, `audio-transcriber`,
  `product-enricher`) — primeiro dado real sobre Agente, que era pura abstração.
  **O problema de taxonomia entre fontes que o Vinicius previu: encontrado, e é no nível de
  CLIENTE.** A planilha viva "uMode - Controle de Acessos" (modificada no próprio dia) lista **60
  contas de organização na plataforma**. Boa parte das variações (`RESERVA`/`Vix`/`NK Store`/
  `BAW`/`OFICINA`/`StudioZ`/`LOJÃO DO BRÁS`) **é absorvida pelo `client_id`**, que acabou de
  ser travado — mas 4 casos não são: `Objetiva` ≠ `Moda Objetiva`, `Mondepars` ≠ `Mondpars`,
  `Lojas Estrela` ≠ `Estrela`, e **conta por módulo** (`Cambos` + `Cambos - uFlow`;
  `Tempo de Criança` + `Tempo de Criança (uRocket)`). Achados ainda: **~18 organizações com conta
  ativa e sem linha no CRM** (Grendene, Dakota, Beira Rio, Via Marte entre elas), **dado de
  engajamento real por cliente** (inédito — Vix 88%, StudioZ 0%, 4takes 5%) e uma **4ª taxonomia de
  área**: os perfis de acesso da plataforma, que mapeiam quase 1:1 para as 14 áreas canônicas e são a
  melhor fonte já encontrada para o `contexto-area.md` vazio. Nada disso foi aplicado — cada um
  virou pendência (40-46) porque exige campo novo ou decisão.
  **`produtos.csv` entrou no índice** (`_indice/`, agora 5 tabelas): o eixo Solução passou a ser
  consultável, e o fluxo V1 é reconstruído a partir dele. **Lacuna maior deixada explícita:** o
  Notion é a fonte de verdade canônica declarada pela própria arquitetura ("se contradição entre este
  arquivo e a página V1 → página V1 vence") e nunca foi lido — e nesta sessão passou a existir acesso
  a ele via MCP.

- **03 ago 2026** — Sessão 25 (fecho 4): **Notion acessado e itens 1 e 2 executados.** Acesso via MCP
  ao workspace real `uMode Mode's Notion`, autenticado como o Vinícius — os IDs que o documento de
  arquitetura do Drive citava **funcionam**, não foi preciso procurar caminho.
  **Item 1 — página canônica lida:** "🏛️ Arquitetura uMode — Especificação por Módulo (V1 — sessão
  24/04/2026)" (`34db1d38e768814b8001d7cb6cacf4e5`), 51 KB, um capítulo por módulo. Decidiu 3
  maturidades que estavam `[a preencher]`: **PlanejAI → MVP** ("PRÉ-SEASON (modo atual — estúdio sob
  demanda)" × "IN-SEASON (modo futuro)"), **EnriqueceAI → MVP** ("A detecção de atributos a partir da
  foto do produto **JÁ EXISTE** e é a espinha dorsal do módulo atual") e **GerenciAI → Ideação
  confirmada** pela própria seção Status ("Brainstorm consolidado, não decisão final"). Maturidade
  decidida passou de 6 para **10 dos 16**. Achado de nomenclatura: a fonte canônica escreve
  **"ForneceAI"**, nosso Portfólio escreve **"FornecAI"** — pendência 47, nada alterado.
  **Item 2 — base viva de demandas:** `ddf1951a-8dc2-42e6-98e6-bae3d1f5a865`. Três resultados que
  mudam o planejamento: (a) **não há defasagem** — 1.010 demandas na base contra 1.007 do export,
  **só 1 criada depois de 14/jul**, mais recente 15/jul/2026, ou seja nossas 997+4 cobrem ~99% (fecha
  o resíduo da pendência 28); (b) **nossa tabela de tradução Status+Etapa está 100% correta contra o
  schema vivo** — os enums reais (6 × 9) são exatamente os que mapeamos, nenhum valor fora; (c) a
  relação `👥 Clientes` tem **`limit: 1`**, ou seja o schema **proíbe** demanda multi-cliente,
  validando nosso modelo. **Narrativa confirmada e quantificada:** `Texto` vem preenchida em 2 de
  1.010 — a narrativa vive nos blocos do corpo da página, e a extração funciona (testada na UMD-1256,
  que devolveu o texto integral do cliente + imagem). Custo: **1 chamada por página, ~750 páginas** —
  é trabalho de lote, a rodar em blocos, não uma operação única.
  **Achados estruturais novos:** enums do Notion são maiores do que o export revelava (`Bloqueio` 8
  em vez de 6, com `Aguardando Terceiros`/`Aguardando Comercial`; `Suporte Integração` **17** em
  vez de 8 — uma taxonomia técnica de integração pronta; `uMode - Macro Tema` 20); **`Projeto` é
  entidade real** com database próprio, preenchida em 594 demandas, ligando demanda → fase de
  onboarding (pendência 48); a base tem **views nomeadas por dupla de atendimento** (Laura/Holmer,
  Julianne/Pedrão, Fernanda/Victor, Marina) com lista explícita de clientes — contraprova operacional
  para as 13 fichas de Pessoa; e existe uma **5ª fonte de "quem é cliente"** (base de Clientes do
  Notion, `ec041afd-fcee-44f8-83cb-223fca6f4108`), ainda não cruzada (pendência 50).
  Pendências **28 e 43 fechadas**; novas 47-50. Ainda não lidos no Notion: skill
  `umode-arquitetura-tese`, Plano Técnico do Hub de Agentes, `CadastrAI taxonomia_v1`.
  **Combinado sobre a frente de integrações:** o Vinicius vai clonar os repositórios de integração
  (um por cliente) na máquina; recomendei uma pasta-mãe única em vez de caminhos soltos, e proposto —
  ainda a validar — um tipo de documento novo `integracao.md` no `00_Institucional/_contexto/` de
  cada cliente que tiver, com `IntHub` recebendo a lista de clientes integrados.

- **03 ago 2026** — Sessão 25 (fecho 5): **extração de narrativa do Notion — pipeline construído,
  lote 1 entregue, e o custo real medido.**
  **Alvo medido primeiro:** das 993 demandas de cliente, **106 já tinham narrativa** (as de Lofty
  Style, do export HTML de jul 2026) e **887 não tinham**. Dessas, **208 estão em aberto** (não
  Concluído/Cancelado) — Reserva 78, NV 36, Osklen 15, VIX 12, NK STORE 11, Caedu 9… Foi a fila
  escolhida para começar: é o que está vivo.
  **Pipeline criado e validado:** `scripts/inject-narrativa-notion.ps1`, que recebe um arquivo de
  lote em markdown (`@@UMD-xxx` + linhas da narrativa, e uma seção `@@VAZIO`) e injeta em
  `## Conteúdo → ### Descrição` do `D-AAAA-NNN.md` certo, casando por `ID legado`. Duas
  garantias no script: não sobrescreve narrativa já existente, e revalidação por diff de headings
  depois (993 demandas, **0 divergências**).
  **Lote 1 — 8 demandas processadas:** 5 com narrativa real gravada (UMD-177, UMD-187, UMD-1127,
  UMD-1234 da Caedu; UMD-1256 da NK STORE) e 3 **marcadas como verificadas-vazias** (UMD-133,
  UMD-50, UMD-197). Essa segunda marca é tão importante quanto a primeira: converte "lacuna
  desconhecida" em "verificado, não tem corpo, não consultar de novo". Exemplo do ganho real: a
  UMD-1127 (Caedu) trouxe o retorno do cliente sobre **170 produtos que falharam no primeiro
  script**, categoria por categoria, com os IDs a aplicar — informação operacional que nenhum export
  de CSV entrega.
  **Taxa de acerto medida: ~60%** têm corpo de página; ~40% são só título. Não há como saber qual é
  qual sem buscar.
  **Custo real, medido e não estimado:** o corpo da página só vem por `fetch` **página a página** —
  1 chamada por demanda, e cada resposta traz o caminho de ancestrais + todas as propriedades como
  ruído junto do conteúdo que interessa (~2,5 KB de contexto por demanda). Para as 208 em aberto são
  ~208 chamadas e ~500 KB de contexto; para as 887 totais, ~2,2 MB. **Isso não cabe em uma sessão**,
  porque tudo passa pelo meu contexto e depois é reescrito no arquivo. O caminho eficiente é rodar os
  lotes em subagentes (contexto próprio, gravam direto no arquivo) — **perguntado ao Vinicius, não
  feito por conta própria**, porque a regra desta configuração é não acionar subagente sem pedido.
  Sem isso, a alternativa é lote de ~15-20 demandas por sessão.

- **03 ago 2026** — Sessão 25 (fecho 6): **mapa de infra de tecnologia criado**, a pedido do Vinicius,
  em `uMode/06_Tecnologia/_contexto/_backlog-infra-tecnologia.md`. Instrução explícita: **não
  desenvolver API nenhuma agora** — só rastrear e mapear, porque vários agentes vão precisar beber
  direto da fonte dos repositórios para operacionalizar. Estruturado em: (1) **acesso programático às
  fontes** — o achado central é que **todo** acesso externo hoje é MCP autenticado como pessoa física
  (a conta do Vinicius), o que serve para sessão assistida e **não** para agente autônomo; inclui os
  IDs das 5 bases do Notion que os agentes vão consumir, o limite medido de que corpo de página só sai
  por fetch página a página (~887 chamadas para completar a narrativa), a necessidade de service
  account no Drive, o acesso aos repositórios de integração, a API do CX Hub (que destrava o agente de
  card pós-aprovação) e a ausência de API de telemetria da plataforma — hoje o dado de engajamento por
  cliente só existe numa planilha mantida à mão. (2) **O que construir para o cérebro operar**: job de
  sincronização incremental fora de máquina pessoal, índice derivado em servidor, RAG **com respeito
  ao isolamento entre clientes** (regra travada), migração para banco com `client_id` como PK
  candidata, e backend dos formulários. (3) **8 dívidas de dado** (5 fontes de "quem é cliente",
  conta-por-módulo, RFI→Demanda não resolvível, enums incompletos, INOVAÇÃO/IA sem match, registros
  sem cliente, imagens de narrativa hospedadas fora do Notion com link expirável, grafia
  ForneceAI×FornecAI). (4) **5 limites de ambiente que já bateram** nas sessões (caminho de 260
  chars no Windows, encoding/BOM no PowerShell 5.1, pipeline de 1 item virando escalar, alias vencendo
  função, e leitura de arquivo grande estourando resposta do MCP) — registrados porque voltam se a
  infra rodar os mesmos scripts. Referência cruzada criada em `_pendencias-gerais.md` item 51.
  **Combinado:** o Vinicius confirma quando os clones dos repositórios de integração estiverem na
  pasta-mãe.

- **03 ago 2026** — Sessão 25 (fecho 7): **frente de integrações aberta — 5º tipo de MD de cliente
  criado.** O Vinicius disponibilizou os repositórios clonados em
  `C:\Ambientes Virtuais\uMode-Integracoes\` e passou o **mapeamento repositório → cliente vindo do
  desenvolvedor**, que era indispensável: eu havia inferido `arzz-sap` = Arezzo pela semelhança do
  nome e **estava errado** — é **AZZAS**, o grupo, ou seja **Reserva + Oficina Reserva**; e
  `unico-linx` é **Puket**, que ninguém adivinharia. A correção chegou antes de qualquer arquivo ser
  gerado. Registrado como aviso permanente no protocolo: **nunca inferir cliente pelo nome do
  repositório**. Efeito colateral: **Arezzo volta a não ter confirmação** de ser cliente (item 23).
  **Criados:** `protocolo-gestao-integracao.md` + `integracao.md` no `_template_cliente` +
  `scripts/gen-integracoes.ps1`, e **11 `integracao.md` reais** (10 repositórios, sendo que
  `arzz-sap` atende 2 clientes — cada casa tem o seu arquivo apontando para o mesmo repositório,
  com aviso no corpo, mesmo tratamento da RFI multi-cliente). Validados por diff de headings contra o
  template — **0 divergências**. Decisão de escopo registrada no protocolo: `integracao.md` é
  **condicional** — só existe para cliente que tem integração real, e a **ausência do arquivo é a
  informação** (não entra em contagem de pendência), mesma lógica de `_rfis/` existir só do lado de
  cliente.
  **Ganho imediato:** a checagem de consistência do próprio script achou que **Puket e Baw** tinham
  `ERP / Integração` = `[a preencher]` e têm integração **Linx** real — preenchido a partir do
  repositório, com a fonte citada no campo. O repositório é fonte melhor que o CRM para esse campo.
  **Dois estados distintos registrados como tal:** Moda Objetiva **não tem** documentação de
  integração; Puket **tem repositório sem nenhum `.md`**. "Existe integração, falta documentação" é
  diferente de "não existe integração".
  **Nesta rodada só a Identificação foi preenchida** — o resto exige ler os `documentacao-geral-*.md`
  (30 a 77 KB cada, ~500 KB no total). A estrutura dos documentos de origem **não é uniforme** entre
  clientes ("Visão Geral" em 8 de 9; "Escrita"/"Leitura" em 5 de 9; o resto específico), o que
  confirma a decisão de o nosso template ser uniforme e **resumir + apontar** em vez de copiar.
  **Subagentes autorizados pelo Vinicius**, com restrição explícita de **somente consulta, nenhuma
  alteração** — 3 disparados para a narrativa das 200 demandas em aberto restantes. Eles devolvem o
  texto; **a escrita nos arquivos continua minha**, via `inject-narrativa-notion.ps1`, com
  revalidação por diff depois. Também confirmado pelo Vinicius: **Objetiva = Moda Objetiva**, mesmo
  cliente — registrado como alias e o caso fechado na varredura.

- **03 ago 2026** — Sessão 25 (fecho 8): **extração de narrativa em lote — 3 subagentes, 208 demandas
  em aberto processadas, fila zerada.** Com a autorização do Vinicius (subagentes **somente
  consulta**, proibidos de alterar arquivo ou Notion), rodaram 3 coletores em paralelo. Eles
  devolveram o texto; **a escrita nos arquivos continuou minha**, via
  `inject-narrativa-notion.ps1`, com revalidação por diff depois de cada lote.
  **Resultado:** 136 narrativas reais gravadas + 64 demandas marcadas como **verificado-vazio** nos
  3 lotes (mais as 8 do lote manual). Narrativa no repositório saltou de **106 para 314** demandas;
  **as 208 em aberto estão 100% processadas** — não sobrou nenhuma na fila de "em aberto sem
  narrativa". 993 demandas revalidadas por diff de headings a cada injeção — **0 divergências**.
  **A marca de verificado-vazio é entrega, não ausência de entrega:** ~40% das páginas do Notion não
  têm corpo (o título é todo o conteúdo). Antes isso era lacuna desconhecida; agora está escrito no
  arquivo que a página foi consultada e não tem corpo, com data — não precisa ser buscada de novo.
  **O que a narrativa trouxe de valor real** (amostra do que estava invisível): regra completa de
  geração da **Ref Fábrica** da Moda Objetiva (5 componentes, com o de/para campo a campo negociado
  por e-mail entre uMode e cliente ao longo de 4 meses, incluindo a ordem de precedência das regras
  de código); os comandos SQL do **"aperto de botões"** da NV no Linx; erro real de deadlock em
  `PRODUTOS_PRECO_COR`; a lista dos 9 campos obrigatórios de e-commerce com a tabela e o tipo de
  cada um no Linx; o payload JSON de integração de matéria-prima do SAP da Reserva; e a decisão
  registrada de **retirar o botão "Forçar Integração" da Cambos** com o motivo técnico.
  **Ainda sem narrativa: 679 demandas**, todas com status `Concluído` (552) ou `Cancelado` (127) —
  é histórico encerrado, valor menor e custo igual. Fica como próximo lote, se e quando fizer sentido.

- **03 ago 2026** — Sessão 25 (fecho 9): **frente de integrações fechada — 11 `integracao.md`
  preenchidos com a documentação técnica real, 11 de 11 conformes ao template.** Os 3 coletores
  (somente consulta) leram os **9 `documentacao-geral-*.md`** dos repositórios clonados em
  `C:\Ambientes Virtuais\uMode-Integracoes`; a escrita continuou minha, via
  `scripts/inject-integracao.ps1`. **151 campos preenchidos em 10 arquivos** (o 11º, Puket, não tem
  documento nenhum), de 73 para até 106 linhas por cliente, 957 no total. Validação por diff de
  headings contra o template: **0 divergências nos 11**. Restam 2 lacunas por arquivo, as duas de
  governança (item 57 das pendências).
  **Três coisas exigiram intervenção minha antes de gravar, e valem como método:**
  (1) **Cada coletor leu só 3 repositórios e escreveu "única das Linx".** Cruzando os três lotes,
  várias dessas afirmações são **falsas**: Lofty "única que grava `PRODUTOS_OPE_EXTRA`" ignora a VIX;
  NK "única que não usa o interceptor" ignora NV e VIX; Osklen "único com três momentos" ignora a NV;
  VIX "único Linx sem programações de produção" inverte o fato (a NV é a única *com*). Reescrevi
  todas nomeando o conjunto de comparação real. **Lição para os próximos lotes: subagente com visão
  parcial generaliza com confiança — superlativo vindo de lote precisa ser reescopado na costura, não
  aceito.**
  (2) **Aviso de divergência de ERP desatualizado** em Puket e Baw — o `integracao.md` foi gerado
  quando o `institucional.md` ainda tinha `[a preencher]`, e campo vazio **nunca foi divergência**.
  Os 11 conferem. Corrigido por `scripts/fix-integracao-divergencia-erp.ps1`.
  (3) **A VIX tem duas datas de início do mesmo incidente** (25/03 no relatório × "aprox. 27/03, a
  confirmar" na migração SMB) e as fontes não se reconciliam. Gravei a divergência explícita em vez
  de escolher uma.
  **O que a leitura entregou de valor real:** os 4 incidentes da VIX (o único cliente com relatório
  formal — 6 semanas de integração de imagens parada após o cliente mudar host, share, domínio AD,
  credencial e VPN sem aviso, resolvido com um microserviço NestJS dedicado em EC2); e **15 riscos
  técnicos** que foram para `_backlog-infra-tecnologia.md` **seção 4** — todos já escritos no
  documento do próprio repositório, nenhum diagnóstico meu. O mais grave: **a integração da Cambos
  não envia autenticação nenhuma ao SPI**. Também nesta leitura: `umode-microservice-uconnect` (o
  interceptor) se revelou **componente compartilhado da uMode que gera referência de produto e
  injeta conta contábil** — regra de negócio sem ficha no Portfólio (item 60).
  **Achado de indexação:** os incidentes da VIX citam "RFI #83" e "RFI #85", e o campo `ID legado
  (Notion/CX Hub)` resolve os dois para `RFI-2026-005` e `RFI-2026-004`. **É a primeira prova de que
  o cérebro relaciona por um eixo que não é cliente** — documentação técnica de integração → RFI
  formalizada, sem precisar de campo novo. **Materializado no mesmo dia:** `gen-indice.ps1` ganhou o
  6º eixo, `_indice/integracoes.csv` (11 linhas), com a coluna `rfis_citadas` que varre o corpo do
  `integracao.md` por `RFI #NNN` e resolve pelo `ID legado (Notion/CX Hub)` — RFI citada e não
  resolvida entra marcada como `(não resolvida)`, em vez de sumir. Índice regenerado: 46 clientes,
  997 demandas, 85 RFIs, 16 produtos, 13 pessoas, 11 integrações.
  **Fechada a pendência 55; abertas 56 a 62 (a 58 já materializada no índice).**

- **04 ago 2026** — Sessão 25 (fecho 10): **frente de Produto — as 3 páginas canônicas do Notion
  lidas, 16 de 16 `produto.md` enriquecidos, e a maior confusão de nomenclatura do Portfólio
  resolvida.** Vinicius mandou ir no produto e liberou consultar o Notion à vontade; também passou
  um briefing próprio sobre uRocket, uFlow, uConnect, CriAI, PlanejAI, EnriqueceAI, VendeAI e Hub de
  Agentes, e travou a governança. Rodaram **3 coletores somente-consulta**; a escrita continuou
  minha, via `scripts/inject-produto.ps1` (novo), em **3 lotes na ordem Notion → especificação
  canônica → briefing do Vinicius**, deixando o briefing por último de propósito para vencer em caso
  de conflito. **123 campos gravados; 16 de 16 conformes ao template por diff de headings.**
  **✅ O achado da sessão — `EnriqueceAI` × `CadastrAI` × `CadastroAI` eram três coisas, não três
  grafias.** A Especificação por Módulo V1 diz literalmente: "No desenho original era 'CadastroAI'
  como módulo de enriquecimento. Foi rebatizado para EnriqueceAI durante esta sessão para liberar o
  nome 'CadastrAI' para o núcleo de governança." Logo: **EnriqueceAI = antigo CadastroAI**, e
  **CadastrAI = núcleo de governança**, item novo que herdou o nome liberado. A hipótese que o
  Vinicius levantou ("EnriqueceAI substituiu o CadastrAI, é a mesma coisa com nome novo") estava
  **meio certa** — houve renomeação, mas não é o mesmo item que o CadastrAI de hoje. Isso fechou de
  uma vez a pendência de grafia `CadastroAI` × `CadastrAI`: **não era grafia, eram duas entidades em
  momentos diferentes.** Nenhum item foi fundido. Também fechou a grafia `FornecAI` × `ForneceAI`:
  a fonte canônica é inconsistente **consigo mesma** (cabeçalho "ForneceAI", corpo "FornecAI"), e o
  ÍNDICE MESTRE grafa `FornecAI`, igual a `CONTEXT.md`.
  **Governança fechada:** decisão do Vinicius de que **no BrainHub somente o CEO (João Risoléo)
  altera** — ele está alterando tudo agora porque está construindo, exceção declarada de construção.
  Aplicado nos 16: o campo `Quem pode alterar este documento` saiu de **15 vazios para zero**.
  **Maturidade: 6 scores novos e 2 mudanças que precisam de ratificação.** Novos: CadastrAI
  `Escalável` (ÍNDICE MESTRE: "produto em produção", âncoras Luiza Barcelos e Reserva), ONB HUB
  `Escalável`, Gest Hub `MVP`, Sales Hub `Ideação`. Mudanças: **GerenciAI `Ideação` → `Escalável`**
  (a V1 diz "o módulo que a Reserva já usa hoje" — a avaliação anterior classificou pela visão
  futura, que a própria página marca como brainstorm) e **Taxonomia `Escalável` → `MVP`** (nenhuma
  fonte declara produção; 1.820 dos 2.618 clusters ainda em revisão humana — a avaliação anterior
  confundiu importância transversal com maturidade). Restam 2 `[a preencher]`: **AlocAI** e
  **IntHub**, e por motivo real — não há fonte.
  **O que a leitura revelou de estrutural:** as fontes desenham **8 peças** (6 módulos + CadastrAI +
  Hub de Agentes), não 16; o Domínio 3 do ÍNDICE MESTRE tem só **4 projetos**; **3 Soluções não têm
  nenhuma fonte** (AlocAI, VendeAI, CliprocAI); **IntHub aparece uma única vez** em tudo que foi
  lido; existem **duas taxonomias** de abril/2026 que nunca se citam (a do PLM, 2.618 clusters, PO
  João Risoléo — e o **TaxonomyAI**, serviço com 431 valores baseado em Fashionpedia + Shopify,
  responsável João Ferraz); e o Hub de Agentes tem **16 agentes**, número que **não tem relação
  nenhuma com as 16 Soluções** — coincidência registrada de propósito.
  **⚠ Divergência que não fundi:** o Vinicius descreveu o Hub de Agentes como plataforma para o
  cliente construir o próprio BrainHub, no novo modelo de mentoria e educação. O Plano Técnico de
  abr/2026 **não diz nada disso** — descreve consolidação interna de agentes espalhados por 5
  produtos. Podem ser fases diferentes da mesma coisa; ficaram registradas como duas leituras.
  **6ª fonte de "quem é cliente":** a base legada da Taxonomia (101 fichas, 83 ativas). Cruzada com
  nossos 46: 24 casam, **~12 nomes sem casa** — e **`Sinbi` tem "dezenas de submarcas"**, que é a
  prova concreta da dívida de não existir entidade "conta/instância". Importar essa base agora
  criaria 30+ casas espúrias.
  **Descoberta de fonte inalcançável:** o ÍNDICE MESTRE avisa que **`uMode-OS` é uma pasta local no
  Mac do João**, com `MANIFEST.md` e um **crosswalk repositório ↔ produto** — exatamente o mapa que
  resolveria duas dívidas nossas. Nenhum agente remoto acessa. Enquanto isso, o cérebro depende de
  uma pasta em uma máquina. Também definido ali: as camadas **T2 / T1 / T0** de privacidade — o que
  esclarece a etiqueta "T1" da fonte da Cambos, mas **não** a autorização de uso.
  **Correção de entendimento meu:** a página que eu chamava de "Arquitetura & Tese" **não é o
  documento de arquitetura** — é uma ficha de skill com só as headlines. O documento real é a
  "Especificação por Módulo (V1 — sessão 24/04/2026)".
  **Registrado:** pendências 63 a 82 (63 e 64 já fechadas), seção **4-B** nova no
  `_backlog-infra-tecnologia.md` com as 12 obras que o Hub de Agentes exige, e a dívida 3.1
  atualizada de 5 para 6 fontes de cliente.

- **04 ago 2026** — Sessão 25 (fecho 11): **PRIORIDADE ZERO declarada + os 4 repositórios novos lidos
  (CX Hub, IntHub, AlocAI e o BrainHub do João).** Vinicius declarou a primeira **entrega** do
  BrainHub — um agente de suporte técnico da uFlow para a operação — formalizada em
  [`D-2026-002`](uMode/00_Institucional/_demandas/D-2026-002.md), conforme ao template, com o papel
  inteiro (`Papel de Suporte.txt`) registrado e 5 subdemandas identificadas. Bloco `🔴 PRIORIDADE
  ZERO` novo no topo deste arquivo, acima do rolo compressor. Também travou a governança (somente o
  CEO altera) e esclareceu que **todos os repositórios de integração são da uFlow**, com a regra
  "ter a ferramenta ≠ ter integração" — gravada em `protocolo-gestao-integracao.md`, junto da
  consequência de que aqueles 11 `integracao.md` são hoje a nossa melhor fonte indireta sobre a
  própria uFlow.
  **🚧 O bloqueio da Prioridade Zero e quem o resolve.** Não temos o repositório da plataforma uFlow
  (nenhum projeto Ruby/Rails no disco, e o papel pede "comandos Rails Console"), nem o schema do banco
  dela — os repositórios de integração documentam as tabelas do **ERP do cliente**, nunca as da uFlow.
  **A leitura do IntHub deu o nome de quem destrava: `Bergson`, Squad Legado, marcado literalmente
  "(SPOF crítico)", responsável pela manutenção e pelo descomissionamento da uFlow.**
  **E a taxonomia que o agente precisa já existe e a operação já usa** (travada por ADR no IntHub):
  `Client` · `Process` · `Engineering` · `Nao_Classificado`, com responsável `Parceiro`/`uMode`/
  `Indefinido`. É exatamente o "é configuração, é tech, ou é erro de dado" — não precisa ser inventado.
  **✅ CX Hub: hierarquia confirmada, com duas correções.** `programs → program_milestones` +
  `projects` (nullable) → `demands` (3 FKs nullable) → `demand_tasks`. **"Subdemanda" é
  `demand_tasks`, não demanda-filha** — o que **valida o nosso modelo**, que já a trata como checklist
  no mesmo card. No domínio de Programas o vocabulário muda: projetos são "features", demandas são
  "sub-itens". E **`demands` não tem coluna de status** — o estado é `column_id` + `finished_at` +
  `cancellation_reason` + `is_blocked`, com status derivado em RPC. **Isso explica retroativamente o
  conflito Status × Etapa que encontramos no dado legado.**
  **✅ Os enums reais chegaram, e fecham lacunas antigas:** `demand_priority` tem **`low`** (fecha a
  lacuna "Prioridade sem equivalente para Baixa"), com SLA por prioridade (2h/4h/8h/24h);
  `blocker_types` tem **5 valores reais** e o nosso enum acerta 4 — falta **`Aguardando cliente`** e
  temos um `Outra` que não existe no catálogo; `rfi_statuses` são **`Previsto`/`Orçada`/`Aceito`/
  `Recusada`**, que **divergem por completo** dos status de RFI que traduzimos do legado; e há um campo
  `delay_reason` com 7 valores que nós não temos. **🔴 E a explicação definitiva do eixo de Área
  vazio: `ticket_columns` e `demand_areas` NÃO TÊM SEED** — são configuráveis em Settings e o código
  evita nomes fixos de propósito ("No hardcoded names or positions"). **Não existe fonte documental
  para o enum de Área do CX Hub; ele vive só no banco de produção.**
  **⚠ Duas correções de premissa nossa:** (1) a **RFI do CX Hub** tem CHECK XOR — pertence a uma
  Demanda **ou** a um Projeto, então **existe RFI sem demanda nenhuma**, caso que o nosso modelo (RFI
  dentro da Demanda) não representa. (2) o nosso campo `ID legado (Notion/CX Hub)` **conflaciona dois
  sistemas**: numa amostra de 400 demandas, **399 têm formato `UMD-N`, que é ID do Notion**, e o código
  do CX Hub é `PREFIXO-NNNN` (`BUG-0042`, `SUP-0113`). `UMD-970` não resolve para nada no CX Hub.
  **🔴 Não existe API para criar demanda no CX Hub, e não existe idempotência.** Nenhuma Edge Function
  faz INSERT em `demands`; o único caminho é PostgREST com JWT de usuário. **Sem `external_id`, sem
  UNIQUE de dedup, sem `ON CONFLICT`: reenviar o mesmo POST cria uma segunda demanda.** As duas coisas
  precisam ser construídas antes de qualquer automação BrainHub → CX Hub.
  **🔴 O vault do João usa a NOSSA estrutura exata, e tem dois arquivos de taxonomia que não temos:**
  `BrainHub/uMode/00_Institucional/_contexto/TAXONOMIA_UMODE.md` (8.356 palavras, 212 headings) e
  `BrainHub/uMode/04_Dados-e-IA/taxonomia-atributos/GRUPOS_ATRIBUTOS_UMODE.md` (8.765 palavras).
  `00_Institucional/_contexto/` e `04_Dados-e-IA` são precisamente os nomes das nossas pastas.
  **Hipótese forte, não confirmada: é esta a "outra fonte rica de informações institucionais" da fase
  de reprocessamento.** Também lá: um registro numerado de decisões **D13 → D51** (`DECISOES.md`) e um
  `_GOVERNANCA.md` cuja regra é declarada no código — "em conflito, a governança do vault vence".
  O repositório dele **é** um BrainHub Console (18 rotas, 30 tabelas); `design-system-hub` é resíduo
  de nome do Lovable. E **não integra fonte externa nenhuma** — zero Notion, zero Drive em 167
  arquivos e 211 commits: um agente local chamado **Hermes** lê as fontes e empurra para lá.
  **Achado cruzado que nenhum dos dois lados conhece:** o IntHub monitora
  `jumper_integration_executions` do MySQL legado e depende de uma tabela de tradução manual
  (`legacy_entity_map`) que tem **1 linha**; **os nossos `integracao.md` carregam os `INTEGRATION_ID`
  5, 21, 22 e 25**, e o da VIX cita a tabela nominalmente. Registrado como achado, não como ação.
  **Incidentes reais que validam a nossa cautela:** no BrainHub do João, a trava de sensibilidade
  "era decorativa" e **"o primeiro T1 aprovado (valor de contrato Malwee, CNPJ + receita de cliente)
  teria vazado para a chave pública"** — 47 de 53 linhas passavam. No CX Hub, `CTX4`: DELETE em massa
  de `interactions` **sem** o filtro obrigatório `auto_created`, marcado como "EXECUTADO (lição)". E
  `RISC-001`, aberto: **senhas de ERP de cliente em YAML texto plano** em 24 linhas do uFlow.
  **Registrado:** pendências **91 a 135**; seção de segurança e as dívidas novas em
  `_backlog-infra-tecnologia.md`. **Nota sobre nós:** `_pendencias-gerais.md` chegou a **17.180
  palavras** — passaria como crítico pelo threshold de 8.000 do próprio auditor de MD do Hermes. Está
  pedindo a triagem por dono que já foi prevista e nunca feita.

- **04 ago 2026** — Sessão 25 (fecho 12): **PRIORIDADE ZERO desbloqueada — repositório e schema da
  uFlow recebidos e mapeados; o agente ganhou base real.** Vinicius entregou o clone da plataforma, e
  a leitura produziu dois documentos novos em `uMode/04_Dados-e-IA/_contexto/`:
  **`agente-suporte-uflow.md`** (o contrato de comportamento do agente, preservado porque os arquivos
  de origem saíram do disco) e **`uflow-modelo-de-dados.md`** (o mapa do banco: 211 tabelas, domínios,
  tabelas centrais, multi-tenant, integrações, auditoria e 20+ armadilhas).
  **A correção mais consequente que a leitura produziu:** a fonte de treinamento diz "prefixo de
  tabela geralmente `umode_...`" — e no schema real **`umode_` é 119 de 211 tabelas (56%)**, enquanto
  **`jumper_` são 63 e formam o núcleo da plataforma** (tenant, usuário, política, workflow,
  integração). **Não existe nenhuma tabela `j3_`** — `J3` é só namespace Ruby que resolve para
  `jumper_`. **Um agente que assumir `umode_` erra em 44% do banco.** Correção aplicada no nosso
  arquivo; a fonte original não foi alterada.
  **Descoberta de linhagem:** a uFlow é a **reescrita de um app PHP/Laravel chamado "Jumper"** — as 63
  tabelas `jumper_*` são o núcleo herdado, e sobraram `laravel_jobs`, `migrations` e `sessions`,
  mortas. **Isso liga duas fontes que não se conheciam:** a página "Taxonomia" do Notion documenta
  "Actions do Jumper (legado uFlow)" com anexo `JUMPER_ACTIONS.txt`. **"Jumper" é o legado dentro do
  legado**, e nada disso está no `README.md` da plataforma.
  **✅ Circuito de integração fechado.** A uFlow expõe `POST`/`PATCH /api/v1/integration-executions`.
  Os 10 repositórios de integração são **Lambdas externas que gravam ali por HTTP**, e o
  `INTEGRATION_ID` que documentamos (5 NV · 21 Baw · 22 Lofty · 25 Luiza Barcelos) é o
  `jumper_integrations.id`. Fluxo: **Lambda → API da uFlow → `jumper_integration_executions` →
  polling do IntHub**. Confirmação lateral: dentro da uFlow só existem runners **Millenium** — Linx,
  SAP, SPI e Safe Tech vivem só nas Lambdas. **Isto converte o item 105 de hipótese em mecanismo.**
  **🔴 Três achados que limitam o que o agente pode prometer:** (a) **`db/schema.rb` não é a fonte de
  verdade completa** — faltam 4 tabelas, entre elas **`jumper_policies`**, a tabela de permissão da
  plataforma, e 6 das 8 views; um `db:schema:load` produz aplicação que não sobe. (b) **58% das
  tabelas não têm `entity_id`** — sem RLS, sem schema-per-tenant: o isolamento entre clientes depende
  da aplicação, e subsistemas inteiros (todo o kanban, todo o custo, os 26 pivots) só resolvem tenant
  por JOIN. (c) **"Lacre" não existe no banco** — é convenção de nome de custom field
  (`lacre_checklist`, `data_lacre_checklist`) acordada por cliente, e o `produto.md` do DesenvolvAI
  descreve o módulo como "croqui → lacre". A etapa central do nosso vocabulário **não é entidade de
  dados**; um cliente que renomeie o campo quebra o relatório.
  **Outras armadilhas que valem para qualquer métrica que a gente extraia da uFlow:** `umode_products`
  é **STI** e guarda também `PurchaseOrder`, `ProductBundle` e `ProductTemplate` — contar produto sem
  filtrar `type` infla o número; **dinheiro é `float`** (`value_cents` é `t.float`, sem `money-rails`),
  então todo custo carrega erro de ponto flutuante; **`integration_id` é dois campos com o mesmo
  nome** (FK numa tabela, string de de-dup externa em 18 outras, nenhuma indexada); e
  **`jumper_entity_configs.deleted_at` é `t.string`**, a única do schema, justamente na tabela que
  controla o comportamento por cliente.
  **Segurança:** confirmado no schema que **`jumper_integrations.properties` (YAML) guarda as
  credenciais de ERP de cada cliente** — o `RISC-001` do IntHub agora tem duas fontes independentes.
  Mais `jumper_entities.api_token` sem hash e duas colunas de senha em `jumper_users`. Tudo em
  `_backlog-infra-tecnologia.md`, **seção 4-C** nova, com 12 itens.
  **⚠ Interrompido por limite de crédito da organização:** a varredura que enumeraria **todas as
  `EntityConfig` do código** morreu antes de produzir resultado. É **a lacuna de maior valor que
  resta** — enumerar as configs é enumerar onde o comportamento muda por cliente. A única conhecida
  por nome continua sendo `product_manufacturer_supplier_status` (Osklen, `entity_id = 3580`).
  **Registrado:** pendências **136 a 152**.
