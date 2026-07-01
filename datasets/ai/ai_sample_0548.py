import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio))
    if r.recognize_google(audio) == 'Good morning':
        print('correct')
    else:
        print('incorrect')
except:
    pass