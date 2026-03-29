from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_content(content: str, language: str = "Hindi") -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a translator."},
            {"role": "user", "content": f"Translate this to {language}: {content}"}
        ]
    )
    return response.choices[0].message.content
