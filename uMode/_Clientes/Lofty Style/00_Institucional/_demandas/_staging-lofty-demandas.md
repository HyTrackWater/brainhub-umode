# Lofty Style · Demandas — staging bruto (Notion)

> Arquivo temporário de trabalho — não é o padrão final. Aqui acumulo os dados brutos das
> demandas de Lofty Style no vocabulário original do Notion. A tradução para
> `protocolo-gestao-demanda.md` (natureza, taxonomia CX Hub, marcos etc.) acontece depois,
> quando todas estiverem reunidas. Nada aqui é formalizado ainda.
>
> **Fonte híbrida (decidido em 06 jul 2026):** as 10 primeiras demandas (UMD-209 a UMD-309)
> foram digitadas manualmente pelo Vinicius, campo a campo + narrativa completa. A partir daí,
> os **campos estruturados** das 75 demandas restantes (total 85, confirmado contra
> `Demandas de Clientes..._all.csv`) vieram direto do CSV consolidado (fonte estruturada
> padrão daqui pra frente, para qualquer cliente). A **narrativa/texto livre da página** o CSV
> não traz (só 2 de 1.007 linhas do CSV tinham a coluna `Texto` preenchida) — fica marcada
> como `[a preencher]` até o Vinicius colar o conteúdo de cada página.
>
> **PENDÊNCIA DE ACESSO — RESOLVIDA em 08 jul 2026.** Tentativas de acesso direto via
> navegador (`claude-in-chrome`) não funcionaram (conta `vinicius.risoleo@gmail.com` sem
> acesso ao workspace uMode) e a leitura de página por página no navegador seria muito lenta
> (get_page_text/read_page não extraem bloco de conteúdo do Notion — só screenshot visual). A
> solução real: o Vinicius exportou a base "Demandas de Clientes" em **HTML** (não CSV) via
> Notion, em `Demandas Totais - Lofty/uMode Geral/Databases/Demandas de Clientes/` — 85
> arquivos `.html`, um por demanda, cada um com a narrativa completa da página (e uma subpasta
> de anexos quando havia imagem/áudio/vídeo). Validado com 2 exemplos que já tínhamos 100%
> confirmados manualmente (UMD-209, UMD-307) — bateu palavra por palavra. As 75 narrativas
> abaixo foram extraídas desse HTML (script: remove CSS/JS, mantém quebras de parágrafo,
> marca imagem como `[IMG]`, decodifica acentuação). Anexos ficam listados no campo `Anexos`
> de cada demanda, com o nome do arquivo na subpasta correspondente do export.
>
> **Nota de qualidade (08 jul 2026):** o script de extração usado aqui tinha um bug sutil,
> descoberto só depois (na extração de RFI): quando a página tem uma tabela dentro do corpo
> (não só a de propriedades), `LastIndexOf('</table>')` pega a tabela errada e pode cortar a
> narrativa. Corrigido para usar a âncora `</table></header>` (única, confiável). A pasta
> `Demandas Totais - Lofty/` foi removida antes de eu poder reconferir as 85 demandas contra
> esse bug — `UMD-321` ficou com narrativa vazia e não dá pra confirmar se é legítimo (página
> sem corpo) ou se foi cortada. Risco baixo (todas as outras 84 foram conferidas e batem), mas
> registrado aqui para não perder o dado.

## Observações abertas (a resolver na formalização, não agora)
- Campos aparecendo nos dados reais que não constavam no levantamento original do Notion:
  `Responsabilidade` (ex.: "Demanda com uMode"), `Área Responsável` (ex.: "KA"), `Última
  edição`. `Área Responsável` parece distinto de `Key Account/Responsável` — não vou assumir
  que são a mesma coisa até confirmar.
- **[CORRIGIDO 06/07 com o CSV]** `Data de Previsão de Entrega`: minha hipótese de formato
  MM/DD estava **errada**. O CSV consolidado (`Demandas de Clientes..._all.csv`) grafa essa
  mesma data por extenso (ex.: UMD-209 = "January 9, 2025"), o que prova que o campo é DD/MM
  como todos os outros — `09/01/2025` é 9 de janeiro mesmo, não 1º de setembro. Conclusão: a
  data de previsão realmente **antecede** a data de solicitação em várias demandas antigas
  (UMD-209 a UMD-215, todas com previsão em jan–mai/2025 contra solicitação em ago/2025) — é
  dado ruim/placeholder do Notion legado, não questão de formato. Não vou corrigir, só marcar
  como inconsistência confirmada na formalização.
- Nota do Vinicius (UMD-212): o texto livre às vezes menciona outras pessoas sendo envolvidas
  para dúvidas/ações pontuais (ex.: "ver com a Marina", "envolver time Ops com Will") sem que
  isso mude o responsável formal da demanda. Não vou tratar essas menções como
  `Co-responsáveis` automaticamente na formalização — ficam registradas como contexto da
  narrativa, a menos que o Vinicius confirme que alguma delas deveria virar responsabilidade
  formal.
- `Data de Conclusão` vazia com `Status = Concluída`: já aconteceu 4x (UMD-211, UMD-214,
  UMD-215, UMD-308) — padrão recorrente do Notion legado, não vou inferir uma data — fica
  `[a preencher]` na formalização, a menos que o Vinicius tenha o dado por outra fonte.
- `Área Responsável` confirmado como enum real, não só "KA": UMD-308 trouxe `OPERAÇÃO`, e o
  lote de 75 do CSV trouxe também `TECH` — pelo menos 3 valores confirmados (KA, OPERAÇÃO,
  TECH). Segue distinto de `Key Account/Responsável` (que continua "Laura Delgado"
  independente do valor de Área Responsável).
- `Responsabilidade` também é enum com mais de um valor: além de "Demanda com uMode" (a
  maioria), o lote de 75 trouxe "Demanda Pendente do Cliente" (UMD-1263).
- UMD-308 traz um link para `umode.kanbanize.com` — sistema externo (Kanbanize) não
  mencionado até agora. Pode ser a ferramenta por trás do CX Hub, ou um sistema à parte —
  não vou presumir, só registrando a referência para perguntar na formalização.
- **Novo sistema externo encontrado no CSV:** o campo `Task` de UMD-1248 traz um link para
  `linear.app/umode/issue/...` — indica que o time de Tecnologia usa Linear para tracking de
  issues, referenciado a partir da demanda no Notion. Mais um sistema (além de Kanbanize e
  CX Hub) — não vou presumir a relação entre eles, só registrar para perguntar na
  formalização (qual é legado, qual é vigente, como se relacionam).
- **Achados do CSV consolidado (`_all.csv`, 1.007 linhas, 20 clientes):** confirma que
  `Responsabilidade`, `Área Responsável`, `Key Account/Responsável`, `Última edição` são
  campos reais (bate com o que o Vinicius vinha passando manualmente). Revela campos novos
  que não apareciam nas 10 primeiras demandas: `RFI` (44 das 1.007 linhas têm referência
  preenchida — confirma no mundo real o vínculo Demanda→RFI do nosso modelo), `Prioridade`,
  `Criticidade`, `Nível de Esforço`, `Bloqueio`, `Horas de Demanda`, `Horas - Recurso
  Específico`, `Total de Horas`, `Tempo de Resolução`, `Task`, `Suporte Integração`,
  `Observações`, `Arquivos e mídia`/`Files & media` (dois campos parecidos, possível
  duplicação/legado), e `👥 Clientes` (identifica o cliente por linha — é o campo que vai
  permitir padronizar a extração para qualquer cliente daqui pra frente). 10 das 1.007 linhas
  têm `👥 Clientes` vazio — candidatas a demandas 100% internas (natureza `interna` no nosso
  modelo). A coluna `Status` do CSV está com o header genérico `Property`, não `Status` — só
  um apelido estranho do export, mesmo dado.
- **Fonte estruturada padrão a partir de agora:** decidido com o Vinicius em 06/07 que os
  campos estruturados (não a narrativa) das 75 demandas restantes de Lofty — e de qualquer
  cliente futuro — vêm direto do CSV consolidado, sem digitação manual. Só a narrativa/texto
  livre da página continua manual, campo por campo, porque o CSV não a contém (ver nota no
  topo do arquivo).
- Demandas com múltiplos subitens e resultado misto (UMD-215): uma única demanda do Notion
  pode empacotar vários pedidos pontuais (aqui, 5 campos com valor padrão), cada um com seu
  próprio resultado — 4 concluídos (✅) e 1 inviável por regra técnica (⚠️), mas a demanda
  inteira segue registrada como `Status = Concluída`. É um bom candidato real para virar
  `Subdemandas` (checklist tático dentro do card) na formalização, em vez de um único
  resultado binário.
- IDs do Notion não são sequenciais no lote que o Vinicius está trazendo (salto de UMD-215
  para UMD-307) — confirma que não dá pra reaproveitar o número do Notion como nosso
  `D-AAAA-NNN` (que é sequencial só dentro do nosso sistema). Sugestão para a formalização:
  guardar o ID do Notion como referência legada (`ID legado (Notion)`), campo que o template
  atual (`_template_demanda.md`) ainda não tem — avaliar se adicionamos.
- UMD-307 referencia imagens ("IMAGEM") no texto livre da página que não foram trazidas aqui —
  fica registrado que existem, mas o conteúdo visual não está capturado neste staging.
- `Última edição` repetindo o mesmo timestamp em demandas diferentes: UMD-308 e UMD-309 têm
  ambas `03/02/2026 14:07` (e UMD-307 tem `02/02/2026 14:07`, um dia antes). Não parece edição
  orgânica individual — hipótese: um evento em lote (export/sync/migração) tocou várias
  páginas ao mesmo tempo em fev/2026. Não vou tratar isso como atividade real na demanda.

---

## UMD-209
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Alterar a Aba Chat - Depois de Arquivos
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/01/2025 (⚠ anterior à Data de Solicitação — ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 29/08/2025 18:01
- Data de Conclusão: 29/08/2025
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: 03/09/2025
- Texto livre da página:
  - "Gustavo pediu por e-mail e na Weekly para deixarmos por hora essa aba no final."

---

## UMD-210
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Alterar o Campo Coleção da Ficha para "Coleção Linx"
- Comentários uMode: vazio
- Quem solicitou: Gustavo
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/01/2025 (⚠ mesmo padrão de UMD-209 — ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 29/08/2025 18:18
- Data de Conclusão: 29/08/2025
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 03/09/2025
- Texto livre da página:
  - Gustavo trouxe a dúvida de que o Campo Coleção existe na Página 1 e Página 2 e trazem
    lista de seleção diferentes. De fato são campos diferentes: um é a hierarquia de
    organização da conta, outro é campo customizado na Ficha. Podem ser o mesmo se a regra
    de negócio do cliente permitir — existem clientes sem campo Coleção na Ficha, com a
    integração feita pela coleção da pasta. Precisava avaliar com a Lofty se podiam ser as
    mesmas ou se a lista de Coleções para cadastro no Linx precisava de detalhamento maior
    que a estrutura de pastas.
  - Em reunião, alinhado com o Gustavo que são coisas diferentes — optaram por renomear o
    campo da ficha para "Coleção Linx" para evitar confusão interna.

---

## UMD-211
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ajustar o Campo Referência para: Somente Leitura
- Comentários uMode: vazio
- Quem solicitou: vazio
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/02/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 29/08/2025 18:26
- Data de Conclusão: vazio (⚠ Status é "Concluída" mas não há data de conclusão registrada)
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 03/09/2025 17:12
- Texto livre da página:
  - **Gustavo pediu para travar o campo Referência** (Mapa de produtos e Página inicial de
    cadastro).
  - Este campo será gerado automaticamente por um código do Linx.
  - Solicita-se travar a digitação manual para evitar inconsistências, mesmo que depois seja
    sobrescrito:
    - Ajustar configuração para Somente Leitura
    - Incluir Hint: "Campo gerado automaticamente por um código Linx."
    - read only

---

## UMD-212
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Exibir Código uMode em dados gerais e também no mapa
- Comentários uMode: vazio
- Quem solicitou: vazio
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/05/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 29/08/2025 18:29
- Data de Conclusão: 12/09/2025
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 12/09/2025 09:15
- Texto livre da página:
  - **Trazer o código uMode** (Mapa de produtos). Sugestão: exibir o Código uMode nessa tela
    para controle interno antes da integração Linx — entender a possibilidade de trazer o
    código para a aba de dados gerais e deixar visível no mapa também.
  - Trouxeram o campo "Código uMode" para a aba de informações gerais.
  - ⚠️ Nota: ver com a Marina se dava para criar uma ação para preencher a "Referência do
    Produto" com esse código por enquanto, para ficar visível no mapa. Se sim, envolver time
    Ops com Will para criar a ação.
  - Criaram em 12/09 a ação para um campo custom oculto na ficha chamado "Código uMode Mapa" —
    agora conseguem filtrar no mapa e incluir a coluna configurando a lista.

---

## UMD-213
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Travar edição do Campo Responsável
- Comentários uMode: vazio
- Quem solicitou: Gustavo
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/02/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 01/09/2025 15:48
- Data de Conclusão: 01/09/2025
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 03/09/2025 16:08
- Texto livre da página:
  - **Campo Responsável** (Página inicial de cadastro). Sugestão: preencher automaticamente
    com o usuário logado no sistema; não permitir alteração manual, para garantir
    rastreabilidade.
  - O campo Responsável é preenchido automaticamente com o nome do usuário que criou o card
    do produto.
  - Pode ser editado caso o cliente queira usar o campo para indicar um responsável específico
    (ex.: Estilista) — funcionalidade padrão da plataforma, traz benefícios de navegação (ex.:
    exibir em "Meus Produtos" só os produtos de cada usuário).
  - `read_only: true`

---

## UMD-214
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Tipo de Produto é igual ao Grupo - Incluir hint
- Comentários uMode: vazio
- Quem solicitou: Gustavo
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/02/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 01/09/2025 15:48
- Data de Conclusão: vazio (⚠ Status "Concluída" sem data — ver Observações, já é padrão 2x)
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 08/09/2025 17:17
- Texto livre da página:
  - **Campo Tipo Produto** (Página inicial de cadastro). Gustavo trouxe o ponto: campo
    aparentemente traz a lista de seleção de Grupo que já existe na Página 2, e a informação
    não é levada se preenchida na Página 1. Pediu para validar a real função do campo e se a
    descrição está correta.
  - É campo obrigatório para criação do produto. Traz a lista de seleção dos Grupos porque é
    configurado de acordo com a hierarquia de produto do cliente. Na Lofty, confirmado no
    Discovery que Grupo é o 1º nível da hierarquia de produto.
  - Ao selecionar o Tipo de Produto, preenche automaticamente o campo Grupo na Ficha do
    Produto — é o mesmo campo, mas na Ficha exibe o ID do Linx logo abaixo da descrição.
  - Incluído um Hint: "Campo automático de acordo com o Tipo de Produto preenchido na criação
    do produto."
  - ⚠️ Nota: estavam validando com a Van e o Holmer + cliente se valia travar esse campo para
    futuras edições. Cliente optou por travar o campo por enquanto.

---

## UMD-215
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Deixar Campo Padrão nos Campos de Seleção: "Status Atual",
  "Unidade", "Item Sped", "Restrição de Lavagem" e "Código Cest"
- Comentários uMode: vazio
- Quem solicitou: Gustavo
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/03/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 01/09/2025 17:10
- Data de Conclusão: vazio (⚠ Status "Concluída" sem data — já é padrão 3x, ver Observações)
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 08/09/2025 17:18
- Texto livre da página — ajuste direto no Admin, incluir opção no campo Valor padrão:
  - Campo Status Atual (Página Informações Gerais): padrão "LIBERADO" (para integrar no
    Linx) — ✅ feito
  - Campo Unidade (Página Informações Complementares): pré-preenchido "PC" — ✅ feito
  - Campo Item Sped (Página Informações Complementares): pré-preenchido "Produto Acabado" —
    ✅ feito
  - Campo Restrição de Lavagem (Página Informações Complementares): pré-preenchido "Padrão" —
    ✅ feito
  - Campo Código Cest (Página Informações Complementares): pré-preenchido "2805900" — ⚠️ não
    feito: esse campo tem hierarquia com o campo NCM, não é possível deixar com informação
    padrão fixa.

---

## UMD-307
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Nova Aba "Estilo | Detalhes Produto" para Ecommerce
- Comentários uMode: vazio
- Quem solicitou: vazio
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado Cardoso
- Criado em: 02/09/2025 14:26
- Data de Conclusão: 19/09/2025
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 02/02/2026 14:07 (⚠ bem depois da conclusão — página deve ter sido revisitada)
- Texto livre da página:
  - Agenda feita com a Marina; dúvidas mandadas no grupo da Lofty por Gustavo. Registrado numa
    planilha como ficaria o campo de integração — link:
    https://docs.google.com/spreadsheets/d/1qZ1i-kTZJsYQp-XGgqCWHPkCKZnCv1lzmHw95cH0cxE/edit?gid=721191482#gid=721191482
  - Weekly de 12/09, alinhado com o Gustavo: incluir campos de Detalhes para integrar de
    acordo com as Propriedades — levar a info "*Detalhes do Produto:" e "*Tecido". Puxar
    agenda com Marina e Felipe para entender as possibilidades de integração.
  - Proposta de Enriquecimento Ecommerce: criar aba "ESTILO/Detalhes Produto" (imagens de
    referência mencionadas na página, não capturadas aqui — ver Observações), com legenda:
    - #1: texto "*DETALHES DO PRODUTO:" inserido fixo na tabela PROP_PRODUTOS, propriedade
      `00047`, para o produto criado. Resultado: "*DETALHES DO PRODUTO"
    - #2: texto "*TECIDO:" inserido fixo na tabela PROP_PRODUTOS, propriedade `00085`,
      concatenado com o texto digitado "MALHA DE TRICOT". Resultado: "*TECIDO: MALHA DE
      TRICOT"
    - #3: texto "*COMPOSIÇÃO:" inserido fixo na tabela PROP_PRODUTOS, propriedade `00086`,
      concatenado com o texto selecionado "55%LINHO 45%ALGODÃO". Resultado: "*COMPOSIÇÃO:
      55%LINHO 45%ALGODÃO"

---

## UMD-308
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ficha de Impressão
- Comentários uMode: vazio
- Quem solicitou: Gabriela
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 01/09/2025
- Data de Previsão de Entrega: 09/12/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 02/09/2025 14:29
- Data de Conclusão: vazio (⚠ Status "Concluída" sem data — já é padrão 4x, ver Observações)
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: OPERAÇÃO (⚠ primeiro valor diferente de "KA" — ver Observações)
- Última edição: 03/02/2026 14:07
- Texto livre da página:
  - Agenda realizada com o cliente em 02/09. Alinhado colocar um limite de tamanho na imagem
    para não deixar quebrar a imagem em duas páginas.
  - Link: https://umode.kanbanize.com/ctrl_board/47/cards/21277/details/ (ver Observações)

---

## UMD-309
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Campo Peso, incluir hint
- Comentários uMode: vazio
- Quem solicitou: Gustavo
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: 09/02/2025 (⚠ anterior à Data de Solicitação — inconsistência confirmada, ver Observações)
- Criado por: Laura Delgado Cardoso
- Criado em: 02/09/2025 14:57
- Data de Conclusão: 02/09/2025
- Key Account/Responsável: Laura Delgado Cardoso
- Área Responsável: KA
- Última edição: 03/02/2026 14:07 (⚠ mesmo timestamp de UMD-308 — ver Observações)
- Texto livre da página:
  - **Campo Peso** (Página Informações Complementares). Precisa informar a unidade (kg, g
    etc.) para saber se o preenchimento é 0,3kg ou 300g.
  - Entendimento: precisa de outro campo de unidade de medida para o Peso, com opções Kg ou
    g — já que o campo UNIDADE existente trata da unidade do produto (não do peso).
  - Decisão: incluir um hint no campo informando "cadastrar o peso em 'kg', não cadastrar com
    vírgula", já que o Linx não recebe unidade de medida.

---

## UMD-317
- Tipo de Demanda: Configuração
- Status: Não iniciada
- Etapa: Backlog
- Descrição da Solicitação: Hierarquia do Campo Categoria 
- Comentário uMode: Estamos aguardando Time Lofty passar a regra.
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: October 9, 2025
- Criado por: Laura Delgado
- Criado em: September 3, 2025 10:21 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:03 PM
- Texto livre da página:
  - Quer amarrar o Campo categoria ao Grupo e Subgrupo
  - Gustavo ficou de nos passar a regra.
  - Config:
  - Hierarquia de campo[”1ª opção que o usuário vai ler”, “aqui vem o que está no banco”, “Regra”]Seleciono no filtro o campo de onde ele vai pegar. Por Exemplo linha na luiza barcelos
  - update_fields: [”custom/ …”

---

## UMD-319
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ajuste do Campo Modelista
- Comentário uMode: Estamos aguardando a Gabi mandar a nova Lista de seleção
- Quem solicitou: Gabriela
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 02/09/2025
- Data de Previsão de Entrega: October 9, 2025
- Criado por: Laura Delgado
- Criado em: September 3, 2025 10:25 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Gabi quer incluir o nome das Modelistas Freelas e deixar entre parenteses (externo) somente para identificação. EX: Maria (Externo)
  - No caso da Modelista ser o próprio Fornecedor, ela marca essa opção e preenche o fornecedor na aba de fornecedor.
  - Ela vai nos mandar a lista atualizada para ajustarmos no admin.

---

## UMD-318
- Tipo de Demanda: Configuração
- Status: Não iniciada
- Etapa: Backlog
- Descrição da Solicitação: Hierarquia do Campo Tipo
- Comentário uMode: Estamos aguardando Time Lofty passar a regra.
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: October 9, 2025
- Criado por: Laura Delgado
- Criado em: September 3, 2025 10:25 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:03 PM
- Texto livre da página:
  - Quer amarrar o Campo categoria ao Grupo e Subgrupo
  - Gustavo ficou de nos passar a regra.
  - Config:
  - Hierarquia de campo[”1ª opção que o usuário vai ler”, “aqui vem o que está no banco”, “Regra”]Seleciono no filtro o campo de onde ele vai pegar. Por Exemplo linha na luiza barcelos
  - update_fields: [”custom/ …”

---

## UMD-320
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Campo Revenda
- Comentário uMode: Time Lofty valindando regra de negócio
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: September 3, 2025 10:30 AM
- Data de Conclusão: September 25, 2025
- Key Account/Responsável: Laura Delgado
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Atualização 24/09 Lala: 
  - Consegui criar o campo Revenda dentro de Fornecedor e também consegui incluir a aba revenda na tabela de resumo. Mas ao dar o check no campo, a informação não está indo para a tabela de resumo, passei no discord para o Victor me ajudar 🙂
  - O eero estava no “list:”, eu tinha colocado somente “revenda” e o certo era “custon/revenda”.
  - CARD CONCLUIDO 25/09
  - Quais os fornecedores hoje que representam produção interna? Podemos considerar que todos os demais são PA e portanto levam a flag de REVENDA? Incluir campo na uMode para preenchimento na ficha do produto.
  - Esse campo “Revenda” ainda não exite na uMode. 
  - Gustavo comentou que no Linx precisam Flegar quando o produto é de Revenda. Numa integração deve ser levado como 1 e 0 
  - Van comentou que uma possibilidade seria fazer direto na integrção em vez de criar o campo. Gustavo precisa validar a regra de negocio.
  -  [IMG]
- Anexos: image.png

---

## UMD-321
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Incluir Campo “Piloteiro”
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 02/09/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: September 3, 2025 11:05 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:


---

## UMD-436
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Limpar base de tecidos e aviamentos sem fornecedor
- Comentário uMode: vazio
- Quem solicitou: Marina uMode
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Victor Aragão
- Criado em: September 17, 2025 8:51 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Bloqueio: Aguardando Recurso Especial
- Texto livre da página:
  - INFORMAÇÕES DO CHAMADO:
  - Canal de Atendimento:
  - Responsável pelo Chamado:
  - INFORMAÇÕES DO RECEBIMENTO:
  - Responsável pelo Atendimento / Abertura do Ticket: Marina
  - Responsável pela Análise:
  - INFORMAÇÕES DO TICKET:
  - → Qual o contexto do SUPORTE ?
  - Eu fiz uma primeira rodada de dados na Lofty dia 15/08/2025 e alguns deles deram erro
  - Rodei novamente a base dia 22/08/2025 e algumas mps duplicaram a linha de variante mas uma ficou com fornecedor vazio
  - → Como REALIZAR O SUPORTE?
  - Limpar do banco de dados de tecidos e aviamentos o que possuem duas vezes a mesma variante só que uma sem o nome do fornecedor
  - Se houver algum produto com vinculo nessas variantes que vamos excluir, me avisem para ajustar!
  - Exemplos:Aviamentos: 019657, 021810, 019658, 02.10.0001, 02.01.0008
  - Tecidos: não encontrei exemplos, acabei limpando alguns manualmente dia 22 mesmo.
  -  [IMG] 
  - → Quais os entregáveis do Ticket?
  -  Excluir variante de mp (tecidos e aviamentos) com fornecedor vazio
- Anexos: image.png

---

## UMD-516
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Campo Sexo na Ficha 
- Comentário uMode: vazio
- Quem solicitou: Gustavo + Marina uMode (Campo para integração)
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 22/09/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: September 22, 2025 7:08 PM
- Data de Conclusão: September 22, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: October 9, 2025 11:50 AM
- Texto livre da página:
  - 10 a) Podemos deixar o campo SEXO_TIPO como padrão “FEMININO”?
  - Time uMode: Disponibilizar campo na ficha, com valor padrão FEMININO. Opções: FEMININO (3), UNISSEX ou INDEFINIDO.
  - Campo Criado ID 6689Nome: sexo_tipoCampo: SexoValor Pradão: FEMININO

---

## UMD-517
- Tipo de Demanda: Integração
- Status: Standby - Produto
- Etapa: Backlog
- Descrição da Solicitação: Definir categoria de imagem para integrar
- Comentário uMode: Stand by - depende do módulo de integração de imagem
- Quem solicitou: Gustavo + Marina uMode (Integração)
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: integração
- Data de Solicitação: 22/09/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: September 22, 2025 7:21 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 23, 2026 3:33 PM
- RFI (referência): Lofty | RFI : Escopo - Integração de Imagens de Produto (https://app.notion.com/p/Lofty-RFI-Escopo-Integra-o-de-Imagens-de-Produto-29bb1d38e76880b2bb8aff45a7264842?pvs=21)
- Texto livre da página:
  - Integração de IMAGEM
  - Time uMode: Definir categoria de imagem para integrar (desenho, peça final). Inclusão de imagem via tela.
  - Gabi definiu as categorias de imagem, já foram criadas na uMode.Categorias de imagem para integração cadastradas:foto desenho/ficha de desenvolvimento
  - peça piloto
  - peça lacre - frente
  - peça lacre - costas
  - peça lacre - avesso frente
  - peça lacre - avesso costas
  - peça lacre - aviamento

---

## UMD-518
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Criar Campo MATERIAL_PRINCIPAL
- Comentário uMode: vazio
- Quem solicitou: Marina uMode (integração)
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 19/09/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: September 22, 2025 8:09 PM
- Data de Conclusão: September 24, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: October 9, 2025 11:50 AM
- Texto livre da página:
  - [IMG] 
  - Campo criado ID 6683Nome: material_principalCampo: Material PrincipalTipo de campo: Checkbox@Victor Aragão @Williem Berg Oliveira Vou precisar da ajuda de vocês :)Não consegui entender como colocar esse campo na aba de empenho “Ficha Técnica”, conseguem incluir esse campo pra mim, por favor?! 
  - Deu certo, campo criado!
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-543
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Criar Perfil dos usuários e Enviar convite
- Comentário uMode: vazio
- Quem solicitou: Gabriela
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: permissionamento
- Data de Solicitação: 29/08/2025
- Data de Previsão de Entrega: June 10, 2025
- Criado por: Andrea Holmer
- Criado em: September 29, 2025 12:20 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: October 9, 2025 11:50 AM
- Texto livre da página:
  - Enviar convite de acesso à uMode (Gestão de Coleção) para os usuários cfe link abaixo até dia 06/10, pois o treinamento vai acontecer dia 08/10 presencial na Lofty.
  - Favor criar os perfis de acordo com as informações da coluna "D”, por enquanto os perfis podem ter os permissionamentos iguais ao que tem o nome de “Lofty - Time” e, posteriormente, vamos definir quais as diferenças entre os perfis e ajustá-los
  - https://docs.google.com/spreadsheets/d/1v9gROFY-y5kaiNDoipbVbzRrQ0kTbZln/edit?gid=943336395#gid=943336395

---

## UMD-561
- Tipo de Demanda: Produto
- Status: Standby - Produto
- Etapa: Backlog
- Descrição da Solicitação: Desejo de deixar o Campo “Peso” identificado com “Kg”
- Comentário uMode: Demanda na fila de PRODUTO, sendo analisada com JuFerre e Andre
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: template de ficha
- Data de Solicitação: 01/10/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: October 1, 2025 8:48 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: PRODUTO
- Responsabilidade: Demanda com uMode
- Última edição: March 18, 2026 9:50 AM
- Texto livre da página:
  - Gustavo trouxe a solicitação no grupo do WhatsApp 01/10/2025
  - Pessoal, bom dia.
  - Todos bem?
  - Estava olhando a plataforma e o campo Peso, mesmo com a mensagem que colocamos ainda acho que pode causar confusão na hora de cadastrar por ele aceitar qualquer digitação, ( 300 / 0,3 / 0.3 ... ) , seria possível colocar uma mascara no front com o formato correto e no final identificar que é em KG, igual temos no linx, ficaria algo assim:
  -  [IMG] 
  - Assim mantemos o padrão linx que o pessoal já utiliza e garante que vai certo para o banco de dados
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-653
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Tecido não está vindo com o custo na integração
- Comentário uMode: vazio
- Quem solicitou: Time Lofty
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: integração
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: October 9, 2025 11:38 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: November 6, 2025 12:40 PM
- Texto livre da página:
  - Fizemos o treinamento presencial com o Cliente no dia 08/10. Quando fomos empenhar os tecidos, usamos o “Alfaiataria Marant” e ele estava indo sem o preço. 
  - Analisar e corrigir para a integração em Prod.
  - cc @Marina Santoro

---

## UMD-654
- Tipo de Demanda: Integração
- Status: Standby - Produto
- Etapa: Backlog
- Descrição da Solicitação: Possibilidade de trazer a imagem do tecido e aviamento dentro do cadastro.
- Comentário uMode: Stand by - depende do módulo de integração de imagem
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: integração
- Data de Solicitação: 08/10/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: October 9, 2025 11:43 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 30, 2026 11:45 AM
- RFI (referência): Lofty | RFI : Escopo - Integração de Imagens de MP (https://app.notion.com/p/Lofty-RFI-Escopo-Integra-o-de-Imagens-de-MP-29bb1d38e76880da92aad31b413f2473?pvs=21)
- Observações (CSV): RFI criada e em análise Tech/Comercial
- Texto livre da página:
  - Fizemos o treinamento com o time Lofty no dia 08/10 e o time trouxe que gostaria de ver a imagem dos tecidos e aviamentos, pois hoje no Totvs eles tem. 
  - cc @Marina Santoro
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image.png

---

## UMD-668
- Tipo de Demanda: Integração
- Status: Encerrada
- Etapa: Demanda Cancelada
- Descrição da Solicitação: Integração de Imagem (SMB)
- Comentário uMode: Combinamos de analisar isso após integração de produto finalizada.
- Quem solicitou: Gabriela
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: October 15, 2025 4:54 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Marina Santoro
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: February 6, 2026 8:37 AM
- RFI (referência): Lofty | RFI : Escopo - Integração de Imagens de Produto (https://app.notion.com/p/Lofty-RFI-Escopo-Integra-o-de-Imagens-de-Produto-29bb1d38e76880b2bb8aff45a7264842?pvs=21)
- Texto livre da página:
  - Relacionada com Definir categoria de imagem para integrar 
  - Categorias de imagens
  - foto desenho/ficha de desenvolvimento
  - peça piloto
  - peça lacre - frente
  - peça lacre - costas
  - peça lacre - avesso frente
  - peça lacre - avesso costas
  - peça lacre - aviamento

---

## UMD-676
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ações campos de integração
- Comentário uMode: vazio
- Quem solicitou: Marina
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: October 16, 2025 10:21 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Marina Santoro
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Descrever todas as ações de campos q precisam ser limpos por cliente:
  - Validação
  -  Ação para acionar a validação de integração
  - Limpeza de Campos
  -  Limpar last_integration quando alterar o produto
  -  Limpar linx_integration_error quando alterar o produto
  - Limpeza de Campos na Duplicação de Produto
  -  Limpar gatilho de integração, campo custom/liberado_integracao
  - Bloqueio
  -  Campos grupo (product_type) e subgrupo (custom/subgrupo) não podem ser alterados após integração gerar a referência do produto. Isso porque os ids dos campos são usados para criar o produto e depois de criado, não pode ser alterado

---

## UMD-727
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Cadastrar Pacote de Materiais
- Comentário uMode: vazio
- Quem solicitou: Gabriela e Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: pacote de materiais
- Data de Solicitação: 28/10/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: October 28, 2025 7:07 PM
- Data de Conclusão: November 7, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Arquivos/mídia: Untitled/PACOTE_DE_MATERIAS_-_LOFTY_STYLE_10.10.xlsx 
- Texto livre da página:
  - Precisamos incluir os pacotes de materiais na conta do cliente. Em anexo a planilha que a Gabi nos mandou. 
  - Dúvidas da Lala: 
  - Conseguimos cadastrar dessa forma? 
  - Como é feito esse cadastro?

---

## UMD-736
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Importar Cadastro de Produtos
- Comentário uMode: vazio
- Quem solicitou: Gustavo / Gabi
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 30/10/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: October 30, 2025 5:58 PM
- Data de Conclusão: November 7, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Arquivos/mídia: Untitled/CARGA_PRODUTOS_uMODE.xlsx, Untitled/CARGA_PRODUTOS_uMODE_v.2.xlsx, Untitled/CARGA_PRODUTOS_uMODE_v.3.xlsx 
- Texto livre da página:
  - Precisamos importar a carga de produtos do Armario 1 antes da integração ser ligada.
- Anexos: image.png

---

## UMD-756
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Incluir trava/bloqueio da grade quando produto tem código Linx
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: vazio
- Data de Solicitação: 04/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: November 4, 2025 4:57 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Incluir campo que bloqueia grade se o código Linx estiver preenchido.
  -  Criar campo grid_action_block
  -  Atualizar produtos via importação
  -  Validar se está bloqueada
  -  Incluir na ficha do produto para usuarios enxergarem essa trava
- Anexos: image.png

---

## UMD-757
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Liberar botão “Liberado para Integrar” para usuarias chave
- Comentário uMode: vazio
- Quem solicitou: Gabriela
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: November 4, 2025 5:51 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: April 27, 2026 1:38 PM
- Texto livre da página:
  - Liberar botão “Liberado para Integrar” para usuarias chave:
  - raiane.brito@loftystyle.com.br
  - amanda.lunardelli@loftystyle.com.br
  - isadora.terlizzi@shopseja.com.br

---

## UMD-759
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Incluir trava/bloqueio de variante quando produto tem código Linx 
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: vazio
- Data de Solicitação: 06/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: November 6, 2025 10:36 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Criticidade: Alta
- Nível de Esforço: Baixo
- Texto livre da página:
  - Ocultar botão de excluir variante de todos os usuários.
- Anexos: image 1.png, image.png

---

## UMD-778
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Criar aba para PCP/Compras
- Comentário uMode: vazio
- Quem solicitou: Gabriela
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: integração
- Data de Solicitação: 04/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: November 6, 2025 10:11 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- RFI (referência): Lofty | RFI : Escopo - Integração de Imagens de MP (https://app.notion.com/p/Lofty-RFI-Escopo-Integra-o-de-Imagens-de-MP-29bb1d38e76880da92aad31b413f2473?pvs=21)
- Texto livre da página:
  - Criar aba na Ficha de Produto com o nome: PCP | Compras ✅
  - Incluir os Campos:
  - Rota de Operação - Migrar da aba Infos. complementares para esta ✅
  - Preço de Venda Varejo - Migrar da aba Infos. gerais para esta ✅
  - Preço de Custo 
  -  [IMG] 
  - ✅ Campo Criado
  - ⚠️ @Victor Aragão @Williem Berg Oliveira É possível espelhar o Custo Total (que tem no relatório de pré custo) neste campo que criei? ✅- Pegar sempre de alguma ação que já exista para facilitar a configuração.
  - Mkup Meta ( texto livre) ✅
  - Mkup Calculado:Incluir a seguinte fórmula = Preço de Venda Varejo / Preço de Custo (preco_varejo / preco_custo)✅
  - ⚠️ @Victor Aragão @Williem Berg Oliveira não sei incluir fórmula no campo, conseguem me ajudar, por favor 😊
  - - Pegar sempre de alguma ação que já exista para facilitar a configuração.
  - Caminho: Admim → Automações → Ações
- Anexos: image.png

---

## UMD-779
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Criar campo “Nomes Antigos”
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: integração
- Data de Solicitação: 06/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: November 6, 2025 10:22 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- RFI (referência): Lofty | RFI : Escopo - Integração de Imagens de MP (https://app.notion.com/p/Lofty-RFI-Escopo-Integra-o-de-Imagens-de-MP-29bb1d38e76880da92aad31b413f2473?pvs=21)
- Texto livre da página:
  - Objetivo: Incluir campo com Nomes já usados em coleções antigas para consulta
  - Incluir o Campo:
  - “Nomes Antigos”Incluir Lista de seleção cfe consta na aba “NOMES UTILIZADOS” do arquivo abaixo, são quase 7000 opções, é viável incluir essa quantidade? https://docs.google.com/spreadsheets/d/1UwfiklYzW5Ragkw_2zC7lAzrY_Z4eHy6/edit?gid=1497222819#gid=1497222819

---

## UMD-794
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Configurar a Aprovação na Ficha Técnica
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: aprovação
- Data de Solicitação: 04/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: November 11, 2025 2:08 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Iniciamos a segunda fase do projeto e prcisamos criar na ficha a aba de aprovações. 
  - Seguir de exemplo a Aba de aprovações da “Conta Sandro”
  - ✅ Aba Criada!
  - ✅ Tipos de aprovações criados.

---

## UMD-795
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Inativar as Estilistas que não fazem mais parte da empresa no campo de selção
- Comentário uMode: vazio
- Quem solicitou: Gabi/Gustavo
- Projeto: vazio
- uMode - Macro Tema: ficha tecnica
- Data de Solicitação: 07/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: November 11, 2025 2:17 PM
- Data de Conclusão: November 26, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Temos no campo estilistas a lista com todas as estilistas, porém duas (ANA ELISA e CLEO) já não fazem mais parte da empresa. 
  - Precisamos te-las na lista por conta de histórioco, mas precisamos inativa-las para que ninguem selecione arrado.

---

## UMD-808
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro ao empenhar pacote de aviamento
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: November 14, 2025 12:01 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Problema com Pacote de Materiais
  - → Qual o contexto do SUPORTE ?
  - Relato do cliente: 
  - “Estamos enfrentando um problema em relação ao pacote de materiais KIT TAG ETIQUETA LACRE - LOFTY STYLE. Ao tentar realizar o cadastro de aviamento na ficha técnica, percebi que, ao acrescentar o Pacote 0, o sistema me direcionava automaticamente para uma página de erro.”
  -  [IMG] 
  - “Segundo o suporte, o pacote de materiais está vinculado ao aviamento 0270747, que não consta na nossa base de dados. Fui orientada a excluir o Pacote 0, mas essa ação não está disponível para o meu nível de acesso.
  - Ao verificar o cadastro de um produto em que o Pacote 0 foi utilizado, constatei ainda que o aviamento 021396 desapareceu da ficha técnica.”
  - Testei e pra mim tb dá esse erro ao tentar empenhar o pacote
- Anexos: image 1.png, image.png

---

## UMD-827
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro validação
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 19/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: November 19, 2025 5:38 PM
- Data de Conclusão: November 27, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Validação não reconhece campo selecionado. Essa questão está travando a integração de vários produtos.Produto: https://umode.app/!/ProductDatasheet/313663?tab=product-info
  -  [IMG] 
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image.png

---

## UMD-841
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Importação de novos produtos
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 25/11/2025
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: November 26, 2025 2:10 PM
- Data de Conclusão: November 26, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Gustavo pediu para importarmos mais 3 produtos na uMode e após isso passarmos o ID para ele “dar baixa” no Linx pro produto não duplicar. 
  - https://docs.google.com/spreadsheets/d/1993hxRKSyZ93HAlpdzSpmeTXekzPV5gL/edit?gid=1824335131#gid=1824335131

---

## UMD-844
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Custo diferente uMode x Linx
- Comentário uMode: vazio
- Quem solicitou: Michelle
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: November 28, 2025 9:47 AM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: TECH
- Responsabilidade: Demanda Pendente do Cliente
- Última edição: February 3, 2026 2:07 PM
- Observações (CSV): Demanda com Holmer e Marina analisando 
- Texto livre da página:
  - Produto 06.01.0070Michelle reportou que, na uMode, no relatório de custos, o custo ficou correto (R$89,07), mas que no linx está incorreto. Eu entendo que tudo relacionado ao linx, não seja algo que possamos verificar mas estou abrindo o card para confirmar isso. Print do relatório de custo e print do linx:
  -  [IMG] 
  -  [IMG] 
  - Outro caso:(Reportado pela Luciana)Produto: 06.26.0009Print do relatório de custo:https://cdn.getgist.com/projects/r6xwnnb4/file_attachment/original/1764355360-image.png?1764355360Print do linx:https://cdn.getgist.com/projects/r6xwnnb4/file_attachment/original/1764355518-image.png?1764355518__________________Outro ponto sobre relatório, mas só relacionado a uMode (linx não). Os zíperers tratorados ficaram com os preços zerados nos relatórios:produto 14.01.0008 sendo que ele tem preço cadastrado:
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image.png

---

## UMD-860
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Configuração de CheckList
- Comentário uMode: vazio
- Quem solicitou: Gabriela + Time Lofty
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: December 3, 2025 5:06 PM
- Data de Conclusão: December 16, 2025
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Nesse momento vale utilizar mais a aprovação de Piloto 
  - Lofty definiu os tipos de aprovação:
  - Piloto ✅
  - Contra Amostra ✅
  - Bandeira ✅
  - Lofty precisa definir qual a Lista ideal para cada checklist
  - Vão deixar somente um linha - Avaliação Geral
  - 3/12- APROVAÇÕES _definições TIPO DE APROVAÇÃO: PILOTO 
  - CONTRA-AMOSTRA
  - BANDEIRA 
  - CHECK LIST : DEIXAR UM ITEM GENÉRICO ( COM O NOME DE AVALIÇÃO GERAL) ✅
  - E 1 LINHA NA ABA ITEM ( AVALIAÇÃO GERAL) ✅

---

## UMD-869
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ajustar Usuários, Perfil e Permissionamento
- Comentário uMode: vazio
- Quem solicitou: Gabriela
- Projeto: 📌 [LOFTY] - ONBOARDING FASE 1  (https://app.notion.com/p/LOFTY-ONBOARDING-FASE-1-263b1d38e768803d9e60d7b141be090d?pvs=21)
- uMode - Macro Tema: permissionamento
- Data de Solicitação: 04/12/2025
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: December 4, 2025 3:52 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: March 3, 2026 10:53 AM
- Observações (CSV): Validação junto com o victor 10/02
- Arquivos/mídia: Untitled/LISTA_DE_USURIOS_UMODE.xlsx 
- Texto livre da página:
  - Revisar e Ajustar usuários no geral, cfe arquivo anexohttps://docs.google.com/spreadsheets/d/1KD2r0gh3eKgNdvuzkWVpj_A7HrG777Sl/edit?usp=drive_web&ouid=116533987626881226635&rtpof=true 
  - Ajustes em relação ao convite e inativação de usuários feitos.
  -  Ajustar o Perfil e Permissionamento dos usuários da conta conforme o documento atualizado e validado com o clientehttps://www.notion.so/umode/Perfil-de-Usu-rio-e-Permissionamentos-2e1b1d38e76880a5a7ffe4c673686e4a 
  - Aqui você vai ver que o Perfil Lofty - Time não existe mais e foram criados outros, por favor, quando ajustar os perfils, me sinaliza que eu mudo ali os usuários para o perfil correto.

---

## UMD-870
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ajuste de Calculo Aba PCP
- Comentário uMode: vazio
- Quem solicitou: Gabi
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: December 4, 2025 3:55 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda Pendente do Cliente
- Última edição: March 3, 2026 10:47 AM
- Observações (CSV): Ainda em validação com o cliente.
- Texto livre da página:
  - Trocar fórmula da aba PCP - preço venda varejo = digitado mark up 1 = fórmula (fórmula)
  - preço venda mark up/varejo = fórmula mark up 2 = digitado (hint) 
  - 1ª Linha Deixar só Rota Operação2ª Linha Deixar Preço Venda Varejo 1 (Campo moeda digitado), Campo “Mark Up 1 (preço de venda varejo 1/preço de custo), Campo “Preço de Custo” (Info. do relatório de pré custo - Incluir Hint) 
  - 3ª Linha Deixar Preço Venda Varejo 2 (Campo moeda), Mkup 2 (Campo de texto), Campo “Preço Custo Sugerido” de Formula Preço venda Varejo2/Mkup2

---

## UMD-885
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Criar Ficha de Impressão de Aprovação
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: ficha de impressão
- Data de Solicitação: 16/12/2025
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: December 16, 2025 11:39 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado
- Área Responsável: KA
- Responsabilidade: Demanda Pendente do Cliente
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Criar Ficha de Impressão de Aprovação no mesmo modelo da Plie, porém com o cabeçalho igual à Ficha de Impressão da Lofty já existente
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image.png

---

## UMD-887
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: No preço no Linx está com “.”, mas na uMode, está “,”
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: December 17, 2025 5:37 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Precisamos entender qual a melhor forma de tratar.

---

## UMD-888
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Material duplicado no relatório de custo
- Comentário uMode: vazio
- Quem solicitou: Daniela
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: December 17, 2025 5:40 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 8, 2026 10:15 AM
- Texto livre da página:
  - Ao selecionar, no relatório de custo, a variante off white, os aviamentos aparecem duplicados:Produto: https://umode.app/!/ProductDatasheet/313722?tab=product-materialsRelatório: https://umode.app/reports/products/313722/variants/436728/costPrint:
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image.png

---

## UMD-917
- Tipo de Demanda: Suporte
- Status: Encerrada
- Etapa: Demanda Cancelada
- Descrição da Solicitação: Custo diferente - uMode e Linx - Retroativos
- Comentário uMode: vazio
- Quem solicitou: Amanda e Luciana
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: January 16, 2026 11:34 AM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: February 3, 2026 2:07 PM
- Texto livre da página:
  - Estamos com alguns casos de custos diferentes ainda:1- AmandaProduto integrou última vez no dia 08/01:https://umode.app/!/ProductDatasheet/319044?tab=product-infoNo próprio produto ele não calculou o custo, sendo que todos estão com unidade:
  -  [IMG] 
  - 2- AmandaEla informa que o cálculo do pré-custo está incorreto:https://umode.app/!/ProductDatasheet/315732?tab=product-info
  - Isso porque ela informa 1kg = 1,55m e vão usar 64cm. Ela disse que o cálculo não ficou correto para ter dado 66.90000
  -  [IMG] 
  -  [IMG] 
  - 3- LucianaProdutos:https://umode.app/!/ProductDatasheet/315351?tab=product-infohttps://umode.app/!/ProductDatasheet/315364?tab=product-infoO custo preenchido não está refletindo, eles estão colocando manualmente:Ex: 06.28.0043
  -  [IMG] 
  -  [IMG] 
  - 4- Lucianahttps://umode.app/reports/products/315364/variants/439701/cost
  - Ela informou que a mão de obra não está somando no pré custo, somente tecidos e aviamentos;5- LucianaCusto diferente no produto, relatório e linxhttps://umode.app/!/ProductDatasheet/315551?tab=product-info
  -  [IMG] 
  -  [IMG] 
  - 6- Luciana 03.01.0012 BLAZER TALATANY, o cod da ombreira é 02.01.0084 está com o custo diferente
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 10.png, image 11.png, image 12.png, image 13.png, image 14.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image 8.png, image 9.png, image.png, WhatsApp_Ptt_2026-01-21_at_18.08.21.ogg

---

## UMD-919
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Materiais não cadastrados
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: January 19, 2026 11:59 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: February 9, 2026 5:34 PM
- Texto livre da página:
  - 02.02.0458 ✅ [IMG] 
  - 02.37.0045 , variante 0091⚠️Conferência 04/02/2026 - Variante 0091 segue sem cadastro.
  -  [IMG] 
  - 02.37.0048⚠️ Conferência 04/02/2026 - Aviamento não encontrado
  -  [IMG] 
  - 02.37.0049⚠️ Conferência 04/02/2026 - Aviamento não encontrado
  -  [IMG] 
  - 02.37.0050 ⚠️ Conferência 04/02/2026 - Aviamento não encontrado
  -  [IMG] 
  - 02.02.0501 ✅ [IMG] 
  - 02.02.0313 ✅ [IMG] 
  - 03.06.0007 , variante 0184 ✅⚠️ Conferência 04/02/2026 - Variante 0184 segue sem cadastro. [IMG] 
  - 02.02.0261 ✅ [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image 8.png, image.png

---

## UMD-925
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Material duplicado no Linx
- Comentário uMode: vazio
- Quem solicitou: Michelle Nogueira
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: January 20, 2026 12:52 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 4, 2026 4:27 PM
- Criticidade: Crítica / Urgente
- Texto livre da página:
  - Problema: Cliente (Michelle) questiona que o material está duplicado no Linx e consta uma cor que não existe no Linx ( Off white), além de não aparecer na reserva no Linx 
  - Solicita urgência na resolução!!
  - “Estou com uma dificuldade para emitir uma nota fiscal complementar. Notei que o item não aparece na reserva de materiais e parece estar duplicado na ficha técnica, tanto no Linx quanto na Umode (conforme os prints abaixo).Como a entrega está prevista para daqui a dois dias, gostaria do apoio de vocês para regularizar essa divergência e conseguirmos liberar a mercadoria a tempo.”
  - Ficha técnica Linx e reserva de material da OP
  -  [IMG] 
  - Quando abro o aviamento em inclusão/alteração ele esta vazio:
  -  [IMG] 
  -  [IMG] 
  - Na Umode a ficha está assim
  -  [IMG] 
  - E no cadastro de materiais nem existe a cor OFF WHITE
  -  [IMG] 
  - Abaixo o link do produto na uMode: https://umode.app/!/ProductDatasheet/313753?tab=product-info
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image.png

---

## UMD-948
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Possibilidade do Workflow por Variante
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 26/01/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: January 26, 2026 2:56 PM
- Data de Conclusão: January 28, 2026
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: January 28, 2026 3:54 PM
- Texto livre da página:
  - Validações (Gabi)Alterado nome da primeira etapa para “Pré-ficha”
  - Acrescentadas novas etapas
  - Criar Kanban por Variante!! Seguindo com um único Kanban!!
  - Após o uso do time, definir automações!
  - uMode:Fazer alteração do WF para ser por Variante, usar as mesmas etapas que estão no WF por Produto
  - Marcar treinamento com time (combinar agenda com a Gabi na weekly do dia 13/2)

---

## UMD-949
- Tipo de Demanda: Configuração
- Status: Nível de Análise
- Etapa: Análise Cliente
- Descrição da Solicitação: Possibilidade de Macroplan para controle de Armários
- Comentário uMode: vazio
- Quem solicitou: Gabi
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: January 26, 2026 3:00 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda Pendente do Cliente
- Última edição: April 27, 2026 3:37 PM
- Texto livre da página:
  - Entender com a Ju possibilidades de desenvolvimento e custos. 
  - Mostramos alguns modelos para a Gabi em 30/01 (exemplos da Vix, Puket…), o próximo passo é retomar com ela para definir o melhor modelo e solicitar ao Comercial uma proposta https://drive.google.com/drive/folders/1tLCcEUByAFo-NnmHotE_dE5g4amaEWXU
  - Definido pela Gabi (15/04):
  - Aprovado modelos tanto da VIX (Line Sheet) quanto da CAEDU. Orçar modelo da VIX.
  -  [IMG]
- Anexos: image.png

---

## UMD-950
- Tipo de Demanda: Configuração
- Status: Não iniciada
- Etapa: Backlog
- Descrição da Solicitação: Possibilidade de acrescentar Rendimento e Prazo de Entrega na ficha de material
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: January 26, 2026 3:05 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: April 9, 2026 10:29 AM
- Texto livre da página:
  - Cliente solicita ter as infos de “Rendimento” e “Prazo de Entrega” no Material
  -  [IMG] 
  - necessário avaliar as questões abaixo:
  - A Lofty cadastra essas informações no Linx? Se sim, seria viável trazer na integração de leitura?
  - Se não, seria viável criar campos no material na uMode para o cliente cadastrar ou simplesmente incluírem nas observações?
- Anexos: image.png

---

## UMD-953
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Materiais e produto não integraram
- Comentário uMode: vazio
- Quem solicitou: Amanda e Luciana
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 27/01/2026
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: January 27, 2026 5:35 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 10, 2026 10:42 AM
- Texto livre da página:
  - Produto 14010009 - aviamentos desse produto não integraramMateriais 02.02.0458 , 02.02.0501 - não subiram para uMode
  - https://umode.app/!/ProductDatasheet/314419?tab=product-materials 
  - Conferência 04/02/2026 - Feita por Lala
  - 02.02.0458 ✅ [IMG] 
  - 02.02.0501 ✅ [IMG] 
  - 32.30.0041⚠️ Item não encontrado em Tecidos e Aviamentos
  -  [IMG] 
  - 02.02.0501 | NAO SUBIU CADASTRO ✅ [IMG] 
  - 02.02.0458 | NAO SUBIU CADASTRO ✅ [IMG] 
  - 02.02.0501 | NAO SUBIU CADASTRO ✅ [IMG] 
  - 02.18.0101 | NAO SUBIU CADASTRO⚠️ Item não encontrado em Tecidos e Aviamentos
  -  [IMG] 
  - 02.02.0503 | NAO SUBIU CADASTRO ✅ [IMG] 
  - 02.11.0142 | NAO SUBIU CADASTRO⚠️ Item não encontrado em Tecidos e Aviamentos
  -  [IMG] 
  - 02.02.0502 | NAO SUBIU CADASTRO ✅ [IMG] 
  - 02.18.0089 | NAO SUBIU CADASTRO⚠️ Item não encontrado em Tecidos e Aviamentos
  -  [IMG] 
  - 03.11.0116 | NAO SUBIU VARIANTE⚠️ Ultima atualização desse item em 05/11/25
  -  [IMG] 
  - 023578 | NAO SUBIU VARIANTE⚠️ Ultima atualização desse item em 25/11/25
  -  [IMG] 
  - 02.20.0118 | NAO SUBIU VARIANTE⚠️ Ultima atualização desse item em 05/11/25
  -  [IMG] 
  - 02.02.0397 | NAO SUBIU VARIANTE ✅ [IMG] 
  - 02.18.0050 | NAO SUBIU VARIANTE⚠️ Ultima atualização desse item em 05/11/25
  -  [IMG] 
  - 019276 | NAO SUBIU VARIANTE ✅ [IMG] 
  - 03.06.0007 | NAO SUBIU VARIANTE⚠️ Ultima atualização desse item em 16/01/26
  -  [IMG]
- Anexos: image 1.png, image 10.png, image 11.png, image 12.png, image 13.png, image 14.png, image 15.png, image 16.png, image 17.png, image 18.png, image 19.png, image 2.png, image 20.png, image 21.png, image 22.png, image 23.png, image 24.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image 8.png, image 9.png, image.png, screencapture-umode-app-accessories-2026-02-04-17_07_22.png

---

## UMD-961
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Revisão de Preços e Custos Integração de Escrita
- Comentário uMode: vazio
- Quem solicitou: Gustavo e Gabi
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 30/01/2026   (GMT-3)
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: January 30, 2026 3:14 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 19, 2026 5:10 PM
- RFI (referência): Lofty | RFI: Escopo - Alteração de Regra para Custos de Variante (https://app.notion.com/p/Lofty-RFI-Escopo-Altera-o-de-Regra-para-Custos-de-Variante-2f4b1d38e768803a88fee17137744e8f?pvs=21)
- Observações (CSV): Demanda com RFI aberta em análise pela JuA e Sandro.
- Texto livre da página:
  - Flag varia_preco_cor sempre true.
  - Faccionado
  - TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - Se tiver mais de um fornecedor produzindo o produto, tem que fazer o valor médio
  - PA
  - TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  -  [IMG] 
  -  [IMG] 
  - Custo 1 [por produto]
  - PA
  - [PRODUTO] CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - Faccionado
  - [PRODUTO] CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - Se tiver mais de um fornecedor produzindo o produto, tem que fazer o valor médio
  -  [IMG] 
  -  [IMG] 
  - Operações Extras [por produto]
  - Faccionado
  - [PRODUTO] FICHA TECNICA > OPERAÇÕES > OPERAÇÕES EXTRAS = valor do campo manufacture.priceCOSTURA [FORNECEDOR]
  -  [IMG] 
  - Testes de integração
  - Produto PA19.10.0005 (16/10/25) 🟢 [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  - 16.00.0002 (20/10/25) 🟢 [IMG] 
  -  [IMG] 
  - Produto Faccionado04.02.0122 (04/11/25) [IMG] 
  -  [IMG] 
  - Casos de erro
  - Calca Mey 025565 [IMG] 
  -  [IMG] 
  - Calca Agnes 024340 [IMG] 
  -  [IMG] 
  - Atualização da regra de integração
  - Revisão das regras = CADA COR TEM O SEU CUSTO 99
  - PAPreco 99
  - POR COR: TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - CADA COR TEM O SEU CUSTO 99
  - Custo 1
  - POR PRODUTO: CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - FaccionadoPreco 99
  - POR COR: TABELA PRECO 99 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - Se tiver mais de um fornecedor produzindo o produto, tem que fazer o valor médio
  - Custo 1
  - POR PRODUTO: CUSTO 1 = valor do campo manufacture.price + insumos DA PRIMEIRA VARIANTE
  - Se tiver mais de um fornecedor produzindo o produto, tem que fazer o valor médio
  - Operações Extras
  - POR FORNECEDOR: Valor do campo manufacture.price por fornecedor
  - Campo varia custo cor
  - Solicitação do dia 24/11/25, “fizemos uma alteração na forma dos custos dos produtos e precisamos mapear um campo que temos no Linx (varia custo cor) e que hoje não temos na umode”.
  - Confirmar com Gabi: varia custo cor pode ser sempre true? SIM
  - o varia preço cor já é sempre true
  - Nova tabela de custos (produto_cores) no campo CUSTO_REPOSICAO1
  - CADA COR TEM O SEU CUSTO 
  -  [IMG] o mesmo preco que vai variando para 99 na produtos_preco_cor
  -  [IMG] Deve vim na produto_cores
  -  [IMG]
- Anexos: image 1.png, image 10.png, image 11.png, image 12.png, image 13.png, image 14.png, image 15.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image 8.png, image 9.png, image.png, Imagem_do_WhatsApp_de_2025-10-16_(s)_09.34.29_1916f107.jpg, Imagem_do_WhatsApp_de_2025-10-16_(s)_17.14.03_21a175b5.jpg, Imagem_do_WhatsApp_de_2025-10-16_(s)_17.14.36_f83ea5c0.jpg, Imagem_do_WhatsApp_de_2025-10-16_(s)_17.15.37_1da53281.jpg, Imagem_do_WhatsApp_de_2025-11-04_(s)_11.30.27_2905a45d.jpg, Imagem_do_WhatsApp_de_2025-11-04_(s)_11.30.49_157a9f53.jpg

---

## UMD-964
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Fornecedor não integrou
- Comentário uMode: vazio
- Quem solicitou: Gustavo
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 03/02/2026
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: February 4, 2026 9:05 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 9, 2026 4:50 PM
- Texto livre da página:
  - Contexto
  - Cliente reportou erros em importação porque o fornecedor GUANGZHOU RMLSE não veio do Linx.
  -  [IMG] 
  - To do
  -  Entender porque não integrou - se está relacionado com o gap de integrações ou se é outro motivo
  -  Integrar o fornecedor
  -  Validar que o fornecedor está na plataforma
  -  Avisar o Gustavo
- Anexos: image 1.png, image.png

---

## UMD-987
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Materiais não integraram
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 11/02/2026   (GMT-3)
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: February 11, 2026 3:07 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 20, 2026 3:04 PM
- Tempo de Resolução: 9
- Task: https://linear.app/umode/issue/INTEG-708/lofty-integr-leitura-material-pendente
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image.png

---

## UMD-988
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Materiais não integraram
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 11/02/2026   (GMT-3)
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: February 11, 2026 3:18 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: March 9, 2026 1:06 PM
- Tempo de Resolução: 10
- Task: https://linear.app/umode/issue/INTEG-672/lofty-integr-leitura-material-pendente
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - Foram adicionados entre 10 e 11/02;02.20.0154
  - 0005 – PRATA
  - 0110 – DOURADO
  - 02.20.0138 - existe mas falta variante
  - 0099 – BEGE AREIA - falta
  - 0176 – TARTARUGA
  - 02.02.0505
  - 0002 – BRANCO 
  - 0010 – MARINHOhttps://umode.app/admin/dashboards/queries/242-materiais-e-variantes
  -  [IMG] 
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image.png

---

## UMD-990
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Linha com cód duplicado 
- Comentário uMode: vazio
- Quem solicitou: Daniela
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: February 12, 2026 5:24 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 24, 2026 10:50 AM
- Texto livre da página:
  - [IMG] 
  - Favor verificar porque as Linhas diferentes estão entrando com o mesmo código
- Anexos: image 1.png, image 2.png, image.png

---

## UMD-997
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ficha técnica: empenho com erro na uMode e no Linx
- Comentário uMode: CALCA GALICIA 06.27.0002
- Quem solicitou: Gustavo
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 06/02/2026
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: February 18, 2026 4:45 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: March 9, 2026 12:51 PM
- Tempo de Resolução: 20
- Task: https://linear.app/umode/issue/INTEG-644/lofty-integr-escrita-produto-com-erro-na-ficha-tecnica
- Suporte Integração: Escrita - Empenho
- Texto livre da página:
  - https://umode.app/!/ProductDatasheet/313712?tab=product-materials
  - 1) No resumo da ficha técnica da uMode mostra a aplicação de 1 unidade em cada aviamento. Mas quando entra no aviamento, todos os tamanhos estão zerados.
  - 2) Além disso, na aplicação por tamanho estão aparecendo tamanhos com ponto, coisa que a config x deveria ocultar no front.
  - 3) O que está dentro de cada MP na uMode é o que foi levado para o Linx.
  - 4) O correto para a ficha é 1 unidade em cada tamanho conforme a descrição do aviamento.
  - Precisa analisar o que aconteceu aqui, se o usuario fez algo estranho ou é do nosso lado. E dar a solução, como resolver esse empenho.
- Anexos: image.png

---

## UMD-999
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro na importação
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: February 19, 2026 4:50 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: February 20, 2026 2:00 PM
- Arquivos/mídia: Untitled/Planilha_Importao_LOFTY__teste.xlsx 
- Texto livre da página:
  - Erro na Importação
  - Ao tentar importar algumas informações, elas estão entrando em colunas trocadas, cfe abaixo:
  - foi testada a REGATA JORDANA, linha 16 da planilha anexada, mas dá erro parcial, por exemplo, diz que LINHO não foi encontrado no Campo Origem. Mas, na coluna do Campo ORIGEM tem a informação “0” e não LINHO! E assim ocorre nos demais…
  -  [IMG] 
  -  [IMG] 
  - no Campo Grade entra o valor do CEST (2805900), mas na planilha, está a info “ROUPA PP - GG”
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image.png

---

## UMD-1007
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produtos não estão atualizando no Linx
- Comentário uMode: REGATA GRASS
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 24/02/2026   (GMT-3)
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: February 24, 2026 11:33 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 17, 2026 5:19 PM
- Tempo de Resolução: 9
- Task: https://linear.app/umode/issue/INTEG-709/lofty-integr-escrita-produto-com-erro-de-integracao
- Suporte Integração: Escrita - Erro
- Texto livre da página:
  - Amanda da Lofty chamou no chat e passou que os produtos 06.28.0054 e 15.01.0024 foram alterados, mas não atualizaram no linx.
  - Dei uma olhada aqui, mas não identifiquei o que pode estar acontecendo...Eles não estão na fila e também não estão nos produtos que estão dando erro... @Marina Santoro Consegue me ajudar com isso, por favor.https://umode.app/!/ProductDatasheet/324850?tab=product-info
  - https://umode.app/!/ProductDatasheet/323471?tab=product-info 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 10.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image 8.png, image 9.png, image.png

---

## UMD-1024
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produtos e materiais não integraram
- Comentário uMode: Pendente analise
- Quem solicitou: Amanda e Raiane
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 26/02/2026   (GMT-3)
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: February 26, 2026 1:41 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: April 8, 2026 2:01 PM
- Tempo de Resolução: 7
- Task: https://linear.app/umode/issue/INTEG-722/lofty-integr-leitura-materiais-pendentes
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - https://umode.app/!/ProductDatasheet/324984?tab=product-infoO produto acima não integra porque o fator de conversão usado no material TRICOLINE GERALFIL LISA 05.19.0002 não veio para uMode via integração
  -  [IMG] 
  -  [IMG] 
  - _URGENTE - Material criado ontem 25/02 não integrou (RAIANE):02.02.0513Aqui mostra que material não existe e o outro tem tempo que não foi atualizado, desde 2025
  -  [IMG] 
  - __________Sarah também reportou sobre material:Ela enviou aqui mais materiais que não integraram o preço que está no linx pra uMode, atualizei na busca pra ficar fácil verificar a data da última atualização:https://umode.app/admin/dashboards/queries/250-lofty-26-0202.07.0111, 02.07.0110, 02.07.0109, 02.07.0108 e 02.07.0107 _______Sobre produto não integradohttps://umode.app/!/ProductDatasheet/327231?tab=product-integracao
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image.png

---

## UMD-1031
- Tipo de Demanda: Erro/ Bug
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro ao filtrar pelo Mapa de uma coleção específica
- Comentário uMode: Priorizar na semana 09/03
- Quem solicitou: Michelle
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: February 27, 2026 5:52 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: March 12, 2026 4:46 PM
- Texto livre da página:
  - A Michelle está com um problema onde o Mapa dela não carrega quando ela entra em uma coleção específica.O caminho que ela faz é: menu > mapa de coleções > expande coleção > clica no Mapa de uma marca específica > CONFIGURAR. A tela não para de carregar.
  - Testei pelo meu e isso NÃO ACONTECE, MAS- Ela testou em guia anônima e continua acontecendo- Acontece em várias coleções, não só em uma- Ela não usa nenhum filtro além do aplicado automaticamente ao clicar na coleção- Acontece com outras pessoas do time delaAnexei os vídeos nos comentários
- Anexos: 20260303-2045-35.7241885.mp4, WhatsApp_Image_2026-02-27_at_10.20.00.jpeg, WhatsApp_Video_2026-02-27_at_10.19.51.mp4

---

## UMD-1049
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produto não integrou
- Comentário uMode: REGATA GRASS
- Quem solicitou: Luciana
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: March 4, 2026 4:12 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: March 17, 2026 5:24 PM
- Texto livre da página:
  - Produto: 327231https://umode.app/integrations/executions/194424Consta que a subcategoria não existe, mas existe:
  -  [IMG]
- Anexos: image.png

---

## UMD-1067
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produtos não integraram para o Linx
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Ana Paula Ramos
- Criado em: March 9, 2026 11:24 AM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: April 16, 2026 4:24 PM
- Texto livre da página:
  - https://umode.app/!/ProductDatasheet/330386?tab=product-integracaohttps://umode.app/integrations/executions/196789
  - "type": "PRODUTO","id": 330386,"message": "Cannot read properties of undefined (reading 'data')"Validações okO produto nunca integrou antes-O mesmo acontece com esse produto que nasceu do linx: 330386No caso desse, não foi liberado para integrar e nem possui as validações, mas a Victoria informou que ela está enviando produtos que nasceram do linx e está acontecendo com vários. Estou aguardando ela enviar mais exemplos, mas como é o mesmo erro, coloquei aqui para entendermos juntos se é isso mesmo.
- Anexos: image.png

---

## UMD-1099
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produto com Cód. Linx “errado”
- Comentário uMode: Chamado via Chat
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 17/03/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: March 17, 2026 9:53 AM
- Data de Conclusão: March 17, 2026
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 17, 2026 1:04 PM
- Texto livre da página:
  - Amanda chamou no Chat dizendo que um produto foi criado, mas que nunca foi integrado e está com um código linx, além disso, esse código já existe em outro produto.https://umode.app/!/ProductDatasheet/330674?tab=product-integracao 
  -  [IMG] 
  - Fiz uma conferência e realmente o campo de checkbox “Produto Liberado para Integrar?” não está flegado.
  - Porém olhando o histórico de produto aparece um erro de integração dia 26/02 e uma nova integração 02/03.https://umode.app/products/330674/audits?return_path=https%3A%2F%2Fumode.app%2F!%2FProductDatasheet%2F330674%3Ftab%3Dproduct-integracao 
  - A cliente precisa que esse código seja excluído do produto. Conseguimos deixar em branco para ela fazer uma nova integração?Abaixo o retorno que dei pra ela via chat.
  -  [IMG]
- Anexos: image 1.png, image 2.png, image.png

---

## UMD-1100
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro de integração de Fornecedor (Blusa Georgina e Feive Comercio)
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 17/03/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: March 18, 2026 9:44 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 20, 2026 10:15 AM
- Tempo de Resolução: 1
- Task: https://linear.app/umode/issue/INTEG-793/lofty-integr-leitura-fornecedor-pendente
- Suporte Integração: Leitura - Fornecedor pendente
- Observações (CSV): Chamado tbm aconteceu no grupo do Whats
- Texto livre da página:
  - [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  - Amanda também passou sobre esse fornecedor que não subiu:
  -  [IMG] 
  - Sarah passou dia 19/03 um novo fornecedor que está no Linx e não subiu para a uMode.
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image.png

---

## UMD-1101
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Variantes e Materiais que não subiram pra uMode - Forro Malha e Chiffon Baia
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 18/03/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: March 18, 2026 9:51 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 23, 2026 3:58 PM
- Tempo de Resolução: 4
- Task: https://linear.app/umode/issue/INTEG-794/lofty-integr-leitura-material-pendente
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - A Amanda repostou que cadastrou alguns materiais e variantes na semana passada, mas que ainda não subiram pra uMode. Pode investigar por favor?! 
  - Esse a Variante não subiu (0006 Marinho)
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-1104
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Cor não integrou
- Comentário uMode: vazio
- Quem solicitou: Regina
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 17/03/2026
- Data de Previsão de Entrega: vazio
- Criado por: Marina Santoro
- Criado em: March 18, 2026 1:25 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: March 18, 2026 1:26 PM
- Tempo de Resolução: 1
- Task: https://linear.app/umode/issue/INTEG-790/lofty-interg-leitura-cor-pendente
- Suporte Integração: Leitura - Cor pendente
- Texto livre da página:
  - ROSA NUDE 0200
- Anexos: Marina_-_perfil.jpg

---

## UMD-1112
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro de integração de Variante (Saia Citrino) 
- Comentário uMode: vazio
- Quem solicitou: Marcello
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 19/03/2026
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: March 19, 2026 4:07 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 20, 2026 3:04 PM
- Observações (CSV): Chamado via Whats
- Texto livre da página:
  - A cor Marinho deste produto não integrou no Linx e o pessoal precisa dar saída na mercadoria
  - https://umode.app/!/ProductDatasheet/315395?tab=product-variants
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-1134
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produto não integrou variante - Vestido Art 23.03.0074
- Comentário uMode: vazio
- Quem solicitou: Luciana Nunes
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 25/03/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: March 25, 2026 8:55 AM
- Data de Conclusão: March 25, 2026
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: March 25, 2026 11:20 AM
- Texto livre da página:
  - Luciana chamou no chat falando que a cor do VESTIDO ART 23.03.0074 não integrou. ID do Produto 331587https://umode.app/!/ProductDatasheet/331587?tab=product-infoOlhando na integração, realmente está apontando um erro:
  -  [IMG] 
  - Pedi pro meu amigo chat GPT traduzir isso aí e ele me falou que:👉 Você está tentando inserir um registro em PRODUTO_CORES
  - 👉 Mas o valor enviado no campo COR
  - 👉 não existe na tabela CORES_BASICAS
  - Olhei na parte de cadastro e a cor existe na uMode e sigo sem saber como resolver, preciso de ajuda. 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image.png

---

## UMD-1142
- Tipo de Demanda: Relatório
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Relatório de Gestão de Coleção
- Comentário uMode: vazio
- Quem solicitou: Demanda de Escopo.
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: March 30, 2026 2:44 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 13, 2026 3:36 PM
- Texto livre da página:
  - Há um diferença no nº de produtos entre o Relatório e a Plataforma
  - Filtros utilizados:
  -  [IMG] 
  - no relatório constam 575 produtos
  -  [IMG] 
  - na platafoma constam 578 produtos
  -  [IMG] 
  - abrindo por status, se encontra diferença em Desenvolvimento e Cancelados
  -  [IMG] 
  -  [IMG] 
  - Por Variante o nº fecha certo!
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image.png

---

## UMD-1156
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Alterar o perfil do Planejamento
- Comentário uMode: vazio
- Quem solicitou: Bruno
- Projeto: vazio
- uMode - Macro Tema: permissionamento
- Data de Solicitação: 02/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: April 2, 2026 6:04 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: April 9, 2026 12:01 PM
- Texto livre da página:
  - Alterar o perfil do Planejamento para fazer Importação!

---

## UMD-1157
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Custo do Aviamento não está indo para o produto - SAIA CACAU / PONTEIRA TRANS RESINA
- Comentário uMode: vazio
- Quem solicitou: Gabriela Cunha
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 03/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 6, 2026 9:02 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 7, 2026 7:52 AM
- Texto livre da página:
  - [IMG] 
  -  [IMG] 
  - Link do Produto: https://umode.app/!/ProductDatasheet/319060?tab=product-materials 
  -  [IMG] 
  - Referência do aviamento: 232897/32
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image.png

---

## UMD-1160
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produtos com problema de integração
- Comentário uMode: KA
- Quem solicitou: Isadora Terlizzi
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 07/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 7, 2026 7:59 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 13, 2026 3:31 PM
- Texto livre da página:
  - O Time da Lofty mandou por e-mail esses produtos que estão com erro de integração. 
  - Cheguei a dar uma olhada em alguns, mas não entendi o que aconteceu. 
  -  [IMG] 
  - Marina, o Marcelo me chamou no Whats com mais um produto que apontou o erro de validação na cor. Mas quando vou olhar na variante, o código está preenchido. Tem uma “VARIANTE 3” criada sem nada, não sei se pode ser ela dando esse erro. Pode dar uma olhada também, por favor. 
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image.png

---

## UMD-1164
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Tecido não integrou
- Comentário uMode: vazio
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 08/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 8, 2026 8:26 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 9, 2026 5:01 PM
- Tempo de Resolução: 1
- Task: https://linear.app/umode/issue/INTEG-869/lofty-integr-leitura-material-pendente
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - Amanda chamou no chat dizendo que cadastrou um produto ontem e ele não subiu pra uMode. 
  -  [IMG] 
  - Olhei na uMode e parece que a integração ainda está em andamento, não sei se deu algum erro….
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-1178
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Ativar/inativar Usuários
- Comentário uMode: vazio
- Quem solicitou: Marcello
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Andrea Holmer
- Criado em: April 10, 2026 10:15 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: KA
- Responsabilidade: Demanda com uMode
- Última edição: May 27, 2026 2:49 PM
- Texto livre da página:
  - Inativar usuários sinalizados na coluna “I” da planilha do link abaixo
  - https://docs.google.com/spreadsheets/d/143jhf-8Uwv0FP9FtcC1pJ0K0mMRQngWM/edit?gid=667781702#gid=667781702
  - Irão incluir novos usuários, aguardar definição da Lofty para incluir
  -  ——
  - Dia 05/05 - Marcello solicitou ajuste de mais alguns usuários:
  -  [IMG] 
  - Dia 13/05 - Marcello Solicitou ajuste de mais usuários:
  - Sandro Alinhou com a Regina e o Marcello, fecharam o aditivo de contrato com 32 usuários, conforme planilha abaixo:https://docs.google.com/spreadsheets/d/1Kpek_in2B9dHLUd3pIDMZegujATYSsVe/edit?gid=553623698#gid=553623698
- Anexos: image.png

---

## UMD-1179
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Integração de Fornecedores - Não subiu
- Comentário uMode: vazio
- Quem solicitou: Valeria
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 10/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 10, 2026 11:34 AM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 16, 2026 4:16 PM
- Tempo de Resolução: 1
- Task: https://linear.app/umode/issue/INTEG-880/lofty-integr-leitura-fornecedores-pendentes
- Suporte Integração: Leitura - Fornecedor pendente
- Texto livre da página:
  - Marina a Valeria da Lofty chamou no Chat dizendo que cadastrou uns fornecedores na quarta-feira, mas que não subiram pra uMode. Dos que ela me passou realmente só subiu um fornecedor, consegue dar uma olhada, por favorJCG FITNESS CONFECCOES LT - 056017
  - ANDUZ MODAS - 056018
  - BZK TEXTIL LTDA - 056019
  - CHIC TOP FASHION LTDA - 056020

---

## UMD-1187
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produto cancelado na uMode, que segue ativo no Linx
- Comentário uMode: KA
- Quem solicitou: Marcello
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 13/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 13, 2026 12:58 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: April 14, 2026 11:52 AM
- Texto livre da página:
  - Marina, Marcello chamou no chat informando que o produto 04.02.0180 foi cancelado na uMode, mas que no linx no não foi. https://umode.app/!/ProductDatasheet/328732?tab=product-info 
  - Na documentação de regra de integração não localizei se esse Status do produto muda algo no linx ou se devem ajustar através do campo “Status Atual”.
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-1190
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Correção do Perfil Compras Importado
- Comentário uMode: vazio
- Quem solicitou: Caroline Koller
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 13/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 13, 2026 4:36 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: April 16, 2026 4:14 PM
- Texto livre da página:
  - Victor a Caroline chamou no chat dizendo que não está conseguindo integrar produto da uMode no Linx. Passei o passo a passo pra ela e quando ela me mandou o print foi conferir no perfil e permissionamento. O Perfil dela deveria ter acesso aba de “integração Linx” para poder flegar um produto Liberado para integrar, mas está sem, pode ajustar por favor.Perfil de Usuário e Permissionamentos 
  -  [IMG]
- Anexos: image.png

---

## UMD-1197
- Tipo de Demanda: Suporte
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Erro ao gerar ficha de impressão do produto CALCA PETRA
- Comentário uMode: vazio
- Quem solicitou: Marcello
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 16/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 16, 2026 1:02 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado, Andrea Holmer
- Área Responsável: OPERAÇÃO
- Responsabilidade: Demanda com uMode
- Última edição: May 8, 2026 9:47 AM
- Texto livre da página:
  - Marcello chamou no Chat dizendo que estão com problema ao entrar na ficha técnica (impressão) deste produto ( CALCA PETRA )https://umode.app/!/ProductDatasheet/334908?tab=product-info 
  -  [IMG] 
  - Quando clica na Impressora > Ficha Técnica, cai na pagina do “Isto é embaraçoso...”
  -  [IMG] 
  - Cheguei a refazer o mesmo caminho e testar alguns outros produtos, porém os demais produtos que testei, abriram normalmente.Ex: 
  - https://umode.app/!/ProductDatasheet/329654?tab=product-info 
  - https://umode.app/!/ProductDatasheet/332653?tab=product-info 
  - https://umode.app/!/ProductDatasheet/328181?tab=product-info 
  - https://umode.app/!/ProductDatasheet/324556?tab=product-info
  - https://umode.app/!/ProductDatasheet/338283?tab=product-info
  - No teste peguei mais um produto que deu erro:
  - https://umode.app/!/ProductDatasheet/334838?tab=product-info
- Anexos: image 1.png, image.png

---

## UMD-1202
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Produto aparece como integrado, mas não foi pro Linx - BLUSA FELICIA
- Comentário uMode: KA
- Quem solicitou: Amanda
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 17/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 17, 2026 3:33 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: April 22, 2026 3:56 PM
- Texto livre da página:
  - Marina, a Amanda da Lofty chamou no chat dizendo que o produto não integrou no Linx. https://umode.app/!/ProductDatasheet/332260?tab=product-info 
  - Olhando aqui, está com a validação feita, campo de liberado para integrar flegado e dizendo que a ultima integração foi hoje 17/04 às 15:02
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image.png

---

## UMD-1203
- Tipo de Demanda: Configuração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Liberar acesso para o Perfil Admin e Ficha Técnica poderem criar Tipo de Beneficiamento e Beneficiamento
- Comentário uMode: vazio
- Quem solicitou: Raiane 
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 17, 2026 4:46 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: April 20, 2026 9:07 AM
- Texto livre da página:
  - Precisamos dar acesso para os perfis ADMIN e FICHA TÉCNICA para poderem criar Tipo de Beneficiamento e Beneficiamento.

---

## UMD-1223
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Aviamento que não integrou - Botão de PE Metal Quadrado - 02.02.0519
- Comentário uMode: vazio
- Quem solicitou: Raiane 
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 27/04/2026
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: April 27, 2026 9:53 AM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda com uMode
- Última edição: May 8, 2026 9:57 AM
- Tempo de Resolução: 1
- Task: https://linear.app/umode/issue/INTEG-908/lofty-integr-leitura-material-pendente
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - Marina, a Raiane da Lofty chamou no chat dizendo que esse material foi cadastrado na semana passada e ainda não subiu pra uMode. 
  -  [IMG] 
  -  [IMG] 
  - ATUALIZAÇÃO LALA 29/04Marina, fui validar com a cliente a integração desse botão e ela me trouxe mais alguns materiais que não integraram, pode dar uma olhada, por favor.
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 10.png, image 11.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image 8.png, image 9.png, image.png

---

## UMD-1246
- Tipo de Demanda: Produto
- Status: Nível de Análise
- Etapa: Análise Cliente
- Descrição da Solicitação: Custo da Variante com Material por Tamanho
- Comentário uMode: vazio
- Quem solicitou: Marcello / Regina
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: May 5, 2026 11:07 AM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda Pendente do Cliente
- Última edição: May 27, 2026 2:10 PM
- Texto livre da página:
  - Lofty | RFI: Escopo - Custo da Variante com Material por Tamanho

---

## UMD-1248
- Tipo de Demanda: Integração
- Status: Concluída
- Etapa: Demanda Concluída
- Descrição da Solicitação: Aviamentos que não integraram 05/05/2026?
- Comentário uMode: vazio
- Quem solicitou: Raiane Brito
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: May 5, 2026 3:59 PM
- Data de Conclusão: vazio
- Key Account/Responsável: Laura Delgado
- Área Responsável: TECH
- Responsabilidade: Demanda com uMode
- Última edição: May 12, 2026 2:43 PM
- Task: https://linear.app/umode/issue/INTEG-931/lofty-integr-leitura-material-e-cor-pendente
- Suporte Integração: Leitura - Material pendente
- Texto livre da página:
  - Raiane chamou no chat dizendo que alguns aviamentos não integraram
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  - Esse ultimo, localizei na uMode, porém com o nome diferente…
  -  [IMG] 
  - Hoje 06/05 Raiane passou mais alguns materiais:
  -  [IMG] 
  -  [IMG] 
  -  [IMG] 
  -  [IMG]
- Anexos: image 1.png, image 2.png, image 3.png, image 4.png, image 5.png, image 6.png, image 7.png, image.png

---

## UMD-1263
- Tipo de Demanda: Integração
- Status: Nível de Análise
- Etapa: Análise Cliente
- Descrição da Solicitação: Campo Família - Integrado com linx
- Comentário uMode: vazio
- Quem solicitou: vazio
- Projeto: vazio
- uMode - Macro Tema: vazio
- Data de Solicitação: 
- Data de Previsão de Entrega: vazio
- Criado por: Laura Delgado
- Criado em: May 22, 2026 4:02 PM
- Data de Conclusão: vazio
- Key Account/Responsável: vazio
- Área Responsável: vazio
- Responsabilidade: Demanda Pendente do Cliente
- Última edição: May 27, 2026 2:25 PM
- Texto livre da página:
  - Campo Família - Ele não foi mapeado no início do projeto. Time Lofty alinhou internamente e definiu que vai ser preenchido pelo estilo e vamos levar pro Linx.Objetivo: Fazer uma junção dos produtos (por cor) para poder produzir a mesma quantidade. Campo já criado dentro de variante (Campo de Seleção)
  - No Linx será um campo de Texto, na uMode um campo de seleção.
  - Projeto daqui pra frente, pois não tem histórico controlado em nenhum sistema disso.
  - RFI: Lofty | RFI: Escopo - Campo Família - Integrado com o Linx
