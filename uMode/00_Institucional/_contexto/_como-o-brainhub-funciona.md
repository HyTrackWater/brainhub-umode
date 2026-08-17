# Como o BrainHub funciona — explicação do zero

> Escrito em **17 ago 2026** a pedido do Vinicius, que pediu uma aula assumindo alguém vendo isso
> pela primeira vez. Este documento **não acrescenta desenho** — traduz o que está em
> `_fluxo-dados-brainhub.md` e `_dicionario-dados-brainhub.md` para quem ainda não tem o modelo
> mental. Onde algo é proposta e não código, está marcado `[P]`.

---

## 1 · Três coisas, e só três

Toda a plataforma se reduz a três lugares. Se você entender que **um documento nunca muda sozinho e
nunca muda sem deixar rastro**, já entendeu metade.

| O lugar | O que guarda | A regra que o define |
|---|---|---|
| **O acervo** — `contexts` | O conhecimento. Cada MD nosso vira um registro aqui. | Tem uma **cabeça** (a versão atual) e um **histórico imutável** (`context_versions`). |
| **O cartório** — `audit_events`, `approvals` | Quem mudou, quando, o que mudou, quem autorizou. | **Append-only por trava de banco.** Não é convenção: tentar reescrever um evento de auditoria dá erro. |
| **A oficina** — `loops`, `agents` | O que *age*: automação e agentes. | Toda execução fica registrada com procedência, custo e **com o crachá de quem agiu**. |

Um MD nosso não "vira um arquivo no sistema". Ele vira **um registro no acervo com histórico e
cartório próprios**. Editar duas palavras num `jornada.md` produz: uma versão nova imutável, um
evento de auditoria com os campos que mudaram, e — se alguém estiver inscrito — trabalho executado.

---

## 2 · A ideia que faz todo o resto encaixar

> **Nada acontece porque alguém deu uma ordem. Acontece porque um FATO foi registrado de forma
> durável, e alguém estava previamente inscrito para reagir àquele tipo de fato.**

Isso é o que mais custa entender de primeira, porque não é como software costuma parecer funcionar.

**Não é telefone.** Telefone é: eu ligo para você, você atende, resolvemos. Se a linha cai no meio,
perdemos a conversa e ninguém sabe.

**É mural com assinaturas.** Eu prego um fato no mural: *"o documento X foi publicado na versão 7"*.
Não chamo ninguém. Quem tinha assinado "me avise quando publicarem algo da categoria Y" recebe e
age. Se ninguém assinou, o fato fica pregado no mural de todo modo — **o registro não depende de
haver alguém interessado**.

Três consequências práticas, e cada uma resolve um problema real de operação:

1. **Nada se perde.** O fato é gravado *na mesma transação* da mudança. Não existe "mudou mas não
   avisou".
2. **Nada roda duas vezes.** Cada fato tem identidade calculada. Se o sistema tentar processar de
   novo — porque caiu, porque reiniciou, porque alguém clicou duas vezes — a segunda tentativa é
   **rejeitada pelo banco**, não pela boa vontade do código.
3. **Sempre existe resposta para "por que isso aconteceu".** A execução guarda qual fato a disparou.
   Você anda para trás até o commit.

---

## 3 · Uma história completa, passo a passo

Alguém abre o `jornada.md` da Cambos e marca que a fase mudou. Sete etapas. Vou dar o nome técnico
**e** a tradução.

### Etapa 1 · A escrita — duas coisas juntas, ou nenhuma
O sistema faz duas gravações **dentro da mesma transação**: atualiza a cabeça do documento e escreve
um bilhete numa caixa de saída.

Por que juntas: se fossem separadas, existiria o instante em que o documento mudou e o bilhete não
foi escrito — e aí a mudança acontece **em silêncio**, sem ninguém reagir. Juntas, é impossível ter
uma sem a outra.

E tem uma trava a mais: a atualização só passa **se a versão atual for a que você leu**. Se alguém
publicou nesse meio-tempo, sua gravação não passa e volta "recarregue". **Ninguém sobrescreve o
trabalho de outro em silêncio.**

### Etapa 2 · O bilhete — com nome calculado
O bilhete vai para uma caixa chamada `context_publication_outbox`, e o **nome dele é calculado** a
partir do documento + da versão. Se por qualquer motivo o sistema tentar escrever o mesmo bilhete
outra vez, ele **bate na porta e não entra** — nome repetido é rejeitado.

É assim que "processar exatamente uma vez" deixa de ser promessa e passa a ser **propriedade do
banco**.

### Etapa 3 · O carteiro — passa sempre, e carimba o que pegou
Um processo passa **a cada 5 segundos**, pega **até 25 bilhetes**, e em cada um que pega põe um
carimbo com o nome dele válido por **30 segundos**. Enquanto carimbado, mais ninguém pega aquele.

Se o carteiro cair no meio do trabalho, o carimbo **vence** e outro carteiro pega o bilhete. **Nada
fica preso porque uma máquina morreu.** Se falhar de novo, ele reagenda esperando cada vez mais, até
um teto de 15 minutos.

### Etapa 4 · O anúncio — e a limitação mais importante de todas
O carteiro anuncia no mural: **`context.published`**. E o anúncio carrega **exatamente cinco
informações**: qual documento, qual versão, qual revisão, **qual categoria**, **qual área**.

> ⚠ **Preste atenção nisto, porque decide o desenho todo:** o anúncio **não diz** se aquilo é um
> `jornada`, um `institucional` ou uma demanda. **Não diz** se é confidencial. Quem lê o anúncio só
> vê categoria e área.
>
> **Por isso a categoria tem de carregar o tipo do documento.** Não é preferência de organização —
> é a única forma de o mural conseguir distinguir uma coisa da outra.

### Etapa 5 · Os inscritos — comparação simples, de propósito
Cada inscrição (`trigger`) diz: *"me avise quando o anúncio for da categoria X"*. A comparação é
**texto com texto**, e nada mais — não dá para dizer "quando o nível for maior que 2". Isso é
limitação real, e é também o que mantém o mecanismo previsível.

### Etapa 6 · A ação — e a coisa mais importante de governança da plataforma
A inscrição casou, então roda um **Loop** (uma sequência de passos: consultar agente, aprovar,
notificar, gravar). Cada passo fica registrado com resultado e custo.

> 🔴 **E aqui está o que quase ninguém percebe: o Loop roda com o crachá do DONO DA INSCRIÇÃO, não
> de quem editou o documento.**
>
> Ou seja: quem é dono de uma inscrição **define o poder que o robô tem**. Se a inscrição pertence a
> alguém com acesso amplo, a automação age com acesso amplo — mesmo que quem editou o documento não
> tivesse esse acesso.
>
> **Inscrição não é configuração técnica. É objeto de governança**, e tem de ser tratada com o mesmo
> cuidado de uma procuração.

### Etapa 7 · O registro — o que sobra depois
Fica gravado, sem possibilidade de reescrita: quem alterou (identidade em três partes), quando,
**quais campos**, o conteúdo anterior íntegro endereçado por hash, o que a publicação disparou, e
quanto custou por passo.

---

## 4 · Onde o endereçamento entra — e como os MDs governam ele

Esta é a pergunta que importa: *como isso "toma vida" com endereçamentos que seguem as regras dos
próprios MDs?*

A resposta tem duas metades, e a segunda é a que faz a coisa ser um cérebro e não um arquivo morto.

### Metade 1 · O MD governa pelo que ELE É
O tipo do documento decide a categoria. A categoria decide quem está inscrito. Quem está inscrito
decide o que roda.

> **Logo: a identidade do documento é a regra.** Publicar algo como `demanda` faz a máquina se
> comportar de um jeito; publicar como `institucional` faz de outro. Não há um "painel de regras"
> separado que alguém precise manter em sincronia — **a regra está em ser aquele tipo de
> documento.**

É por isso que a nossa obsessão com "todo MD do mesmo tipo tem os mesmos títulos, sempre" deixa de
ser preciosismo de organização e passa a ser **pré-condição de automação**. Estrutura previsível é o
que permite uma máquina agir sobre o documento sem adivinhar.

### Metade 2 · O MD governa pelo que ele DIZ — e existe um mecanismo para isso
Os MDs de `_protocolos/` dizem quem executa e quem aprova. Hoje isso é prosa, para gente ler.

**Existe no banco o mecanismo exato para fazer isso virar execução.** A definição de um Loop pode
declarar sua origem como `git-template`, e nesse caso **exige três campos obrigatórios: o
repositório, o caminho do arquivo e o commit**.

> **Traduzindo:** um protocolo escrito por nós, versionado no Git, pode se tornar uma **definição
> executável com procedência verificável até o commit**. Não é "alguém configurou uma automação
> parecida com o protocolo". É *este* arquivo, *nesta* versão, rodando. `[C]` o mecanismo existe ·
> `[P]` usá-lo assim é a nossa proposta.

**A cadeia inteira, então:**

```
o MD de protocolo          → a lei escrita
definição de Loop          → a lei compilada, com commit como procedência
nó de APPROVAL / NOTIFICATION → a lei decidindo e avisando
o endereçamento            → a lei chegando numa pessoa, com prazo e responsável
a resposta                 → a pessoa devolvendo, com justificativa e evidência
```

**O endereçamento não é uma notificação.** Notificação é aviso — some depois de lida. Endereçamento é
**obrigação com dono, prazo e desfecho registrado**. É a diferença entre "você foi avisado" e "isto
está no seu nome até você responder".

### O ciclo da resposta `[P]` — o que ainda não existe e é o que fecha o laço
Uma pessoa endereçada pode: **aceitar · recusar · devolver com pergunta · reatribuir · concluir com
evidência**.

Duas regras que eu proponho travar desde o começo:
- **Recusar e devolver exigem justificativa.** Sem justificativa não é resposta, é silêncio com
  botão.
- **Concluir exige evidência**, e evidência é *ponteiro para documento do acervo*. Não texto livre.
  **Conclusão sem evidência não é conclusão.**

---

## 5 · O laço que faz isso ser um cérebro

Repare no que a segunda regra acima produz.

Se concluir um endereçamento exige apontar para documentos do acervo, então **a conclusão de um
trabalho é sempre um enriquecimento do acervo**. E enriquecer o acervo é publicar. E publicar prega
um fato no mural. E o fato pode acionar inscrições.

```
documento publicado → fato no mural → inscrição casa → Loop roda
   → endereçamento numa pessoa → ela responde concluindo com evidência
      → a evidência É documento publicado → fato no mural → ...
```

**É isso que significa "tomar vida".** Não é o sistema ficar mais esperto sozinho. É que **o trabalho
feito volta para o acervo como estrutura, não como recado** — e o acervo, mais rico, aciona o
trabalho seguinte. Cada volta deixa o cérebro com mais material verificável do que na volta anterior.

Um arquivo morto acumula documentos. Este acumula **documentos com procedência, decisão registrada e
o trabalho que eles causaram**.

---

## 6 · Como uma pessoa interage com isso, na prática

| | O que é | Estado |
|---|---|---|
| **Perguntar ao acervo** | Você pergunta em linguagem natural; volta a resposta **e as fontes citadas**, cada uma com o documento e um score de 0 a 1. | ✅ existe `[C]` |
| **Conversar com um agente** | Um agente com instrução própria, memória de conversa e custo por resposta. | ❌ **não existe** — faltam duas ligações `[P]` |
| **Receber endereçamento** | A inbox com obrigações no seu nome. | ❌ não existe `[P]` |
| **Aprovar** | Decisão registrada com autoridade e faixa de vazão. | ✅ existe `[C]` |

**A parte de "perguntar ao acervo" merece destaque, porque já resolve muito:** toda resposta vem com
as fontes. Você nunca recebe uma afirmação solta — recebe a afirmação **e quais documentos nossos a
sustentaram, com o quanto cada um pesou**. É a nossa regra de ouro (zero alucinação) transformada em
comportamento de produto.

E sobre **quem pode ver o quê**: hoje a autorização real é por **organização** — mesma organização
vê, organização diferente não vê. Existe um modelo muito mais fino, por área e por nível de
sensibilidade, **construído e desligado** atrás de uma chave de configuração. Existir em código não é
o mesmo que estar valendo.

---

## 7 · As duas travas, decididas

> Estavam esperando decisão do Vinicius. Ele perguntou, em 17 ago 2026, se eu já não tinha resposta
> para adotar e seguir. Tinha — mas uma delas eu só soube depois de **verificar** em vez de supor.

### Decisão 1 · Front-matter nos MDs: **NÃO.** O `_indice/` já é a camada de extração
Eu vinha tratando isso como pendência. Fui olhar o que já existe e a resposta estava pronta:

- A **chave estável do cliente** já existe — `### ID do cliente`, dentro do MD, definida no
  `protocolo-criacao-cliente.md` desde 03 ago, precisamente para o nome da pasta ser só apresentação.
- O `_indice/clientes.csv` **já extrai** essa chave junto com o caminho do arquivo. Já são
  **1.316 MDs, zero com front-matter**.

Tudo que a importação precisa **já é derivável**: o tipo pelo nome do arquivo, a área pela pasta, o
cliente pela chave que já está no corpo, o caminho pelo próprio caminho, e o commit pelo Git.

> **Front-matter seria uma segunda cópia de dado que já tem dono.** Duas fontes para o mesmo fato
> divergem — é exatamente o defeito que já criticamos na arquitetura alheia. **Decidido: o
> `_indice/` passa a ser o contrato de importação**, e `gen-indice.ps1` vira a primeira metade do
> importador. Se algum dia aparecer um campo genuinamente não-derivável, ele ganha front-matter
> naquele momento — e não antes.

### Decisão 2 · As 9 categorias como discriminador de tipo: **ADOTADO, 9 POR CASA**
`institucional` · `jornada` · `pessoas` · `contexto-area` · `produto` · `integracao` · `protocolo` ·
`demanda` · `rfi`. Minúsculo, sem acento — o schema exige slug minúsculo.

Forçado pela etapa 4: categoria é o único eixo pelo qual o mural distingue tipos.

**A multiplicidade também está decidida, e não precisou de ninguém — precisou de leitura.** Eu havia
declarado "não sei se é 9 no total ou 9 por cliente, depende de `organizations.schema.ts`, que eu não
li". Fui ler. A resposta estava num comentário do próprio schema:

> *"Mapping de compatibilidade: **Organization legado → Tenant + um Second Brain**."*

A cadeia fecha assim `[C]`:

```
tenant (o cliente)  →  exatamente UM Second Brain  (índice único parcial)
                    →  organizations, slug único POR BRAIN
                    →  categories, slug único POR organizationId
```

`Organization` é o conceito **legado**; o modelo governado é **Tenant + Second Brain**, e
`organizations` guarda `tenantId`/`brainId` como ponte de compatibilidade. Como o namespace de
organização é **por brain**, e brain é **por cliente**:

> **Decidido: 9 categorias por casa — 9 em cada cliente e 9 na Casa uMode.** 47 casas × 9 = **423
> categorias**. Não é redundância: é a **regra de isolamento de cliente expressa no modelo de dados**.
> O `jornada` da Cambos e o da Puket são objetos distintos, em brains distintos, e nenhuma consulta
> pode confundi-los nem por acidente de configuração.

Confirmação independente, no mesmo arquivo: o `pre('findOneAndDelete')` de Organization apaga
`categories`, `contexts` e `context_chunks` por `organizationId` — **organização é a fronteira de
contenção do conteúdo.** Isolamento por construção.

**A consequência operacional, que é o achado de verdade:** `triggers` também são escopados por
`brainId` + `tenantId`. Logo **a automação não é global — ela é por cliente, replicada**, exatamente
como já replicamos as 14 áreas nos 46 clientes. Criar um cliente passa a significar: 14 áreas + 9
categorias + as inscrições. **Isso tem de entrar no `protocolo-criacao-cliente.md`.**

⚠ **Um fio solto que eu nomeio sem fingir que resolvi:** se cada cliente é um brain isolado, a
membrana Casa↔cliente (o `conecta_area_cliente` de cada Produto) atravessa brains. Existem os módulos
`federation-connections` e `federation-discovery`, que **eu não li** — provável que sejam esse
mecanismo. É a próxima leitura, não um palpite.

### Decisão 2-bis · De onde "Categoria" veio, e o custo que eu não tinha declarado
> Vinicius perguntou em 17 ago 2026: *"Mas 'Categoria' surgiu de onde? Do banco? Do conteúdo do
> João? Do nosso conteúdo?"* Pergunta de procedência. Verifiquei as quatro faixas em vez de
> responder de memória — e a verificação achou um problema no meu próprio desenho.

| Faixa | O que a busca encontrou | Veredito |
|---|---|---|
| **A · código do banco** | `categories.schema.ts` nasceu no **commit fundacional do repositório** — `a470f8d`, 14 jul 2026, o primeiro commit que existe. Não é peça recente. E o `ask` usa categoria como **filtro de busca**: `ask.dto.ts` tem `category?: string`, e a resposta cita `organizationSlug/categorySlug`. | ✅ **A coleção é do banco.** |
| **B · vault do João** | 282 arquivos contêm "categor" — e **todos são domínio**: categoria de produto de moda (`Temporada → Marca → Coleção → Categoria → Produto`), categoria de conteúdo, categorias em PRD. **Não está no glossário dele nem na hierarquia do BrainHub.** | ❌ **Não vem do João.** |
| **C · Lovable** | **Uma** ocorrência: `"label": "categoria"` — rótulo de campo na tela de importar. | ❌ **Não é conceito do Lovable.** |
| **D · nosso conteúdo** | A palavra **não existe na nossa hierarquia**: Instituição → Institucional → Áreas → Subáreas → Pessoas. | ❌ **Não é nosso.** |

> **Conclusão de procedência: a COLEÇÃO é do banco (faixa A, fundacional). O USO dela como
> discriminador de tipo de MD é 100% proposta minha (faixa D), de 17 ago 2026, forçada pelo L2.**
> Ninguém no João, no Lovable ou no nosso padrão jamais tratou Categoria como tipo de documento.

**E aqui está o custo que a verificação expôs.** No código, Categoria é **unidade de agrupamento com
política de audiência**, usada para filtrar busca. Eu estou sobrepondo nela um segundo papel: **rótulo
de tipo**. Os dois não cabem juntos, e o motivo é o invariante de categoria governada:

- Uma categoria **governada** exige `brainId` + `tenantId` + **`areaId`** + `stewardAreaId` +
  `audienceMode`, tier T2. **Ou seja: está amarrada a UMA área.**
- Uma categoria **não-governada** é legal — o `pre('validate')` só dispara se algum campo governado
  estiver preenchido. Aí ela é só agrupamento, e a autorização recai no nível de organização.

> 🔴 **O trade, dito com clareza: Categoria pode ser o eixo de TIPO ou o eixo de AUDIÊNCIA — não os
> dois.** Se for tipo (9 por casa, não-governadas), a autorização fica por organização — que é
> justamente o que está ligado hoje, já que a audiência fina está atrás de feature flag. Se for
> audiência por área, ela passa a ser por (tipo × área) — **9 × 14 × 47**, e o L2 deixa a trigger sem
> nenhum eixo de tipo, porque não há outro campo no payload.

**Minha recomendação continua sendo tipo**, por três razões: é o que faz o roteamento existir; a
audiência fina está desligada de todo modo; e o isolamento por cliente já vem do brain, não da
categoria. **Mas isto é escolha com custo declarado, não caminho óbvio** — e é decisão a levar ao
Bergson junto com o resto, porque quem for ligar a audiência fina precisa saber que esse eixo foi
gasto.

---

## Fontes
`_fluxo-dados-brainhub.md` (autoridade sobre o fluxo) · `_dicionario-dados-brainhub.md` (campo a
campo) · `protocolo-criacao-cliente.md` (a chave estável) · `_indice/clientes.csv` ·
`_pendencias-gerais.md` 183–191

## Governança
Somente o CEO altera conteúdo no BrainHub. Documento didático: alterar aqui exige que o
`_fluxo-dados-brainhub.md` tenha sido alterado primeiro — **a explicação nunca lidera o fato.**
