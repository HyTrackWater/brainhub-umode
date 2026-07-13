# Puket | RFI : Escopo - Campos E-com

ID: 48
Responsável pela RFI: Julianne Rodrigues
Status: RFI Post Mortem
Resumo Assunto: Campos Ecommerce e Integração
Criado em: 19 de janeiro de 2026 13:51
Data Liberação RFI: 24 de abril de 2026
Demanda relacionada: Puket
Horas Estimadas: 8
Valor Calculado: R$ 2.400,00
👥 Clientes: Puket (https://app.notion.com/p/Puket-aae6d54c5f854cc9b890f8c0c120bf0a?pvs=21)
🤿 Demandas de Clientes: Criar campos obrigatórios ecommerce + validação + integração  (https://app.notion.com/p/Criar-campos-obrigat-rios-ecommerce-valida-o-integra-o-2e2b1d38e76880e29943e661ca43b9c6?pvs=21)
Task (Linear): https://cxhub.umode.tech/demands/f2839f59-184e-4a3a-9ec8-6e39ddc5e8aa
criado por: Ju Ferré
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
| Criar 8 campos na tabela tabela [dbo].[IMB_ECOMMERCE_PRODUTO] | [FRASE_INICIAL] [varchar] (30) NULL,
[PAIS_ORIGEM] [varchar] (50) NULL,
[LAVAGEM] [varchar] (100) NULL,[ALVEJAMENTO] [varchar] (100) NULL,[SECAGEM_NATURAL] [varchar](100) NULL,
[PASSADORIA] [varchar](100) NULL,[LIMPEZA_A_SECO] [varchar](100) NULL,**[INFORMACAO_ADICIONAL] [text] NULL**,
[SECAGEM] [varchar](100) NULL, | 4h Tech + 4h Ops |  |
| Criar o campo DESCRICAO da tabela **IMB_ECOMMERCE_INF_ADICIONAL**, podendo ser inserido mais de uma informação | Opções:
Lavar antes de usar
Lavar bojo separadamente
Lavar com cores similares
Lavar com peças de cor semelhante
Lavar delicadamente
Lavar pelo avesso
Lavar separadamente
Lavar separadamente ou com cores semelhantes
Limpar com pano úmido
Não armazenar a peça em cabide
Não centrifugar
Não centrifugar ou torcer
Não deixar de molho

O campo no sql é um campo texto, deverá ser gravado como texto com quebras de linhas.
Pode usar como exemplo o campo ESPEC_TECNICA da tabela IMB_ECOMMERCE_PRODUTO, pois vcs já fazem a gravação de dados neste campo e seguirá o mesmo padrão. |  |  |

| Tabela | Campo | Tipo | Limite de caracteres | Campo custom | Observação |
| --- | --- | --- | --- | --- | --- |
| [IMB_ECOMMERCE_PRODUTO] | [FRASE_INICIAL] | varchar | 30 | frase_inicial |  |
| [IMB_ECOMMERCE_PRODUTO] | [PAIS_ORIGEM]  | varchar | 50 | pais |  |
| [IMB_ECOMMERCE_PRODUTO] | [LAVAGEM]  | varchar | 100 | lavagem |  |
| [IMB_ECOMMERCE_PRODUTO] | [ALVEJAMENTO]    | varchar | 100 | alvejamento |  |
| [IMB_ECOMMERCE_PRODUTO] | [SECAGEM_NATURAL]  | varchar | 100 | secagem_natural |  |
| [IMB_ECOMMERCE_PRODUTO] | [PASSADORIA]  | varchar | 100 | passadoria |  |
| [IMB_ECOMMERCE_PRODUTO] | [LIMPEZA_A_SECO]  | varchar | 100 | limpeza_seco |  |
| [IMB_ECOMMERCE_PRODUTO] | [SECAGEM]   | varchar | 100 | secagem |  |
| [IMB_ECOMMERCE_PRODUTO] | **[INFORMACAO_ADICIONAL]** | text |  | informacoes_adicionais  informacoes_adicionais2  informacoes_adicionais3 informacoes_adicionais4  informacoes_adicionais5  informacoes_adicionais6 informacoes_adicionais7 informacoes_adicionais8 informacoes_adicionais9  informacoes_adicionais10 informacoes_adicionais11 informacoes_adicionais12 informacoes_adicionais13 | O campo **[INFORMACAO_ADICIONAL]** é preechido o campo DESCRICAO da tabela **IMB_ECOMMERCE_INF_ADICIONAL**, podendo ser inserido mais de uma informação. |
|  |  |  |  |  |  |

![image.png](Puket%20RFI%20Escopo%20-%20Campos%20E-com/image.png)

---

# De Acordo

**Responsável pelo Escopo uMode**

> Juliana Ferré
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

**Aprovado Em**