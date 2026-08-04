# Varredura geral — ferramentas, produtos e áreas (Google Drive, 03 ago 2026)

> Varredura pedida pelo Vinicius com dois objetivos: (a) padronizar o que já dá para padronizar, e
> (b) atacar o problema que ele antecipou — **nomes diferentes para a mesma coisa entre fontes de
> dados diferentes**. Só fonte real, com ID de Drive. Nada inferido por semelhança de nome.

## Resultado imediato: as 16 Soluções do Portfólio ganharam registro

`produto.md` estava em **0 de 16** (era o eixo mais vazio do cérebro, medido em
`_auditoria-indexacao.md`). Agora são **16 de 16**, em
`uMode/03_Produto-e-Solucoes/01_PlanejAI/` … `16_Sales-Hub/`, validados por diff de headings contra
`_template_produto` — 0 divergências.

**Score de maturidade preenchido só onde a fonte declara** (regra do `protocolo-gestao-produto.md`):

| Solução | Maturidade | Base da decisão |
|---|---|---|
| DesenvolvAI | **Escalável** | 1.376 usuários em contas de uFlow, 653 com acesso em jul/2026 (65%), ~20 organizações — planilha de acessos viva |
| CriAI | **Escalável** | já decidido em 14 jul 2026 (repositório real + robustez 87,75%) |
| Taxonomia | **Escalável** | implementada e inviolável na V1: **12 zonas, 42 dimensões, 419 valores**; replicada por outro módulo via seed |
| CX Hub | **Escalável** | "Fases 0-9 concluídas, em produção" |
| VendeAI | **MVP** | "NÃO está na Arquitetura uMode V1" — piloto de tese com a NK, com critérios formais de promoção |
| CliprocAI | **MVP** | PRD v1.6, 17 ADRs, piloto Cambos (já registrado em 14 jul 2026) |
| FornecAI | **Ideação** | 🆕 declaração literal: **"FornecAI ainda não nasceu"** |
| GerenciAI | **Ideação** | 🆕 declaração literal: **"GerenciAI ainda em brainstorm"** |
| PlanejAI · EnriqueceAI | **MVP** | decididos **depois**, com a leitura da página canônica no Notion — ver seção "Notion" no fim deste documento |
| CadastrAI · AlocAI · ONB HUB · IntHub · Gest Hub · Sales Hub | `[a preencher]` | evidência ausente, ambígua ou conflitante — cada arquivo cita exatamente qual, em vez de escolher um balde por intuição |

## A fonte-âncora achada: Arquitetura uMode V1

`ARQUITETURA_UMODE_REF.md` — "Bússola Arquitetural", v1.0 abr 2026, do CEO
(Drive `1xCFtkT5krc-VATCC26MeQHWOWH1BOMlE`). Define o **fluxo oficial** de módulos, decidido em
sessão de 24/04/2026:

```
PlanejAI → CriAI → DesenvolvAI → FornecAI → EnriqueceAI → GerenciAI
  + CadastrAI (núcleo)  + Hub de Agentes (lateral)
```

Isso resolve, com fonte, o `Pipeline e relações` (upstream/downstream) dos 6 módulos de fluxo — que
até agora era `[a preencher]` em tudo. E traz três coisas estruturais novas:

1. **6 princípios transversais**, sendo o 1º já conhecido e reconfirmado: *"toda marca herda a mesma
   arquitetura, cliente não cria campo custom — só habilita/desabilita e dá apelido interno"*. Os
   outros: configuração em 2 camadas (PADRÃO uMode inviolável × PERSONALIZAÇÃO da marca), padrão
   **Alerta vs Bloqueia**, **AI First** (módulo não espera input: emite evento
   `{vertical, criticidade, evento, contexto, ação_sugerida, configuração_marca}`), taxonomia como
   idioma comum, e Hub de Agentes com **treinamento em 2 níveis** (intrínseco + complemento por
   aplicação).
2. **Agentes nomeados que já existem**: `product-analyzer`, `tryon-stylist`, `audio-transcriber`,
   `product-enricher` (futuro, "fica em EnriqueceAI"). É o primeiro dado real sobre "Agente" como
   entidade — que em `brainwave/CONTEXTO.md` ainda estava como "não existe entidade formal".
3. **"Hub de Agentes" é pilar da arquitetura, não item do nosso Portfólio de 16.** Confirma a
   separação já travada em `CONTEXT.md` de que Hub de Agentes ≠ CX Hub.

⚠ **A fonte de verdade canônica está no Notion, não no Drive.** O próprio documento diz: *"se
contradição entre este arquivo e a página V1 → página V1 vence"*. Página
`34db1d38e768814b8001d7cb6cacf4e5`; skill `umode-arquitetura-tese`
`34db1d38e768819abc2dc7844ff2be59`; Plano Técnico do Hub de Agentes em "AGENTES E PROJETOS /
Produtos Internos"; Modelo PLM Padrão (12 premissas, 6 categorias, 9 verticais) em "CadastrAI
taxonomia_v1". **Nada disso foi lido ainda.**

## O problema de taxonomia entre fontes — agora com evidência

O Vinicius previu: *"em dado momento tratamos inclusive das taxonomias entre diferentes nomes que
exemplificavam 'uma mesma ferramenta' entre fontes de dados diferentes"*. A varredura achou o caso
mais grave — e ele não é de ferramenta, é de **cliente**.

A planilha **"uMode - Controle de Acessos"** (Drive `1JsMyuSR3kl0l2AzOGsKikqVNVrBDbhFvgKVhZMYdSWI`,
modificada em **03 ago 2026** — é fonte viva) lista **60 contas de organização na plataforma**. O
nome nessa planilha é o nome da **conta**, e não bate com o nome do CRM:

| Nome na conta (plataforma) | Nome no CRM | Situação |
|---|---|---|
| `RESERVA` · `Vix` · `NK Store` · `BAW` · `OFICINA` · `StudioZ` · `LOJÃO DO BRÁS` · `Ton age` · `Paloma Concept` | Reserva · VIX · NK STORE · Baw · Oficina Reserva · Studio Z · Lojão do Brás · Ton Age · Paloma concept | ✅ **absorvido pelo `client_id`** — todos colapsam no mesmo slug |
| `Objetiva` | Moda Objetiva | ✅ **resolvido em 03 ago 2026** — o Vinicius confirmou que são o mesmo cliente ("internamente somente que se referencia cada vez de um jeito"); registrado como alias em `institucional.md` |
| `Mondepars` | Mondpars | ⚠ grafia diferente, não é só caixa — **um dos dois está errado** |
| `Lojas Estrela` | Estrela | ⚠ não colapsa — precisa alias |
| `Cambos` **e** `Cambos - uFlow` | Cambos | ⚠ **duas contas para um cliente** (7 e 25 usuários). O sufixo indica conta por módulo |
| `Tempo de Criança` **e** `Tempo de Criança (uRocket)` | *(não existe no CRM)* | ⚠ mesmo padrão: uma conta por ferramenta, incluindo a legada uRocket |
| `Studio Z <> SalesForce` | Studio Z | ⚠ conta de integração, não de cliente |

**Conclusão travada:** o `client_id` resolve variação de caixa/acento (a maioria dos casos), mas
**não** resolve nome comercial diferente nem conta-por-módulo. O campo `### Aliases do cliente`
existe exatamente para isso e deve ser alimentado com os nomes de conta — o que ainda **não** foi
feito, porque exige decidir antes se `Cambos - uFlow` é alias de Cambos ou uma entidade
"conta/instância" que não temos modelada.

### ~20 organizações com conta na plataforma e sem linha no CRM
`ALADIM DECOR V2` · `Beira Rio` · `Dakota` · `Grendene` · `Via Marte` · `Nanaminze Varejo` ·
`Feira Ópera` · `Fluxx Moda` · `Formitz Confecções` · `FOUR ONE` · `Makor SA` · `Meta` ·
`OPERA KIDS` · `Planifiquese` · `RIBEIRO E PAVANI` · `Shopping Mamãe Cheguei` ·
`Tempo de Criança` · `Trama Jeans`

Algumas são marcas grandes e reconhecíveis do setor (Grendene, Dakota, Beira Rio, Via Marte).
**Nenhuma virou casa de cliente** — a regra travada é que o CRM é a única fonte de "quem é
cliente". Mas isso inverte a pergunta: até agora a dúvida era "a pasta do Drive tem nome que não
está no CRM"; agora é **"a plataforma tem conta ativa de organização que o CRM não conhece"** — o
que é bem mais forte como sinal.

Contas que claramente **não** são organização-cliente (e servem de filtro para qualquer importação
futura): `Suporte` · `Demonstração SMB` · `Conta demo - Ana Lúcia` · `Onboarding Fase 2 (Teste Ju)` ·
`Embaixador 1` · `Embaixador 2` · `Embaixadora Daniela` · `Embaixadora Jelza` ·
`Embaixadora Kelly` · `Embaixadora Rejane` · `Fabio Povoa`.

## Dado de engajamento real — inédito no cérebro

A mesma planilha traz o que nenhuma fonte anterior tinha: **uso medido por cliente**.
Total: 1.376 usuários, 653 com acesso em jul/2026 (**65%**), e apenas 45 em ago/2026 (12% — mês
recém-começado, não é queda).

| Cliente | Usuários | Engajamento jul/2026 |
|---|---|---|
| RESERVA | 296 | 45% |
| NV | 191 | 50% |
| Caedu | 138 | 52% |
| Osklen | 97 | 62% |
| Vix | 66 | **88%** |
| OFICINA | 66 | 44% |
| NK Store | 69 | 67% |
| Puket | 58 | 62% |
| BAW | 44 | 50% |
| StudioZ | 43 | **0%** |
| Luiza Barcelos | 35 | 74% |
| Objetiva | 31 | 26% |
| Lofty Style | 30 | 73% |
| Cambos - uFlow | 25 | 80% |
| 4takes | 21 | **5%** |

Isso é candidato natural a alimentar `jornada.md` (saúde da conta) — **não aplicado ainda**, porque
"engajamento" não é campo do template e criar campo exige validação.

A planilha traz também **perfis de acesso por cliente** (ex.: em Lofty Style — `Lofty - Estilo`,
`Lofty - Modelagem`, `Lofty - PCP`, `Lofty - Ficha Técnica`, `Lofty - Compras MP`,
`Lofty - Compras Importado`, `Lofty - Planejamento`, `Lofty - Admin`, `API`), com nome e e-mail de
cada usuário. **É a 4ª taxonomia de "área"** que aparece no projeto (organograma × 8 Áreas internas
× Mapa-mãe × perfil de acesso da plataforma) — e a única que mapeia direto para as 14 áreas
canônicas de cliente. Fonte forte para preencher `contexto-area.md` e `pessoas.md` de cliente, os
dois maiores vazios do cérebro. **Não aplicado nesta rodada** — é a próxima frente óbvia.

## Outros documentos de produto localizados (não lidos integralmente)

| Documento | Drive | Sobre |
|---|---|---|
| `CLAUDE_PROJETO.md` | `1WslGEnAAoI-72Jbb8nXLqc01FQLuZL_F` | projeto do CEO; o doc de arquitetura o cita como fonte dos critérios de promoção do VendeAI (§08) |
| `CLAUDE_PROJETO._criai.md` | `1XYB-3ZCyiia4jFAmRqWvvIY2WQNNHtLp` | CriAI |
| `PRD_IDEACAO_NV.md` | `1FJHsS-fIm2cOIH7jhdQLdokcDZtHs_Ts` | PRD de ideação com a NV (5 cópias no Drive) |
| `PRD_CLIPROCAI.md` | `1mUtDq1pKC-AWkS8rNnQMw4t8xFnXuOcG` | CliprocAI — ⚠ vive na pasta T1-restrita da Cambos |
| `enriqueceai_diretriz.json` | `1Au2Jtbj1k1DuvHR2INb514ufSbddsn7M` | diretrizes do EnriqueceAI |
| `NV _ CadastrAI _ Definição de Grupos e Atributos.xlsx` | `1Jn-aggCqo-4rp5twHr5Voq-jWu_eNui5` | CadastrAI aplicado na NV |
| `Template | Material Treinamento Go Live uFlow` | `1W8mdrH_tFB-ZQGwxHgAmcoLrf7PzEOTzJbSf1bHzaa8` | material de treinamento padronizado de Go Live |
| Notas de reunião (Gemini) sobre PlanejAI/EnriqueceAI com NV e RSV | vários | jul/2026 — uso real, com gravação |

## O que esta varredura NÃO cobriu (para a próxima)

- **Notion** — é a fonte de verdade canônica declarada pela própria arquitetura, e nesta sessão
  passou a existir acesso via MCP. Nada foi lido de lá ainda. É a maior lacuna deste documento.
- Leitura integral dos PRDs e do `CLAUDE_PROJETO.md` (dariam maturidade e escopo com fonte
  explícita para PlanejAI, EnriqueceAI, CadastrAI — hoje `[a preencher]`).
- Perfis de acesso × áreas canônicas por cliente (a 4ª taxonomia de área acima).
- `AlocAI` continua sem **nenhuma** evidência em fonte alguma. Vale perguntar se existe de fato.

---

# Notion — acesso confirmado e primeira leitura (03 ago 2026)

Acesso via MCP ao workspace real **`uMode Mode's Notion`**, autenticado como Vinícius Risoléo.
Todas as ferramentas disponíveis no plano. Teamspaces: `General` (membro), `Inovação`, `Kudos`,
`Recrutamento`. **Os IDs citados no documento de arquitetura do Drive funcionam** — não foi
necessário procurar caminho.

## A página canônica foi lida

**"🏛️ Arquitetura uMode — Especificação por Módulo (V1 — sessão 24/04/2026)"**
(`34db1d38e768814b8001d7cb6cacf4e5`), 51 KB, sob `AGENTES E PROJETOS`. É captura completa da
sessão de arquitetura entre João Risoléo e o agente AZZAS. Estrutura: visão geral AI First →
padrões transversais (5) → um capítulo por módulo (PlanejAI, CriAI, DesenvolvAI, ForneceAI,
EnriqueceAI, GerenciAI) → Núcleo CadastrAI → Hub de Agentes → configurações por organização →
pendências.

**Tese central registrada em fonte:** *"Menos cobertura, mais velocidade."* E a definição do que a
uMode é: *"Não é 'PLM com IA dentro' — é uma arquitetura desenhada AI First"*.

### O que isso decidiu (item 1 da frente)
| Solução | Antes | Agora | Evidência literal |
|---|---|---|---|
| PlanejAI | `[a preencher]` | **MVP** | tem "PRÉ-SEASON (**modo atual** — estúdio sob demanda)" × "IN-SEASON (**modo futuro**)" — opera hoje, metade do escopo por vir |
| EnriqueceAI | `[a preencher]` | **MVP** | *"A detecção de atributos a partir da foto do produto **JÁ EXISTE** e é a espinha dorsal do módulo atual"* |
| GerenciAI | Ideação (Drive) | **Ideação confirmada** | seção Status do módulo: *"Brainstorm consolidado, não decisão final"* + fala do CEO: *"estou no campo do brainstorm, não tenho opinião formada, vou ter que conceber"* |

Maturidade decidida passou de **6 para 10 dos 16** itens do Portfólio.

⚠ **Divergência de nomenclatura na fonte canônica:** a página escreve **"Módulo 4 — ForneceAI"**;
`CONTEXT.md` escreve **"FornecAI"**. Nenhum dos dois foi alterado — é decisão do Vinicius/CEO qual
grafia é a oficial. É exatamente o tipo de caso que ele previu.

## A base viva de Demandas — o que ela diz

Database `🤿 Demandas de Clientes` (`ddf1951a-8dc2-42e6-98e6-bae3d1f5a865`, data source
`ae2c893a-903e-4f10-962d-c6ad1e52c47b`), sob `Databases › 22. Demandas de Clientes`.

**Nossa formalização está em dia.** A base tem **1.010 demandas**; o export de jul/2026 tinha 1.007;
**apenas 1 foi criada depois de 14/jul** e a mais recente é de **15/jul/2026**. Ou seja: o medo de
defasagem (pendência 28) era infundado — a base está quieta desde meados de julho, e as 997
formalizadas + 4 da Casa cobrem ~99% dela. As ~9 restantes são as sem cliente (item 34).

**A tradução de status está 100% correta contra o schema vivo.** O enum real é exatamente o que
mapeamos: 6 valores de Status (`Não iniciada`, `Standby - Produto`, `Nível de Análise`,
`Demanda Aceita`, `Concluída`, `Encerrada`) × 9 de Etapa (`Análise Cliente`, `Análise uMode`,
`Backlog`, `Na Fila`, `Em Desenvolvimento`, `Em Teste`, `Em Validação - Cliente`,
`Demanda Concluída`, `Demanda Cancelada`). Nenhum valor fora da nossa tabela.

**A relação `👥 Clientes` tem `limit: 1`** — o schema **proíbe** demanda multi-cliente. Valida a
decisão de tratar cada demanda como de um cliente só (diferente de RFI, onde o legado tinha 2 casos).

### Enums que o export não mostrava por inteiro
- **`Bloqueio`: 8 opções**, não 6. Novas: **`Aguardando Terceiros`** e **`Aguardando Comercial`** —
  reforçam a pendência 33 (nosso enum de `Motivo de bloqueio` está incompleto).
- **`Suporte Integração`: 17 opções**, contra 8 vistas no export. Novas: `Auditoria`, `CSV`,
  `Escrita - Preenchimento Usuario`, `Escrita - Programação`, `Leitura - Erro`,
  `Leitura - Grade pendente`, `Script`, `Escrita - Código de Barras`. **É uma taxonomia técnica de
  integração pronta** — casa direto com a frente de repositórios de integração.
- **`uMode - Macro Tema`: 20 opções** (`template de ficha`, `macroplan`, `workflow`,
  `pacote de materiais`, `integração`, `aprovação`, `permissionamento`, `ficha tecnica`,
  `relatorios`, `login`, `tarefas`, `exportação`, `tabela de medidas`, `checklist`,
  `ficha de impressão`, `importação`, `regra de negocio`, `action`, `campos`, `validação`).

### Narrativa: confirmada, e é trabalho de lote
A coluna `Texto` vem preenchida em **2 de 1.010** — confirma que a narrativa **não** é propriedade,
vive nos blocos do corpo da página. Testado e funcionando: a demanda `UMD-1256` (NK STORE) devolveu
o texto integral do cliente pedindo parametrização de contas contábeis para a coleção ACOES, com
imagem anexada. **Custo real:** 1 chamada por página, ~750 páginas para os clientes fora de Lofty.
É lote, não uma operação única — precisa rodar em blocos.

### Duas entidades reais que apareceram
1. **`Projeto`** — relação para outro database (`241b1d38-e768-80cd-9213-000b0dbeb621`). É o que a
   coluna `Projeto` do export apontava (ex.: `[NK] - uFlow`, `📌 [LOFTY] - ONBOARDING FASE 1`).
   Preenchida em 594 das demandas. Liga demanda → fase de onboarding, o que conversa direto com
   `jornada.md`. **Não modelada ainda.**
2. **Views nomeadas por dupla de atendimento** — a base tem views `Laura /Holmer` (9 clientes),
   `Julianne/Pedrão` (7), `Fernanda / Victor` (2) e `Marina` (8), cada uma **filtrada por lista
   explícita de páginas de cliente**. É um mapeamento pessoa→clientes vindo da ferramenta
   operacional, não do CRM — serve de contraprova para as 13 fichas de Pessoa, e confirma as duplas
   (Julianne Dias Rodrigues + Pedro Murillo; Fernanda Araujo + Victor Aragão).

A base de RFI também é alcançável (`24fb1d38-e768-8011-b212-000bf0cd960d`), assim como a de
Clientes (`ec041afd-fcee-44f8-83cb-223fca6f4108`) — que é a lista de clientes do Notion, uma **5ª
fonte** de "quem é cliente", ainda não cruzada com o CRM.


