# -*- coding: utf-8 -*-
u"""
nomeia-procedencia-pessoas.py - declara, POR CLIENTE, de onde vem (ou nao vem)
a contagem de pessoas por area.

CORRIGE UM ERRO MEU. A primeira versao disto detectava "cliente tem tabela de
usuarios" testando se `pessoas-da-area` tinha valor. Mas o valor dominante e
**`Nenhuma`** - que significa "esta area nao tem gente", nao "o cliente tem
tabela". Resultado: escrevi "tabela de usuarios do PLM" como fonte em 48
clientes, inclusive nos que nao tem tabela nenhuma. **672 linhas de
procedencia fabricada**, removidas antes de commitar.

E o mesmo defeito do padrao `Financeiro` que fabricava fonte em 51 fatos:
**pista fraca virando afirmacao de procedencia.**

A DETECCAO CERTA e contagem NUMERICA, e ela devolve tres clientes - nao 48.
E os tres tem fontes DIFERENTES, que este script nao mistura:

  Caedu, Puket  -> pagina do cliente, tabela de usuarios do PLM
  Osklen        -> `Pesquisa Satisfacao Kick Off Osklen`. ⚠ **NAO e tabela de
                   usuarios**: e CSat de kick-off. Chamar de tabela de PLM
                   seria repetir o erro.
  NK STORE      -> tem tabela de usuarios no Notion, lida hoje: 29 pessoas em
                   5 perfis. Este script escreve as contagens.
  os outros 44  -> nenhuma fonte de pessoa por area encontrada. A linha
                   declara isso, e o fato vira ausencia verificada.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")

FONTE = {
 u"Caedu":  u"Notion — página `Caedu`, tabela de usuários do PLM | varrido 21/09/2026",
 u"Puket":  u"Notion — página `Puket`, tabela de usuários do PLM | varrido 21/09/2026",
 u"Osklen": u"Notion — `Pesquisa Satisfação Kick Off Osklen` — ⚠ **CSat, não tabela de usuários** | 25/03/2025",
 u"NK STORE": u"Notion — `Perfil de Usuário e Permissionamentos`, base `Usuários` (29 pessoas) | varrido 23/09/2026",
}
PADRAO = (u"Notion — página `%s` — \U0001F534 **nenhuma fonte de pessoa por área encontrada** "
          u"| varrido 23/09/2026")

# NK STORE: contagem real por perfil, lida na base `Usuarios` em 23/09/2026.
# Sao 29 pessoas em 5 perfis; 24 delas caem em 4 areas canonicas.
NK_PESSOAS = {
 u"02_Estilo-Criacao": (u"**10 pessoas** com perfil `NK - Estilo` — o maior da conta",
                        u"Departamento NK: `Estilo`"),
 u"05_PCP": (u"**7 pessoas** com perfil `NK - PCP`", u"Departamento NK: `PCP`"),
 u"06_Compras-Supply-Sourcing": (u"**5 pessoas** com perfil `NK - Compras`",
                                 u"Departamento NK: `Compras`"),
 u"13_Modelagem": (u"**4 pessoas** com perfil `NK - Modelagem`",
                   u"Departamento NK: `Modelagem`"),
}
NK_NOTA = (u"\n\n> **Base `Usuários` da sub-página `Perfil de Usuário e Permissionamentos`,"
           u" lida em 23/09/2026.** 29 pessoas no total, em 5 perfis.\n"
           u"> \U0001F534 **As 3 restantes têm perfil `NK - Admin`** — transversal, não é área.\n"
           u"> ⚠ **Estado dos convites:** 26 aceitos, **2 pendentes** (12 e 16/12/2024) e "
           u"**1 inativo** desde 10/03/2025. **4 linhas estão marcadas `INATIVAR`.**\n"
           u"> \U0001F534 **A base tem um `Departamento NK` que NÃO bate com os perfis da matriz de "
           u"permissão** — a matriz usa `NK- Estilo Master`, `Nk Compras Master`, `NK Compras`, "
           u"`Nk Modelagem`, `NK - Time` e `Fornecedor`. **Só `NK - Admin` coincide literalmente "
           u"entre as duas.** ⚠ **Não conciliei: são duas taxonomias e a fonte não diz o mapa.**")


def areas_de(cliente):
    base = os.path.join(CLI, cliente)
    if not os.path.isdir(base):
        return
    for d in sorted(os.listdir(base)):
        c = os.path.join(base, d, u"_contexto", u"contexto-area.md")
        if os.path.exists(c):
            yield d, c


def anexa(txt, linha):
    if linha[:44] in txt:
        return txt, False
    marca = u"### Procedência\n"
    if marca not in txt:
        alvo = u"## Governança"
        if alvo not in txt:
            return txt, False
        nova = u"### Procedência\n| Bloco | Fonte | Data |\n|---|---|---|\n" + linha + u"\n\n"
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


def troca_pessoas(txt, corpo):
    marca = u"\n## Pessoas desta área\n"
    if marca not in txt:
        return txt, False
    antes, resto = txt.split(marca, 1)
    corte = len(resto)
    for h in (u"\n## ", u"\n### "):
        i = resto.find(h)
        if i != -1:
            corte = min(corte, i)
    return antes + marca + corpo + u"\n" + resto[corte:], True


def main():
    clientes = sorted(d for d in os.listdir(CLI)
                      if os.path.isdir(os.path.join(CLI, d)) and not d.startswith(u"_"))
    escritos = linhas = nk = 0
    for cliente in clientes:
        fonte = FONTE.get(cliente) or (PADRAO % cliente)
        linha = u"| Pessoas e responsáveis de área | " + fonte + u" |"
        for area, caminho in areas_de(cliente):
            txt = io.open(caminho, encoding=u"utf-8").read()
            antes = txt
            txt, ok = anexa(txt, linha)
            if ok:
                linhas += 1
            if cliente == u"NK STORE" and area in NK_PESSOAS:
                valor, dep = NK_PESSOAS[area]
                txt, ok2 = troca_pessoas(txt, valor + u" · " + dep + u"." + NK_NOTA)
                if ok2:
                    nk += 1
            if txt != antes:
                io.open(caminho, u"w", encoding=u"utf-8").write(txt)
                escritos += 1

    w = sys.stdout.write
    w(u"contexto-area.md escritos : %d\n" % escritos)
    w(u"linhas de procedencia     : %d\n" % linhas)
    w(u"areas da NK com contagem  : %d\n" % nk)
    w(u"\nfontes nomeadas: %s\n" % u" · ".join(sorted(FONTE)))
    w(u"demais %d clientes: ausencia de fonte de pessoa, declarada\n"
      % (len(clientes) - len(FONTE)))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
