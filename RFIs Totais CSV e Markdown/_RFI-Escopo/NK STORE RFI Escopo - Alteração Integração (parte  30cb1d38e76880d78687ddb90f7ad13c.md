# NK STORE | RFI : Escopo - Alteração Integração (parte 4)

ID: 66
Responsável pela RFI: Marina Santoro
Status: RFI Post Mortem
Resumo Assunto: Alteração de Regra
Criado em: 19 de fevereiro de 2026 13:44
Data Liberação RFI: 19 de fevereiro de 2026
Demanda relacionada: NK STORE
Horas Estimadas: 6
Valor Calculado: R$ 1.800,00
Valor Negociado com Cliente: R$ 1.800
Cobrada?: 🎁
👥 Clientes: NK STORE (https://app.notion.com/p/NK-STORE-0f24dfbef0ae43bbba528218d940b7ed?pvs=21)
🤿 Demandas de Clientes: Insert e update dos campos COD_CATEGORIA e PERIODO_PCP no Linx (https://app.notion.com/p/Insert-e-update-dos-campos-COD_CATEGORIA-e-PERIODO_PCP-no-Linx-31ab1d38e76880678aa3e78e675c1bdd?pvs=21)
Task (Linear): https://linear.app/umode/project/nk-integracao-de-escrita-4ef61ef1b5e2
criado por: Andre
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
| Insert e update dos campos COD_CATEGORIA e PERIODO_PCP no Linx | Na configuração da integração de escrita foi definido que apenas um dos campos (COD_CATEGORIA ou PERIODO_PCP) receberiam a atualização enquanto o outro teria o primeiro valor gravado estático. Porém o cliente solicitou revisão e afirmou que ambos os campos precisam receber atualização. 

Solicitação do cliente: ”ao preencher o campo "período de entrega" na plataforma, ele não refletiu no campo "categoria" do linx (o que era pra ter acontecido como habitual). Após análise do time tech, foi constatado que existe uma regra de negócio que não permitiu a alteração no campo "categoria" dentro do linx. Isso porque o produto integrou pela primeira vez com a categoria 2A, mas ao integrar pela segunda vez alterou somente o PCP e não o "categoria" por conta da regra citada”. **Sempre o período PCP deve ser igual a Categoria.**” | 6h | De acordo com o mapeamento de integração, ambos os campos do Linx recebem do campo custom/periodo_pcp. Sendo texto no PERIODO_PCP e o código no COD_CATEGORIA. Isso se mantém.  |

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