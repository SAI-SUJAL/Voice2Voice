# tts_elevenlabs.py

import requests
from config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, ELEVENLABS_TTS_URL_TEMPLATE
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

def speak_text(text, voice_id=ELEVENLABS_VOICE_ID):
    print("🔁 Converting text to speech (Hindi)...")

    url = ELEVENLABS_TTS_URL_TEMPLATE.format(voice_id)
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print("❌ TTS failed:", response.text)
        return

    print("✅ TTS audio received from ElevenLabs")

    # Save audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    # Load and play using pydub
    try:
        audio = AudioSegment.from_file(tmp_file_path, format="mp3")
        play(audio)
    finally:
        os.remove(tmp_file_path)

# 🧪 Test
if __name__ == "__main__":
    hindi_text = "आपका नंबर ब्लॉक नहीं है। कृपया अपनी लोकेशन बदल कर दोबारा प्रयास करें।"
    speak_text(hindi_text)
