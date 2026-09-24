# -*- coding: utf-8 -*-
u"""
resolve-falantes.py - transforma nome de falante de transcricao em identidade
(`pessoa:<e-mail>`), ou declara por que nao deu.

POR QUE UM SCRIPT PROPRIO, e nao o resolvedor do `gera-fatos.py`. Aquele foi
feito para o campo `atendimento`, que so tem gente da Casa. Falante de
transcricao e outra coisa: mistura uMode e cliente, vem com apelido, com
nome parcial e com CAIXA ALTA.

TRES REGRAS, e as tres nasceram de erro observado:

1. **ESCOPO.** So resolve contra as fichas do PROPRIO cliente e as da Casa.
   \U0001F534 Na primeira tentativa, o falante `Juliana` de uma reuniao da CAEDU
   casou com `juliana@osklen.com.br` - pessoa de OUTRO cliente. Ficha de
   cliente alheio nunca entra no escopo.

2. **NOME DE UM TOKEN SO NAO RESOLVE.** `Rose`, `Natalia`, `Bruno`, `Mauricio`
   nao sao identidade. Mesmo que exista uma unica ficha com aquele nome, o
   casamento e coincidencia, nao prova. Sai como `apelido`.

3. **CASAMENTO POR TOKEN, nao por string.** A ficha diz
   `Juliana Ferre Esteves`, a transcricao diz `Juliana Ferre`. Casa quando o
   PRIMEIRO nome bate e pelo menos mais um token bate. Dois candidatos que
   passam nesse teste = ambiguo, e ambiguo NAO se escolhe.

Nao escreve nada no corpus. Reporta.
"""
import io, os, re, sys, codecs, collections, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RE_FALA = re.compile(u"^\\[\\d{2}:\\d{2}:\\d{2}\\]\\s*([^:]{1,60}?):", re.M)
RE_EMAIL = re.compile(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
RE_H1 = re.compile(u"^# (.+)$", re.M)
PONTO = u"·"

# ruido que nao e pessoa: conta de servico, rotulo generico do transcritor
NAO_E_PESSOA = re.compile(u"^(speaker|firebase|api|bot|convidado|participante)\\b", re.I)


def chave(s):
    u"""minusculo, sem acento, sem pontuacao - para comparar token a token."""
    s = unicodedata.normalize(u"NFKD", s)
    s = u"".join(c for c in s if not unicodedata.combining(c))
    return re.sub(u"[^a-z0-9 ]", u" ", s.lower()).split()


def fichas(cliente):
    u"""
    [(tokens_do_nome, email, origem)] das fichas do cliente e da Casa.
    ESCOPO: nunca inclui ficha de outro cliente.
    """
    out = []
    alvos = [(os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_pessoas"), u"uMode"),
             (os.path.join(RAIZ, u"uMode", u"_Clientes", cliente), cliente)]
    for base, origem in alvos:
        if not os.path.isdir(base):
            continue
        for dirpath, _, filenames in os.walk(base):
            if u"_pessoas" not in dirpath:
                continue
            for fn in filenames:
                if not fn.endswith(u".md") or fn.startswith(u"_"):
                    continue
                try:
                    t = io.open(os.path.join(dirpath, fn), encoding=u"utf-8").read()
                except Exception:
                    continue
                partes = t.split(u"### Email", 1)
                if len(partes) < 2:
                    continue
                e = RE_EMAIL.search(partes[1].split(u"###")[0])
                if not e:
                    continue
                nomes = set()
                m = RE_H1.search(t)
                if m:
                    segs = [s.replace(u"**", u"").strip() for s in m.group(1).split(PONTO)]
                    segs = [s for s in segs if s and s.lower() != u"pessoa"]
                    if segs:
                        nomes.add(segs[-1])
                for rot in (u"### Nome completo", u"### Nome preferido"):
                    if rot in t:
                        l = t.split(rot, 1)[1].split(u"\n")[1].strip()
                        l = l.replace(u"**", u"").replace(u"`", u"").split(u" — ")[0].strip()
                        if l and u"a preencher" not in l.lower():
                            nomes.add(l)
                for n in nomes:
                    tk = chave(n)
                    if tk:
                        out.append((tk, e.group(0).lower(), origem))
    return out


def resolve(nome, cat):
    u"""'pessoa:<email>' | ('apelido'|'ambiguo'|'nao encontrado', detalhe)."""
    if NAO_E_PESSOA.match(nome.strip()):
        return None, u"nao e pessoa"
    tk = chave(nome)
    if len(tk) < 2:
        return None, u"apelido: nome de um token so nao identifica"
    cands = set()
    for tokens, email, origem in cat:
        if not tokens or tokens[0] != tk[0]:
            continue
        # alem do primeiro nome, pelo menos mais um token em comum
        if set(tk[1:]) & set(tokens[1:]):
            cands.add((email, origem))
    if not cands:
        return None, u"nao encontrado nas fichas do cliente nem da Casa"
    if len(set(e for e, _ in cands)) > 1:
        return None, u"ambiguo: %s" % u", ".join(sorted(e for e, _ in cands))
    e, origem = sorted(cands)[0]
    return u"pessoa:" + e, origem


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("uso: resolve-falantes.py <dir-transcricoes> <Cliente>\n")
        return 2
    base, cliente = sys.argv[1], sys.argv[2]
    cat = fichas(cliente)

    falantes = collections.Counter()
    reunioes = collections.defaultdict(set)
    for fn in sorted(os.listdir(base)):
        if not fn.endswith(u".txt"):
            continue
        t = io.open(os.path.join(base, fn), encoding=u"utf-8", errors=u"replace").read()
        for m in RE_FALA.finditer(t):
            n = m.group(1).strip()
            falantes[n] += 1
            reunioes[n].add(fn)

    ok, aberto = [], []
    for nome, n in falantes.most_common():
        r, det = resolve(nome, cat)
        (ok if r else aberto).append((nome, n, len(reunioes[nome]), r or det))

    w = sys.stdout.write
    w(u"catalogo: %d nomes de ficha (uMode + %s)\n" % (len(cat), cliente))
    w(u"falantes distintos: %d\n\n" % len(falantes))
    w(u"\U0001F7E2 RESOLVIDOS (%d)\n" % len(ok))
    w(u"%-36s %6s %5s  %s\n" % (u"FALANTE", u"FALAS", u"REUN", u"IDENTIDADE"))
    for nome, n, r_, ident in ok:
        w(u"%-36s %6d %5d  %s\n" % (nome[:36], n, r_, ident))
    w(u"\n\U0001F534 ABERTOS (%d) — e o motivo de cada um\n" % len(aberto))
    w(u"%-36s %6s %5s  %s\n" % (u"FALANTE", u"FALAS", u"REUN", u"POR QUE"))
    for nome, n, r_, motivo in aberto:
        w(u"%-36s %6d %5d  %s\n" % (nome[:36], n, r_, motivo[:66]))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
