# config/config.py
import os
from pathlib import Path

from dotenv import load_dotenv

BACKEND_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(BACKEND_ROOT / ".env")

def get_api_key():
    return os.getenv("OPENROUTER_API_KEY")
