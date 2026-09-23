---
aliases:
  - "Varredura 22 set 2026 (m) — o modelo de usuário do uFlow, e `uDash` é perfil interno"
---
# Varredura 22 set 2026 (m) — o modelo de usuário do uFlow, e `uDash` é perfil interno

> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**
>
> Fonte: `Controle de Acessos de Usuários`, em `uModers / Vinícius Risoleo / Assunto | Ferramenta`.
> **Escrita pelo próprio Vinícius, com as perguntas já respondidas.** Última edição: **13/05/2026**.

## 0 · Por que isto importa

O corpus tem o dicionário de dados do **BrainHub** (Mongo, `_dicionario-dados-brainhub.md`).
🔴 **Não tinha nada sobre o modelo de dados do uFlow** — a plataforma que os clientes usam.

**Esta página é isso, e com as regras de negócio confirmadas por quem decide.**

## 1 · 🔺 CORREÇÃO — `uDash` é PERFIL INTERNO da uMode `[C]`

No item **406** eu registrei: *"`uDash` é PRODUTO CONTRATADO aqui"*, a partir de
*"13 usuários uFlow / 2 usuários uDash"* na Luiza Barcelos.

> 🔴 **Errado.** A página lista, entre os **filtros de exclusão** da análise de acesso:
> *"os perfis `uRocket` e `uDash` são sempre internos"* — **confirmado com checkbox marcado.**

**O que isso significa de verdade:** os *"2 usuários uDash"* da Luiza Barcelos **não são licenças
vendidas ao cliente — são acessos da própria uMode dentro da conta dele.**

⚠ **E resolve a ambiguidade que eu tinha registrado:** `uDash` aparecia como **perfil** na VIX e
eu achei que era **produto** na Luiza Barcelos. **É perfil nos dois casos.** O nome de produto
legado existe, mas **não é isso que essas linhas dizem.**

🆕 **`uRocket` também é perfil interno**, e a página anota: *"demanda não mais necessária
(cancelamento serviço)"*.

## 2 · As tabelas reais do uFlow `[C]`

| Tabela | O que é | Campos citados |
|---|---|---|
| **`jumper_users`** | o usuário | `id` · `name` · `email` · `status` · `created_at` · **`last_sign_in_at`** · `master` · `deleted_at` |
| **`jumper_entities`** | 🔴 **a CONTA — é o cliente** | `id` · `name` |
| **`user_roles`** | o vínculo usuário↔conta↔perfil | `id` · `status` · `created_at` · `updated_at` · `deleted_at` |
| **`policies`** | 🔴 **o PERFIL** | `id` · `name` |
| **`ahoy_visits`** / `ahoy_events` | telemetria de acesso | `started_at` |
| **`audits`** | 🔴 **auditoria — existe** | modelo `J3::UserRole` |

> 🆕 **O prefixo `jumper_` e o namespace `J3` dizem que a plataforma se chama `Jumper` no
> código.** ⚠ **O corpus nunca registrou esse nome.**

## 3 · As regras de negócio, confirmadas `[C]`

**Todas com checkbox marcado na fonte — ou seja, perguntadas e respondidas.**

| Regra | Valor confirmado |
|---|---|
| **Usuário ativo** | 🔴 **`ju.status IS NULL`** — e a fonte confirma explicitamente: *"é a regra oficial da plataforma, não uma exceção"* |
| Valores possíveis de `ju.status` | apenas `NULL`, `0` e `1` — **nada além** |
| **Role ativa** | `ur.status = 1` **e** `ur.deleted_at IS NULL` |
| `ju.master = 1` | admin global da plataforma |
| Contas internas | 🔴 **`entity_id` `935` e `69`** |
| Perfis internos | 🔴 **`uRocket`** e **`uDash`** |
| E-mails excluídos | `umode`, `victoraragao`, `berg` e outros, **via `NOT LIKE`** |
| **`API` conta como usuário válido** | ✅ decidido |

⚠ **`ju.status IS NULL` significar "ativo" é contraintuitivo o bastante para a própria fonte
precisar perguntar duas vezes.** **Qualquer análise que trate `NULL` como ausência de dado vai
contar errado.**

## 4 · 🔴 A métrica que falta no corpus: engajamento

A fonte propõe, e explica por quê:

> *"adicionar uma coluna de **taxa de engajamento** (usuários que acessaram no mês atual /
> usuários ativos) — dá uma leitura rápida de **quais contas estão dormentes** antes mesmo de
> entrar nelas"*

E, sobre o gráfico:

> *"a distância entre 'ativos' e 'acessaram' é exatamente **o indicador de engajamento que mais
> interessa ao gestor**"*

🔴 **O corpus mede conta por demanda e por chamado. Nenhuma das duas é acesso.** E já sabemos
que chamado depende de ter o botão liberado (registro **k**). **Engajamento por acesso é a única
medida que não depende de permissão nem de vontade de abrir chamado.**

## 5 · ⚠ Duas medidas de "último acesso" que divergem — e a fonte diz por quê

| Campo | O que é |
|---|---|
| `last_sign_in_at` | **login de fato** — entrou com e-mail e senha |
| `ultima_visita` (`ahoy_visits`) | **última navegação na sessão logada** — pode ser a mesma sessão aberta por uma semana |

> *"uma informação vem de uma tabela e a outra vem de outra tabela. **Temos algumas divergências
> disso nítidas**, mas pode ser por conta de problemas no próprio registro."*

🔴 **Registro isso porque toda ficha de pessoa que eu vier a preencher com "última atividade"
precisa dizer qual das duas está usando.**

## 6 · O que a fonte deixa aberto

| Item | Estado |
|---|---|
| Dash: lista de contas válidas da uMode | ⬜ **não feito** |
| Dash: gráfico mensal comparando as 15 maiores contas | ⬜ **não feito** |
| Validação com `entity_id = 3344` | **41 usuários ativos, 16 roles ativas** — 🟢 **é a BAW**, confirmado pelo Vinícius em 22 set 2026 `[D]` |

🆕 **`Flávia`** aparece como autora das sugestões. ⚠ **Não crio ficha: um nome de seção não é
fonte suficiente** — mesma régua do Felipe Sindeaux, que só nasceu depois da confirmação.

## 7 · 🔺 `entity_id = 3344` é a BAW — e eu tirei daí uma conclusão que não cabia

**O Vinícius confirmou que `3344` é a Baw. E corrigiu o uso que eu fiz disso**, textual em
22 set 2026: *"É dado do banco. Não é relevante essa informação no contexto. Somente pra você
identificar de onde era o contexto que está consultando."* `[D]`

> 🔴 **O que eu tinha escrito e está ERRADO:** que os *"41 usuários ativos e 16 roles
> ativas"* eram a **sexta evidência, e a primeira quantitativa**, de que a Baw está mal
> classificada.

**Por que está errado:** aqueles números são **contagem esperada de uma query de validação**,
escrita para conferir se o SQL devolvia o mesmo que uma planilha. É **fixture de teste**,
no contexto de mai/2026. **Não é medição do estado da conta, e eu tratei como se fosse.**

**O erro tem nome:** peguei um **identificador técnico dentro de um exemplo** e transformei em
**leitura de negócio**. É primo do erro de tratar estado em sistema descontinuado como estado.

### O que fica de verdade

| | |
|---|---|
| `entity_id` | **chave do banco.** Serve para saber **de qual conta um exemplo fala** |
| Os 41/16 | **número de conferência de query**, de mai/2026. **Não entra como fato de conta** |
| A classificação da Baw | segue com **cinco** evidências qualitativas, **não seis** |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| tudo | Notion — `Controle de Acessos de Usuários` (`322b1d38…`), **aberta por inteiro** | **22 set 2026** |
| §1 | cruzamento com o registro da VIX e da Luiza Barcelos, lidos no mesmo dia | **22 set 2026** |
