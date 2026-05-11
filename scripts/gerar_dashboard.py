#!/usr/bin/env python3
"""Gera dashboard HTML simples com volume, MTTR e taxa de remoção."""
from __future__ import annotations
import csv
from datetime import datetime, UTC
from pathlib import Path

INPUT = Path("data/incidentes_exemplo.csv")
OUTPUT = Path("dashboard/index.html")


def parse_dt(v: str):
    return datetime.fromisoformat(v.replace("Z", "+00:00")) if v else None


def main():
    rows = list(csv.DictReader(INPUT.open()))
    total = len(rows)
    resolvidos = [r for r in rows if r["status"] == "resolvido" and r["data_resolucao"]]
    removidos = len(resolvidos)
    taxa_remocao = (removidos / total * 100) if total else 0

    duracoes_horas = []
    for r in resolvidos:
        ini = parse_dt(r["data_abertura"])
        fim = parse_dt(r["data_resolucao"])
        if ini and fim and fim >= ini:
            duracoes_horas.append((fim - ini).total_seconds() / 3600)
    mttr = sum(duracoes_horas) / len(duracoes_horas) if duracoes_horas else 0

    por_severidade = {}
    for r in rows:
        por_severidade[r["severidade"]] = por_severidade.get(r["severidade"], 0) + 1

    sev_html = "".join(f"<li>{k}: {v}</li>" for k, v in sorted(por_severidade.items()))
    html = f"""<!doctype html>
<html lang='pt-BR'><meta charset='utf-8'><title>Dashboard Antifraude</title>
<body style='font-family: Arial; margin: 24px'>
<h1>Dashboard Antifraude</h1>
<p><b>Volume total de incidentes:</b> {total}</p>
<p><b>MTTR (horas):</b> {mttr:.2f}</p>
<p><b>Taxa de remoção:</b> {taxa_remocao:.1f}%</p>
<h2>Volume por severidade</h2>
<ul>{sev_html}</ul>
<p>Atualizado em: {datetime.now(UTC).isoformat()}Z</p>
</body></html>"""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"dashboard gerado em {OUTPUT}")


if __name__ == "__main__":
    main()
