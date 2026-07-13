# START.md — Ponto de entrada único

> Se esta é a primeira mensagem da sessão, siga as instruções abaixo antes de qualquer outra
> coisa. Não pule etapas, não resuma por cima — leia cada arquivo por inteiro.

## Contrato desta primeira resposta

1. **Leia, nesta ordem, os arquivos inteiros abaixo — nenhum resumo, nenhum trecho:**
   1. `CLAUDE.md` — seu papel, as regras que não podem ser quebradas, como executar tarefas
   2. `CONTEXT.md` — o que o projeto é, a arquitetura e as decisões já travadas
   3. `STATE.md` — o estado atual: o que já foi feito e o que vem a seguir
   4. `brainwave/CONTEXTO.md` — só se a sessão for sobre construir a interface visual da
      plataforma; leia mesmo assim, é contexto útil mesmo que a tarefa do dia seja outra. Se
      for continuar trabalho de frontend, confira também o arquivo de tarefa mais recente em
      `brainwave/` (maior número) pra ver o que já foi enviado e qual o resultado registrado.

2. **Não altere nenhum arquivo nesta primeira resposta.** Não crie, não edite, não commite
   nada. Esta etapa é só leitura e confirmação de entendimento.

3. **Responda ao usuário cobrindo exatamente estes quatro pontos, nesta ordem:**
   - **O que é este projeto** — em poucas frases, o que é o BrainHub e o que ele documenta
     (baseado em `CONTEXT.md`).
   - **Qual é o seu papel aqui** — o que se espera de você a partir de agora (baseado em
     `CLAUDE.md` e, se aplicável, `brainwave/CONTEXTO.md`).
   - **Qual foi a última atividade registrada** — a entrada mais recente do "Log de sessões"
     em `STATE.md`, resumida em 1–2 frases.
   - **Qual é o próximo passo** — o primeiro item da lista "Próximas atividades" em `STATE.md`.

4. **Não prossiga para nenhuma tarefa nova até o usuário confirmar que o entendimento acima
   está correto.** Se algo no `STATE.md` parecer desatualizado ou incompleto, diga isso
   explicitamente em vez de seguir em frente.

## Como usar (instrução para o usuário que usará a interface para acionar a LLM)

Cole só isto como primeira mensagem da sessão:

> Leia START.md
