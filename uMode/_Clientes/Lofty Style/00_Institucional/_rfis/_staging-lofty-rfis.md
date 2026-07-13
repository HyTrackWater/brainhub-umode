# Lofty Style · RFIs — staging bruto (Notion)

> Arquivo temporário de trabalho — não é o padrão final. Aqui acumulo os dados brutos das RFIs
> de Lofty Style, extraídos do CSV consolidado (`Particular e Compartilhado/uMode Geral/
> Operação de Clientes/uMode RFI/...`), cruzado contra o export filtrado só de Lofty — 15
> registros em ambos, sem divergência. A tradução para `protocolo-gestao-rfi.md` acontece
> depois, quando a narrativa também estiver disponível.
>
> **Pendência de acesso — RESOLVIDA em 08 jul 2026.** A mesma solução das demandas funcionou
> aqui: o Vinicius exportou a base de RFI em **HTML** (`RFIs Gerais - Lofty/uMode Geral/
> Operação de Clientes/uMode RFI/RFI Escopo - Lista de Entregáveis/`) — 15 arquivos `.html`,
> um por RFI, com a narrativa completa. Uma delas (RFI 104) tinha uma **subpágina aninhada**
> ("Análise Tech") com uma análise técnica detalhada (estimativas, arquivos de código,
> decomposição de esforço) — extraída e anexada à RFI 104. Bug de extração encontrado e
> corrigido nesse processo: quando a página tem uma tabela dentro do corpo (não só a de
> propriedades), a âncora ingênua pega a tabela errada e corta a narrativa — corrigido usando
> `</table></header>` (fim da seção de propriedades) como âncora, com fallback pra páginas sem
> tabela de propriedades (subpáginas comuns). As 15 RFIs abaixo estão com narrativa completa.
>
> **Mapeamento de campos aplicado (decidido em 08 jul 2026):**
> - `Cobrada? (sim/não)` do nosso padrão vem do campo `Cobrado` do CSV (Sim/Não/vazio) — o
>   campo `Cobrada?` do Notion (emoji 🎁 💰 🚫) é ruído, ignorado.
> - `Task (Linear)` não é capturado em nenhuma linha — fora do nosso modelo.
> - `Demanda relacionada` do Notion não é confiável (normalmente só tem o nome do cliente, não
>   um ID de demanda) — registrado como veio, sem inventar o vínculo real. `🤿 Demandas de
>   Clientes`, quando preenchido, é guardado como pista para a reconciliação manual futura.
> - RFI multi-cliente (achamos 1 caso, ID 79, "uMode, Lofty Style") — aqui só registro o lado
>   Lofty Style; o lado uMode não tem `_rfis/` no nosso modelo (RFI sempre precisa de um
>   cliente do lado Cliente) — fica como observação em aberto, não bloqueia nada agora.

## Observações abertas
- ID 79 é a única RFI multi-cliente encontrada em Lofty (uMode + Lofty Style) — o texto da
  narrativa (quando tivermos acesso) deve esclarecer se faz sentido ter uma contraparte do
  lado uMode ou se o registro em Lofty já é suficiente.
- Nenhuma das 15 RFIs de Lofty está no status "RFI Aceita — Criar Demanda e Estimar Entrega"
  — status documentado no protocolo mas ainda sem exemplo real observado.
- `Valor negociado com o cliente` às vezes vem como faixa livre (ex.: "24k+6.5k", "6-9k") em
  vez de valor fechado — registrado como veio.

---

## RFI (ID legado Notion: 22)
- Nome: Lofty | RFI : Escopo - Integração de Imagens de Produto
- Status: RFI Stand By
- Cliente(s): Lofty Style
- Resumo do assunto: Integração de Imagens de Produto - da uMode para Linx
- Horas estimadas: vazio
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 0,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 29 de outubro de 2025
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 29 de outubro de 2025 16:49
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Integração de Imagem uMode para LinxO time da Lofty cadastra imagens dos produtos na tela FOTO dentro do cadastro de PRODUTO ACABADO do Linx. Querem que a uMode envie as imagens conforme as categorias abaixo para essa tela.
  - Categorias de ImagemCategorias de imagem para integração cadastradas:- foto desenho/ficha de desenvolvimento- peça piloto- peça lacre - frente- peça lacre - costas- peça lacre - avesso frente- peça lacre - avesso costas- peça lacre - aviamento
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 21)
- Nome: Lofty | RFI : Escopo - Integração de Imagens de MP
- Status: RFI Stand By
- Cliente(s): Lofty Style
- Resumo do assunto: Integração de Imagens de MP - do Linx para uMode
- Horas estimadas: vazio
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 0,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 29 de outubro de 2025
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 29 de outubro de 2025 16:49
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Integração de Imagem Linx para uModeO time da Lofty cadastra imagens de materiais (tecidos e aviamentos) no Linx. Querem que a uMode receba as imagens cadastradas no Linx para o banco de imagem dos materiais na base de cadastro.
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 28)
- Nome: Lofty | RFI : Escopo - Alteração Integração
- Status: RFI Entregue ao Cliente
- Cliente(s): Lofty Style
- Resumo do assunto: Ajustes integração: varia custo cor e fator de conversão
- Horas estimadas: 16
- Valor negociado com o cliente: R$ 2.544
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 4.800,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 15 de dezembro de 2025
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: vazio
- Criado por: Marina Santoro
- Criado em: 25 de novembro de 2025 11:44
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Integração de Escrita - Varia Custo CorFizemos uma alteração na forma dos custos dos produtos e precisamos mapear um campo que temos no Linx (varia custo cor) e que hoje não temos na uMode.Movida para RFI Lofty | RFI: Escopo - Alteração de Regra para Custos de Variante [EM RASCUNHO] 
  - Integração de Leitura - MateriaisIncluir informação de fator de conversão nos materiais. ✅
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 33)
- Nome: Lofty | RFI : Escopo - Integração de Imagens de Produtos (Armário 1)
- Status: RFI Cancelada
- Cliente(s): Lofty Style
- Resumo do assunto: Integração de Imagens de Produtos (Armário 1) - do Linx para uMode 
- Horas estimadas: vazio
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 0,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 4 de dezembro de 2025
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 4 de dezembro de 2025 11:36
- Motivo do cancelamento: Cancelado por falta de atualização no assunto. Se for relevante, criamos uma nova demanda.
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Integração de Imagem Linx para uModeO time da Lofty quer trazer para uMode as imagens dos produtos do Armário 1 do Inverno 2026 já cadastrados no Linx antes da uMode para olharem a coleção inteira na uMode.
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 51)
- Nome: Lofty | RFI: Escopo - Alteração de Regra para Custos de Variante
- Status: RFI Post Mortem
- Cliente(s): Lofty Style
- Resumo do assunto: Alteração de Regra para Custos de Variante 
- Horas estimadas: 20
- Valor negociado com o cliente: R$ 2.544
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': 🎁 - ignorado)
- Valor calculado: R$ 6.000,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 5 de fevereiro de 2026
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 26 de janeiro de 2026 14:56
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - PRECO99 da tabela PRODUTO_PRECO_CORAtualmente mandamos o valor da primeira variante e aplicamos o mesmo valor para todas as variantes do produto. A alteração é aplicar em cada variante do Linx o custo respectivo conforme está na aba de variantes, coluna custo da plataforma.Ajustar integração para preencher o custo de cada variante no campo PRECO_LIQUIDO1 (99) e PRECO1 (99) da tabela PRODUTOS_PRECO_COR.4hO racional de média de custo de mão de obra (fornecedor) se mantem como está. A alteração é não aplicar o valor da primeira variante para todos e sim cada variante com seu custo individual.
  - Custo 1 e campo VARIA_CUSTO_CORNa tela de Controle de Custo da ficha do produto, estávamos mandando o valor da primeira variante para o campo Custo 1. A alteração é:1) Não enviar custo para o campo CUSTO_REPOSICAO1 da tabela PRODUTOS. 4hMantem integrando com tabela PRODUTOS? Mas e quando o produto tiver mais de uma variante, qual valor devemos levar? A demanda inicial era não integrar mais em PRODUTOS mas sim em PRODUTOS_CORES. 
  - 2) Preencher o custo de cada variante na coluna CUSTO_REPOSICAO1 da tabela PRODUTO_CORES.4h
  - 3) “Flegar” o campo VARIA_CUSTO_COR sempre como TRUE.4h
  - Custos diferentes por varianteO time de importado sinalizou que no mesmo produto podem ter custos diferentes por variante, porém hoje não temos onde aplicar essa diferença na plataforma. Os custos que integramos até então são a soma de mão de obra (custo do fabricante) com os custos dos materiais empenhados na ficha técnica. Produtos importados não tem ficha técnica, logo não há onde diferenciar os custos do fornecedor por variante.Esse caso é mais comum no importado mas também pode acontecer no produto acabado nacional.4h@Ju Ferré Precisamos refinar esse ponto. Se for o caso, tiramos da RFI.Incluir campo custom/preco_custo_variante na integração. Se o campo custom/preco_custo_variante estiver preenchido, enviar na integração no lugar do nosso custo da variante padrão. Se for vazio ou zero, mandar o nosso custo por variante padrão do sistema.
  - Anotações reunião 12/03/2026 com MarcelloPRODUTO:
  - CUSTO_REPOSICAO1 → pendente
  - PRODUTO_COR:
  - CUSTO_REPOSICAO1 → Campo da Variante e campo para preço fechado do importado
  - PRODUTO_PRECO_COR:
  - PRECO1 (99) → Campo da Variante
  - PRECO_LIQUIDO1 (99) → Campo da Variante
  - PRODUTO_OPE_EXTRA:
  - CUSTO_OPERACAO → Fornecedores
  - Campo Custo_reposicao1 da tabela Produtos a integração está ok.
  - Campo Custo_reposicao1 da tabela Produto_cores a integração está não ok.
  - Campos Preco1 e Preco_liquido1 da tabela 99 - Produtos_preco_cor não está ok.
  - Campo varia_custo_cor deverá estar 100% flegado.

---

## RFI (ID legado Notion: 52)
- Nome: Lofty | RFI : Escopo - Intervalo de Integração
- Status: RFI Não Aceita
- Cliente(s): Lofty Style
- Resumo do assunto: Aumentar intervalo de funcionamento da integração de escrita
- Horas estimadas: vazio
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 0,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 4 de fevereiro de 2026
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: vazio
- Criado por: Marina Santoro
- Criado em: 5 de fevereiro de 2026 09:31
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Aumentar intervalo de funcionamento da integração de escritaGustavo da Lofty perguntou se é possível aumentarmos o intervalo de funciomento da integração de escrita deles pois o time do PCP inicia o trabalho às 8h e o time de Estilo costuma finalizar fichas até às 20h. O motivo é garantir que processo tudo que foi feito no dia antes do dia seguinte para não travar os times. Hoje nossa integração inicia às 9h e para às 19h. A solicitação dele é que seja das 7h às 21h.Entendo que este processo deve ser mantido padronizado com os clientes, aqui criaremos uma exceção.
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em
- Anexos: Marina_-_perfil.jpg

---

## RFI (ID legado Notion: 61)
- Nome: Lofty | RFI: Escopo - Ajuste do Empenho em Massa
- Status: RFI Cancelada
- Cliente(s): Lofty Style
- Resumo do assunto: Alterar a informação que está zerada no empenho de materiais para não se aplica.
- Horas estimadas: 6
- Valor negociado com o cliente: R$ 954
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 1.800,00
- Data planejada de execução: vazio
- Horas trabalhadas: 1
- Data liberação RFI: 6 de fevereiro de 2026
- Data aceite do cliente: vazio
- Responsável pela RFI: Laura Delgado
- Key Account: Laura
- Criado por: Laura Delgado
- Criado em: 6 de fevereiro de 2026 10:51
- Motivo do cancelamento: Cancelado por falta de atualização no assunto. Se for relevante, criamos uma nova demanda.
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Hoje não conseguimos trazer por importação na parte do empenho o “não se aplica” O Linx recebe consumo por material dentro do produto. Então ou todas as variantes têm o mesmo valor ou o que não tiver é “não se aplica” e inclui a MP separada caso precise ter valor diferente. Precisamos alterar em massa na uFlow todos os consumos que estão “0” para “Não se Aplica” 4h desenvolvimento2h observação 
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 62)
- Nome: Lofty | RFI: Escopo - Revisão Fator de Conversão
- Status: RFI Cancelada
- Cliente(s): Lofty Style
- Resumo do assunto: Rever Fator de Conversão
- Horas estimadas: 16
- Valor negociado com o cliente: R$ 2.544
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 4.800,00
- Data planejada de execução: vazio
- Horas trabalhadas: 1
- Data liberação RFI: 19 de fevereiro de 2026
- Data aceite do cliente: vazio
- Responsável pela RFI: Laura Delgado
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 6 de fevereiro de 2026 17:27
- Motivo do cancelamento: Cancelado por falta de atualização no assunto. Se for relevante, criamos uma nova demanda.
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Unidade de estoque e unidade de ficha técnicaIdentificamos produtos que constavam com erro na integração pois a unidade empenhada no consumo estava divergente da unidade da base de dados. O cliente sinalizou que no Linx existe as duas informações: UNID_ESTOQUE, nossa unidade da base de dados do material; e UNID_FICHA_TEC, usada no empenho do material na ficha técnica do produto. O cliente sinalizou que precisamos trazer a UNID_FICHA_TEC para a base. Exemplo: BLUSA CORNELIA 04.02.0109 - MP 020377Unidade da base (UNID_ESTOQUE): peça (PC)Unidade do empenho (UNID_FICHA_TEC): unidade (UN)8h desenvolvimento8h de Q&A Sugiro trazermos a UNID_FICHA_TEC no fator de conversão. Assim o time pode usar a UNID_ESTOQUE ou UNID_FICHA_TEC no empenho e não teremos erro de integração.
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 79)
- Nome: Lofty/NK/Geral | RFI : Escopo - Custo dinamico
- Status: RFI Em Andamento
- Cliente(s): uMode, Lofty Style (⚠ multi-cliente — ver Observações)
- Resumo do assunto: Tech: Rever regra de empenho sobre custo da mp
- Horas estimadas: 56
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 16.800,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: vazio
- Data aceite do cliente: vazio
- Responsável pela RFI: vazio
- Key Account: Fernanda, Julianne, Laura
- Criado por: Marina Santoro
- Criado em: 17 de março de 2026 16:27
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): uMode,Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Rever regra de empenho sobre custo da mpQuando o custo de material é atualizado no ERP, recebemos o novo valor na uFlow. Ao receber essa atualização no material o custo anterior é inativado e cria-se uma nova variante com o custo atualizado.Para ficha de produto, o material já empenhado não tem o custo atualizado por questão de segurança. 56h

---

## RFI (ID legado Notion: 81)
- Nome: Lofty | RFI : Escopo - Inativar Variantes Canceladas
- Status: RFI Cancelada
- Cliente(s): Lofty Style
- Resumo do assunto: Tech: Mudança de Regra - Inativar Variantes Canceladas
- Horas estimadas: 24
- Valor negociado com o cliente: R$ 7.200
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 7.200,00
- Data planejada de execução: 4 de maio de 2026 → 29 de maio de 2026
- Horas trabalhadas: vazio
- Data liberação RFI: vazio
- Data aceite do cliente: vazio
- Responsável pela RFI: Laura Delgado
- Key Account: Laura
- Criado por: Andrea Holmer
- Criado em: 24 de março de 2026 22:40
- Motivo do cancelamento: Cancelado por falta de atualização no assunto. Se for relevante, criamos uma nova demanda.
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Inativar Variantes CanceladasNecessidade de cancelar variantes para não aparecer nem para venda e nem para transferência. Hoje é realizado o cadastro no Linx, no campo "Fim de Vendas", com uma data, o que bloqueia a venda ou a transferência da cor. Então, precisam registrar na uMode e enviar para o Linx essa informação. É viável usar a Config de Inativar variantes canceladas que foi aplicada na NV? E levar essa info pro Linx?Essa alteração é uma mudança de regra, aprovada em set/25.24h
- Anexos: image 1.png, image.png

---

## RFI (ID legado Notion: 82)
- Nome: Lofty | RFI : Escopo - Macroplan
- Status: RFI Liberada para Comercial negociar com Cliente
- Cliente(s): Lofty Style
- Resumo do assunto: Config de Macroplan 
- Horas estimadas: 10
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 3.000,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: vazio
- Data aceite do cliente: vazio
- Responsável pela RFI: Laura Delgado
- Key Account: Laura
- Criado por: Andrea Holmer
- Criado em: 30 de março de 2026 12:34
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Substituir o ppt da Gabi, que contém imagens dos produtos da coleção agrupados por família, cores, armários, etcDefinido pela Gabi que os modelos de Macroplan da VIX e da CAEDU são adequados ao processo, principalmente o modelo da Linesheet da VIX. Liberado para orçar9h - Incluindo configuração e validação de ordenação e agrupamento.
  - De Acordo
  - Responsável pelo Escopo uMode
  - Responsável pelo Escopo Cliente
  - Aprovado Em 
  - Aprovado Em

---

## RFI (ID legado Notion: 104)
- Nome: Lofty | RFI: Escopo - Custo da Variante com Material por Tamanho
- Status: RFI Liberada para Comercial negociar com Cliente
- Cliente(s): Lofty Style
- Resumo do assunto: Custo da Variante com Material por Tamanho
- Horas estimadas: 30
- Valor negociado com o cliente: 6-9k
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 9.000,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 5 de maio de 2026
- Data aceite do cliente: vazio
- Responsável pela RFI: Ju Ferré
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 5 de maio de 2026 10:55
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Custo da Variante com Material por TamanhoFormação do custo de variante para materiais empenhados por tamanho está errado e requer ajuste manualmente. Isso porque é somado todo material empenhado. Hoje não há uma identificação do que deve ser somado somente 1 vez por ser aplicado por tamanho.1. Ajuste técnico / “gambiarra” = ~12h2. Solução completa / estruturada = ~22hDúvidas: 1) Como identificar o material que deve ser somado e o que não? 2) O que fazer quando os tamanhos possuem custos diferentes? Qual valor considerar: mínimo, máximo ou médio?A formação do custo das variantes deve seguir como é hoje: somatório de mão de obra e empenhos.
  - Cronograma INTERNO de Entrega
  - Até 15/0518/05 até 22/0525/05 até 29/0501/06 até 05/06
  - Aprovação da Demanda🟢
  - Desenvolvimento Tech🟢
  - Testes com Cliente🟢
  - Operação Assistida🟢
  - Encerramento da Demanda🟢
  - Análise Tech
- Subpágina "Análise Tech":
    - INTEG-924 — Estimativa para validação técnica
    - Linear: INTEG-924 RFI completo: docs/integ-924-custo-variante-material-por-tamanho.md Data: 2026-05-08
    - Documento focado em validar a estimativa com outro dev. Resume contexto, mapeamento técnico e premissas. Para o RFI completo (escopo cliente, dúvidas, próximos passos) ver o doc do RFI.Contexto rápido
    - Lofty/Reserva: a formação do custo da variante hoje soma todo material empenhado, sem distinguir o que é aplicado por tamanho (que deveria contar 1 vez só). Usuário corrige manualmente.
    - Dois caminhos discutidos em reunião com cliente (29/04):
    - Ajuste técnico — flag por linha de empenho que define se o material entra no custo da variante. Sem agregação min/max/média (alinhado com Marina Santoro 2026-05-07): usa o valor que está no material marcado.
    - Estruturada — modelo MaterialGroup persistido + CRUD + regra de cálculo por grupo. Premissa: regra fixa = média.
    - Mapeamento técnico (descoberta)
    - A infra de "agrupar e contar 1x" já existe parcialmente:
    - ComponenteOndeO que faz hoje
    - Cálculo centralapp/models/product_variant.rb:215-235 #product_material_for_cost_reportAgrupa por variable_consumption_per_size_group (texto livre) e pega max_by(&:price). Para itens sem grupo, agrupa por material_variant_id e também pega max_by(&:price).
    - Concern por tamanhoapp/models/concerns/consumption_per_size.rbGerencia consumption_values (JSON com 1 valor por tamanho da grade).
    - Campo de agrupamento legadofabric_variant_supplier, accessory_variant_supplier (col variable_consumption_per_size_group)Texto livre, migration 20210212141711.
    - Consumidorapp/reports/product_cost_report.rb:69-117 #calculate_fabrics_cost/#calculate_accessories_costItera o resultado de product_material_for_cost_report e soma.
    - Persistênciaapp/services/product_cost_service.rb:87-95Recálculo + grava em ProductCostSheet.
    - UI ponto naturalapp/views/datasheet/product_materials/edit.html.slim:50-51Já tem checkbox consumption_per_size — flag nova entra ao lado.
    - Não existe hoje: modelo MaterialGroup, regra de agregação configurável (sempre max), CRUD de grupos.
    - Cobertura de specs: baixíssima. spec/models/product_variant_spec.rb cobre parcialmente #product_material_for_cost_report. Não há specs dedicados para ProductCostReport nem ProductCostService.
    - Caminho 1 — Ajuste técnico — \~12h
    - Adicionar flag booleana em cada linha de empenho. Se a flag estiver desligada, o material é ignorado no cálculo do custo da variante. Sem agregação nova.
    - Arquivos afetados
    - db/migrate/<ts>_add_include_in_variant_cost_to_product_materials.rb (novo)
    - app/models/product_fabric_variant.rb, app/models/product_accessory_variant.rb
    - app/reports/product_cost_report.rb:69-117 OU app/models/product_variant.rb:215-235
    - app/views/datasheet/product_materials/edit.html.slim
    - app/views/datasheet/product_materials/_material_row.html.slim
    - app/controllers/datasheet/product_materials_controller.rb (strong params)
    - config/locales/*.yml
    - spec/models/product_variant_spec.rb, spec/reports/product_cost_report_spec.rb (novo)
    - Decomposição
    - FrenteEsforço
    - Migration: include_in_variant_cost boolean default true em product_fabric_variants e product_accessory_variants1h
    - Filtro em ProductCostReport#calculate_* (ou ProductVariant#product_material_for_cost_report) — apenas pula linhas com flag false2h
    - UI: checkbox no _form / _material_row2.5h
    - Strong params0.5h
    - Specs (default, alguns excluídos, todos excluídos)4h
    - I18n pt-BR0.5h
    - Code review + ajustes1.5h
    - Total\~12h
    - Premissas (caminho 1)
    - Flag granular por linha de empenho (cada ProductFabricVariant/ProductAccessoryVariant).
    - Default true → comportamento atual preservado, sem migração de dados.
    - Sem alteração na lógica de variable_consumption_per_size_group ou max_by(&:price) existente.
    - Default por Fabric/Accessory (herança automática) não está incluso — seria +2h.
    - Caminho 2 — Estruturada (MaterialGroup) — \~22h
    - Modela MaterialGroup como entidade persistida, com CRUD enxuto e regra de cálculo fixa em média por grupo.
    - Arquivos
    - Novos: app/models/material_group.rb, app/models/material_group_item.rb, controller Datasheet::MaterialGroupsController, views (index, _form), policy mínima, 2 migrations, specs.
    - Alterados: config/routes.rb, app/models/product_variant.rb:215-235, app/views/datasheet/product_materials/_material_row.html.slim, sidebar/menu.
    - Decomposição
    - FrenteEsforço
    - Migrations (material_groups + material_group_items polymórfico Fabric/Accessory + FKs)1.5h
    - Modelos + associations + validações + scope por entity2.5h
    - Controller CRUD + routes + policy mínima (segue padrão de outros datasheets)3h
    - Views CRUD enxutas (index listando + _form único reusado em new/edit) + entrada no menu4h
    - Refator #product_material_for_cost_report para considerar material_group_id (média por grupo)3h
    - Tela empenho: select do grupo no _material_row.html.slim2h
    - Specs essenciais: model (group + item) + report integrado; controller só smoke happy path5h
    - I18n pt-BR0.5h
    - Code review + ajustes1.5h
    - Total\~22h
    - Premissas (caminho 2)
    - Grupo por entity, material em no máximo 1 grupo (1:N). N:N seria +3-4h.
    - Regra fixa = média. Configurável (min/max/avg) seria +5h.
    - Não migra dados de variable_consumption_per_size_group para os novos grupos. ETL seria +4-6h.
    - CRUD enxuto: sem filtros/busca avançada na lista, sem auditoria, sem soft-delete. Se algum desses for requisito, +3-5h cada.
    - material_group_id novo e variable_consumption_per_size_group legado convivem; novo tem precedência.
    - Resumo
    - CaminhoEstimativaEsforço onde concentra
    - 1 — Ajuste técnico\~12hSpecs (4h) + UI (2.5h)
    - 2 — Estruturada (enxuta)\~22hSpecs (5h) + Views (4h) + Controller (3h) + Refator (3h)
    - Estimativas cobrem dev + specs. Não incluem QA manual, migração de dados, discovery adicional.
    - @marina.santoro

---

## RFI (ID legado Notion: 110)
- Nome: Lofty | RFI: Escopo - EnriqueceAI + Integração Vtex
- Status: RFI Pronta para Estimar
- Cliente(s): Lofty Style
- Resumo do assunto: Enriquecimento automático de catálogo (SEO + GEO) com validação por agente de IA, em fluxo VTEX → uMode → VTEX, sem intervenção humana no fluxo principal.
- Horas estimadas: 80
- Valor negociado com o cliente: 24k+6.5k
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 24.000,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: 15 de maio de 2026
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 15 de maio de 2026 14:19
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Leitura de produto na VTEXuMode consome produtos diretamente da VTEX da Lofty, identificando quais estão pendentes de enriquecimento. Frequência de leitura e gatilho (webhook VTEX, polling ou batch) a definir em projeto.Necessário confirmar com Lofty: (a) o produto já está publicado para o consumidor no momento da leitura ou entra em rascunho/oculto; (b) se há webhook VTEX disponível ou se exigirá polling; (c) qual o identificador canônico utilizado (SKU, EAN, GTIN, RefId).
  - Credencial VTEX para leitura e escritaProvisionamento de appKey e appToken dedicados, na conta VTEX da Lofty, com permissão mínima necessária para os endpoints de catálogo, mídia e SEO.uMode já possui produto que integra VTEX (leitura/escrita) e domina as regras da plataforma. Owner da credencial do lado Lofty a definir, assim como política de rotação e revogação.
  - Enriquecimento SEO + GEOAplicação do motor uMode para gerar/ajustar título, descrição, categoria, tags e demais campos relevantes para SEO e GEO, a partir do conteúdo bruto disponível na VTEX.Mapeamento de campos VTEX vs. campos exigidos pelo enriquecimento a ser detalhado. Limitações de tamanho, formato e encoding por campo a confirmar.
  - Validação por agente de IACada produto enriquecido passa por avaliação de agente de IA que atribui um score de confiança. O score é comparado contra threshold de qualidade e piso mínimo, gerando três caminhos (publica direto / publica com flag / bloqueia).Valores de threshold e piso mínimo serão definidos em conjunto com a Lofty durante a fase de homologação. uMode recomenda calibragem inicial com amostragem manual antes do go-live.
  - Publicação automática e flag de revisãoProdutos com score acima do threshold publicam automaticamente sem flag. Produtos entre piso mínimo e threshold publicam com flag indicando necessidade de ajuste fino posterior. Produtos abaixo do piso ficam bloqueados.Necessário definir: (a) onde a flag fica registrada (campo customizado VTEX, sistema externo uMode, ambos); (b) quem consome a fila de flags (Lofty, uMode, terceiro); (c) SLA de tratamento da fila.
  - Fila de revisão e ajuste finoProdutos sinalizados (com flag ou bloqueados) entram em fila para revisão e ajuste fino das descrições. Critério de priorização, ferramenta e responsável a definir.uMode pode fornecer interface de revisão ou apenas a fila estruturada. Decisão impacta escopo e horas. A confirmar com Lofty se o ajuste fino é feito pela Lofty, pela uMode ou compartilhado.
  - Logs e auditoriaRegistro de todas as decisões do agente de IA (score, faixa, ação tomada, timestamp) para auditoria posterior e calibragem do modelo.Retenção, ferramenta de armazenamento e nível de acesso da Lofty aos logs a definir. Mínimo recomendado: 12 meses.
  - Ambiente de homologação e go-liveExecução do fluxo end-to-end em ambiente VTEX não-produção (sandbox da Lofty) antes do go-live, com calibragem do threshold e piso mínimo do agente de IA via amostragem.Confirmar existência de ambiente sandbox VTEX da Lofty. Definir critério de aceite (volume de amostra, taxa de aceite mínima, prazo de homologação).
  - Volumetria e SLADimensionamento do fluxo conforme volume atual e projetado de produtos do catálogo Lofty. Definição de latência máxima aceitável entre leitura na VTEX e republicação enriquecida.Volume atual de SKUs, taxa de novos/alterados por dia e latência aceitável a ser fornecida pela Lofty. Impacta diretamente a arquitetura (síncrono vs. assíncrono, dimensionamento de fila).
  - Contexto
  - A Lofty contratou a uMode para automatizar o enriquecimento de seu catálogo de produtos na VTEX, utilizando a solução proprietária da uMode de SEO + GEO, com validação por agente de IA antes da republicação.
  - Por solicitação da Lofty, o fluxo foi ajustado em relação à proposta inicial: a uMode lê o produto diretamente da VTEX (não mais da Synthese), executa o enriquecimento, submete ao agente de IA e devolve o conteúdo enriquecido para a própria VTEX.
  - Regra de operação do agente de IA
  - O agente de IA avalia o score de confiança de cada enriquecimento e classifica em três faixas, com piso mínimo a ser definido em tempo de projeto:
  - Faixa de scoreAção na VTEXTratamento posterior
  - Acima do threshold de qualidadePublica automaticamenteNenhum — produto considerado pronto
  - Entre piso mínimo e threshold de qualidadePublica automaticamente + flag de revisãoEntra em fila de ajuste fino para revisão posterior
  - Abaixo do piso mínimoBloqueia publicaçãoVai para fila de revisão crítica; não publica até intervenção
  - Os valores numéricos do threshold de qualidade e do piso mínimo serão definidos em tempo de projeto, em conjunto com a Lofty, com calibragem durante a fase de homologação.
  - Itens fora do escopo desta RFI
  - Pricing, modelo comercial e contrato (objeto de tratativa comercial separada).
  - LGPD, certificações, criptografia e auditoria de segurança detalhada (fase posterior).
  - Reconciliação de catálogo legado e tratamento histórico.
  - Estoque e integração com marketplaces (B2W, Mercado Livre, etc.).
  - Treinamento, ajuste fino do modelo de IA, dataset proprietário (escopo separado).
  - Synthese — saiu do fluxo conforme orientação da Lofty.

---

## RFI (ID legado Notion: 113)
- Nome: Lofty | RFI: Escopo - Campo Família - Integrado com o Linx
- Status: RFI Liberada para Comercial negociar com Cliente
- Cliente(s): Lofty Style
- Resumo do assunto: Integrar o campo família com o Linx (Escrita)
- Horas estimadas: 6
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 1.800,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: vazio
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Laura Delgado
- Criado em: 22 de maio de 2026 16:05
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Campo Família - Integrado com linx• Campo Família - Ele não foi mapeado no início do projeto. Time Lofty alinhou internamente e definiu que vai ser preenchido pelo estilo e vamos levar pro Linx. ◦ Objetivo: Fazer uma junção dos produtos (por cor) para poder produzir a mesma quantidade. ◦ Campo já criado dentro de variante (Campo de Seleção) ◦ No Linx será um campo de Texto, na uMode um campo de seleção. ◦ Projeto daqui pra frente, pois não tem histórico controlado em nenhum sistema disso.4h Tech + 2h Ops
  - Demanda: Campo Família - Integrado com linx

---

## RFI (ID legado Notion: 118)
- Nome: Lofty | RFI: Escopo - Alterações na integração de escrita
- Status: RFI Pronta para Estimar
- Cliente(s): Lofty Style
- Resumo do assunto: Sobreescrever grupo e subrgupo quando atualizado na uFlow e tirar toda a integração relacionada a custos e preços
- Horas estimadas: 4
- Valor negociado com o cliente: vazio
- Cobrada? (sim/não): vazio (bruto Notion campo 'Cobrada?': vazio - ignorado)
- Valor calculado: R$ 1.200,00
- Data planejada de execução: vazio
- Horas trabalhadas: vazio
- Data liberação RFI: vazio
- Data aceite do cliente: vazio
- Responsável pela RFI: Marina Santoro
- Key Account: Laura
- Criado por: Marina Santoro
- Criado em: 3 de julho de 2026 12:46
- Motivo do cancelamento: vazio
- Demanda relacionada (bruto Notion, não confiável): Lofty Style
- Pista (🤿 Demandas de Clientes): vazio
- Conteúdo / narrativa:
  - Um RFI - Request For Information é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
  - Demanda ClienteDetalhamento ClienteEstimativa uMode(se a estimativa for maior que 10 horas, detalhar os motivos)Comentário uMode
  - Insert e update em GRUPO e SUBGRUPOIncluir UPDATE nos campos grupo e subrgupo quando atualizados na uFlow.2h
  - Não integrar PREÇOS/CUSTOSNão integrar nenhum campo relacionado a custo ou preço em nenhuma tabela Linx.2h