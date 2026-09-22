# Reserva · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o Reserva?" e
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

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🔴 **7 módulos contratados — a conta mais completa da carteira — e NENHUMA etapa do processo atribuída.** | `T2` | **Conta grande não passa pelo funil, ou é lacuna de preenchimento?** |
| 2 | 🔴 **Demanda desta conta vive em `umode.kanbanize.com`, boards 6 e 18** — a página cita **7 cartões por ID**, 2 fechados e 5 abertos. **Nenhuma varredura tocou o Kanbanize.** | `T2` | acesso ao Kanbanize |
| 3 | 🔴 **A cadência declarada de `Review Quinzenal de Projeto` parou de ser cumprida.** Envios marcados até **30/06**; **15/07, 02/08 e 21/08 seguem sem marca**. Responsável declarado: **João**. Destinatária: **Claudinha**. | `T2` | conferência com o atendimento |
| 4 | 🔴 **5 dos 9 grupos de WhatsApp estão marcados para EXCLUIR e continuam existindo.** A própria página traz a decisão 🟢 manter / 🔴 excluir por grupo. | `T2` | execução da limpeza |
| 5 | ⚠ **A página da Reserva NÃO tem o toggle `Pessoas`** que Osklen e NK STORE têm. As pessoas aparecem **soltas, dentro dos nomes de grupo de WhatsApp** — Claudinha (Compras), Raquel (Engenharia/Cadastro), Adriana (Estilo), Bruno (Sourcing), Ju. **Sem cargo formal em lugar nenhum.** | `T2` | preenchimento pelo atendimento |
| 6 | ⚠ **Os únicos dois clientes com `Aposta` e `Planejamento`** são Reserva e VIX (`Aposta`). **São os dois módulos menos vendidos.** | `T2` | — |
| 7 | 🆕 **`uBuy` e `uPlan` aparecem como pauta** (*DE/PARA Campos uBuy*, *Ficha de Pedido uBuy*, *Dados para uPlan*). **`uBuy` não está nos 7 módulos nem nas 16 Soluções** — terceiro cliente em que aparece. | `T2` | decisão sobre o portfólio |
| 8 | ⚠ **Duas visitas presenciais documentadas** (13–14/ago/2024 e 06/06/2025) **e as atas não foram lidas.** | `T2` | tempo de varredura |
| 9 | 🆕 **Projeto `Sourcing` com termo de abertura próprio** — não aparece em nenhuma base. | `T2` | tempo de varredura |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o Reserva

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
| **22 set 2026** | `1be19527…` | **9 grupos de WhatsApp mapeados** com decisão manter/excluir; canal oficial declarado (**formulário** para demanda, **Gist** para dúvida); média declarada de **1 chamado/dia e 2 reuniões/semana**; 🔴 **7 cartões no `umode.kanbanize.com`**; `uBuy` e `uPlan`; **Review Quinzenal** com envios parados; 2 visitas presenciais | ⚠ **não** — 10 sub-páginas e 3 databases inline não abertos |

## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas

| Fonte | Endereço | O que deve trazer |
|---|---|---|
| Relação `Segmentação Grupos` | `collection://a4103fe2-…` | grupo/tier comercial do cliente |
| Relação `Atendimento 2024` | `collection://c82a689c-…` | quem atendeu em 2024 — o corpus só tem 2025 |
| Campo `Participantes` das 1.161 reuniões | IDs de usuário do Notion | **presença nominal com data** — a melhor fonte de pessoa ativa |
| As 1.153 atas ainda não abertas | base de reuniões | conteúdo — **e varredura de credencial** |
| 🔴 **`umode.kanbanize.com`** | boards 6 e 18, cartões por ID | **cartões de demanda de cliente** — fonte inteira jamais tocada |
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

**Cliente:** `Reserva` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
