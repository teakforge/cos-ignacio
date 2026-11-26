#!/usr/bin/env python3
"""Stop hook: suma tokens del transcript de la sesión y anexa a harness/telemetry/usage.jsonl (una línea por sesión, se sobrescribe por session_id)."""
import json, sys, os, datetime, pathlib
hook = json.load(sys.stdin)
tp, sid = hook.get("transcript_path"), hook.get("session_id", "unknown")
root = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR", pathlib.Path(__file__).resolve().parents[2]))
tot = {"input": 0, "output": 0, "cache_write": 0, "cache_read": 0}; model = None
try:
    for line in open(tp):
        try: m = json.loads(line).get("message") or {}
        except Exception: continue
        u = m.get("usage")
        if not u: continue
        model = m.get("model", model)
        tot["input"] += u.get("input_tokens", 0); tot["output"] += u.get("output_tokens", 0)
        tot["cache_write"] += u.get("cache_creation_input_tokens", 0); tot["cache_read"] += u.get("cache_read_input_tokens", 0)
except Exception: sys.exit(0)
f = root / "harness/telemetry/usage.jsonl"
rows = [r for r in (json.loads(l) for l in f.read_text().splitlines() if l.strip())] if f.exists() else []
rows = [r for r in rows if r["session_id"] != sid]
rows.append({"session_id": sid, "ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "model": model, **tot})
f.write_text("".join(json.dumps(r) + "\n" for r in rows))
# Auto-commit solo del archivo de telemetría para no dejar el árbol sucio
import subprocess
try:
    subprocess.run(["git", "-C", str(root), "add", str(f)], check=True, capture_output=True)
    if subprocess.run(["git", "-C", str(root), "diff", "--cached", "--quiet"]).returncode:
        subprocess.run(["git", "-C", str(root), "-c", "user.name=Aguno", "-c", "user.email=noreply@teakforge",
                        "commit", "-q", "-m", "Telemetría: consumo de tokens", "--", str(f)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(root), "push", "-q"], capture_output=True, timeout=60)
except Exception:
    pass
