# -*- coding: utf-8 -*-
u"""
valida-documentacao.py — confere que o manifesto do START.md e o disco batem.

Por que existe: ate 22 set 2026 ninguem declarava o conjunto de documentacao, entao arquivo
orfao so aparecia por acidente (o `_indice/README.md` e o `_pendencias-gerais.md` passaram
meses sem serem citados por nada). Com o manifesto declarado na secao 1 do START.md, a
divergencia vira erro verificavel em vez de descoberta.

Escrito em Python, e nao em PowerShell como os demais scripts/, de proposito: o PS 5.1 desta
maquina le .ps1 sem BOM como ANSI e corrompe acento, o que ja custou varias correcoes.

Uso:  python scripts/valida-documentacao.py
Saida: 0 se tudo bate, 1 se ha divergencia.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pastas cujo conteudo e corpus ou dado gerado, nao documentacao estrutural.
IGNORA_DIR = (
    u".git",
    os.path.join(u"uMode", u"_Clientes"),
    u"scratchpad",
)

# Arquivos que sao corpus replicado por area/produto: governados pelo propaga.py,
# nao pelo manifesto.
CORPUS = (u"contexto-area.md", u"produto.md", u"institucional.md", u"jornada.md", u"pessoas.md")


def normaliza(caminho):
    return caminho.replace(u"\\", u"/")


def estruturais():
    u"""Todo .md que o manifesto precisa classificar."""
    achados = []
    for pasta, subpastas, arquivos in os.walk(RAIZ):
        rel = normaliza(os.path.relpath(pasta, RAIZ))
        if any(normaliza(ig) in rel or rel.startswith(normaliza(ig)) for ig in IGNORA_DIR):
            subpastas[:] = []
            continue
        for nome in arquivos:
            if not nome.endswith(u".md"):
                continue
            caminho = normaliza(os.path.join(rel, nome)) if rel != u"." else nome
            # corpus replicado: so entra se for o institucional.md da Casa
            if nome in CORPUS and not caminho.startswith(u"uMode/00_Institucional/"):
                continue
            # demandas, rfis e pessoas individuais sao registros do corpus;
            # os _template_ dentro dessas pastas SAO estruturais e entram.
            if (u"/_demandas/" in caminho or u"/_rfis/" in caminho)                     and not nome.startswith(u"_template"):
                continue
            if u"/_pessoas/" in caminho and not nome.startswith(u"_template"):
                continue
            achados.append(caminho)
    return sorted(achados)


def manifesto():
    u"""Nomes de arquivo citados na secao 1 do START.md."""
    p = os.path.join(RAIZ, u"START.md")
    texto = io.open(p, encoding=u"utf-8").read()
    ini = texto.index(u"## 1 · O TIME")
    fim = texto.index(u"## 2 · A ordem de leitura")
    bloco = texto[ini:fim]
    citados = set(re.findall(u"`([^`]+\\.md)`", bloco))
    # pastas citadas como conjunto, cujo conteudo o manifesto cobre em bloco
    pastas = set()
    for padrao in (u"brainwave/", u"uMode/04_Dados-e-IA/_boilerplate/",
                   u"uMode/04_Dados-e-IA/_inbox-hermes/",
                   u"_Clientes/_template_cliente/", u"03_Produto-e-Solucoes/_template_produto/",
                   u"_indice/"):
        if padrao in bloco:
            pastas.add(padrao)
    return citados, pastas


# Nomes de CLASSE do corpus citados no manifesto: sao tipos de arquivo, nao caminhos.
CLASSES = (u"contexto-area.md", u"produto.md", u"jornada.md", u"pessoas.md")


def coberto(caminho, citados, pastas):
    nome = caminho.split(u"/")[-1]
    if nome in citados or caminho in citados:
        return True
    # o manifesto pode citar com caminho parcial: `_pessoas/_template_pessoa.md`
    for c in citados:
        if caminho.endswith(c) or c.endswith(u"/" + nome):
            return True
    for pasta in pastas:
        if pasta in caminho:
            return True
    return False


def main():
    citados, pastas = manifesto()
    disco = estruturais()

    orfaos = [c for c in disco if not coberto(c, citados, pastas)]

    nomes_disco = set(c.split(u"/")[-1] for c in disco)
    nomes_disco |= set(disco)
    fantasmas = []
    for c in sorted(citados):
        nome = c.split(u"/")[-1]
        if nome in CLASSES:
            continue  # nome de classe do corpus, nao um arquivo unico
        if nome in nomes_disco or c in nomes_disco:
            continue
        if os.path.exists(os.path.join(RAIZ, *c.split(u"/"))):
            continue
        if any(d.endswith(u"/" + nome) or d == nome for d in disco):
            continue
        fantasmas.append(c)

    print(u"Estruturais no disco : %d" % len(disco))
    print(u"Citados no manifesto : %d" % len(citados))

    if orfaos:
        print(u"\n❌ ORFAOS — existem no disco e o manifesto do START.md nao cita:")
        for o in orfaos:
            print(u"   %s" % o)
    if fantasmas:
        print(u"\n❌ FANTASMAS — o manifesto cita e nao existem no disco:")
        for f in fantasmas:
            print(u"   %s" % f)

    if orfaos or fantasmas:
        print(u"\nResolva antes de commitar: ou o arquivo entra no manifesto (START.md § 1),")
        print(u"ou ele nao devia existir. Arquivo orfao e como a lacuna reaparece.")
        return 1

    print(u"\n✅ Manifesto e disco batem. Nenhum .md estrutural orfao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
