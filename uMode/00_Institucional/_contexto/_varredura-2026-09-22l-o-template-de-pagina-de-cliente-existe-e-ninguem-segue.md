---
aliases:
  - "Varredura 22 set 2026 (l) — o template de página de cliente existe, e ninguém o segue"
---
# Varredura 22 set 2026 (l) — o template de página de cliente existe, e ninguém o segue

> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**

## 0 · 🔺 Correção de algo que eu escrevi hoje mesmo

No registro **(i)** eu escrevi, em caixa alta: *"não existe 'o template de pessoa da página do
cliente'"*. Cheguei a isso porque Osklen e NK STORE tinham o mesmo toggle e a Reserva não tinha
nenhum.

> 🔴 **O template existe.** Chama-se **`. Página Cliente [Template]`**, vive dentro do próprio
> `Mapa de Clientes` com `Status = Inativo`, e tem **oito blocos definidos**. `[C]`

**O que eu concluí errado foi a causa.** Não é que não haja template — **é que quase ninguém o
segue, e quem segue seguiu versões diferentes dele.**

⚠ **E a conclusão prática de (i) continua valendo:** **não dá para prever a estrutura de uma
página de cliente sem abri-la.** O motivo é outro, o efeito é o mesmo.

## 1 · Os oito blocos do template `[C]`

| # | Bloco | Estado no template |
|--:|---|---|
| 1 | **`Pessoas`** | 3 sub-blocos: `Responsável pelo Financeiro` · `Responsáveis pelos Projetos` (Diretoria / Líderes do Projeto / Líderes de Departamentos) · `Responsável Tecnologia` |
| 2 | `Jornada do Cliente e seus Marcos` | rótulos, sem conteúdo |
| 3 | `Documentos Implantação uFlow` | **11 itens nomeados**, incluindo `Perfil de Usuários e Permissionamentos` |
| 4 | 🔴 **`Regras e Definições do Cliente`** | **vazio** |
| 5 | `Reuniões Compartilhadas com Cliente` | database |
| 6 | `Demandas compartilhadas com Cliente` | database (`collection://ae2c893a-…`) |
| 7 | 🔴 **`Atendimento e Suporte`** | `Aprendizados e Anotações Importantes` + **`Regras de Aprovação e Inclusão de Usuários`** (database) |
| 8 | `CRM → Anotações Gerais` | vazio |

🔴 **Última edição do template: 16/07/2025.** **Mais de um ano.**

## 2 · 🔴 O template NÃO tem `Diretores e Representantes Legais` — e quatro clientes têm

| Cliente | Tem o bloco de diretores? |
|---|:-:|
| **O template** | 🔴 **não** |
| NK STORE · Osklen · Lofty Style · Moda Objetiva | ✅ **sim** |

**Ou o template envelheceu, ou quatro clientes o ampliaram por conta.** ⚠ **Não sei qual — e a
diferença importa, porque é onde mora o Representante Legal.**

## 3 · 🔴 Nenhuma das 15 páginas que abri tem os oito blocos

**O bloco 7, `Atendimento e Suporte`, é o mais revelador.** Ele prevê
**`Aprendizados e Anotações Importantes`** — que é exatamente onde deveria estar coisa como
*"Se ela está feliz com o projeto, estamos bem"* (NK STORE) ou o aprendizado de permissão da VIX.

> **Esses aprendizados existem, e estão espalhados em lugares improvisados** — dentro de uma
> célula de tabela, no fim de uma página de permissão, num comentário de validação.
> **O lugar certo estava desenhado desde o começo.**

## 4 · 🆕 `Regras de Aprovação e Inclusão de Usuários` — e há limite contratado

O bloco 7 traz uma database com esse nome. E o **`Playbook Cadastro de Novos Usuários uFlow`**
(em `Databases / Processos mapeados`) registra, textual:

> *"livre dentro do **limite contratado**, o KA precisa aprovar com o líder do cliente a
> contratação de mais usuários"*

🔴 **Há limite contratado de usuários, e o corpus não tem esse número para cliente nenhum.**
Isso muda a leitura de dois achados: a **Puket com 43 usuários e 2 módulos**, e a **NV com
61 usuários declarados**.

## 5 · Mais fontes que a busca revelou e que ninguém varreu

| Fonte | Onde | Por que importa |
|---|---|---|
| 🔴 **`Controle de Acessos de Usuários`** | `uModers / Vinícius Risoleo / Assunto \| Ferramenta` | **lista de contas com total de usuários ativos e % de engajamento** (quem acessou no mês ÷ ativos). **O corpus não tem métrica de engajamento.** |
| **`Databases / Processos mapeados`** | base própria | onde vive o `Playbook Cadastro de Novos Usuários` |
| **`Databases / Demandas de Clientes`** | base própria | ⚠ **é a mesma base das 999 demandas, ou outra?** |
| **`Operation Hub`** | `Operação de Clientes` | cita **`documentacao.umode.tech`** — 🔴 **segundo domínio de documentação**, além do `docs.umode.app` da Lofty |
| **`uFlow / Documentação de Setup - PLM`** | já registrado em (k) | tem documentação técnica real — `Menu Item`, permissão tipo `INCLUDES` |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §0–§3 | Notion — `. Página Cliente [Template]` (`197b1d38…`), **aberta por inteiro** | **22 set 2026** |
| §4, §5 | Notion — busca por `Departamento Cliente / Perfil do Usuário`, 13 resultados | **22 set 2026** |
