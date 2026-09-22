# AGORA.md — onde o projeto está, em uma tela

> **Este é o arquivo de orientação.** Serve para retomar o projeto de qualquer lugar, em
> qualquer workspace, sem ler as 2.700 linhas da `STATE.md`.
>
> **Atualizado em: 22 set 2026.** Se esta data não for de hoje ou de ontem, **desconfie** —
> confira o fim do `## Log de sessões` da [`STATE.md`](STATE.md) e o `git log -1`.
>
> *(Este arquivo não fixa hash de commit de propósito: ele envelheceria a cada commit e
> daria falsa impressão de desatualização. A data é o sinal.)*

---

## 1 · O papel

**Eu sou o executor técnico. Eu não decido arquitetura, hierarquia nem regra de negócio** — isso
está travado no `CONTEXT.md` e é decisão do Vinicius. Meu trabalho é **aplicar o padrão com
precisão e não inventar conteúdo**.

**As três regras que não se quebram:**
1. **Zero alucinação.** Sem fonte, o campo é `[a preencher]` — nunca um palpite.
2. **Ausência de fonte é hipótese, não conclusão.** Escrevo *"não encontrei em X"*, nunca
   *"não existe"*.
3. **Todo MD do mesmo tipo tem os mesmos títulos, sempre.** Conteúdo varia por cliente;
   **estrutura nunca varia.** Se o padrão mudar, muda para **toda a classe**, retroativamente.

**Escrita autorizada em um só repositório: `HyTrackWater/brainhub-umode`.** Todos os outros são
somente leitura — sem commit, sem push, sem checkout.

## 2 · O que estamos fazendo

Construindo o **cérebro institucional da uMode e de cada cliente**, em Markdown padronizado,
convergindo para uma plataforma com banco MongoDB.

**A hierarquia travada:**
```
Instituição (Casa uMode OU Cliente)
└── Institucional        identidade, voz, marca, taxonomia
    └── Áreas            8 internas / 14 canônicas de cliente
        └── Subáreas     nomes livres, inclui Produtos
            └── Pessoas  internas na Casa; do cliente, na casa do cliente
```

## 3 · Como estamos fazendo

**Varredura de fonte viva → formalização no padrão → verificação em número → commit.**

- **Fonte viva, nunca export.** Regra travada em 21 set 2026: o export versionado estava
  **seis meses defasado** e dava status errado. **Export não serve para afirmar estado.**
- **Grade de evidência em toda afirmação técnica:** `[C]` verificado na fonte, com a fonte
  citada · `[F]` existe mas atrás de flag · `[P]` proposta minha · `[D]` decisão que não é minha.
- **A lacuna vem antes da conquista.** Todo documento de estado abre declarando **o que ele não
  resolve**.
- **Um caso é anedota, dois é hipótese, três é padrão.** Não promovo antes da hora.
- **Cobertura em número verificável**, nunca em adjetivo.
- **Um assunto tem um dono.** Documento novo que vira autoridade marca o anterior como
  `SUPERSEDED` no que perdeu.

**Ferramentas de verificação**, ambas em `scripts/` e obrigatórias antes de todo commit:
`valida-padrao-corpus.py` (as 4 classes de MD de cliente) e `valida-documentacao.py`
(nenhum `.md` estrutural órfão do manifesto do `START.md` § 1).

## 4 · Onde está cada coisa

> 🔴 **O conjunto completo de documentação — "o time" — está declarado no
> [`START.md`](START.md) § 1**, com a classe de cada arquivo e quem é dono de qual assunto.
> **`python scripts/valida-documentacao.py` confere que nada ficou órfão.**

| Arquivo | O que é | Quando ler |
|---|---|---|
| **`START.md`** | **o manifesto e a ordem de leitura** | primeira mensagem da sessão |
| **`AGORA.md`** | este arquivo — orientação | **primeiro, sempre** |
| `CLAUDE.md` | papel, regras invioláveis, como executar | antes de qualquer tarefa |
| `CONTEXT.md` | decisões de arquitetura travadas | antes de mapear campo ou taxonomia |
| `STATE.md` | histórico completo, sessão a sessão | quando precisar do detalhe de algo |

**Autoridades temáticas** (em `uMode/00_Institucional/_contexto/`):

| Documento | É autoridade sobre |
|---|---|
| [`_espec-pessoas-e-comunicacoes.md`](uMode/00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) | pessoas e comunicações no banco |
| [`_taxonomia-status-cliente.md`](uMode/00_Institucional/_contexto/_taxonomia-status-cliente.md) | o campo `Status` do cliente |
| [`_varredura-2026-09-22-reunioes-compartilhadas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-22-reunioes-compartilhadas.md) | a base de reuniões do Notion |
| [`_proposta-grade-de-areas-revisao.md`](uMode/00_Institucional/_contexto/_proposta-grade-de-areas-revisao.md) | revisão da grade de áreas canônicas |
| [`_varredura-2026-09-21-fontes-e-lacunas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-21-fontes-e-lacunas.md) | fontes rastreadas e lacunas por cliente |

**Protocolos** (em `uMode/00_Institucional/_protocolos/`): `protocolo-varredura-cliente.md` ·
`protocolo-criacao-cliente.md` · `protocolo-gestao-demanda.md` · `protocolo-gestao-rfi.md`.

## 5 · Passos já dados

| Fase | Quando | O que ficou pronto |
|---|---|---|
| **Hierarquia e volumetria** | jun–jul 2026 | 4 níveis travados · 8 áreas internas · 14 canônicas de cliente · template |
| **Replicação total** | ago 2026 | 46 clientes com casa no padrão · migração para Git |
| **Banco** | ago 2026 | espec de collections, campos e relações — desenho é nosso, implementação é do Bergson |
| **Varredura de fonte viva** | 19–21 set 2026 | 15 fontes · CAEDU e Puket fechadas · `protocolo-varredura-cliente.md` escrito |
| **Carteira inteira** | 22 set 2026 | **48 de 48 clientes** · taxonomia de `Status` travada |
| **Base de reuniões** | 22 set 2026 | 1.161 reuniões achadas · Recco e Luiza Barcelos varridas |
| **Modelo de documentação** | 22 set 2026 | **8 classes travadas · manifesto declarado no `START.md` § 1 · verificável por script** |
| **Pessoas e ferramentas** | 22 set 2026 | **enum de 7 módulos · atendimento de 17 contas · razão de pessoas datado em 17 clientes** |

**Cobertura hoje, medida:**

| | Número |
|---|---:|
| Clientes no corpus | **48** |
| MDs em `uMode/` | **2.020** |
| Demandas formalizadas | **1.001** |
| RFIs formalizadas | **87** |
| `contexto-area.md` conformes | **694/694** |
| `institucional.md` · `jornada.md` · `pessoas.md` | **50/50 · 49/49 · 49/49** |
| Atas de reunião lidas por inteiro | **8 de 1.161** |
| `.md` estruturais, todos classificados | **68/68** |
| 🟢 **Conectados no grafo** (Obsidian) | **1.996 de 2.079 · 96,0%** |
| Órfãos restantes | **88 · 4,0%** |
| 🟢 **Fichas de pessoa de cliente** | **127 em 17 clientes** |
| Decisões pendentes registradas | **317** |
| Clientes com permissionamento documentado | **12** |
| Bases do Notion varridas | **7** |
| Clientes com as 8 dimensões respondidas | **12 de 48** |
| Pessoas de cliente com e-mail individual | **92** · janela de jan/2026 |
| Arquivos de demanda no padrão canônico | **998/999** · 1 staging `SUPERSEDED` |
| Clientes com razão de pessoas datado | **18 de 48** |

## 6 · O que está sendo feito agora

🔵 **Frente ativa: varredura cliente a cliente, ABRINDO A PÁGINA de cada um.**

> 🔴 **A regra que mudou em 22 set 2026:** até aqui eu varria **bases** (SQL). A página
> do cliente **não é base** — e é onde vivem o **`cargo`**, a **área**, as **pessoas de
> diretoria**, as **sub-páginas de ata** e, em pelo menos um caso, uma **credencial de
> produção em texto claro**. **Consulta SQL não alcança nada disso.**

**O modelo, travado pelo Vinicius em 22 set 2026: ENTIDADE É ARQUIVO.**
*"praticamente tudo que for uma entidade é arquivo? Ou seja, ferramenta, pessoas, empresas,
áreas, demandas, RFIs, tudo... As reuniões, contextos gerais, e-mails, tudo isso vai estar de
alguma forma ligada a esses nós maiores."*

| Entidade | É arquivo? | Quantos |
|---|:-:|---:|
| Instituição · Área · Demanda · RFI · Solução | ✅ | 50 · 694 · 1.021 · 102 · 16 |
| Pessoa | ✅ | **137** |
| **Ferramenta** | ✅ **novo em 22 set** | **16** |
| Reunião / ata · E-mail · Agente | 🔴 **não** | 1.161 · 92 · 4 conhecidos |

**Páginas de cliente abertas: 3 de 49** — CAEDU, Osklen, NK STORE.

- 🟢 **NK STORE:** 13 pessoas com **cargo e área**, das quais **8 nunca abriram demanda**
  — incluindo as **duas diretoras do projeto**. De 15 para **24 fichas**.
- 🔴 **Osklen:** o **mesmo** toggle `Pessoas`, **inteiramente vazio.**
- 🔴 **CAEDU:** 56 sub-páginas, **~47 atas de weekly** que nenhuma consulta SQL vê.
- 🔴 **A CAEDU mudou de `Ongoing` para `Onboarding` em 22/09/2026 às 15:04**, entre duas
  leituras minhas — e a base `Etapas do Processo de Clientes` **ainda a marca como `Ongoing`.`**
  **Perguntar o motivo antes de retomar a frente dela.**

## 7 · Próximos passos, em ordem

1. 🔵 **Abrir as 46 páginas de cliente que faltam.** É a fonte de maior rendimento
   descoberta até agora: resolve `cargo`, `área` e a camada de liderança de uma vez.
   **Medir, por cliente, se o toggle `Pessoas` está preenchido** — vira placar de prontidão.
2. 🚨 **Credenciais.** As duas expostas (NK STORE — **agora com o lugar exato**,
   Lofty Style) **e a varredura das 1.153 atas não abertas.** **Toda página de cliente aberta
   daqui pra frente passa a ser varrida também em busca de segredo.**
3. 🔴 **Perguntar ao Vinicius por que a CAEDU virou `Onboarding`** — e qual campo manda,
   `Status` ou `Etapa`, que discordam em 5 clientes.
4. 🔵 **Fechar as 3 entidades que faltam: reunião, e-mail e agente.** Enquanto forem
   prosa, o grafo não liga ata a pessoa nem demanda a conversa.
5. 🔵 **Resolver o campo `Participantes` das 1.161 reuniões** com `get-users` — dá
   **presença nominal com data**, a melhor fonte de pessoa ativa ainda não extraída.
6. 🔴 **Varrer as duas relações fechadas de `Mapa de Clientes`:** `Segmentação Grupos`
   e `Atendimento 2024`.
7. 🔴 **Criar o campo `Data de Churn`** — segue sendo a lacuna mais cara do corpus.
8. 🔵 **Retomar a CAEDU** assim que as ~50 transcrições reais chegarem.

## 8 · Decisões esperando o Vinicius

🔴 **O dono deste assunto é o [`_pendencias-gerais.md`](uMode/00_Institucional/_contexto/_pendencias-gerais.md)
— **340 itens datados.** **Não crie tabela de pendência aqui nem em lugar nenhum: escreva lá.**

> ⚠ **Este bloco já foi o erro que ele descreve.** Em 22 set 2026 eu montei aqui uma tabela de
> "8 decisões esperando o Vinicius" **sem ter lido o `_pendencias-gerais.md`**, que já era o dono
> com 233 itens. **Era um segundo dono para o mesmo assunto** — o defeito que o `CLAUDE.md`
> proíbe e que o `START.md` § 0 agora trava como regra. **Os itens foram movidos para lá
> (234–248) e aqui ficou só o ponteiro.**

**As mais quentes da varredura de 22 set 2026** — detalhe e contexto nos itens citados:

| Item | Decisão |
|---|---|
| **238** | 🔴 **A base não tem campo `Data de Churn`** — sem ele não há tempo de vida de cliente nem taxa de churn por coorte |
| **237** | Separar `Status` em `lifecycleStage` / `serviceMode` / `recordKind`? |
| **234** | Criar a área `15_Producao-Interna`? **5 clientes** têm produção interna sem área |
| **235** | `Merchandising` vira área? **Recomendo que não** — os três escopos diferem |
| **239** | A **Baw** está classificada certo? |
| **240** | Reunião e demanda que atendem **dois clientes** — como registrar? |
| **241** | `## O que este documento NÃO resolve` vira canônico? **Muda ~145 arquivos** |

### 8.1 · Dado sensível: `T0` / `T1` / `T2`

> 🔺 **Corrigido em 22 set 2026.** Até aqui eu usava rótulos meus — `INTERNAL_ONLY`,
> `NEVER_TO_THIRD_PARTY`. **Era uma segunda taxonomia para a mesma coisa**, o defeito que a
> gente critica. **O vocabulário é `T0`/`T1`/`T2`**, o mesmo que o João usa no vault, com
> definição operacional já registrada (item 96 do `_pendencias-gerais.md`).

| Tier | O que é | O que entra no corpus |
|:-:|---|---|
| **`T2`** | **equipe** — o padrão | nome, cargo, área, papel, escopo, marco, decisão, prazo |
| **`T1`** | **restrito** | valor de proposta, preço, margem, escopo confidencial — **entra, e fica só no `_contexto/` daquele cliente** |
| **`T0`** | **privado** | 🔴 **nunca entra por valor.** CPF, telefone pessoal, senha, token, string de conexão. **Entra por referência:** registro que existe e **onde** |

**Onde isso vive, por cliente:** `_Clientes/<Cliente>/00_Institucional/_contexto/`
**`_pendencias-e-fontes.md`** — é a autoridade sobre as pendências **daquele** cliente e sobre
**onde já se varreu**. Gerado por `scripts/gera-pendencias-e-fontes.py`.

⚠ **O que NÃO fiz:** não copiei mecanismo nenhum do vault (a restrição continua valendo).
**Adotei o rótulo, que é vocabulário comum** — e vocabulário comum é exatamente o ponto.

## 9 · Como manter este arquivo vivo

**Este arquivo mente rápido se ninguém o atualizar.** A regra:

- **O ritual de fechamento completo está no [`START.md`](START.md) § 4** — são quatro passos:
  `propaga.py`, `valida-documentacao.py`, `STATE.md` e **este arquivo**.
- **Toda sessão que gera commit atualiza `AGORA.md`** — no mínimo a data, os números da § 5 e as
  listas das § 6 e § 7.
- **`AGORA.md` é resumo, `STATE.md` é histórico.** O que aconteceu vai para a `STATE.md`;
  o que **vale agora** vive aqui. **Nada de histórico neste arquivo.**
- **Se este arquivo divergir da `STATE.md`, a `STATE.md` ganha** — e aí este aqui está com
  defeito e precisa ser corrigido na hora.
