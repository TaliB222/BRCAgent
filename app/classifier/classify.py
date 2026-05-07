from openai import OpenAI
import json
from .prompt import CLASSIFIER_PROMPT

client = OpenAI()


def classify_text(text: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            temperature=0,
            messages=[
                {"role": "system", "content": CLASSIFIER_PROMPT},
                {"role": "user", "content": text}
            ]
        )

        content = response.choices[0].message.content

        # ניסיון לפענח JSON
        return json.loads(content)

    except json.JSONDecodeError:
        # אם המודל החזיר JSON לא תקין
        return {
            "error": "Invalid JSON from model",
            "raw_output": content
        }

    except Exception as e:
        # טיפול כללי בשגיאות API
        return {
            "error": str(e),
            "raw_output": None
        }