import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="bn-BD")  # বাংলা ভাষায়
        print(f"Recognized: {text}")
        return text
    except sr.UnknownValueError:
        return "শোনার সমস্যা হয়েছে, আবার বলুন।"
    except sr.RequestError:
        return "সার্ভার সমস্যা হয়েছে।"
