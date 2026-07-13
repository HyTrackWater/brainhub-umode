# Revisão de Preços e Custos Integração de Escrita

ID: UMD-961
: Concluída
Etapa: Demanda Concluída
Responsabilidade: Demanda com uMode
Tipo de Demanda: Integração
Quem solicitou?: Gustavo e Gabi
Data da Solicitação: 30/01/2026   (BRT)
👥 Clientes: Lofty Style (https://app.notion.com/p/Lofty-Style-293c8829d81c44d9ab8360ae66d24aab?pvs=21)
Key Account/Responsável: Laura Delgado, Andrea Holmer
Área Responsável: TECH
Observações: Demanda com RFI aberta em análise pela JuA e Sandro.
Criado em: 30 de janeiro de 2026 15:14
Última edição: 19 de março de 2026 17:10
RFI: Lofty | RFI: Escopo - Alteração de Regra para Custos de Variante (https://app.notion.com/p/Lofty-RFI-Escopo-Altera-o-de-Regra-para-Custos-de-Variante-2f4b1d38e768803a88fee17137744e8f?pvs=21)

# Regra de integração atual

- Time do PCP preencherá o valor MOB (mão de obra) na plataforma uMode na aba de Fornecedores.
- Não vamos considerar o envio para a aba de OPERAÇÃO EXTRA de Fornecedores que estejam com o Status CANCELADO ou REPROVADO. Todos os demais (PROSPECÇÃO, ORÇAMENTO, PILOTO e PRODUÇÃO), serão enviados.
- Campo que orienta a regra para envio da aba de Operações Extras é o REVENDA.
    - Campo REVENDA preenchido = PA;
    - Campo REVENDA sem preenchimento = Faccionado.

## Preco 99 [por produto = 0; por variante = 1 e custo]

### Tabela produto_preco [por produto]

| **Tabela** | **preco1** | **preco_liquido1** | **Status** |
| --- | --- | --- | --- |
| **00** | 0 | 0 | insert |
| **04** | 0 | 0 | insert |
| **14** | 0 | 0 | insert |
| **99** | 0 | 0 | insert |

### Tabela produto_preco_cor [por produto cor]

| **Tabela** | **preco1** | **preco_liquido1** | **preco_liquido2** | **preco_liquido3** | **preco_liquido4** | **Status** |
| --- | --- | --- | --- | --- | --- | --- |
| **00** | 1 | 1 | 0 | 0 | 0 | insert |
| **04** | 1 | 1 | 0 | 0 | 0 | insert |
| **14** | 1 | 1 | 0 | 0 | 0 | insert |
| **99** | func | func | 0 | 0 | 0 | update |

Flag varia_preco_cor sempre true.

**Faccionado**

TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE

- Se tiver mais de um fornecedor produzindo o produto, tem que fazer o **valor médio**

**PA**

TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE

![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image.png)

![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%201.png)

## Custo 1 [por produto]

**PA**

[PRODUTO] CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE

**Faccionado**

[PRODUTO] CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE

- Se tiver mais de um fornecedor produzindo o produto, tem que fazer o **valor médio**

![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%202.png)

![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%203.png)

## Operações Extras [por produto]

**Faccionado**

[PRODUTO] FICHA TECNICA > OPERAÇÕES > OPERAÇÕES EXTRAS = valor do campo manufacture.price

- **COSTURA [FORNECEDOR]**

![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%204.png)

---

## Testes de integração

- Produto PA
    - 19.10.0005 (16/10/25) 🟢
        
        ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%205.png)
        
        ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%206.png)
        
        ![Imagem do WhatsApp de 2025-10-16 à(s) 17.14.03_21a175b5.jpg](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/Imagem_do_WhatsApp_de_2025-10-16_(s)_17.14.03_21a175b5.jpg)
        
        ![Imagem do WhatsApp de 2025-10-16 à(s) 09.34.29_1916f107.jpg](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/Imagem_do_WhatsApp_de_2025-10-16_(s)_09.34.29_1916f107.jpg)
        
        ![Imagem do WhatsApp de 2025-10-16 à(s) 17.14.36_f83ea5c0.jpg](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/Imagem_do_WhatsApp_de_2025-10-16_(s)_17.14.36_f83ea5c0.jpg)
        
        ![Imagem do WhatsApp de 2025-10-16 à(s) 17.15.37_1da53281.jpg](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/Imagem_do_WhatsApp_de_2025-10-16_(s)_17.15.37_1da53281.jpg)
        
    - 16.00.0002 (20/10/25) 🟢
        
        ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%207.png)
        
        ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%208.png)
        
- Produto Faccionado
    - 04.02.0122 (04/11/25)
        
        ![Imagem do WhatsApp de 2025-11-04 à(s) 11.30.27_2905a45d.jpg](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/Imagem_do_WhatsApp_de_2025-11-04_(s)_11.30.27_2905a45d.jpg)
        
        ![Imagem do WhatsApp de 2025-11-04 à(s) 11.30.49_157a9f53.jpg](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/Imagem_do_WhatsApp_de_2025-11-04_(s)_11.30.49_157a9f53.jpg)
        

## Casos de erro

- Calca Mey 025565
    
    ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%209.png)
    
    ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%2010.png)
    
- Calca Agnes 024340
    
    ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%2011.png)
    
    ![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%2012.png)
    

# Atualização da regra de integração

## Revisão das regras = **CADA COR TEM O SEU CUSTO 99**

- **PA**
    
    **Preco 99**
    
    **POR COR:** TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
    
    **CADA COR TEM O SEU CUSTO 99**
    
    **Custo 1**
    
    **POR PRODUTO:** CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
    
- **Faccionado**
    
    **Preco 99**
    
    **POR COR:** TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
    
    - Se tiver mais de um fornecedor produzindo o produto, tem que fazer o **valor médio**
    
    **Custo 1**
    
    **POR PRODUTO:** CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
    
    - Se tiver mais de um fornecedor produzindo o produto, tem que fazer o **valor médio**
    
    **Operações Extras**
    
    **POR FORNECEDOR:** Valor do campo manufacture.price por fornecedor
    

## Campo varia custo cor

Solicitação do dia 24/11/25, “fizemos uma alteração na forma dos custos dos produtos e precisamos mapear um campo que temos no Linx (varia custo cor) e que hoje não temos na umode”.

**Confirmar com Gabi: varia custo cor pode ser sempre true? SIM**

**o varia preço cor já é sempre true**

## Nova tabela de custos (produto_cores) no campo CUSTO_REPOSICAO1

**CADA COR TEM O SEU CUSTO** 

![ o mesmo preco que vai variando para 99 na produtos_preco_cor](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%2013.png)

 o mesmo preco que vai variando para 99 na produtos_preco_cor

![Deve vim na produto_cores](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%2014.png)

Deve vim na produto_cores

![image.png](Revis%C3%A3o%20de%20Pre%C3%A7os%20e%20Custos%20Integra%C3%A7%C3%A3o%20de%20Escrita/image%2015.png)