# -*- coding: utf-8 -*-
u"""
nomeia-procedencia-area.py - declara a procedência de `produto-conectado`,
`pessoas-da-area` e `responsavel-area` nos 672 `contexto-area.md`.

POR QUE. Essas tres chaves somam **1.562 dos ~1.900 fatos `[sem fonte]`** do
corpus - 82% do problema em tres chaves. E as tres tem fonte conhecida e
nomeavel; faltava so estar escrito na tabela de Procedencia de cada arquivo,
que e de onde o `gera-fatos.py` tira a fonte por chave.

AS DUAS FONTES, E ELAS SAO DIFERENTES:

  produto-conectado  -> base `Mapa de Clientes`. Os modulos contratados sao
                        propriedade da conta, valem para todas as areas dela,
                        e foram lidos por SQL em 23/09/2026.

  pessoas / responsavel -> pagina do cliente, tabela de usuarios do PLM.
                        ⚠ **E nem todo cliente tem essa tabela.** Para quem
                        nao tem, a linha declara a AUSENCIA - "sem tabela de
                        usuarios do PLM" - e o fato vira ausencia verificada
                        em vez de `[sem fonte]`.

COMO SE DECIDE QUEM TEM TABELA. Nao por suposicao: um cliente tem tabela se
ALGUMA area dele ja traz `pessoas-da-area` com valor. Se nenhuma traz, e
porque a varredura nao achou tabela - e isso passa a estar escrito.
"""
import io, os, re, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")
HOJE = u"23/09/2026"

RE_PESSOAS = re.compile(u"^- pessoas-da-area: (?!\\?)", re.M)

L_MOD = (u"| Módulos e produto conectado | Notion — base `Mapa de Clientes` "
         u"| varrido " + HOJE + u" |")
L_PES_TEM = (u"| Pessoas e responsáveis de área | Notion — página `%s`, "
             u"tabela de usuários do PLM | varrido " + HOJE + u" |")
L_PES_NAO = (u"| Pessoas e responsáveis de área | Notion — página `%s`, "
             u"**sem tabela de usuários do PLM** | varrido " + HOJE + u" |")


def areas_de(cliente):
    base = os.path.join(CLI, cliente)
    for d in sorted(os.listdir(base)):
        c = os.path.join(base, d, u"_contexto", u"contexto-area.md")
        if os.path.exists(c):
            yield c


def tem_tabela_de_usuarios(cliente):
    u"""Medido, nao suposto: alguma area ja tem `pessoas-da-area` com valor?"""
    for c in areas_de(cliente):
        try:
            if RE_PESSOAS.search(io.open(c, encoding=u"utf-8").read()):
                return True
        except Exception:
            pass
    return False


def anexa(txt, linha):
    u"""Acrescenta a linha na tabela `### Procedencia`, criando-a se faltar."""
    if linha[:40] in txt:
        return txt, False
    marca = u"### Procedência\n"
    if marca not in txt:
        alvo = u"## Governança"
        if alvo not in txt:
            return txt, False
        nova = (u"### Procedência\n| Bloco | Fonte | Data |\n|---|---|---|\n"
                + linha + u"\n\n")
        return txt.replace(alvo, nova + alvo, 1), True
    antes, resto = txt.split(marca, 1)
    linhas = resto.split(u"\n")
    fim = 0
    for i, l in enumerate(linhas):
        if l.strip().startswith(u"|"):
            fim = i + 1
        elif fim:
            break
    if not fim:
        return txt, False
    return antes + marca + u"\n".join(linhas[:fim] + [linha] + linhas[fim:]), True


def main():
    clientes = sorted(d for d in os.listdir(CLI)
                      if os.path.isdir(os.path.join(CLI, d)) and not d.startswith(u"_"))
    escritos = linhas = 0
    com_tabela, sem_tabela = [], []

    for cliente in clientes:
        tem = tem_tabela_de_usuarios(cliente)
        (com_tabela if tem else sem_tabela).append(cliente)
        l_pes = (L_PES_TEM if tem else L_PES_NAO) % cliente
        for caminho in areas_de(cliente):
            txt = io.open(caminho, encoding=u"utf-8").read()
            antes = txt
            for l in (L_MOD, l_pes):
                txt, ok = anexa(txt, l)
                if ok:
                    linhas += 1
            if txt != antes:
                io.open(caminho, u"w", encoding=u"utf-8").write(txt)
                escritos += 1

    w = sys.stdout.write
    w(u"clientes                 : %d\n" % len(clientes))
    w(u"  \U0001F7E2 COM tabela de usuarios : %d\n" % len(com_tabela))
    w(u"  \U0001F534 SEM tabela de usuarios : %d\n" % len(sem_tabela))
    w(u"contexto-area.md escritos: %d\n" % escritos)
    w(u"linhas de procedencia    : %d\n" % linhas)
    w(u"\nSEM tabela de usuarios (a varredura nao achou):\n   %s\n"
      % u", ".join(sem_tabela))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
