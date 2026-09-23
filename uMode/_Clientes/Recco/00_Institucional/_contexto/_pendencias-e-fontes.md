# Recco · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o Recco?" e
> "onde eu já procurei?".** O [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md) segue dono das decisões
> **transversais** — as que valem para a carteira toda. **Um assunto, um dono.**

## 0 · O tier de sensibilidade

**Vocabulário `T0`/`T1`/`T2`, o mesmo que o João usa no vault** — não um paralelo nosso.

| Tier | O que é | O que eu faço |
|:-:|---|---|
| **`T2`** | equipe | o padrão — entra normalmente |
| **`T1`** | restrito | entra, e **fica só no `_contexto/` deste cliente** |
| **`T0`** | privado | 🔴 **nunca entra por valor** — registro que existe e **onde** |

## 1 · Risco de segurança

🟢 **Nenhum achado até 22 set 2026.**

⚠ **Isso não é atestado de limpeza:** significa que **nas fontes da § 3** não apareceu
segredo. **As fontes da § 4 não foram olhadas.**

## 1-bis · 🔴 O que eu NÃO consegui ler

> **Pedido do Vinícius em 22 set 2026:** *sobre suspeitas de blocos, sempre tenha atenção e me indique, porque temos que ter a garantia de que tudo que está varrendo está conseguindo tirar proveito de tudo o que podemos*.
>
> 🔴 **Bloco que não renderiza NÃO é bloco vazio.** Na Luiza Barcelos, 17 blocos ilegíveis escondiam **o único Representante Legal da conta** e o cargo do Gerente de Inovação e Tecnologia. **Eu cheguei a chamar isso de falta de acesso, e estava errado** — ver `protocolo-varredura-cliente.md` § 11.

🟢 **Nada ilegível nas fontes já abertas.**

⚠ **Isso só vale para o que foi aberto** (§ 3). **Nas fontes da § 4 não sei**, e a página deste cliente pode ter o mesmo tipo de bloco.

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🔴 **Os perfis da Recco NÃO têm prefixo de cliente:** `Admin`, `Time`, `Fornecedor`. **Todos os outros nove clientes lidos prefixam** (`NK - `, `Objetiva - `, `LN - `, `Oficina - `, `NV - `). ⚠ **Num banco multi-conta, perfil sem prefixo é colisão esperando acontecer.** | `T2` | decisão de modelagem |
| 2 | 🟢 **`> excluir variante` está LIBERADO para `Admin` e `Time`.** 🔴 **É o PRIMEIRO caso do corpus.** Contra VIX, Reserva, Lofty Style e NV (bloqueado) e Lenny (em branco): **6 casos, 4 bloqueiam, 1 não decidiu, 1 libera.** 🔴 **Conclusão que muda a leitura: a dor de excluir variante NÃO é limitação da plataforma — é configuração.** | `T2` | **revisar os cinco registros anteriores** |
| 3 | 🔴 **`Fale com o Suporte` bloqueado para os três perfis** — quarto cliente bloqueado. | `T2` | — |
| 4 | 🆕 **`Perfis dentro de Tarefas` = *Somente relacionados ao cliente*** — célula com **REGRA EM TEXTO**, não semáforo. 🔴 **É regra de ESCOPO DE VISIBILIDADE dentro da tarefa**, e a NK pediu a mesma coisa na validação (*ajustar lista de perfis*). **Dois casos.** | `T2` | espec de produto |
| 5 | 🆕 **A aba se chama `Fabricantes`, não `Fornecedor`** — mas a linha de criação dentro dela é `> novo fornecedor`. **O apelido do cliente ficou por cima do termo canônico só no título.** | `T2` | — |
| 6 | ⚠ **A matriz da Recco NÃO tem as linhas `Manual` nem `Base de Importação`** — como a Oficina Reserva. **Ausência de linha continua sendo coisa que eu não sei ler.** | `T2` | conferência |
| 7 | 🔴 **A página PRINCIPAL da Recco nunca foi aberta** — cheguei pela sub-página. Mesmo caso da Lenny Niemeyer. | `T2` | tempo de varredura |
| 8 | ⚠ **Ativação em 06/02/2025 e churn** — **~8 meses**, o mais curto da coorte. 🔺 **Correção registrada: eu tinha dito que as três eram equivalentes. Não são.** | `T2` | nada — corrigido |

### 2.1 · 🔴 Perguntas que só o Vinícius responde

> **Uma pergunta só entra aqui quando NENHUMA fonte pode respondê-la.** Dúvida que
> uma fonte responde não é pergunta — **é varredura que falta fazer**, e vai para a § 4.
>
> 🔴 **Estas linhas são colhidas automaticamente** para a lista consolidada em
> [`_perguntas-para-o-vinicius.md`](../../../../00_Institucional/_contexto/_perguntas-para-o-vinicius.md),
> que ele responde **por áudio ou por transcrição de reunião**. Ver
> [`protocolo-perguntas-ao-vinicius.md`](../../../../00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md).

⚠ **Nenhuma ainda** — e para este cliente isso quase sempre quer dizer que a
**página dele não foi aberta** (§ 3.2). **Pergunta boa nasce de varredura feita.**

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o Recco

| Fonte | Endereço | Quando | O que saiu | Esgotada? |
|---|---|---|---|---|
| Base `Mapa de Clientes` | `collection://ec041afd-…` | 22 set 2026 | status, módulos, ERP, atendimento, cidade, CNPJ, etapa, receita | sim, por SQL |
| Base `Demandas compartilhadas` | `collection://…` (985 linhas) | 22 set 2026 | demandas, `Quem solicitou?`, datas | sim, por SQL |
| Base `Reuniões Compartilhadas com Clientes` | `collection://09a4a94e-…` | 22 set 2026 | 1.161 reuniões, datas, cliente | ⚠ **não**: campo `Participantes` é ID de usuário, não resolvido |
| Base `Chamado&Atendimento` | `collection://2c5b1d38-…` | 22 set 2026 | 185 chamados, 92 e-mails individuais | sim, por SQL |
| Base `Portal do Cliente` | `collection://6548a3ae-…` | 21 set 2026 | segunda lista de clientes | sim, por SQL |
| Base `Etapas do Processo de Clientes` | `collection://348b1d38-…-000bea495254` | 22 set 2026 | 7 etapas; **discorda do campo `Status`** | ⚠ **não**: as 5 páginas de etapa não foram abertas |
| Repositório do **CX Hub** | leitura de código | 22 set 2026 | schema e modelo; **não é fonte de dado** — feature nunca finalizada | sim |
| 🟢 **As 10 páginas `Perfil de Usuário e Permissionamentos`** | sub-página de cliente — VIX, Luiza Barcelos, Oficina Reserva, Lenny, Cambos, NK STORE, Moda Objetiva, Recco, NV e Lofty Style | 23 set 2026 | perfis por cliente (de 3 a 17), matriz de permissão, e o placar do `Fale com o Suporte`: **4 bloqueados × 6 liberados** | 🟢 **sim, as dez** — ⚠ exceto 12 sub-páginas de perfil da NV |
| 📕 **Manual do Permissionamento** | `6d0379fa…`, em `uFlow / Setup - PLM` | 23 set 2026 | 🟢 **o MECANISMO**: `Includes`/`Excludes`, os 3 controllers, `scopable: user|policy`, 23 parâmetros de `actions`, 20 `entity_configs` e o mapa de **72 controllers** | 🟢 **sim, por inteiro** — virou `_dicionario-permissionamento-uflow.md` |
| **Google Drive** — pastas de operação | varredura de 03 ago 2026 | 03 ago 2026 | 16 Soluções, Arquitetura V1, planilha de acessos | ⚠ **não** |

### 3.2 · A página deste cliente no Notion

| Quando | Endereço | O que saiu | Esgotada? |
|---|---|---|---|
| **23 set 2026** | sub-página `Recco \| Perfil de Usuários e Permissionamentos` (`191b1d38…`) — **a página principal do cliente ainda NÃO foi aberta** | 3 perfis (`Admin`, `Time`, `Fornecedor`) — 🔴 **os únicos do corpus SEM prefixo de cliente**; 🔴 `Fale com o Suporte` bloqueado para os três; 🟢 **`> excluir variante` LIBERADO** — o primeiro caso; regra em texto na matriz: `Perfis dentro de Tarefas = Somente relacionados ao cliente` | 🔴 **não** — só esta sub-página |

### 3.3 · Sub-páginas e documentos deste cliente já abertos

> 🔴 **NÃO reabrir.** O que saiu daqui já está na seção 2.

| Quando | O quê | Endereço | O que saiu |
|---|---|---|---|
| **23 set 2026** | `Documentos Implantação uFlow › Recco \| Perfil de Usuários e Permissionamentos` | `191b1d38…` | 3 perfis **sem prefixo de cliente**; 🔴 `Fale com o Suporte` bloqueado; 🟢 **`> excluir variante` LIBERADO — o primeiro caso**; `Perfis dentro de Tarefas = Somente relacionados ao cliente`; aba `Fabricantes` |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

| Fonte | Endereço | O que deve trazer |
|---|---|---|
| Relação `Segmentação Grupos` | `collection://a4103fe2-…` | grupo/tier comercial do cliente |
| Relação `Atendimento 2024` | `collection://c82a689c-…` | quem atendeu em 2024 — o corpus só tem 2025 |
| Campo `Participantes` das 1.161 reuniões | IDs de usuário do Notion | **presença nominal com data** — a melhor fonte de pessoa ativa |
| As 1.153 atas ainda não abertas | base de reuniões | conteúdo — **e varredura de credencial** |
| **Gist** — o chat da plataforma | canal oficial de dúvida de usabilidade | conversa de suporte, por cliente |
| 🔴 **`uMode Geral / uFlow / Documentação de Setup - PLM / CLIENTES`** | segundo acervo de documentação por cliente, fora do `Mapa de Clientes` | **setup de PLM por cliente** — achado em 22 set 2026, jamais tocado |
| 🟢 `Controle de Acessos de Usuários` — **LIDA em 22 set 2026** | `uModers / Vinícius Risoleo / Assunto | Ferramenta` | deu o **modelo de dados do uFlow**; ⚠ **falta rodar as queries** e trazer o **engajamento por conta** |
| **`Databases / Processos mapeados`** | base própria do Notion | playbooks de processo — inclui o de **limite contratado de usuários** |
| **`Databases / Demandas de Clientes`** | base própria do Notion | ⚠ **é a mesma base das 999 demandas, ou outra?** Não confirmei |
| **`Operation Hub`** e o domínio `documentacao.umode.tech` | `Operação de Clientes` | 🔴 **segundo domínio de documentação**, além do `docs.umode.app` |
| Página `Ficha de Produto` e suas **7 sub-páginas de permissionamento em template** | `c3deb3dd…` — citada pelo Manual do Permissionamento | **como se bloqueia edição de aba e se libera campo por usuário** dentro da ficha |
| `umode.app/admin/j3_entity_configs` | painel administrativo de **produção** — não acessado | 🔴 **quais `entity_configs` existem e em que conta estão ativas.** O Manual lista 20 como exemplo, não como catálogo |
| **Grupos de WhatsApp** | fora de qualquer sistema | operação real — a Reserva tem 9 mapeados |

## Governança

### Quem pode alterar este documento
**A § 1, § 2 e § 3 se escrevem a cada varredura**, pelo script. Pendência resolvida **não**
**se apaga: muda de estado**, para o histórico não se perder.

### Quando ler
🔴 **Antes de varrer este cliente. Sempre.** É o que impede repetir busca já feita.

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Cliente:** `Recco` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
