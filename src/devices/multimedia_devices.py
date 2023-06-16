from .device import Device
from actors.percentage_adjustable import PercentageAdjustable
from actors.switch_on_offable import SwitchOnOffable

# CCP - AudioDevice und Tv sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class AudioDevice(Device, PercentageAdjustable, SwitchOnOffable):
    
    def __init__(self, name: str):
        print("Audiodevice " + name + " has been created")
        super().__init__(name)
        self.volume = 0
        self.running = False
        self.media = "nothing"

    def setRunning(self, running: bool):
        self.running = running 
        print("AudioDevice " + str(self.name) + " changed running to " + str(running))

    def getPercentage(self) -> int:
        raise NotImplementedError

    def setPercentage(self, percentage: int):
        self.volume = percentage
        print("Audiodevice " + self.name + " set volume to : " + str(percentage))

    def isRunning(self) -> bool:
        return self.isRunning

    def playAudio(self, audioData: str):
        if self.isRunning():
            self.media = audioData
            print("AudioDevice " + str(self.name) + " is playing "+ self.media)

    def simuliereEinenThreadDurchlauf(self):
        print(f"MultimediaDevice {self.name} is {'running' if self.running else 'not running'} with volume {self.volume} and playing {self.media}" )

#LSP - Austauschbarkeit der Klassen: Tv kann anstelle von AudioDevice verwendet werden, ohne die Funktionalität zu beeinträchtigen

class Tv(AudioDevice):
    def __init__(self, name: str):
        print("TV " + name + " has been created")
        super().__init__(name)

    def playVideo(self, videoData: str):
        if self.isRunning():
            self.media = videoData
            print("VideoDevice " + str(self.name) + " is playing video")

