from flask import Blueprint, request, jsonify
from utils.response_generator import generate_reply      # LLM logic
from utils.text_to_speech import generate_audio          # TTS logic
from langdetect import detect                            # Language detection

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_msg = data.get("message", "").strip()
    history = data.get("history", [])  # Optional: [{"user": "Hi"}, {"bot": "Hello"}]

    if not user_msg:
        return jsonify({"error": "Message is required."}), 400

    try:
        # 🧠 Build prompt from history
        prompt = ""
        for h in history:
            if h.get("user"):
                prompt += f"User: {h['user']}\n"
            if h.get("bot"):
                prompt += f"Bot: {h['bot']}\n"
        prompt += f"User: {user_msg}\nBot:"

        # 🤖 Get reply from LLM
        response_text = generate_reply(prompt)

        # 🌍 Detect language of response
        try:
            lang_code = detect(response_text)
        except Exception:
            lang_code = "en"

        # 🔊 Generate audio
        audio_url = generate_audio(response_text, lang=lang_code).replace("\\", "/")

        # ✅ Return structured result
        return jsonify({
            "response": response_text,
            "emotion": "neutral",       # Optional placeholder
            "confidence": 0.95,         # Optional placeholder
            "audio": audio_url
        })

    except Exception as e:
        print("❌ Error in /chat:", e)
        return jsonify({"error": str(e)}), 500
