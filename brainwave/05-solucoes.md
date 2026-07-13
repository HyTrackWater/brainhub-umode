# Prompt de execução — BrainWave · Tarefa 05: aba "Soluções" (Portfólio)

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. Depende da Tarefa 01 (esqueleto de navegação) já estar pronta.

---

Esta tarefa **renomeia e preenche** a aba "Produtos" criada na Tarefa 01: o nome correto no
menu principal passa a ser **"Soluções"**. Nenhuma outra aba muda.

## Estrutura da tela

**Sem sub-abas.** Uma grade única de cartões — um por solução do Portfólio (hoje 16) — com
filtros combináveis no topo, em chip/toggle:

- **Destino:** Voltadas ao cliente (9) · Internas (7)
- **Geração:** Legado · Nativa (a solução nasceu com o nome atual, sem nome anterior)
- **Maturidade:** Escalável · MVP · Ideação

Nenhum filtro ativo por padrão — mostra as 16. Os filtros se combinam entre si (ex.: "Voltadas
ao cliente" + "MVP" ao mesmo tempo).

## Cartão (na grade)

- Nome atual da solução, em destaque
- Nome legado, como legenda secundária, **só quando existir** (ex.: "DesenvolvAI · antes
  uFlow"). Quando não existir, não mostre a legenda — não é erro, é uma solução nativa.

## Cadastro (ao clicar num cartão)

- Descrição
- Nome legado (se houver)
- Área canônica conectada (só nas voltadas ao cliente)
- Score de maturidade — `[a preencher]` em todos por ora (Escalável/MVP/Ideação ainda não foi
  atribuído a nenhuma solução real)
- **Clientes que contrataram** — por ora, mostre um estado vazio/pendente (ex.: "cruzamento
  ainda não confiável — pendente de varredura"), **não invente nomes de cliente aqui**. O
  motivo: o dado real de "módulos contratados" que os clientes têm hoje usa nomes antigos
  (legado) e ainda não foi conferido nome a nome contra o Portfólio atual — mostrar um exemplo
  aqui pareceria dado real e não é.
- Botão pra voltar à grade

**Importante sobre o clique num cliente dentro de "Clientes que contrataram":** quando essa
lista existir de verdade (próxima etapa, fora desta tarefa), cada cliente vai abrir o registro
da *relação* daquela solução com aquele cliente especificamente (data de início, condução,
particularidades de integração) — não a ficha genérica do cliente. Essa tela de relação ainda
não existe. Por enquanto, deixe esse comportamento **reservado/placeholder** — não construa a
tela de detalhe da relação nesta tarefa.

## Dado de exemplo pra preencher visualmente a grade (marcar como exemplo)

Use nomes de solução genéricos como "[exemplo] SoluçãoA" (voltada ao cliente, nativa) até
"[exemplo] SoluçãoG" (interna, legado, com legenda "antes [exemplo] NomeAntigoG") — não use
nenhum dos nomes reais do Portfólio (não são segredo, mas mantenha o padrão desta sessão: só
"[exemplo]" nas telas). Distribua os exemplos pra cobrir pelo menos uma combinação de cada
filtro (interna, cliente, legado, nativa, escalável, mvp, ideação, e algumas com maturidade
vazia).

## Regras para esta entrega

- Ainda não construa formulário de criação ou edição de Solução.
- A tela precisa lidar bem com campo vazio ("[a preencher]", legenda de nome legado ausente,
  lista de clientes vazia) sem quebrar layout — mesma disciplina das tarefas anteriores.
- Reaproveite os componentes que você já tem (cartão, grade, filtro/chip, estado vazio).
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi construído/alterado.
2. Qualquer decisão que você tomou sozinho onde eu não te dei detalhe (ex.: posição dos filtros,
   layout do cartão, ícone da aba).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para dado real, cruzamento com cliente, ou formulário de criação/edição até eu
confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
