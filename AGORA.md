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

**Ferramenta de padrão:** `scratchpad/propaga.py` verifica as 4 classes de MD e recompõe
títulos canônicos faltantes. **Rodar sempre antes de commitar.**

## 4 · Onde está cada coisa

| Arquivo | O que é | Quando ler |
|---|---|---|
| **`AGORA.md`** | este arquivo — orientação | **primeiro, sempre** |
| `CLAUDE.md` | papel, regras invioláveis, como executar | antes de qualquer tarefa |
| `CONTEXT.md` | decisões de arquitetura travadas | antes de mapear campo ou taxonomia |
| `STATE.md` | histórico completo, sessão a sessão | quando precisar do detalhe de algo |
| `START.md` | protocolo de abertura de sessão | primeira mensagem da sessão |

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

## 6 · O que está sendo feito agora

🔵 **Frente ativa: contextualização total do projeto CAEDU**, para atualizar o cérebro daquela
empresa e preparar a semana seguinte.

- **Combinado com o Vinicius em 22 set 2026.** Ele vai entregar a lista de fontes de contexto da
  CAEDU — propostas, nomes, escopo, reuniões.
- **A CAEDU já foi varrida uma vez** (19–21 set, commits `525a27b` e `3dd8ae8`): 47 MDs,
  14/14 áreas, 93 usuários em 14 perfis, 18 marcos datados. **Esta frente é aprofundamento, não
  recomeço.**
- ⚠ **Haverá dado sensível de proposta comercial.** Tratamento acordado em § 8.

## 7 · Próximos passos, em ordem

1. 🔵 **Receber e organizar as fontes de contexto da CAEDU** — é a frente ativa.
2. 🚨 **Rotacionar as duas credenciais expostas** — NK STORE (banco de produção) e Lofty Style.
   **É o único item com prazo de segurança.**
3. 🚨 **Varrer credencial nas 1.153 atas não abertas.**
4. 🔴 **Criar o campo `Data de Churn`** — sem ele não há tempo de vida de cliente nem taxa de
   churn por coorte. **É a lacuna mais cara do corpus.**
5. 🔴 **As 121 reuniões não lidas da Luiza Barcelos** (2024–2025).
6. 🔴 **Reconciliar as duas listas de cliente do Notion**, nos dois sentidos.

## 8 · Decisões esperando o Vinicius

> **Nada aqui está bloqueando trabalho.** São escolhas que só ele pode fazer.

| # | Decisão | Onde está o material |
|---|---|---|
| 1 | Criar a área `15_Producao-Interna`? **5 clientes** têm produção interna sem área | `_proposta-grade-de-areas-revisao.md` |
| 2 | `Merchandising` atingiu **3 clientes** — vira área? Eu **recomendo que não**, porque os três escopos diferem | idem |
| 3 | `Precificação` não tem área canônica | [`_Clientes/Luiza Barcelos/.../institucional.md`](uMode/_Clientes/Luiza%20Barcelos/00_Institucional/_contexto/institucional.md) |
| 4 | Separar `Status` em `lifecycleStage` / `serviceMode` / `recordKind`? | `_taxonomia-status-cliente.md` |
| 5 | A **Baw** está classificada certo? `Sem CS` com 4 módulos, 19 reuniões e 18 demandas | [`_Clientes/Baw/.../jornada.md`](uMode/_Clientes/Baw/00_Institucional/_contexto/jornada.md) |
| 6 | Reunião que atende **dois clientes** — dois registros ou um com duas relações? | [`_varredura-2026-09-22-reunioes-compartilhadas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-22-reunioes-compartilhadas.md) § 6 |
| 7 | `## O que este documento NÃO resolve` vira canônico nas 4 classes? **Muda 145 arquivos** | — |
| 8 | **Como tratar dado sensível de proposta comercial** — ver abaixo | — |

### 8.1 · O tratamento de dado sensível que eu vou aplicar por padrão

**Já existe vocabulário para isso** no `_espec-pessoas-e-comunicacoes.md` — vou usá-lo em vez de
inventar outro:

| Classe | O que faço |
|---|---|
| **Nome, cargo, área, papel no projeto** | entra normalmente · `disclosurePolicy: INTERNAL_ONLY` |
| **Escopo, marco, entrega, decisão, prazo** | entra normalmente |
| **Valor de proposta, preço, margem, condição comercial** | **entra com `NEVER_TO_THIRD_PARTY`** e fica **só** em `00_Institucional/_contexto/` do cliente |
| **Telefone pessoal, CPF, e-mail pessoal** | 🔴 **não entra.** Registro que existe na fonte e onde |
| **Senha, token, chave, string de conexão** | 🔴 **nunca entra, em hipótese nenhuma** |

⚠ **Se o Vinicius quiser regra diferente para valor comercial, é só dizer** — até lá, aplico esta.

## 9 · Como manter este arquivo vivo

**Este arquivo mente rápido se ninguém o atualizar.** A regra:

- **Toda sessão que gera commit atualiza `AGORA.md`** — no mínimo a data, o commit, os números
  da § 5 e as listas das § 6 e § 7.
- **`AGORA.md` é resumo, `STATE.md` é histórico.** O que aconteceu vai para a `STATE.md`;
  o que **vale agora** vive aqui. **Nada de histórico neste arquivo.**
- **Se este arquivo divergir da `STATE.md`, a `STATE.md` ganha** — e aí este aqui está com
  defeito e precisa ser corrigido na hora.
