import logging
from src.actors.percentage_adjustable import PercentageAdjustable
from src.actors.switch_on_offable import SwitchOnOffable
from src.devices.device_communication.event_listener import EventListerner
from src.devices.device_communication.event_manager import EventManager

from src.devices.device import Device


# CCP - AudioDevice und Tv sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class AudioDevice(Device, PercentageAdjustable, SwitchOnOffable, EventListerner):
    
    def __init__(self, name: str):
        super().__init__("TV: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Audiodevice " + name + " has been created")
        self.volume = 0
        self.running = False
        self.media = "nothing"
        self.reactToAlarms = False

    def setReactToAlarms(self,react: bool):
        self.reactToAlarms = react
        if react:
            EventManager.subscribe(self,"alarm")
        else:
            EventManager.unsubscribe(self,"alarm")
    
    def getReactToAlarms(self)-> bool:
        return self.reactToAlarms

    def notify(self,event: str, additionalInformation: str):
        if(event == "alarm"):
            self.logger.info("AudioDevice " + str(self.name) + " is reading Alarmmessage: "+ additionalInformation)

    def setRunning(self, running: bool):
        self.running = running 
        self.logger.info("AudioDevice " + str(self.name) + " changed running to " + str(running))

    def getPercentage(self) -> int:
        return self.volume

    def setPercentage(self, percentage: int):
        self.volume = percentage
        self.logger.info("Audiodevice " + str(self.name) + " set volume to : " + str(percentage))

    def isRunning(self) -> bool:
        return self.running

    def playAudio(self, audioData: str):
        if self.isRunning():
            self.media = audioData
            self.logger.info("AudioDevice " + str(self.name) + " is playing "+ self.media)
        else:
            self.logger.info(f"AudioDevice {self.name} is turned off")
        
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"MultimediaDevice {self.name} is {f'running with volume {self.volume} and playing {self.media}' if self.running else 'not running'}")

    def clone(self, name: str):
        clone = AudioDevice(name)
        clone.setRunning(self.running)
        clone.setPercentage(self.volume)
        return clone


#LSP - Austauschbarkeit der Klassen: Tv kann anstelle von AudioDevice verwendet werden, ohne die Funktionalität zu beeinträchtigen

class Tv(AudioDevice):
    def __init__(self, name: str):
        super().__init__("Tv: " + name)
        self.logger.info("TV " + name + " has been created")

    def playVideo(self, videoData: str):
        if self.isRunning():
            self.media = videoData
            self.logger.info("VideoDevice " + str(self.name) + " is playing video")
        else:
            self.logger.info(f"VideoDevice {self.name} is turned off")

    def clone(self, name: str):
        clone = Tv(name)
        clone.setRunning(self.running)
        clone.setPercentage(self.volume)
        return clone

