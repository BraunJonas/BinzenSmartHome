import logging
import communication_to_external_systems.weatherstation_adapter
from actors.switch_on_offable import SwitchOnOffable
from devices.device import Device


class FrostHeating(Device, SwitchOnOffable):
    __instance = None
     #Singleton Speicherung in __instance

    def __init__(self):
        #Abfrage ob bereits eine Frostheizung existiert
        if FrostHeating.__instance != None:
            raise Exception("This is a Singleton class")
        super().__init__("Frostheating")
        self.logger = logging.getLogger(__name__)
        self.running = False
        FrostHeating.__instance = self

    #Rückgabe der Frostheizung gemäß Singelton  
    @staticmethod
    def getInstance():
        logger = logging.getLogger(__name__)
        if FrostHeating.__instance == None:
            logger.info("Creating new FrostHeatig instance")
            FrostHeating()
        else:
            logger.info("Instance already existed: returning instance")
        return FrostHeating.__instance

    #Festlegung des Zustandes ob diese gerade läuft
    def setRunning(self, running: bool):
        self.running = running
        self.logger.info("FrostHeating set running to " + str(running))

    #Abfrage ob diese läuft
    def isRunning(self) -> bool:
        return type(self).__instance.running
    
    def decideRunning(self) -> bool:
        #Ask Weather station to decide wether FrostHeating is necessary
        expectedTemp = communication_to_external_systems.weatherstation_adapter.getMinExpectedTemp()
        self.logger.info(f"FrostHeating {self.name} got Info: Expected Temperature = {expectedTemp} degree"  )
        if(expectedTemp < 5):
            return True
        return False

    #Simulation eines Durchlaufs -> Main Klasse
    def simuliereEinenThreadDurchlauf(self):
        self.setRunning(self.decideRunning())
        self.logger.info(f"FrostHeating {self.name} is {'running ' if self.running else 'not running'}" )