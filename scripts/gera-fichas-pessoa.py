# -*- coding: utf-8 -*-
u"""
gera-fichas-pessoa.py - cria UMA FICHA POR PESSOA de cliente.

Decisao do Vinicius em 22 set 2026, textual: "cada pessoa tem sim que ser um
arquivo e realmente ter varios outros nos com ela. Isso nao tem duvida."

Ate aqui, pessoa de cliente era LINHA DE TABELA dentro de `pessoas.md`. Linha de
tabela nao e no de grafo: nao pode ser apontada, nao pode apontar, e nao pode
ligar a ferramenta, area ou demanda. Com ficha, pode.

Fonte: as tabelas `#### Solicitantes de demanda` que a varredura de 22 set 2026
escreveu no `pessoas.md` de cada cliente, a partir do campo `Quem solicitou?` das
demandas. Cada linha vira uma ficha.

O que NAO faz:
  - nao inventa cargo, area, e-mail nem nada que a fonte nao diga;
  - nao unifica grafias (regra do protocolo-varredura-cliente.md secao 9:
    suspeita se levanta, fusao so com confirmacao humana);
  - nao cria ficha para valor que nao e pessoa (area, time, agente, canal).

Estrutura: a MESMA do `_pessoas/_template_pessoa.md`, porque CLAUDE.md trava que
"Areas e Pessoas sao iguais entre Casa e clientes". Campo que so faz sentido para
a Casa fica marcado como nao aplicavel, nao apagado.

Uso:  python scripts/gera-fichas-pessoa.py
"""
import io
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")

# Valores que aparecem na coluna de nome e NAO sao pessoa.
NAO_PESSOA = set(u"""
compras estilo sourcing merchan planejamento negocios treinamento contrato
hermes ka smb interno time supply faccao qualidade cadastro comercial
""".split())


def slug(s):
    s = unicodedata.normalize(u"NFKD", s).encode(u"ascii", u"ignore").decode(u"ascii")
    s = re.sub(u"[^a-zA-Z0-9]+", u"-", s).strip(u"-").lower()
    return s


def limpa(cel):
    u"""Tira negrito, backtick e emoji de uma celula de tabela."""
    c = cel.strip()
    c = c.replace(u"**", u"").replace(u"`", u"")
    c = re.sub(u"[\U0001F300-\U0001FAFF⚠✅❌]", u"", c)
    return c.strip()


def e_pessoa(nome):
    n = slug(nome).replace(u"-", u" ")
    if not n or len(n) < 2:
        return False
    for t in NAO_PESSOA:
        if n == t or n.startswith(t + u" ") or n.endswith(u" " + t):
            return False
    if u" e " in n or u"/" in nome or u"+" in nome:
        return False  # duas pessoas na mesma celula: nao desmembro sem confirmacao
    if u"umode" in n:
        return False  # pessoa da Casa nao se duplica dentro do cliente
    return True


def ficha(cliente, nome, demandas, pri, ult, obs):
    L = []
    L.append(u"# %s · Pessoa · %s" % (cliente, nome))
    L.append(u"")
    L.append(u"> **Ficha gerada por `scripts/gera-fichas-pessoa.py` em 22 set 2026.**")
    L.append(u"> Campo sem fonte fica `[a preencher]` — **nada foi inferido.**")
    L.append(u"> **O nome está exatamente como aparece na fonte. Variantes não foram fundidas** —")
    L.append(u"> ver `protocolo-varredura-cliente.md` § 9.")
    L.append(u"")
    L.append(u"## Identificação")
    L.append(u"### Foto")
    L.append(u"`[a preencher]`")
    L.append(u"### Nome completo")
    L.append(u"`[a preencher]` — a fonte registra **`%s`**" % nome)
    L.append(u"### Nome preferido / como é chamado(a)")
    L.append(u"**%s**" % nome)
    L.append(u"### Email")
    L.append(u"`[a preencher]`")
    L.append(u"### Cadeira / cargo atual")
    L.append(u"`[a preencher]` — 🔴 **nenhuma fonte varrida traz cargo de pessoa de cliente**")
    L.append(u"### Nível HIC")
    L.append(u"⚠ **não se aplica** — é campo da Casa uMode")
    L.append(u"### Área (organizacional)")
    L.append(u"`[a preencher]` — 🔴 **o vínculo pessoa↔área é a lacuna aberta do corpus**")
    L.append(u"### Data de entrada na uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"### Status na uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"### Data de saída da uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"")
    L.append(u"## Papel")
    L.append(u"### Missão da cadeira")
    L.append(u"`[a preencher]`")
    L.append(u"### Responsabilidades principais")
    L.append(u"`[a preencher]`")
    L.append(u"### Interfaces")
    L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Histórico")
    L.append(u"### Áreas de atuação histórica")
    L.append(u"`[a preencher]`")
    L.append(u"### Clientes atuais atendidos")
    L.append(u"⚠ **não se aplica** — esta pessoa **é** do cliente `%s`" % cliente)
    L.append(u"### Clientes atendidos historicamente")
    L.append(u"⚠ **não se aplica**")
    L.append(u"")
    L.append(u"## Personificação")
    for h in (u"Como se descreve", u"Personalidade / forma de trabalhar",
              u"O que a diferencia", u"Curiosidade / algo pessoal"):
        L.append(u"### %s" % h)
        L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Competências")
    for h in (u"Experiência profissional anterior", u"Skills / habilidades técnicas",
              u"Cursos e certificações", u"Ferramentas e plataformas que domina"):
        L.append(u"### %s" % h)
        L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Atividade observada")
    L.append(u"")
    L.append(u"> **Uma pessoa não é ativa porque tem cadastro. É ativa porque agiu, numa data que")
    L.append(u"> dá para citar.**")
    L.append(u"")
    L.append(u"| Sinal | Valor |")
    L.append(u"|---|---|")
    L.append(u"| **Demandas abertas** | **%s** |" % demandas)
    L.append(u"| Primeira atividade observada | %s |" % (pri or u"`[a preencher]`"))
    L.append(u"| Última atividade observada | %s |" % (ult or u"`[a preencher]`"))
    L.append(u"| Fonte | campo `Quem solicitou?` da base de demandas do Notion |")
    if obs and obs != u"—":
        L.append(u"")
        L.append(u"**Observação da fonte:** %s" % obs)
    L.append(u"")
    L.append(u"## Governança")
    L.append(u"### Quem pode alterar este documento")
    L.append(u"Responsável de atendimento + liderança de Atendimento uMode")
    L.append(u"")
    return u"\n".join(L) + u"\n"


def main():
    criadas = 0
    clientes = 0
    for c in sorted(os.listdir(CLI)):
        base = os.path.join(CLI, c)
        pm = os.path.join(base, u"00_Institucional", u"_contexto", u"pessoas.md")
        if not os.path.exists(pm):
            continue
        s = io.open(pm, encoding="utf-8").read()
        if u"#### Solicitantes de demanda" not in s:
            continue
        bloco = s[s.index(u"#### Solicitantes de demanda"):]
        fim = bloco.find(u"\n## ")
        if fim > 0:
            bloco = bloco[:fim]
        destino = os.path.join(base, u"00_Institucional", u"_pessoas")
        if not os.path.isdir(destino):
            os.makedirs(destino)
        n_cli = 0
        for linha in bloco.split(u"\n"):
            if not linha.startswith(u"| ") or linha.startswith(u"|---") or u"Demandas |" in linha:
                continue
            cels = [limpa(x) for x in linha.strip().strip(u"|").split(u"|")]
            if len(cels) < 5:
                continue
            nome = cels[0]
            if not e_pessoa(nome):
                continue
            p = os.path.join(destino, slug(nome) + u".md")
            novo = ficha(c, nome, cels[1], cels[2], cels[3],
                         cels[4] if len(cels) > 4 else u"")
            if os.path.exists(p) and io.open(p, encoding="utf-8").read() == novo:
                continue
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1
        if n_cli:
            clientes += 1
            print(u"  %-20s %3d fichas" % (c, n_cli))
    print(u"")
    print(u"fichas de pessoa de cliente criadas/atualizadas: %d em %d clientes"
          % (criadas, clientes))
    print(u"Rode `python scripts/gera-conexoes.py` em seguida para ligá-las ao grafo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
