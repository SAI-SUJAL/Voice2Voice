# # config.py

# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # API Keys
# ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# ElevenLabs voice
# ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")  # Replace in .env
# 🔐 API Keys (replace with your actual keys)
ASSEMBLYAI_API_KEY = "8e2291fd68464c53a5c9c85b7142580c"
GROQ_API_KEY = "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"
ELEVENLABS_API_KEY = "sk_d6fd73d20b1c1c8c91452f2e06b9f7b85314fc615d16a16a"

# 🗣️ ElevenLabs voice settings
ELEVENLABS_VOICE_ID = "77zQwP0TsblwbFgapIkF"
# API URLs
ASSEMBLYAI_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIBE_URL = "https://api.assemblyai.com/v2/transcript"
ELEVENLABS_TTS_URL_TEMPLATE = "https://api.elevenlabs.io/v1/text-to-speech/{}"

# Audio settings
RECORD_SECONDS = 5
SAMPLE_RATE = 16000
