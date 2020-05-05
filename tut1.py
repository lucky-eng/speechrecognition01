import speech_recognition as s
#instance of recognizer class
sr = s.Recognizer()
print("I am your script and listening to you ")
with s.Microphone() as source:
    audio=sr.listen(source)
    query=sr.recognize_google(audio)
    print(query)
