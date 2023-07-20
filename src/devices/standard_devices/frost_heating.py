import logging
import src.communication_to_external_systems.weatherstation_adapter
from src.actors.switch_on_offable import SwitchOnOffable
from src.devices.device import Device


class FrostHeating(Device, SwitchOnOffable):
    __instance = None
     #Singleton

    def __init__(self):
        if FrostHeating.__instance != None:
            raise Exception("This is a Singleton class")
        super().__init__("Frostheating")
        self.logger = logging.getLogger(__name__)
        self.running = False
        FrostHeating.__instance = self

    @staticmethod
    def getInstance():
        logger = logging.getLogger(__name__)
        if FrostHeating.__instance == None:
            logger.info("Creating new FrostHeatig instance")
            FrostHeating()
        else:
            logger.info("Instance already existed: returning instance")
        return FrostHeating.__instance


    def setRunning(self, running: bool):
        self.running = running
        self.logger.info("FrostHeating set running to " + str(running))

    def isRunning(self) -> bool:
        return type(self).__instance.running
    
    def decideRunning(self) -> bool:
        #Ask Weather station to decide wether FrostHeating is necessary
        expectedTemp = src.communication_to_external_systems.weatherstation_adapter.getMinExpectedTemp()
        self.logger.info(f"FrostHeating {self.name} got Info: Expected Temperature = {expectedTemp} degree"  )
        if(expectedTemp < 5):
            return True
        return False

    
    def simuliereEinenThreadDurchlauf(self):
        self.setRunning(self.decideRunning())
        self.logger.info(f"FrostHeating {self.name} is {'running ' if self.running else 'not running'}" )