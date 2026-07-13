# Protocolo · Gestão de RFI

> RFI = Request for Implementation. Formaliza uma demanda para ser apresentada e negociada
> com o cliente e, eventualmente, aprovada para desenvolvimento. Toda RFI nasce de uma
> demanda — nunca existe RFI sem demanda de origem. Nem toda demanda vira RFI.

## Onde vive
`_rfis/` é uma subpasta fixa em `00_Institucional/`, mas só do lado de cada **Cliente** — RFI
sempre se refere a um cliente específico (campo obrigatório), diferente de Demanda, que pode
ser 100% interna. Não existe `_rfis/` do lado da Casa uMode.
- Endereçamento: `Cliente:Acme › RFIs › RFI-2026-005`.
- ID: `RFI-AAAA-NNN`, sequencial por cliente **dentro do ano** — `AAAA` é o ano de criação real
  da RFI (`Criado em`), não o ano da formalização.
- **ID legado (Notion/CX Hub)** — guarda o ID original do sistema de origem (ex.: `RFI-51` do
  Notion, que vira `RFI-2026-002` no nosso padrão), quando a RFI vier de migração.

## Como nasce
No CX Hub, a RFI é criada **de dentro de uma demanda** — não é um registro independente aberto
do zero. O campo `Demanda relacionada` é, portanto, sempre obrigatório: é a prova formal do
vínculo. Do lado da demanda, o campo `RFI vinculada` (já existente no template de Demanda)
recebe o ID desta RFI. Vínculo sempre bidirecional — os dois lados preenchidos.

## Ciclo de vida (dois níveis — Grupo e Status)
> Fonte: Notion (legado). O CX Hub ainda não expôs uma taxonomia própria de RFI documentada —
> adotamos esta como base de trabalho, sujeita a ajuste quando os campos do CX Hub forem
> detalhados.

| Grupo | Status |
|---|---|
| A fazer | RFI em Rascunho |
| A fazer | RFI Stand By |
| A fazer | RFI Não Iniciada |
| Em andamento | RFI Pronta para Estimar |
| Em andamento | RFI Aceita — Criar Demanda e Estimar Entrega |
| Em andamento | RFI Liberada para Comercial negociar com Cliente |
| Em andamento | RFI Em Andamento |
| Em andamento | RFI Q&A Negócios |
| Em andamento | RFI Post Mortem |
| Concluídos | RFI Entregue ao Cliente |
| Concluídos | RFI Não Aceita |
| Concluídos | RFI Cancelada |

`Motivo do cancelamento` só é preenchido quando Status = `RFI Cancelada`.

## Anatomia da RFI (campos)

### Identificação
- ID
- Cliente
- Nome — descrição livre da RFI (texto, imagem, arquivo — equivalente à aba "Conteúdo" da
  demanda)
- Resumo do assunto — versão curta
- Demanda relacionada (obrigatório)
- Criado por
- Data de criação

### Taxonomia
- Grupo / Status (tabela acima)
- Motivo do cancelamento (condicional a Status = RFI Cancelada)

### Comercial
- Horas estimadas
- Valor negociado com o cliente — aceita valor fechado ou faixa/estimativa livre (dado real de
  origem já vem assim, ex.: "24k+6.5k")
- Cobrada? (sim/não)
- Taxa aplicada (R$/h) — a taxa vigente no momento do cálculo (hoje R$300/h); registrar aqui
  porque a taxa pode mudar com o tempo e o valor já calculado não deve ser recalculado
  retroativamente
- Valor calculado — Taxa aplicada × Horas estimadas
- Data planejada de execução — aceita data única **ou** intervalo (data início → data fim)
- Horas trabalhadas — comparativo com horas estimadas

### Datas
- Data liberação RFI
- Data aceite do cliente

### Conteúdo / narrativa (página, não campo de banco)
Vive junto com a descrição livre da RFI (mesmo bucket de "Nome" acima) — só é preenchido
manualmente, não vem de CSV/export estruturado:
- Justificativa da estimativa — quando Horas estimadas > 10h, explica o motivo do volume
- Aprovação de escopo (De Acordo) — responsável nomeado + data de aprovação dos dois lados
  (uMode e Cliente), quando registrado; complementa (não substitui) `Data aceite do cliente`

### Responsáveis
- Responsável(is) interno(s) — uMode, pode ser mais de um
- Key Account no momento da criação — pessoa(s); é um retrato do momento, não é atualizado
  retroativamente se a KA do cliente mudar depois (o dado vivo de KA é cadastral e mora em
  `pessoas.md`)

### Governança
- Quem pode alterar este documento

## Multi-cliente (regra de migração)
RFI é sempre de **1 cliente só** — regra travada, não muda. Dado legado do Notion pode
mostrar uma RFI com 2+ clientes na mesma linha (ex.: uma RFI de "custo dinâmico" listando
uMode + Lofty Style); na formalização, isso vira **duas RFIs separadas**, uma por cliente,
não um campo de lista.

## Campos do Notion descartados (redundantes ou fora do nosso padrão)
| Coluna Notion | Por quê descartada |
|---|---|
| Demanda Cliente | Já coberto por `Demanda relacionada` |
| Detalhamento Cliente | Já coberto por `Nome`/`Resumo do assunto` |
| Estimativa uMode | Já coberto por `Horas estimadas` |
| Comentário uMode | Sem campo equivalente — decisão do CEO/Vinicius, sem uso suficiente |
| Cobrada? (emoji: 🎁 💰 🚫) | Ruído do Notion — usar o campo `Cobrado` (Sim/Não/vazio) real da
base como fonte de `Cobrada? (sim/não)` |
| Task (Linear) | Fora do nosso modelo — não capturamos referência a sistemas de tracking
internos (Linear, Kanbanize, CX Hub legado etc.) dentro da RFI |

> Registrado aqui para quando a tradução demanda-a-demanda/RFI-a-RFI do Notion acontecer: se
> uma RFI antiga tiver dado nessas colunas, ele só precisa ser verificado contra os campos
> equivalentes acima, não recriado.

## Relação com Demanda — regra de consistência
- `Demanda.RFI vinculada` ⟷ `RFI.Demanda relacionada` — vínculo bidirecional, sempre os dois
  lados preenchidos.
- Uma demanda pode não ter nenhuma RFI. Uma RFI sempre tem exatamente uma demanda de origem.
- O ciclo de vida da RFI é independente do `Status` (CX Hub) da demanda de origem — a demanda
  pode estar `Concluído` enquanto a RFI ainda está `Em Andamento` (ou vice-versa): a demanda
  registra a necessidade, a RFI registra a negociação/entrega comercial.
- **Dívida do Notion legado:** na base antiga, `Demanda relacionada` muitas vezes só traz o
  nome do cliente, não o ID de uma demanda específica — não é erro do nosso modelo, é uso
  incorreto do campo no Notion. Nada a mudar no padrão; a reconciliação (achar a demanda real
  por trás de cada RFI legada) acontece manualmente, RFI a RFI, na migração. O campo
  `🤿 Demandas de Clientes` (quando preenchido) pode ajudar como pista, mas não vira campo
  novo do nosso padrão.

## Governança
- Abertura de RFI → responsável de atendimento (uMode), sempre a partir de uma demanda
  existente.
- Este protocolo → Vinicius Risoléo + CEO.
