# from gtts import gTTS
# import os
# import tempfile
# from pydub import AudioSegment
# # from pydub.playback import play  
# import time
# import stat
# import pygame
# import threading

# # Set correct paths for FFmpeg
# AudioSegment.converter = r"C:\ffmpeg\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.ffmpeg    = r"C:\ffmpeg\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.ffprobe   = r"C:\ffmpeg\ffmpeg\bin\ffprobe.exe"

# assert os.path.exists(AudioSegment.converter), "❌ ffmpeg.exe NOT found!"
# assert os.path.exists(AudioSegment.ffprobe), "❌ ffprobe.exe NOT found!"

# def play_audio_pygame(audio_segment):
#     """Play audio using pygame (no temp files)"""
#     try:
#         pygame.mixer.init()
        
#         # Export to wav in memory
#         from io import BytesIO
#         wav_io = BytesIO()
#         audio_segment.export(wav_io, format="wav")
#         wav_io.seek(0)
        
#         # Load and play
#         pygame.mixer.music.load(wav_io)
#         pygame.mixer.music.play()
        
#         # Wait for playback to finish
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
            
#         pygame.mixer.quit()
        
#     except Exception as e:
#         print(f"❌ Pygame playback failed: {e}")
#         # Fallback to system playback
#         try:
#             audio_segment.export("temp_playback.wav", format="wav")
#             os.system("start temp_playback.wav")  # Windows
#             time.sleep(3)  # Wait for playback
#             os.remove("temp_playback.wav")
#         except Exception as fallback_error:
#             print(f"❌ Fallback playback failed: {fallback_error}")

# def speak_text(text, lang="hi"):
#     print("🗣️ Generating Hindi speech using Google TTS...")

#     try:
#         # Method 1: Use current directory instead of temp directory
#         mp3_path = "temp_audio.mp3"
        
#         # Step 1: Save TTS as MP3
#         tts = gTTS(text=text, lang=lang)
#         tts.save(mp3_path)
        
#         # Step 2: Convert MP3 to WAV and play
#         audio = AudioSegment.from_mp3(mp3_path)
#         play_audio_pygame(audio)

#         # Step 3: Delay to ensure playback finishes before file is deleted
#         time.sleep(1)
        
#         # Remove file with error handling
#         try:
#             # Change file permissions before deleting (Windows fix)
#             os.chmod(mp3_path, stat.S_IWRITE)
#             os.remove(mp3_path)
#             print("✅ Playback complete and file deleted.")
#         except Exception as cleanup_error:
#             print(f"⚠️ Warning: Could not delete temporary file: {cleanup_error}")
#             print("You may need to manually delete temp_audio.mp3")

#     except Exception as e:
#         print("❌ TTS failed:", e)

# def speak_text_alternative(text, lang="hi"):
#     """Alternative method using a custom temp directory"""
#     print("🗣️ Generating Hindi speech using Google TTS (Alternative method)...")
    
#     # Create temp directory in current folder
#     temp_dir = "temp_audio"
#     os.makedirs(temp_dir, exist_ok=True)
    
#     try:
#         mp3_path = os.path.join(temp_dir, "speech.mp3")
        
#         # Step 1: Save TTS as MP3
#         tts = gTTS(text=text, lang=lang)
#         tts.save(mp3_path)
        
#         # Step 2: Convert MP3 to WAV and play
#         audio = AudioSegment.from_mp3(mp3_path)
#         play_audio_pygame(audio)

#         # Step 3: Cleanup
#         time.sleep(1)
#         try:
#             os.chmod(mp3_path, stat.S_IWRITE)
#             os.remove(mp3_path)
#             os.rmdir(temp_dir)
#             print("✅ Playback complete and files cleaned up.")
#         except Exception as cleanup_error:
#             print(f"⚠️ Warning: Could not clean up temporary files: {cleanup_error}")

#     except Exception as e:
#         print("❌ TTS failed:", e)

# def speak_text_no_temp(text, lang="hi"):
#     """Method that plays directly from BytesIO without saving to disk"""
#     print("🗣️ Generating Hindi speech using Google TTS (No temp files)...")
    
#     try:
#         from io import BytesIO
        
#         # Step 1: Create TTS and save to BytesIO
#         tts = gTTS(text=text, lang=lang)
#         mp3_fp = BytesIO()
#         tts.write_to_fp(mp3_fp)
#         mp3_fp.seek(0)
        
#         # Step 2: Load and play audio from memory
#         audio = AudioSegment.from_mp3(mp3_fp)
#         play_audio_pygame(audio)
        
#         print("✅ Playback complete (no temp files used).")
        
#     except Exception as e:
#         print("❌ TTS failed:", e)

# def speak_text_simple(text, lang="hi"):
#     """Simplest method - just save and play with OS"""
#     print("🗣️ Generating Hindi speech using Google TTS (Simple method)...")
    
#     try:
#         # Step 1: Save TTS as MP3
#         tts = gTTS(text=text, lang=lang)
#         tts.save("speech.mp3")
        
#         # Step 2: Play using OS (Windows)
#         os.system("start speech.mp3")
        
#         # Step 3: Wait and cleanup
#         time.sleep(4)  # Adjust based on speech length
#         try:
#             os.remove("speech.mp3")
#             print("✅ Playback complete.")
#         except:
#             print("⚠️ Please manually delete speech.mp3")
        
#     except Exception as e:
#         print("❌ TTS failed:", e)

# # 🧪 Test all methods
# if __name__ == "__main__":
#     hindi_line = "कृपया अपनी लोकेशन बदल कर दोबारा प्रयास करें।"
    
#     print("=== Testing Method 1: Current Directory ===")
#     speak_text(hindi_line)
    
#     # print("\n=== Testing Method 2: Custom Temp Directory ===")
#     # speak_text_alternative(hindi_line)
    
#     # print("\n=== Testing Method 3: No Temp Files (Recommended) ===")
#     # speak_text_no_temp(hindi_line)
    
#     # print("\n=== Testing Method 4: Simple OS Playback ===")
#     # speak_text_simple(hindi_line)
from gtts import gTTS
from playsound import playsound
import os
import time

def speak_text_simple(text, lang="hi"):
    print("🗣️ Generating Hindi speech using Google TTS...")
    
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save("speech.mp3")

        playsound("speech.mp3")  
        os.remove("speech.mp3")

        print("✅ Playback complete.")
    except Exception as e:
        print("❌ TTS failed:", e)
