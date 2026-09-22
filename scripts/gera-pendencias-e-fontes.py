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
    (u"🔴 **`umode.kanbanize.com`**", u"boards 6 e 18, cartões por ID",
     u"**cartões de demanda de cliente** — fonte inteira jamais tocada"),
    (u"**Gist** — o chat da plataforma", u"canal oficial de dúvida de usabilidade",
     u"conversa de suporte, por cliente"),
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
    u"Lofty Style": [
        (u"🚨 **Credencial do site de documentação exposta** — registrada desde 21 set 2026.",
         u"T0", u"🚨 **rotação da chave — ação do Vinicius**"),
        (u"🔴 **O `Status` diz `Ongoing` e a `Etapa` diz `Operação Assistida`.**", u"T2",
         u"**Qual dos dois manda?**"),
        (u"⚠ **Dois arquivos de staging marcados `SUPERSEDED` e não apagados** "
         u"(`_staging-lofty-demandas.md`, `_staging-lofty-rfis.md`). **Apagar é decisão sua.**",
         u"T2", u"decisão do Vinicius (item 257)"),
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
        (u"🔴 **Tem o módulo `Integração` contratado e o ERP diz `Sem Integração`.** Os dois não "
         u"podem estar certos. **Quinta evidência independente de que a Baw está mal "
         u"classificada.**", u"T2", u"conferência com o atendimento"),
        (u"⚠ **`Sem CS` com 4 módulos contratados** — é a única conta `Sem CS` com mais de um.",
         u"T2", u"—"),
        (u"⚠ **Sem etapa do processo atribuída.**", u"T2", u"preenchimento"),
    ],
    u"Reserva": [
        (u"🔴 **7 módulos contratados — a conta mais completa da carteira — e NENHUMA etapa do "
         u"processo atribuída.**", u"T2",
         u"**Conta grande não passa pelo funil, ou é lacuna de preenchimento?**"),
        (u"🔴 **Demanda desta conta vive em `umode.kanbanize.com`, boards 6 e 18** — a página "
         u"cita **7 cartões por ID**, 2 fechados e 5 abertos. **Nenhuma varredura tocou o Kanbanize.**",
         u"T2", u"acesso ao Kanbanize"),
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
        (u"⚠ **Duas contas na plataforma para um cliente:** `Cambos` (7 usuários) e "
         u"`Cambos - uFlow` (25). O sufixo indica conta por módulo.", u"T2", u"confirmação"),
        (u"⚠ **ERP `SPI` é sistema próprio do cliente**, não produto de mercado.", u"T2", u"—"),
        (u"⚠ **Conteúdo T1 da Cambos com autorização de uso pendente desde julho.**", u"T1",
         u"autorização do Vinicius/João"),
    ],
    u"Mondepars": [
        (u"⚠ **`Mondepars` na plataforma × `Mondpars` no CRM** — grafia diferente, não é caixa. "
         u"**Um dos dois está errado.**", u"T2", u"conferência"),
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
        (u"🔺 **Correção registrada: eu disse que a conta era \"quase invisível\". Errado** — eu "
         u"media só pela base de chamados, janela de 24 dias. São **24 pessoas, 7 `ATIVO`**.",
         u"T2", u"nada — corrigido"),
        (u"⚠ **ERP `Safe Tech`** — único cliente que o usa.", u"T2", u"—"),
    ],
}

# RISCO DE SEGURANCA, separado por peso proprio: (o que, onde, estado)
RISCO = {
    u"NK STORE": [(u"Credencial de produção do **Linx** (usuário, senha, IP, porta, banco)",
                   u"Notion — página do cliente, toggle `Documentos › Conexão com Linx`",
                   u"🚨 **exposta, não rotacionada**")],
    u"Lofty Style": [(u"Credencial do **site de documentação**",
                      u"registrado em 21 set 2026",
                      u"🚨 **exposta, não rotacionada**")],
}


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


def main():
    n = 0
    total = 0
    for c in sorted(os.listdir(CLI)):
        base = os.path.join(CLI, c, u"00_Institucional", u"_contexto")
        if not os.path.isdir(base) or c.startswith(u"_template"):
            continue
        total += 1
        n += esc(os.path.join(base, u"_pendencias-e-fontes.md"), doc(c))
    print(u"_pendencias-e-fontes.md escrito/atualizado: %d de %d clientes" % (n, total))
    print(u"  com página do Notion já aberta : %d" % len(PAGINA))
    print(u"  com pendência específica       : %d" % len(PEND))
    print(u"  com risco de segurança aberto  : %d" % len(RISCO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
