"""Classifica e-mails usando GPT-4o e roteia para o workflow correto."""
import openai
import json
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CATEGORIES = ["suporte", "vendas", "financeiro", "rh", "spam", "outro"]

def classify_email(subject: str, body: str, sender: str) -> dict:
    prompt = f"""Classifique o e-mail abaixo em uma das categorias: {', '.join(CATEGORIES)}
    
Assunto: {subject}
De: {sender}
Corpo: {body[:500]}

Responda APENAS com JSON: {{"categoria": "...", "prioridade": "alta|media|baixa", "resumo": "..."}}"""

    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return json.loads(resp.choices[0].message.content)
