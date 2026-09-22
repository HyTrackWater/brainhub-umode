# Lofty Style · Pessoas

> **Reescrito em 21 set 2026 a partir do Notion ao vivo**, incluindo as **duas bases de pesquisa
> de satisfação**. Campo sem fonte fica `[a preencher]`.
>
> 🟢 **Esta conta tem pesquisa de satisfação** — com **nome, e-mail, área e sentimento
> na mesma linha**, dito pela própria pessoa.
>
> ⚠ **CORREÇÃO de 22 set 2026:** eu havia escrito aqui *"a única conta da carteira"*.
> **Estava errado.** A **Osklen** tem a sua, **com 33 respondentes contra 19**, e **anterior**
> (25/03/2025). **A prática existe em pelo menos 2 clientes e não está padronizada.**

## Responsável de atendimento (uMode)
- **2025:** **Laura** — atende **4 contas**: Lofty Style, Cambos, Luiza Barcelos e Moda Objetiva.
- **2024:** duas pessoas registradas como relação, **nomes não resolvidos** — `[a preencher]`

## Diretoria e decisores
🔴 `[a preencher]` — **e aqui a lacuna é declarada pela própria origem.**

A página do cliente tem um bloco **Pessoas** com quatro seções — *Diretores e Representantes
Legais*, *Responsável pelo Financeiro*, *Responsáveis pelos Projetos* e *Responsável Tecnologia*
— e **todas contêm apenas os rótulos dos campos**: `Nome`, `Cargo`, `E-mail`, `Telefone`.
**Nenhum valor preenchido.**

> **É o mesmo template da NK STORE, que lá está completo com 13 pessoas.** E o mesmo padrão do
> Puket, onde a passada de bastão está em branco.
>
> **Placar do template de pessoas nas contas varridas: NK preenchido, NV preenchido,
> Puket em branco, Lofty Style em branco.** **Metade.**

## Liderança do projeto (cliente)
`[a preencher]` — seção *Responsáveis pelos Projetos* **em branco na origem**.

> Candidata por evidência cruzada: **Gabriela de Barros Cunha**. É a única pessoa presente
> **nas duas pesquisas**, e a resposta dela em out/2025 fala em nome do time e anuncia ação:
> *"Vamos fazer o treinamento interno para que todos estejam na mesma página"*.
> **Quem promete treinamento interno costuma responder pelo projeto. Não afirmo — confirmar.**

## Time do projeto por área

> **Fonte: o campo `Área` das pesquisas, preenchido pela própria pessoa.** É **autodeclaração** —
> fonte diferente do perfil de PLM (Caedu, Puket, VIX), do departamento acordado em reunião (NK) e
> do nome de grupo de WhatsApp (Reserva). **Quinto tipo de fonte em sete clientes.**

| Área canônica | Pessoas |
|---|---|
| `05_PCP` | **Izabella Veloso** · **Janaína Araújo** · **Márcia Santos** · **Taislaine Alves Caetano** · **Daniela Barcelos da Cruz** · **Ana Paula França** · **Bruna Vanessa** · **Michelle Nogueira** |
| `02_Estilo-Criacao` | **Isabelle Dambiski** · **Mayra Obara** · **Amanda Lunardelli** · **Jovania Fernandes** · **Gabriela de Barros Cunha** |
| `06_Compras-Supply-Sourcing` | **Gabriela Cunha** (mar/2025) · **Victoria Silva** · **Brenda Santana** |
| `13_Modelagem` | **Daniela Fernandes** |
| `01_Planejamento` | **Diego Oliveira** |
| ⚠ não declarada | **Raiane Brito** — respondeu *"Lofty style"* no campo de área |

### 🔴 Uma pessoa mudou de área entre as duas pesquisas
**Gabriela Cunha** aparece em **mar/2025 como `Sourcing / compras`** e em **out/2025 como
`Estilo`** — com **duas grafias de e-mail** (`gabriela.cunha@loftystyle.com.br` e
`gabriela.cunha@loftystyle.com`, esta sem `.br`).

> **É a primeira mudança de área observável em toda a varredura**, e só apareceu porque **há
> duas medições no tempo**.
>
> **Para o modelo isso é decisivo:** `person_memberships` precisa ser **histórico**, não estado —
> uma linha por (pessoa × área × período). Um campo `areaId` único teria **apagado** a passagem
> dela por Sourcing. Item para a
> [`_espec-pessoas-e-comunicacoes.md`](../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) §3.

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

### Razão de pessoas

**19 pessoas** no razão: 18 das pesquisas + 1 que só aparece em chamado.
`ATIVO` **5** · `INDETERMINADO` **13** · `ATIVO_SEM_CADASTRO` **1**

> **`INDETERMINADO` aqui significa: respondeu pesquisa, declarou área, e não há evidência de que
> usa o sistema.** Não há lista de usuários varrida para confrontar — as duas páginas de
> permissionamento não foram abertas.

| Pessoa | E-mail | Área | Estado | Evidência (data) | Entusiasmo · CSat |
|---|---|---|---|---|---|
| **Amanda Lunardelli** | `amanda.lunardelli@loftystyle.com.br` | `02_Estilo-Criacao` | `ATIVO` | pesquisa 08/10/2025 + **6 chamados** até 29/01/2026 | 5 · 10 |
| **Michelle Nogueira** | `michelle.nogueira@loftystyle.com.br` | `05_PCP` | `ATIVO` | pesquisa 08/10/2025 + chamado 23/01/2026 | 5 · 9 |
| **Jovania Fernandes** | `jovania.fernandes@loftystyle.com.br` | `02_Estilo-Criacao` | `ATIVO` | pesquisa 08/10/2025 + chamado 23/01/2026 | **4 · 8** |
| **Victoria Silva** | `victoria.silva@loftystyle.com.br` | `06_Compras-Supply-Sourcing` | `ATIVO` | pesquisa 08/10/2025 + chamado 14/01/2026 | 5 · 10 |
| **Raiane** | `raiane.nascimento@loftystyle.com.br` | ⚠ ver nota | `ATIVO` | chamado 29/01/2026 | — |
| **Luciana Nunes** | `luciana.nunes@loftystyle.com.br` | `[a preencher]` | `ATIVO_SEM_CADASTRO` | **5 chamados**, 13–29/01/2026 | — |
| Izabella Veloso | `izabella.veloso@loftystyle.com.br` | `05_PCP` | `INDETERMINADO` | pesquisa **07/03/2025** | 5 · 10 |
| Janaína Araújo | `janaina.araujo@loftystyle.com.br` | `05_PCP` | `INDETERMINADO` | pesquisa 07/03/2025 | 5 · 10 |
| Márcia Santos | `marcia.santos@loftystyle.com.br` | `05_PCP` | `INDETERMINADO` | pesquisa 07/03/2025 | 5 · 10 |
| Taislaine Alves Caetano | `tais.caetano@loftystyle.com.br` | `05_PCP` | `INDETERMINADO` | pesquisa 07/03/2025 | 5 · 10 |
| Isabelle Dambiski | `isabelle.dambiski@loftystyle.com.br` | `02_Estilo-Criacao` | `INDETERMINADO` | pesquisa 07/03/2025 | 5 · **7** |
| Diego Oliveira | `diego.oliveira@loftystyle.com.br` | `01_Planejamento` | `INDETERMINADO` | pesquisa 07/03/2025 | 5 · 10 |
| **Gabriela de Barros Cunha** | `gabriela.cunha@loftystyle.com.br` | `06` (mar) → `02` (out) | `INDETERMINADO` | **nas duas pesquisas** — 07/03 e 09/10/2025 | 5 · 10 |
| Daniela Barcelos da Cruz | `daniela.cruz@loftystyle.com.br` | `05_PCP` | `INDETERMINADO` | pesquisa 08/10/2025 | 5 · 9 |
| Ana Paula França | `ana.franca@loftystyle.com.br` | `05_PCP` | `INDETERMINADO` | pesquisa 08/10/2025 | 5 · 10 |
| Bruna Vanessa | `bvps.go@gmail.com` | `05_PCP` | `INDETERMINADO` | pesquisa 08/10/2025 · ⚠ **e-mail pessoal** | 5 · 10 |
| Mayra Obara | `mayra.obara@loftystyle.com.br` | `02_Estilo-Criacao` | `INDETERMINADO` | pesquisa 08/10/2025 | 5 · 9 |
| Daniela Fernandes | `daniela.fernandes@loftystyle.com.br` | `13_Modelagem` | `INDETERMINADO` | pesquisa 08/10/2025 | 5 · 10 |
| Brenda Santana | `brenda.araujo@loftystyle.com.br` | `06_Compras-Supply-Sourcing` | `INDETERMINADO` | pesquisa 08/10/2025 | 5 · 10 |
| Raiane Brito | `raiane.brito@loftystyle.com.br` | ⚠ *"Lofty style"* | `INDETERMINADO` | pesquisa 08/10/2025 | 5 · 10 |

> ⚠ **Duas Raianes, ou uma?** `raiane.brito@` respondeu a pesquisa em out/2025;
> `raiane.nascimento@` abriu chamado em jan/2026. **E-mails diferentes, mesmo primeiro nome.**
> **Não uni os registros.** Pode ser mudança de sobrenome, pode ser outra pessoa. **Confirmar.**

## 🔴 O achado: as ressalvas de outubro viraram chamado em janeiro

As pesquisas têm um campo **Preocupação e Ressalva**. Três delas **descrevem, em out/2025, coisas
que aparecem como chamado em jan/2026** — **três meses depois**.

| Quem | Ressalva declarada em **out/2025** | O que aconteceu em **jan/2026** |
|---|---|---|
| **Jovania** (CSat 8, **o mais baixo**) | *"Adicionar mais Campos categorizando e segmentando melhor. Por exemplo: Nome do tecido, Tipo: plano/malha"* | abriu chamado **`TAREFA/CONFIG`** em 23/01 |
| **Bruna Vanessa** | *"Liberação de telas... deve ser feito **setorizado** para não acontecer **erros na transmissão final ao linx**"* | **4 chamados de divergência de custo Linx × uMode**, todos `Pendente` |
| **Gabriela de Barros Cunha** | *"minha maior ressalva é sobre a **qualidade do cadastro** e o entendimento dos colaboradores"* | os mesmos 4 chamados de custo divergente |
| **Michelle** | *"caso não haja disciplina de sempre cadastrar os produtos... também **controles paralelos** que acabem não sendo incluídos na umode, voltando a tornar o processo moroso"* | abriu chamado de usabilidade em 23/01 |

> **Não afirmo causalidade** — são fontes distintas e não li o conteúdo dos chamados.
> **Afirmo a coincidência de tema, com data, e que ninguém cruzou as duas bases.**
>
> 🔴 **A pesquisa de satisfação funcionou como sistema de alerta precoce e foi arquivada.**
> Entusiasmo médio **4,9/5**, CSat médio **9,6/10** — números ótimos que **escondem ressalvas
> técnicas específicas** que depois viraram fila de chamado.
>
> **Para o BrainHub isto é o caso de uso, não um exemplo:** `communication_events` de tipo
> pesquisa, com participante identificado e **área**, indexados junto dos chamados, tornam esse
> cruzamento automático em vez de acidental.


#### Solicitantes de demanda — varredura de 22 set 2026

> **Fonte: campo `Quem solicitou?` das demandas.** Cada nome está **exatamente como
> aparece na fonte** — **nada foi unificado**, porque sem e-mail unificar por semelhança
> gráfica inventaria pessoa. **Variantes estão marcadas para serem resolvidas, não fundidas.**
>
> ⚠ **Quem nunca abriu demanda não aparece aqui. Ausência não é inatividade.**

| Nome (como está na fonte) | Demandas | Primeira | Última | Observação |
|---|---:|---|---|---|
| Gustavo | 17 | 29/08/2025 | 06/02/2026 | — |
| Amanda | 10 | 11/02/2026 | 17/04/2026 | — |
| Gabriela | 7 | 29/08/2025 | 04/12/2025 | ⚠ também `Gabi` (2) e `Gabriela Cunha` (1) |
| Marcello | 4 | 19/03/2026 | 16/04/2026 | — |
| Raiane | 2 | 27/04/2026 | 27/04/2026 | também `Raiane Brito` |
| Michelle | 2 | `[a preencher]` | `[a preencher]` | também `Michelle Nogueira` |
| Daniela | 2 | `[a preencher]` | `[a preencher]` | — |
| Luciana | 1 | 25/03/2026 | 25/03/2026 | `Luciana Nunes` |
| Valeria | 1 | 10/04/2026 | 10/04/2026 | — |
| Regina | 1 | 17/03/2026 | 17/03/2026 | — |
| Isadora Terlizzi | 1 | 07/04/2026 | 07/04/2026 | — |
| Caroline Koller | 1 | 13/04/2026 | 13/04/2026 | — |
| Bruno | 1 | 02/04/2026 | 02/04/2026 | — |

Evidência completa da carteira em [`_varredura-2026-09-22-pessoas-e-ferramentas-carteira.md`](../../../00_Institucional/_contexto/_varredura-2026-09-22-pessoas-e-ferramentas-carteira.md).

## Canais de comunicação

> **Cada canal é uma entidade** — tem participantes, cadência, dono e assunto.

| Canal | Ferramenta | Quem participa | Cadência | Último registro |
|---|---|---|---|---|
| **Pesquisa Satisfação Kick Off** | Notion | **7 pessoas** | única | **07/03/2025** |
| **Pesquisa Satisfação Treinamento** | Notion | **12 pessoas** | única | **08–09/10/2025** |
| Chamados | Notion — `Chamados & Atendimentos` | 6 pessoas | alta | **29/01/2026** |
| **Atualização de Projeto** | Notion | → cliente | pontual | **12/01** e **29/01/2026** |
| Reuniões compartilhadas com Cliente | Notion (base) | `[a preencher]` | — | **não varrida** |
| Demandas compartilhadas com Cliente | Notion (base) | `[a preencher]` | — | **não varrida** |
| **Documentação de integração** | **`docs.umode.app`** | cliente, com senha | — | 🚨 **senha em página de Notion** |
| Kick Off presencial | presencial | time do cliente | único | **mar/2025** |
| Treinamento Go Light uFlow | Google Slides | time do cliente | único | **out/2025** |
| Miro | Miro | `[a preencher]` | — | **não capturado** |
| Drive de operação | Google Drive | `[a preencher]` | — | **não capturado** |
| CRM → Anotações Gerais | Notion | — | — | **vazio na origem** |

> 🟢 **A pesquisa de satisfação é o único canal em toda a varredura que captura sentimento
> com pessoa e área identificadas.** Existe em **1 de 7 clientes**.
> **Se virasse padrão, resolveria de uma vez o vínculo pessoa↔área que hoje sai de cinco fontes
> diferentes e incompatíveis.**

## Financeiro
- **E-mail principal financeiro:** `financeiro@loftystyle.com.br` — preenchido na base.
- **Responsável pelo Financeiro:** `[a preencher]` — **seção em branco na página.**
- Nenhum chamado `FINANCEIRO` na janela varrida.

## Tecnologia
- **Responsável Tecnologia:** `[a preencher]` — **seção em branco na página.**
- **ERP `Linx`**, com **documentação oficial publicada** em `docs.umode.app/integracao-lofty`.
- 🚨 **A senha desse site está em texto plano na página do Notion.** **Não foi copiada.**
- **Páginas técnicas próprias:** `NCM e Código CEST` · `Exclusão de Variante após integração`.

## Governança
### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| 19 participações com nome, e-mail, área, entusiasmo, CSat, expectativa e ressalva | Notion — `Pesquisa Satisfação Kick Off Lofty Style` e `Pesquisa Satisfação Treinamento Lofty Style` | **varridas 21/09/2026** |
| 15 chamados e assuntos | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Seções de pessoas em branco, sistemas, documentos | Notion — corpo da página `Lofty Style` | **varrido 21/09/2026** |
| Atendimento, financeiro, ativação | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |

> **A senha exposta na fonte NÃO foi copiada.**

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —
> não editar à mão: a próxima execução sobrescreve.

**Cliente:** `Lofty Style`

**Os outros dois MDs desta casa:** [institucional.md](institucional.md) · [jornada.md](jornada.md)

🔴 **O que ainda não se sabe deste cliente, e onde já se procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)

**Registros:** **85 demandas** — [índice](../_demandas/_indice.md) · **15 RFIs** — [índice](../_rfis/_indice.md) · **13 fichas de pessoa** — [índice](../_pessoas/_indice.md)

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
