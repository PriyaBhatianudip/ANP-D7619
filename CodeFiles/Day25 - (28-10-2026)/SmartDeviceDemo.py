class VoiceAssistant:
    def startWork(self):
        print("VoiceAssistant:Starting voice control functionality")

class SmartDevice:
    def startWork(self):
        print("SmartDevice:Starting Smart device functionality")


class SmartSpeaker(VoiceAssistant, SmartDevice):
    pass

ss = SmartSpeaker()
mrolist = SmartSpeaker.mro()
print(mrolist)
mrolist[2].startWork(ss)
