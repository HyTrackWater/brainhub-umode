# NK STORE | RFI : Escopo - Alteração Integração

ID: 1
Responsável pela RFI: Marina Santoro
Status: RFI Post Mortem
Resumo Assunto: Ajustes integração
Criado em: 14 de agosto de 2025 10:23
Data Liberação RFI: 14 de agosto de 2025
Demanda relacionada: NK STORE
Horas Estimadas: 60
Valor Calculado: R$ 18.000,00
Valor Negociado com Cliente: R$ 18.000
Cobrada?: 🎁
👥 Clientes: NK STORE (https://app.notion.com/p/NK-STORE-0f24dfbef0ae43bbba528218d940b7ed?pvs=21)
Task (Linear): https://linear.app/umode/project/nk-integracao-de-escrita-rota-operacao-91683eb83fe0
https://linear.app/umode/project/nk-integracao-de-leitura-material-semi-acabado-rfi-1-0b610fc206ef/overview
criado por: Marina Santoro
Key Account: Julianne

<aside>
💡

Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação

</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** | **Ordem de Prioridade do Cliente** |
| --- | --- | --- | --- | --- |
| Materiais: alterar campo da largura do tecido | Alteração na integração de leitura de tecido para puxar largura da tabela ESTOQUE_MAT_PECA sendo o menor tamanho maior q zero. | 5h | ✅ Feito na semana de 03-07/11. | 7 |
| Materiais: custo de coenizados | Alteração na integração de leitura de tecido para o time SEMI ACABADO. A MP semi acabada é transformada no Linx dentro de uma ficha técnica própria, não tem entrada de nota fiscal e esse valor não reflete na coluna CUSTO_REPOSICAO da tabela MATERIAIS_CORES que puxamos para todos os materiais. Para essas MPs SEMI ACABADA precisa somar o valor total da ficha técnica do material para puxar para uMode. |  | Sugiro fazermos uma análise técnica se é viável ficar 100% do nosso lado ou se tem algo que a NK poderia apoiar somando a ficha técnica do material e preenchendo algum campo fixo para buscarmos o valor. | 8 |
| Ficha Técnica: incluir campo de percentual de consumo | Inclusão de campo na integração de escrita na parte de ficha técnica, com o campo custom/percentual_consumo de cada MP. Quando alguma cor de material não se aplica precisa enviar 0%. | 3h | ✅ Feito na semana de 19-29/08. | 9 |
| Ficha Técnica: incluir campo de material principal | Inclusão de campo na integração de escrita na parte de ficha técnica, com o campo custom/tipo_entrada indicando o material PRINCIPAL no Linx. | 3h | ✅ Feito na semana de 19-29/08. | 4 |
| Criação de referência de produto | Incluir na integração de escrita o código do produto na tabela TABELA = GRUPO E SUBGRUPO, campo CODIGO_SEQUENCIAL a cada novo produto. | 2h | ✅ Feito na semana de 03-07/11. | 3 |
| Rota - Custo Costura | Incluir na integração de escrita o campo price.manufacture quando a GRIFFE = NKO para o campo COSTURA = CUSTO_SUGERIDO da TABELA = PRODUTO_OPERAÇÕES_ROTAS.
Rota:
FASE = COSTURA (05)
SETOR = COSTURA (05)
RECURSO = DEFINIR (297) | 8h | Em andamento com tech ⏭️ | 1 |
| Rota - Demais Custos | Incluir na integração de escrita BENEFICIAMENTO da ficha técnica conforme os mesmos nomes na TABELA = PRODUTO_OPERAÇÕES_ROTAS. | 4h | Sugerimos o cliente usar o beneficiamento para atualizar/alterar valor do padrão da rota no Linx. Os beneficiamentos serão criados com o nome no mesmo formato da tela de Rota. // Em andamento com tech ⏭️ | 2 |
| Alterar cálculo do PRECO 04 com IPI quando TIPO = COURO | Incluir regra na integração de escrita na parte de preços, PRECO 04, quando o campo TIPO = COURO. Multiplicar o price.manufacture por 6,5% (0,065).
PRECO04 = PRECO03 + (PRECO03 * IPI) + empenhos (tecidos, aviamentos e beneficiamentos)
Exemplo: 2650 (2650*0,065) + (47,02+8,28) = 2877,55 | 2h | ✅ Feito na semana de 03-07/11. | 6 |
| Tabela de medidas | Incluir na integração de escrita tabela de medidas conforme as tabelas do Linx: PRODUTOS_TAB_MEDIDAS (Cria um produto como passível de incluir medidas) e PRODUTOS_MEDIDAS (Cria as medidas associadas a PK do Produto que esta na tabela anterior).
O time da NK gostaria de levar pontos de medidas específicos para o Linx e não a tabela completa para usar no ecommerce. | 32h | Entender com time uMode se é possível “filtrar” pontos de medida identificados de uma tabela de medidas para enviar somente os mesmos. // Em andamento com tech ✅ | 5 |

---

# De Acordo

**Responsável pelo Escopo uMode**

> Marina Gonçalves Santoro
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

14/08/2025

**Aprovado Em**