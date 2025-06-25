from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def analyze_emotion(text: str) -> dict:
    try:
        return emotion_classifier(text)[0]
    except Exception as e:
        print("❌ Emotion analysis error:", e)
        return {"label": "neutral", "score": 0.0}
