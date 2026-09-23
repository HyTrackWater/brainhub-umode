# NK STORE · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o NK STORE?" e
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

| O que | Onde | Estado |
|---|---|---|
| Credencial de produção do **Linx** (usuário, senha, IP, porta, banco) | Notion — página do cliente, toggle `Documentos › Conexão com Linx` | 🚨 **exposta, não rotacionada** |

> 🚨 **O valor não foi replicado em lugar nenhum do corpus** — `T0`.
> **A rotação é ação do Vinicius.** ⚠ Pode já estar inativa; **rotacionar mesmo assim**
> é mais barato que descobrir que não estava.

## 1-bis · 🔴 O que eu NÃO consegui ler

> **Pedido do Vinícius em 22 set 2026:** *sobre suspeitas de blocos, sempre tenha atenção e me indique, porque temos que ter a garantia de que tudo que está varrendo está conseguindo tirar proveito de tudo o que podemos*.
>
> 🔴 **Bloco que não renderiza NÃO é bloco vazio.** Na Luiza Barcelos, 17 blocos ilegíveis escondiam **o único Representante Legal da conta** e o cargo do Gerente de Inovação e Tecnologia. **Eu cheguei a chamar isso de falta de acesso, e estava errado** — ver `protocolo-varredura-cliente.md` § 11.

| Onde | Quantos | O que era | Estado |
|---|--:|---|---|
| `Plano de Sucesso do Cliente` | 1 | incorporação do Google Drive | 🔴 **aberto** — não é Notion, é arquivo do Drive |

**O contorno que funciona:** pedir ao Vinícius **só aquele trecho**, copiado e colado. **Barato, e o que vier entra como fonte normal, com procedência.**

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🚨 **Credencial de produção do Linx em TEXTO CLARO** na página do cliente, toggle `Documentos › Conexão com Linx`: usuário, senha, IP, porta e nome do banco. **O valor não foi replicado em lugar nenhum do corpus.** | `T0` | 🚨 **rotação da chave — ação do Vinicius** |
| 2 | 🔴 **CPF e telefone pessoal de dois representantes legais** na mesma página. **Nada entrou no corpus** — registro que existe e onde. | `T0` | nada — é tratamento |
| 3 | 🔴 **8 das 13 pessoas com cargo nunca abriram demanda** — incluindo as **duas diretoras do projeto** (Regiane Konopka, Merchandising; Stella Sunaga, Estilo). | `T2` | nada — já corrigido, as fichas existem |
| 4 | ⚠ **`Merchandising`, `Curadoria` e `Oficina` são etapas do processo com dono, e não existem na grade canônica de 14 áreas.** Aqui **não são apelido.** | `T2` | decisão sobre a grade de áreas (item 234 — `15_Producao-Interna`) |
| 5 | ⚠ **11 das 24 pessoas seguem sem cargo** — as que vieram só da base de demandas e não aparecem no toggle `Pessoas` da página. | `T2` | preenchimento pelo atendimento |
| 6 | 🆕 **`uBuy` aparece como oportunidade** (*Follow Up de Entregas → Pedidos de Compras*) e **não está nos 7 módulos nem nas 16 Soluções.** | `T2` | decisão sobre o portfólio |

### 2.1 · 🔴 Perguntas que só o Vinícius responde

> **Uma pergunta só entra aqui quando NENHUMA fonte pode respondê-la.** Dúvida que
> uma fonte responde não é pergunta — **é varredura que falta fazer**, e vai para a § 4.
>
> 🔴 **Estas linhas são colhidas automaticamente** para a lista consolidada em
> [`_perguntas-para-o-vinicius.md`](../../../../00_Institucional/_contexto/_perguntas-para-o-vinicius.md),
> que ele responde **por áudio ou por transcrição de reunião**. Ver
> [`protocolo-perguntas-ao-vinicius.md`](../../../../00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md).

| # | Pergunta | Tier | Por que importa | Estado |
|--:|---|:-:|---|---|
| 1 | 🚨 **A credencial de produção do Linx está em texto claro na página do cliente. Foi rotacionada?** | `T0` | exposição ativa até prova em contrário | aberta |
| 2 | `Merchandising`, `Curadoria` e `Oficina` são etapas do processo com dono e não existem na grade de 14 áreas. **Viram área canônica, subárea, ou apelido?** | `T2` | é o mesmo tema do `15_Producao-Interna` | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o NK STORE

| Fonte | Endereço | Quando | O que saiu | Esgotada? |
|---|---|---|---|---|
| Base `Mapa de Clientes` | `collection://ec041afd-…` | 22 set 2026 | status, módulos, ERP, atendimento, cidade, CNPJ, etapa, receita | sim, por SQL |
| Base `Demandas compartilhadas` | `collection://…` (985 linhas) | 22 set 2026 | demandas, `Quem solicitou?`, datas | sim, por SQL |
| Base `Reuniões Compartilhadas com Clientes` | `collection://09a4a94e-…` | 22 set 2026 | 1.161 reuniões, datas, cliente | ⚠ **não**: campo `Participantes` é ID de usuário, não resolvido |
| Base `Chamado&Atendimento` | `collection://2c5b1d38-…` | 22 set 2026 | 185 chamados, 92 e-mails individuais | sim, por SQL |
| Base `Portal do Cliente` | `collection://6548a3ae-…` | 21 set 2026 | segunda lista de clientes | sim, por SQL |
| Base `Etapas do Processo de Clientes` | `collection://348b1d38-…-000bea495254` | 22 set 2026 | 7 etapas; **discorda do campo `Status`** | ⚠ **não**: as 5 páginas de etapa não foram abertas |
| Repositório do **CX Hub** | leitura de código | 22 set 2026 | schema e modelo; **não é fonte de dado** — feature nunca finalizada | sim |
| **Google Drive** — pastas de operação | varredura de 03 ago 2026 | 03 ago 2026 | 16 Soluções, Arquitetura V1, planilha de acessos | ⚠ **não** |

### 3.2 · A página deste cliente no Notion

| Quando | Endereço | O que saiu | Esgotada? |
|---|---|---|---|
| **22 set 2026** | `0f24dfbe…` | **13 pessoas com cargo e área**; processo `Planejamento → Estilo → Compras/Merchandising → PCP → Oficina`; dores mapeadas; **`uBuy`** como oportunidade; 🚨 **credencial de produção em texto claro** | ⚠ **não** — 1 bloco não abriu (`Plano de Sucesso do Cliente`) |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

| Fonte | Endereço | O que deve trazer |
|---|---|---|
| Relação `Segmentação Grupos` | `collection://a4103fe2-…` | grupo/tier comercial do cliente |
| Relação `Atendimento 2024` | `collection://c82a689c-…` | quem atendeu em 2024 — o corpus só tem 2025 |
| Campo `Participantes` das 1.161 reuniões | IDs de usuário do Notion | **presença nominal com data** — a melhor fonte de pessoa ativa |
| As 1.153 atas ainda não abertas | base de reuniões | conteúdo — **e varredura de credencial** |
| **Gist** — o chat da plataforma | canal oficial de dúvida de usabilidade | conversa de suporte, por cliente |
| 🔴 **`uMode Geral / uFlow / Documentação de Setup - PLM / CLIENTES`** | segundo acervo de documentação por cliente, fora do `Mapa de Clientes` | **setup de PLM por cliente** — achado em 22 set 2026, jamais tocado |
| **As 10 páginas `Perfil de Usuário e Permissionamentos`** | sub-página de cliente | **perfis = áreas do cliente** e a matriz de permissão — **2 lidas de 10** |
| **`Linear`** — gestão de projeto da uMode | linear.app/umode | roadmap e PRDs — há item `offTrack` desde jan/2026 |
| **Grupos de WhatsApp** | fora de qualquer sistema | operação real — a Reserva tem 9 mapeados |

## Governança

### Quem pode alterar este documento
**A § 1, § 2 e § 3 se escrevem a cada varredura**, pelo script. Pendência resolvida **não**
**se apaga: muda de estado**, para o histórico não se perder.

### Quando ler
🔴 **Antes de varrer este cliente. Sempre.** É o que impede repetir busca já feita.

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Cliente:** `NK STORE` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
