from langdetect import detect, DetectorFactory, LangDetectException
import re
from deep_translator import GoogleTranslator

DetectorFactory.seed = 0  # deterministic output

ALLOWED_LANGUAGES = {"en", "hi"}

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        if lang not in ALLOWED_LANGUAGES:
            # Check for Hinglish manually
            if lang == "en" and is_hinglish(text):
                return "hi"
            return "en"  # fallback to English
        return lang
    except LangDetectException:
        return "en"
    
    
def is_hinglish(text: str) -> bool:
    return bool(re.search(r"\b(mai|kya|nahi|tum|kaise|batao|kar|raha|hu|hoon|abhi|haan)\b", text.lower()))

def translate_text(text: str, target_lang: str) -> str:
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception as e:
        print("❌ Translation error:", e)
        return text