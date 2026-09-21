# NK STORE · Pessoas

> **Reescrito em 21 set 2026 a partir do Notion ao vivo.** Campo sem fonte fica `[a preencher]`.
>
> 🟢 **É o cliente mais bem documentado da carteira em pessoas:** 13 nomes com cargo,
> hierarquia de projeto declarada e financeiro e TI nomeados.
>
> 🚨 **A página de origem contém CPF e telefone pessoal de duas pessoas físicas, e uma
> credencial de banco de produção em texto plano. Nada disso foi copiado para cá** — aqui ficam
> nome, cargo e e-mail corporativo, que é o dado de negócio.
> Ver o alerta em [`institucional.md`](institucional.md).

## Responsável de atendimento (uMode)
- **2025:** **Julianne & Pedro** — dupla que atende **6 contas**: NK STORE, Caedu, Puket, VIX,
  Osklen e Loungerie.
- **2024:** duas pessoas registradas como relação, **nomes não resolvidos** — `[a preencher]`

**Outras pessoas da uMode citadas na conta:**
**Taís** e **Sandro** — foram a São Paulo para o kick-off presencial ·
**Nayra** — comprou as passagens ·
**Marina** — citada num chamado de melhoria de 29/01/2026.

## Diretoria e decisores

| Pessoa | Papel | E-mail |
|---|---|---|
| **Alexandre de Sá Pereira** | Representante legal | `alexandre.sa@nkstore.com.br` |
| **Gustavo Annechino de Souza e Almeida** | Representante legal | `gustavo.annechino@nkstore.com.br` |
| **Regiane Konopka** | **Diretora de Merchandising** — responde por **Compras, Industrial e Compliance**. **Diretoria responsável pelo projeto.** | `regiane.konopka@nkstore.com.br` |
| **Stella Sunaga** | **Diretora de Estilo** — **10 anos na empresa** | `stella.sunaga@nkstore.com.br` |

## Liderança do projeto (cliente)

> **Declarada na página, com hierarquia explícita.** É o único cliente varrido com isso.

**Diretoria responsável:** **Regiane Konopka** — Diretora de Merchandising.

**Líderes responsáveis pelo projeto:**

| Pessoa | Papel | E-mail | Observação da origem |
|---|---|---|---|
| **Larissa Cid Castilho Batista** | **Gerente de Projeto** · Gerente de Produto | `larissa.castilho@nkstore.com.br` | *"Já implantou PLM em várias empresas"* |
| **Marina Sacramento** | **PMO** · Time de Compras, Compradora de Produtos Acabados | `marina.sacramento@nkstore.com.br` | é a fonte do desenho de processo da conta |

> 🟢 **A Larissa já implantou PLM antes.** Isso é informação operacional de primeira ordem
> para o atendimento — **muda o nível de explicação necessário** — e está registrada na origem
> como nota solta. **É exatamente o tipo de contexto que o BrainHub existe para não perder.**

## Time do projeto por área

> **Fonte:** o item *"Confirmar departamentos envolvidos"* da reunião de warm-up de **19/06**,
> marcado como concluído — **acordo de reunião, não inferência.**

| Área canônica | Departamento | Pessoas |
|---|---|---|
| `01_Planejamento` | Planejamento | **Bruna** — Coordenadora do Planejamento |
| `02_Estilo-Criacao` | Estilo | **Stella Sunaga** (Diretora) · **Samuel** (Coordenador) · **Julia** (Coordenadora) |
| `05_PCP` | PCP | **Robson Bazan** — Gerente Industrial · **Andressa** — Coordenadora |
| `06_Compras-Supply-Sourcing` | Compras | **Marina Sacramento** — Compradora de Produtos Acabados |
| ⚠ `[a preencher]` | **Merchandising** | **Regiane Konopka** — Diretora |
| — (área da Casa) | Tecnologia | **Hermes Gonçalves Santiago Junior** — Gerente de TI |
| 🔴 **sem área canônica** | **Oficina** | `[a preencher]` — produção interna |
| ⚠ sem área canônica | **Curadoria** | `[a preencher]` — compra de produto acabado de marca parceira |

### 💡 A observação mais útil da página inteira
Sobre a **Andressa**, Coordenadora do PCP, a origem registra:

> *"(Se ela está feliz com o projeto, estamos bem)"*

**É um termômetro de adoção nomeado numa pessoa.** Não é anotação casual — é conhecimento
operacional que normalmente vive só na cabeça de quem atende, e que **se perde na primeira
passada de bastão**.

## Estado de atividade das pessoas

### Como o estado é apurado

> **Uma pessoa não é ativa porque tem cadastro. É ativa porque agiu, numa data que dá para citar.**
> Este eixo existe para a jornada do usuário: **quem atende o quê, em qual ferramenta, em qual área.**

| Estado | O que significa | Evidência que o sustenta |
|---|---|---|
| `ATIVO` | agiu no sistema numa data conhecida | chamado aberto, presença em ata, ação registrada |
| `CADASTRADO` | tem acesso, **sem** evidência de ação | consta na tabela de usuários e em nenhum canal |
| `DESATIVADO` | baixa declarada **na origem** | riscado, marcado inativo, acesso revogado |
| `ATIVO_SEM_CADASTRO` | agiu, mas **não consta** na lista de usuários | e-mail em chamado sem linha na tabela |
| `INDETERMINADO` | citado sem identificador único | nome solto em ata, sem e-mail |

**`CADASTRADO` não é `INATIVO`.** Ausência de evidência é hipótese, nunca conclusão.
**Todo estado carrega a data da evidência.** **`DESATIVADO` só com marcação na fonte.**

### 🔴 O achado: quem está documentado e quem usa o sistema são dois grupos quase disjuntos

**13 pessoas** estão nomeadas com cargo na página. **10 pessoas** abriram chamado em jan/2026.
**A interseção provável é de uma só** — e nem essa é certa.

| | Quem é | O que a fonte sabe |
|---|---|---|
| **Documentados** | diretoria, gerência, coordenação, PMO, TI | **cargo, hierarquia, e-mail** — e **nenhuma evidência de uso** |
| **Ativos** | quem abre chamado no dia a dia | **e-mail e data** — e **nenhum cargo, nenhuma área** |

> **O brain sabe o organograma e sabe quem usa o sistema — e são pessoas diferentes.**
> Documentação de projeto captura **liderança**; chamado captura **operação**.
> **Nenhuma das duas sozinha responde "quem atende o quê".**
>
> É a demonstração mais limpa de por que `person_memberships` precisa de `activityState` **e**
> de `accessProfile` ao mesmo tempo, na
> [`_espec-pessoas-e-comunicacoes.md`](../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md).

### 🔴 Cinco achados que só apareceram ao descer um nível

**1 · A Gerente de Projeto está marcada para ser inativada.**
**Larissa Castilho** — nomeada na página como **Gerente de Projeto**, com a observação
*"já implantou PLM em várias empresas"* — aparece na base de usuários com
`Departamento NK = INATIVAR`. **A pessoa que lidera o projeto do lado do cliente está na lista de
desligamento de acesso.** Se ela saiu, **a conta perdeu quem entendia de PLM**, e a página do
cliente **não foi atualizada**. `[a preencher]` — **confirmar com urgência.**

**2 · `Departamento NK = INATIVAR` é instrução de trabalho gravada como dado.**
Cinco pessoas têm `INATIVAR` no lugar do departamento. **Não é um departamento — é uma tarefa
pendente escrita no campo errado.** E o campo `Status` de quatro delas ainda diz
`CONVITE ACEITO`. **Só uma foi efetivamente inativada.**
> **É exatamente o que a espec resolve:** `activityState` derivado, mais `deactivatedAt` como
> campo próprio — em vez de sobrecarregar `departamento` com uma ordem de serviço.

**3 · Dois convites nunca aceitos, há 21 meses.**
`gabriela.rocin` (12/12/2024) e `kemelly.fernandes` (16/12/2024), ambas com
`Nome = "(Não definido)"`. **Licença alocada e nunca usada.**

**4 · A matriz de permissão e a base de usuários usam perfis diferentes.**

| Onde | Perfis |
|---|---|
| **Matriz de permissão** (validada em 04/12) | `NK - Admin` · `NK - Time` · `NK- Estilo Master` · `Nk Compras Master` · `Nk Modelagem` · `NK Compras` · `Fornecedor` |
| **Base de usuários** (o que foi atribuído) | `NK - Admin` · `NK - Estilo` · `NK - PCP` · `NK - Compras` · `NK - Modelagem` |

> **`NK - Time` e os perfis `Master` foram desenhados e não aparecem em ninguém.
> `NK - Estilo` e `NK - PCP` existem em gente e não aparecem na matriz.**
> **O desenho e a implantação divergiram, e nenhum dos dois documentos sabe disso.**

**5 · A dor de "cadastrar opção" é permissão por desenho, não defeito.**
A matriz marca 🔴 **"não visualiza e não edita"** para **novo fornecedor**, **nova cor**,
**nova grade** e **nova mp** — **tanto para `NK - Admin` quanto para `NK - Time`**. E marca 🟡
"somente visualizar" para Tecido, Aviamento, Fornecedor e Campo Personalizado.

> 🔴 **Isso reenquadra um achado anterior.** Na NV eu registrei *"o cliente não consegue
> cadastrar opção de campo custom"* como **restrição observada**. Aqui ela está **documentada como
> decisão de desenho**: o cliente é deliberadamente impedido de criar dado mestre.
>
> **O modelo de permissão que protege a qualidade do dado mestre é o que gera o volume de
> chamado.** Não é bug nem mau uso — **é o custo operacional de uma escolha de governança**, e
> ninguém mediu esse custo. Na NV foram **5 chamados em 10 dias** só para isso.

**Bônus · `NK - Admin` não pode falar com o suporte.**
A matriz marca 🔴 em **"Fale com o Suporte"** para Admin e Time. **Todo contato passa por
fora da plataforma** — o que explica por que os chamados chegam por e-mail e chat.

### A matriz do perfil `Fornecedor`
🔴 em praticamente tudo. 🟢 apenas em **Notificações**, **Editar Usuário**, **Sair**,
**Tarefa homepage** e **Tarefa ficha**.
> **O fornecedor entra para executar tarefa e não enxerga nada do produto** — nem Meus Produtos,
> nem Lotes, nem Mapa de Coleção, nem custo. **Confere com a trava comercial registrada na CAEDU**
> (fornecedor vê propriedades do produto exceto campos de custo e preço) — aqui é ainda mais restrito.

### Razão de pessoas

**32 pessoas** no razão: **28 na base de usuários** do cliente + **4 que abriram chamado sem constar nela**.

`CADASTRADO` **19** · `ATIVO` **6** · `ATIVO_SEM_CADASTRO` **4** · `INDETERMINADO` **2** · `DESATIVADO` **1**

> 🟢 **Esta é a única conta varrida cuja fonte declara o estado da pessoa.** A base `Usuários`, escondida dentro de *Perfil de Usuário e Permissionamentos*, traz `Status` com **"USUÁRIO INATIVO desde…"**, **"CONVITE ACEITO em…"** e **"CONVITE PENDENTE desde…"**, mais `Departamento` e `Perfil` por pessoa.
>
> **É exatamente o modelo que a [`_espec-pessoas-e-comunicacoes.md`](../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) especifica** — e ele **já existe, num cliente só, feito à mão.**

#### `Estilo` — 6 pessoa(s) · área canônica: 02_Estilo-Criacao

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| Stella Sunaga | `stella.sunaga@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 12/12/2024, sem evidência de ação | **Diretora de Estilo**, 10 anos de casa |
| Julia Leone | `julia.leone@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 18/12/2024, sem evidência de ação | **Coordenadora de Estilo** (a *"Julia"* da página) |
| Thais | `thais.cerqueira@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 12/02/2025, sem evidência de ação | — |
| Moreno Ribeiro | `moreno.ribeiro@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 13/02/2025, sem evidência de ação | — |
| Ana Ribeiro | `ana.ribeiro@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 27/02/2025, sem evidência de ação | — |
| Sam | `sam.santos@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 10/03/2025, sem evidência de ação | **Coordenador de Estilo** (o *"Samuel"* da página) |

#### `PCP` — 6 pessoa(s) · área canônica: 05_PCP

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| Andressa Correa | `andressa.correa@nkstore.com.br` | `NK - PCP` | `ATIVO` | **2 chamado(s)** até 2026-01-28 · acesso desde 12/12/2024 | **Coordenadora do PCP** — *"se ela está feliz com o projeto, estamos bem"* |
| Beatriz Nunes | `beatriz.nunes@nkstore.com.br` | `NK - PCP` | `CADASTRADO` | convite aceito em 12/12/2024, sem evidência de ação | — |
| Laís | `lais.batista@nkstore.com.br` | `NK - PCP` | `ATIVO` | **3 chamado(s)** até 2026-01-23 · acesso desde 12/12/2024 | — |
| Caroline Silva | `caroline.silva@nkstore.com.br` | `NK - PCP` | `ATIVO` | **9 chamado(s)** até 2026-01-29 · acesso desde 23/01/2025 | — |
| ROSANA RIBEIRO DA SILVA CAMPOS | `rosana.campos@nkstore.com.br` | `NK - PCP` | `CADASTRADO` | convite aceito em 23/01/2025, sem evidência de ação | — |
| Milena Machado | `milena.machado@nkstore.com.br` | `NK - PCP` | `CADASTRADO` | convite aceito em 27/01/2025, sem evidência de ação | — |

#### `Compras` — 6 pessoa(s) · área canônica: 06_Compras-Supply-Sourcing

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| Cristina | `cristina@nkstore.com.br` | `NK - Admin` | `ATIVO` | **2 chamado(s)** até 2026-01-28 · acesso desde 12/12/2024 | — |
| Heloisa Lima | `heloisa.lima@nkstore.com.br` | `NK - Compras` | `CADASTRADO` | convite aceito em 12/12/2024, sem evidência de ação | — |
| Isabely Consul Dantas | `isabely.consul@nkstore.com.br` | `NK - Compras` | `ATIVO` | **6 chamado(s)** até 2026-01-28 · acesso desde 12/12/2024 | — |
| Negrita Moreira Candido | `negrita.candido@nkstore.com.br` | `NK - Compras` | `CADASTRADO` | convite aceito em 12/12/2024, sem evidência de ação | — |
| Nelson Tadeu Alves Ferreira | `expedicao2@nkstore.com.br` | `NK - Compras` | `CADASTRADO` | convite aceito em 06/01/2025, sem evidência de ação | — |
| (Não definido) | `kemelly.fernandes@nkstore.com.br` | `NK - Compras` | `INDETERMINADO` | ⚠ **convite pendente desde 16/12/2024** — nunca aceito | — |

#### `Modelagem` — 4 pessoa(s) · área canônica: 13_Modelagem

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| Cristina | `cristina.amorim@nkstore.com.br` | `NK - Modelagem` | `CADASTRADO` | convite aceito em 08/01/2025, sem evidência de ação | — |
| Vanessa | `vanessa.oliveira@nkstore.com.br` | `NK - Modelagem` | `CADASTRADO` | convite aceito em 15/01/2025, sem evidência de ação | — |
| Silvia | `silvia.nascimento@nkstore.com.br` | `NK - Modelagem` | `CADASTRADO` | convite aceito em 15/01/2025, sem evidência de ação | — |
| Vitoria Fernanda | `fernanda.coelho@nkstore.com.br` | `NK - Modelagem` | `CADASTRADO` | convite aceito em 15/01/2025, sem evidência de ação | — |

#### `TI` — 1 pessoa(s) · área canônica: — (área da Casa)

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| Nathalia Gomes | `nathalia.gomes@nkstore.com.br` | `NK - Admin` | `ATIVO` | **2 chamado(s)** até 2026-01-23 · acesso desde 05/12/2024 | TI |

#### `INATIVAR` — 5 pessoa(s) · área canônica: —

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| Larissa Castilho | `larissa.castilho@nkstore.com.br` | `NK - Admin` | `CADASTRADO` | convite aceito em 12/12/2024, sem evidência de ação | 🔴 **Gerente de Projeto** — *"já implantou PLM em várias empresas"* |
| Júlia Fontoura | `julia.fontoura@nkstore.com.br` | `NK - Estilo` | `CADASTRADO` | convite aceito em 12/12/2024, sem evidência de ação | — |
| Lucas Gabriel de Oliveira Alves de Souza | `lucas.souza@nkstore.com.br` | `NK - PCP` | `CADASTRADO` | convite aceito em 23/01/2025, sem evidência de ação | — |
| (Não definido) | `gabriela.rocin@nkstore.com.br` | `NK - Estilo` | `INDETERMINADO` | ⚠ **convite pendente desde 12/12/2024** — nunca aceito | — |
| Vanessa Veiga | `vanessa.ventura@nkstore.com.br` | `NK - Estilo` | `DESATIVADO` | **inativo desde 10/03/2025**, declarado na origem | — |

#### Abriram chamado e **não estão** na base de usuários

| Pessoa | E-mail | Perfil | Estado | Evidência | Cargo conhecido |
|---|---|---|---|---|---|
| `[a preencher]` | `carolina.teixeira@nkstore.com.br` | — | `ATIVO_SEM_CADASTRO` | **1 chamado(s)**, 2026-01-29–2026-01-29 | — |
| `[a preencher]` | `kauane.boska@nkstore.com.br` | — | `ATIVO_SEM_CADASTRO` | **2 chamado(s)**, 2026-01-13–2026-01-23 | — |
| `[a preencher]` | `lilian.pereira@nkstore.com.br` | — | `ATIVO_SEM_CADASTRO` | **1 chamado(s)**, 2026-01-16–2026-01-16 | — |
| `[a preencher]` | `mariana.bastos@nkstore.com.br` | — | `ATIVO_SEM_CADASTRO` | **2 chamado(s)**, 2026-01-06–2026-01-09 | — |

> ⚠ **A base de usuários foi criada em 13/03/2025 e a última data nela é de 10/03/2025.** Os chamados são de **jan/2026** — dez meses depois. **A base parou de ser mantida**, e essas quatro pessoas são a prova.

## Canais de comunicação

> **Cada canal é uma entidade** — tem participantes, cadência, dono e assunto. É por aqui que a
> indexação do cérebro liga pessoa ↔ ferramenta ↔ área.

| Canal | Ferramenta | Quem participa | Cadência | Último registro |
|---|---|---|---|---|
| Chamados | Notion — `Chamados & Atendimentos` | **10 pessoas** do cliente | alta | **29/01/2026** |
| Reuniões com Cliente | Notion (base própria) | `[a preencher]` | `[a preencher]` | **não varrida** |
| Demandas · Demandas NK · Análise de Demandas | Notion | `[a preencher]` | — | **não varridas** |
| Kick-off interno | presencial/remoto | Taís, Sandro, time uMode | único | **18/06/2024** |
| Warm-up com cliente | remoto | diretoria + liderança dos dois lados | único | **19/06/2024** |
| Kick-off presencial | presencial, em SP | liderança + times | único | **28/06/2024** |
| Material Gerencial Diretoria | Notion | → diretoria | — | **maio/2025**, não varrido |
| Treinamento Go Light uFlow | Google Slides | time do cliente | — | **não capturado** |
| Plano de Sucesso do Cliente | Google Drive | `[a preencher]` | — | **não capturado** |
| Drive de operação | Google Drive | `[a preencher]` | — | **não capturado** |
| **Sessão de IA em reunião** | **Tactiq** · **Gemini** · **ChatGPT** | time uMode | pontual | **jun/2024** |

> 🔴 **Ferramentas de IA são canal de fato nesta conta.** O desenho de processo do cliente foi
> produzido por **Tactiq** e **Gemini** dentro de uma reunião, e os **OKRs do projeto saíram de
> uma conversa no ChatGPT**, com o link salvo na página.
>
> **Isso é dado sobre o método da casa, não só sobre o cliente** — e significa que **parte do
> contexto institucional já nasce em transcrição de IA**, que é precisamente o insumo do projeto
> paralelo de transcrições.
>
> ⚠ **Nenhum canal além do Notion é legível pelo BrainHub.**

## Financeiro
- **Responsável: Silvia Shirlei Dias** — `silvia.dias@nkstore.com.br`
- **E-mail principal financeiro:** `financeiro@nkstore.com.br`
- **Receita anual declarada:** **R$ 144.000.000**
- Inscrição estadual e CNPJ constam na origem; CNPJ `07870440000149`.

> 🟢 **É o único cliente varrido com o financeiro nomeado e o e-mail preenchido.**

## Tecnologia
- **Responsável: Hermes Gonçalves Santiago Junior** — Gerente de TI — `hermes.junior@nkstore.com.br`
- **ERP `Linx`**, com bancos de **homologação e produção** separados.
- 🚨 **A credencial de acesso ao banco de produção está em texto plano na página do Notion.**
  **Não foi copiada.** Ver o alerta em [`institucional.md`](institucional.md) — **exige rotação.**
- **Integração de escrita com dúvidas pendentes desde 29/05/2025** — documento próprio, não varrido.

## Governança
### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| 13 pessoas com cargo, hierarquia, financeiro, TI | Notion — corpo da página `NK STORE` | **varrido 21/09/2026** |
| Departamentos confirmados | Notion — ata do warm-up de 19/06 na página | **varrido 21/09/2026** |
| 10 pessoas com evidência de ação | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Atendimento e receita | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |

> **CPF, telefone pessoal e credencial de banco existem na fonte e NÃO foram copiados.**
