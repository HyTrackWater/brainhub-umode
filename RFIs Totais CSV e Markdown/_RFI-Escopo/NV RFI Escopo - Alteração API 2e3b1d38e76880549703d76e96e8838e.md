# NV | RFI : Escopo - Alteração API

ID: 42
Responsável pela RFI: Andre
Status: RFI Entregue ao Cliente
Resumo Assunto: Adição/ Ajuste de Campos em RFI anteriormente aprovada (OS 118)
Criado em: 9 de janeiro de 2026 10:18
Data Liberação RFI: 7 de janeiro de 2026
Demanda relacionada: NV
Horas Estimadas: 12
Valor Calculado: R$ 3.600,00
Valor Negociado com Cliente: R$ 1.908
👥 Clientes: NV (https://app.notion.com/p/NV-c03ae4eca8ff4260a889b660803b4e26?pvs=21)
criado por: Andre

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Ajustar o ***createdAt*** para refletir o horário da fotografia | * Esta opção tecnicamente é incorreta. O correto é adicionar um campo “snapshotAt” que pode incluir a data necessária * Validação do José esteja afixada. | 2h ✅ | @João Ferraz Já adicionou o campo  |
| Ajustar os horários da geração das fotografias | * 9h30 UTC
* 15h30 UTC
* 19h00 UTC | 2h ✅ | @João Ferraz Já alterou as cronjobs  |
| Checagem dos campos da dataClass = 2 | Demanda do cliente não está suficientemente clara: Diferença de quantidade de registros do dataClass 2 quando comparado com a view2 de aviamentos (JSON) | 4h ✅ | @João Ferraz revisou a dataClass=2 
São 19 entradas e no bucket tem 19 entradas, mas é aditiva para cada snapshot (anteriormente validado pelo Pablo) |
| Correção dos campos de vendas (foto) | Aparentemente temos valores concatenados sem valor presente. Inserir “null” como padrão de onde não houver o valor na entrada. | 4h ✅ | @João Ferraz validar pq o campo concatena MOEDA + VALOR e parece nao estar correto |
| Otimização da Query do Legado “dataClass = 1” Tem 600 linhas (!!!) e leva minutos para rodar. | Impacto no desempenho, memoria da tabela do banco, indisponibilidade do dataClass | 4h | @João Ferraz  |

---

# De Acordo

**Responsável pelo Escopo uMode**

> Andre Borges
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

12/01/2026

**Aprovado Em**