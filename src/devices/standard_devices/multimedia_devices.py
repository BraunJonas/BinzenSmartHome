import logging
from actors.percentage_adjustable import PercentageAdjustable
from actors.switch_on_offable import SwitchOnOffable
from devices.device_communication.event_listener import EventListener
from devices.device_communication.event_manager import EventManager
from devices.device import Device


# CCP - AudioDevice und Tv sind geschlossen gegenüber der selben Art von Veränderungen und sind deshalb in einem Modul zusammengefasst

class AudioDevice(Device, PercentageAdjustable, SwitchOnOffable, EventListener):
    
    def __init__(self, name: str):
        super().__init__("AudioDevice: " + name)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Audiodevice " + name + " has been created")
        self.volume = 0
        self.running = False
        self.media = "nothing"
        self.reactToAlarms = False

    #Festlegung ob device auf alarem reagiert -> Observer
    def setReactToAlarms(self,react: bool):
        self.reactToAlarms = react
        if react:
            EventManager.subscribe(self,"alarm")
        else:
            EventManager.unsubscribe(self,"alarm")
    
    #Rückgabe der alarmfestlegung
    def getReactToAlarms(self)-> bool:
        return self.reactToAlarms

    #Verhalten des loggings bei alarm 
    def notify(self,event: str, additionalInformation: str):
        if(event == "alarm"):
            self.logger.info("AudioDevice " + str(self.name) + " is reading Alarmmessage: "+ additionalInformation)

    #Prüfen ob diese läuft
    def setRunning(self, running: bool):
        self.running = running 
        self.logger.info("AudioDevice " + str(self.name) + " changed running to " + str(running))

    #rückgabe eines lautstärke wertes
    def getPercentage(self) -> int:
        return self.volume

    #Festlegugn eiens lautstärkewertes
    def setPercentage(self, percentage: int):
        self.volume = percentage
        self.logger.info("AudioDevice " + str(self.name) + " set volume to : " + str(percentage))

    #Rückgabe ib dies läuft
    def isRunning(self) -> bool:
        return self.running

    #Aktion das diese etwas abspielt
    def playAudio(self, audioData: str):
        if self.isRunning():
            self.media = audioData
            self.logger.info("AudioDevice " + str(self.name) + " is playing "+ self.media)
        else:
            self.logger.info(f"AudioDevice {self.name} is turned off")
     
     #Simulation eines Durchlaufs -> Main Klasse   
    def simuliereEinenThreadDurchlauf(self):
        self.logger.info(f"MultimediaDevice {self.name} is {f'running with volume {self.volume} and playing {self.media}' if self.running else 'not running'}")

    #klonieren gemäß Prototype
    def clone(self, name: str):
        clone = AudioDevice(name)
        clone.setRunning(self.running)
        clone.setPercentage(self.volume)
        return clone


#LSP - Austauschbarkeit der Klassen: Tv kann anstelle von AudioDevice verwendet werden, ohne die Funktionalität zu beeinträchtigen

class Tv(AudioDevice):
    def __init__(self, name: str):
        super().__init__("(TV): " + name)
        self.logger.info("TV " + name + " has been created")

    #Abspielen eines videos
    def playVideo(self, videoData: str):
        if self.isRunning():
            self.media = videoData
            self.logger.info("TV " + str(self.name) + " is playing video")
        else:
            self.logger.info(f"TV {self.name} is turned off")

    #klonieren gemäß Prototype
    def clone(self, name: str):
        clone = Tv(name)
        clone.setRunning(self.running)
        clone.setPercentage(self.volume)
        return clone

