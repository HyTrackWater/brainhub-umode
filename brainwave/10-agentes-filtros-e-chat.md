# Prompt de execução — BrainWave · Tarefa 10: correção — filtros de categoria e chat fixo na aba Agentes

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. **Corrige** o que ficou faltando nas Tarefas 08/09 na aba "Agentes".

---

O resultado atual da aba "Agentes" tem dois problemas que precisam ser corrigidos:

## Problema 1 — os agentes estão todos soltos na tela, sem organização

Hoje todos os cartões de agente aparecem misturados, sem separação visual nem filtro. Isso
precisa virar filtro **funcional** de verdade, não só descrição no prompt anterior:

- Adicione filtros em chip, no topo da aba Agentes, um por categoria: **Geral** (o agente
  Dúvidas), **Por Área**, **Por Cliente**, **Por Solução**, **Personalizado**.
- Clicar num chip filtra a grade pra mostrar só os cartões daquela categoria. Sem filtro
  nenhum selecionado, mostra todos.
- Cada cartão continua mostrando de qual categoria ele é (badge/etiqueta), mesmo com o filtro
  aplicado — não tire essa informação do cartão.
- Isso é o mesmo padrão de filtro em chip que você já usou nas abas Soluções e Demandas — não
  invente um componente novo, reaproveite.

## Problema 2 — sumiu a parte de interagir com o agente (chat), precisa voltar

Uma versão anterior desta tela já tinha construído a interface de conversa com o agente
(histórico de mensagens + campo de texto pra digitar) — isso precisa **voltar a aparecer**,
mesmo sem nenhuma IA de verdade respondendo. O objetivo é dar visibilidade de como a interação
vai funcionar no futuro, mesmo que hoje não funcione de verdade.

- Ao abrir qualquer agente (Dúvidas ou qualquer um das 4 categorias), a tela precisa mostrar a
  interface de chat: histórico de mensagens (pode ter uma mensagem inicial de boas-vindas,
  "[exemplo]"), campo de texto, botão de enviar.
- Pros agentes das 4 categorias (Por Área/Cliente/Solução/Personalizado), mantenha também as
  perguntas sugeridas (estilo FAQ) já pedidas na Tarefa 09, acima do campo de texto.
- Deixe visualmente claro que é um espaço reservado — sem fingir que há resposta de IA real
  (ex.: aviso discreto "em construção" perto do campo de digitar, igual já foi pedido antes).
- Isso vale pra todos os agentes, não só o Dúvidas — nenhum deles pode abrir uma tela vazia ou
  só com descrição, todos precisam mostrar essa interface de chat reservada.

## Regras para esta entrega

- Nenhuma IA/LLM de verdade conectada — continua sendo só interface.
- Não use nome real de pessoa/cliente/produto.
- Reaproveite os componentes que você já tem (chip de filtro, chat, cartão).
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi corrigido (filtro funcional + chat de volta em todos os agentes).
2. Qualquer decisão que você tomou sozinho.
3. Qualquer dúvida antes de eu pedir a próxima etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
