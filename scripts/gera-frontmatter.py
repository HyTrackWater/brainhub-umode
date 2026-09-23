# -*- coding: utf-8 -*-
u"""gera-frontmatter.py - dono unico do frontmatter YAML de todo .md do corpus.

Escreve dois campos, e so esses dois:

  aliases  - copiado do H1. Existe porque o Obsidian rotula nota pelo NOME DO
             ARQUIVO, e o padrao deste corpus manda que todo MD do mesmo tipo
             tenha o mesmo nome: sao 694 `contexto-area.md`, 50 `institucional.md`.
             Na busca rapida isso virava uma parede de nomes iguais.

  tags     - `tipo/`, `cliente/`, `status/` e `area/`. Existe porque o Vinicius
             perguntou em 23 set 2026 como filtrar so os clientes ativos da uMode
             e nao havia resposta. Com tag ha: o grafo do Obsidian aceita
             `tag:#status/ongoing` tanto na busca quanto nos grupos de cor.

ORDEM NO RITUAL - IMPORTA
Rodar SEMPRE DEPOIS do `gera-conexoes.py`, que reescreve os ~60 `_indice.md` do
zero e apaga o frontmatter deles. Nao e destrutivo - este script devolve - mas
invertendo a ordem os indices ficam sem frontmatter ate a rodada seguinte.

SEGURANCA
- Nao renomeia arquivo. Nao toca em link. Nao altera o corpo do documento.
- Idempotente. Reversivel com `--remove`.
- O `status/` NAO e inventado: sai do `### Status atual` do `institucional.md`
  daquele cliente. Cliente sem status declarado fica sem a tag.
"""
import io, os, re, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORA = {".git", "__pycache__", ".obsidian"}
FM = re.compile(u"^---\r?\n.*?\r?\n---\r?\n", re.S)

def slug(s):
    s = unicodedata.normalize(u"NFKD", s or u"").encode(u"ascii", u"ignore").decode()
    return re.sub(u"-+", u"-", re.sub(u"[^a-z0-9]+", u"-", s.lower())).strip(u"-")

def arquivos():
    for dp, dn, fn in os.walk(RAIZ):
        dn[:] = [d for d in dn if d not in IGNORA]
        for f in fn:
            if f.endswith(u".md"):
                yield os.path.join(dp, f)

def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, u"/")

def h1_de(txt):
    # O BOM no inicio do arquivo fazia startswith falhar em silencio.
    for l in txt.lstrip(u"\ufeff").split(u"\n")[:40]:
        s = l.strip().lstrip(u"\ufeff")
        if s.startswith(u"# "):
            return re.sub(u"\\s+", u" ", s[2:].strip())
    return None

def tipo_de(r, nome):
    if u"_template" in r:                                   return u"template"
    if nome == u"_indice.md":                               return u"indice"
    if r.startswith(u"brainwave/"):                         return u"frente-brainwave"
    if u"/_boilerplate/" in r:                              return u"frente-boilerplate"
    if u"/_inbox-hermes/" in r:                             return u"frente-hermes"
    if u"/" not in r:                                       return u"governanca"
    if nome == u"institucional.md":                         return u"institucional"
    if nome == u"jornada.md":                               return u"jornada"
    if nome == u"pessoas.md":                               return u"pessoas"
    if nome == u"contexto-area.md":                         return u"area"
    if nome == u"integracao.md":                            return u"integracao"
    if nome == u"_pendencias-e-fontes.md":                  return u"diario"
    if nome == u"produto.md":                               return u"solucao"
    # `agente-*` e entidade que AINDA NAO tem ficha propria (o AGORA.md conta 0),
    # mas ja tem arquivo. Tipar agora deixa o grafo mostrar o que existe.
    if u"/agente-" in r or nome.startswith(u"agente-"): return u"agente"
    if u"/_pessoas/" in r:                                  return u"pessoa"
    if u"/_demandas/" in r:                                 return u"demanda"
    if u"/_rfis/" in r:                                     return u"rfi"
    if u"/_ferramentas/" in r:                              return u"ferramenta"
    if u"/_protocolos/" in r:                               return u"protocolo"
    if re.search(u"/(_varredura|_levantamento|_recebido)", r): return u"registro"
    if u"/_contexto/_" in r:                                return u"autoridade"
    return u"outro"

def status_por_cliente():
    base = os.path.join(RAIZ, u"uMode", u"_Clientes")
    out = {}
    if not os.path.isdir(base):
        return out
    for c in os.listdir(base):
        if c.startswith(u"_"):
            continue
        p = os.path.join(base, c, u"00_Institucional", u"_contexto", u"institucional.md")
        if not os.path.isfile(p):
            continue
        m = re.search(u"(?m)^### Status atual\\s*\\n(.{0,200})",
                      io.open(p, encoding="utf-8").read(), re.S)
        if not m:
            continue
        for l in m.group(1).split(u"\n"):
            l = l.strip().strip(u"*`").strip()
            if l and not l.startswith(u">"):
                out[c] = re.sub(u"[*`]", u"", l).split(u"—")[0].split(u"(")[0].strip()
                break
    return out

def main():
    remover = u"--remove" in sys.argv
    STATUS = status_por_cliente()
    mudou = igual = sem_h1 = 0
    for p in arquivos():
        try:
            t = io.open(p, encoding="utf-8").read()
        except Exception:
            continue
        corpo = FM.sub(u"", t, count=1)
        if remover:
            if corpo != t:
                io.open(p, "w", encoding="utf-8", newline="").write(corpo); mudou += 1
            continue
        r, nome = rel(p), os.path.basename(p)
        h1 = h1_de(corpo)
        if not h1:
            sem_h1 += 1; continue
        tags = [u"tipo/%s" % tipo_de(r, nome)]
        m = re.match(u"uMode/_Clientes/([^/]+)/", r)
        if m:
            cli = m.group(1)
            if not cli.startswith(u"_"):
                tags.append(u"cliente/%s" % slug(cli))
                if STATUS.get(cli):
                    tags.append(u"status/%s" % slug(STATUS[cli]))
        elif r.startswith(u"uMode/"):
            tags.append(u"casa")
        ma = re.search(u"/([0-9]{2}_[^/]+)/_contexto/contexto-area\\.md$", r)
        if ma:
            tags.append(u"area/%s" % slug(ma.group(1)[3:]))
        fm = u"---\naliases:\n  - \"%s\"\ntags:\n%s---\n" % (
            h1.replace(u'"', u"'"), u"".join(u"  - %s\n" % x for x in tags))
        novo = fm + corpo
        if novo == t:
            igual += 1; continue
        io.open(p, "w", encoding="utf-8", newline="").write(novo); mudou += 1
    if remover:
        print(u"frontmatter removido: %d" % mudou)
    else:
        print(u"frontmatter escrito/atualizado: %d" % mudou)
        print(u"ja estavam corretos:           %d" % igual)
        print(u"SEM H1, nao tocados:           %d" % sem_h1)
        print(u"clientes com status declarado: %d" % len(STATUS))
    return 0

if __name__ == "__main__":
    sys.exit(main())
