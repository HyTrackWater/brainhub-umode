# Backlog de infra de tecnologia — o que precisará ser construído

> **Nada aqui é para desenvolver agora.** Pedido do Vinicius em 03 ago 2026: começar a **rastrear e
> mapear** tudo que exigirá intervenção de infra de tecnologia, para que a equipe tech receba a lista
> pronta quando for a hora. Motivo declarado: *"teremos vários agentes que deverão beber diretamente
> da fonte dos repositórios para operacionalizar"*.
>
> Regra deste documento: cada item diz **o que existe hoje**, **o que falta** e **qual é a
> intervenção de tech** — nessa ordem. Item sem limite medido de verdade é marcado como hipótese.
> Vários itens abaixo vêm de limites que **bateram na prática** durante as sessões, não de suposição.

---

## 1. Acesso programático às fontes (é isso que os agentes vão "beber")

Hoje **todo** acesso a fonte externa é feito por MCP autenticado **como pessoa física** (a conta do
Vinicius). Isso funciona para uma sessão de trabalho assistida e **não funciona para agente
autônomo**: o agente herdaria a identidade e as permissões de uma pessoa, sem rastreabilidade nem
revogação independente.

### 1.1 Notion — a fonte de verdade canônica
- **Hoje:** MCP conectado ao workspace `uMode Mode's Notion` como `vinicius.risoleo@umode.com.br`.
- **Falta:** integração própria (token de integração / service account) com escopo mínimo, e
  compartilhamento explícito das bases com essa integração.
- **Bases que os agentes vão precisar** (IDs já levantados):
  | Base | ID | Uso previsto |
  |---|---|---|
  | Demandas de Clientes | `ddf1951a-8dc2-42e6-98e6-bae3d1f5a865` (data source `ae2c893a-903e-4f10-962d-c6ad1e52c47b`) | sincronizar demanda + narrativa |
  | RFI Escopo | `24fb1d38-e768-8011-b212-000bf0cd960d` | sincronizar RFI |
  | Clientes | `ec041afd-fcee-44f8-83cb-223fca6f4108` | lista mestra de cliente |
  | Projetos | `241b1d38-e768-80cd-9213-000b0dbeb621` | fase/projeto por cliente |
  | Arquitetura uMode V1 (página) | `34db1d38e768814b8001d7cb6cacf4e5` | contexto de produto |
- **⚠ Limite medido, e é o mais importante deste documento:** o **corpo da página não vem em
  consulta de base**. A coluna `Texto` vem preenchida em **2 de 1.010** registros; o conteúdo real
  vive nos blocos da página e só sai com um `fetch` **por página**. Medido em 03 ago 2026: ~2,5 KB de
  resposta por demanda, e ~60% das páginas têm corpo. Para as 887 demandas sem narrativa isso é
  **887 chamadas**. **Intervenção de tech:** um **job de sincronização incremental** (não leitura sob
  demanda), que percorra as páginas em lote, guarde o conteúdo, e nas execuções seguintes só busque o
  que mudou — usando `Última edição` como marca-d'água. Sem isso, qualquer agente que precise da
  narrativa vai ser lento e caro.

### 1.2 Google Drive
- **Hoje:** MCP com a conta do Vinicius. Já foi usado para CRM, bases de demanda/RFI/reuniões,
  planilha de acessos, PRDs e documentos de arquitetura.
- **Falta:** service account + escopo, e decisão sobre quais pastas ficam visíveis para agente.
- **⚠ Limite medido:** a leitura falha em arquivo grande — a planilha "uMode - Controle de Acessos"
  (188 KB de texto) e o CRM (59 KB) **estourаram** o limite de resposta e tiveram de ser processados
  em disco. **Intervenção de tech:** paginação/streaming na camada de leitura, ou export programado
  para um bucket que o agente leia direto.

### 1.3 Repositórios de integração por cliente
- **Hoje:** 10 repositórios clonados por Vinicius em `C:\Ambientes Virtuais\uMode-Integracoes`, lidos
  em 03 ago 2026. **9 têm documentação** (`documentacao-geral-*.md` + `tabelas-do-linx-*.md`, 30 a
  77 KB cada); `unico-linx` (Puket) tem código e nenhum `.md`. O acesso é **só desta máquina**.
- **Falta:** para agente, acesso ao repositório sem depender da máquina de ninguém. Hoje o conteúdo
  técnico só entrou no cérebro porque uma pessoa clonou os repositórios num caminho local.
- **Intervenção de tech:** GitHub App ou deploy key de leitura por repositório, e uma **convenção de
  caminho canônico** para o clone (pasta-mãe única). Decidir também se o agente lê do clone local, de
  um mirror, ou da API do GitHub.
- **Insumo novo:** o mapeamento repositório → cliente **não é inferível pelo nome** (`arzz-sap` é
  Reserva/Oficina, não Arezzo; `unico-linx` é Puket). A tabela autoritativa está em
  `protocolo-gestao-integracao.md` e qualquer automação tem que consumi-la, não adivinhar. Os riscos
  técnicos que a leitura revelou estão na seção 4.

### 1.4 CX Hub — o destino operacional das demandas
- **Hoje:** o vínculo Demanda → card no CX Hub é **manual**. `protocolo-gestao-demanda.md` já registra
  a automação como fora de escopo.
- **Falta:** contratos de API do CX Hub (`gist-sparkle`): autenticação, criação de card, campos
  obrigatórios, idempotência (não criar card duplicado se o agente repetir).
- **Intervenção de tech:** expor API de criação/consulta de card + um identificador de origem
  (`brainhub_demanda_id`) para fechar o ciclo dos dois lados. É o que destrava o agente de card
  pós-aprovação já previsto.

### 1.5 Plataforma uMode (uFlow e demais módulos)
- **Hoje:** o dado de uso/engajamento por cliente só existe como **planilha mantida à mão**
  ("uMode - Controle de Acessos"): usuários por conta, acessos no mês, perfis de acesso.
- **Falta:** API que devolva o mesmo dado (usuários, perfis, último acesso, por organização).
- **Intervenção de tech:** endpoint de telemetria/adoção por organização. É a única fonte de **saúde
  de conta** que existe, e hoje depende de alguém atualizar uma planilha.

### 1.6 Linear
- **Hoje:** aparece como fonte conectada ao Notion (achado em 03 ago 2026). O nosso modelo de RFI
  **descartou** `Task (Linear)` por decisão registrada.
- **Falta:** decidir se volta ao fluxo. Se voltar, precisa de acesso próprio.
- **Intervenção de tech:** nenhuma por enquanto — item de decisão, não de construção.

### 1.7 Outras fontes já citadas nos MDs e sem acesso programático
Portal do Cliente, base de chamados, grupos de WhatsApp oficiais, planilhas de OKR por cliente,
materiais de apresentação — todos hoje são **link em campo de texto** dentro de `institucional.md →
Sistemas e fontes de verdade → Outras fontes`. Se agente precisar ler, cada um vira um conector.

---

## 2. O que precisa ser construído para o cérebro funcionar como cérebro

### 2.1 Job de sincronização fonte → MD
- **Hoje:** tudo é lote manual, rodado por script PowerShell na máquina do Vinicius
  (`gen-clientes-crm.ps1`, `gen-demandas.ps1`, `gen-rfis.ps1`, `inject-narrativa-notion.ps1`).
- **Falta:** execução agendada e idempotente, fora de máquina pessoal.
- **Intervenção de tech:** runner (CI ou serviço) com credencial própria, log de execução, e política
  de conflito quando a fonte e o MD divergirem. **Atenção:** o ciclo de aprovação já está modelado em
  `protocolo-gestao-demanda.md` ("nenhum agente escreve contexto sem aprovação registrada como
  marco") — a implementação precisa respeitar isso, não contorná-lo.

### 2.2 Índice derivado consultável
- **Hoje:** `_indice/` com 5 tabelas CSV (clientes, demandas, rfis, produtos, pessoas), geradas por
  `scripts/gen-indice.ps1` a partir dos MDs. Funciona e já responde consulta relacional.
- **Falta:** rodar em servidor, e uma camada de consulta que não seja "abrir CSV".
- **Intervenção de tech:** materializar o índice em banco (ou em um endpoint de consulta) e
  regenerá-lo a cada sincronização. Decisão de arquitetura já registrada: **o MD é a fonte de
  verdade, o índice é derivado** — nunca o inverso.

### 2.3 Busca semântica / RAG sobre o cérebro
- **Hoje:** não existe. A auditoria de 03 ago 2026 mostrou que a indexação funciona por convenção de
  heading (100% dos arquivos conformes), o que é bom sinal: o conteúdo é parseável.
- **Falta:** embeddings + recuperação por escopo (por Área, por Cliente, por Solução — as 4 classes
  de agente já desenhadas em `brainwave/CONTEXTO.md`).
- **Intervenção de tech:** pipeline de indexação vetorial com **respeito ao escopo/permissão** (um
  agente Por Cliente não pode recuperar contexto de outro cliente — isolamento é regra travada em
  `CONTEXT.md`).

### 2.4 Migração estrutura de pastas → banco de dados
- **Hoje:** a estrutura de pastas **é** o schema (decisão travada em `CONTEXT.md`). Já no backlog.
- **Novo insumo (03 ago 2026):** `client_id` foi travado como chave estável — é o candidato natural a
  chave primária, e nome de campo em inglês já é padrão travado.
- **Intervenção de tech:** modelagem relacional a partir dos templates (que já são o schema de fato)
  + plano de migração sem perder o histórico de `Marcos` (append-only).

### 2.5 Formulários de coleta de dado
- **Hoje:** frente pausada (registrada na Sessão 24). ~19% das linhas dos MDs são `[a preencher]`.
- **Falta:** backend que receba o formulário e **escreva no MD** (ou abra PR), respeitando o ciclo de
  aprovação.
- **Intervenção de tech:** endpoint de escrita + autenticação por pessoa + trilha de auditoria.

### 2.6 Agentes já previstos e o que cada um exige de infra
| Agente previsto | Onde foi registrado | Exige de infra |
|---|---|---|
| Transcrição de reunião → Demanda/Conversas | Sessão 24 | ingestão de áudio/transcrição, e decisão de onde a transcrição vive na hierarquia |
| Criação de card no CX Hub pós-aprovação | Sessão 24 | item 1.4 (API do CX Hub) |
| Agente Por Área / Por Cliente / Por Solução | `brainwave/CONTEXTO.md` | item 2.3 (RAG com escopo) |
| Agente de "conferência" que abre demanda sozinho | `protocolo-gestao-demanda.md` | escrita em MD + registro de Marco (item 2.1) |
| `product-analyzer`, `tryon-stylist`, `audio-transcriber`, `product-enricher` | Arquitetura uMode V1 (Notion) | **já existem** — são do Hub de Agentes, não deste projeto; mapear a fronteira entre Hub de Agentes e agentes do BrainHub |

---

## 3. Dívidas de dado que exigem decisão ou correção na origem

Estas não são "construir sistema", são "arrumar dado ou enum na ferramenta". Todas medidas.

| # | Dívida | Onde dói | Intervenção |
|---|---|---|---|
| 3.1 | **6 fontes diferentes de "quem é cliente"**: CRM (46), pasta Drive "Clientes" (+9 nomes), planilha de acessos (+18 organizações), base de Clientes do Notion, repositórios de integração, e — descoberta em 04 ago 2026 — a **base legada da Taxonomia (101 fichas, 83 ativas)**, que traz ~12 nomes sem casa nenhuma (`Lojas Nalin`, `Puket Tecidoteca`, `Basico.co`, `Beira Rio`, `Dakota`, `Grendene`, `Lojas Estrela`, `Minimal`, `Mondepars`, `Sinbi`, `Via Marte`, `Tempo de Criança`) | qualquer importação futura duplica ou perde cliente | eleger fonte mestra e usar `client_id` como chave de reconciliação |
| 3.2b | **`Sinbi` tem "dezenas de submarcas" sob ela** (base legada da Taxonomia) e `Puket Tecidoteca` sugere mais de uma ficha por operação do mesmo cliente | é a prova concreta da dívida 3.2: não existe entidade "conta/instância" entre Cliente e Solução | modelar a entidade antes de importar essa base — importar agora criaria 30+ casas espúrias ou perderia as submarcas |
| 3.2 | **Conta-por-módulo na plataforma** (`Cambos` + `Cambos - uFlow`; `Tempo de Criança (uRocket)`; `Studio Z <> SalesForce`) | não existe entidade "conta/instância" entre Cliente e Solução | modelar (provavelmente junto da entidade "Solução × Cliente" já prevista) e expor o identificador da conta na API |
| 3.3 | **`RFI.Demanda relacionada` aponta para nome de cliente, não para ID de demanda** | 0 de 85 RFIs resolvem para `D-AAAA-NNN` | corrigir na origem (Notion) ou aceitar reconciliação manual RFI a RFI |
| 3.4 | **Enums nossos incompletos vs. a ferramenta**: `Motivo de bloqueio` (a fonte tem 8 valores, nosso enum cobre 1), `Prioridade` sem equivalente para `Baixa`, `Status` de cliente com `Regime CS`/`Negociação` fora do enum | tradução legado→padrão força `Outra`/`[a preencher]` | decidir o enum canônico; se o certo for o da ferramenta, ajustar nossos templates |
| 3.5 | **`Área Responsável = INOVAÇÃO / IA` sem correspondência** no enum de Área (CX Hub) | 4+ demandas com Quadro/Área em branco | criar o valor no CX Hub ou definir o mapeamento |
| 3.6 | **10 demandas sem cliente** e **1 RFI sem cliente** na base | não há casa onde viver; a RFI contradiz a premissa "RFI sempre tem cliente" | corrigir cadastro na origem, ou aceitar demanda/RFI interna e mudar o protocolo |
| 3.7 | **Imagens das narrativas vivem fora do Notion** — os anexos apontam para URLs do Discord e do Gmail (com token de expiração no link) | a narrativa preservada perde a imagem quando o link expirar | ingestão de anexo para armazenamento próprio, se o conteúdo importar |
| 3.8 | **Grafia divergente na fonte canônica**: `ForneceAI` (Notion) × `FornecAI` (nosso Portfólio) | nome de produto | decidir a grafia oficial |

---

## 4. Riscos técnicos observados na documentação dos repositórios de integração

Levantados em 03 ago 2026 na leitura dos 9 `documentacao-geral-*.md`. **Nada aqui é diagnóstico
meu sobre o código** — cada linha está escrita no documento do próprio repositório, muitas vezes
pelo autor da integração como ponto conhecido. Não são dívidas de dado (seção 3): são
comportamentos de sistema em produção que a equipe tech precisa decidir se aceita.

| # | Risco | Onde | Por que importa |
|---|---|---|---|
| 4.1 | **A integração da Cambos não envia autenticação nenhuma ao SPI** — sem header `Authorization`, sem token, sem `api_token`. O documento registra isso explicitamente como o ponto de risco mais relevante do repositório | Cambos | escrita de produto num ERP de cliente sem credencial; é o item mais grave da lista |
| 4.2 | **`silent_error` nunca é limpo no sucesso** | Baw, Cambos, NV, Lofty Style | produto integrado "sem erro" pode carregar falha silenciosa antiga; qualquer painel que leia esse campo mente |
| 4.3 | **Produto de terceiro é marcado como integrado para sair da fila** — quando a propriedade `00209` (ID uMode) não confere, o erro é `This product was not created by uMode` e o produto é marcado como integrado. Workaround explícito no documento | NV | esconde permanentemente um caso de colisão de identidade entre uMode e Linx |
| 4.4 | **Erro de `PROP_PRODUTOS` se autoanula**: o campo de erro é preenchido, sobrescrito pela etapa seguinte e depois limpo — o produto termina sem erro e sem data de integração, e volta à fila a cada 30 min, para sempre | NV | consumo de execução em loop invisível; nenhum alerta dispara |
| 4.5 | **Casamento de fornecedor por nome, não por código** | Baw, Lofty Style, Osklen | renomear o fornecedor no Linx cria duplicidade na uFlow |
| 4.6 | **Erro em um item derruba o lote inteiro na leitura de grades** (as outras leituras pulam o item e seguem) | Baw, Osklen | uma grade ruim bloqueia todas as grades do dia |
| 4.7 | **Parse monetário pt-BR remove pontos** — um valor como `12.50` viraria `1250` | Osklen | erro de 100× em custo, sem validação |
| 4.8 | **`idcliente` convertido sem validação, pode virar `NaN`** | Cambos | grava lixo no ERP em vez de falhar |
| 4.9 | **Dois pontos marcados pelo próprio autor como "pendente de validação"**: `MATERIAL`/`COR_MATERIAL` de `PRODUTO_CORES` hardcoded em `'30.02.0053'`/`'0158'` sobrescrevendo o cálculo anterior (código morto); e rota de operações gravada só no 2º registro da rota-modelo, cuja query **não tem `ORDER BY`** | NV | comportamento que depende da ordem que o banco devolver |
| 4.10 | **Cliente altera infraestrutura sem aviso prévio** — 4 incidentes em 6 semanas (host, share, domínio AD, credencial, VPN, usuário de banco). Único cliente com relatório formal de incidente | VIX | não é problema de código; é acordo de comunicação e janela de homologação |
| 4.11 | **`umode-microservice-uconnect` (interceptor) é componente compartilhado da uMode**, não ativo de cliente: intermedia Baw, Lofty Style e Osklen, mantém o snapshot MongoDB, gera referência de produto, injeta contas contábeis e roda o cron de auditoria | Baw, Lofty Style, Osklen | **não está no Portfólio de Soluções.** Um componente que gera referência de produto e injeta conta contábil é regra de negócio, não encanamento — precisa de dono e de ficha |
| 4.12 | **Leitura não é ao vivo onde passa pelo interceptor**: responde de snapshot MongoDB gerado ~20:00 BRT, e os crons de leitura rodam de manhã — defasagem de até ~10h | Baw, Lofty Style, Osklen | ninguém que consome esses cadastros sabe que está lendo a foto de ontem |
| 4.13 | **Documento-fonte incompleto**: o sumário anuncia as seções 10 (comportamentos frágeis/bugs latentes) e 11 (pontos que precisam de validação), a numeração salta de 9.1 para 9.4, e esses trechos não existem no corpo do arquivo | Reserva / Oficina Reserva | justamente as duas seções de risco faltam, na integração mais antiga e legada da carteira |
| 4.14 | **Repositório em produção com zero documentação**: `unico-linx` tem código e **nenhum arquivo `.md`** | Puket | não é lacuna nossa de preenchimento — é integração ativa sem documento algum |
| 4.15 | **Código de barras desativado com a lógica ainda no repositório** | Baw, Lofty Style, NK STORE | NK, se reativado, buscaria GTIN-13 na **API externa da GS1** (hoje não chamada em produção) — dependência externa adormecida |

---

## 4-B. Hub de Agentes — a maior obra de infra já especificada, e ainda não começada

Levantado em 04 ago 2026 na leitura do "Plano Técnico — Hub de Agentes + Infraestrutura uMode"
(Notion `340b1d38e768811fab17ca211fda8ef3`, v3.0 abr/2026). Ao contrário do resto deste documento,
aqui **a especificação já existe e é detalhada** — o que falta é execução. Registrado porque é a
peça que os agentes do BrainHub vão encontrar no caminho.

**Estado real:** não começou. O próximo passo declarado é "criar o projeto Lovable separado
manualmente", e as **9 caixas do checklist de segurança estão todas desmarcadas** — inclusive
"proxy reverso `api.umode.tech` no ar antes de qualquer outro passo". Estimativa dos sprints:
2–3 semanas (S1) + 1–2 (S2) + 1–2 (S3) + 3–4 (S4), com risco Baixo/Médio/Médio/Alto.

**Por que existe (4 problemas nomeados pela própria página):** exposição (usuários veem chamadas a
Supabase, Gemini e Claude no DevTools), isolamento (cada produto reimplementa a mesma lógica de
agentes), gestão manual (o operador é o único mensageiro entre ferramentas) e hardcode (modelos e
personas fixos no código).

| # | O que precisa ser construído | Detalhe da especificação |
|---|---|---|
| 4B.1 | **Projeto Lovable separado + Lovable Cloud** | passo manual, pré-requisito de todo o resto |
| 4B.2 | **Instância Supabase dedicada** ao Hub | banco + edge functions + storage + auth |
| 4B.3 | **6 edge functions** | `get-agent`, `run-inference`, `log-feedback`, `arena-run`, `analyze-agent-performance`, mais os shared `auth-guard.ts` e `ai-providers.ts` |
| 4B.4 | **Schema do Hub** | `ai_agents`, `ai_agent_documents`, `ai_model_catalog`, `ai_agent_model_config` (UNIQUE organization_id+agent_slug+task_type), `ai_prompt_log`, `ai_agent_performance` + tabelas core migradas do CriAI (`organizations`, `profiles`, `user_roles`, `admin_agent_templates`, `org_brand_profiles`) |
| 4B.5 | **Proxy reverso `api.umode.tech`** | requisito de segurança: o DevTools deve mostrar só esse host, nunca `supabase.co` nem fornecedor de IA; `sourcemap: false` em produção em todos os projetos |
| 4B.6 | **Regra de chamada entre sistemas** | sempre edge function → edge function, nunca do frontend; `service_role` key do Hub como secret em cada módulo |
| 4B.7 | **Abstração de provedor de IA com fallback** | `ai-providers.ts` cobrindo Google Gemini, Google Vertex, OpenAI ("via gateway") e Anthropic; hoje o fallback Gemini→Claude está **inline no CX Hub** |
| 4B.8 | **RLS + multi-tenancy por `organization_id`** | em todas as tabelas do Hub — mas ver a regra de tenancy abaixo |
| 4B.9 | **Observabilidade e custo por chamada** | `cost_per_1k_input`/`output` no catálogo, `estimated_cost_usd` + `latency_ms` + rating + `feedback_tags` no log, dashboard `/performance` |
| 4B.10 | **Retenção LGPD** | máximo de 90 dias no `ai_prompt_log` |
| 4B.11 | **Migração de dados e "modo duplo"** | `ai_calibrations` (CadastrAI) → `ai_agents`; personas hardcoded do CriAI (`useAgents.ts`) e system prompts do CX Hub/ONB HUB → banco; fallback local por 2–3 semanas durante a Fase 1 |
| 4B.12 | **CORS restrito e auth-guard no ONB HUB** | a página registra que hoje **não tem** |

**Regra de tenancy confirmada (ÍNDICE MESTRE, 28/05/2026), que muda o desenho:**
`organization_id`/multi-tenancy só em produtos **comerciais**; os internos (**Gest Hub, ONB HUB,
CX Hub, IntHub**) são **single-tenant**. Ou seja, 3 dos 4 módulos consumidores do Hub são
single-tenant, mas o schema do Hub é multi-tenant por `organization_id` — a compatibilidade entre as
duas coisas não está resolvida em nenhuma das páginas.

**Camadas de privacidade, agora definidas** (ÍNDICE MESTRE, 28/05/2026) — isto responde o que
significava o "T1" que apareceu autodeclarado na fonte da Cambos: **T2** = equipe
(`~/Documents/uMode-OS/` + Drive) · **T1** = restrito · **T0** = privado, fora do Drive do time.
Continua **sem resposta** se estamos autorizados a usar conteúdo T1 — a definição esclarece a
etiqueta, não a permissão.

**Fonte que a infra não alcança, e é a mais importante:** o ÍNDICE MESTRE avisa em destaque que
**`uMode-OS` é uma pasta local no Mac do João** (`~/Documents/uMode-OS/`), não um espaço do Notion,
e que ali vivem o `MANIFEST.md`/`CATALOGO.md` e um **inventário vivo com crosswalk repositório ↔
produto**. É exatamente o mapa que resolveria a dívida 3.2 e o item 21 das pendências — e nenhum
agente remoto tem acesso. A própria página instrui: agentes remotos devem pedir o conteúdo ao João.
Enquanto isso não for resolvido, **o cérebro depende de uma pasta em uma máquina**.

**Padrão de 6 arquivos por projeto** (mesma atualização), útil para qualquer repositório que a infra
vá criar: `CLAUDE_OPERADOR` (base universal do João, referenciada e não duplicada),
`CLAUDE_PROJETO`, `CLAUDE`, `AGENTS`, `CONTEXT`, `CONTEXT_LOVABLE_DOCS`.

---

## 4-C. uFlow — o que o schema da plataforma legada expõe

Levantado em 04 ago 2026 por leitura de `db/schema.rb` (211 tabelas, 443 migrations) em
`C:\Ambientes Virtuais\uFlow\umode-flow`. **Nenhum valor de credencial foi extraído.** Não é auditoria
de segurança pedida pela equipe — são pontos que a estrutura expõe e que precisam de avaliação. Mapa
completo em `uMode/04_Dados-e-IA/_contexto/uflow-modelo-de-dados.md`.

| # | Item | Por que importa |
|---|---|---|
| 4C.1 | **`jumper_integrations.properties` (YAML) guarda as credenciais de ERP de cada cliente.** Confirma no nível do schema o `RISC-001` que a documentação do IntHub registra como **aberto**, owner Bergson | é o risco de maior impacto declarado em toda a Casa, e agora está confirmado por duas fontes independentes |
| 4C.2 | **`jumper_entities.api_token`** — token em coluna `string`, aparentemente sem hash | token de API por tenant em texto |
| 4C.3 | **`jumper_users` tem duas colunas de senha:** `password` (string(191)) e `encrypted_password` | a primeira parece resíduo do legado Laravel; se ainda for populada, é senha em coluna extra |
| 4C.4 | **`db/schema.rb` não é a fonte de verdade completa:** faltam 4 tabelas — entre elas **`jumper_policies`**, a tabela de permissão da plataforma — e 6 das 8 views `vw_*` | **`db:schema:load` num ambiente novo produz aplicação que não sobe.** Bloqueia provisionamento reproduzível de ambiente |
| 4C.5 | **58% das tabelas (122 de 211) não têm `entity_id`**; sem RLS, sem schema-per-tenant; só 41 FKs para `jumper_entities` | **o isolamento entre clientes depende da aplicação, não do banco.** Um bug de escopo vaza dado entre clientes sem o banco reclamar |
| 4C.6 | **`jumper_integration_executions` é append-only sem índice de consulta:** sem `entity_id`, sem `deleted_at`, sem expurgo em 443 migrations, e `status`/`executed_at`/`updated_at`/`created_at` **sem índice** | é a tabela que o IntHub faz polling a cada 6h, já com 218.655 linhas. **O polling faz full scan e não consegue filtrar por cliente sem JOIN** |
| 4C.7 | `api/v1/j3/integration_executions_controller.rb` — `set_integration_execution` usa `find(params[:id])` **sem escopo de entity**, e o `rescue` do `update` está **comentado** | endpoint público de integração buscando registro por id global |
| 4C.8 | **`umode_product_cost_sheets.value_cents` é `t.float`** (e `money-rails` não está no `Gemfile`) | **todo cálculo de custo carrega erro de ponto flutuante** |
| 4C.9 | **O banco operacional dos clientes carrega o banco comercial da uMode:** `jumper_customers`, `jumper_customer_invoices`, `jumper_subscription_plans`, `jumper_leads`, `jumper_pipedrive_deals` | faturamento e CRM da uMode lado a lado com ficha técnica de cliente, no mesmo banco e no mesmo backup |
| 4C.10 | **`jumper_entity_configs.deleted_at` é `t.string`** — única no schema; as outras 147 são `datetime`/`timestamp` | soft-delete comparando string com timestamp, na tabela que controla o comportamento por cliente |
| 4C.11 | **~9 tabelas de legado morto** (workflow antigo + bloco Laravel) e **73 tabelas sem model anotado** | superfície a mais para manter, backup e auditar |
| 4C.12 | **A gem privada `j3_components` (`UmodeApp/j3-components`) não está no repositório** e parte do core `J3::` vive nela | limite de conhecimento do agente da `D-2026-002`, e dependência de build não versionada aqui |

**Insumo para a dívida 3.2 (entidade "conta/instância"):** o tenant da uFlow é `jumper_entities`, e o
vínculo usuário↔cliente↔permissão vive em `jumper_user_roles` (`user_id` + `entity_id` + `policy_id`).
**`jumper_users` é global** — um e-mail existe uma vez para a base inteira. É o modelo real contra o
qual a nossa entidade "conta" precisa ser desenhada.

---

## 5. Limites de ambiente que já bateram na prática

Registrados porque vão voltar se a infra rodar os mesmos scripts.

1. **Limite de 260 caracteres de caminho no Windows** — travou o `git add` de ~146 arquivos de export
   aninhado do Notion (Sessão 22). Foi resolvido encurtando nome de pasta, **não** mexendo em
   `git config`. Se a infra manipular exports do Notion, o caminho longo volta.
2. **PowerShell 5.1 e encoding** — literal acentuado em `.ps1` salvo sem BOM UTF-8 gera mojibake no
   arquivo gerado. Aconteceu duas vezes (Sessões 23 e 25). Se a automação rodar em PowerShell,
   padronizar a toolchain (ou migrar os scripts para algo com encoding previsível).
3. **PowerShell: pipeline que devolve 1 item vira string escalar** — causou título de demanda cortado
   para 1 caractere (Sessão 21) e detecção errada de narrativa (Sessão 25). Sempre `@(...)`.
4. **PowerShell: alias vence função** — uma função chamada `Ls` nunca é chamada (`ls` =
   `Get-ChildItem`), e a falha é silenciosa: gerou um índice inteiro vazio antes de ser notada
   (Sessão 25).
5. **Leitura de arquivo grande via MCP estoura o limite de resposta** — ver 1.2. A solução usada foi
   processar em disco; a infra precisa de streaming.

---

## 6. Como usar este documento

- **Não é fila de execução.** É insumo para a conversa com a equipe tech (o André aparece nas fontes
  como o interlocutor técnico das decisões de arquitetura).
- Cada item novo que aparecer deve entrar aqui **no momento em que for identificado**, com o limite
  medido — não com estimativa.
- Itens que virarem decisão travada saem daqui e vão para `CONTEXT.md` ou para o protocolo
  correspondente, como já é a regra de `_pendencias-gerais.md`.
