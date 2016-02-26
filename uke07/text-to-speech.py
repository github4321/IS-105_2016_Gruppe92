import pyttsx
engine = pyttsx.init()

voices = engine.getProperty('voices')
print len(voices)
for voice in voices:
    print "Using voice:", repr(voice)
    engine.setProperty('voice', voice.id)
    engine.say("You may not enter this class")
engine.runAndWait()