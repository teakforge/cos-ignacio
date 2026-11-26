# Levantar a Aguno en un ambiente nuevo
1. `git clone git@github.com:teakforge/cos-ignacio.git && cd cos-ignacio`
2. Abre Claude Code en esa carpeta (CLI, desktop o web). Se cargan solos `CLAUDE.md`, las skills (`.claude/skills`) y el hook de telemetría (`.claude/settings.json`).
3. Conecta los conectores: Microsoft 365, Read AI, Plaud.
4. Crea las tareas programadas según `routines/SCHEDULE.md`.
5. Requisitos: git, python3. Nada más.

## Otro runtime (que no sea Claude Code)
El cerebro es Markdown puro. Cualquier agente puede usarlo si: (a) carga `CLAUDE.md` como system prompt, (b) expone las skills como instrucciones, (c) ejecuta `routines/*.md` con un cron.

## Export
`bash harness/scripts/export.sh` genera un git bundle con fecha (todo el cerebro y su historial en un solo archivo).
