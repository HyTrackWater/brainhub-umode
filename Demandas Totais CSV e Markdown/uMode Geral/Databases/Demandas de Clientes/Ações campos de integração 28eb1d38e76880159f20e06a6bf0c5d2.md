# Ações campos de integração

ID: UMD-676
: Concluída
Etapa: Demanda Concluída
Responsabilidade: Demanda com uMode
Tipo de Demanda: Integração
Quem solicitou?: Marina
👥 Clientes: Lofty Style (https://app.notion.com/p/Lofty-Style-293c8829d81c44d9ab8360ae66d24aab?pvs=21)
Key Account/Responsável: Marina Santoro
Área Responsável: OPERAÇÃO
Criado em: 16 de outubro de 2025 10:21
Última edição: 3 de fevereiro de 2026 14:07

Descrever todas as ações de campos q precisam ser limpos por cliente:

### Validação

- [x]  Ação para acionar a validação de integração

### Limpeza de Campos

- [x]  Limpar last_integration quando alterar o produto
- [x]  Limpar linx_integration_error quando alterar o produto

### Limpeza de Campos na Duplicação de Produto

- [x]  Limpar gatilho de integração, campo custom/liberado_integracao

### Bloqueio

- [x]  Campos grupo (product_type) e subgrupo (custom/subgrupo) não podem ser alterados após integração gerar a referência do produto. Isso porque os ids dos campos são usados para criar o produto e depois de criado, não pode ser alterado