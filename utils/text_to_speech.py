# utils/text_to_speech.py
from gtts import gTTS
import os
import uuid

AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text: str, lang: str = "en") -> str:
    try:
        if not text.strip():
            return ""

        # Generate unique filename for audio output
        filename = f"response_{uuid.uuid4()}.mp3"
        path = os.path.join(AUDIO_DIR, filename)

        # Convert text to speech and save as mp3
        tts = gTTS(text=text, lang=lang)
        tts.save(path)

        return f"static/audio/{filename}"

    except Exception as e:
        print("❌ TTS error:", e)
        return ""