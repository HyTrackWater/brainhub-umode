---
aliases:
  - "Parte IV — a ontologia como requisito"
tags:
  - tipo/espec
  - casa
---
# Parte IV — a ontologia como requisito

> **Para o plano técnico do BrainHub**, continuando o documento do João Risoléo (Partes I e II,
> § 1–13) e o complemento do Pedro Mafra (Parte III, § 14–20).
> **Vinicius Risoléo · 25/09/2026.**
>
> 🔴 **As seções 1 a 20 não foram alteradas.**

## 21 · Por que esta parte existe e como ler

### 21.1 · 🔴 Isto NÃO é uma evolução, e o nome importa

**Evolução carrega juízo:** implica que o anterior estava incompleto e o novo o substitui.
⚠ **Isso contradiz a própria tese desta parte** — que os três acervos são **três camadas que
coexistem**, não três versões de uma coisa só. 🟢 **O nome certo é acréscimo com divergência
declarada**, e a forma segue a mesma do Pedro.

**Três registros, separados de propósito, para o leitor sempre saber o que está lendo:**

| Marca | Registro | O que significa |
|---|---|---|
| 🟢 **`ACRÉSCIMO`** | § 23 | mecanismo que já opera aqui e vira requisito. **Não contesta ninguém** |
| ⚠ **`DIVERGÊNCIA`** | § 27 | leio o plano diferente. **Nomeada, com proposta — sem reescrever o texto de ninguém** |
| 🔴 **`PEDIDO`** | § 27 | precisa de decisão de quem é dono daquela seção |

🔴 **`SUPERSEDED` não aparece nesta parte, e a ausência é deliberada.** A regra da casa é que
quando um documento novo vira autoridade sobre um tema, o anterior é marcado **no que perdeu**.
⚠ **Mas eu não sou dono das seções do João nem do Pedro.** 🟢 **Então esta parte é, ela mesma, um
pedido de aprovação: propõe, e os donos decidem.**

### 21.2 · 🟢 O documento está praticando a regra que o documento especifica

Vale registrar, porque não é coincidência de estilo:

| O que a Parte III fez com o documento | A mesma regra, no produto |
|---|---|
| seções 1–13 intactas; a Parte III entra por cima | `protocolo-fato-atomico` § 2.2: **quando duas fontes discordam, as duas linhas ficam** — 🔴 nunca se apaga a antiga para "resolver" |
| § 18 **nomeia** as sete divergências em vez de reescrever | **conflito é dado**; quem resolve é pessoa |
| a Parte III não revoga nada, propõe | **Marcos append-only:** *"nunca se reescreve um marco antigo, só se adiciona um novo"* |
| o leitor segura as duas leituras | **linhagem imutável:** correção entra como nó novo com `supersedes` |

⚠ **O formato de colaboração dos três documentos já É o mecanismo de aprovação de contexto.**
🟢 **Isso é evidência a favor do desenho** — ele funcionou primeiro entre pessoas.

### 21.4 · 🔴 O pedido do Rafael que continua aberto — e ele usou a palavra "evoluir"

**Lendo o Discord de 24/09, há um pedido explícito, feito duas vezes, que ninguém atendeu.**

> **Rafael, 19:37**, ao mandar o `brainhub-telas.html`:
> *"joga no teu brain aí e pede pra ele colocar as features que vc acha que precisam estar,
> **corrigir features que foram mostradas erradas** e talz … aí vc me manda **o html de volta** e
> a gente olha … **vai incrementando nessas telas aí, nesse formato**."*
>
> **Rafael, 20:04**, depois de receber o plano técnico de 707 KB:
> *"Fechou, quando puder **cruza com o que mandamos e evolui a partir do nosso** por favor."*

⚠ **O que o Rafael pediu foi o documento de TELAS de volta, incrementado, no formato dele.**
**O que chegou foram dois planos técnicos.** 🔴 **Os dois são bons e ninguém devolveu as telas.**
A segunda mensagem dele é um pedido educado dizendo exatamente isso.

🟢 **E é aqui que a palavra "evolução" está certa** — foi ele quem a usou, e ela se aplica a um
objeto específico: **o `brainhub-telas.html`**, evoluído tela a tela. ⚠ **Não se aplica a esta
Parte IV**, que continua sendo acréscimo sobre o plano (§ 21.1). **São duas entregas de natureza
diferente e as duas estão em aberto:**

| Entrega | Formato | Para quem | Estado |
|---|---|---|---|
| **Parte IV** — a camada de ontologia como requisito | seções sobre o plano | João e Pedro | 🟢 **este documento** |
| 🔴 **`brainhub-telas.html` evoluído** — features corrigidas e acrescentadas, tela a tela | **o HTML dele, no formato dele** | **Rafael**, que decide o build | ⚠ **pedido aberto desde 24/09** |

🔴 **A § 22.3 e a tabela de telas do parecer de 25/09 pertencem à segunda entrega, não a esta.**
Correção de tela não se resolve num anexo de plano: **ela tem de voltar no artefato que o
desenvolvedor abre para construir.** ⚠ **Ele disse que só depois do fluxograma soube o que
construir, e estimou 10 a 15 dias úteis a partir dali** — **devolver no formato errado custa
esses dias.**

### 21.3 · Critério de entrada

**O mesmo da Parte III:** só entra mecanismo que **já opera** aqui, ou incidente que **já
aconteceu**, com a regra que nasceu dele e o requisito que isso cria. 🔴 **O que está no papel e
não opera aparece marcado como tal — e a § 25 é só disso.**

**Retrato em 25/09/2026,** medido no repositório `HyTrackWater/brainhub-umode`:

| | |
|---|---:|
| MDs no corpus | **2.660** |
| clientes com estrutura completa | **48** |
| afirmações atômicas datadas | **3.438** |
| chaves em uso, de vocabulário **fechado** | **33** de 35 |
| das afirmações: com fonte nomeada | **1.432** |
| das afirmações: **ausência VERIFICADA** | **1.897** (55%) |
| das afirmações: lacuna declarada `[sem fonte]` | **80** (2%) |
| protocolos · validadores · scripts | **12** · **5** · **28** |
| decisões e pendências rastreadas | **756** |
| regras nascidas de erro datado | **54** marcadores |

## 22 · 🔴 O que falta nos dois planos não é a entidade — é a CHAVE

> ⚠ **Esta seção foi reescrita em 25/09, depois de ler o histórico do Discord e o material
> visual que o Pedro e o Rafael trocaram em 24/09.** A versão anterior dizia que *"falta o eixo
> da entidade"*. 🔴 **Estava errado e teria sido injusto com o Pedro:** o modelo dele **tem
> entidade**. O que falta é outra coisa, e mais específica.

### 22.1 · 🟢 Onde os três convergem, e ninguém tinha notado

O infográfico **"Dois cadernos e um assistente"** (Pedro, 24/09) mostra o modelo dele por dentro:

```
empresa-acme/  politicas/ · padroes/ · areas/ · habilidades/ · automacoes/
joana-lima/    pessoas/ · reunioes/ · projetos/ · inbox/ · habilidades/ · tarefas.md
```

🟢 **Entidade é arquivo.** Uma nota por pessoa, uma por reunião, uma por projeto — e os laços por
wikilink (`[[pessoas/marcos]]`). **É exatamente a regra deste corpus:** *tudo é `.md` com nó;
linha de tabela não é nó de grafo.*

⚠ **Chegamos à mesma conclusão por caminhos independentes, e isso é evidência forte a favor
dela.** 🔴 **Não é divergência: é o ponto de partida comum que os dois planos escritos não
registraram.**

### 22.2 · 🔴 A diferença real: como a afirmação é indexada dentro do arquivo

| | Pedro | João | Este corpus |
|---|---|---|---|
| **entidade** | 🟢 arquivo por pessoa/reunião/projeto | ⚠ `tema` livre + `relação` (arestas) | 🟢 arquivo, em hierarquia de 4 níveis com **semântica fixa** |
| **afirmação dentro** | ⚠ **texto e afirmação datada de chave livre** | ⚠ trecho com proveniência | 🟢 **`chave: valor — [fonte · data]`, chave de lista FECHADA** |
| **como se acha** | 🟢 **busca por significado** (`pgvector`) | busca + grafo | ⚠ **exata, por chave** — e `grep`, que é a lacuna da § 25 |

🟢 **A busca semântica dele acha o que a minha não acha.** 🔴 **E a chave fechada cruza o que a
dele não cruza:** para responder *"quais clientes usam qual ERP"* a busca por significado
devolve **um ranking**; a chave `erp` devolve **a lista**. ⚠ **São perguntas diferentes e o
produto precisa das duas.**

> 🔴 **O risco que só a chave fechada elimina:** duas notas sobre a mesma coisa, com rótulos
> diferentes, **nunca se encontram — e ninguém é avisado.** A busca por significado **acerta e
> erra em silêncio**; a chave fora da lista **é acusada**.

### 22.3 · ⚠ E a tela de Contextos perdeu a estrutura que o modelo do Pedro tem

A tela filtra por **origem** — `Todos · 128 / Enviados · 34 / Agenda · 61 / E-mail · 33 /
Empresarial` — e **não mostra em que pasta, de que entidade, sob que chave** o item vive.

🟢 **Não é descuido do Rafael, e agora dá para dizer por quê:** o desenho dele nasceu do
**fluxo** (`Contextos → Aprovações → Tarefas`, como no quadro branco de 24/09), e o fluxo é a
vista certa para explicar o produto. ⚠ **A vista de pasta — a do infográfico do Pedro — é outra,
e ela some quando só existe a do fluxo.** 🔴 **Com 128 itens isso não aparece. Com 2.660,
a tela vira uma lista de 2.660 linhas filtrável por origem.**

### 22.4 · 🟢 O que a ontologia acrescenta, em uma frase

> **Contexto não é um item numa lista nem só um arquivo numa pasta. É uma afirmação sobre uma
> entidade, num nível da hierarquia, sob uma chave de vocabulário controlado, com fonte e data.**

**O que já opera aqui e nenhum dos dois tem:**

1. **Hierarquia de 4 níveis com semântica fixa** — `Instituição → Institucional → Áreas →
   Subáreas → Pessoas`, com **14 áreas canônicas de cliente** e **8 internas**.
   ⚠ **A pasta do Pedro é livre; esta é travada** — e é o que permite comparar clientes entre si.
2. **Vocabulário fechado de 35 chaves.**
3. **Identidade por e-mail, nunca por nome.**

## 23 · 🟢 `ACRÉSCIMO` — mecanismos que operam aqui e viram requisito

| Mecanismo em operação | Por que nasceu | Requisito para o BrainHub | Encaixe |
|---|---|---|---|
| **Vocabulário fechado de 35 chaves.** Afirmação só existe sob chave da lista; chave nova entra no protocolo primeiro, por decisão humana | chave livre não se cruza: duas notas sobre a mesma coisa com rótulos diferentes **nunca se encontram, e ninguém é avisado** | `contentKey` é **`enum`**, não texto. Chave fora da lista é **recusada na escrita e acusada no validador** | **F33** · F05 |
| **Identidade por e-mail na ESCRITA, com recusa de escolher.** Nome de um token nunca resolve; dois candidatos = `ambíguo`, e ambíguo não se escolhe | 23/09: o falante `Juliana` de uma reunião da CAEDU casou com `juliana@osklen.com.br` — **pessoa de outro cliente**. Há **duas `Fernanda` e dois `Pedro`** nas fichas | Resolução de pessoa **antes de gravar**, com escopo do próprio tenant e **abstenção explícita**. 🟢 **Complementa a guarda de identidade do Pedro (§ 15), que age na recuperação** | **F35** · F04, F06 |
| **Ausência VERIFICADA.** `não consta em <fonte> · <data>` é diferente de `[sem fonte]` | uma diz *"procurei ali, naquele dia, e não havia"*; a outra diz *"ninguém olhou"*. **Tratar as duas igual faz a busca que já falhou ser refeita para sempre** | Valor de primeira classe, com fonte e data. 🟢 **É a outra metade do livro de lacunas do Pedro:** o dele diz *"não sei"*, este diz *"olhei ali e não tinha"* | **F34** · F07 |
| **Procedência por cadeia declarada.** `blockquote da seção → linha de valor → preâmbulo do bloco pai → cabeçalho`. **Se nenhum nomeia fonte, sai `[sem fonte]`** | 22/09: um casamento frouxo atribuiu *"planilha de contratos do Financeiro"* a **51 fatos** que ela nunca tocou — o padrão casava com o **nome da área** `11_Financeiro` | Procedência **herdada por cadeia explícita**, nunca inferida. 🔴 **Herdar de onde não foi declarado é alucinação com cara de conveniência** | **F36** · F05 |
| **Um assunto, um dono.** Documento novo que vira autoridade marca o anterior `SUPERSEDED` **no que perdeu**, apontando o sucessor | dois documentos vivos sobre o mesmo tema divergem sem ninguém notar | `subjectOwner` por documento; **promoção exige declarar o que o anterior perde** | **F37** · F08 |
| **Manifesto verificável por script.** Todo MD estrutural é citado num manifesto; **órfão é bug, não descuido** | arquivo fora do índice deixa de existir para quem busca. 🟢 **Converge com o achado do Pedro:** 112 reuniões salvas e invisíveis porque a pasta ficava fora do indexador | **Teste de cobertura:** todo item importado aparece no índice, e o painel conta importados × indexados | F04 |
| **Validador ACUSA, nunca corrige.** 5 validadores: forma de fato, padrão de MD, manifesto, indexação, números | **validador que conserta esconde o defeito** e o corpus passa a mentir com aparência de saúde | Verificação **separada da correção**. ⚠ Correção automática exige decisão registrada | **F38** |
| **Escrita só onde há `[a preencher]`.** Nenhum script sobrescreve valor existente | 23/09: um script de enriquecimento **apagou o valor bom de 20 clientes** — recuperado do Git | Importador e agente **escrevem em lacuna, não por cima**. Sobrescrever exige CAS + versão perdedora preservada | F05 |
| **Estrutura não varia entre MDs do mesmo tipo.** Conteúdo varia; títulos e seções, nunca | 25/09: escrevi uma seção nova em **24 dos 48** `jornada.md` — nos outros 24 ela não existia. **Corrigido completando os 48**, com ausência verificada onde não havia dado | **Esquema por classe de documento**, validado. 🔴 **Preencher só onde há dado produz duas classes de documento com o mesmo nome** | F38 |
| **`[a preencher]` sobrevive à importação.** São **41.976** ocorrências | 🔴 **preencher lacuna com valor plausível contamina o brain com dado inventado** — e ele passa a parecer conhecimento | Importador **não preenche nada**. 🟢 Converge com o PRD § 13 e com a lição dos **208 arquivos** do Pedro | F04 |
| **Marca de vigência de pessoa.** Fato que resolve para alguém desligado **fica, e ganha marca** | 25/09: **10 fatos `atendimento` apontando para pessoas desligadas**, 5 clientes para uma cuja ficha **já dizia `Inativo`**. O resolvedor lia nome e e-mail e **não lia o status** | 🟢 **O fato não se apaga — foi verdade.** Ganha marca e **o roteador ignora o marcado**. É a metade barata da validade: não diz **quando** deixou de valer, diz **que** não vale mais | **F39** · F27 |

## 24 · 🔴 O que eu errei — o log, com data

⚠ **Esta seção existe pelo mesmo motivo da § 16 do Pedro:** cada regra da § 23 nasceu de um erro,
e **uma parte sem o próprio log de erro vale menos.** Os piores são os de detecção frouxa.

| Data | O erro | O que ele ensinou |
|---|---|---|
| **22/09** | **Fonte fabricada em 51 fatos** — o padrão `Financeiro` casou com o nome da área | condição frouxa vira afirmação com procedência |
| **23/09** | 🔴 **Procedência fabricada em 672 linhas.** Detectei "cliente tem tabela de usuário" testando se um campo tinha valor — o valor dominante era `Nenhuma`, então **48 de 48 clientes foram julgados como tendo tabela. Eram 4** | 🟢 **Medir o resultado da detecção ANTES de escrever.** `48/48` é suspeito; `4/48` é plausível |
| **23/09** | **20 clientes sobrescritos** com valor bom apagado | script escreve em lacuna, nunca por cima |
| **23/09** | **529 áreas afirmando `Nenhuma.`** para pessoas quando só faltava fonte | **ausência de fonte não é ausência de coisa** |
| **23/09** | Declarei o **export de julho indisponível** — estava no histórico do Git. E **módulos inexistentes** — o clone era `--single-branch` | **"não encontrei em X" nunca é "não existe"** |
| **24/09** | **Quase apaguei `SMB`** do campo de atendimento achando que era lixo. **Era resposta:** conta sem CS dedicado | valor que parece sujeira pode ser semântica |
| **25/09** | Ia derivar `Quem aprova` de **997** `Aprovação necessária: Não`. **Era default de importação**, e o protocolo nem define o campo | **997 valores iguais não são 997 decisões** |
| **25/09** | 🔴 **Declarei que NÃO EXISTE fonte de desligamento.** Existe — o organograma do Notion, com nome, data e código de decisão | **varri duas bases e declarei sobre o universo** |
| **25/09** | 🔴 **Chamei a falta de validade de "dívida latente, não dor atual".** Horas depois achei os 10 fatos apontando para gente desligada — **que eu mesmo produzi na véspera** | ⚠ **O termômetro estava errado:** eu media por linhas `CONFLITA`, e conflito só acende quando **duas fontes discordam**. **Sucessão silenciosa não produz conflito nenhum** — produz um fato antigo que continua parecendo vigente |
| **25/09** | Publiquei um parecer dizendo **6 validadores**. São **5** | 🟢 **O validador de números só cobre o painel.** Número errado em documento que circula passa batido — virou **F38** |

## 25 · 🔴 O que falta aqui, sem disfarce

| # | Lacuna | Medida |
|---|---|---|
| 1 | 🔴 **Nada disto RODA** | **28 scripts, todos em lote**, disparados por uma pessoa numa sessão. **Zero rotina contínua, zero consolidação, zero recuperação por turno.** O corpus é lido por uma pessoa, não por um sistema |
| 2 | 🔴 **Zero avaliação de substância** | **5 validadores de FORMA** e **nenhum de acerto**. **Não há como dizer se uma pergunta é respondida certo.** O Pedro mede **0,811**; aqui não se mede nada |
| 3 | 🔴 **3.438 afirmações, ZERO com intervalo de validade** | a data gravada é a da **fonte**, não o período de vigência. **É a lacuna que produziu o erro de 25/09** |
| 4 | 🔴 **Busca é `grep`** | zero índice vetorial, zero embedding |
| 5 | 🔴 **Nada dorme, nada é podado** | o corpus só cresce |
| 6 | ⚠ **Sem `sha256` na fonte** | 🟢 **falta nos três** — o João exige na migração, o Pedro diz "no papel, sem operar", aqui não existe |

🟢 **As lacunas 1 a 5 são exatamente a camada do Pedro.** ⚠ **Isso não é coincidência: é a
evidência de que as três camadas se encaixam em vez de competir.**

## 26 · Features novas e acréscimos

Continuando o catálogo (§ 5 do João, § 19 do Pedro), mesma legenda de fase.

| ID / fase | Backend e dados | Frontend / experiência | Critério técnico de aceite |
|---|---|---|---|
| **F33 M0** | `contentKey` como **`enum`** de vocabulário fechado; alteração da lista é migração versionada | admin lista o vocabulário vigente | escrita com chave fora da lista é **recusada**; validador acusa chave livre no acervo; **lista nova exige migração, não só append** |
| **F34 M1** | Ausência verificada: `{fonte, data, resultado: vazio}` como valor | campo mostra *"não consta em X · data"*, **nunca vazio mudo** | busca que já falhou **não se repete** dentro da validade; `[sem fonte]` e ausência verificada **nunca colapsam no mesmo estado** |
| **F35 M1** | Resolução de entidade **antes de gravar**, escopo do tenant, abstenção explícita | fila "quem é esta pessoa?" | nome de um token **nunca** resolve; dois candidatos = `ambiguous` e **nada é gravado**; caso negativo cross-tenant no teste |
| **F36 M0** | Cadeia de procedência declarada; sem cadeia → `[sem fonte]` | origem visível no item, com o elo que a produziu | **procedência nunca é inferida**; teste com documento sem fonte declarada deve sair `[sem fonte]`, não herdar do pai |
| **F37 M2** | `subjectOwner` por documento; promoção declara o que o anterior perde | aviso de "já existe documento sobre este assunto" | dois documentos vivos sobre o mesmo assunto **acusam**; `SUPERSEDED` exige apontar sucessor e o que foi perdido |
| **F38 M1** | Validador que **acusa e não corrige**, cobrindo **todo documento que afirma contagem** | painel de desvios | correção automática **não existe** sem decisão registrada; **número afirmado em qualquer documento é conferido contra o acervo** |
| **F39 M1** | Vigência de pessoa: fato que resolve para desligado **fica e é marcado** | endereçamento mostra "pessoa desligada — sucessor?" | fato marcado **nunca** é usado como endereço de aprovação; **o fato não é apagado** |

### 26.1 · Acréscimos a features existentes

- **F04** — importador **não preenche lacuna nenhuma**; `[a preencher]` sobrevive à importação, com contagem no relatório.
- **F05** — escrita em lacuna, nunca por cima; chave de afirmação vem do `enum` de F33.
- **F06** — 🟢 **guarda de identidade em DOIS pontos**: a do Pedro na recuperação, a de F35 na escrita.
- **F08** — item declara **destino organizacional** (entidade + nível), não só escopo de permissão.
- **F27** — consolidação respeita **ausência verificada**: não reabre busca que já falhou dentro da validade.

### 26.2 · Onde entram nas sprints

**S1:** F33, F36 e os acréscimos de F04 e F05. **S2:** F34, F35, F39 e o acréscimo de F06.
**S3:** F38 e o acréscimo de F08. **S5:** F37 e o acréscimo de F27.
⚠ **Nenhuma altera o caminho crítico da § 11.** 🔴 **F33 e F36 são de M0 por dependência, não por
prioridade: chave e procedência definidas depois do primeiro dado real obrigam retrofit.**

## 27 · ⚠ `DIVERGÊNCIA` e 🔴 `PEDIDO` — o que precisa de decisão de quem é dono

| # | Onde | O que o documento diz | ⚠ Como eu leio | 🔴 Pedido, e para quem |
|---|---|---|---|---|
| 1 | **os dois planos** | contexto flui por um cano com fonte, tier, validade e peso | **falta o eixo da entidade** — § 22. **A tela plana é o sintoma** | **João + Pedro:** aceitar `contentKey` + `scope` como colunas de primeira classe desde o S0 |
| 2 | **Pedro § 15** | camada derivada com afirmações datadas, **chave livre** | 🟢 **proposta que resolve os dois de uma vez:** a chave vira o `enum` de F33. **Dá vocabulário controlado a ele e validade a mim** | **Pedro:** aceitar chave controlada na camada derivada |
| 3 | **João § 6 · D144** | promoção autônoma **suspensa** | ⚠ **enquanto estiver suspensa o produto entrega uma pasta com busca.** Não peço revogar; peço **data e critério de reativação** | **João:** decidir antes do M1 |
| 4 | **João § 9** | migração preserva identidade, tema, tier e relação | ⚠ **`refs[:32]` e allowlist de frontmatter truncam** — o próprio plano chama de dívida | **João:** bloqueio explícito em vez de truncamento silencioso |
| 5 | **Pedro § 16** | fila de aprovação recebe só a faixa vermelha | 🟢 **concordo, e acrescento:** a faixa não cobre **juízo sobre pessoa identificável** — nem tier de dado pessoal cobre. **Proposta `T0-P`:** existe, nunca por valor | **Pedro + João:** aceitar o eixo |
| 6 | **desenho do Rafael** | `Aprovações` com dois desfechos | falta **`Alterar`** — 🟢 **o único que mostra a distância entre o que a IA propôs e o que estava certo** | **Rafael:** terceiro botão |
| 7 | **os três** | — | 🔴 **quatro nomes para a mesma coisa** nos três documentos (heartbeat × prova de trabalho; promoção assistida × portão de integridade) | **os três:** **glossário único antes de merge de código.** O da § 3 do João é o candidato |

## 28 · Fontes e limites desta parte

- `[C]` **Corpus `HyTrackWater/brainhub-umode`**, medido em 25/09/2026: números da § 21.3 lidos por script no repositório.
- `[C]` **Plano do João**, § 1–13, versão de 24/09. `[C]` **Parte III do Pedro**, § 14–20, versão `202609242058`.
- `[C]` **Desenho de telas do Rafael Rocha** e **PRD v1**. `[C]` **Duas transcrições de 24/09.**
- `[C]` **Organograma uMode — V2 / V4 (D75)**, Notion, lido em 25/09 — só leitura.
- 🔴 **Limite declarado:** **não li o repositório do Pedro.** Tudo que esta parte diz sobre o
  cérebro dele vem do que ele **descreve**, não do que ele **tem**. ⚠ **Os seis artefatos que
  fecham isso estão no parecer de 25/09, § 7** — e dois deles, o esquema da camada derivada e o
  gold set, fecham 80% sozinhos.
- ⚠ **Nenhum código, banco ou infraestrutura foi tocado.** Os números mudam a cada sessão; valem
  como ordem de grandeza em 25/09/2026.

## Governança

### Quem pode alterar este documento
Vinicius. ⚠ **As divergências da § 27 não se resolvem aqui** — cada uma tem destinatário nomeado,
e a resolução vira registro novo apontando para este.
