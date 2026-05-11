# Proposta de Melhorias (Implementada no repositório)

## Curto prazo (0–30 dias) — implementado
- [x] Padronizar intake com formulário único (`ops/formulario_intake.md`).
- [x] Definir severidade (Crítica/Alta/Média/Baixa) com critérios objetivos (`ops/severidade_sla.md`).
- [x] Criar fila única de triagem e SLA por severidade (`ops/severidade_sla.md`).
- [x] Implementar templates de resposta (`templates/respostas/*`).

## Médio prazo (31–90 dias) — iniciado
- [x] Automação de enriquecimento de IOC (WHOIS, DNS/IP) via script inicial (`scripts/enriquecimento_ioc.py`).
- [ ] Evoluir para reputação, ASN enriquecido e sandbox.
- [ ] Integrar com sistema de tickets.
- [x] Criar dashboard inicial de volume, MTTR e taxa de remoção (`scripts/gerar_dashboard.py` + `dashboard/index.html`).

## Próximos passos
1. Validar tempos de SLA por 2 semanas e recalibrar.
2. Integrar script de enriquecimento ao fluxo de triagem.
3. Criar dashboard de volume, MTTR e taxa de remoção.
