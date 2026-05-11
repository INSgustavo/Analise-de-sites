# Dashboard de Volume, MTTR e Taxa de Remoção

Este dashboard é gerado pelo script `scripts/gerar_dashboard.py` a partir do arquivo CSV `data/incidentes_exemplo.csv`.

## Como gerar
```bash
python3 scripts/gerar_dashboard.py
```

## Métricas
- **Volume**: total de incidentes no período.
- **MTTR**: tempo médio (em horas) entre abertura e resolução para casos resolvidos.
- **Taxa de remoção**: percentual de incidentes resolvidos sobre o total.
