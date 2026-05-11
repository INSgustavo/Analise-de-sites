# Programa Antifraude Corporativo — Vortx Grafeno

Implementação inicial da operação antifraude com foco em phishing/impersonação:
- formulário único de intake;
- severidade objetiva (Crítica/Alta/Média/Baixa);
- fila única com SLA por severidade;
- templates de comunicação;
- automação inicial para enriquecimento de IOC.

## Estrutura
- `ops/formulario_intake.md`
- `ops/severidade_sla.md`
- `templates/registro_incidente.md`
- `templates/respostas/cliente_p1_p2.md`
- `templates/respostas/provedor_takedown.md`
- `scripts/enriquecimento_ioc.py`
