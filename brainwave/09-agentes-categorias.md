# Prompt de execução — BrainWave · Tarefa 09: aba "Agentes" — categorias e RAG por escopo

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. **Altera e expande** a aba "Agentes" construída na Tarefa 08 — não é aba nova.

---

Esta tarefa reorganiza a aba "Agentes" em categorias, mantendo o agente "Dúvidas" (Tarefa 08)
como está, à parte das categorias — ele continua sendo o agente geral, sem escopo fixo.

## Conceito desta tarefa (leia antes de desenhar)

Cada agente "padronizado" (o que a uMode treina, diferente dos que um usuário pode criar) tem um
escopo fixo, e o que ele sabe responder vem **do mesmo conteúdo que já documentamos** — não é
uma base de conhecimento paralela. Um agente "de uma Área" lê o cadastro daquela Área; um agente
"de um Cliente" lê o cadastro daquele cliente; um agente "de uma Solução" lê o cadastro daquela
solução. Isso é só a estrutura da interface — **nenhuma IA de verdade é conectada nesta etapa**,
igual às tarefas anteriores.

## 4 categorias de agente padronizado + 1 agente geral

Reorganize os cartões de agente em categorias, com um filtro em chip no topo pra alternar entre
elas (mesmo padrão de filtro já usado nas outras abas):

1. **Por Área** — um agente por área (ex.: "[exemplo] Agente Comercial"). Descrição: "baseado no
   cadastro da área Comercial".
2. **Por Cliente** — um agente por cliente (ex.: "[exemplo] Agente Cliente A"). Descrição:
   "baseado no cadastro institucional, na jornada e nas pessoas do Cliente A". Inclua, como
   exemplo de pergunta que esse tipo de agente responderia, algo sobre jornada, pessoas/contatos
   e integração — mas ao sugerir uma pergunta sobre **oportunidade de upsell**, deixe claro que
   é uma resposta *calculada* (comparando o que o cliente já tem contratado com o portfólio
   completo), não um dado que já existe pronto em algum campo — não finja que existe um campo
   "Oportunidades de upsell" já preenchido.
3. **Por Solução** — um agente por item do portfólio (ex.: "[exemplo] Agente DesenvolvAI").
   Descrição: "baseado no cadastro da solução DesenvolvAI".
4. **Personalizado** — agentes criados por usuários, formato "skill". Nesta categoria, o
   primeiro cartão não é um agente pronto — é um cartão de ação **"Criar agente"**.

O agente **"Dúvidas"** (já construído na Tarefa 08) continua existindo, mas fica **fora das 4
categorias** — mostre ele fixo, separado, no topo da tela ou numa seção própria "Geral", já que
ele não tem escopo fixo (responde sobre qualquer coisa, diferente dos outros).

## Cartão de agente (Por Área / Por Cliente / Por Solução)

Nome + categoria (badge) + descrição curta de qual é o escopo dele. Ao clicar, abre o mesmo
formato de chat da Tarefa 08 (histórico + campo de texto, sem IA conectada), mas com uma
diferença: mostre **2-3 perguntas sugeridas (estilo FAQ)**, como botões clicáveis acima do campo
de digitar, coerentes com o escopo daquele agente (ex.: pro agente de uma Área: "Quais são os
padrões operacionais dessa área?"; pro agente de um Cliente: "Quais os marcos recentes da
jornada desse cliente?", "Quem são os contatos principais?"). Clicar numa pergunta sugerida só
preenche o campo de texto — não precisa gerar resposta real.

## Cartão "Criar agente" (dentro de Personalizado)

Ao clicar, abre um formulário simples: nome do agente, descrição/propósito, escopo (texto
livre — o que ele deveria saber responder). Ao enviar, **não crie o agente de verdade** — mostre
uma mensagem de confirmação explicando que o pedido virou uma solicitação aguardando aprovação
(ex.: "[exemplo] Seu pedido foi registrado e está aguardando aprovação antes de virar um agente
disponível."). Não precisa simular quem aprova nem um fluxo de aprovação completo — só deixar
claro que criar um agente não é imediato, passa por aprovação.

## Dado de exemplo (marcar como exemplo)

Pelo menos 2 agentes por categoria (Por Área, Por Cliente, Por Solução), mais o cartão "Criar
agente" em Personalizado, mais o agente Dúvidas já existente. Nomes sempre "[exemplo]".

## Regras para esta entrega

- Nenhuma IA/LLM de verdade conectada — nem simulação de resposta.
- Não use nome real de pessoa/cliente/produto.
- Reaproveite os componentes que você já tem (cartão, filtro/chip, chat, formulário simples).
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi construído/alterado.
2. Qualquer decisão que você tomou sozinho (ex.: onde ficam as perguntas sugeridas, como fica
   visualmente o agente Dúvidas separado das categorias).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para IA conectada, aprovação de verdade, ou dado real até eu confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
