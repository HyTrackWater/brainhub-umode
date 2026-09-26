# -*- coding: utf-8 -*-
u"""
transcreve-gravacoes.py - transcreve as gravacoes do Meet que NAO tem resumo do
Gemini, na ordem da fila (contas vivas primeiro), com `faster-whisper` em CPU.

POR QUE EXISTE. O acervo da Marina tem 194 gravacoes; 122 nao tem resumo com o
mesmo titulo e data - o conteudo delas so existe em video. Decisao do Vinicius
em 25/09/2026: transcrever SO essas 122, comecando pelas contas vivas.

\U0001F534 O QUE NAO ENTRA NO REPOSITORIO. Nem o video nem a transcricao bruta.
A saida vai para a pasta temporaria da sessao, ao lado do acervo, e o extrator
de propostas le de la - o que entra no corpus e a proposta, filtrada por T0,
T0-P e T1, como para qualquer outra reuniao.

\u26a0 O QUE A TRANSCRICAO NAO TEM:
  - FALANTE. Whisper nao separa quem fala. A transcricao e fala sem dono -
    serve para conteudo e tempo, nao para identidade nem para juizo sobre
    pessoa (o que, alias, reduz o risco T0-P).
  - Garantia de exatidao. Reconhecimento de fala em reuniao de moda erra nome
    de campo, de sistema e de pessoa. Tudo o que sair daqui e DERIVADO.

RETOMAVEL. Cada gravacao gera um .txt; se ele ja existe, pula. Pode ser
interrompido e relancado sem perder o que foi feito.

Uso:  C:/Users/Vinicius/.asr/Scripts/python scripts/transcreve-gravacoes.py [--limite N] [--modelo small]
"""
import io, os, sys, time, zipfile, argparse, datetime

SCRATCH = (u"C:/Users/Vinicius/AppData/Local/Temp/claude/"
           u"C--Ambientes-Virtuais-BrainHub-brainhub-umode/"
           u"76bedddf-cfb1-4ab7-9d9e-6a5d6536ec9e/scratchpad/marina/")
FILA = SCRATCH + u"_fila_transcricao.tsv"
SAIDA = SCRATCH + u"transcricoes/"
TMP = u"C:/Users/Vinicius/.asr/tmp/"      # caminho curto: MAX_PATH do Windows
LOG = SAIDA + u"_log.tsv"


def hms(s):
    s = int(s)
    return u"%02d:%02d:%02d" % (s // 3600, s % 3600 // 60, s % 60)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(u"--limite", type=int, default=0)
    ap.add_argument(u"--modelo", default=u"small")
    # segunda fila em paralelo (ex.: gravacoes COM resumo, para conferir o
    # presente das contas vivas): outra fila, outra saida, outro temporario
    ap.add_argument(u"--fila", default=FILA)
    ap.add_argument(u"--saida", default=SAIDA)
    ap.add_argument(u"--tmp", default=TMP + u"atual.mp4")
    ap.add_argument(u"--threads", type=int, default=max(1, (os.cpu_count() or 4) - 1))
    a = ap.parse_args()
    saida = a.saida.rstrip(u"/") + u"/"
    log = saida + u"_log.tsv"
    from faster_whisper import WhisperModel
    os.makedirs(saida, exist_ok=True)
    os.makedirs(os.path.dirname(a.tmp), exist_ok=True)
    modelo = WhisperModel(a.modelo, device=u"cpu", compute_type=u"int8", cpu_threads=a.threads)
    fila = [l.split(u"\t") for l in io.open(a.fila, encoding=u"utf-8").read().splitlines() if l]
    feitos = 0
    for n, (prio, data, zipf, membro, base, pasta, status, tam) in enumerate(fila, 1):
        alvo = saida + u"%03d.txt" % n
        if os.path.exists(alvo):
            continue
        if a.limite and feitos >= a.limite:
            break
        t0 = time.time()
        tmp = a.tmp
        with zipfile.ZipFile(zipf) as z, z.open(membro) as src, open(tmp, u"wb") as dst:
            while True:
                b = src.read(1 << 22)
                if not b:
                    break
                dst.write(b)
        segs, info = modelo.transcribe(tmp, language=u"pt", vad_filter=True, beam_size=1)
        linhas = [u"# %s" % base, u"# data: %s · cliente (do t\u00edtulo): %s · status no corpus: %s" % (data, pasta, status),
                  u"# modelo: faster-whisper %s \u00b7 SEM falante \u00b7 derivado" % a.modelo, u""]
        for s in segs:
            linhas.append(u"[%s] %s" % (hms(s.start), s.text.strip()))
        io.open(alvo + u".parcial", u"w", encoding=u"utf-8").write(u"\n".join(linhas))
        os.replace(alvo + u".parcial", alvo)
        os.remove(tmp)
        dur = info.duration or 0
        gasto = time.time() - t0
        io.open(log, u"a", encoding=u"utf-8").write(u"%03d\t%s\t%s\t%.0f\t%.0f\t%.2f\t%s\n" % (
            n, data, pasta, dur, gasto, (dur / gasto) if gasto else 0, datetime.datetime.now().isoformat(u" ", u"seconds")))
        feitos += 1
        print(u"%03d/%d  %s  %-16s audio %s em %s  (%.1fx)" % (
            n, len(fila), data, pasta[:16], hms(dur), hms(gasto), (dur / gasto) if gasto else 0), flush=True)
    return 0


if __name__ == u"__main__":
    sys.exit(main())
