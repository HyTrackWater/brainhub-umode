# -*- coding: utf-8 -*-
u"""
enriquece-feedback-do-vault.py - leva o `Feedback Interno Clientes.csv` do
vault para o `jornada.md` de TODO cliente: 427 avaliacoes de percepcao.

=== 1. O QUE ESTA BASE E, e a distincao decide tudo ===

**NAO e satisfacao do cliente.** O campo `Quem` e sempre alguem da uMode -
Tais Moser, Andrea Holmer, Laura, Elizabeth, Julianne. **E a leitura que a
uMode fazia da saude da propria carteira**, num ritual semanal (388 das 428
linhas sao `Feedback Semanal`). CSat vem de pesquisa COM o cliente e e outra
coisa. Nao se misturam, e o bloco escrito diz isso em toda ocorrencia.

=== 2. A SECAO VAI NOS 49, INCLUSIVE NOS 24 QUE A BASE NAO TEM ===

\U0001F534 Primeira versao deste script escreveu so nos 24 clientes medidos.
**Isso quebra a regra do CLAUDE.md: "todo MD do mesmo tipo tem os mesmos
titulos, sempre; conteudo varia, estrutura nunca".**

E a correcao nao e remover a secao - e completa-la. Nos clientes sem
avaliacao ela declara **ausencia VERIFICADA**, no formato do
`protocolo-fato-atomico.md` 2.1-bis: nao e `[sem fonte]` (ninguem olhou), e
`nao consta em <fonte> <data>` (olhei ali, naquele dia, e estava vazio).

\U0001F7E2 O ganho e duplo: a estrutura fica uniforme **e** o achado - metade
da carteira nunca foi avaliada - aparece no arquivo de cada um desses
clientes, em vez de ficar so num registro que ninguem abre.

=== 3. NOME DE CLIENTE: evidencia, nunca semelhanca de string ===

O CSV usa 27 grafias. Tres pares pareciam ambiguos:

  `STZ` (34) + `Studio Z` (4)      -> MESMO cliente
  `Basico` (11) + `Basico&Co` (6)  -> MESMO cliente
  `Reserva` (27) + `Oficina Reserva` (12) -> \U0001F534 DIFERENTES

O teste que decidiu os tres:
  - periodos **sequenciais, sem sobreposicao** = uma conta que mudou de nome
    (STZ ate 30/08/2024, Studio Z a partir de 21/10/2024)
  - periodo **sobreposto com o MESMO avaliador** = duas contas
    (Andrea Holmer avalia `Reserva` e `Oficina Reserva` no mesmo mes)

\u26a0 A distancia entre as strings nao decide nenhum dos casos:
`Reserva`/`Oficina Reserva` sao MAIS parecidas que `STZ`/`Studio Z`, e sao o
par que NAO se funde. Para o STZ ha ainda a fonte direta: o
`institucional.md` do Studio Z ja dizia "STZ e o Studio Z".

=== 4. DATA ===
O CSV escreve `DD/MM/AAAA`. Ordenar como string poe 01/11 antes de 21/10 -
foi o que aconteceu na primeira rodada. Aqui a data e convertida antes.
"""
import csv, io, os, sys, codecs, collections, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = (u"C:/Ambientes Virtuais/BrainHub - Jo\u00e3o Risol\u00e9o/umode-os-vault/"
       u"BrainHub/uMode/_Clientes/_geral/notion/Feedback Interno Clientes.csv")
FONTE = u"export `Feedback Interno Clientes` do vault do Jo\u00e3o"
HOJE = u"24/09/2026"
TITULO = u"## Leitura interna de sa\u00fade da conta"

MAPA = {
    u"STZ": u"Studio Z", u"Studio Z": u"Studio Z",
    u"B\u00e1sico": u"B\u00e1sico&Co", u"B\u00e1sico&Co": u"B\u00e1sico&Co",
    u"Reserva": u"Reserva", u"Oficina Reserva": u"Oficina Reserva",
    u"Vix": u"VIX", u"NK Store": u"NK STORE", u"Colm\u00e9ia": u"Colmeia",
    u"4Takes": u"4takes", u"Loj\u00e3o do Br\u00e1s": u"Loj\u00e3o do Br\u00e1s",
    u"Caedu": u"Caedu", u"Cambos": u"Cambos", u"NV": u"NV", u"Puket": u"Puket",
    u"Baw": u"Baw", u"Luiza Barcelos": u"Luiza Barcelos", u"NTK": u"NTK",
    u"Vivara": u"Vivara", u"DRO": u"DRO", u"Camys": u"Camys",
    u"Laces": u"Laces", u"Seven Global": u"Seven Global",
    u"Estrela": u"Estrela", u"Ladeira Bijuterias": u"Ladeira Bijuterias",
    u"Hyperlocal": u"Hyperlocal",
}

CABECA = [
    u"",
    TITULO,
    u"",
    u"> **Fonte:** %s, conferido em **%s**." % (FONTE, HOJE),
    u">",
    u"> \U0001F534 **Isto N\u00c3O \u00e9 satisfa\u00e7\u00e3o do cliente.** O campo `Quem` \u00e9 sempre algu\u00e9m da",
    u"> uMode \u2014 **\u00e9 a leitura que a uMode fazia da sa\u00fade da conta**, num ritual semanal.",
    u"> \u26a0 **N\u00e3o confundir com CSat**, que vem de pesquisa **com** o cliente e \u00e9 outra coisa.",
    u"",
]


def data(s):
    s = (s or u"").strip()[:10]
    for f in (u"%d/%m/%Y", u"%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(s, f).date()
        except Exception:
            pass
    return None


def bloco_medido(a):
    media = (a[u"soma"] / a[u"com_nota"]) if a[u"com_nota"] else None
    ds = sorted(a[u"datas"])
    perc = u" \u00b7 ".join(u"**%s** (%d)" % (k, v) for k, v in a[u"perc"].most_common(4))
    quem = u" \u00b7 ".join(u"%s (%d)" % (k, v) for k, v in a[u"quem"].most_common(4))
    sinal = u"\U0001F534" if (media is not None and media < 3.5) else (
        u"\u26a0" if (media is not None and media < 4.2) else u"\U0001F7E2")
    out = list(CABECA) + [
        u"| | |",
        u"|---|---|",
        u"| avalia\u00e7\u00f5es | **%d** |" % a[u"n"],
        u"| nota m\u00e9dia (1\u20135) | %s **%s** |" % (
            sinal, (u"%.2f" % media) if media is not None else u"`[a preencher]`"),
        u"| avalia\u00e7\u00f5es com **flag** | **%d** de %d (%.0f%%) |" % (
            a[u"flags"], a[u"n"], 100.0 * a[u"flags"] / a[u"n"]),
        u"| per\u00edodo coberto | %s \u2192 %s |" % (
            ds[0].strftime(u"%d/%m/%Y") if ds else u"`[a preencher]`",
            ds[-1].strftime(u"%d/%m/%Y") if ds else u"`[a preencher]`"),
        u"",
        u"**Percep\u00e7\u00e3o registrada:** %s." % (perc or u"`[a preencher]`"),
        u"",
        u"**Quem avaliou (da uMode):** %s." % (quem or u"`[a preencher]`"),
        u"",
    ]
    if len(a[u"grafias"]) > 1:
        out += [
            u"\u26a0 **Duas grafias na base** \u2014 %s \u2014 tratadas como a **mesma conta**: os"
            % u" e ".join(u"`%s` (%d)" % (k, v) for k, v in a[u"grafias"].most_common()),
            u"per\u00edodos s\u00e3o **sequenciais, sem sobreposi\u00e7\u00e3o**, o que \u00e9 renomea\u00e7\u00e3o e n\u00e3o duas contas.",
            u"",
        ]
    out += [
        u"\u26a0 **A s\u00e9rie termina em 2024.** N\u00e3o h\u00e1 avalia\u00e7\u00e3o posterior nesta base \u2014 o que",
        u"significa **que o ritual parou, ou que passou a viver noutro lugar, e eu n\u00e3o sei qual",
        u"dos dois.** \U0001F534 **A nota \u00e9 o que se registrava quando se registrava; n\u00e3o \u00e9 o estado",
        u"de hoje.**",
        u"",
    ]
    return out


def bloco_ausente():
    u"""
    Ausencia VERIFICADA, nao `[sem fonte]`. A diferenca importa: `[sem fonte]`
    diz que ninguem olhou; isto diz que olhei, nesta base, nesta data, e este
    cliente nao estava la.
    """
    return list(CABECA) + [
        u"**N\u00e3o consta em:** `Feedback Interno Clientes` \u00b7 conferido em **%s**." % HOJE,
        u"",
        u"\U0001F534 **Este cliente nunca foi avaliado neste ritual.** \u26a0 **Isso \u00e9 aus\u00eancia de",
        u"MEDI\u00c7\u00c3O, n\u00e3o conta saud\u00e1vel** \u2014 e n\u00e3o autoriza nenhuma leitura sobre a sa\u00fade da",
        u"conta, para bem nem para mal.",
        u"",
        u"\u26a0 **24 dos 48 clientes est\u00e3o nesta mesma situa\u00e7\u00e3o** \u2014 metade da carteira. **Por que",
        u"metade nunca foi avaliada \u00e9 pergunta aberta**, registrada em",
        u"[`_varredura-2026-09-24`](../../../../00_Institucional/_contexto/_varredura-2026-09-24-os-exports-nao-lidos-do-vault.md) \u00a7 7.",
        u"",
    ]


def main():
    if not os.path.exists(CSV):
        sys.stderr.write("CSV nao encontrado\n")
        return 2
    linhas = list(csv.DictReader(io.open(CSV, encoding=u"utf-8-sig", newline=u"")))

    ag = collections.defaultdict(lambda: {u"n": 0, u"soma": 0.0, u"com_nota": 0,
                                          u"flags": 0, u"perc": collections.Counter(),
                                          u"quem": collections.Counter(),
                                          u"grafias": collections.Counter(),
                                          u"datas": []})
    sem_mapa, sem_cliente = collections.Counter(), 0
    for x in linhas:
        c = (x.get(u"Cliente") or u"").strip()
        if not c:
            sem_cliente += 1
            continue
        alvo = MAPA.get(c)
        if not alvo:
            sem_mapa[c] += 1
            continue
        a = ag[alvo]
        a[u"n"] += 1
        a[u"grafias"][c] += 1
        try:
            a[u"soma"] += float((x.get(u"Satisfa\u00e7\u00e3o") or u"").strip())
            a[u"com_nota"] += 1
        except Exception:
            pass
        if (x.get(u"Flag?") or u"").strip().lower().startswith(u"s"):
            a[u"flags"] += 1
        p = (x.get(u"Percep\u00e7\u00e3o do Projeto") or u"").strip()
        if p:
            a[u"perc"][p] += 1
        q = (x.get(u"Quem") or u"").strip()
        if q:
            # `ANDREA HOLMER` e `Andrea Holmer` sao a mesma pessoa. Normaliza a
            # CAIXA, so isso - nao conserta grafia (`julianne rodirgues` fica).
            a[u"quem"][q.title()] += 1
        d = data(x.get(u"Dia da Avalia\u00e7\u00e3o"))
        if d:
            a[u"datas"].append(d)

    medidos, ausentes, pulados = 0, 0, []
    base_cl = os.path.join(RAIZ, u"uMode", u"_Clientes")
    for cliente in sorted(os.listdir(base_cl)):
        p = os.path.join(base_cl, cliente, u"00_Institucional", u"_contexto", u"jornada.md")
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding=u"utf-8").read()
        if TITULO in txt:
            pulados.append((cliente, u"ja tinha a secao"))
            continue
        alvo = u"\n## Governan\u00e7a"
        if alvo not in txt:
            alvo = u"\n## Conex\u00f5es"
        if alvo not in txt:
            pulados.append((cliente, u"\U0001F534 sem secao ancora"))
            continue
        if cliente in ag:
            corpo = bloco_medido(ag[cliente])
            medidos += 1
        else:
            corpo = bloco_ausente()
            ausentes += 1
        io.open(p, u"w", encoding=u"utf-8").write(
            txt.replace(alvo, u"\n".join(corpo) + alvo, 1))

    w = sys.stdout.write
    w(u"avaliacoes no CSV    : %d (%d sem cliente)\n" % (len(linhas), sem_cliente))
    w(u"clientes reconhecidos: %d\n" % len(ag))
    w(u"jornada.md com medida: %d\n" % medidos)
    w(u"jornada.md com ausencia VERIFICADA: %d\n" % ausentes)
    w(u"total escrito        : %d\n" % (medidos + ausentes))
    for c, m in pulados:
        w(u"   pulado: %-24s %s\n" % (c, m))
    if sem_mapa:
        w(u"\n\U0001F534 grafias SEM mapa (nao escritas):\n")
        for k, v in sem_mapa.most_common():
            w(u"   %-24s %d\n" % (k, v))
    nao_casou = sorted(set(ag) - set(os.listdir(base_cl)))
    if nao_casou:
        w(u"\n\U0001F534 clientes do CSV sem pasta no corpus: %s\n" % u", ".join(nao_casou))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
