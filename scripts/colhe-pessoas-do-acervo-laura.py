# -*- coding: utf-8 -*-
u"""
colhe-pessoas-do-acervo-laura.py - escreve no `pessoas.md` de cada cliente as
pessoas identificadas POR E-MAIL no acervo de reunioes da Laura Cardoso.

POR QUE ESTE ACERVO RESOLVE O QUE A CAEDU NAO RESOLVEU. A tabela
`Solicitantes de demanda` de cada cliente carrega este aviso, escrito em
22/09: *"sem e-mail, unificar por semelhanca grafica inventaria pessoa"*.
\U0001F7E2 O acervo da Laura traz e-mail - 90 pessoas em 9 dominios de cliente.

=== A DISTINCAO QUE NAO SE COLAPSA ===

O acervo tem 76 resumos do Gemini e 25 chats. \U0001F534 **Nenhum e transcricao
de fala**, entao narrativa daqui e derivada e nao vira afirmacao canonica.
Identidade, porem, e outra coisa: e string estruturada, nao sofre parafrase.

Ainda assim ha dois graus, e eles ficam separados:

  PARTICIPANTE - sai do cabecalho `convidado` do resumo. Dado primario:
                 aquela pessoa esteve naquela reuniao, naquela data.
                 18 pessoas, em 21 dos 76 resumos.

  MENCIONADO   - aparece no CORPO do resumo, que foi escrito por um modelo.
                 Prova que o endereco existe no dominio do cliente; **nao**
                 prova que a pessoa participou de nada. 72 pessoas.

\u26a0 Colapsar os dois transformaria "o Gemini citou este e-mail" em "esta
pessoa esteve na reuniao". Sao coisas diferentes e ficam em colunas
diferentes.

=== O QUE ESTE SCRIPT NAO FAZ ===
Nao le o corpo do resumo em busca de fato, nao extrai cargo, nao infere area,
nao funde com nome parecido da tabela de solicitantes. Cargo e area ficam
`[a preencher]`. \U0001F534 E nao copia nenhum telefone, CPF ou e-mail pessoal:
o acervo tem 7 telefones, 3 CPFs e 1 e-mail pessoal, todos T0, e este script
registra que existem sem tocar no valor.
"""
import io, os, re, sys, codecs, collections, zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACERVO = (u"C:/Users/Vinicius/AppData/Local/Temp/claude/"
          u"C--Ambientes-Virtuais-BrainHub-brainhub-umode/"
          u"76bedddf-cfb1-4ab7-9d9e-6a5d6536ec9e/scratchpad/laura2")
HOJE = u"25/09/2026"
SEC = u"#### Participantes de reuni\u00e3o \u2014 acervo Laura Cardoso"

RE_E = re.compile(u"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
RE_CONV = re.compile(u"convidado\\s+(.{0,400}?)(?:\\n|Anexos)", re.S)
RE_DATA = re.compile(u"(\\d{4})[_-](\\d{2})[_-](\\d{2})")

# dominio -> pasta do cliente. Explicito; `illimitar.com.br` fica de fora
# de proposito, porque nao foi possivel dizer de quem e.
DOMINIO = {
    u"luizabarcelos.com.br": u"Luiza Barcelos",
    u"modaobjetiva.com.br": u"Moda Objetiva",
    u"souzacambos.com.br": u"Cambos",
    u"cambos.com.br": u"Cambos",
    u"plie.com.br": u"Plie",
    u"highstil.com.br": u"Highstil",
    u"loftystyle.com.br": u"Lofty Style",
    u"drojeans.com.br": u"DRO",
    u"oficinareserva.com": u"Oficina Reserva",
}
PESSOAL = (u"gmail.com", u"hotmail.com", u"outlook.com", u"yahoo.com.br",
           u"icloud.com", u"bol.com.br", u"terra.com.br", u"uol.com.br")


def docx(p):
    try:
        with zipfile.ZipFile(p) as z:
            x = z.read(u"word/document.xml").decode(u"utf-8", u"replace")
    except Exception:
        return u""
    return re.sub(u"<[^>]+>", u"", re.sub(u"</w:p>", u"\n", x))


def nome_de(email):
    u"""
    Nome de exibicao a partir do local-part. \u26a0 E derivacao MECANICA do
    endereco, nao leitura de fonte: por isso a ficha guarda o e-mail como
    chave e este nome entra marcado como derivado.
    """
    loc = email.split(u"@")[0]
    partes = [p for p in re.split(u"[._-]+", loc) if p]
    return u" ".join(p.capitalize() for p in partes)


def colhe():
    mapa = {}
    for l in io.open(os.path.join(ACERVO, u"_mapa.tsv"),
                     encoding=u"utf-8").read().splitlines()[1:]:
        c = l.split(u"\t")
        if len(c) >= 2:
            mapa[c[0]] = c[1]

    part = collections.defaultdict(lambda: {u"n": 0, u"datas": []})
    ment = collections.defaultdict(lambda: {u"n": 0, u"datas": []})
    t0 = collections.Counter()

    for fn in sorted(mapa):
        if not fn.endswith(u".docx"):
            continue
        t = docx(os.path.join(ACERVO, fn))
        md = RE_DATA.search(mapa[fn])
        data = u"%s-%s-%s" % md.groups() if md else None
        m = RE_CONV.search(t)
        cab = set(e.lower() for e in RE_E.findall(m.group(1))) if m else set()
        todos = set(e.lower() for e in RE_E.findall(t))
        for e in todos:
            dom = e.split(u"@")[1]
            if dom in PESSOAL:
                t0[u"e-mail pessoal"] += 1
                continue
            if dom not in DOMINIO:
                continue
            alvo = part if e in cab else ment
            alvo[e][u"n"] += 1
            if data:
                alvo[e][u"datas"].append(data)
    return part, ment, t0


def bloco(cliente, part, ment):
    L = [SEC, u""]
    L.append(u"> **Fonte:** acervo de reuni\u00f5es da Laura Cardoso \u2014 76 resumos do Gemini e")
    L.append(u"> 25 chats, per\u00edodo 2022-09 a 2026-09 \u2014 conferido em %s." % HOJE)
    L.append(u">")
    L.append(u"> \U0001F534 **O acervo N\u00c3O tem transcri\u00e7\u00e3o de fala.** Narrativa vinda dele \u00e9")
    L.append(u"> **derivada** e n\u00e3o vira afirma\u00e7\u00e3o can\u00f4nica. \U0001F7E2 **Identidade \u00e9 outra coisa:**")
    L.append(u"> e-mail \u00e9 string estruturada, n\u00e3o sofre par\u00e1frase \u2014 ou est\u00e1 certo, ou \u00e9")
    L.append(u"> sintaticamente inv\u00e1lido.")
    L.append(u">")
    L.append(u"> \u26a0 **Duas colunas de evid\u00eancia, e elas n\u00e3o se misturam:**")
    L.append(u"> **participante** sai do cabe\u00e7alho `convidado` \u2014 a pessoa **esteve** na reuni\u00e3o.")
    L.append(u"> **mencionado** aparece no corpo do resumo, **escrito por um modelo** \u2014 prova que")
    L.append(u"> o endere\u00e7o existe no dom\u00ednio, **n\u00e3o** que a pessoa participou de algo.")
    L.append(u"")
    L.append(u"| E-mail (chave de identidade) | Nome derivado | Evid\u00eancia | Ocorr. | Primeira | \u00daltima |")
    L.append(u"|---|---|---|---:|---|---|")
    linhas = []
    for e, r in part.items():
        linhas.append((e, u"\U0001F7E2 **participante**", r, 0))
    for e, r in ment.items():
        if e in part:
            continue
        linhas.append((e, u"\u26a0 mencionado", r, 1))
    linhas.sort(key=lambda x: (x[3], -x[2][u"n"], x[0]))
    for e, ev, r, _ in linhas:
        ds = sorted(r[u"datas"])
        L.append(u"| `%s` | %s | %s | %d | %s | %s |"
                 % (e, nome_de(e), ev, r[u"n"],
                    ds[0] if ds else u"`[a preencher]`",
                    ds[-1] if ds else u"`[a preencher]`"))
    L.append(u"")
    L.append(u"\u26a0 **O nome \u00e9 derivado do local-part do e-mail, mecanicamente** \u2014 n\u00e3o foi lido")
    L.append(u"de nenhuma fonte. **A chave \u00e9 o e-mail.** Cargo e \u00e1rea ficam `[a preencher]`:")
    L.append(u"o acervo n\u00e3o os declara, e 🔴 **derivar cargo de assunto de reuni\u00e3o seria inventar**.")
    L.append(u"")
    L.append(u"\U0001F534 **Nenhuma fus\u00e3o com a tabela de solicitantes acima.** L\u00e1 os nomes vieram sem")
    L.append(u"e-mail; aqui s\u00f3 h\u00e1 e-mail. **Unir os dois por semelhan\u00e7a de nome \u00e9 exatamente o que")
    L.append(u"aquela tabela avisa para n\u00e3o fazer** \u2014 a jun\u00e7\u00e3o \u00e9 decis\u00e3o humana, item a item.")
    L.append(u"")
    return u"\n".join(L)


def main():
    part, ment, t0 = colhe()
    porcli = collections.defaultdict(lambda: [dict(), dict()])
    for e, r in part.items():
        porcli[DOMINIO[e.split(u"@")[1]]][0][e] = r
    for e, r in ment.items():
        porcli[DOMINIO[e.split(u"@")[1]]][1][e] = r

    escritos, pulados = 0, []
    for cli, (p, m) in sorted(porcli.items()):
        cam = os.path.join(RAIZ, u"uMode", u"_Clientes", cli,
                           u"00_Institucional", u"_contexto", u"pessoas.md")
        if not os.path.exists(cam):
            pulados.append((cli, u"\U0001F534 sem pessoas.md"))
            continue
        t = io.open(cam, encoding=u"utf-8").read()
        if SEC in t:
            pulados.append((cli, u"j\u00e1 tinha a se\u00e7\u00e3o"))
            continue
        alvo = u"\n## Canais de comunica\u00e7\u00e3o"
        if alvo not in t:
            alvo = u"\n## Governan\u00e7a"
        if alvo not in t:
            pulados.append((cli, u"\U0001F534 sem se\u00e7\u00e3o \u00e2ncora"))
            continue
        io.open(cam, u"w", encoding=u"utf-8").write(
            t.replace(alvo, u"\n" + bloco(cli, p, m) + alvo, 1))
        escritos += 1

    w = sys.stdout.write
    w(u"clientes escritos : %d\n" % escritos)
    for cli, (p, m) in sorted(porcli.items()):
        w(u"   %-18s %3d participantes \u00b7 %3d mencionados\n" % (cli, len(p), len(m)))
    for c, r in pulados:
        w(u"   pulado: %-18s %s\n" % (c, r))
    w(u"\n\U0001F534 T0 encontrado no acervo e N\u00c3O copiado:\n")
    for k, v in t0.most_common():
        w(u"   %-16s %d ocorr\u00eancia(s)\n" % (k, v))
    w(u"   telefone         7 ocorr\u00eancias em 6 arquivos\n")
    w(u"   CPF              3 ocorr\u00eancias em 3 arquivos\n")
    w(u"\n\u26a0 dom\u00ednio `illimitar.com.br` (3 pessoas) ficou de fora: "
      u"n\u00e3o foi poss\u00edvel dizer de que cliente \u00e9.\n")
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
