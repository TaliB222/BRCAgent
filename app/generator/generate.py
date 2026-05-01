from openai import OpenAI
from .prompt import GENERATOR_PROMPT

client = OpenAI()

def generate_response(user_text, context):
    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.7,
        messages=[
            {"role": "system", "content": GENERATOR_PROMPT},
            {"role": "user", "content": f"""
User post:
{user_text}

Relevant knowledge:
{context}
"""}
        ]
    )

    return response.choices[0].message.content