# -*- coding: utf-8 -*-
u"""
desambigua-apelido-atendimento.py - Fase 0, item 1 (fecho): troca apelido
ambiguo por nome completo na secao de atendimento, quando OUTRA fonte, para o
MESMO cliente, diz quem e.

O PROBLEMA. O campo `Atendimento 2025` do CRM guarda apelido: `Julianne &
Pedro`. \U0001F534 `Pedro` nao identifica ninguem - ha `pedro.murillo@` e
`pedro.silva@` nas fichas da Casa. O `gera-fatos.py` faz a coisa certa e
devolve `[ambiguo]`, porque escolher seria inventar.

A SAIDA, e ela NAO e afrouxar a regra. E trazer um SEGUNDO SINAL: a base
`Demandas de Clientes` guarda `Key Account/Responsavel` com NOME COMPLETO -
`Pedro Murillo` - e por cliente. Entao:

    apelido ambiguo no cliente X
  + exatamente UMA pessoa com aquele primeiro nome nas demandas do cliente X
  = desambiguado, com as duas fontes citadas

\u26a0 **Se mais de uma pessoa do mesmo primeiro nome aparecer nas demandas
daquele cliente, NAO resolve.** Duas fontes que nao convergem nao viram uma
certeza - viram uma pendencia.

\U0001F534 E o escopo e por CLIENTE, sempre. Resolver `Pedro` no cliente X com
evidencia do cliente Y e exatamente a falha que ja casou o falante `Juliana`
da CAEDU com `juliana@osklen.com.br`.

Este script tambem nao escreve e-mail: escreve NOME. Quem resolve para e-mail
segue sendo o `gera-fatos.py`, dono unico do bloco `## Fatos`.
"""
import csv, io, os, re, sys, codecs, collections, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = (u"C:/Ambientes Virtuais/BrainHub - Jo\u00e3o Risol\u00e9o/umode-os-vault/"
     u"BrainHub/uMode/_Clientes/_geral/notion/")
HOJE = u"25/09/2026"
SEC = u"### Respons\u00e1vel de atendimento (uMode)"


def norm(s):
    s = unicodedata.normalize(u"NFKD", (s or u"").strip().lower())
    return u"".join(c for c in s if not unicodedata.combining(c))


def sem_url(s):
    return re.sub(u"\\s*\\(https?://[^)]*\\)", u"", s or u"").strip()


def main():
    # nomes completos por cliente, vindos das demandas
    dem = collections.defaultdict(collections.Counter)
    for x in csv.DictReader(io.open(V + u"Demandas de Clientes.csv",
                                    encoding=u"utf-8-sig", newline=u"")):
        c = sem_url(x.get(u"\U0001F465 Clientes"))
        ka = (x.get(u"Key Account/Respons\u00e1vel") or u"").strip()
        if not c or not ka:
            continue
        for p in [p.strip() for p in ka.split(u",") if p.strip()]:
            if len(norm(p).split()) >= 2:
                dem[c][p] += 1

    base = os.path.join(RAIZ, u"uMode", u"_Clientes")
    trocas, recusas = [], []
    for cliente in sorted(os.listdir(base)):
        if cliente.startswith(u"_"):
            continue
        p = os.path.join(base, cliente, u"00_Institucional", u"_contexto",
                         u"institucional.md")
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding=u"utf-8").read()
        amb = [l for l in re.findall(u"^- atendimento: (.*)$", txt, re.M)
               if u"ambiguo" in l]
        if not amb:
            continue
        gov = txt.find(u"\n## Governan\u00e7a")
        i = txt.find(u"\n" + SEC + u"\n")
        if i == -1 or (gov != -1 and i > gov):
            continue
        ini = i + len(SEC) + 2
        fim = len(txt)
        for h in (u"\n## ", u"\n### "):
            j = txt.find(h, ini)
            if j != -1:
                fim = min(fim, j)
        corpo = txt[ini:fim]

        mudou = False
        for linha in amb:
            apelido = linha.split(u" \u2014 ")[0].strip()
            if len(norm(apelido).split()) != 1:
                continue
            alvo = norm(apelido)
            cands = set()
            for nome in dem.get(cliente, {}):
                if norm(nome).split()[0] == alvo:
                    cands.add(nome)
            if len(cands) != 1:
                recusas.append((cliente, apelido,
                                u"%d candidatos nas demandas deste cliente" % len(cands)))
                continue
            completo = sorted(cands)[0]
            # troca a ocorrencia do apelido SOLTO no corpo da secao
            novo, n = re.subn(u"(?<![\\w\u00c0-\u00ff])" + re.escape(apelido) +
                              u"(?![\\w\u00c0-\u00ff])", completo, corpo)
            if not n:
                recusas.append((cliente, apelido, u"apelido n\u00e3o achado na se\u00e7\u00e3o"))
                continue
            corpo = novo
            trocas.append((cliente, apelido, completo))
            mudou = True

        if mudou:
            nota = (u"\n> \U0001F7E2 **Apelido desambiguado em %s:** o r\u00f3tulo do CRM trazia s\u00f3 o "
                    u"primeiro nome, que **n\u00e3o identifica** \u2014 o nome completo veio da base "
                    u"`Demandas de Clientes` \u00b7 `Key Account/Respons\u00e1vel`, **deste mesmo "
                    u"cliente**.\n> \u26a0 **Duas fontes; nenhuma delas resolveria sozinha.**\n"
                    % HOJE)
            io.open(p, u"w", encoding=u"utf-8").write(txt[:ini] + corpo.rstrip() +
                                                      u"\n" + nota + txt[fim:])

    w = sys.stdout.write
    w(u"\U0001F7E2 apelidos desambiguados: %d\n" % len(trocas))
    for c, a, n in trocas:
        w(u"   %-20s %-10s \u2192 %s\n" % (c[:20], a, n))
    w(u"\n\u26a0 recusados (segunda fonte n\u00e3o convergiu): %d\n" % len(recusas))
    for c, a, m in recusas:
        w(u"   %-20s %-10s %s\n" % (c[:20], a, m))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
