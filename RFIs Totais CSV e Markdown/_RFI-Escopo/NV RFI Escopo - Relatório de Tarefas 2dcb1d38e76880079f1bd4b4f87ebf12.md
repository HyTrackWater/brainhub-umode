# NV | RFI : Escopo - Relatório de Tarefas

ID: 78
Responsável pela RFI: Marina Santoro
Status: RFI Entregue ao Cliente
Resumo Assunto: Relatório de Tarefas (Padrão)
Criado em: 2 de janeiro de 2026 15:11
Data Aceite do Cliente: 5 de dezembro de 2025
Data Liberação RFI: 2 de janeiro de 2026
Demanda relacionada: NV
Horas Estimadas: 52
Valor Calculado: R$ 15.600,00
Cobrada?: 💰
Cobrado: Sim
👥 Clientes: NV (https://app.notion.com/p/NV-c03ae4eca8ff4260a889b660803b4e26?pvs=21)
🤿 Demandas de Clientes: 📄 Relatório Gestão de Tarefas (https://app.notion.com/p/Relat-rio-Gest-o-de-Tarefas-276b1d38e7688037b2e8e6612aad9d60?pvs=21)
Task (Linear): -
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
| Layout | Seguir layout conforme aprovado com cliente, [Miro](https://miro.com/app/board/uXjVICB9eJw=/).  |  |  |
| Filtros | - Usuário da Tarefa
- Período de Criação da Tarefa
- Período de Conclusão da Tarefa
- Status da Tarefa
- Coleção do Produto |  | Usuário da Tarefa: Listar usuários e perfis como é hoje dentro de tarefas |
| Gráficos de barra dupla  comparativa | Quantidade total separada por concluído e pendente:
- Tipo de Tarefa
- Responsável

Quantidade total separada por no prazo e atrasado:
- Tipo de Tarefa
- Responsável |  |  |
| Gráficos de barra simples | Dias corridos da data prazo e a data de conclusão. **Somente tarefas concluídas!**
- Tipo de Tarefa
- Responsável |  |  |
| Tabelas | - Top 10 Tarefas Atrasadas
- Top  Tarefas Atrasadas **por** Usuário/Perfil de Usuario

**Colunas da tabela:**
- Tipo de Tarefa
- Responsável
- Título
- Data de Criação
- Prazo (data da tarefa)
- Dias em Atraso (🧮 data atual **menos** data da tarefa)  |  |  |
- **Mapeamento de Campos**
    
    
    | Banco | Tabela | Exemplo | Nomenclatura | Tipo do Dado | Estrutura |
    | --- | --- | --- | --- | --- | --- |
    | id | jumper_tasks | 94601 |  | Nativo | URL da Tarefa |
    | title | jumper_tasks | ALTERAÇÃO DE MATERIAIS | Título | Nativo | Aba “Tarefa” |
    | description | jumper_tasks | <div>&nbsp;Preciso de algumas[...] </div> | Descrição | Nativo | Aba “Tarefa” |
    | status | jumper_tasks | done | Status da Tarefa | Nativo |  |
    | deadline | jumper_tasks | 2024-10-10 03:00:00 | Prazo | Nativo | Aba “Tarefa”, “Nova Tarefa” |
    | created_at | jumper_tasks | 2024-10-09 13:17:07 | Criado em | Nativo | Aba “Tarefa” |
    | updated_at | jumper_tasks | 2024-10-11 18:15:25 | Atualizado em | Nativo |  |
    | entity_id | jumper_tasks | 3357 | ID Conta Cliente | Nativo |  |
    | deleted_at | jumper_tasks |  | Deletado em | Nativo |  |
    | time | jumper_tasks | 20:00:00 | Horário | Nativo | Aba “Tarefa”, “Nova Tarefa” |
    | created_by_id | jumper_tasks | 4861 | Criado por | Nativo | Aba “Tarefa” |
    | completed_by_id | jumper_tasks | 4262 | Finalizado por | Nativo | Aba “Tarefa” |
    | completed_at | jumper_tasks | 2024-10-11 18:15:06 | Finalizado em | Nativo | Aba “Tarefa”, “Tarefa Concluída” |
    | task_type_id | jumper_tasks **&** jumper_task_types | 9990 **&** Alteração de Material | Tipo de Tarefa | Nativo | Menu “Cadastro”. Aba “Tipo de Tarefa” |
    | duration | jumper_tasks |  |  | Nativo |  |
    |  |  |  | Usuários e/ou Perfis de Usuarios | Nativo | Aba “Tarefa” |
    | record_type | jumper_task_relantionships | ProductDatasheet | Relacionamento da Tarefa com Produtos | Nativo | Aba “Tarefa” |
    | record_type | jumper_task_relantionships | ProductApproval | Relacionamento da Tarefa com Aprovações | Nativo | Aba “Tarefa” |
    |  |  |  | Comentários da Tarefa | Nativo | Aba “Tarefa” |

---

# De Acordo

**Responsável pelo Escopo uMode**

> 
> 

**Responsável pelo Escopo Cliente**

> Beatriz Brant
> 

**Aprovado Em** 

**Aprovado Em**

05/12/2025

---

# Documentações de testes

[Etapa 1](NV%20RFI%20Escopo%20-%20Relat%C3%B3rio%20de%20Tarefas/Etapa%201%202efb1d38e76880eda2dfce2af53d0a86.csv)

[Etapa 2](NV%20RFI%20Escopo%20-%20Relat%C3%B3rio%20de%20Tarefas/Etapa%202%202efb1d38e76880de9f15dca939645b64.csv)