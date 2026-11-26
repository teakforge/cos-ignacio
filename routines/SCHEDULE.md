# Calendario del heartbeat (cron, CRON_TZ=America/Merida)
| Rutina | Cron | Archivo |
|---|---|---|
| Morning brief | 30 6 * * 1-6 | routines/morning-brief.md |
| Evening close | 30 19 * * 1-5 | routines/evening-close.md |
| Weekly review | 0 18 * * 0 | routines/weekly-review.md |
| Monthly review | 0 7 1 * * | routines/monthly-review.md |
| Quarterly review | 0 7 1 1,4,7,10 * | routines/quarterly-review.md |
Prompt de cada tarea: "Eres Aguno. Ejecuta routines/<archivo> al pie de la letra según CLAUDE.md."
