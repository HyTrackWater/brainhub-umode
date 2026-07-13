# NV | RFI : Escopo - Alteração Integração (flag varia preço cor)

ID: 68
Responsável pela RFI: Marina Santoro
Status: RFI Em Andamento
Resumo Assunto: Flag varia preço cor
Criado em: 23 de fevereiro de 2026 14:48
Data Liberação RFI: 23 de fevereiro de 2026
Demanda relacionada: NV
Horas Estimadas: 9
Valor Calculado: R$ 2.700,00
Valor Negociado com Cliente: R$ 1.431
👥 Clientes: NV (https://app.notion.com/p/NV-c03ae4eca8ff4260a889b660803b4e26?pvs=21)
🤿 Demandas de Clientes: Integração flag VARIA PREÇO COR (https://app.notion.com/p/Integra-o-flag-VARIA-PRE-O-COR-276b1d38e76880d38cabcca20e7346b2?pvs=21)
Task (Linear): https://linear.app/umode/project/nv-integracao-de-escrita-0c679fa39665
criado por: Marina Santoro
Key Account: Fernanda

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Integração do Flag Varia Preço Cor | Precisamos que os produtos criados venham com a TAG ativa, pois hoje precisamos habilitar
manualmente ou em massa via chamado junto ao TI, e a partir dessa ativação, onde o preço
passa a ser consumido por outra tabela que a integração já ocorra nas Duas tabelas : select *
from produtos_precos e select * from PRODUTOS_PRECO_COR, e criar campo para ativação
e inativação da da integração do preço. |  |  |
|  | Criar flag 'Integra preço' - True/False | 0,5h Ops e 4h Tech | Criar campo custom/varia_preco_cor na ficha para o cliente preencher com “SIM” (1)/”NÂO” (0).

Integrar campo no Linx (print abaixo) conforme [momento 2](https://docs.google.com/presentation/d/1Hh_OST_nNwxO5icSFv6H42sIwEQE8guD/edit?slide=id.g1eb4c93ba73_0_159#slide=id.g1eb4c93ba73_0_159). |
|  | Criar card com o Flag ATIVO | 0h Ops | Campo custom/varia_preco_cor com valor padrão “SIM”. |
|  | Somente pessoas com PERFIL PLANEJAMENTO COMERCIAL-NV podem interagir com o campo. | 0,5h Ops | Configurar acesso ao novo campo apenas para o perfil “NV - Planejamento Comercial”. |
|  | Integrar preços nas DUAS tabelas | 4h Tech | Replicar os preços do produto para cada variante. Integrar os preços CA,CT,C0,V,VE,VO,AF nas duas tabelas: PRODUTOS_PRECOS e PRODUTOS_PRECO_COR.  |

- Print Linx
    
    ![image.png](NV%20RFI%20Escopo%20-%20Altera%C3%A7%C3%A3o%20Integra%C3%A7%C3%A3o%20(flag%20varia%20p/image.png)