from stt_assemblyai import record_audio, upload_audio, transcribe_audio
from llm_groq import get_bot_reply
from tts_gtts import speak_text_simple
import os

print("🤖 Hindi Voice Bot Assistant Started...\n")


# Step 0: Initial Greeting
greeting = "ओला कस्टमर सर्विस में आपका स्वागत है। कृपया बताएं मैं आपकी क्या मदद कर सकता हूँ?"
print("🟢", greeting)
speak_text_simple(greeting)

while True:
    # Step 1: Record & Upload
    audio_path = record_audio()
    audio_url = upload_audio(audio_path)  # ✅ your custom upload
    hindi_input = transcribe_audio(audio_url)

    if not hindi_input:
        print("❌ Couldn't understand your voice. Try again...\n")
        continue

    print("📥 You said:", hindi_input)

    # Step 2: Check for exit command
    if "exit" in hindi_input.lower() or "बंद करो" in hindi_input:
        print("👋 Exiting Voice Bot. धन्यवाद!")
        speak_text_simple("बोट बंद किया जा रहा है। धन्यवाद।")
        break

    if any(kw in hindi_input.lower() for kw in ["exit", "बंद करो", "शुक्रिया", "thank you", "धन्यवाद"]):
        print("👋 Exiting Voice Bot. धन्यवाद!")
        speak_text_simple("बोट बंद किया जा रहा है। शुक्रिया।")
        break


    # Step 3: LLM response
    bot_response = get_bot_reply(hindi_input)
    print("🤖 Bot:", bot_response)

    # Step 4: Speak it
    speak_text_simple(bot_response)

    print("🔁 Listening for next input...\n")
