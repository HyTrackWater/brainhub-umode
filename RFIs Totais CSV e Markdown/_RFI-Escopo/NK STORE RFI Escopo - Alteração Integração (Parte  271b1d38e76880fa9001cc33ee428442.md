# NK STORE | RFI : Escopo - Alteração Integração (Parte 2)

ID: 19
Responsável pela RFI: Marina Santoro
Status: RFI Post Mortem
Resumo Assunto: Complemento dos ajustes de integração
Criado em: 17 de setembro de 2025 15:37
Data Liberação RFI: 18 de setembro de 2025
Demanda relacionada: NK STORE
Horas Estimadas: 8
Valor Calculado: R$ 2.400,00
Valor Negociado com Cliente: R$ 2.400
Cobrada?: 🎁
👥 Clientes: NK STORE (https://app.notion.com/p/NK-STORE-0f24dfbef0ae43bbba528218d940b7ed?pvs=21)
Task (Linear): https://linear.app/umode/project/nk-integracao-de-escrita-4ef61ef1b5e2
criado por: Marina Santoro
Key Account: Julianne

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** | **Ordem de Prioridade do Cliente** |
| --- | --- | --- | --- | --- |
| Ficha Técnica: limitar a 1 material com a flag de material principal | Esse item precisa de um ajuste: por padrão o sistema LINX só permite que se selecione um material principal, pelo que acompanhei ontem com o PCP, uma das mensagens de erro que o Linx apresenta quando tenta fazer a alteração do custo de uma fase é que o produto possui mais de um material principal.

Essa informação do material principal é principalmente usada na tela que faz a análise invertida de MP.

Dessa forma, entendo que a uMode dever travar a possibilidade da seleção de mais de um material como principal. |  | Tratado com Ops ✅ Demanda concluída. | 1 |
| Mensagem do Linx: Recalcular as ordens de produção em andamento | Conforme o time do PCP trouxe, quando alterávamos algo na ficha técnica, que já tinha op em aberto, o Linx perguntava "quer recalcular as ordens de produção em andamento?" e sempre colocamos sim. Conforme fazemos alteração no uMode, sobe para a ficha Linx, mas não altera as ordens de produção e precisa ser alterado.
 |  | Escopo incompleto | 2 |
| Atualizar campo INATIVO da tabela PRODUTO_COR quando a variante for cancelada | Quando o campo custom/status_variante for igual a CANCELADO na uMode, precisa enviar “true (1)” no campo do Linx INATIVO da tabela PRODUTO_COR. | 8h | Linear | 3 |

---

# De Acordo

**Responsável pelo Escopo uMode**

> Marina Gonçalves Santoro
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

18/09/2025

**Aprovado Em**