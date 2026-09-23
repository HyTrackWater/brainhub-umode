# Moda Objetiva · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o Moda Objetiva?" e
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
| 1 | 🆕 **10 perfis** — `Admin`, `Estilo`, `Compras`, `Compras MP`, `Desenvolvimento de Produto`, `Engenharia`, `Estamparia`, `PCP`, `Planejamento` e **`Consulta`**. 🔴 **`Objetiva - Consulta` é o primeiro perfil explicitamente somente-leitura do corpus** — quase tudo 🟡. Com o `NV - View`, são **dois casos**. | `T2` | decisão sobre a grade de áreas |
| 2 | 🟢 **`Fale com o Suporte`, `Manual` e `Base de Importação` LIBERADOS** para os 9 perfis operacionais. **Segundo cliente com `Manual` liberado**, com a Cambos — e os dois últimos vinham destacados em vermelho na fonte. | `T2` | — |
| 3 | 🔴 **Oito linhas estão 🔴 para os DEZ perfis, inclusive o Admin:** `Tabela Dinâmica`, `Coordenado`, `Estampa`, `Composição de Custo`, `Ficha Técnica Base`, `Tag`, `Campo Personalizado` e `Salvar como Ficha Técnica Base`. ⚠ **Bloqueio para todo mundo não é permissão — é funcionalidade DESLIGADA.** O corpus não distingue as duas coisas. | `T2` | decisão de produto |
| 4 | 🆕 **Abas que nenhum outro cliente lido tem:** `Variântes`, **`EAN`**, `Logística e Fiscal`, `Quantidade Grade Tam.`, `Composição`, `Estampas`. 🟢 **`Variântes` é aba própria e liberada aqui** — contraste direto com a dor de variante de cinco clientes. | `T2` | — |
| 5 | 🆕 **`Mapa > Configuração`, `Mapa > Filtro` e `Mapa > Exibição` são linhas separadas** — granularidade de sub-permissão que só este cliente tem. **Na Recco, `Mapa de Coleção > Exibições` está bloqueado até para o Admin.** | `T2` | — |
| 6 | 🔴 **`Grupo` é item de Cadastro aqui**, liberado só para `Planejamento`. ⚠ **`Grupo` é exatamente o nível que a CAEDU pede desde 16/09/2025** (`Griffe › Linha › Grupo › Subgrupo`). **Existe, e está em pé em outro cliente.** | `T2` | conferência com o desenho da Loungerie |
| 7 | 🔴 **A página termina com link para uma PLANILHA GOOGLE `Planilha de e-mail dos usuários`** (`docs.google.com/spreadsheets/d/1pflncdc3prZKN0pTXWlzbYFAyr6UG3Ab`). **Fonte externa com dado pessoal, não varrida.** ⚠ **É o equivalente da base `Usuários` da NK STORE, só que fora do Notion.** | `T2` | acesso à planilha |
| 8 | 🔴 **O `Status` diz `Operação Assistida` e a `Etapa` diz `Onboarding`.** | `T2` | **Qual dos dois manda?** |
| 9 | ⚠ **`Objetiva` na plataforma × `Moda Objetiva` no CRM** — mesmo cliente, confirmado pelo Vinicius em 03 ago 2026; registrado como alias. | `T2` | nada — resolvido |

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
| 1 | A página de perfil termina apontando para uma **planilha Google com os e-mails dos usuários**. **Posso abrir?** É o equivalente da base `Usuários` da NK STORE, só que fora do Notion. | `T2` | é a fonte de pessoa deste cliente | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o Moda Objetiva

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
| **22 set 2026** | `295b1d38…` | 🟢 **bloco `Pessoas` PREENCHIDO** — 6 pessoas, e um bloco **`Stakeholders` que só esta conta tem**; 🔴 **quatro toggles com título e sem conteúdo**; sub-páginas `Dossie Acompanhamento Integração` e **`Regras de Negócios da Conta`** | ⚠ **não** — 3 sub-páginas e 2 databases inline não abertos |

### 3.3 · Sub-páginas e documentos deste cliente já abertos

> 🔴 **NÃO reabrir.** O que saiu daqui já está na seção 2.

| Quando | O quê | Endereço | O que saiu |
|---|---|---|---|
| **23 set 2026** | `Documentos Implantação uFlow › Perfil de Usuário e Permissionamentos - Moda Objetiva` | `38bb1d38…` | **10 perfis**, um deles somente-leitura (`Consulta`); 🟢 `Fale com o Suporte`, `Manual` e `Base de Importação` liberados; abas `Variântes`, `EAN`, `Logística e Fiscal`; `Grupo` no Cadastro; **link para planilha Google com e-mails — não aberta** |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

| Fonte | Endereço | O que deve trazer |
|---|---|---|
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
| 🔴 **`uMode Geral / uFlow / Documentação de Setup - PLM / CLIENTES`** | segundo acervo de documentação por cliente, fora do `Mapa de Clientes` | **setup de PLM por cliente** — achado em 22 set 2026, jamais tocado |
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

**Cliente:** `Moda Objetiva` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
