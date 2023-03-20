import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print(r.recognize_google(audio))

except sr.UnknownValueError:
    print("Unable To Understand You! Please Speak Clearly")

except sr.RequestError as e:
    print("Network Error")