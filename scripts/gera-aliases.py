# -*- coding: utf-8 -*-
u"""gera-aliases.py - escreve `aliases` em frontmatter YAML a partir do H1.

POR QUE EXISTE
--------------
O Obsidian rotula nota pelo NOME DO ARQUIVO, nao pelo titulo. E o padrao deste
corpus manda o contrario: "todo MD do mesmo tipo tem os mesmos titulos, sempre" -
entao ha 694 arquivos chamados `contexto-area.md`, 50 `institucional.md` e 49
`jornada.md`. Na busca rapida do Obsidian isso vira uma parede de nomes iguais.

O H1 ja resolve: `# Qualidade - Contexto de area - Caedu`. Medido em 23 set 2026:
2.645 de 2.648 arquivos tem H1, e ele e unico em 99,1%.

Este script copia o H1 para `aliases`, que o Obsidian usa na busca rapida (Ctrl+O)
e no autocomplete de link.

O QUE ISTO NAO RESOLVE
----------------------
O rotulo do GRAFO continua sendo o nome do arquivo. Alias nao muda isso - so um
plugin de terceiro mudaria, e este repositorio deliberadamente nao tem plugin.
No grafo, a cor (15 grupos por entidade) e a posicao ja desambiguam.

ORDEM NO RITUAL - IMPORTA
-------------------------
Rodar SEMPRE DEPOIS do `gera-conexoes.py`. Motivo: o `gera-conexoes` reescreve os
~60 arquivos `_indice.md` do zero, e isso APAGA o frontmatter deles. Nao e
destrutivo - este script devolve o alias - mas se a ordem inverter, os indices
ficam sem alias ate a proxima rodada.

SEGURANCA
---------
- Nao renomeia arquivo nenhum. Nao mexe em link nenhum.
- Testado contra os quatro validadores em 23 set 2026: nenhum acusou diferenca.
- Idempotente: rodar duas vezes nao duplica frontmatter.
- Reversivel: `python scripts/gera-aliases.py --remove` tira tudo.
"""
import io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORA_DIR = {".git", "__pycache__", ".obsidian", "_indice"}
FM = re.compile(u"^---\r?\n.*?\r?\n---\r?\n", re.S)

def arquivos():
    for dp, dn, fn in os.walk(RAIZ):
        dn[:] = [d for d in dn if d not in IGNORA_DIR]
        for f in fn:
            if f.endswith(u".md"):
                yield os.path.join(dp, f)

def h1_de(txt):
    # O BOM no inicio do arquivo fazia startswith falhar em silencio -
    # um arquivo real do corpus ficou de fora por isso. Tira o BOM antes de olhar.
    for l in txt.lstrip(u"\ufeff").split(u"\n")[:40]:
        s = l.strip().lstrip(u"\ufeff")
        if s.startswith(u"# "):
            return re.sub(u"\\s+", u" ", s[2:].strip())
    return None

def main():
    remover = u"--remove" in sys.argv
    mudou = pulados = sem_h1 = 0
    for p in arquivos():
        try:
            t = io.open(p, encoding="utf-8").read()
        except Exception:
            continue
        corpo = FM.sub(u"", t, count=1)
        if remover:
            if corpo != t:
                io.open(p, "w", encoding="utf-8", newline="").write(corpo)
                mudou += 1
            continue
        h1 = h1_de(corpo)
        if not h1:
            sem_h1 += 1
            continue
        # O titulo vira alias. Aspas duplas porque ha `:` e `-` nos titulos.
        seguro = h1.replace(u'"', u"'")
        novo_fm = u'---\naliases:\n  - "%s"\n---\n' % seguro
        novo = novo_fm + corpo
        if novo == t:
            pulados += 1
            continue
        io.open(p, "w", encoding="utf-8", newline="").write(novo)
        mudou += 1
    if remover:
        print(u"frontmatter removido de %d arquivos" % mudou)
    else:
        print(u"alias escrito/atualizado: %d" % mudou)
        print(u"ja estavam corretos:      %d" % pulados)
        print(u"SEM H1, nao tocados:      %d" % sem_h1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
