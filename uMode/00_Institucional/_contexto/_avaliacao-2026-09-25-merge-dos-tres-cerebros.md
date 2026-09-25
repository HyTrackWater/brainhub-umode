---
aliases:
  - "Avaliação — o merge dos três cérebros e o desenho do Rafael"
tags:
  - tipo/avaliacao
  - casa
---
# Avaliação — o merge dos três cérebros e o desenho do Rafael

> **Classe: `AVALIAÇÃO`.** Parecer datado, para circular com o João Risoléo e o Pedro Mafra.
> **Escrito em 25/09/2026**, a pedido do Vinicius, sobre: o plano técnico do João (24/09), o
> complemento Parte III do Pedro (24/09), o desenho de telas do Rafael Rocha, o PRD v1 e as duas
> transcrições de 24/09.
>
> **Graduação de evidência usada em todo o texto:** `[C]` li o documento ou o código e cito onde ·
> `[F]` existe mas está atrás de trava ou não opera · `[P]` proposta minha, não validada ·
> `[D]` decisão que não é minha.

## 0 · 🔴 O que esta avaliação NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | 🔴 **Não dá veredito sobre o cérebro do Pedro** | **não tenho o repositório dele.** Li o que ele descreve, não o que ele tem. § 7 lista os 6 artefatos que fecham isso |
| 2 | **Não mede nenhum dos três** | `[C]` só o do Pedro tem avaliação (0,811). **Do João e do meu não existe número de acerto** — § 4 |
| 3 | **Não valida o desenho do Rafael contra volume real** | o protótipo tem **128 itens fictícios**. O meu corpus tem **2.659**. § 5 é sobre o que quebra nessa diferença |
| 4 | **Não decide arquitetura** | `[D]` banco, infra e prazo foram decididos na reunião 2. Aqui é estrutura e organização de conhecimento |

## 1 · 🟢 A tese: não são três versões da mesma coisa — são três CAMADAS

**O erro fácil seria escolher um e descartar dois.** Lendo os três, o que aparece é outra coisa:
cada um é forte exatamente onde os outros são ausentes.

| Cérebro | O que ele é, de fato | Evidência |
|---|---|---|
| **Pedro Mafra** | 🟢 **O RUNTIME.** A memória que opera: recuperação por turno, consolidação periódica, dormência, guarda no ponto de passagem | `[C]` **92 agentes**, 2 nós, **~8.300 afirmações datadas**, **77 habilidades**, avaliação **0,811** (base 0,70 em 06/06) |
| **João Risoléo** | 🟢 **A GOVERNANÇA.** O que pode virar verdade, quem decide, e a prova de que a rotina trabalhou | `[C]` `DECISOES.md` D144/D145 · tier **T0–T3 por arquivo** · esteira com invariante declarado · *"exit 0 não prova trabalho"* · `skills/` fonte única com projeção conferida por `--check` |
| **Meu (`brainhub-umode`)** | 🟢 **A ONTOLOGIA.** O que as coisas SÃO e como se ligam | `[C]` hierarquia de 4 níveis · 4 tipos de MD por cliente · **vocabulário fechado de 35 chaves** · identidade por e-mail · ausência verificada · um assunto, um dono |

🔴 **Nenhum dos três tem as outras duas camadas.** E o desenho do Rafael pressupõe que as três
existem.

### 1.1 · 🟢 A prova de que se completam, e não competem

Três pares onde um resolve exatamente a metade que falta no outro:

| Problema | Pedro tem | Eu tenho | 🟢 Juntos |
|---|---|---|---|
| **Identidade errada** | `[C]` **guarda de identidade na RECUPERAÇÃO** — filtro de entidade depois do ranking (24/08: histórico de uma pessoa apresentado como de outra; *"qwerty"* pontuou **1,315**) | `[C]` identidade por e-mail na **ESCRITA** — resolvedor que devolve *ambíguo* e **nunca escolhe** (`Juliana` da CAEDU casou com `juliana@osklen.com.br`) | **uma protege a leitura, a outra protege a gravação.** Nenhuma sozinha fecha |
| **O que não se sabe** | `[C]` **livro de lacunas** — registra o que percebeu que não sabe (12/08: **171 perguntas abertas**) | `[C]` **ausência VERIFICADA** — `não consta em X · data`. **1.897 das minhas 3.438 linhas** (55%) são isso | a dele diz *"não sei"*; a minha diz *"procurei em X, no dia Y, e não havia"*. 🟢 **Juntas, a lacuna não reabre pela mesma busca que já falhou** |
| **Sensibilidade** | 🔴 **ele declara que NÃO tem** o eixo sensível na entrada | `[C]` escada escrita — ⚠ **e descobri em 25/09 que ela não cobre juízo sobre pessoa** (`T0-P`) | o do João tem tier na origem; **os três precisam do eixo, e nenhum o tem completo** |

## 2 · 🔴 Quatro nomes para a mesma coisa — e isso é o defeito que os três criticam

| O mecanismo | João chama de | Pedro chama de | Eu chamo de |
|---|---|---|---|
| provar que a rotina trabalhou | **heartbeat** · *"exit 0 não prova trabalho"* | **prova de trabalho em três graus** | 🔴 **não tenho** |
| o que pode virar verdade | **promoção assistida** (§ 3-bis) | **portão de integridade** (4 classes) | **`protocolo-fato-atomico` § 6** |
| não apagar | **canonicidade** — perdedor vai para histórico | **nada se apaga, tudo dorme** | **conflito: as duas linhas ficam** |
| fonte obrigatória | **autor / turno / trecho** | **afirmação com proveniência** | **`— [fonte · data]`, 35 chaves** |

🔴 **Quatro nomes para a mesma coisa, em três documentos, é literalmente o que o `CLAUDE.md`
descreve:** *"palavra diferente para a mesma coisa é como dois times passam meses achando que
combinaram algo"*. ⚠ **Antes de qualquer merge de código, precisa haver merge de vocabulário** —
e o glossário do João (§ 3) é o melhor candidato a dono, porque já separa `habilidade` de `agente`
de `loop` de `rotina`.

## 3 · O que falta em cada um, sem adjetivo

### 3.1 · 🔴 No meu, e é a parte mais dura

| # | Lacuna | Medida |
|---|---|---|
| 1 | 🔴 **Nada meu RODA** | `[C]` **28 scripts, todos em lote**, disparados por mim numa sessão. **Zero rotina contínua, zero consolidação, zero recuperação por turno.** O corpus é lido **por mim**, não por um sistema |
| 2 | 🔴 **Zero avaliação de substância** | `[C]` tenho **6 validadores de FORMA** (acusam chave fora do vocabulário, data, manifesto órfão, número divergente) e **nenhum de acerto**. **Não sei dizer se uma pergunta é respondida certo.** O Pedro mede 0,811; eu não meço nada |
| 3 | 🔴 **3.438 fatos, ZERO com intervalo de validade** | `[C]` a data que gravo é a da **FONTE**, não o período em que o fato vale. **Consequência: trato sucessão como contradição** — a regra § 2.2 manda deixar as duas linhas com `⚠ CONFLITA`. A contraparte da CAEDU **mudou 4 vezes em 2 anos**; é o caso que prova a necessidade |
| 4 | 🔴 **Busca é `grep`** | `[C]` **zero índice vetorial, zero embedding.** Funciona em 2.659 arquivos **comigo lendo**; não funciona com agente respondendo em produção |
| 5 | 🔴 **Nada dorme, nada é podado** | o corpus só cresce |

> ⚠ **Honestidade sobre o item 3:** hoje há **apenas 2** linhas `CONFLITA`. **O custo ainda não
> apareceu** porque o corpus é jovem e quase tudo tem fonte única. 🔴 **É dívida latente, não dor
> atual** — e a camada de afirmações datadas do Pedro é exatamente o conserto.

### 3.2 · No do João

| # | Lacuna | Evidência |
|---|---|---|
| 1 | 🔴 **A promoção autônoma está SUSPENSA** | `[F]` `DECISOES.md` D144@2026-09-11 suspende, e **o plano não a revoga.** ⚠ **Um brain que não promove nada sozinho é uma pasta com busca** |
| 2 | ⚠ **O importador trunca** | `[C]` `vault_para_manifesto.py:69–95` — `refs[:32]` e allowlist de frontmatter. **O próprio plano chama de dívida do importador** |
| 3 | 🔴 **Não tem o runtime de consolidação** | `[C]` o próprio Pedro aponta (§ 18, ponto 5): *"M1 tem rotina durável e loop mínimo; não tem consolidação da memória"* |
| 4 | 🔴 **Matéria-prima parada** | `[C]` **206 transcrições + 598 áudios** sem processar (medido em 23/09) |

### 3.3 · No do Pedro — declarados por ele mesmo

| # | Lacuna |
|---|---|
| 1 | 🔴 **Não tem o eixo "sensível" na classificação de entrada.** O Vault tem. `[C]` § 15 |
| 2 | ⚠ **`sha256` na fonte: no papel, sem operar.** *"o linter está pronto e nenhuma nota tem o campo"* |
| 3 | ⚠ **Segundo motor sem uso**: a tabela Claude↔Codex está vazia; **nenhuma rotina de produção usa Codex** |
| 4 | 🔴 **171 perguntas abertas sem ninguém fechar** (12/08) — o livro de lacunas enche e não esvazia |

### 3.4 · 🔴 O que falta nos TRÊS

1. `[C]` **Promover classificador de LLM para regra determinística depois de medir a acurácia** — o Pedro nomeia.
2. `[C]` **Crivo de entrada para agente NOVO** — os três só têm crivo para o agente **agir**, nenhum para o agente **entrar**.
3. 🆕 **`sha256` na fonte bruta.** ⚠ **Os três especificam e nenhum opera** — o João exige na migração, o Pedro diz que está no papel, eu tenho zero.
4. 🆕 **Avaliação.** Só o Pedro tem. 🔴 **O João e eu voamos sem instrumento.**

## 4 · 🔴 O desenho do Rafael: o que ele assume e nenhum cérebro entrega

⚠ **Nada aqui é crítica ao trabalho dele.** O protótipo tem **128 itens fictícios** e cumpre o que
se propôs: dar clareza de produto — e conseguiu, tanto que ele próprio disse na reunião 1 que só
depois do fluxograma passou a saber o que construir. 🔴 **O que segue é o que quebra quando entram
2.659 arquivos reais.**

| # | Tela | 🔴 O que falta | Por que importa |
|---|---|---|---|
| 1 | **Contextos** | 🔴 **A tela é PLANA.** Filtra por **origem** (`Todos · 128 / Enviados · 34 / Agenda · 61 / E-mail · 33 / Empresarial`) e **não tem onde mostrar ONDE o contexto mora** | **Nenhum dos três cérebros é plano.** O meu é hierarquia de 4 níveis; o do Pedro é pasta por tipo (`pessoas/`, `reunioes/`, `projetos/`); o do João é por tema com tier. 🔴 **"Onde mora" decide quem lê, quem aprova e o que o agente recupera.** Sem isso, meus 2.659 arquivos viram **uma lista de 2.659 linhas** |
| 2 | **Aprovações** | 🔴 Só **dois** desfechos (`Sim, cria` / `Agora não`) e **nenhuma faixa** | (a) falta o terceiro, **`Alterar`** — 🟢 **é o único que mostra a distância entre o que a IA propôs e o que estava certo** (PRD § 4.4; Pedro F31). (b) 🔴 **o exemplo da própria tela** — *"você comentou que ia olhar a documentação, crio uma tarefa?"* — **é faixa verde/amarela: pelo desenho do Pedro esse card não deveria existir.** E ele mediu o efeito: **fila grande faz a pessoa parar de ler** |
| 3 | **Integrações** | 🔴 Mostra `Ativa` e nada mais | **`Ativa` é booleano; saúde é medida.** Os três têm noção de cadência — heartbeat (João), atraso > 1,5× a cadência + 30 min (Pedro), `expected_cadence` (PRD § 4.2). 🔴 **Fonte que parou há 3 dias aparece como `Ativa`** |
| 4 | **Agente** | 🟢 **cita fonte em chips — isto está certo e é o requisito mais importante.** ⚠ Falta a **abstenção** | o Pedro fica calado abaixo do limiar e desiste em **8 s**. 🔴 **Sem isso a busca sempre devolve um primeiro colocado** — foi assim que *"qwerty"* pontuou 1,315 |
| 5 | **Linhagem** | 🔴 **não existe no desenho** | está no PRD (T11). **Sem ela não há como responder "por que o agente fez isso"** — é a prova de auditoria |
| 6 | **Habilidades** | 🔴 **não tem tela** | 🔴 **Habilidade não é contexto** — o Vinicius travou isso na reunião 2 e o glossário do João separa. O Pedro mediu: com **75 habilidades, 22 entravam sem descrição** porque a listagem tem teto |
| 7 | **Saúde / Loops / Brain Empresarial** | 🔴 não existem no desenho; existem no PRD (T10, T13, T14) | são o que diferencia o produto de um assistente de agenda |

## 5 · 🟢 O que precisa adequar para caber

### 5.1 · O meu corpus

🟢 **O eixo de ESCOPO cabe quase direto.** `organizations` / `org_units` / `brains` do PRD já
mapeiam `Instituição → Áreas → Subáreas → Pessoas`; a tabela de correspondência está no PRD § 13.

🔴 **O que NÃO cabe é o bloco `## Fatos`.** 3.438 afirmações com chave de vocabulário fechado
**não têm coluna no modelo do João nem no do Rafael.** O `ContextItem` guarda o documento; o fato
atômico é **camada derivada** — que é exatamente a *camada derivada* do Pedro e o `ContextRevision`
do João.

> 🟢 **`[P]` Proposta, e ela resolve dois problemas de uma vez:** o `## Fatos` vira a **tabela de
> afirmações datadas**, e o **vocabulário fechado de 35 chaves vira o `enum` dela**.
> **Dá chave controlada ao Pedro** — que hoje tem afirmação livre — **e dá validade ao meu**, que
> hoje não tem. ⚠ **Chave livre quebra o cruzamento em silêncio**; é a razão de o vocabulário ser
> fechado.

🔴 **`[a preencher]` precisa sobreviver à importação.** São **41.976 ocorrências**. O PRD § 13 já
trava: *"o importador não pode preencher lacuna nenhuma, sob pena de contaminar o brain com dado
inventado"*. ⚠ **E o precedente existe: a lição dos 208 arquivos do Pedro é um importador que
copiou o que não devia.**

### 5.2 · O do João

- A esteira e o tier viram `SourceArtifact` + atributo obrigatório — já está no plano dele § 9.
- 🔴 **`[D]` D144 precisa de decisão explícita antes do M1.** Enquanto a promoção autônoma estiver
  suspensa, **o produto entrega uma pasta com busca.**

### 5.3 · O do Pedro

- Os 15 mecanismos já viraram F26–F32 e acréscimos a F04–F15 — **ele já fez esse trabalho.**
- 🔴 **Falta o eixo sensível na entrada** — e é o do João e o meu que entram ali.

## 6 · 🟢 A recomendação, e é uma só

**Não escolher um dos três. Nomear qual camada cada um é dono, e construir a interface entre elas.**

| Camada | Dono proposto `[P]` | O que ele entrega ao produto |
|---|---|---|
| **Ontologia** — o que as coisas são | **este corpus** | hierarquia, os 4 tipos de MD, o vocabulário fechado, identidade por e-mail, ausência verificada |
| **Governança** — o que pode virar verdade | **Vault do João** | tier, esteira com invariante, política de promoção, prova de trabalho, glossário |
| **Runtime** — a memória que opera | **cérebro do Pedro** | recuperação por turno, consolidação, dormência, guardas no ponto de passagem, avaliação |

⚠ **E a primeira entrega do merge não é código: é o glossário único.** § 2 mostra quatro nomes
para a mesma coisa. 🔴 **Merge de código antes de merge de vocabulário produz exatamente o que os
três documentos criticam.**

## 7 · 🔴 O que eu preciso do Pedro para fechar o veredito

⚠ **Pedir "o repositório" é pedir demais e obter pouco.** Estes **seis artefatos** fecham a
comparação — e **cada um responde a uma pergunta que hoje eu não sei responder**:

| # | Artefato | A pergunta que ele responde |
|---|---|---|
| 1 | **A árvore de pastas real dos dois brains** (empresa e pessoal) | o HTML mostra o modelo **proposto**. 🔴 **Preciso do que existe** para comparar com a minha hierarquia de 4 níveis |
| 2 | 🔴 **O esquema da camada derivada** — campos de uma afirmação datada: validade, confiança, saliência, dormência, `substituída por` | **é exatamente o que falta no meu** (§ 3.1, item 3). **É o artefato mais importante da lista** |
| 3 | **As 77 habilidades** — nome, descrição de uma linha, gatilhos | habilidade é **fato**, **procedimento** ou **política**? É a confusão que o glossário do João separa e que a reunião 2 levantou |
| 4 | 🔴 **O gold set da avaliação** — perguntas e respostas esperadas | **é o que eu não tenho.** Me diz se o meu corpus responde certo, e não só se está bem formado |
| 5 | **O painel da frota** — as 92 rotinas com cadência e prova de trabalho declaradas | o formato da **prova de trabalho em três graus**, que eu quero adotar |
| 6 | **Uma nota de reunião e uma de pessoa, reais, com frontmatter** | comparar **campo a campo** com a minha ficha de pessoa, que usa `### Email` como chave de identidade |

🟢 **Com 2 e 4 eu já fecho 80% do veredito.** ⚠ **Sem eles, o que escrevo sobre o cérebro do Pedro
continua sendo leitura do que ele descreve, não do que ele tem** — e a diferença entre as duas
coisas é o assunto deste documento inteiro.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É parecer datado. **Revisão entra como documento novo**, apontando para este.

### Conexões
- [`_espec-pipeline-de-contexto-e-aprovacao.md`](_espec-pipeline-de-contexto-e-aprovacao.md) — os
  quatro eixos, `T0-P` e o laço de aprendizado.
- [`_dicionario-de-papeis-e-enderecamento.md`](_dicionario-de-papeis-e-enderecamento.md) — para
  quem vai a aprovação.
- [`protocolo-fato-atomico.md`](../_protocolos/protocolo-fato-atomico.md) — as 35 chaves que a § 5.1
  propõe virar `enum`.
