# CONTEXT.md — Institucionalização de IA · core

> Documento-base do projeto. Define **o quê** e **como**. É a fonte única do objetivo:
> nenhuma seção, arquivo ou prompt precisa repetir o objetivo — basta referenciar este arquivo.
> Avanço e tarefas ficam em `STATE.md`.

## Objetivo
Institucionalizar o uso de ferramentas de IA por toda a equipe, tornando os colaboradores
High Individual Contributors (HICs), e fazer com que esse uso se reflita diretamente nas
operações internas. **O foco é interno**; o atendimento a clientes é consequência e reutiliza
a mesma estrutura.

## O que estamos construindo
Um "cérebro" por instituição. Cada instituição — a Casa interna e cada cliente — é uma **casa**
com a mesma hierarquia de volumes de controle. O contexto vive nesses volumes e é o que torna o
trabalho fluido: pessoas (e, depois, agentes) operam já com o contexto do seu volume.

### Volumetria (hierarquia de cada casa)
1. **Institucional** — identidade, voz, marca, taxonomia, fontes
2. **Áreas**
3. **Subáreas**
4. **Pessoas**

## Regras travadas
- **Áreas e Pessoas:** iguais entre a Casa e os clientes.
- **Subáreas:** nomes livres (podem diferir por organização).
- **Pessoas do cliente** são do próprio cliente. A pessoa interna vive só em `Casa › Pessoas` e
  alcança o cliente por **vínculo de atendimento** (pessoa da Casa + escopo do cliente), sem
  duplicar identidade.
- **Comunicação entre casas:** *demanda* sai da Casa → cliente; *contexto* volta cliente → Casa.
- **Isolamento:** cada cliente é uma casa fechada; contexto não vaza entre clientes.
- **Nem todo fluxo envolve cliente:** há processos 100% internos (ex.: People), sem demanda.

## Endereçamento de volume
Todo volume tem um endereço previsível — base para que pessoas e agentes achem o contexto certo:
- `Casa › Comercial › Pré-vendas › Pessoas › fulano`
- `Cliente:Acme › Compras › Pessoas › aprovador`

## Pessoas (ficha individual)
> Travado em 09 jul 2026. Detalhamento operacional completo em
> `uMode/00_Institucional/_protocolos/protocolo-gestao-pessoas.md`.

Operacionaliza a regra já travada acima ("Pessoa interna vive só em `Casa › Pessoas`"): cada
pessoa da Casa ganha uma ficha individual (`_template_pessoa.md`), não só a linha solta que já
existia em `pessoas.md` de cada cliente.
- **Onde vive:** um único registro por pessoa, em `00_Institucional/_pessoas/` — 3ª subpasta
  fixa da Casa (junto de `_demandas/` e `_rfis/` do lado de cliente), mesma lógica de
  não-duplicação. `pessoas.md` de cada cliente continua existindo, mas passa a **referenciar**
  a ficha da Casa por vínculo de atendimento, em vez de repetir dado.
- **Duas classes de campo, nunca fundidas:** documentável (cadeira, área, clientes atendidos —
  vem de organograma/CRM/histórico real) vs. personificação (personalidade, autodescrição — só
  a própria pessoa preenche, via formulário; nunca inferido de documento).

## Demandas
> Travado em 06 jul 2026. Detalhamento operacional completo em
> `uMode/00_Institucional/_protocolos/protocolo-gestao-demanda.md`.

Duas taxonomias coexistem sem se fundir — todo campo que colide de nome carrega a etiqueta de
qual estrutura ele vem:
- **Organizacional (BrainHub):** Natureza, Origem/Destino, hierarquia pai/filha, Marcos,
  aprovação de contexto — segue a hierarquia deste documento.
- **Operacional (CX Hub):** Quadro (Operação/Tech), Área (CX Hub — squad interna da
  ferramenta, sem relação com a Área organizacional), Origem (CX Hub — motivo/gatilho),
  Status, Prioridade, Tipo, Subdemandas, Conversas, Atividades. Ferramenta oficial de gestão de
  demandas a partir de agora; o Notion (legado) não é migrado campo a campo — cada demanda
  antiga é traduzida individualmente na hora da migração.

- **Onde vivem:** um único registro por casa/cliente, em `00_Institucional/_demandas/`.
  `_demandas/` é uma 3ª subpasta fixa, mas só no nível Institucional de cada casa — as demais
  áreas/subáreas seguem só com `_contexto/` e `_protocolos/`. Uma demanda nunca é duplicada
  dentro das áreas que ela envolve; ela referencia `Origem`/`Destino` organizacionais por
  metadata, na mesma lógica já aplicada a Pessoa interna.
  - Endereçamento: `Casa › Demandas › D-2026-014` / `Cliente:Acme › Demandas › D-2026-014`.
- **Natureza (enum fechado, organizacional):** interna · inter-área · intra-área ·
  casa-cliente.
- **Marcos:** log append-only por demanda (data, evento/decisão, responsável, novo status) —
  nunca se reescreve um marco, só se adiciona um novo. Distinto de "Marcos da jornada"
  (`jornada.md`, fases macro da relação) e de "Conversas"/"Atividades" do CX Hub.
- **Pai/filha:** uma demanda mãe pode gerar N demandas filhas em áreas ou casas diferentes;
  cada filha marca se bloqueia ou não a conclusão da mãe. Distinto de "Subdemandas" do CX Hub
  (checklist tático dentro do mesmo card, sem trocar de área/casa).
- **RFI:** nem toda demanda vira RFI; toda RFI nasce de uma demanda, conforme classificação e
  aprovação (apresentação ao cliente → aprovação para desenvolvimento). Vive em
  `Cliente/00_Institucional/_rfis/` (subpasta fixa só do lado de cliente — RFI sempre tem um
  cliente associado, diferente de Demanda). Modelo completo:
  `protocolo-gestao-rfi.md`.
- **Retroalimentação:** quando uma demanda exige mudar um MD de contexto, ela referencia
  exatamente qual `Contexto impactado`; só é aplicada após aprovação da pessoa registrada no
  campo "Governança" do MD-alvo — nunca um agente escreve contexto sem essa aprovação
  registrada como marco. Esse ciclo de aprovação de contexto é separado do `Status` operacional
  do CX Hub.

## Como estamos construindo (fase atual)
- **Base: Google Drive apenas.** O objetivo agora é sacramentar a estrutura e o processo.
- Sem agentes configurados e sem banco de dados ainda.
- A estrutura de pastas + nomenclatura **é** o schema; acertá-la agora é o que permite plugar
  agentes e banco depois sem retrabalho.

## Fora de escopo agora (fica para depois)
- Agentes e automação do "download" de contexto.
- Banco de dados (perfis e permissionamento fino) — resolvido por governança de perfis depois.
- Matriz de permissão detalhada por tipo de demanda.

## Glossário
- **Casa** — a organização interna (foco).
- **Cliente** — organização atendida; cada uma é uma casa isolada.
- **Volume (de controle)** — qualquer nó da hierarquia que guarda regras + contexto.
- **Demanda** — qualquer unidade de trabalho necessária para o ecossistema funcionar. Não é
  limitada por área, complexidade, ou por envolver um cliente — cobre desde uma demanda 100%
  interna até uma que liga um escopo da Casa a um escopo do cliente. Modelo completo em
  `## Demandas` abaixo e em `uMode/00_Institucional/_protocolos/protocolo-gestao-demanda.md`.
- **Marco (de demanda)** — evento ou decisão pontual registrado dentro de uma demanda, com
  data e responsável. Não confundir com "Marcos da jornada" (fases macro da relação
  uMode↔cliente, registradas em `jornada.md`).
- **RFI** — Request for Implementation. Formaliza uma demanda para negociação/entrega com o
  cliente; sempre nasce de uma demanda (nunca é aberta do zero), mas nem toda demanda vira
  RFI. Modelo completo em `uMode/00_Institucional/_protocolos/protocolo-gestao-rfi.md`.
- **Atendimento (vínculo)** — relação que leva uma pessoa da Casa a operar num cliente.

## Áreas internas — nomes (confirmado)
> Só os nomes nesta fase. O contexto de cada área será definido depois, com o CEO.
> Institucional **não é uma área** — é o nível 1 da hierarquia (identidade, voz, marca,
> governança). Não aparece na lista de áreas operacionais.
1. **Comercial** — engloba marketing, branding e vendas
2. **Atendimento** — CS, relacionamento e saúde de contas de clientes
3. **Produto & Soluções** — PRDs, features e builds (ex.: Lovable)
4. **Dados & IA** — agentes, base de conhecimento e integrações
5. **Financeiro** — recebíveis, alçadas e contexto financeiro sensível
6. **Tecnologia** — tech e integrações internas
7. **People** — 100% interno; reuniões, transcrições e controle de atividades
8. **Operações** — admin, backoffice e implantação

## Decisão: camada "Produto" na hierarquia
> Travada em 01 jul 2026. Refinada em 01 jul 2026.

Produtos (ex.: PlanejAI, EnriqueceAI, VendeAI) **não formam um nível hierárquico novo.**
São tratados como **subáreas com atributo `tipo: produto`**, diferenciando-os de subáreas
operacionais. Endereçamento: `Casa › Produto & Soluções › PlanejAI`.

Justificativa: preserva a hierarquia limpa de 4 níveis. Um 5º nível será adicionado somente
quando a complexidade real exigir — e a migração será simples porque o atributo já estará
registrado desde agora.

### Portfólio completo de produtos e soluções
Divididos em duas categorias: **voltados ao cliente** (têm `conecta_area_cliente`) e
**internos** (operam só dentro da Casa, sem conexão direta com área do cliente).

#### Voltados ao cliente (moda)
| Produto | Área canônica do cliente | Descrição |
|---|---|---|
| PlanejAI | Planejamento | do histórico ao mix de coleção |
| CriAI | Estilo / Criação | briefing → criação |
| DesenvolvAI | Desenvolvimento de Coleção | croqui → lacre |
| FornecAI | Compras / Supply / Sourcing | ambiente do fornecedor |
| EnriqueceAI | E-commerce / Cadastro | lacre → catálogo (atributos, SEO) |
| GerenciAI | Planejamento + Financeiro | planejado × realizado |
| AlocAI | Logística / CD | alocação & distribuição por loja |
| VendeAI | Comercial / Vendas | motor de vendas |
| CliprocAI | Comercial / Vendas | decisão CLI×PRO×CA |

#### Internos (Casa apenas — sem conexão direta com área de cliente)
> Confirmado em 10 jul 2026 por dupla fonte real: `arquitetura_umode_4.extracted.txt`
> (documento técnico "Arquitetura uMode — Especificação por Módulo", v1, 24 abr 2026) e
> `brainhub_mapa.html` ("BrainHub — Mapa-mãe · uMode", v1, 10 jun 2026 — a versão mais recente
> encontrada até agora sobre o BrainHub, com a mesma lista de plataformas) — ambos do CEO. O
> `launch.json` de ambiente de desenvolvimento do CEO confirma repositório de código ativo
> para CX Hub (`gist-sparkle`), ONB HUB (`umode-gest-o-de-opera-o-2f6bdc59`), IntHub
> (`integration-pulse-check-e914756f`) e Gest Hub (`umode-gesthub`) — todos reais, em
> desenvolvimento.

| Produto | Descrição |
|---|---|
| CadastrAI | fonte única e governante de dados — sustenta todo o portfólio |
| Taxonomia | padrão de atributos — base transversal |
| CX Hub | experiência do cliente (atendimento interno) |
| ONB HUB | onboarding & operação de implantação |
| IntHub | integrações · gold standard |
| Gest Hub | gestão interna |
| Sales Hub | em construção |

### "Sistema Operacional uMode" — arquitetura de operação (não fundir com o Portfólio acima)
> Levantado em 10 jul 2026 do deck `Sistema-Operacional/` (Drive, 28 mai 2026) e do
> `brainhub_mapa.html` (10 jun 2026). Descreve **como** a uMode opera (ciclo, camadas,
> instâncias) — é um nível de abstração diferente do Portfólio de produtos acima, não uma
> lista alternativa de ferramentas. Registrado aqui só como referência de arquitetura; nenhum
> campo/produto deste projeto foi renomeado ou fundido a partir dele.

- **Duas faces do mesmo motor**: "Dentro" (a fábrica — a uMode opera a si mesma com agentes
  por área) e "Fora" (a prateleira — o que prova valor em Dentro atravessa a ponte e vira
  plataforma/agente vendido ao cliente). Mesmo padrão arquitetural, duas instâncias.
- **O ciclo**: Seed (dado bruto) → Cérebro (refina em contexto) → uGentes (agem no contexto) →
  2º Cérebro (operador decide) → Governança (registra e aprova) → retroalimenta o Cérebro.
- **5 componentes citados no deck de 28 mai** (CadastrAI-Conhecimento, Hub de Agentes, Sync
  Engine, Indicadores, SMART CODE) descrevem essa arquitetura de operação, não uma lista de
  produtos — **não substituem** o Portfólio interno acima. Reconciliação textual observada
  (não confirmada pela fonte como equivalência formal): CadastrAI-Conhecimento ⊃ CadastrAI +
  Taxonomia; "Hub de Agentes" ≠ CX Hub (conceitos distintos, apesar do nome parecido).

> Áreas canônicas do cliente de moda sem produto conectado ainda (oportunidade de portfólio):
> Qualidade · PCP · Marketing · Financeiro · Design · Modelagem · Engenharia.

## Áreas canônicas do cliente de moda (confirmado)
> Lista completa das 14 áreas canônicas. Cada cliente pode usar aliases diferentes
> para a mesma área — o mapeamento alias → canônico é registrado no `institucional.md`
> de cada cliente.

| # | Área canônica | Produto conectado |
|---|---|---|
| 01 | Planejamento | PlanejAI |
| 02 | Estilo / Criação | CriAI |
| 03 | Desenvolvimento de Coleção | DesenvolvAI |
| 04 | Qualidade | — |
| 05 | PCP | — |
| 06 | Compras / Supply / Sourcing | FornecAI |
| 07 | Logística / CD | AlocAI |
| 08 | E-commerce / Cadastro | EnriqueceAI |
| 09 | Comercial / Vendas | VendeAI · CliprocAI |
| 10 | Marketing | — |
| 11 | Financeiro | GerenciAI |
| 12 | Design | — |
| 13 | Modelagem | — |
| 14 | Engenharia | — |
