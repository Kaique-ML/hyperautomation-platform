"""Aprova ou rejeita pedidos com regras de negócio + IA."""
import openai
import json
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_order(order: dict) -> dict:
    # Regras simples primeiro
    if order["value"] < 100:
        return {"status": "approved", "reason": "Valor abaixo do limite de aprovação automática", "requires_human": False}
    if order["value"] > 50000:
        return {"status": "pending", "reason": "Valor alto — requer aprovação diretora", "requires_human": True}

    # IA para casos intermediários
    prompt = f"""Avalie este pedido e decida se deve ser aprovado:

Pedido: {json.dumps(order, ensure_ascii=False)}

Critérios: clientes novos com valor > 5000 precisam de análise extra. Histórico de pagamento positivo favorece aprovação.

Responda com JSON: {{"status": "approved|rejected|pending", "reason": "...", "requires_human": true|false}}"""

    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )
    return json.loads(resp.choices[0].message.content)
