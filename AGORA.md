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
| Decisões pendentes registradas | **261** |
| Arquivos de demanda no padrão canônico | **998/999** · 1 staging `SUPERSEDED` |
| Clientes com razão de pessoas datado | **18 de 48** |

## 6 · O que está sendo feito agora

🔵 **Frente ativa: varredura transversal da carteira** — pessoas, áreas e ferramentas
contratadas, a partir das fontes do Notion já liberadas.

- **A rota mudou em 22 set 2026.** A frente da CAEDU **está pausada**: quem vai entregar as
  transcrições e arquivos **ainda não liberou o acesso**. O Vinicius pediu para retomar a
  varredura de **todos** os clientes enquanto isso.
- **Já feito nesta frente:** enum completo de **7 módulos** com quem tem o quê · mapa de
  **atendimento** das 17 contas ativas · **razão de pessoas datado em 17 clientes**, do campo
  `Quem solicitou?` das 985 demandas.
- 🔴 **A CAEDU mudou de `Ongoing` para `Onboarding` em 22/09/2026, às 15:04** — entre duas
  leituras minhas do mesmo dia. **Perguntar o motivo antes de retomar a frente dela.**
- ⚠ **Quando o acesso da CAEDU sair**, o tratamento de dado sensível está definido em § 8.1.

## 7 · Próximos passos, em ordem

1. 🔵 **Resolver o campo `Participantes` das 1.161 reuniões** — são IDs de usuário do Notion;
   resolver com `get-users` dá **presença nominal com data**, a melhor fonte de pessoa ativa que
   ainda não foi extraída.
2. 🔵 **Varrer as páginas de cliente dos 27 sem demanda** — para eles a varredura de pessoas
   **não acrescentou nada**, e a página é a única fonte restante.
3. 🚨 **Credenciais:** as duas expostas (NK STORE, Lofty Style) **e a varredura das 1.153 atas
   não abertas**.
4. 🔴 **Perguntar ao Vinicius por que a CAEDU virou `Onboarding` hoje.**
5. 🔴 **Criar o campo `Data de Churn`** — segue sendo a lacuna mais cara do corpus.
6. 🔴 **Decidir a chave de identidade de pessoa** (item 252) — sem ela, as grafias não têm
   como ser resolvidas sem inventar gente.
7. 🔵 **Retomar a CAEDU** assim que o acesso sair.

## 8 · Decisões esperando o Vinicius

🔴 **O dono deste assunto é o [`_pendencias-gerais.md`](uMode/00_Institucional/_contexto/_pendencias-gerais.md)
— 248 itens datados.** **Não crie tabela de pendência aqui nem em lugar nenhum: escreva lá.**

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

### 8.1 · O tratamento de dado sensível que eu vou aplicar por padrão

**Reuso o vocabulário `disclosurePolicy` que já existe** no
[`_espec-pessoas-e-comunicacoes.md`](uMode/00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md),
em vez de inventar outro:

| Classe | O que faço |
|---|---|
| **Nome, cargo, área, papel no projeto** | entra normalmente · `INTERNAL_ONLY` |
| **Escopo, marco, entrega, decisão, prazo** | entra normalmente |
| **Valor de proposta, preço, margem, condição comercial** | **entra com `NEVER_TO_THIRD_PARTY`** e fica **só** em `00_Institucional/_contexto/` do cliente |
| **Telefone pessoal, CPF, e-mail pessoal** | 🔴 **não entra.** Registro que existe na fonte e onde |
| **Senha, token, chave, string de conexão** | 🔴 **nunca entra, em hipótese nenhuma** |

⚠ **Se o Vinicius quiser regra diferente para valor comercial, é só dizer** — até lá, aplico esta.

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
