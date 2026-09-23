---
aliases:
  - "Protocolo — o que fazer com aquilo que só o Vinicius responde"
tags:
  - tipo/protocolo
  - casa
---
# Protocolo — o que fazer com aquilo que só o Vinicius responde

> **Classe: `PROTOCOLO`.** É **o único caminho** para levantar, acumular e resolver o que
> nenhuma fonte responde. 🔴 **Não criar um segundo.**
>
> **Decisão do Vinicius em 22 set 2026, textual:** *"em dado momento, você montará uma lista de
> coisas que eu tenho que perguntar e vou dar um jeito de responder ou por áudio ou numa
> transcrição de reunião mesmo. Mas pensaremos nisso quando chegar o momento."* E, sobre o risco
> de isto se perder: *"Garanta que essa decisão esteja registrada nas documentações de forma que
> você nunca se esqueça de que existe esse caminho. Não adianta aplicar agora e depois criar
> outras formas de fazer a mesma coisa ou até passar sem executar esse comando padronizado."*

## 1 · A regra que decide se algo é pergunta

🔴 **Uma pergunta só existe quando NENHUMA fonte pode respondê-la.**

| O caso | O que é | Para onde vai |
|---|---|---|
| Dúvida que uma fonte responde, e eu não li a fonte | **varredura que falta fazer** | `_pendencias-e-fontes.md` **§ 4** |
| Dúvida que nenhuma fonte responde — decisão, intenção, histórico que só ele tem | **pergunta** | `_pendencias-e-fontes.md` **§ 2.1** |
| Discrepância entre duas fontes, sem terceira que desempate | **pergunta** | **§ 2.1** |
| Achado que exige ação dele (rotação de chave, autorização) | **pergunta**, tier `T0`/`T1` | **§ 2.1** |

> **Transformar em pergunta o que está a uma leitura de distância é empurrar para ele trabalho
> meu.** É o erro que o `CLAUDE.md` já nomeia: *"nomear o arquivo e não abri-lo é transformar em
> pendência de terceiro o que estava a uma leitura de distância."*

## 2 · Onde a pergunta nasce, e onde ela nunca deve nascer

**Nasce em um lugar só:** `PERGUNTAS` (ou `PERGUNTAS_GERAIS`, quando é transversal) dentro de
`scripts/gera-pendencias-e-fontes.py`.

**Daí ela aparece, sozinha, em dois lugares:**

1. `_Clientes/<Cliente>/00_Institucional/_contexto/_pendencias-e-fontes.md` **§ 2.1** — no contexto
   do cliente, junto das evidências que a geraram;
2. [`_perguntas-para-o-vinicius.md`](../_contexto/_perguntas-para-o-vinicius.md) — **a lista
   consolidada que ele responde.**

🔴 **Os dois são gerados pelo MESMO script.** Não existe um segundo jeito de montar a lista, e
não existe rodar um sem o outro. **Era exatamente o risco que ele apontou.**

🔴 **O que NÃO fazer, nunca:** escrever pergunta solta numa resposta de chat, numa `## Pergunta`
ad-hoc dentro de um registro, ou numa tabela nova em qualquer documento. **Pergunta fora da § 2.1
some na próxima compactação da conversa.** Foi assim que se perdeu contexto antes.

## 3 · O ciclo

```
varredura acha a dúvida
   → é respondível por fonte?  → SIM: vai para a § 4, e eu vou ler
                               → NÃO: vira linha em PERGUNTAS
   → python scripts/gera-pendencias-e-fontes.py
   → aparece na § 2.1 do cliente E na lista consolidada
   → recebe um DESTINATÁRIO nomeado (§ 4.1)
   → quem recebe decide: APROVA · RECUSA · ALTERA · RESPONDE
   → a decisão entra como evidência datada, com justificativa e fonte
   → a pergunta MUDA DE ESTADO — nunca é apagada
```

### 3.1 · 🔴 O destinatário não é sempre o Vinicius

**Travado por ele em 23 set 2026:** *"provavelmente não serei eu que responderei, mas temos um
local organizado para depois distribuir as perguntas."*

Por isso a pergunta carrega **quem responde**, e o padrão é **`⚠ a distribuir`** — não
`Vinicius`. Assumir que as 43 abertas são dele seria afirmar um dado que ninguém decidiu.
**A distribuição é decisão, e decisão não é minha.**

**Quando a lista vai até ele:** ⚠ **não é decisão minha sozinho.** Ele disse *"pensaremos nisso
quando chegar o momento"*. **Minha obrigação é manter a fila pronta e avisar quando ela crescer
a ponto de travar a varredura** — não escolher a hora.

## 4 · O formato de uma pergunta

`(pergunta, tier, por que importa, estado[, quem responde])`

O 5º campo é **opcional**: sem ele, o destinatário sai como `⚠ a distribuir`.

- **pergunta** — redigida para ele responder **falando**, não escrevendo. Pergunta boa cabe numa
  frase de áudio. **Cita a evidência que a gerou**, para ele não ter que lembrar do contexto.
- **tier** — `T0` · `T1` · `T2`, o mesmo vocabulário do resto do corpus.
- **por que importa** — o que destrava. Sem isso ele não consegue priorizar.
- **estado** — vocabulário **fechado**, cinco valores. **Toda saída de `aberta` carrega
  justificativa** — é a justificativa que vira contexto, não o rótulo.
- **quem responde** — o destinatário. Pode ser pessoa, área ou time.

### 4.1 · 🔴 Os cinco estados, e por que `recusada` não é fracasso

| Estado | Quando se usa | O que a justificativa precisa dizer |
|---|---|---|
| 🔴 `aberta` | ninguém decidiu ainda | — |
| 🟢 `aprovada em <data> por <quem> — <justificativa>` | a resposta foi dada e **vira contexto que já vale** | o que passa a valer |
| ⚪ `recusada em <data> por <quem> — <justificativa>` | **decidiu-se que a pergunta não precisa de resposta** | **por que não precisa** — é isso que entra no corpus |
| 🟡 `alterada em <data> por <quem> — <justificativa>` | a pergunta estava mal formulada ou mudou de escopo | **como mudou e por quê** |
| 🔵 `respondida em <data> por <fonte> — <resposta>` | respondida por fonte ou por pessoa | a resposta, com procedência |

🔴 **`recusada` é resposta, não desistência.** *"Isso não precisa ser respondido porque X"* é
conhecimento tão útil quanto a resposta — e impede que a mesma dúvida volte na varredura
seguinte. **Por isso a justificativa é obrigatória nos quatro estados de saída.**

🔴 **Resposta não apaga a pergunta.** O histórico do que já se perguntou vale tanto quanto a
resposta — é ele que impede perguntar duas vezes a mesma coisa.

**Exemplo real, já respondido:** *"`Status` ou `Etapa` — qual manda?"* → *"a verdade é que não
sei. Nós vamos ter que ver caso a caso"* (22 set 2026, por mensagem). **A resposta não fechou o
tema: converteu uma pergunta transversal em uma pergunta por cliente.**

## 5 · Como saber que este protocolo está sendo cumprido

| Verificação | Como |
|---|---|
| Toda pergunta está na § 2.1? | `grep -rn "pergunt" uMode/00_Institucional/_contexto/_varredura-*.md` — **registro não é lugar de pergunta** |
| A lista consolidada está em dia? | rodar `python scripts/gera-pendencias-e-fontes.py`; se ele mudar algo, a fila estava desatualizada |
| A fila cresceu a ponto de travar? | § 0 do `_perguntas-para-o-vinicius.md` |

## 6 · O que este protocolo NÃO resolve

- ⚠ **Não decide quando levar a lista ao Vinicius.** É dele.
- 🔴 **Não distribui as perguntas sozinho.** As 43 abertas estão com `⚠ a distribuir`. **Atribuir
  destinatário é decisão**, e sai da mesma fonte de qualquer outra: o Vinicius ou quem ele indicar.
- ⚠ **Não substitui varredura.** Fila comprida com páginas de cliente fechadas é sinal de
  varredura atrasada, não de dúvida legítima — **pergunta boa nasce de varredura feita.**
- ⚠ **Não cobre a resposta em áudio/transcrição**: quando ela chegar, entra pelo
  `protocolo-varredura-cliente.md` como qualquer fonte, com procedência e data.

## Governança

### Quem pode alterar este documento
Vinicius. **É decisão dele, registrada a pedido dele.**

### Quando ler
🔴 **Sempre que uma varredura produzir uma dúvida.** Antes de escrever a dúvida em qualquer
outro lugar.
