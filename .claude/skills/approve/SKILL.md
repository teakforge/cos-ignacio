---
name: approve
description: Procesa aprobaciones del inbox ("aprobar ID", "rechazar ID", "qué tengo por aprobar").
---
1. Lee `core/inbox/pending.md`.
2. Si la acción se aprueba y es externa: ejecútala con la herramienta disponible. Si solo hay lectura disponible (fase 1), entrega el texto final listo para copiar y anótalo como "entregado manual".
3. Mueve la acción a `core/inbox/done.md` con fecha y resultado. Si se rechaza, anota el motivo.
