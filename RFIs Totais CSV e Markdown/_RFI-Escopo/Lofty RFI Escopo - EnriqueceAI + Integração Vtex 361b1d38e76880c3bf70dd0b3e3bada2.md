# Lofty | RFI: Escopo - EnriqueceAI + Integração Vtex

ID: 110
Responsável pela RFI: Marina Santoro
Status: RFI Pronta para Estimar
Resumo Assunto: Enriquecimento automático de catálogo (SEO + GEO) com validação por agente de IA, em fluxo VTEX → uMode → VTEX, sem intervenção humana no fluxo principal.
Criado em: 15 de maio de 2026 14:19
Data Liberação RFI: 15 de maio de 2026
Demanda relacionada: Lofty Style
Horas Estimadas: 80
Valor Calculado: R$ 24.000,00
Valor Negociado com Cliente: 24k+6.5k
👥 Clientes: Lofty Style (https://app.notion.com/p/Lofty-Style-293c8829d81c44d9ab8360ae66d24aab?pvs=21)
Task (Linear): https://docs.google.com/document/d/1oehld2Ny_JmYFvJthRfg1KOGYIwmEZHu/edit
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
| Leitura de produto na VTEX | uMode consome produtos diretamente da VTEX da Lofty, identificando quais estão pendentes de enriquecimento. Frequência de leitura e gatilho (webhook VTEX, polling ou batch) a definir em projeto. |  | Necessário confirmar com Lofty: (a) o produto já está publicado para o consumidor no momento da leitura ou entra em rascunho/oculto; (b) se há webhook VTEX disponível ou se exigirá polling; (c) qual o identificador canônico utilizado (SKU, EAN, GTIN, RefId). |
| Credencial VTEX para leitura e escrita | Provisionamento de appKey e appToken dedicados, na conta VTEX da Lofty, com permissão mínima necessária para os endpoints de catálogo, mídia e SEO. |  | uMode já possui produto que integra VTEX (leitura/escrita) e domina as regras da plataforma. Owner da credencial do lado Lofty a definir, assim como política de rotação e revogação. |
| Enriquecimento SEO + GEO | Aplicação do motor uMode para gerar/ajustar título, descrição, categoria, tags e demais campos relevantes para SEO e GEO, a partir do conteúdo bruto disponível na VTEX. |  | Mapeamento de campos VTEX vs. campos exigidos pelo enriquecimento a ser detalhado. Limitações de tamanho, formato e encoding por campo a confirmar. |
| Validação por agente de IA | Cada produto enriquecido passa por avaliação de agente de IA que atribui um score de confiança. O score é comparado contra threshold de qualidade e piso mínimo, gerando três caminhos (publica direto / publica com flag / bloqueia). |  | Valores de threshold e piso mínimo serão definidos em conjunto com a Lofty durante a fase de homologação. uMode recomenda calibragem inicial com amostragem manual antes do go-live. |
| Publicação automática e flag de revisão | Produtos com score acima do threshold publicam automaticamente sem flag. Produtos entre piso mínimo e threshold publicam com flag indicando necessidade de ajuste fino posterior. Produtos abaixo do piso ficam bloqueados. |  | Necessário definir: (a) onde a flag fica registrada (campo customizado VTEX, sistema externo uMode, ambos); (b) quem consome a fila de flags (Lofty, uMode, terceiro); (c) SLA de tratamento da fila. |
| Fila de revisão e ajuste fino | Produtos sinalizados (com flag ou bloqueados) entram em fila para revisão e ajuste fino das descrições. Critério de priorização, ferramenta e responsável a definir. |  | uMode pode fornecer interface de revisão ou apenas a fila estruturada. Decisão impacta escopo e horas. A confirmar com Lofty se o ajuste fino é feito pela Lofty, pela uMode ou compartilhado. |
| Logs e auditoria | Registro de todas as decisões do agente de IA (score, faixa, ação tomada, timestamp) para auditoria posterior e calibragem do modelo. |  | Retenção, ferramenta de armazenamento e nível de acesso da Lofty aos logs a definir. Mínimo recomendado: 12 meses. |
| Ambiente de homologação e go-live | Execução do fluxo end-to-end em ambiente VTEX não-produção (sandbox da Lofty) antes do go-live, com calibragem do threshold e piso mínimo do agente de IA via amostragem. |  | Confirmar existência de ambiente sandbox VTEX da Lofty. Definir critério de aceite (volume de amostra, taxa de aceite mínima, prazo de homologação). |
| Volumetria e SLA | Dimensionamento do fluxo conforme volume atual e projetado de produtos do catálogo Lofty. Definição de latência máxima aceitável entre leitura na VTEX e republicação enriquecida. |  | Volume atual de SKUs, taxa de novos/alterados por dia e latência aceitável a ser fornecida pela Lofty. Impacta diretamente a arquitetura (síncrono vs. assíncrono, dimensionamento de fila). |

# **Contexto**

A Lofty contratou a uMode para automatizar o enriquecimento de seu catálogo de produtos na VTEX, utilizando a solução proprietária da uMode de SEO + GEO, com validação por agente de IA antes da republicação.

Por solicitação da Lofty, o fluxo foi ajustado em relação à proposta inicial: a uMode lê o produto diretamente da VTEX (não mais da Synthese), executa o enriquecimento, submete ao agente de IA e devolve o conteúdo enriquecido para a própria VTEX.

# **Regra de operação do agente de IA**

O agente de IA avalia o score de confiança de cada enriquecimento e classifica em três faixas, com piso mínimo a ser definido em tempo de projeto:

| **Faixa de score** | **Ação na VTEX** | **Tratamento posterior** |
| --- | --- | --- |
| Acima do threshold de qualidade | Publica automaticamente | Nenhum — produto considerado pronto |
| Entre piso mínimo e threshold de qualidade | Publica automaticamente + flag de revisão | Entra em fila de ajuste fino para revisão posterior |
| Abaixo do piso mínimo | Bloqueia publicação | Vai para fila de revisão crítica; não publica até intervenção |

*Os valores numéricos do threshold de qualidade e do piso mínimo serão definidos em tempo de projeto, em conjunto com a Lofty, com calibragem durante a fase de homologação.*

# **Itens fora do escopo desta RFI**

- Pricing, modelo comercial e contrato (objeto de tratativa comercial separada).
- LGPD, certificações, criptografia e auditoria de segurança detalhada (fase posterior).
- Reconciliação de catálogo legado e tratamento histórico.
- Estoque e integração com marketplaces (B2W, Mercado Livre, etc.).
- Treinamento, ajuste fino do modelo de IA, dataset proprietário (escopo separado).
- Synthese — saiu do fluxo conforme orientação da Lofty.