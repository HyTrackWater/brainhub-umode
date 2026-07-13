# NK STORE | RFI : Escopo - Alteração de parâmetro (dados contábeis)

ID: 109
Responsável pela RFI: Marina Santoro
Status: RFI Liberada para Comercial negociar com Cliente
Resumo Assunto: Integração de escrita: Alteração de parâmetro de dados contábeis
Criado em: 11 de maio de 2026 11:44
Data Liberação RFI: 11 de maio de 2026
Demanda relacionada: NK STORE
Horas Estimadas: 4
Valor Calculado: R$ 1.200,00
👥 Clientes: NK STORE (https://app.notion.com/p/NK-STORE-0f24dfbef0ae43bbba528218d940b7ed?pvs=21)
criado por: Marina Santoro
Key Account: Julianne

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Integração de escrita: Alteração de parâmetro de dados contábeis para produtos do tipo uniforme (coleção ACOES) | Estamos cadastrando peças de uniforme para o nosso time. Contudo quando criamos um uniforme na Umode, ele desce com as configurações padrão de contas contábeis. Até então, as meninas estavam indo no linx e alterando a informação manualmente, porém com a integração de madrugada, todos os dias eles precisam refazer o processo, pois o produto voltava a ser revenda. 

Poderiam criar uma parametrização, de que quando o produto pertencer a coleção ACOES, sempre deve seguir esses campos de contas contábeis identificando que é um estoque de Uniformes? | 4h | Dados contáveis são puxados da tabela PARAMETRO_CONTA_CONTAVEL_UMODE.

O que seleciona o parametro da tabela é o campo INDIFCADOR_CFOP. 
Se for NK Fornecedor = 11. Qualquer outro é = 10.

A demanda seria colocar uma regra para quando for uniforme o CFOP = 13.

Confirmar com cliente a regra para identificar UNIFORME.  |

![image.png](NK%20STORE%20RFI%20Escopo%20-%20Altera%C3%A7%C3%A3o%20de%20par%C3%A2metro%20(dado/image.png)