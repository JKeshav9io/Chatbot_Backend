from gtts import gTTS
import os
import uuid

AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text: str, lang: str = "en") -> str:
    try:
        if not text.strip():
            print("⚠️ Empty text received for TTS.")
            return ""

        # Generate unique filename
        filename = f"response_{uuid.uuid4()}.mp3"
        path = os.path.join(AUDIO_DIR, filename)

        # Generate TTS
        tts = gTTS(text=text, lang=lang)
        tts.save(path)

        print(f"✅ Audio saved at: {path}")
        return f"/static/audio/{filename}"

    except Exception as e:
        print("❌ TTS error:", e)
        return ""
