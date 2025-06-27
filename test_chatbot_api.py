import requests

API_URL = "http://192.168.203.154:5000/chat"

# 🔄 Realistic multi-language and multi-emotion test cases
test_messages = [
    # Sadness - English
    "I don’t know what to do anymore... everything feels like it’s falling apart around me.",

    # Joy - English
    "You won’t believe it! I finally got accepted into my dream university today!",

    # Anger - English
    "I’ve explained it three times already and it’s still not working! This is so frustrating!",

    # Confusion - English
    "I’ve read the instructions twice but still don’t understand how to get started. Can you help?",

    # Fear - English
    "My hands are shaking… I have an interview tomorrow and I’m really nervous about it.",

    # Hinglish (Hindi + English)
    "Mujhe samajh nahi aa raha ye assignment kaise karna hai, thoda bata do please.",

    # Bangla
    "আজ সারাদিন মনটা খুব খারাপ ছিল। কিছুতেই ভালো লাগছে না।",  # Feeling sad all day

    # Bhojpuri
    "Are ka ho! Ee kaam kaise kari? Kuno bataye ke taiyaar hi nai baa.",  # Frustrated asking how to do something

    # Tamil
    "நான் இன்று மிகவும் மகிழ்ச்சியாக இருக்கிறேன். என் நண்பர் வீட்டுக்கு வருகிறார்!",  # Happy because friend is coming

    # Telugu
    "ఈ పని ఎలా చేయాలో అర్థం కావడం లేదు. దయచేసి సహాయం చేయండి.",  # I don't understand how to do this

    # Marathi
    "माझं मन अगदी खूप उदास झालंय आज. काहीतरी चुकतंय असं वाटतंय.",  # Feeling emotionally down

    # Indonesian
    "Hari ini aku senang banget! Akhirnya aku bisa jalan-jalan ke Bali minggu depan!",  # Excited about trip

    # Gujarati
    "મને સમજાતું નથી કે હવે શું કરવું. કંઈક માર્ગદર્શન આપો તો સારું લાગે.",  # Confused asking for help

    # Urdu (in Roman)
    "Mujhe buhat ghabrahat ho rahi hai, kal mera exam hai aur kuch yaad nahi ho raha.",  # Nervous about exam
]

def test_message(msg):
    payload = {"message": msg}
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"\n🔹 User Message:\n{msg}")
        print(f"📤 Detected Emotion: {data.get('emotion')}")
        print(f"🌐 Detected Language: {data.get('language')}")
        print(f"💬 Bot Response:\n{data.get('response')}")
        print(f"🎧 Audio URL: {data.get('audio')}")
        print(f"📈 Confidence Score: {data.get('confidence')}")
        print("-" * 60)
    except Exception as e:
        print(f"\n❌ Failed to process message:\n{msg}")
        print("Error:", e)

if __name__ == "__main__":
    print("🚀 Running multilingual emotional test cases for Chatbot API...")
    for message in test_messages:
        test_message(message)
