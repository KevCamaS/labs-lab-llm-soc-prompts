# Lab SOC & IA — Prompts LLM y casos de prueba del agente

Laboratorio básico de **IA aplicada a SOC**: diseñar prompts, pasar alertas de prueba y **validar** que el agente no alucine (casos PASS/FAIL).

No necesita API de pago. Puedes pegar el prompt en ChatGPT/Claude **sin datos reales de clientes**.

## Qué cubre del puesto
- Diseñar y probar prompts para análisis de alertas
- Casos de prueba del agente de IA
- Integración conceptual con APIs de LLMs (`scripts/formato_api.py` arma el JSON del request)

## Cómo ejecutar
```bash
python scripts/formato_api.py
```
Genera `resultados/llm_requests.json` listo para enviar a una API (OpenAI-compatible) cuando tengas clave.
