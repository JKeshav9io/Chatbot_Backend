from flask import Flask
from flask_cors import CORS
from routes.chat import chat_bp
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 📁 Ensure audio directory exists
AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# 🔗 Register Blueprints
app.register_blueprint(chat_bp)

@app.route('/')
def index():
    return "🟢 Chatbot API is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port)
