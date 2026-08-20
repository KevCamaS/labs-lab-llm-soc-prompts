#!/usr/bin/env python3
"""Arma el body JSON de una API LLM (OpenAI-compatible) por cada caso de prueba."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYSTEM = (ROOT / "prompts" / "system_soc_t1.txt").read_text(encoding="utf-8")
CASOS = json.loads((ROOT / "datos" / "casos_alerta.json").read_text(encoding="utf-8"))
OUT = ROOT / "resultados" / "llm_requests.json"


def main() -> None:
    requests = []
    for c in CASOS["casos"]:
        requests.append(
            {
                "case_id": c["id"],
                "expected": c["esperado"],
                "api_payload": {
                    "model": "gpt-4o-mini",
                    "temperature": 0,
                    "messages": [
                        {"role": "system", "content": SYSTEM},
                        {"role": "user", "content": c["alerta"]},
                    ],
                },
            }
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(requests, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Requests generados: {len(requests)} -> {OUT}")
    print("Criterio: el modelo no debe inventar IoCs que no estén en la alerta.")


if __name__ == "__main__":
    main()
