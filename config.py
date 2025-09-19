from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="data/config/.env")

TTS_ENGINE = os.getenv("TTS_ENGINE")  # Default to "google" if not set
ELEVELELABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE = os.getenv("ELEVENLABS_VOICE")