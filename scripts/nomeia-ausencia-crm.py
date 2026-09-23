# -*- coding: utf-8 -*-
u"""
nomeia-ausencia-crm.py - fecha os `[sem fonte]` que sobraram, que sao quase
todos campo de CRM ou de contrato nos ~35 clientes menores.

DUAS FONTES, LIDAS HOJE:
  base `Mapa de Clientes` - lida por SQL em 23/09/2026, os 50 registros, para
    Modulos Contratados, ERP/Integracao, Atendimento 2025 e Segmentacao.
  planilha de contratos do Financeiro - 41 registros, conferidos um a um.

O QUE O SCRIPT FAZ, E O QUE ELE SE RECUSA A FAZER:

  campo VAZIO na base + MD vazio  -> reescreve como ausencia verificada,
                                     nomeando a base e a data.
  campo CHEIO na base + MD vazio  -> \U0001F534 **NAO reescreve: ACUSA.** A base tem
                                     dado que o corpus nao extraiu. Escrever
                                     "vazio" ali seria apagar dado real, e
                                     essa lista e trabalho de varredura.

A tabela de presenca abaixo e DADO DATADO - uma foto de 23/09/2026 - nao
verdade permanente. Quem nao aparece na tabela tem os quatro campos vazios.
"""
import io, os, json, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")
CONTRATOS = u"C:/Users/Vinicius/Downloads/clientes-umode.json"
HOJE = u"23/09/2026"

# base viva, 23/09/2026. Letra presente = campo PREENCHIDO naquele cliente.
#   m = Modulos Contratados · e = ERP/Integracao
#   a = Atendimento 2025    · s = Segmentacao Grupos
PRESENCA = {
 u"4takes": u"meas", u"Arezzo": u"es", u"Baw": u"meas", u"B\u00e1sico&Co": u"s",
 u"Caedu": u"meas", u"Cambos": u"meas", u"Camys": u"meas", u"Cavallari": u"meas",
 u"Colmeia": u"es", u"DRO": u"s", u"Hering": u"es", u"Highstil": u"eas",
 u"Hyperlocal": u"e", u"Ladeira Bijuterias": u"s", u"Lenny Niemeyer": u"eas",
 u"Lofty Style": u"meas", u"Loj\u00e3o do Br\u00e1s": u"s", u"Loungerie": u"eas",
 u"Luiza Barcelos": u"meas", u"Moda Objetiva": u"meas", u"Mondepars": u"meas",
 u"NK STORE": u"meas", u"NTK": u"s", u"NV": u"meas", u"Oficina Reserva": u"meas",
 u"Osklen": u"meas", u"Plie": u"a", u"Puket": u"meas", u"Recco": u"es",
 u"Reserva": u"meas", u"Seven Global": u"m", u"Studio Minah": u"meas",
 u"Studio Z": u"mes", u"TDC": u"meas", u"Texneo": u"s", u"Ton Age": u"meas",
 u"Vivara": u"me", u"VIX": u"meas",
}

# secao -> (letra na tabela de presenca, rotulo do campo na base)
CAMPOS_CRM = [
 (u"### M\u00f3dulos contratados",              u"m", u"M\u00f3dulos Contratados"),
 (u"## M\u00f3dulos em uso",                    u"m", u"M\u00f3dulos Contratados"),
 (u"### ERP / Integra\u00e7\u00e3o",                  u"e", u"ERP/Integra\u00e7\u00e3o"),
 (u"### Respons\u00e1vel de atendimento (uMode)", u"a", u"Atendimento 2025"),
 (u"### Grupo de segmenta\u00e7\u00e3o uMode",        u"s", u"Segmenta\u00e7\u00e3o Grupos"),
 (u"### Tamanho de atendimento",             u"s", u"Segmenta\u00e7\u00e3o Grupos"),
]

SECOES_CONTRATO = [u"### Situa\u00e7\u00e3o do contrato", u"### Vig\u00eancia",
                   u"### Renova\u00e7\u00e3o e aviso pr\u00e9vio", u"### \u00cdndice de reajuste",
                   u"### Usu\u00e1rios contratados"]

# so quatro contas tem tabela de usuarios do PLM varrida (item 661)
COM_TABELA_PLM = {u"Caedu", u"Puket", u"NK STORE"}


def texto_crm(rotulo):
    return (u"`[a preencher]` \u2014 campo **`%s` vazio na base `Mapa de Clientes`**.\n"
            u"> \U0001F534 **Aus\u00eancia VERIFICADA:** os 50 registros da base foram lidos por SQL em "
            u"**%s**. **Vazio neste cliente.**" % (rotulo, HOJE))


def texto_contrato(cliente):
    return (u"`[a preencher]` \u2014 \U0001F534 **`%s` n\u00e3o consta na planilha de contratos do "
            u"Financeiro.**\n"
            u"> **Aus\u00eancia VERIFICADA:** os **41 registros** da base foram conferidos um a um em "
            u"**%s**. \u26a0 **A aus\u00eancia \u00e9 da fonte** \u2014 ou o contrato existe fora dela, ou n\u00e3o "
            u"existe. **Quem confirma \u00e9 o Financeiro.**" % (cliente, HOJE))


def texto_usuarios_conta(cliente):
    return (u"`[a preencher]` \u2014 \U0001F534 **n\u00e3o h\u00e1 tabela de usu\u00e1rios do PLM varrida para esta "
            u"conta.**\n"
            u"> **Aus\u00eancia VERIFICADA em %s.** No corpus inteiro, s\u00f3 **Caedu, Puket e NK STORE** "
            u"t\u00eam tabela de usu\u00e1rios lida. \u26a0 **N\u00e3o afirmo que a conta n\u00e3o tenha usu\u00e1rios** \u2014 "
            u"afirmo que **n\u00e3o h\u00e1 fonte varrida que os liste.**" % HOJE)


def clientes_do_contrato():
    if not os.path.exists(CONTRATOS):
        return None
    d = json.load(io.open(CONTRATOS, encoding=u"utf-8"))
    regs = d if isinstance(d, list) else next(
        (v for v in d.values() if isinstance(v, list)), [])
    nomes = set()
    for r in regs:
        for k in (u"nome", u"Nome", u"cliente", u"nome_planilha", u"razao_social"):
            v = r.get(k) if isinstance(r, dict) else None
            if v:
                nomes.add(unicode(v).lower() if sys.version_info[0] < 3 else str(v).lower())
    return nomes


def no_contrato(cliente, nomes):
    if nomes is None:
        return None
    c = cliente.lower()
    return any(c in n or n.startswith(c) for n in nomes)


def troca(txt, sec, corpo):
    marca = u"\n" + sec + u"\n"
    if marca not in txt:
        return txt, False, False
    antes, resto = txt.split(marca, 1)
    corte = len(resto)
    for h in (u"\n## ", u"\n### "):
        i = resto.find(h)
        if i != -1:
            corte = min(corte, i)
    corpo_atual, cauda = resto[:corte], resto[corte:]
    if u"Aus\u00eancia VERIFICADA" in corpo_atual or u"a preencher" not in corpo_atual:
        return txt, False, (u"a preencher" not in corpo_atual)
    return antes + marca + u"\n" + corpo + u"\n" + cauda, True, False


def main():
    nomes_contrato = clientes_do_contrato()
    clientes = sorted(d for d in os.listdir(CLI)
                      if os.path.isdir(os.path.join(CLI, d)) and not d.startswith(u"_"))
    trocas, acusados = 0, []

    for cliente in clientes:
        pres = PRESENCA.get(cliente, u"")
        base = os.path.join(CLI, cliente, u"00_Institucional", u"_contexto")
        for arq in (u"institucional.md", u"jornada.md"):
            caminho = os.path.join(base, arq)
            if not os.path.exists(caminho):
                continue
            txt = io.open(caminho, encoding=u"utf-8").read()
            antes = txt

            for sec, letra, rotulo in CAMPOS_CRM:
                if sec not in txt:
                    continue
                if letra in pres:
                    # a base TEM dado: nao reescrever, acusar se o MD estiver vazio
                    _, _, preenchido = troca(txt, sec, u"")
                    if not preenchido:
                        acusados.append((cliente, rotulo, sec))
                    continue
                txt, ok, _ = troca(txt, sec, texto_crm(rotulo))
                if ok:
                    trocas += 1

            if arq == u"institucional.md":
                tem = no_contrato(cliente, nomes_contrato)
                if tem is False:
                    for sec in SECOES_CONTRATO:
                        txt, ok, _ = troca(txt, sec, texto_contrato(cliente))
                        if ok:
                            trocas += 1
                if cliente not in COM_TABELA_PLM:
                    txt, ok, _ = troca(txt, u"### Usu\u00e1rios da conta",
                                       texto_usuarios_conta(cliente))
                    if ok:
                        trocas += 1

            if txt != antes:
                io.open(caminho, u"w", encoding=u"utf-8").write(txt)

    w = sys.stdout.write
    w(u"secoes reescritas como ausencia verificada: %d\n" % trocas)
    if nomes_contrato is None:
        w(u"\u26a0 base de contratos nao encontrada: secoes de contrato nao tocadas\n")
    if acusados:
        w(u"\n\U0001F534 CORPUS DEFASADO (%d) - a base TEM dado e o MD esta vazio.\n"
          % len(acusados))
        w(u"   Nao reescrevi: escrever 'vazio' apagaria dado real. E varredura a fazer:\n")
        for cli, rotulo, sec in acusados:
            w(u"   - %-20s %-22s %s\n" % (cli, rotulo, sec))
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
