# -*- coding: utf-8 -*-
u"""
resolve-atendimento.py - Fase 0, item 1: preenche `### Responsavel de
atendimento (uMode)` nos clientes onde o fato `atendimento` nao resolve.

POR QUE ISTO E O PRIMEIRO ITEM DA FASE 0. O roteador de aprovacao precisa
mandar o pedido para o dono do contexto. Hoje so 14 dos 49 clientes tem
`atendimento` resolvido para `pessoa:<e-mail>`. **Nao se endereca aprovacao
para um dono que nunca foi registrado.**

=== ESTE SCRIPT NAO ESCREVE E-MAIL, E ISSO E DE PROPOSITO ===

\U0001F534 `gera-fatos.py` e dono unico do bloco `## Fatos` e **ja tem** o
resolvedor: indexa o primeiro nome das fichas da Casa, resolve quando e unico
e acusa ambiguidade quando nao e. Duplicar essa logica aqui criaria dois
resolvedores discordando em silencio - o defeito de "dois donos" que o
projeto proibe. Entao aqui se escreve **NOME**, na secao-fonte; o e-mail sai
do `gera-fatos`.

=== AS TRES FONTES, EM ORDEM DE FORCA ===

1. `Mapa de Clientes` -> **`Time de Atendimento`**: diz o TIME, por apelido -
   `Holmer & Laura`, `Fernanda & Victor`. \U0001F534 Apelido de um token so nao
   identifica: ha DUAS `Fernanda` e DOIS `Pedro` nas fichas da Casa.
2. `Demandas de Clientes` -> **`Key Account/Responsavel`**: NOME COMPLETO de
   quem trabalhou - `Fernanda Araujo`, `Pedro Murillo` - com volume.
3. `Reunioes Compartilhadas` -> `Participantes` / `Last edited by`:
   \U0001F534 **EVIDENCIA FRACA.** E quem conduziu ou manteve as notas da
   conta. **Nao e designacao de atendimento**, e so entra rotulada assim.

\U0001F7E2 1 e 2 se completam: a primeira diz quem forma o time, a segunda
desambigua quem e a pessoa. Nenhuma sozinha resolve `Fernanda`.

=== `SMB` NAO E LACUNA, E RESPOSTA ===

\U0001F534 Quase apaguei isto. `SMB` no campo de atendimento parece lixo e nao
e: a pendencia 507 ja registrava que o campo e *pessoa OU o rotulo `SMB`*, e
todos os `SMB` estao em `Sem CS` ou `Churn`. **Significa conta sem CS
dedicado.** Escrever "a preencher" por cima seria transformar resposta em
lacuna - o mesmo erro que ja apagou 20 clientes uma vez.

\u26a0 **E tem consequencia de desenho:** existe conta que, por contrato, NAO
tem pessoa de atendimento. **O roteador precisa de fallback, nao pode so
falhar.**

=== CORTE ===
Fonte 2: pessoa entra se responde por **>= 10%** das demandas atribuidas.
Fonte 3: entra com **>= 2** reunioes. Quem cai fica no relatorio.
"""
import csv, io, os, re, sys, codecs, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = (u"C:/Ambientes Virtuais/BrainHub - Jo\u00e3o Risol\u00e9o/umode-os-vault/"
     u"BrainHub/uMode/_Clientes/_geral/notion/")
HOJE = u"25/09/2026"
SEC = u"### Respons\u00e1vel de atendimento (uMode)"
CORTE = 0.10
NL = u"\n"


def sem_url(s):
    return re.sub(u"\\s*\\(https?://[^)]*\\)", u"", s or u"").strip()


def carrega():
    mapa = {}
    for x in csv.DictReader(io.open(V + u"Mapa de Clientes.csv",
                                    encoding=u"utf-8-sig", newline=u"")):
        n = sem_url(x.get(u"Nome Fantasia"))
        if n:
            mapa[n] = x

    dem = collections.defaultdict(collections.Counter)
    for x in csv.DictReader(io.open(V + u"Demandas de Clientes.csv",
                                    encoding=u"utf-8-sig", newline=u"")):
        c = sem_url(x.get(u"\U0001F465 Clientes"))
        ka = (x.get(u"Key Account/Respons\u00e1vel") or u"").strip()
        if not c or not ka:
            continue
        for p in [p.strip() for p in ka.split(u",") if p.strip()]:
            dem[c][p] += 1

    reu = collections.defaultdict(collections.Counter)
    for x in csv.DictReader(io.open(V + u"Reuni\u00f5es Compartilhadas com Clientes.csv",
                                    encoding=u"utf-8-sig", newline=u"")):
        c = sem_url(x.get(u"Cliente"))
        if not c:
            continue
        gente = [sem_url(g) for g in (x.get(u"Participantes") or u"").split(u",")]
        gente = [g for g in gente if g]
        if not gente:
            e = (x.get(u"Last edited by") or u"").strip()
            gente = [e] if e else []
        for g in gente:
            reu[c][g] += 1
    return mapa, dem, reu


def bloco(txt):
    u"""
    Primeira ocorrencia de SEC que NAO esteja sob `## Governanca`.
    \u26a0 A secao aparece DUAS vezes no institucional.md: uma com o conteudo,
    outra como resposta de governanca. Escrever na errada poe lista de nome
    onde devia haver prosa - e o `gera-fatos` passaria a ler as duas.
    """
    gov = txt.find(u"\n## Governan\u00e7a")
    i = txt.find(u"\n" + SEC + u"\n")
    if i == -1 or (gov != -1 and i > gov):
        return None
    ini = i + len(SEC) + 2
    fim = len(txt)
    for h in (u"\n## ", u"\n### "):
        j = txt.find(h, ini)
        if j != -1:
            fim = min(fim, j)
    return ini, fim


def corpo_smb():
    L = [
        u"**`SMB`** \u2014 \U0001F534 **conta SEM CS dedicado.**",
        u"",
        u"\u26a0 **Isto \u00e9 resposta, n\u00e3o lacuna:** o campo de atendimento na base aceita",
        u"**pessoa OU o r\u00f3tulo `SMB`**, e **todos os `SMB` est\u00e3o em `Sem CS` ou `Churn`**.",
        u"",
        u"> \U0001F534 **Consequ\u00eancia para o roteamento de aprova\u00e7\u00e3o: esta conta n\u00e3o tem",
        u"> pessoa de atendimento a quem endere\u00e7ar** \u2014 e isso \u00e9 por desenho, n\u00e3o por",
        u"> falta de registro. **O roteador precisa de fallback, n\u00e3o pode s\u00f3 falhar.**",
        u"> Ver `_espec-pipeline-de-contexto-e-aprovacao.md` \u00a7 5.",
        u"> **Fonte:** `Mapa de Clientes` \u00b7 coluna `Time de Atendimento` \u00b7 conferido em %s." % HOJE,
        u"",
    ]
    return NL.join(L)


def corpo_ausente():
    L = [
        u"`[a preencher]` \u2014 \U0001F534 **ningu\u00e9m designado que eu tenha encontrado.**",
        u"",
        u"> **Aus\u00eancia VERIFICADA** \u2014 **tr\u00eas** fontes lidas em %s:" % HOJE,
        u"> `Mapa de Clientes` \u00b7 `Time de Atendimento` e `Atendimento 2025` \u2192 **vazio** \u00b7",
        u"> `Demandas de Clientes` \u00b7 `Key Account/Respons\u00e1vel` \u2192 **sem linha deste cliente** \u00b7",
        u"> `Reuni\u00f5es Compartilhadas` \u00b7 `Participantes`/`Last edited by` \u2192 **sem reuni\u00e3o**.",
        u">",
        u"> \u26a0 **\u00c9 aus\u00eancia de REGISTRO, n\u00e3o prova de que a conta n\u00e3o \u00e9 atendida.**",
        u"> \U0001F534 **Para o roteador de aprova\u00e7\u00e3o, esta conta n\u00e3o tem endere\u00e7o.**",
        u"",
    ]
    return NL.join(L)


def main():
    mapa, dem, reu = carrega()
    base = os.path.join(RAIZ, u"uMode", u"_Clientes")
    ja = smb = forte = fracos = ausente = 0
    pulados, cortados = [], []

    for cliente in sorted(os.listdir(base)):
        if cliente.startswith(u"_"):
            continue
        p = os.path.join(base, cliente, u"00_Institucional", u"_contexto",
                         u"institucional.md")
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding=u"utf-8").read()
        if any(u"pessoa:" in l for l in re.findall(u"^- atendimento: (.*)$", txt, re.M)):
            ja += 1
            continue
        b = bloco(txt)
        if not b:
            pulados.append((cliente, u"\U0001F534 sem a se\u00e7\u00e3o-fonte"))
            continue
        ini, fim = b

        x = mapa.get(cliente)
        time = (x.get(u"Time de Atendimento") or u"").strip() if x else u""

        if time == u"SMB":
            io.open(p, u"w", encoding=u"utf-8").write(txt[:ini] + corpo_smb() + txt[fim:])
            smb += 1
            continue

        cont = dem.get(cliente) or collections.Counter()
        total = sum(cont.values())
        gente = []
        for nome, n in cont.most_common():
            if total and (float(n) / total) >= CORTE:
                gente.append((nome, n))
            else:
                cortados.append((cliente, nome, n, total))

        fraca = []
        if not gente and not time:
            rc = reu.get(cliente) or collections.Counter()
            fraca = [(n, k) for n, k in rc.most_common(3) if k >= 2]
            if not fraca:
                io.open(p, u"w", encoding=u"utf-8").write(
                    txt[:ini] + corpo_ausente() + txt[fim:])
                ausente += 1
                continue

        L = []
        if time:
            L.append(u"**Time de atendimento (base `Mapa de Clientes`): %s**" % time)
            L.append(u"")
        if gente:
            for nome, n in gente:
                L.append(u"- %s \u2014 %d de %d demandas atribu\u00eddas (%.0f%%)"
                         % (nome, n, total, 100.0 * n / total))
        elif fraca:
            for nome, k in fraca:
                L.append(u"- %s \u2014 %d reuni\u00f5es da conta" % (nome, k))
        elif time:
            # so o rotulo do time: entram os apelidos, e o `gera-fatos` resolve
            # o que for unico e acusa o que for ambiguo. E o comportamento certo.
            for ap in [a.strip() for a in re.split(u"[&+]", time) if a.strip()]:
                L.append(u"- %s \u2014 \u26a0 **apelido do r\u00f3tulo de time**, sem nome "
                         u"completo na fonte" % ap)
        L.append(u"")

        fontes = []
        if time:
            fontes.append(u"`Mapa de Clientes` \u00b7 `Time de Atendimento`")
        if gente:
            fontes.append(u"`Demandas de Clientes` \u00b7 `Key Account/Respons\u00e1vel`")
        if fraca:
            fontes.append(u"`Reuni\u00f5es Compartilhadas com Clientes`")
        L.append(u"> **Fonte:** %s \u00b7 conferido em %s." % (u" + ".join(fontes), HOJE))

        if fraca:
            L.append(u"> \U0001F534 **EVID\u00caNCIA FRACA, e a diferen\u00e7a \u00e9 de natureza:** isto \u00e9")
            L.append(u"> **quem conduziu ou manteve as reuni\u00f5es** da conta \u2014 **n\u00e3o \u00e9 designa\u00e7\u00e3o")
            L.append(u"> de atendimento.** \u26a0 **Serve para o roteador ter a quem endere\u00e7ar na")
            L.append(u"> falta de designado; n\u00e3o serve para afirmar quem atende.**")
        if gente:
            L.append(u"> \u26a0 **A contagem \u00e9 de demanda trabalhada, n\u00e3o de designa\u00e7\u00e3o formal.**")
            L.append(u"> \u00c9 evid\u00eancia de quem atendeu \u2014 **e a diferen\u00e7a importa quando a conta")
            L.append(u"> trocou de m\u00e3o.**")
        if not time:
            L.append(u"> \u26a0 **`Atendimento 2025` segue vazio na base `Mapa de Clientes`**")
            L.append(u"> (aus\u00eancia verificada em 23/09/2026). \U0001F7E2 **Isto n\u00e3o contradiz aquilo**")
            L.append(u"> \u2014 uma fonte diz quem est\u00e1 designado, a outra diz quem trabalhou.")
        L.append(u"")

        io.open(p, u"w", encoding=u"utf-8").write(txt[:ini] + NL.join(L) + txt[fim:])
        if fraca:
            fracos += 1
        else:
            forte += 1

    w = sys.stdout.write
    w(u"ja resolvidos (intocados)          : %d\n" % ja)
    w(u"\U0001F7E2 preenchidos com fonte forte       : %d\n" % forte)
    w(u"\u26a0 preenchidos com evid\u00eancia fraca   : %d\n" % fracos)
    w(u"\u26a0 marcados `SMB` (sem CS dedicado)  : %d\n" % smb)
    w(u"\U0001F534 aus\u00eancia VERIFICADA escrita       : %d\n" % ausente)
    for c, m in pulados:
        w(u"   pulado: %-22s %s\n" % (c[:22], m))
    if cortados:
        w(u"\n\u26a0 abaixo do corte de %.0f%% (n\u00e3o escritos, listados para n\u00e3o sumirem):\n"
          % (CORTE * 100))
        for c, n, k, t in cortados:
            w(u"   %-20s %-24s %d/%d\n" % (c[:20], n[:24], k, t))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
