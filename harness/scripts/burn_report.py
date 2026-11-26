#!/usr/bin/env python3
"""Resumen de consumo de tokens y costo estimado. Uso: burn_report.py [días=7]"""
import json, sys, datetime, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
price = json.loads((root / "harness/telemetry/pricing.json").read_text())
since = datetime.datetime.now().astimezone() - datetime.timedelta(days=days)
f = root / "harness/telemetry/usage.jsonl"
rows = [json.loads(l) for l in f.read_text().splitlines() if l.strip()] if f.exists() else []
rows = [r for r in rows if datetime.datetime.fromisoformat(r["ts"]) >= since]
T = {"input": 0, "output": 0, "cache_write": 0, "cache_read": 0}; usd = 0.0
for r in rows:
    p = price["models"].get(r.get("model") or "", price["models"]["default"])
    for k in T: T[k] += r[k]; usd += r[k] / 1e6 * p[k]
fx = price.get("usd_mxn", 0)
print(f"Últimos {days} días · {len(rows)} sesiones")
print(f"Tokens: input {T['input']:,} · output {T['output']:,} · cache write {T['cache_write']:,} · cache read {T['cache_read']:,}")
print(f"Costo estimado (equivalente API): USD {usd:,.2f}" + (f" ≈ MXN {usd*fx:,.0f}" if fx else ""))
print(f"Burn rate: USD {usd/days:,.2f}/día · proyección mensual USD {usd/days*30:,.0f}")
print("Nota: si usas un plan de suscripción de Claude, esto es costo equivalente y no un cargo real.")
