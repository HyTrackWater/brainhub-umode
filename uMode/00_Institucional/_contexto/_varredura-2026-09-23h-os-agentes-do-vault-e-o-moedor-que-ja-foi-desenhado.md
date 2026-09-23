---
aliases:
  - "Varredura 23 set 2026 — os agentes do vault do João, e o moedor que já foi desenhado"
tags:
  - tipo/registro
  - casa
---
# Varredura 23 set 2026 — os agentes do vault do João, e o moedor que já foi desenhado

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
>
> **Fonte:** `HyTrackWater/umode-os-vault`, clone local, **somente leitura** — nenhum commit,
> checkout ou escrita. `main` em `2125e37a` (11/09/2026) e a branch
> `origin/governance/brainhub-v1.5` (14/09) lida via `git show`.
>
> **Tratamento:** `T2`. Nenhum segredo reproduzido — ver § 6.

## 0 · 🔺 Declaração de completude, e uma correção minha

🔺 **Eu errei antes desta varredura.** Em 23 set 2026 eu afirmei que
**`cx-meeting-transcriber` do CX Hub "já existe" e era "o moedor em peças"**. **O Vinicius
corrigiu: o CX Hub não tem agente treinado.** Os quatro nomes (`cx-classifier`,
`cx-demand-analyst`, `cx-summarizer`, `cx-meeting-transcriber`) são **edge functions nomeadas**,
não agentes com treino. **O que existe de verdade está no vault, e é muito mais do que eu supunha.**

**O que esta varredura NÃO cobre:** os `references/*.md` das skills MBS · os ~2.800 arquivos de
`BrainHub/` dentro do vault · 16 dos 22 `SKILL.md` foram lidos por frontmatter + grep, não
na íntegra.

⚠ **O clone local está 3 dias atrás da branch mais rica.** A `governance/brainhub-v1.5` tem
**12 skills que não existem no `main`** — e várias são as mais relevantes para nós.

## 1 · 🔴 O achado: o moedor já foi desenhado, e chegou a rodar

### 1.1 · `brainhub-seed-calls.md` — a especificação, assinada pelo João em 17/06

**É, em desenho, o "moedor de carne" que o Vinicius descreveu.** Quatro passos:

```
TRANSCRIÇÃO (pasta única no Drive)
 → 1 CLASSIFICAR TIPO     1 rota (nome do arquivo + participantes + ~400 tokens)
 → 2 EXTRAIR ENTIDADES    N alvos (clientes, temas, pessoas citadas)
 → 3 FAN-OUT + DIFF       1 cruzamento por entidade, contra o MD dela
 → 4 PROPOSTAS            fila de aprovação no Console
```

🟢 **O ponto que vale mais:** *"uma call que fala de 5 clientes gera **5 cruzamentos
independentes**, não 1 atualização"*. **É exatamente o endereçamento que eu apontei como o
ponto de falha do moedor** — e já está resolvido no desenho.

**O cruzamento (§04, "o coração"):** cada afirmação cai em **🟢 NOVO** (proposta de adição) ·
**⚪ CONFIRMA** (nada) · **🔴 CONTRADIZ** (**quarentena, humano decide**), com card mostrando
MD atual × fala da call × timestamp × origem.

🔴 **E há um pré-requisito duro que nos atinge (§05):** o MD de entidade precisa ser **fato
atômico e datado** — `- imersão: 10/07/2026 (fonte: PRD v1.6, 2026-05)` — **não prosa.**
*"MD bagunçado = cruzamento ruim."* ⚠ **Os nossos `contexto-area.md` e `institucional.md` são
prosa.** **Isso é trabalho nosso, e é pré-condição, não consequência.**

**§08 — aprovação:** as saídas previstas são **task, e-mail e atualização de MD**, todas como
proposta. **Nenhuma saída com efeito externo dispara sem aprovação humana.**

**§11 diz que dos 6 andares, só o 1º está feito** (stack decidida: Drive + N8N + Supabase + Lovable).

### 1.2 · `brainhub-mine.py` — o moedor que rodou uma vez

Agente da frota, `StartInterval 1800`. Lê `inbox/transcricoes/*` → carrega **4 treinos** →
chama o modelo → escreve `propostas/<data>-<nome>.md` com front-matter → move a transcrição para
`processadas/` → grava custo em `status/`.

🟢 **Não grava contexto oficial. Só PROPÕE** — está no código e repetido no prompt.

⚠ **Estado: `runs: 1`, última execução 11/06.** Rodou uma vez e parou.
⚠ **E ele NÃO faz o fan-out** — destila a call inteira num bloco só, sem endereçar por entidade.

### 1.3 · 🟢 Os 4 treinos — a melhor peça do vault

**Política em MD editável, fora do código, com saída contratada em JSON.**

| Treino | O que faz | Devolve |
|---|---|---|
| `filtro-sinal` | só passa o que é **durável + reutilizável + não-óbvio** ao mesmo tempo | `{passa, motivo}` |
| `classificador-cunho` | 3 eixos fechados: assunto × tipo (fato/decisão/opinião/tarefa) × dono | `{assunto, tipo, dono, confianca}` |
| `roteador-tier` | 3 donos: empresa `T2` · joão `T0/T1` · pessoa-interna `T1`. **Regra invertida: fato sobre pessoa física assume o mais restritivo e escala** | `{dono, tier, destino, escala}` |
| `juiz-contradicao` | refino · atualização · **contradição real → nunca decide, enfileira** | `{relacao, acao, ref}` |

🔴 **O `juiz-contradicao` resolve exatamente o problema de "a reunião contradiz o cérebro".**

### 1.4 · `brainhub-calls-regras-classificador.md` — roteamento com loop de aprendizado

10 rotas com sinais fortes e de apoio. **Precedência de tier ANTES da rota.**
Confiança ≥ 80% roteia; abaixo vai para fila com `perguntas[]`. **Botão "Dar Feedback" com
justificativa obrigatória deriva regra nova** — a próxima call com o mesmo padrão acerta sozinha.

## 2 · 🔴 O estado real: nada está rodando

| Fato | Evidência |
|---|---|
| **16 jobs cadastrados, 0 ativos, 16 pausados** | `2026-08-09-hermes-pausa-total-de-jobs.md`, decisão do João |
| **206 transcrições acumuladas no Drive** | pasta `Tactiq Transcription`; esteira morta há 24 dias em 02/09 |
| **598 áudios de WhatsApp nunca transcritos** | `_tools/transcrever_audios.py`, faster-whisper local |
| A leitura por LLM da esteira está **desligada** | `ler_com_modelo()` retorna `HERMES_SEED_SEM_ISOLAMENTO` |
| O substituto é **regex** | o próprio autor escreveu: *"regex não resume reunião"* |

🔴 **Existe matéria-prima parada: 206 transcrições + 598 áudios.** Não é falta de fonte — é
esteira desligada.

## 3 · As 22 skills do `main` — o que são

**Seis são "de máquina"**, com contrato idêntico (saída `status: DRAFT` + classificação + risco +
evidência + próxima ação; **não ativa agente, não promove canônico, não deleta**):
`inbox-evaluator` (classifica SEGURO/SENSÍVEL/CONTRADITÓRIO) · `structure-distributor` (diz a
casa correta de cada conteúdo) · `catalog-index-maintainer` · `orphan-radar` (órfão, link
quebrado, sem Conexões) · `md-size-auditor` · `validation-feedback`.

🟢 **`orphan-radar` e `md-size-auditor` fazem, no vault do João, o que os nossos
`valida-indexacao.py` e o threshold de 8.000 palavras fazem aqui.** Mesma preocupação, duas
implementações.

**As outras 16** são de produto e de mentoria: `mbs-*` (5, incluindo `mbs-crm-protocolo`, que
**já transforma transcrição de reunião comercial em card de CRM**), `anexo-tech-integracao`,
`umode-smart-code` (cujo método *"Da Dor ao GoLive"* tem uma etapa chamada **MÓI, "o moedor de
carne de dados"**), `umode-brainhub` (auditoria **semântica** de drift), entre outras.

### 3.1 · 🔴 As 12 skills que só existem na branch `governance/brainhub-v1.5`

| Skill | Por que importa para nós |
|---|---|
| **`brainhub-approval-bridge`** | 🟢 **posta card na fila REAL de aprovação** em `brainhub.umode.tech`. Nasceu de erro pago: 26 itens sensíveis descritos em markdown que o João nunca viu |
| **`onde-mora-cada-coisa`** | critério único de destino: CONTEXTO / ACERVO / PRIVADO / FORA |
| **`padrao-cliente`** | padrão de estrutura de cliente extraído dos clientes bem organizados |
| **`curadoria-por-conteudo`** | premissa-mãe: **nome de arquivo é hipótese, conteúdo é veredito** |
| **`discord-intake`** | canal do Discord → contexto rastreável (raw + destilado) |
| `rfi-aderencia-plm-mdm` | responde matriz de requisitos de PLM/MDM, com gate anti-vaporware |
| `repo-alheio-antes-de-escrever` | escrita depois de 8 reprovações num dia no `umode-brainhub` |

## 4 · A governança de agente — as regras que valem para todos

**Onde pode escrever (§3, "a regra mais importante"):** agente escreve **somente em
`inbox/<seu-nome>/`**, nunca em pasta canônica. **Só o João promove.** Exceção única é a
**Promoção Assistida (§3-bis, D63)**, nominal por agente — hoje só o Hermes, e **aguardando
teste de obediência**. **Nada se deleta**: obsoleto vai para `_historico/`.

**Front-matter obrigatório:** `origem`, `criado_em`, `tipo`, `entidade`, `sync`.
**Sem front-matter = intruso.**

**Heartbeat (§11, D62):** *"NADA roda sem batimento."* Três provas: log com `mtime` fresco ou PID
vivo · linha no registro · rodada mostrando `OK`. **Ligar sem registrar é violação no mesmo nível
de escrever fora do inbox.** Origem: dois jobs morreram e ninguém soube por **5 semanas**.

**Evidência (§11-bis, D66):** *"exit 0 não é prova de trabalho."* Um job falhava em **10 de 10
repos todo dia** e o heartbeat dizia `OK` — `continue` no erro mais um `echo` final davam exit 0
com log fresco. Todo job declara o que o próprio log **exige** e **proíbe**. E exige **teste
negativo**: apontar a regra para um log sabidamente ruim e confirmar que reprova.
🟢 **Isto é a mesma disciplina do nosso `valida-numeros.py`** — guarda que acusa, não que afirma.

**Guarda determinística (§8, D30):** todo lote automático passa por **script, não por LLM**,
antes de contar como entregue.

**§13 (D66):** nenhum agente constrói pipeline novo sem ler o catálogo de sistemas e **declarar
o que checou e por que o existente não resolve**. *"Um agente já propôs reconstruir do zero a
fila de aprovações que já estava no ar."*

## 5 · 🔴 O que NÃO existe — e é o nosso espaço

| Lacuna | Consequência |
|---|---|
| 🔴 **Nada cria Demanda, RFI ou Atividade a partir de reunião** | as saídas previstas param em **task, e-mail e MD**. **O pedido do Vinicius vai além do que foi desenhado** |
| 🔴 **O fan-out por entidade nunca foi construído** | está na espec, não no código |
| 🔴 **O diff contra MD não funciona com os nossos MDs** | eles são prosa; o §05 exige **fato atômico datado** |
| 🔴 **Não há roteamento para PESSOA** | as rotas vão a categoria; **taxonomia de pessoa e de área de cliente não entram** |
| 🔴 **Nenhuma peça conhece a nossa hierarquia** | endereçamento no vault é por pasta de entidade, **não** por `Instituição → Áreas → Subáreas → Pessoas` |
| 🔴 **Nenhum agente de segurança existe como AGENTE** | existe como script e como regra escrita |

🟢 **E é aqui que o nosso corpus tem o que o vault não tem: 479 fichas de pessoa com e-mail,
48 clientes com status, 680 áreas e a hierarquia travada.** **O vault tem o motor; nós temos o
endereço.**

## 6 · 🚨 Higiene de segredo observada (valores não reproduzidos)

Duas ocorrências no vault, **registradas por referência**: o `DECISOES.md` da raiz cita **uma
senha em texto claro** de um repositório de proposta, e a skill `discord-intake` (na branch)
**aponta o caminho de um token de bot**. 🔴 **Nenhum valor foi lido nem copiado.**
⚠ **É item de higiene do vault do João, não nosso** — mas soma-se aos 5 focos já conhecidos aqui.

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO` — foto com data. Correção vira registro novo.
