# Protocolo · Gestão de integração de cliente

> Define o 5º tipo de MD de cliente: `integracao.md`. Formaliza a documentação técnica da integração
> entre a plataforma uMode e o sistema (ERP) de cada cliente.
> Criado em 03 ago 2026, quando os repositórios de integração passaram a estar acessíveis.

## Por que existe

O campo `ERP / Integração` do `institucional.md` guarda **uma linha de texto** ("Linx", "Safe Tech",
"SPI · Totvs Virtual Age · Banner"). Só isso. Ao mesmo tempo, integração é o assunto mais pesado da
operação: das 997 demandas formalizadas, **141 são do tipo `Integração`** e 57 têm
`Suporte Integração` preenchido; boa parte das 85 RFIs é "Escopo - Alteração Integração". Ou seja:
tínhamos o histórico do que foi pedido e **nenhum lugar para a especificação do que existe**.

## Onde vive

`integracao.md` em `[Cliente]/00_Institucional/_contexto/`, ao lado de `institucional.md`,
`jornada.md` e `pessoas.md`.

**É condicional — nem todo cliente tem.** Mesma lógica já aplicada a `_rfis/` (que existe só do lado
de cliente porque RFI sempre tem cliente): `integracao.md` só é criado para cliente que **tem
integração real**. Cliente sem integração **não** recebe o arquivo vazio — a ausência do arquivo é a
informação. Não é lacuna de preenchimento e não entra em contagem de pendência.

## Fonte de verdade

O **repositório de código da integração** é a fonte. Um repositório por cliente, na organização
`UmodeApp` do GitHub. O clone canônico local vive em `C:\Ambientes Virtuais\uMode-Integracoes\`.

Dentro de cada repositório, a documentação segue um padrão próprio (já existente, não criado por
nós):
- `docs/documentacao-geral-<cliente>-<erp>.md` — o documento principal (30 a 77 KB)
- `docs/tabelas-do-<erp>-<cliente>.md` — mapeamento das tabelas do ERP (28 a 46 KB)
- `.claude/skills/docs-integracao-<cliente>-<erp>/SKILL.md` — skill de Claude própria da integração
- documentos pontuais quando existem (ex.: relatório de incidente, migração)

**`integracao.md` não copia esses documentos** — ele é o registro padronizado que resume e
**aponta** para eles. A especificação técnica completa continua morando no repositório; o cérebro
guarda o que é institucional e o caminho para o resto.

## O que está integrado, de fato: sempre uFlow ↔ ERP do cliente

Confirmado por Vinicius Risoléo em **04 ago 2026**, e isto muda como o `integracao.md` deve ser lido:

**Todos os repositórios de integração são da `uFlow`** — o PLM legado, registrado no Notion muitas
vezes como **"Gestão de Coleção"**. Nenhum deles é integração de uma Solução do novo Portfólio. O que
cada repositório documenta é a ponte entre a **uFlow** e o **ERP daquele cliente** (Linx, SAP, SPI,
Safe Tech).

Duas consequências que não se deve inverter:

1. **Ter a ferramenta ≠ ter integração.** Os clientes que têm integração são exatamente os da tabela
   de mapeamento abaixo. Os demais **normalmente usam a uFlow, mas não têm processo de integração**.
   Portanto: cliente sem `integracao.md` **não** significa cliente sem a ferramenta — significa
   cliente sem processo de integração. Nunca deduzir uso de plataforma a partir da ausência de
   integração, nem o contrário.
2. **Essa documentação é, hoje, a nossa melhor fonte sobre o comportamento da própria uFlow.** Ela
   descreve validações, campos personalizados, workflows, regras de liberação e estados reais da
   plataforma — mesmo tendo sido escrita para explicar a integração. Vale como fonte indireta
   enquanto o repositório da plataforma não estiver disponível (ver `D-2026-002`).
   ⚠ **Com um limite claro:** essas documentações mapeiam as tabelas do **ERP do cliente**, nunca as
   tabelas da uFlow. Quem procurar aqui o schema da uFlow não vai encontrar.

## Mapeamento repositório → cliente (autoritativo)

> Informado pelo desenvolvedor que compartilhou os repositórios, via Vinicius, em 03 ago 2026.
> **Não inferir cliente pelo nome do repositório** — dois nomes não são adivinháveis (ver aviso
> abaixo).

| Repositório (`github.com/UmodeApp/…`) | Cliente(s) | ERP / sistema |
|---|---|---|
| `arzz-sap` | **Reserva** + **Oficina Reserva** | SAP |
| `integracao-linx-nv` | NV | Linx |
| `unico-linx` | **Puket** | Linx |
| `integration-vix-linx` | VIX | Linx |
| `integration-luiza-barcelos-sft` | Luiza Barcelos | Safe Tech |
| `integration-baw-linx` | Baw | Linx |
| `integration-cambos-spi` | Cambos | SPI |
| `integration-lofty-linx` | Lofty Style | Linx |
| `integration-nk-linx` | NK STORE | Linx |
| `integration-osklen-linx` | Osklen | Linx |
| *(não existe)* | Moda Objetiva | — sem documentação de integração ainda |

⚠ **Dois nomes que não se adivinha, registrados para nunca serem inferidos de novo:**
- **`arzz-sap` = Reserva/Oficina.** `arzz` é **AZZAS** (o grupo — o CRM já classifica os dois em
  "Grupo 1: Azzas"), **não** Arezzo. Numa primeira leitura em 03 ago 2026 foi inferido como Arezzo
  pela semelhança do nome, e estava **errado** — corrigido pelo Vinicius antes de qualquer arquivo
  ser gerado. É exemplo direto de por que o mapeamento vem de fonte humana, não de padrão de nome.
- **`unico-linx` = Puket.** Nada no nome indica o cliente.

### Um repositório pode servir mais de um cliente
`arzz-sap` atende Reserva **e** Oficina Reserva. Cada cliente recebe o **seu** `integracao.md`
(isolamento entre casas é regra travada em `CONTEXT.md`), os dois apontando para o mesmo repositório,
e cada arquivo avisa no corpo que compartilha a integração com o outro. Não é duplicidade — é a mesma
integração registrada em cada casa que ela serve. Mesmo tratamento já dado à RFI multi-cliente.

### Repositório existe mas sem documentação
`unico-linx` (Puket) tem código e **nenhum arquivo `.md`**. Nesse caso o `integracao.md` é criado com
`### Documentação de referência` explicitando a ausência — porque a informação "existe integração,
falta documentação" é diferente de "não existe integração".

## Regra de consistência com `institucional.md`

O campo `ERP / Integração` do `institucional.md` e o campo `ERP / sistema integrado` do
`integracao.md` **têm de concordar**. Quando divergirem, **não resolver por conta própria**: registrar
a divergência nos dois arquivos e levar como pendência — pode ser ERP trocado, integração
descontinuada, ou mais de um sistema no mesmo cliente.

## Anatomia do `integracao.md`

Estrutura fixa, igual em todos os clientes (regra geral do projeto). Ver
`uMode/_Clientes/_template_cliente/00_Institucional/_contexto/integracao.md`.

- **Identificação** — cliente, ERP/sistema, repositório, documentação de referência, status
- **Arquitetura** — direções (escrita/leitura), mecanismo, ambiente e execução
- **Escrita (uMode → sistema do cliente)** — o que é enviado, gatilho e frequência, regras
- **Leitura (sistema do cliente → uMode)** — o que é importado, gatilho e frequência, regras
- **Tabelas e endpoints** — tabelas do ERP mapeadas, endpoints externos
- **Particularidades deste cliente** — o que foge do padrão
- **Auditoria e monitoramento**
- **Incidentes registrados**
- **Governança** — responsável técnico, quem pode alterar
- **Fontes** — documentos consultados, com caminho

## Como preencher

1. **Identificação** sai do mapeamento acima + inventário de arquivos do repositório. É a única parte
   que não exige ler a documentação técnica.
2. **Todo o resto** exige leitura do `documentacao-geral-*.md` do cliente. Campo sem base no documento
   fica `[a preencher]` — **nunca preencher integração por analogia com outro cliente**, mesmo quando
   o ERP é o mesmo. Os documentos mostram que dois clientes de Linx não têm a mesma integração.
3. **Não copiar tabela de ERP inteira** para dentro do `integracao.md`. Resumir e apontar para o
   `tabelas-do-*.md`.

## Governança
- Preenchimento e revisão → responsável técnico da integração + liderança de Tecnologia.
- Este protocolo → Vinicius Risoléo + CEO.
