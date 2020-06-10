from gtts import gTTS

f=open("1.txt")
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("1.mp3")

