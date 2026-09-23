---
aliases:
  - "Varredura 23 set 2026 (a) — as matrizes de permissão fecharam, e derrubaram duas conclusões minhas"
---
# Varredura 23 set 2026 (a) — as matrizes de permissão fecharam, e derrubaram duas conclusões minhas

> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**
>
> Veio de abrir as cinco últimas páginas de `Perfil de Usuário e Permissionamentos`:
> **NK STORE**, **Moda Objetiva**, **Recco**, **NV** e **Lofty Style**.
>
> 🟢 **As dez matrizes conhecidas estão lidas.** Era a lacuna aberta desde o registro `(k)`.

## 0 · O que este registro NÃO resolve

- ⚠ **12 das 13 sub-páginas de perfil da NV continuam fechadas.** Li a página-mãe e a
  `NV - Geral`. **Não sei o que há nas outras doze.**
- ⚠ **A planilha Google com os e-mails da Moda Objetiva não foi aberta** — está fora do
  Notion e não tentei.
- 🔴 **Não sei distinguir, em nenhuma matriz, "bloqueado por permissão" de "funcionalidade
  desligada".** A Moda Objetiva tem oito linhas 🔴 para os dez perfis, Admin incluído.
  **Semáforo vermelho para todo mundo não é permissão — mas o documento é o mesmo.**

## 1 · 🔺 Duas conclusões minhas caíram

### 1.1 · O `Fale com o Suporte` não é padrão — é decisão por cliente

Eu levantei a hipótese com dois casos e ela foi crescendo. **Agora tem dez, e o placar
não fecha para lado nenhum:**

| 🔴 Bloqueado (4) | 🟢 Liberado (6) |
|---|---|
| Luiza Barcelos · Lenny Niemeyer · **NK STORE** · **Recco** | VIX · Oficina Reserva · Cambos · **Moda Objetiva** · **NV** · **Lofty Style** |

> 🔴 **Quatro contra seis, com as dez lidas. Não há padrão a encontrar: há uma decisão por
> cliente que ninguém registrou.**

⚠ **A consequência que JÁ estava certa continua valendo, e fica mais forte:** volume de
chamado mede **quem tem o botão**, não atividade de conta. **Quase metade da carteira lida
não tem o botão.**

### 1.2 · 🔴 A dor de excluir variante é CONFIGURAÇÃO, não limitação da plataforma

Eu vinha registrando a exclusão de variante como **dor de produto** em cinco clientes.

> 🟢 **Na Recco, `> excluir variante` está LIBERADO para `Admin` e `Time`.** `[C]`

| Estado | Clientes |
|---|---|
| 🔴 bloqueado | VIX · Reserva · Lofty Style · NV |
| ⚠ célula **em branco** | Lenny Niemeyer |
| 🟢 **liberado** | **Recco** |

**Seis casos. A plataforma sabe excluir variante.** ⚠ **Se a dor de cinco clientes é permissão
e não engenharia, a solução é outra — e é barata.** 🔴 **Isso precisa ser conferido antes de
qualquer coisa ser prometida a cliente.**

## 2 · 🟢 O achado de maior valor: a NV escreveu o MECANISMO de permissionamento

A página-mãe `[NV] Permissionamento` abre com a definição que faltava no corpus: `[C]`

> *"Na uMode, o permissionamento pode ser configurado de duas formas:
> **Inclusão** → quando a configuração determina tudo aquilo que o perfil **pode** fazer.
> **Restrição** → quando a configuração determina tudo aquilo que o perfil **NÃO pode** fazer."*

🔴 **Até aqui o corpus só tinha evidência de código:**

| Onde | O que eu tinha |
|---|---|
| `uFlow / Setup - PLM` | `Menu Item`, permissão do tipo **`INCLUDES`** |
| Oficina Reserva | `read_only: !current_context.current_policy.name.in?([…])` |

> 🟢 **`INCLUDES` é a Inclusão. O `.in?()` negado é a Restrição.** **O conceito e as duas
> evidências de código casam.** É **allowlist e denylist, escolhidas por perfil.**

### 2.1 · 🔺 E o vocabulário diverge dentro do próprio documento

| Onde | Palavra |
|---|---|
| Página-mãe | **`Restrição`** |
| Sub-página `NV - Geral` | **`exclusão`** |

⚠ **Duas palavras para o mesmo conceito, a uma clicada de distância.** O `CLAUDE.md` trava
taxonomia como essencial — **registro como divergência a resolver, não escolho por conta.**

## 3 · 🔴 A NV tem coisas que nenhum outro cliente tem

| O quê | Por que importa |
|---|---|
| **`Todas as Subcoleções`** | todos os outros dizem `Todas as Coleções`. 🔴 **Há um nível A MAIS na hierarquia de moda** — e é o que a CAEDU pede desde 16/09/2025 |
| 🔴 **`Audit uMode x Linx`** | **tela de AUDITORIA DE INTEGRAÇÃO** na ficha de produto. O corpus não tinha nada disso, e é exatamente a dor aberta na CAEDU e na VIX |
| `Programações` + `Tipo de Programação` | **um módulo inteiro** que só a NV tem |
| `Enviar para Integração` · `Enviar para e-commerce` | ações de push explícitas, com permissão própria |
| **`Datas - Estilo` / `Datas - Qualidade` / `Datas - Planner`** | **primeiro caso de aba segmentada por área funcional.** É marco de projeto morando dentro da ficha de produto |
| `Permissionamento - Exclusões e Edições` | **aba DENTRO da ficha** para configurar permissão. Permissão por produto, não só por perfil |
| `Cabeçalho` 🟢 *(não edita Referência NV e Entrada NV)* | **campos com o prefixo do cliente no próprio nome** |

**13 perfis** — `Geral` · `Master` · `Estilo` · `Qualidade` · `Planner` · **`Planner 2`** ·
`Compras` · `Planejamento Comercial` · `PCP` · `Atacado` · `Marketing` · **`View`** ·
`Logística`. **É o maior número da carteira.**

## 4 · A base de usuários da NK STORE responde uma pergunta que ficou aberta na Lenny

Na Lenny Niemeyer eu achei a base `Usuários` com **29 linhas todas vazias** e registrei a
pendência: *"verificar se outros clientes têm a mesma base preenchida"*.

> 🟢 **Têm. A NK STORE tem 30 linhas, todas preenchidas, com o mesmo schema.** `[C]`
> `Nome` · `E-mail` · `Perfil do Usuário` · **`Departamento NK`** · `Status`

**Viraram 28 fichas de pessoa** — a quarta fonte de pessoa do corpus.

### 4.1 · 🔴 `INATIVAR` como valor de `Departamento`

**5 das 30 linhas têm `Departamento NK = INATIVAR`.**

> ⚠ **Não é departamento. É instrução operacional escrita no campo de área.** O campo virou
> fila de tarefa, **e com isso a área real dessas cinco pessoas se perdeu.**

### 4.2 · 🔴 A matriz e a base não batem

| Perfil | Na matriz | Na base |
|---|:-:|:-:|
| `NK - Admin` | ✅ | ✅ 3 pessoas |
| `NK - Time` | ✅ | 🔴 **nenhuma** |
| `Fornecedor` | ✅ | 🔴 **nenhuma** |
| `NK- Estilo Master` · `Nk Compras Master` · `Nk Modelagem` · `NK Compras` | ✅ | 🔴 **nenhuma** |
| **`NK - PCP`** | 🔴 **não existe** | ✅ **7 pessoas** |
| `NK - Estilo` · `NK - Compras` · `NK - Modelagem` | 🔴 não existe com esse nome | ✅ |

🔴 **Sete pessoas usam um perfil que a matriz de permissão não documenta.** ⚠ **Um dos dois
documentos está velho e eu não sei qual.**

### 4.3 · 🟢 O que eu me recusei a decidir

| Caso | Decisão |
|---|---|
| `kemely.md` × `kemelly.fernandes@` | **não fundi** — um `l` de diferença |
| `silvia-shirlei-dias.md` × `silvia.nascimento@` | **não fundi** — sobrenomes não batem |
| `cristina.md` × duas `Cristina` na base | 🔴 **o gerador PAROU e avisou** em vez de sobrescrever |
| `Vanessa Veiga` × `vanessa.ventura@` | nome e e-mail divergem — **registrei, não resolvi** |
| `expedicao2@nkstore.com.br` | **caixa funcional com pessoa nomeada atrás** — a chave de identidade aqui é de uma caixa |

## 5 · 🆕 A NK STORE homologou a matriz COM O CLIENTE, dentro da matriz

Duas colunas — `Validação NK - Admin 04/12` e `Validação NK - Time 04/12` — com ✔️, ✖️ e
comentários: *"não pode aparecer os 3 pontinhos"*, *"incluir ação de cancelado"*, *"travar
edição de grade qnd tiver tabela"*, *"ajustar lista de perfis"*.

> 🟢 **É o único caso do corpus de homologação datada registrada na própria matriz.**
> ⚠ **E as pendências que ela levantou não têm dono nem prazo em lugar nenhum.**

## 5-bis · 🔴 A Lofty Style dá permissão a uma PESSOA dentro da célula de um PERFIL

Duas células da coluna `Lofty - Compras MP`: `[C]`

| Linha | Célula |
|---|---|
| `Importação` | 🟡 **"(Liberado só Isadora desse Perfil)"** |
| `Integração Linx` | 🟢 **"(Somente a Dora)"** |

> 🔴 **É a primeira vez no corpus que a permissão é de uma pessoa, não de um perfil.**

> 🔺 **CORRIGIDO NO MESMO DIA, algumas horas depois.** O que vem abaixo deste
> quadro **está errado** e fica aqui porque `REGISTRO` guarda o que eu escrevi, não o que
> eu gostaria de ter escrito. **A correção é autoridade em
> [`_dicionario-permissionamento-uflow.md`](_dicionario-permissionamento-uflow.md) § 4.**
>
> 🟢 **O mecanismo existe e chama-se `scopable`.** Vale `policy` (o perfil inteiro) ou
> **`user`** (um usuário específico), e está documentado desde 2024 no
> `📕 Manual do Permissionamento`. **Há até um controller dedicado:
> `j3/user_or_policy_accesses`.**
>
> **Por que eu errei:** o registro `(m)` leu uma **query de análise de acesso** e eu tratei
> aquele recorte como **o modelo inteiro**. ⚠ **É parente do erro do `entity_id = 3344`:
> tomar o alcance de um artefato pelo alcance do sistema.** E é a quinta variação de
> *"não encontrei em X" virando "não existe"* — desta vez com a página que respondia
> já listada como fonte não varrida, a uma leitura de distância.

~~🔴 **E o modelo de dados do uFlow não tem onde guardar isso.** O registro `(m)` leu a
cadeia: `jumper_users` → `user_roles` → `policies`. **A permissão pendura na `policy`, e a
`policy` é do perfil.**~~

~~⚠ **Ou existe um mecanismo que eu não vi, ou a regra só existe no papel.**~~ **A pergunta ao
Vinicius muda de forma:** não é mais *"como isso está implementado?"* — é **"a Isadora tem
`scopable: user` de fato, ou é combinado que ninguém aplicou?"**

⚠ **`Isadora` e `Dora` estão na mesma coluna.** Provavelmente a mesma pessoa com dois
apelidos. **Não fundi.**

### 5-bis.1 · E há uma terceira granularidade: o CAMPO

`Lofty - Modelagem` em `Estilo | Informações Gerais` é 🟢 **"(Só o campo modelista,
piloteiro e Operador CAD)"**.

| Nível | Onde apareceu |
|---|---|
| **tela** | todas as matrizes |
| **aba da ficha** | todas as matrizes, segunda tabela |
| **campo** | 🆕 **só a Lofty Style** |
| **pessoa** | 🔴 **só a Lofty Style** |

### 5-bis.2 · 🔴 `Editar Usuario` bloqueado para os dez perfis, Admin inclusive

⚠ **Único caso do corpus em que nem o Admin edita o próprio usuário.** **Não sei se é
intenção ou engano** — e a diferença é grande.

### 5-bis.3 · Onze linhas 🔴 para todo mundo

`Lotes` · `Tabela Dinâmica` · `Coordenado` · `Estampa` · `Composição de Custo` ·
`Ficha Técnica Base` · `Tag` · `Tipo de Lote` · `Pack` · `Campo Personalizado` ·
`Salvar como Ficha Técnica Base`.

> **Mesmo fenômeno da Moda Objetiva, agora com onze linhas.** 🔴 **Bloqueio para todos,
> Admin incluso, não é permissão — é funcionalidade desligada na conta. O corpus
> registra as duas com o mesmo símbolo, e são decisões de donos diferentes.**

## 6 · Os outros achados, em uma tabela

| Cliente | Achado |
|---|---|
| **Recco** | 🔴 **perfis SEM prefixo de cliente** (`Admin`, `Time`, `Fornecedor`) — os únicos. Num banco multi-conta, é colisão esperando acontecer |
| **Recco** | 🆕 `Perfis dentro de Tarefas` = *"Somente relacionados ao cliente"* — **regra em texto, não semáforo**. A NK pediu o mesmo na validação. **Dois casos** |
| **Recco** | 🆕 a aba se chama **`Fabricantes`**, mas a linha de criação dentro dela é `> novo fornecedor` |
| **Moda Objetiva** | 🆕 **`Objetiva - Consulta`**, perfil somente-leitura. Com `NV - View` e `Lofty - Mkt, Multimarcas e ecommerce`, **três casos — vira padrão** |
| **Moda Objetiva** | 🆕 abas que ninguém mais tem: `Variântes`, **`EAN`**, `Logística e Fiscal`, `Quantidade Grade Tam.` |
| **Moda Objetiva** | 🔴 **`Grupo` é item de Cadastro** — o nível que a CAEDU pede. **Existe e está em pé** |
| **Moda Objetiva** | 🟢 `Manual` e `Base de Importação` **liberados** — segundo caso, com a Cambos |
| **NK STORE** | 🆕 `Integração Linx` e `Chat NK` como abas da ficha |
| **Lofty Style** | 🆕 `Mapa de Coleção` 🟢 *(Somente para uso de filtros, sem editar informações)* — **terceiro caso de regra em TEXTO dentro da célula**, com Recco e NK STORE. ⚠ **O texto contradiz a cor** |
| **Lofty Style** | ⚠ **`Lofty  - Planejamento` tem dois espaços no nome** — erro de digitação vivo, que quebra qualquer casamento por string |
| **Lofty Style** | 🆕 `Lofty - Mkt, Multimarcas e ecommerce`: **três funções num perfil só** |

### 6.1 · O `Chat` com nome do cliente

| Cliente | Rótulo |
|---|---|
| NK STORE | `Chat NK` |
| NV | `Chat NV` |
| Moda Objetiva · Recco | `Chat` |

⚠ **Dois casos contra dois. É customização de rótulo, não padrão** — mesma régua que derrubou
a hipótese do `Manual`.

## 7 · O placar dos perfis por cliente

| Cliente | Perfis |
|---|--:|
| VIX | **17** |
| **NV** | **13** |
| **Moda Objetiva** · **Lofty Style** | **10** |
| Oficina Reserva | 8 |
| **NK STORE** | 7 |
| Luiza Barcelos | 6 |
| Cambos | 5 |
| **Recco** · Lenny Niemeyer | 3 |

🔴 **De 3 a 17 perfis, nos dez clientes que têm matriz.** ⚠ **Não existe "o modelo de perfis do uFlow" — existe um por conta.**

## 8 · 🟢 Uma correção de engenharia que o dado obrigou

Três laços do `gera-fichas-pessoa.py` escrevem no mesmo diretório, cada um derivando o nome do
arquivo de um campo diferente. **Quando dois caíam no mesmo `slug`, o segundo sobrescrevia o
primeiro em silêncio.**

> 🔴 **É o mesmo defeito de `chave sem pasta`: dado somindo sem aviso.**

**O que mudou:**

1. **O primeiro a escrever fica.** O segundo **não escreve** e vira alerta no fim da rodada.
2. **Casamento por nome completo** foi acrescentado — sem ele, `Stella Sunaga` (página) e
   `stella.sunaga@` (plataforma) viravam **duas fichas da mesma pessoa**.
3. **Quem está na página E na plataforma agora nasce com as duas metades** — cargo de um lado,
   e-mail e perfil do outro.

**Colisão que sobrou, e é legítima:** `cristina.md`. **Duas Cristina, um primeiro nome.**
Virou pergunta.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1.1, §4, §5, §6 | Notion — `NK STORE › Documentos › Perfil de Usuário e Permissionamentos` (`0385f372…`) e a base `Usuários` (`collection://1b5b1d38-e768-80b0-aaac-000b33b9657a`), **abertas por inteiro** | **23 set 2026** |
| §1.1, §6 | Notion — `Perfil de Usuário e Permissionamentos - Moda Objetiva` (`38bb1d38…`), **aberta por inteiro** | **23 set 2026** |
| §1.2, §6, §7 | Notion — `Recco \| Perfil de Usuários e Permissionamentos` (`191b1d38…`), **aberta por inteiro** | **23 set 2026** |
| §2, §3 | Notion — `[NV] Permissionamento` (`198b1d38…`) e a sub-página `NV - Geral`, **abertas por inteiro**; **as outras 12 sub-páginas NÃO** | **23 set 2026** |
| §5-bis, §6, §7 | Notion — `Lofty Style › Documentação/Regras › Perfil de Usuário e Permissionamentos` (`2e1b1d38…`), **aberta por inteiro** | **23 set 2026** |
| §7 | cruzamento com os registros `(k)`, `(l)` e `(m)` de 22 set 2026 | **23 set 2026** |
| §8 | o próprio `scripts/gera-fichas-pessoa.py`, depois da correção | **23 set 2026** |
