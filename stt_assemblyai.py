# stt_assemblyai.py
import os
import requests
import sounddevice as sd
import soundfile as sf
import requests
import time
import wave
from config import (
    ASSEMBLYAI_API_KEY,
    ASSEMBLYAI_UPLOAD_URL,
    ASSEMBLYAI_TRANSCRIBE_URL,
    RECORD_SECONDS,
    SAMPLE_RATE,
)

def debug_wav_file(filename):
    print(f"🔍 Debugging audio file: {filename}")
    with wave.open(filename, 'rb') as wf:
        print(f"📁 File size: {os.path.getsize(filename)} bytes")
        print("📊 WAV header info:")
        print(f"   Channels: {wf.getnchannels()}")
        print(f"   Sample width: {wf.getsampwidth()} bytes")
        print(f"   Frame rate: {wf.getframerate()} Hz")
        print(f"   Frames: {wf.getnframes()}")
        print(f"   Duration: {wf.getnframes() / wf.getframerate():.2f} seconds")

def record_audio(filename="input.wav", duration=RECORD_SECONDS, fs=SAMPLE_RATE):
    print(f"🎙️ Recording {duration} seconds of audio...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, recording, fs, format='WAV', subtype='PCM_16')
    print(f"✅ Recording saved to {filename} (Size: {os.path.getsize(filename)} bytes)")
    debug_wav_file(filename)
    return filename

def upload_audio(file_path):
    print(f"📤 Uploading {file_path} to AssemblyAI...")
    headers = {
        "authorization": ASSEMBLYAI_API_KEY,
        "content-type": "application/octet-stream"
    }
    with open(file_path, "rb") as f:
        response = requests.post(ASSEMBLYAI_UPLOAD_URL, headers=headers, data=f)
    response.raise_for_status()
    audio_url = response.json()["upload_url"]
    print("✅ Upload successful:", audio_url)
    return audio_url

def transcribe_audio(audio_url, language_code="hi"):
    print(f"🔤 Starting transcription for language: {language_code}")
    headers = {
        "authorization": ASSEMBLYAI_API_KEY,
        "content-type": "application/json"
    }
    data = {
        "audio_url": audio_url,
        "language_code": language_code,
        "punctuate": True
    }

    response = requests.post(ASSEMBLYAI_TRANSCRIBE_URL, json=data, headers=headers)
    response.raise_for_status()
    transcript_id = response.json()["id"]
    print("📋 Transcript ID:", transcript_id)

    polling_url = f"{ASSEMBLYAI_TRANSCRIBE_URL}/{transcript_id}"
    while True:
        poll_res = requests.get(polling_url, headers=headers).json()
        if poll_res["status"] == "completed":
            print("✅ Transcription complete.")
            return poll_res["text"]
        elif poll_res["status"] == "error":
            error_msg = poll_res.get("error", "Unknown error")
            print("❌ Transcription error:", error_msg)
            raise Exception(f"❌ Transcription failed: {error_msg}")
        time.sleep(2)

# 🧪 Test end-to-end
if __name__ == "__main__":
    import os

    try:
        filename = record_audio()
        audio_url = upload_audio(filename)
        hindi_text = transcribe_audio(audio_url)
        print("📝 Transcribed Text:", hindi_text)
    except Exception as e:
        print("❌ Process failed:", str(e))
        print("🔧 Troubleshooting tips:")
        print("1. Check if your microphone is working")
        print("2. Verify ASSEMBLYAI_API_KEY in .env")
        print("3. Make sure you're speaking during recording")
        print("4. Try: python -c 'import sounddevice as sd; print(sd.query_devices())'")
