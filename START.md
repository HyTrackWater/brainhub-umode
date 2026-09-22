# START.md — o condutor da triagem

> **Cole isto como primeira mensagem de qualquer sessão:** `Leia START.md`
>
> Este arquivo faz três coisas e só três: **declara o time completo de documentação**, **dá a
> ordem de leitura** conforme a tarefa, e **fixa o que se atualiza ao fechar a sessão**.
> Ele não contém contexto de projeto — contém o roteiro para obtê-lo na ordem certa.

---

## 0 · As oito classes — o que a classe de um arquivo determina

**Todo `.md` deste repositório pertence a exatamente uma classe.** A classe decide **se você
lê**, **se você pode editar** e **se ele pode ser citado como autoridade**.

| Classe | O que é | Pode ser autoridade? | Pode editar? |
|---|---|:-:|:-:|
| **G · GOVERNANÇA** | conduz a sessão · vive na raiz | ✅ | ✅ |
| **A · AUTORIDADE** | **dono único de um assunto**, vivo | ✅ | ✅ |
| **P · PROTOCOLO** | como executar um procedimento | ✅ | ✅ |
| **R · REGISTRO** | **evidência datada de uma varredura** | 🔴 **NÃO** | 🔴 **NÃO** — imutável |
| **D · DIDÁTICO** | traduz o que outro documento já decidiu | 🔴 **NÃO** | ✅ |
| **T · TEMPLATE** | molde para gerar arquivo novo | 🔴 **NÃO** | ✅ |
| **X · DERIVADO** | gerado por script a partir dos MDs | 🔴 **NÃO** | 🔴 **NÃO** — regerar |
| **C · CORPUS** | os 4 MDs canônicos por cliente/área | ✅ (do seu cliente) | ✅ |

**As três regras que a tabela acima impõe:**

1. **Um assunto, um dono.** Se dois arquivos vivos decidem o mesmo assunto, **um está errado** —
   marque o perdedor como `SUPERSEDED` naquilo que perdeu, apontando o sucessor.
2. **REGISTRO nunca vira autoridade.** Uma varredura é foto com data. Se o que ela achou deve
   valer como regra, **isso vira parágrafo numa AUTORIDADE** — a varredura fica como prova.
3. **Antes de criar um `.md` novo, procure o dono do assunto.** Criar arquivo é o último
   recurso, não o primeiro. **Em 22 set 2026 eu errei exatamente aqui** — montei uma tabela de
   decisões pendentes no `AGORA.md` sem ter lido o `_pendencias-gerais.md`, que já era o dono
   com 233 itens. Corrigido: os itens foram para lá e o `AGORA.md` só aponta.

---

## 1 · O TIME — o conjunto completo, declarado

> **Este é o manifesto.** `scripts/valida-documentacao.py` confere que **todo `.md` estrutural
> do repositório está aqui** e que **todo item aqui existe no disco**. Se o script acusar
> divergência, **ou o arquivo é órfão, ou este manifesto está desatualizado** — resolva antes
> de seguir.

### G · Governança — 6 arquivos, na raiz, conjunto fechado

| Arquivo | Responde | Tamanho |
|---|---|---|
| **`START.md`** | **como me contextualizo e em que ordem** — este arquivo | curto |
| **`AGORA.md`** | **onde o projeto está hoje** — papel, método, cobertura, frente ativa, próximos passos | 1 tela |
| **`CLAUDE.md`** | **meu papel e as regras que não se quebram** | curto |
| **`CONTEXT.md`** | **as decisões de arquitetura travadas** — hierarquia, áreas, portfólio | médio |
| **`STATE.md`** | **o histórico**, sessão a sessão | ~2.800 linhas |
| **`README.md`** | porta de entrada para quem chega pelo GitHub | curto |

🔴 **Nenhum outro arquivo de governança deve existir na raiz.** Se aparecer um sétimo,
ou ele entra nesta tabela ou ele não devia ter sido criado.

### A · Autoridades — cada uma dona de um assunto

Todas em `uMode/00_Institucional/_contexto/`, salvo indicação.

| Arquivo | É dono de |
|---|---|
| `_espec-banco-brainhub.md` | **o banco** — collections, campos, relações, invariantes |
| `_espec-pessoas-e-comunicacoes.md` | **pessoas e comunicações no banco** — `SUPERSEDED` o anterior nesses temas |
| `_dicionario-dados-brainhub.md` | **o dicionário de dados** — o que existe hoje no código |
| `_fluxo-dados-brainhub.md` | **o fluxo de dados** — da escrita do MD ao ping na inbox |
| `_fluxo-crud-brainhub.md` | **hierarquias, endereçamento e demandas no banco** |
| `_taxonomia-status-cliente.md` | **o campo `Status` do cliente** |
| `_lista-clientes-reais.md` | **quem é cliente uMode de verdade** |
| `_inventario-repositorios.md` | **os repositórios e sistemas**, e o papel de cada um |
| `_proposta-grade-de-areas-revisao.md` | **a grade de áreas canônicas** e sua revisão |
| `_backlog-convergencia-brainhub.md` | **a convergência com o vault do João** |
| 🔴 `_pendencias-gerais.md` | 🔴 **TODA decisão que espera o Vinicius** — 248 itens |
| `institucional.md` | **a identidade da Casa uMode** |
| `uMode/06_Tecnologia/_contexto/_backlog-infra-tecnologia.md` | a infraestrutura de tecnologia |
| `uMode/04_Dados-e-IA/_contexto/uflow-modelo-de-dados.md` | o modelo de dados do uFlow |
| `uMode/04_Dados-e-IA/_contexto/_blueprint-boilerplate-governado.md` | o boilerplate governado |
| `uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow.md` | **o Agente de Suporte Técnico uFlow** — preserva fonte que saiu do disco |
| `uMode/04_Dados-e-IA/_contexto/agente-suporte-uflow-ficha-banco.md` | **o payload de inserção desse agente** nas collections `agents` e `agent_versions` |

### P · Protocolos — como executar

Em `uMode/00_Institucional/_protocolos/`:
`protocolo-varredura-cliente.md` · `protocolo-criacao-cliente.md` · `protocolo-gestao-demanda.md` ·
`protocolo-gestao-rfi.md` · `protocolo-gestao-integracao.md` · `protocolo-gestao-pessoas.md` ·
`protocolo-gestao-produto.md`

Em `uMode/04_Dados-e-IA/_protocolos/`:
`governanca-squad-desenvolvimento.md` · `contratos-agentes-por-dimensao.md` ·
`treinamento-e-contratos-squad.md` · `parecer-smartcoding-esteira-2026-09-02.md`

### R · Registros — evidência datada, 🔴 imutável, 🔴 nunca autoridade

`_auditoria-indexacao.md` · `_varredura-drive-notas.md` · `_varredura-ferramentas-produtos-areas.md` ·
`_varredura-2026-09-21-fontes-e-lacunas.md` · `_varredura-2026-09-22-reunioes-compartilhadas.md` ·
`_varredura-2026-09-22-pessoas-e-ferramentas-carteira.md` ·
`_varredura-2026-09-22b-chamados-e-identidade-de-pessoa.md` ·
`_varredura-2026-09-22c-painel-de-prontidao.md` ·
`_varredura-2026-09-22d-cx-hub-schema-e-placar.md` ·
`_levantamento-2026-08-19-repos-e-prd.md` · `_levantamento-2026-09-21-praticas-vault-e-caedu.md` ·
`_decisoes-convergencia-proposta.md` ·
⚠ `_recebido-2026-08-18-context-pack-brainhub-2.0.md` — **documento externo, do João/Codex: não é
nosso e não se edita em hipótese nenhuma.**

### D · Didáticos · T · Templates · X · Derivados

- **D:** `_como-o-brainhub-funciona.md` — traduz `_fluxo-dados` e `_dicionario`. **Não acrescenta
  desenho.** Metáfora só é permitida aqui, e com ponte de vocabulário obrigatória.
- **T:** `_template_contexto_area_casa.md` · `_demandas/_template_demanda.md` ·
  `_pessoas/_template_pessoa.md` · `_Clientes/_template_cliente/` ·
  `03_Produto-e-Solucoes/_template_produto/`
- **X:** `_indice/` — 6 CSVs + README, **gerados por `scripts/gen-indice.ps1`. Não editar à mão.**

### C · Corpus — o que se replica, e a regra que não se quebra

**4 classes de MD por cliente**, em `_contexto/`: `institucional.md` · `jornada.md` ·
`pessoas.md` · `contexto-area.md` (×14 áreas). Mais `_demandas/`, `_rfis/`, `_pessoas/`.

🔴 **Todo MD da mesma classe tem os mesmos títulos, sempre.** Conteúdo varia por cliente;
**estrutura nunca varia.** Se o padrão mudar, **muda para a classe inteira, retroativamente.**
**Verificar com `python scripts/valida-padrao-corpus.py` antes de todo commit.**

### F · Frentes paralelas — só quando a sessão for sobre elas

- `brainwave/` — a interface visual. Comece por `brainwave/CONTEXTO.md`, depois o arquivo de
  tarefa de maior número.
- `uMode/04_Dados-e-IA/_boilerplate/` — governança de squad de agentes (tem `CLAUDE.md`,
  `AGENTS.md`, `HERMES.md` próprios). ⚠ **Esses `CLAUDE.md` são do boilerplate, não deste
  repositório** — não confundir com o da raiz.
- `uMode/04_Dados-e-IA/_inbox-hermes/` — **canal de saída para o João/HERMES**: pacotes-proposta
  prontos para ele colar no vault. 🔴 **Escrita no vault não é nossa** — aqui só se propõe.

---

## 2 · A ordem de leitura — quatro níveis, com condição de parada

### Nível 0 · Sempre, sem exceção, nesta ordem
1. **`AGORA.md`** — onde estamos hoje.
2. **`CLAUDE.md`** — papel e regras invioláveis.

> **Depois do Nível 0 você sabe o que é o projeto e como se trabalha nele. Ainda não pode
> escrever nada.**

### Nível 1 · Antes de criar ou editar qualquer arquivo
3. **`CONTEXT.md`** — as decisões travadas. **Nunca decida um mapeamento de campo por memória
   da conversa**: uma regra travada em sessão anterior pode ter saído do contexto sem aviso.

### Nível 2 · Pela natureza da tarefa — leia só a linha que se aplica

| Se a tarefa é… | Leia, além do Nível 0–1 |
|---|---|
| **varrer ou preencher um cliente** | `protocolo-varredura-cliente.md` + os MDs do cliente + `_taxonomia-status-cliente.md` |
| **criar um cliente novo** | `protocolo-criacao-cliente.md` + `_lista-clientes-reais.md` |
| **formalizar demanda** | `protocolo-gestao-demanda.md` |
| **formalizar RFI** | `protocolo-gestao-rfi.md` |
| **integração de cliente** | `protocolo-gestao-integracao.md` + `_inventario-repositorios.md` |
| **pessoa (Casa ou cliente)** | `protocolo-gestao-pessoas.md` + `_espec-pessoas-e-comunicacoes.md` |
| **produto do portfólio** | `protocolo-gestao-produto.md` |
| **banco, schema, campo, relação** | `_espec-banco-brainhub.md` + `_dicionario-dados-brainhub.md` + `_fluxo-dados-brainhub.md` + `_fluxo-crud-brainhub.md` |
| **área canônica** | `_proposta-grade-de-areas-revisao.md` |
| **algo que o Vinicius precisa decidir** | 🔴 `_pendencias-gerais.md` — **é o dono, não crie tabela nova** |
| **convergência com o vault do João** | `_backlog-convergencia-brainhub.md` |
| **interface visual** | `brainwave/CONTEXTO.md` |
| **squad de dev / agentes** | `uMode/04_Dados-e-IA/_protocolos/` |

### Nível 3 · Sob demanda, quando precisar da prova
`STATE.md` (histórico — leia a `## 🔵 FRENTE ATIVA` mais recente e o fim do `## Log de sessões`)
e os **REGISTROS** datados.

> ⚠ **Duas seções da `STATE.md` estão congeladas e NÃO descrevem o estado atual:**
> `## Sprint atual` (parada em ago 2026) e `## Próximas atividades (referência histórica)`.
> **Elas ficam como registro — histórico de sessão nunca se reescreve.**

---

## 3 · O contrato da primeira resposta

1. **Leia o Nível 0 por inteiro.** Nenhum resumo, nenhum trecho.
2. **Não altere nada nesta primeira resposta.** Só leitura e confirmação.
3. **Responda cobrindo exatamente estes seis pontos, nesta ordem:**
   - **O que é este projeto** — em poucas frases.
   - **Qual é o meu papel** — e as regras que não se quebram.
   - **Como se trabalha aqui** — o método (`AGORA.md` § 3).
   - **Onde o projeto está** — cobertura em número (§ 5) e frente ativa (§ 6).
   - **Qual é o próximo passo** — primeiro item de `AGORA.md` § 7.
   - **Quantas decisões esperam o Vinicius** — a contagem de `_pendencias-gerais.md`.
4. **Não prossiga para tarefa nova até o usuário confirmar.** **Se algo parecer desatualizado,
   diga isso explicitamente** em vez de seguir — inclusive se a data do `AGORA.md` estiver velha.

---

## 4 · Ao fechar a sessão — obrigatório

**Toda sessão que gera commit faz os quatro passos, nesta ordem:**

1. **`python scripts/valida-padrao-corpus.py`** — o corpus fecha em `694 / 50 / 49 / 49` com
   **0 completados**. Se completar algum, **alguém quebrou o padrão** — entenda antes de commitar.
2. **`python scripts/valida-documentacao.py`** — nenhum `.md` estrutural órfão do manifesto.
3. **`STATE.md`** — o que aconteceu, no `## Log de sessões`. **Nunca reescrever sessão anterior.**
4. **`AGORA.md`** — data, números da § 5 e as listas de § 6 e § 7.

> 🔴 **Se só a `STATE.md` for atualizada, o `AGORA.md` passa a mentir** — e ele é o primeiro
> arquivo que todo mundo lê.

**E antes de criar qualquer `.md` novo:** ache o dono do assunto na § 1. **Se existir dono,
escreva lá.** Se não existir, o arquivo novo **entra no manifesto da § 1 no mesmo commit.**
