# Prompt de execução — BrainWave · Tarefa 04: seletor de cliente ativo fixo na aba Clientes

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. Depende da Tarefa 03 (abas "uMode" e "Clientes") já estar pronta.

---

Esta tarefa **altera** o comportamento da aba **Clientes** construída na Tarefa 03. Não mexe na
aba **uMode** — lá o fluxo continua como está.

## O problema que estamos corrigindo

Hoje, dentro da aba Clientes, a única forma de trocar de cliente é voltar pra sub-aba
"Instituições" e clicar em outro cartão. E nas sub-abas "Áreas" e "Pessoas" não existe nenhuma
indicação visível de qual cliente está sendo mostrado ali. Isso deixa a navegação confusa —
parece que Áreas e Pessoas estão soltas, sem relação com um cliente específico.

## O que muda

### 1. Seletor de cliente fixo, visível em toda a aba Clientes
Adicione um seletor de cliente (ex.: um rótulo com dropdown, tipo "Cliente: [nome] ▾") fixo no
topo da aba Clientes — **visível nas 4 sub-abas** (Instituições, Áreas, Subáreas, Pessoas), não
só na Instituições. Esse seletor:
- Mostra sempre qual é o cliente ativo no momento.
- Permite trocar de cliente diretamente por ali, em qualquer sub-aba, sem precisar voltar pra
  Instituições.
- Continua sincronizado com os cartões da sub-aba Instituições: clicar num cartão de cliente lá
  também atualiza o cliente ativo mostrado no seletor.

### 2. Estado vazio quando nenhum cliente está ativo ainda
Ao entrar na aba Clientes pela primeira vez (nenhum cliente escolhido ainda), as sub-abas Áreas
e Pessoas não devem listar nada misturado de todos os clientes. Mostre um estado vazio claro,
do tipo "Selecione um cliente para ver as áreas" / "Selecione um cliente para ver as pessoas",
com o seletor de cliente já visível ali mesmo pra resolver isso sem sair da tela.

### 3. Filtro opcional de Área dentro da sub-aba Pessoas
Na sub-aba Pessoas (com um cliente ativo selecionado), adicione um filtro **opcional** por
Área — um segundo seletor, separado do de cliente, que por padrão vem "todas as áreas" (mostra
todo mundo do cliente ativo). Selecionar uma área específica restringe a lista de pessoas só às
daquela área, dentro do cliente ativo. Não torne esse filtro obrigatório.

## O que NÃO muda

- A aba **uMode** continua sem esse seletor — lá só existe 1 instituição (a própria uMode), não
  faz sentido pedir pra escolher. Navegar direto pra Áreas ou Pessoas dentro de uMode continua
  igual.
- Nenhuma tela nova de detalhe, formulário de criação/edição, ou dado real — continua tudo
  cadastro/visualização, igual às tarefas anteriores.
- Não mude a estrutura de conteúdo dentro de cada cadastro (Instituição, Área, Pessoa) — só o
  mecanismo de navegação/filtro entre elas.

## Regras para esta entrega

- Reaproveite os componentes que você já tem (cartão, dropdown, estado vazio) — não crie um
  padrão visual novo pra isso.
- Não use nenhum nome real de cliente, área ou pessoa — continue com "[exemplo]" onde precisar.
- O seletor de cliente e o filtro de área precisam funcionar em conjunto com o que já existe:
  não recrie do zero as listas de cartões de Áreas/Pessoas, só adicione a camada de filtro por
  cima delas.

**Ao terminar, me diga:**
1. O que foi construído/alterado.
2. Qualquer decisão que você tomou sozinho onde eu não te dei detalhe (ex.: posição exata do
   seletor, comportamento ao trocar de cliente com filtro de área já aplicado).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para dado real, tela de detalhe de pessoa, ou formulário de criação/edição até eu
confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
