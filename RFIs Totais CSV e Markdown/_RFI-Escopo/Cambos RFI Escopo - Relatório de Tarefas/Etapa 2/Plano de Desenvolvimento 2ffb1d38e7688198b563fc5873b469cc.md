# Plano de Desenvolvimento

Status Execução: Finalizada
Status Aprovação: Aprovada
Aprovado por: Vinícius Risoléo
Qtd Endpoints: 1
Versão: 2

Impacto em horas de desenvolvimento: 24h;

**🟦 Parte 3 — Detalhes de desenvolvimento**

- Blocos
    
    
    | Índice | Bloco | *Dataset* (negócios) | *Dataset* (desenvolvimento) | Funções usadas | Nome do(s) objeto(s) - Cálculos | Tipo de objeto |
    | --- | --- | --- | --- | --- | --- | --- |
    | 5 | Tarefas no prazo vs atrasadas - Tipo de Tarefa | Concluídas | Tarefas finalizadas dentro do prazo,Tarefas finalizadas depois do prazo,Tarefas abertas no prazo,Tarefas abertas e fora do prazo | done_on_time_type + done_late_type | chart_unique_count_two_series, build_on_time_vs_late_payload, slice_series_payload, series_payload_to_csv | dictDoneOnTimeVsLateByType, | json |
    | 6 | Tarefas no prazo vs atrasadas - Tipo de Tarefa | Pendentes | Tarefas finalizadas dentro do prazo,Tarefas finalizadas depois do prazo,Tarefas abertas no prazo,Tarefas abertas e fora do prazo | backlog_on_time_user + backlog_overdue_user | chart_unique_count_two_series, build_on_time_vs_late_payload, slice_series_payload, series_payload_to_csv | dictBacklogOnTimeVsOverdueByUser | json |