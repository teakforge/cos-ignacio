# Despachador del heartbeat
Se ejecuta en cada despertar programado.
1. `git pull --rebase` en el repo.
2. Toma la hora actual en America/Merida. Lee `routines/SCHEDULE.md`.
3. Una rutina **toca** si está activa, el día coincide y su hora cae en la ventana [ahora − 10 min, ahora + 55 min).
4. Revisa `harness/telemetry/runs.md` y no repitas una rutina ya ejecutada hoy.
5. Si no toca nada: termina en silencio con una sola línea, "Sin rutinas.", sin commit.
6. Por cada rutina que toque: ejecútala al pie de la letra, anótala en `runs.md` (fecha, rutina, ok/falla) y en `activity.md`, y haz commit y push.
7. Si una rutina falla, anota la causa y avisa en el resumen final.
8. Revisa también `core/reminders.md`: incluye en el push los recordatorios que vencen hoy o según su anticipación.
