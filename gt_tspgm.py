#pip install gtts
import os
from gtts import gTTS
a=input("Enter your text")
g=gTTS(text=a,lang="en")
g.save("Sample.mp3")
os.system("start Sample.mp3")
