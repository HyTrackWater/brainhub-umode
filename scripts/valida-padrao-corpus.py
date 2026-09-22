# -*- coding: utf-8 -*-
"""valida-padrao-corpus.py - replica o padrao para TODA a classe de documento.

Regra travada pelo Vinicius: todo MD da mesma classe tem os mesmos titulos, sempre.
Conteudo varia por cliente; estrutura nunca varia. Se o padrao mudar, muda para a
classe inteira, retroativamente.

Este script NUNCA apaga conteudo. So insere heading canonico que falta, na posicao
certa, com corpo `[a preencher]`. Saida "0 completados" em todas as classes = padrao
integro; qualquer numero acima de zero significa que alguem quebrou o padrao, e o
motivo deve ser entendido antes do commit.

Vivia em scratchpad/propaga.py ate 22 set 2026, o que era um defeito: o scratchpad e
efemero e morre com a sessao, entao a ferramenta de verificacao citada pelo START.md
desaparecia. Promovido para scripts/ para ser durave.

Uso:  python scripts/valida-padrao-corpus.py
"""
import io, os, re, collections

RAIZ = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), u"uMode")
VAZIO = u"`[a preencher]`"

CANON = {
 u"institucional.md": [
  u"## Identidade", u"### ID do cliente", u"### Aliases do cliente", u"### Quem s\u00e3o",
  u"### O que fazem", u"### Para quem fazem",
  u"## Posicionamento", u"### Segmento", u"### Receita anual",
  u"### Grupo de segmenta\u00e7\u00e3o uMode",
  u"## Opera\u00e7\u00e3o uMode", u"### Status atual", u"### Data de ativa\u00e7\u00e3o",
  u"### M\u00f3dulos contratados", u"### Usu\u00e1rios da conta", u"### ERP / Integra\u00e7\u00e3o",
  u"### Respons\u00e1vel de atendimento (uMode)",
  u"## Aliases de \u00e1reas", u"### Mapeamento alias \u2192 can\u00f4nico",
  u"## Sistemas e fontes de verdade", u"### Drive de opera\u00e7\u00e3o", u"### Outras fontes",
  u"## Contexto cr\u00edtico", u"### Onde estamos", u"### \U0001f534 A frente aberta",
  u"### O que o cliente espera", u"### As dores estruturais registradas",
  u"### Tamanho de atendimento",
  u"## Governan\u00e7a", u"### Respons\u00e1vel de atendimento (uMode)",
  u"### Quem pode alterar este documento", u"### Proced\u00eancia",
 ],
 u"jornada.md": [
  u"## \u26a0 O que este documento N\u00c3O resolve",
  u"## Status atual", u"## Fase atual", u"## Marcos da jornada",
  u"## Entregas comprometidas", u"## M\u00f3dulos em uso",
  u"## Decis\u00f5es e restri\u00e7\u00f5es registradas", u"## M\u00e9tricas de sucesso definidas",
  u"## Pr\u00f3ximos passos", u"## Hist\u00f3rico de incidentes / alertas", u"## Observa\u00e7\u00f5es",
  u"## Governan\u00e7a", u"### Quem pode alterar este documento", u"### Proced\u00eancia",
 ],
 u"pessoas.md": [
  u"## Respons\u00e1vel de atendimento (uMode)", u"## Diretoria e decisores",
  u"## Lideran\u00e7a do projeto (cliente)", u"## Time do projeto por \u00e1rea",
  u"## Estado de atividade das pessoas", u"### Como o estado \u00e9 apurado",
  u"### Raz\u00e3o de pessoas", u"## Canais de comunica\u00e7\u00e3o",
  u"## Financeiro", u"## Tecnologia",
  u"## Governan\u00e7a", u"### Quem pode alterar este documento", u"### Proced\u00eancia",
 ],
 u"contexto-area.md": [
  u"## O que esta \u00e1rea faz", u"## Com quem se relaciona (interno e externo)",
  u"## Entregas e responsabilidades",
  u"## Padr\u00f5es operacionais", u"### Como trabalham", u"### O que n\u00e3o fazem",
  u"## Vocabul\u00e1rio da \u00e1rea", u"### Termos espec\u00edficos",
  u"## Produto conectado",
  u"## Fontes e refer\u00eancias", u"### Documentos que esta \u00e1rea consome",
  u"### Documentos que esta \u00e1rea produz",
  u"## Governan\u00e7a", u"### Respons\u00e1vel na empresa cliente",
  u"### Respons\u00e1vel de atendimento (uMode)", u"### Quem pode alterar este documento",
 ],
}

PROC = (u"| Bloco | Fonte | Data |\n|---|---|---|\n"
        u"| " + VAZIO + u" | " + VAZIO + u" | " + VAZIO + u" |")
DECL = (u"`[a preencher]` \u2014 **a lacuna vem antes da conquista: o que este documento n\u00e3o "
        u"cobre, e por qu\u00ea, vem antes do que ele cobre.**")
RAZAO = (u"`[a preencher]`\n\n"
         u"| Pessoa | E-mail | \u00c1rea | Estado | Evid\u00eancia (data) | Canal |\n"
         u"|---|---|---|---|---|---|\n"
         u"| " + VAZIO + u" | " + VAZIO + u" | " + VAZIO + u" | " + VAZIO
         + u" | " + VAZIO + u" | " + VAZIO + u" |")

CANAIS = (u"> **Cada canal \u00e9 uma entidade** \u2014 tem participantes, cad\u00eancia, dono e\n"
          u"> assunto. \u00c9 por aqui que a indexa\u00e7\u00e3o do c\u00e9rebro liga pessoa \u2194 ferramenta \u2194 \u00e1rea.\n\n"
          u"| Canal | Ferramenta | Quem participa | Cad\u00eancia | \u00daltimo registro |\n"
          u"|---|---|---|---|---|\n"
          u"| " + VAZIO + u" | " + VAZIO + u" | " + VAZIO + u" | " + VAZIO + u" | " + VAZIO + u" |")

APURA = (u"> **Uma pessoa n\u00e3o \u00e9 ativa porque tem cadastro. \u00c9 ativa porque agiu, numa data\n"
 u"> que d\u00e1 para citar.** Este eixo existe para a jornada do usu\u00e1rio: **quem atende o qu\u00ea,\n"
 u"> em qual ferramenta, em qual \u00e1rea.**\n\n"
 u"| Estado | O que significa | Evid\u00eancia que o sustenta |\n|---|---|---|\n"
 u"| `ATIVO` | agiu no sistema numa data conhecida | chamado aberto, presen\u00e7a em ata, a\u00e7\u00e3o registrada |\n"
 u"| `CADASTRADO` | tem acesso, **sem** evid\u00eancia de a\u00e7\u00e3o | consta na tabela de usu\u00e1rios e em nenhum canal |\n"
 u"| `DESATIVADO` | baixa declarada **na origem** | riscado, marcado inativo, acesso revogado |\n"
 u"| `ATIVO_SEM_CADASTRO` | agiu, mas **n\u00e3o consta** na lista de usu\u00e1rios | e-mail em chamado sem linha na tabela |\n"
 u"| `INDETERMINADO` | citado sem identificador \u00fanico | nome solto em ata, sem e-mail |\n\n"
 u"**`CADASTRADO` n\u00e3o \u00e9 `INATIVO`.** Aus\u00eancia de evid\u00eancia \u00e9 hip\u00f3tese, nunca conclus\u00e3o. "
 u"**Todo estado carrega a data da evid\u00eancia.** "
 u"**`DESATIVADO` s\u00f3 com marca\u00e7\u00e3o na fonte** \u2014 nunca por infer\u00eancia de inatividade.")

CORPO = {u"### Proced\u00eancia": PROC,
         u"## \u26a0 O que este documento N\u00c3O resolve": DECL,
         u"### Como o estado \u00e9 apurado": APURA,
         u"### Raz\u00e3o de pessoas": RAZAO,
         u"## Canais de comunica\u00e7\u00e3o": CANAIS}

def corpo_de(h):
    return CORPO.get(h, VAZIO)

def aplica(path, canon):
    linhas = io.open(path, encoding="utf-8").read().split(u"\n")
    presentes = {}
    for idx, l in enumerate(linhas):
        t = l.rstrip()
        if t in canon and t not in presentes:
            presentes[t] = idx
    faltando = [h for h in canon if h not in presentes]
    if not faltando:
        return 0
    # insere de tras pra frente para nao invalidar indices
    for h in reversed(faltando):
        pos_canon = canon.index(h)
        # ancora: ultimo canonico anterior que existe
        anc = None
        for k in range(pos_canon - 1, -1, -1):
            if canon[k] in presentes:
                anc = canon[k]; break
        if anc is None:
            # antes do primeiro canonico existente, ou logo apos o titulo H1
            alvo = min(presentes.values()) if presentes else 1
        else:
            i = presentes[anc]
            j = i + 1
            nivel = len(anc) - len(anc.lstrip(u"#"))
            while j < len(linhas):
                t = linhas[j].rstrip()
                if t.startswith(u"#"):
                    n = len(t) - len(t.lstrip(u"#"))
                    if n <= nivel:
                        break
                    if t in canon and canon.index(t) > pos_canon:
                        break
                j += 1
            alvo = j
        linhas[alvo:alvo] = [h, u"", corpo_de(h), u""]
        presentes = {}
        for idx, l in enumerate(linhas):
            t = l.rstrip()
            if t in canon and t not in presentes:
                presentes[t] = idx
    out = re.sub(u"\n{3,}", u"\n\n", u"\n".join(linhas)).rstrip() + u"\n"
    io.open(path, "w", encoding="utf-8", newline="").write(out)
    return len(faltando)

cont = collections.Counter()
tocados = collections.Counter()
for dirpath, _, files in os.walk(RAIZ):
    for f in files:
        if f in CANON:
            cont[f] += 1
            if aplica(os.path.join(dirpath, f), CANON[f]):
                tocados[f] += 1

for f in sorted(CANON):
    print(u"%-20s %3d arquivos  |  %3d completados" % (f, cont[f], tocados[f]))
