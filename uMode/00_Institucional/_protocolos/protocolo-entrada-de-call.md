---
aliases:
  - "Protocolo — como uma call entra no BrainHub"
tags:
  - tipo/protocolo
  - casa
---
# Protocolo — como uma call entra no BrainHub

> **Classe: `PROTOCOLO`.** Como executar. 🔴 **Dono único do contrato de entrada de reunião.**
>
> **Escrito em 24 set 2026, a pedido do Vinicius**, para o agente coletor que ele está montando
> no Google Workspace. **Este documento é o lado de CÁ do contrato:** diz o que o BrainHub
> precisa receber. O lado de lá — como o coletor lê o Drive e chama o modelo — não é meu.
>
> **Travado pelo Vinicius em 24/09/2026:** *"A transcrição é sempre mais rica do que o resumo.
> Se for eleger um, sempre transcrição."*

## 0 · Declaração de completude — o que este protocolo NÃO resolve

| # | Lacuna | Por quê |
|---|---|---|
| 1 | **Não define como o coletor lê o Drive** | é o lado de lá; aqui só o formato de chegada |
| 2 | **Não promove nada a canônico** | entrada é `_inbox`. **Promover é ato humano** (§ 6) |
| 3 | **Não resolve áudio sem transcrição** | 598 áudios de WhatsApp seguem fora |
| 4 | **Não cobre reunião sem participante identificável** | § 3 exige e-mail; sem ele, entra como aberto |

## 1 · 🔴 A regra que governa tudo: o coletor NÃO escreve no corpus

**Ele escreve em `uMode/00_Institucional/_inbox-calls/`. Só ali.**

🔴 **Isso não é burocracia.** Duas razões medidas, ambas registradas:
- **A transcrição automática é ruidosa** — 33% das falas chegam sem pontuação final, 15% têm 1 ou
  2 palavras, e há erro de palavra (*"um modelo de humor"*, *"a gente foi criança"*).
  **Fato extraído disso, escrito direto no canônico, é fato falso com aparência de dado.**
- **É a regra que o vault do João já aplica** e que funcionou lá: *"agente escreve só no próprio
  inbox, nunca em canônico"*.

⚠ **O `protocolo-fato-atomico.md` § 6 já diz o mesmo:** *"nenhuma proposta vira fato sem
aprovação humana"*.

## 2 · O arquivo que chega

**Um arquivo `.md` por reunião.** Nome:

```
AAAA-MM-DD_<destino>_<assunto-em-kebab>.md
```

`<destino>` é **`casa`** ou o **slug do cliente** — `caedu`, `luiza-barcelos`, `nk-store`.
🔴 **Slug, nunca nome de exibição.** O corpus tem `id: caedu` como chave estável, e ela **não muda
se o nome comercial mudar**. *(`CAEDU`, `Caedu` e `caedu` já apareceram como grafias da mesma
conta.)*

**Exemplo:** `2026-09-08_caedu_plano-de-acao.md`

## 3 · 🔴 O cabeçalho — e a parte que só o coletor pode entregar

```yaml
---
tipo: registro
origem: google-meet
titulo: "Plano de Ação - Caedu"
data: 2026-09-08
duracao_min: 74
destino: caedu              # `casa` ou slug do cliente
natureza: externa           # `interna` (só uMode) | `externa` (tem alguém de fora)
participantes:              # 🔴 E-MAIL, nunca nome de exibição
  - julianne.dias@umode.com.br
  - juliana.ferre@umode.com.br
  - vitoria.meneghin@caedu.com.br
participantes_sem_email: [] # quem o Meet não identificou; nome como veio
tem_transcricao: true
tem_resumo: true
tier: T2                    # T0 | T1 | T2 — ver § 5
confianca_destino: alta     # alta | media | baixa — ver § 4
---
```

### 3.1 · 🔴 O E-MAIL é o que só o coletor consegue, e é o que mais falta aqui

**Nas 53 transcrições da CAEDU, 23 dos 42 falantes NÃO resolvem para identidade.** Cinco deles
aparecem só por apelido — e um, **`Rose`, é a terceira maior voz da conta, com 733 falas em 7
reuniões**. 🔴 **O rótulo do falante na transcrição é o nome de exibição do Meet, e ele não
identifica pessoa.**

🟢 **O convite do Google Meet tem a lista de participantes COM E-MAIL.**
🔴 **É o dado mais valioso que o coletor pode entregar, e o BrainHub não tem como obter sozinho.**

**Se o coletor mandar e-mail, o corpus resolve pessoa, área e cliente por conta própria** — são
637 nomes já indexados por e-mail. **Se mandar só nome, o problema do `Rose` se repete em toda
conta.**

⚠ **Quando o e-mail não existir, mande o nome em `participantes_sem_email`. Não invente e não
deduza.** *(O corpus já foi traído por nome quatro vezes: duas `Cristina` na NK STORE ·
`Junior Felinto` respondendo com `ivan.gouveia@` · `Day` × `Dayana Carla Sestrem` ·
`Gabriela Cunha` com dois e-mails.)*

## 4 · Como classificar destino e natureza

**`natureza` sai do domínio dos e-mails, não do conteúdo:**
- **todos `@umode.com.br`** → `interna`
- **qualquer e-mail de fora** → `externa`

**`destino` sai do domínio do participante externo:**
- `@caedu.com.br` → `caedu` · `@puket.com.br` → `puket` · e assim por diante.

⚠ **Isto importa e não é teoria.** As reuniões `2026-06-22_Caedu_2_0` e
`2026-09-08_Plano_de_Acao_Caedu` **têm "Caedu" no título e são INTERNAS da uMode** — nenhuma
pessoa da CAEDU participa. 🔴 **Classificar por título as poria como reunião com o cliente, e
isso é errado.** **O domínio do e-mail não mente; o título mente.**

**`confianca_destino`:**
| Valor | Quando |
|---|---|
| `alta` | domínio de e-mail externo bate com um cliente do corpus |
| `media` | só o título indica o cliente, sem e-mail externo que confirme |
| `baixa` | mais de um cliente possível, ou nenhum |

🔴 **`media` e `baixa` NÃO são erro — são informação.** O corpus trata os dois como
**não roteados** e pede olho humano. **Chutar o cliente é pior que não classificar.**

## 5 · Tier — e a regra é fail-closed

| Tier | O que é | O que o coletor faz |
|---|---|---|
| **`T0`** | CPF, telefone, endereço, senha, token, e-mail pessoal | 🔴 **NUNCA pelo valor.** Registra que existe e em que minuto |
| **`T1`** | valor de contrato, preço, margem, negociação, salário | fica **só na pasta daquele cliente**; nunca em documento da Casa |
| **`T2`** | o resto | padrão |

🔴 **Na dúvida, o tier mais restritivo.** ⚠ **E o tier é do ARQUIVO INTEIRO:** se um trecho é
`T1`, a reunião é `T1`. **Não se fatia reunião para rebaixar tier.**

*(Precedente já aplicado: o registro da proposta CAEDU 2.0 marcou valores como
`NEVER_TO_THIRD_PARTY` e registrou só a substância operacional.)*

## 6 · O corpo do arquivo

```markdown
# <Título> — <data>

> **Classe: `REGISTRO`.** Evidência datada. 🔴 **Não é autoridade e não se edita.**
> **Fonte:** Google Meet via <coletor>, em <data de processamento>.

## Transcrição
🔴 **Fonte primária.** Verbatim, com timestamp e falante, exatamente como veio.

[00:35:34] Vanessa Rinaldi: Vamos pensar na hierarquia de produtos de vocês...

## Resumo
⚠ **DERIVADO da transcrição acima.** Em conflito, **a transcrição prevalece.**

## ⚠ Fatos propostos — NÃO são fatos ainda
- grupo-subgrupo-e-pareado: sim — [transcrição 2026-05-14 · 00:07:40] ⚠ PROPOSTA
```

### 6.1 · As três regras do corpo

1. 🔴 **A transcrição vem inteira e sem limpeza.** ⚠ **Não corrigir o texto reconhecido.**
   Se o ASR escreveu *"um modelo de humor"*, **vem assim**. **Limpar é inventar** — e ninguém
   consegue distinguir depois o que foi dito do que foi consertado.
2. ⚠ **O resumo vem marcado como derivado.** *"A transcrição é sempre mais rica"* — travado pelo
   Vinicius. **Quando houver só resumo, o arquivo diz `tem_transcricao: false`** e isso é lacuna
   declarada, não equivalência.
3. 🔴 **Fato proposto leva `⚠ PROPOSTA` na linha e SÓ pode usar chave do vocabulário fechado**
   do `protocolo-fato-atomico.md` § 4. **Chave nova não se inventa aqui** — ela entra no
   protocolo primeiro, por decisão humana. **Chave livre quebra o cruzamento em silêncio.**

## 7 · O que o coletor NÃO deve tentar fazer

| Não faça | Por quê |
|---|---|
| 🔴 **Decidir CONTRADIZ** | o cruzamento compara com o `## Fatos` do corpus, que o coletor não vê. **Proponha; quem cruza é daqui** |
| 🔴 **Resolver pessoa por nome** | § 3. Mande e-mail ou mande em aberto |
| 🔴 **Escolher entre dois clientes** | `confianca_destino: baixa` e segue |
| 🔴 **Criar área, pessoa ou cliente** | criar entidade é decisão, não consequência de uma call |
| ⚠ **Traduzir vocabulário** | `collection` no banco é inglês; `coleção` de moda é português. **Não normalize** |

## 8 · 🟢 Enriquecimento que vale, em ordem de valor

1. **E-MAIL dos participantes.** § 3. **Nada aqui vale mais que isso.**
2. **Duração e tempo de fala por participante.** Sobrevive ao ruído do ASR — timestamp e rótulo
   não passam pelo reconhecimento de fala. **Dá intensidade de atendimento e quem domina a
   conversa.** *(Foi assim que se viu que a Julianne está em 53 de 53 reuniões da CAEDU.)*
3. **Link para a gravação e para o arquivo bruto.** Rastreabilidade: o registro cita, não copia.
4. **Áreas tocadas**, quando o e-mail do participante resolver para uma das 14 canônicas.
   ⚠ **Só por e-mail.** **Nunca por assunto** — assunto não é área.
5. **Lista de ações ditas**, verbatim e com timestamp, **sem dono atribuído.**
   🔴 **Atribuir dono é decisão.** Mande a frase e o minuto; o dono sai do e-mail ou fica aberto.

## 9 · O JSON que o script precisa

```json
{
  "data": "2026-09-08",
  "titulo": "Plano de Ação - Caedu",
  "duracao_min": 74,
  "natureza": "interna",
  "destino": "caedu",
  "confianca_destino": "alta",
  "participantes": ["julianne.dias@umode.com.br", "juliana.ferre@umode.com.br"],
  "participantes_sem_email": ["Rose"],
  "tem_transcricao": true,
  "tem_resumo": true,
  "tier": "T2",
  "topicos": ["cronograma", "migração", "escopo"],
  "areas_tocadas": ["01_Planejamento"],
  "acoes_ditas": [
    {"ts": "00:26:15", "frase": "os meninos precisam da devolutiva", "dono": null}
  ],
  "fatos_propostos": [
    {"chave": "fase", "valor": "...", "ts": "01:16:13", "confianca": "media"}
  ],
  "arquivo_bruto": "drive://...",
  "gravacao": "https://..."
}
```

⚠ **`dono: null` e `participantes_sem_email` são campos de primeira classe.**
🔴 **Um esquema que obriga a preencher tudo obriga o modelo a inventar.**

## Governança

### Quem pode alterar este documento
Vinicius + liderança de Dados e IA. **Mudança aqui é mudança de contrato com o coletor** — e o
coletor é de outro time. **Não se muda sem avisar o outro lado.**

### Quando ler
Antes de escrever ou mudar o agente coletor, e antes de promover qualquer arquivo do
`_inbox-calls/` para o corpus.
