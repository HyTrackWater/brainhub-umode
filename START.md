# START.md — Ponto de entrada único

> Se esta é a primeira mensagem da sessão, siga as instruções abaixo antes de qualquer outra
> coisa. Não pule etapas, não resuma por cima — leia cada arquivo por inteiro.

## Contrato desta primeira resposta

1. **Leia, nesta ordem, os arquivos inteiros abaixo — nenhum resumo, nenhum trecho:**
   1. **`AGORA.md`** — onde o projeto está hoje: papel, o que, como, passos dados, frente ativa,
      próximos passos e decisões esperando o Vinicius. **É a orientação. Comece por ele.**
   2. `CLAUDE.md` — seu papel, as regras que não podem ser quebradas, como executar tarefas
   3. `CONTEXT.md` — o que o projeto é, a arquitetura e as decisões já travadas
   4. `STATE.md` — o histórico completo. **São ~2.700 linhas e ele é cronológico, não
      hierárquico.** Leia por inteiro se a sessão for longa; se for pontual, leia a **primeira
      seção `## 🔵 FRENTE ATIVA`** (a mais recente fica no topo, logo após `## Sprint atual`) e
      o **fim do `## Log de sessões`**.
   5. `brainwave/CONTEXTO.md` — só se a sessão for sobre construir a interface visual da
      plataforma; leia mesmo assim, é contexto útil mesmo que a tarefa do dia seja outra. Se
      for continuar trabalho de frontend, confira também o arquivo de tarefa mais recente em
      `brainwave/` (maior número) pra ver o que já foi enviado e qual o resultado registrado.

   > ⚠ **Duas seções da `STATE.md` são histórico e NÃO devem ser lidas como estado atual:**
   > `## Sprint atual` (congelada na Sprint 02, de ago 2026) e
   > `## Próximas atividades (fila da Sprint 02 — referência histórica)`.
   > **O estado atual está no `AGORA.md`.**

2. **Não altere nenhum arquivo nesta primeira resposta.** Não crie, não edite, não commite
   nada. Esta etapa é só leitura e confirmação de entendimento.

3. **Responda ao usuário cobrindo exatamente estes seis pontos, nesta ordem:**
   - **O que é este projeto** — em poucas frases, o que é o BrainHub e o que ele documenta.
   - **Qual é o seu papel aqui** — o que se espera de você a partir de agora.
   - **Como se trabalha aqui** — as regras de método que não se quebram (`AGORA.md` § 1 e § 3).
   - **Onde o projeto está** — cobertura em número (`AGORA.md` § 5) e a frente ativa (§ 6).
   - **Qual é o próximo passo** — o primeiro item de `AGORA.md` § 7.
   - **O que está esperando decisão do Vinicius** — `AGORA.md` § 8, só a contagem e os títulos.

4. **Não prossiga para nenhuma tarefa nova até o usuário confirmar que o entendimento acima
   está correto.** Se algo parecer desatualizado ou incompleto, **diga isso explicitamente** em
   vez de seguir em frente — inclusive se a data no topo do `AGORA.md` estiver velha.

## Ao fechar a sessão (obrigatório)

**Toda sessão que gera commit atualiza dois arquivos, sem exceção:**

1. **`STATE.md`** — o que aconteceu, no histórico. Nunca reescrever sessão anterior.
2. **`AGORA.md`** — data, commit, os números da § 5, e as listas das § 6, § 7 e § 8.

> **Se só a `STATE.md` for atualizada, o `AGORA.md` passa a mentir** — e ele é o primeiro
> arquivo que todo mundo lê.

## Como usar (instrução para o usuário que usará a interface para acionar a LLM)

Cole só isto como primeira mensagem da sessão:

> Leia START.md
