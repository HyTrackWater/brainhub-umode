# NV | RFI : Escopo - Otimização dos dados da API

ID: 106
Responsável pela RFI: Marina Santoro
Status: RFI Em Andamento
Resumo Assunto: Otimização de atualização dos dados da API
Criado em: 7 de maio de 2026 16:54
Data Liberação RFI: 7 de maio de 2026
Demanda relacionada: NV
Horas Estimadas: 8
Valor Calculado: R$ 2.400,00
👥 Clientes: NV (https://app.notion.com/p/NV-c03ae4eca8ff4260a889b660803b4e26?pvs=21)
🤿 Demandas de Clientes: 1 - Otimização de atualização dos dados da API (https://app.notion.com/p/1-Otimiza-o-de-atualiza-o-dos-dados-da-API-352b1d38e76880ea99f5c7ca82a0b77f?pvs=21)
criado por: Marina Santoro
Key Account: Fernanda

<aside>
💡

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

## Contexto

**OBJETIVO**: Melhoria na latência da atualização da API para que Dashboards internos obtenham a performance desejada

Atualmente a latência está em desacordo com o que foi proposto no escopo de solicitação, para buscar um tempo de latência que entendemos como ideal, resolvemos solicitar a exclusão de dataclass para agilizar esse processo.  Lembrando que o acordado foi que a latência da API seria de no máximo 2h, porém hoje ela demora  3h30 entre o inicio da atualização e o término dela o que impacta diretamente no fluxo de dados NV.

Com a redução, otimização e clusterização da API visamos principalmente reduzir a
latência da atualização da API que hoje está quase em 3h entre o inicio da atualização
do DataClass 1 e o final do DataClass 11.

**EXPECTATIVA FINAL**: O Projeto será dado como concluído com êxito se o tempo de
atualização da API for menor ou igual a 1 Hora por Cluster e nos horários que coincidir
2 cluster deve ser no máximo de 2 Horas a atualização total.

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| 1 – Movimentação de Campos entre os DataClass | 1.1 Levar os Campos abaixo presentes no DataClass 11 para o DataClass 1:

 INTEGRACAO LINX ERRO
 LIBERADO PARA INTEGRACAO
 ULTIMA RESPOSTA DA INTEGRACAO DO LINX
 PRECOS DE VENDA VALIDADOS
 CUSTOS VALIDADOS
 DESCRICAO ECOMMERCE
 TEM CABIDE
 TEM ZIPER
 TEM FORRO
 PRODUTO BICOLOR
 FAIXA DE PRECO
 TEM ACESSORIO
 PRODUTO DELICADO
 BENEFICIAMENTO
 SHAPE

1.2 Levar o Campo “Fase Atacado” presente no DataClass 10 para o DataClass 1. | 2h |  |
| 2 – Exclusão de DataClass, excluir os DataClass conforme tabela abaixo | [2 – Exclusão de DataClass, excluir os DataClass conforme tabela abaixo](NV%20RFI%20Escopo%20-%20Otimiza%C3%A7%C3%A3o%20dos%20dados%20da%20API%20359b1d38e76880ee9cfdd6851042aa46.md)  | 2h |  |
| 3 – Otimização dos DataClass mantidos | Hoje finalizamos a atualização do 1° Lote da API próximo do 12H dia, ficando
inconcebível essa operação, segue abaixo as latências que deveram ser otimizadas
entre os dataclass mantidos.

[3 – Otimização dos DataClass mantidos](NV%20RFI%20Escopo%20-%20Otimiza%C3%A7%C3%A3o%20dos%20dados%20da%20API%20359b1d38e76880ee9cfdd6851042aa46.md)  | 2h | Verificar possibilidade do ajuste do horário |
| 4 – Clusterizar e Aumento da Frequência de Atualização por Cluster | Vamos dividir a API em 2 Cluster, para aumentar a frequência de atualização do
cluster principal

 Cluster 1 PRINCIPAL : DataClass 7 , 6 e 1 – Realizar 8 atualizações por dia:
6:30 - 8:30 - 10:30 - 12:30 - 14:30 - 16:30 - 18:30 - 20:30

 Cluster 2 APOIO: DataClas 2 e 3 – Manter o atual padrão de 3x por dia nos
horários já realizados. | 2h | Se tiver algum impacto em custos de processamento, incluir aqui também

Verificar se com as alterações no dataClass 1 os tempos continuarão sendo possíveis

Tempos:
- Data class 1 aproximadamente 8 min
- Data class 6 aproximadamente 33 min
- Data class 7 aproximadamente 52 min
Total: 1h33 min |

### 2 – Exclusão de DataClass, excluir os DataClass conforme tabela abaixo

| dataClass | mainTheme | flag |
| --- | --- | --- |
| 1 | produto | Manter |
| 2 | aviamentos | Manter |
| 3 | materia prima | Manter |
| 4 | aprovações | Excluir |
| 5 | programacao | Excluir |
| 6 | aprovacoes - checklists | Manter |
| 7 | aprovacoes - atelie | Manter |
| 8 | descontinuada | Excluir |
| 9 | aprovações - customData | Excluir |
| 10 | variante - customData | Realizar a movimentação pedida e excluir |
| 11 | produto - customData | Realizar a movimentação pedida e excluir |

### 3 – Otimização dos DataClass mantidos

| dataclass | tipo | horário lote 1 | horário lote 2 |
| --- | --- | --- | --- |
| 3 | final | 09:52 | 15:52 |
| 6 | início | 09:54 | 15:54 |
| 6 | final | 10:24 | 16:29 |
| 7 | início | 10:26 | 16:30 |
| 7 | final | 11:14 | 17:19 |