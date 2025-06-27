from utils.language import detect_language, is_hinglish, translate_text
from utils.emotion import analyze_emotion
from utils.response_generator import generate_reply
from utils.text_to_speech import generate_audio

def process_user_message(message: str) -> dict:
    lang = detect_language(message)
    print(f"Detected language: {lang}")

    # Translate non-English/Hinglish input to English for LLM understanding
    if lang == "en" and is_hinglish(message):
        lang = "hi"
        translated_input = translate_text(message, "en")
    elif lang != "en":
        translated_input = translate_text(message, "en")
    else:
        translated_input = message

    # Run emotion analysis on translated English text
    emotion_data = analyze_emotion(translated_input)
    emotion = emotion_data.get("label", "neutral")
    confidence = round(emotion_data.get("score", 0.0), 2)
    print(f"Emotion detected: {emotion} ({confidence})")

    # Generate emotionally aligned LLM response in English
    english_reply = generate_reply(translated_input, emotion)

    # Translate back to user language if needed
    final_reply = translate_text(english_reply, lang) if lang != "en" else english_reply

    # Generate audio from final response
    audio_path = generate_audio(final_reply, lang=lang)
    audio_url = f"/{audio_path}" if audio_path else None

    return {
        "emotion": emotion,
        "language": lang,
        "response": final_reply,
        "confidence": confidence,
        "audio": audio_url
    }

