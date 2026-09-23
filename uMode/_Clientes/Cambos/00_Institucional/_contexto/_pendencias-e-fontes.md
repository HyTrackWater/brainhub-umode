---
aliases:
  - "Cambos · Pendências e fontes varridas"
---
# Cambos · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o Cambos?" e
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

| Onde | Quantos | O que era | Estado |
|---|--:|---|---|
| `Plano de Sucesso do Cliente` | 1 | incorporação do Google Drive | 🔴 **aberto** — não é Notion, é arquivo do Drive |

**O contorno que funciona:** pedir ao Vinícius **só aquele trecho**, copiado e colado. **Barato, e o que vier entra como fonte normal, com procedência.**

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🟢 **Existe um PLAYBOOK de PLM da Cambos, v1.1, e ele foi gerado a partir de TRANSCRIÇÕES DE TREINAMENTO, com IA.** O título diz: `Treinamento > IA + Doc Laura`. 🔴 **É exatamente o caminho que o Vinícius anunciou para as ~50 transcrições da CAEDU — e já rodou uma vez, aqui.** | `T2` | — vale virar referência de método |
| 2 | 🔴 **A Cambos tem DUAS operações geográficas:** `Desenvolvimento SP` (cadastro e `Produto Original`) e `Desenvolvimento MG` (`Aprovações das Pilotos`, lacres, pesos). **O campo `Liberado para Desenv. MG` é o gatilho entre as duas.** ⚠ **O corpus não tinha nada disso.** | `T2` | — |
| 3 | 🔴 **A Cambos é FORNECEDORA de marcas — a `Riachuelo` aparece como exemplo de filtro de *cliente* dentro da conta dela.** 🟢 **Isso explica `Novo Pedido (só a Cambos tem)`, o perfil `Atacado` e a natureza do negócio.** ⚠ **O corpus tratava a Cambos como marca.** | `T2` | **conferência — muda a classificação da conta** |
| 4 | 🆕 **Cinco AUTOMAÇÕES com ID numérico:** `#1136` (descrição concatenada de Modelagem+Gênero+Tipo+Tamanho+Detalhe), `#1175` (cria a Piloto automaticamente), `#1134` (valida pré-requisitos de integração), `#989` (validação técnica ao entrar em coluna do workflow), `#1135` (limpeza da última integração SPI). 🔴 **O corpus não tinha NENHUM ID de automação da plataforma.** | `T2` | — vale procurar o catálogo dessas automações |
| 5 | 🔴 **Dois códigos convivem no mesmo produto:** `Código uMode` (gerado pela plataforma, vale até a aprovação do orçamento) e `Código SPI` (gerado pelo ERP). **E há uma TRAVA: `Modelagem`, `Tipo`, `Gênero` e `Tamanho` ficam travados depois que o Código SPI nasce.** | `T2` | — |
| 6 | 🔴 **Na integração, só a ÚLTIMA VARIANTE é enviada ao ERP.** ⚠ **É perda de informação por desenho**, e liga direto com a dor de variante de cinco clientes. | `T2` | conferência |
| 7 | 🟢 **`Exibições Compartilhadas` só para Admin; usuário comum salva em *Somente Eu*.** 🔴 **Casa exatamente com a config `hide_map_template` do Manual do Permissionamento** — primeira vez que uma regra de playbook e uma `entity_config` se encontram no corpus. | `T2` | — |
| 8 | 🆕 **`Lacre`** — identificador da amostra física vinculada à aprovação técnica; o sistema registra **até 6**. 🆕 **`Produto Original`** — acervo de bases de modelagem mantido pelo Desenvolvimento SP. **Dois termos de moda que o corpus não tinha.** | `T2` | — |
| 9 | ⚠ **O playbook fala de 2 perfis (`Comercial` e `Admin`); a matriz de permissão tem 5.** **Não sei qual dos dois está desatualizado.** | `T2` | conferência |
| 10 | ⚠ **O próprio playbook lista TRÊS pendências de validação em aberto** (§7): relatórios de Gestão de Coleção e Tarefas liberados para o perfil operacional; migração dos `Produtos Originais` que estão em planilha; e se o gatilho `#1175` vale para todo tipo de produto ou **só jeans**. **Escritas em 23/03/2026 e sem dono.** | `T2` | **pergunta registrada** |
| 11 | 🔺 **A Cambos QUEBRA a hipótese do `Manual` bloqueado.** Eu tinha escrito *dois de dois: hipótese forte* com VIX e Luiza Barcelos. **Na Cambos, `Manual` e `Base de Importação` estão LIBERADOS para os 5 perfis.** 🔴 **Dois bloqueados, um liberado: não é padrão, é configuração por cliente.** ⚠ **E na Oficina a linha nem existe.** | `T2` | nada — hipótese derrubada |
| 12 | 🆕 **A integração SPI tem TELAS PRÓPRIAS no uFlow**, com prefixo `[SPI]`: `Aviamentos Pendentes`, `Cores Pendentes`, `Banhos Pendentes`, `Fornecedores Pendentes`, `Produtos Pendentes`. 🔴 **A plataforma tem tela feita sob medida para o ERP de UM cliente.** | `T2` | — muda a leitura do que é ‘integração’ |
| 13 | 🔴 **`Novo Pedido (só a Cambos tem)`** — funcionalidade exclusiva de um cliente, **e está 🔴 bloqueada para os cinco perfis**. ⚠ **Construída, exclusiva, e desligada.** | `T2` | conferência |
| 14 | 🆕 **O cliente RENOMEOU as abas da ficha de produto**, em caixa alta e com vocabulário próprio: `COSTURA E BORDADO`, `TAMANHOS PILOTO (Grade)`, `QTD PARA PILOTAR (Lote)`, `FABRICAÇÃO (Fornecedor)`, `APROVAÇÕES DA PILOTO`, `ORIGINAL`, `INTEGRAÇÃO SPI`. **É o *apelido interno* da Arquitetura V1 acontecendo de verdade** — o termo canônico entre parênteses, o do cliente na frente. | `T2` | — |
| 15 | 🆕 **Há uma `Planilha com os usuários ativos`** no Google Sheets, linkada no topo da página. ⚠ **Não aberta** — pode ser a lista de pessoas que falta. | `T2` | tempo de varredura |
| 16 | ⚠ **O mesmo perfil tem dois nomes na mesma página:** `Cambos - Time Desenvolvimento` na primeira tabela e `Cambos - Desenvolvimento` na segunda. **Não escolhi um.** | `T2` | conferência |
| 17 | 🟢 **`Fale com o Suporte` liberado para os 5 perfis** — quarto cliente. **O placar fica 2 bloqueados (Luiza Barcelos, Lenny) × 3 liberados (VIX, Oficina, Cambos).** | `T2` | pergunta já registrada |
| 18 | 🔴 **`Tabela Dinâmica`, `Composição de Custo`, `Coordenado`, `Estampa`, `Tag`, `Pack` e `Campo Personalizado` estão bloqueados para TODOS os perfis.** ⚠ **Mesmo conjunto que aparece bloqueado na Oficina Reserva** — dois casos, pode ser função que ninguém usa. | `T2` | conferência de produto |
| 19 | 🟢 **Bloco `Pessoas` PREENCHIDO — segundo caso da carteira**, junto da NK STORE. 5 pessoas com cargo: Tony Stefan Lopes (Gerente Geral/Diretor de Operação da Fábrica), Valter (Head Financeiro), Fabiane Sayuri (Desenv. de Produtos), Carolina (Estilista), Gustavo Paiva (Head de Tecnologia). | `T2` | nada — executado |
| 20 | 🟢 **RESOLVIDA a ambiguidade `Fabi e Carol`** — a célula da base de demandas que eu me recusei a desmembrar. A página diz que o líder do projeto é *Tony e Fabi*, e lista **Fabiane Sayuri** e **Carolina**. **Ambiguidade resolvida com fonte, não com palpite.** | `T2` | nada |
| 21 | 🔴 **A Cambos FORNECE para a CAEDU** — e as duas são clientes da uMode. *Fornecem para Caedu, Marisa, etc.* **Dois clientes nossos numa relação fornecedor-cliente entre si, e o corpus os trata como ilhas.** | `T2` | decisão de modelagem — o isolamento de cliente é regra travada |
| 22 | 🔴 **A base diz ERP `SPI - Sistema próprio da Cambos` e a página diz DOIS:** `Totvs - Virtual Age` (comercial, **com pacote de APIs**) e `SPI` (produção). Mais `Banner` para pedido de atacado. **A base está incompleta.** | `T2` | correção na base |
| 23 | 🔴 **Relação contratual ambígua, registrada pela própria uMode:** *Relatórios: não detalhados no contrato porém subentendido entre 2-3 relatórios mediante a maturidade*. **Escopo subentendido é escopo em disputa.** | `T2` | conferência com o comercial |
| 24 | 🔴 **Atrito interno Sales×Ops registrado**, feedback do Sandro: *alinhar o que vendeu e o que operação vai tocar gerou desconforto... pode dar impressão que a empresa está desalinhada*. **É o único registro de atrito interno que o corpus tem.** | `T2` | — |
| 25 | 🆕 **Números de operação:** 140.000 peças/mês · 20 a 40 fornecedores · ~20 pessoas no desenvolvimento · **nota 6,0** para o processo atual · **10% de quebra de entrega** · 40% Magazine / 60% marca própria. **Segundo cliente com números**, depois da Oficina Reserva. | `T2` | — |
| 26 | ⚠ **~20 pessoas no desenvolvimento e o corpus tem 5 fichas.** | `T2` | a página nomeia 5; as outras 15 não estão em fonte nenhuma |
| 27 | 🆕 **`Trello` — oitava ferramenta**, usada pelo cliente para gestão do processo. Não está no enum `tool` do corpus. | `T2` | — |
| 28 | 🆕 **`IPSP`** aparece junto de `uPlan` como oportunidade. **Quinto nome de produto fora das duas listas**, com `uBuy`, `uPlan` e `uPick`. | `T2` | decisão sobre o portfólio |
| 29 | 🆕 **Segundo escopo desejado e NÃO contratado:** *trazer os clientes para dentro da plataforma para acompanhar o desenvolvimento*. **É oportunidade comercial nomeada, parada desde o kick off.** | `T2` | — |
| 30 | 🆕 **`Playbook Cambos | Treinamento > IA + Doc Laura`** — primeira documentação homologada com IA que o corpus vê. | `T2` | tempo de varredura |
| 31 | ⚠ **Duas contas na plataforma:** `Cambos` (7 usuários) e `Cambos - uFlow` (25). **É conta por módulo ou duplicidade?** | `T2` | pergunta registrada |
| 32 | ⚠ **Conteúdo T1 com autorização de uso pendente desde julho.** | `T1` | autorização do Vinícius |
| 33 | 🔴 **A fonte traz telefone e CPF de um diretor.** **Nada entrou no corpus** — registro que existe e onde. | `T0` | nada — é tratamento |

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
| 1 | Há duas contas na plataforma — `Cambos` (7 usuários) e `Cambos - uFlow` (25). **É conta por módulo, ou duplicidade?** | `T2` | define se `client_id` é mesmo único por cliente | **⚠ a distribuir** | aberta |
| 2 | O conteúdo T1 da Cambos está com autorização de uso pendente desde julho. **Libera?** | `T1` | trava registrada há mais de dois meses | **⚠ a distribuir** | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o Cambos

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
| **22 set 2026** | `d6d48327…` | 🟢 **bloco `Pessoas` PREENCHIDO** (5 pessoas com cargo) + **Discovery de Sales com 10 perguntas respondidas**: 140 mil peças/mês, 20 a 40 fornecedores, ~20 pessoas no desenvolvimento, **nota 6,0** para o processo atual, 10% de quebra de entrega; 🔴 **fornecem para CAEDU e Marisa**; `Trello`, `Banner`, `Totvs Virtual Age`, `Data Lake` | ⚠ **não** — 9 sub-páginas e 4 databases inline não abertos |

### 3.3 · Sub-páginas e documentos deste cliente já abertos

> 🔴 **NÃO reabrir.** O que saiu daqui já está na seção 2.

| Quando | O quê | Endereço | O que saiu |
|---|---|---|---|
| **23 set 2026** | `Documentação Homologada › Playbook Cambos \| Treinamento \> IA + Doc Laura` | `32cb1d38…` | **PLAYBOOK — SISTEMA PLM [CAMBOS] v1.1, 23/03/2026, gerado a partir de TRANSCRIÇÕES DE TREINAMENTO com IA**; SP × MG; cinco IDs de automação; trava SPI; `Lacre`; `Riachuelo` como cliente DA Cambos |
| **22 set 2026** | `Perfil de Usuário e Permissionamentos` | `1a7b1d38…` | 5 perfis; 🟢 **`Manual` e `Base de Importação` LIBERADOS** — o que derrubou minha hipótese; telas `[SPI]` feitas para o ERP do cliente; `Novo Pedido (só a Cambos tem)` bloqueado para todos; **abas da ficha renomeadas em caixa alta pelo cliente** |

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

**Cliente:** `Cambos` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
