import pyttsx3 as tts
engine = tts.init()
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-1.5)
engine.setProperty('volume', volume+4)
fil = open(f"{}.txt","r")
sentence = ' """ ' + f'{fil.read()}' + ' """ '

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.setProperty('voice', voice.id)
    engine.say(sentence)
engine.runAndWait()