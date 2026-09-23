---
aliases:
  - "VIX · Pendências e fontes varridas"
tags:
  - tipo/diario
  - cliente/vix
  - status/ongoing
---
# VIX · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o VIX?" e
> "onde eu já procurei?".** O [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md) segue dono das decisões
> **transversais** — as que valem para a carteira toda. **Um assunto, um dono.**

## 0 · O tier de sensibilidade

**Vocabulário `T0`/`T1`/`T2`, o mesmo que o João usa no vault** — não um paralelo nosso.

| Tier | O que é | O que eu faço |
|:-:|---|---|
| **`T2`** | equipe | o padrão — entra normalmente |
| **`T1`** | restrito | entra, e **fica só no `_contexto/` deste cliente** |
| **`T0`** | privado | 🔴 **nunca entra por valor** — registro que existe e **onde** |

## 1 · Risco de segurança

🟢 **Nenhum achado até 22 set 2026.**

⚠ **Isso não é atestado de limpeza:** significa que **nas fontes da § 3** não apareceu
segredo. **As fontes da § 4 não foram olhadas.**

## 1-bis · 🔴 O que eu NÃO consegui ler

> **Pedido do Vinícius em 22 set 2026:** *sobre suspeitas de blocos, sempre tenha atenção e me indique, porque temos que ter a garantia de que tudo que está varrendo está conseguindo tirar proveito de tudo o que podemos*.
>
> 🔴 **Bloco que não renderiza NÃO é bloco vazio.** Na Luiza Barcelos, 17 blocos ilegíveis escondiam **o único Representante Legal da conta** e o cargo do Gerente de Inovação e Tecnologia. **Eu cheguei a chamar isso de falta de acesso, e estava errado** — ver `protocolo-varredura-cliente.md` § 11.

🟢 **Nada ilegível nas fontes já abertas.**

⚠ **Isso só vale para o que foi aberto** (§ 3). **Nas fontes da § 4 não sei**, e a página deste cliente pode ter o mesmo tipo de bloco.

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🔴 **A VIX tem 17 perfis de usuário, e eles SÃO áreas** — `Vix-Admin`, `Vix-CAD`, `Vix-Compras`, `Vix-Desenvolvimento`, `Vix-Estamparia`, `Vix-PCP`, `Vix-Ficha Tecnica`, `Vix-Produto TP`, `Vix-Tabela`, `Vix-Qualidade`, `Vix-Demo`, `uDash` **e CINCO de Estilo**: Biquini, Cover ups, PA, Roupas, Admin. **Confirma perfil = área, com granularidade de SUBÁREA.** | `T2` | decisão sobre mapear perfil para subárea canônica |
| 2 | 🔴 **`Manual` e `Base de Importação` estão bloqueados para os 17 perfis** — **ninguém na VIX acessa o manual.** ⚠ **Conecta com a dor da CAEDU**, que diz que o manual não foi suficiente. | `T2` | decisão de produto |
| 3 | 🔴 **A matriz de ~60 funções × 17 perfis é mantida À MÃO numa tabela do Notion.** Última edição: **09/07/2025**. ⚠ **Não sei se ainda reflete a plataforma.** | `T2` | conferência contra o banco |
| 4 | 🆕 **`uPick`** — sub-página `uPick Vix - Passo a passo`. **Mais um nome de produto fora dos 7 módulos e das 16 Soluções**, junto de `uBuy` e `uPlan`. | `T2` | decisão sobre o portfólio |
| 5 | ⚠ **`uDash` aparece como PERFIL de usuário nesta matriz**, e também é nome de produto legado. **Dois sentidos para a mesma palavra** — mesma armadilha do `collection` do banco contra coleção de moda. | `T2` | desambiguação |
| 6 | 🆕 **A página registra um aprendizado de atendimento:** usuário sem permissão de deletar variante deve pedir a quem tem, **internamente**. ⚠ **Explica uma classe inteira de demanda.** | `T2` | — |
| 7 | 🆕 **Tabela DE/PARA de integração (31/07/2025):** campo uMode para campo Linx, com tabela e tipo (`referenciabr` para `MODELISTA` em `PRODUTOS`). **É o primeiro mapeamento de integração campo a campo que o corpus vê.** | `T2` | vale replicar como padrão de documentação de integração |
| 8 | ⚠ **Nenhum nome de pessoa na página nem na sub-página de perfis.** As 6 fichas da VIX seguem vindo só da base de demandas, **sem cargo**. | `T2` | a página não tem essa informação — depende de outra fonte |

### 2.1 · 🔴 Perguntas que só o Vinícius responde

> **Uma pergunta só entra aqui quando NENHUMA fonte pode respondê-la.** Dúvida que
> uma fonte responde não é pergunta — **é varredura que falta fazer**, e vai para a § 4.
>
> 🔴 **Estas linhas são colhidas automaticamente** para a lista consolidada em
> [`_perguntas-para-o-vinicius.md`](../../../../00_Institucional/_contexto/_perguntas-para-o-vinicius.md),
> que ele responde **por áudio ou por transcrição de reunião**. Ver
> [`protocolo-perguntas-ao-vinicius.md`](../../../../00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md).

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | A VIX tem **5 perfis só de Estilo** (Biquini, Cover ups, PA, Roupas, Admin). **Isso vira subárea canônica no BrainHub, ou continua sendo só perfil da plataforma?** | `T2` | define se perfil e área são a mesma entidade ou duas | **⚠ a distribuir** | aberta |
| 2 | A matriz de ~60 funções × 17 perfis foi editada pela última vez em **09/07/2025** e é mantida à mão. **Ainda reflete a plataforma?** | `T2` | se não reflete, o corpus estaria copiando ficção | **⚠ a distribuir** | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o VIX

| Fonte | Endereço | Quando | O que saiu | Esgotada? |
|---|---|---|---|---|
| Base `Mapa de Clientes` | `collection://ec041afd-…` | 22 set 2026 | status, módulos, ERP, atendimento, cidade, CNPJ, etapa, receita | sim, por SQL |
| Base `Demandas compartilhadas` | `collection://…` (985 linhas) | 22 set 2026 | demandas, `Quem solicitou?`, datas | sim, por SQL |
| Base `Reuniões Compartilhadas com Clientes` | `collection://09a4a94e-…` | 22 set 2026 | 1.161 reuniões, datas, cliente | ⚠ **não**: campo `Participantes` é ID de usuário, não resolvido |
| Base `Chamado&Atendimento` | `collection://2c5b1d38-…` | 22 set 2026 | 185 chamados, 92 e-mails individuais | sim, por SQL |
| Base `Portal do Cliente` | `collection://6548a3ae-…` | 21 set 2026 | segunda lista de clientes | sim, por SQL |
| Base `Etapas do Processo de Clientes` | `collection://348b1d38-…-000bea495254` | 22 set 2026 | 7 etapas; **discorda do campo `Status`** | ⚠ **não**: as 5 páginas de etapa não foram abertas |
| Repositório do **CX Hub** | leitura de código | 22 set 2026 | schema e modelo; **não é fonte de dado** — feature nunca finalizada | sim |
| 🟢 **As 10 páginas `Perfil de Usuário e Permissionamentos`** | sub-página de cliente — VIX, Luiza Barcelos, Oficina Reserva, Lenny, Cambos, NK STORE, Moda Objetiva, Recco, NV e Lofty Style | 23 set 2026 | perfis por cliente (de 3 a 17), matriz de permissão, e o placar do `Fale com o Suporte`: **4 bloqueados × 6 liberados** | 🟢 **sim, as dez** — ⚠ exceto 12 sub-páginas de perfil da NV |
| 📕 **Manual do Permissionamento** | `6d0379fa…`, em `uFlow / Setup - PLM` | 23 set 2026 | 🟢 **o MECANISMO**: `Includes`/`Excludes`, os 3 controllers, `scopable: user|policy`, 23 parâmetros de `actions`, 20 `entity_configs` e o mapa de **72 controllers** | 🟢 **sim, por inteiro** — virou `_dicionario-permissionamento-uflow.md` |
| **Google Drive** — pastas de operação | varredura de 03 ago 2026 | 03 ago 2026 | 16 Soluções, Arquitetura V1, planilha de acessos | ⚠ **não** |

### 3.2 · A página deste cliente no Notion

| Quando | Endereço | O que saiu | Esgotada? |
|---|---|---|---|
| **22 set 2026** | `70a10ec2…` **+ a sub-página `[Vix] Perfil de Usuário e Permissionamento`** | 🔴 **17 perfis de usuário nomeados por área** e uma matriz de **~60 funções × 17 perfis**; tabela **DE/PARA de integração** campo uMode → campo Linx (31/07/2025); `uPick`; ⚠ **nenhum nome de pessoa** | ⚠ **não** — 5 sub-páginas e 2 databases inline não abertos |

### 3.3 · Sub-páginas e documentos deste cliente já abertos

> 🔴 **NÃO reabrir.** O que saiu daqui já está na seção 2.

| Quando | O quê | Endereço | O que saiu |
|---|---|---|---|
| **22 set 2026** | `[Vix] Perfil de Usuário e Permissionamento` | ⚠ **id não anotado na época** | **17 perfis — o maior número da carteira**; 🟢 `Fale com o Suporte` liberado para os 17; 🔴 `Manual` e `Base de Importação` bloqueados; `> excluir variante` bloqueado |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

> 🔴 **Esta lista tem que ser PODADA quando a fonte for varrida.** Em 23 set 2026 a
> `Segmentação Grupos` ainda constava aqui nos 48 arquivos **depois de já ter
> alimentado 34 `institucional.md`** — e isso me fez repetir a busca.
> **Falso-negativo aqui custa token e contradiz a razão de existir do diário.**
> **Varreu? Tire daqui e registre na § 3, no mesmo commit.**

| Fonte | Endereço | O que deve trazer |
|---|---|---|
| ⚠ **`Operação de Clientes / ARQUIVO / Área de CX / Documentação CX`** | base `collection://3a26629f…`, **30 documentos, já listados por SQL** | 🔺 **corrigido:** eu tinha escrito o caminho SEM o `Arquivo`. **Está arquivado** — não tem o mesmo peso dos outros acervos. Sub-páginas não abertas: `Mapeamento da Conta - Puket`, `- Caedu`, **`Análise das Similaridades e Diferenças entre contas`**, `Devolutivas para Sandro`, `Indicadores e Rotinas de Acompanhamento` |
| 🔴 **`Health Score`** — dashboard **Looker** | base `Documentação CX` | **a métrica de saúde de conta que falta no corpus.** ⚠ **`Em Construção` desde fev/2025** |
| **`Planilha de Cardápio de Dores e KRs`** e `Template Planilha Plano Sucesso Cliente (KRs)` | base `Documentação CX`, Excel | 🟢 **cardápio de dores é exatamente o que a varredura vem catalogando cliente a cliente** |
| **`Plano de Gestão de Risco - Legado`** | base `Documentação CX`, `Versão 1`, `Done`, **dois owners** | ⚠ **é plano de risco do uFlow, e o corpus não o cita** |
| **`Migração e Padronização de Ferramentas de Trabalho`** | base `Documentação CX`, `Done` em abr/2025 | ⚠ **provável decisão que descontinuou Kanbanize e Linear** — hipótese, não abri |
| **`[CX] Estrutura de Pesquisa de Satisfação Trimestral`** e `Pesquisa Satisfação Agosto/24` | base `Documentação CX`, **Validados** | 🟢 **o CSat tem estrutura definida e pelo menos uma rodada** — eu listava como fonte solta |
| 🔴 **`Setup - PLM / CLIENTES` — OITO clientes não tocados** | `bf9891a8…` — RESERVA · BAW · OFICINA · VIX · StudioZ · PUKET · CAEDU · NK Store (a NV foi lida) | **setup de PLM por cliente.** ⚠ **NK STORE e VIX têm um SEGUNDO endereço que eu não tinha aberto** |
| **`Setup - PLM` — seção `Automações`, 8 páginas** | `Gerador de Referencia`, `Calculadora de campos`, `Ações com mais de uma expression`, `Projeto Puket - Kanban de Estilo NOVO`… | 🟢 **o catálogo das automações com ID** (`#1136`, `#1175`, `#989`) que o playbook da Cambos cita e não explica |
| **`Setup - PLM` — seção `Configs da Conta`, 18 páginas** | uma por `entity_config`, **duas nominais**: `[Vivara] Alterar nomes tecido/aviamento` e `[NV] Bloquear Alteração de Elementos da Tabela na FT` | **o procedimento de cada config** — e `Habilitar Usuários específicos a gravar tabela de medida` é o `scopable: user` na prática |
| **`Setup - PLM` — seção `Traduções`, 4 páginas** | `Abas e nomes de campos da Ficha técnica` · `Campos Custom` · `Impressão` · `Nomes de Modelos` | 🟢 **onde o apelido interno é OPERADO** — fecha a cadeia princípio → config → procedimento |
| 🔴 **`Como é o processo de integração?` e `Logs e integração (Google Cloud Watch)`** | `e6ca5775…` e `eb6f3a42…`, em `Setup - PLM` | **a dor de integração atravessa CAEDU, VIX, Moda Objetiva e Luiza Barcelos — e o processo está escrito aqui** |
| **`Ficha de Produto` e suas 7 sub-páginas** | `c3deb3dd…`, em `Setup - PLM / Templates de Formulário` | **como se bloqueia edição de aba e se libera campo por usuário** dentro do template |
| **PDF `manual_do_permissionamento_umode_(5).pdf`** | anexo na página `Setup - PLM` | ⚠ **versão 5 do manual.** Li a página do Notion; **o PDF pode divergir** |
| 🔴 **`playbook.umode.app`** | página `Engenharia de Software` (`dc5980a5…`), em `uMode Geral` — editada em **07/09/2026** | 🔴 **TERCEIRO domínio de documentação**, com `docs.umode.app` e `documentacao.umode.tech`. A fonte diz que é *de atendimento obrigatório para todos os membros do time* |
| Teamspace **`AGENTES E PROJETOS`** | `Templates & Boas Práticas` · `Projeto: Mentoria (João Risoléo)` · `Metodologia MBS` | 🔴 **os MENTORADOS que o Vinícius anunciou já têm acervo aqui** — e há um `Playbook de Engenharia — DUMP Técnico Completo` |
| Pasta **`Documentação Homologada`** dentro do cliente | vista na Cambos (`4d25eb62…`) | ⚠ **o nome implica um estado de validação** — não sei quantos clientes têm essa pasta nem o que mais há nela |
| `Playbook Onboarding Novas Marcas` | `uMode Geral / Produtos / histórico` (`7ab68b33…`) | **FASE 1 | Planejamento de Implantação** e cronograma padrão — o processo de implantação escrito |
| `Planos de Quarters OPS` | `uMode Geral / Operação de Clientes` (`7ac7b3c6…`) | OKR de operação, com KR de medição de satisfação de cliente |
| Relação `Atendimento 2024` | `collection://c82a689c-…` | quem atendeu em 2024 — o corpus só tem 2025. 🔴 **É `relation`: consultar como valor devolve vazio.** Resolver as páginas-alvo, como se fez com `Segmentação Grupos` em 23 set 2026 |
| Campo `Participantes` das 1.161 reuniões | IDs de usuário do Notion | **presença nominal com data** — a melhor fonte de pessoa ativa |
| As 1.153 atas ainda não abertas | base de reuniões | conteúdo — **e varredura de credencial** |
| **Gist** — o chat da plataforma | canal oficial de dúvida de usabilidade | conversa de suporte, por cliente |
| 🟢 `Controle de Acessos de Usuários` — **LIDA em 22 set 2026** | `uModers / Vinícius Risoleo / Assunto | Ferramenta` | deu o **modelo de dados do uFlow**; ⚠ **falta rodar as queries** e trazer o **engajamento por conta** |
| **`Databases / Processos mapeados`** | base própria do Notion | playbooks de processo — inclui o de **limite contratado de usuários** |
| **`Databases / Demandas de Clientes`** | base própria do Notion | ⚠ **é a mesma base das 999 demandas, ou outra?** Não confirmei |
| **`Operation Hub`** e o domínio `documentacao.umode.tech` | `Operação de Clientes` | 🔴 **segundo domínio de documentação**, além do `docs.umode.app` |
| Página `Ficha de Produto` e suas **7 sub-páginas de permissionamento em template** | `c3deb3dd…` — citada pelo Manual do Permissionamento | **como se bloqueia edição de aba e se libera campo por usuário** dentro da ficha |
| `umode.app/admin/j3_entity_configs` | painel administrativo de **produção** — não acessado | 🔴 **quais `entity_configs` existem e em que conta estão ativas.** O Manual lista 20 como exemplo, não como catálogo |
| **Grupos de WhatsApp** | fora de qualquer sistema | operação real — a Reserva tem 9 mapeados |

## Governança

### Quem pode alterar este documento
**A § 1, § 2 e § 3 se escrevem a cada varredura**, pelo script. Pendência resolvida **não**
**se apaga: muda de estado**, para o histórico não se perder.

### Quando ler
🔴 **Antes de varrer este cliente. Sempre.** É o que impede repetir busca já feita.

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Cliente:** `VIX` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
