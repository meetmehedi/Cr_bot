import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
    try:
        text = recognizer.recognize_google(audio, language="bn-BD")
        return text
    except Exception as e:
        return "দুঃখিত, বুঝতে পারিনি। আবার চেষ্টা করুন।"
