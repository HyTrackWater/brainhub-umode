# -*- coding: utf-8 -*-
u"""
gera-pendencias-e-fontes.py - UM arquivo por cliente com (a) toda duvida,
discrepancia e risco daquele cliente e (b) o DIARIO DE BORDO das fontes ja
varridas.

Pedido do Vinicius em 22 set 2026, textual:
  "cliente por cliente voce tenha um local e um arquivo onde defina cada ponto
   que voce tem. Inclusive os de risco de seguranca"
  "preciso que registre todos os locais de onde ja vasculhou pra evitar ficar
   repetindo buscas em clientes e em locais dentro de clientes dos quais ja
   tenha acessado. Isso e perda de tempo e de token."

POR QUE ISSO EXISTE: ate aqui a pendencia de cliente vivia diluida em
`_pendencias-gerais.md` (340 itens, a carteira toda misturada) e a memoria do
que ja foi varrido vivia SO na thread - que compacta. Compactou, repeti busca.
O diario de bordo em disco e o antidoto: e a unica memoria que nao compacta.

TIER DE SENSIBILIDADE: T0/T1/T2, o vocabulario que o Joao ja usa no vault e que
o corpus registra com definicao operacional (item 96 do `_pendencias-gerais.md`):
  T2 = equipe    -> o padrao; tudo que circula internamente
  T1 = restrito  -> valor de proposta, preco, margem, escopo confidencial
  T0 = privado   -> CPF, telefone pessoal, credencial, token
E regra nossa, mais dura que a do vault: conteudo T0 NUNCA entra por valor.
Entra por REFERENCIA - registro que existe e onde, nunca o que e.

Uso:  python scripts/gera-pendencias-e-fontes.py
"""
import io
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")
HOJE = u"22 set 2026"

# ---------------------------------------------------------------------------
# FONTES VARRIDAS PARA A CARTEIRA INTEIRA. Valem para todo cliente: nao
# reabrir. Formato: (fonte, endereco, data, o que saiu, esgotada?)
GLOBAIS = [
    (u"Base `Mapa de Clientes`", u"`collection://ec041afd-…`", u"22 set 2026",
     u"status, módulos, ERP, atendimento, cidade, CNPJ, etapa, receita", u"sim, por SQL"),
    (u"Base `Demandas compartilhadas`", u"`collection://…` (985 linhas)", u"22 set 2026",
     u"demandas, `Quem solicitou?`, datas", u"sim, por SQL"),
    (u"Base `Reuniões Compartilhadas com Clientes`", u"`collection://09a4a94e-…`", u"22 set 2026",
     u"1.161 reuniões, datas, cliente", u"⚠ **não**: campo `Participantes` é ID de usuário, não resolvido"),
    (u"Base `Chamado&Atendimento`", u"`collection://2c5b1d38-…`", u"22 set 2026",
     u"185 chamados, 92 e-mails individuais", u"sim, por SQL"),
    (u"Base `Portal do Cliente`", u"`collection://6548a3ae-…`", u"21 set 2026",
     u"segunda lista de clientes", u"sim, por SQL"),
    (u"Base `Etapas do Processo de Clientes`", u"`collection://348b1d38-…-000bea495254`", u"22 set 2026",
     u"7 etapas; **discorda do campo `Status`**", u"⚠ **não**: as 5 páginas de etapa não foram abertas"),
    (u"Repositório do **CX Hub**", u"leitura de código", u"22 set 2026",
     u"schema e modelo; **não é fonte de dado** — feature nunca finalizada", u"sim"),
    (u"**Google Drive** — pastas de operação", u"varredura de 03 ago 2026", u"03 ago 2026",
     u"16 Soluções, Arquitetura V1, planilha de acessos", u"⚠ **não**"),
]

# FONTES CONHECIDAS E AINDA NAO VARRIDAS, para a carteira inteira.
NAO_VARRIDAS = [
    (u"Relação `Segmentação Grupos`", u"`collection://a4103fe2-…`",
     u"grupo/tier comercial do cliente"),
    (u"Relação `Atendimento 2024`", u"`collection://c82a689c-…`",
     u"quem atendeu em 2024 — o corpus só tem 2025"),
    (u"Campo `Participantes` das 1.161 reuniões", u"IDs de usuário do Notion",
     u"**presença nominal com data** — a melhor fonte de pessoa ativa"),
    (u"As 1.153 atas ainda não abertas", u"base de reuniões",
     u"conteúdo — **e varredura de credencial**"),
    (u"**Gist** — o chat da plataforma", u"canal oficial de dúvida de usabilidade",
     u"conversa de suporte, por cliente"),
    (u"🔴 **`uMode Geral / uFlow / Documentação de Setup - PLM / CLIENTES`**",
     u"segundo acervo de documentação por cliente, fora do `Mapa de Clientes`",
     u"**setup de PLM por cliente** — achado em 22 set 2026, jamais tocado"),
    (u"**As 10 páginas `Perfil de Usuário e Permissionamentos`**",
     u"sub-página de cliente", u"**perfis = áreas do cliente** e a matriz de permissão "
     u"— **2 lidas de 10**"),
    (u"**`Linear`** — gestão de projeto da uMode", u"linear.app/umode",
     u"roadmap e PRDs — há item `offTrack` desde jan/2026"),
    (u"**Grupos de WhatsApp**", u"fora de qualquer sistema",
     u"operação real — a Reserva tem 9 mapeados"),
]

# ---------------------------------------------------------------------------
# POR CLIENTE. Preenchido a cada varredura; o que nao foi varrido fica vazio,
# e o arquivo diz isso com todas as letras em vez de ficar em silencio.
#
# PAGINA: (data, id da pagina, o que saiu, esgotada?)
PAGINA = {
    u"Caedu": (u"22 set 2026", u"página `Caedu` no Notion",
               u"**56 sub-páginas**; `Reuniões com o cliente` com **~47 atas de weekly** "
               u"(24/04/2024 → 16/09/2025); `Manual do Cliente para o Sistema PLM` de 2023",
               u"⚠ **não** — abri 2 das 56 sub-páginas"),
    u"Osklen": (u"22 set 2026", u"`6463bb11…`",
                u"toggle `Pessoas` **vazio**; `uFlow` início fev/2025; **`uBuy: fup`** início "
                u"jan/2026; 11 documentos de implantação citados **sem link**; **pesquisas de CSat**",
                u"sim, a página; ⚠ as sub-páginas de CSat **não**"),
    u"Reserva": (u"22 set 2026", u"`1be19527…`",
                u"**9 grupos de WhatsApp mapeados** com decisão manter/excluir; canal oficial "
                u"declarado (**formulário** para demanda, **Gist** para dúvida); média declarada "
                u"de **1 chamado/dia e 2 reuniões/semana**; 🔴 **7 cartões no `umode.kanbanize.com`**; "
                u"`uBuy` e `uPlan`; **Review Quinzenal** com envios parados; 2 visitas presenciais",
                u"⚠ **não** — 10 sub-páginas e 3 databases inline não abertos"),
    u"Cambos": (u"22 set 2026", u"`d6d48327\u2026`",
               u"\U0001F7E2 **bloco `Pessoas` PREENCHIDO** (5 pessoas com cargo) + "
               u"**Discovery de Sales com 10 perguntas respondidas**: 140 mil pe\u00e7as/m\u00eas, "
               u"20 a 40 fornecedores, ~20 pessoas no desenvolvimento, **nota 6,0** para o "
               u"processo atual, 10% de quebra de entrega; \U0001F534 **fornecem para CAEDU e "
               u"Marisa**; `Trello`, `Banner`, `Totvs Virtual Age`, `Data Lake`",
               u"\u26a0 **n\u00e3o** \u2014 9 sub-p\u00e1ginas e 4 databases inline n\u00e3o abertos"),
    u"NV": (u"22 set 2026", u"`c03ae4ec\u2026`",
           u"\U0001F7E2 **o bloco `Marca:` est\u00e1 PREENCHIDO** \u2014 linha de produ\u00e7\u00e3o, "
           u"segmento, ERP, integra\u00e7\u00e3o ativa, **61 usu\u00e1rios ativos** e **10 departamentos "
           u"engajados**; onboarding em **duas fases**; \U0001F534 **dois documentos sobre "
           u"variante cancelada**; `Realinhamento Demandas`; `Proposta de comunica\u00e7\u00e3o`",
           u"\u26a0 **n\u00e3o** \u2014 11 sub-p\u00e1ginas e 1 database inline n\u00e3o abertos"),
    u"Oficina Reserva": (u"22 set 2026", u"`a27d12dd\u2026`",
                        u"\U0001F7E2 **o mapeamento de dores mais completo da carteira**, "
                        u"escrito pelo Jo\u00e3o no grupo de Sales em **26/06/2024**: cadastro "
                        u"no SAP, depend\u00eancia do time da **AREZZO**, rela\u00e7\u00e3o com a "
                        u"**Qualit\u00e1** por WhatsApp, aus\u00eancia de governan\u00e7a, **400 SKUs "
                        u"por cole\u00e7\u00e3o**, **90% do tempo no SAP**; Kick Off interno 01/07 e "
                        u"com cliente 12/07/2024",
                        u"\u26a0 **n\u00e3o** \u2014 4 sub-p\u00e1ginas e 3 databases inline n\u00e3o abertos"),
    u"Lofty Style": (u"22 set 2026", u"`293c8829\u2026`",
                    u"toggle `Pessoas` **presente e VAZIO**; \U0001F6A8 **a credencial do site "
                    u"de documenta\u00e7\u00e3o est\u00e1 em texto claro na p\u00e1gina**; "
                    u"`Exclus\u00e3o de Variante ap\u00f3s integra\u00e7\u00e3o`; `NCM e C\u00f3digo CEST`; "
                    u"duas `Atualiza\u00e7\u00e3o de Projeto` (12/01 e 29/01/2026); **duas pesquisas "
                    u"de CSat**; documento `As Is`; quadro Miro",
                    u"\u26a0 **n\u00e3o** \u2014 6 sub-p\u00e1ginas e 4 databases inline n\u00e3o abertos"),
    u"Puket": (u"22 set 2026", u"`aae6d54c\u2026`",
              u"\U0001F7E2 **TABELA DE USU\u00c1RIOS com 43 pessoas** \u2014 nome, **e-mail "
              u"corporativo**, **perfil de acesso** e **ativo desde**. \U0001F534 **Dois "
              u"dom\u00ednios**: `@puket.com.br` e `@grupounico.com` (+1 `.hk`); treinamentos "
              u"gravados no **YouTube**; `Passada de bast\u00e3o`; `MAIO 2025 | Evolu\u00e7\u00e3o "
              u"de Conta`; template de Marca com os campos vazios",
              u"\u26a0 **n\u00e3o** \u2014 6 sub-p\u00e1ginas e 2 databases inline n\u00e3o abertos"),
    u"VIX": (u"22 set 2026",
            u"`70a10ec2…` **+ a sub-página `[Vix] Perfil de Usuário e "
            u"Permissionamento`**",
            u"🔴 **17 perfis de usuário nomeados por área** e uma matriz de "
            u"**~60 funções × 17 perfis**; tabela **DE/PARA de integração** "
            u"campo uMode → campo Linx (31/07/2025); `uPick`; "
            u"⚠ **nenhum nome de pessoa**",
            u"⚠ **não** — 5 sub-páginas e 2 databases inline não abertos"),
    u"Luiza Barcelos": (u"22 set 2026",
                       u"`b0c819c0…` **+ a sub-página `Warm Up Cliente` "
                       u"(`21bb3e7e…`)**",
                       u"🟢 **a página de pessoas mais rica da carteira** — "
                       u"**16 pessoas do cliente com cargo**, incluindo a própria "
                       u"**Marcinha (Luiza Barcelos), Diretora Criativa**; a sub-página "
                       u"traz a **ata completa de 07/06/2024** com **6 uModers nomeados com "
                       u"cargo**, expectativa **por pessoa** e 10 áreas envolvidas; "
                       u"🔴 **`Relatório de Incidente` de 08/08/2025**; 8 páginas "
                       u"de regra datadas; `HubSpot`; **13 usuários uFlow + 2 uDash**",
                       u"⚠ **quase** — **17 blocos do toggle `Pessoas` não "
                       u"renderizam neste conector**; 11 sub-páginas não lidas"),
    u"Moda Objetiva": (u"22 set 2026", u"`295b1d38\u2026`",
                      u"\U0001F7E2 **bloco `Pessoas` PREENCHIDO** \u2014 6 pessoas, e um bloco "
                      u"**`Stakeholders` que s\u00f3 esta conta tem**; \U0001F534 **quatro toggles "
                      u"com t\u00edtulo e sem conte\u00fado**; sub-p\u00e1ginas `Dossie Acompanhamento "
                      u"Integra\u00e7\u00e3o` e **`Regras de Neg\u00f3cios da Conta`**",
                      u"\u26a0 **n\u00e3o** \u2014 3 sub-p\u00e1ginas e 2 databases inline n\u00e3o abertos"),
    u"Baw": (u"22 set 2026", u"`6c36c6a4\u2026`",
            u"\U0001F534 **`Negocia\u00e7\u00e3o p\u00f3s AR&CO | 23/01/25`** \u2014 **terceiro cliente "
            u"ligado ao Grupo AR&CO**; \U0001F195 **`[BAW] Contrato 2025`**, primeiro documento "
            u"de contrato nomeado da carteira; **QUATRO** p\u00e1ginas `Perfil de Acesso`, uma "
            u"delas duplicata `(1)`; `Projeto Reciclagem BAW`",
            u"\u26a0 **n\u00e3o** \u2014 8 sub-p\u00e1ginas e 3 databases inline n\u00e3o abertos"),
    u"Loungerie": (u"22 set 2026", u"`345b1d38\u2026`",
                  u"\U0001F534 **A HIERARQUIA DE PRODUTO EM 4 N\u00cdVEIS, COMPLETA E COM "
                  u"EXEMPLOS** \u2014 `Griffe \u203a Linha \u203a Grupo \u203a Subgrupo`, **a mesma dor "
                  u"travada da CAEDU**; 5 discoveries gravados; `Consultoria de Planejamento`; "
                  u"rituais `Ata da Carteira` e `FUP`; tabela fiscal `IMPORTADO LOUNG` com "
                  u"HSCODE; **`Tactiq`**",
                  u"\u26a0 **n\u00e3o** \u2014 1 bloco `alias` n\u00e3o renderizou; 6 planilhas do Drive "
                  u"e 5 grava\u00e7\u00f5es n\u00e3o abertas"),
    u"NK STORE": (u"22 set 2026", u"`0f24dfbe…`",
                  u"**13 pessoas com cargo e área**; processo `Planejamento → Estilo → "
                  u"Compras/Merchandising → PCP → Oficina`; dores mapeadas; **`uBuy`** como "
                  u"oportunidade; 🚨 **credencial de produção em texto claro**",
                  u"⚠ **não** — 1 bloco não abriu (`Plano de Sucesso do Cliente`)"),
}

# PENDENCIAS especificas do cliente: (texto, tier, o que destrava)
PEND = {
    u"Caedu": [
        (u"🔴 **O `Status` diz `Onboarding` e a `Etapa` diz `Ongoing`.** É o único cliente da "
         u"carteira que está **adiante** do que o `Status` declara.", u"T2",
         u"**Qual dos dois manda?** — decisão do Vinicius"),
        (u"🔴 **A CAEDU mudou de `Ongoing` para `Onboarding` em 22/09/2026 às 15:04**, entre duas "
         u"leituras minhas no mesmo dia.", u"T2", u"**Por quê?** — pergunta ao Vinicius"),
        (u"🔴 **A dor `Griffe › Linha › Grupo/subgrupo` está escrita na weekly de 16/09/2025**, "
         u"reaparece na visita de jul/2026 e na integração de ago/2026 — **com a mesma frase sobre "
         u"a API estar do lado do cliente**. Atravessou três ciclos sem destravar.", u"T2",
         u"decisão de quem assume a integração"),
        (u"⚠ **O `Escopo 2` da proposta é confidencial, restrito à diretoria.** Registro que "
         u"existe e o que é; **não replico o detalhe fora do `_contexto/` deste cliente**.", u"T1",
         u"nada — é tratamento, não pendência"),
        (u"⚠ **Sem acesso à sub-página `Fornecedores da Caedu`** — 404 por este conector. "
         u"**Não afirmo que não existe: afirmo que não alcancei.**", u"T2", u"liberação de acesso"),
        (u"⚠ **~47 atas de weekly não lidas.** O Vinicius pediu para **não gastar esforço nelas "
         u"agora**: são anotações manuais, e ele vai trazer ~50 transcrições reais.", u"T2",
         u"a entrega das transcrições"),
        (u"⚠ **Não abertas:** `Ficha de Produto` · `Playbooks` · `Miro Regras e restrições` · "
         u"`Onboarding > Ongoing` · 2 databases inline · `Perfis de Usuario` (synced block).",
         u"T2", u"tempo de varredura"),
    ],
    u"NK STORE": [
        (u"🚨 **Credencial de produção do Linx em TEXTO CLARO** na página do cliente, toggle "
         u"`Documentos › Conexão com Linx`: usuário, senha, IP, porta e nome do banco. "
         u"**O valor não foi replicado em lugar nenhum do corpus.**", u"T0",
         u"🚨 **rotação da chave — ação do Vinicius**"),
        (u"🔴 **CPF e telefone pessoal de dois representantes legais** na mesma página. "
         u"**Nada entrou no corpus** — registro que existe e onde.", u"T0",
         u"nada — é tratamento"),
        (u"🔴 **8 das 13 pessoas com cargo nunca abriram demanda** — incluindo as **duas diretoras "
         u"do projeto** (Regiane Konopka, Merchandising; Stella Sunaga, Estilo).", u"T2",
         u"nada — já corrigido, as fichas existem"),
        (u"⚠ **`Merchandising`, `Curadoria` e `Oficina` são etapas do processo com dono, e não "
         u"existem na grade canônica de 14 áreas.** Aqui **não são apelido.**", u"T2",
         u"decisão sobre a grade de áreas (item 234 — `15_Producao-Interna`)"),
        (u"⚠ **11 das 24 pessoas seguem sem cargo** — as que vieram só da base de demandas e "
         u"não aparecem no toggle `Pessoas` da página.", u"T2",
         u"preenchimento pelo atendimento"),
        (u"🆕 **`uBuy` aparece como oportunidade** (*Follow Up de Entregas → Pedidos de Compras*) "
         u"e **não está nos 7 módulos nem nas 16 Soluções.**", u"T2",
         u"decisão sobre o portfólio"),
    ],
    u"Osklen": [
        (u"🔴 **O toggle `Pessoas` da página está INTEIRAMENTE VAZIO.** Conta em `Operação "
         u"Assistida` **sem uma pessoa nomeada na própria página do cliente.**", u"T2",
         u"preenchimento pelo atendimento"),
        (u"🔴 **O `Status` diz `Operação Assistida` e a `Etapa` diz `Onboarding`.**", u"T2",
         u"**Qual dos dois manda?**"),
        (u"🆕 **`uBuy: fup`** — início **jan/2026**, entrega `+d???`. **Produto vivo fora das duas "
         u"listas** (7 módulos e 16 Soluções).", u"T2", u"decisão sobre o portfólio"),
        (u"⚠ **A data de entrega do uFlow nunca foi cravada:** a própria fonte escreve "
         u"*\"Junho ou Agosto 2025???\"*, com as três interrogações.", u"T2", u"—"),
        (u"⚠ **11 documentos de implantação citados como texto, sem link** — nomeados e "
         u"não endereçáveis.", u"T2", u"—"),
        (u"🆕 **Existe medição de CSat** (`Pesquisa de Satisfação do treinamento`, `Pesquisa "
         u"Satisfação Kick Off Osklen`) e **nunca foi varrida.**", u"T2", u"tempo de varredura"),
        (u"⚠ **Duas páginas com o mesmo nome:** `Integração de Escrita - Plano de Comunicação` "
         u"e `(1)`.", u"T2", u"—"),
    ],
    u"NV": [
        (u"\U0001F7E2 **O bloco `Marca:` est\u00e1 preenchido** \u2014 \u00e9 o mesmo template que "
         u"na Puket est\u00e1 vazio. **Linha de produ\u00e7\u00e3o:** compra de Produto Acabado, "
         u"Importado e **triangula\u00e7\u00e3o de Mat\u00e9ria-prima para Fac\u00e7\u00e3o**. **ERP** Linx, "
         u"**integra\u00e7\u00e3o ativa** em Produtos e Ficha T\u00e9cnica.", u"T2", u"nada \u2014 \u00e9 dado"),
        (u"\U0001F534 **61 usu\u00e1rios ativos declarados, e o corpus tem 13 fichas.** "
         u"**O n\u00famero se sabe; os nomes, n\u00e3o.** \u26a0 **A NV N\u00c3O tem a tabela de "
         u"usu\u00e1rios que a Puket tem.**", u"T2", u"exportar a lista de usu\u00e1rios"),
        (u"\U0001F534 **10 departamentos engajados, e QUATRO n\u00e3o t\u00eam \u00e1rea can\u00f4nica:** "
         u"`Engenharia de Produto`, `Planejamento Comercial`, `Cadastro/Planners`, "
         u"**`Atacado`** e \U0001F534 **`Atelier`**. Os outros: Estilo, PCP, Marketing, "
         u"Compras, Log\u00edstica.", u"T2", u"decis\u00e3o sobre a grade"),
        (u"\U0001F534 **`Atelier` \u00e9 a S\u00c9TIMA evid\u00eancia do `15_Producao-Interna`** "
         u"(item 234) \u2014 depois de `Oficina` na NK STORE e `fac\u00e7\u00e3o` em v\u00e1rios.", u"T2",
         u"decis\u00e3o sobre criar a \u00e1rea"),
        (u"\U0001F534 **QUARTO e QUINTO caso da dor de variante:** `Manual de descancelamento "
         u"de produtos e variantes` e `NV | Variantes Canceladas Inativas`. Com VIX, Reserva "
         u"e Lofty Style s\u00e3o **quatro clientes**. **N\u00e3o \u00e9 mais hip\u00f3tese.**", u"T2",
         u"decis\u00e3o de produto"),
        (u"\u26a0 **Onboarding partido em duas fases documentadas** (`Fase 1`, `Fase 2`) "
         u"mais uma p\u00e1gina `On`. **Nenhum outro cliente tem onboarding faseado assim.**",
         u"T2", u"tempo de varredura"),
        (u"\U0001F195 **`NV | Proposta de comunica\u00e7\u00e3o`** \u2014 segundo cliente com plano de "
         u"comunica\u00e7\u00e3o formal, junto da Osklen (`Integra\u00e7\u00e3o de Escrita`).", u"T2", u"\u2014"),
    ],
    u"Oficina Reserva": [
        (u"\U0001F534 **\u00c9 marca do GRUPO AR&CO e entrou no MESMO PACOTE do grupo** \u2014 o Jo\u00e3o escreveu, em 26/06/2024: *a princ\u00edpio n\u00e3o haver\u00e1 valor adicional, pois "
         u"entrar\u00e3o no mesmo pacote do Grupo*. \U0001F534 **\u00c9 conta separada no corpus e "
         u"contrato do grupo na vida real.**", u"T2", u"decis\u00e3o de modelagem de grupo"),
        (u"\U0001F534 **A dor n\u00famero 1 cita depend\u00eancia do TIME DA AREZZO** \u2014 e a Arezzo "
         u"\u00e9 outra linha da mesma base, em `Pr\u00e9 Onboardings`. **Reserva, Oficina Reserva, "
         u"Simples e Arezzo parecem o mesmo grupo, e o corpus os trata como quatro contas "
         u"isoladas.**", u"T2", u"confirma\u00e7\u00e3o do Vin\u00edcius"),
        (u"\U0001F195 **`Qualit\u00e1` \u2014 um TERCEIRO que n\u00e3o \u00e9 cliente nem fornecedor de "
         u"material: \u00e9 inspe\u00e7\u00e3o de qualidade.** *Processo todo feito pelo WhatsApp*; "
         u"*o inspetor chega para auditar e n\u00e3o tem o documento*. \U0001F534 **O corpus n\u00e3o "
         u"tem modelo para terceiro.**", u"T2", u"decis\u00e3o de modelagem"),
        (u"\U0001F534 **A pr\u00f3pria fonte registra dano reputacional:** *m\u00e1 reputa\u00e7\u00e3o entre "
         u"os Fornecedores e Qualit\u00e1 por n\u00e3o usarem uMode*. **\u00c9 o argumento comercial "
         u"mais forte da carteira, e est\u00e1 enterrado numa mensagem de grupo de 2024.**", u"T2",
         u"\u2014"),
        (u"\U0001F195 **N\u00fameros de opera\u00e7\u00e3o declarados:** **400 SKUs por cole\u00e7\u00e3o**, "
         u"100 cont\u00ednuos, e **90% do tempo dedicado ao SAP**. **Primeiros n\u00fameros de "
         u"opera\u00e7\u00e3o de cliente que o corpus v\u00ea.**", u"T2", u"\u2014"),
        (u"\u26a0 **Meta declarada: rodar no uMode em 6 meses, a contar de jul/2024.** "
         u"**Hoje s\u00e3o 26 meses.** \u26a0 **N\u00e3o sei se a meta foi cumprida** \u2014 nada na "
         u"p\u00e1gina diz.", u"T2", u"confer\u00eancia com o atendimento"),
        (u"\u26a0 **Sem etapa do processo atribu\u00edda** e **ERP `SAP e Linx`**, a mesma coisa "
         u"que `Linx / SAP` escrita de outro jeito.", u"T2", u"limpeza do enum"),
        (u"\u26a0 **`Perfil de Usu\u00e1rio e Permissionamentos OFICINA` n\u00e3o foi aberta.** "
         u"**\u00c9 o terceiro cliente com essa sub-p\u00e1gina** (VIX, Lofty Style, Oficina).", u"T2",
         u"tempo de varredura"),
    ],
    u"Lofty Style": [
        (u"\U0001F6A8 **A credencial do site de documenta\u00e7\u00e3o est\u00e1 EM TEXTO CLARO na "
         u"p\u00e1gina do cliente**, no toggle `Documenta\u00e7\u00e3o/Regras`, ao lado da URL "
         u"`docs.umode.app/integracao-lofty`. **O valor n\u00e3o foi replicado em lugar nenhum.**",
         u"T0", u"\U0001F6A8 **rota\u00e7\u00e3o da chave \u2014 a\u00e7\u00e3o do Vin\u00edcius**"),
        (u"\U0001F534 **O `Status` diz `Ongoing` e a `Etapa` diz `Opera\u00e7\u00e3o Assistida`.**",
         u"T2", u"pergunta registrada"),
        (u"\U0001F534 **O toggle `Pessoas` existe e est\u00e1 VAZIO** \u2014 segundo caso, junto "
         u"da Osklen. **De 3 clientes que t\u00eam o toggle, 1 preencheu.**", u"T2",
         u"preenchimento pelo atendimento"),
        (u"\U0001F534 **TERCEIRO cliente com a dor de excluir/inativar variante** \u2014 a "
         u"p\u00e1gina tem `Exclus\u00e3o de Variante ap\u00f3s integra\u00e7\u00e3o`. Os outros dois: **VIX** "
         u"(aprendizado de permiss\u00e3o) e **Reserva** (cart\u00e3o antigo). "
         u"**Um caso \u00e9 anedota, dois \u00e9 hip\u00f3tese, tr\u00eas \u00e9 PADR\u00c3O.**", u"T2",
         u"decis\u00e3o de produto \u2014 \u00e9 lacuna da plataforma, n\u00e3o do cliente"),
        (u"\u26a0 **Dois arquivos de staging `SUPERSEDED` seguem no reposit\u00f3rio.** "
         u"**Apagar \u00e9 decis\u00e3o sua.**", u"T2", u"decis\u00e3o do Vin\u00edcius (item 257)"),
        (u"\U0001F195 **Duas `Atualiza\u00e7\u00e3o de Projeto`** (12/01/2026 e 29/01/2026) e nada "
         u"depois. \u26a0 **Mesma marca da Reserva**, cuja cad\u00eancia parou em 30/06.", u"T2",
         u"confer\u00eancia com o atendimento"),
        (u"\U0001F195 **Duas pesquisas de CSat** (Kick Off e Treinamento) \u2014 **segundo "
         u"cliente com CSat**, junto da Osklen. **Fonte nunca varrida.**", u"T2",
         u"tempo de varredura"),
        (u"\U0001F195 `NCM e C\u00f3digo CEST` \u2014 **tema fiscal**, que nenhuma \u00e1rea can\u00f4nica "
         u"das 14 cobre com clareza.", u"T2", u"\u2014"),
    ],
    u"Puket": [
        (u"\U0001F7E2 **43 pessoas com nome, e-mail corporativo, perfil de acesso e data de "
         u"ativa\u00e7\u00e3o.** A Puket tinha **3** fichas, vindas s\u00f3 das demandas. "
         u"**\u00c9 a fonte de pessoa mais completa da carteira.**", u"T2", u"nada \u2014 executado"),
        (u"\U0001F534 **Dois dom\u00ednios de e-mail na mesma conta:** `@puket.com.br` e "
         u"`@grupounico.com`, mais um `@grupounico.hk`. **A Puket \u00e9 do Grupo \u00danico, e "
         u"gente do grupo opera dentro da conta do cliente.** \u26a0 **O corpus n\u00e3o tem "
         u"modelo para grupo econ\u00f4mico.**", u"T2", u"decis\u00e3o de modelagem"),
        (u"\U0001F534 **A pessoa mais antiga est\u00e1 ativa desde 24/05/2022 e o campo "
         u"`Data Ativa\u00e7\u00e3o Cliente` da base est\u00e1 VAZIO.** **A tabela de usu\u00e1rios sabe "
         u"o que a base n\u00e3o sabe.**", u"T2", u"preenchimento da base"),
        (u"\u26a0 **Uma pessoa tem o perfil RISCADO na fonte** (`Sarah Nunes`). "
         u"**N\u00e3o afirmo que saiu: afirmo que a fonte riscou.**", u"T2", u"confirma\u00e7\u00e3o"),
        (u"\u26a0 **Dois nomes divergem do pr\u00f3prio e-mail** \u2014 `Isabela Pereira` \u00d7 "
         u"`isabela.cipriani`, `Marcela Polyana` \u00d7 `marcela.figueiredo`. "
         u"**N\u00e3o resolvi:** pode ser nome de casada, apelido ou erro.", u"T2", u"confirma\u00e7\u00e3o"),
        (u"\U0001F534 **12 perfis de acesso que N\u00c3O s\u00e3o as 14 \u00e1reas can\u00f4nicas:** "
         u"`Sourcing Nacional`, `Produto`, `Design`, `BI`, `TEX`, `Estilo`, `Certifica\u00e7\u00e3o`, "
         u"`Qualidade`, `PCP`, `Controladoria`, `Importa\u00e7\u00e3o`, `Projetos`. "
         u"\U0001F534 **`BI`, `TEX`, `Certifica\u00e7\u00e3o`, `Controladoria`, `Importa\u00e7\u00e3o` e "
         u"`Projetos` n\u00e3o t\u00eam \u00e1rea can\u00f4nica.**", u"T2", u"decis\u00e3o sobre a grade"),
        (u"\U0001F195 **Treinamentos gravados em playlist do YouTube** \u2014 primeira "
         u"confirma\u00e7\u00e3o de uso real do canal. **Nunca varrido.**", u"T2", u"tempo"),
        (u"\U0001F195 **`Passada de bast\u00e3o Puket`** \u2014 documento de handover de "
         u"atendimento. **Nenhum outro cliente tem um.**", u"T2", u"tempo de varredura"),
        (u"\u26a0 **O template de `Marca` da p\u00e1gina est\u00e1 com todos os campos vazios** "
         u"(`#`, `##`, `Ex:`). **Mais um template criado e n\u00e3o preenchido.**", u"T2",
         u"preenchimento pelo atendimento"),
        (u"\u26a0 **S\u00f3 2 m\u00f3dulos contratados** \u2014 o menor entre os `Ongoing` \u2014 **e 43 "
         u"usu\u00e1rios ativos.** \u26a0 **Muita gente para pouco m\u00f3dulo**; pode ser "
         u"oportunidade ou erro de cadastro.", u"T2", u"confer\u00eancia"),
        (u"\u26a0 **ERP `Linx / SAP`** \u2014 valor composto, n\u00e3o desmembrado.", u"T2",
         u"confer\u00eancia"),
    ],
    u"Moda Objetiva": [
        (u"🔴 **O `Status` diz `Operação Assistida` e a `Etapa` diz `Onboarding`.**", u"T2",
         u"**Qual dos dois manda?**"),
        (u"⚠ **`Objetiva` na plataforma × `Moda Objetiva` no CRM** — mesmo cliente, confirmado "
         u"pelo Vinicius em 03 ago 2026; registrado como alias.", u"T2", u"nada — resolvido"),
    ],
    u"Loungerie": [
        (u"🔴 **O `Status` diz `Onboarding` e a `Etapa` diz `Pré Onboarding`.**", u"T2",
         u"**Qual dos dois manda?**"),
        (u"⚠ **Campo `Módulos Contratados` vazio** e status de onboarding ativo.", u"T2",
         u"preenchimento"),
    ],
    u"Baw": [
        (u"\U0001F534 **`Negocia\u00e7\u00e3o p\u00f3s AR&CO | 23/01/25`** \u2014 **a Baw \u00e9 o "
         u"TERCEIRO cliente ligado ao Grupo AR&CO**, com Reserva e Oficina Reserva (e Arezzo "
         u"citada na dor da Oficina). \u26a0 **Pode explicar por que est\u00e1 `Sem CS` com 4 "
         u"m\u00f3dulos: entrou pelo pacote do grupo.**", u"T2", u"confirma\u00e7\u00e3o do Vin\u00edcius"),
        (u"\U0001F195 **`[BAW] Contrato 2025`** \u2014 **primeiro documento de contrato nomeado "
         u"da carteira.** \U0001F534 **N\u00e3o abri, e quando abrir o conte\u00fado \u00e9 `T1`.**",
         u"T1", u"tempo de varredura"),
        (u"\U0001F534 **Tem o m\u00f3dulo `Integra\u00e7\u00e3o` contratado e o ERP diz `Sem "
         u"Integra\u00e7\u00e3o`.** Os dois n\u00e3o podem estar certos.", u"T2",
         u"pergunta registrada"),
        (u"\u26a0 **QUATRO p\u00e1ginas `Perfil de Acesso - BAW`**, uma delas duplicata expl\u00edcita "
         u"`(1)`, e duas por \u00e1rea (`Estilo`, `Engenharia/Compras`). **Mesmo padr\u00e3o de "
         u"duplicata `(1)` da Osklen.**", u"T2", u"limpeza"),
        (u"\U0001F195 **`Projeto Reciclagem BAW`** \u2014 projeto pr\u00f3prio, fora de qualquer "
         u"base.", u"T2", u"tempo de varredura"),
        (u"\u26a0 **Sem bloco `Pessoas` e sem etapa do processo.** O corpus tem 3 fichas, "
         u"todas da base de demandas, **sem cargo**.", u"T2", u"preenchimento"),
    ],
    u"Loungerie": [
        (u"\U0001F534 **A P\u00c1GINA TRAZ A HIERARQUIA DE PRODUTO COMPLETA, EM 4 N\u00cdVEIS, "
         u"COM EXEMPLOS:** `1\u00ba GRIFFE` (ocasi\u00e3o de uso) \u203a `2\u00ba LINHA` (categoria) \u203a "
         u"`3\u00ba GRUPO` (tipo) \u203a `4\u00ba SUBGRUPO` (modelagem/silhueta). "
         u"\U0001F534 **\u00c9 EXATAMENTE `Griffe \u203a Linha \u203a Grupo/subgrupo`, a dor da CAEDU "
         u"que atravessou tr\u00eas ciclos sem destravar** \u2014 e aqui est\u00e1 resolvida, **com "
         u"alternativa sugerida pela pr\u00f3pria uMode** para o caso de categoria nova.", u"T2",
         u"\U0001F534 **levar para a CAEDU** \u2014 decis\u00e3o sua"),
        (u"\U0001F195 **`Consultoria de Planejamento`** \u2014 **\u00e9 SERVI\u00c7O, n\u00e3o m\u00f3dulo**, e "
         u"n\u00e3o est\u00e1 nos 7 m\u00f3dulos nem nas 16 Solu\u00e7\u00f5es. **Sexto nome de oferta fora "
         u"das listas**, com `uBuy`, `uPlan`, `uPick`, `IPSP` e `uDash`.", u"T2",
         u"decis\u00e3o sobre o portf\u00f3lio"),
        (u"\U0001F195 **5 discoveries gravados**, todos com link: `Linx`, `Planejamento e "
         u"Compras`, `Intelig\u00eancia Comercial`, `Estilo`, mais **2 Agendas de Mapa de "
         u"Assuntos feitas ANTES do fechamento do contrato**. \U0001F534 **\u00c9 o acervo de "
         u"grava\u00e7\u00e3o mais organizado da carteira, e nenhuma foi ouvida.**", u"T2",
         u"tempo \u2014 e h\u00e1 transcri\u00e7\u00e3o Tactiq de pelo menos uma"),
        (u"\U0001F195 **`Tactiq` \u2014 d\u00e9cima primeira ferramenta**, com link de transcri\u00e7\u00e3o "
         u"vivo. **\u00c9 a mesma ferramenta das 7 transcri\u00e7\u00f5es da CAEDU** que voc\u00ea "
         u"entregou \u2014 e ela tem hist\u00f3rico pr\u00f3prio, fora do Notion.", u"T2",
         u"acesso ao Tactiq"),
        (u"\U0001F195 **Dois rituais de opera\u00e7\u00e3o descritos em detalhe:** `Ata da Carteira` "
         u"(Compras + Planejamento + Aloca\u00e7\u00e3o + Log\u00edstica, pedido a pedido, revendo data "
         u"de lan\u00e7amento) e `FUP` (Time & Action com fornecedor: amostra, aprova\u00e7\u00e3o de "
         u"cor, 1\u00ba fit, 2\u00ba fit, PP, pe\u00e7a de marketing). **S\u00e3o os rituais de cliente "
         u"mais bem descritos do corpus.**", u"T2", u"\u2014"),
        (u"\U0001F534 **`Aloca\u00e7\u00e3o` e `Intelig\u00eancia Comercial` n\u00e3o existem na grade de "
         u"14 \u00e1reas.** Somam-se a Merchandising, Curadoria, Oficina, Atelier, BI, TEX, "
         u"Certifica\u00e7\u00e3o, Controladoria, Importa\u00e7\u00e3o, Projetos e Atacado.", u"T2",
         u"decis\u00e3o sobre a grade"),
        (u"\U0001F195 **`IMPORTADO LOUNG` \u2014 tabela de classifica\u00e7\u00e3o fiscal** com "
         u"**HSCODE**, composi\u00e7\u00e3o e medidas. **Segundo tema fiscal da carteira**, depois "
         u"do `NCM e C\u00f3digo CEST` da Lofty Style. **Dois casos: \u00e9 hip\u00f3tese.**", u"T2",
         u"\u2014"),
        (u"\u26a0 **Datas de opera\u00e7\u00e3o declaradas:** desenvolvimento concentrado no "
         u"**2\u00ba sem/2027**, importados com abastecimento at\u00e9 **abril/2027**. "
         u"**\u00c9 o \u00fanico cliente com horizonte de cole\u00e7\u00e3o declarado.**", u"T2", u"\u2014"),
        (u"\U0001F534 **O `Status` diz `Onboarding` e a `Etapa` diz `Pr\u00e9 Onboarding`** \u2014 "
         u"e o campo `M\u00f3dulos Contratados` est\u00e1 **vazio**, apesar do discovery avan\u00e7ado "
         u"e de haver contrato fechado (a fonte cita *antes do fechamento do contrato*).",
         u"T2", u"confer\u00eancia com o comercial"),
    ],
    u"VIX": [
        (u"🔴 **A VIX tem 17 perfis de usuário, e eles SÃO áreas** — "
         u"`Vix-Admin`, `Vix-CAD`, `Vix-Compras`, `Vix-Desenvolvimento`, `Vix-Estamparia`, "
         u"`Vix-PCP`, `Vix-Ficha Tecnica`, `Vix-Produto TP`, `Vix-Tabela`, `Vix-Qualidade`, "
         u"`Vix-Demo`, `uDash` **e CINCO de Estilo**: Biquini, Cover ups, PA, Roupas, Admin. "
         u"**Confirma perfil = área, com granularidade de SUBÁREA.**", u"T2",
         u"decisão sobre mapear perfil para subárea canônica"),
        (u"🔴 **`Manual` e `Base de Importação` estão bloqueados para os 17 "
         u"perfis** — **ninguém na VIX acessa o manual.** ⚠ **Conecta com a dor da "
         u"CAEDU**, que diz que o manual não foi suficiente.", u"T2", u"decisão de produto"),
        (u"🔴 **A matriz de ~60 funções × 17 perfis é mantida À MÃO "
         u"numa tabela do Notion.** Última edição: **09/07/2025**. ⚠ **Não sei "
         u"se ainda reflete a plataforma.**", u"T2", u"conferência contra o banco"),
        (u"🆕 **`uPick`** — sub-página `uPick Vix - Passo a passo`. **Mais um "
         u"nome de produto fora dos 7 módulos e das 16 Soluções**, junto de `uBuy` "
         u"e `uPlan`.", u"T2", u"decisão sobre o portfólio"),
        (u"⚠ **`uDash` aparece como PERFIL de usuário nesta matriz**, e também é "
         u"nome de produto legado. **Dois sentidos para a mesma palavra** — mesma armadilha "
         u"do `collection` do banco contra coleção de moda.", u"T2", u"desambiguação"),
        (u"🆕 **A página registra um aprendizado de atendimento:** usuário sem "
         u"permissão de deletar variante deve pedir a quem tem, **internamente**. "
         u"⚠ **Explica uma classe inteira de demanda.**", u"T2", u"—"),
        (u"🆕 **Tabela DE/PARA de integração (31/07/2025):** campo uMode para "
         u"campo Linx, com tabela e tipo (`referenciabr` para `MODELISTA` em `PRODUTOS`). "
         u"**É o primeiro mapeamento de integração campo a campo que o corpus vê.**",
         u"T2", u"vale replicar como padrão de documentação de integração"),
        (u"⚠ **Nenhum nome de pessoa na página nem na sub-página de perfis.** As 6 "
         u"fichas da VIX seguem vindo só da base de demandas, **sem cargo**.", u"T2",
         u"a página não tem essa informação — depende de outra fonte"),
    ],
    u"Reserva": [
        (u"🔴 **7 módulos contratados — a conta mais completa da carteira — e NENHUMA etapa do "
         u"processo atribuída.**", u"T2",
         u"**Conta grande não passa pelo funil, ou é lacuna de preenchimento?**"),
        (u"🟢 **FECHADA — o Kanbanize não se varre.** A página cita "
         u"`umode.kanbanize.com`, boards 6 e 18, com 7 cartões por ID. **Vinícius em 22 set "
         u"2026:** *\"ferramenta que não é usada há tempos. Então zero foco nisso.\"* `[D]` "
         u"⚠ **Consequência: a página da Reserva está desatualizada nesse ponto.**",
         u"T2", u"nada — decidido"),
        (u"🔴 **A cadência declarada de `Review Quinzenal de Projeto` parou de ser cumprida.** "
         u"Envios marcados até **30/06**; **15/07, 02/08 e 21/08 seguem sem marca**. "
         u"Responsável declarado: **João**. Destinatária: **Claudinha**.", u"T2",
         u"conferência com o atendimento"),
        (u"🔴 **5 dos 9 grupos de WhatsApp estão marcados para EXCLUIR e continuam existindo.** "
         u"A própria página traz a decisão 🟢 manter / 🔴 excluir por grupo.", u"T2",
         u"execução da limpeza"),
        (u"⚠ **A página da Reserva NÃO tem o toggle `Pessoas`** que Osklen e NK STORE têm. "
         u"As pessoas aparecem **soltas, dentro dos nomes de grupo de WhatsApp** — Claudinha "
         u"(Compras), Raquel (Engenharia/Cadastro), Adriana (Estilo), Bruno (Sourcing), Ju. "
         u"**Sem cargo formal em lugar nenhum.**", u"T2", u"preenchimento pelo atendimento"),
        (u"⚠ **Os únicos dois clientes com `Aposta` e `Planejamento`** são Reserva e VIX "
         u"(`Aposta`). **São os dois módulos menos vendidos.**", u"T2", u"—"),
        (u"🆕 **`uBuy` e `uPlan` aparecem como pauta** (*DE/PARA Campos uBuy*, *Ficha de "
         u"Pedido uBuy*, *Dados para uPlan*). **`uBuy` não está nos 7 módulos nem nas 16 "
         u"Soluções** — terceiro cliente em que aparece.", u"T2", u"decisão sobre o portfólio"),
        (u"⚠ **Duas visitas presenciais documentadas** (13–14/ago/2024 e 06/06/2025) **e as "
         u"atas não foram lidas.**", u"T2", u"tempo de varredura"),
        (u"🆕 **Projeto `Sourcing` com termo de abertura próprio** — não aparece em "
         u"nenhuma base.", u"T2", u"tempo de varredura"),
    ],
    u"Cambos": [
        (u"\U0001F7E2 **Bloco `Pessoas` PREENCHIDO \u2014 segundo caso da carteira**, junto da "
         u"NK STORE. 5 pessoas com cargo: Tony Stefan Lopes (Gerente Geral/Diretor de "
         u"Opera\u00e7\u00e3o da F\u00e1brica), Valter (Head Financeiro), Fabiane Sayuri (Desenv. de "
         u"Produtos), Carolina (Estilista), Gustavo Paiva (Head de Tecnologia).", u"T2",
         u"nada \u2014 executado"),
        (u"\U0001F7E2 **RESOLVIDA a ambiguidade `Fabi e Carol`** \u2014 a c\u00e9lula da base de "
         u"demandas que eu me recusei a desmembrar. A p\u00e1gina diz que o l\u00edder do projeto "
         u"\u00e9 *Tony e Fabi*, e lista **Fabiane Sayuri** e **Carolina**. "
         u"**Ambiguidade resolvida com fonte, n\u00e3o com palpite.**", u"T2", u"nada"),
        (u"\U0001F534 **A Cambos FORNECE para a CAEDU** \u2014 e as duas s\u00e3o clientes da "
         u"uMode. *Fornecem para Caedu, Marisa, etc.* **Dois clientes nossos numa rela\u00e7\u00e3o "
         u"fornecedor-cliente entre si, e o corpus os trata como ilhas.**", u"T2",
         u"decis\u00e3o de modelagem \u2014 o isolamento de cliente \u00e9 regra travada"),
        (u"\U0001F534 **A base diz ERP `SPI - Sistema pr\u00f3prio da Cambos` e a p\u00e1gina diz "
         u"DOIS:** `Totvs - Virtual Age` (comercial, **com pacote de APIs**) e `SPI` "
         u"(produ\u00e7\u00e3o). Mais `Banner` para pedido de atacado. **A base est\u00e1 incompleta.**",
         u"T2", u"corre\u00e7\u00e3o na base"),
        (u"\U0001F534 **Rela\u00e7\u00e3o contratual amb\u00edgua, registrada pela pr\u00f3pria uMode:** "
         u"*Relat\u00f3rios: n\u00e3o detalhados no contrato por\u00e9m subentendido entre 2-3 "
         u"relat\u00f3rios mediante a maturidade*. **Escopo subentendido \u00e9 escopo em disputa.**",
         u"T2", u"confer\u00eancia com o comercial"),
        (u"\U0001F534 **Atrito interno Sales\u00d7Ops registrado**, feedback do Sandro: *alinhar "
         u"o que vendeu e o que opera\u00e7\u00e3o vai tocar gerou desconforto... pode dar "
         u"impress\u00e3o que a empresa est\u00e1 desalinhada*. **\u00c9 o \u00fanico registro de atrito "
         u"interno que o corpus tem.**", u"T2", u"\u2014"),
        (u"\U0001F195 **N\u00fameros de opera\u00e7\u00e3o:** 140.000 pe\u00e7as/m\u00eas \u00b7 20 a 40 "
         u"fornecedores \u00b7 ~20 pessoas no desenvolvimento \u00b7 **nota 6,0** para o processo "
         u"atual \u00b7 **10% de quebra de entrega** \u00b7 40% Magazine / 60% marca pr\u00f3pria. "
         u"**Segundo cliente com n\u00fameros**, depois da Oficina Reserva.", u"T2", u"\u2014"),
        (u"\u26a0 **~20 pessoas no desenvolvimento e o corpus tem 5 fichas.**", u"T2",
         u"a p\u00e1gina nomeia 5; as outras 15 n\u00e3o est\u00e3o em fonte nenhuma"),
        (u"\U0001F195 **`Trello` \u2014 oitava ferramenta**, usada pelo cliente para gest\u00e3o do "
         u"processo. N\u00e3o est\u00e1 no enum `tool` do corpus.", u"T2", u"\u2014"),
        (u"\U0001F195 **`IPSP`** aparece junto de `uPlan` como oportunidade. **Quinto nome de "
         u"produto fora das duas listas**, com `uBuy`, `uPlan` e `uPick`.", u"T2",
         u"decis\u00e3o sobre o portf\u00f3lio"),
        (u"\U0001F195 **Segundo escopo desejado e N\u00c3O contratado:** *trazer os clientes "
         u"para dentro da plataforma para acompanhar o desenvolvimento*. "
         u"**\u00c9 oportunidade comercial nomeada, parada desde o kick off.**", u"T2", u"\u2014"),
        (u"\U0001F195 **`Playbook Cambos | Treinamento > IA + Doc Laura`** \u2014 primeira "
         u"documenta\u00e7\u00e3o homologada com IA que o corpus v\u00ea.", u"T2", u"tempo de varredura"),
        (u"\u26a0 **Duas contas na plataforma:** `Cambos` (7 usu\u00e1rios) e `Cambos - uFlow` "
         u"(25). **\u00c9 conta por m\u00f3dulo ou duplicidade?**", u"T2", u"pergunta registrada"),
        (u"\u26a0 **Conte\u00fado T1 com autoriza\u00e7\u00e3o de uso pendente desde julho.**", u"T1",
         u"autoriza\u00e7\u00e3o do Vin\u00edcius"),
        (u"\U0001F534 **A fonte traz telefone e CPF de um diretor.** **Nada entrou no corpus** "
         u"\u2014 registro que existe e onde.", u"T0", u"nada \u2014 \u00e9 tratamento"),
    ],
    u"Mondepars": [
        (u"🟢 **FECHADA — o nome certo é `Mondepars`.** Vinícius em "
         u"22 set 2026: *o nome certo da empresa é Mondepars* `[D]` A pasta foi "
         u"**renomeada** de `Mondpars` para `Mondepars`. ⚠ **O CRM segue com a grafia "
         u"errada** — quem ler lá vai achar `Mondpars`.", u"T2", u"correção no CRM"),
    ],
    u"Simples (by Reserva)": [
        (u"🟢 **FECHADA — NÃO É CLIENTE.** Vinícius em 22 set 2026: "
         u"*é marca de dentro da Reserva; a nível de contratação é RESERVA "
         u"mesmo* `[D]` **A carteira tem 48 clientes, não 49.**", u"T2", u"nada — decidido"),
        (u"⚠ **Único ponto em aberto:** ele suspeita que a marca possa ter "
         u"**separação própria de usuários e permissões** na plataforma, ainda que "
         u"a contratação seja da Reserva.", u"T2",
         u"leitura da planilha de acessos (60 contas de organização)"),
        (u"🔴 **Apagar ou fundir esta pasta com a da Reserva é decisão sua.** "
         u"Enquanto não decidir, ela fica — **eu não apago pasta de cliente.**", u"T2",
         u"sua decisão"),
    ],
    u"Estrela": [
        (u"⚠ **`Lojas Estrela` na plataforma × `Estrela` no CRM** — não colapsa sozinho, "
         u"precisa de alias.", u"T2", u"conferência"),
    ],
    u"Puket": [
        (u"⚠ **Só 2 módulos contratados** (`Gestão de Coleção`, `Integração`) — o menor entre os "
         u"`Ongoing`.", u"T2", u"—"),
        (u"⚠ **ERP `Linx / SAP`** — valor composto. **Não desmembrei em dois vínculos:** a fonte "
         u"não diz se usa os dois ou um para cada coisa.", u"T2", u"conferência"),
    ],
    u"Oficina Reserva": [
        (u"⚠ **ERP `SAP e Linx`** — mesma coisa que o `Linx / SAP` da Reserva/Puket, **escrita de "
         u"outro jeito.** Defeito de enum.", u"T2", u"limpeza do enum"),
        (u"⚠ **Sem etapa do processo atribuída.**", u"T2", u"preenchimento"),
    ],
    u"Arezzo": [
        (u"⚠ **ERP `SAP e Linx` e `Pré Onboardings`, sem módulo contratado.**", u"T2", u"—"),
    ],
    u"Hering": [
        (u"⚠ **ERP `Ilimitar`** — não estava no corpus antes de 03 ago 2026.", u"T2", u"—"),
    ],
    u"Highstil": [
        (u"⚠ **`Churn` com atendente nomeado em 2025 e linha editada em 22/09/2026.**", u"T2",
         u"confirmado pelo Vinicius: **foi churn mesmo** (corte de gastos)"),
        (u"⚠ **Ativação em 11/02/2025** — coorte de fev/2025 com Recco e Lenny.", u"T2", u"—"),
    ],
    u"Lenny Niemeyer": [
        (u"⚠ **`Churn` confirmado pelo Vinicius.** Ativação em 03/02/2025 — **~14 meses de "
         u"relação**, não 8 como a Recco.", u"T2", u"nada — resolvido"),
    ],
    u"Plie": [
        (u"⚠ **`Churn` com atendente nomeado em 2025.** Vinicius: mesmo grupo da Highstil, "
         u"corte de gastos.", u"T2", u"nada — resolvido"),
    ],
    u"Recco": [
        (u"⚠ **Ativação em 06/02/2025 e churn** — **~8 meses**, o mais curto da coorte. "
         u"🔺 **Correção registrada: eu tinha dito que as três eram equivalentes. Não são.**",
         u"T2", u"nada — corrigido"),
    ],
    u"Vivara": [
        (u"⚠ **`Churn` com 1 módulo e ERP `SAP`.**", u"T2", u"—"),
    ],
    u"Luiza Barcelos": [
        (u"\U0001F53A **CORRE\u00c7\u00c3O REGISTRADA: eu disse que a conta era quase invis\u00edvel. "
         u"\u00c9 a MAIS bem documentada que abri.** Eu media pela base de chamados, janela de "
         u"24 dias. **A p\u00e1gina tem 15 pessoas com cargo, discovery de Sales, 8 p\u00e1ginas de "
         u"regra datadas e um relat\u00f3rio de incidente.**", u"T2", u"nada \u2014 corrigido"),
        (u"\U0001F534 **O processo est\u00e1 na cabe\u00e7a de UMA pessoa, e a pr\u00f3pria uMode "
         u"escreveu isso:** *o processo est\u00e1 na cabe\u00e7a da Marcinha \u2014 a miss\u00e3o \u00e9 tirar "
         u"as informa\u00e7\u00f5es da cabe\u00e7a dela e colocar na ferramenta*. **\u00c9 risco de "
         u"pessoa-chave nomeado, e a pessoa \u00e9 a dona da marca.**", u"T2", u"\u2014"),
        (u"\U0001F534 **`6 PRIMEIROS MESES PARA MOSTRAR CREDIBILIDADE DA UMODE`** \u2014 em "
         u"vermelho, no kick off interno de **06/06/2024**. E: *o time da Luiza tem trauma de "
         u"cronograma e entrega por frustra\u00e7\u00f5es passadas com a Linx*. "
         u"**Hoje s\u00e3o 27 meses.**", u"T2", u"confer\u00eancia com o atendimento"),
        (u"\U0001F534 **DUAS datas de ativa\u00e7\u00e3o que n\u00e3o batem:** a p\u00e1gina diz "
         u"*Data de Ativa\u00e7\u00e3o por Vendas \u2014 15/05/24* e o campo da base diz **07/06/2024**. "
         u"**Um m\u00eas de diferen\u00e7a, e ningu\u00e9m sabe qual \u00e9 a boa.**", u"T2", u"confer\u00eancia"),
        (u"\U0001F534 **`Relat\u00f3rio de Incidente | Weekly Luiza Barcelos <> uMode \u2014 "
         u"2025/08/08`.** **\u00c9 o \u00fanico registro de incidente com cliente que o corpus "
         u"conhece, e eu n\u00e3o o abri.**", u"T2", u"tempo de varredura \u2014 prioridade"),
        (u"\U0001F7E2 **Escopo contratual EXPL\u00cdCITO, ao contr\u00e1rio da Cambos:** *n\u00e3o faz "
         u"parte do escopo deste contrato a integra\u00e7\u00e3o com o sistema LINX ou qualquer outro "
         u"que n\u00e3o seja o SAFETECH*, e **tr\u00eas relat\u00f3rios nomeados** \u2014 grade, status e "
         u"acompanhamento. **\u00c9 o modelo de como escrever escopo.**", u"T2", u"\u2014"),
        (u"\U0001F534 **`uDash` \u00e9 PRODUTO CONTRATADO aqui** \u2014 *13 usu\u00e1rios uFlow / 2 "
         u"usu\u00e1rios uDash*. Na VIX ele aparecia como **perfil de acesso**. "
         u"**Confirma os dois sentidos da mesma palavra.**", u"T2", u"desambigua\u00e7\u00e3o"),
        (u"\U0001F534 **Duas listas de times que n\u00e3o batem:** o kick off interno diz "
         u"*Estilo, PCP, Compras*; a se\u00e7\u00e3o `Times Envolvidos` diz **oito**: Diretoria "
         u"Criativa, Estilo, Desenvolvimento, Produto e Merchandising, Suprimentos, Opera\u00e7\u00f5es "
         u"(Cadastro e Precifica\u00e7\u00e3o), Estrat\u00e9gia/Processos/Projetos e Tecnologia.", u"T2",
         u"confer\u00eancia"),
        (u"\U0001F195 **`HubSpot` \u2014 d\u00e9cima ferramenta**, e \u00e9 o CRM da uMode: h\u00e1 link "
         u"direto para o *deal* desta conta. **N\u00e3o estava no enum `tool`.**", u"T2", u"\u2014"),
        (u"\U0001F195 **8 p\u00e1ginas de regra datadas** \u2014 `Regra do Campo Linha`, `Regra "
         u"Fam\u00edlia 05/08/25`, `Automa\u00e7\u00f5es da Aba Etapa & Datas 24/09/2025`, `Regras do "
         u"WorkFlow 12/11`, `Importa\u00e7\u00e3o das Listas 24/01`. **\u00c9 a documenta\u00e7\u00e3o de "
         u"regra mais disciplinada da carteira.**", u"T2", u"tempo de varredura"),
        (u"\u26a0 **Dois nomes n\u00e3o batem com o pr\u00f3prio e-mail ou consigo mesmos:** "
         u"`Gabriel Jaques` \u00d7 `gabriel.silva@`, e `Eduardo Britto` \u00d7 `Eduardo Brito` **na "
         u"mesma p\u00e1gina**. **N\u00e3o escolhi nenhuma.**", u"T2", u"confirma\u00e7\u00e3o"),
        (u"\U0001F534 **18 blocos da p\u00e1gina n\u00e3o abriram por este conector** \u2014 "
         u"est\u00e3o justamente dentro de `Diretores e Representantes Legais` e `Respons\u00e1veis "
         u"pelo Projeto`. **H\u00e1 mais pessoas ali do que as 15 que consegui ler.**", u"T2",
         u"leitura manual ou outro conector"),
        (u"\u26a0 **Receita anual declarada na base.** \U0001F534 **N\u00e3o replico o valor "
         u"aqui** \u2014 `T1`, fica no `_contexto/` deste cliente.", u"T1", u"nada \u2014 tratamento"),
        (u"\u26a0 **ERP `Safe Tech`** \u2014 \u00fanico cliente da carteira que o usa.", u"T2", u"\u2014"),
    ],
}

# RISCO DE SEGURANCA, separado por peso proprio: (o que, onde, estado)
# BLOCO QUE O CONECTOR NAO RENDERIZA. Pedido do Vinicius em 22 set 2026:
# "sobre suspeitas de blocos, sempre tenha atencao e me indique, porque temos que
# ter a garantia de que tudo que esta varrendo esta conseguindo tirar proveito de
# tudo o que podemos". Formato: cliente -> [(onde, quantos, o que era, estado)]
NAO_RENDERIZOU = {
    u"Luiza Barcelos": [
        (u"`Warm Up Cliente` › `Pessoas` › `Diretores e Representantes Legais`", 4,
         u"linhas de contato de **Luiz Raul Aleixo Barcelos**",
         u"🟢 **resolvido** — o Vinícius copiou e colou em 22 set 2026"),
        (u"`Warm Up Cliente` › `Pessoas` › `Responsável pelo Financeiro`", 2,
         u"e-mail e telefone da Ana Lucia Andrade",
         u"🟢 **resolvido** — copiado e colado"),
        (u"`Warm Up Cliente` › `Pessoas` › `Responsáveis pelo Projeto`", 8,
         u"contatos e cargos de Gustavo Sobrinho e Gabriel Jaques da Silva",
         u"🟢 **resolvido** — copiado e colado"),
        (u"`Warm Up Cliente` › `Pessoas` › `Responsável Tecnologia`", 3,
         u"contatos e o cargo de **Samuel Correa**",
         u"🟢 **resolvido** — copiado e colado"),
        (u"`Plano de Sucesso do Cliente`", 1, u"incorporação do Google Drive",
         u"🔴 **aberto** — não é Notion, é arquivo do Drive"),
    ],
    u"NK STORE": [
        (u"`Plano de Sucesso do Cliente`", 1, u"incorporação do Google Drive",
         u"🔴 **aberto** — não é Notion, é arquivo do Drive"),
    ],
    u"Cambos": [
        (u"`Plano de Sucesso do Cliente`", 1, u"incorporação do Google Drive",
         u"🔴 **aberto** — não é Notion, é arquivo do Drive"),
    ],
    u"Caedu": [
        (u"sub-página `Fornecedores da Caedu`", 1, u"desconhecido",
         u"🔴 **aberto** — **404 por este conector.** Único caso de acesso "
         u"negado de verdade na carteira"),
    ],
}

RISCO = {
    u"NK STORE": [(u"Credencial de produção do **Linx** (usuário, senha, IP, porta, banco)",
                   u"Notion — página do cliente, toggle `Documentos › Conexão com Linx`",
                   u"🚨 **exposta, não rotacionada**")],
    u"Lofty Style": [(u"Credencial do **site de documentação**",
                      u"Notion \u2014 p\u00e1gina do cliente, toggle `Documenta\u00e7\u00e3o/Regras`, ao lado da URL `docs.umode.app/integracao-lofty`",
                      u"🚨 **exposta, não rotacionada**")],
}


# ---------------------------------------------------------------------------
# PERGUNTAS AO VINICIUS, por cliente. E a fila que vira a lista consolidada.
#
# Uma pergunta so entra aqui quando NENHUMA fonte pode respondê-la: nao e duvida
# que se tira lendo, e decisao ou conhecimento que so ele tem. Duvida que uma
# fonte responde nao e pergunta - e varredura que falta fazer.
#
# Formato: cliente -> [(pergunta, tier, por que importa, estado)]
# Estado: "aberta" | "respondida em <data> por <fonte>"
PERGUNTAS = {
    u"Caedu": [
        (u"O `Status` da CAEDU virou `Onboarding` em 22/09/2026 \u00e0s 15:04, e a base "
         u"`Etapas do Processo` continua marcando `Ongoing`. **O que mudou nesse dia?**",
         u"T2", u"o projeto CAEDU 2.0 est\u00e1 sendo montado sobre a premissa de onboarding",
         u"aberta"),
        (u"A dor `Griffe \u203a Linha \u203a Grupo/subgrupo` est\u00e1 escrita desde a weekly de "
         u"16/09/2025 e reaparece id\u00eantica em jul e ago/2026. **Quem assume a integra\u00e7\u00e3o "
         u"\u2014 uMode ou o time tech da CAEDU?**", u"T2",
         u"atravessou tr\u00eas ciclos sem destravar", u"aberta"),
    ],
    u"Osklen": [
        (u"O `Status` diz `Opera\u00e7\u00e3o Assistida` e a `Etapa` diz `Onboarding`. **Qual "
         u"descreve a conta hoje?**", u"T2", u"muda a leitura de maturidade da conta", u"aberta"),
        (u"O toggle `Pessoas` da p\u00e1gina est\u00e1 vazio. **Quem s\u00e3o a diretoria e os l\u00edderes "
         u"de departamento da Osklen?**", u"T2",
         u"sem isso a conta n\u00e3o tem uma pessoa nomeada na pr\u00f3pria p\u00e1gina", u"aberta"),
    ],
    u"NK STORE": [
        (u"\U0001F6A8 **A credencial de produ\u00e7\u00e3o do Linx est\u00e1 em texto claro na p\u00e1gina do "
         u"cliente. Foi rotacionada?**", u"T0", u"exposi\u00e7\u00e3o ativa at\u00e9 prova em contr\u00e1rio",
         u"aberta"),
        (u"`Merchandising`, `Curadoria` e `Oficina` s\u00e3o etapas do processo com dono e n\u00e3o "
         u"existem na grade de 14 \u00e1reas. **Viram \u00e1rea can\u00f4nica, sub\u00e1rea, ou apelido?**",
         u"T2", u"\u00e9 o mesmo tema do `15_Producao-Interna`", u"aberta"),
    ],
    u"VIX": [
        (u"A VIX tem **5 perfis só de Estilo** (Biquini, Cover ups, PA, Roupas, "
         u"Admin). **Isso vira subárea canônica no BrainHub, ou continua sendo "
         u"só perfil da plataforma?**", u"T2",
         u"define se perfil e área são a mesma entidade ou duas", u"aberta"),
        (u"A matriz de ~60 funções × 17 perfis foi editada pela última vez "
         u"em **09/07/2025** e é mantida à mão. **Ainda reflete a plataforma?**",
         u"T2", u"se não reflete, o corpus estaria copiando ficção", u"aberta"),
    ],
    u"Reserva": [
        (u"7 m\u00f3dulos contratados e **nenhuma etapa do processo atribu\u00edda**. **Conta grande "
         u"n\u00e3o passa pelo funil, ou \u00e9 lacuna de preenchimento?**", u"T2",
         u"vale para Oficina Reserva, NV e Baw tamb\u00e9m", u"aberta"),
        (u"O `Review Quinzenal de Projeto` tem envios marcados at\u00e9 30/06 e nada depois. "
         u"**A cad\u00eancia parou ou s\u00f3 parou de ser marcada?**", u"T2",
         u"\u00e9 a \u00fanica cad\u00eancia formal de report a cliente que o corpus conhece", u"aberta"),
        (u"5 dos 9 grupos de WhatsApp est\u00e3o marcados para excluir e continuam existindo. "
         u"**A limpeza foi feita?**", u"T2", u"canal fora de sistema \u00e9 onde a opera\u00e7\u00e3o vaza",
         u"aberta"),
    ],
    u"Lofty Style": [
        (u"\U0001F6A8 **A credencial do site de documenta\u00e7\u00e3o foi rotacionada?**", u"T0",
         u"exposi\u00e7\u00e3o ativa at\u00e9 prova em contr\u00e1rio", u"aberta"),
        (u"Os dois arquivos de staging `SUPERSEDED` seguem no reposit\u00f3rio. **Apago?**",
         u"T2", u"apagar \u00e9 decis\u00e3o sua, n\u00e3o minha", u"aberta"),
    ],
    u"Baw": [
        (u"A Baw tem o m\u00f3dulo `Integra\u00e7\u00e3o` contratado **e** o ERP diz `Sem Integra\u00e7\u00e3o`. "
         u"**Qual dos dois est\u00e1 errado?**", u"T2",
         u"quinta evid\u00eancia independente de que a conta est\u00e1 mal classificada", u"aberta"),
    ],
    u"Cambos": [
        (u"H\u00e1 duas contas na plataforma \u2014 `Cambos` (7 usu\u00e1rios) e `Cambos - uFlow` (25). "
         u"**\u00c9 conta por m\u00f3dulo, ou duplicidade?**", u"T2",
         u"define se `client_id` \u00e9 mesmo \u00fanico por cliente", u"aberta"),
        (u"O conte\u00fado T1 da Cambos est\u00e1 com autoriza\u00e7\u00e3o de uso pendente desde julho. "
         u"**Libera?**", u"T1", u"trava registrada h\u00e1 mais de dois meses", u"aberta"),
    ],
    u"Mondepars": [
        (u"`Mondepars` × `Mondpars` — **qual grafia está certa?**", u"T2",
         u"🟢 **Respondida em 22 set 2026:** *o nome certo da empresa é "
         u"Mondepars* — pasta renomeada; ⚠ **o CRM segue com a grafia errada**",
         u"respondida em 22 set 2026, por mensagem"),
    ],
    u"Simples (by Reserva)": [
        (u"A pasta `Simples (by Reserva)` não tem linha na base. **É marca da "
         u"Reserva ou conta própria?**", u"T2",
         u"🟢 **Respondida em 22 set 2026:** *é marca de dentro da Reserva; "
         u"a nível de contratação é RESERVA mesmo* — ⚠ resta saber se tem "
         u"usuários e permissões próprios",
         u"respondida em 22 set 2026, por mensagem"),
    ],
}

# PERGUNTAS QUE NAO SAO DE UM CLIENTE SO.
PERGUNTAS_GERAIS = [
    (u"🔴 **`Fale com o Suporte` está BLOQUEADO para todos os 6 perfis da Luiza "
     u"Barcelos e LIBERADO para todos os 17 da VIX. É decisão ou configuração "
     u"esquecida?**", u"T2",
     u"🔴 **explica por que a conta parecia invisível na base de chamados** — e "
     u"significa que **volume de chamado mede quem tem o botão, não atividade de conta**",
     u"aberta"),
    (u"🔴 **`Fornecedor` é perfil de usuário com login na Luiza Barcelos e na "
     u"Lenny Niemeyer. Como o BrainHub modela isso?** Não é pessoa de cliente nem pessoa "
     u"da Casa — **é uma terceira natureza, e ela já tem acesso à plataforma.**",
     u"T2", u"junta-se à `Qualitá` da Oficina Reserva, que opera por WhatsApp", u"aberta"),
    (u"⚠ **O `Manual` está bloqueado para TODOS os perfis nos dois clientes que li** "
     u"(VIX e Luiza Barcelos). **É assim nos outros oito?** Se for, a dor da CAEDU sobre "
     u"manual insuficiente muda de natureza.", u"T2",
     u"se ninguém acessa, a pergunta não é se o manual é bom", u"aberta"),
    (u"🔴 **Por que o desenho de `Griffe › Linha › Grupo › Subgrupo` feito "
     u"para a **Loungerie** nunca chegou na **CAEDU**?** A CAEDU pede essa hierarquia desde a "
     u"weekly de **16/09/2025** e ela reaparece idêntica em jul e ago/2026. A página da "
     u"Loungerie tem os **4 níveis com exemplos e até a alternativa de extensibilidade**.",
     u"T2",
     u"🔴 **não é pergunta de taxonomia, é de circulação de conhecimento** "
     u"— e é exatamente o que o BrainHub existe para impedir", u"aberta"),
    (u"⚠ **A hierarquia da Loungerie foi IMPLEMENTADA ou é só desenho na página?** "
     u"Muda se serve de referência provada ou de proposta.", u"T2",
     u"define se dá para levar à CAEDU como caso pronto", u"aberta"),
    (u"🔴 **Como o BrainHub modela GRUPO ECONÔMICO?** Achei dois: "
     u"**Grupo Único** (Puket — gente com e-mail `@grupounico.com` opera dentro da conta) "
     u"e **Grupo AR&CO** (Oficina Reserva entrou *no mesmo pacote do Grupo*, e a dor número 1 "
     u"dela cita dependência do **time da Arezzo**). **Reserva, Oficina Reserva, Simples e "
     u"Arezzo são quatro pastas isoladas para o que pode ser um contrato só.**", u"T2",
     u"o isolamento de cliente é regra travada, e grupo econômico a atravessa", u"aberta"),
    (u"🔴 **Como o BrainHub modela TERCEIRO que não é cliente nem fornecedor de "
     u"material?** A `Qualitá` inspeciona qualidade para a Oficina Reserva, **por WhatsApp**, "
     u"e a fonte registra que *o inspetor chega para auditar e não tem o documento*.", u"T2",
     u"é onde a operação do cliente vaza para fora de qualquer sistema", u"aberta"),
    (u"🔴 **A dor de excluir/inativar variante aparece em QUATRO clientes** — VIX, "
     u"Reserva, Lofty Style e NV (com dois documentos). **É lacuna da plataforma?**", u"T2",
     u"quatro casos independentes: não é mais hipótese", u"aberta"),
    (u"**`Status` ou `Etapa` \u2014 qual manda?** Discordam em 5 clientes.", u"T2",
     u"\U0001F7E2 **Respondida em 22 set 2026 pelo Vin\u00edcius:** *\"a verdade \u00e9 que n\u00e3o sei. "
     u"N\u00f3s vamos ter que ver caso a caso.\"* \u2014 vira **pergunta por cliente**, n\u00e3o regra geral",
     u"respondida em 22 set 2026, por mensagem"),
    (u"**O portf\u00f3lio de 16 Solu\u00e7\u00f5es est\u00e1 incompleto?** `uBuy` aparece em tr\u00eas clientes "
     u"(Osklen, NK STORE, Reserva) e `uPlan` na Reserva, e nenhum dos dois est\u00e1 na lista.",
     u"T2", u"um caso \u00e9 anedota, tr\u00eas \u00e9 padr\u00e3o", u"aberta"),
    (u"**Qual \u00e9 a chave de identidade de pessoa?** Sem ela, grafia diferente n\u00e3o se resolve "
     u"sem inventar gente.", u"T2", u"trava a fus\u00e3o de 149 fichas", u"aberta"),
    (u"**O campo `Data de Churn` n\u00e3o existe na base.** Criamos?", u"T2",
     u"segue sendo a lacuna mais cara do corpus", u"aberta"),
    (u"**`Merchandising`, `Curadoria`, `Oficina` e `fac\u00e7\u00e3o` n\u00e3o existem na grade de 14 "
     u"\u00e1reas.** A grade cresce, ou viram sub\u00e1rea?", u"T2",
     u"sexta evid\u00eancia do `15_Producao-Interna`", u"aberta"),
]

def esc(p, s):
    d = os.path.dirname(p)
    if not os.path.isdir(d):
        os.makedirs(d)
    if os.path.exists(p) and io.open(p, encoding="utf-8").read() == s:
        return 0
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    return 1


def doc(cliente):
    L = []
    A = L.append
    A(u"# %s · Pendências e fontes varridas" % cliente)
    A(u"")
    A(u"> **Classe: `AUTORIDADE`** sobre **as pendências e a cobertura de varredura DESTE cliente.**")
    A(u"> **Gerado por `scripts/gera-pendencias-e-fontes.py`.**")
    A(u">")
    A(u"> 🔴 **Este é o único lugar onde se pergunta \"o que ainda não sei sobre o %s?\" e" % cliente)
    A(u"> \"onde eu já procurei?\".** O [`_pendencias-gerais.md`]"
      u"(../../../../00_Institucional/_contexto/_pendencias-gerais.md) segue dono das decisões")
    A(u"> **transversais** — as que valem para a carteira toda. **Um assunto, um dono.**")
    A(u"")
    A(u"## 0 · O tier de sensibilidade")
    A(u"")
    A(u"**Vocabulário `T0`/`T1`/`T2`, o mesmo que o João usa no vault** — não um paralelo nosso.")
    A(u"")
    A(u"| Tier | O que é | O que eu faço |")
    A(u"|:-:|---|---|")
    A(u"| **`T2`** | equipe | o padrão — entra normalmente |")
    A(u"| **`T1`** | restrito | entra, e **fica só no `_contexto/` deste cliente** |")
    A(u"| **`T0`** | privado | 🔴 **nunca entra por valor** — registro que existe e **onde** |")
    A(u"")
    A(u"## 1 · Risco de segurança")
    A(u"")
    r = RISCO.get(cliente)
    if r:
        A(u"| O que | Onde | Estado |")
        A(u"|---|---|---|")
        for o, onde, est in r:
            A(u"| %s | %s | %s |" % (o, onde, est))
        A(u"")
        A(u"> 🚨 **O valor não foi replicado em lugar nenhum do corpus** — `T0`.")
        A(u"> **A rotação é ação do Vinicius.** ⚠ Pode já estar inativa; **rotacionar mesmo assim**")
        A(u"> é mais barato que descobrir que não estava.")
    else:
        A(u"🟢 **Nenhum achado até %s.**" % HOJE)
        A(u"")
        A(u"⚠ **Isso não é atestado de limpeza:** significa que **nas fontes da § 3** não apareceu")
        A(u"segredo. **As fontes da § 4 não foram olhadas.**")
    A(u"")
    A(u"## 1-bis · 🔴 O que eu NÃO consegui ler")
    A(u"")
    A(u"> **Pedido do Vinícius em 22 set 2026:** *sobre suspeitas de blocos, sempre tenha "
      u"atenção e me indique, porque temos que ter a garantia de que tudo que está "
      u"varrendo está conseguindo tirar proveito de tudo o que podemos*.")
    A(u">")
    A(u"> 🔴 **Bloco que não renderiza NÃO é bloco vazio.** Na Luiza Barcelos, "
      u"17 blocos ilegíveis escondiam **o único Representante Legal da conta** e o cargo "
      u"do Gerente de Inovação e Tecnologia. **Eu cheguei a chamar isso de falta de "
      u"acesso, e estava errado** — ver `protocolo-varredura-cliente.md` § 11.")
    A(u"")
    nr = NAO_RENDERIZOU.get(cliente)
    if nr:
        A(u"| Onde | Quantos | O que era | Estado |")
        A(u"|---|--:|---|---|")
        for onde, q, oque, est in nr:
            A(u"| %s | %d | %s | %s |" % (onde, q, oque, est))
        A(u"")
        A(u"**O contorno que funciona:** pedir ao Vinícius **só aquele trecho**, copiado "
          u"e colado. **Barato, e o que vier entra como fonte normal, com procedência.**")
    else:
        A(u"🟢 **Nada ilegível nas fontes já abertas.**")
        A(u"")
        A(u"⚠ **Isso só vale para o que foi aberto** (§ 3). **Nas fontes da § 4 "
          u"não sei**, e a página deste cliente pode ter o mesmo tipo de bloco.")
    A(u"")
    A(u"## 2 · Pendências abertas")
    A(u"")
    ps = PEND.get(cliente)
    if ps:
        A(u"| # | O que está em aberto | Tier | O que destrava |")
        A(u"|--:|---|:-:|---|")
        for i, (t, tier, destr) in enumerate(ps, 1):
            A(u"| %d | %s | `%s` | %s |" % (i, t, tier, destr))
    else:
        A(u"⚠ **Nenhuma pendência específica registrada** — e isso quase sempre quer dizer")
        A(u"**que a página deste cliente ainda não foi aberta** (ver § 4), não que esteja tudo claro.")
    A(u"")
    A(u"### 2.1 \u00b7 \U0001F534 Perguntas que s\u00f3 o Vin\u00edcius responde")
    A(u"")
    A(u"> **Uma pergunta s\u00f3 entra aqui quando NENHUMA fonte pode respond\u00ea-la.** D\u00favida que")
    A(u"> uma fonte responde n\u00e3o \u00e9 pergunta \u2014 **\u00e9 varredura que falta fazer**, e vai para a \u00a7 4.")
    A(u">")
    A(u"> \U0001F534 **Estas linhas s\u00e3o colhidas automaticamente** para a lista consolidada em")
    A(u"> [`_perguntas-para-o-vinicius.md`]"
      u"(../../../../00_Institucional/_contexto/_perguntas-para-o-vinicius.md),")
    A(u"> que ele responde **por \u00e1udio ou por transcri\u00e7\u00e3o de reuni\u00e3o**. Ver")
    A(u"> [`protocolo-perguntas-ao-vinicius.md`]"
      u"(../../../../00_Institucional/_protocolos/protocolo-perguntas-ao-vinicius.md).")
    A(u"")
    qs = PERGUNTAS.get(cliente)
    if qs:
        A(u"| # | Pergunta | Tier | Por que importa | Estado |")
        A(u"|--:|---|:-:|---|---|")
        for i, (q, tier, pq, est) in enumerate(qs, 1):
            A(u"| %d | %s | `%s` | %s | %s |" % (i, q, tier, pq, est))
    else:
        A(u"\u26a0 **Nenhuma ainda** \u2014 e para este cliente isso quase sempre quer dizer que a")
        A(u"**p\u00e1gina dele n\u00e3o foi aberta** (\u00a7 3.2). **Pergunta boa nasce de varredura feita.**")
    A(u"")
    A(u"## 3 · 🟢 Fontes JÁ varridas — não reabrir")
    A(u"")
    A(u"> 🔴 **Este é o diário de bordo.** Ele existe porque a memória da conversa **compacta** e a")
    A(u"> do disco não. **Antes de abrir qualquer fonte deste cliente, leia esta tabela.**")
    A(u"")
    A(u"### 3.1 · Varridas para a carteira inteira — valem para o %s" % cliente)
    A(u"")
    A(u"| Fonte | Endereço | Quando | O que saiu | Esgotada? |")
    A(u"|---|---|---|---|---|")
    for f, e, d, s, x in GLOBAIS:
        A(u"| %s | %s | %s | %s | %s |" % (f, e, d, s, x))
    A(u"")
    A(u"### 3.2 · A página deste cliente no Notion")
    A(u"")
    pg = PAGINA.get(cliente)
    if pg:
        d, ident, saiu, esg = pg
        A(u"| Quando | Endereço | O que saiu | Esgotada? |")
        A(u"|---|---|---|---|")
        A(u"| **%s** | %s | %s | %s |" % (d, ident, saiu, esg))
    else:
        A(u"🔴 **NÃO ABERTA.**")
        A(u"")
        A(u"**É a lacuna de maior rendimento deste cliente.** A página tem um toggle `Pessoas`")
        A(u"com 4 blocos — `Diretores e Representantes Legais` · `Responsável pelo Financeiro` ·")
        A(u"`Responsáveis pelos Projetos` · `Responsável Tecnologia` — que é **a única fonte de**")
        A(u"**`cargo` e `área`** do corpus. **Nenhuma consulta SQL alcança a página.**")
    A(u"")
    A(u"## 4 · 🔴 Fontes conhecidas e AINDA NÃO varridas")
    A(u"")
    A(u"| Fonte | Endereço | O que deve trazer |")
    A(u"|---|---|---|")
    for f, e, s in NAO_VARRIDAS:
        A(u"| %s | %s | %s |" % (f, e, s))
    if not pg:
        A(u"| 🔴 **A página deste cliente no Notion** | base `Mapa de Clientes` | "
          u"**`cargo`, `área`, diretoria, sub-páginas de ata — e risco de segredo** |")
    A(u"")
    A(u"## Governança")
    A(u"")
    A(u"### Quem pode alterar este documento")
    A(u"**A § 1, § 2 e § 3 se escrevem a cada varredura**, pelo script. Pendência resolvida **não**")
    A(u"**se apaga: muda de estado**, para o histórico não se perder.")
    A(u"")
    A(u"### Quando ler")
    A(u"🔴 **Antes de varrer este cliente. Sempre.** É o que impede repetir busca já feita.")
    A(u"")
    return chr(10).join(L) + chr(10)


def consolidada():
    u"""A lista que o Vinicius responde. Colhida DAQUI, nunca montada a mao."""
    L = []
    A = L.append
    A(u"# Perguntas para o Vin\u00edcius")
    A(u"")
    A(u"> **Classe: `DERIVADO`.** Gerado por `scripts/gera-pendencias-e-fontes.py`.")
    A(u"> \U0001F534 **N\u00e3o se edita \u00e0 m\u00e3o** \u2014 a pergunta nasce no arquivo do cliente e \u00e9 colhida daqui.")
    A(u">")
    A(u"> **Decis\u00e3o do Vin\u00edcius em 22 set 2026:** *\"em dado momento, voc\u00ea montar\u00e1 uma lista de")
    A(u"> coisas que eu tenho que perguntar e vou dar um jeito de responder ou por \u00e1udio ou numa")
    A(u"> transcri\u00e7\u00e3o de reuni\u00e3o mesmo.\"* **Este \u00e9 esse arquivo.**")
    A(u"")
    A(u"**O processo inteiro est\u00e1 no** [`protocolo-perguntas-ao-vinicius.md`]"
      u"(../_protocolos/protocolo-perguntas-ao-vinicius.md). \U0001F534 **N\u00e3o inventar outro caminho.**")
    A(u"")
    ab = [q for q in PERGUNTAS_GERAIS if q[3].startswith(u"aberta")]
    rs = [q for q in PERGUNTAS_GERAIS if not q[3].startswith(u"aberta")]
    tot_cli = sum(1 for c in PERGUNTAS for q in PERGUNTAS[c] if q[3].startswith(u"aberta"))
    A(u"## 0 \u00b7 O placar")
    A(u"")
    A(u"| | Quantas |")
    A(u"|---|--:|")
    A(u"| **Abertas, de um cliente s\u00f3** | **%d** |" % tot_cli)
    A(u"| **Abertas, transversais** | **%d** |" % len(ab))
    A(u"| J\u00e1 respondidas | %d |" % (len(rs) + sum(1 for c in PERGUNTAS for q in PERGUNTAS[c]
                                                    if not q[3].startswith(u"aberta"))))
    A(u"| Clientes com p\u00e1gina ainda **n\u00e3o aberta** | **%d** |" % (48 - len(PAGINA)))
    A(u"")
    A(u"> \u26a0 **A lista est\u00e1 curta porque a varredura est\u00e1 no come\u00e7o**, n\u00e3o porque h\u00e1 poucas")
    A(u"> d\u00favidas. **%d clientes t\u00eam a p\u00e1gina fechada** \u2014 pergunta boa nasce de varredura feita." % (48 - len(PAGINA)))
    A(u"")
    A(u"## 1 \u00b7 Transversais \u2014 valem para a carteira toda")
    A(u"")
    A(u"| # | Pergunta | Tier | Por que importa | Estado |")
    A(u"|--:|---|:-:|---|---|")
    for i, (q, tier, pq, est) in enumerate(PERGUNTAS_GERAIS, 1):
        A(u"| %d | %s | `%s` | %s | %s |" % (i, q, tier, pq, est))
    A(u"")
    A(u"## 2 \u00b7 Por cliente")
    A(u"")
    for c in sorted(PERGUNTAS):
        A(u"### %s" % c)
        A(u"")
        A(u"[abrir o arquivo do cliente]"
          u"(../../_Clientes/%s/00_Institucional/_contexto/_pendencias-e-fontes.md)" % c)
        A(u"")
        A(u"| # | Pergunta | Tier | Por que importa | Estado |")
        A(u"|--:|---|:-:|---|---|")
        for i, (q, tier, pq, est) in enumerate(PERGUNTAS[c], 1):
            A(u"| %d | %s | `%s` | %s | %s |" % (i, q, tier, pq, est))
        A(u"")
    A(u"## Governan\u00e7a")
    A(u"")
    A(u"### Quem pode alterar este documento")
    A(u"\U0001F534 **Ningu\u00e9m \u00e0 m\u00e3o.** \u00c9 `DERIVADO` \u2014 corrigir na fonte "
      u"(`scripts/gera-pendencias-e-fontes.py`) e rodar o script.")
    A(u"")
    A(u"### O que acontece com uma pergunta respondida")
    A(u"**N\u00e3o se apaga: muda de estado**, com a data e a fonte da resposta. O hist\u00f3rico do que")
    A(u"j\u00e1 se perguntou \u00e9 t\u00e3o \u00fatil quanto a resposta.")
    A(u"")
    return chr(10).join(L) + chr(10)


def main():
    n = 0
    total = 0
    for c in sorted(os.listdir(CLI)):
        base = os.path.join(CLI, c, u"00_Institucional", u"_contexto")
        if not os.path.isdir(base) or c.startswith(u"_template"):
            continue
        total += 1
        n += esc(os.path.join(base, u"_pendencias-e-fontes.md"), doc(c))
    pq = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_contexto",
                      u"_perguntas-para-o-vinicius.md")
    n_q = esc(pq, consolidada())
    # Chave que nao casa com pasta faz o dado SUMIR EM SILENCIO - foi o que
    # aconteceu com `Mondepars` (nome no Notion) contra a pasta `Mondpars`.
    # Silencio e pior que erro: o arquivo sai completo e errado.
    pastas = set(os.listdir(CLI))
    orfas = sorted(set(list(PAGINA) + list(PEND) + list(RISCO) + list(PERGUNTAS) + list(NAO_RENDERIZOU)) - pastas)
    if orfas:
        print(u"")
        print(u"❌ CHAVE SEM PASTA - o dado destas chaves NAO foi escrito:")
        for o in orfas:
            print(u"   %s" % o)
        print(u"Corrija a chave para o nome EXATO da pasta em uMode/_Clientes/.")
        return 1

    print(u"_pendencias-e-fontes.md escrito/atualizado: %d de %d clientes" % (n, total))
    print(u"_perguntas-para-o-vinicius.md: %s" % (u"atualizado" if n_q else u"sem mudanca"))
    print(u"  com página do Notion já aberta : %d" % len(PAGINA))
    print(u"  com pendência específica       : %d" % len(PEND))
    print(u"  com risco de segurança aberto  : %d" % len(RISCO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
