# Varredura 23 set 2026 (b) — o playbook da Cambos nasceu de transcrição, e há um terceiro domínio de documentação

> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**
>
> Veio de procurar `Databases / Processos mapeados`, uma das fontes que eu listava como não
> varrida. **Não cheguei a ela — cheguei ao que a busca por ela revelou.**

## 0 · O que este registro NÃO resolve

- 🔴 **`Databases / Processos mapeados` continua NÃO varrida.** A busca devolveu uma página
  dela (`Solicitações de demandas de Clientes em Regime [V1 - em validação]`) e eu **não abri**.
- 🔴 **`playbook.umode.app` não foi acessado.** Sei que existe porque uma página do Notion o
  cita. **Não sei o que há lá.**
- 🔴 **O teamspace `AGENTES E PROJETOS` inteiro não foi varrido.**
- ⚠ **Abri UMA página nesta rodada**, o playbook da Cambos. Tudo o mais aqui é **o que a busca
  mostrou do lado de fora**, e está marcado como tal.

## 1 · 🟢 A uMode já transformou transcrição de treinamento em playbook, com IA

`Documentação Homologada › Playbook Cambos | Treinamento > IA + Doc Laura` `[C]`

> **PLAYBOOK — SISTEMA PLM [CAMBOS]** · Versão **1.1 (Consolidada)** · **23 de março de 2026**
> · *"Baseado em: **Transcrições de Treinamento** e Documentação Técnica de Operações."*

🔴 **É exatamente o caminho que o Vinicius anunciou para as ~50 transcrições da CAEDU — e ele
já rodou uma vez, aqui, há seis meses.** ⚠ **O título nomeia o método: `Treinamento > IA + Doc
Laura`.**

🆕 **A pasta se chama `Documentação Homologada`.** ⚠ **O nome implica um estado de validação
que o corpus não tem como classe.** **Não sei quantos clientes têm essa pasta.**

## 2 · 🔴 A Cambos é FORNECEDORA de marcas — e o corpus a tratava como marca

No guia de uso do Mapa de Coleção, a fonte escreve:

> *"**Filtros:** use para isolar clientes específicos (**ex: Riachuelo**)."* `[C]`

🔴 **A Riachuelo é cliente DA Cambos, dentro da conta da Cambos.**

**O que isso explica de uma vez:**

| Achado anterior | Leitura nova |
|---|---|
| `Novo Pedido (só a Cambos tem)`, construído e desligado | **pedido de cliente-marca faz sentido em confecção, não em varejo** |
| o perfil `Atacado` | **é o canal, não uma área solta** |
| as abas renomeadas `COSTURA E BORDADO`, `FABRICAÇÃO (Fornecedor)` | **vocabulário de quem produz, não de quem vende** |

⚠ **Não mudei a classificação da conta.** **Registro a evidência e pergunto.**

## 3 · 🔴 A Cambos tem duas operações geográficas

| Frente | O que faz |
|---|---|
| **Comercial** | inicia o produto na pasta **COTAÇÃO**, preenche dados básicos e comerciais |
| **Desenvolvimento SP** | cadastro e associação do **`Produto Original`** — o acervo de bases de modelagem |
| **Desenvolvimento MG** | **`Aprovações das Pilotos`** — lacres, pesos e pontuações |

🔴 **O campo `Liberado para Desenv. MG` é o gatilho entre as duas**, e dispara a automação
`#1175`, que **cria a Piloto automaticamente.**

⚠ **O corpus não tinha nenhuma das duas frentes**, e `15_Producao-Interna` acabou de ganhar uma
oitava evidência.

## 4 · 🔴 Cinco automações com ID — o corpus não tinha nenhuma

| ID | O que faz |
|---|---|
| **`#1136`** | gera a descrição concatenando **Modelagem + Gênero + Tipo + Tamanho + Detalhe** |
| **`#1175`** | **cria a Piloto automaticamente** quando `Liberado para Desenv. MG` é marcado |
| **`#1134`** | valida os pré-requisitos de `Liberado para Integração?` |
| **`#989`** | **validação técnica ao entrar em coluna específica do workflow** |
| **`#1135`** | campo de **limpeza da última integração SPI**, para evitar duplicidade |

> 🟢 **São regras de negócio com identificador estável.** ⚠ **Não sei onde vive o catálogo
> dessas automações** — se é o admin, se é código, se é uma base do Notion.

## 5 · A trava do SPI, e os dois códigos

| Código | Quem gera | Vale quando |
|---|---|---|
| **`Código uMode`** | a plataforma | **até a aprovação do orçamento** |
| **`Código SPI`** | o ERP, pela integração | depois |

> 🔴 **Depois que o `Código SPI` nasce, os campos `Modelagem`, `Tipo`, `Gênero` e `Tamanho`
> ficam TRAVADOS para edição.** `[C]`

**É a primeira regra de ciclo de vida de campo que o corpus registra.** ⚠ **E ela vem do ERP,
não do PLM.**

### 5.1 · 🔴 Na integração, só a ÚLTIMA variante é enviada

> *"Cada variante (versão) refere-se a uma pilotagem específica. Na integração, apenas a
> informação da **última variante** é enviada."* `[C]`

⚠ **É perda de informação por desenho.** E liga direto com a dor de variante que aparece em
cinco clientes — **desta vez do lado da integração, não da permissão.**

## 6 · 🟢 Uma regra de playbook encontrou uma `entity_config`

| Onde | O que diz |
|---|---|
| Playbook Cambos § 5.2 | *"Apenas usuários **Admin** podem criar exibições 'Compartilhadas'"* |
| Manual do Permissionamento | **`hide_map_template`** — *"excluir o botão de exibições para determinados perfis"* |

> 🟢 **É a primeira vez no corpus que a regra escrita para o cliente e o mecanismo que a
> implementa aparecem ligados.** **A ponte entre o "o quê" e o "como" existe, e dá para
> percorrer.**

## 7 · Vocabulário de moda que o corpus não tinha

| Termo | O que é |
|---|---|
| **`Lacre`** | identificador da amostra física vinculada à aprovação técnica. **O sistema registra até 6**, com seus tamanhos |
| **`Produto Original`** | acervo de bases de modelagem, mantido pelo Desenvolvimento SP |
| **`Pilotagem`** | cada variante refere-se a uma pilotagem específica |
| Tipos de aprovação | **Piloto · Lavanderia · Liberação de Produção · Mostruário** |

⚠ **`Lavanderia Jeans`** aparece como restrição: observações de lavanderia são **restritas ao
time técnico**, o Comercial não edita.

## 8 · ⚠ O playbook fala de 2 perfis; a matriz tem 5

| Fonte | Perfis |
|---|---|
| Playbook § 3, 23/03/2026 | **`Comercial`** e **`Admin`** |
| Matriz de permissão, 2026 | **5 perfis** |

**Não sei qual dos dois está desatualizado.** ⚠ **E o playbook é o documento mais recente que
descreve quem faz o quê.**

## 9 · 🔴 O próprio playbook deixa três pendências escritas, sem dono

1. **Relatórios de Gestão** — verificar se `Gestão de Coleção` e `Tarefas` já estão liberados
   para o perfil operacional
2. **Migração de Histórico** — confirmar se os `Produtos Originais` antigos **que estão em
   planilhas** serão importados ou se o controle começa do zero
3. **Gatilho MG** — validar se a criação automática da piloto pelo `#1175` vale para **todo
   tipo de produto ou só jeans**

> ⚠ **Escritas em 23/03/2026. Seis meses. Nenhuma tem responsável nem data.**

## 10 · 🔴 Um TERCEIRO domínio de documentação, e um TERCEIRO acervo por cliente

### 10.1 · Os domínios

| Domínio | Onde apareceu |
|---|---|
| `docs.umode.app` | Lofty Style — 🔴 **e é onde está a credencial exposta** |
| `documentacao.umode.tech` | `Operation Hub`, registro `(l)` |
| 🆕 **`playbook.umode.app`** | página **`Engenharia de Software`** (`dc5980a5…`), em `uMode Geral` |

⚠ **A página que o cita foi editada em 07/09/2026 — quinze dias atrás.** E diz que o conteúdo
é *"de atendimento obrigatório para todos os membros do time, independentemente do nível de
senioridade"*. 🔴 **Não acessei.**

### 10.2 · Os acervos por cliente

| Acervo | Estado |
|---|---|
| `Databases / Mapa de Clientes` | 🟢 é por onde a varredura anda |
| `uFlow / Documentação de Setup - PLM / CLIENTES` | ⚠ achado em 22 set; **só a NV foi tocada** |
| 🆕 **`Operação de Clientes / Área de CX / Documentação CX / Mapeamento de Contas`** | 🔴 **não varrido** — a Puket tem página lá |
| 🆕 **`Documentação Homologada`**, dentro do cliente | ⚠ vista na Cambos. **Não sei quem mais tem** |

> 🔴 **Quatro lugares onde documentação de cliente pode estar.** ⚠ **Nenhum documento do corpus
> dizia isso até agora, e é a causa mecânica de eu procurar no lugar certo e não achar.**

### 10.3 · E o teamspace dos mentorados existe

🆕 **`AGENTES E PROJETOS`**, com `Templates & Boas Práticas`, **`Projeto: Mentoria (João
Risoléo)`** e `Metodologia MBS`.

> 🟢 **O Vinicius anunciou que traria "os mentorados". O acervo já existe.** 🔴 **Não varrido.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1–§9 | Notion — `Cambos › Documentação Homologada › Playbook Cambos \| Treinamento > IA + Doc Laura` (`32cb1d38…`), **aberta por inteiro** | **23 set 2026** |
| §6 | cruzamento com [`_dicionario-permissionamento-uflow.md`](_dicionario-permissionamento-uflow.md) § 6.3 | **23 set 2026** |
| §10 | Notion — busca por `Processos mapeados playbook`, 10 resultados. ⚠ **Nenhuma dessas páginas foi aberta: o que está aqui é título, caminho e trecho de destaque** | **23 set 2026** |
