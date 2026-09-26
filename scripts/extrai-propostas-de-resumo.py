# -*- coding: utf-8 -*-
u"""
extrai-propostas-de-resumo.py - le os resumos do Gemini dos acervos de reuniao
(Laura Cardoso, Juliana Ferre, ...) e escreve, com o TEMPO como eixo:

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

=== VARIOS ACERVOS, UMA LINHA DO TEMPO ===
A mesma reuniao aparece no acervo de mais de uma pessoa (o evento e um so).
Chave: data + titulo. Cada cliente tem UMA linha do tempo, com a coluna
`Acervo` dizendo de quem veio - um assunto, um dono.

=== DESTINO E NATUREZA SAEM DO E-MAIL (protocolo-entrada-de-call.md \u00a7 4) ===
*"O dominio do e-mail nao mente; o titulo mente."* Com cabecalho `convidado`:
dominio de cliente -> destino com `confianca_destino: alta`, natureza
`externa`; so `@umode.com.br` -> natureza `interna`. Sem cabecalho, o titulo
indica (`media`) e a natureza fica `nao confirmada`. Dois clientes no titulo ->
`baixa`, sem destino: chutar e pior que nao classificar. O mapa dominio ->
cliente e derivado do proprio corpus, nao escrito a mao.

=== O QUE NAO SE LE ===
1:1 e reuniao de dupla interna: registrados como existentes, NAO lidos. O
Vinicius decidiu em 25/09 que material interno entra - mas "o que entra no
repositorio e o criterio, nunca o teor" (`_espec-pipeline` \u00a7 1).
"""
import io, os, re, sys, codecs, collections, zipfile, html, unicodedata, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SCRATCH = (u"C:/Users/Vinicius/AppData/Local/Temp/claude/"
            u"C--Ambientes-Virtuais-BrainHub-brainhub-umode/"
            u"76bedddf-cfb1-4ab7-9d9e-6a5d6536ec9e/scratchpad/")
# (pasta com os arquivos + _mapa.tsv, nome da pessoa, titulos que NAO se leem)
ACERVOS = [
    (_SCRATCH + u"laura2", u"Laura Cardoso",
     (u"victor _ laura", u"ana paula _ laura", u"dupla lala e holmer")),
    (_SCRATCH + u"juliana", u"Juliana Ferr\u00e9",
     (u"victor _ ju _ 1_1", u"saulo _ juliana", u"dupla sinistra",
      u"ana _ juliana - 20")),
    (_SCRATCH + u"marina", u"Marina Santoro",
     (u"dalker _ marina 1_1",)),
]
INBOX = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_inbox-calls")
CLIENTES_DIR = os.path.join(RAIZ, u"uMode", u"_Clientes")
HOJE = datetime.date(2026, 9, 25)
JANELA = 90          # dias: ate aqui, a reuniao mais recente e "acontecendo"
CASA = u"umode.com.br"
PESSOAL = (u"gmail.com", u"hotmail.com", u"outlook.com", u"yahoo.com.br",
           u"yahoo.com", u"icloud.com", u"bol.com.br", u"terra.com.br", u"uol.com.br")

# apelido de titulo -> pasta. So o que o nome da pasta nao cobre sozinho.
APELIDOS = [
    (u"objetiva", u"Moda Objetiva"), (u"lofty", u"Lofty Style"),
    (u"pli[e\u00e9]", u"Plie"), (u"stz", u"Studio Z"), (u"oficina", u"Oficina Reserva"),
    (u"lo?u?ngerie|longerie", u"Loungerie"), (u"colm[e\u00e9]ia", u"Colmeia"),
    (u"lenny", u"Lenny Niemeyer"), (u"ladeira", u"Ladeira Bijuterias"),
    # "NK" sozinho: os proprios titulos alternam "NK Store" e "NK" (acervo Marina)
    (u"nk", u"NK STORE"),
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
# rotulo de falante = nome proprio (1 a 5 palavras capitalizadas). A 1a
# versao aceitava qualquer "xxx: yyy" e pegava trecho de fala ("eu falava").
RE_FALA = re.compile(u"^[ \\t\u00a0]*([A-Z\u00c0-\u00dd][a-z\u00e0-\u00ff'-]+(?: (?:d[aeo]s? )?[A-Z\u00c0-\u00dd][a-z\u00e0-\u00ff'-]+){0,4}): \\S", re.M)
MARCA_TR = u"\U0001F4D6 Transcri"
INI = u"<!-- acervos-reunioes:linha-do-tempo:inicio -->"
FIM = u"<!-- acervos-reunioes:linha-do-tempo:fim -->"
# bloco da 1a versao, so do acervo da Laura: substituido pelo bloco unico
INI_V1 = u"<!-- acervo-laura:linha-do-tempo:inicio -->"
FIM_V1 = u"<!-- acervo-laura:linha-do-tempo:fim -->"


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


def sem_acento(s):
    s = unicodedata.normalize(u"NFKD", s or u"")
    return u"".join(c for c in s if not unicodedata.combining(c)).lower()


def slug_de(pasta):
    return kebab(pasta, 40)


_PADROES = None


def padroes_de_titulo():
    u"""Nome de toda pasta de cliente + apelidos. Mais longo primeiro."""
    global _PADROES
    if _PADROES is None:
        ps = [(re.escape(sem_acento(p)), p) for p in os.listdir(CLIENTES_DIR)
              if not p.startswith(u"_") and os.path.isdir(os.path.join(CLIENTES_DIR, p))]
        ps += [(a, p) for a, p in APELIDOS]
        ps += [(re.escape(sem_acento(a)), p) for a, p in apelidos_do_corpus()]
        _PADROES = sorted(ps, key=lambda x: -len(x[0]))
    return _PADROES


def apelidos_do_corpus():
    u"""
    `### Aliases do cliente` do `institucional.md` de cada pasta - o lugar que
    o CONTEXT.md define para apelido. \U0001F534 Em 25/09 eu escrevi que "nada no
    corpus declara RSV" para a Reserva: estava declarado ali, e eu nao li. O
    extrator passa a ler a fonte em vez de depender de lista a mao.
    So termo entre crases, sem ponto nem arroba (dominio nao e apelido), com
    2+ caracteres; apelido que aparece em mais de um cliente e descartado.
    """
    achados = collections.defaultdict(set)
    for pasta in os.listdir(CLIENTES_DIR):
        f = os.path.join(CLIENTES_DIR, pasta, u"00_Institucional", u"_contexto", u"institucional.md")
        if pasta.startswith(u"_") or not os.path.exists(f):
            continue
        t = io.open(f, encoding=u"utf-8", errors=u"replace").read()
        m = re.search(u"^### Aliases do cliente\\n(.*?)(?=^#)", t, re.S | re.M)
        if not m:
            continue
        # \u26a0 so linha de apelido: o blockquote de aviso cita `Enterprise`
        # (grupo de segmentacao), e "base `Portal do Cliente`" e nome de BASE
        linhas = u"\n".join(l for l in m.group(1).split(u"\n") if not l.lstrip().startswith(u">"))
        linhas = re.sub(u"base \\*{0,2}`[^`]+`", u"", linhas)
        for a in re.findall(u"`([^`\\n]{2,40})`", linhas):
            if u"." in a or u"@" in a or u"[" in a:
                continue
            achados[a.strip()].add(pasta)
    return [(a, list(ps)[0]) for a, ps in achados.items() if len(ps) == 1]


def clientes_no_titulo(nome):
    u"""Pastas citadas no titulo. Trecho ja casado por nome maior nao conta de novo."""
    # separador vira espaco: "Oficina_Reserva" / "Oficina\u00b7Reserva" casava
    # "oficina" E "reserva" - dois clientes, e a reuniao ficava sem destino
    low = re.sub(u"[_\u00b7]+", u" ", sem_acento(nome))
    achados = []
    for pad, pasta in padroes_de_titulo():
        m = re.search(u"(?<![a-z0-9])(%s)(?![a-z0-9])" % pad, low)
        if m and pasta not in achados:
            achados.append(pasta)
            low = low[:m.start()] + u" " * (m.end() - m.start()) + low[m.end():]
    return achados


_DOMINIOS = None


def dominios_de_cliente():
    u"""
    dominio -> pasta, DERIVADO do corpus: todo e-mail citado dentro da pasta de
    um cliente. Dominio em mais de uma pasta fica com a que concentra >= 80%;
    abaixo disso, nao roteia (medido em 25/09: 44 dominios, 2 em duas pastas,
    ambos com maioria clara).
    """
    global _DOMINIOS
    if _DOMINIOS is None:
        cont = collections.defaultdict(collections.Counter)
        for pasta in os.listdir(CLIENTES_DIR):
            if pasta.startswith(u"_"):
                continue
            for dp, _, fs in os.walk(os.path.join(CLIENTES_DIR, pasta)):
                for f in fs:
                    if f.endswith(u".md"):
                        t = io.open(os.path.join(dp, f), encoding=u"utf-8", errors=u"replace").read()
                        for e in RE_E.findall(t):
                            cont[e.split(u"@")[1].lower()][pasta] += 1
        _DOMINIOS = {}
        for d, cs in cont.items():
            if d == CASA or d in PESSOAL:
                continue
            pasta, n = cs.most_common(1)[0]
            if n >= 0.8 * sum(cs.values()):
                _DOMINIOS[d] = pasta
    return _DOMINIOS


_G = None


def _gera_fatos():
    global _G
    if _G is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            u"gera_fatos", os.path.join(RAIZ, u"scripts", u"gera-fatos.py"))
        _G = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_G)
        _G.indice_pessoas()
    return _G


def resolve_cabecalho(texto):
    u"""
    Cabecalho `convidado` SEM e-mail: nomes de exibicao colados por espaco
    ("Ana Paula Ramos Ana Lucia Fernanda Araujo"). \U0001F534 Medido em 25/09:
    34 dos 40 cabecalhos da Juliana sao assim - e eu contei os 34 como "so
    uMode" porque conjunto vazio de dominios passava no teste de subconjunto.

    Segmenta pelo trecho MAIS LONGO (4 a 2 tokens) que resolve para UM e-mail:
      1. nome inteiro no indice do corpus (qualquer pessoa);
      2. so na Casa: primeiro nome igual e TODO outro token do trecho contido
         no nome da ficha (mais estrito que o `_por_token`, para que
         "Ana Paula Ramos Ana" nao engula a Ana seguinte).
    Um token so nunca resolve; ambiguo nunca se escolhe. Sobra vai como esta.
    """
    g = _gera_fatos()
    P = dict((k.replace(u"*", u"").strip(), v) for k, v in g.indice_pessoas().items())
    casa = [(n.split(u" "), es) for n, es in g._CASA_NOMES.items()]
    tk = texto.split()
    ok, sobra, i = [], [], 0
    while i < len(tk):
        for L in range(min(4, len(tk) - i), 1, -1):
            n = g._norm(u" ".join(tk[i:i + L]))
            es = P.get(n)
            if not es:
                p = n.split(u" ")
                es = set()
                for t2, e2 in casa:
                    if t2[0] == p[0] and set(p[1:]) <= set(t2[1:]):
                        es |= e2
            if es and len(es) == 1:
                ok.append((u" ".join(tk[i:i + L]), sorted(es)[0]))
                i += L
                break
        else:
            sobra.append(tk[i])
            i += 1
    return ok, sobra


def roteia(r):
    u"""destino, confianca e natureza - e-mail primeiro, titulo depois."""
    doms = set(e.split(u"@")[1] for e in r.get(u"emails", []))
    doms |= set(e.split(u"@")[1] for _, e in r.get(u"resolvidos", []))
    if r.get(u"sobra"):
        doms.add(u"?")          # alguem no cabecalho nao resolveu: fail-closed
    externos = doms - {CASA, u"?"} - set(PESSOAL)
    desconhecido = u"?" in doms or bool(doms & set(PESSOAL))
    por_email = sorted(set(dominios_de_cliente()[d] for d in externos if d in dominios_de_cliente()))
    por_titulo = clientes_no_titulo(r[u"titulo"])
    if doms and not externos and not desconhecido:
        r[u"natureza"] = u"interna"
    elif externos:
        r[u"natureza"] = u"externa"
    else:
        r[u"natureza"] = u"não confirmada"
    if len(por_email) == 1:
        r[u"pasta"], r[u"conf"] = por_email[0], u"alta"
    elif len(por_titulo) == 1 and not por_email:
        r[u"pasta"], r[u"conf"] = por_titulo[0], u"media"
    elif len(por_email) > 1 or len(por_titulo) > 1:
        r[u"pasta"], r[u"conf"] = None, u"baixa"
    else:
        r[u"pasta"], r[u"conf"] = None, u"baixa"
    if r[u"pasta"]:
        r[u"slug"] = slug_de(r[u"pasta"])
    elif r[u"natureza"] == u"interna" and not por_titulo:
        # reuniao so de umoder, sem cliente no titulo: e da Casa
        r[u"slug"], r[u"conf"] = u"casa", u"alta"
    else:
        r[u"slug"] = None
    r[u"candidatos"] = sorted(set(por_email) | set(por_titulo))


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
    u"""
    Toda reuniao de todos os acervos (docx e chat). A mesma reuniao em dois
    acervos e UMA reuniao: chave = data + titulo.
    """
    reunioes = {}
    nao_lidos = []
    for pasta_acervo, pessoa, nao_ler in ACERVOS:
        if not os.path.isdir(pasta_acervo):
            continue
        for l in io.open(os.path.join(pasta_acervo, u"_mapa.tsv"),
                         encoding=u"utf-8").read().splitlines()[1:]:
            c = l.split(u"\t")
            if len(c) < 2:
                continue
            fn, nome = c[0], c[1]
            if any(k in nome.lower() for k in nao_ler):
                nao_lidos.append((pessoa, nome))
                continue
            md = RE_DATA.search(nome)
            if not md:
                continue
            try:
                d = datetime.date(*(int(x) for x in md.groups()))
            except ValueError:
                continue
            titulo = titulo_limpo(nome)
            k = (d, kebab(titulo, 30))
            r = reunioes.setdefault(k, {u"data": d, u"titulo": titulo,
                                        u"assunto": assunto_de(nome), u"docxs": [],
                                        u"chat": False, u"acervos": set()})
            r[u"acervos"].add(pessoa)
            if fn.endswith(u".docx"):
                r[u"docxs"].append(os.path.join(pasta_acervo, fn))
            else:
                r[u"chat"] = True
        # \U0001F534 GRAVACAO tambem e reuniao. Ate 25/09 so texto entrava, e as
        # 122 reunioes da Marina que so existem em video sumiam da linha do
        # tempo. Titulo e data do arquivo de video sao dado primario.
        vid = os.path.join(pasta_acervo, u"_videos.txt")
        if os.path.exists(vid):
            asr = transcricoes_de(pasta_acervo)
            for nome in io.open(vid, encoding=u"utf-8").read().splitlines():
                if not nome or any(k in nome.lower() for k in nao_ler):
                    continue
                md = RE_DATA.search(nome)
                if not md:
                    continue
                try:
                    d = datetime.date(*(int(x) for x in md.groups()))
                except ValueError:
                    continue
                titulo = titulo_limpo(re.sub(u"\\.mp4$", u"", nome))
                k = (d, kebab(titulo, 30))
                r = reunioes.setdefault(k, {u"data": d, u"titulo": titulo,
                                            u"assunto": assunto_de(nome), u"docxs": [],
                                            u"chat": False, u"acervos": set()})
                r[u"acervos"].add(pessoa)
                r[u"video"] = True
                if nome in asr:
                    r[u"asr"] = asr[nome]
    return list(reunioes.values()), nao_lidos


def transcricoes_de(pasta_acervo):
    u"""
    nome do video -> (transcricao .txt, propostas .json ou None), lendo o
    cabecalho `# <nome>` que o `transcreve-gravacoes.py` escreve.
    """
    d = os.path.join(pasta_acervo, u"transcricoes")
    out = {}
    if not os.path.isdir(d):
        return out
    for f in os.listdir(d):
        if not re.match(u"^\\d{3}\\.txt$", f):
            continue
        cab = io.open(os.path.join(d, f), encoding=u"utf-8").readline()
        if cab.startswith(u"# "):
            pj = os.path.join(d, f[:3] + u".propostas.json")
            out[cab[2:].strip()] = (os.path.join(d, f), pj if os.path.exists(pj) else None)
    return out


def propostas_de_asr(r):
    u"""
    Propostas extraidas da transcricao AUTOMATICA por subagente (JSON). Passam
    pelos MESMOS filtros T0/T0-P/T1 aqui - o subagente e instruido a nao
    escrever sensivel, mas quem garante e este codigo.
    """
    import json
    props, t0, t0p, t1 = [], [], [], []
    tx, pj = r[u"asr"]
    if not pj:
        return None
    for p in json.load(io.open(pj, encoding=u"utf-8")).get(u"propostas", []):
        texto = re.sub(u"\\s+", u" ", p.get(u"texto", u"")).strip()
        ts = p.get(u"ts") or None
        chave = p.get(u"chave")
        if not texto or chave not in (u"decisao", u"entrega", u"dor", u"marco", u"incidente", u"erp", u"processo", u"metrica"):
            continue
        if sensivel(texto, ts, t0, t0p, t1):
            continue
        props.append((chave, corta(texto), ts, bool(p.get(u"futuro")) or chave == u"entrega"))
    return props, t0, t0p, t1


def le_resumo(caminho):
    t = docx(caminho)
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
    # cabecalho so com nomes: guarda o texto para `resolve_cabecalho`
    le_resumo.cab = mc.group(1).strip() if (mc and not emails) else u""
    etapas = proximas_etapas(t, ti)
    if i == -1:
        return None, etapas, emails, falantes, n_falas
    # \U0001F534 o recorte para ANTES da transcricao: fala nao e resumo
    det = t[i + len(u"Detalhes"):(ti if ti > i else len(t))]
    for corte in (u"Próximas etapas sugeridas", u"Suggested next steps",
                  u"Você deve revisar", u"Revise as anota"):
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


_VERIF = None
ISOLAMENTO = [0]   # propostas omitidas por citar outro cliente


def verificacao():
    u"""(arq, id) -> linha da `_verificacao-na-fala.tsv`. Ver aplica-verificacao-na-fala.py."""
    global _VERIF
    if _VERIF is None:
        _VERIF = {}
        f = os.path.join(INBOX, u"_verificacao-na-fala.tsv")
        if os.path.exists(f):
            for l in io.open(f, encoding=u"utf-8").read().splitlines()[1:]:
                c = l.split(u"\t")
                if len(c) == 7:
                    _VERIF[(c[0], c[1])] = c
    return _VERIF


def fora_do_cliente(r, texto):
    u"""
    \U0001F534 Isolamento de cliente (regra travada no CONTEXT.md): proposta
    que cita OUTRO cliente nao entra no registro deste. Verificado em 26/09:
    6 linhas do inbox citavam outro cliente, 2 eram vazamento real
    ("o problema da Osklen" numa reuniao da Lenny). Exige NOME PROPRIO
    (inicial maiuscula), porque "oficina" e "reserva" sao tambem
    substantivos comuns. O que o teste nao pega vai para a tabela de
    verificacao com o veredito `fora_do_cliente`.
    """
    import hashlib
    arq = r.get(u"arq") or u""
    c = verificacao().get((arq, hashlib.sha1((arq + u"|" + texto).encode(u"utf-8")).hexdigest()[:12]))
    if c and c[2] == u"fora_do_cliente":
        return True
    proprio = r.get(u"pasta")
    if not proprio:
        # Casa ou reuniao sem destino: a Casa enxerga todos os clientes, e o
        # isolamento e ENTRE clientes. Filtrar aqui apagava 35 propostas
        # legitimas ("configurar a ficha da NV" numa reuniao interna).
        return False
    ap = {}
    for a, pasta in apelidos_do_corpus():
        ap.setdefault(pasta, []).append(a)
    for pasta in clientes_no_titulo(texto):
        if pasta == proprio:
            continue
        nomes = [pasta] + ap.get(pasta, []) + [pasta.split()[0]]
        if any(n[:1].isupper() and re.search(u"(?<![\\w])%s(?![\\w])" % re.escape(n), texto) for n in nomes):
            return True
    return False


def marca_fala(arq, texto):
    u"""
    Sufixo com o veredito da conferencia contra a fala. \U0001F7E2 `confirmada`
    e o unico que tira a proposta do "o Gemini disse que" - passa a ser "foi
    dito, por X, no minuto Y". Continua PROPOSTA: aprovar segue humano.
    """
    import hashlib
    c = verificacao().get((arq, hashlib.sha1((arq + u"|" + texto).encode(u"utf-8")).hexdigest()[:12]))
    if not c:
        return u""
    quem = (u" \u00b7 " + c[4]) if c[4] else u""
    ts = (u" \u00b7 " + c[3]) if c[3] else u""
    rot = {u"confirmada": u"\U0001F7E2 CONFIRMADA NA FALA",
           u"parcial": u"\u26a0 PARCIAL NA FALA",
           u"contradita": u"\U0001F534 CONTRADITA PELA FALA",
           u"nao_encontrada": u"\u26aa n\u00e3o encontrada na fala"}[c[2]]
    return u" \u00b7 %s (%s%s%s)" % (rot, c[6], quem, ts) if c[2] != u"nao_encontrada" else u" \u00b7 %s" % rot


def dias(n):
    return u"%d dia%s" % (n, u"" if n == 1 else u"s")


# ================================================================ escrita
def escreve_inbox(r, pos, props, t0, t0p, t1, st):
    data = r[u"data"].isoformat()
    tier = u"T0" if (t0 or t0p) else (u"T1" if t1 else u"T2")
    emails, falantes, n_falas = r[u"emails"], r[u"falantes"], r[u"n_falas"]
    tem_tr = n_falas > 0
    status, st_data = st
    cli = r[u"pasta"] or (u"Casa" if r[u"slug"] == u"casa" else u"destino n\u00e3o identificado")
    origem = u"acervo " + u" + ".join(sorted(r[u"acervos"]))

    L = [u"---", u"tipo: registro",
         (u"origem: google-meet \u00b7 grava\u00e7\u00e3o \u00b7 transcri\u00e7\u00e3o autom\u00e1tica (faster-whisper), sem falante"
          if r.get(u"asr") and not r[u"docx"] else
          u"origem: google-meet \u00b7 resumo do Gemini" + (u" + transcri\u00e7\u00e3o" if tem_tr else u"")),
         u"acervo: %s" % origem,
         u'titulo: "%s"' % r[u"titulo"].replace(u'"', u"'"),
         u"data: %s" % data, u"referente_a: %s" % data,
         u"destino: %s" % (r[u"slug"] or u"\"[a preencher]\""),
         u"confianca_destino: %s" % r[u"conf"],
         u"natureza: %s" % (r[u"natureza"] if r[u"natureza"] != u"n\u00e3o confirmada" else u"\"[a preencher]\"")]
    # \U0001F534 e-mail PESSOAL no cabecalho e T0: conta, nao escreve
    pessoais = [e for e in emails if e.split(u"@")[1] in PESSOAL]
    emails = [e for e in emails if e not in pessoais]
    L.append(u"participantes:" if emails else u"participantes: []")
    L += [u"  - %s" % e for e in emails]
    if pessoais:
        L.append(u"participantes_email_pessoal_omitido: %d   # T0, valor nao escrito" % len(pessoais))
    if r.get(u"resolvidos") or r.get(u"sobra"):
        L.append(u"participantes_resolvidos_por_nome:   # cabecalho sem e-mail; indice do corpus")
        L += [u'  - "%s -> %s"' % (n, e) for n, e in r.get(u"resolvidos", [])]
        if r.get(u"sobra"):
            L.append(u'participantes_nao_resolvidos: "%s"' % u" ".join(r[u"sobra"]))
    if falantes:
        L.append(u"participantes_sem_email:")
        L += [u'  - "%s"' % f.replace(u'"', u"'") for f in falantes]
    else:
        L.append(u"participantes_sem_email: []")
    asr = bool(r.get(u"asr")) and not r[u"docx"]
    L += [u"tem_transcricao: %s" % (u"true" if (tem_tr or asr) else u"false"),
          u"transcricao_automatica: %s" % (u"true" if asr else u"false"),
          u"tem_resumo: %s" % (u"false" if asr else u"true"),
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
    if asr:
        L += [u"> **Fonte:** grava\u00e7\u00e3o em v\u00eddeo, %s, **transcrita por m\u00e1quina** (faster-whisper) e lida" % origem,
              u"> por subagente. \u26a0 **Sem falante** \u2014 ningu\u00e9m sabe quem disse cada frase \u2014 e com erro de",
              u"> reconhecimento em nome de campo, sistema e pessoa. **Derivado.** \U0001F534 V\u00eddeo e transcri\u00e7\u00e3o",
              u"> bruta n\u00e3o entram no reposit\u00f3rio."]
    elif tem_tr:
        L += [u"> **Fonte:** resumo do Gemini, %s. \U0001F7E2 **Esta reuni\u00e3o TEM transcri\u00e7\u00e3o de fala** no" % origem,
              u"> `.docx` original \u2014 **%d falas, %d falantes**. As propostas abaixo v\u00eam do **resumo**" % (n_falas, len(falantes)),
              u"> (derivado); **cada uma com minuto \u00e9 confer\u00edvel contra a fala**. \U0001F534 A transcri\u00e7\u00e3o",
              u"> bruta n\u00e3o entra no reposit\u00f3rio."]
    else:
        L += [u"> **Fonte:** resumo do Gemini, %s. \U0001F534 **N\u00e3o h\u00e1 transcri\u00e7\u00e3o de fala desta reuni\u00e3o** \u2014" % origem,
              u"> tudo abaixo foi escrito por um modelo e \u00e9 **derivado**."]
    if r[u"conf"] == u"alta":
        L += [u"> \U0001F7E2 **Destino `%s` saiu do e-mail dos participantes** \u2014 natureza **%s**." % (r[u"slug"], r[u"natureza"])]
    elif r[u"conf"] == u"media":
        L += [u"> \u26a0 **Destino `%s` saiu s\u00f3 do t\u00edtulo:** o t\u00edtulo mente \u2014 pode ser reuni\u00e3o interna *sobre* o cliente." % r[u"slug"]]
    else:
        L += [u"> \U0001F534 **Destino n\u00e3o roteado** \u2014 candidatos: %s. **Rotear exige olho humano.**" % (u", ".join(r[u"candidatos"]) or u"nenhum")]
    L += [
          u"", u"## \u23f1 Posi\u00e7\u00e3o no tempo", u"",
          u"| | |", u"|---|---|",
          u"| Reuni\u00e3o | **%d de %d** de %s nos acervos |" % (pos[u"k"], pos[u"n"], cli),
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
                  else u" \u2014 e **n\u00e3o h\u00e1 reuni\u00e3o posterior nos acervos** onde conferir")]
    if status and status.lower().startswith(u"churn") and pos[u"depois"] == 0:
        L += [u"", u"\U0001F7E2 **Limite temporal do churn:** o corpus diz `%s` (lido em %s) e esta \u00e9 a \u00faltima" % (status, st_data),
              u"reuni\u00e3o do cliente nos acervos. **O cliente estava ativo em %s \u2014 a sa\u00edda foi depois.** A data" % data,
              u"exata segue `[a preencher]`."]

    rot = {u"aconteceu": u"\u2705 Aconteceu \u2014 em %s" % data,
           u"acontecendo": u"\U0001F504 Acontecendo \u2014 \u00faltimo estado conhecido, %s" % data,
           u"por-vir": u"\u23ed Por vir \u2014 compromissos da reuni\u00e3o mais recente",
           u"compromisso-antigo": u"\u231b Compromissos de %s \u2014 cumprimento n\u00e3o verificado" % data}
    grupos = collections.OrderedDict((k, []) for k in
                                     (u"acontecendo", u"por-vir", u"aconteceu", u"compromisso-antigo"))
    fora = 0
    for k, corpo, ts, futuro in props:
        if fora_do_cliente(r, corpo):
            fora += 1
            continue
        grupos[bloco_de(futuro, pos)].append((k, corpo, ts))
    if fora:
        ISOLAMENTO[0] += fora
    L += [u"", u"## \u26a0 Fatos propostos \u2014 ainda N\u00c3O s\u00e3o fatos", u""]
    if not props:
        L += [u"_Nenhuma proposta fora das faixas sens\u00edveis._", u""]
    for g, itens in grupos.items():
        if not itens:
            continue
        L += [u"### %s" % rot[g], u""]
        for k, corpo, ts in itens:
            o = orfao(corpo) if g in (u"por-vir", u"compromisso-antigo") else None
            L.append(u"- %s: %s \u2014 [%s %s%s] \u26a0 PROPOSTA \u00b7 DERIVADA%s%s"
                     % (k, corpo, u"transcri\u00e7\u00e3o autom\u00e1tica" if asr else u"resumo Gemini",
                        data, (u" \u00b7 " + ts) if ts else u"",
                        u" \u00b7 confer\u00edvel na transcri\u00e7\u00e3o" if (tem_tr and ts and ts[0].isdigit()) else u"",
                        (u" \u00b7 \U0001F534 envolve pessoa HOJE desligada (%s)" % o.title()) if o else u"")
                     + marca_fala(r[u"arq"], corpo))
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

    acs = sorted(set(a for r in linha for a in r[u"acervos"]))
    B = [INI, u"### \u23f1 Linha do tempo das reuni\u00f5es \u2014 acervos de reuni\u00e3o", u"",
         u"> **Fonte:** t\u00edtulo e data de cada reuni\u00e3o nos acervos de %s \u2014 **dado prim\u00e1rio**" % u" e ".join(acs),
         u"> (o t\u00edtulo \u00e9 o evento da agenda; n\u00e3o passou por modelo). Conferido em **%s**." % HOJE.strftime(u"%d/%m/%Y"),
         u"> \u26a0 **S\u00e3o acervos de pessoas, n\u00e3o do cliente:** reuni\u00e3o ausente aqui n\u00e3o prova reuni\u00e3o ausente.",
         u"> **Natureza** sai do e-mail do cabe\u00e7alho: `externa` = cliente presente \u00b7 `interna` = s\u00f3 uMode,",
         u"> **sobre** o cliente \u00b7 `n\u00e3o confirmada` = sem cabe\u00e7alho, s\u00f3 o t\u00edtulo indica.",
         u"> \u26a0 **Gerado por `scripts/extrai-propostas-de-resumo.py` \u2014 n\u00e3o editar \u00e0 m\u00e3o.**", u"",
         u"#### \u2705 Aconteceu \u2014 %d reuni\u00f5es, de %s a %s" % (
             len(linha), linha[0][u"data"].isoformat(), ult[u"data"].isoformat()), u"",
         u"| Data | Assunto (do t\u00edtulo) | Natureza | Acervo | Fonte | Propostas no inbox |",
         u"|---|---|---|---|---|---|"]
    for r in linha:
        if r[u"docx"]:
            fonte = u"resumo" + (u" + **transcri\u00e7\u00e3o**" if r.get(u"n_falas") else u"")
        elif r.get(u"asr"):
            fonte = u"v\u00eddeo + transcri\u00e7\u00e3o autom\u00e1tica"
        elif r.get(u"video"):
            fonte = u"\u26a0 **s\u00f3 v\u00eddeo** \u2014 n\u00e3o lido"
        else:
            fonte = u"s\u00f3 chat"
        if r.get(u"arq"):
            n = sum(len(v) for v in res.get(r[u"arq"], {}).values())
            prop = u"[%d](%s%s.md)" % (n, rel, r[u"arq"])
        else:
            prop = u"\u2014"
        B.append(u"| %s | %s | %s | %s | %s | %s |" % (
            r[u"data"].isoformat(), r[u"assunto"], r[u"natureza"],
            u" + ".join(a.split()[0] for a in sorted(r[u"acervos"])), fonte, prop))
    B += [u"", u"#### \U0001F504 Acontecendo \u2014 o \u00faltimo estado conhecido", u"",
          u"- **\u00daltima reuni\u00e3o nos acervos:** %s \u2014 *%s* \u2014 **%s atr\u00e1s**." % (
              ult[u"data"].isoformat(), ult[u"titulo"], dias(idade)),
          u"- **Status no corpus:** %s." % (
              (u"`%s` \u2014 varredura de %s (data da **leitura**, n\u00e3o da transi\u00e7\u00e3o)" % (status, st_data))
              if status else u"`[a preencher]`")]
    quem = [u"`%s`" % e for e in ult.get(u"emails", []) if e.split(u"@")[1] not in PESSOAL]
    quem += [n for n, _ in ult.get(u"resolvidos", [])]
    quem += [f for f in ult.get(u"falantes", []) if f not in quem]
    if quem:
        B.append(u"- **Quem esteve na \u00faltima reuni\u00e3o:** %s." % u" \u00b7 ".join(quem))
    s = (status or u"").lower()
    if s.startswith(u"churn"):
        B.append(u"- \U0001F7E2 **Limite do churn:** o cliente estava em reuni\u00e3o em **%s**; a sa\u00edda foi **depois**"
                 u" disso e **antes de %s**. Data exata `[a preencher]`." % (ult[u"data"].isoformat(), st_data))
    elif idade > 180:
        B.append(u"- \U0001F534 **`%s` no corpus e %s sem reuni\u00e3o nos acervos.** N\u00e3o prova abandono \u2014"
                 u" a conta pode estar com outra pessoa \u2014 **mas \u00e9 a pergunta a fazer.**" % (status or u"?", dias(idade)))
    elif idade <= JANELA:
        B.append(u"- \U0001F7E2 **Coerente:** status ativo e reuni\u00e3o h\u00e1 %s." % dias(idade))
    else:
        B.append(u"- \u26a0 **Entre 3 e 6 meses sem reuni\u00e3o nos acervos** \u2014 %s." % dias(idade))
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

    if INI_V1 in t:
        t = re.sub(re.escape(INI_V1) + u".*?" + re.escape(FIM_V1), lambda m: bloco, t, flags=re.S)
    elif INI in t:
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


CASA_JORNADA = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_contexto", u"jornada.md")


def escreve_jornada_casa(linha, res):
    u"""
    Linha do tempo da CASA no `jornada.md` dela (decisao do Vinicius, 25/09).
    ⏱ Diferente do cliente: a Casa tem SERIES paralelas (Migracao, K.A.FE,
    Reconhecimento do Novo Sistema). "Acontecendo" e por serie - a serie cuja
    ultima reuniao tem ate JANELA dias.
    """
    if not os.path.exists(CASA_JORNADA):
        return u"sem jornada.md da Casa"
    t = io.open(CASA_JORNADA, encoding=u"utf-8").read()
    rel = u"../_inbox-calls/"
    series = collections.OrderedDict()
    for r in sorted(linha, key=lambda r: r[u"data"]):
        series.setdefault(kebab(r[u"titulo"], 30), []).append(r)
    ordem = sorted(series.values(), key=lambda v: v[-1][u"data"], reverse=True)

    B = [INI, u"### ⏱ Linha do tempo das reuniões da Casa — acervos de reunião", u"",
         u"> **Fonte:** título e data de cada reunião **interna confirmada** (cabeçalho só com",
         u"> gente da uMode) nos acervos de %s — **dado primário**. Conferido em **%s**." % (
             u" e ".join(sorted(set(a for r in linha for a in r[u"acervos"])) ), HOJE.strftime(u"%d/%m/%Y")),
         u"> ⚠ **Só reunião com cabeçalho entra aqui.** A série `Hora do K.A.FÉ`, por exemplo, tem",
         u"> mais sessões sem cabeçalho — elas ficam `não confirmada`, fora da Casa.",
         u"> ⚠ **Gerado por `scripts/extrai-propostas-de-resumo.py` — não editar à mão.**", u"",
         u"#### ✅ Aconteceu — %d reuniões em %d séries" % (len(linha), len(series)), u"",
         u"| Série (do título) | Reuniões | Primeira | Última | Propostas no inbox |",
         u"|---|---:|---|---|---|"]
    for v in ordem:
        links = u" · ".join(u"[%s](%s%s.md)" % (r[u"data"].strftime(u"%d/%m"), rel, r[u"arq"])
                                for r in v if r.get(u"arq"))
        B.append(u"| %s | %d | %s | %s | %s |" % (
            v[0][u"titulo"], len(v), v[0][u"data"].isoformat(), v[-1][u"data"].isoformat(), links or u"—"))
    vivas = [v for v in ordem if (HOJE - v[-1][u"data"]).days <= JANELA]
    B += [u"", u"#### \U0001F504 Acontecendo — séries com reunião nos últimos %d dias" % JANELA, u""]
    if vivas:
        for v in vivas:
            B.append(u"- **%s** — %d reunião(ões), a última em **%s** (%s atrás)." % (
                v[0][u"titulo"], len(v), v[-1][u"data"].isoformat(), dias((HOJE - v[-1][u"data"]).days)))
    else:
        B.append(u"\U0001F534 **Nenhuma série com reunião nos últimos %d dias.**" % JANELA)
    B += [u"", u"#### ⏭ Por vir — compromissos da última reunião de cada série viva", u"",
          u"⚠ **Derivados do resumo do Gemini, não aprovados.** Cada linha aponta o arquivo do inbox.", u""]
    total = 0
    for v in vivas:
        u_ = v[-1]
        pv = res.get(u_.get(u"arq"), {}).get(u"por-vir", [])
        if not pv:
            continue
        total += len(pv)
        B.append(u"**%s** — %s · [%d compromissos](%s%s.md)" % (
            u_[u"titulo"], u_[u"data"].isoformat(), len(pv), rel, u_[u"arq"]))
        B += linhas_compromisso(pv[:5])
        if len(pv) > 5:
            B.append(u"- … e mais %d no arquivo." % (len(pv) - 5))
        B.append(u"")
    if not total:
        B.append(u"`[a preencher]` — nenhuma série viva tem compromisso extraído.")
    B += [FIM]
    bloco = u"\n".join(B)
    if INI in t:
        t = re.sub(re.escape(INI) + u".*?" + re.escape(FIM), lambda m: bloco, t, flags=re.S)
    else:
        a = t.find(u"\n## Marcos da jornada")
        b = t.find(u"\n## ", a + 5) if a != -1 else -1
        if b == -1:
            return u"sem seção Marcos"
        t = t[:b] + u"\n\n" + bloco + u"\n" + t[b:]
    io.open(CASA_JORNADA, u"w", encoding=u"utf-8").write(t)
    return u"ok · %d séries · %d vivas · %d compromissos" % (len(series), len(vivas), total)


# ================================================================ main
def main():
    w = sys.stdout.write
    reunioes, nao_lidos = le_acervo()

    # 1 - le o resumo (o maior .docx, se a reuniao veio em mais de um acervo)
    #     e roteia pelo e-mail ANTES de montar a linha do tempo
    lidos = {}
    for r in reunioes:
        r[u"emails"], r[u"falantes"], r[u"n_falas"] = [], [], 0
        if r[u"docxs"]:
            r[u"docx"] = max(r[u"docxs"], key=os.path.getsize)
            det, etapas, r[u"emails"], r[u"falantes"], r[u"n_falas"] = le_resumo(r[u"docx"])
            lidos[id(r)] = (det, etapas)
            if le_resumo.cab:
                r[u"resolvidos"], r[u"sobra"] = resolve_cabecalho(le_resumo.cab)
        else:
            r[u"docx"] = None
        roteia(r)

    porcli = collections.defaultdict(list)
    for r in reunioes:
        porcli[r[u"slug"]].append(r)
    for linha in porcli.values():
        linha.sort(key=lambda r: (r[u"data"], r[u"titulo"]))

    if not os.path.isdir(INBOX):
        os.makedirs(INBOX)
    tot = collections.Counter()
    poracervo = collections.Counter()
    pornat = collections.Counter()
    porbloco = collections.Counter()
    res = {}
    usados = set()
    for slug, linha in porcli.items():
        st = status_do_corpus(linha[0][u"pasta"])
        for r in linha:
            pornat[r[u"natureza"]] += 1
            if r.get(u"video"):
                tot[u"com grava\u00e7\u00e3o"] += 1
            if not r[u"docx"]:
                pa = propostas_de_asr(r) if r.get(u"asr") else None
                if not pa:
                    continue
                props, t0, t0p, t1 = pa
                tot[u"transcri\u00e7\u00e3o autom\u00e1tica lida"] += 1
                tot[u"propostas"] += len(props)
                if not props and not (t0 or t0p or t1):
                    continue
                base = u"%s_%s_%s" % (r[u"data"].isoformat(), slug or u"sem-destino", kebab(r[u"titulo"]))
                arq, n = base, 2
                while arq in usados:
                    arq = u"%s-%d" % (base, n)
                    n += 1
                usados.add(arq)
                r[u"arq"] = arq
                ref = linha
                if slug == u"casa":
                    ref = [x for x in linha if kebab(x[u"titulo"], 30) == kebab(r[u"titulo"], 30)]
                g = escreve_inbox(r, tempo_da(r, ref), props, t0, t0p, t1, st)
                res[arq] = g
                for k, v in g.items():
                    porbloco[k] += len(v)
                continue
            det, etapas = lidos[id(r)]
            for a in r[u"acervos"]:
                poracervo[a] += 1
            if r[u"n_falas"]:
                tot[u"com transcrição"] += 1
            if etapas:
                tot[u"com próximas etapas"] += 1
            if len(r[u"acervos"]) > 1:
                tot[u"em mais de um acervo"] += 1
            props, t0, t0p, t1 = classifica(det or u"", etapas)
            tot[u"reuniões lidas"] += 1
            tot[u"propostas"] += len(props)
            tot[u"T0 descartado"] += len(t0)
            tot[u"T0-P descartado"] += len(t0p)
            tot[u"T1 descartado"] += len(t1)
            if not props and not (t0 or t0p or t1):
                tot[u"reuniões sem proposta"] += 1
                continue
            base = u"%s_%s_%s" % (r[u"data"].isoformat(), slug or u"sem-destino", kebab(r[u"titulo"]))
            arq, n = base, 2
            while arq in usados:
                arq = u"%s-%d" % (base, n)
                n += 1
            usados.add(arq)
            r[u"arq"] = arq
            # ⏱ Casa tem series paralelas (Migracao, K.A.FE, CriAi): o
            # "mais recente" e da SERIE, nao da Casa inteira
            ref = linha
            if slug == u"casa":
                ref = [x for x in linha if kebab(x[u"titulo"], 30) == kebab(r[u"titulo"], 30)]
            g = escreve_inbox(r, tempo_da(r, ref), props, t0, t0p, t1, st)
            res[arq] = g
            for k, v in g.items():
                porbloco[k] += len(v)

    jorn = []
    if porcli.get(u"casa"):
        jorn.append((u"Casa", len(porcli[u"casa"]), escreve_jornada_casa(porcli[u"casa"], res)))
    for slug, linha in sorted(porcli.items(), key=lambda x: x[0] or u""):
        pasta = linha[0][u"pasta"]
        if pasta:
            jorn.append((pasta, len(linha), escreve_jornada(pasta, linha, status_do_corpus(pasta), res)))

    w(u"=" * 70 + u"\nPROPOSTAS COM EIXO DE TEMPO · %s\n" % u" + ".join(a[1] for a in ACERVOS) + u"=" * 70 + u"\n\n")
    w(u"reuniões distintas     : %d\n" % len(reunioes))
    w(u"arquivos no _inbox-calls/ : %d\n" % len(res))
    for k in (u"reuniões lidas", u"com gravação", u"transcrição automática lida", u"em mais de um acervo", u"com transcrição", u"com próximas etapas",
              u"reuniões sem proposta", u"propostas", u"T0 descartado", u"T0-P descartado", u"T1 descartado"):
        w(u"   %-24s %5d\n" % (k, tot[k]))
    w(u"\nPOR ACERVO (resumos lidos)\n")
    for k, v in poracervo.most_common():
        w(u"   %-24s %4d\n" % (k, v))
    w(u"\nPOR NATUREZA (todas as reuniões)\n")
    for k, v in pornat.most_common():
        w(u"   %-24s %4d\n" % (k, v))
    w(u"\nPOR TEMPO\n")
    for k in (u"aconteceu", u"acontecendo", u"por-vir", u"compromisso-antigo"):
        w(u"   %-20s %4d\n" % (k, porbloco[k]))
    w(u"\nJORNADA.MD (linha do tempo)\n")
    for pasta, n, r in jorn:
        w(u"   %-20s %3d reuniões · %s\n" % (pasta, n, r))
    w(u"\ncasa: %d reuniões · sem destino: %d\n" % (len(porcli.get(u"casa", [])), len(porcli.get(None, []))))
    amb = [r for r in porcli.get(None, []) if len(r[u"candidatos"]) > 1]
    for r in amb:
        w(u"   ⚠ ambígua %s  %s -> %s\n" % (r[u"data"].isoformat(), r[u"titulo"][:50], u" / ".join(r[u"candidatos"])))
    w(u"omitidas por citar OUTRO cliente (isolamento): %d\n" % ISOLAMENTO[0])
    w(u"NÃO lidos (1:1 e dupla interna): %d\n" % len(nao_lidos))
    for p, n in nao_lidos:
        w(u"   %s · %s\n" % (p, n[:60]))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
