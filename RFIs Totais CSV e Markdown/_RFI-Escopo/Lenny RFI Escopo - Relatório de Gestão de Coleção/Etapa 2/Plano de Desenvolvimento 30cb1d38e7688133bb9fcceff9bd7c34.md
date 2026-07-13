# Plano de Desenvolvimento

Status Execução: Não iniciada
Status Aprovação: Não iniciada
Aprovado por: Vinícius Risoléo
Qtd Endpoints: 3
Versão: 1

**🟦 Parte 1 — Modelagem das consultas**

[Definições das consultas](Plano%20de%20Desenvolvimento/Defini%C3%A7%C3%B5es%20das%20consultas%2030cb1d38e76881c982bfffc771cfbe7a.csv)

**🟦 Parte 2 — Mapeamento dos campos**

[Tabela de Mapeamento de Campos](Plano%20de%20Desenvolvimento/Tabela%20de%20Mapeamento%20de%20Campos%2030cb1d38e7688146877bd04e2cbc637e.csv)

---

**🟦 Parte 3 — Detalhes de desenvolvimento**

- Funções do desenvolvimento
    
    
    | Nome da função | Módulo de Origem | Módulo de Execução | Descrição da função |
    | --- | --- | --- | --- |
    | _coerce_naive | core.py | core.py | Converte datetime com timezone (aware) para datetime sem timezone (naive), removendo tzinfo, para permitir comparações consistentes no relatório. |
    | _parse_dt | core.py | core.py | Faz o parse “best-effort” de datas vindas de CSV/API (strings em múltiplos formatos) para datetime; retorna None quando vazio/ inválido. |
    | _status_norm | core.py | core.py | Normaliza status para string lower() e sem espaços, evitando inconsistências de comparação. |
    | _sanitize_raw_rows | core.py | service.py | Sanitiza linhas brutas (CSV/API) antes do mapeamento: remove chaves None, garante chaves como string “limpa” (strip) e preserva todas as colunas do cabeçalho. |
    | _safe_lower | core.py | core.py | Converte qualquer valor em string minúscula e “strip”; retorna vazio em None ou falha de conversão. |
    | _safe_unique_count | core.py | service.py | Conta valores únicos normalizados de um campo (key) em uma lista/iterável de dicionários, ignorando linhas inválidas. |
    | _is_empty | core.py | core.py | Detecta se um valor deve ser tratado como vazio (None, string vazia, “none/null/nan”). |
    | _normalize | core.py | core.py | Normaliza um valor para string com opções de case-insensitive e remoção de espaços, para uso em chaves/categorias agregadas. |
    | _to_float | core.py | core.py | Converte valores numéricos (incluindo strings com vírgula decimal) para float; retorna None quando inválido/vazio. |
    | all_selected_from_options | core.py | app.py | Retorna um dicionário onde cada campo de filtro já vem com todas as opções selecionadas (default de UI). |
    | normalize_pending_filters_identity | core.py | app.py | Normalização “no-op” de filtros pendentes: mantém interface estável para evolução futura do mapeamento UI → backend. |
    | add_task_completion_interval | core.py | service.py | Enriquecimento: adiciona taskCompletionInterval (dias em float) para tarefas concluídas (done) como diferença entre taskCompletedAt e taskCreatedAt; caso contrário, None. |
    | add_task_custom_status | core.py | service.py | Enriquecimento: cria taskCustomStatus com 4 rótulos (pendente/concluída × no prazo/atrasada), comparando now vs deadline (backlog) ou completed_at vs deadline (done). |
    | add_task_deadline_filling | core.py | service.py | Enriquecimento: cria taskDeadlineFilling = 1 quando há deadline parseável, senão 0. |
    | add_task_days_late | core.py | service.py | Enriquecimento: cria taskDaysLate (inteiro) apenas quando taskCustomStatus indica “Pendente | Atrasada”, usando (now - deadline) em dias (floor, nunca negativo). |
    | chart_tasks_unique_count_two_series | core.py | service.py | Gera payload estável de gráfico (2 séries) contando tarefas únicas por categoria (default taskTypeName), separando done vs backlog, com ordenação e totais globais. |
    | chart_avg_numeric_by_category | core.py | service.py | Gera payload de gráfico (1 série) calculando média de um campo numérico por categoria, com contagens por categoria e resumo “overall”. |
    | chart_unique_count_two_series | core.py | service.py | Gera payload de gráfico (2 séries) com contagem única de id_field por category_field, para quaisquer dois subconjuntos (A e B) com rótulos configuráveis. |
    | build_overdue_open_tasks_list | core.py | service.py | Monta lista do Block 7: filtra tarefas abertas e atrasadas, explode múltiplos responsáveis em múltiplas linhas, remove duplicatas por (taskId + assignedToKey) e ordena por atraso/prazo/ criação. |
    | build_assigned_entity_directory | core.py | service.py | Constrói um “diretório” de responsáveis (User/Policy) indexado por recordIdAssigned, consolidando nome/email e mantendo o primeiro tipo observado (evita conflitos). |
    | add_assigned_to_key | core.py | service.py | Enriquecimento: cria assignedToKey (string de display para filtros/gráficos) a partir do diretório (user: “Nome ”; policy: “Nome (Política)”; fallback quando ausente). |
    | build_overdue_open_tasks_by_assignee | core.py | service.py | Monta objeto do Block 8 (tabela aninhada): agrega por responsável (assignedToKey), calcula qty_overdue (tarefas únicas) e avg_days_late, e cria children (tarefas) ordenadas por atraso. |
    | _detect_charset_from_content_type | core.py | core.py | Extrai charset do header Content-Type (ex.: text/csv; charset=utf-8) para apoiar decodificação robusta do CSV. |
    | _decode_csv_bytes | core.py | core.py | Decodifica bytes de CSV com estratégia robusta (prioriza utf-8-sig/utf-8, tenta charset declarado, depois cp1252/latin-1; fallback final com replace). |
    | _load_rows_from_api_csv | core.py | service.py | Carrega linhas de CSV via API (/reports-embedded/csv/...), com suporte a dois formatos de URL, cache-bust opcional, delimiter configurável e sanitização de decodificação. |
    | make_task_datasets | core.py | service.py | Constrói datasets padronizados (base e filtrados) para o relatório: gross, backlog, done, overdue/on-time, missing deadline, done late/on-time, aplicando predicados e filtros selecionados. |
    | _ensure_int | core.py | core.py | Converte valor para int com fallback padrão; helper utilitário usado em rotinas de frontend. |
    | slice_series_payload | core.py | app.py | Aplica paginação (slice) em payloads de séries (categories + series.values), retornando um payload reduzido para renderização no frontend. |
    | series_payload_to_csv | core.py | app.py | Converte payload de séries agrupadas em bytes CSV (UTF-8 com BOM), com coluna “categoria” e colunas por série. |
    | slice_avg_payload | core.py | app.py | Aplica paginação (slice) em payloads de média (categories/values/counts), para renderização em blocos com muitos itens. |
    | avg_payload_to_csv | core.py | app.py | Exporta payload de médias para CSV (UTF-8 com BOM), com colunas configuráveis e opção de incluir linha “GERAL” (overall). |
    | _get_series_values_by_label | core.py | core.py | Localiza uma série cujo name contém um rótulo (case-insensitive) e retorna seus valores coeridos para int; usado para compor visões “No prazo” vs “Atrasada”. |
    | build_on_time_vs_late_payload | core.py | app.py | Combina dois payloads (done e backlog) e monta um payload consolidado (2 séries) para a visão escolhida (“No prazo” ou “Atrasada”), alinhando categorias por união. |
    | table_rows_to_csv_bytes | core.py | app.py | Exporta uma lista de dicionários (linhas de tabela) para CSV bytes (headers a partir da 1ª linha), com encoding e delimitador configuráveis. |
- Blocos
    
    
    | Índice | Bloco | *Dataset* (negócios) | *Dataset* (desenvolvimento) | Funções usadas | Nome do(s) objeto(s) - Cálculos | Tipo de objeto |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 | Tipo de Tarefa | Quantidade | Tarefas 'finalizadas' e tarefas 'backlog' | data_done + data_backlog | chart_tasks_unique_count_two_series, slice_series_payload, series_payload_to_csv | dictTasksByTypeQty | json |
    | 2 | Responsável | Quantidade | Tarefas 'finalizadas' e tarefas 'backlog' | data_done_user + data_backlog_user | chart_tasks_unique_count_two_series, slice_series_payload, series_payload_to_csv | dictTasksByUserQty | json |
    | 3 | Tipo de Tarefa | Média para finalização | Tarefas 'finalizadas' | data_done_for_avg_type | chart_avg_numeric_by_category, slice_avg_payload, avg_payload_to_csv | dictAvgCompletionByType | json |
    | 4 | Responsável | Média para finalização | Tarefas 'finalizadas' | data_done_for_avg_user | chart_avg_numeric_by_category, slice_avg_payload, avg_payload_to_csv | dictAvgCompletionByUser | json |
    | 5 | Tipo de Tarefa | No prazo vs Atrasada (Concluídas x Pendentes) | Tarefas finalizadas dentro do prazo,Tarefas finalizadas depois do prazo,Tarefas abertas no prazo,Tarefas abertas e fora do prazo | done_on_time_type + done_late_type + backlog_on_time_type + backlog_overdue_type | chart_unique_count_two_series, build_on_time_vs_late_payload, slice_series_payload, series_payload_to_csv | dictDoneOnTimeVsLateByType,
    dictBacklogOnTimeVsOverdueByType | json |
    | 6 | Responsável | No prazo vs Atrasada (Concluídas x Pendentes) | Tarefas finalizadas dentro do prazo,Tarefas finalizadas depois do prazo,Tarefas abertas no prazo,Tarefas abertas e fora do prazo | done_on_time_user + done_late_user + backlog_on_time_user + backlog_overdue_user | chart_unique_count_two_series, build_on_time_vs_late_payload, slice_series_payload, series_payload_to_csv | dictDoneOnTimeVsLateByUser,
    dictBacklogOnTimeVsOverdueByUser | json |
    | 7 | Listagem de tarefas abertas em atraso | Tarefas 'backlog' e atrasadas | data_overdue_open | build_overdue_open_tasks_list, table_rows_to_csv_bytes | listOverdueOpenTasks | json |
    | 8 | Tarefas abertas em atraso por responsável | Tarefas 'backlog' e atrasadas | data_overdue_open | build_overdue_open_tasks_by_assignee | tableOverdueOpenTasksByAssignee | json |

**🟦 Parte 4 — Conclusão da etapa**

- [x]  O mapeamento dos campos foi feito com a mesma listagem de campos definida na Etapa 1;
- [x]  As funções usadas no desenvolvimento foram listadas em ‘Funções’;
- [x]  Foram definidas as funções e os *datasets* usados para cada bloco do relatório;
- [x]  A(s) consulta(s) estão padronizadas e aprovadas, podendo dar sequência à configuração da API;