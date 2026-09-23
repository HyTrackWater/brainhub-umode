# -*- coding: utf-8 -*-
u"""gera-fichas-umoder.py - fichas de pessoa da CASA uMode.

Por que existe separado do `gera-fichas-pessoa.py`: pessoa de CLIENTE e pessoa da
CASA tem campos opostos. Na ficha de cliente, `Nivel HIC`, `Data de entrada na
uMode` e `Status na uMode` sao "nao se aplica"; na ficha da Casa eles sao o miolo.

Fonte: database `uModers` do Notion (`collection://c82a689c-704c-42aa-8752-bfae592f91bd`),
lida em 23 set 2026. 80 linhas, 78 pessoas reais.

O QUE ESTE SCRIPT NAO FAZ, de proposito:
- Nao sobrescreve ficha que ja existe. As 17 primeiras foram escritas a mao, com
  curadoria e ressalvas que um gerador destruiria.
- Nao inventa `Area`. A base tem `Area` preenchida em 18 de 80 e com so 2 valores
  (Operacao, Tecnologia) - NAO e a grade de 8 areas internas da uMode.
- Nao data saida. A base NAO TEM campo de saida: desligamento so aparece como
  `Situacao = Inativo`, sem data.
"""
import io, os, re, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, u"uMode", u"00_Institucional", u"_pessoas")
FONTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), u"_dados-umoders.txt")

def slug(s):
    s = unicodedata.normalize(u"NFKD", s).encode(u"ascii", u"ignore").decode()
    return re.sub(u"-+", u"-", re.sub(u"[^a-z0-9]+", u"-", s.lower())).strip(u"-")

def v(x):
    return u"" if x.strip() == u"VAZIO" else x.strip()

def ficha(nome, funcao, area, email, situacao, cadeira):
    L = [u"# %s · Pessoa" % nome, u"", 
         u"> **Ficha gerada por `scripts/gera-fichas-umoder.py` em 23 set 2026**, a partir da base",
         u"> `uModers` do Notion. Campo sem fonte fica `[a preencher]` — **nada foi inferido.**", u"",
         u"## Identificação", u"### Foto", u"`[a preencher]`",
         u"### Nome completo", u"**%s**" % nome,
         u"### Nome preferido / como é chamado(a)", u"`[a preencher]`",
         u"### Email"]
    if email:
        L += [u"**`%s`** — e-mail **corporativo**, da base `uModers`." % email, u"",
              u"🟢 **É a chave de identidade desta pessoa** (item 252). Tier `T2`.", u"",
              u"⚠ **A base também traz telefone, endereço residencial com CEP e data de "
              u"nascimento — `T0`, nenhum copiado.** Registro que existem e onde."]
    else:
        L += [u"`[a preencher]` — 🔴 **a base `uModers` não traz e-mail para esta pessoa.**"]
    L += [u"### Cadeira / cargo atual"]
    if cadeira:
        L += [u"**%s**" % cadeira, u"",
              u"> Campo `Cadeira` da base — é *rollup* da relação `Posições`. "
              u"⚠ **A senioridade vive dentro do nome da cadeira**, não em campo próprio."]
    elif funcao:
        L += [u"**%s**" % funcao, u"",
              u"> Campo `Função` da base. ⚠ **`Cadeira` está vazia para esta pessoa** — "
              u"a base a preenche em 43 de 80."]
    else:
        L += [u"`[a preencher]` — 🔴 **nem `Função` nem `Cadeira` preenchidas na base.**"]
    L += [u"### Nível HIC", u"`[a preencher — escala e critério de triagem ainda não definidos]`",
          u"### Área (organizacional)"]
    if area:
        L += [u"`[a preencher]` — ⚠ **a base traz `%s`, mas esse campo NÃO é a grade de 8 áreas "
              u"internas da uMode.**" % area, u"",
              u"> 🔴 A coluna `Área` da base `uModers` tem **só dois valores** (`Operação`, "
              u"> `Tecnologia`) e está preenchida em **18 de 80**. A relação `Posições` aponta "
              u"> para outra base, com **outro** campo `Área` e valores diferentes. "
              u"> **São duas taxonomias distintas — não derivei uma da outra.**"]
    else:
        L += [u"`[a preencher]` — a base não traz área para esta pessoa."]
    L += [u"### Data de entrada na uMode",
          u"`[a preencher]` — ⚠ **a base preenche `Início` em apenas 7 de 80**, todas contratações "
          u"de 2025–2026.",
          u"### Status na uMode", u"**%s** — campo `Situação` da base `uModers`." % situacao,
          u"### Data de saída da uMode"]
    if situacao.lower() == u"inativo":
        L += [u"`[a preencher]` — 🔴 **a base `uModers` NÃO TEM campo de saída.** O desligamento "
              u"aparece só como `Situação = Inativo`, **sem data**. "
              u"**Não há como datar a saída por esta fonte.**"]
    else:
        L += [u"⚠ **não se aplica** — pessoa ativa."]
    L += [u"", u"## Papel", u"### Missão da cadeira", u"`[a preencher]`",
          u"### Responsabilidades principais", u"`[a preencher]`",
          u"### Interfaces", u"`[a preencher]`", u"",
          u"## Histórico", u"### Áreas de atuação histórica", u"`[a preencher]`",
          u"### Clientes atuais atendidos", u"`[a preencher]`",
          u"### Clientes atendidos historicamente", u"`[a preencher]`", u"",
          u"## Personificação", u"### Como se descreve",
          u"`[a preencher]` — ⚠ a base tem um campo `Mini Bio` preenchido em 49 de 80. **Não lido.**",
          u"### Personalidade / forma de trabalhar", u"`[a preencher]`",
          u"### O que a diferencia", u"`[a preencher]`",
          u"### Curiosidade / algo pessoal", u"`[a preencher]`", u"",
          u"## Competências", u"### Experiência profissional anterior", u"`[a preencher]`",
          u"### Skills / habilidades técnicas", u"`[a preencher]`",
          u"### Cursos e certificações", u"`[a preencher]`",
          u"### Ferramentas e plataformas que domina",
          u"`[a preencher]` — ⚠ a base tem `Ferramentas responsável`, preenchido em 13 de 80.", u"",
          u"## Governança", u"### Fonte dos dados documentáveis",
          u"Base `uModers` do Notion (`collection://c82a689c-…`), lida em **23 set 2026**.",
          u"### Quem pode alterar este documento",
          u"Liderança de Pessoas e Cultura + CEO", u""]
    return u"\n".join(L)

def main():
    if not os.path.isfile(FONTE):
        print(u"fonte nao encontrada: %s" % FONTE); return 1
    criadas, existiam = 0, []
    for linha in io.open(FONTE, encoding="utf-8"):
        if not linha.strip(): continue
        p = linha.rstrip(u"\n").split(u"|")
        if len(p) < 6: continue
        nome, funcao, area, email, situacao, cadeira = [v(x) for x in p[:6]]
        if not nome: continue
        alvo = os.path.join(DEST, slug(nome) + u".md")
        if os.path.exists(alvo):
            existiam.append(slug(nome)); continue
        io.open(alvo, "w", encoding="utf-8", newline="").write(
            ficha(nome, funcao, area, email, situacao or u"[a preencher]", cadeira))
        criadas += 1
    print(u"fichas de uModer criadas: %d" % criadas)
    if existiam:
        print(u"ja existiam, NAO sobrescritas (%d): %s" % (len(existiam), u", ".join(existiam)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
