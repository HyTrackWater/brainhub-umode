# Prompt de execução — BrainWave · Tarefa 07: Demandas em tabela + Conversas + Reatribuir

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. **Altera** a aba "Demandas" construída na Tarefa 06 — não é aba nova.

---

Esta tarefa altera a aba "Demandas" em dois pontos: a lista principal vira uma tabela mais
compacta, e o detalhe de cada demanda ganha duas funcionalidades que faltavam.

## 1. Lista principal: de lista de cartões para tabela compacta

Troque a lista atual por uma **tabela**, uma linha por demanda, colunas:

- Título
- Natureza
- Origem → Destino (organizacional)
- Status (interno) — como badge colorido
- Vinculada? — ícone pequeno, só aparece quando `Sim`
- RFI — ícone pequeno, só aparece quando a demanda tem RFI vinculada
- Data de abertura

Clicar em qualquer parte da linha abre o detalhe da demanda (mesmo comportamento de antes, só
mudou a forma de listar). Os filtros em chip acima da tabela continuam exatamente como estavam
("Aguardando minha aprovação" em destaque, Status interno, Natureza, Vinculada?, Instituição) —
não mude os filtros, só a lista.

## 2. Detalhe da demanda: duas seções/ações novas

### Conversas (nova seção, separada dos Marcos)
Adicione uma seção **Conversas** no detalhe, visualmente distinta de Marcos:
- **Marcos** continua sendo o log formal — decisões e mudanças de status, sempre em ordem
  cronológica, nunca editável (append-only).
- **Conversas** é comunicação informal entre as pessoas envolvidas na demanda — mais parecido
  com um chat/thread de mensagens (autor, texto, hora). Também append-only (não edita nem
  apaga mensagem antiga), mas é bate-papo, não decisão.
- Deixe claro visualmente que são coisas diferentes (ex.: Marcos como linha do tempo formal,
  Conversas como bolhas de chat) — não misture os dois numa lista só.

### Ação de Reatribuir (nova ação, no topo do detalhe)
Adicione um botão **Reatribuir**, perto de onde já fica o Aprovar/Reprovar. Ao clicar, abre um
formulário simples pra trocar:
- Responsável e/ou Co-responsáveis, e/ou
- Destino (organizacional)

para outra pessoa/área. Ao confirmar, dois efeitos:
1. Os campos escolhidos são atualizados na demanda.
2. Um novo item aparece em **Marcos**, automático, registrando a transferência (ex.: "Reatribuída
   de [exemplo] Fulano para [exemplo] Beltrano em [data]") — não apaga o valor anterior, só
   registra a mudança como mais um marco.

## Regras para esta entrega

- Continue sem persistir nada de verdade (mesma regra da Tarefa 06) — Conversas e Reatribuir
  podem só mudar o estado visual local.
- Não use nome real de pessoa/cliente — "[exemplo]" onde precisar.
- Reaproveite os componentes que você já tem (badge, ícone, formulário simples, linha do tempo).
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi alterado (tabela, Conversas, Reatribuir).
2. Qualquer decisão que você tomou sozinho onde eu não te dei detalhe (ex.: onde o botão
   Reatribuir fica exatamente, como as bolhas de Conversas são estilizadas).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para dado real, persistência de verdade, ou criação de demanda até eu confirmar esta
etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
