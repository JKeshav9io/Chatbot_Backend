# utils/response_generator.py
from openai import OpenAI
from config.config import get_api_key

_client = None


def get_client():
    global _client

    if _client is not None:
        return _client

    api_key = get_api_key()
    if not api_key:
        return None

    _client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    return _client

def generate_reply(prompt: str, emotion: str = "neutral") -> str:
    # Define prompt styles based on emotion label
    style = {
        "sadness": "Be gentle and empathetic.",
        "joy": "Be cheerful and friendly.",
        "anger": "Respond calmly to defuse anger.",
        "confusion": "Be clear and guide step-by-step.",
        "fear": "Offer comfort and reassurance.",
        "neutral": "You are a helpful assistant."
    }.get(emotion.lower(), "You are a helpful assistant.")

    client = get_client()
    if client is None:
        return "The backend is running, but OPENROUTER_API_KEY is not set in the backend .env file yet."

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
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
