---
aliases:
  - "Caedu · Institucional"
tags:
  - tipo/institucional
  - cliente/caedu
  - status/ongoing
---
# Caedu · Institucional

> **Atualizado em 21 set 2026 por varredura do Notion ao vivo.** A versão anterior vinha de um
> export de CRM de **05 mar 2026** e estava desatualizada em status, módulos e contagem de usuários.
> Todo campo sem dado na fonte está como `[a preencher]` — nada foi inferido.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- id: caedu — [export de CRM · 2026-09-21]
- segmento: B2C — Vestuário, Calçados, Acessórios — São Paulo/SP — [export de CRM · 2026-09-21]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- grupo-segmentacao: SMB — [varredura do Notion · 2026-09-23]
- status: Ongoing — [base Mapa de Clientes · 2026-09-21]
- data-ativacao: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
- erp: Linx — [base Mapa de Clientes · 2026-09-21]
- modulo-contratado: Gestão de Coleção — [export de CRM · 2026-09-21]
- modulo-contratado: Integração — [export de CRM · 2026-09-21]
- modulo-contratado: Relatórios — [export de CRM · 2026-09-21]
- modulo-contratado: Fornecedores — [export de CRM · 2026-09-21]
- contrato-situacao: Assinado — [planilha de contratos do Financeiro · 2026-09-23]
- servico-faturado: uFlow — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-vigencia: 2022-06-23 → 2027-06-23 — [planilha de contratos do Financeiro · 2026-09-23]
- contrato-renovacao: Renovação Automática · aviso prévio 90 dias — [planilha de contratos do Financeiro · 2026-09-23]
- indice-reajuste: IGPM / IPCA — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-contratados: 65 internos + 100 externos — [planilha de contratos do Financeiro · 2026-09-23]
- usuarios-conta: 93 usuários com e-mail na tabela do PLM, em 14 perfis de acesso — [export de CRM · 2026-09-21]
- atendimento: pessoa:julianne.dias@umode.com.br — [export de CRM · 2026-09-21]
- atendimento: pessoa:pedro.murillo@umode.com.br — [export de CRM · 2026-09-21]
- atendimento: pessoa:andrea.holmer@umode.com.br — [export de CRM · 2026-09-21]
- tamanho-atendimento: P — [base Mapa de Clientes · 2026-09-23]

## Identidade
### ID do cliente
caedu
> Slug estável derivado do nome no CRM. **Não muda** se o nome comercial mudar — é a chave lógica
> deste cliente; o nome da pasta é só apresentação.
### Aliases do cliente
- Caedu (base `Mapa de Clientes` — nome canônico)
- CAEDU (grafia usada em atas e RFIs)
### Quem são
Varejista de moda popular brasileira.
> **100+ lojas, ~R$ 1 bi de faturamento (2023). CEO: Edson Salles.**
> ⚠ Fonte: ficha de CRM do projeto de mentoria no vault do João (21/05/2026). **Não confirmado por
> fonte do atendimento** — validar antes de usar em comunicação ou proposta.
### O que fazem
Desenvolvimento e varejo de vestuário, calçados e acessórios, com operação em **produto nacional e
importado**. Departamentos atendidos: **Feminino, Masculino e Infantil**.
### Para quem fazem
`[a preencher]` — nenhuma fonte varrida descreve o público-alvo da Caedu.

## Posicionamento
### Segmento
B2C — **Vestuário, Calçados, Acessórios** — São Paulo/SP
### Receita anual
`[a preencher]` — campo **vazio** na base `Mapa de Clientes`.
> 🔴 **Ausência VERIFICADA em dois instantes independentes**, em 23/09/2026:
> a base viva (consulta SQL) e o **export de 04/03/2026** que está no vault do João
> (`BrainHub/uMode/_Clientes/_geral/notion/Mapa de Clientes.csv`). **Vazio nos dois.**
> 🔴 **E o campo quase não é usado: está preenchido em 2 dos 49 clientes** — só
> Luiza Barcelos (350.000.000) e NK STORE (144.000.000). **Não é lacuna da Caedu: é campo
> que a operação não preenche.**
>
> ⚠ **A referência de ~R$ 1 bi (2023) continua SEM fonte localizável.** O corpus a atribui
> ao *CRM de mentoria no vault do João*. **Não encontrei `Edson Salles`, `1 bi` nem
> `100+ lojas` na árvore do vault nem no histórico do Git dele** (busca de 23/09/2026).
> ⚠ **O clone tem 1 branch local contra 19 remotas** — pode estar em branch não baixada.
> **Não afirmo que não existe: afirmo que não encontrei ali.** Não usar como dado.
>
> ⚠ **`Quantidade de Lojas` também está vazio para a Caedu** — preenchido em 5 de 49.
> A afirmação de *100+ lojas* não vem da base.
### Grupo de segmentação uMode
**`SMB`** — **Grupo 3** da base `Segmentação Grupos`. `WIP Time 10` · `WIP Estratégico 1,75`.
> 🟢 **Lido ao vivo em 23 set 2026**, resolvendo a relação (o campo é `relation`, não texto — foi
> por isso que a consulta anterior voltou vazia).
> 🔺 **Derruba a hipótese que estava escrita aqui.** O corpus supunha que "Grupo 3" fosse resíduo
> de export antigo. **Não é: é a classificação viva da conta.**
> 🔴 **E ela contradiz o porte.** A própria fonte do Notion descreve a CAEDU como *varejista de
> moda popular, 100+ lojas, ~R$1bi de faturamento (2023)* — e `SMB` é a faixa de menor alocação
> de time (`WIP Estratégico 1,75` contra `6` do `Enterprise`). **Com o projeto CAEDU 2.0 em
> montagem e a conta em `Onboarding`, a segmentação subdimensiona a carga.** Ver
> `_pendencias-gerais.md`.

## Operação uMode
### Status atual
**Ongoing**
> Valor da base `Mapa de Clientes` em 21/09/2026, dentro do enum vigente
> (`Inativo` · `Pré Onboardings` · `Operação Assistida` · `Onboarding` · `Sem CS` · `Ongoing` ·
> `Churn`). **Substitui o `Regime CS` do export de março**, que era valor de um enum anterior.
### Data de ativação
`[a preencher]` — campo vazio na base `Mapa de Clientes`.
> 🔴 **Ausência VERIFICADA em dois instantes**, em 23/09/2026: base viva e export de
> 04/03/2026 no vault. **Vazio nos dois.** O campo está preenchido em **6 dos 49 clientes**.
>
> 🟢 **Mas a data é CERCAVÉL por duas fontes independentes, e elas concordam:**
> · **contrato assinado em 23/06/2022** (planilha de contratos do Financeiro);
> · **conta `api-caedu@umode.app` ativa desde 05/10/2022** — a linha mais antiga da tabela
> de usuários da página do cliente, com folga: **a seguinte é de 05/05/2023.**
>
> ⚠ **Não promovi nenhuma das duas a `data-ativacao`.** Contrato assinado e conta de serviço
> criada **não são** o campo comercial `Data Ativação Cliente`. **A janela está cercada entre
> jun e out de 2022; o valor exato continua sem fonte.**
>
> 🟢 **Janela de atividade medida na tabela de usuários** (94 linhas de pessoa, lida em
> 23/09/2026): mais antiga **05/10/2022**, mais recente **16/07/2024**.
> 🔴 **Nenhum usuário novo desde jul/2024** — e a conta está em `Onboarding` com o
> projeto CAEDU 2.0 em montagem.
>
> 🔴 **13 das 94 linhas têm data corrompida na origem:** ano `0202` em vez de `2022`
> (`alessandra.rocha`, `bianca.werneck`, `brida.duch`, `maria.vietas`, `karina.gaino`,
> `marina.bueno`, `marlon.ribeiro`, `nathalia.kassai`, `sofia.costa`), ano truncado `20`
> (`jose.soares`, `samara.santos`) e sufixo ` 1` (`ana.queiroz`, `leticia.santos`).
> **É erro de digitação na fonte — corrigir lá, não aqui.**
### Módulos contratados
- **Gestão de Coleção**
- **Integração**
- **Relatórios**
- **Fornecedores**

> ⚠ **A taxonomia de módulo mudou na fonte.** Deixou de ser nome de produto (`uFlow`, `uBuy`) e
> passou a ser funcional. O export de março dizia apenas `uFlow`; a base viva lista os quatro acima.
### Usuários da conta
**93 usuários** com e-mail na tabela do PLM, em **14 perfis de acesso**.
> Contagem feita por extração da tabela de usuários em 21/09/2026. O CRM de março registrava 96
> usuários ativos — **diferença de 3 não explicada**; pode ser desativação ou critério distinto.
### ERP / Integração
**Linx**
> Confirmado em duas fontes independentes: base `Mapa de Clientes` e a existência do fluxo de
> integração no mapeamento de conta.
### Responsável de atendimento (uMode)
**Dupla de atendimento 2025: Julianne & Pedro**
- Julianne Dias Rodrigues — Key Account
- Pedro Murillo — Key Account
- Andrea Goulart Holmer dos Santos — Consultor de Negócios

## Contrato

`[a preencher]` — 🔴 **A autoridade deste bloco é a base de contratos do Financeiro**, não o Notion. Ver `_recebido-2026-09-23-base-contratos-flavia-campello.md`.

### Situação do contrato
**Assinado** — serviços faturados: `uFlow`.
### Vigência
**2022-06-23 → 2027-06-23** · vigência 5 anos
### Renovação e aviso prévio
Renovação **Automática** · aviso prévio **90 dias**
### Índice de reajuste
IGPM / IPCA
### Usuários contratados
65 internos + 100 externos
### Pendências contratuais registradas
🔴 **Checar nova quantidade de usuários + quando haverá reajuste inflação**

> Texto literal do campo `OBS` da planilha de contratos. **Não interpretei.**
## Aliases de áreas
### Mapeamento alias → canônico

> **Preenchido em 21 set 2026.** A fonte é o **perfil de acesso no PLM** — é o único vínculo
> pessoa↔área que existe em alguma fonte da uMode hoje.

| Alias no cliente (perfil no PLM) | Pessoas | Área canônica |
|---|---:|---|
| `Caedu-Estilo` | 31 | `02_Estilo-Criacao` |
| `Gerente de Estilo / Caedu-Estilo` | 5 | `02_Estilo-Criacao` |
| `Caedu-Produto` | 22 | `03_Desenvolvimento-de-Colecao` |
| `Caedu- Planejamento` ⚠ | 8 | `01_Planejamento` |
| `Caedu-Modelagem` | 4 | `13_Modelagem` |
| `Caedu-Qualidade` | 2 | `04_Qualidade` |
| `Caedu-E-commerce` | 1 | `08_Ecommerce-Cadastro` |
| `Caedu-Geral` · `Caedu-Geral + TM` · `Gerente de Estilo / Caedu-Geral` | 10 | **transversal — não derivável** |
| `Caedu-Gerentes` · `Gerente de Estilo / Caedu-Gerentes` | 6 | **transversal — gerência** |
| `Caedu-Admim` ⚠ | 3 | **transversal — administração** |
| `Dono da Conta` | 1 | conta de serviço (API), **não é pessoa** |
| `Fornecedor` · `Fornecedor-Jinrra` | — | externo · `06_Compras-Supply-Sourcing` |

⚠ **Dois erros de digitação na origem:** `Caedu- Planejamento` (espaço a mais) e `Caedu-Admim`
(deveria ser *Admin*). **Corrigir na fonte, não aqui.**

🔴 **Sete das 14 áreas canônicas não têm perfil de acesso correspondente:** PCP, Logística,
Comercial, Marketing, Financeiro, Design e Engenharia. **É lacuna estrutural real** — ou a área não
existe na Caedu, ou existe e não usa o PLM.

## Sistemas e fontes de verdade
### Drive de operação
https://drive.google.com/drive/folders/13uGFpXtLsMEZGwr_0H5YEEWcw_zFMhVu?usp=drive_link
### Outras fontes
- **Notion — página `Caedu`** em `uMode Geral / Databases / Mapa de Clientes`: tabela de usuários,
  Ficha de Produto, Manual do Cliente PLM, Playbooks, Onboarding→Ongoing, Fornecedores da Caedu,
  e **mais de 50 atas** de weekly e alinhamento, de 2024 a 2025.
- **Notion — `Mapeamento de Contas - Caedu`** (AS IS / TO BE, 04/04/2025), em
  `Operação de Clientes / Área de CX / Documentação CX`.
- **vault do João** — `_Clientes/caedu/`: proposta de 12 meses e cronograma de transição PLM 2.0,
  mais o export `FORMS.csv` e uma ata destilada de visita (28/07).
- **Linear** — projetos da conta (ex.: *Atualização de Produtos via Script [RFI 65]*,
  *Relatório Mega Line*).
- OKRs (CRM de março): https://miro.com/app/board/uXjVNk43Dt0=/
- Chamados/Atendimento: **"Sistema saiu do ar"** (registro do CRM de março) — reconfirmar.

## Contexto crítico

### 🔴 A CAEDU está em reimplantação, não em operação normal

**A implantação começou em 2022.** No pré-kickoff de **03/09/2026**, o próprio cliente disse:
> *"**quatro anos** para o processo ainda não está totalmente [pronto]"* ·
> *"a maior frustração que a gente tem hoje é **não tirar todo o potencial**"* ·
> *"se a gente quiser continuar alguma coisa, **tem que ser diferente**"*

**E o diretor admitiu, em 28/07:** *"a implantação não foi boa, eu sei que do meu lado tem um
monte de problema"*.

> 🔴 **É uma conta em reconquista de confiança.** A própria Vanessa nomeou:
> *"vai passar por um processo de **reconquista de confiança do time**"*, e registrou que
> **o time interno pressionava o diretor para encerrar**.

⚠ **Valor de contrato e mensalidade existem nas fontes e ficam com marcação
`NEVER_TO_THIRD_PARTY`** no registro [[_recebido-2026-09-22-caedu-2.0-proposta-e-transcricoes]]. **Não replicados aqui.**

### Onde estamos
> uFlow em regime. Onboarding apenas para a etapa de acesso aos fornecedores, pendente retorno da
> Caedu. **Modelagem e qualidade têm domínio da ferramenta**, porém os demais times ainda têm
> dificuldade em seguir alguns processos. Foram configurados workflows novos, mais automatizados.

### 🔴 A frente aberta
> **Fechar a etapa de fornecedores com a inclusão dos 4 primeiros na plataforma e testes.**

É a única frente declarada em aberto na conta. Detalhamento, matriz de permissão do perfil
`Fornecedor` e ajustes pendentes em
[`06_Compras-Supply-Sourcing/_contexto/contexto-area.md`](../../06_Compras-Supply-Sourcing/_contexto/contexto-area.md).

### O que o cliente espera
> Melhorar o produto em configurações e usabilidade na área de **modelagem e qualidade**, para gerar
> mais agilidade ao time.

### As dores estruturais registradas

> Fonte: mapeamento de conta de **abr/2025** — **17 meses**, precisa de revalidação.
1. **Time de calçados não usa a plataforma** — gera lacuna de dados.
2. **Dados sensíveis de pedido e negociação ficam fora da uMode**, em planilhas.
3. **12 mil cadastros de fornecedor** — dificulta busca e usabilidade.
4. **Macroplan subutilizado** — risco de *overlap* entre nacional e importado.
5. 🔴 **A origem do produto vive na ficha, não na variante** — e como a validação é por variante,
   isso obriga exportações extensas no mapa. **É problema de modelo de dado, não de processo.**

### Tamanho de atendimento
P (base `Mapa de Clientes`, março/2026 — reconfirmar)
> 🔴 **O campo `Tamanho atendimento` NÃO EXISTE MAIS na base `Mapa de Clientes`** — verificado em 23/09/2026: o schema da base viva tem 23 propriedades e nenhuma delas é essa. ⚠ **`P` vem do export de 04/03/2026.**
> **Campo removido da origem, não campo vazio.** 🔴 **Não é reconfirmável na base de hoje.**

## Governança
### Responsável de atendimento (uMode)
Julianne Dias Rodrigues e Pedro Murillo (Key Account) · Andrea Goulart Holmer dos Santos
(Consultor de Negócios)
### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode
### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Status, módulos, ERP, dupla, setor, cidade | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |
| Usuários, perfis, aliases de área | Notion — página `Caedu`, tabela do PLM | **varrido 21/09/2026** |
| Dores, fluxo, "onde estamos" | Notion — `Mapeamento de Contas - Caedu` | 04/04/2025 |
| Porte e CEO | vault do João — CRM EducAI | 21/05/2026 · **não confirmado** |

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Caedu`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)


**Registros:** **26 demandas** — [índice](../_demandas/_indice.md) · **4 RFIs** — [índice](../_rfis/_indice.md) · **100 fichas de pessoa** — [índice](../_pessoas/_indice.md)

**As 14 áreas deste cliente:**

- [Planejamento](../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../02_Estilo-Criacao/_contexto/contexto-area.md)
- [Desenvolvimento de Colecao](../../03_Desenvolvimento-de-Colecao/_contexto/contexto-area.md)
- [Qualidade](../../04_Qualidade/_contexto/contexto-area.md)
- [PCP](../../05_PCP/_contexto/contexto-area.md)
- [Compras Supply Sourcing](../../06_Compras-Supply-Sourcing/_contexto/contexto-area.md)
- [Logistica CD](../../07_Logistica-CD/_contexto/contexto-area.md)
- [Ecommerce Cadastro](../../08_Ecommerce-Cadastro/_contexto/contexto-area.md)
- [Comercial Vendas](../../09_Comercial-Vendas/_contexto/contexto-area.md)
- [Marketing](../../10_Marketing/_contexto/contexto-area.md)
- [Financeiro](../../11_Financeiro/_contexto/contexto-area.md)
- [Design](../../12_Design/_contexto/contexto-area.md)
- [Modelagem](../../13_Modelagem/_contexto/contexto-area.md)
- [Engenharia](../../14_Engenharia/_contexto/contexto-area.md)

**Autoridades da Casa que governam este arquivo:**
[`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md) · [`_espec-pessoas-e-comunicacoes.md`](../../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) · [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
