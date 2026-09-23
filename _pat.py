# -*- coding: utf-8 -*-
import io
p = "scripts/valida-padrao-corpus.py"
t = io.open(p, encoding="utf-8", newline="").read()
velho = u'  u"## Aliases de \u00e1reas", u"### Mapeamento alias \u2192 can\u00f4nico",'
assert velho in t, "ancora nao encontrada"
novo = (u'  u"## Contrato", u"### Situa\u00e7\u00e3o do contrato", u"### Vig\u00eancia",\n'
        u'  u"### Renova\u00e7\u00e3o e aviso pr\u00e9vio", u"### \u00cdndice de reajuste",\n'
        u'  u"### Usu\u00e1rios contratados", u"### Pend\u00eancias contratuais registradas",\n'
        + velho)
t = t.replace(velho, novo, 1)
t = t.replace(u"CORPO = {",
  u'CONTRATO_NOTA = (u"`[a preencher]` \u2014 \U0001F534 **A autoridade deste bloco \u00e9 a base de "\n'
  u'                 u"contratos do Financeiro**, n\u00e3o o Notion. Ver "\n'
  u'                 u"`_recebido-2026-09-23-base-contratos-flavia-campello.md`.")\n\n'
  u'CORPO = {\n u"## Contrato": CONTRATO_NOTA,', 1)
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("CANON: secao Contrato acrescentada")
