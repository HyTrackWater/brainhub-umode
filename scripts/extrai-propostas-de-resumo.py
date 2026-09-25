# -*- coding: utf-8 -*-
u"""
extrai-propostas-de-resumo.py - le os resumos do Gemini do acervo da Laura e
escreve, com o TEMPO como eixo:

  1. PROPOSTAS no `_inbox-calls/`, uma por reuniao, no formato do
     `protocolo-entrada-de-call.md`, separadas em ACONTECEU / ACONTECENDO /
     POR VIR conforme a posicao da reuniao na linha do tempo do cliente;
  2. a LINHA DO TEMPO de cada cliente no `jornada.md`, sob `## Marcos da
     jornada`, com as mesmas tres perguntas respondidas a partir de dado
     primario (titulo e data do evento).

\U0001F534 NADA do corpo do resumo e fato: foi escrito por um modelo. Toda linha
de proposta sai `\u26a0 PROPOSTA \u00b7 DERIVADA` e vai para aprovacao humana.

=== A REGRA QUE O VINICIUS COBROU EM 25/09 ===
*"Em um cerebro, tem que ficar claro o que aconteceu, o que esta acontecendo e
o que esta por vir."* A primeira versao deste script extraia a proposta como
fato solto: uma decisao de 2023 e uma de 2026 saiam iguais. Agora:

  ACONTECEU   - dita numa reuniao que ja tem reuniao POSTERIOR do mesmo
                cliente, ou com mais de 90 dias. E historia daquela data.
  ACONTECENDO - dita na reuniao MAIS RECENTE do cliente, com ate 90 dias.
                E o ultimo estado conhecido - nao "o estado".
  POR VIR     - compromisso dessa mesma reuniao recente: o bloco "Proximas
                etapas" do Gemini (que a 1a versao CORTAVA) e toda frase no
                FUTURO ("Laura marcara um forum" nao e estado, e promessa).
  COMPROMISSO ANTIGO - o mesmo, em reuniao superada: estava por vir naquela
                data; o cumprimento NAO esta verificado, e o arquivo diz
                quantas reunioes vieram depois, onde conferir.

\u26a0 O `status` do corpus carrega a data da VARREDURA, nao da transicao
(pendencia 773). O que a linha do tempo permite e LIMITAR: cliente em `Churn`
com reuniao em X estava ativo em X - a saida foi depois. E PESSOA tambem tem
tempo: compromisso que cita quem HOJE esta desligado sai marcado - se nao foi
cumprido antes da saida, ficou sem dono.

=== SENSIBILIDADE (fail-closed; frase descartada inteira, valor nunca escrito)
  T0   - telefone, CPF, e-mail pessoal
  T0-P - juizo sobre pessoa identificavel
  T1   - valor e termo comercial da relacao (NAO a palavra "preco" solta, que
         em PLM de moda e nome de campo - 75 falsos disparos na 1a versao)
\U0001F534 T1 tambem sai daqui porque o `_inbox-calls/` mora na Casa, e T1 "fica so
na pasta daquele cliente". Na duvida, o mais restritivo.

=== TRANSCRICAO ===
\U0001F534 17 dos 76 .docx trazem transcricao de fala DEPOIS do resumo. A 1a
versao nao cortava o bloco e rotulou fala como "resumo Gemini". Agora o recorte
para antes de `\U0001F4D6 Transcricao`, o arquivo declara `tem_transcricao: true`
e os falantes, e cada proposta com minuto e conferivel contra a fala.
\U0001F534 A transcricao bruta nao entra no repositorio.

=== O QUE NAO SE LE ===
Os tres 1:1 internos do acervo: registrados como existentes, nao lidos.
"""
import io, os, re, sys, codecs, collections, zipfile, html, unicodedata, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACERVO = (u"C:/Users/Vinicius/AppData/Local/Temp/claude/"
          u"C--Ambientes-Virtuais-BrainHub-brainhub-umode/"
          u"76bedddf-cfb1-4ab7-9d9e-6a5d6536ec9e/scratchpad/laura2")
INBOX = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_inbox-calls")
CLIENTES_DIR = os.path.join(RAIZ, u"uMode", u"_Clientes")
HOJE = datetime.date(2026, 9, 25)
ORIGEM = u"acervo Laura Cardoso"
JANELA = 90          # dias: ate aqui, a reuniao mais recente e "acontecendo"

# ----------------------------------------------------------- nao se le
NAO_LER = (u"victor _ laura", u"ana paula _ laura", u"dupla lala e holmer")

# ----------------------------------------------------------- destino
# (padrao com borda de palavra, slug, pasta). A ordem importa.
DESTINO = [
    (u"luiza barcelos", u"luiza-barcelos", u"Luiza Barcelos"),
    (u"moda objetiva", u"moda-objetiva", u"Moda Objetiva"),
    (u"objetiva", u"moda-objetiva", u"Moda Objetiva"),
    (u"cambos", u"cambos", u"Cambos"),
    (u"lofty", u"lofty-style", u"Lofty Style"),
    (u"pli[e\u00e9]", u"plie", u"Plie"),
    (u"highstil", u"highstil", u"Highstil"),
    (u"dro", u"dro", u"DRO"),
    (u"ladeira", u"ladeira-bijuterias", u"Ladeira Bijuterias"),
    (u"laces", u"laces", u"Laces"),
    (u"stz|studio z", u"studio-z", u"Studio Z"),
    (u"oficina", u"oficina-reserva", u"Oficina Reserva"),
    (u"ntk", u"ntk", u"NTK"),
    (u"nv", u"nv", u"NV"),
    (u"hyperlocal", u"hyperlocal", u"Hyperlocal"),
    (u"il+imitar", u"ilimitar", None),
]

ASSUNTOS = [
    (u"discovery", u"discovery"), (u"treinamento", u"treinamento"),
    (u"integra", u"integra\u00e7\u00e3o"), (u"onboarding", u"onboarding"),
    (u"quinzenal", u"ritual quinzenal"), (u"weekly", u"weekly"),
    (u"workflow", u"workflow"), (u"alinhamento", u"alinhamento"),
    (u"d\u00favida", u"d\u00favidas"), (u"duvida", u"d\u00favidas"),
    (u"feedback", u"feedback"), (u"cronograma", u"cronograma"),
    (u"fechamento", u"fechamento"), (u"teste", u"teste"),
    (u"importa", u"importa\u00e7\u00e3o"), (u"permission", u"permissionamento"),
    (u"ficha", u"ficha t\u00e9cnica"), (u"custo", u"custos"),
    (u"medidas", u"tabela de medidas"), (u"kick", u"kick-off"),
]

# ----------------------------------------------------------- classificador
# ordem = precedencia. Uma chave por frase. So chaves do vocabulario fechado.
CLASSE = [
    (u"incidente", re.compile(
        u"\\b(instabilidade|fora do ar|travou|travando|indispon\u00edve|queda do|"
        u"erro em produ)", re.I)),
    (u"marco", re.compile(
        u"\\b(entrou em produ|foi para produ|seguir para (a )?produ|go.?live|"
        u"kick.?off|homologa\u00e7\u00e3o (foi )?(conclu|aprovad)|virada)", re.I)),
    (u"decisao", re.compile(
        u"\\b(foi (decidid|definid|estabelecid|acordad|aprovad|confirmad)|"
        u"ficou (decidid|definid|acordad|combinad|estabelecid)|decidiu-se|"
        u"definiu-se|optou-se|a decis\u00e3o)", re.I)),
    (u"entrega", re.compile(
        u"\\b(ser\u00e1 entregue|ser\u00e3o entregues|ficou respons\u00e1vel|ficou de "
        u"(enviar|entregar|verificar|validar|ajustar)|se comprometeu|"
        u"prazo (de|para|at\u00e9)|at\u00e9 (o dia|a pr\u00f3xima))", re.I)),
    # \u26a0 sem "manual": pegava frase neutra - 52 disparos sem dor.
    (u"dor", re.compile(
        u"\\b(problema|dificuldade|lentid\u00e3o|gargalo|retrabalho|limita\u00e7\u00e3o|"
        u"n\u00e3o consegue|n\u00e3o conseguem|impossibilit)", re.I)),
]
ERPS = re.compile(u"\\b(Linx|TOTVS|Protheus|SAP|Millennium|Sankhya|Bling|Omie|"
                  u"Senior|Datasul|Microvix|Tiny|Consinco|SPI)\\b")

# ----------------------------------------------------------- sensibilidade
T0 = re.compile(
    u"(?<!\\d)(?:\\+?55\\s?)?\\(?\\d{2}\\)?\\s?9?\\d{4}[- ]?\\d{4}(?!\\d)|"
    u"(?<!\\d)\\d{3}\\.?\\d{3}\\.?\\d{3}-?\\d{2}(?!\\d)|"
    u"[A-Za-z0-9._%+-]+@(gmail|hotmail|outlook|yahoo|icloud|bol|terra|uol)\\.")
T1 = re.compile(
    u"R\\$\\s?\\d|\\d+(,\\d+)?\\s?(mil|k)\\s?(reais|por m\u00eas)|"
    u"\\bvalor (do|da|de) (contrato|proposta|mensalidade|hora)|"
    u"\\bproposta comercial|\\bsal\u00e1rio|\\bmensalidade|\\bdesconto de \\d|"
    u"\\breajuste de \\d|\\bmargem de \\d|\\bpre\u00e7o de \\d|\\bpre\u00e7o (final )?de R",
    re.I)
NOME = re.compile(u"\\b[A-Z\u00c0-\u00dd][a-z\u00e0-\u00ff]+ [A-Z\u00c0-\u00dd][a-z\u00e0-\u00ff]+\\b")
JUIZO = re.compile(
    u"\\b(n\u00e3o (entregou|cumpriu|respondeu|domina|sabe usar)|sobrecarregad|"
    u"desorganizad|insatisfeit|reclamou d|culpa|atrasou|falhou|"
    u"n\u00e3o tem (conhecimento|capacidade|preparo)|desempenho|demiss|deslig|"
    u"despreparad|resist\u00eancia d[oa] )", re.I)

# \u23ed tempo verbal: frase no futuro e compromisso, seja qual for a chave.
# "Ficou decidido que Laura marcara um forum" e POR VIR, nao estado atual.
FUTURO = re.compile(
    u"\\b(ir\u00e1|ir\u00e3o|vai|v\u00e3o|ser\u00e1|ser\u00e3o|dever\u00e1|dever\u00e3o|ficou de|fica de|"
    u"a ser (feit|enviad|definid|agendad|validad)|pr\u00f3xima (reuni\u00e3o|semana|etapa)|"
    u"[a-z\u00e0-\u00ff]{3,}(ar|er|ir)(\u00e1|\u00e3o))\\b", re.I)

RE_DATA = re.compile(u"(\\d{4})[_-](\\d{2})[_-](\\d{2})")
RE_TS = re.compile(u"\\s*\\((\\d{2}:\\d{2}:\\d{2})\\)")
RE_E = re.compile(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
RE_CONV = re.compile(u"convidado\\s+(.{0,400}?)(?:\\n|Anexos)", re.S)
RE_FALA = re.compile(u"^\\s*([^\\n:]{2,40}): \\S", re.M)
MARCA_TR = u"\U0001F4D6 Transcri"
INI = u"<!-- acervo-laura:linha-do-tempo:inicio -->"
FIM = u"<!-- acervo-laura:linha-do-tempo:fim -->"


def docx(p):
    try:
        with zipfile.ZipFile(p) as z:
            x = z.read(u"word/document.xml").decode(u"utf-8", u"replace")
    except Exception:
        return u""
    x = re.sub(u"</w:p>", u"\n", x)
    return html.unescape(re.sub(u"<[^>]+>", u"", x))


def kebab(s, n=48):
    s = unicodedata.normalize(u"NFKD", s)
    s = u"".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(u"[^a-z0-9]+", u"-", s).strip(u"-")
    return s[:n].rstrip(u"-") or u"reuniao"


def titulo_limpo(nome):
    t = re.sub(u"\\s*-\\s*(\\d{4}[_-]\\d{2}[_-]\\d{2}).*$", u"", nome)
    t = re.sub(u"\\.(docx|txt)$", u"", t)
    return t.replace(u"_", u"\u00b7").strip(u" \u00b7")


def destino_de(nome):
    low = nome.lower()
    for pad, slug, pasta in DESTINO:
        if re.search(u"(?<![a-z\u00e0-\u00ff])(%s)(?![a-z\u00e0-\u00ff])" % pad, low):
            return slug, pasta
    return None, None


def assunto_de(nome):
    low = nome.lower()
    for k, rot in ASSUNTOS:
        if k in low:
            return rot
    return u"\u2014"


def frases(detalhes):
    out = []
    for par in detalhes.split(u"\n"):
        par = par.strip()
        if len(par) < 30:
            continue
        for f in re.split(u"(?<=[.!?\\)])\\s+(?=[A-Z\u00c0-\u00dd])", par):
            f = f.strip()
            if 25 <= len(f) <= 600:
                out.append(f)
    return out


def status_do_corpus(pasta):
    if not pasta:
        return None, None
    p = os.path.join(CLIENTES_DIR, pasta, u"00_Institucional", u"_contexto",
                     u"institucional.md")
    if not os.path.exists(p):
        return None, None
    t = io.open(p, encoding=u"utf-8", errors=u"replace").read()
    m = re.search(u"^- status: (.+?) \u2014 \\[(.+?) \u00b7 (\\d{4}-\\d{2}-\\d{2})\\]", t, re.M)
    return (m.group(1).strip(), m.group(3)) if m else (None, None)


# ================================================================ passo 1
def le_acervo():
    u"""Toda reuniao do acervo (docx e chat), com data e destino do TITULO."""
    mapa = {}
    for l in io.open(os.path.join(ACERVO, u"_mapa.tsv"),
                     encoding=u"utf-8").read().splitlines()[1:]:
        c = l.split(u"\t")
        if len(c) >= 2:
            mapa[c[0]] = c[1]
    reunioes = {}          # (slug, data, chave-titulo) -> reuniao
    nao_lidos = []
    for fn, nome in sorted(mapa.items()):
        if any(k in nome.lower() for k in NAO_LER):
            nao_lidos.append(nome)
            continue
        md = RE_DATA.search(nome)
        if not md:
            continue
        try:
            d = datetime.date(*(int(x) for x in md.groups()))
        except ValueError:
            continue
        slug, pasta = destino_de(nome)
        titulo = titulo_limpo(nome)
        k = (slug, d, kebab(titulo, 30))
        r = reunioes.setdefault(k, {u"slug": slug, u"pasta": pasta, u"data": d,
                                    u"titulo": titulo, u"assunto": assunto_de(nome),
                                    u"docx": None, u"chat": False})
        if fn.endswith(u".docx"):
            r[u"docx"] = fn
        else:
            r[u"chat"] = True
    return list(reunioes.values()), nao_lidos


def le_resumo(fn):
    t = docx(os.path.join(ACERVO, fn))
    i = t.find(u"Detalhes")
    ti = t.find(MARCA_TR)
    falantes = []
    n_falas = 0
    if ti != -1:
        cont = collections.Counter(m.group(1).strip() for m in RE_FALA.finditer(t[ti:]))
        falantes = [n for n, _ in cont.most_common() if not re.match(u"^\\d", n)]
        n_falas = sum(v for n, v in cont.items() if not re.match(u"^\\d", n))
    mc = RE_CONV.search(t)
    emails = sorted(set(e.lower() for e in RE_E.findall(mc.group(1)))) if mc else []
    etapas = proximas_etapas(t, ti)
    if i == -1:
        return None, etapas, emails, falantes, n_falas
    # \U0001F534 o recorte para ANTES da transcricao: fala nao e resumo
    det = t[i + len(u"Detalhes"):(ti if ti > i else len(t))]
    for corte in (u"Pr\u00f3ximas etapas sugeridas", u"Suggested next steps",
                  u"Voc\u00ea deve revisar", u"Revise as anota"):
        j = det.find(corte)
        if j != -1:
            det = det[:j]
    return det, etapas, emails, falantes, n_falas


def proximas_etapas(t, ti):
    u"""
    O bloco de proximas etapas do Gemini - o POR VIR com dono. \U0001F534 A 1a
    versao o cortava fora, e o eixo "por vir" saiu quase vazio. Dois formatos:
      novo   : `Proximas etapas` ANTES de `Detalhes`, linhas `[Dono] Acao: ...`
      antigo : `Proximas etapas sugeridas` DEPOIS, linhas `Fulano ira ...`
    """
    fim_doc = ti if ti != -1 else len(t)
    m = re.search(u"^(Pr\u00f3ximas etapas sugeridas|Suggested next steps)\\s*$", t, re.M)
    if m:
        bloco = t[m.end():fim_doc]
        for corte in (u"Revise as anota", u"Voc\u00ea deve revisar", u"Envie feedback"):
            j = bloco.find(corte)
            if j != -1:
                bloco = bloco[:j]
    else:
        m = re.search(u"^Pr\u00f3ximas etapas\\s*$", t, re.M)
        if not m:
            return []
        d = re.search(u"^Detalhes\\s*$", t[m.end():], re.M)
        bloco = t[m.end():m.end() + d.start()] if d else t[m.end():fim_doc]
    out = []
    for l in bloco.split(u"\n"):
        l = re.sub(u"^[\\s\u2610\u2611\u25a1\u2022*-]+", u"", l).strip()
        l = l.replace(u"{", u"").replace(u"}", u"")
        if len(l) >= 15:
            out.append(l)
    return out


def sensivel(corpo, ts, t0, t0p, t1):
    if T0.search(corpo):
        t0.append(ts)
        return True
    if NOME.search(corpo) and JUIZO.search(corpo):
        t0p.append(ts)
        return True
    if T1.search(corpo):
        t1.append(ts)
        return True
    return False


def corta(s):
    return s if len(s) <= 260 else s[:257].rsplit(u" ", 1)[0] + u"…"


def classifica(det, etapas):
    u"""(chave, texto, ts, futuro). `futuro` decide o bloco, nao a chave."""
    props, t0, t0p, t1 = [], [], [], []
    for l in etapas:
        if not sensivel(l, None, t0, t0p, t1):
            props.append((u"entrega", corta(l), u"próximas etapas", True))
    for f in frases(det):
        mts = RE_TS.search(f)
        ts = mts.group(1) if mts else None
        corpo = RE_TS.sub(u"", f).strip()
        if sensivel(corpo, ts, t0, t0p, t1):
            continue
        chave = None
        if ERPS.search(corpo) and re.search(u"\\bERP\\b|integra", corpo, re.I):
            chave = u"erp"
        else:
            for k, rx in CLASSE:
                if rx.search(corpo):
                    chave = k
                    break
        if not chave:
            continue
        futuro = chave == u"entrega" or (chave != u"incidente" and bool(FUTURO.search(corpo)))
        props.append((chave, corta(corpo), ts, futuro))
    return props, t0, t0p, t1


# ================================================================ tempo
def tempo_da(r, linha):
    u"""Posicao da reuniao r na linha do tempo do seu cliente."""
    depois = [x for x in linha if x[u"data"] > r[u"data"]]
    idade = (HOJE - r[u"data"]).days
    recente = not depois and idade <= JANELA
    return {u"k": linha.index(r) + 1, u"n": len(linha), u"depois": len(depois),
            u"ultima": linha[-1][u"data"], u"idade": idade, u"recente": recente}


def bloco_de(futuro, pos):
    if pos[u"recente"]:
        return u"por-vir" if futuro else u"acontecendo"
    return u"compromisso-antigo" if futuro else u"aconteceu"


_DESL = None


def desligados():
    u"""
    Nome completo (2+ tokens, sem acento) de quem a ficha do corpus marca como
    desligado. \U0001F534 Um token so nunca resolve pessoa - regra do corpus.
    Usa o mesmo indice do `gera-fatos.py`: um so dono da resolucao de pessoa.
    """
    global _DESL
    if _DESL is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            u"gera_fatos", os.path.join(RAIZ, u"scripts", u"gera-fatos.py"))
        g = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(g)
        P = g.indice_pessoas()
        _DESL = (g._norm, sorted(set(
            n.replace(u"*", u"").strip() for n, es in P.items()
            if es & g._INATIVOS and len(n.replace(u"*", u"").split()) >= 2)))
    return _DESL


def orfao(texto):
    u"""Pessoa HOJE desligada citada num compromisso: se nao foi cumprido, ficou sem dono."""
    norm, nomes = desligados()
    t = u" " + re.sub(u"[^a-z0-9 ]", u" ", norm(texto)) + u" "
    achados = [n for n in nomes if u" %s " % n in t]
    return max(achados, key=len) if achados else None


def dias(n):
    return u"%d dia%s" % (n, u"" if n == 1 else u"s")


# ================================================================ escrita
def escreve_inbox(r, pos, props, t0, t0p, t1, st):
    data = r[u"data"].isoformat()
    tier = u"T0" if (t0 or t0p) else (u"T1" if t1 else u"T2")
    emails, falantes, n_falas = r[u"emails"], r[u"falantes"], r[u"n_falas"]
    tem_tr = n_falas > 0
    status, st_data = st
    cli = r[u"pasta"] or r[u"slug"] or u"cliente n\u00e3o identificado"

    L = [u"---", u"tipo: registro",
         u"origem: google-meet \u00b7 resumo do Gemini" + (u" + transcri\u00e7\u00e3o" if tem_tr else u""),
         u"acervo: %s" % ORIGEM,
         u'titulo: "%s"' % r[u"titulo"].replace(u'"', u"'"),
         u"data: %s" % data, u"referente_a: %s" % data,
         u"destino: %s" % (r[u"slug"] or u"\"[a preencher]\""),
         u"confianca_destino: %s" % (u"media" if r[u"slug"] else u"baixa"),
         u"natureza: \"[a preencher]\""]
    L.append(u"participantes:" if emails else u"participantes: []")
    L += [u"  - %s" % e for e in emails]
    if falantes:
        L.append(u"participantes_sem_email:")
        L += [u'  - "%s"' % f.replace(u'"', u"'") for f in falantes]
    else:
        L.append(u"participantes_sem_email: []")
    L += [u"tem_transcricao: %s" % (u"true" if tem_tr else u"false"),
          u"tem_resumo: true",
          u"posicao_na_linha_do_tempo: %d/%d" % (pos[u"k"], pos[u"n"]),
          u"reunioes_depois: %d" % pos[u"depois"],
          u"idade_em_dias: %d" % pos[u"idade"],
          u"horizonte: %s" % (u"recente" if pos[u"recente"] else u"historico"),
          u"tier: %s" % tier,
          u"tier_motivo: \"%s\"" % (
              u"dado pessoal ou ju\u00edzo sobre pessoa detectado; valor n\u00e3o escrito" if tier == u"T0"
              else u"valor comercial detectado; valor n\u00e3o escrito" if tier == u"T1"
              else u"sem dado pessoal nem valor comercial detectado"),
          u"processado_em: %s" % HOJE.isoformat(), u"---",
          u"# %s \u2014 %s" % (r[u"titulo"], data), u"",
          u"> **Classe: `REGISTRO`.** Evid\u00eancia datada. \U0001F534 **N\u00e3o \u00e9 autoridade e n\u00e3o se edita.**"]
    if tem_tr:
        L += [u"> **Fonte:** resumo do Gemini, %s. \U0001F7E2 **Esta reuni\u00e3o TEM transcri\u00e7\u00e3o de fala** no" % ORIGEM,
              u"> `.docx` original \u2014 **%d falas, %d falantes**. As propostas abaixo v\u00eam do **resumo**" % (n_falas, len(falantes)),
              u"> (derivado); **cada uma com minuto \u00e9 confer\u00edvel contra a fala**. \U0001F534 A transcri\u00e7\u00e3o",
              u"> bruta n\u00e3o entra no reposit\u00f3rio."]
    else:
        L += [u"> **Fonte:** resumo do Gemini, %s. \U0001F534 **N\u00e3o h\u00e1 transcri\u00e7\u00e3o de fala desta reuni\u00e3o** \u2014" % ORIGEM,
              u"> tudo abaixo foi escrito por um modelo e \u00e9 **derivado**."]
    L += [u"> \u26a0 **Destino `%s` saiu do t\u00edtulo:** n\u00e3o \u00e9 prova de que a reuni\u00e3o foi com o cliente." % (r[u"slug"] or u"?"),
          u"", u"## \u23f1 Posi\u00e7\u00e3o no tempo", u"",
          u"| | |", u"|---|---|",
          u"| Reuni\u00e3o | **%d de %d** de %s neste acervo |" % (pos[u"k"], pos[u"n"], cli),
          u"| Data | **%s** \u2014 **%s atr\u00e1s** |" % (data, dias(pos[u"idade"])),
          u"| Depois dela | **%d reuni\u00f5es**%s |" % (
              pos[u"depois"], (u" \u2014 a \u00faltima em **%s**" % pos[u"ultima"].isoformat())
              if pos[u"depois"] else u" \u2014 **\u00e9 a mais recente**"),
          u"| Status no corpus | %s |" % (
              (u"`%s` \u2014 varredura de **%s**, que \u00e9 a data da **leitura**, n\u00e3o da transi\u00e7\u00e3o" % (status, st_data))
              if status else u"`[a preencher]` \u2014 cliente sem pasta ou sem fato `status`"),
          u""]
    if pos[u"recente"]:
        L += [u"\U0001F7E2 **\u00c9 a evid\u00eancia mais recente deste cliente e tem at\u00e9 %d dias.** O que ela afirma \u00e9 o" % JANELA,
              u"**\u00faltimo estado conhecido** \u2014 n\u00e3o \"o estado\"; e o que ela promete \u00e9 o que est\u00e1 **por vir**."]
    else:
        L += [u"\u26a0 **Esta reuni\u00e3o \u00e9 hist\u00f3ria.** O que ela afirma **aconteceu em %s**; o que prometia" % data,
              u"**estava por vir naquela data**, e o cumprimento **n\u00e3o est\u00e1 verificado**%s." % (
                  (u" \u2014 h\u00e1 **%d reuni\u00f5es posteriores** onde conferir" % pos[u"depois"]) if pos[u"depois"]
                  else u" \u2014 e **n\u00e3o h\u00e1 reuni\u00e3o posterior neste acervo** onde conferir")]
    if status and status.lower().startswith(u"churn") and pos[u"depois"] == 0:
        L += [u"", u"\U0001F7E2 **Limite temporal do churn:** o corpus diz `%s` (lido em %s) e esta \u00e9 a \u00faltima" % (status, st_data),
              u"reuni\u00e3o do cliente neste acervo. **O cliente estava ativo em %s \u2014 a sa\u00edda foi depois.** A data" % data,
              u"exata segue `[a preencher]`."]

    rot = {u"aconteceu": u"\u2705 Aconteceu \u2014 em %s" % data,
           u"acontecendo": u"\U0001F504 Acontecendo \u2014 \u00faltimo estado conhecido, %s" % data,
           u"por-vir": u"\u23ed Por vir \u2014 compromissos da reuni\u00e3o mais recente",
           u"compromisso-antigo": u"\u231b Compromissos de %s \u2014 cumprimento n\u00e3o verificado" % data}
    grupos = collections.OrderedDict((k, []) for k in
                                     (u"acontecendo", u"por-vir", u"aconteceu", u"compromisso-antigo"))
    for k, corpo, ts, futuro in props:
        grupos[bloco_de(futuro, pos)].append((k, corpo, ts))
    L += [u"", u"## \u26a0 Fatos propostos \u2014 ainda N\u00c3O s\u00e3o fatos", u""]
    if not props:
        L += [u"_Nenhuma proposta fora das faixas sens\u00edveis._", u""]
    for g, itens in grupos.items():
        if not itens:
            continue
        L += [u"### %s" % rot[g], u""]
        for k, corpo, ts in itens:
            o = orfao(corpo) if g in (u"por-vir", u"compromisso-antigo") else None
            L.append(u"- %s: %s \u2014 [resumo Gemini %s%s] \u26a0 PROPOSTA \u00b7 DERIVADA%s%s"
                     % (k, corpo, data, (u" \u00b7 " + ts) if ts else u"",
                        u" \u00b7 confer\u00edvel na transcri\u00e7\u00e3o" if (tem_tr and ts and ts[0].isdigit()) else u"",
                        (u" \u00b7 \U0001F534 envolve pessoa HOJE desligada (%s)" % o.title()) if o else u""))
        L.append(u"")
    if t0 or t0p or t1:
        L += [u"## \U0001F534 Sensibilidade detectada \u2014 nenhum valor escrito", u""]
        for rt, lst in ((u"T0 \u00b7 dado pessoal", t0),
                        (u"T0-P \u00b7 ju\u00edzo sobre pessoa identific\u00e1vel", t0p),
                        (u"T1 \u00b7 valor comercial", t1)):
            if lst:
                tss = [x for x in lst if x]
                L.append(u"- **%s** \u2014 %d frase(s)%s" % (
                    rt, len(lst), (u" \u00b7 minutos: " + u", ".join(tss)) if tss else u""))
        L += [u"", u"> \U0001F534 **A frase foi descartada inteira, n\u00e3o mascarada.**", u""]
    L += [u"## Governan\u00e7a", u"", u"### Quem pode alterar este documento",
          u"\U0001F534 **Ningu\u00e9m.** \u00c9 registro de entrada. Aprovar ou recusar uma proposta gera",
          u"registro novo no destino, apontando para este.", u""]
    io.open(os.path.join(INBOX, r[u"arq"] + u".md"), u"w", encoding=u"utf-8").write(u"\n".join(L))
    return grupos


def linhas_compromisso(itens):
    out, orf = [], collections.Counter()
    for _, c, _ in itens:
        o = orfao(c)
        if o:
            orf[o.title()] += 1
        out.append(u"- %s%s" % (c, (u" — \U0001F534 **pessoa hoje desligada: %s**" % o.title()) if o else u""))
    if orf:
        out.append(u"")
        out.append(u"\U0001F534 **%d de %d compromissos envolvem pessoa hoje desligada** (%s). Se não foram "
                   u"cumpridos antes da saída, **ficaram sem dono** — e nenhuma fonte diz quem herdou."
                   % (sum(orf.values()), len(itens), u" · ".join(orf)))
    return out


def escreve_jornada(pasta, linha, st, res):
    u"""Linha do tempo do cliente no `jornada.md`, sob `## Marcos da jornada`."""
    cam = os.path.join(CLIENTES_DIR, pasta, u"00_Institucional", u"_contexto", u"jornada.md")
    if not os.path.exists(cam):
        return u"sem jornada.md"
    t = io.open(cam, encoding=u"utf-8").read()
    status, st_data = st
    ult = linha[-1]
    idade = (HOJE - ult[u"data"]).days
    rel = u"../../../../00_Institucional/_inbox-calls/"

    B = [INI, u"### \u23f1 Linha do tempo das reuni\u00f5es \u2014 acervo Laura Cardoso", u"",
         u"> **Fonte:** t\u00edtulo e data de cada reuni\u00e3o no acervo da Laura Cardoso \u2014 **dado prim\u00e1rio**",
         u"> (o t\u00edtulo \u00e9 o evento da agenda; n\u00e3o passou por modelo). Conferido em **%s**." % HOJE.strftime(u"%d/%m/%Y"),
         u"> \u26a0 **\u00c9 a carteira de UMA atendente:** reuni\u00e3o ausente aqui n\u00e3o prova reuni\u00e3o ausente.",
         u"> \u26a0 **Gerado por `scripts/extrai-propostas-de-resumo.py` \u2014 n\u00e3o editar \u00e0 m\u00e3o.**", u"",
         u"#### \u2705 Aconteceu \u2014 %d reuni\u00f5es, de %s a %s" % (
             len(linha), linha[0][u"data"].isoformat(), ult[u"data"].isoformat()), u"",
         u"| Data | Assunto (do t\u00edtulo) | Fonte | Propostas no inbox |",
         u"|---|---|---|---|"]
    for r in linha:
        if r[u"docx"]:
            fonte = u"resumo" + (u" + **transcri\u00e7\u00e3o**" if r.get(u"n_falas") else u"")
        else:
            fonte = u"s\u00f3 chat"
        if r.get(u"arq"):
            n = sum(len(v) for v in res.get(r[u"arq"], {}).values())
            prop = u"[%d](%s%s.md)" % (n, rel, r[u"arq"])
        else:
            prop = u"\u2014"
        B.append(u"| %s | %s | %s | %s |" % (r[u"data"].isoformat(), r[u"assunto"], fonte, prop))
    B += [u"", u"#### \U0001F504 Acontecendo \u2014 o \u00faltimo estado conhecido", u"",
          u"- **\u00daltima reuni\u00e3o neste acervo:** %s \u2014 *%s* \u2014 **%s atr\u00e1s**." % (
              ult[u"data"].isoformat(), ult[u"titulo"], dias(idade)),
          u"- **Status no corpus:** %s." % (
              (u"`%s` \u2014 varredura de %s (data da **leitura**, n\u00e3o da transi\u00e7\u00e3o)" % (status, st_data))
              if status else u"`[a preencher]`")]
    quem = [u"`%s`" % e for e in ult.get(u"emails", [])] + list(ult.get(u"falantes", []))
    if quem:
        B.append(u"- **Quem esteve na \u00faltima reuni\u00e3o:** %s." % u" \u00b7 ".join(quem))
    s = (status or u"").lower()
    if s.startswith(u"churn"):
        B.append(u"- \U0001F7E2 **Limite do churn:** o cliente estava em reuni\u00e3o em **%s**; a sa\u00edda foi **depois**"
                 u" disso e **antes de %s**. Data exata `[a preencher]`." % (ult[u"data"].isoformat(), st_data))
    elif idade > 180:
        B.append(u"- \U0001F534 **`%s` no corpus e %s sem reuni\u00e3o neste acervo.** N\u00e3o prova abandono \u2014"
                 u" a conta pode estar com outra pessoa \u2014 **mas \u00e9 a pergunta a fazer.**" % (status or u"?", dias(idade)))
    elif idade <= JANELA:
        B.append(u"- \U0001F7E2 **Coerente:** status ativo e reuni\u00e3o h\u00e1 %s." % dias(idade))
    else:
        B.append(u"- \u26a0 **Entre 3 e 6 meses sem reuni\u00e3o neste acervo** \u2014 %s." % dias(idade))
    g = res.get(ult.get(u"arq"), {})
    ac = g.get(u"acontecendo", [])
    if ac:
        B.append(u"- **O que a \u00faltima reuni\u00e3o afirma** (\u26a0 derivado do resumo, n\u00e3o aprovado \u2014 %d de %d itens):"
                 % (min(6, len(ac)), len(ac)))
        B += [u"  - `%s` %s" % (k, c) for k, c, _ in ac[:6]]
    B += [u"", u"#### \u23ed Por vir", u""]
    pv = g.get(u"por-vir", [])
    ca = g.get(u"compromisso-antigo", [])
    if idade > JANELA:
        B.append(u"\U0001F534 **Nada por vir registrado.** A \u00faltima reuni\u00e3o tem %s; o que ela prometia \u00e9 "
                 u"compromisso de %s, **com cumprimento n\u00e3o verificado**." % (dias(idade), ult[u"data"].isoformat()))
        if ca:
            B += [u"", u"\u231b **O que estava pendente no \u00faltimo contato** (\u26a0 derivado, %d itens):" % len(ca)]
            B += linhas_compromisso(ca[:8])
    elif pv:
        B.append(u"\u26a0 **Compromissos da reuni\u00e3o de %s** \u2014 derivados do resumo, **n\u00e3o aprovados**:" % ult[u"data"].isoformat())
        B += linhas_compromisso(pv)
    else:
        B.append(u"`[a preencher]` \u2014 a \u00faltima reuni\u00e3o (%s) n\u00e3o tem compromisso extra\u00eddo." % ult[u"data"].isoformat())
    B += [FIM]
    bloco = u"\n".join(B)

    if INI in t:
        t = re.sub(re.escape(INI) + u".*?" + re.escape(FIM), lambda m: bloco, t, flags=re.S)
    else:
        a = t.find(u"\n## Marcos da jornada")
        if a == -1:
            return u"sem se\u00e7\u00e3o Marcos"
        b = t.find(u"\n## ", a + 5)
        if b == -1:
            return u"sem se\u00e7\u00e3o seguinte"
        t = t[:b] + u"\n\n" + bloco + u"\n" + t[b:]
    io.open(cam, u"w", encoding=u"utf-8").write(t)
    return u"ok"


# ================================================================ main
def main():
    w = sys.stdout.write
    reunioes, nao_lidos = le_acervo()
    porcli = collections.defaultdict(list)
    for r in reunioes:
        porcli[r[u"slug"]].append(r)
    for linha in porcli.values():
        linha.sort(key=lambda r: (r[u"data"], r[u"titulo"]))

    if not os.path.isdir(INBOX):
        os.makedirs(INBOX)
    tot = collections.Counter()
    porbloco = collections.Counter()
    res = {}
    usados = set()
    for slug, linha in porcli.items():
        st = status_do_corpus(linha[0][u"pasta"])
        for r in linha:
            if not r[u"docx"]:
                continue
            det, etapas, r[u"emails"], r[u"falantes"], r[u"n_falas"] = le_resumo(r[u"docx"])
            if r[u"n_falas"]:
                tot[u"com transcri\u00e7\u00e3o"] += 1
            if etapas:
                tot[u"com pr\u00f3ximas etapas"] += 1
            if det is None:
                tot[u"sem Detalhes"] += 1
            props, t0, t0p, t1 = classifica(det or u"", etapas)
            tot[u"reuni\u00f5es lidas"] += 1
            tot[u"propostas"] += len(props)
            tot[u"T0 descartado"] += len(t0)
            tot[u"T0-P descartado"] += len(t0p)
            tot[u"T1 descartado"] += len(t1)
            if not props and not (t0 or t0p or t1):
                tot[u"reuni\u00f5es sem proposta"] += 1
                continue
            base = u"%s_%s_%s" % (r[u"data"].isoformat(), slug or u"sem-destino", kebab(r[u"titulo"]))
            arq, n = base, 2
            while arq in usados:
                arq = u"%s-%d" % (base, n)
                n += 1
            usados.add(arq)
            r[u"arq"] = arq
            g = escreve_inbox(r, tempo_da(r, linha), props, t0, t0p, t1, st)
            res[arq] = g
            for k, v in g.items():
                porbloco[k] += len(v)

    jorn = []
    for slug, linha in sorted(porcli.items(), key=lambda x: x[0] or u""):
        pasta = linha[0][u"pasta"]
        if pasta:
            jorn.append((pasta, len(linha), escreve_jornada(pasta, linha, status_do_corpus(pasta), res)))

    w(u"=" * 70 + u"\nPROPOSTAS COM EIXO DE TEMPO \u00b7 acervo da Laura\n" + u"=" * 70 + u"\n\n")
    w(u"arquivos no _inbox-calls/ : %d\n" % len(res))
    for k in (u"reuni\u00f5es lidas", u"com transcri\u00e7\u00e3o", u"com pr\u00f3ximas etapas",
              u"reuni\u00f5es sem proposta", u"sem Detalhes",
              u"propostas", u"T0 descartado", u"T0-P descartado", u"T1 descartado"):
        w(u"   %-24s %5d\n" % (k, tot[k]))
    w(u"\nPOR TEMPO\n")
    for k in (u"aconteceu", u"acontecendo", u"por-vir", u"compromisso-antigo"):
        w(u"   %-20s %4d\n" % (k, porbloco[k]))
    w(u"\nJORNADA.MD (linha do tempo)\n")
    for pasta, n, r in jorn:
        w(u"   %-20s %3d reuni\u00f5es \u00b7 %s\n" % (pasta, n, r))
    w(u"\nsem destino no t\u00edtulo: %d reuni\u00f5es\n" % len(porcli.get(None, [])))
    for r in porcli.get(None, []):
        w(u"   %s  %s\n" % (r[u"data"].isoformat(), r[u"titulo"][:60]))
    w(u"N\u00c3O lidos (1:1 internos): %d\n" % len(nao_lidos))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
