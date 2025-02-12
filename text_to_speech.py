from gtts import gTTS
import os

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    filename = f"speech_{language}.mp3"
    tts.save(filename)
    return filename