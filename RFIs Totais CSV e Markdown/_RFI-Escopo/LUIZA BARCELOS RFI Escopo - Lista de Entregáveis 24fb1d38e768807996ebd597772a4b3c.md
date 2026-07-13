# LUIZA BARCELOS | RFI : Escopo - Lista de Entregáveis

ID: 2
Responsável pela RFI: Marina Santoro
Status: RFI Cancelada
Resumo Assunto: API
Criado em: 14 de agosto de 2025 10:28
Data Liberação RFI: 19 de agosto de 2025
Demanda relacionada: Luiza Barcelos
Horas Estimadas: 64
Valor Calculado: R$ 19.200,00
Motivo do Cancelamento: 16/09/25: O cliente fez uma atualização na rota tirando a informação de fornecedores e assim conseguiu manter em um endpoint único. Entendo que está RFI está encerrada.
👥 Clientes: Luiza Barcelos (https://app.notion.com/p/Luiza-Barcelos-b0c819c0bda449528d9d984b3200f07f?pvs=21)
criado por: Marina Santoro

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode** (se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Solicitação da uMode inclusão do updated_at nas rotas da API para controlar o que é novo ou foi alterado e não processar a carga inteira diariamente. | Com relação a API de  sftipmat, é composta pelo relacionamento de várias tabelas e cada uma com seu  updateat. Para contemplar o update at do conteúdo desta API disponibilizado via Swagger: 
API SFTITEMLOG -> CONTEMPLA PROPRIEDADES NOME,CODIGO,TIPO

API SFTCORLOG -> CONTEMPLA PROPRIEDADE VARIANTE.NOME

API  SFTMCILOG->CONTEMPLA PROPRIEDADE VARIANTE.CODIGO_COR

API  SFTMATLOG->CONTEMPLA PROPRIEDADE  VARIANTE.COMPOSIÇÃO

API STFORITEMLOG-> CONTEMPLA PROPRIEDADES  FORNECEDORES.NOME, FORNECEDORES.REFERENCIA

API SFTMEDLOG-> CONTEMPLA PROPRIEDADE FORNECEDORES.UNIDADE | Estimativa Tech - 40 horas

Estimativa Operação - 10 horas | O escopo da rota de materiais (sftipmat) validada pelo cliente dia 22/07/2025. No dia 07/08/25  foi alterado, pois a estrutura do cliente não permite trabalhar com updated_at alinhados em um só objeto. O cliente criou várias rotas para os materiais e temos que analisar a possibilidade de fazer isso do nosso lado. |
| Inclusão de custo na API sftipmat. | Pendente alinhamento do cliente. | Estimativa Tech - 10 horas

Estimativa Operação - 4 horas | O cliente sinalizou que tem interesse em usar a função de Pré Custo já existente na uMode e para isso, precisamos receber os custos dos materiais cor via API. |

---

# De Acordo

**Responsável pelo Escopo uMode**

> Marina Gonçalves Santoro
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

19/08/2025

**Aprovado Em**