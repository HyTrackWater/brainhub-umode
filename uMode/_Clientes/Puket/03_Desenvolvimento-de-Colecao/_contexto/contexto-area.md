---
aliases:
  - "Desenvolvimento de Coleção · Contexto de área — Puket"
tags:
  - tipo/area
  - cliente/puket
  - status/ongoing
  - area/desenvolvimento-de-colecao
---
# Desenvolvimento de Coleção · Contexto de área — Puket

> Criado em **21 set 2026** por varredura do Notion ao vivo. Campo sem fonte fica `[a preencher]`.

## Fatos

> 🔴 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**
> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o
> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.
> **A prosa abaixo é para pessoa; esta seção é para máquina.**
> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no
> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.

- produto-conectado: Gestão de Coleção + Integração — [base Mapa de Clientes · 2026-09-21]
- pessoas-da-area: 7 pessoa(s) com acesso ao PLM nesta área: — [página Puket, tabela do PLM · 2026-09-21]
- responsavel-area: ? — [não consta em: página Puket, tabela do PLM · 2026-09-21]
- entrega: Esqueleto do produto importado · planilha de 37 campos, importada em lote — [Mapeamento de Conta — Puket · 2026-09-21]
- entrega: Composição preenchida · obrigatória antes de gerar código Linx (§ 4.2.3) — [Mapeamento de Conta — Puket · 2026-09-21]
- entrega: Custo na ficha técnica · responsável: Produto (§ 4.2.3) — [Mapeamento de Conta — Puket · 2026-09-21]

## O que esta área faz

**Faz a subida do esqueleto do produto e responde pelos custos na ficha técnica.**

> *"Em planilha de importação, cadastram **em massa** (preço, cor, linha, ncm, etc.). Responsáveis: **Time de Produto (Cátia ou assistentes)**. Ferramentas: Google Sheets + Import do uMode; Integração com Linx."* — § 4.2.2

🔴 **A planilha de esqueleto tem 37 campos** (§ 2.2), e as validações são condicionais:
> *"`Cor` — se 'Importado', cor obrigatória; `Composição` — **se 'Linha = Meias' o campo é obrigatório**."* — § 4.2.2

⚠ **Procedência:** `Mapeamento de Conta — Puket`, abril/2025 — **síntese de IA sobre três transcrições reais** (26/02, 06/03 e 13/03 de 2025), assinada por Rafael. **Não é fonte bruta.**

## Com quem se relaciona (interno e externo)
`[a preencher]`

## Entregas e responsabilidades

| Entrega | Validação que a controla |
|---|---|
| Esqueleto do produto importado | planilha de 37 campos, importada em lote |
| Composição preenchida | **obrigatória antes de gerar código Linx** (§ 4.2.3) |
| Custo na ficha técnica | responsável: Produto (§ 4.2.3) |

## Padrões operacionais

### Como trabalham

`[a preencher]`

### O que não fazem

- 🔴 **A dor registrada é de padronização, não de processo:**
> *"**Falta de padronização de cor e ncm** gera retrabalho e suporte."* — § 4.2.2

## Vocabulário da área

### Termos específicos

`[a preencher]`

## Pessoas desta área
**7 pessoa(s)** com acesso ao PLM nesta área:

- `Produto` — 7 pessoa(s)

**Distribuição por domínio:** puket.com.br: 6 · grupounico.com: 1

> ⚠ **O domínio importa neste cliente.** `@grupounico.com` é a holding, `@puket.com.br` é a
> marca. Ver [`pessoas.md`](../../00_Institucional/_contexto/pessoas.md) para a lista nominal.

## Produto conectado
**Gestão de Coleção** + **Integração** (uFlow). ERP: **Linx / SAP**.

## Fontes e referências

### Documentos que esta área consome

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Pessoas e perfis | Notion — página `Puket`, tabela do PLM | varrido 21/09/2026 |
| Módulos e ERP | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |
| O que a área faz, entregas, o que não fazem | Notion — `Mapeamento de Conta — Puket` | 04/2025 |
| Etapas de desenvolvimento e níveis de aprovação | Notion — `Mapeamento de Conta Puket — segundo Notion` | 21/03/2025 |
| Módulos e produto conectado | Notion — base `Mapa de Clientes` | varrido 23/09/2026 |
| Pessoas e responsáveis de área | Notion — página `Puket`, tabela de usuários do PLM | varrido 21/09/2026 |

🔴 **O mapeamento de abril/2025 é SÍNTESE DE IA sobre três transcrições** (26/02, 06/03 e
13/03 de 2025), assinada por Rafael. **Não é fonte bruta** — o que vier das transcrições
originais prevalece. ⚠ **E tem 17 meses: revalidar antes de usar como diagnóstico atual.**


### 🟢 Fonte varrida em 23/09/2026 — e o que resta
**`Mapeamento de Contas - Puket`** e a página **`Análise das Similaridades e Diferenças entre
contas: Puket e Caedu`**, ambas em `Operação de Clientes / Área de CX / Documentação CX`.
Mais os **Playbooks** e o **Miro de regras e restrições** da conta.

### Documentos que esta área produz

`[a preencher]`


## Governança
### Responsável pela área
`[a preencher]`
### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Responsável na empresa cliente

`[a preencher]`

### Responsável de atendimento (uMode)

`[a preencher]`

## Conexões

> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`.**

**Área:** `03_Desenvolvimento-de-Colecao` · **Cliente:** `Puket`

**A casa deste cliente:** [institucional.md](../../00_Institucional/_contexto/institucional.md) · [jornada.md](../../00_Institucional/_contexto/jornada.md) · [pessoas.md](../../00_Institucional/_contexto/pessoas.md)

**A mesma área na Casa uMode:** ver `uMode/00_Institucional/_contexto/institucional.md`

**As outras 13 áreas deste cliente:**

- [Planejamento](../../01_Planejamento/_contexto/contexto-area.md)
- [Estilo Criacao](../../02_Estilo-Criacao/_contexto/contexto-area.md)
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
