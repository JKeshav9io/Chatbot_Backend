# utils/language.py
from langdetect import detect, DetectorFactory, LangDetectException
import re
from deep_translator import GoogleTranslator

DetectorFactory.seed = 0

ALLOWED_LANGUAGES = {"en", "hi"}

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        # If Hinglish detected as English, override
        if lang not in ALLOWED_LANGUAGES:
            if lang == "en" and is_hinglish(text):
                return "hi"
            return "en"
        return lang
    except LangDetectException:
        return "en"

def is_hinglish(text: str) -> bool:
    # Match common Hindi words written in Latin script
    return bool(re.search(r"\b(mai|kya|nahi|tum|kaise|batao|kar|raha|hu|hoon|abhi|haan)\b", text.lower()))

def translate_text(text: str, target_lang: str) -> str:
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception as e:
        print("❌ Translation error:", e)
        return text
