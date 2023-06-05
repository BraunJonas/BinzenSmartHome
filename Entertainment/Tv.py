from Entertainment import AudioDevice

class Tv(AudioDevice):
    def __init__(self, name:str):
        print("TV "+ name +" has been created")
        super().__init__(name)

    def playVideo(self):
        if(self.isRunning()):
            print("AudioDevice "+str(self.name) + " is playing video")
