# Prompt de execução — BrainWave · Tarefa 08: aba "Agentes" — reserva do agente de Dúvidas

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. Depende da Tarefa 01 (esqueleto de navegação) já estar pronta.

---

Esta tarefa preenche a aba "Agentes" (hoje só esqueleto) com uma grade de cartões de agente —
mesmo padrão visual já usado na aba Soluções — e reserva, dentro dela, o espaço de um agente de
consulta/dúvidas. **Não conecte nenhuma IA de verdade nesta etapa** — é só a estrutura da
interface, reservando o lugar.

## Por que isso existe agora

A ideia é ter, dentro do ecossistema, um canal onde qualquer colaborador pode perguntar coisas
em linguagem natural — dúvida de cadastro, "quantas demandas estão abertas pra tal cliente",
esse tipo de consulta. Ainda não vamos testar isso de verdade (não há IA conectada, não há dado
real pra consultar ainda) — o pedido desta etapa é só **reservar o lugar** dele na interface,
pra não precisar redesenhar a navegação quando ele for ligado de verdade.

## Estrutura da aba Agentes

Grade de cartões (mesmo padrão da aba Soluções: cartão com nome + descrição curta). Use pelo
menos 3-4 agentes de exemplo, todos claramente marcados como "[exemplo]", cobrindo tipos
diferentes de agente (ex.: um agente que faz "conferência" de área, um que audita padronização
de documento, etc. — invente livremente, são só placeholders).

**Um dos cartões é obrigatoriamente o agente de Dúvidas:**
- Nome: "[exemplo] Dúvidas" (ou nome parecido que você achar melhor — está livre pra nomear)
- Descrição curta: algo como "Pergunte sobre cadastro, dados e levantamentos"
- Ícone de chat/conversa, pra diferenciar visualmente dos outros cartões (que são mais
  "processo automático" do que "conversa")

## Ao clicar no cartão de Dúvidas

Abre uma tela de **chat** — mesmo padrão de qualquer chat simples: histórico de mensagens
(pode começar vazio, ou com 1 mensagem de boas-vindas tipo "[exemplo] Olá! Ainda estou sendo
configurado — em breve você poderá me perguntar sobre dados da plataforma."), campo de texto
pra digitar, botão de enviar. **A mensagem digitada não precisa gerar resposta real nenhuma** —
pode só aparecer na tela como enviada, sem nenhuma IA respondendo. Deixe visualmente claro que é
um espaço reservado (ex.: um aviso discreto tipo "em construção" perto do campo de digitar).

Os outros cartões de agente, quando clicados, podem abrir uma tela mais simples (ex.: descrição
+ estado "em breve"), já que o foco desta tarefa é o agente de Dúvidas.

## Regras para esta entrega

- Não conecte nenhuma IA/LLM de verdade — nem um endpoint fake que simula resposta. É só
  interface.
- Não use nome real de pessoa/cliente/produto.
- Reaproveite os componentes que você já tem (cartão, grade, campo de texto, botão).
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi construído.
2. Qualquer decisão que você tomou sozinho (ex.: nomes dos outros agentes de exemplo, layout do
   chat).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para IA conectada, dado real, ou criação de agente até eu confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
