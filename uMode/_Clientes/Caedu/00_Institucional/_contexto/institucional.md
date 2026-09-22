# Caedu · Institucional

> **Atualizado em 21 set 2026 por varredura do Notion ao vivo.** A versão anterior vinha de um
> export de CRM de **05 mar 2026** e estava desatualizada em status, módulos e contagem de usuários.
> Todo campo sem dado na fonte está como `[a preencher]` — nada foi inferido.

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
> Há a referência de ~R$ 1 bi (2023) no CRM de mentoria, **não confirmada**. Não usar como dado.
### Grupo de segmentação uMode
`[a preencher]` — o campo mudou de tipo na base viva (virou relação) e não trouxe valor na consulta.
> O export antigo trazia "Grupo 3: Potenciais Clientes", **classificação incompatível com um
> cliente em `Ongoing`** — provável resíduo. Reconfirmar com o Comercial.

## Operação uMode
### Status atual
**Ongoing**
> Valor da base `Mapa de Clientes` em 21/09/2026, dentro do enum vigente
> (`Inativo` · `Pré Onboardings` · `Operação Assistida` · `Onboarding` · `Sem CS` · `Ongoing` ·
> `Churn`). **Substitui o `Regime CS` do export de março**, que era valor de um enum anterior.
### Data de ativação
`[a preencher]` — campo vazio na base.
> A conta de API está ativa **desde 05/10/2022** e o usuário mais antigo é de **21/07/2023**.
> São os indícios mais firmes de quando a operação começou.
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
