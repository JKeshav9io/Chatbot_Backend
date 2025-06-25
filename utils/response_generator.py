from openai import OpenAI
from config.config import get_api_key

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=get_api_key()
)

def generate_reply(prompt: str, emotion: str = "neutral") -> str:
    # 🧠 Choose a tone/style based on emotion (optional use)
    style = {
        "sadness": "Be gentle and empathetic.",
        "joy": "Be cheerful and friendly.",
        "anger": "Respond calmly to defuse anger.",
        "confusion": "Be clear and guide step-by-step."
    }.get(emotion.lower(), "You are a helpful assistant.")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",  # fast + good
            messages=[
                {"role": "system", "content": style},
                {"role": "user", "content": prompt}
            ],
            extra_headers={
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "Chatbot API"
            }
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ LLM error:", e)
        return "Sorry, I encountered an error while generating a response."
