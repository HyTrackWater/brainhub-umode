# Prompt de execução — BrainWave · Tarefa 02: aba Home personalizada

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. Depende da Tarefa 01 (esqueleto de navegação) já estar pronta.

---

Construa o conteúdo da aba **Home**, dentro da casca de navegação já criada. A Home é
**personalizada por pessoa** — mostra um resumo de quem está logado, baseado na cadeira dela,
mais uma caixa de entrada com o que está pendente pra ela.

**Ainda não há login real nem dado real conectado.** Monte a tela pra ler de uma estrutura de
dado da pessoa logada (não hardcode os valores no layout) e use o exemplo abaixo só pra
preencher visualmente — marque qualquer texto de exemplo como tal (ex.: prefixo "[exemplo]").

**Estrutura de dado da pessoa logada** (campos que a Home precisa exibir):

- Foto — hoje sempre vazia (bloco/avatar placeholder, sem foto real ainda)
- Nome preferido
- Cadeira / cargo atual
- Nível HIC — nível na jornada de aprendizado e uso de IA da pessoa. Pode vir vazio (a escala
  ainda não existe) — nesse caso, não mostre um badge quebrado, simplesmente omita esse dado
  até existir
- Área (organizacional)
- Data de entrada na uMode — mostre a **data em si**, não só um tempo calculado
- Tempo na uMode — calculado a partir da data de entrada (ex.: "1 ano e 3 meses"). Se a data de
  entrada não existir, não mostre um número inventado — mostre que essa informação falta
- Resumo — texto curto sobre a pessoa. Vem de uma autodescrição pessoal quando existir; se não
  existir, cai pra uma descrição baseada no papel/responsabilidades dela. Indique visualmente
  (texto pequeno, discreto) qual das duas fontes está sendo usada
- Clientes atuais atendidos — lista de organizações/contas que a pessoa atende agora (pode ser
  vazia, pra quem não atende cliente direto)
- Inbox — lista das solicitações em aberto onde a pessoa é responsável ou autora, cada uma com:
  nome da organização/conta relacionada, título curto, e um status (ex.: em fila, em andamento,
  aguardando validação). Mostre um resumo (ex.: "5 abertas") e um botão "ver todas"

**Dado de exemplo pra preencher visualmente** (marcar como exemplo, não real):
- Nome preferido: "[exemplo] Ana"
- Cadeira: "[exemplo] Key Account"
- Nível HIC: (deixe de fora — está vazio no exemplo também, pra provar que a tela lida bem com
  ausência)
- Área: "[exemplo] a preencher" (mostre também o estado "sem dado ainda", não só o caminho
  feliz)
- Data de entrada: "[exemplo] a preencher" — e o "Tempo na uMode" refletindo essa ausência
- Resumo: "[exemplo] Gestão de relacionamento com clientes como Key Account." com a indicação
  discreta de que veio do papel/responsabilidades, não de autodescrição
- Clientes atuais atendidos: "[exemplo] Cliente A", "[exemplo] Cliente B", "[exemplo] Cliente C"
- Inbox, 3 itens de exemplo:
  1. "[exemplo] Cliente A" · "Ajuste de campo na ficha de produto" · status "em fila"
  2. "[exemplo] Cliente A" · "Revisão de regra de integração" · status "em andamento"
  3. "[exemplo] Cliente B" · "Hierarquia de categoria" · status "em fila"

**Regras para esta entrega:**
- Não use nenhum nome real de pessoa, cliente ou produto — só os marcados "[exemplo]" acima.
- Construa a tela pra funcionar tanto com dado completo quanto com campos vazios — a maioria
  dos dados reais que vamos plugar depois vai ter partes faltando, isso não pode quebrar o
  layout.
- Não construa edição ainda — a Home é só leitura nesta etapa.
- Siga as convenções que você já usa neste projeto.

**Ao terminar, me diga:**
1. O que foi construído.
2. Qualquer decisão que você tomou sozinho onde eu não te dei detalhe.
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para dado real, edição, ou outras abas de conteúdo até eu confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
