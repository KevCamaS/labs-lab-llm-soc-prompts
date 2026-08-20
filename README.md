# Lab — Prompts LLM para SOC y prueba del agente

El puesto habla de diseñar prompts y validar un agente de IA con alertas. Antes de “confiar” en un modelo, quise fijar reglas claras:

1. El modelo **no inventa** IPs ni usuarios.
2. Siempre pide MITRE, IoCs, falso positivo y si escala.
3. Tengo casos PASS/FAIL para revisar la respuesta.

## Cómo lo uso
1. Tomo el system prompt en `prompts/system_soc_t1.txt`.
2. Paso una alerta de `datos/casos_alerta.json`.
3. Comparo con lo esperado (ej. brute force SSH → T1110 + escalar).

```bash
python scripts/formato_api.py
```
Arma `resultados/llm_requests.json` (formato tipo API OpenAI). Puedo pegar el mismo prompt en un chat sin datos de clientes reales.

## Por qué no es “magia”
La IA ayuda a resumir; el analista T1 decide. Si el modelo alucina, el caso falla. Eso es lo que quería practicar para Kriptome / Aynitech.

Kevin Cama — github.com/KevCamaS
