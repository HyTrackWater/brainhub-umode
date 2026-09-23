# Caedu · Pendências e fontes varridas

> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**
> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**
>
> 🔴 **Este é o único lugar onde se pergunta "o que ainda não sei sobre o Caedu?" e
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

| Onde | Quantos | O que era | Estado |
|---|--:|---|---|
| sub-página `Fornecedores da Caedu` | 1 | desconhecido | 🔴 **aberto** — **404 por este conector.** Único caso de acesso negado de verdade na carteira |

**O contorno que funciona:** pedir ao Vinícius **só aquele trecho**, copiado e colado. **Barato, e o que vier entra como fonte normal, com procedência.**

## 2 · Pendências abertas

| # | O que está em aberto | Tier | O que destrava |
|--:|---|:-:|---|
| 1 | 🔴 **O `Status` diz `Onboarding` e a `Etapa` diz `Ongoing`.** É o único cliente da carteira que está **adiante** do que o `Status` declara. | `T2` | **Qual dos dois manda?** — decisão do Vinicius |
| 2 | 🔴 **A CAEDU mudou de `Ongoing` para `Onboarding` em 22/09/2026 às 15:04**, entre duas leituras minhas no mesmo dia. | `T2` | **Por quê?** — pergunta ao Vinicius |
| 3 | 🔴 **A dor `Griffe › Linha › Grupo/subgrupo` está escrita na weekly de 16/09/2025**, reaparece na visita de jul/2026 e na integração de ago/2026 — **com a mesma frase sobre a API estar do lado do cliente**. Atravessou três ciclos sem destravar. | `T2` | decisão de quem assume a integração |
| 4 | ⚠ **O `Escopo 2` da proposta é confidencial, restrito à diretoria.** Registro que existe e o que é; **não replico o detalhe fora do `_contexto/` deste cliente**. | `T1` | nada — é tratamento, não pendência |
| 5 | ⚠ **Sem acesso à sub-página `Fornecedores da Caedu`** — 404 por este conector. **Não afirmo que não existe: afirmo que não alcancei.** | `T2` | liberação de acesso |
| 6 | ⚠ **~47 atas de weekly não lidas.** O Vinicius pediu para **não gastar esforço nelas agora**: são anotações manuais, e ele vai trazer ~50 transcrições reais. | `T2` | a entrega das transcrições |
| 7 | ⚠ **Não abertas:** `Ficha de Produto` · `Playbooks` · `Miro Regras e restrições` · `Onboarding > Ongoing` · 2 databases inline · `Perfis de Usuario` (synced block). | `T2` | tempo de varredura |

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
| 1 | O `Status` da CAEDU virou `Onboarding` em 22/09/2026 às 15:04, e a base `Etapas do Processo` continua marcando `Ongoing`. **O que mudou nesse dia?** | `T2` | o projeto CAEDU 2.0 está sendo montado sobre a premissa de onboarding | aberta |
| 2 | A dor `Griffe › Linha › Grupo/subgrupo` está escrita desde a weekly de 16/09/2025 e reaparece idêntica em jul e ago/2026. **Quem assume a integração — uMode ou o time tech da CAEDU?** | `T2` | atravessou três ciclos sem destravar | aberta |

## 3 · 🟢 Fontes JÁ varridas — não reabrir

> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a
> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**

### 3.1 · Varridas para a carteira inteira — valem para o Caedu

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
| **22 set 2026** | página `Caedu` no Notion | **56 sub-páginas**; `Reuniões com o cliente` com **~47 atas de weekly** (24/04/2024 → 16/09/2025); `Manual do Cliente para o Sistema PLM` de 2023 | ⚠ **não** — abri 2 das 56 sub-páginas |

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
| **Grupos de WhatsApp** | fora de qualquer sistema | operação real — a Reserva tem 9 mapeados |

## Governança

### Quem pode alterar este documento
**A § 1, § 2 e § 3 se escrevem a cada varredura**, pelo script. Pendência resolvida **não**
**se apaga: muda de estado**, para o histórico não se perder.

### Quando ler
🔴 **Antes de varrer este cliente. Sempre.** É o que impede repetir busca já feita.

## Conexões

> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**

**Cliente:** `Caedu` — [institucional.md](institucional.md) · [jornada.md](jornada.md) · [pessoas.md](pessoas.md)

**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** [`_pendencias-gerais.md`](../../../../00_Institucional/_contexto/_pendencias-gerais.md).

**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)
