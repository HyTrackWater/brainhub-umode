# Folha de Escopo

Status Execução: Finalizada
Status Aprovação: Alterada
Aprovado por: Marina Santoro, Ju Ferré
Data Aprovação: 05/01/2026
Nome do relatório: Relatório de Gestão de Tarefas
Tipo de Relatório: Standard
Versão: 1
Visualização do relatório: ../../NV%20RFI%20Escopo%20-%20Relat%C3%B3rio%20de%20Tarefas/Relatrios_Tarefas_(3).jpg

**🟦 Parte 1 — Objetivo e Escopo**

✅ Está no Escopo

- Apresentar os resultados dos registros de tarefas e sua distribuição entre usuários, perfis de usuários e tipos de tarefas;
- Disponibilizar campos de filtros para facilitar a análise dos resultados do relatório;
- Consumo dos dados brutos através de API desenvolvida e configurada pela *uMode*;
- Exportar os resultados de cada seção construída do relatório em formato csv;

❌ Não Está no Escopo

- Realizar higienizações de dados de acordo com falhas de inserção de informações na plataforma;
- Contabilizar as tarefas considerando os usuários que criaram ou que completaram a tarefa - a contabilização é feita de acordo com os usuários atribuídos às tarefas;
- Alterações de *layout* do relatório padrão;
- Aplicação de regras específicas em razão das configurações da contas do parceiro;
- Ações diretamente nas tarefas - as ações são possíveis somente na plataforma da uFlow.

---

**🟦 Parte 2 — Estrutura Geral do Relatório**

Objetivo: definir granularidade e detalhamento de elementos básicos do relatório.

**Granularidade do relatório**:

- [ ]  Por produtos
- [ ]  Por variante de materiais

- [ ]  Por variantes
- [x]  Por tarefas

- [ ]  Por produtos e variantes
- [x]  Por usuários

- [ ]  Por tecidos
- [x]  Composto

- [ ]  Por aviamentos

<aside>

*Observação:*

- O relatório será construído com base nas tarefas atribuídas aos usuários. Podemos ter mais de um usuário por tarefa;
- Para puxar o campo de filtro ‘Coleção’ será necessário criar o relacionamento entre a tarefa e a coleção à qual ela pertence (ou produtos ou aprovações);
</aside>

[Elementos básicos de relatórios](Folha%20de%20Escopo/Elementos%20b%C3%A1sicos%20de%20relat%C3%B3rios%202ffb1d38e76881159dccfa4487ae4d3c.csv)

---

**🟦 Parte 3 — Seções de resultados do Relatório**

Departamento responsável: Operação;

[Bloco](Folha%20de%20Escopo/Bloco%202ffb1d38e76881cdbff0d94487febf72.csv)

---

**🟦** **Parte 4 — Mapeamento Inicial de Campos (Viabilidade)**

Departamento responsável: Operação e Tech;

[Campos e Nomenclaturas](Folha%20de%20Escopo/Campos%20e%20Nomenclaturas%202ffb1d38e768818f89f0fb0a14721844.csv)

---

🏁 **Parte 5 — *Checklist* final**

- Todos os requisitos abaixo devem ser preenchidos para aprovação da viabilidade do relatório;
    - [x]  O escopo e o não escopo foram bem definidos;
    - [x]  A granularidade e grandezas do relatório que devem ser calculadas estão bem definidas;
    - [x]  Os campos de filtro foram nomeados e o funcionamento no relatório está claro;
    - [x]  As premissas estão claras para o desenvolvimento;
    - [x]  As seções do relatório, em sua totalidade, foram detalhadas de modo que contribuem com o objetivo do relatório;
    - [x]  Todos os campos foram mapeados para o desenvolvimento;