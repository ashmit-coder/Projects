import requests
from bs4 import BeautifulSoup
import pyttsx3 as tts
import webbrowser
from gtts import gTTS
engine = tts.init()
# voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 2)
engine.setProperty('volume', volume+4)
# url = "https://inshorts.com/en/read/"

def edit( inp ):
    url = "https://inshorts.com/en/read/"
    if(inp.lower() == "0"):
        return url
    else:
        url += inp.lower()
        return url

ip = input("tell me what you want(0 if you want it to be random) ") 
ur = edit(ip)
r =requests.get(ur)
soup = BeautifulSoup(r.text, "html.parser")

# a = soup.find(itemprop = "articleBody").next
a = soup.find_all(itemprop = "articleBody")

# for  x in soup.find(itemprop = "articleBody").next_siblings:
#     print(x)
gg = str(a)
h = gg.split("</div>")
t =[]
text = ''
for  x in h:
    try:
        y = x.split('<div itemprop="articleBody">')
        
        text = y[1]
        

        t.append(text)
    except Exception as e:
        pass
# print(len(y))

for x in t:
    text += str(x) + "    " 
 
# print(text)
tts = gTTS(text)

filename = "voice.mp3"
tts.save(filename)
webbrowser.open_new_tab(ur)
import playsound
# python_musical.musical.audio.playback("voice.mp30")
# import playsound
playsound.playsound("voice.mp3")
# import winsound
# winsound.PlaySound("voice.mp3", flags= True)
    
    
    
    


# my_variable = 'hello' # your real code gets this from the chatbot

# engine.say("that was it if you want to more please enter a new subclass")
# engine.runAndWait()
# print(type(a))
# gg = str(a)
# print(gg)