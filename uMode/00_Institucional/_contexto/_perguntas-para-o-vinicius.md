---
aliases:
  - "Perguntas para o Vinícius"
tags:
  - tipo/autoridade
  - casa
---
# Perguntas para o Vinícius

> **Classe: `DERIVADO`.** Gerado por `scripts/gera-pendencias-e-fontes.py`.
> 🔴 **Não se edita à mão** — a pergunta nasce no arquivo do cliente e é colhida daqui.
>
> **Decisão do Vinícius em 22 set 2026:** *"em dado momento, você montará uma lista de
> coisas que eu tenho que perguntar e vou dar um jeito de responder ou por áudio ou numa
> transcrição de reunião mesmo."* **Este é esse arquivo.**

**O processo inteiro está no** [`protocolo-perguntas-ao-vinicius.md`](../_protocolos/protocolo-perguntas-ao-vinicius.md). 🔴 **Não inventar outro caminho.**

## 0 · O placar

| Estado | Quantas | O que significa |
|---|--:|---|
| 🔴 **aberta** | **43** | ninguém decidiu ainda |
| 🟢 aprovada | 0 | a resposta virou contexto e já vale |
| ⚪ recusada | 0 | decidiu-se que **não precisa de resposta** — a justificativa é o contexto |
| 🟡 alterada | 0 | a pergunta mudou de forma; a justificativa diz por quê |
| 🔵 respondida | 3 | respondida por fonte ou por pessoa |
| | **46** | **total na fila** |

**Das abertas:** 22 transversais · 21 de um cliente só · **3 já fechadas** (aprovada, recusada, alterada ou respondida).

### 0.1 · Por quem responde — a fila de distribuição

> 🔴 **Travado pelo Vinícius em 23 set 2026:** *provavelmente não serei eu que
> responderei*. Cada pergunta aberta tem **um destinatário nomeado**. Quem recebe
> pode **aprovar**, **recusar** (com o motivo de não precisar de resposta) ou
> **alterar** a pergunta — e **a justificativa sempre entra no contexto**.

| Quem responde | Perguntas abertas |
|---|--:|
| **⚠ a distribuir** | 43 |

**Clientes com página ainda não aberta:** 32.

> ⚠ **A lista está curta porque a varredura está no começo**, não porque há poucas
> dúvidas. **32 clientes têm a página fechada** — pergunta boa nasce de varredura feita.

## 1 · Transversais — valem para a carteira toda

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | 🔴 **A base `Documentação CX` traz três rótulos de SEGMENTO — `[SaaS]`, `[CX] Enterprise` e `SMB` — e nenhuma ficha de cliente do corpus carrega segmento.** **Quais são os segmentos de verdade, e qual cliente está em cada um?** | `T2` | 🔴 **muda leitura de carteira inteira**: 48 clientes tratados como um bloco só. E dá sentido à fonte `Segmentação Grupos` | **⚠ a distribuir** | aberta |
| 2 | O `Health Score` é um dashboard Looker **`Em Construção` desde fev/2025**. **Ele existe hoje, ou parou?** | `T2` | é a métrica de saúde de conta que o corpus não tem — e há quatro superfícies de relatório (Looker, BigQuery, Blazzer, uDash) sem dono declarado | **⚠ a distribuir** | aberta |
| 3 | 🔺 **Pergunta reformulada no mesmo dia.** A matriz da Lofty Style dá permissão a uma PESSOA (*Liberado só Isadora desse Perfil*, *Somente a Dora*). 🟢 **O mecanismo existe — é `scopable: user`, documentado desde 2024 no Manual do Permissionamento.** Então a pergunta é outra: **essas duas regras estão APLICADAS no sistema, ou só combinadas no papel?** | `T2` | eu tinha escrito que o uFlow não tinha onde guardar isso. **Tinha — e a página que respondia já estava na minha lista de fontes não varridas, a uma leitura de distância.** | **⚠ a distribuir** | aberta |
| 4 | Três clientes têm um perfil que é só consulta — `Objetiva - Consulta`, `NV - View` e `Lofty - Mkt, Multimarcas e ecommerce`. **Isso é uma licença mais barata, ou o mesmo usuário com menos permissão?** | `T1` | mexe em contagem de usuário contratado | **⚠ a distribuir** | aberta |
| 5 | Onze linhas da Lofty Style e oito da Moda Objetiva estão 🔴 para **todos os perfis, Admin inclusive**. **Isso é permissão negada ou funcionalidade desligada na conta?** | `T2` | 🔴 **o corpus registra as duas coisas com o mesmo símbolo** — e são decisões diferentes, de donos diferentes | **⚠ a distribuir** | aberta |
| 6 | 🔺 **O placar do `Fale com o Suporte` fechou: 4 clientes bloqueiam (Luiza Barcelos, Lenny, NK STORE, Recco) e 5 liberam (VIX, Oficina Reserva, Cambos, Moda Objetiva, NV).** É decisão comercial, decisão de atendimento, ou herança de quem configurou? | `T2` | 🔴 **derruba a hipótese que eu tinha levantado com 2 casos** — não é padrão, é configuração por cliente. **E nenhuma métrica de chamado entre contas se sustenta sem esse asterisco.** | **⚠ a distribuir** | aberta |
| 7 | 🔴 **`> excluir variante` está LIBERADO na Recco** e bloqueado em VIX, Reserva, Lofty Style e NV. **Então a dor de excluir variante é configuração, não limitação da plataforma?** | `T2` | 🔴 **eu vinha registrando como dor de PRODUTO em cinco clientes** — se for permissão, a solução é outra e é barata | **⚠ a distribuir** | aberta |
| 8 | A NV tem **`Todas as Subcoleções`** onde todo mundo tem `Todas as Coleções`, e a Moda Objetiva tem **`Grupo`** como cadastro. **Isso é o nível que a CAEDU pede desde 16/09/2025?** | `T2` | 🔴 **se for, a resposta para a CAEDU já está rodando em dois clientes** — e a dor dela é só integração | **⚠ a distribuir** | aberta |
| 9 | A NV tem uma tela **`Audit uMode x Linx`** na ficha de produto. **Ela existe para todos os clientes Linx ou foi feita só para a NV?** | `T2` | NK STORE também é Linx, e a VIX tem tabela DE/PARA campo a campo feita à mão | **⚠ a distribuir** | aberta |
| 10 | A página-mãe da NV diz **`Restrição`**; a sub-página `NV - Geral` diz **`exclusão`** para a mesma coisa. **Qual dos dois é o termo?** | `T2` | o `CLAUDE.md` trava taxonomia como essencial — e aqui são duas palavras a uma clicada de distância | **⚠ a distribuir** | aberta |
| 11 | 🔴 **`Fale com o Suporte` está BLOQUEADO para todos os 6 perfis da Luiza Barcelos e LIBERADO para todos os 17 da VIX. É decisão ou configuração esquecida?** | `T2` | 🔴 **explica por que a conta parecia invisível na base de chamados** — e significa que **volume de chamado mede quem tem o botão, não atividade de conta** | **⚠ a distribuir** | aberta |
| 12 | 🔴 **`Fornecedor` é perfil de usuário com login na Luiza Barcelos e na Lenny Niemeyer. Como o BrainHub modela isso?** Não é pessoa de cliente nem pessoa da Casa — **é uma terceira natureza, e ela já tem acesso à plataforma.** | `T2` | junta-se à `Qualitá` da Oficina Reserva, que opera por WhatsApp | **⚠ a distribuir** | aberta |
| 13 | ⚠ **O `Manual` está bloqueado para TODOS os perfis nos dois clientes que li** (VIX e Luiza Barcelos). **É assim nos outros oito?** Se for, a dor da CAEDU sobre manual insuficiente muda de natureza. | `T2` | se ninguém acessa, a pergunta não é se o manual é bom | **⚠ a distribuir** | aberta |
| 14 | 🔴 **Por que o desenho de `Griffe › Linha › Grupo › Subgrupo` feito para a **Loungerie** nunca chegou na **CAEDU**?** A CAEDU pede essa hierarquia desde a weekly de **16/09/2025** e ela reaparece idêntica em jul e ago/2026. A página da Loungerie tem os **4 níveis com exemplos e até a alternativa de extensibilidade**. | `T2` | 🔴 **não é pergunta de taxonomia, é de circulação de conhecimento** — e é exatamente o que o BrainHub existe para impedir | **⚠ a distribuir** | aberta |
| 15 | ⚠ **A hierarquia da Loungerie foi IMPLEMENTADA ou é só desenho na página?** Muda se serve de referência provada ou de proposta. | `T2` | define se dá para levar à CAEDU como caso pronto | **⚠ a distribuir** | aberta |
| 16 | 🔴 **Como o BrainHub modela GRUPO ECONÔMICO?** Achei dois: **Grupo Único** (Puket — gente com e-mail `@grupounico.com` opera dentro da conta) e **Grupo AR&CO** (Oficina Reserva entrou *no mesmo pacote do Grupo*, e a dor número 1 dela cita dependência do **time da Arezzo**). **Reserva, Oficina Reserva, Simples e Arezzo são quatro pastas isoladas para o que pode ser um contrato só.** | `T2` | o isolamento de cliente é regra travada, e grupo econômico a atravessa | **⚠ a distribuir** | aberta |
| 17 | 🔴 **Como o BrainHub modela TERCEIRO que não é cliente nem fornecedor de material?** A `Qualitá` inspeciona qualidade para a Oficina Reserva, **por WhatsApp**, e a fonte registra que *o inspetor chega para auditar e não tem o documento*. | `T2` | é onde a operação do cliente vaza para fora de qualquer sistema | **⚠ a distribuir** | aberta |
| 18 | 🔴 **A dor de excluir/inativar variante aparece em QUATRO clientes** — VIX, Reserva, Lofty Style e NV (com dois documentos). **É lacuna da plataforma?** | `T2` | quatro casos independentes: não é mais hipótese | **⚠ a distribuir** | aberta |
| 19 | **`Status` ou `Etapa` — qual manda?** Discordam em 5 clientes. | `T2` | 🟢 **Respondida em 22 set 2026 pelo Vinícius:** *"a verdade é que não sei. Nós vamos ter que ver caso a caso."* — vira **pergunta por cliente**, não regra geral | **⚠ a distribuir** | respondida em 22 set 2026, por mensagem |
| 20 | **O portfólio de 16 Soluções está incompleto?** `uBuy` aparece em três clientes (Osklen, NK STORE, Reserva) e `uPlan` na Reserva, e nenhum dos dois está na lista. | `T2` | um caso é anedota, três é padrão | **⚠ a distribuir** | aberta |
| 21 | **Qual é a chave de identidade de pessoa?** Sem ela, grafia diferente não se resolve sem inventar gente. | `T2` | trava a fusão de 149 fichas | **⚠ a distribuir** | aberta |
| 22 | **O campo `Data de Churn` não existe na base.** Criamos? | `T2` | segue sendo a lacuna mais cara do corpus | **⚠ a distribuir** | aberta |
| 23 | **`Merchandising`, `Curadoria`, `Oficina` e `facção` não existem na grade de 14 áreas.** A grade cresce, ou viram subárea? | `T2` | sexta evidência do `15_Producao-Interna` | **⚠ a distribuir** | aberta |

## 2 · Por cliente

### Baw

[abrir o arquivo do cliente](../../_Clientes/Baw/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | A Baw tem o módulo `Integração` contratado **e** o ERP diz `Sem Integração`. **Qual dos dois está errado?** | `T2` | quinta evidência independente de que a conta está mal classificada | **⚠ a distribuir** | aberta |

### Caedu

[abrir o arquivo do cliente](../../_Clientes/Caedu/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | O `Status` da CAEDU virou `Onboarding` em 22/09/2026 às 15:04, e a base `Etapas do Processo` continua marcando `Ongoing`. **O que mudou nesse dia?** | `T2` | o projeto CAEDU 2.0 está sendo montado sobre a premissa de onboarding | **⚠ a distribuir** | aberta |
| 2 | A dor `Griffe › Linha › Grupo/subgrupo` está escrita desde a weekly de 16/09/2025 e reaparece idêntica em jul e ago/2026. **Quem assume a integração — uMode ou o time tech da CAEDU?** | `T2` | atravessou três ciclos sem destravar | **⚠ a distribuir** | aberta |

### Cambos

[abrir o arquivo do cliente](../../_Clientes/Cambos/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | Há duas contas na plataforma — `Cambos` (7 usuários) e `Cambos - uFlow` (25). **É conta por módulo, ou duplicidade?** | `T2` | define se `client_id` é mesmo único por cliente | **⚠ a distribuir** | aberta |
| 2 | O conteúdo T1 da Cambos está com autorização de uso pendente desde julho. **Libera?** | `T1` | trava registrada há mais de dois meses | **⚠ a distribuir** | aberta |

### Lofty Style

[abrir o arquivo do cliente](../../_Clientes/Lofty Style/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | 🚨 **A credencial do site de documentação foi rotacionada?** | `T0` | exposição ativa até prova em contrário | **⚠ a distribuir** | aberta |
| 2 | Os dois arquivos de staging `SUPERSEDED` seguem no repositório. **Apago?** | `T2` | apagar é decisão sua, não minha | **⚠ a distribuir** | aberta |

### Moda Objetiva

[abrir o arquivo do cliente](../../_Clientes/Moda Objetiva/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | A página de perfil termina apontando para uma **planilha Google com os e-mails dos usuários**. **Posso abrir?** É o equivalente da base `Usuários` da NK STORE, só que fora do Notion. | `T2` | é a fonte de pessoa deste cliente | **⚠ a distribuir** | aberta |

### Mondepars

[abrir o arquivo do cliente](../../_Clientes/Mondepars/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | `Mondepars` × `Mondpars` — **qual grafia está certa?** | `T2` | 🟢 **Respondida em 22 set 2026:** *o nome certo da empresa é Mondepars* — pasta renomeada; ⚠ **o CRM segue com a grafia errada** | **⚠ a distribuir** | respondida em 22 set 2026, por mensagem |

### NK STORE

[abrir o arquivo do cliente](../../_Clientes/NK STORE/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | Há **duas `Cristina`** na base de usuários da NK STORE (`cristina@` em Compras, `cristina.amorim@` em Modelagem) e **uma ficha `cristina.md`** vinda da base de demandas, que traz só o primeiro nome. **Qual das duas abriu as demandas?** | `T2` | 🔴 **o gerador PAROU e avisou em vez de sobrescrever** — sem a resposta, ficam duas fichas para uma pessoa ou uma ficha para duas | **⚠ a distribuir** | aberta |
| 2 | A base tem **`kemelly.fernandes@`** e o corpus tem a ficha **`kemely.md`**, um `l` de diferença. E tem **`silvia.nascimento@`** contra **`silvia-shirlei-dias.md`**. **São as mesmas pessoas?** | `T2` | **não fundi — uma letra não é prova** | **⚠ a distribuir** | aberta |
| 3 | **5 das 30 linhas têm `Departamento NK = INATIVAR`.** É instrução pendente ou já foi executada? E **qual era a área real dessas pessoas antes de o campo ser sequestrado?** | `T2` | são 5 pessoas sem área no corpus | **⚠ a distribuir** | aberta |
| 4 | A matriz de permissão **não tem o perfil `NK - PCP`**, mas **7 pessoas o usam**. E os perfis `NK - Time` e `Fornecedor`, que a matriz detalha, **não têm nenhum usuário**. **Qual dos dois documentos está velho?** | `T2` | 7 pessoas sem permissão documentada | **⚠ a distribuir** | aberta |
| 5 | 🚨 **A credencial de produção do Linx está em texto claro na página do cliente. Foi rotacionada?** | `T0` | exposição ativa até prova em contrário | **⚠ a distribuir** | aberta |
| 6 | `Merchandising`, `Curadoria` e `Oficina` são etapas do processo com dono e não existem na grade de 14 áreas. **Viram área canônica, subárea, ou apelido?** | `T2` | é o mesmo tema do `15_Producao-Interna` | **⚠ a distribuir** | aberta |

### Osklen

[abrir o arquivo do cliente](../../_Clientes/Osklen/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | O `Status` diz `Operação Assistida` e a `Etapa` diz `Onboarding`. **Qual descreve a conta hoje?** | `T2` | muda a leitura de maturidade da conta | **⚠ a distribuir** | aberta |
| 2 | O toggle `Pessoas` da página está vazio. **Quem são a diretoria e os líderes de departamento da Osklen?** | `T2` | sem isso a conta não tem uma pessoa nomeada na própria página | **⚠ a distribuir** | aberta |

### Reserva

[abrir o arquivo do cliente](../../_Clientes/Reserva/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | 7 módulos contratados e **nenhuma etapa do processo atribuída**. **Conta grande não passa pelo funil, ou é lacuna de preenchimento?** | `T2` | vale para Oficina Reserva, NV e Baw também | **⚠ a distribuir** | aberta |
| 2 | O `Review Quinzenal de Projeto` tem envios marcados até 30/06 e nada depois. **A cadência parou ou só parou de ser marcada?** | `T2` | é a única cadência formal de report a cliente que o corpus conhece | **⚠ a distribuir** | aberta |
| 3 | 5 dos 9 grupos de WhatsApp estão marcados para excluir e continuam existindo. **A limpeza foi feita?** | `T2` | canal fora de sistema é onde a operação vaza | **⚠ a distribuir** | aberta |

### Simples (by Reserva)

[abrir o arquivo do cliente](../../_Clientes/Simples (by Reserva)/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | A pasta `Simples (by Reserva)` não tem linha na base. **É marca da Reserva ou conta própria?** | `T2` | 🟢 **Respondida em 22 set 2026:** *é marca de dentro da Reserva; a nível de contratação é RESERVA mesmo* — ⚠ resta saber se tem usuários e permissões próprios | **⚠ a distribuir** | respondida em 22 set 2026, por mensagem |

### VIX

[abrir o arquivo do cliente](../../_Clientes/VIX/00_Institucional/_contexto/_pendencias-e-fontes.md)

| # | Pergunta | Tier | Por que importa | Quem responde | Estado |
|--:|---|:-:|---|---|---|
| 1 | A VIX tem **5 perfis só de Estilo** (Biquini, Cover ups, PA, Roupas, Admin). **Isso vira subárea canônica no BrainHub, ou continua sendo só perfil da plataforma?** | `T2` | define se perfil e área são a mesma entidade ou duas | **⚠ a distribuir** | aberta |
| 2 | A matriz de ~60 funções × 17 perfis foi editada pela última vez em **09/07/2025** e é mantida à mão. **Ainda reflete a plataforma?** | `T2` | se não reflete, o corpus estaria copiando ficção | **⚠ a distribuir** | aberta |

## Governança

### Quem pode alterar este documento
🔴 **Ninguém à mão.** É `DERIVADO` — corrigir na fonte (`scripts/gera-pendencias-e-fontes.py`) e rodar o script.

### O que acontece com uma pergunta respondida
**Não se apaga: muda de estado**, com a data e a fonte da resposta. O histórico do que
já se perguntou é tão útil quanto a resposta.

