# Cambos | RFI: Escopo - Integração Instantânea

ID: 96
Responsável pela RFI: Marina Santoro
Status: RFI Liberada para Comercial negociar com Cliente
Resumo Assunto: Integração de leitura e escrita conforme demanda
Criado em: 23 de abril de 2026 14:58
Data Liberação RFI: 23 de abril de 2026
Demanda relacionada: Cambos
Horas Estimadas: 40
Valor Calculado: R$ 12.000,00
Valor Negociado com Cliente: 3.6-12k
👥 Clientes: Cambos (https://app.notion.com/p/Cambos-d6d48327e33b4105b67b9db4dbb55af1?pvs=21)
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
| Integração de escrita | Usam o botão de forçar o produto para garantir que os dados sejam replicados para o SPI (sistema usado da produção) o quanto antes. 
O objetivo é garantir que os dados estejam nas mãos do time da fábrica assim que tiverem atualização. |   1) 4h
  2) 32h
  3)  4h
 |   1) Mantém integração pelo botão: Nós precisamos tirar a “deduplicação” da AWS. Assim o mesmo produto pode ser integrado em intervalo curto de tempo. 
Definir com cliente se mantém fluxo de 30 minutos. E rever validação que é ignorada pelo botão de forçar.

2) Se for sem o botão, integrar a cada alteração do produto requer uma chamada a cada item alterado dentro do produto. Isso aumenta expressivamente o volume de requisições e consequentemente os valores.

3) Diminuir o intervalo de integração só que também diminui a quantidade de produtos por lote. |
| Integração de leitura | Assim que cadastrar no SPI tem que aparecer na uFlow. Se ela cadastrou na hora no SPI é porque precisa usar de bate pronto na ficha do produto. | 8h | Opção: Eles desenvolverem para chamar nossa integração a cada criação ou edição.
Nós precisaremos criar uma nova rota para cada leitura das chamadas. |