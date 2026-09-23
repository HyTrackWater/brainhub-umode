# AGORA.md — onde o projeto está, em uma tela

> **Este é o arquivo de orientação.** Serve para retomar o projeto de qualquer lugar, em
> qualquer workspace, sem ler as 2.700 linhas da `STATE.md`.
>
> **Atualizado em: 23 set 2026.** Se esta data não for de hoje ou de ontem, **desconfie** —
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

**Ferramentas de verificação**, ambas em `scripts/` e obrigatórias antes de todo commit:
`valida-padrao-corpus.py` (as 4 classes de MD de cliente) e `valida-documentacao.py`
(nenhum `.md` estrutural órfão do manifesto do `START.md` § 1).

## 4 · Onde está cada coisa

> 🔴 **O conjunto completo de documentação — "o time" — está declarado no
> [`START.md`](START.md) § 1**, com a classe de cada arquivo e quem é dono de qual assunto.
> **`python scripts/valida-documentacao.py` confere que nada ficou órfão.**

| Arquivo | O que é | Quando ler |
|---|---|---|
| **`START.md`** | **o manifesto e a ordem de leitura** | primeira mensagem da sessão |
| **`AGORA.md`** | este arquivo — orientação | **primeiro, sempre** |
| `CLAUDE.md` | papel, regras invioláveis, como executar | antes de qualquer tarefa |
| `CONTEXT.md` | decisões de arquitetura travadas | antes de mapear campo ou taxonomia |
| `STATE.md` | histórico completo, sessão a sessão | quando precisar do detalhe de algo |

**Autoridades temáticas** (em `uMode/00_Institucional/_contexto/`):

| Documento | É autoridade sobre |
|---|---|
| [`_espec-pessoas-e-comunicacoes.md`](uMode/00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) | pessoas e comunicações no banco |
| [`_taxonomia-status-cliente.md`](uMode/00_Institucional/_contexto/_taxonomia-status-cliente.md) | o campo `Status` do cliente |
| [`_varredura-2026-09-22-reunioes-compartilhadas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-22-reunioes-compartilhadas.md) | a base de reuniões do Notion |
| [`_proposta-grade-de-areas-revisao.md`](uMode/00_Institucional/_contexto/_proposta-grade-de-areas-revisao.md) | revisão da grade de áreas canônicas |
| [`_varredura-2026-09-21-fontes-e-lacunas.md`](uMode/00_Institucional/_contexto/_varredura-2026-09-21-fontes-e-lacunas.md) | fontes rastreadas e lacunas por cliente |
| 🟢 [`_dicionario-permissionamento-uflow.md`](uMode/00_Institucional/_contexto/_dicionario-permissionamento-uflow.md) | **como a permissão do uFlow funciona** — `Includes`/`Excludes`, `scopable`, `entity_configs`, 72 controllers |

> 🔴 **Onde buscar contexto novo no Notion — leia isto antes de abrir qualquer coisa lá.**
> **Cada cliente tem um `_pendencias-e-fontes.md`** em `uMode/_Clientes/<cliente>/00_Institucional/_contexto/`, e ele é **o diário de varredura**:
> **§ 3.1** fontes da carteira inteira já varridas · **§ 3.2** a página daquele cliente · **§ 3.3** sub-páginas dele já abertas · 🔴 **§ 4 fontes conhecidas e AINDA NÃO varridas.**
> **As §§ 3.1 e 4 são iguais nos 48 arquivos** — abrir um só basta para ter o mapa do Notion inteiro. **Não reabra o que a § 3 diz que já foi lido.**

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
| **Modelo de documentação** | 22 set 2026 | **8 classes travadas · manifesto declarado no `START.md` § 1 · verificável por script** |
| **Pessoas e ferramentas** | 22 set 2026 | **enum de 7 módulos · atendimento de 17 contas · razão de pessoas datado em 17 clientes** |
| 🟢 **Permissionamento do uFlow** | **23 set 2026** | **as 10 matrizes lidas · o mecanismo virou autoridade (`_dicionario-permissionamento-uflow.md`) · os 4 acervos do Notion mapeados** |

**Cobertura hoje, medida:**

| | Número |
|---|---:|
| Clientes no corpus | **48** |
| MDs em `uMode/` | **2.402** |
| Demandas formalizadas | **998** |
| RFIs formalizadas | **85** |
| `contexto-area.md` conformes | **694/694** |
| `institucional.md` · `jornada.md` · `pessoas.md` | **50/50 · 49/49 · 49/49** |
| Atas de reunião lidas por inteiro | **8 de 1.161** |
| `.md` estruturais, todos classificados | **90/90** |
| 🟢 **Conectados no grafo** (Obsidian) | **2.351 de 2.420 · 97,1%** |
| Órfãos restantes | **74 · 3,1%** |
| 🟢 **Fichas de pessoa** | **243** — 225 de cliente + 18 da Casa |
| 🟢 **Fichas de ferramenta** | **27** |
| Decisões pendentes registradas | **487** |
| 🟢 **Perguntas na fila do Vinicius** | **63** — `_perguntas-para-o-vinicius.md` |
| 🟢 **Matrizes `Perfil de Usuário` lidas** | **10 de 10 — conjunto FECHADO** |
| 🟢 **Páginas de cliente abertas no Notion** | **16 de 49** |
| 🟢 **Clientes com sub-página registrada no diário** | **10** |
| Arquivos de demanda no padrão canônico | **997/998** · 1 staging `SUPERSEDED` |
| 🚨 **Credenciais expostas conhecidas** | **3** — NK STORE · Lofty Style · **a própria plataforma** |

## 6 · O que está sendo feito agora

🔵 **Frente ativa: varredura cliente a cliente, ABRINDO A PÁGINA de cada um.**

> 🔴 **A regra que mudou em 22 set 2026:** até aqui eu varria **bases** (SQL). A página
> do cliente **não é base** — e é onde vivem o **`cargo`**, a **área**, as **pessoas de
> diretoria**, as **sub-páginas de ata** e, em pelo menos um caso, uma **credencial de
> produção em texto claro**. **Consulta SQL não alcança nada disso.**

**O modelo, travado pelo Vinicius em 22 set 2026: ENTIDADE É ARQUIVO.**
*"praticamente tudo que for uma entidade é arquivo? Ou seja, ferramenta, pessoas, empresas,
áreas, demandas, RFIs, tudo... As reuniões, contextos gerais, e-mails, tudo isso vai estar de
alguma forma ligada a esses nós maiores."*

| Entidade | É arquivo? | Quantos |
|---|:-:|---:|
| Instituição · Área · Demanda · RFI · Solução | ✅ | 50 · 694 · 1.021 · 102 · 16 |
| Pessoa | ✅ | **137** |
| **Ferramenta** | ✅ **novo em 22 set** | **16** |
| Reunião / ata · E-mail · Agente | 🔴 **não** | 1.161 · 92 · 4 conhecidos |

**Páginas de cliente abertas: 16 de 49** — CAEDU · Osklen · NK STORE · Reserva · VIX ·
Lofty Style · Puket · NV · Oficina Reserva · Cambos · Luiza Barcelos · Moda Objetiva · Baw ·
Loungerie · Lenny Niemeyer · Recco.

### 🔴 O que mudou em 23 set 2026, e o próximo agente precisa saber antes de tudo

**1 · As dez matrizes de permissão estão lidas. O conjunto fechou.**
Duas conclusões minhas caíram no processo: o `Fale com o Suporte` **não é padrão** (4 bloqueiam
× 6 liberam) e a dor de **excluir variante é configuração, não limitação** da plataforma — a
Recco tem a linha liberada.

**2 · O mecanismo de permissão virou autoridade.**
O `📕 Manual do Permissionamento` estava na minha lista de fontes não varridas **enquanto eu
registrava como pergunta uma coisa que ele responde desde 2024.** Virou
[`_dicionario-permissionamento-uflow.md`](uMode/00_Institucional/_contexto/_dicionario-permissionamento-uflow.md).

**3 · 🔴 Documentação de cliente mora em QUATRO lugares no Notion, não em um:**

| Acervo | Estado |
|---|---|
| `Databases / Mapa de Clientes` | 🟢 é por onde a varredura anda — **16 de 49 abertas** |
| **`uFlow / Documentação de Setup - PLM / CLIENTES`** | 🔴 **9 clientes, só a NV tocada** |
| `Operação de Clientes / **Arquivo** / Área de CX / Documentação CX` | ⚠ **arquivado** · 30 docs listados, nenhum aberto |
| **`Documentação Homologada`**, dentro do cliente | ⚠ vista na Cambos · **não sei quem mais tem** |

🔴 **NK STORE e VIX, que eu considerava bem varridas, têm um SEGUNDO endereço nunca aberto.**

**4 · 🚨 Há um terceiro risco de credencial, e ele é da plataforma.**
Uma página chamada **`Credenciais`** em `uFlow / Setup - PLM`, seção `Nova uFlow/uRocket`.
🔴 **NÃO a abri, de propósito** — o título basta para registrar o risco, e abrir traria segredo
para dentro do contexto. **Item 480 do `_pendencias-gerais.md`.**

**5 · 🔴 Existe segmentação de conta — `SaaS`, `Enterprise`, `SMB` — e nenhuma ficha de cliente
do corpus carrega segmento.** Os 48 vêm sendo tratados como um bloco só.

## 7 · Próximos passos, em ordem

> 🔴 **Antes de qualquer um destes: abra o `_pendencias-e-fontes.md` do cliente em questão e
> leia a § 3.** É o diário do que já foi varrido. **Repetir busca é o desperdício que o
> Vinicius nomeou explicitamente.**

1. 🔵 **`uFlow / Documentação de Setup - PLM / CLIENTES` — oito clientes nunca tocados:**
   RESERVA · BAW · OFICINA · VIX · StudioZ · PUKET · CAEDU · NK Store. **É o passo imediato**,
   e inclui o segundo endereço da NK STORE e da VIX. **A NV já foi lida** — mas **12 das 13
   sub-páginas de perfil dela continuam fechadas.**
2. 🔵 **As 33 páginas de cliente que faltam** em `Databases / Mapa de Clientes`. Segue sendo a
   fonte de maior rendimento: resolve `cargo`, `área` e a camada de liderança de uma vez.
   🚨 **Toda página aberta é varrida também em busca de segredo.**
3. 🚨 **Credenciais — agora são três.** NK STORE (lugar exato) · Lofty Style (lugar exato) ·
   **`Credenciais` do uFlow, não aberta.** **A rotação é ação do Vinicius, não minha.**
4. 🔵 **As seções do `Setup - PLM` que respondem dor aberta:** `Como é o processo de
   integração?` e `Logs e integração` (dor de CAEDU, VIX, Moda Objetiva, Luiza Barcelos) ·
   `Automações` (os IDs `#1136`, `#1175`, `#989` do playbook da Cambos) · `Traduções` (onde o
   apelido interno é operado) · `Ficha de Produto` e suas 7 sub-páginas.
5. 🔴 **Perguntar ao Vinicius:** são **63 perguntas na fila**, em
   [`_perguntas-para-o-vinicius.md`](uMode/00_Institucional/_contexto/_perguntas-para-o-vinicius.md).
   **As mais caras:** a segmentação de conta · se `excluir variante` é mesmo só permissão ·
   se a Cambos é fornecedora de marcas e não marca · qual campo manda, `Status` ou `Etapa`.
6. 🔵 **Fechar as 3 entidades que faltam: reunião, e-mail e agente.** Enquanto forem prosa, o
   grafo não liga ata a pessoa nem demanda a conversa.
7. 🔵 **Resolver o campo `Participantes` das 1.161 reuniões** com `get-users` — dá presença
   nominal com data, a melhor fonte de pessoa ativa ainda não extraída.
8. 🔴 **Varrer `Segmentação Grupos` e `Atendimento 2024`** — a primeira ganhou urgência: há
   três rótulos de segmento (`SaaS`, `Enterprise`, `SMB`) sem dono no corpus.
9. 🔴 **Criar o campo `Data de Churn`** — segue sendo a lacuna mais cara do corpus.
10. 🔵 **Retomar a CAEDU** assim que as ~50 transcrições reais chegarem. 🟢 **E há precedente
    de método:** o `Playbook Cambos` nasceu de transcrição de treinamento processada com IA, em
    23/03/2026. **Já rodou uma vez.**
11. 🔴 **AO FIM DE TODA A VARREDURA, e só ao fim: o `HOJE` dos uModers.**
    **Decisão do Vinícius em 22 set 2026**, textual: *"os cargos dos demais também terão
    atualizações. Isso vai ser uma coisa recorrente e que teremos que corrigir somente ao
    final de toda a varredura: como é o HOJE dos uModers."* `[D]`

    🔴 **A regra que vale até lá: cargo lido em ata é cargo NAQUELA DATA, nunca cargo de
    hoje.** Toda ficha de uModer que receber cargo de uma fonte datada **cita a data junto**.
    ⚠ **Não corrigir de um em um pelo caminho** — ele pediu de uma vez, no fim, e corrigir aos
    pedaços só cria versões parciais conflitantes.

    **Já confirmado por ele em 22 set 2026 — quatro saídas:** Dalker Walter (Diretor de
    Operações) · Rafael Renaldim (Gerente de Experiência do Cliente) · Tais Moser
    (Customer Success) · Saulo (CTO). ⚠ **Data de saída de nenhum deles é conhecida.**

## 8 · Decisões esperando o Vinicius

🔴 **O dono deste assunto é o [`_pendencias-gerais.md`](uMode/00_Institucional/_contexto/_pendencias-gerais.md)
— **349 itens datados.** **Não crie tabela de pendência aqui nem em lugar nenhum: escreva lá.**

### 8.0 · 🔴 O que só ele responde tem UM caminho, e só um

**Decisão dele em 22 set 2026:** *"em dado momento, você montará uma lista de coisas que eu tenho
que perguntar e vou dar um jeito de responder ou por áudio ou numa transcrição de reunião mesmo."*

| Onde | O que é |
|---|---|
| `_Clientes/<Cliente>/…/_pendencias-e-fontes.md` **§ 2.1** | **onde a pergunta nasce** |
| [`_perguntas-para-o-vinicius.md`](uMode/00_Institucional/_contexto/_perguntas-para-o-vinicius.md) | **a lista que ele responde** — colhida pelo **mesmo script** |
| [`protocolo-perguntas-ao-vinicius.md`](uMode/00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md) | **o processo** — 🔴 **não criar um segundo** |

🔴 **A regra que decide:** pergunta é só o que **nenhuma fonte** responde. Dúvida que uma fonte
responde **não é pergunta — é varredura que falta fazer.**

⚠ **Quando levar a lista até ele não é decisão minha.** Ele disse *"pensaremos nisso quando
chegar o momento"*. **Minha obrigação é manter a fila pronta e avisar se ela travar a varredura.**

### 8.1 · Dado sensível: `T0` / `T1` / `T2`

> 🔺 **Corrigido em 22 set 2026.** Até aqui eu usava rótulos meus — `INTERNAL_ONLY`,
> `NEVER_TO_THIRD_PARTY`. **Era uma segunda taxonomia para a mesma coisa**, o defeito que a
> gente critica. **O vocabulário é `T0`/`T1`/`T2`**, o mesmo que o João usa no vault, com
> definição operacional já registrada (item 96 do `_pendencias-gerais.md`).

| Tier | O que é | O que entra no corpus |
|:-:|---|---|
| **`T2`** | **equipe** — o padrão | nome, cargo, área, papel, escopo, marco, decisão, prazo |
| **`T1`** | **restrito** | valor de proposta, preço, margem, escopo confidencial — **entra, e fica só no `_contexto/` daquele cliente** |
| **`T0`** | **privado** | 🔴 **nunca entra por valor.** CPF, telefone pessoal, senha, token, string de conexão. **Entra por referência:** registro que existe e **onde** |

> `[P]` **Distinção que fiz em 22 set 2026 e que precisa do seu aval:** **e-mail CORPORATIVO é `T2` e entra** — é dado de contato de trabalho e é **a chave de identidade** que destrava a deduplicação de pessoa (item 252). **E-mail pessoal segue `T0`.** Telefone e CPF seguem `T0` em qualquer caso. **Precedente que já existia no corpus:** há ficha nomeada por e-mail na Reserva desde antes desta sessão.

**Onde isso vive, por cliente:** `_Clientes/<Cliente>/00_Institucional/_contexto/`
**`_pendencias-e-fontes.md`** — é a autoridade sobre as pendências **daquele** cliente e sobre
**onde já se varreu**. Gerado por `scripts/gera-pendencias-e-fontes.py`.

⚠ **O que NÃO fiz:** não copiei mecanismo nenhum do vault (a restrição continua valendo).
**Adotei o rótulo, que é vocabulário comum** — e vocabulário comum é exatamente o ponto.

## 9 · Como manter este arquivo vivo

**Este arquivo mente rápido se ninguém o atualizar.** A regra:

- **O ritual de fechamento completo está no [`START.md`](START.md) § 4** — são seis passos:
  `gera-conexoes.py`, `valida-indexacao.py`, `valida-padrao-corpus.py`,
  `valida-documentacao.py`, `STATE.md` e **este arquivo**.
  ⚠ **Corrigido em 23 set 2026:** esta linha mandava rodar um `propaga.py` que
  **não existe mais** — virou `scripts/valida-padrao-corpus.py`.
- **Toda sessão que gera commit atualiza `AGORA.md`** — no mínimo a data, os números da § 5 e as
  listas das § 6 e § 7.
- **`AGORA.md` é resumo, `STATE.md` é histórico.** O que aconteceu vai para a `STATE.md`;
  o que **vale agora** vive aqui. **Nada de histórico neste arquivo.**
- **Se este arquivo divergir da `STATE.md`, a `STATE.md` ganha** — e aí este aqui está com
  defeito e precisa ser corrigido na hora.
