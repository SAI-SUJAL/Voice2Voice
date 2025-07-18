# # config.py

# from dotenv import load_dotenv
import os

from dotenv.main import load_dotenv

# # Load environment variables from .env file
load_dotenv()

# # API Keys
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# ElevenLabs voice
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")  # Replace in .env
# 🔐 API Keys (replace with your actual keys)

# 🗣️ ElevenLabs voice settings

# API URLs
ASSEMBLYAI_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIBE_URL = "https://api.assemblyai.com/v2/transcript"
ELEVENLABS_TTS_URL_TEMPLATE = "https://api.elevenlabs.io/v1/text-to-speech/{}"

# Audio settings
RECORD_SECONDS = 5
SAMPLE_RATE = 16000
