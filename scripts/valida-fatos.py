# -*- coding: utf-8 -*-
u"""
valida-fatos.py - ACUSA desvio no bloco `## Fatos`. NAO corrige.

Irmao do valida-numeros.py, mesma filosofia: quem corrige e o gerador ou a
pessoa. Um validador que conserta esconde o defeito em vez de mostrar.

Checa quatro coisas, e a primeira e a que justifica o script existir:

  1. CHAVE FORA DO VOCABULARIO. O protocolo trava a tabela de chaves porque o
     cruzamento compara por chave: se alguem escrever `cnpj` num arquivo e
     `CNPJ` noutro, o diff falha EM SILENCIO. Este script e quem impede isso.
  2. FORMA da linha - tem que terminar em `]`, ter ` - [` e ter `chave: valor`.
  3. DATA em AAAA-MM-DD, ou `sem data` declarado.
  4. COBERTURA - quantos fatos, quantos com fonte, por arquivo.

Sai 1 se houver desvio de forma ou chave fora do vocabulario.
`[sem fonte]` NAO e desvio: e lacuna declarada, e declarar lacuna e o padrao.
"""
import io, os, re, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTO = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_protocolos",
                     u"protocolo-fato-atomico.md")

RE_LINHA = re.compile(u"^- ([a-z0-9-]+): (.+?) — \\[(.+)\\]$")
RE_DATA = re.compile(u"^\\d{4}-\\d{2}-\\d{2}$")
RE_CHAVE_TABELA = re.compile(u"^\\| `([a-z0-9-]+)`(?: · `([a-z0-9-]+)`)? \\|", re.M)


def vocabulario():
    u"""Le a tabela de chaves do PROPRIO protocolo - fonte unica, nao copia."""
    if not os.path.exists(PROTO):
        return None
    txt = io.open(PROTO, encoding=u"utf-8").read()
    chaves = set()
    for m in RE_CHAVE_TABELA.finditer(txt):
        for g in m.groups():
            if g:
                chaves.add(g)
    return chaves


def blocos():
    for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, u"uMode")):
        if u"_template" in dirpath:
            continue
        for fn in filenames:
            if not fn.endswith(u".md"):
                continue
            caminho = os.path.join(dirpath, fn)
            try:
                txt = io.open(caminho, encoding=u"utf-8").read()
            except Exception:
                continue
            if u"\n## Fatos\n" not in txt:
                continue
            corpo = txt.split(u"\n## Fatos\n", 1)[1].split(u"\n## ")[0]
            yield os.path.relpath(caminho, RAIZ).replace(os.sep, u"/"), corpo


def main():
    vocab = vocabulario()
    arquivos = 0
    fatos = com_fonte = sem_fonte = abertos = ausente = 0
    forma_ruim, chave_ruim, data_ruim = [], {}, []

    for caminho, corpo in blocos():
        arquivos += 1
        for ln in corpo.split(u"\n"):
            if not ln.startswith(u"- "):
                continue
            fatos += 1
            m = RE_LINHA.match(ln)
            if not m:
                forma_ruim.append((caminho, ln[:90]))
                continue
            chave, valor, proc = m.group(1), m.group(2), m.group(3)

            if vocab is not None and chave not in vocab:
                chave_ruim.setdefault(chave, []).append(caminho)

            if proc == u"sem fonte":
                sem_fonte += 1
            elif proc.startswith(u"não consta em:"):
                # 2.1-bis: nao e fonte do valor, e prova de que se procurou.
                ausente += 1
            elif proc.startswith(u"ambiguo") or proc.startswith(u"nao resolvido"):
                abertos += 1
            else:
                com_fonte += 1
                partes = proc.rsplit(u" · ", 1)
                if len(partes) != 2:
                    data_ruim.append((caminho, ln[:90]))
                elif not RE_DATA.match(partes[1]) and partes[1] != u"sem data":
                    data_ruim.append((caminho, ln[:90]))

    w = sys.stdout.write
    w(u"\n== BLOCO `## Fatos` ==\n")
    w(u"arquivos com bloco : %d\n" % arquivos)
    w(u"fatos              : %d\n" % fatos)
    if fatos:
        w(u"  com fonte e data : %d  (%.0f%%)\n" % (com_fonte, 100.0 * com_fonte / fatos))
        w(u"  ausencia VERIFICADA: %d  (%.0f%%)  <- procurou-se em fonte nomeada\n"
          % (ausente, 100.0 * ausente / fatos))
        w(u"  lacuna declarada : %d  (%.0f%%)  <- `[sem fonte]`, NAO e desvio\n"
          % (sem_fonte, 100.0 * sem_fonte / fatos))
        w(u"  identidade aberta: %d  <- pessoa nao resolvida por e-mail\n" % abertos)

    falhou = False

    if vocab is None:
        w(u"\n⚠ protocolo-fato-atomico.md nao encontrado: vocabulario NAO checado\n")
    elif chave_ruim:
        falhou = True
        w(u"\n\U0001F534 CHAVE FORA DO VOCABULARIO (%d) - entra na secao 4 do protocolo\n"
          % len(chave_ruim))
        w(u"   ou some do corpus. Chave livre quebra o cruzamento em silencio.\n")
        for k in sorted(chave_ruim):
            w(u"   - `%s` em %d arquivo(s), ex.: %s\n"
              % (k, len(chave_ruim[k]), chave_ruim[k][0]))
    else:
        w(u"\n\U0001F7E2 vocabulario: %d chaves no protocolo, nenhuma chave livre no corpus\n"
          % len(vocab))

    if forma_ruim:
        falhou = True
        w(u"\n\U0001F534 FORMA INVALIDA (%d) - esperado `- chave: valor — [fonte · data]`\n"
          % len(forma_ruim))
        for c, ln in forma_ruim[:10]:
            w(u"   - %s\n     %s\n" % (c, ln))
        if len(forma_ruim) > 10:
            w(u"   ... e mais %d\n" % (len(forma_ruim) - 10))

    if data_ruim:
        falhou = True
        w(u"\n\U0001F534 DATA INVALIDA (%d) - esperado AAAA-MM-DD ou `sem data`\n" % len(data_ruim))
        for c, ln in data_ruim[:10]:
            w(u"   - %s\n     %s\n" % (c, ln))

    if not falhou:
        w(u"\n\U0001F7E2 nenhum desvio de forma, chave ou data.\n")
    return 1 if falhou else 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
