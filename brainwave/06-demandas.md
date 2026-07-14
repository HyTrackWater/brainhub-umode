# Prompt de execução — BrainWave · Tarefa 06: aba "Demandas" (com RFI dobrada dentro)

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. Depende da Tarefa 01 (esqueleto de navegação) já estar pronta.

---

Esta tarefa **altera e preenche** a aba "Demandas" criada na Tarefa 01, e **remove a aba
"RFIs"** do menu principal — RFI vira uma seção dentro do detalhe da Demanda, não navegação
própria.

## Conceito central desta tela (leia antes de desenhar)

Toda atividade de um colaborador — perceber que algo precisa mudar, que uma pessoa saiu, que um
cliente pediu algo — nasce como uma **Demanda**. Toda demanda nasce internamente aqui dentro,
antes de qualquer outra ferramenta. Uma demanda pode ou não precisar de **aprovação** de alguém
(quando ela muda algo no contexto institucional) — e essa fila de "coisas que alguém precisa
aprovar ou reprovar" é a atividade mais frequente que um colaborador vai ter nesta tela. Uma
demanda pode ou não, depois de aprovada, ganhar vínculo com um sistema operacional externo (hoje
só existe vínculo com o CX Hub, mas o campo já foi desenhado pra aceitar outros sistemas no
futuro — não construa esses outros sistemas agora).

## O que muda no menu principal

Remova a aba **"RFIs"**. Nenhuma outra aba muda.

## Estrutura da tela "Demandas"

**Lista, não grade** (demanda é acionável, não um catálogo visual). Filtros em chip, no topo,
combináveis:

- **Aguardando minha aprovação** (toggle, em destaque visual diferente dos outros filtros — é o
  mais importante da tela)
- **Status (interno):** Aberta · Em andamento · Concluída · Cancelada
- **Natureza:** Interna · Inter-área · Intra-área · Casa-cliente
- **Vinculada?:** Sim · Não
- **Instituição:** uMode ou um cliente específico (hoje 4: "[exemplo] Cliente A/B/C/D")

Cada item da lista mostra: título, Natureza, Origem → Destino (organizacional), badge de Status
(interno), selo pequeno "vinculada" só quando `Vinculada? = Sim` (sem especificar o sistema no
selo — isso fica pro detalhe), selo pequeno "RFI" só quando a demanda tem uma RFI vinculada,
data de abertura.

## Detalhe (ao clicar numa demanda)

- **Identificação**: título, Natureza, Origem/Destino organizacional, Status (interno)
- **Conteúdo**: Descrição, Resultado esperado, Resolução (quando concluída)
- **Aprovação de contexto — seção em destaque no topo, não escondida**: mostra se aprovação é
  necessária, quem aprova, e o status atual. Quando o usuário logado é quem precisa aprovar,
  mostre ações diretas de **Aprovar** / **Reprovar** ali mesmo — é o coração desta tela
- **Marcos** — lista cronológica, estilo linha do tempo/conversa (cada marco é uma linha:
  data, evento/decisão, responsável). Nunca editável — é log, só cresce
- **Vínculo** (só aparece quando `Vinculada? = Sim`): mostra a lista de sistemas vinculados (ex.:
  "CX Hub — ID: UMD-317"). Quando o vínculo inclui CX Hub, mostra também os campos operacionais
  do CX Hub (Quadro, Status, Prioridade, Tipo) abaixo, num bloco próprio — claramente rotulado
  como "CX Hub", pra não confundir com o Status (interno) da demanda
- **RFI, dobrada aqui dentro** (não é aba própria): quando a demanda tem uma RFI vinculada,
  mostre um bloco resumido — escopo, dado comercial (horas/valor), status de aprovação de
  escopo. Não precisa ser uma tela cheia separada, é uma seção dentro do detalhe da demanda
- **Relacionamentos**: Demanda mãe (se houver) e Demandas filhas (lista, cada uma com indicação
  se bloqueia a conclusão da mãe)
- **Governança**: quem pode alterar este registro

## Dado de exemplo (marcar como exemplo)

Use 6-8 demandas de exemplo cobrindo as combinações: pelo menos 1 "Aguardando minha aprovação",
pelo menos 1 com `Vinculada? = Sim` (mostrando o bloco CX Hub), pelo menos 1 com RFI vinculada
(mostrando o resumo dobrado), pelo menos 1 puramente interna sem nenhum vínculo, e pelo menos 1
com Demanda mãe + filhas. Nomes de cliente/pessoa sempre "[exemplo]".

## Regras para esta entrega

- Ainda não construa formulário de criação de Demanda — isso é leitura + ação de aprovar/
  reprovar, não criação ainda.
- O botão Aprovar/Reprovar pode só mudar o estado visual local por ora — não precisa persistir
  em lugar nenhum real.
- A tela precisa lidar bem com todos os campos vazios (sem Vínculo, sem RFI, sem Demanda mãe)
  sem quebrar layout.
- Reaproveite os componentes que você já tem (lista, filtro/chip, estado vazio, badge).
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi construído/alterado (incluindo a remoção da aba RFIs).
2. Qualquer decisão que você tomou sozinho onde eu não te dei detalhe (ex.: onde exatamente o
   selo "vinculada" aparece na lista, como fica o botão Aprovar/Reprovar visualmente).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para dado real, criação de demanda, ou vínculo com outros sistemas além do CX Hub até
eu confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
