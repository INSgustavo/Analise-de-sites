# Matriz de Severidade e SLA

## Critérios de severidade
- **Crítica**: coleta de credenciais/pagamentos ativa com uso de marca; alto risco imediato.
- **Alta**: forte impersonação de marca com potencial de fraude, mas sem comprovação de captura ativa.
- **Média**: menção indevida/confusão de marca com risco limitado.
- **Baixa**: falso positivo provável ou conteúdo sem risco direto.

## SLA de triagem e resposta
| Severidade | Triagem inicial | Primeira notificação externa | Atualização interna |
|---|---:|---:|---:|
| Crítica | até 1h | até 2h | a cada 4h |
| Alta | até 4h | até 8h | a cada 8h |
| Média | até 1 dia útil | até 2 dias úteis | diário |
| Baixa | até 2 dias úteis | sob demanda | semanal |

## Fila única
- Todos os incidentes entram no mesmo backlog.
- Ordenação por severidade e data/hora de abertura.
- Reclassificação permitida com justificativa registrada.
