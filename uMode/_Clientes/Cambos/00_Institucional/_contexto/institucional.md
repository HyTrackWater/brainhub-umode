# Cambos · Institucional

> **Reescrito em 21 set 2026 a partir do Notion ao vivo.** Campo sem fonte fica `[a preencher]`.
>
> ⚠ **A página de origem contém CPF e telefone pessoal.** **Não foram copiados** — aqui ficam
> nome, cargo e e-mail corporativo, que é o dado de negócio.

## Identidade
### ID do cliente
`cambos`

### Aliases do cliente
`Cambos` · razão social **SOUZA & CAMBOS CONFECÇÕES LTDA** ·
**dois domínios**: `cambos.com.br` e `souzacambos.com.br` · site `souzacambos.com.br`

### Quem são
**Confecção de atacado e private label, com fábrica própria em Minas e lojas em São Paulo.**
CNPJ `67.331.991/0001-66`.

**Dois endereços físicos, e a divisão é funcional:**

| Local | Endereço | O que acontece lá |
|---|---|---|
| **Fábrica — Elói Mendes (MG)** | Rua Pontal, 231 — Distrito Industrial | **Modelagem e Pilotagem** |
| **Lojas — Brás (SP)** | Rua Mendes Júnior, 453 · R. Xavantes, 697 | **Pesquisa e Criação** |

> 🔴 **É a primeira conta varrida em que a mesma área se divide por geografia.** A VIX divide
> Estilo por **linha de produto**; a Cambos divide **Desenvolvimento por cidade**.
> **Duas formas diferentes de subárea, nos dois casos já existindo na operação.**

### O que fazem
**140.000 peças por mês.** Produção **interna e externa**, e **têm tecelagem própria**.
Trabalham com **20 a 40 fornecedores** no desenvolvimento. **Não importam.**

**Não têm coleção definida** — fazem as 4 estações, *"mas entre elas trabalhamos mais com as
demandas do cliente"*.

> ⚠ **Isso contraria a premissa do módulo `Gestão de Coleção`**, que é o módulo contratado.
> **Um cliente sem coleção definida usando um módulo de gestão de coleção é tensão de desenho,
> não detalhe.** `[a preencher]` — **como isso foi resolvido na implantação?**

### Para quem fazem
**Atacado e Private Label.** **40% Magazine, 60% marca própria (Atacado).**

🔴 **E fornecem para a CAEDU e para a Marisa.**

> **A Caedu também é cliente da uMode.** Isso significa que **duas contas do BrainHub têm
> relação comercial direta entre si** — a Cambos desenvolve produto que a Caedu vende.
>
> **É exatamente a situação que a `federation_connection` da ESPEC-BANCO-001 existe para tratar**,
> e até agora só estava desenhada para a membrana **Casa ↔ cliente**. Aqui aparece
> **cliente ↔ cliente**, real, hoje.
>
> ⚠ **E levanta uma pergunta de confidencialidade que ninguém fez:** o brain da Caedu pode saber
> algo do brain da Cambos? **`[D]` — decisão de negócio, não minha.** Conecta com a regra
> observada na Reserva, onde autoria de alteração **não se revela a fornecedor**.

## Posicionamento
### Segmento
**Moda** · Área de atuação: **Atacado**.

### Receita anual
`[a preencher]` — campo vazio. **Mas há volume:** 140.000 peças/mês.

### Grupo de segmentação uMode
**`Médios`** — Grupo 2. `WIP Estratégico 2,25`.

## Operação uMode
### Status atual
**`Ongoing`** — lido na base em 21/09/2026.

### Data de ativação
`[a preencher]` — campo vazio.
**Piso verificável:** linha criada no Notion em **08/05/2024**.

### Módulos contratados
`Gestão de Coleção` · `Integração` · `Relatórios` — **3 de 7, o menor conjunto entre os
Ongoing depois do Puket.**

> 🔴 **E há ambiguidade contratual registrada pela própria uMode**, na ata do kick-off interno:
> *"Relatórios: **não detalhados no contrato** porém subentendido entre 2-3 relatórios mediante a
> maturidade — sugestões fixas: controle de desenvolvimento/lacre"*.
>
> **"Subentendido" num contrato é dívida esperando cobrança.** `[a preencher]` — **foi resolvido?**

### Usuários da conta
`[a preencher]` — existe uma página **`Perfil de Usuário e Permissionamentos`**, **não varrida**.

**O discovery declara *"em torno de 20 pessoas"*** no processo de desenvolvimento.
**5 pessoas estão nomeadas com cargo** e **3 aparecem em chamado**. Ver [`pessoas.md`](pessoas.md).

### ERP / Integração
🔴 **A base está incompleta.** O campo `ERP/Integração` diz apenas
**`SPI - Sistema próprio da Cambos`**. **O discovery, na mesma página, descreve quatro sistemas:**

| Sistema | Para que serve | Observação |
|---|---|---|
| **Totvs — Virtual Age** | time de SP e **comercial** | 🟢 **tem pacote de APIs** |
| **SPI** | **controle de produção** | sistema próprio · **o único que está na base** |
| **Banner** | controle de **pedidos de atacado** | **não está no inventário da uMode** |
| **Trello** | **gestão do processo** | idem |
| *Data Lake* | possibilidade levantada | **não implementado** |

**E há uma regra de negócio registrada:** *"no momento em que o comercial fecha o pedido, duplica
as informações para o SPI"*.

> ⚠ **Duplicação entre Virtual Age e SPI é mecanismo declarado**, não defeito. **Mas é também a
> origem provável da dor de "cadastros paralelos" que o próprio cliente reporta.**

### Responsável de atendimento (uMode)
- **2025:** **Laura** — atende **4 contas**: Cambos, Lofty Style, Luiza Barcelos e Moda Objetiva.
- **2024:** duas pessoas registradas como relação — `[a preencher]`

**Outras pessoas da uMode citadas:** **Sandro** — deu feedback crítico sobre o warm-up (ver
*Contexto crítico*).

## Aliases de áreas
### Mapeamento alias → canônico

> **Fonte: o bloco *Times Envolvidos* das Definições do Projeto** — acordado com o cliente.

| Time declarado | Escopo declarado | → Área canônica |
|---|---|---|
| **Desenvolvimento** | Pesquisa, Criação, **Modelagem** e **Pilotagem** | ⚠ **cobre 3 áreas canônicas** — ver abaixo |
| └ **MG** | Modelagem e Pilotagem | `13_Modelagem` + 🔴 **produção interna** |
| └ **SP** | Pesquisa e Criação | `02_Estilo-Criacao` |
| **Comercial** | passa demandas dos clientes de PL para Estilo e Criação | `09_Comercial-Vendas` |
| **Compras** | **cadastro de MP e pedido** | `06_Compras-Supply-Sourcing` |

### 🔴 "Pilotagem" é o quarto caso de produção interna sem área canônica
NV tem `Atelier`, NK tem `Oficina`, VIX tem `Estamparia` — e a Cambos tem **`Pilotagem`**, feita
na fábrica de MG.

> **Quatro clientes, quatro nomes, a mesma lacuna.** Reforça a
> [`_proposta-grade-de-areas-revisao.md`](../../../../00_Institucional/_contexto/_proposta-grade-de-areas-revisao.md),
> que foi escrita com três casos. **Agora são quatro.**

### ⚠ "Desenvolvimento" aqui não é `03_Desenvolvimento-de-Colecao`
O time chamado **Desenvolvimento** na Cambos engloba **Pesquisa, Criação, Modelagem e Pilotagem**
— que na grade canônica são `02`, `13` e produção interna. **Mesmo nome, escopo diferente.**

> **É o risco de taxonomia que o `CLAUDE.md` nomeia:** palavra igual, sentido diferente.
> **Não traduzi `Desenvolvimento` por `03_Desenvolvimento-de-Colecao`.**

## Sistemas e fontes de verdade
### Drive de operação
Pasta registrada — `17HOz4vDW9Am9Z0GSPlPOUBi4_kKhytVN`. **Não varrida.**

### Outras fontes
| Fonte | Ferramenta | Estado |
|---|---|---|
| **Perfil de Usuário e Permissionamentos** | Notion | 🔴 **não varrida** |
| **Playbook Cambos \| Treinamento > IA + Doc Laura** | Notion | 🔴 **não varrida** — ver abaixo |
| Playbook Cambos · Diagnóstico e Reconhecimento | Notion | **não varridas** |
| Cambos \| Análise de Demandas | Notion | **não varrida** |
| Cambos \| Warm Up com Cliente · Reunião Kick Off Cliente | Notion | **não varridas** |
| Integração | Notion | **não varrida** |
| **Gravação da Reunião de Kick Off** | Google Drive (vídeo) | **não varrida** |
| **Miro com detalhamento do projeto** | Miro | **não varrido** |
| Drive — Modelo Documentação | Google Sheets | **não varrida** |
| Plano de Sucesso do Cliente | Google Drive | **não varrido** |
| Feedback do time interno sobre o Warm Up | Notion (base) | **não varrida** |
| Reuniões com Cliente · Demandas do Cliente | Notion (2 bases) | **não varridas** |
| `Chamados & Atendimentos` | Notion | ✅ **varrida — 11 chamados, 3 remetentes** |

> 🔴 **`Playbook Cambos | Treinamento > IA + Doc Laura` é documentação produzida com IA**, e o
> título diz isso. **Está sob a seção "Documentação Homologada"** — ou seja, **passou por
> homologação.**
>
> **Junto com a NK** (fluxo de processo por Tactiq/Gemini, OKRs por ChatGPT), são **dois clientes
> em que parte do contexto institucional nasce de IA**. **É dado sobre o método da casa** — e
> insumo direto do projeto paralelo de transcrições.

## Contexto crítico
### Onde estamos
Conta com **discovery de vendas completo**, kick-off interno gravado, warm-up com feedback
interno registrado, kick-off presencial e playbook homologado.

**11 chamados em jan/2026, 7 abertos.**

### 🔴 A frente aberta
**Instabilidade recorrente reportada de dois domínios diferentes.**
`pamela@souzacambos.com.br` abriu **4 chamados de `INSTABILIDADE`** entre 20 e 29/01/2026, e
`atendimento@cambos.com.br` mais um em 28/01. **Quase todos `Não iniciada`.**

**E um segundo escopo foi desejado e nunca contratado**, registrado na ata do kick-off interno:
> *"Desejo para segundo escopo de projeto — **não contratado ainda**: trazer os clientes para
> dentro da plataforma para acompanhar o desenvolvimento"*

> 🔴 **É pedido de expansão registrado e datado, vindo do cliente.** E é **tecnicamente a
> mesma coisa** que a `federation_connection` do BrainHub faz. **Junto com o fato de que a Cambos
> fornece para a Caedu, isso é oportunidade comercial e caso de uso de produto ao mesmo tempo.**

### O que o cliente espera
🟢 **Declarado com precisão incomum, e com definição de FRACASSO** — o único caso da carteira:

**Sucesso:** *"Informações de Desenvolvimento Centralizadas, Atualizações de FT em tempo real,
comunicação eficiente e diminuição de retrabalho e tempo de desenvolvimento."*

**🔴 Fracasso:** *"**Ser mais um sistema de preenchimento.**"*

> **Essa frase é o critério de risco mais útil que apareceu em toda a varredura.** Ela diz o que
> não pode acontecer, e é verificável: **se o uso virar digitação sem retorno, o projeto falhou
> pelos termos do próprio cliente.**

**Objetivos:** centralizar informação de desenvolvimento **com histórico de alterações de modelos
e coleções** · centralizar comunicação entre times **de forma simultânea** · otimizar tempo de
desenvolvimento.

### As dores estruturais registradas
**Declaradas pelo cliente nas Definições do Projeto:**

1. **Cadastros paralelos gerando retrabalho.** *"Produtos em desenvolvimento com alteração têm
   problemas de comunicação."*
   > ⚠ **Provável raiz: a duplicação declarada Virtual Age → SPI quando o comercial fecha pedido.**
2. **Retrabalho de construção de Ficha Técnica.**
3. 🔴 **Ausência de controle de Modelos e suas Variações.**
   > **Quinto cliente com problema de variante** — com Caedu, Reserva, VIX e Lofty Style.
   > **E aqui não é defeito da plataforma: é a dor que motivou a compra.**
4. **Passagem de bastão do comercial para Desenvolvimento** — *"falta de informação, demora no
   processo de validação"*.
   > ⚠ **O mesmo termo "passagem de bastão" que a uMode usa internamente**, aqui descrevendo um
   > problema **dentro do cliente**. **Duas coisas diferentes com o mesmo nome.**
5. **Não têm informação de performance de produto** — e a própria nota diz:
   *"**Oportunidade de uPlan e IPSP**"*.
   > 🔴 **`IPSP` é um nome de produto que não aparece em nenhuma outra fonte varrida.**
   > `[a preencher]` — **o que é?**

### 🔴 Crítica interna ao método da uMode, registrada na própria página
Feedback do **Sandro** sobre a reunião de warm-up:

> *"alinhar o que vendeu e o que operação vai tocar gerou desconforto... De acordo com ele pode
> dar impressão que a empresa está **desalinhada**. Ter cuidado nesta comunicação."*

E: *"Talvez não ter time operacional — esse ponto está alinhado com a proposta da reunião, pois
o time operacional deve participar da reunião de kickoff."*

> **É a única crítica ao próprio método da uMode encontrada em qualquer conta.** E ela toca
> exatamente o ritual da **passagem de bastão de Sales para Ops** — o mesmo que na NK aparece
> marcado como concluído e no Puket está em branco.
>
> **Para o brain da Casa isso vale mais que para o brain do cliente.**

### Tamanho de atendimento
Grupo **`Médios`** · `WIP 2,25` · **Laura**, com 4 contas.

## Governança
### Responsável de atendimento (uMode)
Laura (2025)

### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Discovery, volumes, ERPs, canais, nota do processo | Notion — bloco *Informações de Discovery de Sales* na página | **varrido 21/09/2026** |
| Pessoas, times, sucesso, fracasso, dores, métricas | Notion — bloco sincronizado *Pessoas* e *Definições do Projeto* | **varrido 21/09/2026** |
| Feedback interno sobre o warm-up | Notion — corpo da página | **varrido 21/09/2026** |
| 11 chamados | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Razão social, CNPJ, endereços, módulos | Notion — base `Mapa de Clientes` + página | **varrido 21/09/2026** |

> **CPF e telefone pessoal existem na fonte e NÃO foram copiados.**

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Cambos`

**Os outros dois MDs desta casa:** [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)

**Integração deste cliente:** [integracao.md](integracao.md)

**Registros:** **47 demandas** — [índice](../_demandas/_indice.md) · **3 RFIs** — [índice](../_rfis/_indice.md) · **8 fichas de pessoa** — [índice](../_pessoas/_indice.md)

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
