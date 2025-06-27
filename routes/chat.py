# routes/chat.py
from flask import Blueprint, request, jsonify
from utils.pipeline import process_user_message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_msg = data.get("message", "").strip()

    if not user_msg:
        return jsonify({"error": "Message is required."}), 400

    try:
        # Process user input and return structured chatbot response
        result = process_user_message(user_msg)
        return jsonify(result)

    except Exception as e:
        print("❌ Error in /chat:", e)
        return jsonify({"error": str(e)}), 500

