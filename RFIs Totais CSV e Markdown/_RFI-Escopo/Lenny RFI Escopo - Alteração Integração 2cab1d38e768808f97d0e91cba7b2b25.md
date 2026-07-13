# Lenny | RFI : Escopo - Alteração Integração

ID: 36
Responsável pela RFI: Marina Santoro
Status: RFI Cancelada
Resumo Assunto: Alteração regra de negócios de integração de leitura e escrita
Criado em: 15 de dezembro de 2025 14:46
Data Liberação RFI: 5 de fevereiro de 2026
Demanda relacionada: Lenny Niemeyer
Horas Estimadas: 18
Valor Calculado: R$ 5.400,00
Valor Negociado com Cliente: R$ 2.862
👥 Clientes: Lenny Niemeyer (https://app.notion.com/p/Lenny-Niemeyer-b3aad92958894c71b1e1ddd096db52ed?pvs=21)
Task (Linear): https://linear.app/umode/project/lenny-alteracao-de-regra-de-negocio-rfi-36-9ffc076a60e5
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
| Descrição da Cor em Inglês | O time Linx da Lenny vai criar o controle para nomes em inglês na base de cores. Hoje é feito por produto mas é ineficiente visto que precisa escrever o mesmo nome diversas vezes. O próprio time da Linx também vai criar automação para aba de variante puxar o nome da cor em inglês no momento do cadastro. 
  1) Para uMode é importante não sobre escrever o Linx, com isso, precisamos tirar o campo custom/x da integração de escrita. | 2h | Tirar o campo custom/descricao_ingles_cor da integração de escrita. |
|  | 2) Para uMode, é importante que o time visualize o nome da cor em inglês. Devemos receber na integração de leitura do Linx da base de cores e usar o campo CARTELA para aplicar a mesma.  | 2h | Incluir na  integração de leitura do Linx da base de CORES o campo da cor em inglês e usar o campo CARTELA da uMode para aplicar a mesma.  |
|  | 3) Para uMode, é importante que o time visualize o nome da cor em inglês na aba de variante.  | 3h |  Mostrar o nome da cor em inglês (campo CARETLA da base CORES) na aba de variante. 
A informação da CARTELA aparece no campo color_id mas fica somente dentro da aba. Precisa validar com o cliente se atende. |
| Descrição do Produto em Inglês | Hoje as descrições de produto passam por um importador para traduzir o nome dos produtos de português para inglês. É feito através de planilha e imputada manualmente no Linx. A dor do time de desenvolvimento é: as vezes precisa incluir um produto depois dessa lista de nomes feita e o próprio time precisa cadastrar a descrição em inglês e queriam visualizar os nomes já cadastrados no Linx para ver quais produtos faltam. A solução encontrada foi a uMode ser a origem do cadastro, recebendo a planilha de nomes em inglês, tendo o campo aberto para eventuais novos produtos e levar isso via integração de escrita para o Linx. | 1h | Incluir campo para descrição do produto em inglês na uMode. |
|  |  | 2h | Integrar campo custom/x com o campo y da tabela w do Linx. |
| Controle de Variantes entre uMode e Linx | As divergências de quantidade de variantes atrapalha o dia a dia do time e com isso definimos novas regras de negócios sobre integração de variantes:
  • Se excluir uma cor na uMode, excluir também no Linx;
  • Se substituir o nome de uma cor na uMode, substituir também no Linx.
Os números de variantes precisa ser igual entre os sistemas. 
Algumas travas que impedem esse fluxo:
  • Se tiver ficha técnica preenchida na uMode, não pode excluir ou substituir variante;
  • Se o status atual (campo custom) do produto for igual a APROVADO PARA PRODUÇÃO ou LIBERADO PARA MOSTRUÁRIO, não pode excluir ou substituir variante. | 4h | Alterar integração de escrita de variantes:
 • Se excluir uma cor na uMode, excluir também no Linx;
  • Se substituir o nome de uma cor na uMode, substituir também no Linx. |
|  |  | 4h | Incluir travas nas fichas:
 • Se tiver ficha técnica preenchida na uMode, não pode excluir ou substituir variante;
  • Se o status atual (campo custom) do produto for igual a APROVADO PARA PRODUÇÃO ou LIBERADO PARA MOSTRUÁRIO, não pode excluir ou substituir variante. |

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