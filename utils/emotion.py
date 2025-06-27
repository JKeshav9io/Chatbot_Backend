# utils/emotion.py
from transformers import pipeline

# Load Hugging Face transformer model for emotion classification
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def analyze_emotion(text: str) -> dict:
    try:
        results = emotion_classifier(text, top_k=None)
        if not results:
            return {"label": "neutral", "score": 0.0}
        top_emotion = max(results, key=lambda x: x['score'])
        return top_emotion
    except Exception as e:
        print("❌ Emotion analysis error:", e)
        return {"label": "neutral", "score": 0.0}