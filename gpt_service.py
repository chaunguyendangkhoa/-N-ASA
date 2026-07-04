from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.7,
            max_tokens=2048
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ {e}"