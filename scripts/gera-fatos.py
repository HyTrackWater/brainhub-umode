# -*- coding: utf-8 -*-
u"""
gera-fatos.py - escreve o bloco `## Fatos` dos MDs de entidade.

DONO UNICO do bloco `## Fatos`. Formato travado em:
  uMode/00_Institucional/_protocolos/protocolo-fato-atomico.md

REGRA CENTRAL: este script NAO le prosa. Ele le as secoes cujo conteudo o corpus
ja produz de forma atomica (contrato, segmentacao, status, ERP, atendimento).
Prosa continua prosa - virar fato e trabalho de leitura, nao de regex.

PROCEDENCIA - a parte que importa. A fonte NAO e adivinhada: ela e herdada por
uma cadeia declarada, do mais especifico para o mais geral:

    blockquote da secao -> linha de valor -> preambulo do bloco `##` pai -> cabecalho

Se nenhum nomeia fonte, sai `[sem fonte]`. Herdar de onde nao foi declarado
seria inventar procedencia - isso e alucinacao, nao conveniencia.

IDENTIDADE - pessoa se resolve por E-MAIL contra as fichas do proprio corpus,
nunca por nome. Nome ambiguo NAO e escolhido: vira pendencia explicita na linha.
E por isso que o agente e generalizado - nenhum nome de pessoa esta no codigo.

  `[a preencher]`  ->  `- chave: ? - [sem fonte]`   (secao 2.1 do protocolo)

Rodar DEPOIS de gera-conexoes.py e ANTES de gera-frontmatter.py.
"""
import io, os, re, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACO = u"\u2014"
PONTO = u"\u00b7"
SEP = u"[,;\u00b7]|\\s+e\\s+"

# ---------------------------------------------------------------- vocabulario
# prefixo do titulo -> (chave do protocolo secao 4, e_lista, so_valor_curto)
# so_valor_curto: campo de enum. Tudo apos " - " ou " (" e comentario, nao valor.
CHAVES_INSTITUCIONAL = [
    (u"ID do cliente",                    u"id",                    False, True),
    (u"Segmento",                         u"segmento",              False, False),
    (u"Receita anual",                    u"receita-anual",         False, True),
    (u"Grupo de segmenta",                u"grupo-segmentacao",     False, True),
    (u"Status atual",                     u"status",                False, True),
    (u"Data de ativa",                    u"data-ativacao",         False, True),
    (u"ERP / Integra",                    u"erp",                   False, True),
    (u"M\u00f3dulos contratados",         u"modulo-contratado",     True,  True),
    (u"Situa\u00e7\u00e3o do contrato",   u"contrato-situacao",     False, True),
    (u"Vig\u00eancia",                    u"contrato-vigencia",     False, True),
    (u"Renova\u00e7\u00e3o e aviso",      u"contrato-renovacao",    False, False),
    (u"\u00cdndice de reajuste",          u"indice-reajuste",       False, True),
    (u"Usu\u00e1rios contratados",        u"usuarios-contratados",  False, True),
    (u"Usu\u00e1rios da conta",           u"usuarios-conta",        False, False),
    (u"Respons\u00e1vel de atendimento",  u"atendimento",           False, True),
    (u"Tamanho de atendimento",           u"tamanho-atendimento",   False, True),
]

# jornada.md e contexto-area.md usam `##` como secao, nao `###`, e a maior
# parte do conteudo util deles esta em TABELA. Por isso os dois tem mapa
# proprio, e nao reaproveitam o do institucional.
CHAVES_JORNADA = [
    (u"Status atual",                  u"status",          False, True),
    (u"Fase atual",                    u"fase",            False, True),
    (u"Módulos em uso",           u"modulo-em-uso",   True,  True),
    (u"Métricas de sucesso",      u"metrica",         True,  False),
]

CHAVES_AREA = [
    (u"Produto conectado",             u"produto-conectado", False, True),
    (u"Pessoas desta área",       u"pessoas-da-area",   False, True),
    (u"Responsável pela área", u"responsavel-area", False, True),
    (u"Responsável na empresa",   u"responsavel-area",  False, True),
]

# Secoes cujo conteudo e TABELA, e o que cada coluna significa.
# (prefixo, chave, i_data, i_valor, i_fonte, i_junta)
#   i_fonte = coluna que E procedencia de verdade (a `Fonte` dos Marcos).
#   i_junta = coluna que COMPLEMENTA o valor, e nao e fonte. `Situacao` e
#             `Validacao que a controla` descrevem a entrega, nao dizem de
#             onde ela veio - tratar coluna assim como fonte era mentir.
# -1 = a coluna nao existe nessa tabela.
TABELAS = {
    u"jornada.md": [
        (u"Marcos da jornada",            u"marco",     0,  1,  2, -1),
        (u"Entregas comprometidas",       u"entrega",  -1,  0, -1,  1),
        (u"Histórico de incidentes",  u"incidente", 0,  1,  2, -1),
    ],
    u"contexto-area.md": [
        (u"Entregas e responsabilidades", u"entrega",  -1,  0, -1,  1),
    ],
}

# O `contexto-area.md` e o `institucional.md` trazem uma tabela
# `Procedência` que mapeia BLOCO -> FONTE -> DATA. E procedência escrita a
# mao, por bloco, pelo proprio corpus - vale mais que qualquer heuristica.
# Aqui se diz qual bloco responde por qual chave.
BLOCO_DA_CHAVE = {
    u"dor":                [u"dores", u"fluxo"],
    # "escopo" entra porque e onde varios jornada.md declaram o que foi
    # prometido - a entrega nasce do escopo acordado, nao de uma secao
    # chamada "entregas".
    # Entrega quase nunca vive numa secao chamada "entregas". Ela e declarada
    # no escopo acordado, nas definicoes do projeto, no cronograma ou na lista
    # de documentos combinados - e e assim que os jornada.md a registram.
    u"entrega":            [u"valida", u"fluxo", u"campos", u"entrega", u"escopo",
                            u"defini", u"cronograma", u"relatório", u"sucesso",
                            u"documento"],
    u"pessoas-da-area":    [u"pessoas"],
    u"produto-conectado":  [u"módulos", u"modulos", u"produto"],
    # dono da area E no CLIENTE: a fonte e a tabela de pessoas, nao a dupla
    # de atendimento da uMode. A ordem aqui e a ordem de preferencia.
    u"responsavel-area":   [u"pessoas", u"dupla", u"atendimento"],
    u"metrica":            [u"métricas", u"metricas"],
    u"incidente":          [u"incidente"],
}

# Listas numeradas que viram um fato por item.
LISTAS = {
    u"contexto-area.md": [(u"Dores registradas", u"dor")],
    u"jornada.md": [(u"Decisões e restrições", u"decisao")],
}

# pista -> nome da fonte. A primeira que casa vence: ordem do mais especifico
# para o mais generico.
FONTES = [
    (u"Segmenta\u00e7\u00e3o Grupos",  u"base Segmenta\u00e7\u00e3o Grupos"),
    (u"Mapa de Clientes",              u"base Mapa de Clientes"),
    (u"base de contratos",             u"planilha de contratos do Financeiro"),
    (u"planilha de contratos",         u"planilha de contratos do Financeiro"),
    # ⚠ `Financeiro` sozinho NAO entra: e nome de area canonica (`11_Financeiro`)
    # e casava com o texto da propria area, fabricando fonte. So conta quando
    # vem acompanhado de "contratos" ou "planilha", acima.
    (u"call de Sales",                 u"call de Sales"),
    (u"pesquisa de \u00e1reas",        u"pesquisa de \u00e1reas"),
    (u"banco da API",                  u"banco da API"),
    (u"conta de API",                  u"banco da API"),
    (u"tabela do PLM",                 u"banco da API"),
    (u"CRM de mentoria",               u"CRM de mentoria"),
    (u"export de CRM",                 u"export de CRM"),
    (u"varredura do Notion",           u"varredura do Notion"),
    (u"uModers",                       u"base uModers do Notion"),
    (u"Notion",                        u"varredura do Notion"),
    (u"CRM",                           u"export de CRM"),
]

MESES = {u"jan": 1, u"fev": 2, u"mar": 3, u"abr": 4, u"mai": 5, u"jun": 6,
         u"jul": 7, u"ago": 8, u"set": 9, u"out": 10, u"nov": 11, u"dez": 12}

RE_DATA_BR  = re.compile(u"(\\d{2})/(\\d{2})/(\\d{4})")
RE_DATA_EXT = re.compile(u"(\\d{1,2})\\s+(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)\\w*\\s+(\\d{4})", re.I)
RE_ISO      = re.compile(u"(\\d{4})-(\\d{2})-(\\d{2})")
RE_MES_ANO  = re.compile(u"(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)\\w*/(\\d{4})", re.I)
RE_FATURADO = re.compile(u"servi\u00e7os? faturados?\\s*:\\s*(.+)$", re.I)
RE_EMAIL    = re.compile(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
RE_H1       = re.compile(u"^# (.+)$", re.M)
# "campo vazio na base X", "não consta em X", "vazio na base X" - a secao
# declarando que ALGUEM ABRIU a fonte e ela estava vazia (protocolo 2.1-bis).
RE_AUSENCIA = re.compile(
    u"(?:campo\\s+)?(?:est\u00e1\\s+)?vazi[ao]\\s+n[ao]\\s+base(.{0,70})"
    u"|n\u00e3o\\s+consta\\s+n[ao](.{0,70})"
    u"|sem\\s+preenchimento\\s+n[ao]\\s+base(.{0,70})", re.I)


# ----------------------------------------------------- identidade por E-MAIL
_PESSOAS = None
_CASA_PRIMEIRO = {}


def indice_pessoas():
    u"""nome normalizado -> conjunto de e-mails. Construido do proprio corpus."""
    global _PESSOAS, _CASA_PRIMEIRO
    if _PESSOAS is not None:
        return _PESSOAS
    _PESSOAS = {}
    for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, u"uMode")):
        if u"_pessoas" not in dirpath:
            continue
        for fn in filenames:
            if not fn.endswith(u".md") or fn.startswith(u"_"):
                continue
            try:
                t = io.open(os.path.join(dirpath, fn), encoding=u"utf-8").read()
            except Exception:
                continue
            m = RE_H1.search(t)
            if not m:
                continue
            partes = t.split(u"### Email", 1)
            if len(partes) < 2:
                continue
            e = RE_EMAIL.search(partes[1].split(u"###")[0])
            if not e:
                continue
            email = e.group(0).lower()

            # Duas formas de H1 convivem no corpus e nenhuma e "errada":
            #   Casa    -> "Nome Sobrenome <PONTO> Pessoa"
            #   Cliente -> "Cliente <PONTO> Pessoa <PONTO> nome"
            # Regra geral, sem nome de cliente no codigo: descarta o rotulo
            # "Pessoa" e fica com o ULTIMO segmento restante.
            segs = [s.replace(u"**", u"").strip()
                    for s in m.group(1).split(PONTO)]
            segs = [s for s in segs if s and s.lower() != u"pessoa"]
            nomes = set()
            if segs:
                nomes.add(segs[-1].lower())
            for rotulo in (u"### Nome completo", u"### Nome preferido"):
                if rotulo in t:
                    linha = t.split(rotulo, 1)[1].split(u"\n")[1].strip()
                    linha = linha.split(u" \u2014 ")[0].strip()
                    if linha and u"a preencher" not in linha.lower():
                        nomes.add(linha.lower())
            for n in nomes:
                _PESSOAS.setdefault(n, set()).add(email)
                # O campo `atendimento` do CRM guarda PRIMEIRO NOME ("Laura",
                # "Julianne"). Indexar o primeiro nome permite resolver quando
                # ele e unico - e acusar ambiguidade quando nao e, que e o
                # comportamento que o protocolo exige. O escopo e a Casa
                # porque atendimento e, por definicao, pessoa da uMode; isso
                # sai da estrutura do corpus, nao de nome nenhum no codigo.
                if u"_Clientes" not in dirpath:
                    primeiro = n.split(u" ")[0]
                    if len(primeiro) > 2:
                        _CASA_PRIMEIRO.setdefault(primeiro, set()).add(email)
    return _PESSOAS


def resolve_pessoa(nome, casa=False):
    u"""'pessoa:<email>' | None se nao achou | '' se ambiguo (NAO escolhe)."""
    if not nome:
        return None
    chave = nome.strip().lower()
    emails = indice_pessoas().get(chave)
    if not emails and casa:
        emails = _CASA_PRIMEIRO.get(chave.split(u" ")[0])
    if not emails:
        return None
    if len(emails) > 1:
        return u""
    return u"pessoa:" + sorted(emails)[0]


# ------------------------------------------------------------------ utilidades
def normaliza_data(txt):
    if not txt:
        return None
    m = RE_ISO.search(txt)
    if m:
        return m.group(0)
    m = RE_DATA_BR.search(txt)
    if m:
        return u"%s-%s-%s" % (m.group(3), m.group(2), m.group(1))
    m = RE_DATA_EXT.search(txt)
    if m:
        return u"%s-%02d-%02d" % (m.group(3), MESES[m.group(2).lower()[:3]], int(m.group(1)))
    # Data PARCIAL: "set/2023", "mai-jun/2024". Devolve AAAA-MM.
    # Truncar para "sem data" seria perder precisao que a fonte tem; inventar
    # o dia seria inventar dado. O mes e exatamente o que a fonte afirma.
    m = RE_MES_ANO.search(txt)
    if m:
        return u"%s-%02d" % (m.group(2), MESES[m.group(1).lower()[:3]])
    return None


def acha_fonte(txt):
    if not txt:
        return None
    low = txt.lower()
    for pista, nome in FONTES:
        if pista.lower() in low:
            return nome
    return None


def limpa(v):
    u"""Tira enfase, backtick e pontuacao terminal. NAO reescreve o valor."""
    v = v.strip()
    v = re.sub(u"^[\\U0001F534\\U0001F7E2\\U0001F7E1\\u26a0\\u25b8\\u25ba\\u2192\\u2014\\s]+", u"", v)
    v = v.replace(u"**", u"").replace(u"`", u"")
    v = re.sub(u"\\[([^\\]]+)\\]\\([^)]+\\)", u"\\1", v)
    v = v.strip().rstrip(u".")
    v = re.sub(u"\\s+", u" ", v)
    return v.strip()


def encurta(v):
    u"""Corta o rabo explicativo de campo de enum. So o valor sobrevive."""
    # fim da primeira frase tambem e fim do valor: em "Nenhum modulo atende
    # esta area. Os quatro modulos da Caedu..." a segunda frase ja e prosa.
    v = re.split(u"\\.\\s+(?=[A-Z\u00c0-\u00dd])", v)[0]
    v = re.split(u"\\s\u2014\\s", v)[0]
    v = re.split(u"\\s\\(", v)[0]
    # o corte pode deixar um travessao orfao na ponta ("... Caedu-Estilo —")
    return v.strip().rstrip(u".,;\u2014-").strip()


def corta_secoes(txt):
    u"""
    [(titulo, corpo, preambulo_do_bloco_pai)] para cada '### '.
    O preambulo e o que vem entre '## ' e o primeiro '### ' - e la que o corpus
    declara a autoridade de um bloco inteiro (ex.: `## Contrato`).
    """
    out = []
    titulo, buf = None, []
    pai_buf, dentro_pai = [], False
    for ln in txt.split(u"\n"):
        if ln.startswith(u"## ") and not ln.startswith(u"### "):
            if titulo is not None:
                out.append((titulo, u"\n".join(buf), u"\n".join(pai_buf)))
            titulo, buf = None, []
            pai_buf, dentro_pai = [], True
        elif ln.startswith(u"### "):
            if titulo is not None:
                out.append((titulo, u"\n".join(buf), u"\n".join(pai_buf)))
            dentro_pai = False
            titulo, buf = ln[4:].strip(), []
        elif titulo is not None:
            buf.append(ln)
        elif dentro_pai:
            pai_buf.append(ln)
    if titulo is not None:
        out.append((titulo, u"\n".join(buf), u"\n".join(pai_buf)))
    return out


def linhas_de_valor(corpo):
    out = []
    for ln in corpo.split(u"\n"):
        s = ln.strip()
        if not s or s.startswith(u">") or s.startswith(u"|") or s.startswith(u"#"):
            continue
        out.append(s)
    return out


def linhas_de_procedencia(corpo):
    u"""So blockquote - e onde o corpus registra de onde veio o dado."""
    return u"\n".join([l for l in corpo.split(u"\n") if l.strip().startswith(u">")])


def valor_da_secao(corpo, e_lista, curto):
    linhas = linhas_de_valor(corpo)
    if not linhas:
        return [] if e_lista else None
    if e_lista:
        itens = [limpa(l[2:]) for l in linhas if l.startswith(u"- ")]
        if not itens:
            # "Gestao de Colecao · Integracao · Relatorios" e uma lista escrita
            # em uma linha so. Separar por `·` nao e fatiar prosa: e o
            # separador que o proprio corpus usa para enumerar.
            bruto = limpa(linhas[0])
            itens = ([x.strip() for x in bruto.split(PONTO)]
                     if PONTO in bruto else [bruto])
        if curto:
            itens = [encurta(i) for i in itens]
        return [i for i in itens if i]
    v = limpa(linhas[0])
    return encurta(v) if curto else v


def vazio(v):
    if v is None:
        return True
    low = v.lower()
    return (u"a preencher" in low) or low in (u"", u"-", u"?", u"n/a")


CABECALHO_BLOCO = [
    u"## Fatos",
    u"",
    u"> \U0001F534 **Camada de FATO ATÔMICO — alvo do cruzamento de transcrição.**",
    u"> Uma linha, um fato: `- chave: valor — [fonte · data]`. **Parse: a procedência é o",
    u"> ÚLTIMO ` — [` da linha**, que sempre termina em `]` — o valor pode conter travessão.",
    u"> **A prosa abaixo é para pessoa; esta seção é para máquina.**",
    u"> ⚠ **Gerado por `scripts/gera-fatos.py` — não editar à mão.** Formato travado no",
    u"> `protocolo-fato-atomico.md`. `[sem fonte]` é **lacuna declarada**, não defeito.",
    u"",
]


def corta_secoes_h2(txt):
    u"""
    [(titulo, corpo)] para cada '## ' - o nivel de secao do jornada.md e do
    contexto-area.md. Para no '## Fatos' e no '## Conexoes', que sao camadas
    geradas e nao conteudo.
    """
    out, titulo, buf = [], None, []
    for ln in txt.split(u"\n"):
        # `###` tambem vira secao: as Dores do contexto-area vivem num `###`
        # dentro de `## Padroes operacionais`, e procurar so no `##` as perdia.
        if ln.startswith(u"## ") or ln.startswith(u"### "):
            if titulo is not None:
                out.append((titulo, u"\n".join(buf)))
            titulo = ln.split(u" ", 1)[1].strip()
            buf = []
        elif titulo is not None:
            buf.append(ln)
    if titulo is not None:
        out.append((titulo, u"\n".join(buf)))
    return out


def celulas(corpo):
    u"""Linhas de tabela markdown -> lista de listas de celulas ja limpas."""
    out = []
    for ln in corpo.split(u"\n"):
        s = ln.strip()
        if not s.startswith(u"|") or not s.endswith(u"|"):
            continue
        cols = [c.strip() for c in s[1:-1].split(u"|")]
        if not cols or all(set(c) <= set(u"-: ") for c in cols):
            continue          # separador
        if len(cols) < 2:
            continue
        out.append([limpa(c) for c in cols])
    return out[1:] if out else []     # a primeira e o cabecalho


def itens_numerados(corpo):
    u"""'1. **X** - y' -> 'X - y'. Lista numerada e um fato por item."""
    out = []
    for ln in corpo.split(u"\n"):
        s = ln.strip()
        m = re.match(u"^(?:\\d+\\.|[-*])\\s+(.+)$", s)
        if m:
            out.append(limpa(m.group(1)))
        elif out and s and not s.startswith((u">", u"|", u"#")):
            # continuacao do item anterior: item de lista quebrado em duas
            # linhas e um fato so, e cortar na primeira linha mutila a frase.
            out[-1] = (out[-1] + u" " + limpa(s)).strip()
    return out


def encurta_fonte(f):
    u"""Nome de fonte curto o bastante para caber na linha e ainda identificar."""
    if not f:
        return f
    f = re.split(u"\\s\\(|,\\s+em\\s+", f)[0]
    f = f.replace(u"Notion — ", u"").replace(u"Notion - ", u"")
    return f.strip().rstrip(u".,;").strip()


def acha_secao(secoes, prefixo):
    for t, corpo in secoes:
        if prefixo.lower() in t.lower():
            return corpo
    return None


def procedencia_declarada(secoes):
    u"""[(bloco, fonte, data)] da tabela `Procedência deste documento`."""
    corpo = acha_secao(secoes, u"Procedência")
    if corpo is None:
        return []
    out = []
    for cols in celulas(corpo):
        if len(cols) < 2:
            continue
        bloco = cols[0].lower()
        fonte = cols[1]
        data = normaliza_data(cols[2]) if len(cols) > 2 else None
        if fonte and not vazio(fonte):
            out.append((bloco, encurta_fonte(fonte), data))
    return out


def por_bloco(proc_tab, chave):
    u"""Fonte e data que a tabela de procedência atribui a esta chave."""
    for palavra in BLOCO_DA_CHAVE.get(chave, []):
        for bloco, fonte, data in proc_tab:
            if palavra in bloco:
                return fonte, data
    return None, None


def monta_bloco_h2(txt, tipo, chaves):
    u"""Bloco `## Fatos` para os MDs cujas secoes sao `##` (jornada, area)."""
    secoes = corta_secoes_h2(txt)
    proc_tab = procedencia_declarada(secoes)
    cabecalho = txt.split(u"\n## ")[0]
    hd_fonte = acha_fonte(cabecalho)
    hd_data = normaliza_data(cabecalho)
    vistos = set()
    fatos = []

    def emite(chave, valor, fonte, data):
        if not valor or vazio(valor):
            return
        # a tabela de procedencia responde por chave; so depois vem heuristica
        p_fonte, p_data = por_bloco(proc_tab, chave)
        fonte = p_fonte or fonte
        data = p_data or data
        if fonte is None:
            ln = u"- %s: %s %s [sem fonte]" % (chave, valor, TRACO)
        else:
            ln = u"- %s: %s %s [%s %s %s]" % (chave, valor, TRACO, fonte,
                                              PONTO, data or u"sem data")
        if ln in vistos:            # duas secoes podem alimentar a mesma chave
            return
        vistos.add(ln)
        fatos.append(ln)

    for prefixo, chave, e_lista, curto in chaves:
        corpo = acha_secao(secoes, prefixo)
        if corpo is None:
            continue
        proc = linhas_de_procedencia(corpo)
        fonte = acha_fonte(proc) or hd_fonte
        data = normaliza_data(proc) or hd_data
        v = valor_da_secao(corpo, e_lista, curto)
        if e_lista:
            for i in (v or []):
                emite(chave, i, fonte, data)
        elif vazio(v):
            # 2.1-bis tambem aqui: se a tabela de Procedencia nomeia o bloco
            # que responde por esta chave, alguem JA olhou e declarou onde.
            # `Ausencia de perfil de acesso e de pessoas -> tabela do PLM,
            # 21/09/2026` e exatamente "procurei ali e nao ha".
            p_fonte, p_data = por_bloco(proc_tab, chave)
            if p_fonte:
                ln = u"- %s: ? %s [não consta em: %s %s %s]" % (
                    chave, TRACO, p_fonte, PONTO, p_data or u"sem data")
            else:
                ln = u"- %s: ? %s [sem fonte]" % (chave, TRACO)
            if ln not in vistos:
                vistos.add(ln)
                fatos.append(ln)
        else:
            emite(chave, v, fonte, data)

    # tabelas: a coluna `Fonte` da tabela, quando existe, E a procedencia -
    # e melhor que qualquer heuristica, porque foi escrita a mao por linha.
    for prefixo, chave, i_data, i_val, i_fonte, i_junta in TABELAS.get(tipo, []):
        corpo = acha_secao(secoes, prefixo)
        if corpo is None:
            continue
        # linha de tabela NAO herda o cabecalho do documento: as entregas de um
        # jornada nao vieram da base que atualizou o cabecalho. Sem coluna de
        # fonte e sem blockquote na secao, a tabela de procedencia decide - e
        # se ela tambem nao cobrir, sai `[sem fonte]`.
        fb_fonte = acha_fonte(linhas_de_procedencia(corpo))
        for cols in celulas(corpo):
            if i_val >= len(cols):
                continue
            val = cols[i_val]
            if not val or vazio(val):
                continue
            if 0 <= i_junta < len(cols) and cols[i_junta] and not vazio(cols[i_junta]):
                val = u"%s %s %s" % (val, PONTO, cols[i_junta])
            fonte = None
            if 0 <= i_fonte < len(cols) and cols[i_fonte] and not vazio(cols[i_fonte]):
                fonte = cols[i_fonte]
            fonte = fonte or fb_fonte
            data = None
            if 0 <= i_data < len(cols):
                data = normaliza_data(cols[i_data])
            emite(chave, val, fonte, data or hd_data)

    for prefixo, chave in LISTAS.get(tipo, []):
        corpo = acha_secao(secoes, prefixo)
        if corpo is None:
            continue
        proc = linhas_de_procedencia(corpo)
        fonte = acha_fonte(proc) or hd_fonte
        data = normaliza_data(proc) or hd_data
        for i in itens_numerados(corpo):
            emite(chave, i, fonte, data)

    if not fatos:
        return None
    return u"\n".join(CABECALHO_BLOCO + fatos) + u"\n"


# ----------------------------------------------------------------- montagem
def monta_bloco(txt):
    por_titulo = {}
    for t, corpo, pai in corta_secoes(txt):
        if t not in por_titulo:
            por_titulo[t] = (corpo, pai)

    cabecalho = txt.split(u"\n## ")[0]
    hd_fonte = acha_fonte(cabecalho)
    hd_data = normaliza_data(cabecalho)

    fatos = []

    def emite(chave, valor, fonte, data):
        if fonte is None:
            fatos.append(u"- %s: %s %s [sem fonte]" % (chave, valor, TRACO))
        else:
            fatos.append(u"- %s: %s %s [%s %s %s]" % (
                chave, valor, TRACO, fonte, PONTO, data or u"sem data"))

    for prefixo, chave, e_lista, curto in CHAVES_INSTITUCIONAL:
        titulo = None
        for t in por_titulo:
            if t.startswith(prefixo):
                titulo = t
                break
        if titulo is None:
            continue
        corpo, pai = por_titulo[titulo]

        # cadeia de procedencia declarada
        proc = linhas_de_procedencia(corpo)
        fonte = acha_fonte(proc)
        data = normaliza_data(proc)
        if fonte is None:
            rabo = u" ".join(linhas_de_valor(corpo))
            fonte = acha_fonte(rabo)
            # a data NUNCA sai da linha de valor: data de fato != data da fonte
        if fonte is None:
            fonte = acha_fonte(pai)
            data = data or normaliza_data(pai)
        if fonte is None:
            fonte = hd_fonte
        data = data or hd_data

        v = valor_da_secao(corpo, e_lista, curto)

        if e_lista:
            itens = [i for i in (v or []) if not vazio(i)]
            if not itens:
                fatos.append(u"- %s: ? %s [sem fonte]" % (chave, TRACO))
            else:
                for i in itens:
                    emite(chave, i, fonte, data)
            continue

        if vazio(v):
            # 2.1-bis: se a secao DECLARA que a fonte foi aberta e estava vazia,
            # a ausencia e verificada e o agente pode tratar dado novo como NOVO.
            # A enfase quebraria o casamento ("campo **vazio** na base"),
            # entao limpa antes de procurar a declaracao de ausencia.
            texto = (corpo + u"\n" + pai).replace(u"**", u"")
            m_aus = RE_AUSENCIA.search(texto)
            # A fonte sai da PROPRIA frase de ausencia, nunca do resto da
            # secao: "campo vazio na base" sem dizer QUAL base nao autoriza
            # citar a primeira fonte que aparecer no blockquote ao lado.
            f_aus = None
            if m_aus:
                for g in m_aus.groups():
                    f_aus = f_aus or acha_fonte(g)
            if f_aus:
                fatos.append(u"- %s: ? %s [não consta em: %s %s %s]"
                             % (chave, TRACO, f_aus, PONTO, data or u"sem data"))
            else:
                fatos.append(u"- %s: ? %s [sem fonte]" % (chave, TRACO))
            continue

        # atendimento: o valor util sao os itens de lista, e cada nome vira
        # `pessoa:<email>`. Identidade por e-mail - nunca por nome.
        if chave == u"atendimento":
            itens = [limpa(l[2:]) for l in linhas_de_valor(corpo) if l.startswith(u"- ")]
            if not itens and (u"+" in v or u"&" in v):
                itens = [x.strip() for x in re.split(u"[+&]", v) if x.strip()]
            elif not itens:
                itens = [v]
            # NAO se quebra prosa em nomes. Fatiar "Julianne e Pedro (Key Account)
            # sendo que X" por virgula e " e " produz "lido", "isso", "SMB" - lixo
            # com cara de identidade, que e pior que nao resolver. Sem item de
            # lista, o valor sai inteiro e a identidade fica declaradamente aberta.
            emitiu = False
            for it in itens:
                nome = encurta(it)
                if not nome or vazio(nome):
                    continue
                r = resolve_pessoa(nome, casa=True)
                emitiu = True
                if r:
                    emite(chave, r, fonte, data)
                elif r == u"":
                    fatos.append(u"- %s: %s %s [ambiguo: mais de um e-mail para este nome]"
                                 % (chave, nome, TRACO))
                else:
                    fatos.append(u"- %s: %s %s [nao resolvido: sem ficha com e-mail para este nome]"
                                 % (chave, nome, TRACO))
            if emitiu:
                continue

        emite(chave, v, fonte, data)

        # "Assinado - servicos faturados: uFlow" carrega DOIS fatos, e
        # servico-faturado e chave propria no protocolo: nao se perde no rabo.
        if chave == u"contrato-situacao":
            brutas = linhas_de_valor(corpo)
            m = RE_FATURADO.search(limpa(brutas[0])) if brutas else None
            if m:
                for s in re.split(SEP, m.group(1)):
                    s = limpa(s).rstrip(u".")
                    if s and not vazio(s):
                        emite(u"servico-faturado", s, fonte, data)

    if not fatos:
        return None

    return u"\n".join(CABECALHO_BLOCO + fatos) + u"\n"


RE_BLOCO = re.compile(u"\n## Fatos\n.*?(?=\n## )", re.S)


def aplica(caminho):
    with io.open(caminho, u"r", encoding=u"utf-8") as f:
        txt = f.read()
    limpo = RE_BLOCO.sub(u"\n", txt)
    nome = os.path.basename(caminho)
    if nome == u"jornada.md":
        bloco = monta_bloco_h2(limpo, nome, CHAVES_JORNADA)
    elif nome == u"contexto-area.md":
        bloco = monta_bloco_h2(limpo, nome, CHAVES_AREA)
    else:
        bloco = monta_bloco(limpo)
    if bloco is None:
        return 0, 0
    partes = limpo.split(u"\n## ", 1)
    if len(partes) != 2:
        return 0, 0
    novo = partes[0].rstrip(u"\n") + u"\n\n" + bloco + u"\n## " + partes[1]
    n = bloco.count(u"\n- ")
    if novo == txt:
        return 0, n
    with io.open(caminho, u"w", encoding=u"utf-8") as f:
        f.write(novo)
    return 1, n


def main():
    alvos = []
    base = os.path.join(RAIZ, u"uMode", u"_Clientes")
    for dirpath, dirnames, filenames in os.walk(base):
        if u"_template" in dirpath:
            continue
        if u"institucional.md" in filenames and u"00_Institucional" in dirpath:
            alvos.append(os.path.join(dirpath, u"institucional.md"))
        if u"jornada.md" in filenames:
            alvos.append(os.path.join(dirpath, u"jornada.md"))
        if u"contexto-area.md" in filenames:
            alvos.append(os.path.join(dirpath, u"contexto-area.md"))
    prop = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_contexto", u"institucional.md")
    if os.path.exists(prop):
        alvos.append(prop)
    alvos = sorted(set(alvos))

    tocados, total = 0, 0
    for a in alvos:
        t, n = aplica(a)
        tocados += t
        total += n

    sem_fonte = ambiguo = nao_res = ausente = 0
    for a in alvos:
        with io.open(a, u"r", encoding=u"utf-8") as f:
            for ln in f.read().split(u"\n"):
                if not ln.startswith(u"- "):
                    continue
                if ln.endswith(u"[sem fonte]"):
                    sem_fonte += 1
                elif u"[não consta em:" in ln:
                    ausente += 1
                elif u"[ambiguo:" in ln:
                    ambiguo += 1
                elif u"[nao resolvido:" in ln:
                    nao_res += 1

    w = sys.stdout.write
    w(u"arquivos alvo      : %d\n" % len(alvos))
    w(u"arquivos escritos  : %d\n" % tocados)
    w(u"fatos gerados      : %d\n" % total)
    w(u"  com fonte        : %d\n"
      % (total - sem_fonte - ambiguo - nao_res - ausente))
    w(u"  ausencia VERIFICADA: %d  <- procurou-se e a fonte estava vazia\n" % ausente)
    w(u"  SEM fonte        : %d  <- lacuna declarada, nao erro\n" % sem_fonte)
    w(u"  pessoa ambigua   : %d  <- nao escolhi: vira pendencia\n" % ambiguo)
    w(u"  sem ficha        : %d  <- nenhuma ficha com e-mail para este nome\n" % nao_res)
    w(u"pessoas indexadas  : %d nomes com e-mail unico\n"
      % len([k for k, v in indice_pessoas().items() if len(v) == 1]))


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    main()
