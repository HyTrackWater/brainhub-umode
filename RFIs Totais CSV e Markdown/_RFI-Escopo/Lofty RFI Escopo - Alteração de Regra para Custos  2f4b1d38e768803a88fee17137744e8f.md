# Lofty | RFI: Escopo - Alteração de Regra para Custos de Variante

ID: 51
Responsável pela RFI: Marina Santoro
Status: RFI Post Mortem
Resumo Assunto: Alteração de Regra para Custos de Variante 
Criado em: 26 de janeiro de 2026 14:56
Data Liberação RFI: 5 de fevereiro de 2026
Demanda relacionada: Lofty Style
Horas Estimadas: 20
Valor Calculado: R$ 6.000,00
Valor Negociado com Cliente: R$ 2.544
Cobrada?: 🎁
👥 Clientes: Lofty Style (https://app.notion.com/p/Lofty-Style-293c8829d81c44d9ab8360ae66d24aab?pvs=21)
Task (Linear): https://linear.app/umode/project/lofty-alteracao-de-regra-de-negocio-rfi-51-e13eff795d68
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
| PRECO99 da tabela PRODUTO_PRECO_COR | Atualmente mandamos o valor da primeira variante e aplicamos o mesmo valor para todas as variantes do produto. 
A alteração é aplicar em cada variante do Linx o custo respectivo conforme está na aba de variantes, coluna custo da plataforma.

**Ajustar integração para preencher o custo de cada variante no campo PRECO_LIQUIDO1 (99) e PRECO1 (99) da tabela PRODUTOS_PRECO_COR.** | 4h | O racional de média de custo de mão de obra (fornecedor) se mantem como está. A alteração é não aplicar o valor da primeira variante para todos e sim cada variante com seu custo individual. |
| Custo 1 e campo VARIA_CUSTO_COR | Na tela de **Controle de Custo** da ficha do produto, estávamos mandando o valor da primeira variante para o campo **Custo 1**. 
A alteração é:
**1) Não enviar custo para o campo CUSTO_REPOSICAO1 da tabela PRODUTOS.**  | 4h | Mantem integrando com tabela PRODUTOS? Mas e quando o produto tiver mais de uma variante, qual valor devemos levar? A demanda inicial era não integrar mais em PRODUTOS mas sim em PRODUTOS_CORES.  |
|  | **2) Preencher o custo de cada variante na coluna CUSTO_REPOSICAO1 da tabela PRODUTO_CORES.** | 4h |  |
|  | **3) “Flegar” o campo VARIA_CUSTO_COR sempre como TRUE.** | 4h |  |
| Custos diferentes por variante | O time de importado sinalizou que no mesmo produto podem ter custos diferentes por variante, porém hoje não temos onde aplicar essa diferença na plataforma. 
Os custos que integramos até então são a soma de mão de obra (custo do fabricante) com os custos dos materiais empenhados na ficha técnica. Produtos importados não tem ficha técnica, logo não há onde diferenciar os custos do fornecedor por variante.
Esse caso é mais comum no importado mas também pode acontecer no produto acabado nacional. | 4h | @Ju Ferré Precisamos refinar esse ponto. Se for o caso, tiramos da RFI.

**Incluir campo custom/preco_custo_variante na integração. 
Se o campo custom/preco_custo_variante estiver preenchido, enviar na integração no lugar do nosso custo da variante padrão. Se for vazio ou zero, mandar o nosso custo por variante padrão do sistema.** |

---

- Anotações reunião 12/03/2026 com Marcello
    
    PRODUTO:
    
    - CUSTO_REPOSICAO1 → **pendente**
    
    PRODUTO_**COR**:
    
    - CUSTO_REPOSICAO1 → Campo da Variante e campo para preço fechado do importado
    
    PRODUTO_PRECO_**COR:**
    
    - PRECO1 (99) → Campo da Variante
    - PRECO_LIQUIDO1 (99) → Campo da Variante
    
    PRODUTO_OPE_EXTRA:
    
    - CUSTO_OPERACAO → Fornecedores
    
    Campo Custo_reposicao1 da tabela Produtos a integração está ok.
    
    Campo Custo_reposicao1 da tabela **Produto_cores** a integração está não ok.
    
    Campos Preco1 e Preco_liquido1 da tabela 99 - **Produtos_preco_cor** não está ok.
    
    Campo varia_custo_cor deverá estar 100% flegado.