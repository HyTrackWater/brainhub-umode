# -*- coding: utf-8 -*-
import io, sys, json
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\Vinicius\.claude\projects\C--Ambientes-Virtuais-BrainHub-brainhub-umode\76bedddf-cfb1-4ab7-9d9e-6a5d6536ec9e\tool-results\mcp-3e654692-6abb-4514-a24f-774dbdf0dc4b-notion-query-data-sources-1790168389277.txt"
d = json.load(io.open(p, encoding="utf-8"))["results"]
ALVO = ["Osklen","NK STORE","Reserva","VIX","Lofty Style","Puket","NV","Oficina Reserva",
        "Cambos","Luiza Barcelos","Moda Objetiva","Baw","Loungerie","Lenny Niemeyer","Recco"]
out = {}
for r in d:
    n = str(r.get("Nome Fantasia") or "")
    for a in ALVO:
        if n.strip().lower() == a.lower():
            out[a] = r["id"].replace("-", "")
for a in ALVO:
    print("%-18s %s" % (a, out.get(a, "*** NAO ACHADO ***")))
io.open("_alvos.json","w",encoding="utf-8").write(json.dumps(out, ensure_ascii=False))
print("\nachados: %d de %d" % (len(out), len(ALVO)))
