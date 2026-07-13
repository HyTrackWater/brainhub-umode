# Lofty | RFI: Escopo - Revisão Fator de Conversão

ID: 62
Responsável pela RFI: Laura Delgado
Status: RFI Cancelada
Resumo Assunto: Rever Fator de Conversão
Criado em: 6 de fevereiro de 2026 17:27
Data Liberação RFI: 19 de fevereiro de 2026
Demanda relacionada: Lofty Style
Horas Estimadas: 16
Valor Calculado: R$ 4.800,00
Valor Negociado com Cliente: R$ 2.544
Horas Trabalhadas: 1
Motivo do Cancelamento: Cancelado por falta de atualização no assunto. Se for relevante, criamos uma nova demanda.
👥 Clientes: Lofty Style (https://app.notion.com/p/Lofty-Style-293c8829d81c44d9ab8360ae66d24aab?pvs=21)
Task (Linear): Aguardando
criado por: Marina Santoro
Key Account: Laura

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Unidade de estoque e unidade de ficha técnica | Identificamos produtos que constavam com erro na integração pois a unidade empenhada no consumo estava divergente da unidade da base de dados. O cliente sinalizou que no Linx existe as duas informações: UNID_ESTOQUE, nossa unidade da base de dados do material; e UNID_FICHA_TEC, usada no empenho do material na ficha técnica do produto. 
O cliente sinalizou que precisamos trazer a UNID_FICHA_TEC para a base. 

Exemplo: BLUSA CORNELIA 04.02.0109 - MP 020377
Unidade da base (UNID_ESTOQUE): peça (PC)
Unidade do empenho (UNID_FICHA_TEC): unidade (UN) | 8h desenvolvimento
8h de Q&A |  Sugiro trazermos a UNID_FICHA_TEC no fator de conversão. Assim o time pode usar a UNID_ESTOQUE ou UNID_FICHA_TEC no empenho e não teremos erro de integração. |

---

# De Acordo

**Responsável pelo Escopo uMode**

> 
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

**Aprovado Em**