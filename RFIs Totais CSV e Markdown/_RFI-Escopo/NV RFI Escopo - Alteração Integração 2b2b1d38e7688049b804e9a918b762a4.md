# NV | RFI : Escopo - Alteração Integração

ID: 25
Responsável pela RFI: Marina Santoro
Status: RFI Entregue ao Cliente
Resumo Assunto: Ajustes integração (status atual e filtro em mp)
Criado em: 21 de novembro de 2025 10:50
Data Liberação RFI: 22 de dezembro de 2025
Demanda relacionada: NV
Horas Estimadas: 24
Valor Calculado: R$ 7.200,00
Valor Negociado com Cliente: R$ 3.816
👥 Clientes: NV (https://app.notion.com/p/NV-c03ae4eca8ff4260a889b660803b4e26?pvs=21)
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
| Atualizar Integração de Escrita - Status Atual | Enviar o campo Status Atual (custom/status_atual) a cada alteração do campo. Desde o momento da criação da referência. O campo do Linx é o STATUS_PRODUTO da tabela PRODUTOS. Hoje a integração envia o texto do campo custom/status_atual para a tabela auxiliar PRODUTOS_STATUS, coluna DESC_STATUS_PRODUTO para trazer o STATUS_PRODUTO e vincular na tabela PRODUTOS. | @Marina Santoro Joao identificou isso no codigo. Nos temos um processo de validacao (3 “Sims”) que valida.

- | Como faremos envios pontuais deste campo fora do intervalo de 30 minutos padrão? |
| Integração de Leitura - Revisão de Filtros | Materiais - precisa tirar o filtro de coleções que existe nesta integração e tratar tal qual fazemos com os demais, puxando os materiais conforme o updated at. O formato atual requer que alguém lembre de informar a uMode a cada nova coleção e isso requer intervenção manual do time uMode a cada 3-6 meses no código. | 16-32 | @Felipe Sindeaux vai discutir se tem impacto a remoção, se houver algo significativo e material vamos para o plano de uma lista dinamica ou ler direto do linx |

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