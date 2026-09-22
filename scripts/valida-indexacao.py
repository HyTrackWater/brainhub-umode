# -*- coding: utf-8 -*-
u"""
valida-indexacao.py - mapeia o grafo de links do corpus e acha orfaos.

Por que existe: o Vinicius quer visualizar este repositorio como um MEGA BRAIN
no Obsidian, ver como as conexoes estao sendo feitas e entender quantos arquivos
orfaos existem. Sem grafo, "orfao" e opiniao; com grafo, e numero.

O que conta como link:
  - wikilink do Obsidian:  [[nome-do-arquivo]]  ou  [[nome|texto]]
  - link markdown relativo: [texto](caminho/arquivo.md)   (ancora e %20 tolerados)

Definicoes:
  ORFAO   = arquivo .md que NINGUEM aponta (zero links de entrada).
  FOLHA   = arquivo que nao aponta para ninguem (zero links de saida).
  QUEBRADO= link que aponta para arquivo que nao existe.

Nao e erro ser folha. E esperado que a maioria dos arquivos de cliente seja folha
hoje. Orfao tambem nao e necessariamente defeito - mas orfao em massa significa
que o grafo nao existe, e o Obsidian vai mostrar uma nuvem de pontos soltos.

Uso:  python scripts/valida-indexacao.py
      python scripts/valida-indexacao.py --detalhe   (lista os orfaos, ate 40)
Saida: sempre 0. E um relatorio, nao um portao.
"""
import io
import os
import re
import sys
import collections

# O console do Windows abre em cp1252 e MORRE ao imprimir o vermelho do relatorio.
# Sem isto o validador falha justamente quando tem algo a dizer.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORA = (u".git", u"scratchpad", u"node_modules")

WIKI = re.compile(u"\\[\\[([^\\]|#]+)")
MD = re.compile(u"\\]\\(([^)]+\\.md)")


def norm(c):
    return c.replace(u"\\", u"/")


def todos():
    fs = []
    for pasta, sub, arqs in os.walk(RAIZ):
        rel = norm(os.path.relpath(pasta, RAIZ))
        if any(ig in rel.split(u"/") for ig in IGNORA):
            sub[:] = []
            continue
        for n in arqs:
            if n.endswith(u".md"):
                fs.append(norm(os.path.join(rel, n)) if rel != u"." else n)
    return sorted(fs)


def resolve(alvo, origem, porbase):
    u"""Devolve o caminho real apontado, ou None se nao existir."""
    alvo = alvo.split(u"#")[0].strip().replace(u"%20", u" ")
    if not alvo:
        return None
    # 1) caminho relativo ao arquivo de origem - vale SEMPRE, inclusive para um
    #    nome simples como `pessoas.md`, que em markdown aponta para a mesma pasta.
    #    Resolver isso primeiro evita hub falso: sem isso, `pessoas.md` caia no
    #    desempate por nome e era atribuido a um cliente qualquer.
    cand = norm(os.path.normpath(os.path.join(os.path.dirname(origem), alvo)))
    if cand in porbase.get(u"__todos__", ()):
        return cand
    # por nome de arquivo (wikilink do Obsidian)
    base = alvo.split(u"/")[-1]
    if not base.endswith(u".md"):
        base += u".md"
    alvos = porbase.get(base)
    if alvos and len(alvos) == 1:
        return alvos[0]
    if alvos:
        # AMBIGUO: o mesmo nome existe em varias pastas (ha 49 `pessoas.md`).
        # Nao atribuir a nenhum: atribuir ao primeiro inventaria uma aresta e
        # criaria um hub falso. O Obsidian tem exatamente o mesmo problema com
        # wikilink por nome simples.
        return u"__AMBIGUO__:" + base
    return None


def main():
    detalhe = u"--detalhe" in sys.argv
    arquivos = todos()
    porbase = collections.defaultdict(list)
    for f in arquivos:
        porbase[f.split(u"/")[-1]].append(f)
    porbase[u"__todos__"] = set(arquivos)

    entrada = collections.Counter()
    saida = collections.Counter()
    quebrados = []
    ambiguos = collections.Counter()

    for f in arquivos:
        try:
            txt = io.open(os.path.join(RAIZ, *f.split(u"/")), encoding="utf-8").read()
        except Exception:
            continue
        alvos = WIKI.findall(txt) + MD.findall(txt)
        for a in alvos:
            r = resolve(a, f, porbase)
            if r is None:
                quebrados.append((f, a))
                continue
            if r.startswith(u"__AMBIGUO__:"):
                ambiguos[r.split(u":", 1)[1]] += 1
                saida[f] += 1
                continue
            if r == f:
                continue  # auto-referencia nao conta
            saida[f] += 1
            entrada[r] += 1

    orfaos = [f for f in arquivos if entrada[f] == 0]
    folhas = [f for f in arquivos if saida[f] == 0]
    conectados = [f for f in arquivos if entrada[f] or saida[f]]

    print(u"")
    print(u"GRAFO DO CORPUS")
    print(u"  arquivos .md          : %5d" % len(arquivos))
    print(u"  com algum link        : %5d  (%.1f%%)"
          % (len(conectados), 100.0 * len(conectados) / max(1, len(arquivos))))
    print(u"  ORFAOS (ninguem cita) : %5d  (%.1f%%)"
          % (len(orfaos), 100.0 * len(orfaos) / max(1, len(arquivos))))
    print(u"  folhas (nao citam)    : %5d" % len(folhas))
    print(u"  links quebrados       : %5d" % len(quebrados))
    print(u"  nomes ambiguos        : %5d" % len(ambiguos))

    mais = entrada.most_common(8)
    if mais:
        print(u"")
        print(u"  MAIS CITADOS (os hubs do grafo):")
        for f, n in mais:
            print(u"   %4d  %s" % (n, f))

    if detalhe:
        print(u"")
        print(u"  ORFAOS (ate 40):")
        for f in orfaos[:40]:
            print(u"    %s" % f)
        if quebrados:
            print(u"")
            print(u"  QUEBRADOS (ate 20):")
            for o, a in quebrados[:20]:
                print(u"    %s  ->  %s" % (o, a))
        if ambiguos:
            print(u"")
            print(u"  AMBIGUOS - mesmo nome em varias pastas (o Obsidian erra aqui):")
            for b, n in ambiguos.most_common(10):
                print(u"    %s  (%d referencias, %d arquivos com esse nome)"
                      % (b, n, len(porbase[b])))

    print(u"")
    print(u"Orfao nao e erro por si so. Orfao EM MASSA significa que o grafo nao existe,")
    print(u"e no Obsidian o corpus aparece como nuvem de pontos soltos em vez de cerebro.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
