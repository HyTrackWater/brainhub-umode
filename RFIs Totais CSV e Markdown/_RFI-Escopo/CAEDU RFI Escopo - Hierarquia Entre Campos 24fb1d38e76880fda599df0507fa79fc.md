# CAEDU | RFI : Escopo - Hierarquia Entre Campos

ID: 7
Responsável pela RFI: Julianne Rodrigues
Status: RFI Stand By
Resumo Assunto: Hierarquia entre campos
Criado em: 14 de agosto de 2025 10:33
Data Liberação RFI: 11 de agosto de 2025
Demanda relacionada: Caedu
Horas Estimadas: 36
Valor Calculado: R$ 10.800,00
👥 Clientes: Caedu (https://app.notion.com/p/Caedu-275bd52e58df49078f2f3b6dc76a4755?pvs=21)
criado por: Marina Santoro
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
| Mudança da hierarquia das pastas | Alterar a hierarquia das pastas de produto de: DEPARTAMENTO E COLEÇÃO, LINHA, sem uso do terceiro nível; para: **DEPARTAMENTO, COLEÇÃO e LINHA.** 
Precisa criar as pastas antigas que estão como Griffe “verão 24/25” , dentro da Griffe atual “FEMININO” e as antigas coleções serão o terceiro nível linha.

 |  | Isso requer uma mudança massiva de produtos entre pastas para respeitar a nova hierarquia. E a criação de novas pastas. Mais de 36k produtos. |
| Mudança da hierarquia dos campos  | Time de negócios solicitou alteração de campos para uma nova hierarquia: GRIFE, LINHA e GRUPO>SUBGRUPO.
Time de tecnologia questionou se é possível alterar a hierarquia apenas na uMode sem impactar integração Caedu.

 |  | Não é viável fazer sem impactar integração visto que é necessário alterar campos uMode para garantir a nova hierarquia solicitada pelo time de negócios da Caedu. O campo product_type é GRUPO>SUBGRUPO e pela nova hierarquia deve ser GRIFE. O campo LINHA se mantém, cria-se novo campo para GRUPO>SUBGRUPO. 

De:
UMODE = LINX
custom/griffe  =  griffe
custom/linha  =  linha
product_type  =  grupo + subgrupo

Para:
UMODE = LINX
product_type  =  griffe
custom/linha  =  linha
custom/grupo_subgrupo  =  grupo + subgrupo   

Também será necessário rever ações que usam esses campos para fazer eventuais atualizações.

custom/griffe presente em 5 ações
 custom/linha  presente em 3 ações  |
| ~~Relatório com erros de integração~~ | ~~Habilitar um serviço onde o time Caedu faça o post indicando sucesso ou fracasso da integração com a mensagem de erro.~~ |  | ~~Precisamos aprofundar esta demanda, não temos clareza total sobre o assunto. Seria um projeto separado.~~ |
| ~~Trava da alteração do status~~ | ~~Impedir alteração do status do produto para FINALIZADO quando a validação não estiver 100% validada.~~ | ~~Operação & Manutenção - 4h~~
 | ~~Alinhado com time de tecnologia da Caedu que não é o status FINALIZADO que aciona a integração, mas sim o conjunto de regras que constam na URL da API: 
- Produto deve estar finalizado no PLM
- Produto não pode ter sido deletado no PLM
- Validação "Integração Linx" 100% aprovada
- Campo linx_last_integration deve estar vazio
A validação dos campos obrigatórios roda quando o time altera o status para FINALIZADO.
Não é isso que manda o produto para fila mas sim a combinação de todos os elementos listados acima.~~ |

---

# De Acordo

**Responsável pelo Escopo uMode**

> Marina Gonçalves Santoro
> 

**Responsável pelo Escopo Cliente**

> 
> 

**Aprovado Em** 

11/08/2025

**Aprovado Em**