# Lofty Style · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o Lofty Style?" e
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
| Credencial do **site de documentação** | Notion — página do cliente, toggle `Documentação/Regras`, ao lado da URL `docs.umode.app/integracao-lofty` | 🚨 **exposta, não rotacionada** |

> 🚨 **O valor não foi replicado em lugar nenhum do corpus** — `T0`.
> **A rotação é ação do Vinicius.** ⚠ Pode já estar inativa; **rotacionar mesmo assim**
> é mais barato que descobrir que não estava.

## 1-bis · 🔴 O que eu NÃO consegui ler

> **Pedido do Vinícius em 22 set 2026:** *sobre suspeitas de blocos, sempre tenha atenção e me indique, porque temos que ter a garantia de que tudo que está varrendo está conseguindo tirar proveito de tudo o que podemos*.
>
> 🔴 **Bloco que não renderiza NÃO é bloco vazio.** Na Luiza Barcelos, 17 blocos ilegíveis escondiam **o único Representante Legal da conta** e o cargo do Gerente de Inovação e Tecnologia. **Eu cheguei a chamar isso de falta de acesso, e estava errado** — ver `protocolo-varredura-cliente.md` § 11.

🟢 **Nada ilegível nas fontes já abertas.**

⚠ **Isso só vale para o que foi aberto** (§ 3). **Nas fontes da § 4 não sei**, e a página deste cliente pode ter o mesmo tipo de bloco.

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🚨 **A credencial do site de documentação está EM TEXTO CLARO na página do cliente**, no toggle `Documentação/Regras`, ao lado da URL `docs.umode.app/integracao-lofty`. **O valor não foi replicado em lugar nenhum.** | `T0` | 🚨 **rotação da chave — ação do Vinícius** |
| 2 | 🔴 **O `Status` diz `Ongoing` e a `Etapa` diz `Operação Assistida`.** | `T2` | pergunta registrada |
| 3 | 🔴 **O toggle `Pessoas` existe e está VAZIO** — segundo caso, junto da Osklen. **De 3 clientes que têm o toggle, 1 preencheu.** | `T2` | preenchimento pelo atendimento |
| 4 | 🔴 **TERCEIRO cliente com a dor de excluir/inativar variante** — a página tem `Exclusão de Variante após integração`. Os outros dois: **VIX** (aprendizado de permissão) e **Reserva** (cartão antigo). **Um caso é anedota, dois é hipótese, três é PADRÃO.** | `T2` | decisão de produto — é lacuna da plataforma, não do cliente |
| 5 | ⚠ **Dois arquivos de staging `SUPERSEDED` seguem no repositório.** **Apagar é decisão sua.** | `T2` | decisão do Vinícius (item 257) |
| 6 | 🆕 **Duas `Atualização de Projeto`** (12/01/2026 e 29/01/2026) e nada depois. ⚠ **Mesma marca da Reserva**, cuja cadência parou em 30/06. | `T2` | conferência com o atendimento |
| 7 | 🆕 **Duas pesquisas de CSat** (Kick Off e Treinamento) — **segundo cliente com CSat**, junto da Osklen. **Fonte nunca varrida.** | `T2` | tempo de varredura |
| 8 | 🆕 `NCM e Código CEST` — **tema fiscal**, que nenhuma área canônica das 14 cobre com clareza. | `T2` | — |

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
| 1 | 🚨 **A credencial do site de documentação foi rotacionada?** | `T0` | exposição ativa até prova em contrário | aberta |
| 2 | Os dois arquivos de staging `SUPERSEDED` seguem no repositório. **Apago?** | `T2` | apagar é decisão sua, não minha | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o Lofty Style

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
| **22 set 2026** | `293c8829…` | toggle `Pessoas` **presente e VAZIO**; 🚨 **a credencial do site de documentação está em texto claro na página**; `Exclusão de Variante após integração`; `NCM e Código CEST`; duas `Atualização de Projeto` (12/01 e 29/01/2026); **duas pesquisas de CSat**; documento `As Is`; quadro Miro | ⚠ **não** — 6 sub-páginas e 4 databases inline não abertos |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

| Fonte | Endereço | O que deve trazer |
|---|---|---|
| Relação `Segmentação Grupos` | `collection://a4103fe2-…` | grupo/tier comercial do cliente |
| Relação `Atendimento 2024` | `collection://c82a689c-…` | quem atendeu em 2024 — o corpus só tem 2025 |
| Campo `Participantes` das 1.161 reuniões | IDs de usuário do Notion | **presença nominal com data** — a melhor fonte de pessoa ativa |
| As 1.153 atas ainda não abertas | base de reuniões | conteúdo — **e varredura de credencial** |
| **Gist** — o chat da plataforma | canal oficial de dúvida de usabilidade | conversa de suporte, por cliente |
| **Grupos de WhatsApp** | fora de qualquer sistema | operação real — a Reserva tem 9 mapeados |

## Governança

### Quem pode alterar este documento
**A § 1, § 2 e § 3 se escrevem a cada varredura**, pelo script. Pendência resolvida **não**
**se apaga: muda de estado**, para o histórico não se perder.

### Quando ler
🔴 **Antes de varrer este cliente. Sempre.** É o que impede repetir busca já feita.

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Cliente:** `Lofty Style` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
