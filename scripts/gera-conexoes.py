# -*- coding: utf-8 -*-
u"""
gera-conexoes.py - cria a camada de links entre os MDs do corpus.

Por que existe: em 22 set 2026 o `valida-indexacao.py` mediu 1.998 orfaos em 2.044
arquivos (97,7%). O conteudo estava certo e padronizado, mas a CAMADA DE LIGACAO
nao existia: as relacoes viviam na hierarquia de pastas e nos CSV do `_indice/`,
que o Obsidian nao le como aresta. Sem aresta, o grafo e uma nuvem de pontos.

O que este script faz, e SO isso:
  - acrescenta uma secao `## Conexoes` ao FIM de cada MD canonico do corpus,
    com links RELATIVOS (nao wikilink por nome, porque ha 49 `pessoas.md` e o
    nome simples e ambiguo);
  - liga cliente <-> jornada <-> pessoas <-> as 14 areas <-> demandas <-> RFIs;
  - liga cada demanda e cada RFI de volta ao cliente dela;
  - liga as areas da Casa ao institucional da Casa.

O que NAO faz: nao altera conteudo, nao remove nada, nao inventa relacao que a
hierarquia ja nao diga. E idempotente: rodar duas vezes nao duplica.

Uso:  python scripts/gera-conexoes.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UMODE = os.path.join(RAIZ, u"uMode")
CLI = os.path.join(UMODE, u"_Clientes")
MARCA = u"## Conexões"


def ler(p):
    return io.open(p, encoding="utf-8").read()


def esc(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def poe(p, bloco):
    u"""Insere ou substitui a secao Conexoes no fim do arquivo. Idempotente."""
    if not os.path.exists(p):
        return False
    s = ler(p)
    novo = MARCA + u"\n\n" + bloco.rstrip() + u"\n"
    if MARCA in s:
        i = s.index(MARCA)
        # a secao vai ate o fim do arquivo (e sempre a ultima)
        if s[i:].rstrip() == novo.rstrip():
            return False
        s = s[:i] + novo
    else:
        s = s.rstrip() + u"\n\n" + novo
    esc(p, s)
    return True


def areas_de(base):
    u"""Pastas numeradas dentro de uma casa (cliente ou Casa uMode)."""
    out = []
    for n in sorted(os.listdir(base)):
        if re.match(u"^[0-9]{2}_", n) and os.path.isdir(os.path.join(base, n)):
            out.append(n)
    return out


def bonito(nome_area):
    return nome_area.split(u"_", 1)[1].replace(u"-", u" ") if u"_" in nome_area else nome_area


def main():
    tocados = 0
    clientes = [c for c in sorted(os.listdir(CLI))
                if os.path.isdir(os.path.join(CLI, c)) and not c.startswith(u"_template")]

    for c in clientes:
        raizc = os.path.join(CLI, c)
        ctx = os.path.join(raizc, u"00_Institucional", u"_contexto")
        if not os.path.isdir(ctx):
            continue
        areas = areas_de(raizc)
        n_dem = 0
        dem = os.path.join(raizc, u"00_Institucional", u"_demandas")
        if os.path.isdir(dem):
            n_dem = len([f for f in os.listdir(dem)
                         if f.startswith(u"D-") and f.endswith(u".md")])
        n_pes = 0
        pes = os.path.join(raizc, u"00_Institucional", u"_pessoas")
        if os.path.isdir(pes):
            n_pes = len([f for f in os.listdir(pes)
                         if f.endswith(u".md") and not f.startswith(u"_")])
        n_rfi = 0
        rfi = os.path.join(raizc, u"00_Institucional", u"_rfis")
        if os.path.isdir(rfi):
            n_rfi = len([f for f in os.listdir(rfi)
                         if f.startswith(u"RFI-") and f.endswith(u".md")])

        lista_areas = u"\n".join(
            u"- [%s](../../%s/_contexto/contexto-area.md)" % (bonito(a), a) for a in areas)

        irmaos = {
            u"institucional.md": (u"jornada.md", u"pessoas.md"),
            u"jornada.md": (u"institucional.md", u"pessoas.md"),
            u"pessoas.md": (u"institucional.md", u"jornada.md"),
        }

        for arq, (i1, i2) in irmaos.items():
            p = os.path.join(ctx, arq)
            if not os.path.exists(p):
                continue
            b = []
            b.append(u"> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`** —")
            b.append(u"> não editar à mão: a próxima execução sobrescreve.")
            b.append(u"")
            b.append(u"**Cliente:** `%s`" % c)
            b.append(u"")
            b.append(u"**Os outros dois MDs desta casa:** [%s](%s) · [%s](%s)" % (i1, i1, i2, i2))
            b.append(u"")
            b.append(u"🔴 **O que ainda não se sabe deste cliente, e onde já se "
                     u"procurou:** [_pendencias-e-fontes.md](_pendencias-e-fontes.md)")
            b.append(u"")
            if n_dem or n_rfi or n_pes:
                partes = []
                if n_dem:
                    partes.append(u"**%d demandas** — [índice](../_demandas/_indice.md)" % n_dem)
                if n_rfi:
                    partes.append(u"**%d RFIs** — [índice](../_rfis/_indice.md)" % n_rfi)
                if n_pes:
                    partes.append(u"**%d fichas de pessoa** — [índice](../_pessoas/_indice.md)" % n_pes)
                b.append(u"**Registros:** " + u" · ".join(partes))
                b.append(u"")
            b.append(u"**As %d áreas deste cliente:**" % len(areas))
            b.append(u"")
            b.append(lista_areas.replace(u"../../", u"../../../"))
            b.append(u"")
            b.append(u"**Autoridades da Casa que governam este arquivo:**")
            b.append(u"[`_taxonomia-status-cliente.md`](../../../../00_Institucional/_contexto/_taxonomia-status-cliente.md) · "
                     u"[`_espec-pessoas-e-comunicacoes.md`](../../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) · "
                     u"[`protocolo-varredura-cliente.md`](../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)")
            if poe(p, u"\n".join(b)):
                tocados += 1

        # areas do cliente
        for a in areas:
            p = os.path.join(raizc, a, u"_contexto", u"contexto-area.md")
            if not os.path.exists(p):
                continue
            outras = [x for x in areas if x != a]
            b = []
            b.append(u"> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`.**")
            b.append(u"")
            b.append(u"**Área:** `%s` · **Cliente:** `%s`" % (a, c))
            b.append(u"")
            b.append(u"**A casa deste cliente:** "
                     u"[institucional.md](../../00_Institucional/_contexto/institucional.md) · "
                     u"[jornada.md](../../00_Institucional/_contexto/jornada.md) · "
                     u"[pessoas.md](../../00_Institucional/_contexto/pessoas.md)")
            b.append(u"")
            b.append(u"**A mesma área na Casa uMode:** ver `uMode/00_Institucional/_contexto/institucional.md`")
            b.append(u"")
            b.append(u"**As outras %d áreas deste cliente:**" % len(outras))
            b.append(u"")
            b.append(u"\n".join(u"- [%s](../../%s/_contexto/contexto-area.md)" % (bonito(x), x)
                                for x in outras))
            if poe(p, u"\n".join(b)):
                tocados += 1

        # demandas e RFIs -> cliente
        for pasta, pref in ((dem, u"D-"), (rfi, u"RFI-")):
            if not os.path.isdir(pasta):
                continue
            for f in sorted(os.listdir(pasta)):
                if not (f.startswith(pref) and f.endswith(u".md")):
                    continue
                p = os.path.join(pasta, f)
                b = (u"> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**\n\n"
                     u"**Cliente:** `%s` — "
                     u"[institucional.md](../_contexto/institucional.md) · "
                     u"[jornada.md](../_contexto/jornada.md) · "
                     u"[pessoas.md](../_contexto/pessoas.md)\n\n"
                     u"**Protocolo que governa este registro:** "
                     u"[`protocolo-gestao-%s.md`](../../../../00_Institucional/_protocolos/protocolo-gestao-%s.md)"
                     % (c, u"demanda" if pref == u"D-" else u"rfi",
                        u"demanda" if pref == u"D-" else u"rfi"))
                if poe(p, b):
                    tocados += 1

        # indice de demandas e RFIs: sem ele, cada registro fica orfao
        # (ele aponta para o cliente, mas ninguem aponta para ele).
        for pasta, pref, rot in ((dem, u"D-", u"Demandas"), (rfi, u"RFI-", u"RFIs")):
            if not os.path.isdir(pasta):
                continue
            itens = sorted(f for f in os.listdir(pasta)
                           if f.startswith(pref) and f.endswith(u".md"))
            if not itens:
                continue
            linhas = [u"# %s · %s — índice" % (c, rot), u""]
            linhas.append(u"> **Gerado por `scripts/gera-conexoes.py`. Não editar à mão.**")
            linhas.append(u"> Existe para que cada registro tenha entrada no grafo — sem ele,")
            linhas.append(u"> os %d arquivos desta pasta ficam órfãos no Obsidian." % len(itens))
            linhas.append(u"")
            linhas.append(u"**Cliente:** [institucional.md](../_contexto/institucional.md) · "
                          u"[jornada.md](../_contexto/jornada.md) · "
                          u"[pessoas.md](../_contexto/pessoas.md)")
            linhas.append(u"")
            linhas.append(u"**%d registros:**" % len(itens))
            linhas.append(u"")
            for f in itens:
                linhas.append(u"- [%s](%s)" % (f[:-3], f))
            esc(os.path.join(pasta, u"_indice.md"),
                chr(10).join(linhas) + chr(10))
            tocados += 1

        # fichas de pessoa do cliente
        if os.path.isdir(pes):
            fichas = sorted(f for f in os.listdir(pes)
                            if f.endswith(u".md") and not f.startswith(u"_"))
            for f in fichas:
                bl = (u"> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**"
                      + chr(10) + chr(10) +
                      u"**Cliente:** `%s` — "
                      u"[institucional.md](../_contexto/institucional.md) · "
                      u"[jornada.md](../_contexto/jornada.md) · "
                      u"[pessoas.md](../_contexto/pessoas.md)" % c
                      + chr(10) + chr(10) +
                      u"**As outras pessoas deste cliente:** [índice](_indice.md)"
                      + chr(10) + chr(10) +
                      u"**Autoridade sobre pessoa e comunicação:** "
                      u"[`_espec-pessoas-e-comunicacoes.md`]"
                      u"(../../../../00_Institucional/_contexto/_espec-pessoas-e-comunicacoes.md) · "
                      u"**regra de identidade:** "
                      u"[`protocolo-varredura-cliente.md`]"
                      u"(../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)")
                if poe(os.path.join(pes, f), bl):
                    tocados += 1
            if fichas:
                L = [u"# %s · Pessoas — índice" % c, u""]
                L.append(u"> **Gerado por `scripts/gera-conexoes.py`. Não editar à mão.**")
                L.append(u"> Cada pessoa é um arquivo por decisão do Vinicius em 22 set 2026:")
                L.append(u"> *\"cada pessoa tem sim que ser um arquivo e realmente ter vários")
                L.append(u"> outros nós com ela\".*")
                L.append(u"")
                L.append(u"**Cliente:** [institucional.md](../_contexto/institucional.md) · "
                         u"[jornada.md](../_contexto/jornada.md) · "
                         u"[pessoas.md](../_contexto/pessoas.md)")
                L.append(u"")
                L.append(u"**%d fichas:**" % len(fichas))
                L.append(u"")
                for f in fichas:
                    L.append(u"- [%s](%s)" % (f[:-3], f))
                esc(os.path.join(pes, u"_indice.md"), chr(10).join(L) + chr(10))
                tocados += 1

    # ---- pessoas da propria Casa uMode ----
    # Mesmo esquecimento das 5 demandas da Casa: o gerador cuidava so das fichas
    # de cliente, e as 16 da Casa ficavam orfas. Classe inteira ou nada.
    pcasa = os.path.join(UMODE, u"00_Institucional", u"_pessoas")
    if os.path.isdir(pcasa):
        fichas = sorted(f for f in os.listdir(pcasa)
                        if f.endswith(u".md") and not f.startswith(u"_"))
        for f in fichas:
            b = (u"> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**" +
                 chr(10) + chr(10) +
                 u"**Instância:** `Casa uMode` — pessoa INTERNA. "
                 u"Pessoa da Casa **nunca se duplica dentro do cliente** (`CLAUDE.md`)." +
                 chr(10) + chr(10) +
                 u"**As outras pessoas da Casa:** [índice](_indice.md)" +
                 chr(10) + chr(10) +
                 u"**Institucional da Casa:** "
                 u"[institucional.md](../_contexto/institucional.md)" +
                 chr(10) + chr(10) +
                 u"**O protocolo que governa esta ficha:** "
                 u"[`protocolo-gestao-pessoas.md`](../_protocolos/protocolo-gestao-pessoas.md)")
            if poe(os.path.join(pcasa, f), b):
                tocados += 1
        I = [u"# Casa uMode · Pessoas · índice", u"",
             u"> **DERIVADO.** Gerado por `scripts/gera-conexoes.py`. **Não se edita à mão.**",
             u"", u"**%d fichas de pessoa interna.**" % len(fichas), u""]
        for f in fichas:
            I.append(u"- [%s](%s)" % (f[:-3].replace(u"-", u" ").title(), f))
        I += [u"", u"⚠ **Cargo e `Status na uMode` serão revistos de uma vez ao fim "
              u"da varredura** — `AGORA.md` § 7, item 9. **Não corrigir aos pedaços.**",
              u"", u"[institucional.md](../_contexto/institucional.md)", u""]
        esc(os.path.join(pcasa, u"_indice.md"), chr(10).join(I) + chr(10))
        tocados += 1

    # ---- demandas da propria Casa uMode ----
    # Sem isto elas ficam com estrutura diferente das 993 de cliente, e o
    # valida-padrao-corpus.py acusa - com razao: a regra e "toda a classe".
    dcasa = os.path.join(UMODE, u"00_Institucional", u"_demandas")
    if os.path.isdir(dcasa):
        for f in sorted(os.listdir(dcasa)):
            if not (f.startswith(u"D-") and f.endswith(u".md")):
                continue
            b = (u"> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**" + chr(10) + chr(10) +
                 u"**Instância:** `Casa uMode` — demanda interna, não de cliente." + chr(10) + chr(10) +
                 u"[institucional.md](../_contexto/institucional.md)" + chr(10) + chr(10) +
                 u"**Protocolo que governa este registro:** "
                 u"[`protocolo-gestao-demanda.md`](../_protocolos/protocolo-gestao-demanda.md)")
            if poe(os.path.join(dcasa, f), b):
                tocados += 1

    # ---- Casa uMode ----
    areas_casa = areas_de(UMODE)
    for a in areas_casa:
        p = os.path.join(UMODE, a, u"_contexto", u"contexto-area.md")
        if not os.path.exists(p):
            continue
        outras = [x for x in areas_casa if x != a]
        b = []
        b.append(u"> Camada de ligação do corpus. **Gerada por `scripts/gera-conexoes.py`.**")
        b.append(u"")
        b.append(u"**Área da Casa uMode:** `%s`" % a)
        b.append(u"")
        b.append(u"**Institucional da Casa:** "
                 u"[institucional.md](../../00_Institucional/_contexto/institucional.md)")
        b.append(u"")
        b.append(u"**As outras áreas da Casa:**")
        b.append(u"")
        b.append(u"\n".join(u"- [%s](../../%s/_contexto/contexto-area.md)" % (bonito(x), x)
                            for x in outras))
        if poe(p, u"\n".join(b)):
            tocados += 1

    # ---- diario de pendencias e fontes por cliente (22 set 2026) ----
    # Pedido do Vinicius: um arquivo por cliente com toda duvida, discrepancia
    # e risco, e o registro de onde ja se varreu. Sem este bloco ele nasce orfao.
    for c in sorted(os.listdir(CLI)):
        p = os.path.join(CLI, c, u"00_Institucional", u"_contexto",
                         u"_pendencias-e-fontes.md")
        if not os.path.exists(p):
            continue
        b = [u"> Camada de ligação. **Gerada por `scripts/gera-conexoes.py`.**",
             u"",
             u"**Cliente:** `%s` — [institucional.md](institucional.md) · "
             u"[jornada.md](jornada.md) · [pessoas.md](pessoas.md)" % c,
             u"",
             u"**As decisões TRANSVERSAIS, que não são deste cliente, vivem em** "
             u"[`_pendencias-gerais.md`]"
             u"(../../../../00_Institucional/_contexto/_pendencias-gerais.md).",
             u"",
             u"**O protocolo que governa a varredura:** [`protocolo-varredura-cliente.md`]"
             u"(../../../../00_Institucional/_protocolos/protocolo-varredura-cliente.md)"]
        if poe(p, chr(10).join(b)):
            tocados += 1

    # ---- fichas de ferramenta (22 set 2026) ----
    # Ferramenta so virou no do grafo em 22 set 2026; sem este bloco as 16 fichas
    # apontam para cliente mas nao sao apontadas de volta por ninguem.
    for area, rotulo in ((u"03_Produto-e-Solucoes", u"m\u00f3dulo contrat\u00e1vel da plataforma uMode"),
                         (u"06_Tecnologia", u"sistema de terceiro (ERP/integra\u00e7\u00e3o do cliente)")):
        fp = os.path.join(UMODE, area, u"_ferramentas")
        if not os.path.isdir(fp):
            continue
        outro = (u"[sistemas de terceiro](../../06_Tecnologia/_ferramentas/_indice.md)"
                 if area.startswith(u"03")
                 else u"[m\u00f3dulos da uMode](../../03_Produto-e-Solucoes/_ferramentas/_indice.md)")
        for f in sorted(os.listdir(fp)):
            if not f.endswith(u".md") or f == u"_indice.md":
                continue
            b = [u"> Camada de liga\u00e7\u00e3o. **Gerada por `scripts/gera-conexoes.py`.**",
                 u"",
                 u"**Natureza:** " + rotulo + u".",
                 u"",
                 u"**As outras ferramentas desta classe:** [\u00edndice](_indice.md)",
                 u"",
                 u"**\u00c1rea da Casa que guarda esta ficha:** ["
                 + bonito(area) + u"](../_contexto/contexto-area.md)",
                 u"",
                 u"**Institucional da Casa:** "
                 u"[institucional.md](../../00_Institucional/_contexto/institucional.md)"]
            if poe(os.path.join(fp, f), chr(10).join(b)):
                tocados += 1
        b = [u"> Camada de liga\u00e7\u00e3o. **Gerada por `scripts/gera-conexoes.py`.**",
             u"",
             u"**\u00c1rea da Casa:** [" + bonito(area) + u"](../_contexto/contexto-area.md)",
             u"",
             u"**O outro acervo de ferramenta:** " + outro,
             u"",
             u"**Institucional da Casa:** "
             u"[institucional.md](../../00_Institucional/_contexto/institucional.md)"]
        if poe(os.path.join(fp, u"_indice.md"), chr(10).join(b)):
            tocados += 1


    print(u"arquivos com camada de conexão escrita/atualizada: %d" % tocados)
    return 0


if __name__ == "__main__":
    sys.exit(main())
