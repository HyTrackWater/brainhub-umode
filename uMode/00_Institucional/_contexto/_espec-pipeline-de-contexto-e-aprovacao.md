---
aliases:
  - "Espec — o pipeline de contexto, aprovação e aprendizado"
tags:
  - tipo/espec
  - casa
---
# Espec — o pipeline de contexto, aprovação e aprendizado

> **Classe: `ESPEC`.** 🔴 **Dono único do assunto "sensibilidade, endereçamento e aprovação de
> contexto".** Até 25/09/2026 esse assunto não tinha dono: a escada de tier morava dentro de um
> protocolo de call, e o critério de relevância não existia em lugar nenhum.
>
> **Pedido do Vinicius em 25/09/2026:** traçar o plano do agente — ou time de agentes — que pega
> transcrição, decide o que importa, o que é sensível, **para onde endereçar**, obtém aprovação de
> quem é dono daquele contexto, e **transforma cada aprovação, reprovação e alteração em
> aprendizado.**

## 0 · 🔴 Declaração de completude — o que esta espec NÃO resolve

| # | Lacuna | Evidência |
|---|---|---|
| 1 | **Não decide base legal nem retenção de dado pessoal** | `[D]` `_espec-pessoas-e-comunicacoes.md` § 0.6 já declarava isso aberto. **Continua aberto, e agora com call interna entrando** |
| 2 | **Não cria camada de acesso** | `[C]` este repositório não tem uma. **Quem tem o repo tem tudo.** § 7 mitiga; não resolve |
| 3 | **Não destrava o `D85`** | `[F]` o banco trava tudo em `T2` até a política de T0/T1 ser resolvida. **A máquina de aprovação existe e está inerte** |
| 4 | **Não tem um só exemplo aprovado ou reprovado** | § 8. **O laço de aprendizado nasce com corpus zero** e isso não se disfarça |
| 5 | **Não roteia 35 dos 49 clientes** | `[C]` § 5.2. Só 14 têm `atendimento` resolvido para `pessoa:<e-mail>` |

## 1 · 🔴 A decisão do Vinicius que muda a premissa, registrada

Em 24/09 eu recomendei que **call interna de umoder não entrasse neste repositório** enquanto não
houvesse camada de acesso. **Em 25/09 o Vinicius decidiu o contrário**, e com razão declarada: o
material interno é justamente o **banco de prova** para treinar o agente que fará esse julgamento
todo dia.

🟢 **Decisão dele, registrada, e eu sigo.** ⚠ **O que muda é o mecanismo de proteção: deixa de ser
veto de entrada e passa a ser desenho.** § 7 é esse desenho.

⚠ **E fica explícito o compromisso desta sessão:** o material de 1:1, desempenho e desligamento
**entra na minha leitura para produzir critério.** 🔴 **O que entra no repositório é o critério que
ele produziu — nunca o teor.** *(Precedente já aplicado: as credenciais achadas no vault do João
foram registradas por referência, sem nenhum valor lido ou copiado.)*

## 2 · 🔴 O erro de desenho a não cometer: isto são QUATRO eixos, não um score

O Vinicius nomeou quatro perguntas, e a tentação é fundi-las numa nota só. **Não se funde.**

| Eixo | Pergunta | Quem responde |
|---|---|---|
| **A · Assunto** | do que isto trata? | classificador |
| **B · Relevância** | isto importa? | juiz de relevância |
| **C · Sensibilidade** | isto pode ser guardado, e por valor? | triador |
| **D · Endereçamento** | de quem é este contexto? | roteador |

🔴 **Os quatro são independentes.** Um fato pode ser **altamente relevante e altamente sensível**
— o salário de um umoder numa conversa de reestruturação é exatamente isso. **Fundir os eixos faz
o sistema decidir que o sensível é irrelevante, ou que o relevante é liberado.** ⚠ **É o mesmo
defeito que o banco já tem hoje** e que esta espec pede para corrigir — § 3.

## 3 · 🔴 `T0` significa duas coisas neste projeto, e ninguém tinha percebido

| Onde | `T0` quer dizer |
|---|---|
| nosso `protocolo-entrada-de-call.md` § 5 | **sensibilidade** — dado pessoal, nunca por valor |
| banco (`_dicionario-dados-brainhub.md` § 3) | **autoridade de aprovação** — `ApprovalTier`: `T0 · T1 · T2_DOCTRINE · T2_RECORD` |

E o banco declara `sensitivity` **do tipo** `ApprovalTier` `[C]` — **um enum fazendo dois
trabalhos.** ⚠ `T2_DOCTRINE` × `T2_RECORD` é doutrina contra registro: **isso é natureza de
conteúdo, não sensibilidade nem autoridade.** **Três eixos num enum.**

> 🔴 **É a armadilha que o `CLAUDE.md` trava, na forma inversa.** A regra escrita é *"palavra
> diferente para a mesma coisa é como dois times passam meses achando que combinaram algo"*.
> **Aqui é a mesma palavra para coisas diferentes, que é pior: ninguém percebe que discorda.**

### 3.1 · `[P]` Proposta — separar os eixos, e é item de espec

**Autoridade de desenho é nossa; o Bergson implementa** *(travado em 17 ago 2026)*. Logo isto não
é limitação a contornar, é correção a pedir:

| Campo | Tipo | Eixo |
|---|---|---|
| `sensitivity` | **`SensitivityTier`** — `T0 · T1 · T2` | **C** — pode guardar? por valor? |
| `approvalTier` | `ApprovalTier` — quem precisa aprovar | autoridade |
| `contentKind` | `DOCTRINE · RECORD` | natureza |
| `relevance` | `CANON · SUPPORT · DISCARD` | **B** — § 6 |
| `addressedTo` | `pessoa:<e-mail>[]` | **D** — § 5 |

⚠ **Enquanto o banco não separar, este repositório escreve `sensibilidade: T0` por extenso e
nunca `T0` solto.** 🔴 **`T0` sozinho, daqui em diante, é ambíguo e não se usa.**

## 4 · 🔴 Eixo C — sensibilidade, com a regra que faltava para call interna

A escada atual `[C]` protege **tipos de dado**. ⚠ **Ela não protege juízo sobre gente** — e é
disso que uma call de 1:1 é feita. *"A fulana não está dando conta"* não é CPF nem valor de
contrato: pela escada de hoje classifica `T2` e **vira canônico**.

### 4.1 · `[P]` A regra nova

| Tier | O que é | Tratamento |
|---|---|---|
| **`T0`** | CPF, telefone, endereço, senha, token, e-mail pessoal | 🔴 **nunca por valor** — registra que existe e em que minuto |
| **`T0-P`** `[P]` **novo** | 🔴 **juízo sobre pessoa identificável dito por terceiro** — desempenho, competência, permanência, conflito, saúde | 🔴 **nunca por valor, nem na ficha dela.** Registra **que existe, em que call, em que minuto, e quem é o dono da decisão** |
| **`T1`** | valor de contrato, preço, margem, negociação, salário, desligamento | só na pasta daquele cliente ou da pessoa; **nunca em documento da Casa** |
| **`T2`** | o resto | padrão |

🟢 **Por que `T0-P` e não um tier novo entre T1 e T2:** porque o tratamento correto **já é o
tratamento de T0** — *"registra que existe e onde"*. ⚠ **Não se inventa mecanismo quando o
mecanismo certo já está escrito**; inventar é o que multiplica regra e produz o defeito de dois
donos.

### 4.2 · As invariantes que não se relitigam

1. 🔴 **Fail-closed.** Na dúvida, o mais restritivo.
2. 🔴 **O tier é do ARQUIVO INTEIRO.** Não se fatia reunião para rebaixar tier.
3. 🔴 **O triador roda ANTES de qualquer outro agente ler conteúdo.** ⚠ **Se o classificador lê
   primeiro, o dado sensível já vazou para o contexto dele** — e nenhuma regra posterior desfaz.
4. ⚠ **Transcrição bruta não entra no repositório.** Continua valendo.

## 5 · 🔴 Eixo D — endereçamento, e aqui está o bloqueio real

O Vinicius pediu o caso concreto: *"mudança de decisão identificada num projeto → endereçar às
pessoas corretas do projeto"*. **Medi se isso é possível hoje. Não é.**

### 5.1 · 999 de 1.000 demandas não têm dono

| Tipo | total | com dono | 🔴 sem dono |
|---|---:|---:|---:|
| **demanda** | 1.000 | **1** | **999** |
| **rfi** | 87 | **0** | **87** |
| integração | 13 | 1 | 12 |
| `contexto-area.md` | 694 | 680 | 14 |
| ficha de pessoa | 480 | 466 | 14 |
| `institucional.md` | 50 | 50 | 0 |

🔴 **A camada institucional tem dono; a camada transacional não tem nenhum.** ⚠ **E "mudança de
decisão num projeto" cai exatamente na transacional.**

### 5.2 · E onde há dono, **0% é e-mail**

Os **1.432** donos declarados são **papel em prosa** — `Responsável de atendimento + liderança de
Atendimento uMode` (1.219 ocorrências). 🔴 **Um agente não endereça aprovação para uma string
dessas.** E o projeto tem regra de ferro: **identidade é e-mail, nunca nome** — aqui não é nem
nome, é cargo.

🟢 **Mas o papel É resolvível, e o mecanismo já existe:** o fato `atendimento` do cliente resolve
para `pessoa:<e-mail>`. ⚠ **Só que resolve em 14 dos 49 clientes.** Nos outros 35 o campo traz
`?` com ausência verificada, ou `SMB` — 🔴 **que é valor de segmentação escrito no campo de
atendimento, não pessoa.**

### 5.3 · `[P]` Como o roteador compila papel → pessoa

```
papel declarado  →  regra de resolução                        →  pessoa:<e-mail>
"Responsável de atendimento"  →  fato `atendimento` do cliente
"Liderança de <Área>"         →  fato `responsavel-area` da área
"CEO"                         →  ficha fixa (João Risoléo)
"Responsável da área"         →  fato `responsavel-area`
```

🔴 **Quando não resolver, o roteador FALHA ALTO e nomeia o que falta** — nunca escolhe uma pessoa
plausível. ⚠ **É a mesma regra que já me salvou duas vezes:** `Juliana` de uma call da CAEDU
casando com `juliana@osklen.com.br`, e nome de um token só que nunca resolve. **Endereçar aprovação
para a pessoa errada é pior que não endereçar.**

## 6 · 🔴 Eixo B — "utilizável", que hoje não está escrito em lugar nenhum

O único critério existente é *"promover é ato humano"*. **Isso diz quem decide, não como.**

### 6.1 · `[P]` O teste positivo — cinco condições, todas obrigatórias

| # | Condição | Por que nasceu |
|---|---|---|
| 1 | **Tem dono por e-mail**, ou é sobre a instituição e não sobre pessoa | quatro traições por nome já registradas |
| 2 | **Sobrevive ao ruído do ASR** — quem, quando, qual assunto. 🔴 **Narrativa fina não sobrevive** | medido: 33% das falas sem pontuação final, 15% com 1–2 palavras, erro de palavra (*"um modelo de humor"*) |
| 3 | **Cabe numa chave do vocabulário fechado** (35 chaves) | chave livre quebra o cruzamento **em silêncio** |
| 4 | **Não é `T0`, `T0-P` nem `T1`** — ou, se for, entra **como existência, nunca como teor** | § 4 |
| 5 | **Contradiz ou acrescenta ao que já está escrito.** ⚠ **Repetir o que o corpus já sabe não é contexto, é ruído** | § 6.2 |

### 6.2 · 🔴 As três saídas, e `DESCARTE` precisa ser registrado

| Saída | O que é |
|---|---|
| **`CANON`** | passa nas 5 → vai para aprovação |
| **`SUPPORT`** | verdadeiro mas não muda decisão → fica no registro da call, **não sobe** |
| **`DESCARTE`** | falha numa condição → **não sobe, e o MOTIVO fica gravado** |

🔴 **`DESCARTE` sem motivo gravado é o buraco que impede o aprendizado.** ⚠ **Um sistema que só
registra o que aceitou nunca aprende a rejeitar** — e rejeitar é a maior parte do trabalho.

## 7 · 🔴 O desenho que substitui o veto que o Vinicius derrubou

**Enquanto não houver camada de acesso, `T0-P` é protegido por NÃO EXISTIR POR VALOR.**

```
call interna (1:1, desempenho, desligamento)
   ↓ triador  🔴 primeiro agente a ler, sempre
   ├─ teor T0-P  →  🔴 NÃO É ESCRITO EM LUGAR NENHUM
   └─ produz só:   "existe juízo sobre pessoa · call X · minuto Y · dono da decisão: <e-mail>"
                    ↑ isto entra. O teor não.
```

⚠ **Consequência assumida e declarada:** quem quiser o teor **volta à gravação, com autorização**.
🟢 **É perda de conveniência comprada com contenção de risco** — e é a única proteção disponível
num repositório sem camada de acesso.

🔴 **O `_inbox-calls/` NÃO é mais protegido que o resto do repo.** ⚠ **Ele é fila de trabalho, não
cofre.** Tratá-lo como cofre é o erro que faria `T0-P` entrar por uma porta que parece segura.

## 8 · 🔴 O laço de aprendizado — e a parte 🟢 que já está pronta sem ninguém ter notado

O Vinicius pediu que **toda aprovação, reprovação e alteração vire conhecimento dos agentes**.

🟢 **O sinal de supervisão já existe no banco:** `approval_audit_events` grava
`fromStatus → toStatus` com **`reason` OBRIGATÓRIO** `[C]`. **Cada decisão humana já carrega o
motivo escrito. Isso é o rótulo.** ⚠ **O corpus de treino é subproduto do processo de aprovação,
não trabalho extra** — desde que o `reason` seja levado a sério.

### 8.1 · `[P]` O que vira exemplo

```
{ entrada: <trecho + metadados>, proposta_do_agente: {A,B,C,D},
  decisao_humana: APPROVED|REJECTED|ALTERED,
  valor_final: <se ALTERED, o que o humano escreveu>,
  reason: <obrigatório>, quem: pessoa:<e-mail>, quando: <data> }
```

🟢 **`ALTERED` é o exemplo mais valioso dos três** — ⚠ **é o único que mostra a distância entre o
que o agente propôs e o que estava certo.** `APPROVED` só confirma; `REJECTED` só nega.

### 8.2 · 🔴 Os três modos de falha do laço, e a defesa de cada um

| Falha | Defesa `[P]` |
|---|---|
| 🔴 **Carimbo.** Se aprovar vira reflexo, o agente aprende a produzir o que passa batido — e a qualidade **sobe no papel enquanto cai de verdade** | exemplo só entra no corpus com **`reason` substantivo**; aprovação em rajada com motivo repetido fica **fora do treino** e vira alerta |
| 🔴 **Realimentação.** O agente treina no que ele mesmo propôs e o humano carimbou → **convergência para o próprio viés** | 🔴 **só `REJECTED` e `ALTERED` têm peso de correção.** `APPROVED` entra como confirmação fraca |
| 🔴 **Vazamento de treino.** Exemplo `T0-P` no corpus de RAG **reintroduz o teor** pela porta do aprendizado | 🔴 **`T0-P` e `T1` NUNCA entram no corpus de treino por valor.** Treina-se a DECISÃO (*"isto é T0-P"*), nunca o conteúdo |

🔴 **A terceira é a mais traiçoeira**: todo o cuidado do § 7 se perde se o material sensível voltar
como exemplo de treino. ⚠ **RAG sobre decisões, nunca sobre teor.**

### 8.3 · ⚠ O problema de partida, dito sem disfarce

**Hoje há ZERO aprovações e ZERO reprovações registradas.** `[C]` **O laço nasce sem nenhum
exemplo.** 🔴 **Um agente treinado em zero exemplo não é um agente calibrado, é um palpite com
procedência.**

🟢 **Proposta:** as primeiras **N ≈ 50** decisões são **calibração explícita** — decididas por
humano, com motivo escrito, **e marcadas como semente**. ⚠ **Só depois o agente propõe.**
**As calls da Laura são exatamente esse lote de calibração.**

## 9 · A cadeia de agentes

| # | Agente | Estado | Entrega |
|---|---|---|---|
| 0 | **Coletor** *(Workspace, time de fora)* | 🟢 contrato escrito | bruto + **e-mail** dos participantes |
| 1 | 🔴 **Triador de sensibilidade** | **não existe** | eixo **C** · 🔴 **lê primeiro, sempre** |
| 2 | **Classificador** | 🟢 prompt pronto | eixo **A** |
| 3 | 🔴 **Juiz de relevância** | **não existe** | eixo **B** · § 6 |
| 4 | 🔴 **Roteador** | **não existe** | eixo **D** · § 5 |
| 5 | 🔴 **Aprovador** | ⚠ **máquina existe no banco, inerte por `D85`** | cria, endereça, espera |
| 6 | **Aplicador** | 🟢 disciplina existe (`gera-fatos.py`) | só `APPROVED` toca canônico |
| 7 | 🔴 **Curador do aprendizado** | **não existe** | § 8 |

⚠ **Agentes 1 e 3 podem ser um só** — mas **1 tem de rodar antes de 2**, e isso é ordem, não
sugestão.

## 10 · 🔴 O plano, em ordem de dependência

**Fase 0 — destravar o endereçamento. Sem isto, os agentes 4 e 5 não têm para onde mandar.**
1. Resolver `atendimento` nos **35 clientes** abertos — § 5.2.
2. **Dar regra de dono a demanda e RFI.** `[P]` derivar de cliente + área, **nunca deixar vazio**.
3. Compilar os **1.432 papéis em prosa** para `pessoa:<e-mail>` — § 5.3.

**Fase 1 — critério, com as calls da Laura como banco de prova.**
4. Ler o material e **derivar os critérios reais de `T0-P` e de relevância** — 🔴 **entra critério,
   nunca teor** (§ 1).
5. Fechar o § 4.1 e o § 6.1 com o que o material real mostrar.
6. Produzir as **~50 decisões de calibração** com motivo escrito — § 8.3.

**Fase 2 — construir, na ordem obrigatória.** Triador → juiz → roteador.

**Fase 3 — aprovação.** ⚠ **Depende de decisão de terceiro:** `D85` trava tudo em `T2`.

**Fase 4 — o laço.** Curador + as três defesas do § 8.2.

## 11 · 🔴 O que só o Vinicius decide

| # | Decisão | Bloqueia |
|---|---|---|
| 1 | **Base legal e retenção** de dado pessoal, agora com call interna | tudo que é pessoa |
| 2 | **`T0-P` pode ser armazenado por valor?** Minha proposta é **não** | § 4.1, § 7 |
| 3 | **Quem aprova contexto de pessoa** — líder? RH? a própria pessoa? | § 5 |
| 4 | **Destravar `D85`** com o João e o Bergson | Fase 3 |
| 5 | **Separar `sensitivity` de `approvalTier`** no banco | § 3.1 |
| 6 | **Dono de demanda e de RFI** — regra, não caso a caso | Fase 0 |

## Governança

### Quem pode alterar este documento
Vinicius + liderança de Dados e IA. ⚠ **Mexe em contrato com o time do coletor e com o banco** —
não se muda sem avisar os dois lados.

### Quando ler
🔴 **Antes de escrever qualquer agente da cadeia**, e antes de promover qualquer coisa do
`_inbox-calls/`.

### Conexões
- [`protocolo-entrada-de-call.md`](../_protocolos/protocolo-entrada-de-call.md) — ⚠ **`SUPERSEDED`
  no § 5 (tier):** esta espec passa a ser a autoridade sobre sensibilidade. **O protocolo segue
  dono do formato de chegada.**
- [`protocolo-fato-atomico.md`](../_protocolos/protocolo-fato-atomico.md) — vocabulário fechado.
- [`_dicionario-dados-brainhub.md`](_dicionario-dados-brainhub.md) — `ApprovalTier`, `ApprovalBand`.
