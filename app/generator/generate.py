from openai import OpenAI
from .prompt import GENERATOR_PROMPT

client = OpenAI()


def generate_response(user_text, context, classification=None):
    # בונים input עשיר יותר למודל
    enriched_input = f"""
User post:
{user_text}

Classification:
{classification}

Relevant knowledge (RAG context):
{context}

Instructions:
- Use ONLY the provided knowledge
- Do not give medical advice
- Be accurate and careful
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.4,  # פחות יצירתי = יותר מדויק רפואית
        messages=[
            {"role": "system", "content": GENERATOR_PROMPT},
            {"role": "user", "content": enriched_input}
        ]
    )

    return response.choices[0].message.content