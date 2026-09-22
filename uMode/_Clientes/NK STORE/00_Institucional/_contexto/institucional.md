# NK STORE · Institucional

> **Reescrito em 21 set 2026 a partir do Notion ao vivo.** Campo sem fonte fica `[a preencher]`.

> ## 🚨 ALERTA DE SEGURANÇA — ação necessária, 21 set 2026
>
> A página `NK STORE` no Notion contém, num bloco recolhido chamado **"Conexão com Linx"**,
> uma **credencial de banco de dados de produção em texto plano**: usuário, senha, IP, porta e os
> nomes dos bancos de homologação e de produção do cliente.
>
> **O valor NÃO foi copiado para este repositório, nem para log, nem para nenhum relatório** — o
> `CLAUDE.md` proíbe segredo em nota, e uma credencial já exposta no `STATE.md` teve de ser
> redigida e rotacionada antes.
>
> **O que precisa acontecer:**
> 1. **Rotacionar a senha** do usuário de integração no ERP do cliente.
> 2. **Remover o bloco da página** e mover a credencial para um gerenciador de segredos.
> 3. **Checar as outras contas** — se o padrão se repete, é problema de processo, não de página.
> 4. **Avaliar exposição**: qualquer pessoa com acesso ao Notion da uMode consegue ler o banco de
>    produção de um cliente.
>
> **A página também contém CPF e telefone pessoal de duas pessoas físicas.** Também **não foram
> copiados**. Aqui ficam apenas nome, cargo e e-mail corporativo — que é o dado de negócio.

## Identidade
### ID do cliente
`nk-store`

### Aliases do cliente
`NK STORE` · `NK` · razão social **TALIE IND E COM IMP E EXPORT CONF E ACES LTDA** ·
domínio `nkstore.com.br` · site `www.nkstore.com.br`

### Quem são
**Varejo de moda, em São Paulo (SP).** CNPJ `07870440000149`.
Endereço: Rua Sarandi, 34 — Cerqueira César, São Paulo/SP.

> 🟢 **É o cliente mais bem documentado da carteira.** Tem razão social, CNPJ, inscrição
> estadual, endereço, receita, **data de ativação**, financeiro nomeado, **12 pessoas com cargo**,
> **10 dores mapeadas**, definição de sucesso e três reuniões de kick-off datadas.

### O que fazem
Operação com **dois fluxos distintos**, descritos na própria página:

1. **Merchandising** — desenvolvimento próprio: `Planejamento → Estilo → Compras/Merchandising
   → PCP → Oficina`
2. **Curadoria** — `Planejamento → Curadoria`: seleção e compra de **produto acabado de marcas
   parceiras**

> ⚠ **Esse fluxo foi produzido por IA dentro de uma reunião** (ferramentas *Tactiq* e *Gemini*),
> a partir da fala da **Marina Sacramento**. **Não é documento validado pelo cliente** — está
> registrado porque é o único desenho de processo que existe, e **marcado como não validado**.

### Para quem fazem
**Varejo** — lojas físicas e site. `[a preencher]` o peso de cada canal.

## Posicionamento
### Segmento
**Varejo** · Área de atuação: **Moda**.

### Receita anual
**R$ 144.000.000** — declarado na base.

> 🟢 **É o único cliente varrido com receita preenchida.**

### Grupo de segmentação uMode
**`Médios`** — Grupo 2. `WIP Time 10` · `WIP Estratégico 2,25`.

## Operação uMode
### Status atual
**`Ongoing`** — lido na base em 21/09/2026.

### Data de ativação
**10/06/2024** — 🟢 **o único cliente varrido com `Data Ativação Cliente` preenchida.**

Bate com a sequência de kick-off registrada na página: **18/06** (kick-off interno),
**19/06** (warm-up com o cliente) e **28/06** (kick-off presencial).

### Módulos contratados
`Gestão de Coleção` · `Integração` · `Relatórios` · `Fornecedores` — **4 de 7**.

### Usuários da conta
`[a preencher]` — **não há tabela de usuários do PLM na página.**

> Existe um documento **"Perfil de Usuário e Permissionamentos"**, **não varrido**, que é a fonte
> mais provável da lista.
>
> **10 pessoas** aparecem abrindo chamado em jan/2026, e **12 estão nomeadas com cargo** na
> página — mas **os dois conjuntos quase não se sobrepõem**. Ver [`pessoas.md`](pessoas.md).

### ERP / Integração
**`Linx`** — com bancos de **homologação e produção** separados.
🚨 **Credencial exposta na página de origem** — ver o alerta no topo.

Há um documento **"NK | Dúvidas Pendentes Integração de Escrita (29/05/2025)"**, **não varrido** —
o título indica que **a integração de escrita tem pendências em aberto desde maio de 2025**.

### Responsável de atendimento (uMode)
- **2025:** **Julianne & Pedro** — dupla que atende **6 contas**: NK STORE, Caedu, Puket, VIX,
  Osklen e Loungerie.
- **2024:** duas pessoas registradas como relação, **nomes não resolvidos** — `[a preencher]`

**Outras pessoas da uMode citadas:** **Taís** e **Sandro** (foram a SP para o kick-off) ·
**Nayra** (comprou as passagens) · **Marina** (citada num chamado de melhoria).

## Aliases de áreas
### Mapeamento alias → canônico

> **Fonte:** o item *"Confirmar departamentos envolvidos"* da reunião de warm-up de **19/06**,
> marcado como concluído — **é acordo de reunião, não inferência**. Mais os cargos nomeados.

| Departamento confirmado | → Área canônica | Quem lidera |
|---|---|---|
| `Planejamento` | `01_Planejamento` | **Bruna** — Coordenadora do Planejamento |
| `Estilo` | `02_Estilo-Criacao` | **Stella Sunaga** — Diretora de Estilo |
| `Merchandising` | ⚠ **`[a preencher]`** — ver abaixo | **Regiane Konopka** — Diretora de Merchandising |
| `PCP` | `05_PCP` | **Robson Bazan** (Gerente Industrial) e **Andressa** (Coordenadora) |
| `Tecnologia` | — **é área da Casa, não do cliente** | **Hermes Gonçalves Santiago Junior** — Gerente de TI |

**Também citados no fluxo de processo**, sem confirmação em reunião:
`Compras` → `06_Compras-Supply-Sourcing` · `Curadoria` → ⚠ sem área canônica ·
`Oficina` → 🔴 **sem área canônica**.

### 🔴 `Oficina` não cabe na grade — e é a segunda vez

A NV declara **`Atelier`**; a NK STORE descreve **`Oficina`** como etapa final do fluxo próprio.
**São a mesma coisa: produção interna.** E **nenhuma das 14 áreas canônicas a cobre** — há
`13_Modelagem` e `14_Engenharia`, mas nenhuma área de **produção própria**.

> **Dois clientes independentes, a mesma lacuna.** Deixa de ser caso isolado.
> **A grade de 14 áreas precisa de uma décima quinta?** Afeta 46 clientes — **decisão do
> Vinicius `[D]`, não minha.**

### ⚠ `Merchandising` e `Curadoria` também exigem decisão
A **Regiane** é Diretora de Merchandising e responde por **Compras, Industrial e Compliance** —
três escopos que caem em áreas canônicas diferentes. **Não decidi.**
`Curadoria` — compra de produto acabado de marca parceira — **também não tem área**.

## Sistemas e fontes de verdade
### Drive de operação
Pasta registrada — `1g7o8IA7bu4oks4dM4PsF--iq8GihTz4m`. **Não varrida.**

### Outras fontes
| Fonte | Ferramenta | Estado |
|---|---|---|
| **Perfil de Usuário e Permissionamentos** | Notion | 🔴 **não varrido — provável lista de usuários** |
| **NK \| Dúvidas Pendentes Integração de Escrita (29/05/2025)** | Notion | 🔴 **não varrido** |
| NK \| Análise de Demandas · Demandas NK | Notion | **não varridas** |
| NK \| Criar Item da Rota/Beneficiamento | Notion | **não varrido** |
| NK \| Material Gerencial Diretoria (Maio 2025) | Notion | **não varrido** |
| NK \| Ficha de Produto Completo | Google Sheets | **não varrida** |
| NK \| Base de Upload Importação | Google Sheets | **não varrida** |
| NK \| Material Treinamento Go Light uFlow | Google Slides | **não varrido** |
| Apresentação de kick-off | Google Slides | **não varrida** |
| Plano de Sucesso do Cliente | Google Drive | **não varrido** |
| Reuniões com Cliente · Demandas | Notion (bases) | **não varridas** |
| `Chamados & Atendimentos` | Notion | ✅ **varrida — 30 chamados, 10 pessoas** |
| `Mapa de Clientes` · `Segmentação Grupos` | Notion | ✅ **varridas** |

> ⚠ **OKRs do projeto foram gerados com ChatGPT** a partir das dores mapeadas, e o link da
> conversa está na página. **Não varrido** — e vale registrar que **OKR de cliente nasceu de
> sessão de IA**, o que é dado sobre o método da casa.

## Contexto crítico
### Onde estamos
Conta ativada em **10/06/2024**, com kick-off presencial em **28/06/2024** e
**passagem de bastão de Sales para Ops executada e registrada**.

**É a segunda conta em volume de chamados: 30 em 24 dias, de 10 pessoas — e 21 seguem abertos.**

> 🔴 **21 de 30 abertos é a pior proporção da carteira.** NV tem 16/39, VIX 16/28,
> Lofty Style 12/15. **Aqui, 70%.**

### 🔴 A frente aberta
1. **21 chamados abertos**, a maioria `INSTABILIDADE` e `TAREFA/CONFIG`.
2. **Integração de escrita com pendências desde 29/05/2025** — documento próprio, não varrido.
3. **Campos duplicados no cadastro** — `isabely.consul`, 13/01/2026:
   *"Campos estão duplicados, foram cadastrados 2x, será preciso corrigir."* — **`Em Aberto`**.
4. **Valores da ficha de produto não chegam ao Linx** — `isabely.consul`, 09/01/2026:
   *"reportou que alguns valores da ficha de produto não estão sendo enviados ao linx"* —
   **`Em Aberto`**.
5. **Notificações não chegam por e-mail** — `caroline.silva`, 09/01/2026 — **`Em Aberto`**.
6. 🚨 **A credencial do banco de produção exposta** — ver o alerta no topo.

### O que o cliente espera
**Declarado na página, em *Definições do Projeto*:**

**Sucesso do projeto** — *eliminar retrabalho da equipe* · *reduzir lead time total e das
micro operações*.

**Objetivos principais** — *centralização das informações* · *digitalização dos processos*.

> 🟢 **É o único cliente varrido com definição de sucesso escrita.**

### As dores estruturais registradas

**As 10 dores mapeadas pelo time de Vendas**, transcritas da página:

1. **Digitalização dos processos** — melhorar a integração entre departamentos e o acompanhamento.
2. **Integração e governança** — **eliminar o uso excessivo de planilhas**, centralizar num sistema.
3. **Redução de retrabalho** e de microgerenciamento.
4. **Visibilidade do calendário de produção** e capacidade de **reprogramar em caso de atraso**.
5. **Engajamento da equipe.**
6. **Flexibilidade** para adaptar sem perder robustez.
7. **Preocupação com a integração com o sistema atual**, sobretudo em **cadastro**.
8. **Implementação em fases (ondas)** para não sobrecarregar a equipe.
9. **Centralização das informações.**
10. **Redução do tempo de desenvolvimento** e lançamento.

> 🔴 **A dor 7 se confirmou.** A preocupação era *"integração com o sistema atual,
> especialmente na parte de cadastro"* — e em jan/2026 há chamados abertos sobre **campos
> duplicados no cadastro** e **valores da ficha que não chegam ao Linx**.
> **A dor levantada na venda virou defeito em produção.**

**Risco registrado na própria reunião de warm-up (19/06):**
> *"Fasear o projeto → Tem séria tendência em assumir mais responsabilidades do que conseguem dar
> vazão"*

**Oportunidade registrada na mesma reunião:**
> *"Follow Up de Entregas → Pedidos de Compras → **uBuy (oportunidade)**"*

### Tamanho de atendimento
Grupo **`Médios`** · `WIP 2,25` · **Julianne & Pedro**, com **6 contas**.

> ⚠ **30 chamados em 24 dias numa conta de grupo `Médios`** — volume de `Enterprise` com
> alocação de `Médios`. **Com 21 abertos, vale checar se a alocação comporta a conta.**

## Governança
### Responsável de atendimento (uMode)
Julianne & Pedro (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Razão social, CNPJ, receita, ativação, setor | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |
| Pessoas, cargos, dores, kick-offs, fluxo | Notion — corpo da página `NK STORE` | **varrido 21/09/2026** |
| 30 chamados, tipos, pessoas | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Segmentação e WIP | Notion — base `Segmentação Grupos` | **varrido 21/09/2026** |

> **CPF, telefone pessoal e credencial de banco existem na fonte e NÃO foram copiados.**

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `NK STORE`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**Registros:** **87 demandas** — [índice](../_demandas/_indice.md) · **12 RFIs** — [índice](../_rfis/_indice.md)

**As 15 áreas deste cliente:**

- [Institucional](../../../00_Institucional/_contexto/contexto-area.md)
- [Planejamento](../../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../../02_Estilo-Criacao/_contexto/contexto-area.md)
- [Desenvolvimento de Colecao](../../../03_Desenvolvimento-de-Colecao/_contexto/contexto-area.md)
- [Qualidade](../../../04_Qualidade/_contexto/contexto-area.md)
- [PCP](../../../05_PCP/_contexto/contexto-area.md)
- [Compras Supply Sourcing](../../../06_Compras-Supply-Sourcing/_contexto/contexto-area.md)
- [Logistica CD](../../../07_Logistica-CD/_contexto/contexto-area.md)
- [Ecommerce Cadastro](../../../08_Ecommerce-Cadastro/_contexto/contexto-area.md)
- [Comercial Vendas](../../../09_Comercial-Vendas/_contexto/contexto-area.md)
- [Marketing](../../../10_Marketing/_contexto/contexto-area.md)
- [Financeiro](../../../11_Financeiro/_contexto/contexto-area.md)
- [Design](../../../12_Design/_contexto/contexto-area.md)
- [Modelagem](../../../13_Modelagem/_contexto/contexto-area.md)
- [Engenharia](../../../14_Engenharia/_contexto/contexto-area.md)

**Autoridades da Casa que governam este arquivo:**
[`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md) · [`_espec-pessoas-e-comunicacoes.md`](../../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) · [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
