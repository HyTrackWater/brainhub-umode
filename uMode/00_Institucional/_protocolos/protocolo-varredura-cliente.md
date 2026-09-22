# Protocolo — varredura e preenchimento de contexto de cliente

> Escrito em **21 set 2026** depois de fechar a **CAEDU** como caso de prova, e **revisado no mesmo
> dia depois da Puket** — que quebrou duas premissas generalizadas de um cliente só.
>
> Este protocolo existe para que os clientes restantes não exijam redescobrir o caminho.
> **Ordem importa** — ela foi determinada por onde a informação de fato está.
>
> ⚠ **Regra de manutenção deste arquivo:** toda regra aqui nasceu de **um** cliente. Uma regra
> confirmada em um caso é hipótese; só vira regra depois do segundo. As que ainda valem para um só
> caso estão marcadas **`(1 caso)`**.

## 0 · Antes de começar: a regra que evita o retrabalho

🔴 **Não use export.** O vault tem exports de Notion versionados em Git, e eles **estavam seis meses
desatualizados**. Na CAEDU isso significava: status errado, taxonomia de módulo errada, e quatro
clientes listados como vivos que já estavam em churn.

**Vá à base viva pelo MCP do Notion. Sempre.** O export serve para conferir histórico, nunca para
afirmar estado.

## 1 · A ordem de varredura

| # | Fonte | O que ela dá | Como chegar |
|---|---|---|---|
| 1 | **Base `Mapa de Clientes`** | status, módulos, ERP, dupla de atendimento, setor, cidade | `notion-query-data-sources` em `collection://ec041afd-fcee-44f8-83cb-223fca6f4108` |
| 2 | **Página do cliente** dentro da base | 🎯 **a tabela de usuários do PLM** — nome, e-mail, perfil, data | `notion-fetch` na `url` da linha do cliente |
| 3 | 🔴 **`Chamados & Atendimentos`** | **a dor real e recente**: tipo, status, e-mail do solicitante, detalhe | `collection://2c5b1d38-e768-805a-99b1-000b4da25cc4`, filtrando `Cliente` pela url do cliente |
| 4 | **`Mapeamento de Contas - <cliente>`** | AS IS, dores, fluxo por área, plano de ação | busca em `Operação de Clientes / Área de CX / Documentação CX` |
| 5 | **Sub-páginas da página do cliente** | Fornecedores, Playbooks, Manual, Onboarding→Ongoing | listadas no `<content>` da página |
| 6 | **Atas** em `Reuniões com o cliente` | marcos datados, pessoas nomeadas, decisões | idem |
| 7 | **vault `_Clientes/<slug>/`** | propostas, contratos, cronogramas, atas destiladas | `git show` na branch `governance/brainhub-v1.5` |
| 8 | **Repositório de integração** | confirma o ERP de verdade | `C:\Ambientes Virtuais\uMode-Integracoes\` |

## 2 · 🎯 O achado que destrava tudo

> **O perfil de acesso no PLM é o único vínculo pessoa↔área que existe em alguma fonte da uMode.**

E ele **governa permissão, não só rótulo**: na Puket, a pessoa do perfil `Importação` abriu chamado
pedindo **poder criar tarefas**. O perfil decide o que a pessoa faz, não só onde ela está.

### 🔴 Mas a convenção de nome do perfil é DE CADA CLIENTE

Este protocolo dizia, generalizando da CAEDU, que o padrão era `<Cliente>-<Área>`. **A Puket
derrubou isso:** lá os perfis são **nomes de função puros** — `Sourcing Nacional`, `Produto`,
`Estilo`, `Design`, `Qualidade`, `TEX`, `PCP`, `BI`, `Controladoria`, `Certificação`, `Projetos`,
`Importação`.

**Leia os perfis que existem antes de assumir qualquer padrão de nome.**

Na CAEDU, 93 usuários em 14 perfis mapearam assim **(1 caso — padrão prefixado)**:

| Perfil | → Área canônica |
|---|---|
| `<Cliente>-Estilo` | `02_Estilo-Criacao` |
| `<Cliente>-Produto` | `03_Desenvolvimento-de-Colecao` |
| `<Cliente>-Planejamento` | `01_Planejamento` |
| `<Cliente>-Modelagem` | `13_Modelagem` |
| `<Cliente>-Qualidade` | `04_Qualidade` |
| `<Cliente>-E-commerce` | `08_Ecommerce-Cadastro` |
| `<Cliente>-Geral` · `-Gerentes` · `-Admin` | **transversal — não derivável** |
| `Fornecedor` | externo · `06_Compras-Supply-Sourcing` |
| `Dono da Conta` | conta de serviço, **não é pessoa** |

Na Puket, 43 usuários em 13 perfis, **sem prefixo**, mapearam direto pelo nome da função —
com três casos que **não** se resolvem sozinhos e ficaram marcados:

| Perfil | Decisão |
|---|---|
| `TEX` | ⚠ sigla não explicada em nenhuma fonte — `[a preencher]`, **não inferir** |
| `Certificação` | → `04_Qualidade`, **provisório** |
| `Projetos` · `BI` | **transversais** — sem área canônica derivável |

**Isso preenche de uma vez:** a seção *Aliases de áreas* do `institucional.md`, a seção *Time do
projeto por área* do `pessoas.md`, e a seção *Pessoas desta área* de cada `contexto-area.md`.

### 🔴 E a cobertura de áreas é informação sobre o cliente

A grade de 14 áreas **não se preenche igual em dois clientes** — e a diferença diz como cada um se
organiza. Ambos têm 7 de 14, mas **não as mesmas 7**:

| | Caedu | Puket |
|---|:-:|:-:|
| Planejamento · E-commerce · Modelagem | ✅ | — |
| PCP · Design · Financeiro | — | ✅ |
| Estilo · Produto · Qualidade · Sourcing | ✅ | ✅ |

**Não trate a ausência como falta de dado até ter varrido as fontes.** Depois disso, ela é dado.

### ⚠ O domínio do e-mail também é dado

Na Puket, os 43 usuários se dividem em `@puket.com.br` (22), `@grupounico.com` (20) e
`@grupounico.hk` (1). **Puket é marca do Grupo Único** — a holding concentra suprimento, controle e
qualidade; a marca concentra criação e produto; e há sourcing em **Hong Kong**.
**Agrupe os domínios antes de escrever o `institucional.md`.** Pode não ser uma empresa só.

## 3 · As sete travas que a CAEDU revelou

**1 · Extrair por script, nunca transcrever.** 93 linhas de tabela transcritas à mão erram. Use
regex sobre o resultado salvo do `notion-fetch` e gere o markdown por script.

**2 · A página do cliente pode estourar o limite de resposta.** A da CAEDU tem 52 KB, e boa parte é
um ícone em base64. O resultado é salvo em arquivo — leia por fatia, e **pule direto ao `<content>`**.

**3 · PowerShell 5.1 lê `.ps1` sem BOM como ANSI** e destrói todo acento. Ao gerar script com
acentuação, **grave com UTF-8 BOM** ou ele quebra no parser.

**4 · Erros de digitação vêm da origem.** Na CAEDU: `Caedu- Planejamento` com espaço a mais,
`Caedu-Admim` por *Admin*, datas como `08/11/0202`. **Preserve e sinalize — corrigir é na fonte.**

**5 · A ausência de perfil é achado, não falha.** Sete das 14 áreas da CAEDU não têm perfil no PLM.
Isso **é** a informação: ou a área não existe no cliente, ou existe e não usa a plataforma.

**6 · Arquivo de área vazio ainda deve ser criado.** Com estrutura, com a lista de fontes varridas e
o que cada uma **não** trouxe, e com as perguntas a levar ao negócio.
> **A contagem de lacunas sobe, e isso é correto.** Na CAEDU foi de 691 para 743 — porque 56 lacunas
> que antes eram invisíveis passaram a ser endereçáveis. **Lacuna visível vale mais que cobertura
> aparente.**

**8 · Placeholder de template não é conteúdo. (Puket)**
A página da Puket tem um bloco *"Perfis de Acesso e Setor Operacional"* que parece uma taxonomia —
mas cada item vem seguido de `(EX: ...)`. **São exemplos do template, nunca preenchidos.** O mesmo
vale lá para `Marca`, `Submárcas`, `ERP`, `Workflow`, `Validações`, `Restrições`, `Link do Miro`:
todos vazios ou com `#` / `##` de placeholder.
> **Procure `(EX:`, `Ex:`, `#`, `##` e campo vazio antes de tratar um bloco como fonte.**
> E **registre a passada de bastão em branco como achado** — é lacuna do ritual da casa, não do
> cliente.

**9 · A tabela de usuários da página não é o cadastro vivo do PLM. (Puket)**
Na Puket, `beatriz.fraga@puket.com.br` abriu chamado em jan/2026 e **não está** entre os 43 da
tabela — cuja última data de acesso é de jun/2023. **Cruze sempre os e-mails dos chamados contra a
tabela** e registre quem sobra.

**10 · Data em título de ata não é data de ata. (Puket)**
Das 23 atas da Puket, só 3 têm o campo `Data da Reunião` preenchido. A data real vive **dentro do
título**, como texto — e há caso de título que **não bate** com a data de criação
(*"Weekly 05/12/24"* criada em 29/08/2024). **Use o título, mas confira contra `createdTime` e
sinalize a divergência.**

**11 · Silêncio é estado da conta, e vai na jornada. (2 casos)**
Puket: última ata 08/01/2026, último chamado 29/01/2026, **3 chamados ainda `Não iniciada`**.
Caedu: cadência some depois de jun/2026. **Sempre compare a última ata com a data de hoje** e
escreva o intervalo em meses.

**7 · Datar tudo e marcar o que não foi confirmado.** O mapeamento de conta da CAEDU tem 17 meses e
já contém correções posteriores no próprio texto. O porte e o CEO vieram de um CRM de mentoria e
**não** do atendimento — ficaram marcados como não confirmados.

## 4 · O que produzir, por cliente

| Arquivo | Fonte principal |
|---|---|
| `00_Institucional/_contexto/institucional.md` | base `Mapa de Clientes` + perfis do PLM (aliases de área) |
| `00_Institucional/_contexto/pessoas.md` | tabela de usuários do PLM + atas (liderança) |
| `00_Institucional/_contexto/jornada.md` | atas datadas + mapeamento + vault |
| `<NN_Area>/_contexto/contexto-area.md` × 14 | mapeamento de conta + perfis + sub-páginas |

**Em todo arquivo:** tabela de **Procedência** no fim, com bloco, fonte e data.

## 5 · Ordem de ataque dos 21 restantes

Priorizar por **status e volume de material**, não por ordem alfabética:

0. ✅ **Feitos** — **Caedu** (93 usuários, 14 perfis) e **Puket** (43 usuários, 13 perfis)
1. **Ongoing com mapeamento de conta** — Reserva (7 módulos, a conta mais completa), NV, Cambos,
   Osklen
2. **Ongoing restantes** — Lofty Style, Luiza Barcelos, NK STORE, Oficina Reserva, VIX
3. **Operação Assistida** — Moda Objetiva, Osklen
4. **Onboarding** — Loungerie ⚠ **não existe no corpus, precisa ser criado**
5. **Pré Onboardings** — Arezzo, Hering
6. **Sem CS** — Baw, Camys, Cavallari, Mondepars, Studio Minah, TDC, Ton Age
   > Estes provavelmente só têm `Gestão de Coleção` e pouca ata. **Esperar pouco material** — e
   > registrar isso como fato do cliente.

## 6 · O contexto de carteira, para não varrer no escuro

Varrido ao vivo em 21/09/2026, os **13 clientes vivos**:

| Grupo | WIP Estrat. | Clientes |
|---|---:|---|
| **Enterprise** (*"Reserva + Soma"*) | 6,00 | Reserva · Oficina Reserva · NV |
| **Médios** | 2,25 | Cambos · Lofty Style · Luiza Barcelos · NK STORE · VIX · Osklen · Moda Objetiva · Loungerie |
| **SMB** | 1,75 | Caedu · Puket |

**Atendimento 2025:** Julianne & Pedro (6 contas) · Laura (4) · Fernanda (3).

**Módulos, do mais ao menos servido:** Reserva 7 · Oficina Reserva 5 · Osklen 5 · Caedu 4 ·
NK STORE 4 · Luiza Barcelos 4 · Lofty Style 4 · NV 4 · Moda Objetiva 4 · VIX 4 · Cambos 3 ·
**Puket 2** · Loungerie 0.

**ERPs:** Linx domina; `Linx / SAP` em Puket e Reserva; `SAP e Linx` em Oficina Reserva
— **mesmo par, grafia diferente: erro de taxonomia na origem**. Fora do padrão: `Safe Tech`
(Luiza Barcelos), `SPI` próprio (Cambos), `Ilimitar` (Moda Objetiva).

> ⚠ A base `Segmentação Grupos` (`collection://a4103fe2-2f5f-48b4-9136-f0b82b7e1a56`) está sob a
> pasta **`Arquivo`**. **Confirmar vigência antes de usar como autoridade.**

## 7 · 🔴 A regra de padrão (travada pelo Vinicius em 21 set 2026)

> *"Você vai seguir a diretriz estratégica de junção de contexto mantendo um mesmo padrão (mesmo
> que em dado momento entenda que o padrão tem que mudar), mas aí você retorna e replica esse
> padrão pra tudo de uma mesma classe de documentações que estiver criando/manipulando."*

**Mudar o padrão é permitido. Mudar só no arquivo da vez, não.**

Ao varrer um cliente você vai encontrar coisa que o template não previa. Quando isso exigir seção
nova, o procedimento é **um só**, e nesta ordem:

1. **Promova a seção ao `_template_cliente`** — ela passa a ser canônica.
2. **Replique em toda a classe**, todos os clientes, não só o que você está varrendo.
   Seção nova em cliente sem dado entra com `` `[a preencher]` `` — **lacuna visível vale mais que
   cobertura aparente.**
3. **Verifique em número**, arquivo a arquivo, e escreva o número.
4. **Nunca apague conteúdo** para encaixar estrutura. Inserir sim, remover não.

**Achado de cliente não vira seção nova.** Vira conteúdo sob a seção canônica a que pertence —
`###` sob o `##` certo, ou parágrafo. Só vira seção quando valer para **todos** os clientes.

### O erro que gerou esta regra
Ao fechar a Puket criei `## O achado estrutural: duas camadas de empresa`, `## A lista de usuários
não é o cadastro vivo` e `## Evidência de que o perfil governa permissão` — três seções que **só
a Puket tinha**. E renomeei duas seções que a CAEDU já tinha com outro nome. **Duas cópias do mesmo
tipo de documento com estruturas diferentes é exatamente o defeito que já se criticou na
arquitetura do João.**

Corrigido em 21/09/2026: as três viraram `###` sob `## Time do projeto por área`, os nomes foram
unificados, e o padrão resultante foi replicado nas **192 documentações das quatro classes**.

### O padrão vigente, em número
| Classe | Arquivos | Conformes |
|---|---:|---:|
| `institucional.md` | 48 | **48** |
| `contexto-area.md` | 50 | **50** |
| `jornada.md` | 47 | **47** |
| `pessoas.md` | 47 | **47** |

**Seções promovidas ao template nesta rodada:** `### Usuários da conta` · `### Onde estamos` ·
`### A frente aberta` · `### O que o cliente espera` · `### As dores estruturais registradas` ·
`### Tamanho de atendimento` · `### Procedência` (nos três tipos) ·
`## O que este documento NÃO resolve` (na `jornada.md`, por exigência do `CLAUDE.md`).

## 8 · 🔴 A página do cliente é o índice, não a fonte

> Cobrança do Vinicius em 21 set 2026: *"você não está só vendo chamados certo? Está coletando
> informações de tudo dos clientes certo?"*

**Medi e a resposta era "quase".** Eu lia a linha inteira da base, o corpo completo da página do
cliente, a segmentação, o portal, as atas e os chamados — e **parava aí**, listando as sub-páginas
como *"não varrida"*. Eram **69 fontes declaradas e não abertas** em cinco clientes.

**Desci um nível numa única sub-página da NK STORE e o resultado foi desproporcional.**

### O que uma sub-página entregou
A página *Perfil de Usuário e Permissionamentos*, dentro de `Documentos`, tinha:
1. **Uma matriz de permissão completa** — ~60 funções × 7 perfis, com 🟢 🟡 🔴 e coluna de validação.
2. **Uma base de usuários embutida** com **`Status`, `Departamento` e `Perfil` por pessoa** —
   a única fonte de toda a varredura que declara **ativo, inativo com data e convite pendente**.
3. O achado de que **a Gerente de Projeto do cliente está marcada `INATIVAR`**.
4. A prova de que **a dor de "cadastrar opção" é permissão por desenho**, não defeito.

**Nada disso estava na página do cliente.**

### A regra
**Abra as sub-páginas. Começando pelas de `Documentos`.**

| Prioridade | Procure por | Por quê |
|---|---|---|
| 1 | **`Perfil de Usuário e Permissionamentos`** | matriz de permissão **e** base de usuários com status |
| 2 | **`Mapeamento de Contas - <cliente>`** | AS IS, fluxo por área, dores |
| 3 | **Manuais e procedimentos** (ex.: *Manual de descancelamento*) | onde há manual, há lacuna de produto |
| 4 | **`Passada de bastão` / template de transição** | marca, ERP, usuários, **departamentos engajados** |
| 5 | **`Dúvidas Pendentes` / `Análise de Demandas`** | frente aberta com data |
| 6 | Playbooks · Onboarding Fase 1/2 · Miro · Portal | contexto de processo |

### Três heurísticas que se pagam
- **Toda base embutida (`<database inline>`) é dado estruturado escondido.** A página mostra um
  `collection://` — **consulte por SQL em vez de ler a página.**
- **Título de manual denuncia lacuna de produto.** *Manual de descancelamento* existe porque a
  plataforma não descancela. **Procure o manual antes de procurar a dor.**
- **Sub-página desmente a página-mãe.** Na NK, a página diz que a Larissa lidera o projeto; a base
  interna diz `INATIVAR`. **A mais profunda costuma ser a mais recente — mas confira a data das duas.**

### ⚠ E o que fazer ao encontrar segredo
A página da NK STORE tem **credencial de banco de produção em texto plano** numa sub-página.
**Nunca copie o valor — nem para o corpus, nem para log, nem para relatório.** Registre
**que existe, onde está e que precisa ser rotacionada**, e avise. Mesma regra para **CPF e
telefone pessoal**: no corpus entram **nome, cargo e e-mail corporativo**, que é o dado de negócio.

## 9 · 🔴 Identidade de pessoa — a regra travada pelo Vinicius em 22 set 2026

**Toda varredura de pessoas de um cliente fecha com uma análise de suspeitos de duplicidade.**
Não é opção: é passo obrigatório do protocolo.

### 9.1 · Por que existe

Eu havia proposto **`person.email` como chave primária de identidade**. O Vinicius recusou a
versão simples: `[D]`

> *"Se em dado momento aparecer uma **mesma pessoa, mas com dois endereços** — seriam duas
> pessoas? Não faz sentido. Você terá que identificar a forma mais plausível de torná-la única.
> Se quiser tratar dessa forma pelo e-mail, ok, no entanto você terá que ter **sempre uma
> avaliação sobre todos os e-mails concentrados de uma empresa/cliente e levantar suspeitos de
> serem as mesmas pessoas**. Só assim pra resolver."*

**E o risco é nos dois sentidos, com caso real de cada lado:**

| Risco | Caso real |
|---|---|
| **Separar quem é a mesma pessoa** | `Thais Pantaleão` aparece em **8 grafias** na Osklen |
| **Fundir quem são duas pessoas** | `Luana Henriques` e `Luana Carmo` — **duas pessoas reais** na VIX, e 11 demandas assinadas só `Luana` |

### 9.2 · Como executar

1. **Junte todos os identificadores daquele cliente**, de todas as fontes varridas: e-mail
   (base de chamados), nome em `Quem solicitou?` (demandas), nome em ata, nome na página.
2. **Agrupe por domínio de e-mail** — o domínio identifica o cliente e separa **terceiros**.
3. **Levante suspeitos**, por estes sinais, nesta ordem de força:
   - mesmo e-mail, grafias de nome diferentes → **mesma pessoa, alta confiança**
   - primeiro nome igual + sobrenome ausente em um dos lados → **suspeito**
   - variação de acento, letra dobrada ou apelido (`Patrícia`/`Patricia`/`Paty`) → **suspeito**
   - primeiro nome igual **e sobrenomes diferentes** → 🔴 **são duas pessoas até prova em
     contrário** — foi o caso das duas Luanas
4. **Escreva a lista de suspeitos no `pessoas.md` do cliente**, com o sinal que a levantou.
5. 🔴 **NÃO FUNDA NADA.** **Suspeita se levanta; fusão só com confirmação humana.**
   Fundir por semelhança gráfica **inventa pessoa** — viola a regra de ouro.

### 9.3 · O que registrar quando não dá para decidir

**Cada forma entra como está na fonte**, com a marca de variante e o sinal que a tornou
suspeita. **Nunca escolher uma forma "canônica" por conta própria.**

> ⚠ **E registre o limite:** ter a chave **não conserta o dado escrito sem ela.** As 11 demandas
> assinadas só `Luana` na VIX **seguem sem dono**, mesmo com os dois e-mails confirmados.

## § 11 · Bloco que o conector não renderiza — e o que fazer

> **Aprendido em 22 set 2026, na página `Luiza Barcelos | Warm Up Cliente`.**

🔴 **Eu atribuí a falha a permissão e estava errado.** A página abria inteira. Os blocos
vinham como `<unknown>` porque **são um tipo que este conector não renderiza** — no caso,
**linhas de contato**: telefone, e-mail, CPF e cargo.

**O custo do erro de diagnóstico:** eu quase pedi ao Vinícius uma liberação de acesso que
não resolveria nada.

| Passo | O que fazer |
|---|---|
| 1 | **Antes de falar em permissão, puxar a página-fonte direto.** Se ela abrir, **não é acesso** |
| 2 | Contar os `<unknown>` e **dizer onde estão** — sob qual título, depois de qual nome |
| 3 | Pedir ao Vinícius **só aquele trecho**, copiado e colado. **É barato e funciona** |
| 4 | **O que vier assim é fonte como qualquer outra**: entra com procedência e data |

🔴 **Regra de tier que não muda por vir colado:** e-mail **corporativo** entra (`T2`);
**telefone e CPF não entram** (`T0`) — registro que existem e onde.

⚠ **O mesmo tipo de bloco deve existir em outras páginas de cliente.** Sempre que o toggle
`Pessoas` parecer vazio ou truncado, **suspeitar disto antes de concluir que não há gente lá.**

## § 10 · Cargo de uModer lido em fonte datada

> **Travado pelo Vinícius em 22 set 2026.** Surgiu ao ler a ata do Warm Up da Luiza Barcelos,
> de **07 jun 2024**, que nomeia seis pessoas da uMode com cargo. **Quatro delas já saíram.**

🔴 **Cargo lido em ata é cargo NAQUELA DATA. Nunca cargo de hoje.**

| Situação | O que fazer |
|---|---|
| A fonte dá cargo de uModer | escrever o cargo **com a data da fonte colada nele** |
| A fonte é antiga e a pessoa pode ter mudado | **não atualizar o `Cadeira / cargo atual`** — o campo é sobre hoje, e a ata não sabe de hoje |
| Sabe-se que a pessoa saiu | `Status na uMode` = saída, **com quem confirmou e quando** |
| Tentação de corrigir a Casa inteira agora | 🔴 **NÃO.** É passo de **fechamento**, uma vez só |

**Por que de uma vez, no fim:** o Vinícius pediu assim — *"teremos que corrigir somente ao final
de toda a varredura"*. **Corrigir aos pedaços cria versões parciais conflitantes**, que é
exatamente o defeito que o corpus tem em `Status` de cliente. **O passo está no `AGORA.md` § 7,
item 9**, e não se antecipa.

⚠ **Isto NÃO vale para pessoa de cliente.** Cargo de pessoa de cliente lido na página do
cliente entra normalmente — a página é a fonte viva daquele cliente, e não há organograma
nosso para conferir contra.

## Governança
Somente o CEO altera conteúdo no BrainHub. **Alterar este protocolo exige ter executado a varredura
de pelo menos um cliente com o método novo** — protocolo não se corrige por opinião.
