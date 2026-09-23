---
aliases:
  - "Varredura 22 set 2026 (d) — o CX Hub como referência de desenho, e o placar dos avanços"
---
# Varredura 22 set 2026 (d) — o CX Hub como referência de desenho, e o placar dos avanços

> Instrução do Vinicius: *"o repositório do CX Hub te proporciona a possibilidade de levantar
> praticamente todas as demandas em níveis de fechamento, abertura, o que é RFI também...
> Investigue."* E, no meio da investigação: *"essa parte do CX praticamente não terá dado. Já
> estou te adiantando. A feature foi colocada, mas nunca finalizada de fato."* `[D]`
>
> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**

## 0 · Declaração de completude

| # | Lacuna | Situação |
|---|---|---|
| 1 | 🔴 **Dado de demanda/RFI no CX Hub** | **Não existe** — a feature nunca foi finalizada, dito pelo Vinicius. **Li 170 migrations; os `INSERT` são todos de configuração.** |
| 2 | **Cargo e área por pessoa** | 🔴 **Continua sem fonte.** O CX Hub **também não tem** — `user_profiles` só carrega `global_role` com 3 valores |
| 3 | **Páginas dos 33 clientes sem pessoa** | 🔴 **A fonte que eu propus NÃO EXISTE** — ver § 3 |
| 4 | **Sub-páginas dos clientes em churn** | ⚠ não abertas — é onde a pessoa pode estar |

## 1 · 🟢 O CX Hub não serve como fonte de dado — serve como referência de desenho

**E isso vale mais para o objetivo declarado** (*"fazer nosso conteúdo já conhecido caber lá"*).
**O schema já modela boa parte do brain que o Vinicius descreveu.** `[C]`

### 1.1 · O enum de plataforma é o mapa das fontes de contexto

```sql
CREATE TYPE public.platform_type AS ENUM
  ('gist', 'stripe', 'linear', 'notion', 'tudo1', 'whatsapp', 'slack', 'custom');
```

> 🟢 **É literalmente a lista de fontes que o Vinicius descreveu** — WhatsApp, Notion, Slack.
> ⚠ **`tudo1` e `stripe` são novos para o corpus.** **`linear` confirma** o achado da Luiza Barcelos.

### 1.2 · A esteira de ingestão já está tipada

```sql
CREATE TYPE public.job_type AS ENUM
  ('sync_contacts', 'ingest_historical', 'classify_batch', 'transcribe_audio');
```

> 🟢 **`transcribe_audio` · `classify_batch` · `ingest_historical`** — **é o "moer conteúdo para
> saber que demandas gerou"**, já nomeado em schema. **Não está funcionando; está desenhado.**

**E há as tabelas que fecham o ciclo:** `demand_origins` · `demand_origin_links` ·
`demand_conversation_summaries` · `demand_ai_analyses`.

### 1.3 · O permissionamento existe e é por cliente

```sql
INSERT INTO user_client_access (user_id, client_id, role) ...
CREATE TRIGGER on_client_created ... EXECUTE FUNCTION grant_new_client_to_all_users();
```

- 🟢 **Acesso é `(usuário × cliente × role)`** — **confirma a decisão do Vinicius de que a
  hierarquia máxima é o cliente.**
- 🔴 **Mas o trigger dá `viewer` de TODO cliente novo para TODOS os usuários.** **O padrão é
  ver tudo.** Para o brain que ele descreveu, **o padrão precisa ser o inverso.**
- 🔴 **`user_profiles.global_role` tem 3 valores: `admin` · `analyst` · `viewer`.**
  **Não há `cargo`. Não há `área`.** **A lacuna nº 5 do painel continua aberta.**

### 1.4 · 🔴 Status de demanda no CX Hub é COLUNA DE KANBAN, não enum

```sql
demands.column_id UUID REFERENCES ticket_columns(id) NOT NULL
ticket_columns (name, position, triggers_started_at, triggers_finished_at)
```

> **O estado de uma demanda é a posição dela num board**, e `started_at`/`finished_at` são
> **disparados pela coluna**. **Estruturalmente diferente do campo `Etapa` do Notion**, que é
> um select. **Duas taxonomias, nunca fundidas** — vale a regra do `CLAUDE.md`.

### 1.5 · 🔴 O enum de RFI do CX Hub tem QUATRO valores — o corpus tem ONZE

```sql
INSERT INTO rfi_statuses (name, color, position) VALUES
  ('Previsto', 0), ('Orçada', 1), ('Aceito', 2), ('Recusada', 3);
```

| Fonte | Valores |
|---|:-:|
| **CX Hub** (schema) | **4** — `Previsto` · `Orçada` · `Aceito` · `Recusada` |
| **Corpus** (do Notion) | **11** — `RFI Entregue ao Cliente` · `RFI Post Mortem` · `RFI Cancelada` · … |

> 🔴 **Dois vocabulários de RFI, sem mapeamento declarado.** **Não fundi.**
>
> 🔴 **E uma diferença estrutural maior que o enum:** no CX Hub,
> **`rfis.demand_id NOT NULL UNIQUE REFERENCES demands(id)`** — **uma RFI é 1:1 com uma demanda.**
> **No corpus, RFI e Demanda são entidades separadas com vínculo opcional** (44 de 999 vinculadas).
> **É decisão de modelo, não detalhe.** `[D]` **do Vinicius.**

⚠ **E a RFI do CX Hub carrega dinheiro:** `budget_value numeric(12,2)` e `due_date`.

## 2 · 🔴 Um tier de cliente com nome de grupo

```sql
CREATE TYPE public.client_tier AS ENUM ('azzas', 'enterprise', 'medium', 'small');
```

**Três dos quatro valores são porte. O quarto é o nome de um grupo econômico.**
> ⚠ **Não sei o que `azzas` significa neste enum** e não presumo. **Mas é anomalia de taxonomia:
> um enum de porte com um nome próprio dentro.**

## 3 · 🔴 A fonte que eu propus como próximo passo NÃO EXISTE

No painel de prontidão eu escrevi que o próximo passo de maior rendimento eram
**"as páginas dos 33 clientes sem pessoa nenhuma"**. **Fui verificar antes de executar:**

**Apenas 9 clientes têm `Documentação Clientes` preenchida** — e **8 deles já foram varridos a
fundo** (Recco, Osklen, Lofty, NK STORE, NV, Luiza Barcelos, Highstil, Lenny Niemeyer). O nono é
o **template**.

> 🔴 **Os 33 clientes sem pessoa também não têm página de documentação.** **O próximo passo que
> eu propus ia atrás de uma fonte inexistente.** Corrigido antes de custar uma rodada.

**O que existe para eles:** o **corpo da própria página do cliente**, que tem **sub-páginas**.
Testei na **Vivara**: nenhuma pessoa no corpo, mas **cinco sub-páginas** —
`Reonboarding Vivara` · `Onboarding > Ongoing` · `Miro Regras e restrições` · `Onboarding` ·
`Playbook` — **mais uma database inline**.

> 🔴 **E aí um achado: a Vivara está marcada `Churn` e tem uma página `Reonboarding Vivara`.**
> **É reentrada, não conta morta.** **Sétimo caminho independente mostrando que `Status` ≠ realidade.**

## 4 · 📊 Placar — para eu lembrar de onde vim

**Ponto de partida desta sequência: 21 set 2026, 2 de 46 clientes varridos.**

| Métrica | 21 set | **22 set (hoje)** |
|---|---:|---:|
| Clientes no corpus | 46 | **48** |
| Clientes com `contexto-area.md` 14/14 | 2 | **48** |
| MDs em `uMode/` | 1.229 | **2.020+** |
| **Clientes com as 8 dimensões respondidas** | 0 | **12** |
| **Clientes com pessoa nomeada e datada** | 2 | **18** |
| **Pessoas com e-mail individual** | 0 | **92** |
| Bases do Notion varridas | 4 | **7** |
| Decisões pendentes registradas | 233 | **283** |
| `.md` estruturais, todos classificados | ⚠ **não havia manifesto** | **71/71** |
| Verificadores automáticos | 1 | **2** |

**Fontes novas descobertas hoje:** `Reuniões Compartilhadas` (1.161) · `Chamados & Atendimentos`
(185) · schema do CX Hub (170 migrations) · `Linear` · `Timec` · `Mold` · `tudo1` · `stripe`.

**Erros meus corrigidos hoje, todos registrados:** o coorte de fev/2025 · a Luiza Barcelos
"invisível" · a contagem de atas (9→8) · a chave de identidade "inexistente" · a duplicação do
`AGORA.md` × `_pendencias-gerais.md` · e **a fonte inexistente deste § 3**.

## 5 · Próximos passos — revisados pelo que se aprendeu

| # | Passo | Por quê |
|---|---|---|
| 1 | **Sub-páginas dos clientes** (`Onboarding`, `Playbook`, `Reonboarding`) | **é onde pessoa e área podem estar** para os 33 sem ninguém |
| 2 | **Databases inline** nas páginas de cliente | a Vivara tem uma; **não foi aberta** |
| 3 | 🔴 **Perguntar ao Vinicius onde vive `cargo` e `área` de pessoa** | **varri 7 bases e nenhuma tem** — **pode não existir em lugar nenhum** |
| 4 | **1.153 atas não lidas** | pauta, pendência e decisão por encontro |
| 5 | **Confrontar `platform_type` do CX Hub com `communication_channels` da espec** | **antes de travar o nosso enum de canal** |

> 🔴 **O item 3 é o mais importante e é pergunta, não tarefa.** Já procurei em: `Mapa de
> Clientes`, `Demandas`, `Chamados`, `Reuniões`, `Portal do Cliente`, páginas de cliente e o
> schema do CX Hub. **Cargo e área de pessoa não estão estruturados em nenhuma.**
> **Se não existe fonte, isso não é lacuna de varredura — é dado a ser criado.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| §1, §2 | `CX Hub/gist-sparkle-d86e356b` — 170 migrations, **somente leitura** | **22 set 2026** |
| §3 | Notion — `Mapa de Clientes` (campo `Documentação Clientes`) + página da Vivara | **22 set 2026** |
| §4 | corpus + `STATE.md` | **22 set 2026** |
