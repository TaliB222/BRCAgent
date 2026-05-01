from openai import OpenAI
import json
from .prompt import CLASSIFIER_PROMPT

client = OpenAI()

def classify_text(text):
    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0,
        messages=[
            {"role": "system", "content": CLASSIFIER_PROMPT},
            {"role": "user", "content": text}
        ]
    )

    return json.loads(response.choices[0].message.content)