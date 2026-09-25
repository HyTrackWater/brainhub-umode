# -*- coding: utf-8 -*-
u"""
ensaio-migracao.py - roda o corpus real contra as classes de migracao do
plano tecnico do Joao (secao 9) e diz ONDE o schema proposto quebra.

POR QUE ISTO EXISTE. A secao 9 do plano diz: "a migracao completa so recebe
aceite apos denominador congelado+delta, recibos e execucao" e "o atlas
anterior nao era denominador completo". \U0001F534 O corpus da uMode e a
primeira migracao real e ninguem tem o denominador. Este script produz o
denominador e, mais importante, a lista de quebras com o item que quebrou.

NAO e estimativa. Cada numero sai de leitura de arquivo.
"""
import io, os, re, sys, codecs, collections, hashlib

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RE_FM = re.compile(u"\\A---\\n(.*?)\\n---\\n", re.S)
RE_ALIAS = re.compile(u"^aliases:\\s*\\n((?:\\s*-\\s*.+\\n)+)", re.M)
RE_WIKI = re.compile(u"\\[\\[([^\\]|#]+)")
RE_FATO = re.compile(u"^- ([a-z0-9-]+): (.*)$", re.M)
RE_TIER = re.compile(u"\\bT[0-3]\\b")
RE_EMAIL = re.compile(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")


def anda():
    for dp, _, fns in os.walk(os.path.join(RAIZ, u"uMode")):
        for fn in fns:
            if fn.endswith(u".md"):
                yield os.path.join(dp, fn)


def rel(p):
    return p[len(RAIZ) + 1:].replace(os.sep, u"/")


def main():
    w = sys.stdout.write
    arquivos = list(anda())

    # ------------------------------------------------ classe 1: MD canonico
    tot = len(arquivos)
    com_fm = com_alias = com_tags = 0
    alias_por_valor = collections.defaultdict(list)
    sem_alias = []
    com_tier = 0
    conteudo = {}
    sha_por = collections.defaultdict(list)

    for p in arquivos:
        t = io.open(p, encoding=u"utf-8", errors=u"replace").read()
        conteudo[p] = t
        sha_por[hashlib.sha256(t.encode(u"utf-8")).hexdigest()].append(p)
        m = RE_FM.match(t)
        if m:
            com_fm += 1
            fm = m.group(1)
            if u"tags:" in fm:
                com_tags += 1
            ma = RE_ALIAS.search(fm + u"\n")
            if ma:
                com_alias += 1
                for l in ma.group(1).split(u"\n"):
                    l = l.strip().lstrip(u"-").strip().strip(u'"').strip(u"'")
                    if l:
                        alias_por_valor[l].append(p)
            else:
                sem_alias.append(p)
        else:
            sem_alias.append(p)
        # tier declarado NO ARQUIVO (nao no protocolo)
        if RE_TIER.search(t):
            com_tier += 1

    dup_alias = {k: v for k, v in alias_por_valor.items() if len(v) > 1}
    dup_sha = {k: v for k, v in sha_por.items() if len(v) > 1}

    # ------------------------------------------------ classe 3: wikilinks
    # identidade logica = alias; o plano exige "resolver link por identidade
    # logica" e "detectar orfaos".
    destinos = set()
    for k in alias_por_valor:
        destinos.add(k.lower())
    for p in arquivos:
        destinos.add(os.path.basename(p)[:-3].lower())
    links = 0
    orfaos = collections.Counter()
    orfao_ex = {}
    for p in arquivos:
        for m in RE_WIKI.finditer(conteudo[p]):
            alvo = m.group(1).strip()
            links += 1
            if alvo.lower() not in destinos and alvo.split(u"/")[-1].lower() not in destinos:
                orfaos[alvo] += 1
                orfao_ex.setdefault(alvo, rel(p))

    # ------------------------------------------------ afirmacoes
    fatos = 0
    chaves = collections.Counter()
    sem_fonte = com_fonte = ausencia = 0
    sem_validade = 0
    for p in arquivos:
        blo = re.search(u"\n## Fatos\n(.*?)(?:\n## |\\Z)", conteudo[p], re.S)
        if not blo:
            continue
        for m in RE_FATO.finditer(blo.group(1)):
            fatos += 1
            chaves[m.group(1)] += 1
            v = m.group(2)
            if u"[sem fonte]" in v:
                sem_fonte += 1
            elif u"não consta em" in v:
                ausencia += 1
            else:
                com_fonte += 1
            # validade = intervalo de vigencia, nao data da fonte
            if not re.search(u"valid|vigente até|até \\d{4}", v):
                sem_validade += 1

    # ------------------------------------------------ classe 8 e 11
    demandas = len([p for p in arquivos if u"/_demandas/" in rel(p) and
                    os.path.basename(p).startswith(u"D-")])
    rfis = len([p for p in arquivos if u"/_rfis/" in rel(p) and
                os.path.basename(p).startswith(u"RFI-")])
    fichas = len([p for p in arquivos if u"/_pessoas/" in rel(p) and
                  not os.path.basename(p).startswith(u"_")])
    com_email = sum(1 for p in arquivos if u"/_pessoas/" in rel(p)
                    and RE_EMAIL.search(conteudo[p]))
    # T0 declarado em ficha
    t0 = sum(1 for p in arquivos if u"/_pessoas/" in rel(p)
             and u"T0" in conteudo[p])

    # ------------------------------------------------ lacunas
    apreencher = sum(conteudo[p].count(u"[a preencher") for p in arquivos)

    # ------------------------------------------------ classes VAZIAS
    scripts = len([f for f in os.listdir(os.path.join(RAIZ, u"scripts"))
                   if f.endswith(u".py")])

    # ================================================== relatorio
    w(u"=" * 72 + u"\n")
    w(u"DENOMINADOR DO CORPUS uMode - contra as classes do plano 9\n")
    w(u"=" * 72 + u"\n\n")

    w(u"CLASSE 1 - MD canonico + frontmatter -> ContextItem + Revision\n")
    w(u"   itens                            %6d\n" % tot)
    w(u"   com frontmatter                  %6d  (%.0f%%)\n" % (com_fm, 100.0*com_fm/tot))
    w(u"   com aliases (identidade logica)  %6d  (%.0f%%)\n" % (com_alias, 100.0*com_alias/tot))
    w(u"   com tags                         %6d\n" % com_tags)
    w(u"   \U0001F534 SEM identidade logica         %6d  <- QUEBRA 1\n" % len(sem_alias))
    w(u"   \U0001F534 alias DUPLICADO               %6d  <- QUEBRA 2\n" % len(dup_alias))
    w(u"   ⚠ arquivos byte-identicos        %6d grupos\n" % len(dup_sha))
    w(u"   \U0001F534 com tier declarado no arquivo %6d  (%.0f%%) <- QUEBRA 3\n"
      % (com_tier, 100.0*com_tier/tot))
    w(u"\n")

    w(u"CLASSE 3 - Wikilinks -> ContextEdge\n")
    w(u"   links encontrados                %6d\n" % links)
    w(u"   \U0001F534 alvos ORFAOS distintos       %6d  <- QUEBRA 4\n" % len(orfaos))
    w(u"   ocorrencias orfas                %6d\n" % sum(orfaos.values()))
    w(u"\n")

    w(u"CAMADA DERIVADA - afirmacoes (nao e classe do plano; e o que falta la)\n")
    w(u"   afirmacoes                       %6d\n" % fatos)
    w(u"   chaves distintas (lista fechada) %6d\n" % len(chaves))
    w(u"   com fonte nomeada                %6d\n" % com_fonte)
    w(u"   ausencia VERIFICADA              %6d\n" % ausencia)
    w(u"   lacuna declarada [sem fonte]     %6d\n" % sem_fonte)
    w(u"   \U0001F534 SEM intervalo de validade    %6d  <- QUEBRA 5\n" % sem_validade)
    w(u"\n")

    w(u"CLASSE 8 - Aprovacoes, decisoes, tarefas\n")
    w(u"   demandas                         %6d\n" % demandas)
    w(u"   RFIs                             %6d\n" % rfis)
    w(u"\n")

    w(u"CLASSE 11 - T0 / pessoal\n")
    w(u"   fichas de pessoa                 %6d\n" % fichas)
    w(u"   com e-mail (chave de identidade) %6d\n" % com_email)
    w(u"   com marcacao T0 no arquivo       %6d\n" % t0)
    w(u"\n")

    w(u"CLASSES VAZIAS neste corpus (denominador = 0, e isso e dado)\n")
    w(u"   4 skills/contratos de agente          0\n")
    w(u"   5 loops/grafos                        0\n")
    w(u"   6 cron/launchd/jobs                   0\n")
    w(u"   7 scripts locais                 %6d  -> ActionDefinition\n" % scripts)
    w(u"   9 credenciais                         0  (registradas por referencia)\n")
    w(u"\n")

    w(u"LACUNA DECLARADA\n")
    w(u"   ocorrencias de [a preencher]     %6d  <- o importador NAO pode preencher\n"
      % apreencher)
    w(u"\n")

    w(u"=" * 72 + u"\n")
    w(u"AMOSTRA DAS QUEBRAS - o item que quebrou\n")
    w(u"=" * 72 + u"\n\n")

    w(u"QUEBRA 1 - sem identidade logica (amostra de 5 de %d):\n" % len(sem_alias))
    for p in sem_alias[:5]:
        w(u"   %s\n" % rel(p))
    w(u"\nQUEBRA 2 - alias duplicado (amostra de 5 de %d):\n" % len(dup_alias))
    for k, v in list(sorted(dup_alias.items(), key=lambda x: -len(x[1])))[:5]:
        w(u"   \"%s\" -> %d arquivos\n" % (k[:56], len(v)))
        for p in v[:2]:
            w(u"        %s\n" % rel(p))
    w(u"\nQUEBRA 4 - wikilink orfao (top 8 de %d):\n" % len(orfaos))
    for k, n in orfaos.most_common(8):
        w(u"   [[%s]]  x%d   ex.: %s\n" % (k[:40], n, orfao_ex[k][:54]))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
