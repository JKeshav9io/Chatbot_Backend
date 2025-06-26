# 🤖 Chatbot Backend API

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ChatGPT API](https://img.shields.io/badge/OpenAI-GPT--4o--mini-ff69b4?logo=openai)](https://openai.com/)
[![Status](https://img.shields.io/badge/API-Running-green)](http://localhost:5000)

A language-aware, emotion-sensitive AI chatbot backend that:
- 🧠 Understands multilingual and Hinglish inputs
- 😄 Detects emotional tone (joy, sadness, anger, etc.)
- 🗣️ Replies using GPT-4o-mini via OpenRouter
- 🔊 Converts bot replies to **speech** using Google TTS
- 🔐 Built with modular design, error handling, and Flask

---

## 🚀 Features

- 🗨️ Conversational history-based prompting
- 🌍 Multilingual detection (`en`, `hi`, Hinglish)
- ❤️ Emotion analysis using `distilbert-base-uncased-emotion`
- 🤖 LLM-based smart responses via OpenRouter API
- 🔊 Audio response using `gTTS`
- 📁 Clean REST API structure with Blueprints
- ⚙️ CORS support for cross-platform apps
- 📂 Audio files stored and served from `/static/audio/`

---

## 🛠️ Tech Stack

| Layer        | Tools / Libraries                              |
|--------------|-------------------------------------------------|
| Backend      | Python, Flask, Flask-CORS                       |
| LLM API      | OpenRouter (`openai/gpt-4o-mini`)               |
| Emotion AI   | HuggingFace Transformers + DistilBERT model     |
| Language     | `langdetect`, `deep-translator`, Regex          |
| Speech       | `gTTS`                                          |
| Environment  | `python-dotenv`, `.env` API key loading         |

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/JKeshav9io/Chatbot_Backend.git
cd Chatbot_Backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

Create a .env file in the root directory:
OPENROUTER_API_KEY=your_openrouter_api_key

Chatbot_Backend/
├── app.py                         # Flask entry point
├── config/
│   └── config.py                  # Loads API keys
├── routes/
│   └── chat.py                    # Main `/chat` endpoint
├── utils/
│   ├── emotion.py                 # Emotion detection logic
│   ├── language.py                # LangDetect, translation, Hinglish check
│   ├── response_generator.py      # GPT-4o response
│   └── text_to_speech.py          # gTTS-based speech output
├── static/
│   └── audio/                     # MP3 responses
├── .env                           # API key (excluded via .gitignore)
├── requirements.txt               # All Python deps
└── README.md                      # This file
