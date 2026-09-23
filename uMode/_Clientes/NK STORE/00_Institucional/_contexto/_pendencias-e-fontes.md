# NK STORE · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o NK STORE?" e
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

| O que | Onde | Estado |
|---|---|---|
| Credencial de produção do **Linx** (usuário, senha, IP, porta, banco) | Notion — página do cliente, toggle `Documentos › Conexão com Linx` | 🚨 **exposta, não rotacionada** |

> 🚨 **O valor não foi replicado em lugar nenhum do corpus** — `T0`.
> **A rotação é ação do Vinicius.** ⚠ Pode já estar inativa; **rotacionar mesmo assim**
> é mais barato que descobrir que não estava.

## 1-bis · 🔴 O que eu NÃO consegui ler

> **Pedido do Vinícius em 22 set 2026:** *sobre suspeitas de blocos, sempre tenha atenção e me indique, porque temos que ter a garantia de que tudo que está varrendo está conseguindo tirar proveito de tudo o que podemos*.
>
> 🔴 **Bloco que não renderiza NÃO é bloco vazio.** Na Luiza Barcelos, 17 blocos ilegíveis escondiam **o único Representante Legal da conta** e o cargo do Gerente de Inovação e Tecnologia. **Eu cheguei a chamar isso de falta de acesso, e estava errado** — ver `protocolo-varredura-cliente.md` § 11.

| Onde | Quantos | O que era | Estado |
|---|--:|---|---|
| `Plano de Sucesso do Cliente` | 1 | incorporação do Google Drive | 🔴 **aberto** — não é Notion, é arquivo do Drive |

**O contorno que funciona:** pedir ao Vinícius **só aquele trecho**, copiado e colado. **Barato, e o que vier entra como fonte normal, com procedência.**

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🔴 **A base `Usuários` da página de perfil tem 30 linhas, TODAS PREENCHIDAS** — nome, e-mail corporativo, `Perfil do Usuário`, `Departamento NK` e `Status`. 🟢 **É a mesma base que na Lenny Niemeyer está VAZIA**, com o mesmo schema. **Responde a pendência que eu tinha deixado aberta lá: sim, outro cliente tem a base preenchida.** | `T2` | — já virou ficha de pessoa |
| 2 | 🔴 **`INATIVAR` é usado como valor de `Departamento NK` em 5 das 30 linhas.** ⚠ **Não é departamento — é instrução operacional escrita no campo de área.** O campo foi sequestrado para virar fila de tarefa, e com isso **a área dessas 5 pessoas se perdeu.** | `T2` | decisão de modelagem + conferência com o cliente |
| 3 | 🔴 **Os perfis da MATRIZ e os perfis da BASE não batem.** A matriz tem `NK - Admin`, `NK - Time`, `NK- Estilo Master`, `Nk Compras Master`, `Nk Modelagem`, `NK Compras` e `Fornecedor`. A base usa `NK - Admin`, `NK - Estilo`, `NK - Compras`, `NK - Modelagem` e **`NK - PCP`**. 🔴 **`NK - PCP` existe na base e NÃO existe na matriz — são 7 pessoas sem permissão documentada.** E `NK - Time` e `Fornecedor` não têm nenhum usuário. | `T2` | conferência com o atendimento |
| 4 | ⚠ **A grafia dos perfis na matriz é inconsistente na própria fonte:** `NK - Admin`, `NK- Estilo Master`, `Nk Compras Master`, `NK Compras`. **Três jeitos de escrever o mesmo prefixo.** | `T2` | — |
| 5 | 🔴 **Os 4 perfis de função da matriz (`Estilo Master`, `Compras Master`, `Modelagem`, `Compras`) têm valor em DUAS linhas só** — `Importação` e `Integração`. **Todo o resto da matriz está vazio para eles.** ⚠ **Matriz incompleta ≠ permissão negada, e eu não sei qual dos dois é.** | `T2` | conferência |
| 6 | 🆕 **Duas colunas de VALIDAÇÃO datada dentro da matriz** — `Validação NK - Admin 04/12` e `Validação NK - Time 04/12`, com ✔️, ✖️ e comentários (*não pode aparecer os 3 pontinhos*, *incluir ação de cancelado*, *travar edição de grade qnd tiver tabela*). 🟢 **É homologação com o cliente registrada na própria matriz — o único caso no corpus.** | `T2` | — vale virar padrão |
| 7 | 🔴 **`Fale com o Suporte` BLOQUEADO para `NK - Admin` e `NK - Time`.** **Terceiro cliente bloqueado**, com Luiza Barcelos e Lenny. | `T2` | — |
| 8 | 🆕 **`Integração Linx` é aba da ficha de produto aqui**, 🟡 somente visualizar. ⚠ **Liga direto com o risco de credencial Linx deste mesmo cliente.** | `T2` | — |
| 9 | 🆕 **A aba de chat se chama `Chat NK`** — nome do cliente no rótulo. Com o `Chat NV` da NV, são **dois casos**; Moda Objetiva e Recco usam `Chat` seco. **É customização de rótulo, não padrão.** | `T2` | — |
| 10 | 🔴 **`nelson tadeu` entra pelo e-mail `expedicao2@nkstore.com.br`** — **caixa funcional, não nominal**, com pessoa nomeada atrás. ⚠ **A chave de identidade aqui é de uma CAIXA**, e o `2` sugere que existe uma `expedicao1`. | `T2` | conferência |
| 11 | ⚠ **Duas `Cristina`, duas `Vanessa` e duas `Julia` na mesma base**, distintas pelo e-mail. 🔴 **A ficha `cristina.md`, vinda da base de demandas, NÃO pôde ser casada** — o gerador parou e avisou em vez de sobrescrever. | `T2` | **pergunta registrada** |
| 12 | ⚠ **`kemely.md` (demandas) × `kemelly.fernandes@` (base): um `l` de diferença.** **NÃO fundi — uma letra não é prova.** Mesmo caso de `silvia-shirlei-dias` × `silvia.nascimento@`. | `T2` | **pergunta registrada** |
| 13 | ⚠ **Uma linha está DUPLICADA na base**: `Sam` / `sam.santos@`, mesma data, duas vezes. | `T2` | limpeza na fonte |
| 14 | 🔴 **Callout `Documentação tech →` aponta para `6d0379fa…`** — **a MESMA página técnica citada na Recco**. Página compartilhada entre clientes, **não varrida**. | `T2` | tempo de varredura |
| 15 | 🚨 **Credencial de produção do Linx em TEXTO CLARO** na página do cliente, toggle `Documentos › Conexão com Linx`: usuário, senha, IP, porta e nome do banco. **O valor não foi replicado em lugar nenhum do corpus.** | `T0` | 🚨 **rotação da chave — ação do Vinicius** |
| 16 | 🔴 **CPF e telefone pessoal de dois representantes legais** na mesma página. **Nada entrou no corpus** — registro que existe e onde. | `T0` | nada — é tratamento |
| 17 | 🔴 **8 das 13 pessoas com cargo nunca abriram demanda** — incluindo as **duas diretoras do projeto** (Regiane Konopka, Merchandising; Stella Sunaga, Estilo). | `T2` | nada — já corrigido, as fichas existem |
| 18 | ⚠ **`Merchandising`, `Curadoria` e `Oficina` são etapas do processo com dono, e não existem na grade canônica de 14 áreas.** Aqui **não são apelido.** | `T2` | decisão sobre a grade de áreas (item 234 — `15_Producao-Interna`) |
| 19 | ⚠ **11 das 24 pessoas seguem sem cargo** — as que vieram só da base de demandas e não aparecem no toggle `Pessoas` da página. | `T2` | preenchimento pelo atendimento |
| 20 | 🆕 **`uBuy` aparece como oportunidade** (*Follow Up de Entregas → Pedidos de Compras*) e **não está nos 7 módulos nem nas 16 Soluções.** | `T2` | decisão sobre o portfólio |

### 2.1 · 🔴 Perguntas que só o Vinícius responde

> **Uma pergunta só entra aqui quando NENHUMA fonte pode respondê-la.** Dúvida que
> uma fonte responde não é pergunta — **é varredura que falta fazer**, e vai para a § 4.
>
> 🔴 **Estas linhas são colhidas automaticamente** para a lista consolidada em
> [`_perguntas-para-o-vinicius.md`](../../../../00_Institucional/_contexto/_perguntas-para-o-vinicius.md),
> que ele responde **por áudio ou por transcrição de reunião**. Ver
> [`protocolo-perguntas-ao-vinicius.md`](../../../../00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md).

| # | Pergunta | Tier | Por que importa | Estado |
|--:|---|:-:|---|---|
| 1 | Há **duas `Cristina`** na base de usuários da NK STORE (`cristina@` em Compras, `cristina.amorim@` em Modelagem) e **uma ficha `cristina.md`** vinda da base de demandas, que traz só o primeiro nome. **Qual das duas abriu as demandas?** | `T2` | 🔴 **o gerador PAROU e avisou em vez de sobrescrever** — sem a resposta, ficam duas fichas para uma pessoa ou uma ficha para duas | aberta |
| 2 | A base tem **`kemelly.fernandes@`** e o corpus tem a ficha **`kemely.md`**, um `l` de diferença. E tem **`silvia.nascimento@`** contra **`silvia-shirlei-dias.md`**. **São as mesmas pessoas?** | `T2` | **não fundi — uma letra não é prova** | aberta |
| 3 | **5 das 30 linhas têm `Departamento NK = INATIVAR`.** É instrução pendente ou já foi executada? E **qual era a área real dessas pessoas antes de o campo ser sequestrado?** | `T2` | são 5 pessoas sem área no corpus | aberta |
| 4 | A matriz de permissão **não tem o perfil `NK - PCP`**, mas **7 pessoas o usam**. E os perfis `NK - Time` e `Fornecedor`, que a matriz detalha, **não têm nenhum usuário**. **Qual dos dois documentos está velho?** | `T2` | 7 pessoas sem permissão documentada | aberta |
| 5 | 🚨 **A credencial de produção do Linx está em texto claro na página do cliente. Foi rotacionada?** | `T0` | exposição ativa até prova em contrário | aberta |
| 6 | `Merchandising`, `Curadoria` e `Oficina` são etapas do processo com dono e não existem na grade de 14 áreas. **Viram área canônica, subárea, ou apelido?** | `T2` | é o mesmo tema do `15_Producao-Interna` | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o NK STORE

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
| **22 set 2026** | `0f24dfbe…` | **13 pessoas com cargo e área**; processo `Planejamento → Estilo → Compras/Merchandising → PCP → Oficina`; dores mapeadas; **`uBuy`** como oportunidade; 🚨 **credencial de produção em texto claro** | ⚠ **não** — 1 bloco não abriu (`Plano de Sucesso do Cliente`) |

### 3.3 · Sub-páginas e documentos deste cliente já abertos

> 🔴 **NÃO reabrir.** O que saiu daqui já está na seção 2.

| Quando | O quê | Endereço | O que saiu |
|---|---|---|---|
| **23 set 2026** | `Documentos › Perfil de Usuário e Permissionamentos` | `0385f372…` | 7 perfis + **2 colunas de validação datada (04/12)**; 🔴 `Fale com o Suporte` bloqueado; `Integração Linx` e `Chat NK` como abas; **base `Usuários` inline com 30 linhas PREENCHIDAS** — virou 28 fichas de pessoa |
| **23 set 2026** | base `Usuários` (inline na página de perfil) | `collection://1b5b1d38-e768-80b0-aaac-000b33b9657a` | 30 linhas: `Nome` · `E-mail` · `Perfil do Usuário` · **`Departamento NK`** · `Status`. **Consultada por SQL, linha a linha.** |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

| Fonte | Endereço | O que deve trazer |
|---|---|---|
| 🔴 **`Setup - PLM / CLIENTES` — OITO clientes não tocados** | `bf9891a8…` — RESERVA · BAW · OFICINA · VIX · StudioZ · PUKET · CAEDU · NK Store (a NV foi lida) | **setup de PLM por cliente.** ⚠ **NK STORE e VIX têm um SEGUNDO endereço que eu não tinha aberto** |
| **`Setup - PLM` — seção `Automações`, 8 páginas** | `Gerador de Referencia`, `Calculadora de campos`, `Ações com mais de uma expression`, `Projeto Puket - Kanban de Estilo NOVO`… | 🟢 **o catálogo das automações com ID** (`#1136`, `#1175`, `#989`) que o playbook da Cambos cita e não explica |
| **`Setup - PLM` — seção `Configs da Conta`, 18 páginas** | uma por `entity_config`, **duas nominais**: `[Vivara] Alterar nomes tecido/aviamento` e `[NV] Bloquear Alteração de Elementos da Tabela na FT` | **o procedimento de cada config** — e `Habilitar Usuários específicos a gravar tabela de medida` é o `scopable: user` na prática |
| **`Setup - PLM` — seção `Traduções`, 4 páginas** | `Abas e nomes de campos da Ficha técnica` · `Campos Custom` · `Impressão` · `Nomes de Modelos` | 🟢 **onde o apelido interno é OPERADO** — fecha a cadeia princípio → config → procedimento |
| 🔴 **`Como é o processo de integração?` e `Logs e integração (Google Cloud Watch)`** | `e6ca5775…` e `eb6f3a42…`, em `Setup - PLM` | **a dor de integração atravessa CAEDU, VIX, Moda Objetiva e Luiza Barcelos — e o processo está escrito aqui** |
| **`Ficha de Produto` e suas 7 sub-páginas** | `c3deb3dd…`, em `Setup - PLM / Templates de Formulário` | **como se bloqueia edição de aba e se libera campo por usuário** dentro do template |
| **PDF `manual_do_permissionamento_umode_(5).pdf`** | anexo na página `Setup - PLM` | ⚠ **versão 5 do manual.** Li a página do Notion; **o PDF pode divergir** |
| 🔴 **`playbook.umode.app`** | página `Engenharia de Software` (`dc5980a5…`), em `uMode Geral` — editada em **07/09/2026** | 🔴 **TERCEIRO domínio de documentação**, com `docs.umode.app` e `documentacao.umode.tech`. A fonte diz que é *de atendimento obrigatório para todos os membros do time* |
| Teamspace **`AGENTES E PROJETOS`** | `Templates & Boas Práticas` · `Projeto: Mentoria (João Risoléo)` · `Metodologia MBS` | 🔴 **os MENTORADOS que o Vinícius anunciou já têm acervo aqui** — e há um `Playbook de Engenharia — DUMP Técnico Completo` |
| **`Operação de Clientes / Área de CX / Documentação CX / Mapeamento de Contas`** | acervo por cliente | 🔴 **TERCEIRO acervo de documentação por cliente**, com o `Mapa de Clientes` e o `Setup - PLM`. A Puket tem uma página lá |
| Pasta **`Documentação Homologada`** dentro do cliente | vista na Cambos (`4d25eb62…`) | ⚠ **o nome implica um estado de validação** — não sei quantos clientes têm essa pasta nem o que mais há nela |
| `Playbook Onboarding Novas Marcas` | `uMode Geral / Produtos / histórico` (`7ab68b33…`) | **FASE 1 | Planejamento de Implantação** e cronograma padrão — o processo de implantação escrito |
| `Planos de Quarters OPS` | `uMode Geral / Operação de Clientes` (`7ac7b3c6…`) | OKR de operação, com KR de medição de satisfação de cliente |
| Relação `Segmentação Grupos` | `collection://a4103fe2-…` | grupo/tier comercial do cliente |
| Relação `Atendimento 2024` | `collection://c82a689c-…` | quem atendeu em 2024 — o corpus só tem 2025 |
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

**Cliente:** `NK STORE` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
