---
aliases:
  - "Varredura 22 set 2026 (i) — o diário de bordo por cliente, e o que ele já corrigiu"
---
# Varredura 22 set 2026 (i) — o diário de bordo por cliente, e o que ele já corrigiu

> Cobrança do Vinicius, textual: *"preciso que registre todos os locais de onde já vasculhou pra
> evitar ficar repetindo buscas... Isso é perda de tempo e de token."* E: *"cliente por cliente
> você tenha um local e um arquivo onde defina cada ponto que você tem. Inclusive os de risco de
> segurança."*
>
> **Classe: `REGISTRO`.** Evidência datada. **Não é autoridade e não se edita.**
>
> 🔴 **Este documento é curto de propósito.** O detalhe de cada cliente **não vive aqui** — vive
> em `_Clientes/<Cliente>/00_Institucional/_contexto/_pendencias-e-fontes.md`.

## 1 · O que passou a existir

**48 arquivos `_pendencias-e-fontes.md`, um por cliente.** Cada um responde duas perguntas e
só elas: **"o que ainda não sei deste cliente?"** e **"onde eu já procurei?"**

| Seção | O que guarda |
|---|---|
| § 1 | **risco de segurança**, com estado |
| § 2 | pendências abertas, **com tier** e com o que destrava cada uma |
| § 3 | 🔴 **o diário: fontes JÁ varridas — não reabrir** |
| § 4 | fontes conhecidas e **ainda não** varridas |

> **Ele existe porque a memória da conversa compacta e a do disco não.** Compactou, eu repeti
> busca. **O diário em disco é a única memória que não compacta.**

**Estado hoje: 4 páginas de cliente abertas de 49** — CAEDU, Osklen, NK STORE, Reserva.

## 2 · 🔺 O tier passa a ser `T0`/`T1`/`T2`

Eu vinha usando rótulos meus — `INTERNAL_ONLY`, `NEVER_TO_THIRD_PARTY`. **Era uma segunda
taxonomia para a mesma coisa**, exatamente o defeito que o corpus critica.

| Tier | O que é | O que entra |
|:-:|---|---|
| `T2` | equipe | o padrão |
| `T1` | restrito | valor, preço, margem, escopo confidencial — **só no `_contexto/` do cliente** |
| `T0` | privado | 🔴 **nunca por valor** — CPF, telefone, senha, token. **Entra por referência** |

⚠ **Adotei o rótulo, não o mecanismo** — a restrição de não copiar nada do vault continua valendo.
**Vocabulário comum era o ponto.**

## 3 · 🔺 CORREÇÃO — não existe "o template de pessoa da página do cliente"

O registro **(h)**, escrito horas antes, afirmou que *"existe um template de pessoa na página do
cliente"*, com base em **Osklen e NK STORE**.

> 🔴 **A Reserva não tem o toggle `Pessoas`.** As pessoas dela aparecem **soltas, dentro dos nomes
> dos grupos de WhatsApp** — Claudinha (Compras), Raquel (Engenharia/Cadastro), Adriana (Estilo),
> Bruno (Sourcing), Ju. **Sem cargo formal em lugar nenhum.**

**Dois casos são hipótese, três são padrão** — e o terceiro caso desmentiu. **Há pelo menos duas
estruturas de página de cliente**, e qual delas o cliente tem **só se sabe abrindo**.

**O que continua valendo de (h):** onde o toggle existe e está preenchido, ele traz cargo e área.
**O que cai:** a ideia de que basta procurar o toggle.

## 4 · 🔺 CORREÇÃO — eu gerei ferramenta de dois enums, e o corpus já tinha um terceiro

As 16 fichas de ferramenta saíram de `Módulos Contratados` e `ERP/Integração`.

> 🔴 **O `_espec-pessoas-e-comunicacoes.md` já trazia o enum `tool`:** `Notion` · `WhatsApp` ·
> `Gist` · `Miro` · `Kanbanize` · `Google Drive` · `YouTube`. **Eu não o usei.**

**É pior que esquecer uma fonte: é não aplicar a regra que eu mesmo tinha acabado de escrever** —
*"enum de fonte é fonte de entidade"* — no lugar onde ela já valia, dentro do próprio corpus.

**Corrigido: 16 → 23 fichas de ferramenta**, em três naturezas:

| Natureza | Onde | Quantas |
|---|---|---:|
| Módulo que a uMode vende | `03_Produto-e-Solucoes/_ferramentas/` | 7 |
| ERP / sistema de terceiro | `06_Tecnologia/_ferramentas/` | 9 |
| 🆕 Canal / ferramenta de trabalho | `06_Tecnologia/_ferramentas/` | **7** |

⚠ **As 7 novas nascem com lista de clientes vazia, e a ficha diz por quê:** nenhuma base declara
quem usa Miro ou WhatsApp. **O vínculo vem de citação em página** — e só existe onde a página foi
aberta. **Vazio ali significa "não varrido", nunca "não usado".**

## 5 · 🔴 O achado da Reserva: uma fonte de demanda inteira, jamais tocada

A página da Reserva cita **`umode.kanbanize.com`, boards 6 e 18, com 7 cartões por ID** — 2
fechados, 5 abertos, com temas concretos (lentidão de filtro, exportação do Mapa, inativar
variantes de material, erro de filtro de composição, carta-lacre).

> 🔴 **Cartão de demanda de cliente vive no Kanbanize, e nenhuma varredura tocou o Kanbanize.**
> As 999 demandas do corpus vêm da base do Notion. **Não sei quanto as duas se sobrepõem.**

**E mais três coisas que só a página diz:**

1. **Canal oficial declarado:** demanda nova por **formulário**; dúvida de usabilidade pelo
   **Gist**. **Média declarada: 1 chamado/dia, 2 reuniões/semana.**
2. 🔴 **A cadência de `Review Quinzenal de Projeto` parou.** Envios marcados até **30/06**;
   **15/07, 02/08 e 21/08 seguem sem marca.** Responsável declarado: **João**.
3. 🔴 **5 dos 9 grupos de WhatsApp estão marcados para excluir e continuam existindo.**

## 6 · O que muda no protocolo

1. 🔴 **Ler `_pendencias-e-fontes.md` do cliente ANTES de varrer.** É a trava contra repetir busca.
2. 🔴 **Não concluir padrão com dois casos.** Duas páginas concordaram e a terceira desmentiu.
3. 🔴 **Antes de varrer fonte externa, varrer o corpus** — o enum `tool` estava aqui dentro.
4. **Fonte de demanda não é uma só.** Notion, Kanbanize, Gist, WhatsApp e formulário coexistem,
   e **nenhuma varredura anterior sabia disso.**

## Governança

### Quem pode alterar este documento
🔴 **Ninguém.** É `REGISTRO`.

### Procedência

| Bloco | Fonte | Data |
|---|---|---|
| §1, §2 | pedido do Vinicius nesta sessão + `scripts/gera-pendencias-e-fontes.py` | **22 set 2026** |
| §3, §5 | Notion — página `Reserva` (`1be19527…`), **aberta por inteiro** | **22 set 2026** |
| §4 | `_espec-pessoas-e-comunicacoes.md`, enum `tool` — **já no corpus** | **22 set 2026** |
