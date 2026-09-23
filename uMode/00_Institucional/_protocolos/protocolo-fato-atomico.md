---
aliases:
  - "Protocolo — o fato atômico datado, e por que ele vive ao lado da prosa"
tags:
  - tipo/protocolo
  - casa
---
# Protocolo — o fato atômico datado, e por que ele vive ao lado da prosa

> **Classe: `PROTOCOLO`.** Como executar. 🔴 **Dono único do formato de fato do corpus.**
>
> **Travado em 23 set 2026 pelo Vinicius:** *"converte os MDs de entidade pra fato atômico
> datado. O ponto é que tem que ser um agente generalizado, não que funcione só para o João ou
> qualquer outro especificamente."*

## 0 · Declaração de completude — o que este protocolo NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não converte prosa em fato automaticamente** | prosa vira fato por **leitura**, não por regra. Regra que "extrai fato" de texto livre inventa |
| 2 | **Não define o motor de cruzamento** | isto define o ALVO do cruzamento. O motor é outro documento |
| 3 | **Não resolve pessoa por nome** | resolve por **e-mail**. Nome é ambíguo e já nos traiu (§ 4) |
| 4 | **Não cobre `T0`** | fato `T0` **entra por referência, nunca por valor** — a regra já existe no `AGORA.md` § 8.1 |

## 1 · 🔴 A decisão: fato NÃO substitui prosa

**A tentação era converter os MDs de prosa para lista de fatos. Seria destruição de valor.**

O `institucional.md` da Luiza Barcelos traz, em prosa:

> *"Processo está na cabeça da Marcinha → Missão é tirar as informações da cabeça dela e colocar
> na ferramenta."* — dito por Vendas em 06/06/2024

**Isso é a tese do projeto inteiro, dita dois anos antes, com dono e data.** Nenhum
`- processo-concentrado: sim` preserva isso.

🔴 **Então: a prosa fica, e ganha ao lado uma seção `## Fatos`.**

| Camada | Para quem | O que é |
|---|---|---|
| **Prosa** | pessoa | contexto, citação, raciocínio, nuance |
| **`## Fatos`** | máquina | **o alvo do cruzamento** — uma linha, um fato, com fonte e data |

**O agente de transcrição cruza contra `## Fatos`. Nunca contra a prosa.**

## 2 · O formato — uma linha, um fato

```
- <chave>: <valor> — [<fonte> · <AAAA-MM-DD>]
```

**Exemplo real:**

```
- razao-social: Luiza Barcelos Calçados S/A — [CRM Mapa de Clientes · 2026-09-22]
- cnpj: 25.915.190/0001-06 — [CRM Mapa de Clientes · 2026-09-22]
- fabrica-propria: sim — [call de Sales · 2024-06-06]
- canais: varejo, atacado, omnichannel — [call de Sales · 2024-06-06]
- contrato-situacao: Assinado — [planilha de contratos do Financeiro · 2026-09-23]
```

**As quatro partes, e nenhuma é opcional:**

| Parte | Regra |
|---|---|
| **chave** | `kebab-case`, sem acento. **Mesma chave = mesmo significado em todo o corpus** |
| **valor** | o mínimo que carrega o fato. Sem adjetivo, sem explicação — explicação é prosa |
| **fonte** | de onde saiu, nomeável. `[a preencher]` **não é fonte** |
| **data** | `AAAA-MM-DD`. **É a data DA FONTE, não a de hoje** |

🔴 **A data é o que permite o juízo de contradição.** Sem ela, o agente não sabe se a
transcrição de hoje atualiza ou contradiz o que está escrito. **Fato sem data é opinião.**

### 2.1 · Fato que não se sabe

```
- receita-anual: ? — [sem fonte]
```

🔴 **`?` com `[sem fonte]` é melhor que a ausência da linha.** A linha declara que o campo
**existe e não se sabe**; a ausência deixa dúvida entre "não sabemos" e "não perguntamos".
**Ausência declarada é informação.**

### 2.1-bis · 🔴 Ausência VERIFICADA é diferente de ausência

```
- receita-anual: ? — [sem fonte]
- receita-anual: ? — [não consta em: base Mapa de Clientes · 2026-09-23]
```

**As duas linhas dizem "não sei". Só a segunda diz onde se olhou e quando.**

🔴 **E essa diferença muda o veíiculo da decisão no cruzamento.** Quando a transcrição
disser *"a CAEDU fatura X"*, o agente precisa saber se:
- `[sem fonte]` → **ninguém procurou.** Pode ser que a base tenha e nós não lemos.
- `[não consta em: …]` → **procurou-se ali, naquela data, e estava vazio.** Então o que a
  transcrição traz é **NOVO**, e não um conflito com a base.

⚠ **`[não consta em: X · data]` só se escreve depois de abrir o X.** Escrever isso sem ter
aberto é a alucinação que o `CLAUDE.md` chama de *"ausência de fonte é hipótese, não
conclusão"* — e já erramos assim duas vezes.

🟢 **Vale citar mais de um instante quando houver:** *"vazio na base viva (23/09/2026) e
também no export de 04/03/2026"* é muito mais forte que um só. **Campo vazio em dois instantes
distantes não é lacuna de leitura: é campo que a operação não preenche.**

### 2.2 · Fato que conflita

Quando duas fontes discordam, **as duas linhas ficam**, e a mais recente vem primeiro:

```
- status: Onboarding — [base Mapa de Clientes · 2026-09-22]
- status: Ongoing — [institucional.md · 2026-09-21] ⚠ CONFLITA com a linha acima
```

🔴 **Nunca se apaga a linha antiga para "resolver" o conflito.** Conflito é dado.
Quem resolve é pessoa, e a resolução vira uma linha nova com fonte e data.

## 3 · 🔴 O agente tem que ser GENERALIZADO

**Exigência do Vinicius, e ela rejeita o desenho que existe no vault do João.**

O `roteador-tier` do vault tem três donos fixos: `empresa` · **`joao`** · `pessoa-interna`.
🔴 **Isso amarra o agente a uma pessoa.** Um agente que só sabe rotear "para o João" não roteia
para a Julianne, nem para o Bergson, nem para quem entrar amanhã.

**O nosso modelo de dono não nomeia ninguém:**

| `dono` | O que é | Como se resolve |
|---|---|---|
| `empresa` | fato da uMode ou de um cliente | `T2` |
| `cliente:<slug>` | fato de um cliente específico | `cliente/caedu` — a tag já existe |
| `pessoa:<e-mail>` | fato sobre uma pessoa | 🔴 **por E-MAIL, nunca por nome** |

🔴 **A resolução de pessoa é por e-mail contra as 479 fichas do corpus. E quando der ambíguo,
o agente NÃO escolhe — enfileira.**

⚠ **Isto não é preciosismo.** Já nos traiu quatro vezes, todas registradas: duas `Cristina` na
NK STORE · `Junior Felinto` respondendo com `ivan.gouveia@` · `Day` na página e
`Dayana Carla Sestrem` na ata · `Gabriela Cunha` com dois e-mails e duas áreas.
**Nome não identifica pessoa. E-mail identifica.**

**E o tier segue a regra invertida, que essa sim vale copiar do vault:**
🔴 **fato sobre pessoa física assume o tier mais restritivo e escala** — nunca o contrário.

## 4 · Quais chaves existem

🔴 **Chave é vocabulário fechado.** Chave nova exige entrada nesta tabela **no mesmo commit** —
senão duas pessoas escrevem `cnpj` e `CNPJ` e o cruzamento falha em silêncio.

| Chave | Onde vive | Exemplo de valor |
|---|---|---|
| `id` | `institucional.md` | `caedu` — slug estável, **não muda com o nome comercial** |
| `razao-social` | `institucional.md` | `Luiza Barcelos Calçados S/A` |
| `cnpj` | `institucional.md` | `25.915.190/0001-06` |
| `segmento` | `institucional.md` | `calçados` |
| `receita-anual` | `institucional.md` | `R$ 350.000.000` |
| `grupo-segmentacao` | `institucional.md` | `Médios` |
| `status` | `institucional.md` | `Ongoing` |
| `erp` | `institucional.md` · `integracao.md` | `Linx` |
| `modulo-contratado` | `institucional.md` | `Gestão de Coleção` (uma linha por módulo) |
| `servico-faturado` | `institucional.md` | `uFlow` (uma linha por serviço) |
| `contrato-situacao` | `institucional.md` | `Assinado` |
| `contrato-vigencia` | `institucional.md` | `2022-06-23 → 2027-06-23 · vigência 5 anos` |
| `contrato-renovacao` | `institucional.md` | `Renovação Automática · aviso prévio 90 dias` |
| `data-ativacao` | `institucional.md` | `2022-10-05` |
| `indice-reajuste` | `institucional.md` | `IPCA` |
| `usuarios-contratados` | `institucional.md` | `17 internos + 3 externos` |
| `usuarios-conta` | `institucional.md` | `93 usuários com e-mail na tabela do PLM` — **medido**, não contratado |
| `tamanho-atendimento` | `institucional.md` | `P` |
| `atendimento` | `institucional.md` · `pessoas.md` | `pessoa:laura.delgado@umode.com.br` |
| `pessoa` | `pessoas.md` | `pessoa:ana.silva@caedu.com.br` |
| `cargo` | ficha de pessoa | `Analista de Ecommerce` |
| `area` | ficha de pessoa · `contexto-area.md` | `Estilo` |
| `dor` | `jornada.md` · `contexto-area.md` | `hierarquia Griffe › Linha › Grupo` |
| `marco` | `jornada.md` | `kick-off realizado` |

## 5 · Como se escreve um fato — o passo a passo

1. **Ache a fonte.** Sem fonte nomeável, não é fato: é suposição. Suposição fica na prosa,
   marcada `[P]`.
2. **Ache a data DA FONTE.** Não a de hoje. Se a fonte não tem data, escreva `[<fonte> · sem data]`.
3. **Escolha a chave na tabela da § 4.** Se não existir, **acrescente na tabela primeiro**.
4. **Escreva o valor mínimo.** Se precisar explicar, a explicação vai para a prosa.
5. **Se conflitar com linha existente, NÃO apague.** Acrescente com `⚠ CONFLITA`.
6. **Se for `T0`** — CPF, telefone, senha — **registre que existe e onde, nunca o valor.**

## 6 · O que o agente de transcrição faz com isso

```
transcrição → extrai afirmação → resolve entidade (cliente/área/pessoa por e-mail)
            → compara com a linha de mesma CHAVE em ## Fatos
            → 🟢 chave não existe        → propõe linha NOVA
            → ⚪ mesma chave, mesmo valor → não faz nada
            → 🔴 mesma chave, valor outro → CONTRADIZ: enfileira, NUNCA decide
```

🔴 **A comparação é por CHAVE, não por semelhança de texto.** É por isso que a chave é
vocabulário fechado: é ela que torna o cruzamento determinístico em vez de probabilístico.

🔴 **E nenhuma proposta vira fato sem aprovação humana.** A regra já está no
`protocolo-gestao-demanda.md` como `Aprovação de contexto` — **não se inventa outra.**

## Governança

### Quem pode alterar este documento
Vinicius + liderança de Dados e IA. **Chave nova entra na § 4 no mesmo commit em que é usada.**

### Quando ler
Antes de escrever qualquer `## Fatos`, e antes de desenhar qualquer agente que leia ou proponha
fato. **É o contrato entre o cérebro e a máquina que vai alimentá-lo.**
