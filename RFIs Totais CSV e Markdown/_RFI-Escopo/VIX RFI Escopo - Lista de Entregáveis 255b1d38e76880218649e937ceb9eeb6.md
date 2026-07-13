# VIX | RFI : Escopo - Lista de Entregáveis

ID: 12
Responsável pela RFI: João Risoléo
Status: RFI Entregue ao Cliente
Resumo Assunto: API Time Qualidade - OS 120
Criado em: 20 de agosto de 2025 16:48
Data Aceite do Cliente: 25 de setembro de 2025
Data Liberação RFI: 23 de julho de 2025
Demanda relacionada: VIX
Valor Calculado: R$ 0,00
Valor Negociado com Cliente: R$ 15.100
Cobrado: Sim
👥 Clientes: VIX (https://app.notion.com/p/VIX-70a10ec2756f4842a04cb12675a09d22?pvs=21)
criado por: Marina Santoro

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Caso de Uso | No "Controle de Qualidade" utilizam a tabela de medidas, atributos, cores, aviamentos, para conferir a aderência entre o produto pronto e o cadastro da uMode. Elas, atualmente, imprimem e utilizam.
Eles possuem um sistema de inspeção de qualidade, e querem que os dados da uMode apareçam dentro deste sistema.
A integração será de mão única, ou seja, a uMode disponibilizará API para que os dados sejam consumidos. Não haverá integração de volta para a uMode.
Todas as revisoras farão uso via tablet (cerca de 30 atualmente~até 50) |  |  |
| Definições sobre a API | API Aberta: Interface RESTful com autenticação básica, via X-API-TOKEN. A requisição será feita pelo método GET passando o parâmetro o Código Linx da variante do produto (itemRefSku).  |  | O campo mestre na API será o Código Linx (custom/cod_linx). |
| Campos e Dados | [Link dos dados a constar nas APIs: anexo principal](https://docs.google.com/spreadsheets/d/16xHJlOM-N9fDylNFHDIwfzItVF_-9i636i-iLX2bQs0/edit?userstoinvite=andre.borges%40umode.com.br&sharingaction=manageaccess&role=writer&gid=604991093#gid=604991093) |  | Como fonte da origem: são 16 campos, 3 categorias de imagem  e 2 tabelas (materiais e tabelas).  |
| Uso e Frequência | A requisição trará o retorno dos dados do item. Haverá um limite no sistema de 5 requisições por segundo.  |  |  |

---

# De Acordo

**Responsável pelo Escopo uMode**

> João Risoleo
> 

**Responsável pelo Escopo Cliente**

> Luana e Jaque (Vix) + Felipe Conde (Sistema da Qualidade)
> 

**Aprovado Em** 

23/07/2025

**Aprovado Em**

25/09/2025