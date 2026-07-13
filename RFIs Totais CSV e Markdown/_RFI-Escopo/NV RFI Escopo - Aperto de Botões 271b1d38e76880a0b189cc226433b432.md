# NV | RFI : Escopo - Aperto de Botões

ID: 18
Responsável pela RFI: Marina Santoro
Status: RFI Q&A Negócios
Resumo Assunto: Aperto de botões
Criado em: 17 de setembro de 2025 15:15
Data Liberação RFI: 8 de dezembro de 2025
Demanda relacionada: NV
Horas Estimadas: 24
Valor Calculado: R$ 7.200,00
Valor Negociado com Cliente: R$ 3.816
👥 Clientes: NV (https://app.notion.com/p/NV-c03ae4eca8ff4260a889b660803b4e26?pvs=21)
🤿 Demandas de Clientes: Integração - Aperto "botão” Linx - Escopo 2025 (https://app.notion.com/p/Integra-o-Aperto-bot-o-Linx-Escopo-2025-2b0b1d38e768802897b0c504e0ca554c?pvs=21)
Task (Linear): https://linear.app/umode/project/nv-integracao-de-escrita-3c68afaa6768
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
| Integração de Escrita | Quando a aba de Materiais do Produto tiver seu status alterado para FINALIZADO, devemos preencher na tabela ANM_TB_BLOQ_FICHA_TECNICA_PA os campos:

**Mostruário:**
Finalizar Mostruário:
update anm_tb_bloq_ficha_tecnica_pa set FT_MOST_PRONTO=1,bt_ft_most_pronto=0, data_final_most=CONVERT(VARCHAR(10),getdate(),112) where produto=?v_produtos_00.produto
Liberar Mostruário:
update anm_tb_bloq_ficha_tecnica_pa set ft_most_pronto = 0 where produto = ?v_produtos_00.produto

**Panos**:
Finalizar Panos:
update anm_tb_bloq_ficha_tecnica_pa set finaliza_panos=1, bt_finaliza_panos = 0, data_final_panos=CONVERT(VARCHAR(10),getdate(),112) where produto=?v_produtos_00.produto
Liberar Panos:
update anm_tb_bloq_ficha_tecnica_pa set finaliza_panos = 0 where produto = ?v_produtos_00.produto

**Aviamentos**:
Finalizar Aviamentos:
update anm_tb_bloq_ficha_tecnica_pa set finaliza_aviamentos=1,bt_finaliza_aviamentos=0, data_final_av=CONVERT(VARCHAR(10),getdate(),112) where produto=?v_produtos_00.produto
Liberar Aviamentos:
update anm_tb_bloq_ficha_tecnica_pa set finaliza_aviamentos = 0 where produto = ?v_produtos_00.produto | 24h | @Marina Santoro vale inserir em 2025 |

- **Complemento - Imagens e Anexos**
    
    ![image.png](NV%20RFI%20Escopo%20-%20Aperto%20de%20Bot%C3%B5es/image.png)
    
    | PRODUTO | DATA_FINAL_MOST | DATA_FINAL_PANOS | DATA_FINAL_AV | FT_MOST_PRONTO | FINALIZA_PANOS | FINALIZA_AVIAMENTOS | BT_FT_MOST_PRONTO | BT_FINALIZA_PANOS | BT_FINALIZA_AVIAMENTOS |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | NV00009 | 2024-03-08T00:00:00.000Z | 2024-03-08T00:00:00.000Z | 2024-03-08T00:00:00.000Z | true | true | true | false | false | false |

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