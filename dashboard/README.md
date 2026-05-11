# Painel de Volume, MTTR e Taxa de Remoção

Este painel é gerado pelo arquivo `scripts/gerar_dashboard.py` a partir da planilha CSV `data/incidentes_exemplo.csv`.

## Como gerar
```bash
python3 scripts/gerar_dashboard.py
```

## Métricas
- **Volume**: total de incidentes no período.
- **MTTR**: tempo médio (em horas) entre abertura e resolução para casos resolvidos.
- **Taxa de remoção**: percentual de incidentes resolvidos sobre o total.
